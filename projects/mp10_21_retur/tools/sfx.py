"""Synthesised SFX for MasterPajak AI Video 21 (Retur Juga Harus Dicatat) — sits under the VO (no samples, no music).
Beat times are parsed from window.TM in index.html (real VO word times + 0.30 s), so `python3 tools/sfx.py` after any re-time.
Sounds: yard air, track draw, boomerang whirrs (spin-chopped noise with a doppler arc) + landing thuds, sticker pops, sale-chip
pop + ding, "?" pop + wobble ticks, stabilo markers, pallet knocks, ten shipping hops with count ticks + rising dings and delivery
bumps, TERCATAT stamp, money whooshes + coin dings, blur whoosh, ghost-row slide, balloon "inflate" on the swollen number, bar
sweeps, card fly-ins, soft "eh-eh" mismatch buzz on the ≠, band sweep, hologram fx, scan shimmer, value pops, selisih chime,
beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py [project dir]"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(21)
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

def whirr(dur=1.6, f0=700, f1=1400):
    """boomerang whirr: band noise chopped by the spin (AM) with a doppler-ish pitch arc (rises going out, falls coming back)"""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    f = f0 + (f1 - f0) * np.sin(np.pi * u)
    am = 0.55 + 0.45 * np.sin(2 * np.pi * np.cumsum(9 + 7 * np.sin(np.pi * u)) / SR) ** 2
    x = svf_bp(rng.standard_normal(n), f, 2.2) * am * (0.35 + 0.65 * np.sin(np.pi * u) ** 0.6) * env(n, 0.1)
    return x / (np.abs(x).max() + 1e-9)

def inflate(dur=0.55):
    """balloon puff: a rising, slightly wobbly tone + air"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 220 * (2.2 ** (t / dur)) * (1 + 0.03 * np.sin(2 * np.pi * 14 * t))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.7) * 0.7 + svf_bp(rng.standard_normal(n), np.linspace(600, 2400, n), 1.0) * env(n, 0.6) * 0.4
    return x / np.abs(x).max()

def nope(dur=0.34):
    """soft 'eh-eh' mismatch buzz (two short low square-ish blips)"""
    o = np.zeros(int(dur * SR))
    for k, t0 in enumerate((0.0, 0.17)):
        n = int(0.13 * SR); t = np.arange(n) / SR
        x = np.tanh(3 * np.sin(2 * np.pi * (180 - 20 * k) * t)) * np.exp(-t * 14)
        i = int(t0 * SR); o[i:i + n] += x[: len(o) - i]
    return o / np.abs(o).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# S1 · hook: yard air, the track draws, the parcel boomerangs out and back (whirr), lands with a thud, stickers, chip, "?"
wh(0.0, 2.4, 200, 800, 0.9, 0.5, 0.3)
put(0.05, whoosh(0.65, 600, 1800, 1.4, 0.5), W * 0.25)
put(0.3, whirr(1.62, 650, 1500), 0.12); wh(0.3, 0.5, 300, 2000, 1.0, 0.7, 0.45)
put(1.9, knock(115, 0.24), 0.2); put(1.92, paper(0.3), 0.12)
put(1.97, pop(700, 1300, 0.07), 0.09); put(2.02, pop(760, 1400, 0.07), 0.08)
put(TM['hook'] + 0.2, pop(480, 900, 0.09), 0.1); put(TM['hook'] + 0.3, ding(1760, 0.45), 0.05)
put(TM['ret0'] + 0.3, marker(0.42), MK)
put(TM['pj0'] + 0.05, tick(0.02, 3000), 0.08)
put(TM['hit0'] + 0.02, pop(380, 1100, 0.12), 0.14)
for j in range(4): put(TM['hit0'] + 0.47 + j * 0.2, tick(0.016, 2400 + 300 * (j % 2)), 0.04)
put(TM['hit0'] + 0.3, marker(0.4), MK)
# S2 · the pallet fills, the ledger swings in, ten parcels ship (hop, count tick + rising ding, delivery bump), stamp, flash
wh(TM['mis'] - 0.1, 0.35, 1600, 400, 1.0, 0.4, 0.3)
for k in range(10): put(TM['mis'] + 0.05 + (9 - k) * 0.045 + 0.16, knock(150 + 6 * k, 0.16), 0.06)
wh(TM['mis'] + 0.05, 0.6, 300, 2200, 1.0, 0.6, 0.5)
TS0, DT = TM['p10'] - 0.12, 0.215
for j in range(10):
    ts = TS0 + j * DT
    put(ts, pop(500, 800, 0.06), 0.05)
    put(ts + 0.3, tick(0.018, 3200), 0.07); put(ts + 0.32, ding(1318.5 * (1.0595 ** j), 0.35), 0.035)
    put(ts + 1.16, knock(170, 0.12), 0.035)
