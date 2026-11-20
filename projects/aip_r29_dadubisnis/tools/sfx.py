"""R29 SFX bed (synthesised, deterministic, no samples): dice clacks on every landing (same timing rules as vendor/dice.js),
a rattle for the 100-dice rain and the storm, tray thumps, the giant-die crash, whooshes on wipes / iris / flood, stamp thuds,
card pops on section tabs, counter ticks, a sparkle for the shiny object, success chimes on the sixes, CTA typing + send + DM chime.
Writes assets/audio/sfx.wav (48 kHz mono, quiet: the VO leads). Run: python3 -I tools/sfx.py ."""
import json, sys, wave
from pathlib import Path
import numpy as np
from scipy.signal import butter, sosfilt

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/timing.json").read_text())
SR = 48000; N = int((T["total_sec"] + 1) * SR); out = np.zeros(N)
rng = np.random.default_rng(29)
WD = T["words"]; SC = T["scenes"]
def W(txt, after=0.0):
    for w in WD:
        if w["w"] == txt and w["s"] >= after - 1e-6: return w["s"]
    raise SystemExit("word not found " + txt)
S = lambda n: SC[n - 1]["start"]
def put(t, x, g=1.0):
    i = int(t * SR)
    if i < 0 or i >= N: return
    j = min(N, i + len(x)); out[i:j] += g * x[: j - i]
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], btype="band", fs=SR, output="sos"), x)
def lp(x, f): return sosfilt(butter(2, f, btype="low", fs=SR, output="sos"), x)
def norm(x): return x / (np.abs(x).max() + 1e-9)
def clack(bright=1.0):
    n = int(0.09 * SR); t = np.arange(n) / SR
    a = bp(rng.standard_normal(n), 1800, 5200) * np.exp(-t * 90)
    b = np.sin(2 * np.pi * (520 + 200 * rng.random()) * t) * np.exp(-t * 60) * 0.5
    th = lp(rng.standard_normal(n), 300) * np.exp(-t * 40) * 1.5
    return norm(bright * a + b + th)
def land(t, g=0.5, hops=2):
    put(t, clack(), g)
    for k in range(hops): put(t + 0.17 + 0.12 * k, clack(0.7), g * 0.45 / (k + 1))
def whoosh(dur=0.5, lo=300, hi=3000):
    n = int(dur * SR); u = np.linspace(0, 1, n); x = rng.standard_normal(n)
    y = np.zeros(n); seg = 2048
    for i in range(0, n, seg):
        c = lo * (hi / lo) ** np.sin(np.pi * min(1, (i + seg / 2) / n) * 0.5) ; y[i:i + seg] = bp(x[i:i + seg + 0][: len(y[i:i + seg])], max(80, c * 0.6), min(SR / 2 - 100, c * 1.6))
    return norm(y * np.sin(np.pi * u) ** 1.5)
def thud(f0=110, dur=0.35):
    n = int(dur * SR); t = np.arange(n) / SR
    return norm(np.sin(2 * np.pi * f0 * t * (1 - 0.4 * t / dur)) * np.exp(-t * 14) + 0.3 * lp(rng.standard_normal(n), 400) * np.exp(-t * 30))
def boom(): return norm(np.tanh(2 * thud(70, 0.9)))
def pop(f0=880, f1=420, dur=0.08):
    n = int(dur * SR); t = np.arange(n) / SR
    return norm(np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / dur)) / SR) * np.exp(-t * 40))
def tick(): n = int(0.02 * SR); t = np.arange(n) / SR; return norm(bp(rng.standard_normal(n), 3000, 6000) * np.exp(-t * 300))
def chime(fs=(880, 1320, 1760), dur=0.9):
    n = int(dur * SR); t = np.arange(n) / SR
    return norm(sum(np.sin(2 * np.pi * f * t) * np.exp(-t * (4 + i)) / (i + 1) for i, f in enumerate(fs)))
def sparkle():
    x = np.zeros(int(0.9 * SR))
    for k in range(9):
        f = 2400 + 1800 * rng.random(); n = int(0.12 * SR); t = np.arange(n) / SR; i = int(k * 0.08 * SR)
        x[i:i + n] += np.sin(2 * np.pi * f * t) * np.exp(-t * 35) * (1 - k / 12)
    return norm(x)
