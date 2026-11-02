#!/usr/bin/env python3
"""Manual onset corrections measured on the waveform (soft 's' fricatives the CTC aligner starts late on).
Run after tools/vo_align.py. Index -> corrected start (s)."""
import json, re
from pathlib import Path
P = Path(__file__).resolve().parents[1]
FIX = {0: 0.18, 70: 29.74}          # Screenshot, Sekarang (energy rise of the 's', see transcript_review.md)
wt = json.loads((P / "production/word_timing.json").read_text())
for i, t in FIX.items():
    wt["words"][i]["start"] = t
for g in wt["caption_groups"]:
    if g["word_idx"][0] in FIX and g["start"] > 0:
        g["start"] = round(FIX[g["word_idx"][0]] - 0.1, 3)
for k in range(len(wt["caption_groups"]) - 1):
    wt["caption_groups"][k]["end"] = wt["caption_groups"][k + 1]["start"]
(P / "production/word_timing.json").write_text(json.dumps(wt, indent=1, ensure_ascii=False))
js = (P / "vendor/vo_words.js").read_text()
m = re.search(r"window\.VO_WORDS = (\[.*?\]);", js, re.S)
vw = json.loads(m.group(1))
for i, t in FIX.items():
    vw[i][1] = t
js = js.replace(m.group(0), "window.VO_WORDS = " + json.dumps(vw, separators=(",", ":"), ensure_ascii=False) + ";")
(P / "vendor/vo_words.js").write_text(js)
print("fixed", FIX)
