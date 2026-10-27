"""Private builders for S04 (backdrop word) and S05 (glass widgets).

The giant word is matte navy dimensional signage: each letter is an SVG stroke glyph (custom condensed block letters),
extruded by stacking darker copies offset down-right (key light upper-left), with a floor contact shadow.
Layout (pulled-out, identity): letters 480 tall standing on a floor line at y 950."""
from xk import box, r3

LH = 480                      # letter height
LY = 470                      # letter top (floor line = LY + LH = 950)
T = 64                        # stroke thickness
LETTERS = [("C", 15, 240), ("L", 265, 130), ("A", 405, 172), ("U", 587, 160), ("D", 757, 168), ("E", 935, 130)]
EXTRUDE = 14                  # stacked side layers
STEP = 1.7                    # px per layer (down-right)
# parting on "terbuka": C slides left, L slides right -> gap 195..335 (140 x 480), centre (265, 710)
C_OPEN, L_OPEN = -60, 70
GAP_C = (265, 710)


def glyph_path(ch, w):
    h = LH
    x0, x1, y0, y1 = T / 2, w - T / 2, T / 2, h - T / 2
    R = (x1 - x0) / 2
    if ch == "C":
        return f"M{r3(x1)},{r3(y0)} H{r3(x0 + R)} A{r3(R)},{r3(R)} 0 0 0 {r3(x0)},{r3(y0 + R)} V{r3(y1 - R)} A{r3(R)},{r3(R)} 0 0 0 {r3(x0 + R)},{r3(y1)} H{r3(x1)}"
    if ch == "L":
        return f"M{r3(x0)},0 V{r3(y1)} H{r3(w)}"
    if ch == "A":
        return f"M{r3(x0)},{h} V{r3(y0 + R)} A{r3(R)},{r3(R)} 0 0 1 {r3(x1)},{r3(y0 + R)} V{h} M{r3(x0)},{r3(h * 0.6)} H{r3(x1)}"
    if ch == "U":
        return f"M{r3(x0)},0 V{r3(y1 - R)} A{r3(R)},{r3(R)} 0 0 0 {r3(x1)},{r3(y1 - R)} V0"
    if ch == "D":
        r = R * 0.9
        return f"M{r3(x0)},{r3(y0)} H{r3(x1 - r)} A{r3(r)},{r3(r)} 0 0 1 {r3(x1)},{r3(y0 + r)} V{r3(y1 - r)} A{r3(r)},{r3(r)} 0 0 1 {r3(x1 - r)},{r3(y1)} H{r3(x0)} Z"
    if ch == "E":
        return f"M{r3(w)},{r3(y0)} H{r3(x0)} V{r3(y1)} H{r3(w)} M{r3(x0)},{r3(h / 2)} H{r3(w - 18)}"
    raise ValueError(ch)


def letter(pid, ch, x, w):
    """one extruded letter (local origin = its box top-left). id = pid."""
    d = glyph_path(ch, w)
    gid = f"{pid}-g"
    layers = []
    for k in range(EXTRUDE, 0, -1):
        c = "#0A0D2C" if k > EXTRUDE * 0.45 else "#13234a"
        layers.append(f'<path d="{d}" transform="translate({r3(k * STEP)},{r3(k * STEP)})" fill="none" stroke="{c}" stroke-width="{T}" stroke-linejoin="miter"/>')
    face = (f'<path d="{d}" fill="none" stroke="url(#{gid})" stroke-width="{T}" stroke-linejoin="miter"/>'
            f'<path d="{d}" transform="translate(-1.5,-1.5)" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="3" stroke-linejoin="miter"/>')
    pad = 40
    svg = (f'<svg class="abs" style="left:{-pad}px;top:{-pad}px;width:{w + 2 * pad}px;height:{LH + 2 * pad}px;overflow:visible" '
           f'viewBox="{-pad} {-pad} {w + 2 * pad} {LH + 2 * pad}">'
           f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a6299"/>'
           f'<stop offset=".45" stop-color="#1f3b68"/><stop offset="1" stop-color="#0f1f44"/></linearGradient></defs>'
           + "".join(layers) + face + "</svg>")
    # floor: contact shadow + a soft forward-right cast silhouette
    cast = (f'<svg class="abs" style="left:0;top:{LH}px;width:{w}px;height:{LH}px;overflow:visible;transform-origin:50% 0%;'
            f'transform:skewX(-38deg) scaleY(.22);filter:blur(7px);opacity:.28" viewBox="0 0 {w} {LH}">'
            f'<path d="{d}" transform="translate(0,{LH}) scale(1,-1)" fill="none" stroke="#0A0D2C" stroke-width="{T}"/></svg>')
    contact = f'<div class="abs cshadow" style="{box(-30, LH - 26, w + 80, 56)}opacity:.75"></div>'
    return f'<div class="abs" id="{pid}" style="{box(x, LY, w, LH)}">{contact}{cast}{svg}</div>'


def floor(pid):
    """pale stage floor in front of the letters (keeps the user's plate visible above it)."""
    return (f'<div class="abs" id="{pid}" style="{box(-60, LY + LH - 2, 1200, 1920 - LY - LH + 2)}'
            f'background:linear-gradient(180deg,rgba(255,255,255,.55) 0%,rgba(226,235,248,.35) 40%,rgba(205,220,243,.18) 100%)">'
            f'<div class="abs" style="left:0;top:0;width:1200px;height:2px;background:rgba(41,75,119,.18)"></div></div>')


def gap_glass(pid):
    """the translucent glass pane that sits behind the letters and shows through the C|L gap (group coords)."""
    gx0, gx1 = 195 - 26, 335 + 26
    return (f'<div class="abs" id="{pid}" style="{box(gx0, LY - 30, gx1 - gx0, LH + 60)}">'
            f'<div class="abs glass" style="left:0;top:0;width:{gx1 - gx0}px;height:{LH + 60}px;border-radius:18px"></div>'
            f'<div class="abs" id="{pid}-band" style="left:0;top:0;width:{gx1 - gx0}px;height:120px;'
            f'background:linear-gradient(180deg,rgba(255,255,255,0),rgba(255,255,255,.75),rgba(255,255,255,0))"></div></div>')


def rims(pid):
    """bright glass rims along the C's right edge and the L's left edge once parted (group coords)."""
    return (f'<div class="abs glint" id="{pid}-r0" style="{box(193, LY + 6, 5, LH - 12)}border-radius:3px"></div>'
            f'<div class="abs glint" id="{pid}-r1" style="{box(333, LY + 6, 5, LH - 12)}border-radius:3px"></div>')
