"""Shared pieces for AI ENGINEER 2026 — BUILD THE MACHINE (1080x1920, suit mascot).
Framings, EXPLAIN MODE (mascot comes to the front, half-body, scene behind goes soft, he talks with hands + head),
machine materials (porcelain / satin navy enamel / brushed aluminium / frosted glass), liquid-glass chips, cables."""
from xk import box, r3, WORDS

NAVY = "linear-gradient(135deg,#0A0D2C 0%,#294B77 100%)"
# ---------------------------------------------------------------- framings (fx/fy = feet px, h = figure px; model: eyes u .596,
# mouth u .548, hair top ~.95). Captions live at y 236-400, so the explain framing keeps the hair below ~y 440.
HALF = {"fx": 540, "fy": 2230, "h": 1660, "yaw": 0, "pitch": 4}      # EXPLAIN: waist-up, hair top ~570, eyes ~1220, mouth ~1300
EXPLAIN_BAND = (420, 548)   # free band between the caption card and his hair: explain-mode visuals live here (y0, y1)
HALF_IN = dict(HALF, fy=2080, h=1420)                                 # entry pose for the dolly-in to HALF (no caption overlap)
MED = {"fx": 540, "fy": 1960, "h": 1420, "yaw": 0, "pitch": 5}       # medium: knees-up, hair top ~540
WIDE = {"fx": 540, "fy": 1640, "h": 980, "yaw": 0, "pitch": 5}       # full body on the workbench floor (feet ~1640)
SIDE_L = {"fx": 230, "fy": 1700, "h": 880, "yaw": 0, "pitch": 6}    # demonstrating: small, lower-left, turned to the machine
SIDE_R = {"fx": 850, "fy": 1700, "h": 880, "yaw": 0, "pitch": 6}   # demonstrating: small, lower-right
FLOOR_Y = 1640
CORE = (540, 1080)          # the AI core always sits at screen centre x (continuity anchor)
NO_FILTER = "drop-shadow(0px 0px 0px rgba(0,208,254,0))"

# ======================================================================= EXPLAIN MODE (user rule)
BLUR_ON = "blur(18px) brightness(1.05) saturate(0.85)"
BLUR_OFF = "blur(0px) brightness(1) saturate(1)"
GESTURES = [("explain", "low"), ("palmUp", "explain"), ("together", "together"), ("open", "palmUp"), ("explainHi", "open"),
            ("explain", "palmUp")]


def blur_wrap(S, start_blurred=False):
    """wrap everything already in S.back into one element (#<id>-bgblur) so the whole back layer can go soft."""
    S.back[:] = [f'<div class="abs" id="{S.id}-bgblur" style="left:0;top:0;width:1080px;height:1920px">'] + S.back + ["</div>"]
    S.init(f"#{S.id}-bgblur", {"filter": BLUR_ON if start_blurred else "none"})


def blur_in(S, t, dur=0.45):
    S.ft(f"#{S.id}-bgblur", {"filter": BLUR_OFF}, {"filter": BLUR_ON}, t, dur, "power2.inOut")


def blur_out(S, t, dur=0.45):
    S.ft(f"#{S.id}-bgblur", {"filter": BLUR_ON}, {"filter": BLUR_OFF}, t, dur, "power2.inOut")
    S.tset(f"#{S.id}-bgblur", {"filter": "none"}, t + dur + 0.01)


