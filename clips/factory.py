#!/usr/bin/env python3
"""
AECODE Clip Factory — «Historias de la IA» sobre MoneyPrinterTurbo.

Por episodio:
  1. Voz        MPT voice.tts con el proveedor offline `piper:` (es_MX)      -> voice.mp3 + tiempos
  2. Subtítulos MPT voice.create_subtitle (una línea por cláusula)            -> subtitle.srt
  3. Escenas    engine/stage.html renderizado cuadro a cuadro (Playwright)    -> visual.mp4
  4. Música     music.build_bed: cama original + whoosh + ducking             -> bed.wav
  5. Montaje    MPT video.generate_video: subtítulos AECODE + mezcla          -> mpt.mp4
  6. Master     loudnorm -14 LUFS (redes) + faststart + portada               -> output/

Uso:
  python clips/factory.py                 # los 3 episodios
  python clips/factory.py --only 2        # solo el episodio 2
  python clips/factory.py --preview       # solo fotogramas de control, sin video
"""

import argparse
import base64
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time
import wave
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MPT = ROOT / "MoneyPrinterTurbo"
sys.path.insert(0, str(MPT))
sys.path.insert(0, str(HERE))

from app.config import config  # noqa: E402

import episodes as E  # noqa: E402
import music  # noqa: E402

VOICE = os.environ.get("AECODE_VOICE", "piper:es_MX-claude-high")
VOICE_RATE = float(os.environ.get("AECODE_VOICE_RATE", "1.1"))
FPS = 30
LEAD = 0.12   # el corte visual se adelanta a la voz (se siente más ágil)
TAIL = 2.6    # segundos de cierre con la tarjeta final después de la voz
STAGE = HERE / "engine" / "stage.html"
WORK = HERE / ".work"
OUT = HERE / "output"

config.piper["models_dir"] = os.environ.get("AECODE_PIPER_MODELS", str(MPT / "models" / "piper"))
config.piper["sentence_pause"] = 0.34
config.piper["lexicon"] = E.LEXICON
config.app["subtitle_provider"] = "edge"  # usa los tiempos del SubMaker, sin Whisper

from app.models.schema import VideoParams  # noqa: E402
from app.services import video as mpt_video  # noqa: E402
from app.services import voice  # noqa: E402
from app.utils import utils  # noqa: E402

FFMPEG = utils.get_ffmpeg_binary()

# MPT escribe con los valores por defecto de libx264 (crf 23). Para gradientes
# y tipografía fina subimos la calidad sin tocar el código vendorizado.
_write = mpt_video._write_videofile_with_codec_fallback


def _write_hq(clip, output_file, codec, **kwargs):
    kwargs.setdefault("ffmpeg_params", ["-crf", "17", "-pix_fmt", "yuv420p", "-tune", "animation"])
    kwargs.setdefault("preset", "medium")
    return _write(clip, output_file, codec, **kwargs)


