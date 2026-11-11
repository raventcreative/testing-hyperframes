"""Synthesised SFX for MasterPajak AI Video 6 (Bulanan ≠ Tahunan) — sits under the VO (no samples, no music, per the client's rule).
Deterministic. Beat times are parsed from window.TM in index.html, so a VO re-time moves every cue:
camera air moves, the ≠ slam (drop + thud + shake), the 12 months bursting out and being counted back in (ascending ticks),
"error" blips on the duplicate row, a ghost shimmer for the missing row, magnifier steps + a clock that speeds up,
band sweep, chest-hologram fx, months snapping into the grid, the scan with ✓ pops and the yellow flags (marker strokes),
the list sorting, the beam + iris and the end card. Writes assets/audio/sfx.wav (48 kHz mono). Run: python3 tools/sfx.py ."""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(6)
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

def rumble(dur=1.5):
    n = int(dur * SR)
    x = svf_bp(rng.standard_normal(n), np.linspace(70, 260, n), 0.7)
    return x / np.abs(x).max() * env(n, 0.3, 1.0)

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy 40-70 Hz texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def shimmer(dur=0.9, f0=1900, f1=820):
    """ghost row: a falling glassy tone with tremolo"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (f1 / f0) ** (t / dur)
    x = (np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.5 * np.sin(2 * np.pi * np.cumsum(f * 1.5) / SR)) * (0.6 + 0.4 * np.sin(2 * np.pi * 9 * t)) * env(n, 0.2)
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# ---- P · hook: camera push, the two cards lift on "bulanan"/"tahunan", ≠ drops and slams ----
wh(0.0, 1.3, 200, 900, 1.0, 0.5, 0.3)
put(TM['hook'] + 0.42, pop(420, 760, 0.09), 0.1); put(TM['hook'] + 1.2, pop(380, 680, 0.09), 0.1)
wh(TM['ne'] - 0.55, 0.45, 900, 2400, 1.3, 0.5, 0.22)
wh(TM['ne'] - 0.28, 0.3, 2600, 500, 1.2, 0.3, 0.5); put(TM['ne'] - 0.01, boom(0.8, 150, 48), 0.24); put(TM['ne'], tick(0.03, 2600), 0.08)
# ---- the months burst out, then are counted back into the monthly total ----
wh(TM['sum'] - 0.02, 0.6, 300, 3200, 1.1, 0.35, 0.6)
for k in range(12): put(TM['sum'] + 0.05 + k * 0.045 + 0.25, pop(700 + 40 * k, 1100 + 40 * k, 0.05), 0.045)
for k in range(12):
    t0 = TM['add'] + k * 0.058
    put(t0 + 0.2, tick(0.02, 2200 + 210 * k), 0.09); put(t0 + 0.2, pop(500 + 60 * k, 900 + 60 * k, 0.04), 0.04)
# ---- "nggak sama": ≠ again + the gap chip ----
wh(TM['tot'] - 0.05, 0.75, 300, 1500, 1.0, 0.5, 0.35)
wh(TM['tot'] + 0.13, 0.26, 2600, 500, 1.2, 0.3, 0.35); put(TM['tot'] + 0.36, boom(0.6, 140, 52), 0.16)
put(TM['tot'] + 0.6, pop(500, 1000, 0.1), P_); put(TM['tot'] + 0.72, square_blips([620, 465], 0.06), 0.022)
# ---- dive into the spreadsheet; duplicate row; missing row ----
wh(TM['why'], 1.05, 450, 2200, 0.9, 0.55, 0.65)
put(TM['dup'], square_blips([700, 525, 700, 525], 0.05), 0.02); put(TM['dup'] + 0.12, pop(300, 600, 0.12), 0.12); put(TM['dup'] + 0.45, pop(900, 1500, 0.08), 0.1)
put(TM['miss'] - 0.35, pop(600, 300, 0.1), 0.06)
wh(TM['miss'] + 0.03, 0.55, 200, 800, 0.9, 0.5, 0.35); put(TM['miss'] + 0.4, shimmer(0.9), 0.05); put(TM['miss'] + 0.75, pop(900, 1500, 0.08), 0.1)
# ---- the hunt: pull back, magnifier steps, the clock speeds up ("bisa seharian") ----
wh(TM['hunt'], 0.8, 1800, 350, 1.0, 0.5, 0.45); put(TM['hunt'] + 0.25, pop(500, 1000, 0.1), 0.12); wh(TM['hunt'] + 0.42, 0.45, 2400, 700, 1.4, 0.4, 0.25)
for j in range(13): put(TM['hunt'] + 0.95 + j * 0.2, tick(0.018, 3400 + 300 * (j % 2)), 0.055)
t = TM['hunt'] + 0.4
while t < TM['day']: put(t, tick(0.012, 5200), 0.05); t += 0.25
iv = 0.2
while t < TM['sol'] - 0.35: put(t, tick(0.012, 5200), 0.05); t += iv; iv = max(0.045, iv * 0.86)
put(TM['day'] - 0.05, rumble(1.4), 0.1); put(TM['day'], square_blips([523, 440, 392], 0.07), 0.015)
# ---- band sweep -> navy; MasterPajak AI ----
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
for k in range(12): put(TM['sol'] + 0.12 + k * 0.055 + 0.42, tick(0.016, 3000 + 120 * k), 0.07)
put(TM['sol'] + 0.35, pop(500, 900, 0.1), 0.08)
for g0 in (TM['sol'] + 3.0, TM['sol'] + 5.3, TM['end'] + 4.4, TM['end'] + 6.6): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# ---- "cocokkan": scan + ✓ pops, yellow months; summary pills ----
SC0, SCD = TM['cek'] + 0.1, 1.15
put(SC0 - 0.05, whoosh(SCD + 0.1, 500, 2600, 2.2, 0.5), W * 0.3)
for k in range(12):
    r = k // 3; tc = SC0 + SCD * ((24 + r * 186 + 80) / 760) + (k % 3) * 0.04
    if k in (2, 7): put(tc, pop(330, 220, 0.12), 0.12); put(tc, marker(0.22), MK * 0.6)
    else: put(tc, pop(900 + 25 * k, 1500, 0.06), 0.07)
put(SC0 + SCD + 0.05, pop(400, 800, 0.1), 0.08); put(SC0 + SCD + 0.3, pop(800, 1400, 0.08), 0.09); put(SC0 + SCD + 0.55, pop(500, 1000, 0.1), 0.11)
# ---- "tandai baris yang perlu dicek": March opens into its list ----
for k in range(2): put(TM['flag'] - 0.1 + k * 0.24, tick(0.02, 3000), 0.05)
wh(TM['flag'] + 0.22, 0.7, 300, 2000, 1.0, 0.45, 0.55)
for i in range(6): put(TM['flag'] + 0.6 + i * 0.07, tick(0.014, 3800), 0.05)
for k in range(4): put(TM['flag'] + 1.05 + k * 0.08, pop(950, 1500, 0.06), 0.07)
for k in range(2): put(TM['flag'] + 1.45 + k * 0.32, marker(0.38), MK); put(TM['flag'] + 1.5 + k * 0.32, pop(500, 1000, 0.09), 0.09)
# ---- "mulai periksa dari mana": the checked rows step aside, the flagged rows rise, the pointer ----
wh(TM['know'], 0.45, 1500, 400, 1.0, 0.4, 0.25); wh(TM['know'] + 0.2, 0.6, 300, 1600, 1.0, 0.5, 0.35)
put(TM['know'] + 0.85, pop(500, 1000, 0.12), P_); put(TM['know'] + 0.9, chime((1046, 1318.5, 1568), 1.0), 0.035)
# ---- beam + iris -> end card ----
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 0.5, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
