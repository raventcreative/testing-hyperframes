"""Shared pieces for the SIX WORLDS scenes: framings, explain mode, hand-off contracts, small builders."""
from xk import box, r3, WORDS

NAVY = "linear-gradient(135deg,#0A0D2C 0%,#294B77 100%)"
MED = {"fx": 540, "fy": 1800, "h": 1470, "yaw": 0, "pitch": 5}       # medium (full figure tall in frame)
WIDE = {"fx": 540, "fy": 1720, "h": 1150, "yaw": 0, "pitch": 5}      # full body, feet on the floor line
FLOOR_Y = 1722
NO_FILTER = "drop-shadow(0px 0px 0px rgba(0,208,254,0))"

# ======================================================================= EXPLAIN MODE (user rule)
# When the mascot explains (not demonstrating a world): he dollies forward to a half-body (waist-up) shot, the scene
# behind him goes soft, and he talks with his hands and head.
HALF = {"fx": 540, "fy": 2446, "h": 2156, "yaw": 0, "pitch": 4}      # waist up: hair top ≈ 290, face ≈ 1160, mouth ≈ 1300
BLUR_ON = "blur(16px) brightness(1.04) saturate(0.85)"
BLUR_OFF = "blur(0px) brightness(1) saturate(1)"
GESTURES = [("explain", "low"), ("palmUp", "explain"), ("together", "together"), ("open", "palmUp"), ("explainHi", "open")]


def blur_wrap(S, start_blurred=False):
    """wrap everything already in S.back into one element (#<id>-bgblur) so the whole back layer can go soft."""
    S.back[:] = [f'<div class="abs" id="{S.id}-bgblur" style="left:0;top:0;width:1080px;height:1920px">'] + S.back + ["</div>"]
    S.init(f"#{S.id}-bgblur", {"filter": BLUR_ON if start_blurred else "none"})


def blur_in(S, t, dur=0.45):
    S.ft(f"#{S.id}-bgblur", {"filter": BLUR_OFF}, {"filter": BLUR_ON}, t, dur, "power2.inOut")


def blur_out(S, t, dur=0.45):
    S.ft(f"#{S.id}-bgblur", {"filter": BLUR_ON}, {"filter": BLUR_OFF}, t, dur, "power2.inOut")
    S.tset(f"#{S.id}-bgblur", {"filter": "none"}, t + dur + 0.01)


def talk(S, i0, i1, seed=0, both=True, rest=True):
    """explaining gestures on VO words i0..i1: alternating two-hand beats, nods / tilts, small chest turns."""
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
    for tr, keys in (("armL", arm_l), ("armR", arm_r), ("head", head), ("torso", torso)):
        if keys:
            S.act(tr, keys)


def tx(id_, x, y, w, text, size=72, weight=700, align="left", style="", lh=1.08):
    """navy-gradient text block (brand normal text)."""
    i = f' id="{id_}"' if id_ else ""
    return (f'<div{i} class="abs" style="left:{r3(x)}px;top:{r3(y)}px;width:{r3(w)}px;text-align:{align};{style}">'
            f'<span class="tx" style="font:{weight} {size}px/{lh} Poppins, sans-serif">{text}</span></div>')


def badge(id_, x, y, text, size=64, style=""):
    """white text inside the navy-gradient highlight box."""
    i = f' id="{id_}"' if id_ else ""
    return (f'<div{i} class="abs" style="left:{r3(x)}px;top:{r3(y)}px;{style}">'
            f'<span class="badge" style="font:700 {size}px/1.1 Poppins, sans-serif">{text}</span></div>')


def shadow(x, y, w, h, op=0.7, id_=None):
    i = f' id="{id_}"' if id_ else ""
    return f'<div{i} class="abs cshadow" style="{box(x, y, w, h)}opacity:{op}"></div>'


# ======================================================================= HAND-OFF CONTRACTS (screen px, 1080x1920)
SLOTS = [(560, 560 + k * 150, 440, 118) for k in range(6)]   # S01: six timeline slots on the right (x, y, w, h)
CHART = (450, 470, 560, 900)        # S01 end slot #1 grows into / S02 chart slab (x, y, w, h)
BAR3 = (727, 1022, 70, 348)         # S02 bar #03 (x, y, w, h) at full height — the camera flies through it
MONITOR = (150, 380, 780, 500)      # S02 end bar edge = S03 monitor screen rect (x, y, w, h)
LETTER_C = (90, 520, 300, 520)      # S03 end monitor edge = S04 first stroke of the giant C (x, y, w, h)
GAP = (380, 520, 140, 520)          # S04 end: gap between the parted letters = S05 glass aperture (x, y, w, h)
GLINT_Y = 760                       # S05 end: the edge glint runs along this y and becomes the S06 beam
IRIS = (720, 900, 260)              # S06 end palm iris = S07 dial (centre x, y, diameter)
SELF = "assets/elements/selfshots"  # stills of our own result: {SELF}/<name>.jpg (540x960) + <name>_full.jpg
