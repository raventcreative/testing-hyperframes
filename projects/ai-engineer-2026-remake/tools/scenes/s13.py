"""S13 — PILIH JALUR (W185 – W198). VO: "Setelah itu, pilih jalur. Mau membangun produk AI? Atau mendalami modelnya sampai
level training?"
Opens on the finished machine casing exactly at kit.MACHINE (the S12 hand-off). DEMONSTRATE: the mascot stands at the
master selector lever under the machine; on "pilih" he pulls it, on "jalur" the base rail splits left/right, the machine
lifts and settles smaller and two bays slide in: LEFT = PRODUK AI (API / RAG / agent / eval tiles in a navy enamel bay),
RIGHT = MODEL (training curve + gear in a porcelain workshop). One core anchors both. EXPLAIN MODE for the question: he comes
forward, the set goes soft, chips PRODUK AI / TRAINING pop in the band on their words while each bay glows behind him.
He steps back to the lever; both routes stay lit on the rail at y = STAGE_RAIL_Y (-> S14 rail)."""
from xk import box, r3
from kit import (MACHINE, STAGE_RAIL_Y, FLOOR_Y, MAT, part, cable, grid_floor, shadow, blur_wrap, explain, chip, ICON, EXPLAIN_BAND)
from kit_d import label, icon_tile, orb

MX, MY, MW, MH = MACHINE
MCX = MX + MW / 2
LEV = (720, 1440)          # lever pivot
SHRINK = 0.72
BAY_L = (20, 770, 290, 540)
BAY_R = (770, 770, 290, 540)


