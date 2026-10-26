"""S02 — THE X-RAY REVEAL (3.24–5.18)  VO: "Lihat. Layarnya kebuka."
Same mechanical phone, seen closer (gears already turning, glass unlocked from S01). "Lihat.": the glass dips as
anticipation and the seam pulses. "Layarnya": the real 3D glass rises off its left-edge hinge and swings. "kebuka.":
it lands in the photo's floating pose (overshoot + settle) while the camera pulls back to reveal the opened phone;
gears run faster, light sweep, REF-H apex. Hand-off: the glass turns square-on and flies at the camera, whitening
into a glass sheet (S03 opens on a centred, square-on glass type plate)."""
import math
import numpy as np
from xk import box, r3
import kit_phone as K
from kit_phone import phone_rig, Placement, glass_point, gears_motion, apex_h, bokeh_far, rig_point, GW, GH, GX0, GY0, OPEN
from scenes.s01 import screen_html

SFX = [(4.06, "whoosh", 0.06), (4.40, "click", 0.10), (4.95, "whoosh", 0.07)]
PLACE = Placement(0.85, (590.5, 635.5), (590, 937))      # body + open glass fit the hero zone (top ~440)


# ------------------------------------------------------------------ CSS math for the glass child transform
def _R(rx, ry, rz):
    a, b, c = (math.radians(v) for v in (rx, ry, rz))
    Rx = np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])
    Ry = np.array([[math.cos(b), 0, math.sin(b)], [0, 1, 0], [-math.sin(b), 0, math.cos(b)]])
    Rz = np.array([[math.cos(c), -math.sin(c), 0], [math.sin(c), math.cos(c), 0], [0, 0, 1]])
    return Rz @ Ry @ Rx                               # GSAP order: rotate(z) rotateY rotateX


def glass_rig(x, y, z, rx, ry, rz, sc=1.0, origin=(0.5, 0.5)):
    """rig px of the glass corners (tl, tr, br, bl) for a GSAP child transform."""
    ox, oy = GW * origin[0], GH * origin[1]
    R = _R(rx, ry, rz)
    out = []
    for u, v in ((0, 0), (GW, 0), (GW, GH), (0, GH)):
        p = R @ (np.array([u - ox, v - oy, 0.0]) * sc) + np.array([ox + x, oy + y, z])
        out.append(rig_point(GX0 + p[0], GY0 + p[1], p[2] + 1.0))
    return np.array(out)


def square_on_angles():
    C = K.M4[:3, :3]
    U, _, Vt = np.linalg.svd(C)
    Rt = (U @ Vt).T                                    # child rotation that cancels the face's 3D pose
    ry = -math.degrees(math.asin(max(-1, min(1, Rt[2, 0]))))
    rz = math.degrees(math.atan2(Rt[1, 0], Rt[0, 0]))
    rx = math.degrees(math.atan2(Rt[2, 1], Rt[2, 2]))
    return rx, ry, rz


