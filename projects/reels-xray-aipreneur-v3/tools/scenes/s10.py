"""S10 — MODULAR TEMPLATE DISCOVERY (22.82–25.58)  VO: "Sekarang bayangin kalau templatenya udah modular."
The finished reel from S09 drops into the top slot of a porcelain cabinet. On "bayangin" the doors swing open
(3D hinges) onto a navy interior with four module cartridges: content (paper sheets), visual object (product),
motion (path + dot) and timing (dial). They rise on "templatenya"; on "modular" they slide together and a reel
frame locks around them (apex). A selection ring then lands on the product module (hand-off to S11)."""
from xk import box, screw, shadow, apex, rivets_line, gear_svg, r3
from kit_c import product_b, product_a

SFX = []

CX, CY, CW, CH = 270, 500, 640, 720          # cabinet body
GX, GY = 330, 600                            # interior module grid origin
MW, MH, GAP = 250, 250, 20                   # module cartridge size / gap


def module_inner(kind, p):
    """physical symbol of each module (no labels)."""
    if kind == "content":   # stacked paper sheets with abstract lines
        sh = []
        for k in range(3):
            sh.append(f'<div class="abs paper" style="{box(52 + k * 10, 46 + k * 12, 130, 150)}border-radius:6px">'
                      + "".join(f'<div class="abs" style="{box(16, 22 + j * 20, [90, 70, 98, 60, 84][j], 7)}border-radius:4px;background:{"#294b77" if j == 0 else "#cbdbf4"}"></div>' for j in range(5))
                      + '</div>')
        return "".join(sh)
    if kind == "object":    # the product
        return product_a(f"{p}-prod", 64, 34, 1.0)
    if kind == "motion":    # an S path with keyframe dots and a riding card
        return (f'<svg class="abs" style="left:0;top:0" width="{MW}" height="{MH}" viewBox="0 0 {MW} {MH}">'
                f'<path d="M40,190 C90,190 90,70 140,110 S200,60 214,56" fill="none" stroke="#cbdbf4" stroke-width="10" stroke-linecap="round"/>'
                f'<path d="M40,190 C90,190 90,70 140,110 S200,60 214,56" fill="none" stroke="#294b77" stroke-width="3" stroke-dasharray="6 9" stroke-linecap="round"/>'
                f'<circle cx="40" cy="190" r="9" fill="#294b77"/><circle cx="140" cy="110" r="9" fill="#294b77"/><circle cx="214" cy="56" r="9" fill="#294b77"/></svg>'
                f'<div class="abs mr-navy" id="{p}-mcard" style="{box(122, 92, 40, 34)}border-radius:8px"></div>')
    if kind == "timing":    # dial with ticks + pointer
        ticks = "".join(f'<div class="abs" style="{box(124, 46, 2, 14 if k % 3 == 0 else 8)}background:{"#294b77" if k % 3 == 0 else "#9fb6d6"};transform-origin:1px 79px;transform:rotate({k * 30}deg)"></div>' for k in range(12))
        return (f'<div class="abs por" style="{box(55, 55, 140, 140)}border-radius:50%"></div>{ticks}'
                f'<div class="abs" id="{p}-dial" style="{box(55, 55, 140, 140)}"><div class="abs" style="{box(68, 18, 4, 56)}border-radius:2px;background:#294b77"></div>'
                f'<div class="abs" style="{box(58, 58, 24, 24)}border-radius:50%;background:linear-gradient(150deg,#3a6299,#1c3354)"></div></div>')
    return ""


