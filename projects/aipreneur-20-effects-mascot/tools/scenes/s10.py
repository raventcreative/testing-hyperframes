"""S10 — 09 STUDIO REVEAL (17.43–20.07)  VO: "Sekarang lihat perubahan gayanya. Studio menyala."
Opens on S09's glowing curve tip (CABLE0). "Sekarang lihat": the graph world goes dark, the mascot dims, the tip
runs down as a glowing cable into the right-hand light stand (and across the floor to the left stand).
"perubahan gayanya": two satin-metal stands rise and their softbox heads swing open toward the mascot.
"Studio menyala": the softboxes switch on (faces glow, beams, floor pool), the mascot is lit (brightness up, warm
key), a cyan STUDIO sign lights on the back wall; the camera re-frames WIDE -> MED 3/4.
Hand-off: everything dims except the key-light rectangle, which narrows into the MONITOR rect with the mascot
inside it -> S11's editor monitor."""
from xk import box, r3, apex, CYAN, clip_rect, CLIP_NONE
from kit import WIDE, MED, NO_FILTER, CABLE0, MONITOR, graph_world

FLT = "brightness({b}) drop-shadow(0px 0px 0px rgba(0,208,254,0))"
MON_VIEW = {"fx": 540, "fy": 1458, "h": 1128, "yaw": -10, "pitch": 4}   # == S11 monitor framing


