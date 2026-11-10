"""Synthesised SFX bed for the ANIM10 reel (no samples, no downloads): per round: a number slam, the digital re-render SCAN of the
stage sweep, a GENRE STINGER the moment the robot lands in its new style (brick clicks, neon shimmer, comic pow, chalk scratch, 8-bit
arpeggio, pen stroke, soft marimba, console pad, clean UI pops, cinematic braaam), a chip flip; hook flicker + slams, CTA ticks.
Deterministic (seeded). Writes assets/audio/sfx.wav (48 kHz mono, full reel length).
Run: python3 tools/sfx.py ."""
import json, sys, wave
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/timing.json").read_text())
SR = 48000; N = int(T["total_sec"] * SR) + SR
out = np.zeros(N)
rng = np.random.default_rng(7)
S = {s["id"]: s for s in T["scenes"]}
def wt(txt, after=0.0):
    for w in T["words"]:
        if w["w"] == txt and w["s"] >= after: return w["s"]
    return None

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
    u = np.linspace(0, 1, n); k = int(n * a)
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

def rip(dur=0.55):
    n = int(dur * SR); t = np.arange(n) / SR
    jit = np.repeat(rng.random(n // 240 + 1), 240)[:n] ** 3
    x = svf_bp(rng.standard_normal(n), np.linspace(1400, 3600, n), 1.4) * jit * env(n, 0.2)
    return x / np.abs(x).max()

def scribble(dur=0.6):
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 13 * t))
    x = svf_bp(rng.standard_normal(n), 2600 + 900 * np.sin(2 * np.pi * 6.5 * t), 1.6) * am * env(n, 0.2)
    return x / np.abs(x).max()

def rumble(dur=1.5):
    n = int(dur * SR); t = np.arange(n) / SR
    x = svf_bp(rng.standard_normal(n), np.linspace(70, 260, n), 0.7)
    x = x / np.abs(x).max() * env(n, 0.3, 1.0)
    return x


def flap():
    """split-flap clack: two quick clicks + a soft low knock"""
    x = np.zeros(int(0.22 * SR)); a = tick(0.02, 3000); b = tick(0.02, 2400)
    x[: len(a)] += a; i = int(0.11 * SR); x[i:i + len(b)] += 0.8 * b
    k = pop(180, 90, 0.08); x[: len(k)] += 0.35 * k
    return x / np.abs(x).max()

def rise(dur=0.6, f0=300, f1=1200):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * env(n, 0.8, 1.0) * (0.6 + 0.4 * np.sign(np.sin(2 * np.pi * 14 * t)))
    return x / np.abs(x).max()

def buzz(dur=0.35):
    n = int(dur * SR); t = np.arange(n) / SR
    x = (np.sign(np.sin(2 * np.pi * 110 * t)) * 0.5 + np.sign(np.sin(2 * np.pi * 116 * t)) * 0.5) * env(n, 0.05, 1.0)
    return x / np.abs(x).max()

def typing(t0, t1, gain=0.11, rate=16):
    k = 0; t = t0
    while t < t1:
        put(t, tick(0.02, 3600 + 500 * (k % 3)), gain * (0.8 + 0.2 * (k % 2))); k += 1; t += 1.0 / rate * (0.8 + 0.4 * ((k * 7) % 5) / 5)


W = 0.15

def saw(f, n):
    t = np.arange(n) / SR; return 2 * ((f * t) % 1.0) - 1

def lowpass(x, fc):
    y = np.zeros_like(x); a = 1 - np.exp(-2 * np.pi * fc / SR); z = 0.0
    for i in range(len(x)): z += a * (x[i] - z); y[i] = z
    return y

