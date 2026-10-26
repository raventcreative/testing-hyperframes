"""S06 — CLAUDE CODE INPUT (13.78–16.72)  VO: "Kasih naskah dan referensi visual ke Claude Code."
Motion source REF-M (search-bar morph, user reference 6f29fd9a…mp4): a navy cube tumbles in and settles, stretches
horizontally into a porcelain search bar, icons appear, "Claude Code" is typed, a pointer clicks search, the bar
collapses into a thin navy line. LINE MATCH: that line travels down and becomes the composer of the user's real
Claude Code screen (assets/elements/xray/s06/cc_screen.png, private task list removed), which unfolds upward out of
it (SCALE MORPH). The camera follows the caret while "naskah + referensi visual" is typed; on "Claude" the send
button fires (apex), the message rises into the thread and Claude's reply streams in. Hand-off: the screen tips
back onto the round stage that opens S07."""
from xk import box, shadow, apex, r3, Rng
from kit_b import backdrop, near_blur

SFX = []          # filled in build(): typing ticks + click + send (VO-aware levels in tools/gen_sfx.py)

# device geometry (screen space at z = 0)
K = 932 / 744                      # screenshot scale
BZ = 16                            # bezel
DW, DH = 932 + 2 * BZ, round(582 * K) + 2 * BZ
DX, DY = 560 - DW / 2, 560
def dx(x):                         # screenshot x (original 1614-wide coords) -> device-local x
    return BZ + (x - 440) * K
def dy(y):
    return BZ + (y - 120) * K
CMP = (dx(468), dy(635), dx(1156) - dx(468), dy(672) - dy(635))      # composer rect (device-local)
BAR_Y, BAR_W, BAR_H, BAR_CX = 930, 820, 92, 560                      # REF-M search bar
TYPE1 = "Claude Code"
TYPE2 = "naskah + referensi visual"


def chars(prefix, text):
    return "".join(f'<span class="ch" id="{prefix}{k}">{("&nbsp;" if c == " " else c)}</span>' for k, c in enumerate(text))


