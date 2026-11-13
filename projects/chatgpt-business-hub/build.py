# ChatGPT business profile how-to (AIpreneur navy, 5 slides). Icons: Lucide (ISC); OpenAI mark: Simple Icons (CC0).
import re
from pathlib import Path
D = Path(__file__).parent
def L(n, w=2):
    s = re.sub(r"<!--.*?-->", "", (D / f"assets/icons/{n}.svg").read_text(), flags=re.S)
    return re.sub(r'class="[^"]*"|width="24"|height="24"', "", s).replace('stroke-width="2"', f'stroke-width="{w}"')
OAI = re.search(r'd="([^"]+)"', (D / "assets/icons/openai.svg").read_text()).group(1)
def oai(c="#0a0d2c"): return f'<svg viewBox="0 0 24 24"><path fill="{c}" d="{OAI}"/></svg>'

def frame(cls, body, swipe=False):
    sw = '<div class="bot">Swipe →</div>' if swipe else ''
    return f'<section class="slide {cls}"><img class="logo" src="assets/logo_white.png" alt="AIpreneur">{body}{sw}</section>'

def step(n, title, lede, mock, note):
    return frame("st", f'''<div class="label"><b>{n:02d}</b>Step {n} of 4</div>
  <h1>{title}</h1><p class="lede">{lede}</p>
  <div class="mock">{mock}</div>
  <div class="note">{L("check", 3)}<span>{note}</span></div>''')

# COVER
cover = frame("cover", f'''<div class="brk">Breaking</div>
  <h1>ChatGPT now lets you<br><span>register your business.</span></h1>
  <p class="lede">Claim a free business profile so ChatGPT can show your brand, products and website when people ask.</p>
  <div class="scene">
    <div class="tile3">{oai("#fff")}</div>
    <div class="chat">
      <div class="q">Where can I buy good kopi susu in Jakarta?</div>
      <div class="a"><span class="av">{oai()}</span><div>
        <p>Here are a few popular spots:</p>
        <div class="biz"><div class="bl">KS</div><div><b>Kopi Senja</b><small>Coffee shop · Jakarta Selatan</small></div><span class="vb">{L("badge-check")}Verified</span></div>
        <div class="acts"><span>{L("arrow-up-right")}Website</span><span>{L("package")}Products</span></div></div></div>
    </div></div>''', swipe=True)

# STEP 1
m1 = f'''<div class="ui"><div class="uh">{L("store")}<b>Claim your business</b></div>
  <label>Business name</label><div class="in">Kopi Senja</div>
  <label>Phone number</label><div class="row"><div class="in cc">🇮🇩 +62</div><div class="in f">812 3456 7890</div><span class="ok">{L("check", 3)}</span></div>
  <label>Business email</label><div class="row"><div class="in f">halo@kopisenja.id</div><span class="ok">{L("check", 3)}</span></div>
  <div class="btn">Send verification code</div></div>'''
s1 = step(1, "Claim it, then verify<br><span>your phone + email.</span>",
  "Find your business in ChatGPT’s Business Hub and confirm you own it.", m1,
  "Use the email on your business domain, so ownership is easy to prove.")

# STEP 2
m2 = f'''<div class="ui"><div class="id">
  <div class="sh">{L("shield-check")}</div><div><b>Verify your identity with a government ID</b><small>Required before you can publish edits or see insights.</small></div></div>
  <div class="card"><div class="ph"></div><div class="ln"><i></i><i></i><i class="s"></i></div><span>ID card</span></div>
  <div class="prog"><span class="d">{L("check", 3)}Phone</span><span class="d">{L("check", 3)}Email</span><span class="n">ID check</span><span>Live</span></div></div>'''
s2 = step(2, "The step most people<br><span>skip: verify your ID.</span>",
  "This is what unlocks editing, insights and everything after it.", m2,
  "Skip this and your profile stays locked. Most people stop right here.")

# STEP 3
PR = [("Kopi Susu Gula Aren", "Rp28.000"), ("Cold Brew 1L", "Rp95.000"), ("Biji Kopi Arabika 250g", "Rp120.000")]
prods = "".join(f'<div class="pc"><div class="pi"><span></span></div><b>{a}</b><small>{b}</small></div>' for a, b in PR)
m3 = f'''<div class="ui"><div class="uh">{L("package")}<b>Bring your products into the conversation</b></div>
  <p class="ux">Your products can show up in ChatGPT answers when they match what people ask, and in your business side panel.</p>
  <div class="pg">{prods}</div></div>'''
s3 = step(3, "Then add<br><span>your products.</span>",
  "Upload your catalog so people can find what you sell, right inside the chat.", m3,
  "Write product names the way buyers search, not the way your POS labels them.")

# STEP 4
bars = "".join(f'<i style="--h:{h}%"></i>' for h in [18, 26, 22, 38, 44, 40, 58, 66, 61, 78, 84, 92])
m4 = f'''<div class="ui"><div class="kp">
  <div><small>{L("message-circle")}Mentions</small><b>128</b><em>+42% this week</em></div>
  <div><small>{L("mouse-pointer-click")}Website clicks</small><b>34</b><em>+18% this week</em></div></div>
  <div class="ch">{bars}</div><p class="ex">Example numbers. Your data appears a few days after you go live.</p></div>'''
s4 = step(4, "After a few days,<br><span>the data starts.</span>",
  "See how often ChatGPT mentions you and how many people click to your website.", m4,
  "Still in beta. A profile is free, but it doesn’t guarantee more mentions.")

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>ChatGPT Business</title><style>{CSS}</style></head><body>{cover}{s1}{s2}{s3}{s4}</body></html>')
print("ok")
