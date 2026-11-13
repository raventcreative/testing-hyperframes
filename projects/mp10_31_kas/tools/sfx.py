"""Synthesised SFX for MasterPajak AI Video 31 (Untung Tapi Uang Kok Nggak Ada?) — sits under the VO (no samples, no music, per the client's rule).
Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again. Deterministic.
Sounds: room air, card swing + UNTUNG stamp, camera whooshes, the steel cash-box lid clank, dust, moth flutter, the laba chip
flying up and splashing into the LABA tank, tank fills (rising resonance + bubbles), valve squeaks, water running in the glass
pipes, amount-chip pops + dings, racing clock ticks, padlock click, a box dropping into the basket, the tap and three or four
drips (plink), number-card pops + the not-equal stamp, band sweep, hologram fx, pembukuan rows + tags, beam/iris, end pops + chime.
Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py [project dir]"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(31)
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


def boing(f0=520, f1=980, dur=0.22):
    """cartoon question-mark pop: a short upward glide with a wobble"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (f1 / f0) ** (t / dur) * (1 + 0.06 * np.sin(2 * np.pi * 22 * t))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 11)
    return x / np.abs(x).max()

def drip(dur=0.18):
    """sweat drop: a falling water blip"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(1500 * (500 / 1500) ** (t / dur)) / SR) * np.exp(-t * 20)
    return x / np.abs(x).max()

def nope(dur=0.34):
    """soft two-tone 'nope' for the ✕ badge (low, rounded, not harsh)"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = np.where(t < dur / 2, 392.0, 311.0)
    x = (np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.3 * np.sin(2 * np.pi * np.cumsum(2 * f) / SR)) * env(n, 0.08, 1.0)
    return x / np.abs(x).max()

def tap(f=900, dur=0.07):
    """glass tablet tap"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 70) + 0.4 * svf_bp(rng.standard_normal(n), np.full(n, 3500.0), 2.0) * np.exp(-t * 120)
    return x / np.abs(x).max()

def room(dur):
    """quiet meeting-room air: low band noise, very soft"""
    n = int(dur * SR)
    x = svf_bp(rng.standard_normal(n), np.full(n, 260.0), 0.7)
    x *= np.minimum(1, np.arange(n) / (0.4 * SR)) * np.minimum(1, (n - np.arange(n)) / (0.5 * SR))
    return x / (np.abs(x).max() + 1e-9)



# ---------------- water / plumbing sounds (all synthesised) ----------------
def bubble(f=520, dur=0.06):
    """a single bubble 'bloop': fast upward chirp with a quick decay"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f * (1 + 0.9 * t / dur)) / SR) * np.exp(-t * 55)
    return x / np.abs(x).max()

def flow(dur=1.2, fc=900):
    """water running in a glass pipe: soft band noise with a slow wobble plus scattered bubbles"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), fc * (1 + 0.15 * np.sin(2 * np.pi * 3.1 * t)), 0.8) * (0.7 + 0.3 * np.sin(2 * np.pi * 7.3 * t + 1))
    x = x / (np.abs(x).max() + 1e-9) * 0.6
    for k in range(int(dur * 14)):
        i = int(rng.random() * (n - 4000)); b = bubble(380 + 700 * rng.random(), 0.05 + 0.04 * rng.random()); x[i:i + len(b)] += b * (0.25 + 0.3 * rng.random())
    x *= np.minimum(1, t / 0.12) * np.minimum(1, (dur - t) / 0.25)
    return x / (np.abs(x).max() + 1e-9)

def fill(dur=1.0, f0=420, f1=1150):
    """a tank filling: the resonance rises as the water level goes up"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), f0 * (f1 / f0) ** (t / dur), 3.0)
    x = x / (np.abs(x).max() + 1e-9) * 0.7
    for k in range(int(dur * 18)):
        i = int(rng.random() * (n - 4000)); b = bubble(300 + 500 * rng.random() + 400 * i / n, 0.06); x[i:i + len(b)] += b * 0.3
    x *= np.minimum(1, t / 0.08) * np.minimum(1, (dur - t) / 0.2)
    return x / (np.abs(x).max() + 1e-9)

