"""S04 — FRAME BREAK. A video plays inside a phone frame, centred on a dark background. On the break the clip opens
upward: his head and both hands burst out over the phone's top edge (only chest-down stays inside the screen), the
protruding part casts a shadow, a few glass shards fly off the edge and the body rises 40 px in 0.3 s."""
import math
from xk import box, r3, Rng

PX, PY, PW, PH, PR, BZ = 290, 470, 500, 700, 64, 16       # phone (bottom runs off-frame like a held phone)
SX, SY, SW, SR = PX + BZ, PY + BZ, PW - 2 * BZ, PR - BZ   # screen
A = {"fx": 540, "fy": 1060, "h": 560, "yaw": 0, "pitch": 5}      # inside the video: full figure, head under the top edge
B = {"fx": 540, "fy": 980, "h": 1000, "yaw": 0, "pitch": 5}      # broken out: chest top just under the edge, head above


def poly(pts):
    return "polygon(" + ", ".join(f"{r3(x)}px {r3(y)}px" for x, y in pts) + ")"


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    tb = t0 + 0.6                       # the break
    # ------------------------------------------------ back: dark stage + phone + the video's own picture
    S.back.append(f'<div class="abs" style="left:0;top:0;width:1080px;height:1080px;background:radial-gradient(ellipse at 50% 58%,#22406e 0%,#122448 42%,#060918 100%)"></div>')
    S.back.append(f'<div class="abs" style="left:0;top:0;width:1080px;height:1080px;opacity:.35;background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);background-size:54px 54px"></div>')
    S.back.append(f'<div class="abs cshadow" style="{box(PX - 120, PY + 40, PW + 240, 260)}opacity:.0"></div>')
    S.back.append(f'<div class="abs" id="{s}-ph" style="{box(PX, PY, PW, PH)}">'
                  f'<div class="abs" style="left:0;top:0;width:{PW}px;height:{PH}px;border-radius:{PR}px;background:linear-gradient(150deg,#3a4458 0%,#0f1420 45%,#2a3242 100%);'
                  f'box-shadow:0 0 0 2px rgba(255,255,255,.18) inset,0 40px 80px -30px rgba(0,0,0,.8),0 0 120px rgba(80,130,220,.25)"></div>'
                  f'<div class="abs" style="left:{BZ}px;top:{BZ}px;width:{SW}px;height:{PH - 2 * BZ}px;border-radius:{SR}px;overflow:hidden;'
                  f'background:url(assets/brand/bg_1080.png) 50% 30% / 1080px 1080px">'
                  f'<div class="abs" style="left:0;top:0;width:{SW}px;height:{PH}px;background:radial-gradient(circle at 50% 35%,rgba(255,255,255,.55),rgba(255,255,255,0) 60%)"></div>'
                  f'<div class="abs" style="left:{SW / 2 - 60}px;top:14px;width:120px;height:32px;border-radius:16px;background:#05070f"></div>'
                  # reels UI (sits behind him)
                  + "".join(f'<div class="abs" style="left:{SW - 58}px;top:{300 + i * 66}px;width:40px;height:40px;border-radius:20px;background:rgba(10,13,44,.28)"></div>' for i in range(3))
                  + f'<div class="abs" style="left:20px;top:{1080 - SY - 62}px;padding:6px 14px;border-radius:14px;background:rgba(10,13,44,.55);font:700 18px/1.2 Poppins;color:#fff">@aipreneur</div>'
                  f'<div class="abs" style="left:20px;top:{1080 - SY - 22}px;width:{SW - 40}px;height:5px;border-radius:3px;background:rgba(10,13,44,.2)"></div>'
                  f'<div class="abs" id="{s}-prog" style="left:20px;top:{1080 - SY - 22}px;width:{SW - 40}px;height:5px;border-radius:3px;background:#0A0D2C;transform-origin:0% 50%"></div>'
                  f'</div></div>')
    S.init(f"#{s}-prog", {"scaleX": 0.18})
    S.ft(f"#{s}-prog", {"scaleX": 0.18}, {"scaleX": 0.86}, t0, t1 - t0, "none")
    # phone recoils on the break
    S.init(f"#{s}-ph", {"y": 0, "scale": 1, "transformOrigin": "50% 0%"})
    S.ft(f"#{s}-ph", {"y": 0, "scale": 1}, {"y": 10, "scale": 0.985}, tb, 0.1, "power2.out")
    S.ft(f"#{s}-ph", {"y": 10, "scale": 0.985}, {"y": 0, "scale": 1}, tb + 0.1, 0.45, "elastic.out(1,0.5)")
    # ------------------------------------------------ front: glass shards flying off the top edge
    R = Rng(41)
    for k in range(10):
        x = SX + 30 + (SW - 60) * (k + R.u(0.1, 0.9)) / 10
        sz = R.u(10, 24)
        S.front.append(f'<div class="abs" id="{s}-g{k}" style="{box(x - sz / 2, SY - sz / 2, sz, sz)}background:linear-gradient(135deg,rgba(255,255,255,.95),rgba(170,200,240,.55));'
                       f'clip-path:polygon(50% 0%,100% {r3(R.u(40, 80))}%,{r3(R.u(10, 50))}% 100%,0% {r3(R.u(20, 60))}%)"></div>')
        ang = math.radians(-90 + (x - 540) / (SW / 2) * 70 + R.u(-12, 12))
        dist = R.u(150, 320)
        S.init(f"#{s}-g{k}", {"opacity": 0, "x": 0, "y": 0, "rotation": 0, "scale": 0.4})
        S.ft(f"#{s}-g{k}", {"opacity": 1, "x": 0, "y": 0, "rotation": 0, "scale": 1},
             {"opacity": 0, "x": r3(dist * math.cos(ang)), "y": r3(dist * math.sin(ang) + 120), "rotation": r3(R.u(-260, 260)), "scale": 0.6},
             tb + 0.02, R.u(0.55, 0.85), "power2.out")
    # ------------------------------------------------ mascot: in the video -> breaks out over the top edge
    inside = poly([(SX, SY), (SX + SW, SY), (SX + SW, SY), (SX + SW, SY), (SX + SW, 1180), (SX, 1180), (SX, SY), (SX, SY)])
    broken = poly([(-400, -400), (1480, -400), (1480, SY), (SX + SW, SY), (SX + SW, 1180), (SX, 1180), (SX, SY), (-400, SY)])
    S.mc([(t0, {"clipPath": inside}, None)])
    S.mset("#m-clip", {"clipPath": broken}, tb)
    S.mv([(t0, A, None), (tb, dict(A, fy=A["fy"] + 6), "sine.inOut"), (tb + 0.24, dict(B, fy=B["fy"] + 40), "power3.out"),
          (tb + 0.54, B, "back.out(1.8)"), (t1, dict(B, yaw=3), "sine.inOut")])
    no_sh = "drop-shadow(0px 0px 0px rgba(5,8,25,0))"
    sh = "drop-shadow(0px 22px 18px rgba(5,8,25,0.6))"
    S.mx([(t0, {"filter": no_sh}, None), (tb, {"filter": no_sh}, "none"), (tb + 0.3, {"filter": sh}, "power2.out")])
    S.act("armL", [(t0, "low", 0.3), (tb - 0.12, "wave", 0.28), (tb + 1.4, "explainHi", 0.4), (t0 + 3.4, "wave", 0.35), (t0 + 4.3, "explainHi", 0.4)])
    S.act("armR", [(t0, "low", 0.3), (tb - 0.1, "wave", 0.28), (tb + 1.5, "explainHi", 0.4), (t0 + 3.5, "pointUp", 0.35), (t0 + 4.4, "explainHi", 0.4)])
    S.act("head", [(t0, [-0.12, 0, 0], 0.3), (tb, [0.1, 0, 0], 0.25), (tb + 0.4, [-0.05, 0.08, 0.06], 0.4), (t0 + 2.6, [-0.02, -0.15, -0.05], 0.5),
                   (t0 + 3.8, [-0.06, 0.12, 0.04], 0.5)])
    S.act("torso", [(tb, {"chest": [-0.06, 0, 0]}, 0.3), (tb + 0.5, {"chest": [0.02, 0, 0]}, 0.5)])
