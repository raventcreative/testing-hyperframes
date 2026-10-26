"""S01 — THE IMPOSSIBLE OBJECT (0.00–3.24)  VO: "Gila, satu Reels bisa dibongkar jadi mesin."
A porcelain phone plays our own Hypit Reel (real footage of the Reel we made, with its 3D host). On "dibongkar" the
video freezes on the exact frame the layers were rendered from and the screen comes apart: background, hero machine,
host and caption separate along Z (the Reel's real build layers), the glass lifts, the phone turns to show the
depth. On "mesin" four navy rods slide through the layer corners and pin the stack together like a machine.
The camera pushes into the stack (match cut to S02, same stack, closer)."""
from xk import WORDS, box, shadow, apex, r3
from kit_reel import phone, PX, PY, PW, PH, SW, SH, BZ

SFX = [(WORDS[4]["start"], "click", 0.12), (WORDS[4]["start"] + 0.04, "sparkle", 0.06), (WORDS[6]["start"], "key", 0.07), (3.0, "whoosh", 0.06)]
Z1 = {"bg": 0, "scene": 70, "mascot": 140, "cap": 210, "ui": 260}     # separation after "dibongkar"


def build(S):
    s = S.id
    S.persp_origin = (575, 860)
    W4, W6 = S.W(4), S.W(6)                                  # dibongkar 1.88, mesin 2.56
    t1 = S.t1
    # far plane: soft arch + bokeh discs (REF-H)
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(250, 240, 680, 1240)}border-radius:340px 340px 40px 40px;opacity:.5"></div>'
                 f'<div class="abs" style="{box(300, 300, 580, 1150)}border-radius:290px 290px 30px 30px;border:2px solid rgba(255,255,255,.8)"></div>'
                 + "".join(f'<div class="abs" style="{box(x, y, d, d)}border-radius:50%;opacity:.6;filter:blur(7px);background:radial-gradient(circle at 35% 30%,#fff,#e8f0fb 45%,#acc6e7)"></div>'
                           for (x, y, d) in ((140, 620, 80), (900, 760, 60), (820, 1320, 100), (200, 1180, 54))) + "</div>")
    S.mid.append(shadow(PX + 40, PY + PH - 10, PW + 40, 90, 0.85, id_=f"{s}-sh"))
    S.mid.append(f'<div class="abs p3" id="{s}-ph" style="{box(PX, PY, PW, PH)}">{phone(s, video=True)}</div>')
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(930, 520, 170, 170)}border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"></div>'
                  f'<div class="abs" style="{box(-40, 1470, 300, 24)}border-radius:12px;background:linear-gradient(180deg,#fff,#cbdbf4);filter:blur(4px);opacity:.9"></div></div>')
    apex(S, S.near, f"{s}-ap", 590, 900, W4 + 0.02, size=760, sparks=10, seed=101, op=0.7)

    # ------------------------------------------------------------------ motion
    S.cam([(0.0, {"z": 0, "x": 0, "y": 0, "rotationX": 0, "rotationY": 0}, None),
           (W4 - 0.06, {"z": 120}, "sine.inOut"),
           (W6 + 0.2, {"z": 150, "x": 40}, "power2.out"),
           (t1, {"z": 380, "x": 60, "y": 30}, "power3.in")])
    S.keys(f"#{s}-ph", [(0.0, {"rotationY": -10, "rotationX": 5, "y": 24, "transformOrigin": "50% 60%"}, None),
                        (0.5, {"y": 0}, "power3.out"),
                        (W4, {"rotationY": 8, "rotationX": 4}, "sine.inOut"),
                        (W4 + 0.55, {"rotationY": 34, "rotationX": 9}, "power3.out"),
                        (t1, {"rotationY": 40, "rotationX": 10}, "sine.inOut")])
    # Reel playing: progress bar runs, then freezes on the cut frame
    S.init(f"#{s}-prog", {"scaleX": 0.18, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-prog", {"scaleX": 0.18}, {"scaleX": 0.26}, 0.0, W4, "none")
    S.init(f"#{s}-vid", {"opacity": 1})
    S.tset(f"#{s}-vid", {"opacity": 0}, W4)               # freeze -> the layers (same frame) take over
    # seams: shimmer (anticipation) then flare on the break
    for nm in "tblr":
        sel = f"#{s}-seam{nm}"
        S.init(sel, {"opacity": 0})
        S.ft(sel, {"opacity": 0}, {"opacity": 0.5}, W4 - 0.45, 0.12, "power1.out")
        S.ft(sel, {"opacity": 0.5}, {"opacity": 0.2}, W4 - 0.33, 0.2, "power1.in")
        S.ft(sel, {"opacity": 0.2}, {"opacity": 1}, W4 - 0.07, 0.07, "power2.in")
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, W4 + 0.05, 0.5, "power2.out")
    # the screen comes apart along Z (overshoot + settle), glass lifts in front
    for name, z in Z1.items():
        sel = f"#{s}-L{name}"
        S.init(sel, {"z": 0})
        S.ft(sel, {"z": 0}, {"z": z}, W4, 0.5, "back.out(1.7)")
    S.init(f"#{s}-glass", {"z": 2, "opacity": 1})
    S.ft(f"#{s}-glass", {"z": 2}, {"z": 310}, W4, 0.5, "back.out(1.6)")
    S.init(f"#{s}-gsheen", {"x": 0, "rotation": 18})
    S.ft(f"#{s}-gsheen", {"x": 0, "rotation": 18}, {"x": SW + 420, "rotation": 18}, W4 + 0.1, 0.6, "power2.inOut")
    # layer edges light in sequence
    for k, name in enumerate(("bg", "scene", "mascot", "cap")):
        sel = f"#{s}-E{name}"
        S.init(sel, {"opacity": 0})
        S.ft(sel, {"opacity": 0}, {"opacity": 1}, W4 + 0.18 + k * 0.08, 0.16, "power2.out")
        S.ft(sel, {"opacity": 1}, {"opacity": 0.35}, W4 + 0.5 + k * 0.08, 0.4, "power2.inOut")
    # "mesin": rods slide through the stack corners and pin it
    for k in range(4):
        sel = f"#{s}-rod{k}"
        S.init(sel, {"z": -320, "opacity": 0})
        S.ft(sel, {"z": -320, "opacity": 0}, {"z": -30, "opacity": 1}, W6 - 0.12 + k * 0.05, 0.32, "power4.out")
    S.ft(f"#{s}-sh", {"scaleX": 1, "opacity": 0.85}, {"scaleX": 1.12, "opacity": 0.7}, W4, 0.6, "power2.out")
