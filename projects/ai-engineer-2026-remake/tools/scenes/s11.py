"""S11 — 09 EVALUATION. VO: "Kesembilan, evaluation. Tes pakai kasus sulit. Cari bagian yang gagal. Perbaiki. Lalu tes lagi."
Opens on S10's hand-off: the loop wheel is now at the gauge spot and its pointer is the needle; the robot sits in the
test-bench slot. Ticks draw on, a test bench rises. EXPLAIN MODE on "Tes pakai kasus sulit" (TES + KASUS SULIT chips,
three test cartridges load behind him). Back at the bench: the needle sweeps, falls into the fail zone on "gagal" and a
muted-coral ERROR lamp lights inside the instrument (only there). "Perbaiki": the mascot pulls the faulty side module,
a fresh one clicks in. "tes lagi": the needle sweeps into the pass zone, pass lamp, a check sticker stamps onto the
robot. Hand-off: gauge + bench fall away, the passed robot stays on its spot (S12 lifts it into the production casing)."""
import math
from xk import box, r3
from kit import MAT, part, shadow, chip, grid_floor, blur_wrap, explain, ICON, EXPLAIN_BAND
from kit_c import G11, B11, WHEEL_D, HUB_D, DEMO_R, pol, wheel, pointer, hub, label

CORAL = "#d9776a"
BENCH = (130, 1250, 660, 230)      # x y w h (porcelain test bench)
MOD = (B11[0] + 62, B11[1] - 26, 64, 52)   # side module on the robot (x y w h)


