"""Synthesised SFX bed for R18 (gladi resik reels sebelum posting / Virality Predictor) — no samples, no downloads: posting click +
denied buzz, curtain whoosh + valance flap, GLADI RESIK stamp, seat pops + sparkle ticks, name wipe, terminal typing + installed chime,
strip ticks, clip drop, scan rises, sensor pops, rapor counter ticks, peak chime, crowd pops + "kabur" whoosh, KELAMAAN stamp, editor
grab / move / snip / fall, re-test click, A/B scans + coins + unlock, BUKAN JAMINAN stamp, audience pops, CTA (VIRAL typing, plane,
DM chime), end chime. Deterministic. Writes assets/audio/sfx.wav. Run: python3 tools/sfx.py ."""
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
def out_(sid):
    put(st(sid) - 0.26, whoosh(0.32, 1800, 600, 1.3, 0.35), W * 0.4)
def card_in(t, g=1.0):
    put(t, whoosh(0.38, 450, 1600, 1.2, 0.45), W * 0.4 * g); put(t + 0.24, pop(420, 760, 0.09), 0.1 * g)
def stamp(t):   # t = moment the stamp lands
    put(t - 0.17, whoosh(0.2, 2400, 800, 1.4, 0.3), W * 0.3); put(t, boom(0.35, 170, 70), 0.2); put(t, pop(320, 160, 0.1), 0.12)
def click(t, g=1.0): put(t, tick(0.03, 2000), 0.18 * g); put(t + 0.01, pop(1400, 900, 0.04), 0.05 * g)
# --- s01 hook: draft reel + Posting, click, denied (lock), curtains + valance, GLADI RESIK stamp, seats + AI viewers, sparkles
put(0.02, pop(500, 760, 0.08), 0.08)
tS = wt("Sebelum"); click(tS + 0.06)
tP = wt("posting,"); put(tP - 0.12, buzz(0.22), 0.035); put(tP - 0.1, tick(0.025, 1500), 0.12)
tR = wt("reels"); put(tR - 0.05, whoosh(0.5, 300, 1500, 1.0, 0.4), W * 0.7); put(tR + 0.05, rumble(0.6), 0.05); put(tR + 0.3, flap(), 0.07)
stamp(wt("gladi resik") + 0.05)
tD = wt("depan")
for i in range(6): put(tD - 0.06 + i * 0.06, pop(560 + 70 * i, 900 + 70 * i, 0.07), 0.09)
tA = wt("AI.")
for i in range(6): put(tA - 0.08 + i * 0.045, tick(0.02, 4600 + 150 * i), 0.07)
put(tA + 0.05, chime((2093, 2637), 0.6), 0.03)
out_("s02")
# --- s02 plugin card: name wipe, repo + MIT, terminal unfolds, plug clicks, two commands type, installed chime, chips
s2 = st("s02"); card_in(s2)
put(wt("Virality") - 0.08, whoosh(0.4, 900, 2600, 1.5, 0.4), W * 0.35)
tH = wt("Higgsfield,"); put(tH - 0.1, tick(0.025, 2600), 0.08); put(tH + 0.12, pop(800, 1300, 0.07), 0.1); put(tH + 0.2, whoosh(0.35, 400, 1300, 1.2, 0.45), W * 0.35)
tPl = wt("plugin"); put(tPl - 0.08, pop(500, 900, 0.09), 0.12); put(tPl + 0.26, zap(0.25), 0.03)
tG = wt("gratis."); typing(tPl + 0.05, tG - 0.2, 0.08)
put(tG - 0.16, chime((1318.5, 1760, 2349), 0.7), 0.05); put(tG - 0.06, pop(700, 1100, 0.07), 0.1); put(tG + 0.12, pop(800, 1250, 0.07), 0.09)
out_("s03")
# --- s03 15-second clip: strip + frames, bracket, MAKS chip, clip chip drops, viewer, scan rings, four sensor rows
s3 = st("s03"); card_in(s3, 0.8)
for i in range(9): put(s3 + 0.05 + i * 0.035, tick(0.018, 2400 + 120 * i), 0.05)
put(wt("maksimal") - 0.05, whoosh(0.35, 700, 2200, 1.4, 0.4), W * 0.35); put(wt("maksimal") + 0.05, pop(800, 1300, 0.07), 0.09)
put(wt("15") + 0.05, tick(0.03, 2200), 0.12)
tAI = wt("AI-nya"); card_in(tAI - 0.35, 0.8); put(tAI - 0.22, whoosh(0.45, 1400, 500, 1.2, 0.4), W * 0.4); put(tAI + 0.42, pop(500, 900, 0.09), 0.11)
put(wt("memprediksi"), rise(0.9, 400, 1100), 0.025); put(wt("penonton:") + 0.1, rise(0.9, 450, 1200), 0.02)
for k, w_ in enumerate(["visual,", "suara,", "bahasa,", "fokus."]):
    t = wt(w_, s3) - 0.1; put(t, pop(700 + 120 * k, 1100 + 120 * k, 0.07), 0.11); put(t + 0.05, tick(0.02, 3000 + 200 * k), 0.06)
