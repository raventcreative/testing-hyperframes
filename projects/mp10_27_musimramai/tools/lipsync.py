"""Lip-sync track from the VO: per 1/60 s mouth OPEN (loudness envelope, fast attack / slower release, gated) and
WIDE (bright 'e/i' vs round 'o/u' from the 1.8-4.5 kHz / 0.25-1 kHz energy ratio). Leads the audio by 2 frames (lips move
slightly before the sound reaches the ear). Writes lipsync.js (window.LIPSYNC). Run: python3 tools/lipsync.py assets/audio/vo.wav lipsync.js"""
import sys, json, wave
import numpy as np
src, out = sys.argv[1], sys.argv[2]
w = wave.open(src); sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768; w.close()
FPS = 60; hop = sr // FPS; win = int(sr * 0.032); n = len(x) // hop + 1
xp = np.pad(x, (win, win)); hann = np.hanning(win)
freqs = np.fft.rfftfreq(win, 1 / sr); lo = (freqs > 250) & (freqs < 1000); hi = (freqs > 1800) & (freqs < 4500)
rms = np.zeros(n); ratio = np.zeros(n)
for i in range(n):
    c = i * hop + win; seg = xp[c - win // 2: c - win // 2 + win] * hann
    S = np.abs(np.fft.rfft(seg)) ** 2
    rms[i] = np.sqrt(np.mean(seg ** 2) + 1e-12)
    ratio[i] = (S[hi].sum() + 1e-9) / (S[lo].sum() + 1e-9)
db = 20 * np.log10(rms + 1e-9); peak = np.percentile(db, 98)
# syllable-level movement: normalise loudness against a rolling 0.3 s min/max (ElevenLabs audio is compressed, so the
# absolute level alone would keep the mouth wide open); silence gate closes it completely
R = int(0.15 * FPS); lo_ = np.array([db[max(0, i - R): i + R + 1].min() for i in range(n)]); hi_ = np.array([db[max(0, i - R): i + R + 1].max() for i in range(n)])
local = np.clip((db - lo_) / (hi_ - lo_ + 4.0), 0, 1)
level = np.clip((db - (peak - 30)) / 26, 0, 1)
o = (0.15 + 0.85 * local) * level
o[db < peak - 38] = 0
sm = np.zeros(n); a_up, a_dn = 0.7, 0.35
for i in range(1, n): sm[i] = sm[i - 1] + (a_up if o[i] > sm[i - 1] else a_dn) * (o[i] - sm[i - 1])
wide = np.clip((np.log10(ratio + 1e-6) + 1.2) / 1.4, 0, 1)
ws = np.zeros(n)
for i in range(1, n): ws[i] = ws[i - 1] + 0.3 * (wide[i] - ws[i - 1])
lead = 2; sm = np.concatenate([sm[lead:], np.zeros(lead)]); ws = np.concatenate([ws[lead:], np.zeros(lead)])
open(out, "w").write("window.LIPSYNC = " + json.dumps({"fps": FPS, "open": [round(float(v), 3) for v in sm], "wide": [round(float(v), 3) for v in ws]}) + ";\n")
print("frames", n, "dur", round(len(x) / sr, 2), "mean open", round(float(sm.mean()), 3), "talking frac", round(float((sm > 0.15).mean()), 3))
