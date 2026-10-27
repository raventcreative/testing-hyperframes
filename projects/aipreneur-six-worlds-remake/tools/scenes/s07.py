"""S07 — 06/06 COLOR GRADE (20.63–23.57)  VO: "Satu gerakan tangan, warnanya berubah total."
Opens on S06's palm iris. The iris drops into his hand and becomes a physical colour-grade dial (anodized ring,
knurled edge, detent ticks); from the iris the graded frame opens as a card - one still of OUR spotlight shot
(the SAME frame, two grades). "gerakan tangan": he grips and turns the dial, a thick reflective divider sweeps in and
splits the frame: BEFORE (flat, desaturated) | AFTER (balanced brand look) - held so both can be compared.
"warnanya berubah total": a second turn sweeps the divider across, the whole frame is AFTER, held.
Hand-off: the dial lifts to the centre and becomes a thin navy ring with 6 detents (RING_END) - S08 opens on it."""
from xk import box, r3
from kit import SELF
from kit_c import IRIS_C, S06_END, S07_VIEW, DIAL, CARD, RING_END
from s06 import CONE

BEFORE = "saturate(0.25) contrast(0.8) brightness(1.08)"
AFTER = "saturate(1.06) contrast(1.05)"


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W43, W44, W45, W46, W47 = (S.W(i) for i in range(43, 48))      # gerakan 20.98 tangan 21.30 warnanya 21.90 berubah 22.38 total 22.84
    cx, cy, cw, ch = CARD
    dx, dy, dd = DIAL
    ix, iy, idm = IRIS_C
    rx, ry, rd = RING_END
    # ---------------------------------------------------------------- back: S06's stage light lingers and lifts (continuity)
    S.back.append(f'<div class="abs" id="{s}-dim" style="{box(0, 0, 1080, 1920)}'
                  f'background:radial-gradient(ellipse 78% 62% at 50% 56%, rgba(10,13,44,.52) 0%, rgba(10,13,44,.40) 46%, rgba(10,13,44,.10) 82%, rgba(10,13,44,0) 100%)"></div>')
    S.back.append(f'<div class="abs" id="{s}-cone" style="{box(0, 0, 1080, 1920)}clip-path:{CONE};'
                  f'background:linear-gradient(160deg, rgba(255,255,255,.92) 0%, rgba(236,243,255,.55) 30%, rgba(222,234,252,.30) 70%, rgba(222,234,252,.12) 100%);filter:blur(6px)"></div>')
    # ---------------------------------------------------------------- back: the graded frame card (same still, two grades)
    img_w = cw * 1.5
    img_h = img_w * 1920 / 1080
    ox, oy = -(img_w - cw) / 2, -330

    def still(id_, flt, clip=""):
        return (f'<div class="abs" id="{id_}" style="{box(0, 0, cw, ch)}overflow:hidden;border-radius:22px;{clip}">'
                f'<div class="abs" style="left:{r3(ox)}px;top:{r3(oy)}px;width:{r3(img_w)}px;height:{r3(img_h)}px;'
                f'background:url({SELF}/spot_full.jpg) 0 0 / 100% 100% no-repeat;filter:{flt}"></div></div>')
    S.back.append(f'<div class="abs" id="{s}-cardsh" style="{box(cx + 30, cy + ch - 30, cw - 20, 90)}border-radius:50%;'
                  f'background:radial-gradient(ellipse at 50% 50%, rgba(10,13,44,.32) 0%, rgba(10,13,44,0) 70%)"></div>')
    S.back.append(f'<div class="abs" id="{s}-card" style="{box(cx, cy, cw, ch)}border-radius:22px;'
                  f'box-shadow:0 0 0 1px rgba(41,75,119,.12), 0 30px 60px -28px rgba(10,13,44,.5)">'
                  + still(f"{s}-bef", BEFORE)
                  + still(f"{s}-aft", AFTER)
                  + f'<div class="abs" id="{s}-div" style="{box(-7, -10, 14, ch + 20)}border-radius:7px;'
                    f'background:linear-gradient(90deg,#8995a8 0%,#f4f7fb 35%,#ffffff 50%,#c3ccd8 70%,#7d899c 100%);'
                    f'box-shadow:0 0 0 1px rgba(10,13,44,.18), 0 8px 18px rgba(10,13,44,.35)">'
                    f'<div class="abs anod" style="{box(-17, ch / 2 - 14, 48, 48)}border-radius:24px"></div></div>'
                  + f'<div class="abs" id="{s}-lb" style="left:20px;top:20px;padding:8px 16px;border-radius:12px;background:rgba(255,255,255,.88);'
                    f'box-shadow:0 6px 14px -8px rgba(10,13,44,.5)"><span class="tx" style="font:700 26px/1 Poppins, sans-serif;letter-spacing:.08em">BEFORE</span></div>'
                  + f'<div class="abs" id="{s}-la" style="right:20px;top:20px"><span class="badge" style="font:700 26px/1 Poppins, sans-serif;letter-spacing:.08em;padding:10px 16px">AFTER</span></div>'
                  + "</div>")
    # ---------------------------------------------------------------- front: the dial (anodized, knurled, detents), iris, end ring
    ticks = "".join(f'<div class="abs" style="left:{r3(dd / 2 - 2)}px;top:6px;width:4px;height:16px;border-radius:2px;background:#0A0D2C;'
                    f'transform-origin:2px {r3(dd / 2 - 6)}px;transform:rotate({a}deg)"></div>' for a in range(0, 360, 30))
    S.front.append(f'<div class="abs" id="{s}-dial" style="{box(dx - dd / 2, dy - dd / 2, dd, dd)}">'
                   f'<div class="abs" style="{box(10, 26, dd - 20, dd - 6)}border-radius:50%;background:radial-gradient(ellipse at 50% 50%, rgba(10,13,44,.35), rgba(10,13,44,0) 70%)"></div>'
                   f'<div class="abs" id="{s}-knurl" style="{box(0, 0, dd, dd)}border-radius:50%;'
                   f'background:repeating-conic-gradient(from 0deg, #7d899c 0deg 3deg, #eef2f8 3deg 6deg);box-shadow:0 14px 26px -12px rgba(10,13,44,.6)">'
                   + ticks +
                   f'<div class="abs anod" style="{box(22, 22, dd - 44, dd - 44)}border-radius:50%"></div>'
                   f'<div class="abs" style="{box(44, 44, dd - 88, dd - 88)}border-radius:50%;'
                   f'background:radial-gradient(circle at 38% 32%, #ffffff 0%, #dfe7f2 40%, #9aa7ba 100%);box-shadow:inset 0 2px 4px rgba(10,13,44,.35)"></div>'
                   f'<div class="abs" style="{box(dd / 2 - 4, 30, 8, 40)}border-radius:4px;background:#0A0D2C"></div></div></div>')
    S.front.append(f'<div class="abs" id="{s}-iris" style="{box(ix - idm / 2, iy - idm / 2, idm, idm)}border-radius:50%;'
                   f'border:4px solid rgba(255,255,255,.98);box-shadow:0 0 18px rgba(255,255,255,.95), 0 0 40px rgba(190,215,250,.8), inset 0 0 22px rgba(255,255,255,.75)"></div>')
    det = "".join(f'<div class="abs" style="left:{r3(rd / 2 - 5)}px;top:-12px;width:10px;height:30px;border-radius:5px;background:linear-gradient(180deg,#0A0D2C,#294B77);'
                  f'transform-origin:5px {r3(rd / 2 + 12)}px;transform:rotate({a}deg)"></div>' for a in range(0, 360, 60))
    S.front.append(f'<div class="abs" id="{s}-ring" style="{box(rx - rd / 2, ry - rd / 2, rd, rd)}">'
                   f'<div class="abs" style="{box(0, 0, rd, rd)}border-radius:50%;border:5px solid #294B77;box-shadow:0 0 0 1px rgba(10,13,44,.15), 0 18px 30px -18px rgba(10,13,44,.5)"></div>'
                   + det + "</div>")

    # ---------------------------------------------------------------- motion
    open_ = t0 + 0.06
    for sel in (f"#{s}-dim", f"#{s}-cone"):
        S.init(sel, {"opacity": 1})
        S.ft(sel, {"opacity": 1}, {"opacity": 0}, t0, 0.42, "power2.inOut")
    # iris drops into the hand and turns into the dial
    S.init(f"#{s}-iris", {"x": 0, "y": 0, "scale": 1, "opacity": 1})
    S.ft(f"#{s}-iris", {"x": 0, "y": 0, "scale": 1}, {"x": dx - ix, "y": dy - iy, "scale": dd / idm}, t0, 0.4, "power3.inOut")
    S.ft(f"#{s}-iris", {"opacity": 1}, {"opacity": 0}, t0 + 0.32, 0.14, "power1.in")
    S.init(f"#{s}-dial", {"opacity": 0, "scale": 0.86, "rotation": -20})
    S.ft(f"#{s}-dial", {"opacity": 0, "scale": 0.86, "rotation": -20}, {"opacity": 1, "scale": 1, "rotation": 0}, t0 + 0.28, 0.3, "back.out(1.8)")
    # the graded frame opens from the iris (circle mask), starts fully BEFORE
    lx, ly = ix - cx, iy - cy
    S.init(f"#{s}-card", {"clipPath": f"circle(0px at {r3(lx)}px {r3(ly)}px)", "opacity": 1})
    S.ft(f"#{s}-card", {"clipPath": f"circle(0px at {r3(lx)}px {r3(ly)}px)"}, {"clipPath": f"circle(1150px at {r3(lx)}px {r3(ly)}px)"}, open_, 0.5, "power3.inOut")
    S.init(f"#{s}-cardsh", {"opacity": 0})
    S.ft(f"#{s}-cardsh", {"opacity": 0}, {"opacity": 1}, open_ + 0.3, 0.3, "power2.out")
    S.init(f"#{s}-aft", {"clipPath": f"inset(0px 0px 0px {cw}px)"})
    S.init(f"#{s}-div", {"x": cw, "opacity": 0})
    S.init(f"#{s}-lb", {"opacity": 0, "y": -10})
    S.init(f"#{s}-la", {"opacity": 0, "y": -10})
    S.ft(f"#{s}-lb", {"opacity": 0, "y": -10}, {"opacity": 1, "y": 0}, open_ + 0.35, 0.22, "power2.out")
    # turn 1 ("gerakan tangan"): dial -70 deg, divider sweeps in from the right to the middle -> split, held
    a1, a2 = W43 - 0.04, W44 + 0.3
    S.ft(f"#{s}-knurl", {"rotation": 0}, {"rotation": -70}, a1, a2 - a1, "power2.inOut")
    S.tset(f"#{s}-div", {"opacity": 1}, a1)
    S.ft(f"#{s}-div", {"x": cw}, {"x": cw / 2}, a1, a2 - a1, "power2.inOut")
    S.ft(f"#{s}-aft", {"clipPath": f"inset(0px 0px 0px {cw}px)"}, {"clipPath": f"inset(0px 0px 0px {r3(cw / 2)}px)"}, a1, a2 - a1, "power2.inOut")
    S.ft(f"#{s}-la", {"opacity": 0, "y": -10}, {"opacity": 1, "y": 0}, a2 - 0.2, 0.22, "power2.out")
    # turn 2 ("warnanya berubah total"): dial -110 deg more, divider sweeps left -> whole frame AFTER, held
    b1, b2 = W46 - 0.06, W47 + 0.1
    S.ft(f"#{s}-knurl", {"rotation": -70}, {"rotation": -180}, b1, b2 - b1, "power2.inOut")
    S.ft(f"#{s}-div", {"x": cw / 2}, {"x": 0}, b1, b2 - b1, "power2.inOut")
    S.ft(f"#{s}-aft", {"clipPath": f"inset(0px 0px 0px {r3(cw / 2)}px)"}, {"clipPath": "inset(0px 0px 0px 0px)"}, b1, b2 - b1, "power2.inOut")
    S.ft(f"#{s}-div", {"opacity": 1}, {"opacity": 0}, b2 - 0.04, 0.16, "power1.in")
    S.ft(f"#{s}-lb", {"opacity": 1}, {"opacity": 0}, b1 + 0.2, 0.2, "power1.in")
    S.ft(f"#{s}-la", {"scale": 1}, {"scale": 1.12}, W47 - 0.02, 0.16, "back.out(3)")
    S.ft(f"#{s}-la", {"scale": 1.12}, {"scale": 1}, W47 + 0.14, 0.2, "power2.out")
    # hand-off: dial lifts to the centre and becomes the thin navy ring with 6 detents; the card steps back
    h0 = t1 - 0.32
    S.ft(f"#{s}-dial", {"x": 0, "y": 0, "scale": 1, "opacity": 1}, {"x": rx - dx, "y": ry - dy, "scale": rd / dd, "opacity": 0}, h0, 0.3, "power3.inOut")
    S.init(f"#{s}-ring", {"x": dx - rx, "y": dy - ry, "scale": dd / rd, "opacity": 0, "rotation": -180})
    S.ft(f"#{s}-ring", {"x": dx - rx, "y": dy - ry, "scale": dd / rd, "opacity": 0, "rotation": -180},
         {"x": 0, "y": 0, "scale": 1, "opacity": 1, "rotation": 0}, h0, 0.3, "power3.inOut")
    S.ft(f"#{s}-card", {"opacity": 1, "scale": 1}, {"opacity": 0.0, "scale": 0.92}, h0, 0.28, "power2.in")
    S.ft(f"#{s}-cardsh", {"opacity": 1}, {"opacity": 0}, h0, 0.2, "power1.in")
    S.ft(f"#{s}-la", {"opacity": 1}, {"opacity": 0}, h0, 0.16, "power1.in")

    # ---------------------------------------------------------------- mascot: steps aside, small, hand on the dial
    S.mv([(t0, S06_END, None), (t0 + 0.45, S07_VIEW, "power3.inOut"), (W46, dict(S07_VIEW, yaw=18), "sine.inOut"), (t1, dict(S07_VIEW, yaw=12), "sine.inOut")])
    S.act("armL", [(t0, "present", 0.3), (a1 - 0.08, "fist", 0.22), (a2 + 0.1, "present", 0.3), (b1 - 0.08, "fist", 0.22), (b2 + 0.12, "present", 0.3), (h0, "point", 0.3)])
    S.act("armR", [(t0, "low", 0.3), (W45 - 0.1, "explain", 0.3), (W47 + 0.2, "low", 0.4)])
    S.act("head", [(t0, [0.04, 0.18, -0.04], 0.3), (a1, [0.12, 0.28, 0], 0.3), (a2, [-0.04, 0.34, 0.02], 0.3),
                   (W46, [0.06, 0.3, -0.03], 0.25), (W47 + 0.05, [-0.08, 0.3, 0.04], 0.25), (h0, [-0.16, 0.22, 0], 0.3)])
    S.act("torso", [(t0, {"chest": [0.04, 0.08, 0]}, 0.3), (a1, {"chest": [0.05, -0.1, 0]}, 0.3), (a2, {"chest": [0.03, 0.06, 0]}, 0.3),
                    (b1, {"chest": [0.05, -0.12, 0]}, 0.3), (b2, {"chest": [0, 0.06, 0]}, 0.3)])
    S.fx(t0 + 0.32, "pop", 0.05)
    for t in (a1 + 0.1, a1 + 0.3, a1 + 0.5, b1 + 0.1, b1 + 0.3):
        S.fx(t, "key", 0.04)
    S.fx(W47 + 0.02, "sparkle", 0.04)
    S.fx(h0, "whoosh", 0.05)
