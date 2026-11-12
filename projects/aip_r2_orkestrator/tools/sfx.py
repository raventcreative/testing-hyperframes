"""Synthesised SFX bed for the AIP R2 ORKESTRATOR reel (agent chaos → 4 pills, the 4 tool cards, the honest note, CTA); kit text below:
Synthesised SFX bed for the PROMPTBUILDER reel (no samples, no downloads): a STOP stamp + price strikes, 6 prompt blocks snapping in,
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
en = lambda i: S[i]["start"] + S[i]["dur"]
def rail_on(w, after):   # a rail pill becomes active
    t = wt(w, after); put(t - 0.02, tick(0.03, 2200), 0.2); put(t + 0.02, pop(600, 950, 0.07), 0.1)
def pops(t0, n, step=0.07, f0=700, g=0.1):
    for k in range(n): put(t0 + k * step, pop(f0 + 80 * k, f0 + 400 + 80 * k, 0.06), g)
# --- s01 hook: agent windows pile up, tangle, chaos swept, 4 pills + title, GRATIS seal, tidy grid
put(0.02, pop(500, 760, 0.08), 0.08)
pops(wt("agent") - 0.06, 2, 0.14, 800, 0.1); pops(wt("banyak,") - 0.14, 3, 0.12, 900, 0.1)
put(wt("tapi") - 0.05, scribble(0.5), 0.07)
for k in range(5): put(wt("berantakan?") - 0.12 + k * 0.05, pop(1500 + 100 * k, 2100 + 100 * k, 0.05), 0.07)
put(wt("berantakan?") + 0.02, buzz(0.28), 0.05); put(wt("berantakan?") + 0.04, boom(0.4, 140, 60), 0.16)
put(wt("Ini") - 0.16, whoosh(0.5, 2200, 500, 1.2, 0.4), W * 0.7)
for k in range(4): put(wt("empat") - 0.16 + k * 0.07, tick(0.03, 2400 + 200 * k), 0.16)
put(wt("empat") - 0.14, whoosh(0.45, 500, 2400, 1.3, 0.5), W * 0.6)
put(wt("open") + 0.02, whoosh(0.35, 1200, 3000, 1.8, 0.4), W * 0.3)
put(wt("gratis") - 0.04, boom(0.35, 200, 90), 0.2); put(wt("gratis") + 0.02, chime((1318.5, 1760, 2637), 1.0), 0.07)
pops(wt("ngaturnya.") - 0.2, 9, 0.045, 900, 0.07); put(wt("ngaturnya.") + 0.35, chime((1568, 2093), 0.7), 0.05)
put(en("s01") - 0.36, whoosh(0.35, 800, 2600, 1.4, 0.4), W * 0.4)
# --- t1 OpenHands Agent Canvas
put(st("t1") - 0.02, whoosh(0.5, 400, 2000, 1.2, 0.5), W * 0.6); rail_on("Satu,", 6)
put(wt("OpenHands") - 0.1, whoosh(0.35, 900, 2600, 1.6, 0.4), W * 0.4); put(wt("Canvas.") - 0.02, pop(900, 1500, 0.08), 0.12)
for k in range(4): put(wt("Canvas.") - 0.08 + k * 0.07, tick(0.02, 3000 + 200 * k), 0.07)
put(wt("pusat") + 0.05, chime((1046, 1318, 1568), 0.9), 0.06)
for w, after in [("jalanin", 9), ("Claude", 10), ("Codex,", 11), ("Gemini,", 12)]:
    t = wt(w, after); put(t - 0.02, rise(0.25, 500, 1100), 0.05); put(t + 0.04, pop(1000, 1500, 0.06), 0.1)
typing(wt("jalanin") + 0.1, wt("Gemini,") + 0.3, 0.06, 18)
for w in ["laptop,", "server,", "cloud."]: put(wt(w) - 0.04, tick(0.03, 2000), 0.18); put(wt(w) + 0.06, pop(800, 1300, 0.07), 0.12)
put(en("t1") - 0.42, pop(1100, 1700, 0.06), 0.12); put(en("t1") - 0.3, whoosh(0.4, 600, 2800, 1.4, 0.4), W * 0.6)
# --- t2 Paperclip
rail_on("Dua,", 15); put(wt("Paperclip.") - 0.12, whoosh(0.35, 900, 2600, 1.6, 0.4), W * 0.4)
put(wt("Kamu", 16) - 0.1, pop(700, 1100, 0.08), 0.13); put(wt("perusahaan") - 0.08, pop(800, 1200, 0.08), 0.12)
pops(wt("AI", 17) - 0.12, 4, 0.09, 800, 0.11)
put(wt("struktur") - 0.06, whoosh(0.4, 1500, 3500, 2.0, 0.4), W * 0.3)
for k in range(3): put(wt("tugas,") - 0.08 + k * 0.07, tick(0.025, 3200 + 250 * k), 0.14)
put(wt("budget,") - 0.1, pop(700, 1000, 0.08), 0.1); put(wt("budget,") + 0.1, rise(0.55, 400, 900), 0.04)
put(wt("approval") - 0.3, whoosh(0.4, 500, 2000, 1.3, 0.5), W * 0.5)
put(wt("kamu.", 21) - 0.06, tick(0.03, 1800), 0.24); put(wt("kamu.", 21) + 0.02, chime((1568, 2093, 2637), 0.9), 0.07)
put(en("t2") - 0.42, pop(1100, 1700, 0.06), 0.12); put(en("t2") - 0.33, whoosh(0.45, 2600, 500, 1.2, 0.4), W * 0.7)
# --- t3 Orca
put(st("t3"), whoosh(0.45, 500, 2600, 1.2, 0.4), W * 0.6); rail_on("Tiga,", 22)
put(wt("Orca.") - 0.12, whoosh(0.35, 900, 2600, 1.6, 0.4), W * 0.4)
put(wt("Satu", 23) - 0.1, pop(700, 1100, 0.08), 0.13); put(wt("koordinator,") - 0.05, chime((1318.5, 1760), 0.6), 0.06)
put(wt("bagi") + 0.02, zap(0.35), 0.04); pops(wt("bagi") + 0.04, 3, 0.05, 1000, 0.1)
pops(wt("agent", 26) + 0.4, 3, 0.06, 600, 0.12)
put(wt("kerja", 27), rise(wt("sendiri.", 28) - wt("kerja", 27) + 0.2, 300, 900), 0.035)
for k in range(3): put(wt("worktree") - 0.12 + k * 0.07, tick(0.025, 2800 + 250 * k), 0.14)
pops(wt("sendiri.", 28) + 0.05, 3, 0.12, 1100, 0.12); put(wt("sendiri.", 28) + 0.42, chime((1568, 2093, 2637), 0.8), 0.06)
put(en("t3") - 0.42, pop(1100, 1700, 0.06), 0.12); put(en("t3") - 0.31, whoosh(0.4, 1800, 400, 1.2, 0.4), W * 0.5)
# --- t4 TeamAI
put(st("t4"), whoosh(0.5, 300, 2200, 1.0, 0.6), W * 0.6); rail_on("Empat,", 29)
put(wt("TeamAI") - 0.12, whoosh(0.35, 900, 2600, 1.6, 0.4), W * 0.4); put(wt("Tencent.") - 0.05, pop(900, 1400, 0.07), 0.11)
for w in ["Skill,", "rules,", "MCP"]: put(wt(w) - 0.08, pop(800, 1200, 0.07), 0.12)
pops(wt("semua") - 0.06, 4, 0.1, 700, 0.11)
typing(wt("disimpan") + 0.05, wt("Git,") - 0.05, 0.07, 20); put(wt("Git,") - 0.1, pop(900, 1500, 0.08), 0.13)
put(wt("sync") - 0.15, whoosh(0.5, 600, 3000, 1.4, 0.4), W * 0.5); pops(wt("sync") + 0.32, 4, 0.07, 1200, 0.1)
put(wt("otomatis.") + 0.1, chime((1046, 1568, 2093), 1.0), 0.07)
put(en("t4") - 0.45, pop(1100, 1700, 0.06), 0.12); put(en("t4") - 0.31, whoosh(0.4, 2000, 600, 1.4, 0.4), W * 0.5)
# --- s06 the honest note
for k in range(4): put(wt("Keempatnya") + k * 0.07, whoosh(0.25, 2400, 900, 2.0, 0.3), W * 0.3); put(wt("Keempatnya") + 0.25 + k * 0.07, pop(700, 1100, 0.07), 0.1)
for k in range(4): put(wt("open", 38) - 0.12 + k * 0.08 + 0.2, pop(500, 300, 0.07), 0.12)
put(wt("gratis.") - 0.04, boom(0.4, 180, 80), 0.2); put(wt("gratis.") + 0.03, chime((1318.5, 1760, 2637), 1.0), 0.07)
put(wt("Cuma,") - 0.15, whoosh(0.5, 2000, 500, 1.2, 0.5), W * 0.5); put(wt("Cuma,") + 0.05, pop(400, 260, 0.1), 0.1)
for w in ["model", "akun", "API"]: put(wt(w, 40) - 0.08, pop(800, 1250, 0.07), 0.12)
put(wt("sendiri.", 43) - 0.1, tick(0.03, 2200), 0.1)
put(en("s06") - 0.34, whoosh(0.35, 800, 2600, 1.4, 0.4), W * 0.4)
# --- s07 CTA
put(st("s07"), whoosh(0.5, 400, 1800, 1.3, 0.4), W * 0.6)
for k in range(4): put(wt("link", 44) - 0.12 + k * 0.07, tick(0.025, 2600 + 200 * k), 0.12)
put(wt("cara", 44) - 0.05, boom(0.3, 220, 110), 0.12); put(wt("cara", 44) + 0.12, pop(900, 1400, 0.07), 0.1)
put(wt("Komen") - 0.32, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.6)
for k in range(5): put(wt("AGENT,") - 0.1 + k * 0.075, tick(0.022, 4200), 0.15)
put(wt("AGENT,") + 0.32, pop(900, 1600, 0.1), 0.15)
put(wt("aku", 46) - 0.08, tick(0.03, 2000), 0.2); put(wt("aku", 46) + 0.15, whoosh(0.6, 700, 3600, 1.2, 0.5), W)
put(wt("DM.") - 0.02, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 0.9, chime((1046, 1568, 2093, 2637), 1.6), 0.06)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
