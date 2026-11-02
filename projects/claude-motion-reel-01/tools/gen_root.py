#!/usr/bin/env python3
"""index.html (root) + compositions/captions.html for the Claude Code 3D remake.
Layers (back -> front): supplied background plate (never stretched) -> sNN back -> 3D mascot -> sNNf front ->
captions -> AIpreneur logo (upper-left, masked sheen) -> grain.  VO: the user's file once, from 0, untouched."""
import html, json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
from xk import r3
wt = json.loads((P / "production/word_timing.json").read_text())
sc = json.loads((P / "production/scenes.json").read_text())
words, D, SC = wt["words"], sc["duration"], sc["scenes"]
import os
PROOF = float(os.environ.get("PROOF", "0") or 0)      # PROOF=6 -> a 0-6 s proof build (Gate C)
if PROOF:
    D = PROOF
    SC = [dict(x, end=min(x["end"], D)) for x in SC if x["start"] < D]
cut = lambda t: 0.0 if t <= 0 else round(t - 0.001, 4)

hosts = []
for s in SC:
    a, b = cut(s["start"]), (cut(s["end"]) if s["end"] < D else D)
    for suf, z, tr in (("", "back", 2), ("f", "front", 5)):
        hosts.append(f'      <div id="{s["id"]}{suf}" class="clip host-{z}" data-composition-id="{s["id"]}{suf}" data-composition-src="compositions/{s["id"]}{suf}.html" '
                     f'data-start="{r3(a)}" data-duration="{r3(b - a)}" data-track-index="{tr}" data-width="1080" data-height="1920"></div>')
back = [h for h in hosts if "host-back" in h]
front = [h for h in hosts if "host-front" in h]

# SFX (production/sfx_plan.json from tools/gen_sfx.py)
sp = P / "production/sfx_plan.json"
SFX = json.loads(sp.read_text()) if sp.exists() else []
lanes, sfx_tags = {}, []
def lane(t0, t1):
    for ln in range(10, 22):
        if lanes.get(ln, -1) <= t0:
            lanes[ln] = t1
            return ln
    return 21
for i, fx in enumerate(sorted([x for x in SFX if x["t"] < D - 0.1], key=lambda x: x["t"])):
    d = min(fx["dur"], D - fx["t"] - 0.005)
    sfx_tags.append(f'      <audio id="sfx{i:02d}" class="clip" src="assets/sfx/{fx["file"]}" data-start="{r3(fx["t"])}" data-duration="{r3(d)}" '
                    f'data-track-index="{lane(fx["t"], fx["t"] + d)}" data-volume="{fx["vol"]}"></audio>')

# logo: genuine wordmark (logo_trim.png 1199x119) upper-left; deterministic irregular sheen every ~4-7 s (0.5 s pass);
# 3 % pulse only on SATU KALIMAT / 06 / ANIMASI; final sheen then a calm hold
LW = 270; LH = round(LW * 119 / 1199, 2); LX, LY = 60, 112
W = lambda i: words[i]["start"]
gaps = [4.6, 6.3, 5.1, 6.8, 4.2, 5.7, 6.4, 4.9, 5.5, 6.1, 4.4, 6.6, 5.3]
SHEEN, t = [], 1.2
for g in gaps * 2:
    if t > D - 2.4: break
    SHEEN.append(round(t, 2)); t += g
SHEEN.append(round(D - 1.6, 2))
PULSE = [t for t in (W(6), W(55), W(94)) if t < D]

index = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>AIpreneur — Claude Code Motion Reel 01</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script>window.MASCOT_TEX_CLEAN = true;</script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <link rel="stylesheet" href="vendor/fx.css" />
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #0a1430; }}
      body {{ font-family: "Poppins", sans-serif; font-synthesis: none; color: #FFFFFF; -webkit-font-smoothing: antialiased; }}
      #main {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; isolation: isolate; background: #0a1430; }}
      /* user's background_original.png (1080x1350) at native scale + mirrored softened bands (tools: bg extension) */
      #bg {{ position: absolute; inset: 0; z-index: 0; background: url(assets/brand/bg_1080x1920.png) 0 0 / 1080px 1920px no-repeat; }}
      #vig {{ position: absolute; inset: 0; z-index: 1; background: radial-gradient(ellipse 80% 60% at 50% 45%, rgba(0,0,0,0) 55%, rgba(2,4,20,.38) 100%); }}
      .host-back {{ z-index: 10 !important; position: absolute !important; }}
      #mascot {{ z-index: 40 !important; position: absolute !important; }}
      .host-front {{ z-index: 50 !important; position: absolute !important; }}
      #captions {{ z-index: 62 !important; position: absolute !important; }}
      #clogo {{ position: absolute; left: {LX}px; top: {LY}px; width: {LW}px; height: {LH}px; z-index: 70; pointer-events: none; opacity: 0; transform-origin: 0 50%; }}
      #clogo img {{ position: absolute; left: 0; top: 0; width: {LW}px; height: {LH}px; }}
      #clogo .halo {{ position: absolute; left: -30px; top: -26px; width: {LW + 60}px; height: {LH + 52}px; border-radius: 40px;
        background: radial-gradient(ellipse at 50% 50%, rgba(0,208,254,.22) 0%, rgba(0,208,254,0) 70%); opacity: .55; }}
      #clogo .mk {{ position: absolute; inset: 0; overflow: hidden; -webkit-mask: url(assets/brand/logo_trim.png) 0 0/{LW}px {LH}px no-repeat; mask: url(assets/brand/logo_trim.png) 0 0/{LW}px {LH}px no-repeat; }}
      #clband {{ position: absolute; left: -90px; top: -10px; width: 64px; height: {r3(LH + 20)}px; transform: skewX(-20deg);
        background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,.95) 45%, rgba(0,208,254,.9) 60%, rgba(255,255,255,0)); }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 2048px; z-index: 80; opacity: .10; background: url(assets/brand/grain_256.png); pointer-events: none; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{r3(D)}" data-width="1080" data-height="1920" data-fps="30">
      <div id="bg" data-layout-ignore></div>
      <div id="vig" data-layout-ignore></div>
{chr(10).join(back)}
      <!-- the user's rigged 3D mascot (one WebGL canvas), VO lip sync + acting director -->
      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{r3(D)}" data-track-index="3" data-width="1080" data-height="1920"></div>
{chr(10).join(front)}
      <div id="captions" class="clip" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{r3(D)}" data-track-index="7" data-track-kind="captions" data-width="1080" data-height="1920"></div>
      <div id="clogo" data-layout-ignore><div class="halo"></div><img src="assets/brand/logo_trim.png" alt="AIpreneur"><div class="mk"><div id="clband"></div></div></div>
      <div id="grain" data-layout-ignore></div>
      <!-- the one voice-over: user's ElevenLabs file, from 0, untouched. NO music. -->
      <audio id="vo" class="clip" src="assets/audio/voiceover_final.mp3" data-start="0" data-duration="{r3(min(wt["audio_duration"], D))}" data-track-index="8" data-volume="1"></audio>
{chr(10).join(sfx_tags)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {r3(D)}, ease: "steps({int(D * 12)})", immediateRender: false }}, 0);
        tl.fromTo("#clogo", {{ opacity: 0, y: 6, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.42, ease: "power3.out", immediateRender: false }}, 0.1);
        {(chr(10) + '        ').join(f'tl.fromTo("#clband", {{ x: 0 }}, {{ x: {LW + 180}, duration: 0.5, ease: "power2.inOut", immediateRender: false }}, {t});' for t in SHEEN)}
        {(chr(10) + '        ').join(f'tl.fromTo("#clogo", {{ scale: 1 }}, {{ scale: 1.03, duration: 0.14, ease: "power2.out", immediateRender: false }}, {r3(t)}); tl.fromTo("#clogo", {{ scale: 1.03 }}, {{ scale: 1, duration: 0.2, ease: "power2.inOut", immediateRender: false }}, {r3(t + 0.14)});' for t in PULSE)}
        tl.set({{}}, {{}}, {r3(D - 0.01)});
        window.__timelines["main"] = tl;
      }})();
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(index)

