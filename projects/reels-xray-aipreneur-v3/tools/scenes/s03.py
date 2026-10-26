"""S03 — TYPOGRAPHY EXTRACTION (5.18–7.22)  VO: "Teks, kartu, transisi,"
Opens on S02's type plate (glass, navy type slugs). "Teks": the slugs melt and the word rises out of the plate as
dimensional porcelain letters with navy sidewalls (each letter at its own speed). "kartu": the card sheet behind
unfolds card by card on paper hinges, linked to the type plate by motion connectors. "transisi": a ribbon swoops
from the type plate around to the cards; its tail straightens into a rail (hand-off to the S04 camera rail).
A selection frame (four navy corners) follows the spoken words. Slow circular camera move shows the thickness."""
import math
from xk import box, screw, shadow, apex, extrude_text, rivets_line, r3

SFX = [(5.84, "pop", 0.08), (6.44, "whoosh", 0.07)]

PLX, PLY, PLW, PLH = 250, 470, 680, 400        # type plate
CLX, CLY, CLW, CLH = 330, 1010, 660, 330       # card layer sheet
LETTERS = [("T", 0, 0.0), ("e", 132, 0.07), ("k", 262, 0.03), ("s", 392, 0.11)]   # glyph, x offset, delay
LX0, LY0, LSIZE = 330, 540, 200


def cubic_len(p0, p1, p2, p3, n=200):
    L, prev = 0.0, p0
    for i in range(1, n + 1):
        t = i / n
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t * t * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t * t * p2[1] + t ** 3 * p3[1]
        L += math.hypot(x - prev[0], y - prev[1]); prev = (x, y)
    return L


