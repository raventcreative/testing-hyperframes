# The AI Agent Map: AIpreneur navy carousel (5 slides, 1080x1350). Render: node render.js
from pathlib import Path
D = Path(__file__).parent
def ic(b, w=1.8): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{b}</svg>'
I = {
 "eng": ic('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8h18M9.5 11.5 7 14l2.5 2.5M14.5 11.5 17 14l-2.5 2.5"/>'),
 "mkt": ic('<path d="M4 10v4a1 1 0 0 0 1 1h2l6 4V5L7 9H5a1 1 0 0 0-1 1z"/><path d="M17 9a4 4 0 0 1 0 6M19.5 6.5a7.5 7.5 0 0 1 0 11"/>'),
 "sales": ic('<path d="m3 11 3.5-3.5 4 1.2L13 7l4.5 1.5L21 11"/><path d="m3 11 5.5 5.5a1.6 1.6 0 0 0 2.2 0l.3-.3M21 11l-6.6 6.6a1.6 1.6 0 0 1-2.2 0L8.5 14"/>'),
 "ads": ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m6.5 15 2-6 2 6M7.2 13h2.6M13 9v6h1.5a3 3 0 0 0 0-6z"/>'),
 "design": ic('<path d="M12 3a9 9 0 1 0 0 18c1 0 1.5-.7 1.5-1.5 0-.5-.2-.8-.5-1.2-.3-.3-.5-.7-.5-1.1 0-.9.7-1.5 1.5-1.5H16a5 5 0 0 0 5-5C21 6.5 17 3 12 3z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7" r="1"/><circle cx="15" cy="7.5" r="1"/>'),
 "product": ic('<path d="m12 3 8 4v10l-8 4-8-4V7z"/><path d="m4 7 8 4 8-4M12 11v10"/>'),
 "projects": ic('<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4M8 14l2 2 4-4"/>'),
 "support": ic('<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/><path d="M19 19c0 1.5-1.5 2.5-4 2.5h-2"/>'),
 "finance": ic('<rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M5.5 9v.01M18.5 15v.01"/>'),
 "spec": ic('<path d="M12 3l2.5 5.5L20 9.5l-4 4 1 5.5-5-2.8-5 2.8 1-5.5-4-4 5.5-1z"/>'),
 "x": ic('<path d="M6 6l12 12M18 6 6 18"/>', 2.4), "ok": ic('<path d="m5 12.5 4.5 4.5L19 7.5"/>', 2.4),
}
DEP = [
 ("Engineering", "eng", "Build the product", ["Frontend", "Backend architect", "AI engineer", "Prompt engineer", "RAG pipelines", "Rapid prototyping", "Code reviewer", "Mobile apps", "DevOps", "Multi-agent systems"]),
 ("Marketing", "mkt", "Win attention", ["Social strategy", "Content creator", "Instagram", "TikTok", "LinkedIn", "SEO", "Email marketing", "Growth hacker", "Viral carousels", "Cross-platform posting"]),
 ("Sales", "sales", "Close more deals", ["Sales coach", "Discovery calls", "Outbound", "Offers & leads", "Proposals", "Deal closing", "Pipeline analysis", "Key accounts", "Sales engineer"]),
 ("Advertising", "ads", "Make ads perform", ["Account auditor", "Creative strategist", "Paid social", "Google Ads", "Programmatic ads", "Search spend", "Tracking & measurement"]),
 ("Design", "design", "Look professional", ["Brand guardian", "UI designer", "UX architect", "UX research", "Image prompts", "Visual storytelling", "Final UI review", "Design polish", "User journey"]),
 ("Product", "product", "Know what to build", ["Product manager", "Sprint priorities", "Trend scout", "User feedback", "Behavior nudges", "Developer experience"]),
 ("Projects", "projects", "Deliver on time", ["Senior PM", "Project tracking", "Meeting notes", "A/B experiments", "Operations", "Producer", "Jira workflows"]),
 ("Support", "support", "Keep clients happy", ["Customer support", "Reports & metrics", "Executive summary", "Expense control", "Legal review", "Servers"]),
 ("Finance", "finance", "Keep numbers in order", ["Accountant", "Financial analyst", "Budgets", "Taxes", "Investments"]),
 ("Specialists", "spec", "Cover the rest", ["Agent orchestrator", "Chief of staff", "CFO", "Customer success", "Recruiting", "Onboarding", "Business strategy", "MCP builder", "Workflow architect", "Translator"]),
]
assert sum(len(d[3]) for d in DEP) == 79

def frame(cls, body, swipe=False):
    sw = '<div class="bot">Swipe →</div>' if swipe else ''
    return f'<section class="slide {cls}"><div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>{body}{sw}</section>'

# 1 COVER
tiles = "".join(f'<div class="dt"><div class="dh"><span class="ico">{I[k]}</span><em>{i+1:02d}</em></div><ul class="pv">{"".join(f"<li>{x}</li>" for x in a[:3])}<li class="more">+{len(a)-3} more</li></ul><b>{n}</b><span class="ct">{len(a)} agents</span><small>{g}</small></div>'
                for i, (n, k, g, a) in enumerate(DEP))
cover = frame("cover", f'''<div class="label">The complete guide</div>
  <h1>The AI agent map<span>.</span></h1>
  <div class="stats"><div><b>79</b><span>agent roles</span></div><div><b>10</b><span>departments</span></div><div><b>1</b><span>agency team on Claude Code</span></div></div>
  <div class="dgrid">{tiles}</div>''', swipe=True)