def talk(S, i0, i1, seed=0, both=True, rest=True, every=2):
    """explaining gestures on VO words i0..i1: alternating two-hand beats, nods / tilts, small chest turns.
    Hands change pose every `every` words (2 = lively, 3 = calmer) so they are never frozen while he speaks."""
    arm_l, arm_r, head, torso = [], [], [], []
    k = seed
    for n, i in enumerate(range(i0, i1 + 1)):
        w = WORDS[i]
        if n % every == 0:
            gl, gr = GESTURES[k % len(GESTURES)]
            arm_l.append((w["start"] - 0.14, gl, 0.3))
            if both:
                arm_r.append((w["start"] - 0.1, gr, 0.32))
            k += 1
        sgn = 1 if (n + seed) % 2 == 0 else -1
        head.append((w["start"] - 0.06, [-0.07 + 0.04 * (n % 3 == 0), 0.12 * sgn, 0.05 * sgn], 0.28))
        if n % 3 == 0:
            torso.append((w["start"] - 0.08, {"chest": [0.04, 0.06 * sgn, 0.02 * sgn]}, 0.35))
    end = WORDS[i1]["end"] + 0.2
    if rest:
        arm_l.append((end, "low", 0.4)); head.append((end, [0, 0, 0], 0.4)); torso.append((end, {}, 0.4))
        if both:
            arm_r.append((end, "low", 0.4))
    for tr, keys in (("armL", arm_l), ("armR", arm_r), ("head", head), ("torso", torso)):
        if keys:
            S.act(tr, keys)


def explain(S, t_in, t_out, i0, i1, seed=0, enter=None, leave=None, yaw_sway=0):
    """full explain beat: dolly in to HALF at t_in (from `enter` view), talk on words i0..i1, then (if leave) step back
    to `leave` at t_out. Background must be blur_wrap'ed; blurs in with the dolly, sharpens as he steps back."""
    enter = enter or HALF_IN
    keys = [(t_in, dict(enter), None), (t_in + 0.5, dict(HALF, yaw=-yaw_sway / 2), "power3.inOut")]
    mid = (t_in + 0.5 + t_out) / 2
    if t_out - t_in > 2.2:
        keys.append((mid, dict(HALF, yaw=yaw_sway), "sine.inOut"))
    keys.append((t_out, dict(HALF, yaw=0), "sine.inOut"))
    if leave:
        keys.append((t_out + 0.5, dict(leave), "power3.inOut"))
    S.mv(keys)
    blur_in(S, t_in + 0.05, 0.45)
    if leave:
        blur_out(S, t_out, 0.45)
    talk(S, i0, i1, seed=seed, rest=bool(leave))


# ======================================================================= type
def tx(id_, x, y, w, text, size=72, weight=700, align="left", style="", lh=1.08):
    i = f' id="{id_}"' if id_ else ""
    return (f'<div{i} class="abs" style="left:{r3(x)}px;top:{r3(y)}px;width:{r3(w)}px;text-align:{align};{style}">'
            f'<span class="tx" style="font:{weight} {size}px/{lh} Poppins, sans-serif">{text}</span></div>')


def badge(id_, x, y, text, size=64, style=""):
    i = f' id="{id_}"' if id_ else ""
    return (f'<div{i} class="abs" style="left:{r3(x)}px;top:{r3(y)}px;{style}">'
            f'<span class="badge" style="font:700 {size}px/1.1 Poppins, sans-serif">{text}</span></div>')


def shadow(x, y, w, h, op=0.7, id_=None):
    i = f' id="{id_}"' if id_ else ""
    return f'<div{i} class="abs cshadow" style="{box(x, y, w, h)}opacity:{op}"></div>'


# ======================================================================= machine materials (CSS, deterministic)
MAT = {
    "porcelain": "background:linear-gradient(160deg,#ffffff 0%,#f1f4f9 55%,#dfe6f0 100%);"
                 "box-shadow:inset 0 2px 0 rgba(255,255,255,.95),inset 0 -6px 12px rgba(41,75,119,.12),0 1px 0 rgba(255,255,255,.8),0 26px 40px -22px rgba(10,13,44,.45);",
    "enamel": "background:linear-gradient(160deg,#2f558a 0%,#1c3561 45%,#0f1d3d 100%);"
              "box-shadow:inset 0 2px 0 rgba(255,255,255,.28),inset 0 -8px 14px rgba(0,0,0,.35),0 26px 40px -20px rgba(10,13,44,.55);",
    "alu": "background:linear-gradient(150deg,#f2f5f9 0%,#c9d1dc 35%,#9aa6b6 55%,#dde3ea 100%);"
           "box-shadow:inset 1px 1px 0 rgba(255,255,255,.95),inset -1px -1px 0 rgba(10,13,44,.35),0 18px 30px -18px rgba(10,13,44,.45);",
    "glass": "background:linear-gradient(150deg,rgba(255,255,255,.66) 0%,rgba(232,240,252,.42) 50%,rgba(205,220,243,.34) 100%);"
             "border:1.5px solid rgba(255,255,255,.95);border-bottom-color:rgba(41,75,119,.28);border-right-color:rgba(41,75,119,.22);"
             "box-shadow:inset 0 2px 0 rgba(255,255,255,.95),inset 0 -6px 14px rgba(41,75,119,.10),0 28px 50px -26px rgba(10,13,44,.45);",
    "rubber": "background:linear-gradient(180deg,#3a4250 0%,#1d222b 100%);box-shadow:inset 0 1px 0 rgba(255,255,255,.18);",
}


