"""S13 — ONE SYSTEM, MULTIPLE USES (32.48–37.88)
VO: "Jadi, satu proyek bisa jadi kerangka untuk konten edukasi, promo, sampai iklan."
A master template machine receives one project cartridge ("proyek"), its navy skeleton lights up ("kerangka") and a
rail carries the same motion skeleton to three dioramas built from the same parts: learning board ("edukasi"),
rotating product stand ("promo"), campaign billboard ("iklan"). The camera tracks across them and pulls back to the
product family; the machine's round meter sits at the centre for the match into S14 (credit meter)."""
from xk import box, screw, screws_rect, shadow, pedestal, apex, gear_svg, rivets_line, r3
from kit_d import bottle, dial, vent_lines

SFX = [(33.5, "click", 0.09), (37.06, "sparkle", 0.08)]

MX, MY, MW, MH = 1060, 500, 460, 300     # master machine (world coords; camera starts centred on it)
DX = (590, 1290, 1990)                   # diorama centres
RAIL_Y = 852


def build(S):
    s = S.id
    S.persp_origin = (590, 520)
    W = S.W
    wPro, wKer, wEdu, wPromo, wIkl = W(71), W(74), W(77), W(78), W(80)

    # ------------------------------------------------------------ far: long porcelain gallery wall + arches
    far = [f'<div class="abs" style="{box(-200, 1500, 2900, 8)}border-radius:4px;background:rgba(172,198,231,.55)"></div>',
           f'<div class="abs" style="{box(-200, 1526, 2900, 3)}background:rgba(172,198,231,.35)"></div>']
    for k, cx in enumerate(DX):
        far.append(f'<div class="abs por-dim" style="{box(cx - 270, 720, 540, 760)}border-radius:270px 270px 30px 30px;opacity:.5"></div>')
        far.append(f'<div class="abs" style="{box(cx - 230, 760, 460, 700)}border-radius:230px 230px 22px 22px;border:2px solid rgba(255,255,255,.85)"></div>')
    far.append(f'<div class="abs" style="{box(MX - 120, 380, MW + 240, 520)}border-radius:50%;background:radial-gradient(ellipse,rgba(255,255,255,.95),rgba(255,255,255,0) 65%)"></div>')
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">{"".join(far)}</div>')

    # ------------------------------------------------------------ master template machine
    m = []
    m.append(shadow(MX - 30, MY + MH + 30, MW + 60, 60, 0.8))
    m.append(f'<div class="abs por-dim" style="{box(MX - 50, MY + MH + 6, MW + 100, 22)}border-radius:8px"></div>')  # shelf
    m.append(f'<div class="abs navy-side" style="{box(MX - 50, MY + MH + 24, MW + 100, 8)}border-radius:0 0 6px 6px"></div>')
    m.append(f'<div class="abs por" style="{box(MX, MY, MW, MH)}border-radius:34px"></div>')
    m.append(f'<div class="abs navy-side" style="{box(MX + 14, MY + MH - 10, MW - 28, 10)}border-radius:0 0 30px 30px;opacity:.9"></div>')
    m.append(screws_rect(MX, MY, MW, MH, inset=20, size=12))
    # top band: slot, leds, meter dial
    m.append(f'<div class="abs" style="{box(MX + MW / 2 - 70, MY + 14, 140, 14)}border-radius:7px;background:#1c3354;box-shadow:inset 0 2px 3px rgba(0,0,0,.4),0 1px 0 #fff"></div>')
    for k in range(3):
        m.append(f'<div class="led-off" id="{s}-ml{k}" style="left:{MX + 46 + k * 22}px;top:{MY + 26}px"></div>')
        m.append(f'<div class="led" id="{s}-mlo{k}" style="left:{MX + 46 + k * 22}px;top:{MY + 26}px"></div>')
    m.append(dial(f"{s}-dl", MX + MW - 62, MY + 46, 30, arcs=((60, 118, "#9fd8c4"),)))
    # window with the skeleton ("kerangka")
    WX, WY, WW, WH = MX + 28, MY + 76, MW - 56, MH - 104
    m.append(f'<div class="abs glass" style="{box(WX, WY, WW, WH)}border-radius:18px;background:linear-gradient(160deg,rgba(232,240,251,.9),rgba(203,219,244,.55))"></div>')
    sk = []
    for k in range(3):
        fx_ = 46 + k * 128
        sk.append(f'<div class="abs" style="{box(fx_, 22, 74, 128)}border-radius:10px;border:2.5px dashed rgba(58,98,153,.35)"></div>')
        sk.append(f'<div class="abs" id="{s}-sk{k}" style="{box(fx_, 22, 74, 128)}border-radius:10px;border:3px solid #294b77;box-shadow:0 0 12px rgba(58,98,153,.45)"></div>')
        sk.append(f'<div class="abs" style="{box(fx_ + 10, 34, 40, 6)}border-radius:3px;background:rgba(41,75,119,.4)"></div>')
        sk.append(f'<div class="abs" style="{box(fx_ + 10, 50, 54, 50)}border-radius:6px;background:rgba(172,198,231,.55)"></div>')
    sk.append(f'<div class="abs" style="{box(40, 164, WW - 80, 4)}border-radius:2px;background:rgba(58,98,153,.3)"></div>')
    sk.append(f'<div class="abs" id="{s}-skr" style="{box(40, 164, WW - 80, 4)}border-radius:2px;background:#294b77"></div>')
    for k in range(4):
        sk.append(f'<div class="pin" style="left:{40 + k * (WW - 80) / 3 - 5}px;top:161px"></div>')
    m.append(f'<div class="abs" style="{box(WX, WY, WW, WH)}">{"".join(sk)}</div>')
    m.append(f'<div class="abs" id="{s}-wrefl" style="{box(WX + 10, WY, 70, WH)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.6),rgba(255,255,255,0))"></div>')
    # output port
    m.append(f'<div class="abs por" style="{box(MX + MW / 2 - 40, MY + MH + 30, 80, 26)}border-radius:6px 6px 14px 14px"></div>')
    # project cartridge (enters the slot on "proyek"), clipped by a slot mask
    m.append(f'<div class="abs" style="{box(MX + MW / 2 - 80, 420, 160, MY + 21 - 420)}overflow:hidden">'
             f'<div class="abs por" id="{s}-cart" style="{box(25, 0, 110, 80)}border-radius:12px">'
             f'<div class="abs navy-side" style="{box(0, 30, 110, 22)}"></div>'
             f'<div class="abs" style="{box(14, 58, 50, 6)}border-radius:3px;background:#9fd8c4"></div>'
             f'<div class="abs" style="{box(14, 10, 70, 6)}border-radius:3px;background:#cbdbf4"></div>'
             f'{screw(96, 14, 30, 8)}</div></div>')
    S.mid.extend(m)

    # ------------------------------------------------------------ rail (the shared motion skeleton travels here)
    S.mid.append(f'<div class="abs" style="{box(MX + MW / 2 - 4, MY + MH + 54, 8, RAIL_Y - MY - MH - 54)}background:linear-gradient(90deg,#3a6299,#1c3354)"></div>')
    S.mid.append(f'<div class="abs navy-side" id="{s}-rl" style="{box(DX[0], RAIL_Y, DX[1] - DX[0], 8)}border-radius:4px"></div>')
    S.mid.append(f'<div class="abs navy-side" id="{s}-rr" style="{box(DX[1], RAIL_Y, DX[2] - DX[1], 8)}border-radius:4px"></div>')
    for k, cx in enumerate(DX):
        S.mid.append(f'<div class="abs" id="{s}-drop{k}" style="{box(cx - 3, RAIL_Y + 4, 6, 70)}background:linear-gradient(90deg,#3a6299,#1c3354)"></div>')
        S.mid.append(f'<div class="abs por" style="{box(cx - 14, RAIL_Y - 6, 28, 20)}border-radius:6px"></div>')
    S.mid.append(rivets_line(DX[0] + 40, RAIL_Y + 4, DX[2] - 40, RAIL_Y + 4, 12))
    for k in range(3):  # light pulses along the rail
        S.mid.append(f'<div class="abs" id="{s}-pl{k}" style="{box(DX[1] - 14, RAIL_Y - 10, 28, 28)}border-radius:50%;background:#ffffff;box-shadow:0 0 14px 6px rgba(203,219,244,.95)"></div>')

    # ------------------------------------------------------------ D1 learning board
    x0 = DX[0]
    d1 = [pedestal(f"{s}-p1", x0, 1270, 420, depth=70)]
    d1.append(f'<div class="abs" id="{s}-d1" style="{box(x0 - 200, 926, 400, 380)}">'
              f'<div class="abs por" style="{box(40, 300, 14, 72)}border-radius:6px"></div><div class="abs por" style="{box(346, 300, 14, 72)}border-radius:6px"></div>'
              f'<div class="abs por" style="{box(0, 0, 400, 310)}border-radius:20px"></div>'
              f'<div class="abs grid-paper" style="{box(18, 40, 364, 252)}border-radius:10px;box-shadow:inset 0 0 0 1.5px rgba(172,198,231,.8)"></div>'
              f'<div class="abs navy-side" style="{box(18, 14, 364, 18)}border-radius:8px"></div>'
              f'<div class="abs" style="{box(40, 64, 150, 10)}border-radius:5px;background:#294b77"></div>'
              f'<div class="abs" style="{box(40, 84, 110, 8)}border-radius:4px;background:#acc6e7"></div>'
              f'<div class="abs" style="{box(40, 100, 130, 8)}border-radius:4px;background:#acc6e7"></div>'
              + "".join(f'<div class="abs" id="{s}-b{k}" style="{box(220 + k * 46, 270 - hh, 32, hh)}border-radius:6px 6px 2px 2px;background:{c}"></div>'
                        for k, (hh, c) in enumerate(((70, "#acc6e7"), (120, "#3a6299"), (180, "#1c3354"))))
              + f'<div class="abs" style="{box(206, 270, 150, 3)}background:#294b77"></div>'
              f'<div class="abs" id="{s}-ptr" style="{box(70, 196, 150, 6)}border-radius:3px;background:linear-gradient(90deg,#c3d5ee,#294b77)">'
              f'<div class="abs" style="{box(140, -5, 16, 16)}border-radius:50%;background:#9fd8c4"></div></div>'
              f'{screws_rect(0, 0, 400, 310, inset=12, size=9)}</div>')
    S.mid.extend(d1)

    # ------------------------------------------------------------ D2 rotating product stand
    x1 = DX[1]
    d2 = [pedestal(f"{s}-p2", x1, 1260, 400, depth=80)]
    d2.append(f'<svg class="abs" style="left:{x1 - 170}px;top:1266px;overflow:visible" width="340" height="80" viewBox="0 0 340 80">'
              f'<ellipse id="{s}-tt" cx="170" cy="40" rx="150" ry="30" fill="none" stroke="#294b77" stroke-width="3" stroke-dasharray="6 22" stroke-linecap="round"/></svg>')
    d2.append(f'<svg class="abs" id="{s}-beam" style="left:{x1 - 200}px;top:900px;overflow:visible" width="400" height="420" viewBox="0 0 400 420">'
              f'<defs><linearGradient id="{s}-bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity=".95"/><stop offset="1" stop-color="#e8f0fb" stop-opacity="0"/></linearGradient></defs>'
              f'<polygon points="150,0 250,0 380,400 20,400" fill="url(#{s}-bg)"/></svg>')
    d2.append(f'<div class="abs por" style="{box(x1 - 60, 880, 120, 30)}border-radius:10px 10px 30px 30px"></div>')
    d2.append(f'<div class="abs" id="{s}-prw" style="{box(x1 - 70, 1056, 140, 240)}">{bottle(f"{s}-pr", 15, 0, 110, 230)}</div>')
    d2.append(shadow(x1 - 90, 1280, 180, 34, 0.9))
    S.mid.extend(d2)

    # ------------------------------------------------------------ D3 campaign billboard
    x2 = DX[2]
    d3 = [pedestal(f"{s}-p3", x2, 1270, 420, depth=70)]
    d3.append(f'<div class="abs" id="{s}-lg" style="{box(x2 - 150, 1150, 300, 150)}">'
              f'<div class="abs por" style="{box(30, 0, 16, 150)}border-radius:6px"></div><div class="abs por" style="{box(254, 0, 16, 150)}border-radius:6px"></div>'
              f'<div class="abs por-dim" style="{box(30, 70, 240, 10)}border-radius:5px"></div></div>')
    bb = (f'<div class="abs navy-side" style="{box(0, 0, 440, 300)}border-radius:22px;box-shadow:0 22px 34px -16px rgba(28,51,84,.45)"></div>'
          f'<div class="abs" style="{box(16, 16, 408, 268)}border-radius:14px;background:linear-gradient(160deg,#fbfcfe,#e3ebf7)"></div>'
          f'<div class="abs" style="{box(36, 36, 180, 228)}border-radius:12px;background:linear-gradient(150deg,#cbdbf4,#acc6e7)"></div>'
          f'<div class="abs" style="{box(150, 60, 70, 70)}border-radius:50%;background:#9fd8c4"></div>'
          + bottle(f"{s}-bb", 70, 70, 96, 190) +
          f'<div class="abs" style="{box(244, 70, 150, 14)}border-radius:7px;background:#294b77"></div>'
          f'<div class="abs" style="{box(244, 96, 120, 10)}border-radius:5px;background:#acc6e7"></div>'
          f'<div class="abs" style="{box(244, 116, 136, 10)}border-radius:5px;background:#acc6e7"></div>'
          f'<div class="abs" style="{box(244, 214, 110, 40)}border-radius:20px;background:#294b77"></div>'
          f'{screws_rect(0, 0, 440, 300, inset=10, size=9)}')
    d3.append(f'<div class="abs" id="{s}-bbw" style="{box(x2 - 220, 870, 440, 300)}">{bb}</div>')
    for k in range(3):
        lx = x2 - 150 + k * 150
        d3.append(f'<div class="abs por" style="{box(lx - 4, 846, 8, 28)}border-radius:4px"></div>')
        d3.append(f'<div class="led" id="{s}-lp{k}" style="left:{lx - 6}px;top:838px"></div>')
    S.mid.extend(d3)

    # ------------------------------------------------------------ near: out-of-focus foreground glass rods
    near = []
    for k, (nx, ny, w, h) in enumerate(((980, 560, 30, 380), (1660, 1380, 260, 26), (2360, 640, 26, 340), (240, 600, 200, 200))):
        if k == 3:
            near.append(f'<div class="abs" style="{box(nx, ny, w, h)}border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"></div>')
        else:
            near.append(f'<div class="abs" style="{box(nx, ny, w, h)}border-radius:14px;background:linear-gradient(90deg,#ffffff,#cbdbf4);opacity:.85;filter:blur(4px)"></div>')
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">{"".join(near)}</div>')
    apex(S, S.mid, f"{s}-ap", x2, 1020, wIkl, size=620, sparks=7, seed=13)

    # ============================================================ motion
    # camera: on the machine -> track D1 -> D2 -> D3 -> pull back to the family
    S.cam([(S.t0, {"x": -700, "y": 40, "z": 560, "rotationY": 0, "rotationX": 0}, None),
           (wKer - 0.05, {"z": 640, "y": 30}, "sine.inOut"),
           (wEdu - 0.62, {"z": 300, "y": 0}, "power2.inOut"),
           (wEdu - 0.08, {"x": 0, "y": -110, "z": 60, "rotationY": 3}, "power3.inOut"),
           (wPromo - 0.35, {"x": 30, "z": 90, "rotationY": 1.5}, "sine.inOut"),
           (wPromo - 0.02, {"x": -700, "z": 60, "rotationY": -2}, "power3.inOut"),
           (wIkl - 0.5, {"x": -730, "z": 90, "rotationY": -1}, "sine.inOut"),
           (wIkl - 0.08, {"x": -1400, "z": 60, "rotationY": 2}, "power3.inOut"),
           (wIkl + 0.32, {"x": -1420, "z": 90, "rotationY": 0}, "sine.out"),
           (S.t1 - 0.1, {"x": -700, "y": 210, "z": -1300, "rotationY": 0}, "power3.inOut"),
           (S.t1, {"z": -1270}, "sine.out")])
    # leds: off until the cartridge locks
    for k in range(3):
        S.init(f"#{s}-mlo{k}", {"opacity": 0})
        S.ft(f"#{s}-mlo{k}", {"opacity": 0}, {"opacity": 1}, wPro + 0.25 + k * 0.08, 0.12, "power2.out")
    S.keys(f"#{s}-dl-nd", [(S.t0, {"rotation": -110, "transformOrigin": "50% 100%"}, None),
                          (wPro + 0.3, {"rotation": -20}, "back.out(1.6)"),
                          (wKer + 0.3, {"rotation": 85}, "back.out(1.4)"),
                          (wIkl + 0.2, {"rotation": 92}, "sine.inOut"),
                          (S.t1, {"rotation": 88}, "sine.inOut")])
    # cartridge drop into the slot
    S.init(f"#{s}-cart", {"y": -110, "opacity": 0})
    S.ft(f"#{s}-cart", {"y": -110, "opacity": 0}, {"y": 8, "opacity": 1}, wPro - 0.55, 0.4, "power2.out")
    S.ft(f"#{s}-cart", {"y": 8, "opacity": 1}, {"y": 120, "opacity": 1}, wPro - 0.05, 0.3, "power3.in")
    # skeleton draws on "kerangka"
    for k in range(3):
        S.init(f"#{s}-sk{k}", {"opacity": 0, "scale": 0.86})
        S.ft(f"#{s}-sk{k}", {"opacity": 0, "scale": 0.86}, {"opacity": 1, "scale": 1}, wKer - 0.05 + k * 0.09, 0.32, "back.out(2)")
    S.init(f"#{s}-skr", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-skr", {"scaleX": 0}, {"scaleX": 1}, wKer + 0.1, 0.4, "power3.out")
    S.init(f"#{s}-wrefl", {"x": 0})
    S.ft(f"#{s}-wrefl", {"x": 0}, {"x": 300}, wKer, 0.6, "power2.inOut")
    # rail draws out from the machine, drops extend
    S.init(f"#{s}-rl", {"scaleX": 0, "transformOrigin": "100% 50%"})
    S.ft(f"#{s}-rl", {"scaleX": 0}, {"scaleX": 1}, wKer + 0.25, 0.55, "power3.inOut")
    S.init(f"#{s}-rr", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-rr", {"scaleX": 0}, {"scaleX": 1}, wKer + 0.25, 0.55, "power3.inOut")
    for k, at in enumerate((wEdu - 0.2, wPromo - 0.2, wIkl - 0.2)):
        S.init(f"#{s}-drop{k}", {"scaleY": 0, "transformOrigin": "50% 0%"})
        S.ft(f"#{s}-drop{k}", {"scaleY": 0}, {"scaleY": 1}, at, 0.2, "power2.out")
    # pulses ride the rail into each diorama
    for k, (dx, at) in enumerate(((DX[0] - DX[1], wEdu - 0.55), (0, wPromo - 0.4), (DX[2] - DX[1], wIkl - 0.55))):
        S.init(f"#{s}-pl{k}", {"opacity": 0, "x": 0, "y": 0, "scale": 0.6})
        S.ft(f"#{s}-pl{k}", {"opacity": 0, "x": 0, "y": -40, "scale": 0.6}, {"opacity": 1, "x": dx, "y": 0, "scale": 1}, at, 0.4, "power2.inOut")
        S.ft(f"#{s}-pl{k}", {"opacity": 1, "x": dx, "y": 0, "scale": 1}, {"opacity": 0, "x": dx, "y": 70, "scale": 0.5}, at + 0.4, 0.16, "power2.in")

    # D1 learning board hinges up on "edukasi"
    S.init(f"#{s}-d1", {"rotationX": -82, "transformOrigin": "50% 100%", "opacity": 0.0, "transformPerspective": 900})
    S.ft(f"#{s}-d1", {"rotationX": -82, "opacity": 0}, {"rotationX": 0, "opacity": 1}, wEdu - 0.12, 0.55, "back.out(1.5)")
    for k in range(3):
        S.init(f"#{s}-b{k}", {"scaleY": 0, "transformOrigin": "50% 100%"})
        S.ft(f"#{s}-b{k}", {"scaleY": 0}, {"scaleY": 1}, wEdu + 0.25 + k * 0.1, 0.4, "back.out(1.8)")
    S.keys(f"#{s}-ptr", [(S.t0, {"rotation": 18, "transformOrigin": "0% 50%"}, None),
                         (wEdu + 0.55, {"rotation": -16}, "back.out(2)"),
                         (S.t1, {"rotation": -12}, "sine.inOut")])
    # D2 product drops onto the turntable on "promo"; turntable + gloss keep rotating
    S.init(f"#{s}-prw", {"y": -340, "opacity": 0})
    S.ft(f"#{s}-prw", {"y": -340, "opacity": 0}, {"y": 0, "opacity": 1}, wPromo - 0.2, 0.42, "bounce.out")
    S.init(f"#{s}-beam", {"opacity": 0})
    S.ft(f"#{s}-beam", {"opacity": 0}, {"opacity": 0.95}, wPromo - 0.05, 0.3, "power2.out")
    S.init(f"#{s}-tt", {"strokeDashoffset": 0})
    S.ft(f"#{s}-tt", {"strokeDashoffset": 0}, {"strokeDashoffset": -280}, wPromo - 0.1, S.t1 - wPromo + 0.1, "none")
    S.init(f"#{s}-pr-gl", {"x": 0})
    for k in range(3):
        a = wPromo + 0.25 + k * 0.5
        if a < S.t1:
            S.ft(f"#{s}-pr-gl", {"x": 0}, {"x": 190}, a, 0.48, "sine.inOut")
    # D3 billboard: legs rise, panel flips down on "iklan", lamps light
    S.init(f"#{s}-lg", {"scaleY": 0, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-lg", {"scaleY": 0}, {"scaleY": 1}, wIkl - 0.4, 0.3, "power3.out")
    S.init(f"#{s}-bbw", {"rotationX": 92, "transformOrigin": "50% 100%", "opacity": 0, "transformPerspective": 900})
    S.ft(f"#{s}-bbw", {"rotationX": 92, "opacity": 0}, {"rotationX": 0, "opacity": 1}, wIkl - 0.18, 0.5, "back.out(1.6)")
    for k in range(3):
        S.init(f"#{s}-lp{k}", {"opacity": 0, "scale": 0.4})
        S.ft(f"#{s}-lp{k}", {"opacity": 0, "scale": 0.4}, {"opacity": 1, "scale": 1}, wIkl + 0.15 + k * 0.08, 0.2, "back.out(2.5)")
