"""Synthesised SFX bed for R14 "3 prompt buat ngedit reels pakai Claude Code" — no samples, no downloads: bookmark press + toast,
the deck spreading, header pills, flow line + stamp, each prompt card dealt (whoosh + flap), Salin click + copy chime, card folds,
work folder pop, five tool installs (pop + tick + small chime each), "5 alat siap", reels drop + hearts, scan sweep, console knobs,
"jangan re-upload" buzz, transcript rows, scissors cuts, caption pops, selera.md whoosh, "?", voice bubble, caption lift, stamps,
video files absorbed, the pack, PROMPT keycaps, paper plane, DM chime, end chime. Deterministic (fixed seed).
Writes assets/audio/sfx.wav (mono 48 kHz). Run: python3 tools/sfx.py ."""
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
L = lambda txt, sid: wt(txt, st(sid) - 0.05)          # word time inside a given scene (duplicates-safe)

L = lambda txt, sid: wt(txt, st(sid) - 0.05)          # word time inside a given scene (duplicates-safe)
def deal(t):                                           # a prompt card is dealt: whoosh + soft flap + landing pop
    put(t - 0.05, whoosh(0.45, 2200, 600, 1.3, 0.35), W * 0.5); put(t + 0.32, flap(), 0.06); put(t + 0.36, pop(420, 260, 0.09), 0.1)
def copyclick(t):                                      # cursor click on Salin + "Tersalin" chime
    put(t - 0.04, tick(0.03, 2100), 0.22); put(t + 0.06, chime((1568, 2093), 0.6), 0.05)
def fold(t):                                           # card folds into the strip
    put(t, whoosh(0.35, 1600, 500, 1.3, 0.35), W * 0.45); put(t + 0.42, pop(700, 1000, 0.06), 0.08)
# --- s01 hook: bookmark pressed, deck spreads, PROMPT labels, header pills, flow line, stamp
put(0.02, pop(500, 760, 0.08), 0.07)
tS = wt("Simpan"); put(tS - 0.06, tick(0.03, 2000), 0.2); put(tS + 0.04, pop(900, 1400, 0.07), 0.12); put(wt("dulu:") - 0.04, chime((1318.5, 1760), 0.6), 0.05)
tT = wt("tiga"); put(tT - 0.2, whoosh(0.5, 500, 2000, 1.2, 0.45), W * 0.5)
for i in range(3): put(tT + 0.3 + i * 0.12, pop(500 + 140 * i, 900 + 140 * i, 0.07), 0.11)
for i in range(3): put(wt("prompt") - 0.05 + i * 0.06, tick(0.02, 3200 + 200 * i), 0.06)
put(wt("ngedit") - 0.12, pop(700, 1100, 0.07), 0.11); put(wt("Claude") - 0.14, pop(800, 1250, 0.07), 0.11); put(wt("Code.") - 0.02, bell(0.6), 0.04)
put(wt("Ini") - 0.05, rise(0.6, 400, 1200), 0.025)
for i in range(3): put(wt("Ini") + i * 0.16, tick(0.02, 2600 + 300 * i), 0.07)
tAk = wt("aku", st("s01")); put(tAk + 0.1, boom(0.35, 160, 70), 0.16); put(tAk + 0.14, pop(600, 300, 0.09), 0.1)
# (scene hand-overs: the outgoing scene fades UNDER the next card after the cut, so the card's own deal whoosh covers it)
# --- s02 prompt 1: card, copy, fold, folder hub, five installs, ready
deal(st("s02") + 0.02)
copyclick(L("alat.", "s02") + 0.12)
fold(L("folder,", "s02") - 0.42)
tF = L("folder,", "s02"); put(tF - 0.08, pop(450, 800, 0.09), 0.13)
for k in range(3): put(tF + 0.24 + k * 0.1, pop(900 + 120 * k, 1300 + 120 * k, 0.05), 0.07)
for i in range(5): put(L("pasang", "s02") - 0.08 + i * 0.08, tick(0.02, 2400 + 150 * i), 0.06)
put(L("lima", "s02") - 0.02, pop(800, 1200, 0.06), 0.08)
for txt in ["yt-dlp", "Whisper", "FFmpeg", "HyperFrames", "Remotion"]:
    t = L(txt, "s02"); put(t - 0.14, pop(600, 1000, 0.08), 0.12); put(t - 0.08, whoosh(0.3, 900, 2400, 1.5, 0.35), W * 0.2)
    for k in range(3): put(t + 0.05 + k * 0.08, tick(0.018, 3400 + 200 * k), 0.05)
    put(t + 0.42, chime((1568, 2093), 0.5), 0.04)
