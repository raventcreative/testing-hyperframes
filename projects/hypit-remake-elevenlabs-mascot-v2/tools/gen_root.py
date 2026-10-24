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

CUTS = [  # (time, kind, ox, oy)
    (4.2, "zoom", 540, 470), (9.167, "whipL", 0, 0), (13.8, "zoom", 540, 820), (16.867, "push", 0, 0),
    (20.467, "zoom", 520, 1000), (23.267, "zoom", 520, 1000), (25.133, "whipL", 0, 0), (27.967, "zoom", 420, 720),
    (30.1, "flash", 540, 900), (31.867, "flash", 540, 900), (35.933, "zoom", 540, 760), (40.7, "whipR", 0, 0),
    (42.867, "flash", 420, 1000), (46.867, "zoom", 400, 1050), (49.867, "flash", 540, 950), (51.767, "whipL", 0, 0),
    (56.7, "push", 0, 0), (58.733, "zoom", 380, 1000),
]
# global stage-cam punch at every cut (on top of the per-scene wrapper transitions)
PUNCH = []
for (t, k, ox, oy) in CUTS:
    rot = {"whipL": -1.4, "whipR": 1.4}.get(k, 0)
    ry = {"whipL": 22, "whipR": -22}.get(k, 0)          # 3D swing on whips (reference-style card turn)
    psc = {"zoom": 1.09, "flash": 1.05, "push": 1.04}.get(k, 1.04)
    PUNCH.append(f'        tl.fromTo("#stage-cam", {{ scale: 1, rotation: 0, rotationY: 0, filter: "blur(0px)" }}, {{ scale: {psc}, rotation: {rot}, rotationY: {ry}, filter: "blur(5px)", transformPerspective: 1600, duration: 0.22, ease: "power2.in", immediateRender: false }}, {r3(t - 0.22)});')
    PUNCH.append(f'        tl.fromTo("#stage-cam", {{ scale: {psc}, rotation: {-rot * 0.5}, rotationY: {-ry * 0.6}, filter: "blur(5px)" }}, {{ scale: 1, rotation: 0, rotationY: 0, filter: "blur(0px)", transformPerspective: 1600, duration: 0.5, ease: "expo.out", immediateRender: false }}, {r3(t)});')
ORBIT = []
for k, sc_ in enumerate(sc["scenes"]):
    a_, b_ = sc_["start"], sc_["end"]
    sgn = 1 if k % 2 == 0 else -1
    ORBIT.append(f'        tl.fromTo("#stage-orbit", {{ rotationY: {-3.5 * sgn}, rotationX: 2.5 }}, {{ rotationY: {3.5 * sgn}, rotationX: -1.5, transformPerspective: 1800, duration: {r3(b_ - a_ - 0.002)}, ease: "sine.inOut", immediateRender: false }}, {r3(a_)});')
PUNCH += ORBIT

# presenter windows: (blur-in start, blur full, unblur start, unblur end)
PRESENTER = json.loads((P / "tools/presenter_windows.json").read_text())
st = []
for w in PRESENTER:
    if w.get('noblur'):
        continue
    a, b, c, d = w["in0"], w["in1"], w["out0"], w["out1"]
    if b - a < 0.05:
        st.insert(0, f'        gsap.set("#stage", {{ filter: "blur({w.get("blur", 16)}px) saturate(0.85)", scale: {w.get("scale", 1.06)} }});')
    else: st.append(f'        tl.fromTo("#stage", {{ filter: "blur(0px) saturate(1)", scale: 1 }}, {{ filter: "blur({w.get("blur", 16)}px) saturate(0.85)", scale: {w.get("scale", 1.06)}, duration: {r3(b - a)}, ease: "power2.inOut", immediateRender: false }}, {r3(a)});')
    st.append(f'        tl.fromTo("#stage", {{ filter: "blur({w.get("blur", 16)}px) saturate(0.85)", scale: {w.get("scale", 1.06)} }}, {{ filter: "blur(0px) saturate(1)", scale: 1, duration: {r3(d - c)}, ease: "power2.inOut", immediateRender: false }}, {r3(c)});')
