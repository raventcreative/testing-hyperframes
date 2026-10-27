"""S06 — 05/06 SPOTLIGHT (18.83–20.63)  VO: "Panggung spotlight muncul."
Opens on S05's hand-off: one bright glint line across the frame at y = GLINT_Y. The line gathers into a small stage
lamp (upper-left, the scene's key direction) and opens as a real cone of light down onto the mascot: local stage
dim (radial navy vignette, the pale plate stays readable at the margins), a floor pool + contact shadow that agree
with the beam, slow seeded dust motes in the cone. "Panggung": he turns his head up into the beam; "spotlight":
the light lands and he brightens; "muncul": confident open hero pose, held. Beat end: his lifted palm catches the
light and a thin luminous iris forms at IRIS (S07 opens on it and turns it into the colour-grade dial)."""
from xk import box, r3, Rng
from kit import WIDE, GLINT_Y, NO_FILTER
from kit_c import IRIS_C as IRIS, S06_END, S05_END

LAMP = (330, 336)                      # beam apex (lamp lens)
FLOOR = (480, 1726)                    # beam centre on the floor
CONE = f"polygon({LAMP[0] - 30}px {LAMP[1]}px, {LAMP[0] + 30}px {LAMP[1]}px, 820px 1760px, 150px 1760px)"
FLT = "brightness({b}) drop-shadow(0px 0px 0px rgba(0,208,254,0))"


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W39, W40, W41 = S.W(39), S.W(40), S.W(41)      # Panggung 18.92, spotlight 19.26, muncul 19.82
    on = W40 - 0.02                                # light lands
    ix, iy, idm = IRIS
    # ---------------------------------------------------------------- back: local stage dim, cone, floor pool, lamp
    S.back.append(f'<div class="abs" id="{s}-dim" style="{box(0, 0, 1080, 1920)}'
                  f'background:radial-gradient(ellipse 78% 62% at 50% 56%, rgba(10,13,44,.52) 0%, rgba(10,13,44,.40) 46%, rgba(10,13,44,.10) 82%, rgba(10,13,44,0) 100%)"></div>')
    S.back.append(f'<div class="abs" id="{s}-cone" style="{box(0, 0, 1080, 1920)}clip-path:{CONE};'
                  f'background:linear-gradient(160deg, rgba(255,255,255,.92) 0%, rgba(236,243,255,.55) 30%, rgba(222,234,252,.30) 70%, rgba(222,234,252,.12) 100%);'
                  f'filter:blur(6px)"></div>')
    S.back.append(f'<div class="abs" id="{s}-pool" style="{box(FLOOR[0] - 380, FLOOR[1] - 70, 760, 150)}border-radius:50%;'
                  f'background:radial-gradient(ellipse at 50% 50%, rgba(255,255,255,.95) 0%, rgba(236,244,255,.6) 45%, rgba(236,244,255,0) 72%)"></div>')
    # cast shadow falls down-right of the feet (light comes from the upper left)
    S.back.append(f'<div class="abs" id="{s}-cast" style="{box(FLOOR[0] - 40, FLOOR[1] - 24, 420, 64)}border-radius:50%;transform:skewX(-32deg);'
                  f'background:radial-gradient(ellipse at 30% 50%, rgba(10,13,44,.42) 0%, rgba(10,13,44,.18) 45%, rgba(10,13,44,0) 72%)"></div>')
    # motes (seeded) inside the cone
    R = Rng(6060)
    motes = []
    for k in range(12):
        u = R.u(0.18, 0.92)                         # along the beam
        cx = LAMP[0] + (FLOOR[0] - LAMP[0]) * u + R.u(-1, 1) * 200 * u
        cy = LAMP[1] + (1700 - LAMP[1]) * u
        d = R.u(4, 9)
        motes.append((k, cx, cy, d, R.u(-50, -110), R.u(-20, 20), R.u(0.35, 0.85)))
        S.back.append(f'<div class="abs" id="{s}-m{k}" style="{box(cx, cy, d, d)}border-radius:50%;background:radial-gradient(circle,#fff 0%,rgba(255,255,255,.4) 55%,rgba(255,255,255,0) 72%)"></div>')
    # lamp fixture (anodized can + barn-door lip), aimed down-right along the beam
    S.back.append(f'<div class="abs" id="{s}-lamp" style="{box(LAMP[0] - 70, LAMP[1] - 64, 140, 76)}transform:rotate(28deg);transform-origin:70px 64px">'
                  f'<div class="abs anod" style="{box(14, 0, 112, 60)}border-radius:16px 16px 10px 10px"></div>'
                  f'<div class="abs" style="{box(0, 54, 140, 12)}border-radius:6px;background:linear-gradient(180deg,#5b6779,#2b3445)"></div>'
                  f'<div class="abs" id="{s}-lens" style="{box(30, 58, 80, 14)}border-radius:7px;background:radial-gradient(ellipse at 50% 30%,#ffffff,#e8f0ff 60%,#9fb4d6)"></div></div>')
    # the incoming glint line (S05 hand-off), gathers into the lamp
    S.back.append(f'<div class="abs glint" id="{s}-line" style="{box(0, GLINT_Y - 3, 1080, 6)}border-radius:3px"></div>')
    # ---------------------------------------------------------------- front: soft volumetric haze over the mascot, lens flare, iris
    S.front.append(f'<div class="abs" id="{s}-haze" style="{box(0, 0, 1080, 1920)}clip-path:{CONE};'
                   f'background:linear-gradient(160deg, rgba(255,255,255,.55) 0%, rgba(240,246,255,.16) 45%, rgba(240,246,255,0) 100%);filter:blur(10px)"></div>')
    S.front.append(f'<div class="abs" id="{s}-flare" style="{box(LAMP[0] - 120, LAMP[1] - 110, 240, 240)}border-radius:50%;'
                   f'background:radial-gradient(circle, rgba(255,255,255,1) 0%, rgba(235,243,255,.65) 22%, rgba(235,243,255,0) 62%)"></div>')
    S.front.append(f'<div class="abs" id="{s}-iris" style="{box(ix - idm / 2, iy - idm / 2, idm, idm)}border-radius:50%;'
                   f'border:4px solid rgba(255,255,255,.98);box-shadow:0 0 18px rgba(255,255,255,.95), 0 0 40px rgba(190,215,250,.8), inset 0 0 22px rgba(255,255,255,.75)"></div>')
    S.front.append(f'<div class="abs" id="{s}-irisc" style="{box(ix - idm * 0.32, iy - idm * 0.32, idm * 0.64, idm * 0.64)}border-radius:50%;'
                   f'background:radial-gradient(circle, rgba(255,255,255,.85) 0%, rgba(230,240,255,.35) 50%, rgba(230,240,255,0) 72%)"></div>')

    # ---------------------------------------------------------------- motion
    # glint line gathers into the lamp lens (shrinks toward the lamp x while rising to it)
    S.init(f"#{s}-line", {"x": 0, "y": 0, "scaleX": 1, "opacity": 1, "transformOrigin": f"{LAMP[0]}px 3px"})
    S.ft(f"#{s}-line", {"y": 0, "scaleX": 1}, {"y": LAMP[1] - GLINT_Y, "scaleX": 0.04}, t0 + 0.01, 0.26, "power3.in")
    S.ft(f"#{s}-line", {"opacity": 1}, {"opacity": 0}, t0 + 0.24, 0.06, "none")
    # stage dims locally
    S.init(f"#{s}-dim", {"opacity": 0})
    S.ft(f"#{s}-dim", {"opacity": 0}, {"opacity": 1}, t0 + 0.02, 0.4, "power2.out")
    # lamp drops into place, lens flares, cone opens from the apex
    S.init(f"#{s}-lamp", {"y": -120, "opacity": 0})
    S.ft(f"#{s}-lamp", {"y": -120, "opacity": 0}, {"y": 0, "opacity": 1}, t0 + 0.02, 0.26, "power3.out")
    S.init(f"#{s}-flare", {"opacity": 0, "scale": 0.3})
    S.ft(f"#{s}-flare", {"opacity": 0, "scale": 0.3}, {"opacity": 1, "scale": 1}, t0 + 0.26, 0.12, "power2.out")
    S.ft(f"#{s}-flare", {"opacity": 1, "scale": 1}, {"opacity": 0.55, "scale": 0.8}, t0 + 0.38, 0.4, "power2.out")
    for sel, op in ((f"#{s}-cone", 1), (f"#{s}-haze", 1)):
        S.init(sel, {"opacity": 0, "scaleX": 0.06, "scaleY": 0.35, "transformOrigin": f"{LAMP[0]}px {LAMP[1]}px"})
        S.ft(sel, {"opacity": 0, "scaleX": 0.06, "scaleY": 0.35}, {"opacity": op, "scaleX": 1, "scaleY": 1}, t0 + 0.27, on - t0 - 0.2, "power3.out")
    S.init(f"#{s}-pool", {"opacity": 0, "scale": 0.4})
    S.ft(f"#{s}-pool", {"opacity": 0, "scale": 0.4}, {"opacity": 1, "scale": 1}, on - 0.04, 0.3, "power2.out")
    S.init(f"#{s}-cast", {"opacity": 0})
    S.ft(f"#{s}-cast", {"opacity": 0}, {"opacity": 1}, on, 0.3, "power2.out")
    # motes drift slowly (finite, linear)
    for (k, cx, cy, d, dy, dx, op) in motes:
        S.init(f"#{s}-m{k}", {"opacity": 0, "x": 0, "y": 0})
        S.ft(f"#{s}-m{k}", {"opacity": 0}, {"opacity": op}, on + 0.02 * k, 0.3, "power1.out")
        S.ft(f"#{s}-m{k}", {"x": 0, "y": 0}, {"x": r3(dx), "y": r3(dy)}, on, t1 - on, "none")
    # beat end: the palm catches the light -> iris
    ir = W41 + 0.52
    S.init(f"#{s}-iris", {"opacity": 0, "scale": 0.2, "rotation": -40})
    S.ft(f"#{s}-iris", {"opacity": 0, "scale": 0.2, "rotation": -40}, {"opacity": 1, "scale": 1, "rotation": 0}, ir, t1 - ir - 0.02, "power3.out")
    S.init(f"#{s}-irisc", {"opacity": 0, "scale": 0.3})
    S.ft(f"#{s}-irisc", {"opacity": 0, "scale": 0.3}, {"opacity": 1, "scale": 1}, ir - 0.04, 0.16, "power2.out")
    S.ft(f"#{s}-irisc", {"opacity": 1, "scale": 1}, {"opacity": 0.35, "scale": 0.8}, ir + 0.12, t1 - ir - 0.14, "power2.out")

    # ---------------------------------------------------------------- mascot: full body on stage, turns into the beam, hero pose
    # continues S05's framing, then the camera settles on the stage while the beam opens
    S.mv([(t0, S05_END, None), (t0 + 0.42, dict(S06_END, yaw=16, pitch=5), "power3.inOut"),
          (on + 0.1, dict(S06_END, yaw=6, pitch=5), "sine.inOut"), (t1, S06_END, "sine.inOut")])
    S.mx([(t0, {"filter": FLT.format(b=0.82)}, None), (on - 0.05, {"filter": FLT.format(b=0.82)}, "none"),
          (on + 0.12, {"filter": FLT.format(b=1.14)}, "power2.out"), (on + 0.55, {"filter": FLT.format(b=1.05)}, "power2.inOut")])
    S.act("head", [(t0 + 0.02, [0.02, 0.18, 0], 0.3), (W39 - 0.02, [-0.2, -0.32, 0.06], 0.35),     # looks up into the lamp
                   (W41 - 0.06, [-0.1, -0.06, 0.02], 0.3), (ir - 0.08, [-0.06, 0.18, -0.04], 0.3)])  # then to his palm
    S.act("torso", [(t0 + 0.02, {"chest": [0.02, 0.06, 0]}, 0.3), (on, {"chest": [-0.08, -0.04, 0], "spine": [-0.04, 0, 0]}, 0.3),
                    (W41 - 0.08, {"chest": [-0.1, 0, 0], "spine": [-0.05, 0, 0]}, 0.25)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W41 - 0.14, "open", 0.28), (ir + 0.05, "low", 0.4)])
    S.act("armL", [(t0 + 0.02, "low", 0.3), (W41 - 0.14, "open", 0.28), (ir - 0.3, "present", 0.3)])
    S.act("root", [(t0 + 0.02, {"y": 0, "ry": 0.1}, 0.3), (on, {"y": 0.008, "ry": 0}, 0.25), (on + 0.3, {"y": 0}, 0.3)])
    S.fx(t0 + 0.2, "whoosh", 0.05)
    S.fx(on - 0.02, "click", 0.09)
    S.fx(ir, "sparkle", 0.05)
