"""S04 — THE CAMERA MOTION RAIL (7.22–10.42)
VO: "sampai gerak kamera ternyata punya lapisan masing-masing."
A curved miniature dolly track lies on a porcelain stage floor (true 3D plane). A tiny camera on a dolly cart travels
along it while the viewer camera tracks with it: four suspended glass scene planes (background / midground /
subject / foreground) hang at different depths and slide past at different speeds (real perspective parallax).
"ternyata": the rail assembly rolls up and shows its engineered navy underside. "masing-masing": the four planes
separate into an exploded view, then align into one composed frame. End: the track winds itself onto a spool at
its near end and the camera pushes onto the spool (hand-off to S05)."""
import math
from xk import box, screw, shadow, apex, gear_svg, r3

SFX = [(9.24, "whoosh", 0.07), (9.72, "click", 0.10)]

# stage floor (lies in 3D: rotateX ~72deg about its centre)
FX, FY, FW, FH = 130, 1010, 820, 700
TILT = 72
# arc track in floor coordinates: quarter circle centred at (CX, CY), from far-left (-90deg) to near-right (0deg)
CX, CY, R = 120, 640, 560
A0, A1 = -88, 0
PLANES = [  # id, x offset, base z, open (exploded) x / z
    ("bg", 0, -380, -250, -560),
    ("mid", 0, -160, -90, -220),
    ("sub", 0, 40, 80, 120),
    ("fg", 0, 220, 240, 380),
]


def arc_pt(a_deg, r=R):
    a = math.radians(a_deg)
    return CX + r * math.cos(a), CY + r * math.sin(a)


def arc_path(r):
    x0, y0 = arc_pt(A0, r)
    x1, y1 = arc_pt(A1, r)
    return f"M{r3(x0)},{r3(y0)} A{r},{r} 0 0 1 {r3(x1)},{r3(y1)}", math.pi * r * (A1 - A0) / 180


def plane_inner(kind, w, h):
    if kind == "bg":
        return (f'<div class="abs" style="{box(0, 0, w, h)}border-radius:14px;background:linear-gradient(180deg,#e8f0fb,#cbdbf4)"></div>'
                f'<div class="abs" style="{box(w - 130, 50, 84, 84)}border-radius:50%;background:radial-gradient(circle at 40% 35%,#ffffff,#fbfcfe 50%,#e8f0fb)"></div>'
                + "".join(f'<div class="abs" style="{box(0, 40 + k * 46, w, 1)}background:rgba(41,75,119,.12)"></div>' for k in range(8)))
    if kind == "mid":
        return (f'<svg class="abs" style="left:0;top:0" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
                f'<path d="M0,{h} L0,{h - 140} L70,{h - 210} L140,{h - 150} L220,{h - 250} L300,{h - 160} L300,{h} Z" fill="#acc6e7"/>'
                f'<path d="M0,{h} L0,{h - 90} L90,{h - 150} L170,{h - 100} L250,{h - 170} L300,{h - 120} L300,{h} Z" fill="#3a6299"/></svg>')
    if kind == "sub":
        return (f'<div class="abs" style="{box(80, 130, 140, 190)}border-radius:16px;background:linear-gradient(150deg,#3a6299,#1c3354);box-shadow:0 14px 20px -8px rgba(28,51,84,.5)"></div>'
                f'<div class="abs" style="{box(158, 150, 44, 44)}border-radius:50%;background:radial-gradient(circle at 35% 30%,#e9fbf4,#9fd8c4)"></div>'
                f'<div class="abs" style="{box(100, 280, 70, 12)}border-radius:6px;background:#cbdbf4"></div>')
    return (f'<div class="abs" style="{box(30, h - 82, 200, 18)}border-radius:9px;background:#294b77"></div>'
            f'<div class="abs" style="{box(30, h - 54, 150, 14)}border-radius:7px;background:#cbdbf4"></div>'
            + "".join(f'<div class="corner {c}" style="left:{x}px;top:{y}px"></div>' for c, (x, y) in
                      (("tl", (14, 14)), ("tr", (w - 40, 14)), ("bl", (14, h - 40)), ("br", (w - 40, h - 40)))))


