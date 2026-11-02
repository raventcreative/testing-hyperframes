"""CLAUDE CODE MOTION REEL 01 — 'the screenshot comes alive'. Genuine assets only (assets/ui, masked/cleaned copies
from tools/prep_ui.py). 2.5D language: real screenshots become physical slabs (front face + dark back slab for visible
thickness, glossy rim, contact shadow), arranged on CSS-3D depth planes and moved by one camera. The pixel cursor is the
editing tool that causes every cut. All times are measured VO word starts (S.W)."""
from xk import box, r3, apex
from kit_cc import pop, MASCOT_C, MASCOT_R, OFF

SHOT = "assets/ui/01_session_crop_safe.png"             # 930 x 629: centre of the real session screenshot (masked copy), ~native scale
FULL = "assets/ui/01_claude_code_session_safe.png"      # 1648 x 929 whole real screen (private strings masked)
SIDE = "assets/ui/03_claude_code_sidebar.png"            # 244 x 233
LOGO = "assets/ui/02_claude_logo_3d_clean.png"          # 1254 x 1254 (edge-decontaminated copy)
CUR = "assets/ui/09_cursor_trim.png"                     # 1028 x 1014 pixel art -> nearest-neighbour
SW, SH = 930, 629
ORANGE = "#D97757"


def slab(sid, src, x, y, w, h, radius=22, thick=16, extra=""):
    """genuine image as a physical plate: back slab (thickness) + face + rim/sheen. Transforms go on the outer id."""
    return (f'<div id="{sid}" class="abs p3" style="{box(x, y, w, h)}">'
            f'<div class="abs" style="left:0;top:0;width:{r3(w)}px;height:{r3(h)}px;border-radius:{radius}px;transform:translateZ(-{thick}px);'
            f'background:linear-gradient(160deg,#20283d,#06080f);box-shadow:0 60px 90px -36px rgba(0,0,0,.75)"></div>'
            f'<div id="{sid}-face" class="abs" style="left:0;top:0;width:{r3(w)}px;height:{r3(h)}px;border-radius:{radius}px;overflow:hidden;'
            f'box-shadow:0 0 0 1.5px rgba(255,255,255,.14), inset 0 1px 0 rgba(255,255,255,.25)">'
            f'<img src="{src}" style="position:absolute;left:0;top:0;width:{r3(w)}px;height:{r3(h)}px">{extra}'
            f'<div id="{sid}-sh" class="abs sheen" style="left:-40%;top:-10%;width:30%;height:120%;opacity:.0;transform:skewX(-16deg)"></div>'
            f'</div></div>')


def logo3d(lid, x, y, w):
    """the genuine 3D Claude badge with a soft grounded shadow"""
    return (f'<div id="{lid}" class="abs p3" style="{box(x, y, w, w)}">'
            f'<div id="{lid}-cs" class="abs cshadow" style="{box(w * 0.08, w * 0.86, w * 0.84, w * 0.22)}"></div>'
            f'<img id="{lid}-im" src="{LOGO}" style="position:absolute;left:0;top:0;width:{r3(w)}px;height:{r3(w)}px;'
            f'filter:drop-shadow(0 24px 30px rgba(0,0,0,.45))"></div>')


def cursor(cid, x, y, w=150):
    """genuine pixel cursor; hotspot = fingertip at (x, y); nearest-neighbour scaling keeps it crisp"""
    h = w * 1014 / 1028
    return (f'<img id="{cid}" class="abs" src="{CUR}" style="left:{r3(x - w * 0.02)}px;top:{r3(y - h * 0.01)}px;width:{r3(w)}px;height:{r3(h)}px;'
            f'image-rendering:pixelated;transform-origin:2% 1%;filter:drop-shadow(10px 16px 14px rgba(0,0,0,.45))">')


def label(lid, x, y, text, cyan=False):
    col = "#00D0FE" if cyan else "#fff"
    return (f'<div id="{lid}" class="abs plate plate-s" style="left:{r3(x)}px;top:{r3(y)}px;padding:10px 22px;'
            f'font:700 28px/1 Poppins;letter-spacing:.12em;color:{col};white-space:nowrap">{text}</div>')


HALF = {"fx": 540, "fy": 2210, "h": 1190, "yaw": 0, "pitch": 4}      # educator framing: half-body, head top ~y 1020 (panel above stays clear)
NARR = {"fx": 900, "fy": 1900, "h": 640, "yaw": 0, "pitch": 4}       # small narrator bottom-right


def narrator(S, view, rise=True):
    if rise:
        S.mv([(S.t0, dict(view, fy=view["fy"] + 1000, vis=1), None), (S.t0 + 0.1, dict(view, fy=view["fy"] + 1000), None),
              (S.t0 + 0.7, dict(view), "power3.out")])
    else:
        S.mv([(S.t0, dict(view, vis=1), None)])


def edu_bg(S, layer, src=None, dim=0.5):
    """educator mode: the real interface fills the frame, blurred and dimmed, so the mascot reads in front of it"""
    src = src or FULL
    layer.append(f'<div id="{S.id}-bg" class="abs" style="left:-120px;top:-60px;width:1320px;height:2040px;overflow:hidden">'
                 f'<img src="{src}" style="position:absolute;left:-560px;top:300px;width:2440px;height:1376px;filter:blur(16px) brightness({dim})">'
                 f'<div class="abs" style="inset:0;background:radial-gradient(ellipse 70% 55% at 50% 60%,rgba(41,75,119,.25),rgba(5,8,22,.55))"></div></div>')
    S.ft(f"#{S.id}-bg", {"scale": 1.0}, {"scale": 1.05}, S.t0, S.t1 - S.t0, "sine.inOut")


