"""
Offline Piper TTS engine (via sherpa-onnx).

Piper voices are small VITS models that run on CPU in real time, with no API
key and no network once the model is on disk. This module only knows how to
load a voice and turn sentences into PCM; ``voice.piper_tts`` owns the
MoneyPrinterTurbo contract (SubMaker, subtitle alignment, output file).

Model layout (the tarballs published at
https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models)::

    <models_dir>/vits-piper-<voice>/<voice>.onnx
    <models_dir>/vits-piper-<voice>/tokens.txt
    <models_dir>/vits-piper-<voice>/espeak-ng-data/

Config (``config.toml``)::

    [piper]
    models_dir = "./models/piper"   # relative to the project root
    sentence_pause = 0.32           # seconds of silence between sentences
    num_threads = 4
    # Spoken form for words the phonemizer reads badly. Only the audio uses
    # it; subtitles keep the original spelling.
    lexicon = { "ChatGPT" = "Chat ye pe te", "IA" = "i a" }
"""

import os
import re
import threading

import numpy as np

from app.config import config
from app.utils import utils

_tts_cache: dict[str, object] = {}
_tts_lock = threading.Lock()


def models_dir() -> str:
    configured = str(config.piper.get("models_dir", "") or "").strip()
    if not configured:
        return os.path.join(utils.root_dir(), "models", "piper")
    if os.path.isabs(configured):
        return configured
    return os.path.join(utils.root_dir(), configured)


def voice_dir(voice: str) -> str:
    return os.path.join(models_dir(), f"vits-piper-{voice}")


def list_voices() -> list[str]:
    root = models_dir()
    if not os.path.isdir(root):
        return []
    voices = []
    for name in sorted(os.listdir(root)):
        if name.startswith("vits-piper-") and os.path.isfile(
            os.path.join(root, name, "tokens.txt")
        ):
            voices.append(name[len("vits-piper-"):])
    return voices


def _load(voice: str):
    with _tts_lock:
        if voice in _tts_cache:
            return _tts_cache[voice]

        import sherpa_onnx

        d = voice_dir(voice)
        model = os.path.join(d, f"{voice}.onnx")
        if not os.path.isfile(model):
            raise FileNotFoundError(
                f"piper voice not found: {model}. Download vits-piper-{voice}.tar.bz2 "
                "from https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models"
            )
        tts_config = sherpa_onnx.OfflineTtsConfig(
            model=sherpa_onnx.OfflineTtsModelConfig(
                vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                    model=model,
                    tokens=os.path.join(d, "tokens.txt"),
                    data_dir=os.path.join(d, "espeak-ng-data"),
                ),
                num_threads=int(config.piper.get("num_threads", 4)),
            ),
            max_num_sentences=1,
        )
        tts = sherpa_onnx.OfflineTts(tts_config)
        _tts_cache[voice] = tts
        return tts


def apply_lexicon(text: str) -> str:
    lexicon = config.piper.get("lexicon", {}) or {}
    for written, spoken in lexicon.items():
        text = re.sub(rf"(?<!\w){re.escape(written)}(?!\w)", spoken, text)
    return text


def synthesize(text: str, voice: str, speed: float = 1.0) -> tuple[np.ndarray, int]:
    """Return mono float32 samples in [-1, 1] and the sample rate."""
    tts = _load(voice)
    audio = tts.generate(apply_lexicon(text), sid=0, speed=float(speed or 1.0))
    samples = np.asarray(audio.samples, dtype=np.float32)
    return samples, int(audio.sample_rate)


def spoken_length(text: str) -> float:
    """Approximate spoken length in characters: lexicon applied, digits read out."""
    text = apply_lexicon(text)

    def expand(match):
        digits = match.group(0).replace(" ", "")
        try:
            from num2words import num2words

            return num2words(int(digits), lang="es")
        except Exception:
            return "x" * int(len(digits) * 3.5)

    text = re.sub(r"\d+(?: \d{3})*", expand, text)
    return float(len(text))


def clause_boundaries(samples: np.ndarray, sample_rate: int, weights: list[float]) -> list[float]:
    """
    Times (s) where each clause after the first starts inside one sentence.

    First guess: split the speech by the spoken length of each clause. Then
    snap every guess to the nearest real pause (commas make Piper breathe),
    so subtitles and on-screen reveals land on what the voice actually says.
    """
    duration = len(samples) / sample_rate
    total = sum(weights) or 1.0
    guesses, acc = [], 0.0
    for w in weights[:-1]:
        acc += w
        guesses.append(duration * acc / total)
    if not guesses:
        return []

    frame = int(0.01 * sample_rate)
    frames = samples[: len(samples) // frame * frame].reshape(-1, frame)
    rms = np.sqrt((frames ** 2).mean(axis=1))
    quiet = rms < max(1e-4, rms.max() * 0.05)
    pauses, start = [], None
    for i, q in enumerate(quiet):
        if q and start is None:
            start = i
        elif not q and start is not None:
            if i - start >= 6:  # >= 60 ms
                pauses.append(((start + i) / 2 * 0.01, (i - start) * 0.01))
            start = None

    points, floor = [], 0.0
    for index, guess in enumerate(guesses):
        # A clause never lasts much less than its spoken length suggests;
        # this skips the short closures of stop consonants (p, t, k).
        min_len = max(0.15, 0.55 * duration * weights[index] / total)
        best = None
        for center, length in pauses:
            dist = abs(center - guess)
            if center > floor + min_len and dist < 0.7:
                score = dist - length * 2  # prefer longer pauses
                if best is None or score < best[0]:
                    best = (score, center)
        point = best[1] if best else guess
        point = max(point, floor + 0.15)
        points.append(point)
        floor = point
    return points


def trim_silence(samples: np.ndarray, sample_rate: int, threshold: float = 0.01) -> np.ndarray:
    """Drop leading/trailing near-silence so our own pauses stay predictable."""
    loud = np.flatnonzero(np.abs(samples) > threshold)
    if loud.size == 0:
        return samples
    pad = int(0.03 * sample_rate)
    start = max(0, loud[0] - pad)
    end = min(len(samples), loud[-1] + pad)
    return samples[start:end]
