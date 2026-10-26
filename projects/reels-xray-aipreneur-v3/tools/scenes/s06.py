"""S06 — CLAUDE CODE INPUT (13.78–16.72)  VO: "Kasih naskah dan referensi visual ke Claude Code."
A precision input machine. The script sheet slides in from the left on "Kasih/naskah", the visual reference
board from the right on "referensi"; both are scanned by a navy light bar, rollers pull them into the glass
slot, and on "Claude Code" the machine activates (LEDs, engraved label fills navy, slot glow, one burst).
End: the front panel splits open on a round stage (S07)."""
from xk import box, screw, shadow, apex, rivets_line, r3
from kit_b import backdrop, near_blur, code_lines, engrave, roller, spin_roller

SFX = [(13.9, "whoosh", 0.06), (15.82, "click", 0.13)]

MX, MY, MW, MH = 250, 782, 680, 440      # machine front panel


def build(S):
    s = S.id
    S.persp_origin = (590, 560)
    W29, W30, W32, W35 = S.W(29), S.W(30), S.W(32), S.W(35)     # Kasih 13.88, naskah 14.16, referensi 14.78, Claude 15.82
    end = S.t1
    backdrop(S, seed=6)
    # ------------------------------------------------ round stage behind the machine (revealed at the end)
    S.mid.append(f'<div class="abs" id="{s}-stage" style="{box(230, 900, 720, 300)}">'
                 f'<div class="abs" style="{box(0, 110, 720, 120)}border-radius:0 0 360px 360px / 0 0 60px 60px;background:linear-gradient(90deg,#3a6299,#294b77 45%,#1c3354)"></div>'
                 f'<div class="abs" style="{box(0, 0, 720, 170)}border-radius:50%;background:radial-gradient(ellipse at 40% 35%,#ffffff,#eef3fa 55%,#d3dff0);box-shadow:inset 0 -4px 8px rgba(172,198,231,.7)"></div>'
                 f'<div class="abs" style="{box(110, 26, 500, 118)}border-radius:50%;border:2px solid rgba(58,98,153,.35)"></div></div>')
    # ------------------------------------------------ machine: shadow, side face, top face with slot
    S.mid.append(shadow(200, 1170, 860, 110, 0.9))
    S.mid.append(f'<div class="abs navy-side" style="{box(MX + MW - 6, MY - 30, 40, MH + 6)}border-radius:0 18px 18px 0;transform-origin:0 0;transform:skewY(-38deg) translateY(30px)"></div>')
    top = (f'<div class="abs por-flat" style="{box(MX + 10, MY - 46, MW - 4, 56)}border-radius:20px 26px 0 0"></div>'
           f'<div class="abs" id="{s}-slot" style="{box(MX + 70, MY - 34, MW - 140, 30)}border-radius:15px;background:linear-gradient(180deg,#1c3354,#294b77 70%,#3a6299);box-shadow:inset 0 3px 6px rgba(0,0,0,.35),0 1px 0 #fff"></div>'
           f'<div class="abs" id="{s}-slotglow" style="{box(MX + 60, MY - 70, MW - 120, 90)}border-radius:50%;background:radial-gradient(ellipse,rgba(203,219,244,.95),rgba(203,219,244,0) 70%)"></div>')
    S.mid.append(top)
    # ------------------------------------------------ the two inputs (behind the front panel -> they disappear into the slot)
    sheet = (f'<div class="abs paper" id="{s}-sheet" style="{box(338, 452, 236, 300)}border-radius:10px">'
             f'<div class="abs" style="{box(22, 22, 120, 14)}border-radius:7px;background:#294b77"></div>'
             f'{code_lines(s + "-sc", 22, 56, 190, 9, seed=31, gap=24, h=7, ink_every=4)}'
             f'<div class="abs" style="{box(206, 0, 30, 30)}border-radius:0 10px 0 10px;background:linear-gradient(225deg,#e6edf8 50%,#cbdbf4 50%)"></div></div>')
    frames = "".join(f'<div class="abs" style="{box(22 + (k % 2) * 112, 50 + (k // 2) * 116, 100, 104)}border-radius:8px;background:{bg};box-shadow:0 4px 8px -4px rgba(28,51,84,.35)">'
                     f'<div class="abs" style="{box(14 + 30 * (k % 2), 18 + 20 * (k // 2), 34, 34)}border-radius:50%;background:{dot}"></div></div>'
                     for k, (bg, dot) in enumerate((("linear-gradient(150deg,#3a6299,#1c3354)", "#9fd8c4"), ("linear-gradient(160deg,#ffffff,#cbdbf4)", "#294b77"),
                                                    ("linear-gradient(160deg,#e8f0fb,#acc6e7)", "#ffffff"), ("linear-gradient(150deg,#294b77,#3a6299)", "#cbdbf4"))))
    board = (f'<div class="abs grid-paper" id="{s}-board" style="{box(600, 452, 254, 300)}border-radius:12px;box-shadow:0 0 0 3px #ffffff,0 0 0 4.5px #acc6e7,0 18px 26px -12px rgba(28,51,84,.35)">'
             f'<div class="abs" style="{box(22, 18, 70, 10)}border-radius:5px;background:#acc6e7"></div>{frames}'
             f'<div class="abs" style="{box(108, 288, 38, 22)}border-radius:6px;background:#e8f0fb;box-shadow:inset 0 0 0 1.5px #acc6e7"></div></div>')
    S.mid.append(sheet + board)
    # scan light bars (navy light)
    for nm, x, w in (("scA", 330, 252), ("scB", 592, 270)):
        S.mid.append(f'<div class="abs" id="{s}-{nm}" style="{box(x, 452, w, 16)}border-radius:8px;background:linear-gradient(180deg,rgba(58,98,153,0),rgba(58,98,153,.55) 50%,rgba(58,98,153,0));box-shadow:0 0 18px rgba(58,98,153,.45)"></div>')
    # ------------------------------------------------ front panel (two halves that open at the end)
    def half(nm, x, w, rad):
        return (f'<div class="abs por" id="{s}-{nm}" style="{box(x, MY, w, MH)}border-radius:{rad}">'
                f'{rivets_line(28 if nm == "fl" else 20, MH - 30, w - 20 if nm == "fl" else w - 28, MH - 30, 8)}'
                + "".join(f'<div class="abs" style="{box(30 if nm == "fl" else 20, 300 + k * 16, w - 50, 4)}border-radius:2px;background:rgba(172,198,231,.55)"></div>' for k in range(5))
                + (f'{screw(26, 26, 30, 12)}{screw(26, MH - 64, -15, 12)}' if nm == "fl" else f'{screw(w - 26, 26, 70, 12)}{screw(w - 26, MH - 64, 10, 12)}')
                + "</div>")
    S.mid.append(half("fl", MX, MW / 2, "26px 0 0 30px") + half("fr", MX + MW / 2, MW / 2, "0 26px 30px 0"))
    S.mid.append(f'<div class="abs" id="{s}-seam" style="{box(MX + MW / 2 - 1, MY + 8, 2, MH - 16)}background:rgba(41,75,119,.25)"></div>')
    # label plate + dial + meter + LEDs (one group that lifts away before the split)
    leds = "".join(f'<div class="led-off" style="left:{230 + k * 40}px;top:206px"></div><div class="led" id="{s}-led{k}" style="left:{230 + k * 40}px;top:206px"></div>' for k in range(5))
    dial = (f'<div class="abs por" id="{s}-dial" style="{box(34, 64, 92, 92)}border-radius:50%">'
            f'<div class="abs" style="{box(43, 8, 6, 30)}border-radius:3px;background:#294b77"></div></div>')
    meter = (f'<div class="abs glass" style="{box(MW - 150, 64, 110, 92)}border-radius:14px;overflow:hidden">'
             + "".join(f'<div class="abs" style="{box(14 + k * 9, 60 - (k % 3) * 4, 2, 12 + (k % 3) * 4)}background:#3a6299;opacity:.6"></div>' for k in range(10))
             + f'<div class="abs" id="{s}-needle" style="{box(53, 22, 4, 60)}border-radius:2px;background:#294b77"></div></div>')
    plate = (f'<div class="abs por-dim" style="{box(150, 66, MW - 310, 92)}border-radius:16px;box-shadow:inset 2px 2px 4px rgba(28,51,84,.18),inset -1px -1px 0 #fff">'
             f'{engrave(s + "-lab", "Claude Code", 0, 22, 40, w=MW - 310)}'
             f'<div class="abs" id="{s}-labon" style="left:0;top:22px;width:{MW - 310}px;text-align:center;white-space:nowrap;font:800 40px Montserrat;letter-spacing:.04em;color:#294b77;text-shadow:0 0 14px rgba(172,198,231,.9)">Claude Code</div></div>')
    S.mid.append(f'<div class="abs" id="{s}-ctrl" style="{box(MX, MY, MW, 260)}">{dial}{meter}{plate}{leds}</div>')
    # rollers in the slot (drawn last so the inputs vanish under them)
    S.mid.append(roller(f"{s}-r1", MX + 76, MY - 32, MW - 152, 12) + roller(f"{s}-r2", MX + 76, MY - 18, MW - 152, 12))
    near_blur(S, [(f"{s}-n1", 880, 520, 200, 200, "border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"),
                  (f"{s}-n2", -40, 1400, 280, 28, "border-radius:14px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px)")])
    apex(S, S.near, f"{s}-ap", 590, 880, W35, size=620, sparks=6, seed=8)

    # ================================================================ motion
    S.cam([(S.t0, {"z": 60, "rotationY": 5, "x": 0, "y": 0}, None),
           (W32, {"z": 0, "rotationY": 0}, "power2.out"),
           (W35 - 0.05, {"z": 10, "rotationY": -3}, "sine.inOut"),
           (W35 + 0.25, {"z": 70}, "power3.out"),
           (end, {"z": 200, "rotationY": 0, "y": -60}, "power2.in")])
    S.init(f"#{s}-stage", {"scale": 0.7, "opacity": 0, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-stage", {"scale": 0.7, "opacity": 0}, {"scale": 1, "opacity": 1}, end - 0.38, 0.36, "power3.out")
    # inputs: in -> hover -> scanned -> pulled down into the slot
    S.keys(f"#{s}-sheet", [(S.t0, {"x": -520, "rotation": -10, "y": 0}, None), (W29 - 0.05, {"x": -520}, "none"),
                           (W30 + 0.25, {"x": 0, "rotation": -3}, "expo.out"), (15.42, {"y": -6, "rotation": -2}, "sine.inOut"),
                           (W35 - 0.04, {"y": 330, "rotation": 0}, "power3.in")])
    S.keys(f"#{s}-board", [(S.t0, {"x": 520, "rotation": 10, "y": 0}, None), (W32 - 0.12, {"x": 520}, "none"),
                           (W32 + 0.3, {"x": 0, "rotation": 3}, "expo.out"), (15.48, {"y": -6, "rotation": 2}, "sine.inOut"),
                           (W35 - 0.02, {"y": 330, "rotation": 0}, "power3.in")])
    for nm, a in (("scA", 14.55), ("scB", 15.08)):
        S.init(f"#{s}-{nm}", {"y": 0, "opacity": 0})
        S.ft(f"#{s}-{nm}", {"y": 0, "opacity": 0}, {"y": 140, "opacity": 1}, a, 0.18, "power1.in")
        S.ft(f"#{s}-{nm}", {"y": 140, "opacity": 1}, {"y": 290, "opacity": 0}, a + 0.18, 0.2, "power1.out")
    spin_roller(S, f"#{s}-r1", 15.4, end, 260)
    spin_roller(S, f"#{s}-r2", 15.4, end, -260)
    # activation on "Claude Code"
    S.init(f"#{s}-lab", {"opacity": 0, "scale": 1.15})
    S.ft(f"#{s}-lab", {"opacity": 0, "scale": 1.15}, {"opacity": 1, "scale": 1}, W35 - 0.12, 0.16, "power3.out")
    for nm in ("sheet", "board"):
        S.ft(f"#{s}-{nm}", {"opacity": 1}, {"opacity": 0}, W35 + 0.02, 0.04, "none")
    S.init(f"#{s}-labon", {"opacity": 0})
    S.ft(f"#{s}-labon", {"opacity": 0}, {"opacity": 1}, W35 - 0.02, 0.25, "power2.out")
    for k in range(5):
        S.init(f"#{s}-led{k}", {"opacity": 0})
        S.ft(f"#{s}-led{k}", {"opacity": 0}, {"opacity": 1}, W35 + 0.04 * k, 0.1, "none")
    S.init(f"#{s}-slotglow", {"opacity": 0, "scale": 0.6})
    S.ft(f"#{s}-slotglow", {"opacity": 0, "scale": 0.6}, {"opacity": 1, "scale": 1.1}, W35 - 0.06, 0.2, "power2.out")
    S.ft(f"#{s}-slotglow", {"opacity": 1, "scale": 1.1}, {"opacity": 0.45, "scale": 1}, W35 + 0.2, 0.5, "power2.inOut")
    S.keys(f"#{s}-needle", [(S.t0, {"rotation": -50, "transformOrigin": "50% 100%"}, None), (W30, {"rotation": -20}, "power2.out"),
                            (W32 + 0.1, {"rotation": 5}, "power2.out"), (W35 + 0.1, {"rotation": 48}, "back.out(2.5)")])
    S.keys(f"#{s}-dial", [(S.t0, {"rotation": -40}, None), (W35 - 0.1, {"rotation": 10}, "sine.inOut"), (W35 + 0.2, {"rotation": 130}, "back.out(1.8)")])
    # open on the stage
    S.init(f"#{s}-ctrl", {"y": 0, "opacity": 1})
    S.ft(f"#{s}-ctrl", {"y": 0, "opacity": 1}, {"y": -40, "opacity": 0}, end - 0.42, 0.2, "power2.in")
    S.init(f"#{s}-seam", {"opacity": 1})
    S.ft(f"#{s}-seam", {"opacity": 1}, {"opacity": 0}, end - 0.3, 0.05, "none")
    for nm, dx in (("fl", -420), ("fr", 420)):
        S.init(f"#{s}-{nm}", {"x": 0, "rotationY": 0})
        S.ft(f"#{s}-{nm}", {"x": 0, "rotationY": 0}, {"x": dx, "rotationY": -35 if dx < 0 else 35}, end - 0.32, 0.32, "power3.in")
