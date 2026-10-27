"""S24 — HUMAN DIRECTION + CHECKS (43.30–46.27)
VO: "Tetap perlu arahan visual, timing, dan pengecekan hasil."
S23's preview card fans out into a montage strip of our own results (+ a 20/20 badge). On their words three human
checks pop on the right - Arahan visual, Timing, Pengecekan hasil - each with a drawn cyan tick. Honest message:
the code builds it, a person directs and reviews. Mascot medium-left, nodding to each check.
Hand-off: on "hasil." the montage cards fly together into one stack at the centre (S25 opens on it)."""
from xk import box, r3, CYAN, check_svg
from kit import SELF, HALF, blur_wrap, talk

THUMBS = ["orbit", "paper", "cover", "city", "phone"]
TW, TH = 150, 267
TY = 268
TX = [75 + k * (TW + 45) for k in range(5)]
START = (720, 322, 291, 518)      # S23 end: preview card rect (approx.)
STACK = (465, 300, 150, 267)      # S25 start: stack at the centre
CHECKS = [("Arahan visual", "eye"), ("Timing", "wave"), ("Pengecekan hasil", "check")]
CK_Y, CK_H = 236, 66
CK_W = [318, 200, 372]
CK_X = [84, 84 + 318 + 16, 84 + 318 + 16 + 200 + 16]


