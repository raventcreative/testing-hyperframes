"""S01 — HOOK (0 – W19). VO: "Bikin AI agent doang, belum bikin lo jadi AI Engineer. Kalau fondasinya bolong, demo yang
keren pun bisa ambruk."
The mascot WALKS forward toward camera and waves hi; behind him a flashy AI AGENT tower (glass dome + enamel body) stands
on one thin rod. EXPLAIN MODE on "belum bikin lo jadi AI Engineer" (half-body, tower soft behind). He steps back to the
left; the camera drops to the base plate: two bolt holes are EMPTY ("bolong"). On "ambruk" the rod tilts, the tower
slips and the mascot catches it. A connector falls, hits the floor and runs out as one blueprint line (-> S02)."""
from xk import box, r3
from kit import (HALF, HALF_IN, FLOOR_Y, MAT, part, socket, shadow, cable, grid_floor, blur_wrap, explain, LINE_S01, chip, ICON)

TX, TOP = 700, 560          # tower centre x, dome top


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    # ---------------------------------------------------------------- back: floor, base plate, rod, tower
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(shadow(TX - 260, FLOOR_Y - 40, 520, 90, 0.55, f"{s}-tsh"))
    # base plate with 4 bolt seats: two bolts present, two EMPTY (the "bolong" foundation)
    bolts = ""
    for k, bx in enumerate((24, 96, 284, 356)):
        empty = k in (1, 2)
        bolts += (f'<div class="abs" id="{s}-bolt{k}" style="left:{bx}px;top:22px;width:34px;height:34px;border-radius:50%;'
                  + ('background:radial-gradient(circle at 45% 40%,#1b2232 0%,#05070d 70%);box-shadow:inset 0 3px 6px rgba(0,0,0,.7)'
                     if empty else MAT["alu"] + "border-radius:50%") + '"></div>')
    S.back.append(f'<div class="abs" id="{s}-base" style="{box(TX - 205, FLOOR_Y - 70, 410, 78)}border-radius:16px;{MAT["porcelain"]}">{bolts}</div>')
    # the tower: thin rod + enamel body + glass dome with the AI AGENT band
    tower = (part(None, 190, 520, 36, 300, "alu", 10)                                             # rod (x rel. to tower box)
             + part(None, 40, 230, 336, 300, "enamel", 40,
                    inner='<div class="abs" style="left:34px;top:60px;width:268px;height:60px;border-radius:30px;background:rgba(255,255,255,.12)"></div>'
                          '<div class="abs" style="left:58px;top:150px;width:220px;height:14px;border-radius:7px;background:linear-gradient(90deg,#9fc4ff,#ffffff)"></div>'
                          '<div class="abs" style="left:58px;top:180px;width:150px;height:14px;border-radius:7px;background:rgba(255,255,255,.35)"></div>')
             + f'<div class="abs" style="left:0;top:0;width:416px;height:260px;border-radius:208px 208px 40px 40px;{MAT["glass"]}">'
               f'<div class="abs" id="{s}-orb" style="left:128px;top:46px;width:160px;height:160px;border-radius:50%;'
               f'background:radial-gradient(circle at 38% 32%,#ffffff 0%,#bcd6ff 30%,#3f6fb0 70%,#1c3561 100%);'
               f'box-shadow:0 0 0 6px rgba(255,255,255,.6),0 18px 30px -12px rgba(10,13,44,.6)"></div></div>'
             + f'<div class="abs" style="left:58px;top:236px;width:300px;height:62px;border-radius:14px;background:linear-gradient(105deg,#0A0D2C,#294B77);'
               f'box-shadow:inset 0 1px 0 rgba(255,255,255,.3);font:700 38px/62px Poppins;color:#fff;text-align:center;letter-spacing:.06em">AI AGENT</div>')
    S.back.append(f'<div class="abs" id="{s}-tower" style="{box(TX - 208, TOP, 416, 820)}">{tower}</div>')
    # a loose connector on the tower flank (it falls on "ambruk")
    S.back.append(part(f"{s}-conn", TX + 150, TOP + 470, 70, 34, "alu", 8))
    S.back.append(cable(f"{s}-line", f"M{TX + 185},{FLOOR_Y} L{LINE_S01[2]},{FLOOR_Y} M{TX + 185},{FLOOR_Y} L{LINE_S01[0]},{FLOOR_Y}", w=5, color="#1c3561"))
    blur_wrap(S)
    # explain-mode visuals (front layer, beside his head, never over the face): AI AGENT chip -> arrow -> AI ENGINEER chip
    S.front.append(chip(f"{s}-c1", 60, 446, "AI AGENT", ICON["chat"], size=34))
    S.front.append(chip(f"{s}-c2", 600, 446, "AI ENGINEER", ICON["tool"], size=34, dark=True))
    S.front.append(f'<svg class="abs" id="{s}-arw" style="left:405px;top:456px;width:180px;height:60px;overflow:visible" viewBox="0 0 180 60">'
                   f'<path id="{s}-arwp" d="M10 30 H160 M140 12 L162 30 L140 48" fill="none" stroke="#294B77" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')

    # ---------------------------------------------------------------- motion
    # world camera: slow macro push-in for the whole hook; drops toward the base plate on "fondasinya bolong"
    bol = W(11)
    S.cam([(t0, {"y": 0, "scale": 1, "rotation": 0}, None), (bol - 0.3, {"y": 0, "scale": 1.03, "rotation": 0}, "sine.inOut"),
           (bol + 0.45, {"y": -230, "scale": 1.32, "rotation": 0}, "power3.inOut"), (W(16), {"y": -210, "scale": 1.3, "rotation": 0}, "sine.inOut"),
           (W(18) - 0.05, {"y": -60, "scale": 1.1, "rotation": 0}, "power3.inOut"), (W(18) + 0.25, {"y": -60, "scale": 1.1, "rotation": -1.6}, "power2.out"),
           (t1, {"y": -40, "scale": 1.08, "rotation": -0.8}, "sine.inOut")])
    # tower idles with a faint sway (it is top-heavy) from the start, glows on "AI agent"
    S.init(f"#{s}-tower", {"rotation": 0, "x": 0, "y": 0, "transformOrigin": "208px 820px"})
    S.keys(f"#{s}-tower", [(t0, {"rotation": 0}, None), (t0 + 1.2, {"rotation": -0.8}, "sine.inOut"), (t0 + 2.4, {"rotation": 0.8}, "sine.inOut"),
                           (t0 + 3.6, {"rotation": -0.6}, "sine.inOut"), (W(16), {"rotation": 0.6}, "sine.inOut")])
    S.init(f"#{s}-orb", {"scale": 1, "filter": "brightness(1)"})
    S.ft(f"#{s}-orb", {"scale": 1, "filter": "brightness(1)"}, {"scale": 1.08, "filter": "brightness(1.25)"}, W(1) - 0.05, 0.3, "back.out(2)")
    S.ft(f"#{s}-orb", {"scale": 1.08, "filter": "brightness(1.25)"}, {"scale": 1, "filter": "brightness(1)"}, W(3), 0.5, "power2.out")
    # empty bolt seats pulse while the camera looks at them
    for k in (1, 2):
        S.init(f"#{s}-bolt{k}", {"boxShadow": "inset 0 3px 6px rgba(0,0,0,0.7), 0 0 0 0px rgba(41,75,119,0)"})
        S.ft(f"#{s}-bolt{k}", {"boxShadow": "inset 0 3px 6px rgba(0,0,0,0.7), 0 0 0 0px rgba(41,75,119,0)"},
             {"boxShadow": "inset 0 3px 6px rgba(0,0,0,0.7), 0 0 0 8px rgba(41,75,119,0.35)"}, W(12) - 0.1 + 0.08 * k, 0.35, "power2.out")
    # AMBRUK: rod tips, tower lurches toward the mascot, he catches it -> it settles leaning on his hand
    amb = W(18)
    S.ft(f"#{s}-tower", {"rotation": 0.6, "x": 0, "y": 0}, {"rotation": -9, "x": -26, "y": 14}, amb - 0.08, 0.32, "power3.in")
    S.ft(f"#{s}-tower", {"rotation": -9, "x": -26, "y": 14}, {"rotation": -7.2, "x": -22, "y": 10}, amb + 0.24, 0.35, "back.out(2.5)")
    S.ft(f"#{s}-tsh", {"x": 0, "scaleX": 1}, {"x": -40, "scaleX": 1.15}, amb - 0.08, 0.32, "power3.in")
    # the loose connector drops, bounces once and its cable runs out along the floor as a blueprint line
    S.init(f"#{s}-conn", {"y": 0, "rotation": 0, "opacity": 1})
    S.ft(f"#{s}-conn", {"y": 0, "rotation": 0}, {"y": FLOOR_Y - (TOP + 470) - 34, "rotation": 70}, amb, 0.42, "power2.in")
    S.ft(f"#{s}-conn", {"y": FLOOR_Y - (TOP + 470) - 34}, {"y": FLOOR_Y - (TOP + 470) - 60}, amb + 0.42, 0.12, "power2.out")
    S.ft(f"#{s}-conn", {"y": FLOOR_Y - (TOP + 470) - 60}, {"y": FLOOR_Y - (TOP + 470) - 34}, amb + 0.54, 0.14, "power2.in")
    S.init(f"#{s}-line", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-line", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, amb + 0.6, t1 - amb - 0.62, "power2.inOut")
    S.fx(amb - 0.05, "whoosh", 0.05)
    S.fx(amb + 0.42, "click", 0.07)

    for k, (sel, at) in enumerate(((f"#{s}-c1", W(4) - 0.05), (f"#{s}-c2", W(8) - 0.05))):
        S.init(sel, {"opacity": 0, "y": 30, "scale": 0.8, "rotation": -4 if k == 0 else 4})
        S.ft(sel, {"opacity": 0, "y": 30, "scale": 0.8}, {"opacity": 1, "y": 0, "scale": 1}, at, 0.4, "back.out(2)")
        S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": -20}, W(10) - 0.35, 0.25, "power2.in")
    S.init(f"#{s}-arwp", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-arwp", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(6), 0.5, "power2.inOut")
    S.init(f"#{s}-arw", {"opacity": 1})
    S.ft(f"#{s}-arw", {"opacity": 1}, {"opacity": 0}, W(10) - 0.35, 0.25, "power2.in")
    S.fx(W(8) - 0.02, "pop", 0.05)

    # ---------------------------------------------------------------- mascot
    deep = {"fx": 400, "fy": 1500, "h": 640, "yaw": 0, "pitch": 6}           # small, deep in the set
    near = {"fx": 330, "fy": 1820, "h": 1180, "yaw": 14, "pitch": 5}       # arrived at camera, left of the tower
    side = {"fx": 250, "fy": 1800, "h": 1080, "yaw": 26, "pitch": 6}       # beside the tower, ready to catch
    t_in = W(4) - 0.3
    t_out = W(10) - 0.3
    S.mv([(t0, deep, None), (t0 + 1.45, near, "power1.inOut")])
    explain(S, t_in, t_out, 4, 9, seed=1, enter=near, leave=side)
    S.mv([(t_out + 0.5, side, None), (amb - 0.3, dict(side, yaw=30), "sine.inOut"), (amb + 0.1, dict(side, fx=290, yaw=36), "power3.out"),
          (t1, dict(side, fx=290, yaw=30), "sine.inOut")])
    # hi! wave while walking in, then the explain talk (from explain()), then reach + catch
    S.act("armR", [(t0, "low", 0.3), (t0 + 0.35, "wave", 0.35), (t0 + 0.75, {"upperarm": [-0.85, 0, -0.25], "forearm": [-1.45, 0, 0.1], "hand": [0, 0, -0.15]}, 0.22),
                   (t0 + 1.0, "wave", 0.22), (t0 + 1.25, {"upperarm": [-0.85, 0, -0.25], "forearm": [-1.45, 0, 0.1], "hand": [0, 0, -0.15]}, 0.22),
                   (t0 + 1.5, "wave", 0.25)])
    S.act("armL", [(t0, "low", 0.3)])
    S.act("head", [(t0, [0.02, 0.1, 0.06], 0.3), (t0 + 0.5, [-0.06, 0.14, 0.1], 0.35)])
    S.act("armL", [(t_out + 0.25, "low", 0.4), (W(12), "point", 0.35), (W(14), "low", 0.4), (amb - 0.25, "stop", 0.22), (amb + 0.15, "present", 0.3)])
    S.act("armR", [(t_out + 0.25, "low", 0.4), (amb - 0.2, "open", 0.25), (t1 - 0.3, "low", 0.4)])
    S.act("head", [(t_out + 0.2, [0.12, 0.3, 0], 0.4), (W(13), [-0.05, 0.36, 0.02], 0.4), (amb - 0.1, [-0.12, 0.4, 0.05], 0.22), (amb + 0.4, [0.05, 0.3, 0], 0.4)])
    S.act("torso", [(amb - 0.15, {"chest": [0.05, 0.14, 0]}, 0.25), (t1 - 0.2, {}, 0.4)])
    S.fx(t0 + 0.4, "pop", 0.04)
