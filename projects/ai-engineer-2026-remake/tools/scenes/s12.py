"""S12 — 10 PRODUCTION (hero beauty reveal). VO: "Kesepuluh, production. Deploy sistemnya. Pantau biaya, kecepatan,
keamanan, dan kestabilannya."
Opens on S11's passed robot (check sticker) in its bench spot. It rises into a dark enamel cavity; on "production" a
porcelain HOOD hinges down from the top and an INSTRUMENT PANEL hinges up from the bottom: the casing closes around it
(camera cranes up from low). "Deploy": status lamps light in sequence, the hood screen shows the running app output.
EXPLAIN MODE on "Pantau biaya, kecepatan, keamanan" (BIAYA / KECEPATAN / KEAMANAN chips) while the matching dials fill
behind him; on "keamanan" a frosted security gate engages over the whole casing. "kestabilannya": the last dial fills,
lamps keep a calm rhythm — hero still. Ends with the finished casing exactly at kit.MACHINE (S13 branches from it)."""
from xk import box, r3
from kit import MAT, part, shadow, chip, grid_floor, blur_wrap, explain, ICON, EXPLAIN_BAND, MACHINE
from kit_c import B11, HUB_D, DEMO_R, hub

MX, MY, MW, MH = MACHINE
HC = (MX + MW / 2, MY + 380)               # hub centre inside the casing
DIALS = [("coin", 180), ("bolt", 181), ("shield", 182), ("gauge", 184)]   # icon, word index that fills it


