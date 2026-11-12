"""Builds index.html for the EDIT VIDEO PAKAI CLAUDE reel (R5; adapted from the IGAGENT builder) from production/timing.json: the client's navy
background, word-synced Poppins captions (white + cyan #01CCF7) on navy chips (legible over every world), the white AI PRENEUR logo
(top-left, safe zone), scene slots (s01, st1–st4, s06; each slot lives OVL s past its cut so the next scene can transition over it),
the persistent 4-step rail (y 316–376: Setup · Tools · Gaya · Edit; active pill white, done pills get a cyan check), the robot
(operator) and the mascot (host).
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
LAST = T["scenes"][-1]["id"]
ovl = lambda sid: 0.0 if sid == LAST else 0.4   # each scene stays alive 0.4 s past its cut (its OUT runs while the next scene's IN runs)
def wt(txt, after=0.0):
    for w in T["words"]:
        if w["w"] == txt and w["s"] >= after: return w["s"]
    raise KeyError(txt)
t_step = wt("step")
RAIL = {"labels": ["Setup", "Tools", "Gaya", "Edit"],
        "land": [round(t_step - 0.05 + 0.42 + i * 0.09, 3) for i in range(4)],   # = the s01 chapter markers' arrival times
        "active": [[S[a]["start"], S[b]["start"]] for a, b in (("st1", "st2"), ("st2", "st3"), ("st3", "st4"), ("st4", LAST))],
        "out": round(total - 1.4, 3)}
slots = "".join(f'      <div id="{s["id"]}" class="scene" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" data-start="{s["start"]}" '
                f'data-duration="{round(s["dur"] + ovl(s["id"]), 4)}" data-track-index="{2 + k % 3}" data-width="1080" data-height="1920"></div>\n' for k, s in enumerate(T["scenes"]))
html = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Edit video pakai Claude — AI PRENEUR</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/robot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <script src="vendor/r5_kit.js"></script>
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
      /* the 4-step rail (persistent from "step by step" to the end card) */
      #rail {{ position: absolute; left: 60px; top: 316px; width: 960px; height: 60px; }}
      .rp {{ position: absolute; top: 0; width: 228px; height: 60px; border-radius: 30px; opacity: 0; transform-origin: 50% 50%;
             background: rgba(12,22,64,.82); box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.10), 0 10px 24px -14px rgba(2,6,28,.8); }}
      .rp .on {{ position: absolute; inset: 0; border-radius: 30px; opacity: 0; background: linear-gradient(180deg, #ffffff, #e9f2fd);
                 box-shadow: 0 0 0 2px rgba(1,204,247,.85), 0 0 26px rgba(1,204,247,.45); }}
      .rp .nc {{ position: absolute; left: 10px; top: 10px; width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,.10); }}
      .rp .nc .a {{ position: absolute; inset: 0; border-radius: 50%; opacity: 0; background: #01ccf7; }}
      .rp .n {{ position: absolute; inset: 0; text-align: center; font: 700 22px/40px Poppins, sans-serif; color: #b9c8e6; }}
      .rp .n2 {{ position: absolute; inset: 0; text-align: center; font: 700 22px/40px Poppins, sans-serif; color: #0b1440; opacity: 0; }}
      .rp .ck {{ position: absolute; inset: 0; opacity: 0; color: #0b1440; }}
      .rp .ck svg {{ position: absolute; left: 9px; top: 9px; width: 22px; height: 22px; }}
      .rp .lb, .rp .lb2 {{ position: absolute; left: 62px; top: 0; font: 700 25px/60px Poppins, sans-serif; white-space: nowrap; letter-spacing: -.005em; }}
      .rp .lb {{ color: #8fa3c8; }}
      .rp .lb2 {{ color: #0a0d2c; opacity: 0; }}
      .rp .lb3 {{ position: absolute; left: 62px; top: 0; font: 700 25px/60px Poppins, sans-serif; white-space: nowrap; color: #e3edfa; opacity: 0; }}
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
      <div id="fx" class="clip layer" data-start="0" data-duration="{total}" data-track-index="8"><div id="grain"></div><img id="brandlogo" src="assets/brand/logo_white_trim.png" alt="AI PRENEUR"><div id="rail"></div></div>
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
        // ---- the 4-step rail: pops in pill by pill when the hook's 4 chapter markers land (s01), then tracks the active step
        const RAIL = {json.dumps(RAIL)};
        const ck = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>';
        const rail = document.getElementById("rail");
        RAIL.labels.forEach((lab, i) => {{
          const p = mk("div", "rp", rail); p.id = "rp" + i; p.style.left = (i * 244) + "px";
          p.innerHTML = `<i class="on"></i><b class="nc"><i class="a"></i><span class="n">${{i + 1}}</span><span class="n2">${{i + 1}}</span><span class="ck">${{ck}}</span></b><span class="lb">${{lab}}</span><span class="lb2">${{lab}}</span><span class="lb3">${{lab}}</span>`;
          const q = (c) => p.querySelector(c);
          tl.set(p, {{ opacity: 0, scale: 0.6, y: -14 }}, 0);
          tl.set([q(".on"), q(".a"), q(".n2"), q(".ck"), q(".lb2"), q(".lb3")], {{ opacity: 0 }}, 0);
          tl.set([q(".n"), q(".lb")], {{ opacity: 1 }}, 0);
          const tin = RAIL.land[i];
          tl.fromTo(p, {{ opacity: 0, scale: 0.6, y: -14 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.42, ease: "back.out(2.2)", immediateRender: false }}, tin);
          const [a0, a1] = RAIL.active[i];
          // active: white pill, cyan number disc, navy label (+ a small bump)
          tl.fromTo([q(".on"), q(".a"), q(".n2"), q(".lb2")], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.22, ease: "power2.out", immediateRender: false }}, a0);
          tl.fromTo([q(".n"), q(".lb")], {{ opacity: 1 }}, {{ opacity: 0, duration: 0.22, ease: "power2.out", immediateRender: false }}, a0);
          tl.fromTo(p, {{ scale: 1 }}, {{ scale: 1.08, duration: 0.14, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }}, a0);
          // done: navy pill, cyan disc with a check, cool label
          tl.fromTo([q(".on"), q(".n2"), q(".lb2")], {{ opacity: 1 }}, {{ opacity: 0, duration: 0.22, ease: "power2.out", immediateRender: false }}, a1);
          tl.fromTo([q(".ck"), q(".lb3")], {{ opacity: 0 }}, {{ opacity: 1, duration: 0.22, ease: "power2.out", immediateRender: false }}, a1);
          tl.fromTo(q(".ck"), {{ scale: 0.3, rotation: -30 }}, {{ scale: 1, rotation: 0, duration: 0.36, ease: "back.out(3)", immediateRender: false }}, a1);
          // leaves with the corner logo (the end card shows the logo centred)
          tl.fromTo(p, {{ opacity: 1, y: 0 }}, {{ opacity: 0, y: -10, duration: 0.3, ease: "power2.in", immediateRender: false }}, RAIL.out + i * 0.04);
        }});
        // ambient (slow, seekable)
        tl.fromTo("#glow-a", {{ x: 0, y: 0 }}, {{ x: 90, y: 70, duration: {total}, ease: "sine.inOut", immediateRender: false }}, 0);
        tl.fromTo("#glow-b", {{ x: 0, y: 0 }}, {{ x: -110, y: -60, duration: {total}, ease: "sine.inOut", immediateRender: false }}, 0);
        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {total}, ease: "steps({int(total * 15)})", immediateRender: false }}, 0);
        tl.set("#brandlogo", {{ opacity: 0.95 }}, 0);   // visible from frame 0
        tl.fromTo("#brandlogo", {{ opacity: 0.95 }}, {{ opacity: 0, duration: 0.35, ease: "power2.out", immediateRender: false }}, {RAIL["out"]});
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
