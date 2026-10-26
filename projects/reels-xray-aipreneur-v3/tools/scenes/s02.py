"""S02 — THE X-RAY REVEAL (3.24–5.18)  VO: "Lihat. Layarnya kebuka."
Same phone as S01's end (bezel already split), seen closer. On "Lihat." the latch slides and the hinge pins light;
on "Layarnya" the glass screen swings open on a precision hinge (left edge) like a glass door; on "kebuka." it lands
at full swing and the stacked layers inside (typography / cards / transition / camera) fan out in depth while the
phone turns 3/4 so the stack reads. Last beat: camera dollies into the front type plate (match cut into S03)."""
from xk import box, screw, shadow, minireel_anim, apex, rivets_line, r3
from scenes.s01 import phone_parts, PW, PH

PX, PY = 380, 560            # phone placed lower than in S01 (closer framing keeps the caption band clear)
SW, SH = PW - 48, PH - 88    # screen / layer plate size
SX, SY = 24, 44              # screen offset inside the phone

# s01 end state of the bezel pieces (moves x 1.25)
BEZ = {"top": {"y": -80, "z": 22}, "bot": {"y": 67.5, "z": 22}, "lft": {"x": -60, "z": 22}, "rgt": {"x": 60, "z": 22}}

SFX = [(3.62, "click", 0.10), (4.38, "whoosh", 0.08)]


