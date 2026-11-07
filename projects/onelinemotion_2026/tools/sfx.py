"""Synthesised SFX bed for the ONELINEMOTION reel (no samples, no downloads): whooshes on every world cut with a flavour per
style (pixel blips, CRT zap, comic punch + BOOM, cinematic hit, pencil scribble, wind chime, paper rip), launch rumble, pops on
apex beats, typing clicks on the CTA. Deterministic (seeded). Writes assets/audio/sfx.wav (48 kHz mono, full reel length).
Run: python3 tools/sfx.py ."""
import json, sys, wave
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/timing.json").read_text())
SR = 48000; N = int(T["total_sec"] * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(7)
S = {s["id"]: s for s in T["scenes"]}
def wt(txt, after=0.0):
    for w in T["words"]:
        if w["w"] == txt and w["s"] >= after: return w["s"]
    return None

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

W = 0.16   # whoosh level (the VO stays on top)
# --- s01 / s02 ---
put(0.02, whoosh(0.5, 200, 1400), W * 0.8)                                # mascot pops up
put(wt("10") - 0.04, pop(1200, 500), 0.18); put(wt("10"), chime((1568, 2093, 2637), 1.0), 0.07)  # the fan of cards
put(wt("After Effects.") + 0.1, whoosh(0.35, 900, 3500, 1.4, 0.2), W * 0.8); put(wt("After Effects.") + 0.32, pop(300, 120, 0.12), 0.25)
put(4.25, whoosh(0.5, 400, 1800), W * 0.7)                                # collapse -> card flips in
put(wt("gratis,") - 0.08, boom(0.6, 140, 60), 0.22)                       # GRATIS stamp
put(wt("dan", S["s02"]["start"]) - 0.25, whoosh(0.55, 2400, 500, 1.3, 0.3), W)   # card -> line, rocket swoops in
put(wt("terbang", S["s02"]["start"]) - 0.1, rumble(1.6), 0.22); put(wt("terbang", S["s02"]["start"]) + 0.4, whoosh(1.1, 300, 3200, 1.0, 0.7), W * 1.1)
# --- world cuts: whoosh + a flavour per style ---
for i in range(1, 11):
    c = S[f"w{i:02d}"]["start"]
    put(c - 0.14, whoosh(0.62, 350, 3000 if i != 8 else 1200), W)
put(S["w01"]["start"] + 0.05, pop(700, 1400, 0.12), 0.1)                     # cartoon iris
put(S["w02"]["start"] + 0.02, scribble(0.5), 0.07)                             # eraser
put(S["w03"]["start"] + 0.02, square_blips([523, 659, 784, 1047, 1319], 0.05), 0.07)   # pixel dissolve
put(wt("jadul.") - 0.05, square_blips([784, 1047, 1568], 0.06), 0.06)
put(S["w04"]["start"] - 0.02, zap(0.5), 0.09)                                 # CRT power-on
put(S["w05"]["start"] + 0.05, pop(260, 120, 0.15), 0.25)                      # panel slam
put(wt("BOOM!") - 0.02, boom(1.5, 110, 36), 0.42)                             # BOOM!
put(S["w06"]["start"] + 0.05, square_blips([880, 1175, 1568], 0.035), 0.035)  # facets
put(S["w07"]["start"] + 0.05, pop(220, 520, 0.18), 0.22)                      # clay blob "bloop"
put(S["w08"]["start"] - 0.05, boom(2.2, 70, 30), 0.3); put(S["w08"]["start"] + 0.02, chime((523, 784, 1046), 2.0), 0.05)   # cinematic hit
put(S["w09"]["start"] + 0.0, scribble(0.6), 0.09)                             # pencil scribble
put(S["w10"]["start"] + 0.05, chime((1046, 1318, 1568, 2093), 1.6), 0.06)     # watercolour bloom
put(S["s13"]["start"] - 0.02, rip(0.6), 0.16)                                 # torn paper
# --- s13 .. s16 ---
hop = wt("nggak", S["s13"]["start"]) - 0.15
put(hop, pop(400, 900, 0.16), 0.18); put(hop + 0.5, pop(600, 250, 0.1), 0.15); put(hop + 0.45, whoosh(0.8, 500, 3000, 1.0, 0.6), W * 0.9)
put(wt("animasi.", S["s13"]["start"]) - 0.05, boom(0.5, 160, 70), 0.2)        # NGGAK PERLU stamp
k0 = wt("ketik")
for j in range(14): put(k0 + 0.05 + j * 0.055, tick(0.022, 3800 + 400 * (j % 3)), 0.12)   # typing the prompt
put(wt("Claude", S["s14"]["start"]) - 0.05, chime((1318, 1976), 0.9), 0.06)
put(wt("videonya.") - 0.05, pop(500, 1000, 0.12), 0.16)
m0 = wt("MOTION,")
for j in range(6): put(m0 - 0.05 + j * 0.06, tick(0.022, 4200), 0.14)          # M-O-T-I-O-N
put(m0 + 0.42, pop(900, 1600, 0.1), 0.16)                                       # heart
put(wt("kirim") - 0.05, whoosh(0.7, 700, 3600, 1.2, 0.5), W)                   # paper plane
put(wt("DM.") - 0.02, chime((1568, 2093), 0.8), 0.06)
put(S["s16"]["start"] - 0.2, whoosh(0.7, 300, 2000), W * 0.8)
put(S["s16"]["start"] + 0.35, whoosh(3.2, 400, 1600, 0.9, 0.5), W * 0.6)      # the loop around the grid
put(wt("angkanya") - 0.05, pop(800, 1300, 0.1), 0.12)
put(T["total_sec"] - 1.6, chime((1046, 1568, 2093, 2637), 1.6), 0.07)          # end lockup
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
