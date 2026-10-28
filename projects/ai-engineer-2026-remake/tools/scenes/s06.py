"""S06 — 04 DEEP LEARNING (w85-95). VO: "Keempat, deep learning. Kenali neural network, tensor, dan framework seperti PyTorch."
Opens on S05's fitted trend line (kit.ML_TREND). Its six vertices pop into glass neurons and swing up into the first
vertical layer; two more frosted layers slide in, weighted connectors draw, a pulse crosses the net ("deep learning").
EXPLAIN MODE on "Kenali neural network, tensor, dan framework seperti": half-body, net soft behind (pulses keep
travelling), chips NEURAL NETWORK / TENSOR / PyTorch pop in the band. He steps back; on "PyTorch" the whole net fires
once; the last node's edge drops and runs out left as the TOKEN TRACK (-> S07)."""
from xk import box, r3
from kit import ML_TREND, MAT, SIDE_L, part, shadow, chip, cable, grid_floor, blur_wrap, explain, FLOOR_Y
from kit_b import node, plate, pop_chip, rail, TRACK, ICON_B

L1 = [(520, 740 + 124 * k) for k in range(6)]
L2 = [(720, 790 + 124 * k) for k in range(5)]
L3 = [(920, 890 + 124 * k) for k in range(3)]
PULSES = [(0, 2, 1), (3, 1, 0), (5, 4, 2), (2, 3, 2)]     # (L1 idx, L2 idx, L3 idx)


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    # ---------------------------------------------------------------- back
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(shadow(430, FLOOR_Y - 50, 600, 90, 0.4, f"{s}-sh"))
    S.back.append(f'<div class="abs" id="{s}-net" style="left:0;top:0;width:1080px;height:1920px">')
    S.back.append(plate(f"{s}-p1", 465, 690, 110, 720))
    S.back.append(plate(f"{s}-p2", 665, 740, 110, 596))
    S.back.append(plate(f"{s}-p3", 865, 840, 110, 348))
    lines = []
    for a, (x1, y1) in enumerate(L1):
        for b, (x2, y2) in enumerate(L2):
            lines.append(f'<path id="{s}-e1-{a}-{b}" d="M{x1},{y1} L{x2},{y2}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>')
    for a, (x1, y1) in enumerate(L2):
        for b, (x2, y2) in enumerate(L3):
            lines.append(f'<path id="{s}-e2-{a}-{b}" d="M{x1},{y1} L{x2},{y2}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>')
    S.back.append(f'<svg class="abs" id="{s}-edges" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<g fill="none" stroke="#294B77" stroke-width="2.5" stroke-opacity=".32">{"".join(lines)}</g></svg>')
    for k, (x, y) in enumerate(L1):
        S.back.append(node(f"{s}-a{k}", x, y))
    for k, (x, y) in enumerate(L2):
        S.back.append(node(f"{s}-b{k}", x, y))
    for k, (x, y) in enumerate(L3):
        S.back.append(node(f"{s}-c{k}", x, y))
    for k in range(len(PULSES)):
        S.back.append(f'<div class="abs" id="{s}-q{k}" style="{box(-9, -9, 18, 18)}border-radius:50%;background:#fff;'
                      f'box-shadow:0 0 0 4px #294B77,0 0 14px 4px rgba(150,190,255,.9)"></div>')
    # tensor slab (snaps into layer 2 on "tensor")
    S.back.append(part(f"{s}-ten", 664, 1352, 112, 70, "enamel", 12,
                       inner='<div class="abs" style="left:0;top:0;width:112px;font:700 20px/70px Poppins;color:#fff;text-align:center;letter-spacing:.06em">TENSOR</div>'))
    S.back.append('</div>')
    # the trend line from S05 (visible at t0) + the token track it becomes
    pts = " L".join(f"{x},{y}" for x, y in ML_TREND)
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-trend" d="M{pts}" fill="none" stroke="#1c3561" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    x3, y3 = L3[-1]
    S.back.append(rail(f"{s}-rail", TRACK[0], TRACK[1], TRACK[2]))
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-tk" d="M{x3},{y3} L{x3},{TRACK[1]} L{TRACK[0] + 20},{TRACK[1]}" fill="none" stroke="#1c3561" stroke-width="7" '
                  f'stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')
    S.back.append(f'<div class="abs" id="{s}-lab" style="left:465px;top:1440px"><span class="badge" style="font:700 30px/1 Poppins;padding:10px 16px">04 DEEP LEARNING</span></div>')
    blur_wrap(S)
    # explain band chips
    S.front.append(chip(f"{s}-k1", 40, 446, "NEURAL NETWORK", ICON_B["nn"], size=30))
    S.front.append(chip(f"{s}-k2", 448, 446, "TENSOR", ICON_B["cube"], size=30, dark=True))
    S.front.append(chip(f"{s}-k3", 712, 446, "PyTorch", ICON_B["flame"], size=30))

    # ---------------------------------------------------------------- motion
    dl = W(86)
    # vertices -> neurons (pop on the line), then swing into layer 1
    for k, (x, y) in enumerate(L1):
        vx, vy = ML_TREND[k]
        a = {"x": vx - x, "y": vy - y, "scale": 0}
        S.init(f"#{s}-a{k}", a)
        S.ft(f"#{s}-a{k}", a, {"x": vx - x, "y": vy - y, "scale": 1}, t0 + 0.05 + 0.06 * k, 0.28, "back.out(2.4)")
        S.ft(f"#{s}-a{k}", {"x": vx - x, "y": vy - y}, {"x": 0, "y": 0}, t0 + 0.55 + 0.03 * k, 0.55, "power3.inOut")
    S.init(f"#{s}-trend", {"opacity": 1})
    S.ft(f"#{s}-trend", {"opacity": 1}, {"opacity": 0}, t0 + 0.5, 0.35, "power2.in")
    S.init(f"#{s}-p1", {"opacity": 0, "scaleY": 0.2, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-p1", {"opacity": 0, "scaleY": 0.2}, {"opacity": 1, "scaleY": 1}, t0 + 0.75, 0.45, "power3.out")
    for k, sel in enumerate((f"#{s}-p2", f"#{s}-p3")):
        S.init(sel, {"opacity": 0, "x": 160, "rotationY": -40})
        S.ft(sel, {"opacity": 0, "x": 160, "rotationY": -40}, {"opacity": 1, "x": 0, "rotationY": 0}, dl - 0.1 + 0.12 * k, 0.5, "power3.out")
    for k in range(len(L2)):
        S.init(f"#{s}-b{k}", {"scale": 0})
        S.ft(f"#{s}-b{k}", {"scale": 0}, {"scale": 1}, dl + 0.12 + 0.05 * k, 0.3, "back.out(2.2)")
    for k in range(len(L3)):
        S.init(f"#{s}-c{k}", {"scale": 0})
        S.ft(f"#{s}-c{k}", {"scale": 0}, {"scale": 1}, dl + 0.3 + 0.06 * k, 0.3, "back.out(2.2)")
    for a in range(len(L1)):
        for b in range(len(L2)):
            sel = f"#{s}-e1-{a}-{b}"
            S.init(sel, {"attr": {"stroke-dashoffset": 1}})
            S.ft(sel, {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, dl + 0.25 + 0.015 * (a + b), 0.4, "power2.out")
    for a in range(len(L2)):
        for b in range(len(L3)):
            sel = f"#{s}-e2-{a}-{b}"
            S.init(sel, {"attr": {"stroke-dashoffset": 1}})
            S.ft(sel, {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, dl + 0.45 + 0.015 * (a + b), 0.4, "power2.out")
    # pulses crossing the weighted connectors (two passes + a full fire on "PyTorch")
    starts = [dl + 0.75, W(89) + 0.1, W(91) + 0.1, W(93)]
    for k, (ia, ib, ic) in enumerate(PULSES):
        p0, p1, p2 = L1[ia], L2[ib], L3[ic]
        b = starts[k]
        S.init(f"#{s}-q{k}", {"x": p0[0], "y": p0[1], "opacity": 0, "scale": 0.6})
        S.ft(f"#{s}-q{k}", {"opacity": 0, "scale": 0.6}, {"opacity": 1, "scale": 1}, b, 0.1, "power2.out")
        S.ft(f"#{s}-q{k}", {"x": p0[0], "y": p0[1]}, {"x": p1[0], "y": p1[1]}, b, 0.38, "power1.inOut")
        S.ft(f"#{s}-q{k}", {"x": p1[0], "y": p1[1]}, {"x": p2[0], "y": p2[1]}, b + 0.4, 0.34, "power1.inOut")
        S.ft(f"#{s}-q{k}", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.4}, b + 0.74, 0.14, "power2.in")
    # tensor slab snaps into layer 2
    S.init(f"#{s}-ten", {"y": 140, "opacity": 0, "rotation": -8})
    S.ft(f"#{s}-ten", {"y": 140, "opacity": 0, "rotation": -8}, {"y": 0, "opacity": 1, "rotation": 0}, W(91) - 0.15, 0.32, "back.out(2.5)")
    # "PyTorch": the whole net fires once (nodes flash)
    pt = W(95)
    for grp, n in (("a", 6), ("b", 5), ("c", 3)):
        off = {"a": 0, "b": 0.08, "c": 0.16}[grp]
        for k in range(n):
            sel = f"#{s}-{grp}{k}"
            S.ft(sel, {"scale": 1, "filter": "brightness(1)"}, {"scale": 1.18, "filter": "brightness(1.3)"}, pt + off, 0.14, "power2.out")
            S.ft(sel, {"scale": 1.18, "filter": "brightness(1.3)"}, {"scale": 1, "filter": "brightness(1)"}, pt + off + 0.14, 0.24, "power2.inOut")
    S.init(f"#{s}-edges", {"opacity": 1})
    S.ft(f"#{s}-edges", {"opacity": 1}, {"opacity": 1.9}, pt, 0.12, "power2.out")
    # hand-off: last node's edge drops onto the floor line and runs left as the token track; the net recedes up
    ho = t1 - 0.62
    S.init(f"#{s}-tk", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-tk", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, ho, 0.45, "power2.inOut")
    S.init(f"#{s}-rail", {"opacity": 0, "scaleX": 0, "transformOrigin": "100% 50%"})
    S.ft(f"#{s}-rail", {"opacity": 0, "scaleX": 0}, {"opacity": 1, "scaleX": 1}, ho + 0.15, 0.45, "power3.out")
    S.init(f"#{s}-net", {"opacity": 1, "y": 0})
    S.ft(f"#{s}-net", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -120}, ho + 0.1, 0.5, "power2.in")
    S.init(f"#{s}-lab", {"opacity": 0, "y": 20})
    S.ft(f"#{s}-lab", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, dl + 0.2, 0.35, "power3.out")
    S.ft(f"#{s}-lab", {"opacity": 1}, {"opacity": 0}, ho, 0.25, "power2.in")
    S.fx(t0 + 0.1, "pop", 0.04)
    S.fx(dl, "whoosh", 0.04)
    S.fx(W(91) + 0.15, "click", 0.06)
    S.fx(pt + 0.02, "sparkle", 0.04)
    # band chips
    t_in, t_out = W(88) - 0.3, W(95) - 0.15
    pop_chip(S, f"#{s}-k1", W(89) - 0.05, t_out - 0.1, -3)
    pop_chip(S, f"#{s}-k2", W(91) - 0.05, t_out - 0.1, 2)
    pop_chip(S, f"#{s}-k3", W(93) - 0.05, t_out - 0.1, -2)

    # ---------------------------------------------------------------- mascot
    side = dict(SIDE_L, fx=215, yaw=26)
    S.mv([(t0, dict(side, yaw=18), None), (dl, dict(side, yaw=30), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (dl - 0.15, "present", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (dl + 0.1, "palmUp", 0.35)])
    S.act("head", [(t0, [0.02, 0.3, 0], 0.3), (t0 + 0.6, [-0.12, 0.38, 0.02], 0.4), (dl + 0.1, [-0.08, 0.3, -0.03], 0.35)])
    S.act("torso", [(t0, {"chest": [0.02, 0.12, 0]}, 0.3)])
    explain(S, t_in, t_out, 88, 94, seed=2, enter=dict(side, yaw=30), leave=dict(side, yaw=24))
    S.mv([(t_out + 0.5, dict(side, yaw=24), None), (t1, dict(side, yaw=30, fx=225), "sine.inOut")])
    S.act("armL", [(t_out + 0.2, "pointUp", 0.3), (pt + 0.3, "present", 0.35), (t1 - 0.3, "low", 0.35)])
    S.act("armR", [(t_out + 0.2, "low", 0.35)])
    S.act("head", [(t_out + 0.2, [-0.15, 0.35, 0], 0.35), (ho, [0.08, 0.28, 0.02], 0.35)])