def build(S):
    s = S.id
    S.persp_origin = (560, 620)
    W = S.W
    t0, t1 = S.t0, S.t1
    W30, W32, W33, W35, W36 = W(30), W(32), W(33), W(35), W(36)     # naskah, referensi, visual, Claude, Code.
    S.css += [
        f"#{s}-bar .ch, #{s}-cmp-tx .ch {{ display: none; }}",
        f".{s}-ico {{ position:absolute; width:40px; height:40px; }}",
    ]
    backdrop(S, seed=11)
    # far bokeh discs (REF-H depth)
    R = Rng(606)
    disc = "".join(f'<div class="abs" style="{box(R.u(80, 980), R.u(420, 1500), d, d)}border-radius:50%;opacity:.55;filter:blur(7px);'
                   f'background:radial-gradient(circle at 35% 30%,#fff,#e8f0fb 45%,#acc6e7)"></div>' for d in (70, 46, 96, 38, 60))
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-300px) scale(1.15)">{disc}</div>')

    # ------------------------------------------------------------------ A. REF-M search bar
    m = []
    m.append(shadow(BAR_CX - 430, BAR_Y + 26, 900, 70, 0.75, id_=f"{s}-barsh"))
    # navy enamel cube (tumbles in, then becomes the bar)
    m.append(f'<div class="abs" id="{s}-cube" style="{box(BAR_CX - 30, BAR_Y - 30, 60, 60)}border-radius:12px;'
             f'background:linear-gradient(135deg,#3a6299,#294b77 55%,#1c3354);box-shadow:inset 2px 2px 0 rgba(255,255,255,.35),0 14px 22px -8px rgba(28,51,84,.55)"></div>')
    # the bar (porcelain, navy rim); revealed by an animated clip-path so the rounded ends never distort
    m.append(f'<div class="abs" id="{s}-bar" style="{box(BAR_CX - BAR_W / 2, BAR_Y - BAR_H / 2, BAR_W, BAR_H)}border-radius:46px;'
             f'background:linear-gradient(176deg,#ffffff,#eef3fa);border:3px solid #294b77;box-shadow:inset 0 2px 0 #fff,inset 0 -3px 6px rgba(172,198,231,.6)">'
             # search glass icon (left) + typed text + caret
             f'<svg class="{s}-ico" id="{s}-ic1" style="left:30px;top:23px" viewBox="0 0 40 40"><circle cx="17" cy="17" r="10" fill="none" stroke="#294b77" stroke-width="4"/><path d="M25 25 L34 34" stroke="#294b77" stroke-width="5" stroke-linecap="round"/></svg>'
             f'<div class="abs" style="left:88px;top:20px;height:50px;font:600 38px/50px Inter,sans-serif;color:#202b3b;white-space:nowrap">{chars(s + "-g", TYPE1)}'
             f'<span id="{s}-caret1" style="display:inline-block;width:3px;height:38px;margin-left:3px;vertical-align:-6px;background:#294b77"></span></div>'
             # mic + search button (right)
             f'<svg class="{s}-ico" id="{s}-ic2" style="left:{BAR_W - 136}px;top:23px" viewBox="0 0 40 40"><rect x="14" y="5" width="12" height="20" rx="6" fill="#294b77"/><path d="M9 19 a11 11 0 0 0 22 0 M20 30 V36" fill="none" stroke="#294b77" stroke-width="3.5" stroke-linecap="round"/></svg>'
             f'<div class="abs" id="{s}-go" style="left:{BAR_W - 80}px;top:13px;width:60px;height:60px;border-radius:30px;background:linear-gradient(135deg,#3a6299,#294b77 60%,#1c3354);box-shadow:0 6px 12px -4px rgba(28,51,84,.5)">'
             f'<svg style="position:absolute;left:12px;top:12px;width:36px;height:36px" viewBox="0 0 40 40"><circle cx="17" cy="17" r="9" fill="none" stroke="#fbfcfe" stroke-width="4"/><path d="M24 24 L32 32" stroke="#fbfcfe" stroke-width="5" stroke-linecap="round"/></svg></div>'
             f'</div>')
    # the user's Google logo above the bar (supplied asset, only width set)
    m.append(f'<img id="{s}-glogo" src="assets/elements/xray/s06/google_logo.png" alt="" style="position:absolute;left:{BAR_CX - 150}px;top:{BAR_Y - 190}px;width:300px" />')
    # line that the bar collapses into -> travels to the composer
    m.append(f'<div class="abs" id="{s}-line" style="{box(BAR_CX - BAR_W / 2, BAR_Y - 3, BAR_W, 6)}border-radius:3px;background:#294b77;box-shadow:0 0 12px rgba(172,198,231,.9)"></div>')
    # pointer (REF-M interaction)
    m.append(f'<svg id="{s}-ptr" style="position:absolute;left:0;top:0;width:54px;height:66px;overflow:visible" viewBox="0 0 27 33">'
             f'<path d="M2 2 L2 26 L8 20 L12 30 L16 28 L12 19 L20 19 Z" fill="#fbfcfe" stroke="#1c3354" stroke-width="2" stroke-linejoin="round"/></svg>')

    # ------------------------------------------------------------------ B. Claude Code screen (user's screenshot)
    cx0, cy0, cw, ch = CMP
    dev = []
    for k in range(6, 0, -1):    # thickness (navy sidewall)
        dev.append(f'<div class="abs" style="{box(0, 0, DW, DH)}border-radius:30px;background:{"#1c3354" if k > 3 else "#294b77"};transform:translateZ({-k * 3}px)"></div>')
    dev.append(f'<div class="abs por" style="{box(0, 0, DW, DH)}border-radius:30px"></div>')
    dev.append(f'<div class="abs" style="{box(BZ, BZ, DW - 2 * BZ, DH - 2 * BZ)}border-radius:16px;overflow:hidden;background:#191919">'
               f'<img src="assets/elements/xray/s06/cc_screen.png" alt="" style="position:absolute;left:0;top:0;width:{DW - 2 * BZ}px" />'
               # user message bubble (appears after send) + Claude reply (abstract streaming lines)
               f'<div class="abs" id="{s}-ubub" style="{box(DW - 2 * BZ - 470, 300, 430, 56)}border-radius:16px;background:#303030;color:#ececec;'
               f'font:500 23px/56px Inter,sans-serif;text-align:center;white-space:nowrap">{TYPE2}</div>'
               + "".join(f'<div class="abs" id="{s}-rl{k}" style="{box(60, 400 + k * 34, w, 14)}border-radius:7px;background:{c}"></div>'
                         for k, (w, c) in enumerate(((520, "#5a5a5a"), (600, "#4a4a4a"), (430, "#4a4a4a"), (300, "#3f3f3f"))))
               + f'<div class="abs" id="{s}-rdot" style="{box(28, 402, 12, 12)}border-radius:6px;background:#d97757"></div>'
               f'<div class="abs" id="{s}-sheen" style="{box(-300, -80, 200, DH + 160)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.14),rgba(255,255,255,0))"></div>'
               f'</div>')
    # composer overlay: typed text, caret, send button, focus ring
    dev.append(f'<div class="abs" id="{s}-cring" style="{box(cx0 - 4, cy0 - 4, cw + 8, ch + 8)}border-radius:16px;border:3px solid #acc6e7;box-shadow:0 0 18px rgba(172,198,231,.8)"></div>')
    dev.append(f'<div class="abs" id="{s}-cmp-tx" style="left:{r3(dx(505))}px;top:{r3(cy0 + 6)}px;height:{r3(ch - 12)}px;font:500 26px/{r3(ch - 12)}px Inter,sans-serif;color:#ececec;white-space:nowrap">'
               f'{chars(s + "-c", TYPE2)}<span id="{s}-caret2" style="display:inline-block;width:2px;height:28px;margin-left:2px;vertical-align:-5px;background:#ececec"></span></div>')
    dev.append(f'<div class="abs" id="{s}-send" style="{box(dx(1138) - 24, cy0 + ch / 2 - 24, 48, 48)}border-radius:24px;background:#d97757">'
               f'<svg style="position:absolute;left:10px;top:10px;width:28px;height:28px" viewBox="0 0 28 28"><path d="M14 22 V7 M7 13 L14 6 L21 13" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    for k, (x, y) in enumerate(((10, 10), (DW - 10, 10), (10, DH - 10), (DW - 10, DH - 10))):
        dev.append(f'<div class="rivet" style="left:{x - 4}px;top:{y - 4}px"></div>')
    S.mid.append(shadow(DX - 20, DY + DH - 30, DW + 60, 90, 0.85, id_=f"{s}-devsh"))
    # stage top that the device tips onto (same geometry as S07's opening stage)
    S.mid.append(f'<div class="abs" id="{s}-stage" style="{box(230, 1010, 720, 130)}border-radius:0 0 360px 360px / 0 0 64px 64px;background:linear-gradient(90deg,#3a6299,#294b77 45%,#1c3354)"></div>'
                 f'<div class="abs" id="{s}-stagetop" style="{box(230, 900, 720, 170)}border-radius:50%;background:radial-gradient(ellipse at 40% 35%,#ffffff,#eef3fa 55%,#d3dff0);box-shadow:inset 0 -4px 8px rgba(172,198,231,.7)"></div>')
    S.mid.append(f'<div class="abs p3" id="{s}-dev" style="{box(DX, DY, DW, DH)}">{"".join(dev)}</div>')
    S.mid += m
    near_blur(S, [(f"{s}-nr1", 900, 520, 170, 170, "border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"),
                  (f"{s}-nr2", -40, 1480, 300, 24, "border-radius:12px;background:linear-gradient(180deg,#fff,#cbdbf4);filter:blur(4px);opacity:.9")])

    # ================================================================== MOTION
    send_x, send_y = DX + dx(1138), DY + cy0 + ch / 2
    apex(S, S.near, f"{s}-ap", send_x - 40, send_y - 60, W35, size=620, sparks=8, seed=66)
    # camera: push-in, follow the caret, settle after send, tip toward the stage
    S.cam([(t0, {"z": 60, "x": 0, "y": 0, "rotationX": 0, "rotationY": -3}, None),
           (15.08, {"z": 120, "rotationY": 2}, "sine.inOut"),
           (15.42, {"z": 150, "x": 70, "y": -170}, "power3.inOut"),        # onto the composer (left part, where the text grows)
           (15.78, {"z": 190, "x": -20, "y": -190}, "sine.inOut"),        # follows the caret
           (16.2, {"z": 90, "x": 0, "y": -40}, "power3.out"),            # pull back on send
           (t1, {"z": 170, "y": 20, "rotationX": 4}, "power2.in")])

    # A1 cube tumbles in (already moving at frame 0), settles with a small overshoot
    S.keys(f"#{s}-cube", [(t0, {"rotation": 52, "y": -70, "scaleX": 0.7, "scaleY": 0.7, "opacity": 1}, None),
                          (t0 + 0.14, {"rotation": -6, "y": 0, "scaleX": 1.0, "scaleY": 1.0}, "power3.out"),
                          (t0 + 0.2, {"rotation": 0}, "power2.out"),
                          (14.04, {"scaleX": 1.25, "scaleY": 0.9}, "power2.in"),
                          (14.07, {"opacity": 0}, "none")])
    # A2 bar stretches out of the cube (clip-path keeps the round ends)
    S.init(f"#{s}-bar", {"clipPath": "inset(0% 46.3% 0% 46.3% round 46px)", "opacity": 0})
    S.tset(f"#{s}-bar", {"opacity": 1}, 14.04)
    S.ft(f"#{s}-bar", {"clipPath": "inset(0% 46.3% 0% 46.3% round 46px)"}, {"clipPath": "inset(0% 0% 0% 0% round 46px)"}, 14.04, 0.24, "power4.out")
    S.init(f"#{s}-barsh", {"scaleX": 0.08, "opacity": 0.75})
    S.ft(f"#{s}-barsh", {"scaleX": 0.08}, {"scaleX": 1}, 14.04, 0.24, "power4.out")
    for k, (sel, at) in enumerate(((f"#{s}-ic1", 14.2), (f"#{s}-ic2", 14.24), (f"#{s}-go", 14.27))):
        S.init(sel, {"scale": 0.4, "opacity": 0})
        S.ft(sel, {"scale": 0.4, "opacity": 0}, {"scale": 1, "opacity": 1}, at, 0.26, "back.out(1.8)")
    S.init(f"#{s}-glogo", {"y": 26, "opacity": 0})
    S.ft(f"#{s}-glogo", {"y": 26, "opacity": 0}, {"y": 0, "opacity": 1}, 14.16, 0.34, "power3.out")
    # A3 typing "Claude Code" (each char on its own frame step), caret blinks
    ts = 14.3
    for k, c in enumerate(TYPE1):
        S.tset(f"#{s}-g{k}", {"display": "inline"}, ts + k * 0.048)
        if c != " " and k % 2 == 0:
            SFX.append((ts + k * 0.048, "type", 0.035))
    S.init(f"#{s}-caret1", {"opacity": 1})
    S.ft(f"#{s}-caret1", {"opacity": 1}, {"opacity": 0.15}, 14.86, 0.12, "steps(1)")
    # A4 pointer arrives and clicks the search button
    gx, gy = BAR_CX - BAR_W / 2 + BAR_W - 50, BAR_Y
    S.init(f"#{s}-ptr", {"opacity": 0})
    S.tset(f"#{s}-ptr", {"opacity": 1}, 14.78)
    S.keys(f"#{s}-ptr", [(14.78, {"x": 1000, "y": 1400, "scale": 1}, None),
                         (14.96, {"x": gx, "y": gy}, "power3.out"),
                         (15.0, {"scale": 0.86, "transformOrigin": "0% 0%"}, "power2.in"),
                         (15.08, {"scale": 1}, "power2.out"),
                         (15.2, {"x": gx + 140, "y": gy + 160}, "power2.in")])
    S.tset(f"#{s}-ptr", {"opacity": 0}, 15.2)
    S.init(f"#{s}-go", {"scale": 1})
    S.ft(f"#{s}-go", {"scale": 1}, {"scale": 0.84}, 14.99, 0.05, "power2.in")
    SFX.append((15.0, "click", 0.07))
    # A5 bar collapses into a thin line (REF-M), logo lifts away
    S.ft(f"#{s}-bar", {"clipPath": "inset(0% 0% 0% 0% round 46px)"}, {"clipPath": "inset(48% 0% 48% 0% round 3px)"}, 15.06, 0.1, "power3.in")
    S.ft(f"#{s}-glogo", {"y": 0, "opacity": 1}, {"y": -30, "opacity": 0}, 15.04, 0.14, "power2.in")
    S.ft(f"#{s}-barsh", {"scaleX": 1, "opacity": 0.75}, {"scaleX": 0.9, "opacity": 0}, 15.06, 0.12, "power2.in")
    S.tset(f"#{s}-bar", {"opacity": 0}, 15.16)
    # A6 LINE MATCH: the line travels to the composer and becomes it
    S.init(f"#{s}-line", {"opacity": 0, "x": 0, "y": 0, "scaleX": 1})
    S.tset(f"#{s}-line", {"opacity": 1}, 15.15)
    tgt_y = DY + cy0 + ch / 2 - BAR_Y
    S.ft(f"#{s}-line", {"x": 0, "y": 0, "scaleX": 1}, {"x": 0, "y": tgt_y, "scaleX": cw / BAR_W}, 15.15, 0.18, "power3.inOut")
    S.tset(f"#{s}-line", {"opacity": 0}, 15.36)
    # B1 the screen unfolds upward out of the composer line (scale morph)
    org = f"50% {r3((cy0 + ch / 2) / DH * 100)}%"
    S.init(f"#{s}-dev", {"scaleY": 0.02, "scaleX": 1, "opacity": 0, "transformOrigin": org, "rotationX": 0, "y": 0})
    S.tset(f"#{s}-dev", {"opacity": 1}, 15.32)
    S.ft(f"#{s}-dev", {"scaleY": 0.02}, {"scaleY": 1}, 15.32, 0.3, "power4.out")
    S.init(f"#{s}-devsh", {"opacity": 0, "scaleX": 0.6})
    S.ft(f"#{s}-devsh", {"opacity": 0, "scaleX": 0.6}, {"opacity": 0.85, "scaleX": 1}, 15.32, 0.3, "power3.out")
    S.init(f"#{s}-sheen", {"x": 0})
    S.ft(f"#{s}-sheen", {"x": 0}, {"x": DW + 500}, 15.4, 0.7, "power2.inOut")
    # B2 composer focus + typing the spoken prompt
    S.init(f"#{s}-cring", {"opacity": 0, "scale": 1.04})
    S.ft(f"#{s}-cring", {"opacity": 0, "scale": 1.04}, {"opacity": 1, "scale": 1}, 15.4, 0.2, "power3.out")
    ts2, step = 15.44, 0.016
    for k, c in enumerate(TYPE2):
        S.tset(f"#{s}-c{k}", {"display": "inline"}, ts2 + k * step)
        if c != " " and k % 3 == 0:
            SFX.append((ts2 + k * step, "type", 0.03))
    S.init(f"#{s}-send", {"scale": 0, "opacity": 0})
    S.ft(f"#{s}-send", {"scale": 0, "opacity": 0}, {"scale": 1, "opacity": 1}, 15.5, 0.24, "back.out(2)")
    # B3 APEX on "Claude": send fires, text leaves the composer, the message lands in the thread
    S.ft(f"#{s}-send", {"scale": 1}, {"scale": 0.78}, W35 - 0.06, 0.06, "power2.in")
    S.ft(f"#{s}-send", {"scale": 0.78}, {"scale": 1}, W35, 0.3, "back.out(2.4)")
    S.ft(f"#{s}-cmp-tx", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -24}, W35 + 0.01, 0.12, "power2.in")
    S.ft(f"#{s}-cring", {"opacity": 1}, {"opacity": 0}, W35 + 0.05, 0.25, "power2.out")
    S.init(f"#{s}-ubub", {"opacity": 0, "y": 330, "scale": 0.9})
    S.ft(f"#{s}-ubub", {"opacity": 0, "y": 330, "scale": 0.9}, {"opacity": 1, "y": 0, "scale": 1}, W35 + 0.04, 0.36, "power3.out")
    SFX.append((W35, "pop", 0.06))
    # B4 Claude replies: dot pulses, lines stream in on "Code"
    for k in range(4):
        S.init(f"#{s}-rl{k}", {"scaleX": 0, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-rl{k}", {"scaleX": 0}, {"scaleX": 1}, W36 + 0.04 + k * 0.08, 0.3, "power2.out")
    S.init(f"#{s}-rdot", {"scale": 0})
    S.ft(f"#{s}-rdot", {"scale": 0}, {"scale": 1}, W36 - 0.08, 0.2, "back.out(2.5)")
    S.ft(f"#{s}-rdot", {"scale": 1}, {"scale": 1.35}, W36 + 0.2, 0.18, "sine.inOut")
    S.ft(f"#{s}-rdot", {"scale": 1.35}, {"scale": 1}, W36 + 0.38, 0.18, "sine.inOut")
    # C hand-off: the screen tips back onto the round stage (S07 opens on it)
    S.init(f"#{s}-stage", {"opacity": 0, "y": 40})
    S.init(f"#{s}-stagetop", {"opacity": 0, "y": 40})
    for sel in (f"#{s}-stage", f"#{s}-stagetop"):
        S.ft(sel, {"opacity": 0, "y": 40}, {"opacity": 1, "y": 0}, 16.48, 0.22, "power3.out")
    S.ft(f"#{s}-dev", {"rotationX": 0, "y": 0, "scaleX": 1, "scaleY": 1},
         {"rotationX": 68, "y": -60, "scaleX": 0.78, "scaleY": 0.78}, 16.3, 0.26, "power2.in")
    S.ft(f"#{s}-dev", {"opacity": 1}, {"opacity": 0}, 16.5, 0.1, "power1.in")
    S.ft(f"#{s}-devsh", {"opacity": 0.85}, {"opacity": 0}, 16.4, 0.2, "power1.in")
