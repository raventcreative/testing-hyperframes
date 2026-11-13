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
    return frame("st", f'''<div class="label"><b>{n:02d}</b>Step {n} of 8</div>
  <h1>{title}</h1><p class="lede">{lede}</p>
  <div class="mock">{mock}</div>
  <div class="note">{L("check", 3)}<span>{note}</span></div>''')

# COVER
cover = frame("cover", f'''<div class="brk">Breaking</div>
  <h1>ChatGPT now lets you<br><span>register your business.</span></h1>
  <p class="lede">Claim a free business profile so ChatGPT can show your brand, products and website when people ask.</p>
  <div class="scene"><div class="app"><span class="ai">{oai()}</span><div><b>ChatGPT</b><small>Business Hub · Beta</small></div></div>
    <div class="chat"><div class="cht">{oai()}<b>ChatGPT</b></div>
      <div class="q">Can you recommend a good local coffee shop in Jakarta?</div>
      <div class="a"><span class="av">{oai()}</span><div>
        <p>Here’s one people like:</p>
        <div class="biz"><div class="bl">{L("store")}</div><div><b>Your Business</b><small>Your category · Your city</small></div><span class="vb">{L("badge-check")}Verified</span></div>
        <div class="acts"><span>{L("arrow-up-right")}Website</span><span>{L("package")}Products</span></div></div></div>
    </div></div>''', swipe=True)

# STEP 1
m1 = f'''<div class="ui"><div class="uh">{L("store")}<b>Claim your business</b></div>
  <label>Business name</label><div class="in">Your Business</div>
  <label>Phone number</label><div class="row"><div class="in cc">🇮🇩 +62</div><div class="in f">812 3456 7890</div><span class="ok">{L("check", 3)}</span></div>
  <label>Business email</label><div class="row"><div class="in f">hello@yourbusiness.com</div><span class="ok">{L("check", 3)}</span></div>
  <div class="btn">Send verification code</div></div>'''
s1 = step(5, "Verify your<br><span>phone + email.</span>",
  "A quick code to your business number and inbox confirms it’s really you.", m1,
  "Use the email on your business domain, so ownership is easy to prove.")

# STEP 2
m2 = f'''<div class="ui"><div class="id">
  <div class="sh">{L("shield-check")}</div><div><b>Verify your identity with a government ID</b><small>Required before you can publish edits or see insights.</small></div></div>
  <div class="idr"><div class="ic">{L("id-card", 1.6)}<b>Upload your ID</b><small>Photo of the front</small></div><div class="ic">{L("scan-face", 1.6)}<b>Take a selfie</b><small>To match your face</small></div></div>
  <div class="prog"><span class="d">{L("check", 3)}Phone</span><span class="d">{L("check", 3)}Email</span><span class="n">ID check</span><span>Live</span></div></div>'''
s2 = step(6, "The step most people<br><span>skip: verify your ID.</span>",
  "This is what unlocks editing, insights and everything after it.", m2,
  "Skip this and your profile stays locked. Most people stop right here.")

# STEP 3
PR = [("coffee", "Iced coffee", "Rp28.000"), ("cup-soda", "Cold brew 1L", "Rp95.000"), ("bean", "Coffee beans 250g", "Rp120.000")]
prods = "".join(f'<div class="pc"><div class="pi">{L(i, 1.6)}</div><b>{a}</b><small>{b}</small></div>' for i, a, b in PR)
m3 = f'''<div class="ui"><div class="uh">{L("package")}<b>Bring your products into the conversation</b></div>
  <p class="ux">Your products can show up in ChatGPT answers when they match what people ask, and in your business side panel.</p>
  <div class="pg">{prods}</div></div>'''
s3 = step(7, "Then add<br><span>your products.</span>",
  "Upload your catalog so people can find what you sell, right inside the chat.", m3,
  "Write product names the way buyers search, not the way your POS labels them.")

# STEP 4
bars = "".join(f'<i style="--h:{h}%"></i>' for h in [18, 26, 22, 38, 44, 40, 58, 66, 61, 78, 84, 92])
m4 = f'''<div class="ui"><div class="kp">
  <div><small>{L("message-circle")}Mentions</small><b>128</b><em>+42% this week</em></div>
  <div><small>{L("mouse-pointer-click")}Website clicks</small><b>34</b><em>+18% this week</em></div></div>
  <div class="ch">{bars}</div><p class="ex">Example numbers. Your data appears a few days after you go live.</p></div>'''
