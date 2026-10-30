#!/usr/bin/env python3
"""Sound design for the no-VO SHOWCASE (original, synthesised here with numpy — no library, no music track, no TTS).
Writes assets/sfx/showcase/*.wav and production/sfx_extra.json (mounted by tools/gen_root.py as plain <audio> clips).
Cues are placed on the world clock of compositions/world.html (video t = WT0 + wt)."""
import json, wave
from pathlib import Path
import numpy as np
P = Path(__file__).resolve().parents[1]
OUT = P / "assets/sfx/showcase"; OUT.mkdir(parents=True, exist_ok=True)
SR = 44100
WT0 = 12.9
rs = np.random.RandomState(7)

def save(name, x):
    x = np.clip(x / (np.max(np.abs(x)) + 1e-9) * 0.89, -1, 1)
    st = np.stack([x, x], 1) if x.ndim == 1 else x
    with wave.open(str(OUT / f"{name}.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
    return len(x) / SR

def env(n, a, r):
    e = np.ones(n); ai, ri = int(a * SR), int(r * SR)
    if ai: e[:ai] = np.linspace(0, 1, ai) ** 2
    if ri: e[-ri:] *= np.linspace(1, 0, ri) ** 2
    return e

def onepole(x, fc):   # lowpass, fc may be an array (time-varying)
    fc = np.broadcast_to(fc, x.shape); a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); z = 0.0
    for i in range(len(x)):
        z = (1 - a[i]) * x[i] + a[i] * z; y[i] = z
    return y

def band(x, lo, hi):
    return onepole(x, hi) - onepole(onepole(x, hi), lo)

def pink(n):
    w = rs.randn(n); b = np.zeros(n); s = [0.0] * 3
    for i in range(n):
        s[0] = 0.99765 * s[0] + w[i] * 0.0990460; s[1] = 0.96300 * s[1] + w[i] * 0.2965164; s[2] = 0.57000 * s[2] + w[i] * 1.0526913
        b[i] = s[0] + s[1] + s[2] + w[i] * 0.1848
    return b

cues = []
def cue(name, x, wt, vol, fade_in=0.0, fade_out=0.0):
    d = save(name, x); cues.append({"file": f"showcase/{name}.wav", "t": round(WT0 + wt, 3), "dur": round(d, 3), "vol": vol, "fi": fade_in, "fo": fade_out})

IN0, IN1, S1 = 7.41, 19.0, 22.2   # world clock: city window and end of the showcase
# 1. air bed across the whole showcase
n = int(17.4 * SR); tt = np.arange(n) / SR
x = band(pink(n), 180, 1600) * (0.6 + 0.4 * np.sin(tt * 0.9) * np.sin(tt * 0.37 + 1))
cue("air_bed", x * env(n, 1.2, 2.0), 5.0, 0.22, 0.6, 1.2)
# 2. dive whoosh into the cloud flash, and the flash itself (soft airy swish)
n = int(1.6 * SR); tt = np.arange(n) / SR; u = tt / tt[-1]
x = onepole(rs.randn(n), 300 + 3600 * u ** 1.6) * u ** 1.5 * (1 - u) ** 0.3
cue("dive", x, IN0 - 1.35, 0.55)
n = int(1.4 * SR); tt = np.arange(n) / SR
cue("cloud", band(pink(n), 500, 5000) * np.exp(-tt * 2.6) * (1 - np.exp(-tt * 40)), IN0 - 0.05, 0.4)
# 3. city ambience: low traffic hum + far horns, under the whole city
n = int((IN1 - IN0) * SR); tt = np.arange(n) / SR
hum = onepole(pink(n), 260) * 1.0 + 0.25 * band(rs.randn(n), 600, 2500)
for th in (2.1, 7.9):
    m = (tt > th) & (tt < th + 0.45); hum[m] += 0.12 * np.sin(2 * np.pi * 392 * tt[m]) * np.sin(np.pi * (tt[m] - th) / 0.45)
cue("city", hum * env(n, 0.8, 1.0), IN0 + 0.1, 0.32, 0.5, 0.8)
# 4. cars passing the street-level camera
for k, ti in enumerate([4.3, 5.4, 6.3]):
    n = int(1.1 * SR); tt = np.arange(n) / SR; u = tt / tt[-1]
    fc = 500 + 2400 * np.exp(-((u - 0.55) ** 2) / 0.03)
    x = onepole(rs.randn(n), fc) * np.exp(-((u - 0.55) ** 2) / 0.05) + 0.4 * np.sin(2 * np.pi * (90 - 40 * u) * tt) * np.exp(-((u - 0.55) ** 2) / 0.04)
    cue(f"car{k}", x, IN0 + ti - 0.6, 0.38)
# 5. birds by the lake (short chirp sweeps)
n = int(2.6 * SR); tt = np.arange(n) / SR; x = np.zeros(n); RB = np.random.RandomState(3)
for k in range(9):
    t0 = RB.rand() * 2.3; m = (tt >= t0) & (tt < t0 + 0.09); tl = tt[m] - t0; f0 = 2600 + RB.rand() * 1600
    x[m] += np.sin(2 * np.pi * (f0 * tl + 9000 * tl * tl)) * np.sin(np.pi * tl / 0.09)
cue("birds", x, IN0 + 8.1, 0.12)
# 6. lights-on shimmer at blue hour
n = int(2.6 * SR); tt = np.arange(n) / SR; x = np.zeros(n)
for i, f in enumerate([659.3, 784.0, 987.8, 1174.7, 1318.5, 1568.0]):
    t0 = i * 0.17; m = tt >= t0; tl = tt[m] - t0
    x[m] += np.exp(-tl * 2.2) * (np.sin(2 * np.pi * f * tl) + 0.35 * np.sin(2 * np.pi * f * 2.01 * tl)) * (0.9 - i * 0.08)
cue("shimmer", x, IN0 + 9.4, 0.2)
# 7. rise whoosh into the exit flash, then the reveal hit on the floating island
n = int(1.8 * SR); tt = np.arange(n) / SR; u = tt / tt[-1]
x = onepole(rs.randn(n), 200 + 4000 * u ** 2) * u ** 2 + 0.4 * np.sin(2 * np.pi * (60 + 140 * u ** 2) * tt) * u
cue("riser", x, IN1 - 1.6, 0.34)
n = int(2.4 * SR); tt = np.arange(n) / SR
x = np.sin(2 * np.pi * (52 - 14 * tt) * tt) * np.exp(-tt * 1.6) + 0.25 * onepole(rs.randn(n), 900) * np.exp(-tt * 2.5)
cue("boom", x, IN1 + 0.05, 0.55)
(P / "production/sfx_extra.json").write_text(json.dumps(cues, indent=1))
print(len(cues), "showcase cues:", [(c["file"], c["t"]) for c in cues])
