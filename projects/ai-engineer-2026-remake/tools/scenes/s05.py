"""S05 — 03 MACHINE LEARNING. VO: "Ketiga, machine learning. Pelajari cara data dipakai buat melatih dan menguji model.
Termasuk cara mengetahui ketika modelnya salah."
S04's data bead drops into a frosted-glass ML TEST PLANE (aluminium stand, drafting axes) and lands as the first point;
on "machine learning" more training beads rain in to their places. EXPLAIN MODE on "Pelajari cara data dipakai buat melatih
dan menguji model" (plane soft behind; chips DATA -> MELATIH -> MENGUJI). Step back: on "mengetahui" the fitted line draws
through the cloud, hollow TEST points appear; on "salah" one test point turns coral, a dashed residual drops to the line
and an inspection ring locks on it. Hand-off: the fitted line ends exactly on kit.ML_TREND (navy 6 px) for S06."""
from xk import box, r3
from kit import MAT, part, shadow, grid_floor, blur_wrap, explain, ICON, ML_TREND
from kit_a import chip_row, chips_out

PL = (100, 740, 880, 600)      # glass plane x y w h
TRAIN = [(330, 1110, 0), (205, 1150, 1), (260, 1205, 2), (390, 1060, 3), (455, 1100, 4), (520, 1030, 5), (585, 1060, 6),
         (640, 1010, 7), (700, 950, 8), (760, 975, 9), (840, 890, 10), (880, 930, 11), (430, 1140, 12), (600, 990, 13)]
TEST = [(300, 1080), (470, 1030), (720, 990), (900, 860)]
OUT = (560, 870)               # the wrong test point (residual to the line at y ~1037)


