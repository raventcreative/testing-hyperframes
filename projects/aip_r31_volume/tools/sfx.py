"""R31 SFX layer (assets/audio/sfx.wav, 48 kHz mono, 57 s) — client request 2026-11-21 "kasih sound effect biar gak suara VO aja":
clearly audible and richer. Levels are set relative to the VO PEAK (the remix plays this file at volume 0.62, no compressor):
  big hits (transition whooshes, impacts)  -8 dB under the VO peak
  medium (pops, pings, swipes, risers)     -11 dB
  UI ticks / counters / caption-in clicks  -15 dB
Samples: Pixabay Content License (repo vo_safe set: click key ping pop sparkle type whoosh; indonesia-map-journey set: impact,
whoosh_c (cinematic), chime). Riser and IG-scroll swipes are synthesised here (filtered noise).
Rule: no SFX transient on a word onset — a transient within -0.05..+0.08 s of an onset moves to 0.07 s before it (hits) or is
dropped (repetitive ticks). Risers are swells (no transient) and end on the transition hit."""
import wave, json
import numpy as np
SR, DUR, OFF = 48000, 57.0, 0.3
ONS = [w[1] + OFF for w in json.load(open("production/words.json"))]
WORDS = json.load(open("production/words.json"))
def pcm(f):
    import subprocess
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(r, np.int16).astype(float) / 32768
VOPEAK = float(np.abs(pcm("assets/audio/vo.mp3")).max())
MIXVOL = 0.62
def lvl(db): return VOPEAK * 10 ** (db / 20) / MIXVOL               # sample peak in sfx.wav that lands `db` under the VO peak
out = np.zeros(int(SR * DUR))
def load(n, maxlen=None):
    a = pcm(f"assets/sfx/{n}.wav")
    if maxlen: L = int(maxlen * SR); a = a[:L] * np.minimum(1, np.linspace(6, 0, len(a[:L])))   # trim with a fade-out
    return a / (np.abs(a).max() + 1e-9)                              # every sample normalised to peak 1
S = {n: load(n) for n in ["click", "key", "ping", "pop", "sparkle", "type", "whoosh", "impact", "chime"]}
S["whoosh_c"] = load("whoosh_c", 1.7)
rng = np.random.default_rng(31)
def lp(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); z = 0.0
    for i in range(len(x)): z = (1 - a) * x[i] + a * z; y[i] = z
    return y
def riser(d):                                                          # soft swell: noise through a rising low-pass + rising pitch tone
    n = int(d * SR); t = np.arange(n) / SR; u = t / d
    nz = rng.standard_normal(n); y = np.zeros(n); z = 0.0
    for i in range(n):
        a = np.exp(-2 * np.pi * (300 + 5500 * u[i] ** 2) / SR); z = (1 - a) * nz[i] + a * z; y[i] = z
    tone = np.sin(2 * np.pi * np.cumsum(220 + 660 * u ** 2) / SR) * 0.25
    x = (y / (np.abs(y).max() + 1e-9) + tone) * (u ** 2.2); return x / (np.abs(x).max() + 1e-9)
def swipe():                                                           # IG scroll swipe: short band-passed noise sweep
    n = int(0.2 * SR); t = np.arange(n) / SR; nz = rng.standard_normal(n)
    hp = nz - lp(nz, 1800); y = lp(hp, 7000) * np.sin(np.pi * np.minimum(1, t / 0.2)) ** 1.5
    return y / (np.abs(y).max() + 1e-9)
SW = [swipe() for _ in range(4)]
PEAK = {n: int(np.argmax(np.abs(x))) / SR for n, x in S.items()}
log = []
def add(x, i, g):
    if i < 0: x = x[-i:]; i = 0
    j = min(len(out), i + len(x)); out[i:j] += g * x[: j - i]
def put(t, n, db, rate=1.0, tick=False):
    tp = t; near = [o for o in ONS if -0.05 <= tp - o <= 0.08]
    if near:
        if tick: log.append(("drop", round(t, 2), n)); return
        tp = near[0] - 0.07; log.append(("move", round(t, 2), round(tp, 2), n))
    x = S[n]
    if rate != 1.0: x = np.interp(np.arange(0, len(x) - 1, rate), np.arange(len(x)), x)
    add(x, int((tp - PEAK[n] / rate) * SR), lvl(db))
def put_riser(t_end, d, db):
    x = riser(d); add(x, int((t_end - d) * SR), lvl(db))
def put_swipe(t, db, k):
    near = [o for o in ONS if -0.05 <= t + 0.1 - o <= 0.08]
    if near: t = near[0] - 0.17
    add(SW[k % 4], int(t * SR), lvl(db))
BIG, MID, UI = -8, -11, -15
# ---- transitions: a whoosh on every one (+ impacts on the cuts that land) and soft risers into the reveals
put_riser(3.33, 0.9, MID); put(3.33, "whoosh_c", BIG)                                      # zoom-out reveal
put(7.22, "whoosh", BIG, 1.2)                                                              # snap cut
put_riser(13.2, 0.8, MID); put(13.33, "whoosh_c", BIG, 1.1)                                # bullseye -> island hop flight
put(18.6, "whoosh", BIG, 1.25)                                                             # whip tilt
put(24.8, "whoosh_c", BIG, 1.2)                                                            # 180 orbit
put_riser(30.3, 0.7, MID); put(30.3, "whoosh", BIG, 1.4); put(30.56, "impact", BIG)        # dive match cut + flash
put_riser(37.34, 0.6, MID); put(37.34, "whoosh", BIG, 0.9); put(37.78, "whoosh", MID, 1.3) # iris through the robot face
put(44.22, "whoosh_c", BIG, 0.9); put(44.3, "impact", BIG)                                 # vertigo cut
put(47.25, "whoosh", MID, 0.8)                                                             # crane starts up the spiral
put_riser(51.67, 0.8, MID); put(51.67, "whoosh", BIG, 1.0)                                 # CTA
# ---- UI: title flips, chip/tag pops, caption-in clicks (just before each caption chunk's first word)
for t in (0.35, 3.6, 7.4, 13.95, 18.9, 25.05, 31.0, 34.95, 37.9, 44.45, 47.3): put(t, "click", MID)
for t in (0.5, 7.55, 15.45, 20.15, 27.95, 31.7, 47.55): put(t, "pop", MID, 1.2)           # chip in
for t in (7.95, 10.05, 14.1, 20.15, 29.55): put(t, "pop", UI, 1.5, tick=True)              # tag in
CH = []; a = 0
for i, w in enumerate(WORDS):
    import re
    if re.search(r"[,.:?]$", w[0]) or i - a == 3 or i == len(WORDS) - 1: CH.append(a); a = i + 1
