"""Synthesised SFX for MasterPajak AI Video 29 (Hari Pertama Pakai MasterPajak AI) — sits under the VO (no samples, no music, per
the client's rule). Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again.
Deterministic. Sounds: dawn air + little bird chirps (pagi), the TUTUP/BUKA sign flip, four time-lapses (soft swell + the wall
clock ratcheting) with HUD stop pops/dings, the card flying out of the phone, a camera shutter, upload ticks, field pops and a
"Tersimpan" ding, order notification blips + parcels landing, rows snapping into the table, the "Rapi" stamp chime, report rows
and bars, the LABA ding, the lamp click, night crickets, message send / typing / reply blips, band sweep, hologram fx, the
pembukuan rows and the trace-line shimmer, beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s).
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
rng = np.random.default_rng(14)
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

def bird(f0=3200, dur=0.16, up=True):
    """tiny morning bird chirp: a fast FM sweep with a warble"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (1 + (0.45 if up else -0.3) * np.sin(np.pi * t / dur)) + 260 * np.sin(2 * np.pi * 38 * t)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / dur) ** 1.5
    return x / np.abs(x).max()

def shutter():
    """camera shutter: two short mechanical clicks with a noisy body"""
    a = svf_bp(rng.standard_normal(int(0.03 * SR)), np.full(int(0.03 * SR), 3000.0), 1.4) * np.exp(-np.arange(int(0.03 * SR)) / SR * 160)
    b = svf_bp(rng.standard_normal(int(0.05 * SR)), np.full(int(0.05 * SR), 1900.0), 1.1) * np.exp(-np.arange(int(0.05 * SR)) / SR * 90)
    x = np.zeros(int(0.12 * SR)); x[: len(a)] += a; i = int(0.055 * SR); x[i: i + len(b)] += b
    return x / np.abs(x).max()

def notif(f1=1318.5, f2=1975.5):
    """friendly two-note notification blip"""
    n = int(0.09 * SR); t = np.arange(n) / SR
    a = np.sin(2 * np.pi * f1 * t) * np.exp(-t * 30); b = np.sin(2 * np.pi * f2 * t) * np.exp(-t * 22)
    x = np.concatenate([a, b * 0.9]); return x / np.abs(x).max()

def crickets(dur=4.0):
    """night crickets: pulsed narrow tones in chirp groups, very soft"""
    n = int(dur * SR); t = np.arange(n) / SR
    car = np.sin(2 * np.pi * 4300 * t) + 0.5 * np.sin(2 * np.pi * 4720 * t + 1.3)
    puls = (np.sin(2 * np.pi * 28 * t) > 0.2).astype(float)
    grp = (np.sin(2 * np.pi * 1.6 * t + 0.7) > 0.35).astype(float)
    e = np.minimum(1, t / 0.6) * np.minimum(1, (dur - t) / 0.5)
    x = car * puls * grp * e; return x / (np.abs(x).max() + 1e-9)

def timelapse(t0, d=0.95, g=1.0):
    """time-lapse: a soft swell + the wall clock ratcheting fast"""
    wh(t0, d, 250, 1400, 0.9, 0.55, 0.38 * g)
    tt = t0 + 0.04
    for j in range(16): put(tt, tick(0.012, 3400 + 200 * (j % 2)), 0.05 * g); tt += 0.055

PH = [TM['pagi'], TM['siang'], TM['sore'], TM['malam']]
TL0 = [p - 0.3 for p in PH]
# S1 · hook (dawn): air, birds waking, the HUD drops in, the shop sign flips TUTUP -> BUKA, stabilo
wh(0.0, 3.4, 180, 700, 0.9, 0.5, 0.3)
for t, f, up in ((0.7, 3300, True), (0.95, 3600, True), (1.9, 3100, False), (2.15, 3500, True), (3.4, 3800, True)): put(t, bird(f, 0.15, up), 0.045)
put(TM['hook'] - 0.1, pop(500, 900, 0.08), 0.07); put(TM['mpai'] - 0.15, pop(560, 1000, 0.08), 0.08)
for k in range(5): put(0.9 + k * 0.08, tick(0.016, 3000 + 250 * k), 0.05)
put(TM['ngap'] - 0.2, knock(320, 0.12), 0.1); put(TM['ngap'] - 0.05, pop(700, 1300, 0.07), 0.11)
put(TM['ngap'] + 0.55, marker(0.4), MK)
# time-lapses (dawn -> pagi, pagi -> siang, siang -> sore, sore -> malam) + HUD stop pops
timelapse(TM['pagi'] - 0.75, 1.2)
for k in (1, 2, 3): timelapse(TL0[k])
for k, t in enumerate(PH):
    put(t, pop(600 + 80 * k, 1150 + 80 * k, 0.08), 0.1)
    if k: put(t + 0.05, ding(2093 * (1.0595 ** (2 * k)), 0.45), 0.05)
