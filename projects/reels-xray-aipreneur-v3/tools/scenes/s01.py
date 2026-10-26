"""S01 — THE IMPOSSIBLE OBJECT (0.00–3.24)  VO: "Gila, satu Reels bisa dibongkar jadi mesin."
Porcelain-and-glass phone on an ivory pedestal playing a mini Reel. On "dibongkar" its frame splits along
mechanical seams (anticipation shiver -> snap open with a light pulse), the machine inside shows; the camera
pushes into the opening for the match cut into S02 (same phone, closer)."""
from xk import WORDS, box, div, screw, shadow, pedestal, minireel, minireel_anim, apex, gear_svg, rivets_line, r3

PX, PY, PW, PH = 380, 420, 420, 860      # phone front plate (screen-space at z=0)
SFX = [(WORDS[4]["start"], "click", 0.13), (WORDS[4]["start"] + 0.04, "sparkle", 0.06), (3.02, "whoosh", 0.07)]


def phone_parts(pre, mech=True):
    """phone markup (shared by S01/S02): thickness slabs, inner mechanism, bezel pieces, glass screen."""
    W, H = PW, PH
    out = []
    # thickness: stacked rounded slabs (ice sidewall) behind the front plate
    for k in range(12, 0, -1):
        c = "#1c3354" if k > 8 else "#294b77" if k > 4 else "#3a6299" if k > 1 else "#acc6e7"
        out.append(f'<div style="position:absolute;{box(0, 0, W, H)}border-radius:58px;background:{c};transform:translateZ({-k * 2.6}px)"></div>')
    # inner mechanism (visible through the seams once the frame opens)
    if mech:
        g = []
        g.append(f'<div class="abs" style="{box(-40, -56, W + 80, H + 112)}border-radius:70px;background:linear-gradient(160deg,#3a6299,#1c3354 70%);box-shadow:inset 0 0 0 3px rgba(203,219,244,.35)"></div>')
        g.append(f'<div class="abs" id="{pre}-mg1" style="left:{-30}px;top:{90}px;width:120px;height:120px">{gear_svg(pre + "-g1", 120, 16)}</div>')
        g.append(f'<div class="abs" id="{pre}-mg2" style="left:{W - 96}px;top:{H - 220}px;width:130px;height:130px">{gear_svg(pre + "-g2", 130, 18)}</div>')
        g.append(f'<div class="abs" id="{pre}-mg3" style="left:{W - 70}px;top:{60}px;width:84px;height:84px">{gear_svg(pre + "-g3", 84, 12)}</div>')
        g.append(f'<div class="abs" id="{pre}-mg4" style="left:{-24}px;top:{H - 160}px;width:90px;height:90px">{gear_svg(pre + "-g4", 90, 12)}</div>')
        for k in range(7):  # rails / wiring ribs
            g.append(f'<div class="abs" style="{box(30, 240 + k * 52, W - 60, 3)}background:rgba(203,219,244,.35);border-radius:2px"></div>')
        out.append(f'<div class="abs p3" id="{pre}-mech" style="{box(0, 0, W, H)}">{"".join(g)}</div>')
    # bezel pieces (porcelain), each moves on the "dibongkar" snap
    out.append(f'<div class="abs por" id="{pre}-top" style="{box(0, 0, W, 44)}border-radius:58px 58px 6px 6px">'
               f'<div class="abs" style="{box(W / 2 - 46, 16, 92, 8)}border-radius:4px;background:#cbdbf4;box-shadow:inset 0 1px 2px rgba(28,51,84,.35)"></div>'
               f'<div class="abs" style="{box(W / 2 + 62, 13, 13, 13)}border-radius:50%;background:radial-gradient(circle at 40% 35%,#5d84b9,#1c3354)"></div>'
               f'{screw(34, 24, 30, 9)}{screw(W - 34, 24, -40, 9)}</div>')
    out.append(f'<div class="abs por" id="{pre}-bot" style="{box(0, H - 44, W, 44)}border-radius:6px 6px 58px 58px">'
               f'<div class="abs" style="{box(W / 2 - 60, 22, 120, 6)}border-radius:3px;background:#dbe6f6"></div>'
               f'{screw(34, 20, 70, 9)}{screw(W - 34, 20, 15, 9)}</div>')
    out.append(f'<div class="abs por" id="{pre}-lft" style="{box(0, 40, 24, H - 80)}border-radius:4px">{rivets_line(12, 40, 12, H - 120, 6)}</div>')
    out.append(f'<div class="abs por" id="{pre}-rgt" style="{box(W - 24, 40, 24, H - 80)}border-radius:4px">{rivets_line(12, 40, 12, H - 120, 6)}'
               f'<div class="abs" style="{box(18, 150, 9, 70)}border-radius:5px;background:linear-gradient(90deg,#e6edf8,#c3d5ee)"></div>'
               f'<div class="abs" style="{box(18, 240, 9, 46)}border-radius:5px;background:linear-gradient(90deg,#e6edf8,#c3d5ee)"></div></div>')
    # glass screen with the playing mini Reel
    out.append(f'<div class="abs" id="{pre}-scr" style="{box(24, 44, W - 48, H - 88)}border-radius:16px;overflow:hidden;'
               f'background:linear-gradient(170deg,#fbfcfe 0%,#eef3fa 60%,#e2eaf6 100%);box-shadow:inset 0 0 0 2px rgba(41,75,119,.55),inset 0 0 0 5px rgba(255,255,255,.9)">'
               f'<div class="abs" style="{box(0, 0, W - 48, H - 88)}">{minireel(pre + "-mr", W - 48, H - 88)}</div>'
               f'<div class="abs" id="{pre}-refl" style="{box(-200, -100, 160, H + 100)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.7),rgba(255,255,255,0))"></div></div>')
    # seam light lines (edge lighting follows the separation)
    for nm, b in (("sl1", box(20, 42, W - 40, 3)), ("sl2", box(20, H - 45, W - 40, 3)), ("sl3", box(22, 46, 3, H - 92)), ("sl4", box(W - 25, 46, 3, H - 92))):
        out.append(f'<div class="abs" id="{pre}-{nm}" style="{b}border-radius:2px;background:#ffffff;box-shadow:0 0 10px 2px rgba(172,198,231,.95),0 0 26px rgba(203,219,244,.9)"></div>')
    return "".join(out)


