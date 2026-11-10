"""Synthesised SFX bed for the IGAGENT reel (no samples, no downloads): Claude flare, lanyard badges dropping + swinging, a GRATIS stamp,
the 13-badge team wall, an x-ray scan + leaderboard sort, a slot machine for the hooks + score stamps, a 12-segment ring fill, the week
board, the 9-card deal, an eraser, paste/install/"selesai", a blocked switch + lock + DRAF stamps, the CTA. Deterministic.
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
st = lambda i: S[i]["start"]
# --- s01 hook
put(0.02, rise(0.6, 300, 1200), 0.05); put(wt("Claude") - 0.02, chime((1046, 1318, 1568), 1.1), 0.07)
for k in range(6): put(1.36 + k * 0.07, whoosh(0.25, 1800, 700, 1.6, 0.25), W * 0.35); put(1.55 + k * 0.07, tick(0.02, 2200 + 150 * k), 0.08)
put(wt("Gratis,") - 0.04, boom(0.45, 150, 60), 0.3); put(wt("Gratis,") - 0.02, pop(300, 140, 0.12), 0.2)
put(3.9, pop(800, 1300, 0.08), 0.12); put(wt("source.") + 0.05, chime((1760, 2349), 0.7), 0.05)
# --- s02 team wall
put(wt("Namanya") - 0.08, whoosh(0.45, 2400, 600, 1.4, 0.4), W * 0.7)
typing(5.51, 6.6, 0.09, 18); put(6.6, chime((1318.5, 1760), 0.6), 0.04)
for k in range(13): put(7.14 + k * 0.032, tick(0.018, 3000 + 60 * k), 0.07)
put(wt("13") - 0.02, pop(700, 1200, 0.09), 0.14)
for k in range(13): put(8.5 + k * 0.09, flap(), 0.05)
put(9.7, whoosh(0.5, 2000, 6000, 2.0, 0.3), W * 0.35)
# --- r1 /ig-viral
put(st("r1") + 0.25, whoosh(0.4, 2000, 500, 1.3, 0.4), W * 0.6)
put(wt("kaget:") - 0.03, boom(0.45, 140, 55), 0.3); put(wt("kaget:") + 0.02, zap(0.4), 0.06)
for k in range(6): put(11.6 + k * 0.06, pop(800 + 80 * k, 1200 + 80 * k, 0.05), 0.08)
for k in range(14): put(wt("bedah") + k * 0.07, tick(0.015, 4600), 0.04)
for k in range(5): put(wt("urutin") + k * 0.15, whoosh(0.18, 1400, 2600, 2.0, 0.2), W * 0.3)
for k in range(6): put(15.2 + k * 0.05, pop(1000 + 60 * k, 1500 + 60 * k, 0.04), 0.07)
put(wt("melonjak.") - 0.03, boom(0.3, 220, 100), 0.14); put(wt("melonjak.") + 0.05, chime((1568, 2093, 2637), 0.9), 0.07)
# --- r2 /ig-reel: note, script, slot machine, score stamps
put(wt("Lalu,") - 0.02, whoosh(0.5, 600, 2400, 1.2, 0.5), W * 0.6)
typing(wt("ide") - 0.05, wt("ide") + 0.45, 0.1, 22)
put(wt("dijadiin") - 0.02, whoosh(0.35, 500, 1800, 1.4, 0.4), W * 0.5)
put(wt("reel.", st("r2")) - 0.02, tick(0.04, 1500), 0.22)
for k in range(26): put(wt("Tiga", st("r2")) + 0.1 + k * 0.05, tick(0.012, 3200 + (k % 4) * 300), 0.05)
for w in ["hook", "26", "rumus,"]: put(wt(w, st("r2")) - 0.01, tick(0.03, 1600), 0.2); put(wt(w, st("r2")) + 0.02, pop(600, 900, 0.07), 0.1)
for t in (22.04, 22.2, 22.37): put(t, boom(0.22, 200, 100), 0.14); put(t + 0.01, pop(400, 200, 0.08), 0.1)
put(22.2, chime((1568, 2093), 0.6), 0.04); put(22.8, whoosh(0.3, 2000, 600, 1.5, 0.4), W * 0.5)
# --- r3 /ig-profile: scan, 12-segment ring, score, fix
put(st("r3") + 0.05, flap(), 0.12)
for k in range(10): put(wt("diaudit") + k * 0.06, tick(0.015, 4400), 0.04)
for k in range(12): put(wt("12", st("r3")) + k * 0.06, pop(900 + 40 * k, 1300 + 40 * k, 0.04), 0.07)
put(wt("100.", st("r3")) - 0.02, pop(700, 1100, 0.08), 0.12)
put(wt("lemah") - 0.02, buzz(0.2), 0.05); put(wt("dibenerin") - 0.02, scribble(0.4), 0.09)
put(wt("duluan.") - 0.02, rise(0.5, 500, 1400), 0.05); put(wt("duluan.") + 0.3, chime((1318.5, 1760, 2637), 0.9), 0.06)
# --- r4 /ig-plan: the week board
put(st("r4") + 0.05, whoosh(0.5, 500, 2000, 1.2, 0.5), W * 0.6)
for k in range(7): put(29.5 + k * 0.09, flap(), 0.08)
for w in ["Posting", "formatnya", "jam"]: put(wt(w, st("r4")) - 0.02, pop(800, 1300, 0.07), 0.11)
for k in range(10): put(wt("10", st("r4")) + k * 0.05, pop(1000 + 50 * k, 1500 + 50 * k, 0.04), 0.07)
put(wt("ajak") - 0.02, whoosh(0.5, 1800, 3600, 2.0, 0.25), W * 0.35); put(wt("interaksi.") + 0.05, chime((1568, 2093), 0.7), 0.05)
# --- s07 the rest + the eraser
for k in range(7): put(36.7 + k * 0.08, flap(), 0.08)
for w in ["Caption,", "carousel,", "story,", "balas", "komentar,", "DM,"]: put(wt(w, st("s07")) - 0.05, whoosh(0.2, 2600, 1100, 2.0, 0.2), W * 0.35); put(wt(w, st("s07")) + 0.02, tick(0.025, 2000), 0.16)
put(40.81, tick(0.025, 2000), 0.14); put(40.93, tick(0.025, 2100), 0.14)
put(wt("bersihin") - 0.02, scribble(0.55), 0.1); typing(wt("bersihin") + 0.5, wt("gaya", st("s07")) - 0.05, 0.08, 20)
put(wt("gaya", st("s07")) - 0.02, scribble(0.5), 0.1); put(wt("AI.") - 0.02, chime((1318.5, 1760, 2637), 0.9), 0.06)
# --- s08 install
put(st("s08") + 0.02, whoosh(0.45, 2400, 700, 1.4, 0.35), W * 0.6)
for k in range(3): put(wt("gampang.") + k * 0.08, pop(900 + 120 * k, 1300 + 120 * k, 0.05), 0.09)
put(wt("Tempel", st("s08")) - 0.15, tick(0.03, 1600), 0.16); put(wt("Tempel", st("s08")) + 0.02, whoosh(0.3, 2400, 800, 1.6, 0.3), W * 0.5)
typing(wt("suruh") - 0.02, wt("install.") - 0.05, 0.1, 22); put(wt("install.") - 0.02, tick(0.03, 2000), 0.2); put(wt("install.") + 0.02, whoosh(0.35, 700, 2400, 1.4, 0.4), W * 0.5)
put(wt("Selesai.") - 0.03, boom(0.3, 200, 90), 0.14); put(wt("Selesai.") + 0.02, chime((1568, 2093, 2637), 1.0), 0.08)
for k in range(13): put(wt("Selesai.") + 0.12 + k * 0.03, tick(0.012, 3500 + 60 * k), 0.04)
# --- s09 nothing posts by itself
put(st("s09") + 0.05, whoosh(0.5, 300, 1600, 1.1, 0.5), W * 0.6)
for w in ["nggak", "keposting"]: put(wt(w, st("s09")) - 0.02, buzz(0.18), 0.05); put(wt(w, st("s09")), tick(0.03, 1200), 0.16)
put(wt("sendiri.", st("s09")) - 0.02, tick(0.04, 1500), 0.26); put(wt("sendiri.", st("s09")) + 0.03, boom(0.2, 240, 120), 0.1)
for k in range(3): put(wt("Semuanya") + 0.1 + k * 0.1, whoosh(0.2, 900, 2400, 1.6, 0.25), W * 0.3)
for k in range(3): put(wt("draf,") + k * 0.14, boom(0.25, 160, 70), 0.18); put(wt("draf,") + 0.01 + k * 0.14, pop(300, 140, 0.1), 0.12)
put(wt("posting.") - 0.02, tick(0.04, 1800), 0.26); put(wt("posting.") + 0.05, chime((1318.5, 1760), 0.7), 0.05)
# --- s10 CTA
put(st("s10") + 0.05, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.6)
put(wt("link-nya?") - 0.02, pop(700, 1100, 0.07), 0.1)
put(wt("Komen") - 0.1, whoosh(0.35, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(3): put(wt("TIM,") - 0.02 + k * 0.07, tick(0.022, 4200), 0.15)
put(wt("aku", st("s10")) - 0.02, pop(900, 1600, 0.1), 0.15)
put(wt("kirim", st("s10")) - 0.02, whoosh(0.7, 700, 3600, 1.2, 0.5), W)
put(wt("DM.") - 0.02, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.5, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
