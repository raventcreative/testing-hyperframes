"""S03 — UI WORLD. He lives inside a cream chat-app window. A row of 4 clip thumbnails drops in above his head one by
one (0.08 s stagger); a chat column of instructions runs beside him; his body sits at the bottom of the window
(clipped to it) and the line under him switches from text 1 to text 2 mid-clip."""
from xk import box, r3, clip_rect
from kit_a import vthumb, NAVY

WX, WY, WW, WH, WR = 36, 36, 1008, 1008, 30
BAR = 58
CREAM = "#FBF6EC"
TW, TH, TG = 226, 150, 16
TX0, TY = 68, WY + BAR + 26
V = {"fx": 735, "fy": 1205, "h": 880, "yaw": -6, "pitch": 5}    # hair top ~y350, eyes ~y680, chest ~y890
CLIPS = [("Hook 1", "0:12"), ("Hook 2", "0:09"), ("Hook 3", "0:14"), ("Hook 4", "0:11")]


def bubble(id_, y, text, me, w=330):
    bg = NAVY if me else "#ffffff"
    col = "#fff" if me else "#0A0D2C"
    x = 66 + (348 - w if me else 0)
    rad = "20px 20px 6px 20px" if me else "20px 20px 20px 6px"
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, 0)}height:auto;padding:14px 18px 15px;border-radius:{rad};background:{bg};'
            f'box-shadow:0 12px 24px -16px rgba(10,13,44,.45),0 0 0 1px rgba(41,75,119,.08);font:{700 if me else 400} 25px/1.3 Poppins;color:{col}">{text}</div>')


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    # ------------------------------------------------ window (back)
    S.back.append(f'<div class="abs" id="{s}-win" style="{box(WX, WY, WW, WH)}border-radius:{WR}px;background:{CREAM};overflow:hidden;'
                  f'box-shadow:0 40px 70px -40px rgba(10,13,44,.55),0 0 0 1px rgba(41,75,119,.12)">'
                  f'<div class="abs" style="left:0;top:0;width:{WW}px;height:{BAR}px;background:#f3ecdf;border-bottom:1px solid rgba(41,75,119,.10)"></div>'
                  + "".join(f'<div class="abs" style="left:{24 + i * 22}px;top:{BAR / 2 - 7}px;width:14px;height:14px;border-radius:7px;background:{c}"></div>'
                            for i, c in enumerate(("#e7a29a", "#e9cf8e", "#a9cf9e")))
                  + f'<div class="abs" style="left:0;top:0;width:{WW}px;text-align:center;font:700 22px/{BAR}px Poppins;color:#0A0D2C">AIpreneur Studio</div>'
                  f'<div class="abs" style="left:{WW - 140}px;top:14px;width:116px;height:30px;border-radius:15px;background:{NAVY};font:700 15px/30px Poppins;color:#fff;text-align:center;letter-spacing:.06em">AI AKTIF</div>'
                  # chat column panel
                  f'<div class="abs" style="left:18px;top:{BAR + TH + 52}px;width:380px;height:{WH - BAR - TH - 70}px;border-radius:22px;background:rgba(255,255,255,.55);border:1px solid rgba(41,75,119,.08)"></div>'
                  "</div>")
    # thumbnail slots (soft placeholders so frame 0 already reads as an app) + the clips that drop in
    row = []
    oy = WY + BAR   # the clips drop inside the window body (clipped under the title bar)
    for k, (t, d) in enumerate(CLIPS):
        x = TX0 + k * (TW + TG) - WX
        row.append(f'<div class="abs" style="{box(x, TY - oy, TW, TH)}border-radius:16px;border:2px dashed rgba(41,75,119,.22)"></div>')
        row.append(f'<div class="abs" id="{s}-t{k}" style="{box(x, TY - oy, TW, TH)}border-radius:16px;overflow:hidden;box-shadow:0 16px 26px -16px rgba(10,13,44,.55)">'
                   f'{vthumb(TW, TH, t, dur=d, light=(k % 2 == 1))}</div>')
    S.back.append(f'<div class="abs" style="{box(WX, oy, WW, TH + 70)}overflow:hidden">' + "".join(row) + "</div>")
    # ------------------------------------------------ chat column (front: arms may pass behind it, never the face)
    cy = TY + TH + 42
    S.front.append(bubble(f"{s}-m0", cy, "Potong video ini jadi 4 klip.", True, w=300))
    S.front.append(bubble(f"{s}-m1", cy + 112, "Siap. 4 klip sudah jadi, cek di atas.", False))
    S.front.append(bubble(f"{s}-m2", cy + 262, "Tambahin hook + caption.", True, w=300))
    S.front.append(f'<div class="abs" id="{s}-dots" style="{box(66, cy + 372, 92, 46)}border-radius:20px 20px 20px 6px;background:#fff;box-shadow:0 12px 24px -16px rgba(10,13,44,.45)">'
                   + "".join(f'<div class="abs" id="{s}-d{i}" style="left:{20 + i * 20}px;top:19px;width:10px;height:10px;border-radius:5px;background:#294B77"></div>' for i in range(3)) + "</div>")
    S.front.append(bubble(f"{s}-m3", cy + 372, "Beres. Hook &amp; caption siap posting.", False))
    S.front.append(f'<div class="abs" style="{box(66, WY + WH - 84, 348, 52)}border-radius:26px;background:#fff;border:1px solid rgba(41,75,119,.15);'
                   f'font:400 21px/52px Poppins;color:rgba(41,75,119,.6);padding-left:22px">Ketik instruksi...</div>'
                   f'<div class="abs" style="{box(368, WY + WH - 78, 40, 40)}border-radius:20px;background:{NAVY}"></div>')
    # text under the body: text 1 -> text 2
    for i, txt in enumerate(("Lagi motong 4 klip...", "4 klip siap posting")):
        S.front.append(f'<div class="abs" id="{s}-u{i}" style="left:470px;top:950px;width:540px;text-align:center">'
                       f'<span class="badge" style="font:700 34px/1.2 Poppins, sans-serif;padding:12px 26px;border-radius:16px">{txt}</span></div>')
    # ------------------------------------------------ motion
    for k in range(4):
        at = t0 + 0.45 + k * 0.08
        S.init(f"#{s}-t{k}", {"y": -150, "opacity": 0, "rotation": -4 + 2.5 * k})
        S.ft(f"#{s}-t{k}", {"y": -150, "opacity": 0, "rotation": -4 + 2.5 * k}, {"y": 0, "opacity": 1, "rotation": 0}, at, 0.5, "bounce.out")
    S.init(f"#{s}-m1", {"opacity": 0, "y": 18, "scale": 0.94, "transformOrigin": "0% 100%"})
    S.ft(f"#{s}-m1", {"opacity": 0, "y": 18, "scale": 0.94}, {"opacity": 1, "y": 0, "scale": 1}, t0 + 0.3, 0.3, "back.out(2)")
    S.init(f"#{s}-m2", {"opacity": 0, "y": 18, "scale": 0.94, "transformOrigin": "100% 100%"})
    S.ft(f"#{s}-m2", {"opacity": 0, "y": 18, "scale": 0.94}, {"opacity": 1, "y": 0, "scale": 1}, t0 + 1.6, 0.3, "back.out(2)")
    S.init(f"#{s}-dots", {"opacity": 0})
    S.tset(f"#{s}-dots", {"opacity": 1}, t0 + 2.0)
    for i in range(3):
        for c in range(2):
            a = t0 + 2.0 + c * 0.36 + i * 0.1
            S.ft(f"#{s}-d{i}", {"y": 0}, {"y": -7}, a, 0.13, "sine.out")
            S.ft(f"#{s}-d{i}", {"y": -7}, {"y": 0}, a + 0.13, 0.13, "sine.in")
    S.tset(f"#{s}-dots", {"opacity": 0}, t0 + 2.75)
    S.init(f"#{s}-m3", {"opacity": 0, "y": 18, "scale": 0.94, "transformOrigin": "0% 100%"})
    S.ft(f"#{s}-m3", {"opacity": 0, "y": 18, "scale": 0.94}, {"opacity": 1, "y": 0, "scale": 1}, t0 + 2.75, 0.3, "back.out(2)")
    mid = t0 + 2.75
    S.init(f"#{s}-u0", {"opacity": 1, "y": 0})
    S.ft(f"#{s}-u0", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -24}, mid - 0.05, 0.22, "power2.in")
    S.init(f"#{s}-u1", {"opacity": 0, "y": 24})
    S.ft(f"#{s}-u1", {"opacity": 0, "y": 24}, {"opacity": 1, "y": 0}, mid + 0.12, 0.3, "back.out(2)")
    # thumbs pulse once when the reply lands
    for k in range(4):
        S.ft(f"#{s}-t{k}", {"scale": 1}, {"scale": 1.05}, mid + 0.05 + k * 0.05, 0.14, "power2.out")
        S.ft(f"#{s}-t{k}", {"scale": 1.05}, {"scale": 1}, mid + 0.19 + k * 0.05, 0.25, "power2.inOut")
    # ------------------------------------------------ mascot: inside the window (clipped to it), body at the bottom
    S.mv([(t0, V, None), (t1, dict(V, yaw=-2), "sine.inOut")])
    S.mc([(t0, {"clipPath": clip_rect(WX, WY + BAR, WW, WH - BAR, WR)}, None)])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.45, "pointUp", 0.35), (t0 + 1.3, "low", 0.4), (mid, "palmUp", 0.35), (t0 + 4.0, "low", 0.45)])
    S.act("armR", [(t0, "low", 0.3), (t0 + 1.5, "point", 0.35), (t0 + 2.4, "low", 0.4), (mid + 0.1, "open", 0.35), (t0 + 4.1, "low", 0.45)])
    S.act("head", [(t0, [0, 0, 0], 0.3), (t0 + 0.4, [-0.2, 0.1, 0.02], 0.35), (t0 + 1.4, [0.02, -0.3, -0.03], 0.4),
                   (mid, [-0.04, 0.05, 0.05], 0.35), (t0 + 4.0, [0, -0.04, 0], 0.5)])
    S.act("torso", [(t0 + 1.4, {"chest": [0, -0.08, 0]}, 0.5), (mid, {"chest": [0.03, 0.04, 0]}, 0.4), (t0 + 4.0, {}, 0.5)])
