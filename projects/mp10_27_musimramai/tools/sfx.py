"""Synthesised SFX for MasterPajak AI Video 27 (Musim Ramai, Catatan Jangan Ikut Kacau) — sits under the VO (no samples, no music,
per the client's rule). Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again.
Deterministic. Sounds: rain bed + wind under the order storm, thunder + crack on "badai", card paper slaps, parcel drops (cardboard
knocks), pile sway, receipt flutter + slide, sticky-note slaps, stabilo markers, the storm lifting away + parcels shipping out
(whooshes), notebook page flip, "?" scribble, lamp click, softer outside rain + distant thunder, one scribble + rising ding per
written day, clock ticks + 5-minute chime, sign flip, band sweep, hologram fx, order-chip pops, nota-photo ticks, total chime +
shimmer, chat bubble pops, typing ticks, answer chime, row-flash ticks, beam/iris boom, end pops + chime.
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
rng = np.random.default_rng(27)
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

def rainbed(dur, f=2600.0, q=0.7):
    """steady rain: band noise with a slow swell + sparse drop ticks"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, f), q) * (0.8 + 0.2 * np.sin(2 * np.pi * 0.31 * t))
    e = np.minimum(1, t / 0.6) * np.minimum(1, (dur - t) / 0.8)
    x = x / (np.abs(x).max() + 1e-9) * e
    for k in range(int(dur * 9)):
        i = int(rng.random() * (n - 2000)); d = tick(0.012, 3000 + 3000 * rng.random()); x[i:i + len(d)] += d * 0.35
    return x

def thunder(dur=2.2):
    """crack + rolling rumble"""
    n = int(dur * SR); t = np.arange(n) / SR
    cr = svf_bp(rng.standard_normal(n), np.linspace(3200, 600, n), 0.9) * np.exp(-t * 9)
    rb = boom(dur, 70, 28)[:n] * (0.6 + 0.4 * np.abs(np.sin(2 * np.pi * 3.1 * t))) * np.exp(-t * 0.8)
    x = 0.7 * cr + rb
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

CUTB = TM['sol'] + 0.15
BT = [1.0, 1.75, 2.35, 2.85, TM['badai'] + 0.12, TM['paket'] + 0.05, TM['numpuk'] + 0.05, TM['numpuk'] + 0.45]   # parcel drops (index.html BT)
CLUT = [0.55, 1.35, 2.1, TM['badai'] + 0.25, TM['badai'] + 0.55, 4.25, TM['nota'] + 0.2, TM['catat'] + 0.1, TM['tunda'] + 0.25, TM['terus'] + 0.1]   # cards that land on the floor
DAYT = [TM['tiap'] - 0.05 + k * 0.24 for k in range(7)]

# S1-S2 · the order storm: rain bed + wind, card slaps, parcel knocks, thunder on "badai"
put(0.0, rainbed(TM['sepi'] + 0.3), 0.045)
wh(0.0, 3.2, 180, 700, 0.8, 0.4, 0.4); wh(2.9, 2.4, 160, 600, 0.8, 0.5, 0.3); wh(6.2, 2.8, 170, 650, 0.8, 0.5, 0.3)
for t in CLUT: put(t - 0.02, paper(0.22), 0.07)
for k, t in enumerate(BT): put(t - 0.12, whoosh(0.18, 900, 2200, 1.2, 0.6), W * 0.25); put(t + 0.16, knock(150 - 6 * k, 0.22), 0.15); put(t + 0.17, paper(0.2), 0.05)
put(TM['badai'] - 0.04, thunder(2.4), 0.24); put(TM['badai'] - 0.03, zap(0.3), 0.04)
put(TM['badai'] + 0.29, svf_bp(rng.standard_normal(int(0.35 * SR)), np.linspace(3000, 800, int(0.35 * SR)), 0.9) * np.exp(-np.arange(int(0.35 * SR)) / SR * 10), 0.05)
put(TM['paket'] + 1.18, thunder(1.6), 0.08)
# copy pops + stabilo
for t in (TM['hook'] - 0.2, TM['pes'] - 0.12, TM['badai'] - 0.12, TM['paket'] - 0.05, TM['nota'] - 0.1, TM['catat'] - 0.1): put(t + 0.1, pop(500, 950, 0.08), 0.07)
put(TM['badai'] + 0.15, marker(0.38), MK)
# pile sway (two low wood-ish knocks), the receipt flutters and slides under the box, ring pop
put(TM['numpuk'] + 0.62, knock(90, 0.3), 0.1); put(TM['numpuk'] + 0.95, knock(80, 0.3), 0.07)
put(TM['nota'] - 0.85, flutter(0.9), 0.07); put(TM['nota'] + 0.06, whoosh(0.3, 2400, 900, 1.0, 0.3), W * 0.35); put(TM['nota'] + 0.1, paper(0.25), 0.08)
put(TM['nyelip'], pop(800, 1400, 0.08), 0.1)
# sticky notes slap onto the notebook, stabilo on "ditunda"
for t in (TM['tunda'] - 0.05, TM['tunda'] + 0.33, TM['terus'] + 0.12): put(t + 0.18, paper(0.16), 0.13); put(t + 0.19, pop(300, 220, 0.06), 0.06)
put(TM['tunda'] + 0.25, marker(0.32), MK)

