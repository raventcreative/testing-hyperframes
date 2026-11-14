"""SFX track for the voxel test (assets/audio/sfx.wav, 48 kHz mono, 18 s) from the repo's vo_safe sample set
(projects/reels-xray-aipreneur-v3/assets/sfx/vo_safe). Times are video seconds (VO starts at 0.3 s)."""
import wave
import numpy as np
SR, DUR = 48000, 18.0
out = np.zeros(int(SR * DUR))
def load(n):
    w = wave.open(f"assets/sfx/{n}.wav"); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
    return a.reshape(-1, w.getnchannels()).mean(axis=1)
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh"]}
def put(t, n, g=1.0, rate=1.0):
    x = S[n]
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    i = int(t * SR); j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
put(0.02, "type", 0.18)
for k in range(0, 16, 2): put(0.62 + k * 0.095, "pop", 0.10, 1.25)                 # CVs leave the laptop
for t in (0.35, 2.62, 7.3, 11.62): put(t, "click", 0.16)                          # title flips
put(2.62, "pop", 0.22, 0.7)                                                        # BALASAN 0
for t in (2.45, 3.8): put(t, "whoosh", 0.22)                                      # whip pans
put(2.92, "click", 0.3, 0.8)                                                       # mailbox door
put(4.12, "sparkle", 0.16)                                                         # "?" assembles
put(5.95, "whoosh", 0.3, 0.8)                                                      # zoom out
put(6.12, "pop", 0.22, 0.9)                                                        # host pops in
put(6.86, "whoosh", 0.28, 1.1)                                                     # cube wipe
for i in range(7): put(7.42 + i * 0.2 - 0.02, "pop", 0.2, 0.8 + 0.06 * i)         # robots land
put(8.3, "whoosh", 0.14, 1.3)                                                      # CV slides in
put(9.83, "sparkle", 0.15); [put(9.83 + i * 0.06, "key", 0.08) for i in range(7)]  # score cards
put(10.75, "whoosh", 0.3, 0.75); put(11.3, "whoosh", 0.18, 1.2)                    # dive + pull out
for t, r in ((14.55, 1.0), (14.8, 1.12)): put(t, "ping", 0.16, r)                  # keyword hits
put(15.05, "pop", 0.22, 0.6)                                                       # keyword miss
put(15.86, "click", 0.3, 0.7); put(16.36, "pop", 0.3, 0.55)                        # trapdoor + bin
out = np.clip(out, -1, 1)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("sfx peak", round(float(np.abs(out).max()), 3))
