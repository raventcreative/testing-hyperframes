"""The 18 shots of the Claude Code 3D remake (brief 03_PREMIUM_STORYBOARD.md), every apex keyed to the measured VO.
Each sNN(S) builds one scene; the last ~0.3 s of a scene morphs one physical element into the first element of the next
scene (same place, same shape) so every cut is motivated (transition chart S01->S18)."""
from xk import el, box, r3, check_svg, apex, clip_rect, CLIP_NONE
from kit_cc import (heading, step_badge, cursor, click, appwin, laptop, folder3d, phone, checkrow, led_on, pop, out,
                    MASCOT_R, MASCOT_L, MASCOT_C, OFF, HEAD_Y, CY)

LINE_Y = 1180      # S01 -> S02 playhead/cable height


def vframe(layer, fid, rect, r=40, w=3):
    """cyan rounded frame as an SVG rect (attr-tweened: no layout snapping, stroke never distorts)"""
    x, y, ww, hh = rect
    layer.append(f'<svg id="{fid}" class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                 f'<rect id="{fid}-r" x="{x}" y="{y}" width="{ww}" height="{hh}" rx="{r}" fill="none" stroke="#00D0FE" stroke-width="{w}"/></svg>')


def vmove(S, fid, a, b, at, dur, ease, ra=40, rb=40):
    S.ft(f"#{fid}-r", {"attr": {"x": a[0], "y": a[1], "width": a[2], "height": a[3], "rx": ra}}, {"attr": {"x": b[0], "y": b[1], "width": b[2], "height": b[3], "rx": rb}}, at, dur, ease)


def hide_mascot(S):
    S.mv([(S.t0, dict(OFF), None)])


def narrator(S, view, rise=True):
    """mascot enters its framing for this scene (rises from below on the first scene he appears in a run)"""
    if rise:
        S.mv([(S.t0, dict(view, fy=view["fy"] + 900, vis=1), None), (S.t0 + 0.12, dict(view, fy=view["fy"] + 900), None),
              (S.t0 + 0.75, dict(view), "power3.out")])
    else:
        S.mv([(S.t0, dict(view, vis=1), None)])


def mini_anim(pid):
    """original 'finished animation' frame shown inside screens: navy sky, sun disc, city blocks, mascot silhouette slot"""
    blocks = "".join(f'<div class="abs" style="left:{x}%;bottom:18%;width:{w}%;height:{h}%;background:linear-gradient(180deg,#2e5c95,#132a52);border-radius:4px 4px 0 0;'
                     f'box-shadow:inset 1px 1px 0 rgba(255,255,255,.25)"></div>' for x, w, h in [(6, 12, 30), (20, 10, 44), (32, 14, 24), (60, 12, 38), (74, 16, 52), (88, 9, 28)])
    return (f'<div id="{pid}" class="abs" style="inset:0;background:linear-gradient(180deg,#1f4f8f 0%,#3e7fc4 55%,#9cc7ee 100%);overflow:hidden">'
            f'<div id="{pid}-sun" class="abs" style="left:58%;top:22%;width:22%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,#fff6d8,#ffd27a 55%,rgba(255,210,122,0) 72%)"></div>'
            f'{blocks}<div class="abs" style="left:0;bottom:0;width:100%;height:18%;background:linear-gradient(180deg,#1b2f55,#0c1834)"></div>'
            f'<div id="{pid}-play" class="abs" style="left:4%;bottom:5%;width:92%;height:5px;border-radius:3px;background:rgba(255,255,255,.25)">'
            f'<div id="{pid}-prog" class="abs line-cy" style="left:0;top:0;height:5px;width:100%;transform-origin:0 50%"></div></div></div>')


# ============================================================================== S01 FINISHED PRODUCT FIRST
def s01(S):
    s, W = S.id, S.W
    # three miniature production planes behind the hero phone (script / character / camera path)
    for k, (lab, x, y, rot) in enumerate([("SCRIPT", 70, 640, -16), ("KARAKTER", 690, 560, 14), ("KAMERA", 640, 1010, 10)]):
        S.back.append(f'<div id="{s}-c{k}" class="abs plate plate-s" style="{box(x, y, 320, 200)}transform:rotateY({rot}deg)">'
                      f'<div class="abs sub" style="left:24px;top:18px;font-size:26px;color:#00D0FE;font-weight:700">{lab}</div>'
                      + "".join(f'<div class="abs" style="left:24px;top:{70 + j * 34}px;width:{240 - j * 50}px;height:12px;border-radius:6px;background:rgba(255,255,255,.22)"></div>' for j in range(3))
                      + '</div>')
        pop(S, f"#{s}-c{k}", S.t0 + 0.15 + k * 0.12, 0.5, {"opacity": 0, "z": -300, "y": 40}, {"opacity": 1, "z": 0, "y": 0}, "power3.out")
        S.ft(f"#{s}-c{k}", {"y": 0}, {"y": -24 if k % 2 else 18}, S.t0 + 0.7, S.t1 - S.t0 - 0.9, "sine.inOut")
    S.back.append(phone(f"{s}-ph", 345, 470, 360, mini_anim(f"{s}-an")))
    pop(S, f"#{s}-ph", S.t0, 0.6, {"opacity": 0, "scale": 1.25, "rotationY": -24, "y": 60}, {"opacity": 1, "scale": 1, "rotationY": -8, "y": 0}, "power3.out")
    S.ft(f"#{s}-ph", {"rotationY": -8}, {"rotationY": 6}, S.t0 + 0.6, 2.4, "sine.inOut")
    S.ft(f"#{s}-an-sun", {"y": 0}, {"y": 30}, S.t0, 3.4, "sine.inOut")
    S.init(f"#{s}-an-prog", {"scaleX": 0})
    S.ft(f"#{s}-an-prog", {"scaleX": 0}, {"scaleX": 1}, S.t0, S.t1 - S.t0 - 0.35, "none")
    S.fx(S.t0 + 0.05, "whoosh", 0.06)
    heading(S, S.front, f"{s}-h", "SATU TIM *EDITOR?*", 60, HEAD_Y, 960, 74, "center", keys=[W(6), W(7), W(8)])
    # bracket grows around EDITOR on the word
    S.front.append(f'<div id="{s}-brk" class="abs brk" style="{box(470, HEAD_Y + 16, 420, 110)}"></div>')
    pop(S, f"#{s}-brk", W(8) + 0.05, 0.3, {"opacity": 0, "scaleX": 0.4, "scaleY": 0.6}, {"opacity": 1, "scaleX": 1, "scaleY": 1}, "power3.out")
    apex(S, S.front, f"{s}-ap", 680, HEAD_Y + 70, W(8) + 0.08, 360, ring=True, sparks=0, op=0.35)
    S.fx(W(8), "pop", 0.07)
    narrator(S, MASCOT_R)
    S.intent(W(1), "pointFwd", "left")
    S.intent(W(5), "question")
    # handoff: the phone's playhead becomes a cyan cable across the frame (same y as S02's cable)
    S.front.append(f'<div id="{s}-cab" class="abs line-cy" style="{box(0, LINE_Y, 1080, 6)}transform-origin:500px 50%"></div>')
    S.init(f"#{s}-cab", {"scaleX": 0, "opacity": 0})
    S.ft(f"#{s}-cab", {"scaleX": 0.3, "opacity": 0}, {"scaleX": 1, "opacity": 1}, S.t1 - 0.34, 0.34, "power3.in")
    S.ft(f"#{s}-ph", {"opacity": 1, "y": 0}, {"opacity": 0, "y": 80}, S.t1 - 0.3, 0.3, "power2.in")


# ============================================================================== S02 THE SECRET REVEAL
def s02(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-cab" class="abs line-cy" style="{box(0, LINE_Y, 1080, 6)}"></div>')
    # the cable lands and becomes a single input strip
    S.ft(f"#{s}-cab", {"scaleX": 1, "opacity": 1}, {"scaleX": 0.78, "opacity": 0}, S.t0 + 0.05, 0.35, "power3.out")
    S.back.append(f'<div id="{s}-in" class="abs plate" style="{box(110, LINE_Y - 66, 860, 132)}border-radius:66px">'
                  f'<div class="abs sub mono" id="{s}-tx" style="left:44px;top:42px;width:720px;font-size:34px;color:#fff;white-space:nowrap;overflow:hidden"></div>'
                  f'<div id="{s}-car" class="abs" style="left:44px;top:40px;width:4px;height:50px;background:#00D0FE"></div></div>')
    pop(S, f"#{s}-in", S.t0 + 0.12, 0.4, {"opacity": 0, "scaleY": 0.05, "scaleX": 1.2}, {"opacity": 1, "scaleY": 1, "scaleX": 1}, "power3.out")
    line = "Bikin video animasi 3D..."
    t0, t1 = W(10), W(15) - 0.1
    S.init(f"#{s}-tx", {"textContent": ""})
    for k in range(1, len(line) + 1):
        at = t0 + (t1 - t0) * k / len(line)
        S.tset(f"#{s}-tx", {"textContent": line[:k]}, at)
        if k % 3 == 0:
            S.fx(at, "key", 0.03)
        S.tset(f"#{s}-car", {"x": round(20.5 * k, 1)}, at)
    # the workflow station rises behind the strip on "Claude Code"
    for k, (lab, x) in enumerate([("STORYBOARD", 120), ("KAMERA", 420), ("RENDER", 720)]):
        S.back.append(f'<div id="{s}-m{k}" class="abs p3" style="{box(x, 760, 240, 240)}">'
                      f'<div class="abs cshadow" style="{box(-20, 200, 280, 70)}"></div>'
                      f'<div class="abs metal" style="{box(0, 0, 240, 200)}border-radius:22px;border:1.5px solid rgba(0,208,254,.35)"></div>'
                      f'<div class="abs sub" style="left:0;top:80px;width:240px;text-align:center;font-size:28px;font-weight:700;color:#fff">{lab}</div></div>')
        pop(S, f"#{s}-m{k}", W(17) + k * 0.09, 0.5, {"opacity": 0, "y": 160, "rotationX": 50}, {"opacity": 1, "y": 0, "rotationX": 12}, "back.out(1.3)")
    S.fx(W(17), "whoosh", 0.06)
    heading(S, S.front, f"{s}-h", "*SATU* *KALIMAT*", 60, HEAD_Y, 960, 84, "center", keys=[W(14), W(15)])
    S.front.append(f'<div id="{s}-sub" class="abs sub" style="left:0;top:{HEAD_Y + 170}px;width:1080px;text-align:center;font-size:40px">di <b class="cy">Claude Code</b></div>')
    pop(S, f"#{s}-sub", W(17) - 0.05, 0.35)
    apex(S, S.front, f"{s}-ap", 540, HEAD_Y + 80, W(15) + 0.1, 520, ring=True, sparks=6, op=0.5)
    S.fx(W(15) + 0.05, "sparkle", 0.06)
    narrator(S, dict(MASCOT_R, fx=880, h=760), rise=False)
    S.intent(W(13), "present", "left")
    # handoff: the strip folds into a slim numbered ribbon
    S.ft(f"#{s}-in", {"scaleY": 1}, {"scaleY": 0.22}, S.t1 - 0.28, 0.28, "power3.in")
    S.ft(f"#{s}-tx", {"opacity": 1}, {"opacity": 0}, S.t1 - 0.3, 0.12, "none")
    for k in range(3):
        S.ft(f"#{s}-m{k}", {"opacity": 1}, {"opacity": 0, "y": 120}, S.t1 - 0.3, 0.28, "power2.in")


# ============================================================================== S03 SIX-STEP MYSTERY
STEPS = ["DESKTOP", "FOLDER", "LOKAL", "CEK", "IDE", "REVISI"]


def s03(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-rib" class="abs plate" style="{box(110, LINE_Y - 15, 860, 30)}border-radius:15px"></div>')
    S.ft(f"#{s}-rib", {"opacity": 1, "scaleX": 1}, {"opacity": 0, "scaleX": 1.15}, S.t0 + 0.2, 0.3, "power2.in")
    S.back.append(f'<div id="{s}-trk" class="abs p3" style="{box(0, 560, 1080, 760)}">'
                  f'<div class="abs grid-fine" style="{box(60, 520, 960, 260)}transform:rotateX(70deg);opacity:.8"></div></div>')
    for k in range(6):
        col, row = k % 3, k // 3
        x, y = 90 + col * 315, 590 + row * 330
        dark = k == 5
        bg = "background:linear-gradient(150deg,#0b1024,#05070f);border:2px solid rgba(0,208,254,.8)" if dark else ""
        S.back.append(f'<div id="{s}-t{k}" class="abs plate" style="{box(x, y, 270, 290)}{bg}">'
                      f'<div id="{s}-n{k}" class="abs" style="left:24px;top:22px;font:700 72px/1 Poppins;color:{"#00D0FE" if dark else "#fff"}">0{k + 1}</div>'
                      f'<div class="abs sub" style="left:24px;top:206px;font-size:30px;color:rgba(255,255,255,{0.25 if dark else 0.85})">{"???" if dark else STEPS[k]}</div>'
                      f'<div id="{s}-g{k}" class="abs" style="inset:0;border-radius:22px;box-shadow:inset 0 0 0 3px #00D0FE, 0 0 22px rgba(0,208,254,.45);opacity:0"></div></div>')
        ry = (col - 1) * -12
        pop(S, f"#{s}-t{k}", S.t0 + 0.2 + k * 0.065, 0.42, {"opacity": 0, "y": 80, "scaleY": 0.2, "rotationY": ry}, {"opacity": 1, "y": 0, "scaleY": 1, "rotationY": ry}, "power3.out")
        if k < 5:
            S.ft(f"#{s}-g{k}", {"opacity": 0}, {"opacity": 1}, W(21) + k * 0.065, 0.1, "none")
            S.ft(f"#{s}-g{k}", {"opacity": 1}, {"opacity": 0}, W(21) + k * 0.065 + 0.2, 0.3, "power2.out")
    S.ft(f"#{s}-g5", {"opacity": 0}, {"opacity": 1}, W(24), 0.12, "power2.out")
    S.ft(f"#{s}-g5", {"opacity": 1}, {"opacity": 0.45}, W(24) + 0.5, 0.6, "sine.inOut")
    S.ft(f"#{s}-n5", {"scale": 1}, {"scale": 1.15}, W(24), 0.16, "power2.out")
    S.ft(f"#{s}-n5", {"scale": 1.15}, {"scale": 1}, W(24) + 0.16, 0.3, "power2.inOut")
    S.fx(W(21), "pop", 0.05)
    S.fx(W(24), "ping", 0.07)
    S.cam([(S.t0, {"rotationY": 5, "z": 0}, None), (S.t1 - 0.4, {"rotationY": -5, "z": 40}, "sine.inOut")])
    heading(S, S.front, f"{s}-h", "*6* LANGKAH", 60, HEAD_Y, 960, 84, "center", keys=[W(20), W(21)])
    S.front.append(f'<div id="{s}-sub" class="abs sub" style="left:0;top:{HEAD_Y + 165}px;width:1080px;text-align:center;font-size:40px">yang <b class="cy">terakhir</b> paling sering dilewatkan</div>')
    pop(S, f"#{s}-sub", W(24) - 0.05, 0.35)
    narrator(S, dict(MASCOT_R, h=660, fx=930), rise=False)
    S.intent(W(24), "pointFwd", "left")
    # handoff: fly through checkpoint 01 (its border becomes the next frame)
    S.ft(f"#{s}-t0", {"scale": 1, "scaleY": 1, "x": 0, "y": 0, "rotationY": 12}, {"scale": 5.2, "scaleY": 5.2, "x": 360, "y": 300, "rotationY": 0}, S.t1 - 0.38, 0.38, "power3.in")
    for k in range(1, 6):
        S.ft(f"#{s}-t{k}", {"opacity": 1}, {"opacity": 0}, S.t1 - 0.36, 0.2, "power2.in")
    S.fx(S.t1 - 0.36, "whoosh", 0.06)


# ============================================================================== S04 STEP 1 DESKTOP -> CODE
def app_body(s, active=None):
    side = (f'<div class="abs" style="left:0;top:0;width:200px;height:100%;background:rgba(255,255,255,.04);border-right:1px solid rgba(255,255,255,.07)">'
            + "".join(f'<div id="{s}-tab{k}" class="abs sub" style="left:18px;top:{28 + k * 70}px;width:164px;height:54px;border-radius:12px;font-size:26px;line-height:54px;padding-left:18px;'
                      f'color:rgba(255,255,255,.85);background:rgba(255,255,255,{0.06 if k else 0.12})">{lab}</div>' for k, lab in enumerate(["Chat", "Code"]))
            + '</div>')
    return (side + f'<div class="abs sub" style="left:240px;top:120px;width:300px;font-size:30px;color:#fff;font-weight:700">Claude</div>'
            f'<div class="abs" style="left:240px;top:180px;width:330px;height:16px;border-radius:8px;background:rgba(255,255,255,.12)"></div>'
            f'<div class="abs" style="left:240px;top:210px;width:250px;height:16px;border-radius:8px;background:rgba(255,255,255,.08)"></div>'
            f'<div class="abs" style="left:240px;bottom:40px;width:340px;height:56px;border-radius:16px;border:1.5px solid rgba(255,255,255,.18)"></div>')


def s04(S):
    s, W = S.id, S.W
    hide_mascot(S)
    vframe(S.back, f"{s}-fr", (0, 0, 1080, 1920))
    vmove(S, f"{s}-fr", (0, 0, 1080, 1920), (194, 594, 692, 406), S.t0, 0.45, "power3.out", 40, 14)
    S.ft(f"#{s}-fr", {"opacity": 1}, {"opacity": 0}, S.t0 + 0.35, 0.2, "none")
    S.back.append(laptop(f"{s}-lap", 180, 580, 720, app_body(s)))
    S.init(f"#{s}-lap-lid", {"rotationX": -85})
    S.ft(f"#{s}-lap-lid", {"rotationX": -85}, {"rotationX": 0}, S.t0 + 0.1, 0.7, "power3.out")
    S.cam([(S.t0, {"z": -80, "rotationX": 6}, None), (S.t1 - 0.4, {"z": 70, "rotationX": 0, "x": 60, "y": 40}, "power2.inOut")])
    step_badge(S, S.front, f"{s}-b", 1, 60, HEAD_Y + 4, W(29))
    heading(S, S.front, f"{s}-h", "BUKA *CLAUDE* *CODE*", 180, HEAD_Y, 840, 66, "left", keys=[W(30), W(31), W(37)])
    # cursor travels to the Code tab and clicks on "Code."
    tab = (180 + 14 + 18 + 82, 580 + 14 + 28 + 70 + 27)
    cursor(S.back, f"{s}-cur", tab[0], tab[1], 60)
    S.keys(f"#{s}-cur", [(S.t0, {"x": 420, "y": 380, "opacity": 0}, None), (W(30), {"x": 420, "y": 380, "opacity": 1}, "power2.out"),
                         (W(37) - 0.1, {"x": 0, "y": 0}, "power3.inOut")])
    click(S, S.back, f"{s}-cur", tab[0], tab[1], W(37))
    sel = (tab[0] - 98, tab[1] - 34, 190, 66)
    vframe(S.back, f"{s}-sel", sel, 14)
    S.init(f"#{s}-sel", {"opacity": 0})
    S.ft(f"#{s}-sel", {"opacity": 0}, {"opacity": 1}, W(37) + 0.02, 0.1, "none")
    vmove(S, f"{s}-sel", (sel[0] - 30, sel[1] - 12, sel[2] + 60, sel[3] + 24), sel, W(37) + 0.02, 0.24, "power3.out", 14, 14)
    S.ft(f"#{s}-tab1", {"backgroundColor": "rgba(255,255,255,.06)"}, {"backgroundColor": "rgba(0,208,254,.22)"}, W(37) + 0.02, 0.2, "power2.out")
    # handoff: the selection border expands into the next scene's window frame
    vmove(S, f"{s}-sel", sel, (140, 560, 800, 820), S.t1 - 0.3, 0.3, "power3.in", 14, 40)


# ============================================================================== S05 STEP 2 CREATE FOLDER
def s05(S):
    s, W = S.id, S.W
    vframe(S.back, f"{s}-fr", (140, 560, 800, 820))
    vmove(S, f"{s}-fr", (140, 560, 800, 820), (190, 760, 520, 400), S.t0, 0.4, "power3.out", 40, 18)
    S.ft(f"#{s}-fr", {"opacity": 1}, {"opacity": 0}, S.t0 + 0.3, 0.2, "none")
    S.back.append(folder3d(f"{s}-fd", 190, 760, 520, 400))
    pop(S, f"#{s}-fd", S.t0 + 0.15, 0.5, {"opacity": 0, "y": 60, "rotationX": 30}, {"opacity": 1, "y": 0, "rotationX": 10}, "power3.out")
    S.ft(f"#{s}-fd-tab", {"x": -60}, {"x": 0}, S.t0 + 0.3, 0.4, "power3.out")
    S.back.append(f'<div id="{s}-np" class="abs plate plate-s mono" style="{box(250, 980, 400, 70)}font-size:32px;line-height:70px;text-align:center;color:#fff"></div>')
    pop(S, f"#{s}-np", W(41) - 0.1, 0.3)
    name = "VIDEO-ANIMASI"
    for k in range(1, len(name) + 1):
        at = W(42) + (W(45) - W(42)) * k / len(name)
        S.tset(f"#{s}-np", {"textContent": name[:k]}, at)
        if k % 3 == 0:
            S.fx(at, "key", 0.03)
    S.cam([(S.t0, {"z": 0}, None), (S.t1, {"z": 60}, "sine.inOut")])
    step_badge(S, S.front, f"{s}-b", 2, 60, HEAD_Y + 4, W(38))
    heading(S, S.front, f"{s}-h", "SATU *FOLDER* PROJECT", 180, HEAD_Y, 840, 66, "left", keys=[W(40), W(41), W(44)])
    narrator(S, dict(MASCOT_R, fx=860, h=800))
    S.intent(W(41), "point", "left")
    # tab reacts to the tap (the hand lands on the right of the folder at "folder")
    S.ft(f"#{s}-fd-tab", {"y": 0}, {"y": 6}, W(41) + 0.18, 0.08, "power2.in")
    S.ft(f"#{s}-fd-tab", {"y": 6}, {"y": 0}, W(41) + 0.26, 0.3, "back.out(2)")
    S.fx(W(41) + 0.2, "click", 0.06)
    # handoff: the front flap hinges open to reveal the inside
    S.ft(f"#{s}-fd-front", {"rotationX": 0}, {"rotationX": 72}, S.t1 - 0.45, 0.45, "power2.in")
    S.ft(f"#{s}-np", {"opacity": 1}, {"opacity": 0}, S.t1 - 0.45, 0.2, "none")


# ============================================================================== S06 WHY A FOLDER MATTERS
def s06(S):
    s, W = S.id, S.W
    hide_mascot(S)
    S.back.append(f'<div id="{s}-desk" class="abs metal" style="{box(90, 700, 900, 640)}border-radius:30px;filter:brightness(.8);border:1.5px solid rgba(0,208,254,.3)"></div>')
    pop(S, f"#{s}-desk", S.t0, 0.4, {"opacity": 0, "scaleY": 0.5, "rotationX": 40}, {"opacity": 1, "scaleY": 1, "rotationX": 0}, "power3.out")
    labs = [("ASET", "assets/", W(47)), ("SCENE", "scenes/", W(48)), ("RENDER", "out/", W(51))]
    for k, (lab, path, t) in enumerate(labs):
        x = 130 + k * 285
        S.back.append(f'<div id="{s}-bay{k}" class="abs plate plate-s" style="{box(x, 760, 250, 380)}background:linear-gradient(170deg,rgba(5,8,22,.7),rgba(20,40,75,.7))">'
                      f'<div class="abs sub" style="left:0;top:300px;width:250px;text-align:center;font-size:32px;color:#fff">{lab}</div>'
                      f'<div class="abs sub mono" style="left:0;top:340px;width:250px;text-align:center;font-size:22px;color:rgba(255,255,255,.55)">{path}</div></div>')
        pop(S, f"#{s}-bay{k}", S.t0 + 0.2 + k * 0.08, 0.35)
        # a messy card flies into its own bay on the word
        S.back.append(f'<div id="{s}-cd{k}" class="abs plate plate-s" style="{box(x + 35, 800, 180, 230)}border-color:rgba(0,208,254,.7)">'
                      f'<div class="abs" style="left:20px;top:24px;width:140px;height:90px;border-radius:10px;background:linear-gradient(160deg,#3e7fc4,#132a52)"></div>'
                      + "".join(f'<div class="abs" style="left:20px;top:{136 + j * 26}px;width:{130 - j * 40}px;height:10px;border-radius:5px;background:rgba(255,255,255,.3)"></div>' for j in range(3))
                      + '</div>')
        mess = {"x": [180, -300, -40][k], "y": [-230, -120, 280][k], "rotation": [-28, 22, -14][k], "opacity": 1}
        S.init(f"#{s}-cd{k}", dict(mess, opacity=0))
        S.ft(f"#{s}-cd{k}", dict(mess, opacity=0), mess, S.t0 + 0.3, 0.3, "power2.out")
        S.ft(f"#{s}-cd{k}", mess, {"x": 0, "y": 0, "rotation": 0, "opacity": 1}, t - 0.05, 0.4, "back.out(1.4)")
        S.fx(t + 0.3, "click", 0.05)
        S.back.append(f'<div id="{s}-ptr{k}" class="abs line-cy" style="{box(x + 95, 1150, 60, 6)}"></div>')
        pop(S, f"#{s}-ptr{k}", t + 0.3, 0.2, {"opacity": 0, "scaleX": 0}, {"opacity": 1, "scaleX": 1}, "power2.out")
    heading(S, S.front, f"{s}-h", "NGGAK *BERANTAKAN*", 60, HEAD_Y, 960, 70, "center", keys=[W(52), W(53)])
    # handoff: the SCENE card slides forward and grows into the app window of S07
    S.ft(f"#{s}-cd1", {"x": 0, "y": 0, "scaleX": 1, "scaleY": 1, "transformOrigin": "0% 0%"},
         {"x": 120 - 450, "y": 560 - 800, "scaleX": 840 / 180, "scaleY": 760 / 230, "transformOrigin": "0% 0%"}, S.t1 - 0.32, 0.32, "power3.in")


# ============================================================================== S07 STEP 3 LOCAL SESSION
def s07(S):
    s, W = S.id, S.W
    hide_mascot(S)
    rows = (f'<div id="{s}-new" class="abs plate plate-s" style="{box(40, 40, 360, 80)}font:700 32px/80px Poppins;text-align:center;color:#fff">+ Sesi baru</div>'
            f'<div id="{s}-loc" class="abs plate plate-s" style="{box(430, 40, 330, 80)}font:400 30px/80px Poppins;text-align:center;color:#fff;opacity:.6">Lokal</div>'
            f'<div class="abs sub" style="left:40px;top:160px;font-size:26px;color:rgba(255,255,255,.55)">Pilih folder</div>'
            + "".join(f'<div id="{s}-f{k}" class="abs plate plate-s" style="{box(40, 210 + k * 96, 720, 80)}font:400 30px/80px Poppins;padding-left:30px;color:{"#fff" if k == 1 else "rgba(255,255,255,.55)"}">'
                      f'{nm}</div>' for k, nm in enumerate(["Documents", "VIDEO-ANIMASI", "Downloads"])))
    S.back.append(appwin(f"{s}-win", 120, 560, 840, 760, "Claude  ·  Code", rows))
    pop(S, f"#{s}-win", S.t0, 0.3, {"opacity": 0.6, "scale": 0.98}, {"opacity": 1, "scale": 1}, "power2.out")
    cursor(S.back, f"{s}-cur", 0, 0, 60)
    pts = [(120 + 220, 560 + 58 + 80, W(55)), (120 + 595, 560 + 58 + 80, W(57)), (120 + 400, 560 + 58 + 210 + 96 + 40, W(60))]
    keys = [(S.t0, {"x": 700, "y": 1500, "opacity": 0}, None), (S.t0 + 0.25, {"opacity": 1}, "power2.out")]
    for (x, y, t) in pts:
        keys.append((t - 0.08, {"x": x, "y": y}, "power3.inOut"))
        keys.append((t + 0.25, {"x": x, "y": y}, "none"))
    S.keys(f"#{s}-cur", keys)
    for k, (x, y, t) in enumerate(pts):
        S.back.append(f'<div id="{s}-c{k}rg" class="abs ringfx" style="{box(x - 40, y - 40, 80, 80)}"></div>')
        S.init(f"#{s}-c{k}rg", {"opacity": 0, "scale": 0.3})
        S.ft(f"#{s}-c{k}rg", {"opacity": 0.95, "scale": 0.3}, {"opacity": 0, "scale": 1.9}, t, 0.45, "power3.out")
        S.fx(t, "click", 0.08)
    S.ft(f"#{s}-new", {"borderColor": "rgba(0,208,254,.4)"}, {"borderColor": "rgba(0,208,254,1)"}, W(55), 0.2, "power2.out")
    S.ft(f"#{s}-loc", {"opacity": 0.6, "borderColor": "rgba(0,208,254,.4)"}, {"opacity": 1, "borderColor": "rgba(0,208,254,1)"}, W(57), 0.2, "power2.out")
    S.ft(f"#{s}-f1", {"borderColor": "rgba(0,208,254,.4)", "scale": 1}, {"borderColor": "rgba(0,208,254,1)", "scale": 1.03}, W(60), 0.25, "back.out(2)")
    step_badge(S, S.front, f"{s}-b", 3, 60, HEAD_Y + 4, W(54))
    heading(S, S.front, f"{s}-h", "SESI *LOKAL* + FOLDER", 180, HEAD_Y, 840, 66, "left", keys=[W(56), W(57), W(59), W(60)])
    # handoff: a wire draws out of the selected folder down to the file tree
    S.back.append(f'<div id="{s}-wire" class="abs line-cy" style="{box(518, 1010, 6, 420)}transform-origin:50% 0"></div>')
    S.init(f"#{s}-wire", {"scaleY": 0})
    S.ft(f"#{s}-wire", {"scaleY": 0}, {"scaleY": 1}, S.t1 - 0.3, 0.3, "power2.in")


# ============================================================================== S08 PROJECT ACCESS
def s08(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-wire" class="abs line-cy" style="{box(518, 600, 6, 230)}"></div>')
    root = (220, 840)
    S.back.append(f'<div id="{s}-tree" class="abs p3" style="{box(0, 0, 1080, 1920)}transform:rotateY(-15deg);transform-origin:300px 1000px">'
                  f'<div id="{s}-root" class="abs plate" style="{box(root[0], root[1], 400, 110)}font:700 34px/110px Poppins;padding-left:30px;color:#fff">VIDEO-ANIMASI</div>'
                  + "".join(f'<div id="{s}-k{k}" class="abs plate plate-s mono" style="{box(420, 1010 + k * 130, 380, 92)}font-size:30px;line-height:92px;padding-left:30px;color:#fff">{nm}</div>'
                            f'<div id="{s}-ln{k}" class="abs" style="{box(300, 965, 8, 92 + k * 130)}background:rgba(255,255,255,.18);border-radius:4px"></div>'
                            f'<div id="{s}-lh{k}" class="abs" style="{box(300, 1053 + k * 130, 120, 8)}background:rgba(255,255,255,.18);border-radius:4px"></div>'
                            for k, nm in enumerate(["assets/", "scenes/", "out/"]))
                  + '</div>')
    pop(S, f"#{s}-root", S.t0 + 0.05, 0.35)
    for k, t in enumerate([W(63), W(65), W(67)]):
        pop(S, f"#{s}-k{k}", S.t0 + 0.15 + k * 0.08, 0.35)
        S.ft(f"#{s}-lh{k}", {"backgroundColor": "rgba(255,255,255,.18)", "boxShadow": "0 0 0 rgba(0,0,0,0)"}, {"backgroundColor": CY, "boxShadow": "0 0 12px rgba(0,208,254,.6)"}, t, 0.2, "power2.out")
        S.ft(f"#{s}-ln{k}", {"backgroundColor": "rgba(255,255,255,.18)"}, {"backgroundColor": CY}, t, 0.2, "power2.out")
        S.ft(f"#{s}-k{k}", {"borderColor": "rgba(0,208,254,.4)"}, {"borderColor": "rgba(0,208,254,1)"}, t, 0.2, "power2.out")
        S.fx(t, "ping", 0.04)
    S.cam([(S.t0, {"x": 30}, None), (S.t1, {"x": -40}, "sine.inOut")])
    heading(S, S.front, f"{s}-h", "PROJECT *TERHUBUNG*", 60, HEAD_Y, 960, 70, "center", keys=[W(65), W(67)])
    narrator(S, dict(MASCOT_R, fx=940, h=640))
    S.intent(W(63), "present", "left")
    # handoff: the signal travels down into a progress line under the tool row
    S.back.append(f'<div id="{s}-sig" class="abs line-cy" style="{box(120, 1430, 840, 6)}transform-origin:0 50%"></div>')
    S.init(f"#{s}-sig", {"scaleX": 0})
    S.ft(f"#{s}-sig", {"scaleX": 0}, {"scaleX": 1}, S.t1 - 0.35, 0.35, "power2.in")


# ============================================================================== S09 STEP 4 PRE-FLIGHT
def s09(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-sig" class="abs line-cy" style="{box(120, 1430, 840, 6)}"></div>')
    S.back.append(f'<div class="abs grid-fine" style="{box(40, 1150, 1000, 320)}transform:rotateX(66deg)"></div>')
    mods = [("RENDER", "HyperFrames", W(75)), ("FONT", "Poppins", W(76)), ("AUDIO", "VO .mp3", W(77))]
    for k, (lab, val, t) in enumerate(mods):
        x = 80 + k * 315
        S.back.append(f'<div id="{s}-m{k}" class="abs p3" style="{box(x, 760, 290, 420)}">'
                      f'<div class="abs cshadow" style="{box(-20, 380, 330, 80)}"></div>'
                      f'<div class="abs metal" style="{box(0, 0, 290, 380)}border-radius:26px;border:1.5px solid rgba(0,208,254,.35)"></div>'
                      f'<div id="{s}-led{k}" class="abs led" style="left:30px;top:30px;width:34px;height:34px"></div>'
                      f'<div class="abs" style="left:0;top:150px;width:290px;text-align:center;font:700 40px/1 Poppins;color:#fff">{lab}</div>'
                      f'<div class="abs sub" style="left:0;top:210px;width:290px;text-align:center;font-size:26px;color:rgba(255,255,255,.7)">{val}</div>'
                      f'<div id="{s}-ok{k}" class="abs" style="left:111px;top:270px;width:68px;height:68px">{check_svg(f"{s}-ck{k}", CY, 3.4)}</div></div>')
        pop(S, f"#{s}-m{k}", S.t0 + 0.2 + k * 0.1, 0.45, {"opacity": 0, "y": 80, "rotationX": 40}, {"opacity": 1, "y": 0, "rotationX": 8}, "power3.out")
        S.ft(f"#{s}-led{k}", {"backgroundColor": "#3b4a66", "boxShadow": "0 0 0 rgba(0,0,0,0)"}, {"backgroundColor": CY, "boxShadow": "0 0 14px rgba(0,208,254,.7)"}, t, 0.2, "power2.out")
        S.init(f"#{s}-ck{k}", {"strokeDashoffset": 1})
        S.ft(f"#{s}-ck{k}", {"strokeDashoffset": 1}, {"strokeDashoffset": 0}, t + 0.05, 0.3, "power2.out")
        S.fx(t, "ping", 0.05)
    S.cam([(S.t0, {"x": 40, "rotationY": -3}, None), (S.t1, {"x": -30, "rotationY": 3}, "sine.inOut")])
    step_badge(S, S.front, f"{s}-b", 4, 60, HEAD_Y + 4, W(69))
    heading(S, S.front, f"{s}-h", "CEK *SEBELUM* MULAI", 180, HEAD_Y, 840, 66, "left", keys=[W(70), W(72), W(73)])
    narrator(S, dict(MASCOT_R, fx=900, h=700))
    S.intent(W(70), "thinking", "left")
    # handoff: the tool bay slides aside, revealing the character turntable
    for k in range(3):
        S.ft(f"#{s}-m{k}", {"x": 0, "opacity": 1}, {"x": -1100, "opacity": 1}, S.t1 - 0.36, 0.36, "power3.in")


# ============================================================================== S10 CHARACTER READINESS
def s10(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-tt" class="abs" style="{box(190, 1470, 700, 150)}border-radius:50%;background:radial-gradient(ellipse,rgba(41,75,119,.9),rgba(10,13,44,.95));'
                  f'border:2px solid rgba(0,208,254,.55);box-shadow:0 0 30px rgba(0,208,254,.25)"></div>')
    S.back.append(f'<div id="{s}-gr" class="abs grid-fine" style="{box(140, 1380, 800, 300)}transform:rotateX(72deg);opacity:.9"></div>')
    pop(S, f"#{s}-tt", S.t0, 0.4, {"opacity": 0, "scaleX": 0.4}, {"opacity": 1, "scaleX": 1}, "power3.out")
    V = {"fx": 540, "fy": 1560, "h": 1050, "yaw": 0, "pitch": 4}
    S.mv([(S.t0, dict(V, fx=1500, vis=1), None), (S.t0 + 0.45, dict(V), "power3.out"),
          (W(80), dict(V, yaw=18), "sine.inOut"), (W(82), dict(V, yaw=-14), "sine.inOut"), (W(86), dict(V, yaw=0), "sine.inOut")])
    chips = [("RIG 19 SENDI", W(79), 30, 720), ("TEKSTUR JAS", W(81), 750, 760), ("SHADOW", W(81) + 0.3, 30, 1100)]
    for k, (lab, t, x, y) in enumerate(chips):
        S.front.append(f'<div id="{s}-c{k}" class="abs plate plate-s" style="{box(x, y, 300, 82)}">'
                       f'<div id="{s}-cd{k}" class="abs led" style="left:22px;top:26px;width:30px;height:30px"></div>'
                       f'<div class="abs sub" style="left:68px;top:20px;font-size:28px;color:#fff;white-space:nowrap">{lab}</div></div>')
        pop(S, f"#{s}-c{k}", t, 0.32)
        S.ft(f"#{s}-cd{k}", {"backgroundColor": "#3b4a66"}, {"backgroundColor": CY}, t + 0.25, 0.2, "power2.out")
    # "error" -> amber warning on the jacket chip, "beresin" -> fixed
    S.front.append(f'<div id="{s}-err" class="abs plate plate-s" style="{box(720, 1120, 330, 82)}border-color:rgba(255,190,90,.9);font:700 30px/82px Poppins;text-align:center;color:#ffc46b">PERLU DIRAPIKAN</div>')
    pop(S, f"#{s}-err", W(85), 0.25)
    S.ft(f"#{s}-err", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.9}, W(87), 0.25, "power2.in")
    S.front.append(f'<div id="{s}-fix" class="abs plate plate-s" style="{box(720, 1120, 330, 82)}font:700 30px/82px Poppins;text-align:center;color:#00D0FE">BERES</div>')
    pop(S, f"#{s}-fix", W(87) + 0.15, 0.3)
    S.fx(W(85), "pop", 0.05)
    S.fx(W(87) + 0.15, "ping", 0.06)
    heading(S, S.front, f"{s}-h", "KARAKTER *3D* SIAP?", 60, HEAD_Y, 960, 70, "center", keys=[W(79), W(80), W(81)])
    S.intent(W(85), "emphasize", "right")
    # handoff: the turntable grid compresses into the prompt caret
    S.ft(f"#{s}-tt", {"scaleX": 1, "opacity": 1}, {"scaleX": 0.006, "opacity": 1}, S.t1 - 0.3, 0.3, "power3.in")
    S.ft(f"#{s}-gr", {"opacity": 0.9}, {"opacity": 0}, S.t1 - 0.3, 0.2, "none")
    S.mv([(S.t1 - 0.3, dict(V), None), (S.t1, dict(V, fy=2900), "power3.in")])


# ============================================================================== S11 + S12 STEP 5 TYPE THE IDEA -> STORYBOARD
CON = (110, 720, 860, 420)
IDEA = "Bikin animasi 3D tentang cara membuat Reels dengan AI."


def console(s):
    x, y, w, h = CON
    return (f'<div id="{s}-con" class="abs glassd" style="{box(x, y, w, h)}border-radius:28px">'
            f'<div class="abs sub" style="left:36px;top:26px;font-size:24px;color:rgba(255,255,255,.55)">Claude Code</div>'
            f'<div class="abs mono" style="left:36px;top:96px;font-size:40px;color:#00D0FE">&gt;</div>'
            f'<div id="{s}-tx" class="abs mono" style="left:84px;top:96px;width:{w - 130}px;font-size:36px;line-height:1.4;color:#fff"></div>'
            f'<div id="{s}-car" class="abs" style="left:84px;top:100px;width:4px;height:48px;background:#00D0FE"></div></div>')


def s11(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-seed" class="abs" style="{box(536, 1540, 8, 50)}background:#00D0FE"></div>')
    S.ft(f"#{s}-seed", {"opacity": 1, "x": 0, "y": 0}, {"opacity": 0, "x": -452, "y": -820}, S.t0, 0.32, "power3.out")
    S.back.append(console(s))
    pop(S, f"#{s}-con", S.t0 + 0.12, 0.4, {"opacity": 0, "scale": 0.9, "rotationX": 25}, {"opacity": 1, "scale": 1, "rotationX": 0}, "power3.out")
    for k in range(5):
        S.tset(f"#{s}-car", {"opacity": 1 if k % 2 == 0 else 0}, S.t0 + 0.5 + k * 0.4)
    step_badge(S, S.front, f"{s}-b", 5, 60, HEAD_Y + 4, W(89))
    heading(S, S.front, f"{s}-h", "TULIS *IDEMU*", 180, HEAD_Y, 840, 72, "left", keys=[W(90), W(91)])
    apex(S, S.front, f"{s}-ap", 540, CON[1] + 120, W(91) + 0.05, 420, ring=False, sparks=0, op=0.3)
    narrator(S, dict(MASCOT_L, fx=230, h=760))
    S.intent(W(90), "explain", "right")


def s12(S):
    s, W = S.id, S.W
    S.back.append(console(s))
    t0, t1 = W(93), W(102) + 0.25
    S.init(f"#{s}-tx", {"textContent": ""})
    n = len(IDEA)
    for k in range(1, n + 1):
        at = t0 + (t1 - t0) * k / n
        S.tset(f"#{s}-tx", {"textContent": IDEA[:k]}, at)
        if k % 3 == 0:
            S.fx(at, "key", 0.03)
    S.tset(f"#{s}-car", {"opacity": 0}, t0)
    # "Tapi jangan berhenti di satu kalimat": the sentence breaks into five storyboard cards along a timeline
    brk = W(104)
    S.ft(f"#{s}-con", {"y": 0, "scale": 1}, {"y": -150, "scale": 0.82}, brk, 0.5, "power3.inOut")
    cards = ["HOOK", "STUDIO", "KAMERA", "TRANSISI", "ENDING"]
    S.back.append(f'<div id="{s}-tl" class="abs" style="{box(70, 1390, 940, 6)}border-radius:3px;background:rgba(255,255,255,.25);transform-origin:0 50%"></div>')
    S.init(f"#{s}-tl", {"scaleX": 0})
    S.ft(f"#{s}-tl", {"scaleX": 0}, {"scaleX": 1}, brk + 0.1, 0.6, "power2.out")
    for k, lab in enumerate(cards):
        x = 70 + k * 190
        S.back.append(f'<div id="{s}-cd{k}" class="abs plate plate-s" style="{box(x, 1060, 172, 300)}">'
                      f'<div class="abs" style="left:14px;top:14px;width:144px;height:150px;border-radius:12px;background:linear-gradient(160deg,{["#3e7fc4,#132a52", "#294B77,#0A0D2C", "#00D0FE,#163a6c", "#5f8fd0,#1b2f55", "#9cc7ee,#294B77"][k]})"></div>'
                      f'<div class="abs" style="left:0;top:190px;width:172px;text-align:center;font:700 24px/1 Poppins;color:#fff">{lab}</div>'
                      f'<div class="abs" style="left:0;top:240px;width:172px;text-align:center;font:700 34px/1 Poppins;color:#00D0FE">{k + 1}</div></div>')
        pop(S, f"#{s}-cd{k}", brk + 0.15 + k * 0.12, 0.45, {"opacity": 0, "y": -260, "x": 450 - x, "scale": 0.4, "rotationY": 70},
            {"opacity": 1, "y": 0, "x": 0, "scale": 1, "rotationY": 0}, "back.out(1.3)")
        S.fx(brk + 0.2 + k * 0.12, "pop", 0.04)
    heading(S, S.front, f"{s}-h", "IDE JADI *STORYBOARD*", 60, HEAD_Y, 960, 70, "center", keys=[W(104), W(105), W(108)])
    S.cam([(S.t0, {"z": 60}, None), (brk, {"z": 60}, None), (S.t1, {"z": -40}, "power2.inOut")])
    narrator(S, dict(MASCOT_L, fx=230, h=760), rise=False)
    S.mv([(brk - 0.2, dict(MASCOT_L, fx=230, h=760), None), (brk + 0.4, dict(MASCOT_L, fx=230, fy=2700, h=760), "power2.in")])
    S.intent(W(103), "emphasize", "right")
    # handoff: the first card's edge wipes the frame
    S.back.append(f'<div id="{s}-wipe" class="abs plate" style="{box(-1100, 0, 1100, 1920)}border-radius:0"></div>')
    S.ft(f"#{s}-wipe", {"x": 0}, {"x": 1100}, S.t1 - 0.28, 0.28, "power3.in")


# ============================================================================== S13 CAMERA + TRANSITIONS
def s13(S):
    s, W = S.id, S.W
    hide_mascot(S)
    S.back.append(f'<div id="{s}-wipe" class="abs plate" style="{box(0, 0, 1100, 1920)}border-radius:0"></div>')
    S.ft(f"#{s}-wipe", {"x": 0}, {"x": 1120}, S.t0, 0.3, "power3.out")
    for k in range(5):
        x, z = 70 + k * 190, -k * 40
        S.back.append(f'<div id="{s}-set{k}" class="abs plate plate-s" style="{box(x, 900, 172, 220)}">'
                      f'<div class="abs" style="left:14px;top:14px;width:144px;height:120px;border-radius:12px;background:linear-gradient(160deg,#3e7fc4,#0A0D2C)"></div></div>')
        pop(S, f"#{s}-set{k}", S.t0 + 0.15 + k * 0.06, 0.35, {"opacity": 0, "y": 24, "z": z, "rotationY": -18}, {"opacity": 1, "y": 0, "z": z, "rotationY": -18})
    # camera crane path: a dashed arc + a camera body travelling along it
    S.back.append('<svg id="%s-arc" class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  '<path id="%s-path" d="M110 860 C 330 640, 750 640, 970 860" fill="none" stroke="#00D0FE" stroke-width="5" stroke-dasharray="14 12" pathLength="1"/></svg>' % (s, s))
    S.back.append(f'<div id="{s}-camb" class="abs p3" style="{box(70, 790, 90, 70)}">'
                  f'<div class="abs metal" style="{box(0, 0, 90, 62)}border-radius:14px;border:1.5px solid rgba(0,208,254,.6)"></div>'
                  f'<div class="abs" style="left:66px;top:14px;width:40px;height:34px;border-radius:8px;background:#0A0D2C;border:2px solid #00D0FE"></div></div>')
    pts = [(0, 0), (240, -150), (440, -205), (640, -150), (860, 0)]
    keys = [(S.t0 + 0.2, {"x": 0, "y": 0}, None)]
    marks = [W(110), W(112), W(114), W(116), W(119)]
    for (dx, dy), t in zip(pts, marks):
        keys.append((t, {"x": dx, "y": dy}, "power2.inOut"))
    S.keys(f"#{s}-camb", keys)
    S.fx(W(112), "whoosh", 0.05)
    # the four asks light up exactly when spoken
    labs = [("STORYBOARD", W(110)), ("KAMERA", W(112)), ("VOICE-OVER", W(114)), ("TRANSISI", W(116))]
    for k, (lab, t) in enumerate(labs):
        x = 60 + (k % 2) * 490
        y = 1200 + (k // 2) * 120
        S.back.append(f'<div id="{s}-ch{k}" class="abs chip plate plate-s" style="{box(x, y, 470, 96)}font-size:36px">{lab}</div>')
        pop(S, f"#{s}-ch{k}", S.t0 + 0.3 + k * 0.06, 0.3, {"opacity": 0, "y": 20}, {"opacity": 0.5, "y": 0})
        S.ft(f"#{s}-ch{k}", {"opacity": 0.5, "color": "#ffffff", "borderColor": "rgba(0,208,254,.4)"}, {"opacity": 1, "color": CY, "borderColor": "rgba(0,208,254,1)"}, t - 0.03, 0.2, "power2.out")
        if k < 3:
            S.ft(f"#{s}-ch{k}", {"color": CY}, {"color": "#ffffff"}, labs[k + 1][1] - 0.03, 0.2, "power2.out")
        S.fx(t, "pop", 0.04)
    heading(S, S.front, f"{s}-h", "MINTA YANG *NYAMBUNG*", 60, HEAD_Y, 960, 68, "center", keys=[W(109), W(117), W(118)])
    S.cam([(S.t0, {"x": 40}, None), (S.t1, {"x": -40}, "sine.inOut")])
    # handoff: the camera arc collapses into an audio waveform line
    S.ft(f"#{s}-arc", {"scaleY": 1, "opacity": 1}, {"scaleY": 0.05, "opacity": 1}, S.t1 - 0.36, 0.36, "power3.in")


# ============================================================================== S14 STEP 6 THE INTERRUPT
def s14(S):
    s, W = S.id, S.W
    bars = []
    for k in range(40):
        hgt = 20 + 90 * abs(((k * 37) % 23) / 23 - 0.5) * 2
        bars.append(f'<div id="{s}-wv{k}" class="abs" style="{box(90 + k * 23, 1240 - hgt / 2, 12, hgt)}border-radius:6px;background:#00D0FE;opacity:.8"></div>')
    S.back.append(f'<div id="{s}-wave" class="abs" style="{box(0, 0, 1080, 1920)}">{"".join(bars)}</div>')
    S.init(f"#{s}-wave", {"scaleY": 0.05})
    S.ft(f"#{s}-wave", {"scaleY": 0.05}, {"scaleY": 1}, S.t0, 0.3, "power3.out")
    # "Nah," -> the soundtrack dips (wave flattens) before the big 06
    S.ft(f"#{s}-wave", {"scaleY": 1}, {"scaleY": 0.25}, W(120), 0.2, "power2.out")
    S.back.append(f'<div id="{s}-tline" class="abs plate plate-s" style="{box(70, 1180, 940, 130)}"></div>')
    pop(S, f"#{s}-tline", W(120) + 0.1, 0.3, {"opacity": 0}, {"opacity": 1})
    for k in range(6):
        S.back.append(f'<div class="abs" style="{box(100 + k * 150, 1205, 130, 80)}border-radius:10px;background:linear-gradient(160deg,#3e7fc4,#0A0D2C);opacity:.85"></div>')
    S.back.append(f'<div id="{s}-ph" class="abs line-cy" style="{box(110, 1150, 6, 190)}"></div>')
    S.ft(f"#{s}-ph", {"x": 0}, {"x": 420}, W(121), W(128) - W(121), "none")
    S.back.append(f'<div id="{s}-mk" class="abs" style="{box(520, 1130, 26, 26)}transform:rotate(45deg);background:#00D0FE"></div>')
    pop(S, f"#{s}-mk", W(121) + 0.06, 0.2, {"opacity": 0, "y": -40}, {"opacity": 1, "y": 0}, "power3.out")
    S.fx(W(121) + 0.06, "click", 0.06)
    # the dark checkpoint 06 slides out, controlled punch-in on "keenam" (brightest apex)
    S.back.append(f'<div id="{s}-six" class="abs plate" style="{box(330, 520, 420, 440)}background:linear-gradient(150deg,#0b1024,#05070f);border:3px solid #00D0FE">'
                  f'<div class="abs" style="left:0;top:90px;width:420px;text-align:center;font:700 220px/1 Poppins;color:#00D0FE">06</div></div>')
    pop(S, f"#{s}-six", W(122) - 0.16, 0.42, {"opacity": 0, "x": 500, "rotationY": -60, "scale": 0.8}, {"opacity": 1, "x": 0, "rotationY": 0, "scale": 1}, "power3.out")
    S.cam([(S.t0, {"z": 0}, None), (W(122) - 0.02, {"z": 0}, None), (W(122) + 0.14, {"z": 120}, "power3.out"), (W(126), {"z": 40}, "power2.inOut")])
    apex(S, S.back, f"{s}-ap", 540, 740, W(122) + 0.1, 700, ring=True, sparks=6, op=0.55)
    S.fx(W(122), "sparkle", 0.07)
    heading(S, S.front, f"{s}-h", "*REVISI* SEPERTI EDITOR", 60, HEAD_Y, 960, 66, "center", keys=[W(128), W(129), W(130)])
    narrator(S, dict(MASCOT_R, fx=880, h=760))
    S.intent(W(126), "thinking", "left")
    # handoff: the playhead rule fills the frame (matte wipe into the diagnosis close-up)
    S.ft(f"#{s}-ph", {"scaleX": 1, "transformOrigin": "50% 50%"}, {"scaleX": 200}, S.t1 - 0.26, 0.26, "power3.in")


# ============================================================================== S15 DIAGNOSIS (real before/after)
def s15(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-mat" class="abs" style="{box(0, 0, 1080, 1920)}background:#00D0FE"></div>')
    S.ft(f"#{s}-mat", {"opacity": 1}, {"opacity": 0}, S.t0, 0.3, "power2.out")
    # REAL evidence: the same jacket crop before / after the texture repair (qa_suit_zoom.jpg vs qa_suit_zoom_clean3.jpg)
    S.back.append(f'<div id="{s}-win" class="abs plate" style="{box(90, 560, 900, 760)}overflow:hidden;padding:0">'
                  f'<div class="abs" style="{box(0, 0, 900, 760)}background:url(assets/qa/suit_after.jpg) center/cover"></div>'
                  f'<div id="{s}-bef" class="abs" style="{box(0, 0, 900, 760)}background:url(assets/qa/suit_before.jpg) center/cover;clip-path:inset(0 0 0 0)"></div>'
                  f'<div id="{s}-sl" class="abs" style="{box(447, 0, 6, 760)}background:#00D0FE"></div>'
                  f'<div class="abs sub" style="left:24px;top:20px;font-size:26px;font-weight:700">SEBELUM</div>'
                  f'<div class="abs sub cy" style="left:720px;top:20px;font-size:26px;font-weight:700">SESUDAH</div></div>')
    pop(S, f"#{s}-win", S.t0 + 0.08, 0.4)
    # slider physically scrubbed across on "jasnya tembus"
    S.init(f"#{s}-bef", {"clipPath": "inset(0px 0px 0px 0px)"})
    S.ft(f"#{s}-bef", {"clipPath": "inset(0px 0px 0px 0px)"}, {"clipPath": "inset(0px 450px 0px 0px)"}, W(136), 0.8, "power2.inOut")
    S.ft(f"#{s}-sl", {"x": 450}, {"x": 0}, W(136), 0.8, "power2.inOut")
    S.init(f"#{s}-sl", {"x": 450})
    chips = [("KAKU?", W(135), 90), ("JAS TEMBUS?", W(137), 330), ("TRANSISI MURAHAN?", W(141), 640)]
    for k, (lab, t, x) in enumerate(chips):
        w = [200, 270, 360][k]
        S.front.append(f'<div id="{s}-c{k}" class="abs chip plate plate-s" style="{box(x if k < 2 else 620, 1350, w, 90)}font-weight:700;font-size:30px;color:#fff">{lab}</div>')
        pop(S, f"#{s}-c{k}", t, 0.3)
        S.fx(t, "pop", 0.05)
    heading(S, S.front, f"{s}-h", "CARI YANG *MASIH* SALAH", 60, HEAD_Y, 960, 66, "center", keys=[W(132), W(133), W(134), W(135)])
    narrator(S, dict(MASCOT_R, fx=900, h=640), rise=True)
    S.intent(W(136), "point", "left")
    # handoff: the slider bar sweeps across the whole screen into the QA desk
    S.front.append(f'<div id="{s}-sw" class="abs line-cy" style="{box(-20, 0, 14, 1920)}"></div>')
    S.init(f"#{s}-sw", {"x": 0, "opacity": 0})
    S.ft(f"#{s}-sw", {"x": 0, "opacity": 1}, {"x": 1110, "opacity": 1}, S.t1 - 0.37, 0.37, "power3.in")


# ============================================================================== S16 FEEDBACK LOOP
def s16(S):
    s, W = S.id, S.W
    hide_mascot(S)
    S.back.append(f'<div id="{s}-sw" class="abs line-cy" style="{box(1060, 0, 14, 1920)}"></div>')
    S.ft(f"#{s}-sw", {"opacity": 1}, {"opacity": 0}, S.t0 + 0.1, 0.2, "none")
    notes = [("rapikan lapel jas", W(142)), ("perbaiki pose tangan", W(144)), ("kurangi blur transisi", W(146))]
    for k, (nt, t) in enumerate(notes):
        y = 600 + k * 150
        S.back.append(f'<div id="{s}-n{k}" class="abs plate plate-s" style="{box(110, y, 860, 120)}">'
                      f'<div class="abs mono" style="left:30px;top:36px;font-size:34px;color:#00D0FE">&gt;</div>'
                      f'<div class="abs sub" style="left:80px;top:32px;font-size:38px;color:#fff">{nt}</div>'
                      f'<div id="{s}-ok{k}" class="abs" style="left:770px;top:30px;width:60px;height:60px">{check_svg(f"{s}-ck{k}", CY, 3.4)}</div></div>')
        pop(S, f"#{s}-n{k}", t - 0.06, 0.36, {"opacity": 0, "x": -60}, {"opacity": 1, "x": 0}, "power3.out")
        S.fx(t, "key", 0.04)
        ck = W(147) + 0.25 + k * 0.35 if k < 2 else W(150)
        S.init(f"#{s}-ck{k}", {"strokeDashoffset": 1})
        S.ft(f"#{s}-ck{k}", {"strokeDashoffset": 1}, {"strokeDashoffset": 0}, ck, 0.3, "power2.out")
        S.fx(ck, "ping", 0.04)
    flow = ["FEEDBACK", "PREVIEW", "FIX"]
    for k, lab in enumerate(flow):
        S.back.append(f'<div id="{s}-f{k}" class="abs chip plate plate-s" style="{box(80 + k * 320, 1150, 280, 96)}font-weight:700;font-size:32px">{lab}</div>')
        t = [W(142), W(147), W(150)][k]
        pop(S, f"#{s}-f{k}", t, 0.32)
        S.ft(f"#{s}-f{k}", {"color": "#ffffff", "borderColor": "rgba(0,208,254,.4)"}, {"color": CY, "borderColor": "rgba(0,208,254,1)"}, t + 0.1, 0.2, "power2.out")
        if k < 2:
            S.back.append(f'<div id="{s}-ar{k}" class="abs line-cy" style="{box(360 + k * 320, 1196, 40, 5)}transform-origin:0 50%"></div>')
            S.init(f"#{s}-ar{k}", {"scaleX": 0})
            S.ft(f"#{s}-ar{k}", {"scaleX": 0}, {"scaleX": 1}, [W(147), W(150)][k] - 0.1, 0.2, "power2.out")
    heading(S, S.front, f"{s}-h", "KOREKSI YANG *SPESIFIK*", 60, HEAD_Y, 960, 66, "center", keys=[W(143), W(144), W(146)])
    # handoff: the corrected clip snaps into the timeline that becomes the final player
    S.back.append(f'<div id="{s}-clip" class="abs" style="{box(440, 1300, 200, 110)}border-radius:12px;background:linear-gradient(160deg,#3e7fc4,#0A0D2C);border:2px solid #00D0FE"></div>')
    S.init(f"#{s}-clip", {"opacity": 0})
    S.ft(f"#{s}-clip", {"opacity": 1, "x": 0, "y": 0, "scaleX": 1, "scaleY": 1, "transformOrigin": "0% 0%"},
         {"opacity": 1, "x": 110 - 440, "y": 600 - 1300, "scaleX": 860 / 200, "scaleY": 484 / 110, "transformOrigin": "0% 0%"}, S.t1 - 0.32, 0.32, "power3.in")


# ============================================================================== S17 FINAL EXPORT / PAYOFF
def s17(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-pl" class="abs plate" style="{box(110, 600, 860, 484)}overflow:hidden;padding:0">{mini_anim(f"{s}-an")}'
                  f'<div id="{s}-play" class="abs" style="left:380px;top:192px;width:100px;height:100px;border-radius:50%;background:rgba(10,13,44,.75);border:3px solid #00D0FE">'
                  f'<div class="abs" style="left:38px;top:28px;width:0;height:0;border-left:34px solid #fff;border-top:22px solid transparent;border-bottom:22px solid transparent"></div></div></div>')
    S.init(f"#{s}-an-prog", {"scaleX": 0})
    S.ft(f"#{s}-an-prog", {"scaleX": 0}, {"scaleX": 1}, W(158), W(160) + 0.3 - W(158), "none")
    S.ft(f"#{s}-an-sun", {"y": 0}, {"y": 40}, S.t0, S.t1 - S.t0, "sine.inOut")
    S.ft(f"#{s}-play", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.6}, W(152) + 0.1, 0.3, "power2.in")
    for k in range(6):
        import math
        x, y = 130 + k * 116, 1230
        S.back.append(f'<div id="{s}-k{k}" class="abs num" style="{box(x - 42, y, 84, 84)}font-size:30px;color:#fff">0{k + 1}</div>')
        t = W(152) + 0.12 * k
        pop(S, f"#{s}-k{k}", S.t0 + 0.1 + k * 0.05, 0.3)
        S.ft(f"#{s}-k{k}", {"color": "#ffffff", "boxShadow": "0 0 0 rgba(0,0,0,0)"}, {"color": CY, "boxShadow": "0 0 18px rgba(0,208,254,.6)"}, t, 0.18, "power2.out")
        S.fx(t, "click", 0.03)
    apex(S, S.back, f"{s}-ap", 540, 840, W(160) + 0.1, 600, ring=True, sparks=6, op=0.4)
    S.fx(W(160), "ping", 0.07)
    S.back.append(f'<div id="{s}-ok" class="abs plate plate-s" style="{box(110, 1110, 420, 90)}font:700 40px/90px Poppins;text-align:center;color:#fff">RENDER <span class="cy">OK</span></div>')
    pop(S, f"#{s}-ok", W(152) + 0.1, 0.32)
    S.cam([(S.t0, {"z": 80}, None), (S.t1, {"z": -30}, "power2.inOut")])
    heading(S, S.front, f"{s}-h", "CEK *SEMUA* FRAME", 60, HEAD_Y, 960, 70, "center", keys=[W(154), W(157), W(159)])
    narrator(S, dict(MASCOT_R, fx=950, h=560))
    S.intent(W(154), "present", "left")
    # handoff: the play icon slides right and becomes the CTA bubble tail
    S.back.append(f'<div id="{s}-tail" class="abs" style="left:540px;top:1404px;width:0;height:0;border-left:44px solid #294B77;border-top:28px solid transparent;border-bottom:28px solid transparent"></div>')
    S.init(f"#{s}-tail", {"opacity": 0, "x": -200})
    S.ft(f"#{s}-tail", {"opacity": 0, "x": -200}, {"opacity": 1, "x": 0}, S.t1 - 0.34, 0.34, "power3.inOut")


# ============================================================================== S18 CTA + BRAND LOCKUP
def s18(S):
    s, W = S.id, S.W
    S.back.append(f'<div id="{s}-sheet" class="abs plate" style="{box(110, 560, 520, 640)}">'
                  f'<div class="abs" style="left:34px;top:30px;font:700 34px/1.1 Poppins;color:#fff">TEMPLATE<br><span class="cy">PROMPT</span></div>'
                  + "".join(f'<div class="abs" style="left:34px;top:{150 + j * 40}px;width:{420 - (j % 3) * 70}px;height:14px;border-radius:7px;background:rgba(255,255,255,.25)"></div>' for j in range(5))
                  + f'<div class="abs" style="left:34px;top:370px;font:700 34px/1.1 Poppins;color:#fff">CHECKLIST</div>'
                  + "".join(f'<div class="abs" style="left:34px;top:{430 + j * 52}px;width:34px;height:34px;border-radius:8px;border:2.5px solid #00D0FE"></div>'
                            f'<div class="abs" style="left:90px;top:{442 + j * 52}px;width:{300 - j * 40}px;height:12px;border-radius:6px;background:rgba(255,255,255,.25)"></div>' for j in range(3))
                  + '</div>')
    pop(S, f"#{s}-sheet", W(162) - 0.1, 0.5, {"opacity": 0, "rotationY": -80, "x": -120}, {"opacity": 1, "rotationY": -6, "x": 0}, "power3.out")
    S.fx(W(162), "whoosh", 0.05)
    # CTA bubble (its tail arrived from the S17 play icon)
    S.front.append(f'<div id="{s}-cta" class="abs plate" style="{box(60, 1260, 600, 150)}border:2.5px solid #00D0FE;border-radius:40px;overflow:hidden">'
                   f'<div class="abs" style="left:0;top:36px;width:600px;text-align:center;font:700 62px/1 Poppins;color:#fff">KOMEN <span class="cy" id="{s}-kw">ANIMASI</span></div>'
                   f'<div id="{s}-csh" class="abs sheen" style="left:-200px;top:0;width:160px;height:150px"></div></div>'
                   f'<div class="abs" style="left:540px;top:1404px;width:0;height:0;border-left:44px solid #294B77;border-top:28px solid transparent;border-bottom:28px solid transparent"></div>')
    pop(S, f"#{s}-cta", W(167) - 0.1, 0.45, {"opacity": 0, "scale": 0.7}, {"opacity": 1, "scale": 1}, "back.out(1.6)")
    S.ft(f"#{s}-csh", {"x": 0}, {"x": 900}, W(168) + 0.1, 0.6, "power2.inOut")
    S.ft(f"#{s}-kw", {"textShadow": "0 0 0px rgba(0,208,254,0)"}, {"textShadow": "0 0 14px rgba(0,208,254,.35)"}, W(168), 0.2, "power2.out")
    apex(S, S.front, f"{s}-ap", 360, 1335, W(168) + 0.12, 560, ring=True, sparks=6, op=0.45)
    S.fx(W(168), "sparkle", 0.07)
    heading(S, S.front, f"{s}-h", "MAU *TEMPLATE-NYA?*", 60, HEAD_Y, 960, 70, "center", keys=[W(161), W(162)])
    narrator(S, dict(MASCOT_R, fx=900, h=820), rise=False)
    S.intent(W(167), "cta", "left")