# S3 · "begitu sepi": the storm lifts away, the parcels ship out, the notebook opens, a "?" is drawn
wh(TM['sepi'] - 0.3, 0.8, 600, 2600, 1.0, 0.7, 0.55)
for k in range(5): wh(TM['sepiW'] - 0.1 + k * 0.08, 0.5, 400 + 80 * k, 1800, 1.1, 0.7, 0.3)
put(TM['sepi'] + 0.15, pop(450, 900, 0.08), 0.06)
put(TM['pikir'] + 0.3, flutter(0.45), 0.07); put(TM['pikir'] + 0.95, paper(0.25), 0.1)
put(TM['berapa'] - 0.1, marker(0.45), MK * 1.1); put(TM['berapa'] + 0.3, marker(0.35), MK)
put(TM['untung'] - 0.1, pop(520, 980, 0.08), 0.07)

# S4 · the habit: lamp click, the rain is back (outside, softer), one written row + day tick per day, the clock, the sign
put(TM['kunci'] + 0.13, tick(0.02, 2400), 0.16); put(TM['kunci'] + 0.15, pop(1200, 700, 0.05), 0.08)
put(TM['kunci'], rainbed(CUTB - TM['kunci'] + 0.2, 1500.0, 0.8), 0.025)
put(TM['kunci'] + 1.4, thunder(1.8), 0.05); put(TM['lima'] + 0.4, thunder(1.4), 0.04)
wh(TM['kunci'] + 0.3, 0.35, 900, 2400, 1.2, 0.5, 0.25)
for k, t in enumerate(DAYT):
    put(t, marker(0.16), MK * 0.55); put(t + 0.12, ding(1568 * (1.0595 ** (2 * k)), 0.4), 0.045)
put(TM['hari'] + 0.15, marker(0.36), MK)
for j in range(int((TM['toko'] + 0.4 - (TM['lima'] - 0.6)) / 0.5)): put(TM['lima'] - 0.6 + j * 0.5, tick(0.014, 3400 if j % 2 else 2800), 0.06)
put(TM['lima'] + 1.0, chime((1318.5, 1760, 2637), 1.1), 0.055); put(TM['menit'] - 0.05, pop(600, 1200, 0.08), 0.1)
put(TM['menit'] + 0.2, marker(0.36), MK)
put(TM['tutup'] - 0.12, whoosh(0.3, 1200, 2600, 1.4, 0.5), W * 0.3); put(TM['tutup'] + 0.04, knock(210, 0.15), 0.1)
put(TM['sebelum'] - 0.05, pop(520, 980, 0.08), 0.06)

# band sweep -> brand
for k in range(3): wh(CUTB - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(CUTB + 0.55)
wh(CUTB + 0.1, 0.8, 250, 2200, 1.0, 0.45, 0.55)
for g0 in (CUTB + 2.9, TM['q'] + 1.0, TM['dari'] + 0.4, TM['cta'] + 1.2, TM['bio'] + 0.9): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# order chips rain into the Penjualan column, nota photos into Modal & biaya
for k in range(7):
    t = TM['bantu'] - 0.2 + k * 0.17; put(t, whoosh(0.4, 2400, 900, 1.3, 0.5), W * 0.2); put(t + 0.4, pop(560 + 60 * k, 1100 + 90 * k, 0.07), 0.11)
for k in range(7):
    t = TM['foto'] - 0.25 + k * 0.13; put(t, whoosh(0.45, 500, 2400, 1.2, 0.5), W * 0.18); put(t + 0.48, tick(0.02, 3600), 0.08); put(t + 0.49, pop(700 + 50 * k, 1300, 0.06), 0.06)
put(TM['foto'] - 0.3, tick(0.018, 2600), 0.08)
for t in (TM['kejar'] - 0.1, TM['jadi'] - 0.05, TM['tanya'] - 0.08): put(t + 0.1, pop(520, 980, 0.08), 0.06)
put(TM['ramainya'] + 0.25, marker(0.42), MK); put(TM['rapi'] + 0.05, marker(0.42), MK)
put(TM['pemb'] + 0.1, chime((1318.5, 1760, 2637), 1.2), 0.06); put(TM['rapi'] + 0.05, shimmer(0.8), 0.03)
# chat: panel in, question bubble, typing dots, the answer, the source chip, rows flash
wh(TM['q'] - 0.05, 0.7, 300, 2200, 1.0, 0.5, 0.45); put(TM['q'] + 0.2, pop(700, 1300, 0.07), 0.11)
for j in range(4): put(TM['tanya'] + 0.1 + j * 0.16, tick(0.012, 2200 + 200 * j), 0.05)
put(TM['asis'] + 0.35, pop(500, 1000, 0.09), 0.12); put(TM['asis'] + 0.5, chime((1568, 2093, 2637), 1.2), 0.055)
put(TM['dari'] - 0.1, pop(900, 1500, 0.07), 0.08); put(TM['catmu'] + 0.1, ding(2093, 0.5), 0.06)
for k in range(7): put(TM['catmu'] - 0.05 + k * 0.07, tick(0.012, 3800 + 100 * k), 0.04)
put(TM['jawab'] - 0.1, marker(0.42), MK)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.0, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")

