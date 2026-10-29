"""S02 — ONE FILE, TWO LAYERS (W7 – W23). "Lihat file ini. Dari luar kelihatan biasa. Tapi pas dibedah, ada dua
lapisan yang sering ketuker."  The same glass file turns on its axis; on "dibedah" it separates in depth: the glass
shell (METADATA) comes forward, the pixel artwork (WATERMARK) drops back; an aluminium separation ring holds them
apart. On "ketuker" the two labels cross over (the mix-up) and snap back."""
from kit_hm import floor, glass_file, stamp, stamp_in, spec_sweep, chip, MAT, SIDE_R
from xk import box


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(glass_file(f"{s}-file", 200, 640, 440, 560, badge=False, sig_op=0.85))
    S.back.append(f'<div class="abs" id="{s}-ring" style="{box(150, 600, 540, 640)}border-radius:40px;border:6px solid #c9d1dc;'
                  f'box-shadow:inset 0 0 0 2px rgba(255,255,255,.9),0 0 0 2px rgba(10,13,44,.18);opacity:0"></div>')
    S.front.append(chip(f"{s}-cm", 60, 560, "METADATA", dark=True, size=32))
    S.front.append(chip(f"{s}-cw", 470, 1225, "WATERMARK", dark=False, size=32))
    S.front.append(stamp(f"{s}-st", 540, 452, "DUA LAPISAN", 46))
    S.init(f"#{s}-file", {"rotationY": -16, "rotationX": 6, "transformPerspective": 1400})
    S.ft(f"#{s}-file", {"rotationY": -16}, {"rotationY": -30}, S.t0, W(16) - S.t0, "sine.inOut")
    spec_sweep(S, f"{s}-file", W(7) - 0.1, 0.6)
    # dissect: shell forward, artwork back (real depth inside the file's own 3D space)
    S.ft(f"#{s}-file-shell", {"z": 0, "x": 0, "y": 0}, {"z": 150, "x": -70, "y": -50}, W(16), 0.7, "power3.inOut")
    S.ft(f"#{s}-file-art", {"x": 0, "y": 0}, {"x": 70, "y": 60}, W(16) + 0.06, 0.7, "power3.inOut")
    S.ft(f"#{s}-ring", {"opacity": 0, "scale": 0.9}, {"opacity": 1, "scale": 1}, W(16) + 0.25, 0.45, "power2.out")
    S.fx(W(16), "whoosh", 0.05)
    for c, x0 in ((f"#{s}-cm", -40), (f"#{s}-cw", 40)):
        S.init(c, {"opacity": 0, "x": x0})
        S.ft(c, {"opacity": 0, "x": x0}, {"opacity": 1, "x": 0}, W(18) + (0 if "cm" in c else 0.12), 0.4, "power3.out")
    S.fx(W(18), "click", 0.06)
    stamp_in(S, f"{s}-st", W(19))
    # "ketuker": the labels cross over, then snap back
    S.ft(f"#{s}-cm", {"x": 0, "y": 0}, {"x": 410, "y": 665}, W(22) - 0.05, 0.32, "power2.inOut")
    S.ft(f"#{s}-cw", {"x": 0, "y": 0}, {"x": -410, "y": -665}, W(22) - 0.05, 0.32, "power2.inOut")
    S.ft(f"#{s}-cm", {"x": 410, "y": 665}, {"x": 0, "y": 0}, W(22) + 0.42, 0.3, "back.out(1.6)")
    S.ft(f"#{s}-cw", {"x": -410, "y": -665}, {"x": 0, "y": 0}, W(22) + 0.42, 0.3, "back.out(1.6)")
    S.fx(W(22) + 0.42, "click", 0.05)
    S.cam([(S.t0, {"scale": 1.0}, None), (S.t1, {"scale": 1.04}, "sine.inOut")])
    S.mv([(S.t0, dict(SIDE_R, fx=900, fy=1790, h=880), None)])
    S.intent(W(7), "present", "left")
    S.intent(W(14), "reveal")
    S.intent(W(20), "question")
