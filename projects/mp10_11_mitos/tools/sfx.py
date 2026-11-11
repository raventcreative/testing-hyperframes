"""Synthesised SFX for MasterPajak AI Video 11 (Mitos vs Fakta Pembukuan): card fan + deal, rubber-stamp slams, tower rise,
typed numbers, pile crash, 3D card flips, monthly steps, brand deck, hologram, beam/iris, CTA (no samples, no music, per the
client's rule; it sits under the VO). Every beat is read from window.TM in index.html. Deterministic.
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
def thump(dur=0.28):
    """rubber stamp on paper: a short low knock + a paper slap"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(150 * (60 / 150) ** (t / dur)) / SR) * np.exp(-t * 22)
    x += svf_bp(rng.standard_normal(n), np.full(n, 1400.0), 0.9) * np.exp(-t * 55) * 0.7
    return x / np.abs(x).max()
def boing(dur=0.42, f0=260, f1=520):
    """cartoon question-mark wobble: a vibrato glide"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = f0 * (f1 / f0) ** (t / dur) * (1 + 0.06 * np.sin(2 * np.pi * 18 * t))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.08, 1.2)
    return x / np.abs(x).max()
def rumble(dur=0.7):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(260, 70, n), 0.7) * env(n, 0.1, 1.0)
    return x / np.abs(x).max()
MT, FT = [TM['m1'], TM['m2'], TM['m3']], [TM['f1'], TM['f2'], TM['f3']]

# HOOK · the stacked cards fan out (3 flicks), stabilo on "pembukuan"
for k in range(3): put(TM['hook'] + 0.14 + k * 0.1, flick(0.15), 0.1 + 0.015 * k)
put(TM['hook'] + 1.0, marker(0.42), MK)
# the camera swings in while the cards are dealt out to their stations
wh(TM['m1'] - 0.55, 0.8, 250, 2400, 1.0, 0.6, 0.8)
for k in range(3): put(TM['m1'] - 0.5 + k * 0.05 + 0.3, flick(0.14), 0.08)
put(TM['m1'] - 0.2, pop(500, 1000, 0.09), 0.09)                    # top bar drops in
# MITOS stamps (land at m + 0.58)
for m in MT: wh(m + 0.36, 0.24, 2400, 600, 1.2, 0.8, 0.35); put(m + 0.58, thump(0.3), 0.32)
# whips between the cards
for m in MT[1:]: wh(m - 0.34, 0.46, 300, 2600, 1.1, 0.7, 0.9)
# flips: lift whoosh + flick at the turn + landing knock (card 2 spins 1.5 turns)
for i, (f, d) in enumerate(zip(FT, (0.8, 1.0, 0.8))):
    t0 = f - 0.36
    wh(t0, d + 0.1, 300, 2200, 1.0, 0.5, 0.75)
    for j in range(3 if i == 1 else 1): put(t0 + 0.2 + j * 0.26, flick(0.16), 0.11)
    put(t0 + d + 0.04, pop(220, 90, 0.14), 0.16); put(t0 + d + 0.05, tick(0.02, 2400), 0.08)
    put(f - 0.05, pop(800, 1500, 0.07), 0.07)                          # top bar MITOS -> FAKTA
# card 1 · tower rises, sign drops, tiny shop pops, "?" wobbles | the shop's profit card, bars, check, stabilo
put(TM['m1'] + 1.0, sweep(0.75, 180, 520), 0.07); put(TM['m1'] + 1.0, rumble(0.7), 0.06)
put(TM['m1'] + 1.85, pop(420, 900, 0.1), P_ * 0.9)
put(TM['m1'] + 2.2, pop(1200, 1900, 0.06), 0.1); put(TM['m1'] + 2.5, boing(0.42, 300, 600), 0.06)
put(TM['f1'] + 0.62, pop(500, 1000, 0.1), P_)
for k in range(4): put(TM['f1'] + 0.95 + k * 0.08, tick(0.02, 3000 + 400 * k), 0.07)
put(TM['f1'] + 1.4, pop(900, 1700, 0.08), 0.12); put(TM['f1'] + 1.45, chime((1568, 2093), 0.9), 0.03)
put(TM['f1'] + 1.95, marker(0.45), MK)
# card 2 · omzet typed in, empty biaya boxes blink, LABA "?" | biaya typed in, laba appears, stabilo x2
for k in range(4):
    for j in range(9): put(TM['m2'] + 0.85 + k * 0.18 + j * 0.035, tick(0.012, 4600 + 300 * (j % 3)), 0.045)
put(TM['m2'] + 1.75, square_blips([660, 440], 0.07), 0.025)
put(TM['m2'] + 2.2, boing(0.45, 240, 520), 0.07)
for k in range(4):
    for j in range(8): put(TM['f2'] + 0.75 + k * 0.16 + j * 0.037, tick(0.012, 4800 + 300 * (j % 3)), 0.045)
put(TM['f2'] + 0.95, marker(0.45), MK)
for j in range(11): put(TM['f2'] + 1.75 + j * 0.036, tick(0.012, 5000), 0.05)
put(TM['f2'] + 2.3, marker(0.42), MK); put(TM['f2'] + 2.4, chime((1318.5, 1760), 0.9), 0.03)
# card 3 · 12 folders drop onto the pile, it wobbles and crashes | 12 steps rise, checks climb, stabilo
for k in range(12): put(TM['m3'] + 0.62 + k * 0.075 + 0.19, pop(300 + 18 * k, 140, 0.08), 0.07)
put(TM['m3'] + 1.5, square_blips([300, 260], 0.08), 0.02)
put(TM['m3'] + 1.86, rumble(0.8), 0.12); put(TM['m3'] + 2.33, boom(0.6, 120, 50), 0.12)
for k in range(8): put(TM['m3'] + 1.95 + k * 0.05 + rng.random() * 0.03, flick(0.1), 0.05)
for k in range(12):
    put(TM['f3'] + 0.5 + k * 0.1, pop(400 + 60 * k, 700 + 70 * k, 0.07), 0.07)
    put(TM['f3'] + 0.68 + k * 0.1, tick(0.015, 3800 + 120 * k), 0.035)
put(TM['f3'] + 1.85, marker(0.45), MK); put(TM['f3'] + 1.95, chime((1046, 1318.5, 1568), 1.1), 0.035)
# band sweep -> MasterPajak AI
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
# the three FAKTA cards fly in and stack, square up, the top card flips into the report, rows land, stabilo on Laba
for k, dt in enumerate((0.18, 0.4, 0.62)): wh(TM['sol'] + dt, 0.6, 250 + 80 * k, 2200, 1.1, 0.5, 0.5); put(TM['sol'] + dt + 0.55, flick(0.12), 0.09)
put(TM['sol'] + 1.42, tick(0.02, 3200), 0.08); put(TM['sol'] + 1.5, tick(0.02, 3600), 0.06)
wh(TM['sol'] + 1.8, 0.85, 300, 2400, 1.0, 0.5, 0.6); put(TM['sol'] + 2.12, flick(0.16), 0.1); put(TM['sol'] + 2.6, pop(240, 100, 0.12), 0.14)
for k in range(3): put(TM['sol'] + 2.62 + k * 0.16, pop(520 + 60 * k, 1050, 0.08), P_ * 0.8)
put(TM['sol'] + 3.35, tick(0.02, 3000), 0.06)
for k in range(3): put(TM['sol'] + 3.5 + k * 0.15, pop(600 + 70 * k, 1200, 0.08), P_ * 0.8)
put(TM['sol'] + 4.3, marker(0.45), MK); put(TM['sol'] + 4.4, chime((1568, 2093), 1.0), 0.04)
for g0 in (TM['sol'] + 2.9, TM['sol'] + 4.6, TM['end'] + 4.4, TM['end'] + 6.4): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
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
