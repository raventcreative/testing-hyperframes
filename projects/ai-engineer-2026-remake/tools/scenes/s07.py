"""S07 — 05 LLM (w96-106). VO: "Kelima, LLM. Pahami token, konteks, embedding, dan cara model memproses bahasa."
Opens on S06's token track. The camera tilts down along it; letter tiles type in ("AI ENGINEER"), and on "LLM" the
tiles split into token groups (AI | ENGIN | EER) with navy token bars. EXPLAIN MODE on "Pahami token, konteks,
embedding": half-body, chips TOKEN / KONTEKS / EMBEDDING; behind him the context frame closes around the tokens and each
token grows its embedding column. He steps back; on "memproses" an attention matrix fills cell by cell and attention
arcs link the tokens. The token sequence then leaves right along the OUTPUT RAIL (-> S08)."""
from xk import box, r3
from kit import MAT, SIDE_L, part, shadow, chip, grid_floor, blur_wrap, explain, FLOOR_Y
from kit_b import rail, TRACK, OUT_Y, ICON_B, pop_chip

TXT = "AI ENGINEER"
PITCH, TW, TH = 76, 68, 84
X0 = 122
RY = TRACK[1]                       # rail y (world)
TY = RY - 13 - TH - 4               # tile top (sits on the rail)
GROUPS = [[0, 1], [3, 4, 5, 6, 7], [8, 9, 10]]
SHIFT = [-26, 0, 26]
SHADE = ["#0A0D2C", "#294B77", "#5a82bb"]
CAM_Y = -(RY - OUT_Y)               # camera tilt that brings the rail to OUT_Y on screen
MX, MY, MC = 600, 1330, 92           # attention matrix (world) origin + cell


