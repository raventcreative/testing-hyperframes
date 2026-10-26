"""S01 — THE IMPOSSIBLE OBJECT (0.00–3.24)  VO: "Gila, satu Reels bisa dibongkar jadi mesin."
Hero = the user's mechanical phone photo, dissected (tools/assets_phone.py, tools/kit_phone.py): floating diagonal,
screen ON playing a mini Reel. Anticipation shiver of the seam, then on "dibongkar" the latch pins slide out, the
seam light flares and the real 3D glass lifts off the face (screen switches off -> the watch movement shows through)
+ REF-H apex. On "mesin" the gears start turning. The camera then pushes into the movement (cut to S02)."""
from xk import WORDS, box, shadow, minireel, minireel_anim, r3
from kit_phone import (phone_rig, Placement, glass_point, gears_motion, apex_h, bokeh_far, rig_point, GW, GH, FW, FH)

SFX = [(WORDS[4]["start"], "click", 0.11), (WORDS[4]["start"] + 0.04, "sparkle", 0.06), (3.10, "whoosh", 0.07)]
PLACE = Placement(0.9, (530, 733), (585, 935))          # body centre -> hero centre


def screen_html(pre):
    """mini Reel UI on the phone screen (content area GW-18 x GH-18)."""
    w, h = GW - 18, GH - 18
    s = w / 300
    ui = (f'<div class="abs" style="{box(0, 0, w, h * 0.72)}">{minireel(pre + "-mr", w, h * 0.72)}</div>'
          # Reels side rail (like / comment / share dots) + caption bars + progress line
          + "".join(f'<div class="abs" style="{box(w - 46, h * 0.50 + k * 62, 30, 30)}border-radius:50%;background:{c};box-shadow:0 4px 8px -4px rgba(28,51,84,.4)"></div>'
                    for k, c in enumerate(("#294b77", "#cbdbf4", "#cbdbf4", "#9fd8c4")))
          + f'<div class="abs" style="{box(28, h * 0.76, w * 0.62, 14)}border-radius:7px;background:#294b77"></div>'
          + f'<div class="abs" style="{box(28, h * 0.76 + 26, w * 0.74, 11)}border-radius:6px;background:#acc6e7"></div>'
          + f'<div class="abs" style="{box(28, h * 0.76 + 46, w * 0.5, 11)}border-radius:6px;background:#cbdbf4"></div>'
          + f'<div class="abs" style="{box(28, h - 34, w - 56, 5)}border-radius:3px;background:#dbe6f6"></div>'
          + f'<div class="abs" id="{pre}-prog" style="{box(28, h - 34, w - 56, 5)}border-radius:3px;background:#3a6299;transform-origin:0 50%"></div>')
    return ui


