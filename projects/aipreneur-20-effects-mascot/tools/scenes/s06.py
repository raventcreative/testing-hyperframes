"""S06 — 05 CHECKLIST POP (11.43–13.17)  VO: "Checklist muncul satu per satu."
Opens on S05's cyan disc at CHECK0. The camera re-frames to a 3/4 medium (mascot left, turned toward screen-right);
the disc is the first check: a smoked-glass pill grows out of it ("Checklist"), then the other three pop one by
one on the spoken beats ("muncul / satu / satu"): 01 Orbit, 02 Chat Takeover, 03 Frame Escape, 04 Snap Zoom - the
effects we just saw. White check strokes draw, a glint passes each pill, a cyan spine connects the discs.
The mascot points at them. Hand-off: the top pill stretches into the headline band STRIP_B (S07 opening state)."""
from xk import box, r3, CYAN, check_svg
from kit import CHECK0
from kit_b import CHECK_VIEW, CHECK_END, STRIP_B

LABELS = ["Orbit", "Chat Takeover", "Frame Escape", "Snap Zoom"]
PX, PW, PH, GAP = 652, 380, 80, 92


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W30, W31, W32, W34 = S.W(30), S.W(31), S.W(32), S.W(34)   # Checklist 11.52, muncul 11.94, satu 12.28, satu. 12.60
    cx0, cy0, d = CHECK0
    rows = [cy0 + k * GAP for k in range(4)]
    pops = [W30 + 0.04, W31 + 0.03, W32 + 0.02, W34 + 0.02]
    # ---------------------------------------------------------------- back: the headline band (hidden until the hand-off)
    sx, sy, sw, sh = STRIP_B
    S.back.append(f'<div class="abs" id="{s}-strip" style="{box(sx, sy, sw, sh)}">'
                  f'<div class="abs smoked" style="left:0;top:0;width:{sw}px;height:{sh}px;border-radius:6px;border-left:0;border-right:0;'
                  f'border-top:3px solid {CYAN};border-bottom:3px solid {CYAN}"></div></div>')
    # ---------------------------------------------------------------- front: spine + pills
    S.front.append(f'<div class="abs glowline" id="{s}-spine" style="{box(cx0 - 2, rows[0], 4, rows[3] - rows[0])}background:linear-gradient(180deg,#9ff0ff,{CYAN});"></div>')
    for k, cy in enumerate(rows):
        dx = cx0 - d / 2 - PX
        S.front.append(
            f'<div class="abs" id="{s}-p{k}" style="{box(PX, cy - PH / 2, PW, PH)}">'
            f'<div class="abs smoked pill" id="{s}-pb{k}" style="left:0;top:0;width:{PW}px;height:{PH}px;overflow:hidden">'
            f'<div class="abs" id="{s}-gl{k}" style="left:-140px;top:-20px;width:90px;height:{PH + 40}px;transform:skewX(-22deg);'
            f'background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.35),rgba(255,255,255,0))"></div>'
            f'<div class="abs" id="{s}-tx{k}" style="left:{dx + d + 18}px;top:0;width:{PW - dx - d - 24}px;height:{PH}px;font:700 30px/{PH}px Poppins, sans-serif;color:#fff;white-space:nowrap">'
            f'<span style="color:{CYAN};font-weight:700;margin-right:10px">{k + 1:02d}</span>{LABELS[k]}</div></div>'
            f'<div class="abs" id="{s}-d{k}" style="left:{dx}px;top:{(PH - d) / 2}px;width:{d}px;height:{d}px;border-radius:50%;background:{CYAN};'
            f'box-shadow:inset 0 2px 0 rgba(255,255,255,.6), inset 0 -3px 6px rgba(0,90,140,.45), 0 6px 14px rgba(3,8,28,.55)">'
            f'<div class="abs" style="left:14px;top:14px;width:36px;height:36px">{check_svg(f"{s}-ck{k}", color="#fff", width=3.6)}</div></div></div>')

    # ---------------------------------------------------------------- motion
    S.init(f"#{s}-spine", {"scaleY": 0, "transformOrigin": "50% 0%", "opacity": 0.85})
    for k in range(1, 4):
        S.ft(f"#{s}-spine", {"scaleY": (k - 1) / 3}, {"scaleY": k / 3}, pops[k] - 0.1, 0.16, "power2.out")
    for k, at in enumerate(pops):
        org = f"{cx0 - PX}px {PH / 2}px"
        if k == 0:
            S.init(f"#{s}-d0", {"scale": 1})
        else:
            S.init(f"#{s}-d{k}", {"scale": 0})
            S.ft(f"#{s}-d{k}", {"scale": 0}, {"scale": 1}, at - 0.03, 0.26, "back.out(2.6)")
        S.init(f"#{s}-pb{k}", {"scaleX": d / PW, "opacity": 0, "transformOrigin": org})
        S.ft(f"#{s}-pb{k}", {"scaleX": d / PW, "opacity": 0}, {"scaleX": 1, "opacity": 1}, at, 0.3, "back.out(1.5)")
        S.init(f"#{s}-tx{k}", {"opacity": 0, "x": -24})
        S.ft(f"#{s}-tx{k}", {"opacity": 0, "x": -24}, {"opacity": 1, "x": 0}, at + 0.1, 0.22, "power3.out")
        S.init(f"#{s}-ck{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-ck{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, at + 0.12, 0.22, "power2.out")
        S.init(f"#{s}-gl{k}", {"x": 0})
        S.ft(f"#{s}-gl{k}", {"x": 0}, {"x": PW + 240}, at + 0.22, 0.4, "power2.inOut")
        S.init(f"#{s}-p{k}", {"y": 0})
        S.ft(f"#{s}-p{k}", {"y": 10}, {"y": 0}, at, 0.3, "back.out(2)")
    # hand-off: the top pill stretches into the headline band above the head
    ho = t1 - 0.24
    pcx, pcy = PX + PW / 2, rows[0]
    scx, scy = sx + sw / 2, sy + sh / 2
    S.init(f"#{s}-strip", {"opacity": 0, "x": pcx - scx, "y": pcy - scy, "scaleX": PW / sw, "scaleY": PH / sh})
    S.tset(f"#{s}-strip", {"opacity": 1}, ho)
    S.ft(f"#{s}-strip", {"x": pcx - scx, "y": pcy - scy, "scaleX": PW / sw, "scaleY": PH / sh}, {"x": 0, "y": 0, "scaleX": 1, "scaleY": 1}, ho, 0.22, "power3.inOut")
    S.tset(f"#{s}-p0", {"opacity": 0}, ho + 0.02)
    for k in range(1, 4):
        S.ft(f"#{s}-p{k}", {"opacity": 1}, {"opacity": 0.55}, ho, 0.2, "power1.out")
    S.ft(f"#{s}-spine", {"opacity": 0.85}, {"opacity": 0}, ho, 0.16, "power1.out")

    # ---------------------------------------------------------------- mascot: 3/4, eye line on the list
    S.mv([(t0, dict(CHECK_VIEW), None), (t1, dict(CHECK_END), "sine.inOut")])
    S.act("head", [(t0 + 0.02, [0.02, 0.26, 0.04], 0.25), (pops[1], [0.06, 0.3, 0.02], 0.25), (pops[2], [0.1, 0.3, 0], 0.25),
                   (pops[3], [0.14, 0.32, -0.02], 0.25), (ho, [-0.06, 0.24, 0.05], 0.25)])
    S.act("armL", [(t0 + 0.02, "low", 0.25), (W30 - 0.06, "point", 0.28), (pops[2] - 0.08, "present", 0.3), (pops[3] - 0.06, "point", 0.25), (ho, "pointUp", 0.25)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W31, "explain", 0.35), (W34 + 0.1, "low", 0.4)])
    S.act("torso", [(t0 + 0.02, {"chest": [0.03, 0.1, 0]}, 0.3), (ho, {"chest": [-0.02, 0.12, 0]}, 0.3)])
    S.act("root", [(t0 + 0.02, {"y": 0, "ry": 0.12, "rz": 0}, 0.3)])
    for at in pops[1:]:
        S.fx(at, "pop", 0.05)
    S.fx(pops[0] + 0.12, "click", 0.05)
    S.fx(ho, "whoosh", 0.05)
