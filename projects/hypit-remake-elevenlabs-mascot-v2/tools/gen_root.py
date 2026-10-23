#!/usr/bin/env python3
"""Generate index.html (root) and compositions/captions.html from
production/word_timing.json (single source of truth for words) and
production/scenes.json (locked scene table). Run: python3 -I tools/gen_root.py <project_dir>
"""
import json, sys, html
from pathlib import Path

P = Path(sys.argv[1]).resolve()
wt = json.loads((P / "production/word_timing.json").read_text())
sc = json.loads((P / "production/scenes.json").read_text())
words = wt["words"]
D = sc["duration"]
FPS = 30


def r3(x):
    return f"{x:.3f}".rstrip("0").rstrip(".")


# ---------------------------------------------------------------- index.html
hosts = []
# Each cut sits 1 ms before its frame time, so exactly one scene owns every rendered frame.
def cut(t):
    return 0.0 if t <= 0 else round(t - 0.001, 4)
for s in sc["scenes"]:
    sid = s["id"]
    s = dict(s, start=cut(s["start"]), end=(cut(s["end"]) if s["end"] < D else D))
    hosts.append(
        f'      <div id="{sid}" class="clip scene-host" data-composition-id="{sid}" '
        f'data-composition-src="compositions/{sid}.html" data-start="{s["start"]}" '
        f'data-duration="{round(s["end"] - s["start"], 4)}" data-track-index="2" data-track-kind="graphics" '
        f'data-width="1080" data-height="1920"></div>'
    )

sfx_tags = []
_sfxp = P / "tools/sfx_plan.json"
SFX = json.loads(_sfxp.read_text()) if _sfxp.exists() else sc.get("sfx", [])
for i, fx in enumerate(SFX):
    sfx_tags.append(
        f'      <audio id="sfx-{i:02d}" class="clip" src="assets/sfx/{fx["file"]}" data-start="{r3(fx["t"])}" '
        f'data-duration="{r3(fx["dur"])}" data-track-index="{4 + (i % 2)}" data-volume="{fx["vol"]}"></audio>'
    )

index = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Hypit — ElevenLabs × Mascot (AI PRENEUR)</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Poppins"; src: url("assets/fonts/poppins-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: block; }}
      @font-face {{ font-family: "Poppins"; src: url("assets/fonts/poppins-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-style: normal; font-display: block; }}
      @font-face {{ font-family: "Poppins"; src: url("assets/fonts/poppins-latin-800-normal.woff2") format("woff2"); font-weight: 800; font-style: normal; font-display: block; }}
      :root {{
        --navy-deep: #121532; --navy-mid: #274976; --white: #ffffff; --ice: #f7faff; --rim: #dce8f6; --graphite: #26354e;
        --hero-grad: linear-gradient(105deg, #121532 0%, #274976 100%);
      }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #f7faff; }}
      body {{ font-family: "Poppins", sans-serif; font-synthesis: none; color: var(--navy-deep); -webkit-font-smoothing: antialiased; }}
      #main {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; isolation: isolate; }}
      /* Supplied 1080x1350 plate, uniform cover to 1080x1920 (scale 1.422, centre crop). Never stretched. */
      #bg-plate {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; object-fit: cover; object-position: 50% 50%; z-index: 0; }}
      #bg-haze {{ position: absolute; inset: 0; z-index: 1; pointer-events: none;
        background: radial-gradient(ellipse 70% 42% at 50% 56%, rgba(255,255,255,.34), rgba(255,255,255,0) 70%); }}
      #bg-grain {{ position: absolute; inset: 0; z-index: 2; opacity: .035; pointer-events: none;
        background-image: repeating-linear-gradient(90deg, rgba(18,21,50,.35) 0 1px, rgba(18,21,50,0) 1px 4px), repeating-linear-gradient(0deg, rgba(18,21,50,.25) 0 1px, rgba(18,21,50,0) 1px 5px); }}
      .scene-host {{ z-index: 10; }}
      #captions {{ z-index: 60; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{r3(D)}" data-width="1080" data-height="1920" data-fps="{FPS}">
      <img id="bg-plate" src="assets/background_asli.png" alt="" data-layout-ignore />
      <div id="bg-haze" data-layout-ignore></div>
      <div id="bg-grain" data-layout-ignore></div>

{chr(10).join(hosts)}

      <div id="captions" class="clip" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{r3(D)}" data-track-index="1" data-track-kind="captions" data-width="1080" data-height="1920"></div>

      <!-- EXACTLY ONE voice-over: Freddie's ElevenLabs file. Normal speed/pitch. -->
      <audio id="vo" class="clip" src="assets/vo_elevenlabs_final.mp3" data-start="0" data-duration="{r3(wt["audio"]["duration"])}" data-track-index="3" data-volume="1"></audio>
{chr(10).join(sfx_tags)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(index)

# ---------------------------------------------------------- captions.html
groups = wt["caption_groups"]
gmark = []
for gi, g in enumerate(groups):
    spans_of = {sp[0]: sp for sp in g.get("highlight_spans", [])}
    parts, wi_list, k = [], g["word_idx"], 0
    while k < len(wi_list):
        wi = wi_list[k]
        if wi in spans_of:
            a_, b_ = spans_of[wi]
            inner = " ".join(f'<span class="hw" id="cap-t{j}">{html.escape(words[j]["text"])}</span>' for j in range(a_, b_ + 1))
            parts.append(f'<span class="cw hl" id="cap-h{a_}"><span class="hl-box" id="cap-b{a_}"></span><span class="hl-tx">{inner}</span></span>')
            k += b_ - a_ + 1
        else:
            parts.append(f'<span class="cw" id="cap-w{wi}">{html.escape(words[wi]["text"])}</span>')
            k += 1
    gmark.append(f'    <div class="cap-g" id="cap-g{gi}" data-layout-allow-overlap><div class="cap-line">{" ".join(parts)}</div></div>')

tl, init = [], []
for gi, g in enumerate(groups):
    gs, ge = g["start"], g["end"]
    hl = set(g.get("highlight", []))
    starts = {sp[0] for sp in g.get("highlight_spans", [])}
    if gs <= 0:
        init.append(f'gsap.set("#cap-g{gi}", {{ opacity: 1, visibility: "visible" }});')
    else:
        init.append(f'gsap.set("#cap-g{gi}", {{ opacity: 0, visibility: "hidden" }});')
        tl.append(f'tl.set("#cap-g{gi}", {{ opacity: 1, visibility: "visible" }}, {r3(gs)});')
    for wi in g["word_idx"]:
        ws = max(gs + 0.01, words[wi]["start"] - 0.03)
        if wi in starts:
            init.append(f'gsap.set("#cap-b{wi}", {{ scaleX: 0.06, opacity: 0 }});')
            tl.append(f'tl.fromTo("#cap-b{wi}", {{ scaleX: 0.06, opacity: 0 }}, {{ scaleX: 1, opacity: 1, duration: 0.16, ease: "expo.out", immediateRender: false }}, {r3(max(gs + 0.005, ws - 0.05))});')
        if wi in hl:
            init.append(f'gsap.set("#cap-t{wi}", {{ opacity: 0, filter: "blur(5px)" }});')
            tl.append(f'tl.fromTo("#cap-t{wi}", {{ opacity: 0, filter: "blur(5px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.13, ease: "power2.out", immediateRender: false }}, {r3(ws + 0.03)});')
        else:
            init.append(f'gsap.set("#cap-w{wi}", {{ opacity: 0, filter: "blur(6px)" }});')
            tl.append(f'tl.fromTo("#cap-w{wi}", {{ opacity: 0, filter: "blur(6px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.13, ease: "power2.out", immediateRender: false }}, {r3(ws)});')
    if gi + 1 < len(groups):
        tl.append(f'tl.fromTo("#cap-g{gi}", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.08, ease: "power2.in", immediateRender: false }}, {r3(ge - 0.08)});')
        tl.append(f'tl.set("#cap-g{gi}", {{ opacity: 0, visibility: "hidden" }}, {r3(ge)});')

cap = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; font-family: "Poppins", sans-serif; }}
    /* Caption band: y 228-384, full-width container, centred text, never translateX(-50%). */
    .cap-g {{ position: absolute; left: 70px; top: 228px; width: 940px; height: 156px; display: flex; align-items: center; justify-content: center; overflow: visible; }}
    .cap-line {{ width: 940px; text-align: center; font-size: 46px; line-height: 1.42; font-weight: 400; letter-spacing: -0.015em; color: #121532; }}
    .cw {{ display: inline-block; white-space: nowrap; }}
    .cw.hl {{ position: relative; font-weight: 700; color: #ffffff; padding: 2px 16px 5px; margin: 0 2px; }}
    .hl-box {{ position: absolute; inset: 0; border-radius: 12px; background: linear-gradient(105deg, #121532 0%, #274976 100%);
      box-shadow: 0 8px 16px rgba(18,21,50,.16), inset 0 1px 0 rgba(255,255,255,.18); transform-origin: 0% 50%; }}
    .hl-tx {{ position: relative; display: inline-block; white-space: nowrap; }}
    .hw {{ display: inline-block; }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
{chr(10).join(gmark)}
  </div>
  <script>
    (function () {{
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {chr(10) + '      '.join([''] + init)}
      {chr(10) + '      '.join([''] + tl)}
      tl.set({{}}, {{}}, {r3(D - 0.02)});
      window.__timelines["captions"] = tl;
    }})();
  </script>
</template>
"""
(P / "compositions/captions.html").write_text(cap)
print("index.html + captions.html written;", len(sc["scenes"]), "scenes,", len(groups), "caption groups, D =", D)