put(L("Remotion", "s02") + 0.3, pop(700, 1100, 0.06), 0.08)
put(L("animasi.", "s02") + 0.1, chime((1318.5, 1760, 2637), 0.9), 0.06); put(L("animasi.", "s02") + 0.12, pop(500, 900, 0.08), 0.1)
# --- s03 prompt 2: card, copy, fold, reels + hearts, console, scan, knobs, saved, veil, caution
deal(st("s03") + 0.02)
copyclick(L("selera.", "s03") + 0.14)
fold(L("favoritmu,", "s03") - 0.38)
tFv = L("favoritmu,", "s03")
for i in range(4): put(tFv - 0.12 + i * 0.08 + 0.3, pop(400 + 60 * i, 260, 0.08), 0.1); put(tFv + 0.32 + i * 0.09, pop(1100 + 80 * i, 1700 + 80 * i, 0.05), 0.08)
put(L("Claude", "s03") - 0.15, whoosh(0.45, 400, 1500, 1.2, 0.45), W * 0.35); put(L("Claude", "s03") + 0.15, pop(500, 800, 0.08), 0.1)
tC = L("catat", "s03"); put(tC - 0.05, rise(0.9, 500, 1800), 0.025)
for i in range(4): put(tC + 0.08 + i * 0.19, tick(0.02, 2800 + 200 * i), 0.07)
for txt in ["tempo,", "caption,", "warna,", "pembuka."]:
    t = L(txt, "s03") - 0.1; put(t, whoosh(0.3, 700, 2000, 1.6, 0.4), W * 0.18); put(t + 0.3, pop(900, 1300, 0.05), 0.08)