for k in CH: put(WORDS[k][1] + OFF - 0.1, "key", UI - 3, 1.4, tick=True)                  # caption chunk in
# ---- A: cannon, misses, hits, bullseye
for t in (0.556, 1.111, 1.667): put(t, "impact", MID, 1.8); put(t + 0.01, "pop", MID, 0.6)  # cannon shots (hook, on the beat)
for t in (1.27, 1.83, 2.39): put(t, "whoosh", UI, 1.6)                                     # misses fall away
put(2.72, "pop", MID, 1.3)                                                                 # give-up flag
put(3.72, "pop", MID, 0.9); put(5.68, "whoosh", MID, 1.1); put(6.05, "sparkle", MID)       # host rises, robot in, pile fills
RAP = [7.62 + (12.5 - 7.62) * i / 96 for i in range(97)]
for k, t in enumerate(RAP):
    if k % 3 == 0: put(t, "key", UI, 0.9, tick=True)                                      # rapid fire + counter ticks
HITS = (14, 27, 38, 47, 56, 64, 71, 79, 86)
for i in HITS: put(RAP[i] + 0.72, "impact", UI, 2.2, tick=True); put(RAP[i] + 0.72, "ping", UI, 1.2, tick=True)   # blocks hit the target
put(13.22, "impact", BIG); put(13.24, "sparkle", MID)                                      # bullseye: "datang"
# ---- B: the real IG feed (counter ticks, swipes on the scroll, zoom)
for k in range(5): put(15.5 + k * 0.07, "pop", UI, 1.2, tick=True)
for k, t in enumerate(np.arange(16.62, 18.5, 0.36)): put_swipe(float(t), MID, k)          # scroll swipes
for k in range(0, 95, 6): put(16.7 + k / 94 * 1.05, "key", UI, 1.3, tick=True)            # counter 5 -> 100
put(17.45, "whoosh", UI, 1.6)                                                              # zoom on the grid
# ---- C: follow-up bubbles, shutter, replies
for w in (20.2, 22.32, 22.88, 23.44):
    put(w, "pop", MID, 1.25, tick=True); put(w + 0.62, "click", UI, 1.4, tick=True)
put(21.45, "impact", MID, 1.6)                                                             # shutter down
for t in (23.5, 23.56, 24.06, 24.1): put(t + 0.02, "ping", UI, 1.1, tick=True)            # replies
# ---- D: coins, boards, bars, winner
for k in range(10): put(28.1 + k * 0.05, "click", UI, 1.5, tick=True)
for k in range(10): put(28.05 + k * 0.05, "pop", UI, 1.2, tick=True)
put(29.55, "type", UI, 1.3); put(30.18, "chime", MID); put(30.2, "impact", MID, 1.4)       # data bars, winner + crown lands
# ---- E: 30 days, bars per day, notebook
for k in range(0, 30, 2): put(31.78 + k * 0.052, "key", UI, 1.1, tick=True)
put(33.4, "whoosh", UI, 1.8)                                                               # pulse across the streak
for k in range(0, 30, 3): put(35.62 + k * 0.03, "pop", UI, 1.3, tick=True)
put(34.95, "pop", MID, 1.0)                                                                # notebook pops up
# ---- F: typing, Kirim, cards printing, done
for k in range(0, 60, 3): put(38.15 + k / 42, "key", UI, 1.0, tick=True)
put(39.75, "click", MID)
for s0 in (40.45, 41.28, 42.25):
    put(s0, "pop", MID, 1.1, tick=True)
    for k in range(1, 10, 2): put(s0 + k * 0.07, "pop", UI, 1.3, tick=True)
put_riser(43.75, 0.5, UI); put(43.79, "sparkle", MID)
# ---- G: buttons, hops, hit, CTA
put(44.7, "impact", MID, 1.3); put(44.7, "click", MID, 0.7); put(45.58, "impact", MID, 1.3); put(45.58, "click", MID, 0.75)
for k in range(0, 30, 2): put(47.62 + k * 0.118, "key", UI, 1.4, tick=True)
put(52.55, "impact", BIG); put(52.57, "sparkle", MID)                                      # the cube hits the bullseye (callback)
for i in range(6): put(52.25 + i * 0.09, "key", UI, 1.0, tick=True)                        # typing VOLUME
put(52.95, "click", MID); put(53.42, "ping", MID); put(53.42, "chime", UI)                 # send + DM
out = np.tanh(out * 1.0)                                                                   # soft safety (no compressor, no pumping)
w = wave.open("assets/audio/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.clip(out, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()
print("VO peak", round(VOPEAK, 3), "| sfx peak", round(float(np.abs(out).max()), 3), "| big hit level", round(lvl(BIG), 3),
      "| moved", sum(1 for l in log if l[0] == "move"), "dropped", sum(1 for l in log if l[0] == "drop"))