def build(S):
    s = S.id
    S.persp_origin = (590, 600)
    S.css.append(f"#{s}-persp {{ perspective: 1600px; }}")
    W10, W11, W12 = S.W(10), S.W(11), S.W(12)       # Teks 5.28, kartu 5.84, transisi 6.44
    t0, t1 = S.t0, S.t1
    # ---------------- far plane: tilted grid sheet + rails (workshop wall)
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs grid-paper" style="{box(170, 430, 840, 1100)}border-radius:28px;opacity:.7;box-shadow:0 30px 60px -30px rgba(28,51,84,.25)"></div>'
                 f'<div class="abs" style="{box(120, 1560, 940, 6)}border-radius:3px;background:rgba(172,198,231,.55)"></div>'
                 f'<div class="abs" style="{box(120, 1584, 940, 3)}border-radius:2px;background:rgba(172,198,231,.35)"></div>'
                 + "".join(f'<div class="abs" style="{box(190 + k * 60, 445, 2, 18)}background:rgba(58,98,153,.35)"></div>' for k in range(14))
                 + '</div>')
    # ---------------- mid: type plate + letters (front), card sheet (behind), connectors, ribbon, rail
    plate = (f'<div class="abs glass" id="{s}-plate" style="{box(PLX, PLY, PLW, PLH)}border-radius:22px;border:2px solid rgba(41,75,119,.7);'
             f'background:linear-gradient(135deg,rgba(255,255,255,.82),rgba(232,240,251,.6) 55%,rgba(203,219,244,.5))">'
             f'<div class="abs" id="{s}-slug1" style="{box(60, 70, 330, 34)}border-radius:17px;background:#294b77;box-shadow:0 3px 0 rgba(28,51,84,.35)"></div>'
             f'<div class="abs" id="{s}-slug2" style="{box(60, 124, 470, 22)}border-radius:11px;background:#acc6e7"></div>'
             f'<div class="abs" style="{box(60, PLH - 64, 420, 14)}border-radius:7px;background:#cbdbf4"></div>'
             f'<div class="abs" style="{box(60, PLH - 40, 260, 14)}border-radius:7px;background:#cbdbf4"></div>'
             f'{screw(22, 22, 20, 10)}{screw(PLW - 22, 22, -30, 10)}{screw(22, PLH - 22, 50, 10)}{screw(PLW - 22, PLH - 22, 5, 10)}'
             + "".join(f'<div class="abs" style="{box(PLW - 30, 60 + k * 26, 12, 2)}background:rgba(41,75,119,.45)"></div>' for k in range(11))
             + '</div>')
    letters = []
    for k, (ch, dx, _) in enumerate(LETTERS):
        letters.append(f'<div class="abs" id="{s}-lsh{k}" style="{box(LX0 + dx + 8, LY0 + 196, 120, 22)}border-radius:50%;background:radial-gradient(ellipse,rgba(28,51,84,.38),rgba(28,51,84,0) 70%)"></div>')
        letters.append(f'<div class="abs p3" style="left:{LX0 + dx}px;top:{LY0}px">{extrude_text(f"{s}-ch{k}", ch, LSIZE, layers=14, step=2.3, stroke="#3a6299")}</div>')
    # card sheet (porcelain) with three hinged cards that unfold
    cards = []
    for k, (x, kind) in enumerate(((36, "navy"), (250, "white"), (464, "ice"))):
        inner = ""
        if kind == "navy":
            inner = (f'<div class="abs" style="{box(118, 26, 50, 50)}border-radius:50%;background:radial-gradient(circle at 35% 30%,#e9fbf4,#9fd8c4)"></div>'
                     f'<div class="abs" style="{box(22, 180, 120, 12)}border-radius:6px;background:#cbdbf4"></div>')
            bg = "linear-gradient(150deg,#3a6299,#1c3354)"
        elif kind == "white":
            inner = (f'<div class="abs" style="{box(22, 30, 140, 16)}border-radius:8px;background:#294b77"></div>'
                     f'<div class="abs" style="{box(22, 60, 110, 12)}border-radius:6px;background:#cbdbf4"></div>'
                     f'<div class="abs" style="{box(22, 110, 156, 80)}border-radius:10px;background:linear-gradient(160deg,#e8f0fb,#cbdbf4)"></div>')
            bg = "linear-gradient(160deg,#ffffff,#eef3fa)"
        else:
            inner = (f'<div class="abs" style="{box(30, 40, 80, 80)}border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffffff,#acc6e7)"></div>'
                     f'<div class="abs" style="{box(22, 160, 90, 26)}border-radius:13px;background:#9fd8c4"></div>')
            bg = "linear-gradient(160deg,#e8f0fb,#cbdbf4)"
        cards.append(f'<div class="abs" style="{box(x + 4, 56, 186, 226)}border-radius:14px;background:rgba(41,75,119,.06);border:2px dashed rgba(41,75,119,.28)"></div>'   # card footprint
                     f'<div class="abs" id="{s}-cd{k}" style="{box(x, 50, 190, 230)}border-radius:14px;background:{bg};box-shadow:0 14px 22px -10px rgba(28,51,84,.4),inset 1px 1px 0 rgba(255,255,255,.6)">{inner}</div>'
                     f'<div class="abs" style="{box(x + 30, 44, 130, 10)}border-radius:5px;background:linear-gradient(180deg,#ffffff,#acc6e7);box-shadow:0 2px 3px rgba(28,51,84,.3)"></div>')   # paper hinge
    sheet = (f'<div class="abs por p3" id="{s}-sheet" style="{box(CLX, CLY, CLW, CLH)}border-radius:22px">{"".join(cards)}'
             f'{rivets_line(30, CLH - 18, CLW - 30, CLH - 18, 9)}</div>')
    # motion connectors: navy rods with ball joints from the plate's bottom edge to the sheet's top edge
    conn = []
    for k, x in enumerate((420, 590, 760)):
        conn.append(f'<div class="abs" id="{s}-cn{k}" style="{box(x - 3, PLY + PLH, 6, CLY - PLY - PLH)}border-radius:3px;background:linear-gradient(90deg,#3a6299,#1c3354);transform-origin:50% 0%"></div>')
        conn.append(f'<div class="pin" style="left:{x - 5}px;top:{PLY + PLH - 5}px"></div><div class="pin" style="left:{x - 5}px;top:{CLY - 5}px"></div>')
    # transition ribbon (SVG, drawn on "transisi") and the rail it turns into
    p0, p1, p2, p3 = (930, 640), (1130, 900), (700, 1000), (440, 1312)
    L = cubic_len(p0, p1, p2, p3)
    rib = (f'<svg class="abs" style="left:0;top:0;overflow:visible" width="1080" height="1920" viewBox="0 0 1080 1920">'
           f'<defs><linearGradient id="{s}-rg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a6299"/><stop offset="1" stop-color="#1c3354"/></linearGradient></defs>'
           f'<path id="{s}-rib2" d="M{p0[0]},{p0[1] + 16} C{p1[0]},{p1[1] + 16} {p2[0]},{p2[1] + 16} {p3[0]},{p3[1] + 16}" fill="none" stroke="#cbdbf4" stroke-width="22" stroke-linecap="round" '
           f'stroke-dasharray="{r3(L)}" stroke-dashoffset="{r3(L)}"/>'
           f'<path id="{s}-rib" d="M{p0[0]},{p0[1]} C{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}" fill="none" stroke="url(#{s}-rg)" stroke-width="16" stroke-linecap="round" '
           f'stroke-dasharray="{r3(L)}" stroke-dashoffset="{r3(L)}"/></svg>')
    rail = (f'<div class="abs" id="{s}-rail" style="{box(430, 1300, 640, 24)}">'
            + "".join(f'<div class="abs" style="{box(30 + k * 62, -14, 16, 52)}border-radius:4px;background:linear-gradient(90deg,#ffffff,#dbe6f6 60%,#acc6e7);box-shadow:2px 3px 3px rgba(28,51,84,.3)"></div>' for k in range(10))
            + f'<div class="abs" style="{box(0, 0, 640, 9)}border-radius:5px;background:linear-gradient(180deg,#5d84b9,#1c3354);box-shadow:0 4px 6px rgba(28,51,84,.4)"></div>'
            + f'<div class="abs" style="{box(0, 17, 640, 9)}border-radius:5px;background:linear-gradient(180deg,#5d84b9,#1c3354);box-shadow:0 4px 6px rgba(28,51,84,.4)"></div>'
            + '</div>')
    S.mid.append(shadow(CLX - 20, CLY + CLH - 20, CLW + 40, 80, 0.8))
    S.mid.append(f'<div class="abs p3" id="{s}-grpB" style="{box(0, 0, 1080, 1920)}">{sheet}</div>')
    S.mid.append("".join(conn))
    S.mid.append(f'<div class="abs p3" id="{s}-grpA" style="{box(0, 0, 1080, 1920)}">{plate}{"".join(letters)}</div>')
    S.mid.append(rib)
    S.mid.append(rail)
    # selection corners (follow the spoken words)
    for c in ("tl", "tr", "bl", "br"):
        S.mid.append(f'<div class="corner {c}" id="{s}-sel{c}" style="left:0;top:0"></div>')
    # ---------------- near plane
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(960, 470, 200, 26)}border-radius:13px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px)"></div>'
                  f'<div class="abs" style="{box(900, 1500, 160, 160)}border-radius:50%;border:12px solid rgba(255,255,255,.75);filter:blur(5px)"></div></div>')
    apex(S, S.near, f"{s}-ap", 590, 660, W10 + 0.12, size=620, sparks=6, seed=21, op=0.6)

    # ---------------- motion
    # circular camera move (reveals letter thickness), slight push
    S.cam([(t0, {"z": 520, "x": 0, "y": 130, "rotationY": -6, "rotationX": 2}, None),
           (W10 + 0.12, {"z": 60, "y": 20, "rotationY": -18, "rotationX": 8}, "expo.out"),
           (W11, {"z": 30, "rotationY": -8, "rotationX": 7, "y": 30}, "sine.inOut"),
           (W12, {"z": 10, "rotationY": 8, "rotationX": 6, "y": 30}, "sine.inOut"),
           (t1, {"z": 90, "rotationY": 18, "rotationX": 12, "y": -10, "x": -30}, "power2.in")])
    # type slugs melt into the letters
    for sl in ("slug1", "slug2"):
        S.init(f"#{s}-{sl}", {"opacity": 1, "scaleX": 1, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-{sl}", {"opacity": 1, "scaleX": 1}, {"opacity": 0, "scaleX": 0.2}, W10 - 0.08, 0.3, "power3.in")
    for k, (ch, dx, dl) in enumerate(LETTERS):
        cid = f"#{s}-ch{k}"
        S.init(cid, {"z": -40, "y": 30, "opacity": 0, "rotationX": -35, "transformOrigin": "50% 100%"})
        S.ft(cid, {"z": -40, "y": 30, "opacity": 0, "rotationX": -35}, {"z": 70 + 22 * (k % 2), "y": -6, "opacity": 1, "rotationX": 0},
             W10 - 0.04 + dl, 0.42 + 0.08 * (k % 3), "back.out(1.6)")
        S.ft(cid, {"z": 70 + 22 * (k % 2), "y": -6, "rotationX": 0}, {"z": 92 + 30 * (k % 2), "y": -18 - 6 * k, "rotationX": 4},
             W10 + 0.5 + dl, t1 - W10 - 0.5 - dl, "sine.inOut")
        S.init(f"#{s}-lsh{k}", {"opacity": 0, "scaleX": 0.4})
        S.ft(f"#{s}-lsh{k}", {"opacity": 0, "scaleX": 0.4}, {"opacity": 1, "scaleX": 1}, W10 + dl, 0.45, "power2.out")
    # card sheet unfolds card by card on "kartu"; connectors extend from the plate
    S.init(f"#{s}-sheet", {"z": -120, "rotationX": 18, "transformOrigin": "50% 0%"})
    S.ft(f"#{s}-sheet", {"z": -120, "rotationX": 18}, {"z": -60, "rotationX": 6}, W11 - 0.2, 0.6, "power3.out")
    for k in range(3):
        S.init(f"#{s}-cd{k}", {"rotationX": -96, "transformOrigin": "50% 0%", "transformPerspective": 900})
        S.ft(f"#{s}-cd{k}", {"rotationX": -96}, {"rotationX": 8}, W11 - 0.05 + 0.12 * k, 0.34, "power3.out")
        S.ft(f"#{s}-cd{k}", {"rotationX": 8}, {"rotationX": 0}, W11 + 0.29 + 0.12 * k, 0.3, "sine.inOut")   # paper joint flex
    for k in range(3):
        S.init(f"#{s}-cn{k}", {"scaleY": 0})
        S.ft(f"#{s}-cn{k}", {"scaleY": 0}, {"scaleY": 1}, W11 - 0.25 + 0.06 * k, 0.4, "power3.out")
    # ribbon draws on "transisi", then the rail rolls out from its tail
    S.ft(f"#{s}-rib", {"strokeDashoffset": r3(L)}, {"strokeDashoffset": 0}, W12 - 0.06, 0.5, "power2.inOut")
    S.ft(f"#{s}-rib2", {"strokeDashoffset": r3(L)}, {"strokeDashoffset": 0}, W12 + 0.02, 0.5, "power2.inOut")
    S.init(f"#{s}-rail", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-rail", {"scaleX": 0}, {"scaleX": 1}, W12 + 0.42, 0.42, "power3.inOut")
    S.init(f"#{s}-grpA", {"z": 0})
    # selection frame follows the words: letters -> card sheet -> ribbon/rail
    targets = [(t0, (PLX - 14, PLY - 14, PLW + 28, PLH + 28)), (W10 + 0.05, (LX0 - 30, LY0 - 20, 560, 250)),
               (W11 + 0.02, (CLX - 14, CLY + 30, CLW + 28, 270)), (W12 + 0.05, (400, 1250, 670, 130))]
    for c in ("tl", "tr", "bl", "br"):
        def pos(r):
            x, y, w, h = r
            return {"x": x if c in ("tl", "bl") else x + w - 26, "y": y if c in ("tl", "tr") else y + h - 26}
        S.init(f"#{s}-sel{c}", pos(targets[0][1]))
        for (ta, ra), (tb, rb) in zip(targets, targets[1:]):
            S.ft(f"#{s}-sel{c}", pos(ra), pos(rb), tb - 0.06, 0.3, "expo.out")
