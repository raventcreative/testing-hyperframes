#!/usr/bin/env python3
"""index.html (root) + compositions/captions.html + compositions/hud.html.
Run after tools/make_scenes.py; SFX from production/sfx_plan.json (tools/gen_sfx.py)."""
import html, json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
from xk import r3
wt = json.loads((P / "production/word_timing.json").read_text())
sc = json.loads((P / "production/scenes.json").read_text())
words, D, SC = wt["words"], sc["duration"], sc["scenes"]
cut = lambda t: 0.0 if t <= 0 else round(t - 0.001, 4)

hosts = []
for s in SC:
    a, b = cut(s["start"]), (cut(s["end"]) if s["end"] < D else D)
    for suf, z, tr in (("", "back", 2), ("f", "front", 5)):
        hosts.append(f'      <div id="{s["id"]}{suf}" class="clip host-{z}" data-composition-id="{s["id"]}{suf}" data-composition-src="compositions/{s["id"]}{suf}.html" '
                     f'data-start="{r3(a)}" data-duration="{r3(b - a)}" data-track-index="{tr}" data-width="1080" data-height="1920"></div>')
back = [h for h in hosts if "host-back" in h]
front = [h for h in hosts if "host-front" in h]

# SFX
sp = P / "production/sfx_plan.json"
SFX = json.loads(sp.read_text()) if sp.exists() else []
lanes, sfx_tags = {}, []
def lane(t0, t1):
    for ln in range(10, 18):
        if lanes.get(ln, -1) <= t0:
            lanes[ln] = t1
            return ln
    return 17
for i, fx in enumerate(sorted(SFX, key=lambda x: x["t"])):
    d = min(fx["dur"], D - fx["t"] - 0.005)
    sfx_tags.append(f'      <audio id="sfx{i:02d}" class="clip" src="assets/sfx/{fx["file"]}" data-start="{r3(fx["t"])}" data-duration="{r3(d)}" '
                    f'data-track-index="{lane(fx["t"], fx["t"] + d)}" data-volume="{fx["vol"]}"></audio>')

# logo sheen: ~0.45 s glyph-clipped white-cyan band every ~9 s + once on the final CTA
SHEEN = [1.3] + [round(1.3 + 8.2 * k, 2) for k in range(1, 14) if 1.3 + 8.2 * k < D - 2] + [round(D - 0.95, 2)]
LW, LH = 204, round(204 * 112 / 1158, 2)
ltl = ['        tl.fromTo("#logo", { x: -8, opacity: 0 }, { x: 0, opacity: 1, duration: 0.28, ease: "power2.out", immediateRender: false }, 0.05);', '        gsap.set("#logo", { x: -8, opacity: 0 });'] + [f'        tl.fromTo("#logo-band", {{ x: 0 }}, {{ x: {LW + 200}, duration: 0.45, ease: "power2.inOut", immediateRender: false }}, {t});' for t in SHEEN]
ltl += [f'        tl.fromTo("#logo-glow", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, ease: "sine.out", immediateRender: false }}, {t});'
        f'\n        tl.fromTo("#logo-glow", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.3, ease: "sine.in", immediateRender: false }}, {r3(t + 0.2)});' for t in SHEEN]

index = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>AIpreneur — AI Engineer 2026</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <link rel="stylesheet" href="vendor/fx.css" />
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #eef4fc; }}
      body {{ font-family: "Poppins", sans-serif; font-synthesis: none; color: #0A0D2C; -webkit-font-smoothing: antialiased; }}
      #main {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; isolation: isolate; background: #eef4fc; }}
      /* supplied pale-blue plate, mirror-extended to 9:16 (tools/prep_brand.py, no stretch, no hue change) */
      #bg {{ position: absolute; inset: 0; z-index: 0; background: url(assets/brand/bg_1080x1920.png) 0 0 / 1080px 1920px no-repeat; }}
      #key {{ position: absolute; left: 40px; top: 420px; width: 1000px; height: 1000px; z-index: 1; border-radius: 50%;
        background: radial-gradient(circle, rgba(255,255,255,.35) 0%, rgba(255,255,255,0) 65%); }}
      .host-back {{ z-index: 10 !important; position: absolute !important; }}
      #mascot {{ z-index: 40 !important; position: absolute !important; }}
      .host-front {{ z-index: 50 !important; position: absolute !important; }}
      #hud {{ z-index: 60 !important; position: absolute !important; }}
      #captions {{ z-index: 62 !important; position: absolute !important; }}
      #logo {{ position: absolute; left: 68px; top: 96px; width: {LW}px; height: {LH}px; z-index: 70; }}
      #logo img {{ position: absolute; left: 0; top: 0; width: {LW}px; height: {LH}px; }}
      #logo-mask {{ position: absolute; inset: 0; overflow: hidden; -webkit-mask: url(assets/brand/logo_trim.png) 0 0 / {LW}px {LH}px no-repeat; mask: url(assets/brand/logo_trim.png) 0 0 / {LW}px {LH}px no-repeat; }}
      #logo-band {{ position: absolute; left: -180px; top: -20px; width: 140px; height: {LH + 40}px; transform: skewX(-20deg);
        background: linear-gradient(90deg, rgba(150,190,240,0) 0%, rgba(150,190,240,.75) 40%, rgba(255,255,255,.95) 50%, rgba(150,190,240,.75) 60%, rgba(150,190,240,0) 100%); }}
      #logo-glow {{ position: absolute; left: -16px; top: -14px; width: {LW + 32}px; height: {LH + 28}px; opacity: 0; border-radius: 20px;
        background: radial-gradient(ellipse at 50% 50%, rgba(255,255,255,.6), rgba(255,255,255,0) 70%); }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 2048px; z-index: 80; opacity: .35; background: url(assets/brand/grain_256.png); pointer-events: none; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{r3(D)}" data-width="1080" data-height="1920" data-fps="30">
      <div id="bg" data-layout-ignore></div>
      <div id="key" data-layout-ignore></div>
{chr(10).join(back)}
      <!-- the user's rigged 3D mascot (one WebGL canvas), lip sync + acting from the measured VO -->
      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{r3(D)}" data-track-index="3" data-width="1080" data-height="1920"></div>
{chr(10).join(front)}
      <div id="captions" class="clip" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{r3(D)}" data-track-index="7" data-track-kind="captions" data-width="1080" data-height="1920"></div>
      <!-- genuine AIpreneur logo (alpha-trimmed copy, dark glyphs kept), never recoloured: the sheen is a band clipped to the glyphs -->
      <div id="logo" data-layout-ignore><div id="logo-glow"></div><img src="assets/brand/logo_trim.png" alt="AIpreneur" /><div id="logo-mask"><div id="logo-band"></div></div></div>
      <div id="grain" data-layout-ignore></div>
      <!-- the one voice-over: user's ElevenLabs file, untouched. NO background music. -->
      <audio id="vo" class="clip" src="assets/audio/voiceover_final.mp3" data-start="0" data-duration="{r3(wt["audio_duration"])}" data-track-index="8" data-volume="1"></audio>
{chr(10).join(sfx_tags)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {r3(D)}, ease: "steps({int(D * 12)})", immediateRender: false }}, 0);
{chr(10).join(ltl)}
        tl.set({{}}, {{}}, {r3(D - 0.01)});
        window.__timelines["main"] = tl;
      }})();
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(index)

