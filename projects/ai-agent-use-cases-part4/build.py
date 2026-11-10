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


FEAT = [("02", "YouTube Influencer Finder"), ("04", "Market Research Tool"), ("08", "Startup Idea Proof of Concept"),
        ("12", "Client Onboarding Generator"), ("13", "AI Resume Builder")]

# ---------- 1. COVER ----------
cover = frame("cover p2", f'''<div class="label">Part 4 <em>· save this list</em></div>
  <div class="big g">64</div>
  <h1 class="g">AI Agent<br>Use Cases.</h1>
  <p class="lede">Five more jobs you can hand to an AI agent today.</p>
  <div class="inside"><h3>Inside this post</h3>
    {"".join(f'<div class="row"><em>{n}</em><b>{t}</b>{I["arrow"]}</div>' for n, t in FEAT)}
    <div class="row more"><em>+</em><b>The full list of 64</b>{I["arrow"]}</div>
  </div>''', swipe=True)

# ---------- 2. YOUTUBE INFLUENCER FINDER (02) ----------
yt_tbl = '''<table class="tbl yt">
  <thead><tr><th>#</th><th>Channel</th><th>Relevant videos</th><th>Avg. views</th><th>Last upload</th></tr></thead>
  <tbody>
  <tr><td>1</td><td><b>Lidah Api Review</b></td><td>14</td><td><b>82,500</b></td><td>3 days ago</td></tr>
  <tr><td>2</td><td><b>Dapur Kos Bandung</b></td><td>11</td><td><b>64,200</b></td><td>1 week ago</td></tr>
  <tr><td>3</td><td><b>Cicip Pedas Bareng</b></td><td>9</td><td><b>51,800</b></td><td>5 days ago</td></tr>
  <tr class="more"><td>…</td><td>+ 22 more channels</td><td></td><td></td><td></td></tr>
  </tbody></table>'''
uc02 = usecase(2, "YouTube Influencer Finder.",
               "Finds YouTube creators for brand deals, fast and backed by data.",
               two(("Niche brands", "Find creators who already talk about your product and your audience."),
                   ("Agencies", "A ranked CSV of channels, ready for client outreach.")),
               steps([("It writes search terms from your product, audience and interests.", ""),
                      ("It scans up to 100 videos per term, then removes duplicates.", ""),
                      ("It checks relevance, views and upload dates.", "Inactive or off-topic channels drop out."),
                      ("You get a ranked CSV.", "Channel links, names, relevant video counts and average views.")]),
               "A local chili sauce brand finds 25 mid-size food channels that already do spicy taste tests, and starts outreach with a ranked list instead of random DMs.",
               yt_tbl, cls="wide tight-h one")

# ---------- 3. MARKET RESEARCH (04) ----------
mkt = '''<div class="mkt">
  <div class="sh-h"><b>Pastry market</b><span>Surabaya</span></div>
  <p class="mb"><span>Weekend pre-orders</span><i style="--w:92%"></i><b class="hi">Strong</b></p>
  <p class="mb"><span>Office snack boxes</span><i style="--w:70%"></i><b class="hi">Good</b></p>
  <p class="mb"><span>Weekday walk-ins</span><i class="lo" style="--w:24%"></i><b>Weak</b></p>
  <p class="fix">Action: pre-order first, storefront 3 days a week</p>
</div>'''
uc04 = usecase(4, "Market Research Tool.",
               "Give it a topic, get a full market report with data and next steps.",
               two(("Local market report", "e.g. Halal skincare demand in Indonesia."),
                   ("Regional market report", "e.g. Pet care spending across Southeast Asia.")),
               steps([("Describe the topic, the place and the time period.", "From one city to a global industry."),
                      ("It reads hundreds of sources at once.", "Social sentiment, competitor prices, rules and buying patterns."),
                      ("You get the report in one sitting.", "Key takeaways, charts and next steps. Normal research takes weeks.")]),
               "Before signing a lease, a pastry owner in Surabaya sees pre-orders are strong but weekday walk-ins are weak, so she opens pre-order first.",
               mkt, cls="wide")

