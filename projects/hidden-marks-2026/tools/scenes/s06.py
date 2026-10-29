"""S06 — DIFFERENT PRODUCTS, DIFFERENT SUPPORT (W68 – W87). "Sebagian model Claude mendukung watermark teks. Sementara
gambar dan audio OpenAI yang didukung punya sinyal asal yang bisa diperiksa."  Two instrument bays (names only, no
copied UI). A glass lens rides an aluminium rail from the CLAUDE bay to the OPENAI bay; the mascot compares."""
from kit_hm import floor, stamp, stamp_in, MAT, SVG_TXT, SVG_IMG, SVG_AUD
from xk import box


def bay(id_, x, title, icons, l1, l2):
    ic = "".join(f'<div class="abs" style="left:{40 + 76 * i}px;top:120px;width:60px;height:60px;color:#294B77">{svg}</div>' for i, svg in enumerate(icons))
    return (f'<div class="abs" id="{id_}" style="{box(x, 540, 450, 430)}border-radius:30px;{MAT["porcelain"]}">'
            f'<div class="abs" style="left:0;top:0;width:450px;height:92px;border-radius:30px 30px 0 0;background:linear-gradient(108deg,#0A0D2C,#294B77);'
            f'font:700 40px/92px Poppins;color:#fff;text-align:center;letter-spacing:.06em">{title}</div>{ic}'
            f'<div class="abs" style="left:40px;top:214px;width:380px;font:700 32px/1.2 Poppins;color:#0A0D2C">{l1}</div>'
            f'<div class="abs" style="left:40px;top:300px;width:380px;font:400 26px/1.3 Poppins;color:#294B77">{l2}</div></div>')


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(bay(f"{s}-cl", 60, "CLAUDE", [SVG_TXT], "Watermark teks", "pada sebagian model"))
    S.back.append(bay(f"{s}-oa", 570, "OPENAI", [SVG_IMG, SVG_AUD], "Sinyal asal", "gambar &amp; audio yang didukung"))
    S.back.append(f'<div class="abs" id="{s}-rail" style="{box(60, 1000, 960, 16)}border-radius:8px;{MAT["alu"]}"></div>')
    S.back.append(f'<div class="abs" id="{s}-lens" style="{box(70, 520, 470, 470)}border-radius:36px;border:5px solid rgba(255,255,255,.95);'
                  f'box-shadow:0 0 0 2px rgba(41,75,119,.35),0 0 30px rgba(120,170,240,.45),inset 0 0 40px rgba(170,205,255,.35)"></div>')
    S.front.append(stamp(f"{s}-st", 540, 452, "DUKUNGAN BEDA-BEDA", 44))
    for b, d in ((f"#{s}-cl", 0), (f"#{s}-oa", 0.12)):
        S.init(b, {"opacity": 0, "y": 50, "rotationX": 20, "transformPerspective": 1400})
        S.ft(b, {"opacity": 0, "y": 50, "rotationX": 20}, {"opacity": 1, "y": 0, "rotationX": 0}, S.t0 + d, 0.55, "power3.out")
    S.init(f"#{s}-lens", {"opacity": 0, "scale": 1.1})
    S.ft(f"#{s}-lens", {"opacity": 0, "scale": 1.1}, {"opacity": 1, "scale": 1}, W(70) - 0.1, 0.35, "power2.out")
    S.ft(f"#{s}-lens", {"x": 0}, {"x": 510}, W(78) - 0.3, 0.6, "power3.inOut")       # optical slider, no spin
    S.fx(W(78) - 0.3, "whoosh", 0.05)
    S.ft(f"#{s}-cl", {"opacity": 1}, {"opacity": 0.55}, W(78), 0.5, "sine.inOut")
    stamp_in(S, f"{s}-st", W(74))
    S.cam([(S.t0, {"scale": 1.0}, None), (S.t1, {"scale": 1.03}, "sine.inOut")])
    S.mv([(S.t0, {"fx": 540, "fy": 1960, "h": 900, "yaw": 0, "pitch": 5}, None)])
    S.intent(W(68), "compare", "left")
    S.intent(W(74), "present", "right")
    S.intent(W(81), "explain", "right")
