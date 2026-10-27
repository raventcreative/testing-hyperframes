"""S10 — CHART GROW (efek #10).
A weekly line chart lives on the wall BEHIND the mascot: 7 points with day labels above, the line draws left -> right in
0.55 s (navy, 5 px, round caps), each point pops as the line reaches it, then the end dot + a small label land."""
from xk import box, r3
from kit import MED

DAYS = ["SEN", "SEL", "RAB", "KAM", "JUM", "SAB", "MIN"]
XS = [100 + k * 140 for k in range(7)]
YS = [560, 516, 540, 452, 400, 330, 246]
TOP = 92      # day-label row
BASE = 700    # chart floor (behind the body)
VIEW = {"fx": 420, "fy": 1300, "h": 790, "yaw": 12, "pitch": 5}


def smooth_path(pts):
    d = f"M{pts[0][0]},{pts[0][1]}"
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        mx = (x0 + x1) / 2
        d += f" C{r3(mx)},{y0} {r3(mx)},{y1} {x1},{y1}"
    return d


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    td = t0 + 0.45          # line starts drawing
    dur = 0.55
    pts = list(zip(XS, YS))
    line = smooth_path(pts)
    area = line + f" L{XS[-1]},{BASE} L{XS[0]},{BASE} Z"
    # ---------------------------------------------------------------- back: chart board
    grid = "".join(f'<line x1="{x}" y1="{TOP + 50}" x2="{x}" y2="{BASE}" stroke="#294B77" stroke-opacity=".12" stroke-width="2" stroke-dasharray="4 10" stroke-linecap="round"/>' for x in XS)
    grid += "".join(f'<line x1="70" y1="{y}" x2="1010" y2="{y}" stroke="#294B77" stroke-opacity=".08" stroke-width="2"/>' for y in (190, 330, 470, 610))
    grid += f'<line x1="70" y1="{BASE}" x2="1010" y2="{BASE}" stroke="#294B77" stroke-opacity=".3" stroke-width="3" stroke-linecap="round"/>'
    S.back.append(f'<div class="abs card" style="{box(40, 50, 1000, 760)}border-radius:36px;opacity:.9"></div>')
    S.back.append(f'<svg class="abs" style="left:0;top:0;width:1080px;height:1080px;overflow:visible" viewBox="0 0 1080 1080">'
                  f'<defs><linearGradient id="{s}-lg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#294B77"/><stop offset="1" stop-color="#0A0D2C"/></linearGradient>'
                  f'<linearGradient id="{s}-ag" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#294B77" stop-opacity=".28"/><stop offset="1" stop-color="#294B77" stop-opacity="0"/></linearGradient></defs>'
                  f'{grid}'
                  f'<path id="{s}-area" d="{area}" fill="url(#{s}-ag)"/>'
                  f'<path id="{s}-line" d="{line}" fill="none" stroke="url(#{s}-lg)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>'
                  + "".join(f'<circle id="{s}-p{k}" cx="{x}" cy="{y}" r="9" fill="#ffffff" stroke="#0A0D2C" stroke-width="4"/>' for k, (x, y) in enumerate(pts[:-1]))
                  + f'<circle id="{s}-halo" cx="{XS[-1]}" cy="{YS[-1]}" r="34" fill="#294B77" fill-opacity=".18"/>'
                  + f'<circle id="{s}-end" cx="{XS[-1]}" cy="{YS[-1]}" r="16" fill="#0A0D2C" stroke="#ffffff" stroke-width="5"/>'
                  + '</svg>')
    for k, (x, d) in enumerate(zip(XS, DAYS)):
        S.back.append(f'<div class="abs" id="{s}-d{k}" style="{box(x - 50, TOP, 100, 40)}text-align:center;font:700 26px/40px Poppins, sans-serif;letter-spacing:.06em;color:#294B77">{d}</div>')
    # end label: small navy badge left of / below the end dot
    S.back.append(f'<div class="abs" id="{s}-lab" style="{box(XS[-1] - 258, YS[-1] - 104, 230, 96)}border-radius:18px;background:linear-gradient(135deg,#0A0D2C,#294B77);'
                  f'box-shadow:0 14px 26px -12px rgba(10,13,44,.6);color:#fff;text-align:center">'
                  f'<div style="font:700 40px/52px Poppins, sans-serif;padding-top:6px">+312%</div>'
                  f'<div style="font:400 19px/22px Poppins, sans-serif;opacity:.85">views minggu ini</div></div>')

    # ---------------------------------------------------------------- motion
    S.init(f"#{s}-line", {"attr": {"stroke-dashoffset": 1}})
    S.ft(f"#{s}-line", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, td, dur, "power1.inOut")
    S.init(f"#{s}-area", {"opacity": 0})
    S.ft(f"#{s}-area", {"opacity": 0}, {"opacity": 1}, td + dur - 0.1, 0.45, "power2.out")
    # each point pops when the line passes it (x-progress ~ arc progress for this gentle curve)
    span = XS[-1] - XS[0]
    for k in range(6):
        tk = td + dur * (XS[k] - XS[0]) / span
        o = {"svgOrigin": f"{XS[k]} {YS[k]}"}
        S.init(f"#{s}-p{k}", dict(o, scale=0, opacity=1))
        S.ft(f"#{s}-p{k}", {"scale": 0}, {"scale": 1}, tk - 0.02, 0.22, "back.out(3)")
    te = td + dur
    S.init(f"#{s}-end", {"svgOrigin": f"{XS[-1]} {YS[-1]}", "scale": 0})
    S.ft(f"#{s}-end", {"scale": 0}, {"scale": 1}, te - 0.03, 0.3, "back.out(3)")
    S.init(f"#{s}-halo", {"svgOrigin": f"{XS[-1]} {YS[-1]}", "scale": 0, "opacity": 0})
    for n in range(3):    # soft pulse rings (finite)
        tp = te + 0.1 + n * 1.1
        S.ft(f"#{s}-halo", {"scale": 0.6, "opacity": 0.9}, {"scale": 1.9, "opacity": 0}, tp, 0.9, "power2.out")
    S.init(f"#{s}-lab", {"opacity": 0, "y": 18, "scale": 0.85, "transformOrigin": "100% 100%"})
    S.ft(f"#{s}-lab", {"opacity": 0, "y": 18, "scale": 0.85}, {"opacity": 1, "y": 0, "scale": 1}, te + 0.12, 0.34, "back.out(2)")
    # day labels are on from frame 0 (finished thumbnail); a quiet left->right highlight runs with the line
    for k in range(7):
        tk = td + dur * (XS[k] - XS[0]) / span
        S.init(f"#{s}-d{k}", {"color": "#294B77", "y": 0})
        S.ft(f"#{s}-d{k}", {"color": "#294B77", "y": 0}, {"color": "#0A0D2C", "y": -6}, tk - 0.04, 0.16, "power2.out")
        S.ft(f"#{s}-d{k}", {"y": -6}, {"y": 0}, tk + 0.14, 0.25, "power2.inOut")

    # ---------------------------------------------------------------- mascot: in front of the chart, presents the growth
    S.mv([(t0, VIEW, None), (te + 0.2, dict(VIEW, yaw=20), "sine.inOut"), (t1, dict(VIEW, yaw=14), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.01), (td - 0.15, "pointUp", 0.35), (te + 1.4, "present", 0.4), (t1 - 0.8, "low", 0.45)])
    S.act("armR", [(t0, "low", 0.01), (te + 0.25, "fist", 0.3), (te + 1.3, "low", 0.45)])
    S.act("head", [(t0, [-0.02, 0.12, 0], 0.01), (td - 0.1, [-0.16, 0.34, 0.02], 0.45), (te + 0.3, [-0.1, 0.22, -0.05], 0.35),
                   (te + 1.5, [-0.03, 0.06, 0.03], 0.4), (t1 - 0.6, [0, 0.1, 0], 0.4)])
    S.act("torso", [(t0, {"chest": [0.02, 0.06, 0]}, 0.01), (td, {"chest": [0.03, 0.14, 0]}, 0.4), (te + 1.4, {"chest": [0.02, 0.06, 0]}, 0.4)])
    S.act("root", [(t0, {"y": 0, "ry": 0, "rz": 0}, 0.01), (te + 0.25, {"y": 0.012, "ry": 0, "rz": 0}, 0.2), (te + 0.6, {"y": 0, "ry": 0, "rz": 0}, 0.35)])
