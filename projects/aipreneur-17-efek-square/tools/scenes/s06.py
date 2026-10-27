"""S06 — PHONE MOCKUP. A phone (~40 % of the frame height) floats beside his head (never over the face): it enters
from the right rotating 12 -> -8 deg in 0.32 s, then floats +-5 px. Inside, a chat: 2 messages from me and 2 replies
pop in one by one. He turns to it and points."""
from xk import box, r3

PX, PY, PW, PH = 670, 150, 296, 580
MSGS = [(1, "Bisa bikinin konten 30 hari?"), (0, "Bisa! Pakai AI, 1 jam beres."), (1, "Serius? Gimana caranya?"), (0, "Pakai workflow AIpreneur.")]


def build(S):
    s, t0 = S.id, S.t0
    sw, sh = PW - 24, PH - 24
    bub = []
    y = 100
    for k, (mine, text) in enumerate(MSGS):
        hgt = 58
        if mine:
            st = (f"right:12px;top:{y}px;max-width:200px;padding:10px 14px;border-radius:16px 16px 4px 16px;"
                  f"background:linear-gradient(135deg,#0A0D2C,#294B77);color:#fff;transform-origin:100% 100%")
        else:
            st = (f"left:12px;top:{y}px;max-width:200px;padding:10px 14px;border-radius:16px 16px 16px 4px;"
                  f"background:#fff;color:#0A0D2C;box-shadow:0 4px 10px -4px rgba(10,13,44,.25);transform-origin:0% 100%")
        bub.append(f'<div class="abs" id="{s}-m{k}" style="{st};font:{700 if not mine else 400} 16px/1.35 Poppins, sans-serif">{text}</div>')
        y += hgt + 22
    typing = (f'<div class="abs" id="{s}-typ" style="left:12px;top:{y}px;width:62px;height:30px;border-radius:15px;background:#fff;'
              f'box-shadow:0 4px 10px -4px rgba(10,13,44,.25)">' +
              "".join(f'<div class="abs" id="{s}-td{i}" style="left:{13 + i * 13}px;top:12px;width:8px;height:8px;border-radius:4px;background:#294B77"></div>' for i in range(3)) + "</div>")
    screen = (f'<div class="abs" style="left:12px;top:12px;width:{sw}px;height:{sh}px;border-radius:30px;overflow:hidden;'
              f'background:linear-gradient(180deg,#f4f7fc 0%,#e8eef8 100%)">'
              f'<div class="abs" style="left:0;top:0;width:{sw}px;height:84px;background:#fff;box-shadow:0 1px 0 rgba(41,75,119,.12)">'
              f'<div class="abs" style="left:16px;top:38px;width:36px;height:36px;border-radius:17px;background:linear-gradient(135deg,#0A0D2C,#294B77);'
              f'font:700 13px/36px Poppins;color:#fff;text-align:center">AI</div>'
              f'<div class="abs" style="left:62px;top:36px;width:170px;font:700 16px/20px Poppins;color:#0A0D2C">AIpreneur</div>'
              f'<div class="abs" style="left:62px;top:57px;width:170px;font:400 12px/16px Poppins;color:#294B77">online</div></div>'
              + "".join(bub) + typing +
              f'<div class="abs" style="left:10px;top:{sh - 50}px;width:{sw - 20}px;height:38px;border-radius:19px;background:#fff;box-shadow:0 0 0 1px rgba(41,75,119,.12)">'
              f'<div class="abs" style="left:16px;top:0;width:150px;font:400 13px/38px Poppins;color:rgba(41,75,119,.55)">Ketik pesan...</div>'
              f'<div class="abs" style="left:{sw - 56}px;top:5px;width:28px;height:28px;border-radius:14px;background:linear-gradient(135deg,#0A0D2C,#294B77)"></div></div>'
              "</div>")
    phone = (f'<div class="abs" id="{s}-ph" style="{box(PX, PY, PW, PH)}">'
             f'<div class="abs" style="left:0;top:0;width:{PW}px;height:{PH}px;border-radius:42px;background:linear-gradient(150deg,#2c4f80 0%,#101f42 55%,#0A0D2C 100%);'
             f'box-shadow:inset 0 0 0 2px rgba(255,255,255,.18),0 40px 60px -26px rgba(10,13,44,.6)"></div>'
             + screen +
             f'<div class="abs" style="left:{PW / 2 - 40}px;top:20px;width:80px;height:20px;border-radius:10px;background:#0A0D2C"></div>'
             f'<div class="abs" style="left:18px;top:14px;width:70px;height:{PH - 60}px;border-radius:30px;background:linear-gradient(100deg,rgba(255,255,255,.22),rgba(255,255,255,0));opacity:.6"></div></div>')
    S.front.append(f'<div class="abs" id="{s}-flo" style="left:0;top:0;width:1080px;height:1080px">{phone}</div>')
    S.back.append(f'<div class="abs cshadow" id="{s}-sh" style="{box(PX - 10, PY + PH + 150, PW + 20, 50)}opacity:.5"></div>')

    a = t0 + 0.3
    S.init(f"#{s}-ph", {"x": 520, "rotation": 12, "opacity": 1, "transformOrigin": "50% 60%"})
    S.ft(f"#{s}-ph", {"x": 520, "rotation": 12}, {"x": 0, "rotation": -8}, a, 0.32, "power3.out")
    S.init(f"#{s}-sh", {"opacity": 0, "scale": 0.6})
    S.ft(f"#{s}-sh", {"opacity": 0, "scale": 0.6}, {"opacity": 0.5, "scale": 1}, a + 0.1, 0.3, "power2.out")
    # float +-5 px after landing (finite yoyo cycles)
    f0 = a + 0.32
    n = 4
    seg = (S.t1 - f0) / n
    S.init(f"#{s}-flo", {"y": 0})
    ys = [0, -5, 5, -5, 0]
    for i in range(n):
        S.ft(f"#{s}-flo", {"y": ys[i]}, {"y": ys[i + 1]}, f0 + i * seg, seg, "sine.inOut")
    # messages pop in one by one (typing dots before each reply)
    beats = [a + 0.55, a + 1.15, a + 1.95, a + 2.55]
    for k, b in enumerate(beats):
        S.init(f"#{s}-m{k}", {"opacity": 0, "scale": 0.6, "y": 10})
        S.ft(f"#{s}-m{k}", {"opacity": 0, "scale": 0.6, "y": 10}, {"opacity": 1, "scale": 1, "y": 0}, b, 0.26, "back.out(2.2)")
    S.init(f"#{s}-typ", {"opacity": 0, "y": 0})
    for k in (1, 3):
        S.tset(f"#{s}-typ", {"opacity": 1, "y": (k - 4) * 80}, beats[k] - 0.4)
        S.tset(f"#{s}-typ", {"opacity": 0}, beats[k] - 0.02)
    for i in range(3):
        S.init(f"#{s}-td{i}", {"y": 0})
        for st in (beats[1] - 0.4, beats[3] - 0.4):
            S.ft(f"#{s}-td{i}", {"y": 0}, {"y": -5}, st + i * 0.07, 0.12, "sine.out")
            S.ft(f"#{s}-td{i}", {"y": -5}, {"y": 0}, st + i * 0.07 + 0.12, 0.12, "sine.in")
    # mascot: left of centre, turns to the phone, points at it, reacts to the replies
    v = {"fx": 380, "fy": 1180, "h": 1050, "yaw": 0, "pitch": 5}
    S.mv([(t0, v, None), (a, dict(v, yaw=10), "sine.inOut"), (S.t1, dict(v, yaw=16), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.01), (a + 0.2, "point", 0.3), (beats[1] + 0.1, "palmUp", 0.3), (beats[3] + 0.05, "present", 0.35)])
    S.act("armR", [(t0, "low", 0.01), (beats[1] + 0.15, "chin", 0.4), (beats[3] + 0.1, "low", 0.4)])
    S.act("head", [(t0, [0, 0, 0], 0.01), (a + 0.05, [-0.05, 0.32, -0.04], 0.3), (beats[1], [-0.1, 0.3, -0.07], 0.35),
                   (beats[2], [0.02, 0.24, 0.03], 0.3), (beats[3], [-0.08, 0.34, -0.05], 0.3), (beats[3] + 0.6, [0.04, 0.1, 0.02], 0.4)])
    S.act("torso", [(t0, {}, 0.01), (a, {"chest": [0, 0.12, 0]}, 0.4)])
