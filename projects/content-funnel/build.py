# Instagram content funnel (AIpreneur light, 1 slide 1080x1350). Render: node render.js
from pathlib import Path
D = Path(__file__).parent
T = [
 ("ToF", "Top of funnel", "Reach people who don’t know you yet.", "Get new followers",
  ["Carousels like this one", "Hook-first Reels", "AI tool breakdowns", "Before vs after AI", "Step-by-step tutorials", "Myth-busting posts", "Trend reactions", "Raw talking heads"]),
 ("MoF", "Middle of funnel", "Build trust and prove you know your stuff.", "Build authority",
  ["Behind the scenes", "Your real workflow", "A day in the business", "Lessons from mistakes", "Stories and polls", "Live Q&A", "Your personal story"]),
 ("BoF", "Bottom of funnel", "Turn followers into paying clients.", "Get clients",
  ["Client results", "Case studies", "How your offer works", "Testimonials", "FAQs and objections", "Why you started"]),
]
# funnel tiers (SVG): continuous funnel split into 3 bands
W, H, G, RY = 360, 252, 14, 20
xs = [(0, 360), (40, 320), (80, 280), (112, 248)]
FILL = ["url(#g0)", "url(#g1)", "url(#g2)"]
svg = '<svg class="fn" viewBox="0 -22 360 818" preserveAspectRatio="none"><defs>' \
      '<linearGradient id="g0" x1="0" x2="1"><stop offset="0" stop-color="#3f7ec4"/><stop offset="1" stop-color="#294b77"/></linearGradient>' \
      '<linearGradient id="g1" x1="0" x2="1"><stop offset="0" stop-color="#294b77"/><stop offset="1" stop-color="#1a2d57"/></linearGradient>' \
      '<linearGradient id="g2" x1="0" x2="1"><stop offset="0" stop-color="#16244d"/><stop offset="1" stop-color="#0a0d2c"/></linearGradient>' \
      '<linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".35" stop-color="#fff" stop-opacity="0"/><stop offset=".8" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".25"/></linearGradient></defs>'
for i in range(3):
    y0 = i * (H + G); y1 = y0 + H
    a0, b0 = xs[i]; a1, b1 = xs[i + 1]
    cx0, rx0 = (a0 + b0) / 2, (b0 - a0) / 2; cx1, rx1 = (a1 + b1) / 2, (b1 - a1) / 2
    body = f'M{a0} {y0} L{a1} {y1} A{rx1} {RY*rx1/rx0:.1f} 0 0 0 {b1} {y1} L{b0} {y0} Z'
    svg += f'<path d="{body}" fill="{FILL[i]}"/><path d="{body}" fill="url(#sh)"/>'
    svg += f'<ellipse cx="{cx0}" cy="{y0}" rx="{rx0}" ry="{RY}" fill="{FILL[i]}"/><ellipse cx="{cx0}" cy="{y0}" rx="{rx0-10}" ry="{RY-6}" fill="#060820" opacity=".85"/>'
svg += "</svg>"
labels = "".join(f'<div class="tl t{i}" style="top:{(i*(H+G)+H*0.45+22)/818*100:.2f}%"><b>{k}</b><span>{n}</span></div>' for i, (k, n, *_ ) in enumerate(T))
cards = "".join(f'''<div class="cd c{i}"><div class="ch"><b>{k}</b><span>Goal: {short}</span></div><p class="gl">{goal}</p>
  <ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>''' for i, (k, n, goal, short, items) in enumerate(T))
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Content Funnel</title><style>{CSS}</style></head><body>
<section class="slide">
 <div class="tp"><img class="logo" src="assets/logo_navy.png" alt="AIpreneur"></div>
 <div class="label">For AI and business creators</div>
 <h1>The Instagram<br><span>content funnel.</span></h1>
 <div class="body"><div class="fw">{svg}{labels}</div><div class="cards">{cards}</div></div>
 <div class="sv"><span class="save">Save this</span></div>
</section></body></html>''')
print("ok")
