"""Synthesised SFX bed for the R17 BUILDX reel (adapted from the R13 TRADER / R9 YOUTUBE beds; no samples, no downloads): to-do cards
cloning + sticker, the kit frame, scissors snipping the gates, parts assembling + typing, repo header + README marker, the GitHub-stars
bars, counter roll + step nodes + blueprint cards, CV pile + "CV KAMU" + badge, the cutaway lid + internals scan, the tutor chat
(typing, dots, answer), the KODE JADI stamp, the Learning terminal + TODO(human) typing, the CTA. Deterministic.
Run: python3 -I tools/sfx.py ."""
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

def wt_(txt, after=0.0):
    v = wt(txt, after)
    if v is None: raise SystemExit("word not found " + txt)
    return v
def out_whoosh(sid): put(st(sid) - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s01 hook: board, cards clone (2), sticker, board out, kit pops, glow, scissors + snips, parts assemble, typing, result, stamp
put(0.02, rise(0.6, 300, 1200), 0.05)
for k, t in enumerate((wt_("to-do") - 0.12, wt_("app") - 0.06)):
    put(t, whoosh(0.3, 700, 2200, 1.4, 0.4), W * 0.35); put(t + 0.28, pop(800 + 150 * k, 1300 + 150 * k, 0.07), 0.12)
put(wt_("lagi?") - 0.02, square_blips([520, 520, 520, 520], 0.05), 0.035); put(wt_("lagi?") + 0.06, pop(600, 1000, 0.09), 0.14)
put(wt_("Coba") - 0.16, whoosh(0.35, 2000, 600, 1.4, 0.35), W * 0.5)
put(wt_("Coba") + 0.08, chime((1046, 1318, 1568), 0.8), 0.05); put(wt_("Coba") + 0.08, pop(500, 900, 0.09), 0.1)
put(wt_("rakit"), rise(0.3, 600, 1400), 0.03)
for k in range(3): put(wt_("Git") - 0.02 + k * 0.15, rip(0.08), 0.07); put(wt_("Git") + 0.0 + k * 0.15, tick(0.02, 3200), 0.12)
put(wt_("versi") - 0.06, whoosh(0.45, 500, 1800, 1.3, 0.45), W * 0.4)
for k in range(2): put(wt_("sendiri,") + 0.02 + k * 0.1, tick(0.02, 2600), 0.08)
for k in range(3): put(wt_("sendiri,") + 0.12 + k * 0.08, pop(1000 + 120 * k, 1600 + 120 * k, 0.05), 0.08)
typing(wt_("versi") + 0.12, wt_("versi") + 0.12 + 12 / 22, 0.09, 22)
put(wt_("versi") + 0.12 + 12 / 22 + 0.12, chime((1318.5, 1760), 0.6), 0.045)
put(wt_("nol.") - 0.08, boom(0.3, 150, 70), 0.16); put(wt_("nol.") - 0.06, pop(700, 1200, 0.09), 0.12)
out_whoosh("s02")
# --- s02 repo: header drop + flap, README card, marker, chips, leaderboard, bars, #1, date
put(st("s02") + 0.02, whoosh(0.45, 2400, 600, 1.4, 0.45), W * 0.6); put(st("s02") + 0.32, flap(), 0.1)
put(wt_("Panduannya") + 0.0, whoosh(0.35, 500, 1800, 1.4, 0.4), W * 0.4)
put(wt_("gratis") - 0.04, pop(800, 1300, 0.08), 0.12)
put(wt_("Build") - 0.06, scribble(0.65), 0.035)
put(wt_("repo") - 0.12, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.45)
for k in range(3): put(wt_("repo") + 0.04 + k * 0.08, tick(0.018, 3000 + 200 * k), 0.06)
put(wt_("bintang") - 0.1, rise(0.7, 400, 1500), 0.035)
put(wt_("terbanyak") - 0.02, chime((1318.5, 1760, 2637), 1.0), 0.06); put(wt_("terbanyak"), pop(700, 1200, 0.08), 0.12)
put(wt_("saat") - 0.04, pop(900, 1500, 0.06), 0.08)
out_whoosh("t1")
# --- t1 isinya: flap, counter card, digits roll, step nodes, blueprint cards
put(st("t1") + 0.02, flap(), 0.12)
put(wt_("Isinya") - 0.02, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.45)
for k in range(14): put(wt_("ratusan") - 0.12 + k * 0.06, tick(0.012, 3400 + 60 * (k % 4)), 0.045)
put(wt_("ratusan") + 0.8, pop(900, 1500, 0.07), 0.1)
for k in range(5): put(wt_("step") - 0.08 + k * (wt_("step:") + 0.3 - wt_("step") + 0.08) / 4, square_blips([660 + 110 * k], 0.06), 0.045)
for k, w in enumerate(("Git,", "Docker,", "database,", "sistem")):
    put(wt_(w) - 0.14, whoosh(0.25, 600, 2000, 1.4, 0.4), W * 0.3); put(wt_(w) - 0.02, pop(700 + 120 * k, 1200 + 120 * k, 0.08), 0.12)
put(wt_("operasi."), boom(0.25, 180, 80), 0.1)
out_whoosh("t2")
# --- t2 portofolio: flap, pile deals, highlights, sticker, CV KAMU, chips, pulse, badge
put(st("t2") + 0.02, flap(), 0.12)
put(wt_("To-do") - 0.12, whoosh(0.35, 500, 1800, 1.4, 0.4), W * 0.4)
for k in range(6): put(wt_("To-do") - 0.04 + k * 0.05, tick(0.02, 2400 + 120 * k), 0.07)
for k in range(6): put(wt_("app", 17) - 0.06 + k * 0.06, tick(0.016, 1800), 0.06)
put(wt_("pasaran.") + 0.02, pop(500, 800, 0.1), 0.13); put(wt_("pasaran.") + 0.04, buzz(0.18), 0.025)
put(wt_("Git", 18) - 0.2, whoosh(0.45, 600, 2200, 1.3, 0.45), W * 0.5)
put(wt_("rakitan") - 0.04, chime((1046, 1318.5), 0.6), 0.045)
for k in range(9): put(wt_("rakitan") + 0.06 + k * 0.05 + (0.3 if k > 4 else 0), pop(1000 + 60 * k, 1600 + 60 * k, 0.04), 0.06)
put(wt_("CV") - 0.04, pop(600, 900, 0.08), 0.08)
put(wt_("beda.") - 0.06, chime((1318.5, 1760, 2637), 0.9), 0.06); put(wt_("beda.") - 0.06, pop(800, 1400, 0.08), 0.12)
out_whoosh("t3")
# --- t3 interview: flap, question, panel, typing, lid up, boxes, arrows, hashes, scan, note, pills
put(st("t3") + 0.02, flap(), 0.12)
put(wt_("interview,") - 0.16, pop(600, 1000, 0.09), 0.12)
put(wt_("interview,") + 0.02, whoosh(0.35, 500, 1800, 1.4, 0.4), W * 0.4)
typing(wt_("interview,") + 0.24, wt_("interview,") + 0.24 + 26 / 40, 0.08, 24)
put(wt_("jelasin", 23) - 0.08, whoosh(0.4, 400, 2400, 1.2, 0.3), W * 0.5); put(wt_("jelasin", 23) - 0.06, rip(0.3), 0.04)
for k in range(3): put(wt_("cara", 23.5) - 0.1 + k * 0.12, pop(800 + 150 * k, 1300 + 150 * k, 0.06), 0.11)
for k in range(2): put(wt_("kerjanya") + 0.04 + k * 0.1, tick(0.02, 3000), 0.08)
put(wt_("dari", 24.3) - 0.12, rise(0.6, 500, 2000), 0.035)
for k in range(3): put(wt_("dari", 24.3) - 0.1 + k * 0.1, tick(0.02, 4200), 0.06)
put(wt_("dalam,") - 0.04, pop(700, 1200, 0.07), 0.08)
put(wt_("bukan") - 0.04, pop(600, 900, 0.08), 0.1); put(wt_("cuma") + 0.06, pop(900, 1500, 0.08), 0.12); put(wt_("cuma") + 0.1, chime((1568, 2093), 0.6), 0.04)
out_whoosh("s06")
# --- s06 tutor: flap, page, marker + "?", Claude panel, chime, swirl, typing, dots, answer, ID
put(st("s06") + 0.02, flap(), 0.12)
put(wt_("Tutorialnya") - 0.1, whoosh(0.35, 500, 1800, 1.4, 0.4), W * 0.4)
put(wt_("Inggris?") - 0.24, scribble(0.4), 0.035); put(wt_("Inggris?") - 0.02, pop(500, 800, 0.09), 0.12)
put(wt_("Jadiin") - 0.12, whoosh(0.4, 600, 2200, 1.3, 0.45), W * 0.45)
put(wt_("Claude", 28) - 0.02, chime((1046, 1318, 1568), 0.9), 0.05)
put(wt_("tutor:"), rise(0.35, 600, 1600), 0.035); put(wt_("tutor:") + 0.06, pop(800, 1300, 0.07), 0.1)
typing(wt_("minta", 29) - 0.06, wt_("minta", 29) - 0.06 + 80 / 62, 0.08, 20)
put(wt_("pakai", 31) - 0.04, pop(700, 1200, 0.08), 0.1)
for k in range(5): put(wt_("pakai", 31) + 0.02 + k * 0.11, tick(0.016, 2800 + 100 * k), 0.05)
put(wt_("Indonesia."), chime((1318.5, 1760), 0.6), 0.045)
out_whoosh("s07")
# --- s07 Learning: flap, request, X, strike, stamp, out, terminal + typing, result, editor, TODO, badge, typing, chip, header out
put(st("s07") + 0.02, flap(), 0.12)
put(st("s07") + 0.06, whoosh(0.35, 500, 1800, 1.4, 0.4), W * 0.4)
put(wt_("Jangan") + 0.08, boom(0.3, 160, 70), 0.16); put(wt_("Jangan") + 0.12, buzz(0.22), 0.04)
put(wt_("kode") - 0.04, rip(0.26), 0.06)
put(wt_("jadi.") - 0.06, pop(500, 800, 0.09), 0.13)
put(wt_("Pakai", 34) - 0.38, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
put(wt_("Pakai", 34) - 0.12, whoosh(0.3, 500, 1800, 1.4, 0.4), W * 0.35)
typing(wt_("Pakai", 34) + 0.06, wt_("Pakai", 34) + 0.06 + 22 / 30, 0.09, 22)
put(wt_("Code:") - 0.04, chime((1318.5, 1760, 2637), 0.8), 0.05)
put(wt_("Learning") - 0.04, whoosh(0.35, 500, 1800, 1.4, 0.4), W * 0.35)
put(wt_("beberapa") - 0.06, pop(800, 1300, 0.07), 0.1); put(wt_("beberapa") + 0.06, pop(900, 1500, 0.06), 0.08)
typing(wt_("kamu", 37) - 0.12, wt_("kamu", 37) - 0.12 + 38 / 52, 0.1, 24)
put(wt_("sendiri.", 37.5) - 0.02, chime((1568, 2093), 0.6), 0.05); put(wt_("sendiri.", 37.5), pop(800, 1400, 0.07), 0.1)
put(st("s08") - 0.3, whoosh(0.32, 2000, 600, 1.4, 0.35), W * 0.45)
# --- s08 CTA
put(st("s08") + 0.04, pop(600, 1000, 0.08), 0.1)
put(wt_("Komen") - 0.06, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(5): put(wt_("RAKIT,") - 0.08 + k * 0.06, tick(0.022, 4200), 0.15)
put(wt_("RAKIT,") + 0.4, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", 39) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("kirim", 39) - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

