"""R31 SFX (assets/audio/sfx.wav, 48 kHz mono, 57 s) from the repo's vo_safe sample set (copied to assets/sfx).
Times are video seconds (VO starts at 0.3 s). Rule (client, batch 8): no SFX transient on a word onset -> every event that
lands within -0.05..+0.08 s of a word onset is moved to 0.07 s before that onset (big hits) or dropped (repetitive ticks)."""
import wave, json
import numpy as np
SR, DUR, OFF = 48000, 57.0, 0.3
ONS = [w[1] + OFF for w in json.load(open("production/words.json"))]
out = np.zeros(int(SR * DUR))
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    return a.reshape(-1, w.getnchannels()).mean(axis=1)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
PEAK = {n: int(np.argmax(np.abs(x))) / SR for n, x in S.items()}           # place by measured peak, not file start
log = []
def put(t, n, g=1.0, rate=1.0, tick=False):
    tp = t                                                                # wanted time of the transient
    near = [o for o in ONS if -0.05 <= tp - o <= 0.08]
    if near:
        if tick: log.append(("drop", round(t, 2), n)); return
        tp = near[0] - 0.07; log.append(("move", round(t, 2), round(tp, 2), n))
    x = S[n]
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    i = int((tp - PEAK[n] / rate) * SR)
    if i < 0: x = x[-i:]; i = 0
    j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
for t in (0.35, 3.6, 7.4, 13.95, 18.9, 25.05, 31.0, 34.95, 37.9, 44.45, 47.3): put(t, "click", 0.12)      # title flips
for t in (0.556, 1.111, 1.667): put(t, "pop", 0.32, 0.6)                                                # cannon shots (hook, on the beat)
for t in (1.27, 1.83, 2.39): put(t, "whoosh", 0.07, 1.5)                                                # misses fall away
put(2.72, "pop", 0.2, 1.3)                                                                              # give-up flag
put(3.33, "whoosh", 0.26, 0.7)                                                                          # zoom-out reveal
put(3.72, "pop", 0.18, 0.9)                                                                             # host rises
put(5.68, "whoosh", 0.16, 1.1)                                                                          # robot flies in
put(6.05, "sparkle", 0.18)                                                                              # the pile fills
put(7.22, "whoosh", 0.22, 1.2)                                                                          # snap cut
import math
RAP = [7.62 + (12.5 - 7.62) * i / 96 for i in range(97)]
for k, t in enumerate(RAP):
    if k % 2 == 0: put(t, "key", 0.05, 0.9, tick=True)                                                 # rapid fire
for t in (7.62 + (12.5 - 7.62) * i / 96 + 0.72 for i in (14, 27, 38, 47, 56, 64, 71, 79, 86)): put(t, "ping", 0.07, 1.2, tick=True)
put(13.22, "sparkle", 0.3); put(13.24, "pop", 0.25, 0.7)                                                # bullseye
put(13.33, "whoosh", 0.3, 0.8)                                                                          # island hop flight
for k in range(5): put(15.5 + k * 0.07, "pop", 0.12, 1.1, tick=True)                                    # 5 videos
for k in range(0, 95, 4): put(16.7 + k / 94 * 1.05, "key", 0.05, 1.3, tick=True)                        # 100 videos
put(17.62, "sparkle", 0.18)                                                                             # tiles rise
put(18.6, "whoosh", 0.3, 1.25)                                                                          # whip tilt
for w in (20.2, 22.32, 22.88, 23.44):
    put(w, "pop", 0.13, 1.25, tick=True); put(w + 0.62, "click", 0.08, 1.4, tick=True)                   # bubbles out / land
put(21.45, "click", 0.2, 0.6)                                                                           # shutter down
for t in (23.5, 23.56, 24.06, 24.1): put(t + 0.62 - 0.6, "ping", 0.09, 1.1, tick=True)                  # replies
put(24.8, "whoosh", 0.28, 0.7)                                                                          # orbit
for k in range(10): put(28.1 + k * 0.05, "click", 0.06, 1.5, tick=True)                                 # coins split
for k in range(10): put(28.05 + k * 0.05, "pop", 0.06, 1.2, tick=True)                                  # boards
put(29.55, "type", 0.08, 1.3)                                                                           # data bars
put(30.18, "sparkle", 0.26)                                                                             # winner
put(30.3, "whoosh", 0.28, 1.4)                                                                          # dive match cut
for k in range(0, 30, 2): put(31.78 + k * 0.052, "key", 0.06, 1.1, tick=True)                           # 30 days
for k in range(0, 30, 3): put(35.62 + k * 0.03, "pop", 0.05, 1.3, tick=True)                            # bars per day
put(37.34, "whoosh", 0.24, 0.9)                                                                         # iris into the robot screen
for k in range(0, 60, 3): put(38.15 + k / 42, "key", 0.07, 1.0, tick=True)                              # typing the prompt
put(39.75, "click", 0.22)                                                                               # Kirim
for s0 in (40.45, 41.28, 42.25):
    for k in range(0, 10, 2): put(s0 + k * 0.07, "pop", 0.06, 1.3, tick=True)                           # cards print
put(43.79, "sparkle", 0.18)                                                                             # done in one sitting
put(44.22, "whoosh", 0.3, 0.6)                                                                          # vertigo cut
put(44.7, "click", 0.3, 0.7); put(45.58, "click", 0.3, 0.75)                                            # POSTING / KIRIM pressed
for k in range(0, 30, 2): put(47.62 + k * 0.118, "key", 0.05, 1.4, tick=True)                           # hops up the stairs
put(52.55, "sparkle", 0.3); put(52.57, "pop", 0.25, 0.6)                                               # hit (callback to the hook)
for i in range(6): put(52.25 + i * 0.09, "key", 0.1, tick=True)                                         # typing VOLUME
put(52.95, "click", 0.22); put(53.42, "ping", 0.18)                                                     # send + DM
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("sfx peak", round(float(np.abs(out).max()), 3), "moved", sum(1 for l in log if l[0] == "move"), "dropped", sum(1 for l in log if l[0] == "drop"))
for l in log:
    if l[0] == "move": print(" ", l)
