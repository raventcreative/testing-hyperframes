"""S12 — GREEN SCREEN (efek #12).
Opens on the mascot in front of a real-looking green screen (tracking crosses). A key line sweeps left -> right and
replaces the green with an app view: big focus timer top-left, 3 tasks in the middle, one sentence below. The mascot
stays in front, lower right, so his head clears the timer; the timer starts counting and task 2 gets ticked."""
from xk import box, r3, check_svg

VIEW = {"fx": 768, "fy": 1250, "h": 870, "yaw": -14, "pitch": 5}
TASKS = ["Riset 5 hook pakai AI", "Generate visual produk", "Jadwalkan 3 posting"]
TIMES = ["25:00", "24:59", "24:58", "24:57", "24:56"]


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    tw = t0 + 0.45          # key wipe starts
    wd = 0.55
    # ---------------------------------------------------------------- back: app view (revealed)
    app = [f'<div class="abs" style="left:0;top:0;width:1080px;height:1080px;background:linear-gradient(160deg,#f7faff 0%,#e8f0fb 55%,#d9e5f5 100%)"></div>',
           f'<div class="abs grid-fine" style="left:0;top:0;width:1080px;height:1080px;opacity:.55"></div>',
           f'<div class="abs" style="{box(640, 260, 560, 560)}border-radius:50%;background:radial-gradient(circle,rgba(41,75,119,.22),rgba(41,75,119,0) 68%)"></div>',
           f'<div class="abs" style="{box(60, 56, 150, 40)}border-radius:20px;background:linear-gradient(135deg,#0A0D2C,#294B77);color:#fff;font:700 18px/40px Poppins, sans-serif;text-align:center;letter-spacing:.12em">FOKUS</div>']
    for k, tm in enumerate(TIMES):
        app.append(f'<div class="abs" id="{s}-tm{k}" style="{box(52, 92, 560, 190)}white-space:nowrap"><span class="tx" style="font:700 176px/190px Poppins, sans-serif;letter-spacing:-0.02em">{tm}</span></div>')
    app.append(f'<div class="abs" style="{box(64, 288, 440, 8)}border-radius:4px;background:rgba(41,75,119,.14)"></div>'
               f'<div class="abs" id="{s}-tbar" style="{box(64, 288, 440, 8)}border-radius:4px;background:linear-gradient(90deg,#294B77,#0A0D2C)"></div>')
    for k, t in enumerate(TASKS):
        y = 352 + k * 104
        done = k == 0
        app.append(f'<div class="abs" id="{s}-t{k}" style="{box(60, y, 444, 86)}border-radius:20px;background:#ffffff;box-shadow:0 0 0 1px rgba(41,75,119,.10),0 14px 24px -16px rgba(10,13,44,.4)">'
                   f'<div class="abs" id="{s}-cb{k}" style="left:20px;top:21px;width:44px;height:44px;border-radius:12px;border:3px solid #294B77;background:{"linear-gradient(135deg,#0A0D2C,#294B77)" if done else "#fff"}"></div>'
                   f'<div class="abs" id="{s}-cf{k}" style="left:20px;top:21px;width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,#0A0D2C,#294B77)"></div>'
                   f'<div class="abs" style="left:28px;top:29px;width:28px;height:28px">{check_svg(f"{s}-ck{k}", "#ffffff", 3.6, drawn=done)}</div>'
                   f'<div class="abs" style="left:84px;top:0;width:350px;font:700 23px/86px Poppins, sans-serif;color:#0A0D2C;white-space:nowrap">{t}</div></div>')
    app.append(f'<div class="abs" id="{s}-sent" style="{box(62, 680, 440, 100)}"><span class="tx" style="font:400 30px/42px Poppins, sans-serif">Satu sesi fokus, <b style="font-weight:700">3 konten</b> siap tayang.</span></div>')
    S.back.append(f'<div class="abs" id="{s}-app" style="left:0;top:0;width:1080px;height:1080px">' + "".join(app) + "</div>")
    # ---------------------------------------------------------------- back: the green screen (on top of the app, wiped away)
    marks = "".join(f'<div class="abs" style="{box(x - 14, y - 2, 28, 4)}background:rgba(255,255,255,.75)"></div><div class="abs" style="{box(x - 2, y - 14, 4, 28)}background:rgba(255,255,255,.75)"></div>'
                    for x in (150, 540, 930) for y in (150, 520, 890))
    S.back.append(f'<div class="abs" id="{s}-green" style="left:0;top:0;width:1080px;height:1080px;background:linear-gradient(180deg,#22c25c 0%,#16a84a 70%,#12923f 100%)">'
                  f'<div class="abs" style="left:-100px;top:-200px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.18),rgba(255,255,255,0) 65%)"></div>'
                  f'{marks}</div>')
    S.back.append(f'<div class="abs" id="{s}-edge" style="{box(-30, 0, 30, 1080)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.95) 70%,rgba(190,215,250,.9) 85%,rgba(255,255,255,0));'
                  f'box-shadow:0 0 30px 8px rgba(255,255,255,.6)"></div>')

    # ---------------------------------------------------------------- motion: key wipe
    S.init(f"#{s}-green", {"clipPath": "inset(0px 0px 0px 0px)"})
    S.ft(f"#{s}-green", {"clipPath": "inset(0px 0px 0px 0px)"}, {"clipPath": "inset(0px 0px 0px 1080px)"}, tw, wd, "power2.inOut")
    S.init(f"#{s}-edge", {"x": 0, "opacity": 0})
    S.tset(f"#{s}-edge", {"opacity": 1}, tw)
    S.ft(f"#{s}-edge", {"x": 0}, {"x": 1110}, tw, wd, "power2.inOut")
    S.tset(f"#{s}-edge", {"opacity": 0}, tw + wd + 0.01)
    # app items settle in behind the key line (slight rise, staggered by x position = when the key reaches them)
    for sel, k in ((f"#{s}-t0", 0), (f"#{s}-t1", 1), (f"#{s}-t2", 2), (f"#{s}-sent", 3)):
        S.init(sel, {"y": 0})
        S.ft(sel, {"y": 22}, {"y": 0}, tw + 0.1 + k * 0.06, 0.45, "power3.out")
    # timer counts down once the app is live
    tk0 = tw + wd + 0.35
    for k in range(len(TIMES)):
        S.init(f"#{s}-tm{k}", {"opacity": 1 if k == 0 else 0})
        if k:
            S.tset(f"#{s}-tm{k - 1}", {"opacity": 0}, tk0 + (k - 1) * 0.95 + 0.6)
            S.tset(f"#{s}-tm{k}", {"opacity": 1}, tk0 + (k - 1) * 0.95 + 0.6)
    S.init(f"#{s}-tbar", {"scaleX": 1, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-tbar", {"scaleX": 1}, {"scaleX": 0.96}, tk0, t1 - tk0 - 0.02, "none")
    # task 2 gets ticked
    tc = t0 + 2.6
    for k in (1, 2):
        S.init(f"#{s}-cf{k}", {"scale": 0, "opacity": 1, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-cf1", {"scale": 0}, {"scale": 1}, tc, 0.22, "back.out(2.5)")
    S.ft(f"#{s}-ck1", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, tc + 0.12, 0.22, "power2.out")
    S.ft(f"#{s}-t1", {"x": 0}, {"x": 8}, tc, 0.1, "power2.out")
    S.ft(f"#{s}-t1", {"x": 8}, {"x": 0}, tc + 0.1, 0.25, "power2.inOut")
    S.init(f"#{s}-cf0", {"scale": 1})

    # ---------------------------------------------------------------- mascot: in front the whole time
    S.mv([(t0, VIEW, None), (tw + wd, dict(VIEW, yaw=-22), "sine.inOut"), (t1, dict(VIEW, yaw=-18), "sine.inOut")])
    S.act("armR", [(t0, "low", 0.01), (t0 + 0.05, "wave", 0.3), (tw + 0.1, "low", 0.35), (tw + wd + 0.1, "point", 0.35), (tc + 0.6, "low", 0.4)])
    S.act("armL", [(t0, "low", 0.01), (tw + wd + 0.25, "together", 0.35), (tc + 0.9, "palmUp", 0.35), (t1 - 0.5, "low", 0.4)])
    S.act("head", [(t0, [-0.02, -0.04, 0.03], 0.01), (tw + wd, [-0.12, -0.36, 0.03], 0.4), (tc - 0.1, [-0.02, -0.3, 0.05], 0.35),
                   (tc + 0.9, [-0.04, -0.06, 0], 0.4), (t1 - 0.5, [0, -0.12, 0.02], 0.4)])
    S.act("torso", [(t0, {"chest": [0.02, 0, 0]}, 0.01), (tw + wd, {"chest": [0.03, -0.14, 0]}, 0.4), (tc + 0.9, {"chest": [0.02, -0.04, 0]}, 0.4)])
