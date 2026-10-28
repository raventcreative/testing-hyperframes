"""S04 — 02 SOFTWARE ENGINEERING. VO: "Kedua, software engineering. Pahami Git, database, backend, dan cara aplikasi saling
terhubung. Karena AI tetap butuh sistem yang rapi."
The camera keeps following S03's cable in from the left until it plugs into the BACKEND chassis port ("software
engineering"). Then the software bay assembles itself as architecture, each part on its word: GIT version rails fork and
rejoin, three DATABASE cylinders rise with contact shadows, the BACKEND chassis closes its auth gate, an APP tile docks;
on "saling terhubung" cables link db -> backend -> app and a pulse runs through them. EXPLAIN MODE on "Karena AI tetap butuh
sistem" (bay soft behind; chips AI -> SISTEM). Step back on "rapi": every slightly-crooked part snaps square and a check
seal lands. Hand-off: a database pin drops out of the bottom as a data bead (-> S05's ML tray)."""
from xk import box, r3
from kit import MAT, part, shadow, grid_floor, blur_wrap, explain, ICON, cable
from kit_a import chip_row, chips_out

CY = 1090                       # incoming cable height
DB = [(150, 940), (275, 960), (400, 940)]    # cylinder (x, top)
BE = (560, 880, 400, 300)       # backend chassis
APP = (700, 560, 260, 230)      # app tile
GIT_Y = (600, 690)              # git rail main / branch y


