"""S11 — CHANGE THE CONTENT (25.58–28.54)  VO: "Lo ganti produk, ubah kalimat, geser timing,"
A porcelain editing console with four deliberate controls:
  product bay   — the selected (navy bottle) cartridge ejects on "ganti", the new (mint jar) cartridge comes over
                  from the side rack and SNAPS in on "produk" (apex), the old one parks in the rack;
  text strips   — three split-flap strips flip (3D, staggered) to a new bar pattern on "kalimat";
  timing ruler  — the knob turns and the keyframe diamonds slide along the ruler on "timing".
A preview reel on the right shows each edit as it lands. Then the three edited parts lift toward the camera
(hand-off: they float into S12's assembly)."""
from xk import box, screw, shadow, apex, rivets_line, r3
from kit_c import product_a, product_b, BARS_A, BARS_B, bars, ruler, diamond

SFX = []

MX, MY, MW, MH = 180, 470, 820, 850     # console body
BAY = (470, 540, 300, 300)              # product bay (screen coords)
RACK = (205, 540, 230, 470)             # side rack with two slots
PRV = (800, 530, 175, 330)              # preview reel
STR = (470, 890, 505, 180)              # split-flap strips
RUL = (205, 1110, 680, 70)              # ruler
KNOB = (900, 1100, 90)                  # x, y, size


def cart(id_, inner):
    """a product cartridge: porcelain block, navy grip rails, screws."""
    return (f'<div class="abs por" id="{id_}" style="{box(0, 0, 230, 230)}border-radius:28px">'
            f'<div class="abs" style="{box(14, 14, 202, 202)}border-radius:20px;background:linear-gradient(160deg,#fbfcfe,#e3ebf7);box-shadow:inset 0 0 0 1.5px rgba(172,198,231,.8)"></div>'
            f'{inner}'
            f'<div class="abs navy-side" style="{box(-6, 70, 8, 90)}border-radius:4px"></div><div class="abs navy-side" style="{box(228, 70, 8, 90)}border-radius:4px"></div>'
            f'{screw(26, 26, 20, 9)}{screw(204, 204, -40, 9)}</div>')


