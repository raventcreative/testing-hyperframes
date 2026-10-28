#!/usr/bin/env python3
"""production/scenes.json — 15 scenes, every cut ~0.08 s before the first word of its phrase (frame-snapped, 30 fps).
D = VO length + ~0.33 s still hold."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
wt = json.loads((P / "production/word_timing.json").read_text())
W = wt["words"]
D = round(round((wt["audio_duration"] + 0.33) * 30) / 30, 4)
snap = lambda t: round(round(t * 30) / 30, 4)
cut = lambda i, lead=0.08: snap(W[i]["start"] - lead)
ROWS = [  # id, module number (1..10) or None, label, first word index
    ("s01", None, "HOOK", 0), ("s02", None, "10 KOMPONEN", 19), ("s03", 1, "PYTHON", 32),
    ("s04", 2, "SOFTWARE ENGINEERING", 48), ("s05", 3, "MACHINE LEARNING", 67), ("s06", 4, "DEEP LEARNING", 85),
    ("s07", 5, "LLM", 96), ("s08", 6, "AI APPLICATION", 107), ("s09", 7, "RAG", 123), ("s10", 8, "AI AGENT", 141),
    ("s11", 9, "EVALUATION", 161), ("s12", 10, "PRODUCTION", 175), ("s13", None, "PILIH JALUR", 185),
    ("s14", None, "SATU PROYEK DULU", 199), ("s15", None, "SISTEM AI YANG BEKERJA", 215),
]
sc = []
for k, (sid, n, label, wi) in enumerate(ROWS):
    t0 = 0.0 if k == 0 else cut(wi)
    t1 = cut(ROWS[k + 1][3]) if k + 1 < len(ROWS) else D
    w1 = ROWS[k + 1][3] - 1 if k + 1 < len(ROWS) else len(W) - 1
    sc.append({"id": sid, "fx": n, "label": label, "start": t0, "end": t1, "dur": round(t1 - t0, 4), "words": [wi, w1]})
(P / "production/scenes.json").write_text(json.dumps({"fps": 30, "duration": D, "vo_duration": wt["audio_duration"], "scenes": sc}, indent=1))
for s in sc:
    print(f'{s["id"]} {str(s["fx"] or "-"):>3} {s["start"]:7.3f}-{s["end"]:7.3f} ({s["dur"]:.2f}) w{s["words"]} {s["label"]}')
print("D", D)
