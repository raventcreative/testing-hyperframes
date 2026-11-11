"""Synthesised SFX for MasterPajak AI Video 14 (Siapin 4 Data Ini) — sits under the VO (no samples, no music, per the client's rule).
Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again. Deterministic.
Sounds: studio dolly air, stabilo marker, archive-box lid (creak-less hinge swing + cardboard knock), item fly-ins (whoosh per
direction), tick stamps (pop + bright ding), HUD bar fills + counter clicks, paper drops into the box (soft papery thud),
checkbox ticks, lid close thump + stamp chime, band sweep, hologram fx, the pour (paper flutters + landing pops), odometer
ticks + result chime, shine shimmer, beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s).
Run: python3 tools/sfx.py [project dir]"""
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
    x = np.tanh(1.8 * (x + nb)); return x / np.abs(x).max()

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

def ding(f=2093, dur=0.5):
    """bright check-mark ding: a sine + soft inharmonic partial, fast decay"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 7) + 0.35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 14)
    return x / np.abs(x).max()

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def knock(f=150, dur=0.22):
    """cardboard box knock: low damped body + a papery click"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 26) + 0.5 * np.sin(2 * np.pi * f * 1.9 * t) * np.exp(-t * 40)
    x += svf_bp(rng.standard_normal(n), np.full(n, 1300.0), 1.0) * np.exp(-t * 70) * 0.5
    return x / np.abs(x).max()

