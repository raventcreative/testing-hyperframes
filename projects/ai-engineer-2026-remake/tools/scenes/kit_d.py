"""private helpers for s13-s15 (fork D)."""
from xk import box, r3
from kit import MAT, part, ICON


def label(id_, x, y, w, text, size=28, color="#0A0D2C", align="center", weight=700, style=""):
    i = f' id="{id_}"' if id_ else ""
    return (f'<div{i} class="abs" style="left:{r3(x)}px;top:{r3(y)}px;width:{r3(w)}px;text-align:{align};'
            f'font:{weight} {size}px/1.15 Poppins, sans-serif;color:{color};letter-spacing:.02em;{style}">{text}</div>')


def icon_tile(id_, x, y, w, h, icon, color="#1c3561", mat="glass", r=16, num=None):
    """small material tile with a centred line icon (+ optional number top-left)."""
    n = (f'<div class="abs" style="left:12px;top:8px;font:700 26px/1 Poppins;color:{"#fff" if mat == "enamel" else "#294B77"}">{num}</div>'
         if num else "")
    s = min(w, h) * 0.46
    ic = (f'<div class="abs" style="left:{r3((w - s) / 2 + (10 if num else 0))}px;top:{r3((h - s) / 2 + (6 if num else 0))}px;'
          f'width:{r3(s)}px;height:{r3(s)}px;color:{color}">{ICON[icon]}</div>')
    return part(id_, x, y, w, h, mat, r, inner=n + ic)


def orb(id_, cx, cy, d):
    return (f'<div class="abs" id="{id_}" style="{box(cx - d / 2, cy - d / 2, d, d)}border-radius:50%;'
            f'background:radial-gradient(circle at 38% 32%,#ffffff 0%,#bcd6ff 30%,#3f6fb0 70%,#1c3561 100%);'
            f'box-shadow:0 0 0 6px rgba(255,255,255,.6),0 18px 30px -12px rgba(10,13,44,.6)"></div>')


def stage_models(s, PADS, RY):
    """the three stage models of S14 on the rail (returns html list); ids {s}-st0..2 / {s}-ok."""
    from kit import part, shadow, MAT
    out = []
    names = [("PROYEK", "KECIL"), ("APP LLM", "+ RAG"), ("ASISTEN", "SIAP PAKAI")]
    for k, (cx, w, h) in enumerate(PADS):
        out.append(part(None, cx - w / 2 - 20, RY - 14, w + 40, 30, "alu", 12))
        out.append(shadow(cx - w / 2, RY - 30, w, 46, 0.5))
        if k == 0:    # small ML project: porcelain cube with a scatter + fit line
            inner = (f'<svg class="abs" style="left:14px;top:14px;width:{w - 28}px;height:{h - 28}px" viewBox="0 0 100 70">'
                     + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#294B77"/>' for x, y in ((12, 56), (28, 48), (40, 42), (56, 30), (70, 26), (86, 12)))
                     + '<path d="M6 60 L94 10" stroke="#0A0D2C" stroke-width="3.5" stroke-linecap="round"/></svg>')
            mat = "porcelain"
        elif k == 1:  # LLM app + RAG: doc stack feeding a chat bubble
            inner = (icon_tile(None, 18, 20, 70, 84, "doc", mat="porcelain", r=12)
                     + icon_tile(None, w - 92, 20, 74, 84, "chat", color="#fff", mat="enamel", r=12)
                     + f'<div class="abs" style="left:92px;top:58px;width:{w - 188}px;height:6px;border-radius:3px;background:#294B77"></div>'
                     + f'<div class="abs" style="left:24px;top:118px;width:{w - 48}px;height:12px;border-radius:6px;background:rgba(10,13,44,.2)"></div>'
                     + f'<div class="abs" style="left:24px;top:140px;width:{w - 90}px;height:12px;border-radius:6px;background:rgba(10,13,44,.14)"></div>')
            mat = "glass"
        else:         # ready assistant: enamel unit with screen, check + shield lamps
            inner = (f'<div class="abs" style="left:20px;top:22px;width:{w - 40}px;height:120px;border-radius:14px;{MAT["glass"]}">'
                     f'<div class="abs" style="left:16px;top:20px;width:110px;height:12px;border-radius:6px;background:#294B77"></div>'
                     f'<div class="abs" style="left:16px;top:44px;width:140px;height:12px;border-radius:6px;background:rgba(41,75,119,.4)"></div>'
                     f'<div class="abs" style="left:16px;top:68px;width:90px;height:12px;border-radius:6px;background:rgba(41,75,119,.4)"></div></div>'
                     + icon_tile(f"{s}-ok", 26, 160, 76, 70, "check", color="#0A0D2C", mat="porcelain", r=14)
                     + icon_tile(None, w - 102, 160, 76, 70, "shield", color="#0A0D2C", mat="porcelain", r=14))
            mat = "enamel"
        out.append(f'<div class="abs" id="{s}-st{k}" style="{box(cx - w / 2, RY - 14 - h, w, h)}">{part(None, 0, 0, w, h, mat, 22, inner=inner)}</div>')
    return out
