"""Synthesised SFX bed for R10 "Edit video yang sudah ada pakai AI (Runway Aleph)" (no samples, no downloads): player settle, REC
beep, prompt typing + send clicks, the before/after divider sweeps (airy whoosh + a sparkle per edit: night = low bell, sakura =
pentatonic chime, snow = icy high chime, car = soft thunk, product = glint), whip transitions between clips, the lamp flicker, step
cards, the "tanpa syuting ulang" strike, the note-card stamp and the CTA (AI typing, heart, plane, DM chime). Deterministic.
Writes assets/audio/sfx.wav. Run: python3 tools/sfx.py ."""
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
L = lambda i: S[i]["start"] + S[i]["dur"]
def whip_out(t): put(t - 0.11, whoosh(0.36, 900, 3400, 1.3, 0.55), W * 0.6)     # carousel slide (last 0.33 s of a clip)
def whip_in(t): put(t + 0.01, pop(520, 760, 0.06), 0.05)                       # the next clip lands
def send(t): put(t, tick(0.035, 1900), 0.24); put(t + 0.02, pop(520, 320, 0.08), 0.11)
def sweep(t, d=0.42): put(t, whoosh(d + 0.1, 500, 3200, 1.6, 0.55), W * 0.55); put(t + 0.05, rise(d, 600, 1800), 0.018)
def typed(t0, t1, g=0.1): typing(t0, t1, g, 22)
# --- s01 hook: settle, REC beep, prompt rises + types + send, sweep → snow, split back, ring + badge, whip
put(0.02, pop(500, 760, 0.08), 0.08)
tR = wt("rekam,"); put(tR - 0.06, square_blips([1320, 1320], 0.06), 0.03)
tS = wt("sekarang"); put(tS - 0.24, whoosh(0.36, 600, 2200, 1.3, 0.45), W * 0.45); put(tS + 0.1, pop(700, 1100, 0.07), 0.09)
tU = wt("ubah"); typed(tS + 0.18, tU - 0.14); send(tU - 0.1)
sweep(tU - 0.04); put(tU + 0.36, chime((2093, 2637, 3136, 4186), 1.0), 0.06)
put(wt("cuma") + 0.02, whoosh(0.4, 2400, 900, 1.3, 0.4), W * 0.3)
put(wt("satu") - 0.06, pop(900, 1400, 0.07), 0.12); put(wt("kalimat.") - 0.04, chime((1568, 2093), 0.6), 0.05)
whip_out(L("s01") - 0.22)
# --- s02 night: whip in, typing, send, sweep, night bell, lamp flicker, split back, "ketik" pulse, whip out
whip_in(st("s02")); tM = wt("malam?")
typed(wt("Mau") - 0.06, tM - 0.32); send(tM - 0.28)
sweep(tM - 0.24); put(tM - 0.02, boom(0.6, 90, 45), 0.12); put(tM + 0.12, chime((784, 1046, 1318), 1.2), 0.05)
for k, dt in enumerate([0, 0.06, 0.12, 0.18, 0.24]): put(tM + 0.42 + dt, tick(0.02, 2600 - 200 * k), 0.12 if k % 2 == 0 else 0.05)
put(tM + 0.44, buzz(0.3), 0.012)
put(wt("Tinggal") - 0.06, whoosh(0.4, 2400, 900, 1.3, 0.4), W * 0.3)
put(wt("ketik.") - 0.06, pop(900, 1400, 0.07), 0.11)
whip_out(L("s02") - 0.22)
# --- s03 seasons: whip in, chip, typing 1, send, sweep → sakura chime, retype, send, sweep → snow chime, whip out
whip_in(st("s03")); put(wt("musim?") - 0.1, pop(800, 1200, 0.06), 0.09); put(wt("panas,") - 0.06, pop(1000, 1500, 0.05), 0.08)
tK = wt("sakura,"); typed(wt("Dari") - 0.02, tK - 0.42); send(tK - 0.36)
sweep(tK - 0.26, 0.44); put(tK + 0.1, chime((1175, 1397, 1760, 2349), 1.1), 0.065)
tA, tJ = wt("atau"), wt("salju.")
for k in range(4): put(tA - 0.5 + k * 0.02, tick(0.015, 2200), 0.05)
typed(tA - 0.42, tJ - 0.3); send(tJ - 0.26)
sweep(tJ - 0.2, 0.44); put(tJ + 0.12, chime((2637, 3136, 3951, 5274), 1.2), 0.05); put(tJ - 0.1, whoosh(0.9, 300, 900, 0.8, 0.5), W * 0.25)
whip_out(L("s03") - 0.22)
# --- s04 car: whip in, marquee, typing, send, sweep, thunk + sparkle, whip out
whip_in(st("s04")); put(wt("kosong,") - 0.12, pop(700, 1100, 0.07), 0.1)
for k in range(3): put(wt("kosong,") + k * 0.08, tick(0.02, 3000), 0.04)
tB = wt("mobil."); typed(wt("kosong,") + 0.12, wt("bisa", st("s04")) + 0.16); send(tB - 0.56)
sweep(tB - 0.48, 0.44); put(tB - 0.01, boom(0.35, 140, 60), 0.2); put(tB + 0.02, pop(300, 150, 0.1), 0.1); put(tB + 0.04, chime((2093, 2637, 3136), 0.7), 0.05)
whip_out(L("s04") - 0.22)
# --- s05 product: whip in, marquees, typing, send, sweep, glint, player sinks
whip_in(st("s05")); put(wt("polos,") - 0.1, pop(700, 1100, 0.07), 0.1)
tP = wt("produk"); tBi = wt("bisa", st("s05"))
typed(wt("polos,") + 0.12, tBi + 0.04); send(tBi + 0.08)
sweep(tBi + 0.14, 0.44); put(tP - 0.04, chime((1568, 2093, 2637, 3136), 0.9), 0.06); put(tP - 0.02, pop(1200, 1900, 0.05), 0.08)
put(L("s05") - 0.3, whoosh(0.4, 1800, 400, 1.2, 0.5), W * 0.5)
# --- s06 how it works
s6 = st("s06")
put(wt("Namanya") - 0.2, whoosh(0.42, 500, 1800, 1.2, 0.45), W * 0.45); put(wt("Namanya") + 0.1, pop(600, 900, 0.08), 0.1)
put(wt("Aleph.") - 0.04, pop(1100, 1700, 0.06), 0.1); put(wt("Aleph.") + 0.02, chime((1318.5, 1760, 2637), 0.8), 0.05)
tKm, tKs, tVd = wt("Kamu"), wt("kasih"), wt("videonya,")
put(tKm - 0.2, whoosh(0.36, 600, 2000, 1.3, 0.4), W * 0.35); put(tKs - 0.12, pop(400, 700, 0.09), 0.12)
put(tKs, rise(tVd + 0.3 - tKs, 500, 1500), 0.02); put(tVd + 0.3, chime((1568, 2093), 0.6), 0.05); put(tVd + 0.4, tick(0.025, 2600), 0.1)
tT, tAp = wt("tulis"), wt("apa,")
put(tT - 0.32, whoosh(0.36, 600, 2000, 1.3, 0.4), W * 0.35); typed(tT, tAp - 0.2, 0.09); send(tAp - 0.12)
put(tAp - 0.08, tick(0.025, 2600), 0.1); put(tAp - 0.06, whoosh(0.36, 600, 2000, 1.3, 0.4), W * 0.35)
put(tAp + 0.3, whoosh(0.5, 500, 2800, 1.6, 0.5), W * 0.35); put(tAp + 0.7, chime((1568, 2093, 2637), 0.7), 0.05)
for k in range(2): put(wt("lainnya") - 0.1 + k * 0.08, pop(900 + 200 * k, 1400 + 200 * k, 0.06), 0.1)
for t in (wt("dibiarin"), wt("kayak", s6), wt("aslinya.")): put(t - 0.14, pop(700, 1200, 0.07), 0.11); put(t - 0.1, tick(0.02, 3200), 0.06)
put(L("s06") - 0.3, whoosh(0.4, 1800, 500, 1.2, 0.5), W * 0.45)
# --- s07 use cases
put(st("s07") + 0.04, whoosh(0.42, 500, 1800, 1.2, 0.45), W * 0.4); put(st("s07") + 0.3, pop(600, 900, 0.08), 0.08)
for t in (wt("konten"), wt("marketing:")): put(t - 0.1, pop(800, 1300, 0.07), 0.12)
put(wt("satu", st("s07")) - 0.12, pop(600, 1000, 0.07), 0.1); put(wt("video,", st("s07")) - 0.04, tick(0.025, 2400), 0.1)
tBn = wt("banyak")
put(tBn - 0.16, whoosh(0.5, 2400, 700, 1.3, 0.45), W * 0.45)
for k in range(4): put(tBn - 0.06 + k * 0.1 + 0.2, pop(700 + 120 * k, 1100 + 120 * k, 0.06), 0.1)
for k in range(4): put(wt("versi,") - 0.04 + k * 0.06, tick(0.02, 2800 + 200 * k), 0.06)
put(wt("tanpa") - 0.14, whoosh(0.4, 600, 2000, 1.3, 0.4), W * 0.35)
tUl = wt("ulang."); put(tUl - 0.12, rip(0.3), 0.06); put(tUl - 0.02, boom(0.35, 160, 70), 0.14)
put(L("s07") - 0.3, whoosh(0.4, 1800, 500, 1.2, 0.5), W * 0.45)
# --- s08 note
put(st("s08") + 0.02, whoosh(0.42, 500, 1600, 1.2, 0.45), W * 0.4); put(wt("Catatan:") + 0.05, pop(500, 800, 0.09), 0.1)
put(wt("fitur") - 0.12, tick(0.025, 2400), 0.07); put(wt("paket") - 0.14, tick(0.025, 2400), 0.07)
tBr = wt("berbayar"); put(tBr - 0.08, scribble(0.32), 0.05); put(tBr + 0.2, boom(0.35, 170, 70), 0.18); put(tBr + 0.21, pop(300, 140, 0.1), 0.1)
for k in range(3): put(tBr + 0.24 + k * 0.2, pop(900 + 100 * k, 1300 + 100 * k, 0.05), 0.07)
put(L("s08") - 0.28, whoosh(0.4, 1800, 500, 1.2, 0.5), W * 0.45)
# --- s09 CTA
s9 = st("s09")
put(s9 + 0.02, pop(700, 1200, 0.08), 0.12); put(s9 + 0.04, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5)
tAI = wt("AI,")
for k in range(2): put(tAI - 0.1 + k * 0.16, tick(0.022, 4200), 0.16)
put(tAI + 0.12, pop(900, 1600, 0.1), 0.15)
tAk = wt("aku", s9); put(tAk - 0.01, tick(0.03, 2000), 0.2); put(tAk + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("kirim", s9) + 0.22, pop(600, 1000, 0.07), 0.08)
tD = wt("pakainya."); put(tD - 0.12, pop(800, 1300, 0.07), 0.1); put(tD + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
