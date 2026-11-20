"""R30: inserts a short breath (PAD s of silence) before the lines that open a new section (loop, module 1/2/3, Claude Code, outro),
so every section change gets a beat for its transition and the reel keeps the reference's length (~92 s) without slowing the voice.
Reads production/vo_el.mp3 + production/vo_el_raw.json (ElevenLabs output), writes assets/audio/vo.mp3 + production/vo_el.json
(line times and character alignment shifted).   Run: python3 -I tools/vo_pad.py ."""
import json, subprocess, sys
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
PAD, SR = 0.7, 44100
BEFORE = [2, 4, 6, 8, 10, 12]          # 0-based line indexes that start a new section
d = json.loads((P / "production/vo_el_raw.json").read_text())
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(P / "production/vo_el.mp3"), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(pcm, np.int16)
L = d["lines"]; cuts = [round((L[i - 1]["end"] + L[i]["start"]) / 2, 3) for i in BEFORE]
parts, prev = [], 0
for c in cuts:
    k = int(c * SR); parts += [a[prev:k], np.zeros(int(PAD * SR), np.int16)]; prev = k
parts.append(a[prev:]); out = np.concatenate(parts)
sh = lambda t: round(t + PAD * sum(1 for c in cuts if t >= c), 3)
for l in L: l["start"], l["end"] = sh(l["start"]), sh(l["end"])
al = d["align"]; al["start"] = [sh(t) for t in al["start"]]; al["end"] = [sh(t) for t in al["end"]]
d["duration"] = round(len(out) / SR, 3); d["pad"] = {"sec": PAD, "at_raw": cuts}
(P / "production/vo_el.json").write_text(json.dumps(d, ensure_ascii=False, indent=1))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "libmp3lame", "-b:a", "128k",
                str(P / "assets/audio/vo.mp3")], input=out.tobytes(), check=True)
print("cuts", cuts, "->", d["duration"], "s")
