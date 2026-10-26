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

# ---- REF-H ambient layers (house style bible §5): 22 seeded glass motes rising, drifting haze, grid, stepped grain
R = Rng(20261021)
parts, ptl = [], []
for k in range(22):
    sz = 4 + R.u(0, 9)
    x, y = R.u(0, 1080), 300 + R.u(0, 1500)
    parts.append(f'      <div class="mote" id="mote{k}" style="left:{r3(x)}px;top:{r3(y)}px;width:{r3(sz)}px;height:{r3(sz)}px;opacity:{r3(0.3 + R.u(0, 0.45))}"></div>')
    ptl.append(f'        tl.fromTo("#mote{k}", {{ y: 0 }}, {{ y: {r3(-(120 + R.u(0, 240)))}, duration: {r3(D)}, ease: "none", immediateRender: false }}, 0);')
H = round(D / 2, 3)
ptl += [f'        tl.fromTo("#haze-a", {{ x: 0, y: 0 }}, {{ x: 70, y: 60, duration: {H}, ease: "sine.inOut", yoyo: true, repeat: 1, immediateRender: false }}, 0);',
        f'        tl.fromTo("#haze-b", {{ x: 0, y: 0 }}, {{ x: -90, y: -50, duration: {H}, ease: "sine.inOut", yoyo: true, repeat: 1, immediateRender: false }}, 0);',
        f'        tl.fromTo("#bggrid", {{ x: 0, y: 0 }}, {{ x: 27, y: 27, duration: {r3(D)}, ease: "none", immediateRender: false }}, 0);',
        f'        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {r3(D)}, ease: "steps({int(D * 10)})", immediateRender: false }}, 0);']

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
      /* REF-H ground (house style bible §5): supplied pastel plate + 54 px paper grid + drifting haze + motes + grain */
      #bg {{ position: absolute; inset: 0; z-index: 0; overflow: hidden; }}
      #bg .plate {{ position: absolute; inset: 0; background: url(assets/brand/pastel_background_1080x1920.png) center / cover no-repeat; }}
      #bggrid {{ position: absolute; inset: -60px;
        background: repeating-linear-gradient(90deg, rgba(41,75,119,0.055) 0 1px, transparent 1px 54px), repeating-linear-gradient(0deg, rgba(41,75,119,0.055) 0 1px, transparent 1px 54px);
        -webkit-mask-image: radial-gradient(ellipse 75% 60% at 50% 52%, #000 30%, transparent 85%); mask-image: radial-gradient(ellipse 75% 60% at 50% 52%, #000 30%, transparent 85%); }}
      .haze {{ position: absolute; border-radius: 50%; }}
      #haze-a {{ left: -260px; top: -120px; width: 900px; height: 900px; background: radial-gradient(circle, rgba(172,198,231,0.5), rgba(172,198,231,0) 68%); }}
      #haze-b {{ left: 420px; top: 1240px; width: 1000px; height: 1000px; background: radial-gradient(circle, rgba(203,219,244,0.55), rgba(203,219,244,0) 68%); }}
      #haze-c {{ left: 140px; top: 560px; width: 800px; height: 800px; background: radial-gradient(circle, rgba(255,255,255,0.8), rgba(255,255,255,0) 66%); }}
      .mote {{ position: absolute; background: url(assets/brand/mote_64.png) center / 100% 100% no-repeat; z-index: 3; }}
      #world {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 10; transform-origin: 590px 930px; }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 2048px; z-index: 70; opacity: .5; background: url(assets/brand/grain_256.png); pointer-events: none; }}
      .scene-host {{ z-index: 10; }}
      #mascot {{ z-index: 40 !important; position: absolute !important; }}
      #captions {{ z-index: 60 !important; position: absolute !important; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{r3(D)}" data-width="1080" data-height="1920" data-fps="30">
      <div id="bg" data-layout-ignore><div class="plate"></div><div id="bggrid"></div><div id="haze-a" class="haze"></div><div id="haze-b" class="haze"></div><div id="haze-c" class="haze"></div></div>
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
        parts_.append(f'<span class="m"><span class="w{" key" if wi in hl else ""}" id="cw{wi}">{t}</span></span>')
    marks.append(f'    <div class="cg" id="cg{gi}"><div class="cl">{" ".join(parts_)}</div></div>')
    gs, ge = g["start"], min(g["end"], D)
    init.append(f'gsap.set("#cg{gi}", {{ opacity: {1 if gs <= 0 else 0} }});')
    if gs > 0:
        tl.append(f'tl.set("#cg{gi}", {{ opacity: 1 }}, {r3(gs)});')
    for wi in g["word_idx"]:
        ws = max(gs + 0.01, words[wi]["start"] - 0.08)
        init.append(f'gsap.set("#cw{wi}", {{ yPercent: 110, opacity: 0 }});')
        tl.append(f'tl.set("#cw{wi}", {{ opacity: 1 }}, {r3(ws)});')
        tl.append(f'tl.fromTo("#cw{wi}", {{ yPercent: 110 }}, {{ yPercent: 0, duration: 0.34, ease: "power4.out", immediateRender: false }}, {r3(ws)});')
    if gi + 1 < len(groups):
        tl.append(f'tl.set("#cg{gi}", {{ opacity: 0 }}, {r3(ge)});')

cap = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    /* REF-H caption (bible §5.7): top 232, sides 70, centred, Montserrat 700 46/1.22, ink; each word rises out of an
       overflow mask; key words navy + ice highlighter. One block per phrase (1–2 lines). */
    .cg {{ position: absolute; left: 70px; top: 232px; width: 940px; height: 148px; display: flex; align-items: flex-start; justify-content: center; }}
    .cl {{ width: 940px; text-align: center; font: 700 46px/1.22 Montserrat, sans-serif; letter-spacing: -0.01em; color: #202b3b; }}
    .m {{ display: inline-block; overflow: hidden; vertical-align: top; padding: 0.04em 0.06em 0.14em; margin: -0.04em -0.06em -0.14em; }}
    .w {{ display: inline-block; }}
    .key {{ color: #294b77; background: linear-gradient(transparent 62%, rgba(172,198,231,0.75) 62%, rgba(172,198,231,0.75) 92%, transparent 92%); }}
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
