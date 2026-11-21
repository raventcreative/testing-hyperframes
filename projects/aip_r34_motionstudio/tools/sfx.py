"""SFX for R34 (assets/audio/sfx.wav, 48 kHz mono, 42 s) from the repo's vo_safe set (assets/sfx). Fixed low levels; any hit that
would land on a VO word onset (±70 ms) is moved to just before that word, so no transient masks a consonant."""
import json, wave
import numpy as np
SR, DUR, OFF = 48000, 42.0, 0.3
out = np.zeros(int(SR * DUR))
ON = [w[1] + OFF for w in json.load(open("production/words.json"))]
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    return a.reshape(-1, w.getnchannels()).mean(axis=1)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
PK = {n: int(np.argmax(np.abs(S[n]))) / SR for n in S}            # place by measured peak, not file start
moved = []
def put(t, n, g=1.0, rate=1.0):
    x = S[n]; pk = PK[n] / rate
    clear = lambda u: all(abs(u - o) >= 0.07 for o in ON)
    if not clear(t):
        for d in sorted([k * 0.01 for k in range(-25, 26)], key=abs):
            if clear(t + d): moved.append((round(t, 2), n, round(d, 2))); t += d; break
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    i = max(0, int((t - pk) * SR)); j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
for k in range(13): put(0.25 + k * 0.24, "key", 0.05, 1.1)                       # code typing on the monitor
put(4.2, "whoosh", 0.2, 1.2); put(4.45, "pop", 0.3, 0.6)                          # cursor cube jumps out, knocks the clips
for k in range(4): put(4.55 + k * 0.08, "click", 0.08, 1.2)
put(5.3, "whoosh", 0.18, 0.7)                                                      # zoom-out reveal
for k in range(4): put(5.15 + k * 0.12, "pop", 0.14, 0.8)                          # crates rise
put(5.85, "sparkle", 0.14); put(7.05, "pop", 0.16, 0.9)                            # GitHub / Claude logos
for k in range(4): put(7.66 + k * 0.14, "ping", 0.06, 1.2)                          # studio icons
put(8.45, "whoosh", 0.14, 1.3); put(8.98, "whoosh", 0.24, 0.8)                     # hop + portal dive
for k in range(15): put(10.5 + k * 0.13, "key", 0.04, 1.3)                         # star counter
put(10.5, "sparkle", 0.12)
put(12.95, "pop", 0.14); put(13.45, "pop", 0.14, 1.1)                              # Claude + HTML logos
for k in range(6): put(13.0 + k * 0.24, "key", 0.05, 1.1)
put(14.62, "click", 0.16); put(14.9, "whoosh", 0.12, 1.4); put(15.62, "ping", 0.12)  # render -> frames -> done
put(16.78, "pop", 0.12, 1.1)
put(18.92, "whoosh", 0.26, 1.1)                                                    # whip tilt
put(19.76, "pop", 0.16, 0.9); put(21.12, "pop", 0.1, 1.1)
put(23.25, "sparkle", 0.1, 1.1)
for k in range(3): put(24.02 + k * 0.18, "click", 0.1, 1.0)                        # timeline bars
put(25.7, "whoosh", 0.22, 0.75); put(26.32, "pop", 0.24, 0.55)                     # fall + land
put(26.9, "pop", 0.14, 0.9)
for k in range(8): put(28.1 + k * 0.13, "key", 0.05, 1.1)                          # prompt typing
for k in range(9): put(29.55 + k * 0.1, "pop", 0.07, 0.8 + k * 0.05)               # scene assembles
put(30.62, "whoosh", 0.2, 0.9); put(30.96, "click", 0.14, 0.8)                     # lens dive + REC
put(32.8, "pop", 0.12); put(33.52, "pop", 0.12, 1.1)
put(34.3, "whoosh", 0.1, 0.6); put(35.3, "whoosh", 0.14, 1.2); put(35.86, "pop", 0.14, 0.7)
for k in range(4): put(36.47 + k * 0.1, "pop", 0.09, 1.0 + 0.05 * k)
put(37.14, "click", 0.18); put(37.3, "ping", 0.1, 1.1)                             # edit a shot
put(37.78, "whoosh", 0.2, 1.0); put(38.2, "sparkle", 0.14)                         # card into the lens
put(38.32, "pop", 0.14, 0.9)
for k in range(6): put(38.46 + k * 0.08, "key", 0.08)                              # typing STUDIO
put(39.17, "click", 0.18); put(39.42, "ping", 0.14)                                # send + DM
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("sfx peak", round(float(np.abs(out).max()), 3), "moved off word onsets:", moved)
