"""Turns production/motion_plan.json (tools/motion_director.py) into:
  compositions/director.html      overlay effects built with vendor/motion-director.js (z 35, under the host)
  production/director_camera.json camera effects for the root timeline (snap / digital / dolly zoom)
Layout per (scene, effect) lives here: where each effect may sit without covering the hero, the host's
face or the captions band (y 220-385).
"""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
plan = json.loads((P / "production/motion_plan.json").read_text())["effects"]
words = json.loads((P / "production/word_timing.json").read_text())["words"]
scenes = {s["id"]: s for s in json.loads((P / "production/scenes.json").read_text())["scenes"]}
W = lambda i: round(words[i]["start"], 3)
GH = "assets/elements/ref15_github_mark_3d.png"   # Freddie's 3D GitHub mark (background removed)

js, html, cam = [], [], []
for e in plan:
    fx, at, sid = e["effect"], e["at"], e["scene"]
    end = scenes[sid]["end"] if sid in scenes else 61.1
    pr = e.get("preset", "STANDARD")
    if fx == "studioReveal":
        js.append(f'MD.fx.studioReveal(ctx, {{ at: {at}, dur: 1.1, preset: "{pr}" }});')
    elif fx == "snapZoom":
        cam.append({"fx": "snapZoom", "opts": {"target": "#world", "at": at, "amount": 0.07, "origin": "540px 760px", "preset": pr, "hold": 0.3, "release": 0.45}})
    elif fx == "digitalZoom":
        cam.append({"fx": "digitalZoom", "opts": {"target": "#world", "at": round(at - 0.1, 3), "amount": 0.07, "dy": -30, "dur": 0.45, "preset": pr, "releaseAt": round(end - 0.42, 3)}})
    elif fx == "dollyZoom":
        cam.append({"fx": "dollyZoom", "opts": {"background": "#stage-dir", "at": round(at - 0.08, 3), "dur": 0.85, "preset": pr}})
    elif fx == "orbitReveal" and sid == "s02":
        html.append(f'<div class="md-gh" id="dir-gh1" style="left:770px;top:790px;width:240px;height:265px"><img src="{GH}" alt="" /><div class="md-gh-glint" id="dir-gh1g"></div></div>')
        js.append(f'MD.fx.orbitReveal(ctx, {{ target: "#dir-gh1", glint: "#dir-gh1g", at: {round(at - 0.12, 3)}, preset: "{pr}", restY: -12, until: {round(W(17) + 0.25, 3)}, dir: "R" }});')
        js.append(f'tl.fromTo("#dir-gh1 img", {{ y: 0 }}, {{ y: -10, duration: 0.55, ease: "sine.inOut", yoyo: true, repeat: 1, immediateRender: false }}, {round(at + 0.7, 3)});')
    elif fx == "growthCurve":
        js.append(f'MD.fx.growthCurve(ctx, {{ x: 680, y: 780, w: 370, h: 320, at: {round(at - 0.2, 3)}, dir: "R", preset: "{pr}", drawDur: {round(W(20) - at + 0.15, 3)}, icon: "assets/elements/star_badge.svg", until: {round(end - 0.3, 3)} }});')
    elif fx == "chatTakeover":
        js.append(f'''MD.fx.chatTakeover(ctx, {{ x: 60, y: 420, w: 960, h: 500, at: {round(at - 0.05, 3)}, preset: "{pr}", dir: "L", until: {round(end - 0.27, 3)},
  messages: [{{ side: "R", type: "video", src: "assets/elements/ref5_player_phone.png", at: {round(W(25) - 0.1, 3)}, sfx: "pop" }},
             {{ side: "L", type: "typing", at: {round(W(28) - 0.08, 3)} }},
             {{ side: "L", type: "code", w: 150, h: 70, at: {round(W(30), 3)}, sfx: "pop" }}],
  takeoverAt: {round(W(31) - 0.05, 3)}, takeover: {{ x: 40, y: 400, w: 1000, h: 540, src: "assets/elements/ref4_app_ui.png", imgW: "86%" }}, takeoverSfx: "whoosh" }});''')
    elif fx == "checklistPop":
        items = [(i, words[i]["text"].rstrip(",.:")) for i in (49, 50, 51, 53)]
        rows = ", ".join(f'{{ label: "{t}", at: {W(i)}, sfx: "key" }}' for i, t in items)
        js.append(f'MD.fx.checklistPop(ctx, {{ x: 610, y: 420, w: 430, h: 372, at: {round(at - 0.45, 3)}, rowH: 70, dir: "R", preset: "{pr}", until: {round(end - 0.3, 3)}, items: [{rows}] }});')
    elif fx == "orbitReveal" and sid == "s18":
        html.append(f'<div class="md-gh" id="dir-gh2" style="left:60px;top:300px;width:200px;height:221px"><img src="assets/elements/source/ref15_github_mark_3d.webp" alt="" /><div class="md-gh-glint" id="dir-gh2g"></div></div>')
        js.append(f'MD.fx.orbitReveal(ctx, {{ target: "#dir-gh2", glint: "#dir-gh2g", at: {round(at + 0.2, 3)}, preset: "{pr}", restY: 14, until: 58.45, dir: "L" }});')
    elif fx == "frameEscape" and sid == "s19":
        # Frame Escape / Frame Break: a glass frame lands behind the host; on 'HYPIT' its top edge shatters
        # and his head + pointing arm break out over the border (the host is drawn above the frame)
        html.append('<div id="dir-cta-glass" style="position:absolute;left:600px;top:1395px;width:460px;height:560px;border-radius:44px;background:linear-gradient(165deg,rgba(255,255,255,.6),rgba(214,229,248,.45))"></div>')
        js.append('gsap.set("#dir-cta-glass", { opacity: 0, y: 140 });')
        js.append(f'tl.fromTo("#dir-cta-glass", {{ opacity: 0, y: 140 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "expo.out", immediateRender: false }}, {round(at - 0.4, 3)});')
        js.append(f'MD.fx.frameBreak(ctx, {{ frame: {{ x: 600, y: 1395, w: 460, h: 560 }}, at: {round(at - 0.4, 3)}, breakAt: {round(at, 3)}, preset: "{pr}", gapColor: "transparent" }});')

