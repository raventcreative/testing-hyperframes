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


FEAT = [("26", "AI Anime Generator"), ("27", "AI Avatar Generator"), ("29", "AI Interior Design"),
        ("46", "AI Math Solver"), ("64", "AI Lead Management Tool")]

# ---------- 1. COVER ----------
cover = frame("cover p2", f'''<div class="label">Part 2 <em>· save this list</em></div>
  <div class="big g">64</div>
  <h1 class="g">AI Agent<br>Use Cases.</h1>
  <p class="lede">Five more jobs you can hand to an AI agent today.</p>
  <div class="inside"><h3>Inside this post</h3>
    {"".join(f'<div class="row"><em>{n}</em><b>{t}</b>{I["arrow"]}</div>' for n, t in FEAT)}
    <div class="row more"><em>+</em><b>The full list of 64</b>{I["arrow"]}</div>
  </div>''', swipe=True)

avs = f'''<div class="avs">
  <small>Before: random</small>
  <div class="row r0"><i class="a1"></i><i class="a2">~</i><i class="a3">☆</i><i class="a4">?</i></div>
  <span class="dn">{I["down"]}</span>
  <small>After: one team look</small>
  <div class="row r1"><i>AL</i><i>JT</i><i>MR</i><i>DK</i></div>
</div>'''

# ---------- 2. ANIME (26) ----------
STY = [("style_ghibli", "Ghibli-inspired"), ("style_cyber", "Cyberpunk"), ("style_shonen", "Shonen"),
       ("style_shojo", "Shojo"), ("style_retro", "Retro 90s")]
uc26 = frame("uc anime", f'''<div class="label">Use case 26 <em>of 64</em></div>
  <h1 class="g">AI Anime Generator.</h1>
  <p class="lede">Turn a text idea or a photo into anime art and characters.</p>
  <div class="hero">
    <div class="hl">
      <div class="sec"><h3>Use it for</h3>
        <div class="stack"><div><b>Custom characters</b><span>Stories, games, side projects. You set hair, outfit, expression.</span></div>
        <div><b>Photo-to-anime portraits</b><span>Avatars, profile pictures and gifts.</span></div></div></div>
      <div class="sec"><h3>How it works</h3>{steps([("Describe the scene, or upload a photo.", ""), ("Refine style, details, expression.", ""), ("Generate. Keep face, hair and outfit locked.", "")])}</div>
    </div>
    <figure class="shot"><img src="assets/examples/anime_main.jpg" alt="Anime detective example">
      <figcaption>{I["quote"]}<p>A young male detective in a trench coat and fedora, on a rain-soaked Tokyo street at night.</p></figcaption></figure>
  </div>
  <div class="sec"><h3>Styles include</h3><div class="thumbs">{"".join(f'<figure><img src="assets/examples/{f}.jpg" alt="{t}"><figcaption>{t}</figcaption></figure>' for f, t in STY)}</div></div>
  <div class="ex slim"><div class="ex-t"><h3>Real example</h3><p>An indie game dev turns his detective hero into anime key art for the Steam page, then reuses the same look in every promo post.</p></div></div>''')

# ---------- 3. AVATAR (27) ----------
AVS = [("av_real", "Realistic"), ("av_anime", "Anime"), ("av_cyber", "Cyberpunk"), ("av_fantasy", "Fantasy")]
uc27 = frame("uc avatar", f'''<div class="label">Use case 27 <em>of 64</em></div>
  <h1 class="g">AI Avatar Generator.</h1>
  <p class="lede">Turn one photo or a text prompt into avatars and profile pictures.</p>
  <div class="avrow">
    <figure class="src"><img src="assets/examples/av_selfie.jpg" alt="Selfie"><figcaption>One selfie</figcaption></figure>
    <span class="ar">{I["arrow"]}</span>
    {"".join(f'<figure><img src="assets/examples/{f}.jpg" alt="{t}"><figcaption>{t}</figcaption></figure>' for f, t in AVS)}
  </div>
  <div class="sec"><h3>Use it for</h3>{two(("Team headshots", "Matching professional headshots for the whole team. No photo shoot."), ("Game &amp; stream avatars", "Anime, cyberpunk or fantasy looks for Twitch, Discord and Steam."))}</div>
  <div class="sec"><h3>How it works</h3>{steps([("Upload a reference photo, or describe the style.", ""), ("Pick from several versions.", "Light, composition and style matched. Same person across the set."), ("Download in high resolution.", "PNG or JPEG, sized for LinkedIn, Instagram, X or Discord.")])}</div>
  <div class="ex slim"><div class="ex-t"><h3>Real example</h3><p>A small agency of 8 swaps mismatched profile pics on its website and LinkedIn for one consistent headshot style, made from one selfie each.</p></div></div>''')

