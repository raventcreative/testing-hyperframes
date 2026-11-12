"""Synthesised SFX for MasterPajak AI Video 26 (Reseller & Dropship: Uang Lewat vs Untung) — sits under the VO (no samples, no music).
Beat times are parsed from window.TM in index.html (real VO word times + 0.30 s), so `python3 tools/sfx.py` after any re-time.
Sounds: stadium air, tag pops, starter whistles, footfalls on the track (same stride maths as the film's run cycles), baton glint,
coin-stream whoosh + dings, changeover clacks, the split zipper, coin chime on OMZET, stub ding + UNTUNG chime, scoreboard clunk +
lamp ticks + LED blips, "eh-eh" on "nggak dicatat", "?" wobble, strike scratch, stabilo markers, band sweep, hologram fx, row
fly-ins, beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py [project dir]"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(26)
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

def whistle(dur=0.45, f=2600):
    """referee/starter whistle: a trilled sine with breath noise"""
    n = int(dur * SR); t = np.arange(n) / SR
    fm = f * (1 + 0.025 * np.sign(np.sin(2 * np.pi * 28 * t)))
    x = np.sin(2 * np.pi * np.cumsum(fm) / SR) * env(n, 0.08, 1.0) + 0.25 * svf_bp(rng.standard_normal(n), np.full(n, f), 3.0) * env(n, 0.1)
    return x / np.abs(x).max()

def step(f=95, dur=0.09):
    """soft rubber-track footfall"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 55) + svf_bp(rng.standard_normal(n), np.full(n, 900.0), 1.2) * np.exp(-t * 90) * 0.5
    return x / np.abs(x).max()

def clack(dur=0.12):
    """baton changeover: a bright hollow tube clack"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 820 * t) * np.exp(-t * 45) + 0.6 * np.sin(2 * np.pi * 1960 * t) * np.exp(-t * 70)
    x += svf_bp(rng.standard_normal(n), np.full(n, 3200.0), 1.5) * np.exp(-t * 120) * 0.6
    return x / np.abs(x).max()

def zipup(dur=0.5):
    """the split reveal: a rising zipper (pulse train with an upward sweep)"""
    n = int(dur * SR); t = np.arange(n) / SR
    rate = 40 + 90 * t / dur
    pulses = (np.sin(2 * np.pi * np.cumsum(rate) / SR) > 0.85).astype(float)
    x = svf_bp(rng.standard_normal(n) * (0.3 + pulses), np.linspace(900, 3600, n), 1.6) * env(n, 0.2)
    return x / np.abs(x).max()

def clunk(dur=0.5):
    """scoreboard power-on: low mechanical clunk + hum"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 70 * t) * np.exp(-t * 14) + 0.4 * np.sign(np.sin(2 * np.pi * 120 * t)) * np.exp(-t * 6) * 0.3
    x += svf_bp(rng.standard_normal(n), np.full(n, 500.0), 1.0) * np.exp(-t * 40) * 0.6
    return x / np.abs(x).max()

