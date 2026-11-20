# How to make an offer people can’t refuse (AIpreneur white, 1080x1350). Render: node render.js | Check: node check-safezone.js
from pathlib import Path
D = Path(__file__).parent
CORE = [
 ("Foundation", ["Know your ideal client", "Find their biggest problem", "Define the result they want"]),
 ("Value", ["Make one clear promise", "Show the transformation", "Add bonuses that matter", "Overdeliver on the details"]),
 ("Structure", ["One simple offer", "Clear deliverables", "Price for the value", "Back it with a guarantee"]),
 ("Presentation", ["A headline that stops them", "Benefits, not features", "Answer objections early", "Create real urgency"]),
]
EXEC = [
 ("Research", ["Study the market", "Check competitors", "Position differently"]),
 ("Design", ["Define the outcome", "List deliverables", "Stack the bonuses", "Set the price"]),
 ("Message", ["Write benefit-led copy", "Show proof", "Make yes easy"]),
 ("Launch", ["Plan the launch", "Explain it clearly", "Deliver a great experience"]),
 ("Scale", ["Collect feedback", "Read the results", "Refine the offer", "Raise value and price"]),
]
def cards(items):
    out = ""
    for i, (t, li) in enumerate(items, 1):
        out += f'<div class="c"><h3><i>{i}</i>{t}</h3><ul>' + "".join(f"<li>{x}</li>" for x in li) + "</ul></div>"
    return out
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Offer People Can't Refuse</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo_navy.png" alt="AIpreneur"></div>
  <div class="label">Save this framework</div>
  <h1>How to make an offer<br>people can’t refuse.</h1>
  <div class="sec"><div class="sh">Core framework</div><div class="row r4">{cards(CORE)}</div></div>
  <div class="sec"><div class="sh">Execution system</div><div class="row r5">{cards(EXEC)}</div></div>
  <div class="ex"><small>Example (concept)</small><p><b>AI content package for a local skincare brand:</b> 30 posts + 4 reels in 14 days, Rp4.900.000, free redo if you don’t approve the first batch.</p></div>
</section></body></html>''')
print("ok")
