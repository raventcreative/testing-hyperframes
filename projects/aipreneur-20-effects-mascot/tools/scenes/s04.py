"""S04 — 03 FRAME ESCAPE (8.20–9.23)  VO: "Dia keluar dari frame,"
Match cut from S03: the chat preview bubble becomes a physical navy-porcelain picture frame (glazed face, bevel,
sidewall thickness) holding the clipped live mascot (PREVIEW / PREVIEW_VIEW). "keluar": the frame tilts back on its
bottom edge and recedes while the clip releases top-first - head and shoulders come forward over the frame edge,
then the whole figure (real camera re-frame to MED, small weight hop, no fake walk). Contact shadow lands.
Hand-off: the receded frame dissolves into four viewfinder corners on VF = S05's opening state."""
from xk import box, r3, clip_rect, CLIP_NONE
from kit import PREVIEW, PREVIEW_VIEW, MED, VF, NO_FILTER, corner_frame
from kit_b import porcelain_frame


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W21, W22, W24 = S.W(21), S.W(22), S.W(24)          # Dia 8.28, keluar 8.46, frame 9.00
    x, y, w, h, r = PREVIEW
    S.persp_origin = (540, 980)
    # ---------------------------------------------------------------- back: frame + contact shadow
    S.back.append(f'<div class="abs cshadow" id="{s}-sh" style="{box(300, 1748, 480, 96)}"></div>')
    S.back.append(porcelain_frame(f"{s}-fr", x, y, w, h, r))
    # ---------------------------------------------------------------- front: viewfinder corners (S05 opening state)
    vx, vy, vw, vh = VF
    S.front.append(f'<div class="abs" id="{s}-vf" style="{box(0, 0, 1080, 1920)}">' + corner_frame(f"{s}-vf", vx, vy, vw, vh, arm=90, th=6) + "</div>")
    S.back.append(f'<div class="abs glowline" id="{s}-edge" style="{box(x - 40, y - 38, w + 80, 4)}"></div>')

    # ---------------------------------------------------------------- motion
    S.keys(f"#{s}-fr", [(t0, {"rotationX": 0, "scale": 1.0, "y": 0, "opacity": 1, "transformOrigin": "50% 100%"}, None),
                        (W22, {"scale": 0.985}, "sine.inOut"),
                        (W22 + 0.48, {"rotationX": 30, "scale": 0.84, "y": -24}, "power2.inOut"),
                        (t1 - 0.03, {"rotationX": 34, "scale": 0.8, "y": -40, "opacity": 0}, "power2.in")])
    # the frame's top edge flares as the head crosses it
    S.init(f"#{s}-edge", {"opacity": 0, "scaleX": 0.3})
    S.ft(f"#{s}-edge", {"opacity": 0, "scaleX": 0.3}, {"opacity": 1, "scaleX": 1}, W22 + 0.08, 0.14, "power2.out")
    S.ft(f"#{s}-edge", {"opacity": 1, "scaleX": 1}, {"opacity": 0, "scaleX": 1.2}, W22 + 0.24, 0.26, "power2.in")
    S.init(f"#{s}-sh", {"opacity": 0, "scale": 0.6})
    S.ft(f"#{s}-sh", {"opacity": 0, "scale": 0.6}, {"opacity": 0.9, "scale": 1}, W22 + 0.32, 0.3, "power2.out")
    cx, cy = vx + vw / 2, vy + vh / 2
    S.init(f"#{s}-vf", {"opacity": 0, "scale": 0.8, "transformOrigin": f"{cx}px {cy}px"})
    S.ft(f"#{s}-vf", {"opacity": 0, "scale": 0.8}, {"opacity": 1, "scale": 1}, t1 - 0.3, 0.28, "power3.out")

    # ---------------------------------------------------------------- mascot: clipped in the frame -> steps out
    S.mv([(t0, dict(PREVIEW_VIEW), None), (W22 - 0.04, dict(PREVIEW_VIEW), "none"),
          (W22 + 0.56, dict(MED), "power3.inOut"), (t1, dict(MED, yaw=4), "sine.out")])
    S.mc([(t0, {"clipPath": clip_rect(x, y, w, h, r)}, None),
          (W22, {"clipPath": clip_rect(x, y, w, h, r)}, "none"),
          (W22 + 0.26, {"clipPath": clip_rect(x - 120, -400, w + 240, y + h + 400, r)}, "power2.in"),
          (W22 + 0.52, {"clipPath": CLIP_NONE}, "power2.out")])
    S.mx([(t0, {"filter": NO_FILTER}, None)])
    # acting: lean in, small hop over the frame edge, arms open, settle
    S.act("torso", [(t0 + 0.02, {}, 0.3), (W22 - 0.06, {"chest": [0.09, 0, 0], "spine": [0.05, 0, 0]}, 0.25), (W24 - 0.05, {}, 0.35)])
    S.act("root", [(t0 + 0.02, {"y": 0, "ry": 0, "rz": 0}, 0.3), (W22 + 0.04, {"y": 0.025, "rz": -0.02}, 0.2), (W22 + 0.3, {"y": 0, "rz": 0}, 0.25)])
    S.act("armL", [(t0 + 0.02, "low", 0.3), (W22 - 0.04, "present", 0.3), (W24 - 0.02, "low", 0.4)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W22 - 0.02, "explain", 0.32), (W24, "low", 0.4)])
    S.act("head", [(t0 + 0.02, [-0.03, 0, 0], 0.3), (W22 + 0.05, [0.05, 0.06, -0.03], 0.3), (W24, [0, -0.04, 0.02], 0.35)])
    S.fx(W22 + 0.02, "whoosh", 0.06)
    S.fx(W22 + 0.36, "pop", 0.05)
    S.fx(t1 - 0.2, "click", 0.05)
