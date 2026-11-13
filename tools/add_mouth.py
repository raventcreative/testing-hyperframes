"""Upgrade a reel project to robot v3: front-facing AIpreneur robot with an animated, lip-synced mouth.
- copies brand/robot parts (r3_head.png -> assets/robot/r2_head.png, cleaned body/hands) and brand/robot/robot_rig3.js
  -> vendor/robot_rig2.js (same ROBOT_RIG2 variable, new eye boxes + mouth box)
- injects the mouth (glowing D-shaped smile, drawn as SVG to match the client's robot art) into the head layer and a
  per-frame driver that opens/closes it from the VO loudness envelope (window.VO_ENV, 30 fps) -> talks with the VO.
Run after tools/build.py (idempotent):  python3 -I tools/add_mouth.py projects/<name>"""
import json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = Path(sys.argv[1]).resolve()
B = ROOT / "brand/robot"
shutil.copy(B / "r3_head.png", P / "assets/robot/r2_head.png")
for n in ("r2_body.png", "r2_lhand.png", "r2_rhand.png"):
    shutil.copy(B / n, P / "assets/robot" / n)
shutil.copy(B / "robot_rig3.js", P / "vendor/robot_rig2.js")
rig = json.loads((B / "robot_rig3.js").read_text().split("= ", 1)[1].rstrip(";\n"))
mx, my, mw, mh = rig["mouth"]; hx, hy = rig["head"][0], rig["head"][1]

html = (P / "index.html").read_text()
html = re.sub(r"\n\s*/\* robot-mouth:css \*/.*?/\* /robot-mouth:css \*/", "", html, flags=re.S)
html = re.sub(r"<i class=\"mouth\">.*?</i>", "", html, flags=re.S)
html = re.sub(r"\n\s*/\* robot-mouth:js \*/.*?/\* /robot-mouth:js \*/", "", html, flags=re.S)

css = f"""
      /* robot-mouth:css */
      #robot .mouth {{ position: absolute; left: {mx - hx:.1f}px; top: {my - hy:.1f}px; width: {mw:.1f}px; height: {mh:.1f}px; display: block;
        filter: drop-shadow(0 0 2px rgba(120,190,255,0.95)) drop-shadow(0 0 7px rgba(40,120,255,0.65)); }}
      #robot .mouth svg {{ width: 100%; height: 100%; display: block; overflow: visible; transform-origin: 50% 8%; }}
      /* /robot-mouth:css */"""
html = html.replace("</style>", css + "\n    </style>", 1)

svg = ('<i class="mouth"><svg viewBox="0 0 123 54" preserveAspectRatio="none"><defs>'
       '<linearGradient id="mFill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b2fb8"/><stop offset="1" stop-color="#2b8cff"/></linearGradient>'
       '<pattern id="mDots" width="4" height="4" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="0.9" fill="rgba(160,215,255,0.55)"/></pattern></defs>'
       '<path d="M6,6 H117 C117,33 97,49 61.5,49 C26,49 6,33 6,6 Z" fill="url(#mFill)"/>'
       '<path d="M6,6 H117 C117,33 97,49 61.5,49 C26,49 6,33 6,6 Z" fill="url(#mDots)"/>'
       '<path d="M6,6 H117 C117,33 97,49 61.5,49 C26,49 6,33 6,6 Z" fill="none" stroke="#f3f9ff" stroke-width="2.6" vector-effect="non-scaling-stroke" stroke-linejoin="round"/>'
       '</svg></i>')
anchor = '<i class="lid"></i><i class="lid"></i>'
assert anchor in html, "robot head markup not found"
html = html.replace(anchor, anchor + svg, 1)

js = """
        /* robot-mouth:js */
        { const _m = document.querySelector("#robot .mouth svg"), _env = window.VO_ENV || [], _D = (typeof D !== "undefined") ? D : tl.duration();
          tl.fromTo({ v: 0 }, { v: 0 }, { v: 1, duration: _D, ease: "none", immediateRender: false, onUpdate: () => {
            const f = Math.min(_env.length - 1, Math.max(0, Math.round(tl.time() * 30)));
            const e = _env[f] || 0, ep = _env[Math.max(0, f - 2)] || 0;
            const sy = Math.min(1.05, 0.3 + 0.72 * e + 0.5 * Math.abs(e - ep));
            const sx = 0.9 + 0.13 * e;
            _m.style.transform = "scale(" + sx.toFixed(3) + "," + sy.toFixed(3) + ")"; } }, 0); }
        /* /robot-mouth:js */
"""
tlreg = '        window.__timelines["main"] = tl;'
assert tlreg in html, "timeline registration not found"
html = html.replace(tlreg, js + tlreg, 1)
(P / "index.html").write_text(html)
print("mouth added:", P.name)