def part(id_, x, y, w, h, mat="porcelain", r=18, inner="", style=""):
    """a machine part: material face + a 1px gasket seam inset (reads as a manufactured piece, not a flat card)."""
    i = f' id="{id_}"' if id_ else ""
    seam = (f'<div class="abs" style="left:6px;top:6px;right:6px;bottom:6px;border-radius:{max(2, r - 6)}px;'
            f'border:1px solid {"rgba(255,255,255,.22)" if mat == "enamel" else "rgba(41,75,119,.14)"};pointer-events:none"></div>')
    return f'<div{i} class="abs" style="{box(x, y, w, h)}border-radius:{r}px;{MAT[mat]}{style}">{seam}{inner}</div>'


def socket(id_, cx, cy, d=92, n=None):
    """a brushed-aluminium socket ring with a dark bore (+ optional engraved number)."""
    num = (f'<div class="abs" style="left:0;top:{d + 8}px;width:{d}px;text-align:center;font:700 22px/1 Poppins;color:#294B77">{n:02d}</div>'
           if n is not None else "")
    return (f'<div class="abs" id="{id_}" style="{box(cx - d / 2, cy - d / 2, d, d)}">'
            f'<div class="abs" style="inset:0;border-radius:50%;{MAT["alu"]}"></div>'
            f'<div class="abs" style="left:{d * .2}px;top:{d * .2}px;width:{d * .6}px;height:{d * .6}px;border-radius:50%;'
            f'background:radial-gradient(circle at 40% 35%,#2a3446 0%,#0b1020 70%);box-shadow:inset 0 4px 8px rgba(0,0,0,.6)"></div>{num}</div>')


def chip(id_, x, y, text, icon="", w=None, size=34, dark=False, style=""):
    """liquid-glass label chip (frosted, white rim, soft highlight) or a dark enamel chip; icon = inline SVG markup."""
    ww = f"width:{r3(w)}px;" if w else ""
    bg = MAT["enamel"] if dark else MAT["glass"]
    col = "#fff" if dark else "#0A0D2C"
    ic = f'<span style="display:inline-block;width:{size}px;height:{size}px;margin-right:14px;vertical-align:middle">{icon}</span>' if icon else ""
    return (f'<div class="abs" id="{id_}" style="left:{r3(x)}px;top:{r3(y)}px;{ww}border-radius:22px;{bg}padding:16px 26px;'
            f'white-space:nowrap;{style}"><span style="font:700 {size}px/1.2 Poppins, sans-serif;color:{col};vertical-align:middle">{ic}{text}</span></div>')


def cable(id_, d, w=10, color="#1c3561", glow=False, dash=True):
    """an SVG cable path (full frame coords). dash=True -> pathLength=1 dasharray so it can be drawn on."""
    extra = ' pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"' if dash else ""
    g = (f'<path d="{d}" fill="none" stroke="rgba(120,170,240,.55)" stroke-width="{w + 10}" stroke-linecap="round" opacity=".5"/>' if glow else "")
    return (f'<svg class="abs" style="left:0;top:0;width:1080px;height:1920px;overflow:visible" viewBox="0 0 1080 1920">{g}'
            f'<path id="{id_}" d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round"{extra} '
            f'style="filter:drop-shadow(4px 8px 1px rgba(10,13,44,.18))"/></svg>')   # shadow follows the drawn length


