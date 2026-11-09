# Builds carousel.html (AIpreneur "AI Team" carousel, 6 slides, 1080x1350, English)
# Render: node render.js  |  Check: node check-safezone.js
import re
from pathlib import Path

D = Path(__file__).parent
TOTAL = 6


def brand(name):
    d = re.search(r'd="([^"]+)"', (D / "assets/icons" / f"{name}.svg").read_text()).group(1)
    return f'<svg viewBox="0 0 24 24"><path fill="currentColor" d="{d}"/></svg>'


def line(body, w=1.7):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


I = {
    "bolt": line('<path d="M13 2.5 4.5 13.5H12l-1 8 8.5-11H12z"/>'),
    "target": line('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><path d="M12 12 19 5M16.5 4.5 19 5l.5 2.5"/>'),
    "deal": line('<path d="m3 11 3.5-3.5 4 1.2L13 7l4.5 1.5L21 11"/><path d="m3 11 5.5 5.5a1.6 1.6 0 0 0 2.2 0l.3-.3M21 11l-6.6 6.6a1.6 1.6 0 0 1-2.2 0L8.5 14"/><path d="m10.5 8.7 3.3 3.3"/>'),
    "funnel": line('<path d="M3.5 4.5h17l-6.5 8v6l-4 2v-8z"/>'),
    "mega": line('<path d="M4 10v4a1 1 0 0 0 1 1h2l6 4V5L7 9H5a1 1 0 0 0-1 1z"/><path d="M17 9a4 4 0 0 1 0 6M19.5 6.5a7.5 7.5 0 0 1 0 11"/>'),
    "mail": line('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>'),
    "db": line('<ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"/><path d="M4.5 5.5v13c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8v-13M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8"/>'),
    "headset": line('<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/><path d="M19 19c0 1.5-1.5 2.5-4 2.5h-2"/>'),
    "chart": line('<path d="M4 20h16"/><path d="m5 15 4.5-4.5 3.5 3L19.5 7"/><path d="M15 7h4.5v4.5"/>'),
    "invoice": line('<path d="M6 2.5h12v19l-3-2-3 2-3-2-3 2z"/><path d="M9 7.5h6M9 11h6M9 14.5h3.5"/>'),
    "calendar": line('<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'),
    "gear": line('<circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M4.6 4.6l2.1 2.1M17.3 17.3l2.1 2.1M2.5 12h3M18.5 12h3M4.6 19.4l2.1-2.1M17.3 6.7l2.1-2.1"/>'),
    "cv": line('<rect x="4" y="3" width="16" height="18" rx="2.5"/><circle cx="12" cy="9.5" r="2.6"/><path d="M7.5 17c.6-2.2 2.4-3.3 4.5-3.3s3.9 1.1 4.5 3.3"/>'),
    "check": line('<path d="m5 12.5 4.5 4.5L19 7.5"/>', 2.4),
    "plus": line('<path d="M12 5v14M5 12h14"/>', 2),
    "arrow": line('<path d="M12 19V5M6 11l6-6 6 6"/>', 2.4),
}


def frame(n, cls, body, swipe=False):
    foot = '<div class="bot">Swipe →</div>' if swipe else ''
    return f'''<section class="slide {cls}">
  <div class="top"><img class="logo-a" src="assets/logo.png" alt="AIpreneur"></div>
  {body}
  {foot}
</section>'''


def head(label, title, sub=""):
    s = f'<p class="sub">{sub}</p>' if sub else ""
    return f'<div class="label">{label}</div><h1>{title}</h1>{s}'


# ---------- 1. COVER ----------
DIVS = [("09", "Social Media"), ("06", "Business Growth"), ("02", "Sales &amp; Comms"), ("04", "Finance &amp; Ops")]
cover = frame(1, "cover", swipe=True, body=f'''{head("Claude for Business", 'Your Complete<br><span class="c">AI Team.</span>', "21 roles. 4 divisions. One goal: grow your business.")}
  <div class="org">
    <div class="root">Claude</div>
    <svg class="wires" viewBox="0 0 860 70"><path d="M430 0V35M100 70V47a12 12 0 0 1 12-12h636a12 12 0 0 1 12 12v23M320 35v35M540 35v35"/></svg>
    <div class="divs">{"".join(f'<div class="div"><b>{n}</b><span>{t}</span><i>roles</i></div>' for n, t in DIVS)}</div>
  </div>''')

# ---------- 2. SOCIAL MEDIA ----------
SOC = [("youtube", "Channel Growth", "YouTube"),
       ("instagram", "Social Media Manager", "Instagram"),
       ("youtube", "Viral Scripts &amp; SEO", "YouTube"),
       ("tiktok", "Content Repurposing", "TikTok"),
       ("facebook", "Organic Growth", "Facebook"),
       ("instagram", "Instagram Growth", "Instagram"),
       ("linkedin", "LinkedIn Growth", "LinkedIn"),
       ("x", "X / Twitter Growth", "X"),
       ("bolt", "Viral Hooks", "All platforms")]
