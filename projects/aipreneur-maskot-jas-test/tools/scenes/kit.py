"""Shared pieces for the 17 EFEK square (1080x1080) demos: framings, small builders, thumbnails."""
from xk import box, r3

NAVY = "linear-gradient(135deg,#0A0D2C 0%,#294B77 100%)"
TH = "assets/elements/thumbs"
THUMBS = ["sw_editorial", "fx_orbit", "sw_glass", "fx_cover", "sw_spot", "fx_growth", "sw_word", "fx_dolly", "sw_grade",
          "fx_paper", "sw_ots", "fx_headline", "fx_studio", "fx_glass", "fx_chat", "fx_phone"]
# framings for the 1080x1080 canvas (fx/fy = feet px, h = figure px; chibi model: eyes at u .583, mouth .521, hair top ~.95)
WIDE = {"fx": 540, "fy": 1050, "h": 800, "yaw": 0, "pitch": 5}    # full body, feet ~y1050, eyes ~y574
MED = {"fx": 540, "fy": 1180, "h": 1050, "yaw": 0, "pitch": 5}    # head + torso + hips: hair top ~y160, eyes ~y555, chest ~y800
HALF = {"fx": 540, "fy": 1500, "h": 1440, "yaw": 0, "pitch": 4}   # head + chest (bust): eyes ~y643, shirt from ~y900
NO_FILTER = "drop-shadow(0px 0px 0px rgba(0,208,254,0))"


def thumb(k):
    return f"{TH}/{THUMBS[k % len(THUMBS)]}.jpg"


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


def card_img(id_, x, y, w, h, k, r=16, border=6, style=""):
    """a screenshot / video-thumbnail card (white border, soft shadow)."""
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}{style}">'
            f'<div class="abs" style="left:-{border}px;top:-{border}px;width:{w + 2 * border}px;height:{h + 2 * border}px;border-radius:{r + border}px;background:#fff;'
            f'box-shadow:0 18px 30px -16px rgba(10,13,44,.45),0 0 0 1px rgba(41,75,119,.08)"></div>'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;border-radius:{r}px;overflow:hidden;background:#dfe7f3">'
            f'<img src="{thumb(k)}" alt="" style="position:absolute;left:0;top:50%;width:{w}px;height:auto;transform:translateY(-50%)" /></div></div>')
