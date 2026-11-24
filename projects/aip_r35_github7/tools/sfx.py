"""SFX for R35 (assets/audio/sfx.wav, 48 kHz mono, 87 s) — client: "kasih sound effect biar gak suara VO aja".
Whoosh on every transition, riser + soft impact on the reveals, pops/clicks on UI objects and on every caption chunk, typing ticks
on the scripted windows. Hits ~8-10 dB under the VO peaks; every hit placed by its measured peak and moved off VO word onsets
(no transient within 70 ms of a word start). Samples from the repo's vo_safe set (normalised), impact/riser synthesised here."""
import json, wave
import numpy as np
SR, DUR, OFF = 48000, 87.0, 0.3
out = np.zeros(int(SR * DUR))
W = json.load(open("production/words.json")); ON = [w[1] + OFF for w in W]
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    a = a.reshape(-1, w.getnchannels()).mean(axis=1); return a / (np.abs(a).max() + 1e-9)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
t_ = np.arange(int(0.6 * SR)) / SR
imp = np.sin(2 * np.pi * (60 - 22 * t_ / 0.6) * t_) * np.exp(-t_ * 7) + 0.25 * np.random.default_rng(3).normal(0, 1, len(t_)) * np.exp(-t_ * 60)
S["impact"] = imp / np.abs(imp).max()
r = np.random.default_rng(5).normal(0, 1, int(0.7 * SR)); k = np.linspace(0, 1, len(r))
r = np.convolve(r, np.ones(6) / 6, "same") * (k ** 2.2) * (1 - np.exp(-(1 - k) * 60)); S["riser"] = r / np.abs(r).max()
PK = {n: int(np.argmax(np.abs(S[n]))) / SR for n in S}
PW = json.load(open("production/warp_points.json"))          # take-2 scene time -> final VO time (tools/warp.py)
WI = lambda t: float(np.interp(t, [b for a, b in PW], [a for a, b in PW]))
moved = []
def put(t, n, db, rate=1.0, raw=False):
    if not raw: t = WI(t)
    x = S[n]; pk = PK[n] / rate; g = 10 ** (db / 20)
    clear = lambda u: all(abs(u - o) >= 0.07 for o in ON)
    if not clear(t):
        for d in sorted([k * 0.01 for k in range(-25, 26)], key=abs):
            if clear(t + d): moved.append(round(t, 2)); t += d; break
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    i = max(0, int((t - pk) * SR)); j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
WH, IM, RI, UI, CAP, TK = -11, -10, -16, -14, -21, -23
# ---- transitions: whoosh on every one, riser + impact on the reveals
for t, rate in [(5.45, 0.8), (6.95, 1.5), (12.75, 1.1), (13.08, 0.8), (21.55, 1.3), (21.78, 0.9), (31.95, 1.0), (32.42, 0.85), (40.95, 1.3), (41.2, 0.9),
                (49.8, 0.7), (50.3, 1.2), (52.8, 1.5), (54.5, 1.3), (60.4, 1.0), (60.95, 0.8), (68.7, 0.75), (69.3, 1.1), (79.6, 0.8), (80.15, 1.0), (24.95, 1.4), (37.05, 1.4), (75.5, 1.4)]: put(t, "whoosh", WH, rate)
