"""S02 — 01/06 EDITORIAL SPLIT (5.03–7.77)  VO: "Grafik tumbuh, dan kamera menembusnya."
Opens on S01's hand-off: the white grid slab at CHART. 40/60 split: the mascot (3/4, turned toward the chart) on the
left, the editorial chart on the right. The baseline traces first, then six extruded bars rise out of it with a
NON-uniform rhythm (different start, duration and ease each); no numbers, no views — abstract editorial cells only.
The mascot presents the chart on "Grafik", follows bar #03 with his eyes. "kamera": slow anticipation push; on
"menembusnya" the camera flies THROUGH bar #03 (the mascot, nearer the lens, whips out of frame left = faster
parallax); the bar's dark front face fills the lens and its rectangular contour tightens into the anodized
monitor bezel at MONITOR — S03 opens on exactly that monitor."""
from xk import box, r3
from kit import CHART, MONITOR, badge, tx, shadow
from kit_a import bar3d, bar_x, BAR_W, BAR_H, BASE_Y, DEPTH, HERO, monitor

STARTS = [0.0, 0.11, 0.17, 0.31, 0.36, 0.52]      # non-uniform stagger (s after "Grafik")
DURS = [0.46, 0.38, 0.62, 0.34, 0.56, 0.44]
EASES = ["power3.out", "back.out(1.4)", "power2.out", "expo.out", "back.out(1.15)", "power4.out"]


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W9, W10, W12, W13 = S.W(9), S.W(10), S.W(12), S.W(13)       # Grafik 5.10 tumbuh 5.44 kamera 6.28 menembusnya 6.78
    cx, cy, cw, ch = CHART
    # ---------------------------------------------------------------- back: chart card (same as S01's slab)
    parts = [f'<div class="abs card grid-fine" style="{box(0, 0, cw, ch)}border-radius:26px"></div>']
    parts.append(f'<div class="abs" style="left:33px;top:34px;width:{cw - 66}px;height:46px;display:flex;align-items:center;gap:14px">'
                 f'<span class="badge" style="font:700 24px/1 Poppins, sans-serif;padding:9px 12px;border-radius:10px">01/06</span>'
                 f'<span class="tx" style="font:700 30px/1 Poppins, sans-serif;letter-spacing:.06em">EDITORIAL</span></div>')
    parts.append(f'<div class="abs" style="{box(33, 100, cw * 0.55, 14)}border-radius:7px;background:rgba(41,75,119,.28)"></div>')
    parts.append(f'<div class="abs" style="{box(33, 126, cw * 0.36, 10)}border-radius:5px;background:rgba(41,75,119,.16)"></div>')
    # y ticks (no labels / values)
    for k in range(5):
        parts.append(f'<div class="abs" style="{box(14, BASE_Y - 130 * (k + 1), 10, 2)}background:rgba(41,75,119,.35)"></div>')
    parts.append(f'<div class="abs" id="{s}-base" style="{box(24, BASE_Y, cw - 48, 4)}background:#0A0D2C;border-radius:2px"></div>')
    for k, h in enumerate(BAR_H):
        parts.append(bar3d(f"{s}-b{k}", bar_x(k), BASE_Y, BAR_W, h, hero=(k == HERO)))
        parts.append(f'<div class="abs" style="{box(bar_x(k) - 4, BASE_Y + 10, BAR_W + 24, 22)}border-radius:50%;background:radial-gradient(ellipse,rgba(10,13,44,.22),rgba(10,13,44,0) 70%)"></div>')
    # cell labels under the bars: abstract categories (not data)
    for k in range(6):
        parts.append(f'<div class="abs" style="{box(bar_x(k), BASE_Y + 34, BAR_W, 8)}border-radius:4px;background:rgba(41,75,119,{0.45 if k == HERO else 0.18})"></div>')
    S.back.append(f'<div class="abs" id="{s}-world" style="{box(0, 0, 1080, 1920)}">'
                  + shadow(cx + 30, cy + ch - 20, cw - 20, 70, 0.55, id_=f"{s}-csh")
                  + f'<div class="abs" id="{s}-chart" style="{box(cx, cy, cw, ch)}">' + "".join(parts) + "</div></div>")
    # ---------------------------------------------------------------- front: monitor (the hand-off object) + navy fill
    S.front.append(f'<div class="abs" id="{s}-mw" style="{box(0, 0, 1080, 1920)}">' + monitor(s) +
                   f'<div class="abs" id="{s}-fill" style="{box(MONITOR[0], MONITOR[1], MONITOR[2], MONITOR[3])}border-radius:26px;'
                   f'background:linear-gradient(180deg,#22416d 0%,#0A0D2C 100%)"></div></div>')

    # ---------------------------------------------------------------- motion: chart
    S.init(f"#{s}-base", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-base", {"scaleX": 0}, {"scaleX": 1}, t0 + 0.02, 0.32, "power2.inOut")
    for k, h in enumerate(BAR_H):
        sel = f"#{s}-b{k}-in"
        S.init(sel, {"y": h + DEPTH + 2})
        S.ft(sel, {"y": h + DEPTH + 2}, {"y": 0}, W9 - 0.04 + STARTS[k], DURS[k], EASES[k])
    # bar #03 settles a touch later with a tiny secondary rise on "tumbuh" (it is the hero)
    r_end = W9 - 0.04 + STARTS[HERO] + DURS[HERO] + 0.02
    S.ft(f"#{s}-b{HERO}-in", {"y": 0}, {"y": -14}, r_end, 0.24, "power2.out")
    S.ft(f"#{s}-b{HERO}-in", {"y": -14}, {"y": 0}, r_end + 0.25, 0.26, "power2.inOut")

    # camera: anticipation push on "kamera", fly-through bar #03 on "menembusnya"
    bx = cx + bar_x(HERO) + BAR_W / 2
    by = cy + BASE_Y - BAR_H[HERO] / 2 + DEPTH / 2
    def toward(sc):
        return {"scale": sc, "x": r3((540 - (540 + sc * (bx - 540))) * min(1, sc / 4)), "y": r3((960 - (960 + sc * (by - 960))) * min(1, sc / 4))}
    fly0, fly1 = W13 - 0.06, W13 + 0.26
    S.keys(f"#{s}-world", [(t0, {"scale": 1, "x": 0, "y": 0, "transformOrigin": "540px 960px"}, None),
           (W12 - 0.05, {"scale": 1, "x": 0, "y": 0}, "none"),
           (fly0, dict(toward(1.18)), "power1.in"),
           (fly1, dict(toward(4.4)), "power3.in"),
           (fly1 + 0.25, dict(toward(9.0)), "power2.out")])
    S.ft(f"#{s}-csh", {"opacity": 0.55}, {"opacity": 0}, fly0, 0.2, "power2.in")
    S.ft(f"#{s}-chart", {"opacity": 1}, {"opacity": 0}, fly1 + 0.02, 0.14, "power1.in")
    # the bar's front face (now filling the lens) tightens into the monitor bezel
    mx, my, mw, mh = MONITOR
    face_w, face_h = BAR_W * 4.4, BAR_H[HERO] * 4.4
    sx0, sy0 = face_w / mw, face_h / mh
    fy0 = 960 + 4.4 * 0 - (my + mh / 2)          # bar face is centred on the lens at the switch
    S.init(f"#{s}-mw", {"opacity": 0})
    S.tset(f"#{s}-mw", {"opacity": 1}, fly1)
    S.init(f"#{s}-mon", {"scaleX": sx0, "scaleY": sy0, "y": fy0, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-mon", {"scaleX": sx0, "scaleY": sy0, "y": fy0}, {"scaleX": 1, "scaleY": 1, "y": 0}, fly1, 0.36, "power3.out")
    S.init(f"#{s}-fill", {"scaleX": sx0, "scaleY": sy0, "y": fy0, "opacity": 1, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-fill", {"scaleX": sx0, "scaleY": sy0, "y": fy0}, {"scaleX": 1, "scaleY": 1, "y": 0}, fly1, 0.36, "power3.out")
    S.ft(f"#{s}-fill", {"opacity": 1}, {"opacity": 0}, fly1 + 0.16, 0.26, "power2.out")

    # ---------------------------------------------------------------- mascot: 40% left, 3/4 toward the chart
    v = {"fx": 225, "fy": 1795, "h": 1010, "yaw": -14, "pitch": 5}
    S.mv([(t0, dict(v, yaw=-8), None), (W10, dict(v, yaw=-16), "sine.inOut"), (fly0, dict(v, yaw=-18), "sine.inOut")])
    S.mx([(t0, {"x": 0, "scale": 1, "transformOrigin": "225px 1300px"}, None),
          (fly0, {"x": 0, "scale": 1}, "none"),
          (fly1, {"x": -760, "scale": 1.7}, "power3.in")])
    S.mset("V", {"vis": 0}, fly1 + 0.02)
    S.act("root", [(t0, {"ry": 0.3}, 0.3), (W12, {"ry": 0.38}, 0.4)])
    S.act("armL", [(t0, "low", 0.2), (W9 - 0.15, "present", 0.3), (W10 + 0.25, "point", 0.32), (W12 + 0.05, "pointUp", 0.28)])
    S.act("armR", [(t0, "low", 0.2), (W9, "open", 0.32), (W10 + 0.3, "low", 0.4), (W12, "explain", 0.3)])
    S.act("head", [(t0, [-0.04, 0.22, 0.02], 0.3), (W9, [-0.08, 0.32, 0.03], 0.28), (W10 + 0.2, [-0.14, 0.26, -0.02], 0.35),
                   (W12, [-0.1, 0.3, 0.0], 0.3)])
    S.act("torso", [(t0, {"chest": [0, 0.1, 0]}, 0.3), (W9, {"chest": [0.04, 0.16, 0]}, 0.3), (W12, {"chest": [0.06, 0.12, 0]}, 0.3)])
    S.fx(t0 + 0.03, "click", 0.05)
    S.fx(W9 + 0.1, "pop", 0.05)
    S.fx(fly0 + 0.05, "whoosh", 0.07)
    S.fx(fly1 + 0.3, "click", 0.06)