put(L("Ambil", "s03") - 0.04, chime((1568, 2093, 2637), 0.8), 0.05); put(L("Ambil", "s03") - 0.02, pop(700, 1100, 0.07), 0.1)
put(L("isinya,", "s03") - 0.12, pop(600, 950, 0.07), 0.1)
put(L("jangan", "s03") - 0.06, buzz(0.25), 0.035); put(L("jangan", "s03") - 0.04, pop(380, 200, 0.1), 0.12)
for k in range(3): put(L("upload", "s03") + 0.1 + k * 0.1, tick(0.02, 1500), 0.07)
# --- s04 prompt 3: card, copy, fold, raw file, rows, cuts, captions, selera, sticker, "?", voice, caption up, reply
deal(st("s04") + 0.02)
copyclick(L("edit.", "s04") + 0.12)
fold(L("Masukin", "s04") + 0.25)
tM = L("mentahmu,", "s04"); put(tM - 0.08, whoosh(0.4, 500, 1700, 1.2, 0.45), W * 0.35)
for k in range(6): put(tM + 0.2 + k * 0.07, tick(0.02, 2600 + 120 * k), 0.06)
tB = L("buang", "s04")
for j in range(3): put(tB - 0.15 + j * 0.12, scribble(0.18), 0.05); put(tB - 0.13 + j * 0.12, tick(0.025, 1800), 0.14)
put(L("jeda,", "s04") + 0.3, whoosh(0.35, 1800, 700, 1.4, 0.35), W * 0.3); put(L("jeda,", "s04") + 0.66, chime((1568, 2093), 0.5), 0.045)
put(L("jeda,", "s04") + 1.14, rise(0.5, 900, 400), 0.02)
put(L("pasang", "s04") + 0.02, pop(900, 1500, 0.06), 0.1); put(L("caption,", "s04") + 0.02, pop(1000, 1600, 0.06), 0.1)
put(L("sesuai", "s04") - 0.1, whoosh(0.4, 600, 2200, 1.4, 0.4), W * 0.35); put(L("selera", "s04") + 0.3, boom(0.3, 170, 80), 0.12); put(L("selera", "s04") + 0.32, bell(0.6), 0.04)
put(L("tadi.", "s04") - 0.1, pop(700, 1200, 0.07), 0.1)
put(L("Kurang", "s04") - 0.08, tick(0.025, 2400), 0.1); put(L("pas?", "s04") - 0.08, pop(1200, 1700, 0.06), 0.1)
put(L("Tinggal", "s04") - 0.1, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.3); put(L("kayak", "s04") - 0.05, pop(800, 1300, 0.07), 0.1)
for txt in ["caption-nya", "naikin", "dikit."]: put(L(txt, "s04") - 0.06, tick(0.02, 3000), 0.07)
put(L("naikin", "s04") + 0.05, rise(0.42, 500, 1400), 0.03); put(L("naikin", "s04") + 0.32, pop(900, 1400, 0.06), 0.1)
put(L("dikit.", "s04") - 0.04, chime((1568, 2093), 0.5), 0.045)
# --- s05 the three cards, stamps, next videos, card 3 loop
put(st("s05") + 0.0, whoosh(0.4, 600, 2000, 1.3, 0.4), W * 0.4)
for i in range(3): put(st("s05") + 0.2 + i * 0.07, pop(500 + 100 * i, 850 + 100 * i, 0.07), 0.09)
tSk = L("sekali.", "s05")
for i in range(2): put(tSk + 0.12 + i * 0.1, boom(0.25, 180, 80), 0.12); put(tSk + 0.14 + i * 0.1, tick(0.03, 1500), 0.12)
tV = L("Video", "s05")
for i in range(3): put(tV - 0.08 + i * 0.09, whoosh(0.25, 800, 2000, 1.6, 0.4), W * 0.18)
put(L("tinggal", "s05") - 0.1, rise(0.4, 400, 1000), 0.03)
tP = L("prompt", "s05")
for i in range(3): put(tP + 0.3 + i * 0.16, pop(1000 + 150 * i, 600, 0.06), 0.09)
put(L("tiga.", "s05") + 0.05, chime((1318.5, 1760, 2637), 0.8), 0.05)
# --- s06 CTA: pack, PROMPT keycaps, plane, DM chime, end
tMu = wt("Mau"); put(tMu - 0.08, whoosh(0.4, 1800, 600, 1.3, 0.35), W * 0.4); put(tMu + 0.36, boom(0.3, 160, 70), 0.12); put(tMu + 0.4, pop(600, 1000, 0.08), 0.1)
tK, tPR = wt("Komen"), wt("PROMPT,")
for i in range(6): put(tK - 0.3 + i * 0.035, pop(700 + 50 * i, 1000 + 50 * i, 0.05), 0.05)
for i in range(6): put(tK + 0.06 + i * ((tPR + 0.36 - tK) / 6), tick(0.03, 1700 + 120 * (i % 3)), 0.2)
put(tPR + 0.42, chime((1568, 2093, 2637), 0.8), 0.05)
tAk2 = wt("aku", st("s06")); put(tAk2 - 0.05, whoosh(0.35, 1600, 500, 1.3, 0.35), W * 0.4)
put(wt("kirim") - 0.2, whoosh(0.55, 700, 3600, 1.2, 0.45), W * 0.8)
put(wt("lewat") - 0.1, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.06, chime((1568, 2093), 0.8), 0.06)
put(T["total_sec"] - 1.1, chime((1046, 1568, 2093, 2637), 1.6), 0.06)
out *= 1.25   # +2 dB: ~12-13 LU under the VO, like the kit
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
