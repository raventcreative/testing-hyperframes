"""THE INVISIBLE LAYER — shared stage pieces (1080x1920, ice-white forensic lab, brand navy #0A0D2C -> #294B77).
One hero object runs through the whole film: the GLASS FILE (outer glass shell + C2PA ID badge = metadata layer,
inner pixel artwork + woven signal lattice = in-content watermark). Materials: porcelain / satin navy enamel /
brushed aluminium / frosted glass / printed paper. Key light upper-left, contact shadows down-right."""
from xk import box, r3
from kit import MAT, NAVY, chip, part, HALF, HALF_IN, MED, WIDE, SIDE_L, SIDE_R, blur_wrap, blur_in, blur_out  # noqa: F401

INK = "linear-gradient(100deg,#0A0D2C 0%,#294B77 100%)"
GLOW_REST = "0 0 0 1px rgba(170,205,255,.22), 0 0 14px rgba(41,75,119,.22), 0 18px 30px -16px rgba(10,13,44,.45)"
GLOW_PEAK = "0 0 0 2px rgba(200,225,255,.6), 0 0 26px rgba(80,135,215,.30), 0 18px 30px -16px rgba(10,13,44,.45)"
ART = ("background:radial-gradient(120% 80% at 25% 20%,#ffffff 0%,rgba(255,255,255,0) 55%),"
       "radial-gradient(90% 60% at 80% 85%,#294B77 0%,rgba(41,75,119,0) 60%),"
       "linear-gradient(170deg,#dfe9f7 0%,#a9c1e2 42%,#5d7fae 70%,#21385f 100%);")
PIX = ("background-image:linear-gradient(rgba(255,255,255,.16) 1px,transparent 1px),"
       "linear-gradient(90deg,rgba(255,255,255,.16) 1px,transparent 1px);background-size:18px 18px;")
SIG = ("background-image:radial-gradient(circle,rgba(220,235,255,.95) 0 2.2px,transparent 3px),"
       "radial-gradient(circle,rgba(10,13,44,.55) 0 1.6px,transparent 2.4px);"
       "background-size:36px 36px,36px 36px;background-position:0 0,18px 18px;")


def ink(id_, x, y, w, text, size=44, weight=700, align="center", style=""):
    i = f' id="{id_}"' if id_ else ""
    return (f'<div{i} class="abs" style="left:{r3(x)}px;top:{r3(y)}px;width:{r3(w)}px;text-align:{align};{style}">'
            f'<span class="tx" style="font:{weight} {size}px/1.15 Poppins, sans-serif">{text}</span></div>')


def stamp(id_, cx, y, text, size=46, style=""):
    """brand highlight: white Poppins 700 inside the navy-gradient box, contained glow (bloom via glow_on)."""
    return (f'<div class="abs" style="left:{r3(cx - 470)}px;top:{r3(y)}px;width:940px;text-align:center;{style}">'
            f'<span id="{id_}" style="display:inline-block;font:700 {size}px/1.18 Poppins, sans-serif;color:#fff;'
            f'background:linear-gradient(108deg,#0A0D2C 0%,#294B77 100%);border-radius:18px;padding:12px 30px 15px;'
            f'box-shadow:{GLOW_REST};white-space:nowrap">{text}</span></div>')


def stamp_in(S, id_, at, glint=False):
    """stamp lands (0.32 s power3.out) and blooms once on the spoken keyword, then settles to a low glow."""
    S.init(f"#{id_}", {"scale": 1.18, "opacity": 0, "boxShadow": GLOW_REST})
    S.ft(f"#{id_}", {"scale": 1.18, "opacity": 0}, {"scale": 1, "opacity": 1}, at, 0.32, "power3.out")
    S.ft(f"#{id_}", {"boxShadow": GLOW_REST}, {"boxShadow": GLOW_PEAK}, at + 0.05, 0.3, "power3.out")
    S.ft(f"#{id_}", {"boxShadow": GLOW_PEAK}, {"boxShadow": GLOW_REST}, at + 0.4, 0.6, "sine.inOut")
    S.fx(at, "pop", 0.06)