for t in (4.3, 4.65, 5.9): put(t, bird(3400, 0.14, True), 0.035)
# pagi: the card flies out of the phone, shutter + flash, upload scan, three fields, Tersimpan
wh(TM['pagi'] - 0.12, 0.7, 2600, 500, 1.1, 0.25, 0.6); put(TM['pagi'] + 0.6, pop(420, 840, 0.09), 0.1)
put(TM['foto'] - 0.02, shutter(), 0.22); put(TM['foto'], shimmer(0.3), 0.03)
put(TM['blj'] + 0.1, marker(0.36), MK)
tt = TM['ungg'] - 0.05
for j in range(8): put(tt, tick(0.014, 2600 + 220 * j), 0.05); tt += 0.075
for k, dt in enumerate((-0.02, 0.14, 0.3)): put(TM['apl'] + dt, pop(620 + 120 * k, 1250 + 160 * k, 0.07), 0.11)
put(TM['apl'] + 0.45, ding(2349, 0.55), 0.07)
# siang: flip, orders pop in (notification blips) + parcels drop, rows line up, Rapi stamp
wh(PH[1] - 0.2, 0.5, 600, 2600, 1.2, 0.5, 0.4)
for k in range(4): put(TM['pes'] - 0.06 + k * 0.19, notif(1318.5 * (1.0595 ** k), 1975.5 * (1.0595 ** k)), 0.07)
for k in range(3): put(TM['pes'] + 0.05 + k * 0.2 + 0.36, knock(150 + 30 * k, 0.2), 0.12)
for k in range(4): put(TM['cat'] + 0.06 + k * 0.13, whoosh(0.3, 1400, 500, 1.2, 0.4), W * 0.25); put(TM['cat'] + 0.42 + k * 0.13, tick(0.016, 3600), 0.08)
put(TM['rapi'] - 0.1, paper(0.25), 0.1); put(TM['rapi'] + 0.1, pop(700, 1400, 0.08), 0.13); put(TM['rapi'] + 0.16, chime((1568, 2093, 2637), 1.0), 0.05)
put(TM['rapi'] + 0.1, marker(0.36), MK)
# sore: flip, report rows + bars, LABA pops
wh(PH[2] - 0.2, 0.5, 600, 2600, 1.2, 0.5, 0.4)
put(TM['lap'] + 0.3, marker(0.36), MK)
for t in (TM['pj'] - 0.04, TM['by'] - 0.06, TM['by'] + 0.2): put(t, pop(520, 1040, 0.08), 0.1); put(t + 0.12, whoosh(0.5, 400, 1800, 1.3, 0.3), W * 0.25)
put(TM['laba'] - 0.06, pop(600, 1300, 0.1), 0.14); put(TM['laba'], ding(2637, 0.6), 0.07); put(TM['laba'] + 0.25, marker(0.32), MK)
# malam: flip, the lamp clicks on, crickets, the question is sent, typing, the answer arrives
wh(PH[3] - 0.2, 0.5, 600, 2600, 1.2, 0.5, 0.4)
put(TM['malam'] + 0.32, knock(900, 0.06), 0.12); put(TM['malam'] + 0.35, tick(0.02, 2400), 0.1)
put(TM['malam'] + 0.2, crickets(TM['sol'] - TM['malam'] - 0.6), 0.018)
put(TM['masih'] + 0.05, whoosh(0.25, 800, 3200, 1.4, 0.3), W * 0.3); put(TM['masih'] + 0.22, notif(1568, 2093), 0.06)
for j in range(9): put(TM['tanya'] + j * 0.12, tick(0.01, 1800 + 300 * (j % 3)), 0.04)
put(TM['jwb'] - 0.05, notif(1175, 1760), 0.07)
put(TM['asis'] + 0.35, marker(0.4), MK); put(TM['data'] - 0.02, marker(0.34), MK)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
# brand: the pembukuan card swings up, four day rows pop, the trace line draws through the four icons, underlines
wh(TM['sol'] + 0.15, 0.8, 250, 2200, 1.0, 0.45, 0.5)
holo_fx(TM['sol'] + 0.55)
for k, t in enumerate((TM['fn'] - 0.05, TM['fn'] + 0.42, TM['lr'] - 0.05, TM['lr'] + 0.5)): put(t, pop(520 + 90 * k, 1050 + 120 * k, 0.08), 0.12)
put(TM['nyb'] - 0.1, shimmer(0.8), 0.04)
for k in range(4): put(TM['nyb'] - 0.1 + k * 0.24, ding(1568 * (1.0595 ** (2 * k)), 0.35), 0.045)
put(TM['lr'] + 0.55, marker(0.45), MK); put(TM['mpai2'] + 0.3, marker(0.45), MK)
for g0 in (TM['lr'] + 0.3, TM['nyb'] + 0.7, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
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
