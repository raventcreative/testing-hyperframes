"""S03 — 02 CHAT TAKEOVER (6.87–8.20)  VO: "Chat mengambil alih layar."
S02's 'Aa' chip is now the chat avatar (AVATAR). A smoked-glass chat window grows out of it and takes over the
frame - it covers the character (FRONT layer) except one cut-out: the reply bubble's video preview (PREVIEW), where
the live mascot reappears small (PREVIEW_VIEW). Messages are VO words: user 'Satu klip polos.' -> typing dots ->
reply 'Dua puluh efek.' / 'Lihat hasilnya.' + the live preview. A cursor clicks the preview (cyan flash, he waves).
Hand-off: the chat UI falls away and only the preview frame with the mascot remains -> S04 makes it a real frame."""
from xk import box, r3, CYAN, clip_rect, CLIP_NONE
from kit import MED, AVATAR, CHAT, PREVIEW, PREVIEW_VIEW
from kit_a import chip

CX, CY, CW, CH_, CR = CHAT
QX, QY, QW, QH, QR = PREVIEW


def rrect(x, y, w, h, r):
    return (f"M{r3(x + r)} {r3(y)} H{r3(x + w - r)} A{r} {r} 0 0 1 {r3(x + w)} {r3(y + r)} V{r3(y + h - r)} A{r} {r} 0 0 1 {r3(x + w - r)} {r3(y + h)} "
            f"H{r3(x + r)} A{r} {r} 0 0 1 {r3(x)} {r3(y + h - r)} V{r3(y + r)} A{r} {r} 0 0 1 {r3(x + r)} {r3(y)} Z")


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W17, W18, W19, W20 = S.W(17), S.W(18), S.W(19), S.W(20)    # Chat 6.94, mengambil 7.20, alih 7.54, layar 7.76
    ax, ay, ad = AVATAR
    g0, g1 = t0 + 0.0, t0 + 0.42          # window growth
    m0, m1 = t0 + 0.08, t0 + 0.5          # mascot shrinks into the preview
    click = W20 + 0.02
    out0 = t1 - 0.24                       # chat UI falls away
    lx, ly = QX - CX, QY - CY              # preview hole in panel-local coords
    bx, by, bw, bh = 160, 100, 620, 950    # reply bubble (local)
    # opaque smoked panel with a rounded cut-out at the preview: the cut-out's huge box-shadow IS the panel fill
    # (clipped by the panel's rounded overflow) -> the live mascot shows through the hole only
    panel = (f'<div class="abs" id="{s}-panel" style="{box(CX, CY, CW, CH_)}border-radius:{CR}px;overflow:hidden">'
             f'<div class="abs" style="left:{lx}px;top:{ly}px;width:{QW}px;height:{QH}px;border-radius:{QR}px;box-shadow:0 0 0 1600px rgba(17,34,68,.975)"></div>'
             f'<div class="abs" style="left:0;top:0;width:{CW}px;height:300px;background:linear-gradient(180deg,rgba(120,170,235,.16),rgba(120,170,235,0))"></div>'
             f'<div class="abs" style="left:0;top:{CH_ - 300}px;width:{CW}px;height:300px;background:linear-gradient(0deg,rgba(3,8,28,.35),rgba(3,8,28,0))"></div>'
             f'<div class="abs" style="left:0;top:0;width:{CW}px;height:{CH_}px;border-radius:{CR}px;border:2px solid rgba(255,255,255,.24);'
             f'box-shadow:inset 0 1px 0 rgba(255,255,255,.3)"></div>'
             f'<div class="abs" style="left:40px;top:26px;width:200px;font:700 30px/44px Poppins, sans-serif;color:#fff">'
             f'<span style="display:inline-block;width:12px;height:12px;border-radius:6px;background:{CYAN};margin-right:12px;vertical-align:2px"></span>Chat</div>'
             f'<div class="abs" id="{s}-rb" style="left:{bx}px;top:{by}px;width:{bw}px;height:{bh}px;border-radius:30px;border:1.5px solid rgba(255,255,255,.2)"></div>'
             f'<div class="abs" style="left:{bx}px;top:{by}px;width:{bw}px;height:{ly - by - 20}px;border-radius:30px 30px 10px 10px;background:rgba(255,255,255,.06)"></div>'
             f'<div class="abs acrylic" id="{s}-ub" style="left:{CW - 490}px;top:22px;width:450px;height:68px;border-radius:34px 34px 8px 34px;'
             f'font:400 30px/66px Poppins, sans-serif;color:#fff;text-align:center">Satu klip polos.</div>'
             + "".join(f'<div class="abs" id="{s}-d{k}" style="left:{bx + 34 + k * 26}px;top:{by + 44}px;width:14px;height:14px;border-radius:7px;background:#fff"></div>' for k in range(3))
             + f'<div class="abs" id="{s}-t1" style="left:{bx + 32}px;top:{by + 20}px;width:560px;font:700 40px/52px Poppins, sans-serif;color:#fff">Dua puluh <span style="color:{CYAN}">efek.</span></div>'
             f'<div class="abs" id="{s}-t2" style="left:{bx + 32}px;top:{by + 76}px;width:560px;font:400 30px/42px Poppins, sans-serif;color:#fff">Lihat hasilnya.</div>'
             '</div>')
    S.front.append(panel)
    S.front.append(f'<div class="abs" id="{s}-qb" style="{box(QX, QY, QW, QH)}border-radius:{QR}px;border:4px solid rgba(255,255,255,.9);'
                   f'box-shadow:0 0 0 1px rgba(0,208,254,.3), 0 0 22px rgba(0,208,254,.25)"></div>')
    S.front.append(f'<div class="abs" id="{s}-qf" style="{box(QX, QY, QW, QH)}border-radius:{QR}px;border:4px solid {CYAN};box-shadow:0 0 26px rgba(0,208,254,.8), inset 0 0 26px rgba(0,208,254,.45)"></div>')
    S.front.append(chip(f"{s}-av", ax, ay, ad, "aa"))
    S.front.append(f'<svg class="abs" id="{s}-cur" style="left:0;top:0;width:56px;height:66px;overflow:visible" viewBox="0 0 40 46">'
                   f'<path d="M6 3 L6 35 L14 27 L20 41 L26 38 L20 25 L31 25 Z" fill="#fff" stroke="#0b1636" stroke-width="2" stroke-linejoin="round" '
                   f'style="filter:drop-shadow(0 4px 6px rgba(3,8,28,.6))"/></svg>')

    # ---------------------------------------------------------------- motion: window grows out of the avatar
    S.init(f"#{s}-panel", {"scale": ad / CW, "opacity": 0, "transformOrigin": f"{ax - CX}px {ay - CY}px"})
    S.ft(f"#{s}-panel", {"scale": ad / CW, "opacity": 0}, {"scale": 1, "opacity": 1}, g0, g1 - g0, "power3.out")
    S.ft(f"#{s}-panel", {"opacity": 1, "y": 0}, {"opacity": 0, "y": -30}, out0, 0.2, "power2.in")
    S.init(f"#{s}-ub", {"opacity": 0, "y": 20})
    S.ft(f"#{s}-ub", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, W17 + 0.1, 0.22, "power3.out")
    for k in range(3):
        S.init(f"#{s}-d{k}", {"opacity": 0, "y": 0})
        S.tset(f"#{s}-d{k}", {"opacity": 0.85}, W18 - 0.02)
        S.ft(f"#{s}-d{k}", {"y": 0}, {"y": -8}, W18 + k * 0.06, 0.1, "sine.out")
        S.ft(f"#{s}-d{k}", {"y": -8}, {"y": 0}, W18 + 0.1 + k * 0.06, 0.1, "sine.in")
        S.tset(f"#{s}-d{k}", {"opacity": 0}, W19 - 0.06)
    for k, sel in enumerate((f"#{s}-t1", f"#{s}-t2")):
        S.init(sel, {"opacity": 0, "y": 14})
        S.ft(sel, {"opacity": 0, "y": 14}, {"opacity": 1, "y": 0}, W19 - 0.04 + k * 0.08, 0.22, "power3.out")
    S.init(f"#{s}-qb", {"opacity": 0, "scale": 1.06, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-qb", {"opacity": 0, "scale": 1.06}, {"opacity": 1, "scale": 1}, m1 - 0.12, 0.2, "power2.out")
    S.init(f"#{s}-qf", {"opacity": 0})
    S.ft(f"#{s}-qf", {"opacity": 0}, {"opacity": 1}, click, 0.06, "none")
    S.ft(f"#{s}-qf", {"opacity": 1}, {"opacity": 0}, click + 0.08, 0.3, "power2.out")
    S.init(f"#{s}-av", {"opacity": 1, "scale": 1})
    S.ft(f"#{s}-av", {"opacity": 1, "scale": 1}, {"opacity": 0, "scale": 0.7}, out0 - 0.02, 0.2, "power2.in")
    # cursor glides to the preview and clicks
    S.init(f"#{s}-cur", {"x": 980, "y": 1330, "opacity": 0, "scale": 1, "transformOrigin": "15% 10%"})
    S.ft(f"#{s}-cur", {"opacity": 0}, {"opacity": 1}, W19 - 0.12, 0.08, "none")
    S.ft(f"#{s}-cur", {"x": 980, "y": 1330}, {"x": 690, "y": 1140}, W19 - 0.06, click - W19 + 0.04, "power3.inOut")
    S.ft(f"#{s}-cur", {"scale": 1}, {"scale": 0.82}, click - 0.03, 0.05, "power2.in")
    S.ft(f"#{s}-cur", {"scale": 0.82}, {"scale": 1}, click + 0.03, 0.12, "power2.out")
    S.ft(f"#{s}-cur", {"opacity": 1}, {"opacity": 0}, out0, 0.16, "none")

    # ---------------------------------------------------------------- mascot: shrinks into the preview (re-framed, clipped)
    S.mv([(t0, dict(MED, yaw=-14, pitch=6), None), (m0, {}, "none"), (m1, dict(PREVIEW_VIEW, yaw=-6), "power3.inOut"), (t1, dict(PREVIEW_VIEW, yaw=0), "sine.inOut")])
    S.mc([(t0, {"clipPath": CLIP_NONE}, None), (m0, {}, "none"), (m1, {"clipPath": clip_rect(QX, QY, QW, QH, QR)}, "power3.inOut")])
    S.act("head", [(t0, [-0.12, 0.3, 0.06], 0.3), (W18, [0.02, 0.08, 0], 0.35), (W19, [-0.04, -0.06, -0.03], 0.3), (click, [-0.1, 0.12, 0.08], 0.25)])
    S.act("armL", [(t0, "present", 0.3), (W18, "low", 0.35), (click - 0.06, "wave", 0.25), (t1 - 0.05, "low", 0.35)])
    S.act("armR", [(t0, "low", 0.35)])
    S.act("torso", [(t0, {}, 0.35)])
    S.fx(g0 + 0.02, "whoosh", 0.05)
    S.fx(W17 + 0.12, "pop", 0.05)
    S.fx(W19 - 0.02, "pop", 0.05)
    S.fx(click, "click", 0.08)
