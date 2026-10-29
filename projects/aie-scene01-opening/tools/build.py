#!/usr/bin/env python3
"""AI ENGINEER 2026 — SCENE 01 premium cinematic opening (5.5 s, 1080x1920, 30 fps). Built without the 14 s reference.
Shots: 01 cosmic intro (orb, haze, particles, push-in) -> 02 orb morphs into a precision ring that opens on "AI" /
"ENGINEER 2026" -> 03 the camera flies through the counter of the A into the ice-white learning world (4 glass panels in
depth, connection lines) -> 04 the panels fall out of order, one link snaps, "SALAH URUTAN?" -> 05 the existing 3D mascot
rises from behind the panels (rack focus), looks at the broken path, turns, one open-palm gesture, looks to camera,
settles. No VO (no fake lip sync). Deterministic: GSAP paused timeline + seeded particles + seek-driven mascot."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1]
D = 5.5
face = (P / "tools/mascot_face.json").read_text().strip()
decals = (P / "tools/decals.json").read_text().strip()

# seeded particles
s = 7
def rnd():
    global s
    s = (1103515245 * s + 12345) & 0x7FFFFFFF
    return s / 0x7FFFFFFF
parts = []
for i in range(46):
    x, y, r, o = 40 + rnd() * 1000, 200 + rnd() * 1500, 1.5 + rnd() * 3.2, 0.25 + rnd() * 0.55
    parts.append((x, y, r, o))
ph = "".join(f'<div class="pt" style="left:{x:.0f}px;top:{y:.0f}px;width:{2*r:.1f}px;height:{2*r:.1f}px;opacity:{o:.2f}"></div>' for x, y, r, o in parts)

PANELS = [  # id, title, x, y, rotY, z
    ("p1", "PYTHON", 90, 610, 14, 40), ("p2", "API", 590, 800, -14, -40),
    ("p3", "LARGE LANGUAGE<br>MODELS", 90, 1000, 14, 0), ("p4", "AI AGENTS", 590, 1210, -14, -80)]
PW, PH = 400, 160
pan = ""
for k, (pid, t, x, y, ry, z) in enumerate(PANELS):
    pan += (f'<div class="panel" id="{pid}" style="left:{x}px;top:{y}px;width:{PW}px;height:{PH}px">'
            f'<div class="num">{k + 1:02d}</div><div class="ptitle"><span class="tx">{t}</span></div>'
            f'<div class="bar"><i style="width:{60 + 12 * k}%"></i></div><div class="spec"></div></div>')
cen = [(x + PW / 2, y + PH / 2) for _, _, x, y, _, _ in PANELS]
segs = ""
for k in range(3):
    (x0, y0), (x1, y1) = cen[k], cen[k + 1]
    segs += (f'<path id="ln{k}" d="M{x0:.0f} {y0:.0f} C{(x0 + x1) / 2:.0f} {y0:.0f} {(x0 + x1) / 2:.0f} {y1:.0f} {x1:.0f} {y1:.0f}" '
             f'pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>')

html = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=1080, height=1920">
<title>AI Engineer 2026 — Scene 01 Opening</title>
<script src="vendor/gsap/dist/gsap.min.js"></script><script src="vendor/mascot3d.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#0a0d2c}}
body{{font-family:"Poppins",sans-serif;-webkit-font-smoothing:antialiased}}
#main{{position:relative;width:1080px;height:1920px;overflow:hidden;background:#eef4fc}}
.abs{{position:absolute}}
#bg{{position:absolute;inset:0;background:url(assets/brand/bg_1080x1920.png) 0 0/1080px 1920px}}
#world{{position:absolute;inset:0;perspective:1500px;perspective-origin:540px 960px}}
#pgroup{{position:absolute;inset:0;transform-style:preserve-3d}}
.panel{{position:absolute;border-radius:28px;transform-style:preserve-3d;
  background:linear-gradient(150deg,rgba(255,255,255,.78) 0%,rgba(232,240,252,.55) 50%,rgba(205,220,243,.45) 100%);
  border:1.5px solid rgba(255,255,255,.95);border-bottom-color:rgba(41,75,119,.28);border-right-color:rgba(41,75,119,.22);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.95),inset 0 -6px 14px rgba(41,75,119,.10),0 30px 50px -26px rgba(10,13,44,.5);overflow:hidden}}
.num{{position:absolute;left:24px;top:22px;width:58px;height:58px;border-radius:16px;background:linear-gradient(108deg,#0a0d2c,#294b77);
  color:#fff;font:700 26px/58px Poppins;text-align:center}}
.ptitle{{position:absolute;left:100px;top:20px;width:280px;height:72px;display:flex;align-items:center}}
.tx{{font:700 30px/1.08 Poppins;background:linear-gradient(100deg,#0a0d2c 0%,#294b77 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#0a0d2c}}
.bar{{position:absolute;left:24px;right:24px;bottom:28px;height:10px;border-radius:5px;background:rgba(41,75,119,.12)}}
.bar i{{position:absolute;left:0;top:0;bottom:0;border-radius:5px;background:linear-gradient(90deg,#0a0d2c,#294b77)}}
.spec{{position:absolute;left:-40%;top:-20%;width:30%;height:140%;transform:rotate(18deg);background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.7),rgba(255,255,255,0))}}
#lines{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
#lines path{{fill:none;stroke:#294b77;stroke-width:5;stroke-linecap:round;filter:drop-shadow(3px 6px 1px rgba(10,13,44,.15))}}
#spark{{position:absolute;width:90px;height:90px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95) 0%,rgba(160,200,255,.6) 30%,rgba(160,200,255,0) 70%);opacity:0}}
#c{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
#space{{position:absolute;inset:0;overflow:hidden;background:radial-gradient(circle at 50% 44%,#294b77 0%,#0a0d2c 58%,#05071a 100%)}}
#scam{{position:absolute;inset:0;transform-origin:499px 850px}}
.haze{{position:absolute;border-radius:50%;filter:blur(50px);opacity:.55}}
.pt{{position:absolute;border-radius:50%;background:#d8e8ff;box-shadow:0 0 6px rgba(190,215,255,.9)}}
#orb{{position:absolute;left:430px;top:750px;width:220px;height:220px;border-radius:50%;
  background:radial-gradient(circle at 38% 32%,#ffffff 0%,#cfe2ff 22%,#6f98d2 55%,#294b77 85%);
  box-shadow:0 0 40px rgba(170,205,255,.55),0 0 120px rgba(120,165,235,.35)}}
#ring{{position:absolute;left:280px;top:600px;width:520px;height:520px;border-radius:50%;
  background:conic-gradient(from 210deg,#ffffff,#9fc4ff,#294b77,#cfe2ff,#ffffff);
  -webkit-mask:radial-gradient(circle,transparent 0 63%,#000 64% 71%,transparent 72%);mask:radial-gradient(circle,transparent 0 63%,#000 64% 71%,transparent 72%);
  box-shadow:0 0 60px rgba(150,190,250,.35)}}
#ticks{{position:absolute;left:280px;top:600px;width:520px;height:520px;border-radius:50%;
  background:repeating-conic-gradient(rgba(220,235,255,.85) 0 0.6deg,transparent 0.6deg 7.5deg);
  -webkit-mask:radial-gradient(circle,transparent 0 76%,#000 77% 80%,transparent 81%);mask:radial-gradient(circle,transparent 0 76%,#000 77% 80%,transparent 81%)}}
#ai{{position:absolute;left:0;top:700px;width:1080px;text-align:center;white-space:nowrap}}
#ai span{{display:inline-block;font:700 300px/1 Poppins;color:#fff;background:linear-gradient(180deg,#ffffff 0%,#d6e5fb 100%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;text-shadow:none}}
#eng{{position:absolute;left:0;top:1030px;width:1080px;text-align:center;white-space:nowrap}}
#eng span{{display:inline-block;font:700 62px/1 Poppins;color:#fff;letter-spacing:.14em;margin:0 .02em}}
#stampw{{position:absolute;left:0;top:450px;width:1080px;text-align:center}}
#stamp{{display:inline-block;font:700 64px/1.1 Poppins;color:#fff;background:linear-gradient(108deg,#0a0d2c 0%,#294b77 100%);
  border-radius:22px;padding:16px 40px 20px;box-shadow:0 0 0 1.5px rgba(170,205,255,.35),0 0 16px rgba(41,75,119,.3),0 24px 40px -18px rgba(10,13,44,.5)}}
#logo{{position:absolute;left:68px;top:96px;width:204px;height:19.73px;z-index:70}}
#logo img{{position:absolute;left:0;top:0;width:204px;height:19.73px}}
#lmask{{position:absolute;inset:0;overflow:hidden;-webkit-mask:url(assets/brand/logo_trim.png) 0 0/204px 19.73px no-repeat;mask:url(assets/brand/logo_trim.png) 0 0/204px 19.73px no-repeat}}
#lband{{position:absolute;left:-160px;top:-20px;width:120px;height:60px;transform:skewX(-20deg);
  background:linear-gradient(90deg,rgba(150,190,240,0),rgba(150,190,240,.7) 40%,rgba(255,255,255,.95) 50%,rgba(150,190,240,.7) 60%,rgba(150,190,240,0))}}
</style>
</head>
<body>
<div id="main" data-composition-id="main" data-start="0" data-duration="{D}" data-width="1080" data-height="1920" data-fps="30">
  <div id="bg"></div>
  <div id="world"><div id="pgroup">
    <svg id="lines" viewBox="0 0 1080 1920">{segs}</svg>
    {pan}
    <div id="spark" style="left:{(cen[1][0] + cen[2][0]) / 2 - 45:.0f}px;top:{(cen[1][1] + cen[2][1]) / 2 - 45:.0f}px"></div>
  </div></div>
  <canvas id="c" width="1080" height="1920"></canvas>
  <div id="stampw"><span id="stamp">SALAH URUTAN?</span></div>
  <div id="space"><div id="scam">
    <div class="haze" id="hz1" style="left:-120px;top:420px;width:700px;height:520px;background:radial-gradient(circle,#3c6aa8,rgba(60,106,168,0))"></div>
    <div class="haze" id="hz2" style="left:520px;top:1050px;width:680px;height:560px;background:radial-gradient(circle,#2c4f84,rgba(44,79,132,0))"></div>
    <div class="haze" id="hz3" style="left:200px;top:180px;width:760px;height:420px;background:radial-gradient(circle,#1e3a66,rgba(30,58,102,0))"></div>
    <div id="pts">{ph}</div>
    <div id="orb"></div><div id="ring"></div><div id="ticks"></div>
    <div id="ai"><span id="aA">A</span><span id="aI">I</span></div>
    <div id="eng">{"".join(f'<span class="el">{c if c != " " else "&nbsp;"}</span>' for c in "ENGINEER 2026")}</div>
  </div></div>
  <div id="logo"><img src="assets/brand/logo_trim.png" alt="AIpreneur"><div id="lmask"><div id="lband"></div></div></div>
  <audio id="sx0" class="clip" src="assets/sfx/sparkle.wav" data-start="0.15" data-duration="0.9" data-volume="0.10"></audio>
  <audio id="sx1" class="clip" src="assets/sfx/whoosh.wav" data-start="0.72" data-duration="0.6" data-volume="0.10"></audio>
  <audio id="sx2" class="clip" src="assets/sfx/pop.wav" data-start="1.0" data-duration="0.5" data-volume="0.09"></audio>
  <audio id="sx3" class="clip" src="assets/sfx/type.wav" data-start="1.2" data-duration="0.4" data-volume="0.06"></audio>
  <audio id="sx4" class="clip" src="assets/sfx/whoosh.wav" data-start="1.66" data-duration="0.6" data-volume="0.12"></audio>
  <audio id="sx5" class="clip" src="assets/sfx/click.wav" data-start="2.3" data-duration="0.3" data-volume="0.08"></audio>
  <audio id="sx6" class="clip" src="assets/sfx/click.wav" data-start="3.05" data-duration="0.3" data-volume="0.10"></audio>
  <audio id="sx7" class="clip" src="assets/sfx/ping.wav" data-start="3.24" data-duration="0.7" data-volume="0.08"></audio>
  <audio id="sx8" class="clip" src="assets/sfx/whoosh.wav" data-start="4.05" data-duration="0.6" data-volume="0.09"></audio>
  <audio id="sx9" class="clip" src="assets/sfx/pop.wav" data-start="4.48" data-duration="0.5" data-volume="0.05"></audio>
</div>
<script>
(function () {{
  const D = {D};
  const tl = gsap.timeline({{ paused: true }});
  const F = (sel, a, b, at, dur, ease) => tl.fromTo(sel, a, Object.assign({{}}, b, {{ duration: dur, ease: ease || "power2.out", immediateRender: false }}), at);
  // ---------------- initial states
  gsap.set("#orb", {{ opacity: 0, scale: 0.55 }}); gsap.set("#ring", {{ opacity: 0, scale: 0.42, rotation: -40 }}); gsap.set("#ticks", {{ opacity: 0, scale: 0.42 }});
  gsap.set("#aA,#aI", {{ opacity: 0, y: 70 }}); gsap.set(".el", {{ opacity: 0, y: 40 }});
  gsap.set("#pgroup", {{ scale: 1.35, rotationY: 10, filter: "blur(10px)" }});
  gsap.set(".panel", {{ transformPerspective: 1500 }});
  {"".join(f'gsap.set("#{pid}", {{ rotationY: {ry}, z: {z} }}); ' for pid, _, _, _, ry, z in PANELS)}
  gsap.set("#stamp", {{ opacity: 0, scale: 1.25 }});
  gsap.set("#logo", {{ opacity: 0, x: -12, rotation: -2.5, transformOrigin: "0% 50%" }});
  // ---------------- SHOT 01 cosmic intro (0 - 0.8): orb emerges, particles + haze drift, push-in
  F("#scam", {{ scale: 1 }}, {{ scale: 1.1 }}, 0, 1.7, "sine.inOut");
  F("#orb", {{ opacity: 0, scale: 0.55 }}, {{ opacity: 1, scale: 1 }}, 0, 0.7, "power2.out");
  F("#pts", {{ scale: 1, opacity: 0.6 }}, {{ scale: 1.25, opacity: 1 }}, 0, 1.7, "sine.in");
  F("#hz1", {{ x: 0 }}, {{ x: 90 }}, 0, 1.75, "sine.inOut"); F("#hz2", {{ x: 0 }}, {{ x: -80 }}, 0, 1.75, "sine.inOut"); F("#hz3", {{ y: 0 }}, {{ y: 50 }}, 0, 1.75, "sine.inOut");
  // ---------------- SHOT 02 orb -> precision ring -> "AI" / "ENGINEER 2026" (0.8 - 1.7)
  F("#orb", {{ opacity: 1, scale: 1 }}, {{ opacity: 0, scale: 2.2 }}, 0.78, 0.32, "power2.in");
  F("#ring", {{ opacity: 0, scale: 0.42, rotation: -40, filter: "blur(8px)" }}, {{ opacity: 1, scale: 1, rotation: 0, filter: "blur(0px)" }}, 0.8, 0.38, "power3.out");
  F("#ticks", {{ opacity: 0, scale: 0.42, rotation: 30 }}, {{ opacity: 0.9, scale: 1, rotation: 0 }}, 0.84, 0.4, "power3.out");
  F("#ring", {{ scale: 1, rotation: 0, opacity: 1 }}, {{ scale: 1.55, rotation: 25, opacity: 0.35 }}, 1.18, 0.5, "power2.inOut");
  F("#ticks", {{ scale: 1, opacity: 0.9 }}, {{ scale: 1.7, opacity: 0 }}, 1.18, 0.45, "power2.in");
  F("#aA", {{ opacity: 0, y: 70, filter: "blur(10px)" }}, {{ opacity: 1, y: 0, filter: "blur(0px)" }}, 0.98, 0.32, "power3.out");
  F("#aI", {{ opacity: 0, y: 70, filter: "blur(10px)" }}, {{ opacity: 1, y: 0, filter: "blur(0px)" }}, 1.06, 0.32, "power3.out");
  tl.fromTo(".el", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.26, ease: "power3.out", stagger: 0.025, immediateRender: false }}, 1.2);
  // ---------------- SHOT 03 fly through the counter of the A into the ice learning world (1.7 - 3.0)
  F("#scam", {{ scale: 1.1 }}, {{ scale: 24 }}, 1.7, 0.5, "power3.in");
  F("#space", {{ opacity: 1 }}, {{ opacity: 0 }}, 1.98, 0.22, "power1.in");
  tl.set("#space", {{ visibility: "hidden" }}, 2.21);
  F("#pgroup", {{ scale: 1.35, rotationY: 10, filter: "blur(10px)" }}, {{ scale: 1, rotationY: 0, filter: "blur(0px)" }}, 1.92, 0.7, "power3.out");
  F("#pgroup", {{ x: 0, rotationX: 0 }}, {{ x: -18, rotationX: 3 }}, 2.62, 0.4, "sine.inOut");
  {"".join(f'F("#ln{k}", {{ strokeDashoffset: 1 }}, {{ strokeDashoffset: 0 }}, {2.2 + 0.14 * k:.2f}, 0.3, "power2.out"); ' for k in range(3))}
  {"".join(f'F("#{pid} .spec", {{ xPercent: 0 }}, {{ xPercent: 520 }}, {2.15 + 0.08 * k:.2f}, 0.6, "power2.inOut"); ' for k, (pid, *_ ) in enumerate(PANELS))}
  F("#logo", {{ opacity: 0, x: -12, rotation: -2.5 }}, {{ opacity: 1, x: 0, rotation: 0 }}, 2.05, 0.45, "power3.out");
  F("#lband", {{ x: 0 }}, {{ x: 404 }}, 2.45, 0.75, "power2.inOut");
  // ---------------- SHOT 04 wrong order (3.0 - 4.1): one link snaps, panels fall out of sequence
  F("#ln1", {{ strokeDashoffset: 0 }}, {{ strokeDashoffset: 0.5 }}, 3.02, 0.22, "power2.in");
  F("#spark", {{ opacity: 0, scale: 0.3 }}, {{ opacity: 1, scale: 1.2 }}, 3.02, 0.12, "power2.out");
  F("#spark", {{ opacity: 1 }}, {{ opacity: 0 }}, 3.16, 0.3, "power2.in");
  F("#p2", {{ x: 0, y: 0, rotation: 0 }}, {{ x: -500, y: 200, rotation: -6 }}, 3.08, 0.5, "power3.inOut");
  F("#p3", {{ x: 0, y: 0, rotation: 0 }}, {{ x: 500, y: -200, rotation: 5 }}, 3.08, 0.5, "power3.inOut");
  F("#p4", {{ y: 0, rotation: 0 }}, {{ y: 46, rotation: 9 }}, 3.14, 0.45, "back.out(1.4)");
  F("#ln0", {{ opacity: 1 }}, {{ opacity: 0.25 }}, 3.08, 0.3); F("#ln2", {{ opacity: 1 }}, {{ opacity: 0.25 }}, 3.08, 0.3);
  F("#stamp", {{ opacity: 0, scale: 1.25 }}, {{ opacity: 1, scale: 1 }}, 3.22, 0.32, "power3.out");
  F("#stamp", {{ boxShadow: "0 0 0 1.5px rgba(170,205,255,.35),0 0 16px rgba(41,75,119,.3),0 24px 40px -18px rgba(10,13,44,.5)" }},
    {{ boxShadow: "0 0 0 2.5px rgba(205,228,255,.75),0 0 30px rgba(90,145,225,.4),0 24px 40px -18px rgba(10,13,44,.5)" }}, 3.27, 0.3, "power3.out");
  F("#stamp", {{ boxShadow: "0 0 0 2.5px rgba(205,228,255,.75),0 0 30px rgba(90,145,225,.4),0 24px 40px -18px rgba(10,13,44,.5)" }},
    {{ boxShadow: "0 0 0 1.5px rgba(170,205,255,.35),0 0 16px rgba(41,75,119,.3),0 24px 40px -18px rgba(10,13,44,.5)" }}, 3.62, 0.5, "sine.inOut");
  // ---------------- SHOT 05 mascot reveal (4.1 - 5.5): panels part + rack focus, mascot rises from behind
  F("#p1", {{ x: 0, opacity: 1 }}, {{ x: -260, opacity: 0.85 }}, 4.05, 0.6, "power3.inOut");
  F("#p2", {{ x: -500 }}, {{ x: -760 }}, 4.05, 0.6, "power3.inOut");
  F("#p3", {{ x: 500 }}, {{ x: 760 }}, 4.05, 0.6, "power3.inOut");
  F("#p4", {{ x: 0 }}, {{ x: 260 }}, 4.05, 0.6, "power3.inOut");
  F("#pgroup", {{ filter: "blur(0px)" }}, {{ filter: "blur(6px)" }}, 4.15, 0.5, "power2.inOut");
  F("#stamp", {{ opacity: 1, y: 0, scale: 1 }}, {{ opacity: 0, y: -30, scale: 0.92 }}, 4.7, 0.35, "power2.in");
  tl.set({{}}, {{}}, D - 0.02);
  window.__timelines = window.__timelines || {{}};
  window.__timelines["main"] = tl;

  // ---------------- 3D mascot (existing approved GLB + shared runtime), seek-driven, no VO -> mouth stays closed
  const M3 = window.Mascot3D, PO = M3.POSE;
  const tracks = {{
    armR: [[0, PO.rest, 0.3], [4.36, PO.open, 0.45], [4.98, PO.restIn, 0.5]],          // his right arm -> screen-left (the broken path)
    armL: [[0, PO.rest, 0.3], [4.5, PO.restIn, 0.55]],
    head: [[0, [0, 0, 0], 0.3], [4.12, [-0.07, -0.24, -0.04], 0.36], [4.86, [0.0, 0.04, 0.04], 0.42], [5.12, [0.07, 0.03, 0.02], 0.16], [5.28, [0.0, 0.03, 0.02], 0.25]],
    torso: [[0, {{}}, 0.3], [4.24, {{ chest: [0.02, -0.09, -0.015], spine: [0.015, -0.035, 0] }}, 0.45], [4.95, {{ chest: [0.012, 0.015, 0] }}, 0.5]],
    root: [[0, {{ x: 0, y: 0, ry: 0, rz: 0 }}, 0.3], [4.3, {{ ry: -0.05 }}, 0.5], [4.95, {{ ry: 0.0, rz: 0.008 }}, 0.6]],
  }};
  const perf = M3.buildPerformance(tracks, D + 0.05);
  const gk = [[0, 0, 0], [4.02, -1, 0.75], [4.76, 0, 0]];
  const ss = (u) => {{ u = Math.max(0, Math.min(1, u)); return u * u * (3 - 2 * u); }};
  function gaze(t) {{ let i = 0; while (i < gk.length - 1 && gk[i + 1][0] <= t) i++; const a = gk[i], p = gk[i - 1] || a, u = ss((t - a[0]) / 0.14);
    return [0.0036 * (p[1] + (a[1] - p[1]) * u), 0.0026 * (p[2] + (a[2] - p[2]) * u)]; }}
  const V0 = {{ fx: 540, fy: 2700, h: 1500, yaw: 0, pitch: 4 }}, V1 = {{ fx: 540, fy: 2150, h: 1560, yaw: -4, pitch: 4 }}, V2 = {{ fx: 540, fy: 2150, h: 1580, yaw: 0, pitch: 4 }};
  const eo = (u) => 1 - Math.pow(1 - Math.max(0, Math.min(1, u)), 3);
  function view(t) {{
    const u = eo((t - 4.08) / 0.55), w = ss((t - 4.7) / 0.8);
    const o = {{}}; for (const k in V0) o[k] = V0[k] + (V1[k] - V0[k]) * u + (V2[k] - V1[k]) * w; return o;
  }}
  const canvas = document.getElementById("c");
  let mascot = null;
  function apply(t) {{
    canvas.style.visibility = t < 4.0 ? "hidden" : "visible";
    if (t < 4.0) return;
    const Pf = perf(t), mi = M3.micro(t, 5, M3.vnoise);
    for (const k in mi) {{ const a = Pf.bones[k] || [0, 0, 0]; Pf.bones[k] = a.map((v, i) => v + mi[k][i]); }}
    mascot.setView(view(t));
    const bl = M3.blink(t, 0, D + 3, 9, [4.8]);
    mascot.setState({{ root: Object.assign({{ rx: 0 }}, Pf.root), bones: Pf.bones, face: {{ blink: [bl, bl], gaze: gaze(t), mouthMix: 1, mouth: [0.03, 0, 0.007, 0] }} }});
    mascot.render();
  }}
  window.__hf = window.__hf || {{}}; window.__hf.buildReady = window.__hf.buildReady || {{}};
  const ready = M3.Mascot.create(canvas, {{ url: "assets/mascot3d/mascot_jas3_rigged.glb", face: {face}, decals: {decals}, width: 1080, height: 1920, envIntensity: 0.55 }})
    .then((m) => {{ mascot = m; for (const o of m.scene.children) if (o.isDirectionalLight && o.position.z < 0) {{ o.intensity = 1.5; o.color.setRGB(0.86, 0.92, 1.0); o.position.set(1.5, 1.4, -1.5); }} apply(0); }});
  window.__hf.buildReady["main"] = ready;
  window.addEventListener("hf-seek", (e) => {{ const t = e.detail.time; if (mascot) apply(t); else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => apply(t))); }});
}})();
</script>
</body>
</html>
"""
(P / "index.html").write_text(html)
print("index.html", D)
