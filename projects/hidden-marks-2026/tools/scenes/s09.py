"""S09 — OPENAI VERIFY (W101 – W109). "Untuk gambar atau audio OpenAI, pakai OpenAI Verify."  The camera tracks
right along the same rail: the Claude station slides out, the second station (official name only) slides in; its
type selector lights IMAGE then AUDIO on the spoken words. No fabricated result."""
from kit_hm import floor, station, stamp, stamp_in, MAT, SVG_IMG, SVG_AUD, SIDE_L
from xk import box


def build(S):
    s, W = S.id, S.W
    S.back.append(floor(f"{s}-floor"))
    S.back.append(f'<div class="abs" id="{s}-rail" style="{box(0, 1240, 1080, 16)}border-radius:8px;{MAT["alu"]}"></div>')
    S.back.append(station(f"{s}-old", 420, 560, 600, 640, "CLAUDE<br>CONTENT CHECKER", "memeriksa file Claude yang didukung"))
    icons = "".join(f'<div class="abs" id="{s}-t{i}" style="left:{40 + 150 * i}px;top:300px;width:128px;height:128px;border-radius:24px;'
                    f'background:rgba(255,255,255,.10);border:2px solid rgba(255,255,255,.25);color:#fff;padding:26px">{svg}</div>'
                    for i, svg in enumerate((SVG_IMG, SVG_AUD)))
    S.back.append(station(f"{s}-ov", 420, 560, 600, 640, "OPENAI VERIFY", "gambar &amp; audio yang didukung", icons))
    S.front.append(stamp(f"{s}-st", 540, 452, "OPENAI VERIFY", 44))
    S.ft(f"#{s}-old", {"x": 0, "opacity": 1}, {"x": -900, "opacity": 0.4}, S.t0, 0.8, "power3.inOut")
    S.init(f"#{s}-ov", {"x": 900})
    S.ft(f"#{s}-ov", {"x": 900}, {"x": 0}, S.t0 + 0.08, 0.8, "power3.inOut")
    S.fx(S.t0 + 0.1, "whoosh", 0.05)
    for i, wi in enumerate((102, 104)):
        S.ft(f"#{s}-t{i}", {"backgroundColor": "rgba(255,255,255,0.10)", "scale": 1}, {"backgroundColor": "rgba(160,200,255,0.35)", "scale": 1.08}, W(wi), 0.25, "power3.out")
        S.ft(f"#{s}-t{i}", {"scale": 1.08}, {"scale": 1}, W(wi) + 0.25, 0.35, "sine.inOut")
        S.fx(W(wi), "click", 0.05)
    S.ft(f"#{s}-ov-beam", {"opacity": 0, "y": 0}, {"opacity": 1, "y": 0}, W(107), 0.1, "none")
    S.ft(f"#{s}-ov-beam", {"y": 0}, {"y": -330}, W(107) + 0.1, 0.8, "sine.inOut")
    S.ft(f"#{s}-ov-beam", {"opacity": 1}, {"opacity": 0}, W(107) + 0.9, 0.2, "none")
    stamp_in(S, f"{s}-st", W(107))
    S.mv([(S.t0, dict(SIDE_L, fx=200, fy=1790, h=860), None)])
    S.intent(W(101), "point", "right")
    S.intent(W(106), "present", "right")
