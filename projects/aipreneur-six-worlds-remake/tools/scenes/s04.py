"""S04 — 03/06 BACKDROP WORD (12.67–17.10)
VO: "Huruf itu terbuka, memperlihatkan panel kaca yang bergerak mengikuti kamera."
Opens on the matte navy extruded C filling LETTER_C (S03's monitor edge became that stroke). The camera pulls back:
the rest of the giant dimensional word CLAUDE rises from the stage floor behind the mascot (letters behind the canvas
= real occlusion; extruded sides + floor contact/cast shadows from an upper-left key). The mascot arrives in front and
looks up at the sign; the camera slides on a small arc (mascot yaw + slower letter parallax).
"terbuka": C and L part like mechanical doors (C swings left on its hinge, L slides right). "memperlihatkan panel
kaca": a translucent glass pane behind the sign shows through the gap, its edges light up as rims. "bergerak
mengikuti kamera": the camera pushes into the gap (sign scales around the gap centre, the mascot passes by the lens
and leaves frame right) while the glass sheen travels with the move.
End state: the C|L gap = GAP rect (≈380..520 x 520..1040) filled with glass, bright rims on both edges -> S05."""
from xk import box, r3
from kit import tx
from kit_b import LETTERS, letter, floor, gap_glass, rims, C_OPEN, L_OPEN, GAP_C, LY, LH

