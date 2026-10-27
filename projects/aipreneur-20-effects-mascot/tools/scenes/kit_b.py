"""Private helpers for S04–S08 (frame escape -> snap zoom -> checklist pop -> headline storm -> zoom portal).
Contracts shared ONLY between these scenes (both sides built here):
  STRIP_B  S06 end (top pill stretched) == S07 start: headline band above the head (kit.STRIP would sit behind the face)
  RING_B   S07 end (strip curls into a ring) == S08 start: portal ring beside the mascot's head (never over the face)
  PORTAL_VIEW  mascot framing shared by S07 end / S08 start (3/4, head left of the ring)"""
from xk import box, r3, CYAN

STRIP_B = (-40, 400, 1160, 96)
RING_B = (820, 860, 480)            # centre x, y, diameter (hole Ø424)
PORTAL_VIEW = {"fx": 330, "fy": 1780, "h": 1180, "yaw": -16, "pitch": 5}
CHECK_VIEW = {"fx": 320, "fy": 1820, "h": 1380, "yaw": -20, "pitch": 5}   # S06 (3/4, looking screen-right)
CHECK_END = {"fx": 320, "fy": 1840, "h": 1420, "yaw": -25, "pitch": 5}    # S06 end == S07 start
STORM_VIEW = {"fx": 540, "fy": 1780, "h": 1180, "yaw": 0, "pitch": 5}     # S07 centre


def band(id_, x, y, w, h, inner="", rot=0, size=56, extra=""):
    """smoked-glass headline band with cyan edge lines; white Poppins Bold text (cyan spans for keywords)."""
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}transform:rotate({rot}deg);{extra}">'
            f'<div class="abs smoked" style="left:0;top:0;width:{r3(w)}px;height:{r3(h)}px;border-radius:6px;border-left:0;border-right:0;'
            f'border-top:3px solid {CYAN};border-bottom:3px solid {CYAN}"></div>'
            f'<div class="abs" id="{id_}-t" style="left:0;top:0;width:{r3(w)}px;height:{r3(h)}px;font:700 {size}px/{r3(h)}px Poppins, sans-serif;'
            f'color:#fff;text-align:center;white-space:nowrap;letter-spacing:.02em">{inner}</div></div>')


def ring_markup(id_, cx, cy, d, rim=True):
    """satin-metal portal ring (annulus via radial mask) + cyan acrylic inner rim + soft drop shadow."""
    R = d / 2
    th = 28
    return (f'<div class="abs" id="{id_}" style="{box(cx - R, cy - R, d, d)}">'
            f'<div class="abs" style="left:0;top:0;width:{r3(d)}px;height:{r3(d)}px;filter:drop-shadow(0 18px 26px rgba(3,8,28,.7))">'
            f'<div class="abs" style="left:0;top:0;width:{r3(d)}px;height:{r3(d)}px;border-radius:50%;'
            f'background:conic-gradient(from 210deg,#f1f4f8,#8b97aa 18%,#dfe5ee 32%,#9aa6b8 50%,#f6f8fb 62%,#7f8ba0 80%,#f1f4f8);'
            f'-webkit-mask:radial-gradient(circle at 50% 50%,transparent 0 {r3(R - th)}px,#000 {r3(R - th + 1)}px {r3(R - 1)}px,transparent {r3(R)}px);'
            f'mask:radial-gradient(circle at 50% 50%,transparent 0 {r3(R - th)}px,#000 {r3(R - th + 1)}px {r3(R - 1)}px,transparent {r3(R)}px)"></div></div>'
            + (f'<div class="abs" style="left:{th - 2}px;top:{th - 2}px;width:{r3(d - 2 * th + 4)}px;height:{r3(d - 2 * th + 4)}px;border-radius:50%;'
               f'border:4px solid rgba(120,232,255,.95);box-shadow:0 0 16px rgba(0,208,254,.65), inset 0 0 14px rgba(0,208,254,.45)"></div>' if rim else "")
            + f'<div class="abs" style="left:{r3(R * 0.32)}px;top:{r3(R * 0.1)}px;width:{r3(R * 0.5)}px;height:10px;border-radius:5px;transform:rotate(-24deg);'
              f'background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.9),rgba(255,255,255,0))"></div></div>')


def porcelain_frame(id_, x, y, w, h, r, th=34, depth=10):
    """navy-porcelain picture frame around an opening (x, y, w, h, r): sidewall layers along -Z for thickness,
    glazed face, bevel, inner screen (lighter navy cyc). Needs a preserve-3d parent (fx-cam is)."""
    X, Y, Wd, Hd, R = x - th, y - th, w + 2 * th, h + 2 * th, r + th * 0.75
    out = [f'<div class="abs p3" id="{id_}" style="{box(X, Y, Wd, Hd)}">']
    out.append(f'<div class="abs" style="left:20px;top:{r3(Hd - 20)}px;width:{r3(Wd - 40)}px;height:60px;border-radius:50%;'
               f'background:radial-gradient(ellipse,rgba(3,8,28,.6),rgba(3,8,28,0) 70%);transform:translateZ(-40px)"></div>')
    for k in range(depth, 0, -1):
        c = "#0a1a38" if k > depth * 0.6 else "#14305a" if k > 2 else "#22477a"
        out.append(f'<div class="abs" style="left:0;top:0;width:{r3(Wd)}px;height:{r3(Hd)}px;border-radius:{r3(R)}px;background:{c};transform:translateZ({-k * 3}px)"></div>')
    out.append(f'<div class="abs por" style="left:0;top:0;width:{r3(Wd)}px;height:{r3(Hd)}px;border-radius:{r3(R)}px"></div>')
    # inner bevel + screen
    out.append(f'<div class="abs" style="left:{th - 6}px;top:{th - 6}px;width:{r3(w + 12)}px;height:{r3(h + 12)}px;border-radius:{r3(r + 6)}px;'
               f'background:linear-gradient(160deg,#081430,#2a5288);box-shadow:inset 0 2px 0 rgba(3,8,28,.6)"></div>')
    out.append(f'<div class="abs" id="{id_}-scr" style="left:{th}px;top:{th}px;width:{r3(w)}px;height:{r3(h)}px;border-radius:{r3(r)}px;'
               f'background:radial-gradient(ellipse at 50% 35%,#2f5f9c 0%,#173866 60%,#0d2347 100%)"></div>')
    out.append(f'<div class="abs" style="left:{r3(Wd * 0.08)}px;top:6px;width:{r3(Wd * 0.5)}px;height:4px;border-radius:2px;'
               f'background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.7),rgba(255,255,255,0))"></div>')
    out.append("</div>")
    return "".join(out)
