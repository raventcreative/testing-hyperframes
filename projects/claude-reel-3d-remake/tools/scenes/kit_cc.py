"""Shared builders for the Claude Code 3D remake scenes (dark navy / cyan kit, vendor/fx.css).
Everything is deterministic: positions are fixed, every reveal is keyed to a measured VO word."""
import re
from xk import el, box, r3, Rng

CY = "#00D0FE"
HEAD_Y = 250           # hero heading band (logo sits at y 108-138)
MASCOT_R = {"fx": 830, "fy": 1880, "h": 860, "yaw": 0, "pitch": 4}      # narrator bottom-right
MASCOT_L = {"fx": 250, "fy": 1880, "h": 860, "yaw": 0, "pitch": 4}
MASCOT_C = {"fx": 540, "fy": 2000, "h": 1200, "yaw": 0, "pitch": 4}
OFF = {"fx": -900, "fy": 3200, "h": 900, "yaw": 0, "pitch": 4, "vis": 0}


def heading(S, layer, hid, markup, x, y, w, size=64, align="left", at=None, step=0.06, keys=None, plate=True, pad=(26, 34)):
    """markup: words; *word* = cyan keyword. Each word rises out of a mask at `at` + i*step, or at keys[i] if given
    (keys = list of global times, one per word). Cyan words get an underline sweep 0.12 s after they land."""
    words = markup.split()
    parts, cy_ids = [], []
    for i, wd in enumerate(words):
        cyan = wd.startswith("*") and wd.endswith("*")
        t = wd.strip("*")
        wid = f"{hid}-w{i}"
        ul = f'<span class="ul" id="{wid}-ul"></span>' if cyan else ""
        cls = "wd cy" if cyan else "wd"
        parts.append(f'<span class="m"><span class="{cls}" id="{wid}" style="position:relative">{t}{ul}</span></span>')
        if cyan:
            cy_ids.append(i)
    inner = " ".join(parts)
    py, px = pad
    pl = "plate" if plate else ""
    layer.append(f'<div id="{hid}" class="abs {pl}" style="left:{r3(x)}px;top:{r3(y)}px;width:{r3(w)}px;padding:{py}px {px}px {py + 4}px;'
                 f'text-align:{align};font:700 {size}px/1.1 Poppins, sans-serif;color:#fff">{inner}</div>')
    base = S.t0 + 0.12 if at is None else at
    S.init(f"#{hid}", {"opacity": 0, "y": 18})
    S.ft(f"#{hid}", {"opacity": 0, "y": 18}, {"opacity": 1, "y": 0}, base - 0.08, 0.36, "power3.out")
    for i in range(len(words)):
        t = keys[i] if keys and i < len(keys) else base + i * step
        S.init(f"#{hid}-w{i}", {"yPercent": 108})
        S.ft(f"#{hid}-w{i}", {"yPercent": 108}, {"yPercent": 0}, t - 0.05, 0.32, "power4.out")
    for i in cy_ids:
        t = (keys[i] if keys and i < len(keys) else base + i * step) + 0.12
        S.init(f"#{hid}-w{i}-ul", {"scaleX": 0})
        S.ft(f"#{hid}-w{i}-ul", {"scaleX": 0}, {"scaleX": 1}, t, 0.28, "power3.out")
        S.ft(f"#{hid}-w{i}", {"textShadow": "0 0 0px rgba(0,208,254,0)"}, {"textShadow": "0 0 14px rgba(0,208,254,.35)"}, t, 0.12, "power2.out")
        S.ft(f"#{hid}-w{i}", {"textShadow": "0 0 14px rgba(0,208,254,.35)"}, {"textShadow": "0 0 0px rgba(0,208,254,0)"}, t + 0.45, 0.5, "power2.inOut")


def step_badge(S, layer, bid, n, x, y, at, size=96):
    layer.append(f'<div id="{bid}" class="abs num" style="{box(x, y, size, size)}font-size:{int(size * 0.46)}px">{n:02d}</div>')
    S.init(f"#{bid}", {"opacity": 0, "scale": 0.6, "rotationY": -70})
    S.ft(f"#{bid}", {"opacity": 0, "scale": 0.6, "rotationY": -70}, {"opacity": 1, "scale": 1, "rotationY": 0}, at - 0.12, 0.42, "back.out(1.6)")


