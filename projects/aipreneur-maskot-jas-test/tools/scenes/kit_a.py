"""Fork-A helpers: synthetic mini 'screenshots' (pure HTML, no mascot inside) for cards / thumbnails."""
from xk import box, r3

NAVY = "linear-gradient(150deg,#0A0D2C 0%,#294B77 100%)"


def _bars(w, h, vals, color="#294B77", gap=0.28):
    n = len(vals)
    bw = w / (n + (n - 1) * gap)
    out = []
    for i, v in enumerate(vals):
        bh = h * v
        out.append(f'<div class="abs" style="{box(i * bw * (1 + gap), h - bh, bw, bh)}border-radius:{r3(bw * 0.25)}px {r3(bw * 0.25)}px 2px 2px;background:{color}"></div>')
    return "".join(out)


def mini(kind, w, h):
    """inner HTML of a w x h mini screen. kinds: chart, video, chat, hook, stats, list"""
    k = w / 150.0
    f = lambda px: r3(px * k)
    if kind == "chart":
        return (f'<div class="abs" style="inset:0;background:linear-gradient(180deg,#ffffff,#eef3fb)"></div>'
                f'<div class="abs" style="left:{f(12)}px;top:{f(14)}px;font:700 {f(11)}px/1 Poppins;color:#294B77;letter-spacing:.06em">VIEWS / MINGGU</div>'
                f'<div class="abs" style="left:{f(12)}px;top:{f(32)}px;font:700 {f(30)}px/1 Poppins;color:#0A0D2C">128K</div>'
                f'<div class="abs" style="left:{f(12)}px;top:{f(70)}px;padding:{f(3)}px {f(7)}px;border-radius:{f(6)}px;background:{NAVY};font:700 {f(11)}px/1.2 Poppins;color:#fff">+248%</div>'
                f'<div class="abs" style="{box(12 * k, h - 110 * k, w - 24 * k, 90 * k)}">{_bars(w - 24 * k, 90 * k, [.25, .32, .3, .45, .52, .7, .95])}</div>')
    if kind == "video":
        return (f'<div class="abs" style="inset:0;background:{NAVY}"></div>'
                f'<div class="abs" style="inset:0;background:radial-gradient(circle at 70% 25%,rgba(130,170,230,.45),rgba(130,170,230,0) 55%)"></div>'
                f'<div class="abs" style="left:{f(12)}px;top:{f(16)}px;font:700 {f(17)}px/1.1 Poppins;color:#fff;width:{f(126)}px">1 VIDEO<br>30 KONTEN</div>'
                f'<div class="abs" style="{box(w / 2 - 22 * k, h / 2 - 8 * k, 44 * k, 44 * k)}border-radius:50%;background:rgba(255,255,255,.95)"></div>'
                f'<div class="abs" style="left:{r3(w / 2 - 5 * k)}px;top:{r3(h / 2 + 4 * k)}px;width:0;height:0;border-left:{f(15)}px solid #0A0D2C;border-top:{f(10)}px solid transparent;border-bottom:{f(10)}px solid transparent"></div>'
                f'<div class="abs" style="{box(12 * k, h - 22 * k, w - 24 * k, 4 * k)}border-radius:2px;background:rgba(255,255,255,.3)"></div>'
                f'<div class="abs" style="{box(12 * k, h - 22 * k, (w - 24 * k) * 0.62, 4 * k)}border-radius:2px;background:#fff"></div>')
    if kind == "chat":
        rows = []
        y = 16
        for side, wd, ln in (("l", 100, 2), ("r", 92, 1), ("l", 110, 3), ("r", 80, 2)):
            hh = 10 + ln * 9
            x = 10 if side == "l" else 150 - 10 - wd
            bg = "#e7edf6" if side == "l" else NAVY
            lc = "rgba(41,75,119,.45)" if side == "l" else "rgba(255,255,255,.75)"
            lines = "".join(f'<div class="abs" style="left:{f(8)}px;top:{f(7 + j * 9)}px;width:{f((wd - 16) * (0.9 if j < ln - 1 else 0.6))}px;height:{f(4)}px;border-radius:2px;background:{lc}"></div>' for j in range(ln))
            rows.append(f'<div class="abs" style="{box(x * k, y * k, wd * k, hh * k)}border-radius:{f(9)}px;background:{bg}">{lines}</div>')
            y += hh + 9
        return (f'<div class="abs" style="inset:0;background:#fbfcfe"></div>'
                f'<div class="abs" style="left:0;top:0;width:{w}px;height:{f(4)}px;background:{NAVY}"></div>' + "".join(rows) +
                f'<div class="abs" style="{box(10 * k, h - 30 * k, w - 20 * k, 20 * k)}border-radius:{f(10)}px;background:#eef2f8;border:1px solid rgba(41,75,119,.15)"></div>')
    if kind == "hook":
        return (f'<div class="abs" style="inset:0;background:linear-gradient(180deg,#f4f8fe,#dfe9f7)"></div>'
                f'<div class="abs" style="left:{f(12)}px;top:{f(40)}px;width:{f(126)}px;font:700 {f(25)}px/1.05 Poppins;color:#0A0D2C">STOP<br>SCROLL<br>3 DETIK</div>'
                f'<div class="abs" style="left:{f(12)}px;top:{f(140)}px;padding:{f(4)}px {f(8)}px;border-radius:{f(7)}px;background:{NAVY};font:700 {f(12)}px/1.2 Poppins;color:#fff">HOOK</div>'
                f'<div class="abs" style="{box(12 * k, h - 40 * k, w - 24 * k, 6 * k)}border-radius:3px;background:rgba(41,75,119,.25)"></div>'
                f'<div class="abs" style="{box(12 * k, h - 28 * k, (w - 24 * k) * .6, 6 * k)}border-radius:3px;background:rgba(41,75,119,.18)"></div>')
    if kind == "stats":
        sp = " ".join(f"{r3(i * (w - 24 * k) / 6)},{r3(60 * k * (1 - v))}" for i, v in enumerate([.2, .35, .3, .5, .55, .75, .95]))
        return (f'<div class="abs" style="inset:0;background:#ffffff"></div>'
                f'<div class="abs" style="{box(12 * k, 14 * k, 34 * k, 34 * k)}border-radius:50%;background:{NAVY}"></div>'
                f'<div class="abs" style="left:{f(54)}px;top:{f(18)}px;width:{f(80)}px;height:{f(7)}px;border-radius:4px;background:#0A0D2C"></div>'
                f'<div class="abs" style="left:{f(54)}px;top:{f(32)}px;width:{f(56)}px;height:{f(6)}px;border-radius:3px;background:rgba(41,75,119,.3)"></div>'
                f'<div class="abs" style="left:{f(12)}px;top:{f(66)}px;font:700 {f(11)}px/1 Poppins;color:#294B77;letter-spacing:.06em">FOLLOWERS</div>'
                f'<div class="abs" style="left:{f(12)}px;top:{f(82)}px;font:700 {f(30)}px/1 Poppins;color:#0A0D2C">12.4K</div>'
                f'<svg class="abs" style="left:{f(12)}px;top:{f(140)}px;width:{r3(w - 24 * k)}px;height:{f(64)}px;overflow:visible" viewBox="0 0 {r3(w - 24 * k)} {f(64)}">'
                f'<polyline points="{sp}" fill="none" stroke="#294B77" stroke-width="{f(4)}" stroke-linecap="round" stroke-linejoin="round"/></svg>'
                f'<div class="abs" style="{box(12 * k, h - 34 * k, w - 24 * k, 22 * k)}border-radius:{f(8)}px;background:{NAVY}"></div>')
    # list
    items = "".join(f'<div class="abs" style="{box(12 * k, (44 + i * 34) * k, w - 24 * k, 26 * k)}border-radius:{f(8)}px;background:#eef3fb">'
                    f'<div class="abs" style="{box(6 * k, 6 * k, 14 * k, 14 * k)}border-radius:50%;background:{NAVY}"></div>'
                    f'<div class="abs" style="{box(28 * k, 10 * k, (w - 70 * k) * (0.9 - 0.15 * (i % 2)), 6 * k)}border-radius:3px;background:rgba(41,75,119,.4)"></div></div>' for i in range(5))
    return (f'<div class="abs" style="inset:0;background:#ffffff"></div>'
            f'<div class="abs" style="left:{f(12)}px;top:{f(16)}px;font:700 {f(14)}px/1 Poppins;color:#0A0D2C">Content Plan</div>' + items)


