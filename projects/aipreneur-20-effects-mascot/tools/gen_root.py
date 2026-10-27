#!/usr/bin/env python3
"""index.html (root) + compositions/captions.html + compositions/hud.html.
Run after tools/make_scenes.py; SFX from production/sfx_plan.json (tools/gen_sfx.py)."""
import html, json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
from xk import r3, CYAN, EFFECTS
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
SHEEN = [1.0, 10.2, 19.6, 29.0, 38.4, 47.6, round(D - 1.15, 2)]
LW, LH = 265, round(265 * 115 / 1195, 2)
ltl = [f'        tl.fromTo("#logo-band", {{ x: 0 }}, {{ x: {LW + 200}, duration: 0.45, ease: "power2.inOut", immediateRender: false }}, {t});' for t in SHEEN]
ltl += [f'        tl.fromTo("#logo-glow", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, ease: "sine.out", immediateRender: false }}, {t});'
        f'\n        tl.fromTo("#logo-glow", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.3, ease: "sine.in", immediateRender: false }}, {r3(t + 0.2)});' for t in SHEEN]

index = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>AIpreneur — 20 Effects (3D mascot remake)</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <link rel="stylesheet" href="vendor/fx.css" />
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #0b1636; }}
      body {{ font-family: "Poppins", sans-serif; font-synthesis: none; color: #fff; -webkit-font-smoothing: antialiased; }}
      #main {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; isolation: isolate; background: #0b1636; }}
      /* supplied navy plate, mirror-extended to 9:16 (tools/prep_brand.py, no stretch) + soft local key light */
      #bg {{ position: absolute; inset: 0; z-index: 0; background: url(assets/brand/bg_navy_1080x1920.png) 0 0 / 1080px 1920px no-repeat; }}
      #key {{ position: absolute; left: 40px; top: 420px; width: 1000px; height: 1000px; z-index: 1; border-radius: 50%;
        background: radial-gradient(circle, rgba(120,170,230,.16) 0%, rgba(120,170,230,0) 65%); }}
      .host-back {{ z-index: 10 !important; position: absolute !important; }}
      #mascot {{ z-index: 40 !important; position: absolute !important; }}
      .host-front {{ z-index: 50 !important; position: absolute !important; }}
      #hud {{ z-index: 60 !important; position: absolute !important; }}
      #captions {{ z-index: 62 !important; position: absolute !important; }}
      #logo {{ position: absolute; left: 64px; top: 72px; width: {LW}px; height: {LH}px; z-index: 70; }}
      #logo img {{ position: absolute; left: 0; top: 0; width: {LW}px; height: {LH}px; }}
      #logo-mask {{ position: absolute; inset: 0; overflow: hidden; -webkit-mask: url(assets/brand/logo_trim.png) 0 0 / {LW}px {LH}px no-repeat; mask: url(assets/brand/logo_trim.png) 0 0 / {LW}px {LH}px no-repeat; }}
      #logo-band {{ position: absolute; left: -180px; top: -20px; width: 140px; height: {LH + 40}px; transform: skewX(-20deg);
        background: linear-gradient(90deg, rgba(0,208,254,0) 0%, rgba(0,208,254,.95) 42%, rgba(220,250,255,1) 50%, rgba(0,208,254,.95) 58%, rgba(0,208,254,0) 100%); }}
      #logo-glow {{ position: absolute; left: -16px; top: -14px; width: {LW + 32}px; height: {LH + 28}px; opacity: 0; border-radius: 20px;
        background: radial-gradient(ellipse at 50% 50%, rgba(0,208,254,.22), rgba(0,208,254,0) 70%); }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 2048px; z-index: 80; opacity: .55; background: url(assets/brand/grain_256.png); pointer-events: none; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{r3(D)}" data-width="1080" data-height="1920" data-fps="30">
      <div id="bg" data-layout-ignore></div>
      <div id="key" data-layout-ignore></div>
{chr(10).join(back)}
      <!-- the user's rigged 3D mascot (one WebGL canvas) = the "footage" every effect transforms -->
      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{r3(D)}" data-track-index="3" data-width="1080" data-height="1920"></div>
{chr(10).join(front)}
      <div id="hud" class="clip" data-composition-id="hud" data-composition-src="compositions/hud.html" data-start="0" data-duration="{r3(D)}" data-track-index="6" data-width="1080" data-height="1920"></div>
      <div id="captions" class="clip" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{r3(D)}" data-track-index="7" data-track-kind="captions" data-width="1080" data-height="1920"></div>
      <!-- genuine AIpreneur logo (alpha-trimmed copy), never recoloured: the sheen is a band clipped to the glyphs -->
      <div id="logo" data-layout-ignore><div id="logo-glow"></div><img src="assets/brand/logo_trim.png" alt="AIpreneur" /><div id="logo-mask"><div id="logo-band"></div></div></div>
      <div id="grain" data-layout-ignore></div>
      <!-- the one voice-over: user's ElevenLabs file, untouched. NO background music. -->
      <audio id="vo" class="clip" src="assets/audio/vo_20effects_elevenlabs_v2.mp3" data-start="0" data-duration="{r3(wt["audio_duration"])}" data-track-index="8" data-volume="1"></audio>
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

