"""Synthesised SFX for MasterPajak AI Video 24 (Laporan Laba Rugi dalam 30 Detik) — sits under the VO (no samples, no music).
Beat times are parsed from window.TM in index.html, so a VO re-time only needs `python3 tools/sfx.py` again. Deterministic.
Sounds: kitchen room tone, title pops, kitchen-timer wind (ratchet) + soft ticking while the recipe runs, "Yuk, masak!" pan sizzle,
HUD drop, stabilo marker, recipe rows (pencil scribble + pop), whip pan, jar whoosh + coin cascade into the bowl, scale odometer
ticks, portions lifting out of the bowl (whoosh up) and clinking into the cups + tick pops, cup hops (wood knocks), LCD flash
chimes, the kitchen-timer DING + sparkle shimmer on the result, band sweep, hologram fx, card fly-in + flip swish, report row
pops, ghost-card slides, beam/iris boom, end pops + chime. Writes assets/audio/sfx.wav (48 kHz mono, TM.total s).
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
rng = np.random.default_rng(24)
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

def clink(f=3100, dur=0.22):
    """a coin landing on coins: inharmonic metallic partials with a fast decay + a tiny noise transient"""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for r, a, d in ((1.0, 1.0, 22), (1.53, 0.6, 30), (2.37, 0.45, 38), (3.11, 0.3, 50)):
        x += a * np.sin(2 * np.pi * f * r * t + rng.random() * 6) * np.exp(-t * d)
    x += svf_bp(rng.standard_normal(n), np.full(n, 6000.0), 1.5) * np.exp(-t * 300) * 0.6
    return x / np.abs(x).max()

def cascade(dur=0.7, rate=34):
    """coins pouring into a bowl: many clinks with a swell and a falling density"""
    n = int(dur * SR); x = np.zeros(n + SR // 3)
    for k in range(int(rate * dur)):
        u = rng.random() ** 0.8; i = int(u * n)
        c = clink(2400 + 1600 * rng.random(), 0.18) * (0.4 + 0.6 * rng.random())
        x[i:i + len(c)] += c
    return x / np.abs(x).max()

def ratchet(dur=0.6, rate=26):
    """kitchen timer being wound: a fast run of dry clicks"""
    n = int(dur * SR); x = np.zeros(n + 2000)
    for k in range(int(rate * dur)):
        i = int(k / rate * SR); c = tick(0.012, 2600 + 200 * (k % 2)); x[i:i + len(c)] += c * (0.7 + 0.3 * (k % 2))
    return x / np.abs(x).max()

def bell(f=1760, dur=1.6):
    """kitchen-timer bell: a bright struck bell, fast hammer repeats then a long ring"""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for h in range(4):
        d = int(h * 0.075 * SR); tt = t[: n - d]
        y = np.sin(2 * np.pi * f * tt) * np.exp(-tt * (3.5 if h == 3 else 14)) + 0.5 * np.sin(2 * np.pi * f * 2.42 * tt) * np.exp(-tt * (6 if h == 3 else 20)) + 0.25 * np.sin(2 * np.pi * f * 3.9 * tt) * np.exp(-tt * 12)
        x[d:] += y * (0.75 if h < 3 else 1.0)
    return x / np.abs(x).max()

def sizzle(dur=0.6):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, 5200.0), 0.7) * (0.6 + 0.4 * np.abs(np.sin(2 * np.pi * 23 * t + rng.random() * 6))) * env(n, 0.12, 1.5)
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)
def odo(t0, d, n=12, g=0.055):
    tt = t0
    for j in range(n): put(tt, tick(0.012, 3600 + 140 * (j % 3)), g); tt += d / n * (0.75 + 0.5 * j / n)

# S1 · hook: kitchen room tone, title pops, the timer winds on "tiga puluh detik", "Yuk, masak!" pop + sizzle
wh(0.0, 3.4, 200, 800, 0.9, 0.5, 0.3)
put(TM['hook'] - 0.12, pop(500, 900, 0.08), 0.07); put(TM['lap'] - 0.05, pop(540, 960, 0.08), 0.06)
put(TM['dtk'] + 0.05, pop(620, 1200, 0.08), 0.09); put(TM['dtk'] + 0.3, ratchet(0.62, 28), 0.06); put(TM['dtk'] + 0.95, ding(2637, 0.25), 0.03)
put(TM['dtk'] + 0.5, marker(0.4), MK)
put(TM['yuk'] - 0.08, pop(450, 1100, 0.1), 0.12); put(TM['yuk'] + 0.05, sizzle(0.75), 0.035)
put(TM['masak'], knock(260, 0.12), 0.05)
# S2 · HUD drops, pill pops, marker on "tiga", recipe rows (scribble + pop), sub-rows ticks; the kitchen timer ticks softly
wh(TM['bahan'] - 0.25, 1.0, 300, 1700, 1.0, 0.5, 0.45)
put(TM['bahan'] + 0.05, pop(600, 1000, 0.08), 0.07); put(TM['bahan'] + 0.27, pop(700, 1250, 0.07), 0.07)
put(TM['bahan'] + 0.75, marker(0.36), MK)
for t in (TM['pj'] - 0.05, TM['mb'] - 0.05, TM['by'] - 0.08):
    put(t, marker(0.22), 0.05); put(t + 0.02, pop(560, 1100, 0.07), 0.09)
for k in range(3): put(TM['by'] + 0.2 + k * 0.12, tick(0.02, 3300 + 300 * k), 0.06)
t = TM['bahan'] + 0.4
while t < TM['has'] - 0.1: put(t, tick(0.02, 2900 if int((t - TM['bahan']) * 2) % 2 else 2300), 0.022); t += 0.5
# S3 · whip pan, jar flies in + pours (coin cascade), scale odometer, portion out -> cup (clink, tick pop), "laba kotor" flash
wh(TM['l1'] - 0.2, 0.42, 2600, 400, 1.0, 0.35, 0.65); wh(TM['l1'] + 0.08, 0.5, 400, 3000, 1.2, 0.5, 0.8)
put(TM['l1'] + 0.05, pop(600, 1100, 0.08), 0.07); put(TM['l1'] + 0.15, pop(700, 1250, 0.07), 0.06)
tJ = TM['pj2'] - 0.62
wh(tJ, 0.55, 300, 1500, 1.0, 0.5, 0.45); wh(tJ + 0.48, 0.35, 900, 2200, 1.2, 0.5, 0.3)
put(tJ + 0.8, cascade(0.75, 34), 0.11); put(tJ + 0.95, knock(130, 0.2), 0.08)
odo(tJ + 0.95, 0.85, 14)
put(tJ + 1.8, ding(1760, 0.4), 0.035)
wh(tJ + 1.45, 0.55, 1500, 300, 1.0, 0.4, 0.35)
def portion(t0, cupf=2900):
    wh(t0, 0.4, 500, 2400, 1.2, 0.45, 0.35); put(t0 + 0.02, pop(500, 1000, 0.08), 0.07)
    wh(t0 + 0.38, 0.6, 1800, 700, 1.0, 0.5, 0.3)
    put(t0 + 0.92, clink(cupf, 0.25), 0.08); put(t0 + 0.95, clink(cupf * 1.3, 0.2), 0.05); put(t0 + 1.0, pop(800, 1500, 0.07), 0.08)
portion(TM['krg'] + 0.05, 2800)
odo(TM['mb2'] - 0.1, 0.7, 10)
put(TM['lk'] - 0.05, chime((1568, 2093), 0.8), 0.04); put(TM['lk'] + 0.4, marker(0.4), MK)
# S4 · cups hop "satu-satu", three portions out (ongkir, iklan, kemasan), odometer down, caption chips pop
put(TM['krg2'] - 0.15, pop(500, 900, 0.07), 0.05)
put(TM['satu'] + 0.45, marker(0.35), MK)
for k in range(3): put(TM['satu'] + 0.05 + k * 0.24, knock(240 + 30 * k, 0.12), 0.07)
for k, key in enumerate(('ong', 'ikl', 'kem')):
    put(TM[key] - 0.1, pop(600 + 80 * k, 1150 + 120 * k, 0.08), 0.1)
    portion(TM[key] - 0.12, 3000 + 300 * k)
    odo(TM[key] - 0.02, 0.5, 7, 0.045)
# S5 · the kitchen timer DINGs, the scale reads LABA (flash chime), sparkles, marker on "laba." and "sebenarnya"
put(TM['has'] - 0.02, bell(1760, 1.7), 0.075)
wh(TM['has'] - 0.1, 0.9, 250, 1600, 1.0, 0.5, 0.4)
put(TM['laba'] - 0.05, chime((1318.5, 1760, 2637), 1.2), 0.06); put(TM['laba'] + 0.05, shimmer(0.9), 0.03)
for j in range(7): put(TM['laba'] + 0.05 + j * 0.05, pop(1500 + 150 * (j % 4), 2600, 0.04), 0.03)
put(TM['laba'] + 0.3, marker(0.36), MK)
put(TM['sbn'] + 0.45, marker(0.45), MK)
# band sweep -> brand: hologram, the card flies in and flips, rows pop, underline, rows glow, last months' reports slide out
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
wh(TM['sol'] + 0.1, 0.85, 250, 1900, 1.0, 0.45, 0.5)
tF = TM['lr'] - 0.35
wh(tF, 0.6, 600, 3200, 1.4, 0.5, 0.45); put(tF + 0.3, pop(400, 900, 0.1), 0.08)
for k in range(7): put(tF + 0.55 + k * 0.11, pop(520 + 60 * k, 1050 + 90 * k, 0.07), 0.08)
put(TM['lr'] + 0.6, marker(0.45), MK)
for g0 in (TM['lr'] + 0.3, TM['bia'] + 0.6, TM['cta'] + 1.2, TM['bio'] + 1.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
put(TM['cat'] + 0.45, tick(0.02, 3400), 0.06)
for k in range(4): put(TM['bia'] + 0.05 + k * 0.1, tick(0.02, 3000 + 250 * k), 0.05)
for k in range(2): wh(TM['bln'] - 0.1 + k * 0.1, 0.4, 600, 1800, 1.2, 0.4, 0.3)
put(TM['bln'] + 0.45, marker(0.4), MK)
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
