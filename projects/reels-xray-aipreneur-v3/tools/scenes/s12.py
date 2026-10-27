"""S12 — REASSEMBLE THE REEL (28.54–32.48)  VO: "lalu render versi baru. Gerakan utamanya tetap bisa dipakai."
THE PAYOFF. On a porcelain turntable stands the bare motion skeleton of a reel: a dashed glass outline and the
S-shaped animation rail with its keyframe pins. The parts edited in S11 (new product cartridge, new text strips,
re-timed keyframes) fly in from the camera, rotate into alignment and dock onto that SAME rail; on "render" two
clamp arms close, on "baru" the reel locks (porcelain frame + glass fill, shockwave, light burst).
Then the old version slides out from behind it: before/after side by side, both cards riding the identical
motion path in sync. On "dipakai" the shared rail under both lights up end to end. Finally the twin reels slide
down toward the master template plate rising from below (hand-off to S13)."""
from xk import box, screw, shadow, apex, pedestal, rivets_line, r3
from kit_c import product_a, product_b, BARS_A, BARS_B, bars

SFX = []

RW, RH = 300, 540                  # reel size
SX, SY, SW, SH = 16, 34, 268, 472  # screen inside the reel
RX, RY = 440, 560                  # reel position (centre x 590)
PATH = "M30,300 C80,300 70,222 122,230 S196,262 238,190"
PINS = [(30, 300), (122, 230), (238, 190)]
CARD_PTS = [(30, 300), (62, 288), (90, 248), (122, 230), (160, 240), (200, 236), (238, 190)]


def rail_svg(id_, glow=False):
    g = (f'<path d="{PATH}" fill="none" stroke="#ffffff" stroke-width="16" stroke-linecap="round" opacity=".95"/>'
         f'<path d="{PATH}" fill="none" stroke="#9fd8c4" stroke-width="7" stroke-linecap="round"/>') if glow else (
        f'<path d="{PATH}" fill="none" stroke="#cbdbf4" stroke-width="12" stroke-linecap="round"/>'
        f'<path d="{PATH}" fill="none" stroke="#294b77" stroke-width="3.5" stroke-dasharray="7 8" stroke-linecap="round"/>')
    return f'<svg class="abs" id="{id_}" style="left:0;top:0" width="{SW}" height="{SH}" viewBox="0 0 {SW} {SH}">{g}</svg>'


def pin(x, y, id_=None):
    i = f' id="{id_}"' if id_ else ""
    return (f'<div class="abs"{i} style="{box(x - 13, y - 13, 26, 26)}">'
            f'<div class="abs" style="{box(4, 4, 18, 18)}border-radius:4px;background:#294b77;box-shadow:0 3px 6px rgba(28,51,84,.35),inset 1px 1px 0 rgba(255,255,255,.35);transform:rotate(45deg)"></div></div>')