def grid_floor(id_, y=FLOOR_Y, depth=900, op=0.05):
    """the blueprint drafting grid on the workbench floor (CSS 3D plane, 0.05 navy)."""
    return (f'<div class="abs" id="{id_}" style="left:-500px;top:{y - depth}px;width:2080px;height:{depth}px;'
            f'transform:perspective(900px) rotateX(62deg);transform-origin:50% 100%;'
            f'background-image:linear-gradient(rgba(10,13,44,{op}) 2px,transparent 2px),linear-gradient(90deg,rgba(10,13,44,{op}) 2px,transparent 2px);'
            f'background-size:80px 80px"></div>')


ICON = {  # small line icons (navy stroke, 24x24 viewBox)
    "fn": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M9 4c-3 0-3 3-3 5s-1 3-3 3c2 0 3 1 3 3s0 5 3 5M15 4c3 0 3 3 3 5s1 3 3 3c-2 0-3 1-3 3s0 5-3 5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "db": '<svg viewBox="0 0 24 24" width="100%" height="100%"><ellipse cx="12" cy="5" rx="8" ry="3" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>',
    "plug": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "bug": '<svg viewBox="0 0 24 24" width="100%" height="100%"><rect x="7" y="7" width="10" height="13" rx="5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M12 7V4M7 12H3M21 12h-4M7 17l-3 2M17 17l3 2M7 8 4 6M17 8l3-2" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "check": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M4 12.5 9.5 18 20 6" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "branch": '<svg viewBox="0 0 24 24" width="100%" height="100%"><circle cx="6" cy="5" r="2.5" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="6" cy="19" r="2.5" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="18" cy="9" r="2.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M6 7.5v9M18 11.5c0 4-6 3-12 5" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>',
    "server": '<svg viewBox="0 0 24 24" width="100%" height="100%"><rect x="3" y="4" width="18" height="7" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><rect x="3" y="13" width="18" height="7" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M7 7.5h.01M7 16.5h.01" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M6 2h8l5 5v15H6z M14 2v5h5 M9 12h7M9 16h7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>',
    "search": '<svg viewBox="0 0 24 24" width="100%" height="100%"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M15.5 15.5 21 21" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>',
    "gauge": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M4 17a8 8 0 1 1 16 0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M12 17l4-6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>',
    "coin": '<svg viewBox="0 0 24 24" width="100%" height="100%"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M12 7v10M9.5 9.5c0-1.4 5-1.4 5 .5s-5 1.5-5 3.6 5 1.6 5 .4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M13 2 4 14h7l-1 8 9-12h-7z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M4 5h16v11H9l-5 4z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>',
    "tool": '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M14.5 6.5a4 4 0 0 0 5 5L12 19a2.1 2.1 0 0 1-3-3l7.5-7.5a4 4 0 0 1-2-2z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>',
}


# ======================================================================= HAND-OFF CONTRACTS (screen px, 1080x1920)
LINE_S01 = (80, FLOOR_Y, 1000)      # S01 end: the fallen connector becomes one thin navy blueprint line on the floor (x0, y, x1)
ML_TREND = [(170, 1190), (330, 1110), (500, 1060), (660, 980), (820, 920), (930, 870)]   # S05 end: the fitted trend line
#   (navy 6px polyline through these points) -> S06 starts with it and its vertices become the first neuron layer
ANSWER_CARD = (330, 880, 420, 300)  # S09 end: the assembled answer sheet (porcelain card, x y w h) -> S10 docks it into the agent
MACHINE = (240, 640, 600, 760)      # S12 end: the finished machine casing (x y w h, centred on CORE x) -> S13 lever branches from it
STAGE_RAIL_Y = 1500                 # S13/S14: the cable/rail that links the build stages runs along this y
