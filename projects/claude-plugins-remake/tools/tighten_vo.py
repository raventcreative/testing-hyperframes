"""Tighten the ElevenLabs VO: shrink pauses longer than MAXP to MAXP (cut from the middle, 25 ms crossfade),
trim lead/tail, then time-stretch with ffmpeg atempo (pitch kept). Writes assets/audio/vo_tight.wav + production/vo_edit.json
Run: python3 -I tools/tighten_vo.py <project> [tempo]"""
import json, subprocess, sys
from pathlib import Path
import numpy as np
P = Path(sys.argv[1]).resolve(); TEMPO = float(sys.argv[2]) if len(sys.argv) > 2 else 1.15
SR = 44100; MAXP = 0.20; LEAD = 0.06
src = P / "assets/audio/vo_original_elevenlabs.mp3"
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.float32).copy()
hop = 441; n = len(a) // hop
db = 20 * np.log10(np.sqrt(np.mean(a[: n * hop].reshape(n, hop) ** 2, axis=1)) + 1e-7)
sil = db < -42
runs, i = [], 0
while i < n:
    if sil[i]:
        j = i
        while j < n and sil[j]: j += 1
        runs.append((i / 100, j / 100)); i = j
    else: i += 1
keep, cur = [], 0.0
for s, e in runs:
    if s <= 0.001:                       # lead
        cur = max(0, e - LEAD); continue
    if e >= len(a) / SR - 0.011:         # tail
        keep.append((cur, min(len(a) / SR, s + 0.25))); cur = None; break
    if e - s > MAXP:
        mid_l = s + MAXP / 2; mid_r = e - MAXP / 2
        keep.append((cur, mid_l)); cur = mid_r
if cur is not None: keep.append((cur, len(a) / SR))
X = int(0.025 * SR); out = np.zeros(0, np.float32)
for s, e in keep:
    seg = a[int(s * SR): int(e * SR)].copy()
    if len(out) >= X and len(seg) >= X:
        r = np.linspace(0, 1, X, dtype=np.float32)
        out[-X:] = out[-X:] * (1 - r) + seg[:X] * r; seg = seg[X:]
    out = np.concatenate([out, seg])
tmp = P / "production/_vo_cut.f32"; out.tofile(tmp)
dst = P / "assets/audio/vo_tight.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", str(tmp),
                "-af", f"atempo={TEMPO},alimiter=limit=0.89:level=false", "-ar", "48000", "-ac", "2", str(dst)], check=True)
tmp.unlink()
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(dst)], capture_output=True, text=True).stdout)
(P / "production/vo_edit.json").write_text(json.dumps({"source": src.name, "max_pause": MAXP, "tempo": TEMPO, "kept": keep, "cut_dur": len(out) / SR, "final_dur": dur}, indent=1))
print(f"original {len(a)/SR:.2f}s -> cut {len(out)/SR:.2f}s -> tempo {TEMPO} -> {dur:.2f}s, {len(keep)} segments")