s4 = step(8, "After a few days,<br><span>the data starts.</span>",
  "See how often ChatGPT mentions you and how many people click to your website.", m4,
  "Still in beta. A profile is free, but it doesn’t guarantee more mentions.")

# NEW STEPS 1-4
m_a = f'''<div class="ui"><p class="hh">Reach new customers and grow your business with ChatGPT</p>
  <div class="srch">{L("search")}<span>your business</span><i class="caret"></i></div>
  <div class="res">
    <div class="rr add"><span>Create “your business”</span><b class="plus">{L("plus", 2.4)}</b></div>
    <div class="rr hit"><span class="ra">{L("store")}</span><div><b>Your Business</b><small>yourbusiness.com</small></div><b class="claim">Claim</b></div>
  </div></div>'''
sa = step(1, "Search your<br><span>business name.</span>",
  "Found it? Click it and claim the profile. Not listed? Hit + to create it.", m_a,
  "Search the exact name customers use, then try your website domain.")
m_b = f'''<div class="ui"><p class="hq">How do customers usually reach Your Business?</p>
  <div class="opts">
    <div class="op"><span class="oi">{L("store")}</span><div><b>At a physical location</b><small>They visit a store, café, office or other place.</small></div>{L("chevron-right")}</div>
    <div class="op sel"><span class="oi">{L("globe")}</span><div><b>Through a website</b><small>They buy on your website or a marketplace.</small></div>{L("chevron-right")}</div>
  </div></div>'''
sb = step(2, "Choose your<br><span>business type.</span>",
  "Shop, café or office? Pick physical. Selling online? Pick website.", m_b,
  "Both apply? Choose the one most of your sales come from.")
m_c = f'''<div class="ui"><p class="hq">Add your business website</p>
  <label>Website</label><div class="in focus">{L("link")}<span>yourbusiness.com</span><i class="caret"></i></div>
  <p class="hint">ChatGPT reads this site to learn what you sell.</p></div>'''
sc = step(3, "Add your<br><span>website URL.</span>",
  "This is where ChatGPT learns about you, so use your main site.", m_c,
  "Use your own domain, not a link-in-bio page.")
REC = [("Type", "TXT"), ("Name or host", "Shown in your Business Hub"), ("Value or content", "openai-verify=EXAMPLE-1234-ABCD")]
recs = "".join(f'<div class="rc"><div><small>{a}</small><b>{v}</b></div><span>{L("copy")}</span></div>' for a, v in REC)
m_d = f'''<div class="ui"><div class="uh">{L("globe")}<b>Verify that you own the website</b></div>
  <div class="dns">{recs}</div><p class="hint">Example values. Copy the real ones from your Business Hub.</p></div>'''
sd = step(4, "Prove you own<br><span>the website.</span>",
  "Add a TXT record in your domain settings, where you bought the domain.", m_d,
  "Stuck? Screenshot this screen, give it to ChatGPT and ask what to do.")

# FINAL
NEED = [("mail", "Business email or phone", "To get your verification code."), ("globe", "Your website domain", "Plus access to its DNS settings."), ("shield-check", "A government ID", "KTP or passport, plus a quick selfie."), ("package", "Your product list", "Names, prices and photos to upload.")]
need = "".join(f'<li>{L(i)}<div><b>{t}</b><small>{d}</small></div></li>' for i, t, d in NEED)
final = frame("fin", f'''<div class="label2">Ready to start?</div>
  <h1>Register your<br><span>business here.</span></h1>
  <div class="url"><span class="ai">{oai()}</span><b>chatgpt.com/business-hub</b>{L("arrow-up-right")}</div>
  <div class="need"><h3>Have these ready</h3><ul>{need}</ul></div>
  <p class="fine">Free while in beta. A profile helps ChatGPT get your details right, but it doesn’t guarantee more mentions.</p>''')

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>ChatGPT Business</title><style>{CSS}</style></head><body>{cover}{sa}{sb}{sc}{sd}{s1}{s2}{s3}{s4}{final}</body></html>')
print("ok")
