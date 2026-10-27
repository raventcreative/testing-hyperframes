"""S05 — 04/06 GLASS WIDGETS (17.10–18.83)
VO: "Panelnya menangkap cahaya."
Opens on S04's end state (C|L gap at GAP filled with glass, bright rims). The C and L slide out of frame on their rails
while the gap glass grows into the hero frosted panel (~60 % width) behind the mascot, who steps in on the left, face
clear. Two more panels arrive on their own Z rails with different motion mass: a small far panel drifts down slowly
(soft, slightly out of focus) and a near panel snaps in from the left. Real thickness: an offset rim layer under each
pane, bright top hairline, soft contact shadow. Labels are illustration only ("02 / 03 / 04", a progress rail).
"cahaya": one specular glint runs left -> right along the hero panel's top edge (y = GLINT_Y) and keeps going past
the glass as a long light line; at the cut a bright horizontal beam line spans the frame at GLINT_Y -> S06 turns it
into the stage light."""
from xk import box, r3
from kit import GLINT_Y, tx, badge, shadow
from kit_b import LETTERS, letter, gap_glass, rims, GAP_C, LH, C_OPEN, L_OPEN

PUSH = {"scale": 1.083, "x": 185, "y": 70, "transformOrigin": f"{GAP_C[0]}px {GAP_C[1]}px"}   # = S04 end
HERO = (430, GLINT_Y, 600, 520)        # hero panel (x, y, w, h); its top edge carries the glint
FAR = (690, 300, 300, 170)             # small far panel (top right, above the hero)
NEAR = (70, 330, 300, 150)             # near panel (top left, above the head)
# gap glass in group coords (kit_b.gap_glass): x 169..361, y 440..1000 -> screen through PUSH
GX0, GX1, GY0, GY1 = 169, 361, 440, 1000


def to_screen(x, y):
    sc = PUSH["scale"]
    return (GAP_C[0] + (x - GAP_C[0]) * sc + PUSH["x"], GAP_C[1] + (y - GAP_C[1]) * sc + PUSH["y"])