def dial(id_, cx, cy, icon, d=104):
    import math
    r = d / 2 - 12
    return (f'<div class="abs" style="{box(cx - d / 2, cy - d / 2, d, d)}">'
            f'<div class="abs" style="inset:0;border-radius:50%;{MAT["alu"]}"></div>'
            f'<div class="abs" style="left:7px;top:7px;width:{d - 14}px;height:{d - 14}px;border-radius:50%;background:radial-gradient(circle at 40% 30%,#ffffff,#e4eaf3)"></div>'
            f'<svg class="abs" style="left:0;top:0;width:{d}px;height:{d}px;overflow:visible" viewBox="0 0 {d} {d}">'
            f'<circle cx="{d / 2}" cy="{d / 2}" r="{r}" fill="none" stroke="rgba(41,75,119,.15)" stroke-width="8"/>'
            f'<circle id="{id_}" cx="{d / 2}" cy="{d / 2}" r="{r}" fill="none" stroke="#294B77" stroke-width="8" stroke-linecap="round" '
            f'pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" transform="rotate(-90 {d / 2} {d / 2})"/></svg>'
            f'<div class="abs" style="left:{d * .32}px;top:{d * .32}px;width:{d * .36}px;height:{d * .36}px;color:#1c3561">{icon}</div></div>')


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    # ---------------------------------------------------------------- back
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(shadow(MX - 40, MY + MH - 60, MW + 80, 130, 0.6, f"{s}-msh"))
    # dark cavity (machine interior) with a soft inner rim light
    S.back.append(f'<div class="abs" id="{s}-cav" style="{box(MX, MY, MW, MH)}border-radius:46px;{MAT["enamel"]}">'
                  f'<div class="abs" style="left:60px;top:300px;width:480px;height:170px;border-radius:24px;background:radial-gradient(ellipse at 50% 50%,rgba(159,196,255,.35),rgba(10,13,44,0) 70%)"></div></div>')
    # the passed robot (from S11)
    S.back.append(hub(f"{s}-hub", HC, sticker=True, sid=f"{s}-stk"))
    # side rails framing the window
    for k, x in enumerate((MX, MX + MW - 60)):
        S.back.append(part(f"{s}-rail{k}", x, MY + 290, 60, 190, "porcelain", 14))
    # HOOD (hinges down from the top) with the app-output screen
    rows = "".join(f'<div class="abs" id="{s}-b{k}" style="left:{[24, 196, 24][k]}px;top:{24 + k * 62}px;width:{[300, 300, 250][k]}px;height:46px;border-radius:16px;'
                   f'background:{["#ffffff", "linear-gradient(105deg,#0A0D2C,#294B77)", "#ffffff"][k]};box-shadow:0 6px 12px -8px rgba(10,13,44,.4)">'
                   f'<div class="abs" style="left:18px;top:17px;width:{[200, 220, 150][k]}px;height:12px;border-radius:6px;background:{["rgba(41,75,119,.3)", "rgba(255,255,255,.55)", "rgba(41,75,119,.3)"][k]}"></div></div>'
                   for k in range(3))
    S.back.append(f'<div class="abs" id="{s}-hood" style="{box(MX, MY, MW, 300)}border-radius:46px 46px 18px 18px;{MAT["porcelain"]}">'
                  f'<div class="abs" style="left:40px;top:36px;width:520px;height:228px;border-radius:24px;{MAT["glass"]}">{rows}</div></div>')
    # INSTRUMENT PANEL (hinges up from the bottom): 4 dials + status lamps
    dials = "".join(dial(f"{s}-d{k}", 105 + k * 130, 110, ICON[ic]) for k, (ic, _) in enumerate(DIALS))
    lamps = "".join(f'<div class="abs" id="{s}-lp{k}" style="left:{150 + k * 64}px;top:212px;width:40px;height:14px;border-radius:7px;background:rgba(41,75,119,.2)"></div>' for k in range(5))
    S.back.append(f'<div class="abs" id="{s}-panel" style="{box(MX, MY + 480, MW, MH - 480)}border-radius:18px 18px 46px 46px;{MAT["porcelain"]}">{dials}{lamps}</div>')
    # frosted window over the robot (slides down after the casing closes)
    S.back.append(f'<div class="abs" id="{s}-win" style="{box(MX + 60, MY + 300, MW - 120, 170)}border-radius:16px;{MAT["glass"]}opacity:.55"></div>')
    # SECURITY GATE: frosted outline over the whole casing + shield emblem
    S.back.append(f'<div class="abs" id="{s}-gate" style="{box(MX - 26, MY - 26, MW + 52, MH + 52)}border-radius:64px;border:5px solid rgba(255,255,255,.95);'
                  f'box-shadow:0 0 0 2px rgba(41,75,119,.35),0 0 30px rgba(159,196,255,.7),inset 0 0 40px rgba(159,196,255,.35)">'
                  f'<div class="abs" style="left:{(MW + 52) / 2 - 40}px;top:-42px;width:80px;height:80px;border-radius:24px;background:linear-gradient(135deg,#0A0D2C,#294B77);'
                  f'box-shadow:0 0 0 5px #fff,0 12px 20px -8px rgba(10,13,44,.6);color:#fff;padding:20px">{ICON["shield"]}</div></div>')
    blur_wrap(S)
    # explain visuals
    ey = EXPLAIN_BAND[0] + 26
    S.front.append(chip(f"{s}-c0", 70, ey, "BIAYA", ICON["coin"], size=32))
    S.front.append(chip(f"{s}-c1", 330, ey, "KECEPATAN", ICON["bolt"], size=32))
    S.front.append(chip(f"{s}-c2", 680, ey, "KEAMANAN", ICON["shield"], size=32, dark=True))

    # ---------------------------------------------------------------- motion
    # the passed robot rises into the cavity
    S.init(f"#{s}-hub", {"x": B11[0] - HC[0], "y": B11[1] - HC[1], "scale": 0.8})
    S.ft(f"#{s}-hub", {"x": B11[0] - HC[0], "y": B11[1] - HC[1], "scale": 0.8}, {"x": 0, "y": 0, "scale": 1}, t0 + 0.05, 0.7, "power3.inOut")
    S.init(f"#{s}-cav", {"scaleY": 0.2, "opacity": 0, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-cav", {"scaleY": 0.2, "opacity": 0}, {"scaleY": 1, "opacity": 1}, t0 + 0.15, 0.55, "power3.out")
    S.init(f"#{s}-msh", {"opacity": 0})
    S.ft(f"#{s}-msh", {"opacity": 0}, {"opacity": 0.6}, t0 + 0.2, 0.5, "power2.out")
    for k in range(2):
        S.init(f"#{s}-rail{k}", {"scaleY": 0, "transformOrigin": "50% 50%"})
        S.ft(f"#{s}-rail{k}", {"scaleY": 0}, {"scaleY": 1}, t0 + 0.55 + k * 0.06, 0.3, "back.out(2)")
    # the casing closes on "production": hood down, instrument panel up (hinged, 3D)
    close = W(176)
    S.init(f"#{s}-hood", {"rotationX": -112, "transformOrigin": "50% 0%", "transformPerspective": 1400, "opacity": 0})
    S.tset(f"#{s}-hood", {"opacity": 1}, close - 0.45)
    S.ft(f"#{s}-hood", {"rotationX": -112}, {"rotationX": 0}, close - 0.4, 0.5, "power3.in")
    S.init(f"#{s}-panel", {"rotationX": 112, "transformOrigin": "50% 100%", "transformPerspective": 1400, "opacity": 0})
    S.tset(f"#{s}-panel", {"opacity": 1}, close - 0.33)
    S.ft(f"#{s}-panel", {"rotationX": 112}, {"rotationX": 0}, close - 0.28, 0.5, "power3.in")
    S.ft(f"#{s}-hood", {"y": 0}, {"y": -4}, close + 0.1, 0.06, "power2.out")
    S.ft(f"#{s}-hood", {"y": -4}, {"y": 0}, close + 0.16, 0.2, "back.out(3)")
    S.fx(close + 0.1, "click", 0.08)
    S.fx(close + 0.22, "click", 0.05)
    S.init(f"#{s}-win", {"y": -170, "opacity": 0})
    S.ft(f"#{s}-win", {"y": -170, "opacity": 0}, {"y": 0, "opacity": 0.55}, close + 0.3, 0.4, "power3.out")
    # Deploy: status lamps light in sequence, the screen shows the running app
    for k in range(5):
        S.init(f"#{s}-lp{k}", {"backgroundColor": "rgba(41,75,119,0.2)", "boxShadow": "0 0 0px rgba(159,196,255,0)"})
        S.ft(f"#{s}-lp{k}", {"backgroundColor": "rgba(41,75,119,0.2)", "boxShadow": "0 0 0px rgba(159,196,255,0)"},
             {"backgroundColor": "#7fb2ff", "boxShadow": "0 0 12px rgba(159,196,255,0.95)"}, W(177) + k * 0.08, 0.18, "power2.out")
    for k in range(3):
        S.init(f"#{s}-b{k}", {"opacity": 0, "y": 16, "scale": 0.9})
        S.ft(f"#{s}-b{k}", {"opacity": 0, "y": 16, "scale": 0.9}, {"opacity": 1, "y": 0, "scale": 1}, W(178) - 0.05 + k * 0.22, 0.3, "back.out(2)")
    S.fx(W(177) + 0.05, "sparkle", 0.04)
    # dials fill on their words (behind him during the explain beat), last one on "kestabilannya"
    for k, (_, wi) in enumerate(DIALS):
        S.init(f"#{s}-d{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-d{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0.28 + 0.04 * k}}, W(wi), 0.6, "power3.out")
    S.init(f"#{s}-gate", {"opacity": 0, "scale": 1.08})
    S.ft(f"#{s}-gate", {"opacity": 0, "scale": 1.08}, {"opacity": 1, "scale": 1}, W(182) + 0.08, 0.45, "power3.out")
    # explain beat
    t_in, t_out = W(179) - 0.35, W(183) - 0.25
    for k, wi in enumerate((180, 181, 182)):
        sel = f"#{s}-c{k}"
        S.init(sel, {"opacity": 0, "y": 30, "scale": 0.8})
        S.ft(sel, {"opacity": 0, "y": 30, "scale": 0.8}, {"opacity": 1, "y": 0, "scale": 1}, W(wi) - 0.05, 0.36, "back.out(2)")
        S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": -20}, t_out - 0.1, 0.25, "power2.in")
        S.fx(W(wi) - 0.03, "pop", 0.045)
    # calm operating rhythm after the reveal: lamps chase once more, screen bubble breathes
    for k in range(5):
        a = W(184) + 0.2 + k * 0.09
        S.ft(f"#{s}-lp{k}", {"opacity": 1}, {"opacity": 0.45}, a, 0.15, "power2.out")
        S.ft(f"#{s}-lp{k}", {"opacity": 0.45}, {"opacity": 1}, a + 0.15, 0.2, "power2.out")
    S.fx(W(184) + 0.1, "ping", 0.05)
    # crane-up: starts low and close, rises to the hero view, ends exactly on identity (MACHINE rect is screen-true)
    S.cam([(t0, {"y": -220, "scale": 1.16}, None), (W(177), {"y": -40, "scale": 1.04}, "power2.inOut"),
           (t_in + 0.1, {"y": 0, "scale": 1.02}, "sine.inOut"), (t_out + 0.5, {"y": 0, "scale": 1}, "power2.inOut"), (t1, {"y": 0, "scale": 1}, "none")])

    # ---------------------------------------------------------------- mascot
    v0 = dict(DEMO_R, yaw=-24)
    v = {"fx": 915, "fy": 1975, "h": 660, "yaw": -32, "pitch": 3}   # foreground lower-right, below the casing, looking up at it
    S.mv([(t0, v0, None), (t0 + 0.8, v, "power2.inOut"), (t_in, dict(v, yaw=-26), "sine.inOut")])
    explain(S, t_in, t_out, 179, 182, seed=4, enter=dict(v, yaw=-26), leave=v)
    S.mv([(t_out + 0.5, v, None), (t1, dict(v, yaw=-36), "sine.inOut")])
    S.act("armR", [(t0, "low", 0.3), (t0 + 0.3, "present", 0.35), (W(176) + 0.2, "pointUp", 0.3), (W(177) + 0.3, "explain", 0.35), (W(178) + 0.4, "low", 0.4)])
    S.act("armL", [(t0, "low", 0.3), (W(176), "fist", 0.3), (W(177) + 0.2, "low", 0.4)])
    S.act("head", [(t0, [0.1, -0.3, 0], 0.3), (t0 + 0.6, [-0.08, -0.36, 0.03], 0.4), (W(176), [-0.14, -0.3, -0.04], 0.3), (W(178), [0.0, -0.22, 0.05], 0.35)])
    S.act("armR", [(t_out + 0.3, "low", 0.4), (W(184) - 0.1, "present", 0.35), (t1 - 0.4, "low", 0.45)])
    S.act("armL", [(t_out + 0.3, "low", 0.4), (W(184), "together", 0.35), (t1 - 0.35, "low", 0.45)])
    S.act("head", [(t_out + 0.3, [-0.12, -0.34, 0], 0.4), (W(184) + 0.2, [-0.18, -0.26, 0.04], 0.4), (t1 - 0.3, [-0.08, -0.2, 0], 0.4)])
    S.act("torso", [(W(184), {"chest": [-0.03, -0.1, 0]}, 0.4)])
