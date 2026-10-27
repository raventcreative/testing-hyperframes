"""S01 — ORBIT. Five screenshot cards orbit the body on an ellipse centred on the chest. Cards on the far half pass
BEHIND the 3D cutout (back layer, scale .78), on the near half IN FRONT (front layer, scale 1.05); 1.3 s per turn,
each card banks with the orbit. Every card exists twice (back + front copy) and the copies swap opacity exactly
when the card crosses the ellipse's horizontal axis. Frame 0 = cards already placed around him (thumbnail)."""
import math
from xk import box, r3
from kit_a import shot, KINDS

V = {"fx": 540, "fy": 1120, "h": 950, "yaw": 0, "pitch": 5}   # eyes ~y555, chest ~y780
CX, CY = 540, 790                                             # orbit centre (chest)
RX, RY = 395, 132                                             # ellipse semi-axes (128x46 ratio, scaled to frame)
CW, CH = 150, 267                                             # portrait screenshot card
PERIOD = 1.3
N = 5
STEP = 1 / 15


def card(id_, k):
    return shot(id_, CX - CW / 2, CY - CH / 2, CW, CH, ["video", "chart", "chat", "hook", "stats"][k], r=14, border=6)


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    spin0 = t0 + 0.3          # orbit starts, eases up to full speed over 0.6 s

    def theta(k, t):
        u = max(0.0, t - spin0)
        ramp = 0.6
        # integral of a smoothstep speed ramp (0 -> 1 over `ramp`), then constant speed
        if u < ramp:
            x = u / ramp
            f = ramp * (x ** 3 - 0.5 * x ** 4)
        else:
            f = ramp * 0.5 + (u - ramp)
        return 2 * math.pi * k / N + 0.35 + 2 * math.pi * f / PERIOD

    def state(k, t):
        th = theta(k, t)
        sn, cs = math.sin(th), math.cos(th)
        depth = (cs + 1) / 2                     # 0 far (top of ellipse) -> 1 near (bottom)
        return {"x": r3(RX * sn), "y": r3(RY * cs), "scale": r3(0.78 + 0.27 * depth),
                "rotation": r3(-9 * sn * (0.4 + 0.6 * depth)), "rotationY": r3(-24 * sn)}

    # soft floor shadow under the orbit so the ring reads as one plane
    S.back.append(f'<div class="abs cshadow" id="{s}-ring" style="{box(CX - RX - 40, CY + RY + 120, 2 * RX + 80, 70)}opacity:.0"></div>')
    for k in range(N):
        S.back.append(card(f"{s}-b{k}", k))
        S.front.append(card(f"{s}-f{k}", k))
    S.init(f"#{s}-ring", {"opacity": 0.35})

    times = []
    t = t0
    while t < t1 - 1e-6:
        times.append(round(t, 3))
        t += STEP
    times.append(t1)
    for k in range(N):
        for lay in ("b", "f"):
            sel = f"#{s}-{lay}{k}"
            S.init(sel, dict(state(k, t0), transformPerspective=900))
            for a, b in zip(times, times[1:]):
                if b <= spin0:
                    continue
                S.ft(sel, state(k, a), state(k, b), a, b - a, "none")
        # visibility: front copy while cos(theta) > 0 (near half), back copy otherwise; swap at exact crossings
        near = math.cos(theta(k, t0)) > 0
        S.init(f"#{s}-f{k}", {"opacity": 1 if near else 0})
        S.init(f"#{s}-b{k}", {"opacity": 0 if near else 1})
        tt, dt = t0, 1 / 240
        while tt < t1:
            n2 = math.cos(theta(k, tt + dt)) > 0
            if n2 != near:
                lo, hi = tt, tt + dt
                for _ in range(30):
                    mid = (lo + hi) / 2
                    if (math.cos(theta(k, mid)) > 0) == near:
                        lo = mid
                    else:
                        hi = mid
                S.tset(f"#{s}-f{k}", {"opacity": 1 if n2 else 0}, hi)
                S.tset(f"#{s}-b{k}", {"opacity": 0 if n2 else 1}, hi)
                near = n2
            tt += dt

    # mascot: stands in the eye of the orbit, opens his arms, follows the cards with his head
    S.mv([(t0, V, None), (t1, dict(V, yaw=0, fy=V["fy"] - 10), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.35, "open", 0.45), (t0 + 2.4, "palmUp", 0.4), (t0 + 3.6, "open", 0.4), (t1 - 0.75, "low", 0.5)])
    S.act("armR", [(t0, "low", 0.3), (t0 + 0.45, "open", 0.45), (t0 + 2.6, "palmUp", 0.4), (t0 + 3.8, "open", 0.4), (t1 - 0.7, "low", 0.5)])
    S.act("head", [(t0, [0, 0, 0], 0.3), (t0 + 0.5, [-0.05, 0.22, 0.03], 0.5), (t0 + 1.4, [-0.08, -0.22, -0.03], 0.55),
                   (t0 + 2.3, [-0.03, 0.2, 0.04], 0.55), (t0 + 3.2, [-0.08, -0.2, -0.03], 0.55), (t0 + 4.1, [-0.04, 0.05, 0], 0.5), (t1 - 0.6, [0, 0, 0], 0.5)])
    S.act("torso", [(t0 + 0.4, {"chest": [0.03, 0.05, 0]}, 0.5), (t0 + 2.5, {"chest": [0.03, -0.05, 0]}, 0.6), (t1 - 0.7, {}, 0.5)])
