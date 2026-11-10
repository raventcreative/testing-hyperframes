"""Synthesised SFX bed for the PLUGIN4 reel (no samples, no downloads): terminal typing, a TAHAN DULU stamp, 4 plugin outlines flying to
the dock, each cartridge landing in its slot (clack + chime), the star counter, the ask/plan/test/run pipeline, CLAUDE.md rules, the
token squeeze 63 -> 20, the Codex review, the CTA (SETUP typing, heart, plane, DM chime). Deterministic. Writes assets/audio/sfx.wav.
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
F = [wt("Superpowers.") + 0.6, wt("Skills.") + 0.6, wt("Caveman.") + 0.6, wt("Codex,", st("r4")) + 0.6]
# --- s01 hook: the prompt types, TAHAN DULU, the 4 outlines fly to the dock
typing(0.1, 1.85, 0.09, 18)
put(wt("Sebelum") - 0.03, boom(0.45, 150, 60), 0.3); put(wt("Sebelum") - 0.01, pop(300, 140, 0.12), 0.2)
put(wt("vibe") - 0.02, tick(0.03, 900), 0.12); put(wt("coding") - 0.02, tick(0.03, 900), 0.12)
put(wt("Claude Code,") - 0.02, whoosh(0.5, 2000, 6000, 2.0, 0.3), W * 0.4)
for k in range(4): put(wt("pasang") + 0.02 + k * 0.07, whoosh(0.4, 600, 2600, 1.4, 0.4), W * 0.45); put(2.81 + k * 0.07, tick(0.025, 2600 + 200 * k), 0.16)
put(wt("dulu.") - 0.05, pop(500, 800, 0.08), 0.12)
# --- cartridge landings (all rounds): name pop, fly whoosh, slot clack + chime
for k, w in enumerate(["Superpowers.", "Skills.", "Caveman.", "Codex,"]):
    tn = wt(w, st("r%d" % (k + 1)))
    put(tn - 0.03, pop(700, 1200, 0.09), 0.14); put(F[k] - 0.4, whoosh(0.4, 900, 3000, 1.4, 0.4), W * 0.6)
    put(F[k] - 0.01, tick(0.035, 1800), 0.26); put(F[k] + 0.02, boom(0.25, 220, 110), 0.12); put(F[k] + 0.18, chime((1318.5, 1760, 2637), 0.9), 0.06)
# --- r1 Superpowers: star counter, the blocked shortcut, the 4-step pipeline, tests go green
for k in range(12): put(wt("300") + k * 0.03, tick(0.015, 4000 + 60 * k), 0.05)
put(wt("ribu") - 0.02, boom(0.3, 200, 90), 0.14); put(wt("bintang") - 0.02, chime((1760, 2349), 0.7), 0.06)
put(wt("Claude", st("r1") + 4) - 0.02, whoosh(0.5, 500, 2200, 1.2, 0.4), W * 0.6)
put(wt("nggak") - 0.02, boom(0.35, 140, 60), 0.24); put(wt("nggak") + 0.02, buzz(0.2), 0.04)
for w in ["nanya", "rencana,", "tes", "jalan."]: put(wt(w, st("r1")) - 0.02, pop(800, 1300, 0.07), 0.12)
for k in range(3): put(wt("tes", st("r1")) + 0.05 + k * 0.08, buzz(0.08), 0.03)
for k in range(3): put(wt("jalan.", st("r1")) + 0.05 + k * 0.08, pop(1100 + 150 * k, 1700 + 150 * k, 0.06), 0.11)
put(wt("jalan.", st("r1")) + 0.35, chime((1568, 2093), 0.7), 0.05)
put(st("r2") - 0.3, whoosh(0.4, 2600, 400, 1.2, 0.5), W * 0.7)
# --- r2 Karpathy: one file, the editor opens, 4 rules
put(wt("satu", st("r2")) - 0.02, whoosh(0.35, 2200, 600, 1.6, 0.3), W * 0.5)
typing(wt("CLAUDE.md") - 0.02, wt("CLAUDE.md") + 0.4, 0.1, 22)
put(wt("isinya") - 0.02, whoosh(0.4, 400, 2000, 1.3, 0.4), W * 0.6)
for w in ["Mikir", "sesimpel", "ubah", "buktikan"]: put(wt(w, st("r2")) - 0.02, pop(700, 1100, 0.07), 0.12); typing(wt(w, st("r2")), wt(w, st("r2")) + 0.35, 0.08, 22)
put(wt("sesimpel") + 0.3, whoosh(0.3, 3000, 900, 2.0, 0.2), W * 0.5)
for k in range(3): put(wt("jalan.", st("r2")) + k * 0.1, pop(1100 + 150 * k, 1700 + 150 * k, 0.06), 0.1)
put(st("r3") - 0.32, zap(0.35), 0.06)
# --- r3 Caveman: verbose answer, squeeze, 63 -> 20
typing(wt("Jawaban") - 0.02, wt("dipadatkan") - 0.05, 0.08, 20)
put(wt("dipadatkan") - 0.02, rumble(0.5), 0.1); put(wt("dipadatkan") + 0.1, boom(0.3, 180, 80), 0.16)
for k in range(9): put(wt("tanpa") + 0.05 + k * 0.08, whoosh(0.15, 2500, 1200, 2.0, 0.2), W * 0.25)
put(wt("63") - 0.02, pop(500, 800, 0.08), 0.14)
for k in range(12): put(wt("jadi", st("r3") + 5) + k * 0.025, tick(0.012, 5000), 0.05)
put(wt("20.") - 0.02, boom(0.3, 220, 100), 0.16); put(wt("20.") + 0.05, chime((1568, 2093), 0.7), 0.06)
put(wt("sama.") - 0.02, pop(900, 1500, 0.08), 0.14); put(st("r4") - 0.25, whoosh(0.3, 2000, 500, 1.5, 0.4), W * 0.6)
# --- r4 Codex: /codex:review types, the review lands, self-grading crossed out
put(wt("OpenAI.") - 0.02, pop(800, 1300, 0.07), 0.1)
typing(wt("Kerjaan") - 0.1, wt("Kerjaan") + 0.55, 0.1, 22); put(wt("Kerjaan") + 0.6, tick(0.03, 2000), 0.2)
put(wt("direview") - 0.02, whoosh(0.45, 500, 2400, 1.3, 0.45), W * 0.6)
for k in range(3): put(wt("sama", st("r4") + 3) + 0.1 + k * 0.16, pop(700 + 120 * k, 1100 + 120 * k, 0.07), 0.11)
put(wt("bukan") - 0.02, scribble(0.4), 0.1); put(wt("sendiri.") - 0.02, boom(0.3, 180, 80), 0.14); put(wt("sendiri.") + 0.1, chime((1318.5, 1760), 0.7), 0.05)
# --- s06 CTA
put(st("s06") - 0.2, whoosh(0.35, 600, 2000, 1.4, 0.5), W * 0.6)
for k in range(5): put(wt("SETUP,") - 0.02 + k * 0.06, tick(0.022, 4200), 0.14)
for k in range(4): put(wt("SETUP,") + 0.12 + 0.09 * k, pop(900 + 100 * k, 1300 + 100 * k, 0.05), 0.07)
put(wt("SETUP,") + 0.4, pop(900, 1600, 0.1), 0.15)
put(wt("kirim", st("s06")) - 0.02, whoosh(0.7, 700, 3600, 1.2, 0.5), W)
put(wt("DM.") - 0.02, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.5, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
