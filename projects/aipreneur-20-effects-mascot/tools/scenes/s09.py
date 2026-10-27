"""S09 — 08 GROWTH CURVE (15.23–17.43)  VO: "lalu keluar lewat grafik yang sedang naik."
Opens inside S08's portal world (graph_world() fills the frame). "keluar": the mascot comes out of the portal
toward camera (small -> full body) and lands on the matte grid floor. "lewat grafik yang sedang naik": a glowing
SVG curve draws from lower-left up to the top-right BEHIND the mascot (real occlusion), its nodes light segment by
segment, a soft area fill rises under it. The world tilts down slightly (camera looks up the curve) while the
mascot looks up along it and points. No numbers, no axis values. Hand-off: the curve tip glows at CABLE0 and
becomes the studio cable of S10."""
import math
from xk import box, r3, apex, CYAN
from kit import WIDE, NO_FILTER, CABLE0, graph_world

X0, Y0 = 60, 1500


def curve_pts(n=48):
    pts = []
    for k in range(n + 1):
        u = k / n
        pts.append((X0 + (CABLE0[0] - X0) * u, Y0 - (Y0 - CABLE0[1]) * (u ** 2.2)))
    return pts


def curve_svg(s, drawn=False):
    """the growth curve (area fill in a clip wrapper #{s}-areaw, glow, line). Shared with S10 (drawn=True)."""
    pts = curve_pts()
    off = 0 if drawn else 1
    clip = "inset(0px 0px 0px 0px)" if drawn else "inset(0px 1080px 0px 0px)"
    svg = '<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">'
    return (f'<div class="abs" id="{s}-areaw" style="left:0;top:0;width:1080px;height:1920px;clip-path:{clip}">{svg}'
            f'<defs><linearGradient id="{s}-fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00D0FE" stop-opacity=".30"/>'
            f'<stop offset="1" stop-color="#00D0FE" stop-opacity="0"/></linearGradient></defs>'
            f'<path d="{area}" fill="url(#{s}-fill)"/></svg></div>{svg}'
            f'<defs><linearGradient id="{s}-stroke" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#5fe3ff"/><stop offset="1" stop-color="#ffffff"/></linearGradient></defs>'
            f'<path id="{s}-glow" d="{d}" fill="none" stroke="#00D0FE" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" opacity=".28" '
            f'style="filter:blur(10px)" pathLength="1" stroke-dasharray="1" stroke-dashoffset="{off}"/>'
            f'<path id="{s}-line" d="{d}" fill="none" stroke="url(#{s}-stroke)" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" '
            f'pathLength="1" stroke-dasharray="1" stroke-dashoffset="{off}"/></svg>')


NODES = [0.16, 0.34, 0.52, 0.68, 0.82, 0.93]


