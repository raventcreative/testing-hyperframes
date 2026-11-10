# Claude Side Hustle carousel (AIpreneur, navy bg, 5 slides 1080x1350). Render: node render.js
import re
from pathlib import Path
D = Path(__file__).parent

def si(name):
    return re.search(r'd="([^"]+)"', (D / f"assets/icons/{name}.svg").read_text()).group(1)

def line(body, w=1.8):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'

I = {
 "bulb": line('<path d="M9 17.5h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1 2V17h5.2v-1.2c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>'),
 "ladder": line('<path d="M7 3v18M17 3v18M7 7h10M7 12h10M7 17h10"/>'),
 "rocket": line('<path d="M12 15.5c3.5-2 6-6 6.5-11.5-5.5.5-9.5 3-11.5 6.5z"/><path d="m7 10.5-3 1 2.5 2.5M13.5 17l-1 3-2.5-2.5"/><circle cx="14.5" cy="9.5" r="1.4"/>'),
 "play": line('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m10 9.5 4.5 2.5-4.5 2.5z"/>'),
 "check": line('<path d="m5 12.5 4.5 4.5L19 7.5"/>', 2.4),
 "list": line('<path d="M9 6h11M9 12h11M9 18h11M4.5 6h.01M4.5 12h.01M4.5 18h.01"/>', 2),
 "box": line('<path d="m12 3 8 4v10l-8 4-8-4V7z"/><path d="m4 7 8 4 8-4M12 11v10"/>'),
 "store": line('<path d="M4 9.5 5.5 4h13L20 9.5M4 9.5h16v10.5H4zM4 9.5a2.7 2.7 0 0 0 5.3 0 2.7 2.7 0 0 0 5.4 0 2.7 2.7 0 0 0 5.3 0M10 20v-5h4v5"/>'),
 "target": line('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r=".8"/>'),
 "copy": line('<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5.5A1.5 1.5 0 0 0 14.5 4h-9A1.5 1.5 0 0 0 4 5.5v9A1.5 1.5 0 0 0 5.5 16H8"/>'),
}
CLAUDE = '<img class="cl" src="assets/icons/claude.png" alt="Claude">'

def frame(cls, body, swipe=False):
    sw = '<div class="bot">Swipe →</div>' if swipe else ''
    return f'<section class="slide {cls}"><div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>{body}{sw}</section>'

# ---------- 1. COVER ----------
def tile(cls, inner, tilt):
    return f'<div class="t3 {cls}" style="--ry:{tilt}deg"><div class="face">{inner}</div></div>'
eq = (tile("cl3", f'<svg viewBox="0 0 24 24"><path fill="#fff" d="{si("claude")}"/></svg>', 14)
      + '<b class="op">+</b>' + tile("ig3", f'<svg viewBox="0 0 24 24"><path fill="#fff" d="{si("instagram")}"/></svg>', 0)
      + '<b class="op">+</b>' + tile("gr3", f'<svg viewBox="0 0 24 24"><path fill="#0b0b0b" d="{si("gumroad")}"/></svg>', -14)
      + '<b class="op">=</b><b class="money">$$</b>')
cover = frame("cover", f'''<div class="label">Claude side hustle</div>
  <h1>AI side hustle,<br><span>the smart way.</span></h1>
  <div class="eq">{eq}</div>
  <div class="eqcap"><span>Build with Claude</span><span>Sell on Instagram</span><span>Get paid on Gumroad</span></div>
''', swipe=True)

# ---------- 2. OVERVIEW ----------
OV = [("bulb", "Pick your first product"), ("ladder", "Map your offer ladder"), ("rocket", "Launch in 7 days"),
      ("play", "Turn it into a mini-course"), ("check", "Test if people will pay"), ("list", "Outline the product"),
      ("box", "Make a beginner version"), ("store", "Choose where to sell"), ("target", "Set your sales target")]
cells = "".join(f'<div class="oc{" bonus" if i >= 6 else ""}"><div class="oh"><em>{i+1:02d}</em>{"<span>Bonus</span>" if i >= 6 else ""}</div>'
                f'<div class="oi">{I[ic]}</div><b>{t}</b></div>' for i, (ic, t) in enumerate(OV))
