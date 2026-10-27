"""S17 — GLASS TYPE (effect #17).
A big glass word VIRAL behind the head (white transparent gradient fill, thin white stroke, soft shadow, a moving
specular sheen) on a deep navy studio backdrop, tilting in 3D from rotateY -24 deg to -2 deg over the clip."""
from xk import box, r3

WORD, PX, WY = "VIRAL", 290, 96


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    S.back.append(f'<div class="abs" style="left:0;top:0;width:1080px;height:1080px;'
                  f'background:radial-gradient(ellipse at 50% 70%, #3c6aa3 0%, #294B77 30%, #142a52 62%, #0A0D2C 100%)"></div>')
    # soft colour light behind the glass (sells the refraction)
    S.back.append(f'<div class="abs" id="{s}-blob" style="{box(160, 60, 760, 420)}border-radius:50%;'
                  f'background:radial-gradient(ellipse, rgba(140,190,255,.55) 0%, rgba(80,130,210,.25) 45%, rgba(41,75,119,0) 72%)"></div>')
    glass = (f"font:700 {PX}px/1 Poppins, sans-serif;letter-spacing:-6px;white-space:nowrap;text-align:center;"
             "background:linear-gradient(180deg, rgba(255,255,255,.82) 0%, rgba(255,255,255,.30) 48%, rgba(220,235,255,.14) 100%);"
             "-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;-webkit-text-stroke:2px rgba(255,255,255,.9)")
    sheen = (f"font:700 {PX}px/1 Poppins, sans-serif;letter-spacing:-6px;white-space:nowrap;text-align:center;"
             "background:linear-gradient(105deg, rgba(255,255,255,0) 40%, rgba(255,255,255,.95) 50%, rgba(255,255,255,0) 60%) 0 0 / 300% 100% no-repeat;"
             "-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent")
    S.back.append(f'<div class="abs" style="left:0;top:0;width:1080px;height:1080px;perspective:1100px;perspective-origin:540px 260px">'
                  f'<div class="abs p3" id="{s}-word" style="left:0;top:{WY}px;width:1080px;height:{PX + 20}px">'
                  f'<div class="abs" style="left:0;top:0;width:1080px;{glass};filter:drop-shadow(0 26px 30px rgba(0,0,0,.38))">{WORD}</div>'
                  f'<div class="abs" id="{s}-sheen" style="left:0;top:0;width:1080px;{sheen}">{WORD}</div></div></div>')
    # floor glow under the mascot
    S.back.append(f'<div class="abs" style="{box(220, 900, 640, 220)}border-radius:50%;background:radial-gradient(ellipse, rgba(170,205,255,.35) 0%, rgba(41,75,119,0) 70%)"></div>')

    # ---------------------------------------------------------------- motion: 3D tilt -24 -> -2 deg across the clip, sheen sweeps
    S.init(f"#{s}-word", {"rotationY": -24, "rotationX": 8, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-word", {"rotationY": -24, "rotationX": 8}, {"rotationY": -2, "rotationX": 2}, t0 + 0.15, t1 - t0 - 0.35, "power1.inOut")
    S.init(f"#{s}-sheen", {"backgroundPosition": "100% 0%"})
    for a in (t0 + 0.6, t0 + 2.9):
        S.ft(f"#{s}-sheen", {"backgroundPosition": "100% 0%"}, {"backgroundPosition": "0% 0%"}, a, 1.0, "power2.inOut")
    S.init(f"#{s}-blob", {"x": -60})
    S.ft(f"#{s}-blob", {"x": -60}, {"x": 60}, t0, t1 - t0, "sine.inOut")

    # ---------------------------------------------------------------- mascot: in front of the glass word, hair overlaps it
    v = {"fx": 540, "fy": 1300, "h": 1060, "yaw": 10, "pitch": 4}
    S.mv([(t0, v, None), (t1, dict(v, yaw=-4), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.8, "pointUp", 0.4), (t0 + 2.3, "explain", 0.4), (t0 + 3.6, "low", 0.45)])
    S.act("armR", [(t0, "low", 0.3), (t0 + 2.4, "open", 0.4), (t0 + 3.7, "low", 0.45)])
    S.act("head", [(t0, [0, -0.06, 0], 0.3), (t0 + 0.8, [-0.16, 0.18, 0.02], 0.4), (t0 + 2.3, [0.0, -0.06, -0.04], 0.45), (t0 + 3.8, [-0.02, 0.06, 0.03], 0.45)])
    S.mset("#m-xf", {"filter": "drop-shadow(0px 18px 24px rgba(0,0,0,0.35))"}, t0)
