# Builds carousel.html: AIpreneur remake "64 AI Agent Use Cases" Part 2 (7 slides, 1080x1350, English)
# Render: node render.js  |  Check: node check-safezone.js
import base64
from pathlib import Path

D = Path(__file__).parent


def line(body, w=1.8):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


I = {
    "arrow": line('<path d="M5 12h14M13 6l6 6-6 6"/>', 2.2),
    "down": line('<path d="M12 5v14M6 13l6 6 6-6"/>', 2.2),
    "check": line('<path d="m5 12.5 4.5 4.5L19 7.5"/>', 2.6),
    "lock": line('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'),
    "quote": '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M4 18v-5.5C4 8.4 6.2 6 9.8 5.5l.6 1.9C8.3 8 7.4 9.4 7.3 11H10v7zm10 0v-5.5c0-4.1 2.2-6.5 5.8-7l.6 1.9c-2.1.6-3 2-3.1 3.6H20v7z"/></svg>',
    "phone": line('<path d="M6.5 3.5h3l1.5 4-2 1.3a11 11 0 0 0 5.2 5.2l1.3-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2z"/>'),
    "cal": line('<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'),
    "mail": line('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>'),
}


def frame(cls, body, swipe=False):
    foot = '<div class="bot">Swipe →</div>' if swipe else ''
    return f'''<section class="slide {cls}">
  <div class="top"><div class="logo" role="img" aria-label="AIpreneur"></div></div>
  {body}
  {foot}
</section>'''


def steps(items):
    return '<ol class="steps">' + "".join(
        f'<li><i>{n+1}</i><div><b>{t}</b>{f"<span>{d}</span>" if d else ""}</div></li>' for n, (t, d) in enumerate(items)) + '</ol>'


def chips(xs, label=""):
    lab = f'<em>{label}</em>' if label else ""
    return f'<div class="chips">{lab}' + "".join(f'<span>{x}</span>' for x in xs) + '</div>'


def two(a, b):
    return ('<div class="two">' + "".join(f'<div><b>{t}</b><span>{d}</span></div>' for t, d in (a, b)) + '</div>')


def usecase(num, title, lede, uses, how, example, visual, extra="", cls=""):
    return frame(f"uc {cls}", f'''<div class="label">Use case {num} <em>of 64</em></div>
  <h1 class="g">{title}</h1>
  <p class="lede">{lede}</p>
  <div class="sec"><h3>Use it for</h3>{uses}</div>
  <div class="sec"><h3>How it works</h3>{how}</div>
  {extra}
  <div class="ex"><div class="ex-t"><h3>Real example</h3><p>{example}</p></div><div class="ex-v">{visual}</div></div>''')


FEAT = [("03", "AI Slides Generator")]

# ---------- 1. COVER ----------
cover = frame("cover p2", f'''<div class="label">Part 5 <em>· save this list</em></div>
  <div class="big g">64</div>
  <h1 class="g">AI Agent<br>Use Cases.</h1>
  <p class="lede">The last one: the job that saves your nights before every meeting.</p>
  <div class="inside"><h3>Inside this post</h3>
    {"".join(f'<div class="row"><em>{n}</em><b>{t}</b>{I["arrow"]}</div>' for n, t in FEAT)}
    <div class="row more"><em>+</em><b>The full list of 64</b>{I["arrow"]}</div>
  </div>''', swipe=True)

# ---------- 2. AI SLIDES GENERATOR (03) ----------
def mini(tag, title, sub, art):
    return f'<div class="ms"><div class="rail"><i></i><i></i><i></i></div><div class="cv2"><small>{tag}</small><b>{title}</b><span>{sub}</span>{art}</div></div>'

BARS = '<div class="art bars"><i style="--h:40%"></i><i style="--h:58%"></i><i style="--h:52%"></i><i style="--h:80%"></i><i style="--h:96%"></i></div>'
PIE = '<div class="art pie"></div>'
LINES = '<div class="art lines"><i></i><i></i><i class="s"></i></div>'
uses = '<div class="decks">' + mini("Pitch", "Seed Pitch Deck", "Problem · Market · Traction", BARS) + mini("Recap", "Content Recap", "Reels, reach &amp; next tests", PIE) + mini("Class", "Intro to Batik", "History, motifs &amp; regions", LINES) + '</div>'

