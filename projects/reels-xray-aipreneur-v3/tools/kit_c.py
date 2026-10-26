"""Helpers shared by s10–s12 (modular template, change the content, reassemble the reel)."""
from xk import box, r3, screw


def product_a(id_, x, y, s=1.0):
    """'old' product: navy bottle with porcelain cap + label band (illustrated, no text)."""
    def b(px, py, w, h):
        return box(x + px * s, y + py * s, w * s, h * s)
    return (f'<div class="abs" id="{id_}" style="{box(x, y, 120 * s, 170 * s)}">'
            f'<div class="abs" style="{box(14 * s, 150 * s, 92 * s, 18 * s)}border-radius:50%;background:radial-gradient(ellipse,rgba(28,51,84,.35),rgba(28,51,84,0) 70%)"></div>'
            f'<div class="abs" style="{box(30 * s, 50 * s, 60 * s, 110 * s)}border-radius:{r3(18 * s)}px {r3(18 * s)}px {r3(12 * s)}px {r3(12 * s)}px;background:linear-gradient(100deg,#3a6299 0%,#294b77 45%,#1c3354 100%);box-shadow:inset {r3(5 * s)}px 0 0 rgba(255,255,255,.18)"></div>'
            f'<div class="abs" style="{box(46 * s, 30 * s, 28 * s, 24 * s)}background:linear-gradient(90deg,#294b77,#1c3354)"></div>'
            f'<div class="abs" style="{box(40 * s, 12 * s, 40 * s, 22 * s)}border-radius:{r3(6 * s)}px;background:linear-gradient(160deg,#ffffff,#d6e2f2)"></div>'
            f'<div class="abs" style="{box(30 * s, 92 * s, 60 * s, 30 * s)}background:linear-gradient(160deg,#fbfcfe,#dfe8f5)"></div>'
            f'<div class="abs" style="{box(40 * s, 103 * s, 26 * s, 6 * s)}border-radius:3px;background:#294b77"></div>'
            f'</div>')


def product_b(id_, x, y, s=1.0):
    """'new' product: porcelain jar with a mint lid and a navy seal dot (illustrated, no text)."""
    return (f'<div class="abs" id="{id_}" style="{box(x, y, 120 * s, 170 * s)}">'
            f'<div class="abs" style="{box(8 * s, 150 * s, 104 * s, 18 * s)}border-radius:50%;background:radial-gradient(ellipse,rgba(28,51,84,.35),rgba(28,51,84,0) 70%)"></div>'
            f'<div class="abs" style="{box(16 * s, 72 * s, 88 * s, 86 * s)}border-radius:{r3(16 * s)}px {r3(16 * s)}px {r3(22 * s)}px {r3(22 * s)}px;background:linear-gradient(100deg,#ffffff 0%,#eef3fa 50%,#c9d8ee 100%);box-shadow:inset 0 0 0 1.5px rgba(172,198,231,.8)"></div>'
            f'<div class="abs" style="{box(10 * s, 48 * s, 100 * s, 30 * s)}border-radius:{r3(10 * s)}px;background:linear-gradient(180deg,#c9efe1 0%,#9fd8c4 60%,#6fbca2 100%)"></div>'
            f'<div class="abs" style="{box(10 * s, 70 * s, 100 * s, 6 * s)}background:rgba(28,51,84,.18)"></div>'
            f'<div class="abs" style="{box(46 * s, 100 * s, 28 * s, 28 * s)}border-radius:50%;background:linear-gradient(150deg,#3a6299,#1c3354)"></div>'
            f'<div class="abs" style="{box(24 * s, 140 * s, 72 * s, 5 * s)}border-radius:3px;background:#cbdbf4"></div>'
            f'</div>')


BARS_A = [(150, True), (210, False), (120, False)]
BARS_B = [(96, True), (180, True), (230, False)]


def bars(id_, x, y, pattern, s=1.0, gap=22, h=12):
    out = []
    for k, (w, ink) in enumerate(pattern):
        out.append(f'<div class="abs" id="{id_}-{k}" style="{box(x, y + k * gap * s, w * s, h * s)}border-radius:{r3(h * s / 2)}px;background:{"#294b77" if ink else "#cbdbf4"}"></div>')
    return "".join(out)


def reel_frame(id_, x, y, w, h, inner="", cls="por", glass=True):
    """porcelain reel frame (9:16-ish) with a glass screen holding `inner` (coords inside the screen)."""
    sw, sh = w - 32, h - 64
    return (f'<div class="abs {cls}" id="{id_}" style="{box(x, y, w, h)}border-radius:{r3(w * 0.14)}px">'
            f'<div class="abs" style="{box(w / 2 - 30, 13, 60, 6)}border-radius:3px;background:#cbdbf4;box-shadow:inset 0 1px 2px rgba(28,51,84,.3)"></div>'
            f'<div class="abs" style="{box(w / 2 + 40, 11, 10, 10)}border-radius:50%;background:#294b77"></div>'
            f'<div class="abs" id="{id_}-scr" style="{box(16, 32, sw, sh)}border-radius:12px;overflow:hidden;'
            f'background:linear-gradient(170deg,#fbfcfe 0%,#eef3fa 60%,#e2eaf6 100%);box-shadow:inset 0 0 0 2px rgba(41,75,119,.45)">{inner}</div>'
            f'<div class="abs" style="{box(w / 2 - 40, h - 22, 80, 6)}border-radius:3px;background:#dbe6f6"></div>'
            f'</div>')


def ruler(id_, x, y, w, ticks=24):
    t = []
    for k in range(ticks + 1):
        tx = 20 + (w - 40) * k / ticks
        th = 22 if k % 4 == 0 else 12
        t.append(f'<div class="abs" style="{box(tx - 1, 14, 2, th)}background:{"#294b77" if k % 4 == 0 else "#9fb6d6"}"></div>')
    return (f'<div class="abs por-flat" id="{id_}" style="{box(x, y, w, 70)}border-radius:14px">{"".join(t)}'
            f'<div class="abs" style="{box(20, 48, w - 40, 4)}border-radius:2px;background:#dbe6f6"></div></div>')


def diamond(id_, x, y, size=26, col="#294b77"):
    return (f'<div class="abs" id="{id_}" style="{box(x - size / 2, y - size / 2, size, size)}">'
            f'<div class="abs" style="{box(size * 0.15, size * 0.15, size * 0.7, size * 0.7)}border-radius:4px;background:{col};'
            f'box-shadow:0 3px 6px rgba(28,51,84,.35),inset 1px 1px 0 rgba(255,255,255,.35);transform:rotate(45deg)"></div></div>')
