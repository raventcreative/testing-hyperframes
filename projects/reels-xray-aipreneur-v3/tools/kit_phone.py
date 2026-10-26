"""Phone rig for S01/S02 — the user's mechanical phone photo, dissected (tools/assets_phone.py) and rebuilt:

  placement (static, scene px)  >  {pre}-float (bob)  >  {pre}-punch (scale punch)  >  rig 1122x1402 (photo px)
     body.webp (flat photo layer: ivory/navy body, gears, glass removed)
     {pre}-r3  perspective container (f = 5900 px at the photo centre; the photo is near-orthographic)
       {pre}-face  CSS matrix3d = the face plane's 3D pose solved from the photo (exact homography columns)
         gear sprites (rectified circles -> rotate as real in-plane gears), seam light, latch pins, glass shadow
         {pre}-glass  real 3D glass panel (navy rim, notch, thickness, screen content, specular), GSAP x/y/z/rotations
Everything inside the rig is flattened into the placement card, so the scene camera treats the phone as one object.
"""
import json, math
from pathlib import Path
import numpy as np
from xk import box, r3, Rng

P = Path(__file__).resolve().parents[1]
META = json.loads((P / "assets/elements/xray/phone/phone.json").read_text())
IW, IH = META["image"]
FW, FH = META["FW"], META["FH"]
GW, GH = META["glass"]["w"], META["glass"]["h"]
GX0, GY0 = META["glass"]["closed"]
OPEN = {"x": META["glass"]["open"][0] - GX0, "y": META["glass"]["open"][1] - GY0, "z": META["glass"]["open"][2]}
M4 = np.array(META["matrix3d"]).reshape(4, 4).T          # column-major in json -> 4x4
F, CX, CY = META["f"], META["cx"], META["cy"]
GEARS = META["gears"]
GR = 46                                                    # glass corner radius (face-local px)


def rig_point(u, v, w=0.0):
    """face-local point -> photo/rig px (after the rig perspective)."""
    p = M4 @ np.array([u, v, w, 1.0]); s = F / (F - p[2])
    return (CX + (p[0] - CX) * s, CY + (p[1] - CY) * s)


class Placement:
    """rig px -> scene px: scene = (rig - anchor) * scale + at."""
    def __init__(self, scale, anchor, at):
        self.s, self.ax, self.ay, self.x, self.y = scale, anchor[0], anchor[1], at[0], at[1]
    def pt(self, rx, ry):
        return (self.x + (rx - self.ax) * self.s, self.y + (ry - self.ay) * self.s)
    def style(self):
        # the rig's top-left goes to pt(0, 0); scale about the top-left corner
        x0, y0 = self.pt(0, 0)
        return f"left:{r3(x0)}px;top:{r3(y0)}px;width:{IW}px;height:{IH}px;transform-origin:0 0;transform:scale({r3(self.s)})"


def glass_point(dx=0.0, dy=0.0, dz=0.0, fu=0.5, fv=0.5):
    """point at fraction (fu, fv) of the glass, with the glass translated by (dx, dy, dz) (no rotation)."""
    return rig_point(GX0 + dx + GW * fu, GY0 + dy + GH * fv, dz + 1.0)


