"""S14 — DOODLE BOIL (effect #14).
Background slightly darkened; a hand-drawn 7px white line hugs the mascot's silhouette (SVG f-boil0..2 on #m-xf: three
versions cycled every 0.1 s = line boil). Two white doodle icons (light bulb top-left, sparkle top-right) boil with
the same 0.1 s rhythm (three displaced versions each)."""
from xk import box, r3, Rng

ICON_BULB = ('<path d="M0 -70 C 42 -70 70 -40 70 -4 C 70 26 50 42 40 60 L -40 60 C -50 42 -70 26 -70 -4 C -70 -40 -42 -70 0 -70 Z"/>'
             '<path d="M-34 84 L 34 84 M -26 106 L 26 106 M -16 60 L -10 20 L 0 34 L 10 20 L 16 60"/>'
             '<path d="M0 -104 L 0 -128 M 82 -76 L 100 -94 M -82 -76 L -100 -94 M 106 0 L 130 0 M -106 0 L -130 0"/>')
ICON_SPARK = ('<path d="M0 -92 C 8 -30 30 -8 92 0 C 30 8 8 30 0 92 C -8 30 -30 8 -92 0 C -30 -8 -8 -30 0 -92 Z"/>'
              '<path d="M86 -86 L 86 -50 M 68 -68 L 104 -68"/>'
              '<path d="M-78 70 C -78 60 -70 54 -62 60 C -54 54 -46 60 -46 70 C -46 82 -62 92 -62 92 C -62 92 -78 82 -78 70 Z"/>')


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    # ---------------------------------------------------------------- back: darkened plate + soft vignette
    S.back.append(f'<div class="abs" id="{s}-dim" style="left:0;top:0;width:1080px;height:1080px;'
                  f'background:radial-gradient(ellipse at 50% 45%, rgba(41,75,119,.42) 0%, rgba(20,34,70,.6) 55%, rgba(10,13,44,.78) 100%)"></div>')
    # ---------------------------------------------------------------- front: two boiling doodle icons
    defs = "".join(f'<filter id="{s}-wob{k}" x="-30%" y="-30%" width="160%" height="160%"><feTurbulence type="fractalNoise" baseFrequency="0.045" '
                   f'numOctaves="2" seed="{3 + k * 11}" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="9" xChannelSelector="R" yChannelSelector="G"/></filter>'
                   for k in range(3))
    stroke = 'fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
    for name, (cx, cy, icon, rot) in {"b": (175, 205, ICON_BULB, -8), "p": (912, 190, ICON_SPARK, 6)}.items():
        g = "".join(f'<g id="{s}-{name}{k}" filter="url(#{s}-wob{k})" opacity="{1 if k == 0 else 0}"><g {stroke}>{icon}</g></g>' for k in range(3))
        S.front.append(f'<svg class="abs" id="{s}-{name}" style="{box(cx - 160, cy - 160, 320, 320)}overflow:visible" viewBox="-160 -160 320 320">'
                       f'<defs>{defs if name == "b" else ""}</defs><g transform="rotate({rot})">{g}</g></svg>')
    # ---------------------------------------------------------------- motion: boil every 0.1 s (outline + icons in step)
    n = int(round((t1 - t0) / 0.1))
    for i in range(n):
        k = i % 3
        t = t0 + i * 0.1
        S.mset("#m-xf", {"filter": f"url(#f-boil{k})"}, t)
        for name in ("b", "p"):
            for j in range(3):
                if i == 0 and j != k:
                    continue
                if i > 0 and j not in (k, (i - 1) % 3):
                    continue
                S.tset(f"#{s}-{name}{j}", {"opacity": 1 if j == k else 0}, t)
    # icons on from frame 0 (thumbnail), stepped hand-drawn pulses
    for name, d in (("b", 0.0), ("p", 0.25)):
        S.init(f"#{s}-{name}", {"scale": 1, "transformOrigin": "50% 50%"})
        for b in (t0 + 0.4 + d, t0 + 2.2 + d, t0 + 3.9 + d):
            S.ft(f"#{s}-{name}", {"scale": 1}, {"scale": 1.14}, b, 0.3, "steps(3)")
            S.ft(f"#{s}-{name}", {"scale": 1.14}, {"scale": 1}, b + 0.3, 0.3, "steps(3)")

    # ---------------------------------------------------------------- mascot: medium shot, waves + presents the idea
    v = {"fx": 540, "fy": 1190, "h": 1040, "yaw": 0, "pitch": 5}
    S.mv([(t0, dict(v, yaw=4), None), (t1, dict(v, yaw=-6), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.4, "wave", 0.35), (t0 + 1.8, "pointUp", 0.35), (t0 + 3.3, "explain", 0.35)])
    S.act("armR", [(t0, "low", 0.3), (t0 + 1.0, "palmUp", 0.35), (t0 + 2.4, "pointUp", 0.35), (t0 + 3.6, "open", 0.35)])
    S.act("head", [(t0, [0, 0, 0], 0.3), (t0 + 0.4, [-0.04, 0.12, 0.06], 0.3), (t0 + 1.8, [-0.14, 0.2, 0], 0.35),
                   (t0 + 2.4, [-0.14, -0.2, 0], 0.35), (t0 + 3.4, [-0.02, 0.04, -0.04], 0.4)])
