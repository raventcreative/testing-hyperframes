"""Synthesised SFX bed for the LAMARANKERJA reel (InstaJob remake; no samples, no downloads): a night bed (soft chimes, Zzz ticks), the
clock flip, paper-plane whooshes, UI pops on every routed channel / setting, typing ticks, a switch click on "matiin", a dawn rise, CTA.
Deterministic (seeded). Writes assets/audio/sfx.wav (48 kHz mono, full reel length).
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
# --- s01 hook: night, the clock flips to 02:01, the CV pops, paper planes fly into the lit offices ---
put(0.02, whoosh(0.6, 200, 900, 1.0, 0.25), W * 0.5)
for k in range(6): put(0.05 + k * 0.6, tick(0.02, 5200 - 300 * (k % 3)), 0.035)            # Zzz
put(2.2, flap(), 0.24); put(2.36, tick(0.03, 1800), 0.12)                                   # flip 02:00 -> 02:01
put(wt("CV-mu") - 0.02, pop(600, 1100, 0.09), 0.15)
for i in range(4): put(wt("keliling") + 0.05 + i * 0.13, whoosh(0.32, 700, 3000, 1.6, 0.35), W * 0.55)
for i in range(7): put(wt("kantor.") - 0.05 + i * 0.06, pop(1100 + i * 70, 1500 + i * 70, 0.05), 0.07)
put(wt("kantor.") + 0.3, chime((1568, 2093), 0.8), 0.05)
# --- s02: InstaJob wakes up, scans, ticks the matches, sends ---
put(st("s02") - 0.25, whoosh(0.45, 400, 2400), W * 0.8)
put(wt("Namanya") - 0.08, boom(0.35, 200, 90), 0.12)
put(wt("InstaJob.") - 0.02, chime((1318, 1760, 2349), 1.0), 0.07); put(wt("InstaJob.") + 0.02, pop(700, 1200, 0.08), 0.12)
for i in range(10): put(wt("nyariin") + i * 0.07, tick(0.02, 4800), 0.05)                     # scan
for i in range(3): put(wt("pas,") - 0.02 + i * 0.1, pop(900 + i * 120, 1400 + i * 120, 0.06), 0.11)
for i in range(3): put(wt("ngirim") + i * 0.14, whoosh(0.35, 900, 3600, 1.5, 0.35), W * 0.6)
for i in range(3): put(wt("otomatis.") + 0.05 + i * 0.12, pop(1000, 1600, 0.06), 0.1)
# --- s03: routing hub ---
put(st("s03") - 0.25, whoosh(0.45, 2200, 500, 1.2, 0.35), W * 0.9)
put(wt("email,") - 0.02, pop(600, 1000, 0.09), 0.14)
for w in ["LinkedIn,", "Glints,", "Jobstreet,", "Indeed."]: put(wt(w) - 0.02, pop(800, 1300, 0.08), 0.13); put(wt(w) + 0.05, whoosh(0.25, 1500, 3500, 2.0, 0.2), W * 0.3)
put(wt("Indeed.") + 0.25, chime((1568, 2093), 0.7), 0.05)
# --- s04: preferences typed once ---
put(st("s04") - 0.25, whoosh(0.45, 400, 2200), W * 0.8)
put(wt("sekali,") - 0.02, tick(0.03, 2000), 0.2)
typing(wt("posisi,") - 0.05, wt("posisi,") + 0.55, 0.1, 22); typing(wt("lokasi,") - 0.05, wt("lokasi,") + 0.4, 0.1, 22)
put(wt("kerja,", st("s04")) - 0.02, tick(0.03, 2400), 0.2); put(wt("kerja,", st("s04")) + 0.02, pop(700, 1100, 0.07), 0.1)
put(wt("batas") - 0.02, rise(0.7, 300, 1300), 0.06)
put(wt("hari.") + 0.05, tick(0.03, 2000), 0.2); put(wt("hari.") + 0.12, chime((1318, 1760), 0.7), 0.05)
# --- s05: the switch goes OFF ---
put(st("s05") - 0.2, whoosh(0.4, 800, 2600, 1.3, 0.4), W * 0.7)
put(wt("matiin") - 0.02, tick(0.04, 1500), 0.3); put(wt("matiin") + 0.02, boom(0.3, 180, 80), 0.16)
put(wt("matiin") + 0.1, whoosh(0.5, 1600, 300, 1.2, 0.3), W * 0.5)
# --- s06: dawn, the interview invite, the CV gets polished ---
put(st("s06") - 0.1, rise(1.3, 220, 880), 0.07); put(st("s06") + 0.9, chime((1046, 1318, 1568), 1.4), 0.06)
put(wt("wawancaranya") - 0.05, whoosh(0.4, 500, 2000, 1.4, 0.4), W * 0.6); put(wt("wawancaranya") + 0.2, pop(700, 1100, 0.08), 0.12)
put(wt("kamu", st("s06")) - 0.02, pop(900, 1400, 0.07), 0.1)
for i in range(3): put(wt("rapiin") + 0.1 + i * 0.25, pop(900 + i * 150, 1500 + i * 150, 0.06), 0.11)
put(wt("CV-mu.") + 0.15, whoosh(0.5, 2000, 6000, 2.0, 0.3), W * 0.5); put(wt("CV-mu.") + 0.2, chime((1760, 2349, 2637), 1.0), 0.06)
# --- s07 CTA ---
put(st("s07") - 0.2, whoosh(0.35, 600, 2000, 1.4, 0.5), W * 0.6)
for i in range(5): put(wt("KERJA,") - 0.02 + i * 0.06, tick(0.022, 4200), 0.14)
put(wt("KERJA,") + 0.35, pop(900, 1600, 0.1), 0.15)
put(wt("kirim") - 0.02, whoosh(0.7, 700, 3600, 1.2, 0.5), W)
put(wt("DM.") - 0.02, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.5, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
