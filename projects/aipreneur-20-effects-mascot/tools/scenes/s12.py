"""S12 — 11 PAPER CUTOUT (23.43–24.73)  VO: "Karakter berubah jadi potongan kertas,"
Wide shot, full body on a paper diorama (navy cardstock arches, cyan paper sun, cream floor strip).
"Karakter": the paper set slides into place layer by layer (magnetised settle). "berubah": the live 3D mascot
flips edge-on like a card; at 90° it becomes a flat paper cut-out (white cut margin, card layer, cast shadow)
and flips back flat, with a small wobble settle. Hand-off: on "kertas," the cream floor strip stretches and its
top edge lights — S13 opens on the same strip, which becomes the dolly rail."""
from xk import box, r3, apex, CYAN
from kit import WIDE, FLOOR_Y, PAPER_FILTER, NO_FILTER, paper_strip, diorama, ARCHES

SFX = []


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W63, W64, W65, W66, W67 = S.W(63), S.W(64), S.W(65), S.W(66), S.W(67)   # 23.50 23.90 24.24 24.42 24.78
    flip = W64 + 0.02
    # ---------------------------------------------------------------- back: paper diorama
    S.back += diorama(s)
    # floor: cream strip with thickness = the edge that becomes the rail in S13
    S.back.append(paper_strip(f"{s}-floor", -40, FLOOR_Y - 10, 1160, 70))
    S.back.append(f'<div class="abs glowline" id="{s}-edge" style="{box(-40, FLOOR_Y - 12, 1160, 4)}"></div>')
    # cut marks (scissor dashes) around where the cut-out will sit
    S.back.append(f'<div class="abs" id="{s}-cut" style="{box(250, 520, 580, 1230)}border-radius:280px 280px 60px 60px;border:3px dashed rgba(255,255,255,.55)"></div>')
    # ---------------------------------------------------------------- front: foreground paper (parallax)
    S.front.append(paper_strip(f"{s}-fg0", -70, 1590, 360, 120, color="#22c8f5", rot=-8))
    S.front.append(paper_strip(f"{s}-fg1", 820, 1620, 330, 96, color="#f1ece1", rot=6))
    S.front.append(f'<div class="abs" id="{s}-star" style="{box(842, 560, 90, 90)}background:#fbf8f1;clip-path:polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);'
                   f'filter:drop-shadow(5px 7px 0 rgba(6,14,36,.5))"></div>')
    apex(S, S.front, f"{s}-ap", 540, 1000, flip + 0.12, size=720, sparks=8, seed=1201, op=0.45)

    # ---------------------------------------------------------------- motion
    # magnetised placement: each paper layer slides up and settles with a slight overshoot ("Karakter")
    for k, (i, *_r) in enumerate(ARCHES):
        S.init(f"#{s}-{i}", {"y": 420, "rotation": -4 + 2 * k})
        S.ft(f"#{s}-{i}", {"y": 420, "rotation": -4 + 2 * k}, {"y": 0, "rotation": 0}, t0 + 0.02 + k * 0.06, 0.42, "back.out(1.6)")
    S.init(f"#{s}-sun", {"scale": 0.2, "rotation": -40})
    S.ft(f"#{s}-sun", {"scale": 0.2, "rotation": -40}, {"scale": 1, "rotation": 0}, t0 + 0.05, 0.5, "back.out(1.7)")
    S.keys(f"#{s}-floor", [(t0, {"y": 0, "scaleX": 1, "transformOrigin": "50% 0%"}, None),
                           (W67, {"scaleX": 1}, "none"), (t1, {"scaleX": 1.18}, "power2.in")])
    S.init(f"#{s}-edge", {"opacity": 0, "scaleX": 0.2})
    S.ft(f"#{s}-edge", {"opacity": 0, "scaleX": 0.2}, {"opacity": 1, "scaleX": 1.2}, W66 + 0.1, 0.3, "power2.out")
    S.init(f"#{s}-cut", {"opacity": 0, "scale": 1.06})
    S.ft(f"#{s}-cut", {"opacity": 0, "scale": 1.06}, {"opacity": 1, "scale": 1}, W63 + 0.05, 0.25, "power2.out")
    S.ft(f"#{s}-cut", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.97}, flip, 0.12, "power2.in")
    for k, i in enumerate(("fg0", "fg1")):
        S.init(f"#{s}-{i}", {"y": 300})
        S.ft(f"#{s}-{i}", {"y": 300}, {"y": 0}, t0 + 0.12 + k * 0.05, 0.45, "back.out(1.4)")
        S.ft(f"#{s}-{i}", {"y": 0}, {"y": 26}, t0 + 0.6, t1 - t0 - 0.6, "sine.inOut")
    S.init(f"#{s}-star", {"scale": 0, "rotation": -90})
    S.ft(f"#{s}-star", {"scale": 0, "rotation": -90}, {"scale": 1, "rotation": 0}, flip + 0.15, 0.35, "back.out(2.4)")
    S.cam([(t0, {"y": 0, "scale": 1.0}, None), (t1, {"y": -14, "scale": 1.02}, "sine.inOut")])

    # ---------------------------------------------------------------- mascot: 3D -> card flip -> flat paper cut-out
    v = dict(WIDE)
    S.mv([(t0, dict(v, yaw=-10), None), (flip, dict(v, yaw=0), "power2.inOut"), (t1, dict(v, yaw=0), "none")])
    S.mx([(t0, {"rotationY": 0, "rotation": 0, "y": 0, "scale": 1, "transformOrigin": "540px 1200px", "transformPerspective": 1400, "filter": NO_FILTER}, None),
          (flip - 0.13, {"rotationY": 0}, "none"),
          (flip, {"rotationY": 90}, "power2.in")])
    S.mset("#m-xf", {"filter": PAPER_FILTER}, flip)
    S.mx([(flip, {"rotationY": -90, "rotation": -3, "y": -30}, None),
          (flip + 0.26, {"rotationY": 0, "rotation": 1.2, "y": 0}, "back.out(1.5)"),
          (flip + 0.6, {"rotation": 0}, "sine.out")])
    S.mx([(flip + 0.6, {"rotation": 0, "y": 0, "rotationY": 0}, None), (t1, {"y": -6, "rotation": -0.6}, "sine.inOut")])
    S.fx(flip - 0.05, "whoosh", 0.06)
    S.fx(flip + 0.18, "pop", 0.07)
    S.fx(W67 + 0.05, "click", 0.05)