def splash(dur=0.6):
    """the laba drop hitting the tank: bright noise burst + low body + bubbles"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(3200, 1200, n), 0.6) * np.exp(-t * 9)
    x += np.sin(2 * np.pi * 90 * t) * np.exp(-t * 18) * 0.8
    for k in range(12):
        i = int((0.03 + 0.4 * rng.random()) * SR); b = bubble(420 + 600 * rng.random(), 0.06); x[i:i + len(b)] += b * 0.35
    return x / np.abs(x).max()

def plip(dur=0.14):
    """one drop into a shallow puddle: the classic rising 'plink'"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(900 * (2400 / 900) ** np.minimum(1, t / 0.03)) / SR) * np.exp(-t * 32)
    x += svf_bp(rng.standard_normal(n), np.full(n, 3000.0), 1.5) * np.exp(-t * 90) * 0.3
    return x / np.abs(x).max()

def squeak(dur=0.26, f0=1050, f1=1450):
    """valve wheel squeak: a thin gliding tone with a rough vibrato"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = (f0 + (f1 - f0) * t / dur) * (1 + 0.025 * np.sin(2 * np.pi * 38 * t))
    x = (np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.3 * np.sin(4 * np.pi * np.cumsum(f) / SR)) * env(n, 0.2, 1.0)
    return x / np.abs(x).max()

def clank(dur=0.45):
    """the steel cash-box lid: inharmonic metal partials + a knock"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t * d) for f, a, d in ((523, 1.0, 9), (1187, 0.6, 12), (2213, 0.35, 16), (3170, 0.2, 22)))
    x += svf_bp(rng.standard_normal(n), np.full(n, 900.0), 1.0) * np.exp(-t * 60) * 0.8
    return x / np.abs(x).max()

def click2():
    """padlock snapping shut: two close ticks + a small metal ring"""
    a = tick(0.02, 3200); b = tick(0.02, 2400); n = int(0.3 * SR); x = np.zeros(n); x[: len(a)] += a; i = int(0.045 * SR); x[i:i + len(b)] += b * 0.9
    t = np.arange(n) / SR; x += np.sin(2 * np.pi * 2600 * t) * np.exp(-t * 30) * 0.25
    return x / np.abs(x).max()

S1T, S2T, S3T = TM['s1'] + 0.12, TM['s2'] + 0.15, TM['s3'] + 0.15
# S1 · hook: room air, the card swings in, stamp, camera tilts down, the lid clanks open, dust, the moth flutters out
put(0.0, room(TM['bay'] + 0.6), 0.05)
wh(0.0, 0.55, 2200, 500, 1.1, 0.25, 0.4)
put(TM['hook'] - 0.1, pop(520, 980, 0.08), 0.07)
put(TM['untung'] + 0.04, knock(110, 0.24), 0.2); put(TM['untung'] + 0.06, pop(700, 1300, 0.08), 0.12); put(TM['untung'] + 0.3, marker(0.38), MK)
wh(TM['tapi'] - 0.04, 0.6, 300, 1400, 1.0, 0.5, 0.45)
put(TM['uang'] + 0.06, squeak(0.18, 700, 900), 0.03); put(TM['uang'] + 0.3, clank(0.5), 0.13)
wh(TM['uang'] + 0.32, 0.8, 1500, 400, 0.7, 0.2, 0.25)
put(TM['nggak'] + 0.05, flutter(1.4), 0.05); put(TM['nggak'] + 0.3, marker(0.38), MK)
# S2 · the card falls away, the laba chip flies up, drops into the tank: splash + fill
wh(TM['bay'] + 0.04, 1.0, 250, 2600, 1.0, 0.55, 0.9)
put(TM['bay'] + 0.9, pop(400, 900, 0.09), 0.08)
put(TM['bay'] + 1.0, bubble(700, 0.08), 0.12)
put(TM['bay'] + 1.16, splash(0.7), 0.24)
put(TM['bay'] + 1.2, fill(0.9, 300, 900), 0.12)
put(TM['air'] + 0.12, marker(0.32), MK)
wh(TM['s1'] - 0.37, 0.8, 1800, 400, 0.9, 0.4, 0.4)
# S3-S5 · valves squeak open, water runs through the pipe, each tank fills, the amount chip pops
for (t0, kw, chip, dur) in ((S1T, 'laku', TM['laku'] + 0.08, TM['s2'] - 0.12 - S1T), (S2T, 'cair', TM['cair'] + 0.12, TM['s3'] - 0.12 - S2T), (S3T, 'lagi', TM['lagi'] + 0.1, TM['yang'] - 0.1 - S3T)):
    put(t0, squeak(0.3), 0.05)
    put(t0 + 0.15, flow(dur - 0.1, 850), 0.06)
    put(t0 + 0.6, fill(TM[kw] - t0 - 0.3, 420, 1150), 0.08)
    put(chip, pop(600, 1200, 0.09), 0.12); put(chip + 0.04, ding(2093, 0.5), 0.05)
    put(TM[kw] + 0.12, marker(0.32), MK * 0.9)
    put(t0 + dur - 0.1, squeak(0.22, 1300, 1000), 0.035)
