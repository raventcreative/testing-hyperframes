"""S08 — GSAP MOTION ENGINE (18.32–20.22)  VO: "GSAP ngatur geraknya,"
Hero = the user's navy dial photo, split into parts (tools/assets_dial.py): plate (needle painted out, gear window
cut), window gears (rectified, they turn), needle (rectified, turns on the hub) and the hub cap on top.
The dial plane is a circle seen at an angle: the turning parts live in a wrapper carrying the fitted affine
(rotate 6deg . scaleX .8628), so every rotation stays on the dial's own plane.
Opens on S07's grown drive gear (560 px round at 590,930) -> the scalloped dial at the same place, growing to
full size. "GSAP": keyframe pins pop on the tick ring, the needle swings back and kicks pin to pin
(keyframes), then one accelerate/decelerate sweep with the gears turning in sync and a glass easing graph
drawing the same curve; the needle lands EXACTLY on "geraknya" with a small settle + apex.
End: pins/label/graph clear, the dial spins down to 560 px = S09's sprocket drum."""
import json, math
from pathlib import Path
from xk import box, shadow, apex, r3
from kit_b import backdrop, near_blur, ease_io

SFX = [(18.66, "key", 0.07), (18.98, "key", 0.07), (19.44, "click", 0.12)]

META = json.loads((Path(__file__).resolve().parents[2] / "assets/elements/xray/dial/dial.json").read_text())
PX, PY = META["pivot"]                      # hub (photo px)
CX, CY = 590, 930                           # hub on screen
K = 0.72                                    # photo px -> screen px (bezel ~720 px)
OPEN = 560 / 720                            # S07's gear size
D = "assets/elements/xray/dial/"
AFF = f'transform:rotate({META["rot_deg"]}deg) scaleX({r3(META["scale_x"])});transform-origin:{PX}px {PY}px'
TH0 = 90 + META["needle_angle_deg"]         # needle clock angle in the photo (~44.6 deg)
PINS = [-110, -75, -40, -5, 30, 65, 100]     # keyframe pins (clock angles on the dial plane)
PR = 272                                    # pin radius (dial plane px)


def clock_xy(a, r):
    t = math.radians(a)
    return PX + r * math.sin(t), PY - r * math.cos(t)


def photo_to_screen(x, y):
    """dial-plane point -> photo (affine) -> screen."""
    dx, dy = (x - PX) * META["scale_x"], (y - PY)
    c, s_ = math.cos(math.radians(META["rot_deg"])), math.sin(math.radians(META["rot_deg"]))
    px, py = PX + dx * c - dy * s_, PY + dx * s_ + dy * c
    return CX + (px - PX) * K, CY + (py - PY) * K


