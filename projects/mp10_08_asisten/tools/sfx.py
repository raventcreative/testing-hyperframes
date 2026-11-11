"""Synthesised SFX for MasterPajak AI Video 8 (Asisten AI vs Tim Ahli) — sits under the VO (no samples, no music, per the client's
rule). Deterministic. Beat times are parsed from window.TM in index.html, so a VO re-time moves every cue.
Cues: versus set opening + VS impact, stabilo marker strokes, dive whoosh into the AI lane, chat send / typing ticks / answer
pop + digit-roller ratchet, data cards flying into the answer, whip pan, tangle scribble, card flip + iris, expert avatars,
MasterPajak AI band sweep, chest hologram fx, links, beam + iris, end card pops and chime.
Writes assets/audio/sfx.wav (48 kHz mono, TM.total s). Run from the project folder: python3 tools/sfx.py"""
import sys, wave, re
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR = 48000
_tm = re.search(r'window\.TM = (\{.*?\});', (P / 'index.html').read_text()).group(1)
TM = {k: float(v) for k, v in re.findall(r'(\w+):\s*([\d.]+)', _tm)}
TOTAL = TM['total']; N = int(TOTAL * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(8)
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

def scribble(dur=0.6):
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 9 * t + 2 * np.sin(2 * np.pi * 1.3 * t)))
    x = svf_bp(rng.standard_normal(n), 2400 + 900 * np.sin(2 * np.pi * 4.5 * t), 1.6) * am * env(n, 0.15)
    return x / np.abs(x).max()

def flap(dur=0.22):
    """card / paper flip: a short filtered noise burst with a soft low knock"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(900, 2600, n), 1.0) * np.exp(-t * 22)
    x += np.sin(2 * np.pi * 140 * t) * np.exp(-t * 30) * 0.8
    return x / np.abs(x).max()

def marker(dur=0.4):
    """felt-tip highlighter stroke: band-passed noise with a scratchy 40-70 Hz texture and a slight pitch drift"""
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

# S0 · versus set opens, bubbles, VS impact, stabilo on "ahli"
wh(0.0, 0.9, 250, 1400, 1.0, 0.5, 0.35)
put(0.32, pop(240, 110, 0.14), 0.10); put(0.42, pop(260, 120, 0.14), 0.10)
for k, d in enumerate((0.2, 0.35, 0.5, 0.62)): put(d, pop(900 + 120 * k, 1500, 0.06), 0.04)
put(TM['q'] + 0.45, pop(520, 1100, 0.1), P_); put(TM['q'] + 0.47, boom(0.5, 150, 60), 0.12)
put(TM['q2'] + 0.75, marker(0.42), MK)
# dive into the AI lane
wh(TM['ai'] - 0.74, 0.78, 200, 3200, 1.0, 0.85, 0.95); put(TM['ai'] - 0.02, boom(0.6, 120, 45), 0.13)
# S1 · chat: tag, send, typing, answer, rows, digit roller, stabilo, data cards into the answer
put(TM['ai'] + 0.3, pop(700, 1300, 0.08), 0.08)
put(TM['ask'], pop(900, 1700, 0.07), P_); wh(TM['ask'] - 0.03, 0.25, 900, 3200, 1.4, 0.3, 0.25)
t = TM['ask'] + 0.95
while t < TM['ans'] - 0.12:
    put(t, tick(0.015, 3800 + 900 * rng.random()), 0.05); t += 0.08 + 0.07 * rng.random()
put(TM['ans'], pop(520, 1050, 0.1), P_); put(TM['ans'] + 0.05, chime((1568, 2093), 0.8), 0.035)
for d in (0.15, 0.4, 0.62, 0.9): put(TM['ans'] + d, tick(0.02, 3000), 0.07)
t, step = TM['ans'] + 0.92, 0.03
while t < TM['ans'] + 1.62:
    put(t, tick(0.012, 5200), 0.045); t += step; step *= 1.09
put(TM['ans'] + 1.55, marker(0.45), MK)
for k in range(3):
    t0 = TM['dat'] + k * 0.2
    put(t0, whoosh(0.55, 300, 2200, 1.2, 0.7), W * 0.35); put(t0 + 0.56, pop(700 + 160 * k, 1400 + 200 * k, 0.07), 0.11)
# whip pan to the AHLI lane
wh(TM['ex'] - 0.46, 0.62, 220, 3400, 0.9, 0.55, 1.0); wh(TM['ex'] - 0.38, 0.5, 600, 2400, 1.4, 0.5, 0.4)
# S2 · tag, tangle scribble, sticky, stabilo, flip + iris, avatars, list, "sesuai layanan"
put(TM['ex'] + 0.2, pop(700, 1300, 0.08), 0.08)
put(TM['ex'] + 0.45, scribble(1.5), 0.075)
put(TM['ex'] + 1.6, pop(420, 900, 0.1), 0.12)
put(TM['ex'] + 2.2, marker(0.5), MK)
wh(TM['tim'] - 0.5, 0.65, 350, 2600, 1.1, 0.6, 0.6); put(TM['tim'] - 0.12, flap(0.22), 0.12); put(TM['tim'] + 0.16, boom(0.55, 130, 55), 0.1)
for k, d in enumerate((0.0, 0.12, 0.2)): put(TM['tim'] - 0.1 + d, pop(600 + 150 * k, 1200 + 200 * k, 0.08), 0.1)
put(TM['tim'] + 0.9, tick(0.02, 3200), 0.08); put(TM['tim'] + 1.1, tick(0.02, 3400), 0.08)
put(TM['sl'] + 0.15, marker(0.45), MK)
# band sweep -> brand moment
for k in range(3): wh(TM['sol'] - 0.5 + k * 0.06, 0.45, 300 + 200 * k, 1800 + 400 * k, 1.1, 0.7, 0.5)
holo_fx(TM['sol'] + 0.55)
put(TM['sol'] + 0.4, pop(480, 1000, 0.1), P_)
wh(TM['sol'] + 0.52, 0.5, 300, 1800, 1.1, 0.6, 0.35); wh(TM['sol'] + 0.72, 0.5, 320, 2000, 1.1, 0.6, 0.35)
put(TM['sol'] + 1.15, square_blips([1200, 1600], 0.03), 0.025); put(TM['sol'] + 1.3, square_blips([1350, 1800], 0.03), 0.025)
for g0 in (TM['sol'] + 2.7, TM['sol'] + 4.3, TM['end'] + 4.4, TM['end'] + 7.0): put(g0, square_blips([1800, 900, 1500], 0.02), 0.02)
# beam + iris -> end card
put(TM['end'] - 0.5, pop(500, 1000, 0.1), 0.12); wh(TM['end'] - 0.45, 0.5, 200, 2400, 1.0, 0.9, 1.0); put(TM['end'] - 0.02, boom(0.7, 140, 50), 0.2)
holo_fx(TM['end'] + 0.55)
put(TM['cta'], pop(500, 1000, 0.12), P_); put(TM['bio'], pop(900, 1500, 0.08), 0.1)
put(min(TOTAL - 1.0, TM['bio'] + 1.8), chime((784, 1046, 1568), 1.4), 0.05)
x = out[: int(TOTAL * SR)]
x = x / max(1e-9, np.abs(x).max()) * 0.89
x16 = (np.clip(x, -1, 1) * 32767).astype(np.int16)
(P / "assets/audio").mkdir(parents=True, exist_ok=True)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x16.tobytes()); f.close()
print("sfx.wav", round(len(x16) / SR, 2), "s")
