"""S17 — THE RESOURCE REVEAL (50.26–52.26)  VO: "Mau repo dan contoh prompt buat nyoba?"
Opens through the S16 iris onto a translucent liquid-glass repository case. The hinged lid swings open; the code
folder rises carrying the user's 3D GitHub mark (orbit reveal on "repo"), a mini Reel preview rises on "contoh",
the prompt sheet lands on "prompt"; a highlight runs from the repo to the prompt. The lid then lifts off and folds
into the comment bubble's start pose (hand-off to S18)."""
from xk import box, screw, shadow, rivets_line, apex, minireel, minireel_anim, r3
from kit_e import folder, iris_grad, bubble, front, BX, BY, BW, BH

SFX = [(50.52, "sparkle", 0.08), (51.30, "pop", 0.1)]

CX, CY, CW, CHh, CD = 330, 850, 520, 300, 220      # case container (front face) + depth


def build(S):
    s = S.id
    S.persp_origin = (590, 560)
    WM, WR, WC, WP, WB = S.W(109), S.W(110), S.W(112), S.W(113), S.W(114)   # Mau 50.36 repo 50.52 contoh 51.00 prompt 51.30 buat 51.54

    # ---------------- far plane
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(200, 300, 720, 1180)}border-radius:360px 360px 40px 40px;opacity:.5"></div>'
                 f'<div class="abs" style="{box(250, 350, 620, 1090)}border-radius:310px 310px 30px 30px;border:2px solid rgba(255,255,255,.8)"></div>'
                 f'<div class="abs" style="{box(140, 1420, 860, 6)}border-radius:3px;background:rgba(172,198,231,.55)"></div></div>')
    S.far.append(f'<div class="abs" id="{s}-halo" style="{box(150, 380, 880, 880)}border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95) 0%,rgba(255,255,255,0) 62%)"></div>')

    # ---------------- hero: the case (CSS 3D box, open top, hinged glass lid)
    S.mid.append(shadow(CX - 40, CY + CHh - 26, CW + 80, 90, 1.0))
    W, H, D = CW, CHh, CD
    f = []
    # bottom (porcelain tray with grid) + back + sides (tinted glass)
    f.append(f'<div class="abs grid-paper" style="{box(0, (H - D) / 2, W, D)}transform:rotateX(-90deg) translateZ({H / 2}px);box-shadow:inset 0 0 0 3px #dbe6f6"></div>')
    f.append(f'<div class="abs" style="{box(0, 0, W, H)}transform:translateZ({-D / 2}px);border-radius:10px;background:linear-gradient(170deg,rgba(232,240,251,.75),rgba(203,219,244,.6));box-shadow:inset 0 0 0 2px rgba(255,255,255,.9)"></div>')
    for sgn in (-1, 1):
        f.append(f'<div class="abs" style="{box((W - D) / 2, 0, D, H)}transform:rotateY({90 * sgn}deg) translateZ({W / 2}px);'
                 f'background:linear-gradient(180deg,rgba(255,255,255,.55),rgba(203,219,244,.55));box-shadow:inset 0 0 0 2px rgba(255,255,255,.9),inset 0 -26px 0 rgba(41,75,119,.55)"></div>')
    # contents rising (inside the box, at different depths)
    items = []
    items.append(f'<div class="abs p3" id="{s}-it1" style="{box(36, 70, 210, 168)}">{folder(s + "-fd", 0, 0, 210, 168, mark_id=s + "-gh")}</div>')
    items.append(f'<div class="abs p3" id="{s}-it2" style="{box(180, 50, 190, 250)}">'
                 f'<div class="abs por-flat" style="{box(0, 0, 190, 250)}border-radius:14px;box-shadow:0 18px 26px -14px rgba(28,51,84,.4),inset 1.5px 1.5px 0 #fff"></div>'
                 f'<div class="abs navy-side" style="{box(0, 0, 190, 44)}border-radius:14px 14px 0 0"></div>'
                 f'<div class="abs mono" style="left:16px;top:8px;font-size:22px;color:#cbdbf4">&gt;_</div>'
                 f'<div class="abs" style="{box(150, 14, 16, 16)}border-radius:50%;background:#9fd8c4"></div>'
                 + "".join(f'<div class="abs" style="{box(18, 66 + k * 24, [150, 120, 140, 96, 130, 80, 110][k], 9)}border-radius:5px;background:{"#294b77" if k in (0, 3) else "#cbdbf4"}"></div>' for k in range(7))
                 + f'<div class="abs" style="{box(18, 222, 70, 14)}border-radius:7px;background:#9fd8c4"></div></div>')
    items.append(f'<div class="abs p3" id="{s}-it3" style="{box(330, 60, 132, 236)}">'
                 f'<div class="abs" style="{box(4, 4, 132, 236)}border-radius:24px;background:#1c3354"></div>'
                 f'<div class="abs por" style="{box(0, 0, 132, 236)}border-radius:24px"></div>'
                 f'<div class="abs" style="{box(9, 14, 114, 208)}border-radius:12px;overflow:hidden;background:linear-gradient(170deg,#fbfcfe,#e6edf8);box-shadow:inset 0 0 0 1.5px rgba(41,75,119,.45)">'
                 f'<div class="abs" style="{box(0, 0, 114, 208)}">{minireel(s + "-mr", 114, 208, 1)}</div></div></div>')
    # highlight connector repo -> prompt (drawn on "buat")
    items.append(f'<svg class="abs" width="{W}" height="400" viewBox="0 -400 {W} 400" style="left:0;top:-400px;overflow:visible">'
                 f'<path id="{s}-cn" d="M150 -160 C170 -260 230 -300 290 -300" fill="none" stroke="#294b77" stroke-width="4" stroke-dasharray="2 9" stroke-linecap="round" style="stroke-dashoffset:0"/>'
                 f'<circle id="{s}-cd" cx="150" cy="-160" r="8" fill="#ffffff" stroke="#294b77" stroke-width="3"/></svg>')
    f.append(f'<div class="abs p3" id="{s}-items" style="{box(0, 0, W, H)}">{"".join(items)}</div>')
    # front face: glass with navy plinth band, porcelain corner caps, latches, rivets
    caps = "".join(f'<div class="abs por" style="{box(x, y, 46, 46)}border-radius:{r}"></div>' for x, y, r in
                   ((-6, -6, "16px 4px 4px 4px"), (W - 40, -6, "4px 16px 4px 4px"), (-6, H - 40, "4px 4px 4px 16px"), (W - 40, H - 40, "4px 4px 16px 4px")))
    f.append(f'<div class="abs" style="{box(0, 0, W, H)}transform:translateZ({D / 2}px)">'
             f'<div class="abs glass" style="{box(0, 0, W, H)}border-radius:14px;background:linear-gradient(135deg,rgba(255,255,255,.5) 0%,rgba(232,240,251,.28) 45%,rgba(203,219,244,.32) 100%)"></div>'
             f'<div class="abs navy-side" style="{box(0, H - 54, W, 54)}border-radius:0 0 14px 14px;box-shadow:inset 0 2px 0 rgba(255,255,255,.25)"></div>'
             f'<div class="abs" style="{box(30, 26, W - 60, 6)}border-radius:3px;background:linear-gradient(90deg,rgba(255,255,255,.95),rgba(255,255,255,0))"></div>'
             + caps + rivets_line(70, H - 27, W - 70, H - 27, 9) +
             f'<div class="abs navy-side" style="{box(W * 0.28 - 22, -10, 44, 34)}border-radius:8px"></div><div class="abs navy-side" style="{box(W * 0.72 - 22, -10, 44, 34)}border-radius:8px"></div>'
             f'<div class="abs" id="{s}-fr" style="{box(-180, 0, 120, H)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.75),rgba(255,255,255,0))"></div></div>')
    # lid on a hinge at the back-top edge (rotationX 90 = closed flat, ~196 = open, leaning back)
    lid = (f'<div class="abs glass" style="{box(0, 0, W, D)}border-radius:14px;background:linear-gradient(135deg,rgba(255,255,255,.6),rgba(203,219,244,.42))"></div>'
           f'<div class="abs" style="{box(0, 0, W, D)}border-radius:14px;box-shadow:inset 0 0 0 10px rgba(247,249,253,.95),inset 0 0 0 12px rgba(172,198,231,.8)"></div>'
           f'<div class="abs por" style="{box(W / 2 - 80, D - 46, 160, 26)}border-radius:13px"></div>'
           f'{screw(26, 26, 20, 11)}{screw(W - 26, 26, -40, 11)}')
    f.append(f'<div class="abs p3" style="{box(0, 0, W, 1)}transform:translateZ({-D / 2}px)"><div class="abs p3" id="{s}-lid" style="{box(0, 0, W, D)}">{lid}</div></div>')
    S.mid.append(f'<div class="abs p3" style="{box(CX, CY, CW, CHh)}transform:rotateX(-6deg)">{"".join(f)}</div>')

    # ---------------- the bubble panel (appears as the lid lifts off, ends in S18's opening pose)
    S.mid.append(bubble(s))

    # ---------------- near plane + the iris we arrive through
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(920, 1240, 220, 220)}border-radius:50%;border:14px solid rgba(255,255,255,.7);filter:blur(5px)"></div></div>')
    apex(S, S.near, f"{s}-ap", 470, 690, WR + 0.08, size=420, sparks=6, seed=17, op=0.65)
    S.near.append(front(iris_grad(f"{s}-iris") +
                        f'<div class="abs" id="{s}-iring" style="{box(590 - 115, 930 - 115, 230, 230)}border-radius:50%;border:17px solid #f7f9fd;'
                        f'box-shadow:inset 0 0 0 2.5px #294b77,0 0 0 2px #acc6e7,0 18px 30px -12px rgba(28,51,84,.4)"></div>', origin=S.persp_origin))

    # ---------------- motion
    t0 = S.t0
    S.init(f"#{s}-iris", {"--r": "107px", "opacity": 1})
    S.ft(f"#{s}-iris", {"--r": "107px"}, {"--r": "800px"}, t0 + 0.02, 0.36, "power3.in")
    S.ft(f"#{s}-iris", {"opacity": 1}, {"opacity": 0}, t0 + 0.26, 0.12, "power1.in")
    S.init(f"#{s}-iring", {"scale": 1, "opacity": 1})
    S.ft(f"#{s}-iring", {"scale": 1}, {"scale": 7.48}, t0 + 0.02, 0.36, "power3.in")
    S.ft(f"#{s}-iring", {"opacity": 1}, {"opacity": 0}, t0 + 0.26, 0.12, "power1.in")
    S.init(f"#{s}-lid", {"rotationX": 90, "transformOrigin": "50% 0%", "opacity": 1})
    S.ft(f"#{s}-lid", {"rotationX": 90}, {"rotationX": 199}, t0 + 0.04, 0.5, "back.out(1.5)")
    S.ft(f"#{s}-lid", {"rotationX": 199}, {"rotationX": 192}, WB + 0.12, 0.2, "power2.in")
    S.ft(f"#{s}-lid", {"opacity": 1}, {"opacity": 0}, WB + 0.3, 0.12, "power1.in")
    S.init(f"#{s}-fr", {"x": 0})
    S.ft(f"#{s}-fr", {"x": 0}, {"x": 760}, t0 + 0.3, 0.9, "power2.inOut")
    # items rise (folder on "repo", reel on "contoh", prompt lands on "prompt")
    rise = [("it1", WR - 0.2, -330, 20), ("it3", WC - 0.18, -345, 56), ("it2", WP - 0.2, -380, -50)]
    for nm, at, dy, z in rise:
        S.init(f"#{s}-{nm}", {"y": 0, "z": z, "rotation": 0})
        S.ft(f"#{s}-{nm}", {"y": 0, "rotation": 0}, {"y": dy, "rotation": -2 if nm == "it1" else 2}, at, 0.36, "back.out(1.7)")
        S.ft(f"#{s}-{nm}", {"y": dy, "rotation": -2 if nm == "it1" else 2}, {"y": dy - 8, "rotation": 0}, at + 0.36, S.t1 - at - 0.36, "sine.inOut")
    # GitHub mark: orbit reveal on "repo"
    S.init(f"#{s}-gh", {"rotationY": -160, "scale": 0.55, "opacity": 0, "transformPerspective": 800})
    S.ft(f"#{s}-gh", {"rotationY": -160, "scale": 0.55, "opacity": 0}, {"rotationY": 10, "scale": 1, "opacity": 1, "transformPerspective": 800}, WR - 0.06, 0.55, "expo.out")
    S.ft(f"#{s}-gh", {"rotationY": 10}, {"rotationY": 0, "transformPerspective": 800}, WR + 0.5, 0.4, "sine.inOut")
    minireel_anim(S, f"{s}-mr", WC - 0.1, S.t1, period=0.6, amp=1.0)
    # connector repo -> prompt
    S.init(f"#{s}-cn", {"opacity": 0, "strokeDashoffset": 60})
    S.ft(f"#{s}-cn", {"opacity": 0, "strokeDashoffset": 60}, {"opacity": 1, "strokeDashoffset": 0}, WB - 0.06, 0.3, "power2.out")
    S.init(f"#{s}-cd", {"opacity": 0, "x": 0, "y": 0})
    S.ft(f"#{s}-cd", {"opacity": 0, "x": 0, "y": 0}, {"opacity": 1, "x": 140, "y": -140}, WB - 0.04, 0.36, "power2.inOut")
    # bubble takes over from the lid: lifts off, ends folded back (rotationX 62) = S18 frame zero
    S.init(f"#{s}-bub", {"opacity": 0, "y": -40, "scaleX": 0.76, "scaleY": 0.5, "rotationX": 24, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-bub", {"opacity": 0}, {"opacity": 1}, WB + 0.28, 0.12, "power1.out")
    S.ft(f"#{s}-bub", {"y": -40, "scaleX": 0.76, "scaleY": 0.5, "rotationX": 24}, {"y": 0, "scaleX": 1, "scaleY": 1, "rotationX": 40}, WB + 0.28, S.t1 - WB - 0.28, "power3.inOut")
    S.init(f"#{s}-halo", {"opacity": 0.75})
    S.ft(f"#{s}-halo", {"opacity": 0.75}, {"opacity": 1}, t0, S.t1 - t0, "sine.inOut")
    # camera: arrive through the iris, gentle push, settle at S18's opening camera
    S.cam([(t0, {"z": 0, "x": 0, "y": 0, "rotationY": -3, "rotationX": 0}, None),
           (t0 + 0.4, {"z": 120, "rotationY": -1.5}, "power2.out"),
           (WP, {"z": 165, "rotationY": 1.5}, "sine.inOut"),
           (S.t1, {"z": 150, "rotationY": 0}, "sine.inOut")])