def phone_rig(pre, place, mini_html):
    """markup for the whole phone (ids prefixed with pre). mini_html = mini Reel markup for the screen."""
    m3 = ",".join(r3(v) for v in META["matrix3d"])
    g = []
    # glass shadow on the face (moves/softens with the lift)
    g.append(f'<div class="abs" id="{pre}-gsh" style="{box(GX0 + 6, GY0 + 10, GW, GH)}border-radius:{GR}px;background:rgba(14,26,48,.55);filter:blur(6px);opacity:0"></div>')
    # gear sprites (centre/radius in face-local px)
    for name, (gx, gy, rr) in GEARS.items():
        g.append(f'<img class="abs" id="{pre}-{name}" src="assets/elements/xray/phone/gear_{name}.webp" alt="" style="{box(gx - rr, gy - rr, 2 * rr, 2 * rr)}" />')
    # seam light around the screen edge + travelling glint
    g.append(f'<div class="abs" id="{pre}-seam" style="{box(GX0 - 3, GY0 - 3, GW + 6, GH + 6)}border-radius:{GR + 3}px;border:3px solid #ffffff;'
             f'box-shadow:0 0 14px 3px rgba(203,219,244,.95),0 0 34px 6px rgba(172,198,231,.8),inset 0 0 12px rgba(203,219,244,.8);opacity:0"></div>')
    # latch pins (left / right edge, slide outward on unlock)
    for k, (px, py, side) in enumerate(((GX0 - 2, GY0 + GH * 0.30, -1), (GX0 - 2, GY0 + GH * 0.66, -1), (GX0 + GW - 18, GY0 + GH * 0.30, 1), (GX0 + GW - 18, GY0 + GH * 0.66, 1))):
        g.append(f'<div class="abs" id="{pre}-pin{k}" style="{box(px, py, 20, 46)}border-radius:6px;background:linear-gradient(90deg,#e8eef7,#9fb6d6 45%,#3a6299);'
                 f'box-shadow:0 2px 3px rgba(14,26,48,.5),inset 1px 1px 0 rgba(255,255,255,.8)"></div>')
    # ---- the glass panel (3D)
    glass = (
        f'<div class="abs p3" id="{pre}-glass" style="{box(GX0, GY0, GW, GH)}">'
        # thickness: two navy edge layers behind the front face
        f'<div class="abs" style="{box(0, 0, GW, GH)}border-radius:{GR}px;border:7px solid #1c3354;transform:translateZ(-5px)"></div>'
        f'<div class="abs" style="{box(0, 0, GW, GH)}border-radius:{GR}px;border:7px solid #294b77;transform:translateZ(-2.5px)"></div>'
        # screen content (ON while closed)
        f'<div class="abs" id="{pre}-scr" style="{box(9, 9, GW - 18, GH - 18)}border-radius:{GR - 8}px;overflow:hidden;'
        f'background:linear-gradient(170deg,#fbfcfe 0%,#eef3fa 60%,#dfe8f5 100%)">{mini_html}</div>'
        # glass body: faint tint + gloss
        f'<div class="abs" id="{pre}-gfill" style="{box(0, 0, GW, GH)}border-radius:{GR}px;'
        f'background:linear-gradient(150deg,rgba(255,255,255,.34) 0%,rgba(232,240,251,.10) 38%,rgba(203,219,244,.06) 60%,rgba(255,255,255,.26) 100%)"></div>'
        f'<div class="abs" id="{pre}-gwhite" style="{box(0, 0, GW, GH)}border-radius:{GR}px;opacity:0;'
        f'background:linear-gradient(160deg,rgba(255,255,255,.95),rgba(232,240,251,.85) 60%,rgba(214,228,247,.8))"></div>'
        # rim: navy enamel ring + inner ice highlight + outer light edge
        f'<div class="abs" style="{box(0, 0, GW, GH)}border-radius:{GR}px;border:7px solid #294b77;'
        f'box-shadow:inset 0 0 0 1.5px rgba(203,219,244,.95),0 0 0 1px rgba(255,255,255,.7)"></div>'
        # notch pill with two lenses
        f'<div class="abs" style="{box(GW / 2 - 52, 20, 104, 26)}border-radius:13px;background:linear-gradient(180deg,#1c3354,#0f1d33);box-shadow:inset 0 1px 1px rgba(255,255,255,.25)">'
        f'<div class="abs" style="{box(14, 8, 10, 10)}border-radius:50%;background:#3a6299"></div><div class="abs" style="{box(80, 8, 10, 10)}border-radius:50%;background:#3a6299"></div></div>'
        # specular sweep (moves across on the apex)
        f'<div class="abs" style="{box(0, 0, GW, GH)}border-radius:{GR}px;overflow:hidden">'
        f'<div class="abs" id="{pre}-spec" style="{box(-260, -200, 150, GH + 400)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.75),rgba(255,255,255,0))"></div></div>'
        f'</div>')
    g.append(glass)
    face = (f'<div class="abs p3" id="{pre}-face" style="left:0;top:0;width:{FW}px;height:{FH}px;transform-origin:0 0 0;transform:matrix3d({m3})">'
            + "".join(g) + "</div>")
    rig = (f'<div class="abs" style="{place.style()}">'
           f'<div class="abs" id="{pre}-float" style="left:0;top:0;width:{IW}px;height:{IH}px">'
           f'<div class="abs" id="{pre}-punch" style="left:0;top:0;width:{IW}px;height:{IH}px">'
           f'<img class="abs" id="{pre}-body" src="assets/elements/xray/phone/body.webp" alt="" style="left:0;top:0;width:{IW}px;height:{IH}px" />'
           f'<div class="abs" id="{pre}-r3" style="left:0;top:0;width:{IW}px;height:{IH}px;perspective:{int(F)}px;perspective-origin:{r3(CX)}px {r3(CY)}px">{face}</div>'
           f'</div></div></div>')
    return rig


