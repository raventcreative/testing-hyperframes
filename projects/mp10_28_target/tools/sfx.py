"""Synthesised SFX for MasterPajak AI Video 28 (Target Bulan Depan dari Data, Bukan Feeling) — sits under the VO (no samples, no music).
Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again. Deterministic.
Sounds: outdoor range air, title pops, stabilo marker, a wobble on "feeling?", the long pull-back whoosh, a creaky unsure bow draw +
twang + a fluttering whistle + a dull thud in the turf + the X stamp for the feeling arrow; the whip back to the bow, the data
arrow nocked (click), the card swinging in, each figure peeling off its row (tick, whoosh) and snapping into the fletching (pop +
knock); a steady draw, the aim line, twang, a clean whistle and a THWACK into the straw boss with a shimmer, the result tag and the
"masuk akal" ding; band sweep, hologram fx, brand card + row pops, "tiap bulan" pop, the mini arrow thwack, beam/iris boom, end pops
+ chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py [project dir]"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(28)
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
    k = max(1, int(n * a)); e = np.ones(n)
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
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 7) + 0.35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 14)
    return x / np.abs(x).max()

def marker(dur=0.4):
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def knock(f=150, dur=0.22):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 26) + 0.5 * np.sin(2 * np.pi * f * 1.9 * t) * np.exp(-t * 40)
    x += svf_bp(rng.standard_normal(n), np.full(n, 1300.0), 1.0) * np.exp(-t * 70) * 0.5
    return x / np.abs(x).max()

def shimmer(dur=0.8):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(4000, 9000, n), 3.0) * env(n, 0.4)
    return x / np.abs(x).max()


# ---------- archery sounds (synthesised) ----------
def twang(f=150, dur=0.7):
    """bow string release: a plucked low string (harmonics with fast decays, slight pitch drop) + a dry click"""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    fp = f * (1 + 0.06 * np.exp(-t * 30))
    for h, a, d in ((1, 1.0, 9), (2, 0.55, 13), (3, 0.35, 18), (4, 0.2, 24), (6, 0.1, 30)):
        x += a * np.sin(2 * np.pi * np.cumsum(fp * h) / SR) * np.exp(-t * d)
    x += svf_bp(rng.standard_normal(n), np.full(n, 2600.0), 1.2) * np.exp(-t * 160) * 0.8
    return x / np.abs(x).max()

def creak(dur=0.55, rate0=30, rate1=70, f=900):
    """bow being drawn: stick-slip creak (ticks speeding up) over a band-passed rub"""
    n = int(dur * SR); x = np.zeros(n + 3000); tt = 0.0; k = 0
    while tt < dur:
        r = rate0 + (rate1 - rate0) * tt / dur; i = int(tt * SR)
        c = tick(0.018, f * (0.9 + 0.2 * rng.random())); x[i:i + len(c)] += c * (0.35 + 0.4 * tt / dur); tt += 1.0 / r; k += 1
    u = np.linspace(0, 1, n)
    rub = svf_bp(rng.standard_normal(n), 500 + 500 * u, 2.5) * env(n, 0.7, 1.2) * 0.5
    x[:n] += rub
    return x / np.abs(x).max()

def flutter(dur=0.7, f0=2400, f1=900, am=16, depth=0.7):
    """an arrow in flight: a whistle-whoosh; am > 0 adds the wobbly flutter of a badly shot arrow"""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    x = svf_bp(rng.standard_normal(n), f0 * (f1 / f0) ** u, 3.0) * env(n, 0.25, 1.4)
    if am: x *= (1 - depth) + depth * (0.5 + 0.5 * np.sin(2 * np.pi * am * t))
    return x / (np.abs(x).max() + 1e-9)

def thwack(dur=0.45):
    """arrow into the straw boss: a hard low knock + a crunchy straw burst"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 105 * t) * np.exp(-t * 22) + 0.6 * np.sin(2 * np.pi * 240 * t) * np.exp(-t * 35)
    x += svf_bp(rng.standard_normal(n), np.full(n, 1800.0), 0.9) * np.exp(-t * 45) * 0.9
    x += svf_bp(rng.standard_normal(n), np.full(n, 5200.0), 1.0) * np.exp(-t * 90) * 0.4
    return np.tanh(1.4 * x) / np.tanh(1.4)