deck = f'''<div class="dk">
  <div class="thumbs2"><div class="t on"></div><div class="t"></div><div class="t"></div><div class="t"></div></div>
  <div class="dkbig">
    <small>Monthly review · 8 slides</small>
    <b>October Outlet Review</b>
    <span>Sales, best sellers &amp; next month’s target</span>
    <div class="art bars lg"><i style="--h:46%"></i><i style="--h:62%"></i><i style="--h:55%"></i><i style="--h:74%"></i><i style="--h:90%"></i><i style="--h:84%"></i></div>
    <p class="nt">Speaker notes on every slide</p>
  </div>
</div>
<div class="exp"><span>PowerPoint</span><span>Google Slides</span><span>PDF</span></div>'''
uc03 = usecase(3, "AI Slides Generator.",
               "Turns any idea into a clean, editable presentation deck.",
               uses,
               steps([("Tell it your subject: a topic, rough notes or raw numbers.", ""),
                      ("It researches the topic and finds the usual structure.", ""),
                      ("It builds the deck: charts, layouts and speaker notes.", ""),
                      ("Export to PowerPoint, Google Slides or PDF.", "")]),
               "A coffee franchise owner types in last month’s numbers for 6 outlets and walks into Monday’s partner meeting with a clean 8-slide review, not a midnight slide marathon.",
               deck, cls="wide")

# ---------- 7. FULL LIST + CTA ----------
ALL = ["AI video generator", "YouTube influencer finder", "AI slides generator", "Market research tool", "PDF translator",
       "AI market sizing tool", "Business strategy deck", "Startup idea POC", "Business canvas maker",
       "Chrome extension builder", "Incentive tracking", "Client onboarding generator", "AI resume builder",
       "AI asset tracking system", "Competitor analysis tool", "Chief of staff", "AI timeline generator",
       "AI salary calculator", "AI budget tracker", "GitHub deployment tool", "Reimbursement form maker",
       "AI profile builder", "AI scheduling assistant", "Billing dashboard builder", "AI document summariser",
       "AI anime generator", "AI avatar generator", "PhotoStyle insight scanner", "AI interior design",
       "Video to GIF converter", "Sketch-to-photo converter", "AI story generator", "AI sales quote generator",
       "Sales funnel builder", "Commission calculator", "Reddit sentiment analyzer", "Ad copy generator",
       "AI text generator", "YouTube viral analysis", "Marketing deck maker", "Sales territory mapping",
       "EN → Japanese translator", "Essay outline generator", "AI essay writer", "EN → Spanish translator",
       "AI math solver", "AI writing assistant", "EN → Latin translator", "AI homework helper",
       "Training deck maker", "Intro email generator", "Everything calculator", "Phone comparison",
       "PC parts comparison", "AI color analysis", "PC builder", "Camera comparison", "AI fitness coach",
       "Coupon finder", "AI trip planner", "AI text summarizer", "AI code generator", "AI PDF summarizer",
       "AI lead management tool"]
assert len(ALL) == 64
HL = {int(n) for n, _ in FEAT}
items = "".join(f'<li{" class=hl" if i + 1 in HL else ""}><em>{i+1:02d}</em>{n}</li>' for i, n in enumerate(ALL))
index = frame("idx", f'''<div class="label">The full list</div>
  <h1 class="g">All 64 use cases.</h1>
  <ol class="list">{items}</ol>
  <div class="cta"><span>Comment</span><b>“LINK”</b><span>to get the full list</span></div>''')

LOGO = "data:image/png;base64," + base64.b64encode((D / "assets/logo.png").read_bytes()).decode()
CSS = (D / "style.css").read_text().replace("url(assets/logo.png)", f"url({LOGO})")
(D / "carousel.html").write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>AI Agent Use Cases Part 5</title>
<style>{CSS}</style></head><body>
{cover}
{uc03}
{index}
</body></html>''')
print("ok")