def reel(pre, kind):
    """a full reel group. kind 'A' = old version (complete), 'B' = new version (docks in during the scene)."""
    prod = product_a(f"{pre}-pr", 0, 0, 0.92) if kind == "A" else product_b(f"{pre}-pr", 0, 0, 0.92)
    pat = BARS_A if kind == "A" else BARS_B
    z = lambda v: f"transform:translateZ({v}px)"
    out = []
    # body thickness (navy sidewall) + porcelain frame
    out.append(f'<div class="abs" style="{box(0, 0, RW, RH)}border-radius:42px;background:#1c3354;{z(-14)}"></div>')
    out.append(f'<div class="abs" style="{box(0, 0, RW, RH)}border-radius:42px;background:#294b77;{z(-7)}"></div>')
    out.append(f'<div class="abs por" id="{pre}-frame" style="{box(0, 0, RW, RH)}border-radius:42px">'
               f'<div class="abs" style="{box(RW / 2 - 34, 13, 68, 7)}border-radius:4px;background:#cbdbf4;box-shadow:inset 0 1px 2px rgba(28,51,84,.3)"></div>'
               f'<div class="abs" style="{box(RW / 2 + 44, 11, 11, 11)}border-radius:50%;background:#294b77"></div>'
               f'<div class="abs" style="{box(RW / 2 - 44, RH - 20, 88, 6)}border-radius:3px;background:#dbe6f6"></div>'
               f'{screw(22, 22, 30, 8)}{screw(RW - 22, RH - 22, -30, 8)}</div>')
    out.append(f'<div class="abs" id="{pre}-glass" style="{box(SX, SY, SW, SH)}border-radius:14px;background:linear-gradient(170deg,#fbfcfe 0%,#eef3fa 60%,#e2eaf6 100%);'
               f'box-shadow:inset 0 0 0 2px rgba(41,75,119,.45);{z(1)}"></div>')
    # skeleton: dashed outline + rail + pins (identical in both versions)
    out.append(f'<div class="abs" id="{pre}-dash" style="{box(-6, -6, RW + 12, RH + 12)}border-radius:46px;border:3px dashed rgba(41,75,119,.55);{z(2)}"></div>')
    out.append(f'<div class="abs p3" style="{box(SX, SY, SW, SH)}{z(3)}">{rail_svg(pre + "-rail")}'
               f'<div class="abs" id="{pre}-rglow" style="{box(0, 0, SW, SH)}">{rail_svg(pre + "-rg", True)}</div>'
               + "".join(pin(x, y, f"{pre}-pin{k}") for k, (x, y) in enumerate(PINS))
               + f'<div class="abs mr-navy" id="{pre}-card" style="{box(CARD_PTS[0][0] - 20, CARD_PTS[0][1] - 17, 40, 34)}border-radius:9px"></div></div>')
    # content: product + text bars
    out.append(f'<div class="abs p3" style="{box(SX, SY, SW, SH)}{z(5)}">'
               f'<div class="abs" id="{pre}-pw" style="{box(80, 22, 110, 156)}">{prod}</div>'
               f'<div class="abs" id="{pre}-bw" style="{box(26, 360, 220, 80)}">{bars(pre + "-b", 0, 0, pat, 0.92, 24, 13)}</div></div>')
    # mint confirmation tick (on "dipakai")
    out.append(f'<div class="abs" id="{pre}-ok" style="{box(RW - 64, -22, 56, 56)}border-radius:50%;background:linear-gradient(150deg,#c9efe1,#9fd8c4);'
               f'box-shadow:0 6px 12px -4px rgba(28,51,84,.35),inset 0 0 0 3px #fff;{z(8)}">'
               f'<div class="abs" style="{box(16, 26, 12, 4)}border-radius:2px;background:#1c3354;transform:rotate(45deg)"></div>'
               f'<div class="abs" style="{box(22, 22, 22, 4)}border-radius:2px;background:#1c3354;transform:rotate(-50deg)"></div></div>')
    return "".join(out)


