"""S05 — HIDDEN UNICODE CAVEAT (W57 – W68). "Karakter tak terlihat dalam teks pun belum tentu merupakan watermark AI."
A clean editor card; a UV scan bar passes and reveals tiny invisible-character marks between the words. Then a physical
stamp lands on the card: BUKAN BUKTI OTOMATIS (the marks are NOT presented as any vendor's watermark)."""
from kit_hm import floor, stamp, stamp_in, chip, MAT, SIDE_R
from xk import box


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    words = ["Halo,", "ini", "contoh", "teks", "biasa."]
    line, x = "", 40
    for k, w in enumerate(words):
        line += f'<span style="font:400 44px/1 Poppins;color:#0A0D2C">{w}</span>'
        if k < len(words) - 1:
            line += (f'<span id="{s}-mk{k}" style="display:inline-block;width:18px;height:34px;margin:0 8px;vertical-align:-4px;border-radius:5px;'
                     f'background:rgba(120,90,255,.18);border:2px solid rgba(110,80,240,.85);box-shadow:0 0 10px rgba(130,100,255,.6);opacity:0"></span>')
    S.back.append(f'<div class="abs" id="{s}-ed" style="{box(70, 640, 700, 420)}border-radius:26px;{MAT["porcelain"]}">'
                  f'<div class="abs" style="left:0;top:0;width:700px;height:64px;border-radius:26px 26px 0 0;background:rgba(41,75,119,.08)"></div>'
                  + "".join(f'<div class="abs" style="left:{28 + 30 * i}px;top:24px;width:16px;height:16px;border-radius:50%;background:rgba(41,75,119,{.25 - .06 * i})"></div>' for i in range(3))
                  + f'<div class="abs" style="left:40px;top:150px;width:640px;white-space:nowrap">{line}</div>'
                  f'<div class="abs" style="left:40px;top:250px;width:480px;height:14px;border-radius:7px;background:rgba(41,75,119,.14)"></div>'
                  f'<div class="abs" style="left:40px;top:290px;width:360px;height:14px;border-radius:7px;background:rgba(41,75,119,.10)"></div>'
                  f'<div class="abs" id="{s}-uv" style="left:-20px;top:70px;width:740px;height:10px;border-radius:5px;opacity:0;'
                  f'background:linear-gradient(90deg,rgba(130,100,255,0),rgba(170,150,255,.95),rgba(130,100,255,0));box-shadow:0 0 22px rgba(140,110,255,.8)"></div>'
                  f'<div class="abs" id="{s}-stamp" style="left:150px;top:300px;padding:10px 26px;border-radius:14px;border:4px solid #294B77;'
                  f'font:700 36px/1.1 Poppins;color:#0A0D2C;background:rgba(255,255,255,.75);transform:rotate(-7deg)">BUKAN BUKTI OTOMATIS</div></div>')
    S.back.append(chip(f"{s}-lab", 90, 1110, "KARAKTER TAK TERLIHAT", size=30))
    S.front.append(stamp(f"{s}-st", 540, 452, "BUKAN BUKTI OTOMATIS", 44))
    S.init(f"#{s}-ed", {"opacity": 0, "y": 40})
    S.ft(f"#{s}-ed", {"opacity": 0, "y": 40}, {"opacity": 1, "y": 0}, S.t0, 0.45, "power3.out")
    S.ft(f"#{s}-uv", {"opacity": 0, "y": 0}, {"opacity": 1, "y": 0}, W(57), 0.1, "none")
    S.ft(f"#{s}-uv", {"y": 0}, {"y": 300}, W(57) + 0.1, 0.9, "sine.inOut")
    S.ft(f"#{s}-uv", {"opacity": 1}, {"opacity": 0}, W(57) + 1.0, 0.2, "none")
    for k in range(4):
        S.ft(f"#{s}-mk{k}", {"opacity": 0, "scale": 0.4}, {"opacity": 1, "scale": 1}, W(58) + 0.08 * k, 0.3, "back.out(2)")
    S.fx(W(58), "sparkle", 0.05)
    S.init(f"#{s}-lab", {"opacity": 0, "x": -30})
    S.ft(f"#{s}-lab", {"opacity": 0, "x": -30}, {"opacity": 1, "x": 0}, W(59), 0.4, "power3.out")
    S.init(f"#{s}-stamp", {"opacity": 0, "scale": 1.6})
    S.ft(f"#{s}-stamp", {"opacity": 0, "scale": 1.6}, {"opacity": 1, "scale": 1}, W(63) - 0.05, 0.22, "power4.in")
    S.ft(f"#{s}-ed", {"y": 0}, {"y": 6}, W(63) + 0.17, 0.08, "power2.out")
    S.ft(f"#{s}-ed", {"y": 6}, {"y": 0}, W(63) + 0.25, 0.3, "power2.out")
    S.fx(W(63) + 0.15, "click", 0.08)
    stamp_in(S, f"{s}-st", W(63))
    S.cam([(S.t0, {"scale": 1.0}, None), (S.t1, {"scale": 1.05}, "sine.inOut")])
    S.mv([(S.t0, dict(SIDE_R, fx=900, fy=1790, h=880), None)])
    S.intent(W(57), "thinking", "right")
    S.intent(W(63), "emphasize", "left")
