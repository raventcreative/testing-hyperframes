"""Synthesised SFX bed for the R28 SISTEM reel (bangun 5 sistem bisnis; helpers from the R25/R19 bed) (no samples, no downloads):
spinning-list ticks, X stamps, chip bursts, tile pops, per-system flaps + checks, chat pops, card deals, transaction whooshes, CV drops,
truck rumble, gears, chart rises, CTA typing + send. Deterministic.
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
def snip():
    x = np.zeros(int(0.09 * SR)); a = tick(0.03, 2300); b2 = tick(0.025, 3400)
    x[: len(a)] += a; i = int(0.045 * SR); x[i:i + len(b2)] += 0.8 * b2
    return x / np.abs(x).max()
D = {k: st(k) for k in S}; TOT = T["total_sec"]
# --- s01 hook: the list is already spinning (fast ticks that slow down), energy drains, "kurang kerja keras?" + X stamp, lock,
#     card collapses into the KAMU node, 8 chips burst out, warning rings
tS = wt_("Semuanya")
tt, k = 0.03, 0
while tt < tS:
    put(tt, tick(0.015, 2600 + 300 * (k % 3)), 0.035); k += 1
    u = tt / tS; tt += 0.045 + 0.30 * u ** 3
put(wt_("capek") - 0.06, rise(0.6, 1200, 300), 0.03)
put(wt_("kurang") - 0.2, pop(600, 1000, 0.08), 0.09)
put(wt_("keras.") - 0.04, boom(0.22, 200, 90), 0.14); put(wt_("keras.") - 0.02, buzz(0.16), 0.025)
put(tS + 0.03, pop(500, 1000, 0.09), 0.13); put(tS + 0.05, chime((1046, 1318.5), 0.5), 0.03)
put(wt_("nyangkut") - 0.2, whoosh(0.4, 1800, 500, 1.4, 0.45), W * 0.45)
for i in range(8): put(wt_("nyangkut") + 0.12 + i * 0.035, pop(700 + 60 * i, 1000 + 60 * i, 0.05), 0.07)
put(wt_("kamu.") - 0.05, buzz(0.3), 0.03); put(wt_("kamu.") - 0.05, boom(0.3, 150, 70), 0.1)
# --- s02: chips swept, clock chip + X, node -> dot, five tiles spring up, headline
put(D["s02"] + 0.04, whoosh(0.45, 600, 2200, 1.3, 0.45), W * 0.45)
put(wt_("tambah") - 0.2, pop(600, 1000, 0.08), 0.09)
for i in range(8): put(wt_("tambah") - 0.15 + i * 0.11, tick(0.02, 3000), 0.05)
put(wt_("kerja,") - 0.04, boom(0.22, 200, 90), 0.14); put(wt_("kerja,") - 0.02, buzz(0.16), 0.025)
put(wt_("tapi") + 0.02, rise(0.4, 1400, 500), 0.03)
for i in range(5): put(wt_("lima") - 0.2 + i * 0.11, pop(620 + 110 * i, 900 + 140 * i, 0.06), 0.1)
put(wt_("sistem.") - 0.06, chime((1046, 1318.5, 1568), 0.8), 0.045)
put(D["s03"] - 0.38, whoosh(0.35, 1800, 600, 1.4, 0.4), W * 0.3)
# --- s03 the five systems: tile highlight per system, a check + chime on each system's last word
for wd, end in (("Satu,", "otomatis."), ("Dua,", "setujui."), ("Tiga,", "rekap."), ("Empat,", "cocok."), ("Lima,", "nanya.")):
    put(wt_(wd) - 0.1, flap(), 0.09); put(wt_(wd) - 0.08, whoosh(0.34, 500, 1500, 1.4, 0.45), W * 0.3)
    put(wt_(end) + 0.08, pop(900, 1500, 0.06), 0.11); put(wt_(end) + 0.1, chime((1318.5, 1760), 0.6), 0.035)
# 1 penjualan: two message pops, typing dots, reply, order row slides in
put(wt_("chat") - 0.12, pop(700, 1100, 0.07), 0.09); put(wt_("masuk") - 0.05, pop(750, 1150, 0.07), 0.09)
for i in range(3): put(wt_("masuk") + 0.25 + i * 0.12, tick(0.02, 2400), 0.04)
put(wt_("dibalas") - 0.02, pop(500, 1000, 0.09), 0.12)
put(wt_("dicatat") - 0.12, whoosh(0.4, 700, 2000, 1.4, 0.45), W * 0.4)
# 2 pemasaran: seven cards dealt, AI sparkles, cursor click, button expands, page flies into the tile
for i in range(7): put(wt_("draf") - 0.1 + i * 0.085, flap(), 0.05)
put(wt_("AI,") - 0.06, chime((2093, 2637, 3136), 0.9), 0.04)
for i in range(7): put(wt_("AI,") - 0.06 + i * 0.035, tick(0.02, 3600 + 120 * i), 0.05)
put(wt_("setujui.") - 0.05, tick(0.03, 1800), 0.12); put(wt_("setujui.") + 0.1, whoosh(0.35, 500, 1800, 1.4, 0.45), W * 0.4)
put(wt_("Tiga,") - 0.12, whoosh(0.4, 1800, 500, 1.4, 0.4), W * 0.35)
# 3 keuangan: wipe, five transactions pop, fly into the bars, stamp
put(wt_("Tiga,") + 0.06, whoosh(0.4, 400, 1400, 1.2, 0.45), W * 0.35)
for i in range(5): put(wt_("tiap") - 0.12 + i * 0.1, pop(800 + 90 * i, 1200 + 90 * i, 0.05), 0.08)
for i in range(5): put(wt_("langsung") - 0.1 + i * 0.09, whoosh(0.22, 900, 2600, 1.5, 0.35), W * 0.18)
put(wt_("rekap."), boom(0.22, 200, 90), 0.12)
# 4 rekrutmen: filter bar, six CVs drop, sorted through the filter, interview card
put(wt_("rekrutmen:") + 0.1, zap(0.4), 0.025)
for i in range(6): put(wt_("lamaran") - 0.15 + i * 0.05 + 0.3, boom(0.12, 260, 120), 0.07)
put(wt_("disaring") - 0.05, whoosh(0.55, 1600, 500, 1.3, 0.45), W * 0.4)
put(wt_("wawancara") - 0.32, pop(500, 1000, 0.09), 0.07)   # moved off the word onset (the pop masked "wa-" in the final mix)
# 5 pengiriman: truck token, three notifications, X stamp on the question
put(wt_("pengiriman:"), pop(500, 900, 0.08), 0.1)
for t_ in (wt_("dikabari") - 0.2, wt_("pesanannya") - 0.25): put(t_, rumble(0.5), 0.05)
for t_ in (wt_("pengiriman:") + 0.15, wt_("dikabari") + 0.3, wt_("pesanannya") + 0.25): put(t_, chime((1568, 2093), 0.4), 0.03)
put(wt_("tanpa") - 0.04, boom(0.22, 200, 90), 0.14); put(wt_("tanpa") - 0.02, buzz(0.16), 0.025)
put(D["s04"] - 0.3, whoosh(0.35, 2200, 600, 1.4, 0.4), W * 0.35)
# --- s04 gears + chart
for i in range(5): put(wt_("kelimanya") + i * 0.06, pop(400 + 80 * i, 700 + 80 * i, 0.07), 0.09)
put(wt_("jalan,") - 0.1, rumble(1.6), 0.04)
put(wt_("pendapatan") - 0.42, whoosh(0.45, 500, 1600, 1.4, 0.45), W * 0.4)
put(wt_("pendapatan"), rise(0.8, 400, 1400), 0.035); put(wt_("naik,") + 0.02, chime((1318.5, 1760, 2093), 0.7), 0.05)
put(wt_("biaya"), rise(0.7, 1200, 400), 0.03); put(wt_("turun.") + 0.08, pop(500, 300, 0.1), 0.1)
put(D["s05"] - 0.3, whoosh(0.35, 2200, 600, 1.4, 0.4), W * 0.35)
# --- s05 decisions + loop
put(D["s05"] + 0.02, whoosh(0.36, 700, 1900, 1.4, 0.4), W * 0.35)
for i in range(4): put(wt_("pegang") - 0.05 + i * 0.14, pop(700 + 90 * i, 1000 + 90 * i, 0.06), 0.08)
put(wt_("yang", D["s05"]) - 0.2, whoosh(0.4, 600, 1900, 1.4, 0.45), W * 0.35)
put(wt_("sistem", D["s05"]) - 0.08, zap(0.35), 0.03); put(wt_("AI", D["s05"]) - 0.08, chime((2093, 2637, 3136), 0.8), 0.04)
put(D["s06"] - 0.3, whoosh(0.35, 2200, 600, 1.4, 0.4), W * 0.35)
# --- s06 CTA
put(D["s06"] + 0.02, pop(500, 900, 0.09), 0.11)
for i in range(5): put(D["s06"] + 0.22 + i * 0.1, tick(0.02, 2000 + 140 * i), 0.07)
for k in range(6): put(wt_("SISTEM,") - 0.1 + k / 15, tick(0.022, 4200), 0.15)
put(wt_("SISTEM,") + 0.36, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", D["s06"]) - 0.1, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("aku", D["s06"]) + 0.14, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.04, chime((1568, 2093), 0.8), 0.07)
put(TOT - 1.0, chime((1046, 1568, 2093, 2637), 1.4), 0.06)
out *= 0.74   # master: same level as the R19 bed (mean RMS ≈ -35 dB)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