# SFX cues for the director effects (merged into tools/sfx_plan.json as "v5 ..." cues)
SFX_FILE = {"pop": ("pop.mp3", 0.1193, 0.72, 0.09), "click": ("click-soft.mp3", 0.0723, 0.366, 0.15), "key": ("key-press.mp3", None, None, 0.11),
            "whoosh": ("whoosh-short.mp3", None, None, 0.07), "sparkle": ("sparkle.mp3", 0.0263, 1.8, 0.08)}
sp = P / "tools/sfx_plan.json"
sfx = [x for x in json.loads(sp.read_text()) if not x["cue"].startswith("v5 ")]
def ref(file):
    x = next(y for y in sfx if y["file"] == file)
    return round(x["apex"] + 1 / 30 - x["t"], 4), x["dur"]
cues = []
for e in plan:
    fx, at = e["effect"], e["at"]
    if fx == "studioReveal": cues.append(("whoosh", 0.25))
    elif fx == "snapZoom": cues.append(("click", at))
    elif fx == "orbitReveal": cues.append(("sparkle", at + 0.1))
    elif fx == "growthCurve": cues.append(("whoosh", at)); cues.append(("pop", W(20)))
    elif fx == "chatTakeover": cues += [("pop", W(25)), ("pop", W(28)), ("pop", W(30)), ("whoosh", W(31))]
    elif fx == "checklistPop": cues += [("key", W(i)) for i in (49, 50, 51, 53)]
    elif fx == "dollyZoom": cues.append(("whoosh", at - 0.05))
    elif fx == "frameEscape": cues.append(("sparkle", at + 0.1))
for name, apex in cues:
    f, pk, d, vol = SFX_FILE[name]
    if pk is None: pk, d = ref(f)
    sfx.append({"cue": f"v5 {name}", "apex": round(apex, 3), "t": round(apex + 1 / 30 - pk, 3), "file": f, "dur": d, "vol": vol})
sfx.sort(key=lambda x: x["t"])
sp.write_text(json.dumps(sfx, indent=1))

# a tiny star badge for the growth curve tip (inline SVG file so it can be used as <img>)
(P / "assets/elements/star_badge.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#294b77"/><stop offset="1" stop-color="#0a0d2c"/></linearGradient></defs><circle cx="32" cy="32" r="30" fill="url(#g)"/><path d="M32 13l5.6 11.6 12.8 1.8-9.3 9 2.2 12.7L32 42.1l-11.3 6 2.2-12.7-9.3-9 12.8-1.8z" fill="#fff"/></svg>')

doc = f"""<template>
  <style>
    #dir-root {{ position: absolute; inset: 0; pointer-events: none; overflow: hidden; }}
    .md-gh {{ position: absolute; }}
    .md-gh img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; filter: drop-shadow(0 22px 26px rgba(10,13,44,.32)); }}
    .md-gh-glint {{ position: absolute; inset: 0; background: linear-gradient(100deg, rgba(255,255,255,0) 35%, rgba(255,255,255,.55) 50%, rgba(255,255,255,0) 65%);
      -webkit-mask: url({GH}) center / contain no-repeat; mask: url({GH}) center / contain no-repeat; }}
  </style>
  <div id="dir-root" data-composition-id="director" data-width="1080" data-height="1920">
    {chr(10).join("    " + h for h in html).strip()}
  </div>
  <script>
    (function () {{
      // Generated by tools/gen_director.py from production/motion_plan.json (Smart Motion Director).
      const tl = gsap.timeline({{ paused: true }});
      const ctx = {{ tl, root: document.getElementById("dir-root") }};
      {chr(10).join("      " + l for l in js).strip()}
      tl.set({{}}, {{}}, 61.08);
      window.__timelines = window.__timelines || {{}};
      window.__timelines["director"] = tl;
    }})();
  </script>
</template>
"""
(P / "compositions/director.html").write_text(doc)
(P / "production/director_camera.json").write_text(json.dumps(cam, indent=1))
print("director.html:", len(js), "effect calls;", len(cam), "camera moves")
