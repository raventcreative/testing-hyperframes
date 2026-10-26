"""Helpers for scenes s05–s09 (blueprint, input machine, stage, timing wheel, render press)."""
import math
from xk import box, r3, Rng


def backdrop(S, seed=1, arch=True, shelf_y=1410):
    """far plane: soft porcelain arch + shelf rails + a few etched tick marks (pushed back, scaled)."""
    R = Rng(seed)
    ticks = "".join(f'<div class="abs" style="{box(180 + k * 36, shelf_y - 30, 2, 10 if k % 5 else 18)}background:rgba(41,75,119,.18)"></div>' for k in range(21))
    inner = ""
    if arch:
        inner += (f'<div class="abs por-dim" style="{box(220, 260, 740, 1190)}border-radius:370px 370px 36px 36px;opacity:.5"></div>'
                  f'<div class="abs" style="{box(270, 320, 640, 1100)}border-radius:320px 320px 26px 26px;border:2px solid rgba(255,255,255,.85)"></div>')
    inner += (f'<div class="abs" style="{box(120, shelf_y, 940, 6)}border-radius:3px;background:rgba(172,198,231,.55)"></div>'
              f'<div class="abs" style="{box(120, shelf_y + 22, 940, 3)}border-radius:2px;background:rgba(172,198,231,.35)"></div>' + ticks)
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">{inner}</div>')


def near_blur(S, pieces):
    """near plane pieces: list of (id, x, y, w, h, css)."""
    inner = "".join(f'<div class="abs" id="{i}" style="{box(x, y, w, h)}{css}"></div>' for (i, x, y, w, h, css) in pieces)
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">{inner}</div>')


def code_lines(prefix, x, y, w, n, seed=3, gap=22, h=8, ink_every=3):
    """abstract engraved code: indented bars (never readable words)."""
    R = Rng(seed)
    out, ind = [], 0
    for k in range(n):
        if k % 4 == 0:
            ind = 0
        elif R.f() < 0.45:
            ind = min(3, ind + 1)
        elif R.f() < 0.3:
            ind = max(0, ind - 1)
        lw = w * R.u(0.25, 0.78) - ind * 26
        col = "#294b77" if k % ink_every == 0 else "#acc6e7" if k % 2 else "#cbdbf4"
        out.append(f'<div class="abs" id="{prefix}{k}" style="{box(x + ind * 26, y + k * gap, max(30, lw), h)}border-radius:{h / 2}px;background:{col}"></div>')
        if R.f() < 0.35:
            out.append(f'<div class="abs" style="{box(x + ind * 26 + max(30, lw) + 10, y + k * gap, w * 0.12, h)}border-radius:{h / 2}px;background:#9fd8c4;opacity:.8"></div>')
    return "".join(out)


def engrave(id_, text, x, y, size=26, w=None, align="center", weight=800, ls=0.04):
    ww = f"width:{w}px;" if w else ""
    return (f'<div class="abs" id="{id_}" style="left:{r3(x)}px;top:{r3(y)}px;{ww}text-align:{align};white-space:nowrap;'
            f'font:{weight} {size}px Montserrat;letter-spacing:{ls}em;color:#8fa9cf;'
            f'text-shadow:0 1.5px 0 rgba(255,255,255,.95),0 -1px 0 rgba(28,51,84,.28)">{text}</div>')


def roller(id_, x, y, w, h, vertical=False):
    """cylinder roller with ridges; animate its backgroundPosition to spin it."""
    if vertical:
        bg = ("background-image:repeating-linear-gradient(180deg,rgba(41,75,119,.22) 0 3px,rgba(255,255,255,0) 3px 14px),"
              "linear-gradient(90deg,#c9d8ee 0%,#ffffff 30%,#e6edf8 60%,#9fb6d6 100%);")
    else:
        bg = ("background-image:repeating-linear-gradient(90deg,rgba(41,75,119,.22) 0 3px,rgba(255,255,255,0) 3px 14px),"
              "linear-gradient(180deg,#c9d8ee 0%,#ffffff 30%,#e6edf8 60%,#9fb6d6 100%);")
    return f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}border-radius:{min(w, h) / 2}px;{bg}box-shadow:0 6px 10px -4px rgba(28,51,84,.35)"></div>'