def build(S):
    s = S.id
    S.persp_origin = (590, 640)
    S.css.append(f"#{s}-persp {{ perspective: 1700px; }}")
    t0, t1 = S.t0, S.t1
    W14, W15, W16, W18, W19 = S.W(14), S.W(15), S.W(16), S.W(18), S.W(19)   # gerak 7.60 kamera 7.80 ternyata 8.26 lapisan 8.88 masing 9.24
    # ---------------- far plane: studio back wall, softbox (key light upper-left), shelf rails
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-560px) scale(1.3)">'
                 f'<div class="abs por-dim" style="{box(150, 420, 880, 1000)}border-radius:30px;opacity:.6"></div>'
                 f'<div class="abs" style="{box(190, 460, 300, 190)}border-radius:20px;background:linear-gradient(160deg,#ffffff,#f4f7fc);box-shadow:0 0 60px 20px rgba(255,255,255,.9),inset 0 0 0 4px #e3ebf7"></div>'
                 + "".join(f'<div class="abs" style="{box(210 + k * 28, 480, 2, 150)}background:rgba(172,198,231,.4)"></div>' for k in range(10))
                 + f'<div class="abs" style="{box(120, 1450, 940, 6)}border-radius:3px;background:rgba(172,198,231,.55)"></div></div>')
    # ---------------- floor (3D plane) with track, ties, trail, dolly, spool, underside truss
    p_in, L_in = arc_path(R - 18)
    p_out, L_out = arc_path(R + 18)
    p_mid, L_mid = arc_path(R)
    ties = []
    NT = 16
    for k in range(NT):
        a = A0 + (A1 - A0) * (k + 0.5) / NT
        x0, y0 = arc_pt(a, R - 34)
        x1, y1 = arc_pt(a, R + 34)
        ties.append(f'<line id="{s}-ti{k}" x1="{r3(x0)}" y1="{r3(y0)}" x2="{r3(x1)}" y2="{r3(y1)}" stroke="#ffffff" stroke-width="14" stroke-linecap="round"/>'
                    f'<line x1="{r3(x0)}" y1="{r3(y0)}" x2="{r3(x1)}" y2="{r3(y1)}" stroke="#acc6e7" stroke-width="3" stroke-linecap="round" transform="translate(2,3)"/>')
    track = (f'<svg class="abs" style="left:0;top:0;overflow:visible;transform:translateZ(2px)" width="{FW}" height="{FH}" viewBox="0 0 {FW} {FH}">'
             f'<path id="{s}-trail" d="{p_mid}" fill="none" stroke="#9fd8c4" stroke-width="5" stroke-dasharray="4 14" opacity=".9"/>'
             f'<g id="{s}-ties">{"".join(ties)}</g>'
             f'<path id="{s}-r1" d="{p_in}" fill="none" stroke="#1c3354" stroke-width="10" stroke-linecap="round" stroke-dasharray="{r3(L_in)} {r3(L_in)}"/>'
             f'<path id="{s}-r2" d="{p_out}" fill="none" stroke="#1c3354" stroke-width="10" stroke-linecap="round" stroke-dasharray="{r3(L_out)} {r3(L_out)}"/>'
             f'<path d="{p_in}" fill="none" stroke="#5d84b9" stroke-width="3" transform="translate(-1,-2)" id="{s}-r1h" stroke-dasharray="{r3(L_in)} {r3(L_in)}"/>'
             f'<path d="{p_out}" fill="none" stroke="#5d84b9" stroke-width="3" transform="translate(-1,-2)" id="{s}-r2h" stroke-dasharray="{r3(L_out)} {r3(L_out)}"/></svg>')
    floor_surface = (f'<div class="abs por" style="{box(0, 0, FW, FH)}border-radius:36px">'
                     + "".join(f'<div class="abs" style="{box(40, 40 + k * 62, FW - 80, 1.5)}background:rgba(41,75,119,.08)"></div>' for k in range(10))
                     + f'{screw(26, 26, 20, 12)}{screw(FW - 26, 26, -30, 12)}{screw(26, FH - 26, 50, 12)}{screw(FW - 26, FH - 26, 5, 12)}</div>')
    underside = (f'<div class="abs" style="{box(20, 20, FW - 40, FH - 40)}border-radius:30px;transform:translateZ(-18px);'
                 f'background:repeating-linear-gradient(45deg,#294b77 0 6px,#1c3354 6px 34px),linear-gradient(#1c3354,#1c3354);box-shadow:inset 0 0 0 6px #3a6299">'
                 f'<div class="abs" style="left:300px;top:240px;width:200px;height:200px">{gear_svg(s + "-ug", 200, 22)}</div></div>')
    # dolly: cart + tiny camera standing upright on the floor
    dolly = (f'<div class="abs p3" id="{s}-dolly" style="left:-40px;top:-30px;width:80px;height:60px">'
             f'<div class="abs" style="{box(0, 0, 80, 60)}border-radius:12px;background:linear-gradient(150deg,#ffffff,#cbdbf4);box-shadow:0 0 0 2px #acc6e7"></div>'
             f'<div class="abs p3" style="left:0;top:0;width:80px;height:60px;transform:translateZ(1px) rotateX(-{TILT}deg);transform-origin:50% 100%">'
             f'<div class="abs" style="{box(6, -26, 68, 74)}border-radius:10px;background:linear-gradient(150deg,#3a6299,#1c3354);box-shadow:0 6px 10px rgba(28,51,84,.4)"></div>'
             f'<div class="abs" style="{box(22, -14, 36, 36)}border-radius:50%;background:radial-gradient(circle at 40% 35%,#cbdbf4,#3a6299 60%,#1c3354);box-shadow:0 0 0 4px #e8f0fb"></div>'
             f'<div class="abs" id="{s}-glint" style="{box(28, -8, 12, 12)}border-radius:50%;background:#ffffff;box-shadow:0 0 14px 6px rgba(255,255,255,.95)"></div>'
             f'<div class="abs" style="{box(10, -40, 26, 14)}border-radius:5px;background:#e8f0fb;box-shadow:0 2px 3px rgba(28,51,84,.3)"></div>'
             f'<div class="led" style="left:56px;top:-36px;width:9px;height:9px"></div></div></div>')
    sx, sy = arc_pt(A1)
    spool = (f'<div class="abs p3" style="left:{r3(sx + 16)}px;top:{r3(sy - 4)}px;width:0;height:0">'
             f'<div class="abs p3" style="left:0;top:0;width:0;height:0;transform:rotateX(-{TILT}deg)">'
             f'<div class="abs" id="{s}-spool" style="left:-90px;top:-180px;width:180px;height:180px">'
             f'<div class="abs" style="{box(0, 0, 180, 180)}border-radius:50%;background:radial-gradient(circle at 40% 35%,#ffffff,#e3ebf7 55%,#acc6e7);box-shadow:0 0 0 6px #294b77,0 14px 22px rgba(28,51,84,.4)"></div>'
             f'<div class="abs" id="{s}-coil" style="{box(30, 30, 120, 120)}border-radius:50%;border:16px solid #1c3354;box-shadow:inset 0 0 0 6px #3a6299"></div>'
             + "".join(f'<div class="abs" style="{box(86, 14, 8, 152)}border-radius:4px;background:rgba(41,75,119,.55);transform:rotate({k * 60}deg)"></div>' for k in range(3))
             + f'<div class="abs" style="{box(70, 70, 40, 40)}border-radius:50%;background:radial-gradient(circle at 35% 30%,#5d84b9,#1c3354)"></div></div></div></div>')
    floor = (f'<div class="abs p3" id="{s}-floor" style="{box(FX, FY, FW, FH)}">{underside}{floor_surface}{track}{dolly}{spool}</div>')
    S.mid.append(shadow(FX - 40, FY + FH * 0.42, FW + 80, 160, 0.55, soft=True))
    S.mid.append(floor)
    # ---------------- suspended scene planes (cam space, different depths)
    PW_, PH_ = 330, 440
    for k, (nm, ox, z, _, _) in enumerate(PLANES):
        wires = (f'<div class="abs" style="{box(40, -90, 2, 90)}background:linear-gradient(180deg,rgba(41,75,119,0),rgba(41,75,119,.6))"></div>'
                 f'<div class="abs" style="{box(PW_ - 42, -90, 2, 90)}background:linear-gradient(180deg,rgba(41,75,119,0),rgba(41,75,119,.6))"></div>'
                 f'<div class="rivet" style="left:37px;top:-4px"></div><div class="rivet" style="left:{PW_ - 45}px;top:-4px"></div>')
        edge = ["rgba(58,98,153,.45)", "rgba(58,98,153,.55)", "rgba(41,75,119,.7)", "rgba(41,75,119,.8)"][k]
        S.mid.append(f'<div class="abs glass" id="{s}-p{k}" style="{box(590 - PW_ / 2, 610, PW_, PH_)}border-radius:16px;border:2px solid {edge};'
                     f'background:linear-gradient(135deg,rgba(255,255,255,.55),rgba(232,240,251,.35))">{plane_inner(nm, PW_, PH_)}{wires}'
                     f'<div class="abs" id="{s}-pe{k}" style="{box(-3, -3, PW_ + 2, PH_ + 2)}border-radius:17px;border:3px solid #ffffff;box-shadow:0 0 18px rgba(172,198,231,1)"></div></div>')
    # ---------------- near plane: blurred film strip + glass ring
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(280px) scale(.86)">'
                  f'<div class="abs" style="{box(940, 1330, 220, 70)}border-radius:10px;background:repeating-linear-gradient(90deg,#3a6299 0 22px,#cbdbf4 22px 30px);opacity:.75;filter:blur(5px)"></div>'
                  f'<div class="abs" style="{box(-40, 700, 170, 170)}border-radius:50%;border:12px solid rgba(255,255,255,.75);filter:blur(5px)"></div></div>')
    apex(S, S.near, f"{s}-ap", 590, 720, W19 + 0.04, size=760, sparks=8, seed=41, op=0.65)

    # ---------------- motion
    T_ALIGN = W19 + 0.42          # planes align into one frame
    T_WIND = 9.98                 # rail winds onto the spool
    # viewer camera: crane up from the rail, track with the dolly (parallax), square-on for the aligned frame, push to spool
    S.cam([(t0, {"z": 300, "x": -60, "y": 40, "rotationY": 6, "rotationX": -6}, None),
           (W14 + 0.1, {"z": 60, "x": 90, "y": 0, "rotationY": -20, "rotationX": 2}, "power3.out"),
           (W16, {"z": 40, "x": 40, "rotationY": -12, "rotationX": 3}, "sine.inOut"),
           (W19, {"z": 30, "x": -90, "rotationY": 16, "rotationX": 2}, "sine.inOut"),
           (T_ALIGN + 0.15, {"z": 20, "x": 0, "rotationY": 0, "rotationX": 0}, "power3.inOut"),
           (T_WIND, {"z": 40, "x": -20, "y": -20}, "sine.inOut"),
           (t1, {"z": 450, "x": -280, "y": -660, "rotationY": 0, "rotationX": 0}, "power3.in")])
    # floor: lying stage; rolls up on "ternyata" to show the engineered underside, then settles
    S.keys(f"#{s}-floor", [(t0, {"rotationX": TILT, "rotationZ": -4, "transformOrigin": "50% 50%"}, None),
                           (W16 - 0.08, {"rotationX": TILT, "rotationZ": 0}, "sine.inOut"),
                           (W16 + 0.36, {"rotationX": 122, "rotationZ": 6}, "power3.inOut"),
                           (W18 + 0.2, {"rotationX": TILT - 4, "rotationZ": 0}, "power3.inOut"),
                           (t1, {"rotationX": TILT - 2, "rotationZ": 2}, "sine.inOut")])
    # dolly travels the arc (far-left -> near-right), turning with the tangent
    pts = []
    N = 14
    ta, tb = t0 + 0.05, T_WIND - 0.1
    for k in range(N + 1):
        u = k / N
        e = u * u * (3 - 2 * u)                    # smooth start/stop along the track
        a = A0 + (A1 - A0) * (0.04 + 0.82 * e)
        x, y = arc_pt(a)
        pts.append((ta + (tb - ta) * u, {"x": r3(x), "y": r3(y), "rotation": r3(a + 90), "scale": 1.6}, "none"))
    pts[0] = (pts[0][0], pts[0][1], None)
    S.keys(f"#{s}-dolly", pts)
    # trail fills behind the dolly
    S.init(f"#{s}-trail", {"strokeDashoffset": 0, "opacity": 0})
    S.ft(f"#{s}-trail", {"opacity": 0}, {"opacity": 0.9}, ta, 0.4, "power1.out")
    # lens glint on "kamera"
    S.init(f"#{s}-glint", {"opacity": 0, "scale": 0.3})
    S.ft(f"#{s}-glint", {"opacity": 0, "scale": 0.3}, {"opacity": 1, "scale": 1.4}, W15 - 0.04, 0.14, "power2.out")
    S.ft(f"#{s}-glint", {"opacity": 1, "scale": 1.4}, {"opacity": 0, "scale": 0.5}, W15 + 0.12, 0.35, "power2.in")
    # underside gear turns while it is visible
    S.init(f"#{s}-ug", {"rotation": 0, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-ug", {"rotation": 0}, {"rotation": 160}, W16, 0.9, "power2.inOut")
    # planes: hang at their depths, drift; edge-glow on "lapisan"; explode on "masing-masing"; align into one frame
    for k, (nm, ox, z, ex, ez) in enumerate(PLANES):
        pid = f"#{s}-p{k}"
        base = {"x": ox + (k - 1.5) * 64, "y": (k - 1.5) * -6, "z": z, "rotationY": 0, "opacity": 1}
        S.init(pid, base)
        drift = dict(base, x=base["x"] + (k - 1.5) * 8, y=base["y"] - 8)
        S.ft(pid, base, drift, t0, W19 - 0.06 - t0, "sine.inOut")
        exploded = {"x": ex, "y": -20 + k * 14, "z": ez, "rotationY": -16 + k * 6}
        S.ft(pid, drift, exploded, W19 - 0.06, 0.34, "expo.out")
        aligned = {"x": 0, "y": 0, "z": -40 + k * 34, "rotationY": 0}
        S.ft(pid, exploded, aligned, T_ALIGN - 0.22, 0.32, "power4.inOut")
        S.ft(pid, aligned, dict(aligned, opacity=0, y=-30), T_WIND + 0.05, 0.3, "power2.in")
        S.init(f"#{s}-pe{k}", {"opacity": 0})
        S.ft(f"#{s}-pe{k}", {"opacity": 0}, {"opacity": 0.9}, W18 - 0.02 + k * 0.06, 0.14, "power2.out")
        S.ft(f"#{s}-pe{k}", {"opacity": 0.9}, {"opacity": 0}, W18 + 0.2 + k * 0.06, 0.35, "power2.in")
        S.ft(f"#{s}-pe{k}", {"opacity": 0}, {"opacity": 0.8}, T_ALIGN + 0.08, 0.1, "power2.out")
        S.ft(f"#{s}-pe{k}", {"opacity": 0.8}, {"opacity": 0}, T_ALIGN + 0.18, 0.4, "power2.in")
    # the rail winds onto the spool: rails + highlights retract toward the near end, ties drop out in order
    for rid, L in (("r1", L_in), ("r2", L_out), ("r1h", L_in), ("r2h", L_out)):
        S.ft(f"#{s}-{rid}", {"strokeDashoffset": 0}, {"strokeDashoffset": r3(-L * 0.97)}, T_WIND, t1 - T_WIND - 0.02, "power2.in")
    S.ft(f"#{s}-trail", {"opacity": 0.9}, {"opacity": 0}, T_WIND, 0.2, "power1.in")
    for k in range(NT):
        S.init(f"#{s}-ti{k}", {"opacity": 1})
        S.ft(f"#{s}-ti{k}", {"opacity": 1}, {"opacity": 0}, T_WIND + 0.02 * k, 0.12, "power1.in")
    S.init(f"#{s}-spool", {"rotation": 0, "scale": 0.85})
    S.ft(f"#{s}-spool", {"rotation": 0, "scale": 0.85}, {"rotation": 30, "scale": 0.95}, t0, T_WIND - t0, "sine.inOut")
    S.ft(f"#{s}-spool", {"rotation": 30, "scale": 0.95}, {"rotation": 420, "scale": 1.12}, T_WIND, t1 - T_WIND, "power2.in")
    S.init(f"#{s}-coil", {"scale": 0.5})
    S.ft(f"#{s}-coil", {"scale": 0.5}, {"scale": 1.0}, T_WIND, t1 - T_WIND, "power2.in")