def build(S):
    s = S.id
    S.persp_origin = (590, 600)
    T0, T1 = S.t0, S.t1
    W60, W61, W63, W64, W66, W68 = (S.W(i) for i in (60, 61, 63, 64, 66, 68))   # lalu render baru Gerakan tetap dipakai
    LOCK = W63
    SPLIT = W64 - 0.42
    # ---------------- far plane: soft studio cyclorama + two light stands
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs" style="{box(140, 330, 900, 1100)}border-radius:450px 450px 60px 60px;background:radial-gradient(ellipse at 50% 40%,rgba(255,255,255,.95),rgba(232,240,251,.4) 60%,rgba(203,219,244,.25));opacity:.9"></div>'
                 + "".join(f'<div class="abs" style="{box(x, 420, 6, 900)}background:rgba(172,198,231,.6);border-radius:3px"></div><div class="abs por-dim" style="{box(x - 40, 400, 86, 50)}border-radius:20px;opacity:.8"></div>' for x in (190, 980))
                 + '</div>')
    # ---------------- hero: turntable + shared rail + reels + clamps
    S.mid.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-60px) scale(1.03)">{pedestal(s + "-ped", 590, 1112, 860, depth=96)}</div>')
    # shared rail under both reels (glows end to end on "dipakai")
    S.mid.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-90px) scale(1.045)"><div class="abs por" style="{box(170, 1100, 840, 30)}border-radius:15px">'
                 f'<div class="abs" style="{box(16, 11, 808, 8)}border-radius:4px;background:#294b77"></div>'
                 + "".join(f'<div class="abs" style="{box(40 + k * 70, 8, 4, 14)}border-radius:2px;background:#acc6e7"></div>' for k in range(12))
                 + f'<div class="abs" id="{s}-srglow" style="{box(16, 9, 808, 12)}border-radius:6px;background:linear-gradient(90deg,#ffffff,#9fd8c4 40%,#ffffff);box-shadow:0 0 16px rgba(159,216,196,.95)"></div>'
                 f'<div class="abs" id="{s}-srpulse" style="{box(0, -14, 70, 58)}border-radius:50%;background:radial-gradient(ellipse,rgba(255,255,255,1),rgba(159,216,196,.6) 45%,rgba(159,216,196,0) 70%)"></div></div></div>')
    S.mid.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-120px) scale(1.06)">{shadow(250, 1050, 680, 80, 0.9, id_=f"{s}-rsh")}</div>')
    # the old version (behind, slides out left) and the new version (docks in, slides right)
    S.mid.append(f'<div class="abs p3" id="{s}-L" style="{box(RX, RY, RW, RH)}">{reel(s + "-L", "A")}</div>')
    S.mid.append(f'<div class="abs p3" id="{s}-R" style="{box(RX, RY, RW, RH)}">{reel(s + "-R", "B")}</div>')
    # clamp arms (close on "render", open after the lock)
    for side, x0 in (("l", RX - 250), ("r", RX + RW + 20)):
        tip = "left:212px" if side == "l" else "left:-8px"
        S.mid.append(f'<div class="abs p3" id="{s}-arm{side}" style="{box(x0, RY + 230, 230, 74)}">'
                     f'<div class="abs por" style="{box(0, 0, 230, 74)}border-radius:37px">'
                     + rivets_line(40, 37, 190, 37, 5) +
                     f'<div class="abs navy-side" style="{tip};top:10px;width:26px;height:54px;border-radius:12px"></div></div></div>')
    # master template plate (rises at the end; S13 opens on it)
    S.mid.append(f'<div class="abs p3" id="{s}-tpl" style="{box(150, 1230, 880, 240)}">'
                 f'<div class="abs navy-side" style="{box(0, 24, 880, 230)}border-radius:40px;transform:translateZ(-20px)"></div>'
                 f'<div class="abs por" style="{box(0, 0, 880, 230)}border-radius:40px">'
                 f'<div class="abs grid-paper" style="{box(40, 34, 800, 160)}border-radius:20px;box-shadow:inset 0 0 0 2px rgba(172,198,231,.8)"></div>'
                 + "".join(f'<div class="abs" style="{box(120 + k * 380, 50, 260, 40)}border-radius:20px;background:linear-gradient(180deg,#1c3354,#294b77);box-shadow:inset 0 4px 8px rgba(0,0,0,.35)"></div>' for k in range(2))
                 + f'{screw(26, 26, 20)}{screw(854, 26, -30)}{screw(26, 204, 50)}{screw(854, 204, 0)}</div></div>')
    # ---------------- near plane: out-of-focus lens ring + glass shard
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(980, 520, 190, 190)}border-radius:50%;border:14px solid rgba(255,255,255,.75);box-shadow:0 0 0 2px rgba(172,198,231,.5);filter:blur(5px)"></div>'
                  f'<div class="abs glass" style="{box(-90, 760, 160, 260)}border-radius:30px;filter:blur(4px)"></div></div>')
    apex(S, S.near, f"{s}-ap", 590, 820, LOCK + 0.03, size=820, sparks=10, seed=33)
    for k in range(2):
        S.near.append(f'<div class="abs" id="{s}-sw{k}" style="{box(590 - 200, 830 - 200, 400, 400)}border-radius:50%;border:{6 - 2 * k}px solid rgba(58,98,153,.7);box-shadow:0 0 0 6px rgba(203,219,244,.6),inset 0 0 0 4px rgba(255,255,255,.8)"></div>')
        S.init(f"#{s}-sw{k}", {"opacity": 0, "scale": 0.4})
        S.ft(f"#{s}-sw{k}", {"opacity": 0.95, "scale": 0.4}, {"opacity": 0, "scale": 2.1 + 0.5 * k}, LOCK + 0.02 + 0.08 * k, 0.6 + 0.1 * k, "power3.out")

    # ================= motion
    S.cam([(T0, {"z": 110, "x": 0, "y": 30, "rotationX": 3, "rotationY": -4}, None),
           (LOCK - 0.08, {"z": 20, "y": 0, "rotationY": 2}, "power2.inOut"),
           (LOCK + 0.06, {"z": 60}, "power3.out"),
           (SPLIT, {"z": 10, "rotationY": 0}, "power2.inOut"),
           (SPLIT + 0.7, {"z": -70, "y": -10, "rotationX": 2}, "power3.inOut"),
           (W68 + 0.3, {"z": -40, "rotationY": -2}, "sine.inOut"),
           (T1, {"z": -150, "y": 40, "rotationX": 6}, "power2.in")])
    # new reel: orbit into alignment; frame + glass materialise on the lock
    S.keys(f"#{s}-R", [(T0, {"x": 0, "z": 0, "rotationY": -24, "rotationX": 6, "scale": 1}, None),
                       (LOCK - 0.05, {"rotationY": -2, "rotationX": 1}, "power2.inOut"),
                       (LOCK + 0.08, {"scale": 1.035, "rotationY": 0, "rotationX": 0}, "power4.out"),
                       (LOCK + 0.36, {"scale": 1}, "power2.inOut"),
                       (SPLIT + 0.64, {"x": 190, "rotationY": -12, "z": 10}, "power3.inOut"),
                       (W68 + 0.4, {"rotationY": -8}, "sine.inOut"),
                       (T1, {"x": 210, "y": 300, "z": -40, "scale": 0.74, "rotationY": 0, "rotationX": 18}, "power3.in")])
    S.keys(f"#{s}-L", [(T0, {"x": 0, "z": -60, "scale": 0.001, "rotationY": 0}, None),
                       (SPLIT - 0.02, {"scale": 0.001}, "none"),
                       (SPLIT, {"scale": 1}, "none"),
                       (SPLIT + 0.66, {"x": -190, "z": 10, "rotationY": 12}, "power3.inOut"),
                       (W68 + 0.4, {"rotationY": 8}, "sine.inOut"),
                       (T1, {"x": -190, "y": 300, "z": -40, "scale": 0.74, "rotationY": 0, "rotationX": 18}, "power3.in")])
    for nm in ("frame", "glass"):
        S.init(f"#{s}-R-{nm}", {"opacity": 0})
        S.ft(f"#{s}-R-{nm}", {"opacity": 0}, {"opacity": 1}, LOCK - 0.1, 0.14, "power2.in")
    S.init(f"#{s}-R-dash", {"opacity": 1, "scale": 1})
    S.ft(f"#{s}-R-dash", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 1.06}, LOCK - 0.04, 0.3, "power2.out")
    S.init(f"#{s}-L-dash", {"opacity": 0})
    # the edited parts fly in from the camera and dock onto the skeleton (staggered, different arcs)
    S.keys(f"#{s}-R-pw", [(T0, {"x": 250, "y": 30, "z": 230, "rotation": 14, "rotationY": -40, "scale": 1.5}, None),
                          (W61 - 0.05, {"x": 110, "y": 10, "z": 110, "rotation": 6, "rotationY": -20, "scale": 1.15}, "sine.inOut"),
                          (LOCK - 0.12, {"x": 0, "y": 0, "z": 0, "rotation": 0, "rotationY": 0, "scale": 1}, "power3.inOut")])
    S.keys(f"#{s}-R-bw", [(T0, {"x": 300, "y": -150, "z": 220, "rotation": -10, "rotationX": 50, "scale": 1.5}, None),
                          (W61 + 0.05, {"x": 130, "y": -60, "z": 100, "rotation": -4, "rotationX": 20, "scale": 1.15}, "sine.inOut"),
                          (LOCK - 0.06, {"x": 0, "y": 0, "z": 0, "rotation": 0, "rotationX": 0, "scale": 1}, "power3.inOut")])
    for k, (dx, dy) in enumerate(((-250, -40), (-300, -110), (-210, -190))):
        S.keys(f"#{s}-R-pin{k}", [(T0, {"x": dx, "y": dy, "z": 200, "rotation": 90, "scale": 1.4}, None),
                                  (W61 + 0.1 + k * 0.08, {"x": dx * 0.3, "y": dy * 0.3, "z": 60, "rotation": 30}, "sine.inOut"),
                                  (LOCK - 0.16 + k * 0.05, {"x": 0, "y": 0, "z": 0, "rotation": 0, "scale": 1}, "back.out(2.4)")])
    # clamp arms
    S.keys(f"#{s}-arml", [(T0, {"x": -260, "rotationY": 30}, None), (W61 - 0.1, {"x": -260}, "none"),
                          (LOCK - 0.04, {"x": 0, "rotationY": 0}, "power3.inOut"), (LOCK + 0.3, {"x": 0}, "none"), (SPLIT + 0.1, {"x": -330, "rotationY": 25}, "power3.in")])
    S.keys(f"#{s}-armr", [(T0, {"x": 260, "rotationY": -30}, None), (W61 - 0.06, {"x": 260}, "none"),
                          (LOCK - 0.04, {"x": 0, "rotationY": 0}, "power3.inOut"), (LOCK + 0.3, {"x": 0}, "none"), (SPLIT + 0.1, {"x": 330, "rotationY": -25}, "power3.in")])
    # identical motion in both versions: the card rides the same path, in sync
    t = SPLIT + 0.55
    seg = 0.26
    for rep in range(3):
        for k in range(len(CARD_PTS) - 1):
            (x0, y0), (x1, y1) = CARD_PTS[k], CARD_PTS[k + 1]
            for side in ("L", "R"):
                S.ft(f"#{s}-{side}-card", {"x": x0 - CARD_PTS[0][0], "y": y0 - CARD_PTS[0][1]}, {"x": x1 - CARD_PTS[0][0], "y": y1 - CARD_PTS[0][1]},
                     t, seg, "sine.inOut" if k not in (0, len(CARD_PTS) - 2) else ("power2.in" if k == 0 else "power2.out"))
            t += seg
        if t > T1 - 0.3:
            break
        for side in ("L", "R"):   # snap back to the start (deliberate reset, both together)
            S.ft(f"#{s}-{side}-card", {"x": CARD_PTS[-1][0] - CARD_PTS[0][0], "y": CARD_PTS[-1][1] - CARD_PTS[0][1], "scale": 1},
                 {"x": 0, "y": 0, "scale": 1}, t + 0.05, 0.16, "power3.inOut")
        t += 0.24
    for side in ("L", "R"):
        S.init(f"#{s}-{side}-card", {"x": 0, "y": 0})
        S.init(f"#{s}-{side}-rglow", {"opacity": 0})
        S.ft(f"#{s}-{side}-rglow", {"opacity": 0}, {"opacity": 1}, W68 - 0.05 + (0.18 if side == "R" else 0), 0.2, "power2.out")
        S.ft(f"#{s}-{side}-rglow", {"opacity": 1}, {"opacity": 0.35}, W68 + 0.5, T1 - W68 - 0.5, "power1.inOut")
        S.init(f"#{s}-{side}-ok", {"opacity": 0, "scale": 0.3, "rotation": -30})
        S.ft(f"#{s}-{side}-ok", {"opacity": 0, "scale": 0.3, "rotation": -30}, {"opacity": 1, "scale": 1, "rotation": 0}, W68 + (0.22 if side == "R" else 0.04), 0.3, "back.out(2.6)")
    # shared rail lights end to end on "dipakai"
    S.init(f"#{s}-srglow", {"opacity": 0, "scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-srglow", {"opacity": 0, "scaleX": 0}, {"opacity": 1, "scaleX": 1}, W68 - 0.08, 0.42, "power2.inOut")
    S.init(f"#{s}-srpulse", {"opacity": 0, "x": 0})
    S.ft(f"#{s}-srpulse", {"opacity": 0, "x": 0}, {"opacity": 1, "x": 120}, W68 - 0.1, 0.1, "power1.in")
    S.ft(f"#{s}-srpulse", {"opacity": 1, "x": 120}, {"opacity": 0, "x": 780}, W68, 0.42, "power2.inOut")
    # reel contact shadow follows the twin split
    S.init(f"#{s}-rsh", {"scaleX": 0.55, "opacity": 0.9})
    S.ft(f"#{s}-rsh", {"scaleX": 0.55}, {"scaleX": 1.15}, SPLIT, 0.66, "power3.inOut")
    # master template plate rises at the end
    S.init(f"#{s}-tpl", {"y": 780, "rotationX": 30})
    S.ft(f"#{s}-tpl", {"y": 780, "rotationX": 30}, {"y": 0, "rotationX": 14}, T1 - 0.62, 0.62, "power3.out")
    SFX.extend([(W61 + 0.02, "whoosh", 0.06), (LOCK + 0.01, "click", 0.15), (W68 + 0.02, "sparkle", 0.07)])