def cursor(layer, cid, x, y, w=64):
    """user's click cursor asset; hotspot (tip) at (x, y)"""
    h = w * 403 / 397
    layer.append(f'<img id="{cid}" class="abs" src="assets/brand/cursor_trim.png" style="left:{r3(x - w * 0.40)}px;top:{r3(y - h * 0.02)}px;width:{r3(w)}px;height:{r3(h)}px;'
                 f'filter:drop-shadow(0 6px 8px rgba(0,0,0,.5))">')


def click(S, layer, cid, x, y, at, sfx=True):
    """cursor press + one cyan ring at (x, y) (cursor element must already exist as cid)"""
    layer.append(f'<div id="{cid}-rg" class="abs ringfx" style="{box(x - 40, y - 40, 80, 80)}"></div>')
    S.init(f"#{cid}-rg", {"opacity": 0, "scale": 0.3})
    S.ft(f"#{cid}", {"scale": 1}, {"scale": 0.86}, at - 0.08, 0.08, "power2.in")
    S.ft(f"#{cid}", {"scale": 0.86}, {"scale": 1}, at, 0.16, "back.out(2)")
    S.ft(f"#{cid}-rg", {"opacity": 0.95, "scale": 0.3}, {"opacity": 0, "scale": 1.9}, at, 0.45, "power3.out")
    if sfx:
        S.fx(at, "click", 0.08)


def move(S, sel, frm, to, at, dur=0.5, ease="power2.inOut"):
    S.ft(sel, frm, to, at, dur, ease)


def appwin(wid, x, y, w, h, title="Claude", inner="", radius=26):
    """dark app window: traffic lights + title, body slot"""
    return (f'<div id="{wid}" class="abs glassd" style="{box(x, y, w, h)}border-radius:{radius}px;overflow:hidden;background:linear-gradient(170deg,#141b33,#0b1023)">'
            f'<div class="abs" style="left:0;top:0;width:{r3(w)}px;height:58px;background:rgba(255,255,255,.05);border-bottom:1px solid rgba(255,255,255,.08)"></div>'
            + "".join(f'<div class="abs" style="left:{24 + k * 26}px;top:21px;width:16px;height:16px;border-radius:50%;background:{c}"></div>' for k, c in enumerate(["#ff6a5f", "#ffbe3d", "#27c840"]))
            + f'<div class="abs sub" style="left:0;top:12px;width:{r3(w)}px;text-align:center;font-size:24px;color:rgba(255,255,255,.7)">{title}</div>'
            + f'<div class="abs" style="left:0;top:58px;width:{r3(w)}px;height:{r3(h - 58)}px">{inner}</div></div>')


def laptop(lid, x, y, w, screen_inner="", lid_open=True):
    """front-3/4 laptop: base slab + hinged lid (lid id = lid-lid, rotateX 0 = open)"""
    sh = w * 0.62
    return (f'<div id="{lid}" class="abs p3" style="{box(x, y, w, sh + 40)}">'
            f'<div class="abs cshadow" style="{box(-w * 0.08, sh + 6, w * 1.16, 70)}"></div>'
            f'<div class="abs alu" style="{box(-w * 0.06, sh, w * 1.12, 26)}border-radius:6px 6px 18px 18px"></div>'
            f'<div id="{lid}-lid" class="abs p3" style="{box(0, 0, w, sh)}transform-origin:50% 100%">'
            f'<div class="abs alu" style="left:0;top:0;width:{r3(w)}px;height:{r3(sh)}px;border-radius:22px"></div>'
            f'<div class="abs scr" style="left:14px;top:14px;width:{r3(w - 28)}px;height:{r3(sh - 28)}px;border-radius:12px;overflow:hidden">{screen_inner}</div>'
            f'</div></div>')