def build(S):
    s = S.id
    S.persp_origin = (590, 520)   # z-pushes grow downward: the hero stays below the caption band
    W4, W6 = S.W(4), S.W(6)                     # "dibongkar" 1.88, "mesin." 2.56
    # ---------------- far plane: porcelain arch backdrop + halo (pushed back, scaled up to stay large)
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(250, 240, 680, 1240)}border-radius:340px 340px 40px 40px;opacity:.55"></div>'
                 f'<div class="abs" style="{box(300, 300, 580, 1150)}border-radius:290px 290px 30px 30px;border:2px solid rgba(255,255,255,.8)"></div>'
                 f'<div class="abs" style="{box(140, 1400, 900, 6)}border-radius:3px;background:rgba(172,198,231,.5)"></div>'
                 f'<div class="abs" style="{box(140, 1424, 900, 3)}border-radius:2px;background:rgba(172,198,231,.35)"></div></div>')
    S.far.append(f'<div class="abs" id="{s}-halo" style="{box(130, 380, 920, 920)}border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95) 0%,rgba(255,255,255,0) 62%)"></div>')
    # ---------------- hero: pedestal + phone (3D)
    S.mid.append(pedestal(f"{s}-ped", 590, 1238, 600, depth=110))
    S.mid.append(shadow(410, 1268, 360, 70, 1.0, id_=f"{s}-csh"))
    S.mid.append(f'<div class="abs p3" id="{s}-phone" style="{box(PX, PY, PW, PH)}">{phone_parts(s)}</div>')
    # ---------------- near plane: out-of-focus glass ring + rail fragment (foreground depth)
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" id="{s}-nr1" style="{box(900, 600, 170, 170)}border-radius:50%;border:12px solid rgba(255,255,255,.7);box-shadow:0 0 0 2px rgba(172,198,231,.6),0 20px 30px -10px rgba(28,51,84,.25);filter:blur(5px)"></div>'
                  f'<div class="abs" id="{s}-nr2" style="{box(-40, 1460, 300, 26)}border-radius:13px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px);opacity:.9"></div></div>')
    apex(S, S.near, f"{s}-ap", 590, 850, W4, size=700, sparks=8, seed=3)

    # ---------------- motion
    # camera: slow push, snap after the break, accelerate into the seam (match cut to S02)
    S.cam([(0.0, {"z": 0, "x": 0, "y": 0, "rotationY": 0, "rotationX": 0}, None),
           (W4 - 0.05, {"z": 150, "rotationY": -3, "rotationX": 1.5}, "sine.inOut"),
           (W6 + 0.15, {"z": 230, "rotationY": 2, "x": -10}, "power2.out"),
           (S.t1, {"z": 720, "rotationY": 9, "x": -170, "y": 150}, "power3.in")])
    S.keys(f"#{s}-phone", [(0.0, {"rotationY": -30, "rotationX": 5, "transformOrigin": "50% 100%"}, None),
                           (W4, {"rotationY": -20, "rotationX": 3}, "sine.inOut"),
                           (S.t1, {"rotationY": -9, "rotationX": 0}, "power2.inOut")])
    S.init(f"#{s}-halo", {"opacity": 0.7, "scale": 0.92})
    S.ft(f"#{s}-halo", {"opacity": 0.7, "scale": 0.92}, {"opacity": 1, "scale": 1.05}, 0.0, S.t1, "sine.inOut")
    minireel_anim(S, f"{s}-mr", 0.0, S.t1, period=1.05, amp=1.2)
    S.init(f"#{s}-refl", {"x": 0, "rotation": 18})
    S.ft(f"#{s}-refl", {"x": 0, "rotation": 18}, {"x": 640, "rotation": 18}, 0.25, 1.3, "power2.inOut")
    # seam lines: dark until the shiver, flicker, then flare on the break
    for k in range(1, 5):
        S.init(f"#{s}-sl{k}", {"opacity": 0})
        S.ft(f"#{s}-sl{k}", {"opacity": 0}, {"opacity": 0.45}, W4 - 0.55, 0.1, "power1.out")
        S.ft(f"#{s}-sl{k}", {"opacity": 0.45}, {"opacity": 0.15}, W4 - 0.45, 0.2, "power1.in")
        S.ft(f"#{s}-sl{k}", {"opacity": 0.15}, {"opacity": 1}, W4 - 0.08, 0.08, "power2.in")
        S.ft(f"#{s}-sl{k}", {"opacity": 1}, {"opacity": 0.55}, W4 + 0.05, 0.6, "power2.out")
    # anticipation: the frame shivers inward, then snaps open (overshoot + settle)
    moves = {"top": {"y": -64}, "bot": {"y": 54}, "lft": {"x": -48}, "rgt": {"x": 48}}
    for nm, mv in moves.items():
        k_ = list(mv.keys())[0]
        v = mv[k_]
        S.init(f"#{s}-{nm}", {k_: 0, "z": 0})
        S.ft(f"#{s}-{nm}", {k_: 0}, {k_: -v * 0.08}, W4 - 0.36, 0.3, "power2.in")
        S.ft(f"#{s}-{nm}", {k_: -v * 0.08, "z": 0}, {k_: v, "z": 14}, W4 - 0.04, 0.42, "back.out(2.2)")
        S.ft(f"#{s}-{nm}", {k_: v, "z": 14}, {k_: v * 1.25, "z": 22}, W6, S.t1 - W6, "power2.in")
    # screen glass lifts forward a little, mechanism spins up
    S.init(f"#{s}-mech", {"scale": 0.9, "z": -8})
    S.ft(f"#{s}-mech", {"scale": 0.9, "z": -8}, {"scale": 1.0, "z": -8}, W4 - 0.04, 0.42, "power3.out")
    S.init(f"#{s}-scr", {"z": 0})
    S.ft(f"#{s}-scr", {"z": 0}, {"z": 26}, W4, 0.5, "power3.out")
    for k, (deg, d) in enumerate(((240, 1), (-200, 1), (300, 1), (-260, 1)), 1):
        S.init(f"#{s}-mg{k}", {"rotation": 0})
        S.ft(f"#{s}-mg{k}", {"rotation": 0}, {"rotation": deg}, W4 - 0.1, S.t1 - W4 + 0.1, "power2.out")
    # contact shadow tightens as the camera rises
    S.init(f"#{s}-csh", {"scaleX": 1})
    S.ft(f"#{s}-csh", {"scaleX": 1, "opacity": 1}, {"scaleX": 1.08, "opacity": 0.85}, W4, 0.5, "power2.out")