def panel(pid, x, y, w, h, inner, title=None):
    """sharp floating glass panel (the visual the mascot is explaining), edge-lit"""
    t = f'<div class="abs" style="left:24px;top:16px;font:700 24px/1 Poppins;letter-spacing:.12em;color:#00D0FE">{title}</div>' if title else ""
    return (f'<div id="{pid}" class="abs p3" style="{box(x, y, w, h)}">'
            f'<div class="abs plate" style="left:0;top:0;width:{r3(w)}px;height:{r3(h)}px;border-radius:28px;border:2px solid rgba(0,208,254,.7);'
            f'box-shadow:0 0 0 1px rgba(255,255,255,.2) inset, 0 0 26px rgba(0,208,254,.25), 0 40px 70px -30px rgba(0,0,0,.8);overflow:hidden">{t}{inner}</div></div>')


def hide(S):
    S.mv([(S.t0, dict(OFF), None)])


# shared geometry: the hero screenshot slab, full width
HX, HY, HW = 60, 640, 960
HH = HW * SH / SW                      # 531.4
# the tapped element in S02 ('Default' row of the env card) in slab coords
TAP = (HX + HW * 520 / SW, HY + HH * 105 / SH)


# ============================================================================== S01 THE PAYOFF FIRST / THUMB-STOP
def s01(S):
    s, W = S.id, S.W
    # depth stack already in motion on frame 0: back = real screenshot, mid = real sidebar, front = 3D badge, cursor nearest
    S.back.append(slab(f"{s}-bk", SHOT, HX, HY, HW, HH))
    S.back.append(slab(f"{s}-sd", SIDE, 110, 560, 330, 330 * 233 / 244, 18, 12))
    S.back.append(logo3d(f"{s}-lg", 590, 560, 340))
    S.front.append(cursor(f"{s}-cur", 760, 1180, 170))
    stack = {"bk": {"z": -260, "rotationY": -24, "rotationX": 12, "x": 0, "y": 0},
             "sd": {"z": 120, "rotationY": -24, "rotationX": 12, "x": -40, "y": 40},
             "lg": {"z": 300, "rotationY": -16, "rotationX": 8, "x": 0, "y": 0}}
    flat = {"bk": {"z": 0, "rotationY": 0, "rotationX": 0, "x": 0, "y": 0},
            "sd": {"z": 60, "rotationY": 0, "rotationX": 0, "x": 0, "y": 200},
            "lg": {"z": 90, "rotationY": -6, "rotationX": 0, "x": 40, "y": -120}}
    # 0-0.3 s impossible stack, 0.3-1.3 camera dolly-pull reveals the real screenshot
    S.cam([(S.t0, {"z": 210, "rotationY": 8, "y": 30}, None), (S.t0 + 0.3, {"z": 180, "rotationY": 7, "y": 24}, "none"),
           (1.3, {"z": 0, "rotationY": 0, "y": 0}, "power3.inOut"), (S.t1, {"z": -40}, "sine.inOut")])
    for k in ("bk", "sd", "lg"):
        S.keys(f"#{s}-{k}", [(S.t0, stack[k], None), (1.3, flat[k], "power3.inOut")])
    # 1.3-2.4 the cursor sweeps the composition: the planes it touches separate into depth
    S.keys(f"#{s}-cur", [(S.t0, {"x": 0, "y": 0, "rotation": 0}, None), (1.3, {"x": -480, "y": -420, "rotation": -8}, "power2.inOut"),
                         (2.3, {"x": 140, "y": -320, "rotation": 4}, "power3.inOut"), (S.t1 - 0.25, {"x": TAP[0] - 760, "y": TAP[1] - 1180, "rotation": 0}, "power3.inOut")])
    sep = {"bk": {"z": -120, "rotationY": -14, "rotationX": 6}, "sd": {"z": 140, "rotationY": -14, "rotationX": 6, "y": 200}, "lg": {"z": 220, "rotationY": -18, "x": 30, "y": -130}}
    for k in ("bk", "sd", "lg"):
        S.ft(f"#{s}-{k}", flat[k], dict(flat[k], **sep[k]), 1.45, 0.75, "power3.out")
    # apex on "sekeren": badge punch + sheen across the plates
    S.ft(f"#{s}-lg-im", {"scale": 1}, {"scale": 1.08}, W(6), 0.12, "power2.out")
    S.ft(f"#{s}-lg-im", {"scale": 1.08}, {"scale": 1}, W(6) + 0.12, 0.35, "power2.inOut")
    for k in ("bk", "sd"):
        S.ft(f"#{s}-{k}-sh", {"x": 0, "opacity": 0.0}, {"x": 1400, "opacity": 0.55}, W(6) - 0.05, 0.6, "power2.inOut")
    apex(S, S.back, f"{s}-ap", 780, 650, W(6) + 0.05, 520, ring=True, sparks=0, op=0.4)
    S.fx(W(6), "sparkle", 0.06)
    S.fx(1.35, "whoosh", 0.05)
    # 2.6 -> end: the layers snap back into the plain screenshot (match-cut into S02)
    for k in ("bk", "sd", "lg"):
        S.ft(f"#{s}-{k}", dict(flat[k], **sep[k]), {"z": 0, "rotationY": 0, "rotationX": 0, "x": 0, "y": 0, "opacity": 1 if k == "bk" else 0},
             S.t1 - 0.42, 0.42, "power3.in")
    S.fx(S.t1 - 0.05, "click", 0.06)
    hide(S)


