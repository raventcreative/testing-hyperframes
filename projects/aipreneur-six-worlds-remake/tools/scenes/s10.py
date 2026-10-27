"""S10 — CTA: SIX CARDS (36.20–40.40)
VO: "Mau enam prompt dan storyboard lengkapnya? Komen CLAUDE. Gue kirim."
The editor's ruler drops into a 3x2 gallery of six ORIGINAL look frames (stills of our own six worlds), each labelled.
EXPLAIN MODE for the question: half-body mascot asking the viewer, gallery soft behind. "Komen CLAUDE": he steps back to the
lower left, the gallery sharpens, headline `MAU PROMPTNYA?` (navy gradient) + highlight box `KOMEN CLAUDE` (white on
navy). Logo stays top-left (root). Final ~0.5 s is a still, complete brand frame — no fade to black.
Promise = six prompts + storyboard (the real resource in 08_COMMENT_CLAUDE_RESOURCE.md), not 22 effects."""
from xk import box, r3
from kit import HALF, SELF, tx, badge, blur_wrap, blur_in, blur_out, talk

NAMES = ["editorial", "ots", "word", "glass", "spot", "grade"]
LABELS = ["EDITORIAL", "OVER SHOULDER", "BACKDROP WORD", "GLASS", "SPOTLIGHT", "COLOR GRADE"]
CW, CH = 220, 391
XS = [130, 430, 730]
YS = [278, 706]


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W79, W81, W83, W84, W85, W86, W87, W88 = (S.W(i) for i in (79, 81, 83, 84, 85, 86, 87, 88))
    # ---------------------------------------------------------------- back: gallery
    S.back.append(f'<div class="abs" id="{s}-shelf" style="{box(80, 1110, 920, 8)}border-radius:4px;background:#0A0D2C"></div>')
    for k, n in enumerate(NAMES):
        x, y = XS[k % 3], YS[k // 3]
        S.back.append(f'<div class="abs" id="{s}-c{k}" style="{box(x, y, CW, CH)}">'
                      f'<div class="abs card" style="left:-8px;top:-8px;width:{CW + 16}px;height:{CH + 16}px;border-radius:20px"></div>'
                      f'<div class="abs" style="left:0;top:0;width:{CW}px;height:{CH}px;border-radius:14px;overflow:hidden">'
                      f'<img src="{SELF}/{n}.jpg" alt="" style="position:absolute;left:0;top:0;width:{CW}px;height:{CH}px" /></div>'
                      f'<div class="abs" style="left:0;top:{CH - 50}px;width:{CW}px;text-align:center"><span class="badge" style="font:700 19px/1 Poppins;padding:8px 10px;border-radius:10px">{k + 1:02d} {LABELS[k]}</span></div></div>')
    blur_wrap(S)
    # ---------------------------------------------------------------- front: CTA type (right of the mascot, lower half)
    S.front.append(tx(f"{s}-h1", 470, 1150, 600, "MAU PROMPTNYA?", size=60))
    S.front.append(badge(f"{s}-h2", 470, 1236, "KOMEN CLAUDE", size=64))
    S.front.append(f'<div class="abs" id="{s}-sub" style="{box(474, 1346, 590, 40)}"><span class="tx" style="font:400 30px/40px Poppins">6 prompt + storyboard. Gue kirim.</span></div>')

    # ---------------------------------------------------------------- motion
    for k in range(6):
        x, y = XS[k % 3], YS[k // 3]
        a = {"y": 1110 - y - CH, "scaleY": 0.05, "opacity": 0, "transformOrigin": "50% 100%"}
        S.init(f"#{s}-c{k}", a)
        S.ft(f"#{s}-c{k}", dict(a), {"y": 0, "scaleY": 1, "opacity": 1}, t0 + 0.05 + k * 0.06, 0.5, "power3.out")
    S.init(f"#{s}-shelf", {"scaleX": 1, "opacity": 1})
    S.ft(f"#{s}-shelf", {"scaleX": 1, "opacity": 1}, {"scaleX": 0.3, "opacity": 0}, t0 + 0.3, 0.4, "power2.in")
    blur_in(S, t0 + 0.25, 0.45)
    back = W85 - 0.3
    blur_out(S, back, 0.45)
    S.init(f"#{s}-h1", {"opacity": 0, "y": 30})
    S.ft(f"#{s}-h1", {"opacity": 0, "y": 30}, {"opacity": 1, "y": 0}, back + 0.15, 0.35, "power3.out")
    S.init(f"#{s}-h2", {"opacity": 0, "scale": 0.7, "transformOrigin": "0% 50%"})
    S.ft(f"#{s}-h2", {"opacity": 0, "scale": 0.7}, {"opacity": 1, "scale": 1}, W86 - 0.05, 0.36, "back.out(2.2)")
    S.init(f"#{s}-sub", {"opacity": 0, "y": 16})
    S.ft(f"#{s}-sub", {"opacity": 0, "y": 16}, {"opacity": 1, "y": 0}, W87 - 0.05, 0.3, "power3.out")
    S.fx(W86 + 0.02, "pop", 0.08)
    S.fx(W87, "sparkle", 0.04)

    # ---------------------------------------------------------------- mascot: asks (half-body) -> lower left pointing at the CTA
    low = {"fx": 180, "fy": 2120, "h": 980, "yaw": 22, "pitch": 6}
    S.mv([(t0, dict(HALF, fy=HALF["fy"] + 400, yaw=10), None), (t0 + 0.45, dict(HALF, yaw=-3), "power3.inOut"), (W83, dict(HALF, yaw=4), "sine.inOut"),
          (back, dict(HALF, yaw=0), "sine.inOut"), (back + 0.5, low, "power3.inOut"), (S.WE(88), dict(low, yaw=18), "sine.inOut"), (t1, dict(low, yaw=18), "none")])
    talk(S, 79, 84, seed=1, rest=False)
    S.act("armL", [(back + 0.1, "low", 0.35), (W86 - 0.15, "point", 0.28), (W88, "present", 0.35), (S.WE(88) + 0.05, "low", 0.4)])
    S.act("armR", [(back + 0.1, "low", 0.4), (W88 - 0.05, "open", 0.3), (S.WE(88), "low", 0.4)])
    S.act("head", [(back + 0.1, [-0.06, 0.28, 0], 0.35), (W86, [0.04, 0.3, -0.03], 0.3), (W87, [-0.04, 0.0, 0.05], 0.35), (S.WE(88) + 0.05, [0, 0.06, 0], 0.4)])
    S.act("torso", [(back + 0.1, {"chest": [0.03, 0.1, 0]}, 0.4), (S.WE(88), {}, 0.4)])
    S.fx(t0 + 0.05, "whoosh", 0.05)
