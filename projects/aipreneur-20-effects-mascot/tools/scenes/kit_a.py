"""Private helpers for S00-S03 (plain clip panel, orbit ring, icon chips)."""
import math
from xk import box, r3, CYAN
from kit import PANEL, ORBIT

PX, PY, PW, PH, PR = PANEL
OX, OY, OD, OSY, OROT = ORBIT
# the panel border morphs into the orbit ring: scale + offset that maps the PANEL box onto the ring ellipse
RING_FROM_PANEL = {"scaleX": r3(OD / PW), "scaleY": r3(OD * OSY / PH), "x": r3(OX - (PX + PW / 2)), "y": r3(OY - (PY + PH / 2)), "rotation": OROT}
CORNERS = ("borderTopLeftRadius", "borderTopRightRadius", "borderBottomLeftRadius", "borderBottomRightRadius")


def radii(rx, ry):
    return {c: f"{r3(rx)}px {r3(ry)}px" for c in CORNERS}


def panel_bg(id_):
    """flat, effect-free source plate (back layer): lighter navy cyc + soft floor."""
    return (f'<div class="abs" id="{id_}" style="{box(PX, PY, PW, PH)}border-radius:{PR}px;overflow:hidden;'
            f'background:linear-gradient(180deg,#27507f 0%,#1d406e 55%,#16335c 100%);box-shadow:0 40px 80px -30px rgba(3,8,28,.9)">'
            f'<div class="abs" style="left:0;top:{PH * 0.66}px;width:{PW}px;height:{PH * 0.34}px;background:linear-gradient(180deg,rgba(10,24,52,0),rgba(10,24,52,.55))"></div>'
            f'<div class="abs" style="left:{PW * 0.15}px;top:{PH * 0.08}px;width:{PW * 0.7}px;height:{PH * 0.6}px;border-radius:50%;background:radial-gradient(circle,rgba(150,190,240,.18),rgba(150,190,240,0) 70%)"></div></div>')


def panel_border(id_):
    """thin white frame line + label (front layer)."""
    return (f'<div class="abs" id="{id_}" style="{box(PX, PY, PW, PH)}border-radius:{PR}px;border:5px solid rgba(255,255,255,.82);'
            f'box-shadow:0 0 0 1px rgba(0,208,254,.25), inset 0 0 0 1px rgba(0,208,254,.18)"></div>')


def panel_label(id_):
    return (f'<div class="abs" id="{id_}" style="{box(PX + 34, PY + 30, 300, 34)}font:700 22px/34px Poppins, sans-serif;color:#fff;letter-spacing:.16em">'
            f'<span style="display:inline-block;width:12px;height:12px;border-radius:6px;background:{CYAN};margin-right:10px;vertical-align:1px"></span>KLIP POLOS</div>')


def ring(id_, half=None):
    """orbit ring: circle Ø OD scaled to an ellipse. half='front' keeps only the near (lower) half."""
    clip = "clip-path:inset(50% -20px -20px -20px);" if half == "front" else ""
    return (f'<div class="abs" id="{id_}" style="{box(OX - OD / 2, OY - OD / 2, OD, OD)}transform:rotate({OROT}deg) scaleY({OSY});{clip}">'
            f'<div class="abs" style="left:0;top:0;width:{OD}px;height:{OD}px;border-radius:50%;border:5px solid rgba(255,255,255,.85);'
            f'box-shadow:0 0 16px rgba(0,208,254,.55), inset 0 0 12px rgba(0,208,254,.35)"></div></div>')


def orbit_xy(theta):
    """screen position on the tilted orbit ellipse; sin(theta) > 0 = near half (in front of the head)."""
    ex, ey = OD / 2 * math.cos(theta), OD / 2 * OSY * math.sin(theta)
    a = math.radians(OROT)
    return OX + ex * math.cos(a) - ey * math.sin(a), OY + ex * math.sin(a) + ey * math.cos(a)


ICONS = {
    "wave": '<svg viewBox="0 0 40 40" style="position:absolute;left:18%;top:18%;width:64%;height:64%">' + "".join(
        f'<rect x="{4 + k * 7}" y="{20 - h / 2}" width="4" height="{h}" rx="2" fill="{CYAN}"/>' for k, h in enumerate((10, 22, 30, 16, 24))) + "</svg>",
    "aa": f'<div class="abs" style="left:0;top:0;width:100%;height:100%;font:700 34px/84px Poppins, sans-serif;text-align:center;color:#fff">A<span style="color:{CYAN}">a</span></div>',
    "img": '<svg viewBox="0 0 40 40" style="position:absolute;left:20%;top:20%;width:60%;height:60%"><rect x="3" y="6" width="34" height="28" rx="5" fill="none" stroke="#fff" stroke-width="3"/>'
           f'<path d="M7 30 L16 19 L23 26 L27 22 L33 30 Z" fill="{CYAN}"/><circle cx="28" cy="13" r="3.5" fill="#fff"/></svg>',
    "cur": f'<svg viewBox="0 0 40 40" style="position:absolute;left:22%;top:18%;width:60%;height:66%"><path d="M8 4 L8 32 L15 25 L20 36 L25 34 L20 23 L30 23 Z" fill="#fff" stroke="{CYAN}" stroke-width="2" stroke-linejoin="round"/></svg>',
}


def chip(id_, x, y, d, icon, extra=""):
    return (f'<div class="abs smoked" id="{id_}" style="{box(x - d / 2, y - d / 2, d, d)}border-radius:50%;'
            f'border:2px solid rgba(120,232,255,.75);box-shadow:inset 0 1px 0 rgba(255,255,255,.4), 0 0 18px rgba(0,208,254,.3), 0 18px 30px -12px rgba(3,8,28,.85);{extra}">{ICONS[icon]}</div>')
