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
  <div class="robot"><img src="assets/robot.png" alt="Robot working on a laptop"></div>''', swipe=True)

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
def prompt_slide(n, t1, t2, lede, fields, prompt, extra, result, extra_first=False):
    f = "".join(f'<li><em>{i+1}</em><div><b>{a}</b><span>{b}</span></div></li>' for i, (a, b) in enumerate(fields))
    p = re.sub(r"\[([^\]]+)\]", r'<mark>[\1]</mark>', prompt).replace("\n\n", "</p><p>")
    two = f'''<div class="two">
    <div class="card fill"><h3><i>{"2" if extra_first else "1"}</i>Fill this in first</h3><ul>{f}</ul></div>
    <div class="card pr"><h3><i>{"3" if extra_first else "2"}</i>Paste into Claude</h3>
      <div class="chat"><div class="ch">{CLAUDE}<b>Claude</b><span class="cp">{I["copy"]}</span></div><p>{p}</p></div></div>
  </div>'''
    ex = f'<div class="card ex"><h3><i>{"1" if extra_first else "3"}</i>{extra[0]}</h3>{extra[1]}</div>'
    body = (ex + two) if extra_first else (two + ex)
    return frame(f"pp p{n}", f'''<div class="label">Prompt {n:02d}</div>
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

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Claude Side Hustle</title><style>{CSS}</style></head><body>
{cover}{overview}{p1}{p2}{p3}</body></html>''')
print("ok")
