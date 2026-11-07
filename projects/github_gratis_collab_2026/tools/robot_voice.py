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
CHAIN = ("rubberband=pitch=1.189:formant=preserved:transients=crisp,"
         "asplit[a][b];[b]afreqshift=shift=42[bs];[a][bs]amix=inputs=2:weights='0.68 0.32':normalize=0,"
         "aecho=0.85:0.55:6|11:0.28|0.18,acrusher=bits=12:mode=log:aa=1:mix=0.1,"
         "highpass=f=190,lowpass=f=7600,equalizer=f=2600:t=q:w=1.2:g=3,volume=10dB,alimiter=limit=0.8:attack=4:release=60:level=false")
wet = dec(vo, CHAIN)
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
out = dry * (1 - mask) + wet_g * mask
out = np.clip(out, -0.98, 0.98)
dst = P / "assets/audio/vo_collab.wav"
with wave.open(str(dst), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())
print("wrote", dst, "robot windows (VO time):", [(round(a, 2), round(b, 2)) for a, b in wins], "gain", round(g, 2))