# 2-3 DEPARTMENTS
n0 = [0]
def dcard(i):
    name, k, goal, agents = DEP[i]
    start = sum(len(d[3]) for d in DEP[:i])
    li = "".join(f'<li><em>{start+j+1:02d}</em>{a}</li>' for j, a in enumerate(agents))
    return f'<div class="dc"><h3><span class="ico">{I[k]}</span><div><small>Dept {i+1:02d}</small>{name}</div><b>{len(agents)}</b></h3><ul>{li}</ul><p class="goal"><small>Goal</small>{goal}</p></div>'
def tip(t, s): return f'<div class="dc tipc"><small>Tip</small><b>{t}</b><span>{s}</span></div>'
d1 = frame("dept", f'''<div class="label">Departments 01 to 05</div>
  <h1>Your front office<span>.</span></h1>
  <p class="lede">The teams that build, market and sell.</p>
  <div class="dg">{dcard(0)}{dcard(1)}{dcard(2)}{dcard(3)}{dcard(4)}{tip("Don’t hire all 45.", "Pick the 3 agents your next client project needs.")}</div>''')
d2 = frame("dept", f'''<div class="label">Departments 06 to 10</div>
  <h1>Your back office<span>.</span></h1>
  <p class="lede">The teams that deliver, support and keep the money right.</p>
  <div class="dg">{dcard(5)}{dcard(6)}{dcard(7)}{dcard(8)}{dcard(9)}{tip("Start with Specialists.", "An orchestrator plus a chief of staff keeps every other agent on track.")}</div>''')

# 4 USE IT RIGHT
inst = "".join(f'<li><em>{i+1}</em><div><b>{a}</b><span>{b}</span></div></li>' for i, (a, b) in enumerate([
  ("Get the agent files", "One file per role, written in plain text."), ("Add them to Claude Code", "Drop them into your project’s agents folder."),
  ("Call one by name", "“Use the proposal agent to draft this quote.”")]))
anat = "".join(f'<div class="an"><b>{a}</b><span>{b}</span></div>' for a, b in [
  ("Identity", "Who it is and its role"), ("Method", "How it does the work"), ("Rules", "What it must follow"),
  ("Metrics", "How it measures success"), ("Style", "How it hands work back")])
mist = "".join(f'<li>{I["x"]}<div><b>{t}</b><span>{d}</span><p class="fx"><small>Fix</small>{f}</p></div></li>' for t, d, f in [
  ("Installing every agent at once", "Too many voices. Claude picks the wrong one.", "Install 3 agents for this week’s project only."),
  ("Leaving the agent’s job vague", "“Help with marketing” gets you generic output.", "Give one task, one deliverable, one deadline."),
  ("Skipping the client’s context", "No brand, audience or offer means guesswork.", "Paste a one-page client brief before you start."),
  ("Shipping without a human review", "You sign the work, so you check it first.", "Read every output before it reaches the client.")])
use = frame("use", f'''<div class="label">Use it right</div>
  <h1>How to run your<br>agent team<span>.</span></h1>
  <div class="ug">
    <div class="card"><h3>Install in 3 steps</h3><ol class="inst">{inst}</ol></div>
    <div class="card"><h3>Anatomy of an agent</h3><div class="anat">{anat}</div></div>
    <div class="card wide"><h3>Beginner mistakes</h3><ul class="mist">{mist}</ul>
      <p class="do">{I["ok"]}Start with the one department your business needs most.</p></div>
  </div>''')

# 5 BUILD YOUR AGENCY
combos = "".join(f'<div class="cb"><b>{a}</b><span>{b}</span></div>' for a, b in [
  ("Win clients", "Offers & leads + Outbound + Discovery + Proposals"), ("Create content", "Social strategy + Viral carousels + Instagram + Cross-platform"),
  ("Run ads", "Account auditor + Creative strategist + Tracking + Reports"), ("Deliver projects", "Senior PM + Frontend + Code reviewer")])
flow = "".join(f'<div class="fs"><em>{i+1}</em><b>{a}</b><span>{b}</span></div>' + ('<i>→</i>' if i < 4 else '') for i, (a, b) in enumerate([
  ("Offers & leads", "Who to target"), ("Outbound", "The first message"), ("Discovery", "The first call"), ("Proposal", "The quote"), ("Close", "The signed deal")]))
road = "".join(f'<div class="rs{" hi" if i == 2 else ""}"><em>{a}</em><b>{b}</b><span>{c}</span></div>' for i, (a, b, c) in enumerate([
  ("Step 1", "One agent", "Fix one task"), ("Step 2", "One team", "Run one service"), ("Step 3", "Your agency", "Sell it to clients")]))
build = frame("build", f'''<div class="label">Build your agency</div>
  <h1>From one agent<br>to a full agency<span>.</span></h1>
  <div class="card"><h3>Team up agents per service</h3><div class="cbs">{combos}</div></div>
  <div class="card"><h3>Win clients with 5 sales agents</h3><div class="flow">{flow}</div></div>
  <div class="card"><h3>Your roadmap</h3><div class="road">{road}</div></div>''')

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>AI Agent Map</title><style>{CSS}</style></head><body>{cover}{d1}{d2}{use}{build}</body></html>')
print("ok")
