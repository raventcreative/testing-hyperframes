"""Extra builders for scenes s13–s15 (template family, credit meter / local render, balance scale)."""
import math
from xk import box, r3, screw


def bottle(id_, x, y, w=110, h=220):
    """generic product bottle (no text): navy cap, porcelain body, navy label band with a mint stripe, gloss band."""
    cw, ch = w * 0.42, h * 0.16
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}">'
            f'<div class="abs" style="{box((w - cw) / 2, 0, cw, ch)}border-radius:8px 8px 4px 4px;background:linear-gradient(90deg,#3a6299,#1c3354)"></div>'
            f'<div class="abs" style="{box((w - cw * 0.8) / 2, ch - 2, cw * 0.8, h * 0.07)}background:linear-gradient(90deg,#e6edf8,#ffffff 40%,#c9d8ee)"></div>'
            f'<div class="abs" style="{box(0, ch + h * 0.06, w, h - ch - h * 0.06)}border-radius:{r3(w * 0.28)}px {r3(w * 0.28)}px {r3(w * 0.16)}px {r3(w * 0.16)}px;'
            f'background:linear-gradient(90deg,#dbe6f6 0%,#ffffff 28%,#f4f7fc 55%,#c3d5ee 100%);box-shadow:inset -3px -3px 0 rgba(172,198,231,.6);overflow:hidden">'
            f'<div class="abs" style="{box(0, (h - ch) * 0.38, w, (h - ch) * 0.3)}background:linear-gradient(90deg,#294b77,#3a6299 35%,#1c3354)"></div>'
            f'<div class="abs" style="{box(w * 0.18, (h - ch) * 0.47, w * 0.64, 6)}border-radius:3px;background:#9fd8c4"></div>'
            f'<div class="abs" style="{box(w * 0.18, (h - ch) * 0.56, w * 0.4, 5)}border-radius:3px;background:rgba(203,219,244,.8)"></div>'
            f'<div class="abs" id="{id_}-gl" style="{box(-w * 0.5, 0, w * 0.22, h)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.85),rgba(255,255,255,0))"></div>'
            f'</div></div>')


def dial(id_, cx, cy, r, a0=-120, a1=120, ticks=17, arcs=(), face="por"):
    """round gauge: porcelain face, tick ring, optional coloured arcs [(from_deg, to_deg, colour)], needle id {id}-nd."""
    sz = 2 * r
    svg = [f'<svg width="{sz}" height="{sz}" viewBox="0 0 {sz} {sz}" style="position:absolute;left:0;top:0;overflow:visible">']
    for (b0, b1, col) in arcs:
        ra = r * 0.74
        p0 = (r + ra * math.sin(math.radians(b0)), r - ra * math.cos(math.radians(b0)))
        p1 = (r + ra * math.sin(math.radians(b1)), r - ra * math.cos(math.radians(b1)))
        large = 1 if (b1 - b0) > 180 else 0
        svg.append(f'<path d="M{r3(p0[0])},{r3(p0[1])} A{r3(ra)},{r3(ra)} 0 {large} 1 {r3(p1[0])},{r3(p1[1])}" fill="none" stroke="{col}" stroke-width="{r3(r * 0.09)}" stroke-linecap="round"/>')
    for k in range(ticks):
        a = math.radians(a0 + (a1 - a0) * k / (ticks - 1))
        big = k % 4 == 0
        r_in, r_out = r * (0.6 if big else 0.66), r * 0.72
        svg.append(f'<line x1="{r3(r + r_in * math.sin(a))}" y1="{r3(r - r_in * math.cos(a))}" x2="{r3(r + r_out * math.sin(a))}" y2="{r3(r - r_out * math.cos(a))}" '
                   f'stroke="{"#294b77" if big else "#9fb6d6"}" stroke-width="{2.6 if big else 1.6}" stroke-linecap="round"/>')
    svg.append("</svg>")
    nl = r * 0.62
    return (f'<div class="abs" id="{id_}" style="{box(cx - r, cy - r, sz, sz)}">'
            f'<div class="abs {face}" style="{box(0, 0, sz, sz)}border-radius:50%"></div>'
            f'<div class="abs" style="{box(r * 0.1, r * 0.1, sz - r * 0.2, sz - r * 0.2)}border-radius:50%;border:1.5px solid rgba(172,198,231,.8)"></div>'
            + "".join(svg) +
            f'<div class="abs" id="{id_}-nd" style="{box(r - 3, r - nl, 6, nl)}border-radius:3px;background:linear-gradient(180deg,#294b77,#1c3354)"></div>'
            f'<div class="abs" style="{box(r - r * 0.12, r - r * 0.12, r * 0.24, r * 0.24)}border-radius:50%;background:#1c3354;box-shadow:0 1px 2px rgba(28,51,84,.5)"></div>'
            f'</div>')


def frame_card(id_, x, y, w=96, h=150, variant=0, extra_style=""):
    """a finished little Reel frame (output of the render machine)."""
    inner = (f'<div class="abs" style="{box(w * 0.1, h * 0.1, w * 0.8, h * 0.08)}border-radius:3px;background:#294b77"></div>'
             f'<div class="abs" style="{box(w * 0.1, h * 0.26, w * 0.8, h * 0.4)}border-radius:6px;background:linear-gradient(150deg,{"#3a6299,#1c3354" if variant % 2 == 0 else "#cbdbf4,#acc6e7"})"></div>'
             f'<div class="abs" style="{box(w * 0.58, h * 0.3, w * 0.18, w * 0.18)}border-radius:50%;background:#9fd8c4"></div>'
             f'<div class="abs" style="{box(w * 0.1, h * 0.74, w * 0.7, h * 0.05)}border-radius:3px;background:#cbdbf4"></div>'
             f'<div class="abs" style="{box(w * 0.1, h * 0.83, w * 0.45, h * 0.05)}border-radius:3px;background:#294b77"></div>')
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}border-radius:10px;background:linear-gradient(160deg,#ffffff,#eef3fa);'
            f'box-shadow:inset 0 0 0 1.5px rgba(41,75,119,.35),0 6px 10px -4px rgba(28,51,84,.35);{extra_style}">{inner}</div>')


def chain(x, y, n, step=13):
    """vertical chain of porcelain links (thin ovals) starting at (x, y) going down."""
    out = []
    for k in range(n):
        horiz = k % 2 == 1
        w, h = (8, 14) if not horiz else (4, 14)
        out.append(f'<div class="abs" style="{box(x - w / 2, y + k * step, w, h)}border-radius:4px;border:2px solid {"#9fb6d6" if horiz else "#c3d5ee"};background:transparent"></div>')
    return "".join(out)


def vent_lines(x, y, w, n, gap=10, col="rgba(41,75,119,.35)"):
    return "".join(f'<div class="abs" style="{box(x, y + k * gap, w, 3)}border-radius:2px;background:{col}"></div>' for k in range(n))