overview = frame("ov", f'''<div class="label">Claude + side hustle</div>
  <h1><span>6 Claude prompts</span><br>to build a side hustle.</h1>
  <div class="goal"><b>Goal: Rp3 juta a day</b><span>10 sales × Rp300k, before fees. A laptop, Wi-Fi and a few hours.</span></div>
  <div class="ogrid">{cells}</div>''')

# ---------- PROMPT TEMPLATE ----------
def prompt_slide(n, t1, t2, lede, fields, prompt, extra, result, extra_first=False, label=None):
    f = "".join(f'<li><em>{i+1}</em><div><b>{a}</b><span>{b}</span></div></li>' for i, (a, b) in enumerate(fields))
    p = re.sub(r"\[([^\]]+)\]", r'<mark>[\1]</mark>', prompt).replace("\n\n", "</p><p>")
    two = f'''<div class="two">
    <div class="card fill"><h3><i>{"2" if extra_first else "1"}</i>Fill this in first</h3><ul>{f}</ul></div>
    <div class="card pr"><h3><i>{"3" if extra_first else "2"}</i>Paste into Claude</h3>
      <div class="chat"><div class="ch">{CLAUDE}<b>Claude</b><span class="cp">{I["copy"]}</span></div><p>{p}</p></div></div>
  </div>'''
    ex = f'<div class="card ex"><h3><i>{"1" if extra_first else "3"}</i>{extra[0]}</h3>{extra[1]}</div>'
    body = (ex + two) if extra_first else (two + ex)
    return frame(f"pp p{n}", f'''<div class="label">{label or f"Prompt {n:02d}"}</div>
  <h1>{t1} <span>{t2}</span></h1>
  <p class="lede">{lede}</p>
  {body}''')

p1 = prompt_slide(1, "Pick your first", "digital product.",
  "Turn a skill you already have into something people pay for.",
  [("Your skill", "What can you help people do?"), ("Your level", "Beginner, intermediate or expert."),
   ("Your buyer", "Who needs this right now?"), ("Your time", "How fast can you build it?")],
  "You're a digital product strategist. I'm good at [skill], my level is [beginner / intermediate / expert], and I want to sell to [audience].\n\nList 15 digital product ideas I could make. For each one: what it is, who pays for it, the problem it fixes, how hard it is to make, how fast I can launch, and where to sell it.\n\nSort them by fastest first sale, then by long-term potential.",
  ("Example shortlist · café social media", '''<div class="sl">
    <div class="sr"><em>1</em><b>Caption template pack</b><span>Saves 5 hours a week</span><strong>Rp99k</strong></div>
    <div class="sr"><em>2</em><b>Notion content calendar</b><span>Plans a month in one sitting</span><strong>Rp149k</strong></div>
    <div class="sr"><em>3</em><b>Reels hook swipe file</b><span>Stops the scroll in 3 seconds</span><strong>Rp79k</strong></div></div>'''),
  "Keep ideas with a clear buyer and one specific problem.")

ladder = '''<div class="ld">
  <div class="st"><em>1</em><small>Starter</small><b>Caption checklist</b><span>Rp49k</span></div><i>›</i>
  <div class="st"><em>2</em><small>Core</small><b>Template pack</b><span>Rp199k</span></div><i>›</i>
  <div class="st"><em>3</em><small>Premium</small><b>Video course</b><span>Rp990k</span></div><i>›</i>
  <div class="st hi"><em>4</em><small>Monthly</small><b>Content drop</b><span>Rp149k / mo</span></div></div>'''
p2 = prompt_slide(2, "Map your", "offer ladder.",
  "Four offers, each giving buyers a reason to take the next step.",
  [("Your skill", "What result can you deliver?"), ("Your buyer", "What does a first-time buyer need?"),
   ("Entry offer", "Which small problem can you fix first?"), ("Next step", "What will they want after that?")],
  "You're a product strategist. My skill is [skill] and my buyers are [audience].\n\nDesign a 4-step offer ladder: a starter offer, a core offer, a premium digital product and a monthly offer.\n\nFor each step, tell me what to sell, a price range, the format, who buys it, and how it leads to the next step.",
  ("Example ladder · café social media", ladder),
  "Every offer should lead buyers to the next one.", extra_first=True)

