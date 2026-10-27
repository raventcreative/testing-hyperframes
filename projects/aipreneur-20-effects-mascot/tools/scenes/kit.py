"""Shared pieces for the 20-effects scenes (positions, paper look, frames)."""
from xk import box, r3, CYAN

WIDE = {"fx": 540, "fy": 1720, "h": 1150, "yaw": 0, "pitch": 5}      # full body, feet on the floor line
MED = {"fx": 540, "fy": 1800, "h": 1470, "yaw": 0, "pitch": 5}       # medium hero (head + torso)
FLOOR_Y = 1722
PAPER_C = "#fbf8f1"
# flat paper cut-out of the live mascot: white cut margin (4 offsets) + one card layer + soft cast shadow
PAPER_FILTER = ("drop-shadow(6px 0px 0px #fbf8f1) drop-shadow(-6px 0px 0px #fbf8f1) drop-shadow(0px 6px 0px #fbf8f1) "
                "drop-shadow(0px -6px 0px #fbf8f1) drop-shadow(9px 11px 0px #cbbfa9) drop-shadow(18px 30px 18px rgba(3,8,28,0.55))")
NO_FILTER = "drop-shadow(0px 0px 0px rgba(0,208,254,0))"
COVER = (160, 300, 760, 990)    # magazine cover rect (x, y, w, h) = the S13 viewfinder rect


def paper_strip(id_, x, y, w, h, color=PAPER_C, edge=True, rot=0, extra=""):
    """a cut paper strip with visible thickness (bottom/right edge) and a soft cast shadow."""
    e = (f'<div class="abs" style="left:0;top:{r3(h)}px;width:{r3(w)}px;height:5px;background:#d4c9b4;border-radius:0 0 2px 2px"></div>' if edge else "")
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}transform:rotate({rot}deg)">'
            f'<div class="abs" style="left:10px;top:{r3(h * 0.5)}px;width:{r3(w - 6)}px;height:{r3(h * 0.5 + 18)}px;background:rgba(3,8,28,.45);filter:blur(10px)"></div>'
            f'<div class="abs" style="left:0;top:0;width:{r3(w)}px;height:{r3(h)}px;background:{color};{extra}"></div>{e}</div>')


def corner_frame(id_, x, y, w, h, arm=70, th=5, color="#fff", glow=True):
    """four L-shaped viewfinder corners (ids {id}-c0..3)."""
    g = "box-shadow:0 0 12px rgba(0,208,254,.55);" if glow else ""
    out = []
    for k, (cx, cy, sx, sy) in enumerate(((x, y, 1, 1), (x + w, y, -1, 1), (x, y + h, 1, -1), (x + w, y + h, -1, -1))):
        ox = cx if sx > 0 else cx - arm
        oy = cy if sy > 0 else cy - arm
        hb = f'<div class="abs" style="left:{0 if sx > 0 else 0}px;top:{0 if sy > 0 else arm - th}px;width:{arm}px;height:{th}px;background:{color};{g}"></div>'
        vb = f'<div class="abs" style="left:{0 if sx > 0 else arm - th}px;top:0;width:{th}px;height:{arm}px;background:{color};{g}"></div>'
        out.append(f'<div class="abs" id="{id_}-c{k}" style="{box(ox, oy, arm, arm)}">{hb}{vb}</div>')
    return "".join(out)


ARCHES = [  # (id, x, y, w, h, top colour, shade)
    ("a0", -120, 980, 700, 900, "#2b5a92", "#1a3b66"),
    ("a1", 560, 900, 680, 980, "#244f86", "#163460"),
    ("a2", -60, 1180, 560, 700, "#1d4174", "#102850"),
    ("a3", 600, 1240, 560, 640, "#1a3a6a", "#0d2146"),
]


def diorama(s):
    """S12/S13 paper set (back layer): cyan paper sun, navy cardstock arches. ids {s}-sun, {s}-a0..a3."""
    out = [f'<div class="abs" id="{s}-sun" style="{box(300, 420, 480, 480)}border-radius:50%;background:radial-gradient(circle at 38% 34%,#7ee8ff 0%,#22c8f5 45%,#0aa6d6 100%);'
           f'box-shadow:12px 18px 0 #0a7fa8, 26px 40px 30px rgba(3,8,28,.5)"></div>']
    for (i, x, y, w, h, c, d) in ARCHES:
        out.append(f'<div class="abs" id="{s}-{i}" style="{box(x, y, w, h)}border-radius:{r3(w / 2)}px {r3(w / 2)}px 0 0;background:linear-gradient(160deg,{c} 0%,{d} 100%);'
                   f'box-shadow:inset 3px 4px 0 rgba(255,255,255,.18), 14px 20px 0 rgba(6,14,36,.55), 20px 34px 30px rgba(3,8,28,.55)"></div>')
    return out


