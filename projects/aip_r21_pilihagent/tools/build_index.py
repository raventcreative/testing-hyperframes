"""Builds index.html for the R21 PILIH reel (6 agent AI: cloud vs open source vs orchestrator; adapted from the R19 ASISTEN builder) from production/timing.json: the client's navy background, word-synced Poppins
captions (white + cyan #01CCF7) on navy chips (legible over every world), the white AI PRENEUR logo (top-left, safe zone), scene
slots (s01–s09), the topic header lives inside the scenes (vendor/r21kit.js), the robot (operator) and the mascot (host).
All caption chunks sit mid (y≈968, above the mascot's head).
Missing scene files are created as empty placeholders.   Run: python3 -I tools/build_index.py ."""
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
    <title>6 agent AI, pilih yang mana? — AI PRENEUR</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/robot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <script src="vendor/r21icons.js"></script>
    <script src="vendor/r21kit.js"></script>
        <style>
      @font-face {{ font-family: Poppins; src: url(assets/fonts/poppins-latin-400-normal.woff2) format("woff2"); font-weight: 400; }}
      @font-face {{ font-family: Poppins; src: url(assets/fonts/poppins-latin-700-normal.woff2) format("woff2"); font-weight: 700; }}
      :root {{ --cy: #01ccf7; --cy2: #6adfff; --white: #ffffff; --cool: #e3edfa; --ink: #080b2a; --navy: #0b1440; --chip: rgba(8, 14, 46, 0.78); }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #0a1033; }}
      #main-root {{ position: relative; width: 100%; height: 100%; overflow: hidden; font-family: Poppins, sans-serif; color: #fff; -webkit-font-smoothing: antialiased; }}
      .layer {{ position: absolute; inset: 0; }}
      /* BG: the client's navy gradient (4:5 original extended to 9:16 by mirrored, blurred bands — never stretched) */
      #bg .plate {{ position: absolute; inset: 0; background: url(assets/brand/bg_1080x1920.png) center / 1080px 1920px no-repeat; }}
      .glow {{ position: absolute; border-radius: 50%; mix-blend-mode: screen; }}
      #glow-a {{ left: -380px; top: 120px; width: 1000px; height: 1000px; background: radial-gradient(circle, rgba(48,93,143,.30), rgba(48,93,143,0) 66%); }}
      #glow-b {{ left: 480px; top: 1180px; width: 1000px; height: 1000px; background: radial-gradient(circle, rgba(1,204,247,.12), rgba(1,204,247,0) 66%); }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 2048px; background: url(assets/brand/grain_256.png); opacity: .06; }}
      /* captions: every word sits on its own navy chip, so it reads over every world */
      .cap {{ opacity: 0; position: absolute; left: 70px; right: 70px; text-align: center; font-size: 44px; line-height: 1.5; letter-spacing: -0.005em; }}
      .cap.mid {{ top: 960px; }}
      .cap.low {{ top: 1262px; }}
      .cap .m {{ display: inline-block; overflow: hidden; vertical-align: top; padding: 0.06em 0.06em 0.12em; margin: -0.06em -0.06em -0.12em; }}
      .cap .w {{ display: inline-block; position: relative; padding: 0.02em 0.26em 0.06em; border-radius: 0.22em; background: var(--chip);
                 box-shadow: 0 6px 18px rgba(4,8,30,.35), inset 0 0 0 1.5px rgba(255,255,255,.08); }}
      .cap .b {{ font-weight: 700; color: var(--white); }}
      .cap .r {{ font-weight: 400; color: var(--cool); }}
      .cap .c {{ font-weight: 700; color: var(--cy); }}
      .cap .k {{ font-weight: 700; color: var(--cy); background: #ffffff; box-shadow: 0 8px 22px rgba(1,204,247,.35); }}
      /* persistent brand mark (client logo, white) — top-left inside the safe zone */
      #brandlogo {{ opacity: 0; position: absolute; left: 84px; top: 262px; width: 236px; height: auto; filter: drop-shadow(0 2px 8px rgba(4,8,30,.55)); }}
    </style>
  </head>
  <body>
    <div id="main-root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      <div id="bg" class="clip layer" data-start="0" data-duration="{total}" data-track-index="0">
        <div class="plate"></div><div id="glow-a" class="glow"></div><div id="glow-b" class="glow"></div>
      </div>
{slots}      <div id="robot" class="clip" data-composition-id="robot" data-composition-src="compositions/robot.html" data-start="0" data-duration="{total}" data-track-index="6" data-width="1080" data-height="1920"></div>
      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{total}" data-track-index="7" data-width="1080" data-height="1920"></div>
      <div id="fx" class="clip layer" data-start="0" data-duration="{total}" data-track-index="8"><div id="grain"></div><img id="brandlogo" src="assets/brand/logo_white_trim.png" alt="AI PRENEUR"></div>
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
        const P0 = gsap.timeline(); tl.add(P0, 0);   // initial states: nested timeline, first child at 0
        const pin = (el, v) => {{ gsap.set(el, _sc(v)); P0.set(el, _sc(v), 0); }};
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
          pin(c, {{ opacity: 0 }});
          tl.set(c, {{ opacity: 1 }}, s);
          tl.set(c, {{ opacity: 0 }}, e);
          for (let i = a; i <= b; i++) {{
            const st = W[i][2];
            const m = mk("span", "m", c);
            const w = mk("span", "w " + (st === "m" ? "k" : st), m, W[i][0]);
            if (i < b) c.appendChild(document.createTextNode(" "));
            const t = Math.max(s + 0.02, W[i][1] - 0.08);
            pin(w, {{ yPercent: 118, opacity: 0 }});
            tl.set(w, {{ opacity: 1 }}, t);
            tl.fromTo(w, {{ yPercent: 118 }}, {{ yPercent: 0, duration: 0.34, ease: "power4.out", immediateRender: false }}, t);
            if (st === "m") tl.fromTo(w, {{ scale: 1 }}, {{ scale: 1.08, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }}, t + 0.3);
          }}
        }});
        // ambient (slow, seekable)
        tl.fromTo("#glow-a", {{ x: 0, y: 0 }}, {{ x: 90, y: 70, duration: {total}, ease: "sine.inOut", immediateRender: false }}, 0);
        tl.fromTo("#glow-b", {{ x: 0, y: 0 }}, {{ x: -110, y: -60, duration: {total}, ease: "sine.inOut", immediateRender: false }}, 0);
        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {total}, ease: "steps({int(total * 15)})", immediateRender: false }}, 0);
        pin("#brandlogo", {{ opacity: 0.95 }});   // visible from frame 0
        pin("#glow-a", {{ x: 0, y: 0 }}); pin("#glow-b", {{ x: 0, y: 0 }}); pin("#grain", {{ x: 0, y: 0 }});
        tl.fromTo("#brandlogo", {{ opacity: 0.95 }}, {{ opacity: 0, duration: 0.35, ease: "power2.out", immediateRender: false }}, {round(S["s09"]["start"] + S["s09"]["dur"] - 1.4, 3)});
        (function (t) {{ const r = t.render; t.render = function (tt, se, f) {{ if (tt < this._tTime - 1e-7) r.call(this, 0, true, true); return r.call(this, tt, se, f); }}; }})(tl);
        tl.render(0, true, true);   // apply every pinned initial state now (frame 0 of the real runtime)
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
