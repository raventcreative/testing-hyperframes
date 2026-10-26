"""S02 — THE X-RAY REVEAL (3.24–5.18)  VO: "Lihat. Layarnya kebuka."
Continues S01's pinned layer stack of our Hypit Reel. "Lihat": the camera pulls back while the phone turns toward
us and the rods withdraw. "Layarnya": the glass swings away on its left hinge. "kebuka": the Reel's layers fan open
around their left edge like pages (background, hero machine, host, caption, app UI), each edge lights in turn, apex.
Hand-off: the caption layer ("Namanya Hypit,") swings square-on and flies to camera, whitening, into S03's plate."""
from xk import WORDS, box, shadow, apex, r3
from kit_reel import phone, PX, PY, PW, PH, SW, SH, BZ

SFX = [(WORDS[7]["start"], "whoosh", 0.06), (WORDS[8]["start"], "click", 0.08), (WORDS[9]["start"], "sparkle", 0.07), (4.98, "whoosh", 0.06)]
Z1 = {"bg": 0, "scene": 70, "mascot": 140, "cap": 210, "ui": 260}        # S01's end state
FAN = {"bg": (0, 0), "scene": (-34, 190), "mascot": (-68, 380), "cap": (-102, 570), "ui": (-128, 720)}   # y lift, z (exploded cascade)


def build(S):
    s = S.id
    S.persp_origin = (575, 860)
    W7, W8, W9 = S.W(7), S.W(8), S.W(9)              # Lihat 3.34, Layarnya 4.04, kebuka 4.38
    t0, t1 = S.t0, S.t1
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(250, 240, 680, 1240)}border-radius:340px 340px 40px 40px;opacity:.5"></div>'
                 f'<div class="abs" style="{box(300, 300, 580, 1150)}border-radius:290px 290px 30px 30px;border:2px solid rgba(255,255,255,.8)"></div>'
                 + "".join(f'<div class="abs" style="{box(x, y, d, d)}border-radius:50%;opacity:.6;filter:blur(7px);background:radial-gradient(circle at 35% 30%,#fff,#e8f0fb 45%,#acc6e7)"></div>'
                           for (x, y, d) in ((120, 700, 90), (930, 640, 60), (860, 1360, 110))) + "</div>")
    S.mid.append(shadow(PX + 40, PY + PH - 10, PW + 80, 90, 0.8, id_=f"{s}-sh"))
    S.mid.append(f'<div class="abs p3" id="{s}-ph" style="{box(PX, PY, PW, PH)}">{phone(s, video=False)}</div>')
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(-60, 560, 200, 200)}border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(6px)"></div></div>')
    apex(S, S.near, f"{s}-ap", 620, 860, W9 + 0.06, size=900, sparks=12, seed=202, op=0.6)

    # ------------------------------------------------------------------ motion
    S.cam([(t0, {"z": 300, "x": 60, "y": 30, "rotationX": 0, "rotationY": 0}, None),
           (W7 + 0.5, {"z": 0, "x": -40, "y": 0}, "power3.out"),
           (W9, {"z": -60, "x": -90, "y": 30}, "sine.inOut"),
           (W9 + 0.5, {"z": -140, "x": -150, "y": 40}, "power3.out"),
           (t1, {"z": 260, "x": -260, "y": 10}, "power3.in")])
    S.keys(f"#{s}-ph", [(t0, {"rotationY": 40, "rotationX": 10, "transformOrigin": "50% 60%"}, None),
                        (W7 + 0.55, {"rotationY": 50, "rotationX": 12}, "power3.inOut"),
                        (t1, {"rotationY": 54, "rotationX": 12}, "sine.inOut")])
    # rods withdraw on "Lihat"
    for k in range(4):
        sel = f"#{s}-rod{k}"
        S.init(sel, {"z": -30, "opacity": 1})
        S.ft(sel, {"z": -30, "opacity": 1}, {"z": -340, "opacity": 0}, W7 + 0.1 + k * 0.04, 0.32, "power3.in")
    # glass: hovering at S01's height, then swings open on its left hinge ("Layarnya")
    S.init(f"#{s}-glass", {"z": 310, "rotationY": 0, "opacity": 1, "transformOrigin": "100% 50%"})
    S.ft(f"#{s}-glass", {"z": 310, "rotationY": 0}, {"z": 330, "rotationY": 112}, W8 - 0.04, 0.42, "power3.inOut")
    S.ft(f"#{s}-glass", {"opacity": 1}, {"opacity": 0}, W8 + 0.3, 0.16, "power1.in")
    S.init(f"#{s}-gsheen", {"x": 0, "rotation": 18})
    S.ft(f"#{s}-gsheen", {"x": 0, "rotation": 18}, {"x": SW + 420, "rotation": 18}, W8, 0.4, "power2.inOut")
    # layers: settle from S01's stack, then fan open like pages ("kebuka")
    for k, (name, z) in enumerate(Z1.items()):
        sel = f"#{s}-L{name}"
        ry, fz = FAN[name]
        S.init(sel, {"z": z, "y": 0})
        S.ft(sel, {"z": z, "y": 0}, {"z": z * 0.5, "y": 0}, W7 + 0.1, 0.5, "power2.inOut")
        S.ft(sel, {"z": z * 0.5, "y": 0}, {"z": fz, "y": ry}, W9 - 0.06 + k * 0.04, 0.6, "back.out(1.4)")
    for k, name in enumerate(("bg", "scene", "mascot", "cap")):
        sel = f"#{s}-E{name}"
        S.init(sel, {"opacity": 0.35})
        S.ft(sel, {"opacity": 0.35}, {"opacity": 1}, W9 + 0.1 + k * 0.07, 0.14, "power2.out")
        S.ft(sel, {"opacity": 1}, {"opacity": 0.55}, W9 + 0.4 + k * 0.07, 0.3, "power2.inOut")
    # hand-off: the caption layer swings square-on and flies at the camera; the frame whitens into S03's plate
    S.ft(f"#{s}-Lcap", {"rotationY": 0, "scale": 1}, {"rotationY": -54, "scale": 1.25}, 4.98, 0.2, "power3.in")
    for nm in "tblr":
        S.init(f"#{s}-seam{nm}", {"opacity": 0})
    S.init(f"#{s}-prog", {"scaleX": 0.26, "transformOrigin": "0% 50%"})
