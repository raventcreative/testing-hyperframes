"""S08 — 07 ZOOM PORTAL (14.13–15.23)  VO: "Kamera masuk ke portal,"
Opens on S07's satin-metal ring (RING_B) beside the mascot (PORTAL_VIEW, 3/4, he points at it). "Kamera": the iris
inside the ring opens onto the graph world (graph_world(): grid floor + horizon glow) - a real masked view into the
next scene, never over his face. "masuk ke portal": the camera flies into the ring - ring and its window grow and
centre together (same ease, the window = the ring hole), the mascot passes the lens on the left (camera re-frame,
he exits frame), cyan speed streaks, HERO APEX #2 as the rim passes the lens.
End state: graph_world() fills the frame at identity, mascot hidden (vis 0) = S09's opening state."""
import math
from xk import box, r3, apex, CYAN
from kit import graph_world, NO_FILTER
from kit_b import RING_B, PORTAL_VIEW, ring_markup


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W37, W38, W40 = S.W(37), S.W(38), S.W(40)     # Kamera 14.20, masuk 14.52, portal 14.82
    rcx, rcy, rd = RING_B
    hole = rd / 2 - 28
    p0, p1 = W38 - 0.04, t1 - 0.16                # the push
    SC = 6.0
    # ---------------------------------------------------------------- back: contact shadow
    S.back.append(f'<div class="abs cshadow" id="{s}-sh" style="{box(120, 1740, 440, 84)}opacity:.85"></div>')
    # ---------------------------------------------------------------- front: portal window (graph world, clipped to the ring hole), streaks, ring
    S.front.append(f'<div class="abs" id="{s}-gwc" style="{box(0, 0, 1080, 1920)}clip-path:circle(0px at {rcx}px {rcy}px)">'
                   f'<div class="abs" id="{s}-gwz" style="{box(0, 0, 1080, 1920)}">{graph_world(s)}</div></div>')
    for k in range(10):
        a = 2 * math.pi * (k + 0.35) / 10
        S.front.append(f'<div class="abs" id="{s}-st{k}" style="left:540px;top:960px;width:520px;height:3px;transform-origin:0 50%;'
                       f'background:linear-gradient(90deg,rgba(159,240,255,0),rgba(159,240,255,.9));opacity:0"></div>')
    S.front.append(ring_markup(f"{s}-ring", rcx, rcy, rd))
    apex(S, S.front, f"{s}-ap", 540, 960, t1 - 0.3, size=1200, sparks=12, seed=808, op=0.5)

    # ---------------------------------------------------------------- motion
    # iris opens inside the ring ("Kamera")
    def circ(r, x, y):
        return f"circle({r3(r)}px at {r3(x)}px {r3(y)}px)"
    S.init(f"#{s}-gwc", {"clipPath": circ(0, rcx, rcy)})
    S.ft(f"#{s}-gwc", {"clipPath": circ(0, rcx, rcy)}, {"clipPath": circ(hole, rcx, rcy)}, t0 + 0.04, 0.3, "power3.out")
    # fly-through: the ring and its window grow and centre together
    S.ft(f"#{s}-gwc", {"clipPath": circ(hole, rcx, rcy)}, {"clipPath": circ(hole * SC, 540, 960)}, p0, p1 - p0, "power2.in")
    S.init(f"#{s}-ring", {"x": 0, "y": 0, "scale": 1, "rotation": 0, "opacity": 1})
    S.ft(f"#{s}-ring", {"rotation": 0}, {"rotation": 18}, t0, p0 - t0, "sine.inOut")
    S.ft(f"#{s}-ring", {"x": 0, "y": 0, "scale": 1, "rotation": 18}, {"x": 540 - rcx, "y": 960 - rcy, "scale": SC, "rotation": 40}, p0, p1 - p0, "power2.in")
    S.tset(f"#{s}-ring", {"opacity": 0}, p1)
    # inside the portal the world comes toward us (ends at identity = S09)
    S.init(f"#{s}-gwz", {"scale": 1.35, "y": -480, "transformOrigin": f"{rcx}px {rcy}px"})
    S.ft(f"#{s}-gwz", {"scale": 1.35, "y": -480}, {"scale": 1, "y": 0}, t0 + 0.04, p1 - t0 - 0.04, "power2.inOut")
    for k in range(10):
        a = 2 * math.pi * (k + 0.35) / 10
        S.init(f"#{s}-st{k}", {"opacity": 0, "scaleX": 0.2, "rotation": r3(math.degrees(a)), "x": r3(260 * math.cos(a)), "y": r3(260 * math.sin(a)), "transformOrigin": "0px 1.5px"})
        S.ft(f"#{s}-st{k}", {"opacity": 0, "scaleX": 0.2}, {"opacity": 0.9, "scaleX": 1.6}, p0 + 0.2 + (k % 3) * 0.04, 0.26, "power2.in")
        S.ft(f"#{s}-st{k}", {"opacity": 0.9, "scaleX": 1.6}, {"opacity": 0, "scaleX": 2.4}, p1 - 0.04 + (k % 3) * 0.02, 0.2, "power2.out")
    S.init(f"#{s}-sh", {"opacity": 0.85, "x": 0})
    S.ft(f"#{s}-sh", {"opacity": 0.85, "x": 0}, {"opacity": 0, "x": -500}, p0, p1 - p0 - 0.1, "power2.in")

    # ---------------------------------------------------------------- mascot: looks at the portal, the camera passes him on the left
    S.mv([(t0, dict(PORTAL_VIEW), None), (p0, dict(PORTAL_VIEW, yaw=-20), "sine.inOut"),
          (p1 - 0.08, {"fx": -330, "fy": 2620, "h": 2500, "yaw": -30, "pitch": 4}, "power2.in")])
    S.mset("V", {"vis": 0}, p1 - 0.08)
    S.mx([(t0, {"filter": NO_FILTER}, None)])
    S.act("head", [(t0 + 0.02, [-0.02, 0.34, 0.02], 0.25), (W37 + 0.1, [0.04, 0.38, -0.03], 0.3), (W38, [-0.04, 0.42, 0], 0.3)])
    S.act("armL", [(t0 + 0.02, "point", 0.25), (W38 - 0.02, "present", 0.3)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W37 + 0.1, "open", 0.3)])
    S.act("torso", [(t0 + 0.02, {"chest": [0.04, 0.14, 0]}, 0.3), (W38, {"chest": [0.07, 0.18, 0], "spine": [0.03, 0.06, 0]}, 0.3)])
    S.act("root", [(t0 + 0.02, {"y": 0, "ry": 0.1, "rz": 0}, 0.3)])
    S.fx(t0 + 0.06, "sparkle", 0.04)
    S.fx(p0 + 0.05, "whoosh", 0.07)
    S.fx(t1 - 0.3, "ping", 0.06)
