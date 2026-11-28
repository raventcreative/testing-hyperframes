# Claude MBA: set up Claude as your AI operating system (AIpreneur navy remake, 1 slide 1080x1350).
# Only real Claude features (checked against support.claude.com / code.claude.com, Nov 2026).
import math
from pathlib import Path
D = Path(__file__).parent
SEC = {
 1: ("Choose your AI brain", [("Haiku", "fast, simple tasks"), ("Sonnet", "daily work & writing"), ("Opus", "complex reasoning & code"), ("Effort", "low → max in Claude Code")]),
 2: ("Build your workspace", [("Projects", "your business knowledge"), ("Artifacts", "docs, apps & dashboards"), ("Plan mode", "plan before it edits"), ("CLAUDE.md", "project memory")]),
 3: ("Install power skills", [("Skills", "reusable instructions"), ("Doc skills", "PDF, Excel, Word, PPT"), ("Skill creator", "build your own"), ("Plugins", "skills + tools bundled")]),
 4: ("Connect business tools", [("Drive & Gmail", "your files and inbox"), ("Calendar", "meetings & schedule"), ("Notion & GitHub", "notes and code"), ("n8n & CRM", "via MCP")]),
 5: ("Build your AI team", [("Subagents", "split big jobs"), ("Research agent", "market & competitors"), ("Content agent", "scripts & captions"), ("Review agent", "check before delivery")]),
 6: ("Automate your work", [("Scheduled tasks", "recurring jobs in Cowork"), ("MCP", "talk to other apps"), ("n8n webhooks", "trigger workflows"), ("Approvals", "you sign off risky steps")]),
 7: ("Create business outputs", [("Websites", "landing pages"), ("Dashboards", "reports & KPIs"), ("Presentations", "decks & docs"), ("WhatsApp agents", "via n8n")]),
 8: ("Power user system", [("Claude Code", "build software"), ("Cowork", "delegate tasks"), ("Skills + tools", "one setup, reused"), ("Dashboards", "measure results")]),
}
WHEEL = ["AI brain", "Workspace", "Power skills", "Business tools", "AI team", "Automation", "Outputs", "Power user"]
def card(n):
    t, items = SEC[n]
    li = "".join(f"<li><b>{a}</b> · {b}</li>" for a, b in items)
    return f'<div class="c"><h3><i>{n:02d}</i>{t}</h3><ul>{li}</ul></div>'
# donut wheel, segment 1 at the top, clockwise
cx = cy = 140; R1, R0 = 136, 66
segs = ""
for k in range(8):
    a0 = math.radians(-90 - 22.5 + k * 45 + 1.2); a1 = math.radians(-90 + 22.5 + k * 45 - 1.2)
    p = lambda r, a: f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}"
    op = 0.95 - k * 0.075
    segs += f'<path d="M{p(R1,a0)} A{R1},{R1} 0 0 1 {p(R1,a1)} L{p(R0,a1)} A{R0},{R0} 0 0 0 {p(R0,a0)} Z" fill="rgba(1,204,247,{op:.2f})"/>'
    am = math.radians(-90 + k * 45); tx, ty = cx + 101 * math.cos(am), cy + 101 * math.sin(am)
    segs += f'<text x="{tx:.1f}" y="{ty-4:.1f}" class="wn">{k+1:02d}</text><text x="{tx:.1f}" y="{ty+12:.1f}" class="wl">{WHEEL[k]}</text>'
wheel = f'<div class="wh"><svg viewBox="0 0 280 280">{segs}</svg><img src="assets/claude3d.png" alt="Claude"></div>'
grid = card(8) + card(1) + card(2) + card(7) + wheel + card(3) + card(6) + card(5) + card(4)
steps = ["Knowledge", "Skills", "Cowork", "Code", "Agents", "Connectors", "Automation", "Business intelligence"]
formula = '<span class="ar">→</span>'.join(f"<span>{s}</span>" for s in steps)
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Claude MBA</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>
  <h1>Claude <span>MBA</span></h1>
  <p class="sub">Set up Claude as your AI operating system, step by step</p>
  <div class="grid">{grid}</div>
  <div class="fx"><div class="fl">The formula</div><div class="fs">{formula}</div>
  <p>Don’t just use Claude to generate answers. Build a system that researches, creates, automates and executes real work.</p></div>
</section></body></html>''')
print("ok")
