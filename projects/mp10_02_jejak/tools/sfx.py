"""Synthesised SFX for MasterPajak AI Video 2 (Jejak 1 Transaksi) — sits under the VO; no samples, no music (client rule). Deterministic.
Camera moves get soft air whooshes, every tollgate bite gets a chomp + a mechanical odometer tick train, chips land with a soft
thud, pencairan/bank get small chimes, the crane-up a long rising whoosh, "ribuan" a dense tick swarm, the tangles straighten
with zips, the ledger rows pop, checks get bright pops and flags a gentle double blip; series band sweep, hologram fx and the
beam/iris end card as in Video 1. Beat times are parsed from window.TM in index.html. Writes assets/audio/sfx.wav (48 kHz mono).
Run: python3 tools/sfx.py ."""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(12)
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
    return x / np.abs(x).max() * env(n, 0.3, 1.0)

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def chomp():
    """a bite: low thump + a short crunchy noise burst"""
    n = int(0.22 * SR); t = np.arange(n) / SR
    th = np.sin(2 * np.pi * np.cumsum(170 * (55 / 170) ** (t / 0.22)) / SR) * np.exp(-t * 18)
    cr = svf_bp(rng.standard_normal(n), np.full(n, 1700.0), 0.9) * np.exp(-t * 45) * (0.6 + 0.4 * np.sign(np.sin(2 * np.pi * 70 * t)))
    x = np.tanh(2.2 * (th + 0.5 * cr)); return x / np.abs(x).max()

def odo_ticks(t0, d=0.5, n=9, g=0.07):
    """mechanical counter: ticks that slow down as the digits settle"""
    for k in range(n):
        u = k / (n - 1); put(t0 + d * (1 - (1 - u) ** 2), tick(0.012, 3900 + 500 * (k % 2)), g * (1 - 0.5 * u))

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# ---- beat times (mirrors index.html) ----
SEG = [(TM['fee'] - 0.25, TM['fee'] + 0.65), (TM['ong'] - 0.4, TM['ong'] + 0.25), (TM['ret'] - 0.25, TM['ret'] + 0.4), (TM['l3'] - 0.45, TM['l3'] + 0.55), (TM['bank'] - 0.2, TM['bank'] + 0.8)]
BT = [SEG[0][1] + 0.05, SEG[1][1] + 0.04, SEG[2][1] + 0.04]; tP, tB = SEG[3][1], SEG[4][1]

# S1 · hook: slow orbit air, the road reveal (pull back + rise), stabilo on the amount
wh(0.0, 1.6, 200, 700, 0.9, 0.5, 0.3)
put(TM['q1'] + 0.4, pop(420, 700, 0.07), 0.07)
wh(TM['q1'] + 0.1, 1.5, 900, 260, 0.9, 0.45, 0.45)
put(TM['l2'] + 0.55, marker(0.45), MK)
# journey: a whoosh per road segment, chomp + odometer + chip pop/thud per bite
for k, (t0, t1) in enumerate(SEG):
    wh(t0 - 0.05, (t1 - t0) + 0.2, 260 + 60 * k, 1500 + 200 * k, 1.0, 0.5, 0.55)
for i, tb in enumerate(BT):
    put(tb - 0.01, chomp(), 0.2); put(tb + 0.02, zap(0.18), 0.03)
    odo_ticks(tb + 0.04, 0.55, 9, 0.07)
    put(tb + 0.05, pop(600 + 80 * i, 1250 + 80 * i, 0.08), 0.1)            # chip pops out
    put(tb + 1.0, pop(260, 120, 0.12), 0.1)                               # chip lands flat
put(tP + 0.02, chime((988, 1318.5), 0.9), 0.05); put(tP, pop(500, 900, 0.08), 0.08)
put(tB + 0.02, pop(300, 150, 0.12), 0.12); put(tB + 0.25, pop(800, 1500, 0.09), 0.12)
put(tB + 0.3, chime((1318.5, 1760, 2349), 1.3), 0.06)
# S2 · crane-up and the swarm
wh(TM['l4'] - 0.05, 2.5, 160, 1400, 0.8, 0.55, 0.75); put(TM['l4'] + 0.2, rumble(2.2, 60, 180), 0.05)
for k in range(3): put(TM['l4'] + 0.1 + k * 0.12, pop(500 + 100 * k, 900 + 100 * k, 0.07), 0.06)
put(TM['l4b'], pop(420, 760, 0.07), 0.06)
wh(TM['ribu'] - 0.55, 1.0, 400, 3000, 1.2, 0.6, 0.6); put(TM['ribu'] - 0.3, rumble(1.6, 90, 320), 0.07)
r2 = np.random.default_rng(5)
for k in range(70):                                                         # the swarm: dense, randomised ticks
    t = TM['ribu'] - 0.25 + r2.random() * 1.6; put(t, tick(0.01, 2500 + r2.random() * 3500), 0.035 + 0.02 * r2.random())
for k in range(12): put(TM['ribu'] - 0.05 + k * 0.035, pop(700 + 60 * k, 1200 + 40 * k, 0.05), 0.05)
odo_ticks(TM['ribu'] + 0.05, 0.9, 12, 0.06)
put(TM['ribu'] + 0.55, marker(0.42), MK)
# band sweep -> brand
for k in range(3): wh(TM['l5'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['l5'] + 0.55)
for g0 in (TM['l5'] + 3.2, TM['l5'] + 5.3, TM['l7'] + 4.4, TM['l7'] + 6.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# tangles straighten (zips), the ledger forms, stabilo
for i in range(5): put(TM['l5'] + 1.0 + i * 0.12, whoosh(0.9, 900, 3800, 3.0, 0.7), W * 0.22)
put(TM['l5b'] - 0.25, pop(300, 600, 0.1), 0.1)
for i in range(5): put(TM['l5b'] + 0.15 + i * 0.1, tick(0.016, 3000), 0.06)
put(TM['l5b'] + 1.1, marker(0.45), MK)
# pull back: orders -> pembukuan -> laporan, pulses
wh(TM['l5c'] - 0.2, 1.2, 1200, 300, 0.9, 0.5, 0.6)
for i in range(5): put(TM['l5c'] + 0.25 + i * 0.07, square_blips([2200], 0.03), 0.02)
for dt in (0.3, 0.65, 1.15): put(TM['l5c'] + dt, pop(520, 980, 0.08), 0.09)
# push in, scan, checks and flags
wh(TM['l6'] - 0.25, 1.1, 300, 1500, 1.0, 0.5, 0.55)
put(TM['l6'] + 1.0, whoosh(1.1, 1800, 3200, 4.0, 0.5), W * 0.18)
for j in range(3): put(TM['l6'] + 1.35 + j * 0.3, pop(1100 + 150 * j, 1900 + 150 * j, 0.07), 0.12)
put(TM['l6'] + 2.2, pop(600, 1100, 0.08), 0.1)
for j in range(2): put(TM['l6b'] + 0.5 + j * 0.3, square_blips([660, 880], 0.06), 0.035)
put(TM['l6b'] + 1.0, pop(500, 900, 0.08), 0.1)
# beam + iris -> end card
put(TM['l7'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['l7'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['l7'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['l7'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.3, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