def node_html(s, k, u, lit=False):
    pts = curve_pts()
    i = int(u * (len(pts) - 1))
    x, y = pts[i]
    st = "" if not lit else ""
    return (f'<div class="abs" id="{s}-n{k}" style="{box(x - 17, y - 17, 34, 34)}border-radius:50%;background:radial-gradient(circle at 38% 34%,#ffffff 0%,#9ff0ff 40%,#00D0FE 75%);'
            f'box-shadow:0 0 0 5px rgba(0,208,254,.25),0 0 22px rgba(0,208,254,.85)"></div>'
            f'<div class="abs" id="{s}-nd{k}" style="{box(x - 3, y + 17, 6, 1720 - y - 17)}background:linear-gradient(180deg,rgba(0,208,254,.55),rgba(0,208,254,0))"></div>')


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W41, W42, W43, W44, W46, W47 = S.W(41), S.W(42), S.W(43), S.W(44), S.W(46), S.W(47)  # lalu 15.32 keluar 15.54 lewat 15.86 grafik 16.12 sedang 16.60 naik 16.84
    pts = curve_pts()
    # arc-length fractions for node timing
    L = [0.0]
    for a, b in zip(pts, pts[1:]):
        L.append(L[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    tot = L[-1]
    draw0, draw1 = W43 - 0.05, W47 + 0.18          # the curve draws over "lewat grafik yang sedang naik"

    # ---------------------------------------------------------------- back: graph world + curve (behind the mascot)
    S.back.append(f'<div class="abs" id="{s}-world" style="{box(0, 0, 1080, 1920)}">' + graph_world(s) + curve_svg(s, drawn=False))
    node_t = []
    nodes_html = ""
    for k, u in enumerate(NODES):
        i = int(u * (len(pts) - 1))
        frac = L[i] / tot
        node_t.append(draw0 + (draw1 - draw0) * (1 - (1 - frac) ** 1.6))   # matches the power1.out draw below
        nodes_html += node_html(s, k, u)
    # nodes live inside the moving world (same transform as the curve)
    # glowing tip at CABLE0 (hand-off)
    tip = f'<div class="abs" id="{s}-tip" style="{box(CABLE0[0] - 30, CABLE0[1] - 30, 60, 60)}border-radius:50%;background:radial-gradient(circle,#ffffff 0%,#9ff0ff 35%,rgba(0,208,254,0) 70%)"></div>'
    S.back[-1] = S.back[-1][:-len("</div>")] + nodes_html + tip + "</div>"
    # portal ring remnant shrinking behind the mascot (we just came out of it)
    S.back.append(f'<div class="abs" id="{s}-ring" style="{box(540 - 280, 1050 - 280, 560, 560)}border-radius:50%;border:16px solid #c3ccd8;'
                  f'box-shadow:inset 0 0 0 5px rgba(0,208,254,.8),0 0 30px rgba(0,208,254,.45)"></div>')
    # ---------------------------------------------------------------- front: drifting data motes (depth) + contact shadow
    S.front.append(f'<div class="abs cshadow" id="{s}-sh" style="{box(330, 1690, 420, 70)}"></div>')
    for k, (x, y, sz) in enumerate(((120, 640, 14), (930, 860, 10), (210, 1240, 9), (860, 1290, 13), (980, 520, 8))):
        S.front.append(f'<div class="abs spark" id="{s}-m{k}" style="{box(x, y, sz, sz)}opacity:.7"></div>')
    apex(S, S.back, f"{s}-ap", CABLE0[0], CABLE0[1], draw1 + 0.02, size=380, ring=True, sparks=6, seed=903, op=0.55)

    # ---------------------------------------------------------------- motion
    # world tilts down slowly (camera looks up the curve); mascot stays framed (world-only move)
    S.init(f"#{s}-world", {"y": -70, "scale": 1.1, "transformOrigin": "540px 1100px"})
    S.ft(f"#{s}-world", {"y": -70, "scale": 1.1}, {"y": 0, "scale": 1.0}, t0, t1 - t0, "sine.inOut")
    S.init(f"#{s}-ring", {"scale": 1.0, "opacity": 1})
    S.ft(f"#{s}-ring", {"scale": 1.0, "opacity": 1}, {"scale": 0.25, "opacity": 0}, t0, 0.5, "power3.in")
    S.init(f"#{s}-line", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-line", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, draw0, draw1 - draw0, "power1.out")
    S.init(f"#{s}-glow", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-glow", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, draw0 + 0.04, draw1 - draw0, "power1.out")
    S.init(f"#{s}-areaw", {"clipPath": "inset(0px 1080px 0px 0px)"})
    S.ft(f"#{s}-areaw", {"clipPath": "inset(0px 1080px 0px 0px)"}, {"clipPath": "inset(0px 0px 0px 0px)"}, draw0, draw1 - draw0, "power1.out")
    for k, tn in enumerate(node_t):
        S.init(f"#{s}-n{k}", {"scale": 0, "opacity": 0})
        S.ft(f"#{s}-n{k}", {"scale": 0, "opacity": 0}, {"scale": 1, "opacity": 1}, tn, 0.22, "back.out(2.6)")
        S.init(f"#{s}-nd{k}", {"scaleY": 0, "transformOrigin": "50% 0%"})
        S.ft(f"#{s}-nd{k}", {"scaleY": 0}, {"scaleY": 1}, tn + 0.04, 0.3, "power2.out")
    S.init(f"#{s}-tip", {"scale": 0, "opacity": 0})
    S.ft(f"#{s}-tip", {"scale": 0, "opacity": 0}, {"scale": 1.4, "opacity": 1}, draw1 - 0.04, 0.2, "power2.out")
    S.ft(f"#{s}-tip", {"scale": 1.4, "opacity": 1}, {"scale": 1, "opacity": 1}, draw1 + 0.16, t1 - draw1 - 0.16, "sine.inOut")
    for k in range(5):
        S.init(f"#{s}-m{k}", {"y": 0})
        S.ft(f"#{s}-m{k}", {"y": 0}, {"y": -90 - 30 * k}, t0, t1 - t0, "none")
    S.init(f"#{s}-sh", {"opacity": 0, "scaleX": 0.4})
    S.ft(f"#{s}-sh", {"opacity": 0, "scaleX": 0.4}, {"opacity": 0.8, "scaleX": 1}, W42 + 0.05, 0.4, "power2.out")

    # ---------------------------------------------------------------- mascot: comes out of the portal, stands in the graph world
    v = dict(WIDE, yaw=-6)
    S.mv([(t0, v, None), (W44, dict(v, yaw=10), "power2.inOut"), (t1, dict(v, yaw=14), "sine.inOut")])
    S.mx([(t0, {"scale": 0.42, "y": -320, "opacity": 0, "transformOrigin": "540px 1720px", "filter": NO_FILTER}, None),
          (t0 + 0.08, {"opacity": 1}, "none"),
          (W42 + 0.3, {"scale": 1.0, "y": 0}, "power3.out")])
    # acting: lands, looks up along the curve, points at the rising tip
    S.act("root", [(t0 + 0.02, {"y": 0.04, "ry": 0}, 0.2), (W42 + 0.25, {"y": 0, "ry": 0.1}, 0.3), (W46, {"y": 0, "ry": 0.22}, 0.5)])
    S.act("head", [(t0 + 0.02, [0.05, 0, 0], 0.2), (W43, [-0.06, 0.18, 0.03], 0.35), (W44 + 0.1, [-0.14, 0.3, 0.02], 0.4),
                   (W47, [-0.2, 0.38, -0.02], 0.4)])
    S.act("armL", [(t0 + 0.02, "low", 0.3), (W44 - 0.12, "pointUp", 0.32), (W47 + 0.15, "present", 0.35)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W43, "open", 0.35), (W46, "low", 0.4)])
    S.act("torso", [(t0 + 0.02, {"spine": [0.04, 0, 0]}, 0.3), (W44, {"chest": [-0.05, 0.1, 0]}, 0.4)])
    S.fx(W42 + 0.05, "whoosh", 0.05)
    for k, tn in enumerate(node_t[::2]):
        S.fx(tn, "ping" if k == 2 else "click", 0.04)
    S.fx(draw1 + 0.02, "sparkle", 0.05)
