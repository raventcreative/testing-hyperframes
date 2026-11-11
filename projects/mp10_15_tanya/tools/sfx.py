"""Synthesised SFX for MasterPajak AI Video 15 (Tanya Cepat ke Robot) — sits under the VO (no samples, no music, per the client's rule).
Deterministic. All beat times are parsed from window.TM in index.html, so a VO re-time only needs a re-run.
Hook: robot pop-up, title thud, stabilo, three ascending badge pops; dive whoosh; chat "ding" per question, typing ticks, answer pops,
check-stamp thud, bar rise, marker strokes; chat-scroll whoosh + counter ticks; book drop + heavy thud, flick whoosh, strike scribble;
band sweep, hologram fx, paper flutter, notes docking into the report; whip pan; ta-da shimmer; beam + iris boom; end card.
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
rng = np.random.default_rng(15)
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

def thud(dur=0.5, f0=120, f1=45):
    """book / stamp landing: short pitched-down body + a papery slap"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 11)
    sl = svf_bp(rng.standard_normal(n), np.full(n, 900.0), 0.9) * np.exp(-t * 45) * 0.7
    x = np.tanh(2.2 * (x + sl))
    return x / np.abs(x).max()

def pop(f0=900, f1=320, dur=0.09):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 38)
    return x / np.abs(x).max()

def tick(dur=0.025, f=4200):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, f), 2.0) * np.exp(-t * 260)
    return x / (np.abs(x).max() + 1e-9)

def ding(f=(1318.5, 1975.5), dur=0.55):
    """soft two-tone chat notification"""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, fr in enumerate(f):
        d = int(k * 0.085 * SR); tt = t[: n - d]
        x[d:] += (np.sin(2 * np.pi * fr * tt) + 0.25 * np.sin(4 * np.pi * fr * tt)) * np.exp(-tt * 9) * (0.85 ** k)
    return x / np.abs(x).max()

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

def flutter(dur=0.8):
    """paper sheets fluttering: band-passed noise with a fast irregular amplitude flap"""
    n = int(dur * SR); t = np.arange(n) / SR
    flap = 0.45 + 0.55 * np.abs(np.sin(2 * np.pi * (17 + 6 * np.sin(2 * np.pi * 1.3 * t)) * t))
    x = svf_bp(rng.standard_normal(n), 1800 + 900 * np.sin(2 * np.pi * 2.2 * t), 1.3) * flap * env(n, 0.3)
    return x / np.abs(x).max()

