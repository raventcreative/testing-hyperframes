"""Private helpers for S02 (editorial split) and S03 (over the shoulder)."""
from xk import box, r3
from kit import CHART, MONITOR

# bar layout inside the CHART card (local px)
BAR_W, BAR_GAP, BAR_X0, BASE_Y = 64, 22, 33, 800
BAR_H = [250, 390, 540, 330, 610, 450]          # abstract heights (no data, no numbers)
DEPTH = 16
HERO = 2                                         # bar #03 = the portal


def bar_x(k):
    return BAR_X0 + k * (BAR_W + BAR_GAP)


def bar3d(id_, x, base_y, w, h, hero=False, d=DEPTH):
    """extruded bar: front + top + right side faces inside a mask that sits on the baseline.
    Animate #{id}-in with y from h+d -> 0 (it rises out of the baseline, top face intact)."""
    front = ("linear-gradient(180deg,#22416d 0%,#0A0D2C 100%)" if hero else
             "linear-gradient(180deg,#5a7fb0 0%,#3a6296 45%,#294B77 100%)")
    top = "#8fb0dc" if not hero else "#4d71a4"
    side = "#1d3a63" if not hero else "#060820"
    inner = (f'<div class="abs" style="left:0;top:{d}px;width:{w}px;height:{h}px;background:{front};'
             f'box-shadow:inset 1px 0 0 rgba(255,255,255,.35)"></div>'
             f'<div class="abs" style="left:0;top:0;width:{w + d}px;height:{d}px;background:{top};'
             f'clip-path:polygon(0 100%,{w}px 100%,100% 0,{d}px 0)"></div>'
             f'<div class="abs" style="left:{w}px;top:0;width:{d}px;height:{h + d}px;background:{side};'
             f'clip-path:polygon(0 {d}px,100% 0,100% {h}px,0 100%)"></div>')
    return (f'<div class="abs" style="{box(x, base_y - h - d, w + d, h + d)}overflow:hidden">'
            f'<div class="abs" id="{id_}-in" style="left:0;top:0;width:{w + d}px;height:{h + d}px">{inner}</div></div>')


def mini_chart(w, h):
    """original editorial artwork for the monitor screen: title lines + six small bars + baseline (no numbers)."""
    sx = w / 560
    bars = ""
    for k, bh in enumerate(BAR_H):
        x = (BAR_X0 + k * (BAR_W + BAR_GAP)) * sx
        hh = bh * 0.42 * sx
        col = "#0A0D2C" if k == HERO else "#3a6296"
        bars += f'<div class="abs" style="{box(x, h - 46 - hh, BAR_W * sx, hh)}background:{col};border-radius:2px"></div>'
    return (f'<div class="abs grid-fine" style="{box(0, 0, w, h)}background-color:#fbfdff;background-size:28px 28px"></div>'
            f'<div class="abs" style="{box(28, 26, w * 0.42, 16)}border-radius:8px;background:linear-gradient(90deg,#0A0D2C,#294B77)"></div>'
            f'<div class="abs" style="{box(28, 52, w * 0.28, 10)}border-radius:5px;background:rgba(41,75,119,.35)"></div>'
            f'<div class="abs" style="{box(w * 0.62, 26, w * 0.3, 40)}border-radius:10px;background:linear-gradient(135deg,#0A0D2C,#294B77)"></div>'
            + bars +
            f'<div class="abs" style="{box(18, h - 46, w - 36, 3)}background:#0A0D2C"></div>')


def monitor(s, inner_id=None):
    """anodized monitor at MONITOR (bezel 22 px, screen = mini editorial artwork). ids {s}-mon, {s}-scr."""
    x, y, w, h = MONITOR
    bz = 22
    sid = inner_id or f"{s}-scr"
    return (f'<div class="abs anod" id="{s}-mon" style="{box(x, y, w, h)}border-radius:26px">'
            f'<div class="abs" id="{sid}" style="{box(bz, bz, w - 2 * bz, h - 2 * bz)}border-radius:10px;overflow:hidden;background:#0b1430">'
            + mini_chart(w - 2 * bz, h - 2 * bz) +
            f'<div class="abs" style="{box(0, 0, w - 2 * bz, h - 2 * bz)}background:linear-gradient(125deg,rgba(255,255,255,.35) 0%,rgba(255,255,255,0) 35%)"></div></div>'
            f'<div class="abs" style="{box(w / 2 - 5, 8, 10, 10)}border-radius:5px;background:#3a4558"></div></div>')


def c_stroke(id_, w, h, d=14):
    """matte navy extruded 'C' (first stroke of the giant word), w x h, with a stacked side wall (depth d)."""
    # C outline as an even-odd SVG path (outer ellipse arc minus inner arc, opening on the right)
    def path(ox, oy):
        r1x, r1y = w / 2, h / 2
        t = w * 0.30
        r2x, r2y = r1x - t, r1y - t * 0.9
        cx, cy = w / 2 + ox, h / 2 + oy
        a = 0.62   # half opening angle (rad) on the right
        import math
        p1 = (cx + r1x * math.cos(a), cy - r1y * math.sin(a))
        p2 = (cx + r1x * math.cos(a), cy + r1y * math.sin(a))
        q2 = (cx + r2x * math.cos(a), cy + r2y * math.sin(a))
        q1 = (cx + r2x * math.cos(a), cy - r2y * math.sin(a))
        f = lambda p: f"{r3(p[0])},{r3(p[1])}"
        return (f"M{f(p1)} A{r3(r1x)},{r3(r1y)} 0 1 0 {f(p2)} L{f(q2)} A{r3(r2x)},{r3(r2y)} 0 1 1 {f(q1)} Z")
    side = "".join(f'<path d="{path(k, k)}" fill="#0A0D2C"/>' for k in range(d, 0, -2))
    return (f'<svg id="{id_}" viewBox="0 0 {w + d} {h + d}" style="position:absolute;left:0;top:0;width:{w + d}px;height:{h + d}px;overflow:visible">'
            f'<defs><linearGradient id="{id_}-g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a5f92"/>'
            f'<stop offset=".5" stop-color="#1c3561"/><stop offset="1" stop-color="#101f42"/></linearGradient></defs>'
            f'{side}<path d="{path(0, 0)}" fill="url(#{id_}-g)"/>'
            f'<path d="{path(0, 0)}" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="2"/></svg>')
