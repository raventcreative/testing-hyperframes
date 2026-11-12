"""Synthesised SFX bed for the R5 reel "Edit video pakai Claude" (no samples, no downloads): the editor cut + Claude filling the tracks,
the 4 chapter markers landing in the step rail, download/progress/installed, folder + typing + 3 sub-folders, the GRATIS stamp + 4 card
flips + link paste + install ticks, the key + 5 reels + film strip scan + 5 breakdown rows + style-sheet stamp, footage/prompt/storyboard/
revision/render/final, the CTA (EDIT typing, heart, paper plane, DM chime). Deterministic.
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
def w(txt, scene=None):
    t = wt(txt, st(scene) - 0.05 if scene else 0.0)
    assert t is not None, txt
    return t
# --- s01 hook: the editor timeline, the cut, Claude fills the tracks, 4 chapter markers fly into the rail
put(0.02, rise(0.6, 300, 1200), 0.05); put(0.3, chime((1046, 1318, 1568), 1.0), 0.05)
tc = w("edit") + 0.06
put(tc - 0.12, pop(500, 900, 0.07), 0.08); put(tc, tick(0.03, 3200), 0.24); put(tc + 0.09, tick(0.03, 2600), 0.2)
put(tc + 0.2, whoosh(0.3, 900, 300, 1.4, 0.4), W * 0.4); put(tc + 0.32, whoosh(0.35, 600, 1800, 1.4, 0.4), W * 0.5)
put(w("Claude.") - 0.05, chime((1046, 1318, 1568), 1.1), 0.07)
for k in range(3): put(w("Claude.") + 0.02 + k * 0.1, pop(700 + 120 * k, 1100 + 120 * k, 0.06), 0.1)
for k in range(9): put(w("Claude.") + 0.14 + k * 0.05, tick(0.015, 3800 + 80 * k), 0.06)
for k in range(4): put(w("setup-nya,") + 0.08 + k * 0.1 + 0.2, pop(900, 500, 0.06), 0.1)
for k in range(4): put(w("step") - 0.05 + k * 0.09, whoosh(0.4, 700, 2600, 1.6, 0.6), W * 0.3); put(w("step") + 0.37 + k * 0.09, flap(), 0.07)
# --- st1 setup: download, the folder, 3 sub-folders, into Claude
put(st("st1") + 0.0, whoosh(0.45, 400, 1800, 1.2, 0.5), W * 0.5)
put(w("download") + 0.02, tick(0.03, 2200), 0.22)
for k in range(10): put(w("download") + 0.2 + k * 0.06, tick(0.012, 3000 + 90 * k), 0.05)
put(w("desktop.") + 0.04, chime((1318.5, 1760, 2637), 0.9), 0.07); put(w("desktop.") + 0.04, pop(600, 1100, 0.08), 0.12)
put(w("Bikin") - 0.3, whoosh(0.45, 1800, 500, 1.3, 0.4), W * 0.6)
put(w("folder", "st1") - 0.1, pop(400, 900, 0.1), 0.16); put(w("folder", "st1") - 0.05, rise(0.4, 600, 1500), 0.04)
typing(w("AI") - 0.04, w("Editor,") + 0.3, 0.1, 18); put(w("Editor,") + 0.36, tick(0.035, 1500), 0.22)
put(w("isinya") - 0.1, tick(0.02, 2600), 0.18); put(w("isinya") + 0.04, tick(0.02, 2600), 0.18); put(w("isinya") + 0.2, whoosh(0.4, 500, 2600, 1.2, 0.4), W * 0.6)
for k in range(3): put(w("tiga:") - 0.1 + k * 0.08, pop(1000 + 100 * k, 1400 + 100 * k, 0.05), 0.08)
for x in ("raw", "referensi,", "export."): put(w(x, "st1") - 0.02, boom(0.22, 220, 110), 0.12); put(w(x, "st1"), pop(500, 260, 0.08), 0.12)
put(w("Terus") + 0.05, whoosh(0.4, 2200, 600, 1.4, 0.4), W * 0.6)
put(w("buka") - 0.12, whoosh(0.45, 400, 1600, 1.2, 0.5), W * 0.6)
put(w("folder", "st1") + 5.7, whoosh(0.42, 800, 2600, 1.6, 0.4), W * 0.4)
put(w("itu") + 0.05, tick(0.03, 1800), 0.2); put(w("itu") + 0.08, chime((1568, 2093), 0.7), 0.05)
put(w("Claude.", "st1") - 0.1, whoosh(0.6, 1200, 2600, 2.0, 0.5), W * 0.25)
# --- st2 tools: deal, GRATIS, flips, sticker, links, ticks
put(w("Dua:") - 0.05, whoosh(0.45, 1800, 400, 1.2, 0.4), W * 0.6)
for k in range(4): put(w("Dua:") + 0.12 + k * 0.1, flap(), 0.08)
put(w("gratis.") - 0.08, boom(0.45, 150, 60), 0.3); put(w("gratis.") - 0.06, pop(300, 140, 0.12), 0.2)
put(w("HyperFrames") - 0.42, whoosh(0.36, 1200, 3000, 1.6, 0.6), W * 0.4)
for x in ("HyperFrames", "FFmpeg", "Whisper", "yt-dlp"): put(w(x) - 0.16, flap(), 0.1); put(w(x) - 0.02, pop(800, 1300, 0.07), 0.1)
put(w("aku", "st2") - 0.06, boom(0.25, 200, 100), 0.14); put(w("aku", "st2") - 0.04, pop(1200, 700, 0.08), 0.12)
for k in range(2): put(w("motong") - 0.05 + k * 0.18, tick(0.03, 3000), 0.18)
for k in range(4): put(w("Tempel") - 0.12 + k * 0.1, whoosh(0.4, 1800, 700, 1.6, 0.6), W * 0.3); put(w("Tempel") + 0.22 + k * 0.1, pop(900 + 80 * k, 1300 + 80 * k, 0.05), 0.08)
put(w("GitHub-nya,") + 0.25, tick(0.03, 2000), 0.2); put(w("GitHub-nya,") + 0.27, whoosh(0.35, 700, 2400, 1.4, 0.4), W * 0.4)
for k in range(4): put(w("pasang.") - 0.25 + k * 0.13, pop(900 + 150 * k, 1400 + 150 * k, 0.05), 0.1)
put(w("pasang.") + 0.3, chime((1568, 2093, 2637), 0.9), 0.07)
# --- st3 style: the key, 5 reels, the strip, the breakdown, the style sheet stamp
put(st("st3") + 0.02, rise(0.5, 400, 1100), 0.05)
for k in range(5): put(st("st3") + 0.15 + k * 0.08, pop(1100 + 90 * k, 1500 + 90 * k, 0.04), 0.06)
put(w("kuncinya:") - 0.02, tick(0.04, 1200), 0.24); put(w("kuncinya:") + 0.1, chime((784, 1046, 1568), 1.0), 0.06)
put(w("kasih") - 0.2, whoosh(0.35, 2000, 600, 1.4, 0.4), W * 0.4)
for k in range(3): put(w("tiga") - 0.12 + k * 0.08, whoosh(0.3, 600, 1800, 1.6, 0.5), W * 0.3)
for k in range(2): put(w("lima") - 0.12 + k * 0.08, whoosh(0.3, 600, 1800, 1.6, 0.5), W * 0.3)
for k in range(5): put(w("suka.") - 0.08 + k * 0.06, pop(1300 + 100 * k, 1900 + 100 * k, 0.05), 0.08)
put(w("Claude", "st3") - 0.1, whoosh(0.4, 1400, 500, 1.4, 0.4), W * 0.5)
put(w("pecah") - 0.02, rip(0.3), 0.06)
for k in range(6): put(w("pecah") + 0.05 + k * 0.04, tick(0.015, 3000 + 120 * k), 0.06)
put(w("frame,") - 0.1, rise(0.8, 500, 2200), 0.04)
for k in range(6): put(w("frame,") - 0.05 + k * 0.13, tick(0.015, 4400), 0.05)
put(w("lalu") + 0.05, whoosh(0.4, 2000, 600, 1.3, 0.4), W * 0.5)
for k, x in enumerate(("font,", "warna,", "caption,", "transisi,", "sound.")): put(w(x) - 0.08, pop(800 + 110 * k, 1200 + 110 * k, 0.06), 0.11); put(w(x) - 0.02, tick(0.02, 2400), 0.1)
put(w("Hasilnya") - 0.1, whoosh(0.4, 600, 2000, 1.4, 0.4), W * 0.5); typing(w("Hasilnya") + 0.22, w("Hasilnya") + 0.7, 0.08, 18)
put(w("style") - 0.05, boom(0.35, 170, 70), 0.24); put(w("style") - 0.03, pop(300, 140, 0.12), 0.2); put(w("style") + 0.2, chime((1318.5, 1760, 2637), 1.0), 0.07)
# --- st4 edit: footage, prompt, storyboard, revision, render, final
put(st("st4") + 0.0, whoosh(0.45, 2200, 600, 1.4, 0.4), W * 0.5)
put(w("raw", "st4") - 0.1, pop(400, 800, 0.1), 0.14); put(w("raw", "st4") + 0.05, boom(0.2, 220, 110), 0.1)
typing(w("kirim", "st4") - 0.08, w("prompt.") + 0.3, 0.1, 20); put(w("prompt.") + 0.34, tick(0.03, 2000), 0.2)
put(w("Claude", "st4") - 0.2, whoosh(0.45, 700, 2400, 1.4, 0.4), W * 0.5)
for k in range(6): put(w("storyboard") - 0.05 + k * 0.09, pop(900 + 70 * k, 1300 + 70 * k, 0.05), 0.08)
put(w("dulu,") + 0.02, pop(1200, 1600, 0.05), 0.08); put(w("videonya.") + 0.02, tick(0.025, 1600), 0.14)
put(w("pas?") - 0.05, tick(0.02, 3600), 0.1)
typing(w("Bilang") + 0.02, w("gedein.") + 0.12, 0.1, 18); put(w("gedein.") + 0.2, tick(0.03, 2000), 0.2)
for k in range(6): put(w("gedein.") + 0.36 + k * 0.05, pop(600 + 100 * k, 1000 + 100 * k, 0.06), 0.1)
put(w("oke,") - 0.02, chime((1318.5, 1760), 0.6), 0.06); put(w("oke,"), pop(800, 1300, 0.06), 0.1)
put(w("render") - 0.05, whoosh(0.45, 1400, 500, 1.4, 0.4), W * 0.5); put(w("render") + 0.15, rise(w("final.") - w("render") - 0.2, 400, 1600), 0.05)
put(w("final.") - 0.08, boom(0.5, 160, 60), 0.26); put(w("final.") - 0.02, chime((1046, 1318.5, 1568, 2093), 1.3), 0.08)
# --- s06 CTA
put(w("Mau") - 0.05, whoosh(0.45, 600, 2000, 1.4, 0.5), W * 0.5)
for k in range(4): put(w("prompt", "s06") + 0.05 + k * 0.1, flap(), 0.08)
put(w("Komen") - 0.2, whoosh(0.4, 500, 1800, 1.4, 0.5), W * 0.5)
for k in range(4): put(w("EDIT,") - 0.06 + k * 0.07, tick(0.022, 4200), 0.16)
put(w("aku", "s06") - 0.05, pop(900, 1600, 0.1), 0.16)
put(w("kirim", "s06") - 0.04, whoosh(0.7, 700, 3600, 1.2, 0.5), W)
put(w("DM.") - 0.1, chime((1568, 2093), 0.8), 0.07)
put(T["total_sec"] - 1.35, chime((1046, 1568, 2093, 2637), 1.6), 0.07)
x = np.clip(out, -1, 1); x = (x * 32767).astype(np.int16)
f = wave.open(str(P / "assets/audio/sfx.wav"), "wb"); f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(x.tobytes()); f.close()
print("sfx.wav", round(len(x) / SR, 2), "s, peak", round(float(np.abs(out).max()), 3))
