"""SFX for R36 (assets/audio/sfx.wav, 48 kHz mono, 55.5 s). The events are the scene's own times (vendor/r36.js ev() ->
production/sfx_events.json, dumped with `SFX=production/sfx_events.json node tools/shots.cjs <port> <dir> ""`): whoosh on every
card/scene change, a soft tick on every beat counter change, pops/clicks on chips, rows, tiles and logos, typing ticks on typed
text, riser + impact on the CTA, impacts on stamps. Hits about 8-10 dB under the VO peaks, fixed level (no sidechain), each hit
placed by its measured peak and moved >= 70 ms off VO word onsets. Samples: repo vo_safe set (assets/sfx), impact/riser synthesised.
Run from the project folder: python3 -I tools/sfx.py"""
import json, wave
import numpy as np
SR, DUR, OFF = 48000, 55.5, 0.3
out = np.zeros(int(SR * DUR))
W = json.load(open("production/words.json")); ON = [w[1] + OFF for w in W]
E = json.load(open("production/sfx_events.json"))
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    a = a.reshape(-1, w.getnchannels()).mean(axis=1); return a / (np.abs(a).max() + 1e-9)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
t_ = np.arange(int(0.6 * SR)) / SR
imp = np.sin(2 * np.pi * (60 - 22 * t_ / 0.6) * t_) * np.exp(-t_ * 7) + 0.25 * np.random.default_rng(3).normal(0, 1, len(t_)) * np.exp(-t_ * 60)
S["impact"] = imp / np.abs(imp).max()
r = np.random.default_rng(5).normal(0, 1, int(0.9 * SR)); k = np.linspace(0, 1, len(r))
r = np.convolve(r, np.ones(6) / 6, "same") * (k ** 2.2) * (1 - np.exp(-(1 - k) * 60)); S["riser"] = r / np.abs(r).max()
PK = {n: int(np.argmax(np.abs(S[n]))) / SR for n in S}
moved = []
def put(t, n, db, rate=1.0):
    x = S[n]; pk = PK[n] / rate; g = 10 ** (db / 20)
    clear = lambda u: all(abs(u - o) >= 0.07 for o in ON)
    if not clear(t):
        for d in sorted([k * 0.01 for k in range(-25, 26)], key=abs):
            if clear(t + d): moved.append(round(t, 2)); t += d; break
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    i = max(0, int((t - pk) * SR)); j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
BASE = {"whoosh": -12, "impact": -11, "riser": -15, "pop": -14, "click": -15, "tick": -19, "ping": -15, "sparkle": -15, "type": -22, "send": -15, "thud": -13}
for t, n, db, rate in E:
    b = BASE[n] + db + 2   # +2 dB: clearly audible, still ~8-9 dB under the VO peaks
    if n == "tick": put(t, "click", b, 1.5)
    elif n == "type":
        for q in range(8): put(t + q * 0.075, "key", b - (q % 3), 1.1 + 0.08 * (q % 3))
    elif n == "send": put(t, "whoosh", b - 2, 1.8); put(t + 0.12, "pop", b - 3, 0.8)
    elif n == "thud": put(t, "impact", b, 1.3)
    else: put(t, n, b, rate)
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("events", len(E), "· peak", round(20 * np.log10(np.abs(out).max()), 1), "dBFS · moved off onsets:", len(moved))
