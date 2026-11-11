"""Synthesised SFX for MasterPajak AI Video 7 (Kalkulator Gratis 3 Langkah). No samples, no music (client rule); sits under the VO.
Camera dolly air, stabilo marker, band sweep, phone fly-in + soft landing, hologram build, numeral fly-bys with a low thud per step,
UI taps (typing ticks, chips, keypad clicks, button presses), loading shimmer, result chime + count-up ticks, card lifts,
beam + iris boom, end-card pops. Deterministic. All times come from window.TM in index.html.
Writes assets/audio/sfx.wav (48 kHz mono). Run: python3 tools/sfx.py ."""
import sys, re, wave
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(7)
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

def flyby(dur=0.7, f0=500, fpk=3200, f1=260, q=1.4):
    """air rushing past the lens: pitch rises to the closest point, then drops (doppler-ish)"""
    n = int(dur * SR); u = np.linspace(0, 1, n)
    f = np.where(u < 0.38, f0 * (fpk / f0) ** (u / 0.38), fpk * (f1 / fpk) ** ((u - 0.38) / 0.62))
    x = svf_bp(rng.standard_normal(n), f, q) * env(n, 0.38, 1.6)
    return x / (np.abs(x).max() + 1e-9)

def boom(dur=1.4, f0=95, f1=38):
    n = int(dur * SR); t = np.arange(n) / SR
    ph = 2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR
    x = np.sin(ph) * np.exp(-t * 3.2)
    nb = svf_bp(rng.standard_normal(n), np.full(n, 180.0), 0.8) * np.exp(-t * 9) * 0.6
    x = np.tanh(1.8 * (x + nb))
    return x / np.abs(x).max()

def thud(dur=0.35, f0=120, f1=55):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 14)
    x += svf_bp(rng.standard_normal(n), np.full(n, 900.0), 1.0) * np.exp(-t * 60) * 0.25
    return x / np.abs(x).max()

def pop(f0=900, f1=320, dur=0.09):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 38)
    return x / np.abs(x).max()

def tick(dur=0.025, f=4200):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.full(n, f), 2.0) * np.exp(-t * 260)
    return x / (np.abs(x).max() + 1e-9)

def tap():
    """glass tap: short click + tiny low body"""
    a = tick(0.02, 5200); b = pop(420, 180, 0.06) * 0.5
    x = np.zeros(int(0.07 * SR)); x[:len(a)] += a; x[:len(b)] += b
    return x / np.abs(x).max()

def key():
    """soft keypad key: plastic-y mid click"""
    a = tick(0.018, 2600) * 0.8; b = pop(700, 300, 0.05) * 0.6
    x = np.zeros(int(0.06 * SR)); x[:len(a)] += a; x[:len(b)] += b
    return x / np.abs(x).max()

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

