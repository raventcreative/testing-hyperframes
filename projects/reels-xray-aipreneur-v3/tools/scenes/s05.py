"""S05 — CODE AS THE BLUEPRINT (10.42–13.78)  VO: "Ini yang terjadi kalau motion graphics dibangun lewat kode."
Opens on a closed scroll spool at hero centre (s04's rail curled into it). The two spool rods roll apart and
unroll a drafting blueprint on a tilted porcelain drafting machine; engraved glass code plates rise off the
sheet, connection lines draw to a mini Reel above, a motion frame is stamped around the Reel on "dibangun",
and on "kode" the plates lock into register (pins + one light burst). End: the rods roll back together and a
navy cartridge shell closes over the scroll (input cartridge for s06)."""
from xk import box, screw, shadow, apex, minireel, minireel_anim, rivets_line, r3
from kit_b import backdrop, near_blur, code_lines, engrave, along, bezier_d

SFX = [(10.5, "whoosh", 0.07), (12.98, "click", 0.13)]

BX, BY, BW, BH = 180, 560, 820, 600      # drafting board (screen box before tilt)


def build(S):
    s = S.id
    S.persp_origin = (590, 560)
    W24, W26, W28 = S.W(24), S.W(26), S.W(28)    # motion 11.60, dibangun 12.34, kode 12.98
    end = S.t1
    backdrop(S, seed=5)
    # ---------------------------------------------------------------- platform (drafting machine base)
    S.mid.append(shadow(150, 1250, 900, 90, 0.85))
    S.mid.append(f'<div class="abs navy-side" style="{box(150, 1232, 880, 46)}border-radius:0 0 22px 22px"></div>')
    S.mid.append(f'<div class="abs por" style="{box(150, 1150, 880, 92)}border-radius:22px">'
                 f'{screw(28, 46, 20, 12)}{screw(852, 46, -30, 12)}{rivets_line(80, 70, 800, 70, 12)}'
                 f'<div class="abs" style="{box(300, 30, 280, 10)}border-radius:5px;background:#cbdbf4;box-shadow:inset 0 1px 2px rgba(28,51,84,.3)"></div></div>')
    # sliding guides (rails + carriage blocks) on the platform
    for side, x0, dx in (("gl", 168, -46), ("gr", 912, 46)):
        S.mid.append(f'<div class="abs" style="{box(x0 - 30 if side == "gl" else x0 - 50, 1132, 120, 8)}border-radius:4px;background:#acc6e7"></div>')
        S.mid.append(f'<div class="abs por" id="{s}-{side}" style="{box(x0, 1100, 60, 54)}border-radius:10px">'
                     f'<div class="abs" style="{box(14, 10, 32, 6)}border-radius:3px;background:#294b77"></div>{screw(30, 36, 45, 10)}</div>')
        S.init(f"#{s}-{side}", {"x": 0})
        S.ft(f"#{s}-{side}", {"x": 0}, {"x": dx}, S.W(22) - 0.1, 0.55, "power3.inOut")
    # ---------------------------------------------------------------- tilted drafting board
    dims = (f'<div class="abs" style="{box(40, BH - 34, BW - 80, 2)}background:rgba(41,75,119,.45)"></div>'
            + "".join(f'<div class="abs" style="{box(40 + k * (BW - 80) / 8, BH - 42, 2, 18)}background:rgba(41,75,119,.45)"></div>' for k in range(9))
            + "".join(f'<div class="abs corner {c}" style="{box(x, y, 22, 22)}border-color:#3a6299;opacity:.7"></div>'
                      for c, x, y in (("tl", 18, 18), ("tr", BW - 40, 18), ("bl", 18, BH - 70), ("br", BW - 40, BH - 70))))
    circle = f'<div class="abs" style="{box(560, 70, 190, 190)}border-radius:50%;border:2px dashed rgba(58,98,153,.45)"></div><div class="abs" style="{box(653, 60, 2, 210)}background:rgba(58,98,153,.3)"></div><div class="abs" style="{box(550, 164, 210, 2)}background:rgba(58,98,153,.3)"></div>'
    sheet = f'<div class="abs grid-paper" id="{s}-sheet" style="{box(0, 0, BW, BH)}border-radius:6px;box-shadow:0 2px 0 #dbe6f6,0 30px 40px -24px rgba(28,51,84,.35)">{dims}{circle}</div>'
    plates = []
    POS = [(-110, 50, -6), (0, -30, 4), (115, 22, -3)]
    for k in range(3):
        pid = f"{s}-pl{k}"
        plates.append(f'<div class="abs glass" id="{pid}" style="{box(190, 130, 440, 300)}border-radius:16px">'
                      f'{code_lines(pid + "-c", 30, 34, 380, 10, seed=11 + k * 7, gap=24, h=8)}'
                      f'<div class="pin" id="{pid}-p1" style="left:10px;top:10px"></div><div class="pin" id="{pid}-p2" style="left:420px;top:10px"></div>'
                      f'<div class="pin" id="{pid}-p3" style="left:10px;top:280px"></div><div class="pin" id="{pid}-p4" style="left:420px;top:280px"></div></div>')
    spool = lambda nm: (f'<div class="abs p3" id="{s}-{nm}" style="{box(BW / 2 - 24, -26, 48, BH + 52)}">'
                        f'<div class="abs" style="{box(6, 18, 36, BH + 16)}border-radius:18px;background:linear-gradient(90deg,#c9d8ee 0%,#ffffff 30%,#e6edf8 62%,#8fa9cf 100%);box-shadow:4px 8px 12px -4px rgba(28,51,84,.35)"></div>'
                        f'<div class="abs navy-side" style="{box(0, 0, 48, 24)}border-radius:50%"></div>'
                        f'<div class="abs navy-side" style="{box(0, BH + 28, 48, 24)}border-radius:50%"></div>'
                        f'<div class="abs" style="{box(18, 6, 12, 12)}border-radius:50%;background:#cbdbf4"></div></div>')
    cart = (f'<div class="abs" id="{s}-cart" style="{box(BW / 2 - 66, -44, 132, BH + 88)}border-radius:66px;'
            f'background:linear-gradient(90deg,#1c3354 0%,#3a6299 28%,#294b77 60%,#1c3354 100%);box-shadow:inset 0 0 0 3px rgba(203,219,244,.4),0 24px 30px -14px rgba(28,51,84,.45)">'
            f'<div class="abs" style="{box(54, 40, 24, BH + 8)}border-radius:12px;background:rgba(203,219,244,.25)"></div>'
            f'<div class="led" style="left:60px;top:{BH / 2 + 38}px"></div></div>')
    S.mid.append(f'<div class="abs p3" style="{box(BX, BY, BW, BH)}transform-origin:50% 100%;transform:rotateX(26deg)">'
                 f'{sheet}{"".join(plates)}{spool("spL")}{spool("spR")}{cart}</div>')
    # ---------------------------------------------------------------- mini Reel above the blueprint + stamped frame
    S.mid.append(shadow(790, 760, 220, 50, 0.6, soft=True))
    S.mid.append(f'<div class="abs por" id="{s}-reel" style="{box(800, 430, 180, 310)}border-radius:26px">'
                 f'<div class="abs" style="{box(12, 16, 156, 278)}border-radius:16px;overflow:hidden;background:linear-gradient(170deg,#fbfcfe,#e6edf8);box-shadow:inset 0 0 0 2px rgba(41,75,119,.45)">{minireel(s + "-mr", 156, 278, 1)}</div></div>')
    for c, x, y in (("tl", 782, 412), ("tr", 972, 412), ("bl", 782, 724), ("br", 972, 724)):
        S.mid.append(f'<div class="corner {c}" id="{s}-cn{c}" style="left:{x}px;top:{y}px"></div>')
    # connection lines plates -> reel (navy, soft glow), plus travelling beads
    CON = [((560, 820), (650, 760), (700, 650), (805, 600)), ((640, 900), (720, 860), (760, 760), (810, 700)), ((470, 760), (560, 600), (700, 520), (805, 500))]
    paths = "".join(f'<path id="{s}-ln{k}" d="{bezier_d(p)}" fill="none" stroke="#3a6299" stroke-width="3" stroke-linecap="round" stroke-dasharray="520" stroke-dashoffset="520" opacity=".75"/>' for k, p in enumerate(CON))
    S.mid.append(f'<svg class="abs" style="{box(0, 0, 1080, 1920)}overflow:visible" viewBox="0 0 1080 1920">{paths}</svg>')
    for k, p in enumerate(CON):
        S.mid.append(f'<div class="abs" id="{s}-bd{k}" style="{box(p[0][0] - 7, p[0][1] - 7, 14, 14)}border-radius:50%;background:#ffffff;box-shadow:0 0 0 3px #3a6299,0 0 14px rgba(172,198,231,.95)"></div>')
    # ---------------------------------------------------------------- near plane
    near_blur(S, [(f"{s}-n1", 900, 1380, 240, 30, "border-radius:15px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px);opacity:.9"),
                  (f"{s}-n2", -60, 520, 150, 150, "border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)")])
    apex(S, S.near, f"{s}-ap", 600, 820, W28, size=640, sparks=6, seed=5)

    # ================================================================ motion
    S.cam([(S.t0, {"z": 180, "rotationY": -6, "rotationX": 2, "x": 0, "y": 0}, None),
           (S.W(22), {"z": 0, "rotationY": -2, "rotationX": 0}, "expo.out"),
           (W28 - 0.1, {"z": 26, "rotationY": 2.5}, "sine.inOut"),
           (W28 + 0.25, {"z": 80}, "power3.out"),
           (end, {"z": 170, "rotationY": 0}, "power2.in")])
    # scroll: rods roll apart (unroll), later back together into the cartridge
    S.keys(f"#{s}-spL", [(S.t0, {"x": -2}, None), (S.t0 + 0.12, {"x": 6}, "power2.out"),
                         (S.W(22), {"x": -(BW / 2) + 8}, "power3.inOut"), (end - 0.5, {"x": -(BW / 2) + 8}, "none"), (end - 0.2, {"x": -2}, "power3.in")])
    S.keys(f"#{s}-spR", [(S.t0, {"x": 2}, None), (S.t0 + 0.12, {"x": -6}, "power2.out"),
                         (S.W(22), {"x": BW / 2 - 8}, "power3.inOut"), (end - 0.5, {"x": BW / 2 - 8}, "none"), (end - 0.2, {"x": 2}, "power3.in")])
    S.keys(f"#{s}-sheet", [(S.t0, {"scaleX": 0.02, "transformOrigin": "50% 50%"}, None), (S.t0 + 0.12, {"scaleX": 0.02}, "none"),
                           (S.W(22), {"scaleX": 1}, "power3.inOut"), (end - 0.5, {"scaleX": 1}, "none"), (end - 0.2, {"scaleX": 0.02}, "power3.in")])
    S.init(f"#{s}-cart", {"scaleY": 0, "opacity": 0, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-cart", {"scaleY": 0, "opacity": 0}, {"scaleY": 1, "opacity": 1}, end - 0.2, 0.18, "power4.out")
    # plates rise off the sheet (offset, unregistered) ... lock into register on "kode"
    for k, (dx, dy, rot) in enumerate(POS):
        pid = f"#{s}-pl{k}"
        zf = 24 + k * 34
        S.keys(pid, [(S.t0, {"x": dx, "y": dy, "rotation": rot, "z": 0, "opacity": 0, "scale": 0.92}, None),
                     (S.W(22) + 0.1 + k * 0.14, {"opacity": 0}, "none"),
                     (S.W(22) + 0.55 + k * 0.14, {"z": zf, "opacity": 1, "scale": 1}, "power3.out"),
                     (W28 - 0.14, {"x": dx * 1.12, "y": dy * 1.12, "rotation": rot * 1.2}, "sine.inOut"),
                     (W28 + 0.2, {"x": 0, "y": 0, "rotation": 0, "z": zf + 10}, "back.out(1.6)"),
                     (end - 0.5, {"z": zf + 14}, "sine.out"),
                     (end - 0.25, {"z": 0, "scale": 0.3, "opacity": 0}, "power3.in")])
        for q in range(1, 5):
            S.init(f"{pid}-p{q}", {"scale": 0, "opacity": 0})
            S.ft(f"{pid}-p{q}", {"scale": 0, "opacity": 0}, {"scale": 1, "opacity": 1}, W28 + 0.12 + q * 0.02, 0.2, "back.out(3)")
        for c in range(10):  # code lines type in, row by row
            S.init(f"{pid}-c{c}", {"scaleX": 0, "transformOrigin": "0% 50%"})
            S.ft(f"{pid}-c{c}", {"scaleX": 0}, {"scaleX": 1}, S.W(22) + 0.45 + k * 0.14 + c * 0.07, 0.25, "power2.out")
    # connection lines draw on "motion graphics", beads travel after the lock
    for k in range(3):
        S.init(f"#{s}-ln{k}", {"strokeDashoffset": 520})
        S.ft(f"#{s}-ln{k}", {"strokeDashoffset": 520}, {"strokeDashoffset": 0}, W24 + k * 0.1, 0.6, "power2.inOut")
        S.ft(f"#{s}-ln{k}", {"strokeDashoffset": 0}, {"strokeDashoffset": -520}, end - 0.42, 0.3, "power2.in")
        CONk = [((560, 820), (650, 760), (700, 650), (805, 600)), ((640, 900), (720, 860), (760, 760), (810, 700)), ((470, 760), (560, 600), (700, 520), (805, 500))][k]
        S.init(f"#{s}-bd{k}", {"opacity": 0})
        S.ft(f"#{s}-bd{k}", {"opacity": 0}, {"opacity": 1}, W24 + 0.3 + k * 0.1, 0.1, "none")
        along(S, f"#{s}-bd{k}", CONk, W24 + 0.3 + k * 0.1, W28 + 0.35 + k * 0.08, n=10)
        S.ft(f"#{s}-bd{k}", {"opacity": 1}, {"opacity": 0}, W28 + 0.35 + k * 0.08, 0.15, "none")
    # mini Reel: alive the whole time, stamped frame on "dibangun", leaves before the roll-up
    minireel_anim(S, f"{s}-mr", S.t0, end, period=0.9, amp=1.1)
    S.keys(f"#{s}-reel", [(S.t0, {"y": -30, "opacity": 0, "rotation": 4}, None), (S.W(21), {"opacity": 0}, "none"),
                          (S.W(23), {"y": 0, "opacity": 1, "rotation": 0}, "power3.out"),
                          (W26, {"scale": 1}, "none"), (W26 + 0.08, {"scale": 0.96}, "power2.in"), (W26 + 0.3, {"scale": 1}, "back.out(2.5)"),
                          (end - 0.45, {"y": 0, "opacity": 1}, "none"), (end - 0.2, {"y": -40, "opacity": 0}, "power2.in")])
    for c in ("tl", "tr", "bl", "br"):
        S.init(f"#{s}-cn{c}", {"opacity": 0, "scale": 1.8})
        S.ft(f"#{s}-cn{c}", {"opacity": 0, "scale": 1.8}, {"opacity": 1, "scale": 1}, W26 - 0.04, 0.2, "power4.out")
        S.ft(f"#{s}-cn{c}", {"opacity": 1}, {"opacity": 0}, end - 0.45, 0.2, "power2.in")