def build(S):
    s = S.id
    S.persp_origin = (590, 560)
    W47, W48, W50, W52 = S.W(47), S.W(48), S.W(50), S.W(52)       # sekarang, bayangin, templatenya, modular
    T0, T1 = S.t0, S.t1
    # ---------------- far plane: tall shelving backdrop with rails
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(170, 360, 840, 1120)}border-radius:46px;opacity:.5"></div>'
                 + "".join(f'<div class="abs" style="{box(200, 520 + k * 230, 780, 8)}border-radius:4px;background:rgba(172,198,231,.55)"></div>' for k in range(4))
                 + "".join(f'<div class="abs" style="{box(230 + k * 180, 400, 3, 1040)}background:rgba(203,219,244,.5)"></div>' for k in range(5))
                 + '</div>')
    # ---------------- hero: cabinet
    S.mid.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-160px) scale(1.08)">{shadow(200, CY + CH + 10, 780, 120, 1.0, id_=f"{s}-csh")}</div>')
    feet = "".join(f'<div class="abs navy-side" style="{box(fx, CH - 6, 46, 40)}border-radius:0 0 12px 12px"></div>' for fx in (40, CW - 86))
    # interior (navy, with module slots)
    slots, mods = [], []
    kinds = ["content", "object", "motion", "timing"]
    for k, kind in enumerate(kinds):
        mx = GX - CX + (k % 2) * (MW + GAP)
        my = GY - CY + (k // 2) * (MH + GAP)
        slots.append(f'<div class="abs" style="{box(mx - 8, my - 8, MW + 16, MH + 16)}border-radius:30px;background:rgba(10,20,40,.35);box-shadow:inset 0 4px 10px rgba(0,0,0,.35)"></div>')
        mods.append(f'<div class="abs p3" id="{s}-mw{k}" style="{box(mx, my, MW, MH)}">'
                    f'<div class="abs por" id="{s}-m{k}" style="{box(0, 0, MW, MH)}border-radius:26px">{module_inner(kind, f"{s}-m{k}")}'
                    f'{screw(18, 18, 30, 9)}{screw(MW - 18, MH - 18, -30, 9)}</div></div>')
    interior = (f'<div class="abs" style="{box(24, 24, CW - 48, CH - 48)}border-radius:30px;background:linear-gradient(160deg,#3a6299 0%,#294b77 35%,#1c3354 100%);'
                f'box-shadow:inset 0 0 0 3px rgba(203,219,244,.25),inset 0 18px 40px rgba(0,0,0,.35)"></div>'
                + rivets_line(46, 50, CW - 46, 50, 9) + "".join(slots))
    # reel frame that locks around the assembled modules on "modular"
    fx0, fy0 = GX - CX + 12 - 26, GY - CY + 12 - 70
    fw, fh = 2 * (MW - 12) + 8 + 52, 2 * (MH - 12) + 8 + 140
    frame = (f'<div class="abs" id="{s}-rf" style="{box(fx0, fy0, fw, fh)}border-radius:46px;border:22px solid #fbfcfe;'
             f'box-shadow:0 0 0 2px rgba(172,198,231,.9),inset 0 0 0 2px rgba(41,75,119,.5),0 24px 40px -18px rgba(28,51,84,.45)">'
             f'<div class="abs" style="{box(fw / 2 - 22 - 40, -16, 80, 8)}border-radius:4px;background:#cbdbf4"></div>'
             f'<div class="abs" style="{box(fw / 2 - 22 + 50, -18, 12, 12)}border-radius:50%;background:#294b77"></div>'
             f'<div class="abs" id="{s}-rfb1" style="{box(20, fh - 44 - 52, 220, 12)}border-radius:6px;background:#294b77"></div>'
             f'<div class="abs" id="{s}-rfb2" style="{box(20, fh - 44 - 30, 300, 10)}border-radius:5px;background:#cbdbf4"></div></div>')
    # doors (3D hinges on the outer edges)
    def door(side):
        dx = 0 if side == "L" else CW / 2
        hx = 18 if side == "L" else CW / 2 - 18
        knob_x = CW / 2 - 40 if side == "L" else 26
        return (f'<div class="abs p3" id="{s}-d{side}" style="{box(dx, 0, CW / 2, CH)}">'
                f'<div class="abs por" style="{box(0, 0, CW / 2, CH)}border-radius:{"34px 6px 6px 34px" if side == "L" else "6px 34px 34px 6px"}">'
                f'<div class="abs" style="{box(30, 40, CW / 2 - 60, CH - 80)}border-radius:20px;box-shadow:inset 2px 2px 0 rgba(255,255,255,.9),inset -2px -3px 0 rgba(172,198,231,.7),inset 0 0 0 1px rgba(172,198,231,.5)"></div>'
                f'<div class="abs" style="{box(54, 90, CW / 2 - 108, 3)}background:rgba(172,198,231,.6)"></div>'
                f'<div class="abs" style="{box(54, CH - 94, CW / 2 - 108, 3)}background:rgba(172,198,231,.6)"></div>'
                f'<div class="abs navy-side" style="{box(knob_x, CH / 2 - 70, 14, 140)}border-radius:7px;box-shadow:0 6px 10px rgba(28,51,84,.35)"></div>'
                + "".join(f'<div class="abs ice-side" style="{box(hx - 9, hy, 18, 64)}border-radius:9px;box-shadow:inset 0 0 0 1.5px rgba(41,75,119,.35)"></div>' for hy in (70, CH - 134))
                + f'{screw(hx, 150, 20, 10)}{screw(hx, CH - 150, -40, 10)}</div></div>')
    top_slot = (f'<div class="abs" style="{box(CW / 2 - 130, -18, 260, 30)}border-radius:15px;background:linear-gradient(180deg,#1c3354,#294b77);box-shadow:inset 0 3px 6px rgba(0,0,0,.4),0 2px 0 #fff"></div>')
    S.mid.append(f'<div class="abs p3" id="{s}-cab" style="{box(CX, CY, CW, CH)}">'
                 f'<div class="abs p3" style="{box(0, 0, CW, CH)}transform:translateZ(-46px)"><div class="abs por" style="{box(-16, -26, CW + 32, CH + 40)}border-radius:44px"></div>{feet}</div>'
                 f'<div class="abs p3" style="{box(0, 0, CW, CH)}transform:translateZ(-40px)">{interior}<div class="abs p3" id="{s}-mods" style="{box(0, 0, CW, CH)}">{"".join(mods)}</div></div>{frame}'
                 f'<div class="abs p3" style="{box(0, 0, CW, CH)}transform:translateZ(6px)">{door("L")}{door("R")}</div><div class="abs p3" style="{box(0, 0, CW, CH)}transform:translateZ(8px)">{top_slot}</div>'
                 f'<div class="abs" style="{box(CW / 2 - 60, -96, 120, 92)}overflow:hidden"><div class="abs" id="{s}-drop" style="{box(10, 0, 100, 140)}">'
                 f'<div class="abs por" style="{box(0, 0, 100, 140)}border-radius:16px"><div class="abs" style="{box(9, 12, 82, 116)}border-radius:9px;background:linear-gradient(160deg,#3a6299,#1c3354)"></div>'
                 f'<div class="abs" style="{box(18, 84, 56, 6)}border-radius:3px;background:#cbdbf4"></div><div class="abs" style="{box(18, 98, 38, 6)}border-radius:3px;background:#9fd8c4"></div></div></div></div>'
                 f'</div>')
    # selection ring + corner brackets for the product module (top-right slot)
    px, py = GX + MW + GAP, GY
    rcx, rcy = px + MW / 2, py + MH / 2
    S.mid.append(f'<div class="abs" id="{s}-sel" style="{box(rcx - 175, rcy - 175, 350, 350)}">'
                 f'<div class="abs" style="{box(0, 0, 350, 350)}border-radius:50%;border:5px solid #294b77;box-shadow:0 0 0 10px rgba(203,219,244,.55),0 0 30px rgba(172,198,231,.9)"></div>'
                 f'<div class="abs" style="{box(18, 18, 314, 314)}border-radius:50%;border:2px dashed rgba(41,75,119,.6)"></div>'
                 + "".join(f'<div class="abs" style="{box(171, -14, 8, 26)}border-radius:4px;background:#294b77;transform-origin:4px 189px;transform:rotate({a}deg)"></div>' for a in (0, 90, 180, 270))
                 + '</div>')
    # ---------------- near plane: out-of-focus glass rod + a floating spare module
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(960, 380, 34, 520)}border-radius:17px;background:linear-gradient(90deg,#ffffff,#cbdbf4);filter:blur(4px);opacity:.85"></div>'
                  f'<div class="abs por" style="{box(-60, 1000, 170, 170)}border-radius:28px;filter:blur(5px);opacity:.8"></div></div>')
    apex(S, S.near, f"{s}-ap", 590, 860, W52 + 0.04, size=760, sparks=8, seed=12)

    # ================= motion
    S.cam([(T0, {"z": 120, "x": 0, "y": 0, "rotationY": 0, "rotationX": 0}, None),
           (W48 - 0.05, {"z": 40, "rotationY": -4, "rotationX": 2}, "power2.out"),
           (W52 - 0.1, {"z": 0, "rotationY": 3, "rotationX": 1}, "sine.inOut"),
           (W52 + 0.35, {"z": 60, "rotationY": 0}, "power3.out"),
           (T1, {"z": 300, "x": -240, "y": 110, "rotationY": -6}, "power3.in")])
    S.keys(f"#{s}-cab", [(T0, {"rotationY": -14, "rotationX": 3}, None),
                         (W48 + 0.3, {"rotationY": -6, "rotationX": 2}, "power2.out"),
                         (T1, {"rotationY": 2, "rotationX": 0}, "sine.inOut")])
    # reel from S09 drops into the top slot
    S.keys(f"#{s}-drop", [(T0, {"y": -10}, None), (T0 + 0.32, {"y": 100}, "power2.in")])
    # doors open on "bayangin": slight anticipation (they press shut), then swing
    S.keys(f"#{s}-dL", [(T0, {"rotationY": 0, "transformOrigin": "0% 50%"}, None),
                        (W48 - 0.1, {"rotationY": 3}, "power2.in"),
                        (W48 + 0.6, {"rotationY": -112}, "back.out(1.3)")])
    S.keys(f"#{s}-dR", [(T0, {"rotationY": 0, "transformOrigin": "100% 50%"}, None),
                        (W48 - 0.06, {"rotationY": -3}, "power2.in"),
                        (W48 + 0.66, {"rotationY": 112}, "back.out(1.3)")])
    # modules rise forward on "templatenya", slide together on "modular"
    for k in range(4):
        dx = (1 if k % 2 == 0 else -1) * (GAP / 2 + 6)
        dy = (1 if k < 2 else -1) * (GAP / 2 + 6)
        S.keys(f"#{s}-mw{k}", [(T0, {"z": 8, "x": 0, "y": 0, "scale": 0.96}, None),
                               (W50 - 0.05 + k * 0.07, {"z": 8}, "none"),
                               (W50 + 0.4 + k * 0.07, {"z": 80, "scale": 1}, "back.out(1.8)"),
                               (W52 - 0.12, {"z": 76, "x": -dx * 0.3, "y": -dy * 0.3}, "power2.in"),
                               (W52 + 0.08, {"z": 64, "x": dx, "y": dy}, "power4.out")])
    # module micro-motion: motion card rides, dial ticks
    S.init(f"#{s}-m2-mcard", {"x": -90, "y": 80})
    S.ft(f"#{s}-m2-mcard", {"x": -90, "y": 80}, {"x": 70, "y": -48}, W48, 1.1, "power2.inOut")
    S.ft(f"#{s}-m2-mcard", {"x": 70, "y": -48}, {"x": -90, "y": 80}, W48 + 1.15, 1.1, "power2.inOut")
    S.init(f"#{s}-m3-dial", {"rotation": -40})
    S.ft(f"#{s}-m3-dial", {"rotation": -40}, {"rotation": 50}, W50, 0.5, "back.out(2)")
    S.ft(f"#{s}-m3-dial", {"rotation": 50}, {"rotation": 140}, W52 + 0.2, 0.5, "back.out(2)")
    # reel frame locks around the 4 modules
    S.init(f"#{s}-rf", {"opacity": 0, "scale": 1.18, "z": 40})
    S.ft(f"#{s}-rf", {"opacity": 0, "scale": 1.18, "z": 40}, {"opacity": 1, "scale": 1, "z": 40}, W52 - 0.08, 0.22, "power3.in")
    S.ft(f"#{s}-rf", {"scale": 1}, {"scale": 1.025}, W52 + 0.14, 0.08, "power2.out")
    S.ft(f"#{s}-rf", {"scale": 1.025}, {"scale": 1}, W52 + 0.22, 0.25, "power2.inOut")
    for b in ("rfb1", "rfb2"):
        S.init(f"#{s}-{b}", {"scaleX": 0, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-{b}", {"scaleX": 0}, {"scaleX": 1}, W52 + 0.1, 0.35, "power3.out")
    # selection ring on the product module (hand-off to S11)
    S.init(f"#{s}-sel", {"opacity": 0, "scale": 1.6, "rotation": -40, "z": 90})
    S.ft(f"#{s}-sel", {"opacity": 0, "scale": 1.6, "rotation": -40, "z": 90}, {"opacity": 1, "scale": 0.86, "rotation": 0, "z": 90}, W52 + 0.38, 0.32, "power3.out")
    S.ft(f"#{s}-sel", {"scale": 0.86, "rotation": 0}, {"scale": 0.8, "rotation": 20}, W52 + 0.7, T1 - W52 - 0.7, "sine.inOut")
    SFX.extend([(W48 + 0.12, "whoosh", 0.06), (W52 + 0.05, "click", 0.14)])
