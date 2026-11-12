"""Synthesised SFX for MasterPajak AI Video 17 (Bukti Transfer Nyelip di Galeri) — sits under the VO (no samples, no music, per the
client's rule). Beat times are parsed from window.TM in index.html (real VO word times), so a re-time only needs
`python3 tools/sfx.py` again. Deterministic.
Sounds: thumb flicks on glass (swipe + decelerating scroll ticks), "found" ding, tile lift pops + label chips, stabilo marker,
receipt-ring dings, meme boings, rekap card whoosh + row ticks + a soft "missed" double blip, gallery grey-out, six photo lifts and
fly-aways, band sweep, hologram fx, upload drops + check pops + done chime, album whoosh + photo flutter + date-pill ticks,
pembukuan rows, trace callout pop, lens glide + found ding, split whooshes + badge pops, beam/iris boom, end pops + chime.
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
rng = np.random.default_rng(17)
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

def flutter(dur=0.5):
    """paper / photo flutter: AM-chopped band noise"""
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.55 + 0.45 * np.sign(np.sin(2 * np.pi * (16 + 8 * t / dur) * t))
    x = svf_bp(rng.standard_normal(n), 2400 + 700 * np.sin(2 * np.pi * 5 * t), 1.3) * am * env(n, 0.25)
    return x / np.abs(x).max()

def boing(f0=330, dur=0.35):
    """cartoon wobble for the memes: a sine with a decaying vibrato"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (1 + 0.18 * np.sin(2 * np.pi * 14 * t) * np.exp(-t * 6))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 8)
    return x / np.abs(x).max()

