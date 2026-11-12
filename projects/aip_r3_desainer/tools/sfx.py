"""Synthesised SFX bed for the R3 DESAINER reel (adapted from the IGAGENT bed) (no samples, no downloads): Claude flare, lanyard badges dropping + swinging, a GRATIS stamp,
the 13-badge team wall, an x-ray scan + leaderboard sort, a slot machine for the hooks + score stamps, a 12-segment ring fill, the week
board, the 9-card deal, an eraser, paste/install/"selesai", a blocked switch + lock + DRAF stamps, the CTA. Deterministic.
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
# --- s01 hook: generic page, critique tags + GENERIK stamp, 5 tiles dealt, GRATIS pill, Claude disc + pen loop
put(0.02, rise(0.6, 300, 1200), 0.05); put(wt("Website") - 0.05, pop(500, 900, 0.08), 0.1)
put(wt("AI") - 0.03, chime((1760, 2349), 0.5), 0.04)
for k in range(3): put(wt("kelihatan") - 0.05 + k * 0.21, pop(700 + 120 * k, 380, 0.09), 0.13)
put(wt("generik?") - 0.04, boom(0.45, 150, 60), 0.3); put(wt("generik?") - 0.02, pop(300, 140, 0.12), 0.2)
for k in range(5): put(wt("Lima") - 0.06 + k * 0.085, whoosh(0.22, 1800, 700, 1.6, 0.25), W * 0.35); put(wt("Lima") + 0.12 + k * 0.085, tick(0.02, 2200 + 150 * k), 0.08)
put(wt("gratis") - 0.04, pop(800, 1300, 0.08), 0.13); put(wt("gratis") + 0.02, chime((1568, 2093), 0.6), 0.04)
put(wt("Claude") - 0.1, chime((1046, 1318, 1568), 1.1), 0.07); put(wt("Claude") + 0.05, pop(900, 500, 0.1), 0.1)
put(wt("jadi", 5) - 0.08, scribble(0.55), 0.06)
for k in range(4): put(wt("desainer.") + 0.1 + k * 0.06, pop(1000 + 90 * k, 1500 + 90 * k, 0.05), 0.07)
# --- t1 Taste: tile -> header, pocketed tiles, rules ticks, scan reveal
put(st("t1") + 0.0, whoosh(0.5, 600, 2400, 1.2, 0.5), W * 0.6); put(wt("Taste") - 0.1, flap(), 0.1)
for k in range(4): put(st("t1") + 0.1 + k * 0.06, tick(0.018, 3000 + 120 * k), 0.06)
put(wt("dikasih") - 0.1, whoosh(0.4, 2400, 700, 1.4, 0.35), W * 0.5)
for w, a0 in (("aturan", 0), ("desain", 9), ("yang", 9), ("jelas,", 0)): put(wt(w, a0) - 0.03, pop(900, 1500, 0.07), 0.12)
put(wt("jadi", 10) - 0.1, whoosh(0.35, 2400, 900, 1.6, 0.3), W * 0.4)
put(wt("hasilnya") - 0.02, rise(0.95, 400, 1600), 0.05); put(wt("hasilnya") + 0.05, whoosh(0.95, 700, 4200, 1.3, 0.5), W * 0.5)
put(wt("template") - 0.02, chime((1318.5, 1760, 2637), 1.0), 0.06); put(wt("lagi.") - 0.05, chime((2093, 2637), 0.6), 0.04)
# --- t2 Impeccable: header roll, command bar, typing, polish shine, bolder thump, live variants, accept
put(st("t2") + 0.02, flap(), 0.12)
put(wt("Ketik") - 0.5, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
typing(wt("Ketik") - 0.05, wt("Ketik") + 0.42, 0.1, 24); typing(wt("polish") - 0.32, wt("polish") - 0.05, 0.1, 22)
put(wt("polish") + 0.02, tick(0.035, 1500), 0.22); put(wt("polish") + 0.1, whoosh(0.6, 3000, 6000, 2.2, 0.4), W * 0.35)
typing(wt("bolder,") - 0.24, wt("bolder,") - 0.03, 0.1, 30); put(wt("bolder,") + 0.02, tick(0.035, 1500), 0.22); put(wt("bolder,") + 0.06, boom(0.3, 200, 90), 0.16)
put(wt("terus", 16) - 0.12, whoosh(0.35, 1800, 500, 1.4, 0.3), W * 0.4); put(wt("terus", 16) + 0.15, square_blips([880, 1320]), 0.05)
for t in (wt("variasinya") - 0.06, wt("variasinya") + 0.38): put(t, whoosh(0.22, 1500, 3000, 2.0, 0.25), W * 0.4); put(t + 0.1, tick(0.02, 2600), 0.1)
put(wt("langsung") + 0.22, tick(0.03, 1800), 0.25); put(wt("langsung") + 0.42, chime((1568, 2093, 2637), 0.9), 0.06)
# --- t3 Playwright CLI: terminal, browser sessions pop, clicks, scan, camera shutters, warning, fix
put(st("t3") + 0.02, flap(), 0.12)
put(wt("buka") - 0.6, whoosh(0.4, 500, 1800, 1.4, 0.45), W * 0.5)
typing(wt("buka") - 0.28, wt("buka") + 0.2, 0.08, 26); typing(wt("browser", 22) + 0.02, wt("browser", 22) + 0.5, 0.08, 26)
put(wt("browser", 22) + 0.05, pop(600, 1000, 0.08), 0.12); put(wt("sendiri,") - 0.05, pop(700, 1100, 0.08), 0.12)
for k in range(3): put(wt("ngetes") + 0.17 + k * 0.12, tick(0.025, 2000), 0.18)
put(wt("websitenya,") - 0.05, whoosh(0.6, 1200, 3000, 2.0, 0.3), W * 0.3)
for k in range(3):
    t = wt("screenshot") - 0.04 + k * 0.1; put(t, tick(0.02, 5200), 0.22); put(t + 0.03, svf_bp(rng.standard_normal(int(0.06 * SR)), np.full(int(0.06 * SR), 2600.0), 1.2) * np.exp(-np.arange(int(0.06 * SR)) / SR * 60) / 3, 0.5)
for t in (wt("ngecek") - 0.04, wt("ngecek") + 0.12): put(t, pop(900, 1500, 0.07), 0.12)
put(wt("ngecek") + 0.14, buzz(0.18), 0.05); put(wt("ngecek") + 0.6, scribble(0.25), 0.06); put(wt("ngecek") + 0.72, chime((1568, 2093), 0.6), 0.05)
put(st("t4") - 0.2, whoosh(0.3, 2400, 700, 1.4, 0.35), W * 0.4)
# --- t4 Awesome DESIGN.md: file drop, list cascade, highlight run, tokens pop
put(st("t4") + 0.02, flap(), 0.12)
put(wt("Awesome") - 0.25, whoosh(0.45, 2400, 600, 1.4, 0.4), W * 0.6); put(wt("Awesome") + 0.2, boom(0.25, 180, 90), 0.1)
put(wt("Kumpulan") - 0.25, whoosh(0.4, 600, 2000, 1.4, 0.45), W * 0.5)
for k in range(8): put(wt("Kumpulan") + 0.05 + k * 0.07, tick(0.016, 3200 + 80 * k), 0.06)
put(wt("desain", 29), pop(800, 1300, 0.08), 0.1)
for k in range(8): put(wt("website", 30) - 0.05 + k * 0.1, tick(0.014, 4200), 0.05)
for k in range(6): put(wt("warna,") - 0.06 + k * 0.05, pop(900 + 100 * k, 1400 + 100 * k, 0.04), 0.07)
put(wt("font,") - 0.08, pop(500, 900, 0.09), 0.13); put(wt("tombol,") - 0.06, pop(700, 1100, 0.07), 0.1); put(wt("tombol,") + 0.08, pop(800, 1200, 0.07), 0.1)
for k in range(12): put(wt("layout.") - 0.1 + k * 0.022, tick(0.012, 2800 + 90 * k), 0.05)
put(st("t5") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- t5 img2threejs: viewport, photo drop, code lines, build passes, 3D flash, orbit drag, code chip
put(st("t5") + 0.02, flap(), 0.12)
put(wt("img2threejs.") - 0.3, whoosh(0.5, 2400, 600, 1.4, 0.4), W * 0.6); put(wt("img2threejs.") + 0.2, rumble(1.4), 0.03)
put(wt("Kasih") - 0.12, whoosh(0.4, 2000, 500, 1.4, 0.4), W * 0.5); put(wt("Kasih") + 0.32, pop(300, 160, 0.1), 0.15)
for k in range(5): put(wt("Claude", 37) - 0.05 + k * 0.2, tick(0.02, 3000 + 200 * k), 0.08)
put(wt("bangun") - 0.05, square_blips([660, 990]), 0.05); put(wt("jadi", 38) - 0.02, square_blips([880, 1320]), 0.05)
put(wt("3D") - 0.08, zap(0.45), 0.07); put(wt("3D") - 0.05, boom(0.35, 160, 70), 0.18); put(wt("3D") + 0.05, chime((1318.5, 1760, 2637), 1.0), 0.06)
put(wt("interaktif,") - 0.02, whoosh(0.9, 500, 2200, 1.0, 0.5), W * 0.5)
put(wt("cuma") + 0.02, pop(800, 1300, 0.08), 0.12)
put(st("s07") - 0.22, whoosh(0.3, 2000, 600, 1.4, 0.35), W * 0.4)
# --- s07 recap: list rows, GRATIS stamp, open-source seal, fold into the link card
for k in range(5): put(wt("Semuanya") + k * 0.07, flap(), 0.06)
put(wt("gratis", 41) - 0.04, boom(0.45, 150, 60), 0.3); put(wt("gratis", 41) - 0.02, pop(300, 140, 0.12), 0.2)
put(wt("open", 42) - 0.05, pop(800, 1300, 0.08), 0.13)
for k in range(5): put(wt("open", 42) + k * 0.05, pop(1000 + 80 * k, 1500 + 80 * k, 0.04), 0.06)
put(wt("Mau", 43) - 0.12, whoosh(0.4, 2400, 700, 1.4, 0.35), W * 0.5); put(wt("Mau", 43) + 0.2, pop(700, 1100, 0.08), 0.12)
# --- s08 CTA
put(wt("Komen") - 0.2, whoosh(0.4, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(6): put(wt("DESAIN,") - 0.06 + k * 0.065, tick(0.022, 4200), 0.15)
put(wt("DESAIN,") + 0.42, pop(900, 1600, 0.1), 0.15)
put(wt("aku", 44) - 0.08, whoosh(0.7, 700, 3600, 1.2, 0.5), W); put(wt("kirim") - 0.02, pop(600, 1000, 0.08), 0.1)
put(wt("DM.") - 0.06, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.4, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