# ------------------------------------------------------------------ captions: navy-gradient Poppins on a soft frosted card,
# key words = white inside the navy-gradient box (brand lock); max 2 lines, words rise in from a mask
NOCAP = set(json.loads((P / "production/nocap.json").read_text())) if (P / "production/nocap.json").exists() else set()
CAPY = json.loads((P / "production/capy.json").read_text()) if (P / "production/capy.json").exists() else {}
groups = wt["caption_groups"]
marks, init, tl = [], [], []
for gi, g in enumerate(groups):
    hl = set(g["highlight"])
    ps = []
    for wi in g["word_idx"]:
        t = html.escape(words[wi]["text"])
        if wi in hl:
            ps.append(f'<span class="m"><span class="w"><span class="kb" id="cw{wi}">{t}</span></span></span>')
        else:
            ps.append(f'<span class="m"><span class="w tx" id="cw{wi}">{t}</span></span>')
    y = CAPY.get(g["id"], 236)
    marks.append(f'    <div class="cg" id="cg{gi}" style="top:{y}px"><div class="cl" id="cgc{gi}">{" ".join(ps)}</div></div>')
    gs, ge = g["start"], min(g["end"], D)
    init.append(f'gsap.set("#cg{gi}", {{ opacity: 0 }});')
    if g["id"] in NOCAP:
        continue
    tl.append(f'tl.set("#cg{gi}", {{ opacity: 1 }}, {r3(max(0.0, gs))});')
    init.append(f'gsap.set("#cgc{gi}", {{ scale: 0.96, opacity: 0 }});')
    tl.append(f'tl.fromTo("#cgc{gi}", {{ scale: 0.96, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.18, ease: "power2.out", immediateRender: false }}, {r3(max(0.0, gs))});')
    for wi in g["word_idx"]:
        ws = max(gs + 0.01, words[wi]["start"] - 0.06)
        init.append(f'gsap.set("#cw{wi}", {{ yPercent: 110, opacity: 0 }});')
        tl.append(f'tl.set("#cw{wi}", {{ opacity: 1 }}, {r3(ws)});')
        tl.append(f'tl.fromTo("#cw{wi}", {{ yPercent: 110 }}, {{ yPercent: 0, duration: 0.3, ease: "power4.out", immediateRender: false }}, {r3(ws)});')
        if wi in hl:
            tl.append(f'tl.fromTo("#cw{wi}", {{ boxShadow: "0 0 0 1px rgba(170,205,255,.16), 0 0 12px rgba(41,75,119,.18)" }}, {{ boxShadow: "0 0 0 1.5px rgba(190,220,255,.55), 0 0 18px rgba(70,120,200,.30)", duration: 0.32, ease: "power3.out", immediateRender: false }}, {r3(words[wi]["start"])});')
            tl.append(f'tl.to("#cw{wi}", {{ boxShadow: "0 0 0 1px rgba(170,205,255,.22), 0 0 12px rgba(41,75,119,.2)", duration: 0.6, ease: "sine.inOut" }}, {r3(words[wi]["start"] + 0.34)});')
    if gi + 1 < len(groups):
        tl.append(f'tl.set("#cg{gi}", {{ opacity: 0 }}, {r3(ge)});')
cap = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    /* editorial headline zone (y 236-400) under the logo row, clear of the 9:16 UI, max 2 lines */
    .cg {{ position: absolute; left: 90px; width: 900px; height: 170px; display: flex; align-items: flex-start; justify-content: center; }}
    .cl {{ max-width: 900px; text-align: center; font: 400 52px/1.28 Poppins, sans-serif; padding: 12px 26px 16px; border-radius: 22px;
      background: rgba(255,255,255,.80); box-shadow: 0 0 0 1px rgba(41,75,119,.10), 0 18px 34px -18px rgba(10,13,44,.35); }}
    .m {{ display: inline-block; overflow: hidden; vertical-align: top; padding: 0.06em 0.06em 0.14em; margin: -0.06em -0.06em -0.14em; }}
    .w {{ display: inline-block; }}
    .tx {{ background: linear-gradient(100deg, #0A0D2C 0%, #294B77 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: #0A0D2C; }}
    .kb {{ display: inline-block; font-weight: 700; color: #fff; background: linear-gradient(135deg, #0A0D2C 0%, #294B77 100%); border-radius: 16px; padding: 0 0.32em 0.04em; box-shadow: 0 0 0 1px rgba(170,205,255,.16), 0 0 12px rgba(41,75,119,.18); }}
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

(P / 'compositions/hud.html').unlink(missing_ok=True)
