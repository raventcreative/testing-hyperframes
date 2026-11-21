"""SFX for R34 (assets/audio/sfx.wav, 48 kHz mono, 42 s) — client: "kasih sound effect biar gak suara VO aja".
Richer, clearly audible layer: whoosh on every transition, soft impact + riser on the reveals, pops/clicks on UI and on every caption
chunk, typing ticks on code/prompt/comment typing. Levels in dBFS before the final loudnorm: hits sit ~8-10 dB under the VO peaks
(VO sample peak -1 dBFS, word peaks ~-4). Samples from the repo's vo_safe set (normalised), impact/riser synthesised here.
Every hit is placed by its measured peak and moved off VO word onsets (no transient within 70 ms of a word start)."""
import json, wave
import numpy as np
SR, DUR, OFF = 48000, 42.0, 0.3
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
moved = []
def put(t, n, db, rate=1.0):
    x = S[n]; pk = PK[n] / rate; g = 10 ** (db / 20)
    clear = lambda u: all(abs(u - o) >= 0.07 for o in ON)
    if not clear(t):
        for d in sorted([k * 0.01 for k in range(-25, 26)], key=abs):
            if clear(t + d): moved.append(round(t, 2)); t += d; break
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    i = max(0, int((t - pk) * SR)); j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
WH, IM, RI, UI, CAP, TK = -11, -10, -16, -14, -21, -23
# ---- transitions: whoosh on every one, riser + impact on the reveals
for t, rate in [(4.2, 1.2), (5.3, 0.7), (8.45, 1.3), (8.98, 0.8), (14.5, 1.3), (14.95, 1.4), (16.0, 1.1), (18.92, 1.0), (19.3, 0.8), (22.3, 1.2),
                (24.05, 1.1), (25.7, 0.75), (30.55, 0.9), (31.4, 1.0), (35.3, 1.2), (36.3, 1.1), (37.78, 1.0)]: put(t, "whoosh", WH, rate)
for t in (5.3, 9.17, 30.93, 38.27): put(t - 0.6, "riser", RI)
for t, db in [(4.45, IM), (5.65, IM - 2), (9.17, IM), (26.32, IM), (30.93, IM - 1), (38.27, IM)]: put(t, "impact", db)
# ---- UI: title tabs, tags, logos, crates, icons, cards, CTA
for t in (0.4, 5.4, 9.45, 19.5, 26.55, 31.2): put(t + 0.05, "click", UI)
for t in (16.75, 21.1, 34.3): put(t, "pop", UI, 1.1)
for t in (5.82, 7.02, 12.95, 13.42, 19.74, 26.86, 29.26, 32.78, 33.5): put(t, "pop", UI + 1, 0.9)
for k in range(4): put(5.55 + k * 0.12, "pop", UI - 2, 0.8 + 0.05 * k)                       # crates rise
for k in range(4): put(7.66 + k * 0.14, "ping", UI - 5, 1.2)                                  # studio icons
for k in range(4): put(4.55 + k * 0.08, "click", UI - 4, 1.2)                                 # clips scatter
put(10.5, "sparkle", UI - 2); put(15.32, "ping", UI); put(23.32, "sparkle", UI - 4, 1.1)
for k in range(3): put(23.98 + k * 0.16, "click", UI - 2)                                     # timeline bars
for k in range(9): put(29.55 + k * 0.1, "pop", UI - 3, 0.8 + k * 0.05)                        # scene assembles
put(13.2, "click", UI - 1); put(13.85, "click", UI - 1); put(27.86, "click", UI - 1)          # click highlights on the real UI
for k in range(4): put(36.47 + k * 0.1, "pop", UI - 2, 1.0 + 0.05 * k)
put(37.12, "click", UI); put(37.3, "ping", UI - 2, 1.1)
put(38.32, "pop", UI); put(39.17, "click", UI); put(39.42, "ping", UI)
for t in (35.86, 22.65): put(t, "pop", UI - 2, 0.7)
# ---- typing ticks
for k in range(26): put(0.2 + k * 0.12, "key", TK, 1.1 + 0.08 * (k % 3))                      # index.html
for k in range(16): put(10.5 + k * 0.12, "key", TK - 2, 1.3)                                   # star counter
for k in range(12): put(28.2 + k * 0.09, "key", TK, 1.1 + 0.08 * (k % 3))                     # prompt into Claude Code
for k in range(6): put(38.46 + k * 0.08, "key", TK + 2)                                       # STUDIO
# ---- caption chunks in: soft tick per chunk
ch, a = [], 0
for i, w in enumerate(W):
    if w[0][-1] in ",.:?" or i - a == 3 or i == len(W) - 1: ch.append(W[a][1] + OFF); a = i + 1
for t in ch: put(t - 0.06, "click", CAP, 1.5)
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("events ok · peak", round(20 * np.log10(np.abs(out).max()), 1), "dBFS · moved off onsets:", len(moved), "· chunks", len(ch))
