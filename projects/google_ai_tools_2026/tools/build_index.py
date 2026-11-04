"""Builds index.html from the REF-H starter + production/timing.json (verified word timings, scene cuts, caption chunks).
Scenes stay in compositions/sNN.html (one per spoken phrase). Missing scene files are created from the template.
Run: python3 -I tools/build_index.py ."""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
KIT = P.parents[1] / "deliverables/HyperFrame_PremiumMotion_V3/house_style_kit/starter"
T = json.loads((P / "production/timing.json").read_text())
VO_FILE = "ElevenLabs_2026-11-04T06_02_17_Dakocan - Expressive, Cheerful and Clear_pvc_sp100_s40_sb50_v4.mp3"
total = T["total_sec"]
html = (KIT / "index.html").read_text()
fonts = """      @font-face { font-family: Montserrat; src: url(assets/fonts/montserrat-latin-400-normal.woff2) format("woff2"); font-weight: 400; }
      @font-face { font-family: Montserrat; src: url(assets/fonts/montserrat-latin-700-normal.woff2) format("woff2"); font-weight: 700; }
      @font-face { font-family: Montserrat; src: url(assets/fonts/montserrat-latin-900-normal.woff2) format("woff2"); font-weight: 900; }
"""
html = html.replace("      /* ===== shared design kit", fonts + "      /* ===== shared design kit", 1)
rep = {"{{TITLE}}": "Google AI Tools 2026", "{{TOTAL_SEC}}": f"{total}", "{{TOTAL_SEC_HALF}}": f"{total / 2:.4f}",
       "{{TOTAL_SEC_X10}}": str(int(round(total * 10))), "{{VO_FILE}}": VO_FILE, "{{VO_SEC}}": f"{T['vo_sec']}"}
for k, v in rep.items(): html = html.replace(k, v)
# scene slots
slot_old = html[html.index('      <div id="s01" data-composition-id="s01"'):html.index('\n', html.index('      <div id="s01" data-composition-id="s01"')) + 1]
slots = "".join(f'      <div id="{s["id"]}" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" data-start="{s["start"]}" '
                f'data-duration="{s["dur"]}" data-track-index="{2 + k % 3}" data-width="1080" data-height="1920"></div>\n' for k, s in enumerate(T["scenes"]))
html = html.replace(slot_old, slots)
# words + captions
W = ",\n          ".join(json.dumps([w["w"], w["s"]], ensure_ascii=False) for w in T["words"])
a = html.index("        const W = ["); b = html.index("];", a) + 2
html = html[:a] + "        const W = [\n          " + W + "\n        ];" + html[b:]
C = ",\n          ".join(json.dumps(c) for c in T["caps"])
a = html.index("        const CAPS = ["); b = html.index("];", a) + 2
html = html[:a] + "        const CAPS = [\n          " + C + "\n        ];" + html[b:]
assert "{{" not in html, html[html.index("{{"):html.index("{{") + 60]
(P / "index.html").write_text(html)
tpl = (KIT / "compositions/_scene_template.html").read_text()
for s in T["scenes"]:
    f = P / f"compositions/{s['id']}.html"
    if not f.exists():
        f.write_text(tpl.replace("sXX", s["id"]).replace("const DUR = 2.5;", f"const DUR = {s['dur']};"))
print("index.html: scenes", len(T["scenes"]), "words", len(T["words"]), "caps", len(T["caps"]), "total", total)
