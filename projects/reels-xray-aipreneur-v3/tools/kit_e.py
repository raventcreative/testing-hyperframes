"""Helpers for scenes s16–s18 (QC studio, repo case, CTA bubble). Pure markup builders, deterministic."""
import math
from xk import box, r3, shadow, rivets_line

GH = "assets/elements/ref15_github_mark_3d.png"   # user's 3D GitHub mark (background removed)


def magnifier(p, cx, cy, R=115, handle=True):
    """porcelain-ringed glass lens (+ navy-grip handle) whose centre sits at (cx, cy); tween #{p}-mag x/y/scale."""
    D = 2 * R
    h = ""
    if handle:
        h = (f'<div class="abs" style="left:{r3(R + R * 0.62)}px;top:{r3(R + R * 0.62)}px;width:36px;height:190px;transform-origin:18px 0;transform:rotate(-45deg)">'
             f'<div class="abs por" style="{box(0, 0, 36, 46)}border-radius:8px"></div>'
             f'<div class="abs" style="{box(2, 42, 32, 6)}background:#acc6e7;border-radius:3px"></div>'
             f'<div class="abs navy-side" style="{box(3, 50, 30, 138)}border-radius:6px 6px 16px 16px;box-shadow:inset 3px 0 0 rgba(255,255,255,.22),0 14px 20px -10px rgba(28,51,84,.45)"></div>'
             + "".join(f'<div class="abs" style="{box(6, 70 + k * 22, 24, 3)}background:rgba(203,219,244,.35);border-radius:2px"></div>' for k in range(5))
             + '</div>')
    ticks = "".join(
        f'<div class="abs" style="left:{r3(R + (R - 26) * math.cos(a) - 1.5)}px;top:{r3(R + (R - 26) * math.sin(a) - 6)}px;width:3px;height:12px;'
        f'background:rgba(41,75,119,.5);border-radius:2px;transform:rotate({r3(math.degrees(a) + 90)}deg)"></div>'
        for a in [k * math.pi / 2 + math.pi / 4 for k in range(4)])
    return (f'<div class="abs" id="{p}-mag" style="{box(cx - R, cy - R, D, D)}">'
            f'<div class="shadow-soft" style="{box(34, 54, D, D)}opacity:.75"></div>'
            + h +
            f'<div class="abs glass" style="{box(0, 0, D, D)}border-radius:50%;background:radial-gradient(circle at 38% 32%,rgba(255,255,255,.55) 0%,rgba(232,240,251,.25) 45%,rgba(172,198,231,.22) 100%)"></div>'
            f'<div class="abs" style="{box(R * 0.32, R * 0.22, R * 0.9, R * 0.9)}border-radius:50%;border-top:6px solid rgba(255,255,255,.85);border-left:3px solid rgba(255,255,255,.4);transform:rotate(-20deg)"></div>'
            + ticks +
            f'<div class="abs" style="{box(0, 0, D, D)}border-radius:50%;border:17px solid #f7f9fd;'
            f'box-shadow:inset 0 0 0 2.5px #294b77,0 0 0 2px #acc6e7,inset 2px 3px 0 17px rgba(255,255,255,.0),0 18px 30px -12px rgba(28,51,84,.4)"></div>'
            f'<div class="abs" style="{box(4, 4, D - 8, D - 8)}border-radius:50%;border-top:3px solid #ffffff;border-left:2px solid rgba(255,255,255,.8)"></div>'
            '</div>')


def check_svg(id_, size, stroke="#1c3354"):
    """mint confirmation disc with a drawable check (tween #{id}-p strokeDashoffset 60 -> 0)."""
    return (f'<svg id="{id_}" width="{size}" height="{size}" viewBox="0 0 48 48" style="position:absolute;left:0;top:0;overflow:visible">'
            f'<circle cx="24" cy="24" r="22" fill="#9fd8c4" stroke="#ffffff" stroke-width="2.5"/>'
            f'<circle cx="24" cy="24" r="17" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="1.2"/>'
            f'<path id="{id_}-p" d="M13.5 24.5 L21 32 L35 16.5" fill="none" stroke="{stroke}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" style="stroke-dasharray:60;stroke-dashoffset:60"/></svg>')