put(wt("fokus.") + 0.1, chime((1568, 2093), 0.6), 0.04)
out_("s04")
# --- s04 rapor: ring fills + counts, 15 cells, peak ring, hold bar, crowd, betah / kabur
s4 = st("s04"); card_in(s4)
tSk = wt("skor"); put(tSk - 0.15, rise(0.85, 300, 1100), 0.03)
for k in range(7): put(tSk - 0.15 + 0.9 * (1 - (1 - (k + 1) / 7) ** 2) * 0.9, tick(0.02, 3200), 0.06)
tPu = wt("puncak")
for i in range(15): put(tPu - 0.1 + i * 0.04, tick(0.015, 2000 + 90 * i), 0.04)
tHk = wt("hook,"); put(tHk - 0.16, pop(900, 1500, 0.08), 0.12); put(tHk - 0.1, chime((1760, 2349), 0.5), 0.04)
put(wt("hold") - 0.05, rise(0.7, 350, 900), 0.025)
for i in range(8): put(wt("rate:") - 0.1 + i * 0.04, pop(650 + 40 * i, 1000 + 40 * i, 0.05), 0.06)
put(wt("betah") - 0.08, chime((1318.5, 1760), 0.5), 0.04)
put(wt("kabur.") - 0.06, whoosh(0.4, 1600, 500, 1.3, 0.4), W * 0.5)
out_("s05")
# --- s05 15 bars: bars grow, PUNCAK flag + "?", amber bracket, scroll-away arrows, KELAMAAN stamp
s5 = st("s05"); card_in(s5, 0.8)
for i in range(15): put(wt("Puncak", s5 - 0.1) - 0.1 + i * 0.045, tick(0.015, 1800 + 100 * i), 0.04)
tK = wt("kelima?"); put(tK - 0.14, pop(900, 1500, 0.08), 0.12); put(tK + 0.06, pop(500, 1200, 0.1), 0.13)
put(wt("intro") - 0.12, whoosh(0.35, 600, 1800, 1.3, 0.4), W * 0.35); put(wt("intro") + 0.05, pop(600, 1000, 0.07), 0.09)
tL = wt("kelamaan."); put(tL - 0.2, whoosh(0.4, 500, 2200, 1.4, 0.4), W * 0.3); stamp(tL + 0.11)
out_("s06")
# --- s06 editor: grab, move, tag, scissors snip, intro falls, gap closes, Tes ulang click + refresh, result chime
s6 = st("s06"); card_in(s6, 0.8)
for i in range(4): put(s6 + 0.08 + i * 0.06, pop(600 + 60 * i, 950 + 60 * i, 0.06), 0.07)
tT = wt("terkuat"); click(tT - 0.08); put(tT - 0.05, pop(500, 800, 0.08), 0.08)
tKe = wt("ke", s6); put(tKe - 0.05, whoosh(0.5, 500, 1600, 1.2, 0.45), W * 0.5)
tPe = wt("pertama,"); put(tPe + 0.12, tick(0.03, 1500), 0.14); put(tPe + 0.2, pop(800, 1300, 0.07), 0.1)
tB = wt("buang"); put(tB, pop(700, 1000, 0.07), 0.08)
tBt = wt("bertele-tele,"); put(tBt - 0.2, rip(0.3), 0.06); put(tBt, tick(0.03, 3200), 0.12); put(tBt + 0.12, whoosh(0.35, 1500, 400, 1.2, 0.4), W * 0.45)
put(tBt + 0.34, whoosh(0.3, 700, 1800, 1.3, 0.4), W * 0.3)
tTs = wt("tes", s6); click(tTs - 0.04); put(tTs, whoosh(0.45, 600, 2400, 1.4, 0.4), W * 0.35)
put(wt("ulang.") + 0.04, chime((1568, 2093, 2637), 0.7), 0.05)
out_("s07")
# --- s07 UMKM: header, two reels, boost card, scans, scores, winner check, coins + lock, unlock
s7 = st("s07"); card_in(s7, 0.8)
tU = wt("UMKM,"); put(tU - 0.1, pop(600, 950, 0.07), 0.09); put(tU + 0.02, pop(700, 1050, 0.07), 0.09); put(tU + 0.2, pop(450, 800, 0.09), 0.1)
tTe = wt("tes", s7); put(tTe - 0.05, rise(0.55, 500, 1400), 0.025); put(tTe + 0.03, rise(0.55, 520, 1450), 0.02)
tJ = wt("jualan"); put(tJ + 0.02, pop(700, 1100, 0.07), 0.09); put(tJ + 0.12, pop(800, 1250, 0.07), 0.09)
tDu = wt("dulu", s7); put(tDu - 0.02, chime((1318.5, 1760, 2349), 0.6), 0.05)
tKl = wt("keluar")
for i in range(3):
    for k in range(3): put(tKl - 0.05 + i * 0.05 + k * 0.1, tick(0.02, 5200 + 300 * k), 0.05)
