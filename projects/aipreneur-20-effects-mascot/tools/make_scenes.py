#!/usr/bin/env python3
"""production/scenes.json — every cut sits ~0.08 s before the first word of its scene (frame-snapped, 30 fps).
D = VO length + a 0.4 s quiet brand hold (the VO plays to its last sample; nothing is cut)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
wt = json.loads((P / "production/word_timing.json").read_text())
W = wt["words"]
D = round(round((wt["audio_duration"] + 0.41) * 30) / 30, 4)
snap = lambda t: round(round(t * 30) / 30, 4)
cut = lambda i, lead=0.08: snap(W[i]["start"] - lead)
# (id, effect number or None, label, start)
ROWS = [
    ("s00", None, "COLD OPEN", 0.0),
    ("s01", None, "SATU KLIP POLOS", cut(8)),
    ("s02", 1, "ORBIT", cut(13)),
    ("s03", 2, "CHAT TAKEOVER", cut(17)),
    ("s04", 3, "FRAME ESCAPE", cut(21)),
    ("s05", 4, "SNAP ZOOM", cut(25)),
    ("s06", 5, "CHECKLIST POP", cut(30)),
    ("s07", 6, "HEADLINE STORM", cut(35)),
    ("s08", 7, "ZOOM PORTAL", cut(37)),
    ("s09", 8, "GROWTH CURVE", cut(41)),
    ("s10", 9, "STUDIO REVEAL", cut(48)),
    ("s11", 10, "B-ROLL OVERLAY", cut(54)),
    ("s12", 11, "PAPER CUTOUT", cut(63)),
    ("s13", 12, "DOLLY ZOOM", snap(W[67]["start"] - 0.06)),     # "kertas," -> the paper edge becomes the rail
    ("s14", 13, "MAGAZINE COVER", snap(W[69]["start"] - 0.06)),  # "ke sampul majalah"
    ("s15", 14, "LIQUID GLASS", cut(72)),
    ("s16", 15, "ZOOM THROUGH CUT", cut(77)),
    ("s17", 16, "GREEN SCREEN", cut(82)),
    ("s18", 17, "FRAME BREAK", cut(86)),
    ("s19", 18, "DIGITAL ZOOM", snap(W[87]["start"] + 0.12)),   # shards clear during "layar,"
    ("s20", 19, "PHONE MOCKUP", snap(W[90]["start"] - 0.04)),   # "ke tampilan HP."
    ("s21", 20, "CHECKLIST", cut(93)),
    ("s22", None, "RAHASIANYA: KONTINUITAS", cut(101)),
    ("s23", None, "CLAUDE CODE", cut(114)),
    ("s24", None, "ARAHAN + PENGECEKAN", cut(125)),
    ("s25", None, "KOMEN EDIT", cut(133)),
]
sc = []
for k, (sid, n, label, t0) in enumerate(ROWS):
    t1 = ROWS[k + 1][3] if k + 1 < len(ROWS) else D
    sc.append({"id": sid, "fx": n, "label": label, "start": t0, "end": t1, "dur": round(t1 - t0, 4)})
(P / "production/scenes.json").write_text(json.dumps({"fps": 30, "duration": D, "vo_duration": wt["audio_duration"], "scenes": sc}, indent=1))
for s in sc:
    print(f'{s["id"]} {str(s["fx"] or "-"):>3} {s["start"]:6.3f}-{s["end"]:6.3f} ({s["dur"]:.2f}) {s["label"]}')
print("D", D)
