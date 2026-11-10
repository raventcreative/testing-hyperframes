"""Synthesised SFX bed for the TIGAMENTAL reel (no samples, no downloads): badges popping into three lanes, a flag split, the 100-cell
boards cascading, Motivasi's fast bursts + a flame going out + a stamp, Disiplin's metronome + time-lapse + confetti, Obsesi's
fast-forward + flag throw + zoom-out to 1.000, the mountain rise, the CTA poll + typing + heart. Deterministic. Writes assets/audio/sfx.wav.
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
def bell(dur=0.9):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate((1568, 2349, 3136)):
        x += np.sin(2 * np.pi * f * t) * np.exp(-t * (4 + 2 * k)) * (0.8 ** k)
    x *= 0.75 + 0.25 * np.sin(2 * np.pi * 11 * t)
    return x / np.abs(x).max()

st = lambda i: S[i]["start"]
# --- s01 hook: three badges, the flag splits, boards cascade
put(0.02, pop(500, 760, 0.08), 0.08)
for k in range(3): put(0.29 + 0.09 * k, pop(700 + 120 * k, 1100 + 120 * k, 0.07), 0.13)
for k in range(3): put(0.62 + 0.18 * k, whoosh(0.3, 700, 2400, 1.4, 0.35), W * 0.45)
put(1.26, tick(0.03, 1500), 0.14)
put(wt("sama.") - 0.06, whoosh(0.35, 2400, 800, 1.6, 0.3), W * 0.6)
for k in range(3): put(2.05 + 0.1 * k, tick(0.025, 2400 + 300 * k), 0.14)
put(wt("Posting") - 0.06, whoosh(0.5, 500, 2200, 1.2, 0.4), W * 0.6)
for k in range(20): put(2.79 + k * 0.055, tick(0.012, 3800 + 40 * k), 0.035)
put(3.62, pop(900, 1500, 0.06), 0.1); put(wt("hari.") - 0.02, chime((1318.5, 1760), 0.6), 0.04)
# --- s02 Motivasi: ink flood, fast bursts, the flame dies, BERHENTI stamp
put(st("s02") - 0.15, whoosh(0.4, 400, 1800, 1.3, 0.4), W * 0.6)
put(wt("Motivasi") - 0.07, rise(0.5, 300, 1400), 0.06)
for t0, n in ((5.42, 6), (5.82, 4), (6.29, 3)):
    for k in range(n): put(t0 + k * 0.06, pop(1100 + 70 * k, 1600 + 70 * k, 0.04), 0.08)
put(wt("ke-14,") - 0.02, pop(700, 1100, 0.08), 0.14)
put(7.45, tick(0.02, 1200), 0.08); put(7.6, tick(0.02, 1100), 0.06)
put(7.75, whoosh(0.5, 900, 250, 1.0, 0.3), W * 0.5)
put(8.05, boom(0.4, 150, 60), 0.28); put(8.06, pop(300, 140, 0.12), 0.2)
# --- s03 Disiplin: metronome, time-lapse to 100, confetti
put(st("s03") - 0.05, whoosh(0.5, 600, 2000, 1.3, 0.4), W * 0.6)
put(8.87, rise(0.5, 300, 1300), 0.05)
for k in range(7): put(9.42 + k * 0.26, tick(0.03, 2200 if k % 2 == 0 else 1800), 0.18)
put(11.22, rise(1.0, 400, 2400), 0.06)
for k in range(24): put(11.25 + k * 0.042, tick(0.01, 5200), 0.03)
put(wt("ke-100,") - 0.02, boom(0.3, 220, 100), 0.16)
put(wt("tercapai.") - 0.03, chime((1318.5, 1760, 2637), 1.1), 0.08)
for k in range(10): put(wt("tercapai.") + k * 0.03, pop(1400 + 80 * k, 1900 + 80 * k, 0.03), 0.05)
# --- s04 Obsesi: dolly in, fast-forward, flag thrown, zoom out to 1.000
put(st("s04") - 0.1, whoosh(0.6, 300, 2600, 1.1, 0.6), W * 0.8)
put(14.51, rise(0.5, 300, 1300), 0.05)
put(14.9, rise(0.9, 400, 2600), 0.06)
for k in range(20): put(14.95 + k * 0.043, tick(0.01, 5200), 0.03)
put(wt("100,") - 0.02, boom(0.3, 220, 100), 0.16)
put(16.76, rip(0.3), 0.08); put(17.06, whoosh(0.45, 1400, 3800, 1.5, 0.4), W * 0.6)
put(17.71, whoosh(0.8, 2600, 300, 1.0, 0.6), W * 0.9); put(wt("1.000.") - 0.02, boom(0.6, 120, 45), 0.3)
put(18.33, pop(800, 1300, 0.07), 0.12)
# --- s05 compare: terrain rise, summit flag, taller peak, pan up
put(st("s05") - 0.1, rumble(0.9), 0.08)
put(19.4, pop(600, 1000, 0.08), 0.12); put(wt("target.", 19) - 0.02, pop(1100, 1700, 0.06), 0.12)
put(wt("Obsesi") - 0.05, rumble(1.0), 0.12); put(wt("Obsesi") + 0.1, rise(0.8, 200, 800), 0.06)
put(21.89, whoosh(0.7, 400, 1600, 1.0, 0.4), W * 0.6); put(wt("tinggi.") - 0.02, chime((1568, 2093, 2637), 1.1), 0.07)
# --- s06 CTA: poll cards, typing, heart
put(st("s06") - 0.1, whoosh(0.45, 2000, 600, 1.4, 0.4), W * 0.7)
for k in range(3): put(23.25 + 0.12 * k, pop(800 + 150 * k, 1200 + 150 * k, 0.06), 0.11)
put(wt("Tulis") - 0.12, whoosh(0.35, 600, 2000, 1.4, 0.5), W * 0.5)
typing(24.29, 25.01, 0.1, 20)
put(25.0, pop(900, 1500, 0.07), 0.1); put(25.11, tick(0.03, 2000), 0.2); put(25.21, pop(900, 1600, 0.1), 0.15)
put(T["total_sec"] - 1.2, chime((1046, 1568, 2093, 2637), 1.4), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