def shimmer(dur=1.1):
    """loading: soft rising noise with a slow tremolo"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(900, 3400, n), 2.2) * (0.6 + 0.4 * np.sin(2 * np.pi * 9 * t)) * env(n, 0.5, 1.2)
    return x / np.abs(x).max()

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# S0 · hook: slow camera dolly air, card arrival, stabilo, the "?" bloop, robot peek
wh(0.0, 2.4, 180, 900, 0.9, 0.5, 0.28)
wh(0.05, 0.8, 300, 1500, 1.0, 0.25, 0.35)
put(TM['hook'] + 0.45, tick(0.02, 3000), 0.06); put(TM['hook'] + 1.2, tick(0.02, 2800), 0.06)
put(TM['hook'] + 0.95, marker(0.5), MK)
put(TM['hook'] + 1.45, pop(500, 1100, 0.12), 0.13)
put(TM['hook'] + 0.85, pop(300, 600, 0.12), 0.08)
# band sweep (+ the whip dolly) -> navy world
for k in range(3): wh(TM['brand'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
wh(TM['brand'] + 0.12, 0.5, 2200, 500, 1.1, 0.3, 0.35)
# S1 · brand: phone flies in from depth and lands; hologram; list ticks; GRATIS badge; "Mulai hitung"
put(TM['brand'] + 0.05, flyby(1.0, 260, 2400, 300, 1.3), W * 0.8)
put(TM['brand'] + 0.95, thud(0.3, 140, 70), 0.10)
holo_fx(TM['brand'] + 0.55)
for k in range(3): put(TM['brand'] + 0.75 + k * 0.13, tick(0.02, 3600 + 300 * k), 0.05)
put(TM['brand'] + 1.45, pop(700, 1500, 0.1), 0.12)
put(TM['brand'] + 2.9, square_blips([1800, 900, 1500], 0.02), 0.02)
put(TM['s1'] - 0.62, tap(), 0.16)
# steps: numeral fly-by + landing thud + screen push swish
for s in ('s1', 's2', 's3'):
    t0 = TM[s] - 0.5
    put(t0, flyby(0.75, 600, 3600, 220, 1.5), W * 0.9)
    put(t0 + 0.62, boom(0.6, 110, 46), 0.13)
    wh(t0 + 0.05, 0.5, 1800, 600, 1.4, 0.3, 0.3)
# step 1 · isi data usaha
put(TM['s1'] + 0.55, tick(0.02, 3000), 0.06)
for k in range(9): put(TM['s1'] + 0.7 + k * 0.075, tick(0.016, 3800 + 300 * ((k * 5) % 3)), 0.07)
put(TM['s1'] + 1.52, tap(), 0.09); put(TM['s1'] + 1.75, pop(600, 1100, 0.08), 0.1)
put(TM['s1'] + 2.2, pop(650, 1200, 0.08), 0.11); put(TM['s1'] + 2.55, pop(720, 1300, 0.08), 0.11)
put(TM['s1'] + 3.55, tap(), 0.16)
# step 2 · masukkan omzet: lift, eight keys, settle, "Hitung estimasi"
wh(TM['s2'] + 0.6, 0.45, 400, 2000, 1.2, 0.3, 0.3)
for k in range(8): put(TM['s2'] + 0.85 + k * 0.19, key(), 0.12)
put(TM['s2'] + 2.75, thud(0.25, 160, 90), 0.07)
put(TM['s2'] + 3.4, tap(), 0.16)
# step 3 · loading, result chime, count-up ticks, label pop, lift-off
put(TM['s3'] - 0.4, shimmer(1.2), 0.05)
put(TM['s3'] + 0.85, chime((1046, 1318.5, 1568), 1.2), 0.07)
for k in range(1, 11): put(TM['s3'] + 0.95 + (1 - (1 - k / 10) ** 1.6) * 0.85, tick(0.014, 4600), 0.045)
put(TM['s3'] + 1.85, pop(800, 1400, 0.08), 0.1)
for k in range(4): put(TM['s3'] + 2.0 + k * 0.12, tick(0.016, 3400), 0.04)
wh(TM['s3'] + 2.6, 0.5, 350, 2200, 1.2, 0.3, 0.35)
# S2 · result: camera pull-back, stabilo on "estimasi", consult card swings in, avatars, bubble
wh(TM['res'] - 0.55, 1.0, 1600, 300, 1.0, 0.45, 0.5)
put(TM['res'] + 0.75, marker(0.45), MK)
wh(TM['kon'] - 0.2, 0.7, 300, 1900, 1.1, 0.4, 0.45)
for k in range(3): put(TM['kon'] + 0.25 + k * 0.1, pop(600 + 120 * k, 1100 + 150 * k, 0.07), 0.09)
put(TM['kon'] + 0.7, pop(900, 1600, 0.08), 0.1)
# beam + iris -> end
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
# S5 · end card
holo_fx(TM['end'] + 0.55)
put(TM['end'] + 0.8, pop(500, 1000, 0.12), P_)
put(TM['end'] + 1.15, pop(800, 1400, 0.08), 0.11); put(TM['end'] + 1.45, pop(900, 1600, 0.08), 0.11)
put(TM['bio'], pop(900, 1500, 0.08), 0.1); put(TM['bio'] + 0.3, marker(0.4), MK * 0.8)
for g0 in (TM['end'] + 3.9, TM['end'] + 5.8): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
put(TM['end'] + 5.2, chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
