"""
Cama musical original para la serie (100 % sintetizada aquí: sin licencias).

Pad cálido + arpegio suave + pulso ligero, en Re menor (Dm9 · B♭maj7 · Fmaj7 · C6/9).
Incluye whoosh en cada corte de escena, un chime en el cierre y ducking:
la música baja mientras habla la voz y respira en las pausas.
"""

import numpy as np
from scipy import signal

SR = 44100
BPM = 100
BEAT = 60 / BPM
BAR = 4 * BEAT

CHORDS = [  # (bajo, notas del pad, notas del arpegio) en MIDI
    (38, [50, 53, 57, 60, 64], [62, 65, 69, 72, 76, 72, 69, 65]),  # Dm9
    (34, [50, 53, 57, 58, 62], [62, 65, 69, 70, 74, 70, 69, 65]),  # Bbmaj7
    (41, [53, 57, 60, 64, 67], [65, 69, 72, 76, 79, 76, 72, 69]),  # Fmaj7
    (36, [52, 55, 57, 62, 64], [64, 67, 69, 74, 76, 74, 69, 67]),  # C6/9
]


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def _lowpass(x, cutoff, order=2):
    b, a = signal.butter(order, cutoff / (SR / 2), "low")
    return signal.lfilter(b, a, x)


def _saw(freq, n, phase=0.0):
    t = np.arange(n) / SR
    return signal.sawtooth(2 * np.pi * freq * t + phase)


def _pad(total_n, rng):
    out = np.zeros((2, total_n))
    bar_n = int(BAR * SR)
    fade = int(0.9 * SR)
    for i, start in enumerate(range(0, total_n, bar_n)):
        _, notes, _ = CHORDS[i % len(CHORDS)]
        n = min(bar_n + fade, total_n - start)
        env = np.ones(n)
        env[:fade] = np.linspace(0, 1, fade) ** 1.5
        env[-fade:] *= np.linspace(1, 0, fade) ** 1.5
        for ch in range(2):
            voice = np.zeros(n)
            for m in notes:
                for cents in (-9, 0, 8):
                    detune = cents + (4 if ch else -4)
                    voice += _saw(hz(m) * 2 ** (detune / 1200), n, rng.uniform(0, 6.28))
            out[ch, start:start + n] += _lowpass(voice, 900) * env
    return out / 60


def _pluck(freq, n):
    t = np.arange(n) / SR
    tone = np.sin(2 * np.pi * freq * t) + 0.35 * np.sin(4 * np.pi * freq * t) + 0.1 * np.sin(6 * np.pi * freq * t)
    return tone * np.exp(-t * 9) * np.minimum(1, t * 400)


