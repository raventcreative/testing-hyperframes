# The AI Agent Map, one slide (AIpreneur light, 1080x1350). Icons: Lucide (ISC), Claude logo: Simple Icons (CC0).
import re
from pathlib import Path
D = Path(__file__).parent
def L(n, w=2):
    s = (D / f"assets/icons/{n}.svg").read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    return re.sub(r'class="[^"]*"|width="24"|height="24"', "", s).replace('stroke-width="2"', f'stroke-width="{w}"')
CLAUDE = re.search(r'd="([^"]+)"', (D / "assets/icons/claude.svg").read_text()).group(1)
DEP = [
 ("Engineering", "code-xml", "Build the product", ["Frontend", "Backend architect", "AI engineer", "Prompt engineer", "RAG pipelines", "Rapid prototyping", "Code reviewer", "Mobile apps", "DevOps", "Multi-agent systems"]),
 ("Marketing", "megaphone", "Win attention", ["Social strategy", "Content creator", "Instagram", "TikTok", "LinkedIn", "SEO", "Email marketing", "Growth hacker", "Viral carousels", "Cross-posting"]),
 ("Sales", "handshake", "Close more deals", ["Sales coach", "Discovery calls", "Outbound", "Offers & leads", "Proposals", "Deal closing", "Pipeline analysis", "Key accounts", "Sales engineer"]),
 ("Advertising", "badge-percent", "Make ads perform", ["Account auditor", "Creative strategist", "Paid social", "Google Ads", "Programmatic", "Search spend", "Tracking"]),
 ("Design", "palette", "Look professional", ["Brand guardian", "UI designer", "UX architect", "UX research", "Image prompts", "Visual stories", "Final UI review", "Design polish", "User journey"]),
 ("Product", "package", "Know what to build", ["Product manager", "Sprint priorities", "Trend scout", "User feedback", "Behavior nudges", "Dev experience"]),
 ("Projects", "calendar-check", "Deliver on time", ["Senior PM", "Project tracking", "Meeting notes", "A/B tests", "Operations", "Producer", "Jira workflows"]),
 ("Support", "headset", "Keep clients happy", ["Customer support", "Reports & metrics", "Exec summary", "Expense control", "Legal review", "Servers"]),
 ("Finance", "wallet", "Keep numbers right", ["Accountant", "Financial analyst", "Budgets", "Taxes", "Investments"]),
 ("Specialists", "sparkles", "Cover the rest", ["Orchestrator", "Chief of staff", "CFO", "Customer success", "Recruiting", "Onboarding", "Biz strategy", "MCP builder", "Workflow architect", "Translator"]),
]
assert sum(len(d[3]) for d in DEP) == 79
num = 0; cards = ""
for i, (name, ico, goal, ag) in enumerate(DEP):
    li = ""
    for a in ag:
        num += 1; li += f"<li><em>{num}</em>{a}</li>"
    cards += f'<div class="dc"><div class="dh"><span class="ico">{L(ico)}</span><em>{i+1:02d}</em></div><b class="dn">{name}</b><small class="cnt">{len(ag)} agents</small><ul>{li}</ul><p class="goal"><small>Goal</small>{goal}</p></div>'
steps = "".join(f'<li><em>{k}</em><div><b>{t}</b><small>{d}</small></div></li>' for k, t, d in [(1, "Get the agent files", "One plain-text file per role"), (2, "Add them to Claude Code", "Drop into your agents folder"), (3, "Call one by name", "“Use the proposal agent…”")])
anat = "".join(f'<li><b>{a}</b>{b}</li>' for a, b in [("Identity", "Its role"), ("Method", "How it works"), ("Rules", "What it follows"), ("Metrics", "How it’s judged"), ("Style", "How it delivers")])
mist = "".join(f'<li>{L("x", 2.6)}{t}</li>' for t in ["Too many agents", "Vague tasks", "No client context", "No human review"])
FLOW = [("target", "Leads", "Who to target"), ("send", "Outbound", "First message"), ("phone-call", "Discovery", "First call"), ("file-text", "Proposal", "The quote"), ("badge-check", "Close", "Signed deal")]
flow = "".join(f'<div class="fs"><span class="ico sm">{L(ic)}</span><b>{a}</b><small>{b}</small></div>' + ('<i>›</i>' if k < 4 else '') for k, (ic, a, b) in enumerate(FLOW))
road = "".join(f'<div class="rs r{k}"><span class="ico sm">{L(ic)}</span><b>{t}</b></div>' for k, (ic, t) in enumerate([("bot", "One agent"), ("users", "One team"), ("building-2", "Your agency")]))
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>AI Agent Map</title><style>{CSS}</style></head><body>
<section class="slide">
 <div class="hd">
  <div class="hl"><img class="logo" src="assets/logo_navy.png" alt="AIpreneur">
   <div class="label">The complete guide</div>
   <h1>The AI agent map.</h1>
   <p class="sub">A full agency team on <span class="cl"><svg viewBox="0 0 24 24"><path fill="#D97757" d="{CLAUDE}"/></svg>Claude Code</span>, split into 10 departments.</p></div>
  <div class="badge"><b>79</b><span>agent roles</span><i></i><b class="s">10</b><span>departments</span></div>
 </div>
 <div class="grid">{cards}</div>
 <div class="row">
  <div class="bx"><h3>Install</h3><ol class="st">{steps}</ol></div>
  <div class="bx"><h3>Anatomy of an agent</h3><ul class="an">{anat}</ul></div>
  <div class="bx"><h3>Beginner mistakes</h3><ul class="ms">{mist}</ul><p class="do">{L("check", 3)}Start with one department.</p></div>
 </div>
 <div class="row r2">
  <div class="bx fl"><h3>Win clients with 5 sales agents</h3><div class="flow">{flow}</div></div>
  <div class="bx rd"><h3>Your roadmap</h3><div class="road">{road}</div></div>
 </div>
</section></body></html>''')
print("ok")
