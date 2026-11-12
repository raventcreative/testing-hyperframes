"""Synthesised SFX bed for the R11 HARNESS reel (adapted from the R9 YOUTUBE bed) (no samples, no downloads): code lines building the
mini reel, subscription stamps, open-source flare, repo header + MIT stamp, plugin modules clicking in, model chips plugging into the
socket + usage ticks, task typing + agent action checks + permission click, terminal/npx typing + browser open, warning stamps +
safety checks, the CTA. Deterministic.
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
# --- s01 hook: code lines build the mini reel, agent chip, play; subscription card + 12 TAGIH stamps; X + open-source flare
put(0.02, rise(0.6, 300, 1200), 0.05); put(0.05, pop(500, 900, 0.08), 0.1)
typing(0.35, wt_("kode.") - 0.1, 0.05, 14)
for t in (wt_("Reel") + 0.35, wt_("agen") , wt_("AI") + 0.25, wt_("nulis") + 0.2): put(t, pop(700, 1200, 0.07), 0.11)
put(wt_("agen") - 0.06, pop(900, 1500, 0.08), 0.12)
put(wt_("kode.") - 0.08, chime((1318.5, 1760, 2637), 0.9), 0.06); put(wt_("kode.") - 0.06, pop(600, 1100, 0.09), 0.12)
put(wt_("Agen") - 0.24, whoosh(0.4, 2400, 600, 1.4, 0.4), W * 0.7); put(wt_("Agen") + 0.1, boom(0.3, 160, 80), 0.12)
for k in range(12): put(wt_("biasanya") - 0.1 + k * 0.075 + 0.14, tick(0.03, 1500 + 40 * k), 0.13)
put(wt_("langganan,") + 0.1, pop(500, 900, 0.09), 0.12); put(wt_("langganan,") + 0.12, buzz(0.25), 0.03)
put(wt_("yang", 5.5) - 0.1, boom(0.35, 150, 70), 0.2); put(wt_("yang", 5.5) + 0.14, whoosh(0.45, 1800, 400, 1.4, 0.3), W * 0.6)
put(wt_("open") - 0.18, chime((1046, 1318, 1568, 2093), 1.2), 0.08); put(wt_("open") - 0.1, pop(900, 500, 0.1), 0.12)
put(wt_("source.") + 0.04, pop(800, 1300, 0.08), 0.12); put(wt_("source.") + 0.2, pop(900, 1400, 0.07), 0.1)
# --- s02 the tool: header drop, repo card, star pop, MIT stamp, board + plugin modules, GRATIS stamp, socket glow, name spin
put(wt_("Kenalin,") - 0.12, whoosh(0.45, 2400, 600, 1.4, 0.45), W * 0.6); put(wt_("Kenalin,") + 0.4, flap(), 0.1)
put(wt_("DeepSeek") - 0.16, whoosh(0.5, 500, 1800, 1.4, 0.45), W * 0.5); put(wt_("Harness,") + 0.06, pop(700, 1300, 0.08), 0.13)
put(wt_("MIT.") - 0.06, boom(0.25, 180, 80), 0.16); put(wt_("MIT.") - 0.04, tick(0.03, 1600), 0.12)
put(wt_("Harness-nya") - 0.18, whoosh(0.5, 400, 1600, 1.2, 0.5), W * 0.5)
for k in range(4): put(wt_("Harness-nya") + 0.14 + k * 0.09, tick(0.03, 1800 + 200 * k), 0.14)
put(wt_("gratis,") - 0.04, boom(0.25, 180, 80), 0.16); put(wt_("gratis,"), pop(800, 1300, 0.08), 0.1)
put(wt_("otaknya") - 0.06, chime((1568, 2093), 0.6), 0.05)
for k in range(4): put(wt_("kamu", 11) - 0.04 + k * 0.19, tick(0.02, 2600 + 300 * k), 0.1)
put(st("s03") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s03 how it works: flap, window open, task typing, three actions, permission card, click, run
put(st("s03") + 0.02, flap(), 0.12)
put(wt_("Suruh") - 0.2, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
typing(wt_("Suruh") + 0.06, wt_("Suruh") + 1.1, 0.08, 20)
for w in ("ngebaca", "ngubah", "ngejalanin"): put(wt_(w) - 0.12, whoosh(0.25, 800, 2200, 1.4, 0.3), W * 0.35)
put(wt_("file,") + 0.18, pop(800, 1400, 0.07), 0.13); put(wt_("kode,", 16) + 0.14, pop(900, 1500, 0.07), 0.13)
put(wt_("perintah,", 17) + 0.1, square_blips([660, 520]), 0.04)
put(wt_("minta") - 0.12, whoosh(0.35, 600, 2000, 1.4, 0.4), W * 0.5); put(wt_("minta") + 0.1, pop(500, 800, 0.08), 0.1)
put(wt_("aksi"), tick(0.04, 1500), 0.22); put(wt_("aksi") + 0.24, pop(900, 1600, 0.08), 0.14); put(wt_("aksi") + 0.3, chime((1568, 2093), 0.5), 0.05)
put(st("s04") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s04 pick the brain: flap, socket card + options, three chips plug in, usage ticks, key jingle, GRATIS stamp, RAM bar
put(st("s04") + 0.02, flap(), 0.12)
put(st("s04") + 0.06, whoosh(0.45, 500, 1800, 1.4, 0.45), W * 0.5)
for k in range(3): put(st("s04") + 0.18 + k * 0.1, tick(0.02, 2200 + 200 * k), 0.08)
for w, a in (("DeepSeek", 20), ("Claude", 22), ("model", 25)):
    t = wt_(w, a) - 0.12; put(t + 0.02, whoosh(0.4, 900, 2600, 1.4, 0.4), W * 0.45); put(t + 0.42, pop(400, 200, 0.1), 0.18); put(t + 0.44, tick(0.03, 1400), 0.14)
for k in range(6): put(wt_("pemakaian,") - 0.05 + k * 0.15, tick(0.02, 3600 + 150 * (k % 3)), 0.07)
for k in range(6): put(wt_("API", 23) + k * 0.15, tick(0.02, 3600 + 150 * (k % 3)), 0.07)
put(wt_("API", 23) - 0.04, scribble(0.25), 0.04)
put(wt_("gratis", 26) - 0.04, boom(0.25, 180, 80), 0.16); put(wt_("gratis", 26), pop(800, 1300, 0.08), 0.1)
put(wt_("laptopnya") - 0.1, rise(0.7, 300, 900), 0.04)
put(st("s05") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s05 start: flap, terminal open, requirement chip + tick, npx typing + enter, browser opens, key dots, ticks, ready
put(st("s05") + 0.02, flap(), 0.12)
put(wt_("Cara") + 0.08, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
put(wt_("pasang") - 0.06, pop(600, 1000, 0.08), 0.12); put(wt_("terbaru,") + 0.1, pop(900, 1500, 0.07), 0.13)
typing(wt_("jalanin", 30) - 0.04, wt_("jalanin", 30) + 0.8, 0.09, 30)
put(wt_("satu", 30) - 0.04, pop(800, 1400, 0.08), 0.12); put(wt_("perintah,", 31) + 0.3, tick(0.04, 1500), 0.2)
put(wt_("browser") - 0.12, square_blips([880, 1320]), 0.04); put(wt_("kebuka.") - 0.08, whoosh(0.45, 500, 2000, 1.3, 0.45), W * 0.55)
typing(wt_("Isi"), wt_("Isi") + 0.63, 0.07, 22)
put(wt_("key,", 33) + 0.04, pop(900, 1500, 0.07), 0.13); put(wt_("folder,") + 0.02, pop(900, 1500, 0.07), 0.13)
put(wt_("beres.") - 0.04, chime((1318.5, 1760, 2637), 0.9), 0.07); put(wt_("beres."), pop(700, 1200, 0.08), 0.1)
put(st("s06") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s06 safety: flap, status card, warning buzz + stamps, three checks, exit to the link card
put(st("s06") + 0.02, flap(), 0.12)
put(wt_("Catatannya:") + 0.1, whoosh(0.4, 500, 1600, 1.2, 0.45), W * 0.5); put(wt_("Catatannya:") + 0.3, boom(0.3, 140, 70), 0.1)
put(wt_("diaudit") - 0.06, buzz(0.3), 0.05); put(wt_("diaudit") - 0.02, boom(0.25, 180, 80), 0.16); put(wt_("keamanan.") + 0.14, boom(0.25, 160, 70), 0.14)
for w in ("Pakai", "backup", "cek"): put(wt_(w) - 0.16, whoosh(0.3, 700, 2000, 1.4, 0.3), W * 0.4)
for t in (wt_("terpisah,") + 0.24, wt_("dulu,") + 0.12, wt_("diizinkan.") + 0.06): put(t, pop(900, 1600, 0.08), 0.15); put(t + 0.02, tick(0.03, 1500), 0.1)
put(st("s07") - 0.45, whoosh(0.4, 2400, 700, 1.4, 0.4), W * 0.5); put(st("s07") - 0.33, pop(600, 1000, 0.08), 0.1)
# --- s07 CTA
put(wt_("Komen") - 0.06, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(7): put(wt_("NGODING,") - 0.08 + k * 0.055, tick(0.022, 4200), 0.15)
put(wt_("NGODING,") + 0.44, pop(900, 1600, 0.1), 0.15)
put(wt_("aku", 44) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt_("kirim") - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt_("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))

