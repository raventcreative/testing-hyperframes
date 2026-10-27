"""S20 — 19 PHONE MOCKUP (32.07–33.30)  VO: "ke tampilan HP."
Opens on S19's end: the 2.0x face clipped to the phone outline, corner guides on its corners. The navy-porcelain
phone materialises around it (sidewall thickness, side buttons, bezel, camera island, glass reflection, contact
shadow) while the shot inside pulls back to a small framing on the screen with a mini effect header -> our own
footage playing on a phone. 'tampilan': the phone turns a little to show its depth; 'HP.': it flips on its
vertical axis (mascot screen turns with it) and its back grows into the checklist board (BOARD) = S21's start."""
from xk import box, r3, CYAN, clip_rect
from kit import PHONE, BOARD, corner_frame
from kit_d import board_surface

PERSP = 1600


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W91, W92 = S.W(91), S.W(92)            # tampilan 32.22, HP. 32.72
    px, py, pw, ph, pr = PHONE
    ins = 18
    sx, sy, sw, sh, sr = px + ins, py + ins, pw - 2 * ins, ph - 2 * ins, pr - ins
    cx, cy = px + pw / 2, py + ph / 2
    f0, f1 = W92 + 0.02, W92 + 0.24        # flip: front 0 -> 90
    b1 = f1 + 0.16                         # back -90 -> 0
    # ---------------------------------------------------------------- back layer: shadow, phone body + screen bg, phone back -> board
    S.back.append(f'<div class="abs cshadow" id="{s}-sh" style="{box(px - 40, py + ph - 30, pw + 80, 90)}"></div>')
    body = []
    for k in range(9, 0, -1):     # sidewall thickness
        c = "#0a1a38" if k > 6 else "#122a52" if k > 3 else "#1c3a66"
        body.append(f'<div class="abs" style="{box(0, 0, pw, ph)}border-radius:{pr}px;background:{c};transform:translateZ({-k * 3}px)"></div>')
    body.append(f'<div class="abs por" style="{box(0, 0, pw, ph)}border-radius:{pr}px"></div>')
    for (yy, hh) in ((230, 110), (370, 70), (460, 70)):
        body.append(f'<div class="abs metal" style="{box(pw - 3, yy, 8, hh)}border-radius:4px"></div>')
    body.append(f'<div class="abs metal" style="{box(-5, 300, 8, 150)}border-radius:4px"></div>')
    # screen recess + screen content (mini header like the real video)
    body.append(f'<div class="abs" style="{box(ins - 2, ins - 2, sw + 4, sh + 4)}border-radius:{sr + 2}px;background:#03081a;transform:translateZ(-1px)"></div>')
    body.append(f'<div class="abs" style="{box(ins, ins, sw, sh)}border-radius:{sr}px;overflow:hidden;background:radial-gradient(ellipse at 30% 25%,#2a5c99 0%,#13305f 45%,#08132e 100%)">'
                f'<div class="abs" style="left:30px;top:74px;width:150px;font:700 13px/16px Poppins;color:#fff;letter-spacing:.06em">AI PRENEUR</div>'
                f'<div class="abs" style="left:30px;top:100px;width:34px;height:34px;border-radius:17px;border:1.5px solid {CYAN};font:700 14px/31px Poppins;color:#fff;text-align:center">19</div>'
                f'<div class="abs" style="left:74px;top:102px;width:300px;font:700 20px/30px Poppins;color:#fff">PHONE MOCKUP</div>'
                + "".join(f'<div class="abs" style="left:{74 + i * 10}px;top:136px;width:5px;height:5px;border-radius:3px;background:{CYAN if i < 19 else "rgba(255,255,255,.3)"}"></div>' for i in range(20))
                + f'<div class="abs" style="left:0;top:{sh - 120}px;width:{sw}px;height:120px;background:linear-gradient(180deg,rgba(3,8,28,0),rgba(3,8,28,.55))"></div>'
                f'<div class="abs" style="left:40px;top:{sh - 92}px;width:{sw - 80}px;font:400 21px/28px Poppins;color:#fff;text-align:center">masuk ke tampilan <b style="color:{CYAN}">HP.</b></div>'
                + "</div>")
    S.back.append(f'<div class="abs p3" id="{s}-ph" style="{box(px, py, pw, ph)}">' + "".join(body) + "</div>")
    bx, by, bw, bh, br = BOARD
    S.back.append(f'<div class="abs" id="{s}-bk" style="{box(0, 0, 1080, 1920)}">' + board_surface(s)
                  + f'<div class="abs" id="{s}-cam" style="{box(bx + 34, by + 34, 150, 150)}border-radius:44px;background:linear-gradient(150deg,#2a4f82,#10264b);'
                    f'box-shadow:inset 2px 2px 0 rgba(255,255,255,.25),0 10px 20px rgba(3,8,28,.6)">'
                  + "".join(f'<div class="abs" style="{box(ox, oy, 52, 52)}border-radius:26px;background:radial-gradient(circle at 40% 35%,#3a5a8a,#050b1f 60%);box-shadow:0 0 0 4px #8b97aa"></div>'
                            for ox, oy in ((18, 18), (80, 18), (18, 80)))
                  + "</div></div>")
    # ---------------------------------------------------------------- front layer: glass, island, bezel rim, closing guides
    S.front.append(f'<div class="abs" id="{s}-phf" style="{box(px, py, pw, ph)}">'
                   f'<div class="abs" style="{box(ins, ins, sw, sh)}border-radius:{sr}px;overflow:hidden;border:1.5px solid rgba(255,255,255,.22)">'
                   f'<div class="abs" style="left:-80px;top:-60px;width:{sw * 0.55}px;height:{sh + 120}px;transform:rotate(16deg);'
                   f'background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.13) 50%,rgba(255,255,255,0))"></div>'
                   f'<div class="abs" id="{s}-sheen" style="left:-260px;top:-80px;width:120px;height:{sh + 160}px;transform:rotate(16deg);'
                   f'background:linear-gradient(90deg,rgba(255,255,255,0),rgba(220,250,255,.35) 50%,rgba(255,255,255,0))"></div></div>'
                   f'<div class="abs" style="{box(pw / 2 - 64, ins + 16, 128, 36)}border-radius:18px;background:#03081a;box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)">'
                   f'<div class="abs" style="left:92px;top:9px;width:18px;height:18px;border-radius:9px;background:radial-gradient(circle at 40% 35%,#2b4d80,#03081a 70%)"></div></div>'
                   f'</div>')
    S.front.append(f'<div class="abs" id="{s}-gd" style="{box(0, 0, 1080, 1920)}">' + corner_frame(f"{s}-gd", px, py, pw, ph, arm=80, th=5) + "</div>")

    # ---------------------------------------------------------------- motion
    turn = {"transformOrigin": f"{pw / 2}px {ph / 2}px", "transformPerspective": PERSP}
    for sel in (f"#{s}-ph", f"#{s}-phf"):
        S.init(sel, dict(turn, rotationY=0, opacity=0, scale=1.03))
        S.ft(sel, {"opacity": 0, "scale": 1.03}, {"opacity": 1, "scale": 1}, t0, 0.2, "power2.out")
        S.ft(sel, {"rotationY": 0}, {"rotationY": -12}, W91, f0 - W91, "sine.inOut")
        S.ft(sel, {"rotationY": -12}, {"rotationY": 90}, f0, f1 - f0, "power2.in")
        S.tset(sel, {"opacity": 0}, f1)
    S.init(f"#{s}-sh", {"opacity": 0, "scaleX": 1})
    S.ft(f"#{s}-sh", {"opacity": 0}, {"opacity": 0.9}, t0, 0.25, "power2.out")
    S.ft(f"#{s}-sh", {"opacity": 0.9, "scaleX": 1}, {"opacity": 0, "scaleX": 1.6}, f1, 0.3, "power2.inOut")
    S.init(f"#{s}-sheen", {"x": 0})
    S.ft(f"#{s}-sheen", {"x": 0}, {"x": sw + 420}, W91 + 0.05, 0.42, "power2.inOut")
    S.init(f"#{s}-gd", {"opacity": 1, "scale": 1, "transformOrigin": f"{cx}px {cy}px"})
    S.ft(f"#{s}-gd", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 1.05}, t0 + 0.06, 0.18, "power2.in")
    # phone back -> board: starts at the phone size edge-on, turns square, grows to the board
    k_sx, k_sy = pw / bw, ph / bh
    dy = (py + ph / 2) - (by + bh / 2)
    b0 = {"rotationY": -90, "scaleX": r3(k_sx), "scaleY": r3(k_sy), "y": r3(dy), "opacity": 0,
          "transformOrigin": "540px 830px", "transformPerspective": PERSP}
    S.init(f"#{s}-bk", b0)
    S.tset(f"#{s}-bk", {"opacity": 1}, f1)
    S.ft(f"#{s}-bk", {"rotationY": -90}, {"rotationY": 0}, f1, b1 - f1, "power2.out")
    S.ft(f"#{s}-bk", {"scaleX": r3(k_sx), "scaleY": r3(k_sy), "y": r3(dy)}, {"scaleX": 1, "scaleY": 1, "y": 0}, b1 - 0.04, t1 - b1 + 0.03, "power3.inOut")
    S.init(f"#{s}-cam", {"opacity": 1})
    S.ft(f"#{s}-cam", {"opacity": 1}, {"opacity": 0}, b1, t1 - b1 - 0.02, "power1.in")

    # ---------------------------------------------------------------- mascot: 2.0x face in the phone outline -> small framing on the screen, turns with the phone
    k0 = 3000
    v0 = {"fx": 540, "fy": r3(922 + 0.585 * k0), "h": r3(0.98 * k0), "yaw": 1, "pitch": 5}
    k1 = 760
    v1 = {"fx": 540, "fy": r3(sy + 440 + 0.585 * k1), "h": r3(0.98 * k1), "yaw": -6, "pitch": 4}
    S.mv([(t0, v0, None), (t0 + 0.4, v1, "power3.inOut"), (f0, dict(v1, yaw=4), "sine.inOut")])
    S.mset("V", {"vis": 0}, f1)
    S.mc([(t0, {"clipPath": clip_rect(px, py, pw, ph, pr)}, None), (t0 + 0.2, {"clipPath": clip_rect(sx, sy, sw, sh, sr)}, "power2.out")])
    S.mx([(t0, {"rotationY": 0, "transformOrigin": f"{cx}px {cy}px", "transformPerspective": PERSP}, None),
          (W91, {"rotationY": 0}, "none"), (f0, {"rotationY": -12}, "sine.inOut"), (f1, {"rotationY": 90}, "power2.in")])
    S.act("armL", [(t0, "low", 0.3), (W91 - 0.1, "present", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (W92 - 0.12, "wave", 0.25)])
    S.act("head", [(t0, [-0.04, 0.0, 0.0], 0.3), (W91, [-0.06, 0.18, 0.04], 0.3), (W92, [-0.02, -0.05, -0.05], 0.25)])
    S.fx(t0 + 0.04, "pop", 0.05)
    S.fx(f0, "whoosh", 0.06)
    S.fx(b1, "click", 0.05)