def scratch(dur=0.32):
    """felt strike-through"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(1800, 3400, n), 1.4) * np.minimum(1, t / 0.02) * np.minimum(1, (dur - t) / 0.05)
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)
def steps(t0, t1, g=0.05, f=95):
    n = max(1, round((t1 - t0) / 0.19)); d = (t1 - t0) / n
    for k in range(1, n + 1): put(t0 + k * d - 0.02, step(f + 14 * (k % 2), 0.09), g)

H1, H2 = TM['omz'], TM['oper']
# S1 · hook: stadium air, Kamu's tag, "lari estafet" (whistle, the runners get set, the baton glints), the coin stream
wh(0.0, 2.6, 200, 700, 0.9, 0.5, 0.3)
put(TM['hook'] + 0.1, pop(520, 1000, 0.09), 0.1)
put(TM['est'] + 0.15, whistle(0.42, 2700), 0.05)
put(TM['est'] + 0.35, pop(560, 1050, 0.08), 0.08)
put(TM['est'] + 0.75, pop(700, 1400, 0.08), 0.1); put(TM['est'] + 1.0, shimmer(0.5), 0.05)
wh(TM['est'] - 0.1, 1.5, 1600, 400, 0.9, 0.5, 0.35)
tc0 = TM['nump'] - 0.1
put(tc0, whoosh(1.3, 400, 3200, 1.3, 0.4), W * 0.6)
for k in range(6): put(tc0 + 0.18 + k * 0.07, ding(1760 * (1.0595 ** (k * 2)), 0.3), 0.025)
put(TM['lewat'] + 0.05, marker(0.42), MK)
# S2 · the first leg: start whistle, footfalls, the price tag, changeover clack on "omzetmu", OMZET badge + coin chime
put(TM['pmb'] - 0.12, whistle(0.3, 2900), 0.045)
wh(TM['pmb'] - 0.45, 1.3, 300, 1500, 1.0, 0.5, 0.35)
steps(TM['pmb'], H1, 0.045); steps(H1, H1 + 0.55, 0.035)
steps(H1 - 0.75, H1, 0.04, 110)
put(TM['r100'], pop(600, 1150, 0.08), 0.1); put(TM['r100'] + 0.04, ding(1568, 0.35), 0.035)
put(H1 - 0.01, clack(0.12), 0.16); wh(H1 - 0.05, 0.4, 600, 2600, 1.2, 0.4, 0.3)
put(H1 + 0.12, pop(500, 1000, 0.09), 0.1); put(H1 + 0.16, chime((1568, 2093, 2637), 0.9), 0.05)
put(H1 + 0.3, marker(0.4), MK)
# S3 · the second leg: zipper on the split reveal, navy tag pops, changeover 2 clack, the supplier runs off with most of it
steps(H1, H2, 0.04, 110)
put(TM['d80'] + 0.05, zipup(0.5), 0.07); put(TM['d80'] + 0.35, pop(480, 950, 0.09), 0.1)
put(TM['lgs'], pop(560, 1050, 0.08), 0.07)
steps(H2 - 0.7, H2, 0.035, 80); steps(H2, H2 + 1.4, 0.03, 80)
put(H2 - 0.01, clack(0.12), 0.16); put(H2 + 0.02, whoosh(0.9, 2200, 400, 1.0, 0.3), W * 0.45)
steps(H2, H2 + 0.57, 0.035, 110)
# S4 · Kamu raises the stub: lift whoosh, Rp20.000 pop + ding, glint, UNTUNG badge, pill
wh(TM['ting'] + 0.15, 0.5, 400, 1800, 1.2, 0.5, 0.3)
put(TM['r20'] - 0.05, pop(620, 1200, 0.09), 0.12); put(TM['r20'], ding(2093, 0.45), 0.05); put(TM['r20'] + 0.2, shimmer(0.5), 0.04)
put(TM['r20'] + 0.45, marker(0.4), MK)
put(TM['itu2'], pop(480, 950, 0.09), 0.09)
put(TM['unt'] - 0.05, pop(700, 1400, 0.08), 0.1); put(TM['unt'] + 0.02, chime((1318.5, 1760, 2637), 1.0), 0.05)
# S5 · the scoreboard rises and powers on, row 1 + "dicatat", row 2 "nggak dicatat", the LED flips to 100.000, "?" wobble,
# strike-through + "aslinya" chip
wh(TM['kal'] - 0.35, 1.0, 200, 1200, 0.9, 0.5, 0.4); put(TM['kal'] + 0.2, clunk(0.5), 0.12)
for k in range(3): put(TM['kal'] + 0.3 + k * 0.08, tick(0.02, 3000 + 400 * k), 0.06)
put(TM['msk'] - 0.05, pop(520, 1000, 0.09), 0.08)
put(TM['dct'], pop(640, 1250, 0.08), 0.1); put(TM['dct'] + 0.04, ding(1760, 0.35), 0.04)
put(TM['dct'] + 0.45, pop(400, 800, 0.09), 0.07); put(TM['dct'] + 0.5, nope(0.34), 0.05)
put(TM['omz2'], square_blips([600, 900, 1200, 1500, 1800], 0.035), 0.05)
put(TM['klh'], pop(560, 1100, 0.08), 0.09)
put(TM['klh'] + 0.25, pop(380, 1100, 0.12), 0.12)
for j in range(3): put(TM['klh'] + 0.72 + j * 0.18, tick(0.016, 2400 + 300 * (j % 2)), 0.04)
put(TM['unt2'] + 0.05, scratch(0.32), 0.08); put(TM['unt2'] + 0.1, pop(620, 1200, 0.09), 0.11); put(TM['unt2'] + 0.15, ding(2093, 0.4), 0.04)
put(TM['unt2'] + 0.05, marker(0.4), MK)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S6 · brand: card swings up, hologram, underline, three baton pieces fly into the rows, laba stabilo
wh(TM['sol'] + 0.3, 0.8, 250, 2200, 1.0, 0.5, 0.55)
holo_fx(TM['sol'] + 0.55)
put(TM['dua2'] + 0.5, marker(0.45), MK)
for k, t in enumerate((TM['dari'] - 0.25, TM['keS'] - 0.2, TM['asli'] - 0.25)):
    wh(t, 0.55, 500, 2400, 1.2, 0.5, 0.3); put(t + 0.56, pop(520 + 60 * k, 1000 + 80 * k, 0.08), 0.1); put(t + 0.6, ding(1568 * (1.122 ** k), 0.35), 0.035)
put(TM['asli'] + 0.6, marker(0.42), MK); put(TM['asli'] + 0.75, marker(0.4), MK * 0.9)
put(TM['asli'] + 0.8, chime((1318.5, 1760, 2637), 1.1), 0.045)
for g0 in (TM['dua2'] + 0.9, TM['jadi'] + 1.2, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
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