def build(S):
    s = S.id
    S.persp_origin = (590, 640)
    W40, W41, W42 = S.W(40), S.W(41), S.W(42)        # GSAP 18.42, ngatur 19.12, geraknya 19.44
    end = S.t1
    backdrop(S, seed=8)
    S.mid.append(shadow(CX - 300, CY + 330, 640, 110, 0.75, soft=True, id_=f"{s}-csh"))

    # ------------------------------------------------------------------ the dial (photo space inside)
    bx, by, bw, bh = META["base_win_box"]
    gears = ""
    for nm, m in META["gears"].items():
        cx, cy = m["c_rect"]; z = m["size"]
        gears += f'<div class="abs" id="{s}-{nm}" style="{box(cx - z / 2, cy - z / 2, z, z)}"><img src="{D}{nm}.png" alt="" style="width:{z}px;height:{z}px;display:block" /></div>'
    pins = ""
    for k, a in enumerate(PINS):
        x, y = clock_xy(a, PR)
        pins += (f'<div class="abs" id="{s}-pin{k}" style="{box(x - 15, y - 15, 30, 30)}border-radius:50%;'
                 f'background:radial-gradient(circle at 38% 32%,#ffffff,#e8f0fb 45%,#acc6e7);box-shadow:0 0 0 3px rgba(28,51,84,.55),0 3px 6px rgba(0,0,0,.35)"></div>'
                 f'<div class="abs" id="{s}-pl{k}" style="{box(x - 15, y - 15, 30, 30)}border-radius:50%;'
                 f'background:radial-gradient(circle at 38% 32%,#f2fffa,#bfe9da 45%,#9fd8c4);box-shadow:0 0 0 3px rgba(28,51,84,.55),0 0 18px 6px rgba(159,216,196,.75)"></div>')
    lx, ly = PX, PY - 178
    label = (f'<div class="abs" id="{s}-lab" style="left:{lx - 160}px;top:{ly - 34}px;width:320px;text-align:center;'
             f'font:900 62px/68px Montserrat;letter-spacing:.14em;color:#e8f0fb;text-shadow:0 -1px 0 rgba(0,0,0,.45),0 2px 0 rgba(172,198,231,.35)">GSAP</div>')
    N = META["needle_sq"]
    needle = f'<div class="abs" id="{s}-ndl" style="{box(PX - N / 2, PY - N / 2, N, N)}"><img src="{D}needle.png" alt="" style="width:{N}px;height:{N}px;display:block" /></div>'
    hx, hy, hs = META["hub_box"]
    dial = (f'<img class="abs" src="{D}base_win.png" alt="" style="{box(bx, by, bw, bh)}" />'
            f'<div class="abs" style="{box(0, 0, 1254, 1254)}{AFF}">{gears}</div>'
            f'<img class="abs" src="{D}plate.png" alt="" style="{box(0, 0, 1254, 1254)}" />'
            f'<div class="abs" style="{box(0, 0, 1254, 1254)}{AFF}">{pins}{label}{needle}</div>'
            f'<img class="abs" src="{D}hub.png" alt="" style="{box(hx, hy, hs, hs)}" />')
    # static placement (scale K about the hub) on a wrapper; GSAP animates the inner group only
    S.mid.append(f'<div class="abs" style="left:{r3(CX - PX)}px;top:{r3(CY - PY)}px;width:1254px;height:1254px;transform:scale({K});transform-origin:{PX}px {PY}px">'
                 f'<div class="abs" id="{s}-dial" style="{box(0, 0, 1254, 1254)}">{dial}</div></div>')

    # ------------------------------------------------------------------ easing graph plate (glass, front)
    GX, GY, GW, GH = 772, 448, 236, 176
    gpts = [(GX + 26 + (GW - 50) * u, GY + GH - 28 - (GH - 60) * ease_io(u, 3.0)) for u in [k / 24 for k in range(25)]]
    gd = "M" + " L".join(f"{r3(x)},{r3(y)}" for x, y in gpts)
    steps = "".join(f'<div class="abs" id="{s}-st{k}" style="{box(GX + 26 + 30 * k - 6, GY + GH - 28 - 14 * k - 6, 12, 12)}border-radius:50%;background:#294b77;box-shadow:0 0 0 3px #ffffff"></div>' for k in range(3))
    S.near.append(f'<div class="abs" id="{s}-graph" style="{box(0, 0, 1080, 1920)}">'
                  f'<div class="abs glass" style="{box(GX, GY, GW, GH)}border-radius:20px"></div>'
                  f'<svg class="abs" style="{box(0, 0, 1080, 1920)}overflow:visible" viewBox="0 0 1080 1920">'
                  f'<path d="M{GX + 26},{GY + 22} L{GX + 26},{GY + GH - 28} L{GX + GW - 20},{GY + GH - 28}" fill="none" stroke="#acc6e7" stroke-width="2.5"/>'
                  f'<path d="M{GX + 26},{GY + GH - 28} L{GX + GW - 20},{GY + 30}" fill="none" stroke="#cbdbf4" stroke-width="2" stroke-dasharray="4 6"/>'
                  f'<path id="{s}-gcurve" d="{gd}" fill="none" stroke="#294b77" stroke-width="5" stroke-linecap="round" stroke-dasharray="420" stroke-dashoffset="420"/></svg>'
                  f'{steps}<div class="abs" id="{s}-gdot" style="{box(gpts[0][0] - 9, gpts[0][1] - 9, 18, 18)}border-radius:50%;background:#ffffff;box-shadow:0 0 0 5px #294b77,0 4px 8px rgba(28,51,84,.35)"></div></div>')
    near_blur(S, [(f"{s}-n1", -60, 600, 190, 190, "border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"),
                  (f"{s}-n2", 860, 1440, 260, 28, "border-radius:14px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px)")])
    tipx, tipy = photo_to_screen(*clock_xy(PINS[-1], PR + 20))
    apex(S, S.near, f"{s}-ap", tipx, tipy, W42, size=420, ring=True, sparks=8, seed=13, op=0.85)

    # ================================================================== motion
    S.cam([(S.t0, {"z": 0, "rotationY": 0, "rotationX": 0}, None),
           (W42, {"z": 55, "rotationY": -3, "rotationX": 1.5}, "sine.inOut"),
           (W42 + 0.18, {"z": 85}, "power3.out"),
           (end, {"z": 20, "rotationY": 0, "rotationX": 0}, "power2.inOut")])
    # dial: grows out of S07's gear, a small scale punch on the landing, spins down to S09's drum size
    S.keys(f"#{s}-dial", [(S.t0, {"scale": OPEN, "rotation": -14, "transformOrigin": f"{PX}px {PY}px"}, None),
                          (S.t0 + 0.42, {"scale": 1.0, "rotation": 0}, "power3.out"),
                          (W42, {"scale": 1.0}, "none"),
                          (W42 + 0.07, {"scale": 1.04}, "power2.out"),
                          (W42 + 0.22, {"scale": 1.0}, "power2.inOut"),
                          (end - 0.34, {"scale": 1.0, "rotation": 0}, "none"),
                          (end, {"scale": OPEN, "rotation": 22}, "power3.in")])
    S.init(f"#{s}-csh", {"scaleX": OPEN, "opacity": 0.4})
    S.ft(f"#{s}-csh", {"scaleX": OPEN, "opacity": 0.4}, {"scaleX": 1, "opacity": 0.75}, S.t0, 0.42, "power3.out")

    # needle: rest pose (photo) -> back to the first keyframe -> 3 kicks -> one eased sweep landing on "geraknya"
    kicks = [W40 + 0.24, W40 + 0.40, W40 + 0.56]      # 18.66 / 18.82 / 18.98
    sw0 = kicks[-1] + 0.15                             # sweep 19.13 -> 19.44 (after the last kick settles)
    d0 = lambda a: a - TH0                            # clock angle -> sprite rotation
    nk = [(S.t0, {"rotation": d0(TH0), "transformOrigin": "50% 50%"}, None),
          (W40, {"rotation": d0(TH0 + 6)}, "power2.out"),                  # tiny anticipation
          (W40 + 0.2, {"rotation": d0(PINS[0] - 5)}, "power3.inOut"),
          (W40 + 0.26, {"rotation": d0(PINS[0])}, "power2.out")]
    for k, tk in enumerate(kicks):
        a = PINS[1 + k]
        nk += [(tk + 0.07, {"rotation": d0(a + 4)}, "power3.out"), (tk + 0.14, {"rotation": d0(a)}, "power2.inOut")]
    nk += [(sw0, {"rotation": d0(PINS[3])}, "none"),
           (W42, {"rotation": d0(PINS[-1])}, "power3.inOut"),
           (W42 + 0.08, {"rotation": d0(PINS[-1] + 5)}, "power2.out"),
           (W42 + 0.3, {"rotation": d0(PINS[-1])}, "power2.inOut"),
           (end, {"rotation": d0(PINS[-1] + 3)}, "sine.inOut")]
    S.keys(f"#{s}-ndl", nk)

    # gears turn with the needle (meshing directions/ratios; gold wheel stays within ~24 deg)
    gk = {"gear_a": 1.0, "gear_b": -128 / 62, "gear_c": 128 / 50 * 0.8, "gear_d": 128 / 24 * 0.6}
    for nm, ratio in gk.items():
        g = [(S.t0, {"rotation": 0}, None), (W40, {"rotation": 1.5 * ratio}, "sine.inOut")]
        r = 1.5
        for tk in kicks:
            r += 4
            g.append((tk + 0.1, {"rotation": r * ratio}, "power3.out"))
        r += 12
        g += [(sw0, {"rotation": (r - 12) * ratio}, "none"), (W42, {"rotation": r * ratio}, "power3.inOut"),
              (W42 + 0.3, {"rotation": (r + 1) * ratio}, "power2.out"), (end, {"rotation": (r + 3) * ratio}, "sine.inOut")]
        S.keys(f"#{s}-{nm}", g)

    # keyframe pins pop on "GSAP"; each lights mint when the needle reaches it
    hits = [W40 + 0.26] + [tk + 0.07 for tk in kicks] + [sw0 + 0.18, sw0 + 0.27, W42]
    for k in range(len(PINS)):
        S.init(f"#{s}-pin{k}", {"scale": 0})
        S.ft(f"#{s}-pin{k}", {"scale": 0}, {"scale": 1}, W40 + 0.03 * k, 0.26, "back.out(2.6)")
        S.init(f"#{s}-pl{k}", {"opacity": 0, "scale": 0.6})
        S.ft(f"#{s}-pl{k}", {"opacity": 0, "scale": 0.6}, {"opacity": 1, "scale": 1.15}, hits[k], 0.08, "power2.out")
        S.ft(f"#{s}-pl{k}", {"scale": 1.15}, {"scale": 1}, hits[k] + 0.08, 0.16, "power2.out")
        S.ft(f"#{s}-pin{k}", {"scale": 1}, {"scale": 0}, end - 0.36 + 0.015 * k, 0.16, "power2.in")
        S.ft(f"#{s}-pl{k}", {"opacity": 1}, {"opacity": 0}, end - 0.36 + 0.015 * k, 0.16, "power2.in")
    S.init(f"#{s}-lab", {"opacity": 0, "scale": 0.82, "y": 10})
    S.ft(f"#{s}-lab", {"opacity": 0, "scale": 0.82, "y": 10}, {"opacity": 1, "scale": 1, "y": 0}, W40 - 0.02, 0.3, "power3.out")
    S.ft(f"#{s}-lab", {"opacity": 1}, {"opacity": 0}, end - 0.34, 0.18, "power2.in")

    # graph plate: slides in on "GSAP"; 3 step dots on the kicks; the in-out curve draws during the sweep
    S.init(f"#{s}-graph", {"x": 60, "opacity": 0, "rotationY": -24})
    S.ft(f"#{s}-graph", {"x": 60, "opacity": 0, "rotationY": -24}, {"x": 0, "opacity": 1, "rotationY": 0}, W40 + 0.05, 0.36, "power3.out")
    S.ft(f"#{s}-graph", {"opacity": 1, "x": 0}, {"opacity": 0, "x": 40}, end - 0.34, 0.24, "power2.in")
    for k, tk in enumerate(kicks):
        S.init(f"#{s}-st{k}", {"scale": 0})
        S.ft(f"#{s}-st{k}", {"scale": 0}, {"scale": 1}, tk + 0.05, 0.18, "back.out(3)")
    S.init(f"#{s}-gcurve", {"strokeDashoffset": 420})
    S.ft(f"#{s}-gcurve", {"strokeDashoffset": 420}, {"strokeDashoffset": 0}, sw0, W42 - sw0, "none")
    n, prev = 12, None
    for k in range(n + 1):
        u = k / n
        cur = {"x": r3((GW - 50) * u), "y": r3(-(GH - 60) * ease_io(u, 3.0))}
        if prev is None:
            S.init(f"#{s}-gdot", cur)
        else:
            a_ = round(sw0 + (W42 - sw0) * (k - 1) / n, 3); b_ = round(sw0 + (W42 - sw0) * k / n, 3)   # no 1 ms overlaps
            S.ft(f"#{s}-gdot", prev, cur, a_, b_ - a_ - 0.001, "none")
        prev = cur
