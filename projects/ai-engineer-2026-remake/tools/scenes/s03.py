"""S03 — 01 PYTHON. VO: "Pertama, Python. Kuasai fungsi, struktur data, API, dan debugging. Mulai dari program kecil yang
benar-benar jalan."
Opens inside S02's dive: socket 01 fills the screen centre. The camera rises while the PYTHON MODULE (porcelain block,
enamel top plate engraved 01 PYTHON + code engravings, two aluminium bracket calipers, a status window, a small gear,
a coral error bolt) rises out of the socket and locks on "Python". EXPLAIN MODE on "Kuasai fungsi, struktur data, API, dan
debugging" (module soft behind; four chips pop on their words). Step back: on "program" the error bolt unscrews and flies
off, on "jalan" the gear spins, the lamp lights, the window turns from bug to check. Hand-off: the engraved code strip
extrudes into a navy cable running right and the camera follows it out of frame (-> S04)."""
from xk import box, r3
from kit import MAT, part, shadow, grid_floor, blur_wrap, explain, ICON, cable
from kit_a import zoom_to, chip_row, chips_out

MX, MY, MW, MH = 130, 830, 540, 460   # module box (world)
SX, SY, SD = MX + MW / 2, 1335, 300   # socket (world)
CY = 1000                          # code strip / cable height


