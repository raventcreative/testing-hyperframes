"""Synthesised SFX bed for the R21 PILIH reel (adapted from the R19 ASISTEN bed) (no samples, no downloads): notification pops for
the six agent cards, suck-in whoosh + question-card slam, fork drawing + signpost flaps, header flaps, hanging cards + amber stamp,
laptop lid + task ticks, data chips flying up into the cloud, key turn + cards docking + machines lighting, chat bubbles + skill
drop, warning buzz + typed config command + switch slide, hub + spokes + pulses, slider snaps + card flip, CTA.
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
def keyclack(f=1900):
    x = tick(0.03, f); k = pop(240, 110, 0.07); y = np.zeros(max(len(x), len(k))); y[:len(x)] += x; y[:len(k)] += 0.5 * k
    return y / np.abs(y).max()
# --- s01 hook: six cards pop like notifications, "rame" wobble, suck-in + question card, fork draws, signs, kamu disc, "?"
put(0.02, rise(0.6, 300, 1200), 0.04)
for k in range(6): put(0.06 + k * 0.15, pop(700 + 60 * k, 1300 + 60 * k, 0.07), 0.11)
put(wt_("rame.") - 0.08, square_blips([880, 1175, 1568]), 0.035)
for k in range(6): put(wt_("rame.") - 0.04 + k * 0.05, tick(0.02, 3000 + 150 * k), 0.06)
put(wt_("Sebelum") - 0.14, whoosh(0.4, 2200, 500, 1.4, 0.45), W * 0.6)
put(wt_("Sebelum") + 0.3, boom(0.26, 190, 80), 0.18)
put(wt_("jawab") - 0.04, pop(500, 900, 0.08), 0.1)
put(wt_("tinggal") - 0.42, whoosh(0.35, 1800, 600, 1.4, 0.4), W * 0.35)
put(wt_("tinggal") - 0.36, rise(0.5, 300, 900), 0.03)
for k in range(2): put(wt_("tinggal") - 0.04 + k * 0.08, flap(), 0.1)
put(wt_("pakai,") - 0.1, chime((1318.5, 1760), 0.5), 0.04)
put(wt_("pegang") - 0.18, whoosh(0.4, 500, 1500, 1.4, 0.45), W * 0.3)
put(wt_("sendiri?") - 0.1, chime((1568, 2093), 0.5), 0.04); put(wt_("sendiri?") + 0.02, pop(900, 1500, 0.07), 0.1)
put(st("s02") - 0.24, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s02 cloud: header flap, cloud swell, three cards drop on strings, Muse stamp + pin
put(st("s02") + 0.04, flap(), 0.12); put(st("s02") + 0.24, whoosh(0.5, 300, 1200, 1.2, 0.45), W * 0.45)
for w in ("Dots", "Grok", "Muse"):
    put(wt_(w) - 0.16, whoosh(0.3, 1600, 500, 1.4, 0.4), W * 0.3); put(wt_(w) + 0.22, pop(420, 220, 0.09), 0.13); put(wt_(w) + 0.24, tick(0.03, 2200), 0.07)
put(wt_("belum") - 0.06, pop(600, 1000, 0.08), 0.1)
put(wt_("Indonesia.") - 0.12 + 0.2, boom(0.24, 200, 90), 0.2); put(wt_("Indonesia.") + 0.1, buzz(0.18), 0.03)
put(st("s03") - 0.2, whoosh(0.28, 2000, 600, 1.4, 0.35), W * 0.3)
# --- s03 trade-off: flap, green chip, laptop lid closes, task ticks, data chips rise and fly up into the cloud, lock, amber chip
put(st("s03") + 0.02, flap(), 0.12); put(st("s03") + 0.06, pop(700, 1200, 0.08), 0.11)
put(wt_("kerja") - 0.1, keyclack(900), 0.16)
for w, d in (("kerja", 0.1), ("terus", 0.2), ("cloud", 0.22)): put(wt_(w) + d, pop(900, 1500, 0.05), 0.09); put(wt_(w) + d + 0.02, tick(0.02, 3200), 0.05)
put(wt_("tapi", st("s03")) - 0.12, whoosh(0.3, 1800, 500, 1.4, 0.4), W * 0.3)
for w, d in (("data", 0), ("login", 0), ("login", 0.3)): put(wt_(w) + d - 0.1, pop(500, 900, 0.08), 0.11)
put(wt_("ikut") - 0.22, whoosh(0.6, 400, 2800, 1.2, 0.5), W * 0.7)
put(wt_("sana.") - 0.04, tick(0.04, 1300), 0.16); put(wt_("sana.") + 0.04, buzz(0.2), 0.035)
put(st("s04") - 0.24, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s04 open source: flap, key turns (clack), box draws, two cards slide in, MIT chips, machines light
put(st("s04") + 0.02, flap(), 0.12); put(st("s04") + 0.06, pop(500, 900, 0.08), 0.1)
put(wt_("sendiri:") - 0.02, keyclack(1500), 0.2); put(wt_("sendiri:") + 0.1, tick(0.03, 2200), 0.1)
put(wt_("sendiri:") + 0.42, whoosh(0.4, 1800, 500, 1.4, 0.4), W * 0.35)
put(wt_("OpenClaw", st("s04")) - 0.14, whoosh(0.36, 500, 1700, 1.4, 0.45), W * 0.4); put(wt_("Hermes,") - 0.14, whoosh(0.36, 500, 1700, 1.4, 0.45), W * 0.4)
for k in range(2): put(wt_("open", st("s04")) - 0.06 + k * 0.1, pop(900, 1500, 0.06), 0.1)
for w in ("laptop", "servermu."): put(wt_(w) - 0.06, tick(0.035, 1700), 0.14); put(wt_(w) - 0.02, chime((1318.5, 1760), 0.45), 0.03)
put(st("s05") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s05 chat + skill: flap, panels slide, bubble out, typing dots, reply, task card, flip, drop into the drawer, counter
put(st("s05") + 0.02, flap(), 0.12); put(st("s05") + 0.08, whoosh(0.36, 1800, 600, 1.4, 0.4), W * 0.35)
put(wt_("kamu", st("s05")) - 0.04, pop(600, 1100, 0.08), 0.13)
for k in range(4): put(wt_("kamu", st("s05")) + 0.34 + k * 0.12, tick(0.015, 2800), 0.05)
put(wt_("WhatsApp,") + 0.02, pop(500, 950, 0.09), 0.13)
put(wt_("Hermes", st("s05")) - 0.1, pop(700, 1200, 0.08), 0.11)
put(wt_("nulis") - 0.04, scribble(0.4), 0.05); put(wt_("nulis") + 0.1, tick(0.03, 2400), 0.1)
put(wt_("skill") + 0.24, whoosh(0.36, 1500, 400, 1.4, 0.4), W * 0.35); put(wt_("skill") + 0.56, pop(420, 220, 0.09), 0.14)
put(wt_("skill") + 0.58, chime((1318.5, 1760, 2637), 0.7), 0.05)
put(st("s06") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s06 caution: amber flap, two tiles light, settings card, BAWAAN tag, command runs (typing + shake buzz), config typed, switch slide
put(st("s06") + 0.02, flap(), 0.12)
put(wt_("tanganmu,") - 0.08, chime((1318.5, 1760), 0.45), 0.035); put(wt_("keamanannya") - 0.08, pop(500, 900, 0.09), 0.12); put(wt_("keamanannya") - 0.04, buzz(0.16), 0.025)
put(wt_("Bawaan") - 0.36, whoosh(0.4, 2200, 600, 1.4, 0.45), W * 0.45)
put(wt_("OpenClaw", 29.9) - 0.06, pop(600, 1000, 0.08), 0.12)
typing(wt_("jalanin") - 0.1, wt_("jalanin") + 0.5, 0.07, 22)
put(wt_("tanpa") - 0.1, keyclack(1100), 0.16); put(wt_("tanpa") - 0.06, buzz(0.3), 0.04); put(wt_("nanya,") - 0.12, pop(500, 900, 0.09), 0.12)
typing(wt_("ubah") - 0.14, wt_("ask.") - 0.12, 0.07, 22)
put(wt_("ask.") - 0.1, whoosh(0.32, 700, 1900, 1.4, 0.4), W * 0.35); put(wt_("ask.") + 0.18, tick(0.04, 1500), 0.18); put(wt_("ask.") + 0.2, chime((1568, 2093), 0.4), 0.04)
# --- s07 MausBot: flap, #6 badge, hub, ghost card + X, chips dock, spokes, pulses, footnote
put(st("s07") + 0.02, flap(), 0.12)
put(wt_("keenam") - 0.06, pop(700, 1300, 0.09), 0.14)
put(wt_("MausBot.") - 0.08, boom(0.26, 190, 85), 0.16); put(wt_("MausBot.") + 0.02, chime((1046, 1318.5, 1568), 0.6), 0.05)
put(wt_("Bukan") - 0.08, pop(500, 900, 0.08), 0.1); put(wt_("baru,") - 0.06, buzz(0.18), 0.04); put(wt_("baru,") - 0.04, pop(400, 200, 0.08), 0.12)
for k in range(4): put(wt_("pengatur") + 0.02 + k * 0.12, pop(800 + 100 * k, 1400 + 100 * k, 0.06), 0.1)
for k in range(4): put(wt_("kamu", st("s07")) - 0.1 + k * 0.1, tick(0.02, 3000 + 200 * k), 0.08)
put(wt_("kamu", st("s07")) - 0.14, rise(0.45, 500, 1400), 0.03)
put(wt_("punya.") - 0.1, pop(600, 1000, 0.07), 0.08)
put(st("s08") - 0.2, whoosh(0.28, 2000, 600, 1.4, 0.35), W * 0.3)
# --- s08 rule: flap, slider, knob snaps left (praktis) + card, flips right (kendali) + card flip
put(st("s08") + 0.02, flap(), 0.12); put(st("s08") + 0.06, whoosh(0.35, 400, 1400, 1.4, 0.4), W * 0.3)
put(wt_("praktis,", st("s08")) - 0.12, whoosh(0.3, 1600, 500, 1.4, 0.4), W * 0.3); put(wt_("praktis,", st("s08")) + 0.18, tick(0.04, 1500), 0.18)
put(wt_("cloud.") - 0.06, pop(700, 1200, 0.07), 0.1)
put(wt_("kendali,") - 0.14, whoosh(0.34, 500, 1600, 1.4, 0.4), W * 0.35); put(wt_("kendali,") + 0.2, tick(0.04, 1700), 0.18)
put(wt_("kendali,") + 0.06, flap(), 0.08)
put(wt_("open", st("s08")) - 0.06, pop(900, 1500, 0.07), 0.1)
put(st("s09") - 0.3, whoosh(0.35, 2400, 700, 1.4, 0.4), W * 0.5); put(st("s09") + 0.02, pop(600, 1000, 0.08), 0.1)
# --- s09 CTA
put(wt_("Komen") - 0.06, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(5): put(wt_("PILIH,") - 0.08 + k * 0.06, tick(0.022, 4200), 0.15)
put(wt_("PILIH,") + 0.4, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", st("s09")) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("kirim", st("s09")) - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