KINDS = ["video", "chart", "chat", "hook", "stats", "list"]


def shot(id_, x, y, w, h, kind, r=14, border=6, style="", extra=""):
    """a white-bordered screenshot card holding a mini screen."""
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}{style}">'
            f'<div class="abs" style="left:-{border}px;top:-{border}px;width:{w + 2 * border}px;height:{h + 2 * border}px;border-radius:{r + border}px;background:#fff;'
            f'box-shadow:0 22px 34px -18px rgba(10,13,44,.55),0 0 0 1px rgba(41,75,119,.10)"></div>'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;border-radius:{r}px;overflow:hidden">{mini(kind, w, h)}</div>{extra}</div>')


def vthumb(w, h, title, dur="0:15", light=False):
    """video-thumbnail screen: gradient frame, title, play button, duration chip."""
    bg = "linear-gradient(160deg,#dfe9f7 0%,#b9cbe6 100%)" if light else NAVY
    col = "#0A0D2C" if light else "#fff"
    pb = "#0A0D2C" if light else "rgba(255,255,255,.95)"
    tri = "#fff" if light else "#0A0D2C"
    d = min(w, h) * 0.24
    return (f'<div class="abs" style="inset:0;background:{bg}"></div>'
            f'<div class="abs" style="inset:0;background:radial-gradient(circle at 75% 20%,rgba(255,255,255,{.5 if light else .25}),rgba(255,255,255,0) 60%)"></div>'
            f'<div class="abs" style="left:{r3(w * .08)}px;top:{r3(h * .07)}px;width:{r3(w * .84)}px;font:700 {r3(w * .11)}px/1.08 Poppins;color:{col}">{title}</div>'
            f'<div class="abs" style="{box(w / 2 - d / 2, h * .58 - d / 2, d, d)}border-radius:50%;background:{pb};box-shadow:0 10px 20px -10px rgba(10,13,44,.6)"></div>'
            f'<div class="abs" style="left:{r3(w / 2 - d * .14)}px;top:{r3(h * .58 - d * .2)}px;width:0;height:0;border-left:{r3(d * .36)}px solid {tri};border-top:{r3(d * .2)}px solid transparent;border-bottom:{r3(d * .2)}px solid transparent"></div>'
            f'<div class="abs" style="right:{r3(w * .07)}px;bottom:{r3(h * .06)}px;padding:{r3(w * .02)}px {r3(w * .04)}px;border-radius:{r3(w * .03)}px;background:rgba(10,13,44,.75);font:700 {r3(w * .065)}px/1.2 Poppins;color:#fff">{dur}</div>')