for t in (6.0, 13.05, 60.91, 80.15, 25.85): put(t - 0.6, "riser", RI)
for t, db in [(6.05, IM - 1), (13.06, IM), (59.45, IM - 2), (60.92, IM), (80.16, IM), (32.38, IM - 3)]: put(t, "impact", db)
# ---- UI: title tabs, tags, logos, objects
for t in (0.4, 7.95, 13.25, 21.95, 32.6, 41.45, 50.65, 61.15, 69.4): put(t + 0.05, "click", UI)
for t in (2.2, 6.05, 14.45, 22.35, 29.75, 33.05, 41.75, 51.05, 61.45, 69.5, 75.75): put(t + 0.04, "pop", UI - 3, 1.2)
put(1.65, "pop", UI, 0.8); put(1.75, "sparkle", UI - 3)
for k in range(7): put(0.92 + k * 0.16, "pop", UI - 5, 1.0 + 0.05 * k)                    # tool tiles on the laptop
for k in range(3): put(6.02 + k * 0.1, "pop", UI - 2, 0.9 + 0.1 * k)                       # subscription cards
for t in (9.82, 10.34, 11.26, 12.22): put(t, "pop", UI, 1.0); put(t - 0.2, "click", UI - 6, 1.4)   # needs + dot hops
put(16.32, "pop", UI); put(17.4, "click", UI - 1); put(17.9, "ping", UI - 3); put(18.02, "pop", UI - 1); put(18.87, "click", UI); put(19.78, "sparkle", UI - 1); put(20.62, "pop", UI - 2)
put(22.02, "pop", UI); put(25.8, "sparkle", UI); put(26.6, "ping", UI - 3)
for t in (27.87, 28.59, 29.07): put(t, "pop", UI)
put(30.32, "pop", UI); put(31.0, "click", UI - 2); put(31.47, "pop", UI - 1)
put(33.62, "ping", UI - 2)
for k in range(3): put(36.72 + k * 0.12, "pop", UI - 1, 0.9 + 0.1 * k)
put(37.62, "click", UI); put(37.7, "pop", UI - 2, 0.7); put(38.17, "pop", UI); put(39.42, "pop", UI - 1); put(39.7, "ping", UI - 3)
put(43.42, "pop", UI); put(44.5, "click", UI)
for k in range(3): put(44.55 + k * 0.12, "ping", UI - 5, 1.2)
put(45.62, "pop", UI); put(46.22, "pop", UI); put(46.72, "sparkle", UI - 2); put(47.57, "pop", UI - 1)
put(51.62, "pop", UI); put(52.9, "ping", UI - 1)
for k in range(10): put(55.7 + k * 0.09, "click", UI - 7, 1.3)
put(56.62, "pop", UI); put(59.4, "click", UI)
put(63.32, "ping", UI); put(64.77, "pop", UI); put(65.97, "pop", UI - 1); put(66.82, "click", UI); put(67.32, "pop", UI - 2)
for k in range(3): put(62.5 + k * 0.25, "pop", UI - 6, 1.3)
put(70.32, "pop", UI); put(71.2, "click", UI - 1); put(72.1, "click", UI - 1)
for t in (73.1, 73.6, 74.2): put(t, "pop", UI)
for t in (74.3, 74.75, 75.1): put(t, "sparkle", UI - 5, 1.2)
put(76.32, "pop", UI); put(77.02, "pop", UI - 1); put(77.17, "pop", UI - 1)
for k in range(7): put(80.4 + k * 0.14, "click", UI - 3, 1.0 + 0.04 * k)
put(80.35, "pop", UI); put(82.87, "pop", UI); put(84.07, "click", UI); put(84.32, "ping", UI)
# ---- typing ticks
for k in range(7): put(0.28 + k * 0.1, "key", TK, 1.1 + 0.08 * (k % 3))                   # "7 aplikasi AI"
for k in range(9): put(12.52 + k * 0.09, "key", TK - 1, 1.1 + 0.08 * (k % 3))            # chat question
for k in range(14): put(13.8 + k * 0.16, "key", TK - 3, 1.2)                               # chat answer
for k in range(10): put(35.48 + k * 0.1, "key", TK, 1.1)                                   # transcript
for k in range(12): put(51.97 + k * 0.08, "key", TK, 1.1 + 0.08 * (k % 3))                # script
for k in range(8): put(63.97 + k * 0.09, "key", TK - 1, 1.2)                               # meeting transcript
for k in range(6): put(83.32 + k * 0.08, "key", TK + 2)                                    # GITHUB
# ---- caption chunks in: soft tick per chunk
ch, a = [], 0
for i, w in enumerate(W):
    if w[0][-1] in ",.:?" or i - a == 3 or i == len(W) - 1: ch.append(W[a][1] + OFF); a = i + 1
for t in ch: put(t - 0.06, "click", CAP, 1.5, raw=True)
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("events ok · peak", round(20 * np.log10(np.abs(out).max()), 1), "dBFS · moved off onsets:", len(moved), "· chunks", len(ch))