def thud(dur=0.4):
    """arrow into the turf: dull and soft, with a little dirt"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 72 * t) * np.exp(-t * 18) + svf_bp(rng.standard_normal(n), np.full(n, 700.0), 0.8) * np.exp(-t * 30) * 0.7
    return x / np.abs(x).max()

def boing(f0=330, f1=220, dur=0.45):
    """a soft unsure 'hmm' wobble for "feeling?" (pitch wobble on a sine)"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (f1 / f0) ** (t / dur) * (1 + 0.06 * np.sin(2 * np.pi * 9 * t))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.1, 1.5)
    return x / np.abs(x).max()

def laser(dur=0.4, f0=900, f1=2400):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * env(n, 0.3, 1.5) * 0.6 + svf_bp(rng.standard_normal(n), np.linspace(3000, 7000, n), 3.0) * env(n, 0.4) * 0.4
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)
def cpop(t, g=0.06): put(t, pop(540, 980, 0.08), g)

# S1 · hook: outdoor range air, title pops, marker on "data", a wobble on "feeling?", the long pull-back down the lane
wh(0.0, 4.2, 180, 700, 0.9, 0.5, 0.28)
cpop(TM['hook'] - 0.12, 0.07); cpop(TM['data'] - 0.3); cpop(TM['atau'] - 0.1); cpop(TM['feel'] - 0.1, 0.07)
put(TM['data'] + 0.3, marker(0.35), MK)
put(TM['feel'] + 0.3, boing(360, 250, 0.42), 0.05)
wh(2.0, 2.1, 250, 1300, 0.9, 0.55, 0.55)
# S2 · "pakai feeling": a creaky, unsure draw; twang; a fluttering arrow that whistles off; a dull thud in the turf; the X stamp
cpop(TM['kal'] - 0.08); cpop(TM['sering'] - 0.14); cpop(TM['ngk'] - 0.12); cpop(TM['sas'] - 0.1)
put(TM['feel2'] - 0.05, creak(0.6, 24, 46, 820), 0.09)
tR = TM['sering'] + 0.02; tL = TM['sas'] - 0.04
put(tR, twang(140, 0.7), 0.16); put(tR + 0.03, flutter(tL - tR + 0.05, 2200, 700, 15, 0.75), 0.17)
wh(tR + 0.05, 0.55, 300, 1500, 1.0, 0.5, 0.45)
put(tL, thud(0.4), 0.2); put(tL + 0.02, tick(0.03, 1500), 0.05)
put(tL + 0.06, pop(700, 300, 0.12), 0.12); put(tL + 0.2, square_blips([520, 390], 0.09), 0.025)
put(TM['kena'] + 0.15, marker(0.32), MK)
# S3 · whip back to the bow, the data arrow is nocked (click), the card swings in, each figure: row flash, peel whoosh, snap into the fletching
wh(TM['bidik'] - 0.12, 0.42, 2600, 400, 1.0, 0.35, 0.65); wh(TM['bidik'] + 0.12, 0.5, 400, 3000, 1.2, 0.5, 0.8)
cpop(TM['bidik'] - 0.02); cpop(TM['data2'] - 0.15)
tUp = TM['bidik'] + 0.42
wh(tUp, 0.6, 400, 1600, 1.0, 0.5, 0.3); put(tUp + 0.62, tick(0.02, 2400), 0.09); put(tUp + 0.64, knock(300, 0.1), 0.05)
put(TM['blnl'] + 0.1, marker(0.36), MK)
wh(TM['lihat'] - 0.1, 0.7, 300, 1800, 1.0, 0.45, 0.45); cpop(TM['lihat'] + 0.5, 0.06)
cpop(TM['apa'] - 0.14); cpop(TM['brp'] - 0.06); cpop(TM['dbrp'] - 0.06)
PEEL = [(TM['apa'] + 0.05, TM['benar'] - 0.02), (TM['modal'] - 0.05, TM['modal'] + 0.08), (TM['biaya'] - 0.05, TM['biaya'] + 0.1), (TM['laba'] - 0.05, TM['laba'] + 0.08)]
for k, (tf, t0) in enumerate(PEEL):
    put(tf, tick(0.02, 3000 + 200 * k), 0.06)
    wh(t0, 0.62, 700, 2600, 1.3, 0.4, 0.32)
    put(t0 + 0.62, pop(900 + 60 * k, 1700, 0.06), 0.1); put(t0 + 0.63, knock(420 + 30 * k, 0.09), 0.06)
