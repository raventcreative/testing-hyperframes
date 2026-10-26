"""S14 — THE COST EXPLANATION (37.88–41.60)
VO: "Render lokal HyperFrames nggak pakai kredit generator video per detik."
Hero: the local render machine (HyperFrames plate) whose wheel keeps turning and drops finished frames into a tray.
Secondary (upper-left, smaller): a per-second credit meter fed by a film strip. On "nggak" the strip slows and stops;
on "kredit" the needle drops to rest and the meter dims, while a mint check confirms the local machine.
No money figures, no "free" claim. Ends with chains lowering onto the tray: the tray becomes S15's scale pan."""
from xk import box, screw, screws_rect, shadow, apex, gear_svg, rivets_line, r3
from kit_d import dial, frame_card, chain_rod, vent_lines

SFX = [(39.74, "click", 0.1), (41.2, "whoosh", 0.06)]

LX, LY, LW, LH = 520, 600, 440, 560      # local render machine
TX, TY = 700, 1250                        # tray (top-left of the dish)


def build(S):
    s = S.id
    S.persp_origin = (650, 540)
    W = S.W
    wR, wHF, wNg, wKr, wDet = W(81), W(83), W(84), W(86), W(90)

    # ---------------------------------------------------------------- far: backdrop
    far = [f'<div class="abs por-dim" style="{box(470, 430, 620, 1050)}border-radius:310px 310px 40px 40px;opacity:.5"></div>',
           f'<div class="abs" style="{box(510, 470, 540, 980)}border-radius:270px 270px 30px 30px;border:2px solid rgba(255,255,255,.85)"></div>',
           f'<div class="abs por-dim" style="{box(40, 380, 460, 560)}border-radius:230px 230px 30px 30px;opacity:.4"></div>',
           f'<div class="abs" style="{box(-100, 1470, 1300, 7)}border-radius:4px;background:rgba(172,198,231,.55)"></div>',
           f'<div class="abs" style="{box(-100, 1494, 1300, 3)}background:rgba(172,198,231,.35)"></div>',
           f'<div class="abs" style="{box(400, 520, 760, 760)}border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95),rgba(255,255,255,0) 62%)"></div>']
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">{"".join(far)}</div>')

    # ---------------------------------------------------------------- credit meter (secondary, upper-left)
    cm = []
    # film strip feeding the meter (behind the housing)
    cells = []
    for k in range(18):
        cells.append(f'<div class="abs" style="{box(14 + k * 64, 12, 50, 34)}border-radius:4px;background:linear-gradient(150deg,#e8f0fb,#acc6e7)"></div>')
        cells.append(f'<div class="abs" style="{box(30 + k * 64, 3, 8, 5)}border-radius:1px;background:#e8f0fb"></div>')
        cells.append(f'<div class="abs" style="{box(30 + k * 64, 50, 8, 5)}border-radius:1px;background:#e8f0fb"></div>')
    cm.append(f'<div class="abs" style="{box(-120, 742, 560, 58)}overflow:hidden"><div class="abs navy-side" id="{s}-strip" style="{box(-640, 0, 1180, 58)}border-radius:4px">{"".join(cells)}</div></div>')
    cm.append(shadow(150, 860, 330, 46, 0.6))
    cm.append(f'<div class="abs" id="{s}-meter" style="{box(140, 470, 330, 380)}">'
              f'<div class="abs por" style="{box(0, 0, 330, 380)}border-radius:32px"></div>'
              f'<div class="abs navy-side" style="{box(12, 366, 306, 12)}border-radius:0 0 26px 26px"></div>'
              + dial(f"{s}-cd", 165, 150, 112, arcs=((-120, -30, "#cbdbf4"),)) +
              f'<div class="abs" style="{box(26, 272, 278, 70)}border-radius:16px;background:linear-gradient(180deg,#e3ebf7,#f6f8fc);box-shadow:inset 0 2px 4px rgba(28,51,84,.2)"></div>'
              f'<div class="abs" id="{s}-cg" style="left:110px;top:250px;width:110px;height:110px">{gear_svg(s + "-cgs", 110, 14)}</div>'
              f'<div class="led" id="{s}-cled" style="left:290px;top:24px;background:radial-gradient(circle at 40% 35%,#ffffff,#acc6e7 55%,#3a6299)"></div>'
              f'{screws_rect(0, 0, 330, 380, inset=16, size=10)}</div>')
    S.mid.extend(cm)

    # ---------------------------------------------------------------- local render machine (hero)
    lm = [shadow(LX - 40, LY + LH - 10, LW + 120, 80, 1.0)]
    lm.append(f'<div class="abs" id="{s}-lm" style="{box(LX, LY, LW, LH)}">'
              f'<div class="abs por" style="{box(0, 0, LW, LH)}border-radius:40px"></div>'
              f'<div class="abs navy-side" style="{box(16, LH - 14, LW - 32, 14)}border-radius:0 0 34px 34px"></div>'
              # name plate (spoken in the VO)
              f'<div class="abs por-flat" style="{box(40, 26, 250, 44)}border-radius:12px"></div>'
              f'<div class="abs" style="{box(40, 26, 250, 44)}display:flex;align-items:center;justify-content:center;font:800 25px Montserrat;letter-spacing:.01em;color:#294b77">HyperFrames</div>'
              f'<div class="led" style="left:{LW - 60}px;top:42px"></div><div class="led" style="left:{LW - 86}px;top:42px"></div>'
              # wheel window
              f'<div class="abs" style="{box(40, 92, LW - 80, 330)}border-radius:28px;background:linear-gradient(160deg,#3a6299,#1c3354 75%);box-shadow:inset 0 3px 8px rgba(0,0,0,.35)"></div>'
              f'<div class="abs" style="{box(54, 106, LW - 108, 302)}border-radius:22px;border:2px solid rgba(203,219,244,.35)"></div>'
              f'</div>')
    # wheel with mounted frames (rotates the whole time)
    wh = [gear_svg(f"{s}-whs", 280, 26, hole=0.22, spokes=6)]
    for k in range(6):
        import math
        a = 2 * math.pi * k / 6
        cx, cy = 140 + 98 * math.cos(a), 140 + 98 * math.sin(a)
        wh.append(f'<div class="abs" style="{box(cx - 20, cy - 28, 40, 56)}border-radius:6px;background:linear-gradient(160deg,#ffffff,#dbe6f6);box-shadow:inset 0 0 0 1.5px rgba(41,75,119,.35)">'
                  f'<div class="abs" style="{box(6, 10, 28, 20)}border-radius:3px;background:{"#294b77" if k % 2 else "#acc6e7"}"></div>'
                  f'<div class="abs" style="{box(6, 36, 22, 4)}border-radius:2px;background:#cbdbf4"></div></div>')
    lm.append(f'<div class="abs" id="{s}-wh" style="{box(LX + LW / 2 - 140, LY + 117, 280, 280)}">{"".join(wh)}</div>')
    # status strip with progress bars
    lm.append(f'<div class="abs glass" style="{box(LX + 40, LY + 440, 250, 80)}border-radius:16px"></div>')
    for k in range(3):
        lm.append(f'<div class="abs" style="{box(LX + 58, LY + 456 + k * 18, 210, 8)}border-radius:4px;background:#dbe6f6"></div>')
        lm.append(f'<div class="abs" id="{s}-pb{k}" style="{box(LX + 58, LY + 456 + k * 18, 210, 8)}border-radius:4px;background:{"#294b77" if k < 2 else "#9fd8c4"}"></div>')
    lm.append(vent_lines(LX + 314, LY + 448, 90, 7, gap=10))
    # output chute
    lm.append(f'<div class="abs por" style="{box(LX + LW - 30, LY + LH - 150, 90, 60)}border-radius:10px 22px 22px 10px"></div>')
    lm.append(f'<div class="abs" style="{box(LX + LW + 10, LY + LH - 132, 40, 8)}border-radius:4px;background:#1c3354"></div>')
    # mint check badge (apex on "kredit")
    lm.append(f'<div class="abs" id="{s}-ok" style="{box(LX + LW - 70, LY - 34, 92, 92)}border-radius:50%;background:radial-gradient(circle at 38% 32%,#e9fbf4,#9fd8c4 60%,#6fbfa4);box-shadow:0 10px 18px -6px rgba(28,51,84,.35),inset 0 2px 0 #fff">'
              f'<svg width="92" height="92" viewBox="0 0 92 92" style="position:absolute;left:0;top:0"><path id="{s}-okp" d="M27 47 L40 60 L66 33" fill="none" stroke="#1c3354" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="60" stroke-dashoffset="60"/></svg></div>')
    S.mid.extend(lm)

    # ---------------------------------------------------------------- tray + stacked frames
    tr = [shadow(TX - 20, TY + 70, 360, 60, 0.9)]
    tr.append(f'<div class="abs" id="{s}-tray" style="{box(TX, TY - 220, 320, 330)}">'
              f'<div class="abs" style="{box(0, 230, 320, 80)}border-radius:50%;background:linear-gradient(180deg,#c3d5ee,#acc6e7);"></div>'
              f'<div class="abs navy-side" style="{box(6, 254, 308, 26)}border-radius:0 0 50% 50% / 0 0 100% 100%"></div>'
              f'<div class="abs" style="{box(0, 220, 320, 76)}border-radius:50%;background:radial-gradient(ellipse at 45% 40%,#ffffff,#f1f5fb 55%,#d6e2f2);box-shadow:inset 0 -4px 8px rgba(172,198,231,.8)"></div>'
              f'<div class="abs" style="{box(26, 232, 268, 52)}border-radius:50%;border:1.5px solid rgba(172,198,231,.7)"></div>'
              + "".join(f'<div class="abs p3" id="{s}-fr{k}" style="{box(110, 150 - k * 12, 100, 120)}">{frame_card(f"{s}-fc{k}", 0, 0, 100, 120, k)}</div>' for k in range(6))
              + f'<div class="abs" id="{s}-ch" style="{box(0, 40, 320, 200)}">'
              + f'<svg width="320" height="200" viewBox="0 0 320 200" style="position:absolute;left:0;top:0;overflow:visible">'
              + '<path d="M18 190 L160 22 L302 190" fill="none" stroke="#9fb6d6" stroke-width="4" stroke-dasharray="7 4" stroke-linecap="round"/>'
              + '<path d="M160 22 L160 190" fill="none" stroke="#9fb6d6" stroke-width="3" stroke-dasharray="7 4"/></svg>'
              + f'<div class="abs" style="{box(142, 0, 36, 36)}border-radius:50%;border:6px solid #3a6299;background:transparent;box-shadow:0 2px 4px rgba(28,51,84,.3)"></div>'
              + '</div>'
              + f'</div>')
    S.mid.extend(tr)

    # ---------------------------------------------------------------- near
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(980, 420, 26, 420)}border-radius:13px;background:linear-gradient(90deg,#ffffff,#cbdbf4);filter:blur(4px);opacity:.85"></div>'
                  f'<div class="abs" style="{box(40, 1000, 160, 160)}border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"></div></div>')
    apex(S, S.near, f"{s}-ap", LX + LW - 24, LY + 12, wKr, size=440, sparks=6, seed=21, op=0.8)

    # ================================================================ motion
    S.cam([(S.t0, {"x": 0, "y": 0, "z": 260, "rotationY": 2, "rotationX": 0}, None),
           (wKr - 0.05, {"x": -20, "z": 330, "rotationY": -1}, "sine.inOut"),
           (S.t1 - 0.3, {"x": -40, "y": -30, "z": 380, "rotationY": -2}, "sine.inOut"),
           (S.t1, {"x": -20, "y": -380, "z": 540, "rotationY": -2}, "power3.in")])
    # film strip: runs, slows on "nggak", stops before "kredit"
    S.init(f"#{s}-strip", {"x": 0})
    S.ft(f"#{s}-strip", {"x": 0}, {"x": 448}, S.t0, wNg - S.t0, "none")
    S.ft(f"#{s}-strip", {"x": 448}, {"x": 512}, wNg, 0.42, "power2.out")
    S.init(f"#{s}-cg", {"rotation": 0})
    S.ft(f"#{s}-cg", {"rotation": 0}, {"rotation": 360}, S.t0, wNg - S.t0, "none")
    S.ft(f"#{s}-cg", {"rotation": 360}, {"rotation": 410}, wNg, 0.42, "power2.out")
    # needle ticks upward per second of video ... then drops to rest on "kredit"
    keys = [(S.t0, {"rotation": -70, "transformOrigin": "50% 100%"}, None)]
    t, a = S.t0, -70
    while t + 0.32 < wNg:
        t += 0.32; a += 9
        keys.append((t, {"rotation": a}, "back.out(3)"))
    keys.append((wKr - 0.04, {"rotation": a + 4}, "sine.inOut"))
    keys.append((wKr + 0.5, {"rotation": -118}, "bounce.out"))
    keys.append((S.t1, {"rotation": -118}, "none"))
    S.keys(f"#{s}-cd-nd", keys)
    S.init(f"#{s}-cled", {"opacity": 1})
    S.ft(f"#{s}-cled", {"opacity": 1}, {"opacity": 0.15}, wKr, 0.2, "power2.out")
    S.init(f"#{s}-meter", {"opacity": 1, "scale": 1, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-meter", {"opacity": 1, "scale": 1}, {"opacity": 0.62, "scale": 0.95}, wKr + 0.1, 0.6, "power2.inOut")
    # local wheel never stops
    S.init(f"#{s}-wh", {"rotation": 0})
    S.ft(f"#{s}-wh", {"rotation": 0}, {"rotation": 420}, S.t0, S.t1 - S.t0, "none")
    for k in range(3):
        S.init(f"#{s}-pb{k}", {"scaleX": 0.1, "transformOrigin": "0% 50%"})
        t = S.t0 + k * 0.2
        n = 0
        while t < S.t1 - 0.2:
            d = 0.9 + 0.15 * k
            S.ft(f"#{s}-pb{k}", {"scaleX": 0.1}, {"scaleX": 1}, t, min(d, S.t1 - t), "power1.inOut")
            t += d + 0.05
            n += 1
    # frames drop out of the chute and stack in the tray
    drops = [S.t0 + 0.2 + k * 0.55 for k in range(6)]
    for k, at in enumerate(drops):
        S.init(f"#{s}-fr{k}", {"x": 140, "y": -150, "opacity": 0, "rotation": -16, "rotationX": 0})
        S.ft(f"#{s}-fr{k}", {"x": 140, "y": -150, "opacity": 0, "rotation": -16}, {"x": 0, "y": 0, "opacity": 1, "rotation": (k % 3 - 1) * 4}, at, 0.42, "power2.in")
        S.ft(f"#{s}-fr{k}", {"y": 0, "rotationX": 0}, {"y": -6, "rotationX": 18}, at + 0.42, 0.2, "power2.out")
    # mint confirmation on "kredit"
    S.init(f"#{s}-ok", {"scale": 0, "opacity": 0})
    S.ft(f"#{s}-ok", {"scale": 0, "opacity": 0}, {"scale": 1, "opacity": 1}, wKr - 0.05, 0.42, "back.out(2.4)")
    S.init(f"#{s}-okp", {"strokeDashoffset": 60})
    S.ft(f"#{s}-okp", {"strokeDashoffset": 60}, {"strokeDashoffset": 0}, wKr + 0.12, 0.3, "power2.out")
    # hand-off: chains lower onto the tray, the tray lifts like a scale pan
    S.init(f"#{s}-ch", {"scaleY": 0, "opacity": 0, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-ch", {"scaleY": 0, "opacity": 0}, {"scaleY": 1, "opacity": 1}, S.t1 - 0.62, 0.36, "back.out(1.6)")
    S.init(f"#{s}-tray", {"y": 0})
    S.ft(f"#{s}-tray", {"y": 0}, {"y": -70}, S.t1 - 0.28, 0.28, "power2.inOut")
