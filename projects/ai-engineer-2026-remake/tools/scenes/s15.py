"""S15 — ENDING (W215 – end). VO: "Karena AI Engineer bukan yang paling banyak coba tools. Tapi yang bisa membangun sistem AI
yang benar-benar bekerja. Simpan roadmap ini. Mulai dari komponen pertama."
Opens on the S14 rail and camera. EXPLAIN MODE first: he comes to the front; behind him (soft) the ten modules glide in and
lock into the final machine around the AI core. In the band a scatter of tool icons pops on "banyak coba tools" and falls
away (it is not about the number of tools). He steps back to the lower left (DEMONSTRATE): the whole machine is sharp —
core, 10 numbered modules, and a readable end-to-end strip INPUT -> RETRIEVE -> TOOL -> HASIL -> TES. A light runs the
strip on "membangun sistem AI", every module answers on "bekerja" and the recap type lands: SISTEM AI YANG BEKERJA; on
"Simpan roadmap ini" it becomes the SIMPAN ROADMAP INI badge; on "komponen pertama" module 01 lights. He does a small
satisfied check (nod, open hand) and everything settles into a calm still for the last ~0.4 s — no fade."""
from xk import box, r3
from kit import (STAGE_RAIL_Y, MAT, part, cable, grid_floor, shadow, blur_wrap, explain, ICON, EXPLAIN_BAND)
from kit_d import label, icon_tile, orb, stage_models
from s14 import PADS