def build(S):
    s = S.id
    S.persp_origin = (590, 560)
    T0, T1 = S.t0, S.t1
    W54, W55, W56, W57, W58, W59 = (S.W(i) for i in (54, 55, 56, 57, 58, 59))   # ganti produk ubah kalimat geser timing
    # ---------------- far plane: workshop wall with pegboard holes + rails
    holes = "".join(f'<div class="abs" style="{box(220 + (k % 12) * 62, 420 + (k // 12) * 62, 8, 8)}border-radius:50%;background:rgba(172,198,231,.55)"></div>' for k in range(12 * 7))
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(190, 390, 800, 470)}border-radius:30px;opacity:.5"></div>{holes}'
                 f'<div class="abs" style="{box(120, 1420, 940, 6)}border-radius:3px;background:rgba(172,198,231,.5)"></div></div>')
    # ---------------- hero: console
    # contact shadow sits on its own plane far behind the tilted console: a flat plane at z=0 would intersect
    # the rotated console and Chrome's 3D sorting then slices a band of the console body over its children
    S.mid.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-160px) scale(1.08)">{shadow(150, MY + MH - 20, 900, 130, 1.0)}</div>')
    bx, by, bw, bh = BAY
    rx, ry, rw, rh = RACK
    px, py, pw, ph = PRV
    sx, sy, sw, sh = STR
    ux, uy, uw, uh = RUL
    kx, ky, ks = KNOB
    L = lambda x, y: (x - MX, y - MY)   # screen -> console local
    parts = []
    # console body + recessed wells
    parts.append(f'<div class="abs p3" style="{box(0, 0, MW, MH)}transform:translateZ(-30px)">'
                 f'<div class="abs navy-side" style="{box(10, 26, MW - 20, MH - 10)}border-radius:46px"></div></div>')
    parts.append(f'<div class="abs por" style="{box(0, 0, MW, MH)}border-radius:46px"></div>')
    def well(x, y, w, h, r=24, dark=False):
        lx, ly = L(x, y)
        bg = "linear-gradient(160deg,#294b77,#1c3354)" if dark else "linear-gradient(160deg,#dfe8f5,#eef3fa)"
        return f'<div class="abs" style="{box(lx - 10, ly - 10, w + 20, h + 20)}border-radius:{r}px;background:{bg};box-shadow:inset 0 4px 10px rgba(28,51,84,.35),inset 0 -1px 0 #fff"></div>'
    parts += [well(bx, by, bw, bh, 34, True), well(rx, ry, rw, rh, 30), well(px, py, pw, ph, 30), well(sx, sy, sw, sh, 22), well(ux, uy, uw, uh, 18)]
    parts.append(screws_four := "".join(screw(*p) for p in ((26, 26, 30), (MW - 26, 26, -20), (26, MH - 26, 60), (MW - 26, MH - 26, 10))))
    parts.append(rivets_line(60, MH - 22, MW - 60, MH - 22, 12))
    # vents
    parts.append("".join(f'<div class="abs" style="{box(MW - 200 + k * 16, MH - 70, 6, 34)}border-radius:3px;background:#cbdbf4;box-shadow:inset 0 1px 2px rgba(28,51,84,.3)"></div>' for k in range(8)))
    # rack: two slot outlines
    for k in range(2):
        lx, ly = L(rx, ry + k * 240)
        parts.append(f'<div class="abs" style="{box(lx, ly, 230, 230)}border-radius:28px;border:2px dashed rgba(41,75,119,.35)"></div>')
    # preview reel (shows each edit as it lands)
    lx, ly = L(px, py)
    prev = (f'<div class="abs por" style="{box(lx, ly, pw, ph)}border-radius:26px">'
            f'<div class="abs" style="{box(pw / 2 - 22, 10, 44, 5)}border-radius:3px;background:#cbdbf4"></div>'
            f'<div class="abs" style="{box(12, 26, pw - 24, ph - 52)}border-radius:12px;overflow:hidden;background:linear-gradient(170deg,#fbfcfe,#e2eaf6);box-shadow:inset 0 0 0 2px rgba(41,75,119,.45)">'
            f'<div class="abs" id="{s}-pvA">{product_a(f"{s}-pa", 22, 20, 0.72)}</div>'
            f'<div class="abs" id="{s}-pvB">{product_b(f"{s}-pb", 22, 20, 0.72)}</div>'
            f'<div class="abs" id="{s}-ptA">{bars(f"{s}-tA", 14, 160, BARS_A, 0.58)}</div>'
            f'<div class="abs" id="{s}-ptB">{bars(f"{s}-tB", 14, 160, BARS_B, 0.58)}</div>'
            f'<div class="abs" style="{box(14, ph - 92, pw - 52, 3)}background:#cbdbf4"></div>'
            + "".join(f'<div class="abs" id="{s}-pk{k}" style="{box(14 + k * 26, ph - 97, 12, 12)}border-radius:3px;background:#294b77;transform-origin:50% 50%"></div>' for k in range(4))
            + '</div></div>')
    parts.append(prev)
    # split-flap strips (3D flip around X): front = old bar, back = new bar
    lx, ly = L(sx, sy)
    for k in range(3):
        wa, inka = BARS_A[k]
        wb, inkb = BARS_B[k]
        yy = ly + 14 + k * 54
        face = lambda w, ink, back: (f'<div class="abs" style="{box(0, 0, sw - 40, 44)}border-radius:10px;background:linear-gradient(180deg,#ffffff,#e9f0fa);'
                                     f'box-shadow:inset 0 0 0 1.5px rgba(172,198,231,.8);backface-visibility:hidden;{"transform:rotateX(180deg);" if back else ""}">'
                                     f'<div class="abs" style="{box(18, 15, w * 1.55, 14)}border-radius:7px;background:{"#294b77" if ink else "#acc6e7"}"></div>'
                                     f'<div class="abs" style="{box(0, 21, sw - 40, 2)}background:rgba(172,198,231,.5)"></div></div>')
        parts.append(f'<div class="abs ice-side" style="{box(lx + 4, yy + 10, 14, 24)}border-radius:7px"></div>'
                     f'<div class="abs ice-side" style="{box(lx + sw - 18, yy + 10, 14, 24)}border-radius:7px"></div>'
                     f'<div class="abs p3" id="{s}-fl{k}" style="{box(lx + 20, yy, sw - 40, 44)}">{face(wa, inka, False)}{face(wb, inkb, True)}</div>')
    # ruler + keyframe diamonds + playhead
    lx, ly = L(ux, uy)
    parts.append(f'<div class="abs" style="{box(lx, ly, uw, uh)}">{ruler(f"{s}-rul", 0, 0, uw)}</div>')
    for k, x0 in enumerate((70, 210, 330, 520)):
        parts.append(f'<div class="abs" id="{s}-kf{k}" style="{box(lx + x0 - 14, ly - 34, 28, 28)}">{diamond(f"{s}-kd{k}", 14, 14, 26)}</div>')
    parts.append(f'<div class="abs" id="{s}-ph" style="{box(lx + 40, ly - 50, 3, uh + 56)}background:#3a6299;border-radius:2px"></div>')
    # timing knob
    lx, ly = L(kx, ky)
    knob_ticks = "".join(f'<div class="abs" style="{box(ks / 2 - 1, -12, 2, 8)}background:#294b77;transform-origin:1px {r3(ks / 2 + 12)}px;transform:rotate({a}deg)"></div>' for a in range(-120, 121, 30))
    parts.append(f'<div class="abs" style="{box(lx - 10, ly, ks, ks)}">{knob_ticks}'
                 f'<div class="abs" style="{box(4, 6, ks, ks)}border-radius:50%;background:rgba(28,51,84,.3)"></div>'
                 f'<div class="abs por" id="{s}-knob" style="{box(0, 0, ks, ks)}border-radius:50%">'
                 f'<div class="abs" style="{box(ks / 2 - 4, 8, 8, 30)}border-radius:4px;background:#294b77"></div>'
                 f'<div class="abs" style="{box(ks / 2 - 26, ks / 2 - 26, 52, 52)}border-radius:50%;box-shadow:inset 0 0 0 2px rgba(172,198,231,.8)"></div></div></div>')
    # status LEDs
    parts.append(f'<div class="led-off" id="{s}-led0" style="left:{MW - 140}px;top:30px"></div><div class="led-off" id="{s}-led1" style="left:{MW - 110}px;top:30px"></div><div class="led-off" id="{s}-led2" style="left:{MW - 80}px;top:30px"></div>')
    parts.append(f'<div class="led" id="{s}-ledon0" style="left:{MW - 140}px;top:30px"></div><div class="led" id="{s}-ledon1" style="left:{MW - 110}px;top:30px"></div><div class="led" id="{s}-ledon2" style="left:{MW - 80}px;top:30px"></div>')
    # cartridges (moving, on top): old in the bay, new in the rack's top slot
    lbx, lby = L(bx + 35, by + 35)
    lrx, lry = L(rx, ry)
    parts.append(f'<div class="abs p3" id="{s}-cO" style="{box(lbx, lby, 230, 230)}">{cart(f"{s}-cOi", product_a(f"{s}-po", 55, 30, 1.0))}</div>')
    parts.append(f'<div class="abs p3" id="{s}-cN" style="{box(lrx, lry, 230, 230)}">{cart(f"{s}-cNi", product_b(f"{s}-pn", 55, 30, 1.0))}</div>')
    # selection ring (continues from S10)
    rcx, rcy = bx + bw / 2, by + bh / 2
    parts.append(f'<div class="abs" id="{s}-sel" style="{box(rcx - MX - 160, rcy - MY - 160, 320, 320)}">'
                 f'<div class="abs" style="{box(0, 0, 320, 320)}border-radius:50%;border:5px solid #294b77;box-shadow:0 0 0 10px rgba(203,219,244,.55),0 0 30px rgba(172,198,231,.9)"></div>'
                 f'<div class="abs" style="{box(16, 16, 288, 288)}border-radius:50%;border:2px dashed rgba(41,75,119,.6)"></div></div>')
    S.mid.append(f'<div class="abs p3" id="{s}-con" style="{box(MX, MY, MW, MH)}">{"".join(parts)}</div>')
    # ---------------- near plane: out-of-focus spare strip + screw tray
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs por" style="{box(-70, 620, 150, 150)}border-radius:50%;filter:blur(5px);opacity:.85"></div>'
                  f'<div class="abs" style="{box(1010, 470, 120, 120)}border-radius:50%;border:14px solid rgba(255,255,255,.75);filter:blur(5px)"></div></div>')
    apex(S, S.near, f"{s}-ap", bx + bw / 2 + 10, by + bh / 2 - 40, W55 + 0.12, size=620, sparks=7, seed=21)

    # ================= motion
    S.cam([(T0, {"z": 60, "x": 0, "y": 60, "rotationX": 6, "rotationY": 0}, None),
           (W55 + 0.1, {"z": 30, "y": 20, "rotationX": 7, "rotationY": -3}, "power2.inOut"),
           (W57 + 0.1, {"z": 10, "x": -20, "y": 0, "rotationY": 2}, "sine.inOut"),
           (W59 + 0.2, {"z": 20, "x": -30, "y": -30, "rotationX": 9, "rotationY": 0}, "power2.inOut"),
           (T1, {"z": 230, "x": -60, "y": -40, "rotationX": 4}, "power3.in")])
    S.keys(f"#{s}-con", [(T0, {"rotationX": 10, "rotationY": -6}, None), (T1, {"rotationX": 6, "rotationY": 3}, "sine.inOut")])
    # selection ring: holds, tightens, releases as the cartridge ejects
    S.init(f"#{s}-sel", {"opacity": 1, "scale": 1.02, "rotation": 20})
    S.ft(f"#{s}-sel", {"scale": 1.02, "rotation": 20}, {"scale": 0.9, "rotation": 50}, T0, W54 - T0, "power2.in")
    S.ft(f"#{s}-sel", {"opacity": 1, "scale": 0.9}, {"opacity": 0, "scale": 1.3}, W54, 0.25, "power2.out")
    # old cartridge: press (anticipation) -> eject up/forward -> swing into the rack's lower slot
    lbx, lby = L(bx + 35, by + 35)
    dx_r, dy_r = (rx - (bx + 35)), (ry + 240 - (by + 35))
    S.keys(f"#{s}-cO", [(T0, {"x": 0, "y": 0, "z": 4, "rotation": 0}, None),
                        (W54 - 0.12, {"y": 6, "z": -4}, "power2.in"),
                        (W54 + 0.12, {"y": -70, "z": 120, "rotation": -6}, "power3.out"),
                        (W55 + 0.3, {"x": dx_r, "y": dy_r, "z": 20, "rotation": 0}, "power2.inOut"),
                        (W55 + 0.5, {"z": 4}, "power2.out")])
    # new cartridge: lift from the rack -> fly over -> SNAP into the bay on "produk"
    S.keys(f"#{s}-cN", [(T0, {"x": 0, "y": 0, "z": 4, "rotation": 0, "scale": 1}, None),
                        (W54 + 0.02, {"z": 4}, "none"),
                        (W54 + 0.16, {"z": 150, "y": -30, "rotation": 5}, "power2.out"),
                        (W55 + 0.06, {"x": (bx + 35) - rx, "y": (by + 35) - ry - 6, "z": 40, "rotation": 0}, "power3.inOut"),
                        (W55 + 0.14, {"y": (by + 35) - ry, "z": 0, "scale": 0.97}, "power4.in"),
                        (W55 + 0.34, {"z": 4, "scale": 1}, "back.out(3)"),
                        (W59 + 0.22, {"z": 4}, "none"),
                        (T1, {"z": 190, "y": (by + 35) - ry - 40, "rotation": -5}, "power2.in")])
    # preview reel follows each edit
    S.init(f"#{s}-pvB", {"opacity": 0, "scale": 0.6, "transformOrigin": "60px 80px"})
    S.ft(f"#{s}-pvB", {"opacity": 0, "scale": 0.6}, {"opacity": 1, "scale": 1}, W55 + 0.16, 0.32, "back.out(2.2)")
    S.init(f"#{s}-pvA", {"opacity": 1})
    S.ft(f"#{s}-pvA", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -20}, W55 + 0.1, 0.16, "power2.in")
    S.init(f"#{s}-ptB", {"opacity": 0})
    S.ft(f"#{s}-ptB", {"opacity": 0, "x": -10}, {"opacity": 1, "x": 0}, W57 + 0.14, 0.24, "power3.out")
    S.init(f"#{s}-ptA", {"opacity": 1})
    S.ft(f"#{s}-ptA", {"opacity": 1}, {"opacity": 0}, W57 + 0.06, 0.12, "power1.in")
    # split-flap strips flip on "kalimat" (start on "ubah")
    for k in range(3):
        a = W56 + 0.12 + k * 0.1
        S.init(f"#{s}-fl{k}", {"rotationX": 0})
        S.ft(f"#{s}-fl{k}", {"rotationX": 0}, {"rotationX": -20}, a - 0.12, 0.12, "power2.in")
        S.ft(f"#{s}-fl{k}", {"rotationX": -20}, {"rotationX": -180}, a, 0.32 + k * 0.02, "back.out(1.6)")
        S.init(f"#{s}-fl{k}", {"z": 0})
        S.ft(f"#{s}-fl{k}", {"z": 0}, {"z": 120 + k * 25}, W59 + 0.3 + k * 0.04, T1 - W59 - 0.3 - k * 0.04, "power2.in")
    # timing: knob turns on "geser", keyframes slide and land on "timing", playhead sweeps
    S.init(f"#{s}-knob", {"rotation": -60})
    S.ft(f"#{s}-knob", {"rotation": -60}, {"rotation": -75}, W58 - 0.1, 0.1, "power2.in")
    S.ft(f"#{s}-knob", {"rotation": -75}, {"rotation": 70}, W58, W59 - W58 + 0.12, "power3.inOut")
    for k, dx in enumerate((40, 70, 110, 60)):
        S.init(f"#{s}-kf{k}", {"x": 0, "y": 0})
        S.ft(f"#{s}-kf{k}", {"x": 0, "y": 0}, {"x": dx, "y": -10}, W58 + 0.04 + k * 0.05, W59 - W58 - 0.05, "power3.inOut")
        S.ft(f"#{s}-kf{k}", {"y": -10}, {"y": 0}, W59 + k * 0.05, 0.22, "back.out(3)")
        S.init(f"#{s}-kf{k}", {"z": 0})
        S.ft(f"#{s}-kf{k}", {"z": 0}, {"z": 110}, W59 + 0.34, T1 - W59 - 0.34, "power2.in")
    for k, dx in enumerate((6, 10, 16, 8)):
        S.init(f"#{s}-pk{k}", {"x": 0})
        S.ft(f"#{s}-pk{k}", {"x": 0}, {"x": dx}, W59 - 0.05 + k * 0.04, 0.25, "power3.out")
    S.init(f"#{s}-ph", {"x": 0})
    S.ft(f"#{s}-ph", {"x": 0}, {"x": 600}, T0 + 0.1, T1 - T0 - 0.1, "none")
    # LEDs confirm each edit (mint)
    for k, t in enumerate((W55 + 0.16, W57 + 0.3, W59 + 0.18)):
        S.init(f"#{s}-ledon{k}", {"opacity": 0, "scale": 0.4})
        S.ft(f"#{s}-ledon{k}", {"opacity": 0, "scale": 0.4}, {"opacity": 1, "scale": 1}, t, 0.18, "back.out(3)")
    SFX.extend([(W55 + 0.14, "click", 0.15), (W57 + 0.2, "key", 0.1), (W59 + 0.02, "click", 0.1)])
