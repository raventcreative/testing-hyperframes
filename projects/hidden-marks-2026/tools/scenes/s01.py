"""S01 — BELIEF REVERSAL (0 – W7). "Hapus metadata belum tentu menghilangkan jejak AI."
Frame 0 is already a macro of the glass file. On "Hapus" the C2PA badge peels off the glass (corner lifts, then it
travels to the mascot's reaching hand). On "belum tentu" the watermark lattice INSIDE the artwork lights up: the
signal is still there. The glass reflection sweeps across at the end and becomes the layer boundary of S02."""
from kit_hm import floor, glass_file, stamp, stamp_in, spec_sweep, SIDE_R


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(glass_file(f"{s}-file", 200, 640, 440, 560, badge=True, sig_op=0))
    S.front.append(stamp(f"{s}-st", 540, 452, "BELUM TENTU HILANG", 44))
    S.init(f"#{s}-file", {"rotationY": -16, "rotationX": 6, "transformPerspective": 1400})
    S.cam([(0, {"scale": 1.16, "x": 30, "y": 40}, None), (3.45, {"scale": 1.0, "x": 0, "y": 0}, "power2.inOut")])
    # peel: corner lifts (anticipation) -> badge travels to his hand (screen ~ 640,1310) and is gone
    b = f"#{s}-file-badge"
    S.init(b, {"transformOrigin": "0% 0%"})
    S.ft(b, {"rotationX": 0, "rotation": 0}, {"rotationX": -28, "rotation": -6}, W(0) + 0.05, 0.28, "power2.out")
    S.ft(b, {"x": 0, "y": 0, "rotationY": 0, "scale": 1}, {"x": 210, "y": 520, "rotationY": -38, "scale": 0.8}, W(1) - 0.05, 0.62, "power3.inOut")
    S.ft(b, {"opacity": 1}, {"opacity": 0}, W(2) + 0.1, 0.35, "sine.in")
    S.fx(W(1), "whoosh", 0.05)
    # the signal stays: lattice glows inside the artwork
    S.ft(f"#{s}-file-sig", {"opacity": 0}, {"opacity": 0.9}, W(2), 0.5, "power2.out")
    S.ft(f"#{s}-file-art", {"boxShadow": "0 20px 40px -24px rgba(10,13,44,.6)"},
         {"boxShadow": "0 0 0 3px rgba(200,225,255,.7), 0 0 34px rgba(90,145,225,.45)"}, W(2), 0.4, "power3.out")
    S.fx(W(2) + 0.05, "sparkle", 0.05)
    stamp_in(S, f"{s}-st", W(2))
    spec_sweep(S, f"{s}-file", W(6) + 0.2, 0.55)
    # mascot: small, right, reaching for the badge
    S.mv([(0, dict(SIDE_R, fx=900, fy=1790, h=880), None)])
    S.intent(W(0), "present", "left")
    S.intent(W(2), "emphasize", "right")