def spin_roller(S, sel, a, b, px_per_s=180, vertical=False):
    d = (b - a) * px_per_s
    if vertical:
        S.ft(sel, {"backgroundPosition": "0px 0px, 0px 0px"}, {"backgroundPosition": f"0px {r3(d)}px, 0px 0px"}, a, b - a, "none")
    else:
        S.ft(sel, {"backgroundPosition": "0px 0px, 0px 0px"}, {"backgroundPosition": f"{r3(d)}px 0px, 0px 0px"}, a, b - a, "none")


def bezier(p0, p1, p2, p3, u):
    a = (1 - u) ** 3; b = 3 * (1 - u) ** 2 * u; c = 3 * (1 - u) * u * u; d = u ** 3
    return (a * p0[0] + b * p1[0] + c * p2[0] + d * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + d * p3[1])


def ease_io(u, p=2.2):  # power-in-out
    return 0.5 * (2 * u) ** p if u < 0.5 else 1 - 0.5 * (2 * (1 - u)) ** p


def along(S, sel, pts, a, b, n=14, rot=False, p=2.4):
    """move an element (positioned with its centre at pts[0]) along a cubic bezier with an in-out ease (piecewise)."""
    prev = None
    for k in range(n + 1):
        u = ease_io(k / n, p)
        x, y = bezier(*pts, u)
        dx, dy = x - pts[0][0], y - pts[0][1]
        cur = {"x": r3(dx), "y": r3(dy)}
        if rot:
            x2, y2 = bezier(*pts, min(1, u + 0.01))
            cur["rotation"] = r3(math.degrees(math.atan2(y2 - y, x2 - x)) * 0.35)
        if prev is None:
            S.init(sel, cur)
        else:
            t0 = a + (b - a) * (k - 1) / n
            S.ft(sel, prev, cur, t0, (b - a) / n, "none")
        prev = cur


def bezier_d(pts):
    (a, b, c, d) = pts
    return f"M{r3(a[0])},{r3(a[1])} C{r3(b[0])},{r3(b[1])} {r3(c[0])},{r3(c[1])} {r3(d[0])},{r3(d[1])}"


def film_frame(id_, x, y, w, h, variant=0):
    """a little porcelain film frame with sprocket holes and an abstract picture."""
    holes = "".join(f'<div class="abs" style="{box(6, 8 + k * (h - 16) / 4, 8, 8)}border-radius:2px;background:#cbdbf4"></div>'
                    f'<div class="abs" style="{box(w - 14, 8 + k * (h - 16) / 4, 8, 8)}border-radius:2px;background:#cbdbf4"></div>' for k in range(5))
    pic = ['linear-gradient(150deg,#3a6299,#1c3354)', 'linear-gradient(160deg,#ffffff,#cbdbf4)', 'linear-gradient(150deg,#9fd8c4,#6fbfa5)'][variant % 3]
    dot = '#9fd8c4' if variant % 3 == 0 else '#294b77'
    return (f'<div class="abs por" id="{id_}" style="{box(x, y, w, h)}border-radius:8px">{holes}'
            f'<div class="abs" style="{box(20, 10, w - 40, h - 20)}border-radius:5px;background:{pic}"></div>'
            f'<div class="abs" style="{box(w - 46, 18, 16, 16)}border-radius:50%;background:{dot}"></div>'
            f'<div class="abs" style="{box(28, h - 26, (w - 56) * 0.6, 6)}border-radius:3px;background:rgba(255,255,255,.75)"></div></div>')
