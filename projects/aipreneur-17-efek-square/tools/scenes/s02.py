"""S02 — COUCH WALL. The wall behind him turns into a 4x3 grid of content cards (video thumbnails alternating with
text cards). They pop in one by one from the centre outwards (0.035 s stagger) with a seeded +-3 deg tilt. The body
stays in front; one big sentence sits under the chest. Then a slow push-in holds the finished wall."""
import math
from xk import box, r3, Rng
from kit import MED, badge
from kit_a import frame_card, vthumb, tcard

COLS, ROWS = 4, 3
M, G = 34, 20
CW = (1080 - 2 * M - (COLS - 1) * G) / COLS
CH = (1080 - 2 * M - (ROWS - 1) * G) / ROWS
VIDS = ["AI untuk UMKM", "Prompt foto produk", "Video 5 menit", "Auto caption", "Riset konten 10x", "Iklan lebih hemat"]
TXTS = [("Hook 3 detik pertama", "HOOK"), ("Script dibantu AI", "SCRIPT"), ("1 ide = 10 konten", "IDE"),
        ("Posting tiap hari", "RUTIN"), ("CTA yang jelas", "CTA"), ("Repurpose otomatis", "SISTEM")]


def build(S):
    s, t0, t1 = S.id, S.t0, S.t1
    R = Rng(23)
    cells = []
    vi = ti = 0
    for r in range(ROWS):
        for c in range(COLS):
            x, y = M + c * (CW + G), M + r * (CH + G)
            if (r + c) % 2 == 0:
                inner = vthumb(CW, CH, VIDS[vi], dur=f"0:{15 + vi * 7:02d}", light=(vi % 3 == 2)); vi += 1
            else:
                txt, lab = TXTS[ti]; inner = tcard(CW, CH, txt, lab, dark=(ti % 3 == 1)); ti += 1
            k = len(cells)
            S.back.append(frame_card(f"{s}-c{k}", x, y, CW, CH, inner, r=16, border=6))
            d = math.hypot(x + CW / 2 - 540, y + CH / 2 - 540)
            cells.append((d, k, R.u(-3, 3)))
    order = sorted(cells)
    a0 = t0 + 0.3
    for n, (d, k, tilt) in enumerate(order):
        at = a0 + n * 0.035
        sel = f"#{s}-c{k}"
        S.init(sel, {"scale": 0.2, "opacity": 0, "rotation": r3(tilt * 3), "transformOrigin": "50% 50%"})
        S.ft(sel, {"scale": 0.2, "opacity": 0, "rotation": r3(tilt * 3)}, {"scale": 1, "opacity": 1, "rotation": r3(tilt)}, at, 0.42, "back.out(1.7)")
    # the one big sentence under the chest
    S.front.append(badge(f"{s}-say", 0, 905, "Satu ide, satu dinding konten.", size=50, style="width:1080px;text-align:center"))
    S.init(f"#{s}-say", {"opacity": 0, "y": 26, "scale": 0.92, "transformOrigin": "50% 50%"})
    S.ft(f"#{s}-say", {"opacity": 0, "y": 26, "scale": 0.92}, {"opacity": 1, "y": 0, "scale": 1}, t0 + 0.95, 0.4, "power3.out")
    # slow push on the finished wall (both layers move as one world)
    S.cam([(t0, {"scale": 1}, None), (t0 + 1.2, {"scale": 1}, "none"), (t1, {"scale": 1.045}, "sine.inOut")])

    # mascot: in front of the wall, presents it, then settles
    v = dict(MED, fy=MED["fy"] + 20)
    S.mv([(t0, v, None), (t0 + 1.2, v, "none"), (t1, dict(v, fy=v["fy"] + 30, h=v["h"] * 1.04), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.3), (t0 + 0.25, "present", 0.4), (t0 + 1.6, "explain", 0.4), (t0 + 3.1, "palmUp", 0.4), (t0 + 4.2, "explain", 0.35), (t1 - 0.55, "low", 0.45)])
    S.act("armR", [(t0, "low", 0.3), (t0 + 0.3, "present", 0.4), (t0 + 1.7, "low", 0.5), (t0 + 3.3, "open", 0.4), (t0 + 4.3, "low", 0.45)])
    S.act("head", [(t0, [0, 0, 0], 0.3), (t0 + 0.3, [-0.12, 0.25, 0.02], 0.4), (t0 + 0.9, [-0.12, -0.25, -0.02], 0.45),
                   (t0 + 1.6, [0.02, 0.0, 0.04], 0.4), (t0 + 3.0, [-0.04, 0.12, -0.03], 0.5), (t0 + 4.2, [0.0, -0.06, 0.02], 0.4), (t1 - 0.5, [0, 0, 0], 0.4)])
    S.act("torso", [(t0 + 0.3, {"chest": [0.02, 0.08, 0]}, 0.5), (t0 + 1.6, {}, 0.5)])