def pane(pid, x, y, w, h, inner="", radius=26, extra=""):
    """frosted glass pane with visible thickness: an offset rim layer + the pane + top hairline + glint slot."""
    return (f'<div class="abs" id="{pid}" style="{box(x, y, w, h)}{extra}">'
            f'{shadow(20, h - 10, w - 20, 60, 0.45)}'
            f'<div class="abs" style="left:7px;top:9px;width:{w}px;height:{h}px;border-radius:{radius}px;background:rgba(41,75,119,.16)"></div>'
            f'<div class="abs glass" style="left:0;top:0;width:{w}px;height:{h}px;border-radius:{radius}px"></div>'
            f'<div class="abs" style="left:{radius}px;top:1px;width:{w - 2 * radius}px;height:2px;background:rgba(255,255,255,.95)"></div>'
            f'<div class="abs" id="{pid}-sheen" style="left:0;top:0;width:{w}px;height:{h}px;border-radius:{radius}px;'
            f'background:linear-gradient(115deg,rgba(255,255,255,0) 30%,rgba(255,255,255,.55) 48%,rgba(255,255,255,0) 62%);opacity:0"></div>'
            f'{inner}</div>')


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W36, W37, W38 = S.W(36), S.W(37), S.W(38)        # Panelnya, menangkap, cahaya
    hx, hy, hw, hh = HERO
    # ---------------------------------------------------------------- S04 end state: parted C | glass | L (exits on its rails)
    sign = [gap_glass(f"{s}-gg")]
    for ch, x, w in LETTERS[:2]:
        sign.append(letter(f"{s}-{ch}", ch, x, w))
    sign.append(rims(f"{s}-rim"))
    S.back.append(f'<div class="abs" id="{s}-sign" style="{box(0, 0, 1080, 1920)}">' + "".join(sign) + "</div>")
    # far + hero panels (back layer: behind the mascot -> real occlusion), near panel too (above the head, never on the face)
    far_in = (tx(None, 26, 26, 260, "LAYER 02", size=24, weight=700)
              + f'<div class="abs" style="left:26px;top:76px;width:120px;height:44px;border-radius:22px;background:rgba(41,75,119,.18)">'
                f'<div class="abs" style="left:4px;top:4px;width:36px;height:36px;border-radius:18px;background:linear-gradient(135deg,#0A0D2C,#294B77)"></div></div>'
              + f'<div class="abs" style="left:164px;top:86px;width:110px;height:10px;border-radius:5px;background:rgba(41,75,119,.20)"></div>'
              + f'<div class="abs" style="left:164px;top:106px;width:80px;height:10px;border-radius:5px;background:rgba(41,75,119,.14)"></div>')
    near_in = (tx(None, 26, 24, 260, "LAYER 03", size=24, weight=700)
               + "".join(f'<div class="abs" style="left:{26 + k * 46}px;top:{110 - h2}px;width:28px;height:{h2}px;border-radius:6px;'
                         f'background:linear-gradient(180deg,#294B77,#0A0D2C);opacity:{0.45 + 0.1 * k}"></div>' for k, h2 in enumerate((22, 40, 30, 52, 36))))
    rows = "".join(f'<div class="abs" style="left:150px;top:{300 + k * 52}px;width:{(380, 300, 340)[k]}px;height:14px;border-radius:7px;background:rgba(41,75,119,{(0.22, 0.16, 0.12)[k]})"></div>' for k in range(3))
    hero_in = (tx(None, 150, 40, 420, "02 / 03 / 04", size=44, weight=700)
               + tx(None, 150, 110, 420, "glass widgets", size=28, weight=400)
               + f'<div class="abs" style="left:150px;top:200px;width:{hw - 194}px;height:16px;border-radius:8px;background:rgba(41,75,119,.16)"></div>'
               + f'<div class="abs" id="{s}-prog" style="left:150px;top:200px;width:{hw - 194}px;height:16px;border-radius:8px;background:linear-gradient(90deg,#0A0D2C,#294B77)"></div>'
               + rows)
    S.back.append(pane(f"{s}-far", *FAR, inner=far_in, radius=22, extra="filter:blur(1.2px)"))
    S.back.append(pane(f"{s}-hero", hx, hy, hw, hh, inner=hero_in, radius=30))
    S.back.append(pane(f"{s}-near", *NEAR, inner=near_in, radius=22))
    # the glint + the light line it becomes (back layer, behind the mascot)
    S.back.append(f'<div class="abs glint" id="{s}-gl" style="{box(hx - 40, GLINT_Y - 3, 240, 6)}border-radius:3px"></div>')
    S.back.append(f'<div class="abs glint" id="{s}-beamR" style="{box(hx, GLINT_Y - 3, 1080 - hx + 40, 6)}border-radius:3px"></div>')
    S.back.append(f'<div class="abs glint" id="{s}-beamL" style="{box(-40, GLINT_Y - 3, hx + 40, 6)}border-radius:3px"></div>')

    # ---------------------------------------------------------------- motion
    # sign: hold S04's end transform, then the C and L slide out of frame on their rails
    S.init(f"#{s}-sign", PUSH)
    S.init(f"#{s}-C", {"x": C_OPEN, "rotationY": -16, "transformOrigin": "0% 50%", "transformPerspective": 1200})
    S.ft(f"#{s}-C", {"x": C_OPEN, "rotationY": -16}, {"x": C_OPEN - 520, "rotationY": -30}, t0 + 0.04, 0.42, "power3.in")
    S.init(f"#{s}-L", {"x": L_OPEN, "rotationY": 12, "transformOrigin": "100% 50%", "transformPerspective": 1200})
    S.ft(f"#{s}-L", {"x": L_OPEN, "rotationY": 12}, {"x": L_OPEN + 900, "rotationY": 24}, t0 + 0.04, 0.42, "power3.in")
    for k in range(2):
        S.init(f"#{s}-rim-r{k}", {"opacity": 1})
        S.ft(f"#{s}-rim-r{k}", {"opacity": 1}, {"opacity": 0}, t0 + 0.1, 0.2, "power2.in")
    # the gap glass becomes the hero panel: hero starts exactly on the gap glass rect and grows into place
    gx0, gy0 = to_screen(GX0, GY0)
    gx1, gy1 = to_screen(GX1, GY1)
    sx, sy = (gx1 - gx0) / hw, (gy1 - gy0) / hh
    S.init(f"#{s}-gg", {"opacity": 1})
    S.tset(f"#{s}-gg", {"opacity": 0}, t0 + 0.06)
    a = {"x": r3(gx0 - hx), "y": r3(gy0 - hy), "scaleX": r3(sx), "scaleY": r3(sy), "transformOrigin": "0% 0%"}
    S.init(f"#{s}-hero", dict(a, opacity=0))
    S.tset(f"#{s}-hero", {"opacity": 1}, t0 + 0.06)
    S.ft(f"#{s}-hero", a, {"x": 0, "y": 0, "scaleX": 1, "scaleY": 1}, t0 + 0.06, 0.5, "power3.out")           # heavy: slow settle
    S.init(f"#{s}-prog", {"scaleX": 0.15, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-prog", {"scaleX": 0.15}, {"scaleX": 0.62}, t0 + 0.4, 0.7, "power2.inOut")
    # far panel: distant, drifts down slowly (lightest mass, longest ease)
    S.init(f"#{s}-far", {"y": -70, "opacity": 0, "scale": 0.9})
    S.ft(f"#{s}-far", {"y": -70, "opacity": 0, "scale": 0.9}, {"y": 0, "opacity": 1, "scale": 1}, t0 + 0.14, 0.85, "sine.out")
    # near panel: closest, snaps in from the left with a small overshoot
    S.init(f"#{s}-near", {"x": -420, "rotation": -4})
    S.ft(f"#{s}-near", {"x": -420, "rotation": -4}, {"x": 0, "rotation": 0}, W36 + 0.04, 0.42, "back.out(1.6)")
    # "menangkap cahaya": sheens wake up in depth order, then the glint runs and becomes the light line
    for k, p in enumerate(("far", "hero", "near")):
        sel = f"#{s}-{p}-sheen"
        S.init(sel, {"opacity": 0, "x": -60})
        S.ft(sel, {"opacity": 0, "x": -60}, {"opacity": 1, "x": 0}, W37 + k * 0.08, 0.25, "power2.out")
        S.ft(sel, {"opacity": 1, "x": 0}, {"opacity": 0.35, "x": 60}, W37 + 0.25 + k * 0.08, 0.35, "power2.inOut")
    g0 = W38 - 0.06
    S.init(f"#{s}-gl", {"x": 0, "opacity": 0})
    S.tset(f"#{s}-gl", {"opacity": 1}, g0)
    S.ft(f"#{s}-gl", {"x": 0}, {"x": hw - 120}, g0, 0.34, "power2.in")
    S.tset(f"#{s}-gl", {"opacity": 0}, g0 + 0.36)
    S.init(f"#{s}-beamR", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-beamR", {"scaleX": 0}, {"scaleX": 1}, g0 + 0.1, 0.4, "power3.in")
    S.init(f"#{s}-beamL", {"scaleX": 0, "transformOrigin": "100% 50%"})
    S.ft(f"#{s}-beamL", {"scaleX": 0}, {"scaleX": 1}, g0 + 0.32, t1 - g0 - 0.34, "power2.out")

    # ---------------------------------------------------------------- mascot: steps in left, face clear; turns into the light
    v = {"fx": 230, "fy": 1830, "h": 1120, "yaw": 16, "pitch": 5}
    S.mset("V", {"vis": 1}, t0)
    S.mv([(t0, dict(v, fx=-120, yaw=30), None), (t0 + 0.45, v, "power3.out"), (W38, dict(v, yaw=22), "sine.inOut"), (t1, dict(v, fx=240, yaw=26), "sine.inOut")])
    S.act("head", [(t0, [-0.05, 0.3, 0.0], 0.3), (W36, [-0.1, 0.36, 0.03], 0.3), (W37, [-0.14, 0.24, 0.0], 0.3), (W38 - 0.05, [-0.06, 0.48, -0.04], 0.3)])
    S.act("armL", [(t0, "low", 0.3), (W36 - 0.12, "present", 0.3), (W38 - 0.1, "open", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (W37, "palmUp", 0.3), (W38 + 0.2, "low", 0.4)])
    S.act("torso", [(t0, {"chest": [0.0, 0.08, 0.0]}, 0.4), (W38 - 0.05, {"chest": [-0.04, 0.16, 0.0]}, 0.3)])
    S.act("root", [(t0, {"ry": 0.12}, 0.4)])
    # ---------------------------------------------------------------- sound: glass ticks + the light line
    S.fx(t0 + 0.05, "whoosh", 0.05)
    S.fx(W36 + 0.1, "pop", 0.05)
    S.fx(W38, "ping", 0.06)
