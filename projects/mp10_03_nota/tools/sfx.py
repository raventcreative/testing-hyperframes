"""Synthesised SFX for MasterPajak AI Video 3 (Foto Nota -> Pembukuan). No samples, no music (client rule); sits under the VO.
Paper flutter/landings for the receipt drawer, camera shutters + flash shimmer, gallery scroll ticks, hologram fx, upload blips,
a scan sweep, lift-whoosh + landing 'thock' for every field/row that flies into the ledger, marker strokes, keyboard ticks,
the series transitions (band sweep, beam + boom, iris) and the end-card chime. All beat times are read from window.TM in
index.html (same offsets as the timeline), so a VO re-time moves the sound too. Deterministic.
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
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 3.2)
    x = np.tanh(1.8 * (x + svf_bp(rng.standard_normal(n), np.full(n, 180.0), 0.8) * np.exp(-t * 9) * 0.6))
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

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy texture and a slight pitch drift"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), 2600 + 900 * np.sin(np.pi * t / dur), 1.6)
    tex = 0.6 + 0.4 * np.abs(np.sin(2 * np.pi * (45 + 25 * rng.random()) * t + rng.random() * 6))
    e = np.minimum(1, t / 0.025) * np.minimum(1, (dur - t) / 0.06)
    x = x * tex * e; return x / (np.abs(x).max() + 1e-9)

def paper(dur=0.3, bright=2600):
    """paper rustle / landing: crackly jittered noise band, fast attack"""
    n = int(dur * SR); t = np.arange(n) / SR
    jit = np.repeat(rng.random(n // 160 + 1), 160)[:n] ** 2.5
    x = svf_bp(rng.standard_normal(n), np.linspace(bright, bright * 0.6, n), 1.3) * (0.35 + jit) * np.exp(-t * 9) * np.minimum(1, t / 0.006)
    return x / (np.abs(x).max() + 1e-9)

def shutter():
    """two-blade camera shutter: click, short mechanical burst, second click"""
    a = tick(0.012, 2600); b = svf_bp(rng.standard_normal(int(0.03 * SR)), np.full(int(0.03 * SR), 3400.0), 1.5) * np.exp(-np.arange(int(0.03 * SR)) / SR * 90)
    x = np.zeros(int(0.16 * SR)); x[: len(a)] += a; x[int(0.008 * SR): int(0.008 * SR) + len(b)] += 0.6 * b / (np.abs(b).max() + 1e-9)
    c = tick(0.014, 2000); i = int(0.075 * SR); x[i: i + len(c)] += 0.8 * c
    return x / np.abs(x).max()

def thock(f=260):
    """soft landing of a chip/row in its slot: low pop + tiny paper tick"""
    p = pop(f * 1.8, f, 0.11); k = tick(0.01, 3800); x = p.copy(); x[: len(k)] += 0.35 * k
    return x / np.abs(x).max()

def scan(dur=1.15):
    """scan beam: soft rising sine + airy band, light tremolo"""
    n = int(dur * SR); t = np.arange(n) / SR
    f = 520 + 900 * (t / dur)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * (0.6 + 0.4 * np.sin(2 * np.pi * 14 * t)) * 0.5
    x += svf_bp(rng.standard_normal(n), f * 3, 4.0) * 0.5
    x *= env(n, 0.2, 1.0)
    return x / np.abs(x).max()

W = 0.22; P_ = 0.15; MK = 0.11
def wh(t, a=0.5, f0=300, f1=2600, q=1.1, at=0.6, g=1.0): put(t, whoosh(a, f0, f1, q, at), W * g)
def holo_fx(t0, g=1.0):
    put(t0, zap(0.35), 0.05 * g); put(t0 + 0.02, whoosh(1.1, 300, 4200, 1.8, 0.9), W * 0.45 * g)
    put(t0 + 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.06 * g)

# ---------- S1 · hook: drawer + falling receipts, the phone snaps one, gallery, "lupa?" ----------
wh(0.0, 1.2, 220, 700, 0.9, 0.5, 0.3)
for t0, d in ((0.0, 0.62), (0.3, 0.8), (0.7, 0.82)):
    wh(t0, d, 900, 2400, 1.4, 0.7, 0.18); put(t0 + d - 0.01, paper(0.32, 2400), 0.16); put(t0 + d + 0.02, pop(260, 120, 0.08), 0.06)
put(TM['numpuk'], marker(0.42), MK)
wh(TM['lupa'] - 0.12, 0.4, 1200, 500, 1.0, 0.4, 0.25)                            # headline swap
wh(TM['lupa'] - 0.36, 0.55, 300, 1800, 1.0, 0.7, 0.55)                           # phone in
SNAP0 = TM['lupa'] + 0.3
put(SNAP0 - 0.03, shutter(), 0.2); put(SNAP0, whoosh(0.35, 3000, 7000, 2.0, 0.2), W * 0.35)
for j in range(16): put(SNAP0 + 0.42 + j * 0.085, tick(0.01, 3400 + (j % 3) * 400), 0.05 * (1 - j / 20))   # gallery scroll
put(TM['lupa'] + 0.95, pop(300, 680, 0.1), 0.1)                                    # robot pops up
put(TM['lupa'] + 1.38, pop(520, 1100, 0.1), P_)                                    # "?"
put(TM['lupa'] + 1.45, square_blips([620, 470], 0.06), 0.025)                      # shrug
wh(TM['lupa'] + 1.45, 0.7, 1600, 400, 1.0, 0.4, 0.3)                               # phone drifts away

# ---------- band sweep -> brand ----------
for k in range(3): wh(TM['brand'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['brand'] + 0.55)
for g0 in (TM['brand'] + 2.9, TM['read'] - 0.6, TM['end'] + 4.4, TM['end'] + 7.0): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
wh(TM['up'] - 0.05, 0.9, 250, 2200, 1.0, 0.75, 0.8)                                # phone flies in
put(TM['snap'] - 0.03, shutter(), 0.22); put(TM['snap'], whoosh(0.4, 3000, 7500, 2.0, 0.2), W * 0.4)
for j in range(6): put(TM['snap'] + 0.45 + j * 0.15, pop(700 + 120 * j, 900 + 120 * j, 0.05), 0.035)   # upload progress
put(TM['snap'] + 1.28, chime((1318.5, 1975.5), 0.9), 0.05)

# ---------- S3 · read ----------
wh(TM['read'] - 0.02, 0.95, 200, 1400, 0.9, 0.6, 0.7)                               # push into the phone
put(TM['read'] + 0.3, pop(600, 1100, 0.07), 0.08)
put(TM['read'] + 0.45, scan(1.15), 0.06)
for k in range(3): put(TM['read'] + 0.75 + k * 0.32, pop(820 + 160 * k, 1500, 0.07), 0.1)
put(TM['susun'] + 0.5, pop(700, 1300, 0.08), 0.08)
wh(TM['susun'] + 0.5, 0.7, 250, 1600, 1.0, 0.6, 0.55)                               # ledger rises
for k, key in enumerate(('tgl', 'kat', 'nom')):
    t0 = TM[key]
    wh(t0, 0.55, 500, 2600 + 300 * k, 1.3, 0.55, 0.5); put(t0 + 0.67, thock(240 + 30 * k), 0.17); put(t0, tick(0.012, 4600), 0.05)
put(TM['nom'] + 0.8, marker(0.45), MK); put(TM['nom'] + 1.0, chime((1568, 2093), 0.8), 0.035)

# ---------- S4 · one photo, one row ----------
wh(TM['row'] - 0.02, 0.75, 1600, 400, 1.0, 0.5, 0.45)
RT = [TM['row'] + 0.65, TM['row'] + 1.25, TM['row'] + 1.85, TM['ketik'] + 1.05, TM['ketik'] + 1.65]
for j, t in enumerate(RT):
    wh(t - 0.42, 0.3, 1800, 900, 1.2, 0.3, 0.18); put(t - 0.1, shutter(), 0.1)
    wh(t, 0.5, 450, 2300, 1.2, 0.55, 0.42); put(t + 0.63, thock(230 + 12 * j), 0.15); put(t + 0.66, marker(0.28), MK * 0.45)
for j in range(6): put(TM['ketik'] + 0.12 + j * 0.085 + 0.02 * (j % 2), tick(0.016, 2400 + 300 * (j % 3)), 0.09)   # "ketik ulang" keys
put(TM['ketik'] + 0.75, marker(0.34), MK * 1.2); put(TM['ketik'] + 0.78, pop(240, 100, 0.12), 0.08)

# ---------- S5 · complete ledger, report ----------
wh(TM['ledger'] - 0.02, 1.0, 1800, 260, 0.9, 0.35, 0.7)
for k in range(6): put(TM['ledger'] + 0.42 + k * 0.1, paper(0.12, 3000), 0.06)
put(TM['ledger'] + 1.15, pop(600, 1200, 0.1), P_); put(TM['ledger'] + 1.2, chime((1318.5, 1760, 2637), 1.0), 0.04)
wh(TM['lap'] - 0.02, 0.8, 250, 2000, 1.0, 0.7, 0.7)
for k in range(3): put(TM['lap'] + 0.35 + k * 0.15, pop(500 + 140 * k, 800 + 200 * k, 0.06), 0.06)
put(TM['lap'] + 1.05, pop(700, 1400, 0.1), P_)

# ---------- beam + iris -> end card ----------
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(TM['end'] + 7.0, chime((784, 1046, 1568), 1.4), 0.05)

x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
