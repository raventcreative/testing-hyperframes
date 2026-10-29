"""S03 — METADATA = ID CARD (W23 – W41). "Pertama, metadata. Ibarat kartu identitas yang menempel di file. Pada file
yang mendukung, kartu digital ini disebut C2PA."  Turntable: the file swings left and its glass shell slides up like a
sleeve; the ID card (porcelain, printed fields, no fake signature) is clipped to it by an aluminium latch. Two small
files show the mechanics: a SUPPORTED file has a card slot that holds the card; an unsupported one has no slot."""
from kit_hm import floor, glass_file, stamp, stamp_in, MAT, SIDE_R, SVG_FILE
from xk import box


def card_html(s):
    rows = ""
    for k, lab in enumerate(("ASAL FILE", "ALAT PEMBUAT", "RIWAYAT EDIT")):
        y = 96 + k * 62
        rows += (f'<div class="abs" style="left:30px;top:{y}px;font:700 22px/1 Poppins;color:#294B77;letter-spacing:.06em">{lab}</div>'
                 f'<div class="abs" style="left:250px;top:{y + 4}px;width:{200 - k * 40}px;height:14px;border-radius:7px;background:rgba(41,75,119,.22)"></div>')
    return (f'<div class="abs" id="{s}-card" style="{box(470, 640, 520, 330)}border-radius:24px;{MAT["porcelain"]}">'
            f'<div class="abs" style="left:30px;top:30px;font:700 30px/1 Poppins;color:#0A0D2C">KARTU IDENTITAS FILE</div>{rows}'
            f'<div class="abs" id="{s}-tag" style="left:30px;top:262px;padding:8px 22px;border-radius:14px;font:700 34px/1.1 Poppins;color:#fff;'
            f'background:linear-gradient(108deg,#0A0D2C,#294B77);box-shadow:0 0 0 1px rgba(170,205,255,.22),0 0 14px rgba(41,75,119,.22)">C2PA</div>'
            f'<div class="abs" style="left:-34px;top:120px;width:60px;height:24px;border-radius:8px;{MAT["alu"]}"></div></div>')


def mini(id_, x, y, ok):
    slot = (f'<div class="abs" id="{id_}-c" style="left:150px;top:18px;width:96px;height:60px;border-radius:10px;{MAT["porcelain"]}">'
            f'<div class="abs" style="left:12px;top:12px;font:700 18px/1 Poppins;color:#0A0D2C">C2PA</div></div>' if ok else
            '<div class="abs" style="left:150px;top:18px;width:96px;height:60px;border-radius:10px;border:2.5px dashed rgba(41,75,119,.35)"></div>')
    lab = "DIDUKUNG" if ok else "TIDAK DIDUKUNG"
    return (f'<div class="abs" id="{id_}" style="{box(x, y, 280, 230)}border-radius:22px;{MAT["glass"]}">'
            f'<div class="abs" style="left:24px;top:22px;width:96px;height:120px;color:#294B77">{SVG_FILE}</div>{slot}'
            f'<div class="abs" style="left:0;top:168px;width:280px;text-align:center;font:700 24px/1 Poppins;color:#0A0D2C">{lab}</div></div>')


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(glass_file(f"{s}-file", 200, 640, 440, 560, badge=False, sig_op=0.85))
    S.back.append(card_html(s))
    S.back.append(mini(f"{s}-ok", 90, 1215, True))
    S.back.append(mini(f"{s}-no", 400, 1215, False))
    S.front.append(stamp(f"{s}-st", 540, 452, "METADATA FILE", 44))
    f = f"#{s}-file"
    S.init(f, {"rotationY": -30, "rotationX": 6, "transformPerspective": 1400})
    # turntable to the left third; the glass shell slides up like a sleeve
    S.ft(f, {"x": 0, "y": 0, "scale": 1, "rotationY": -30}, {"x": -90, "y": 0, "scale": 0.72, "rotationY": 20}, S.t0, 0.9, "power3.inOut")
    S.ft(f"{f}-shell", {"y": 0}, {"y": -90}, W(24), 0.5, "power2.out")
    S.init(f"#{s}-card", {"opacity": 0, "x": 120, "rotationY": -35, "transformPerspective": 1400})
    S.ft(f"#{s}-card", {"opacity": 0, "x": 120, "rotationY": -35}, {"opacity": 1, "x": 0, "rotationY": 0}, W(26) - 0.1, 0.6, "power3.out")
    S.fx(W(27), "click", 0.07)                             # latch clicks onto the file ("menempel")
    S.ft(f"#{s}-card", {"rotation": 0}, {"rotation": -1.2}, W(29), 0.18, "power2.out")
    S.ft(f"#{s}-card", {"rotation": -1.2}, {"rotation": 0}, W(29) + 0.18, 0.4, "back.out(2)")
    for m, d in ((f"#{s}-ok", 0), (f"#{s}-no", 0.14)):
        S.init(m, {"opacity": 0, "y": 60})
        S.ft(m, {"opacity": 0, "y": 60}, {"opacity": 1, "y": 0}, W(33) + d, 0.5, "power3.out")
    S.init(f"#{s}-ok-c", {"y": -70, "opacity": 0})
    S.ft(f"#{s}-ok-c", {"y": -70, "opacity": 0}, {"y": 0, "opacity": 1}, W(35), 0.4, "back.out(1.6)")
    S.fx(W(35) + 0.3, "click", 0.06)
    S.ft(f"#{s}-tag", {"scale": 1}, {"scale": 1.12}, W(40), 0.22, "power3.out")
    S.ft(f"#{s}-tag", {"scale": 1.12}, {"scale": 1}, W(40) + 0.22, 0.4, "sine.inOut")
    S.ft(f"#{s}-tag", {"boxShadow": "0 0 0 1px rgba(170,205,255,.22),0 0 14px rgba(41,75,119,.22)"},
         {"boxShadow": "0 0 0 2px rgba(200,225,255,.6),0 0 26px rgba(80,135,215,.32)"}, W(40), 0.3, "power3.out")
    S.fx(W(40), "ping", 0.05)
    stamp_in(S, f"{s}-st", W(24))
    # C2PA badge edge travels out at the end (-> S04 lens)
    S.ft(f"#{s}-card", {"x": 0, "opacity": 1}, {"x": 520, "opacity": 0}, S.t1 - 0.45, 0.45, "power2.in")
    S.cam([(S.t0, {"scale": 1.04, "rotationY": 0}, None), (S.t1, {"scale": 1.0, "rotationY": 0}, "sine.inOut")])
    S.mv([(S.t0, dict(SIDE_R, fx=880, fy=1820, h=880), None)])
    S.intent(W(23), "explain", "left")
    S.intent(W(25), "present", "left")
    S.intent(W(32), "compare", "left")
    S.intent(W(36), "pointFwd", "left")