rows = "".join(
    f'<li><em>{i+1:02d}</em><span class="lg">{I[ic] if ic in I else brand(ic)}</span><b>{t}</b><small>{p}</small></li>'
    for i, (ic, t, p) in enumerate(SOC))
social = frame(2, "team social", f'''{head("Division 01 &nbsp;·&nbsp; 9 roles", 'Social Media<br><span class="c">Growth Team.</span>', "Build your audience. Grow your reach. Get noticed.")}
  <ul class="table">{rows}</ul>''')

# ---------- 3. BUSINESS GROWTH ----------
BIZ = [("target", "Business Offers", "Offers people find hard to refuse."),
       ("deal", "Sales Negotiation", "Handle objections. Close with confidence."),
       ("funnel", "Sales Funnels", "From first click to paying customer."),
       ("mega", "Branding", "Positioning, voice and identity."),
       ("mail", "Email List Growth", "Build it, nurture it, sell to it."),
       ("db", "CRM &amp; Systems", "Clean customer data. Clear SOPs.")]
cells = "".join(f'<div class="cell"><div class="r"><em>{i+1:02d}</em>{I[ic]}</div><b>{t}</b><span>{d}</span></div>'
                for i, (ic, t, d) in enumerate(BIZ))
business = frame(3, "team biz", f'''{head("Division 02 &nbsp;·&nbsp; 6 roles", 'Business<br><span class="c">Growth Team.</span>', "Stronger offers, sharper brand, sales systems that run.")}
  <div class="grid6">{cells}</div>''')


# ---------- 4. SALES & COMMUNICATION ----------
def advisor(ic, t, d, tasks):
    li = "".join(f'<li>{I["check"]}{x}</li>' for x in tasks)
    return f'<div class="adv"><div class="ring">{I[ic]}</div><b>{t}</b><p>{d}</p><ul>{li}</ul></div>'


STEPS = ["New lead", "Fast reply", "Follow-up", "Closed"]
steps = "".join(f'<div class="st{" on" if i == 3 else ""}"><i>{I["check"] if i == 3 else i+1}</i><span>{s}</span></div>'
                for i, s in enumerate(STEPS))
sales = frame(4, "team sales", f'''{head("Division 03 &nbsp;·&nbsp; 2 roles", 'Sales &amp;<br><span class="c">Communication Team.</span>', "Turn conversations into clients.")}
  <div class="pair">
    {advisor("headset", "Client Advisor", "Client guidance and relationship management.", ["Replies in minutes", "Answers every question", "Keeps clients coming back"])}
    {advisor("chart", "Sales Advisor", "Sales support and deal progression.", ["Qualifies every lead", "Follows up on time", "Moves deals to close"])}
  </div>
  <div class="steps"><div class="track"></div>{steps}</div>''')

# ---------- 5. FINANCE & OPS ----------
FIN = [("invoice", "Invoicing Specialist", "Invoices and payment records."),
       ("calendar", "Management Assistant", "Admin, scheduling and documents."),
       ("gear", "Business Operations", "Day-to-day business assistance."),
       ("cv", "Hiring Assistant", "CVs, resumes and job applications.")]
fcards = "".join(f'<div class="fc"><div class="fi">{I[ic]}</div><b>{t}</b><span>{d}</span></div>' for ic, t, d in FIN)
finance = frame(5, "team fin", f'''{head("Division 04 &nbsp;·&nbsp; 4 roles", 'Finance &amp;<br><span class="c">Operations Team.</span>', "Keep operations organized, so you can focus on selling.")}
  <div class="grid4">{fcards}</div>''')

# ---------- 6. CTA ----------
CMDS = [("/seo-expert", "Audit and fix your website SEO", True),
        ("/viral-hooks", "Hooks for your next 10 posts", False),
        ("/sales-funnel", "Map the path from lead to sale", False)]
menu = "".join(f'<div class="cmd{" sel" if s else ""}"><code>{c}</code><span>{d}</span></div>' for c, d, s in CMDS)
cta = frame(6, "cta", f'''{head("One team. One goal.", 'Every role is one<br><span class="c">command</span> away.')}
  <div class="ui">
    <div class="menu">{menu}</div>
    <div class="input">
      <p><code>/seo-expert</code> Audit my whole site and tell me exactly what to fix to grow traffic. Site: yourbrand.com<i class="caret"></i></p>
      <div class="bar"><span class="pl">{I["plus"]}</span><span class="send">{I["arrow"]}</span></div>
    </div>
  </div>
  <div class="ask">
    <span class="cm">Comment</span>
    <div class="kw">“AI TEAM”</div>
    <span class="cm2">and I’ll send you the full team.</span>
  </div>''')

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>AI Team Carousel</title>
<style>{CSS}</style></head><body>
{cover}
{social}
{business}
{sales}
{finance}
{cta}
</body></html>''')
print("ok")