put(wt("sebelum", s7) + 0.05, tick(0.025, 1400), 0.1); put(wt("duit") - 0.05, tick(0.025, 1400), 0.1)
tI = wt("iklan."); put(tI - 0.06, tick(0.03, 2600), 0.14); put(tI - 0.04, chime((1568, 2093), 0.6), 0.05); put(tI + 0.05, pop(600, 1000, 0.08), 0.08)
out_("s08")
# --- s08 forecast card, BUKAN JAMINAN stamp, real audience, insight bars, check
s8 = st("s08"); card_in(s8)
put(s8 + 0.3, whoosh(0.6, 300, 900, 1.0, 0.5), W * 0.25)
stamp(wt("jaminan.") + 0.09)
tPn = wt("Penonton", s8); card_in(tPn - 0.25, 0.8)
for i in range(7): put(tPn - 0.05 + i * 0.05, pop(600 + 50 * i, 950 + 50 * i, 0.06), 0.07)
for i in range(4): put(wt("asli", s8) - 0.05 + i * 0.08, tick(0.02, 2600 + 200 * i), 0.06)
put(wt("penentunya.") + 0.02, chime((1318.5, 1760, 2349), 0.8), 0.05)
out_("s09")
# --- s09 CTA: package card, comment "VIRAL", heart, send, plane, DM chime, end logo
s9 = st("s09")
put(s9 + 0.0, pop(500, 900, 0.09), 0.12); put(s9 + 0.02, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5)
tV = wt("VIRAL,"); ta = max(s9 + 0.2, tV - 0.1)
for k in range(5): put(ta + k * 0.09, tick(0.022, 4200), 0.16)
put(ta + 0.48, pop(900, 1600, 0.1), 0.15)
put(wt("aku", s9) - 0.01, tick(0.03, 2000), 0.2); put(wt("aku", s9) + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("DM.") - 0.12, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
