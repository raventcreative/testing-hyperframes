# Builds carousel.html: AIpreneur remake of "64 AI Agent Use Cases" (5 slides, 1080x1350, English)
# Render: node render.js  |  Check: node check-safezone.js
from pathlib import Path

D = Path(__file__).parent


def line(body, w=1.8):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


I = {
    "arrow": line('<path d="M5 12h14M13 6l6 6-6 6"/>', 2.2),
    "check": line('<path d="m5 12.5 4.5 4.5L19 7.5"/>', 2.6),
    "mic": line('<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21"/>'),
    "mail": line('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>'),
    "doc": line('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M8.5 12.5h7M8.5 16h4.5"/>'),
    "alert": line('<path d="M12 3.5 21.5 20h-19Z"/><path d="M12 10v4.5M12 17.4v.1"/>'),
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
        f'<li><i>{n+1}</i><div><b>{t}</b><span>{d}</span></div></li>' for n, (t, d) in enumerate(items)) + '</ol>'


def usecase(num, title, lede, uses, how, example, visual, extra=""):
    return frame("uc", f'''<div class="label">Use case {num} <em>of 64</em></div>
  <h1 class="g">{title}</h1>
  <p class="lede">{lede}</p>
  <div class="sec"><h3>Use it for</h3>{uses}</div>
  <div class="sec"><h3>How it works</h3>{steps(how)}</div>
  {extra}
  <div class="ex"><div class="ex-t"><h3>Real example</h3><p>{example}</p></div><div class="ex-v">{visual}</div></div>''')


def chips(xs):
    return '<div class="chips">' + "".join(f'<span>{x}</span>' for x in xs) + '</div>'


# ---------- 1. COVER ----------
FEAT = [("45", "English → Spanish Translator"), ("47", "AI Writing Assistant"), ("49", "AI Homework Helper")]
cover = frame("cover", f'''<div class="label">Save this list</div>
  <div class="big g">64</div>
  <h1 class="g">AI Agent<br>Use Cases.</h1>
  <p class="lede">Real jobs you can hand to an AI agent today. Pick the ones your business actually needs.</p>
  <div class="inside"><h3>Inside this post</h3>
    {"".join(f'<div class="row"><em>{n}</em><b>{t}</b>{I["arrow"]}</div>' for n, t in FEAT)}
    <div class="row more"><em>+</em><b>The full list of 64</b>{I["arrow"]}</div>
  </div>''', swipe=True)

# ---------- 2. USE CASE 45 ----------
docs = f'''<div class="docs">
  <div class="dc"><span class="tg">EN</span><b>Lesson 3</b><small>Ordering at a restaurant</small><i></i><i></i><i class="s"></i></div>
  <span class="ar">{I["arrow"]}</span>
  <div class="dc es"><span class="tg">ES</span><b>Lección 3</b><small>Pedir en un restaurante</small><i></i><i></i><i class="s"></i></div>
</div>'''
uc45 = usecase(45, "English → Spanish<br>Translator.",
               "Professional translation that keeps the cultural context, not just the words.",
               '<div class="two"><div><b>Business documents</b><span>Contracts, legal and technical terms.</span></div>'
               '<div><b>Academic texts</b><span>Specialist terms kept accurate for students.</span></div></div>',
               [("Paste or upload your English text.", "Any document, any length."),
                ("It writes natural Spanish for your market.", "Layout, headings, tables, names, dates and numbers stay exactly in place."),
                ("You get the final version plus a phrase log.", "Every tricky phrase, and why it chose the formal option.")],
               "A Spanish course seller translates her whole English workbook for a new class in Mexico City. Same page design her students already know.",
               docs)

# ---------- 3. USE CASE 47 ----------
voice = f'''<div class="vn">
  <div class="vh">{I["mic"]}<span>Voice note</span><em>0:42</em></div>
  {"".join(f'<p>{I["check"]}{x}</p>' for x in ["Project goal", "What we’ll do", "Timeline", "Pricing", "Next step"])}
</div>
<div class="outs"><span>{I["mail"]}Proposal email</span><span>{I["doc"]}Blog post</span></div>'''
uc47 = usecase(47, "AI Writing Assistant.",
               "Research, draft and polish anything you write. Emails, reports, even stories.",
               chips(["Business emails", "Blog posts", "Reports", "Creative stories"]),
               [("Tell it what you need.", "Audience, tone and key points. Plain words, no template."),
                ("It researches and plans.", "Best practice for that type of writing."),
                ("You get a ready draft.", "Right structure and tone, built on current info."),
                ("Refine and reuse.", "Change the tone, add detail, or turn it into slides.")],
               "A founder who hates writing turns <b>5 rough voice-note points</b> into a client proposal and a blog post in her own tone. Edits two lines, sends both the same day.",
               voice,
               extra='<div class="tips"><p><b>Match your voice.</b> Give it a sample of your writing.</p><p><b>Need it shorter?</b> Ask for a version 30% shorter.</p></div>')