def glass_file(id_, x, y, w=420, h=540, badge=True, sig_op=0.0, label=None):
    """the hero GLASS FILE. ids: {id}-art (content), {id}-sig (watermark lattice), {id}-shell (glass), {id}-badge."""
    fold = 70
    clip = f"clip-path:polygon(0 0,{w - fold}px 0,{w}px {fold}px,{w}px {h}px,0 {h}px);"
    b = ""
    if badge:
        b = (f'<div class="abs" id="{id_}-badge" style="left:{w - 205}px;top:{fold + 26}px;width:180px;height:112px;border-radius:14px;'
             f'{MAT["porcelain"]}">'
             f'<div class="abs" style="left:16px;top:14px;font:700 30px/1 Poppins;color:#0A0D2C;letter-spacing:.02em">C2PA</div>'
             f'<div class="abs" style="left:16px;top:56px;width:120px;height:9px;border-radius:5px;background:rgba(41,75,119,.30)"></div>'
             f'<div class="abs" style="left:16px;top:74px;width:88px;height:9px;border-radius:5px;background:rgba(41,75,119,.18)"></div>'
             f'<div class="abs" style="left:150px;top:-12px;width:16px;height:36px;border-radius:6px;{MAT["alu"]}"></div></div>')
    lab = f'<div class="abs" style="left:28px;top:{h - 62}px;font:700 24px/1 Poppins;color:rgba(255,255,255,.92);letter-spacing:.08em">{label}</div>' if label else ""
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}transform-style:preserve-3d">'
            f'<div class="abs" style="left:24px;top:{h - 6}px;width:{w - 10}px;height:40px;border-radius:50%;'
            f'background:radial-gradient(closest-side,rgba(10,13,44,.32),rgba(10,13,44,0));transform:translateZ(-60px)"></div>'
            f'<div class="abs" id="{id_}-art" style="left:22px;top:22px;width:{w - 44}px;height:{h - 44}px;border-radius:14px;{ART}'
            f'transform:translateZ(-26px);box-shadow:0 20px 40px -24px rgba(10,13,44,.6);overflow:hidden">'
            f'<div class="abs" style="inset:0;{PIX}"></div>'
            f'<div class="abs" id="{id_}-sig" style="inset:0;{SIG}opacity:{sig_op}"></div>{lab}</div>'
            f'<div class="abs" id="{id_}-shell" style="left:0;top:0;width:{w}px;height:{h}px;border-radius:22px;{MAT["glass"]}{clip}">'
            f'<div class="abs" style="left:{w - fold}px;top:0;width:{fold}px;height:{fold}px;'
            f'background:linear-gradient(225deg,rgba(255,255,255,0) 50%,rgba(220,232,248,.95) 50%,#c2d3ea 100%)"></div>'
            f'<div class="abs" id="{id_}-spec" style="left:-60%;top:-10%;width:40%;height:130%;transform:rotate(18deg);'
            f'background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.55),rgba(255,255,255,0))"></div></div>'
            f'{b}</div>')


def spec_sweep(S, id_, at, dur=0.7):
    S.ft(f"#{id_}-spec", {"xPercent": 0}, {"xPercent": 450}, at, dur, "power2.inOut")


def station(id_, x, y, w, h, title, sub="", icons=""):
    """an inspection station: satin enamel housing + porcelain input slot + engraved plaque (official tool NAME only)."""
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}">'
            + part(None, 0, 0, w, h, "enamel", 30)
            + f'<div class="abs" style="left:34px;top:30px;width:{w - 68}px;font:700 34px/1.12 Poppins;color:#fff">{title}</div>'
            + (f'<div class="abs" style="left:34px;top:{30 + 42 * (title.count("<br>") + 1) + 8}px;width:{w - 68}px;font:400 24px/1.3 Poppins;color:rgba(220,232,250,.85)">{sub}</div>' if sub else "")
            + f'<div class="abs" id="{id_}-slot" style="left:34px;top:{h - 118}px;width:{w - 68}px;height:70px;border-radius:16px;{MAT["porcelain"]}">'
            + f'<div class="abs" style="left:18px;top:30px;width:{w - 104}px;height:10px;border-radius:5px;background:#0b1020;box-shadow:inset 0 3px 5px rgba(0,0,0,.6)"></div></div>'
            + f'<div class="abs" id="{id_}-beam" style="left:20px;top:{h - 150}px;width:{w - 40}px;height:4px;border-radius:2px;opacity:0;'
            + 'background:linear-gradient(90deg,rgba(150,195,255,0),rgba(210,230,255,.95),rgba(150,195,255,0));box-shadow:0 0 14px rgba(150,195,255,.8)"></div>'
            + icons + '</div>')


def drawer(id_, x, y, w, h, label, front=MAT["porcelain"], tcol="#0A0D2C"):
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}border-radius:18px;{front}">'
            f'<div class="abs" style="left:0;top:{h / 2 - 22}px;width:{w}px;text-align:center;font:700 30px/1.3 Poppins;color:{tcol}">{label}</div>'
            f'<div class="abs" style="left:{w / 2 - 50}px;top:{h - 30}px;width:100px;height:12px;border-radius:6px;{MAT["alu"]}"></div></div>')


def glow_box(S, sel, at):
    S.ft(sel, {"boxShadow": GLOW_REST}, {"boxShadow": GLOW_PEAK}, at, 0.3, "power3.out")
    S.ft(sel, {"boxShadow": GLOW_PEAK}, {"boxShadow": GLOW_REST}, at + 0.35, 0.6, "sine.inOut")


SVG_IMG = '<svg viewBox="0 0 24 24" width="100%" height="100%"><rect x="3" y="4" width="18" height="16" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="9" cy="10" r="2" fill="currentColor"/><path d="M4 18l5-5 4 4 3-3 4 4" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>'
SVG_AUD = '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M3 12h2M7 8v8M11 4v16M15 7v10M19 10v4M21 12h0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>'
SVG_TXT = '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M4 6h16M4 10h16M4 14h11M4 18h8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>'
SVG_FILE = '<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M6 2h8l5 5v15H6z M14 2v5h5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>'


def floor(id_, y=1790, op=0.045):
    """lab floor: a faint drafting grid in perspective + a soft horizon band (keeps the ice plate visible)."""
    return (f'<div class="abs" id="{id_}" style="left:-500px;top:{y - 820}px;width:2080px;height:820px;'
            f'transform:perspective(900px) rotateX(64deg);transform-origin:50% 100%;'
            f'background-image:linear-gradient(rgba(10,13,44,{op}) 2px,transparent 2px),linear-gradient(90deg,rgba(10,13,44,{op}) 2px,transparent 2px);'
            f'background-size:90px 90px;-webkit-mask:linear-gradient(180deg,transparent 0%,#000 45%);mask:linear-gradient(180deg,transparent 0%,#000 45%)"></div>')
