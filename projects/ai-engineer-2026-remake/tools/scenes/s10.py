"""S10 — 08 AI AGENT (premium showpiece). VO: "Kedelapan, AI agent. Beri sistem alat dan batasan yang jelas. Supaya dia
bisa memilih langkah, menjalankan tugas, lalu memeriksa hasilnya."
Opens on S09's answer sheet (kit.ANSWER_CARD). The sheet folds into the card slot of a small task ROBOT; around it a
finite LOOP WHEEL assembles with four stations: TUGAS -> PILIH -> JALANKAN -> PERIKSA. EXPLAIN MODE on "Beri sistem alat
dan batasan yang jelas" (ALAT + BATASAN chips). Back on the bench the pointer walks the loop on the words; before
JALANKAN an approval GATE blocks it until the mascot lifts it (user control). JALANKAN: a database answers a query
beam, a display fills; PERIKSA: a check is stamped. Hand-off: the wheel slides to the gauge position and its pointer
becomes the EVALUATION needle; the robot rolls down to the test bench (S11)."""
from xk import box, r3
from kit import (MAT, part, shadow, chip, cable, grid_floor, blur_wrap, explain, ICON, ANSWER_CARD, EXPLAIN_BAND)
from kit_c import C10, G11, B11, WHEEL_D, HUB_D, DEMO_R, pol, wheel, pointer, hub, pod, label