# ============================================================================== S02 THE UNEDITED BEFORE
def s02(S):
    s, W = S.id, S.W
    S.back.append(slab(f"{s}-bk", SHOT, HX, HY, HW, HH))
    S.ft(f"#{s}-bk", {"scale": 1}, {"scale": 1.045}, S.t0, S.t1 - S.t0, "sine.inOut")
    S.back.append(label(f"{s}-lab", HX, HY - 74, "BEFORE"))
    pop(S, f"#{s}-lab", S.t0 + 0.15, 0.35, {"opacity": 0, "y": 14}, {"opacity": 1, "y": 0}, "power3.out")
    S.front.append(cursor(f"{s}-cur", TAP[0], TAP[1], 150))
    # cursor rests (continuity), drifts, taps the real 'Default' row on "biasa"
    t = W(12)
    S.keys(f"#{s}-cur", [(S.t0, {"x": 0, "y": 0, "scale": 1}, None), (t - 0.35, {"x": 30, "y": 40}, "sine.inOut"),
                         (t - 0.06, {"x": 0, "y": 0, "scale": 0.9}, "power2.in"), (t + 0.1, {"scale": 1}, "back.out(2)")])
    S.back.append(f'<div id="{s}-rg" class="abs" style="{box(TAP[0] - 40, TAP[1] - 40, 80, 80)}border-radius:50%;border:3px solid #D97757"></div>')
    S.init(f"#{s}-rg", {"opacity": 0, "scale": 0.3})
    S.ft(f"#{s}-rg", {"opacity": 0.95, "scale": 0.3}, {"opacity": 0, "scale": 2.2}, t, 0.5, "power3.out")
    S.fx(t, "click", 0.07)
    # the tap point becomes a live separation line across the panel (handoff to S03)
    S.back.append(f'<div id="{s}-cut" class="abs line-cy" style="{box(HX - 30, TAP[1] - 2, HW + 60, 4)}transform-origin:{r3(TAP[0] - HX + 30)}px 50%"></div>')
    S.init(f"#{s}-cut", {"scaleX": 0})
    S.ft(f"#{s}-cut", {"scaleX": 0}, {"scaleX": 1}, t + 0.12, 0.38, "power3.out")
    narrator(S, NARR)
    S.intent(W(9), "present", "left")


# ============================================================================== S03 FIRST REAL EXTRACTION
def s03(S):
    s, W = S.id, S.W
    cut_y = TAP[1] - HY                     # split height inside the slab
    top = f'<div class="abs" style="left:0;top:0;width:{r3(HW)}px;height:{r3(HH)}px;clip-path:inset(0 0 {r3(HH - cut_y)}px 0)">'
    # two halves of the same real screenshot, split on the S02 line
    S.back.append(f'<div id="{s}-lo" class="abs p3" style="{box(HX, HY, HW, HH)}clip-path:inset({r3(cut_y)}px 0 0 0)">'
                  f'<img src="{SHOT}" style="position:absolute;left:0;top:0;width:{r3(HW)}px;height:{r3(HH)}px;border-radius:22px"></div>')
    S.back.append(f'<div id="{s}-hi" class="abs p3" style="{box(HX, HY, HW, HH)}clip-path:inset(0 0 {r3(HH - cut_y)}px 0)">'
                  f'<img src="{SHOT}" style="position:absolute;left:0;top:0;width:{r3(HW)}px;height:{r3(HH)}px;border-radius:22px"></div>')
    S.back.append(f'<div id="{s}-cut" class="abs line-cy" style="{box(HX - 30, TAP[1] - 2, HW + 60, 4)}"></div>')
    S.ft(f"#{s}-cut", {"opacity": 1, "scaleY": 1}, {"opacity": 0, "scaleY": 6}, S.t0 + 0.05, 0.35, "power2.out")
    S.ft(f"#{s}-hi", {"y": 0, "z": 0, "rotationX": 0}, {"y": -150, "z": -80, "rotationX": 10}, S.t0, 0.6, "power3.out")
    S.ft(f"#{s}-lo", {"y": 0, "z": 0, "rotationX": 0}, {"y": 190, "z": -80, "rotationX": -10}, S.t0, 0.6, "power3.out")
    # the genuine Claude badge rises out of the opened seam, from the real orange UI glyph position
    glyph = (HX + HW * 585 / SW, HY + HH * 75 / SH)
    S.back.append(logo3d(f"{s}-lg", 540 - 210, TAP[1] - 260, 420))
    k0 = {"x": glyph[0] - 540, "y": glyph[1] - (TAP[1] - 50), "scale": 0.06, "rotationY": 0, "z": 0, "opacity": 1}
    S.init(f"#{s}-lg", dict(k0, opacity=0))
    S.ft(f"#{s}-lg", dict(k0, opacity=0), k0, S.t0 + 0.2, 0.05, "none")
    S.ft(f"#{s}-lg", k0, {"x": 0, "y": -40, "scale": 1, "rotationY": -12, "z": 160, "opacity": 1}, S.t0 + 0.25, W(17) - S.t0 - 0.25, "power3.out")
    S.ft(f"#{s}-lg", {"rotationY": -12, "y": -40}, {"rotationY": 8, "y": -60}, W(17), S.t1 - W(17) - 0.3, "sine.inOut")
    S.fx(S.t0 + 0.25, "whoosh", 0.05)
    S.fx(W(17), "pop", 0.06)
    S.cam([(S.t0, {"z": 0}, None), (S.t1, {"z": 80}, "power2.inOut")])
    # handoff: the badge turns 90 deg on its vertical axis into a thin divider (S04)
    S.ft(f"#{s}-lg", {"rotationY": 8}, {"rotationY": 90}, S.t1 - 0.3, 0.3, "power3.in")
    hide(S)



