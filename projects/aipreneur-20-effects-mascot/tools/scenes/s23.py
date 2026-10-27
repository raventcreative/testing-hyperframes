"""S23 — CLAUDE CODE WORKFLOW (39.93–43.30)
VO: "Semua bisa kita rancang di Claude Code lewat animasi berbasis kode."
Opens on S22's cover card (same rect). A smoked-glass code panel unfolds around it; the card slides into the panel's
preview slot. Conceptual code (NOT an official UI) types in, line by line, on the words. Under the panel the chain
FOOTAGE -> BRIEF -> CODED SCENES -> PREVIEW lights node by node. The mascot hands the brief over (present gesture).
Honest framing: it is a diagram of the workflow, not a recording of a product."""
from xk import box, r3, CYAN
from kit import SELF

PX, PY, PW, PH = 70, 262, 940, 590
SLOT = (PX + PW - 300, PY + 70, 270, 480)      # preview slot inside the panel
CARD0 = (375, 300, 330, 587)                    # S22 end rect of the cover card
CODE = [
    ('<span class="cy">scene</span>(<span class="q">"paper-cutout"</span>)', 0),
    ('&nbsp;&nbsp;.edge(<span class="q">"kertas"</span>).<span class="cy">to</span>(<span class="q">"rel kamera"</span>)', 1),
    ('&nbsp;&nbsp;.match(<span class="q">"rel"</span>, <span class="q">"sampul majalah"</span>)', 2),
    ('<span class="cy">timeline</span>.add(<span class="q">"dolly-zoom"</span>, 0.8)', 3),
    ('<span class="cy">render</span>(1080, 1920, 30)', 4),
]
NODES = ["FOOTAGE", "BRIEF", "CODED SCENES", "PREVIEW"]


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W114, W117, W119, W120, W122, W124 = (S.W(i) for i in (114, 117, 119, 120, 122, 124))
    S.css.append(f"#{s}-code .q {{ color: #fff; opacity: .78; }} #{s}-code .cy {{ color: {CYAN}; font-weight: 700; }}")
    # ---------------------------------------------------------------- back: panel + code + preview slot + chain
    S.back.append(f'<div class="abs smoked" id="{s}-panel" style="{box(PX, PY, PW, PH)}border-radius:30px">'
                  f'<div class="abs" style="left:28px;top:24px;width:12px;height:12px;border-radius:6px;background:rgba(255,255,255,.5)"></div>'
                  f'<div class="abs" style="left:48px;top:24px;width:12px;height:12px;border-radius:6px;background:rgba(255,255,255,.3)"></div>'
                  f'<div class="abs" style="left:68px;top:24px;width:12px;height:12px;border-radius:6px;background:rgba(0,208,254,.8)"></div>'
                  f'<div class="abs" style="left:100px;top:14px;width:420px;font:700 24px/32px Poppins;color:#fff;letter-spacing:.02em">Claude Code <span style="font-weight:400;opacity:.7">· brief → scenes</span></div>'
                  f'<div class="abs" style="left:24px;top:58px;width:{PW - 48}px;height:1px;background:rgba(255,255,255,.16)"></div></div>')
    rows = []
    for k, (code, _) in enumerate(CODE):
        rows.append(f'<div class="abs" style="left:0;top:{k * 62}px;width:590px;height:56px;overflow:hidden">'
                    f'<div class="abs" style="left:0;top:0;width:36px;font:400 22px/56px Poppins;color:rgba(255,255,255,.35);text-align:right">{k + 1}</div>'
                    f'<div class="abs" id="{s}-ln{k}" style="left:52px;top:0;width:540px;font:400 25px/56px Poppins;color:#fff;white-space:nowrap">{code}</div>'
                    f'<div class="abs" id="{s}-cur{k}" style="left:52px;top:12px;width:3px;height:32px;background:{CYAN}"></div></div>')
    S.back.append(f'<div class="abs" id="{s}-code" style="{box(PX + 18, PY + 90, 600, 340)}">' + "".join(rows) + "</div>")
    S.back.append(f'<div class="abs" style="{box(SLOT[0] - 6, SLOT[1] - 6, SLOT[2] + 12, SLOT[3] + 12)}border-radius:20px;border:2px dashed rgba(255,255,255,.25)"></div>')
    # chain FOOTAGE -> BRIEF -> CODED SCENES -> PREVIEW
    nw = [170, 140, 230, 170]
    gap = (940 - sum(nw)) / 3
    x = 70
    chain = []
    for k, n in enumerate(NODES):
        chain.append(f'<div class="abs pill" id="{s}-n{k}" style="{box(x, 888, nw[k], 64)}border:2px solid rgba(255,255,255,.3);background:rgba(8,18,44,.6);'
                     f'font:700 22px/60px Poppins;color:#fff;text-align:center;letter-spacing:.04em">{n}</div>')
        chain.append(f'<div class="abs pill acrylic" id="{s}-nh{k}" style="{box(x, 888, nw[k], 64)}font:700 22px/60px Poppins;color:#fff;text-align:center;letter-spacing:.04em">{n}</div>')
        if k < 3:
            chain.append(f'<div class="abs glowline" id="{s}-a{k}" style="{box(x + nw[k] + 6, 918, gap - 12, 4)}"></div>')
        x += nw[k] + gap
    S.back += chain
    # the card (from S22) - moves into the preview slot
    cx, cy, cw, ch = CARD0
    S.back.append(f'<div class="abs" id="{s}-card" style="{box(cx, cy, cw, ch)}border-radius:18px;overflow:hidden;box-shadow:0 0 0 3px {CYAN},0 0 22px rgba(0,208,254,.55)">'
                  f'<img src="{SELF}/cover.jpg" alt="" style="position:absolute;left:0;top:0;width:{cw}px;height:{ch}px" /></div>')

    # ---------------------------------------------------------------- motion
    S.init(f"#{s}-panel", {"scaleX": 0.36, "scaleY": 0.9, "opacity": 0, "transformOrigin": "540px 330px"})
    S.ft(f"#{s}-panel", {"scaleX": 0.36, "scaleY": 0.9, "opacity": 0}, {"scaleX": 1, "scaleY": 1, "opacity": 1}, t0 + 0.04, 0.45, "power3.out")
    sx, sy, sw, sh = SLOT
    S.init(f"#{s}-card", {"x": 0, "y": 0, "scale": 1, "transformOrigin": "0% 0%"})
    S.ft(f"#{s}-card", {"x": 0, "y": 0, "scale": 1}, {"x": sx - cx, "y": sy - cy, "scale": sw / cw}, t0 + 0.1, 0.5, "power3.inOut")
    # code types in on the words (clip reveal + caret)
    beats = [W114 + 0.05, W117, W119, W122, W124 - 0.1]
    for k, b in enumerate(beats):
        S.init(f"#{s}-ln{k}", {"clipPath": "inset(0px 100% 0px 0px)"})
        S.ft(f"#{s}-ln{k}", {"clipPath": "inset(0px 100% 0px 0px)"}, {"clipPath": "inset(0px 0% 0px 0px)"}, b, 0.42, "steps(14)")
        S.init(f"#{s}-cur{k}", {"x": 0, "opacity": 0})
        S.tset(f"#{s}-cur{k}", {"opacity": 1}, b)
        S.ft(f"#{s}-cur{k}", {"x": 0}, {"x": 520}, b, 0.42, "steps(14)")
        S.tset(f"#{s}-cur{k}", {"opacity": 0}, b + 0.5)
        S.fx(b, "type", 0.04)
    # chain lights node by node
    lights = [W114, W117, W122, W124]
    for k, b in enumerate(lights):
        S.init(f"#{s}-nh{k}", {"opacity": 0, "scale": 0.9})
        S.ft(f"#{s}-nh{k}", {"opacity": 0, "scale": 0.9}, {"opacity": 1, "scale": 1}, b, 0.25, "back.out(2.2)")
        if k < 3:
            S.init(f"#{s}-a{k}", {"scaleX": 0, "transformOrigin": "0% 50%"})
            S.ft(f"#{s}-a{k}", {"scaleX": 0}, {"scaleX": 1}, b + 0.12, 0.3, "power2.out")
        S.fx(b + 0.02, "click", 0.05)
    # hand-off: the PREVIEW card widens (S24 montage)
    S.ft(f"#{s}-card", {"scale": sw / cw, "x": sx - cx, "y": sy - cy}, {"scale": sw / cw * 1.08, "x": sx - cx - 10, "y": sy - cy - 10}, t1 - 0.3, 0.3, "power2.in")

    # ---------------------------------------------------------------- mascot: below, hands the brief over
    v = {"fx": 540, "fy": 1760, "h": 800, "yaw": 4, "pitch": 6}
    S.mv([(t0, v, None), (t1, dict(v, yaw=-4), "sine.inOut")])
    S.act("armL", [(t0, "present", 0.3), (W117 - 0.15, "present", 0.3), (W119 - 0.12, "pointUp", 0.3), (W122, "explain", 0.35), (W124 - 0.1, "low", 0.4)])
    S.act("armR", [(t0, "low", 0.3), (W117 - 0.1, "palmUp", 0.3), (W120 + 0.2, "low", 0.4), (W124 - 0.12, "explain", 0.3), (t1 - 0.2, "low", 0.4)])
    S.act("head", [(t0, [-0.14, 0.08, 0.02], 0.3), (W117, [-0.18, -0.06, 0], 0.35), (W119, [-0.2, 0.18, -0.02], 0.35),
                   (W122, [-0.06, 0.02, 0.04], 0.35), (W124, [-0.08, -0.08, 0], 0.35)])
