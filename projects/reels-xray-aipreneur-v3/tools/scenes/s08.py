"""S08 — GSAP MOTION ENGINE (18.32–20.22)  VO: "GSAP ngatur geraknya,"
The timing wheel (S07's gear, same size/position). Keyframe pins pop onto it on "GSAP", a fixed pointer snaps
pin to pin, then the wheel accelerates and decelerates and stops exactly on "geraknya" (a pin under the
pointer). A small card rides a physical easing rail in sync, and a glass graph plate traces the same curve.
End: pins retract, pointer and rail clear, leaving the bare wheel = S09's sprocket drum."""
import math
from xk import box, screw, shadow, apex, gear_svg, r3
from kit_b import backdrop, near_blur, engrave, along, bezier_d, ease_io, gear_side

SFX = [(18.45, "key", 0.08), (19.44, "click", 0.14)]

CX, CY, SZ = 590, 930, 560
RAIL = ((440, 1250), (640, 1270), (760, 1000), (1000, 1030))


def build(S):
    s = S.id
    S.persp_origin = (590, 640)
    W40, W41, W42 = S.W(40), S.W(41), S.W(42)     # GSAP 18.42, ngatur 19.12, geraknya 19.44
    end = S.t1
    backdrop(S, seed=8)
    S.mid.append(shadow(CX - 330, CY + 230, 700, 120, 0.7, soft=True))
    # wheel + keyframe pins (rotate together)
    pins = ""
    for k in range(8):
        a = math.radians(-90 + 45 * k)
        px, py = SZ / 2 + 192 * math.cos(a), SZ / 2 + 192 * math.sin(a)
        pins += (f'<div class="abs" id="{s}-pin{k}" style="{box(px - 13, py - 13, 26, 26)}border-radius:50%;'
                 f'background:linear-gradient(150deg,#3a6299,#1c3354);box-shadow:0 0 0 4px #ffffff,0 4px 6px rgba(28,51,84,.4)"></div>')
    ring = f'<div class="abs" id="{s}-ring" style="{box(SZ / 2 - 192, SZ / 2 - 192, 384, 384)}border-radius:50%;border:2px dashed rgba(58,98,153,.4)"></div>'
    S.mid.append(f'<div class="abs" id="{s}-wheel" style="{box(CX - SZ / 2, CY - SZ / 2, SZ, SZ)}">{gear_side(s + "-gside", SZ, 40, 10, 14)}{gear_svg(s + "-gear", SZ, 40)}{ring}{pins}</div>')
    # fixed hub cap with the engraved label
    S.mid.append(f'<div class="abs por" id="{s}-cap" style="{box(CX - 66, CY - 66, 132, 132)}border-radius:50%"><div class="abs" style="left:0;top:46px;width:132px;text-align:center;font:900 32px Montserrat;letter-spacing:.04em;color:#294b77">GSAP</div></div>')
    # pointer on a bracket above the pin ring
    S.mid.append(f'<div class="abs" id="{s}-ptr" style="{box(CX - 40, 560, 80, 200)}">'
                 f'<div class="abs por" style="{box(0, 0, 80, 56)}border-radius:14px">{screw(18, 28, 30, 10)}{screw(62, 28, -40, 10)}</div>'
                 f'<div class="abs" id="{s}-ndl" style="{box(34, 40, 12, 140)}">'
                 f'<div class="abs" style="{box(0, 0, 12, 120)}border-radius:6px;background:linear-gradient(90deg,#3a6299,#1c3354)"></div>'
                 f'<div class="abs" style="{box(-6, 112, 24, 24)}border-radius:4px;background:#1c3354;transform:rotate(45deg)"></div></div></div>')
    # easing rail (physical), card riding it
    S.mid.append(f'<svg class="abs" id="{s}-rail" style="{box(0, 0, 1080, 1920)}overflow:visible" viewBox="0 0 1080 1920">'
                 f'<path d="{bezier_d(RAIL)}" fill="none" stroke="#acc6e7" stroke-width="22" stroke-linecap="round"/>'
                 f'<path d="{bezier_d(RAIL)}" fill="none" stroke="#ffffff" stroke-width="14" stroke-linecap="round"/>'
                 f'<path d="{bezier_d(RAIL)}" fill="none" stroke="#3a6299" stroke-width="2" stroke-dasharray="2 22" stroke-linecap="round"/></svg>')
    S.mid.append(f'<div class="abs por" id="{s}-card" style="{box(RAIL[0][0] - 50, RAIL[0][1] - 66, 100, 66)}border-radius:12px">'
                 f'<div class="abs" style="{box(14, 14, 50, 10)}border-radius:5px;background:#294b77"></div>'
                 f'<div class="abs" style="{box(14, 32, 72, 8)}border-radius:4px;background:#cbdbf4"></div>'
                 f'<div class="abs" style="{box(70, 12, 18, 18)}border-radius:50%;background:#9fd8c4"></div></div>')
    # graph plate (glass) tracing the same in-out curve
    GX, GY, GW, GH = 110, 470, 240, 180
    pts = [(GX + 24 + (GW - 48) * u, GY + GH - 26 - (GH - 56) * ease_io(u, 2.4)) for u in [k / 24 for k in range(25)]]
    d = "M" + " L".join(f"{r3(x)},{r3(y)}" for x, y in pts)
    S.mid.append(f'<div class="abs glass" id="{s}-graph" style="{box(GX, GY, GW, GH)}border-radius:18px"></div>')
    S.mid.append(f'<svg class="abs" id="{s}-gsvg" style="{box(0, 0, 1080, 1920)}overflow:visible" viewBox="0 0 1080 1920">'
                 f'<path d="M{GX + 24},{GY + 20} L{GX + 24},{GY + GH - 26} L{GX + GW - 20},{GY + GH - 26}" fill="none" stroke="#acc6e7" stroke-width="2"/>'
                 f'<path id="{s}-gcurve" d="{d}" fill="none" stroke="#294b77" stroke-width="4" stroke-linecap="round" stroke-dasharray="400" stroke-dashoffset="400"/></svg>')
    S.mid.append(f'<div class="abs" id="{s}-gdot" style="{box(pts[0][0] - 8, pts[0][1] - 8, 16, 16)}border-radius:50%;background:#ffffff;box-shadow:0 0 0 4px #294b77"></div>')
    near_blur(S, [(f"{s}-n1", 880, 520, 200, 200, "border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"),
                  (f"{s}-n2", -40, 1420, 280, 28, "border-radius:14px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px)")])
    apex(S, S.near, f"{s}-ap", CX, CY - 192, W42, size=380, ring=True, sparks=5, seed=13, op=0.75)

    # ================================================================ motion
    S.cam([(S.t0, {"z": 0, "rotationY": 0, "rotationX": 0}, None),
           (W42, {"z": 40, "rotationY": -3, "rotationX": 1.5}, "sine.inOut"),
           (W42 + 0.2, {"z": 70}, "power3.out"),
           (end, {"z": 0, "rotationY": 0, "rotationX": 0}, "power2.inOut")])
    # wheel rotation: three snaps pin-to-pin, then an accelerate/decelerate run that lands on "geraknya"
    R0 = 180
    keys = [(S.t0, {"rotation": R0}, None), (W40 + 0.02, {"rotation": R0 + 9}, "none")]
    t = W40 + 0.08
    r = R0 + 9
    for k in range(3):
        keys.append((t + 0.17, {"rotation": r + 36}, "power3.inOut"))
        r += 36
        t += 0.2
    target = R0 + 360 + 45 * 6         # a pin sits under the pointer (multiples of 45 from R0)
    keys.append((W42, {"rotation": target}, "power3.inOut"))
    keys.append((W42 + 0.09, {"rotation": target + 2.5}, "power1.out"))
    keys.append((W42 + 0.26, {"rotation": target}, "power2.inOut"))
    keys.append((end, {"rotation": target + 30}, "power1.in"))
    S.keys(f"#{s}-wheel", keys)
    for k in range(8):
        S.init(f"#{s}-pin{k}", {"scale": 0})
        S.ft(f"#{s}-pin{k}", {"scale": 0}, {"scale": 1}, W40 + k * 0.03, 0.22, "back.out(3)")
        S.ft(f"#{s}-pin{k}", {"scale": 1}, {"scale": 0}, end - 0.36 + k * 0.012, 0.16, "power2.in")
    # pointer kicks as pins pass, a firm click on the landing
    nk = [(S.t0, {"rotation": 0, "transformOrigin": "50% 0%"}, None)]
    for k in range(3):
        tk = W40 + 0.08 + k * 0.2
        nk += [(tk + 0.09, {"rotation": 9}, "power2.out"), (tk + 0.19, {"rotation": 0}, "back.out(3)")]
    nk += [(W42 - 0.05, {"rotation": 12}, "power1.in"), (W42 + 0.03, {"rotation": -4}, "power3.out"), (W42 + 0.25, {"rotation": 0}, "back.out(2.5)")]
    S.keys(f"#{s}-ndl", nk)
    S.init(f"#{s}-ptr", {"y": 0, "opacity": 1})
    S.ft(f"#{s}-ptr", {"y": 0, "opacity": 1}, {"y": -90, "opacity": 0}, end - 0.34, 0.26, "power2.in")
    S.init(f"#{s}-cap", {"opacity": 1, "scale": 1})
    S.ft(f"#{s}-cap", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.6}, end - 0.3, 0.22, "power2.in")
    # card along the easing rail, landing on "geraknya"
    along(S, f"#{s}-card", ((RAIL[0][0], RAIL[0][1] - 33), (RAIL[1][0], RAIL[1][1] - 33), (RAIL[2][0], RAIL[2][1] - 33), (RAIL[3][0], RAIL[3][1] - 33)),
          W40 + 0.15, W42, n=16, rot=True, p=2.6)
    # graph: curve draws with the run, dot follows (x = time, y = eased value)
    S.init(f"#{s}-gcurve", {"strokeDashoffset": 400})
    S.ft(f"#{s}-gcurve", {"strokeDashoffset": 400}, {"strokeDashoffset": 0}, W40 + 0.15, W42 - W40 - 0.15, "none")
    n = 12
    prev = None
    for k in range(n + 1):
        u = k / n
        x = (GW - 48) * u
        y = -(GH - 56) * ease_io(u, 2.4)
        cur = {"x": r3(x), "y": r3(y)}
        if prev is None:
            S.init(f"#{s}-gdot", cur)
        else:
            S.ft(f"#{s}-gdot", prev, cur, W40 + 0.15 + (W42 - W40 - 0.15) * (k - 1) / n, (W42 - W40 - 0.15) / n, "none")
        prev = cur
    for sel in (f"#{s}-ring", f"#{s}-rail", f"#{s}-card", f"#{s}-graph", f"#{s}-gsvg", f"#{s}-gdot"):
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, end - 0.34, 0.24, "power2.in")