mpt_video._write_videofile_with_codec_fallback = _write_hq


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ------------------------------------------------------------------ audio
def decode_mono(path, sr=16000):
    raw = subprocess.run(
        [FFMPEG, "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, dtype=np.float32), sr


def speech_intervals(samples, sr, frame=0.02, gap=0.25):
    n = int(frame * sr)
    frames = samples[: len(samples) // n * n].reshape(-1, n)
    rms = np.sqrt((frames ** 2).mean(axis=1))
    on = rms > max(0.012, rms.max() * 0.06)
    spans, start = [], None
    for i, v in enumerate(on):
        t = i * frame
        if v and start is None:
            start = t
        elif not v and start is not None:
            spans.append([start, t])
            start = None
    if start is not None:
        spans.append([start, len(on) * frame])
    merged = []
    for s in spans:
        if merged and s[0] - merged[-1][1] < gap:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    active = samples[np.abs(samples) > 0.01]
    return merged, float(np.sqrt((active ** 2).mean())) if active.size else 0.1


def write_wav(path, stereo, sr=music.SR):
    pcm = (np.clip(stereo.T, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())


# ------------------------------------------------------------------ timeline
def build_timeline(ep, sub_maker, audio_duration):
    clauses = [(o[0] / 1e7, o[1] / 1e7, t) for o, t in zip(sub_maker.offset, sub_maker.subs)]
    scenes, k = [], 0
    for sc in ep["scenes"]:
        n = len(utils.split_string_by_punctuations(voice._format_text(sc["say"])))
        scenes.append(dict(sc, _clauses=clauses[k:k + n]))
        k += n
    if k != len(clauses):
        raise RuntimeError(f"clauses mismatch: {k} scene clauses vs {len(clauses)} in audio")

    duration = round(audio_duration + TAIL, 3)
    for i, sc in enumerate(scenes):
        sc["start"] = 0.0 if i == 0 else max(0.0, sc["_clauses"][0][0] - LEAD)
    for i, sc in enumerate(scenes):
        sc["end"] = scenes[i + 1]["start"] if i + 1 < len(scenes) else duration
        sc["clauses"] = [[a - sc["start"], b - sc["start"], t] for a, b, t in sc.pop("_clauses")]
    return scenes, duration


def filter_srt(src, dst, until):
    """Quita los subtítulos del cierre: la tarjeta final ya muestra el texto."""
    blocks = [b for b in Path(src).read_text(encoding="utf-8").strip().split("\n\n") if b.strip()]
    keep = []
    for b in blocks:
        lines = b.splitlines()
        h, m, s = re.match(r"(\d+):(\d+):(\d+),", lines[1]).groups()
        start = int(h) * 3600 + int(m) * 60 + int(s) + int(lines[1][9:12]) / 1000
        if start < until - 0.05:
            keep.append("\n".join([str(len(keep) + 1)] + lines[1:]))
    Path(dst).write_text("\n\n".join(keep) + "\n", encoding="utf-8")


# ------------------------------------------------------------------ render
def chromium_path():
    env = os.environ.get("AECODE_CHROMIUM")
    if env:
        return env
    hits = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
    return hits[-1] if hits else None


def render_visual(payload, duration, out_mp4, cover_png=None, cover_t=None, preview=None):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=chromium_path(),
            args=["--font-render-hinting=none", "--disable-lcd-text", "--force-color-profile=srgb"],
        )
        page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        page.goto(STAGE.as_uri())
        page.evaluate("d => load(d)", payload)
        page.wait_for_function("window.__ready === true", timeout=20000)

        if preview:
            for t, path in preview:
                page.evaluate(f"seek({t})")
                page.screenshot(path=str(path))
            browser.close()
            return

        # Captura por CDP con optimizeForSpeed: PNG sin pérdida ~2.5x más rápido.
        cdp = page.context.new_cdp_session(page)
        shot = {"format": "png", "optimizeForSpeed": True}
        frames = int(round(duration * FPS))
        enc = subprocess.Popen(
            [FFMPEG, "-y", "-v", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
             "-c:v", "libx264", "-preset", "medium", "-crf", "14", "-tune", "animation",
             "-pix_fmt", "yuv420p", "-r", str(FPS), str(out_mp4)],
            stdin=subprocess.PIPE,
        )
        cover_frame = int(round(cover_t * FPS)) if cover_t is not None else -1
        t0 = time.time()
        for i in range(frames):
            page.evaluate(f"seek({i / FPS})")
            png = base64.b64decode(cdp.send("Page.captureScreenshot", shot)["data"])
            enc.stdin.write(png)
            if i == cover_frame and cover_png:
                Path(cover_png).write_bytes(png)
            if i and i % (FPS * 10) == 0:
                log(f"  frames {i}/{frames} ({(time.time() - t0) / i * 1000:.0f} ms/frame)")
        enc.stdin.close()
        enc.wait()
        browser.close()
        if enc.returncode:
            raise RuntimeError("ffmpeg frame encode failed")


# ------------------------------------------------------------------ episodio
def build_episode(ep, preview=False):
    slug = ep["slug"]
    work = WORK / slug
    work.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    script = " ".join(s["say"] for s in ep["scenes"])

    log(f"{slug}: voz ({VOICE}, x{VOICE_RATE})")
    audio = work / "voice.mp3"
    sub_maker = voice.tts(text=script, voice_name=VOICE, voice_rate=VOICE_RATE, voice_file=str(audio))
    if sub_maker is None:
        raise RuntimeError("TTS failed: ¿descargaste el modelo Piper? (clips/setup_voice.sh)")
    srt_full = work / "subtitle.srt"
    voice.create_subtitle(sub_maker=sub_maker, text=script, subtitle_file=str(srt_full))
    audio_duration = voice.get_audio_duration(str(audio))

    scenes, duration = build_timeline(ep, sub_maker, audio_duration)
    cta_start = scenes[-1]["start"]
    payload = dict(
        series=E.SERIES, total=E.TOTAL, duration=duration,
        episode=dict(number=ep["number"], title=ep["title"], next_title=ep["next_title"]),
        scenes=scenes,
    )
    (work / "timeline.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"{slug}: {len(scenes)} escenas, {duration:.1f}s")

    if preview:
        shots = []
        for i, sc in enumerate(scenes):
            t = min(sc["end"] - 0.3, sc["start"] + max(1.6, (sc["end"] - sc["start"]) * 0.85))
            shots.append((round(t, 2), work / f"preview-{i:02d}-{sc['type']}.png"))
        render_visual(payload, duration, None, preview=shots)
        log(f"{slug}: previews en {work}")
        return [p for _, p in shots]

    log(f"{slug}: render de escenas")
    visual = work / "visual.mp4"
    cover = OUT / f"{slug}-portada.png"
    hook = scenes[0]
    render_visual(payload, duration, visual, cover_png=cover, cover_t=hook["end"] - 0.4)

    log(f"{slug}: música original")
    mono, sr = decode_mono(audio)
    spans, voice_rms = speech_intervals(mono, sr)
    bed = music.build_bed(duration, [s["start"] for s in scenes], spans, cta_start, voice_rms)
    bed_wav = work / "bed.wav"
    write_wav(bed_wav, bed)

    log(f"{slug}: montaje MoneyPrinterTurbo")
    srt = work / "subtitle.cta-free.srt"
    filter_srt(srt_full, srt, cta_start)
    params = VideoParams(
        video_subject=ep["title"],
        video_script=script,
        video_aspect="9:16",
        voice_name=VOICE,
        voice_volume=1.0,
        bgm_type="custom",
        bgm_file=str(bed_wav),
        bgm_volume=1.0,
        subtitle_enabled=True,
        subtitle_position="custom",
        custom_position=76.0,
        subtitle_animation="none",
        font_name="Manrope-ExtraBold.ttf",
        font_size=54,
        text_fore_color="#FFFFFF",
        stroke_color="#0E1121",
        stroke_width=0,
        text_background_color="#4A3AC1",
        rounded_subtitle_background=True,
        n_threads=4,
    )
    mpt_out = work / "mpt.mp4"
    mpt_video.generate_video(
        video_path=str(visual), audio_path=str(audio), subtitle_path=str(srt),
        output_file=str(mpt_out), params=params, bgm_file_override=str(bed_wav),
    )

    log(f"{slug}: master -14 LUFS")
    final = OUT / f"{slug}.mp4"
    subprocess.run(
        [FFMPEG, "-y", "-v", "error", "-i", str(mpt_out), "-c:v", "copy",
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(final)],
        check=True,
    )
    shutil.copy(srt_full, OUT / f"{slug}.srt")
    log(f"{slug}: listo -> {final}")
    return final


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", type=int, action="append", help="número de episodio (repetible)")
    ap.add_argument("--preview", action="store_true", help="solo fotogramas de control")
    args = ap.parse_args()
    for ep in E.EPISODES:
        if args.only and ep["number"] not in args.only:
            continue
        build_episode(ep, preview=args.preview)


if __name__ == "__main__":
    main()
