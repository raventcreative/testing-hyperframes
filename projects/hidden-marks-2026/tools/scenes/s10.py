"""S10 — READING THE RESULT (W109 – W120). "Kalau alatnya tidak menemukan sinyal, itu belum membuktikan file dibuat
manusia."  The station's output becomes three drawers: TERDETEKSI / TIDAK TERDETEKSI / TIDAK DIDUKUNG (no invented
numbers, no green truth badge). The middle one opens; the mascot steps forward (scene softens) for the disclaimer."""
from kit_hm import floor, drawer, stamp, stamp_in, MAT, SIDE_R, HALF, HALF_IN, blur_wrap, blur_in
from xk import box


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(f'<div class="abs" id="{s}-cab" style="{box(110, 560, 760, 640)}border-radius:34px;{MAT["alu"]}"></div>')
    for k, lab in enumerate(("TERDETEKSI", "TIDAK TERDETEKSI", "TIDAK DIDUKUNG")):
        S.back.append(drawer(f"{s}-d{k}", 150, 600 + 196 * k, 680, 168, lab))
    S.back.append(f'<div class="abs" id="{s}-q" style="{box(870, 830, 150, 110)}border-radius:22px;{MAT["glass"]}font:700 64px/110px Poppins;color:#294B77;text-align:center">?</div>')
    blur_wrap(S)
    S.front.append(stamp(f"{s}-st", 540, 452, "TIDAK TERDETEKSI ≠ MANUSIA", 42))
    for k in range(3):
        S.init(f"#{s}-d{k}", {"opacity": 0, "x": -80})
        S.ft(f"#{s}-d{k}", {"opacity": 0, "x": -80}, {"opacity": 1, "x": 0}, S.t0 + 0.1 * k, 0.45, "power3.out")
    S.ft(f"#{s}-d1", {"x": 0, "scale": 1}, {"x": 120, "scale": 1.04}, W(111), 0.45, "power3.out")      # "tidak menemukan"
    S.ft(f"#{s}-d1", {"boxShadow": "0 0 0 0 rgba(0,0,0,0)"}, {"boxShadow": "0 0 0 3px rgba(41,75,119,.55), 0 24px 40px -18px rgba(10,13,44,.5)"}, W(111), 0.4, "power2.out")
    S.fx(W(111), "click", 0.07)
    S.init(f"#{s}-q", {"opacity": 0, "scale": 0.6})
    S.ft(f"#{s}-q", {"opacity": 0, "scale": 0.6}, {"opacity": 1, "scale": 1}, W(112), 0.35, "back.out(1.8)")
    # mascot: watches from the right, then steps forward for the disclaimer
    S.mv([(S.t0, dict(SIDE_R, fx=910, fy=1820, h=860), None), (W(114) - 0.2, dict(SIDE_R, fx=910, fy=1820, h=860), None),
          (W(114) + 0.35, dict(HALF, yaw=0), "power3.inOut"), (S.t1, dict(HALF, yaw=0), "sine.inOut")])
    blur_in(S, W(114) - 0.1, 0.45)
    stamp_in(S, f"{s}-st", W(115))
    S.intent(W(109), "thinking", "left")
    S.intent(W(115), "emphasize", "right")
