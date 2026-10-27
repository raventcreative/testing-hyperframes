#!/usr/bin/env python3
"""production/scenes.json — 17 silent effect demos, SEG seconds each, one per PDF effect (cut later into 17 MP4s)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
SEG = 5.0
FX = ["orbit", "couch_wall", "ui_world", "frame_break", "digital_zoom", "phone_mockup", "checklist", "headline_wall",
      "zoom_cut", "chart_grow", "pull_back_reveal", "green_screen", "paper_cut", "doodle_boil", "vertigo", "cover_story", "glass_type"]
sc = [{"id": f"s{k + 1:02d}", "fx": k + 1, "label": n, "start": round(k * SEG, 4), "end": round((k + 1) * SEG, 4), "dur": SEG} for k, n in enumerate(FX)]
D = round(len(FX) * SEG, 4)
(P / "production/scenes.json").write_text(json.dumps({"fps": 30, "duration": D, "seg": SEG, "scenes": sc}, indent=1))
# silent stubs (no VO): neutral mouth, no accents
(P / "vendor/vo_words.js").write_text("// no voice-over in this project: closed neutral mouth\nwindow.VO_WORDS = [];\nwindow.VO_PHONES = [];\n"
                                      f"window.VO_ENV = new Array({int(D * 100) + 4}).fill(0);\n")
print("scenes", len(sc), "D", D)
