"""Synthesised SFX for MasterPajak AI Video 13 (Laris Tapi Saldo Tipis) — sits under the VO (no samples, no music, per the client's rule).
Deterministic. Every beat time is read from window.TM in index.html, so a VO re-time moves the sound with the picture.
S1 paper pops, parcel thuds, order pings, odometer ticks · whip · S2 balance roll-down (descending ticks + deflating tone), marker ·
vertical whip · S3 X-ray scanner hum + token sparkles, four coin chimes · wipe "light on" + ribbon swishes + card pops + ring ping ·
brand bands, hologram fx, report row pops + coin docks + marker · beam/iris, end-card hologram, CTA pops, chime.
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
rng = np.random.default_rng(13)
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
    k = max(1, int(n * a))
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

def square_blips(notes, step=0.055):
    out_ = []
    for f in notes:
        n = int(step * SR); t = np.arange(n) / SR
        out_.append(np.sign(np.sin(2 * np.pi * f * t)) * 0.6 * np.exp(-t * 18))
    return np.concatenate(out_)

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

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 2600 + 900 * np.sin(np.pi * t / dur)
    x = svf_bp(rng.standard_normal(n), f, 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def thud(f0=150, dur=0.16):
    """cardboard parcel landing: a short low body + a papery noise burst"""
    n = int(dur * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * np.cumsum(f0 * (0.55) ** (t / dur)) / SR) * np.exp(-t * 30)
    pap = svf_bp(rng.standard_normal(n), np.full(n, 1100.0), 0.9) * np.exp(-t * 55) * 0.5
    x = body + pap; return x / np.abs(x).max()

def ping(f=1568, f2=2093, dur=0.32):
    """generic soft two-note notification (no brand sound)"""
    n = int(dur * SR); t = np.arange(n) / SR; h = n // 2
    x = np.zeros(n)
    x[:h] += np.sin(2 * np.pi * f * t[:h]) * np.exp(-t[:h] * 22)
    x[h:] += np.sin(2 * np.pi * f2 * t[: n - h]) * np.exp(-t[: n - h] * 14)
    return x / np.abs(x).max()

def coin(f=2350, dur=0.9):
    """metal coin ring: inharmonic partials, fast attack"""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for r, a, dcy in ((1.0, 1.0, 5.5), (2.76, 0.55, 8), (5.4, 0.3, 12), (8.93, 0.18, 16)):
        x += a * np.sin(2 * np.pi * f * r * t + rng.random()) * np.exp(-t * dcy)
    x += svf_bp(rng.standard_normal(n), np.full(n, 6000.0), 1.5) * np.exp(-t * 90) * 0.5
    return x / np.abs(x).max()

def hum(dur=1.7):
    """X-ray scanner: mains hum harmonics + a band-passed buzz that brightens as it sweeps"""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    x = sum(np.sin(2 * np.pi * 100 * k * t) / k for k in (1, 2, 3, 5)) * 0.35
    x += svf_bp(rng.standard_normal(n), 900 + 2400 * u, 3.0) * 0.8
    x *= env(n, 0.18, 1.0)
    return x / np.abs(x).max()

def deflate(dur=1.35, f0=520, f1=140):
    """descending tone for the shrinking balance"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** ((t / dur) ** 0.8)) / SR)
    x = np.tanh(1.4 * x) * env(n, 0.12, 1.0)
    return x / np.abs(x).max()

W = 0.22
P_ = 0.15
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
MK = 0.11
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# ---------------- S1 · Rina's shop ----------------
wh(0.0, 0.9, 250, 900, 0.9, 0.6, 0.25)                                   # room tone swell
put(TM['rina'] + 0.45, pop(700, 1300, 0.08), 0.12)                        # name tag
put(TM['laris'] + 0.05, pop(500, 1000, 0.1), P_)                          # order card
for k in range(10): put(TM['laris'] + 0.18 + k * 0.21, thud(140 + 12 * (k % 3)), 0.13)      # parcels
for k in range(8): put(TM['laris'] + 0.3 + k * 0.3, ping(1568 + 60 * (k % 3), 2093 + 60 * (k % 3)), 0.045)   # order bubbles
t = TM['laris'] + 0.25; d = 2.5
for j in range(26):                                                        # odometer ticks (ease in/out)
    u = j / 25; tt = t + d * (0.5 - 0.5 * np.cos(np.pi * u)); put(tt, tick(0.012, 3800), 0.035)
