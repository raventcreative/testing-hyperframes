"""Builds index.html for the R18 reel (Prediksi potensi viral reels sebelum posting; adapted from the R12 builder) from production/timing.json: the client's light
background (white -> soft blue; its baked grid removed and re-created as an ANIMATED CSS grid in the top-right that drifts and
breathes), word-synced Poppins captions in the navy text gradient (#0a0d2c -> #294b77), the dark AI PRENEUR logo (top-left),
scene slots (s01–s09), the robot (co-host) and the mascot (host). Shared visual system: vendor/r18kit.js (window.K).
Caption styles: b = 700, r = 400, c = 700 + drawn underline, m = navy gradient pill + white 700.   Run: python3 -I tools/build_index.py ."""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/timing.json").read_text())
total = T["total_sec"]; off = T["vo_offset"]
S = {s["id"]: s for s in T["scenes"]}
W = ",\n          ".join(json.dumps([w["w"], w["s"], w["st"]], ensure_ascii=False) for w in T["words"])
C = ",\n          ".join(json.dumps(c + ["mid"]) for c in T["caps"])
# world transitions: the scene BEFORE a world (and every world) stays alive OVL s past its cut, so the next world can reveal
# itself over it (later scenes paint on top: DOM order). Slot length = dur + ovl(id).
ovl = lambda sid: 0.0   # no overlapping slots: scenes hand objects over at exactly matching positions
slots = "".join(f'      <div id="{s["id"]}" class="scene" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" data-start="{s["start"]}" '
                f'data-duration="{round(s["dur"] + ovl(s["id"]), 4)}" data-track-index="{2 + k % 3}" data-width="1080" data-height="1920"></div>\n' for k, s in enumerate(T["scenes"]))
html = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Gladi resik reels sebelum posting — AI PRENEUR</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/robot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <script src="vendor/scenes.js"></script>
    <script src="vendor/r18icons.js"></script>
    <script src="vendor/r18kit.js"></script>
        <style>
      @font-face {{ font-family: Poppins; src: url(assets/fonts/poppins-latin-400-normal.woff2) format("woff2"); font-weight: 400; }}
      @font-face {{ font-family: Poppins; src: url(assets/fonts/poppins-latin-700-normal.woff2) format("woff2"); font-weight: 700; }}
      :root {{ --grad: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); --navy: #0a0d2c; --navy2: #294b77; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #f4f8fe; }}
      #main-root {{ position: relative; width: 100%; height: 100%; overflow: hidden; font-family: Poppins, sans-serif; color: #0a0d2c; -webkit-font-smoothing: antialiased; }}
      .layer {{ position: absolute; inset: 0; }}
      /* BG: the client's light gradient (4:5 original de-gridded + extended to 9:16 by mirrored, blurred bands — never stretched) */
      #bg .plate {{ position: absolute; inset: 0; background: url(assets/brand/bg_1080x1920.png) center / 1080px 1920px no-repeat; }}
      /* the client's grid, re-created and ANIMATED: 43 px cells, thin blue-grey lines, top-right, radial fade (drifts + breathes) */
      #gridwrap {{ position: absolute; left: 330px; top: 160px; width: 900px; height: 820px;
                   -webkit-mask-image: radial-gradient(ellipse 430px 360px at 450px 405px, #000 35%, transparent 100%); mask-image: radial-gradient(ellipse 430px 360px at 450px 405px, #000 35%, transparent 100%); }}
      #grid {{ position: absolute; left: -473px; top: -473px; width: 1846px; height: 1766px;
               background-image: linear-gradient(90deg, rgba(104,132,186,.30) 2px, transparent 2px), linear-gradient(0deg, rgba(104,132,186,.30) 2px, transparent 2px);
               background-size: 43px 43px; }}
      #gridhl {{ position: absolute; left: 0; top: 0; width: 520px; height: 520px; margin: -260px 0 0 -260px; border-radius: 50%;
                 background: radial-gradient(circle, rgba(255,255,255,.75), rgba(255,255,255,0) 62%); mix-blend-mode: screen; }}
      #gridtint {{ position: absolute; left: 520px; top: -260px; width: 900px; height: 900px; border-radius: 50%; background: radial-gradient(circle, rgba(126,164,226,.22), rgba(126,164,226,0) 64%); }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 2048px; background: url(assets/brand/grain_256.png); opacity: .035; mix-blend-mode: multiply; }}
      /* captions: navy gradient text with a soft white glow (light background) */
      .cap {{ opacity: 0; position: absolute; left: 70px; right: 70px; text-align: center; font-size: 50px; line-height: 1.22; letter-spacing: -0.01em; filter: drop-shadow(0 2px 10px rgba(255,255,255,.9)); }}
      .cap.mid {{ top: 966px; }}
      .cap .m {{ display: inline-block; overflow: hidden; vertical-align: top; padding: 0.04em 0.1em 0.2em; margin: -0.04em -0.1em -0.2em; }}
      .cap .w {{ display: inline-block; position: relative; background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }}
      .cap .b {{ font-weight: 700; }}
      .cap .r {{ font-weight: 400; }}
      .cap .c {{ font-weight: 700; }}
      .cap .c::after {{ content: ""; position: absolute; left: 0.04em; right: 0.04em; bottom: 0.02em; height: 0.11em; border-radius: 0.06em; background: linear-gradient(90deg, rgba(41,75,119,.5), rgba(10,13,44,.3)); }}
      .cap .k {{ font-weight: 700; color: #fff; -webkit-background-clip: border-box; background-clip: border-box; background: var(--grad); padding: 0 0.22em; border-radius: 0.24em; box-shadow: 0 8px 22px rgba(10,13,44,.22); }}
      /* persistent brand mark (client logo, dark) — top-left inside the safe zone */
      #brandlogo {{ opacity: 0; position: absolute; left: 84px; top: 262px; width: 236px; height: auto; }}
    </style>
  </head>
  <body>
    <div id="main-root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      <div id="bg" class="clip layer" data-start="0" data-duration="{total}" data-track-index="0">
        <div class="plate"></div><div id="gridtint"></div><div id="gridwrap"><div id="grid"></div><div id="gridhl"></div></div>
      </div>
{slots}      <div id="robot" class="clip" data-composition-id="robot" data-composition-src="compositions/robot.html" data-start="0" data-duration="{total}" data-track-index="6" data-width="1080" data-height="1920"></div>
      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{total}" data-track-index="7" data-width="1080" data-height="1920"></div>
      <div id="fx" class="clip layer" data-start="0" data-duration="{total}" data-track-index="8"><div id="grain"></div><img id="brandlogo" src="assets/brand/logo_dark_trim.png" alt="AI PRENEUR"></div>
      <div id="caps" class="clip layer" data-start="0" data-duration="{total}" data-track-index="9"></div>
      <audio id="vo" src="assets/audio/vo.mp3" data-start="{off}" data-duration="{T['vo_sec']}" data-track-index="10" data-volume="1"></audio>
      <audio id="sfx" src="assets/audio/sfx.wav" data-start="0" data-duration="{total}" data-track-index="11" data-volume="0.9"></audio>
    </div>
    <script>
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        // expand the "scale" shorthand (seek-order-safe scaleY in the HF runtime)
        const _sc = (v) => {{ if (!v || typeof v !== "object" || v.scale === undefined) return v; const o = Object.assign({{}}, v); o.scaleX = o.scaleY = o.scale; delete o.scale; return o; }};
        {{ const s0 = tl.set.bind(tl), f0 = tl.fromTo.bind(tl), t0 = tl.to.bind(tl); tl.set = (a, v, p) => s0(a, _sc(v), p); tl.fromTo = (a, x, y, p) => f0(a, _sc(x), _sc(y), p); tl.to = (a, v, p) => t0(a, _sc(v), p); }}
        const mk = (tag, cls, parent, html) => {{ const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; if (parent) parent.appendChild(e); return e; }};
        // VERIFIED word timings (VO offset included): [text, start, style]
        const W = [
          {W}
        ];
        // caption chunks: [start, end, firstWord, lastWord, position]
        const CAPS = [
          {C}
        ];
        const root = document.getElementById("caps");
        CAPS.forEach(([s, e, a, b, pos], ci) => {{
          const c = mk("div", "cap " + pos, root); c.id = "cap" + ci;
          tl.set(c, {{ opacity: 0 }}, 0);
          tl.set(c, {{ opacity: 1 }}, s);
          tl.set(c, {{ opacity: 0 }}, e);
          for (let i = a; i <= b; i++) {{
            const st = W[i][2];
            const m = mk("span", "m", c);
            const w = mk("span", "w " + (st === "m" ? "k" : st), m, W[i][0]);
            if (i < b) c.appendChild(document.createTextNode(" "));
            const t = Math.max(s + 0.02, W[i][1] - 0.08);
            tl.set(w, {{ yPercent: 118, opacity: 0 }}, 0);
            tl.set(w, {{ opacity: 1 }}, t);
            tl.fromTo(w, {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.34, ease: "power4.out", immediateRender: false }}, t);
            if (st === "m") tl.fromTo(w, {{ scale: 1 }}, {{ scale: 1.08, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }}, t + 0.3);
          }}
        }});
        // ambient (slow, seekable): the client's grid drifts diagonally by whole cells, a soft light wanders over it, the tint breathes
        tl.fromTo("#grid", {{ x: 0, y: 0 }}, {{ x: 430, y: 430, duration: {total}, ease: "none", immediateRender: false }}, 0);
        tl.fromTo("#gridhl", {{ x: 600, y: 180 }}, {{ x: 180, y: 640, duration: {total}, ease: "none", immediateRender: false }}, 0);
        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {total}, ease: "steps({int(total * 15)})", immediateRender: false }}, 0);
        tl.set("#brandlogo", {{ opacity: 0.95 }}, 0);   // visible from frame 0
        // the CTA end beat shows its own big logo: the small corner mark steps away
        tl.fromTo("#brandlogo", {{ opacity: 0.95 }}, {{ opacity: 0, duration: 0.35, ease: "power2.out", immediateRender: false }}, {round(S["s09"]["start"] + S["s09"]["dur"] - 1.2, 3)});
        (function (t) {{ const r = t.render; t.render = function (tt, se, f) {{ if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }}; }})(tl);
        window.__timelines = window.__timelines || {{}};
        window.__timelines["main"] = tl;
      }})();
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(html)
PLACE = """<template>
  <style>#root {{ position: absolute; inset: 0; overflow: hidden; }}</style>
  <div id="root" data-composition-id="{id}" data-width="1080" data-height="1920"></div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
      tl.set({{}}, {{}}, {dur});
      window.__timelines = window.__timelines || {{}};
      window.__timelines["{id}"] = tl;
    }})();
  </script>
</template>
"""
for s in T["scenes"]:
    f = P / f"compositions/{s['id']}.html"
    if not f.exists(): f.write_text(PLACE.format(id=s["id"], dur=round(s["dur"] + ovl(s["id"]) - 0.01, 3)))
for cid in ("robot", "mascot"):
    f = P / f"compositions/{cid}.html"
    if not f.exists(): f.write_text(PLACE.format(id=cid, dur=round(total - 0.02, 3)))
print("index.html ok:", len(T["scenes"]), "scenes,", len(T["words"]), "words,", len(T["caps"]), "caption chunks, total", total)
