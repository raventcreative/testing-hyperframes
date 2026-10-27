"""S13 — 12 DOLLY ZOOM (24.73–25.57)  VO: "kertas, masuk"
Opens on S12's exact set (same arches, sun, cream floor strip, paper cut-out mascot). The floor strip folds down
and its top edge becomes the two satin-metal rails of a dolly track running toward the camera. The camera dollies
in along the rails (sleepers stream past underneath, foreground paper slides out of frame) while the lens zooms
out: the paper set behind the mascot recedes by depth (sun farthest -> shrinks most) and the mascot keeps its size
-> vertigo. Hand-off: a white viewfinder frame locks onto the magazine-cover rect; outside it the world dims."""
import math
from xk import box, r3
from kit import WIDE, FLOOR_Y, PAPER_FILTER, paper_strip, diorama, ARCHES, corner_frame, COVER

VP = (540, 1560)        # vanishing point of the rails / dolly axis (on the subject plane, behind the feet)


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W68 = S.W(68)                       # masuk 25.32
    d0, d1 = t0 + 0.12, t1 - 0.12       # dolly move
    S.back += diorama(s)
    # floor strip (identical to S12's end state: scaleX 1.18 around its centre)
    S.back.append(paper_strip(f"{s}-floor", -40, FLOOR_Y - 10, 1160, 70))
    # rails: satin-metal lines from the strip edge toward the camera, converging on VP
    rails = []
    for k, (xa, xb) in enumerate(((452, -60), (628, 1140))):
        rails.append(f'<line id="{s}-r{k}" x1="{xa}" y1="{FLOOR_Y - 8}" x2="{xb}" y2="1990" stroke="url(#{s}-mg)" stroke-width="{12 if k else 12}" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>')
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
                  f'<defs><linearGradient id="{s}-mg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8b97aa"/><stop offset=".45" stop-color="#f1f4f8"/><stop offset="1" stop-color="#9aa6b8"/></linearGradient></defs>'
                  + "".join(rails) + "</svg>")
    # sleepers (ties): perspective-spaced bars between the rails; they stream toward camera during the dolly
    NS = 7
    for k in range(NS):
        S.back.append(f'<div class="abs metal" id="{s}-t{k}" style="{box(VP[0] - 300, FLOOR_Y + 20, 600, 16)}border-radius:4px;opacity:0"></div>')
    S.front.append(paper_strip(f"{s}-fg0", -70, 1590, 360, 120, color="#22c8f5", rot=-8))
    S.front.append(paper_strip(f"{s}-fg1", 820, 1620, 330, 96, color="#f1ece1", rot=6))
    # dim matte outside the cover rect + viewfinder corners (front, above the mascot)
    x, y, w, h = COVER
    S.front.append(f'<div class="abs" id="{s}-matte" style="{box(x, y, w, h)}border-radius:6px;box-shadow:0 0 0 2400px rgba(6,13,36,.82)"></div>')
    S.front.append(f'<div class="abs" id="{s}-vf" style="{box(0, 0, 1080, 1920)}">' + corner_frame(f"{s}-vf", x - 8, y - 8, w + 16, h + 16, arm=90, th=6) + "</div>")
    S.front.append(f'<div class="abs" id="{s}-rec" style="{box(x + w - 150, y + 26, 120, 30)}font:700 22px/30px Poppins;color:#fff;letter-spacing:.12em;text-align:right">'
                   f'<span style="display:inline-block;width:12px;height:12px;border-radius:6px;background:#00D0FE;margin-right:8px;vertical-align:1px"></span>REC</div>')

    # ---------------------------------------------------------------- motion
    S.cam([(t0, {"y": -14, "scale": 1.02}, None), (t1, {"y": -14, "scale": 1.02}, "none")])
    S.init(f"#{s}-floor", {"scaleX": 1.18, "scaleY": 1, "transformOrigin": "50% 0%"})
    S.ft(f"#{s}-floor", {"scaleX": 1.18, "scaleY": 1}, {"scaleX": 1.18, "scaleY": 0}, t0 + 0.02, 0.16, "power2.in")
    for k in range(2):
        S.init(f"#{s}-r{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-r{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, t0 + 0.04, 0.22, "power3.out")
    # sleepers: positions along the rail parameter u (0 = at the feet, 1 = at the camera); they flow toward camera
    span = 1990 - (FLOOR_Y - 8)
    def tie(u):
        yy = FLOOR_Y - 8 + span * u ** 1.7
        gap = 176 + 1024 * (yy - (FLOOR_Y - 8)) / span          # distance between the rails at this depth
        sc = gap * 1.3 / 600
        return {"y": r3(yy - (FLOOR_Y + 20)), "scaleX": r3(sc), "scaleY": r3(0.35 + 1.4 * u ** 1.7), "opacity": 1}
    for k in range(NS):
        ua = k / NS
        ub = ua + 0.55 / NS * 1.6
        S.init(f"#{s}-t{k}", dict(tie(ua), opacity=0))
        S.tset(f"#{s}-t{k}", {"opacity": 1}, t0 + 0.06 + k * 0.008)
        S.ft(f"#{s}-t{k}", tie(ua), tie(min(1.0, ub)), d0, d1 - d0, "power1.inOut")
    # dolly zoom: background layers shrink toward the vanishing point by depth; subject constant
    depth = {"sun": 0.55, "a1": 0.74, "a0": 0.78, "a3": 0.86, "a2": 0.88}
    for i, sc in depth.items():
        ox = VP[0] - {"sun": 300, "a0": -120, "a1": 560, "a2": -60, "a3": 600}[i]
        oy = VP[1] - {"sun": 420, "a0": 980, "a1": 900, "a2": 1180, "a3": 1240}[i]
        S.init(f"#{s}-{i}", {"scale": 1, "transformOrigin": f"{r3(ox)}px {r3(oy)}px"})
        S.ft(f"#{s}-{i}", {"scale": 1}, {"scale": sc}, d0, d1 - d0, "power2.inOut")
    # foreground (closer than the subject) grows and slides out under the camera
    for k, (i, dx) in enumerate((("fg0", -260), ("fg1", 260))):
        S.init(f"#{s}-{i}", {"y": 26, "x": 0, "scale": 1})
        S.ft(f"#{s}-{i}", {"y": 26, "x": 0, "scale": 1}, {"y": 420, "x": dx, "scale": 1.9}, d0, d1 - d0, "power2.in")
    # viewfinder locks on the cover rect ("masuk"), world outside dims
    S.init(f"#{s}-matte", {"opacity": 0})
    S.ft(f"#{s}-matte", {"opacity": 0}, {"opacity": 1}, W68 - 0.06, 0.26, "power2.inOut")
    S.init(f"#{s}-vf", {"opacity": 0, "scale": 1.18, "transformOrigin": f"{x + w / 2}px {y + h / 2}px"})
    S.ft(f"#{s}-vf", {"opacity": 0, "scale": 1.18}, {"opacity": 1, "scale": 1}, W68 - 0.1, 0.24, "power3.out")
    S.init(f"#{s}-rec", {"opacity": 0})
    S.ft(f"#{s}-rec", {"opacity": 0}, {"opacity": 1}, W68 + 0.06, 0.1, "none")

    # ---------------------------------------------------------------- mascot: paper cut-out keeps its size (dolly zoom subject)
    S.mv([(t0, dict(WIDE), None), (t1, dict(WIDE, pitch=7), "power1.inOut")])
    S.mx([(t0, {"y": -6, "rotation": -0.6, "transformOrigin": "540px 1200px", "transformPerspective": 1400, "filter": PAPER_FILTER}, None),
          (t1, {"y": 0, "rotation": 0}, "sine.inOut")])
    S.fx(t0 + 0.05, "whoosh", 0.05)
    S.fx(W68 - 0.02, "click", 0.06)
