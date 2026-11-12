"""Synthesised SFX for MasterPajak AI Video 19 (Jualan di Banyak Tempat, Catatannya Satu) — sits under the VO (no samples, no
music, per the client's rule). Beat times are parsed from window.TM in index.html, so a VO re-time only needs
`python3 tools/sfx.py` again. Deterministic.
Sounds: a soft brook bed under the paper map (synthesised bubbles), river draw-in trickles, pool "bloops", camera fly-overs,
signs rising (knock + rising ding per place), token pops, kind chips (pop + ding) with ring shimmers, tokens jumping into their
own notes (flick + paper tap), the tangle scribbles, the "untung?" card thud, the "ribet" paper rattle, band sweep, hologram fx,
the three rivers merging (lake fill bloop, ripple chimes, token plops), card lift + row fills, trace sweep, rekonsiliasi checks
(two dings + a soft low "perlu dicek" double-tone), beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav.
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
rng = np.random.default_rng(19)
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

def bubble(f0=700, dur=0.05):
    """one water bubble: a short sine chirp rising in pitch, fast decay"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (1 + 1.6 * t / dur)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 70) * np.minimum(1, t / 0.002)

def brook(t0, t1, rate=18, g=0.03, fmin=500, fmax=1500):
    """a gentle stream: random bubbles + a soft band of water noise"""
    k = int((t1 - t0) * rate)
    for _ in range(k):
        t = t0 + rng.random() * (t1 - t0); put(t, bubble(fmin + rng.random() * (fmax - fmin), 0.03 + rng.random() * 0.05), g * (0.4 + 0.6 * rng.random()))
    n = int((t1 - t0) * SR); x = svf_bp(rng.standard_normal(n), np.full(n, 1100.0), 0.7)
    e = np.minimum(1, np.minimum(np.arange(n) / (0.4 * SR), (n - np.arange(n)) / (0.4 * SR)))
    put(t0, x / (np.abs(x).max() + 1e-9) * e, g * 0.35)

def bloop(f0=260, f1=520, dur=0.22):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 16) * np.minimum(1, t / 0.004)
    return x / np.abs(x).max()

def rattle(dur=0.5):
    """paper rattle: a train of short papery taps"""
    o = np.zeros(int(dur * SR))
    for j in range(int(dur / 0.045)):
        p_ = paper(0.08); i = int(j * 0.045 * SR + rng.random() * 300); m = min(len(o), i + len(p_)); o[i:m] += p_[: m - i] * (0.6 + 0.4 * rng.random())
    return o / np.abs(o).max()

CH = [TM['chA'], TM['chB'], TM['chC']]
# S1 · hook: brook bed, three rivers draw in, three pools bloop, notes pop scattered, stabilo on "kepencar"
brook(0.0, TM['pisah'] + 0.9, 16, 0.028)
wh(0.0, 2.4, 200, 900, 0.9, 0.5, 0.35)
for i in range(3):
    put(0.12 + i * 0.16, whoosh(1.9, 500 + 150 * i, 1800 + 200 * i, 1.6, 0.5), W * 0.18)
    put(1.85 + i * 0.16 + 0.05, bloop(220 + 40 * i, 480 + 60 * i, 0.24), 0.11)
put(TM['hook'] + 0.0, pop(500, 900, 0.08), 0.06); put(TM['hookB'] - 0.1, pop(520, 950, 0.08), 0.07); put(TM['kep'] - 0.1, pop(560, 1000, 0.08), 0.07)
for i in range(3): put(TM['kep'] - 0.02 + i * 0.12, paper(0.22), 0.1); put(TM['kep'] + i * 0.12, pop(700 + 120 * i, 1300 + 150 * i, 0.07), 0.07)
put(TM['kep'] + 0.35, marker(0.42), MK)
# S2 · fly to the sources; each place's sign rises (knock + rising ding), its spring pulses, its tokens pop onto the current
wh(TM['chA'] - 0.15, 1.05, 250, 1800, 0.9, 0.55, 0.7)
for i, t in enumerate(CH):
    put(t - 0.02, knock(150 + 20 * i, 0.2), 0.12); put(t + 0.06, ding(1568 * (1.0595 ** (3 * i)), 0.5), 0.06)
    put(t + 0.05, bloop(300 + 60 * i, 700 + 80 * i, 0.18), 0.06)
    for k in range(3): put(t + 0.2 + k * 0.14, pop(600 + 100 * k + 60 * i, 1150 + 120 * k, 0.07), 0.06)