def layer_plate(pid, kind):
    """one exposed layer of the Reel: a glass plate with its content (abstract, no invented words)."""
    inner = []
    if kind == "type":      # typography layer: caption bars as raised navy type slugs
        for k, (x, y, w, h, c) in enumerate(((40, 70, 230, 26, "#294b77"), (40, 112, 300, 18, "#acc6e7"), (40, 600, 290, 22, "#294b77"),
                                             (40, 636, 190, 18, "#acc6e7"), (40, 668, 250, 18, "#cbdbf4"))):
            inner.append(f'<div class="abs" style="{box(x, y, w, h)}border-radius:{h / 2}px;background:{c};box-shadow:0 3px 0 rgba(28,51,84,.35)"></div>')
        inner.append(f'<div class="abs" style="{box(26, 56, 18, 18)}border-left:3px solid #294b77;border-top:3px solid #294b77"></div>')
        inner.append(f'<div class="abs" style="{box(SW - 44, SH - 70, 18, 18)}border-right:3px solid #294b77;border-bottom:3px solid #294b77"></div>')
    elif kind == "cards":   # cards & panels layer
        inner.append(f'<div class="mr-navy" style="{box(36, 190, 300, 250)}"></div>')
        inner.append(f'<div class="mr-card" style="{box(80, 360, 210, 150)}"></div>')
        inner.append(f'<div class="abs" style="{box(250, 220, 62, 62)}border-radius:50%;background:radial-gradient(circle at 35% 30%,#e9fbf4,#9fd8c4)"></div>')
        inner.append(f'<div class="abs" style="{box(220, 470, 90, 30)}border-radius:15px;background:#9fd8c4"></div>')
    elif kind == "trans":   # transition layer: swoosh paths + arrows
        inner.append(f'<svg class="abs" style="left:0;top:0" width="{SW}" height="{SH}" viewBox="0 0 {SW} {SH}">'
                     f'<path d="M30,560 C120,420 240,640 342,300" fill="none" stroke="#3a6299" stroke-width="10" stroke-linecap="round"/>'
                     f'<path d="M30,600 C140,470 250,690 342,350" fill="none" stroke="#acc6e7" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 14"/>'
                     f'<path d="M318,300 L342,300 L342,326" fill="none" stroke="#3a6299" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    else:                   # camera layer: viewfinder brackets + a rail line with ticks
        for c, (x, y) in (("tl", (34, 150)), ("tr", (SW - 60, 150)), ("bl", (34, SH - 260)), ("br", (SW - 60, SH - 260))):
            inner.append(f'<div class="corner {c}" style="left:{x}px;top:{y}px"></div>')
        inner.append(f'<div class="abs" style="{box(40, SH - 150, SW - 80, 6)}border-radius:3px;background:#294b77"></div>')
        for k in range(9):
            inner.append(f'<div class="abs" style="{box(48 + k * 36, SH - 162, 3, 12)}background:#3a6299"></div>')
        inner.append(f'<div class="abs" style="{box(150, SH - 186, 58, 34)}border-radius:8px;background:linear-gradient(160deg,#3a6299,#1c3354)"></div>')
        inner.append(f'<div class="abs" style="{box(196, SH - 178, 22, 18)}border-radius:50%;background:#cbdbf4;box-shadow:inset 0 0 0 4px #1c3354"></div>')
    edge = {"type": "rgba(41,75,119,.75)", "cards": "rgba(58,98,153,.6)", "trans": "rgba(58,98,153,.5)", "cam": "rgba(58,98,153,.45)"}[kind]
    return (f'<div class="abs glass" id="{pid}" style="{box(SX, SY, SW, SH)}border-radius:16px;border:2px solid {edge};'
            f'background:linear-gradient(135deg,rgba(255,255,255,.78),rgba(232,240,251,.55) 50%,rgba(203,219,244,.45))">{"".join(inner)}</div>')


def build(S):
    s = S.id
    S.persp_origin = (590, 640)
    S.css.append(f"#{s}-persp {{ perspective: 1400px; }}")
    W7, W8, W9 = S.W(7), S.W(8), S.W(9)        # "Lihat." 3.34, "Layarnya" 4.04, "kebuka." 4.38
    t0, t1 = S.t0, S.t1
    # ---------------- far plane (same arch backdrop as S01, continuity)
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">'
                 f'<div class="abs por-dim" style="{box(250, 300, 680, 1240)}border-radius:340px 340px 40px 40px;opacity:.55"></div>'
                 f'<div class="abs" style="{box(300, 360, 580, 1150)}border-radius:290px 290px 30px 30px;border:2px solid rgba(255,255,255,.8)"></div>'
                 f'<div class="abs" style="{box(140, 1500, 900, 6)}border-radius:3px;background:rgba(172,198,231,.5)"></div></div>')
    S.far.append(f'<div class="abs" id="{s}-halo" style="{box(110, 520, 960, 960)}border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95) 0%,rgba(255,255,255,0) 62%)"></div>')
    # ---------------- hero: phone without the gear mechanism; inside: navy cavity + 4 stacked layer plates
    cav = (f'<div class="abs" id="{s}-cav" style="{box(SX - 6, SY - 6, SW + 12, SH + 12)}border-radius:20px;'
           f'background:linear-gradient(160deg,#3a6299,#1c3354 72%);box-shadow:inset 0 0 0 3px rgba(203,219,244,.4),inset 0 20px 40px rgba(10,20,40,.35)">'
           + "".join(f'<div class="abs" style="{box(20, 40 + k * 64, SW - 28, 2)}background:rgba(203,219,244,.22)"></div>' for k in range(12))
           + f'{screw(22, 22, 20, 10)}{screw(SW - 10, 22, -30, 10)}{screw(22, SH - 10, 50, 10)}{screw(SW - 10, SH - 10, 5, 10)}</div>')
    plates = "".join(layer_plate(f"{s}-L{k}", kind) for k, kind in enumerate(("cam", "trans", "cards", "type")))
    # hinge barrel on the screen's left edge (5 knuckles + navy pins), part of the phone body
    hinge = []
    for k in range(5):
        y = SY + 40 + k * (SH - 80) / 4.0 - 28
        hinge.append(f'<div class="abs" style="{box(SX - 16, y, 22, 56)}border-radius:11px;'
                     f'background:linear-gradient(90deg,#c3d5ee,#ffffff 40%,#dbe6f6 70%,#9fb6d6);box-shadow:0 3px 5px rgba(28,51,84,.35)"></div>')
        hinge.append(f'<div class="pin" id="{s}-hp{k}" style="left:{r3(SX - 10)}px;top:{r3(y + 23)}px"></div>')
    hinge.append(f'<div class="abs" style="{box(SX - 6, SY + 10, 3, SH - 20)}background:linear-gradient(180deg,#1c3354,#3a6299,#1c3354)"></div>')
    # latch on the right edge (slides on "Lihat.")
    latch = (f'<div class="abs" id="{s}-latch" style="{box(SX + SW - 10, SY + SH / 2 - 40, 26, 80)}border-radius:8px;'
             f'background:linear-gradient(90deg,#3a6299,#1c3354);box-shadow:0 4px 8px rgba(28,51,84,.4)">'
             f'<div class="abs" style="{box(8, 12, 10, 56)}border-radius:5px;background:#cbdbf4"></div></div>')
    phone = phone_parts(s, mech=False)
    # insert the cavity + plates BEFORE the bezel/screen (they sit behind the glass)
    S.mid.append(shadow(PX - 40, PY + PH - 30, PW + 120, 90, 0.9, id_=f"{s}-csh"))
    S.mid.append(f'<div class="abs p3" id="{s}-phone" style="{box(PX, PY, PW, PH)}">{cav}{plates}{"".join(hinge)}{phone}{latch}</div>')
    # door shadow cast on the cavity as the glass swings (sits on the floor plane in screen space)
    S.mid.append(f'<div class="abs" id="{s}-dsh" style="{box(PX - 230, PY + PH - 10, 320, 60)}border-radius:50%;'
                 f'background:radial-gradient(ellipse,rgba(28,51,84,.28),rgba(28,51,84,0) 70%)"></div>')
    # ---------------- near plane: out-of-focus glass shard + rail fragment
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(930, 640, 150, 150)}border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"></div>'
                  f'<div class="abs" style="{box(820, 1580, 320, 22)}border-radius:11px;background:linear-gradient(180deg,#ffffff,#cbdbf4);filter:blur(4px)"></div></div>')
    apex(S, S.near, f"{s}-ap", 560, 980, W9 + 0.06, size=760, sparks=6, seed=11, op=0.7)

    # ---------------- motion
    # camera: continues S01's push (closer), dolly forward, then dive into the front type plate
    S.cam([(t0, {"z": 430, "x": -60, "y": 40, "rotationY": 5, "rotationX": 0}, None),
           (W8, {"z": 115, "x": 0, "y": 0, "rotationY": 0, "rotationX": 1}, "power3.out"),
           (W9 + 0.45, {"z": 140, "x": -40, "rotationY": -3, "rotationX": 2}, "power2.out"),
           (t1, {"z": 170, "x": 0, "y": 0, "rotationY": 0, "rotationX": 0}, "power2.in")])
    # phone turns to 3/4 so the layer stack reads in depth
    S.keys(f"#{s}-phone", [(t0, {"rotationY": -8, "rotationX": 2, "transformOrigin": "50% 50%"}, None),
                           (W8, {"rotationY": -5, "rotationX": 2}, "sine.inOut"),
                           (W9 + 0.3, {"rotationY": -38, "rotationX": 6}, "power3.inOut"),
                           (t1 - 0.42, {"rotationY": -36, "rotationX": 5}, "sine.inOut"),
                           (t1, {"rotationY": -4, "rotationX": 0}, "power3.in")])
    # bezel holds S01's split state (slow drift)
    for nm, st in BEZ.items():
        en = {k: (v * 1.05 if k != "z" else v) for k, v in st.items()}
        S.init(f"#{s}-{nm}", st)
        S.ft(f"#{s}-{nm}", st, en, t0, t1 - t0, "sine.inOut")
    for k in range(1, 5):   # seam lights glowing on from S01
        S.init(f"#{s}-sl{k}", {"opacity": 0.5})
        S.ft(f"#{s}-sl{k}", {"opacity": 0.5}, {"opacity": 0.15}, t0, 1.0, "power1.out")
    minireel_anim(S, f"{s}-mr", t0, W9, period=0.9, amp=1.0)
    S.init(f"#{s}-refl", {"x": 0, "rotation": 18})
    S.ft(f"#{s}-refl", {"x": 0, "rotation": 18}, {"x": 640, "rotation": 18}, t0 + 0.05, 0.75, "power2.inOut")
    # latch slides out on "Lihat." (anticipation for the door), hinge pins light up in a ripple
    S.init(f"#{s}-latch", {"x": 0})
    S.ft(f"#{s}-latch", {"x": 0}, {"x": -6}, W7 + 0.1, 0.12, "power2.in")
    S.ft(f"#{s}-latch", {"x": -6}, {"x": 46}, W7 + 0.24, 0.3, "back.out(2.4)")
    for k in range(5):
        S.init(f"#{s}-hp{k}", {"scale": 1})
        S.ft(f"#{s}-hp{k}", {"scale": 1}, {"scale": 1.7}, W7 + 0.35 + k * 0.06, 0.12, "power2.out")
        S.ft(f"#{s}-hp{k}", {"scale": 1.7}, {"scale": 1}, W7 + 0.47 + k * 0.06, 0.25, "power2.inOut")
    # the glass door: unlatch nudge, swing open on the hinge (overshoot + settle on "kebuka.")
    S.init(f"#{s}-scr", {"z": 26, "rotationY": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-scr", {"z": 26, "rotationY": 0}, {"z": 30, "rotationY": 6}, W8 - 0.18, 0.16, "power2.out")
    S.ft(f"#{s}-scr", {"z": 30, "rotationY": 6}, {"z": 34, "rotationY": -118}, W8 - 0.02, W9 - W8 + 0.14, "power3.inOut")
    S.ft(f"#{s}-scr", {"z": 34, "rotationY": -118}, {"z": 34, "rotationY": -104}, W9 + 0.12, 0.42, "back.out(2.6)")
    # door shadow sweeps across the floor as the glass moves
    S.init(f"#{s}-dsh", {"opacity": 0, "scaleX": 0.3, "x": 220})
    S.ft(f"#{s}-dsh", {"opacity": 0, "scaleX": 0.3, "x": 220}, {"opacity": 1, "scaleX": 1, "x": 0}, W8, W9 - W8 + 0.2, "power2.inOut")
    # layers: stacked tight behind the glass, fan out in depth on "kebuka.", float with different rates
    base_z = {0: -24, 1: -16, 2: -8, 3: 0}
    open_z = {0: -60, 1: 50, 2: 150, 3: 245}
    open_xy = {0: (-90, 24), 1: (0, 8), 2: (90, -8), 3: (175, -22)}
    for k in range(4):
        pid = f"#{s}-L{k}"
        bz = base_z[k]
        ox, oy = open_xy[k]
        S.init(pid, {"z": bz, "x": 0, "y": 0, "rotationY": 0})
        opened = {"z": open_z[k], "x": ox, "y": oy, "rotationY": 6 + k * 2}
        if k < 3:
            S.ft(pid, {"z": bz, "x": 0, "y": 0, "rotationY": 0}, opened, W9 - 0.02 + k * 0.05, 0.62, "expo.out")
            drift = {"z": open_z[k] + 18 * (k + 1), "x": ox + 6 * k, "y": oy - 8, "rotationY": 8 + k * 2}
            S.ft(pid, opened, drift, W9 + 0.6 + k * 0.05, t1 - (W9 + 0.6 + k * 0.05), "sine.inOut")
        else:        # hand-off: the type plate opens, then flies to the camera square-on (S03 opens on it)
            S.ft(pid, {"z": bz, "x": 0, "y": 0, "rotationY": 0}, opened, W9 + 0.13, t1 - 0.42 - (W9 + 0.13), "expo.out")
            S.ft(pid, opened, {"z": 420, "x": 0, "y": -60, "rotationY": 0}, t1 - 0.42, 0.42, "power3.in")
    for k in range(3):   # the back layers recede so the type plate owns the hand-off
        S.init(f"#{s}-L{k}", {"opacity": 1})
        S.ft(f"#{s}-L{k}", {"opacity": 1}, {"opacity": 0.35}, t1 - 0.4, 0.35, "power1.in")
    S.init(f"#{s}-halo", {"opacity": 0.8, "scale": 0.95})
    S.ft(f"#{s}-halo", {"opacity": 0.8, "scale": 0.95}, {"opacity": 1, "scale": 1.08}, t0, t1 - t0, "sine.inOut")
    S.init(f"#{s}-csh", {"scaleX": 1, "x": 0})
    S.ft(f"#{s}-csh", {"scaleX": 1, "x": 0}, {"scaleX": 1.15, "x": -30}, W8, 0.6, "power2.out")