def cyl(id_, x, y, w=110, h=200):
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h + w * .3)}">'
            f'<div class="abs" style="left:0;top:{w * .15}px;width:{w}px;height:{h}px;border-radius:0 0 {w / 2}px {w / 2}px / 0 0 {w * .15}px {w * .15}px;{MAT["enamel"]}"></div>'
            f'<div class="abs" style="left:0;top:{w * .15 + h * .33}px;width:{w}px;height:3px;background:rgba(255,255,255,.25)"></div>'
            f'<div class="abs" style="left:0;top:{w * .15 + h * .66}px;width:{w}px;height:3px;background:rgba(255,255,255,.25)"></div>'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:{w * .3}px;border-radius:50%;background:linear-gradient(160deg,#ffffff,#c9d1dc);'
            f'box-shadow:inset 0 -3px 6px rgba(41,75,119,.3)"></div></div>')


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    S.back.append(grid_floor(f"{s}-grid", y=1480))
    # git rails (main + branch that forks and rejoins), commit dots
    gm, gb = GIT_Y
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-gmain" d="M110,{gm} H640" fill="none" stroke="#9aa6b6" stroke-width="12" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                  f'<path id="{s}-gbr" d="M230,{gm} C280,{gb} 300,{gb} 360,{gb} H460 C520,{gb} 520,{gm} 570,{gm}" fill="none" stroke="#294B77" stroke-width="10" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                  + "".join(f'<circle id="{s}-gc{k}" cx="{cx}" cy="{cy}" r="17" fill="#ffffff" stroke="{c}" stroke-width="7"/>'
                            for k, (cx, cy, c) in enumerate(((140, gm, "#7f8b9c"), (230, gm, "#7f8b9c"), (360, gb, "#294B77"), (460, gb, "#294B77"), (570, gm, "#1c3561"), (640, gm, "#1c3561"))))
                  + f'</svg>')
    S.back.append(f'<div class="abs" id="{s}-glab" style="{box(110, gm - 76, 200, 40)}font:700 24px/40px Poppins;color:#294B77;letter-spacing:.08em">'
                  f'<span style="display:inline-block;width:26px;height:26px;vertical-align:-5px;margin-right:8px;color:#294B77">{ICON["branch"]}</span>GIT</div>')
    # incoming cable from S03 (behind the database row)
    bx, by, bw, bh = BE
    S.back.append(cable(f"{s}-in", f"M-200,{CY + 90} C-40,{CY + 90} {bx - 120},{CY} {bx - 26},{CY}", w=14, color="#1c3561", dash=False))
    # database cylinders
    for k, (x, y) in enumerate(DB):
        S.back.append(shadow(x - 20, y + 230, 150, 50, 0.55, f"{s}-dsh{k}"))
        S.back.append(cyl(f"{s}-db{k}", x, y))
    S.back.append(f'<div class="abs" style="{box(150, 1215, 360, 36)}font:700 24px/36px Poppins;color:#294B77;letter-spacing:.08em;text-align:center">DATABASE</div>')
    # backend chassis: label plate, auth gate, interface port
    bx, by, bw, bh = BE
    S.back.append(shadow(bx - 20, by + bh - 20, bw + 40, 70, 0.6))
    gate = (f'<div class="abs" style="left:{bw - 120}px;top:96px;width:84px;height:120px;border-radius:12px;background:#0b1428;overflow:hidden">'
            f'<div class="abs" id="{s}-gate" style="left:0;top:0;width:84px;height:120px;{MAT["alu"]}border-radius:10px">'
            f'<div class="abs" style="left:27px;top:44px;width:30px;height:30px;color:#294B77">{ICON["shield"]}</div></div></div>')
    port = (f'<div class="abs" style="left:-26px;top:{CY - by - 26}px;width:52px;height:52px;border-radius:12px;{MAT["alu"]}"></div>'
            f'<div class="abs" id="{s}-portl" style="left:-14px;top:{CY - by - 14}px;width:28px;height:28px;border-radius:8px;background:#0b1428"></div>')
    rows = "".join(f'<div class="abs" id="{s}-led{k}" style="left:40px;top:{104 + 36 * k}px;width:{150 - 20 * k}px;height:14px;border-radius:7px;background:rgba(255,255,255,.18)"></div>' for k in range(3))
    S.back.append(f'<div class="abs" id="{s}-be" style="{box(bx, by, bw, bh)}">'
                  + part(None, 0, 0, bw, bh, "porcelain", 26,
                         inner=f'<div class="abs" style="left:18px;top:18px;width:{bw - 36}px;height:52px;border-radius:12px;background:linear-gradient(105deg,#0A0D2C,#294B77);'
                               f'font:700 23px/52px Poppins;color:#fff;letter-spacing:.06em;text-align:center">02 SOFTWARE ENG.</div>'
                               f'<div class="abs" style="left:24px;top:88px;width:{bw - 170}px;height:180px;border-radius:14px;{MAT["enamel"]}">{rows}</div>'
                               + gate)
                  + port + '</div>')
    S.back.append(f'<div class="abs" style="{box(bx, by + bh + 18, bw, 36)}font:700 24px/36px Poppins;color:#294B77;letter-spacing:.08em;text-align:center">BACKEND</div>')
    # app tile
    ax, ay, aw, ah = APP
    S.back.append(f'<div class="abs" id="{s}-app" style="{box(ax, ay, aw, ah)}">'
                  + part(None, 0, 0, aw, ah, "glass", 30,
                         inner=f'<div class="abs" style="left:22px;top:22px;width:{aw - 44}px;height:44px;border-radius:12px;background:linear-gradient(105deg,#0A0D2C,#294B77);font:700 22px/44px Poppins;color:#fff;text-align:center;letter-spacing:.08em">APLIKASI</div>'
                               + "".join(f'<div class="abs" style="left:22px;top:{86 + 40 * k}px;width:{aw - 44 - 40 * k}px;height:22px;border-radius:11px;background:rgba(41,75,119,{.25 - .05 * k})"></div>' for k in range(3)))
                  + '</div>')
    # links: db -> backend, backend -> app, incoming cable from S03
    S.back.append(f'<div class="abs" id="{s}-lw1" style="left:0;top:0;width:1080px;height:1920px">' + cable(f"{s}-l1", f"M510,1060 C540,1060 530,1040 {bx},1040", w=9, color="#294B77") + "</div>")
    S.back.append(f'<div class="abs" id="{s}-lw2" style="left:0;top:0;width:1080px;height:1920px">' + cable(f"{s}-l2", f"M{bx + bw - 60},{by} C{bx + bw - 60},{by - 60} {ax + aw / 2},{ay + ah + 60} {ax + aw / 2},{ay + ah}", w=9, color="#294B77") + "</div>")
    S.back.append(f'<div class="abs" id="{s}-lw3" style="left:0;top:0;width:1080px;height:1920px">' + cable(f"{s}-l3", f"M{bx + bw / 2 - 120},{by} C{bx + bw / 2 - 120},{by - 140} 640,{gm + 120} 640,{gm + 20}", w=9, color="#294B77") + "</div>")
    S.back.append(f'<div class="abs" id="{s}-pulse" style="{box(bx - 60, CY - 9, 18, 18)}border-radius:50%;background:#bcd6ff;box-shadow:0 0 14px 4px rgba(150,190,255,.9)"></div>')
    # "rapi" check seal + the database pin that drops as a data bead
    S.back.append(f'<div class="abs" id="{s}-seal" style="{box(860, 1110, 96, 96)}border-radius:50%;background:linear-gradient(135deg,#0A0D2C,#294B77);color:#fff;padding:22px;'
                  f'box-shadow:0 0 0 6px rgba(255,255,255,.9),0 16px 24px -10px rgba(10,13,44,.5)">{ICON["check"]}</div>')
    S.back.append(f'<div class="abs" id="{s}-bead" style="{box(312, 1180, 46, 46)}border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffffff,#9fc4ff 35%,#294B77 75%,#0A0D2C);'
                  f'box-shadow:0 10px 16px -6px rgba(10,13,44,.6)"></div>')
    blur_wrap(S)
    ids = [c[0] for c in chip_row(S, f"{s}-k", [("AI", ICON["bolt"], 61, False), ("butuh sistem", ICON["server"], 64, True)], 444, size=32, gap=80)]
    S.front.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:600px;overflow:visible" viewBox="0 0 1080 600">'
                   f'<path id="{s}-ar" d="M372 484 H448 M430 468 L449 484 L430 500" fill="none" stroke="#294B77" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')

    # ---------------------------------------------------------------- motion
    exp_in, exp_out = W(60) - 0.3, W(65) - 0.25
    S.cam([(t0, {"x": 420, "y": 40, "scale": 1.05}, None), (W(49), {"x": 0, "y": 0, "scale": 1}, "power3.inOut"),
           (W(51), {"x": 0, "y": 0, "scale": 1}, "none"), (W(59) + 0.5, {"x": 0, "y": -30, "scale": 1.04}, "sine.inOut"),
           (t1 - 0.5, {"x": 0, "y": -30, "scale": 1.04}, "none"), (t1, {"x": 0, "y": -340, "scale": 1.12}, "power2.in")])
    # cable plugs in (pulse travels to the port, click), chassis label lights
    S.init(f"#{s}-pulse", {"x": -500, "opacity": 0})
    S.tset(f"#{s}-pulse", {"opacity": 1}, t0 + 0.2)
    S.ft(f"#{s}-pulse", {"x": -500}, {"x": 40}, t0 + 0.2, W(50) - t0 - 0.2, "power2.inOut")
    S.tset(f"#{s}-pulse", {"opacity": 0}, W(50) + 0.02)
    S.init(f"#{s}-portl", {"backgroundColor": "#0b1428"})
    S.ft(f"#{s}-portl", {"backgroundColor": "#0b1428"}, {"backgroundColor": "#9fc4ff"}, W(50), 0.2, "power2.out")
    S.fx(W(50), "click", 0.07)
    # crooked initial attitudes (snap square on "rapi")
    tilt = {f"#{s}-db0": -6, f"#{s}-db1": 4, f"#{s}-db2": -3, f"#{s}-be": 2.5, f"#{s}-app": -5}
    rapi = W(66)
    # git rails draw on "Git"
    S.init(f"#{s}-gmain", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-gmain", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(52) - 0.15, 0.5, "power2.out")
    S.init(f"#{s}-gbr", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-gbr", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(52) + 0.1, 0.5, "power2.inOut")
    for k in range(6):
        S.init(f"#{s}-gc{k}", {"scale": 0, "transformOrigin": "50% 50%"})
        S.ft(f"#{s}-gc{k}", {"scale": 0}, {"scale": 1}, W(52) - 0.1 + 0.08 * k, 0.25, "back.out(3)")
    S.init(f"#{s}-glab", {"opacity": 0, "x": -20})
    S.ft(f"#{s}-glab", {"opacity": 0, "x": -20}, {"opacity": 1, "x": 0}, W(52) - 0.1, 0.3, "power2.out")
    # database cylinders rise
    for k in range(3):
        sel = f"#{s}-db{k}"
        S.init(sel, {"scaleY": 0, "opacity": 0, "rotation": tilt[sel], "transformOrigin": "50% 100%"})
        S.ft(sel, {"scaleY": 0, "opacity": 0}, {"scaleY": 1, "opacity": 1}, W(53) - 0.12 + 0.1 * k, 0.45, "back.out(1.8)")
        S.init(f"#{s}-dsh{k}", {"opacity": 0})
        S.ft(f"#{s}-dsh{k}", {"opacity": 0}, {"opacity": 0.55}, W(53) + 0.1 * k, 0.4, "power2.out")
        S.ft(sel, {"rotation": tilt[sel]}, {"rotation": 0}, rapi - 0.05 + 0.04 * k, 0.3, "back.out(3)")
    S.fx(W(53), "pop", 0.05)
    # backend: rows light + gate slides shut
    S.init(f"#{s}-be", {"rotation": 0, "y": 0, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-be", {"rotation": 0}, {"rotation": tilt[f"#{s}-be"]}, W(53), 0.4, "sine.inOut")
    S.ft(f"#{s}-be", {"rotation": tilt[f"#{s}-be"]}, {"rotation": 0}, rapi, 0.3, "back.out(3)")
    for k in range(3):
        S.init(f"#{s}-led{k}", {"backgroundColor": "rgba(255,255,255,0.18)"})
        S.ft(f"#{s}-led{k}", {"backgroundColor": "rgba(255,255,255,0.18)"}, {"backgroundColor": "rgba(160,200,255,0.9)"}, W(54) + 0.08 * k, 0.2, "power2.out")
    S.init(f"#{s}-gate", {"y": -120})
    S.ft(f"#{s}-gate", {"y": -120}, {"y": 0}, W(54) + 0.1, 0.35, "power3.in")
    S.fx(W(54) + 0.42, "click", 0.06)
    # app tile docks, links draw on "terhubung"
    S.init(f"#{s}-app", {"opacity": 0, "y": -60, "rotation": tilt[f"#{s}-app"], "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-app", {"opacity": 0, "y": -60}, {"opacity": 1, "y": 0}, W(57) - 0.1, 0.4, "back.out(2)")
    S.ft(f"#{s}-app", {"rotation": tilt[f"#{s}-app"]}, {"rotation": 0}, rapi + 0.04, 0.3, "back.out(3)")
    for k, sel in enumerate((f"#{s}-l1", f"#{s}-l2", f"#{s}-l3")):
        S.init(f"#{s}-lw{k + 1}", {"opacity": 0})
        S.tset(f"#{s}-lw{k + 1}", {"opacity": 1}, W(59) - 0.2 + 0.12 * k)
        S.init(sel, {"attr": {"stroke-dashoffset": 1}})
        S.ft(sel, {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(59) - 0.2 + 0.12 * k, 0.4, "power2.inOut")
    S.fx(W(59), "ping", 0.05)
    # "rapi": seal lands
    S.init(f"#{s}-seal", {"scale": 2.2, "opacity": 0, "rotation": -20})
    S.ft(f"#{s}-seal", {"scale": 2.2, "opacity": 0, "rotation": -20}, {"scale": 1, "opacity": 1, "rotation": 0}, rapi + 0.05, 0.3, "back.out(2)")
    S.fx(rapi + 0.1, "pop", 0.06)
    # hand-off: db pin drops out as a data bead (camera tips down to follow it)
    S.init(f"#{s}-bead", {"y": -40, "opacity": 0, "scale": 0.6})
    S.ft(f"#{s}-bead", {"y": -40, "opacity": 0, "scale": 0.6}, {"y": 0, "opacity": 1, "scale": 1}, t1 - 0.62, 0.18, "back.out(2)")
    S.ft(f"#{s}-bead", {"y": 0}, {"y": 760}, t1 - 0.42, 0.42, "power2.in")
    # explain band
    S.init(f"#{s}-ar", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-ar", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(62), 0.35, "power2.out")
    chips_out(S, ids, exp_out - 0.1)
    S.ft(f"#{s}-ar", {"attr": {"stroke-dashoffset": 0}}, {"attr": {"stroke-dashoffset": -1}}, exp_out - 0.1, 0.25, "power2.in")

    # ---------------------------------------------------------------- mascot: lower-left engineer, points at each part
    s03_end = {"fx": 900, "fy": 1890, "h": 820, "yaw": -42, "pitch": 6}
    left = {"fx": 560, "fy": 2000, "h": 760, "yaw": 10, "pitch": 6}
    S.mv([(t0, s03_end, None), (t0 + 0.75, dict(s03_end, fx=1000, yaw=-60), "power2.in"), (t0 + 0.76, dict(left, fx=1250, yaw=-40), "none"),
          (W(51) - 0.1, left, "power3.out"), (W(52), dict(left, yaw=28), "sine.inOut"), (W(54), dict(left, yaw=-18), "sine.inOut"), (W(57), dict(left, yaw=-26), "sine.inOut"),
          (exp_in, dict(left, yaw=0), "sine.inOut")])
    S.act("armR", [(t0, "low", 0.3)])
    S.act("armL", [(t0, "low", 0.3), (W(51) - 0.2, "pointUp", 0.3), (W(53) - 0.2, "point", 0.3), (W(54) - 0.1, "present", 0.3), (W(57), "pointUp", 0.3),
                   (W(59) - 0.1, "open", 0.3), (exp_in - 0.05, "low", 0.3)])
    S.act("armR", [(W(55), "palmUp", 0.3), (W(59), "open", 0.3), (exp_in - 0.05, "low", 0.3)])
    S.act("head", [(W(51) - 0.2, [-0.1, 0.3, 0], 0.3), (W(53), [0.06, 0.34, 0.03], 0.3), (W(54), [0.0, 0.4, 0], 0.3), (W(57), [-0.14, 0.42, 0.04], 0.3),
                   (W(59), [-0.02, 0.3, -0.04], 0.3)])
    explain(S, exp_in, exp_out, 60, 64, seed=3, enter=dict(left, yaw=0), leave=dict(left, yaw=12))
    S.mv([(exp_out + 0.5, dict(left, yaw=12), None), (t1, dict(left, yaw=24), "sine.inOut")])
    S.act("armL", [(exp_out + 0.15, "pointUp", 0.3), (rapi + 0.15, "fist", 0.25), (t1 - 0.1, "low", 0.35)])
    S.act("armR", [(exp_out + 0.15, "low", 0.35), (rapi + 0.1, "fist", 0.25)])
    S.act("head", [(exp_out + 0.15, [-0.05, 0.36, 0], 0.3), (rapi, [0.04, 0.22, 0.06], 0.25), (t1 - 0.3, [0.2, 0.2, 0], 0.3)])
