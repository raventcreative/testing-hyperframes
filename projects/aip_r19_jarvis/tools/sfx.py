"""Synthesised SFX bed for the R19 ASISTEN reel (adapted from the R15 HERMES bed) (no samples, no downloads): key clacks, voice
pill typing, windows snapping tidy, header flaps, window slide, file scan + match, email scan + draft typing, paste + installer steps,
GRATIS stamp + plug seating, warning + permission switches, packets crossing the border, CTA.
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
# --- s01 hook: three keys press (clack) and are held, voice pill + typing, keys spring back, pill flies off, messy desktop, windows snap tidy
def keyclack(f=1900):
    x = tick(0.03, f); k = pop(240, 110, 0.07); y = np.zeros(max(len(x), len(k))); y[:len(x)] += x; y[:len(k)] += 0.5 * k
    return y / np.abs(y).max()
put(0.02, rise(0.6, 300, 1200), 0.04)
for k in range(3): put(max(0.06, wt_("Tahan") - 0.1) + k * 0.09, keyclack(1800 + 150 * k), 0.2)
put(wt_("Tahan") + 0.2, chime((1318.5, 1760), 0.5), 0.035)
put(wt_("ngomong,") - 0.16, pop(500, 950, 0.09), 0.12)
typing(wt_("ngomong,") - 0.02, wt_("lepas.") - 0.1, 0.07, 22)
for k in range(3): put(wt_("lepas.") - 0.06 + k * 0.04, keyclack(2300 + 120 * k), 0.13)
put(wt_("lepas.") + 0.26, whoosh(0.4, 900, 2600, 1.3, 0.45), W * 0.5)
put(wt_("Mac") - 0.42, whoosh(0.35, 2200, 600, 1.4, 0.4), W * 0.4)
for k in range(4): put(wt_("Mac") - 0.18 + k * 0.06, pop(420 + 60 * k, 240, 0.07), 0.1)
for k in range(4): put(wt_("beresin") + 0.28 + k * 0.06, tick(0.02, 2600 + 200 * k), 0.1)
put(wt_("beresin") - 0.1, whoosh(0.45, 500, 1900, 1.3, 0.45), W * 0.5)
put(wt_("sisanya.") + 0.02, chime((1318.5, 1760, 2637), 0.9), 0.06); put(wt_("sisanya.") + 0.02, pop(600, 1200, 0.09), 0.12)
put(st("s02") - 0.26, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.35)
# --- s02 name: header builds, spec card, REPO RESMI, three ticks, footnote
put(st("s02") + 0.04, flap(), 0.12); put(st("s02") + 0.2, whoosh(0.4, 400, 1600, 1.4, 0.45), W * 0.4)
put(wt_("Atticus,") - 0.02, pop(700, 1300, 0.08), 0.13); put(wt_("Atticus,") + 0.1, tick(0.03, 2200), 0.1)
for w in ("asisten", "open", "khusus"): put(wt_(w) + 0.16, pop(900, 1500, 0.06), 0.11); put(wt_(w) + 0.18, tick(0.02, 3000), 0.06)
put(st("s03") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s03 windows: flap, voice pill typing, chat window opens, target pulses, slide left, TANPA AI chip
put(st("s03") + 0.02, flap(), 0.12); put(st("s03") + 0.08, pop(500, 950, 0.09), 0.1)
typing(st("s03") + 0.5, wt_("kiri.") + 0.1, 0.06, 22)
put(wt_("WhatsApp,") - 0.02, pop(500, 1000, 0.09), 0.13)
put(wt_("kiri.") - 0.1, square_blips([660, 880]), 0.04)
put(wt_("Jendelanya") - 0.06, whoosh(0.45, 600, 2400, 1.3, 0.45), W * 0.55); put(wt_("Jendelanya") + 0.36, tick(0.035, 1500), 0.16)
put(wt_("pindah.") - 0.2, chime((1568, 2093), 0.6), 0.05)
put(st("s04") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s04 files: flap, typing, file rows slide in, scan beam ticks, match (COCOK), found chip
put(st("s04") + 0.02, flap(), 0.12)
typing(st("s04") + 0.2, st("s04") + 1.05, 0.06, 22)
for k in range(4): put(st("s04") + 0.32 + k * 0.07, pop(480 + 50 * k, 260, 0.07), 0.1)
put(wt_("nyari") - 0.2, rise(0.5, 400, 1200), 0.03)
for k in range(3): put(wt_("nyari") - 0.12 + k * 0.39, tick(0.03, 2400 + 300 * k), 0.12)
put(wt_("filenya,") - 0.02, pop(700, 1300, 0.09), 0.15); put(wt_("filenya,") + 0.04, chime((1318.5, 1760, 2637), 0.8), 0.06)
put(wt_("bukan") - 0.04, pop(900, 1500, 0.06), 0.11)
put(st("s05") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s05 email: flap, card slides in, focus corners + scan, voice typing, draft card + typing, buttons, locked Kirim buzz, safe chip
put(st("s05") + 0.02, flap(), 0.12); put(st("s05") + 0.1, whoosh(0.4, 2200, 600, 1.4, 0.4), W * 0.45)
for k in range(4): put(wt_("bilang:") - 0.16 + k * 0.03, tick(0.02, 3200), 0.08)
put(wt_("bilang:") - 0.06, rise(0.7, 500, 1500), 0.03)
typing(wt_("balas,") - 0.1, wt_("bisa.") + 0.05, 0.06, 22)
put(wt_("Drafnya") - 0.08, whoosh(0.4, 500, 1700, 1.4, 0.45), W * 0.45)
typing(wt_("Drafnya") + 0.14, wt_("jadi,") + 0.2, 0.08, 24)
for k in range(2): put(wt_("jadi,") - 0.1 + k * 0.08, pop(700 + 100 * k, 1200, 0.07), 0.11)
put(wt_("nggak") + 0.02, buzz(0.2), 0.04)
put(wt_("sendiri.") - 0.08, chime((1568, 2093), 0.6), 0.05)
put(st("s06") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s06 install: flap, link pill, "disalin", paste drop, card glow, ask typing, four installer steps
put(st("s06") + 0.02, flap(), 0.12); put(st("s06") + 0.12, pop(600, 1000, 0.08), 0.1)
put(wt_("tempel") - 0.1, tick(0.03, 2600), 0.12)
put(wt_("tempel") + 0.02, whoosh(0.36, 1800, 500, 1.4, 0.45), W * 0.5); put(wt_("tempel") + 0.38, pop(500, 900, 0.08), 0.12)
put(wt_("Claude") - 0.04, chime((1318.5, 1760), 0.5), 0.035)
typing(wt_("minta") - 0.32, wt_("minta") + 0.3, 0.07, 22)
for k in range(4): put(wt_("minta") + 0.12 + k * 0.213, pop(800 + 120 * k, 1400 + 120 * k, 0.06), 0.11)
put(wt_("pasangin.") + 0.14, chime((1318.5, 1760, 2637), 0.8), 0.06)
put(st("s07") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s07 cost: flap, app card, GRATIS stamp, cable out, plug seats (Claude), chips, unplug -> seat (local), API key chip
put(st("s07") + 0.02, flap(), 0.12); put(st("s07") + 0.12, whoosh(0.4, 400, 1600, 1.4, 0.45), W * 0.4)
put(wt_("gratis,") - 0.08 + 0.2, boom(0.24, 200, 90), 0.2)
put(wt_("otaknya") - 0.06, rise(0.35, 300, 900), 0.03)
put(wt_("Claude", st("s07")) - 0.3 + 0.32, tick(0.04, 1300), 0.2); put(wt_("Claude", st("s07")) + 0.04, zap(0.35), 0.035)
for w in ("Pro", "Max,"): put(wt_(w) - 0.02, tick(0.02, 3000), 0.1)
put(wt_("model", st("s07")) - 0.3, whoosh(0.34, 900, 2000, 1.4, 0.4), W * 0.4)
put(wt_("model", st("s07")) + 0.02, tick(0.04, 1300), 0.2); put(wt_("model", st("s07")) + 0.06, zap(0.35), 0.035)
put(wt_("Max,") + 0.1, pop(700, 1300, 0.08), 0.11)
put(st("s08") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s08 permissions: flap, warning pop + buzz, eye, corners close + scan, settings card, four switches, amber row
put(st("s08") + 0.02, flap(), 0.12)
put(wt_("ingat,") - 0.12, pop(500, 900, 0.09), 0.13); put(wt_("ingat,") - 0.06, buzz(0.22), 0.035)
put(wt_("ingat,") + 0.1, boom(0.3, 170, 70), 0.1)
for k in range(4): put(wt_("lihat") - 0.1 + k * 0.03, tick(0.02, 2400), 0.08)
put(wt_("lihat") - 0.04, rise(0.7, 400, 1300), 0.03)
put(wt_("Kamu") - 0.26, whoosh(0.4, 500, 1700, 1.4, 0.45), W * 0.45)
for w, d in (("mikrofon,", 0), ("mikrofon,", 0.3), ("aksesibilitas,", 0), ("rekam", 0)): put(wt_(w) + d - 0.06, tick(0.035, 1700), 0.15); put(wt_(w) + d + 0.04, pop(900, 1500, 0.05), 0.08)
put(wt_("rekam") - 0.06, square_blips([880, 660]), 0.035)
put(st("s09") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s09 data: flap, zone + provider, voice bars, teks, lock chip, packets, send across the border, provider lights, tip
put(st("s09") + 0.02, flap(), 0.12)
put(wt_("diolah") - 0.04, pop(600, 1100, 0.08), 0.11); put(wt_("Mac,", st("s09")) - 0.06, chime((1046, 1318.5, 1568), 0.7), 0.05)
for w in ("permintaan", "tangkapan"): put(wt_(w) - 0.1, pop(700, 1200, 0.08), 0.12)
put(wt_("dikirim", st("s09")) - 0.06, whoosh(0.7, 500, 3000, 1.2, 0.5), W * 0.7)
for k in range(10): put(wt_("dikirim", st("s09")) - 0.1 + k * 0.05, tick(0.012, 3800), 0.04)
put(wt_("penyedia") - 0.04, pop(400, 800, 0.1), 0.12); put(wt_("penyedia") + 0.02, buzz(0.18), 0.03)
put(wt_("model.", st("s09")) + 0.06, pop(900, 1500, 0.07), 0.1)
put(st("s10") - 0.3, whoosh(0.35, 2400, 700, 1.4, 0.4), W * 0.5); put(st("s10") + 0.02, pop(600, 1000, 0.08), 0.1)
# --- s10 CTA
put(wt_("Komen") - 0.06, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(7): put(wt_("ASISTEN,") - 0.08 + k * 0.06, tick(0.022, 4200), 0.15)
put(wt_("ASISTEN,") + 0.4, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", st("s10")) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("kirim", st("s10")) - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

