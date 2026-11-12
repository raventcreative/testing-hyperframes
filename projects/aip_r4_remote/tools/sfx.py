"""Synthesised SFX bed for the REMOTE reel (tim 3 Claude cari kerja remote) (no samples, no downloads): a STOP stamp + price strikes, 6 prompt blocks snapping in,
a calendar flip + collapse on "capek", Claude chime, the 5-step rail (tick on each step, check on each done), paste / send / build /
typing / copy clicks, the s10 tear + crumple, the CTA (MASTER typing, heart, plane, DM chime). Deterministic. Writes assets/audio/sfx.wav.
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
def bell(dur=0.9):
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate((1568, 2349, 3136)):
        x += np.sin(2 * np.pi * f * t) * np.exp(-t * (4 + 2 * k)) * (0.8 ** k)
    x *= 0.75 + 0.25 * np.sin(2 * np.pi * 11 * t)
    return x / np.abs(x).max()

st = lambda i: S[i]["start"]
# --- s01 hook: seats bump, three flips, Claude chime, job lines, connectors, the "Kerja remote" pill slams
put(0.02, pop(500, 760, 0.08), 0.08)
for k in range(3): put(wt("tim") - 0.06 + k * 0.05, tick(0.025, 2600 + 200 * k), 0.1)
tI, tT = wt("isi"), wt("tiga")
for k in range(3):
    tf = tI + 0.02 + k * ((tT + 0.12 - tI) / 2); put(tf, flap(), 0.13); put(tf + 0.14, pop(700 + 120 * k, 1100 + 120 * k, 0.07), 0.12)
put(wt("Claude,") - 0.03, chime((1318.5, 1760, 2637), 1.0), 0.07)
for k in range(3): put(wt("tugasnya") - 0.04 + k * 0.12, pop(900 + 80 * k, 1300 + 80 * k, 0.05), 0.07)
put(wt("nyariin") - 0.02, whoosh(0.45, 600, 2400, 1.3, 0.4), W * 0.5)
put(wt("kerja") - 0.12, pop(500, 900, 0.09), 0.13)
put(wt("remote.") - 0.05, boom(0.4, 150, 60), 0.22); put(wt("remote.") + 0.02, chime((1568, 2093, 2637), 0.9), 0.06)
put(st("s02") - 0.3, whoosh(0.4, 2000, 600, 1.3, 0.35), W * 0.6)
# --- s02 pain: search typing, battery drains, "capek", tabs pile up, apply hammering, empty inbox
put(st("s02") + 0.02, whoosh(0.35, 500, 2000, 1.3, 0.4), W * 0.5)
typing(wt("nyari") - 0.1, wt("remote", st("s02") + 0.9) + 0.25, 0.08, 18)
tI = wt("itu"); put(tI - 0.35, pop(700, 1100, 0.07), 0.1)
put(tI - 0.15, square_blips([880, 740, 620, 520, 440, 370], 0.11), 0.05)
put(wt("capek") - 0.04, buzz(0.3), 0.05); put(wt("capek") - 0.02, boom(0.45, 120, 50), 0.16)
for k in range(4): put(wt("banget.") + k * 0.09, tick(0.02, 1800), 0.08)
put(wt("capek") + 0.25, pop(600, 260, 0.12), 0.08)
tW0 = wt("Buka") - 0.08; dW = (wt("satu-satu,") + 0.3 - tW0) / 8
for k in range(8): put(tW0 + k * dW, whoosh(0.16, 900, 2400, 1.6, 0.3), W * 0.25); put(tW0 + k * dW + 0.1, pop(650 + 60 * k, 1000 + 60 * k, 0.05), 0.09)
tA, tB = wt("apply"), wt("berkali-kali,")
put(tA - 0.35, pop(800, 1300, 0.07), 0.08)
for t in [tA - 0.02, tA + 0.2, tB + 0.12, tB + 0.34, tB + 0.56]:
    put(t, tick(0.03, 2100), 0.2); put(t + 0.04, whoosh(0.3, 900, 3000, 1.5, 0.35), W * 0.3); put(t + 0.38, pop(1000, 1500, 0.05), 0.08)
tY = wt("yang", st("s02") + 6)
put(tY - 0.1, whoosh(0.45, 2200, 700, 1.2, 0.4), W * 0.6)
for k in range(5): put(wt("bales") - 0.1 + k * 0.07, tick(0.02, 3000), 0.06)
put(wt("dikit") - 0.02, pop(420, 180, 0.18), 0.18); put(wt("dikit"), buzz(0.2), 0.03)
for k in range(5): put(wt("banget.", wt("dikit")) - 0.2 + k * 0.034, tick(0.015, 2200), 0.05)
put(st("s03") - 0.27, whoosh(0.35, 1800, 600, 1.3, 0.35), W * 0.5)
# --- s03 one command: terminal pops in, /loker-remote typing, Enter, the team launches and lights up
put(st("s03") + 0.02, pop(500, 900, 0.09), 0.1)
typing(wt("ketik") - 0.08, wt("perintah,") - 0.12, 0.12, 26)
put(wt("perintah,") + 0.02, tick(0.04, 1500), 0.3); put(wt("perintah,") + 0.04, pop(400, 200, 0.1), 0.15)
put(wt("perintah,") + 0.15, chime((1568, 2093), 0.6), 0.04)
for k in range(3): put(wt("dan", st("s03")) + k * 0.1, rise(0.32, 400 + 100 * k, 1500 + 100 * k), 0.035); put(wt("dan", st("s03")) + k * 0.1 + 0.3, pop(800 + 150 * k, 1300 + 150 * k, 0.06), 0.11)
put(wt("langsung", st("s03")) - 0.05, chime((1046, 1318, 1568, 2093), 1.1), 0.08)
put(st("s04") - 0.34, whoosh(0.35, 1600, 500, 1.3, 0.35), W * 0.4)
# --- s04 Claude 1 crawls the sites and collects listings
for k in range(8): put(st("s04") + k * 0.035, tick(0.02, 2400 + 120 * k), 0.06)
put(wt("pertama") - 0.06, tick(0.03, 2000), 0.16); put(wt("pertama"), pop(700, 1100, 0.07), 0.1)
tH0 = wt("keliling") - 0.08; dH = (wt("loker,") + 0.32 - tH0) / 8
for k in range(8): put(tH0 + k * dH, tick(0.028, 2200 + 180 * k), 0.15); put(tH0 + k * dH + 0.03, pop(1200 + 60 * k, 1700 + 60 * k, 0.04), 0.06)
tN = wt("ngumpulin"); dN = (wt("remote", tN) + 0.1 - tN) / 6
for k in range(6): put(tN - 0.12 + k * dN, whoosh(0.3, 2400, 900, 1.6, 0.3), W * 0.3); put(tN - 0.12 + k * dN + 0.42, pop(500 + 50 * k, 800 + 50 * k, 0.06), 0.11)
put(wt("ada.") - 0.1, pop(900, 1500, 0.08), 0.12)
# --- s05 Claude 2 filters: criteria pills, scan sweeps, rejects (buzz), scam stamp, into the bin, survivors check
put(wt("kedua") - 0.01, pop(1100, 1700, 0.06), 0.12); put(wt("kedua") + 0.02, tick(0.03, 2000), 0.12)
for k in range(3): put(wt("nyaring:") - 0.3 + k * 0.07, pop(700 + 80 * k, 1100 + 80 * k, 0.06), 0.09)
for t in [wt("nyaring:") + 0.05, wt("cocok") - 0.1, wt("dikerjain") - 0.1, wt("mencurigakan") - 0.25]: put(t, whoosh(0.55, 700, 2600, 2.2, 0.5), W * 0.25)
for t in [wt("cocok") - 0.05, wt("Indonesia,") - 0.25, wt("mencurigakan") - 0.05]: put(t + 0.05, pop(1200, 1900, 0.06), 0.12)
for t in [wt("skill"), wt("Indonesia,"), wt("mencurigakan") + 0.1]: put(t - 0.04, buzz(0.18), 0.045); put(t - 0.02, pop(380, 200, 0.1), 0.12)
put(wt("mencurigakan") + 0.13, boom(0.35, 160, 70), 0.18)
for n in range(3): put(wt("dibuang.") - 0.12 + n * 0.08, whoosh(0.32, 2000, 600, 1.4, 0.3), W * 0.35); put(wt("dibuang.") + 0.24 + n * 0.08, pop(300, 150, 0.1), 0.14)
for q in range(3): put(wt("dibuang.") + 0.56 + q * 0.07, pop(1300 + 100 * q, 2000 + 100 * q, 0.05), 0.1)
# --- s06 Claude 3 writes: toss into chip 3, tabs, CV + cover letter writing, KHUSUS stamp, per-listing swaps
for q in range(3): put(wt("lolos") - 0.05 + q * 0.05, pop(900, 1400, 0.05), 0.07)
for q in range(3): put(wt("dilempar") - 0.08 + q * 0.12, whoosh(0.4, 600, 2600, 1.4, 0.4), W * 0.35); put(wt("dilempar") + 0.36 + q * 0.12, tick(0.03, 2600), 0.1)
put(wt("ketiga.") - 0.03, pop(1100, 1700, 0.06), 0.12); put(wt("ketiga.") + 0.02, tick(0.03, 2000), 0.12)
for q in range(3): put(wt("ketiga.") + 0.1 + q * 0.07, tick(0.022, 2800), 0.07)
put(wt("Dia") - 0.1, whoosh(0.35, 500, 1800, 1.3, 0.4), W * 0.4)
put(wt("bikinin", st("s06")) - 0.05, scribble(wt("CV") + 0.35 - wt("bikinin", st("s06"))), 0.08)
put(wt("cover") - 0.2, whoosh(0.35, 700, 2200, 1.4, 0.4), W * 0.35)
put(wt("cover") + 0.05, scribble(wt("khusus") + 0.05 - wt("cover")), 0.07)
put(wt("khusus") - 0.12, boom(0.35, 170, 70), 0.2); put(wt("khusus") - 0.1, pop(300, 140, 0.1), 0.12)
for t in [wt("tiap", st("s06")) - 0.06, wt("lowongan.") + 0.12]: put(t, flap(), 0.1)
for t in [wt("khusus") - 0.05, wt("tiap", st("s06")) - 0.06, wt("lowongan.") + 0.12]: put(t + 0.18, pop(1300, 2000, 0.05), 0.1)
put(wt("lowongan.") + 0.45, chime((1318.5, 1760, 2349), 0.8), 0.06)
# --- s07 the board: chips dive in, page opens, rows slide, "satu halaman", "pribadi" stamp
for i in range(3): put(wt("semuanya") - 0.12 + i * 0.08, whoosh(0.4, 2400, 800, 1.5, 0.35), W * 0.3); put(wt("semuanya") + 0.28 + i * 0.08, pop(900 + 100 * i, 1400 + 100 * i, 0.05), 0.09)
put(st("s07") + 0.02, whoosh(0.5, 400, 1600, 1.2, 0.5), W * 0.5)
for q in range(3): put(wt("semuanya") + 0.12 + q * ((wt("masuk") + 0.1 - wt("semuanya")) / 3), pop(600 + 100 * q, 1000 + 100 * q, 0.07), 0.11)
for i in range(3): put(wt("masuk") + 0.05 + i * 0.07, tick(0.02, 3000), 0.06)
put(wt("satu", st("s07")), tick(0.03, 2200), 0.14); put(wt("halaman,"), boom(0.4, 140, 70), 0.1)
put(wt("pribadi.") - 0.1, boom(0.3, 180, 80), 0.16); put(wt("pribadi.") - 0.08, pop(320, 160, 0.1), 0.1)
# --- s08 pick + apply: popover, gold "paling cocok", click with sparks, toast
put(st("s08") + 0.05, whoosh(0.5, 500, 1300, 1.2, 0.5), W * 0.25)
put(wt("cek,") - 0.02, pop(800, 1300, 0.07), 0.1)
put(wt("paling") - 0.1, chime((1568, 2093, 2637), 0.8), 0.06); put(wt("cocok,", wt("paling")) - 0.1, pop(1000, 1600, 0.07), 0.1)
put(wt("apply.") - 0.04, tick(0.035, 1900), 0.26); put(wt("apply.") - 0.02, pop(500, 300, 0.08), 0.12)
put(wt("apply.") + 0.05, chime((2093, 2637, 3136), 0.7), 0.05); put(wt("apply.") + 0.12, pop(800, 1200, 0.07), 0.08)
# --- s09 CTA
put(wt("Mau") - 0.02, whoosh(0.45, 1800, 500, 1.3, 0.4), W * 0.5); put(wt("cobain?") - 0.02, pop(700, 1200, 0.08), 0.12)
put(wt("Komen") - 0.3, whoosh(0.4, 400, 1800, 1.3, 0.45), W * 0.5)
tR = wt("REMOTE,")
for k in range(6): put(tR - 0.36 + k * 0.084, tick(0.022, 4200), 0.14)
put(tR + 0.12, pop(900, 1600, 0.1), 0.15)
put(wt("aku", tR) - 0.01, tick(0.03, 2000), 0.2); put(wt("aku", tR) + 0.06, whoosh(0.5, 700, 3600, 1.2, 0.45), W * 0.9)
put(wt("DM.") - 0.12, pop(800, 1300, 0.07), 0.1); put(wt("DM.") + 0.08, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.15, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
