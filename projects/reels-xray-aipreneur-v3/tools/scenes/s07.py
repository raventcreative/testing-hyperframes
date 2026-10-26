"""S07 — HYPERFRAMES CONSTRUCTION (16.72–18.32)  VO: "HyperFrames nyusun scene,"
The round production stage revealed at the end of S06. Support rods rise, a 9:16 frame assembles piece by
piece and a miniature scene grows inside it from layered paper / glass / porcelain parts; the last part locks
on "scene". The stage's drive gear (right edge) then lifts and grows to hero centre -> S08's timing wheel."""
import math
from xk import box, screw, shadow, apex, gear_svg, r3
from kit_b import backdrop, near_blur, engrave, gear_side

SFX = [(16.85, "whoosh", 0.06), (17.76, "pop", 0.1)]

FX0, FY0, FW, FH = 440, 470, 300, 470      # the 9:16 frame being assembled


def build(S):
    s = S.id
    S.persp_origin = (590, 600)
    W37, W38, W39 = S.W(37), S.W(38), S.W(39)      # HyperFrames 16.82, nyusun 17.42, scene 17.76
    end = S.t1
    backdrop(S, seed=7)
    g = []
    # stage (same geometry as the stage revealed in S06)
    g.append(shadow(160, 1080, 860, 120, 0.9))
    g.append(f'<div class="abs" style="{box(230, 1010, 720, 130)}border-radius:0 0 360px 360px / 0 0 64px 64px;background:linear-gradient(90deg,#3a6299,#294b77 45%,#1c3354)"></div>')
    g.append(engrave(f"{s}-lab", "HyperFrames", 230, 1080, 24, w=720))
    g.append(f'<div class="abs" style="{box(230, 900, 720, 170)}border-radius:50%;background:radial-gradient(ellipse at 40% 35%,#ffffff,#eef3fa 55%,#d3dff0);box-shadow:inset 0 -4px 8px rgba(172,198,231,.7)"></div>')
    g.append(f'<div class="abs" style="{box(340, 926, 500, 118)}border-radius:50%;border:2px solid rgba(58,98,153,.35)"></div>')
    for k in range(25):  # rim tick marks on the front half of the ellipse
        a = math.pi * (k / 24)
        x, y = 590 + 352 * math.cos(a), 985 + 80 * math.sin(a)
        g.append(f'<div class="abs" style="{box(x - 1, y - 5, 2, 10 if k % 4 else 16)}background:rgba(41,75,119,.35)"></div>')
    # contact shadow of the frame on the stage
    g.append(shadow(430, 950, 320, 50, 0.8, id_=f"{s}-fsh"))
    # support rods
    for k, x in enumerate((452, 520, 660, 728)):
        g.append(f'<div class="abs" id="{s}-rod{k}" style="{box(x - 6, 560, 12, 420)}border-radius:6px;background:linear-gradient(90deg,#c9d8ee,#ffffff 35%,#dbe6f6 65%,#9fb6d6)"></div>')
        g.append(f'<div class="rivet" style="left:{x - 4}px;top:{970}px"></div>')
    # frame pieces
    pieces = {"ft": box(FX0, FY0, FW, 20), "fb": box(FX0, FY0 + FH - 20, FW, 20), "fl": box(FX0, FY0, 20, FH), "fr": box(FX0 + FW - 20, FY0, 20, FH)}
    # miniature scene parts inside the frame (layered)
    inner = [("p0", box(FX0 + 30, FY0 + 40, FW - 60, 240), "border-radius:12px;background:linear-gradient(150deg,#3a6299,#1c3354);box-shadow:0 10px 16px -8px rgba(28,51,84,.5)"),
             ("p1", box(FX0 + 60, FY0 + 170, 180, 130), "border-radius:12px;background:linear-gradient(160deg,#ffffff,#e6edf8);box-shadow:0 10px 18px -8px rgba(28,51,84,.45)"),
             ("p2", box(FX0 + 74, FY0 + 330, 150, 14), "border-radius:7px;background:#294b77"),
             ("p3", box(FX0 + 74, FY0 + 356, 110, 12), "border-radius:6px;background:#acc6e7"),
             ("p4", box(FX0 + 74, FY0 + 384, 60, 22), "border-radius:11px;background:#9fd8c4"),
             ("p5", box(FX0 + 180, FY0 + 70, 70, 70), "border-radius:50%;background:radial-gradient(circle at 35% 30%,#e9fbf4,#9fd8c4);box-shadow:0 8px 12px -6px rgba(28,51,84,.45)")]
    g.append(f'<div class="abs" id="{s}-back" style="{box(FX0 + 10, FY0 + 10, FW - 20, FH - 20)}border-radius:8px;background:linear-gradient(170deg,#fbfcfe,#e6edf8)"></div>')
    for nm, b, css in inner:
        g.append(f'<div class="abs" id="{s}-{nm}" style="{b}{css}"></div>')
    for nm, b in pieces.items():
        g.append(f'<div class="abs por" id="{s}-{nm}" style="{b}border-radius:8px"></div>')
    g.append(screw(FX0 + 10, FY0 + 10, 30, 10) + screw(FX0 + FW - 10, FY0 + 10, -20, 10) + screw(FX0 + 10, FY0 + FH - 10, 70, 10) + screw(FX0 + FW - 10, FY0 + FH - 10, 10, 10))
    S.mid.append(f'<div class="abs" id="{s}-grp" style="{box(0, 0, 1080, 1920)}">{"".join(g)}</div>')
    # drive gear at the stage's right edge (the same 560 px gear as S08's wheel, shown at 0.3 scale)
    S.mid.append(f'<div class="abs" id="{s}-gw" style="{box(870 - 280, 1060 - 280, 560, 560)}">{gear_side(s + "-gside", 560, 40, 10, 14)}{gear_svg(s + "-gear", 560, 40)}</div>')
    near_blur(S, [(f"{s}-n1", -50, 560, 160, 160, "border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"),
                  (f"{s}-n2", 880, 1400, 260, 28, "border-radius:14px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px)")])
    apex(S, S.near, f"{s}-ap", 590, 700, W39, size=420, ring=True, sparks=5, seed=11, op=0.7)

    # ================================================================ motion
    S.cam([(S.t0, {"z": 170, "y": -40, "rotationY": -4}, None),
           (W37 + 0.45, {"z": 0, "y": 0, "rotationY": -1}, "expo.out"),
           (end, {"z": 30, "rotationY": 3}, "sine.inOut")])
    for k in range(4):
        S.init(f"#{s}-rod{k}", {"scaleY": 0, "transformOrigin": "50% 100%"})
        S.ft(f"#{s}-rod{k}", {"scaleY": 0}, {"scaleY": 1}, W37 + 0.02 + k * 0.06, 0.38, "power3.out")
    FROM = {"ft": {"y": -150, "rotation": -10}, "fb": {"y": 140, "rotation": 8}, "fl": {"x": -170, "rotation": -6}, "fr": {"x": 170, "rotation": 6}}
    for k, (nm, frm) in enumerate(FROM.items()):
        st = dict(frm, opacity=0)
        S.init(f"#{s}-{nm}", st)
        zero = {key: 0 for key in frm}
        S.ft(f"#{s}-{nm}", st, dict(zero, opacity=1), W37 + 0.2 + k * 0.09, 0.36, "power3.out")
    S.init(f"#{s}-back", {"opacity": 0, "scale": 0.9})
    S.ft(f"#{s}-back", {"opacity": 0, "scale": 0.9}, {"opacity": 1, "scale": 1}, W37 + 0.5, 0.3, "power2.out")
    OFF = [(0, 70), (-60, 40), (-80, 0), (-80, 0), (-60, 0), (60, -60)]
    for k, (nm, _, _) in enumerate(inner):
        dx, dy = OFF[k]
        st_ = W38 - 0.05 + k * 0.07 if k < 5 else W39 - 0.18
        S.init(f"#{s}-{nm}", {"x": dx, "y": dy, "opacity": 0, "scale": 0.7})
        S.ft(f"#{s}-{nm}", {"x": dx, "y": dy, "opacity": 0, "scale": 0.7}, {"x": 0, "y": 0, "opacity": 1, "scale": 1}, st_, 0.24 if k < 5 else 0.18, "power3.out" if k < 5 else "back.out(2.6)")
    S.init(f"#{s}-fsh", {"opacity": 0.3, "scaleX": 0.8})
    S.ft(f"#{s}-fsh", {"opacity": 0.3, "scaleX": 0.8}, {"opacity": 1, "scaleX": 1}, W37 + 0.2, W39 - W37, "power2.inOut")
    # gear: turns the stage the whole time; then detaches and grows into the timing wheel (rotation ends on a tooth multiple)
    S.init(f"#{s}-gw", {"scale": 0.3, "x": 0, "y": 0, "rotation": 0, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-gw", {"rotation": 0}, {"rotation": 180}, S.t0, end - S.t0, "none")
    S.ft(f"#{s}-gw", {"scale": 0.3, "x": 0, "y": 0}, {"scale": 1, "x": -280, "y": -130}, end - 0.36, 0.36, "power3.inOut")
    S.init(f"#{s}-grp", {"opacity": 1, "scale": 1, "transformOrigin": "590px 900px"})
    S.ft(f"#{s}-grp", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.86}, end - 0.34, 0.3, "power2.in")
