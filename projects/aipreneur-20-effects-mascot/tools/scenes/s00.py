"""S00 — COLD OPEN (0.00–3.40)  VO: "Satu klip polos. Dua puluh efek. Lihat hasilnya."
Proof before explanation: three hard-cut micro previews of OUR results (01 Orbit, 11 Paper Cutout, 17 Frame Break,
self-shots cropped to the exact panel rect) on a punch-in, each tagged with its effect chip. "polos": the last
preview gives way to ONE plain clip (the live mascot, medium, in a flat panel). "Dua puluh efek": the camera pulls
back (panel + mascot scale as one), 20 numbered cyan-acrylic chips burst out into a ring and `20 EFEK` lands below.
"Lihat hasilnya": the chips orbit and collapse into the panel while the camera pushes back in -> S01 opens on the
identical panel."""
import math
from xk import box, r3, CYAN, clip_rect
from kit import PANEL, MED, SELF
from kit_a import panel_bg, panel_border, panel_label, PX, PY, PW, PH, PR

PREV = [("orbit", "01", "ORBIT"), ("paper", "11", "PAPER CUTOUT"), ("break", "17", "FRAME BREAK")]
ORG = (540, 700)                 # pull-back origin (panel + mascot scale around it)
PULL = 0.66
RC, RX, RY = (540, 790), 420, 410   # chip ring


