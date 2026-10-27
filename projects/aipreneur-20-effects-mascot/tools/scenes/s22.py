"""S22 — THE SECRET IS CONTINUITY (35.73–39.93)
VO: "Tepi kertas berubah jadi rel kamera. Rel itu membawa kita ke scene berikutnya."
S21 ends on a cyan line across the frame; here it rises and becomes the track under three cards of our own results
(11 Paper Cutout, 12 Dolly Zoom, 13 Magazine Cover). "Tepi kertas": the first track segment turns into the cream paper
edge under the paper card. "berubah jadi rel kamera": the paper edge stretches right and splits into two satin rails
with sleepers under the dolly card. "Rel itu membawa kita ke scene berikutnya": a miniature camera dolly rides the
rail into the cover card, which then comes forward to the centre (hand-off: S23 opens with that card).
The mascot (full body, small, centred below the diagram) points the way and follows the dolly with his head."""
from xk import box, r3, CYAN
from kit import SELF

CW, CH = 264, 470
CY = 290
CX = [104, 408, 712]
TRACK_Y = 830
LABELS = ["11 · PAPER CUTOUT", "12 · DOLLY ZOOM", "13 · MAGAZINE COVER"]
IMGS = ["paper", "dolly", "cover"]
FINAL = (375, 300, 330, 587)        # cover card at the end (x, y, w, h) == S23 start


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W101, W103, W105, W106, W107, W109, W112, W113 = (S.W(i) for i in (101, 103, 105, 106, 107, 109, 112, 113))
    # ---------------------------------------------------------------- back: cards, track
    for k in range(3):
        x = CX[k]
        S.back.append(f'<div class="abs" id="{s}-c{k}" style="{box(x, CY, CW, CH)}">'
                      f'<div class="abs cshadow" style="{box(-20, CH - 30, CW + 40, 70)}"></div>'
                      f'<div class="abs" style="{box(0, 0, CW, CH)}border-radius:18px;overflow:hidden;box-shadow:0 0 0 2px rgba(255,255,255,.22),0 24px 40px -18px rgba(3,8,28,.8)">'
                      f'<img src="{SELF}/{IMGS[k]}.jpg" alt="" style="position:absolute;left:0;top:0;width:{CW}px;height:{CH}px" /></div>'
                      f'<div class="abs" id="{s}-c{k}hl" style="{box(-6, -6, CW + 12, CH + 12)}border-radius:22px;border:3px solid {CYAN};box-shadow:0 0 22px rgba(0,208,254,.55)"></div>'
                      f'<div class="abs" style="left:0;top:{CH + 14}px;width:{CW}px;font:700 22px/28px Poppins;color:#fff;text-align:center;letter-spacing:.04em">{LABELS[k]}</div></div>')
    # base track (cyan line from S21)
    S.back.append(f'<div class="abs glowline" id="{s}-line" style="{box(40, TRACK_Y, 1000, 4)}"></div>')
    # segment 1: paper edge (cream strip with thickness)
    S.back.append(f'<div class="abs" id="{s}-paper" style="{box(CX[0] - 10, TRACK_Y - 14, CW + 20, 30)}">'
                  f'<div class="abs" style="left:0;top:0;width:{CW + 20}px;height:24px;background:#fbf8f1;box-shadow:0 10px 16px -6px rgba(3,8,28,.7)"></div>'
                  f'<div class="abs" style="left:0;top:24px;width:{CW + 20}px;height:5px;background:#cbbfa9"></div>'
                  f'<div class="abs" id="{s}-pedge" style="left:0;top:-2px;width:{CW + 20}px;height:4px;background:{CYAN};box-shadow:0 0 12px rgba(0,208,254,.9)"></div></div>')
    # segment 2: rails + sleepers (start at the paper edge, run to the cover card)
    rx0, rx1 = CX[0] + 30, CX[2] + CW - 20
    S.back.append(f'<div class="abs" id="{s}-rails" style="{box(rx0, TRACK_Y - 16, rx1 - rx0, 34)}">'
                  + "".join(f'<div class="abs metal" id="{s}-sl{j}" style="left:{r3(j * (rx1 - rx0 - 14) / 15)}px;top:4px;width:14px;height:26px;border-radius:3px"></div>' for j in range(16))
                  + f'<div class="abs metal" id="{s}-rl0" style="left:0;top:6px;width:{rx1 - rx0}px;height:6px;border-radius:3px"></div>'
                  f'<div class="abs metal" id="{s}-rl1" style="left:0;top:22px;width:{rx1 - rx0}px;height:6px;border-radius:3px"></div></div>')
    # miniature camera dolly (cart + camera body + lens)
    S.back.append(f'<div class="abs" id="{s}-dolly" style="{box(rx0 - 20, TRACK_Y - 112, 120, 100)}">'
                  f'<div class="abs metal" style="left:4px;top:62px;width:112px;height:24px;border-radius:6px"></div>'
                  + "".join(f'<div class="abs" style="left:{x}px;top:78px;width:26px;height:26px;border-radius:13px;background:radial-gradient(circle at 40% 35%,#e9eef5,#5d6b80);box-shadow:0 2px 3px rgba(3,8,28,.6)"></div>' for x in (12, 82))
                  + f'<div class="abs por" style="left:26px;top:14px;width:70px;height:46px;border-radius:8px"></div>'
                  f'<div class="abs" style="left:86px;top:20px;width:34px;height:34px;border-radius:17px;background:radial-gradient(circle at 40% 40%,#7ee8ff 0%,#0b2a52 45%,#020814 100%);box-shadow:0 0 0 4px #9aa6b8"></div>'
                  f'<div class="abs" style="left:36px;top:2px;width:30px;height:12px;border-radius:4px;background:#2a4f82"></div></div>')

    # ---------------------------------------------------------------- motion
    # S21's line rises into the track; cards drop in
    S.init(f"#{s}-line", {"y": 1000 - TRACK_Y, "scaleX": 1.08, "opacity": 1})
    S.ft(f"#{s}-line", {"y": 1000 - TRACK_Y, "scaleX": 1.08}, {"y": 0, "scaleX": 1}, t0, 0.32, "power3.out")
    for k in range(3):
        S.init(f"#{s}-c{k}", {"y": -60, "opacity": 0, "rotation": (-3, 0, 3)[k]})
        S.ft(f"#{s}-c{k}", {"y": -60, "opacity": 0, "rotation": (-3, 0, 3)[k]}, {"y": 0, "opacity": 1, "rotation": 0}, t0 + 0.05 + k * 0.07, 0.34, "back.out(1.5)")
        S.init(f"#{s}-c{k}hl", {"opacity": 0})
    # "Tepi kertas": paper card lit, track segment becomes the paper edge
    S.ft(f"#{s}-c0hl", {"opacity": 0}, {"opacity": 1}, W101, 0.16, "power2.out")
    S.ft(f"#{s}-c0", {"scale": 1}, {"scale": 1.05}, W101, 0.3, "back.out(2)")
    S.init(f"#{s}-paper", {"scaleY": 0, "opacity": 1, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-paper", {"scaleY": 0}, {"scaleY": 1}, W101 + 0.04, 0.26, "back.out(2)")
    S.init(f"#{s}-pedge", {"opacity": 0})
    S.ft(f"#{s}-pedge", {"opacity": 0}, {"opacity": 1}, W101 + 0.25, 0.15, "power2.out")
    # "berubah jadi rel kamera": paper edge stretches right, thins, and becomes rails (+ sleepers)
    S.ft(f"#{s}-paper", {"scaleX": 1, "scaleY": 1, "x": 0, "transformOrigin": "0% 50%"}, {"scaleX": 2.6, "scaleY": 0.25, "x": 0}, W103, 0.42, "power3.inOut")
    S.ft(f"#{s}-paper", {"opacity": 1}, {"opacity": 0}, W105 - 0.05, 0.18, "power2.in")
    S.init(f"#{s}-rails", {"opacity": 0})
    S.ft(f"#{s}-rails", {"opacity": 0}, {"opacity": 1}, W105 - 0.12, 0.16, "power2.out")
    for j in range(2):
        S.init(f"#{s}-rl{j}", {"scaleX": 0, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-rl{j}", {"scaleX": 0}, {"scaleX": 1}, W105 - 0.1 + j * 0.05, 0.5, "power3.out")
    for j in range(16):
        S.init(f"#{s}-sl{j}", {"scaleY": 0})
        S.ft(f"#{s}-sl{j}", {"scaleY": 0}, {"scaleY": 1}, W105 + j * 0.025, 0.18, "back.out(2.5)")
    S.ft(f"#{s}-c0hl", {"opacity": 1}, {"opacity": 0}, W105, 0.2, "power2.in")
    S.ft(f"#{s}-c0", {"scale": 1.05}, {"scale": 1}, W105, 0.3, "power2.out")
    S.ft(f"#{s}-c1hl", {"opacity": 0}, {"opacity": 1}, W105 + 0.05, 0.16, "power2.out")
    S.ft(f"#{s}-c1", {"scale": 1}, {"scale": 1.05}, W105 + 0.05, 0.3, "back.out(2)")
    S.ft(f"#{s}-line", {"opacity": 1}, {"opacity": 0.25}, W105, 0.3, "power2.out")
    # "Rel itu membawa kita ke scene berikutnya": dolly rides the rail into the cover card
    S.init(f"#{s}-dolly", {"x": 0, "opacity": 0, "y": 12})
    S.ft(f"#{s}-dolly", {"x": 0, "opacity": 0, "y": 12}, {"x": 0, "opacity": 1, "y": 0}, W107 - 0.1, 0.22, "back.out(2)")
    travel = rx1 - rx0 - 90
    S.ft(f"#{s}-dolly", {"x": 0}, {"x": travel}, W109, W113 - W109 + 0.1, "power2.inOut")
    S.ft(f"#{s}-c1hl", {"opacity": 1}, {"opacity": 0}, S.W(110), 0.2, "power2.in")
    S.ft(f"#{s}-c1", {"scale": 1.05}, {"scale": 1}, S.W(110), 0.3, "power2.out")
    S.ft(f"#{s}-c2hl", {"opacity": 0}, {"opacity": 1}, W112, 0.16, "power2.out")
    # the cover card comes forward to the centre (hand-off), the rest clears
    fx, fy, fw, fh = FINAL
    go = W113 + 0.25
    S.ft(f"#{s}-c2", {"x": 0, "y": 0, "scale": 1, "transformOrigin": "0% 0%"},
         {"x": fx - CX[2], "y": fy - CY, "scale": fw / CW}, go, t1 - go, "power3.inOut")
    for sel in (f"#{s}-c0", f"#{s}-c1", f"#{s}-rails", f"#{s}-dolly", f"#{s}-line"):
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, go, 0.25, "power2.in")

    # ---------------------------------------------------------------- mascot: small, full body under the diagram, guiding
    v = {"fx": 540, "fy": 1760, "h": 800, "yaw": 0, "pitch": 6}
    S.mv([(t0, dict(v, yaw=-6), None), (W107, dict(v, yaw=8), "sine.inOut"), (t1, dict(v, yaw=4), "sine.inOut")])
    S.mx([(t0, {"y": 60, "opacity": 0}, None), (t0 + 0.35, {"y": 0, "opacity": 1}, "power3.out")])
    S.act("armR", [(t0, "low", 0.3), (W101 - 0.15, "pointUp", 0.3), (W103 + 0.2, "low", 0.4), (S.W(114) - 0.3, "low", 0.4)])
    S.act("armL", [(t0, "low", 0.3), (W105 - 0.15, "pointUp", 0.3), (W107 - 0.1, "point", 0.35), (W113 + 0.2, "present", 0.35)])
    S.act("head", [(t0, [-0.12, -0.28, 0.02], 0.3), (W103, [-0.14, -0.05, 0], 0.4), (W105, [-0.16, 0.12, 0], 0.35),
                   (W109, [-0.12, 0.05, 0], 0.4), (W112, [-0.14, 0.3, -0.03], 0.6), (W113 + 0.3, [-0.1, 0.05, 0.03], 0.4)])
    S.act("torso", [(t0, {"chest": [0, -0.06, 0]}, 0.4), (W105, {"chest": [0, 0.06, 0]}, 0.4), (W113, {"chest": [0.03, 0.1, 0]}, 0.4)])
    S.fx(W101 + 0.04, "pop", 0.06)
    S.fx(W105 - 0.05, "click", 0.07)
    S.fx(W109, "whoosh", 0.05)
    S.fx(W112 + 0.02, "ping", 0.05)
