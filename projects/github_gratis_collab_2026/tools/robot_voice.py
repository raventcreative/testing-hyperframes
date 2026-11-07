"""Gives the robot its own voice: the VO segments it speaks (s06 / s09 / s12 / s15 "Gantinya…" lines) are re-voiced as a friendly
AI-assistant robot (pitch +3 semitones with natural formants, a slight inharmonic frequency shift, short metallic comb, light
bit-crush, band-limited 'speaker' EQ), loudness-matched to the mascot, and crossfaded back into the original VO. Timing is
unchanged, so lip/talk-bar sync and the edit stay exact.   Usage: python3 tools/robot_voice.py <project_dir>"""
import json, subprocess, sys, wave
from pathlib import Path
import numpy as np
P = Path(sys.argv[1]).resolve(); SR = 48000
T = json.loads((P / "production/timing.json").read_text()); off = T["vo_offset"]
def dec(path, filt=None):
    cmd = ["ffmpeg", "-v", "error", "-i", str(path)] + (["-af", filt] if filt else []) + ["-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).astype(np.float64)
vo = P / "assets/audio/vo.mp3"
dry = dec(vo)
# v2 "premium AI assistant": clean & full (wider band), soft digital sheen (thin octave-up layer + chorus), only a hint of metal,
# gentle compression and a small room. Pitch +2.7 st with natural formants.
# v3 "real robot": pitch-shifted voice (+2.7 st) -> channel VOCODER on a monotone buzz carrier (classic robot timbre) blended with
# a ring-modulated copy (metallic tremble) and a little of the clean voice for intelligibility; then metallic comb, EQ,
# compression and a limiter for a polished, loud-enough result.
from scipy.signal import stft, istft
from scipy.ndimage import uniform_filter1d
PRE = "rubberband=pitch=1.17:formant=preserved:transients=crisp"
x = dec(vo, PRE)
t = np.arange(len(x)) / SR
f0 = 150.0                                                  # monotone robot pitch
saw = 2 * ((t * f0) % 1.0) - 1                              # buzz carrier (rich harmonics)
saw = saw + 0.5 * (2 * ((t * f0 * 2.003) % 1.0) - 1)        # slight detuned octave for a synthetic shimmer
rng = np.random.default_rng(7); noise = rng.normal(0, 0.25, len(x))
carrier = saw + noise                                       # noise keeps consonants (s, t, k) intelligible
nper, hop = 1024, 256
_, _, X = stft(x, SR, nperseg=nper, noverlap=nper - hop)
_, _, C = stft(carrier, SR, nperseg=nper, noverlap=nper - hop)
EX = uniform_filter1d(np.abs(X), size=9, axis=0)            # spectral envelope of the voice
EC = uniform_filter1d(np.abs(C), size=9, axis=0) + 1e-6
_, voc = istft(C * (EX / EC), SR, nperseg=nper, noverlap=nper - hop)
voc = voc[:len(x)]; voc = np.pad(voc, (0, len(x) - len(voc)))
voc *= np.sqrt(np.mean(x ** 2) / max(np.mean(voc ** 2), 1e-12))
ring = x * np.sin(2 * np.pi * 52 * t)                      # ring modulation (metallic tremble)
mixv = 0.55 * voc + 0.30 * ring + 0.32 * x
# noise gate from the voice itself: the buzz/noise carrier must stay silent between words
_rms = np.sqrt(uniform_filter1d(x ** 2, size=int(0.02 * SR)) + 1e-12)
_gate = np.clip((20 * np.log10(_rms) + 52) / 14, 0, 1)
mixv *= uniform_filter1d(_gate, size=int(0.015 * SR))
tmpw = P / "production/_robot_tmp.wav"
with wave.open(str(tmpw), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mixv / (np.abs(mixv).max() + 1e-9) * 0.9, -1, 1) * 32767).astype(np.int16).tobytes())
POST = ("aecho=0.9:0.6:5|9:0.32|0.22,"
        "highpass=f=120,lowpass=f=11000,equalizer=f=280:t=q:w=1.0:g=-2.5,equalizer=f=1800:t=q:w=1.2:g=2.5,equalizer=f=6500:t=q:w=1.4:g=-1.5,"
        "acompressor=threshold=-22dB:ratio=3.5:attack=5:release=80:makeup=2,"
        "aecho=0.85:0.2:36|61:0.10|0.07,volume=6dB,alimiter=limit=0.8:attack=4:release=60:level=false")
wet = dec(tmpw, POST); tmpw.unlink()
n = min(len(dry), len(wet)); dry, wet = dry[:n], wet[:n]
mask = np.zeros(n)
wins = []
for sid in ("s06", "s09", "s12", "s15"):
    sc = next(s for s in T["scenes"] if s["id"] == sid)
    a = T["words"][sc["w0"]]["s"] - off - 0.12; b = T["words"][sc["w1"]]["e"] - off + 0.18
    wins.append((a, b)); i0, i1 = int(a * SR), int(b * SR); mask[i0:i1] = 1
r = int(0.03 * SR); ker = np.hanning(2 * r + 1); ker /= ker.sum()
mask = np.convolve(mask, ker, mode="same")
# loudness match the robot segments to the dry voice (RMS over the windows)
sel = mask > 0.5
g = np.sqrt(np.mean(dry[sel] ** 2) / max(np.mean(wet[sel] ** 2), 1e-12))
wet_g = wet * g
from scipy.ndimage import maximum_filter1d
_env = maximum_filter1d(np.abs(wet_g), size=480) + 1e-9           # 10 ms look-around peak limiter (no clipped samples)
wet_g *= uniform_filter1d(np.minimum(1.0, 0.9 / _env), size=480)
out = dry * (1 - mask) + wet_g * mask
out = np.clip(out, -0.98, 0.98)
dst = P / "assets/audio/vo_collab.wav"
with wave.open(str(dst), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())
print("wrote", dst, "robot windows (VO time):", [(round(a, 2), round(b, 2)) for a, b in wins], "gain", round(g, 2))
