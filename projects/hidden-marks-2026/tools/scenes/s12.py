"""S12 — CTA (W131 – end). "Komen JEJAK, nanti gue kirim checklist pemeriksaannya."  A drawer slides out and stands up
as the real JEJAK checklist (items from 06_CHECKLIST_JEJAK_LEAD_MAGNET.md). Crane-out; final 0.3 s still, no fade."""
from kit_hm import floor, stamp, stamp_in, MAT, SIDE_R
from xk import box

ITEMS = ["Siapkan file asli", "Kenali 2 jenis jejak", "Pakai alat resmi", "Baca hasil dengan teliti"]


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    rows = ""
    for k, it in enumerate(ITEMS):
        y = 150 + k * 92
        rows += (f'<div class="abs" id="{s}-cb{k}" style="left:40px;top:{y}px;width:44px;height:44px;border-radius:12px;border:3px solid #294B77;background:#fff">'
                 f'<svg class="abs" id="{s}-ck{k}" style="left:4px;top:4px;width:30px;height:30px" viewBox="0 0 24 24"><path d="M4 12.5 9.5 18 20 6" fill="none" stroke="#0A0D2C" stroke-width="3.4" '
                 f'stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg></div>'
                 f'<div class="abs" style="left:108px;top:{y + 4}px;font:700 32px/1.2 Poppins;color:#0A0D2C">{it}</div>')
    S.back.append(f'<div class="abs" id="{s}-clip" style="{box(60, 600, 600, 560)}border-radius:28px;{MAT["porcelain"]}">'
                  f'<div class="abs" style="left:230px;top:-26px;width:140px;height:52px;border-radius:14px;{MAT["alu"]}"></div>'
                  f'<div class="abs" style="left:40px;top:58px;font:700 40px/1 Poppins;color:#0A0D2C">CHECKLIST <span style="color:#fff;background:linear-gradient(108deg,#0A0D2C,#294B77);border-radius:12px;padding:2px 14px">JEJAK</span></div>{rows}</div>')
    S.front.append(stamp(f"{s}-st", 540, 452, "KOMEN JEJAK", 50))
    c = f"#{s}-clip"
    S.init(c, {"opacity": 0, "y": 260, "rotationX": 70, "transformPerspective": 1400, "transformOrigin": "50% 100%"})
    S.ft(c, {"opacity": 0, "y": 260, "rotationX": 70}, {"opacity": 1, "y": 0, "rotationX": 0}, S.t0, 0.7, "power3.out")   # drawer -> clipboard
    S.fx(S.t0 + 0.1, "whoosh", 0.05)
    stamp_in(S, f"{s}-st", W(132))
    for k in range(4):
        at = W(135) + 0.28 * k
        S.ft(f"#{s}-ck{k} path", {"strokeDashoffset": 1}, {"strokeDashoffset": 0}, at, 0.25, "power2.out")
        S.fx(at, "click", 0.04)
    S.cam([(S.t0, {"scale": 1.04}, None), (S.t1 - 0.32, {"scale": 1.0}, "sine.inOut")])
    S.mv([(S.t0, dict(SIDE_R, fx=880, fy=1800, h=900), None)])
    S.intent(W(131), "cta", "left")
    S.intent(W(135), "confident", "right")