def machine_html(s):
    lamps = "".join(f'<div class="abs" style="left:{r3(70 + k * 48)}px;top:{MH - 92}px;width:22px;height:22px;border-radius:50%;'
                    f'background:radial-gradient(circle at 40% 35%,#9fc4ff,#294B77 70%);box-shadow:0 0 0 3px rgba(255,255,255,.7)"></div>'
                    for k in range(10))
    inner = (part(None, 40, 40, MW - 80, 380, "enamel", 30,
                  inner=f'<div class="abs" style="left:{MW / 2 - 40 - 150}px;top:40px;width:300px;height:300px;border-radius:50%;{MAT["glass"]}"></div>'
                        + orb(f"{s}-orb", MW / 2 - 40, 190, 170))
             + part(None, 40, 450, MW - 80, 150, "alu", 18,
                    inner='<div class="abs" style="left:24px;top:30px;width:200px;height:16px;border-radius:8px;background:rgba(10,13,44,.25)"></div>'
                          '<div class="abs" style="left:24px;top:62px;width:300px;height:16px;border-radius:8px;background:rgba(10,13,44,.18)"></div>'
                          '<div class="abs" style="left:24px;top:94px;width:150px;height:16px;border-radius:8px;background:rgba(10,13,44,.18)"></div>')
             + lamps)
    return part(f"{s}-mach", MX, MY, MW, MH, "porcelain", 40, inner=inner)


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    RY = STAGE_RAIL_Y
    # ---------------------------------------------------------------- back
    S.back.append(grid_floor(f"{s}-grid"))
    # bays (hidden off-side at first, slide in on "jalur")
    bl = BAY_L
    tiles_l = "".join(icon_tile(f"{s}-lt{k}", 26 + (k % 2) * 124, 70 + (k // 2) * 140, 110, 120, ic, color="#ffffff", mat="glass")
                      for k, ic in enumerate(("plug", "doc", "tool", "check")))
    S.back.append(f'<div class="abs" id="{s}-bayl" style="{box(*bl)}">'
                  + part(None, 0, 0, bl[2], bl[3], "enamel", 28, inner=tiles_l
                         + label(None, 0, 382, bl[2], "PRODUK AI", 34, "#fff")
                         + label(None, 0, 428, bl[2], "API · RAG · AGENT", 24, "rgba(255,255,255,.75)", weight=400))
                  + f'<div class="abs" id="{s}-glowl" style="left:-14px;top:-14px;width:{bl[2] + 28}px;height:{bl[3] + 28}px;border-radius:38px;'
                    f'box-shadow:0 0 0 5px #9fc4ff,0 0 40px 8px rgba(120,170,240,.55)"></div></div>')
    br = BAY_R
    curve = (f'<svg class="abs" style="left:24px;top:60px;width:{br[2] - 48}px;height:200px;overflow:visible" viewBox="0 0 242 200">'
             f'<path d="M0 0 V200 H242" fill="none" stroke="#294B77" stroke-width="3" opacity=".5"/>'
             f'<path id="{s}-loss" d="M8 20 C 50 120, 90 150, 140 168 S 220 182, 236 184" fill="none" stroke="#0A0D2C" stroke-width="7" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')
    gear = (f'<svg class="abs" id="{s}-gear" style="left:{br[2] / 2 - 50}px;top:276px;width:100px;height:100px" viewBox="-50 -50 100 100">'
            + "".join(f'<rect x="-9" y="-48" width="18" height="22" rx="4" fill="#294B77" transform="rotate({k * 45})"/>' for k in range(8))
            + '<circle r="32" fill="#294B77"/><circle r="13" fill="#eef3fa"/></svg>')
    S.back.append(f'<div class="abs" id="{s}-bayr" style="{box(*br)}">'
                  + part(None, 0, 0, br[2], br[3], "porcelain", 28, inner=curve + gear
                         + label(None, 0, 392, br[2], "MODEL", 34)
                         + label(None, 0, 438, br[2], "TRAINING", 24, "#294B77", weight=400))
                  + f'<div class="abs" id="{s}-glowr" style="left:-14px;top:-14px;width:{br[2] + 28}px;height:{br[3] + 28}px;border-radius:38px;'
                    f'box-shadow:0 0 0 5px #294B77,0 0 40px 8px rgba(41,75,119,.45)"></div></div>')
    # rails: one cable from the machine base splitting left and right along the stage rail
    lx, rx = bl[0] + bl[2] / 2, br[0] + br[2] / 2
    S.back.append(f'<div class="abs" id="{s}-rails" style="left:0;top:0;width:1080px;height:1920px">'
                  + cable(f"{s}-rl", f"M{MCX},{MY + MH + 40} L{MCX},{RY} L{lx},{RY} L{lx},{bl[1] + bl[3]}", w=10)
                  + cable(f"{s}-rr", f"M{MCX},{MY + MH + 40} L{MCX},{RY} L{rx},{RY} L{rx},{br[1] + br[3]}", w=10) + "</div>")
    S.back.append(shadow(MX + 40, MY + MH - 30, MW - 80, 80, 0.55, f"{s}-msh"))
    S.back.append(machine_html(s))
    # plinth + master selector lever
    S.back.append(part(f"{s}-plinth", MX - 20, MY + MH - 6, MW + 40, 52, "alu", 14))
    S.back.append(f'<div class="abs" id="{s}-lev" style="left:{LEV[0] - 14}px;top:{LEV[1] - 150}px;width:28px;height:150px">'
                  f'<div class="abs" style="left:4px;top:24px;width:20px;height:126px;border-radius:10px;{MAT["alu"]}"></div>'
                  f'<div class="abs" style="left:-16px;top:-6px;width:60px;height:46px;border-radius:23px;{MAT["enamel"]}"></div></div>')
    S.back.append(part(None, LEV[0] - 50, LEV[1] - 10, 100, 40, "rubber", 12))
    blur_wrap(S)
    # ---------------------------------------------------------------- front: explain chips (band)
    y0 = EXPLAIN_BAND[0] + 22
    S.front.append(chip(f"{s}-c1", 70, y0, "PRODUK AI", ICON["chat"], size=34))
    S.front.append(label(f"{s}-or", 440, y0 + 16, 200, "atau", 34, "#294B77", weight=400))
    S.front.append(chip(f"{s}-c2", 650, y0, "TRAINING", ICON["gauge"], size=34, dark=True))

    # ---------------------------------------------------------------- motion
    pil, jal = W(187), W(188)
    # lever pull on "pilih" (anticipation back, then pull through, settle)
    S.init(f"#{s}-lev", {"rotation": -28, "transformOrigin": "14px 150px"})
    S.ft(f"#{s}-lev", {"rotation": -28}, {"rotation": -36}, pil - 0.25, 0.2, "power2.out")
    S.ft(f"#{s}-lev", {"rotation": -36}, {"rotation": 32}, pil - 0.05, 0.22, "power3.in")
    S.ft(f"#{s}-lev", {"rotation": 32}, {"rotation": 26}, pil + 0.17, 0.25, "back.out(3)")
    S.fx(pil + 0.15, "click", 0.08)
    # machine lifts a touch and settles smaller (keeps its centre x = the core); shadow follows
    S.init(f"#{s}-mach", {"scale": 1, "y": 0, "transformOrigin": f"{MW / 2}px 0px"})
    S.ft(f"#{s}-mach", {"scale": 1, "y": 0}, {"scale": 1.02, "y": -14}, pil + 0.15, max(0.05, min(0.2, jal - 0.06 - pil - 0.15)), "power2.out")
    S.ft(f"#{s}-mach", {"scale": 1.02, "y": -14}, {"scale": SHRINK, "y": 10}, jal - 0.05, 0.55, "power3.inOut")
    for sel in (f"#{s}-msh", f"#{s}-plinth"):
        S.init(sel, {"scaleX": 1, "transformOrigin": "50% 50%"})
        S.ft(sel, {"scaleX": 1}, {"scaleX": SHRINK}, jal - 0.05, 0.55, "power3.inOut")
    S.init(f"#{s}-msh", {"y": 0, "scaleX": 1})
    S.ft(f"#{s}-msh", {"y": 0}, {"y": -(MH * (1 - SHRINK)) + 10}, jal - 0.05, 0.55, "power3.inOut")
    S.init(f"#{s}-plinth", {"y": 0, "scaleX": 1})
    S.ft(f"#{s}-plinth", {"y": 0}, {"y": -(MH * (1 - SHRINK)) + 16}, jal - 0.05, 0.55, "power3.inOut")
    # rails split, bays slide in from the sides on their rails
    S.init(f"#{s}-rails", {"opacity": 0})
    S.ft(f"#{s}-rails", {"opacity": 0}, {"opacity": 1}, jal - 0.04, 0.12, "none")
    for sel in (f"#{s}-rl", f"#{s}-rr"):
        S.init(sel, {"attr": {"stroke-dashoffset": 1}})
        S.ft(sel, {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, jal - 0.02, 0.5, "power2.inOut")
    for sel, dx in ((f"#{s}-bayl", -340), (f"#{s}-bayr", 340)):
        S.init(sel, {"x": dx, "opacity": 0})
        S.ft(sel, {"x": dx, "opacity": 0}, {"x": 0, "opacity": 1}, jal + 0.1, 0.55, "power3.out")
    S.fx(jal + 0.1, "whoosh", 0.05)
    # bays light on their words; the other dims a little
    pro, tra = W(191), W(198)
    S.init(f"#{s}-glowl", {"opacity": 0}); S.init(f"#{s}-glowr", {"opacity": 0})
    S.ft(f"#{s}-glowl", {"opacity": 0}, {"opacity": 1}, pro - 0.05, 0.3, "power2.out")
    S.ft(f"#{s}-glowl", {"opacity": 1}, {"opacity": 0.45}, W(193), 0.4, "power2.inOut")
    S.ft(f"#{s}-glowr", {"opacity": 0}, {"opacity": 1}, tra - 0.05, 0.3, "power2.out")
    for k in range(4):
        S.init(f"#{s}-lt{k}", {"scale": 1})
        S.ft(f"#{s}-lt{k}", {"scale": 1}, {"scale": 1.12}, pro + 0.05 + k * 0.08, 0.15, "power2.out")
        S.ft(f"#{s}-lt{k}", {"scale": 1.12}, {"scale": 1}, pro + 0.2 + k * 0.08, 0.25, "power2.out")
    S.init(f"#{s}-loss", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-loss", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(194), tra - W(194) + 0.4, "power2.inOut")
    S.init(f"#{s}-gear", {"rotation": 0, "transformOrigin": "50px 50px"})
    S.ft(f"#{s}-gear", {"rotation": 0}, {"rotation": 135}, W(194), t1 - W(194), "power1.inOut")
    S.init(f"#{s}-orb", {"filter": "brightness(1)"})
    S.ft(f"#{s}-orb", {"filter": "brightness(1)"}, {"filter": "brightness(1.3)"}, jal, 0.3, "power2.out")
    S.ft(f"#{s}-orb", {"filter": "brightness(1.3)"}, {"filter": "brightness(1.05)"}, jal + 0.4, 0.6, "sine.inOut")
    # hand-off: in the last beat the bays and the machine sink away; the rail along STAGE_RAIL_Y stays (-> S14 opens on it)
    for k, sel in enumerate((f"#{s}-bayl", f"#{s}-bayr", f"#{s}-mach", f"#{s}-plinth", f"#{s}-lev", f"#{s}-msh")):
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, t1 - 0.34 + k * 0.02, 0.28, "power2.in")
    # explain chips
    S.init(f"#{s}-c1", {"opacity": 0, "y": 26, "scale": 0.85, "rotation": -3})
    S.ft(f"#{s}-c1", {"opacity": 0, "y": 26, "scale": 0.85}, {"opacity": 1, "y": 0, "scale": 1}, pro - 0.05, 0.4, "back.out(2)")
    S.init(f"#{s}-or", {"opacity": 0, "y": 10})
    S.ft(f"#{s}-or", {"opacity": 0, "y": 10}, {"opacity": 1, "y": 0}, W(193) - 0.05, 0.3, "power2.out")
    S.init(f"#{s}-c2", {"opacity": 0, "y": 26, "scale": 0.85, "rotation": 3})
    S.ft(f"#{s}-c2", {"opacity": 0, "y": 26, "scale": 0.85}, {"opacity": 1, "y": 0, "scale": 1}, tra - 0.05, 0.4, "back.out(2)")
    S.fx(pro, "pop", 0.05)
    S.fx(tra, "pop", 0.05)

    # ---------------------------------------------------------------- mascot
    lever = {"fx": 430, "fy": 1790, "h": 730, "yaw": -22, "pitch": 6}     # at the lever, turned to it
    t_in = W(189) - 0.32
    t_out = t1 - 0.5
    S.mv([(t0, dict(lever, yaw=-10), None), (pil - 0.3, lever, "sine.inOut"), (pil + 0.1, dict(lever, fy=1800, yaw=-28), "power2.out"),
          (t_in, dict(lever, yaw=0), "power2.inOut")])
    explain(S, t_in, t_out, 189, 198, seed=2, enter=dict(lever, yaw=0), leave=dict(lever, yaw=0))
    S.ft(f"#{s}-c1", {"opacity": 1}, {"opacity": 0}, t_out - 0.05, 0.25, "power2.in")
    S.ft(f"#{s}-or", {"opacity": 1}, {"opacity": 0}, t_out - 0.05, 0.25, "power2.in")
    S.ft(f"#{s}-c2", {"opacity": 1}, {"opacity": 0}, t_out - 0.05, 0.25, "power2.in")
    # lever acting: reach, grip, pull through; then look at the two routes as they arrive
    S.act("armL", [(t0, "low", 0.3), (pil - 0.45, "present", 0.3), (pil - 0.08, "fist", 0.18), (jal + 0.2, "low", 0.4)])
    S.act("armR", [(t0, "low", 0.3), (pil - 0.4, "explain", 0.35), (jal + 0.25, "low", 0.4)])
    S.act("head", [(t0, [0.1, 0.2, 0], 0.3), (pil - 0.4, [0.2, 0.3, 0], 0.35), (jal, [-0.04, -0.35, -0.03], 0.35), (jal + 0.35, [-0.04, 0.35, 0.03], 0.35)])
    S.act("torso", [(pil - 0.1, {"chest": [0.06, 0.12, 0]}, 0.2), (jal + 0.2, {}, 0.4)])
