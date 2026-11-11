"""Synthesised SFX for MasterPajak AI Video 10 (Sebelum vs Sesudah): keyboard ticks on the hand-typed rekap total, slider grab /
friction slide / snap-open for each of the three before-after wipes, horizontal whip pans, stabilo marker strokes, pen scribbles,
calculator error blips, pops on badges and cards, the chest-hologram fx and the series end (beam boom, iris, CTA pop, chime).
No samples, no music (client rule); sits under the VO. Deterministic. All times come from window.TM in index.html (same offsets as
the slider rig RIG in index.html). Writes assets/audio/sfx.wav (48 kHz mono). Run: python3 tools/sfx.py ."""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(10)
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
    k = int(n * a); e = np.ones(n)
    e[:k] = np.sin(np.linspace(0, np.pi / 2, k)) ** shape; e[k:] = np.cos(np.linspace(0, np.pi / 2, n - k)) ** shape
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

def key_tick():
    """a soft keyboard key: short noise click + a little body thump"""
    n = int(0.05 * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, 2600 + 900 * rng.random()), 1.6) * np.exp(-t * 180)
    x += 0.5 * np.sin(2 * np.pi * (180 + 40 * rng.random()) * t) * np.exp(-t * 90)
    return x / np.abs(x).max()

def square_blips(notes, step=0.055):
    o = []
    for f in notes:
        n = int(step * SR); t = np.arange(n) / SR
        o.append(np.sign(np.sin(2 * np.pi * f * t)) * 0.6 * np.exp(-t * 18))
    return np.concatenate(o)

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

def scribble(dur=0.4):
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.55 + 0.45 * np.sign(np.sin(2 * np.pi * 11 * t))
    x = svf_bp(rng.standard_normal(n), 2400 + 800 * np.sin(2 * np.pi * 7 * t), 1.6) * am * env(n, 0.15)
    return x / np.abs(x).max()

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def slide(dur=0.8):
    """the divider dragged across: soft friction whose loudness follows the drag speed (smootherstep velocity)"""
    n = int(dur * SR); u = np.linspace(0, 1, n)
    v = 30 * u * u * (1 - u) * (1 - u) / 1.875
    x = svf_bp(rng.standard_normal(n), 700 + 900 * v, 1.3)
    grit = 0.75 + 0.25 * np.abs(np.sin(2 * np.pi * 38 * np.cumsum(0.4 + v) / SR * 60))
    x = x * grit * (0.15 + 0.85 * v) * np.minimum(1, u / 0.04) * np.minimum(1, (1 - u) / 0.05)
    return x / (np.abs(x).max() + 1e-9)

W = 0.22; P_ = 0.13; MK = 0.10
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)
def blip(t0): put(t0, square_blips([1800, 900, 1500], 0.02), 0.02)

def drag(tg):
    """same offsets as RIG in index.html: reach tg-.75, grab tg-.4, drag tg-.05 -> tg+.75, release + snap tg+.95 -> tg+1.3"""
    put(tg - 0.4, tick(0.014, 3000), 0.09); put(tg - 0.38, pop(260, 140, 0.07), 0.08)            # grab
    put(tg - 0.05, slide(0.8), 0.11)                                                          # friction slide
    wh(tg + 0.95, 0.38, 500, 3400, 1.3, 0.85, 0.8)                                           # snap open
    put(tg + 1.29, boom(0.5, 120, 55), 0.09); put(tg + 1.29, tick(0.02, 2400), 0.06)

# C1 · divider tease, hand-typed rekap total (same timing as index.html), pull-back, three files, totals never match
wh(0.12, 0.45, 1600, 500, 1.2, 0.3, 0.35); put(0.55, tick(0.012, 3400), 0.05)
ty0, tyd = 0.2, 0.085
for i in range(1, 13):
    put(ty0 + (i - 1) * tyd + (0.12 if i > 4 else 0) + (0.1 if i > 8 else 0), key_tick(), 0.07)
