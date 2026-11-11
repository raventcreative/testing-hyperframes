"""Synthesised SFX for MasterPajak AI Video 1 (Berita Pajak): stabilo marker strokes, browser clicks, transitions (sits under the VO) (no samples, no music, per the client's rule). Deterministic.
Every cut on the 120 BPM grid gets its own whoosh flavour; pops on chips/stars, ticks on the typewriter, impact on the puzzle snap,
shimmer + soft impact on the M-to-wordmark outro. Writes assets/audio/sfx.wav (48 kHz mono, 15 s). Run: python3 tools/sfx.py ."""
import sys, wave
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
import re
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
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
P_ = 0.15
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy 40-70 Hz texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)
def click():
    return tick(0.012, 5200) * 0.8 + np.concatenate([np.zeros(int(0.03 * SR)), pop(1800, 900, 0.03)])[: int(0.06 * SR)] if False else tick(0.014, 5200)
MK = 0.11
# S0
wh(0.0, 0.55, 200, 1600, g=0.6)
for k in range(8): put(0.75 + k * 0.2, marker(0.18), MK * 0.9)
put(1.6, pop(600, 1200, 0.1), P_); put(1.75, marker(0.4), MK)
# articles
for i, (t0, n) in enumerate([(TM['a1'], 1), (TM['a2'], 2), (TM['a3'], 2), (TM['a4'], 1)]):
    put(t0 - 0.05, tick(0.012, 5200), 0.16); put(t0 - 0.03, pop(1600, 900, 0.035), 0.08)
    wh(t0, 0.3, 800, 2200, 1.4, 0.4, 0.35); wh(t0 + 0.28, 0.6, 300, 1200, 1.0, 0.6, 0.45)
    for k in range(n): put(t0 + 0.85 + k * 0.55, marker(0.42), MK)
    wh(t0 + 2.42, 0.45, 1200, 400, 1.1, 0.5, 0.35)
# confusion
wh(TM['conf'] - 0.48, 0.5, 2400, 300, 1.0, 0.7, 0.8)
for k in range(4): put(TM['conf'] + 0.05 + k * 0.1, rip(0.25), 0.05); put(TM['conf'] + 0.1 + k * 0.1, pop(400, 200, 0.1), 0.12)
for k in range(3): put(TM['conf'] + 1.1 + k * 0.15, pop(900 + 200 * k, 1500, 0.08), 0.12)
for j in range(6): put(TM['conf'] + 1.6 + j * 0.09, tick(0.02, 4800), 0.06)
# band sweep -> solution
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)
holo_fx(TM['sol'] + 0.55)
put(TM['sol'] + 2.2, pop(500, 1000, 0.1), P_); put(TM['sol'] + 3.6, marker(0.45), MK)
put(TM['sol'] + 4.6, pop(500, 1000, 0.1), P_); put(TM['sol'] + 5.9, marker(0.45), MK)
for g0 in (TM['sol'] + 3.2, TM['sol'] + 6.3, TM['end'] + 4.4, TM['end'] + 7.0): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# slide-over -> help
wh(TM['help'] - 0.6, 0.62, 250, 2600, 1.0, 0.7, 0.9); put(TM['help'] - 0.02, pop(220, 90, 0.16), 0.16)
put(TM['help'] + 0.6, pop(700, 1300, 0.1), P_); put(TM['help'] + 1.5, pop(760, 1400, 0.1), P_); put(TM['help'] + 2.6, marker(0.4), MK)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['end'] + 3.6, pop(500, 1000, 0.12), P_); put(TM['end'] + 5.0, pop(900, 1500, 0.08), 0.1)
put(TM['end'] + 7.0, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
