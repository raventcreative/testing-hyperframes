"""S08 — 06 AI APPLICATION (w107-122). VO: "Keenam, AI application. Hubungkan model lewat API, atur output, lalu jadikan
fitur yang benar-benar bisa dipakai."
Opens on S07's output rail (enters from the left at kit_b.OUT_Y). The token tiles ride in, the rail bends down into a
cable and its aluminium plug clicks into the API port of one real app apparatus (porcelain phone on an enamel dock) on
"application" — the screen wakes. EXPLAIN MODE on "Hubungkan model lewat API, atur output": chips MODEL -> API -> OUTPUT;
behind him the request goes out and the response arrives. He steps back: structured response rows build on the phone
and the feature button is pressed on "dipakai". Hand-off: the phone turns edge-on and becomes the archive-cabinet spine
(kit_b.CAB_SPINE) that S09 unfolds from."""
from xk import box, r3
from kit import MAT, SIDE_L, part, shadow, chip, grid_floor, blur_wrap, explain, ICON, FLOOR_Y
from kit_b import rail, OUT_Y, CAB_SPINE, ICON_B, pop_chip, arrow, draw_arrow

PX, PY, PW, PH = 560, 560, 360, 700          # phone
DX, DY, DW, DH = 530, 1260, 420, 92          # dock
PORT = (DX - 6, DY + 28)                     # API port (left face of the dock)


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    # ---------------------------------------------------------------- back
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(shadow(DX - 40, FLOOR_Y - 60, DW + 80, 80, 0.5, f"{s}-dsh"))
    S.back.append(rail(f"{s}-rail", -40, OUT_Y, 430))
    cab = f"M430,{OUT_Y} C520,{OUT_Y} 420,{PORT[1]} {PORT[0] - 60},{PORT[1] + 18}"
    S.back.append(f'<svg class="abs" id="{s}-cab" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path d="{cab}" fill="none" stroke="#0A0D2C" stroke-opacity=".16" stroke-width="18" stroke-linecap="round" transform="translate(5 9)"/>'
                  f'<path d="{cab}" fill="none" stroke="#1c3561" stroke-width="14" stroke-linecap="round"/>'
                  f'<path d="{cab}" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="3" stroke-linecap="round" transform="translate(-2 -3)"/></svg>')
    # tokens riding in on the rail
    for k, (lab, w) in enumerate((("AI", 92), ("ENGIN", 150), ("EER", 110))):
        S.back.append(f'<div class="abs" id="{s}-tok{k}" style="{box(-200, OUT_Y - 74, w, 58)}border-radius:12px;{MAT["porcelain"]}'
                      f'font:700 30px/58px Poppins;color:#0A0D2C;text-align:center">{lab}</div>')
    # dock + API port + plug
    S.back.append(part(f"{s}-dock", DX, DY, DW, DH, "enamel", 22,
                       inner=f'<div class="abs" style="left:150px;top:0;width:240px;font:700 28px/{DH}px Poppins;color:#fff;letter-spacing:.08em;text-align:center">API</div>'))
    S.back.append(f'<div class="abs" style="{box(PORT[0] - 6, PORT[1] - 4, 26, 44)}border-radius:6px;background:#05070d;box-shadow:inset 0 3px 6px rgba(0,0,0,.8)"></div>')
    S.back.append(f'<div class="abs" id="{s}-led" style="{box(DX + 40, DY + 36, 20, 20)}border-radius:50%;background:#9fb3cf"></div>')
    S.back.append(part(f"{s}-plug", PORT[0] - 74, PORT[1] - 2, 70, 40, "alu", 8))
    # phone (porcelain body, glass screen, app UI)
    rows = ""
    for k, (lab, ic) in enumerate((("Ringkasan", "doc"), ("Poin penting", "check"), ("Langkah lanjut", "tool"))):
        rows += (f'<div class="abs" id="{s}-r{k}" style="left:22px;top:{250 + k * 92}px;width:268px;height:78px;border-radius:16px;background:#fff;'
                 f'box-shadow:0 8px 16px -10px rgba(10,13,44,.45),0 0 0 1px rgba(41,75,119,.1)">'
                 f'<div class="abs" style="left:14px;top:21px;width:36px;height:36px;color:#294B77">{ICON[ic]}</div>'
                 f'<div class="abs" style="left:62px;top:0;width:200px;font:700 24px/78px Poppins;color:#0A0D2C">{lab}</div></div>')
    ui = (f'<div class="abs" id="{s}-scr" style="left:24px;top:24px;width:312px;height:652px;border-radius:30px;overflow:hidden;'
          f'background:linear-gradient(170deg,#f6f9fd 0%,#e6eef9 100%)">'
          f'<div class="abs" style="left:0;top:0;width:312px;height:86px;background:linear-gradient(105deg,#0A0D2C,#294B77)"></div>'
          f'<div class="abs" style="left:22px;top:24px;width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.2)"></div>'
          f'<div class="abs" style="left:74px;top:0;width:220px;font:700 26px/86px Poppins;color:#fff">Asisten</div>'
          f'<div class="abs" id="{s}-req" style="left:96px;top:118px;width:194px;height:96px;border-radius:20px 20px 6px 20px;'
          f'background:linear-gradient(105deg,#0A0D2C,#294B77);font:400 22px/1.3 Poppins;color:#fff;padding:14px 16px">Ringkas laporan ini</div>'
          f'{rows}'
          f'<div class="abs" id="{s}-btn" style="left:22px;top:540px;width:268px;height:76px;border-radius:38px;background:linear-gradient(105deg,#0A0D2C,#294B77);'
          f'font:700 26px/76px Poppins;color:#fff;text-align:center;letter-spacing:.06em">PAKAI</div>'
          f'<div class="abs" id="{s}-off" style="left:0;top:0;width:312px;height:652px;background:linear-gradient(170deg,#1b2740,#0A0D2C)"></div></div>')
    S.back.append(f'<div class="abs" id="{s}-phone" style="{box(PX, PY, PW, PH)}border-radius:52px;{MAT["porcelain"]}">{ui}</div>')
    S.back.append(f'<div class="abs" id="{s}-lab" style="left:{DX}px;top:{DY + DH + 26}px"><span class="badge" style="font:700 30px/1 Poppins;padding:10px 16px">06 AI APPLICATION</span></div>')
    # the cabinet spine the phone becomes
    sx, sy, sw, sh = CAB_SPINE
    S.back.append(part(f"{s}-spine", sx, sy, sw, sh, "porcelain", 18))
    blur_wrap(S)
    S.front.append(chip(f"{s}-k1", 30, 446, "MODEL", ICON_B["brain"], size=30))
    S.front.append(arrow(f"{s}-a1", 268, 466, 80))
    S.front.append(chip(f"{s}-k2", 356, 446, "API", ICON["plug"], size=30, dark=True))
    S.front.append(arrow(f"{s}-a2", 556, 466, 80))
    S.front.append(chip(f"{s}-k3", 644, 446, "OUTPUT", ICON["doc"], size=30))

    # ---------------------------------------------------------------- motion
    app = W(109)
    # tokens ride the rail in and drop into the cable mouth
    for k in range(3):
        sel = f"#{s}-tok{k}"
        S.init(sel, {"x": 0, "opacity": 1, "y": 0, "scale": 1})
        S.ft(sel, {"x": 0}, {"x": 560 - 40 * k}, t0 + 0.05 * k, 0.65, "power2.out")
        S.ft(sel, {"y": 0, "scale": 1, "opacity": 1}, {"y": 60, "scale": 0.4, "opacity": 0}, t0 + 0.75 + 0.08 * k, 0.3, "power2.in")
    # the plug slides into the API port on "application"
    S.init(f"#{s}-plug", {"x": -40})
    S.ft(f"#{s}-plug", {"x": -40}, {"x": 8}, app - 0.25, 0.25, "power3.in")
    S.ft(f"#{s}-plug", {"x": 8}, {"x": 4}, app, 0.15, "back.out(3)")
    S.init(f"#{s}-led", {"backgroundColor": "#9fb3cf", "boxShadow": "0 0 0px rgba(120,170,255,0)"})
    S.ft(f"#{s}-led", {"backgroundColor": "#9fb3cf", "boxShadow": "0 0 0px rgba(120,170,255,0)"},
         {"backgroundColor": "#7fb0ff", "boxShadow": "0 0 14px rgba(120,170,255,0.9)"}, app, 0.2, "power2.out")
    S.init(f"#{s}-off", {"opacity": 1})
    S.ft(f"#{s}-off", {"opacity": 1}, {"opacity": 0}, app + 0.1, 0.45, "power2.out")
    S.init(f"#{s}-phone", {"y": 0, "x": 0, "rotationY": 0, "opacity": 1, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-phone", {"y": 0}, {"y": -10}, app, 0.15, "power2.out")
    S.ft(f"#{s}-phone", {"y": -10}, {"y": 0}, app + 0.15, 0.3, "back.out(2)")
    S.fx(app, "click", 0.07)
    S.init(f"#{s}-lab", {"opacity": 0, "y": 16})
    S.ft(f"#{s}-lab", {"opacity": 0, "y": 16}, {"opacity": 1, "y": 0}, app + 0.1, 0.3, "power3.out")
    # request / response (request during the explain, rows after he steps back)
    S.init(f"#{s}-req", {"opacity": 0, "scale": 0.6, "transformOrigin": "100% 100%"})
    S.ft(f"#{s}-req", {"opacity": 0, "scale": 0.6}, {"opacity": 1, "scale": 1}, W(111), 0.3, "back.out(2)")
    for k, wi in enumerate((117, 118, 120)):
        sel = f"#{s}-r{k}"
        S.init(sel, {"opacity": 0, "x": -40})
        S.ft(sel, {"opacity": 0, "x": -40}, {"opacity": 1, "x": 0}, W(wi) - 0.05, 0.3, "power3.out")
        S.fx(W(wi), "pop" if k == 0 else "key", 0.04)
    S.init(f"#{s}-btn", {"scale": 1, "opacity": 0.35})
    S.ft(f"#{s}-btn", {"opacity": 0.35}, {"opacity": 1}, W(120), 0.25, "power2.out")
    dp = W(122)
    S.ft(f"#{s}-btn", {"scale": 1}, {"scale": 0.9}, dp - 0.08, 0.1, "power2.in")
    S.ft(f"#{s}-btn", {"scale": 0.9}, {"scale": 1}, dp + 0.02, 0.3, "back.out(3)")
    S.fx(dp, "ping", 0.05)
    # hand-off: the phone turns edge-on and becomes the archive-cabinet spine
    ho = t1 - 0.5
    sx, sy, sw, sh = CAB_SPINE
    S.ft(f"#{s}-phone", {"x": 0, "rotationY": 0, "opacity": 1}, {"x": sx + sw / 2 - (PX + PW / 2), "rotationY": 84, "opacity": 0}, ho, 0.45, "power3.in")
    S.init(f"#{s}-spine", {"opacity": 0, "scaleY": 0.9, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-spine", {"opacity": 0, "scaleY": 0.9}, {"opacity": 1, "scaleY": 1}, ho + 0.22, 0.26, "power2.out")
    for sel in (f"#{s}-dock", f"#{s}-plug", f"#{s}-cab", f"#{s}-rail", f"#{s}-lab", f"#{s}-led", f"#{s}-dsh"):
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, ho, 0.3, "power2.in")
    S.fx(ho, "whoosh", 0.04)
    t_in, t_out = W(110) - 0.3, W(116) - 0.1
    pop_chip(S, f"#{s}-k1", W(111) - 0.05, t_out - 0.1, -2)
    draw_arrow(S, f"{s}-a1", W(112), t_out - 0.1)
    pop_chip(S, f"#{s}-k2", W(113) - 0.05, t_out - 0.1, 2)
    draw_arrow(S, f"{s}-a2", W(114), t_out - 0.1)
    pop_chip(S, f"#{s}-k3", W(115) - 0.05, t_out - 0.1, -2)

    # ---------------------------------------------------------------- mascot
    side = dict(SIDE_L, fx=210, yaw=28)
    S.mv([(t0, dict(side, yaw=16), None), (app, dict(side, yaw=30), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.3, "explain", 0.3), (app - 0.15, "present", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (app - 0.1, "fist", 0.3), (app + 0.4, "low", 0.4)])
    S.act("head", [(t0, [0.0, 0.0, 0.0], 0.3), (t0 + 0.2, [-0.05, -0.2, 0.0], 0.35), (t0 + 0.9, [0.05, 0.3, 0.02], 0.4), (app, [-0.04, 0.38, 0.05], 0.3)])
    explain(S, t_in, t_out, 110, 115, seed=4, enter=dict(side, yaw=30), leave=dict(side, yaw=26))
    S.mv([(t_out + 0.5, dict(side, yaw=26), None), (t1, dict(side, yaw=32, fx=220), "sine.inOut")])
    S.act("armL", [(t_out + 0.2, "present", 0.3), (W(118), "pointUp", 0.3), (dp - 0.1, "present", 0.3), (ho, "low", 0.4)])
    S.act("armR", [(t_out + 0.2, "low", 0.35), (dp - 0.05, "fist", 0.3), (dp + 0.35, "low", 0.4)])
    S.act("head", [(t_out + 0.2, [-0.05, 0.36, 0.0], 0.35), (W(120), [-0.1, 0.42, 0.04], 0.35), (dp, [0.06, 0.3, -0.03], 0.3)])
