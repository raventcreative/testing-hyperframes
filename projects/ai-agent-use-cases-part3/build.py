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


FEAT = [("14", "AI Asset Tracking System"), ("15", "Competitor Analysis Tool"), ("19", "AI Budget Tracker"),
        ("20", "GitHub Deployment Tool"), ("50", "Training Deck Maker")]

# ---------- 1. COVER ----------
cover = frame("cover p2", f'''<div class="label">Part 3 <em>· save this list</em></div>
  <div class="big g">64</div>
  <h1 class="g">AI Agent<br>Use Cases.</h1>
  <p class="lede">Five more jobs you can hand to an AI agent today.</p>
  <div class="inside"><h3>Inside this post</h3>
    {"".join(f'<div class="row"><em>{n}</em><b>{t}</b>{I["arrow"]}</div>' for n, t in FEAT)}
    <div class="row more"><em>+</em><b>The full list of 64</b>{I["arrow"]}</div>
  </div>''', swipe=True)

# ---------- 2. ASSET TRACKING (14) ----------
assets_tbl = '''<table class="tbl">
  <thead><tr><th>Item</th><th>ID</th><th>Holder</th><th>Where</th><th>Status</th></tr></thead>
  <tbody>
  <tr><td><b>Sony FX3</b></td><td>CAM-07</td><td>Dimas</td><td>Bali shoot</td><td><span class="p warm">Out · back 14 Dec</span></td></tr>
  <tr><td><b>Aputure 600D</b></td><td>LGT-12</td><td>Sari</td><td>Studio JKT</td><td><span class="p ok">Available</span></td></tr>
  <tr><td><b>DJI Mavic 3</b></td><td>DRN-02</td><td>Yoga</td><td>Service</td><td><span class="p hot">Repair · 20 Dec</span></td></tr>
  <tr><td><b>Rode Wireless</b></td><td>AUD-05</td><td>Fikri</td><td>Bandung</td><td><span class="p warm">Out · back 12 Dec</span></td></tr>
  </tbody></table>'''
uc14 = usecase(14, "AI Asset Tracking System.",
               "Track what you own, where it is, and who has it.",
               two(("IT tracking", "Laptops, phones and software licences. Assignment, value drop, repair history."),
                   ("Field equipment", "Gear across sites and shoots. Location, usage logs, repair alerts.")),
               steps([("Describe your assets, or upload your spreadsheet.", "XLSX or CSV is fine."),
                      ("It designs the database and the app, then loads your data.", ""),
                      ("You get a live system on any device.", "Update it, pull reports, add new fields later by chat.")]),
               "A wedding production team with gear across 3 cities stops losing lenses and mics. Every item shows its shoot, its holder and its return date in one live list.",
               assets_tbl, cls="wide tight-h one")

# ---------- 3. COMPETITOR ANALYSIS (15) ----------
cmp_tbl = '''<table class="tbl cmp">
  <thead><tr><th></th><th class="you">You</th><th>Rival A</th><th>Rival B</th><th>Rival C</th></tr></thead>
  <tbody>
  <tr><td>Price / month</td><td class="you">Rp189k</td><td>Rp159k</td><td>Rp210k</td><td>Rp175k</td></tr>
  <tr><td>Free trial</td><td class="you">–</td><td>✓</td><td>–</td><td>✓</td></tr>
  <tr><td>Roast to door</td><td class="you"><b>3 days</b></td><td>7 days</td><td>5 days</td><td>10 days</td></tr>
  <tr><td>Rating</td><td class="you">4.6</td><td>4.8</td><td>4.2</td><td>4.4</td></tr>
  </tbody></table>'''
uc15 = usecase(15, "Competitor Analysis Tool.",
               "Compares you with your rivals, then turns the gaps into clear actions.",
               chips(["Market landscape", "Price &amp; package checks", "Feature gap maps", "Message reviews", "Board-ready reports"]),
               steps([("Paste your site and 3 competitor links.", ""),
                      ("It compares everything that sells.", "Pricing, free offer, features, target buyer, headline, proof and CTA."),
                      ("You get clear results.", "Comparison tables, SWOT, positioning notes, feature gaps. Save it and re-run on a schedule.")]),
               "A coffee roastery runs this every month. Every rival fights on price, none promise beans roasted 3 days before delivery, so freshness becomes the headline offer.",
               cmp_tbl, cls="wide tight-h one")