def scan(dur=0.5):
    """digital re-render scan: a rising band-passed sweep + bit-crushed data grains"""
    n = int(dur * SR); t = np.arange(n) / SR; u = t / dur
    x = svf_bp(rng.standard_normal(n), 500 * (5200 / 500) ** u, 2.2) * env(n, 0.7, 1.0)
    g = np.repeat(rng.standard_normal(n // 90 + 1), 90)[:n] * (np.sin(2 * np.pi * 37 * t) > 0.2) * 0.35 * env(n, 0.5, 1.0)
    x = x / (np.abs(x).max() + 1e-9) + g
    return x / np.abs(x).max()

def thud(dur=0.3):
    return boom(dur, 160, 70)

def clicks(n_=3, gap=0.07):
    """toy-brick snaps: a resonant plastic knock + a bright click"""
    x = np.zeros(int((gap * n_ + 0.12) * SR))
    for k in range(n_):
        i = int(k * gap * SR); a = tick(0.018, 3300 + 300 * k); b = pop(700 - 60 * k, 420, 0.05)
        x[i:i + len(a)] += a; x[i:i + len(b)] += 0.55 * b
    return x / np.abs(x).max()

def shimmer(dur=0.9):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate((1760, 2217, 2637, 3520)):
        x += np.sin(2 * np.pi * (f + 3 * np.sin(2 * np.pi * 5 * t)) * t) * np.exp(-t * (2.5 + k)) * (0.8 ** k)
    x *= np.minimum(1, t / 0.04)
    hum = np.sign(np.sin(2 * np.pi * 120 * t)) * 0.12 * np.exp(-t * 7)
    x = x / np.abs(x).max() + hum
    return x / np.abs(x).max()

def pow_(dur=0.35):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.tanh(2.5 * np.sin(2 * np.pi * np.cumsum(220 * (60 / 220) ** (t / 0.12)) / SR) * np.exp(-t * 14))
    x += svf_bp(rng.standard_normal(n), np.full(n, 1800.0), 0.9) * np.exp(-t * 30) * 0.8
    return x / np.abs(x).max()

def chalk(dur=0.55):
    n = int(dur * SR); t = np.arange(n) / SR
    grit = (rng.random(n) > 0.82) * rng.standard_normal(n)
    x = svf_bp(grit + 0.25 * rng.standard_normal(n), 3000 + 1400 * np.sin(2 * np.pi * 3.2 * t), 2.4) * env(n, 0.15, 1.2)
    k = tick(0.03, 1600); x[: len(k)] += 2.5 * k
    return x / np.abs(x).max()

def chip8(notes=(523.25, 659.25, 783.99, 1046.5, 1318.5), step=0.05):
    """an original 8-bit arpeggio (square + a touch of pulse)"""
    seg = []
    for k, f in enumerate(notes):
        n = int(step * SR); t = np.arange(n) / SR
        seg.append((np.sign(np.sin(2 * np.pi * f * t)) * 0.7 + 0.3 * np.sign(np.sin(2 * np.pi * 2 * f * t + 1))) * np.exp(-t * (6 if k == len(notes) - 1 else 22)))
    tail = int(0.12 * SR); t = np.arange(tail) / SR
    seg.append(np.sign(np.sin(2 * np.pi * notes[-1] * t)) * 0.5 * np.exp(-t * 14))
    x = np.concatenate(seg); return x / np.abs(x).max()

def pen(dur=0.6):
    n = int(dur * SR)
    x = svf_bp(rng.standard_normal(n), np.linspace(2400, 5200, n), 3.0) * env(n, 0.55, 1.4)
    return x / np.abs(x).max()

def marimba(freqs=(784, 988, 1175), gap=0.07):
    n = int((gap * len(freqs) + 0.6) * SR); x = np.zeros(n)
    for k, f in enumerate(freqs):
        i = int(k * gap * SR); m = int(0.6 * SR); t = np.arange(m) / SR
        v = (np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t * 30)) * np.exp(-t * 9)
        x[i:i + m] += v[: n - i]
    return x / np.abs(x).max()

def pad2k(dur=1.1):
    """early-2000s console-style synth swell (detuned saws through a slowly opening low-pass + a glassy top)"""
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(saw(f, n) for f in (220, 220.9, 329.6, 330.8)) / 4
    x = lowpass(x * env(n, 0.45, 1.0), 900) * 2.2
    x += np.sin(2 * np.pi * 1760 * t) * 0.18 * env(n, 0.6, 1.0)
    return x / np.abs(x).max()

def uipop():
    x = np.zeros(int(0.2 * SR)); a = pop(1200, 1700, 0.05); b = pop(1500, 2200, 0.05)
    x[: len(a)] += a; i = int(0.08 * SR); x[i:i + len(b)] += 0.8 * b
    return x / np.abs(x).max()

def braaam(dur=1.6):
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(saw(f, n) for f in (55, 55.4, 110.3, 82.4)) / 4
    x = lowpass(x, 420) * 3 * env(n, 0.06, 1.0) * np.exp(-t * 1.1)
    x = np.tanh(1.6 * x) + 0.7 * boom(dur, 70, 32)
    return x / np.abs(x).max()

STING = {"lego": (clicks, 0.22), "glow": (shimmer, 0.12), "comic": (pow_, 0.24), "chalk": (chalk, 0.13), "pixel": (chip8, 0.11),
         "line": (pen, 0.10), "explainer": (marimba, 0.13), "ps2": (pad2k, 0.16), "flat": (uipop, 0.14), "cgi": (braaam, 0.30)}

ROUNDS = json.loads((P / "vendor/rounds.js").read_text().split("window.ROUNDS = ", 1)[1].split(";\n", 1)[0])
H = json.loads((P / "vendor/rounds.js").read_text().split("window.HOOK = ", 1)[1].split(";\n", 1)[0])
CT = json.loads((P / "vendor/rounds.js").read_text().split("window.CTA = ", 1)[1].split(";\n", 1)[0])
# --- s01 hook: the robot flickers through the ten styles, "10" slams, Claude chime, the strip drops in, chip 10 teases ---
put(0.02, boom(0.9, 120, 45), 0.22)
for k in range(10): put(H["tRobot"] + 0.15 + k * 0.2, tick(0.025, 2600 + 220 * k), 0.12)
put(H["t10"] - 0.03, thud(), 0.26)
put(H["tClaude"] - 0.04, chime((1318.5, 1975.5, 2637), 1.0), 0.07)
for k in range(10): put(H["tTahan"] - 0.05 + k * 0.045 + 0.2, pop(600 + 40 * k, 900 + 40 * k, 0.05), 0.06)
put(H["t10b"] - 0.04, shimmer(0.7), 0.06)
# --- the ten rounds ---
for r in ROUNDS:
    put(r["tNum"] - 0.04, thud(), 0.2)                                     # big number slams in
    put(r["sweep"][0], scan(r["sweep"][1] - r["sweep"][0] + 0.05), 0.11)   # re-render scan
    f, g = STING[r["style"]]; put(r["sweep"][1] - 0.02, f(), g)            # genre stinger
    put(r["sweep"][1] - 0.06, tick(0.03, 3000), 0.1)                       # strip chip flips open
    put(r["tDesc"] - 0.06, pop(800, 1200, 0.05), 0.05)
# --- s12 CTA ---
put(CT["start"] + 0.05, whoosh(0.55, 2000, 500, 1.2, 0.4), W * 0.7)
for k in range(10): put(CT["start"] + 0.3 + k * 0.05, pop(900 + k * 50, 1300 + k * 50, 0.05), 0.06)
for k in range(6): put(CT["tPrompt"] - 0.05 + k * 0.055, tick(0.022, 4200), 0.14)
put(CT["tPrompt"] + 0.35, pop(900, 1600, 0.1), 0.15)
put(CT["tDM"] - 0.5, whoosh(0.7, 700, 3600, 1.2, 0.5), W)
put(CT["tDM"] - 0.02, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.4), 0.06)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
