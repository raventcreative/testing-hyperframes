"""S07 — FINISH (W61 – end). "Mau gue bedah prosesnya? Komen animasi."  The PiP flies back into the laptop screen, the
room returns, the mascot steps back to his desk mark; the supplied white AIpreneur wordmark resolves (mask wipe + one
sheen) and holds as a clean lockup for the last ~0.45 s."""
from kit_op import room, MASCOT_ROOM
from xk import box

LOGO_W = 640
LOGO_H = round(640 * 119 / 1199, 2)


def build(S):
    s, W = S.id, S.W
    S.back.append(f'<div class="abs" id="{s}-rw" style="left:0;top:0;width:1080px;height:1920px">' + "".join(room(s)) + "</div>")
    S.keys(f"#{s}-rw", [(S.t0, {"scale": 1.08, "transformOrigin": "755px 1123px"}, None), (S.t0 + 1.0, {"scale": 1.0}, "power3.out")])
    S.front.append(f'<div class="abs" id="{s}-logo" style="{box(540 - LOGO_W / 2, 470, LOGO_W, LOGO_H)}">'
                   f'<img class="abs" src="assets/brand/logo_trim.png" style="left:0;top:0;width:{LOGO_W}px;height:{LOGO_H}px">'
                   f'<div class="abs" style="inset:0;overflow:hidden;-webkit-mask:url(assets/brand/logo_trim.png) 0 0/{LOGO_W}px {LOGO_H}px no-repeat;mask:url(assets/brand/logo_trim.png) 0 0/{LOGO_W}px {LOGO_H}px no-repeat">'
                   f'<div class="abs" id="{s}-band" style="left:-200px;top:-20px;width:150px;height:{LOGO_H + 40}px;transform:skewX(-20deg);'
                   f'background:linear-gradient(90deg,rgba(0,201,255,0),rgba(0,201,255,.8) 40%,rgba(255,255,255,1) 50%,rgba(0,201,255,.8) 60%,rgba(0,201,255,0))"></div></div></div>')
    S.front.append(f'<div class="abs" id="{s}-ul" style="{box(540 - 120, 470 + LOGO_H + 34, 240, 4)}border-radius:2px;background:#00C9FF"></div>')
    S.mv([(S.t0, {"fx": 540, "fy": 2060, "h": 1300, "yaw": 0, "pitch": 4}, None), (S.t0 + 0.9, dict(MASCOT_ROOM), "power3.inOut")])
    la = S.t0 + 0.95
    S.init(f"#{s}-logo", {"clipPath": "inset(0px 100% 0px 0px)", "y": 14})
    S.ft(f"#{s}-logo", {"clipPath": "inset(0px 100% 0px 0px)", "y": 14}, {"clipPath": "inset(0px 0% 0px 0px)", "y": 0}, la, 0.6, "power3.out")
    S.ft(f"#{s}-band", {"x": 0}, {"x": LOGO_W + 300}, la + 0.65, 0.7, "power2.inOut")
    S.init(f"#{s}-ul", {"scaleX": 0})
    S.ft(f"#{s}-ul", {"scaleX": 0}, {"scaleX": 1}, la + 0.4, 0.45, "power3.out")
    S.fx(la + 0.1, "sparkle", 0.06)
    S.intent(W(61), "question")
    S.intent(W(65), "cta", "right")
