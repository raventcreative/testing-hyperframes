"""S02 — LAPTOP TO GOOGLE (W6 – W17). "Coba lihat, animasi kartun kayak gini sekarang bisa kita bangun lewat"
One physical push: the mascot slides past camera-left (over-the-shoulder) while the room zooms into the laptop screen;
the screen becomes the full recreated dark search page. "Claude" is typed (no history/autocomplete), results settle,
the user's pixel-hand cursor arcs in toward the Claude result (click lands in S03 on the spoken "Claude")."""
from kit_op import room, google_ui, cursor, LAP, MASCOT_ROOM

HIT = (175, 905)     # fingertip target on the "Claude" result title


def build(S):
    s, W = S.id, S.W
    S.back.append(f'<div class="abs" id="{s}-rw" style="left:0;top:0;width:1080px;height:1920px">' + "".join(room(s)) + "</div>")
    S.back.append(google_ui(s, f"{s}-q"))
    S.front.append(cursor(f"{s}-cur", HIT[0], HIT[1]))
    lx, ly, lw, lh = LAP
    k = 1080 / lw
    cx, cy = lx + lw / 2, ly + lh / 2
    S.keys(f"#{s}-rw", [(S.t0, {"scale": 1.06, "x": -14, "y": -10, "transformOrigin": "0px 0px"}, None),
                        (S.t0 + 0.08, {"scale": 1.06, "x": -14, "y": -10}, None),
                        (S.t0 + 0.78, {"scale": k, "x": 540 - k * cx, "y": 960 - k * cy}, "power3.in")])
    S.fx(S.t0 + 0.1, "whoosh", 0.06)
    S.init(f"#{s}-g", {"opacity": 0})
    S.ft(f"#{s}-g", {"opacity": 0}, {"opacity": 1}, S.t0 + 0.7, 0.16, "power1.out")
    # the mascot glides past camera-left (shoulder pass), then leaves the shot
    S.mv([(S.t0, dict(MASCOT_ROOM), None), (S.t0 + 0.62, {"fx": -380, "fy": 3100, "h": 2700, "yaw": 0, "pitch": 5}, "power2.in"),
          (S.t0 + 0.66, {"fx": -380, "fy": 3100, "h": 2700, "yaw": 0, "pitch": 5, "vis": 0}, None)])
    # typing "Claude"
    word = "Claude"
    t0 = W(8) + 0.25
    for i in range(len(word) + 1):
        S.tset(f"#{s}-q", {"textContent": word[:i]}, t0 + 0.12 * i) if i else S.init(f"#{s}-q", {"textContent": ""})
        if i:
            S.fx(t0 + 0.12 * i, "key", 0.05)
    S.ft(f"#{s}-box", {"borderColor": "#5f6368"}, {"borderColor": "#8ab4f8"}, t0 - 0.2, 0.2, "power1.out")
    for k2, at in enumerate([S.t0 + 0.9 + 0.5 * j for j in range(8)]):
        S.tset(f"#{s}-caret", {"opacity": 0 if k2 % 2 else 1}, at)
    S.init(f"#{s}-res", {"opacity": 0, "y": 30})
    S.ft(f"#{s}-res", {"opacity": 0, "y": 30}, {"opacity": 1, "y": 0}, t0 + 0.95, 0.35, "power3.out")
    S.fx(t0 + 0.95, "pop", 0.04)
    # cursor: non-linear arc from lower-right onto the result title
    S.init(f"#{s}-cur", {"x": 760, "y": 820, "opacity": 0})
    S.ft(f"#{s}-cur", {"opacity": 0}, {"opacity": 1}, W(13) - 0.1, 0.15, "none")
    S.ft(f"#{s}-cur", {"x": 760}, {"x": 0}, W(13) - 0.1, S.t1 - W(13) - 0.05, "power2.inOut")
    S.ft(f"#{s}-cur", {"y": 820}, {"y": 0}, W(13) - 0.1, S.t1 - W(13) - 0.05, "power3.out")
