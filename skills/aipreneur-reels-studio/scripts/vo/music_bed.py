"""Royalty-free music bed, synthesised from scratch (no samples): soft kick + offbeat hats + plucked bass + a warm side-chained pad,
100 BPM, vi-IV-I-V. Meant to sit far under the VO (the mixer ducks it further while someone speaks) so a reel is never silent.
Usage: python3 tools/music_bed.py <seconds> <out.wav> [seed]   (48 kHz mono, 16-bit)"""
import sys, wave
import numpy as np
SR = 48000
dur, out = float(sys.argv[1]), sys.argv[2]
seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
rng = np.random.default_rng(seed)
BPM = 100 + (seed % 3) * 4; beat = 60 / BPM; bar = 4 * beat
keys = [0, 2, 5, 7, -3]; k = keys[seed % len(keys)]
f = lambda m: 440.0 * 2 ** ((m - 69 + k) / 12)
CH = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]          # Am F C G (shifted by k)
ROOT = [45, 41, 48, 43]
n = int(dur * SR) + SR; t = np.arange(n) / SR
x = np.zeros(n)

def lp(sig, fc):                                                        # two one-pole low-passes
    a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(sig); z1 = z2 = 0.0
    for i in range(len(sig)):
        z1 = (1 - a) * sig[i] + a * z1; z2 = (1 - a) * z1 + a * z2; y[i] = z2
    return y

# pad: band-limited detuned saws per chord, 2 bars each, slow attack/release
pad = np.zeros(n)
nb = int(np.ceil(dur / (2 * bar))) + 1
for b in range(nb):
    s0 = b * 2 * bar; i0 = int(s0 * SR); i1 = min(n, int((s0 + 2 * bar + 0.4) * SR))
    if i0 >= n: break
    tt = np.arange(i1 - i0) / SR; env = np.minimum(1, tt / 0.5) * np.minimum(1, (2 * bar + 0.4 - tt) / 0.5)
    for m in CH[b % 4]:
        for det in (-0.12, 0.11):
            fr = f(m) * 2 ** (det / 12)
            for h in range(1, 9):
                pad[i0:i1] += env * np.sin(2 * np.pi * fr * h * tt + rng.random() * 6) / h * 0.06
pad = lp(pad, 1400)
# side-chain pump on every beat
ph = (t % beat) / beat; pump = 0.55 + 0.45 * np.minimum(1, ph / 0.45)
x += pad * pump * 0.9
# kick on every beat (soft), bass pluck on beats 1 & 3
for i in range(int(dur / beat) + 1):
    s0 = i * beat; i0 = int(s0 * SR); L = int(0.28 * SR)
    if i0 + L >= n: break
    tt = np.arange(L) / SR
    fr = 45 + 75 * np.exp(-tt * 28); ph_ = 2 * np.pi * np.cumsum(fr) / SR
    x[i0:i0 + L] += np.sin(ph_) * np.exp(-tt * 13) * 0.55
    if i % 2 == 0:
        r = ROOT[(i // 8) % 4]; Lb = int(beat * 1.8 * SR); tb = np.arange(Lb) / SR
        if i0 + Lb < n:
            bs = np.tanh(1.6 * np.sin(2 * np.pi * f(r) * tb)) * np.exp(-tb * 3.2) * 0.32
            x[i0:i0 + Lb] += lp(bs, 600)
    # offbeat hat
    j0 = int((s0 + beat / 2) * SR); Lh = int(0.035 * SR)
    if j0 + Lh < n:
        nz = rng.standard_normal(Lh); nz = nz - lp(nz, 6000)
        x[j0:j0 + Lh] += nz * np.exp(-np.arange(Lh) / SR * 90) * 0.10
x = x[: int(dur * SR)]
fade_in, fade_out = int(0.8 * SR), int(1.4 * SR)
x[:fade_in] *= np.linspace(0, 1, fade_in); x[-fade_out:] *= np.linspace(1, 0, fade_out)
x = x / (np.sqrt(np.mean(x ** 2)) + 1e-9) * 10 ** (-20 / 20)              # -20 dBFS RMS
x = np.clip(x, -0.98, 0.98)
w = wave.open(out, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close()
print("bed", out, f"{dur:.2f}s", f"{BPM} BPM")
