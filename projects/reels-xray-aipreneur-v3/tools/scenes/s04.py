"""S04 — THE CAMERA MOTION RAIL (7.22–10.42)
VO: "sampai gerak kamera ternyata punya lapisan masing-masing."
Hero = the user's navy/ivory cinema camera on its dolly rail (assets/elements/user/camera_rail.webp), split by
tools/assets_rail.py into a RAIL layer (rail rebuilt under the cart from its own rung period) and a DOLLY layer.
Opening: tight on the rail running up-right (continues S03's track), pull back to reveal the rig.
"gerak kamera": the dolly glides one-and-a-bit rungs toward us (anticipation, cart bob, wheel glints, mint tally,
lens glint); the viewer camera tracks it, so four glass scene layers hanging in depth in front of the lens
(sky / hills / product / caption frame) slide at different speeds = real perspective parallax.
"lapisan": the layer edges light up one after another. "masing-masing": the layers burst apart (apex: flash,
shockwave, sparkles, scale punch), then snap into one composed frame in front of the lens.
Hand-off: the camera pushes through that frame into the lens (zoom-through) and an exposure flash cuts to S05."""
import json
from pathlib import Path
from xk import box, shadow, apex, r3

SFX = [(7.56, "whoosh", 0.08), (9.24, "sparkle", 0.07), (9.76, "click", 0.10)]

P = Path(__file__).resolve().parents[2]
META = json.loads((P / "assets/elements/xray/rail/rail_meta.json").read_text())
PS, OX, OY = 0.74, 70, 520                      # photo -> screen: scale + origin of the rig
F = 2000                                        # perspective distance (xray.css .xr-persp)
O = (560, 760)                                  # perspective origin for this scene
PW_, PH_ = 250, 440                             # glass layer size (9:16-ish)
LAYERS = ["bg", "mid", "sub", "fg"]             # far from the lens -> near the viewer


def sp(x, y):
    """photo px -> screen px (rig at z=0)."""
    return OX + PS * x, OY + PS * y


def layer_inner(kind, w, h):
    if kind == "bg":   # sky
        return (f'<div class="abs" style="{box(0, 0, w, h)}border-radius:14px;background:linear-gradient(180deg,#e8f0fb,#cbdbf4 70%,#acc6e7)"></div>'
                f'<div class="abs" style="{box(w - 96, 46, 58, 58)}border-radius:50%;background:#fbfcfe;box-shadow:0 0 22px 6px rgba(255,255,255,.9)"></div>'
                + "".join(f'<div class="abs" style="{box(18, 150 + k * 36, w - 36, 2)}border-radius:1px;background:rgba(255,255,255,.7)"></div>' for k in range(5)))
    if kind == "mid":  # hills
        return (f'<svg class="abs" style="left:0;top:0" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
                f'<path d="M0,{h} L0,{h - 170} L60,{h - 240} L120,{h - 190} L185,{h - 280} L{w},{h - 200} L{w},{h} Z" fill="#acc6e7" opacity=".9"/>'
                f'<path d="M0,{h} L0,{h - 110} L80,{h - 175} L150,{h - 120} L{w},{h - 190} L{w},{h} Z" fill="#3a6299"/></svg>')
    if kind == "sub":  # product card
        return (f'<div class="abs" style="{box(64, 130, 122, 172)}border-radius:16px;background:linear-gradient(150deg,#3a6299,#1c3354);box-shadow:0 14px 20px -8px rgba(28,51,84,.5)"></div>'
                f'<div class="abs" style="{box(130, 146, 40, 40)}border-radius:50%;background:#9fd8c4;box-shadow:inset -4px -4px 0 rgba(28,51,84,.18)"></div>'
                f'<div class="abs" style="{box(82, 270, 64, 12)}border-radius:6px;background:#cbdbf4"></div>')
    return (f'<div class="abs" style="{box(26, h - 86, 170, 18)}border-radius:9px;background:#294b77"></div>'     # caption + frame
            f'<div class="abs" style="{box(26, h - 58, 120, 14)}border-radius:7px;background:#cbdbf4"></div>'
            + "".join(f'<div class="corner {c}" style="left:{x}px;top:{y}px"></div>' for c, (x, y) in
                      (("tl", (12, 12)), ("tr", (w - 38, 12)), ("bl", (12, h - 38)), ("br", (w - 38, h - 38)))))