# S3 · crane over the rivers; three kinds: chip pop + ding, rings shimmer on the tokens of that kind
wh(TM['bent'] - 0.05, 1.15, 300, 1500, 0.9, 0.55, 0.55)
put(TM['bent'] - 0.1, pop(520, 950, 0.08), 0.06)
for k, t in enumerate((TM['pes'], TM['pot'], TM['cair'])):
    put(t - 0.06, pop(650 + 80 * k, 1300 + 100 * k, 0.08), 0.12); put(t - 0.02, ding(2093 * (1.0595 ** (2 * k)), 0.5), 0.06)
    put(t + 0.02, shimmer(0.5), 0.03)
# S4 · fly downstream; every token jumps into its own note (flick + paper tap), notes pop back, scribbles, the "untung?" card, ribet rattle
wh(TM['pisah'] - 0.05, 1.15, 400, 1700, 0.9, 0.55, 0.55)
for i in range(3): put(TM['pisah'] - 0.08 + i * 0.06, paper(0.2), 0.08)
for r in range(3):
    for k in range(3):
        tf = TM['pisah'] - 0.02 + r * 0.1 + (2 - k) * 0.12
        put(tf, whoosh(0.35, 900, 2600, 1.4, 0.4), W * 0.16); put(tf + 0.48, paper(0.12), 0.07); put(tf + 0.48, tick(0.016, 3800), 0.04)
for i in range(3): put(TM['untung'] - 0.38 + i * 0.12, marker(0.7), MK * 0.6)
put(TM['untung'] - 0.36, knock(110, 0.3), 0.14); put(TM['untung'] - 0.3, pop(380, 760, 0.12), 0.1)
for j in range(9): put(TM['untung'] + 0.3 + j * 0.2, tick(0.02, 3000 + 400 * (j % 3)), 0.03)
put(TM['ribet'] + 0.05, rattle(0.55), 0.09); put(TM['ribet'] + 0.05, marker(0.36), MK)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S5 · brand: glowing rivers (soft brook), hologram, the merge (lake fill bloop + ripple chimes + token plops), card lift, rows, trace
brook(TM['sol'], TM['pemb'] + 0.4, 12, 0.022, 700, 1900)
holo_fx(TM['sol'] + 0.55)
put(TM['satu'] - 0.1, bloop(160, 420, 0.5), 0.16); wh(TM['satu'] - 0.1, 0.8, 200, 1200, 0.8, 0.4, 0.45)
for k in range(3): put(TM['satu'] + 0.35 + k * 0.38, chime((1318.5 * (1.0595 ** (2 * k)), 1975.5 * (1.0595 ** (2 * k))), 0.9), 0.035)
for j in range(9): put(TM['satu'] + 0.2 + (j % 3) * 0.22 + (j // 3) * 0.08, bubble(500 + 90 * j, 0.06), 0.08)
wh(TM['pemb'] - 0.42, 0.9, 250, 2400, 1.0, 0.45, 0.6)
for k in range(4): put(TM['pemb'] + 0.2 + k * 0.16, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.1)
put(TM['pemb'] + 0.35, marker(0.45), MK)
put(TM['telus'] - 0.05, shimmer(0.7), 0.04)
for k in range(6): put(TM['telus'] + 0.1 + k * 0.07, tick(0.014, 3400 + 200 * k), 0.05)
for g0 in (TM['pemb'] + 0.9, TM['cek'] + 0.6, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# S6 · rekonsiliasi: the pembukuan recedes, the card lifts, two checks ding, the third gets a soft low double tone, summary pop
wh(TM['rek'], 0.8, 1600, 300, 0.9, 0.5, 0.35); wh(TM['rek'] + 0.18, 0.8, 250, 2400, 1.0, 0.45, 0.6)
put(TM['cek'] + 0.1, pop(700, 1400, 0.07), 0.12); put(TM['cek'] + 0.14, ding(2093, 0.55), 0.07)
put(TM['cek'] + 0.75, pop(760, 1500, 0.07), 0.12); put(TM['cek'] + 0.79, ding(2349, 0.55), 0.07)
put(TM['cocok'] + 0.2, pop(500, 900, 0.09), 0.12); put(TM['cocok'] + 0.24, ding(740, 0.3), 0.06); put(TM['cocok'] + 0.38, ding(622, 0.35), 0.06)
put(TM['cocok'] + 0.5, marker(0.35), MK * 0.8); put(TM['cocok'] + 0.35, marker(0.45), MK * 0.7)
put(TM['masuk'] - 0.1, pop(600, 1200, 0.08), 0.1)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'] - 0.1, pop(500, 1000, 0.12), P_); put(TM['bio'] - 0.05, pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.2, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
