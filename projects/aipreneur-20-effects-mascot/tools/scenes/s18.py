"""S18 — 17 FRAME BREAK (30.80–31.40)  VO: "pecahkan layar,"
First frame = S17's last frame as 16 assembled shards (polygon copies of the self-shot `city_end_full.jpg`).
'pecahkan': cracks race out from the face (one controlled cyan-white burst = HERO APEX), the pieces separate,
then fall away toward lower-left, inner pieces first, tilting in 3D with edge glints and cast shadows, revealing
the mascot (medium, unclipped) under the camera HUD. Four edge glints fly into the corners and become the HUD
corner guides of S19 (contract HUD)."""
import math
from xk import box, r3, apex, Rng
from kit import MED, HUD, SELF, corner_frame
from kit_d import shards

ORIGIN = (540, 1006)        # S17 end: face of the WIDE framing pushed to h 1230 / fy 1740
IMG = f"{SELF}/city_end_full.jpg"
GLOW0 = "drop-shadow(0px 0px 0px rgba(220,250,255,0)) drop-shadow(0px 0px 0px rgba(3,8,28,0))"
GLOW1 = "drop-shadow(0px 0px 2px rgba(220,250,255,0.95)) drop-shadow(0px 22px 26px rgba(3,8,28,0.65))"


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W86, W87 = S.W(86), S.W(87)            # pecahkan 30.88, layar 31.28
    crack = W86 + 0.02
    fall = crack + 0.1
    pcs = shards(ORIGIN)
    # ---------------------------------------------------------------- back: dark vignette behind the revealed HUD shot
    S.back.append(f'<div class="abs" style="{box(0, 0, 1080, 1920)}background:radial-gradient(ellipse at 50% 45%,rgba(4,9,23,0) 40%,rgba(4,9,23,.55) 100%)"></div>')
    # ---------------------------------------------------------------- front: shards over the mascot, crack lines, corner glints
    G = Rng(1888)
    for k, (pts, (cx, cy), ring, ang) in enumerate(pcs):
        poly = ",".join(f"{r3(x)}px {r3(y)}px" for x, y in pts)
        S.front.append(f'<div class="abs p3" id="{s}-pw{k}" style="{box(0, 0, 1080, 1920)}">'
                       f'<div class="abs" style="{box(0, 0, 1080, 1920)}background:#0b1636 url({IMG}) 0 0 / 1080px 1920px no-repeat;clip-path:polygon({poly})"></div></div>')
        # 1) crack: tiny outward separation
        dx, dy = math.cos(ang), math.sin(ang)
        sep = 5 + 5 * ring
        a = {"x": 0, "y": 0, "rotation": 0, "rotationX": 0, "rotationY": 0, "scale": 1, "opacity": 1, "filter": GLOW0,
             "transformOrigin": f"{r3(cx)}px {r3(cy)}px", "transformPerspective": 1200}
        b = {"x": r3(dx * sep), "y": r3(dy * sep), "rotation": r3(G.u(-2, 2)), "rotationX": 0, "rotationY": 0, "scale": 1, "opacity": 1, "filter": GLOW1}
        # 2) fall toward lower-left, one consistent direction, inner first
        dist = math.hypot(cx - ORIGIN[0], cy - ORIGIN[1])
        delay = 0.03 * ring + min(0.08, dist / 9000) + G.u(0, 0.03)
        c = {"x": r3(dx * sep * 4 - G.u(260, 520)), "y": r3(dy * sep * 3 + G.u(700, 1150)), "rotation": r3(-G.u(18, 55)),
             "rotationX": r3(G.u(25, 70)), "rotationY": r3(-G.u(10, 40)), "scale": r3(G.u(1.05, 1.25)), "opacity": 1, "filter": GLOW1}
        d = dict(c, opacity=0)
        S.init(f"#{s}-pw{k}", a)
        S.ft(f"#{s}-pw{k}", {kk: a[kk] for kk in b}, b, crack, 0.08, "power3.out")
        S.ft(f"#{s}-pw{k}", b, c, fall + delay, 0.3, "power2.in")
        S.ft(f"#{s}-pw{k}", {"opacity": 1}, {"opacity": 0}, fall + delay + 0.16, 0.12, "none")
    # crack lines (draw outward from the face), above the shards
    paths = []
    for k, (pts, _c, ring, _a) in enumerate(pcs):
        if ring == 0:
            p0, p1, pm, p2 = pts
            paths.append(f"M{r3(p0[0])},{r3(p0[1])} L{r3(p1[0])},{r3(p1[1])}")
            paths.append(f"M{r3(p1[0])},{r3(p1[1])} L{r3(pm[0])},{r3(pm[1])} L{r3(p2[0])},{r3(p2[1])}")
        else:
            q0, q1 = pts[0], pts[1]
            paths.append(f"M{r3(q0[0])},{r3(q0[1])} L{r3(q1[0])},{r3(q1[1])}")
    S.front.append(f'<svg class="abs" id="{s}-cracks" style="{box(0, 0, 1080, 1920)}overflow:visible" viewBox="0 0 1080 1920">'
                   + "".join(f'<path id="{s}-ck{k}" d="{d}" fill="none" stroke="#e9fbff" stroke-width="3" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" '
                             f'style="filter:drop-shadow(0 0 5px rgba(0,208,254,.9))"/>' for k, d in enumerate(paths))
                   + "</svg>")
    for k in range(len(paths)):
        S.init(f"#{s}-ck{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-ck{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, crack - 0.01 + 0.004 * k, 0.09, "power2.out")
    S.init(f"#{s}-cracks", {"opacity": 1})
    S.ft(f"#{s}-cracks", {"opacity": 1}, {"opacity": 0}, fall + 0.02, 0.1, "power1.in")
    apex(S, S.front, f"{s}-ap", ORIGIN[0], ORIGIN[1], crack + 0.02, size=760, sparks=10, seed=1809, op=0.75)
    # edge glints fly into the HUD corners and become the corner guides (S19 opens on the same guides)
    x, y, w, h = HUD
    corners = ((x, y), (x + w, y), (x, y + h), (x + w, y + h))
    starts = ((-30, 160), (1110, 220), (-40, 1700), (1120, 1760))
    for k, ((cx, cy), (sx, sy)) in enumerate(zip(corners, starts)):
        S.front.append(f'<div class="abs" id="{s}-g{k}" style="{box(cx - 26, cy - 26, 52, 52)}clip-path:polygon(50% 0,100% 60%,30% 100%);'
                       f'background:linear-gradient(135deg,rgba(255,255,255,.95),rgba(0,208,254,.6))"></div>')
        S.init(f"#{s}-g{k}", {"x": sx - cx, "y": sy - cy, "rotation": -90, "opacity": 0, "scale": 1.4})
        S.ft(f"#{s}-g{k}", {"x": sx - cx, "y": sy - cy, "rotation": -90, "opacity": 0, "scale": 1.4},
             {"x": 0, "y": 0, "rotation": 30, "opacity": 1, "scale": 0.6}, fall + 0.06 + 0.02 * k, 0.2, "power3.out")
        S.ft(f"#{s}-g{k}", {"opacity": 1, "scale": 0.6}, {"opacity": 0, "scale": 0.2}, fall + 0.26 + 0.02 * k, 0.08, "power1.in")
    S.front.append(f'<div class="abs" id="{s}-hud" style="{box(0, 0, 1080, 1920)}">' + corner_frame(f"{s}-hud", x, y, w, h, arm=80, th=5) + "</div>")
    S.init(f"#{s}-hud", {"opacity": 0, "scale": 1.06, "transformOrigin": f"{x + w / 2}px {y + h / 2}px"})
    S.ft(f"#{s}-hud", {"opacity": 0, "scale": 1.06}, {"opacity": 1, "scale": 1}, fall + 0.2, 0.16, "power3.out")

    # ---------------------------------------------------------------- mascot: the revealed shot = S19 at 1.0x (medium hero)
    S.mv([(t0, dict(MED), None), (t1, dict(MED, yaw=-3), "sine.inOut")])
    S.act("head", [(t0, [0.02, 0.0, 0.0], 0.2), (fall + 0.2, [-0.06, -0.05, 0.04], 0.3)])
    S.act("armL", [(t0, "low", 0.3), (fall + 0.15, "open", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (fall + 0.15, "open", 0.3)])
    S.act("torso", [(t0, {"chest": [-0.04, 0, 0]}, 0.25), (fall + 0.3, {}, 0.35)])
    S.fx(crack, "click", 0.09)
    S.fx(crack + 0.03, "sparkle", 0.06)
    S.fx(fall + 0.05, "whoosh", 0.06)
