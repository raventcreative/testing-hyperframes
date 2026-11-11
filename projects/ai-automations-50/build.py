# 50 AI automations you can build & sell (AIpreneur light, 1080x1350). Render: node render.js
from pathlib import Path
D = Path(__file__).parent
def ic(b): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{b}</svg>'
G = [
 ("Sales & leads", ic('<path d="M4 20V10M10 20V6M16 20v-8M20 4l-4 4-3-2-5 5"/>'),
  ["Lead qualification", "Appointment booking", "Follow-up sequences", "Proposal generator", "CRM updater",
   "Pipeline tracker", "Sales assistant", "Upsell recommender", "Churn alerts", "Client message hub"]),
 ("Customer service", ic('<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/>'),
  ["Email auto-reply", "Customer onboarding", "Ticket triage", "Help center assistant", "Review manager",
   "Feedback analyzer", "Survey automation", "Voice assistant"]),
 ("Marketing", ic('<path d="M4 10v4a1 1 0 0 0 1 1h2l6 4V5L7 9H5a1 1 0 0 0-1 1z"/><path d="M17 9a4 4 0 0 1 0 6"/>'),
  ["Social media scheduler", "Content repurposer", "Webinar automation", "Competitor monitor",
   "Price monitoring", "Local SEO monitor", "Ad performance alerts", "Auto translator"]),
 ("Finance & orders", ic('<path d="M6 3h12v18l-2-1.4-2 1.4-2-1.4-2 1.4-2-1.4L6 21z"/><path d="M9 8h6M9 11.5h6M9 15h3"/>'),
  ["Invoice automation", "Payment reminders", "Expense sorter", "Stock monitor",
   "Order processing", "Shipping updates", "Report generator", "Business insight dashboard"]),
 ("HR & team", ic('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5"/><circle cx="17.5" cy="9" r="2.6"/><path d="M17 14.6c2.4.2 4 1.8 4.6 4.6"/>'),
  ["CV screener", "Interview scheduler", "Employee onboarding", "Timesheet collector",
   "Meeting notes", "Project status reports"]),
 ("Admin & systems", ic('<circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M4.6 4.6l2.1 2.1M17.3 17.3l2.1 2.1M2.5 12h3M18.5 12h3M4.6 19.4l2.1-2.1M17.3 6.7l2.1-2.1"/>'),
  ["Data entry", "Document sorter", "Compliance checker", "Contract analyzer", "Task automation",
   "File organizer", "Transcription", "Auto backup", "System health monitor", "Workflow orchestrator"]),
]
assert sum(len(x) for *_, x in G) == 50
n = 0
def grp(name, icon, items):
    global n
    li = ""
    for t in items:
        n += 1; li += f'<li><em>{n:02d}</em>{t}</li>'
    return f'<div class="g"><h3><span class="ico">{icon}</span>{name}<b>{len(items)}</b></h3><ul>{li}</ul></div>'
blocks = [grp(*g) for g in G]
left, right = "".join(blocks[:3]), "".join(blocks[3:])
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>50 AI Automations</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo_navy.png" alt="AIpreneur"></div>
  <div class="label">Save this list</div>
  <h1>50 AI automations<br>you can build and sell<br>to businesses.</h1>
  <div class="cols"><div>{left}</div><div>{right}</div></div>
</section></body></html>''')
print("ok")
