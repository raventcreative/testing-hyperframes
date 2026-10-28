"""Fork A helpers (s02-s05): the socketed porcelain WORKBENCH (2.5D, faked perspective), camera point-zoom math,
explain-band chip rows."""
from xk import box, r3
from kit import MAT, chip

# workbench trapezoid (top edge y 1120, front edge y 1470, 50 px front face) — the visual home of the machine
B_TOP, B_BOT = 930, 1330
B_TL, B_TR, B_BL, B_BR = 150, 930, 40, 1040
# 10 sockets: back row 01-05, front row 06-10 (centre x, y, diameter, squash)
SOCKETS = ([(220 + 160 * k, 1030, 100, 0.52) for k in range(5)] + [(176 + 182 * k, 1212, 122, 0.55) for k in range(5)])


def zoom_to(px, py, k):
    """camera props (origin 540,960) that put world point (px,py) at screen (540,960) with scale k."""
    return {"x": r3(-(px - 540) * k), "y": r3(-(py - 960) * k), "scale": k}


def bench(id_):
    """porcelain workbench slab: top face (clip trapezoid), front face, contact shadow and 10 aluminium sockets."""
    top = (f'<div class="abs" style="left:0;top:{B_TOP}px;width:1080px;height:{B_BOT - B_TOP}px;'
           f'clip-path:polygon({B_TL}px 0,{B_TR}px 0,{B_BR}px 100%,{B_BL}px 100%);'
           f'background:linear-gradient(180deg,#f7f9fc 0%,#eef2f8 60%,#e3e9f2 100%)"></div>')
    grid = (f'<div class="abs" style="left:0;top:{B_TOP}px;width:1080px;height:{B_BOT - B_TOP}px;'
            f'clip-path:polygon({B_TL}px 0,{B_TR}px 0,{B_BR}px 100%,{B_BL}px 100%);opacity:.6;'
            f'background-image:linear-gradient(rgba(41,75,119,.10) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(41,75,119,.08) 1.5px,transparent 1.5px);'
            f'background-size:60px 44px"></div>')
    rim = (f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
           f'<path d="M{B_TL},{B_TOP} L{B_TR},{B_TOP} L{B_BR},{B_BOT} L{B_BL},{B_BOT} Z" fill="none" stroke="rgba(255,255,255,.95)" stroke-width="3"/>'
           f'<path d="M{B_TL},{B_TOP} L{B_TR},{B_TOP}" stroke="rgba(41,75,119,.25)" stroke-width="2"/></svg>')
    front = (f'<div class="abs" style="left:{B_BL}px;top:{B_BOT}px;width:{B_BR - B_BL}px;height:52px;border-radius:0 0 18px 18px;'
             f'background:linear-gradient(180deg,#dfe6f0 0%,#c3cddb 100%);box-shadow:inset 0 2px 0 rgba(255,255,255,.9),0 30px 40px -20px rgba(10,13,44,.5)"></div>')
    shadow = f'<div class="abs cshadow" style="{box(B_BL - 40, B_BOT + 20, B_BR - B_BL + 80, 90)}opacity:.6"></div>'
    socks = ""
    for n, (cx, cy, d, sq) in enumerate(SOCKETS):
        socks += (f'<div class="abs" id="{id_}-so{n}" style="{box(cx - d / 2, cy - d * sq / 2, d, d * sq)}">'
                  f'<div class="abs" style="inset:0;border-radius:50%;{MAT["alu"]}"></div>'
                  f'<div class="abs" style="left:18%;top:18%;width:64%;height:64%;border-radius:50%;'
                  f'background:radial-gradient(ellipse at 45% 35%,#2a3446 0%,#0b1020 70%);box-shadow:inset 0 3px 6px rgba(0,0,0,.6)"></div>'
                  f'<div class="abs" id="{id_}-sr{n}" style="left:-6px;top:-6px;right:-6px;bottom:-6px;border-radius:50%;border:4px solid #294B77;opacity:0"></div>'
                  f'</div>'
                  f'<div class="abs" id="{id_}-sn{n}" style="left:{r3(cx - 30)}px;top:{r3(cy + d * sq / 2 + 4)}px;width:60px;text-align:center;'
                  f'font:700 {20 if n < 5 else 24}px/1 Poppins;color:#294B77">{n + 1:02d}</div>')
    return f'<div class="abs" id="{id_}" style="left:0;top:0;width:1080px;height:1920px">{shadow}{front}{top}{grid}{rim}{socks}</div>'


def chip_row(S, prefix, items, y, size=28, gap=16, x0=None):
    """items = [(text, icon_svg, word_idx, dark)]. Lays chips out in one centred row in the explain band (estimated
    widths), each pops in on its spoken word. Returns the list of (id, x, w)."""
    ws = [len(t) * size * 0.64 + (size + 14 if ic else 0) + 52 for t, ic, _, _ in items]
    total = sum(ws) + gap * (len(ws) - 1)
    x = x0 if x0 is not None else (1080 - total) / 2
    out = []
    for k, ((t, ic, wi, dark), w) in enumerate(zip(items, ws)):
        cid = f"{prefix}{k}"
        S.front.append(chip(cid, x, y, t, ic, size=size, dark=dark))
        a = S.W(wi) - 0.08
        S.init(f"#{cid}", {"opacity": 0, "y": 26, "scale": 0.7})
        S.ft(f"#{cid}", {"opacity": 0, "y": 26, "scale": 0.7}, {"opacity": 1, "y": 0, "scale": 1}, a, 0.38, "back.out(2.2)")
        out.append((cid, x, w))
        x += w + gap
    return out


def chips_out(S, ids, t, dur=0.25):
    for k, cid in enumerate(ids):
        S.ft(f"#{cid}", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -18}, t + 0.03 * k, dur, "power2.in")


def ghost(id_, cx=540, top=440, w=520, h=440):
    """dashed blueprint ghost of the finished machine (dome + body), hovering above the bench — what we are building."""
    return (f'<svg class="abs" id="{id_}" style="left:{cx - w / 2 - 10}px;top:{top}px;width:{w + 20}px;height:{h + 20}px;overflow:visible" viewBox="-10 -10 {w + 20} {h + 20}">'
            f'<path id="{id_}-p" d="M{w * .18},{h * .42} A{w * .32},{h * .4} 0 0 1 {w * .82},{h * .42} L{w * .9},{h * .42} Q{w},{h * .42} {w},{h * .52} L{w},{h * .9} Q{w},{h} {w * .9},{h} L{w * .1},{h} Q0,{h} 0,{h * .9} L0,{h * .52} Q0,{h * .42} {w * .1},{h * .42} Z" '
            f'fill="rgba(41,75,119,.04)" stroke="#294B77" stroke-width="3" stroke-dasharray="14 10" opacity=".55"/>'
            f'<circle cx="{w / 2}" cy="{h * .3}" r="{h * .13}" fill="none" stroke="#294B77" stroke-width="3" stroke-dasharray="8 8" opacity=".5"/>'
            f'<path d="M{w * .5},{h} V{h + 60}" stroke="#294B77" stroke-width="3" stroke-dasharray="8 8" opacity=".45"/></svg>')
