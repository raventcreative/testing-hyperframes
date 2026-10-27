"""S15 — VERTIGO / DOLLY ZOOM (effect #15).
A CSS-3D corridor (floor tiles, ceiling light strips, framed content on both walls, a glowing navy doorway at the end)
whose vanishing point sits behind the mascot's head. Dolly zoom: the mascot keeps exactly the same size while the
background scales 1 -> 1.55 in 0.85 s and the perspective flattens at the same time (zoom in + dolly out)."""
from xk import box, r3
from kit import thumb

DEPTH = 1600
VP = (540, 470)


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    wall = "background:linear-gradient(180deg,#f7f9fd 0%,#e6edf7 100%);backface-visibility:visible"
    frames_l = "".join(f'<div class="abs" style="{box(140 + k * 470, 300, 300, 400)}border-radius:10px;background:#fff;box-shadow:0 10px 24px -12px rgba(10,13,44,.45);'
                       f'padding:12px"><img src="{thumb(k)}" alt="" style="width:276px;height:376px;object-fit:cover;border-radius:4px;display:block" /></div>' for k in range(3))
    frames_r = "".join(f'<div class="abs" style="{box(1160 - k * 470, 300, 300, 400)}border-radius:10px;background:#fff;box-shadow:0 10px 24px -12px rgba(10,13,44,.45);'
                       f'padding:12px"><img src="{thumb(k + 5)}" alt="" style="width:276px;height:376px;object-fit:cover;border-radius:4px;display:block" /></div>' for k in range(3))
    stripes = "background-image:repeating-linear-gradient(90deg, rgba(41,75,119,.10) 0 2px, transparent 2px 200px)"
    tiles = ("background:#e9eff8;background-image:linear-gradient(rgba(41,75,119,.18) 2px, transparent 2px),"
             "linear-gradient(90deg, rgba(41,75,119,.18) 2px, transparent 2px);background-size:180px 160px")
    lights = "".join(f'<div class="abs" style="{box(390, 120 + k * 360, 300, 60)}border-radius:30px;background:#fff;box-shadow:0 0 40px 10px rgba(255,255,255,.95)"></div>' for k in range(4))
    room = (f'<div class="abs" id="{s}-room" style="left:0;top:0;width:1080px;height:1080px;perspective:900px;perspective-origin:{VP[0]}px {VP[1]}px">'
            f'<div class="abs p3" style="left:0;top:0;width:1080px;height:1080px">'
            # back wall + doorway
            f'<div class="abs" style="left:0;top:0;width:1080px;height:1080px;transform:translateZ(-{DEPTH}px);background:linear-gradient(180deg,#eef3fa,#dde6f2)">'
            f'<div class="abs" style="{box(330, 230, 420, 850)}border-radius:210px 210px 0 0;background:linear-gradient(180deg,#294B77 0%,#0A0D2C 100%);'
            f'box-shadow:0 0 0 18px #fff, 0 0 80px 20px rgba(41,75,119,.35)"></div>'
            f'<div class="abs" style="{box(400, 330, 280, 750)}border-radius:140px 140px 0 0;background:radial-gradient(ellipse at 50% 30%, rgba(255,255,255,.95) 0%, rgba(190,215,245,.6) 35%, rgba(41,75,119,0) 70%)"></div></div>'
            # left / right walls
            f'<div class="abs" style="left:0;top:0;width:{DEPTH}px;height:1080px;transform-origin:0 50%;transform:rotateY(90deg);{wall};{stripes}">{frames_l}</div>'
            f'<div class="abs" style="left:{1080 - DEPTH}px;top:0;width:{DEPTH}px;height:1080px;transform-origin:100% 50%;transform:rotateY(-90deg);{wall};{stripes}">{frames_r}</div>'
            # floor / ceiling
            f'<div class="abs" style="left:0;top:{1080 - DEPTH}px;width:1080px;height:{DEPTH}px;transform-origin:50% 100%;transform:rotateX(90deg);{tiles}"></div>'
            f'<div class="abs" style="left:0;top:0;width:1080px;height:{DEPTH}px;transform-origin:50% 0;transform:rotateX(-90deg);background:linear-gradient(180deg,#f4f7fc,#e3eaf5)">{lights}</div>'
            f'</div></div>')
    S.back.append(f'<div class="abs" id="{s}-bg" style="left:0;top:0;width:1080px;height:1080px;overflow:hidden">{room}</div>')
    # soft floor contact shadow (front of the room, behind the mascot)
    S.back.append(f'<div class="abs cshadow" style="{box(300, 990, 480, 90)}opacity:.55"></div>')

    # ---------------------------------------------------------------- dolly zoom: bg 1 -> 1.55 in 0.85 s + perspective flattens
    S.init(f"#{s}-room", {"scale": 1, "perspective": 900, "transformOrigin": f"{VP[0]}px {VP[1]}px"})
    A, B = {"scale": 1, "perspective": 900}, {"scale": 1.55, "perspective": 1500}
    S.ft(f"#{s}-room", A, B, t0 + 0.45, 0.85, "power2.inOut")
    S.ft(f"#{s}-room", B, A, t0 + 2.2, 0.85, "power2.inOut")
    S.ft(f"#{s}-room", A, B, t0 + 3.6, 0.85, "power2.inOut")
    # slight motion blur only while the background moves
    for a in (t0 + 0.45, t0 + 2.2, t0 + 3.6):
        S.ft(f"#{s}-bg", {"filter": "blur(0px)"}, {"filter": "blur(2.5px)"}, a + 0.1, 0.32, "sine.in")
        S.ft(f"#{s}-bg", {"filter": "blur(2.5px)"}, {"filter": "blur(0px)"}, a + 0.42, 0.33, "sine.out")
    S.init(f"#{s}-bg", {"filter": "blur(0px)"})

    # ---------------------------------------------------------------- mascot: SAME size the whole time; reacts to the pull
    v = {"fx": 540, "fy": 1170, "h": 1030, "yaw": 0, "pitch": 5}
    S.mv([(t0, v, None)])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.45, "stop", 0.3), (t0 + 1.8, "low", 0.4), (t0 + 3.55, "shrug", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (t0 + 0.5, "stop", 0.3), (t0 + 1.8, "low", 0.4), (t0 + 3.6, "shrug", 0.3)])
    S.act("head", [(t0, [0, 0, 0], 0.3), (t0 + 0.45, [0.1, 0, 0], 0.3), (t0 + 1.4, [-0.04, 0.16, 0.04], 0.4),
                   (t0 + 2.2, [0.08, -0.1, -0.03], 0.35), (t0 + 3.6, [0.1, 0.06, 0.06], 0.3)])
    S.act("torso", [(t0, {}, 0.3), (t0 + 0.45, {"chest": [-0.05, 0, 0]}, 0.3), (t0 + 1.6, {}, 0.4), (t0 + 3.6, {"chest": [-0.05, 0, 0]}, 0.3)])
