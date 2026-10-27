"""S19 — 18 DIGITAL ZOOM (31.40–32.07)  VO: "dan masuk"
Camera HUD over the medium shot: four corner guides (same as S18's end), REC with a cyan dot, timecode, zoom
read-out stepping 1.0x -> 1.5x ('dan') -> 2.0x ('masuk') with a tick bar, and a focus box on the face that
pumps on every step. Each step is a real re-framing of the 3D camera around the face (sharp, not a bitmap
upscale). Hand-off: the guides close in to the phone outline (PHONE) while the shot is clipped to it."""
from xk import box, r3, CYAN, clip_rect
from kit import MED, HUD, PHONE, FACE_C, corner_frame


def zview(z, yaw=0.0):
    """MED re-framed around the face by zoom factor z (face stays at FACE_C)."""
    k = 1500 * z
    return {"fx": 540, "fy": r3(FACE_C[1] + 0.585 * k), "h": r3(0.98 * k), "yaw": yaw, "pitch": 5}


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W88, W89 = S.W(88), S.W(89)            # dan 31.66, masuk 31.84
    st1, st2 = W88 - 0.04, W89 - 0.03      # zoom steps
    c0, c1 = W89 + 0.06, t1 - 0.004        # guides close into the phone
    x, y, w, h = HUD
    # ---------------------------------------------------------------- front: HUD
    S.front.append(f'<div class="abs" id="{s}-hud" style="{box(0, 0, 1080, 1920)}">' + corner_frame(f"{s}-hud", x, y, w, h, arm=80, th=5) + "</div>")
    S.front.append(f'<div class="abs" id="{s}-ui" style="{box(0, 0, 1080, 1920)}">'
                   f'<div class="abs" id="{s}-dot" style="{box(x + 40, y + 44, 18, 18)}border-radius:9px;background:{CYAN};box-shadow:0 0 10px rgba(0,208,254,.9)"></div>'
                   f'<div class="abs" style="left:{x + 70}px;top:{y + 34}px;width:120px;font:700 28px/38px Poppins;color:#fff;letter-spacing:.14em">REC</div>'
                   f'<div class="abs" style="left:{x + 40}px;top:{y + 76}px;width:240px;font:400 24px/30px Poppins;color:rgba(255,255,255,.8);letter-spacing:.08em">00:31:40:12</div>'
                   + "".join(f'<div class="abs" id="{s}-z{k}" style="left:{x + w - 210}px;top:{y + 30}px;width:170px;font:700 44px/52px Poppins;color:{CYAN};text-align:right">{t}</div>'
                             for k, t in enumerate(("1.0×", "1.5×", "2.0×")))
                   + f'<div class="abs" style="left:{x + w - 210}px;top:{y + 92}px;width:170px;height:4px;background:rgba(255,255,255,.3)"></div>'
                   + "".join(f'<div class="abs" style="left:{x + w - 210 + i * 56.7}px;top:{y + 86}px;width:2px;height:16px;background:rgba(255,255,255,.6)"></div>' for i in range(4))
                   + f'<div class="abs" id="{s}-zm" style="left:{x + w - 216}px;top:{y + 84}px;width:12px;height:20px;border-radius:3px;background:{CYAN};box-shadow:0 0 8px rgba(0,208,254,.8)"></div>'
                   + f'<div class="abs" style="left:{x + w / 2 - 18}px;top:{y + h / 2 + 2}px;width:36px;height:2px;background:rgba(255,255,255,.55)"></div>'
                   + f'<div class="abs" style="left:{x + w / 2 - 1}px;top:{y + h / 2 - 16}px;width:2px;height:36px;background:rgba(255,255,255,.55)"></div>'
                   + "</div>")
    fx_, fy_ = FACE_C
    S.front.append(f'<div class="abs" id="{s}-focus" style="{box(0, 0, 1080, 1920)}">' + corner_frame(f"{s}-fc", fx_ - 230, fy_ - 230, 460, 430, arm=46, th=4, color="#00D0FE") + "</div>")

    # ---------------------------------------------------------------- motion
    for k, (a, b) in enumerate(((t0, st1), (st1, st2), (st2, t1 + 0.01))):
        S.init(f"#{s}-z{k}", {"opacity": 1 if k == 0 else 0})
        if k > 0:
            S.tset(f"#{s}-z{k}", {"opacity": 1}, a)
        if k < 2:
            S.tset(f"#{s}-z{k}", {"opacity": 0}, b)
    S.keys(f"#{s}-zm", [(t0, {"x": 0}, None), (st1, {"x": 0}, "none"), (st1 + 0.1, {"x": 85}, "power3.out"), (st2, {"x": 85}, "none"), (st2 + 0.1, {"x": 170}, "power3.out")])
    S.keys(f"#{s}-dot", [(t0, {"opacity": 1}, None), (t0 + 0.25, {"opacity": 1}, "none"), (t0 + 0.27, {"opacity": 0.25}, "none"),
                         (t0 + 0.42, {"opacity": 0.25}, "none"), (t0 + 0.44, {"opacity": 1}, "none")])
    S.keys(f"#{s}-focus", [(t0, {"scale": 1.0, "opacity": 0.0, "transformOrigin": f"{fx_}px {fy_ - 15}px"}, None),
                           (t0 + 0.12, {"opacity": 1}, "power2.out"),
                           (st1, {"scale": 1.0}, "none"), (st1 + 0.05, {"scale": 1.14}, "power2.out"), (st1 + 0.16, {"scale": 1.0}, "power3.out"),
                           (st2, {"scale": 1.0}, "none"), (st2 + 0.05, {"scale": 1.14}, "power2.out"), (st2 + 0.12, {"scale": 1.0}, "power3.out"),
                           (st2 + 0.13, {"opacity": 1}, "none"), (st2 + 0.2, {"opacity": 0}, "power1.in")])
    S.init(f"#{s}-ui", {"opacity": 1})
    S.ft(f"#{s}-ui", {"opacity": 1}, {"opacity": 0}, c0, 0.08, "power1.in")
    # corner guides close into the phone outline
    px, py, pw, ph, pr = PHONE
    hud_c = ((x, y), (x + w, y), (x, y + h), (x + w, y + h))
    ph_c = ((px, py), (px + pw, py), (px, py + ph), (px + pw, py + ph))
    for k, ((ax, ay), (bx, by)) in enumerate(zip(hud_c, ph_c)):
        S.init(f"#{s}-hud-c{k}", {"x": 0, "y": 0})
        S.ft(f"#{s}-hud-c{k}", {"x": 0, "y": 0}, {"x": bx - ax, "y": by - ay}, c0, c1 - c0, "power3.inOut")

    # ---------------------------------------------------------------- mascot: stepped digital zoom, then clipped to the phone outline
    S.mv([(t0, zview(1.0, -3), None), (st1, zview(1.0, -2), "none"), (st1 + 0.08, zview(1.5, -1), "power4.out"),
          (st2, zview(1.5, 0), "none"), (st2 + 0.08, zview(2.0, 0), "power4.out"), (t1, zview(2.0, 1), "none")])
    S.mc([(t0, {"clipPath": clip_rect(0, 0, 1080, 1920, 0)}, None), (c0, {"clipPath": clip_rect(0, 0, 1080, 1920, 0)}, "none"),
          (c1, {"clipPath": clip_rect(px, py, pw, ph, pr)}, "power3.inOut")])
    S.act("head", [(t0, [-0.04, -0.05, 0.03], 0.3), (st1, [-0.02, 0.06, -0.03], 0.25), (st2, [-0.08, 0.0, 0.05], 0.25)])
    S.act("armL", [(t0, "open", 0.3), (st2 - 0.1, "low", 0.35)])
    S.act("armR", [(t0, "open", 0.3), (st2 - 0.1, "low", 0.35)])
    S.fx(st1, "click", 0.06)
    S.fx(st2, "click", 0.06)