for t in (TM['s2'], TM['s3'], TM['yang']): wh(t, 0.7, 300, 1300, 1.0, 0.5, 0.35)
# S4 · the clock races, the padlock snaps shut
tt = TM['dana']
while tt < TM['cair'] + 0.5: put(tt, tick(0.018, 3600), 0.05); tt += 0.11
put(TM['blm2'] + 0.18, click2(), 0.14); put(TM['blm2'] + 0.22, knock(160, 0.18), 0.08)
# S5 · the new box drops into the basket
put(TM['stok2'] + 0.2, paper(0.25), 0.12); put(TM['stok2'] + 0.22, knock(130, 0.2), 0.1)
# S6 · the rest runs down, the tap turns, a few drips: plip plip plip
put(TM["yang"] + 0.1, flow(TM["u2"] + 0.3 - TM["yang"], 700), 0.035)
put(TM['kas'], squeak(0.24, 900, 1250), 0.05)
DRT = [TM['kas'] + 0.22, TM['kas'] + 0.56, TM['kas'] + 0.92, TM['sedikit'] + 0.42]
for t in DRT: put(t, drip(0.12), 0.03); put(t + 0.44, plip(0.16), 0.16)
put(TM['sedikit'] + 0.06, pop(500, 760, 0.1), 0.1); put(TM['sedikit'] + 0.3, marker(0.34), MK)
# S7 · camera pulls back, two number cards, the "not equal" sign stamps
wh(TM['u2'], 0.85, 1600, 350, 0.9, 0.4, 0.45)
put(TM['u2'] + 0.05, pop(480, 960, 0.09), 0.12); put(TM['uang2'] - 0.07, pop(560, 1100, 0.09), 0.12)
put(TM['itu2'] + 0.02, knock(120, 0.24), 0.18); put(TM['itu2'] + 0.04, boing(380, 760, 0.2), 0.06)
# band sweep -> brand
tB = TM['sol'] - 0.8
for k in range(3): wh(tB - 0.02 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S8 · brand: hologram, card swings up, trunk + row ticks, nyangkut tags, underline
holo_fx(TM['sol'] - 0.25)
wh(TM['sol'] - 0.32, 0.8, 250, 2400, 1.0, 0.45, 0.55)
wh(TM['mp'] - 0.1, 0.6, 700, 2600, 1.4, 0.5, 0.2)
for k in range(4): put(TM['rapi'] + k * 0.15, tick(0.02, 3000 + 250 * k), 0.08); put(TM['rapi'] + k * 0.15 + 0.15, fill(0.35, 600, 1100), 0.025)
for k in range(3): put(TM['nyangkut'] + 0.02 + k * 0.13, pop(600 + 80 * k, 1200 + 120 * k, 0.08), 0.12)
put(TM['nyangkut'] + 0.42, pop(700, 1400, 0.08), 0.12); put(TM['nyangkut'] + 0.46, ding(2349, 0.5), 0.05)
put(TM['nyangkut'] + 0.12, marker(0.48), MK)
for g0 in (TM['ai'] + 0.5, TM['nyangkut'] + 0.7, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
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
print("sfx.wav", round(len(x16) / SR, 2), "s", "rms dB", round(20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9), 1))
