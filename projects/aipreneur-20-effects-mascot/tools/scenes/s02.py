"""S02 — 01 ORBIT (4.97–6.87)  VO: "Lalu ikon mengorbit kepalanya."
Opens on S01's ring (ORBIT contract). Four smoked-glass icon chips (audio wave, 'Aa' caption, image, cursor) pop
onto the tilted ring and orbit the head 1.25 turns: on the far half they are in the BACK layer (the head hides
them), on the near half in the FRONT layer, bigger and brighter (depth). The camera eases to a 3/4 (yaw -14) and
his head follows the 'Aa' chip. Hand-off: the ring dissolves, the other chips sink into it, and 'Aa' flies forward
to the chat-avatar spot (AVATAR) -> S03 grows the chat window out of it."""
import math
from xk import box, r3
from kit import MED, AVATAR
from kit_a import ring, chip, orbit_xy, OX, OY

CH = [("wave", 150), ("aa", 60), ("img", 240), ("cur", 330)]     # icon, start angle (deg); 'Aa' ends at 150 deg (front-left)
D0 = 84
TURN = 450.0


def prog(u):
    return 2 * u * u if u < 0.5 else 1 - 2 * (1 - u) ** 2


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W13, W14, W15, W16 = S.W(13), S.W(14), S.W(15), S.W(16)    # Lalu 5.04, ikon 5.30, mengorbit 5.62, kepalanya 6.06
    o0, o1 = t0 + 0.37, 6.46
    fly0, fly1 = 6.48, t1 - 0.02
    N = 30
    S.back.append(ring(f"{s}-rb"))
    S.front.append(ring(f"{s}-rf", half="front"))
    for name, a0 in CH:
        S.back.append(chip(f"{s}-b{name}", OX, OY, D0, name, extra="filter:brightness(.72) saturate(.9)"))
        S.front.append(chip(f"{s}-f{name}", OX, OY, D0, name))

    def pose(theta_deg):
        th = math.radians(theta_deg)
        x, y = orbit_xy(th)
        return {"x": r3(x - OX), "y": r3(y - OY), "scale": r3(1 + 0.2 * math.sin(th))}, math.sin(th) > 0

    times = [o0 + (o1 - o0) * k / N for k in range(N + 1)]
    ang = [TURN * prog(k / N) for k in range(N + 1)]
    head_keys = []
    for name, a0 in CH:
        p0, front0 = pose(a0)
        for side in "bf":
            sel = f"#{s}-{side}{name}"
            S.init(sel, dict(p0, opacity=0))
        # pop in
        S.ft(f"#{s}-{'f' if front0 else 'b'}{name}", dict(p0, scale=0, opacity=1), dict(p0, opacity=1), t0 + 0.02 + 0.04 * CH.index((name, a0)), 0.22, "back.out(2)")
        S.tset(f"#{s}-{'b' if front0 else 'f'}{name}", {"opacity": 0}, t0 + 0.01)
        state = front0
        for k in range(N):
            pa, _ = pose(a0 + ang[k])
            pb, fb = pose(a0 + ang[k + 1])
            for side in "bf":
                S.ft(f"#{s}-{side}{name}", pa, pb, times[k], times[k + 1] - times[k], "none")
            mid_front = math.sin(math.radians(a0 + (ang[k] + ang[k + 1]) / 2)) > 0
            if mid_front != state:
                S.tset(f"#{s}-f{name}", {"opacity": 1 if mid_front else 0}, times[k])
                S.tset(f"#{s}-b{name}", {"opacity": 0 if mid_front else 1}, times[k])
                state = mid_front
            if name == "aa" and k % 3 == 0:
                th = math.radians(a0 + ang[k])
                head_keys.append((times[k], [-0.05 + 0.05 * math.sin(th), 0.26 * math.cos(th), 0.03 * math.cos(th)], 0.35))
        pe, fe = pose(a0 + TURN)
        if name == "aa":
            # 'Aa' (front-left) flies forward to the chat-avatar spot
            ax, ay, ad = AVATAR
            S.ft(f"#{s}-faa", pe, {"x": r3(ax - OX), "y": r3(ay - OY), "scale": r3(ad / D0)}, fly0, fly1 - fly0, "power3.inOut")
        else:
            side = "f" if fe else "b"
            S.ft(f"#{s}-{side}{name}", dict(pe, opacity=1), dict(pe, scale=0.2, opacity=0), 6.47 + 0.03 * CH.index((name, a0)), 0.24, "power2.in")
    for sel in (f"#{s}-rb", f"#{s}-rf"):
        S.init(sel, {"opacity": 1})
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, 6.4, 0.32, "power2.in")

    # ---------------------------------------------------------------- mascot: medium -> 3/4, head follows the 'Aa' chip
    S.mv([(t0, dict(MED), None), (6.3, dict(MED, yaw=-14, pitch=6), "sine.inOut"), (t1, dict(MED, yaw=-14, pitch=6), "none")])
    S.act("head", head_keys + [(fly0, [-0.12, 0.3, 0.06], 0.3)])
    S.act("armL", [(t0, "low", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (W14 - 0.14, "pointUp", 0.3), (W15 + 0.3, "explain", 0.35), (W16 + 0.2, "low", 0.4), (fly0, "present", 0.3)])
    S.act("torso", [(t0, {}, 0.3), (W15, {"chest": [-0.03, -0.08, 0]}, 0.4), (fly0, {"chest": [0, 0.08, 0]}, 0.35)])
    S.fx(t0 + 0.06, "pop", 0.05)
    S.fx(W15, "whoosh", 0.04)
    S.fx(fly0 + 0.05, "whoosh", 0.05)