R = 236                     # station radius
ST = [(0, "TUGAS", "doc"), (90, "PILIH", "tool"), (180, "JALANKAN", "bolt"), (270, "PERIKSA", "check")]
GATE_A = 135
DB = (175, 1490)            # database cylinder (centre)
DISP = (290, 1380, 380, 220)  # display panel x y w h


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W, WE = S.W, S.WE
    cx, cy = C10
    # ---------------------------------------------------------------- back
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(shadow(cx - 300, cy + 230, 600, 110, 0.45, f"{s}-wsh"))
    S.back.append(wheel(f"{s}-wheel", C10))
    # loop track arcs between the stations (navy, drawn on)
    import math
    arc = f"M{r3(pol(C10, R - 62, 0)[0])},{r3(pol(C10, R - 62, 0)[1])} A{R - 62},{R - 62} 0 1 1 {r3(pol(C10, R - 62, 359.5)[0])},{r3(pol(C10, R - 62, 359.5)[1])}"
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-trk" d="{arc}" fill="none" stroke="#294B77" stroke-width="6" stroke-linecap="round" stroke-dasharray="3 14" opacity=".55"/>'
                  f'<path id="{s}-trk2" d="{arc}" fill="none" stroke="#0A0D2C" stroke-width="7" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')
    S.back.append(pointer(f"{s}-ptr", C10))
    # approval gate on the track between PILIH and JALANKAN (post + barrier arm)
    gx, gy = pol(C10, R - 62, GATE_A)
    S.back.append(f'<div class="abs" id="{s}-gpost" style="{box(gx + 34, gy - 34, 46, 46)}border-radius:12px;{MAT["enamel"]}">'
                  f'<div class="abs" style="left:10px;top:10px;width:26px;height:26px;color:#fff">{ICON["shield"]}</div></div>')
    S.back.append(f'<div class="abs" id="{s}-garm" style="{box(gx - 70, gy - 9, 118, 18)}border-radius:9px;'
                  f'background:repeating-linear-gradient(90deg,#0A0D2C 0 18px,#e9eef6 18px 34px);box-shadow:0 8px 14px -6px rgba(10,13,44,.5)"></div>')
    for k, (a, name, ic) in enumerate(ST):
        px, py = pol(C10, R, a)
        S.back.append(pod(f"{s}-p{k}", px, py, ICON[ic]))
        ly = py + 62 if a != 0 else py - 100
        S.back.append(label(f"{s}-l{k}", px, ly, name))
    # database + query beam + display (the tool action)
    dx, dy = DB
    S.back.append(shadow(dx - 80, dy + 70, 160, 40, 0.5))
    S.back.append(f'<div class="abs" id="{s}-db" style="{box(dx - 60, dy - 80, 120, 160)}">'
                  f'<div class="abs" style="left:0;top:14px;width:120px;height:132px;border-radius:0 0 60px 60px / 0 0 18px 18px;{MAT["enamel"]}"></div>'
                  f'<div class="abs" style="left:0;top:58px;width:120px;height:4px;background:rgba(255,255,255,.25)"></div>'
                  f'<div class="abs" style="left:0;top:100px;width:120px;height:4px;background:rgba(255,255,255,.25)"></div>'
                  f'<div class="abs" style="left:0;top:0;width:120px;height:36px;border-radius:50%;{MAT["alu"]}"></div>'
                  f'<div class="abs" id="{s}-dbl" style="left:46px;top:70px;width:28px;height:10px;border-radius:5px;background:#9fc4ff;box-shadow:0 0 12px #9fc4ff"></div></div>')
    x, y, w, h = DISP
    rows = "".join(f'<div class="abs" id="{s}-r{k}" style="left:24px;top:{58 + k * 42}px;width:{[300, 250, 280][k]}px;height:22px;border-radius:11px;'
                   f'background:linear-gradient(90deg,#1c3561,#294B77)"></div>' for k in range(3))
    S.back.append(f'<div class="abs" id="{s}-disp" style="{box(x, y, w, h)}border-radius:20px;{MAT["porcelain"]}">'
                  f'<div class="abs" style="left:22px;top:16px;width:120px;height:14px;border-radius:7px;background:rgba(41,75,119,.25)"></div>{rows}'
                  f'<div class="abs" id="{s}-ok" style="left:{w - 88}px;top:{h - 88}px;width:66px;height:66px;border-radius:50%;'
                  f'background:linear-gradient(135deg,#0A0D2C,#294B77);color:#fff;padding:14px;box-shadow:0 10px 18px -8px rgba(10,13,44,.6)">{ICON["check"]}</div></div>')
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-beam" d="M{dx + 40},{dy - 70} C{dx + 60},{dy - 200} {x + 120},{y - 120} {x + 150},{y + 4}" fill="none" stroke="#294B77" '
                  f'stroke-width="6" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1" pathLength="1"/></svg>')
    # robot hub + the incoming answer sheet (S09 hand-off)
    S.back.append(shadow(cx - 110, cy + 80, 220, 50, 0.5, f"{s}-hsh"))
    S.back.append(hub(f"{s}-hub", C10))
    ax, ay, aw, ah = ANSWER_CARD
    S.back.append(f'<div class="abs" id="{s}-card" style="{box(ax, ay, aw, ah)}border-radius:22px;{MAT["porcelain"]}">'
                  f'<div class="abs" style="left:26px;top:24px;width:180px;height:18px;border-radius:9px;background:linear-gradient(90deg,#0A0D2C,#294B77)"></div>'
                  + "".join(f'<div class="abs" style="left:26px;top:{68 + k * 34}px;width:{[360, 330, 350, 260][k]}px;height:14px;border-radius:7px;background:rgba(41,75,119,.28)"></div>' for k in range(4))
                  + "".join(f'<div class="abs" style="left:{26 + k * 70}px;top:{ah - 52}px;width:56px;height:30px;border-radius:8px;{MAT["enamel"]}'
                            f'font:700 18px/30px Poppins;color:#fff;text-align:center">[{k + 1}]</div>' for k in range(2))
                  + '</div>')
    blur_wrap(S)
    # explain visuals (front, in the free band): ALAT -> BATASAN
    by = EXPLAIN_BAND[0] + 26
    S.front.append(chip(f"{s}-c1", 150, by, "ALAT", ICON["tool"], size=36))
    S.front.append(chip(f"{s}-c2", 560, by, "BATASAN", ICON["shield"], size=36, dark=True))
    S.front.append(f'<div class="abs" id="{s}-plus" style="left:440px;top:{by + 4}px;width:80px;text-align:center;font:700 56px/1 Poppins;color:#294B77">+</div>')

    # ---------------------------------------------------------------- motion
    dock = t0 + 0.12
    # the answer sheet folds into the robot's card slot
    hx, hy = cx, cy - HUB_D / 2
    S.init(f"#{s}-card", {"x": 0, "y": 0, "scale": 1, "rotation": 0, "opacity": 1, "transformOrigin": "50% 0%"})
    S.ft(f"#{s}-card", {"x": 0, "y": 0, "scale": 1, "rotation": 0}, {"x": r3(hx - (ax + aw / 2)), "y": r3(hy - 70 - ay), "scale": 0.3, "rotation": -4},
         dock, 0.5, "power3.inOut")
    S.ft(f"#{s}-card", {"y": r3(hy - 70 - ay), "opacity": 1}, {"y": r3(hy - ay + 6), "opacity": 0}, dock + 0.5, 0.22, "power2.in")
    S.init(f"#{s}-hub", {"scale": 0.6, "opacity": 0, "y": 30})
    S.ft(f"#{s}-hub", {"scale": 0.6, "opacity": 0, "y": 30}, {"scale": 1, "opacity": 1, "y": 0}, dock + 0.1, 0.45, "back.out(1.8)")
    S.init(f"#{s}-hsh", {"opacity": 0})
    S.ft(f"#{s}-hsh", {"opacity": 0}, {"opacity": 0.5}, dock + 0.2, 0.4, "power2.out")
    S.ft(f"#{s}-hub", {"scale": 1}, {"scale": 1.07}, dock + 0.72, 0.1, "power2.out")
    S.ft(f"#{s}-hub", {"scale": 1.07}, {"scale": 1}, dock + 0.82, 0.25, "back.out(3)")
    S.fx(dock + 0.7, "click", 0.06)
    # the loop wheel assembles on "AI agent"
    S.init(f"#{s}-wheel", {"scale": 0.7, "opacity": 0, "x": 0, "y": 0, "rotation": -30})
    S.ft(f"#{s}-wheel", {"scale": 0.7, "opacity": 0, "rotation": -30}, {"scale": 1, "opacity": 1, "rotation": 0}, W(142) - 0.25, 0.6, "power3.out")
    S.init(f"#{s}-wsh", {"opacity": 0})
    S.ft(f"#{s}-wsh", {"opacity": 0}, {"opacity": 0.45}, W(142) - 0.2, 0.5, "power2.out")
    S.init(f"#{s}-trk", {"opacity": 0})
    S.ft(f"#{s}-trk", {"opacity": 0}, {"opacity": 0.55}, W(142), 0.4, "power2.out")
    for k in range(4):
        b = W(142) + 0.05 + k * 0.08
        S.init(f"#{s}-p{k}", {"scale": 0.3, "opacity": 0})
        S.ft(f"#{s}-p{k}", {"scale": 0.3, "opacity": 0}, {"scale": 1, "opacity": 1}, b, 0.35, "back.out(2.2)")
        S.init(f"#{s}-l{k}", {"opacity": 0, "y": 14})
        S.ft(f"#{s}-l{k}", {"opacity": 0, "y": 14}, {"opacity": 1, "y": 0}, b + 0.12, 0.3, "power3.out")
        S.init(f"#{s}-p{k}-on", {"opacity": 0, "scale": 0.8})
    for sel in (f"#{s}-gpost", f"#{s}-garm", f"#{s}-db", f"#{s}-disp"):
        S.init(sel, {"opacity": 0, "y": 24})
        S.ft(sel, {"opacity": 0, "y": 24}, {"opacity": 1, "y": 0}, W(143) - 0.05, 0.4, "power3.out")
    S.init(f"#{s}-garm", {"opacity": 0, "y": 24, "rotation": 0, "transformOrigin": "100% 50%"})
    S.init(f"#{s}-ptr", {"rotation": 0, "opacity": 0, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-ptr", {"opacity": 0}, {"opacity": 1}, W(143), 0.25, "power2.out")
    # robot wakes on "agent"
    for e in ("e1", "e2"):
        S.init(f"#{s}-hub-{e}", {"scaleY": 1})
        S.ft(f"#{s}-hub-{e}", {"scaleY": 1}, {"scaleY": 0.15}, W(143) + 0.05, 0.08, "power2.in")
        S.ft(f"#{s}-hub-{e}", {"scaleY": 0.15}, {"scaleY": 1}, W(143) + 0.14, 0.12, "power2.out")

    def station(k, at):
        S.ft(f"#{s}-p{k}-on", {"opacity": 0, "scale": 0.8}, {"opacity": 1, "scale": 1}, at, 0.25, "back.out(2.5)")
        S.ft(f"#{s}-p{k}", {"scale": 1}, {"scale": 1.12}, at, 0.14, "power2.out")
        S.ft(f"#{s}-p{k}", {"scale": 1.12}, {"scale": 1}, at + 0.14, 0.3, "power2.out")
    station(0, W(143) + 0.1)
    # explain beat
    t_in, t_out = W(144) - 0.3, W(151) - 0.3
    for k, (sel, at) in enumerate(((f"#{s}-c1", W(146) - 0.05), (f"#{s}-plus", W(147) - 0.05), (f"#{s}-c2", W(148) - 0.05))):
        S.init(sel, {"opacity": 0, "y": 30, "scale": 0.8})
        S.ft(sel, {"opacity": 0, "y": 30, "scale": 0.8}, {"opacity": 1, "y": 0, "scale": 1}, at, 0.38, "back.out(2)")
        S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": -20}, t_out - 0.1, 0.25, "power2.in")
    S.fx(W(146) - 0.03, "pop", 0.05)
    S.fx(W(148) - 0.03, "pop", 0.05)
    # the pointer walks the loop on the words
    S.ft(f"#{s}-trk2", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0.75}}, W(154) - 0.12, 0.45, "power2.inOut")
    S.init(f"#{s}-trk2", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-ptr", {"rotation": 0}, {"rotation": 90}, W(154) - 0.12, 0.42, "back.out(1.6)")
    station(1, W(154) + 0.2)
    S.fx(W(154) + 0.2, "click", 0.05)
    # blocked at the gate ... the mascot lifts it ... then JALANKAN
    gate = W(155) + 0.25
    S.ft(f"#{s}-ptr", {"rotation": 90}, {"rotation": 122}, W(155) - 0.05, 0.22, "power2.in")
    S.ft(f"#{s}-ptr", {"rotation": 122}, {"rotation": 112}, W(155) + 0.17, 0.2, "power2.out")
    S.ft(f"#{s}-garm", {"rotation": 0}, {"rotation": 4}, W(155) + 0.12, 0.08, "power2.out")
    S.ft(f"#{s}-garm", {"rotation": 4}, {"rotation": -78}, gate, 0.3, "back.out(1.6)")
    S.fx(gate, "click", 0.06)
    S.ft(f"#{s}-ptr", {"rotation": 112}, {"rotation": 180}, W(156) - 0.1, 0.4, "back.out(1.5)")
    S.ft(f"#{s}-trk2", {"attr": {"stroke-dashoffset": 0.75}}, {"attr": {"stroke-dashoffset": 0.5}}, W(156) - 0.1, 0.4, "power2.inOut")
    station(2, W(156) + 0.15)
    # tool action: the database answers, the display fills
    S.init(f"#{s}-beam", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-beam", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(156) + 0.2, 0.35, "power2.out")
    S.init(f"#{s}-dbl", {"scaleX": 1, "opacity": 0.6})
    S.ft(f"#{s}-dbl", {"scaleX": 1, "opacity": 0.6}, {"scaleX": 2.2, "opacity": 1}, W(156) + 0.15, 0.2, "power2.out")
    S.ft(f"#{s}-dbl", {"scaleX": 2.2, "opacity": 1}, {"scaleX": 1, "opacity": 0.6}, W(157) + 0.2, 0.3, "power2.out")
    for k in range(3):
        S.init(f"#{s}-r{k}", {"scaleX": 0, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-r{k}", {"scaleX": 0}, {"scaleX": 1}, W(157) - 0.02 + k * 0.1, 0.32, "power3.out")
    S.fx(W(157), "key", 0.04)
    # PERIKSA: pointer to the check station, check stamped on the display
    S.ft(f"#{s}-ptr", {"rotation": 180}, {"rotation": 270}, W(159) - 0.12, 0.42, "back.out(1.5)")
    S.ft(f"#{s}-trk2", {"attr": {"stroke-dashoffset": 0.5}}, {"attr": {"stroke-dashoffset": 0.25}}, W(159) - 0.12, 0.42, "power2.inOut")
    station(3, W(159) + 0.15)
    S.init(f"#{s}-ok", {"scale": 0, "rotation": -30})
    S.ft(f"#{s}-ok", {"scale": 1.7, "rotation": -30}, {"scale": 1, "rotation": 0}, W(160) - 0.02, 0.32, "back.out(2.2)")
    S.fx(W(160), "ping", 0.06)
    # hand-off: stations and tools clear, the wheel glides to the gauge spot, the pointer swings to the needle's rest,
    # the robot rolls down to the test-bench slot (S11)
    ho = t1 - 0.5
    for k in range(4):
        for sel in (f"#{s}-p{k}", f"#{s}-l{k}"):
            S.ft(sel, {"opacity": 1}, {"opacity": 0}, ho - 0.05 + k * 0.03, 0.25, "power2.in")
    for sel in (f"#{s}-gpost", f"#{s}-garm", f"#{s}-db", f"#{s}-disp", f"#{s}-trk", f"#{s}-trk2", f"#{s}-beam"):
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, ho, 0.3, "power2.in")
    dxw, dyw = G11[0] - cx, G11[1] - cy
    for sel in (f"#{s}-wheel", f"#{s}-ptr"):
        S.ft(sel, {"x": 0, "y": 0}, {"x": dxw, "y": dyw}, ho, 0.48, "power3.inOut")
    S.ft(f"#{s}-wsh", {"opacity": 0.45}, {"opacity": 0}, ho, 0.3, "power2.in")
    S.ft(f"#{s}-ptr", {"rotation": 270}, {"rotation": 225}, ho, 0.48, "power3.inOut")
    S.ft(f"#{s}-hub", {"x": 0, "y": 0, "scale": 1}, {"x": B11[0] - cx, "y": B11[1] - cy, "scale": 0.8}, ho, 0.48, "power3.inOut")
    S.ft(f"#{s}-hsh", {"x": 0, "y": 0, "opacity": 0.5}, {"x": B11[0] - cx, "y": B11[1] - cy, "opacity": 0.5}, ho, 0.48, "power3.inOut")
    S.fx(ho, "whoosh", 0.04)

    S.cam([(t0, {"scale": 1, "y": 0}, None), (W(150), {"scale": 1.05, "y": 20}, "sine.inOut"), (t1 - 0.55, {"scale": 1.04, "y": 10}, "sine.inOut"),
           (t1, {"scale": 1, "y": 0}, "power2.inOut")])

    # ---------------------------------------------------------------- mascot
    v = DEMO_R
    S.mv([(t0, dict(v, yaw=-20), None), (W(142), dict(v, yaw=-34), "sine.inOut"), (t_in, v, "sine.inOut")])
    explain(S, t_in, t_out, 144, 150, seed=2, enter=v, leave=v)
    S.mv([(t_out + 0.5, v, None), (gate - 0.2, dict(v, fx=880, yaw=-40), "power2.inOut"), (gate + 0.4, dict(v, yaw=-30), "power2.out"),
          (t1, dict(v, yaw=-26), "sine.inOut")])
    S.act("armR", [(t0, "low", 0.3), (W(142) - 0.1, "present", 0.35), (W(143) + 0.3, "low", 0.4)])
    S.act("armL", [(t0, "low", 0.3)])
    S.act("head", [(t0, [0.04, -0.3, 0], 0.3), (W(142), [0.1, -0.36, 0.02], 0.35), (W(143) + 0.2, [0.02, -0.12, 0], 0.35)])
    S.act("armR", [(t_out + 0.3, "low", 0.4), (W(154) - 0.25, "point", 0.3), (W(155) - 0.1, "explain", 0.3), (gate - 0.18, "present", 0.22),
                   (gate + 0.3, "low", 0.4), (W(157) - 0.2, "point", 0.3), (W(159) - 0.1, "explain", 0.3), (W(160) + 0.1, "palmUp", 0.35), (t1 - 0.35, "low", 0.4)])
    S.act("armL", [(t_out + 0.3, "low", 0.4), (W(156), "explain", 0.35), (W(157) + 0.4, "low", 0.4), (W(160), "open", 0.35), (t1 - 0.3, "low", 0.4)])
    S.act("head", [(t_out + 0.3, [0.06, -0.25, 0], 0.4), (W(154), [-0.02, -0.18, 0.02], 0.35), (gate - 0.2, [0.16, -0.22, -0.04], 0.3),
                   (W(157), [0.14, -0.42, 0.04], 0.35), (W(159), [0.0, -0.4, -0.02], 0.35), (W(160) + 0.1, [-0.06, -0.1, 0.06], 0.35)])
    S.act("torso", [(gate - 0.2, {"chest": [0.06, -0.12, 0]}, 0.3), (gate + 0.35, {}, 0.4)])
