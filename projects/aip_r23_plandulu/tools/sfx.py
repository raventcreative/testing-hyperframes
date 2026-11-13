"""Synthesised SFX bed for the R23 PLAN reel (adapted from the R19/R15 beds) (no samples, no downloads): prompt typing, focus lock,
files dropping in + glitch, pencil drawing + bricks tumbling, boom gate (slot, lamp, arm), header flaps, chips, blueprint badges,
key press + thumb slide + lock slam, /plan typing + document unroll + stamp, lens + flags + checks, pen strike + code wall collapse,
approval stamp + progress, CTA.
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
# --- s01 hook: prompt pill + typing, focus corners lock on the button, the asked file, five more files drop in, glitch, shake
def keyclack(f=1900):
    x = tick(0.03, f); k = pop(240, 110, 0.07); y = np.zeros(max(len(x), len(k))); y[:len(x)] += x; y[:len(k)] += 0.5 * k
    return y / np.abs(y).max()
put(0.02, rise(0.6, 300, 1200), 0.04)
put(wt_("suruh") - 0.22, pop(500, 950, 0.09), 0.12)
typing(wt_("suruh") - 0.02, wt_("tombol") + 0.1, 0.07, 22)
for k in range(4): put(wt_("benerin") - 0.05 + k * 0.03, tick(0.02, 3000), 0.08)
put(wt_("tombol") - 0.02, pop(700, 1300, 0.08), 0.13); put(wt_("tombol") + 0.05, chime((1318.5, 1760), 0.5), 0.035)
put(wt_("malah") - 0.06, whoosh(0.35, 2200, 600, 1.4, 0.4), W * 0.4)
for k in range(5): put(wt_("malah") + 0.02 + k * (wt_("berubah?") - wt_("malah")) / 5, pop(520 - 40 * k, 240, 0.07), 0.12)
put(wt_("lima") + 0.1, square_blips([440, 330]), 0.035); put(wt_("lima") + 0.32, square_blips([392, 294]), 0.03)
put(wt_("berubah?") + 0.04, buzz(0.22), 0.04); put(wt_("berubah?") + 0.06, boom(0.3, 170, 70), 0.08)
put(st("s02") - 0.26, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s02 blueprint: TUKANG tag, pencil drawing, dimensions, door marks, wall wakes, bricks tumble + dust, "sesuai denah"
put(wt_("Tukang") - 0.08, pop(600, 1000, 0.08), 0.12)
put(wt_("gambar") - 0.1, scribble(wt_("dulu,") - wt_("gambar") + 0.2), 0.06)
for k in range(3): put(wt_("denah") + 0.05 + k * 0.05, tick(0.02, 3400), 0.07)
put(wt_("dulu,") + 0.0, square_blips([660, 880]), 0.035)
put(wt_("baru") - 0.1, rise(0.4, 300, 700), 0.025)
put(wt_("bongkar") - 0.02, boom(0.5, 120, 50), 0.22)
for k in range(9): put(wt_("bongkar") + 0.05 + k * 0.04, tick(0.03, 900 + 120 * (k % 4)), 0.12)
put(wt_("bongkar") + 0.2, rumble(0.6), 0.08)
put(wt_("tembok.") + 0.2, chime((1318.5, 1760, 2637), 0.8), 0.055); put(wt_("tembok.") + 0.2, pop(600, 1200, 0.09), 0.11)
put(st("s03") - 0.26, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s03 gate: agent rolls up, plan sheet out + into the slot, lamp green, arm swings up, agent rolls in, files glow
s3 = st("s03")
put(wt_("Agent") - 0.05, whoosh(0.55, 300, 1300, 1.2, 0.5), W * 0.55); put(wt_("Agent") + 0.45, tick(0.04, 1200), 0.15)
put(wt_("minta", s3) - 0.05, pop(500, 1000, 0.09), 0.12)
put(wt_("rencananya", s3) + 0.15, whoosh(0.42, 800, 2200, 1.4, 0.45), W * 0.4)
put(wt_("rencananya", s3) + 0.56, tick(0.04, 1600), 0.16)
put(wt_("dulu,", s3) + 0.08, chime((1568, 2093), 0.6), 0.05)
put(wt_("baru", s3) - 0.02, rise(0.42, 250, 900), 0.05); put(wt_("baru", s3) + 0.38, tick(0.04, 1100), 0.15)
put(wt_("boleh", s3) - 0.08, whoosh(0.62, 300, 1500, 1.2, 0.5), W * 0.55)
for k in range(3): put(wt_("kerja.") + 0.1 + k * 0.08, pop(800 + 120 * k, 1400 + 120 * k, 0.06), 0.1)
put(st("s04") - 0.26, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s04 tools: header flap, rows rise, chips pop, blueprint badges unfold, name pulses
put(st("s04") + 0.04, flap(), 0.12); put(st("s04") + 0.2, whoosh(0.4, 400, 1600, 1.4, 0.45), W * 0.4)
for w in ("open", "source", "gratis"):
    for k in range(2): put(wt_(w) + k * 0.07, pop(800 + 150 * k, 1400, 0.06), 0.1)
put(wt_("mode") - 0.06, rip(0.4), 0.05); put(wt_("mode") + 0.06, rip(0.4), 0.04)
put(wt_("OpenCode") - 0.06, chime((1318.5, 1760), 0.5), 0.04); put(wt_("Hermes.") - 0.06, chime((1568, 2093), 0.5), 0.04)
put(st("s05") - 0.24, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s05 folder + model: flap, cards rise, agent pills pop + dock, folder glow, highlight walks, check
put(st("s05") + 0.02, flap(), 0.12); put(st("s05") + 0.18, whoosh(0.4, 400, 1600, 1.4, 0.45), W * 0.35)
for k in range(2): put(wt_("Dua-duanya") - 0.02 + k * 0.12, pop(600 + 100 * k, 1100, 0.08), 0.11)
put(wt_("kerja") + 0.05, whoosh(0.5, 900, 2400, 1.3, 0.45), W * 0.45)
put(wt_("folder") + 0.0, tick(0.04, 1400), 0.15); put(wt_("folder") + 0.02, chime((1046, 1318.5), 0.5), 0.035)
for k, dt in enumerate((-0.05, -0.12, 0.24)): put(wt_(("modelnya", "bebas", "bebas")[k]) + dt, tick(0.025, 2600 + 300 * k), 0.1)
put(wt_("pilih.") - 0.02, pop(900, 1500, 0.07), 0.13)
put(st("s06") - 0.24, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s06 OpenCode Plan: flap, keycap press, thumb slides, eyes light, pencil dart, lock slam, refusal buzz
put(st("s06") + 0.02, flap(), 0.12)
put(wt_("aktifkan") + 0.1, keyclack(1700), 0.2); put(wt_("aktifkan") + 0.34, keyclack(2300), 0.1)
put(wt_("aktifkan") + 0.16, whoosh(0.42, 700, 1900, 1.4, 0.45), W * 0.4)
put(wt_("Plan:") - 0.12, chime((1318.5, 1760), 0.5), 0.04)
for k in range(3): put(wt_("baca,") - 0.2 + k * 0.1, pop(900 + 100 * k, 1500, 0.05), 0.1)
put(wt_("nggak") - 0.12, whoosh(0.3, 1800, 3000, 1.6, 0.6), W * 0.35)
put(wt_("ngedit.") - 0.1, tick(0.05, 900), 0.22); put(wt_("ngedit.") - 0.08, boom(0.25, 200, 90), 0.12); put(wt_("ngedit.") + 0.02, buzz(0.2), 0.04)
put(st("s07") - 0.24, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s07 Hermes /plan: flap, bar, typing, enter, document unrolls, rows write, stamp
put(st("s07") + 0.02, flap(), 0.12); put(st("s07") + 0.16, pop(500, 950, 0.09), 0.1)
typing(wt_("pakai") - 0.05, wt_("rencananya") - 0.22, 0.07, 22)
put(wt_("rencananya") - 0.16, keyclack(1500), 0.18)
put(wt_("rencananya") + 0.06, rip(0.6), 0.07)
put(wt_("ditulis") - 0.05, scribble(1.3), 0.045)
put(wt_("belum") - 0.04 + 0.2, boom(0.3, 180, 80), 0.2); put(wt_("belum") + 0.18, tick(0.04, 1100), 0.18)
put(st("s08") - 0.3, whoosh(0.3, 2000, 600, 1.4, 0.3), W * 0.3)
# --- s08 check: flap, tiles pulse, lens glides, amber flag, checks
put(st("s08") + 0.02, flap(), 0.12)
for k in range(3): put(wt_("tiga") - 0.05 + k * 0.12, pop(700 + 120 * k, 1300 + 120 * k, 0.06), 0.1)
put(wt_("disentuh,") - 0.4, whoosh(0.35, 600, 1500, 1.4, 0.4), W * 0.3)
put(wt_("disentuh,") + 0.2, square_blips([523, 392]), 0.04); put(wt_("disentuh,") + 0.3, pop(500, 800, 0.08), 0.1)
for w in ("dihapus,", "ngetesnya."): put(wt_(w) + 0.16, pop(900, 1500, 0.06), 0.12); put(wt_(w) + 0.18, tick(0.02, 3000), 0.06)
put(st("s09") - 0.2, whoosh(0.25, 1600, 700, 1.4, 0.3), W * 0.25)
# --- s09 cheap vs expensive: pen strike, check, document slides, green tag; wall rises, crack, collapse, dust, amber tag
s9 = st("s09")
put(s9 + 0.12, scribble(0.4), 0.07); put(s9 + 0.64, pop(900, 1500, 0.06), 0.12)
put(wt_("itu", s9) - 0.1, whoosh(0.42, 1200, 500, 1.4, 0.4), W * 0.35)
put(wt_("murah,") - 0.04, chime((1318.5, 1760, 2637), 0.6), 0.05)
put(wt_("murah,") + 0.2, whoosh(0.34, 400, 1400, 1.4, 0.45), W * 0.3)
put(wt_("bongkar", s9) - 0.04, tick(0.05, 700), 0.2); put(wt_("bongkar", s9) + 0.1, rumble(0.4), 0.06)
put(wt_("tembok", s9) - 0.04, boom(0.7, 110, 45), 0.24); put(wt_("tembok", s9) + 0.1, rumble(0.8), 0.09)
for k in range(10): put(wt_("tembok", s9) + k * 0.05, tick(0.03, 800 + 110 * (k % 5)), 0.1)
put(wt_("mahal.") - 0.06, buzz(0.22), 0.04); put(wt_("mahal.") - 0.04, pop(500, 300, 0.1), 0.12)
put(st("s10") - 0.36, whoosh(0.34, 600, 1600, 1.4, 0.4), W * 0.3)
# --- s10 approve + work: stamp, action sheet, route chips, progress
put(st("s10") + 0.02, flap(), 0.1)
put(wt_("pas?") - 0.06 + 0.2, boom(0.3, 200, 90), 0.2); put(wt_("pas?") + 0.16, chime((1568, 2093, 2637), 0.7), 0.06)
put(wt_("Baru", st("s10")) - 0.1, whoosh(0.32, 500, 1700, 1.4, 0.45), W * 0.4)
for k in range(2): put(wt_("Baru", st("s10")) + 0.08 + k * 0.16, pop(800 + 150 * k, 1400, 0.06), 0.1)
put(wt_("suruh", st("s10")) + 0.1, rise(0.62, 400, 1300), 0.04)
for k in range(3): put(wt_("suruh", st("s10")) + 0.04 + k * 0.28, tick(0.02, 3200 + 200 * k), 0.08)
put(st("s11") - 0.25, whoosh(0.35, 2400, 700, 1.4, 0.4), W * 0.5); put(st("s11") + 0.02, pop(600, 1000, 0.08), 0.1)
# --- s11 CTA
put(wt_("Komen") - 0.06, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(4): put(wt_("PLAN,") - 0.08 + k * 0.06, tick(0.022, 4200), 0.15)
put(wt_("PLAN,") + 0.4, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", st("s11")) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("kirim", st("s11")) - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out * 0.72, -1, 1); x = (x * 32767).astype(np.int16)   # R23: -2.9 dB overall (busier cue list than R19)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

