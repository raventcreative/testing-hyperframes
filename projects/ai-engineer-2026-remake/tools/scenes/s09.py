"""S09 — 07 RAG, premium showpiece (w123-140). VO: "Ketujuh, RAG. Sebelum menjawab, sistem mencari bagian dokumen yang
relevan. Jadi jawaban bisa didukung data yang kita berikan."
Opens on S08's cabinet spine: an archive cabinet unfolds from it. On "RAG" the middle drawer springs open; three pages
rise and, on "Sebelum menjawab", slice into chunks that file themselves onto an indexed shelf. A question chip sends a
track up into the index and a scanner sweeps the rows ("mencari bagian dokumen"); on "relevan" only two chunks light
and lift (DOKUMEN RELEVAN), the rest dim. EXPLAIN MODE on "Jadi jawaban bisa didukung data yang kita berikan": chips
DATA KITA -> JAWABAN; behind him the two chunks fly into the answer sheet as two source tabs (retrieval vs generation:
chunks are pulled, the answer body is written). He steps back; the archive recedes and the answer sheet stands alone
exactly at kit.ANSWER_CARD (-> S10)."""
from xk import box, r3
from kit import MAT, SIDE_R, part, shadow, chip, grid_floor, blur_wrap, explain, ICON, ANSWER_CARD, FLOOR_Y
from kit_b import CAB_SPINE, pop_chip, arrow, draw_arrow

