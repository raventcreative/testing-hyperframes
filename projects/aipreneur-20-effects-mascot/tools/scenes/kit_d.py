"""Private helpers for S17–S21 (city skyline, shard geometry, checklist board)."""
import math
from xk import box, r3, Rng, CYAN
from kit import BOARD

CITY_BASE = 1722            # tower bases sit on the floor line (WIDE feet)


def city(s):
    """original layered navy skyline: sky, moon, far / mid / near towers with lit windows, plaza floor.
    ids: {s}-sky {s}-cfar {s}-cmid {s}-cnear {s}-plaza"""
    R = Rng(1717)
    out = [f'<div class="abs" id="{s}-sky" style="{box(0, 0, 1080, 1920)}background:linear-gradient(180deg,#060e26 0%,#0c1f48 38%,#173f78 62%,#2a6aa8 72%,#0a1838 72.2%,#081430 100%)"></div>',
           f'<div class="abs" style="{box(0, 1180, 1080, 560)}background:radial-gradient(ellipse at 50% 100%,rgba(0,208,254,.32),rgba(0,208,254,0) 65%)"></div>',
           f'<div class="abs" style="{box(790, 470, 96, 96)}border-radius:50%;background:radial-gradient(circle at 40% 38%,#ffffff,#d6f6ff 55%,#9fe6ff);'
           f'box-shadow:0 0 40px 12px rgba(150,230,255,.35)"></div>']

    def tower(x, w, h, col, lit, edge, lw=9, lh=12):
        top = CITY_BASE - h
        dots = []
        cols, rows = max(1, int((w - 12) // 22)), max(1, int((h - 30) // 30))
        for _ in range(lit):
            c, r = int(R.u(0, cols)), int(R.u(0, rows))
            warm = R.f() < 0.35
            dots.append(f'<div class="abs" style="left:{8 + c * 22}px;top:{18 + r * 30}px;width:{lw}px;height:{lh}px;'
                        f'background:{"#ffe6b8" if warm else "#bff1ff"};opacity:{r3(0.55 + R.u(0, 0.45))};box-shadow:0 0 6px {"rgba(255,220,160,.6)" if warm else "rgba(0,208,254,.6)"}"></div>')
        grid = (f'<div class="abs" style="left:8px;top:18px;width:{w - 16}px;height:{h - 30}px;'
                f'background-image:linear-gradient(180deg,rgba(0,0,0,0) 0 {lh}px,{col} {lh}px 30px),linear-gradient(90deg,rgba(140,190,255,.13) 0 {lw}px,transparent {lw}px 22px);'
                f'background-size:22px 30px"></div>')
        rim = f'<div class="abs" style="left:{w - 3}px;top:0;width:3px;height:{h}px;background:linear-gradient(180deg,rgba(0,208,254,.8),rgba(0,208,254,0))"></div>' if edge else ""
        roof = f'<div class="abs" style="left:{w * 0.3}px;top:-26px;width:{max(4, w * 0.08)}px;height:26px;background:{col}"></div>' if h > 760 else ""
        return (f'<div class="abs" style="{box(x, top, w, h)}background:linear-gradient(180deg,{col},{col});border-top:2px solid rgba(160,210,255,.18)">'
                f'{grid}{"".join(dots)}{rim}{roof}</div>')

    layers = (("cfar", "#14305c", 0.85, (60, 130), (480, 860), 3, False),
              ("cmid", "#0f2550", 1.0, (90, 170), (380, 1000), 7, False),
              ("cnear", "#091a3a", 1.0, (150, 230), (820, 1250), 12, True))
    for (lid, col, op, (wa, wb), (ha, hb), lit, edge) in layers:
        parts, x = [], -60 if lid != "cnear" else -80
        while x < 1140:
            w = R.u(wa, wb)
            if lid == "cnear" and 250 < x < 700:      # keep the centre (behind the mascot) open
                x = 830
                continue
            h = R.u(ha, hb)
            parts.append(tower(x, w, h, col, lit, edge and x > 540))
            x += w + (R.u(6, 26) if lid != "cnear" else R.u(20, 60))
        out.append(f'<div class="abs" id="{s}-{lid}" style="{box(-60, 0, 1200, 1920)}opacity:{op}">' + "".join(parts) + "</div>")
    out.append(f'<div class="abs" id="{s}-plaza" style="{box(0, CITY_BASE, 1080, 1920 - CITY_BASE)}background:linear-gradient(180deg,#0b1d42 0%,#060f28 100%)">'
               f'<div class="abs" style="left:0;top:0;width:1080px;height:3px;background:linear-gradient(90deg,rgba(0,208,254,0),rgba(0,208,254,.8),rgba(0,208,254,0))"></div>'
               f'<div class="abs" style="left:0;top:3px;width:1080px;height:120px;background:linear-gradient(180deg,rgba(60,140,220,.22),rgba(60,140,220,0))"></div></div>')
    return out


def shards(origin, seed=1818, sectors=8, R=2600):
    """radial shard polygons around origin: 'sectors' wedges x 2 rings. Returns [(pts, centroid, dist)]"""
    ox, oy = origin
    G = Rng(seed)
    angs = [2 * math.pi * (k + G.u(-0.22, 0.22)) / sectors - math.pi / 2 for k in range(sectors)]
    r1 = [G.u(300, 470) for _ in range(sectors)]
    P = lambda a, r: (ox + r * math.cos(a), oy + r * math.sin(a))
    out = []
    for k in range(sectors):
        a0, a1 = angs[k], angs[(k + 1) % sectors] + (2 * math.pi if k == sectors - 1 else 0)
        am = (a0 + a1) / 2 + G.u(-0.08, 0.08)
        inner = [(ox, oy), P(a0, r1[k]), P(am, (r1[k] + r1[(k + 1) % sectors]) / 2 * G.u(0.95, 1.1)), P(a1, r1[(k + 1) % sectors])]
        outer = [P(a0, r1[k]), P(a0, R), P(a1, R), P(a1, r1[(k + 1) % sectors]), inner[2]]
        for pts, d in ((inner, 0.0), (outer, 1.0)):
            cx = sum(p[0] for p in pts) / len(pts)
            cy = sum(p[1] for p in pts) / len(pts)
            if d == 1.0:   # pull the outer centroid toward the visible frame
                cx, cy = ox + (cx - ox) * 0.35, oy + (cy - oy) * 0.35
            out.append((pts, (cx, cy), d, (a0 + a1) / 2))
    return out


def board_surface(s):
    """S20 end / S21 start: the checklist board surface at BOARD (navy porcelain, faint grid). id {s}-board"""
    x, y, w, h, r = BOARD
    return (f'<div class="abs por" id="{s}-board" style="{box(x, y, w, h)}border-radius:{r}px;overflow:hidden">'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),'
            f'linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:46px 46px"></div>'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h * 0.45}px;background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,0))"></div>'
            f'<div class="abs" style="left:{w / 2 - 1}px;top:120px;width:2px;height:{h - 160}px;background:rgba(255,255,255,.08)"></div></div>')