def build(S):
    s = S.id
    t1 = S.t1
    W2, W3, W5, W6, W7 = S.W(2), S.W(3), S.W(5), S.W(6), S.W(7)   # polos .68  Dua 1.36  efek 1.82  Lihat 2.32  hasilnya 2.58
    plain = W2 - 0.06
    pb0, pb1 = W3 - 0.1, W3 + 0.22          # pull back
    pi0, pi1 = t1 - 0.48, t1                     # push back in (lands on the S01 panel)
    # ---------------------------------------------------------------- back: plain panel group (scales with the camera pull)
    S.back.append(f'<div class="abs" id="{s}-pg" style="{box(0, 0, 1080, 1920)}">{panel_bg(f"{s}-pbg")}</div>')
    # micro previews: self-shots cropped pixel-exact to the panel rect
    for k, (name, n, lab) in enumerate(PREV):
        S.back.append(f'<div class="abs" id="{s}-pv{k}" style="{box(PX, PY, PW, PH)}border-radius:{PR}px;overflow:hidden;'
                      f'background:#0b1636 url({SELF}/{name}_full.jpg) {-PX}px {-PY}px / 1080px 1920px no-repeat;box-shadow:0 40px 80px -30px rgba(3,8,28,.9)"></div>')
    # ---------------------------------------------------------------- front: border/label (scale group), preview tags, chips, big type
    S.front.append(f'<div class="abs" id="{s}-pf" style="{box(0, 0, 1080, 1920)}">{panel_border(f"{s}-pbd")}{panel_label(f"{s}-plb")}</div>')
    for k, (name, n, lab) in enumerate(PREV):
        S.front.append(f'<div class="abs acrylic chip" id="{s}-tag{k}" style="{box(PX + 34, PY + PH - 200, 60 + 20 * len(lab), 64)}font-size:26px;gap:12px">'
                       f'<span style="color:{CYAN}">{n}</span><span>{lab}</span></div>')
    for k in range(20):
        a = math.radians(-90 + k * 18)
        S.front.append(f'<div class="abs acrylic chip" id="{s}-c{k}" style="{box(RC[0] - 46, RC[1] - 26, 92, 52)}font-size:26px">{k + 1:02d}</div>')
    S.front.append(f'<div class="abs" id="{s}-big" style="{box(0, 1252, 1080, 140)}font:700 128px/140px Poppins, sans-serif;text-align:center;color:#fff;'
                   f'letter-spacing:-0.02em;text-shadow:0 8px 30px rgba(3,8,28,.7)"><span style="color:{CYAN}">20</span> EFEK</div>')

    # ---------------------------------------------------------------- motion: previews (hard cuts on a punch-in)
    cuts = [0.0, 0.2, 0.4, plain]
    for k in range(3):
        a, b = cuts[k], cuts[k + 1]
        for sel in (f"#{s}-pv{k}", f"#{s}-tag{k}"):
            S.init(sel, {"opacity": 1 if k == 0 else 0})
            if k:
                S.tset(sel, {"opacity": 1}, a)
            S.tset(sel, {"opacity": 0}, b)
        S.ft(f"#{s}-pv{k}", {"scale": 1.07}, {"scale": 1.0}, a, b - a, "power3.out")
        S.init(f"#{s}-tag{k}", {"x": -40})
        S.ft(f"#{s}-tag{k}", {"x": -40}, {"x": 0}, a, 0.14, "power3.out")
    S.init(f"#{s}-pv0", {"scale": 1.07, "opacity": 1})
    S.init(f"#{s}-plb", {"opacity": 0})
    S.tset(f"#{s}-plb", {"opacity": 1}, plain)
    # camera pull-back / push-in: panel group + border group + mascot wrapper share origin, scale and ease
    for sel in (f"#{s}-pg", f"#{s}-pf"):
        S.keys(sel, [(0.0, {"scale": 1, "transformOrigin": f"{ORG[0]}px {ORG[1]}px"}, None),
                     (pb0, {"scale": 1}, "none"), (pb1, {"scale": PULL}, "power3.out"),
                     (pi0, {"scale": PULL}, "none"), (pi1, {"scale": 1}, "power2.in")])
    # 20 chips: burst out of the panel into a ring, orbit, collapse back into the panel
    for k in range(20):
        sel = f"#{s}-c{k}"
        def at(deg):
            a = math.radians(deg)
            return {"x": r3(RX * math.cos(a)), "y": r3(RY * math.sin(a))}
        a0 = -90 + k * 18
        S.init(sel, {"x": 0, "y": 26, "scale": 0, "opacity": 0, "rotation": 0})
        b = W3 + 0.02 + k * 0.022
        S.ft(sel, {"x": 0, "y": 26, "scale": 0, "opacity": 0}, dict(at(a0), scale=1, opacity=1), b, 0.36, "back.out(1.7)")
        prev = at(a0)
        seg = (pi0 - 0.01 - W6) / 3
        for j, dd in enumerate((12, 24, 34)):
            nxt = at(a0 + dd)
            S.ft(sel, prev, nxt, W6 + j * seg, seg, "none")
            prev = nxt
        S.ft(sel, dict(prev, scale=1, opacity=1), {"x": 0, "y": 26, "scale": 0.2, "opacity": 0}, pi0 + k * 0.008, 0.3, "power3.in")
    S.init(f"#{s}-big", {"opacity": 0, "y": 40})
    S.ft(f"#{s}-big", {"opacity": 0, "y": 40}, {"opacity": 1, "y": 0}, W3 + 0.12, 0.32, "power3.out")
    S.ft(f"#{s}-big", {"opacity": 1, "y": 0}, {"opacity": 0, "y": 30}, pi0, 0.2, "power2.in")

    # ---------------------------------------------------------------- mascot: hidden behind the previews, then the plain clip
    S.mv([(0.0, dict(MED, vis=0), None)])
    S.mset("V", {"vis": 1}, plain)
    S.mc([(0.0, {"clipPath": clip_rect(PX, PY, PW, PH, PR)}, None)])
    S.mx([(0.0, {"scale": 1, "transformOrigin": f"{ORG[0]}px {ORG[1]}px"}, None),
          (pb0, {"scale": 1}, "none"), (pb1, {"scale": PULL}, "power3.out"),
          (pi0, {"scale": PULL}, "none"), (pi1, {"scale": 1}, "power2.in")])
    # acting: present the plain clip, point up at the 20 chips, open hands on "Lihat hasilnya"
    S.act("armL", [(0.0, "low", 0.2), (W3 - 0.14, "pointUp", 0.3), (W5 + 0.2, "low", 0.4), (W6 - 0.12, "present", 0.32), (t1 - 0.45, "low", 0.4)])
    S.act("armR", [(0.0, "low", 0.2), (W6 - 0.1, "open", 0.32), (t1 - 0.45, "low", 0.4)])
    S.act("head", [(0.0, [0, 0, 0], 0.2), (plain, [-0.04, 0.06, 0.03], 0.3), (W3 - 0.05, [-0.12, 0.2, 0.0], 0.3),
                   (W6 - 0.05, [0.04, -0.06, -0.03], 0.3), (W7, [-0.02, 0.04, 0.02], 0.35)])
    S.act("torso", [(0.0, {}, 0.2), (W3 - 0.1, {"chest": [-0.04, 0.06, 0]}, 0.35), (W6, {"chest": [0.04, 0, 0]}, 0.35), (t1 - 0.45, {}, 0.4)])
    for k in range(3):
        S.fx(cuts[k] + 0.01, "click", 0.07)
    S.fx(W3 + 0.04, "whoosh", 0.06)
    S.fx(W3 + 0.2, "sparkle", 0.05)
    S.fx(pi0 + 0.05, "whoosh", 0.05)
