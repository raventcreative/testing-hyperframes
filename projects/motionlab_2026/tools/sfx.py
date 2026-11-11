"""Synthesised SFX for the MASTER PAJAK 15 s motion preview (no samples, no music, per the client's rule). Deterministic.
Every cut on the 120 BPM grid gets its own whoosh flavour; pops on chips/stars, ticks on the typewriter, impact on the puzzle snap,
shimmer + soft impact on the M-to-wordmark outro. Writes assets/audio/sfx.wav (48 kHz mono, 15 s). Run: python3 tools/sfx.py ."""
import sys, wave
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000; TOTAL = 15.0; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(11)
def put(t, x, g=1.0):
    i = int(t * SR); j = min(N, i + len(x))
    if i < 0 or i >= N: return
    out[i:j] += g * x[: j - i]

def svf_bp(x, f, q=1.2):
    """state-variable band-pass with a per-sample centre frequency"""
    y = np.zeros_like(x); lo = bp = 0.0
    fs = 2 * np.sin(np.pi * np.clip(f, 20, SR / 6) / SR); d = 1.0 / q
    for n in range(len(x)):
        hp = x[n] - lo - d * bp; bp += fs[n] * hp; lo += fs[n] * bp; y[n] = bp
    return y

def env(n, a=0.35, shape=2.0):
    u = np.linspace(0, 1, n); k = int(n * a)
    e = np.ones(n); e[:k] = np.sin(np.linspace(0, np.pi / 2, k)) ** shape; e[k:] = np.cos(np.linspace(0, np.pi / 2, n - k)) ** shape
    return e

def whoosh(dur=0.6, f0=300, f1=2600, q=1.1, a=0.45):
    n = int(dur * SR); u = np.linspace(0, 1, n)
    f = f0 * (f1 / f0) ** (np.sin(np.pi * u * 0.5) ** 1.3)
    x = svf_bp(rng.standard_normal(n), f, q) * env(n, a)
    return x / (np.abs(x).max() + 1e-9)

def boom(dur=1.4, f0=95, f1=38):
    n = int(dur * SR); t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR
    x = np.sin(ph) * np.exp(-t * 3.2)
    nb = svf_bp(rng.standard_normal(n), np.full(n, 180.0), 0.8) * np.exp(-t * 9) * 0.6
    x = np.tanh(1.8 * (x + nb))
    return x / np.abs(x).max()

def pop(f0=900, f1=320, dur=0.09):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 38)
    return x / np.abs(x).max()

def tick(dur=0.025, f=4200):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, f), 2.0) * np.exp(-t * 260)
    return x / (np.abs(x).max() + 1e-9)

def square_blips(notes, step=0.055):
    out_ = []
    for f in notes:
        n = int(step * SR); t = np.arange(n) / SR
        out_.append(np.sign(np.sin(2 * np.pi * f * t)) * 0.6 * np.exp(-t * 18))
    return np.concatenate(out_)

def zap(dur=0.5):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(120 * (2400 / 120) ** (t / dur)) / SR) * env(n, 0.15) * 0.6
    x += np.sin(2 * np.pi * 60 * t) * 0.35 * np.exp(-t * 4) + 0.15 * np.sin(2 * np.pi * 15734 / 4 * t) * np.exp(-t * 10)
    return x / np.abs(x).max()

def chime(freqs=(1318.5, 1760, 2637), dur=1.4):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate(freqs):
        d = int(k * 0.06 * SR); tt = t[: n - d]
        x[d:] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 3.5) * (0.8 ** k)
    return x / np.abs(x).max()

def rip(dur=0.55):
    n = int(dur * SR); t = np.arange(n) / SR
    jit = np.repeat(rng.random(n // 240 + 1), 240)[:n] ** 3
    x = svf_bp(rng.standard_normal(n), np.linspace(1400, 3600, n), 1.4) * jit * env(n, 0.2)
    return x / np.abs(x).max()

def scribble(dur=0.6):
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 13 * t))
    x = svf_bp(rng.standard_normal(n), 2600 + 900 * np.sin(2 * np.pi * 6.5 * t), 1.6) * am * env(n, 0.2)
    return x / np.abs(x).max()

def rumble(dur=1.5):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(70, 260, n), 0.7)
    x = x / np.abs(x).max() * env(n, 0.3, 1.0)
    return x