# ------------------------------------------------------------------ captions (max 2 lines, rise-in, cyan keywords)
NOCAP = set(json.loads((P / "production/nocap.json").read_text())) if (P / "production/nocap.json").exists() else set()
groups = [g for g in wt["caption_groups"]]
marks, init, tl = [], [], []
for gi, g in enumerate(groups):
    hl = set(g["highlight"])
    ps = []
    for wi in g["word_idx"]:
        t = html.escape(words[wi]["text"])
        ps.append(f'<span class="m"><span class="w{" key" if wi in hl else ""}" id="cw{wi}">{t}</span></span>')
    marks.append(f'    <div class="cg" id="cg{gi}"><div class="cl">{" ".join(ps)}</div></div>')
    gs, ge = g["start"], min(g["end"], D)
    init.append(f'gsap.set("#cg{gi}", {{ opacity: 0 }});')
    if g["id"] in NOCAP:
        continue
    tl.append(f'tl.set("#cg{gi}", {{ opacity: 1 }}, {r3(max(0.0, gs))});')
    for wi in g["word_idx"]:
        ws = max(gs + 0.01, words[wi]["start"] - 0.06)
        init.append(f'gsap.set("#cw{wi}", {{ yPercent: 105, opacity: 0 }});')
        tl.append(f'tl.set("#cw{wi}", {{ opacity: 1 }}, {r3(ws)});')
        tl.append(f'tl.fromTo("#cw{wi}", {{ yPercent: 105 }}, {{ yPercent: 0, duration: 0.3, ease: "power4.out", immediateRender: false }}, {r3(ws)});')
    if gi + 1 < len(groups):
        tl.append(f'tl.set("#cg{gi}", {{ opacity: 0 }}, {r3(ge)});')
cap = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    /* lower third, inside the Reels/TikTok safe zone (clear of the right rail and bottom UI), max 2 lines */
    .cg {{ position: absolute; left: 100px; top: 1404px; width: 800px; height: 136px; display: flex; align-items: flex-start; justify-content: center; }}
    .cl {{ width: 800px; text-align: center; font: 400 46px/1.24 Poppins, sans-serif; color: #fff;
      text-shadow: 0 2px 10px rgba(3,8,28,.85), 0 0 2px rgba(3,8,28,.9); }}
    .m {{ display: inline-block; overflow: hidden; vertical-align: top; padding: 0.04em 0.06em 0.16em; margin: -0.04em -0.06em -0.16em; }}
    .w {{ display: inline-block; }}
    .key {{ color: {CYAN}; font-weight: 700; }}
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

# ------------------------------------------------------------------ HUD: effect badge + label + 20-dot progress
hm, hinit, htl = [], [], []
fxs = [s for s in SC if s["fx"]]
first, last = fxs[0], fxs[-1]
hm.append('    <div id="hud-badge" class="abs smoked" style="left:64px;top:128px;width:76px;height:76px;border-radius:38px;border:2px solid rgba(0,208,254,.9);box-shadow:0 0 18px rgba(0,208,254,.35), inset 0 0 14px rgba(0,208,254,.2)"></div>')
hm.append('    <div id="hud-dots" class="abs" style="left:160px;top:196px;width:500px;height:10px">'
          + "".join(f'<div class="abs" id="hd{k}" style="left:{k * 22}px;top:0;width:10px;height:10px;border-radius:5px;background:rgba(255,255,255,.28)"></div>' for k in range(20)) + '</div>')