def paper(dur=0.3):
    """paper slap / settle: soft noise burst with a fast low-mid body"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(2200, 900, n), 0.9) * np.exp(-t * 22)
    x += np.sin(2 * np.pi * 110 * t) * np.exp(-t * 30) * 0.6
    return x / np.abs(x).max()

def flutter(dur=0.5):
    """paper flutter: AM-chopped band noise"""
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.55 + 0.45 * np.sign(np.sin(2 * np.pi * (16 + 8 * t / dur) * t))
    x = svf_bp(rng.standard_normal(n), 2400 + 700 * np.sin(2 * np.pi * 5 * t), 1.3) * am * env(n, 0.25)
    return x / np.abs(x).max()

def shimmer(dur=0.8):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(4000, 9000, n), 3.0) * env(n, 0.4)
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

DK = [TM['d1'], TM['d2'], TM['d3'], TM['d4'], TM['kum']]
TICK = [TM['d1'] + 1.05, TM['d2b'] + 0.8, TM['d3'] + 1.05, TM['d4'] + 1.05]
# S1 · hook: slow studio dolly (air), text pops, stabilo on "gambaran pajak", the "?" marks wobble
wh(0.0, 2.6, 200, 900, 0.9, 0.5, 0.35)
put(TM['hook'] + 0.3, pop(500, 900, 0.08), 0.08); put(TM['hook'] + 0.75, pop(560, 1000, 0.08), 0.08)
put(TM['hook'] + 1.25, marker(0.45), MK)
for j in range(3): put(0.5 + j * 0.81, tick(0.02, 3800), 0.03)
# S2 · siapin: ghost card whips away, the lid swings open and knocks, HUD drops in with four bar ticks
wh(TM['siap'] + 0.02, 0.55, 600, 2600, 1.2, 0.7, 0.55)
put(TM['siap'] + 0.1, knock(170, 0.2), 0.16); wh(TM['siap'] + 0.24, 0.45, 300, 1500, 1.0, 0.6, 0.45); put(TM['siap'] + 0.62, knock(120, 0.25), 0.14)
put(TM['siap'] + 0.45, pop(500, 950, 0.08), 0.08); put(TM['siap'] + 1.05, marker(0.38), MK)
wh(TM['siap'] + 0.9, 0.35, 900, 2400, 1.2, 0.5, 0.25)
for k in range(4): put(TM['siap'] + 1.05 + k * 0.1, tick(0.018, 3200 + 300 * k), 0.06)
# S3 · four items: fly-in, title pop, tick stamp + ding, HUD fill + counter click, drop + paper thud, checkbox tick
for k in range(4):
    t0, tdrop = DK[k], DK[k + 1] - 0.88; tland = tdrop + 0.74
    wh(t0 - 0.05, 0.75, 250 + 60 * k, 2200 + 200 * k, 1.1, 0.55, 0.85)
    put(t0 + 0.02, pop(420, 840, 0.09), 0.1)
    put(TICK[k], pop(700, 1400, 0.07), 0.13); put(TICK[k] + 0.04, ding(2093 * (1.0595 ** (2 * k)), 0.55), 0.07)
    wh(TICK[k] + 0.1, 0.4, 1200, 3200, 1.6, 0.4, 0.18); put(TICK[k] + 0.28, tick(0.02, 2600), 0.08)
    wh(tdrop + 0.2, 0.55, 2200, 400, 1.0, 0.35, 0.5)
    put(tland - 0.02, paper(0.3), 0.16); put(tland - 0.01, knock(140, 0.2), 0.08)
    put(tland + 0.1, tick(0.016, 4400), 0.07)
# 2 · "termasuk ongkir dan iklan": two tags pop, two stabilo strokes
for dt in (0.25, 0.75): put(TM['d2b'] + dt, pop(600, 1200, 0.09), 0.12)
for dt in (0.3, 0.8): put(TM['d2b'] + dt, marker(0.3), MK * 0.8)
# S3b · "Udah kekumpul?": files settle, lid closes with a thump, stamp + chime, LENGKAP pop
wh(TM['kum'] + 0.04, 0.4, 1400, 500, 1.0, 0.4, 0.3)
wh(TM['kum'] + 0.18, 0.42, 400, 1600, 1.0, 0.8, 0.45); put(TM['kum'] + 0.6, knock(95, 0.32), 0.2)
put(TM['kum'] + 0.66, pop(600, 1300, 0.09), 0.14); put(TM['kum'] + 0.72, chime((1568, 2093, 2637), 1.1), 0.06)
put(TM['kum'] + 0.7, pop(900, 1500, 0.07), 0.08)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S4 · brand: box drops in, lid pops off, the pour (flutter + four landing pops), caption marker, box exits
wh(TM['sol'] + 0.05, 0.5, 2000, 400, 1.0, 0.4, 0.5); put(TM['sol'] + 0.64, knock(130, 0.22), 0.14)
put(TM['sol'] + 0.6, pop(380, 760, 0.1), 0.1); wh(TM['sol'] + 0.8, 0.45, 600, 2600, 1.2, 0.6, 0.35)
holo_fx(TM['sol'] + 0.55)
put(TM['sol'] + 0.85, flutter(0.9), 0.07)
for k in range(4): put(TM['sol'] + 1.0 + k * 0.24, whoosh(0.4, 900, 2600, 1.4, 0.5), W * 0.3); put(TM['sol'] + 1.56 + k * 0.24, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.12)
wh(TM['sol'] + 2.25, 0.5, 500, 1800, 1.0, 0.6, 0.35)
put(TM['sol'] + 2.85, marker(0.42), MK)
for g0 in (TM['sol'] + 2.9, TM['est'] + 1.7, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# "estimasi pajak": the ledger recedes, the estimate card lifts out, odometer ticks, result chime, shine
wh(TM['est'], 0.8, 1600, 300, 0.9, 0.5, 0.35); wh(TM['est'] + 0.2, 0.8, 250, 2400, 1.0, 0.45, 0.6)
tt = TM['est'] + 0.45
for j in range(14): put(tt, tick(0.012, 3600 + 120 * (j % 3)), 0.06); tt += 0.05 + 0.006 * j * j * 0.08
put(TM['est'] + 1.75, chime((1318.5, 1760, 2637), 1.3), 0.07)
put(TM['est'] + 1.35, marker(0.42), MK); put(TM['est'] + 2.2, shimmer(0.8), 0.03)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.2, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
