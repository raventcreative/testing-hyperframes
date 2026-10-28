#!/usr/bin/env python3
"""index.html (root): pale AIpreneur plate -> sNN back -> 3D mascot -> sNNf front -> grain. No text, no audio."""
import json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
from xk import r3
sc = json.loads((P / "production/scenes.json").read_text())
D, SC = sc["duration"], sc["scenes"]
cut = lambda t: 0.0 if t <= 0 else round(t - 0.001, 4)
hosts = {"back": [], "front": []}
for s in SC:
    a, b = cut(s["start"]), (cut(s["end"]) if s["end"] < D else D)
    for suf, z, tr in (("", "back", 2), ("f", "front", 5)):
        hosts[z].append(f'      <div id="{s["id"]}{suf}" class="clip host-{z}" data-composition-id="{s["id"]}{suf}" data-composition-src="compositions/{s["id"]}{suf}.html" '
                        f'data-start="{r3(a)}" data-duration="{r3(b - a)}" data-track-index="{tr}" data-width="1080" data-height="1080"></div>')
index = f"""<!doctype html>
<html lang="id" data-resolution="square">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1080" />
    <title>AIpreneur — Maskot Jas (tes)</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <link rel="stylesheet" href="vendor/fx.css" />
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1080px; overflow: hidden; background: #eef4fc; }}
      body {{ font-family: "Poppins", sans-serif; font-synthesis: none; color: #0A0D2C; -webkit-font-smoothing: antialiased; }}
      #main {{ position: relative; width: 1080px; height: 1080px; overflow: hidden; isolation: isolate; background: #eef4fc; }}
      #bg {{ position: absolute; inset: 0; z-index: 0; background: url(assets/brand/bg_1080.png) 0 0 / 1080px 1080px no-repeat; }}
      .host-back {{ z-index: 10 !important; position: absolute !important; }}
      #mascot {{ z-index: 40 !important; position: absolute !important; }}
      .host-front {{ z-index: 50 !important; position: absolute !important; }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 1208px; z-index: 80; opacity: .3; background: url(assets/brand/grain_256.png); pointer-events: none; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{r3(D)}" data-width="1080" data-height="1080" data-fps="30">
      <div id="bg" data-layout-ignore></div>
{chr(10).join(hosts["back"])}
      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{r3(D)}" data-track-index="3" data-width="1080" data-height="1080"></div>
{chr(10).join(hosts["front"])}
      <div id="grain" data-layout-ignore></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {r3(D)}, ease: "steps({int(D * 12)})", immediateRender: false }}, 0);
        tl.set({{}}, {{}}, {r3(D - 0.01)});
        window.__timelines["main"] = tl;
      }})();
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(index)
print("index:", len(SC), "scenes, D =", D)
