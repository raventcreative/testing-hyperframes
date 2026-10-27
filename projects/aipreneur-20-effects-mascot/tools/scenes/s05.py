"""S05 — 04 SNAP ZOOM (9.23–11.43)  VO: "dan kamera langsung menghantam close-up."
Opens on S04's viewfinder corners (VF) around the MED mascot; a thin focus reticle sits on the face. Slow creep
on "kamera langsung". "menghantam": anticipation pull-back 0.15 s -> 0.28 s push to a real close-up (the 3D camera
re-frames: figure 1470 px -> 2240 px, motion blur only during the push) -> 0.16 s settle with a tiny overshoot.
The corners snap inward, HERO APEX #1. Close-up holds through "close-up." with a head-tilt reaction.
Hand-off: the reticle shrinks beside his eye into a cyan disc at CHECK0 = S06's first check disc."""
from xk import box, r3, apex, CYAN
from kit import VF, CU, CHECK0, corner_frame

FACE_K = 0.597          # face height (u 0.585) / 0.98 -> face y = fy - FACE_K * h
F0 = "drop-shadow(0px 0px 0px rgba(0,208,254,0)) blur(0px)"
F1 = "drop-shadow(0px 0px 0px rgba(0,208,254,0)) blur(5px)"


def view(h, face_y, yaw=0, pitch=5, fx=540):
    return {"fx": fx, "fy": round(face_y + FACE_K * h, 1), "h": h, "yaw": yaw, "pitch": pitch}


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W26, W28, W29 = S.W(26), S.W(28), S.W(29)       # kamera 9.50, menghantam 10.16, close-up 10.70
    snap = W28
    vx, vy, vw, vh = VF
    vcx, vcy = vx + vw / 2, vy + vh / 2
    # ---------------------------------------------------------------- front: corners + reticle + end disc
    S.front.append(f'<div class="abs" id="{s}-vf" style="{box(0, 0, 1080, 1920)}">' + corner_frame(f"{s}-vf", vx, vy, vw, vh, arm=90, th=6) + "</div>")
    R = 150
    ticks = "".join(f'<div class="abs" style="{b}background:rgba(255,255,255,.9)"></div>' for b in (
        box(R / 2 - 1.5, -16, 3, 22), box(R / 2 - 1.5, R - 6, 3, 22), box(-16, R / 2 - 1.5, 22, 3), box(R - 6, R / 2 - 1.5, 22, 3)))
    S.front.append(f'<div class="abs" id="{s}-ret" style="{box(540 - R / 2, 922 - R / 2, R, R)}">'
                   f'<div class="abs" id="{s}-rring" style="left:0;top:0;width:{R}px;height:{R}px"><div class="abs" style="left:0;top:0;width:{R}px;height:{R}px;border-radius:50%;border:3px solid rgba(255,255,255,.85);'
                   f'box-shadow:0 0 10px rgba(0,208,254,.5)"></div>{ticks}</div>'
                   f'<div class="abs acrylic" id="{s}-disc" style="left:0;top:0;width:{R}px;height:{R}px;border-radius:50%;background:{CYAN};border:0"></div></div>')
    apex(S, S.front, f"{s}-ap", 540, 960, snap + 0.2, size=1100, sparks=10, seed=505, op=0.4)

    # ---------------------------------------------------------------- mascot: creep -> anticipation -> SNAP -> settle -> hold
    med = view(1470, 922)
    S.mv([(t0, med, None),
          (snap - 0.15, view(1540, 922, yaw=3), "sine.inOut"),           # slow creep on "kamera langsung"
          (snap, view(1430, 924, yaw=2), "power2.out"),                   # anticipation pull-back
          (snap + 0.28, view(2260, 958, yaw=-2, pitch=4), "power4.out"),  # the snap
          (snap + 0.44, dict(CU), "sine.inOut"),                          # settle (tiny overshoot back)
          (t1, view(2160, 960, yaw=-4, pitch=4), "sine.inOut")])          # held close-up, slow drift
    S.mx([(t0, {"filter": F0}, None), (snap, {"filter": F0}, "none"),
          (snap + 0.1, {"filter": F1}, "power2.in"), (snap + 0.3, {"filter": F0}, "power2.out")])

    # ---------------------------------------------------------------- HUD motion
    S.init(f"#{s}-vf", {"scale": 1, "opacity": 1, "transformOrigin": f"{vcx}px {vcy}px"})
    S.ft(f"#{s}-vf", {"scale": 1}, {"scale": 1.04}, snap - 0.15, 0.15, "power2.out")
    S.ft(f"#{s}-vf", {"scale": 1.04}, {"scale": 0.9}, snap, 0.22, "back.out(2.2)")
    S.ft(f"#{s}-vf", {"scale": 0.9, "opacity": 1}, {"scale": 0.94, "opacity": 0}, t1 - 0.34, 0.3, "power2.in")
    S.init(f"#{s}-ret", {"x": 0, "y": 0, "scale": 1, "opacity": 0})
    S.ft(f"#{s}-ret", {"opacity": 0, "scale": 1.3}, {"opacity": 1, "scale": 1}, t0 + 0.02, 0.24, "power3.out")
    S.ft(f"#{s}-ret", {"x": 0, "y": 0, "scale": 1}, {"x": 0, "y": 36, "scale": 0.62}, snap, 0.28, "power4.out")
    S.ft(f"#{s}-ret", {"scale": 0.62}, {"scale": 0.72}, snap + 0.28, 0.16, "sine.inOut")
    # hand-off: reticle travels beside the eye and becomes the cyan check disc (CHECK0)
    cx, cy, d = CHECK0
    S.ft(f"#{s}-ret", {"x": 0, "y": 36, "scale": 0.72}, {"x": cx - 540, "y": cy - 922, "scale": d / R}, t1 - 0.36, 0.32, "power3.inOut")
    S.init(f"#{s}-rring", {"opacity": 1})
    S.ft(f"#{s}-rring", {"opacity": 1}, {"opacity": 0}, t1 - 0.18, 0.14, "power1.in")
    S.init(f"#{s}-disc", {"opacity": 0})
    S.ft(f"#{s}-disc", {"opacity": 0}, {"opacity": 1}, t1 - 0.16, 0.12, "power2.out")

    # ---------------------------------------------------------------- acting: recoil on the hit, curious head tilt on "close-up."
    S.act("torso", [(t0 + 0.02, {}, 0.3), (snap - 0.04, {"chest": [-0.07, 0, 0], "spine": [-0.03, 0, 0]}, 0.16), (snap + 0.3, {"chest": [0.02, 0, 0]}, 0.3), (t1 - 0.2, {}, 0.3)])
    S.act("head", [(t0 + 0.02, [0, 0, 0], 0.3), (W26, [-0.03, 0.06, 0.02], 0.3), (snap - 0.04, [-0.08, 0, 0], 0.14),
                   (snap + 0.32, [0.04, 0.1, 0.13], 0.3), (W29 + 0.2, [0.02, -0.06, -0.05], 0.35), (t1 - 0.15, [0, 0.12, 0.04], 0.3)])
    S.act("armL", [(t0 + 0.02, "low", 0.3), (W26 - 0.1, "explain", 0.3), (snap - 0.05, "fist", 0.18), (snap + 0.45, "low", 0.4)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (snap - 0.05, "fist", 0.18), (snap + 0.45, "low", 0.4)])
    S.act("root", [(t0 + 0.02, {"y": 0, "ry": 0, "rz": 0}, 0.3)])
    S.fx(snap - 0.12, "whoosh", 0.06)
    S.fx(snap + 0.22, "click", 0.09)
    S.fx(t1 - 0.12, "pop", 0.05)
