"""Synthesised SFX for MasterPajak AI Video 9 (POV Tutup Bulan) — sits under the VO (no samples, no music, per the client's rule).
Deterministic. Calendar page flicks + a felt-tip circle on "30", whip pans, an accelerating stream of soft notification pings,
toast whooshes, window pops, receipt rustle, the month-end tunnel fly-by, a deflating "sigh" tone, brand bands, hologram fx,
dashboard docking pops + progress sweep, beam/iris and the end-card pops/chime. All beat times are read from window.TM in
index.html (same keys as the film). Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run: python3 tools/sfx.py ."""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(9)
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

def rip(dur=0.55):
    n = int(dur * SR)
    jit = np.repeat(rng.random(n // 240 + 1), 240)[:n] ** 3
    x = svf_bp(rng.standard_normal(n), np.linspace(1400, 3600, n), 1.4) * jit * env(n, 0.2)
    return x / np.abs(x).max()

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy 40-70 Hz texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def flick(dur=0.16):
    """calendar page flick: a short bright paper snap that brightens as the page whips over"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(1500, 5200, n), 1.3) * (np.minimum(1, t / 0.05) ** 2) * np.exp(-np.maximum(0, t - 0.1) * 60)
    return x / (np.abs(x).max() + 1e-9)

def ping(f=1760, dur=0.32):
    """soft generic notification ping (two partials, no recognisable app sound)"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 14) + 0.5 * np.sin(2 * np.pi * f * 1.5 * t) * np.exp(-t * 20)
    x *= np.minimum(1, t / 0.004)
    return x / np.abs(x).max()

def sigh(dur=0.8):
    """deflating 'capek' tone: a breathy glide down"""
    n = int(dur * SR); t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(420 * (170 / 420) ** (t / dur)) / SR
    x = np.sin(ph) * 0.7 + svf_bp(rng.standard_normal(n), np.linspace(900, 300, n), 0.9) * 0.5
    x *= env(n, 0.12, 1.4)
    return x / np.abs(x).max()

def sweep(dur=0.95, f0=520, f1=1180):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * env(n, 0.5, 1.2)
    return x / np.abs(x).max()

W = 0.22
P_ = 0.15
MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# S1 · calendar: three page flicks, "30" lands, felt-tip circle + stabilo
for k, dt in enumerate((0.25, 0.58, 0.86)): put(TM['pov'] + dt + 0.12, flick(0.17), 0.12 + 0.02 * k)
put(TM['pov'] + 1.16, pop(260, 110, 0.1), 0.12)
put(TM['pov'] + 1.3, marker(0.5), MK); put(TM['pov'] + 1.6, marker(0.35), MK * 0.9)
# whip pan to the phone
wh(TM['notif'] - 0.34, 0.5, 300, 2800, 1.1, 0.7, 0.9)
# notification pings: an accelerating stream (same gaps as the film)
GAP = [0.34, 0.3, 0.26, 0.22, 0.19, 0.17, 0.15, 0.13, 0.12, 0.11, 0.1]
ARR = [TM['notif'] + 0.05]
for g in GAP: ARR.append(ARR[-1] + g)
for i, t0 in enumerate(ARR): put(t0, ping(1760 * (1 + 0.012 * ((i * 7) % 5 - 2)), 0.3), 0.075 - 0.002 * i)
for i in (2, 6, 10): put(ARR[i] + 0.01, pop(700, 1400, 0.08), 0.1)
# toasts spilling out of the phone, the last one into the lens -> white
for k in range(7): wh(TM['notif'] + 0.85 + k * 0.13, 0.32, 500 + 90 * k, 2600, 1.3, 0.5, 0.32)
wh(TM['w1'] - 0.52, 0.55, 200, 3400, 1.0, 0.9, 0.7); put(TM['w1'] - 0.02, boom(0.5, 160, 70), 0.07)
# S3 · windows: land, whip, land, whip, land, pull back, whip down
put(TM['w1'] + 0.05, pop(420, 900, 0.1), P_); put(TM['w1'] + 0.75, marker(0.4), MK)
wh(TM['w2'] - 0.32, 0.46, 280, 2600, 1.1, 0.65, 0.85); put(TM['w2'] + 0.08, pop(460, 960, 0.1), P_); put(TM['w2'] + 0.7, tick(0.02, 3800), 0.08)
wh(TM['w3'] - 0.32, 0.46, 320, 2400, 1.1, 0.65, 0.85); put(TM['w3'] + 0.08, pop(500, 1000, 0.1), P_); put(TM['w3'] + 0.75, marker(0.4), MK)
wh(TM['w3'] + 1.0, 0.7, 1800, 400, 1.0, 0.5, 0.45)
wh(TM['nota'] - 0.36, 0.42, 300, 2200, 1.1, 0.7, 0.9)
# S4 · wallet: receipts rustle out, one flies up; the host pops up
put(TM['nota'] + 0.75, rip(0.55), 0.09); wh(TM['nota'] + 1.0, 0.45, 600, 3000, 1.4, 0.4, 0.4)
put(TM['nota'] + 0.6, square_blips([620, 930], 0.05), 0.025)
# S5 · whip, the month-end pages fly past the lens, the sigh, the shrug
wh(TM['capek'] - 0.32, 0.46, 300, 2600, 1.1, 0.7, 0.85)
dA, dB = TM['capek'] - 0.05, TM['sih'] + 0.4
def ease_io(p): return 2 * p * p if p < 0.5 else 1 - (-2 * p + 2) ** 2 / 2
for k in (0, 1):
    for t in np.arange(dA, dB, 0.005):
        if -150 + 1980 * ease_io((t - dA) / (dB - dA)) - (-900 * k) >= 900: wh(t - 0.25, 0.5, 250, 1500, 0.9, 0.6, 0.55); break
put(TM['sih'] + 0.1, sigh(0.8), 0.07); put(TM['sih'] + 0.5, marker(0.4), MK)
put(TM['sih'] + 0.55, square_blips([700, 520], 0.06), 0.02)
# band sweep -> MasterPajak AI
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
# S6 · dashboard lands, the scraps dock row by row, status pills, progress sweep + check
wh(TM['satu'] - 0.55, 0.8, 1600, 300, 1.0, 0.2, 0.55)
for k in range(4):
    t0 = TM['satu'] + 0.1 + k * 0.32
    wh(t0, 0.5, 400 + 100 * k, 2400, 1.2, 0.5, 0.4); put(t0 + 0.5, pop(500 + 60 * k, 1050, 0.09), P_ * 0.9); put(t0 + 0.72, tick(0.02, 4400), 0.09)
put(TM['tenang'] + 0.15, sweep(0.95), 0.035); put(TM['tenang'] + 1.05, pop(800, 1600, 0.08), 0.12)
put(TM['tenang'] + 1.1, chime((1568, 2093), 1.0), 0.04); put(TM['tenang'] + 0.95, marker(0.45), MK * 0.8)
for g0 in (TM['sol'] + 3.2, TM['sol'] + 5.7, TM['end'] + 4.4, TM['end'] + 7.0): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
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