def arc(c, r, a0, a1):
    x0, y0 = pol(c, r, a0)
    x1, y1 = pol(c, r, a1)
    big = 1 if (a1 - a0) > 180 else 0
    return f"M{r3(x0)},{r3(y0)} A{r},{r} 0 {big} 1 {r3(x1)},{r3(y1)}"


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    gx, gy = G11
    # ---------------------------------------------------------------- back
    S.back.append(grid_floor(f"{s}-grid"))
    # gauge: the S10 wheel + ticks + zones + an instrument window with ERROR / PASS lamps
    S.back.append(wheel(f"{s}-wheel", G11))
    ticks = "".join(
        f'<line x1="{r3(pol(G11, 196, a)[0])}" y1="{r3(pol(G11, 196, a)[1])}" x2="{r3(pol(G11, 196 - (22 if k % 3 == 0 else 12), a)[0])}" '
        f'y2="{r3(pol(G11, 196 - (22 if k % 3 == 0 else 12), a)[1])}" stroke="#294B77" stroke-width="{5 if k % 3 == 0 else 3}" stroke-linecap="round"/>'
        for k, a in enumerate(range(-135, 136, 15)))
    S.back.append(f'<svg class="abs" id="{s}-ticks" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">{ticks}'
                  f'<path id="{s}-zf" d="{arc(G11, 214, -135, -70)}" fill="none" stroke="{CORAL}" stroke-width="10" stroke-linecap="round" opacity=".75"/>'
                  f'<path id="{s}-zp" d="{arc(G11, 214, 65, 135)}" fill="none" stroke="#1c3561" stroke-width="12" stroke-linecap="round"/></svg>')
    S.back.append(f'<div class="abs" id="{s}-win" style="{box(gx - 120, gy + 92, 240, 74)}border-radius:20px;{MAT["enamel"]}">'
                  f'<div class="abs" id="{s}-err" style="left:14px;top:14px;width:118px;height:46px;border-radius:12px;background:{CORAL};'
                  f'box-shadow:0 0 18px rgba(217,119,106,.75);font:700 22px/46px Poppins;color:#fff;text-align:center;letter-spacing:.06em">ERROR</div>'
                  f'<div class="abs" style="left:14px;top:14px;width:118px;height:46px;border-radius:12px;border:2px solid rgba(255,255,255,.18)"></div>'
                  f'<div class="abs" id="{s}-pass" style="left:146px;top:10px;width:80px;height:54px;border-radius:14px;background:linear-gradient(135deg,#9fc4ff,#ffffff);'
                  f'box-shadow:0 0 20px rgba(159,196,255,.95);color:#0A0D2C;padding:9px 20px">{ICON["check"]}</div>'
                  f'<div class="abs" style="left:146px;top:10px;width:80px;height:54px;border-radius:14px;border:2px solid rgba(255,255,255,.18)"></div></div>')
    S.back.append(pointer(f"{s}-ptr", G11))
    S.back.append(f'<div class="abs" id="{s}-cap" style="{box(gx - 26, gy - 26, 52, 52)}border-radius:50%;{MAT["alu"]}"></div>')
    # test bench: porcelain body, cable up to the gauge, three cartridge slots, the robot slot
    bx, by, bw, bh = BENCH
    S.back.append(f'<svg class="abs" id="{s}-cab" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path d="M{gx},{gy + 258} C{gx},{by - 40} {gx - 120},{by - 60} {gx - 120},{by + 10}" fill="none" stroke="#1c3561" stroke-width="9" stroke-linecap="round"/></svg>')
    S.back.append(shadow(bx - 20, by + bh - 40, bw + 40, 90, 0.5, f"{s}-bsh"))
    slots = "".join(f'<div class="abs" style="left:{20 + k * 80}px;top:52px;width:66px;height:120px;border-radius:12px;background:radial-gradient(circle at 50% 30%,#2a3446,#0b1020);'
                    f'box-shadow:inset 0 4px 8px rgba(0,0,0,.6)"></div>' for k in range(3))
    S.back.append(f'<div class="abs" id="{s}-bench" style="{box(bx, by, bw, bh)}border-radius:26px;{MAT["porcelain"]}">{slots}'
                  f'<div class="abs" style="left:{B11[0] - bx - 96}px;top:30px;width:192px;height:150px;border-radius:30px;background:rgba(41,75,119,.10);'
                  f'box-shadow:inset 0 3px 8px rgba(41,75,119,.2)"></div></div>')
    for k in range(3):
        S.back.append(f'<div class="abs" id="{s}-k{k}" style="{box(bx + 20 + k * 80, by + 30, 66, 120)}border-radius:12px;{MAT["enamel"]}'
                      f'font:700 30px/1 Poppins;color:#fff;text-align:center;padding-top:44px">{k + 1}'
                      f'<div class="abs" id="{s}-k{k}b" style="inset:-5px;border-radius:15px;border:5px solid {CORAL};box-shadow:0 0 16px rgba(217,119,106,.6)"></div></div>')
    # the robot (from S10) with its side module (faulty, then replaced) and the pass sticker
    d = HUB_D * 0.8
    S.back.append(shadow(B11[0] - 90, B11[1] + 50, 180, 44, 0.5))
    mx, my, mw, mh = MOD
    S.back.append(part(f"{s}-mod", mx, my, mw, mh, "alu", 10,
                       inner=f'<div class="abs" id="{s}-modg" style="inset:0;border-radius:10px;background:{CORAL};opacity:0;box-shadow:0 0 16px rgba(217,119,106,.8)"></div>'))
    S.back.append(part(f"{s}-mod2", mx, my, mw, mh, "enamel", 10,
                       inner='<div class="abs" style="left:12px;top:20px;width:40px;height:8px;border-radius:4px;background:#9fc4ff"></div>'))
    S.back.append(hub(f"{s}-hub", B11, d=d, sticker=True, sid=f"{s}-stk"))
    blur_wrap(S)
    # explain visuals
    ey = EXPLAIN_BAND[0] + 26
    S.front.append(chip(f"{s}-c1", 170, ey, "TES", ICON["check"], size=36))
    S.front.append(chip(f"{s}-c2", 480, ey, "KASUS SULIT", ICON["bug"], size=36, dark=True))

    # ---------------------------------------------------------------- motion
    # gauge face comes alive (ticks + zones) and the bench rises into frame
    S.init(f"#{s}-ticks", {"opacity": 0, "scale": 0.92, "transformOrigin": f"{gx}px {gy}px"})
    S.ft(f"#{s}-ticks", {"opacity": 0, "scale": 0.92}, {"opacity": 1, "scale": 1}, t0 + 0.08, 0.45, "power3.out")
    S.init(f"#{s}-win", {"opacity": 0, "y": 20})
    S.ft(f"#{s}-win", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, W(162) - 0.1, 0.4, "power3.out")
    for sel in (f"#{s}-bench", f"#{s}-cab", f"#{s}-bsh"):
        S.init(sel, {"y": 300, "opacity": 0})
        S.ft(sel, {"y": 300, "opacity": 0}, {"y": 0, "opacity": 1}, t0 + 0.2, 0.55, "power3.out")
    S.init(f"#{s}-ptr", {"rotation": -135, "transformOrigin": "50% 100%"})
    S.init(f"#{s}-err", {"opacity": 0})
    S.init(f"#{s}-pass", {"opacity": 0})
    S.fx(t0 + 0.2, "whoosh", 0.04)
    # explain beat (cartridges load behind him)
    t_in, t_out = S.WE(162) - 0.3, W(167) - 0.3
    for sel, at in ((f"#{s}-c1", W(163) - 0.05), (f"#{s}-c2", W(165) - 0.05)):
        S.init(sel, {"opacity": 0, "y": 30, "scale": 0.8})
        S.ft(sel, {"opacity": 0, "y": 30, "scale": 0.8}, {"opacity": 1, "y": 0, "scale": 1}, at, 0.38, "back.out(2)")
        S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": -20}, t_out - 0.1, 0.25, "power2.in")
    S.fx(W(165) - 0.03, "pop", 0.05)
    for k in range(3):
        S.init(f"#{s}-k{k}", {"y": -240, "opacity": 0})
        S.ft(f"#{s}-k{k}", {"y": -240, "opacity": 0}, {"y": 0, "opacity": 1}, W(164) + k * 0.1, 0.35, "power3.in")
        S.init(f"#{s}-k{k}b", {"opacity": 0})
    # search for the failure: needle sweeps up, falls into the fail zone on "gagal"
    S.ft(f"#{s}-ptr", {"rotation": -135}, {"rotation": 35}, W(167) + 0.05, 0.55, "power2.inOut")
    S.ft(f"#{s}-ptr", {"rotation": 35}, {"rotation": -100}, W(170) - 0.08, 0.35, "power3.out")
    S.ft(f"#{s}-err", {"opacity": 0}, {"opacity": 1}, W(170), 0.08, "none")
    S.ft(f"#{s}-k1b", {"opacity": 0}, {"opacity": 1}, W(170), 0.12, "none")
    S.init(f"#{s}-modg", {"opacity": 0})
    S.ft(f"#{s}-modg", {"opacity": 0}, {"opacity": 0.85}, W(170), 0.12, "none")
    S.fx(W(170), "key", 0.06)
    # Perbaiki: faulty module out, fresh one in
    fix = W(171)
    S.init(f"#{s}-mod", {"x": 0, "y": 0, "rotation": 0, "opacity": 0})
    S.ft(f"#{s}-mod", {"opacity": 0, "x": 40}, {"opacity": 1, "x": 0}, t0 + 0.3, 0.3, "back.out(2)")
    S.ft(f"#{s}-mod", {"x": 0, "y": 0, "rotation": 0, "opacity": 1}, {"x": 70, "y": -90, "rotation": 28, "opacity": 0}, fix + 0.05, 0.4, "power2.in")
    S.init(f"#{s}-mod2", {"y": -160, "opacity": 0})
    S.ft(f"#{s}-mod2", {"y": -160, "opacity": 0}, {"y": 0, "opacity": 1}, fix + 0.35, 0.3, "back.out(2)")
    S.fx(fix + 0.62, "click", 0.07)
    S.ft(f"#{s}-err", {"opacity": 1}, {"opacity": 0}, fix + 0.6, 0.15, "power2.out")
    S.ft(f"#{s}-k1b", {"opacity": 1}, {"opacity": 0}, fix + 0.6, 0.2, "power2.out")
    # tes lagi: needle into the pass zone, pass lamp, sticker
    S.ft(f"#{s}-ptr", {"rotation": -100}, {"rotation": 105}, W(173) - 0.1, 0.55, "back.out(1.4)")
    S.ft(f"#{s}-pass", {"opacity": 0}, {"opacity": 1}, W(174), 0.12, "power2.out")
    S.init(f"#{s}-stk", {"scale": 0, "rotation": -40})
    S.ft(f"#{s}-stk", {"scale": 1.8, "rotation": -40}, {"scale": 1, "rotation": 0}, W(174) + 0.18, 0.3, "back.out(2.4)")
    S.fx(W(174) + 0.05, "ping", 0.06)
    # hand-off: gauge + bench clear, the passed robot stays (S12 lifts it)
    ho = t1 - 0.32
    for sel in (f"#{s}-wheel", f"#{s}-ticks", f"#{s}-win", f"#{s}-ptr", f"#{s}-cap"):
        S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": -60}, ho, 0.3, "power2.in")
    for sel in (f"#{s}-bench", f"#{s}-cab", f"#{s}-bsh", f"#{s}-k0", f"#{s}-k1", f"#{s}-k2"):
        S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": 120}, ho, 0.3, "power2.in")
    S.cam([(t0, {"scale": 1, "y": 0}, None), (W(167), {"scale": 1, "y": 0}, "none"), (W(170), {"scale": 1.07, "y": 40}, "power2.inOut"),
           (W(174) + 0.3, {"scale": 1.04, "y": 20}, "sine.inOut"), (t1, {"scale": 1, "y": 0}, "power2.inOut")])

    # ---------------------------------------------------------------- mascot
    v = dict(DEMO_R, yaw=-26)
    S.mv([(t0, v, None), (t_in, dict(v, yaw=-32), "sine.inOut")])
    explain(S, t_in, t_out, 163, 166, seed=3, enter=dict(v, yaw=-32), leave=v)
    S.mv([(t_out + 0.5, v, None), (fix - 0.1, dict(v, fx=870, yaw=-38), "power2.inOut"), (fix + 0.7, dict(v, yaw=-30), "power2.out"),
          (t1, dict(v, yaw=-24), "sine.inOut")])
    S.act("armR", [(t0, "low", 0.3), (t0 + 0.25, "present", 0.35), (W(162), "low", 0.4)])
    S.act("armL", [(t0, "low", 0.3), (W(161), "explain", 0.35), (W(162) + 0.3, "low", 0.4)])
    S.act("head", [(t0, [0.0, -0.25, 0], 0.3), (W(161) + 0.2, [-0.05, -0.32, 0.03], 0.35)])
    S.act("armR", [(t_out + 0.3, "low", 0.4), (W(168), "point", 0.3), (W(170) + 0.1, "stop", 0.25), (fix - 0.15, "present", 0.25),
                   (fix + 0.45, "explain", 0.3), (W(173), "point", 0.3), (W(174) + 0.15, "palmUp", 0.3), (t1 - 0.2, "low", 0.4)])
    S.act("armL", [(t_out + 0.3, "low", 0.4), (W(170) + 0.15, "chin", 0.3), (fix + 0.2, "low", 0.35), (W(174) + 0.2, "open", 0.3), (t1 - 0.2, "low", 0.4)])
    S.act("head", [(t_out + 0.3, [-0.1, -0.3, 0], 0.4), (W(170), [0.08, -0.36, -0.06], 0.25), (fix, [0.18, -0.3, 0], 0.3),
                   (W(173), [-0.08, -0.34, 0.02], 0.35), (W(174) + 0.2, [-0.04, -0.12, 0.08], 0.3)])
    S.act("torso", [(W(170), {"chest": [-0.04, 0, 0]}, 0.25), (fix - 0.1, {"chest": [0.07, -0.12, 0]}, 0.3), (fix + 0.6, {}, 0.4)])