def letter_extrude(id_, ch, size, layers=9, step=1.7):
    """one dimensional letter: navy front (white top highlight) + deeper navy sidewall."""
    out = [f'<div id="{id_}" class="p3" style="position:relative;display:inline-block;white-space:nowrap">']
    for k in range(layers, 0, -1):
        col = "#13243d" if k > layers * 0.5 else "#1c3354"
        out.append(f'<div style="position:absolute;left:0;top:0;font:900 {size}px Montserrat;letter-spacing:0;color:{col};transform:translateZ({r3(-k * step)}px)">{ch}</div>')
    out.append(f'<div style="position:relative;font:900 {size}px Montserrat;letter-spacing:0;'
               f'background:linear-gradient(175deg,#5d84b9 0%,#294b77 45%,#1c3354 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent">{ch}</div>')
    out.append("</div>")
    return "".join(out)


def folder(p, x, y, w, h, mark=True, mark_id=None, mark_mode="img"):
    """navy code folder (tab, porcelain sheet peeking out, code ticks) carrying the 3D GitHub mark."""
    tab_w = w * 0.38
    m = ""
    if mark:
        mid = mark_id or f"{p}-gh"
        ms = h * 0.62
        if mark_mode == "img":
            inner = f'<img src="{GH}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:contain" />'
        else:
            inner = f'<div style="position:absolute;inset:0;background:url({GH}) center/contain no-repeat"></div>'
        bs = ms * 1.02
        m = (f'<div class="abs por" style="{box(w / 2 - bs / 2, h * 0.27, bs, bs)}border-radius:50%;box-shadow:inset 1.5px 1.5px 0 #fff,inset -1.5px -2px 0 rgba(172,198,231,.7),0 6px 10px -4px rgba(10,20,40,.45)"></div>'
             f'<div class="abs" id="{mid}-w" style="{box(w / 2 - ms * 0.36, h * 0.27 + bs * 0.1, ms * 0.72, ms * 0.8)}">'
             f'<div class="abs" id="{mid}" style="{box(0, 0, ms * 0.72, ms * 0.8)}">{inner}</div></div>')
    return (f'<div class="abs" id="{p}" style="{box(x, y, w, h)}">'
            f'<div class="abs" style="{box(0, 0, tab_w, h * 0.2)}border-radius:{r3(h * 0.06)}px {r3(h * 0.08)}px 0 0;background:linear-gradient(180deg,#3a6299,#294b77)"></div>'
            f'<div class="abs navy-side" style="{box(0, h * 0.1, w, h * 0.9)}border-radius:{r3(h * 0.05)}px;box-shadow:0 18px 26px -14px rgba(28,51,84,.5)"></div>'
            f'<div class="abs paper" style="{box(w * 0.08, h * 0.04, w * 0.84, h * 0.4)}border-radius:6px"></div>'
            + "".join(f'<div class="abs" style="{box(w * 0.16, h * (0.1 + k * 0.07), w * (0.5 - 0.12 * (k % 2)), 3)}background:#acc6e7;border-radius:2px"></div>' for k in range(3))
            + f'<div class="abs" style="{box(0, h * 0.24, w, h * 0.76)}border-radius:{r3(h * 0.05)}px;background:linear-gradient(170deg,#3a6299 0%,#294b77 55%,#1c3354 100%);'
              f'box-shadow:inset 0 2px 0 rgba(255,255,255,.28),inset 0 -3px 0 rgba(0,0,0,.18)"></div>'
            + m +
            f'<div class="rivet" style="left:{r3(w * 0.08)}px;top:{r3(h * 0.9)}px"></div><div class="rivet" style="left:{r3(w * 0.88)}px;top:{r3(h * 0.9)}px"></div>'
            '</div>')


