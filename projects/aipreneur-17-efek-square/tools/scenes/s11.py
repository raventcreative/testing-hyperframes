"""S11 — PULL-BACK REVEAL (efek #11).
Opens on a face close-up. The camera pulls back 2.05x -> 1x in 0.55 s (ease in-out) and reveals that the shot was the
video inside an app window: left panel with 4 checked steps + a progress bar at 62 %. World and mascot camera are the
same affine move (world = CSS camera, mascot = real 3D camera + clip to the video rect), so they stay locked."""
from xk import box, r3, clip_rect, check_svg

WIN = (50, 80, 980, 920)           # app window (x, y, w, h)
VID = (410, 150, 590, 820)         # video area inside the window
VR = 24                            # video corner radius
END_VIEW = {"fx": 705, "fy": 1010, "h": 760, "yaw": -6, "pitch": 5}
FOCUS = (705, 1010 - 0.595 * 760)  # eyes in the end layout
S0 = 2.05
STEPS = ["Riset hook", "Tulis script", "Generate visual", "Edit & caption"]


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    tp = t0 + 0.4                   # pull-back starts
    te = tp + 0.55
    x0 = -S0 * (FOCUS[0] - 540)
    y0 = (520 - 540) - S0 * (FOCUS[1] - 540)

    def at(px, py, sc, ox, oy):
        return 540 + ox + sc * (px - 540), 540 + oy + sc * (py - 540)

    # ---------------------------------------------------------------- back: app window
    wx, wy, ww, wh = WIN
    vx, vy, vw, vh = VID
    rows = []
    for k, st in enumerate(STEPS):
        y = 250 + k * 92
        rows.append(f'<div class="abs" id="{s}-r{k}" style="{box(80, y, 300, 74)}border-radius:16px;background:#ffffff;box-shadow:0 0 0 1px rgba(41,75,119,.10),0 10px 18px -12px rgba(10,13,44,.35)">'
                    f'<div class="abs" style="left:14px;top:19px;width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#0A0D2C,#294B77)">'
                    f'<div class="abs" style="left:6px;top:6px;width:24px;height:24px">{check_svg(f"{s}-k{k}", "#ffffff", 3.4)}</div></div>'
                    f'<div class="abs" style="left:64px;top:0;width:230px;font:700 22px/74px Poppins, sans-serif;color:#0A0D2C;white-space:nowrap">{st}</div></div>')
    S.back.append(f'<div class="abs card" style="{box(wx, wy, ww, wh)}border-radius:34px"></div>'
                  + "".join(f'<div class="abs" style="{box(wx + 26 + k * 22, wy + 24, 12, 12)}border-radius:6px;background:{c}"></div>'
                            for k, c in enumerate(("rgba(41,75,119,.55)", "rgba(41,75,119,.35)", "rgba(41,75,119,.2)")))
                  + f'<div class="abs" style="{box(wx + 110, wy + 14, 300, 32)}"><span class="tx" style="font:700 20px/32px Poppins, sans-serif;letter-spacing:.06em">AIPRENEUR STUDIO</span></div>'
                  + f'<div class="abs" style="{box(80, 168, 300, 40)}"><span class="tx" style="font:700 28px/40px Poppins, sans-serif">Progress konten</span></div>'
                  + "".join(rows)
                  + f'<div class="abs" style="{box(80, 640, 300, 150)}border-radius:18px;background:linear-gradient(160deg,#ffffff,#eef3fb);box-shadow:0 0 0 1px rgba(41,75,119,.10)">'
                  f'<div class="abs" style="left:20px;top:18px;width:200px;font:400 20px/28px Poppins, sans-serif;color:#294B77">Selesai</div>'
                  f'<div class="abs" id="{s}-pct" style="left:180px;top:6px;width:100px;text-align:right;font:700 44px/52px Poppins, sans-serif;color:#0A0D2C">62%</div>'
                  f'<div class="abs" style="left:20px;top:84px;width:260px;height:18px;border-radius:9px;background:rgba(41,75,119,.14)"></div>'
                  f'<div class="abs" id="{s}-bar" style="left:20px;top:84px;width:{r3(260 * 0.62)}px;height:18px;border-radius:9px;background:linear-gradient(90deg,#294B77,#0A0D2C)"></div>'
                  f'<div class="abs" style="left:20px;top:114px;width:260px;font:400 17px/24px Poppins, sans-serif;color:#294B77">8 dari 13 konten</div></div>'
                  + f'<div class="abs" style="{box(80, 812, 300, 150)}border-radius:18px;border:2px dashed rgba(41,75,119,.25)">'
                  f'<div class="abs" style="left:20px;top:20px;width:260px;font:700 20px/28px Poppins, sans-serif;color:#294B77;opacity:.75">Berikutnya</div>'
                  f'<div class="abs" style="left:20px;top:56px;width:220px;height:14px;border-radius:7px;background:rgba(41,75,119,.14)"></div>'
                  f'<div class="abs" style="left:20px;top:84px;width:160px;height:14px;border-radius:7px;background:rgba(41,75,119,.10)"></div></div>'
                  # video area (the "footage" background)
                  + f'<div class="abs" style="{box(vx, vy, vw, vh)}border-radius:{VR}px;overflow:hidden;background:linear-gradient(165deg,#f4f8fe 0%,#dde8f6 60%,#cddbf0 100%)">'
                  f'<div class="abs" style="left:-120px;top:-60px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95),rgba(255,255,255,0) 65%)"></div>'
                  f'<div class="abs grid-fine" style="left:0;top:{vh - 300}px;width:{vw}px;height:300px;opacity:.6"></div></div>')
    # ---------------------------------------------------------------- front: video chrome (REC + scrub bar), never over the face
    S.front.append(f'<div class="abs" style="{box(vx + 22, vy + 22, 108, 40)}border-radius:20px;background:rgba(10,13,44,.72);color:#fff;font:700 18px/40px Poppins, sans-serif;text-align:center">'
                   f'<span id="{s}-rec" style="display:inline-block;width:12px;height:12px;border-radius:6px;background:#ff4d5e;margin-right:8px;vertical-align:0"></span>REC</div>')
    S.front.append(f'<div class="abs" style="{box(vx + 22, vy + vh - 70, vw - 44, 48)}border-radius:24px;background:rgba(10,13,44,.62)">'
                   f'<svg class="abs" style="left:16px;top:12px;width:24px;height:24px" viewBox="0 0 24 24"><path d="M6 4 L20 12 L6 20 Z" fill="#fff"/></svg>'
                   f'<div class="abs" style="left:56px;top:21px;width:{vw - 44 - 80}px;height:6px;border-radius:3px;background:rgba(255,255,255,.3)"></div>'
                   f'<div class="abs" id="{s}-scrub" style="left:56px;top:21px;width:{vw - 44 - 80}px;height:6px;border-radius:3px;background:#fff;transform-origin:0% 50%"></div></div>')

    # ---------------------------------------------------------------- motion: one locked pull-back
    start = {"scale": S0, "x": r3(x0), "y": r3(y0)}
    end = {"scale": 1, "x": 0, "y": 0}
    S.cam([(t0, start, None), (tp, start, "none"), (te, end, "power2.inOut")])
    fx0, fy0 = at(END_VIEW["fx"], END_VIEW["fy"], S0, x0, y0)
    v0 = dict(END_VIEW, fx=fx0, fy=fy0, h=END_VIEW["h"] * S0)
    S.mv([(t0, v0, None), (tp, v0, "none"), (te, END_VIEW, "power2.inOut"), (t1, dict(END_VIEW, yaw=4), "sine.inOut")])
    cx0, cy0 = at(vx, vy, S0, x0, y0)
    c0 = {"clipPath": clip_rect(cx0, cy0, vw * S0, vh * S0, VR * S0)}
    c1 = {"clipPath": clip_rect(vx, vy, vw, vh, VR)}
    S.mc([(t0, c0, None), (tp, c0, "none"), (te, c1, "power2.inOut")])
    # after the reveal: checks draw in, bar fills to 62 %, scrub advances, REC blinks
    for k in range(4):
        b = te + 0.1 + k * 0.12
        S.init(f"#{s}-k{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-k{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, b, 0.22, "power2.out")
        S.init(f"#{s}-r{k}", {"x": 0})
        S.ft(f"#{s}-r{k}", {"x": 0}, {"x": 6}, b, 0.1, "power2.out")
        S.ft(f"#{s}-r{k}", {"x": 6}, {"x": 0}, b + 0.1, 0.2, "power2.inOut")
    S.init(f"#{s}-bar", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-bar", {"scaleX": 0}, {"scaleX": 1}, te + 0.55, 0.6, "power2.out")
    S.init(f"#{s}-pct", {"opacity": 0, "y": 10})
    S.ft(f"#{s}-pct", {"opacity": 0, "y": 10}, {"opacity": 1, "y": 0}, te + 0.95, 0.3, "back.out(2)")
    S.init(f"#{s}-scrub", {"scaleX": 0.18})
    S.ft(f"#{s}-scrub", {"scaleX": 0.18}, {"scaleX": 0.62}, t0, t1 - t0 - 0.02, "none")
    S.init(f"#{s}-rec", {"opacity": 1})
    for n in range(5):
        S.ft(f"#{s}-rec", {"opacity": 1}, {"opacity": 0.15}, t0 + 0.5 + n * 0.9, 0.3, "sine.inOut")
        S.ft(f"#{s}-rec", {"opacity": 0.15}, {"opacity": 1}, t0 + 0.8 + n * 0.9, 0.3, "sine.inOut")

    # ---------------------------------------------------------------- mascot: talks to camera like the clip being edited
    S.act("head", [(t0, [-0.03, -0.06, 0.04], 0.01), (t0 + 0.2, [0.02, 0.04, -0.03], 0.4), (te + 0.1, [-0.06, -0.1, 0.04], 0.35),
                   (te + 0.9, [0.0, 0.1, -0.04], 0.35), (te + 1.8, [-0.06, -0.06, 0.03], 0.35), (te + 2.7, [0, 0.06, 0], 0.4)])
    S.act("armL", [(t0, "low", 0.01), (te + 0.05, "explain", 0.3), (te + 0.9, "palmUp", 0.3), (te + 1.8, "explainHi", 0.3), (te + 2.8, "low", 0.45)])
    S.act("armR", [(t0, "low", 0.01), (te + 0.15, "open", 0.3), (te + 1.1, "explain", 0.3), (te + 2.0, "together", 0.3), (te + 2.9, "low", 0.45)])
    S.act("torso", [(t0, {"chest": [0.02, 0, 0]}, 0.01), (te + 0.3, {"chest": [0.04, -0.05, 0.01]}, 0.35), (te + 1.6, {"chest": [0.03, 0.05, -0.01]}, 0.4)])
