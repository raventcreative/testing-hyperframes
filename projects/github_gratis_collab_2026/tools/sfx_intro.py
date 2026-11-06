"""Synthesises the intro sound design (original, no samples): 4 marimba-like pops (C5 E5 G5 C6) as the logos appear,
a soft C-major pad under the silent intro, a whoosh on the turn, a rising whoosh + soft low thump as he steps in.
Output: assets/audio/sfx_intro.wav (48 kHz stereo).   Run: python3 -I tools/sfx_intro.py ."""
import sys, wave
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SR, DUR = 48000, 3.2
t = np.arange(int(SR * DUR)) / SR
L = np.zeros_like(t); R = np.zeros_like(t)
rng = np.random.default_rng(20261106)

def place(sig, at, pan=0.0, gain=1.0):
    sig = sig.copy(); k = min(len(sig), int(0.03 * SR)); sig[-k:] *= np.linspace(1, 0, k)   # no end clicks
    i = int(at * SR); n = min(len(sig), len(t) - i)
    gl, gr = gain * np.sqrt(0.5 * (1 - pan)), gain * np.sqrt(0.5 * (1 + pan))
    L[i:i + n] += sig[:n] * gl; R[i:i + n] += sig[:n] * gr

def env_ad(n, a, d):
    x = np.arange(n) / SR
    return np.minimum(1, x / a) * np.exp(-x / d)

def marimba(f, dur=0.9):
    n = int(dur * SR); x = np.arange(n) / SR
    s = (np.sin(2 * np.pi * f * x) * np.exp(-x / 0.32)
         + 0.35 * np.sin(2 * np.pi * f * 3.98 * x) * np.exp(-x / 0.06)
         + 0.12 * np.sin(2 * np.pi * f * 9.9 * x) * np.exp(-x / 0.02))
    s *= np.minimum(1, x / 0.002)
    # soft mallet tick
    tick = rng.normal(0, 1, n) * np.exp(-x / 0.004); tick = np.convolve(tick, np.ones(6) / 6, "same")
    # bubble "pop" under the note (pitch drop)
    fp = 900 * np.exp(-x / 0.03) + 260
    pop = np.sin(2 * np.pi * np.cumsum(fp) / SR) * np.exp(-x / 0.035)
    return 0.6 * s + 0.12 * tick + 0.35 * pop

def bandnoise(n, f0, f1, q=0.35):
    """noise through a sweeping 2-pole band-pass (state variable filter)"""
    w = rng.normal(0, 1, n); out = np.zeros(n); lp = bp = 0.0
    fc = np.geomspace(f0, f1, n)
    for k in range(n):
        F = 2 * np.sin(np.pi * fc[k] / SR)
        hp = w[k] - lp - q * bp; bp += F * hp; lp += F * bp; out[k] = bp
    # tame the top end (one-pole low-pass ~5 kHz): airy, not hissy
    a = np.exp(-2 * np.pi * 5000 / SR); y = np.zeros(n); acc = 0.0
    for k in range(n): acc = (1 - a) * out[k] + a * acc; y[k] = acc
    return y / (np.abs(y).max() + 1e-9)

def whoosh(dur, f0, f1, peak=0.6):
    n = int(dur * SR); x = np.arange(n) / n
    e = np.where(x < peak, (x / peak) ** 2, ((1 - x) / (1 - peak)) ** 1.5)
    return bandnoise(n, f0, f1) * e

# pad (C3 G3 C4 E4), slow attack, gone under the VO
n = int(2.6 * SR); x = np.arange(n) / SR
pad = sum(a * np.sin(2 * np.pi * f * x + ph) for f, a, ph in ((130.81, .5, 0), (196.0, .35, 1), (261.63, .3, 2), (329.63, .22, 3)))
pad *= np.minimum(1, x / 0.5) * np.clip((2.35 - x) / 0.5, 0, 1)
place(pad * 0.12, 0.0, 0.0)
# pops (= POP in s01.html / mascot.html), panned left -> right like the logos
for at, f, pan in ((0.15, 523.25, -0.55), (0.40, 659.26, -0.18), (0.65, 783.99, 0.18), (0.90, 1046.5, 0.55)):
    place(marimba(f), at + 0.02, pan, 0.55)
    place(marimba(f * 2, 0.4), at + 0.02, pan, 0.08)   # sparkle octave
# turn whoosh
place(whoosh(0.42, 600, 3200, 0.55), 1.0, -0.2, 0.32)
# step-in: rising whoosh with the logos
place(whoosh(0.72, 300, 2600, 0.8), 1.28, 0.15, 0.4)
# soft low thump on arrival (mostly sub, short, so it does not mask the first word at 2.03)
n = int(0.45 * SR); x = np.arange(n) / SR
thump = np.sin(2 * np.pi * np.cumsum(55 + 50 * np.exp(-x / 0.05)) / SR) * env_ad(n, 0.004, 0.12)
place(thump, 1.93, 0.0, 0.5)
# small room: two short reflections + gentle decay
def room(s):
    out = s.copy()
    for d, g in ((0.023, 0.22), (0.041, 0.16), (0.067, 0.11), (0.097, 0.07)):
        k = int(d * SR); out[k:] += g * s[:-k]
    return out
L, R = room(L), room(R)
m = max(np.abs(L).max(), np.abs(R).max())
L, R = L / m * 0.7, R / m * 0.7
pcm = (np.stack([L, R], 1) * 32767).astype(np.int16)
out = P / "assets/audio/sfx_intro.wav"
with wave.open(str(out), "wb") as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes(pcm.tobytes())
print("wrote", out, round(DUR, 2), "s")
