"""S08 — CLAUDE CONTENT CHECKER (W92 – W101). "Untuk file Claude yang didukung, buka Claude Content Checker."
An inspection station (official NAME only, no copied site UI, no result shown). The file slides into the input slot,
the file-type selector lights 'FILE CLAUDE · DIDUKUNG', the scan beam passes."""
from kit_hm import floor, glass_file, station, stamp, stamp_in, chip, MAT, SIDE_L
from xk import box


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(station(f"{s}-cc", 420, 560, 600, 640, "CLAUDE<br>CONTENT CHECKER", "memeriksa file Claude yang didukung"))
    S.back.append(f'<div class="abs" id="{s}-rail" style="{box(0, 1240, 1080, 16)}border-radius:8px;{MAT["alu"]}"></div>')
    S.back.append(glass_file(f"{s}-file", 520, 760, 400, 510, badge=True, sig_op=0.8))
    S.back.append(chip(f"{s}-sel", 470, 1290, "FILE CLAUDE · DIDUKUNG", size=28))
    S.front.append(stamp(f"{s}-st", 540, 452, "CLAUDE CONTENT CHECKER", 42))
    f = f"#{s}-file"
    S.init(f, {"scale": 0.6, "x": -320, "transformOrigin": "50% 50%"})
    S.ft(f, {"x": -320, "y": 0}, {"x": 0, "y": 0}, S.t0, 0.7, "power3.out")
    S.ft(f, {"y": 0, "opacity": 1}, {"y": 300, "opacity": 0}, W(96), 0.45, "power3.in")       # into the slot
    S.fx(W(96) + 0.4, "click", 0.07)
    S.init(f"#{s}-sel", {"opacity": 0, "y": 20})
    S.ft(f"#{s}-sel", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, W(94), 0.35, "power3.out")
    S.ft(f"#{s}-cc-beam", {"opacity": 0, "y": 0}, {"opacity": 1, "y": 0}, W(97), 0.1, "none")
    S.ft(f"#{s}-cc-beam", {"y": 0}, {"y": -330}, W(97) + 0.1, 0.9, "sine.inOut")
    S.ft(f"#{s}-cc-beam", {"opacity": 1}, {"opacity": 0}, W(97) + 1.0, 0.25, "none")
    S.fx(W(97), "whoosh", 0.04)
    stamp_in(S, f"{s}-st", W(98))
    S.cam([(S.t0, {"scale": 1.03, "x": 20}, None), (S.t1, {"scale": 1.0, "x": 0}, "sine.inOut")])
    S.mv([(S.t0, dict(SIDE_L, fx=200, fy=1790, h=860), None)])
    S.intent(W(92), "explain", "right")
    S.intent(W(97), "pointFwd", "right")