put(TM['p10'] + 0.35, marker(0.42), MK); put(TM['tc'] + 0.35, marker(0.45), MK)
put(TM['tc'] + 0.42, knock(110, 0.24), 0.16); put(TM['tc'] + 0.44, pop(600, 1200, 0.08), 0.1)
put(TM['pjl'] + 0.05, chime((1568, 2093), 0.8), 0.045)
# S3 · two parcels pop out at the houses and boomerang back (whirr + thud), the money flies back (whoosh + coin ding)
wh(TM['trs'], 0.8, 400, 1400, 0.9, 0.5, 0.3)
for k, tApp in enumerate((TM['dua'] + 0.2, TM['dua'] + 0.38)): put(tApp, pop(420, 900, 0.09), 0.09); put(tApp + 0.25, pop(800, 1500, 0.06), 0.06)
for t0 in (TM['dir'] - 0.02, TM['dir'] + 0.2):
    put(t0, whirr(1.16, 800, 1300), 0.1); put(t0 + 1.14, knock(120, 0.22), 0.17); put(t0 + 1.16, paper(0.25), 0.1)
put(TM['dir'] + 0.3, marker(0.42), MK)
for k, t0 in enumerate((TM['uang'] + 0.02, TM['uang'] + 0.2)):
    put(t0, whoosh(0.9, 500, 2400, 1.2, 0.5), W * 0.5); put(t0 + 0.9, ding(2349 + 300 * k, 0.4), 0.05); put(t0 + 0.92, knock(190, 0.1), 0.05)
put(TM['uang'] + 0.75, marker(0.38), MK)
# S4 · the yard blurs, the ledger comes forward, ghost row, "?" pips, the number inflates, bars grow
wh(TM['kal'] - 0.05, 0.8, 1800, 300, 0.9, 0.5, 0.45); wh(TM['kal'], 0.7, 300, 1600, 1.0, 0.6, 0.4)
wh(TM['ndc'], 0.4, 800, 2200, 1.3, 0.5, 0.25)
for k in range(2): put(TM['ndc'] + 0.3 + k * 0.12, pop(500 + 200 * k, 1100 + 200 * k, 0.08), 0.09)
put(TM['pjm'] + 0.05, inflate(0.55), 0.09)
wh(TM['klh'] - 0.1, 0.4, 600, 2000, 1.2, 0.6, 0.25)
put(TM['klh'] + 0.2, whoosh(0.6, 400, 3000, 1.8, 0.3), W * 0.35); put(TM['asli'], whoosh(0.5, 400, 2400, 1.8, 0.3), W * 0.35)
put(TM['gede'] + 0.25, marker(0.4), MK)
# S5 · the ledger slides left, the rekening card flies in, flash, ≠ with a soft mismatch buzz
wh(TM['pad'], 0.5, 1200, 400, 1.0, 0.4, 0.3); wh(TM['pad'] + 0.2, 0.7, 300, 2200, 1.0, 0.6, 0.55)
put(TM['umsk'] + 0.02, ding(1760, 0.4), 0.05)
put(TM['ngk'] + 0.05, pop(420, 900, 0.1), 0.12); put(TM['ngk'] + 0.1, nope(0.34), 0.07)
put(TM['ngk'] + 0.3, marker(0.4), MK)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S6 · brand: card swings up, hologram, underline, scan + link spin, values pop, ≠, selisih row, chip, flash + stabilo
wh(TM['sol'] + 0.3, 0.8, 250, 2200, 1.0, 0.5, 0.55)
holo_fx(TM['sol'] + 0.55)
put(TM['rek'] + 0.6, marker(0.45), MK)
put(TM['cocok'], shimmer(0.9), 0.04); wh(TM['cocok'], 0.9, 500, 3200, 1.6, 0.5, 0.3)
put(TM['cat'], pop(520, 1000, 0.08), 0.1); put(TM['cat'] + 0.05, ding(1568, 0.4), 0.04)
put(TM['um'], pop(560, 1080, 0.08), 0.1); put(TM['um'] + 0.05, ding(1760, 0.4), 0.04)
put(TM['um'] + 0.7, pop(420, 900, 0.1), 0.1); put(TM['um'] + 0.75, nope(0.34), 0.05)
wh(TM['jadi'] + 0.05, 0.45, 400, 1800, 1.1, 0.6, 0.35)
put(TM['kel'], pop(600, 1200, 0.09), 0.11)
put(TM['sel'] - 0.02, chime((1318.5, 1760, 2637), 1.1), 0.05); put(TM['sel'] + 0.15, marker(0.38), MK); put(TM['sel'] + 0.55, marker(0.4), MK * 0.9)
for g0 in (TM['rek'] + 1.0, TM['jadi'] + 1.4, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
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
