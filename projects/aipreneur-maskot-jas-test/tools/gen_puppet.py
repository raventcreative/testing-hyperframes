#!/usr/bin/env python3
"""compositions/puppet.html — the new 2D suit mascot as a deterministic GSAP puppet (no 3D model available):
parts from tools/prep_puppet.py (body, armL, armR, head on one 1254 px canvas), pivots at shoulders / neck,
drawn mouth (talk shapes over a skin patch that hides the painted smile) and drawn eyelids (blinks).
Acting keys below are global seconds."""
import json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / "tools"))
from xk import r3, Rng, SCENES
D = SCENES["duration"]
SC = 0.96
TX, TY = 540 - 628 * SC, 790 - 800 * SC          # chest (628,800) of the source -> orbit centre (540,790)
PIV = {"armL": (476, 716), "armR": (778, 716), "head": (628, 652)}
EYES = [(511, 522), (737, 522)]
MOUTH = (628, 584)
SKIN = "#fde8db"

# ---------------------------------------------------------------- acting (global seconds)
ARM_L = [(0, 4), (2.45, 34), (3.1, 22), (3.7, 36), (4.6, 4)]                    # degrees, + = outward
ARM_R = [(0, -4), (0.35, -128), (0.62, -112), (0.86, -134), (1.1, -112), (1.34, -134), (1.58, -114), (1.95, -40),
         (2.5, -34), (3.15, -22), (3.75, -36), (4.6, -4)]
HEAD = [(0, 0, 0), (0.4, 4, -4), (1.3, -3, -2), (2.3, 3, -3), (3.2, -4, -2), (4.2, 2, 0), (5.3, 0, 0)]  # (t, rot deg, y px)
TALK = [(0.45, 1.9), (2.6, 4.1)]                                               # mouth moving
BLINKS = [1.15, 3.35, 5.0]

lines, inits = [], []
def ft(sel, a, b, t, d, ease="sine.inOut"):
    lines.append(f'tl.fromTo("{sel}", {json.dumps(a)}, {json.dumps(dict(b, duration=round(max(0.01, d), 3), ease=ease, immediateRender=False))}, {r3(t)});')
def chain(sel, keys, prop, ease="sine.inOut"):
    inits.append(f'gsap.set("{sel}", {json.dumps({prop: keys[0][1]})});')
    for (t0, v0), (t1, v1) in zip(keys, keys[1:]):
        ft(sel, {prop: v0}, {prop: v1}, t0, t1 - t0, "power2.out" if abs(v1 - v0) > 60 else ease)
chain("#pp-armL", ARM_L, "rotation"); chain("#pp-armR", ARM_R, "rotation")
chain("#pp-head", [(t, r) for t, r, _ in HEAD], "rotation"); chain("#pp-headb", [(t, y) for t, _, y in HEAD], "y")
# breathing (whole figure) + tiny weight shift
inits.append('gsap.set("#pp-rig", { scaleY: 1, x: 0 });')
t = 0.0
while t < D - 0.01:
    d = min(1.6, D - t)
    ft("#pp-rig", {"scaleY": 1}, {"scaleY": 1.008}, t, d / 2); ft("#pp-rig", {"scaleY": 1.008}, {"scaleY": 1}, t + d / 2, d / 2)
    t += d
# mouth: talk shapes every 0.09 s (seeded), smile line hidden while talking
R = Rng(11)
inits.append(f'gsap.set("#pp-mo", {{ svgOrigin: "{MOUTH[0]} {MOUTH[1] - 8}", scaleY: 0.05, opacity: 0 }}); gsap.set("#pp-smile", {{ opacity: 1 }});')
for a, b in TALK:
    lines.append(f'tl.set("#pp-smile", {{ opacity: 0 }}, {r3(a)}); tl.set("#pp-mo", {{ opacity: 1 }}, {r3(a)});')
    prev, t = 0.05, a
    while t < b - 0.01:
        v = 0.15 if R.f() < 0.22 else round(R.u(0.35, 1.0), 2)
        ft("#pp-mo", {"scaleY": prev}, {"scaleY": v}, t, 0.08, "sine.inOut"); prev, t = v, t + 0.09
    ft("#pp-mo", {"scaleY": prev}, {"scaleY": 0.05}, t, 0.08)
    lines.append(f'tl.set("#pp-mo", {{ opacity: 0 }}, {r3(t + 0.09)}); tl.set("#pp-smile", {{ opacity: 1 }}, {r3(t + 0.09)});')
# blinks: lids drop from the top (0.07 s), closed line, open (0.1 s)
inits.append(" ".join(f'gsap.set("#pp-lid{k}", {{ svgOrigin: "{x} {y - 70}", scaleY: 0 }});' for k, (x, y) in enumerate(EYES)) + ' gsap.set(".pp-shut", { opacity: 0 });')
for b in BLINKS:
    ft(".pp-lid", {"scaleY": 0}, {"scaleY": 1}, b, 0.07, "power2.in")
    lines.append(f'tl.set(".pp-shut", {{ opacity: 1 }}, {r3(b + 0.07)}); tl.set(".pp-shut", {{ opacity: 0 }}, {r3(b + 0.13)});')
    ft(".pp-lid", {"scaleY": 1}, {"scaleY": 0}, b + 0.12, 0.1, "power2.out")

