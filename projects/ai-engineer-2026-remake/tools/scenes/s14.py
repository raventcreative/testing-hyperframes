"""S14 — SATU PROYEK DULU (W199 – W214). VO: "Gak perlu belajar semuanya sekaligus. Mulai dari satu proyek kecil, lalu naikkan
levelnya sedikit demi sedikit."
EXPLAIN MODE first: he is at the front, the S13 rails go soft behind him; in the band a row of ten module sockets all
light at once on "semuanya", jam and dim on "sekaligus" — only #01 stays. He steps back to the lower left (DEMONSTRATE):
the camera starts tight on the first pad of the SAME rail (y = STAGE_RAIL_Y) and pulls back as three stage models grow on
it, linked by the one cable: PROYEK KECIL (small ML cube) -> APP LLM + RAG -> ASISTEN SIAP PAKAI. A light pulse runs along
the rail and each stage levels up when it arrives (staircase). Hand-off: the whole rail in view, pulse at the far end."""
from xk import box, r3
from kit import (STAGE_RAIL_Y, MAT, part, cable, grid_floor, shadow, blur_wrap, explain, ICON, EXPLAIN_BAND, HALF_IN)
from kit_d import label, icon_tile, stage_models

RY = STAGE_RAIL_Y
PADS = [(390, 150, 110), (640, 190, 180), (900, 220, 250)]     # centre x, width, height of each stage model


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    # ---------------------------------------------------------------- back: rail, pads, three stage models
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(cable(f"{s}-rail", f"M-20,{RY} L1100,{RY}", w=10, dash=False))
    S.back.append(f'<div class="abs" id="{s}-pulse" style="left:{-30}px;top:{RY - 16}px;width:32px;height:32px;border-radius:16px;background:#fff;'
                  f'box-shadow:0 0 0 6px #294B77,0 0 26px 8px rgba(150,190,255,.9)"></div>')
    names = [("PROYEK", "KECIL"), ("APP LLM", "+ RAG"), ("ASISTEN", "SIAP PAKAI")]
    S.back += stage_models(s, PADS, RY)
    for k, (cx, w, h) in enumerate(PADS):
        a, b = names[k]
        S.back.append(f'<div class="abs" id="{s}-lb{k}" style="{box(cx - 130, RY - 14 - h - 92, 260, 80)}">'
                      + label(None, 0, 0, 260, a, 30) + label(None, 0, 36, 260, b, 26, "#294B77", weight=400) + "</div>")
        if k < 2:  # level-up chevron between stages
            nx = PADS[k + 1][0]
            mx = (cx + w / 2 + nx - PADS[k + 1][1] / 2) / 2
            S.back.append(f'<svg class="abs" id="{s}-up{k}" style="left:{mx - 22}px;top:{RY - 120 - k * 40}px;width:44px;height:44px" viewBox="0 0 24 24">'
                          f'<path d="M5 15 L12 8 L19 15" fill="none" stroke="#294B77" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    # the "level" path: one dashed ascending arc over the three stages, drawn on "naikkan levelnya"
    lv = f"M{PADS[0][0]},{RY - 250} C {PADS[0][0] + 160},{RY - 260} {PADS[1][0] - 40},{RY - 330} {PADS[1][0] + 60},{RY - 380} S {PADS[2][0] - 40},{RY - 470} {PADS[2][0] + 30},{RY - 520}"
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-lvd" d="{lv}" fill="none" stroke="#294B77" stroke-width="5" stroke-dasharray="4 14" stroke-linecap="round" opacity=".45"/>'
                  f'<path id="{s}-lvl" d="{lv}" fill="none" stroke="#0A0D2C" stroke-width="6" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')
    S.back.append(f'<div class="abs" id="{s}-lvt" style="left:{PADS[2][0] - 120}px;top:{RY - 600}px;width:240px;text-align:center">'
                  f'<span class="badge" style="font:700 34px/1.1 Poppins, sans-serif">LEVEL UP</span></div>')
    blur_wrap(S)
    # ---------------------------------------------------------------- front: explain band — ten sockets, all at once vs one
    by = EXPLAIN_BAND[0] + 30
    dots = ""
    for k in range(10):
        dots += (f'<div class="abs" id="{s}-d{k}" style="left:{k * 92}px;top:0;width:72px;height:72px;border-radius:18px;{MAT["glass"]}">'
                 f'<div class="abs" style="left:0;top:20px;width:72px;text-align:center;font:700 28px/1 Poppins;color:#0A0D2C">{k + 1:02d}</div></div>')
    S.front.append(f'<div class="abs" id="{s}-row" style="{box(80, by, 920, 72)}">{dots}</div>')
    S.front.append(f'<div class="abs" id="{s}-hl" style="{box(80 - 8, by - 8, 88, 88)}border-radius:24px;box-shadow:0 0 0 5px #0A0D2C"></div>')

    # ---------------------------------------------------------------- motion: explain band
    sem, sek = W(202), W(203)
    S.init(f"#{s}-row", {"opacity": 0, "y": 20})
    S.ft(f"#{s}-row", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, W(201) - 0.1, 0.35, "power3.out")
    for k in range(10):
        sel = f"#{s}-d{k}"
        S.init(sel, {"backgroundColor": "rgba(255,255,255,0.55)", "color": "#0A0D2C", "scale": 1, "x": 0, "rotation": 0, "opacity": 1})
        S.ft(sel, {"scale": 1}, {"scale": 1.1}, sem + k * 0.025, 0.14, "power2.out")
        S.ft(sel, {"scale": 1.1}, {"scale": 1}, sem + 0.16 + k * 0.025, 0.16, "power2.out")
        # jam on "sekaligus": everybody shoves (small seeded jitter), then 02-10 dim
        jx, jr = ((k * 37) % 9 - 4) * 2.2, ((k * 53) % 7 - 3) * 2.0
        S.ft(sel, {"x": 0, "rotation": 0}, {"x": jx, "rotation": jr}, sek, 0.08, "power2.out")
        S.ft(sel, {"x": jx, "rotation": jr}, {"x": 0, "rotation": 0}, sek + 0.1, 0.22, "back.out(3)")
        if k:
            S.ft(sel, {"opacity": 1}, {"opacity": 0.28}, sek + 0.35, 0.3, "power2.inOut")
    S.init(f"#{s}-hl", {"opacity": 0, "scale": 1.4})
    S.ft(f"#{s}-hl", {"opacity": 0, "scale": 1.4}, {"opacity": 1, "scale": 1}, sek + 0.4, 0.35, "back.out(2)")
    S.fx(sem, "click", 0.05)
    S.fx(sek + 0.4, "ping", 0.05)
    back = W(204) - 0.3
    S.ft(f"#{s}-row", {"opacity": 1}, {"opacity": 0}, back, 0.25, "power2.in")
    S.ft(f"#{s}-hl", {"opacity": 1}, {"opacity": 0}, back, 0.25, "power2.in")

    # ---------------------------------------------------------------- motion: demonstrate — stages grow on the rail, camera pulls back
    p0 = PADS[0]
    sc = 1.55
    fx_, fy_ = 600, 1160           # where stage 1 sits on screen while tight
    cx0, cy0 = p0[0], RY - 80
    tight = {"x": r3(fx_ - 540 - (cx0 - 540) * sc), "y": r3(fy_ - 960 - (cy0 - 960) * sc), "scale": sc}
    S.cam([(t0, {"x": 0, "y": 0, "scale": 1}, None), (back - 0.01, {"x": 0, "y": 0, "scale": 1}, "none"),
           (back + 0.5, tight, "power3.inOut"), (W(210) - 0.2, dict(tight, scale=sc * 0.98), "sine.inOut"),
           (W(213), {"x": 40, "y": -270, "scale": 1.04}, "power3.inOut"), (t1, {"x": 40, "y": -285, "scale": 1.03}, "sine.out")])
    births = [W(207) - 0.1, W(210) - 0.05, W(212) - 0.05]
    for k, bt in enumerate(births):
        S.init(f"#{s}-st{k}", {"scaleY": 0.05, "scaleX": 0.6, "opacity": 0, "transformOrigin": "50% 100%"})
        S.ft(f"#{s}-st{k}", {"scaleY": 0.05, "scaleX": 0.6, "opacity": 0}, {"scaleY": 1, "scaleX": 1, "opacity": 1}, bt, 0.45, "back.out(1.8)")
        S.init(f"#{s}-lb{k}", {"opacity": 0, "y": 16})
        S.ft(f"#{s}-lb{k}", {"opacity": 0, "y": 16}, {"opacity": 1, "y": 0}, bt + 0.25, 0.3, "power3.out")
        S.fx(bt + 0.05, "pop", 0.05)
    for k in range(2):
        S.init(f"#{s}-up{k}", {"opacity": 0, "y": 20})
        S.ft(f"#{s}-up{k}", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, births[k + 1] - 0.15, 0.3, "power3.out")
    # the light pulse runs the same cable stage to stage
    S.init(f"#{s}-pulse", {"x": 0, "opacity": 0})
    S.tset(f"#{s}-pulse", {"opacity": 1}, back + 0.4)
    stops = [(back + 0.4, 0), (births[0], PADS[0][0] + 30), (births[1], PADS[1][0] + 30), (births[2], PADS[2][0] + 30), (t1 - 0.1, 1110)]
    for (ta, xa), (tb, xb) in zip(stops, stops[1:]):
        S.ft(f"#{s}-pulse", {"x": xa}, {"x": xb}, ta, max(0.05, tb - ta), "power2.inOut")
    S.init(f"#{s}-lvd", {"opacity": 0})
    S.ft(f"#{s}-lvd", {"opacity": 0}, {"opacity": 0.45}, W(209), 0.4, "power2.out")
    S.init(f"#{s}-lvl", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-lvl", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(210), W(214) - W(210) + 0.2, "power1.inOut")
    S.init(f"#{s}-lvt", {"opacity": 0, "y": 20, "scale": 0.8})
    S.ft(f"#{s}-lvt", {"opacity": 0, "y": 20, "scale": 0.8}, {"opacity": 1, "y": 0, "scale": 1}, W(214) - 0.05, 0.35, "back.out(2)")
    S.init(f"#{s}-ok", {"scale": 1})
    S.ft(f"#{s}-ok", {"scale": 1}, {"scale": 1.18}, W(214), 0.18, "power2.out")
    S.ft(f"#{s}-ok", {"scale": 1.18}, {"scale": 1}, W(214) + 0.2, 0.25, "power2.out")

    # ---------------------------------------------------------------- mascot: explain at the front, then lower-left watching the stages
    enter = {"fx": 430, "fy": 1790, "h": 730, "yaw": 0, "pitch": 6}      # where S13 left him (at the lever)
    left = {"fx": 125, "fy": 1850, "h": 620, "yaw": 28, "pitch": 6}
    explain(S, t0, back, 199, 203, seed=4, enter=enter, leave=left)
    S.mv([(back + 0.5, left, None), (W(210), dict(left, yaw=32), "sine.inOut"), (t1, dict(left, yaw=28), "sine.inOut")])
    S.act("armL", [(back + 0.2, "low", 0.4), (W(206) - 0.1, "point", 0.3), (W(209), "explain", 0.35), (W(212) - 0.1, "pointUp", 0.3),
                   (t1 - 0.3, "low", 0.4)])
    S.act("armR", [(back + 0.2, "low", 0.4), (W(210), "palmUp", 0.35), (t1 - 0.25, "low", 0.4)])
    S.act("head", [(back + 0.2, [0.06, 0.28, 0], 0.4), (W(207), [0.08, 0.34, 0.03], 0.35), (W(211), [-0.04, 0.4, 0.02], 0.4),
                   (W(213), [-0.1, 0.46, 0.04], 0.4)])
    S.act("torso", [(back + 0.2, {"chest": [0.03, 0.12, 0]}, 0.4), (W(212), {"chest": [0.0, 0.18, 0]}, 0.5)])
