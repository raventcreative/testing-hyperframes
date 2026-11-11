"""Synthesised SFX for MasterPajak AI Video 12 (Uang Pribadi vs Uang Usaha). No samples, no music (client rule); sits under the VO.
Coin clinks (inharmonic partials) for every coin that drops through the slot or leaps out to an expense tile, a ratchet on the
UNTUNG gauge needle, a cork-pop when the lid blows off, a rising wind for the coin tornado with scattered jingles, glitch blips on
the scrambling numbers, a bright blade "zing" + impact on the split, pops on the lane signs, then the series brand/end cues
(band whooshes, hologram fx, docking pops, stabilo marker, beam + iris boom, CTA pops, chime). Every cue time is read from
window.TM in index.html, so a VO re-time moves the sound with the picture. Deterministic. Writes assets/audio/sfx.wav
(48 kHz mono, TM.total s). Run: python3 tools/sfx.py ."""
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

def clink(f=2600, dur=0.5, bright=1.0):
    """a coin: inharmonic partials (free metal disc), fast attack, a 4 ms noise strike"""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for r, a, d in ((1.0, 1.0, 9), (2.76, 0.62 * bright, 13), (5.40, 0.36 * bright, 19), (8.93, 0.2 * bright, 27)):
        x += a * np.sin(2 * np.pi * f * r * t + rng.random() * 6) * np.exp(-t * d)
    k = int(0.004 * SR); x[:k] += rng.standard_normal(k) * np.linspace(0.8, 0, k)
    return x / np.abs(x).max()

def slot_drop():
    """coin falls through the lid slot: clink, then a muffled thunk on the pile"""
    a = clink(2400 + rng.random() * 600, 0.32, 0.8)
    b = np.concatenate([np.zeros(int(0.07 * SR)), pop(320, 110, 0.08) * 0.7, np.zeros(int(0.2 * SR))])
    m = min(len(a), len(b)); return a[:m] * 0.8 + b[:m]

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

def zing(dur=0.55):
    """the light blade: a bright downward sweep with a shimmering top, then air"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 5200 * (900 / 5200) ** (t / dur) ** 0.7
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 6) * 0.7
    x += svf_bp(rng.standard_normal(n), f * 1.5, 3.0) * np.exp(-t * 7) * 0.5
    return x / np.abs(x).max()

def chime(freqs=(1318.5, 1760, 2637), dur=1.4):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate(freqs):
        d = int(k * 0.06 * SR); tt = t[: n - d]
        x[d:] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 3.5) * (0.8 ** k)
    return x / np.abs(x).max()

def wind(dur=5.0, f0=180, f1=900):
    """tornado: band-passed noise with a slow rising centre and a 3 Hz swirl modulation"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (f1 / f0) ** (t / dur) * (1 + 0.25 * np.sin(2 * np.pi * 3.1 * t))
    x = svf_bp(rng.standard_normal(n), f, 0.9) * env(n, 0.3, 1.0) * (0.75 + 0.25 * np.sin(2 * np.pi * 3.1 * t + 1))
    return x / np.abs(x).max()

def marker(dur=0.4):
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

W = 0.22; P_ = 0.15; MK = 0.11; CL = 0.085
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# S1 · income: chip whoosh in, two coins through the slot, tag roll ticks + needle up
TC = [TM['masuk'] - 0.25, TM['masuk'] + 0.27, TM['masuk'] + 0.79]
for k, t0 in enumerate(TC):
    wh(max(0, t0 - 0.05), 0.5, 500, 2200, 1.2, 0.5, 0.35)
    put(t0 + 0.5, pop(600, 1100, 0.06), 0.06)
    for j in range(2): put(t0 + 0.52 + j * 0.09 + 0.3, slot_drop(), CL)
    for q in range(4): put(t0 + 0.86 + q * 0.07, tick(0.012, 3800), 0.035)
# "eh, kepake buat ...": tile pops, two coins leap out of the slot (clink up, clink on the tile), the balance ticks down
TX = [TM['eh'] + 0.8, TM['cicil'] + 0.15, TM['kirim'] + 0.2]
for k, t0 in enumerate(TX):
    put(t0, pop(500 + 80 * k, 1000, 0.1), P_)
    for j in range(2):
        tj = t0 + 0.12 + j * 0.1
        put(tj, clink(3000 + 300 * j, 0.4, 1.0), CL * 0.9); wh(tj, 0.5, 900, 3000, 1.6, 0.5, 0.18)
        put(tj + 0.55, clink(2200 + 200 * j, 0.3, 0.6), CL * 0.7)
    for q in range(3): put(t0 + 0.18 + q * 0.08, tick(0.012, 3000 - 400 * q), 0.035)
    put(t0 + 0.2, pop(700, 260, 0.14), 0.06)