# ------------------------------------------------------------------ captions: white Poppins on a navy plate, keywords cyan
NOCAP = json.loads((P / "production/nocap.json").read_text()) if (P / "production/nocap.json").exists() else []
groups = [g for g in wt["caption_groups"] if g["start"] < D and not any(a <= words[g["word_idx"][0]]["start"] < b for a, b in NOCAP)]
marks, init, tl = [], [], []
for gi, g in enumerate(groups):
    hl = set(g["highlight"])
    ps = []
    for wi in g["word_idx"]:
        t = html.escape(words[wi]["text"])
        cls = "w kw" if wi in hl else "w"
        ps.append(f'<span class="m"><span class="{cls}" id="cw{wi}">{t}</span></span>')
    marks.append(f'    <div class="cg" id="cg{gi}"><div class="cl" id="cgc{gi}">{" ".join(ps)}</div></div>')
    gs, ge = g["start"], min(g["end"], D)
    init.append(f'gsap.set("#cg{gi}", {{ opacity: 0 }});')
    gs = max(gs, words[g["word_idx"][0]]["start"] - 0.08)
    tl.append(f'tl.set("#cg{gi}", {{ opacity: 1 }}, {r3(max(0.0, gs))});')
    init.append(f'gsap.set("#cgc{gi}", {{ scale: 0.96, opacity: 0 }});')
    tl.append(f'tl.fromTo("#cgc{gi}", {{ scale: 0.96, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.18, ease: "power2.out", immediateRender: false }}, {r3(max(0.0, gs))});')
    for wi in g["word_idx"]:
        ws = max(gs + 0.01, words[wi]["start"] - 0.06)
        init.append(f'gsap.set("#cw{wi}", {{ yPercent: 110, opacity: 0 }});')
        tl.append(f'tl.set("#cw{wi}", {{ opacity: 1 }}, {r3(ws)});')
        tl.append(f'tl.fromTo("#cw{wi}", {{ yPercent: 110 }}, {{ yPercent: 0, duration: 0.3, ease: "power4.out", immediateRender: false }}, {r3(ws)});')
    if gi + 1 < len(groups) or any(a <= ge < b for a, b in NOCAP):
        tl.append(f'tl.set("#cg{gi}", {{ opacity: 0 }}, {r3(min(ge, words[g["word_idx"][-1]]["end"] + 0.35))});')
cap = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    /* caption band y 236-370 (below the logo): short, word-synced, never over the hero */
    .cg {{ position: absolute; left: 90px; top: 236px; width: 900px; height: 140px; display: flex; align-items: flex-start; justify-content: center; }}
    .cl {{ max-width: 900px; text-align: center; font: 400 40px/1.28 Poppins, sans-serif; padding: 12px 26px 16px; border-radius: 22px;
      background: linear-gradient(135deg, rgba(10,13,44,.95), rgba(41,75,119,.92)); border: 1.5px solid rgba(0,208,254,.40);
      box-shadow: inset 1.5px 1.5px 0 rgba(255,255,255,.16), 0 24px 40px -22px rgba(2,4,20,.75); }}
    .m {{ display: inline-block; overflow: hidden; vertical-align: top; padding: 0.06em 0.06em 0.14em; margin: -0.06em -0.06em -0.14em; }}
    .w {{ display: inline-block; color: #FFFFFF; }}
    .kw {{ font-weight: 700; color: #00D0FE; }}
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
print("index.html + captions.html", len(groups), "caption groups,", len(SHEEN), "logo sheens")
