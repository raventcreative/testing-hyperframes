"""CLAUDE CODE MOTION REEL 01 — 'the screenshot comes alive'. Genuine assets only (assets/ui, masked/cleaned copies
from tools/prep_ui.py). 2.5D language: real screenshots become physical slabs (front face + dark back slab for visible
thickness, glossy rim, contact shadow), arranged on CSS-3D depth planes and moved by one camera. The pixel cursor is the
editing tool that causes every cut. All times are measured VO word starts (S.W)."""
from xk import box, r3, apex
from kit_cc import pop, MASCOT_C, OFF

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
    hide(S)


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


def placeholder(S):
    hide(S)
    S.back.append(f'<div id="{S.id}-ph" class="abs sub" style="left:0;top:900px;width:1080px;text-align:center;font-size:40px;opacity:.5">{S.id} — dibangun setelah proof disetujui</div>')
