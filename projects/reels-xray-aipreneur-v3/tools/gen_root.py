#!/usr/bin/env python3
"""index.html (root) + compositions/captions.html for REELS X-RAY.
Sources: production/word_timing.json (measured VO timing), production/scenes.json, production/sfx_plan.json,
production/director_camera.json (Smart Motion Director camera moves on #world).
Run: python3 tools/gen_root.py
"""
import html, json, math, sys
from pathlib import Path

P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
from xk import Rng, r3

wt = json.loads((P / "production/word_timing.json").read_text())
sc = json.loads((P / "production/scenes.json").read_text())
words, D = wt["words"], sc["duration"]

def cut(t):
    return 0.0 if t <= 0 else round(t - 0.001, 4)

hosts = []
for s in sc["scenes"]:
    a, b = cut(s["start"]), (cut(s["end"]) if s["end"] < D else D)
    hosts.append(f'        <div id="{s["id"]}" class="clip scene-host" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" '
                 f'data-start="{r3(a)}" data-duration="{r3(b - a)}" data-track-index="2" data-track-kind="graphics" data-width="1080" data-height="1920"></div>')

# ---- floating atmospheric particles (seeded), three depths
R = Rng(20261026)
parts, ptl = [], []
for k in range(38):
    depth = k % 3
    sz = [3, 5, 9][depth] + R.u(0, 2)
    x, y = R.u(20, 1060), R.u(120, 1880)
    op = [0.5, 0.85, 0.4][depth]
    parts.append(f'      <div class="pt" id="pt{k}" style="left:{r3(x)}px;top:{r3(y)}px;width:{r3(sz)}px;height:{r3(sz)}px;opacity:{op}"></div>')
    dy = -[60, 120, 220][depth] - R.u(0, 60)
    dx = R.u(-30, 30)
    ptl.append(f'        tl.fromTo("#pt{k}", {{ x: 0, y: 0 }}, {{ x: {r3(dx)}, y: {r3(dy)}, duration: {r3(D)}, ease: "none", immediateRender: false }}, 0);')

# ---- SFX
sfx_tags = []
sp = P / "production/sfx_plan.json"
SFX = json.loads(sp.read_text()) if sp.exists() else []
lanes = {}
def lane(t0, t1):
    for ln in [5, 6, 7, 8, 9, 10]:
        if lanes.get(ln, -1) <= t0:
            lanes[ln] = t1
            return ln
    return 10
for i, fx in enumerate(sorted(SFX, key=lambda x: x["t"])):
    d = min(fx["dur"], D - fx["t"] - 0.005)
    sfx_tags.append(f'      <audio id="sfx{i:02d}" class="clip" src="assets/sfx/{fx["file"]}" data-start="{r3(fx["t"])}" data-duration="{r3(d)}" '
                    f'data-track-index="{lane(fx["t"], fx["t"] + d)}" data-volume="{fx["vol"]}"></audio>')

camp = P / "production/director_camera.json"
DIRCAM = [f'        MD.fx.{c["fx"]}({{ tl }}, {json.dumps(c["opts"])});' for c in (json.loads(camp.read_text()) if camp.exists() else [])]

index = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>REELS X-RAY — AIpreneur V3</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <script src="vendor/motion-director.js"></script>
    <link rel="stylesheet" href="vendor/xray.css" />
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #f4f7fc; }}
      body {{ font-family: "Montserrat", sans-serif; font-synthesis: none; color: #202b3b; -webkit-font-smoothing: antialiased; }}
      #main {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; isolation: isolate; }}
      /* Ice-Ivory ground: paper -> ice white, key light upper-left */
      #bg {{ position: absolute; inset: 0; z-index: 0;
        background: radial-gradient(ellipse 80% 55% at 22% 18%, rgba(255,255,255,.95) 0%, rgba(255,255,255,0) 70%),
                    radial-gradient(ellipse 90% 60% at 70% 92%, rgba(203,219,244,.55) 0%, rgba(203,219,244,0) 70%),
                    linear-gradient(180deg, #fffefb 0%, #f4f7fc 45%, #e8f0fb 100%); }}
      #bg-grid {{ position: absolute; inset: 0; z-index: 1; opacity: .9;
        background-image: linear-gradient(rgba(41,75,119,.045) 1px, transparent 1px), linear-gradient(90deg, rgba(41,75,119,.045) 1px, transparent 1px),
                          linear-gradient(rgba(41,75,119,.035) 1px, transparent 1px), linear-gradient(90deg, rgba(41,75,119,.035) 1px, transparent 1px);
        background-size: 48px 48px, 48px 48px, 240px 240px, 240px 240px; background-position: 6px 0, 6px 0, 6px 0, 6px 0; }}
      #bg-vig {{ position: absolute; inset: 0; z-index: 2; background: radial-gradient(ellipse 85% 70% at 50% 45%, rgba(232,240,251,0) 55%, rgba(172,198,231,.22) 100%); }}
      .pt {{ position: absolute; border-radius: 50%; background: #ffffff; box-shadow: 0 0 0 1px rgba(203,219,244,.7); z-index: 3; }}
      #world {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 10; transform-origin: 590px 930px; }}
      #grain {{ position: absolute; inset: 0; z-index: 70; opacity: .05; background-image: url("assets/elements/grain.png"); background-size: 256px 256px; pointer-events: none; }}
      .scene-host {{ z-index: 10; }}
      #mascot {{ z-index: 40 !important; position: absolute !important; }}
      #captions {{ z-index: 60 !important; position: absolute !important; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{r3(D)}" data-width="1080" data-height="1920" data-fps="30">
      <div id="bg" data-layout-ignore></div>
      <div id="bg-grid" data-layout-ignore></div>
      <div id="bg-vig" data-layout-ignore></div>
{chr(10).join(parts)}
      <!-- #world = everything the director camera moves (snap / digital zoom); host, captions and grain stay put -->
      <div id="world" data-layout-ignore>
{chr(10).join(hosts)}
      </div>
      <!-- 3D rigged mascot host (one WebGL canvas, acting + lip sync driven by the measured VO timing) -->
      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{r3(D)}" data-track-index="3" data-track-kind="graphics" data-width="1080" data-height="1920"></div>
      <div id="captions" class="clip" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{r3(D)}" data-track-index="1" data-track-kind="captions" data-width="1080" data-height="1920"></div>
      <div id="grain" data-layout-ignore></div>
      <!-- the one voice-over: user's ElevenLabs file, untouched (no stretch, no pitch) -->
      <audio id="vo" class="clip" src="assets/audio/vo_xray_elevenlabs.mp3" data-start="0" data-duration="{r3(wt["audio_duration"])}" data-track-index="4" data-volume="1"></audio>
{chr(10).join(sfx_tags)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
{chr(10).join(ptl)}
{chr(10).join(DIRCAM)}
        tl.set({{}}, {{}}, {r3(D - 0.01)});
        window.__timelines["main"] = tl;
      }})();
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(index)

# ------------------------------------------------------------------ captions.html
groups = wt["caption_groups"]
marks, init, tl = [], [], []
for gi, g in enumerate(groups):
    hl = set(g["highlight"])
    parts_ = []
    for wi in g["word_idx"]:
        t = html.escape(words[wi]["text"])
        if wi in hl:
            parts_.append(f'<span class="cw kw" id="cw{wi}"><span class="mk" id="mk{wi}"></span><span class="tx">{t}</span></span>')
        else:
            parts_.append(f'<span class="cw" id="cw{wi}"><span class="tx">{t}</span></span>')
    marks.append(f'    <div class="cg" id="cg{gi}"><div class="cl">{" ".join(parts_)}</div></div>')
    gs, ge = g["start"], min(g["end"], D)
    init.append(f'gsap.set("#cg{gi}", {{ opacity: {1 if gs <= 0 else 0} }});')
    if gs > 0:
        tl.append(f'tl.set("#cg{gi}", {{ opacity: 1 }}, {r3(gs)});')
    for wi in g["word_idx"]:
        ws = max(gs + 0.005, words[wi]["start"] - 0.04)
        init.append(f'gsap.set("#cw{wi}", {{ opacity: 0, y: 16, filter: "blur(5px)" }});')
        tl.append(f'tl.fromTo("#cw{wi}", {{ opacity: 0, y: 16, filter: "blur(5px)" }}, {{ opacity: 1, y: 0, filter: "blur(0px)", duration: 0.2, ease: "power3.out", immediateRender: false }}, {r3(ws)});')
        if wi in hl:
            init.append(f'gsap.set("#mk{wi}", {{ scaleX: 0 }});')
            tl.append(f'tl.fromTo("#mk{wi}", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.26, ease: "power3.inOut", immediateRender: false }}, {r3(ws + 0.06)});')
    if gi + 1 < len(groups):
        tl.append(f'tl.fromTo("#cg{gi}", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.07, ease: "power1.in", immediateRender: false }}, {r3(ge - 0.07)});')

cap = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    /* caption band y 232-380, centred, max two lines (Montserrat 700 46 px, ink; keywords navy on an ice-blue marker) */
    .cg {{ position: absolute; left: 80px; top: 232px; width: 920px; height: 148px; display: flex; align-items: center; justify-content: center; }}
    .cl {{ width: 920px; text-align: center; font-family: "Montserrat", sans-serif; font-weight: 700; font-size: 46px; line-height: 1.28; letter-spacing: -0.01em; color: #202b3b; text-shadow: 0 0 10px rgba(255,254,251,.95), 0 0 22px rgba(255,254,251,.8); }}
    .cw {{ display: inline-block; position: relative; white-space: nowrap; }}
    .cw .tx {{ position: relative; }}
    .kw {{ color: #294b77; }}
    .mk {{ position: absolute; left: -6px; right: -6px; top: 52%; height: 40%; border-radius: 6px; background: #cbdbf4; transform-origin: 0% 50%; }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
{chr(10).join(marks)}
  </div>
  <script>
    (function () {{
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {(chr(10) + '      ').join(init)}
      {(chr(10) + '      ').join(tl)}
      tl.set({{}}, {{}}, {r3(D - 0.02)});
      window.__timelines["captions"] = tl;
    }})();
  </script>
</template>
"""
(P / "compositions/captions.html").write_text(cap)
print(f"index.html: {len(hosts)} scenes, {len(sfx_tags)} sfx, {len(DIRCAM)} director camera moves; captions: {len(groups)} groups; D={D}")
