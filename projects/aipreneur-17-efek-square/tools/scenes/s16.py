"""S16 — COVER STORY (effect #16).
Magazine cover: big serif title AIPRENEUR behind the head (letter-spacing tightens 30px -> 3px in 0.45 s), small labels
top-left / top-right, one italic sentence bottom-left, barcode bottom-right. The mascot's hair covers part of the title."""
from xk import box, r3

TITLE_Y, TITLE_PX = 92, 166
TITLE = "AIPRENEUR"
ADV = [119.88, 64.59, 101.41, 119.88, 110.72, 119.88, 110.72, 119.88, 119.88]   # Liberation Serif Bold advances at 166px (PIL)


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    S.back.append(f'<div class="abs" style="left:0;top:0;width:1080px;height:1080px;'
                  f'background:radial-gradient(ellipse at 50% 62%, rgba(255,255,255,.85) 0%, rgba(255,255,255,0) 60%), linear-gradient(180deg,#dfe8f4 0%,#f4f7fb 70%)"></div>')
    # title = one span per glyph at its final (3px-tracked) x; the 30px -> 3px tracking is animated as each glyph's x
    total = sum(ADV) + 3 * (len(TITLE) - 1)
    x, glyphs = 540 - total / 2, []
    for k, ch in enumerate(TITLE):
        glyphs.append(f'<span class="abs" id="{s}-g{k}" style="left:{r3(x)}px;top:0;font:700 {TITLE_PX}px/1 \'Liberation Serif\', serif;'
                      f'background:linear-gradient(180deg,#0A0D2C 0%,#294B77 100%);-webkit-background-clip:text;background-clip:text;'
                      f'-webkit-text-fill-color:transparent;color:#0A0D2C">{ch}</span>')
        x += ADV[k] + 3
    S.back.append(f'<div class="abs" id="{s}-title" style="left:0;top:{TITLE_Y}px;width:1080px;height:{TITLE_PX + 20}px">' + "".join(glyphs) + "</div>")
    S.back.append(f'<div class="abs" id="{s}-rule" style="{box(40, 74, 1000, 3)}background:#0A0D2C"></div>')
    S.back.append(f'<div class="abs" id="{s}-tl" style="{box(40, 30, 420, 36)}font:700 24px/36px Poppins, sans-serif;letter-spacing:.12em;color:#0A0D2C">EDISI 17 · OKT 2026</div>')
    S.back.append(f'<div class="abs" id="{s}-tr" style="{box(620, 30, 420, 36)}font:700 24px/36px Poppins, sans-serif;letter-spacing:.12em;color:#0A0D2C;text-align:right">SPESIAL AI BISNIS</div>')
    # cover lines in front of the photo (bottom-left italic sentence + small barcode bottom-right)
    S.front.append(f'<div class="abs" id="{s}-q" style="{box(36, 872, 300, 170)}">'
                   f'<div class="abs" style="left:0;top:0;width:60px;height:5px;background:#0A0D2C"></div>'
                   f'<div class="abs" style="left:0;top:18px;width:300px;font:italic 400 36px/1.18 \'Liberation Serif\', serif;color:#0A0D2C">'
                   f'“AI bukan pengganti. AI itu pengungkit.”</div></div>')
    bars = "".join(f'<rect x="{r3(x)}" y="0" width="{w}" height="64" fill="#0A0D2C"/>' for x, w in
                   [(0, 3), (5, 1), (8, 2), (12, 4), (18, 1), (21, 3), (26, 2), (30, 1), (33, 4), (39, 2), (43, 1), (46, 3), (51, 1), (54, 2), (58, 4), (64, 1), (67, 3), (72, 2), (76, 1), (79, 3)])
    S.front.append(f'<div class="abs" id="{s}-bc" style="{box(884, 946, 156, 100)}background:#fff;border-radius:4px;padding:8px 16px">'
                   f'<svg width="86" height="64" viewBox="0 0 82 64">{bars}</svg>'
                   f'<div style="font:400 11px/14px \'DejaVu Sans Mono\', monospace;color:#0A0D2C;letter-spacing:.08em">9 771234 5017</div></div>')

    # ---------------------------------------------------------------- motion
    for k in range(len(TITLE)):
        a = {"x": r3(27 * (k - (len(TITLE) - 1) / 2))}
        S.init(f"#{s}-g{k}", a)
        S.ft(f"#{s}-g{k}", a, {"x": 0}, t0 + 0.35, 0.45, "power3.out")
    S.init(f"#{s}-rule", {"scaleX": 0, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-rule", {"scaleX": 0}, {"scaleX": 1}, t0 + 0.5, 0.45, "power3.inOut")
    for k, sel in enumerate((f"#{s}-tl", f"#{s}-tr")):
        S.init(sel, {"opacity": 0, "y": 12})
        S.ft(sel, {"opacity": 0, "y": 12}, {"opacity": 1, "y": 0}, t0 + 0.7 + k * 0.08, 0.3, "power3.out")
    S.init(f"#{s}-q", {"opacity": 0, "x": -24})
    S.ft(f"#{s}-q", {"opacity": 0, "x": -24}, {"opacity": 1, "x": 0}, t0 + 1.0, 0.4, "power3.out")
    S.init(f"#{s}-bc", {"opacity": 0})
    S.ft(f"#{s}-bc", {"opacity": 0}, {"opacity": 1}, t0 + 1.2, 0.3, "power2.out")

    # ---------------------------------------------------------------- mascot: cover pose, hair over the title
    v = {"fx": 560, "fy": 1206, "h": 1040, "yaw": -8, "pitch": 4}
    S.mv([(t0, v, None), (t0 + 2.4, dict(v, yaw=6), "sine.inOut"), (t1, dict(v, yaw=-2), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.9, "chin", 0.45), (t0 + 3.1, "present", 0.4)])
    S.act("armR", [(t0, "low", 0.3)])
    S.act("head", [(t0, [-0.03, -0.1, 0.04], 0.3), (t0 + 0.9, [0.04, 0.14, 0.08], 0.45), (t0 + 3.1, [-0.04, -0.06, -0.05], 0.45)])
    S.act("torso", [(t0, {"chest": [0, -0.08, 0]}, 0.3), (t0 + 2.4, {"chest": [0, 0.08, 0]}, 0.6)])
