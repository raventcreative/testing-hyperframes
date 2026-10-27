"""S17 — 16 GREEN SCREEN (29.70–30.80)  VO: "pindah ke latar kota,"
Opens on S16's dark pupil: a circle opens from the centre onto the mascot standing on a chroma-green cyc
(tracking crosses, soft floor, contact shadow). 'latar': a cyan key line sweeps left->right and keys the green
out, revealing an original layered navy skyline (far/mid/near towers, lit windows, moon, plaza glow) that
drifts in parallax; the mascot picks up a cool cyan rim to match the city. No fake green spill.
End state (30.78) = the frame S18 shatters (self-shot `city_end`)."""
from xk import box, r3, CYAN, clip_circle
from kit import WIDE, NO_FILTER
from kit_d import city, CITY_BASE

RIM = "drop-shadow(0px 0px 6px rgba(0,208,254,0.5))"


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W84, W85 = S.W(84), S.W(85)            # latar 30.18, kota 30.44
    op0, op1 = t0, t0 + 0.34               # iris open
    w0, w1 = W84 - 0.03, W85 + 0.1         # key wipe
    # ---------------------------------------------------------------- back: dark base, city (under), green cyc (over)
    S.back.append(f'<div class="abs" id="{s}-dark" style="{box(0, 0, 1080, 1920)}background:#040917"></div>')
    S.back.append(f'<div class="abs" id="{s}-world" style="{box(0, 0, 1080, 1920)}clip-path:circle(0px at 540px 960px)">'
                  + "".join(city(s))
                  + f'<div class="abs cshadow" style="{box(330, CITY_BASE - 30, 420, 70)}opacity:.9"></div>'
                  # green cyc with soft floor sweep, tracking crosses and its own contact shadow (keyed out as one plate)
                  + f'<div class="abs" id="{s}-green" style="{box(0, 0, 1080, 1920)}clip-path:inset(0px 0px 0px 0px);'
                    f'background:linear-gradient(180deg,#2bd06a 0%,#25c262 55%,#2fd673 70%,#1ea457 100%)">'
                  + f'<div class="abs" style="{box(-200, 1300, 1480, 700)}border-radius:50%;background:radial-gradient(ellipse at 50% 30%,rgba(255,255,255,.22),rgba(255,255,255,0) 60%)"></div>'
                  + "".join(f'<div class="abs" style="{box(x - 14, y - 2, 28, 4)}background:rgba(255,255,255,.75)"></div>'
                            f'<div class="abs" style="{box(x - 2, y - 14, 4, 28)}background:rgba(255,255,255,.75)"></div>'
                            for x in (150, 930) for y in (420, 820, 1220))
                  + f'<div class="abs cshadow" style="{box(330, CITY_BASE - 30, 420, 70)}"></div></div>'
                  + "</div>")
    # key line (front: it passes over the mascot like a scan)
    S.front.append(f'<div class="abs" id="{s}-key" style="{box(-6, 0, 12, 1920)}background:linear-gradient(90deg,rgba(0,208,254,0),#bff6ff 50%,rgba(0,208,254,0));'
                   f'box-shadow:0 0 24px 6px rgba(0,208,254,.55)"></div>')
    S.front.append(f'<div class="abs" id="{s}-keyh" style="{box(-180, 0, 180, 1920)}background:linear-gradient(90deg,rgba(0,208,254,0),rgba(0,208,254,.16))"></div>')

    # ---------------------------------------------------------------- motion
    S.init(f"#{s}-world", {"clipPath": "circle(0px at 540px 960px)"})
    S.ft(f"#{s}-world", {"clipPath": "circle(0px at 540px 960px)"}, {"clipPath": "circle(1200px at 540px 960px)"}, op0, op1 - op0, "power3.inOut")
    S.init(f"#{s}-green", {"clipPath": "inset(0px 0px 0px 0px)"})
    S.ft(f"#{s}-green", {"clipPath": "inset(0px 0px 0px 0px)"}, {"clipPath": "inset(0px 0px 0px 1080px)"}, w0, w1 - w0, "power2.inOut")
    for sel in (f"#{s}-key", f"#{s}-keyh"):
        S.init(sel, {"x": 0, "opacity": 0})
        S.tset(sel, {"opacity": 1}, w0)
        S.ft(sel, {"x": 0}, {"x": 1086}, w0, w1 - w0, "power2.inOut")
        S.tset(sel, {"opacity": 0}, w1)
    # parallax drift of the skyline (far slow, near fast)
    for lid, dx in (("cfar", -10), ("cmid", -24), ("cnear", -52)):
        S.init(f"#{s}-{lid}", {"x": 0})
        S.ft(f"#{s}-{lid}", {"x": 0}, {"x": dx}, w0, t1 - w0 + 0.04, "power1.out")

    # ---------------------------------------------------------------- mascot: wide, revealed by the iris, slow push; cyan rim after the key
    v0 = dict(WIDE, yaw=-6)
    v1 = dict(WIDE, fy=1740, h=1230, yaw=5)
    S.mv([(t0, v0, None), (t1, v1, "sine.inOut")])
    S.mc([(t0, {"clipPath": clip_circle(540, 960, 2)}, None), (op1, {"clipPath": clip_circle(540, 960, 2400)}, "power3.inOut")])
    S.mx([(t0, {"filter": NO_FILTER}, None), (w1 - 0.1, {"filter": NO_FILTER}, "none"), (w1 + 0.15, {"filter": RIM}, "power1.out")])
    S.act("armL", [(t0, "low", 0.3), (W84 - 0.16, "present", 0.3), (W85 + 0.3, "open", 0.35)])
    S.act("armR", [(t0, "low", 0.3), (W85 - 0.1, "explain", 0.3)])
    S.act("head", [(t0, [-0.04, -0.06, 0], 0.3), (W84 - 0.05, [-0.06, 0.24, 0.03], 0.3), (W85 + 0.1, [-0.1, 0.1, 0.0], 0.3)])
    S.fx(op0 + 0.02, "whoosh", 0.05)
    S.fx(w0 + 0.05, "sparkle", 0.05)
