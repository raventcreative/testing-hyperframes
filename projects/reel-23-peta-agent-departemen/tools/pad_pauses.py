"""Lengthen a few natural sentence pauses in the ElevenLabs VO (silence inserted at the quietest point of each pause) so the
scene transitions can finish before the next VO line. Source: assets/audio/vo.mp3 (TTS output, untouched) -> assets/audio/vo.wav.
Run: python3 -I tools/pad_pauses.py <project>"""
import subprocess, sys, wave
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
PADS = [(4.40, 4.66, 0.35), (10.15, 10.55, 0.30), (15.86, 16.22, 1.35), (22.10, 22.52, 0.55), (28.30, 28.50, 0.35), (33.68, 33.92, 0.35), (40.10, 40.38, 0.25), (44.68, 44.94, 0.40)]   # (search from, to, seconds added)
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(P / "assets/audio/vo.mp3"), "-ac", "1", "-ar", "44100", "-f", "s16le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32); sr = 44100
win = int(0.03 * sr); out, last = [], 0
for a, b, add in PADS:
    i0, i1 = int(a * sr), int(b * sr)
    e = np.convolve(np.abs(x[i0:i1]), np.ones(win) / win, mode="same"); k = i0 + int(np.argmin(e))
    out += [x[last:k], np.zeros(int(add * sr), np.float32)]; last = k
    print(f"pad {add:.2f}s at {k / sr:.3f}s (level {e.min():.1f})")
out.append(x[last:]); y = np.concatenate(out).astype(np.int16)
with wave.open(str(P / "assets/audio/vo.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(y.tobytes())
print("vo.wav", round(len(y) / sr, 2), "s")
