"""S15 — 14 LIQUID GLASS (26.47–28.30)  VO: "lalu melewati kaca yang melengkung."
Opens on S14's exact end frame (the cover is rebuilt from s14.py's own markup, same push 1.035). The gloss band
re-enters from the right as the bright front edge of a tall curved glass slab. The slab sweeps right -> left,
slowing over the face: inside it the world is refracted (backdrop blur/saturation band, bent highlight, cyan
chromatic fringe lines on both edges). Everything the glass has passed is no longer the cover: the cover is wiped
away and the mascot stands free at MED (the camera framing eases from the cover crop to MED under the glass).
"melengkung": the slab, now off the left edge, rolls back in and curls into a round glass lens over the face
(LENS) while the world outside the lens dims -> S16's iris aperture."""
import importlib
from xk import box, r3, CYAN, Scene, CLIP_NONE
from kit import MED, NO_FILTER, COVER, LENS

SW, SH, SY = 430, 1560, 180          # slab width / height / top
COVER_VIEW = {"fx": 540, "fy": 1660, "h": 1190, "yaw": 6, "pitch": 4}


def keep_left(e):
    return f"polygon(-400px -400px, {r3(e)}px -400px, {r3(e)}px 2320px, -400px 2320px)"


def mascot_clip(e):
    x, y, w, h = COVER
    return (f"polygon({x}px {y}px, {r3(e)}px {y}px, {r3(e)}px -400px, 1480px -400px, 1480px 2320px, {r3(e)}px 2320px, "
            f"{r3(e)}px {y + h}px, {x}px {y + h}px)")