RY = STAGE_RAIL_Y
TILE_ICONS = ["fn", "branch", "gauge", "bolt", "chat", "plug", "doc", "tool", "check", "shield"]
TW, TH = 168, 104
TILES = [(70 + (k % 5) * 188, 700 + (k // 5) * 122) for k in range(10)]
CORE = (380, 430, 320, 240)
PIPE = [("INPUT", "chat"), ("RETRIEVE", "search"), ("TOOL", "tool"), ("HASIL", "doc"), ("TES", "check")]
PX0, PY, PW, PH, PG = 76, 990, 172, 120, 14
S14_END = {"x": 40, "y": -285, "scale": 1.03}


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    # ---------------------------------------------------------------- back: workbench, rail, core, modules, pipeline strip
    S.back.append(grid_floor(f"{s}-grid"))
    S.back.append(cable(f"{s}-rail", f"M-20,{RY} L1100,{RY}", w=10, dash=False))
    # the three S14 stage models, still on the rail at the cut; they lift off into the machine behind the blur
    S.back.append(f'<div class="abs" id="{s}-stages" style="left:0;top:0;width:1080px;height:1920px">' + "".join(stage_models(s, PADS, RY)) + "</div>")
    S.back.append(f'<div class="abs" id="{s}-mach" style="left:0;top:0;width:1080px;height:1920px">')
    S.back.append(shadow(60, 1150, 960, 70, 0.4))
    S.back.append(part(None, 40, 1130, 1000, 40, "alu", 14))
    # connectors tile -> core (drawn while the modules lock in)
    paths = "".join(f'<path id="{s}-w{k}" d="M{x + TW / 2},{y} C {x + TW / 2},{y - 60} {540},{CORE[1] + CORE[3] + 60} {540},{CORE[1] + CORE[3]}" '
                    f'fill="none" stroke="#294B77" stroke-width="3" opacity=".55" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                    for k, (x, y) in enumerate(TILES[:5]))
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">{paths}</svg>')
    cx, cy, cw, ch = CORE
    S.back.append(part(f"{s}-core", cx, cy, cw, ch, "enamel", 34,
                       inner=f'<div class="abs" style="left:{cw / 2 - 95}px;top:{ch / 2 - 95}px;width:190px;height:190px;border-radius:50%;{MAT["glass"]}"></div>'
                             + orb(f"{s}-orb", cw / 2, ch / 2, 140)
                             + f'<div class="abs" id="{s}-ring" style="left:{cw / 2 - 95}px;top:{ch / 2 - 95}px;width:190px;height:190px;border-radius:50%;box-shadow:0 0 0 6px #9fc4ff,0 0 40px 10px rgba(150,190,255,.7)"></div>'))
    for k, (x, y) in enumerate(TILES):
        S.back.append(f'<div class="abs" id="{s}-t{k}" style="{box(x, y, TW, TH)}">'
                      + icon_tile(None, 0, 0, TW, TH, TILE_ICONS[k], color="#1c3561", mat="porcelain", num=f"{k + 1:02d}")
                      + f'<div class="abs" id="{s}-tg{k}" style="left:-6px;top:-6px;width:{TW + 12}px;height:{TH + 12}px;border-radius:22px;'
                        f'box-shadow:0 0 0 4px #294B77,0 0 26px 6px rgba(120,170,240,.55)"></div></div>')
    for k, (name, ic) in enumerate(PIPE):
        x = PX0 + k * (PW + PG)
        S.back.append(f'<div class="abs" id="{s}-p{k}" style="{box(x, PY, PW, PH)}">'
                      + part(None, 0, 0, PW, PH, "glass", 18,
                             inner=f'<div class="abs" style="left:{PW / 2 - 21}px;top:14px;width:42px;height:42px;color:#1c3561">{ICON[ic]}</div>'
                                   + label(None, 0, 70, PW, name, 28))
                      + f'<div class="abs" id="{s}-pl{k}" style="left:{PW - 30}px;top:10px;width:20px;height:20px;border-radius:50%;'
                        f'background:radial-gradient(circle at 40% 35%,#cfe2ff,#294B77 70%);box-shadow:0 0 12px 3px rgba(120,170,240,.8)"></div></div>')
        if k < 4:
            ax = x + PW + 1
            S.back.append(f'<svg class="abs" style="left:{ax}px;top:{PY + PH / 2 - 9}px;width:12px;height:18px" viewBox="0 0 12 18">'
                          f'<path d="M2 2 L10 9 L2 16" fill="none" stroke="#294B77" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    S.back.append(f'<div class="abs" id="{s}-dot" style="left:{PX0 - 14}px;top:{PY + PH + 10}px;width:24px;height:24px;border-radius:12px;background:#fff;'
                  f'box-shadow:0 0 0 5px #294B77,0 0 22px 6px rgba(150,190,255,.9)"></div>')
    S.back.append("</div>")
    blur_wrap(S)
    # ---------------------------------------------------------------- front: explain band (tool scatter) + recap type
    tools = ["tool", "chat", "plug", "search", "bolt", "gauge"]
    by = EXPLAIN_BAND[0] + 18
    for k, ic in enumerate(tools):
        x = 90 + k * 152
        S.front.append(f'<div class="abs" id="{s}-k{k}" style="{box(x, by + (k % 2) * 18, 84, 84)}border-radius:22px;{MAT["glass"]}">'
                       f'<div class="abs" style="left:20px;top:20px;width:44px;height:44px;color:#1c3561">{ICON[ic]}</div></div>')
    S.front.append(f'<div class="abs" id="{s}-r1" style="{box(380, 1196, 670, 90)}text-align:left">'
                   f'<span class="tx" style="font:700 66px/1.1 Poppins, sans-serif">SISTEM AI YANG</span></div>')
    S.front.append(f'<div class="abs" id="{s}-r2" style="left:380px;top:1290px"><span class="badge" style="font:700 72px/1.1 Poppins, sans-serif">BEKERJA</span></div>')
    S.front.append(f'<div class="abs" id="{s}-r3" style="left:380px;top:1230px;width:680px">'
                   f'<span class="badge" style="font:700 60px/1.15 Poppins, sans-serif">SIMPAN<br/>ROADMAP INI</span></div>')

    # ---------------------------------------------------------------- motion
    t_out = W(224) - 0.32
    # camera: inherit the S14 end transform, settle to the machine view behind the blur, tiny push while it works
    S.cam([(t0, dict(S14_END), None), (t0 + 1.3, {"x": 0, "y": 0, "scale": 1}, "power3.inOut"), (t_out, {"x": 0, "y": 0, "scale": 1}, "none"),
           (W(232) + 0.3, {"x": 0, "y": -10, "scale": 1.025}, "sine.inOut"), (t1 - 0.4, {"x": 0, "y": -10, "scale": 1.03}, "sine.out")])
    # the machine frame rises in behind the blur (the S14 rail is the only thing carried over the cut)
    for k in range(3):
        S.init(f"#{s}-st{k}", {"y": 0, "scale": 1, "opacity": 1})
        S.ft(f"#{s}-st{k}", {"y": 0, "scale": 1, "opacity": 1}, {"y": -620, "scale": 0.6, "opacity": 0}, t0 + 0.15 + k * 0.08, 0.7, "power3.in")
    S.init(f"#{s}-stages", {"opacity": 1})
    S.ft(f"#{s}-stages", {"opacity": 1}, {"opacity": 0}, t0 + 0.5, 0.4, "power2.in")
    S.init(f"#{s}-mach", {"opacity": 0, "y": 60})
    S.ft(f"#{s}-mach", {"opacity": 0, "y": 60}, {"opacity": 1, "y": 0}, t0 + 0.75, 0.6, "power3.out")
    # modules glide in from scattered positions and lock in (staggered), connectors draw
    for k, (x, y) in enumerate(TILES):
        dx, dy, rr = ((k * 71) % 9 - 4) * 34, 180 + (k % 3) * 60, ((k * 37) % 7 - 3) * 6
        a = {"x": dx, "y": dy, "rotation": rr, "opacity": 0}
        S.init(f"#{s}-t{k}", a)
        bt = t0 + 0.4 + k * 0.12
        S.ft(f"#{s}-t{k}", a, {"x": 0, "y": 0, "rotation": 0, "opacity": 1}, bt, 0.6, "power3.out")
        S.init(f"#{s}-tg{k}", {"opacity": 0})
    for k in range(5):
        S.init(f"#{s}-w{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-w{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, t0 + 1.4 + k * 0.08, 0.6, "power2.inOut")
    S.init(f"#{s}-ring", {"opacity": 0, "scale": 0.8})
    S.init(f"#{s}-orb", {"filter": "brightness(1)"})
    for k in range(5):
        S.init(f"#{s}-pl{k}", {"opacity": 0.15, "scale": 0.8})
    S.init(f"#{s}-dot", {"x": 0, "opacity": 0})
    # explain band: tools pop on "banyak coba tools", then fall away
    ban = W(221)
    for k in range(6):
        sel = f"#{s}-k{k}"
        S.init(sel, {"opacity": 0, "scale": 0.4, "y": 20, "rotation": 0})
        S.ft(sel, {"opacity": 0, "scale": 0.4, "y": 20}, {"opacity": 1, "scale": 1, "y": 0}, ban - 0.1 + k * 0.06, 0.3, "back.out(2.5)")
        S.ft(sel, {"opacity": 1, "y": 0, "rotation": 0, "scale": 1}, {"opacity": 0, "y": 140, "rotation": (k % 2 * 2 - 1) * 24, "scale": 0.7},
             W(223) + 0.25 + k * 0.03, 0.4, "power2.in")
    S.fx(ban, "pop", 0.05)
    # the light runs the end-to-end strip on "membangun sistem AI"
    run0, run1 = W(227) - 0.05, W(229) + 0.3
    S.tset(f"#{s}-dot", {"opacity": 1}, run0)
    seg = (run1 - run0) / 5
    for k in range(5):
        x0 = k * (PW + PG)
        S.ft(f"#{s}-dot", {"x": x0}, {"x": x0 + PW + PG}, run0 + k * seg, seg, "none" if 0 < k < 4 else "power1.inOut")
        S.ft(f"#{s}-pl{k}", {"opacity": 0.15, "scale": 0.8}, {"opacity": 1, "scale": 1}, run0 + k * seg + seg * 0.5, 0.2, "back.out(3)")
        S.fx(run0 + k * seg + seg * 0.5, "click" if k % 2 == 0 else "key", 0.04)
    S.ft(f"#{s}-dot", {"opacity": 1}, {"opacity": 0}, run1, 0.2, "power2.out")
    # "bekerja": every module answers in a ripple, the core rings
    bek = W(232)
    for k in range(10):
        b = bek - 0.08 + (abs(k % 5 - 2) + (k // 5) * 0.5) * 0.06
        S.ft(f"#{s}-tg{k}", {"opacity": 0}, {"opacity": 1}, b, 0.14, "power2.out")
        S.ft(f"#{s}-tg{k}", {"opacity": 1}, {"opacity": 0}, b + 0.3, 0.45, "power2.inOut")
        S.ft(f"#{s}-t{k}", {"scale": 1}, {"scale": 1.06}, b, 0.14, "power2.out")
        S.ft(f"#{s}-t{k}", {"scale": 1.06}, {"scale": 1}, b + 0.16, 0.3, "power2.out")
    S.ft(f"#{s}-ring", {"opacity": 0, "scale": 0.8}, {"opacity": 1, "scale": 1.05}, bek - 0.05, 0.25, "power2.out")
    S.ft(f"#{s}-ring", {"opacity": 1, "scale": 1.05}, {"opacity": 0.35, "scale": 1}, bek + 0.3, 0.6, "power2.inOut")
    S.ft(f"#{s}-orb", {"filter": "brightness(1)"}, {"filter": "brightness(1.35)"}, bek - 0.05, 0.25, "power2.out")
    S.ft(f"#{s}-orb", {"filter": "brightness(1.35)"}, {"filter": "brightness(1.1)"}, bek + 0.3, 0.6, "sine.inOut")
    S.fx(bek, "sparkle", 0.06)
    # recap type
    S.init(f"#{s}-r1", {"opacity": 0, "y": 30})
    S.ft(f"#{s}-r1", {"opacity": 0, "y": 30}, {"opacity": 1, "y": 0}, W(228) - 0.05, 0.4, "power3.out")
    S.init(f"#{s}-r2", {"opacity": 0, "scale": 0.7, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-r2", {"opacity": 0, "scale": 0.7}, {"opacity": 1, "scale": 1}, bek - 0.04, 0.38, "back.out(2.2)")
    sim = W(233)
    for sel in (f"#{s}-r1", f"#{s}-r2"):
        S.ft(sel, {"opacity": 1, "y": 0}, {"opacity": 0, "y": -36}, sim - 0.22, 0.24, "power2.in")
    S.init(f"#{s}-r3", {"opacity": 0, "scale": 0.75, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-r3", {"opacity": 0, "scale": 0.75}, {"opacity": 1, "scale": 1}, sim - 0.02, 0.42, "back.out(2)")
    S.fx(sim, "pop", 0.06)
    # "komponen pertama": module 01 lights and stays lit (the end state)
    kom = W(238)
    S.ft(f"#{s}-tg0", {"opacity": 0}, {"opacity": 1}, kom - 0.05, 0.25, "power2.out")
    S.ft(f"#{s}-t0", {"scale": 1}, {"scale": 1.12}, kom - 0.05, 0.2, "power2.out")
    S.ft(f"#{s}-t0", {"scale": 1.12}, {"scale": 1.05}, kom + 0.2, 0.35, "power2.out")
    S.ft(f"#{s}-pl0", {"scale": 1}, {"scale": 1.4}, kom, 0.18, "power2.out")
    S.ft(f"#{s}-pl0", {"scale": 1.4}, {"scale": 1}, kom + 0.2, 0.3, "power2.out")
    S.fx(kom, "ping", 0.05)

    # ---------------------------------------------------------------- mascot
    enter = {"fx": 125, "fy": 1850, "h": 620, "yaw": 28, "pitch": 6}      # where S14 left him
    stand = {"fx": 190, "fy": 1730, "h": 600, "yaw": 22, "pitch": 6}
    explain(S, t0, t_out, 215, 223, seed=5, enter=enter, leave=stand)
    S.mv([(t_out + 0.5, stand, None), (bek, dict(stand, yaw=28), "sine.inOut"), (sim, dict(stand, yaw=18), "sine.inOut"),
          (t1 - 0.45, dict(stand, yaw=20), "sine.inOut")])
    # satisfied final check: look over the machine, open hand to it, nod, settle (no giant wave)
    S.act("armL", [(t_out + 0.25, "low", 0.4), (W(227) - 0.1, "point", 0.3), (W(230), "present", 0.35), (sim - 0.1, "explain", 0.35),
                   (kom - 0.15, "point", 0.3), (t1 - 0.75, "low", 0.45)])
    S.act("armR", [(t_out + 0.25, "low", 0.4), (bek - 0.1, "palmUp", 0.3), (sim + 0.4, "low", 0.4), (W(236), "together", 0.4), (t1 - 0.7, "low", 0.45)])
    S.act("head", [(t_out + 0.25, [-0.12, 0.3, 0], 0.4), (W(228), [-0.18, 0.36, 0.02], 0.4), (bek, [-0.02, 0.28, 0.06], 0.3),
                   (bek + 0.35, [0.12, 0.24, 0.02], 0.25), (bek + 0.65, [-0.04, 0.24, 0], 0.3), (sim, [0.02, 0.12, 0.04], 0.35),
                   (kom - 0.1, [-0.12, 0.34, 0], 0.35), (W(239) + 0.2, [0.08, 0.2, 0.02], 0.3), (t1 - 0.65, [0.0, 0.16, 0.0], 0.4)])
    S.act("torso", [(t_out + 0.25, {"chest": [0.02, 0.1, 0]}, 0.4), (bek, {"chest": [-0.04, 0.12, 0]}, 0.35), (t1 - 0.7, {"chest": [0, 0.08, 0]}, 0.45)])
