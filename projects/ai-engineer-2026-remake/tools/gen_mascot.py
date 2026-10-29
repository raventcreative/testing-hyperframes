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
wave = []
for si, s in enumerate(SCENES["scenes"]):
    t = r3(s["start"])
    lines.append(f"      // ---- {s['id']} {s['label']} ({s['start']}-{s['end']})")
    lines.append(f"      vt.set(V, RESET.V, {t}); vt.set(\"#m-xf\", RESET.X, {t}); vt.set(\"#m-clip\", RESET.C, {t});")
    f = P / f"production/mtrack/{s['id']}.js"
    if f.exists():
        lines += ["      " + l for l in f.read_text().splitlines() if l.strip()]
# the opening "hai" wave (s01, before the first explain gesture) is kept; everything else = shared acting director
s01 = json.loads((P / "production/acting/s01.json").read_text())
wave = [list(k) for k in s01.get("armR", []) if k[0] < 1.7] + [[1.7, "rest", 0.45]]
intents = [{"t": 0.05, "action": "idle", "until": 1.6}]
acting = (f"      const DIR = M3.direct(VW, D, {{ intents: {js(intents)}, seed: 5, quiet: 0.3 }});\n"
          f"      DIR.tracks.armR = DIR.tracks.armR.filter((k) => k[0] >= 1.7 || k[0] === 0).concat({js(wave)}).sort((a, b) => a[0] - b[0]);\n"
          "      const PERF0 = buildPerformance(DIR.tracks, D + 0.05);\n"
          "      const PERF = (t) => PERF0(t);\n")
extra = P / "tools/mascot_extra.js"
acting += extra.read_text() if extra.exists() else "      const EXTRA = (t) => ({});\n"
cfg = {"__DUR__": str(D), "__RESET__": js({"V": RESET_V, "X": RESET_X, "C": RESET_C}),
       "__TRACK__": "\n".join(lines), "__ACTING__": acting,
       "__FACE__": (P / "tools/mascot_face.json").read_text().strip(), "__DECALS__": (P / "tools/decals.json").read_text().strip(),
       "__CUTS__": js([s["start"] for s in SCENES["scenes"][1:]])}
src = (P / "tools/mascot_src.html").read_text()
for k, v in cfg.items():
    src = src.replace(k, v)
(P / "compositions/mascot.html").write_text(src)
print("mascot.html written,", len(lines), "track lines (director acting)")