CX, CY, CW, CH = 290, 640, 500, 760                 # cabinet
DRW = [(CY + 24 + k * 244, k) for k in range(3)]    # drawer front tops
COLS = [110, 330, 550, 770]
ROWS = [432, 512, 592]
KW, KH = 200, 64
REL = [(0, 2), (2, 1)]                              # the two relevant chunks (row, col)
AX, AY, AW, AH = ANSWER_CARD


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    # ---------------------------------------------------------------- back
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(f'<div class="abs" id="{s}-arch" style="left:0;top:0;width:1080px;height:1920px">')
    S.back.append(shadow(CX - 40, FLOOR_Y - 70, CW + 80, 90, 0.5, f"{s}-csh"))
    # cabinet body + 3 drawers (middle one opens)
    fronts = ""
    for top, k in DRW:
        if k == 1:
            continue
        fronts += _drawer(s, k, 20, top - CY)
    cav = f'<div class="abs" id="{s}-cav" style="left:20px;top:{DRW[1][0] - CY}px;width:{CW - 40}px;height:220px;border-radius:14px;background:linear-gradient(180deg,#05070d,#1c2536);box-shadow:inset 0 10px 20px rgba(0,0,0,.6)"></div>'
    S.back.append(f'<div class="abs" id="{s}-cab" style="{box(CX, CY, CW, CH)}border-radius:26px;{MAT["porcelain"]}">{fronts}{cav}</div>')
    # pages that rise from the open drawer (behind the drawer front)
    for k in range(3):
        strips = "".join(f'<div class="abs" style="left:24px;top:{24 + i * 44}px;width:{150 - 20 * (i % 2)}px;height:12px;border-radius:6px;background:rgba(41,75,119,.35)"></div>' for i in range(4))
        S.back.append(f'<div class="abs" id="{s}-pg{k}" style="{box(370 + k * 10, DRW[1][0] + 20, 220, 200)}border-radius:10px;background:#fff;'
                      f'box-shadow:0 12px 22px -12px rgba(10,13,44,.45),0 0 0 1px rgba(41,75,119,.12)">{strips}</div>')
    S.back.append(_drawer(s, 1, CX + 20, DRW[1][0]))
    S.back.append(f'<div class="abs" id="{s}-lab" style="left:{CX + 20}px;top:{CY + CH + 24}px"><span class="badge" style="font:700 30px/1 Poppins;padding:10px 16px">07 RAG</span></div>')
    # index shelf: 12 chunk cards
    S.back.append(f'<div class="abs" id="{s}-shelf" style="{box(90, 410, 900, 266)}border-radius:24px;{MAT["glass"]}"></div>')
    for r, y in enumerate(ROWS):
        for c, x in enumerate(COLS):
            n = r * 4 + c + 1
            S.back.append(f'<div class="abs" id="{s}-k{r}{c}" style="{box(x, y, KW, KH)}border-radius:12px;background:#fff;'
                          f'box-shadow:0 8px 14px -10px rgba(10,13,44,.45),0 0 0 1px rgba(41,75,119,.12)">'
                          f'<div class="abs" style="left:12px;top:0;font:700 22px/{KH}px Poppins;color:#294B77">#{n:02d}</div>'
                          f'<div class="abs" style="left:74px;top:18px;width:100px;height:10px;border-radius:5px;background:rgba(41,75,119,.3)"></div>'
                          f'<div class="abs" style="left:74px;top:36px;width:70px;height:10px;border-radius:5px;background:rgba(41,75,119,.2)"></div></div>')
            if (r, c) in REL:
                S.back.append(f'<div class="abs" id="{s}-h{r}{c}" style="{box(x, y, KW, KH)}border-radius:12px;background:linear-gradient(105deg,#0A0D2C,#294B77);'
                              f'box-shadow:0 14px 22px -10px rgba(10,13,44,.6)">'
                              f'<div class="abs" style="left:12px;top:0;font:700 22px/{KH}px Poppins;color:#fff">#{n:02d}</div>'
                              f'<div class="abs" style="left:74px;top:18px;width:100px;height:10px;border-radius:5px;background:rgba(255,255,255,.6)"></div>'
                              f'<div class="abs" style="left:74px;top:36px;width:70px;height:10px;border-radius:5px;background:rgba(255,255,255,.4)"></div></div>')
    S.back.append(f'<div class="abs" id="{s}-scan" style="{box(100, ROWS[0] - 6, 880, KH + 12)}border-radius:14px;'
                  f'background:linear-gradient(90deg,rgba(120,170,255,0),rgba(120,170,255,.28),rgba(120,170,255,0));border:2px solid rgba(41,75,119,.35)"></div>')
    S.back.append(f'<div class="abs" id="{s}-rel" style="left:600px;top:690px"><span class="badge" style="font:700 30px/1 Poppins;padding:10px 16px">DOKUMEN RELEVAN</span></div>')
    # question chip + the track it sends into the index
    S.back.append(chip(f"{s}-q", 40, 1480, "Pertanyaan", ICON["search"], size=30))
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-trk" d="M150,1478 C150,1200 70,900 70,700 L70,{ROWS[0] + 32} L100,{ROWS[0] + 32}" fill="none" stroke="#294B77" stroke-width="6" '
                  f'stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1" pathLength="1"/></svg>')
    S.back.append('</div>')
    # the answer sheet (assembles behind the explain, stands alone at the end)
    body = "".join(f'<div class="abs" id="{s}-ln{i}" style="left:30px;top:{92 + i * 40}px;width:{[340, 300, 330, 220][i]}px;height:14px;border-radius:7px;background:rgba(41,75,119,{[.55, .4, .4, .3][i]})"></div>' for i in range(4))
    S.back.append(f'<div class="abs" id="{s}-ans" style="{box(AX, AY, AW, AH)}border-radius:22px;{MAT["porcelain"]}">'
                  f'<div class="abs" style="left:30px;top:30px"><span class="tx" style="font:700 30px/1 Poppins;letter-spacing:.06em">JAWABAN</span></div>{body}'
                  + "".join(f'<div class="abs" id="{s}-src{i}" style="left:{220 + i * 90}px;top:-26px;width:76px;height:44px;border-radius:12px 12px 6px 6px;'
                            f'background:linear-gradient(105deg,#0A0D2C,#294B77);font:700 20px/44px Poppins;color:#fff;text-align:center">#{[3, 10][i]:02d}</div>' for i in range(2))
                  + '</div>')
    blur_wrap(S)
    S.front.append(chip(f"{s}-c1", 60, 446, "DATA KITA", ICON["doc"], size=30))
    S.front.append(arrow(f"{s}-a1", 395, 466, 110))
    S.front.append(chip(f"{s}-c2", 530, 446, "JAWABAN", ICON["check"], size=30, dark=True))

    # ---------------------------------------------------------------- motion
    rag = W(124)
    # cabinet unfolds from the spine
    S.init(f"#{s}-cab", {"scaleX": CAB_SPINE[2] / CW, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-cab", {"scaleX": CAB_SPINE[2] / CW}, {"scaleX": 1}, t0 + 0.02, 0.5, "power3.out")
    S.init(f"#{s}-d1", {"scaleX": CAB_SPINE[2] / CW, "transformOrigin": f"{CW / 2 - 20}px 50%", "y": 0, "scale": 1})
    S.ft(f"#{s}-d1", {"scaleX": CAB_SPINE[2] / CW}, {"scaleX": 1}, t0 + 0.02, 0.5, "power3.out")
    S.init(f"#{s}-csh", {"scaleX": 0.3, "opacity": 0})
    S.ft(f"#{s}-csh", {"scaleX": 0.3, "opacity": 0}, {"scaleX": 1, "opacity": 0.5}, t0 + 0.1, 0.5, "power2.out")
    S.init(f"#{s}-lab", {"opacity": 0, "y": 16})
    S.ft(f"#{s}-lab", {"opacity": 0, "y": 16}, {"opacity": 1, "y": 0}, t0 + 0.45, 0.3, "power3.out")
    # RAG: the middle drawer springs open toward camera
    S.ft(f"#{s}-d1", {"y": 0, "scale": 1}, {"y": 120, "scale": 1.1}, rag - 0.06, 0.42, "back.out(1.6)")
    S.fx(rag, "click", 0.07)
    # pages rise from the drawer and fan out, then slice into chunks that file onto the shelf
    sb = W(125)
    for k in range(3):
        sel = f"#{s}-pg{k}"
        S.init(sel, {"y": 0, "rotation": 0, "opacity": 0, "x": 0})
        S.ft(sel, {"y": 0, "opacity": 0}, {"y": -330 - 20 * k, "opacity": 1, "x": (k - 1) * 150, "rotation": (k - 1) * 7}, rag + 0.15 + 0.08 * k, 0.5, "power3.out")
        S.ft(sel, {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.7}, sb + 0.12 + 0.06 * k, 0.3, "power2.in")
    S.init(f"#{s}-shelf", {"opacity": 0, "scaleY": 0.6, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-shelf", {"opacity": 0, "scaleY": 0.6}, {"opacity": 1, "scaleY": 1}, sb - 0.1, 0.4, "power3.out")
    for r, y in enumerate(ROWS):
        for c, x in enumerate(COLS):
            k = r * 4 + c
            src = k % 3
            fx_, fy_ = 370 + src * 10 + (src - 1) * 150 + 30, DRW[1][0] + 20 - 330 - 20 * src + 40 + 40 * (k // 3 % 4)
            a = {"x": r3(fx_ - x), "y": r3(fy_ - y), "scale": 0.6, "opacity": 0, "rotation": (src - 1) * 7}
            S.init(f"#{s}-k{r}{c}", a)
            S.ft(f"#{s}-k{r}{c}", a, {"x": 0, "y": 0, "scale": 1, "opacity": 1, "rotation": 0}, sb + 0.15 + 0.035 * k, 0.45, "power3.out")
    S.fx(sb + 0.2, "type", 0.04)
    # question -> track -> scanner sweeps the rows ("mencari bagian dokumen")
    S.init(f"#{s}-q", {"opacity": 0, "x": -60})
    S.ft(f"#{s}-q", {"opacity": 0, "x": -60}, {"opacity": 1, "x": 0}, W(127) - 0.2, 0.35, "back.out(1.8)")
    S.init(f"#{s}-trk", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-trk", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(128) - 0.1, 0.45, "power2.inOut")
    S.init(f"#{s}-scan", {"opacity": 0, "y": 0})
    S.ft(f"#{s}-scan", {"opacity": 0}, {"opacity": 1}, W(128) + 0.3, 0.15, "power2.out")
    S.ft(f"#{s}-scan", {"y": 0}, {"y": ROWS[2] - ROWS[0]}, W(128) + 0.35, W(132) - W(128) - 0.45, "sine.inOut")
    S.ft(f"#{s}-scan", {"opacity": 1}, {"opacity": 0}, W(132) - 0.05, 0.2, "power2.in")
    S.fx(W(128), "whoosh", 0.03)
    # "relevan": only two chunks light and lift, the rest dim
    rl = W(132)
    for r in range(3):
        for c in range(4):
            if (r, c) in REL:
                S.init(f"#{s}-h{r}{c}", {"opacity": 0, "scale": 1, "y": 0})
                S.ft(f"#{s}-h{r}{c}", {"opacity": 0, "scale": 1, "y": 0}, {"opacity": 1, "scale": 1.12, "y": -10}, rl - 0.04, 0.3, "back.out(2.5)")
            else:
                S.ft(f"#{s}-k{r}{c}", {"opacity": 1}, {"opacity": 0.3}, rl, 0.3, "power2.out")
    S.init(f"#{s}-rel", {"opacity": 0, "scale": 0.7, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-rel", {"opacity": 0, "scale": 0.7}, {"opacity": 1, "scale": 1}, rl + 0.1, 0.35, "back.out(2)")
    S.fx(rl, "ping", 0.05)
    # behind the explain: the two chunks fly into the answer sheet as source tabs; the archive recedes
    t_in, t_out = W(133) - 0.3, W(139) - 0.1
    S.init(f"#{s}-ans", {"opacity": 0, "scale": 0.7, "y": 40})
    S.ft(f"#{s}-ans", {"opacity": 0, "scale": 0.7, "y": 40}, {"opacity": 1, "scale": 1, "y": 0}, W(134) - 0.1, 0.45, "power3.out")
    for i, (r, c) in enumerate(REL):
        x, y = COLS[c], ROWS[r]
        tx_, ty_ = AX + 220 + i * 90, AY - 26
        S.ft(f"#{s}-h{r}{c}", {"x": 0, "y": -10, "scale": 1.12, "opacity": 1},
             {"x": r3(tx_ + 38 - (x + KW / 2)), "y": r3(ty_ + 22 - (y + KH / 2)), "scale": 0.38, "opacity": 0}, W(137) - 0.2 + 0.12 * i, 0.5, "power3.inOut")
        S.init(f"#{s}-src{i}", {"opacity": 0, "y": 20})
        S.ft(f"#{s}-src{i}", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, W(137) + 0.22 + 0.12 * i, 0.3, "back.out(2)")
    for i in range(4):
        S.init(f"#{s}-ln{i}", {"scaleX": 0, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-ln{i}", {"scaleX": 0}, {"scaleX": 1}, W(135) + 0.15 * i, 0.3, "power2.out")
    S.init(f"#{s}-arch", {"opacity": 1, "scale": 1, "transformOrigin": "540px 900px"})
    S.ft(f"#{s}-arch", {"opacity": 1, "scale": 1}, {"opacity": 0.35, "scale": 0.94}, W(134), 0.6, "power2.inOut")
    S.ft(f"#{s}-arch", {"opacity": 0.35, "scale": 0.94}, {"opacity": 0, "scale": 0.9}, t_out + 0.3, 0.5, "power2.in")
    pop_chip(S, f"#{s}-c1", W(137) - 0.05, t_out - 0.1, -2)
    draw_arrow(S, f"{s}-a1", W(137) + 0.25, t_out - 0.1)
    pop_chip(S, f"#{s}-c2", W(134) - 0.05, t_out - 0.1, 2)
    S.fx(W(134), "pop", 0.04)
    S.fx(W(137) + 0.3, "click", 0.05)

    # ---------------------------------------------------------------- mascot
    side = dict(SIDE_R, fx=945, fy=1830, h=820, yaw=-26)
    end = {"fx": 935, "fy": 1890, "h": 790, "yaw": -30, "pitch": 6}
    S.mv([(t0, dict(side, yaw=-14), None), (rag, dict(side, yaw=-30), "sine.inOut"), (W(128), dict(side, yaw=-34), "sine.inOut")])
    S.act("armR", [(t0, "low", 0.3), (t0 + 0.2, "open", 0.35), (rag - 0.1, "present", 0.3), (W(127) - 0.2, "point", 0.3), (rl - 0.15, "pointUp", 0.3)])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.3, "explain", 0.35), (W(127), "low", 0.4), (rl, "palmUp", 0.3)])
    S.act("head", [(t0, [0.0, -0.1, 0], 0.3), (rag, [0.05, -0.36, 0.03], 0.3), (W(127), [-0.08, -0.4, -0.02], 0.35),
                   (W(129), [-0.22, -0.32, 0.0], 0.35), (rl, [-0.18, -0.24, 0.05], 0.3)])
    S.act("torso", [(t0, {"chest": [0.02, -0.1, 0]}, 0.3)])
    explain(S, t_in, t_out, 133, 139, seed=5, enter=dict(side, yaw=-34), leave=end)
    S.mv([(t_out + 0.5, end, None), (t1, dict(end, yaw=-34), "sine.inOut")])
    S.act("armR", [(t_out + 0.2, "present", 0.3), (t1 - 0.25, "low", 0.35)])
    S.act("armL", [(t_out + 0.2, "low", 0.35)])
    S.act("head", [(t_out + 0.2, [-0.05, -0.4, 0.02], 0.35)])


def _drawer(s, k, x, y):
    """drawer front (porcelain) with aluminium handle and an index tab."""
    lab = ["DOK A", "DOK B", "DOK C"][k]
    return (f'<div class="abs" id="{s}-d{k}" style="{box(x, y, CW - 40, 220)}border-radius:16px;{MAT["porcelain"]}">'
            f'<div class="abs" style="left:150px;top:96px;width:160px;height:30px;border-radius:15px;{MAT["alu"]}"></div>'
            f'<div class="abs" style="left:24px;top:22px;width:120px;height:44px;border-radius:10px;background:#fff;'
            f'box-shadow:inset 0 0 0 2px rgba(41,75,119,.25);font:700 22px/44px Poppins;color:#294B77;text-align:center">{lab}</div></div>')