def _arp(total_n, start_s):
    out = np.zeros((2, total_n))
    step = BEAT / 2
    note_n = int(0.6 * SR)
    t = start_s
    k = 0
    while t < total_n / SR:
        bar = int(t // BAR)
        _, _, arp = CHORDS[bar % len(CHORDS)]
        m = arp[k % len(arp)]
        i = int(t * SR)
        n = min(note_n, total_n - i)
        if n <= 0:
            break
        x = _pluck(hz(m), n) * (0.9 if k % 4 == 0 else 0.6)
        pan = 0.5 + 0.35 * np.sin(k * 0.9)
        out[0, i:i + n] += x * (1 - pan)
        out[1, i:i + n] += x * pan
        # eco a 3/8 de pulso, al lado contrario
        d = int(0.75 * BEAT * SR)
        if i + d < total_n:
            m2 = min(n, total_n - i - d)
            out[0, i + d:i + d + m2] += x[:m2] * pan * 0.35
            out[1, i + d:i + d + m2] += x[:m2] * (1 - pan) * 0.35
        t += step
        k += 1
    return out * 0.11


def _pulse(total_n, start_s, stop_s, rng):
    out = np.zeros(total_n)
    kick_n = int(0.35 * SR)
    kt = np.arange(kick_n) / SR
    kick = np.sin(2 * np.pi * (48 * kt + 30 * (1 - np.exp(-kt * 30)) / 30)) * np.exp(-kt * 9)
    hat_n = int(0.05 * SR)
    b, a = signal.butter(2, 7000 / (SR / 2), "high")
    t = start_s
    k = 0
    while t < min(stop_s, total_n / SR):
        i = int(t * SR)
        if k % 4 in (0, 2) and i + kick_n < total_n:
            out[i:i + kick_n] += kick * 0.55
        if k % 2 == 1 and i + hat_n < total_n:
            hat = signal.lfilter(b, a, rng.standard_normal(hat_n)) * np.exp(-np.arange(hat_n) / SR * 90)
            out[i:i + hat_n] += hat * 0.12
        t += BEAT / 2
        k += 1
    return np.vstack([out, out]) * 0.5


def _sub(total_n):
    out = np.zeros(total_n)
    bar_n = int(BAR * SR)
    for i, start in enumerate(range(0, total_n, bar_n)):
        root = CHORDS[i % len(CHORDS)][0]
        n = min(bar_n, total_n - start)
        t = np.arange(n) / SR
        env = np.minimum(1, t / 0.25) * np.minimum(1, (n / SR - t) / 0.25)
        out[start:start + n] += np.sin(2 * np.pi * hz(root) * t) * env
    return np.vstack([out, out]) * 0.10


def _reverb(x, rng, seconds=2.6, wet=0.28):
    n = int(seconds * SR)
    t = np.arange(n) / SR
    out = np.empty_like(x)
    for ch in range(2):
        ir = rng.standard_normal(n) * np.exp(-t * 3.2)
        ir = _lowpass(ir, 5000)
        ir /= np.sqrt(np.sum(ir ** 2))
        out[ch] = signal.fftconvolve(x[ch], ir)[: x.shape[1]]
    return x * (1 - wet) + out * wet


def _whoosh(rng):
    n = int(0.55 * SR)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    out = np.zeros(n)
    # barrido de paso banda 300 Hz -> 3.5 kHz por bloques
    blocks = 22
    size = n // blocks
    for k in range(blocks):
        f = 300 * (3500 / 300) ** (k / blocks)
        b, a = signal.butter(2, [f * 0.7 / (SR / 2), min(f * 1.4, SR / 2 - 100) / (SR / 2)], "band")
        seg = signal.lfilter(b, a, noise[k * size:(k + 1) * size + 1000])[:size]
        out[k * size:(k + 1) * size] = seg
    env = np.sin(np.pi * np.clip(t / (n / SR), 0, 1)) ** 2
    return out * env * 0.35


def _chime():
    n = int(2.2 * SR)
    t = np.arange(n) / SR
    x = np.zeros(n)
    for m, g in ((74, 1.0), (81, 0.6), (86, 0.35)):
        x += g * np.sin(2 * np.pi * hz(m) * t) * np.exp(-t * 2.2)
    return x * np.minimum(1, t * 300) * 0.22


def _envelope(points, total_n):
    """points: [(t, gain)] -> curva suave por muestra."""
    ts = np.array([p[0] for p in points]) * SR
    gs = np.array([p[1] for p in points])
    curve = np.interp(np.arange(total_n), ts, gs)
    k = int(0.18 * SR)
    kernel = np.hanning(k) / np.hanning(k).sum()
    return np.convolve(curve, kernel, mode="same")


def build_bed(duration, scene_starts, speech, cta_start, voice_rms, seed=7):
    """
    duration      duración total (s)
    scene_starts  inicios de escena (s): whoosh en cada corte
    speech        [(inicio, fin)] con voz: ducking
    cta_start     inicio del cierre: entra el chime y sale el pulso
    voice_rms     RMS de la voz; la cama queda ~15 dB por debajo al hablar
    Devuelve un array (2, n) float32.
    """
    rng = np.random.default_rng(seed)
    n = int(duration * SR)
    music = _pad(n, rng) + _sub(n) + _arp(n, start_s=BAR * 0.5) + _pulse(n, BAR, cta_start, rng)
    music = _reverb(music, rng)

    # ducking: -7 dB bajo la voz, 0 dB en pausas y cierre
    duck = 10 ** (-7 / 20)
    pts = [(0, duck)]
    for a, b in speech:
        pts += [(a - 0.05, duck), (b + 0.05, duck)]
    pts.append((cta_start + 0.4, 1.0))
    pts.append((duration, 1.0))
    # entre frases largas (>0.6 s) la música respira
    speech = sorted(speech)
    for (a1, b1), (a2, b2) in zip(speech, speech[1:]):
        if a2 - b1 > 0.6:
            pts += [(b1 + 0.15, 1.0), (a2 - 0.15, 1.0)]
    pts.sort()
    music *= _envelope(pts, n)

    fx = np.zeros((2, n))
    w = _whoosh(rng)
    for s in scene_starts[1:]:
        i = int((s - 0.4) * SR)
        if 0 <= i and i + len(w) < n:
            fx[0, i:i + len(w)] += w
            fx[1, i:i + len(w)] += w[::-1] * 0.8 + w * 0.2
    c = _chime()
    i = int((cta_start + 0.3) * SR)
    m = min(len(c), n - i)
    if m > 0:
        fx[0, i:i + m] += c[:m]
        fx[1, i:i + m] += c[:m]

    # nivel: cama (sin efectos) ~15 dB bajo la voz
    rms = np.sqrt(np.mean(music ** 2)) + 1e-9
    music *= (voice_rms * 10 ** (-15 / 20)) / rms
    fx *= voice_rms / (np.sqrt(np.mean(w ** 2)) + 1e-9) * 10 ** (-17 / 20)
    bed = music + fx

    # fades de entrada/salida
    fi, fo = int(0.3 * SR), int(1.8 * SR)
    bed[:, :fi] *= np.linspace(0, 1, fi)
    bed[:, -fo:] *= np.linspace(1, 0, fo)
    peak = np.max(np.abs(bed))
    if peak > 0.95:
        bed *= 0.95 / peak
    return bed.astype(np.float32)
