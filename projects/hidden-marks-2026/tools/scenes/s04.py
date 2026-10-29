"""S04 — WATERMARK IN THE CONTENT (W41 – W57). "Kedua, watermark yang tertanam di dalam kontennya. Ini gak otomatis
hilang cuma karena label filenya dibuang."  The camera passes through the glass into the artwork itself: pixel fabric
fills the frame and the woven signal lattice is part of it (illustrative metaphor, not a real algorithm). The mascot
steps in front (background softens) and shakes his head on "gak otomatis hilang"; the C2PA label drops into a bin
while the lattice in the pixels keeps glowing."""
from kit_hm import stamp, stamp_in, chip, ART, MAT, HALF, HALF_IN, blur_wrap, blur_in
from xk import box

BIG_PIX = ("background-image:linear-gradient(rgba(255,255,255,.22) 2px,transparent 2px),"
           "linear-gradient(90deg,rgba(255,255,255,.22) 2px,transparent 2px);background-size:54px 54px;")
BIG_SIG = ("background-image:radial-gradient(circle,rgba(225,238,255,.95) 0 5px,transparent 7px),"
           "repeating-linear-gradient(45deg,rgba(220,235,255,0) 0 40px,rgba(220,235,255,.28) 40px 44px,rgba(220,235,255,0) 44px 108px);"
           "background-size:108px 108px,auto;")


def build(S):
    s, W = S.id, S.W
    S.back.append(f'<div class="abs" id="{s}-macro" style="{box(-60, 420, 1200, 1300)}border-radius:40px;{ART}overflow:hidden">'
                  f'<div class="abs" style="inset:0;{BIG_PIX}"></div><div class="abs" id="{s}-sig" style="inset:0;{BIG_SIG}"></div></div>')
    S.back.append(chip(f"{s}-lab", 250, 1500, "WATERMARK DI KONTEN", dark=True, size=34))
    S.front.append(f'<div class="abs" id="{s}-badge" style="{box(720, 380, 200, 124)}border-radius:16px;{MAT["porcelain"]}">'
                   f'<div class="abs" style="left:18px;top:16px;font:700 32px/1 Poppins;color:#0A0D2C">C2PA</div>'
                   f'<div class="abs" style="left:18px;top:62px;width:130px;height:10px;border-radius:5px;background:rgba(41,75,119,.3)"></div></div>')
    S.front.append(f'<div class="abs" id="{s}-bin" style="{box(760, 1640, 200, 120)}border-radius:20px 20px 30px 30px;{MAT["alu"]}">'
                   f'<div class="abs" style="left:20px;top:14px;width:160px;height:16px;border-radius:8px;background:#0b1020"></div></div>')
    S.front.append(stamp(f"{s}-st", 540, 452, "GAK OTOMATIS HILANG", 44))
    # pass through the glass into the pixels: the macro plate starts as the file's artwork size and fills the frame
    m = f"#{s}-macro"
    S.init(m, {"scale": 0.33, "rotationY": 20, "transformPerspective": 1400, "borderRadius": "40px"})
    S.ft(m, {"scale": 0.33, "rotationY": 20}, {"scale": 1.05, "rotationY": 0}, S.t0, 0.95, "power3.inOut")
    S.ft(m, {"scale": 1.05}, {"scale": 1.12}, S.t0 + 0.95, S.t1 - S.t0 - 0.95, "sine.inOut")
    S.fx(S.t0 + 0.1, "whoosh", 0.06)
    S.ft(f"#{s}-sig", {"opacity": 0.35}, {"opacity": 1}, W(44), 0.5, "power2.out")          # "tertanam"
    S.fx(W(44), "sparkle", 0.05)
    S.init(f"#{s}-lab", {"opacity": 0, "y": 30})
    S.ft(f"#{s}-lab", {"opacity": 0, "y": 30}, {"opacity": 1, "y": 0}, W(42), 0.4, "power3.out")
    # mascot steps in front, background softens
    # he rises into frame from below (no wrapper opacity fade: a partially transparent 3D-filtered WebGL layer
    # stalls Chrome's software compositor during capture)
    S.mv([(S.t0, dict(HALF_IN, fy=3500, vis=1), None), (W(48) - 0.5, dict(HALF_IN, fy=3500, vis=1), None),
          (W(48) - 0.02, dict(HALF, yaw=-3), "power3.out"), (S.t1, dict(HALF, yaw=2), "sine.inOut")])
    # background softens by fading the pixel plate (a CSS blur on this huge 3D plate stalls Chrome's software renderer)
    S.ft(m, {"opacity": 1}, {"opacity": 0.42}, W(48) - 0.45, 0.45, "power2.inOut")
    stamp_in(S, f"{s}-st", W(50))
    # the label is thrown away ... the lattice stays
    b = f"#{s}-badge"
    S.init(b, {"opacity": 0})
    S.ft(b, {"opacity": 0, "y": -60}, {"opacity": 1, "y": 0}, W(53), 0.25, "power2.out")
    S.ft(b, {"y": 0, "rotation": 0}, {"y": 1280, "rotation": 24}, W(55), 0.55, "power2.in")
    S.ft(b, {"opacity": 1}, {"opacity": 0}, W(55) + 0.5, 0.06, "none")
    S.init(f"#{s}-bin", {"y": 200})
    S.ft(f"#{s}-bin", {"y": 200}, {"y": 0}, W(53), 0.4, "power3.out")
    S.fx(W(56), "click", 0.07)
    S.intent(W(48), "emphasize", "left")
    S.intent(W(53), "explain", "right")
