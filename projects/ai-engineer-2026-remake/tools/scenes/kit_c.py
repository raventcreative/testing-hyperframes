"""Private helpers for S10–S12 (agent loop -> evaluation gauge -> production casing). One continuous object chain:
S10 the agent's loop WHEEL (+ robot hub) -> S11 the wheel becomes the EVALUATION GAUGE, the hub sits on the test bench
-> S12 the passed hub rises into the PRODUCTION casing (which ends exactly at kit.MACHINE)."""
import math
from xk import box, r3
from kit import MAT, ICON

C10 = (470, 950)            # S10 wheel centre
G11 = (460, 900)            # S11 gauge centre (= the S10 wheel after its hand-off move)
B11 = (460, 1330)           # S11 bench slot: hub centre on the test bench
WHEEL_D = 520               # bezel diameter (face 480)
HUB_D = 190
POINTER_L = 200
DEMO_R = {"fx": 905, "fy": 1760, "h": 760, "yaw": -28, "pitch": 6}   # mascot, small lower-right, turned to the machine


def pol(c, r, a):
    """screen point at angle a (deg, 0 = up, clockwise) radius r around c."""
    return c[0] + r * math.sin(math.radians(a)), c[1] - r * math.cos(math.radians(a))


def wheel(id_, c, d=WHEEL_D):
    """brushed-aluminium bezel + porcelain face (the loop wheel / gauge body)."""
    f = d - 40
    return (f'<div class="abs" id="{id_}" style="{box(c[0] - d / 2, c[1] - d / 2, d, d)}">'
            f'<div class="abs" style="inset:0;border-radius:50%;{MAT["alu"]}"></div>'
            f'<div class="abs" style="left:20px;top:20px;width:{f}px;height:{f}px;border-radius:50%;'
            f'background:radial-gradient(circle at 38% 30%,#ffffff 0%,#f2f5fa 55%,#dde5f0 100%);'
            f'box-shadow:inset 0 6px 14px rgba(41,75,119,.18),inset 0 -2px 0 rgba(255,255,255,.9)"></div>'
            f'<div class="abs" style="left:60px;top:60px;width:{f - 80}px;height:{f - 80}px;border-radius:50%;border:2px dashed rgba(41,75,119,.18)"></div></div>')


def pointer(id_, c, length=POINTER_L, w=18):
    """enamel pointer bar (rotation 0 = up), pivot at the wheel centre; alu tip."""
    return (f'<div class="abs" id="{id_}" style="{box(c[0] - w / 2, c[1] - length, w, length)}border-radius:{w / 2}px;{MAT["enamel"]}">'
            f'<div class="abs" style="left:-5px;top:-6px;width:{w + 10}px;height:{w + 10}px;border-radius:50%;{MAT["alu"]}"></div></div>')


def hub(id_, c, d=HUB_D, sticker=False, sid=""):
    """the little task robot: satin navy puck, frosted visor with two eyes, a card slot on top, a side module socket."""
    st = (f'<div class="abs" id="{sid}" style="left:{d - 62}px;top:-14px;width:72px;height:72px;border-radius:50%;'
          f'background:linear-gradient(135deg,#0A0D2C,#294B77);box-shadow:0 0 0 5px #fff,0 10px 18px -8px rgba(10,13,44,.6);color:#fff;padding:16px">{ICON["check"]}</div>'
          if sticker else "")
    return (f'<div class="abs" id="{id_}" style="{box(c[0] - d / 2, c[1] - d / 2, d, d)}">'
            f'<div class="abs" style="inset:0;border-radius:50%;{MAT["enamel"]}"></div>'
            f'<div class="abs" style="left:{d * .2}px;top:-10px;width:{d * .6}px;height:20px;border-radius:10px;{MAT["alu"]}"></div>'
            f'<div class="abs" style="left:{d * .28}px;top:-4px;width:{d * .44}px;height:7px;border-radius:4px;background:#0b1020"></div>'
            f'<div class="abs" style="left:{d * .18}px;top:{d * .34}px;width:{d * .64}px;height:{d * .3}px;border-radius:{d * .15}px;{MAT["glass"]}"></div>'
            f'<div class="abs" id="{id_}-e1" style="left:{d * .33}px;top:{d * .44}px;width:{d * .1}px;height:{d * .1}px;border-radius:50%;background:#7fb2ff;box-shadow:0 0 10px #9fc4ff"></div>'
            f'<div class="abs" id="{id_}-e2" style="left:{d * .57}px;top:{d * .44}px;width:{d * .1}px;height:{d * .1}px;border-radius:50%;background:#7fb2ff;box-shadow:0 0 10px #9fc4ff"></div>'
            f'{st}</div>')


def pod(id_, x, y, icon, d=110):
    """a station pod on the loop: frosted glass puck with a navy line icon (+ a navy 'active' ring overlay)."""
    return (f'<div class="abs" id="{id_}" style="{box(x - d / 2, y - d / 2, d, d)}">'
            f'<div class="abs" style="inset:0;border-radius:50%;{MAT["glass"]}"></div>'
            f'<div class="abs" style="left:{d * .27}px;top:{d * .27}px;width:{d * .46}px;height:{d * .46}px;color:#1c3561">{icon}</div>'
            f'<div class="abs" id="{id_}-on" style="inset:-6px;border-radius:50%;border:5px solid #294B77;box-shadow:0 0 18px rgba(41,75,119,.45)"></div></div>')


def label(id_, x, y, text, size=28, w=260):
    return (f'<div class="abs" id="{id_}" style="left:{r3(x - w / 2)}px;top:{r3(y)}px;width:{w}px;text-align:center">'
            f'<span class="tx" style="font:700 {size}px/1.1 Poppins, sans-serif;letter-spacing:.04em">{text}</span></div>')