# ============================================================================== S04 LOGO / PANEL / CURSOR = DEPTH PLANES
def s04(S):
    s, W = S.id, S.W
    # the badge (now a thin divider from S03) opens back into the front plane of an exploded view
    S.back.append(slab(f"{s}-bk", SHOT, HX, 700, HW, HH))
    S.back.append(slab(f"{s}-sd", SIDE, 150, 760, 380, 380 * 233 / 244, 18, 12))
    S.back.append(logo3d(f"{s}-lg", 600, 640, 300))
    S.back.append(cursor(f"{s}-cur", 760, 1180, 180))
    planes = [("bk", -260, None), ("sd", 0, W(18)), ("lg", 200, None), ("cur", 330, W(20))]
    for k, z, t in planes:
        S.init(f"#{s}-{k}", {"z": z})
    S.ft(f"#{s}-lg", {"rotationY": 90, "z": 200}, {"rotationY": -10, "z": 200}, S.t0, 0.45, "power3.out")
    pop(S, f"#{s}-sd", W(18) - 0.1, 0.4, {"opacity": 0, "z": -200, "x": -80}, {"opacity": 1, "z": 0, "x": 0}, "power3.out")
    pop(S, f"#{s}-cur", W(20) - 0.1, 0.4, {"opacity": 0, "z": 600, "x": 200, "y": 200}, {"opacity": 1, "z": 330, "x": 0, "y": 0}, "power3.out")
    pop(S, f"#{s}-bk", S.t0, 0.35, {"opacity": 0.6, "z": -260}, {"opacity": 1, "z": -260})
    # one camera orbits the exploded stack: three planes travel at different speeds (true parallax)
    S.cam([(S.t0, {"rotationY": -28, "rotationX": 8, "z": -60}, None), (W(25) - 0.2, {"rotationY": 22, "rotationX": 4, "z": 40}, "power2.inOut"),
           (S.t1, {"rotationY": 24, "rotationX": 4, "z": 60}, "none")])
    for k, (lab, t, x, y) in enumerate([("LOGO", S.t0 + 0.3, 700, 560), ("PANEL", W(18) + 0.1, 150, 690), ("CURSOR", W(20) + 0.1, 760, 1380)]):
        S.front.append(label(f"{s}-l{k}", x, y, lab, cyan=(k == 2)))
        pop(S, f"#{s}-l{k}", t, 0.3, {"opacity": 0, "y": 12}, {"opacity": 1, "y": 0}, "power3.out")
    S.fx(W(18), "pop", 0.05); S.fx(W(20), "pop", 0.05); S.fx(W(25), "click", 0.06)
    # quiet lock on "layer", then the cursor pierces an outline around the middle panel (handoff to S05)
    S.back.append(f'<div id="{s}-ol" class="abs" style="{box(140, 750, 400, 380 * 233 / 244 + 20)}border:3px dashed #00D0FE;border-radius:22px"></div>')
    pop(S, f"#{s}-ol", W(25), 0.25, {"opacity": 0, "scale": 1.1}, {"opacity": 1, "scale": 1}, "power3.out")
    S.ft(f"#{s}-cur", {"x": 0, "y": 0}, {"x": -440, "y": -300}, S.t1 - 0.35, 0.35, "power3.in")
    hide(S)


# ============================================================================== S05 CLAUDE CODE AS THE MOTION WORKSPACE (educator mode)
def s05(S):
    s, W = S.id, S.W
    edu_bg(S, S.back)
    fw = 900; fh = fw * 929 / 1648
    S.back.append(panel(f"{s}-pn", 90, 420, fw, fh, f'<img src="{FULL}" style="position:absolute;left:0;top:0;width:{fw}px;height:{r3(fh)}px">'))
    pop(S, f"#{s}-pn", S.t0, 0.45, {"opacity": 0, "rotationX": 18, "y": 60, "scale": 0.92}, {"opacity": 1, "rotationX": 6, "y": 0, "scale": 1}, "power3.out")
    S.ft(f"#{s}-pn", {"rotationX": 6, "rotationY": -6}, {"rotationX": 4, "rotationY": 6}, S.t0 + 0.45, S.t1 - S.t0 - 0.5, "sine.inOut")
    # three real snippets lift out of the screen with transform gizmos (labels are ours, the snippets are genuine)
    snips = [("CURSOR", CUR, 120, 560, 120, 118, W(29)), ("PANEL", SIDE, 400, 500, 200, 191, W(30)), ("TIMING", SHOT, 680, 560, 280, 189, W(33))]
    for k, (lab, src, x, y, w, h, t) in enumerate(snips):
        pix = "image-rendering:pixelated;" if src == CUR else ""
        S.front.append(f'<div id="{s}-g{k}" class="abs p3" style="{box(x, y, w, h)}">'
                       f'<img src="{src}" style="position:absolute;left:0;top:0;width:{w}px;height:{h}px;border-radius:10px;{pix}filter:drop-shadow(0 18px 18px rgba(0,0,0,.5))">'
                       f'<div class="abs" style="left:-8px;top:-8px;width:{w + 16}px;height:{h + 16}px;border:2px dashed #00D0FE;border-radius:12px"></div>'
                       + "".join(f'<div class="abs" style="left:{cx - 7}px;top:{cy - 7}px;width:14px;height:14px;background:#fff;border:2px solid #00D0FE;border-radius:3px"></div>'
                                 for cx, cy in [(-8, -8), (w + 8, -8), (-8, h + 8), (w + 8, h + 8)])
                       + f'<div class="abs" style="left:0;top:{h + 18}px;width:{w}px;text-align:center;font:700 24px/1 Poppins;letter-spacing:.1em;color:#fff">{lab}</div></div>')
        pop(S, f"#{s}-g{k}", t - 0.05, 0.45, {"opacity": 0, "z": -120, "y": 60, "scale": 0.8}, {"opacity": 1, "z": 80, "y": 0, "scale": 1}, "back.out(1.5)")
        S.ft(f"#{s}-g{k}", {"rotation": 0, "x": 0}, {"rotation": [-6, 5, -4][k], "x": [16, -10, 12][k]}, W(34) - 0.1, 0.5, "power2.inOut")
        S.fx(t, "pop", 0.04)
    narrator(S, HALF)
    S.intent(W(27), "explain", "left")
    S.intent(W(33), "present", "right")
    # handoff: the real cursor snippet accelerates across the frame
    S.ft(f"#{s}-g0", {"x": 16, "scale": 1}, {"x": 1100, "scale": 2.2}, S.t1 - 0.3, 0.3, "power3.in")