# ------------------------------------------------------------------ gear motion (continuous across S01 -> S02)
SPIN0 = 2.56                     # "mesin."
SPEED = {"g1": 130.0, "g2": -160.0, "g4": 320.0, "g5": -210.0}   # deg/s at cruise
BOOST = 1.9                      # cruise multiplier after "kebuka."


def gear_angle(name, t, kebuka):
    """deterministic gear angle (deg): power2-in spin-up from SPIN0 to 3.24, cruise, faster after kebuka."""
    v = SPEED[name]
    if t <= SPIN0:
        return 0.0
    T1 = 3.24
    if t <= T1:
        u = (t - SPIN0) / (T1 - SPIN0); return v * (T1 - SPIN0) / 2 * u * u
    a1 = v * (T1 - SPIN0) / 2
    if t <= kebuka:
        return a1 + v * (t - T1)
    a2 = a1 + v * (kebuka - T1)
    return a2 + v * BOOST * (t - kebuka)


def gears_motion(S, pre, a, b, kebuka=4.38):
    """gear tweens for scene window [a, b] (global s): continuous angles, piecewise eases matching gear_angle."""
    for name in SPEED:
        sel = f"#{pre}-{name}"
        S.init(sel, {"rotation": gear_angle(name, a, kebuka)})
        cuts = sorted({a, b, *[c for c in (SPIN0, 3.24, kebuka) if a < c < b]})
        for t0, t1 in zip(cuts, cuts[1:]):
            if t1 <= SPIN0:
                continue
            ease = "power2.in" if t1 <= 3.24 and t0 >= SPIN0 else "none"
            S.ft(sel, {"rotation": gear_angle(name, t0, kebuka)}, {"rotation": gear_angle(name, t1, kebuka)}, t0, t1 - t0, ease)
    # the big balance wheel ticks back and forth (a bridge crosses it, so it oscillates instead of spinning);
    # sampled every 1/15 s (linear between samples) so S01 and S02 meet exactly
    sel = f"#{pre}-g3"
    S.init(sel, {"rotation": balance_angle(a)})
    t = max(a, SPIN0)
    while t < b - 1e-4:
        t1 = min(b, t + 1 / 15)
        S.ft(sel, {"rotation": balance_angle(t)}, {"rotation": balance_angle(t1)}, t, t1 - t, "none")
        t = t1


def balance_angle(t, amp=16.0, period=0.56):
    if t <= SPIN0:
        return 0.0
    ramp = min(1.0, (t - SPIN0) / 0.35)
    return amp * ramp * math.sin(2 * math.pi * (t - SPIN0) / period)