def build(S):
    s = S.id
    W4, W6 = S.W(4), S.W(6)                     # "dibongkar" 1.88, "mesin." 2.56
    t1 = S.t1
    cxg, cyg = PLACE.pt(*rig_point(FW / 2, FH * 0.55))      # face centre (scene px) -> camera target
    S.persp_origin = (r3(cxg), r3(cyg))
    # ---------------- far plane: porcelain arch backdrop + REF-H bokeh discs
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(240, 300, 700, 1240)}border-radius:350px 350px 40px 40px;opacity:.5"></div>'
                 f'<div class="abs" style="{box(290, 360, 600, 1150)}border-radius:300px 300px 30px 30px;border:2px solid rgba(255,255,255,.85)"></div>'
                 + "".join(bokeh_far(101, 6)) +
                 f'<div class="abs" style="{box(120, 1470, 940, 6)}border-radius:3px;background:rgba(172,198,231,.5)"></div></div>')
    S.far.append(f'<div class="abs" id="{s}-halo" style="{box(cxg - 520, cyg - 560, 1040, 1040)}border-radius:50%;'
                 f'background:radial-gradient(circle,rgba(255,255,255,.95) 0%,rgba(255,255,255,0) 64%)"></div>')
    # ---------------- mid: contact shadow + phone rig
    bx, by = PLACE.pt(600, 1222)
    S.mid.append(f'<div class="abs" id="{s}-csh" style="{box(bx - 420, by - 30, 820, 96)}border-radius:50%;'
                 f'background:radial-gradient(ellipse,rgba(28,51,84,.34),rgba(28,51,84,.12) 45%,rgba(28,51,84,0) 72%)"></div>')
    S.mid.append(phone_rig(s, PLACE, screen_html(s)))
    ax, ay = PLACE.pt(*glass_point(dz=26))
    apex_h(S, S.mid, f"{s}-ap", ax, ay, W4, size=620, stars=12, seed=11, punch=f"#{s}-punch")
    # ---------------- near plane: out-of-focus glass ring + bokeh
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" id="{s}-nr1" style="{box(905, 520, 180, 180)}border-radius:50%;border:12px solid rgba(255,255,255,.72);'
                  f'box-shadow:0 0 0 2px rgba(172,198,231,.6),0 20px 30px -10px rgba(28,51,84,.25);filter:blur(5px)"></div>'
                  f'<div class="abs" style="{box(-40, 1380, 150, 150)}border-radius:50%;filter:blur(8px);opacity:.7;'
                  f'background:radial-gradient(circle at 35% 30%,#ffffff,#e8f0fb 45%,#acc6e7 100%)"></div></div>')

    # ---------------- motion
    S.cam([(0.0, {"z": 0, "x": 0, "y": 0, "rotationY": 0, "rotationX": 0, "rotationZ": 0}, None),
           (W4 - 0.05, {"z": 130, "rotationY": -2, "rotationX": 1}, "sine.inOut"),
           (W6 + 0.18, {"z": 175, "rotationY": 1.5}, "power2.out"),
           (t1, {"z": 640, "rotationY": 3, "rotationZ": -2, "y": -10}, "power3.in")])
    S.init(f"#{s}-halo", {"opacity": 0.7, "scale": 0.94})
    S.ft(f"#{s}-halo", {"opacity": 0.7, "scale": 0.94}, {"opacity": 1, "scale": 1.05}, 0.0, t1, "sine.inOut")
    # the phone floats (bob + slow roll); contact shadow breathes against it
    S.keys(f"#{s}-float", [(0.0, {"y": 46, "rotation": -2.4}, None), (0.55, {"y": -4, "rotation": 0.3}, "power3.out"), (1.5, {"y": -14, "rotation": -0.8}, "sine.inOut"), (t1, {"y": -4, "rotation": 0.4}, "sine.inOut")])
    S.keys(f"#{s}-csh", [(0.0, {"scaleX": 1, "opacity": 1}, None), (1.4, {"scaleX": 0.92, "opacity": 0.82}, "sine.inOut"), (t1, {"scaleX": 0.98, "opacity": 0.95}, "sine.inOut")])
    # screen ON: mini Reel plays, progress line runs
    minireel_anim(S, f"{s}-mr", 0.0, W4, period=0.92, amp=1.25)
    S.init(f"#{s}-prog", {"scaleX": 0.08})
    S.ft(f"#{s}-prog", {"scaleX": 0.08}, {"scaleX": 0.55}, 0.0, W4, "none")
    # anticipation: the seam flickers and the glass shivers
    S.init(f"#{s}-seam", {"opacity": 0})
    S.ft(f"#{s}-seam", {"opacity": 0}, {"opacity": 0.45}, W4 - 0.55, 0.08, "power1.out")
    S.ft(f"#{s}-seam", {"opacity": 0.45}, {"opacity": 0.12}, W4 - 0.47, 0.22, "power1.in")
    S.ft(f"#{s}-seam", {"opacity": 0.12}, {"opacity": 1}, W4 - 0.08, 0.08, "power2.in")
    S.ft(f"#{s}-seam", {"opacity": 1}, {"opacity": 0.35}, W4 + 0.05, 0.7, "power2.out")
    S.ft(f"#{s}-seam", {"opacity": 0.35}, {"opacity": 0.0}, W6 + 0.3, 0.3, "power1.in")
    glass = f"#{s}-glass"
    S.init(glass, {"x": 0, "y": 0, "z": 0, "rotationX": 0, "rotationY": 0, "transformOrigin": "50% 50%"})
    S.ft(glass, {"x": 0, "z": 0}, {"x": 1.6, "z": 1.5}, W4 - 0.4, 0.07, "sine.inOut")
    S.ft(glass, {"x": 1.6, "z": 1.5}, {"x": -1.4, "z": 0.5}, W4 - 0.33, 0.07, "sine.inOut")
    S.ft(glass, {"x": -1.4, "z": 0.5}, {"x": 0, "z": 0}, W4 - 0.26, 0.08, "sine.inOut")
    # unlock: pins slide out, glass lifts off (overshoot + settle), then keeps rising slowly
    for k in range(4):
        side = -1 if k < 2 else 1
        S.init(f"#{s}-pin{k}", {"x": 0})
        S.ft(f"#{s}-pin{k}", {"x": 0}, {"x": side * 16}, W4 - 0.03 + k * 0.02, 0.22, "back.out(2)")
    S.ft(glass, {"x": 0, "y": 0, "z": 0, "rotationX": 0, "rotationY": 0}, {"x": -3, "y": 2, "z": 30, "rotationX": 1.6, "rotationY": -1.2}, W4 - 0.02, 0.36, "back.out(2.2)")
    S.ft(glass, {"x": -3, "y": 2, "z": 30, "rotationX": 1.6, "rotationY": -1.2}, {"x": -5, "y": 3, "z": 46, "rotationX": 2.2, "rotationY": -2}, W6, t1 - W6, "power1.inOut")
    S.init(f"#{s}-gsh", {"opacity": 0, "x": 0, "y": 0})
    S.ft(f"#{s}-gsh", {"opacity": 0, "x": 0, "y": 0}, {"opacity": 0.42, "x": 9, "y": 13}, W4 - 0.02, 0.36, "power3.out")
    S.ft(f"#{s}-gsh", {"opacity": 0.42, "x": 9, "y": 13}, {"opacity": 0.36, "x": 14, "y": 20}, W6, t1 - W6, "power1.inOut")
    # screen switches off with a short flicker -> the movement shows through the glass
    S.init(f"#{s}-scr", {"opacity": 1})
    S.ft(f"#{s}-scr", {"opacity": 1}, {"opacity": 0.35}, W4 - 0.01, 0.05, "power2.in")
    S.ft(f"#{s}-scr", {"opacity": 0.35}, {"opacity": 0.7}, W4 + 0.05, 0.05, "power1.out")
    S.ft(f"#{s}-scr", {"opacity": 0.7}, {"opacity": 0}, W4 + 0.12, 0.32, "power2.in")
    # gears: "mesin" -> spin up (continuous into S02)
    gears_motion(S, s, 0.0, t1)
    # specular sweep across the lifted glass
    S.init(f"#{s}-spec", {"x": 0, "rotation": 16})
    S.ft(f"#{s}-spec", {"x": 0, "rotation": 16}, {"x": GW + 560, "rotation": 16}, W6 - 0.12, 0.6, "power2.inOut")
