"""Builds index.html (host: user's navy background, word-synced Poppins captions, VO, scene slots, mascot layer)
from production/timing.json. Missing scene files are created as empty placeholders.
Caption styles per word: b = Poppins 700 white, r = Poppins 400 cool white #E3EDFA, c = Poppins 700 cyan #01CCF7,
m = apex marker: crisp white rectangle with cyan Poppins 700 inside.   Run: python3 -I tools/build_index.py ."""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
T = json.loads((P / "production/timing.json").read_text())
total = T["total_sec"]
W = ",\n          ".join(json.dumps([w["w"], w["s"], w["st"]], ensure_ascii=False) for w in T["words"])
C = ",\n          ".join(json.dumps(c) for c in T["caps"])
slots = "".join(f'      <div id="{s["id"]}" class="safe-scene" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html" data-start="{s["start"]}" '
                f'data-duration="{s["dur"]}" data-track-index="{2 + k % 3}" data-width="1080" data-height="1920"></div>\n' for k, s in enumerate(T["scenes"]))
html = f"""<!doctype html>
<html lang="id" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Cloudflare Security Audit Skill — AI PRENEUR</title>
    <script src="vendor/gsap/dist/gsap.min.js"></script>
    <script src="vendor/mascot3d.js"></script>
    <script src="vendor/vo_words.js"></script>
    <style>
      @font-face {{ font-family: Poppins; src: url(assets/fonts/poppins-latin-400-normal.woff2) format("woff2"); font-weight: 400; }}
      @font-face {{ font-family: Poppins; src: url(assets/fonts/poppins-latin-700-normal.woff2) format("woff2"); font-weight: 700; }}
      :root {{ --cy: #01ccf7; --cy2: #6adfff; --white: #ffffff; --cool: #e3edfa; --ink: #080b2a; --navy: #182c53; --blue: #2a507e; --blue2: #305d8f; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #090e2e; }}
      #main-root {{ position: relative; width: 100%; height: 100%; overflow: hidden; font-family: Poppins, sans-serif; color: #fff; -webkit-font-smoothing: antialiased; }}
      .layer {{ position: absolute; inset: 0; }}
      /* BG: the user's navy gradient (4:5 original extended to 9:16 by mirrored, blurred bands — never stretched) */
      #bg .plate {{ position: absolute; inset: 0; background: url(assets/brand/bg_1080x1920.png) center / 1080px 1920px no-repeat; }}
      .glow {{ position: absolute; border-radius: 50%; mix-blend-mode: screen; }}
      #glow-a {{ left: -380px; top: 120px; width: 1000px; height: 1000px; background: radial-gradient(circle, rgba(48,93,143,.32), rgba(48,93,143,0) 66%); }}
      #glow-b {{ left: 480px; top: 1180px; width: 1000px; height: 1000px; background: radial-gradient(circle, rgba(42,80,126,.30), rgba(42,80,126,0) 66%); }}
      #grain {{ position: absolute; left: -64px; top: -64px; width: 1208px; height: 2048px; background: url(assets/brand/grain_256.png); opacity: .07; }}
      #vig {{ position: absolute; inset: 0; background: radial-gradient(ellipse 85% 70% at 50% 52%, rgba(0,0,0,0) 55%, rgba(4,6,24,.55) 100%); }}
      .dust {{ position: absolute; border-radius: 50%; background: radial-gradient(circle, rgba(160,230,255,.9), rgba(1,204,247,0) 70%); }}
      /* captions */
      .cap {{ position: absolute; left: 90px; right: 90px; top: 292px; text-align: center; font-size: 46px; line-height: 1.24; letter-spacing: -0.005em; }}
      .cap .m {{ display: inline-block; overflow: hidden; vertical-align: top; padding: 0.04em 0.1em 0.16em; margin: -0.04em -0.1em -0.16em; }}
      .cap .w {{ display: inline-block; }}
      .cap .b {{ font-weight: 700; color: var(--white); }}
      .cap .r {{ font-weight: 400; color: var(--cool); }}
      .cap .c {{ font-weight: 700; color: var(--cy); }}
      .cap .k {{ font-weight: 700; color: var(--cy); background: #ffffff; padding: 0 9px; border-radius: 2px; }}
      .cap {{ text-shadow: 0 2px 14px rgba(4,8,30,.55); }}
      .cap .k {{ text-shadow: none; }}
      /* SAFE ZONE (IG Reels): top ~250 px header, bottom ~420 px caption/username/buttons, right-side action icons.
         Every scene is scaled into the safe area (content x 110-970, y 460-1480); clipping is disabled so nothing gets
         cut at the scaled box edge — the main root still clips at the frame. */
      .safe-scene {{ transform-origin: 540px 955px; transform: scale(0.86); }}
      .safe-scene, .safe-scene > div, .safe-scene [data-composition-id] {{ overflow: visible !important; }}
    </style>
  </head>
  <body>
    <div id="main-root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      <div id="bg" class="clip layer" data-start="0" data-duration="{total}" data-track-index="0">
        <div class="plate"></div><div id="glow-a" class="glow"></div><div id="glow-b" class="glow"></div><div id="dust"></div>
      </div>
{slots}      <div id="mascot" class="clip" data-composition-id="mascot" data-composition-src="compositions/mascot.html" data-start="0" data-duration="{total}" data-track-index="6" data-width="1080" data-height="1920"></div>
      <div id="fx" class="clip layer" data-start="0" data-duration="{total}" data-track-index="7"><div id="vig"></div><div id="grain"></div></div>
      <div id="caps" class="clip layer" data-start="0" data-duration="{total}" data-track-index="8"></div>
      <audio id="vo" src="assets/audio/vo.mp3" data-start="0" data-duration="{T['vo_sec']}" data-track-index="9" data-volume="1"></audio>
    </div>
    <script>
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        const mk = (tag, cls, parent, html) => {{ const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; if (parent) parent.appendChild(e); return e; }};
        // VERIFIED word timings: [text, start, style]
        const W = [
          {W}
        ];
        // caption chunks: [start, end, firstWord, lastWord]
        const CAPS = [
          {C}
        ];
        const root = document.getElementById("caps");
        CAPS.forEach(([s, e, a, b], ci) => {{
          const c = mk("div", "cap clip", root); c.id = "cap" + ci;
          c.setAttribute("data-start", s); c.setAttribute("data-duration", (e - s).toFixed(3)); c.setAttribute("data-track-index", 8);
          for (let i = a; i <= b; i++) {{
            const st = W[i][2];
            const m = mk("span", "m", c);
            const w = mk("span", "w " + (st === "m" ? "k" : st), m, W[i][0]);
            if (i < b) c.appendChild(document.createTextNode(" "));
            const t = Math.max(s + 0.02, W[i][1] - 0.08);
            tl.set(w, {{ yPercent: 110, opacity: 0 }}, 0);
            tl.set(w, {{ opacity: 1 }}, t);
            tl.fromTo(w, {{ yPercent: 110 }}, {{ yPercent: 0, duration: 0.34, ease: "power4.out", immediateRender: false }}, t);
            if (st === "m") tl.fromTo(w, {{ scale: 1 }}, {{ scale: 1.08, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }}, t + 0.3);
          }}
        }});
        // ambient (seeded, seekable)
        let seed = 20261105;
        const rnd = () => {{ seed |= 0; seed = (seed + 0x6d2b79f5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }};
        for (let i = 0; i < 26; i++) {{
          const d = mk("div", "dust", document.getElementById("dust")); const sz = 3 + rnd() * 7;
          d.style.cssText += `width:${{sz}}px;height:${{sz}}px;left:${{rnd() * 1080}}px;top:${{260 + rnd() * 1560}}px;`;
          tl.set(d, {{ opacity: 0.15 + rnd() * 0.4 }}, 0);
          tl.fromTo(d, {{ y: 0, x: 0 }}, {{ y: -(90 + rnd() * 200), x: (rnd() - 0.5) * 60, duration: {total}, ease: "none", immediateRender: false }}, 0);
        }}
        tl.fromTo("#glow-a", {{ x: 0, y: 0 }}, {{ x: 90, y: 70, duration: {total}, ease: "sine.inOut", immediateRender: false }}, 0);
        tl.fromTo("#glow-b", {{ x: 0, y: 0 }}, {{ x: -110, y: -60, duration: {total}, ease: "sine.inOut", immediateRender: false }}, 0);
        tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 64, y: 40, duration: {total}, ease: "steps({int(total * 15)})", immediateRender: false }}, 0);
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
