"""Synthesised SFX bed for the R30 MARKETING reel (adapted from the R25 SITUS bed; old R25 event notes follow) (bedah prompt website 3D; helpers from the R19/R15 bed) (no samples, no downloads):
card glow, bottle spins, sparkles + struck "sihir?" chip, laser + scissor snips, rows separating + number discs, page rewind; per part:
accordion flap, quiet prompt typing, bottle drop + landing, background wipe, light, shadow, scroll swipes, zoom, sections + scrolls,
WhatsApp button, tech sheet + checks, meter, success chime; deck shuffle, send, Claude typing dots + reply, rescan, revision typing +
send; pricing: coin pop, strike, coin flip, blocks landing, joints, result bar, ruler dots, marker slide; template + CTA.
Deterministic.
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
TOT = T["total_sec"]; L = lambda id: st(id)
# --- scene changes: one hit each (whoosh / flood / whip / dive), small hop for the hosts
for id_, kind in (("s02", "w"), ("s03", "f"), ("s04", "f"), ("s05", "x"), ("s06", "d"), ("s07", "w")):
    t = L(id_)
    if kind == "f": put(t - 0.6, rise(0.55, 300, 1300), 0.08); put(t, boom(0.5, 110, 50), 0.22)
    elif kind == "x": put(t - 0.36, whoosh(0.5, 400, 3200, 1.2, 0.6), W * 1.2)
    elif kind == "d": put(t - 0.32, whoosh(0.45, 1800, 300, 1.3, 0.5), W); put(t + 0.05, boom(0.4, 120, 60), 0.15)
    else: put(t - 0.2, whoosh(0.5, 500, 2400, 1.1, 0.45), W)
# --- s01: the reel spins (ticks), lands on each chore (clack), fast spin, final row, burst, chips into boxes, boss card
for k in range(10): put(0.02 + k * 0.035, tick(0.015, 2600 + 90 * k), 0.05)
for wd in ("Cari", "nulis", "bikin", "isi", "posting,", "balas", "cek"): put(wt_(wd) - 0.1, flap(), 0.13)
tA = wt_("angka.") + 0.05; tS = wt_("Semua")
for k in range(int((tS - tA) / 0.04)): put(tA + k * 0.04, tick(0.012, 3000), 0.045)
put(tS - 0.05, pop(500, 220, 0.12), 0.18); put(wt_("sendiri?"), buzz(0.25), 0.05)
put(wt_("Coba") - 0.05, boom(0.35, 160, 70), 0.14)
for i in range(7): put(wt_("Coba") + 0.02 + i * 0.04, pop(700 + 60 * i, 1100 + 60 * i, 0.05), 0.06)
for i in range(3): put(wt_("tim") - 0.12 + i * 0.12, boom(0.25, 200, 100), 0.12)
for i in range(7): put(wt_("marketing") + 0.43 + i * 0.07, tick(0.02, 2000 + 120 * i), 0.07)
put(wt_("kamu", wt_("dan", 10)) - 0.1, whoosh(0.35, 600, 1800, 1.4, 0.4), W * 0.7); put(wt_("bosnya."), chime((1318.5, 1760, 2637), 0.9), 0.07)
# --- s02: funnel draws, dot drops, flag, strike, ring draws + laps, week flip, gate bump, lock, button, flood
put(wt_("Bentuknya") + 0.1, rise(0.7, 200, 700), 0.05)
put(wt_("sekali") - 0.05, whoosh(0.6, 2400, 400, 1.6, 0.3), W * 0.6); put(wt_("selesai,"), pop(400, 200, 0.1), 0.14)
put(wt_("tapi") - 0.05, rip(0.3), 0.08)
put(wt_("putaran.") - 0.15, rise(0.7, 400, 1600), 0.06)
put(wt_("depan.") - 0.25, flap(), 0.12)
put(wt_("aturan") - 0.05, pop(900, 1400, 0.07), 0.1)
put(wt_("nggak") + 0.05, boom(0.3, 140, 60), 0.2); put(wt_("nggak") + 0.08, tick(0.03, 900), 0.12)
put(wt_("setujui.") - 0.01, pop(1100, 700, 0.06), 0.16); put(wt_("setujui.") + 0.12, chime((1568, 2093), 0.6), 0.06)
# --- s03: radar sweep blips, Claude logo spin, chips, questions + bars, pour into jar, drafts typed, calendar fills
put(wt_("cari", L("s03")) - 0.15, rise(0.5, 300, 900), 0.05)
for wd in ("Claude", "rame", "pasarmu,"): put(wt_(wd, L("s03")) + 0.3, pop(1500, 2400, 0.05), 0.07)
for i in range(3): put(wt_("pertanyaan") - 0.1 + i * 0.22, pop(700, 1000, 0.06), 0.08)
for i in range(6): put(wt_("Dari") + 0.53 + i * 0.13, pop(500 - 30 * i, 260, 0.08), 0.09)
for wd in ("draf", "caption,", "email."): put(wt_(wd, L("s03")) - 0.2, whoosh(0.3, 700, 2000, 1.4, 0.4), W * 0.5); typing(wt_(wd, L("s03")) + 0.2, wt_(wd, L("s03")) + 0.9, 0.035, 18)
for i in range(7): put(wt_("Jadi") + 0.4 + i * 0.12, tick(0.02, 1800 + 140 * i), 0.08)
put(wt_("kehabisan"), chime((1318.5, 1760, 2637), 0.8), 0.06)
# --- s04: chips, tiles resolve, waveform, approve + stamp, schedule, copies fly to the channels, comment + typed reply, sensitive, inbox
for wd in ("kreatif", "distribusi."): put(wt_(wd) - 0.1, pop(800, 1200, 0.06), 0.09)
for wd in ("gambar", "video,"): put(wt_(wd) - 0.1, rise(0.35, 600, 1800), 0.05)
put(wt_("setujui,") - 0.01, pop(1100, 700, 0.06), 0.16); put(wt_("setujui,") + 0.12, boom(0.25, 180, 80), 0.18)
put(wt_("dijadwalkan") - 0.1, flap(), 0.1)
for i in range(3): put(wt_("tiap", L("s04")) + 0.4 + i * 0.08, pop(900 + 150 * i, 1500 + 150 * i, 0.05), 0.09)
put(wt_("komentar") + 0.3, pop(800, 1100, 0.06), 0.08); typing(wt_("dibalas") + 0.1, wt_("bahasamu.") - 0.05, 0.05, 20)
put(wt_("sensitif,") + 0.3, buzz(0.2), 0.06); put(wt_("dilempar"), whoosh(0.45, 1800, 500, 1.4, 0.5), W * 0.8); put(wt_("kamu.", L("s04")), boom(0.25, 160, 80), 0.15)
# --- s05: ring, table bars, strike, winner, dot rides the loop, chart columns + line, spreadsheet struck
for wd in ("chat,", "booking,", "penjualan."): put(wt_(wd, L("s05")) - 0.05, tick(0.03, 1700), 0.1)
put(wt_("Bukan", L("s05")), rip(0.25), 0.08); put(wt_("likes."), chime((1568, 2093), 0.6), 0.06)
put(wt_("balik") - 0.05, whoosh(0.6, 500, 1500, 1.5, 0.5), W * 0.5); put(wt_("satu.", L("s05")) - 0.1, pop(1200, 1800, 0.06), 0.1)
for i in range(4): put(wt_("Minggu", L("s05")) + i * 0.22, pop(400 + 100 * i, 700 + 100 * i, 0.07), 0.09)
put(wt_("banyak") - 0.1, rise(1.1, 400, 1400), 0.05)
put(wt_("rekap") + 0.1, rip(0.25), 0.08); put(wt_("manual.") - 0.2, whoosh(0.4, 1500, 300, 1.4, 0.5), W * 0.5)
# --- s06: terminal typing, module ticks, cables, connectors, page print, sections
typing(L("s06") + 0.45, wt_("Claude", L("s06")), 0.05, 20)
for i in range(3): put(wt_("Claude", L("s06")) + 0.15 + i * 0.22, tick(0.03, 2200), 0.08)
for wd in ("pelanggan,", "kalender,", "sosmedmu."): put(wt_(wd) - 0.3, zap(0.3), 0.04); put(wt_(wd) + 0.05, pop(1300, 1900, 0.05), 0.09)
put(wt_("pagi") - 0.05, rise(0.6, 300, 900), 0.05)
for wd in ("berhasil,", "booking,", "berikutnya."): put(wt_(wd, L("s06")) - 0.33, flap(), 0.09)
# --- s07: belt packets, brand/budget, lock, comment typing, send, file, sent, end logo
for i in range(4): put(wt_("memindahkan") - 0.3 + i * 0.55, tick(0.02, 2500), 0.06)
for wd in ("Brand", "budget,"): put(wt_(wd) - 0.1, pop(800, 1200, 0.06), 0.1)
put(wt_("tetap", L("s07")), tick(0.04, 900), 0.12)
for k in range(9): put(wt_("MARKETING,") - 0.15 + k / 18, tick(0.022, 4200), 0.14)
put(wt_("kirim") - 0.1, whoosh(0.5, 600, 2600, 1.2, 0.4), W * 0.8); put(wt_("blueprint-nya") - 0.1, pop(700, 1100, 0.07), 0.1)
put(wt_("DM."), chime((1318.5, 1760, 2637), 1.0), 0.07)
put(TOT - 2.45 + 0.1, boom(0.6, 110, 45), 0.18); put(TOT - 2.45 + 0.12, chime((1046.5, 1568, 2093, 2637), 1.6), 0.07)
out *= 0.74   # master: same level as the R19 bed (mean RMS ≈ -35 dB)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

