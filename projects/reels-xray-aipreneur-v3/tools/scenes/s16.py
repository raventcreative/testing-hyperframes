"""S16 — QUALITY CONTROL (45.20–50.26)  VO: "Dan hasilnya harus dicek: visual, transisi, terutama sinkron sama suara."
Miniature inspection studio: a porcelain Reel display on a stand, an inspection clipboard (left) and a waveform strip
(below). A porcelain magnifier travels: "visual" -> a tilted card snaps onto the grid, "transisi" -> the split scene
seam aligns, "sinkron" -> word markers slide onto the waveform peaks (apex), "suara" -> mint check. The lens then
centres and becomes an iris (ivory closes around it) = hand-off into S17."""
import math
from xk import box, screw, shadow, rivets_line, apex, minireel, r3
from kit_e import magnifier, check_svg, iris

SFX = [(46.92, "click", 0.1), (48.80, "sparkle", 0.08)]

RX, RY, RW, RH = 400, 446, 380, 664          # reel display frame
SX, SY, SW, SH = RX + 18, RY + 18, RW - 36, RH - 36   # its screen
WX, WY, WW, WH = 438, 1150, 572, 168         # waveform strip
CX_, CY_, CW, CH = 62, 560, 300, 330         # clipboard


def build(S):
    s = S.id
    S.persp_origin = (590, 560)
    WD, WV, WT, WS, WSU = S.W(102), S.W(103), S.W(104), S.W(106), S.W(108)   # dicek 46.18 visual 46.92 transisi 47.60 sinkron 48.80 suara 49.50

    # ---------------- far plane: studio backdrop, two softbox lamps, floor rails
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(150, 300, 780, 1180)}border-radius:390px 390px 36px 36px;opacity:.5"></div>'
                 f'<div class="abs" style="{box(200, 350, 680, 1100)}border-radius:340px 340px 30px 30px;border:2px solid rgba(255,255,255,.8)"></div>'
                 f'<div class="abs por" style="{box(70, 380, 150, 96)}border-radius:20px;transform:rotate(-14deg)"><div class="abs" style="{box(12, 12, 126, 72)}border-radius:12px;background:linear-gradient(160deg,#ffffff,#e8f0fb);box-shadow:0 0 30px 8px rgba(255,255,255,.9)"></div></div>'
                 f'<div class="abs por" style="{box(860, 380, 150, 96)}border-radius:20px;transform:rotate(14deg)"><div class="abs" style="{box(12, 12, 126, 72)}border-radius:12px;background:linear-gradient(160deg,#ffffff,#e8f0fb);box-shadow:0 0 30px 8px rgba(255,255,255,.9)"></div></div>'
                 f'<div class="abs" style="{box(140, 476, 6, 300)}background:linear-gradient(180deg,#cbdbf4,rgba(203,219,244,0));transform:rotate(-14deg)"></div>'
                 f'<div class="abs" style="{box(934, 476, 6, 300)}background:linear-gradient(180deg,#cbdbf4,rgba(203,219,244,0));transform:rotate(14deg)"></div>'
                 f'<div class="abs" style="{box(120, 1430, 860, 6)}border-radius:3px;background:rgba(172,198,231,.55)"></div>'
                 f'<div class="abs" style="{box(120, 1452, 860, 3)}border-radius:2px;background:rgba(172,198,231,.35)"></div></div>')

    # ---------------- hero: reel display on a stand
    m = S.mid
    m.append(shadow(380, 1112, 470, 70, 0.95))
    m.append(f'<div class="abs por" style="{box(540, 1090, 100, 40)}border-radius:10px"></div>')       # stand neck
    m.append(f'<div class="abs por" style="{box(470, 1118, 240, 26)}border-radius:13px"></div>')       # stand foot
    for k in range(9, 0, -1):   # navy sidewall slabs
        c = "#1c3354" if k > 6 else "#294b77" if k > 3 else "#3a6299"
        m.append(f'<div class="abs" style="{box(RX + k * 1.6, RY + k * 1.2, RW, RH)}border-radius:34px;background:{c}"></div>')
    m.append(f'<div class="abs por" style="{box(RX, RY, RW, RH)}border-radius:34px">{screw(22, 22, 30, 10)}{screw(RW - 22, 22, -30, 10)}{screw(22, RH - 22, 60, 10)}{screw(RW - 22, RH - 22, 5, 10)}</div>')
    # screen
    scr = []
    # split scene (seam) — left ice tile, right navy tile (misaligned until "transisi")
    scr.append(f'<div class="abs mr-card" style="{box(20, 26, 152, 196)}border-radius:12px 0 0 12px;background:linear-gradient(160deg,#ffffff,#dbe6f6)">'
               f'<div class="abs" style="{box(18, 26, 70, 70)}border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffffff,#acc6e7)"></div>'
               f'<div class="abs mr-bar ink" style="{box(18, 140, 110, 10)}"></div><div class="abs mr-bar" style="{box(18, 160, 80, 9)}"></div></div>')
    scr.append(f'<div class="abs" id="{s}-tr" style="{box(172, 26, 152, 196)}">'
               f'<div class="abs mr-navy" style="{box(0, 0, 152, 196)}border-radius:0 12px 12px 0">'
               f'<div class="abs" style="{box(-36, 26, 70, 70)}border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffffff,#acc6e7);clip-path:inset(0 0 0 36px)"></div>'
               f'<div class="abs mr-bar" style="{box(20, 140, 100, 10)}background:#cbdbf4"></div></div></div>')
    scr.append(f'<div class="abs" id="{s}-seam" style="{box(170, 20, 4, 208)}border-radius:2px;background:#ffffff;box-shadow:0 0 10px 2px rgba(172,198,231,.95)"></div>')
    # alignment guides (flash on "visual")
    scr.append(f'<div class="abs" id="{s}-gd" style="{box(0, 0, SW, SH)}">'
               f'<div class="abs" style="{box(30, 250, 2, 220)}background:repeating-linear-gradient(180deg,#294b77 0 8px,transparent 8px 14px)"></div>'
               f'<div class="abs" style="{box(SW - 32, 250, 2, 220)}background:repeating-linear-gradient(180deg,#294b77 0 8px,transparent 8px 14px)"></div>'
               f'<div class="abs" style="{box(14, 262, SW - 28, 2)}background:repeating-linear-gradient(90deg,#294b77 0 8px,transparent 8px 14px)"></div></div>')
    # the misaligned card
    scr.append(f'<div class="abs" id="{s}-card" style="{box(30, 262, SW - 60, 160)}">'
               f'<div class="abs mr-card" style="{box(0, 0, SW - 60, 160)}border-radius:14px">'
               f'<div class="abs mr-navy" style="{box(16, 16, 96, 128)}border-radius:10px"></div>'
               f'<div class="abs mr-bar ink" style="{box(128, 30, 120, 12)}"></div><div class="abs mr-bar" style="{box(128, 54, 140, 10)}"></div>'
               f'<div class="abs mr-bar" style="{box(128, 74, 100, 10)}"></div>'
               f'<div class="abs" style="{box(128, 104, 64, 24)}border-radius:12px;background:#9fd8c4"></div></div></div>')
    scr.append(f'<div class="abs mr-bar ink" style="{box(30, 470, 200, 14)}"></div><div class="abs mr-bar" style="{box(30, 496, 260, 12)}"></div>'
               f'<div class="abs mr-bar" style="{box(30, 518, 180, 12)}"></div>')
    # playhead strip at the bottom of the screen
    scr.append(f'<div class="abs" style="{box(30, 568, SW - 60, 6)}border-radius:3px;background:#dbe6f6"></div>'
               f'<div class="abs" id="{s}-ph" style="{box(30, 568, SW - 60, 6)}border-radius:3px;background:#294b77"></div>')
    scr.append(f'<div class="abs" id="{s}-ok" style="{box(SW - 92, 14, 78, 78)}">{check_svg(s + "-ck", 78)}</div>')
    m.append(f'<div class="abs" style="{box(SX, SY, SW, SH)}border-radius:20px;overflow:hidden;background:linear-gradient(170deg,#fbfcfe 0%,#eef3fa 60%,#e2eaf6 100%);'
             f'box-shadow:inset 0 0 0 2px rgba(41,75,119,.5),inset 0 0 0 5px rgba(255,255,255,.9)">{"".join(scr)}</div>')

    # ---------------- inspection clipboard (left): three rows, ticks on the spoken words
    m.append(shadow(CX_ - 10, CY_ + CH - 20, CW + 40, 60, 0.7))
    m.append(f'<div class="abs por" style="{box(CX_, CY_, CW, CH)}border-radius:22px">'
             f'<div class="abs navy-side" style="{box(CW / 2 - 56, -18, 112, 40)}border-radius:12px;box-shadow:0 6px 10px -4px rgba(28,51,84,.45)"></div>'
             f'<div class="abs" style="{box(CW / 2 - 30, -8, 60, 10)}border-radius:5px;background:#acc6e7"></div>'
             f'<div class="abs paper" style="{box(18, 34, CW - 36, CH - 52)}border-radius:12px"></div>{rivets_line(30, CH - 14, CW - 30, CH - 14, 5)}</div>')
    rows = [("visual", WV), ("transisi", WT), ("sinkron", WS)]
    for k, (lab, at) in enumerate(rows):
        y = CY_ + 70 + k * 84
        m.append(f'<div class="abs" style="{box(CX_ + 34, y, 46, 46)}border-radius:12px;background:#fbfcfe;box-shadow:inset 0 0 0 2.5px #acc6e7,inset 1px 2px 3px rgba(28,51,84,.15)"></div>')
        m.append(f'<div class="abs" id="{s}-rk{k}" style="{box(CX_ + 30, y - 4, 54, 54)}">{check_svg(f"{s}-rc{k}", 54)}</div>')
        m.append(f'<div class="abs" id="{s}-rb{k}" style="{box(CX_ + 98, y + 16, 150 - 26 * (k % 2), 14)}border-radius:7px;background:#dbe6f6"></div>')
        m.append(f'<div class="abs" id="{s}-rl{k}" style="left:{CX_ + 96}px;top:{y + 2}px;font:700 34px Montserrat;color:#202b3b;letter-spacing:-.01em;white-space:nowrap">{lab}</div>')
        S.init(f"#{s}-rk{k}", {"scale": 0, "opacity": 0})
        S.ft(f"#{s}-rk{k}", {"scale": 0, "opacity": 0}, {"scale": 1, "opacity": 1}, at - 0.02, 0.32, "back.out(2.6)")
        S.ft(f"#{s}-rc{k}-p", {"strokeDashoffset": 60}, {"strokeDashoffset": 0}, at + 0.04, 0.26, "power2.out")
        S.init(f"#{s}-rl{k}", {"opacity": 0, "x": -14})
        S.ft(f"#{s}-rl{k}", {"opacity": 0, "x": -14}, {"opacity": 1, "x": 0}, at - 0.05, 0.22, "power3.out")
        S.init(f"#{s}-rb{k}", {"opacity": 1})
        S.ft(f"#{s}-rb{k}", {"opacity": 1}, {"opacity": 0}, at - 0.05, 0.12, "power1.in")

    # ---------------- waveform strip + word markers
    m.append(shadow(WX - 10, WY + WH - 24, WW + 30, 56, 0.75))
    m.append(f'<div class="abs por" style="{box(WX, WY, WW, WH)}border-radius:24px">{screw(18, 18, 20, 10)}{screw(WW - 18, 18, -50, 10)}'
             f'<div class="abs" style="{box(18, 62, WW - 36, 2)}background:rgba(41,75,119,.18)"></div></div>')
    pitch, nb = 12, 44
    cl = [6, 16, 27, 37]                         # syllable clusters = where the words start
    bars = []
    for k in range(nb):
        base = 10 + 26 * abs(math.sin(k * 0.73) * math.cos(k * 0.29))
        for c in cl:
            base += 46 * math.exp(-((k - c - 1.2) ** 2) / 3.0)
        hgt = min(78, base)
        bars.append(f'<div class="abs" style="left:{r3(WX + 22 + k * pitch)}px;top:{r3(WY + 118 - hgt / 2)}px;width:6px;height:{r3(hgt)}px;border-radius:3px;background:{"#294b77" if k % 3 else "#3a6299"}"></div>')
    m.append(f'<div class="abs" id="{s}-wv">{"".join(bars)}</div>')
    # marker rail + markers (start offset to the right, slide onto the cluster onsets on "sinkron")
    m.append(f'<div class="abs" style="{box(WX + 18, WY + 26, WW - 36, 8)}border-radius:4px;background:#e3ebf7;box-shadow:inset 0 1px 2px rgba(28,51,84,.2)"></div>')
    mk = []
    for j, c in enumerate(cl):
        x = 22 + c * pitch - 6
        mk.append(f'<div class="abs" style="left:{x}px;top:12px;width:18px;height:22px">'
                  f'<div class="abs" style="{box(0, 0, 18, 18)}border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:linear-gradient(150deg,#3a6299,#1c3354);box-shadow:0 3px 5px rgba(28,51,84,.35)"></div></div>'
                  f'<div class="abs" id="{s}-gl{j}" style="left:{x + 8}px;top:36px;width:2px;height:116px;background:#294b77;opacity:.35"></div>')
    m.append(f'<div class="abs" id="{s}-mk" style="{box(WX, WY, WW, WH)}">{"".join(mk)}</div>')
    S.init(f"#{s}-mk", {"x": 46})
    S.ft(f"#{s}-mk", {"x": 46}, {"x": 52}, S.t0, WS - 0.32 - S.t0, "sine.inOut")
    S.ft(f"#{s}-mk", {"x": 52}, {"x": 0}, WS - 0.3, 0.38, "back.out(1.6)")
    for j in range(len(cl)):
        S.init(f"#{s}-gl{j}", {"backgroundColor": "#294b77", "opacity": 0.35})
        S.ft(f"#{s}-gl{j}", {"backgroundColor": "#294b77", "opacity": 0.35}, {"backgroundColor": "#9fd8c4", "opacity": 1}, WS + 0.06 + j * 0.05, 0.2, "power2.out")
    apex(S, S.near, f"{s}-ap", WX + 22 + 21 * pitch, WY + 100, WS + 0.08, size=440, sparks=6, seed=16, op=0.7)

    # ---------------- magnifier (travels: card -> seam -> waveform -> centre -> iris)
    LX0, LY0 = 760, 600
    m.append(magnifier(f"{s}", LX0, LY0))
    card_c = (SX + SW / 2, SY + 262 + 80)
    seam_c = (SX + 172, SY + 124)
    wave_c = (WX + 22 + 21 * pitch, WY + 96)
    path = [(S.t0, (0, 0), None),
            (WD, (-40, 30), "sine.inOut"),
            (WV - 0.08, (card_c[0] - LX0 + 30, card_c[1] - LY0 - 10), "power3.inOut"),
            (WT - 0.1, (seam_c[0] - LX0 + 26, seam_c[1] - LY0 + 6), "power3.inOut"),
            (WT + 0.4, (seam_c[0] - LX0 + 34, seam_c[1] - LY0 + 2), "sine.out"),
            (WS - 0.1, (wave_c[0] - LX0 + 10, wave_c[1] - LY0 - 6), "power3.inOut"),
            (WSU - 0.15, (wave_c[0] - LX0 + 20, wave_c[1] - LY0 - 12), "sine.inOut"),
            (S.t1 - 0.42, (590 - LX0, 930 - LY0), "power3.inOut")]
    S.keys(f"#{s}-mag", [(t, {"x": xy[0], "y": xy[1], "rotation": 0}, e) for t, xy, e in path])

    # ---------------- reel content actions
    S.init(f"#{s}-card", {"rotation": -8, "x": -34, "y": 18, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-card", {"rotation": -8, "x": -34, "y": 18}, {"rotation": -6.5, "x": -30, "y": 14}, S.t0, WV - 0.12 - S.t0, "sine.inOut")
    S.ft(f"#{s}-card", {"rotation": -6.5, "x": -30, "y": 14}, {"rotation": 0, "x": 0, "y": 0}, WV - 0.1, 0.36, "back.out(2.4)")
    S.init(f"#{s}-gd", {"opacity": 0})
    S.ft(f"#{s}-gd", {"opacity": 0}, {"opacity": 1}, WV - 0.35, 0.2, "power2.out")
    S.ft(f"#{s}-gd", {"opacity": 1}, {"opacity": 0}, WV + 0.3, 0.3, "power2.in")
    S.init(f"#{s}-tr", {"y": 26, "x": 9})
    S.ft(f"#{s}-tr", {"y": 26, "x": 9}, {"y": 0, "x": 0}, WT - 0.08, 0.34, "back.out(2)")
    S.init(f"#{s}-seam", {"opacity": 0.25, "y": 13})
    S.ft(f"#{s}-seam", {"opacity": 0.25, "y": 13}, {"opacity": 1, "y": 0}, WT - 0.08, 0.2, "power2.out")
    S.ft(f"#{s}-seam", {"opacity": 1}, {"opacity": 0}, WT + 0.2, 0.45, "power2.in")
    S.init(f"#{s}-ph", {"scaleX": 0.05, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-ph", {"scaleX": 0.05}, {"scaleX": 1}, S.t0, WSU - S.t0, "none")
    S.init(f"#{s}-ok", {"scale": 0, "opacity": 0})
    S.ft(f"#{s}-ok", {"scale": 0, "opacity": 0}, {"scale": 1, "opacity": 1}, WSU - 0.04, 0.34, "back.out(2.8)")
    S.ft(f"#{s}-ck-p", {"strokeDashoffset": 60}, {"strokeDashoffset": 0}, WSU + 0.04, 0.3, "power2.out")

    # ---------------- iris: ivory closes around the centred lens (hand-off to S17)
    S.near.append(iris(f"{s}-iris", 590, 930, 214))
    S.init(f"#{s}-iris", {"opacity": 0})
    S.ft(f"#{s}-iris", {"opacity": 0}, {"opacity": 1}, S.t1 - 0.3, 0.26, "power2.in")

    # ---------------- near plane: out-of-focus ruler + glass corner
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(900, 1300, 260, 30)}border-radius:8px;background:repeating-linear-gradient(90deg,#ffffff 0 10px,#dbe6f6 10px 12px);filter:blur(4px);opacity:.85"></div>'
                  f'<div class="abs" style="{box(-60, 420, 150, 150)}border-radius:30px;border:10px solid rgba(255,255,255,.7);filter:blur(5px)"></div></div>')

    # ---------------- camera follows the inspection, returns to neutral for the iris
    S.cam([(S.t0, {"z": 40, "x": 0, "y": 0, "rotationY": -2, "rotationX": 0}, None),
           (WV, {"z": 90, "x": 10, "y": 10, "rotationY": 1}, "sine.inOut"),
           (WS + 0.2, {"z": 100, "x": -30, "y": -50, "rotationY": 2.5, "rotationX": 1.5}, "sine.inOut"),
           (S.t1 - 0.35, {"z": 0, "x": 0, "y": 0, "rotationY": 0, "rotationX": 0}, "power2.inOut")])