hinit.append('gsap.set("#hud-badge", { opacity: 0, scale: 0.6 });')
hinit.append('gsap.set("#hud-dots", { opacity: 0 });')
htl.append(f'tl.fromTo("#hud-badge", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)", immediateRender: false }}, {r3(first["start"])});')
htl.append(f'tl.fromTo("#hud-dots", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3, immediateRender: false }}, {r3(first["start"])});')
htl.append(f'tl.fromTo("#hud-badge", {{ opacity: 1, scale: 1 }}, {{ opacity: 0, scale: 0.6, duration: 0.25, ease: "power2.in", immediateRender: false }}, {r3(last["end"] - 0.25)});')
htl.append(f'tl.fromTo("#hud-dots", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.25, immediateRender: false }}, {r3(last["end"] - 0.25)});')
for s in SC:
    i = s["id"]
    if s["fx"]:
        n = s["fx"]
        hm.append(f'    <div class="abs hmask" style="left:64px;top:128px;width:76px;height:76px;overflow:hidden"><div id="hn-{i}" class="abs" style="left:0;top:0;width:76px;height:76px;'
                  f'font:700 32px/76px Poppins, sans-serif;text-align:center;color:#fff">{n:02d}</div></div>')
        hm.append(f'    <div class="abs hmask" style="left:160px;top:124px;width:860px;height:66px;overflow:hidden"><div id="hl-{i}" class="abs" style="left:0;top:0;width:860px;'
                  f'font:700 46px/66px Poppins, sans-serif;color:#fff;letter-spacing:.01em;white-space:nowrap;text-shadow:0 2px 12px rgba(3,8,28,.85),0 0 3px rgba(3,8,28,.8)">{html.escape(EFFECTS[n - 1].upper())}</div></div>')
        for sel, dly in ((f"#hn-{i}", 0.0), (f"#hl-{i}", 0.04)):
            hinit.append(f'gsap.set("{sel}", {{ yPercent: 110, opacity: 0 }});')
            htl.append(f'tl.set("{sel}", {{ opacity: 1 }}, {r3(s["start"] + dly)});')
            htl.append(f'tl.set("{sel}", {{ opacity: 0 }}, {r3((s["end"] if s is not last else s["end"] - 0.25) + 0.26)});') if s["end"] + 0.26 < D else None
            htl.append(f'tl.fromTo("{sel}", {{ yPercent: 110 }}, {{ yPercent: 0, duration: 0.26, ease: "power3.inOut", immediateRender: false }}, {r3(s["start"] + dly)});')
            if s is not last:
                htl.append(f'tl.fromTo("{sel}", {{ yPercent: 0 }}, {{ yPercent: -110, duration: 0.24, ease: "power3.inOut", immediateRender: false }}, {r3(s["end"])});')
            else:
                htl.append(f'tl.fromTo("{sel}", {{ yPercent: 0 }}, {{ yPercent: -110, duration: 0.22, ease: "power3.in", immediateRender: false }}, {r3(s["end"] - 0.25)});')
        hinit.append(f'gsap.set("#hd{n - 1}", {{ backgroundColor: "rgba(255,255,255,0.28)", scale: 1 }});')
        htl.append(f'tl.fromTo("#hd{n - 1}", {{ backgroundColor: "rgba(255,255,255,0.28)", scale: 1 }}, {{ backgroundColor: "{CYAN}", scale: 1.35, duration: 0.2, ease: "back.out(3)", immediateRender: false }}, {r3(s["start"] + 0.06)});')
        htl.append(f'tl.fromTo("#hd{n - 1}", {{ scale: 1.35 }}, {{ scale: 1, duration: 0.3, ease: "power2.out", immediateRender: false }}, {r3(s["start"] + 0.3)});')
    elif s["id"] not in ("s00",):
        y = 128
        hm.append(f'    <div class="abs hmask" style="left:64px;top:{y}px;width:900px;height:56px;overflow:hidden"><div id="hl-{i}" class="abs" style="left:0;top:0;width:900px;'
                  f'font:700 34px/56px Poppins, sans-serif;color:{CYAN};letter-spacing:.06em;white-space:nowrap;text-shadow:0 2px 12px rgba(3,8,28,.85),0 0 3px rgba(3,8,28,.8)">{html.escape(s["label"])}</div></div>')
        hinit.append(f'gsap.set("#hl-{i}", {{ yPercent: 110, opacity: 0 }});')
        htl.append(f'tl.set("#hl-{i}", {{ opacity: 1 }}, {r3(s["start"] + 0.05)});')
        if s["end"] < D - 0.01:
            htl.append(f'tl.set("#hl-{i}", {{ opacity: 0 }}, {r3(s["end"] + 0.2)});')
        htl.append(f'tl.fromTo("#hl-{i}", {{ yPercent: 110 }}, {{ yPercent: 0, duration: 0.3, ease: "power4.out", immediateRender: false }}, {r3(s["start"] + 0.05)});')
        if s["end"] < D - 0.01:
            htl.append(f'tl.fromTo("#hl-{i}", {{ yPercent: 0 }}, {{ yPercent: -110, duration: 0.24, ease: "power3.inOut", immediateRender: false }}, {r3(s["end"])});')
hud = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
  </style>
  <div id="root" data-composition-id="hud" data-width="1080" data-height="1920">
{chr(10).join(hm)}
  </div>
  <script>
    (function () {{
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {(chr(10) + '      ').join(hinit)}
      {(chr(10) + '      ').join(htl)}
      tl.set({{}}, {{}}, {r3(D - 0.02)});
      window.__timelines["hud"] = tl;
    }})();
  </script>
</template>
"""
(P / "compositions/hud.html").write_text(hud)
print(f"index: {len(SC)} scenes x2 layers, {len(sfx_tags)} sfx; captions {len(groups)} groups; D={D}")