# ---------- 4. BUDGET TRACKER (19) ----------
budget = '''<div class="bud">
  <div class="sh-h"><b>Monthly plan</b><span>Income Rp8.0M</span></div>
  <div class="bar"><i class="n" style="width:50%">Needs 50%</i><i class="w" style="width:30%">Wants 30%</i><i class="s" style="width:20%">Save 20%</i></div>
  <p class="leak"><span>Ride-hailing</span><b>Rp650k</b></p>
  <p class="leak"><span>Late-night snacks</span><b>Rp550k</b></p>
  <p class="fix">New limit: Wants Rp2.4M · Save Rp1.6M</p>
</div>'''
uc19 = usecase(19, "AI Budget Tracker.",
               "Reads your spending, sorts it, and builds a personal budget plan you can follow.",
               two(("Personal budgets", "Money tracking from real bank and e-wallet transactions."),
                   ("Freelancer cash flow", "Split business and personal spending, plan for tax.")),
               steps([("Upload statements, or describe income and spending.", ""),
                      ("It sorts every transaction.", "Finds repeat bills, subscriptions and money leaks."),
                      ("It checks your pattern.", "Against simple rules like 50/30/20."),
                      ("You get a plan.", "Limits per category, savings target, charts and alerts. Export to a spreadsheet.")]),
               "A first-jobber in Jakarta uploads 2 months of e-wallet history, finds <b>Rp1.2M a month</b> going to ride-hailing and late-night snacks, and leaves with limits she can actually follow.",
               budget)

# ---------- 5. GITHUB DEPLOY (20) ----------
term = '''<div class="term">
  <div class="tt"><i></i><i></i><i></i><span>deploy</span></div>
  <p class="cmd">› launch repo: appointment-app</p>
  <p class="okk">✓ Dependencies installed</p>
  <p class="okk">✓ Build passed</p>
  <p class="okk">✓ Tests 24/24</p>
  <p class="live">● Live: your-clinic.app</p>
</div>'''
uc20 = usecase(20, "GitHub Deployment Tool.",
               "Launches any GitHub project from its link, or finds the right one from your idea.",
               two(("Internal tools", "An open-source invoice or booking app, running for your team."),
                   ("Campaign sites", "A website template live for your next launch.")),
               steps([("Paste a repo link, or describe what you need.", "It finds matching projects."),
                      ("It sets up, installs and builds.", "Dependencies, build and tests handled. No Docker, no server work."),
                      ("You get a live link.", "Plus what it does, what it needs, and any cost or account it depends on.")]),
               "A clinic owner finds an open-source appointment app on GitHub and has a live version for her front desk to test the same afternoon.",
               term,
               extra=chips(["JavaScript", "Python", "React", "Vue", "Static sites"], "Supports"))

# ---------- 6. TRAINING DECK (50) ----------
deck = '''<div class="deck">
  <div class="sl main"><small>Module 1</small><b>Service Recovery 101</b></div>
  <div class="row2">
    <div class="sl"><small>Scenario</small><b>“My latte is wrong.”</b></div>
    <div class="sl"><small>Quick check</small><b>What do you say first?</b></div>
  </div>
  <p class="nt">Speaker notes · 2 min · role-play in pairs</p>
</div>'''
uc50 = usecase(50, "Training Deck Maker.",
               "Builds training decks with researched content, speaker notes and clean slides.",
               two(("Customer service training", "Retail and F&amp;B teams. Real scenarios and quick quizzes."),
                   ("Sales onboarding", "Product knowledge, objection handling and a 30-60-90 plan.")),
               steps([("Tell it the basics.", "Training goal, audience, learning goals and rules to cover."),
                      ("It builds the training.", "Researches best practice, makes modules with examples and checks."),
                      ("You get a ready-to-teach deck.", "Speaker notes, timing and tips on every slide. Export to PowerPoint, PDF or web.")]),
               "A café chain’s ops manager builds a service recovery training for new baristas, with real complaint scenarios and a 5-question quiz, ready before Monday’s onboarding.",
               deck)

# ---------- 7. FULL LIST + CTA ----------
ALL = ["AI video generator", "YouTube influencer finder", "AI slides generator", "Market research tool", "PDF translator",
       "AI market sizing tool", "Business strategy deck", "AI price estimator", "Business canvas maker",
       "Chrome extension builder", "Incentive tracking", "AI expansion analysis", "AI resume builder",
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
<html lang="en"><head><meta charset="utf-8"><title>AI Agent Use Cases Part 3</title>
<style>{CSS}</style></head><body>
{cover}
{uc14}
{uc15}
{uc19}
{uc20}
{uc50}
{index}
</body></html>''')
print("ok")