# ============================================================================== S06 CURSOR CAUSES THE CUT
def s06(S):
    s, W = S.id, S.W
    hide(S)
    S.back.append(slab(f"{s}-bk", SHOT, HX, 660, HW, HH))
    # the slab's top-left wedge is a separate genuine piece, peeled away like a track matte when the cursor slices it
    S.back.append(f'<div id="{s}-pe" class="abs p3" style="{box(HX, 660, HW, HH)}clip-path:polygon(0 0,100% 0,0 100%);transform-origin:0 0">'
                  f'<img src="{SHOT}" style="position:absolute;left:0;top:0;width:{HW}px;height:{r3(HH)}px;border-radius:22px;filter:brightness(1.08)"></div>')
    S.back.append(f'<div id="{s}-port" class="abs" style="{box(HX, 660, HW, HH)}clip-path:polygon(0 0,100% 0,0 100%);border-radius:22px;'
                  f'background:radial-gradient(circle at 30% 30%,#3e7fc4,#0A0D2C)"></div>')
    S.init(f"#{s}-port", {"opacity": 0})
    S.back.append(f'<svg id="{s}-sl" class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<line x1="{HX + HW}" y1="660" x2="{HX}" y2="{660 + HH}" stroke="#00D0FE" stroke-width="5" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" id="{s}-ln"/></svg>')
    S.front.append(cursor(f"{s}-cur", HX + HW, 660, 300))
    hit = W(37)
    S.keys(f"#{s}-cur", [(S.t0, {"x": 500, "y": -500}, None), (hit - 0.1, {"x": 0, "y": 0}, "power4.in"),
                         (hit + 0.25, {"x": -HW, "y": HH}, "power2.inOut"), (S.t1, {"x": -HW - 300, "y": HH + 300}, "power3.in")])
    S.ft(f"#{s}-ln", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, hit - 0.05, 0.3, "power2.out")
    S.ft(f"#{s}-pe", {"rotationX": 0, "rotationY": 0, "z": 0, "opacity": 1}, {"rotationX": 40, "rotationY": -35, "z": 260, "opacity": 0}, hit + 0.25, 0.6, "power3.in")
    S.ft(f"#{s}-port", {"opacity": 0}, {"opacity": 1}, hit + 0.3, 0.4, "power2.out")
    S.fx(hit, "click", 0.08); S.fx(hit + 0.25, "whoosh", 0.05)
    S.cam([(S.t0, {"z": 0}, None), (hit, {"z": 0}, None), (hit + 0.05, {"x": -6, "y": 4}, "none"), (hit + 0.15, {"x": 0, "y": 0}, "power2.out"), (S.t1, {"z": 60}, "power2.in")])


# ============================================================================== S07 CAMERA DRIVES PANEL PARALLAX
def s07(S):
    s, W = S.id, S.W
    hide(S)
    S.back.append(slab(f"{s}-bk", SHOT, HX, 700, HW, HH))
    S.back.append(slab(f"{s}-sd", SIDE, 120, 560, 420, 420 * 233 / 244, 18, 14))
    S.init(f"#{s}-bk", {"z": -220}); S.init(f"#{s}-sd", {"z": 180})
    pop(S, f"#{s}-sd", S.t0, 0.4, {"opacity": 0, "x": -300, "rotationY": 40, "z": 180}, {"opacity": 1, "x": 0, "rotationY": 0, "z": 180}, "power3.out")
    S.cam([(S.t0, {"rotationY": -30, "rotationX": 6, "x": -60}, None), (W(41), {"rotationY": 18, "rotationX": 2, "x": 40}, "power2.inOut"),
           (S.t1, {"rotationY": 24, "x": 60, "z": 80}, "power1.in")])
    for k in ("bk", "sd"):
        S.ft(f"#{s}-{k}-sh", {"x": 0, "opacity": 0}, {"x": 1400, "opacity": 0.5}, W(41) - 0.3, 0.7, "power2.inOut")
    S.fx(W(38), "whoosh", 0.05)
    # lands on a typographic baseline for S08
    S.back.append(f'<div id="{s}-base" class="abs line-cy" style="{box(90, 1460, 900, 5)}transform-origin:0 50%"></div>')
    S.init(f"#{s}-base", {"scaleX": 0})
    S.ft(f"#{s}-base", {"scaleX": 0}, {"scaleX": 1}, S.t1 - 0.35, 0.35, "power3.out")


