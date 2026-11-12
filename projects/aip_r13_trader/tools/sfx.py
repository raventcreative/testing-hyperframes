"""Synthesised SFX bed for the R9 YOUTUBE reel (adapted from the R3 DESAINER bed) (no samples, no downloads): job chips piling up,
Claude flare + 11 tiles dealt, repo header + tiles sucked in + check stamps, header flaps, hook typing + formula reel + score bars,
title/thumbnail pop + link, strike/cut ticks, comment sort, week board, radar + result sort, terminal paste/typing, the CTA. Deterministic.
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

def wt2(txt, after=0.0):
    v = wt(txt, after)
    if v is None: raise SystemExit("word not found " + txt)
    return v
wt_ = wt2
# --- s01 hook: creator + 7 job chips, shake, collapse, Claude disc, 11 tiles, glow run
put(0.02, rise(0.6, 300, 1200), 0.05); put(0.05, pop(500, 900, 0.08), 0.1)
for k in range(7): put(wt_("Ngurus") - 0.1 + k * 0.16, pop(700 + 70 * k, 1100 + 70 * k, 0.07), 0.1)
put(wt_("sendirian?") + 0.02, buzz(0.3), 0.05); put(wt_("sendirian?") + 0.05, boom(0.35, 150, 70), 0.18)
put(wt_("Sebelas") - 0.3, whoosh(0.35, 2400, 500, 1.4, 0.4), W * 0.7)
for k in range(11): put(wt_("Sebelas") + 0.04 + k * 0.07, tick(0.018, 2400 + 90 * k), 0.07)
put(wt_("Claude") - 0.1, chime((1046, 1318, 1568), 1.1), 0.07); put(wt_("Claude") + 0.02, pop(900, 500, 0.1), 0.1)
put(wt_("gratis") - 0.04, pop(800, 1300, 0.08), 0.13); put(wt_("gratis") + 0.18, pop(900, 1400, 0.07), 0.1)
put(wt_("naskah") - 0.06, chime((1568, 2093), 0.5), 0.05)
for k in range(4): put(wt_("sampai") - 0.1 + k * 0.1, tick(0.016, 3000 + 200 * k), 0.06)
put(wt_("viral.") - 0.08, chime((1318.5, 1760, 2637), 0.9), 0.06); put(wt_("viral.") - 0.06, pop(600, 1200, 0.09), 0.1)
# --- s02 the pack: header drop, tiles sucked into the folder, 11 badge, three check stamps, key strike
put(wt_("Namanya") - 0.1, whoosh(0.45, 2400, 600, 1.4, 0.45), W * 0.6); put(wt_("Namanya") + 0.4, flap(), 0.1)
put(wt_("YouTube", 6) - 0.1, whoosh(0.7, 600, 3000, 1.3, 0.5), W * 0.5)
for k in range(11): put(wt_("YouTube", 6) + 0.25 + k * 0.05, tick(0.014, 3600 - 60 * k), 0.05)
put(wt_("Skill:") + 0.12, pop(500, 1000, 0.09), 0.14)
for w, a in (("open", 8), ("daftar,", 9), ("key.", 10)): put(wt_(w, a) + (0.32 if w == "open" else (0.1 if w == "daftar," else -0.02)), boom(0.25, 180, 80), 0.16)
for w, a in (("open", 8), ("tanpa", 9), ("tanpa", 9.5)): put(wt_(w, a) - 0.12, whoosh(0.3, 700, 2000, 1.4, 0.3), W * 0.4)
put(wt_("API") + 0.02, scribble(0.2), 0.06)
put(st("t1") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- t1 /yt-script: flap, hook card, typing, reel spin + stop, score bars, verdict stamp, REC
put(st("t1") + 0.02, flap(), 0.12)
put(wt_("naskah", 11) - 0.2, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
typing(wt_("naskah", 11) + 0.1, wt_("naskah", 11) + 1.75, 0.08, 18)
for k in range(16): put(wt_("21") - 0.05 + 0.04 * k * (1 + k * 0.06), tick(0.016, 2600), 0.07)
put(wt_("hook,") + 0.02, pop(700, 1200, 0.08), 0.14); put(wt_("hook,") + 0.12, chime((1568, 2093), 0.5), 0.04)
for k in range(5): put(wt_("skor") - 0.05 + k * 0.07, rise(0.25, 500 + 80 * k, 1100 + 80 * k), 0.025)
put(wt_("hook-nya") - 0.02, boom(0.3, 170, 80), 0.18); put(wt_("hook-nya"), pop(300, 140, 0.12), 0.15)
put(wt_("rekaman.") - 0.08, square_blips([880, 1320]), 0.05)
put(st("t2") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- t2 /yt-package: flap, title pop + typing, thumbnail pop, link, outline, lint ticks
put(st("t2") + 0.02, flap(), 0.12)
put(wt_("judul") - 0.2, pop(600, 1000, 0.08), 0.12); typing(wt_("judul") - 0.02, wt_("judul") + 0.62, 0.07, 22)
put(wt_("thumbnail") - 0.16, pop(500, 900, 0.09), 0.14); put(wt_("thumbnail") + 0.06, boom(0.22, 220, 110), 0.1)
put(wt_("ditulis") - 0.06, chime((1318.5, 1760), 0.6), 0.05); put(wt_("ditulis") + 0.2, tick(0.03, 1800), 0.12)
for k in range(3): put(wt_("sepasang.") + 0.1 + k * 0.1, pop(900 + 120 * k, 1500 + 120 * k, 0.05), 0.08)
put(st("t3") - 0.2, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- t3 /yt-edit: flap, transcript slide, 3 strikes (scissor snips), cut list, timecode run
put(st("t3") + 0.02, flap(), 0.12)
put(wt_("transkrip") - 0.24, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
for k in range(5): put(wt_("transkrip") - 0.06 + k * 0.06, tick(0.014, 3200), 0.05)
for k in range(3): put(wt_("daftar", 20) + k * 0.22, rip(0.18), 0.05); put(wt_("daftar", 20) + k * 0.22 + 0.04, tick(0.03, 1500), 0.12)
for k in range(3): put(wt_("edit,") - 0.1 + k * 0.12, pop(700 + 100 * k, 1200 + 100 * k, 0.06), 0.09)
for k in range(8): put(wt_("timecode.") - 0.14 + k * 0.07, tick(0.014, 4200), 0.06)
put(st("t4") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- t4 /yt-comment: flap, comments cascade, sort whoosh, pin, reply typing
put(st("t4") + 0.02, flap(), 0.12)
for k in range(6): put(wt_("komentar") - 0.2 + k * 0.06, pop(800 + 60 * k, 1300 + 60 * k, 0.05), 0.08)
put(wt_("dipilah,") - 0.06, whoosh(0.5, 600, 2400, 1.3, 0.45), W * 0.6)
for k in range(4): put(wt_("dipilah,") + k * 0.07, tick(0.02, 2400 + 200 * k), 0.07)
put(wt_("lalu", 24) + 0.12, pop(500, 900, 0.09), 0.12)
typing(wt_("dibalas") + 0.06, wt_("dibalas") + 1.4, 0.08, 20); put(wt_("gaya") - 0.04, chime((1568, 2093), 0.5), 0.04)
put(st("t5") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- t5 /yt-plan: flap, board rise, 5 cards drop, hours bar fill, "muat"
put(st("t5") + 0.02, flap(), 0.12)
put(wt_("rencana") - 0.2, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
for k in range(5): put((wt_("upload") - 0.08 if k == 0 else wt_("seminggu") - 0.04 + (k - 1) * 0.09) + 0.2, pop(300 + 40 * k, 160, 0.08), 0.13)
put(wt_("waktu") - 0.2, rise(0.6, 400, 1300), 0.04); put(wt_("kamu.", 28.5) - 0.1, chime((1318.5, 1760, 2637), 0.8), 0.05)
put(st("s07") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s07 /yt-viral: flap, ribbon + sparkles, panel, radar pings, typing, results, bars, re-sort, formula chips
put(st("s07") + 0.02, flap(), 0.12)
put(wt_("seru,") - 0.12, chime((1318.5, 1760, 2637), 1.0), 0.07)
for k in range(6): put(wt_("Paling") + 0.1 + k * 0.08, pop(1200 + 80 * k, 1800 + 80 * k, 0.04), 0.06)
put(wt_("mesin") - 0.18, whoosh(0.5, 400, 1800, 1.2, 0.5), W * 0.6); put(wt_("mesin"), rumble(1.4), 0.03)
for k in range(3): put(wt_("viral:") + 0.2 + k * 0.42, chime((2093,), 0.4), 0.035)
typing(wt_("cari") - 0.04, wt_("cari") + 0.62, 0.08, 22)
for k in range(4): put(wt_("niche") + 0.2 + k * 0.08, pop(600 + 60 * k, 1000 + 60 * k, 0.06), 0.09)
for k in range(4): put(wt_("ngalahin") - 0.05 + k * 0.09, rise(0.5, 400 + 60 * k, 1500 + 60 * k), 0.03)
put(wt_("rata-rata") - 0.04, pop(700, 1200, 0.08), 0.1)
put(wt_("channel-nya") - 0.04, whoosh(0.5, 900, 2600, 1.4, 0.4), W * 0.5); put(wt_("sendiri,"), chime((1568, 2093), 0.6), 0.05)
for k in range(4): put(wt_("rumus", 35) - 0.08 + k * 0.1, pop(900 + 100 * k, 1500 + 100 * k, 0.05), 0.08)
put(st("s08") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s08 setup: flap, terminal open, paste, typing, install blips, command + enter
put(st("s08") + 0.02, flap(), 0.12)
put(wt_("buka") - 0.12, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5); put(wt_("Code,") - 0.1, square_blips([660, 990]), 0.04)
put(wt_("link") - 0.08, tick(0.04, 1600), 0.2); put(wt_("tempel"), pop(800, 1300, 0.07), 0.1)
typing(wt_("minta") - 0.04, wt_("minta") + 0.72, 0.08, 22)
put(wt_("install,") + 0.04, square_blips([880, 1100, 1320]), 0.04); put(wt_("terus", 40) - 0.02, chime((1568, 2093), 0.5), 0.05)
typing(wt_("ketik") + 0.02, wt_("ketik") + 0.47, 0.09, 22); put(wt_("/yt-script.") + 0.12, tick(0.04, 1500), 0.2)
put(wt_("/yt-script.") + 0.16, chime((1318.5, 1760, 2637), 0.8), 0.06)
put(st("s09") - 0.42, whoosh(0.4, 2400, 700, 1.4, 0.4), W * 0.5); put(st("s09") - 0.3, pop(600, 1000, 0.08), 0.1)
# --- s09 CTA
put(wt_("Komen") - 0.06, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(7): put(wt_("YOUTUBE,") - 0.08 + k * 0.055, tick(0.022, 4200), 0.15)
put(wt_("YOUTUBE,") + 0.44, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", 43) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("kirim") - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