def gx(k):
    g = next(i for i, grp in enumerate(GROUPS) if k in grp)
    return X0 + PITCH * k + SHIFT[g]


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    # ---------------------------------------------------------------- back
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(rail(f"{s}-rail", TRACK[0], RY, TRACK[2]))
    # output extension of the rail (to the right edge)
    S.back.append(f'<div class="abs" id="{s}-ext" style="{box(TRACK[2] - 20, RY - 13, 1180 - TRACK[2], 26)}border-radius:13px;{MAT["alu"]}">'
                  f'<div class="abs" style="left:10px;right:0;top:10px;height:6px;border-radius:3px;background:#1c3561;opacity:.85"></div></div>')
    # context frame (aluminium brackets around the token row)
    S.back.append(f'<div class="abs" id="{s}-ctx" style="{box(80, TY - 40, 920, TH + 80)}border-radius:26px;border:5px solid #9aa6b6;'
                  f'box-shadow:inset 0 0 0 2px rgba(255,255,255,.8),0 14px 26px -16px rgba(10,13,44,.4)"></div>')
    S.back.append(f'<div class="abs" id="{s}-ctxl" style="left:96px;top:{TY - 76}px"><span class="tx" style="font:700 26px/1 Poppins;letter-spacing:.12em">KONTEKS</span></div>')
    for k, ch in enumerate(TXT):
        if ch == " ":
            continue
        S.back.append(f'<div class="abs" id="{s}-t{k}" style="{box(X0 + PITCH * k, TY, TW, TH)}border-radius:14px;{MAT["porcelain"]}box-shadow:inset 0 2px 0 #fff,inset 0 -5px 0 rgba(41,75,119,.18),0 14px 20px -10px rgba(10,13,44,.55);'
                      f'font:700 52px/{TH}px Poppins;color:#0A0D2C;text-align:center">{ch}</div>')
    for g, grp in enumerate(GROUPS):
        x0 = X0 + PITCH * grp[0] + SHIFT[g]
        w = PITCH * (len(grp) - 1) + TW
        S.back.append(f'<div class="abs" id="{s}-bar{g}" style="{box(x0, TY - 18, w, 10)}border-radius:5px;background:{SHADE[g]}"></div>')
        # embedding column (4 bars) above each token
        cx = x0 + w / 2
        bars = "".join(f'<div class="abs" style="left:0;top:{i * 24}px;width:{36 + 18 * ((g + i) % 3)}px;height:14px;border-radius:7px;background:{SHADE[g]};opacity:{.95 - .15 * i}"></div>' for i in range(4))
        S.back.append(f'<div class="abs" id="{s}-emb{g}" style="{box(cx - 40, TY - 150, 80, 100)}">{bars}</div>')
    # attention matrix (3x3) under the rail + row labels + arcs above the tokens
    cells = ""
    for r in range(3):
        for c in range(3):
            cells += f'<div class="abs" id="{s}-m{r}{c}" style="{box(MX + c * (MC + 8), MY + r * (MC + 8), MC, MC)}border-radius:14px;background:{SHADE[c]};"></div>'
    S.back.append(f'<div class="abs" id="{s}-mat" style="left:0;top:0;width:1080px;height:1920px">'
                  f'<div class="abs" style="{box(MX - 24, MY - 24, 3 * MC + 16 + 48, 3 * MC + 16 + 48)}border-radius:28px;{MAT["glass"]}"></div>'
                  + "".join(f'<div class="abs" id="{s}-c{r}{c}" style="{box(MX + c * (MC + 8), MY + r * (MC + 8), MC, MC)}border-radius:14px;background:rgba(41,75,119,.08)"></div>'
                            for r in range(3) for c in range(3))
                  + cells
                  + "".join(f'<div class="abs" style="left:{MX - 170}px;top:{MY + r * (MC + 8) + 26}px;width:130px;text-align:right">'
                            f'<span class="tx" style="font:700 30px/1 Poppins">{lab}</span></div>' for r, lab in enumerate(["AI", "ENGIN", "EER"]))
                  + '</div>')
    cxs = [X0 + PITCH * (g[0] + g[-1]) / 2 + TW / 2 + SHIFT[i] for i, g in enumerate(GROUPS)]
    arcs = []
    for k, (a, b) in enumerate(((0, 1), (1, 2), (0, 2))):
        xa, xb = cxs[a], cxs[b]
        h = 60 + 40 * (k == 2)
        arcs.append(f'<path id="{s}-arc{k}" d="M{xa},{TY - 26} C{xa},{TY - 26 - h} {xb},{TY - 26 - h} {xb},{TY - 26}" fill="none" stroke="{SHADE[1]}" '
                    f'stroke-width="5" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>')
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">{"".join(arcs)}</svg>')
    S.back.append(f'<div class="abs" id="{s}-lab" style="left:{MX - 24}px;top:{MY + 3 * MC + 60}px"><span class="badge" style="font:700 30px/1 Poppins;padding:10px 16px">05 LLM</span></div>')
    blur_wrap(S)
    S.front.append(chip(f"{s}-k1", 40, 446 - CAM_Y, "TOKEN", ICON_B["tiles"], size=30))
    S.front.append(chip(f"{s}-k2", 330, 446 - CAM_Y, "KONTEKS", ICON_B["window"], size=30, dark=True))
    S.front.append(chip(f"{s}-k3", 660, 446 - CAM_Y, "EMBEDDING", ICON_B["vec"], size=30))

    # ---------------------------------------------------------------- motion
    llm = W(97)
    S.cam([(t0, {"y": 0, "x": 0, "scale": 1}, None), (t0 + 0.7, {"y": CAM_Y, "x": 0, "scale": 1}, "power3.inOut"),
           (t1 - 0.55, {"y": CAM_Y, "x": 0, "scale": 1}, "none"), (t1, {"y": CAM_Y, "x": -60, "scale": 1}, "power2.in")])
    # tiles type in (drop onto the rail), then split into token groups on "LLM"
    ks = [k for k, ch in enumerate(TXT) if ch != " "]
    for n, k in enumerate(ks):
        sel = f"#{s}-t{k}"
        S.init(sel, {"y": -120, "opacity": 0, "x": 0, "rotation": -6})
        S.ft(sel, {"y": -120, "opacity": 0, "rotation": -6}, {"y": 0, "opacity": 1, "rotation": 0}, t0 + 0.35 + 0.045 * n, 0.26, "back.out(2)")
        g = next(i for i, grp in enumerate(GROUPS) if k in grp)
        if SHIFT[g]:
            S.ft(sel, {"x": 0}, {"x": SHIFT[g]}, llm - 0.05, 0.35, "power3.out")
    for g in range(3):
        S.init(f"#{s}-bar{g}", {"scaleX": 0, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-bar{g}", {"scaleX": 0}, {"scaleX": 1}, llm + 0.15 + 0.08 * g, 0.3, "power3.out")
    S.fx(t0 + 0.4, "type", 0.04)
    S.fx(llm, "click", 0.06)
    # context frame closes (behind the blurred explain), embeddings grow
    S.init(f"#{s}-ctx", {"scaleX": 1.25, "opacity": 0, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-ctx", {"scaleX": 1.25, "opacity": 0}, {"scaleX": 1, "opacity": 1}, W(100) - 0.05, 0.4, "power3.out")
    S.init(f"#{s}-ctxl", {"opacity": 0})
    S.ft(f"#{s}-ctxl", {"opacity": 0}, {"opacity": 1}, W(100) + 0.2, 0.3, "power2.out")
    for g in range(3):
        S.init(f"#{s}-emb{g}", {"scaleY": 0, "opacity": 0, "transformOrigin": "50% 100%"})
        S.ft(f"#{s}-emb{g}", {"scaleY": 0, "opacity": 0}, {"scaleY": 1, "opacity": 1}, W(101) + 0.08 * g, 0.35, "back.out(1.8)")
    # attention matrix: panel rises, cells fill on "memproses", arcs light between the tokens
    mp = W(105)
    S.init(f"#{s}-mat", {"opacity": 0, "y": 60})
    S.ft(f"#{s}-mat", {"opacity": 0, "y": 60}, {"opacity": 1, "y": 0}, W(103) - 0.1, 0.4, "power3.out")
    ATT = {(0, 0): .9, (0, 1): .35, (0, 2): .2, (1, 0): .5, (1, 1): .9, (1, 2): .45, (2, 0): .25, (2, 1): .6, (2, 2): .95}
    for n, ((r, c), v) in enumerate(sorted(ATT.items())):
        sel = f"#{s}-m{r}{c}"
        S.init(sel, {"opacity": 0, "scale": 0.4})
        S.ft(sel, {"opacity": 0, "scale": 0.4}, {"opacity": v, "scale": 1}, mp - 0.1 + 0.05 * n, 0.25, "back.out(2)")
    for k in range(3):
        S.init(f"#{s}-arc{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-arc{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, mp + 0.1 + 0.15 * k, 0.4, "power2.inOut")
    S.init(f"#{s}-lab", {"opacity": 0, "y": 16})
    S.ft(f"#{s}-lab", {"opacity": 0, "y": 16}, {"opacity": 1, "y": 0}, llm + 0.1, 0.3, "power3.out")
    S.fx(mp, "key", 0.04)
    # hand-off: the token sequence leaves right along the output rail
    ho = t1 - 0.6
    S.init(f"#{s}-ext", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-ext", {"scaleX": 0}, {"scaleX": 1}, ho - 0.25, 0.35, "power3.out")
    for n, k in enumerate(ks):
        g = next(i for i, grp in enumerate(GROUPS) if k in grp)
        S.ft(f"#{s}-t{k}", {"x": SHIFT[g]}, {"x": SHIFT[g] + 760}, ho + 0.02 * (len(ks) - n), 0.5, "power2.in")
    for g in range(3):
        S.ft(f"#{s}-bar{g}", {"x": 0}, {"x": 760}, ho + 0.05, 0.5, "power2.in")
        S.ft(f"#{s}-emb{g}", {"opacity": 1}, {"opacity": 0}, ho - 0.1, 0.25, "power2.in")
    for sel in (f"#{s}-mat", f"#{s}-ctx", f"#{s}-ctxl", f"#{s}-lab"):
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, ho - 0.1, 0.3, "power2.in")
    S.fx(ho, "whoosh", 0.04)
    t_in, t_out = W(98) - 0.3, W(103) - 0.12
    pop_chip(S, f"#{s}-k1", W(99) - 0.05, t_out - 0.1, -3)
    pop_chip(S, f"#{s}-k2", W(100) - 0.05, t_out - 0.1, 2)
    pop_chip(S, f"#{s}-k3", W(101) - 0.05, t_out - 0.1, -2)

    # ---------------------------------------------------------------- mascot
    start = dict(SIDE_L, fx=225, yaw=30)
    low = {"fx": 200, "fy": 1880, "h": 800, "yaw": 26, "pitch": 6}
    S.mv([(t0, start, None), (t0 + 0.7, low, "power3.inOut"), (llm, dict(low, yaw=32), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.4, "explain", 0.35), (llm - 0.1, "present", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (t0 + 0.5, "palmUp", 0.35)])
    S.act("head", [(t0, [0.05, 0.3, 0], 0.3), (t0 + 0.5, [-0.08, 0.36, 0.03], 0.35), (llm, [-0.03, 0.42, -0.04], 0.3)])
    explain(S, t_in, t_out, 98, 102, seed=3, enter=dict(low, yaw=32), leave=dict(low, yaw=28))
    S.mv([(t_out + 0.5, dict(low, yaw=28), None), (t1, dict(low, yaw=34, fx=215), "sine.inOut")])
    S.act("armL", [(t_out + 0.2, "explainHi", 0.3), (mp, "present", 0.3), (ho, "low", 0.4)])
    S.act("armR", [(t_out + 0.2, "palmUp", 0.35), (ho + 0.1, "low", 0.4)])
    S.act("head", [(t_out + 0.2, [-0.02, 0.35, 0], 0.35), (mp, [0.06, 0.32, 0.03], 0.3), (ho, [0.0, 0.45, 0], 0.3)])