def tcard(w, h, text, label, dark=False):
    """text card: big phrase + small label chip."""
    bg = NAVY if dark else "linear-gradient(160deg,#ffffff 0%,#f1f5fc 100%)"
    col = "#fff" if dark else "#0A0D2C"
    chip_bg = "rgba(255,255,255,.16)" if dark else NAVY
    return (f'<div class="abs" style="inset:0;background:{bg}"></div>'
            f'<div class="abs" style="left:{r3(w * .09)}px;top:{r3(h * .09)}px;padding:{r3(w * .02)}px {r3(w * .045)}px;border-radius:{r3(w * .035)}px;background:{chip_bg};font:700 {r3(w * .06)}px/1.25 Poppins;color:#fff;letter-spacing:.06em">{label}</div>'
            f'<div class="abs" style="left:{r3(w * .09)}px;top:{r3(h * .3)}px;width:{r3(w * .84)}px;font:700 {r3(w * .125)}px/1.1 Poppins;color:{col}">{text}</div>'
            f'<div class="abs" style="{box(w * .09, h * .86, w * .5, h * .022)}border-radius:3px;background:{"rgba(255,255,255,.35)" if dark else "rgba(41,75,119,.25)"}"></div>')


def frame_card(id_, x, y, w, h, inner, r=16, border=6, style=""):
    return (f'<div class="abs" id="{id_}" style="{box(x, y, w, h)}{style}">'
            f'<div class="abs" style="left:-{border}px;top:-{border}px;width:{w + 2 * border}px;height:{h + 2 * border}px;border-radius:{r + border}px;background:#fff;'
            f'box-shadow:0 22px 34px -18px rgba(10,13,44,.5),0 0 0 1px rgba(41,75,119,.10)"></div>'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;border-radius:{r}px;overflow:hidden">{inner}</div></div>')