def iris(id_, cx, cy, hole, color="#f2f6fb"):
    """circular window: everything outside a `hole`-wide circle is covered (huge border ring)."""
    B = 2300
    return (f'<div class="abs" id="{id_}" style="{box(cx - hole / 2 - B, cy - hole / 2 - B, hole + 2 * B, hole + 2 * B)}'
            f'border-radius:50%;border:{B}px solid {color};box-sizing:border-box"></div>')


# comment bubble shared by S17 (end pose) and S18 (unfolds): global box BX..BX+BW, BY..BY+BH, tail bottom-left
BX, BY, BW, BH = 290, 640, 680, 390


def bubble(p, inner=""):
    """porcelain shell + glass face + navy sidewall + tail. Wrapper #{p}-bub is absolutely placed at (BX, BY);
    tween it with rotationX (transformOrigin 50% 100%) / y / scale. `inner` goes on the glass face."""
    tail = (f'<svg class="abs" width="200" height="140" viewBox="0 0 200 140" style="left:40px;top:{BH - 40}px;overflow:visible">'
            f'<defs><linearGradient id="{p}-tg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d9e4f4"/></linearGradient></defs>'
            f'<path d="M30 0 L150 0 C120 40 70 86 6 122 C30 84 40 44 30 0 Z" fill="url(#{p}-tg)" stroke="#acc6e7" stroke-width="2"/>'
            f'<path d="M44 10 C46 40 40 70 26 98" fill="none" stroke="rgba(255,255,255,.95)" stroke-width="3" stroke-linecap="round"/></svg>')
    tail_side = (f'<svg class="abs" width="200" height="140" viewBox="0 0 200 140" style="left:46px;top:{BH - 34}px;overflow:visible;transform:translateZ(-14px)">'
                 f'<path d="M30 0 L150 0 C120 40 70 86 6 122 C30 84 40 44 30 0 Z" fill="#1c3354"/></svg>')
    slabs = "".join(f'<div class="abs" style="{box(0, 0, BW, BH)}border-radius:64px;background:{"#1c3354" if k > 5 else "#294b77" if k > 2 else "#3a6299"};transform:translateZ({-k * 2.2}px)"></div>' for k in range(8, 0, -1))
    return (f'<div class="abs p3" id="{p}-bub" style="{box(BX, BY, BW, BH)}">'
            + slabs + tail_side +
            f'<div class="abs por" style="{box(0, 0, BW, BH)}border-radius:64px"></div>'
            + tail +
            f'<div class="abs" style="{box(22, 22, BW - 44, BH - 44)}border-radius:46px;background:linear-gradient(160deg,rgba(255,255,255,.92) 0%,rgba(232,240,251,.85) 50%,rgba(203,219,244,.75) 100%);'
            f'box-shadow:inset 0 0 0 2px rgba(255,255,255,.95),inset 0 0 0 4px rgba(172,198,231,.55),inset 0 -10px 24px rgba(172,198,231,.35)"></div>'
            f'<div class="abs" style="{box(46, 34, BW * 0.5, 10)}border-radius:5px;background:linear-gradient(90deg,rgba(255,255,255,.95),rgba(255,255,255,0))"></div>'
            f'<div class="screw" style="left:{BW - 52}px;top:30px;width:12px;height:12px;--r:30deg"></div>'
            f'<div class="screw" style="left:{BW - 52}px;top:{BH - 42}px;width:12px;height:12px;--r:-40deg"></div>'
            + inner + '</div>')


def front(inner, z=400, origin=(590, 560)):
    """wrap overlay pieces in a plane pushed toward the camera (z) and scaled back (perspective 2000) so they keep
    their screen position/size but always sort IN FRONT of 3D geometry (preserve-3d sorts by depth, not DOM order)."""
    k = (2000 - z) / 2000
    return (f'<div class="abs p3" style="left:0;top:0;width:1080px;height:1920px;transform-origin:{origin[0]}px {origin[1]}px;'
            f'transform:translateZ({z}px) scale({r3(k)})">{inner}</div>')
