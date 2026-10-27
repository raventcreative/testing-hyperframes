"""S25 — CTA: KOMEN EDIT (46.27–51.40)
VO: "Mau daftar dua puluh efek, breakdown scene, dan prompt yang bisa lo pakai? Komen EDIT. Gue kirim."
Opens on S24's card stack at the centre; the stack unfolds into three deliverable chips on their words (Daftar 20 efek,
Breakdown scene, Prompt). Camera pans to the mascot centre. "Komen": the chips lift away and a smoked-glass comment card
lands; "EDIT" pops in cyan Bold - HERO APEX. "Gue kirim.": a small send arrow leaves the card. The last ~0.5 s is a
calm, complete brand frame (logo final sheen runs in the root), no fade to black."""
from xk import box, r3, CYAN, apex, check_svg
from kit import SELF

STACK = (465, 300, 150, 267)
CHIPS = [("Daftar <span style='color:#00D0FE'>20</span> efek", 134), ("Breakdown scene", 138), ("Prompt", 141)]
CHIP_W = [430, 420, 280]
CHIP_Y = [300, 400, 500]
CARD = (90, 300, 900, 360)


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W146, W147, W148 = S.W(146), S.W(147), S.W(148)
    stx, sty, stw, sth = STACK
    # ---------------------------------------------------------------- back: the stack (from S24)
    for k, n in enumerate(["orbit", "paper", "cover", "city", "phone"]):
        S.back.append(f'<div class="abs" id="{s}-st{k}" style="{box(stx, sty, stw, sth)}border-radius:14px;overflow:hidden;box-shadow:0 0 0 2px rgba(255,255,255,.25),0 18px 30px -14px rgba(3,8,28,.85)">'
                      f'<img src="{SELF}/{n}.jpg" alt="" style="position:absolute;left:0;top:0;width:{stw}px;height:{sth}px" /></div>')
    # ---------------------------------------------------------------- front: chips, comment card
    for k, (label, wi) in enumerate(CHIPS):
        w = CHIP_W[k]
        S.front.append(f'<div class="abs pill acrylic" id="{s}-ch{k}" style="{box(540 - w / 2, CHIP_Y[k], w, 80)}">'
                       f'<div class="abs" style="left:14px;top:14px;width:52px;height:52px;border-radius:26px;background:rgba(3,10,30,.55)">'
                       f'<div class="abs" style="left:9px;top:9px;width:34px;height:34px">{check_svg(f"{s}-cc{k}", CYAN, 3.6)}</div></div>'
                       f'<div class="abs" style="left:80px;top:0;width:{w - 96}px;font:700 34px/80px Poppins;color:#fff;white-space:nowrap;text-align:center">{label}</div></div>')
    cx, cy, cw, chh = CARD
    S.front.append(f'<div class="abs smoked" id="{s}-card" style="{box(cx, cy, cw, chh)}border-radius:40px">'
                   f'<div class="abs" style="left:40px;top:40px;width:76px;height:76px;border-radius:38px;background:linear-gradient(150deg,#4a74ab,#183563);box-shadow:inset 0 0 0 3px rgba(0,208,254,.8)"></div>'
                   f'<div class="abs" style="left:138px;top:44px;width:300px;height:16px;border-radius:8px;background:rgba(255,255,255,.28)"></div>'
                   f'<div class="abs" style="left:138px;top:78px;width:200px;height:14px;border-radius:7px;background:rgba(255,255,255,.16)"></div>'
                   f'<div class="abs" id="{s}-komen" style="left:40px;top:150px;width:300px;font:700 64px/1 Poppins;color:#fff">Komen</div>'
                   f'<div class="abs" id="{s}-edit" style="left:300px;top:112px;width:560px;font:700 190px/1 Poppins;color:{CYAN};letter-spacing:-0.02em;'
                   f'text-shadow:0 0 30px rgba(0,208,254,.45), 0 6px 20px rgba(3,8,28,.6)">EDIT</div>'
                   f'<div class="abs" id="{s}-send" style="left:{cw - 130}px;top:40px;width:80px;height:80px;border-radius:40px;background:{CYAN}">'
                   f'<svg viewBox="0 0 48 48" style="position:absolute;left:16px;top:16px;width:48px;height:48px"><path d="M6 24 L42 8 L32 42 L24 28 Z" fill="#0b1636"/><path d="M24 28 L42 8" stroke="{CYAN}" stroke-width="2.5"/></svg></div></div>')
    apex(S, S.front, f"{s}-ap", 640, 420, W147 + 0.06, size=760, sparks=10, seed=2501, op=0.55)

    # ---------------------------------------------------------------- motion
    # stack unfolds into the chips (cards fan out, fade behind the chips)
    for k in range(5):
        a = {"x": 0, "y": 0, "rotation": (-6, -3, 0, 3, 6)[k], "opacity": 1, "scale": 1}
        S.init(f"#{s}-st{k}", a)
        S.ft(f"#{s}-st{k}", dict(a), {"x": (k - 2) * 170, "y": 40, "rotation": (k - 2) * 9, "opacity": 0, "scale": 0.8}, t0 + 0.05 + k * 0.03, 0.45, "power3.inOut")
    for k, (label, wi) in enumerate(CHIPS):
        b = S.W(wi) - 0.06
        S.init(f"#{s}-ch{k}", {"opacity": 0, "scale": 0.6, "y": 30})
        S.ft(f"#{s}-ch{k}", {"opacity": 0, "scale": 0.6, "y": 30}, {"opacity": 1, "scale": 1, "y": 0}, b, 0.34, "back.out(2)")
        S.init(f"#{s}-cc{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-cc{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, b + 0.25, 0.24, "power2.out")
        S.fx(b + 0.02, "pop", 0.06)
        S.ft(f"#{s}-ch{k}", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -80}, W146 - 0.16 + k * 0.03, 0.22, "power2.in")
    # comment card lands, EDIT pops (apex), send arrow
    S.init(f"#{s}-card", {"opacity": 0, "y": 70, "scale": 0.92})
    S.ft(f"#{s}-card", {"opacity": 0, "y": 70, "scale": 0.92}, {"opacity": 1, "y": 0, "scale": 1}, W146 - 0.04, 0.36, "power3.out")
    S.init(f"#{s}-komen", {"opacity": 0, "x": -30})
    S.ft(f"#{s}-komen", {"opacity": 0, "x": -30}, {"opacity": 1, "x": 0}, W146 + 0.02, 0.28, "power3.out")
    S.init(f"#{s}-edit", {"opacity": 0, "scale": 0.55, "transformOrigin": "30% 60%"})
    S.ft(f"#{s}-edit", {"opacity": 0, "scale": 0.55}, {"opacity": 1, "scale": 1}, W147 - 0.04, 0.4, "back.out(2.4)")
    S.init(f"#{s}-send", {"scale": 0, "rotation": -30, "x": 0})
    S.ft(f"#{s}-send", {"scale": 0, "rotation": -30, "x": 0}, {"scale": 1, "rotation": 0, "x": 0}, W148 - 0.05, 0.3, "back.out(2.4)")
    S.ft(f"#{s}-send", {"x": 0}, {"x": 16}, W148 + 0.3, 0.25, "power2.out")
    S.fx(W146 - 0.02, "whoosh", 0.05)
    S.fx(W147 + 0.02, "sparkle", 0.07)
    S.fx(W148 + 0.02, "click", 0.05)

    # ---------------------------------------------------------------- mascot: pans to centre, points at the card, then at you
    v0 = {"fx": 300, "fy": 1850, "h": 1000, "yaw": 14, "pitch": 5}
    v1 = {"fx": 540, "fy": 1900, "h": 1120, "yaw": 0, "pitch": 5}
    S.mv([(t0, v0, None), (t0 + 0.6, v1, "power3.inOut"), (W146, dict(v1, yaw=-4), "sine.inOut"), (t1 - 0.6, dict(v1, yaw=0), "sine.inOut"), (t1, dict(v1, yaw=0), "none")])
    S.act("armL", [(t0, "low", 0.3), (S.W(134) - 0.12, "explain", 0.3), (S.W(138) - 0.12, "palmUp", 0.3), (S.W(141) - 0.12, "explainHi", 0.3),
                   (S.W(145), "low", 0.35), (W146 - 0.14, "pointUp", 0.3), (W148, "present", 0.35), (50.85, "low", 0.4)])
    S.act("armR", [(t0, "low", 0.3), (S.W(136), "open", 0.3), (S.W(139) + 0.1, "low", 0.35), (S.W(145) - 0.1, "shrug", 0.3), (W146, "low", 0.35),
                   (W148 - 0.05, "wave", 0.3), (50.8, "low", 0.4)])
    S.act("head", [(t0, [-0.04, 0.1, 0], 0.4), (S.W(134), [0.04, -0.06, 0.03], 0.3), (S.W(138), [0, 0.08, -0.03], 0.3), (S.W(141), [0.05, 0, 0.02], 0.3),
                   (S.W(145), [-0.08, 0.02, 0.08], 0.3), (W146, [-0.12, 0.14, 0], 0.3), (W147, [0.06, 0.02, 0], 0.22), (W148, [-0.02, 0, 0.04], 0.35), (50.85, [0, 0, 0], 0.4)])
    S.act("torso", [(t0, {}, 0.4), (W147 - 0.05, {"chest": [0.06, 0, 0]}, 0.25), (W148, {}, 0.4)])