DAYS = [("Choose", "One idea"), ("Scope", "One promise"), ("Draft", "Rough version"), ("Build", "Core product"),
        ("Polish", "Fix weak spots"), ("Test", "3 real users"), ("Launch", "Post the offer")]
tl = '<div class="tl"><div class="bar"></div>' + "".join(
    f'<div class="d{" last" if i == 6 else ""}"><em>{i+1}</em><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(DAYS)) + '</div>'
p3 = prompt_slide(3, "Launch in", "7 days.",
  "Pick a product you can actually finish with the hours you have.",
  [("Your skill", "Start with something you can teach."), ("Your hours", "How many hours a day?"),
   ("Your buyer", "Who would buy version one?"), ("Your tools", "Stick to tools you already use.")],
  "I want to launch a digital product in 7 days using my skill in [skill]. I have [X] hours a day, and my buyers are [audience].\n\nGive me 7 product ideas I can actually finish. For each: a day-by-day build plan, the tools I need, a suggested price and how hard it is.\n\nThen pick the one that's fastest, simplest and most likely to get a first sale.",
  ("Follow a 7-day build plan", tl),
  "Ship the smallest version that keeps the promise.")

def rows(items):
    return '<div class="sl">' + "".join(f'<div class="sr sr3"><em>{i+1}</em><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(items)) + '</div>'

p4 = prompt_slide(4, "Turn your skill into a", "mini&#8209;course.",
  "One clear outcome, five modules, and a plan for your first 10 buyers.",
  [("Course topic", "What do you know really well?"), ("Your student", "Who needs this result?"),
   ("Test price", "Rp149k to Rp299k."), ("First buyers", "10 of them, no paid ads.")],
  "You're an instructional designer. I know [topic] well and I teach [student profile].\n\nDesign a 5-module mini-course I can test at Rp149k to Rp299k. Give me a title that hooks buyers, the main promise, what each module covers, and the worksheets or templates students get.\n\nThen give me 3 ways to land my first 10 buyers without paid ads.",
  ("Example curriculum · Reels for café owners", rows([("Why your Reels flop", "See the gap"), ("Break down 3 Reels that work", "Make it concrete"),
     ("Script with a template", "Give them a tool"), ("Shoot one at your café", "Build confidence"), ("Plan 30 days of posts", "Keep it going")])),
  "")

SC = [("Demand", "8", "Who wants it?"), ("Urgency", "7", "Why now?"), ("Ease", "9", "Can I build it?"), ("Edge", "6", "Why mine?"), ("Will pay", "8", "Real buyers?")]
score = '<div class="sc">' + "".join(f'<div class="sb"><small>{a}</small><b>{v}<i>/10</i></b><span>{c}</span></div>' for a, v, c in SC) + \
        '<div class="sb tot"><small>Total</small><b>38<i>/50</i></b><span>Test it first</span></div></div>'
p5 = prompt_slide(5, "Test if people", "will pay.",
  "Score your ideas, then check if someone actually buys.",
  [("Demand", "Who is already looking for a fix?"), ("Urgency", "Why fix it now, not later?"),
   ("Ease", "How fast can you build version one?"), ("Edge", "Why would they pick yours?")],
  "You're a market validation researcher. I want to sell a digital product based on [skill] to [audience].\n\nGive me 10 ideas and score each 1 to 10 on demand, urgency, ease to build, uniqueness and likelihood to buy. Name the top 3 to sell first and explain why.\n\nFor each finalist, suggest one quick test that proves people will pay.",
  ("Example score · Caption template pack", score), "")

p6 = prompt_slide(6, "Outline the", "product.",
  "Decide what buyers get, how they use it, and their first win.",
  [("Format", "Guide, course, template or toolkit."), ("Topic", "What does it teach or do?"),
   ("Buyer", "Who will use the finished product?"), ("Quick win", "What can they do on day one?")],
  "I want to make a [format] about [topic] for [audience].\n\nBuild the full outline: product title, the promise, sections or modules, what goes in each one, bonus ideas, quick wins, and how the final file is structured.\n\nKeep it simple and practical, so a buyer sees the value before they pay.",
  ("Example outline · Caption template pack", rows([("Start here", "First caption posted in 10 minutes"), ("30 caption templates", "Promo, story and menu posts"),
     ("Bonus: 50 hooks", "Openers that stop the scroll"), ("Posting checklist", "Run it before you hit share")])),
  "")

TOOLS = ('<div class="ld fm">'
  '<div class="st"><em>1</em><small>Google Docs</small><b>Checklist</b><span>A repeatable process</span></div>'
  '<div class="st"><em>2</em><small>Canva</small><b>Worksheet</b><span>A guided exercise</span></div>'
  '<div class="st hi"><em>3</em><small>Google Sheets</small><b>Tracker</b><span>Numbers that update</span></div></div>')
b1 = prompt_slide(7, "Make a", "beginner version.",
  "Use simple tools to build something you can finish and improve.",
  [("Google Docs", "Checklists, guides and swipe files."), ("Canva", "Worksheets and design templates."),
   ("Notion", "Planners and resource hubs."), ("Google Sheets", "Trackers and calculators.")],
  "Help me turn my skill in [skill] into digital products for [audience].\n\nSuggest 10 products that need no technical skills and can be made in Google Docs, Canva, Notion or Google Sheets.\n\nFor each one: the product name, format, price range, how to make it, and why people would buy it.",
  ("Start with a tool you already use", TOOLS), "", extra_first=True, label="Bonus 01")

b2 = prompt_slide(8, "Choose where", "to sell it.",
  "Pick a storefront by product, buyer, and how you will reach them.",
  [("Product type", "What will buyers download or open?"), ("Your buyer", "Where do they already shop?"),
   ("Your goal", "Fast setup, traffic or full control?"), ("Your country", "Can the platform pay you there?")],
  "I want to sell a digital product about [skill]. Compare Gumroad, Lynk.id, Mayar, Etsy, Shopify and my own website.\n\nMy product is [product type], my buyers are [audience], and my goal is [goal]. Compare current fees, setup time, built-in traffic and how beginner-friendly each one is. Check payouts for [country].\n\nRecommend the best fit and explain why.",
  ("Compare storefronts side by side", rows([("Fees", "Platform plus payment fees"), ("Setup", "How fast you can go live"),
     ("Traffic", "Does it bring buyers to you?"), ("Payouts", "Paid to your local bank?")])),
  "", label="Bonus 02")

MATH = ('<div class="mth">'
  '<div class="mr"><b>Rp150k <i>×</i> 20 sales</b><span>= Rp3 juta</span></div>'
  '<div class="mr on"><b>Rp300k <i>×</i> 10 sales</b><span>= Rp3 juta</span></div>'
  '<div class="mr"><b>Rp600k <i>×</i> 5 sales</b><span>= Rp3 juta</span></div>'
  '<div class="fn"><div><small>Visitors</small><b>500</b></div><i>→</i><div><small>Conversion</small><b>2%</b></div><i>→</i><div class="hi"><small>Sales</small><b>10</b></div></div>'
  '</div>')
b3 = prompt_slide(9, "Work back from your", "sales target.",
  "Pick a price, then work out the sales you need for Rp3 juta a day.",
  [("Daily target", "Rp3 juta, before fees and refunds."), ("Your price", "For example, Rp300k."),
   ("Conversion rate", "Your real rate, or a test estimate."), ("Traffic source", "Where will the right buyers find you?")],
  "My daily sales target is Rp3 juta before fees. My price is [price], my store conversion rate is [rate], and my traffic comes from [sources].\n\nWork out how many sales and visitors I need per day. Show the math and compare a few price points. If I don't have conversion data, label every assumption.\n\nSuggest one simple test to check whether people will buy.",
  ("See the math behind the target", MATH), "", extra_first=True, label="Bonus 03")

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Claude Side Hustle</title><style>{CSS}</style></head><body>
{cover}{overview}{p1}{p2}{p3}{p4}{p5}{p6}{b1}{b2}{b3}</body></html>''')
print("ok")