# whip to the balance
wh(TM['tipis'] - 0.34, 0.5, 400, 2800, 1.1, 0.7, 0.9)
# ---------------- S2 · the balance thins out ----------------
s0 = TM['sal'] - 0.55; sD = 1.35
put(s0, deflate(sD), 0.05)
for j in range(30):
    u = j / 29; tt = s0 + sD * (0.5 - 0.5 * np.cos(np.pi * u)); put(tt, tick(0.012, 3400 - 1500 * u), 0.04)
put(s0 + sD + 0.02, thud(110, 0.2), 0.12)
put(TM['sal'] + 0.95, marker(0.42), MK)
# vertical whip down to the month
wh(TM['ternyata'] - 0.36, 0.55, 2400, 300, 1.0, 0.5, 0.9)
# ---------------- S3 · X-ray ----------------
sw0 = TM['ternyata'] + 1.25
put(sw0 - 0.05, tick(0.02, 2000), 0.08); put(sw0, hum(1.7), 0.07)
for j in range(14): put(sw0 + 0.2 + j * 0.1, tick(0.01, 5200 + 300 * (j % 4)), 0.03)   # tokens light up as the line passes
CT = [TM['ongkir'], TM['kemasan'], TM['iklan'], TM['potongan']]
wh(TM['ongkir'] - 0.3, 0.45, 300, 1200, 1.0, 0.6, 0.35)                    # month dims
for k, t0 in enumerate(CT):
    wh(t0 - 0.1, 0.45, 400, 2400, 1.2, 0.7, 0.45)
    put(t0 + 0.35, coin(2100 + 180 * k), 0.06)
# ---------------- S4 · the light comes back on ----------------
wp0 = TM['rapi'] - 0.12
put(wp0, tick(0.02, 2400), 0.12); put(wp0 + 0.01, pop(1600, 2400, 0.04), 0.06)  # "switch"
wh(wp0, 0.75, 500, 3200, 1.0, 0.7, 0.6)
for k in range(4): wh(TM['rapi'] + 0.12 + k * 0.12, 0.5, 600, 1800, 1.3, 0.5, 0.25)  # coins fly to their cards
wh(TM['rapi'] + 0.15, 0.5, 200, 900, 0.9, 0.5, 0.35)                              # source bar fills
for k in range(6): wh(TM['rapi'] + 0.45 + k * 0.12, 0.55, 300, 1500, 1.4, 0.5, 0.22)  # ribbons
for k in range(6): put(TM['rapi'] + 0.72 + k * 0.12, pop(600 + 70 * k, 1200 + 80 * k, 0.07), 0.08)
put(TM['pergi'] + 1.1, marker(0.42), MK)
put(TM['pergi'] + 1.25, ping(1318, 1760, 0.4), 0.06)
# band sweep -> brand
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
# ---------------- S5 · laporan laba rugi ----------------
wh(TM['lap'] - 0.5, 0.8, 250, 1600, 1.0, 0.6, 0.6)                               # report flies in from depth
RT = [TM['lap'] + 0.3, TM['lap'] + 0.55, TM['lap'] + 0.95, TM['lap'] + 1.25, TM['lap'] + 1.55, TM['lap'] + 1.85, TM['baca'] + 0.2]
for k, t0 in enumerate(RT): put(t0, pop(560 + 60 * k, 1100 + 70 * k, 0.08), 0.1)
for k in range(4): put(RT[k + 2] + 0.06, coin(2600 + 150 * k, 0.5), 0.035)        # coins dock
put(TM['baca'] + 0.75, marker(0.45), MK)
for g0 in (TM['sol'] + 3.0, TM['sol'] + 5.6, TM['end'] + 4.4, TM['end'] + 7.0): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# ---------------- beam + iris -> end card ----------------
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
