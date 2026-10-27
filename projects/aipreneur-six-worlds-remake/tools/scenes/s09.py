"""S09 — CODE + QUALITY (29.90–36.20)
VO: "Semua bisa dirancang di Claude Code pakai maskot tiga dimensi. Timing dan detailnya tetap harus dicek."
Opens on S08's flat ruler (y 1180). It lifts into an ORIGINAL editor (built from HTML/SVG, not a product screenshot):
a preview monitor, a timeline with six scene blocks, a VO waveform track and a playhead.
EXPLAIN MODE for "Semua bisa dirancang di Claude Code pakai maskot tiga dimensi": half-body mascot, editor soft behind.
"Timing dan detailnya tetap harus dicek": he steps back (small, left foreground), the editor sharpens, a cursor scrubs the
playhead and snaps a clip, and four checks tick STORY / CAMERA / TIMING / QA (honest: a human still reviews).
Hand-off: the timeline ruler lowers into the six-card gallery shelf of S10."""
from xk import box, r3
from kit import HALF, SELF, tx, badge, blur_wrap, blur_in, blur_out, talk
from xk import check_svg

EX, EY, EW, EH = 70, 300, 940, 1010
NAMES = ["editorial", "ots", "word", "glass", "spot", "grade"]
TL_Y = 880          # timeline top inside the editor
CHECKS = ["STORY", "CAMERA", "TIMING", "QA"]


