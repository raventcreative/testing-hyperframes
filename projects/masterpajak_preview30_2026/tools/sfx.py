"""Synthesised SFX for the MasterPajak AI 38.5 s VO preview (sits under the VO) (no samples, no music, per the client's rule). Deterministic.
Every cut on the 120 BPM grid gets its own whoosh flavour; pops on chips/stars, ticks on the typewriter, impact on the puzzle snap,
shimmer + soft impact on the M-to-wordmark outro. Writes assets/audio/sfx.wav (48 kHz mono, 15 s). Run: python3 tools/sfx.py ."""
import sys, wave
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000; TOTAL = 38.5; N = int(TOTAL * SR) + SR
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

W = 0.22
P_ = 0.16
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
# S1
wh(0.0, 0.5, 200, 1400, g=0.6); wh(0.28, 0.45, 2200, 500, 1.2, 0.3, 0.6); wh(1.93, 0.45, 500, 2200, 1.2, 0.3, 0.6)
put(2.56, pop(700, 1300, 0.1), P_); put(2.7, pop(500, 1100, 0.12), P_)
# T1
wh(2.82, 0.62, 250, 2600, 1.0, 0.7); put(3.38, pop(220, 90, 0.16), 0.2)
# S2
for k in range(7): put(4.86 + k * 0.04, tick(0.03, 1800), 0.07)
for k in range(7): put(5.5 + k * 0.045, tick(0.03, 1500), 0.07)
for k in range(4): put(4.95 + k * 0.06, pop(500 + 90 * k, 900 + 120 * k, 0.07), 0.08)
for j in range(7): put(5.86 + j * 0.083, tick(0.02, 5200), 0.08)
for t0 in (6.52, 7.26, 7.98): wh(t0 - 0.05, 0.35, 600, 2400, 1.3, 0.5, 0.6); put(t0 + 0.42, pop(320, 160, 0.1), 0.18)
# T2
wh(8.3, 0.6, 400, 3000, 1.3, 0.75, 0.9); put(8.84, pop(260, 110, 0.12), 0.18)
# S3
put(8.98, pop(400, 900, 0.14), 0.14); put(10.02, boom(0.45, 180, 70), 0.2); put(10.04, rip(0.3), 0.07)
for k in range(3): put(10.18 + k * 0.05, pop(900 + 200 * k, 1500 + 200 * k, 0.06), 0.09)
# T3
wh(10.36, 0.55, 3200, 600, 1.4, 0.8, 1.0); put(10.9, zap(0.28), 0.07)
# S4
put(10.88, pop(700, 1200, 0.1), 0.12); put(11.18, pop(800, 1500, 0.1), P_); put(12.14, pop(760, 1400, 0.1), P_)
wh(12.6, 0.35, 1500, 600, 1.4, 0.4, 0.5)
for k in range(4): put(12.86 + k * 0.06, tick(0.02, 3800), 0.09)
wh(13.0, 0.35, 600, 2000, 1.3, 0.4, 0.5); put(13.36, pop(300, 700, 0.14), 0.18)
wh(13.58, 0.3, 1200, 4200, 1.6, 0.3, 0.5); put(13.72, boom(0.35, 220, 90), 0.18); put(14.3, pop(300, 700, 0.14), P_)
# T4
for k in range(3): wh(14.38 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S5: hologram power-up, flow pieces, trace
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)
holo_fx(15.25)
wh(17.62, 0.45, 400, 1800, 1.1, 0.6, 0.6); put(17.95, pop(300, 150, 0.12), 0.16)
wh(19.12, 0.4, 2000, 500, 1.2, 0.5, 0.6); put(19.72, boom(0.6, 130, 50), 0.22); put(19.73, pop(1800, 600, 0.05), 0.12)
put(20.3, scribble(0.6), 0.05); put(20.3, chime((1568, 2093), 0.8), 0.04)
wh(21.42, 0.45, 500, 1900, 1.1, 0.6, 0.6); put(22.08, boom(0.6, 130, 50), 0.22); put(22.09, pop(1800, 600, 0.05), 0.12)
for t0 in (18.6, 21.2, 34.3, 37.4): put(t0, square_blips([1800, 900, 1500], 0.02), 0.02)
# T5
wh(22.22, 0.5, 200, 5200, 0.9, 0.95, 1.1); put(22.68, boom(0.6, 160, 60), 0.24)
# S6a
put(22.82, pop(700, 1300, 0.1), P_); wh(22.98, 0.45, 600, 2400, 1.4, 0.4, 0.5)
for k, (t0, g) in enumerate([(23.75, 0.22), (23.92, 0.11), (24.0, 0.05)]): put(t0, pop(260 - 30 * k, 110, 0.12), g)
wh(24.0, 0.45, 300, 2600, 1.0, 0.85, 0.8)
# S6b chat
wh(24.42, 0.4, 500, 1800, 1.2, 0.5, 0.5)
for t0 in (24.6, 25.46, 26.64, 27.44): put(t0, pop(900, 1500, 0.07), 0.12)
for j in range(8): put(25.0 + j * 0.055, tick(0.018, 4200 + 300 * (j % 2)), 0.05)
for k in range(3): put(25.86 + k * 0.12, tick(0.02, 3000), 0.07)
wh(27.28, 0.45, 1200, 400, 1.2, 0.5, 0.4)
for k in range(3): put(27.8 + k * 0.07, pop(700 + 150 * k, 1200 + 150 * k, 0.07), 0.09)
put(28.5, pop(400, 800, 0.1), 0.14); put(29.3, scribble(0.4), 0.04)
# T6
put(29.8, pop(500, 1000, 0.1), 0.14); wh(29.86, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(30.28, boom(0.7, 140, 50), 0.22)
# S7
holo_fx(30.9, 1.0)
put(33.46, pop(500, 1000, 0.12), P_); put(35.46, pop(900, 1500, 0.08), 0.1)
put(37.9, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