def stand(s, k, x, flip):
    """light stand at x (base on the floor ~1700): tripod + pole + yoke + softbox head (id {s}-hd{k})."""
    sx = -1 if flip else 1
    legs = "".join(f'<div class="abs metal" style="{box(x - 3, 1560, 7, 170)}border-radius:3px;transform-origin:50% 0%;transform:rotate({a}deg)"></div>' for a in (-28, 0, 28))
    head = (f'<div class="abs" id="{s}-hd{k}" style="{box(x - 130, 690, 260, 200)}transform-origin:50% 100%">'
            f'<div class="abs metal" style="{box(118, 160, 24, 60)}border-radius:6px"></div>'
            f'<div class="abs" style="{box(0, 0, 260, 180)}border-radius:18px;background:linear-gradient(160deg,#2a3346,#0e1424);'
            f'box-shadow:inset 0 0 0 3px #8b97aa,inset 2px 2px 0 5px rgba(255,255,255,.25),0 18px 30px -10px rgba(3,8,28,.8)"></div>'
            f'<div class="abs" id="{s}-face{k}" style="{box(16, 16, 228, 148)}border-radius:10px;background:radial-gradient(ellipse at 50% 45%,#ffffff 0%,#e9fbff 45%,#bfeeff 80%);'
            f'box-shadow:0 0 40px 10px rgba(200,245,255,.85)"></div>'
            f'<div class="abs" style="{box(16, 16, 228, 148)}border-radius:10px;background:repeating-linear-gradient(90deg,rgba(14,20,36,.0) 0 36px,rgba(14,20,36,.18) 36px 38px)"></div></div>')
    pole = f'<div class="abs metal" id="{s}-pole{k}" style="{box(x - 7, 880, 14, 700)}border-radius:6px;transform-origin:50% 100%"></div>'
    return (f'<div class="abs" id="{s}-st{k}" style="{box(0, 0, 1080, 1920)}">'
            f'<div class="abs cshadow" style="{box(x - 120, 1690, 240, 50)}"></div>{legs}{pole}{head}</div>')


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W48, W49, W50, W51, W52, W53 = (S.W(i) for i in range(48, 54))   # Sekarang 17.52 lihat 17.84 perubahan 18.06 gayanya 18.46 Studio 19.06 menyala 19.42
    on = W52 + 0.04
    mx, my, mw, mh, mr = MONITOR
    LX, RX = 150, 930
    # ---------------------------------------------------------------- back: graph world (fading) -> dark studio cyc
    S.back.append(graph_world(s))
    S.back.append(f'<div class="abs" id="{s}-cyc" style="{box(0, 0, 1080, 1920)}background:linear-gradient(180deg,#07112a 0%,#0c1c40 55%,#132a55 70%,#0a1532 100%)"></div>')
    S.back.append(f'<div class="abs" id="{s}-cycl" style="{box(0, 0, 1080, 1920)}background:radial-gradient(ellipse 55% 42% at 50% 52%,rgba(80,140,220,.55),rgba(80,140,220,0) 70%),'
                  f'linear-gradient(180deg,rgba(0,0,0,0) 60%,rgba(120,170,230,.12) 72%,rgba(0,0,0,0) 90%)"></div>')
    # STUDIO sign on the back wall (cyan LED letters)
    S.back.append(f'<div class="abs" id="{s}-sign" style="{box(340, 300, 400, 90)}border-radius:14px;border:2px solid rgba(0,208,254,.5);'
                  f'font:700 58px/86px Poppins;letter-spacing:.32em;text-indent:.32em;text-align:center;color:{CYAN};text-shadow:0 0 18px rgba(0,208,254,.9),0 0 4px #fff">STUDIO</div>')
    # cable: from the curve tip down the right stand and along the floor to the left stand
    cable = f"M{CABLE0[0]},{CABLE0[1]} C1060,600 {RX + 40},700 {RX + 10},900 L{RX + 10},1700 C{RX - 60},1760 700,1745 540,1745 L{LX + 20},1745 C{LX - 10},1745 {LX - 10},1720 {LX - 8},1700"
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path id="{s}-cab" d="{cable}" fill="none" stroke="#9ff0ff" stroke-width="7" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" '
                  f'style="filter:drop-shadow(0 0 8px rgba(0,208,254,.9))"/>'
                  f'<path id="{s}-cabd" d="{cable}" fill="none" stroke="#1b2438" stroke-width="7" stroke-linecap="round" opacity="0"/></svg>')
    S.back.append(f'<div class="abs" id="{s}-tip" style="{box(CABLE0[0] - 30, CABLE0[1] - 30, 60, 60)}border-radius:50%;background:radial-gradient(circle,#ffffff 0%,#9ff0ff 35%,rgba(0,208,254,0) 70%)"></div>')
    S.back.append(stand(s, 0, LX, False))
    S.back.append(stand(s, 1, RX, True))
    S.back.append(f'<div class="abs" id="{s}-pool" style="{box(140, 1560, 800, 260)}border-radius:50%;background:radial-gradient(ellipse at 50% 50%,rgba(220,240,255,.55),rgba(160,210,255,.18) 45%,rgba(160,210,255,0) 70%)"></div>')
    # ---------------------------------------------------------------- front: beams (light falling on the mascot), dim + key matte
    for k, (x, rot) in enumerate(((LX, -32), (RX, 32))):
        S.front.append(f'<div class="abs" id="{s}-bm{k}" style="{box(x - 230, 790, 460, 1100)}transform-origin:50% 0%;transform:rotate({rot}deg);'
                       f'background:linear-gradient(180deg,rgba(230,248,255,.42),rgba(200,235,255,.08) 70%,rgba(200,235,255,0));'
                       f'clip-path:polygon(38% 0,62% 0,100% 100%,0 100%);mix-blend-mode:screen"></div>')
    S.front.append(f'<div class="abs" id="{s}-dark" style="{box(0, 0, 1080, 1920)}background:rgba(4,9,26,.62)"></div>')
    # key-light matte: everything outside the MONITOR rect goes dark at the end (hole = the monitor)
    S.front.append(f'<div class="abs" id="{s}-matte" style="{box(mx, my, mw, mh)}border-radius:{mr}px;box-shadow:0 0 0 2400px rgba(6,13,36,.94),0 0 60px 12px rgba(0,208,254,.35) inset"></div>')
    S.front.append(f'<div class="abs" id="{s}-mrim" style="{box(mx - 3, my - 3, mw + 6, mh + 6)}border-radius:{mr + 3}px;border:3px solid rgba(160,240,255,.9);box-shadow:0 0 22px rgba(0,208,254,.6)"></div>')
    apex(S, S.front, f"{s}-ap", 540, 760, on + 0.05, size=900, ring=False, sparks=0, seed=1001, op=0.32)

    # ---------------------------------------------------------------- motion
    S.init(f"#{s}-cyc", {"opacity": 0})
    S.ft(f"#{s}-cyc", {"opacity": 0}, {"opacity": 1}, t0 + 0.05, 0.5, "power2.inOut")
    S.init(f"#{s}-cycl", {"opacity": 0})
    S.ft(f"#{s}-cycl", {"opacity": 0}, {"opacity": 1}, on, 0.25, "power2.out")
    S.init(f"#{s}-sign", {"opacity": 0.12})
    S.ft(f"#{s}-sign", {"opacity": 0.12}, {"opacity": 0.75}, W53, 0.06, "none")
    S.ft(f"#{s}-sign", {"opacity": 0.75}, {"opacity": 0.3}, W53 + 0.06, 0.06, "none")
    S.ft(f"#{s}-sign", {"opacity": 0.3}, {"opacity": 1}, W53 + 0.12, 0.12, "power2.out")
    S.init(f"#{s}-tip", {"opacity": 1, "scale": 1})
    S.ft(f"#{s}-tip", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.3}, t0 + 0.3, 0.4, "power2.in")
    S.init(f"#{s}-cab", {"attr": {"stroke-dashoffset": 1}, "opacity": 1})
    S.ft(f"#{s}-cab", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, t0 + 0.02, W50 - t0 + 0.1, "power1.inOut")
    S.ft(f"#{s}-cab", {"opacity": 1}, {"opacity": 0.35}, on + 0.1, 0.4, "power2.out")
    # stands rise (poles extend), heads swing open toward the mascot
    for k, sgn in ((0, 1), (1, -1)):
        S.init(f"#{s}-st{k}", {"y": 520, "opacity": 0})
        S.ft(f"#{s}-st{k}", {"y": 520, "opacity": 0}, {"y": 0, "opacity": 1}, W49 - 0.05 + 0.08 * k, 0.5, "power3.out")
        S.init(f"#{s}-pole{k}", {"scaleY": 0.55})
        S.ft(f"#{s}-pole{k}", {"scaleY": 0.55}, {"scaleY": 1}, W50, 0.45, "back.out(1.4)")
        S.init(f"#{s}-hd{k}", {"rotation": -95 * sgn, "y": 300})
        S.ft(f"#{s}-hd{k}", {"rotation": -95 * sgn, "y": 300}, {"rotation": 30 * sgn, "y": 0}, W50 + 0.05 + 0.06 * k, 0.55, "back.out(1.3)")
        S.init(f"#{s}-face{k}", {"opacity": 0.06})
        S.ft(f"#{s}-face{k}", {"opacity": 0.06}, {"opacity": 1}, on + 0.07 * k, 0.12, "power2.out")
        S.init(f"#{s}-bm{k}", {"opacity": 0, "scaleY": 0.3})
        S.ft(f"#{s}-bm{k}", {"opacity": 0, "scaleY": 0.3}, {"opacity": 1, "scaleY": 1}, on + 0.07 * k, 0.3, "power2.out")
    S.init(f"#{s}-pool", {"opacity": 0, "scale": 0.6})
    S.ft(f"#{s}-pool", {"opacity": 0, "scale": 0.6}, {"opacity": 1, "scale": 1}, on + 0.05, 0.35, "power2.out")
    S.init(f"#{s}-dark", {"opacity": 0})
    S.ft(f"#{s}-dark", {"opacity": 0}, {"opacity": 1}, t0 + 0.05, 0.45, "power2.inOut")
    S.ft(f"#{s}-dark", {"opacity": 1}, {"opacity": 0}, on, 0.2, "power2.out")
    # hand-off: matte closes onto the monitor rect
    m0 = t1 - 0.36
    S.init(f"#{s}-matte", {"opacity": 0, "scale": 1.7, "transformOrigin": f"{mw / 2}px {mh / 2}px"})
    S.ft(f"#{s}-matte", {"opacity": 0, "scale": 1.7}, {"opacity": 1, "scale": 1}, m0, 0.3, "power3.inOut")
    S.init(f"#{s}-mrim", {"opacity": 0, "scale": 1.7, "transformOrigin": f"{mw / 2 + 3}px {mh / 2 + 3}px"})
    S.ft(f"#{s}-mrim", {"opacity": 0, "scale": 1.7}, {"opacity": 1, "scale": 1}, m0, 0.3, "power3.inOut")
    for k in range(2):
        S.ft(f"#{s}-bm{k}", {"opacity": 1}, {"opacity": 0.2}, m0, 0.3, "power2.in")

    # ---------------------------------------------------------------- mascot: dims, gets lit, WIDE -> MED 3/4 -> monitor framing
    v0 = dict(WIDE, yaw=14)
    S.mv([(t0, v0, None), (W50, dict(v0, yaw=4), "sine.inOut"),
          (on + 0.05, dict(MED, yaw=-16), "power3.inOut"),
          (m0, dict(MED, yaw=-12), "sine.inOut"),
          (t1, MON_VIEW, "power3.inOut")])
    S.mx([(t0, {"filter": FLT.format(b=1), "transformOrigin": "540px 960px"}, None),
          (t0 + 0.5, {"filter": FLT.format(b=0.42)}, "power2.inOut"),
          (on, {"filter": FLT.format(b=0.42)}, "none"),
          (on + 0.1, {"filter": FLT.format(b=1.2)}, "power2.out"),
          (on + 0.5, {"filter": FLT.format(b=1.0)}, "power2.inOut")])
    S.mc([(t0, {"clipPath": CLIP_NONE}, None), (m0, {"clipPath": CLIP_NONE}, "none"),
          (t1, {"clipPath": clip_rect(mx, my, mw, mh, mr)}, "power3.inOut")])
    # acting: looks around in the dark, reacts to the lights (lean back, open hands), then presents
    S.act("head", [(t0 + 0.02, [-0.1, 0.3, 0], 0.3), (W49, [0, -0.12, 0.04], 0.4), (W50 + 0.1, [-0.04, 0.25, -0.03], 0.4),
                   (on, [-0.12, 0, 0.06], 0.18), (on + 0.4, [0, -0.08, 0], 0.35), (m0, [0, 0, 0], 0.35)])
    S.act("armL", [(t0 + 0.02, "present", 0.35), (W49, "low", 0.4), (W51 - 0.1, "explain", 0.3), (on - 0.05, "open", 0.22), (on + 0.55, "low", 0.4)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W50, "palmUp", 0.35), (on - 0.05, "open", 0.22), (on + 0.55, "low", 0.4)])
    S.act("torso", [(t0 + 0.02, {"chest": [-0.04, 0.1, 0]}, 0.4), (on, {"chest": [-0.07, 0, 0], "spine": [-0.04, 0, 0]}, 0.2), (on + 0.45, {}, 0.4)])
    S.act("root", [(t0 + 0.02, {"ry": 0.2}, 0.4), (W50, {"ry": 0}, 0.5), (on, {"y": 0.012}, 0.15), (on + 0.3, {"y": 0}, 0.3)])
    S.fx(W50 + 0.1, "whoosh", 0.05)
    S.fx(on, "click", 0.09)
    S.fx(on + 0.07, "click", 0.06)
    S.fx(W53 + 0.12, "sparkle", 0.04)
    S.fx(m0 + 0.05, "whoosh", 0.05)
