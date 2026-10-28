"""Private helpers for s06-s09 (deep learning -> LLM -> AI application -> RAG)."""
from xk import box, r3
from kit import MAT

TRACK = (120, 1250, 960)          # S06 end / S07 start: the token track (aluminium rail, x0, y, x1)
OUT_Y = 790                       # S07 end (after its camera tilt): output rail runs off the right edge at this screen y / S08 start: enters from the left here
CAB_SPINE = (480, 640, 120, 760)  # S08 end / S09 start: the archive-cabinet spine (x y w h)


def node(id_, cx, cy, d=56):
    """a glass neuron: frosted sphere with a satin navy core."""
    return (f'<div class="abs" id="{id_}" style="{box(cx - d / 2, cy - d / 2, d, d)}border-radius:50%;'
            f'background:radial-gradient(circle at 36% 30%,#ffffff 0%,rgba(230,238,250,.9) 32%,rgba(170,195,230,.75) 70%,rgba(110,145,195,.8) 100%);'
            f'box-shadow:inset 0 2px 0 rgba(255,255,255,.95),0 10px 18px -8px rgba(10,13,44,.5),0 0 0 1.5px rgba(255,255,255,.9)">'
            f'<div class="abs" style="left:{d * .3}px;top:{d * .3}px;width:{d * .4}px;height:{d * .4}px;border-radius:50%;'
            f'background:linear-gradient(150deg,#4c79b8 0%,#1c3561 60%,#0A0D2C 100%)"></div></div>')


def plate(id_, x, y, w, h, r=40):
    """frosted glass layer plate."""
    return f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}border-radius:{r}px;{MAT["glass"]}"></div>'


def arrow(id_, x, y, w=90):
    return (f'<svg class="abs" id="{id_}" style="left:{r3(x)}px;top:{r3(y)}px;width:{w}px;height:40px;overflow:visible" viewBox="0 0 {w} 40">'
            f'<path id="{id_}p" d="M6 20 H{w - 10} M{w - 26} 6 L{w - 8} 20 L{w - 26} 34" fill="none" stroke="#294B77" stroke-width="6" '
            f'stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')


def pop_chip(S, sel, at, out, rot=0):
    """band chip: pop in on the word (back-out), leave as he steps back."""
    S.init(sel, {"opacity": 0, "y": 26, "scale": 0.8, "rotation": rot})
    S.ft(sel, {"opacity": 0, "y": 26, "scale": 0.8}, {"opacity": 1, "y": 0, "scale": 1}, at, 0.38, "back.out(2)")
    S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": -18}, out, 0.25, "power2.in")


def draw_arrow(S, id_, at, out):
    S.init(f"#{id_}p", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{id_}p", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, at, 0.35, "power2.inOut")
    S.init(f"#{id_}", {"opacity": 1})
    S.ft(f"#{id_}", {"opacity": 1}, {"opacity": 0}, out, 0.25, "power2.in")


def rail(id_, x0, y, x1, h=26):
    """aluminium rail with a dark groove."""
    return (f'<div class="abs" id="{id_}" style="{box(x0, y - h / 2, x1 - x0, h)}border-radius:{h / 2}px;{MAT["alu"]}">'
            f'<div class="abs" style="left:10px;right:10px;top:{h / 2 - 3}px;height:6px;border-radius:3px;background:#1c3561;opacity:.85"></div></div>')


ICON_B = {
    "nn": '<svg viewBox="0 0 24 24" width="100%" height="100%"><g fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 6 12 4M4 6 12 12M4 18 12 12M4 18 12 20M12 4 20 12M12 12 20 12M12 20 20 12"/></g><g fill="currentColor"><circle cx="4" cy="6" r="2.3"/><circle cx="4" cy="18" r="2.3"/><circle cx="12" cy="4" r="2.3"/><circle cx="12" cy="12" r="2.3"/><circle cx="12" cy="20" r="2.3"/><circle cx="20" cy="12" r="2.3"/></g></svg>',
    "cube": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M12 2 21 7v10l-9 5-9-5V7zM12 12l9-5M12 12v10M12 12 3 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
    "flame": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M12 2c1 4 6 6 6 12a6 6 0 0 1-12 0c0-3 2-5 3-6 0 2 1 3 2 3 0-3-1-6 1-9z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>',
    "tiles": '<svg viewBox="0 0 24 24" width="100%" height="100%"><g fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="8" width="6" height="8" rx="1.5"/><rect x="9" y="8" width="6" height="8" rx="1.5"/><rect x="16" y="8" width="6" height="8" rx="1.5"/></g></svg>',
    "window": '<svg viewBox="0 0 24 24" width="100%" height="100%"><g fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h3M3 18h3M18 6h3M18 18h3M3 6v12M21 6v12"/><rect x="8" y="9" width="8" height="6" rx="1.5"/></g></svg>',
    "vec": '<svg viewBox="0 0 24 24" width="100%" height="100%"><g fill="currentColor"><circle cx="5" cy="17" r="2.2"/><circle cx="10" cy="9" r="2.2"/><circle cx="18" cy="6" r="2.2"/><circle cx="16" cy="16" r="2.2"/></g><path d="M3 21 21 3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2 2"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" width="100%" height="100%"><rect x="6" y="2" width="12" height="20" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 18h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "brain": '<svg viewBox="0 0 24 24" width="100%" height="100%"><rect x="3" y="5" width="18" height="14" rx="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="9" cy="12" r="1.8" fill="currentColor"/><circle cx="15" cy="12" r="1.8" fill="currentColor"/><path d="M12 2v3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
}
