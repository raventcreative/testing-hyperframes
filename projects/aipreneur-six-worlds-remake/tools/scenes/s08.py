"""S08 — THE HIDDEN SECRET (23.57–29.90)
VO: "Rahasia transisi yang terasa mahal ada di sambungannya. Satu objek membawa kita ke adegan berikutnya."
Opens on S07's dial ring (centre 540,1000, Ø560, six detents). The ring unrolls: its six detents fly out and become the
six world cards laid along one winding course (bar -> screen -> letter -> glass -> light -> dial). EXPLAIN MODE for the
first sentence: the mascot dollies in half-body, the course goes soft behind him, hands + head explain; type
`BUKAN BANYAK EFEK` (navy gradient) turns into the white-on-navy badge `TAPI NYAMBUNG` on "sambungannya".
"Satu objek membawa kita ke adegan berikutnya": he steps back (small, lower left), the course sharpens and ONE long
camera travel follows a light along the course through the six object hand-offs. Hand-off: the course straightens into a
flat timeline ruler (S09 opens on it)."""
import math
from xk import box, r3
from kit import HALF, SELF, tx, badge, blur_wrap, blur_in, blur_out, talk

RING = (540, 1000, 560)
NAMES = ["editorial", "ots", "word", "glass", "spot", "grade"]
OBJ = ["BAR", "LAYAR", "HURUF", "KACA", "CAHAYA", "DIAL"]
CW, CH = 176, 313
# course: a gentle S through the frame (card centres), drawn top -> bottom
PTS = [(240, 620), (540, 560), (840, 700), (790, 1010), (470, 1080), (210, 1240)]
RULER_Y = 1180


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W48, W52, W55, W56, W57, W58, W61, W62 = (S.W(i) for i in (48, 52, 55, 56, 57, 58, 61, 62))
    cx, cy, d = RING
    # ---------------------------------------------------------------- back: ring, course path, six cards
    S.back.append(f'<div class="abs" id="{s}-ring" style="{box(cx - d / 2, cy - d / 2, d, d)}border-radius:50%;border:10px solid #1c3561;'
                  f'box-shadow:0 0 0 2px rgba(255,255,255,.8) inset, 0 30px 50px -24px rgba(10,13,44,.45)"></div>')
    path = "M" + " C".join([])  # placeholder for readability
    # smooth path through PTS (cubic segments with vertical tangents)
    d_ = f"M{PTS[0][0]},{PTS[0][1]}"
    for (x0, y0), (x1, y1) in zip(PTS, PTS[1:]):
        my = (y0 + y1) / 2
        d_ += f" C{x0},{my} {x1},{my} {x1},{y1}"
    flat = " ".join(("M" if k == 0 else "L") + f"{90 + k * 180},{RULER_Y}" for k in range(6))
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-path" d="{d_}" fill="none" stroke="#294B77" stroke-width="7" stroke-linecap="round" stroke-dasharray="2 16" opacity=".55"/>'
                  f'<path id="{s}-trail" d="{d_}" fill="none" stroke="#0A0D2C" stroke-width="7" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')
    for k, n in enumerate(NAMES):
        x, y = PTS[k]
        S.back.append(f'<div class="abs" id="{s}-c{k}" style="{box(x - CW / 2, y - CH / 2, CW, CH)}">'
                      f'<div class="abs card" style="left:-8px;top:-8px;width:{CW + 16}px;height:{CH + 16}px;border-radius:20px"></div>'
                      f'<div class="abs" style="left:0;top:0;width:{CW}px;height:{CH}px;border-radius:14px;overflow:hidden">'
                      f'<img src="{SELF}/{n}.jpg" alt="" style="position:absolute;left:0;top:0;width:{CW}px;height:{CH}px" /></div>'
                      f'<div class="abs" style="left:0;top:{CH - 46}px;width:{CW}px;text-align:center"><span class="badge" style="font:700 20px/1 Poppins;padding:8px 12px;border-radius:10px">{k + 1:02d} · {OBJ[k]}</span></div>'
                      f'<div class="abs" id="{s}-h{k}" style="left:-14px;top:-14px;width:{CW + 28}px;height:{CH + 28}px;border-radius:24px;border:5px solid #0A0D2C"></div></div>')
    S.back.append(f'<div class="abs" id="{s}-dot" style="{box(PTS[0][0] - 16, PTS[0][1] - 16, 32, 32)}border-radius:16px;background:#fff;'
                  f'box-shadow:0 0 0 6px #0A0D2C, 0 0 24px 6px rgba(255,255,255,.9)"></div>')
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-ruler" d="M60,{RULER_Y} L1020,{RULER_Y}" stroke="#0A0D2C" stroke-width="7" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')
    blur_wrap(S)
    # ---------------------------------------------------------------- front: type
    S.front.append(tx(f"{s}-t1", 70, 290, 940, "BUKAN BANYAK EFEK", size=78, align="center"))
    S.front.append(badge(f"{s}-t2", 0, 288, "TAPI NYAMBUNG", size=78, style="width:1080px;text-align:center"))

    # ---------------------------------------------------------------- motion
    # ring unrolls: detents fly to their places on the course
    S.init(f"#{s}-ring", {"scale": 1, "opacity": 1, "rotation": 0})
    S.ft(f"#{s}-ring", {"scale": 1, "opacity": 1, "rotation": 0}, {"scale": 0.2, "opacity": 0, "rotation": 120}, t0 + 0.05, 0.5, "power3.in")
    for k in range(6):
        a = math.radians(-90 + k * 60)
        sx, sy = cx + d / 2 * math.cos(a), cy + d / 2 * math.sin(a)
        x, y = PTS[k]
        S.init(f"#{s}-c{k}", {"x": r3(sx - x), "y": r3(sy - y), "scale": 0.12, "opacity": 0})
        S.ft(f"#{s}-c{k}", {"x": r3(sx - x), "y": r3(sy - y), "scale": 0.12, "opacity": 0}, {"x": 0, "y": 0, "scale": 1, "opacity": 1}, t0 + 0.12 + k * 0.05, 0.55, "power3.out")
        S.init(f"#{s}-h{k}", {"opacity": 0})
    S.init(f"#{s}-path", {"opacity": 0})
    S.ft(f"#{s}-path", {"opacity": 0}, {"opacity": 0.55}, t0 + 0.4, 0.3, "none")
    # explain sentence: background soft
    blur_in(S, t0 + 0.25, 0.5)
    back = W56 - 0.3
    blur_out(S, back, 0.45)
    # type: BUKAN BANYAK EFEK -> TAPI NYAMBUNG
    S.init(f"#{s}-t1", {"opacity": 0, "y": 30})
    S.ft(f"#{s}-t1", {"opacity": 0, "y": 30}, {"opacity": 1, "y": 0}, W48 + 0.05, 0.35, "power3.out")
    S.ft(f"#{s}-t1", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -30}, W55 - 0.05, 0.22, "power2.in")
    S.init(f"#{s}-t2", {"opacity": 0, "scale": 0.7, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-t2", {"opacity": 0, "scale": 0.7}, {"opacity": 1, "scale": 1}, W55 + 0.05, 0.34, "back.out(2)")
    S.ft(f"#{s}-t2", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -24}, W56 + 0.1, 0.25, "power2.in")
    # one long travel: the light runs the course, each object hand-off lights up in turn
    tr0, tr1 = W57 - 0.1, W62 + 0.2
    S.init(f"#{s}-trail", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-trail", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, tr0, tr1 - tr0, "power1.inOut")
    S.init(f"#{s}-dot", {"x": 0, "y": 0, "opacity": 0})
    S.tset(f"#{s}-dot", {"opacity": 1}, tr0)
    seg = (tr1 - tr0) / 5
    for k in range(1, 6):
        x, y = PTS[k]
        px, py = PTS[k - 1]
        S.ft(f"#{s}-dot", {"x": r3(px - PTS[0][0]), "y": r3(py - PTS[0][1])}, {"x": r3(x - PTS[0][0]), "y": r3(y - PTS[0][1])}, tr0 + (k - 1) * seg, seg, "power1.inOut")
    for k in range(6):
        b = tr0 + k * seg - 0.05
        S.ft(f"#{s}-h{k}", {"opacity": 0}, {"opacity": 1}, b, 0.12, "power2.out")
        S.ft(f"#{s}-c{k}", {"scale": 1}, {"scale": 1.08}, b, 0.16, "back.out(2)")
        S.ft(f"#{s}-c{k}", {"scale": 1.08}, {"scale": 1}, b + 0.2, 0.25, "power2.out")
        S.fx(b + 0.02, "click" if k % 2 == 0 else "key", 0.035)
    # course pans as the light travels (camera follows, one move) and finally straightens into the ruler
    S.cam([(t0, {"y": 0, "scale": 1}, None), (tr0, {"y": 0, "scale": 1}, "none"), (tr1, {"y": -60, "scale": 1}, "sine.inOut"), (t1, {"y": 0, "scale": 1}, "power2.inOut")])
    S.init(f"#{s}-ruler", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-ruler", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, t1 - 0.32, 0.3, "power3.out")
    for k in range(6):
        S.ft(f"#{s}-c{k}", {"y": 0, "x": 0, "opacity": 1, "rotation": 0},
             {"y": RULER_Y - 120 - PTS[k][1], "x": 90 + k * 180 - PTS[k][0], "opacity": 0, "rotation": 0}, t1 - 0.36 + k * 0.02, 0.32, "power3.in")
    for sel in (f"#{s}-path", f"#{s}-trail", f"#{s}-dot"):
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, t1 - 0.3, 0.2, "power2.in")

    # ---------------------------------------------------------------- mascot: explain (half-body) -> step back, small lower-left
    small = {"fx": 840, "fy": 1880, "h": 700, "yaw": -18, "pitch": 6}
    S.mv([(t0, {"fx": 540, "fy": 1700, "h": 900, "yaw": 0, "pitch": 6}, None), (t0 + 0.5, dict(HALF, yaw=-4), "power3.inOut"),
          (W52, dict(HALF, yaw=5), "sine.inOut"), (back, dict(HALF, yaw=-2), "sine.inOut"), (back + 0.5, small, "power3.inOut"),
          (t1, dict(small, yaw=-24), "sine.inOut")])
    talk(S, 48, 55, seed=0, rest=False)
    S.act("armL", [(back + 0.1, "low", 0.4)])
    S.act("armR", [(back + 0.1, "low", 0.4), (W57 - 0.1, "point", 0.3), (W61, "pointUp", 0.3), (t1 - 0.2, "low", 0.4)])
    S.act("head", [(back + 0.1, [-0.1, -0.2, 0.0], 0.4), (W58, [-0.18, -0.32, 0.02], 0.5), (W61, [-0.06, -0.36, -0.03], 0.5), (t1 - 0.1, [-0.04, -0.1, 0], 0.4)])
    S.act("torso", [(back + 0.1, {"chest": [0, -0.08, 0]}, 0.4)])
    S.fx(t0 + 0.1, "whoosh", 0.05)
    S.fx(W55 + 0.06, "pop", 0.07)
    S.fx(t1 - 0.3, "whoosh", 0.04)