# ============================================================================== S08 TYPE SYNCS TO WORDS
def s08(S):
    s, W = S.id, S.W
    hide(S)
    S.back.append(slab(f"{s}-bk", SHOT, HX, 520, HW, HH))
    S.init(f"#{s}-bk", {"z": -200, "opacity": 0.55})
    S.back.append(f'<div id="{s}-base" class="abs line-cy" style="{box(90, 1460, 900, 5)}transform-origin:0 50%"></div>')
    wl = [("teks", 43, 120, 1000), ("muncul", 44, 420, 1000), ("tepat", 45, 120, 1140), ("mengikuti", 46, 410, 1140), ("suara.", 47, 120, 1280)]
    for k, (wd, wi, x, y) in enumerate(wl):
        cy = "color:#00D0FE;" if wd == "suara." else ""
        size = 150 if wd == "suara." else 104
        S.back.append(f'<div class="abs" style="left:{x}px;top:{y}px;overflow:hidden;padding:0 6px 14px"><div id="{s}-w{k}" style="font:700 {size}px/1 Poppins;color:#fff;{cy}letter-spacing:-.02em">{wd}</div></div>')
        S.init(f"#{s}-w{k}", {"yPercent": 115})
        S.ft(f"#{s}-w{k}", {"yPercent": 115}, {"yPercent": 0}, W(wi) - 0.03, 0.32, "power4.out")
        S.ft(f"#{s}-w{k}", {"scale": 1.08}, {"scale": 1}, W(wi) + 0.29, 0.25, "power2.out")
        S.fx(W(wi), "key", 0.04)
    S.cam([(S.t0, {"y": 60, "z": 40}, None), (W(47), {"y": -40, "z": 0}, "power2.inOut"), (S.t1, {"y": -60, "z": -30}, "sine.inOut")])
    # handoff: the lines compress into a horizontal ruler (S09 timeline)
    S.ft(f"#{s}-base", {"scaleY": 1, "y": 0}, {"scaleY": 3, "y": -200}, S.t1 - 0.3, 0.3, "power3.in")


# ============================================================================== S09-S11 EDUCATOR MODE (half-body mascot, blurred world, sharp panel)
PX, PY, PW, PH = 90, 410, 900, 580


def s09(S):
    s, W = S.id, S.W
    edu_bg(S, S.back)
    hw = PW / 2 - 30; hh = hw * SH / SW
    inner = (f'<div id="{s}-flat" class="abs" style="left:24px;top:110px;width:{r3(hw)}px;height:{r3(hh)}px"><img src="{SHOT}" style="width:100%;height:100%;border-radius:10px;opacity:.85"></div>'
             f'<div id="{s}-deep" class="abs p3" style="left:{r3(PW / 2 + 6)}px;top:110px;width:{r3(hw)}px;height:{r3(hh)}px">'
             f'<img src="{SHOT}" style="position:absolute;inset:0;width:100%;height:100%;border-radius:10px;box-shadow:0 30px 40px -18px rgba(0,0,0,.8),0 0 0 1px rgba(255,255,255,.15)">'
             f'<img id="{s}-dl" src="{LOGO}" style="position:absolute;left:{r3(hw * 0.62)}px;top:-50px;width:120px;height:120px;filter:drop-shadow(0 16px 14px rgba(0,0,0,.5))"></div>'
             f'<div class="abs" style="left:24px;top:{r3(130 + hh)}px;font:700 26px/1 Poppins;color:rgba(255,255,255,.6)">FLAT</div>'
             f'<div class="abs" style="left:{r3(PW / 2 + 6)}px;top:{r3(130 + hh)}px;font:700 26px/1 Poppins;color:#00D0FE">DEPTH</div>'
             f'<div id="{s}-div" class="abs line-cy" style="left:{r3(PW / 2 - 3)}px;top:90px;width:5px;height:{r3(hh + 80)}px"></div>')
    S.back.append(panel(f"{s}-pn", PX, PY, PW, PH, inner, "MOTION MAHAL"))
    pop(S, f"#{s}-pn", S.t0 + 0.05, 0.45, {"opacity": 0, "y": 40, "scale": 0.94}, {"opacity": 1, "y": 0, "scale": 1}, "power3.out")
    S.ft(f"#{s}-deep", {"rotationY": 0, "rotationX": 0, "z": 0}, {"rotationY": -22, "rotationX": 10, "z": 40}, W(52), 0.7, "power3.inOut")
    S.ft(f"#{s}-dl", {"y": 30, "scale": 0.6}, {"y": 0, "scale": 1}, W(52) + 0.2, 0.5, "back.out(1.6)")
    S.ft(f"#{s}-div", {"x": 0}, {"x": -380}, W(55) - 0.1, 0.45, "power3.inOut")
    S.ft(f"#{s}-flat", {"opacity": 1}, {"opacity": 0.35}, W(55), 0.3, "power2.out")
    S.fx(W(55), "pop", 0.05)
    narrator(S, HALF)
    S.intent(W(48), "explain", "left")
    S.intent(W(53), "emphasize", "right")


def s10(S):
    s, W = S.id, S.W
    edu_bg(S, S.back)
    iw = PW - 80; ih = iw * SH / SW
    junk = "".join(f'<div id="{s}-j{k}" class="abs" style="{st}"></div>' for k, st in enumerate([
        f"left:{iw * 0.1}px;top:20px;width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,rgba(255,240,120,.9),rgba(255,120,60,.4) 40%,rgba(255,0,120,0) 70%)",
        f"left:0;top:{ih * 0.45}px;width:{iw}px;height:40px;background:repeating-linear-gradient(90deg,rgba(255,0,90,.7) 0 14px,rgba(0,255,220,.7) 14px 28px)",
        f"left:{iw * 0.55}px;top:{ih * 0.15}px;width:300px;height:300px;background:conic-gradient(from 0deg,rgba(255,255,255,.0),rgba(255,255,255,.7),rgba(255,255,255,0) 20%,rgba(255,255,255,.7) 40%,rgba(255,255,255,0) 60%);border-radius:50%"]))
    inner = f'<div id="{s}-ui" class="abs" style="left:40px;top:80px;width:{r3(iw)}px;height:{r3(ih)}px"><img src="{SHOT}" style="width:100%;height:100%;border-radius:12px">{junk}</div>'
    S.back.append(panel(f"{s}-pn", PX, PY, PW, PH, inner, "BUKAN EFEK NUMPUK"))
    S.ft(f"#{s}-pn", {"opacity": 1}, {"opacity": 1}, S.t0, 0.01, "none")
    for k, t in enumerate([W(57), W(59), W(60)]):
        pop(S, f"#{s}-j{k}", t - 0.05, 0.22, {"opacity": 0, "scale": 0.4, "x": [-80, 0, 80][k]}, {"opacity": 1, "scale": 1, "x": 0}, "back.out(2)")
        S.ft(f"#{s}-j{k}", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.2}, W(61) + 0.1 + k * 0.05, 0.22, "power3.in")
        S.fx(t, "pop", 0.04)
    S.ft(f"#{s}-ui", {"rotation": 0}, {"rotation": 0}, S.t0, 0.01, "none")
    narrator(S, HALF, rise=False)
    S.intent(W(56), "emphasize", "left")


