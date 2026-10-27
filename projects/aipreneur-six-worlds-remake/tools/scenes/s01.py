"""S01 — THE SEED: ONE VIDEO, SIX SLOTS (0.00–5.03)
VO: "Satu video. Enam edit berbeda. Tapi semuanya nyambung. Lihat."
Frame 0 is already the hero: the 3D mascot (left third, curious head tilt, 3/4 toward the panel) and, on the right, an
editorial control panel with six thin timeline slots layered at different depths. "Satu video": `1 VIDEO` (navy gradient).
"Enam edit berbeda": white-in-navy badge `6 GAYA`, the six slots fill with their world names one beat at a time.
"Tapi semuanya nyambung": one navy thread runs through all six slots. "Lihat": he taps slot #01 and the camera closes in
— slot #01 grows into the white chart slab (kit.CHART) that S02 opens on; the other slots fall away."""
from xk import box, r3
from kit import SLOTS, CHART, tx, badge, shadow

NAMES = ["EDITORIAL SPLIT", "OVER THE SHOULDER", "BACKDROP WORD", "GLASS WIDGETS", "SPOTLIGHT", "COLOR GRADE"]
PX, PY, PW, PH = 520, 520, 520, 930      # panel


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W1, W2, W4, W5, W6, W7, W8 = (S.W(i) for i in (1, 2, 4, 5, 6, 7, 8))
    S.persp, S.persp_origin = 1500, (780, 980)
    # ---------------------------------------------------------------- back: panel + slots (3D, varied depth)
    S.back.append(shadow(PX + 30, PY + PH - 20, PW, 90, 0.55, id_=f"{s}-psh"))
    slots = []
    for k, (x, y, w, h) in enumerate(SLOTS):
        lx, ly = x - PX, y - PY
        slots.append(f'<div class="abs card p3" id="{s}-sl{k}" style="{box(lx, ly, w, h)}border-radius:16px">'
                     f'<div class="abs" style="left:18px;top:18px;width:82px;height:82px;border-radius:12px;background:linear-gradient(135deg,#e7eef9,#cfdcf0)"></div>'
                     f'<div class="abs" id="{s}-sf{k}" style="left:18px;top:18px;width:82px;height:82px;border-radius:12px;background:linear-gradient(135deg,#0A0D2C,#294B77);'
                     f'color:#fff;font:700 30px/82px Poppins;text-align:center">{k + 1:02d}</div>'
                     f'<div class="abs" style="left:118px;top:28px;width:300px;height:12px;border-radius:6px;background:rgba(41,75,119,.12)"></div>'
                     f'<div class="abs" id="{s}-sn{k}" style="left:118px;top:22px;width:310px;white-space:nowrap">'
                     f'<span class="tx" style="font:700 27px/34px Poppins">{NAMES[k]}</span></div>'
                     f'<div class="abs" style="left:118px;top:66px;width:{r3(150 + 40 * (k % 3))}px;height:10px;border-radius:5px;background:rgba(41,75,119,.14)"></div></div>')
    S.back.append(f'<div class="abs p3" id="{s}-panel" style="{box(PX, PY, PW, PH)}">'
                  f'<div class="abs card" style="left:-26px;top:-90px;width:{PW + 52}px;height:{PH + 120}px;border-radius:28px;opacity:.94"></div>'
                  f'<div class="abs" style="left:0;top:-62px;width:{PW}px;white-space:nowrap"><span class="tx" style="font:700 26px/30px Poppins;letter-spacing:.12em">TIMELINE · 6 SLOT</span></div>'
                  + "".join(slots) +
                  f'<svg class="abs" style="left:0;top:0;width:{PW}px;height:{PH}px;overflow:visible" viewBox="0 0 {PW} {PH}">'
                  f'<path id="{s}-thr" d="' + " ".join(("M" if k == 0 else "L") + f"{SLOTS[k][0] - PX + 59},{SLOTS[k][1] - PY + 59}" for k in range(6)) +
                  f'" fill="none" stroke="#294B77" stroke-width="5" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>'
                  "</div>")
    # the slab that slot #01 becomes (S02 opens on it)
    cx, cy, cw, ch = CHART
    S.back.append(f'<div class="abs card grid-fine" id="{s}-slab" style="{box(cx, cy, cw, ch)}border-radius:26px"></div>')
    # ---------------------------------------------------------------- front: type
    S.front.append(tx(f"{s}-t1", 70, 286, 520, "1 VIDEO", size=112))
    S.front.append(badge(f"{s}-t2", 74, 420, "6 GAYA", size=84))
    S.front.append(f'<div class="abs" id="{s}-tap" style="{box(SLOTS[0][0] + 20, SLOTS[0][1] + 20, 80, 80)}border-radius:40px;border:4px solid #294B77"></div>')

    # ---------------------------------------------------------------- motion
    S.init(f"#{s}-panel", {"rotationY": -16, "rotationX": 4, "x": 40, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-panel", {"rotationY": -16, "rotationX": 4, "x": 40}, {"rotationY": -10, "rotationX": 2, "x": 0}, t0, W8 - 0.1, "sine.inOut")
    for k in range(6):
        sel = f"#{s}-sl{k}"
        z = (0, 40, 14, 60, 24, 70)[k]
        S.init(sel, {"z": z, "x": 120, "opacity": 0})
        S.tset(sel, {"opacity": 1}, t0 + 0.0 + k * 0.035)
        S.ft(sel, {"z": z, "x": 120}, {"z": z, "x": 0}, t0 + k * 0.035, 0.5, "power3.out")
        S.init(f"#{s}-sf{k}", {"scale": 0, "opacity": 0})
        b = W2 + k * (W5 - 0.1 - W2) / 6
        S.ft(f"#{s}-sf{k}", {"scale": 0, "opacity": 0}, {"scale": 1, "opacity": 1}, b, 0.26, "back.out(2.2)")
        S.init(f"#{s}-sn{k}", {"clipPath": "inset(0px 100% 0px 0px)"})
        S.ft(f"#{s}-sn{k}", {"clipPath": "inset(0px 100% 0px 0px)"}, {"clipPath": "inset(0px 0% 0px 0px)"}, b + 0.05, 0.3, "power2.out")
    S.init(f"#{s}-thr", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-thr", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W5, W7 + 0.4 - W5, "power2.inOut")
    S.init(f"#{s}-t1", {"y": 40, "opacity": 0})
    S.ft(f"#{s}-t1", {"y": 40, "opacity": 0}, {"y": 0, "opacity": 1}, S.W(0), 0.35, "power3.out")
    S.init(f"#{s}-t2", {"scale": 0.6, "opacity": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-t2", {"scale": 0.6, "opacity": 0}, {"scale": 1, "opacity": 1}, W2 - 0.04, 0.32, "back.out(2)")
    # "Lihat": tap on slot #01, the slot grows into the chart slab; everything else falls away
    tap = W8 + 0.05
    S.init(f"#{s}-tap", {"scale": 0.4, "opacity": 0})
    S.ft(f"#{s}-tap", {"scale": 0.4, "opacity": 0.9}, {"scale": 1.6, "opacity": 0}, tap, 0.4, "power2.out")
    go = tap + 0.12
    for sel in (f"#{s}-t1", f"#{s}-t2"):
        S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": -30}, go, 0.3, "power2.in")
    for k in range(1, 6):
        z = (0, 40, 14, 60, 24, 70)[k]
        S.ft(f"#{s}-sl{k}", {"y": 0, "opacity": 1, "rotation": 0}, {"y": 260 + 40 * k, "opacity": 0, "rotation": 6 + k}, go + 0.03 * k, 0.4, "power2.in")
    S.ft(f"#{s}-thr", {"opacity": 1}, {"opacity": 0}, go, 0.2, "power2.in")
    S.ft(f"#{s}-sl0", {"opacity": 1}, {"opacity": 0}, t1 - 0.16, 0.14, "none")
    S.ft(f"#{s}-panel", {"rotationY": -10, "rotationX": 2, "x": 0}, {"rotationY": 0, "rotationX": 0, "x": 0}, go, t1 - go - 0.05, "power3.inOut")
    S.ft(f"#{s}-psh", {"opacity": 0.55}, {"opacity": 0}, go, 0.3, "power2.in")
    # slab: starts as slot #01's rect and grows into CHART
    x0, y0, w0, h0 = SLOTS[0]
    S.init(f"#{s}-slab", {"opacity": 0, "x": x0 - cx, "y": y0 - cy, "scaleX": w0 / cw, "scaleY": h0 / ch, "transformOrigin": "0% 0%"})
    S.tset(f"#{s}-slab", {"opacity": 1}, t1 - 0.16)
    S.ft(f"#{s}-slab", {"x": x0 - cx, "y": y0 - cy, "scaleX": w0 / cw, "scaleY": h0 / ch}, {"x": 0, "y": 0, "scaleX": 1, "scaleY": 1}, go + 0.1, t1 - go - 0.12, "power3.inOut")

    # ---------------------------------------------------------------- mascot: curious, left third; taps on "Lihat"
    v = {"fx": 300, "fy": 1790, "h": 1240, "yaw": 22, "pitch": 5}
    S.mv([(t0, v, None), (W8 - 0.2, dict(v, fx=290, yaw=26), "sine.inOut"), (t1, dict(v, fx=280, h=1180, yaw=24), "power2.inOut")])
    S.act("head", [(t0, [-0.08, 0.22, 0.14], 0.3), (S.W(0), [-0.05, 0.3, 0.1], 0.35), (W2, [0.02, 0.36, 0.0], 0.35), (W5, [-0.06, 0.18, 0.06], 0.35),
                   (W6, [-0.02, 0.32, -0.05], 0.35), (W8, [0.05, 0.4, 0.0], 0.25), (t1, [0.0, 0.3, 0.02], 0.4)])
    S.act("armL", [(t0, "low", 0.3), (W2 - 0.14, "present", 0.32), (W4 + 0.2, "low", 0.4), (W6 - 0.12, "explain", 0.3), (W8 - 0.18, "point", 0.24), (t1 - 0.1, "low", 0.4)])
    S.act("armR", [(t0, "low", 0.3), (S.W(0) - 0.1, "palmUp", 0.3), (W1 + 0.3, "low", 0.4), (W6, "open", 0.32), (W7 + 0.3, "low", 0.4)])
    S.act("torso", [(t0, {"chest": [0, 0.08, 0.03]}, 0.3), (W8 - 0.15, {"chest": [0.06, 0.14, 0], "spine": [0.04, 0, 0]}, 0.25), (t1, {}, 0.4)])
    S.fx(W2, "pop", 0.05)
    S.fx(W5 + 0.1, "whoosh", 0.04)
    S.fx(tap, "click", 0.08)
    S.fx(go + 0.1, "whoosh", 0.05)