# ---------- 4. STARTUP IDEA POC (08) ----------
verdict = '''<div class="vd">
  <div class="sh-h"><b>Laundry pickup app</b><span>Verdict</span></div>
  <div class="sig"><span>GO</span><span class="on">FIX</span><span>STOP</span></div>
  <p class="why">Demand is real. Building an app first is not.</p>
  <ol class="ts"><li>WhatsApp order form</li><li>30 boarding-house tenants</li><li>Track repeat orders, 14 days</li></ol>
</div>'''
uc08 = usecase(8, "Startup Idea POC.",
               "Tests a startup idea with a proof of concept before you build the full thing.",
               two(("Validation report", "Market, real buyer pain and business model. Useful for funding talks."),
                   ("Cost-benefit analysis", "Puts numbers on an investment or a strategy choice.")),
               steps([("It researches the market and the real buyer pain.", ""),
                      ("It checks top rivals and their pricing.", ""),
                      ("It builds a simple 14-day test plan.", ""),
                      ("You get a decision-ready output.", "Cost-benefit table, top 5 risks, exact test steps, and a go, fix or stop verdict.")]),
               "A laundry owner wants a pickup subscription app for students. The plan says: test with a WhatsApp form and 30 boarding-house tenants first, before paying anyone to build an app.",
               verdict, cls="wide")

# ---------- 5. CLIENT ONBOARDING (12) ----------
ob = '''<div class="ob">
  <div class="cb"><small>Before</small>
    <p class="bub">Rundown-nya kapan ya, kak?</p>
    <p class="bub r">Moodboard kirim ke mana?</p>
    <p class="bub">DP kedua tanggal berapa?</p></div>
  <div class="ca"><small>After · day 1</small>
    <p>✓ Welcome pack sent</p><p>✓ Moodboard collected</p><p>✓ Pre-wedding shoot booked</p><p>✓ Payment dates set</p></div>
</div>'''
uc12 = usecase(12, "Client Onboarding Generator.",
               "Builds a full client onboarding checklist and workflow.",
               chips(["Creative studios", "Agencies", "SaaS", "Consulting &amp; legal", "Freelancers"]),
               steps([("Describe your business, client type and goal.", ""),
                      ("It builds the full plan from best practice.", "Pre-onboarding, welcome messages, kickoff agenda, files to collect, access, timeline, training and success checks."),
                      ("Export it.", "As a document, a spreadsheet or an interactive web page.")]),
               "A wedding photo studio stops answering the same questions in scattered chats. Every couple gets one welcome pack, and the moodboard, shoot date and payment dates are set on day one.",
               ob, cls="wide one")

# ---------- 6. RESUME BUILDER (13) ----------
cv = '''<div class="cv">
  <div class="old"><small>Old resume</small><i></i><i class="s"></i><i></i><i class="s"></i></div>
  <div class="new"><small>New · Customer Success</small>
    <p>✓ Raised guest rating <b>4.3 → 4.7</b></p>
    <p>✓ Trained <b>8</b> new staff</p>
    <p>✓ Cut check-in time by <b>30%</b></p></div>
</div>'''
uc13 = usecase(13, "AI Resume Builder.",
               "Basic info in, a resume tailored to the job you want out.",
               two(("Career switch", "Turn past experience into proof for a new field."),
                   ("Senior roles", "Lead with results the hiring company actually asks for.")),
               steps([("Upload your resume, or describe your history.", "A profile link works too."),
                      ("Add the target company and job title.", "It studies what that company wants."),
                      ("It rewrites with the right skills and keywords.", "Strong bullet points with real results, delivered as a PDF.")]),
               "A hotel front-desk lead applying for a customer success role gets a resume that opens with guest ratings and staff training, the exact things the job ad asks for.",
               cv, cls="wide",
               extra='<div class="warn ok"><p><b>Only true facts.</b> It never invents jobs, dates or results.</p></div>')

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
<html lang="en"><head><meta charset="utf-8"><title>AI Agent Use Cases Part 4</title>
<style>{CSS}</style></head><body>
{cover}
{uc02}
{uc04}
{uc08}
{uc12}
{uc13}
{index}
</body></html>''')
print("ok")