# ---------- 4. USE CASE 49 ----------
math = '''<div class="mx">
  <div class="q">3/4 + 1/6 = ?</div>
  <p><i>1</i>Common denominator: <b>12</b></p>
  <p><i>2</i>9/12 + 2/12</p>
  <p class="ok"><i>3</i>= <b>11/12</b></p>
</div>'''
uc49 = usecase(49, "AI Homework Helper.",
               "Step-by-step help across math, science, writing and more.",
               chips(["Math", "Biology", "Chemistry", "Physics", "Writing", "History", "Economics", "Computer Science"]),
               [("Ask, or upload a photo or PDF.", "Equations, formulas, graphs and diagrams all work."),
                ("It names the key concepts.", "So you know what the problem is really testing."),
                ("It breaks the problem into steps.", "Shows the working, explains the why."),
                ("It guides, not just answers.", "A check question after each step. Ask for another method or practice set.")],
               "A parent helps a stuck 12-year-old with fractions at the kitchen table. The kid finishes the page alone, then asks for the practice set.",
               math,
               extra=f'<div class="warn">{I["alert"]}<p><b>AI can be wrong.</b> Double-check with course materials, and disclose AI help if required.</p></div>')

# ---------- 5. FULL LIST + CTA ----------
ALL = ["AI video generator", "YouTube influencer finder", "AI slides generator", "Market research tool", "PDF translator",
       "AI market sizing tool", "Business strategy deck", "AI price estimator", "Business canvas maker",
       "Chrome extension builder", "Incentive tracking", "AI expansion analysis", "AI resume builder",
       "AI asset tracking system", "Competitor analysis tool", "Chief of staff", "AI timeline generator",
       "AI salary calculator", "AI budget planner", "Startup idea POC", "Reimbursement form maker",
       "AI profile builder", "AI scheduling assistant", "Billing dashboard builder", "AI document summariser",
       "AI anime generator", "AI avatar generator", "PhotoStyle insight scanner", "AI interior design",
       "Video to GIF converter", "Sketch-to-photo converter", "AI story generator", "AI sales quote generator",
       "Sales funnel builder", "Commission calculator", "Reddit sentiment analyzer", "Ad copy generator",
       "AI text generator", "YouTube viral analysis", "Marketing deck maker", "Sales territory mapping",
       "EN → Japanese translator", "Essay outline generator", "AI essay writer", "EN → Spanish translator",
       "AI math solver", "AI writing assistant", "EN → Latin translator", "AI homework helper",
       "Teacher PowerPoint maker", "Intro email generator", "Everything calculator", "Phone comparison",
       "PC parts comparison", "AI color analysis", "PC builder", "Camera comparison", "AI fitness coach",
       "Coupon finder", "AI trip planner", "AI text summarizer", "AI code generator", "AI PDF summarizer",
       "Opportunity manager"]
assert len(ALL) == 64
HL = {45, 47, 49}
items = "".join(f'<li{" class=hl" if i + 1 in HL else ""}><em>{i+1:02d}</em>{n}</li>' for i, n in enumerate(ALL))
index = frame("idx", f'''<div class="label">The full list</div>
  <h1 class="g">All 64 use cases.</h1>
  <ol class="list">{items}</ol>
  <div class="cta"><span>Comment</span><b>“LINK”</b><span>to get the full list</span></div>''')

import base64
LOGO = "data:image/png;base64," + base64.b64encode((D / "assets/logo.png").read_bytes()).decode()
CSS = (D / "style.css").read_text().replace("url(assets/logo.png)", f"url({LOGO})")
(D / "carousel.html").write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>AI Agent Use Cases</title>
<style>{CSS}</style></head><body>
{cover}
{uc45}
{uc47}
{uc49}
{index}
</body></html>''')
print("ok")
