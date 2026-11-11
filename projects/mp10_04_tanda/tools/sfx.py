"""Synthesised SFX for MasterPajak AI Video 4 (3 Tanda Pembukuanmu Berantakan): sits under the VO (no samples, no music,
per the client's rule). Deterministic. Every beat time is read from window.TM in index.html, so a VO re-time moves the sound too.
Hook: camera push + numeral swoosh, letter clatter on "berantakan", stabilo marker, stamp slam on "paling sering".
Signs: whip pans, odometer ticks, the ≠ slam (thud + descending error blips), paper flutters + tag pops, bar ticks, "?" boing.
Tidy-up clicks, band sweep, hologram fx, card flip, rows, stabilo, beam + iris, end card pops + chime.
Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py ."""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(14)
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

def flutter(dur=0.35):
    """paper flutter: band-passed noise with a fast irregular amplitude flap"""
    n = int(dur * SR); t = np.arange(n) / SR
    flap = 0.35 + 0.65 * np.abs(np.sin(2 * np.pi * (22 + 10 * rng.random()) * t + rng.random() * 6)) ** 3
    x = svf_bp(rng.standard_normal(n), np.linspace(2200, 1200, n), 0.9) * flap * env(n, 0.15)
    return x / (np.abs(x).max() + 1e-9)

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def boing(dur=0.35, f0=220, f1=520):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 + (f1 - f0) * (1 - np.exp(-t * 18)) + 40 * np.sin(2 * np.pi * 9 * t) * np.exp(-t * 6)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)
    return x / np.abs(x).max()