def build(S):
    s = S.id
    t0, t1 = S.t0, S.t1
    W63, W67, W72, W73, W75, W76, W78 = (S.W(i) for i in (63, 67, 72, 73, 75, 76, 78))
    # ---------------------------------------------------------------- back: editor
    blocks = []
    bw = (EW - 140) / 6
    for k in range(6):
        blocks.append(f'<div class="abs" id="{s}-b{k}" style="{box(110 + k * bw, TL_Y - EY + 40, bw - 8, 74)}border-radius:10px;overflow:hidden;'
                      f'background:linear-gradient(135deg,#0A0D2C,#294B77);box-shadow:0 6px 12px -6px rgba(10,13,44,.5)">'
                      f'<img src="{SELF}/{NAMES[k]}.jpg" alt="" style="position:absolute;left:6px;top:6px;width:36px;height:62px;border-radius:6px" />'
                      f'<div class="abs" style="left:48px;top:0;width:80px;font:700 20px/74px Poppins;color:#fff">{k + 1:02d}</div></div>')
    wave = "".join(f'<rect x="{r3(4 + i * 9)}" y="{r3(36 - h)}" width="5" height="{r3(2 * h)}" rx="2.5" fill="#294B77" opacity=".55"/>'
                   for i, h in enumerate([6 + (13 * ((i * 7) % 11) / 10) for i in range(88)]))
    S.back.append(f'<div class="abs" id="{s}-ed" style="{box(EX, EY, EW, EH)}">'
                  f'<div class="abs card" style="left:0;top:0;width:{EW}px;height:{EH}px;border-radius:30px"></div>'
                  f'<div class="abs" style="left:30px;top:26px;width:400px"><span class="tx" style="font:700 26px/30px Poppins;letter-spacing:.1em">EDITOR · SIX WORLDS</span></div>'
                  # preview monitor
                  f'<div class="abs" style="left:300px;top:80px;width:340px;height:604px;border-radius:18px;overflow:hidden;box-shadow:0 0 0 4px #0A0D2C">'
                  f'<img id="{s}-pv" src="{SELF}/editorial.jpg" alt="" style="position:absolute;left:0;top:0;width:340px;height:604px" /></div>'
                  # timeline
                  f'<div class="abs" style="left:30px;top:{TL_Y - EY}px;width:{EW - 60}px;height:250px;border-radius:18px;background:rgba(41,75,119,.06)"></div>'
                  f'<div class="abs" style="left:46px;top:{TL_Y - EY + 62}px;width:60px;font:700 20px/30px Poppins;color:#294B77">V1</div>'
                  f'<div class="abs" style="left:46px;top:{TL_Y - EY + 150}px;width:60px;font:700 20px/30px Poppins;color:#294B77">VO</div>'
                  + "".join(blocks) +
                  f'<svg class="abs" style="left:110px;top:{TL_Y - EY + 130}px;width:800px;height:72px" viewBox="0 0 800 72">{wave}</svg>'
                  f'<div class="abs" id="{s}-ph" style="left:110px;top:{TL_Y - EY + 18}px;width:4px;height:200px;background:#0A0D2C;border-radius:2px">'
                  f'<div class="abs" style="left:-9px;top:-14px;width:22px;height:22px;border-radius:5px;background:#0A0D2C;transform:rotate(45deg)"></div></div>'
                  f'<svg class="abs" id="{s}-cur" style="left:520px;top:{TL_Y - EY + 100}px;width:44px;height:44px;overflow:visible" viewBox="0 0 24 24">'
                  f'<path d="M3 2 L20 12 L12 13.5 L8 21 Z" fill="#fff" stroke="#0A0D2C" stroke-width="1.6" stroke-linejoin="round"/></svg>'
                  "</div>")
    blur_wrap(S)
    # ---------------------------------------------------------------- front: checks (right column, clear of the face when he is small-left)
    row = []
    for k, c in enumerate(CHECKS):
        row.append(f'<div class="abs" id="{s}-k{k}" style="{box(432 + k * 147, 1330, 140, 62)}border-radius:12px;background:linear-gradient(135deg,#0A0D2C,#294B77);'
                   f'box-shadow:0 10px 20px -10px rgba(10,13,44,.6)">'
                   f'<div class="abs" style="left:10px;top:15px;width:32px;height:32px">{check_svg(f"{s}-kc{k}", "#ffffff", 3.6)}</div>'
                   f'<div class="abs" style="left:44px;top:0;width:100px;font:700 19px/62px Poppins;color:#fff">{c}</div></div>')
    S.front += row
    # ---------------------------------------------------------------- motion
    # ruler lifts into the editor
    S.init(f"#{s}-ed", {"y": 260, "scaleY": 0.2, "opacity": 0, "transformOrigin": "50% 90%"})
    S.ft(f"#{s}-ed", {"y": 260, "scaleY": 0.2, "opacity": 0}, {"y": 0, "scaleY": 1, "opacity": 1}, t0, 0.5, "power3.out")
    for k in range(6):
        S.init(f"#{s}-b{k}", {"scaleX": 0, "transformOrigin": "0% 50%"})
        S.ft(f"#{s}-b{k}", {"scaleX": 0}, {"scaleX": 1}, t0 + 0.25 + k * 0.06, 0.3, "power3.out")
    blur_in(S, t0 + 0.3, 0.45)
    back = W73 - 0.32
    blur_out(S, back, 0.45)
    # playhead scrub + cursor snap (on "Timing" / "detailnya"), preview follows the playhead
    tl_w = EW - 140
    S.init(f"#{s}-ph", {"x": 0})
    S.ft(f"#{s}-ph", {"x": 0}, {"x": tl_w * 0.42}, t0 + 0.4, back - t0 - 0.4, "none")
    S.ft(f"#{s}-ph", {"x": tl_w * 0.42}, {"x": tl_w * 0.62}, W73, 0.5, "power2.inOut")
    S.ft(f"#{s}-ph", {"x": tl_w * 0.62}, {"x": tl_w * 0.97}, W75 + 0.2, t1 - W75 - 0.5, "none")
    S.init(f"#{s}-cur", {"x": 160, "y": 120, "opacity": 0})
    S.tset(f"#{s}-cur", {"opacity": 1}, back + 0.3)
    S.ft(f"#{s}-cur", {"x": 160, "y": 120}, {"x": 0, "y": 0}, back + 0.3, 0.4, "power3.out")
    S.ft(f"#{s}-cur", {"x": 0, "y": 0}, {"x": tl_w * 0.2, "y": -60}, W73, 0.5, "power2.inOut")
    S.ft(f"#{s}-b3", {"x": 0, "y": 0}, {"x": 18, "y": -6}, W75, 0.12, "power2.out")
    S.ft(f"#{s}-b3", {"x": 18, "y": -6}, {"x": 0, "y": 0}, W75 + 0.14, 0.14, "back.out(3)")
    S.fx(W75 + 0.15, "click", 0.06)
    # checks tick on Timing / detailnya / tetap / dicek
    for k, b in enumerate((W73, W75, W76, W78)):
        S.init(f"#{s}-k{k}", {"opacity": 0, "y": 24, "scale": 0.85})
        S.ft(f"#{s}-k{k}", {"opacity": 0, "y": 24, "scale": 0.85}, {"opacity": 1, "y": 0, "scale": 1}, b - 0.06, 0.28, "back.out(2)")
        S.init(f"#{s}-kc{k}", {"attr": {"stroke-dashoffset": 1}})
        S.ft(f"#{s}-kc{k}", {"attr": {"stroke-dashoffset": 1}}, {"attr": {"stroke-dashoffset": 0}}, b + 0.16, 0.22, "power2.out")
        S.fx(b + 0.16, "ping" if k == 3 else "key", 0.04)
    # hand-off: editor flattens down into the gallery shelf
    S.ft(f"#{s}-ed", {"y": 0, "scaleY": 1, "opacity": 1}, {"y": -40, "scaleY": 1, "opacity": 0}, t1 - 0.28, 0.26, "power2.in")
    for k in range(4):
        S.ft(f"#{s}-k{k}", {"opacity": 1}, {"opacity": 0}, t1 - 0.25, 0.2, "power2.in")

    # ---------------------------------------------------------------- mascot: explain (half-body) -> small left foreground pointing at the timeline
    small = {"fx": 200, "fy": 2030, "h": 980, "yaw": 26, "pitch": 6}
    S.mv([(t0, dict(HALF, fy=HALF["fy"] + 500, h=HALF["h"] * 0.8, yaw=6), None), (t0 + 0.5, dict(HALF, yaw=-3), "power3.inOut"),
          (W67, dict(HALF, yaw=4), "sine.inOut"), (back, dict(HALF, yaw=-2), "sine.inOut"), (back + 0.5, small, "power3.inOut"), (t1, dict(small, yaw=30), "sine.inOut")])
    talk(S, 63, 72, seed=2, rest=False)
    S.act("armL", [(back + 0.1, "low", 0.35), (W73 + 0.1, "point", 0.3), (W76, "pointUp", 0.3), (t1 - 0.15, "low", 0.4)])
    S.act("armR", [(back + 0.1, "low", 0.4)])
    S.act("head", [(back + 0.1, [-0.12, 0.3, 0], 0.4), (W75, [-0.2, 0.36, 0.02], 0.4), (W78, [-0.05, 0.12, 0.05], 0.3), (t1 - 0.1, [0, 0.2, 0], 0.4)])
    S.act("torso", [(back + 0.1, {"chest": [0.03, 0.12, 0]}, 0.4)])
    S.fx(t0 + 0.05, "whoosh", 0.05)
