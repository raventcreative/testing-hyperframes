"""S08 — HEADLINE WALL. Seven papers (four newspaper cut-outs + three navy accent sticky notes) slap onto the wall
behind him — left, right and above the head — tilted 3-7 deg, popping 1.4 -> 1 with a 0.06 s stagger. All behind
the body. He opens his arms as they land, then looks around at them."""
from xk import box, r3

SERIF = "Caladea, 'Liberation Serif', 'DejaVu Serif', serif"
# (kind, x, y, w, h, rot, text)
PAPERS = [
    ("art", 300, 26, 480, 170, -3, "AI Bikin Konten 10x Lebih Cepat"),
    ("note", 40, 70, 200, 190, -7, "HOOK 3 DETIK"),
    ("art", 22, 330, 290, 300, 5, "UMKM Mulai Pakai AI untuk Marketing"),
    ("note", 850, 60, 196, 186, 6, "POSTING TIAP HARI"),
    ("art", 770, 300, 290, 290, -4, "Biaya Produksi Video Turun Drastis"),
    ("note", 40, 700, 210, 196, 4, "PAKAI AI!"),
    ("art", 800, 650, 260, 280, -6, "Kreator AI Jadi Profesi Baru"),
]


def article(w, h, text):
    lines = "".join(f'<div class="abs" style="left:18px;top:{r3(h - 26 - i * 16)}px;width:{r3((w - 36) * (0.62 if i == 0 else 1))}px;height:6px;border-radius:3px;background:rgba(10,13,44,.16)"></div>'
                    for i in range(3 if h > 200 else 2))
    big = 34 if w > 400 else 30
    return (f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;background:linear-gradient(170deg,#fffdf8 0%,#f3efe6 100%);'
            f'box-shadow:0 16px 26px -14px rgba(10,13,44,.45),0 0 0 1px rgba(10,13,44,.06)"></div>'
            f'<div class="abs" style="left:18px;top:14px;width:{w - 36}px;font:700 13px/20px Poppins;letter-spacing:.2em;color:#294B77;'
            f'border-bottom:2px solid #0A0D2C;padding-bottom:4px">BERITA BISNIS</div>'
            f'<div class="abs" style="left:18px;top:48px;width:{w - 36}px;font:700 {big}px/1.08 {SERIF};color:#0A0D2C">{text}</div>' + lines)


def note(w, h, text):
    return (f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;border-radius:6px;background:linear-gradient(150deg,#294B77 0%,#0A0D2C 100%);'
            f'box-shadow:0 16px 26px -12px rgba(10,13,44,.55)"></div>'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;display:flex;align-items:center;justify-content:center;text-align:center;'
            f'font:700 30px/1.15 Poppins;color:#fff;padding:0 16px">{text}</div>'
            f'<div class="abs" style="left:{w / 2 - 12}px;top:-8px;width:24px;height:24px;border-radius:12px;background:radial-gradient(circle at 35% 35%,#fff 0%,#c9d6ea 45%,#8fa3c2 100%);'
            f'box-shadow:0 4px 6px -2px rgba(10,13,44,.5)"></div>')


def build(S):
    s, t0 = S.id, S.t0
    S.back.append(f'<div class="abs" id="{s}-wall" style="left:0;top:0;width:1080px;height:1080px">')
    for k, (kind, x, y, w, h, rot, text) in enumerate(PAPERS):
        inner = article(w, h, text) if kind == "art" else note(w, h, text)
        tape = (f'<div class="abs" style="left:{w / 2 - 44}px;top:-14px;width:88px;height:28px;background:rgba(232,238,248,.72);'
                f'box-shadow:0 2px 4px rgba(10,13,44,.12);transform:rotate({-rot * 0.6}deg)"></div>') if kind == "art" else ""
        S.back.append(f'<div class="abs" id="{s}-p{k}" style="{box(x, y, w, h)}">{inner}{tape}</div>')
    S.back.append("</div>")
    a = t0 + 0.35
    order = [0, 1, 3, 2, 4, 5, 6]          # above the head first, then left/right pairs, then lower corners
    for n, k in enumerate(order):
        rot = PAPERS[k][5]
        b = a + n * 0.06
        S.init(f"#{s}-p{k}", {"opacity": 0, "scale": 1.4, "rotation": rot * 1.8, "transformOrigin": "50% 50%"})
        S.ft(f"#{s}-p{k}", {"opacity": 0, "scale": 1.4, "rotation": rot * 1.8}, {"opacity": 1, "scale": 1, "rotation": rot}, b, 0.24, "power3.out")
        # small settle wobble, then a slow drift so the wall stays alive
        S.ft(f"#{s}-p{k}", {"rotation": rot}, {"rotation": rot + (0.8 if n % 2 else -0.8)}, b + 0.24, 0.16, "sine.out")
        S.ft(f"#{s}-p{k}", {"rotation": rot + (0.8 if n % 2 else -0.8)}, {"rotation": rot}, b + 0.4, 0.3, "sine.inOut")
    S.init(f"#{s}-wall", {"scale": 1, "transformOrigin": "540px 500px"})
    S.ft(f"#{s}-wall", {"scale": 1}, {"scale": 1.045}, a + 0.7, S.t1 - a - 0.7, "sine.inOut")
    # mascot: medium, centred (papers frame him); opens arms on the slap, then reads around
    v = {"fx": 540, "fy": 1170, "h": 960, "yaw": 0, "pitch": 5}
    S.mv([(t0, v, None), (a + 0.4, dict(v, yaw=-3), "sine.inOut"), (S.t1, dict(v, yaw=4, h=1000, fy=1200), "sine.inOut")])
    S.act("armL", [(t0, "low", 0.01), (a - 0.05, "open", 0.25), (a + 1.4, "point", 0.35), (a + 2.8, "explain", 0.4)])
    S.act("armR", [(t0, "low", 0.01), (a - 0.05, "open", 0.25), (a + 1.4, "low", 0.4), (a + 2.8, "palmUp", 0.4)])
    S.act("head", [(t0, [0, 0, 0], 0.01), (a + 0.05, [0.06, 0, 0], 0.15), (a + 0.6, [-0.16, -0.05, 0.02], 0.4),
                   (a + 1.4, [-0.05, 0.34, -0.05], 0.4), (a + 2.3, [-0.1, -0.3, 0.05], 0.45), (a + 3.4, [0.0, 0.05, 0.03], 0.45)])
    S.act("torso", [(t0, {}, 0.01), (a + 1.4, {"chest": [0, 0.1, 0]}, 0.4), (a + 2.3, {"chest": [0, -0.1, 0]}, 0.45), (a + 3.4, {}, 0.45)])
