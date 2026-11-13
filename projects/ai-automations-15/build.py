# 15 AI automations for small business (AIpreneur navy, 1 slide). Brand logos: Simple Icons (CC0); line icons: Lucide (ISC).
import re
from pathlib import Path
D = Path(__file__).parent
def L(n, w=2):
    s = re.sub(r"<!--.*?-->", "", (D / f"assets/icons/{n}.svg").read_text(), flags=re.S)
    return re.sub(r'class="[^"]*"|width="24"|height="24"', "", s).replace('stroke-width="2"', f'stroke-width="{w}"')
COL = {"whatsapp": "#25D366", "n8n": "#EA4B71", "claude": "#D97757", "googlesheets": "#34A853", "googledocs": "#4285F4",
       "googlecalendar": "#4285F4", "xendit": "#4573FF", "make": "#6D00CC"}
def B(n):
    if n == "apify": return '<span class="bl"><img src="assets/icons/apify.png" alt=""></span>'
    d = re.search(r'd="([^"]+)"', (D / f"assets/icons/{n}.svg").read_text()).group(1)
    return f'<span class="bl"><svg viewBox="0 0 24 24"><path fill="{COL[n]}" d="{d}"/></svg></span>'
R = [
 ("message-circle", "WhatsApp auto-reply", "Answers prices, hours and FAQs 24/7 from your own info.", ["claude", "whatsapp"], "Claude + WhatsApp Business"),
 ("phone-missed", "Missed-call text back", "Sends a WhatsApp within a minute of every missed call.", ["whatsapp", "n8n"], "WhatsApp + n8n"),
 ("filter", "Lead capture", "Every IG, website and WhatsApp enquiry lands in one sheet.", ["n8n", "googlesheets"], "n8n or Make + Sheets"),
 ("repeat", "Lead follow-ups", "Day 1, 3 and 7 follow-ups go out on their own.", ["n8n", "whatsapp"], "n8n + WhatsApp"),
 ("star", "Review requests", "Sends your Google review link after every order.", ["n8n"], "n8n"),
 ("message-square-quote", "Review replies", "Drafts a reply to every Google review for you to approve.", ["claude"], "Claude"),
 ("file-text", "Quote generator", "Fill a form, get a branded quote PDF in seconds.", ["claude", "googledocs"], "Claude + Google Docs"),
 ("receipt", "Payment reminders", "Reminds clients on the due date, then again if unpaid.", ["xendit", "n8n"], "Xendit + n8n"),
 ("calendar-clock", "Bookings + reminders", "Books slots and sends a reminder the day before.", ["googlecalendar", "whatsapp"], "Google Calendar + WhatsApp"),
 ("list-checks", "Meeting to action items", "Turns call notes into tasks, each with an owner.", ["claude"], "Claude"),
 ("images", "One photo, a week of posts", "Captions and formats from a single product photo.", ["claude"], "Claude"),
 ("radar", "Competitor tracker", "Weekly summary of what competitors posted and priced.", ["apify", "claude"], "Apify + Claude"),
 ("brain-circuit", "Team FAQ brain", "Your staff ask it, instead of asking you.", ["claude"], "Claude Projects"),
 ("chart-column", "Daily sales summary", "Yesterday’s numbers on your WhatsApp at 9am.", ["googlesheets", "n8n", "claude"], "Sheets + n8n + Claude"),
 ("book-open-check", "SOP assistant", "Answers “how do we do X here?” from your docs.", ["claude"], "Claude Projects"),
]
assert len(R) == 15
rows = "".join(f'''<div class="r{" hot" if i == 1 else ""}"><em>{i+1:02d}</em>
 <div class="au"><span class="li">{L(ic)}</span><b>{t}</b>{'<i class="tag">Most skipped</i>' if i == 1 else ''}</div>
 <p class="wd">{d}</p>
 <div class="bw"><div class="lg">{"".join(B(x) for x in bs)}</div><span>{bt}</span></div></div>''' for i, (ic, t, d, bs, bt) in enumerate(R))
PILLS = [("timer", "Save time"), ("trending-up", "More leads"), ("zap", "Runs on autopilot")]
pills = "".join(f'<span>{L(i)}{t}</span>' for i, t in PILLS)
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>15 AI Automations</title><style>{CSS}</style></head><body>
<section class="slide">
 <div class="hd"><div><img class="logo" src="assets/logo_white.png" alt="AIpreneur">
  <div class="label">The curated guide</div>
  <h1>15 AI automations <span>every small<br>business should have running.</span></h1>
  <p class="lede">No developer needed. Pick one, set it up this week.</p></div>
  <div class="pills">{pills}</div></div>
 <div class="th"><span>#</span><span>Automation</span><span>What it does</span><span>Built with</span></div>
 <div class="rows">{rows}</div>
</section></body></html>''')
print("ok")
