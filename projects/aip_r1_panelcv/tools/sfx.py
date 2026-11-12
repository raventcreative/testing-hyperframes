"""Synthesised SFX bed for the R1 PANEL CV reel (no samples, no downloads): 7 judge cards dropping into the panel, 7 TOLAK stamps, 36
applications sent + rejected, the ATS scan + verdicts + barrier, the hiring manager's pen + decision, 5 locked booths + lenses + quote
swipes, notes collected + the rewrite (a chime per fixed note), the certificate struck + torn, the timeline, the CTA. Deterministic.
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
w = lambda txt, after=0.0: wt(txt, after)
# --- s01 hook: the panel fills up, 7 stamps
put(0.02, rise(0.6, 300, 1200), 0.05); put(w("panel") - 0.02, chime((1318.5, 1760), 0.6), 0.04)
order = [4, 3, 5, 2, 6, 1, 7]
for q in range(7): t = w("7") - 0.1 + q * 0.055 + 0.26; put(t - 0.18, whoosh(0.22, 2200, 700, 1.6, 0.3), W * 0.25); put(t, pop(520 + 40 * q, 260, 0.08), 0.12); put(t + 0.01, tick(0.02, 2600), 0.06)
put(w("Claude.") - 0.02, chime((1046, 1318, 1568), 1.0), 0.06)
put(w("Tugasnya") - 0.06, whoosh(0.5, 500, 2600, 1.4, 0.5), W * 0.5)
for i in range(7): t = w("nolak") - 0.06 + i * 0.075 + 0.085; put(t, boom(0.26, 210, 90), 0.12); put(t, pop(320, 140, 0.1), 0.1)
put(w("kamu.") - 0.1, pop(800, 1300, 0.09), 0.12)
# --- s02 applications: 36 sent, all rejected, no reason
put(st("s02") + 0.15, whoosh(0.55, 2000, 500, 1.3, 0.4), W * 0.6)
t0, t1 = w("Soalnya,") + 0.85, w("lowongan,") + 0.4
for k in range(36): put(t0 + (t1 - t0) * k / 35, tick(0.016, 3000 + 40 * (k % 9)), 0.07)
put(t1 + 0.05, pop(700, 1200, 0.09), 0.12)
f0, f1 = w("tapi") - 0.05, w("tahu", 9) - 0.05
for k in range(11): put(f0 + (f1 - f0) * k / 10, flap(), 0.045)
put(w("dikasih") - 0.24, whoosh(0.5, 400, 1800, 1.2, 0.5), W * 0.6)
put(w("kenapa", 9) - 0.04, pop(260, 120, 0.14), 0.18); put(w("kenapa", 9) - 0.02, buzz(0.18), 0.04)
for k in range(6): put(w("ditolak.") + 0.02 + k * 0.06, tick(0.02, 1800 + 200 * (k % 2)), 0.06)
put(st("s03") - 0.36, whoosh(0.4, 1800, 600, 1.4, 0.4), W * 0.4)
# --- s03 ATS
put(st("s03") + 0.02, whoosh(0.6, 400, 1800, 1.2, 0.5), W * 0.6)
put(w("pertama") - 0.1, chime((1568, 2093), 0.6), 0.05); put(w("pertama") + 0.05, pop(700, 1100, 0.08), 0.1)
for i in range(4): put(w("ATS,") - 0.05 + i * 0.08, pop(900 + 90 * i, 1300 + 90 * i, 0.05), 0.08)
s0, s1 = w("penyaring") - 0.12, w("otomatis") + 0.5
put(s0, zap(0.45), 0.04)
for k in range(16): put(s0 + (s1 - s0) * k / 15, tick(0.014, 4600), 0.04)
for i, ok in enumerate([0, 0, 0, 1]):
    t = [s0 + 0.18, s1 - 0.18, s1 - 0.1, s1 - 0.02][i]
    if ok: put(t, chime((1568, 2093), 0.5), 0.05)
    else: put(t, buzz(0.12), 0.035); put(t, tick(0.03, 1200), 0.1)
put(w("sebelum", 13) + 0.2, boom(0.24, 180, 80), 0.16); put(w("sebelum", 13) + 0.22, tick(0.04, 1400), 0.16)
put(w("dibaca") - 0.05, pop(500, 900, 0.09), 0.12)
for k in range(4): put(w("manusia.") + k * 0.05, tick(0.02, 1300), 0.08)
# --- s04 hiring manager
put(st("s04") + 0.02, whoosh(0.45, 2400, 700, 1.4, 0.35), W * 0.55)
put(w("kedua") - 0.1, chime((1318.5, 1760), 0.6), 0.05); put(w("kedua") + 0.05, pop(700, 1100, 0.08), 0.1)
put(w("hiring") + 0.05, scribble(w("manager.") + 0.45 - w("hiring") - 0.05), 0.09)
put(w("Kamu", 18) - 0.27, whoosh(0.45, 600, 2200, 1.3, 0.45), W * 0.5)
for t in (w("dipanggil") - 0.1, w("dipanggil")): put(t, tick(0.025, 2200), 0.1)
put(w("interview,") - 0.08, pop(800, 1300, 0.08), 0.12); put(w("atau", 20) - 0.1, tick(0.03, 1800), 0.12)
put(w("nggak?") - 0.06, whoosh(0.2, 2000, 900, 1.6, 0.2), W * 0.3); put(w("nggak?") + 0.05, boom(0.28, 200, 90), 0.16); put(w("nggak?") + 0.06, buzz(0.2), 0.04)
# --- s05 five readers
put(st("s05") + 0.02, whoosh(0.4, 2000, 600, 1.4, 0.4), W * 0.5)
put(w("5") + 0.05, whoosh(0.6, 500, 2600, 1.2, 0.5), W * 0.6)
for i in range(5): put(w("5") + 0.4 + abs(i - 2) * 0.05, pop(600 + 70 * i, 300, 0.07), 0.08)
for i in range(5): put(w("sendiri-sendiri,") + 0.02 + i * 0.06, tick(0.03, 1500 + 100 * i), 0.13)
for i in range(5): put(w("kacamata") - 0.1 + i * 0.07, chime((1760 + 120 * i, 2349 + 120 * i), 0.4), 0.025)
for t in (w("calon"), w("sesama"), w("CEO.")):
    put(t - 0.3, whoosh(0.3, 1800, 900, 1.6, 0.3), W * 0.35); put(t - 0.1, pop(700, 1100, 0.08), 0.12)
# --- s06 collect + rewrite
put(st("s06") + 0.12, whoosh(0.5, 600, 2400, 1.3, 0.45), W * 0.6); put(w("Semua") + 0.3, boom(0.3, 160, 70), 0.14)
for q in range(7): t = w("alasan") - 0.15 + q * 0.11; put(t + 0.05, whoosh(0.24, 2600, 1000, 1.8, 0.3), W * 0.25); put(t + 0.45, pop(900 + 60 * q, 1400 + 60 * q, 0.05), 0.08)
put(w("dikumpulin.") - 0.1, pop(500, 900, 0.09), 0.1)
typing(w("tulis") - 0.05, 32.9, 0.07, 18)
FIX = {4: 30.95, 7: 31.4, 6: 31.45, 2: 31.85, 3: 32.3, 5: 32.35, 1: 32.75}
for k, t in FIX.items(): put(t, chime((1568 + 40 * k, 2093 + 40 * k), 0.45), 0.035); put(t, tick(0.02, 3200), 0.08)
put(w("dibenerin.") - 0.06, rise(0.4, 600, 1500), 0.05); put(w("dibenerin.") + 0.02, chime((1318.5, 1760, 2093, 2637), 1.2), 0.08)
# --- s07 honest
put(st("s07") + 0.02, whoosh(0.4, 2000, 700, 1.4, 0.4), W * 0.5)
put(w("bukan") - 0.32, whoosh(0.5, 400, 1600, 1.2, 0.5), W * 0.5)
put(w("jaminan") - 0.02, whoosh(0.22, 3000, 1200, 2.0, 0.2), W * 0.4)
put(w("diterima,") - 0.0, boom(0.3, 200, 80), 0.2); put(w("diterima,") + 0.01, pop(300, 140, 0.12), 0.14)
put(w("ya.") - 0.02, rip(0.55), 0.12)
put(w("Tapi") - 0.08, pop(600, 1000, 0.09), 0.12)
put(w("tahu", 36) - 0.02, chime((1568, 2093, 2637), 0.8), 0.06)
put(w("kenapa", 36) - 0.05, whoosh(0.5, 900, 2600, 1.6, 0.4), W * 0.4)
put(w("ditolak,") - 0.04, pop(800, 1200, 0.07), 0.1)
put(w("HRD") - 0.2, pop(500, 800, 0.09), 0.12); put(w("nolak.", 39) - 0.1, tick(0.04, 1600), 0.12)
put(st("s08") - 0.32, whoosh(0.4, 1800, 600, 1.4, 0.4), W * 0.5)
# --- s08 CTA
put(w("Mau") - 0.14, whoosh(0.45, 600, 2200, 1.4, 0.5), W * 0.6)
put(w("workflow-nya?") + 0.25, pop(700, 1100, 0.07), 0.1)
put(w("Komen") - 0.22, whoosh(0.35, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(2): put(w("CV,") - 0.06 + k * 0.09, tick(0.022, 4200), 0.16)
put(w("aku", 41) - 0.1, pop(900, 1600, 0.1), 0.15)
put(w("kirim", 41) - 0.05, whoosh(0.7, 700, 3600, 1.2, 0.5), W)
put(w("DM.") - 0.02, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.2, chime((1046, 1568, 2093, 2637), 1.4), 0.06)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