W = 0.30
# S1 hook: letters + hourglasses
for k in range(5): put(0.0 + k * 0.05, tick(0.03, 2600 + 300 * k), 0.10)
put(0.02, whoosh(0.55, 300, 2200, 1.1, 0.4), W * 0.7); put(0.12, whoosh(0.6, 2400, 400, 1.2, 0.3), W * 0.5)
put(0.5, pop(700, 1300, 0.1), 0.22); put(0.82, pop(500, 1100, 0.12), 0.24)   # chip "beda?" + the not-equal badge
# T1 panel slide-over
put(1.42, whoosh(0.62, 250, 2600, 1.0, 0.7), W); put(1.98, pop(220, 90, 0.16), 0.30)
# S2 BARU TERUS + flying chips + jitter
for k in range(4): put(2.12 + k * 0.045, tick(0.03, 1800), 0.10)
for k in range(6): put(2.34 + k * 0.045, tick(0.03, 1500), 0.10)
for k in range(7): put(2.45 + k * 0.05, pop(500 + 90 * k, 900 + 120 * k, 0.07), 0.12)
for j in range(7): put(2.98 + j * 0.083, tick(0.02, 5200), 0.12)
# T2 blinds
put(3.40, whoosh(0.6, 400, 3000, 1.3, 0.75), W * 0.9); put(3.97, pop(260, 110, 0.12), 0.26)
# S3 clock spin + split + leaders
put(4.02, pop(400, 900, 0.14), 0.2)
for j in range(10): put(4.05 + j * 0.075, tick(0.02, 3600 + 300 * (j % 2)), 0.08)
put(4.82, boom(0.5, 180, 70), 0.30); put(4.84, rip(0.35), 0.10)
for k in range(3): put(5.18 + k * 0.08, pop(900 + 200 * k, 1500 + 200 * k, 0.06), 0.13)
# T3 diagonal slice
put(5.44, whoosh(0.55, 3200, 600, 1.4, 0.8), W * 1.05); put(5.98, zap(0.28), 0.10)
# S4 chip + slice + BERES + stars
put(6.02, pop(800, 1500, 0.1), 0.20); put(6.24, whoosh(0.3, 1200, 4200, 1.6, 0.3), W * 0.6); put(6.36, boom(0.35, 220, 90), 0.22)
put(6.82, pop(300, 700, 0.14), 0.26)
for k in range(3): put(6.45 + k * 0.13, chime((1568 + 200 * k, 2093 + 200 * k), 0.5), 0.05)
# T4 band sweep
for k in range(3): put(7.42 + k * 0.06, whoosh(0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7), W * 0.55)
# S5 puzzle snap
put(8.08, whoosh(0.5, 300, 1600, 1.0, 0.8), W * 0.6)
put(8.74, boom(0.9, 120, 45), 0.42); put(8.75, pop(1800, 600, 0.05), 0.25); put(8.98, chime((1046, 1318, 1568), 0.8), 0.06)
# T5 zoom-through + flash
riser = whoosh(0.5, 200, 5200, 0.9, 0.95); put(9.52, riser, W * 1.1); put(9.98, boom(0.6, 160, 60), 0.30)
# S6 ? drop (bounces) + barcode + typewriter
put(10.1, whoosh(0.4, 600, 2400, 1.4, 0.4), W * 0.5)
for k, (t, g) in enumerate([(10.5, 0.30), (10.7, 0.14), (10.8, 0.07)]): put(t, pop(260 - 30 * k, 110, 0.12), g)
for k in range(10): put(10.45 + k * 0.03, tick(0.015, 6000), 0.06)
for k in range(24): put(10.78 + k * 0.028, tick(0.022, 3600 + 500 * (k % 3)), 0.11)
# T6 beam + iris
put(11.48, pop(500, 1000, 0.1), 0.18); put(11.55, whoosh(0.5, 200, 2400, 1.0, 0.9), W); put(11.98, boom(0.7, 140, 50), 0.30)
# S7 outro: M pop, slide, wordmark, shimmer
put(12.35, pop(600, 1200, 0.12), 0.24); put(12.82, whoosh(0.5, 900, 2600, 1.2, 0.5), W * 0.5)
put(13.1, chime((1046, 1568, 2093, 2637), 1.8), 0.08); put(13.12, boom(1.2, 90, 40), 0.18)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