put(TM['laku'] + 0.1, marker(0.26), MK); put(TM['biaya'] + 0.05, marker(0.3), MK); put(TM['laba'] + 0.2, marker(0.3), MK)
# S4 · a steady, clean draw; the aim line; twang; a clean whistle (no flutter); THWACK in the inner rings; tag pops; "masuk akal" ding
cpop(TM['dari'] - 0.04); cpop(TM['target'] - 0.14); cpop(TM['jadi'] - 0.12); cpop(TM['masuk'] - 0.12)
put(TM['dari'] + 0.12, creak(0.5, 34, 40, 1000), 0.06)
put(TM['dari'] + 0.42, laser(0.35, 900, 2600), 0.035)
tRel = TM['target'] - 0.5
put(tRel, twang(155, 0.7), 0.17); put(tRel + 0.02, flutter(0.5, 3200, 1400, 0, 0), 0.15)
wh(tRel, 0.6, 350, 2400, 1.0, 0.55, 0.6)
put(TM['target'], thwack(0.45), 0.3); put(TM['target'] + 0.05, shimmer(0.7), 0.025)
wh(TM['target'] + 0.12, 0.5, 500, 2200, 1.2, 0.4, 0.3); put(TM['target'] + 0.3, pop(600, 1200, 0.08), 0.1)
put(TM['masuk'] + 0.05, pop(800, 1500, 0.07), 0.1); put(TM['masuk'] + 0.12, ding(2093, 0.5), 0.05)
put(TM['akal'] + 0.25, marker(0.4), MK)
# band sweep -> brand: hologram, card fly-in, row pops, underline, row glows, "tiap bulan" pop, mini target + mini arrow thwack, chip
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
wh(TM['sol'] + 0.15, 0.85, 250, 1900, 1.0, 0.45, 0.5)
for k in range(4): put(TM['sol'] + 0.7 + k * 0.12, pop(520 + 60 * k, 1050 + 90 * k, 0.07), 0.08)
put(TM['lrb'] + 0.6, marker(0.45), MK)
for k in range(4): put(TM['lrb'] + 0.1 + k * 0.15, tick(0.02, 3000 + 250 * k), 0.05)
put(TM['tiap'] - 0.08, pop(500, 1100, 0.1), 0.12)
for g0 in (TM['lrb'] + 0.3, TM['biar'] + 0.4, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
wh(TM['biar'] - 0.05, 0.6, 300, 1600, 1.0, 0.45, 0.35)
put(TM['tgt2'] - 0.26, flutter(0.26, 3000, 1500, 0, 0), 0.1); put(TM['tgt2'], thwack(0.4), 0.18)
put(TM['tgt2'] + 0.12, pop(700, 1400, 0.08), 0.1)
put(TM['data3'] + 0.05, marker(0.4), MK)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'] - 0.1, pop(500, 1000, 0.12), P_); put(TM['bio'] - 0.05, pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.0, chime((784, 1046, 1568), 1.3), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s", "rms dB", round(20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9), 1))
