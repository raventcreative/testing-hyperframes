"""Synthesised SFX bed for the PROMPTBUILDER reel (no samples, no downloads): a STOP stamp + price strikes, 6 prompt blocks snapping in,
a calendar flip + collapse on "capek", Claude chime, the 5-step rail (tick on each step, check on each done), paste / send / build /
typing / copy clicks, the s10 tear + crumple, the CTA (MASTER typing, heart, plane, DM chime). Deterministic. Writes assets/audio/sfx.wav.
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
# --- s01 hook: STOP stamp, prices struck, blocks build the tool, GRATIS stamp
put(0.02, pop(500, 760, 0.08), 0.08)
put(wt("Stop") - 0.04, boom(0.45, 160, 60), 0.3); put(wt("Stop") - 0.02, pop(300, 140, 0.12), 0.22)
put(wt("mahal-mahal.") - 0.02, scribble(0.4), 0.1); put(wt("mahal-mahal.") + 0.25, scribble(0.35), 0.08)
for k in range(6): put(wt("Bikin") + 0.05 + k * 0.09, whoosh(0.2, 900, 2600, 1.6, 0.3), W * 0.35); put(wt("Bikin") + 0.2 + k * 0.09, pop(700 + 60 * k, 1100 + 60 * k, 0.06), 0.1)
put(wt("gratis.") - 0.04, boom(0.35, 200, 90), 0.18); put(wt("gratis.") + 0.02, chime((1318.5, 1760, 2637), 1.0), 0.07)
# --- s02: the 6 parts drop into the prompt
put(st("s02") - 0.2, whoosh(0.4, 500, 2200), W * 0.6)
put(wt("6") - 0.02, pop(600, 1000, 0.09), 0.14)
for w in ["Peran,", "konteks,", "tugas,", "format,", "contoh,", "batasan."]: put(wt(w) - 0.03, whoosh(0.18, 2400, 900, 2.0, 0.2), W * 0.3); put(wt(w) + 0.05, pop(800, 1300, 0.07), 0.13)
put(wt("batasan.") + 0.35, chime((1568, 2093), 0.7), 0.05)
# --- s03: every day again, then the pile collapses on "capek."
put(st("s03") - 0.2, whoosh(0.4, 2000, 600, 1.3, 0.35), W * 0.6)
for k in range(5): put(wt("tiap") - 0.3 + k * 0.22, flap(), 0.12)
put(wt("capek.") - 0.05, rumble(0.6), 0.12); put(wt("capek.") + 0.05, boom(0.5, 110, 45), 0.26); put(wt("capek.") + 0.1, buzz(0.25), 0.04)
# --- s04: Claude arrives, the pile becomes the tool, the 5-step rail
put(wt("Claude", st("s04")) - 0.04, chime((1046, 1318, 1568), 1.1), 0.08)
put(wt("alatnya.") - 0.05, whoosh(0.5, 400, 2400, 1.2, 0.5), W * 0.7)
for k in range(5): put(wt("5", st("s04")) + k * 0.07, tick(0.025, 2600 + 300 * k), 0.12)
# --- the 5 steps: a tick when a step becomes active, a check pop when it is done
for w, after in [("Satu,", 19), ("Dua,", 21), ("Tiga,", 24), ("Empat,", 28), ("Lima,", 33)]:
    put(wt(w, after) - 0.02, tick(0.03, 2200), 0.2); put(wt(w, after) + 0.02, pop(600, 950, 0.07), 0.1)
for t in (20.82, 23.82, 27.69, 32.94, 36.85): put(t, pop(1100, 1700, 0.06), 0.12)
# r1: open Claude
put(wt("buka") - 0.02, tick(0.03, 1800), 0.22); put(wt("buka") + 0.02, whoosh(0.45, 400, 2000, 1.3, 0.45), W * 0.7)
for k in range(3): put(wt("Claude.", 20) + k * 0.08, pop(800 + 120 * k, 1200 + 120 * k, 0.05), 0.08)
# r2: Ctrl+V, paste, send
put(wt("tempel") - 0.25, tick(0.03, 1600), 0.18); put(wt("tempel") - 0.12, tick(0.03, 1700), 0.18)
put(wt("tempel") + 0.02, whoosh(0.35, 2400, 700, 1.6, 0.3), W * 0.6)
for k in range(10): put(wt("tempel") + 0.1 + k * 0.05, tick(0.015, 5000), 0.04)
put(23.2, tick(0.03, 2000), 0.22); put(23.24, whoosh(0.4, 700, 2600, 1.4, 0.4), W * 0.6); put(wt("aku", 23) + 0.02, pop(900, 1500, 0.07), 0.1)
# r3: Claude builds the app
put(24.63, rise(0.9, 300, 1200), 0.05); put(wt("Claude", 25) - 0.02, whoosh(0.6, 2000, 6000, 2.0, 0.3), W * 0.4)
put(wt("aplikasi") - 0.02, pop(700, 1100, 0.08), 0.12); put(wt("kecilnya") - 0.02, pop(800, 1300, 0.08), 0.12)
put(wt("chat.") - 0.02, chime((1568, 2093, 2637), 0.9), 0.07)
# r4: type the idea, press the button
put(wt("ketik") - 0.02, tick(0.03, 1900), 0.22)
typing(30.94, 32.88, 0.1, 20)
put(32.92, tick(0.03, 1800), 0.24); put(32.96, rise(0.5, 400, 1100), 0.05)
# r5: the master prompt fills, copy
put(wt("alatnya", 33) - 0.02, whoosh(0.4, 500, 2400, 1.2, 0.5), W * 0.6)
for k in range(6): put(wt("nyusun") + k * 0.2, pop(700 + 90 * k, 1100 + 90 * k, 0.06), 0.12)
put(wt("lengkap.") - 0.02, chime((1318.5, 1760), 0.7), 0.05)
put(wt("salin.") - 0.02, tick(0.03, 2000), 0.24); put(wt("salin.") + 0.08, chime((1760, 2349, 2637), 0.9), 0.07)
# --- s10: no paid class, no paid prompts
for k in range(6): put(37.2 + k * 0.09, pop(900 + 50 * k, 1300 + 50 * k, 0.05), 0.08)
put(37.37, whoosh(0.35, 600, 2000, 1.4, 0.35), W * 0.5); put(37.47, whoosh(0.35, 700, 2200, 1.4, 0.35), W * 0.5)
put(wt("mahal,") - 0.02, scribble(0.3), 0.1); put(38.35, rip(0.45), 0.14)
put(wt("beli", 39) - 0.02, scribble(0.3), 0.1); put(wt("prompt.", 39) - 0.02, scribble(0.35), 0.1); put(39.68, rip(0.35), 0.1); put(39.72, boom(0.3, 150, 70), 0.12)
put(39.85, pop(700, 1200, 0.09), 0.16); put(39.9, chime((1568, 2093), 0.7), 0.05)
# --- s11 CTA
put(wt("Mau", 40) - 0.02, whoosh(0.5, 400, 1800, 1.3, 0.4), W * 0.6)
for k in range(6): put(wt("alatnya?") + k * 0.06, pop(900 + 60 * k, 1400 + 60 * k, 0.05), 0.08)
put(wt("Komen") - 0.05, whoosh(0.35, 600, 2000, 1.4, 0.5), W * 0.6)
for k in range(6): put(42.13 + k * 0.06, tick(0.022, 4200), 0.14)
put(42.55, pop(900, 1600, 0.1), 0.15)
put(wt("aku", 42) - 0.02, tick(0.03, 2000), 0.2); put(wt("kirim", 42) - 0.02, whoosh(0.7, 700, 3600, 1.2, 0.5), W)
put(wt("DM.") - 0.02, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.5, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