# ======================================================================= HAND-OFF CONTRACTS (screen px)
# The end state of scene A and the start state of scene B share these exact geometries (see MOTION_TRANSITION_MAP.md).
CU = {"fx": 540, "fy": 2206, "h": 2090, "yaw": 0, "pitch": 4}       # close-up: face fills (face y ≈ 960)
ECU = {"fx": 540, "fy": 3292, "h": 3920, "yaw": 0, "pitch": 3}      # extreme close-up: eyes (eye line y ≈ 960)
HEAD_C = (540, 760)                       # MED head centre (hair included)
FACE_C = (540, 922)                       # MED face centre
PANEL = (90, 300, 900, 1180, 36)          # S00 end / S01 plain clip panel (x, y, w, h, radius)
ORBIT = (540, 760, 1000, 0.28, -8)        # S01 end / S02 orbit ring: centre x, y, diameter, scaleY (tilt), rotation deg
AVATAR = (166, 436, 96)                   # S02 end / S03 chat avatar circle: centre x, y, diameter
CHAT = (70, 300, 940, 1060, 44)           # S03 chat window
PREVIEW = (250, 640, 560, 700, 28)        # S03 end / S04 start: preview bubble = picture frame opening
PREVIEW_VIEW = {"fx": 530, "fy": 1560, "h": 820, "yaw": 0, "pitch": 4}
VF = (150, 360, 780, 1040)                # S04 end / S05 start: viewfinder rect (corners)
CHECK0 = (700, 578, 64)                   # S05 end reticle / S06 first check disc: centre x, y, diameter
STRIP = (-40, 1000, 1160, 96)             # S06 end (last pill stretched) / S07 start: headline strip (x, y, w, h)
RING = (540, 1050, 560)                   # S07 end / S08 portal ring: centre x, y, diameter
CABLE0 = (1040, 420)                      # S09 end curve tip / S10 cable start
MONITOR = (110, 300, 860, 640, 24)        # S10 end key-light matte / S11 monitor
LENS = (540, 922, 520)                    # S15 end lens / S16 aperture: centre x, y, diameter
HUD = (90, 290, 900, 1220)                # S18 end shard corners / S19 HUD corner guides
PHONE = (295, 300, 490, 1010, 70)         # S19 end / S20 phone body (x, y, w, h, radius); screen inset 18
BOARD = (80, 290, 920, 1080, 40)          # S20 end phone back / S21 checklist board
SELF = "assets/elements/selfshots"        # self-shots of our own result: {SELF}/<name>.jpg (540x960) and <name>_full.jpg


def graph_world(s, op=1.0):
    """S08 portal interior == S09 opening state: matte grid floor + horizon glow (ids {s}-gw*). Back-layer markup."""
    return (f'<div class="abs" id="{s}-gw" style="left:0;top:0;width:1080px;height:1920px;opacity:{op}">'
            f'<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 70%,#1f4a85 0%,#0c1d42 60%,#081430 100%)"></div>'
            f'<div class="abs" id="{s}-gwfloor" style="left:-540px;top:1180px;width:2160px;height:1400px;transform-origin:50% 0%;transform:perspective(900px) rotateX(62deg);'
            f'background-image:linear-gradient(rgba(0,208,254,.28) 2px,transparent 2px),linear-gradient(90deg,rgba(0,208,254,.28) 2px,transparent 2px);background-size:90px 90px;'
            f'-webkit-mask-image:linear-gradient(180deg,rgba(0,0,0,0),#000 30%);mask-image:linear-gradient(180deg,rgba(0,0,0,0),#000 30%)"></div>'
            f'<div class="abs" style="left:0;top:1120px;width:1080px;height:120px;background:radial-gradient(ellipse at 50% 50%,rgba(0,208,254,.35),rgba(0,208,254,0) 70%)"></div>'
            f'<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:60px 60px;'
            f'-webkit-mask-image:linear-gradient(180deg,#000 0%,rgba(0,0,0,0) 62%);mask-image:linear-gradient(180deg,#000 0%,rgba(0,0,0,0) 62%)"></div></div>')


# ======================================================================= EXPLAIN MODE (user revision)
# When the mascot is explaining (not demonstrating an effect): he dollies forward to a half-body shot, the scene
# behind him goes soft (blur + dim), and he talks with his hands and head.
HALF = {"fx": 540, "fy": 1925, "h": 1700, "yaw": 0, "pitch": 4}      # head + torso (chibi half-body): face ≈ y 910, shirt print ≈ y 1290 (clear above the captions)
BLUR_ON = "blur(16px) brightness(0.62) saturate(0.9)"
BLUR_OFF = "blur(0px) brightness(1) saturate(1)"
GESTURES = [("explain", "low"), ("palmUp", "explain"), ("together", "together"), ("open", "palmUp"), ("explainHi", "open")]


def blur_wrap(S):
    """wrap everything already in S.back into one element (#<id>-bgblur) so the whole back layer can go soft."""
    S.back[:] = [f'<div class="abs" id="{S.id}-bgblur" style="left:0;top:0;width:1080px;height:1920px">'] + S.back + ["</div>"]
    S.init(f"#{S.id}-bgblur", {"filter": "none"})


def blur_bg(S, t_in, t_out=None, dur=0.45):
    """soften the back layer between t_in and t_out (call blur_wrap(S) first)."""
    sel = f"#{S.id}-bgblur"
    S.ft(sel, {"filter": BLUR_OFF}, {"filter": BLUR_ON}, t_in, dur, "power2.inOut")
    if t_out is not None:
        S.ft(sel, {"filter": BLUR_ON}, {"filter": BLUR_OFF}, t_out, dur, "power2.inOut")
        S.tset(sel, {"filter": "none"}, t_out + dur + 0.01)


def talk(S, i0, i1, seed=0, both=True, rest=True):
    """explaining gestures on the VO words i0..i1 (inclusive): alternate two-hand beats on stressed / key words,
    nods and small head tilts on every other word, return to rest after the phrase."""
    from xk import WORDS
    arm_l, arm_r, head, torso = [], [], [], []
    k = seed
    for n, i in enumerate(range(i0, i1 + 1)):
        w = WORDS[i]
        if n % 2 == 0:
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
    return {"armL": arm_l, "armR": arm_r, "head": head, "torso": torso}
