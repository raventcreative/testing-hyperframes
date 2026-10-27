"""S07 — 06 HEADLINE STORM (13.17–14.13)  VO: "Judul berhamburan."
Opens on S06's headline band (STRIP_B, above the head). "Judul": the word slides into the band. "berhamburan":
the storm - VO-word headline bands cross the frame at different depths and angles: two BEHIND the mascot (the head
occludes them), two IN FRONT (over the legs and above the head, never the face); a slight dutch on the camera
(mirrored on the mascot). The mascot ducks as the front band whips past. Hand-off: the camera pans right; the centre
band sweeps down behind the head while a satin-metal ring draws itself beside him = S08's portal ring (RING_B)."""
from xk import box, r3, CYAN
from kit import NO_FILTER
from kit_b import STRIP_B, RING_B, CHECK_END, STORM_VIEW, PORTAL_VIEW, band, ring_markup


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W35, W36 = S.W(35), S.W(36)          # Judul 13.24, berhamburan 13.54
    pan = t1 - 0.32
    sx, sy, sw, sh = STRIP_B
    # ---------------------------------------------------------------- back: centre band + two bands behind the mascot
    inner = (f'<span id="{s}-w1" style="position:relative;display:inline-block">JUDUL</span> '
             f'<span id="{s}-w2" style="position:relative;display:inline-block;color:{CYAN}">BERHAMBURAN</span>')
    S.back.append(band(f"{s}-c", sx, sy, sw, sh, inner, size=58))
    S.back.append(band(f"{s}-b1", -200, 730, 1480, 84, f'DUA PULUH <span style="color:{CYAN}">EFEK</span>', size=50))
    S.back.append(band(f"{s}-b2", -200, 1236, 1480, 84, f'SATU KLIP <span style="color:{CYAN}">POLOS</span>', size=50))
    # ---------------------------------------------------------------- front: two bands in front (legs / above the head) + the ring
    S.front.append(band(f"{s}-f1", -100, 1596, 1280, 92, f'<span style="color:{CYAN}">CLOSE-UP</span>', size=58))
    S.front.append(band(f"{s}-f2", 140, 252, 900, 66, 'CHAT', size=40))
    rcx, rcy, rd = RING_B
    S.front.append(f'<svg class="abs" style="{box(rcx - rd / 2 - 10, rcy - rd / 2 - 10, rd + 20, rd + 20)}overflow:visible" viewBox="0 0 {rd + 20} {rd + 20}">'
                   f'<circle id="{s}-rdraw" cx="{rd / 2 + 10}" cy="{rd / 2 + 10}" r="{rd / 2 - 14}" fill="none" stroke="{CYAN}" stroke-width="5" '
                   f'pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" transform="rotate(-90 {rd / 2 + 10} {rd / 2 + 10})" '
                   f'style="filter:drop-shadow(0 0 8px rgba(0,208,254,.8))"/></svg>')
    S.front.append(ring_markup(f"{s}-ring", rcx, rcy, rd))

    # ---------------------------------------------------------------- camera: slight dutch (mirrored on the mascot wrapper)
    S.cam([(t0, {"rotation": 0}, None), (W36, {"rotation": -2.5}, "power2.out"), (pan, {"rotation": -2}, "sine.inOut"), (t1, {"rotation": 0}, "power2.inOut")])
    S.mx([(t0, {"rotation": 0, "filter": NO_FILTER}, None), (W36, {"rotation": -2.5}, "power2.out"), (pan, {"rotation": -2}, "sine.inOut"), (t1, {"rotation": 0}, "power2.inOut")])

    # ---------------------------------------------------------------- centre band: words land, then it sweeps down behind the head
    S.init(f"#{s}-w1", {"opacity": 0, "y": 40})
    S.ft(f"#{s}-w1", {"opacity": 0, "y": 40}, {"opacity": 1, "y": 0}, W35 - 0.02, 0.24, "power3.out")
    S.init(f"#{s}-w2", {"opacity": 0, "x": 60})
    S.ft(f"#{s}-w2", {"opacity": 0, "x": 60}, {"opacity": 1, "x": 0}, W36 - 0.02, 0.22, "power3.out")
    scx, scy = sx + sw / 2, sy + sh / 2
    S.init(f"#{s}-c", {"x": 0, "y": 0, "scaleX": 1, "rotation": 0, "opacity": 1})
    S.ft(f"#{s}-c", {"rotation": 0}, {"rotation": 2}, W36, 0.2, "back.out(3)")
    S.ft(f"#{s}-c", {"x": 0, "y": 0, "scaleX": 1, "rotation": 2, "opacity": 1},
         {"x": rcx - scx, "y": rcy - scy, "scaleX": rd / sw, "rotation": 0, "opacity": 0}, pan, 0.28, "power3.in")
    # crossing bands (x travel + a jolt on "berhamburan")
    cross = [("b1", -9, 760, -620, W35 - 0.05, 0.56), ("b2", 7, -760, 520, W35 - 0.02, 0.5),
             ("f1", -5, -1500, 240, W36 - 0.06, 0.28), ("f2", 3, 1200, 60, W36 + 0.02, 0.2)]
    for (i, rot, xa, xb, at, dur) in cross:
        S.init(f"#{s}-{i}", {"x": xa, "rotation": rot, "opacity": 1})
        S.ft(f"#{s}-{i}", {"x": xa}, {"x": xb}, at, dur, "power3.out")
        S.ft(f"#{s}-{i}", {"rotation": rot}, {"rotation": rot * 1.5}, W36, 0.24, "back.out(2.5)")
        S.ft(f"#{s}-{i}", {"x": xb, "opacity": 1}, {"x": xb + (900 if xb > xa else -900), "opacity": 0}, pan - 0.04, 0.3, "power3.in")
    # ring draws itself where the band lands
    S.init(f"#{s}-rdraw", {"attr": {"stroke-dashoffset": 1}, "opacity": 1})
    S.ft(f"#{s}-rdraw", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, pan + 0.04, 0.2, "power2.inOut")
    S.ft(f"#{s}-rdraw", {"opacity": 1}, {"opacity": 0}, t1 - 0.08, 0.07, "none")
    S.init(f"#{s}-ring", {"opacity": 0, "scale": 0.78, "rotation": -40})
    S.ft(f"#{s}-ring", {"opacity": 0, "scale": 0.78, "rotation": -40}, {"opacity": 1, "scale": 1, "rotation": 0}, pan + 0.12, 0.2, "power3.out")

    # ---------------------------------------------------------------- mascot: centre, duck, then pan to the portal framing
    S.mv([(t0, dict(CHECK_END), None), (W36 - 0.05, dict(STORM_VIEW), "power2.inOut"),
          (pan, dict(STORM_VIEW, yaw=3), "sine.inOut"), (t1, dict(PORTAL_VIEW), "power3.inOut")])
    S.act("root", [(t0 + 0.02, {"y": 0, "ry": 0.06, "rz": 0}, 0.25), (W36 - 0.04, {"y": -0.035, "rz": 0.03}, 0.16), (pan - 0.06, {"y": 0, "rz": 0}, 0.28)])
    S.act("torso", [(t0 + 0.02, {}, 0.2), (W36 - 0.04, {"spine": [0.1, 0, 0.04], "chest": [0.12, 0, 0]}, 0.16), (pan - 0.06, {}, 0.3)])
    S.act("head", [(t0 + 0.02, [-0.08, 0.08, 0], 0.25), (W36 - 0.04, [0.14, -0.1, 0.08], 0.16), (pan - 0.04, [-0.02, 0.32, 0.02], 0.3)])
    S.act("armL", [(t0 + 0.02, "pointUp", 0.2), (W36 - 0.08, "together", 0.18), (pan, "point", 0.28)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W36 - 0.08, "together", 0.18), (pan, "low", 0.35)])
    S.fx(W35, "click", 0.04)
    S.fx(W36 - 0.06, "whoosh", 0.07)
    S.fx(pan + 0.1, "sparkle", 0.04)
