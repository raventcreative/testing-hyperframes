"""S11 — NOT ONE CLICK (W120 – W131). "Jadi, jangan percaya tool yang menjanjikan semua jejak hilang sekali klik."
A glossy 'magic eraser' claim (generic, no brand) is struck through on "jangan percaya" and shrinks to a broken
claim tag; behind it the file's two layers are still distinguishable (badge gone, lattice still in the pixels)."""
from kit_hm import floor, glass_file, stamp, stamp_in, MAT, SIDE_R
from xk import box


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(glass_file(f"{s}-file", 250, 640, 420, 540, badge=False, sig_op=0.9))
    S.back.append(f'<div class="abs" id="{s}-btn" style="{box(110, 760, 700, 300)}border-radius:150px;'
                  f'background:radial-gradient(120% 140% at 30% 20%,#ffffff 0%,#dfe8f6 40%,#9fb4d4 100%);'
                  f'box-shadow:inset 0 4px 0 rgba(255,255,255,.95),inset 0 -14px 24px rgba(41,75,119,.25),0 40px 60px -30px rgba(10,13,44,.6)">'
                  f'<div class="abs" style="left:0;top:76px;width:700px;text-align:center;font:700 54px/1.1 Poppins;color:#0A0D2C">HAPUS SEMUA JEJAK</div>'
                  f'<div class="abs" style="left:0;top:156px;width:700px;text-align:center;font:400 34px/1.1 Poppins;color:#294B77">“1 klik, 100% bersih”</div></div>')
    S.back.append(f'<div class="abs" id="{s}-strike" style="{box(80, 895, 760, 26)}border-radius:13px;background:linear-gradient(108deg,#0A0D2C,#294B77);'
                  f'box-shadow:0 0 0 1px rgba(170,205,255,.3),0 0 16px rgba(41,75,119,.35);transform:rotate(-8deg);transform-origin:0 50%"></div>')
    S.front.append(stamp(f"{s}-st", 540, 452, "BUKAN SEKALI KLIK", 46))
    S.init(f"#{s}-btn", {"opacity": 0, "scale": 0.9})
    S.ft(f"#{s}-btn", {"opacity": 0, "scale": 0.9}, {"opacity": 1, "scale": 1}, S.t0, 0.45, "back.out(1.5)")
    S.fx(S.t0 + 0.1, "pop", 0.05)
    S.init(f"#{s}-strike", {"scaleX": 0})
    S.ft(f"#{s}-strike", {"scaleX": 0}, {"scaleX": 1}, W(121), 0.3, "power3.out")             # "jangan percaya"
    S.fx(W(121), "whoosh", 0.05)
    S.ft(f"#{s}-btn", {"scale": 1, "rotation": 0, "y": 0, "opacity": 1}, {"scale": 0.38, "rotation": -10, "y": 520, "opacity": 0.85}, W(126) - 0.2, 0.6, "power3.inOut")
    S.ft(f"#{s}-strike", {"scale": 1, "y": 0, "x": 0, "opacity": 1}, {"scale": 0.38, "y": 520, "x": 140, "opacity": 0}, W(126) - 0.2, 0.6, "power3.inOut")
    S.init(f"#{s}-file", {"opacity": 0.25, "rotationY": -14, "transformPerspective": 1400})
    S.ft(f"#{s}-file", {"opacity": 0.25}, {"opacity": 1}, W(126) - 0.1, 0.5, "power2.out")    # "semua jejak": still there
    S.ft(f"#{s}-file-shell", {"z": 0, "x": 0}, {"z": 120, "x": -60}, W(127), 0.5, "power3.out")
    S.fx(W(127), "sparkle", 0.05)
    stamp_in(S, f"{s}-st", W(129))
    S.mv([(S.t0, dict(SIDE_R, fx=900, fy=1790, h=880), None)])
    S.intent(W(120), "emphasize", "left")
    S.intent(W(126), "present", "left")
