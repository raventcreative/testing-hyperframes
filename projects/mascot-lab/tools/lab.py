#!/usr/bin/env python3
"""mascot-lab: writes index.html that renders the 3D mascot from a spec (tools/spec.json):
{ "D": seconds, "views": [[t, {fx,fy,h,yaw,pitch}], ...] (held from t), "tracks": {...buildPerformance tracks...},
  "direct": optional {words:[[text,s,e,key]], intents:[...], seed} -> uses M3.direct, "labels": [[t,"text"]] }"""
import json, sys
from pathlib import Path
P = Path(__file__).resolve().parents[1]
spec = json.loads((P / (sys.argv[1] if len(sys.argv) > 1 else "tools/spec.json")).read_text())
face = (P / "tools/mascot_face.json").read_text().strip()
decals = (P / "tools/decals.json").read_text().strip()
D = spec["D"]
html = f"""<!doctype html>
<html lang="id"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080, height=1920">
<script src="vendor/gsap/dist/gsap.min.js"></script><script src="vendor/mascot3d.js"></script>
<style>*{{margin:0;padding:0}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#eef4fc}}
#main{{position:relative;width:1080px;height:1920px;overflow:hidden;background:url(assets/bg_1080x1920.png) 0 0/1080px 1920px}}
#c{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
#lab{{position:absolute;left:40px;top:40px;font:700 34px/1.2 sans-serif;color:#0A0D2C;background:rgba(255,255,255,.8);padding:8px 16px;border-radius:12px}}</style></head>
<body><div id="main" data-composition-id="main" data-start="0" data-duration="{D}" data-width="1080" data-height="1920" data-fps="30">
<canvas id="c" width="1080" height="1920"></canvas><div id="lab"></div></div>
<script>
(function(){{
const M3 = window.Mascot3D, D = {D};
const SPEC = {json.dumps(spec)};
let perf, gazeAt = () => [0, 0], blinkExtra = [];
if (SPEC.direct) {{ const r = M3.direct(SPEC.direct.words, D, SPEC.direct); perf = M3.buildPerformance(r.tracks, D + 0.05); gazeAt = r.gaze; blinkExtra = r.blinks || []; window.__DIRECT = r; }}
else perf = M3.buildPerformance(SPEC.tracks, D + 0.05);
const views = SPEC.views, labels = SPEC.labels || [];
const sm = (u) => {{ u = Math.max(0, Math.min(1, u)); return u * u * (3 - 2 * u); }};
function viewAt(t) {{
  let i = 0; while (i < views.length - 1 && views[i + 1][0] <= t) i++;
  const v = views[i][1], nx = views[i + 1];
  if (nx && nx[2] && t > nx[0] - nx[2]) {{ const u = sm((t - (nx[0] - nx[2])) / nx[2]); const o = {{}}; for (const k in v) o[k] = v[k] + (nx[1][k] - v[k]) * u; return o; }}
  return v;
}}
let mascot = null;
const lab = document.getElementById('lab');
function apply(t) {{
  const P = perf(t);
  const mi = M3.micro(t, 7, M3.vnoise); for (const k in mi) {{ const a = P.bones[k] || [0,0,0]; P.bones[k] = a.map((v, i) => v + mi[k][i]); }}
  let L = ''; for (const l of labels) if (l[0] <= t) L = l[1]; lab.textContent = L; lab.style.display = L ? 'block' : 'none';
  mascot.setView(viewAt(t));
  const bl = M3.blink(t, 0, D, 3, blinkExtra);
  const g = gazeAt(t);
  mascot.setState({{ root: {{ x: P.root.x, y: P.root.y, ry: P.root.ry, rz: P.root.rz, rx: 0, s: P.root.s }}, bones: P.bones, face: {{ blink: [bl, bl], gaze: g, mouthMix: 1, mouth: [0.03, 0, 0.007, 0] }} }});
  mascot.render();
}}
window.__hf = window.__hf || {{}}; window.__hf.buildReady = window.__hf.buildReady || {{}};
const ready = M3.Mascot.create(document.getElementById('c'), {{ url: 'assets/mascot3d/mascot_jas3_rigged.glb', face: {face}, decals: {decals}, width: 1080, height: 1920, envIntensity: 0.55 }})
  .then((m) => {{ mascot = m; for (const o of m.scene.children) {{ if (o.isDirectionalLight && o.position.z < 0) {{ o.intensity = 1.5; o.color.setRGB(0.86, 0.92, 1.0); o.position.set(1.5, 1.4, -1.5); }} }} apply(0); }});
window.__hf.buildReady['main'] = ready;
window.addEventListener('hf-seek', (e) => {{ const t = e.detail.time; if (mascot) apply(t); else if (e.detail.waitUntil) e.detail.waitUntil(ready.then(() => apply(t))); }});
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused: true }}); tl.set({{}}, {{}}, D - 0.02); window.__timelines['main'] = tl;
}})();
</script></body></html>"""
(P / "index.html").write_text(html)
print("index.html", D, "s")