def build(S):
    s = S.id
    S.persp_origin = O
    t0, t1 = S.t0, S.t1
    W14, W15, W16, W18, W19 = S.W(14), S.W(15), S.W(16), S.W(18), S.W(19)   # gerak 7.60 kamera 7.80 ternyata 8.26 lapisan 8.88 masing 9.24
    RB, DB = META["rail_box"], META["dolly_box"]
    RIGW = 1254 * PS
    cx, cy = META["contact"]
    lens = META["lens"]
    # ------------------------------------------------ dolly travel (photo px along the rail, toward the viewer)
    TRAVEL = 300
    ux, uy = META["rail_dir"]
    dx, dy = -ux * TRAVEL * PS, -uy * TRAVEL * PS            # screen offset of the move
    w_now = 159.8 - 0.0562 * (cx - 360)
    w_end = 159.8 - 0.0562 * (cx - ux * TRAVEL - 360)
    SC_END = w_end / w_now                                    # perspective growth of the dolly when it comes closer
    PRE = 26                                                  # starts slightly further back (anticipation room)
    pre_x, pre_y = ux * PRE * PS, uy * PRE * PS
    # final lens position (screen, z=0) -> where the composed frame forms and the push lands
    lx0, ly0 = sp(lens["cx"], lens["cy"])
    ccx, ccy = sp(cx, cy)
    LX = ccx + dx + (lx0 - ccx) * SC_END
    LY = ccy + dy + (ly0 - ccy) * SC_END

    # ================================================ far plane: studio wall, softbox, bokeh discs
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-560px) scale(1.28)">'
                 f'<div class="abs por-dim" style="{box(150, 430, 840, 1000)}border-radius:420px 420px 30px 30px;opacity:.55"></div>'
                 f'<div class="abs" style="{box(200, 490, 280, 180)}border-radius:20px;background:linear-gradient(160deg,#ffffff,#f4f7fc);box-shadow:0 0 70px 24px rgba(255,255,255,.95),inset 0 0 0 4px #e3ebf7"></div>'
                 + "".join(f'<div class="abs" style="{box(222 + k * 26, 510, 2, 140)}background:rgba(172,198,231,.45)"></div>' for k in range(10))
                 + f'<div class="abs" style="{box(110, 1440, 960, 6)}border-radius:3px;background:rgba(172,198,231,.55)"></div>'
                 + f'<div class="abs" style="{box(110, 1466, 960, 3)}border-radius:2px;background:rgba(172,198,231,.35)"></div></div>')
    for k, (bx, by, bs) in enumerate(((880, 470, 120), (960, 1120, 90), (120, 560, 70), (760, 1380, 60))):
        S.far.append(f'<div class="abs" id="{s}-bk{k}" style="{box(bx, by, bs, bs)}border-radius:50%;filter:blur(7px);opacity:.65;'
                     f'background:radial-gradient(circle at 35% 30%,#ffffff,#e8f0fb 45%,#acc6e7 100%)"></div>')

    # ================================================ hero: rail + dolly (photo layers)
    rail_shadow = (f'<div class="shadow" style="{box(RIGW * 0.06, RIGW * 0.66, RIGW * 0.94, 120)}opacity:.55;transform:translateZ(-3px) rotate(-24.2deg)"></div>')
    dolly_shadow = (f'<div class="shadow" id="{s}-dsh" style="{box((cx - 210) * PS, (cy - 40) * PS, 420 * PS, 150 * PS)}opacity:.6;transform:rotate(-24deg)"></div>')
    hubs = "".join(
        f'<div class="abs" style="{box((hx - hr) * PS, (hy - hr) * PS, 2 * hr * PS, 2 * hr * PS)}">'
        f'<div class="abs" id="{s}-hub{k}" style="{box(0, 0, 2 * hr * PS, 2 * hr * PS)}border-radius:50%;'
        f'background:conic-gradient(from 0deg,rgba(255,255,255,0) 0 40deg,rgba(255,255,255,.85) 52deg,rgba(255,255,255,0) 66deg,rgba(255,255,255,0) 220deg,rgba(255,255,255,.6) 232deg,rgba(255,255,255,0) 246deg)"></div></div>'
        for k, (hx, hy, hr) in enumerate(META["wheel_hubs"]))
    lr = lens["rx"] * PS
    lcx, lcy = lens["cx"] * PS, lens["cy"] * PS
    drawn_lens = (f'<div class="abs" id="{s}-dlens" style="{box(lcx - lr * 1.08, lcy - lr * 1.08, lr * 2.16, lr * 2.16)}border-radius:50%;'
                  f'background:radial-gradient(circle at 50% 50%,rgba(15,28,51,0) 0%,rgba(15,28,51,0) 46%,rgba(58,98,153,.28) 62%,rgba(159,216,196,.18) 74%,rgba(15,28,51,.3) 90%,rgba(15,28,51,0) 100%);'
                  f'box-shadow:inset 0 0 0 2px rgba(203,219,244,.45)">'
                  f'<div class="abs" style="{box(lr * 0.42, lr * 0.32, lr * 0.62, lr * 0.3)}border-radius:50%;background:rgba(255,255,255,.55);filter:blur(2px);transform:rotate(-28deg)"></div>'
                  f'<div class="abs" style="{box(lr * 1.3, lr * 1.32, lr * 0.3, lr * 0.16)}border-radius:50%;background:rgba(172,198,231,.6);filter:blur(1px);transform:rotate(-28deg)"></div></div>')
    rig = (f'<div class="abs p3" id="{s}-rig" style="{box(OX, OY, RIGW, RIGW)}">'
           f'{rail_shadow}'
           f'<img class="abs" id="{s}-rail" src="assets/elements/xray/rail/rail.png" alt="" style="{box(RB[0] * PS, RB[1] * PS, RB[2] * PS, RB[3] * PS)}"/>'
           f'<div class="abs p3" id="{s}-dolly" style="{box(0, 0, RIGW, RIGW)}">'
           f'{dolly_shadow}'
           f'<img class="abs" src="assets/elements/xray/rail/dolly.png" alt="" style="{box(DB[0] * PS, DB[1] * PS, DB[2] * PS, DB[3] * PS)}"/>'
           f'{hubs}'
           f'<div class="led" id="{s}-tally" style="left:{r3(752 * PS)}px;top:{r3(196 * PS)}px;width:10px;height:10px"></div>'
           f'{drawn_lens}'
           f'<div class="abs" id="{s}-glint" style="{box(lcx - 46, lcy - 70, 92, 92)}"><svg width="92" height="92" viewBox="0 0 40 40">'
           f'<path d="M20 2 C21 14 26 19 38 20 C26 21 21 26 20 38 C19 26 14 21 2 20 C14 19 19 14 20 2Z" fill="#ffffff" stroke="#acc6e7" stroke-width=".6"/></svg></div>'
           f'</div></div>')
    S.mid.append(rig)

    # ================================================ glass scene layers hanging in depth in front of the lens
    # world-static (the dolly moves toward them). Projected centre ~ the lens line at mid-travel.
    HANG = []
    for k in range(4):
        # a layer stack in depth (sky farthest) hanging upper-right, behind/beside the rig
        z = -330 + 140 * k
        mag = F / (F - z)
        tx, ty = 770 + 40 * k, 650 + 16 * k                 # where the layer should appear on screen (cam at rest)
        wx, wy = O[0] + (tx - O[0]) / mag, O[1] + (ty - O[1]) / mag
        HANG.append({"x": r3(wx - 540), "y": r3(wy - 960), "z": z, "rotationY": -10, "rotationX": -2, "scale": r3(1.0 / mag), "opacity": 1})
    for k, nm in enumerate(LAYERS):
        edge = ["rgba(58,98,153,.5)", "rgba(58,98,153,.6)", "rgba(41,75,119,.7)", "rgba(41,75,119,.85)"][k]
        wires = (f'<div class="abs" style="{box(34, -120, 2, 120)}background:linear-gradient(180deg,rgba(41,75,119,0),rgba(41,75,119,.55))"></div>'
                 f'<div class="abs" style="{box(PW_ - 36, -120, 2, 120)}background:linear-gradient(180deg,rgba(41,75,119,0),rgba(41,75,119,.55))"></div>'
                 f'<div class="rivet" style="left:31px;top:-4px"></div><div class="rivet" style="left:{PW_ - 39}px;top:-4px"></div>')
        S.mid.append(f'<div class="abs" id="{s}-lw{k}" style="{box(540 - PW_ / 2, 960 - PH_ / 2, PW_, PH_)}">'
                     f'<div class="abs" id="{s}-ly{k}" style="{box(0, 0, PW_, PH_)}border-radius:16px;border:2px solid {edge};'
                     f'background:linear-gradient(135deg,rgba(255,255,255,.6),rgba(232,240,251,.38));box-shadow:0 26px 40px -24px rgba(28,51,84,.35)">'
                     f'<div class="abs" id="{s}-li{k}" style="{box(0, 0, PW_, PH_)}">{layer_inner(nm, PW_, PH_)}</div>{wires}'
                     f'<div class="abs" id="{s}-le{k}" style="{box(-3, -3, PW_ + 2, PH_ + 2)}border-radius:17px;border:3px solid #ffffff;box-shadow:0 0 18px rgba(172,198,231,1)"></div></div></div>')

    # ================================================ near plane: out-of-focus glass ring + rail fragment
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(280px) scale(.86)">'
                  f'<div class="abs" style="{box(930, 640, 200, 200)}border-radius:50%;border:12px solid rgba(255,255,255,.72);box-shadow:0 0 0 2px rgba(172,198,231,.5);filter:blur(5px)"></div>'
                  f'<div class="abs" style="{box(820, 1500, 320, 26)}border-radius:13px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px);opacity:.85"></div></div>')
    # exposure flash for the cut (screen-fixed: outside the camera so it never scales)
    S.near.append(f'<div class="abs" id="{s}-exp" style="{box(-200, -200, 1480, 2320)}background:radial-gradient(ellipse at 50% 42%,#ffffff 0%,#fbfcfe 40%,rgba(232,240,251,.9) 70%,rgba(232,240,251,.6) 100%)"></div>')
    apex(S, S.near, f"{s}-ap", 560, 590, W19 + 0.03, size=820, sparks=10, seed=41, op=0.7)

    # ================================================ motion
    T_EXP = W19 + 0.02          # layers burst apart
    T_ALIGN = W19 + 0.52        # one composed frame (9.76)
    T_PUSH = 9.96               # zoom-through into the lens
    # viewer camera: tight on the rail (continues S03's track) -> pull back -> track the dolly -> square-on -> push into lens
    mag_end = 4.2
    zf = F * (1 - 1 / mag_end)
    txf = (548 - O[0]) / mag_end + O[0] - LX + 14     # +14 / -13: measured correction on the rendered frame
    tyf = (770 - O[1]) / mag_end + O[1] - LY - 13
    S.cam([(t0, {"z": 420, "x": 10, "y": 46, "rotationY": -6, "rotationX": 3}, None),
           (W15 + 0.02, {"z": 40, "x": 0, "y": 0, "rotationY": -6, "rotationX": 1}, "power2.inOut"),
           (W16 + 0.15, {"z": 60, "x": 12, "y": -10, "rotationY": 6, "rotationX": 0}, "sine.inOut"),       # tracking the dolly
           (W19, {"z": 70, "x": 6, "y": -10, "rotationY": 9}, "sine.inOut"),
           (T_ALIGN + 0.12, {"z": 90, "x": 20, "y": 0, "rotationY": 0, "rotationX": 0}, "power3.inOut"),
           (T_PUSH, {"z": 140, "x": 30, "y": 0}, "sine.inOut"),
           (t1 - 0.025, {"z": r3(zf), "x": r3(txf), "y": r3(tyf), "rotationY": 0, "rotationX": 0}, "power3.in")])
    # dolly: parked a touch further back -> anticipation pull -> glide toward us (accelerate / decelerate) -> settle
    cxs, cys = ccx - OX, ccy - OY
    S.keys(f"#{s}-dolly", [(t0, {"x": r3(pre_x), "y": r3(pre_y), "scale": 0.985, "transformOrigin": f"{r3(cxs)}px {r3(cys)}px"}, None),
                           (W14 - 0.08, {"x": r3(pre_x * 1.25), "y": r3(pre_y * 1.25), "scale": 0.982}, "power2.inOut"),
                           (W16 + 0.12, {"x": r3(dx * 1.03), "y": r3(dy * 1.03), "scale": r3(SC_END * 1.002)}, "power3.inOut"),
                           (W16 + 0.42, {"x": r3(dx), "y": r3(dy), "scale": r3(SC_END)}, "power2.out"),
                           (t1, {"x": r3(dx * 1.02), "y": r3(dy * 1.02), "scale": r3(SC_END * 1.005)}, "sine.inOut")])
    # cart bob while rolling (small, decays) — on the photo layer's wrapper via the shadow + hubs
    S.init(f"#{s}-dsh", {"opacity": 0.6, "scaleX": 1})
    S.ft(f"#{s}-dsh", {"opacity": 0.6, "scaleX": 1}, {"opacity": 0.45, "scaleX": 1.08}, W14, 0.5, "sine.inOut")
    S.ft(f"#{s}-dsh", {"opacity": 0.45, "scaleX": 1.08}, {"opacity": 0.6, "scaleX": 1}, W16, 0.4, "sine.inOut")
    for k in range(4):
        S.init(f"#{s}-hub{k}", {"rotation": 0, "opacity": 0})
        S.ft(f"#{s}-hub{k}", {"rotation": 0, "opacity": 0}, {"rotation": -540, "opacity": 0.9}, W14 - 0.05, W16 + 0.35 - W14, "power2.inOut")
        S.ft(f"#{s}-hub{k}", {"rotation": -540, "opacity": 0.9}, {"rotation": -560, "opacity": 0}, W16 + 0.3, 0.3, "power2.out")
    # mint tally lights on "gerak"; lens glint on "kamera"
    S.init(f"#{s}-tally", {"opacity": 0, "scale": 0.4})
    S.ft(f"#{s}-tally", {"opacity": 0, "scale": 0.4}, {"opacity": 1, "scale": 1}, W14 - 0.04, 0.16, "back.out(2)")
    S.init(f"#{s}-glint", {"opacity": 0, "scale": 0.2, "rotation": 0})
    S.ft(f"#{s}-glint", {"opacity": 0, "scale": 0.2, "rotation": 0}, {"opacity": 1, "scale": 1, "rotation": 45}, W15 - 0.03, 0.16, "power3.out")
    S.ft(f"#{s}-glint", {"opacity": 1, "scale": 1, "rotation": 45}, {"opacity": 0, "scale": 0.3, "rotation": 90}, W15 + 0.14, 0.32, "power2.in")
    # drawn lens takes over from the photo lens for the push (crisp at any size)
    S.init(f"#{s}-dlens", {"opacity": 0})
    S.ft(f"#{s}-dlens", {"opacity": 0}, {"opacity": 1}, T_PUSH + 0.12, 0.2, "power1.out")
    # layers: hang -> drift (parallax comes from the camera) -> edge glow -> burst -> compose -> fade through
    for k in range(4):
        pid = f"#{s}-lw{k}"
        base = HANG[k]
        drift = dict(base, y=r3(float(base["y"]) - 10 - 4 * k), rotationY=r3(16 - 3 * k))
        S.init(pid, base)
        S.ft(pid, base, drift, t0, W19 - 0.04 - t0, "sine.inOut")
        burst = {"x": r3(-345 + 222 * k), "y": r3(-390 + (k % 2) * 46), "z": 80 + 40 * k, "rotationY": r3(-20 + 13 * k), "rotationX": -4, "scale": 0.56}
        S.ft(pid, drift, burst, W19 - 0.04, 0.31, "expo.out")
        # composed frame: all layers at one depth, centred over the final lens position
        zc = 200 + 2 * k
        magc = F / (F - zc)
        wx, wy = O[0] + (LX - O[0]) / magc, O[1] + (LY - O[1]) / magc
        comp = {"x": r3(wx - 540), "y": r3(wy - 960), "z": zc, "rotationY": 0, "rotationX": 0, "scale": 0.82}
        S.ft(pid, burst, comp, T_ALIGN - 0.24, 0.3, "power4.inOut")
        S.ft(pid, dict(comp, opacity=1), dict(comp, opacity=0, scale=0.9), T_PUSH + 0.1, 0.22, "power2.in")
        S.init(f"#{s}-le{k}", {"opacity": 0})
        S.ft(f"#{s}-le{k}", {"opacity": 0}, {"opacity": 0.95}, W18 - 0.02 + k * 0.07, 0.12, "power2.out")
        S.ft(f"#{s}-le{k}", {"opacity": 0.95}, {"opacity": 0}, W18 + 0.18 + k * 0.07, 0.3, "power2.in")
        S.ft(f"#{s}-le{k}", {"opacity": 0}, {"opacity": 0.85}, T_ALIGN + 0.02, 0.08, "power2.out")
        S.ft(f"#{s}-le{k}", {"opacity": 0.85}, {"opacity": 0}, T_ALIGN + 0.12, 0.3, "power2.in")
        # layer content punch on the apex (scale punch, inner element so it never fights the wrapper)
        S.init(f"#{s}-li{k}", {"scale": 1})
        S.ft(f"#{s}-li{k}", {"scale": 1}, {"scale": 1.05}, W19 + 0.02, 0.1, "power2.out")
        S.ft(f"#{s}-li{k}", {"scale": 1.05}, {"scale": 1}, W19 + 0.12, 0.2, "power2.inOut")
    # bokeh drift (far plane moves slower than everything else)
    for k in range(4):
        S.init(f"#{s}-bk{k}", {"x": 0, "y": 0})
        S.ft(f"#{s}-bk{k}", {"x": 0, "y": 0}, {"x": (-1) ** k * 18, "y": -24}, t0, t1 - t0, "sine.inOut")
    # exposure flash: the lens fills the frame and blooms to ivory right before the cut
    S.init(f"#{s}-exp", {"opacity": 0})
    S.ft(f"#{s}-exp", {"opacity": 0}, {"opacity": 0.8}, t1 - 0.075, 0.07, "power2.in")