def fly_target(target_rig, width_rig, z=380.0):
    rx, ry, rz = square_on_angles()
    x, y, sc = OPEN["x"], OPEN["y"], 1.0
    for _ in range(60):
        c = glass_rig(x, y, z, rx, ry, rz, sc)
        ctr = c.mean(axis=0); w = np.linalg.norm(c[1] - c[0])
        sc *= (width_rig / w) ** 0.7
        # move in face-local units along the projected local axes
        J = np.zeros((2, 2))
        for k in range(2):
            d = [0, 0]; d[k] = 1.0
            c2 = glass_rig(x + d[0], y + d[1], z, rx, ry, rz, sc).mean(axis=0)
            J[:, k] = c2 - glass_rig(x, y, z, rx, ry, rz, sc).mean(axis=0)
        step = np.linalg.solve(J, np.array(target_rig) - glass_rig(x, y, z, rx, ry, rz, sc).mean(axis=0))
        x += step[0]; y += step[1]
    c = glass_rig(x, y, z, rx, ry, rz, sc)
    tilt = math.degrees(math.atan2(c[1][1] - c[0][1], c[1][0] - c[0][0]))
    return {"x": x, "y": y, "z": z, "rotationX": rx, "rotationY": ry, "rotationZ": rz, "scale": sc}, tilt


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W7, W8, W9 = S.W(7), S.W(8), S.W(9)               # "Lihat." 3.34, "Layarnya" 4.04, "kebuka." 4.38
    bcx, bcy = PLACE.pt(530, 733)                      # body centre (scene px, pre-camera)
    S.persp_origin = (r3(bcx), r3(bcy))
    # ---------------- far / near planes
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(200, 280, 780, 1260)}border-radius:390px 390px 40px 40px;opacity:.45"></div>'
                 f'<div class="abs" style="{box(250, 340, 680, 1170)}border-radius:340px 340px 30px 30px;border:2px solid rgba(255,255,255,.85)"></div>'
                 + "".join(K.bokeh_far(202, 6)) + '</div>')
    gx, gy = PLACE.pt(*glass_point(OPEN["x"], OPEN["y"], OPEN["z"]))
    S.far.append(f'<div class="abs" id="{s}-halo" style="{box(gx - 560, gy - 560, 1120, 1120)}border-radius:50%;'
                 f'background:radial-gradient(circle,rgba(255,255,255,.95) 0%,rgba(255,255,255,0) 64%)"></div>')
    sx_, sy_ = PLACE.pt(600, 1222)
    S.mid.append(f'<div class="abs" id="{s}-csh" style="{box(sx_ - 400, sy_ - 26, 790, 92)}border-radius:50%;'
                 f'background:radial-gradient(ellipse,rgba(28,51,84,.34),rgba(28,51,84,.12) 45%,rgba(28,51,84,0) 72%)"></div>')
    S.mid.append(phone_rig(s, PLACE, screen_html(s)))
    apex_h(S, S.mid, f"{s}-ap", gx, gy, W9, size=700, stars=14, seed=23, punch=f"#{s}-punch")
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(-60, 560, 190, 190)}border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"></div>'
                  f'<div class="abs" style="{box(940, 1300, 160, 160)}border-radius:50%;filter:blur(8px);opacity:.7;'
                  f'background:radial-gradient(circle at 35% 30%,#ffffff,#e8f0fb 45%,#acc6e7 100%)"></div></div>')

    # ---------------- camera: cut in close on the movement, pull back to reveal the opened phone
    S.cam([(t0, {"z": 520, "x": 0, "y": 0, "rotationY": 2, "rotationX": 0, "rotationZ": -1.5}, None),
           (W7 + 0.2, {"z": 470, "rotationZ": -0.8}, "power2.out"),
           (W8, {"z": 330, "rotationY": 0.5}, "sine.inOut"),
           (W9 + 0.38, {"z": 0, "rotationY": -2, "rotationZ": 0}, "power3.inOut"),
           (4.92, {"z": 30, "rotationY": 0}, "sine.inOut"),
           (t1, {"z": 30}, "none")])
    S.init(f"#{s}-halo", {"opacity": 0.6, "scale": 0.9})
    S.ft(f"#{s}-halo", {"opacity": 0.6, "scale": 0.9}, {"opacity": 1, "scale": 1.06}, W8, W9 - W8 + 0.3, "power2.out")
    S.keys(f"#{s}-float", [(t0, {"y": -4, "rotation": 0.4}, None), (W9, {"y": -12, "rotation": -0.5}, "sine.inOut"), (t1, {"y": -6, "rotation": 0}, "sine.inOut")])
    # S01 end states carried over
    S.init(f"#{s}-scr", {"opacity": 0})
    for k in range(4):
        S.init(f"#{s}-pin{k}", {"x": -16 if k < 2 else 16})
    S.init(f"#{s}-seam", {"opacity": 0})
    S.ft(f"#{s}-seam", {"opacity": 0}, {"opacity": 0.6}, W7, 0.1, "power2.out")
    S.ft(f"#{s}-seam", {"opacity": 0.6}, {"opacity": 0.15}, W7 + 0.1, 0.5, "power1.in")
    S.ft(f"#{s}-seam", {"opacity": 0.15}, {"opacity": 0}, W9, 0.25, "power1.in")
    gears_motion(S, s, t0, t1)
    # ---------------- the glass: dip ("Lihat") -> rise + swing on its hinge ("Layarnya") -> land open ("kebuka.")
    g = f"#{s}-glass"
    st0 = {"x": -5, "y": 3, "z": 46, "rotationX": 2.2, "rotationY": -2, "rotationZ": 0, "scale": 1, "transformOrigin": "0% 50%"}
    dip = dict(st0, z=18, rotationX=-1.0, rotationY=1.0)
    swing = dict(st0, x=-16, y=10, z=150, rotationX=-12, rotationY=24)
    openp = dict(st0, x=OPEN["x"], y=OPEN["y"], z=OPEN["z"], rotationX=0, rotationY=0)
    S.init(g, st0)
    S.ft(g, st0, dip, W7 + 0.02, 0.32, "power2.inOut")
    S.ft(g, dip, swing, W8 - 0.02, W9 - W8 - 0.06, "power2.out")
    S.ft(g, swing, openp, W9 - 0.06, 0.5, "back.out(1.6)")
    # glass shadow on the face follows the lift (offset grows toward the lower right, softens)
    S.init(f"#{s}-gsh", {"opacity": 0.36, "x": 14, "y": 20, "scale": 1})
    S.ft(f"#{s}-gsh", {"opacity": 0.36, "x": 14, "y": 20, "scale": 1}, {"opacity": 0.5, "x": 6, "y": 9, "scale": 1}, W7 + 0.02, 0.32, "power2.inOut")
    S.ft(f"#{s}-gsh", {"opacity": 0.5, "x": 6, "y": 9, "scale": 1}, {"opacity": 0.22, "x": 46, "y": 66, "scale": 1.04}, W8, W9 - W8 + 0.4, "power2.out")
    # specular sweep on landing
    S.init(f"#{s}-spec", {"x": 0, "rotation": 16})
    S.ft(f"#{s}-spec", {"x": 0, "rotation": 16}, {"x": GW + 560, "rotation": 16}, W9 + 0.02, 0.55, "power2.inOut")
    # ---------------- hand-off: square-on fly-out toward the camera, whitening into a glass sheet
    m = 2000 / (2000 - 30)                              # camera z 30 at the end
    tx_pre = bcx + (590 - bcx) / m; ty_pre = bcy + (900 - bcy) / m
    rig_tx = (tx_pre - PLACE.x) / PLACE.s + PLACE.ax; rig_ty = (ty_pre - PLACE.y) / PLACE.s + PLACE.ay
    fly, tilt = fly_target((rig_tx, rig_ty), 1500 / (PLACE.s * m))
    open_c = dict(openp, transformOrigin="50% 50%")
    S.ft(g, open_c, dict(fly, transformOrigin="50% 50%"), 4.92, t1 - 4.92 - 0.004, "power3.in")
    S.init(f"#{s}-gwhite", {"opacity": 0})
    S.ft(f"#{s}-gwhite", {"opacity": 0}, {"opacity": 0.9}, 4.98, t1 - 4.98 - 0.004, "power2.in")
    S.raw(f"// fly-out target {fly} (residual tilt {tilt:.2f} deg)")
