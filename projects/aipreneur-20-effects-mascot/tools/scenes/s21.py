"""S21 — 20 CHECKLIST (33.30–35.73)  VO: "Yang bikin ini terasa mahal bukan efeknya satu-satu."
Opens on S20's end: the phone's back has become the checklist board. Two columns list all 20 effects (numbered,
Poppins 30 px). From 'Yang' the checks chain 01 -> 20 (acrylic discs fill, strokes draw, names brighten) while a
cyan focus bar steps along and the progress bar fills. 'mahal': macro push onto the last two names (19, 20).
'bukan efeknya satu-satu': the camera pulls back, the list dims and one cyan line threads all 20 checks in
order - the value is the chain, not the items. Hand-off: the board falls away and the thread straightens into a
single horizontal cyan line across the frame at y 1000 (S22 starts from that line). Mascot: off-screen here
(the board fills the frame; he returns in S22)."""
from xk import box, r3, CYAN, EFFECTS, check_svg
from kit import BOARD
from kit_d import board_surface

LINE_Y = 1000


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W93, W97, W98, W100 = S.W(93), S.W(97), S.W(98), S.W(100)   # Yang 33.38, mahal 34.22, bukan 34.54, satu-satu 35.12
    bx, by, bw, bh, br = BOARD
    # ---------------------------------------------------------------- back layer: board + rows + thread
    S.back.append(f'<div class="abs" id="{s}-bw" style="{box(0, 0, 1080, 1920)}">' + board_surface(s) + "</div>")
    rows, pts = [], []
    row_y = lambda r: by + 132 + r * 92
    for i, name in enumerate(EFFECTS):
        c, r = divmod(i, 10)
        dx = bx + 46 + c * 450
        yy = row_y(r)
        pts.append((dx + 22, yy + 22))
        rows.append(f'<div class="abs" id="{s}-r{i}" style="{box(dx, yy, 420, 44)}opacity:.5">'
                    f'<div class="abs" style="left:0;top:0;width:44px;height:44px;border-radius:22px;border:2px solid rgba(120,232,255,.7);background:rgba(3,8,28,.25)"></div>'
                    f'<div class="abs acrylic" id="{s}-d{i}" style="left:0;top:0;width:44px;height:44px;border-radius:22px;opacity:0"></div>'
                    f'<div class="abs" style="left:9px;top:9px;width:26px;height:26px">{check_svg(f"{s}-k{i}", color="#ffffff", width=3.4)}</div>'
                    f'<div class="abs" style="left:60px;top:0;width:52px;font:700 28px/44px Poppins;color:{CYAN}">{i + 1:02d}</div>'
                    f'<div class="abs" style="left:112px;top:0;width:310px;font:400 30px/44px Poppins;color:#fff;white-space:nowrap">{name}</div></div>')
    head = (f'<div class="abs" style="left:{bx + 46}px;top:{by + 40}px;width:400px;font:700 38px/48px Poppins;color:#fff;letter-spacing:.02em">CHECKLIST</div>'
            f'<div class="abs" style="left:{bx + bw - 346}px;top:{by + 40}px;width:300px;font:700 38px/48px Poppins;color:{CYAN};text-align:right">20 EFEK</div>'
            f'<div class="abs" style="left:{bx + 46}px;top:{by + 100}px;width:{bw - 92}px;height:6px;border-radius:3px;background:rgba(255,255,255,.14)"></div>'
            f'<div class="abs" id="{s}-pb" style="left:{bx + 46}px;top:{by + 100}px;width:{bw - 92}px;height:6px;border-radius:3px;background:{CYAN};box-shadow:0 0 10px rgba(0,208,254,.7)"></div>')
    S.back.append(f'<div class="abs" id="{s}-list" style="{box(0, 0, 1080, 1920)}">'
                  f'<div class="abs acrylic" id="{s}-focus" style="{box(bx + 30, row_y(0) - 14, 430, 72)}border-radius:20px;opacity:0"></div>'
                  + head + "".join(rows) + "</div>")
    d0 = "M" + " L".join(f"{r3(x)},{r3(y)}" for x, y in pts)
    n = len(pts)
    d1 = "M" + " L".join(f"{r3(-40 + 1160 * k / (n - 1))},{LINE_Y}" for k in range(n))
    S.back.append(f'<svg class="abs" style="{box(0, 0, 1080, 1920)}overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-th" d="{d0}" fill="none" stroke="{CYAN}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" '
                  f'pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" style="filter:drop-shadow(0 0 8px rgba(0,208,254,.9))"/></svg>')

    # ---------------------------------------------------------------- motion: checks chain
    ck0, step = W93 + 0.02, 0.056
    S.init(f"#{s}-list", {"opacity": 0})
    S.ft(f"#{s}-list", {"opacity": 0}, {"opacity": 1}, t0, 0.14, "power1.out")
    S.init(f"#{s}-pb", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-pb", {"scaleX": 0}, {"scaleX": 1}, ck0, step * 19 + 0.1, "none")
    fkeys = [(t0, {"x": 0, "y": 0, "opacity": 0}, None), (ck0 - 0.04, {"opacity": 1}, "power1.out")]
    for i in range(20):
        c, r = divmod(i, 10)
        t = ck0 + step * i
        S.init(f"#{s}-d{i}", {"opacity": 0, "scale": 0.6})
        S.ft(f"#{s}-d{i}", {"opacity": 0, "scale": 0.6}, {"opacity": 1, "scale": 1}, t, 0.16, "back.out(2.5)")
        S.init(f"#{s}-k{i}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-k{i}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, t + 0.03, 0.12, "power2.out")
        S.init(f"#{s}-r{i}", {"opacity": 0.5})
        S.ft(f"#{s}-r{i}", {"opacity": 0.5}, {"opacity": 1}, t, 0.1, "power1.out")
        S.ft(f"#{s}-r{i}", {"opacity": 1}, {"opacity": 0.4}, W100 - 0.05, 0.25, "power1.inOut")
        if i:
            fkeys.append((t, {"x": c * 450, "y": r * 92}, "power3.out"))
    fkeys += [(W98, {"opacity": 1}, "none"), (W98 + 0.2, {"opacity": 0}, "power1.in")]
    S.keys(f"#{s}-focus", fkeys)
    # macro push onto 19 / 20, pull back on 'bukan'
    tx, ty = bx + 46 + 450 + 210, row_y(8) + 92
    sc = 1.5
    push = {"scale": sc, "x": r3(-(tx - 540) * sc), "y": r3(1000 - 960 - (ty - 960) * sc)}
    S.css.append(f"#{s}-persp, #{s}f-persp {{ clip-path: inset(236px 0px 0px 0px); }}")   # the macro push never runs into the logo / header band
    S.cam([(t0, {"scale": 1, "x": 0, "y": 0}, None), (W97 - 0.12, {"scale": 1, "x": 0, "y": 0}, "none"),
           (W97 + 0.2, push, "power3.inOut"), (W98 + 0.05, push, "none"), (W98 + 0.42, {"scale": 1, "x": 0, "y": 0}, "power3.inOut")])
    # the thread: draws through all 20 checks, then straightens into the horizontal hand-off line
    th0 = W98 + 0.42
    S.init(f"#{s}-th", {"attr": {"stroke-dashoffset": 1, "d": d0}})
    S.ft(f"#{s}-th", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, th0, W100 + 0.12 - th0, "power1.inOut")
    S.ft(f"#{s}-th", {"attr": {"d": d0}}, {"attr": {"d": d1}}, W100 + 0.18, t1 - W100 - 0.2, "power3.inOut")
    S.init(f"#{s}-bw", {"opacity": 1, "scale": 1, "y": 0, "transformOrigin": "540px 830px"})
    S.ft(f"#{s}-bw", {"opacity": 1, "scale": 1, "y": 0}, {"opacity": 0, "scale": 0.94, "y": 60}, W100 + 0.2, t1 - W100 - 0.24, "power2.in")
    S.ft(f"#{s}-list", {"opacity": 1}, {"opacity": 0}, W100 + 0.18, 0.28, "power2.in")

    # ---------------------------------------------------------------- mascot: off-screen in this scene
    S.mset("V", {"vis": 0}, t0)
    for k in range(4):
        S.fx(ck0 + step * (5 * k + 2), "key", 0.035)
    S.fx(W97 + 0.02, "whoosh", 0.05)
    S.fx(W100 + 0.2, "sparkle", 0.05)
