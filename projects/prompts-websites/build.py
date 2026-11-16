# Viral website prompts Part 2 (AIpreneur white theme, 1080x1350). Websites are original fictional mockups.
import re
from pathlib import Path
D = Path(__file__).parent
def L(n, w=2):
    s = re.sub(r"<!--.*?-->", "", (D / f"assets/icons/{n}.svg").read_text(), flags=re.S)
    return re.sub(r'class="[^"]*"|width="24"|height="24"', "", s).replace('stroke-width="2"', f'stroke-width="{w}"')
def frame(cls, body, swipe=False, foot=True):
    sw = '<div class="bot">Swipe →</div>' if swipe else ''
    ft = f'<div class="ftr"><span class="save">{L("bookmark")}Save for later</span><span class="nx">{L("arrow-right")}</span></div>' if foot else ''
    return f'<section class="slide {cls}"><img class="logo" src="assets/logo_dark.png" alt="AIpreneur">{body}{sw}{ft}</section>'

# ---------- website mockups (original) ----------
SITES = {
"nirmala": ('''<div class="w w1"><nav><b>NIRMALA</b><i>Work</i><i>Studio</i><i>Contact</i></nav>
  <canvas class="pc" data-k="x"></canvas><span class="l">IMAGINE</span><span class="r">MANIFEST</span>
  <p class="cap">Immersive art for brands, rooms and screens.</p></div>''', "Immersive art studio"),
"kopiloka": ('''<div class="w w2"><nav><b>kopiloka</b><i>Menu</i><i>Beans</i><i>Stores</i><em>Order</em></nav>
  <h3>COFFEE<br>FOR YOUR<br><span>morning</span></h3>
  <div class="cup"><i></i></div><div class="bag"><b>kopiloka</b><small>arabika · 250 g</small></div>
  <span class="tg t1">SLOW ROAST</span><span class="tg t2">HOUSE LATTE</span></div>''', "Coffee brand"),
"retrograde": ('''<div class="w w3"><nav><b>RETROGRADE</b><i>Cases</i><i>Team</i><i>Contact</i></nav>
  <h3>WE MAKE THE PAST<br>FEEL NEW</h3>
  <div class="tv a"></div><div class="tv b"></div><div class="tv c"></div><div class="tv d"></div><div class="tv e"></div></div>''', "Creative agency"),
"teduh": ('''<div class="w w4"><nav><b>✚ Klinik Teduh</b><i>Services</i><i>Doctors</i><em>Book a visit</em></nav>
  <div class="t"><small>FAMILY HEALTH CLINIC</small><h3>Medicine that starts with understanding you</h3><p><em>Book a visit</em><span>Our services</span></p></div>
  <svg class="dna" viewBox="0 0 200 300"><path d="M60 0C160 60 40 120 140 180S40 260 120 300" /><path d="M140 0C40 60 160 120 60 180S160 260 80 300"/></svg>
  <div class="cards"><div><b>General</b><small>check-up</small></div><div><b>Lab</b><small>results in 6 h</small></div><div><b>Imaging</b><small>same day</small></div></div></div>''', "Health clinic"),
"neuron": ('''<div class="w w5"><nav><b>◆ NEURON LABS</b><i>Platform</i><i>Research</i><em>Get started</em></nav>
  <h3>Engineering<br>intelligence</h3><h4>that evolves<br>with you.</h4><canvas class="pc" data-k="head"></canvas></div>''', "AI company"),
}
P = [
 ("nirmala", "Nirmala", "A dark, cinematic studio site where thousands of glowing particles form the logo, scatter on scroll and re-form."),
 ("kopiloka", "Kopiloka", "A bold, warm coffee brand site with a floating product hero, menu in Rupiah and a roast-to-cup timeline."),
 ("retrograde", "Retrograde", "A near-black agency site with old CRT screens floating in 3D, a cases carousel and a team row."),
 ("teduh", "Klinik Teduh", "A calm mint clinic site with a line-art DNA hero, service cards, live counters and a booking form."),
 ("neuron", "Neuron Labs", "A deep-navy AI company site with a rotating point-cloud head, product cards and pricing."),
]
def pslide(i, key, name, desc):
    site, cat = SITES[key]
    return frame("ps", f'''<div class="ph"><span class="chip">Prompt {i:02d}/05</span><span class="cat">{cat}</span></div>
  <h1>{name}</h1>
  <div class="br"><div class="bb"><i></i><i></i><i></i><span>{key}.site</span></div>{site}<span class="cn">Concept site</span></div>
  <div class="pr"><div class="prh"><b>PROMPT</b><span>{L("copy")}Full prompt in your DM</span></div>
  <p>“You are an expert creative front-end developer. Build a single self-contained <code>index.html</code> for <b>{name}</b>…”</p>
  <p class="pd">{desc}</p></div>''')

cover = frame("cover", f'''<span class="chip c">Part 2</span>
  <h1 class="ch1">Viral website<br>prompts.</h1>
  <p class="tg2">5 prompts. 5 websites. Paste one into Claude tonight.</p>
  <img class="ico" src="assets/claude3d_cut.png" alt="Claude"><img class="host" src="assets/mascot_host.png" alt="">''', swipe=True, foot=False)
STEPS = [("clipboard-paste", "Copy", "Grab the full prompt from your DM."), ("wand-sparkles", "Rebuild", "Paste it into Claude. Any project, any stack."),
         ("copy", "Remix", "Swap the copy, brand, sections and motion."), ("rocket", "Ship", "A proven base. A site nobody else has.")]
st = "".join(f'<div class="sc"><span class="si">{L(ic)}</span><em>{i+1:02d}</em><div><b>{t}</b><p>{d}</p></div></div>' for i, (ic, t, d) in enumerate(STEPS))
make = frame("mk", f'''<span class="chip">How to</span><h1>Make it <span>yours.</span></h1><div class="scs">{st}</div>''')
rc = "".join(f'<div class="rr"><em>{i+1:02d}</em><b>{n}</b><span>{SITES[k][1]}</span></div>' for i, (k, n, _) in enumerate(P))
recap = frame("rc", f'''<span class="chip">Recap</span><h1>Paste one<br><span>in tonight.</span></h1><div class="rl">{rc}</div>
  <div class="dm">{L("send")}<p>Comment <b>PROMPTS</b> and I’ll DM you all five.</p></div>''')
slides = [cover] + [pslide(i + 1, *p) for i, p in enumerate(P)] + [make, recap]
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Website prompts</title><style>{CSS}</style></head><body>{"".join(slides)}<script>{(D/"particles.js").read_text()}</script></body></html>')
print("ok", len(slides))