def icon(kind):
    if kind == "eye":
        return ('<svg viewBox="0 0 48 48" style="position:absolute;left:0;top:0;width:48px;height:48px"><path d="M4 24 C12 12 36 12 44 24 C36 36 12 36 4 24 Z" fill="none" stroke="#fff" stroke-width="3"/>'
                f'<circle cx="24" cy="24" r="7" fill="{CYAN}"/></svg>')
    if kind == "wave":
        return ('<svg viewBox="0 0 48 48" style="position:absolute;left:0;top:0;width:48px;height:48px">'
                + "".join(f'<rect x="{4 + i * 6}" y="{24 - h}" width="3.5" height="{2 * h}" rx="1.7" fill="{"#fff" if i % 3 else CYAN}"/>' for i, h in enumerate((4, 9, 14, 7, 16, 10, 5)))
                + "</svg>")
    return ('<svg viewBox="0 0 48 48" style="position:absolute;left:0;top:0;width:48px;height:48px"><rect x="5" y="5" width="38" height="38" rx="10" fill="none" stroke="#fff" stroke-width="3"/>'
            f'<path d="M14 25 L21 32 L34 17" fill="none" stroke="{CYAN}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W127, W129, W131, W132 = S.W(127), S.W(129), S.W(131), S.W(132)
    # ---------------------------------------------------------------- back: montage strip + badge
    for k, n in enumerate(THUMBS):
        S.back.append(f'<div class="abs" id="{s}-t{k}" style="{box(TX[k], TY, TW, TH)}border-radius:14px;overflow:hidden;box-shadow:0 0 0 2px rgba(255,255,255,.25),0 18px 30px -14px rgba(3,8,28,.85)">'
                      f'<img src="{SELF}/{n}.jpg" alt="" style="position:absolute;left:0;top:0;width:{TW}px;height:{TH}px" />'
                      f'<div class="abs" style="left:8px;top:8px;width:30px;height:30px;border-radius:15px;background:{CYAN}">{check_svg(f"{s}-tc{k}", "#0b1636", 4, drawn=True)}</div></div>')
    S.back.append(f'<div class="abs acrylic pill" id="{s}-badge" style="{box(400, TY + TH + 24, 280, 64)}font:700 30px/60px Poppins;color:#fff;text-align:center;letter-spacing:.04em">20/20 <span style="color:{CYAN}">SELESAI</span></div>')
    # ---------------------------------------------------------------- front: three human checks (right column)
    for k, (label, ic) in enumerate(CHECKS):
        x, w = CK_X[k], CK_W[k]
        S.front.append(f'<div class="abs smoked pill" id="{s}-k{k}" style="{box(x, CK_Y, w, CK_H)}">'
                       f'<div class="abs" style="left:16px;top:15px;width:36px;height:36px;transform:scale(.75);transform-origin:0 0">{icon(ic)}</div>'
                       f'<div class="abs" style="left:56px;top:0;width:{w - 110}px;font:700 26px/{CK_H}px Poppins;color:#fff;white-space:nowrap">{label}</div>'
                       f'<div class="abs" style="left:{w - 50}px;top:15px;width:36px;height:36px;border-radius:18px;border:2px solid rgba(0,208,254,.7)">'
                       f'<div class="abs" style="left:5px;top:5px;width:24px;height:24px">{check_svg(f"{s}-kc{k}", CYAN, 3.6)}</div></div></div>')
    # ---------------------------------------------------------------- motion
    sx, sy, sw, sh = START
    for k in range(5):
        frm = {"x": sx - TX[k], "y": sy - TY, "scale": sw / TW, "opacity": 0, "rotation": 0, "transformOrigin": "0% 0%"}
        S.init(f"#{s}-t{k}", frm)
        S.ft(f"#{s}-t{k}", dict(frm), {"x": 0, "y": 0, "scale": 1, "opacity": 1, "rotation": (-4, -2, 0, 2, 4)[k]}, t0 + 0.02 + k * 0.05, 0.5, "power3.out")
    S.init(f"#{s}-badge", {"opacity": 0, "scale": 0.7})
    S.ft(f"#{s}-badge", {"opacity": 0, "scale": 0.7}, {"opacity": 1, "scale": 1}, t0 + 0.4, 0.3, "back.out(2.2)")
    for k, b in enumerate((W127, W129, W131)):
        S.init(f"#{s}-k{k}", {"y": -30, "opacity": 0, "scale": 0.8})
        S.ft(f"#{s}-k{k}", {"y": -30, "opacity": 0, "scale": 0.8}, {"y": 0, "opacity": 1, "scale": 1}, b - 0.08, 0.32, "back.out(1.8)")
        S.init(f"#{s}-kc{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-kc{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, b + 0.22, 0.24, "power2.out")
        S.fx(b + 0.22, "ping" if k == 2 else "click", 0.05)
    # hand-off: "hasil." -> montage flies into one stack at the centre; checks clear
    go = W132 + 0.12
    stx, sty, stw, sth = STACK
    for k in range(5):
        S.ft(f"#{s}-t{k}", {"x": 0, "y": 0, "rotation": (-4, -2, 0, 2, 4)[k]}, {"x": stx - TX[k], "y": sty - TY, "rotation": (-6, -3, 0, 3, 6)[k]}, go + k * 0.03, 0.4, "power3.inOut")
    S.ft(f"#{s}-badge", {"opacity": 1}, {"opacity": 0}, go, 0.2, "power2.in")
    for k in range(3):
        S.ft(f"#{s}-k{k}", {"y": 0, "opacity": 1}, {"y": -40, "opacity": 0}, go + 0.1 + k * 0.04, 0.26, "power2.in")
    S.fx(go, "whoosh", 0.05)

    # ---------------------------------------------------------------- mascot: explaining, half-body, centre; montage soft behind
    blur_wrap(S)
    S.ft(f"#{s}-bgblur", {"filter": "blur(0px) brightness(1) saturate(1)"}, {"filter": "blur(16px) brightness(0.62) saturate(0.9)"}, t0, 0.45, "power2.inOut")
    S.mv([(t0, {"fx": 540, "fy": 1760, "h": 800, "yaw": -4, "pitch": 6}, None), (t0 + 0.45, dict(HALF, yaw=-6), "power3.inOut"), (S.W(129), dict(HALF, yaw=5), "sine.inOut"), (t1, dict(HALF, yaw=-2), "sine.inOut")])
    for tr, keys in talk(S, 125, 132, seed=3).items():
        S.act(tr, keys)