def swipe(dur=0.32):
    """a fingertip dragging on glass: short bright noise with a soft attack"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(3200, 5200, n), 1.4) * env(n, 0.3)
    return x / (np.abs(x).max() + 1e-9)

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)
def flick_fx(t0, d, g=1.0):
    """thumb flick: glass swipe + a whoosh + scroll ticks that slow down as the list decelerates"""
    put(t0, swipe(0.24), 0.07 * g); wh(t0, min(0.7, d), 500, 3000, 1.3, 0.25, 0.45 * g)
    tt, gap = t0 + 0.03, 0.022
    while tt < t0 + d * 0.9:
        put(tt, tick(0.012, 3000 + 600 * rng.random()), 0.035 * g); tt += gap; gap *= 1.16

# S1 · hook: flicks, a found transfer (ding), it slips away, frantic flicks; selfie + food lift out with label chips
flick_fx(0.0, 0.95)
put(TM['tf'] + 0.2, ding(2349, 0.5), 0.07); put(TM['tf'] + 0.2, pop(700, 1300, 0.07), 0.08)
put(TM['tf'] + 0.35, marker(0.4), MK)
flick_fx(TM['nyelip'], 0.5, 1.1); flick_fx(TM['nyelip'] + 0.58, 0.38, 0.8); flick_fx(TM['nyelip'] + 1.02, 0.55, 0.9)
put(TM['hook'] - 0.1, pop(500, 900, 0.08), 0.07); put(TM['nyelip'], pop(560, 1000, 0.08), 0.07)
for t0 in (TM['selfie'], TM['makan']):
    put(t0, pop(420, 900, 0.1), 0.12); wh(t0, 0.35, 900, 2600, 1.4, 0.3, 0.25); put(t0 + 0.14, pop(900, 1500, 0.06), 0.08)
# camera pulls back, the robot hops in
wh(TM['makan'] + 0.6, 0.9, 1800, 400, 0.9, 0.5, 0.35); put(TM['makan'] + 1.2, pop(300, 600, 0.12), 0.08)
# S2 · scroll atas / scroll bawah; receipts flash; memes boing
flick_fx(TM['scroll'], 0.95, 1.1); flick_fx(TM['bawah'], 0.55, 1.1); flick_fx(TM['bawah'] + 0.62, 0.42, 0.8)
for k, dt in enumerate((0.1, 0.28, 0.46)): put(TM['nota'] + dt, ding(1760 * (1.0595 ** (3 * k)), 0.4), 0.05)
put(TM['numpuk'] + 0.3, marker(0.38), MK)
for k in range(3): put(TM['meme'] + 0.02 + k * 0.05, boing(300 + 70 * k, 0.32), 0.05)
# S3 · rekap: card whoosh, row ticks, "kelewat" soft double blip + "?" pop
wh(TM['rekap'] - 0.02, 0.7, 2400, 500, 1.0, 0.35, 0.5)
for k in range(3): put(TM['rekap'] + 0.55 + k * 0.32, tick(0.02, 2600), 0.08)
for k in range(2): put(TM['rekap'] + 0.6 + k * 0.32, pop(800, 1500, 0.06), 0.07)
put(TM['lewat'] + 0.05, square_blips([660, 440], 0.09), 0.035); put(TM['lewat'], pop(500, 950, 0.09), 0.1)
put(TM['lewat'] + 0.35, marker(0.36), MK)
# S4 · grey-out, six photos lift (rising pops), "nginep" marker, they fly up and away
wh(TM['mulai'] - 0.05, 0.6, 2200, 600, 1.0, 0.4, 0.35)
wh(TM['nota2'] - 0.1, 0.6, 400, 1200, 0.8, 0.5, 0.25)
for i in range(6): put(TM['nota2'] + 0.05 + i * 0.09, pop(500 + 70 * i, 1000 + 120 * i, 0.08), 0.09)
put(TM['nginep'] + 0.3, marker(0.38), MK)
for i in range(6): put(TM['galeri2'] + 0.05 + i * 0.05, whoosh(0.5, 600, 3400, 1.3, 0.6), W * 0.25)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S5 · brand: phone swings in, hologram, six photos drop into the upload slots, checks, done chime
wh(TM['sol'] + 0.02, 0.7, 2000, 400, 1.0, 0.4, 0.45)
holo_fx(TM['sol'] + 0.55)
for i in range(6):
    t = TM['sol'] + 0.85 + i * 0.16
    put(t, whoosh(0.6, 3000, 700, 1.4, 0.7), W * 0.22); put(t + 0.6, pop(380 + 40 * i, 760 + 60 * i, 0.08), 0.1)
for i in range(6): put(TM['app'] + 0.25 + i * 0.12, pop(900 + 60 * i, 1600 + 80 * i, 0.06), 0.07)
put(TM['mpai'] + 0.4, chime((1318.5, 1760, 2637), 1.2), 0.06)
# album: phone steps back, the album swings in, photos flutter into their date rows, date pills tick
wh(TM['susun'], 0.75, 1600, 400, 1.0, 0.4, 0.35); wh(TM['susun'] + 0.05, 0.8, 300, 2200, 1.0, 0.45, 0.5)
put(TM['susun'] + 0.45, flutter(0.8), 0.06)
for i in range(6): put(TM['susun'] + 1.0 + i * 0.1, tick(0.018, 3400), 0.06)
for d in range(3): put(TM['tgl'] - 0.05 + d * 0.2, ding(1568 * (1.0595 ** (4 * d)), 0.35), 0.05)
put(TM['tgl'] + 0.1, marker(0.42), MK)
# S6 · pembukuan: album leaves, the card lifts in, rows fill, the trace callout, the lens finds the missed transfer
wh(TM['led'] - 0.05, 0.8, 1800, 300, 0.9, 0.5, 0.35); wh(TM['led'] + 0.05, 0.9, 250, 2400, 1.0, 0.45, 0.55)
for k in range(6): put(TM['led'] + 0.47 + k * 0.11, tick(0.016, 3600 + 150 * k), 0.07)
put(TM['telusur'] + 0.05, pop(600, 1200, 0.07), 0.09); put(TM['telusur'] + 0.15, pop(450, 950, 0.1), 0.1); wh(TM['telusur'] + 0.15, 0.35, 900, 2600, 1.4, 0.3, 0.2)
put(TM['telusur'] + 0.55, marker(0.42), MK)
put(TM['cari'] + 0.2, pop(700, 1200, 0.07), 0.07); wh(TM['cari'] + 0.35, 0.65, 700, 1800, 1.6, 0.5, 0.2)
put(TM['dicari'] + 0.05, ding(2093, 0.6), 0.08); put(TM['dicari'] + 0.1, pop(800, 1500, 0.07), 0.09)
for g0 in (TM['mpai'] + 0.6, TM['telusur'] + 0.4, TM['notab'] + 0.4, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# S7 · split: the card steps right, the calm gallery slides in, two badges
wh(TM['kenang'] - 0.05, 0.8, 1600, 400, 1.0, 0.4, 0.35); wh(TM['kenang'], 0.8, 300, 2000, 1.0, 0.45, 0.45)
put(TM['kenang'] + 0.6, pop(520, 1040, 0.09), 0.11); put(TM['kenang'] + 0.62, ding(2637, 0.4), 0.04)
put(TM['notab'] + 0.55, pop(620, 1240, 0.09), 0.11); put(TM['notab'] + 0.57, ding(2349, 0.4), 0.04)
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
