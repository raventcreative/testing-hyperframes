#!/usr/bin/env python3
"""compositions/world.html — the POCKET UNIVERSE layer (global time; mounted 0..D, z between scenes and mascot).
One Three.js render per frame (vendor/world3d_v2.js) feeds three 2D canvases from the SAME pixels and clock:
  #wfull  full frame (S4 aperture -> S5 full screen -> shrinks into the sharp PiP in S6 -> lands in the laptop in S7)
  #wbg    the same frame downsampled + blurred (S6 live background)
The PiP is #wfull itself, clipped to a 16:9 band and scaled into the edge-lit frame (no second copy, no drift).
Only 2D canvases are composited (the WebGL canvas stays hidden): CSS transforms on live WebGL layers stall capture."""
import json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
from xk import r3, WORDS
sc = json.loads((P / "production/scenes.json").read_text())
D = sc["duration"]
S = {s["id"]: s for s in sc["scenes"]}
W = lambda i: WORDS[i]["start"]
WT0 = 12.9                                   # world clock: wt = t - WT0 (unfold on "Dunia", alive on "pelan-pelan jadi hidup")
ON, OFF = 12.5, S["s07"]["start"] + 1.0      # render window
# PiP geometry: 16:9 band of the portrait frame (y 640..1248) -> frame at x 120, y 232, 840 x 472.5
BAND_Y, BAND_H = 640, 608
PX, PY, PW = 120, 232, 840
K = PW / 1080
PH = BAND_H * K
TY = PY - BAND_Y * K
# laptop screen in the room (kit_op.LAP) for the S7 landing
LX, LY, LW = 575, 1012, 360
K2 = LW / 1080
TY2 = LY - BAND_Y * K2
APER = "inset(1150px 340px 470px 340px round 18px)"       # aperture opened inside the Claude Code terminal (S4)
FULL = "inset(0px 0px 0px 0px round 0px)"
BAND = f"inset({BAND_Y}px 0px {1920 - BAND_Y - BAND_H}px 0px round {r3(26 / K)}px)"
s06, s07 = S["s06"]["start"], S["s07"]["start"]
GP = sc.get("gap") or {"cut": s06, "gap": 0}
SHOW0, SHOW1 = r3(GP["cut"] - WT0), r3(s06 - WT0)   # showcase window on the world clock
tl = [
    f'tl.set("#wwrap", {{ visibility: "visible" }}, {ON});',
    f'tl.fromTo("#wwrap", {{ clipPath: "{APER}" }}, {{ clipPath: "{FULL}", duration: 0.62, ease: "power3.inOut", immediateRender: false }}, {ON + 0.05});',
    # S5 -> S6: the full frame shrinks into the sharp PiP while the blurred copy of the same frame fades in behind
    f'tl.fromTo("#wwrap", {{ clipPath: "{FULL}", x: 0, y: 0, scale: 1 }}, {{ clipPath: "{BAND}", x: {PX}, y: {r3(TY)}, scale: {r3(K)}, duration: 0.7, ease: "power3.inOut", immediateRender: false }}, {r3(s06 + 0.02)});',
    f'tl.set("#wbg", {{ visibility: "visible" }}, {r3(s06)});',
    f'tl.fromTo("#wbg", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.6, ease: "power2.out", immediateRender: false }}, {r3(s06 + 0.05)});',
    f'tl.fromTo("#pipf", {{ opacity: 0, scale: 1.04 }}, {{ opacity: 1, scale: 1, duration: 0.35, ease: "power2.out", immediateRender: false }}, {r3(s06 + 0.6)});',
    f'tl.fromTo("#pipl", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power3.out", immediateRender: false }}, {r3(s06 + 0.72)});',
    # S7: the PiP returns into the laptop screen, the room comes back
    f'tl.fromTo("#pipf", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.2, ease: "power1.in", immediateRender: false }}, {r3(s07)});',
    f'tl.fromTo("#pipl", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.2, ease: "power1.in", immediateRender: false }}, {r3(s07)});',
    f'tl.fromTo("#wwrap", {{ x: {PX}, y: {r3(TY)}, scale: {r3(K)} }}, {{ x: {LX}, y: {r3(TY2)}, scale: {r3(K2)}, duration: 0.75, ease: "power3.inOut", immediateRender: false }}, {r3(s07 + 0.05)});',
    f'tl.fromTo("#wbg", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.6, ease: "power2.inOut", immediateRender: false }}, {r3(s07 + 0.05)});',
    f'tl.fromTo("#wwrap", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.18, ease: "none", immediateRender: false }}, {r3(s07 + 0.8)});',
    f'tl.set("#wwrap", {{ visibility: "hidden" }}, {r3(OFF)});',
    f'tl.set("#wbg", {{ visibility: "hidden" }}, {r3(OFF)});',
]
html = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; overflow: hidden; }}
    #wgl {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; visibility: hidden; }}
    #wbg {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; visibility: hidden; }}
    #wwrap {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; transform-origin: 0 0; visibility: hidden; }}
    #wfull {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; }}
    #pipf {{ position: absolute; left: {PX - 6}px; top: {PY - 6}px; width: {PW + 12}px; height: {r3(PH + 12)}px; border-radius: 30px; opacity: 0;
      border: 2px solid rgba(0,201,255,.85); box-shadow: 0 0 0 1px rgba(255,255,255,.25) inset, 0 0 28px rgba(0,201,255,.35), 0 40px 70px -30px rgba(0,0,0,.8); }}
    #pipl {{ position: absolute; left: 0; top: {PY - 66}px; width: 1080px; text-align: center; opacity: 0; }}
    #pipl span {{ display: inline-block; font: 700 34px/1 Poppins, sans-serif; letter-spacing: .14em; color: #fff; padding: 10px 22px; border-radius: 12px;
      background: rgba(6,14,38,.55); border: 1px solid rgba(0,201,255,.45); }}
  </style>
  <div id="root" data-composition-id="world" data-width="1080" data-height="1920">
    <canvas id="wgl" width="1080" height="1920" data-layout-ignore></canvas>
    <canvas id="wbg" width="270" height="480" data-layout-ignore></canvas>
    <div id="wwrap" data-layout-ignore data-layout-allow-occlusion><canvas id="wfull" width="1080" height="1920" data-layout-ignore></canvas></div>
    <div id="pipf" data-layout-ignore></div>
    <div id="pipl" data-layout-ignore><span>CLAUDE OPUS 5.5</span></div>
  </div>
  <script>
    (function () {{
      // generated by tools/gen_world.py — world clock wt = t - {WT0}; render window {ON}..{r3(OFF)} s
      const tl = gsap.timeline({{ paused: true }});
      {(chr(10) + '      ').join(tl)}
      tl.set({{}}, {{}}, {r3(D - 0.02)});
      window.__timelines = window.__timelines || {{}};
      window.__timelines["world"] = tl;
      const gl = document.getElementById("wgl"), full = document.getElementById("wfull").getContext("2d"), bg = document.getElementById("wbg").getContext("2d");
      let world = null;
      function draw(t) {{
        if (t < {ON} || t > {r3(OFF)}) return;
        world.render(Math.max(0, t - {WT0}));
        full.drawImage(gl, 0, 0);
        bg.filter = "blur(3px)"; bg.drawImage(gl, 0, 0, 270, 480); bg.filter = "none";
        bg.fillStyle = "rgba(6,14,38,0.30)"; bg.fillRect(0, 0, 270, 480);
      }}
      window.__hf = window.__hf || {{}}; window.__hf.buildReady = window.__hf.buildReady || {{}};
      const ready = window.World3D.World.create(gl, {{ width: 1080, height: 1920, show: [{SHOW0}, {SHOW1}] }}).then((w) => {{ world = w; }});
      window.__hf.buildReady["world"] = ready;
      window.addEventListener("hf-seek", (e) => {{
        const t = e.detail.time;
        if (world) draw(t); else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => draw(t)));
      }});
    }})();
  </script>
</template>
"""
(P / "compositions/world.html").write_text(html)
print("world.html", "PiP", (PX, PY, PW, round(PH, 1)), "K", round(K, 4))
