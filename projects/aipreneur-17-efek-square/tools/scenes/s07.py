"""S07 — CHECKLIST. A dark transparent card floats above his head; three steps tick every 0.2 s, each with a small pop,
and the counter in the top-right runs 0 dari 3 -> 3 dari 3. He looks up at it and celebrates when it completes."""
from xk import box, r3, check_svg

CX, CY, CW, CH = 230, 50, 620, 330
STEPS = ["Riset hook pakai AI", "Bikin script 30 detik", "Render &amp; posting"]


def build(S):
    s, t0 = S.id, S.t0
    rows = []
    for k, st in enumerate(STEPS):
        y = 104 + k * 70
        rows.append(f'<div class="abs" id="{s}-r{k}" style="{box(34, y, CW - 68, 56)}transform-origin:28px 28px">'
                    f'<div class="abs" style="left:0;top:8px;width:40px;height:40px;border-radius:12px;box-shadow:inset 0 0 0 2.5px rgba(255,255,255,.45)"></div>'
                    f'<div class="abs" id="{s}-b{k}" style="left:0;top:8px;width:40px;height:40px;border-radius:12px;background:#fff">'
                    f'<div class="abs" style="left:6px;top:6px;width:28px;height:28px">{check_svg(f"{s}-c{k}", "#0A0D2C", 3.6)}</div></div>'
                    f'<div class="abs" id="{s}-t{k}" style="left:62px;top:0;width:470px;font:700 30px/56px Poppins, sans-serif;color:#fff;white-space:nowrap">{st}</div></div>')
    counter = "".join(f'<div class="abs" id="{s}-n{k}" style="right:0;top:0;width:150px;text-align:right;font:700 24px/40px Poppins, sans-serif;color:#fff">'
                      f'<span style="display:inline-block;padding:0 14px;border-radius:12px;background:{"rgba(255,255,255,.14)" if k < 3 else "#fff"};'
                      f'color:{"#fff" if k < 3 else "#0A0D2C"}">{k} dari 3</span></div>' for k in range(4))
    S.front.append(f'<div class="abs" id="{s}-card" style="{box(CX, CY, CW, CH)}">'
                   f'<div class="abs" id="{s}-bgc" style="left:0;top:0;width:{CW}px;height:{CH}px;border-radius:30px;background:linear-gradient(150deg,rgba(18,32,68,.86) 0%,rgba(10,13,44,.80) 100%);'
                   f'box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.16),0 34px 60px -28px rgba(10,13,44,.7)"></div>'
                   f'<div class="abs" style="left:34px;top:30px;width:300px;font:700 20px/40px Poppins, sans-serif;color:rgba(255,255,255,.62);letter-spacing:.14em">TO-DO KONTEN</div>'
                   f'<div class="abs" style="left:{CW - 184}px;top:30px;width:150px;height:40px">{counter}</div>'
                   f'<div class="abs" style="left:34px;top:84px;width:{CW - 68}px;height:4px;border-radius:2px;background:rgba(255,255,255,.14)"></div>'
                   f'<div class="abs" id="{s}-bar" style="left:34px;top:84px;width:{CW - 68}px;height:4px;border-radius:2px;background:#fff"></div>'
                   + "".join(rows) + "</div>")
    a = t0 + 0.3
    S.init(f"#{s}-card", {"opacity": 0, "y": 30, "scale": 0.92, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-card", {"opacity": 0, "y": 30, "scale": 0.92}, {"opacity": 1, "y": 0, "scale": 1}, a, 0.4, "back.out(1.6)")
    S.init(f"#{s}-bar", {"scaleX": 0, "transformOrigin": "0% 50%"})
    for k in range(4):
        S.init(f"#{s}-n{k}", {"opacity": 1 if k == 0 else 0})
    c0 = t0 + 1.25
    for k in range(3):
        b = c0 + k * 0.2
        S.init(f"#{s}-b{k}", {"scale": 0, "opacity": 0, "transformOrigin": "20px 20px"})
        S.ft(f"#{s}-b{k}", {"scale": 0, "opacity": 0}, {"scale": 1, "opacity": 1}, b, 0.16, "back.out(3)")
        S.init(f"#{s}-c{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-c{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, b + 0.04, 0.16, "power2.out")
        S.init(f"#{s}-r{k}", {"scale": 1})
        S.ft(f"#{s}-r{k}", {"scale": 1}, {"scale": 1.07}, b, 0.08, "power2.out")
        S.ft(f"#{s}-r{k}", {"scale": 1.07}, {"scale": 1}, b + 0.08, 0.2, "back.out(3)")
        S.init(f"#{s}-t{k}", {"opacity": 0.72})
        S.ft(f"#{s}-t{k}", {"opacity": 0.72}, {"opacity": 1}, b, 0.12, "none")
        S.tset(f"#{s}-n{k}", {"opacity": 0}, b + 0.05)
        S.tset(f"#{s}-n{k + 1}", {"opacity": 1}, b + 0.05)
        S.ft(f"#{s}-bar", {"scaleX": k / 3}, {"scaleX": (k + 1) / 3}, b, 0.18, "power2.out")
    done = c0 + 0.45
    S.init(f"#{s}-n3", {"opacity": 0, "scale": 1, "transformOrigin": "100% 50%"})
    S.ft(f"#{s}-n3", {"scale": 1.25}, {"scale": 1}, done - 0.2, 0.3, "back.out(3)")
    S.ft(f"#{s}-card", {"scale": 1}, {"scale": 1.035}, done, 0.14, "power2.out")
    S.ft(f"#{s}-card", {"scale": 1.035}, {"scale": 1}, done + 0.14, 0.35, "back.out(2)")
    # gentle float afterwards
    S.ft(f"#{s}-card", {"y": 0}, {"y": -6}, done + 0.5, 1.3, "sine.inOut")
    S.ft(f"#{s}-card", {"y": -6}, {"y": 0}, done + 1.8, S.t1 - done - 1.8, "sine.inOut")
    # mascot: smaller, low in frame so the card sits above the head; looks up, points, celebrates
    v = {"fx": 540, "fy": 1330, "h": 900, "yaw": 0, "pitch": 3}
    S.mv([(t0, v, None), (a, dict(v, yaw=-3), "sine.inOut"), (S.t1, dict(v, yaw=3), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.01), (a + 0.25, "pointUp", 0.3), (done + 0.05, "fist", 0.25), (done + 1.2, "low", 0.45)])
    S.act("armR", [(t0, "low", 0.01), (done + 0.05, "fist", 0.25), (done + 1.2, "present", 0.45)])
    S.act("head", [(t0, [0, 0, 0], 0.01), (a + 0.1, [-0.22, 0.05, 0.02], 0.4), (c0, [-0.26, -0.04, -0.02], 0.25),
                   (done + 0.05, [0.08, 0.0, 0.06], 0.2), (done + 0.35, [-0.08, 0.08, -0.04], 0.4), (done + 1.3, [-0.03, -0.06, 0.03], 0.5)])
    S.act("root", [(done, {"y": 0}, 0.1), (done + 0.1, {"y": 0.02}, 0.15), (done + 0.3, {"y": 0}, 0.3)])
