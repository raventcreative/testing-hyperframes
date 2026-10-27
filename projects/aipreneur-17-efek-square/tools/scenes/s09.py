"""S09 — ZOOM CUT (efek #9).
Shot A: big word KONTEN centre (behind the mascot). The camera zooms THROUGH the counter of the "O" 16x in 0.25 s,
a 0.06 s white flash hides the cut, shot B (new set, new framing) lands 1.25 -> 1 in 0.3 s and holds."""
from xk import box, r3
from kit import MED, card_img

WORD = "KONTEN"
O = (345, 352)          # centre of the "O" counter (measured on the snapshot)
A_VIEW = {"fx": 740, "fy": 1250, "h": 900, "yaw": -10, "pitch": 5}
B_VIEW = dict(MED, fx=690, fy=1190, yaw=-14)


def zoom_props(s, p=O):
    return {"scale": s, "x": r3((p[0] - 540) * (1 - s)), "y": r3((p[1] - 540) * (1 - s))}


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    tz = t0 + 1.1           # zoom starts
    tc = tz + 0.25          # cut (under full white)
    # ---------------------------------------------------------------- shot A (back): word + soft floor ring
    S.back.append(f'<div class="abs" id="{s}-A" style="left:0;top:0;width:1080px;height:1080px">'
                  f'<div class="abs" style="{box(140, 760, 800, 220)}border-radius:50%;background:radial-gradient(ellipse,rgba(41,75,119,.16),rgba(41,75,119,0) 70%)"></div>'
                  f'<div class="abs" id="{s}-word" style="left:0;top:250px;width:1080px;text-align:center;white-space:nowrap">'
                  f'<span class="tx" style="font:700 205px/1 Poppins, sans-serif;letter-spacing:-0.01em">{WORD}</span></div>'
                  f'<div class="abs" style="{box(120, 488, 840, 6)}border-radius:3px;background:linear-gradient(90deg,rgba(41,75,119,0),rgba(41,75,119,.35),rgba(41,75,119,0))"></div>'
                  '</div>')
    # ---------------------------------------------------------------- shot B (back): new set — navy halo + thumbnail stack
    S.back.append(f'<div class="abs" id="{s}-B" style="left:0;top:0;width:1080px;height:1080px">'
                  f'<div class="abs" style="left:0;top:0;width:1080px;height:1080px;background:linear-gradient(160deg,#e6eefa 0%,#d3e0f2 100%)"></div>'
                  f'<div class="abs grid-fine" style="left:0;top:0;width:1080px;height:1080px;opacity:.7"></div>'
                  f'<div class="abs" style="{box(330, 90, 720, 720)}border-radius:50%;background:radial-gradient(circle,#294B77 0%,#1c3561 42%,rgba(28,53,97,0) 70%);opacity:.9"></div>'
                  f'<div class="abs" style="{box(390, 150, 600, 600)}border-radius:50%;border:3px solid rgba(255,255,255,.55)"></div>'
                  + card_img(f"{s}-c0", 70, 150, 230, 409, 3, style="transform:rotate(-7deg)")
                  + card_img(f"{s}-c1", 150, 520, 230, 409, 5, style="transform:rotate(5deg)")
                  + '</div>')
    # ---------------------------------------------------------------- flash (front, full frame)
    S.front.append(f'<div class="abs" id="{s}-flash" style="left:0;top:0;width:1080px;height:1080px;background:#ffffff"></div>')

    # ---------------------------------------------------------------- motion
    # A: slow push toward the O, then the 16x zoom through it (accelerating)
    S.cam([(t0, {"scale": 1, "x": 0, "y": 0}, None), (tz, zoom_props(1.06), "sine.inOut"), (tc, zoom_props(16), "power3.in")])
    S.tset(f"#{s}-cam", {"scale": 1, "x": 0, "y": 0}, tc + 0.004)
    S.init(f"#{s}-A", {"opacity": 1})
    S.tset(f"#{s}-A", {"opacity": 0}, tc + 0.004)
    S.init(f"#{s}-B", {"opacity": 0, "scale": 1.25, "transformOrigin": "540px 540px"})
    S.tset(f"#{s}-B", {"opacity": 1}, tc + 0.004)
    S.ft(f"#{s}-B", {"scale": 1.25}, {"scale": 1}, tc + 0.004, 0.3, "power3.out")
    for k, rot in ((0, -7), (1, 5)):
        S.init(f"#{s}-c{k}", {"rotation": rot, "y": 0})
        S.ft(f"#{s}-c{k}", {"y": 0}, {"y": -14 if k == 0 else 12}, tc + 0.35, t1 - tc - 0.36, "sine.inOut")
    S.init(f"#{s}-flash", {"opacity": 0})
    S.ft(f"#{s}-flash", {"opacity": 0}, {"opacity": 1}, tc - 0.04, 0.04, "power1.in")
    S.ft(f"#{s}-flash", {"opacity": 1}, {"opacity": 0}, tc + 0.06, 0.12, "power2.out")

    # ---------------------------------------------------------------- mascot
    def big(v, k):     # the same view seen through a k x zoom about the frame centre
        return dict(v, fx=540 + k * (v["fx"] - 540), fy=540 + k * (v["fy"] - 540), h=v["h"] * k)
    S.mv([(t0, A_VIEW, None), (tc, A_VIEW, "none"), (tc + 0.004, big(B_VIEW, 1.25), "none"), (tc + 0.304, B_VIEW, "power3.out"),
          (t1, dict(B_VIEW, yaw=-8), "sine.inOut")])
    S.mx([(t0, {"scale": 1, "x": 0, "y": 0}, None), (tz, zoom_props(1.06), "sine.inOut"), (tc, zoom_props(16), "power3.in"),
          (tc + 0.004, {"scale": 1, "x": 0, "y": 0}, "none")])
    S.act("armR", [(t0, "present", 0.01), (tz - 0.3, "pointUp", 0.25), (tc + 0.05, "open", 0.3), (tc + 1.6, "explain", 0.35), (t1 - 0.6, "low", 0.4)])
    S.act("armL", [(t0, "low", 0.01), (tc + 0.05, "wave", 0.3), (tc + 1.4, "low", 0.45)])
    S.act("head", [(t0, [-0.08, -0.22, 0.02], 0.01), (tz - 0.3, [-0.14, -0.3, 0.04], 0.3), (tc + 0.05, [0.0, -0.12, -0.03], 0.3),
                   (tc + 1.5, [-0.04, -0.2, 0.03], 0.4), (t1 - 0.5, [0, -0.1, 0], 0.4)])
    S.act("torso", [(t0, {"chest": [0.02, -0.1, 0]}, 0.01), (tc + 0.05, {"chest": [0.03, -0.06, 0]}, 0.3)])
