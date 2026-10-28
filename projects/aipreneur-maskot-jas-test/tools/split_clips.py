#!/usr/bin/env python3
"""Cut out/aipreneur-17-efek_all.mp4 into 17 frame-exact 1080x1080 clips: out/efek_NN_<name>.mp4 (silent, H.264, CRF 16)."""
import json, subprocess
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sc = json.loads((P / "production/scenes.json").read_text())
fps, src = sc["fps"], P / "out/aipreneur-17-efek_all.mp4"
for s in sc["scenes"]:
    a, b = round(s["start"] * fps), round(s["end"] * fps)
    dst = P / f"out/efek_{s['fx']:02d}_{s['label']}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vf", f"trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS",
                    "-an", "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(fps), "-movflags", "+faststart", str(dst)], check=True)
    print(dst.name)
