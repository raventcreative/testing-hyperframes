"""Insert short silences at scene boundaries (lowest-energy point near each target) so every wipe/zoom finishes before the next VO line.
Reads assets/audio/vo_raw.wav, writes assets/audio/vo.wav. Run: python3 -I tools/pad_pauses.py <project>"""
import sys, wave
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
PADS = [(7.05, 0.50), (21.73, 0.45), (27.30, 1.10), (31.90, 1.10)]   # (target time in the raw take, extra silence in s)
w = wave.open(str(P / "assets/audio/vo_raw.wav")); sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).copy()
hop = int(sr * 0.02); out = []; pos = 0; shift = 0.0
for tgt, pad in PADS:
    lo, hi = int((tgt - 0.3) * sr), int((tgt + 0.3) * sr)
    seg = x[lo:hi].astype(np.float32); e = [np.sqrt(np.mean(seg[i:i + hop] ** 2)) for i in range(0, len(seg) - hop, hop)]
    cut = lo + int(np.argmin(e)) * hop + hop // 2
    out.append(x[pos:cut]); out.append(np.zeros(int(pad * sr), np.int16)); pos = cut
    print(f"pad {pad:.2f}s at raw {cut / sr:.2f}s (out {cut / sr + shift:.2f}s)"); shift += pad
out.append(x[pos:]); y = np.concatenate(out)
o = wave.open(str(P / "assets/audio/vo.wav"), "wb"); o.setnchannels(1); o.setsampwidth(2); o.setframerate(sr); o.writeframes(y.tobytes()); o.close()
print("vo.wav", round(len(y) / sr, 2), "s")
