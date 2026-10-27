"""S05 — DIGITAL ZOOM. Medium shot; a real camera punch-in 1.7x in 0.1 s onto the eyes (mascot re-framed via S.mv,
the soft studio world behind scales with it around the same point), 3 px left-right shake for 0.15 s, and a big
accent keyword under the face lands 1.8 -> 1. Released, then punched a second time with a second keyword."""
from xk import box, r3
from kit import MED

P0 = (540, 676)          # zoom centre: keeps the eyes (MED y~555) landing at y~470 at 1.7x
Z = 1.7


def zoomed(v):
    return dict(v, fx=P0[0] + Z * (v["fx"] - P0[0]), fy=P0[1] + Z * (v["fy"] - P0[1]), h=v["h"] * Z)


def build(S):
    s, t0 = S.id, S.t0
    # ---------------------------------------------------------------- back: soft studio world (scales with the punch)
    dots = "".join(f'<div class="abs" style="{box(x - d / 2, y - d / 2, d, d)}border-radius:50%;background:radial-gradient(circle,rgba(41,75,119,{a}) 0%,rgba(41,75,119,0) 70%)"></div>'
                   for x, y, d, a in [(150, 220, 260, .16), (930, 300, 300, .14), (120, 860, 340, .12), (960, 900, 280, .14), (540, 120, 200, .08)])
    S.back.append(f'<div class="abs" id="{s}-world" style="left:0;top:0;width:1080px;height:1080px">'
                  f'<div class="abs grid-fine" style="left:-60px;top:-60px;width:1200px;height:1200px;opacity:.7"></div>{dots}'
                  f'<div class="abs" style="{box(240, 980, 600, 60)}border-radius:50%;background:radial-gradient(ellipse,rgba(10,13,44,.18),rgba(10,13,44,0) 70%)"></div></div>')
    # ---------------------------------------------------------------- front: keywords under the face
    for k, word in enumerate(["HOOK!", "VIRAL"]):
        S.front.append(f'<div class="abs" id="{s}-k{k}" style="{box(140, 770, 800, 150)}display:flex;align-items:center;justify-content:center">'
                       f'<span class="badge" style="font:700 112px/1 Poppins, sans-serif;padding:14px 40px 18px;border-radius:26px;letter-spacing:.02em;'
                       f'box-shadow:0 26px 50px -20px rgba(10,13,44,.65),0 0 0 4px rgba(255,255,255,.9)">{word}</span></div>')
        S.init(f"#{s}-k{k}", {"opacity": 0, "scale": 1.8, "transformOrigin": "50% 50%"})
    S.init(f"#{s}-world", {"scale": 1, "transformOrigin": f"{P0[0]}px {P0[1]}px"})

    v0 = dict(MED, yaw=-4)
    vz = zoomed(dict(MED, yaw=0))
    v1 = dict(MED, yaw=5)
    vz2 = zoomed(dict(MED, yaw=2))
    p1, r1, p2 = t0 + 0.45, t0 + 2.05, t0 + 2.75
    S.mv([(t0, v0, None), (p1, dict(v0, yaw=0), "sine.inOut"), (p1 + 0.1, vz, "power3.out"), (r1, dict(vz, yaw=-2), "sine.inOut"),
          (r1 + 0.28, v1, "power3.inOut"), (p2, v1, "none"), (p2 + 0.1, vz2, "power3.out"), (S.t1, dict(vz2, yaw=-1), "sine.inOut")])
    # 3 px left-right shake for 0.15 s right after each punch (camera + world + keyword shake together)
    for p in (p1, p2):
        a = p + 0.1
        S.mx([(a, {"x": 0}, None), (a + 0.0375, {"x": 3}, "none"), (a + 0.075, {"x": -3}, "none"), (a + 0.1125, {"x": 3}, "none"), (a + 0.15, {"x": 0}, "none")])
        S.ft(f"#{s}-world", {"x": 0}, {"x": 3}, a, 0.0375, "none")
        S.ft(f"#{s}-world", {"x": 3}, {"x": -3}, a + 0.0375, 0.0375, "none")
        S.ft(f"#{s}-world", {"x": -3}, {"x": 3}, a + 0.075, 0.0375, "none")
        S.ft(f"#{s}-world", {"x": 3}, {"x": 0}, a + 0.1125, 0.0375, "none")
    S.ft(f"#{s}-world", {"scale": 1}, {"scale": Z}, p1, 0.1, "power3.out")
    S.ft(f"#{s}-world", {"scale": Z}, {"scale": 1}, r1, 0.28, "power3.inOut")
    S.ft(f"#{s}-world", {"scale": 1}, {"scale": Z}, p2, 0.1, "power3.out")
    # keyword lands 1.8 -> 1 with the punch, leaves on the release
    S.ft(f"#{s}-k0", {"opacity": 0, "scale": 1.8}, {"opacity": 1, "scale": 1}, p1 + 0.04, 0.22, "power3.out")
    S.ft(f"#{s}-k0", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.8}, r1 - 0.02, 0.16, "power2.in")
    S.ft(f"#{s}-k1", {"opacity": 0, "scale": 1.8}, {"opacity": 1, "scale": 1}, p2 + 0.04, 0.22, "power3.out")
    for k, a in ((0, p1 + 0.26), (1, p2 + 0.26)):
        S.ft(f"#{s}-k{k}", {"x": 0}, {"x": 3}, a, 0.0375, "none")
        S.ft(f"#{s}-k{k}", {"x": 3}, {"x": -3}, a + 0.0375, 0.0375, "none")
        S.ft(f"#{s}-k{k}", {"x": -3}, {"x": 0}, a + 0.075, 0.05, "none")
    # acting: settles, leans into the punch with a small nod, explains between punches
    S.act("armL", [(t0, "together", 0.01), (p1 - 0.1, "fist", 0.2), (r1 + 0.05, "explain", 0.3), (p2 - 0.1, "pointUp", 0.2)])
    S.act("armR", [(t0, "together", 0.01), (p1 - 0.1, "fist", 0.2), (r1 + 0.05, "palmUp", 0.3), (p2 - 0.1, "fist", 0.2)])
    S.act("head", [(t0, [0, -0.08, 0.02], 0.01), (p1 - 0.05, [0.1, 0, 0], 0.12), (p1 + 0.25, [-0.03, 0.02, -0.03], 0.35),
                   (r1 + 0.05, [-0.04, 0.12, 0.04], 0.35), (p2 - 0.05, [0.1, 0, 0], 0.12), (p2 + 0.25, [-0.03, -0.04, 0.03], 0.35)])
    S.act("torso", [(t0, {}, 0.01), (p1 - 0.05, {"chest": [0.06, 0, 0]}, 0.15), (p1 + 0.3, {}, 0.4), (p2 - 0.05, {"chest": [0.06, 0, 0]}, 0.15), (p2 + 0.3, {}, 0.4)])
