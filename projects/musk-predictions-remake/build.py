# Elon Musk's predictions for the next 10 years: AIpreneur navy remake (5 slides, 1080x1350).
# Only claims Musk actually made, with when/where he said them. Real CC-licensed photos (credits on-slide + production/asset_credits.json).
from pathlib import Path
D = Path(__file__).parent
def ph(f, credit, st="", pos="center"): return f'<div class="ph" style="{st}"><img src="assets/photos/{f}.jpg" style="object-position:{pos}"><span class="cr">{credit}</span></div>'
def frame(body, swipe=False):
    sw = '<div class="swipe">Swipe →</div>' if swipe else ''
    return f'<section class="slide"><div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>{body}{sw}</section>'
def item(yr, tag, claim, quote, src):
    t = f'<small>{tag}</small>' if tag else ''
    return f'<div class="it"><div class="yr">{yr}{t}</div><div class="cl">{claim}</div><div class="q">{quote}</div><div class="src">{src}</div></div>'
def tl(rows): return frame('<div class="tl2">' + "".join(f'<div class="rw"><div class="items">{it}</div>{p}</div>' for it, p in rows) + '</div>')

S = []
S.append(frame(
  ph("2c9d1b69", "Photo: Daniel Oberhaus · CC BY 2.0", "height:600px", "center 20%")
  + '<h1>Elon Musk’s predictions<br>for the <span class="ac">next 10 years.</span></h1>'
  + '<p class="tg">What he actually said, when he said it,<br>and what it means for your business.</p>', swipe=True))
S.append(tl([
  (item("2026", "→ 2027", "AI smarter than any single human.", "“We may have AI smarter than any human by the end of this year… definitely by next year.”", "World Economic Forum, Davos · Jan 2026"),
   ph("7db7576d", "Photo: NeoSpire · CC BY 2.0")),
  (item("~2029", "", "Optimus robots outperform the best human surgeons.", "“Three years. And by the way, that’s three years at scale.”", "Moonshots podcast with Peter Diamandis · Jan 2026"),
   ph("484ffb80", "Photo: DoD News · Public domain", "", "62% center")),
]))
S.append(tl([
  (item("2030", "", "AI smarter than all of humanity combined.", "“By 2030, AI will likely be smarter than all of humanity combined.”", "World Economic Forum, Davos · Jan 2026"),
   ph("7a8906c5", "Photo: Steve Jurvetson · CC BY 2.0", "", "70% center")),
  (item("~2036", "", "1 billion+ humanoid robots, more productive than all humans.", "“Ten years from now, I would say there are well over a billion humanoid robots.”", "Musk interview · Sept 2026"),
   ph("e1fc69fb", "Tesla Optimus · Photo: Steve Jurvetson · CC BY 2.0", "", "center 28%")),
]))
S.append(tl([
  (item("2035", "→ 2045", "Work becomes optional.", "“In 10 to 20 years, work will be optional.” Like a hobby: you do it because you want to.", "U.S.–Saudi Investment Forum · Nov 2025"),
   ph("fbc72d12", "Photo: Rawpixel · CC0", "", "center")),
  (item("Later", "", "Universal high income. No need to save for retirement.", "Not universal basic income, but universal high income, because goods and services become abundant.", "VivaTech 2024 · repeated on X, 2025"),
   ph("0c95b586", "Photo: StockSnap · CC0", "", "78% center")),
]))
S.append(frame(
  '<h2>Reality check:<br><span class="ac">his dates keep moving.</span></h2>'
  + '<div class="cards">'
  + '<div class="cd"><b>AI smarter than any human</b><p>In 2024 he said 2025. Then 2026. At Davos 2026: end of 2026, “definitely” 2027.</p></div>'
  + '<div class="cd"><b>Robot surgeons</b><p>In 2025 he said about 5 years. In January 2026: 3 years.</p></div>'
  + '<div class="cd"><b>Experts</b><p>Many economists and doctors call these timelines too optimistic. The direction is real. The dates are a guess.</p></div>'
  + '</div>'
  + '<div class="take"><p><b>What this means for you:</b> don’t wait for 2030 to start. The business owners who learn to work with AI <b>now</b> get the advantage first, whatever year Musk turns out to be right.</p></div>'))

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Musk Predictions</title><style>{CSS}</style></head><body>{"".join(S)}</body></html>')
print("ok", len(S))