def folder3d(fid, x, y, w, h, label="", tab_w=None):
    """3D project folder: back panel + tab, front flap (fid-front, hinged at the bottom)"""
    tab_w = tab_w or w * 0.38
    return (f'<div id="{fid}" class="abs p3" style="{box(x, y, w, h)}">'
            f'<div class="abs cshadow" style="{box(-w * 0.06, h - 30, w * 1.12, 80)}"></div>'
            f'<div id="{fid}-tab" class="abs metal" style="{box(0, -38, tab_w, 60)}border-radius:16px 22px 0 0"></div>'
            f'<div id="{fid}-back" class="abs metal" style="{box(0, 0, w, h)}border-radius:6px 18px 18px 18px;filter:brightness(.82)"></div>'
            f'<div id="{fid}-in" class="abs" style="{box(w * 0.06, h * 0.06, w * 0.88, h * 0.8)}"></div>'
            f'<div id="{fid}-front" class="abs metal" style="{box(0, h * 0.18, w, h * 0.82)}border-radius:14px;transform-origin:50% 100%;'
            f'border-top:1.5px solid rgba(0,208,254,.45)">'
            + (f'<div class="abs" style="left:0;top:{r3(h * 0.82 / 2 - 34)}px;width:{r3(w)}px;text-align:center;font:700 44px/1 Poppins;color:#fff;letter-spacing:.02em" id="{fid}-lab">{label}</div>' if label else "")
            + '</div></div>')


def phone(pid, x, y, w, inner=""):
    h = w * 2.05
    return (f'<div id="{pid}" class="abs p3" style="{box(x, y, w, h)}">'
            f'<div class="abs cshadow" style="{box(-w * 0.1, h - 30, w * 1.2, 80)}"></div>'
            f'<div class="abs alu" style="left:0;top:0;width:{r3(w)}px;height:{r3(h)}px;border-radius:{r3(w * 0.16)}px"></div>'
            f'<div class="abs scr" style="left:10px;top:10px;width:{r3(w - 20)}px;height:{r3(h - 20)}px;border-radius:{r3(w * 0.13)}px;overflow:hidden">{inner}</div>'
            f'<div class="abs" style="left:{r3(w / 2 - 40)}px;top:22px;width:80px;height:22px;border-radius:12px;background:#05070f"></div></div>')


def checkrow(rid, x, y, w, label, h=84):
    return (f'<div id="{rid}" class="abs plate plate-s" style="{box(x, y, w, h)}">'
            f'<div id="{rid}-led" class="abs led" style="left:26px;top:{r3(h / 2 - 15)}px;width:30px;height:30px"></div>'
            f'<div class="abs sub" style="left:78px;top:{r3(h / 2 - 22)}px;width:{r3(w - 220)}px;font-size:36px;color:#fff">{label}</div>'
            f'<div id="{rid}-st" class="abs sub" style="left:{r3(w - 170)}px;top:{r3(h / 2 - 18)}px;width:140px;text-align:right;font-size:28px;color:#00D0FE;opacity:0">OK</div></div>')


def led_on(S, rid, at, text="OK"):
    S.ft(f"#{rid}-led", {"backgroundColor": "#3b4a66", "boxShadow": "0 0 0px rgba(0,208,254,0)"},
         {"backgroundColor": CY, "boxShadow": "0 0 14px rgba(0,208,254,.6)"}, at, 0.2, "power2.out")
    S.ft(f"#{rid}-st", {"opacity": 0, "x": 12}, {"opacity": 1, "x": 0}, at + 0.05, 0.25, "power2.out")
    S.fx(at, "ping", 0.05)


def pop(S, sel, at, dur=0.42, frm=None, to=None, ease="back.out(1.5)"):
    frm = frm or {"opacity": 0, "scale": 0.85, "y": 24}
    to = to or {"opacity": 1, "scale": 1, "y": 0}
    S.init(sel, frm)
    S.ft(sel, frm, to, at, dur, ease)


def out(S, sel, at, dur=0.25, to=None, frm=None):
    frm = frm or {"opacity": 1}
    to = to or {"opacity": 0}
    S.ft(sel, frm, to, at, dur, "power2.in")