# ------------------------------------------------------------------ REF-H apex (flash + shockwave + 4-point stars)
STAR = "M20 2 C21 14 26 19 38 20 C26 21 21 26 20 38 C19 26 14 21 2 20 C14 19 19 14 20 2Z"


def apex_h(S, layer, aid, x, y, at, size=560, stars=12, seed=5, punch=None):
    layer.append(f'<div class="bloom" id="{aid}-fl" style="{box(x - size / 2, y - size / 2, size, size)}"></div>')
    S.init(f"#{aid}-fl", {"opacity": 0, "scale": 0.35})
    S.ft(f"#{aid}-fl", {"opacity": 0, "scale": 0.35}, {"opacity": 0.95, "scale": 0.85}, at - 0.06, 0.1, "power2.in")
    S.ft(f"#{aid}-fl", {"opacity": 0.95, "scale": 0.85}, {"opacity": 0, "scale": 1.3}, at + 0.04, 0.3, "power2.out")
    rs = size * 0.36
    layer.append(f'<div class="abs" id="{aid}-sw" style="{box(x - rs / 2, y - rs / 2, rs, rs)}border-radius:50%;border:5px solid rgba(255,255,255,.95);'
                 f'box-shadow:0 0 30px rgba(172,198,231,.9),inset 0 0 24px rgba(172,198,231,.7)"></div>')
    S.init(f"#{aid}-sw", {"opacity": 0, "scale": 0.4})
    S.ft(f"#{aid}-sw", {"opacity": 0.95, "scale": 0.4}, {"opacity": 0, "scale": 1.8}, at, 0.6, "power3.out")
    R = Rng(seed)
    for k in range(stars):
        ang = 2 * math.pi * (k + R.u(0, 0.7)) / stars
        dist = R.u(size * 0.22, size * 0.48)
        sz = R.u(18, 34)
        sid = f"{aid}-st{k}"
        layer.append(f'<svg class="abs" id="{sid}" width="{r3(sz)}" height="{r3(sz)}" viewBox="0 0 40 40" style="left:{r3(x - sz / 2)}px;top:{r3(y - sz / 2)}px;overflow:visible">'
                     f'<path d="{STAR}" fill="#ffffff" stroke="#acc6e7" stroke-width="1.5"/></svg>')
        dx, dy = dist * math.cos(ang), dist * math.sin(ang)
        d0 = R.u(0, 0.08)
        S.init(f"#{sid}", {"opacity": 0, "scale": 0.2})
        S.ft(f"#{sid}", {"opacity": 0, "x": 0, "y": 0, "scale": 0.2, "rotation": 0},
             {"opacity": 1, "x": dx * 0.7, "y": dy * 0.7, "scale": 1.0, "rotation": 30}, at + d0, 0.28, "power3.out")
        S.ft(f"#{sid}", {"opacity": 1, "x": dx * 0.7, "y": dy * 0.7, "scale": 1.0, "rotation": 30},
             {"opacity": 0, "x": dx, "y": dy, "scale": 0.35, "rotation": 70}, at + d0 + 0.28, 0.42, "power2.in")
    if punch:
        S.ft(punch, {"scale": 1}, {"scale": 1.045}, at, 0.1, "power2.out")
        S.ft(punch, {"scale": 1.045}, {"scale": 1}, at + 0.1, 0.22, "power2.inOut")


def bokeh_far(seed, n=6):
    """REF-H far plane: blurred porcelain discs (translateZ -520, scale 1.26)."""
    R = Rng(seed)
    out = []
    for k in range(n):
        d = R.u(70, 190); x = R.u(40, 1040); y = R.u(420, 1580)
        out.append(f'<div class="abs" style="{box(x - d / 2, y - d / 2, d, d)}border-radius:50%;filter:blur(7px);opacity:.62;'
                   f'background:radial-gradient(circle at 35% 30%,#ffffff,#e8f0fb 45%,#acc6e7 100%)"></div>')
    return out
