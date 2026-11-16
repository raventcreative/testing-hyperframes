"""SFX for R26 (assets/audio/sfx.wav, 48 kHz mono, 57.8 s) from the repo's vo_safe set (copied to assets/sfx)."""
import wave
import numpy as np
SR, DUR = 48000, 57.8
out = np.zeros(int(SR * DUR))
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    return a.reshape(-1, w.getnchannels()).mean(axis=1)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
def put(t, n, g=1.0, rate=1.0):
    x = S[n]
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    i = int(t * SR); j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
TT = [0.45, 4.45, 10.1, 15.0, 21.6, 28.05, 34.3, 39.7, 46.6]
for t in TT: put(t, "click", 0.12)                                                 # title flips
put(1.6, "pop", 0.35, 0.5); put(2.05, "sparkle", 0.22); put(2.06, "whoosh", 0.2, 0.8)  # clapper slam + shatter
put(3.0, "whoosh", 0.25, 0.7)                                                      # portal
put(3.62, "pop", 0.2, 0.9)                                                         # host in
for t in (6.3, 6.55): put(t, "type", 0.12, 1.6)                                    # laser
for t in (7.55, 8.1, 8.9): put(t, "pop", 0.18, 1.1)                                # layers light up
put(9.42, "whoosh", 0.25, 0.9)                                                     # elevator layers
for k in range(0, 50, 3): put(10.15 + k * 0.03, "key", 0.06, 1.1)                  # hook cubes rain
for k in range(5): put(11.5 + k * 0.13, "pop", 0.12, 0.8)
for k in range(3): put(12.7 + k * 0.32, "pop", 0.14, 0.7)
put(13.95, "whoosh", 0.28, 1.2)                                                    # whip tilt
put(14.8, "click", 0.3, 0.6)                                                       # lever
for i in range(28): put(14.95 + i * 0.05, "key", 0.05, 1.3)                         # reels spinning
for t in (15.95, 16.15, 16.35, 18.3, 18.45, 18.6, 19.6, 19.75, 19.9): put(t, "click", 0.16, 0.9)
for i in range(0, 44, 3): put(16.45 + i * 0.09, "pop", 0.06, 1.3)                  # cards out
put(17.9, "ping", 0.14); put(19.25, "ping", 0.16, 1.12)                            # math
put(20.45, "sparkle", 0.3, 0.9); put(20.55, "whoosh", 0.3, 0.7)                    # jackpot burst
for t in (23.0, 24.45, 25.8): put(t, "ping", 0.12, 0.9)                            # sources
for t in (24.25, 25.6): put(t, "whoosh", 0.14, 1.3)
put(27.2, "whoosh", 0.22, 1.0)                                                     # iris
for t in (29.05, 31.0, 32.75): put(t + 0.3, "pop", 0.18, 1.0)                      # hooks land on levels
put(33.3, "whoosh", 0.26, 0.6)                                                     # orbit
for t in (35.7, 36.05, 36.8, 37.5, 38.3): put(t, "click", 0.14, 1.1)               # turntable stops
put(38.9, "whoosh", 0.32, 0.5)                                                     # spin blur
for t in (40.95, 41.95, 43.05, 43.45, 45.3): put(t + 0.2, "click", 0.24, 0.75)     # dominoes
put(45.62, "pop", 0.4, 0.5); put(45.66, "whoosh", 0.25, 0.8)                       # button + shockwave
for t in (46.4, 47.0, 47.6): put(t, "type", 0.07)                                  # writer struggling
put(49.2, "whoosh", 0.2, 1.0); put(49.65, "pop", 0.22, 0.7)                        # robot lands
put(50.4, "click", 0.18)
for i in range(0, 30, 2): put(50.85 + i * 0.06, "key", 0.06, 1.2)                  # printing
put(53.2, "sparkle", 0.2)                                                          # pick
for i in range(4): put(54.1 + i * 0.1, "key", 0.12)                                # typing HOOK
put(54.75, "click", 0.22); put(55.0, "ping", 0.2)                                  # send + DM
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("sfx peak", round(float(np.abs(out).max()), 3))