def s11(S):
    s, W = S.id, S.W
    edu_bg(S, S.back)
    cw = (PW - 100) / 3
    ruler = "".join(f'<div class="abs" style="left:{20 + k * 22}px;top:{60 if k % 4 else 40}px;width:3px;height:{20 if k % 4 else 40}px;background:rgba(255,255,255,.7)"></div>' for k in range(10))
    cards = [("TIMING", f'{ruler}<div id="{s}-ph" class="abs line-cy" style="left:20px;top:30px;width:5px;height:90px"></div>', W(63)),
             ("KEDALAMAN", f'<img src="{SHOT}" style="position:absolute;left:30px;top:30px;width:150px;opacity:.5;border-radius:6px"><img src="{SHOT}" style="position:absolute;left:60px;top:55px;width:150px;opacity:.8;border-radius:6px">'
                           f'<img src="{LOGO}" style="position:absolute;left:150px;top:30px;width:70px">', W(64)),
             ("TRANSISI", f'<img src="{CUR}" style="position:absolute;left:80px;top:30px;width:90px;image-rendering:pixelated">', W(66))]
    inner = ""
    for k, (lab, art, t) in enumerate(cards):
        x = 30 + k * (cw + 20)
        inner += (f'<div id="{s}-c{k}" class="abs" style="left:{r3(x)}px;top:90px;width:{r3(cw)}px;height:300px;border-radius:18px;background:rgba(10,13,44,.6);border:1.5px solid rgba(0,208,254,.35)">'
                  f'<div class="abs" style="left:0;top:20px;width:{r3(cw)}px;height:200px">{art}</div>'
                  f'<div class="abs" style="left:0;top:240px;width:{r3(cw)}px;text-align:center;font:700 26px/1 Poppins;color:#fff">{lab}</div></div>')
    inner += f'<div id="{s}-link" class="abs line-cy" style="left:60px;top:430px;width:{PW - 120}px;height:5px;transform-origin:0 50%"></div>'
    S.back.append(panel(f"{s}-pn", PX, PY, PW, PH, inner, "SALING TERHUBUNG"))
    for k, (_, _, t) in enumerate(cards):
        pop(S, f"#{s}-c{k}", t - 0.08, 0.38, {"opacity": 0, "y": 30, "rotationY": -40}, {"opacity": 1, "y": 0, "rotationY": 0}, "power3.out")
        S.ft(f"#{s}-c{k}", {"borderColor": "rgba(0,208,254,.35)"}, {"borderColor": "rgba(0,208,254,1)"}, t + 0.2, 0.2, "power2.out")
        S.fx(t, "pop", 0.04)
    S.ft(f"#{s}-ph", {"x": 0}, {"x": 190}, W(63), 1.2, "none")
    S.init(f"#{s}-link", {"scaleX": 0})
    S.ft(f"#{s}-link", {"scaleX": 0}, {"scaleX": 1}, W(68), W(69) + 0.3 - W(68), "power2.inOut")
    S.fx(W(69), "ping", 0.06)
    narrator(S, HALF, rise=False)
    S.intent(W(63), "compare", "left")
    S.intent(W(69), "present", "right")
    # handoff: the panel aperture closes to a vertical divider (the comparison slider)
    S.ft(f"#{s}-pn", {"scaleX": 1, "opacity": 1}, {"scaleX": 0.01, "opacity": 1}, S.t1 - 0.3, 0.3, "power3.in")
    S.mv([(S.t1 - 0.35, dict(HALF), None), (S.t1, dict(HALF, fy=3200), "power3.in")])


# ============================================================================== S12-S13 THE TRUE BEFORE / AFTER
def comparison(S, slider_at, drag_t0, drag_t1, push_at=None):
    s = S.id
    BX, BY, BW = 40, 560, 1000
    BH = BW * SH / SW
    after = (f'<div class="abs p3" style="left:0;top:0;width:{BW}px;height:{r3(BH)}px;background:radial-gradient(circle at 60% 40%,#294B77,#0A0D2C)">'
             f'<img id="{s}-a0" src="{SHOT}" style="position:absolute;left:90px;top:90px;width:{BW - 260}px;border-radius:14px;box-shadow:0 30px 40px -20px rgba(0,0,0,.8)">'
             f'<img id="{s}-a1" src="{SIDE}" style="position:absolute;left:40px;top:250px;width:280px;border-radius:12px;box-shadow:0 30px 40px -20px rgba(0,0,0,.8)">'
             f'<img id="{s}-a2" src="{LOGO}" style="position:absolute;left:{BW - 330}px;top:30px;width:240px;filter:drop-shadow(0 20px 20px rgba(0,0,0,.5))"></div>')
    S.back.append(f'<div id="{s}-win" class="abs plate" style="{box(BX, BY, BW, BH)}overflow:hidden;padding:0;border:2px solid rgba(0,208,254,.6)">{after}'
                  f'<div id="{s}-bef" class="abs" style="left:0;top:0;width:{BW}px;height:{r3(BH)}px;clip-path:inset(0px {r3(BW - slider_at)}px 0px 0px)"><img src="{SHOT}" style="width:{BW}px;height:{r3(BH)}px"></div>'
                  f'<div id="{s}-sl" class="abs" style="left:{slider_at - 3}px;top:0;width:6px;height:{r3(BH)}px;background:#00D0FE"></div>'
                  f'<div class="abs" style="left:20px;top:{r3(BH - 60)}px;font:700 26px/1 Poppins;color:#fff">BEFORE</div>'
                  f'<div class="abs" style="left:{BW - 150}px;top:{r3(BH - 60)}px;font:700 26px/1 Poppins;color:#00D0FE">AFTER</div></div>')
    for k, (a, b) in enumerate([({"y": 0, "rotation": 0}, {"y": -18, "rotation": 2}), ({"y": 0, "x": 0}, {"y": 22, "x": 10}), ({"y": 0, "rotation": 0}, {"y": -24, "rotation": -6})]):
        S.ft(f"#{s}-a{k}", a, b, S.t0, S.t1 - S.t0, "sine.inOut")
    S.back.append(cursor(f"{s}-cur", BX + slider_at, BY + BH / 2, 130))
    return BX, BY, BW, BH