def cog(id_, r=46, teeth=10):
    import math
    pts = []
    for k in range(teeth * 2):
        a = math.pi * k / teeth
        rr = r if k % 2 == 0 else r * 0.78
        pts.append(f"{r3(r + rr * math.cos(a))},{r3(r + rr * math.sin(a))}")
    return (f'<svg class="abs" id="{id_}" viewBox="0 0 {2 * r} {2 * r}" style="width:{2 * r}px;height:{2 * r}px;overflow:visible">'
            f'<polygon points="{" ".join(pts)}" fill="#c9d1dc" stroke="#7f8b9c" stroke-width="2"/>'
            f'<circle cx="{r}" cy="{r}" r="{r * .32}" fill="#1c3561"/><circle cx="{r}" cy="{r}" r="{r * .12}" fill="#e6ecf4"/></svg>')


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    S.back.append(grid_floor(f"{s}-grid", y=1500))
    S.back.append(shadow(MX - 40, SY - 30, MW + 80, 110, 0.6, f"{s}-msh"))
    # socket ring (the dive target from S02)
    S.back.append(f'<div class="abs" style="{box(SX - SD / 2, SY - SD * .52 / 2, SD, SD * .52)}">'
                  f'<div class="abs" style="inset:0;border-radius:50%;{MAT["alu"]}"></div>'
                  f'<div class="abs" style="left:18%;top:18%;width:64%;height:64%;border-radius:50%;background:radial-gradient(ellipse at 45% 35%,#2a3446,#0b1020 70%)"></div>'
                  f'<div class="abs" style="left:-8px;top:-8px;right:-8px;bottom:-8px;border-radius:50%;border:5px solid #294B77"></div></div>')
    code = ("".join(f'<div class="abs" style="left:26px;top:{20 + 34 * k}px;font:400 26px/30px Poppins;color:rgba(255,255,255,{.9 if k == 0 else .55});white-space:nowrap">{ln}</div>'
                    for k, ln in enumerate(["def jalan(data):", "&nbsp;&nbsp;hasil = olah(data)", "&nbsp;&nbsp;return hasil"])))
    inner = (
        # enamel top plate with label + code engravings
        f'<div class="abs" style="left:18px;top:18px;width:{MW - 36}px;height:58px;border-radius:12px;background:linear-gradient(105deg,#0A0D2C,#294B77);'
        f'box-shadow:inset 0 1px 0 rgba(255,255,255,.3);font:700 30px/58px Poppins;color:#fff;letter-spacing:.08em;text-align:center">01 &nbsp;PYTHON</div>'
        f'<div class="abs" id="{s}-strip" style="left:18px;top:{CY - MY - 16}px;width:{MW - 36}px;height:130px;border-radius:12px;{MAT["enamel"]}">{code}</div>'
        # status window
        f'<div class="abs" style="left:{MW - 150}px;top:{MH - 150}px;width:110px;height:110px;border-radius:50%;{MAT["alu"]}"></div>'
        f'<div class="abs" style="left:{MW - 140}px;top:{MH - 140}px;width:90px;height:90px;border-radius:50%;background:#0b1428;overflow:hidden">'
        f'<div class="abs" id="{s}-bug" style="left:22px;top:22px;width:46px;height:46px;color:#ff8a72">{ICON["bug"]}</div>'
        f'<div class="abs" id="{s}-ok" style="left:20px;top:20px;width:50px;height:50px;color:#9fd0ff">{ICON["check"]}</div>'
        f'<div class="abs" id="{s}-lamp" style="inset:0;border-radius:50%;background:radial-gradient(circle,rgba(160,205,255,.55),rgba(160,205,255,0) 70%)"></div></div>'
        f'<div class="abs" id="{s}-cogw" style="left:40px;top:{MH - 140}px;width:92px;height:92px">{cog(f"{s}-cog")}</div>')
    S.back.append(f'<div class="abs" id="{s}-mod" style="{box(MX, MY, MW, MH)}">{part(None, 0, 0, MW, MH, "porcelain", 26, inner=inner)}</div>')
    # bracket calipers { } either side of the module
    for k, (x, ch) in enumerate(((MX - 86, "{"), (MX + MW + 14, "}"))):
        S.back.append(f'<div class="abs" id="{s}-br{k}" style="{box(x, MY + 70, 72, 220)}font:700 200px/220px Poppins;text-align:center;'
                      f'background:linear-gradient(150deg,#f2f5f9,#9aa6b6 55%,#dde3ea);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;'
                      f'filter:drop-shadow(0 10px 10px rgba(10,13,44,.3))">{ch}</div>')
    # coral error bolt on the module's front-right
    S.back.append(f'<div class="abs" id="{s}-bolt" style="{box(MX + MW - 64, MY + 96, 44, 44)}border-radius:50%;'
                  f'background:radial-gradient(circle at 40% 35%,#ffb4a3,#e2614b 60%,#a8392a);box-shadow:0 4px 8px rgba(120,30,20,.4)">'
                  f'<div class="abs" style="left:8px;top:17px;width:24px;height:6px;border-radius:3px;background:rgba(80,10,5,.6)"></div></div>')
    S.back.append(f'<div class="abs" id="{s}-cabw" style="left:0;top:0;width:1080px;height:1920px">' + cable(f"{s}-cab", f"M{MX + MW - 18},{CY + 40} C{MX + MW + 120},{CY + 40} {MX + MW + 160},{CY + 90} {1200},{CY + 90}", w=14, color="#1c3561") + "</div>")
    blur_wrap(S)
    ids = [c[0] for c in chip_row(S, f"{s}-k", [("fungsi", ICON["fn"], 35, False), ("struktur data", ICON["db"], 36, False),
                                               ("API", ICON["plug"], 38, False), ("debugging", ICON["bug"], 40, True)], 444, size=26, gap=14)]

    # ---------------------------------------------------------------- motion
    back = W(41) - 0.3
    S.cam([(t0, zoom_to(SX, SY, 1.0), None), (t0 + 0.9, {"x": 0, "y": 0, "scale": 1}, "power3.inOut"),
           (t1 - 0.5, {"x": 0, "y": 0, "scale": 1}, "none"), (t1, {"x": -460, "y": -60, "scale": 1.05}, "power2.in")])
    S.init(f"#{s}-mod", {"y": 260, "scaleY": 0.3, "opacity": 0, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-mod", {"y": 260, "scaleY": 0.3, "opacity": 0}, {"y": 0, "scaleY": 1, "opacity": 1}, t0 + 0.15, 0.6, "back.out(1.4)")
    S.ft(f"#{s}-mod", {"y": 0}, {"y": 8}, W(33) - 0.02, 0.08, "power2.in")
    S.ft(f"#{s}-mod", {"y": 8}, {"y": 0}, W(33) + 0.06, 0.25, "back.out(3)")
    S.init(f"#{s}-msh", {"opacity": 0})
    S.ft(f"#{s}-msh", {"opacity": 0}, {"opacity": 0.6}, t0 + 0.3, 0.5, "power2.out")
    for k, dx in enumerate((-60, 60)):
        S.init(f"#{s}-br{k}", {"x": dx, "opacity": 0, "rotationY": 70 if k == 0 else -70})
        S.ft(f"#{s}-br{k}", {"x": dx, "opacity": 0, "rotationY": 70 if k == 0 else -70}, {"x": 0, "opacity": 1, "rotationY": 0}, W(33) - 0.15, 0.4, "back.out(2)")
    S.fx(W(33), "click", 0.07)
    # demonstrate: bolt unscrews, gear spins, lamp + check on "jalan"
    S.init(f"#{s}-bolt", {"rotation": 0, "x": 0, "y": 0, "opacity": 0})
    S.ft(f"#{s}-bolt", {"opacity": 0}, {"opacity": 1}, t0 + 0.6, 0.2, "power2.out")
    S.ft(f"#{s}-bolt", {"rotation": 0}, {"rotation": -540}, W(43) - 0.1, 0.55, "power2.inOut")
    S.ft(f"#{s}-bolt", {"x": 0, "y": 0, "opacity": 1}, {"x": 140, "y": -110, "opacity": 0}, W(43) + 0.45, 0.35, "power2.in")
    S.init(f"#{s}-bug", {"opacity": 1, "scale": 1})
    S.ft(f"#{s}-bug", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.4}, W(46), 0.25, "power2.in")
    S.init(f"#{s}-ok", {"opacity": 0, "scale": 0.4})
    S.ft(f"#{s}-ok", {"opacity": 0, "scale": 0.4}, {"opacity": 1, "scale": 1}, W(47) - 0.05, 0.3, "back.out(2.5)")
    S.init(f"#{s}-lamp", {"opacity": 0})
    S.ft(f"#{s}-lamp", {"opacity": 0}, {"opacity": 1}, W(47) - 0.05, 0.3, "power2.out")
    S.init(f"#{s}-cog", {"rotation": 0, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-cog", {"rotation": 0}, {"rotation": 360}, W(47) - 0.1, t1 - W(47) + 0.1, "power1.in")
    S.fx(W(43), "key", 0.05)
    S.fx(W(47), "ping", 0.06)
    # hand-off: code strip glows, cable extrudes out to the right
    S.init(f"#{s}-strip", {"boxShadow": "0 0 0 0px rgba(120,170,240,0)"})
    S.ft(f"#{s}-strip", {"boxShadow": "0 0 0 0px rgba(120,170,240,0)"}, {"boxShadow": "0 0 0 6px rgba(120,170,240,0.55)"}, t1 - 0.75, 0.3, "power2.out")
    S.init(f"#{s}-cabw", {"opacity": 0})
    S.tset(f"#{s}-cabw", {"opacity": 1}, t1 - 0.66)
    S.init(f"#{s}-cab", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-cab", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, t1 - 0.65, 0.5, "power2.inOut")
    S.fx(t1 - 0.45, "whoosh", 0.05)
    blur_t = back
    chips_out(S, ids, back - 0.1)

    # ---------------------------------------------------------------- mascot
    s02_end = {"fx": 930, "fy": 1900, "h": 780, "yaw": -40, "pitch": 6}
    right = {"fx": 900, "fy": 1890, "h": 820, "yaw": -32, "pitch": 6}
    S.mv([(t0, s02_end, None), (t0 + 0.8, dict(s02_end, yaw=-30), "sine.inOut")])
    S.act("armR", [(t0, "point", 0.3), (W(33) - 0.2, "point", 0.25), (W(33) + 0.35, "low", 0.35)])
    S.act("armL", [(t0, "low", 0.3), (W(33) - 0.1, "fist", 0.25), (W(33) + 0.4, "low", 0.35)])
    S.act("head", [(t0, [0.1, -0.35, 0], 0.3), (W(33), [0.02, -0.25, 0.05], 0.3)])
    explain(S, W(34) - 0.3, back, 34, 40, seed=0, enter=dict(s02_end, yaw=-20), leave=right)
    S.mv([(back + 0.5, right, None), (W(46), dict(right, yaw=-36), "sine.inOut"), (t1, dict(right, yaw=-42, fx=900), "sine.inOut")])
    S.act("armR", [(back + 0.2, "low", 0.35), (W(43) - 0.25, "point", 0.25), (W(44) + 0.1, "fist", 0.3), (W(46) - 0.1, "low", 0.3), (W(47) - 0.1, "pointUp", 0.25), (t1 - 0.2, "present", 0.3)])
    S.act("armL", [(back + 0.2, "low", 0.35), (W(47) - 0.05, "fist", 0.25), (t1 - 0.15, "low", 0.35)])
    S.act("head", [(back + 0.2, [0.08, -0.32, 0], 0.35), (W(43), [0.14, -0.4, 0.04], 0.3), (W(47), [-0.08, -0.3, -0.05], 0.25), (t1 - 0.3, [0.0, -0.5, 0], 0.35)])
    S.act("torso", [(back + 0.2, {"chest": [0.03, -0.12, 0]}, 0.35), (W(47), {"chest": [-0.03, -0.16, 0]}, 0.25)])