def rattle(dur, dens=60):
    x = np.zeros(int(dur * SR) + SR // 4)
    for k in range(int(dur * dens)):
        c = clack(0.8 + 0.4 * rng.random()); i = int(rng.random() * dur * SR); x[i:i + len(c)] += c * (0.3 + 0.7 * rng.random())
    return norm(x)

# ---------------------------------------------------------------- events (mirrors vendor/dice.js)
land(0.95, 0.55)
base = W("Lempar", S(2) - 0.1) + 0.05
for i in range(1, 10): land(base + 0.35 + i * 0.2, 0.35, 1)
put(W("Lempar", S(3) - 0.1) + 0.25, rattle(1.7, 45), 0.4)
for i in range(4): put(S(6) + 0.1 + i * 0.12, thud(150), 0.25)
put(W("Dadunya", S(6)) - 0.05, rattle(0.6, 14), 0.25)
put(W("kegedean,") - 0.2, whoosh(0.5, 150, 900), 0.25); put(W("kekecilan.") - 0.1, pop(1400, 900), 0.3)
put(W("ruko") - 0.05, boom(), 0.6)
land(W("nawarin") + 0.1, 0.18, 1)
put(W("Dadunya", S(10)) - 0.15, whoosh(0.7, 600, 2400), 0.2)
t = S(11)
while t < S(12) - 0.2: land(t + 0.22, 0.3, 1); t += 0.42
for w in [W("Produk"), W("pasar", S(13)), W("harga"), W("cara", S(13))]: put(w - 0.02, thud(180, 0.25), 0.35); put(w, clack(), 0.25)
tl = W("sekaligus?") + 0.1
for i in range(5): land(tl - 0.05 + i * 0.05, 0.3, 1)
land(W("dadunya", S(18)) - 0.05, 0.45, 0); put(W("dadunya", S(18)) + 0.1, whoosh(0.6, 500, 2600), 0.25)
put(W("tanpa") - 0.05, whoosh(0.6, 200, 900), 0.25); put(W("lolos") + 0.05, whoosh(0.7, 1200, 200), 0.3)
for w in ["Modal,", "waktu,", "tenaga"]: land(W(w) + 0.3, 0.35, 1)
t = S(26)
while t < S(28): land(t + 0.28, 0.32, 1); put(t, pop(600, 300), 0.15); t += 0.62
put(W("kunci") + 0.2, thud(240, 0.2), 0.4); put(W("kunci") + 0.38, thud(240, 0.2), 0.4)
for tt in [W("Dadu", S(29)) + 0.1, W("ubah") - 0.1, W("Tiap", S(30)) + 0.1]: land(tt, 0.45)
put(W("Tiap", S(30)) + 0.55, chime(), 0.25)
land(W("Ganti", S(33)) - 0.2, 0.45, 1); put(W("meleset") - 0.05, whoosh(0.4, 800, 3000), 0.3); land(W("sekali.", S(33)) + 0.05, 0.4, 1)
put(W("shiny") - 0.25, sparkle(), 0.3); put(W("kinclong,") - 0.25, sparkle(), 0.25); put(W("banting") - 0.05, whoosh(0.6, 300, 1500), 0.25)
put(W("Semuanya") - 0.05, whoosh(0.6, 2400, 300), 0.3)
put(W("kebalikannya.") - 0.3, whoosh(0.5, 400, 1800), 0.25)
for w in [W("produknya,"), W("penawarannya,"), W("harganya,"), W("jualannya.")]: put(w - 0.05, pop(500, 900, 0.12), 0.35)
l6 = W("6.", S(40)) - 0.05; land(l6, 0.5); put(l6 + 0.35, chime((1047, 1568, 2093)), 0.35); put(l6 + 0.95, whoosh(0.5, 300, 2400), 0.3)
for w in [W("ringkas"), W("cari", S(41)), W("bikin", S(41))]: put(w - 0.25, pop(700, 1100, 0.1), 0.35)
put(S(42) + 0.1, rattle(1.6, 40), 0.3)
lg = W("ganti", S(43)) + 0.15; land(lg, 0.5); put(lg + 0.4, chime((988, 1480, 1976)), 0.35)
# stamps, wipes, iris, tabs
for w in [W("bisnis?") - 0.05, W("iya.") - 0.08, W("ruko") + 0.25, W("sekali.", S(9)) - 0.1, W("6.", S(10)) - 0.2, W("mental") + 0.02, W("lolos") + 0.2, W("shiny") - 0.12]: put(w + 0.18, thud(90, 0.3), 0.45)
for tt in [S(7), S(16), S(23), S(28), S(31), S(42)]: put(tt - 0.32, whoosh(0.62, 250, 3200), 0.32)
for tt in [S(19), S(37)]: put(tt - 0.36, whoosh(0.75, 2600, 300), 0.28)
for s in SC[1:]: put(s["start"] + 0.08, pop(1200, 700, 0.05), 0.08)
# counter ticks + CTA
t = S(11) + 0.1
while t < W("keluar.") + 0.1: put(t, tick(), 0.12); t += 0.05
t0 = W("DADU,") - 0.12
for k in range(4): put(t0 + 0.08 * k, tick(), 0.4)
put(W("aku", S(45)) + 0.05, pop(900, 500, 0.08), 0.5); put(W("kirim", S(45)) - 0.1, chime((1319, 1760)), 0.3)
put(T["total_sec"] - 1.0, chime((784, 1175, 1568, 2349), 1.2), 0.3)
# ---------------------------------------------------------------- write
out = out[: int(T["total_sec"] * SR)]
out = out * (0.36 / max(1e-9, np.abs(out).max()))
pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
with wave.open(str(P / "assets/audio/sfx.wav"), "wb") as f: f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(pcm.tobytes())
print("sfx.wav", round(len(out) / SR, 2), "s peak", round(float(np.abs(out).max()), 3))
