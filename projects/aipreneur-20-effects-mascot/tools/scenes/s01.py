"""S01 — THE BORING SOURCE (3.40–4.97)  VO: "Karakter ini awalnya cuma diam."
The identical plain panel S00 landed on: flat cyc, thin white frame, 'KLIP POLOS' tag, the live mascot medium and
lock-off. Deliberately effect-free; he only breathes, glances, and gives a small head turn on "diam".
Hand-off: in the last 0.36 s the frame line rounds its corners and squeezes into the tilted orbit ellipse around his
head (ORBIT contract) while the clip releases and the flat plate falls away -> S02 opens on that ring."""
from xk import box, r3, clip_rect, CLIP_NONE
from kit import MED
from kit_a import panel_bg, panel_border, panel_label, PX, PY, PW, PH, PR, RING_FROM_PANEL, radii


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W8, W10, W11, W12 = S.W(8), S.W(10), S.W(11), S.W(12)     # Karakter 3.48, awalnya 4.02, cuma 4.34, diam 4.58
    m0 = t1 - 0.36                                              # morph start
    S.back.append(panel_bg(f"{s}-pbg"))
    S.front.append(panel_border(f"{s}-pbd"))
    S.front.append(panel_label(f"{s}-plb"))

    # ---------------------------------------------------------------- hand-off: frame line -> orbit ring
    S.init(f"#{s}-pbd", dict(radii(PR, PR), scaleX=1, scaleY=1, x=0, y=0, rotation=0, transformOrigin="50% 50%"))
    S.ft(f"#{s}-pbd", dict(radii(PR, PR), scaleX=1, scaleY=1, x=0, y=0, rotation=0),
         dict(radii(PW / 2, PH / 2), **RING_FROM_PANEL), m0, t1 - m0, "power3.inOut")
    S.init(f"#{s}-pbg", {"opacity": 1, "scale": 1, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-pbg", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.96}, m0, t1 - m0 - 0.06, "power2.out")
    S.init(f"#{s}-plb", {"opacity": 1})
    S.ft(f"#{s}-plb", {"opacity": 1}, {"opacity": 0}, m0, 0.12, "none")

    # ---------------------------------------------------------------- mascot: medium, lock-off, clip releases on the morph
    S.mv([(t0, dict(MED), None), (W12, dict(MED, yaw=-4), "sine.inOut"), (t1, dict(MED, yaw=0), "sine.inOut")])
    S.mc([(t0, {"clipPath": clip_rect(PX, PY, PW, PH, PR)}, None), (m0, {}, "none"), (t1, {"clipPath": CLIP_NONE}, "power2.in")])
    S.act("head", [(t0, [-0.02, 0.04, 0.02], 0.3), (W10, [0.02, -0.06, -0.02], 0.35), (W12 - 0.08, [-0.08, 0.22, 0.06], 0.3),
                   (W12 + 0.3, [-0.1, 0.24, 0.05], 0.3)])
    S.act("armL", [(t0, "low", 0.3), (W11 - 0.12, "palmUp", 0.3), (W12 + 0.12, "low", 0.35)])
    S.act("armR", [(t0, "low", 0.3)])
    S.act("torso", [(t0, {}, 0.3), (W12 - 0.1, {"spine": [0, 0, 0.03], "chest": [0, 0.06, 0]}, 0.35)])
    S.fx(m0 + 0.06, "whoosh", 0.05)
