"""Builds index.html from production/timing.json: the client's light pastel background, word-synced Poppins captions in the
navy text gradient (#0a0d2c -> #294b77), the dark AI PRENEUR logo (top-left, inside the IG safe zone), a persistent
"Berbayar vs Gratis" round header, scene slots, the 3D mascot layer and the VO (starts at vo_offset).
Caption styles: b = Poppins 700, r = Poppins 400, c = Poppins 700 + drawn underline, m = navy gradient pill + white 700.
s01 chunks sit at the top as the hook headline; every other chunk sits in the middle band (above the mascot's head).
Missing scene files are created as empty placeholders.   Run: python3 -I tools/build_index.py ."""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/timing.json").read_text())
total = T["total_sec"]; off = T["vo_offset"]
S = {s["id"]: s for s in T["scenes"]}
W = ",\n          ".join(json.dumps([w["w"], w["s"], w["st"]], ensure_ascii=False) for w in T["words"])
C = ",\n          ".join(json.dumps(c + ["top" if T["words"][c[2]]["scene"] == "s01" else "mid"]) for c in T["caps"])
slots = "".join(f'      <div id="{s["id"]}" class="scene" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" data-start="{s["start"]}" '
                f'data-duration="{s["dur"]}" data-track-index="{2 + k % 3}" data-width="1080" data-height="1920"></div>\n' for k, s in enumerate(T["scenes"]))
