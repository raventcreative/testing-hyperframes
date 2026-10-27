#!/usr/bin/env python3
"""compositions/mascot.html = tools/mascot_src.html + per-scene mascot tracks (production/mtrack/sNN.js)
+ acting merged from production/acting/sNN.json (auto talk pattern where a scene gives none) + face calibration.
Every scene start first resets the wrapper / view to neutral."""
import json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
from xk import SCENES, HERO, CLIP_NONE, WORDS, js, r3
D = SCENES["duration"]
WT = json.loads((P / "production/word_timing.json").read_text())
KEYW = {i for g in WT["caption_groups"] for i in g["highlight"]}
RESET_V = dict(HERO, fy=1800, h=1470, vis=1, rx=0, rz=0, ry=0, ty=0)
RESET_X = {"x": 0, "y": 0, "scale": 1, "rotation": 0, "rotationX": 0, "rotationY": 0, "opacity": 1, "transformPerspective": 1400,
           "filter": "drop-shadow(0px 0px 0px rgba(0,208,254,0))", "transformOrigin": "540px 960px"}
RESET_C = {"clipPath": CLIP_NONE}
lines = []
tracks = {k: [] for k in ("armL", "armR", "head", "torso", "root")}
for si, s in enumerate(SCENES["scenes"]):
    t = r3(s["start"])
    lines.append(f"      // ---- {s['id']} {s['label']} ({s['start']}-{s['end']})")
    lines.append(f"      vt.set(V, RESET.V, {t}); vt.set(\"#m-xf\", RESET.X, {t}); vt.set(\"#m-clip\", RESET.C, {t});")
    f = P / f"production/mtrack/{s['id']}.js"
    if f.exists():
        lines += ["      " + l for l in f.read_text().splitlines() if l.strip()]
    a = P / f"production/acting/{s['id']}.json"
    act = json.loads(a.read_text()) if a.exists() else {}
    ws = [(i, w) for i, w in enumerate(WORDS) if s["start"] - 0.02 <= w["start"] < s["end"] - 0.02]
    for tr in tracks:
        if act.get(tr):
            tracks[tr] += [list(k) for k in act[tr]]
            continue
        # automatic talk pattern (beats on key words, small head nods / turns on stressed words)
        if tr == "armL":
            tracks[tr].append([s["start"] + 0.02, "low", 0.4])
            for n, (i, w) in enumerate([x for x in ws if x[0] in KEYW][:2]):
                tracks[tr] += [[w["start"] - 0.14, "explain" if n % 2 == 0 else "palmUp", 0.3], [w["end"] + 0.2, "low", 0.4]]
        elif tr == "armR":
            tracks[tr].append([s["start"] + 0.02, "low", 0.4])
            kw = [x for x in ws if x[0] in KEYW]
            if len(kw) >= 1:
                w = kw[-1][1]
                tracks[tr] += [[w["start"] - 0.1, "open", 0.3], [w["end"] + 0.25, "low", 0.4]]
        elif tr == "head":
            for n, (i, w) in enumerate(ws):
                if n % 2 == 0:
                    sgn = 1 if (si + n // 2) % 2 == 0 else -1
                    tracks[tr].append([w["start"] - 0.05, [-0.04, 0.08 * sgn, 0.03 * sgn], 0.3])
            if not ws:
                tracks[tr].append([s["start"] + 0.05, [0, 0, 0], 0.4])
        elif tr == "torso":
            tracks[tr].append([s["start"] + 0.05, {}, 0.4])
        elif tr == "root":
            tracks[tr].append([s["start"] + 0.02, {"y": 0, "ry": 0, "rz": 0}, 0.4])
for tr in tracks:
    tracks[tr].sort(key=lambda k: k[0])
acting = (f"      const PERF0 = buildPerformance({js(tracks)}, D + 0.05);\n"
          "      const PERF = (t) => PERF0(t);\n")
extra = P / "tools/mascot_extra.js"
acting += extra.read_text() if extra.exists() else "      const EXTRA = (t) => ({});\n"
cfg = {"__DUR__": str(D), "__RESET__": js({"V": RESET_V, "X": RESET_X, "C": RESET_C}),
       "__TRACK__": "\n".join(lines), "__ACTING__": acting,
       "__FACE__": (P / "tools/mascot_face.json").read_text().strip()}
src = (P / "tools/mascot_src.html").read_text()
for k, v in cfg.items():
    src = src.replace(k, v)
(P / "compositions/mascot.html").write_text(src)
print("mascot.html written,", len(lines), "track lines,", {k: len(v) for k, v in tracks.items()}, "acting keys")
