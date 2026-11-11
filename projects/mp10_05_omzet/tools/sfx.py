"""Synthesised SFX for MasterPajak AI Video 5 (Omzet vs Untung). Sits under the VO; no samples, no music (client rule). Deterministic.
Beats come from window.TM in index.html (parsed by regex), so a VO re-time moves every cue.
Column rise (riser + low thump on "gede"), odometer ticks that follow the eased digit roll, laser slice + tag pop + falling whoosh +
distant thud for each cost chunk, shimmer + marker on LABA, whip pan, dolly air + pops in the rack-focus scene, series band sweep,
hologram fx, card riffle + row pops, beam/iris boom, CTA pops and chime. Writes assets/audio/sfx.wav (48 kHz mono). Run: python3 tools/sfx.py ."""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(5)
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
    k = int(n * a)
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

def rumble(dur=1.5, f0=70, f1=260):
    n = int(dur * SR)
    x = svf_bp(rng.standard_normal(n), np.linspace(f0, f1, n), 0.7)
    return x / np.abs(x).max() * env(n, 0.7, 1.0)

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def laser(dur=0.3):
    """slicing beam: bright sine sweep up + hiss, short"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(1800 * (5200 / 1800) ** (t / dur)) / SR) * 0.5
    x += svf_bp(rng.standard_normal(n), np.linspace(5000, 8000, n), 2.5) * 0.6
    x *= np.minimum(1, t / 0.01) * np.exp(-t * 7)
    return x / np.abs(x).max()

def io_ease_inv(p):
    """inverse of GSAP power2.inOut (quadratic in-out): eased progress -> time fraction"""
    return np.where(p < 0.5, np.sqrt(p / 2), 1 - np.sqrt((1 - p) / 2))

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def odo_ticks(t0, d, n_cells, g=0.05):
    """one soft tick each time the lowest digit passes a cell (follows the eased roll)"""
    for k in range(1, n_cells + 1):
        put(t0 + float(io_ease_inv(np.array(k / n_cells))) * d, tick(0.012, 3800 + 300 * (k % 3)), g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# S1 · hook: the column shoots up (riser), odometer counts up, low thump + pop on "gede"
wh(0.0, 2.1, 110, 900, 0.9, 0.85, 0.55); put(0.0, rumble(2.1, 60, 220), 0.09)
odo_ticks(0.0, 2.26, 28, 0.045)
put(2.05, boom(0.7, 120, 48), 0.13); put(2.05, pop(420, 900, 0.1), 0.08)
# ask: the camera pulls back to the studio view, the question pops in
wh(TM['ask'] - 0.02, 1.0, 1300, 280, 1.0, 0.45, 0.4)
put(TM['ask'] + 0.6, pop(600, 1200, 0.09), 0.12); put(TM['ask'] + 1.15, tick(0.02, 3000), 0.07)
# S2 · subtractions: laser slice, chunk turns grey (tick), tag pop, fall whoosh, distant thud, odometer roll down
def chunk(ts, tg, tags, falls, roll, cells):
    put(ts, laser(0.3), 0.07)
    put(tg, tick(0.02, 2400), 0.06)
    for t in tags: put(t, pop(500, 1000, 0.1), P_)
    for k, t in enumerate(falls):
        put(t, tick(0.03, 1600), 0.08)                                   # the chunk unhooks
        wh(t + 0.2, 1.05, 2600 - 300 * k, 260, 1.3, 0.35, 0.65)          # falls past the camera
        put(t + 1.15, boom(0.55, 90, 40), 0.07)                          # lands far below, off frame
    odo_ticks(roll[0], roll[1] + 0.21, cells, 0.04)
chunk(TM['c1'] + 0.1, TM['c1'] + 0.25, [TM['c1'] + 0.45], [TM['c1'] + 0.95], (TM['c1'] + 0.95, 0.9), 22)
put(TM['c1'] + 0.95, tick(0.02, 2200), 0.05)                              # kicker roll OMZET -> SISANYA
chunk(TM['c2'] + 0.15, TM['c2'] + 0.3, [TM['c2'] + 0.5], [TM['c2'] + 0.95, TM['c2'] + 1.55], (TM['c2'] + 1.75, 0.9), 21)
chunk(TM['c3'] + 0.05, TM['c3'] + 0.15, [TM['c3'] + 0.3], [TM['c3'] + 0.75], (TM['c3'] + 0.8, 0.9), 26)
# laba: slow push-in, the rest turns yellow (shimmer), LABA marker + shine
wh(TM['laba'], 1.6, 260, 800, 0.9, 0.6, 0.3)
put(TM['laba'] + 1.0, chime((880, 1318.5, 1760), 1.2), 0.04)
put(TM['labaW'] - 0.35, tick(0.02, 2200), 0.05); put(TM['labaW'] + 0.05, marker(0.42), MK)
put(TM['labaW'] - 0.1, pop(400, 800, 0.12), 0.12); wh(TM['labaW'] + 0.1, 0.7, 2000, 6000, 2.0, 0.5, 0.25)
put(TM['labaW'] + 0.3, chime((1568, 2093, 2637, 3136), 1.4), 0.05)
# T · whip pan to the rack-focus scene
wh(TM['seller'] - 0.42, 0.52, 260, 3200, 1.0, 0.55, 1.0)
# S3 · rack focus: headline in, the dolly past OMZET (air), chips pop, the tree draws, stabilo on laba
put(TM['seller'] + 0.6, pop(520, 1000, 0.09), 0.08)
wh(TM['dec'] - 0.05, 1.2, 180, 1500, 0.9, 0.55, 0.7); put(TM['dec'] + 0.25, whoosh(0.5, 3000, 900, 1.5, 0.3), W * 0.35)
for k in range(3): put(TM['dec'] + 1.1 + k * 0.2, pop(650 + 90 * k, 1250 + 120 * k, 0.09), 0.12)
put(TM['dec'] + 1.2, pop(500, 900, 0.1), 0.09)
put(TM['dec'] + 2.1, marker(0.4), MK); put(TM['dec'] + 2.25, marker(0.48), MK * 0.8)
# T · band sweep -> brand (series)
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
# S4 · report card swings up, the three rows riffle apart, each row lands as it is named
wh(TM['sol'] + 0.75, 0.9, 220, 1400, 1.0, 0.5, 0.45)
for k in range(5): put(TM['sol'] + 1.3 + k * 0.045, tick(0.016, 2600 + 400 * k), 0.06)
put(TM['sol'] + 1.36, whoosh(0.45, 900, 3500, 1.4, 0.3), W * 0.3)
for k, t in enumerate((TM['sol'] + 1.75, TM['sol'] + 2.4, TM['sol'] + 3.1)): put(t, pop(520 + 80 * k, 1050 + 120 * k, 0.1), P_)
put(TM['sol'] + 3.1, chime((1318.5, 1760), 0.9), 0.035)
wh(TM['sol'] + 3.85, 0.6, 400, 1500, 1.0, 0.5, 0.2)
for g0 in (TM['sol'] + 2.9, TM['sol'] + 4.6, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# T · beam + iris -> end (series)
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 0.9, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
