"""S14 — 13 MAGAZINE COVER (25.57–26.47)  VO: "ke sampul majalah,"
Match cut on the viewfinder rect: S13's frame becomes the cover border. The cover page swings in on its left
spine (paper thickness visible) and lands square; the mascot - back to full 3D, lit like a cover shoot - is
printed on it: masthead BEHIND the head, cover lines IN FRONT (real cover layering). Original AIpreneur-style
cover, Poppins hierarchy, only words from the VO / effect labels. Hand-off: a gloss band sweeps the cover and
leaves a curved glass highlight -> S15 liquid glass."""
from xk import box, r3, CYAN, clip_rect
from kit import COVER, NO_FILTER, corner_frame

PERSP = 1700


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W70, W71 = S.W(70), S.W(71)          # sampul 25.70, majalah 26.00
    x, y, w, h = COVER
    land = t0 + 0.3
    # ---------------------------------------------------------------- back: dim world, page underneath, cover page + masthead
    S.back.append(f'<div class="abs" id="{s}-dim" style="{box(0, 0, 1080, 1920)}background:rgba(6,13,36,.82)"></div>')
    S.back.append(f'<div class="abs" style="{box(x, y, w, h)}border-radius:6px;background:linear-gradient(160deg,#0f2246,#081430);'
                  f'box-shadow:inset 0 0 0 2px rgba(255,255,255,.12)"></div>')
    page = []
    for k in range(3, 0, -1):   # stacked page edges (thickness) on the open side
        page.append(f'<div class="abs" style="left:{k * 3}px;top:{k * 3}px;width:{w}px;height:{h}px;border-radius:6px;background:{["#e9e3d6", "#d9d1c0", "#c9bfab"][k - 1]}"></div>')
    page.append(f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;border-radius:6px;overflow:hidden;'
                f'background:linear-gradient(165deg,#2c62a3 0%,#173d72 48%,#0c2551 100%)">'
                f'<div class="abs" style="left:-120px;top:{h * 0.52}px;width:{w + 240}px;height:150px;background:linear-gradient(90deg,#00b8e6,#00D0FE);transform:rotate(-14deg);opacity:.9"></div>'
                f'<div class="abs" style="left:-120px;top:{h * 0.52 + 170}px;width:{w + 240}px;height:18px;background:#fbf8f1;transform:rotate(-14deg);opacity:.85"></div>'
                f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;background:radial-gradient(ellipse at 30% 25%,rgba(255,255,255,.22),rgba(255,255,255,0) 55%)"></div>'
                f'<div class="abs" style="left:34px;top:14px;width:{w - 68}px;font:700 236px/1 Poppins;letter-spacing:-0.035em;color:#fff;text-align:center">EFEK</div>'
                f'<div class="abs" style="left:40px;top:262px;width:{w - 80}px;height:3px;background:rgba(255,255,255,.7)"></div>'
                f'<div class="abs" style="left:40px;top:272px;width:{w - 80}px;font:400 22px/30px Poppins;color:#fff;letter-spacing:.14em;display:flex;justify-content:space-between">'
                f'<span>NO. 13</span><span>EDISI 20 EFEK</span><span>SATU KLIP</span></div></div>')
    S.back.append(f'<div class="abs" id="{s}-page" style="{box(x, y, w, h)}">' + "".join(page) + "</div>")
    # ---------------------------------------------------------------- front: cover lines over the mascot, barcode, gloss
    lines = (f'<div class="abs" style="left:38px;top:{h - 330}px;width:420px;font:700 30px/1.1 Poppins;color:#fff;letter-spacing:.06em">SATU KLIP</div>'
             f'<div class="abs" style="left:34px;top:{h - 292}px;width:460px;font:700 92px/1 Poppins;color:{CYAN};letter-spacing:-0.02em;text-shadow:0 4px 18px rgba(3,8,28,.6)">20 EFEK</div>'
             f'<div class="abs" style="left:38px;top:{h - 188}px;width:400px;font:400 27px/1.3 Poppins;color:#fff;text-shadow:0 2px 10px rgba(3,8,28,.8)">Paper Cutout<br>Dolly Zoom<br>Liquid Glass</div>'
             f'<div class="abs" style="left:{w - 200}px;top:{h - 140}px;width:160px;height:104px;border-radius:4px;background:#fbf8f1;padding:10px">'
             + "".join(f'<div class="abs" style="left:{12 + k * 6.6}px;top:12px;width:{(2, 4, 1.5, 3)[k % 4]}px;height:64px;background:#0b1636"></div>' for k in range(20))
             + f'<div class="abs" style="left:12px;top:80px;width:136px;font:400 14px/14px Poppins;color:#0b1636;letter-spacing:.2em">2026 · 13</div></div>'
             f'<div class="abs" style="left:{w - 230}px;top:330px;width:200px;height:200px;border-radius:100px;background:{CYAN};transform:rotate(12deg);'
             f'box-shadow:0 10px 24px rgba(3,8,28,.5);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">'
             f'<div style="font:700 26px/1 Poppins;color:#0b1636;letter-spacing:.06em">LIHAT</div><div style="font:700 34px/1.05 Poppins;color:#fff">HASIL-<br>NYA</div></div>')
    S.front.append(f'<div class="abs" id="{s}-lines" style="{box(x, y, w, h)}">{lines}</div>')
    S.front.append(f'<div class="abs" id="{s}-glossw" style="{box(x, y, w, h)}border-radius:6px;overflow:hidden">'
                   f'<div class="abs" id="{s}-gloss" style="left:-420px;top:-200px;width:300px;height:{h + 400}px;transform:rotate(18deg);'
                   f'background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.55) 45%,rgba(190,245,255,.65) 52%,rgba(255,255,255,0))"></div></div>')
    S.front.append(f'<div class="abs" id="{s}-vf" style="{box(0, 0, 1080, 1920)}">' + corner_frame(f"{s}-vf", x - 8, y - 8, w + 16, h + 16, arm=90, th=6) + "</div>")

    # ---------------------------------------------------------------- motion: page turn on the spine (left edge)
    turn = {"rotationY": -84, "transformOrigin": f"0px {h / 2}px", "transformPerspective": PERSP}
    flat = {"rotationY": 0}
    for sel in (f"#{s}-page", f"#{s}-lines"):
        S.init(sel, turn)
        S.ft(sel, {"rotationY": -84}, flat, t0 + 0.0, 0.3, "power3.out")
    S.init(f"#{s}-glossw", {"opacity": 0})
    S.tset(f"#{s}-glossw", {"opacity": 1}, land)
    S.init(f"#{s}-gloss", {"x": 0})
    S.ft(f"#{s}-gloss", {"x": 0}, {"x": w + 700}, W71 + 0.12, 0.42, "power2.inOut")
    S.init(f"#{s}-vf", {"opacity": 1, "scale": 1, "transformOrigin": f"{x + w / 2}px {y + h / 2}px"})
    S.ft(f"#{s}-vf", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 1.06}, land - 0.05, 0.2, "power2.in")
    S.init(f"#{s}-dim", {"opacity": 1})
    S.ft(f"#{s}-dim", {"opacity": 1}, {"opacity": 0.35}, land, 0.4, "power2.out")
    # a slow push on the finished cover (applied to the cover and the mascot together)
    S.cam([(t0, {"scale": 1}, None), (land, {"scale": 1}, "none"), (t1, {"scale": 1.035}, "sine.inOut")])

    # ---------------------------------------------------------------- mascot: the cover photo (clipped, full 3D, cover key light)
    v = {"fx": 540, "fy": 1660, "h": 1190, "yaw": -8, "pitch": 4}
    S.mv([(t0, v, None), (t1, dict(v, yaw=6), "sine.inOut")])
    S.mc([(t0, {"clipPath": clip_rect(x, y, w, h, 6)}, None)])
    S.mx([(t0, {"rotationY": -84, "transformOrigin": f"{x}px {y + h / 2}px", "transformPerspective": PERSP, "filter": NO_FILTER, "scale": 1}, None),
          (t0 + 0.3, {"rotationY": 0}, "power3.out")])
    # follow the cover push (cam scale is around 540,960; mirror it on the wrapper after the page lands)
    S.mset("#m-xf", {"transformOrigin": "540px 960px"}, land)
    S.mx([(land, {"scale": 1, "rotationY": 0}, None), (t1, {"scale": 1.035}, "sine.inOut")])
    S.fx(t0 + 0.04, "whoosh", 0.06)
    S.fx(land - 0.02, "pop", 0.06)
    S.fx(W71 + 0.2, "sparkle", 0.04)