def odo_ticks(t0, dur, n=16, f=3600, g=0.07):
    """odometer roll: ticks that slow down (ease-out), like the digits"""
    for k in range(n):
        u = k / (n - 1); tt = t0 + dur * 0.95 * u ** 2   # dense at first, then slowing to a stop
        put(tt, tick(0.012, f + 400 * rng.random()), g * (1 - 0.5 * u))

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def whip(tw, g=1.0): wh(tw - 0.3, 0.62, 260, 3000, 1.0, 0.55, 0.95 * g); put(tw + 0.02, tick(0.02, 2400), 0.05)
def slam(t, g=1.0): put(t, boom(0.6, 150, 55), 0.2 * g); put(t, pop(260, 90, 0.12), 0.14 * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

W1, W2, W3, W4 = TM['s1'] - 0.1, TM['s2'] - 0.1, TM['s3'] - 0.1, TM['kal'] - 0.1
# HOOK · camera push-in, hero 3 swings in, title, letters clatter, stabilo, stamp slam
wh(0.0, 1.1, 180, 1500, 1.0, 0.55, 0.55)
put(TM['hook'] + 0.3, pop(600, 1100, 0.08), 0.08); wh(TM['hook'] + 0.7, 0.45, 500, 1800, 1.2, 0.5, 0.3)
for k in range(10): put(TM['hook'] + 1.75 + k * 0.045 + 0.02 * rng.random(), pop(700 + 500 * rng.random(), 300 + 200 * rng.random(), 0.06), 0.06)
put(TM['hook'] + 2.45, marker(0.45), MK)
for k in range(2): put(TM['h3'] + 0.2 + k * 0.36, pop(1200, 1700, 0.06), 0.07)
wh(TM['h3'] + 0.36, 0.32, 2400, 400, 1.2, 0.8, 0.45); slam(TM['h3'] + 0.68)
# SIGN 1 · two totals roll and refuse to match
whip(W1)
wh(TM['s1'] + 0.5, 0.5, 300, 1500, 1.0, 0.5, 0.35); odo_ticks(TM['s1'] + 0.7, 1.4, 18)
wh(TM['s1'] + 1.3, 0.5, 320, 1600, 1.0, 0.5, 0.35); odo_ticks(TM['s1'] + 1.5, 1.4, 18, 3300)
wh(TM['s1'] + 2.3, 0.45, 2200, 300, 1.2, 0.8, 0.5); slam(TM['s1'] + 2.72, 1.1)
put(TM['s1'] + 2.78, square_blips([620, 520, 410, 330], 0.07), 0.045)
wh(TM['s1'] + 3.4, 0.9, 500, 1400, 1.4, 0.5, 0.25)
# SIGN 2 · papers burst into the room, location tags pop
whip(W2)
for k in range(9): put(TM['s2'] + 0.25 + k * 0.08 + 0.03 * rng.random(), flutter(0.32 + 0.1 * rng.random()), 0.09)
wh(TM['s2'] + 0.2, 0.9, 200, 1600, 0.9, 0.4, 0.4)
for k in range(4): put(TM['s2'] + 2.0 + k * 0.14, pop(800 + 120 * k, 1400 + 150 * k, 0.07), 0.1)
put(TM['s2'] + 2.55, marker(0.4), MK)
for k in range(4): put(TM['s2'] + 3.0 + k * 0.2, flutter(0.25), 0.04)
# SIGN 3 · stamp, omzet rolls + bars, "?" boing, "nggak tahu"
whip(W3)
slam(TM['s3'] + 0.56, 0.8); wh(TM['s3'] + 0.5, 0.5, 300, 1500, 1.0, 0.5, 0.35); odo_ticks(TM['s3'] + 0.75, 1.3, 18, 3800)
for k in range(12): put(TM['s3'] + 0.98 + k * 0.045, pop(500 + 70 * k, 800 + 90 * k, 0.05), 0.045)
put(TM['s3u'] + 0.78, boing(0.4), 0.12); put(TM['s3u'] + 0.75, pop(300, 900, 0.1), 0.08)
for k in range(3): put(TM['s3u'] + 1.27 + k * 0.5, tick(0.02, 1800), 0.03)
put(TM['s3u'] + 1.6, square_blips([520, 440, 370], 0.08), 0.03)
# KALAU ADA SATU AJA · numerals hop one by one, then everything snaps tidy
whip(W4)
for k in range(3): put(TM['kal'] + 0.78 + k * 0.16, pop(700 + 200 * k, 1200 + 260 * k, 0.07), 0.09)
for k in range(6): put(TM['kal'] + 1.72 + k * 0.05 + 0.4, tick(0.016, 3000 + 300 * k), 0.07)
wh(TM['kal'] + 1.6, 0.6, 1800, 400, 1.1, 0.4, 0.45); put(TM['kal'] + 1.75, marker(0.42), MK)
put(TM['kal'] + 2.3, chime((1568, 2093), 0.9), 0.04)
# band sweep -> solution
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
for k, dt in enumerate((1.6, 2.85, 3.7)): put(TM['sol'] + dt, pop(600 + 150 * k, 1100 + 200 * k, 0.08), 0.1)
for k in range(3): wh(TM['sol'] + 1.5 + k * 0.12, 0.4, 400, 1800, 1.1, 0.5, 0.25)
wh(TM['sol'] + 2.2, 0.7, 250, 1500, 1.0, 0.5, 0.4)
for k in range(3): put(TM['sol'] + 2.95 + k * 0.06, tick(0.014, 3400), 0.06)
for k in range(4): put(TM['sol'] + 2.98 + k * 0.08, tick(0.012, 4400), 0.05)
wh(TM['sol'] + 3.5, 0.75, 300, 2600, 1.1, 0.55, 0.6); put(TM['sol'] + 4.33, pop(300, 140, 0.1), 0.1)
for k in range(3): put(TM['sol'] + 4.1 + k * 0.22, pop(700, 1200, 0.07), 0.09)
put(TM['sol'] + 4.9, marker(0.4), MK); put(TM['sol'] + 5.4, marker(0.45), MK)
for g0 in (TM['sol'] + 3.0, TM['sol'] + 5.6, TM['end'] + 4.3, TM['end'] + 6.3): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['end'] + 3.35, pop(500, 1000, 0.12), P_); put(TM['end'] + 5.2, pop(900, 1500, 0.08), 0.1)
put(TM['end'] + 6.2, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
fade = int(0.3 * SR); x[-fade:] *= np.linspace(1, 0, fade)
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