def s12(S):
    s, W = S.id, S.W
    hide(S)
    BX, BY, BW, BH = comparison(S, 500, 0, 0)
    S.ft(f"#{s}-win", {"scaleX": 0.02, "opacity": 1}, {"scaleX": 1, "opacity": 1}, S.t0, 0.45, "power3.out")
    S.ft(f"#{s}-cur", {"x": 0, "y": 160, "opacity": 0}, {"x": 0, "y": 0, "opacity": 1}, W(71), 0.4, "power2.out")
    # anticipation: the pointer grabs the slider on "bandingkan"
    S.ft(f"#{s}-cur", {"scale": 1}, {"scale": 0.88}, W(72), 0.1, "power2.in")
    S.ft(f"#{s}-sl", {"scaleX": 1}, {"scaleX": 2}, W(72), 0.15, "power2.out")
    S.fx(W(72), "click", 0.06)


def s13(S):
    s, W = S.id, S.W
    BX, BY, BW, BH = comparison(S, 500, 0, 0)
    t0, t1 = W(74), W(79)
    S.ft(f"#{s}-bef", {"clipPath": "inset(0px 500px 0px 0px)"}, {"clipPath": f"inset(0px {BW - 60}px 0px 0px)"}, t0, t1 - t0, "power2.inOut")
    S.ft(f"#{s}-sl", {"x": 0}, {"x": -440}, t0, t1 - t0, "power2.inOut")
    S.ft(f"#{s}-cur", {"x": 0}, {"x": -440}, t0, t1 - t0, "power2.inOut")
    S.ft(f"#{s}-cur", {"opacity": 1}, {"opacity": 0}, t1 + 0.1, 0.2, "none")
    S.cam([(S.t0, {"z": 0}, None), (W(80), {"z": 0}, None), (W(84), {"z": 260, "x": -60, "y": -40}, "power2.inOut"), (S.t1, {"z": 300}, "none")])
    apex(S, S.back, f"{s}-ap", 640, BY + BH / 2, W(84) + 0.05, 600, ring=True, sparks=6, op=0.4)
    S.fx(t0, "whoosh", 0.05); S.fx(W(84), "sparkle", 0.06)
    narrator(S, NARR)
    S.intent(W(80), "pointFwd", "left")


# ============================================================================== S14 EARNED CTA
def s14(S):
    s, W = S.id, S.W
    edu_bg(S, S.back, dim=0.4)
    S.front.append(f'<div id="{s}-bub" class="abs plate" style="{box(90, 470, 900, 300)}border:2.5px solid #00D0FE;border-radius:46px;overflow:hidden">'
                   f'<div class="abs" style="left:0;top:58px;width:900px;text-align:center;font:700 92px/1 Poppins;color:#fff">KOMEN <span id="{s}-kw" class="cy">MOTION</span></div>'
                   f'<div class="abs" style="left:0;top:184px;width:900px;text-align:center;font:400 34px/1.2 Poppins;color:rgba(255,255,255,.85)">prompt + breakdown cara bikinnya</div>'
                   f'<div id="{s}-sh" class="abs sheen" style="left:-260px;top:0;width:200px;height:300px"></div></div>'
                   f'<div id="{s}-tail" class="abs" style="left:470px;top:764px;width:0;height:0;border-left:36px solid transparent;border-right:36px solid transparent;border-top:44px solid #00D0FE"></div>')
    pop(S, f"#{s}-bub", W(88) - 0.1, 0.5, {"opacity": 0, "scale": 0.8, "y": 40}, {"opacity": 1, "scale": 1, "y": 0}, "back.out(1.5)")
    pop(S, f"#{s}-tail", W(88) + 0.2, 0.3)
    S.front.append(cursor(f"{s}-cur", 940, 700, 120))
    S.keys(f"#{s}-cur", [(S.t0, {"x": 300, "y": 400, "opacity": 0}, None), (W(93), {"x": 0, "y": 0, "opacity": 1}, "power3.out"),
                         (W(94) - 0.06, {"scale": 0.86}, "power2.in"), (W(94) + 0.12, {"scale": 1}, "back.out(2)"), (W(94) + 0.6, {"x": 120, "y": 120, "opacity": 0}, "power2.in")])
    S.fx(W(94) - 0.02, "click", 0.05)
    S.ft(f"#{s}-kw", {"scale": 1.12, "y": -6}, {"scale": 1, "y": 0}, W(94), 0.35, "back.out(2.2)")
    S.ft(f"#{s}-sh", {"x": 0}, {"x": 1300}, W(94) + 0.15, 0.6, "power2.inOut")
    apex(S, S.front, f"{s}-ap", 640, 560, W(94) + 0.08, 520, ring=True, sparks=6, op=0.4)
    narrator(S, HALF)
    S.intent(W(86), "explain", "left")
    S.intent(W(93), "cta", "right")