C_CX, C_CY = 145, 720          # C box centre (45..245 x 520..920)
START = {"scaleX": 1.45, "scaleY": 1.3, "x": 89, "y": 65}   # C mapped onto LETTER_C (90,520,300,520) = S03's last C
PUSH = {"scale": 1.3, "x": 185, "y": 60}        # gap (195..335 x 520..920) mapped onto GAP (≈380..520 x 520..1040)


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W26, W28, W29, W30, W31, W33, W35 = (S.W(i) for i in (26, 28, 29, 30, 31, 33, 35))
    # ---------------------------------------------------------------- back: floor + sign (camA = pull-back / drift, camB = push into gap)
    S.back.append(floor(f"{s}-floor"))
    inner = [gap_glass(f"{s}-glass")]
    for ch, x, w in LETTERS:
        inner.append(letter(f"{s}-{ch}", ch, x, w))
    inner.append(rims(f"{s}-rim"))
    S.back.append(f'<div class="abs" id="{s}-camA" style="{box(0, 0, 1080, 1920)}">'
                  f'<div class="abs" id="{s}-camB" style="{box(0, 0, 1080, 1920)}">' + "".join(inner) + "</div></div>")
    S.front.append(tx(f"{s}-lab", 70, 292, 600, "03 — WORD STAGE", size=30, weight=400))

    # ---------------------------------------------------------------- camera on the sign
    go = W30
    S.keys(f"#{s}-camA", [(t0, dict(START, transformOrigin=f"{C_CX}px {C_CY}px"), None),
                          (t0 + 0.5, {"scaleX": 1, "scaleY": 1, "x": 0, "y": 0}, "power3.out"),
                          (go, {"x": -24}, "sine.inOut"),
                          (W35 + 0.3, {"x": 0}, "power2.inOut")])
    S.keys(f"#{s}-camB", [(t0, {"scale": 1, "x": 0, "y": 0, "transformOrigin": f"{GAP_C[0]}px {GAP_C[1]}px"}, None),
                          (go, {"scale": 1}, "none"),
                          (W35 + 0.3, PUSH, "power2.inOut")])
    # the other letters rise out of the stage floor (C is already there = the hand-off object)
    for k, (ch, x, w) in enumerate(LETTERS[1:]):
        sel = f"#{s}-{ch}"
        S.init(sel, {"scaleY": 0, "transformOrigin": "50% 100%"})
        S.ft(sel, {"scaleY": 0}, {"scaleY": 1}, t0 + 0.12 + k * 0.055 + (0.02 if k % 2 else 0), 0.42, "back.out(1.3)")
    S.init(f"#{s}-floor", {"opacity": 0})
    S.ft(f"#{s}-floor", {"opacity": 0}, {"opacity": 1}, t0 + 0.05, 0.4, "power2.out")
    # "terbuka": C swings on its left hinge and slides left, L slides right on its rail
    S.init(f"#{s}-C", {"x": 0, "rotationY": 0, "transformOrigin": "0% 50%", "transformPerspective": 1200})
    S.ft(f"#{s}-C", {"x": 0, "rotationY": 0}, {"x": C_OPEN, "rotationY": -16}, W28 - 0.04, 0.55, "power3.inOut")
    S.ft(f"#{s}-L", {"x": 0, "rotationY": 0, "transformOrigin": "100% 50%", "transformPerspective": 1200},
         {"x": L_OPEN, "rotationY": 12}, W28 + 0.02, 0.55, "power3.inOut")
    # glass behind the gap + rims + travelling sheen ("bergerak mengikuti kamera")
    S.init(f"#{s}-glass", {"opacity": 0, "y": 40})
    S.ft(f"#{s}-glass", {"opacity": 0}, {"opacity": 1}, W28 + 0.12, 0.35, "power2.out")
    S.ft(f"#{s}-glass", {"y": 40}, {"y": -20}, go, W35 + 0.3 - go, "power2.inOut")
    S.init(f"#{s}-glass-band", {"y": LH - 60})
    S.ft(f"#{s}-glass-band", {"y": LH - 60}, {"y": 0}, W29, W35 + 0.4 - W29, "sine.inOut")
    for k in range(2):
        sel = f"#{s}-rim-r{k}"
        S.init(sel, {"opacity": 0, "scaleY": 0.1})
        S.ft(sel, {"opacity": 0, "scaleY": 0.1}, {"opacity": 1, "scaleY": 1}, W29 + k * 0.06, 0.32, "power3.out")
    S.init(f"#{s}-lab", {"opacity": 0, "y": 12})
    S.ft(f"#{s}-lab", {"opacity": 0, "y": 12}, {"opacity": 1, "y": 0}, t0 + 0.55, 0.3, "power2.out")
    S.ft(f"#{s}-lab", {"opacity": 1}, {"opacity": 0}, go, 0.3, "power2.in")

    # ---------------------------------------------------------------- mascot: arrives in front, looks up, gestures, the camera passes him
    S.mset("V", {"vis": 0}, t0)
    S.mset("V", {"vis": 1}, t0 + 0.1)
    stand = {"fx": 640, "fy": 1840, "h": 1000, "yaw": -14, "pitch": 5}
    S.mv([(t0 + 0.1, {"fx": 1250, "fy": 2120, "h": 1500, "yaw": -26, "pitch": 4}, None),
          (t0 + 0.65, stand, "power3.out"),
          (go, dict(stand, fx=600, yaw=-2), "sine.inOut"),
          (W33, dict(stand, fx=650, fy=1880, h=1080, yaw=6), "sine.inOut"),
          (W35 + 0.15, {"fx": 1520, "fy": 2350, "h": 1750, "yaw": 26, "pitch": 4}, "power2.in")])
    S.mset("V", {"vis": 0}, W35 + 0.16)
    S.act("head", [(t0 + 0.1, [-0.18, -0.3, 0.04], 0.4), (W26, [-0.2, -0.22, 0.02], 0.35), (W28 - 0.1, [-0.12, -0.42, 0.0], 0.3),
                   (W29, [-0.06, -0.26, 0.03], 0.35), (W31, [-0.08, -0.36, 0.0], 0.3), (W33, [0.0, 0.1, 0.0], 0.4)])
    S.act("armR", [(t0 + 0.1, "low", 0.3), (W28 - 0.16, "point", 0.3), (W29 + 0.2, "present", 0.35), (W31 + 0.3, "low", 0.4)])
    S.act("armL", [(t0 + 0.1, "low", 0.3), (W26 - 0.05, "explain", 0.3), (W28, "low", 0.35), (W33 - 0.1, "open", 0.3), (W35, "low", 0.4)])
    S.act("torso", [(t0 + 0.1, {"chest": [0.0, -0.1, 0.0]}, 0.4), (W28 - 0.05, {"chest": [0.03, -0.16, 0.0]}, 0.3), (W33, {}, 0.4)])
    S.act("root", [(t0 + 0.1, {"ry": -0.15}, 0.4), (W33, {"ry": 0.1}, 0.5)])
    # ---------------------------------------------------------------- sound
    S.fx(t0 + 0.2, "whoosh", 0.05)
    S.fx(W28, "click", 0.08)
    S.fx(W29 + 0.02, "sparkle", 0.04)
    S.fx(go + 0.1, "whoosh", 0.05)
