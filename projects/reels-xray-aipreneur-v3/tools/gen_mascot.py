"""compositions/mascot.html = tools/mascot_src.html + tools/mascot_acting.js (performance windows) + face calibration."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sc = json.loads((P / "production/scenes.json").read_text())
cfg = {"__DUR__": str(sc["duration"]),
       "__HOST__": '{ fx: 230, fy: 2075, h: 760 }', "__HOSTBIG__": '{ fx: 305, fy: 2085, h: 840 }',
       "__FACE__": (P / "tools/mascot_face.json").read_text().strip(),
       "__WINDOWS__": (P / "tools/mascot_acting.js").read_text()}
src = (P / "tools/mascot_src.html").read_text()
for k, v in cfg.items():
    src = src.replace(k, v)
(P / "compositions/mascot.html").write_text(src)
print("mascot.html written")
