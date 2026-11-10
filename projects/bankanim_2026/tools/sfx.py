"""Synthesised SFX bed for the BANKANIM reel (no samples, no downloads): an editing app whose clips fall off (thuds), a code window
that types and compiles, a flash + 12 card pops, a spotlight per named animation (ding / tick / rise / bell / pops), a silky wave,
copy click + paste + typing + Enter + birth chime, live-edit keystrokes, two "nope" stamps, the CTA (bundle, EDIT typing, heart, plane,
DM chime). Deterministic (seeded). Writes assets/audio/sfx.wav (48 kHz mono, full reel length).
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

# --- s01: the editing app, its clips fall, the code window types, Claude stamps
put(0.02, pop(500, 760, 0.08), 0.08)
for k in range(9): put(0.05 + k * 0.1, tick(0.015, 5200), 0.035)               # playhead scrub
put(wt("nggak") - 0.02, buzz(0.18), 0.03)
for k in range(13): put(wt("After Effects,") + 0.05 + (k % 5) * 0.05 + (k // 5) * 0.03 + 0.4, pop(260 - 8 * k, 110, 0.1), 0.09)
put(wt("After Effects,") + 0.02, whoosh(0.5, 2200, 500, 1.4, 0.3), W * 0.6)
put(wt("semuanya") - 0.3, whoosh(0.42, 600, 1800, 1.2, 0.5), W * 0.5)
put(wt("semuanya") - 0.06, whoosh(0.5, 300, 2600, 1.1, 0.55), W * 0.8)
typing(wt("semuanya") + 0.2, wt("Claude,") - 0.1, 0.09, 18)
put(wt("Claude,") - 0.02, boom(0.5, 140, 60), 0.22); put(wt("Claude,") + 0.06, chime((1318.5, 1975.5, 2637), 0.9), 0.07)
# --- s02: compile → flash → 12 cards → filed into the strip
put(wt("Termasuk") - 0.1, rise(0.45, 400, 1600), 0.05)
put(wt("dua belas") - 0.3, whoosh(0.3, 2600, 400, 1.6, 0.8), W * 0.7)
put(wt("dua belas") - 0.02, boom(0.35, 220, 90), 0.16)
for k in range(12): put(wt("dua belas") + 0.04 + k * 0.03, pop(700 + 40 * k, 1100 + 40 * k, 0.05), 0.06)
put(wt("ini.") - 0.05, whoosh(0.3, 900, 2200, 1.5, 0.4), W * 0.3)
put(wt("Aku") - 0.05, whoosh(0.8, 500, 2600, 1.2, 0.4), W * 0.6)
for k in range(12): put(wt("Aku") + 0.45 + k * 0.045, tick(0.02, 3000 + 80 * k), 0.06)
# --- the 12 rounds
ROUNDS = json.loads((P / "vendor/rounds.js").read_text().split("window.ROUNDS = ", 1)[1].split(";\n", 1)[0])
def bellsnd(dur=0.8):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate((1568, 2349, 3136)): x += np.sin(2 * np.pi * f * t) * np.exp(-t * (4 + 2 * k)) * (0.8 ** k)
    x *= 0.75 + 0.25 * np.sin(2 * np.pi * 11 * t); return x / np.abs(x).max()
for i, r in enumerate(ROUNDS):
    st, end, ty = r["start"], r["start"] + r["dur"], r["type"]
    put(st + 0.02, whoosh(0.45, 600, 2400, 1.3, 0.5), W * 0.55)                  # the card lifts out of its chip
    put(r["tNum"] - 0.06, boom(0.22, 220, 110), 0.12)                             # number badge
    put(r["tName"] - 0.02, pop(900, 1400, 0.06), 0.09)                            # lands on the name
    if ty == "check": put(r["tName"] + 0.3, chime((1760, 2637), 0.6), 0.05)
    if ty == "loading":
        for k in range(8): put(r["tUse"] + k * 0.12, tick(0.018, 3800), 0.04)
    if ty == "counter": put(r["tUse"] - 0.1, rise(0.8, 400, 1500), 0.04)
    if ty == "bell": put(r["tName"] + 0.1, bellsnd(0.8), 0.05); put(r["tUse"] + 0.3, bellsnd(0.6), 0.04)
    if ty == "chart":
        for k in range(4): put(r["tUse"] + 0.5 + k * 0.07, pop(500 + 120 * k, 800 + 120 * k, 0.06), 0.07)
    if ty == "toggle": put(r["tUse"] + 0.9, tick(0.03, 1800), 0.14); put(r["tUse"] + 1.4, tick(0.03, 1500), 0.12)
    if ty == "heart": put(r["tUse"] + 0.1, pop(400, 900, 0.1), 0.14); put(r["tUse"] + 0.15, chime((2093, 2637), 0.5), 0.04)
    if ty == "ring": put(r["tUse"] - 0.1, rise(0.9, 350, 1300), 0.04)
    if ty == "typing": typing(r["tUse"] + 0.2, r["tUse"] + 0.75, 0.06, 14); put(r["speechEnd"] - 0.25, pop(800, 1300, 0.06), 0.08)
    if ty == "upload": put(r["tUse"] - 0.05, whoosh(0.4, 400, 2800, 1.3, 0.5), W * 0.5); put(r["speechEnd"] - 0.1, chime((1568, 2093), 0.5), 0.05)
    if ty == "search": typing(r["tUse"] - 0.3, r["tUse"] + 0.4, 0.06, 18); put(r["speechEnd"] - 0.1, pop(1200, 1800, 0.05), 0.08)
    if ty == "stars":
        for k in range(5): put(r["tUse"] - 0.2 + k * 0.09, pop(900 + 150 * k, 1300 + 150 * k, 0.05), 0.06)
    put(end - 0.42, whoosh(0.35, 2200, 700, 1.4, 0.3), W * 0.45)                  # exit back into the chip
    put(end - 0.08, tick(0.025, 3200), 0.08)                                       # chip comes back with a ✓
# strip grows back into the GRID
G0 = ROUNDS[-1]["start"] + ROUNDS[-1]["dur"] - 0.5
put(G0, whoosh(0.5, 400, 2000, 1.1, 0.5), W * 0.6)
for k in range(12): put(G0 + 0.1 + k * 0.03, pop(700 + 30 * k, 1000 + 30 * k, 0.04), 0.045)
# --- s05: copy → paste → type → Enter → a new card is born
put(wt("Caranya") - 0.05, whoosh(0.4, 2000, 600, 1.3, 0.4), W * 0.5)
put(wt("Copy") - 0.02, tick(0.025, 2600), 0.16); put(wt("Copy") + 0.12, pop(900, 1500, 0.06), 0.08)
put(wt("tempel") - 0.05, whoosh(0.35, 500, 2400, 1.3, 0.4), W * 0.6)
typing(wt("tempel") + 0.1, wt("animasinya") - 0.05, 0.1, 20)
put(wt("animasinya") - 0.02, pop(180, 90, 0.1), 0.18)
put(wt("animasinya") + 0.05, rise(0.5, 300, 1400), 0.05)
put(wt("jadi.") - 0.05, chime((1318.5, 1760, 2637), 0.9), 0.08); put(wt("jadi.") - 0.02, pop(900, 1600, 0.08), 0.1)
# --- s06: live edit
for k in range(5): put(wt("ganti") + 0.05 + k * 0.07, tick(0.02, 3600 + 300 * (k % 2)), 0.08)
for k in range(4): put(wt("datanya.") + k * 0.06, pop(600 + 90 * k, 900 + 90 * k, 0.05), 0.07)
# --- s08 CTA
put(wt("panduan") - 0.05, whoosh(0.6, 400, 2600, 1.1, 0.6), W * 0.7)
for k in range(12): put(wt("panduan") + 0.15 + k * 0.035, pop(900 + 30 * k, 1300 + 30 * k, 0.04), 0.045)
put(wt("animasinya?") + 0.05, boom(0.3, 240, 110), 0.12)
put(wt("Komen") - 0.1, whoosh(0.35, 1800, 600, 1.3, 0.4), W * 0.5)
for k in range(4): put(wt("EDIT,") - 0.02 + k * 0.07, tick(0.022, 4200), 0.15)
put(wt("EDIT,") + 0.35, pop(900, 1600, 0.1), 0.15)
put(wt("kirim") - 0.05, whoosh(0.7, 700, 3600, 1.2, 0.5), W)
put(wt("DM.") - 0.02, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.3, chime((1046, 1568, 2093, 2637), 1.3), 0.06)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