# ---------- 4. INTERIOR (29) ----------
brief = '''<div class="brief">
  <div class="sh-h"><b>Carpenter brief</b><span>Spare room</span></div>
  <p><em>Style</em>Scandinavian office</p>
  <p><em>Build</em>Full-height shelving, one wall</p>
  <div class="sw"><i style="--c:#e3cfa9"></i><i style="--c:#f6f4ef"></i><i style="--c:#d9cbb4"></i><i style="--c:#4f7a4a"></i><span>Birch · white · wool · green</span></div>
</div>'''
ROOMS = [("room_before", "Before: bare spare room"), ("room_scandi", "After: Scandinavian"), ("room_industrial", "After: Industrial")]
uc29 = frame("uc interior", f'''<div class="label">Use case 29 <em>of 64</em></div>
  <h1 class="g">AI Interior Design.</h1>
  <p class="lede">Redesign a room from a photo, stage an empty space, or turn a sketch into a real interior.</p>
  <div class="rooms">{"".join(f'<figure class="{"b" if i == 0 else "a"}"><img src="assets/examples/{f}.jpg" alt="{t}"><figcaption>{t}</figcaption></figure>' for i, (f, t) in enumerate(ROOMS))}</div>
  <div class="sec"><h3>Use it for</h3>{two(("Scandinavian refresh", "Light wood, white shelving, soft textiles."), ("Industrial office", "Dark steel, walnut, warm leather."))}</div>
  <div class="sec"><h3>How it works</h3>{steps([("Upload a clear room photo, then pick a style.", ""), ("Add specific asks.", "More storage, warmer colors, swap the layout or materials."), ("Get a shopping list.", "Real furniture, cheaper swaps, and the first 3 changes to make.")])}</div>
  <div class="ex"><div class="ex-t"><h3>Real example</h3><p>A freelancer turns a bare spare room into a home office with shelving along one wall, then uses the image to brief his carpenter.</p></div><div class="ex-v">{brief}</div></div>''')

# ---------- 5. MATH (46) ----------
types = '''<div class="types">
  <div><em>Typed</em><b>3x − 7 = 14</b></div>
  <div><em>Photo</em><b>4(x + 2) = 20</b></div>
  <div><em>Handwritten</em><b class="hw">∫ 2x dx</b></div>
  <div><em>PDF</em><b>Exam p.12</b></div>
</div>'''
price = '''<div class="mx">
  <div class="q">Pricing problem</div>
  <p class="sm">Rp250,000 · 20% off · then 11% tax</p>
  <p><i>1</i>250,000 × 0.8 = 200,000</p>
  <p><i>2</i>200,000 × 1.11</p>
  <p class="ok"><i>3</i>= <b>Rp222,000</b></p>
</div>'''
uc46 = usecase(46, "AI Math Solver.",
               "Solves math step by step, with the reason behind each step.",
               types,
               steps([("Input the problem.", ""),
                      ("It analyzes and plans.", "Names the concepts, picks the best method."),
                      ("It shows clear steps.", "Right formulas, matched to your level."),
                      ("It explains and checks.", "States each rule, verifies with a second method."),
                      ("Practice and more.", "3 practice problems, easy to hard, answers hidden.")]),
               "A shop owner snaps a pricing question, follows the worked steps, and finally gets how a discount and tax stack, instead of guessing at the till.",
               price)

# ---------- 6. LEAD MANAGEMENT (64) ----------
tbl = f'''<table class="tbl">
  <thead><tr><th>Lead</th><th>Score</th><th>Priority</th><th>Next action</th></tr></thead>
  <tbody>
  <tr><td>Budi S.</td><td><b>88</b></td><td><span class="p hot">Hot</span></td><td>{I["phone"]}Test drive today</td></tr>
  <tr><td>Rina A.</td><td><b>71</b></td><td><span class="p warm">Warm</span></td><td>{I["cal"]}Follow up in 2 days</td></tr>
  <tr><td>Kevin T.</td><td><b>49</b></td><td><span class="p cold">Cold</span></td><td>{I["mail"]}Monthly promo email</td></tr>
  </tbody></table>'''
uc64 = usecase(64, "AI Lead Management Tool.",
               "Turn scattered leads into a scored, organized pipeline.",
               two(("SaaS teams", "BANT scoring, routing rules, email templates and dashboards."),
                   ("Real estate &amp; dealers", "Priority rules, follow-up timing, call scripts and KPIs.")),
               steps([("Describe your business.", "Lead sources, sales steps, team size, customers, current problems."),
                      ("It researches proven systems.", ""),
                      ("It builds your playbook.", "Scoring points, routing, nurture emails, follow-up timing."),
                      ("It maps fields to your CRM.", "Salesforce, HubSpot or Pipedrive.")]),
               "A car dealership swaps a messy WhatsApp list for lead scoring. Salespeople call the hottest test-drive requests first.",
               tbl, cls="wide lead")

# ---------- 7. FULL LIST + CTA ----------
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
<html lang="en"><head><meta charset="utf-8"><title>AI Agent Use Cases Part 2</title>
<style>{CSS}</style></head><body>
{cover}
{uc26}
{uc27}
{uc29}
{uc46}
{uc64}
{index}
</body></html>''')
print("ok")