part = lambda n, piv: (f'<div class="pp-part" id="pp-{n}" style="transform-origin:{piv[0]}px {piv[1]}px">'
                       f'<img src="assets/puppet/{n}.png" alt="" class="pp-img" /></div>')
eyes = "".join(
    f'<mask id="pp-ec{k}" maskUnits="userSpaceOnUse" x="0" y="0" width="1254" height="1254"><ellipse cx="{x}" cy="{y}" rx="70" ry="64" fill="#fff" filter="url(#pp-lidsoft)"/></mask>'
    for k, (x, y) in enumerate(EYES))
lids = "".join(
    f'<g mask="url(#pp-ec{k})"><g><rect class="pp-lid" x="{x - 76}" y="{y - 70}" width="152" height="140" fill="url(#pp-lidg)" id="pp-lid{k}"/></g></g>'
    f'<path class="pp-shut" d="M{x - 58} {y + 6} Q {x} {y + 34} {x + 58} {y + 6}" fill="none" stroke="#2a1b17" stroke-width="10" stroke-linecap="round"/>'
    f'<path class="pp-shut" d="M{x - 52} {y + 12} l -10 10 M{x + 52} {y + 12} l 10 10" fill="none" stroke="#2a1b17" stroke-width="6" stroke-linecap="round"/>'
    for k, (x, y) in enumerate(EYES))
mx, my = MOUTH
face = (f'<svg class="pp-face" viewBox="0 0 1254 1254" width="1254" height="1254"><defs>{eyes}'
        f'<filter id="pp-lidsoft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>'
        f'<linearGradient id="pp-lidg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff1e9"/><stop offset=".55" stop-color="#fff3ec"/><stop offset="1" stop-color="#fddacc"/></linearGradient>'
        f'<filter id="pp-soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>'
        f'<radialGradient id="pp-sk" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff1e6"/><stop offset="1" stop-color="{SKIN}"/></radialGradient></defs>'
        f'<ellipse cx="{mx}" cy="{my + 2}" rx="50" ry="17" fill="url(#pp-sk)" filter="url(#pp-soft)"/>'
        f'<path id="pp-smile" d="M{mx - 33} {my - 4} Q {mx} {my + 16} {mx + 33} {my - 4}" fill="none" stroke="#e27c6d" stroke-width="5" stroke-linecap="round"/>'
        f'<g id="pp-mo"><path d="M{mx - 24} {my - 8} Q {mx} {my - 12} {mx + 24} {my - 8} Q {mx + 22} {my + 22} {mx} {my + 24} Q {mx - 22} {my + 22} {mx - 24} {my - 8} Z" fill="#7b2f2c"/>'
        f'<ellipse cx="{mx}" cy="{my + 15}" rx="13" ry="7" fill="#e8838a"/></g>{lids}</svg>')
html = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; overflow: hidden; }}
    #pp {{ position: absolute; left: 0; top: 0; width: 1254px; height: 1254px; transform-origin: 0 0;
      transform: translate({r3(TX)}px, {r3(TY)}px) scale({SC}); filter: drop-shadow(0 24px 30px rgba(10,13,44,.22)); }}
    #pp-rig {{ position: absolute; inset: 0; transform-origin: 628px 1222px; }}
    .pp-part, #pp-headb {{ position: absolute; left: 0; top: 0; width: 1254px; height: 1254px; }}
    .pp-img {{ position: absolute; left: 0; top: 0; width: 1254px; height: 1254px; }}
    .pp-face {{ position: absolute; left: 0; top: 0; overflow: visible; }}
  </style>
  <div id="root" data-composition-id="puppet" data-width="1080" data-height="1080">
    <div id="pp" data-layout-ignore data-layout-allow-occlusion><div id="pp-rig">
      {part("body", (628, 1222))}
      {part("armL", PIV["armL"])}
      {part("armR", PIV["armR"])}
      <div id="pp-headb"><div class="pp-part" id="pp-head" style="transform-origin:{PIV['head'][0]}px {PIV['head'][1]}px">
        <img src="assets/puppet/head.png" alt="" class="pp-img" />{face}</div></div>
    </div></div>
  </div>
  <script>
    (function () {{
      // generated by tools/gen_puppet.py
      const tl = gsap.timeline({{ paused: true }});
      {(chr(10) + '      ').join(inits)}
      {(chr(10) + '      ').join(lines)}
      tl.set({{}}, {{}}, {r3(D - 0.01)});
      window.__timelines = window.__timelines || {{}};
      window.__timelines["puppet"] = tl;
    }})();
  </script>
</template>
"""
(P / "compositions/puppet.html").write_text(html)
print("puppet.html", len(lines), "tweens")
