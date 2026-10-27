#!/usr/bin/env python3
"""production/scenes.json — every cut sits ~0.08 s before the first word of its scene (frame-snapped, 30 fps).
D = VO length + ~0.43 s still brand hold (the VO plays to its last sample)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
wt = json.loads((P / "production/word_timing.json").read_text())
W = wt["words"]
D = round(round((wt["audio_duration"] + 0.43) * 30) / 30, 4)
snap = lambda t: round(round(t * 30) / 30, 4)
cut = lambda i, lead=0.08: snap(W[i]["start"] - lead)
ROWS = [  # id, world number (1..6) or None, label, start
    ("s01", None, "1 VIDEO · 6 GAYA", 0.0),
    ("s02", 1, "EDITORIAL SPLIT", cut(9)),
    ("s03", 2, "OVER THE SHOULDER", cut(14)),
    ("s04", 3, "BACKDROP WORD", cut(26)),
    ("s05", 4, "GLASS WIDGETS", cut(36)),
    ("s06", 5, "SPOTLIGHT", cut(39)),
    ("s07", 6, "COLOR GRADE", cut(42)),
    ("s08", None, "RAHASIANYA", cut(48)),
    ("s09", None, "CARA BIKINNYA", cut(63)),
    ("s10", None, "KOMEN CLAUDE", cut(79)),
]
sc = []
for k, (sid, n, label, t0) in enumerate(ROWS):
    t1 = ROWS[k + 1][3] if k + 1 < len(ROWS) else D
    sc.append({"id": sid, "fx": n, "label": label, "start": t0, "end": t1, "dur": round(t1 - t0, 4)})
(P / "production/scenes.json").write_text(json.dumps({"fps": 30, "duration": D, "vo_duration": wt["audio_duration"], "scenes": sc}, indent=1))
for s in sc:
    print(f'{s["id"]} {str(s["fx"] or "-"):>3} {s["start"]:6.3f}-{s["end"]:6.3f} ({s["dur"]:.2f}) {s["label"]}')
print("D", D)
