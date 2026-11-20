"""Synthesised SFX bed for the R25 SITUS reel (bedah prompt website 3D; helpers from the R19/R15 bed) (no samples, no downloads):
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
D1 = st("s02"); D2 = st("s03"); D3 = st("s04"); TOT = T["total_sec"]
# --- s01 hook: card glow, bottle spin on "3D", sparkles + "sihir?" chip, strike, drop, laser + snips, rows separate, discs, footer, rewind
put(0.02, rise(0.5, 300, 900), 0.03)
put(0.3, chime((1318.5, 1760), 0.6), 0.03)
put(wt_("3D") - 0.08, whoosh(0.5, 500, 1800, 1.3, 0.5), W * 0.45)
put(wt_("keren") - 0.06, chime((2093, 2637, 3136), 0.9), 0.045)
for k in range(4): put(wt_("keren") - 0.06 + k * 0.05, tick(0.02, 3800 + 200 * k), 0.06)
put(wt_("keren") + 0.04, pop(500, 950, 0.09), 0.12)
put(wt_("bukan") - 0.04, scribble(0.22), 0.07); put(wt_("bukan") + 0.02, buzz(0.16), 0.025)
put(wt_("sihir.") + 0.38, whoosh(0.32, 1800, 500, 1.4, 0.4), W * 0.35)
tL0 = wt_("Kalau") - 0.02; tLd = max(0.5, wt_("isinya") - 0.12 - tL0)
put(tL0 - 0.12, zap(0.5), 0.035); put(tL0 - 0.12, pop(400, 800, 0.08), 0.08)
for i in range(1, 5):
    y = 72 + i * 100 - 5; put(tL0 + tLd * (y - 60) / (588 - 60), snip(), 0.16)
put(wt_("isinya") - 0.08, whoosh(0.4, 600, 1900, 1.3, 0.45), W * 0.4)
for i in range(5): put(wt_("cuma") - 0.04 + i * 0.07, pop(620 + 110 * i, 900 + 140 * i, 0.06), 0.09)
put(wt_("bagian.") - 0.06, pop(600, 1200, 0.09), 0.13); put(wt_("bagian.") - 0.02, chime((1046, 1318.5, 1568), 0.8), 0.045)
put(D1 - 0.62, whoosh(0.45, 2600, 500, 1.3, 0.4), W * 0.45); put(D1 - 0.6, rise(0.4, 1200, 400), 0.02)
# --- s02 the five parts: accordion flap per part, quiet typing of each prompt line, the phone page gains its layer
for wd in ("Satu,", "Dua,", "Tiga,", "Empat,", "Lima,"):
    put(wt_(wd) - 0.08, flap(), 0.1); put(wt_(wd) - 0.06, whoosh(0.34, 500, 1500, 1.4, 0.45), W * 0.3)
for a_, b_ in ((wt_("objek") + 0.02, wt_("melayang.") + 0.3), (wt_("Dua,") + 0.4, wt_("bayangan.") + 0.3), (wt_("Tiga,") + 0.36, wt_("mendekat.") + 0.3),
               (wt_("Empat,") + 0.36, wt_("WhatsApp.") + 0.2), (wt_("Lima,") + 0.36, wt_("HP.") + 0.2)):
    typing(a_, b_, 0.04, 17)
# part 1: placeholder pulse, the bottle drops in and lands, "melayang" tag
for k in range(2): put(wt_("objek") + k * 0.36, tick(0.02, 2400), 0.05)
put(wt_("botol") - 0.12, whoosh(0.32, 1800, 500, 1.4, 0.4), W * 0.4); put(wt_("botol") + 0.26, boom(0.26, 180, 80), 0.16)
put(wt_("melayang.") - 0.04, pop(700, 1100, 0.07), 0.08)
# part 2: background wipe, light beam, highlight, shadow, three tags
put(wt_("warna") - 0.06, whoosh(0.6, 300, 1400, 1.2, 0.5), W * 0.45); put(wt_("warna") + 0.32, pop(700, 1100, 0.07), 0.08)
put(wt_("arah") - 0.04, rise(0.55, 400, 1100), 0.03); put(wt_("cahaya,") - 0.02, chime((1568, 2093), 0.7), 0.04); put(wt_("cahaya,"), pop(750, 1150, 0.07), 0.08)
put(wt_("bayangan.") - 0.06, pop(300, 160, 0.12), 0.12); put(wt_("bayangan."), pop(700, 1100, 0.07), 0.08)
# part 3: scrollbar, two swipes, 360° spin, zoom closer, zoom back
for k in range(2): put(wt_("pas") - 0.06 + k * 0.42, whoosh(0.3, 900, 2400, 1.5, 0.4), W * 0.35)
put(wt_("botolnya") + 0.02, whoosh(0.9, 500, 1600, 1.2, 0.5), W * 0.45); put(wt_("muter") - 0.1, pop(700, 1150, 0.07), 0.08)
put(wt_("mendekat.") - 0.08, rise(0.5, 300, 900), 0.04); put(wt_("mendekat."), pop(700, 1150, 0.07), 0.08)
put(wt_("Empat,") - 0.1, whoosh(0.4, 1400, 500, 1.4, 0.4), W * 0.3)
# part 4: headline, scroll to products (3 pops), scroll to testimonial, WhatsApp button
put(wt_("judul,") - 0.08, pop(500, 900, 0.08), 0.11)
put(wt_("produk,") - 0.12, whoosh(0.45, 700, 2000, 1.4, 0.45), W * 0.4)
for i in range(3): put(wt_("produk,") + 0.08 + i * 0.08, pop(800 + 120 * i, 1200 + 120 * i, 0.06), 0.08)
put(wt_("testimoni,") - 0.12, whoosh(0.4, 700, 2000, 1.4, 0.45), W * 0.35); put(wt_("testimoni,"), pop(600, 1000, 0.07), 0.09)
put(wt_("tombol") + 0.06, pop(500, 1000, 0.09), 0.13); put(wt_("WhatsApp.") + 0.04, chime((1318.5, 1760), 0.6), 0.035)
# part 5: scroll back, tech sheet rises, three checks, spin, meter fills, success
put(wt_("Lima,") - 0.04, whoosh(0.5, 2000, 600, 1.4, 0.45), W * 0.35)
put(wt_("teknis:"), whoosh(0.42, 400, 1500, 1.4, 0.45), W * 0.4)
for wd, d in (("HTML,", 0), ("Three.js", 0.1)): put(wt_(wd) + d, pop(900, 1500, 0.06), 0.11); put(wt_(wd) + d, tick(0.03, 1800), 0.1)
put(wt_("3D-nya,") - 0.04, whoosh(0.9, 500, 1600, 1.2, 0.5), W * 0.4)
put(wt_("ringan") - 0.12, rise(0.45, 500, 1500), 0.035)
put(wt_("HP.") - 0.02, pop(900, 1500, 0.06), 0.11); put(wt_("HP."), chime((1046, 1318.5, 1568, 2093), 1.0), 0.06)
# combine: sheet down, rows stack (deck shuffle), one message, send, Claude types + answers, rescan, revision typed + sent, headline grows
put(wt_("Gabungin") - 0.06, whoosh(0.36, 1500, 500, 1.4, 0.4), W * 0.3); put(wt_("Gabungin") - 0.08, flap(), 0.08)
for i in range(5): put(wt_("kelimanya,") - 0.08 + (4 - i) * 0.03 + 0.3, tick(0.025, 1500 + 150 * i), 0.1)
put(wt_("kelimanya,") + 0.36, pop(500, 950, 0.09), 0.13)
put(wt_("kasih") + 0.04, whoosh(0.3, 900, 2600, 1.5, 0.4), W * 0.35); put(wt_("kasih") + 0.06, pop(900, 1400, 0.05), 0.08)
for i in range(3): put(wt_("kasih") + 0.2 + i * 0.08, tick(0.02, 2600), 0.05)
put(wt_("Claude,") + 0.26, pop(600, 1100, 0.08), 0.12); put(wt_("Claude,") + 0.22, zap(0.45), 0.025)
typing(wt_("revisi") + 0.12, min(wt_("sehari-hari.") + 0.12, D2 - 0.86) - 0.1, 0.07, 22)
tSend = min(wt_("sehari-hari.") + 0.12, D2 - 0.86)
put(tSend - 0.04, pop(900, 1400, 0.05), 0.09); put(tSend, whoosh(0.3, 900, 2600, 1.5, 0.4), W * 0.3)
put(tSend + 0.18, pop(500, 1000, 0.09), 0.12); put(tSend + 0.2, chime((1318.5, 1760), 0.6), 0.035)
put(D2 - 0.3, whoosh(0.35, 2200, 600, 1.4, 0.4), W * 0.4)
# --- s03 pricing: header flap, $ coin, strike, flip to Rp, coin parks, three blocks land + joints, result bar, city card, dots, band, marker
put(D2 + 0.02, flap(), 0.12); put(D2 + 0.1, boom(0.3, 220, 100), 0.14)
put(wt_("harga,") - 0.02, pop(600, 1000, 0.07), 0.09)
put(wt_("lupakan") - 0.02, scribble(0.25), 0.08); put(wt_("lupakan") + 0.04, buzz(0.18), 0.03)
put(wt_("dolar.") - 0.08, whoosh(0.4, 600, 2200, 1.4, 0.45), W * 0.4); put(wt_("dolar.") + 0.1, chime((1568, 2093, 2637), 0.9), 0.06)
put(wt_("Hitung") - 0.24, whoosh(0.45, 1600, 500, 1.4, 0.4), W * 0.35)
for wd in ("jam", "jatah", "domain"): put(wt_(wd, D2) + 0.1, boom(0.24, 200, 90), 0.18); put(wt_(wd, D2) + 0.1, tick(0.03, 1500), 0.08)
for wd in ("jatah", "domain"): put(wt_(wd, D2) + 0.14, pop(800, 1300, 0.06), 0.08)
put(wt_("hosting,") - 0.06, pop(500, 1000, 0.09), 0.13); put(wt_("hosting,"), chime((1046, 1318.5), 0.6), 0.04)
put(wt_("lalu") - 0.16, whoosh(0.5, 500, 1600, 1.4, 0.45), W * 0.4)
for i in range(5): put(wt_("harga", wt_("bandingkan")) - 0.12 + i * 0.07, tick(0.025, 2600 + 150 * i), 0.09)
put(wt_("harga", wt_("bandingkan")) + 0.3, pop(600, 1100, 0.08), 0.09)
put(wt_("kotamu.") - 0.24, whoosh(0.5, 1800, 700, 1.4, 0.45), W * 0.35); put(wt_("kotamu.") + 0.26, pop(700, 1200, 0.07), 0.11)
put(wt_("kotamu.") + 0.2, pop(400, 700, 0.08), 0.07)
put(D3 - 0.3, whoosh(0.35, 2200, 600, 1.4, 0.4), W * 0.4)
# --- s04 template + CTA
put(D3 + 0.02, pop(500, 900, 0.09), 0.11)
for i in range(5): put(D3 + 0.12 + i * 0.06, tick(0.02, 2000 + 140 * i), 0.07)
for i in range(5): put(wt_("kosongnya") + i * 0.07, tick(0.02, 3000), 0.05)
put(wt_("gratis,") - 0.06, boom(0.26, 200, 90), 0.15); put(wt_("gratis,"), chime((1318.5, 1760, 2637), 0.8), 0.05)
put(wt_("tinggal") - 0.2, whoosh(0.3, 900, 2000, 1.5, 0.4), W * 0.3); put(wt_("tinggal") + 0.1, scribble(max(0.2, wt_("Komen") - 0.34 - wt_("tinggal"))), 0.05)
put(wt_("Komen") - 0.2, whoosh(0.4, 1800, 600, 1.4, 0.45), W * 0.4)
put(wt_("Komen") - 0.06, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(5): put(wt_("SITUS,") - 0.08 + k * 0.06, tick(0.022, 4200), 0.15)
put(wt_("SITUS,") + 0.4, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", wt_("Komen")) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("kirim", wt_("Komen")) - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(TOT - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
out *= 0.74   # master: same level as the R19 bed (mean RMS ≈ -35 dB)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

