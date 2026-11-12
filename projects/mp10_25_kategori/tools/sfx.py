"""Synthesised SFX for MasterPajak AI Video 25 (Kategori Biaya Biar Nggak Campur Aduk) — sits under the VO (no samples, no music,
per the client's rule). Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again.
Deterministic. Sounds: office air, receipts falling onto the heap (flutter + paper slaps), heap shuffle rustle, stabilo marker, text
pops, the total card rising (+ "?" ticks, wobble ticks), the card flying away, the crane whoosh, the filing cabinet dropping in
(fall whoosh + heavy metal thud), drawer slides on metal rails + clunks, label pops and tag pops, band sweep, hologram fx, the phone
swinging in, viewfinder bracket lock, scan beep, camera shutter, upload rise + done ding, result sheet + row pops, "Tercatat" chime,
photos flying into drawers (whoosh, drawer slide, paper drop, clunk), summary bar ticks, total pops, the "paling gede" drawer + chime,
beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py [project dir]"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
SB = TM['sol'] + 0.12; EA = TM['end'] + 0.26          # same offsets as index.html (brand switch / iris)
out = np.zeros(N)
rng = np.random.default_rng(25)
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
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

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

def rail(dur=0.22, f=900):
    """drawer on metal ball-bearing rails: rolling band noise with a fast ripple and a faint metallic ring"""
    n = int(dur * SR); t = np.arange(n) / SR
    rip = 0.6 + 0.4 * np.sin(2 * np.pi * (70 + 40 * t / dur) * t) ** 2
    x = svf_bp(rng.standard_normal(n), np.full(n, f) * (1 + 0.3 * t / dur), 1.6) * rip * env(n, 0.3)
    x += 0.12 * np.sin(2 * np.pi * 2900 * t) * env(n, 0.5)
    return x / np.abs(x).max()

def clunk(f=130, dur=0.28):
    """steel drawer closing: low body thump + bright metal knock + short ring"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 24) + 0.55 * np.sin(2 * np.pi * f * 2.3 * t) * np.exp(-t * 36)
    x += svf_bp(rng.standard_normal(n), np.full(n, 2400.0), 3.0) * np.exp(-t * 60) * 0.5
    x += 0.18 * (np.sin(2 * np.pi * 1730 * t) + 0.6 * np.sin(2 * np.pi * 2610 * t)) * np.exp(-t * 18)
    return x / np.abs(x).max()

