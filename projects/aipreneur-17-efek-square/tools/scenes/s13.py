"""S13 — PAPER CUT (effect #13).
The mascot becomes a paper cut-out: 14px white paper border + thin shadow (SVG f-paper), on cream paper with pen
scribbles, one navy colour block behind him with masking tape, and four ransom-note letters C-U-A-N slapped on top.
Everything wobbles ~1 deg every 0.1 s (stop motion, deterministic sequence)."""
from xk import box, r3, Rng

LET = [  # char, x, y, w, h, rot, bg, color, font
    ("C", 92, 812, 132, 158, -7, "linear-gradient(135deg,#0A0D2C,#294B77)", "#fff", "700 128px/158px 'Liberation Serif', serif"),
    ("U", 238, 842, 124, 138, 5, "#ffffff", "#0A0D2C", "700 112px/138px Poppins, sans-serif"),
    ("A", 806, 806, 134, 150, -4, "#cfe0f5", "#0A0D2C", "italic 700 124px/150px 'DejaVu Serif', serif"),
    ("N", 934, 850, 108, 128, 8, "#111827", "#fff", "700 104px/128px 'DejaVu Sans Mono', monospace"),
]


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    # ---------------------------------------------------------------- back: paper, scribbles, colour block, tape
    S.back.append(f'<div class="abs" id="{s}-paper" style="left:-30px;top:-30px;width:1140px;height:1140px;'
                  f'background:radial-gradient(ellipse at 30% 25%, #fbf6ea 0%, #f3ead6 55%, #e9dcc0 100%)">'
                  f'<div class="abs" style="inset:0;background:url(assets/brand/grain_256.png);opacity:.55;mix-blend-mode:multiply"></div></div>')
    S.back.append(f'<div class="abs" id="{s}-blk" style="{box(250, 190, 590, 700)}border-radius:6px;background:linear-gradient(150deg,#294B77 0%,#1c3561 55%,#0A0D2C 100%);'
                  f'box-shadow:6px 12px 0 rgba(10,13,44,.12), 0 22px 40px -20px rgba(10,13,44,.5);transform:rotate(-4deg)">'
                  f'<div class="abs" style="inset:0;background:url(assets/brand/grain_256.png);opacity:.25;mix-blend-mode:overlay"></div></div>')
    tape = "background:rgba(236,224,190,.86);box-shadow:0 2px 4px rgba(10,13,44,.15)"
    S.back.append(f'<div class="abs" id="{s}-tp0" style="{box(212, 168, 150, 46)}{tape};transform:rotate(-38deg)"></div>')
    S.back.append(f'<div class="abs" id="{s}-tp1" style="{box(744, 150, 150, 46)}{tape};transform:rotate(31deg)"></div>')
    pen = 'fill="none" stroke="#1c3561" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"'
    S.back.append(f'<svg class="abs" id="{s}-scr" style="left:0;top:0;width:1080px;height:1080px;overflow:visible" viewBox="0 0 1080 1080">'
                  # spiral top-left
                  f'<path {pen} d="M120 150 C 150 120, 190 150, 170 180 C 150 210, 100 195, 100 160 C 100 115, 160 90, 200 115 C 240 140, 230 205, 190 225"/>'
                  # stars top-right
                  f'<path {pen} d="M930 120 L944 158 L984 160 L952 184 L964 222 L930 200 L896 222 L908 184 L876 160 L916 158 Z"/>'
                  f'<path {pen} d="M1000 270 l8 20 l20 2 l-16 12 l6 20 l-18 -12 l-18 12 l6 -20 l-16 -12 l20 -2 Z" stroke-width="4"/>'
                  # zig-zag left margin
                  f'<path {pen} d="M70 420 l40 30 l-40 30 l40 30 l-40 30 l40 30"/>'
                  # underline scribble bottom
                  f'<path {pen} d="M380 1010 C 450 990, 520 1030, 600 1004 C 660 986, 720 1024, 790 1000"/>'
                  f'</svg>')
    # pen arrow that draws in (front of the paper, behind the mascot)
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1080px;overflow:visible" viewBox="0 0 1080 1080">'
                  f'<path id="{s}-arw" {pen} pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" d="M960 470 C 990 560, 960 640, 880 680 M 880 680 l 36 -4 M 880 680 l 14 -32"/></svg>')
    # ---------------------------------------------------------------- front: ransom-note letters (on top)
    for k, (ch, x, y, w, h, rot, bg, col, font) in enumerate(LET):
        S.front.append(f'<div class="abs" id="{s}-l{k}" style="{box(x - w / 2 + 40, y, w, h)}background:{bg};color:{col};font:{font};text-align:center;'
                       f'box-shadow:3px 6px 0 rgba(10,13,44,.18), 0 12px 18px -8px rgba(10,13,44,.45);transform:rotate({rot}deg)">{ch}</div>')

    # ---------------------------------------------------------------- motion: letters slap in (stepped), arrow draws in
    for k in range(4):
        S.init(f"#{s}-l{k}", {"opacity": 0, "scale": 1.5})
        b = t0 + 0.35 + k * 0.25
        S.tset(f"#{s}-l{k}", {"opacity": 1}, b)
        S.ft(f"#{s}-l{k}", {"scale": 1.5}, {"scale": 1}, b, 0.2, "steps(2)")
    S.init(f"#{s}-arw", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-arw", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, t0 + 1.5, 0.6, "steps(6)")
    # stop-motion wobble: new pose every 0.1 s (about +-1 deg, +-2 px), one seeded sequence per piece
    pieces = [(f"#{s}-blk", 11, -4, 1.0), (f"#{s}-scr", 23, 0, 0.8), (f"#{s}-tp0", 31, -38, 1.0), (f"#{s}-tp1", 37, 31, 1.0)] + \
             [(f"#{s}-l{k}", 41 + k * 7, LET[k][5], 1.2) for k in range(4)]
    n = int(round((t1 - t0) / 0.1))
    for sel, seed, base, amp in pieces:
        R = Rng(seed)
        for i in range(n):
            S.tset(sel, {"rotation": r3(base + R.u(-amp, amp)), "x": r3(R.u(-2, 2)), "y": r3(R.u(-2, 2))}, t0 + i * 0.1)
    R = Rng(5)
    for i in range(n):
        S.mset("#m-xf", {"rotation": r3(R.u(-1, 1)), "x": r3(R.u(-2, 2)), "y": r3(R.u(-2, 2))}, t0 + i * 0.1)
    S.mset("#m-xf", {"filter": "url(#f-paper)"}, t0)

    # ---------------------------------------------------------------- mascot: paper cut-out in the colour block
    v = {"fx": 548, "fy": 1205, "h": 1010, "yaw": 0, "pitch": 5}
    S.mv([(t0, dict(v, yaw=-6), None), (t1, dict(v, yaw=6), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.6, "wave", 0.35), (t0 + 1.9, "point", 0.35), (t0 + 3.4, "palmUp", 0.35)])
    S.act("armR", [(t0, "low", 0.3), (t0 + 1.0, "open", 0.35), (t0 + 2.6, "fist", 0.35), (t0 + 3.6, "low", 0.4)])
    S.act("head", [(t0, [0, 0, 0], 0.3), (t0 + 0.6, [-0.04, 0.1, 0.06], 0.3), (t0 + 1.9, [-0.06, 0.24, 0.02], 0.35),
                   (t0 + 3.2, [-0.02, -0.08, -0.05], 0.4)])