def line_y(x):
    pts = ML_TREND
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return pts[-1][1]


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    px, py, pw, ph = PL
    S.back.append(grid_floor(f"{s}-grid", y=1560))
    # stand + plane
    S.back.append(f'<div class="abs" id="{s}-rig" style="left:0;top:0;width:1080px;height:1920px">'
                  + shadow(px + 120, py + ph + 150, pw - 240, 90, 0.55)
                  + part(None, 520, py + ph - 10, 40, 190, "alu", 10)
                  + part(None, 360, py + ph + 170, 360, 46, "porcelain", 16)
                  + part(f"{s}-plane", px, py, pw, ph, "glass", 30,
                         inner=f'<div class="abs" style="left:60px;top:40px;width:3px;height:{ph - 100}px;background:rgba(41,75,119,.45)"></div>'
                               f'<div class="abs" style="left:60px;top:{ph - 60}px;width:{pw - 110}px;height:3px;background:rgba(41,75,119,.45)"></div>'
                               f'<div class="abs" style="inset:40px 50px 60px 60px;background-image:linear-gradient(rgba(41,75,119,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(41,75,119,.07) 1px,transparent 1px);background-size:60px 60px"></div>')
                  + part(f"{s}-plate", px + 30, py - 70, 420, 54, "enamel", 14,
                         inner='<div class="abs" style="inset:0;font:700 24px/54px Poppins;color:#fff;letter-spacing:.06em;text-align:center">03 MACHINE LEARNING</div>')
                  + '</div>')
    # fitted line (exact hand-off geometry), residual, test points, beads
    d = "M" + " L".join(f"{x},{y}" for x, y in ML_TREND)
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-res" d="M{OUT[0]},{OUT[1] + 16} V{r3(line_y(OUT[0]))}" stroke="#e2614b" stroke-width="4" stroke-dasharray="10 8" opacity="0"/>'
                  f'<path id="{s}-fit" d="{d}" fill="none" stroke="#0A0D2C" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                  + "".join(f'<circle id="{s}-t{k}" cx="{x}" cy="{y}" r="13" fill="#ffffff" stroke="#294B77" stroke-width="5"/>' for k, (x, y) in enumerate(TEST))
                  + f'<circle id="{s}-out" cx="{OUT[0]}" cy="{OUT[1]}" r="14" fill="#ffffff" stroke="#294B77" stroke-width="5"/>'
                  f'<circle id="{s}-ring" cx="{OUT[0]}" cy="{OUT[1]}" r="40" fill="none" stroke="#e2614b" stroke-width="4"/></svg>')
    for x, y, k in TRAIN:
        S.back.append(f'<div class="abs" id="{s}-b{k}" style="{box(x - 15, y - 15, 30, 30)}border-radius:50%;'
                      f'background:radial-gradient(circle at 35% 30%,#ffffff,#9fc4ff 35%,#294B77 75%,#0A0D2C);box-shadow:0 6px 10px -4px rgba(10,13,44,.6)"></div>')
    blur_wrap(S)
    ids = [c[0] for c in chip_row(S, f"{s}-k", [("data", ICON["db"], 72, False), ("melatih", ICON["gauge"], 75, False), ("menguji", ICON["check"], 77, True)], 444, size=30, gap=60)]
    S.front.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:600px;overflow:visible" viewBox="0 0 1080 600">'
                   + "".join(f'<path id="{s}-ar{k}" d="M{x} 484 H{x + 40} M{x + 26} 470 L{x + 41} 484 L{x + 26} 498" fill="none" stroke="#294B77" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                             for k, x in enumerate((0, 0))) + '</svg>')

    # ---------------------------------------------------------------- motion
    exp_in, exp_out = W(70) - 0.3, W(79) - 0.3
    S.cam([(t0, {"x": 0, "y": 420, "scale": 1.0}, None), (t0 + 0.55, {"x": 0, "y": 0, "scale": 1}, "power3.out"),
           (W(69) + 0.4, {"x": 0, "y": 0, "scale": 1.0}, "none"), (exp_out, {"x": 0, "y": 0, "scale": 1.0}, "none"),
           (W(84) - 0.3, {"x": -60, "y": 40, "scale": 1.08}, "sine.inOut"), (t1, {"x": 0, "y": 0, "scale": 1}, "power2.inOut")])
    # first bead (S04's) falls in and lands; the rest rain in on "machine learning"
    for n, (x, y, k) in enumerate(TRAIN):
        a = t0 + 0.12 if k == 0 else W(68) - 0.2 + 0.06 * n
        S.init(f"#{s}-b{k}", {"y": -900, "opacity": 0 if k else 1})
        if k:
            S.tset(f"#{s}-b{k}", {"opacity": 1}, a)
        S.ft(f"#{s}-b{k}", {"y": -900}, {"y": 0}, a, 0.45, "power2.in")
        S.ft(f"#{s}-b{k}", {"y": 0}, {"y": -14}, a + 0.45, 0.1, "power2.out")
        S.ft(f"#{s}-b{k}", {"y": -14}, {"y": 0}, a + 0.55, 0.12, "power2.in")
    S.fx(t0 + 0.57, "click", 0.06)
    S.fx(W(68), "key", 0.05)
    S.init(f"#{s}-plate", {"opacity": 0, "x": -30})
    S.ft(f"#{s}-plate", {"opacity": 0, "x": -30}, {"opacity": 1, "x": 0}, W(68) - 0.1, 0.35, "power3.out")
    # fitted line + test points + the wrong one
    S.init(f"#{s}-fit", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-fit", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(79), W(81) + 0.3 - W(79), "power2.inOut")
    S.fx(W(79) + 0.1, "sparkle", 0.04)
    for k in range(len(TEST)):
        S.init(f"#{s}-t{k}", {"scale": 0, "transformOrigin": "50% 50%"})
        S.ft(f"#{s}-t{k}", {"scale": 0}, {"scale": 1}, W(81) + 0.1 * k, 0.25, "back.out(3)")
    S.init(f"#{s}-out", {"scale": 0, "transformOrigin": "50% 50%", "attr": {"stroke": "#294B77", "fill": "#ffffff"}})
    S.ft(f"#{s}-out", {"scale": 0}, {"scale": 1}, W(82), 0.25, "back.out(3)")
    S.ft(f"#{s}-out", {"attr": {"stroke": "#294B77", "fill": "#ffffff"}}, {"attr": {"stroke": "#e2614b", "fill": "#ffd9d1"}}, W(84) - 0.05, 0.2, "power2.out")
    S.init(f"#{s}-res", {"opacity": 0})
    S.ft(f"#{s}-res", {"opacity": 0}, {"opacity": 1}, W(84), 0.25, "power2.out")
    S.init(f"#{s}-ring", {"scale": 2.4, "opacity": 0, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-ring", {"scale": 2.4, "opacity": 0}, {"scale": 1, "opacity": 1}, W(84) - 0.02, 0.3, "power3.out")
    S.fx(W(84), "ping", 0.06)
    # explain band
    for k, (sel, w0, w1) in enumerate(((f"#{s}-ar0", 72, 75), (f"#{s}-ar1", 75, 77))):
        S.init(sel, {"attr": {"stroke-dashoffset": 1}})
        S.ft(sel, {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(w1) - 0.15, 0.25, "power2.out")
        S.ft(sel, {"attr": {"stroke-dashoffset": 0}}, {"attr": {"stroke-dashoffset": -1}}, exp_out - 0.1, 0.25, "power2.in")
    chips_out(S, ids, exp_out - 0.1)

    # ---------------------------------------------------------------- mascot: centre -> explain -> lower right, inspects the error
    s04_end = {"fx": 560, "fy": 2000, "h": 760, "yaw": 24, "pitch": 6}
    rt = {"fx": 905, "fy": 1890, "h": 740, "yaw": -26, "pitch": 6}
    S.mv([(t0, s04_end, None), (t0 + 0.6, dict(s04_end, yaw=0), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.35, "pointUp", 0.3), (W(68) + 0.3, "open", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (W(68), "palmUp", 0.3)])
    S.act("head", [(t0, [-0.2, 0.1, 0], 0.3), (t0 + 0.6, [0.12, 0.05, 0], 0.35), (W(68), [-0.08, -0.12, 0.04], 0.3)])
    explain(S, exp_in, exp_out, 70, 78, seed=4, enter=dict(s04_end, yaw=0), leave=rt)
    S.mv([(exp_out + 0.5, rt, None), (W(82), dict(rt, yaw=-32), "sine.inOut"), (W(84) + 0.1, dict(rt, yaw=-40, fx=880), "power2.out"),
          (t1, dict(rt, yaw=-36, fx=885), "sine.inOut")])
    S.act("armR", [(exp_out + 0.2, "low", 0.35), (W(80), "point", 0.3), (W(82), "low", 0.35), (W(84) - 0.2, "point", 0.22), (t1 - 0.1, "point", 0.3)])
    S.act("armL", [(exp_out + 0.2, "low", 0.35), (W(84) - 0.1, "chin", 0.3)])
    S.act("head", [(exp_out + 0.2, [0.0, -0.3, 0], 0.35), (W(80), [-0.08, -0.38, 0.03], 0.3), (W(84) - 0.1, [-0.14, -0.46, -0.06], 0.25)])
    S.act("torso", [(W(84) - 0.15, {"chest": [0.06, -0.16, 0]}, 0.3)])
