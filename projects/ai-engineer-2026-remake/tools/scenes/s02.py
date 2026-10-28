"""S02 — BLUEPRINT / 10 KOMPONEN. VO: "Bayangin lo lagi ngerakit satu mesin AI. Ada sepuluh komponen. Dan urutannya penting."
Opens on S01's floor line (LINE_S01). The line lifts and unrolls upward into a BLUEPRINT sheet whose drawing (workbench
outline + 10 numbered circles) inks itself in. EXPLAIN MODE on "Bayangin ... mesin AI" (blueprint soft behind, chips
NGERAKIT -> MESIN AI in the explain band). He steps back to the right; the blueprint lays down flat and extrudes into the
real porcelain WORKBENCH; on "sepuluh komponen" ten aluminium sockets pop in, on "urutannya" their numbers light in
order 01->10, on "penting" he points at socket 01 and it rings. Hand-off: the camera dives into socket 01 (-> S03)."""
from xk import box, r3
from kit import FLOOR_Y, MAT, grid_floor, blur_wrap, explain, LINE_S01, ICON, part
from kit_a import ghost, bench, SOCKETS, B_TOP, B_BOT, B_TL, B_TR, B_BL, B_BR, zoom_to, chip_row, chips_out

BP = (80, 760, 920, FLOOR_Y - 760)       # blueprint sheet x y w h (bottom edge = the S01 floor line)


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    W = S.W
    x0, y0, w, h = BP
    S.back.append(grid_floor(f"{s}-grid"))
    # ---------------------------------------------------------------- blueprint sheet (inks itself)
    def bx(x): return x - x0
    def by(y): return y - y0
    circ = "".join(f'<ellipse cx="{r3(bx(cx))}" cy="{r3(by(cy) - 60)}" rx="{r3(d / 2)}" ry="{r3(d / 2 * 0.62)}" class="{s}-ink" id="{s}-ink{n}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                   f'<text x="{r3(bx(cx))}" y="{r3(by(cy) - 60 + d * 0.62 / 2 + 30)}" class="{s}-num" text-anchor="middle">{n + 1:02d}</text>'
                   for n, (cx, cy, d, sq) in enumerate(SOCKETS))
    trap = f"M{bx(B_TL)},{by(B_TOP) - 60} L{bx(B_TR)},{by(B_TOP) - 60} L{bx(B_BR)},{by(B_BOT) - 60} L{bx(B_BL)},{by(B_BOT) - 60} Z"
    S.css.append(f".{s}-ink {{ fill:none; stroke:#294B77; stroke-width:3; }}"
                 f" .{s}-num {{ font:700 22px Poppins, sans-serif; fill:#294B77; }}")
    sheet = (f'<div class="abs" id="{s}-bp" style="{box(x0, y0, w, h)}border-radius:6px;'
             f'background:linear-gradient(180deg,#eef4fc 0%,#e3edf9 100%);box-shadow:0 0 0 2px rgba(41,75,119,.25),0 30px 50px -28px rgba(10,13,44,.5)">'
             f'<div class="abs" style="inset:0;background-image:linear-gradient(rgba(41,75,119,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(41,75,119,.10) 1px,transparent 1px);background-size:40px 40px"></div>'
             f'<div class="abs" style="inset:14px;border:2px solid rgba(41,75,119,.35);border-radius:4px"></div>'
             f'<svg class="abs" style="left:0;top:0;width:{w}px;height:{h}px;overflow:visible" viewBox="0 0 {w} {h}">'
             f'<path d="{trap}" class="{s}-ink" pathLength="1" id="{s}-ink10" stroke-dasharray="1" stroke-dashoffset="1"/>{circ}'
             f'<path d="M{w / 2 - 120},{h - 150} h240" class="{s}-ink" pathLength="1" id="{s}-ink11" stroke-dasharray="1" stroke-dashoffset="1"/></svg>'
             f'<div class="abs" style="left:{w - 60}px;top:{h - 112}px;width:300px;height:80px;border:2px solid rgba(41,75,119,.35);'
             f'font:700 22px/38px Poppins;color:#294B77;padding:2px 14px">BLUEPRINT<br><span style="font-weight:400">MESIN AI · 10 SLOT</span></div>'
             f'</div>')
    S.back.append(f'<div class="abs" id="{s}-bpw" style="left:0;top:0;width:1080px;height:1920px;perspective:1400px;perspective-origin:540px 1640px">{sheet}</div>')
    # the S01 floor line (bottom edge of the sheet before it unrolls)
    S.back.append(f'<div class="abs" id="{s}-line" style="{box(LINE_S01[0], LINE_S01[1] - 2.5, LINE_S01[2] - LINE_S01[0], 5)}border-radius:3px;background:#1c3561"></div>')
    # ---------------------------------------------------------------- the real workbench + its name plate
    S.back.append(ghost(f"{s}-ghost"))
    S.back.append(bench(f"{s}-bench"))
    S.back.append(part(f"{s}-plate", 390, B_BOT + 8, 300, 38, "enamel", 10,
                       inner='<div class="abs" style="inset:0;font:700 20px/38px Poppins;color:#fff;text-align:center;letter-spacing:.12em">10 KOMPONEN</div>'))
    blur_wrap(S)
    # explain-band visuals
    ids = [c[0] for c in chip_row(S, f"{s}-k", [("ngerakit", ICON["tool"], 22, False), ("MESIN AI", ICON["bolt"], 24, True)], 440, size=32, gap=70)]
    S.front.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:600px;overflow:visible" viewBox="0 0 1080 600">'
                   f'<path id="{s}-ar" d="M505 484 H565 M548 468 L566 484 L548 500" fill="none" stroke="#294B77" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>')

    # ---------------------------------------------------------------- motion
    S.cam([(t0, {"x": 0, "y": -40, "scale": 1.08, "rotation": -0.8}, None), (t0 + 0.7, {"x": 0, "y": 0, "scale": 1, "rotation": 0}, "power2.out"),
           (t1 - 0.42, {"x": 0, "y": 0, "scale": 1, "rotation": 0}, "none"), (t1, dict(zoom_to(SOCKETS[0][0], SOCKETS[0][1], 2.4), rotation=0), "power3.in")])
    # line lifts -> sheet unrolls upward from it
    S.init(f"#{s}-bp", {"scaleY": 0.006, "transformOrigin": "50% 100%", "rotationX": 0, "opacity": 1})
    S.ft(f"#{s}-bp", {"scaleY": 0.006}, {"scaleY": 1}, t0 + 0.12, 0.55, "power3.out")
    S.init(f"#{s}-line", {"opacity": 1})
    S.tset(f"#{s}-line", {"opacity": 0}, t0 + 0.14)
    for k in range(12):
        a = t0 + 0.4 + (0 if k == 10 else 0.25 + 0.05 * k if k < 10 else 0.9)
        S.init(f"#{s}-ink{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-ink{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, a, 0.6 if k == 10 else 0.4, "power2.inOut")
    # step back: the sheet lays down flat and the porcelain bench extrudes out of it
    back = W(26) - 0.3
    S.ft(f"#{s}-bp", {"rotationX": 0, "opacity": 1}, {"rotationX": 78, "opacity": 0}, back, 0.45, "power2.in")
    S.init(f"#{s}-bench", {"opacity": 0, "y": 60, "scaleY": 0.7, "transformOrigin": "540px 1500px"})
    S.ft(f"#{s}-bench", {"opacity": 0, "y": 60, "scaleY": 0.7}, {"opacity": 1, "y": 0, "scaleY": 1}, back + 0.2, 0.5, "back.out(1.6)")
    S.init(f"#{s}-ghost", {"opacity": 0, "y": 30})
    S.ft(f"#{s}-ghost", {"opacity": 0, "y": 30}, {"opacity": 1, "y": 0}, back + 0.45, 0.5, "power3.out")
    S.keys(f"#{s}-ghost", [(back + 0.95, {"y": 0}, None), (back + 2.0, {"y": -10}, "sine.inOut"), (t1 - 0.4, {"y": 0}, "sine.inOut")])
    S.init(f"#{s}-plate", {"opacity": 0, "y": 20})
    S.ft(f"#{s}-plate", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, W(27), 0.35, "power3.out")
    # sockets pop on "sepuluh komponen", numbers light in order on "urutannya"
    for n in range(10):
        a = W(27) + 0.06 * n
        S.init(f"#{s}-bench-so{n}", {"scale": 0, "transformOrigin": "50% 50%"})
        S.ft(f"#{s}-bench-so{n}", {"scale": 0}, {"scale": 1}, a, 0.3, "back.out(2.6)")
        S.init(f"#{s}-bench-sn{n}", {"opacity": 0.25, "scale": 1, "transformOrigin": "50% 50%"})
        b = W(30) + 0.05 * n
        S.ft(f"#{s}-bench-sn{n}", {"opacity": 0.25, "scale": 1}, {"opacity": 1, "scale": 1.35}, b, 0.14, "power2.out")
        S.ft(f"#{s}-bench-sn{n}", {"scale": 1.35}, {"scale": 1}, b + 0.14, 0.2, "power2.out")
        S.init(f"#{s}-bench-sr{n}", {"opacity": 0, "scale": 1})
    S.ft(f"#{s}-bench-sr0", {"opacity": 0, "scale": 1}, {"opacity": 1, "scale": 1.25}, W(31) - 0.05, 0.22, "power2.out")
    S.ft(f"#{s}-bench-sr0", {"opacity": 1, "scale": 1.25}, {"opacity": 0.85, "scale": 1}, W(31) + 0.18, 0.3, "power2.out")
    S.fx(W(27) + 0.05, "pop", 0.05)
    S.fx(W(30), "key", 0.04)
    S.fx(W(31), "click", 0.07)
    S.fx(t1 - 0.4, "whoosh", 0.05)
    # explain-band out + arrow
    S.init(f"#{s}-ar", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-ar", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, W(23), 0.35, "power2.out")
    chips_out(S, ids, back - 0.1)
    S.ft(f"#{s}-ar", {"attr": {"stroke-dashoffset": 0}}, {"attr": {"stroke-dashoffset": -1}}, back - 0.1, 0.25, "power2.in")

    # ---------------------------------------------------------------- mascot: from S01's catch pose -> explain -> right of the bench
    s01_end = {"fx": 290, "fy": 1800, "h": 1080, "yaw": 30, "pitch": 6}
    right = {"fx": 930, "fy": 1900, "h": 780, "yaw": -30, "pitch": 6}
    S.mv([(t0, s01_end, None), (t0 + 0.4, dict(s01_end, yaw=12), "sine.inOut")])
    explain(S, t0 + 0.42, back, 19, 25, seed=2, enter=dict(s01_end, yaw=12), leave=right)
    S.mv([(back + 0.5, right, None), (W(29), dict(right, yaw=-34), "sine.inOut"), (t1, dict(right, yaw=-40, fx=915), "sine.inOut")])
    S.act("armL", [(t0, "present", 0.3), (t0 + 0.3, "low", 0.35)])
    S.act("armR", [(t0, "open", 0.3), (t0 + 0.3, "low", 0.35)])
    S.act("armR", [(back + 0.2, "low", 0.4), (W(27) - 0.15, "palmUp", 0.3), (W(29), "low", 0.35), (W(31) - 0.2, "point", 0.25), (t1 - 0.1, "low", 0.4)])
    S.act("armL", [(back + 0.2, "low", 0.4), (W(27) - 0.1, "open", 0.3), (W(29) + 0.1, "low", 0.4)])
    S.act("head", [(back + 0.2, [0.06, -0.3, 0], 0.35), (W(28), [0.12, -0.22, 0.02], 0.35), (W(30), [0.1, -0.36, -0.03], 0.35), (W(31), [0.14, -0.42, 0], 0.25)])
    S.act("torso", [(back + 0.2, {"chest": [0.03, -0.1, 0]}, 0.4), (W(31) - 0.2, {"chest": [0.06, -0.16, 0]}, 0.3)])