# Smart Motion Director camera moves (snap / digital / dolly zoom) on #world / #stage-dir
_camp = P / "production/director_camera.json"
DIRCAM = [f'        MD.fx.{c["fx"]}({{ tl }}, {json.dumps(c["opts"])});' for c in (json.loads(_camp.read_text()) if _camp.exists() else [])]
STAGE_TWEENS = chr(10).join(st + PUNCH + DIRCAM)
PHOSTS = [f'      <div id="{w["id"].lower()}" class="clip presenter" data-composition-id="{w["id"].lower()}" data-composition-src="compositions/{w["id"].lower()}.html" data-start="{w["host0"]}" data-duration="{r3(w["host1"] - w["host0"])}" data-track-index="8" data-track-kind="graphics" data-width="1080" data-height="1920"></div>' for w in PRESENTER]

sfx_tags = []
_sfxp = P / "tools/sfx_plan.json"
SFX = json.loads(_sfxp.read_text()) if _sfxp.exists() else sc.get("sfx", [])
# drop exact duplicates, then give every cue a lane that is free at its start (no layered cues on one lane)
_seen, _sfx = set(), []
for fx in SFX:
    k = (fx["file"], round(fx["t"], 2))
    if k not in _seen:
        _seen.add(k); _sfx.append(fx)
SFX = _sfx
_lanes = {}
def _lane(t0, t1):
    for ln in [4, 5, 9, 10, 11, 12]:
        if _lanes.get(ln, -1) <= t0:
            _lanes[ln] = t1
            return ln
    return 12
for i, fx in enumerate(SFX):
    fx["lane"] = _lane(fx["t"], fx["t"] + fx["dur"])
    sfx_tags.append(
        f'      <audio id="sfx-{i:02d}" class="clip" src="assets/sfx/{fx["file"]}" data-start="{r3(fx["t"])}" '
        f'data-duration="{r3(min(fx["dur"], D - fx["t"] - 0.005))}" data-track-index="{fx["lane"]}" data-volume="{fx["vol"]}"></audio>'
    )

index = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Hypit — ElevenLabs × Mascot (AI PRENEUR)</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <script src="vendor/timewarp.js"></script>
    <script src="vendor/motion-director.js"></script>
    <style>
      @font-face {{ font-family: "Poppins"; src: url("assets/fonts/poppins-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: block; }}
      @font-face {{ font-family: "Poppins"; src: url("assets/fonts/poppins-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-style: normal; font-display: block; }}
      @font-face {{ font-family: "Poppins"; src: url("assets/fonts/poppins-latin-800-normal.woff2") format("woff2"); font-weight: 800; font-style: normal; font-display: block; }}
      :root {{
        --navy-deep: #0a0d2c; --navy-mid: #294b77; --white: #ffffff; --ice: #f7faff; --rim: #dce8f6; --graphite: #26354e;
        --hero-grad: linear-gradient(105deg, #0a0d2c 0%, #294b77 100%);
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
        background-image: repeating-linear-gradient(90deg, rgba(10,13,44,.35) 0 1px, rgba(10,13,44,0) 1px 4px), repeating-linear-gradient(0deg, rgba(10,13,44,.25) 0 1px, rgba(10,13,44,0) 1px 5px); }}
      #stage {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 10; transform-origin: 540px 1000px; }}
      #stage-cam {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; transform-origin: 540px 960px; }}
      #world {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 10; transform-origin: 540px 900px; }}
      #stage-dir {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; transform-origin: 540px 1000px; }}
      #director {{ z-index: 35 !important; position: absolute !important; }}
      #stage-orbit {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; transform-origin: 540px 1000px; }}
      .scene-host {{ z-index: 10; }}
      .presenter {{ z-index: 30 !important; position: absolute !important; }}
      #mascot {{ z-index: 40; }}
      #fx {{ z-index: 50; }}
      #captions {{ z-index: 60; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{r3(D)}" data-width="1080" data-height="1920" data-fps="{FPS}">
      <img id="bg-plate" src="assets/background_asli.png" alt="" data-layout-ignore />
      <div id="bg-haze" data-layout-ignore></div>
      <div id="bg-grain" data-layout-ignore></div>

      <!-- #world = everything the camera moves (snap / digital zoom); the 3D host, fx and captions stay in front -->
      <div id="world" data-layout-ignore>
      <!-- global stage camera: blur/zoom behind the presenter mascot + cut punches; #stage-dir = director dolly -->
      <div id="stage" data-layout-ignore><div id="stage-cam" data-layout-ignore><div id="stage-dir" data-layout-ignore><div id="stage-orbit" data-layout-ignore>
{chr(10).join(hosts)}
      </div></div></div></div>
      <!-- presenter layers: veil + pop-up elements around the big mascot (tools/gen_presenter.py) -->
{chr(10).join(PHOSTS)}
      <!-- Smart Motion Director overlay effects (tools/motion_director.py -> tools/gen_director.py) -->
      <div id="director" class="clip" data-composition-id="director" data-composition-src="compositions/director.html" data-start="0" data-duration="{r3(D)}" data-track-index="9" data-track-kind="graphics" data-width="1080" data-height="1920"></div>
      </div>

      <!-- 3D rigged mascot overlay (one WebGL canvas, acting driven by global time) -->
      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{r3(D)}" data-track-index="6" data-track-kind="graphics" data-width="1080" data-height="1920"></div>
      <!-- cut transition light/flash overlay -->
      <div id="fx" class="clip" data-composition-id="fx" data-composition-src="compositions/fx.html" data-start="0" data-duration="{r3(D)}" data-track-index="7" data-track-kind="graphics" data-width="1080" data-height="1920"></div>

      <div id="captions" class="clip" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{r3(D)}" data-track-index="1" data-track-kind="captions" data-width="1080" data-height="1920"></div>

      <!-- EXACTLY ONE voice-over: Freddie's ElevenLabs file. Normal speed/pitch. -->
      <audio id="vo" class="clip" src="assets/vo_elevenlabs_final.mp3" data-start="0" data-duration="{r3(wt["audio"]["duration"])}" data-track-index="3" data-volume="1"></audio>
{chr(10).join(sfx_tags)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
{STAGE_TWEENS}
        window.__timelines["main"] = tl;
      }})();
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
            parts.append(f'<span class="cw hl" id="cap-h{a_}"><span class="hl-box" id="cap-b{a_}"><span class="hl-sheen" id="cap-s{a_}"><span class="hl-sheen-i"></span></span></span><span class="hl-tx">{inner}</span></span>')
            k += b_ - a_ + 1
        else:
            parts.append(f'<span class="cw" id="cap-w{wi}"><span class="kp" id="cap-k{wi}"></span><span class="kt">{html.escape(words[wi]["text"])}</span></span>')
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
            tb = max(gs + 0.005, ws - 0.09)
            init.append(f'gsap.set("#cap-b{wi}", {{ scale: 0.35, opacity: 0, rotation: -4, rotationX: -85, transformPerspective: 500 }}); gsap.set("#cap-s{wi}", {{ xPercent: -160 }});')
            tl.append(f'tl.fromTo("#cap-b{wi}", {{ scale: 0.35, opacity: 0, rotation: -4, rotationX: -85, transformPerspective: 500 }}, {{ scale: 1, opacity: 1, rotation: 0, rotationX: 0, transformPerspective: 500, duration: 0.34, ease: "back.out(2.2)", immediateRender: false }}, {r3(tb)});')
            tl.append(f'tl.fromTo("#cap-h{wi}", {{ scale: 1 }}, {{ scale: 1.12, duration: 0.09, ease: "power2.out", immediateRender: false }}, {r3(tb + 0.1)});')
            tl.append(f'tl.fromTo("#cap-h{wi}", {{ scale: 1.12 }}, {{ scale: 1, duration: 0.22, ease: "back.out(2)", immediateRender: false }}, {r3(tb + 0.19)});')
            tl.append(f'tl.fromTo("#cap-s{wi}", {{ xPercent: -160 }}, {{ xPercent: 260, duration: 0.42, ease: "power2.inOut", immediateRender: false }}, {r3(tb + 0.3)});')
        if wi in hl:
            init.append(f'gsap.set("#cap-t{wi}", {{ opacity: 0, scale: 1.75, filter: "blur(10px)" }});')
            tl.append(f'tl.fromTo("#cap-t{wi}", {{ opacity: 0, scale: 1.75, filter: "blur(10px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.24, ease: "expo.out", immediateRender: false }}, {r3(max(gs + 0.02, ws - 0.04))});')
        else:
            init.append(f'gsap.set("#cap-w{wi}", {{ opacity: 0, y: 10, filter: "blur(6px)" }}); gsap.set("#cap-k{wi}", {{ opacity: 0, scaleX: 0.5 }});')
            tl.append(f'tl.fromTo("#cap-w{wi}", {{ opacity: 0, y: 10, filter: "blur(6px)" }}, {{ opacity: 1, y: 0, filter: "blur(0px)", duration: 0.16, ease: "power3.out", immediateRender: false }}, {r3(ws)});')
            we = min(ge - 0.1, words[wi]["end"])
            if we - ws > 0.06:
                tl.append(f'tl.fromTo("#cap-k{wi}", {{ opacity: 0, scaleX: 0.5 }}, {{ opacity: 1, scaleX: 1, duration: 0.1, ease: "power3.out", immediateRender: false }}, {r3(ws)});')
                tl.append(f'tl.fromTo("#cap-k{wi}", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.1, ease: "power2.in", immediateRender: false }}, {r3(max(ws + 0.1, we))});')
    if gi + 1 < len(groups):
        tl.append(f'tl.fromTo("#cap-g{gi}", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.08, ease: "power2.in", immediateRender: false }}, {r3(ge - 0.08)});')
        tl.append(f'tl.set("#cap-g{gi}", {{ opacity: 0, visibility: "hidden" }}, {r3(ge)});')

cap = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; font-family: "Poppins", sans-serif; }}
    /* Caption band: y 228-384, full-width container, centred text, never translateX(-50%). */
    .cap-g {{ position: absolute; left: 70px; top: 228px; width: 940px; height: 156px; display: flex; align-items: center; justify-content: center; overflow: visible; }}
    .cap-line {{ width: 940px; text-align: center; font-size: 46px; line-height: 1.42; font-weight: 400; letter-spacing: -0.015em; color: #0a0d2c; }}
    .cw {{ display: inline-block; white-space: nowrap; position: relative; }}
    .kp {{ position: absolute; left: -9px; right: -9px; top: 3px; bottom: 1px; border-radius: 10px; background: #dce8f6; box-shadow: inset 0 1px 0 rgba(255,255,255,.9), 0 3px 8px rgba(39,73,118,.14); transform-origin: 50% 50%; }}
    .kt {{ position: relative; }}
    .cw.hl {{ position: relative; transform-origin: 50% 60%; font-weight: 700; color: #ffffff; padding: 2px 16px 5px; margin: 0 2px; }}
    .hl-box {{ position: absolute; inset: 0; border-radius: 12px; overflow: hidden; background: linear-gradient(105deg, #0a0d2c 0%, #294b77 100%);
      box-shadow: 0 8px 16px rgba(10,13,44,.16), inset 0 1px 0 rgba(255,255,255,.18); transform-origin: 0% 50%; }}
    .hl-tx {{ position: relative; display: inline-block; white-space: nowrap; }}
    .hl-sheen {{ position: absolute; top: -20%; bottom: -20%; left: 0; width: 38%; }}
    .hl-sheen-i {{ position: absolute; inset: 0; background: linear-gradient(100deg, rgba(255,255,255,0) 0%, rgba(255,255,255,.42) 50%, rgba(255,255,255,0) 100%); transform: skewX(-18deg); }}
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

# ------------------------------------------------------------- fx.html (cut light FX)
fxm, fxi, fxt = [], [], []
for i, (t, k, ox, oy) in enumerate(CUTS):
    if k in ("zoom", "flash"):
        fxm.append(f'    <div class="fx-flash" id="fx-{i}" style="left:{ox - 700}px;top:{oy - 700}px"></div>')
        fxm.append(f'    <div class="fx-ring" id="fx-{i}r" style="left:{ox - 160}px;top:{oy - 160}px"></div>')
        peak = 0.62 if k == "zoom" else 0.38
        fxi.append(f'gsap.set("#fx-{i}", {{ opacity: 0, scale: 0.4 }}); gsap.set("#fx-{i}r", {{ opacity: 0, scale: 0.3 }});')
        fxt.append(f'tl.fromTo("#fx-{i}", {{ opacity: 0, scale: 0.4 }}, {{ opacity: {peak}, scale: 1, duration: 0.12, ease: "power2.in", immediateRender: false }}, {r3(t - 0.12)});')
        fxt.append(f'tl.fromTo("#fx-{i}", {{ opacity: {peak} }}, {{ opacity: 0, scale: 1.4, duration: 0.26, ease: "power2.out", immediateRender: false }}, {r3(t)});')
        fxt.append(f'tl.fromTo("#fx-{i}r", {{ opacity: 0.8, scale: 0.3 }}, {{ opacity: 0, scale: 2.6, duration: 0.42, ease: "power3.out", immediateRender: false }}, {r3(t)});')
    else:
        horiz = k.startswith("whip")
        cls = "fx-streak-h" if horiz else "fx-streak-v"
        fxm.append(f'    <div class="{cls}" id="fx-{i}"></div>')
        if horiz:
            a, b = (1300, -1300) if k == "whipL" else (-1300, 1300)
            fxi.append(f'gsap.set("#fx-{i}", {{ x: {a}, opacity: 0 }});')
            fxt.append(f'tl.fromTo("#fx-{i}", {{ x: {a}, opacity: 0 }}, {{ x: {b}, opacity: 0.9, duration: 0.42, ease: "power2.inOut", immediateRender: false }}, {r3(t - 0.21)});')
            fxt.append(f'tl.set("#fx-{i}", {{ opacity: 0 }}, {r3(t + 0.22)});')
        else:
            fxi.append(f'gsap.set("#fx-{i}", {{ y: 2200, opacity: 0 }});')
            fxt.append(f'tl.fromTo("#fx-{i}", {{ y: 2200, opacity: 0 }}, {{ y: -2200, opacity: 0.85, duration: 0.42, ease: "power2.inOut", immediateRender: false }}, {r3(t - 0.21)});')
            fxt.append(f'tl.set("#fx-{i}", {{ opacity: 0 }}, {r3(t + 0.22)});')
NL = chr(10) + "      "
fx = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; overflow: hidden; }}
    .fx-flash {{ position: absolute; width: 1400px; height: 1400px; border-radius: 50%;
      background: radial-gradient(circle, rgba(255,255,255,.95) 0%, rgba(247,250,255,.7) 22%, rgba(220,232,246,.25) 48%, rgba(220,232,246,0) 70%); }}
    .fx-ring {{ position: absolute; width: 320px; height: 320px; border-radius: 50%; border: 6px solid rgba(255,255,255,.95); box-shadow: 0 0 40px rgba(159,187,224,.8); }}
    .fx-streak-h {{ position: absolute; left: -200px; top: 0; width: 520px; height: 1920px;
      background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,.85) 45%, rgba(220,232,246,.9) 55%, rgba(255,255,255,0)); filter: blur(18px); }}
    .fx-streak-v {{ position: absolute; left: 0; top: -100px; width: 1080px; height: 420px;
      background: linear-gradient(180deg, rgba(255,255,255,0), rgba(255,255,255,.85) 45%, rgba(220,232,246,.9) 55%, rgba(255,255,255,0)); filter: blur(18px); }}
  </style>
  <div id="root" data-composition-id="fx" data-width="1080" data-height="1920">
{chr(10).join(fxm)}
  </div>
  <script>
    (function () {{
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {NL.join(fxi)}
      {NL.join(fxt)}
      tl.set({{}}, {{}}, {r3(D - 0.02)});
      window.__timelines["fx"] = tl;
    }})();
  </script>
</template>
"""
(P / "compositions/fx.html").write_text(fx)
print("fx.html written;", len(CUTS), "cuts")
