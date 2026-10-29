"""S07 — USE THE ORIGINAL FILE (W87 – W92). "Cara ceknya, gunakan file asli."  The same glass file (badge on, lattice
inside) is handed forward and tagged FILE ASLI; it then glides right toward the inspector slot (-> S08)."""
from kit_hm import floor, glass_file, stamp, stamp_in, chip, spec_sweep, SIDE_L


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(glass_file(f"{s}-file", 470, 660, 400, 510, badge=True, sig_op=0.8))
    S.back.append(chip(f"{s}-tag", 520, 1200, "FILE ASLI", dark=True, size=32))
    S.front.append(stamp(f"{s}-st", 540, 452, "CEK FILE ASLI", 44))
    f = f"#{s}-file"
    S.init(f, {"rotationY": 18, "transformPerspective": 1400, "x": -260, "opacity": 0})
    S.ft(f, {"x": -260, "opacity": 0, "rotationY": 18}, {"x": 0, "opacity": 1, "rotationY": 8}, S.t0, 0.6, "power3.out")
    spec_sweep(S, f"{s}-file", W(90), 0.5)
    S.init(f"#{s}-tag", {"opacity": 0, "y": 30})
    S.ft(f"#{s}-tag", {"opacity": 0, "y": 30}, {"opacity": 1, "y": 0}, W(91) - 0.05, 0.35, "back.out(1.7)")
    S.fx(W(91), "click", 0.06)
    stamp_in(S, f"{s}-st", W(90))
    S.ft(f, {"x": 0, "scale": 1}, {"x": 330, "scale": 0.6}, S.t1 - 0.4, 0.4, "power2.in")
    S.ft(f"#{s}-tag", {"x": 0, "opacity": 1}, {"x": 330, "opacity": 0}, S.t1 - 0.4, 0.4, "power2.in")
    S.mv([(S.t0, dict(SIDE_L, fx=210, fy=1790, h=880), None)])
    S.intent(W(87), "present", "right")