wh(TM['tf'] - 0.55, 0.95, 1400, 350, 1.0, 0.4, 0.45)                                          # camera pulls back
wh(TM['tf'] - 0.5, 0.7, 120, 700, 0.9, 0.7, 0.35)                                              # robot rises
for k in range(3): put(TM['tf'] - 0.1 + k * 0.16, pop(600 + 160 * k, 1200 + 150 * k, 0.08), P_)
for k in range(3): put(TM['nc'] + 0.1 + k * 0.14, marker(0.3), MK * 0.6); put(TM['nc'] + 0.15 + k * 0.12, pop(1400, 700, 0.05), 0.06)
put(TM['nc'] + 0.55, marker(0.45), MK)
blip(TM['nc'] + 0.25)
for j in range(7): put(TM['nc'] + 0.5 + j * 0.06, tick(0.018, 3800), 0.05)
for t0 in (1.6, 3.0, 4.4): put(t0, pop(900, 1300, 0.05), 0.035)
# C1 · drag -> SESUDAH, hologram, three steps light up, the pulse runs the flow
drag(TM['l2'])
holo_fx(TM['l2'] + 1.1)
for g0 in (TM['l2'] + 1.1 + 1.9, TM['l2'] + 1.1 + 3.4): blip(g0)
for t0 in (TM['cj'], TM['pb'], TM['lp']): put(t0, pop(520, 1040, 0.1), P_); put(t0 + 0.15, tick(0.02, 5200), 0.05)
for t0 in (TM['pb'] - 0.45, TM['lp'] - 0.45): wh(t0, 0.45, 900, 2800, 1.6, 0.5, 0.25)
put(TM['sa'], whoosh(1.0, 400, 3600, 2.2, 0.8), W * 0.35); put(TM['sa'] + 1.0, chime((1568, 2093, 2637), 1.2), 0.04)
# whip C1 -> C2
W1, W2 = TM['l3'] - 0.3, TM['l4'] - 0.3
wh(W1 - 0.02, 0.5, 250, 3000, 1.0, 0.55, 1.0); put(W1 + 0.4, pop(200, 90, 0.14), 0.1)
# C2 · nebak-nebak: two strike-throughs + a scribbled circle, then the laporan
put(TM['l3'] + 0.7, scribble(0.22), 0.07); put(TM['l3'] + 1.05, scribble(0.22), 0.07); put(TM['l3'] + 1.4, scribble(0.5), 0.07)
drag(TM['l3b'])
for k in range(5): put(TM['l3b'] - 0.05 + 0.1 + k * 0.12, tick(0.016, 3600 + 300 * k), 0.05)
put(TM['jl'], marker(0.42), MK)
# whip C2 -> C3
wh(W2 - 0.02, 0.5, 280, 3200, 1.0, 0.55, 1.0); put(W2 + 0.4, pop(200, 90, 0.14), 0.1)
# C3 · bingung: sticky notes, calculator error blips, then estimasi + tim ahli
for k in range(3): put(TM['l4'] + 0.3 + k * 0.28, pop(420 + 90 * k, 900, 0.09), P_ * 0.8)
for j in (2, 7): put(TM['l4'] + 0.2 + j * 0.2, square_blips([520, 260], 0.06), 0.035)
for j in range(8): put(TM['l4'] + 1.0 + j * 0.12, tick(0.015, 2600), 0.035)
drag(TM['l4b'])
for j in range(0, 19, 2): put(TM['l4b'] + 0.55 + j * 0.045, tick(0.012, 5200), 0.04)
for k in range(4): put(TM['l4b'] + 0.7 + k * 0.08, pop(700 + 120 * k, 1300, 0.05), 0.05)
put(TM['ta'] - 0.25, pop(500, 1000, 0.1), P_); put(TM['ta'] + 0.6, marker(0.4), MK)
# beam + iris -> end card (series template)
EN = TM['l5']
put(EN - 0.5, pop(500, 1000, 0.1), 0.12); wh(EN - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(EN - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(EN + 0.55)
for g0 in (EN + 4.4, EN + 7.0): blip(g0)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.2, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
