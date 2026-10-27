"""S15 — HONEST COST CAVEAT (41.60–45.20)
VO: "Tapi coding agent dan komputasi masih bisa berbiaya."
A premium porcelain balance scale. A navy code-agent chip lands on the left pan ("coding agent"), the beam tips;
a compute module lands on the right pan ("komputasi"), the beam swings and settles level ("berbiaya") while a
small amber marker at the pivot lights: a calm, honest caveat. Then the camera pushes into the pivot ring,
which lands at the hero centre for the match into S16 (magnifier ring)."""
import math
from xk import box, screw, screws_rect, shadow, pedestal, apex, gear_svg, rivets_line, r3
from kit_d import vent_lines

SFX = [(42.3, "key", 0.09), (43.2, "key", 0.1)]

PX, PY = 590, 680          # pivot
HALF = 320                 # half beam length


def build(S):
    s = S.id
    S.persp_origin = (590, 560)
    W = S.W
    wTapi, wCod, wKom, wBer = W(91), W(92), W(95), W(98)
    land1, land2 = wCod + 0.2, wKom + 0.2

    # ---------------------------------------------------------------- far
    far = [f'<div class="abs por-dim" style="{box(250, 400, 680, 1080)}border-radius:340px 340px 40px 40px;opacity:.5"></div>',
           f'<div class="abs" style="{box(290, 440, 600, 1000)}border-radius:300px 300px 30px 30px;border:2px solid rgba(255,255,255,.85)"></div>',
           f'<div class="abs" style="{box(-100, 1470, 1300, 7)}border-radius:4px;background:rgba(172,198,231,.55)"></div>',
           f'<div class="abs" style="{box(-100, 1494, 1300, 3)}background:rgba(172,198,231,.35)"></div>',
           f'<div class="abs" style="{box(160, 380, 860, 860)}border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95),rgba(255,255,255,0) 62%)"></div>']
    S.far.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(-520px) scale(1.26)">{"".join(far)}</div>')

    # ---------------------------------------------------------------- stand: plinth, column, fixed balance arc
    st = [pedestal(f"{s}-pd", PX, 1310, 480, depth=90)]
    st.append(shadow(PX - 120, 1318, 240, 50, 1.0))
    st.append(f'<div class="abs" style="{box(PX - 30, PY + 40, 60, 1330 - PY - 40)}border-radius:14px;'
              f'background:linear-gradient(90deg,#e6edf8 0%,#ffffff 30%,#e3ebf7 65%,#b9cbe4 100%);box-shadow:inset 0 0 0 1px rgba(172,198,231,.6)"></div>')
    for yy in (PY + 120, PY + 330, 1250):
        st.append(f'<div class="abs navy-side" style="{box(PX - 38, yy, 76, 16)}border-radius:8px"></div>')
    st.append(f'<div class="abs por" style="{box(PX - 70, 1270, 140, 50)}border-radius:16px 16px 8px 8px"></div>')
    # fixed indicator arc above the pivot (ticks + amber centre marker)
    arc = [f'<svg width="260" height="140" viewBox="0 0 260 140" style="position:absolute;left:0;top:0;overflow:visible">',
           '<path d="M24 128 A106 106 0 0 1 236 128" fill="none" stroke="#dbe6f6" stroke-width="16" stroke-linecap="round"/>']
    for k in range(13):
        a = math.radians(-60 + k * 10)
        r0, r1 = (82, 100) if k % 3 == 0 else (90, 100)
        arc.append(f'<line x1="{r3(130 + r0 * math.sin(a))}" y1="{r3(128 - r0 * math.cos(a))}" x2="{r3(130 + r1 * math.sin(a))}" y2="{r3(128 - r1 * math.cos(a))}" stroke="{"#294b77" if k % 3 == 0 else "#9fb6d6"}" stroke-width="{2.6 if k % 3 == 0 else 1.6}" stroke-linecap="round"/>')
    arc.append(f'<path id="{s}-amb" d="M112 24 A106 106 0 0 1 148 24" fill="none" stroke="#f2c46d" stroke-width="16" stroke-linecap="round"/>')
    arc.append("</svg>")
    st.append(f'<div class="abs" style="{box(PX - 130, PY - 128, 260, 140)}">{"".join(arc)}</div>')
    S.mid.extend(st)

    # ---------------------------------------------------------------- pans (cords + dish), with their loads
    def pan(id_, cx, load):
        h = 340
        cords = (f'<svg width="260" height="{h}" viewBox="0 0 260 {h}" style="position:absolute;left:0;top:0;overflow:visible">'
                 f'<path d="M130 8 L16 {h - 22} M130 8 L244 {h - 22} M130 8 L130 {h - 34}" fill="none" stroke="#9fb6d6" stroke-width="3.5" stroke-dasharray="8 4" stroke-linecap="round"/></svg>')
        dish = (f'<div class="abs navy-side" style="{box(6, h - 18, 248, 34)}border-radius:0 0 50% 50% / 0 0 100% 100%"></div>'
                f'<div class="abs" style="{box(0, h - 38, 260, 52)}border-radius:50%;background:radial-gradient(ellipse at 45% 40%,#ffffff,#f1f5fb 55%,#d6e2f2);box-shadow:inset 0 -4px 8px rgba(172,198,231,.8)"></div>'
                f'<div class="abs" style="{box(22, h - 30, 216, 36)}border-radius:50%;border:1.5px solid rgba(172,198,231,.7)"></div>')
        hook = f'<div class="abs" style="{box(116, -6, 28, 28)}border-radius:50%;border:5px solid #3a6299"></div>'
        return (f'<div class="abs" id="{id_}" style="{box(cx - 130, PY, 260, 380)}">{cords}{dish}{hook}'
                f'<div class="abs" id="{id_}-ld" style="{box(0, 0, 260, h)}">{load}</div></div>')

    pins = "".join(f'<div class="abs" style="{box(-12, 14 + k * 18, 14, 7)}border-radius:3px;background:linear-gradient(90deg,#c3d5ee,#ffffff)"></div>'
                   f'<div class="abs" style="{box(128, 14 + k * 18, 14, 7)}border-radius:3px;background:linear-gradient(90deg,#ffffff,#c3d5ee)"></div>' for k in range(5))
    chip = (f'<div class="abs" style="{box(65, 192, 130, 110)}">{pins}'
            f'<div class="abs" style="{box(0, 0, 130, 110)}border-radius:16px;background:linear-gradient(150deg,#3a6299,#1c3354 70%);box-shadow:0 10px 14px -6px rgba(28,51,84,.5),inset 1px 1px 0 rgba(255,255,255,.3)"></div>'
            f'<div class="abs" style="{box(14, 14, 102, 82)}border-radius:10px;border:1.5px solid rgba(203,219,244,.35)"></div>'
            f'<svg width="130" height="110" viewBox="0 0 130 110" style="position:absolute;left:0;top:0"><path d="M48 38 L32 55 L48 72 M82 38 L98 55 L82 72 M72 32 L58 78" fill="none" stroke="#e8f0fb" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            f'<div class="led" style="left:104px;top:10px;width:9px;height:9px"></div></div>')
    module = (f'<div class="abs" style="{box(50, 178, 160, 124)}">'
              f'<div class="abs por" style="{box(0, 0, 160, 124)}border-radius:18px"></div>'
              f'<div class="abs navy-side" style="{box(8, 112, 144, 10)}border-radius:0 0 14px 14px"></div>'
              f'<div class="abs" id="{s}-fan" style="left:14px;top:20px;width:76px;height:76px">{gear_svg(s + "-fs", 76, 10, hole=0.3, spokes=4)}</div>'
              + vent_lines(100, 24, 46, 6, gap=11) +
              f'<div class="led" style="left:104px;top:96px;width:10px;height:10px"></div><div class="led-off" style="left:124px;top:96px;width:10px;height:10px"></div>'
              f'{screw(10, 10, 20, 8)}{screw(150, 10, -30, 8)}</div>')
    S.mid.append(pan(f"{s}-pl", PX - HALF + 10, chip))
    S.mid.append(pan(f"{s}-pr", PX + HALF - 10, module))

    # ---------------------------------------------------------------- beam (rotates about the pivot) + pivot ring
    beam = (f'<div class="abs por" style="{box(0, 0, 2 * HALF + 40, 26)}border-radius:13px"></div>'
            f'<div class="abs navy-side" style="{box(18, 20, 2 * HALF + 4, 8)}border-radius:0 0 6px 6px"></div>'
            + rivets_line(40, 13, 2 * HALF, 13, 9) +
            f'<div class="abs" style="{box(HALF + 17, -112, 6, 112)}border-radius:3px;background:linear-gradient(180deg,#294b77,#1c3354)"></div>'
            f'<div class="abs" style="{box(HALF + 12, -124, 16, 16)}border-radius:50%;background:#1c3354"></div>')
    S.mid.append(f'<div class="abs" id="{s}-beam" style="{box(PX - HALF - 20, PY - 13, 2 * HALF + 40, 26)}">{beam}</div>')
    S.mid.append(f'<div class="abs" id="{s}-ring" style="{box(PX - 62, PY - 62, 124, 124)}">'
                 f'<div class="abs por" style="{box(0, 0, 124, 124)}border-radius:50%"></div>'
                 f'<div class="abs" style="{box(14, 14, 96, 96)}border-radius:50%;border:2px solid rgba(172,198,231,.9);background:linear-gradient(150deg,#f6f8fc,#dfe8f5)"></div>'
                 f'<div class="abs" style="{box(38, 38, 48, 48)}border-radius:50%;background:radial-gradient(circle at 38% 32%,#5d84b9,#1c3354);box-shadow:0 2px 4px rgba(28,51,84,.4)"></div>'
                 f'<div class="abs" style="{box(54, 54, 16, 16)}border-radius:50%;background:#e8f0fb"></div>'
                 + "".join(f'<div class="rivet" style="left:{r3(62 + 52 * math.cos(math.radians(a)) - 4)}px;top:{r3(62 + 52 * math.sin(math.radians(a)) - 4)}px"></div>' for a in range(0, 360, 45))
                 + '</div>')

    # ---------------------------------------------------------------- near
    S.near.append(f'<div class="abs p3" style="{box(0, 0, 1080, 1920)}transform:translateZ(260px) scale(.87)">'
                  f'<div class="abs" style="{box(960, 520, 26, 420)}border-radius:13px;background:linear-gradient(90deg,#ffffff,#cbdbf4);filter:blur(4px);opacity:.85"></div>'
                  f'<div class="abs" style="{box(60, 520, 140, 140)}border-radius:50%;border:12px solid rgba(255,255,255,.7);filter:blur(5px)"></div></div>')
    apex(S, S.far, f"{s}-ap", PX, PY - 80, wBer, size=380, ring=True, sparks=0, op=0.6)

    # ================================================================ motion
    # beam angle (deg, + = clockwise = right pan down)
    ang = [(S.t0, -2.0, None), (wTapi + 0.3, 0.8, "sine.inOut"), (wCod - 0.05, 0.0, "sine.inOut"),
           (land1 + 0.45, -9.5, "back.out(1.4)"), (wKom, -8.5, "sine.inOut"),
           (land2 + 0.3, 4.5, "power2.out"), (land2 + 0.62, -2.2, "sine.inOut"), (land2 + 0.92, 1.0, "sine.inOut"),
           (wBer - 0.02, 0.0, "sine.inOut"), (S.t1, 0.0, "none")]
    S.keys(f"#{s}-beam", [(t, ({"rotation": a, "transformOrigin": "50% 50%"} if e is None else {"rotation": a}), e) for t, a, e in ang])
    S.keys(f"#{s}-pl", [(t, {"y": r3(-HALF * math.sin(math.radians(a)))}, e) for t, a, e in ang])
    S.keys(f"#{s}-pr", [(t, {"y": r3(HALF * math.sin(math.radians(a)))}, e) for t, a, e in ang])
    # loads drop in on their words
    S.init(f"#{s}-pl-ld", {"y": -560, "opacity": 0, "rotation": -8})
    S.ft(f"#{s}-pl-ld", {"y": -560, "opacity": 0, "rotation": -8}, {"y": 0, "opacity": 1, "rotation": 0}, wCod - 0.18, 0.38, "power2.in")
    S.init(f"#{s}-pr-ld", {"y": -560, "opacity": 0, "rotation": 6})
    S.ft(f"#{s}-pr-ld", {"y": -560, "opacity": 0, "rotation": 6}, {"y": 0, "opacity": 1, "rotation": 0}, wKom - 0.18, 0.38, "power2.in")
    S.init(f"#{s}-fan", {"rotation": 0})
    S.ft(f"#{s}-fan", {"rotation": 0}, {"rotation": 540}, wKom, S.t1 - wKom, "power1.out")
    # amber caveat marker: soft on/off pulse, then settles lit
    S.init(f"#{s}-amb", {"opacity": 0})
    S.ft(f"#{s}-amb", {"opacity": 0}, {"opacity": 1}, wBer, 0.18, "power2.out")
    S.ft(f"#{s}-amb", {"opacity": 1}, {"opacity": 0.45}, wBer + 0.2, 0.22, "sine.inOut")
    S.ft(f"#{s}-amb", {"opacity": 0.45}, {"opacity": 1}, wBer + 0.42, 0.22, "sine.inOut")
    # camera: calm framing, slight drift; then push into the pivot ring (hand-off)
    S.cam([(S.t0, {"x": 0, "y": -20, "z": 120, "rotationY": -3, "rotationX": 0}, None),
           (wBer, {"y": -10, "z": 200, "rotationY": 2}, "sine.inOut"),
           (wBer + 0.3, {"z": 220}, "sine.out"),
           (S.t1, {"x": 0, "y": 48, "z": 1100, "rotationY": 0}, "power3.in")])
