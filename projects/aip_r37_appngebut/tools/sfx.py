"""SFX for R37 (assets/audio/sfx.wav, 48 kHz mono) — client: "kasih sound effect biar gak suara VO aja".
Cues come from the composition itself (window.SFX_EVENTS -> production/sfx_events.json via tools/sfx_events.cjs): a whoosh on
every card change, a pop on every card in, ticks on the counter, clicks on cursor presses, typing on typed text, pings on results,
riser + impact on the CTA. Every hit is placed by its measured peak and moved off VO word onsets (no transient within 70 ms of a
word start); levels fixed ~8-10 dB under the VO peaks (no sidechain on the SFX). Samples: repo vo_safe set; impact/riser synthesised."""
import json, wave
import numpy as np
SR, DUR, OFF = 48000, 86.4, 0.3
out = np.zeros(int(SR * DUR))
W = json.load(open("production/words.json")); ON = [w[1] + OFF for w in W]
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
BASE = {"whoosh": -9, "pop": -10, "click": -10, "key": -17, "ping": -11, "sparkle": -13, "impact": -8, "riser": -13, "type": -18}
moved = []
def put(t, n, db, rate=1.0):
    x = S[n]; pk = PK[n] / rate; g = 10 ** ((BASE[n] + db) / 20)
    clear = lambda u: all(abs(u - o) >= 0.07 for o in ON)
    if n != "riser" and not clear(t):
        for d in sorted([k * 0.01 for k in range(-25, 26)], key=abs):
            if clear(t + d): moved.append(round(t, 2)); t += d; break
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    i = max(0, int((t - pk) * SR)); j = min(len(out), i + len(x));
    if j > i: out[i:j] += g * x[: j - i]
EV = json.load(open("production/sfx_events.json"))
for t, n, db, rate in EV: put(t, n, db, rate)
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print(len(EV), "events · peak", round(20 * np.log10(np.abs(out).max()), 1), "dBFS · moved off onsets:", len(moved))