def glass(id_, w, h, r, extra=""):
    """clear curved glass: refraction band (backdrop), bevel edges, bent specular, cyan/white fringes."""
    return (f'<div class="abs" id="{id_}" style="{box(0, 0, w, h)}{extra}">'
            f'<div class="abs" style="{box(0, 0, w, h)}border-radius:{r}px;-webkit-backdrop-filter:blur(7px) saturate(1.7) brightness(1.14) contrast(1.05);'
            f'backdrop-filter:blur(7px) saturate(1.7) brightness(1.14) contrast(1.05);'
            f'background:linear-gradient(90deg,rgba(255,255,255,.20) 0%,rgba(190,240,255,.05) 18%,rgba(255,255,255,0) 50%,rgba(0,208,254,.06) 82%,rgba(255,255,255,.22) 100%)"></div>'
            f'<div class="abs" style="{box(0, 0, w, h)}border-radius:{r}px;box-shadow:inset 10px 0 18px -6px rgba(255,255,255,.75),inset -12px 0 22px -8px rgba(0,208,254,.65),'
            f'inset 0 0 0 2px rgba(255,255,255,.55),0 40px 70px -30px rgba(3,8,28,.8)"></div>'
            f'<div class="abs" style="{box(w * 0.16, h * 0.06, w * 0.16, h * 0.62)}border-radius:{r3(w * 0.08)}px;background:linear-gradient(180deg,rgba(255,255,255,.75),rgba(255,255,255,0));'
            f'transform:skewY(-8deg);filter:blur(2px)"></div>'
            f'<div class="abs" style="{box(w * 0.62, h * 0.55, w * 0.1, h * 0.36)}border-radius:{r3(w * 0.05)}px;background:linear-gradient(0deg,rgba(255,255,255,.45),rgba(255,255,255,0));filter:blur(3px)"></div>'
            f'<div class="abs" style="{box(5, h * 0.12, 3, h * 0.76)}border-radius:2px;background:linear-gradient(180deg,rgba(0,208,254,0),#7fe9ff,rgba(0,208,254,0))"></div>'
            f'<div class="abs" style="{box(w - 9, h * 0.1, 3, h * 0.8)}border-radius:2px;background:linear-gradient(180deg,rgba(255,255,255,0),#ffffff,rgba(255,255,255,0))"></div>'
            f'</div>')


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W72, W73, W74, W75, W76 = (S.W(i) for i in range(72, 77))   # lalu 26.54 melewati 26.74 kaca 27.14 yang 27.44 melengkung 27.56
    # ---------------------------------------------------------------- the S14 cover, rebuilt from s14.py (ids re-prefixed)
    s14 = importlib.import_module("s14")
    C = Scene("s14")
    s14.build(C)
    back = "".join(C.back).replace('id="s14-', f'id="{s}-')
    front = "".join(C.front).replace('id="s14-', f'id="{s}-')
    S.back.append(f'<div class="abs" id="{s}-cov" style="{box(0, 0, 1080, 1920)}">{back}</div>')
    S.front.append(f'<div class="abs" id="{s}-covf" style="{box(0, 0, 1080, 1920)}">{front}</div>')
    # world behind the cover after the wipe: soft navy light pool (MED)
    S.back.insert(0, f'<div class="abs" id="{s}-pool" style="{box(0, 0, 1080, 1920)}background:radial-gradient(ellipse 60% 40% at 50% 48%,rgba(90,150,230,.35),rgba(90,150,230,0) 70%)"></div>')
    # ---------------------------------------------------------------- the slab (front) + lens + outside dim
    S.front.append(f'<div class="abs" id="{s}-slab" style="{box(-SW / 2, SY, SW, SH)}">' + glass(f"{s}-sg", SW, SH, 215) +
                   f'<div class="abs" style="{box(-6, 40, 14, SH - 80)}border-radius:7px;background:linear-gradient(180deg,rgba(255,255,255,0),rgba(255,255,255,.9),rgba(190,245,255,.8),rgba(255,255,255,0));filter:blur(3px)"></div></div>')
    lx, ly, ld = LENS
    S.front.append(f'<div class="abs" id="{s}-ldim" style="{box(lx - ld / 2, ly - ld / 2, ld, ld)}border-radius:50%;box-shadow:0 0 0 2400px rgba(4,9,26,.55)"></div>')
    S.front.append(f'<div class="abs" id="{s}-lens" style="{box(lx - ld / 2, ly - ld / 2, ld, ld)}">' + glass(f"{s}-lg", ld, ld, ld / 2) +
                   f'<div class="abs metal" style="{box(-10, -10, ld + 20, ld + 20)}border-radius:50%;background:none;box-shadow:inset 0 0 0 9px #c3ccd8,inset 0 0 0 11px rgba(40,52,75,.6),0 0 24px rgba(0,208,254,.35)"></div></div>')

    # ---------------------------------------------------------------- motion
    S.init(f"#{s}-dim", {"opacity": 0.35})
    S.init(f"#{s}-glossw", {"opacity": 0})
    S.init(f"#{s}-vf", {"opacity": 0})
    S.init(f"#{s}-pool", {"opacity": 0})
    S.ft(f"#{s}-pool", {"opacity": 0}, {"opacity": 1}, t0 + 0.2, 0.8, "power2.out")
    # slab path: centre x keys (slows over the face), then exits left
    keys = [(t0, 1520), (t0 + 0.48, 760), (W74 + 0.21, 430), (W74 + 0.46, -330)]
    eases = ["power2.out", "sine.inOut", "power2.in"]
    S.init(f"#{s}-slab", {"x": keys[0][1], "rotation": 7})
    for (ta, xa), (tb, xb), ea in zip(keys, keys[1:], eases):
        S.ft(f"#{s}-slab", {"x": xa}, {"x": xb}, ta, tb - ta, ea)
    # wipe edge E follows the slab centre (clamped at the cover's left edge 160)
    t_160 = keys[2][0] + (keys[3][0] - keys[2][0]) * ((430 - 160) / (430 + 330)) ** 0.5
    ekeys = [(t0, 1480), (t0 + 0.48, 760), (keys[2][0], 430), (t_160, 160)]
    for sel, fn in ((f"#{s}-cov", keep_left), (f"#{s}-covf", keep_left)):
        S.init(sel, {"clipPath": fn(1480)})
        for (ta, ea_), (tb, eb), ez in zip(ekeys, ekeys[1:], eases):
            S.ft(sel, {"clipPath": fn(ea_)}, {"clipPath": fn(eb)}, ta, tb - ta, ez)
        S.tset(sel, {"opacity": 0}, t_160 + 0.02)
    # lens: the slab rolls back in from the left and curls into a round lens over the face ("melengkung")
    l0 = W76 - 0.06
    S.init(f"#{s}-lens", {"x": -lx - 330, "scaleX": 0.8, "scaleY": 2.9, "opacity": 0, "rotation": 7})
    S.tset(f"#{s}-lens", {"opacity": 1}, l0)
    S.ft(f"#{s}-lens", {"x": -lx - 330, "scaleX": 0.8, "scaleY": 2.9, "rotation": 7}, {"x": 0, "scaleX": 1, "scaleY": 1, "rotation": 0}, l0, 0.5, "power3.out")
    S.init(f"#{s}-ldim", {"opacity": 0})
    S.ft(f"#{s}-ldim", {"opacity": 0}, {"opacity": 1}, l0 + 0.3, t1 - l0 - 0.3, "power2.in")
    # cover push (1.035) relaxes to 1 as the world is freed (mirrored on the mascot wrapper)
    S.cam([(t0, {"scale": 1.035}, None), (t0 + 0.3, {"scale": 1.035}, "none"), (t_160 + 0.1, {"scale": 1.0}, "sine.inOut")])

    # ---------------------------------------------------------------- mascot: cover crop -> MED under the glass, unclipped
    S.mv([(t0, COVER_VIEW, None), (t0 + 0.3, COVER_VIEW, "none"), (t_160, dict(MED, yaw=-6), "sine.inOut"), (t1, dict(MED, yaw=0), "sine.inOut")])
    S.mx([(t0, {"scale": 1.035, "transformOrigin": "540px 960px", "filter": NO_FILTER}, None), (t0 + 0.3, {"scale": 1.035}, "none"),
          (t_160 + 0.1, {"scale": 1.0}, "sine.inOut")])
    S.mc([(t0, {"clipPath": mascot_clip(1480)}, None), (t0 + 0.48, {"clipPath": mascot_clip(760)}, "power2.out"),
          (keys[2][0], {"clipPath": mascot_clip(430)}, "sine.inOut"), (t_160, {"clipPath": mascot_clip(160)}, "power2.in")])
    S.mset("#m-clip", {"clipPath": CLIP_NONE}, t_160 + 0.02)
    # acting: watches the glass pass right -> left, then looks into the lens
    S.act("head", [(t0 + 0.02, [0, 0.3, 0], 0.3), (W73, [0, 0.12, 0.02], 0.4), (W74 + 0.1, [-0.05, -0.2, 0.04], 0.4), (l0, [0.02, -0.28, 0], 0.3),
                   (l0 + 0.3, [0, 0, 0], 0.4)])
    S.act("armL", [(t0 + 0.02, "low", 0.3), (W73 - 0.1, "open", 0.32), (W75, "low", 0.4)])
    S.act("armR", [(t0 + 0.02, "low", 0.3), (W74 + 0.1, "point", 0.3), (l0 + 0.2, "low", 0.4)])
    S.act("torso", [(t0 + 0.02, {}, 0.3), (W74, {"chest": [0, -0.1, 0]}, 0.4), (l0 + 0.2, {}, 0.4)])
    S.fx(t0 + 0.05, "whoosh", 0.05)
    S.fx(keys[2][0] + 0.1, "whoosh", 0.04)
    S.fx(l0 + 0.4, "ping", 0.04)