# header windows: one per round (paid scene start -> free scene end)
ROUNDS = [("s05", "s06", "ROUND 1 · VIDEO AI"), ("s08", "s09", "ROUND 2 · KLONING SUARA"), ("s11", "s12", "ROUND 3 · GAMBAR AI"), ("s14", "s15", "ROUND 4 · CHATBOT AI")]
HW = [[S[a]["start"], round(S[b]["start"] + S[b]["dur"], 4), lab] for a, b, lab in ROUNDS]
html = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Tools AI berbayar vs versi gratis di GitHub — AI PRENEUR</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <style>
      @font-face {{ font-family: Poppins; src: url(assets/fonts/poppins-latin-400-normal.woff2) format("woff2"); font-weight: 400; }}
      @font-face {{ font-family: Poppins; src: url(assets/fonts/poppins-latin-700-normal.woff2) format("woff2"); font-weight: 700; }}
      :root {{ --ink: #0a0d2c; --ink2: #294b77; --grad: linear-gradient(172deg, #0a0d2c 8%, #294b77 92%); }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #f4f7fd; }}
      #main-root {{ position: relative; width: 100%; height: 100%; overflow: hidden; font-family: Poppins, sans-serif; color: var(--ink); -webkit-font-smoothing: antialiased; }}
      .layer {{ position: absolute; inset: 0; }}
      /* BG: the client's pastel gradient (4:5 original extended to 9:16 with mirrored, blurred bands — never stretched) */
      #bg .plate {{ position: absolute; inset: 0; background: url(assets/brand/bg_1080x1920.png) center / 1080px 1920px no-repeat; }}
      .glow {{ position: absolute; border-radius: 50%; }}
      #glow-a {{ left: -420px; top: -160px; width: 1100px; height: 1100px; background: radial-gradient(circle, rgba(150,186,236,.30), rgba(150,186,236,0) 64%); }}
      #glow-b {{ left: 420px; top: 1100px; width: 1100px; height: 1100px; background: radial-gradient(circle, rgba(141,178,232,.28), rgba(141,178,232,0) 64%); }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 2048px; background: url(assets/brand/grain_256.png); opacity: .045; mix-blend-mode: multiply; }}
      /* captions — navy gradient text */
      .cap {{ opacity: 0; position: absolute; left: 80px; right: 80px; text-align: center; letter-spacing: -0.01em; filter: drop-shadow(0 2px 10px rgba(255,255,255,.85)); }}
      .cap.top {{ top: 318px; font-size: 60px; line-height: 1.16; }}
      .cap.mid {{ top: 968px; font-size: 50px; line-height: 1.22; }}
      .cap .m {{ display: inline-block; overflow: hidden; vertical-align: top; padding: 0.04em 0.1em 0.2em; margin: -0.04em -0.1em -0.2em; }}
      .cap .w {{ display: inline-block; position: relative; background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }}
      .cap .b {{ font-weight: 700; }}
      .cap .r {{ font-weight: 400; }}
      .cap .c {{ font-weight: 700; }}
      .cap .u {{ position: absolute; left: 0.04em; right: 0.04em; bottom: 0.02em; height: 0.12em; border-radius: 0.06em; background: linear-gradient(90deg, rgba(41,75,119,.55), rgba(10,13,44,.35)); transform-origin: 0 50%; }}
      .cap .k {{ font-weight: 700; color: #fff; -webkit-background-clip: border-box; background-clip: border-box; background: var(--grad); padding: 0 0.22em; border-radius: 0.24em; box-shadow: 0 8px 22px rgba(10,13,44,.22); }}
      /* persistent brand mark (client logo, dark) — top-left inside the safe zone */
      #brandlogo {{ opacity: 0; position: absolute; left: 84px; top: 262px; width: 236px; height: auto; }}
      /* round header */
      #hdr {{ position: absolute; left: 0; right: 0; top: 0; height: 0; }}
      .chip {{ opacity: 0; position: absolute; left: 540px; top: 306px; white-space: nowrap; font-weight: 700; font-size: 21px; letter-spacing: .14em; color: #fff;
               background: var(--grad); padding: 7px 18px 6px; border-radius: 30px; box-shadow: 0 8px 20px rgba(10,13,44,.18); }}
      #hdr-title {{ opacity: 0; position: absolute; left: 0; right: 0; top: 350px; text-align: center; font-size: 44px; line-height: 1.1; letter-spacing: -0.015em; white-space: nowrap; }}
      #hdr-title span {{ display: inline-block; background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }}
      #hdr-title .vs {{ font-weight: 400; font-size: 34px; margin: 0 14px; vertical-align: 4px; }}
      #hdr-title .pa {{ font-weight: 700; }}
      #hdr-title .fr {{ font-weight: 700; }}
    </style>
  </head>
  <body>
    <div id="main-root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      <div id="bg" class="clip layer" data-start="0" data-duration="{total}" data-track-index="0">
        <div class="plate"></div><div id="glow-a" class="glow"></div><div id="glow-b" class="glow"></div>
      </div>
{slots}      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{total}" data-track-index="6" data-width="1080" data-height="1920"></div>
      <div id="s01top" data-composition-id="s01top" data-composition-src="compositions/s01top.html" data-start="0" data-duration="1.4" data-track-index="7" data-width="1080" data-height="1920"></div>
      <div id="fx" class="clip layer" data-start="0" data-duration="{total}" data-track-index="8"><div id="grain"></div><img id="brandlogo" src="assets/brand/logo_trim.png" alt="AI PRENEUR">
        <div id="hdr"><div id="hdr-title"><span class="pa">Berbayar</span><span class="vs">vs</span><span class="fr">Gratis</span></div></div></div>
      <div id="caps" class="clip layer" data-start="0" data-duration="{total}" data-track-index="9"></div>
      <audio id="vo" src="assets/audio/vo.mp3" data-start="{off}" data-duration="{T['vo_sec']}" data-track-index="10" data-volume="1"></audio>
    </div>
    <script>
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
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
            tl.set(w, {{ yPercent: 112, opacity: 0 }}, 0);
            tl.set(w, {{ opacity: 1 }}, t);
            tl.fromTo(w, {{ yPercent: 112 }}, {{ yPercent: 0, duration: 0.36, ease: "power4.out", immediateRender: false }}, t);
            if (st === "c") {{
              const u = mk("span", "u", w);
              tl.set(u, {{ scaleX: 0 }}, 0);
              tl.fromTo(u, {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.42, ease: "power3.inOut", immediateRender: false }}, t + 0.14);
            }}
            if (st === "m") tl.fromTo(w, {{ scale: 1 }}, {{ scale: 1.07, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }}, t + 0.3);
          }}
        }});
        // round header (chip text changes per round; hidden during the round-title scenes)
        const HW = {json.dumps(HW, ensure_ascii=False)};
        const hdr = document.getElementById("hdr"), ttl = document.getElementById("hdr-title");
        tl.set(ttl, {{ opacity: 0, y: -18 }}, 0);
        HW.forEach(([a, b, lab], k) => {{
          const chip = mk("div", "chip", hdr, lab);
          gsap.set(chip, {{ xPercent: -50 }}); tl.set(chip, {{ opacity: 0, y: -14, scale: 0.9 }}, 0);
          tl.fromTo(chip, {{ opacity: 0, y: -14, scale: 0.9 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.42, ease: "back.out(2)", immediateRender: false }}, a + 0.04);
          tl.fromTo(chip, {{ opacity: 1, y: 0, scale: 1 }}, {{ opacity: 0, y: -14, scale: 0.9, duration: 0.24, ease: "power2.in", immediateRender: false }}, b - 0.26);
          tl.fromTo(ttl, {{ opacity: 0, y: -18 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "power3.out", immediateRender: false }}, a + 0.1);
          tl.fromTo(ttl, {{ opacity: 1, y: 0 }}, {{ opacity: 0, y: -18, duration: 0.24, ease: "power2.in", immediateRender: false }}, b - 0.26);
        }});
        // ambient (slow, seekable)
        tl.fromTo("#glow-a", {{ x: 0, y: 0 }}, {{ x: 120, y: 90, duration: {total}, ease: "sine.inOut", immediateRender: false }}, 0);
        tl.fromTo("#glow-b", {{ x: 0, y: 0 }}, {{ x: -140, y: -80, duration: {total}, ease: "sine.inOut", immediateRender: false }}, 0);
        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {total}, ease: "steps({int(total * 15)})", immediateRender: false }}, 0);
        // the logo waits for the white world (the opening starts in the sky)
        tl.set("#brandlogo", {{ opacity: 0 }}, 0);
        tl.fromTo("#brandlogo", {{ opacity: 0 }}, {{ opacity: 0.95, duration: 0.5, ease: "power2.out", immediateRender: false }}, 1.25);
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
    if not f.exists(): f.write_text(PLACE.format(id=s["id"], dur=round(s["dur"] - 0.01, 3)))
print("index.html ok:", len(T["scenes"]), "scenes,", len(T["words"]), "words,", len(T["caps"]), "caption chunks, total", total)
