"""S16 — 15 ZOOM THROUGH CUT (28.30–29.70)  VO: "Kita zoom menembus satu frame,"
Opens on S15's lens: a satin-metal iris (8 blades) with its opening exactly on the LENS circle over the face.
"Kita zoom": the iris opens and turns. "menembus": a thin white frame flies at the lens and the camera pushes
THROUGH it with a speed ramp (frame passes the lens, motion blur at peak speed) into an extreme close-up of the
eye (real camera re-framing on the 3D model). "satu frame": the pupil's dark grows until it fills the frame -
S17 opens a circle out of that dark."""
import math
from xk import box, r3, CYAN
from kit import MED, NO_FILTER, LENS

EYE_X = 0.082                    # model-space x of the eye we push into (eyeB, face calibration)
EYE_U = 0.584


def eye_view(h, pitch=3, ey=960, ex=540):
    k = h / 0.98
    return {"fx": round(ex - EYE_X * k, 1), "fy": round(ey + EYE_U * k, 1), "h": h, "yaw": 0, "pitch": pitch}


FLT = "blur({b}px) drop-shadow(0px 0px 0px rgba(0,208,254,0))"


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W77, W78, W79, W80, W81 = (S.W(i) for i in range(77, 82))   # Kita 28.38 zoom 28.66 menembus 28.80 satu 29.16 frame 29.38
    cx, cy, d = LENS
    R0 = d / 2
    # ---------------------------------------------------------------- back: navy light pool (S15 continuity)
    S.back.append(f'<div class="abs" style="{box(0, 0, 1080, 1920)}background:radial-gradient(ellipse 60% 40% at 50% 48%,rgba(90,150,230,.35),rgba(90,150,230,0) 70%)"></div>')
    S.back.append(f'<div class="abs" id="{s}-tun" style="{box(cx - 700, cy - 700, 1400, 1400)}border-radius:50%;'
                  f'background:repeating-radial-gradient(circle,rgba(0,208,254,0) 0 60px,rgba(0,208,254,.16) 61px 63px,rgba(0,208,254,0) 64px 120px)"></div>')
    # ---------------------------------------------------------------- front: iris blades, thin frame, pupil dark
    blades = []
    for k in range(8):
        th = k * 45 + 12
        blades.append(f'<div class="abs" style="{box(cx - 900, cy, 1800, 1)}transform-origin:900px 0px;transform:rotate({th}deg)">'
                      f'<div class="abs" id="{s}-b{k}" style="left:0;top:{r3(R0)}px;width:1800px;height:1500px;'
                      f'background:linear-gradient(180deg,#b8c3d2 0px,#6d7a90 6px,#3a4558 40px,#1d2536 260px,#121826 100%);'
                      f'box-shadow:0 -2px 0 rgba(255,255,255,.55),0 -10px 24px rgba(3,8,28,.6)"></div></div>')
    S.front.append(f'<div class="abs" id="{s}-iris" style="{box(0, 0, 1080, 1920)}">' + "".join(blades) +
                   f'<div class="abs" id="{s}-irim" style="{box(cx - R0 - 8, cy - R0 - 8, d + 16, d + 16)}border-radius:50%;box-shadow:0 0 0 3px rgba(0,208,254,.55),0 0 26px rgba(0,208,254,.4)"></div></div>')
    S.front.append(f'<div class="abs" id="{s}-fr" style="{box(cx - 330, cy - 430, 660, 860)}border-radius:18px;border:5px solid #fff;box-shadow:0 0 18px rgba(0,208,254,.7),inset 0 0 18px rgba(0,208,254,.35)"></div>')
    S.front.append(f'<div class="abs" id="{s}-dark" style="{box(540 - 60, 960 - 60, 120, 120)}border-radius:50%;background:radial-gradient(circle,#03081c 0%,#050b1e 62%,#0a1738 100%);'
                   f'box-shadow:0 0 0 2px rgba(0,208,254,.35)"></div>')
    S.front.append(f'<div class="abs" id="{s}-glint" style="{box(540 - 300, 960 - 300, 600, 600)}border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.55),rgba(160,240,255,.18) 35%,rgba(0,208,254,0) 70%)"></div>')

    # ---------------------------------------------------------------- motion
    o0, o1 = W77 - 0.02, W78 + 0.12                     # iris opens on "Kita zoom"
    for k in range(8):
        S.init(f"#{s}-b{k}", {"y": 160})
        S.ft(f"#{s}-b{k}", {"y": 160}, {"y": 0}, t0, 0.12, "power3.out")          # blades close onto the lens rim
        S.ft(f"#{s}-b{k}", {"y": 0}, {"y": 900}, o0 + 0.1, o1 - o0 - 0.1, "power3.inOut")
    S.init(f"#{s}-iris", {"rotation": 8, "opacity": 0.75, "transformOrigin": f"{cx}px {cy}px"})
    S.ft(f"#{s}-iris", {"rotation": 8, "opacity": 0.75}, {"rotation": 0, "opacity": 1}, t0, 0.12, "power3.out")
    S.ft(f"#{s}-iris", {"rotation": 0}, {"rotation": -28}, o0 + 0.1, o1 - o0 - 0.1, "power3.inOut")
    S.init(f"#{s}-irim", {"opacity": 1, "scale": 1})
    S.ft(f"#{s}-irim", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 2.6}, o0, 0.4, "power2.in")
    S.init(f"#{s}-tun", {"opacity": 0, "scale": 0.4})
    S.ft(f"#{s}-tun", {"opacity": 0, "scale": 0.4}, {"opacity": 1, "scale": 1.2}, W78, 0.17, "power2.out")
    S.ft(f"#{s}-tun", {"opacity": 1, "scale": 1.2}, {"opacity": 0, "scale": 3.4}, W79 + 0.05, 0.4, "power3.in")
    # the thin frame flies at the lens and passes it ("menembus")
    p0, p1 = W79 - 0.06, W80 + 0.02
    S.init(f"#{s}-fr", {"opacity": 0, "scale": 0.35, "transformOrigin": "330px 430px"})
    S.ft(f"#{s}-fr", {"opacity": 0, "scale": 0.35}, {"opacity": 1, "scale": 0.6}, W78 + 0.04, p0 - W78 - 0.04, "power2.out")
    S.ft(f"#{s}-fr", {"opacity": 1, "scale": 0.6}, {"opacity": 0.9, "scale": 4.2}, p0, p1 - p0, "power3.in")
    S.tset(f"#{s}-fr", {"opacity": 0}, p1)
    # pupil dark grows to fill the frame ("satu frame")
    g0 = W81 - 0.08
    S.init(f"#{s}-dark", {"scale": 0, "opacity": 0})
    S.tset(f"#{s}-dark", {"opacity": 1}, g0)
    S.ft(f"#{s}-dark", {"scale": 0.6}, {"scale": 22}, g0, t1 - g0 - 0.03, "power2.in")
    S.init(f"#{s}-glint", {"opacity": 0, "scale": 0.4})
    S.ft(f"#{s}-glint", {"opacity": 0, "scale": 0.4}, {"opacity": 0.8, "scale": 1}, p1 - 0.05, 0.16, "power2.out")
    S.ft(f"#{s}-glint", {"opacity": 0.8, "scale": 1}, {"opacity": 0, "scale": 1.8}, p1 + 0.11, 0.3, "power2.in")

    # ---------------------------------------------------------------- mascot: MED -> (speed ramp) ECU eye -> into the pupil
    S.mv([(t0, MED, None), (W78, dict(MED, h=1700, fy=1800 + 0.585 * (1700 - 1470) / 0.98), "sine.inOut"),
          (p1, eye_view(3920), "power3.in"),
          (g0 + 0.15, eye_view(6400), "power2.out"),
          (t1, eye_view(7600), "power1.in")])
    S.mx([(t0, {"filter": FLT.format(b=0), "transformOrigin": "540px 960px"}, None),
          (p0 + 0.08, {"filter": FLT.format(b=0)}, "none"),
          (p1 - 0.06, {"filter": FLT.format(b=6)}, "power2.in"),
          (p1 + 0.14, {"filter": FLT.format(b=0)}, "power2.out")])
    S.act("head", [(t0 + 0.02, [0, 0, 0], 0.3), (W77, [-0.03, 0, 0.02], 0.4)])
    S.act("armL", [(t0 + 0.02, "low", 0.3)])
    S.act("armR", [(t0 + 0.02, "low", 0.3)])
    S.act("root", [(t0 + 0.02, {"ry": 0, "y": 0}, 0.3)])
    S.fx(o0 + 0.02, "click", 0.06)
    S.fx(p0, "whoosh", 0.07)
    S.fx(g0, "whoosh", 0.04)
