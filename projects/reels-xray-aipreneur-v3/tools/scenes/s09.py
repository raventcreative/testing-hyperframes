"""S09 — THE FINAL RENDER (20.22–22.82)  VO: "FFmpeg nge-render jadi MP4."
Opens on the bare wheel from S08 (same size/position) = the sprocket drum of a miniature rendering press;
the camera pulls back to reveal the press. Film frames travel over the drum, the press head stamps on
"nge-render", rollers turn, and the finished MP4 reel rises from the output with a white glint on "MP4".
End: the reel drops toward a drawer below (S10 opens on the cabinet)."""
from xk import box, screw, shadow, apex, gear_svg, rivets_line, r3
from kit_b import backdrop, near_blur, engrave, roller, spin_roller, film_frame, gear_side

SFX = [(21.0, "click", 0.1), (21.76, "sparkle", 0.09)]

DX, DY, DS = 300, 900, 200            # sprocket drum (centre, size)
SC = 560 / DS                         # opening scale: drum = S08 wheel (560 px at 590, 930)


def build(S):
    s = S.id
    S.persp_origin = (590, 620)
    W43, W44, W46 = S.W(43), S.W(44), S.W(46)    # FFmpeg 20.32, nge-render 21.00, MP4 21.76
    end = S.t1
    backdrop(S, seed=9)
    g = []
    # ---------------------------------------------------- press body
    g.append(shadow(120, 1225, 900, 110, 0.9))
    g.append(f'<div class="abs navy-side" style="{box(140, 1228, 840, 48)}border-radius:0 0 26px 26px"></div>')
    g.append(f'<div class="abs por" style="{box(140, 960, 840, 280)}border-radius:26px">'
             f'{screw(26, 26, 20, 12)}{screw(814, 26, -30, 12)}{screw(26, 254, 60, 12)}{screw(814, 254, 15, 12)}'
             f'{rivets_line(70, 240, 770, 240, 14)}'
             + "".join(f'<div class="abs" style="{box(60 + k * 14, 70, 4, 110)}border-radius:2px;background:rgba(172,198,231,.6)"></div>' for k in range(8))
             + f'<div class="abs por-dim" style="{box(250, 96, 340, 90)}border-radius:16px;box-shadow:inset 2px 2px 4px rgba(28,51,84,.18),inset -1px -1px 0 #fff">'
             f'{engrave(s + "-lab", "FFmpeg", 0, 22, 40, w=340)}</div>'
             + "".join(f'<div class="led-off" style="left:{650 + k * 34}px;top:118px"></div><div class="led" id="{s}-led{k}" style="left:{650 + k * 34}px;top:118px"></div>' for k in range(4))
             + "</div>")
    # guide columns + press head
    for x in (470, 702):
        g.append(f'<div class="abs" style="{box(x - 8, 700, 16, 270)}border-radius:8px;background:linear-gradient(90deg,#c9d8ee,#ffffff 35%,#dbe6f6 65%,#9fb6d6)"></div>')
    g.append(f'<div class="abs por" style="{box(440, 680, 296, 40)}border-radius:14px">{screw(20, 20, 30, 10)}{screw(276, 20, -30, 10)}</div>')
    # film frames (travel left -> right, under the head)
    for k in range(5):
        g.append(film_frame(f"{s}-fr{k}", 330, 820, 130, 98, k))
    g.append(f'<div class="abs por" id="{s}-head" style="{box(456, 760, 264, 104)}border-radius:16px">'
             f'<div class="abs navy-side" style="{box(0, 82, 264, 22)}border-radius:0 0 16px 16px"></div>'
             f'<div class="abs" style="{box(30, 26, 204, 10)}border-radius:5px;background:#cbdbf4;box-shadow:inset 0 1px 2px rgba(28,51,84,.3)"></div>'
             f'{screw(18, 50, 20, 10)}{screw(246, 50, -20, 10)}</div>')
    g.append(roller(f"{s}-r1", 470, 940, 240, 18) + roller(f"{s}-r2", 740, 940, 200, 18))
    # small meshing gear + sprocket drum (drawn on top)
    g.append(f'<div class="abs" id="{s}-g2" style="{box(410, 860, 120, 120)}">{gear_side(s + "-gbs", 120, 24, 3, 4)}{gear_svg(s + "-gb", 120, 24)}</div>')
    g.append(f'<div class="abs" id="{s}-drum" style="{box(DX - DS / 2, DY - DS / 2, DS, DS)}">{gear_side(s + "-gds", DS, 40, 3.6, 5)}{gear_svg(s + "-gd", DS, 40)}</div>')
    # output: the finished MP4 reel (glass display) rises behind the body top
    reel = (f'<div class="abs" id="{s}-mp4" style="{box(780, 600, 180, 320)}">'
            f'<div class="abs glass" style="{box(0, 0, 180, 320)}border-radius:28px;border-color:rgba(58,98,153,.5)"></div>'
            f'<div class="abs" style="{box(14, 16, 152, 250)}border-radius:18px;background:linear-gradient(160deg,#3a6299,#1c3354);overflow:hidden">'
            f'<div class="abs" style="{box(54, 90, 0, 0)}border-style:solid;border-width:34px 0 34px 56px;border-color:transparent transparent transparent #ffffff"></div>'
            f'<div class="abs" style="{box(16, 222, 120, 8)}border-radius:4px;background:rgba(203,219,244,.5)"></div>'
            f'<div class="abs" style="{box(16, 222, 70, 8)}border-radius:4px;background:#9fd8c4"></div>'
            f'<div class="abs" id="{s}-glint" style="{box(-120, -40, 80, 340)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.75),rgba(255,255,255,0))"></div></div>'
            f'<div class="abs" style="left:0;top:276px;width:180px;text-align:center;font:900 30px Montserrat;letter-spacing:.06em;color:#294b77">MP4</div></div>')
    g.append(f'<div class="abs" style="{box(800, 954, 150, 14)}border-radius:7px;background:linear-gradient(180deg,#1c3354,#3a6299);box-shadow:inset 0 2px 4px rgba(0,0,0,.35)"></div>')
    g.append(reel)   # in front: rises out of the output slot
    S.mid.append(f'<div class="abs" id="{s}-rig" style="{box(0, 0, 1080, 1920)}">{"".join(g)}</div>')
    near_blur(S, [(f"{s}-n1", 900, 1420, 240, 28, "border-radius:14px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px)"),
                  (f"{s}-n2", -50, 520, 150, 150, "border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)")])
    apex(S, S.near, f"{s}-ap", 870, 690, W46, size=520, ring=True, sparks=7, seed=17)

    # ================================================================ motion
    # pull back from the drum close-up (drum = S08 wheel) to the whole press
    S.keys(f"#{s}-rig", [(S.t0, {"x": 590 - DX, "y": 930 - DY, "scale": SC, "transformOrigin": f"{DX}px {DY}px"}, None),
                         (S.t0 + 0.08, {"x": 590 - DX, "y": 930 - DY, "scale": SC * 0.985}, "none"),
                         (W43 + 0.55, {"x": 0, "y": 0, "scale": 1}, "expo.inOut")])
    S.cam([(S.t0, {"z": 0, "rotationY": 0, "y": 0}, None),
           (W46 - 0.05, {"z": 30, "rotationY": -3}, "sine.inOut"),
           (W46 + 0.25, {"z": 60}, "power3.out"),
           (end - 0.45, {"z": 50, "rotationY": -1}, "sine.inOut"),
           (end, {"z": 20, "y": -120}, "power2.in")])
    S.ft(f"#{s}-drum", {"rotation": 120}, {"rotation": 120 + 45 * 9}, S.t0, end - S.t0, "power1.inOut")
    S.init(f"#{s}-drum", {"rotation": 120})   # = S08 wheel's final angle (840 deg)
    S.init(f"#{s}-g2", {"rotation": 0})
    S.ft(f"#{s}-g2", {"rotation": 0}, {"rotation": -45 * 9 * 40 / 24}, S.t0, end - S.t0, "power1.inOut")
    spin_roller(S, f"#{s}-r1", W43, end, 220)
    spin_roller(S, f"#{s}-r2", W43, end, 220)
    # frames: a strip travelling right, each vanishes under the head (the press absorbs it)
    for k in range(5):
        a = W43 + 0.35 + k * 0.17
        S.init(f"#{s}-fr{k}", {"x": -420, "y": -150, "rotation": -8, "opacity": 0})
        S.ft(f"#{s}-fr{k}", {"x": -420, "y": -150, "rotation": -8, "opacity": 0}, {"x": -60, "y": -40, "rotation": -3, "opacity": 1}, a, 0.3, "power2.out")
        S.ft(f"#{s}-fr{k}", {"x": -60, "y": -40, "rotation": -3}, {"x": 230, "y": 34, "rotation": 0}, a + 0.3, 0.42, "power2.in")
        S.ft(f"#{s}-fr{k}", {"opacity": 1}, {"opacity": 0}, a + 0.68, 0.05, "none")
    # press head stamps on "nge-render" (and once more, lighter)
    S.keys(f"#{s}-head", [(S.t0, {"y": 0}, None), (W44 - 0.12, {"y": -14}, "power2.out"), (W44 + 0.02, {"y": 30}, "power4.in"),
                          (W44 + 0.3, {"y": 0}, "back.out(2)"), (W46 - 0.4, {"y": 18}, "power3.in"), (W46 - 0.2, {"y": 0}, "power2.out")])
    for k in range(4):
        S.init(f"#{s}-led{k}", {"opacity": 0})
        S.ft(f"#{s}-led{k}", {"opacity": 0}, {"opacity": 1}, W44 + 0.1 + k * 0.18, 0.08, "none")
    # the MP4 reel rises, glints on "MP4", then drops toward the drawer
    S.keys(f"#{s}-mp4", [(S.t0, {"y": 330, "rotation": 0, "scale": 0.12, "opacity": 0, "transformOrigin": "50% 100%"}, None), (W46 - 0.42, {"y": 330, "opacity": 0}, "none"),
                         (W46 - 0.3, {"opacity": 1, "scale": 0.3, "y": 300}, "none"),
                         (W46, {"y": 0, "scale": 1}, "back.out(1.4)"), (end - 0.42, {"y": -12, "rotation": -2}, "sine.inOut"),
                         (end, {"y": 640, "rotation": 7, "scale": 0.94}, "power3.in")])
    S.init(f"#{s}-glint", {"x": 0})
    S.ft(f"#{s}-glint", {"x": 0}, {"x": 360}, W46 - 0.02, 0.45, "power2.inOut")