# S2 · whip to the gauge, needle hunts + collapses (ratchet), "?" pops
wh(TM['cek'] - 0.38, 0.5, 250, 2600, 1.0, 0.7, 0.9)
for t0, cnt in ((TM['cek'] + 0.35, 5), (TM['cek'] + 0.67, 4), (TM['cek'] + 0.97, 3), (TM['mana'] - 0.05, 9)):
    for q in range(cnt): put(t0 + q * 0.035, tick(0.01, 2600 + 300 * (q % 2)), 0.05)
put(TM['mana'] + 0.45, pop(1200, 300, 0.22), 0.07); put(TM['mana'] + 0.4, pop(400, 900, 0.12), P_)
# S3 · whip back, cork pop as the lid blows off, coin burst, tornado wind with jingles, "campur" stinger
wh(TM['campur'] - 0.38, 0.5, 250, 2600, 1.0, 0.7, 0.9)
tS0 = TM['campur'] + 0.2; tS1 = TM['pisah'] + 0.4
put(tS0 - 0.05, pop(260, 90, 0.12), 0.2); put(tS0 - 0.04, tick(0.03, 1800), 0.1); wh(tS0, 0.7, 200, 3000, 1.0, 0.4, 0.6)
put(tS0, wind(tS1 - tS0 + 0.5, 160, 700), 0.09)
for q in range(26):
    tq = tS0 + 0.05 + q * (tS1 - tS0) / 26 + rng.random() * 0.05
    put(tq, clink(2200 + rng.random() * 2200, 0.25, 0.7), CL * (0.35 + 0.3 * rng.random()))
put(TM['campur'] + 2.3, square_blips([1500, 900, 600], 0.05), 0.03)
# "nggak kebaca": card swings down, the numbers scramble (blips), blur
wh(TM['kebaca'] + 0.02, 0.6, 1200, 300, 1.0, 0.4, 0.35); put(TM['kebaca'] + 0.6, pop(300, 160, 0.1), 0.06)
for q in range(14): put(TM['kebaca'] + 1.3 + q * 0.11, square_blips([2200 - 90 * (q % 5) * 3], 0.03), 0.018)
wh(TM['pisah'] - 0.22, 0.4, 600, 2400, 1.2, 0.5, 0.3)
# S4 · chop: wind-up swish, the blade zing + impact, coins scatter, the jar halves slide, lanes whoosh in, sign flips
tB = TM['pisah'] + 0.4
wh(TM['pisah'] + 0.05, 0.3, 400, 1800, 1.4, 0.7, 0.3)
put(tB - 0.02, zing(0.6), 0.16); put(tB + 0.1, boom(0.6, 160, 60), 0.16); put(tB + 0.12, tick(0.03, 6000), 0.12)
for q in range(10): put(tB + 0.15 + q * 0.06 + rng.random() * 0.03, clink(2600 + rng.random() * 1800, 0.25, 0.8), CL * 0.45)
wh(tB + 0.1, 0.9, 200, 1600, 0.9, 0.5, 0.6)
for t0 in (TM['lane1'], TM['lane2']): put(t0 + 0.05, pop(450, 950, 0.1), P_); put(t0 + 0.32, tick(0.02, 2000), 0.06)
for k in range(3): put(TM['lane1'] + 0.1 + k * 0.16 + 0.35, pop(800 + 120 * k, 1300, 0.05), 0.05); put(TM['lane2'] + 0.1 + k * 0.16 + 0.35, pop(700 + 120 * k, 1200, 0.05), 0.05)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
wh(TM['sol'] + 0.6, 0.8, 300, 1400, 1.0, 0.5, 0.4)
for k in range(4): put(TM['sol'] + 1.45 + k * 0.3 + 0.48, pop(600 + 90 * k, 1200, 0.07), 0.1); put(TM['sol'] + 1.45 + k * 0.3, whoosh(0.4, 800, 2600, 1.6, 0.6), W * 0.15)
for g0 in (TM['sol'] + 2.6, TM['telusur'] + 1.6, TM['end'] + 4.4, TM['end'] + 7.0): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
put(TM['telusur'] + 0.35, marker(0.45), MK); put(TM['telusur'] + 0.8, marker(0.6), MK * 0.7)
put(TM['telusur'] + 1.25, pop(500, 1000, 0.1), P_); put(TM['telusur'] + 1.0, marker(0.5), MK * 0.6)
# beam + iris -> end card
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