def thud(dur=0.6):
    """heavy cabinet landing on the floor"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(90 * (45 / 90) ** (t / dur)) / SR) * np.exp(-t * 9)
    x += svf_bp(rng.standard_normal(n), np.full(n, 420.0), 0.8) * np.exp(-t * 28) * 0.8
    x += 0.2 * (np.sin(2 * np.pi * 1210 * t) + 0.5 * np.sin(2 * np.pi * 1890 * t)) * np.exp(-t * 10)
    x = np.tanh(1.5 * x); return x / np.abs(x).max()

def shutter(dur=0.16):
    """camera shutter: two crisp mechanical clicks"""
    n = int(dur * SR); x = np.zeros(n)
    for d, f, g in ((0.0, 3800, 1.0), (0.055, 2600, 0.8)):
        k = int(d * SR); m = n - k; t = np.arange(m) / SR
        x[k:] += svf_bp(rng.standard_normal(m), np.full(m, float(f)), 2.2) * np.exp(-t * 170) * g
        x[k:] += np.sin(2 * np.pi * 420 * t) * np.exp(-t * 90) * 0.4 * g
    return x / np.abs(x).max()

def beep(f0=1500, f1=2300, dur=0.22):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 + (f1 - f0) * t / dur) / SR) * env(n, 0.2, 1.0)
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
def drawer(t_out, d_out, hold, d_in, g=1.0, f=900):
    put(t_out, rail(d_out + 0.05, f), 0.10 * g); put(t_out + d_out - 0.02, clunk(170, 0.16), 0.05 * g)
    put(t_out + d_out + hold, rail(d_in * 0.7, f * 0.85), 0.08 * g); put(t_out + d_out + hold + d_in * 0.55, clunk(125, 0.28), 0.16 * g)

CK = [TM['c1'], TM['c2'], TM['c3'], TM['c4'], TM['c5']]
# S1 · hook: office air under a slow push-in; three receipts fall onto the heap; heap shuffle; text pops + stabilo
wh(0.0, 2.8, 180, 800, 0.9, 0.5, 0.3)
for t0 in (0.15, 0.5, 0.9):
    put(t0, flutter(0.62), 0.07); wh(t0 + 0.05, 0.6, 1800, 500, 1.1, 0.4, 0.3); put(t0 + 0.68, paper(0.3), 0.15)
put(TM['hook'] - 0.1, pop(480, 900, 0.08), 0.06)
put(TM['campur'] + 0.02, flutter(0.55), 0.10); put(TM['campur'] + 0.08, paper(0.25), 0.07)
put(TM['campur'] - 0.1, pop(520, 980, 0.08), 0.08); put(TM['aduk'] + 0.12, marker(0.42), MK); put(TM['kayak'] - 0.06, pop(560, 1040, 0.08), 0.08)
# S2 · camera rise, the total card rises out of the heap, "?" ticks, the amount accent, biggest segment lifts, "?" wobble, marker
wh(TM['ujung'] - 0.1, 1.1, 260, 1400, 1.0, 0.5, 0.45)
wh(TM['ujung'] + 0.05, 0.7, 400, 2200, 1.1, 0.55, 0.5); put(TM['ujung'] + 0.6, pop(420, 820, 0.1), 0.1)
for k in range(5): put(TM['kamu'] + 0.15 + k * 0.08, tick(0.02, 3000 + 250 * k), 0.07)
put(TM['uang'], ding(1568, 0.4), 0.04); put(TM['paling'], pop(380, 760, 0.1), 0.12)
for j in range(5): put(TM['habis'] + j * 0.2, tick(0.016, 3600 + 300 * (j % 2)), 0.05)
put(TM['apa'] + 0.1, marker(0.38), MK)
for t in (TM['ujung'], TM['kamu'], TM['uang'], TM['paling'], TM['habis']): put(t - 0.06, pop(500, 950, 0.07), 0.05)
# S3 · the card flies away, crane, the cabinet drops in, labels: drawer slides + clunks, label pops, tag pops
wh(TM['biar'], 0.55, 2000, 500, 1.1, 0.3, 0.45); wh(TM['biar'] - 0.05, 1.35, 250, 1200, 0.9, 0.5, 0.4)
wh(TM['biar'] + 0.3, 0.45, 600, 180, 0.8, 0.85, 0.55); put(TM['biar'] + 0.72, thud(0.7), 0.3)
put(TM['pisah'] - 0.08, pop(500, 950, 0.08), 0.07); put(TM['kat'] + 0.36, marker(0.4), MK)
for k, t in enumerate(CK):
    put(t - 0.05, pop(620 + 60 * k, 1250 + 80 * k, 0.08), 0.12); put(t - 0.02, ding(1760 * (1.0595 ** (2 * k)), 0.4), 0.035)
    drawer(t - 0.04, 0.2, 0.18, 0.32, 1.0, 800 + 60 * k)
    for j in range(3): put(t + 0.12 + j * 0.07, pop(900, 1600, 0.05), 0.05)
# band sweep -> brand
for k in range(3): wh(SB - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# S4 · brand: hologram, phone swings in, the first receipt in the viewfinder, bracket lock, scan beep, shutter, upload, sheet rows
holo_fx(SB + 0.55)
wh(SB + 0.08, 0.7, 2200, 500, 1.0, 0.35, 0.45)
put(SB + 0.05, pop(480, 900, 0.08), 0.06); put(TM['foto'] - 0.08, pop(560, 1040, 0.08), 0.08); put(TM['nota'] + 0.35, marker(0.45), MK)
put(TM['unggah'] - 0.1, paper(0.25), 0.08); wh(TM['unggah'] - 0.1, 0.4, 900, 2400, 1.2, 0.4, 0.2)
for j in range(2): put(TM['foto'] + j * 0.06, tick(0.018, 3400 + 400 * j), 0.08)
put(TM['foto'] + 0.05, beep(1400, 2200, 0.4), 0.035)
put(TM['nota'] - 0.03, shutter(0.16), 0.22); put(TM['nota'], shimmer(0.35), 0.03)
put(TM['apl'] - 0.1, beep(700, 1500, 0.75), 0.025); put(TM['apl'] + 0.68, ding(2093, 0.45), 0.05)
wh(TM['tgl'] - 0.2, 0.42, 500, 2000, 1.1, 0.5, 0.3)
for t in (TM['tgl'], TM['kat2'], TM['nom']): put(t, pop(700, 1350, 0.07), 0.1); put(t + 0.02, tick(0.02, 3800), 0.05)
for i, t in enumerate((TM['tgl'], TM['kat2'], TM['nom'], TM['catat'])): put(t - 0.06, pop(520 + 40 * i, 980, 0.06), 0.04)
put(TM['catat'] - 0.04, pop(600, 1300, 0.09), 0.12); put(TM['catat'], chime((1568, 2093, 2637), 1.0), 0.05)
wh(TM['masuk'] + 0.1, 0.32, 1800, 500, 1.1, 0.3, 0.25); put(TM['masuk'] - 0.06, pop(560, 1040, 0.08), 0.07); put(TM['laci'] + 0.3, marker(0.42), MK)
# photos fly into their drawers (same times as index.html)
FT = [TM['masuk'] + 0.02, TM['msg'] - 0.42, TM['msg'] - 0.16, TM['msg'] + 0.1, TM['msg'] + 0.36]
for i, t in enumerate(FT):
    dur = 0.55 if i == 0 else 0.46
    if i: put(t - 0.06, shutter(0.12), 0.12); put(t - 0.22, paper(0.18), 0.04)
    wh(t, dur + 0.1, 500, 2600, 1.3, 0.5, 0.35)
    drawer(t + dur - 0.3, 0.22, 0.16, 0.26, 0.8, 900 + 40 * i)
    put(t + dur - 0.02, paper(0.2), 0.1)
# "jadi kelihatan, biaya mana yang paling gede"
put(TM['jadi'] - 0.05, pop(500, 1000, 0.09), 0.1)
for k in range(5): put(TM['lihat'] + k * 0.08, tick(0.018, 2600 + 300 * k), 0.07); put(TM['lihat'] + 0.1 + k * 0.1, pop(700 + 60 * k, 1400 + 90 * k, 0.06), 0.07)
for k in range(5): put(TM['biaya'] + k * 0.1, tick(0.014, 4200), 0.05)
drawer(TM['plg'] - 0.04, 0.26, 3.0, 0.3, 1.0, 760)
put(TM['plg'] + 0.08, marker(0.28), MK * 0.8); put(TM['gede'] - 0.04, chime((1318.5, 1760, 2637), 1.2), 0.07); put(TM['gede'] + 0.12, marker(0.36), MK)
put(TM['jadi'] - 0.04, pop(480, 900, 0.07), 0.05); put(TM['plg'] - 0.2, pop(560, 1040, 0.08), 0.07)
for g0 in (SB + 2.9, TM['catat'] + 0.4, TM['lihat'] + 0.6, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# beam + iris -> end
put(EA - 0.5, pop(500, 1000, 0.1), 0.12); wh(EA - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(EA - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(EA + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['bio'] + 1.2, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
