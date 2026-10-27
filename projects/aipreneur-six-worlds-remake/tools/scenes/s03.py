"""S03 — 02/06 OVER THE SHOULDER (7.77–12.67)
VO: "Sekarang kita di belakang karakter. Layar di depannya berubah jadi huruf raksasa."
Opens on S02's monitor, head-on at MONITOR. The camera pulls back and arcs round the mascot's right shoulder: the
real 3D mascot is seen from BEHIND (camera yaw ~150-165 deg) large in the lower-right foreground, so his head and
shoulder genuinely occlude the bottom-right of the monitor. Parallax: the foreground (mascot framing) travels
faster than the monitor/desk layer. The monitor shows the editorial design we just saw as new artwork. "Layar":
his arm comes up toward the screen. "berubah": the screen dims and the monitor's left edge lights; "huruf raksasa":
that rectangular left edge expands into the first stroke of the giant word — a matte navy extruded C — while the
monitor and the mascot drop away. End state: the C alone at LETTER_C on the pale plate (S04 opens on it)."""
from xk import box, r3
from kit import MONITOR, LETTER_C, shadow
from kit_a import monitor, c_stroke


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W14, W17, W19, W22, W24, W25 = (S.W(i) for i in (14, 17, 19, 22, 24, 25))
    mx, my, mw, mh = MONITOR
    lx, ly, lw, lh = LETTER_C
    # ---------------------------------------------------------------- back: desk + monitor stand + monitor (moves slower)
    desk = (f'<div class="abs" id="{s}-desk" style="{box(-120, my + mh + 150, 1320, 1200)}background:linear-gradient(180deg,#ffffff 0%,#eef3fb 40%,#dfe7f4 100%);'
            f'box-shadow:inset 0 3px 0 rgba(255,255,255,.95), 0 -1px 0 rgba(41,75,119,.18)"></div>')
    stand = (f'<div class="abs anod" style="{box(mx + mw / 2 - 34, my + mh - 6, 68, 162)}border-radius:6px"></div>'
             f'<div class="abs anod" style="{box(mx + mw / 2 - 130, my + mh + 146, 260, 18)}border-radius:9px"></div>')
    S.back.append(f'<div class="abs" id="{s}-room" style="{box(0, 0, 1080, 1920)}">' + desk
                  + shadow(mx + mw / 2 - 200, my + mh + 140, 400, 60, 0.5)
                  + f'<div class="abs" id="{s}-stand" style="{box(0, 0, 1080, 1920)}">{stand}</div>'
                  + monitor(s)
                  + f'<div class="abs" id="{s}-dim" style="{box(mx + 22, my + 22, mw - 44, mh - 44)}border-radius:10px;background:#0b1430"></div>'
                  + f'<div class="abs glint" id="{s}-edge" style="{box(mx - 2, my + 10, 6, mh - 20)}border-radius:3px"></div>'
                  + "</div>")
    # ---------------------------------------------------------------- front: the C stroke (hand-off object)
    S.front.append(f'<div class="abs" id="{s}-c" style="{box(lx, ly, lw, lh)}">'
                   + c_stroke(f"{s}-cs", lw, lh)
                   + "</div>")
    S.front.append(shadow(lx + 10, ly + lh + 4, lw + 40, 60, 0.0, id_=f"{s}-csh"))

    # ---------------------------------------------------------------- motion: camera pull-back + arc (background layer = slower)
    S.keys(f"#{s}-room", [(t0, {"scale": 1, "x": 0, "y": 0, "transformOrigin": "540px 960px"}, None),
                          (t0 + 0.7, {"scale": 0.84, "x": -40, "y": -30}, "power3.out"),
                          (W22, {"scale": 0.8, "x": -10, "y": -36}, "sine.inOut"),
                          (W24 + 0.1, {"scale": 0.83, "x": -20, "y": -30}, "power2.inOut")])
    for sel in (f"#{s}-desk", f"#{s}-stand"):
        S.init(sel, {"opacity": 0})
        S.ft(sel, {"opacity": 0}, {"opacity": 1}, t0 + 0.05, 0.5, "power2.out")
    # screen dims, left bezel edge lights ("berubah")
    S.init(f"#{s}-dim", {"opacity": 0})
    S.ft(f"#{s}-dim", {"opacity": 0}, {"opacity": 0.85}, W22, 0.4, "power2.inOut")
    S.init(f"#{s}-edge", {"opacity": 0, "scaleY": 0.3})
    S.ft(f"#{s}-edge", {"opacity": 0, "scaleY": 0.3}, {"opacity": 1, "scaleY": 1}, W22 + 0.15, 0.35, "power3.out")
    # "huruf raksasa": the monitor's left edge (screen rect in room coords at scale .83) becomes the C
    # left edge on screen at that moment
    sc, ox, oy = 0.83, -20, -30
    ex = 540 + sc * (mx - 540) + ox
    ey0 = 960 + sc * (my - 960) + oy
    eh = sc * mh
    go = W24 - 0.04
    c_from = {"scaleX": r3(10 / lw), "scaleY": r3(eh / lh), "x": r3(ex - lx), "y": r3(ey0 - ly), "opacity": 1, "transformOrigin": "0% 0%"}
    S.init(f"#{s}-c", dict(c_from, opacity=0))
    S.tset(f"#{s}-c", {"opacity": 1}, go)
    S.ft(f"#{s}-c", dict(c_from), {"scaleX": 1, "scaleY": 1, "x": 0, "y": 0, "opacity": 1}, go, 0.62, "power3.inOut")
    S.ft(f"#{s}-room", {"opacity": 1}, {"opacity": 0}, go + 0.12, 0.34, "power2.in")
    S.ft(f"#{s}-csh", {"opacity": 0}, {"opacity": 0.55}, go + 0.4, 0.3, "power2.out")

    # ---------------------------------------------------------------- mascot: seen from behind, big in the lower-right foreground
    v0 = {"fx": 1010, "fy": 2520, "h": 1300, "yaw": 142, "pitch": 6}
    v1 = {"fx": 905, "fy": 1935, "h": 1260, "yaw": 156, "pitch": 6}
    v2 = {"fx": 880, "fy": 1925, "h": 1240, "yaw": 164, "pitch": 6}
    S.mv([(t0, v0, None), (t0 + 0.75, v1, "power3.out"), (W22, v2, "sine.inOut"),
          (go + 0.05, v2, "none"), (go + 0.5, dict(v2, fy=2700, fx=980), "power3.in")])
    S.mset("V", {"vis": 0}, go + 0.52)
    # acting: looks at the screen, lifts the left arm toward it on "Layar", points at the edge on "berubah"
    S.act("root", [(t0, {"ry": -0.1}, 0.3), (W19, {"ry": -0.16}, 0.4)])
    S.act("head", [(t0, [-0.12, -0.18, 0.0], 0.35), (W17, [-0.16, -0.24, 0.02], 0.35), (W19, [-0.1, -0.3, 0.0], 0.3),
                   (W22, [-0.12, -0.36, -0.03], 0.3)])
    S.act("armL", [(t0, "low", 0.2), (W19 - 0.15, "present", 0.32), (W22 - 0.1, "pointUp", 0.3), (W24 + 0.2, "low", 0.4)])
    S.act("armR", [(t0, "low", 0.2), (W14, "explain", 0.35), (W17 + 0.2, "low", 0.4)])
    S.act("torso", [(t0, {"chest": [0.02, -0.06, 0]}, 0.35), (W19, {"chest": [0.05, -0.1, 0]}, 0.35)])
    S.fx(t0 + 0.05, "whoosh", 0.05)
    S.fx(W22 + 0.15, "click", 0.05)
    S.fx(go + 0.05, "whoosh", 0.06)
    S.fx(go + 0.6, "pop", 0.05)