def scribble(dur=0.35):
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 13 * t))
    x = svf_bp(rng.standard_normal(n), 2600 + 900 * np.sin(2 * np.pi * 6.5 * t), 1.6) * am * env(n, 0.2)
    return x / np.abs(x).max()

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def rise(dur=0.5, f0=420, f1=980):
    """little tonal rise for the 'untung' bar filling"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * env(n, 0.5, 1.5)
    return x / np.abs(x).max()

W, P_, MK = 0.22, 0.15, 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)
def typing(t0, t1):
    t = t0; k = 0
    while t < t1 - 0.05:
        put(t, tick(0.012, 3400 + 500 * (k % 3)), 0.05); t += 0.09 + 0.05 * ((k * 7) % 3) / 2; k += 1

# S0 · hook: the robot pops up, title, stabilo, three numbered badges
wh(0.02, 0.6, 200, 1500, 1.0, 0.5, 0.45); put(0.6, pop(260, 520, 0.14), 0.12)
put(0.15, pop(700, 1300, 0.08), 0.11)                                    # kicker
put(TM['hook'] + 0.05, thud(0.35, 160, 70), 0.10); put(TM['hook'] + 0.12, pop(500, 1000, 0.1), 0.10)   # "3" tile
put(TM['hook'] + 1.55, marker(0.42), MK)
for k in range(3): put(TM['hook'] + 1.95 + k * 0.27, pop(700 + 220 * k, 1300 + 260 * k, 0.08), 0.13)
# dive into the bubble field -> Q1
dv = TM['q1'] - 0.58
wh(dv, 0.75, 250, 3200, 1.0, 0.75, 0.9); wh(dv + 0.2, 0.45, 1500, 500, 1.2, 0.3, 0.35)
# S1 · Q1
put(TM['q1'] + 0.05, ding(), 0.09); put(TM['q1'] + 0.35, tick(0.012, 3000), 0.06)
typing(TM['a1'] - 0.8, TM['a1'])
put(TM['a1'], pop(420, 900, 0.12), P_); wh(TM['a1'] - 0.05, 0.5, 300, 1600, 1.0, 0.6, 0.35)
put(TM['a1'] + 0.45, thud(0.4, 140, 60), 0.12); put(TM['a1'] + 0.45, pop(1200, 1800, 0.06), 0.06)   # check stamp lands
put(TM['a1'] + 1.62, marker(0.5), MK); put(TM['a1'] + 1.75, rise(0.5), 0.05)
# chat scroll Q1 -> Q2 (vertical whip) + counter ticks
sc = TM['q2'] - 0.46
wh(sc, 0.62, 300, 2400, 1.0, 0.55, 0.85)
for j in range(3): put(TM['q2'] - 0.22 + j * 0.07, tick(0.012, 4200), 0.07)
# S2 · Q2: ding, book drop + heavy thud, head shake, flick, card, strike
put(TM['q2'] + 0.07, ding((1174.7, 1760)), 0.09)
bk = TM['q2'] + 1.0
wh(bk, 0.42, 1400, 300, 1.0, 0.85, 0.35); put(bk + 0.42, thud(0.55, 110, 40), 0.17); put(bk + 0.42, boom(0.5, 90, 40), 0.06)
wh(TM['a2'] - 0.02, 0.45, 400, 2800, 1.1, 0.4, 0.6)                       # book flicked away
put(TM['a2'] + 0.1, pop(420, 900, 0.12), P_); put(TM['a2'] + 0.62, scribble(0.3), 0.07)
# band sweep -> brand (hologram), notes flutter, dock into the report, marker on laba
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
put(TM['sol'] + 0.45, flutter(0.9), 0.06); put(TM['sol'] + 1.6, flutter(0.7), 0.035)
put(TM['lap'] - 0.1, pop(500, 1000, 0.12), P_)
for j in range(4): put(TM['lap'] + 0.74 + j * 0.16, pop(900 + 120 * j, 1500 + 140 * j, 0.06), 0.09)
put(TM['lap'] + 1.15, tick(0.012, 3000), 0.07); put(TM['lap'] + 1.55, marker(0.45), MK)
for g0 in (TM['sol'] + 2.6, TM['sol'] + 4.4, TM['end'] + 4.4, TM['end'] + 7.0): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# whip pan -> Q3 + counter ticks
wh(TM['q3'] - 0.44, 0.6, 250, 2600, 1.0, 0.7, 0.9)
for j in range(3): put(TM['q3'] - 0.2 + j * 0.07, tick(0.012, 4200), 0.07)
# S4 · Q3: ding, typing, ta-da (chest glow shimmer), cards, marker on "sesuai layanan"
put(TM['q3'] + 0.09, ding((1396.9, 2093)), 0.09)
typing(TM['a3'] - 0.8, TM['a3'])
put(TM['a3'], pop(420, 900, 0.12), P_); put(TM['a3'] + 0.3, chime((1568, 2093, 2637), 0.9), 0.04)
put(TM['tim'], pop(460, 980, 0.12), P_)
for k in range(3): put(TM['tim'] + 0.45 + k * 0.1, pop(900 + 150 * k, 1400, 0.05), 0.06)
put(TM['tim'] + 1.05, marker(0.45), MK)
# beam + iris -> end card
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 0.6, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
