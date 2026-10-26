"""S18 — FINAL CTA (52.26–54.60)  VO: "Komen EDITOR. Gue bagiin."
The comment bubble (folded back at frame zero, continuing S17's lid) unfolds upright onto an ivory pedestal; the
spoken keyword EDITOR lands letter by letter (dimensional navy type) on "EDITOR", navy selection corners lock around
the bubble, one soft ice-blue pulse + a few sparkles; on "Gue bagiin" the small repo folder with the user's 3D GitHub
mark pops up beside it and turns to face us. Everything settles by 53.85 s and the final 0.75 s is perfectly still."""
import math
from xk import box, shadow, pedestal, apex, Rng, r3
from kit_e import bubble, letter_extrude, folder, BX, BY, BW, BH

SFX = [(52.62, "pop", 0.11), (52.98, "sparkle", 0.08)]

END = 53.85   # every tween is finished by here -> still frame to the end


def build(S):
    s = S.id
    S.persp_origin = (590, 560)
    WK, WE, WG, WB = S.W(116), S.W(117), S.W(118), S.W(119)    # Komen 52.36 EDITOR 52.64 Gue 53.30 bagiin 53.44
    t0 = S.t0

    # ---------------- far plane: arch backdrop + halo (book-ends S01)
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(240, 260, 720, 1200)}border-radius:360px 360px 40px 40px;opacity:.55"></div>'
                 f'<div class="abs" style="{box(290, 310, 620, 1110)}border-radius:310px 310px 30px 30px;border:2px solid rgba(255,255,255,.8)"></div>'
                 f'<div class="abs" style="{box(140, 1400, 900, 6)}border-radius:3px;background:rgba(172,198,231,.5)"></div>'
                 f'<div class="abs" style="{box(140, 1424, 900, 3)}border-radius:2px;background:rgba(172,198,231,.35)"></div></div>')
    S.far.append(f'<div class="abs" id="{s}-halo" style="{box(130, 340, 1000, 1000)}border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.98) 0%,rgba(232,240,251,.5) 40%,rgba(255,255,255,0) 64%)"></div>')

    # ---------------- hero: pedestal + bubble with EDITOR
    S.mid.append(pedestal(f"{s}-ped", 630, 1004, 640, depth=120))
    S.mid.append(shadow(360, 1000, 540, 70, 0.9, id_=f"{s}-bsh"))
    letters = "EDITOR"
    row = "".join(f'<div class="p3" id="{s}-L{k}w" style="position:relative;display:inline-block;margin:0 1px">{letter_extrude(f"{s}-L{k}", ch, 138)}</div>' for k, ch in enumerate(letters))
    inner = (f'<div class="abs p3" style="{box(22, 22, BW - 44, BH - 44)}display:flex;align-items:center;justify-content:center;padding-top:6px;transform:translateZ(20px)">{row}</div>'
             f'<div class="abs" id="{s}-sw" style="{box(-160, 20, 110, BH - 40)}background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.45),rgba(255,255,255,0))"></div>')
    S.mid.append(bubble(s, inner))
    # selection corners around the bubble
    m = 26
    for nm, (x, y) in {"tl": (BX - m, BY - m), "tr": (BX + BW + m - 26, BY - m), "bl": (BX - m, BY + BH + m - 26), "br": (BX + BW + m - 26, BY + BH + m - 26)}.items():
        S.mid.append(f'<div class="corner {nm}" id="{s}-c{nm}" style="left:{x}px;top:{y}px;width:34px;height:34px;border-width:0;{"border-top-width:6px;" if nm[0] == "t" else "border-bottom-width:6px;"}{"border-left-width:6px;" if nm[1] == "l" else "border-right-width:6px;"}"></div>')
    # repo folder beside the bubble (GitHub mark as a background image -> no duplicate <img> with S17)
    S.mid.append(shadow(820, 1112, 200, 40, 0.8, id_=f"{s}-fsh"))
    S.mid.append(f'<div class="abs p3" id="{s}-fw" style="{box(752, 1004, 150, 124)}">{folder(s + "-fd", 0, 0, 150, 124, mark_id=s + "-gh", mark_mode="bg")}</div>')

    # ---------------- near plane: bokeh ring + seeded resting sparkles
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(990, 420, 170, 170)}border-radius:50%;border:12px solid rgba(255,255,255,.7);box-shadow:0 0 0 2px rgba(172,198,231,.5);filter:blur(5px)"></div>'
                  f'<div class="abs" style="{box(-30, 1460, 280, 24)}border-radius:12px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px);opacity:.9"></div></div>')
    R = Rng(1818)
    for k in range(5):
        x, y = R.u(BX + 40, BX + BW - 40), R.u(BY - 70, BY - 10) if k % 2 else R.u(BY + BH + 10, BY + BH + 50)
        sz = R.u(10, 18)
        S.near.append(f'<div class="spark" id="{s}-st{k}" style="left:{r3(x)}px;top:{r3(y)}px"></div>')
        S.init(f"#{s}-st{k}", {"opacity": 0, "scale": 0.2, "rotation": 0})
        S.ft(f"#{s}-st{k}", {"opacity": 0, "scale": 0.2, "rotation": 0}, {"opacity": 0.95, "scale": sz / 14, "rotation": 45}, WE + 0.25 + k * 0.08, 0.3, "power3.out")
        S.ft(f"#{s}-st{k}", {"opacity": 0.95, "scale": sz / 14, "rotation": 45}, {"opacity": 0.55, "scale": sz / 20, "rotation": 90}, WE + 0.55 + k * 0.08, END - (WE + 0.55 + k * 0.08), "power2.out")
    apex(S, S.near, f"{s}-ap", BX + BW / 2, BY + BH / 2, WE + 0.02, size=820, sparks=6, seed=18, op=0.55)

    # ---------------- motion
    # bubble unfolds (continues S17's rotationX 62 pose) and settles on the pedestal
    S.init(f"#{s}-bub", {"rotationX": 40, "y": 0, "scale": 1, "transformOrigin": "50% 100%"})
    S.ft(f"#{s}-bub", {"rotationX": 40}, {"rotationX": -4}, t0, 0.42, "power2.out")
    S.ft(f"#{s}-bub", {"rotationX": -4}, {"rotationX": 0}, t0 + 0.425, 0.3, "sine.inOut")
    S.init(f"#{s}-bsh", {"scaleX": 0.7, "opacity": 0.5})
    S.ft(f"#{s}-bsh", {"scaleX": 0.7, "opacity": 0.5}, {"scaleX": 1, "opacity": 0.9}, t0, 0.45, "power2.out")
    # EDITOR lands letter by letter (drop from the camera, flip upright, tiny settle)
    for k in range(len(letters)):
        at = WE - 0.08 + k * 0.055
        # hinge up from lying flat toward the camera (origin at the baseline) -> never cuts through the glass
        S.init(f"#{s}-L{k}", {"rotationX": -92, "y": 24, "scale": 1.15, "opacity": 0, "transformOrigin": "50% 86%"})
        S.ft(f"#{s}-L{k}", {"opacity": 0}, {"opacity": 1}, at, 0.06, "power1.out")
        S.ft(f"#{s}-L{k}", {"rotationX": -92, "y": 24, "scale": 1.15}, {"rotationX": 0, "y": 0, "scale": 1}, at, 0.36, "back.out(1.7)")
    # selection corners lock in once the word is complete
    for nm, (dx, dy) in {"tl": (-30, -30), "tr": (30, -30), "bl": (-30, 30), "br": (30, 30)}.items():
        S.init(f"#{s}-c{nm}", {"opacity": 0, "x": dx, "y": dy})
        S.ft(f"#{s}-c{nm}", {"opacity": 0, "x": dx, "y": dy}, {"opacity": 1, "x": 0, "y": 0}, WE + 0.3, 0.32, "back.out(2.2)")
    # glass sweep across the bubble
    S.init(f"#{s}-sw", {"x": 0, "z": 30})
    S.ft(f"#{s}-sw", {"x": 0, "z": 30}, {"x": BW + 220, "z": 30}, WE + 0.5, 0.75, "power2.inOut")
    # repo folder pops beside the bubble on "Gue bagiin", GitHub mark turns to face us
    S.init(f"#{s}-fw", {"y": 60, "scale": 0.4, "opacity": 0, "rotation": 8})
    S.ft(f"#{s}-fw", {"opacity": 0}, {"opacity": 1}, WG - 0.05, 0.1, "power1.out")
    S.ft(f"#{s}-fw", {"y": 60, "scale": 0.4, "rotation": 8}, {"y": 0, "scale": 1, "rotation": -3}, WG - 0.05, 0.42, "back.out(2)")
    S.ft(f"#{s}-fw", {"rotation": -3}, {"rotation": 0}, WG + 0.37, END - WG - 0.37, "sine.inOut")
    S.init(f"#{s}-fsh", {"opacity": 0, "scaleX": 0.4})
    S.ft(f"#{s}-fsh", {"opacity": 0, "scaleX": 0.4}, {"opacity": 0.8, "scaleX": 1}, WG, 0.4, "power2.out")
    S.init(f"#{s}-gh", {"rotationY": -150, "transformPerspective": 700})
    S.ft(f"#{s}-gh", {"rotationY": -150}, {"rotationY": 0, "transformPerspective": 700}, WB - 0.02, 0.5, "expo.out")
    S.init(f"#{s}-halo", {"opacity": 0.7, "scale": 0.95})
    S.ft(f"#{s}-halo", {"opacity": 0.7, "scale": 0.95}, {"opacity": 1, "scale": 1.02}, t0, END - t0, "sine.inOut")
    # camera: from S17's end camera, a slow settle; completely still after END
    S.cam([(t0, {"z": 150, "x": 0, "y": 0, "rotationY": 0, "rotationX": 0}, None),
           (WE + 0.1, {"z": 172, "rotationY": -1.5, "rotationX": 0.6}, "power2.out"),
           (END, {"z": 185, "rotationY": 0, "rotationX": 0}, "sine.inOut")])
