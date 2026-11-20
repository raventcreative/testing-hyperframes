# Claude + n8n: automate a real estate business, explained (AIpreneur navy carousel, 1080x1350).
# Render: python3 -m http.server 8765 & node render.js | Check: node check-safezone.js
from pathlib import Path
D = Path(__file__).parent
L = lambda s, h=None: f'<img src="assets/3d/{s}.png" alt="{s}"' + (f' style="height:{h}px"' if h else '') + '>'
def ic(b): return f'<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{b}</svg>'
I = {  # Lucide (ISC) paths
 "crm": ic('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M9 9v11"/>'),
 "web": ic('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/>'),
 "home": ic('<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>'),
 "copy": ic('<rect x="8" y="8" width="13" height="13" rx="2"/><path d="M4 16V5a2 2 0 0 1 2-2h11"/>'),
 "clock": ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "chat": ic('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-5.1A8 8 0 1 1 21 12z"/>'),
 "stop": ic('<circle cx="12" cy="12" r="9"/><rect x="9" y="9" width="6" height="6" rx="1"/>'),
 "db": ic('<ellipse cx="12" cy="5.5" rx="8" ry="3"/><path d="M4 5.5v13c0 1.7 3.6 3 8 3s8-1.3 8-3v-13M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>'),
 "bell": ic('<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>'),
 "chart": ic('<path d="M4 20V10M10 20V5M16 20v-7M21 20H3"/>'),
}
def frame(body, swipe=False):
    sw = '<div class="swipe">Swipe →</div>' if swipe else ''
    return f'<section class="slide"><div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>{body}{sw}</section>'
def step(n, title, lead, how, visual, ex_label, ex, z=None, mis=None):
    li = "".join(f"<li>{h}</li>" for h in how)
    return frame(f'''<div class="chip"><b>{n}</b>Step {n}</div><h2>{title}</h2><p class="lead">{lead}</p>
  <div class="cols"><div class="how"><h4>How to set it up</h4><ol>{li}</ol></div><div{f' style="zoom:{z}"' if z else ""}>{visual}</div></div>
  <div class="box"><div class="lbl">{ex_label}</div><p>{ex}</p></div>''' + (f'<div class="box mis"><div class="lbl">Common mistake</div><p>{mis}</p></div>' if mis else ''))
def win(title, logo, body): return f'<div class="win"><div class="wh">{logo}{title}<i></i></div><div class="wb">{body}</div></div>'
WIN_N8N = lambda b: win("n8n workflow", L("n8n"), b)

S = []
# 1 cover
S.append(frame(f'''<div class="chip">Step-by-step guide</div>
  <h1 style="margin-top:22px">Automate your<br>real estate business<br>with <span>Claude + n8n.</span></h1>
  <p class="lead" style="font-size:23px">9 steps, explained simply. From the first<br>lead to the closed deal, on autopilot.</p>
  <div style="flex:1;margin-bottom:60px;display:flex;align-items:center;justify-content:center;gap:34px">
    <img src="assets/3d/claude.png" style="height:320px;transform:rotate(-6deg)" alt="Claude">
    <span style="font-size:90px;font-weight:300;color:var(--ac)">+</span>
    <img src="assets/3d/n8n.png" style="width:340px;transform:rotate(5deg)" alt="n8n"></div>''', swipe=True))
# 2 big picture
roles = [(L("claude", 34), "Claude", "The brain. Answers buyers, scores leads, builds reports."),
         (L("n8n", 22), "n8n", "The engine. Moves data between apps, 24/7, with no copy-paste."),
         (I["crm"], "Twenty CRM", "The memory. One record per buyer: budget, area, status."),
         (L("whatsapp", 32), "WhatsApp", "The front door. Where Indonesian buyers actually reply."),
         (L("googlecalendar", 30), "Google Calendar", "The schedule. Site visits booked without back-and-forth.")]
rl = "".join(f'<div class="row" style="padding:12px 14px;margin-bottom:10px"><span style="width:46px;display:grid;place-items:center">{a}</span><div><b style="font-size:18px">{b}</b><div style="font-size:15px;color:var(--dim)">{c}</div></div></div>' for a, b, c in roles)
flow = ["Lead comes in", "Saved in CRM", "AI replies on WhatsApp", "Scored hot / warm / cold", "Site visit booked", "Follow-ups sent", "Dashboard updated"]
fl = "".join(f'<div class="row{" on" if i in (2,4) else ""}" style="margin-bottom:0;font-size:15.5px;font-weight:600"><b style="color:var(--ac);width:20px">{i+1}</b>{t}</div>' + ('<div class="arrow">↓</div>' if i < len(flow)-1 else '') for i, t in enumerate(flow))
S.append(frame(f'''<div class="chip">Before you start</div><h2>How the whole<br>system <span>fits together.</span></h2>
  <p class="lead">Five tools, each with one job. n8n connects them, Claude does the thinking.</p>
  <div class="cols nz" style="grid-template-columns:1.15fr .85fr"><div><div class="lbl">Who does what</div>{rl}</div>
  <div><div class="lbl">What happens to every lead</div>{fl}</div></div>
  <div class="box"><div class="lbl">Why bother</div><p>Most property deals are lost to <b>slow replies and forgotten follow-ups</b>, not to price. This system replies in seconds and never forgets a buyer.</p></div>'''))
# 3 step 1
S.append(step(1, "Create your <span>Claude project.</span>",
  "A project is Claude’s workspace for your business. Everything you upload here becomes its <b>knowledge</b>, so it answers like your best agent.",
  ["Open <b>claude.ai</b> → <b>Projects</b> → <b>New project</b>.", "Name it, e.g. <code>Real estate AI</code>.",
   "Upload your <b>listings, price list, FAQs</b> and payment terms (cash / KPR).",
   "In <b>Project instructions</b>, write your sales process and tone: who you sell to, what to ask, when to hand over to a human."],
  win("Claude · New project", L("claude"),
      '<div style="font-size:17px;font-weight:700;margin-bottom:8px">Real estate AI</div><div class="lbl" style="font-size:11.5px;margin-bottom:6px">Project knowledge</div>'
      + "".join(f'<div class="row">{I["copy"] if False else ""}<span class="mono">{f}</span><small>{s}</small></div>' for f, s in [("listings.csv", "48 units"), ("price-list.pdf", "2026"), ("faq.docx", "32 Q&A"), ("payment-terms.pdf", "cash / KPR")])
      + '<div class="lbl" style="font-size:11.5px;margin:10px 0 6px">Instructions</div><div class="row" style="display:block;font-size:13px;color:var(--dim)">“Reply in friendly Bahasa Indonesia. Always ask budget, area and timeline. Hand over to a human agent when the buyer wants a site visit.”</div>'),
  "Example", "A developer in BSD uploads 48 listings and a KPR guide. Claude can now answer <b>“Is there a 3-bedroom under Rp1,5 M near the toll gate?”</b> with real units, not guesses."))
# 4 step 2
S.append(step(2, "Connect <span>n8n to Claude.</span>",
  "This lets you build and run n8n workflows <b>by chatting with Claude</b>. It uses MCP, a standard “plug” that lets AI tools talk to other apps.",
  ["In n8n: <b>Settings</b> → <b>Instance-level MCP</b> → turn on <b>Enable MCP access</b>.",
   "Copy the <b>server URL</b>. It ends in <code>/mcp-server/http</code>.",
   "In Claude: <b>Settings</b> → <b>Connectors</b> → <b>Add custom connector</b>, paste the URL.",
   "Click <b>Connect</b> and authorize in n8n. Then mark which workflows Claude may use."],
  win("n8n · Settings", L("n8n"), '<div class="row on"><b>Instance-level MCP</b><span class="tog"></span></div><div class="row"><span class="mono">https://your-n8n…/mcp-server/http</span></div>')
  + '<div class="arrow" style="margin:10px 0">↓ paste URL</div>'
  + win("Claude · Connectors", L("claude"), '<div class="row"><b>n8n</b><small>custom connector</small></div><div class="row on"><b style="color:var(--ac)">✓ Connected</b><small>authorized</small></div><div class="bub out" style="margin-top:8px">“Help me build a workflow that saves new leads to my CRM.”</div>'),
  "Good to know", "Turning on MCP needs <b>owner or admin</b> access in n8n. If Claude shows “connected” but no tools, make sure your workflows are <b>enabled for MCP</b>."))
# 5 step 3
rows = [("Budi", "1,5 M", "BSD", "FB Ads", "82", '<span class="tag">Hot</span>'),
        ("Rina", "900 jt", "Bekasi", "Website", "55", '<span class="tag o">Warm</span>'),
        ("Dimas", "3 M", "Depok", "Portal", "28", '<span class="tag g">Cold</span>')]
tb = "<table><tr><th>Name</th><th>Budget</th><th>Area</th><th>Source</th><th>Score</th><th>Status</th></tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
S.append(step(3, "Set up <span>Twenty CRM.</span>",
  "Twenty is a free, open-source CRM: the <b>single list of every buyer</b>. Without it, leads live in 5 different chats and get lost.",
  ["Create a workspace at <b>twenty.com</b> (cloud) or self-host it.",
   "In <b>Contacts</b>, add fields: <b>phone, budget, area, source, score, status</b>.",
   "Go to <b>Settings</b> → <b>APIs &amp; Webhooks</b> → <b>Create key</b>. Copy it now, it is shown once.",
   "In n8n: <b>Credentials</b> → add a <b>Twenty</b> credential (community node) or use the HTTP Request node with the key."],
  win("Twenty · Contacts", I["crm"].replace('class="ic"', 'class="ic" style="width:22px;height:22px"'), tb)
  + '<div style="display:flex;align-items:center;gap:10px;margin-top:12px"><div class="node" style="flex:1">API key<small>from Twenty</small></div><div style="color:var(--ac);font-size:22px">→</div><div class="node hi" style="flex:1">' + L("n8n") + '<small>credential saved</small></div></div>',
  "Why these fields", "Every later step reads them: the AI agent fills <b>budget</b> and <b>area</b>, scoring writes <b>score</b>, and the dashboard counts <b>status</b>.", mis="Saving leads in WhatsApp chats or a phone’s contact list. When the agent changes phones or leaves, <b>the buyers leave with them</b>."))
# 6 step 4
src = [(L("facebook"), "Facebook Lead Ads", "n8n trigger"), (I["web"], "Website form", "webhook"), (I["home"], "Property portals", "email alert"), (L("gmail"), "Email inquiries", "Gmail trigger")]
sl = "".join(f'<div class="row">{a}<b>{b}</b><small>{c}</small></div>' for a, b, c in src)
S.append(step(4, "Capture <span>every lead</span><br>automatically.",
  "Leads arrive from ads, your website, listing portals and email. n8n collects them all into Twenty, <b>the second they come in</b>.",
  ["Create a new n8n workflow, one <b>trigger</b> per source (Facebook Lead Ads, Webhook, Gmail).",
   "Add a <b>Set</b> node so every lead has the same fields: name, phone, budget, area, source.",
   "Add a <b>duplicate check</b>: search Twenty by phone number first.",
   "New buyer → <b>create</b> contact. Existing buyer → <b>update</b> it. Each lead is saved once."],
  WIN_N8N(sl + '<div class="arrow">↓</div><div style="display:flex;gap:8px;align-items:center"><div class="node" style="flex:1">' + I["copy"] + 'Check duplicate<small>by phone</small></div><div style="color:var(--ac)">→</div><div class="node hi" style="flex:1">' + I["crm"] + 'Save to Twenty<small>create / update</small></div></div>'),
  "Example", "Budi fills a Facebook ad form at 23:40. By <b>23:40</b> he is in your CRM with source “FB Ads”, and Step 5 has already said hello on WhatsApp.", mis="Skipping the duplicate check. The same buyer from an ad and a portal becomes <b>2 contacts</b>, gets 2 replies and looks like spam.", z=1.0))
# 7 step 5
chat = ('<div class="bub in">Halo, rumah 3 kamar di BSD budget 1,5 M masih ada?</div>'
        '<div class="bub out">Ada 2 unit, Pak Budi: Cluster A (Rp1,45 M) dan Cluster C (Rp1,5 M). Rencananya untuk ditinggali atau investasi?</div>')
S.append(step(5, "Build your <span>WhatsApp<br>AI agent.</span>",
  "This is the agent that <b>answers buyers 24/7</b> on WhatsApp, using only your real listings, and writes what it learns back into the CRM.",
  ["Set up the <b>WhatsApp Business Platform</b> (Cloud API) in Meta for Developers and get your number’s token.",
   "In n8n: <b>WhatsApp Trigger</b> → <b>AI Agent</b> (Claude as the chat model) → <b>WhatsApp</b> send.",
   "Give the agent 2 tools: <b>your listings data</b> and <b>Twenty</b> (to read and update the buyer).",
   "Add a rule: price, availability and promos come <b>only from the listings data</b>. Never invent them."],
  WIN_N8N('<div style="display:flex;gap:7px;align-items:center"><div class="node" style="flex:1">' + L("whatsapp") + 'Trigger</div><div style="color:var(--ac)">→</div><div class="node hi" style="flex:1.2">' + L("claude") + 'AI Agent</div><div style="color:var(--ac)">→</div><div class="node" style="flex:1">' + L("whatsapp") + 'Reply</div></div>'
          '<div style="display:flex;gap:8px;margin-top:8px"><div class="node" style="flex:1">' + I["db"] + 'Listings data</div><div class="node" style="flex:1">' + I["crm"] + 'Twenty CRM</div></div>')
  + '<div class="win" style="margin-top:12px"><div class="wh">' + L("whatsapp") + 'WhatsApp<i></i></div><div class="wb">' + chat + '</div></div>',
  "Important", "Outside the <b>24-hour window</b> after a buyer’s last message, WhatsApp only allows <b>pre-approved template messages</b>. Prepare templates for follow-ups and reminders.", z=1.06))
# 8 step 6
qs = ["Budget", "Location", "Property type", "Timeline", "Purpose (live / invest)", "Payment (cash / KPR)"]
ql = "".join(f'<div class="row" style="margin-bottom:6px;font-size:13.5px"><b style="color:var(--ac)">{i+1}</b>{q}</div>' for i, q in enumerate(qs))
rub = [("Budget matches a listing", "+25"), ("Buying within 3 months", "+25"), ("Cash or KPR pre-approved", "+20"), ("Wants your area", "+15"), ("Replies fast", "+15")]
rb = "".join(f'<div class="row" style="margin-bottom:6px;font-size:13.5px">{a}<small style="color:var(--ac);font-weight:700">{b}</small></div>' for a, b in rub)
S.append(step(6, "Qualify and <span>score buyers.</span>",
  "Not every lead is ready to buy. The agent asks <b>6 short questions</b> in the chat, then gives each buyer a score from <b>0 to 100</b>.",
  ["Add the 6 questions to the agent’s instructions. Ask them <b>naturally</b>, one or two at a time.",
   "Save each answer into Twenty as it comes in.",
   "Use a <b>Code</b> or <b>AI</b> node to add up the score with a fixed rubric (right).",
   "Route by score with an <b>IF / Switch</b> node: hot, warm or cold."],
  '<div class="lbl" style="font-size:12px">The 6 questions</div>' + ql + '<div class="lbl" style="font-size:12px;margin-top:10px">Example rubric (max 100)</div>' + rb,
  "What happens next", "<b>Hot 70+</b>: alert your sales agent on WhatsApp now. <b>Warm 40–69</b>: send to follow-ups (Step 8). <b>Cold under 40</b>: monthly newsletter only.", z=1.1))
# 9 step 7
slots = "".join(f'<div class="row{" on" if t == "14:00" else ""}" style="margin-bottom:6px">{"☑" if t == "14:00" else "☐"} Sat 28 Nov · {t}</div>' for t in ["10:00", "14:00", "16:00"])
S.append(step(7, "Automate <span>site visits.</span>",
  "Booking a viewing usually takes 6–10 messages. Here the buyer <b>picks a free slot</b> in the chat and everything else updates itself.",
  ["Connect <b>Google Calendar</b> (or Cal.com) in n8n.",
   "When a hot buyer wants to visit, read your <b>free slots</b> for the next 7 days.",
   "Send 3 options on WhatsApp. The buyer replies with one.",
   "Create the calendar event, set CRM status to <b>Visit booked</b>, and send a reminder <b>1 day before</b>."],
  win("Google Calendar · free slots", L("googlecalendar"), slots)
  + '<div class="arrow">↓ buyer picks 14:00</div>'
  + '<div class="win"><div class="wb"><div class="row on"><b style="color:var(--ac)">✓ Site visit booked</b><small>Sat 14:00</small></div><div class="row">' + I["crm"].replace('class="ic"', 'class="ic" style="width:22px;height:22px"') + 'Twenty updated<small>Visit booked</small></div><div class="row">' + I["bell"].replace('class="ic"', 'class="ic" style="width:22px;height:22px"') + 'Reminder<small>Fri 14:00</small></div></div></div>',
  "Example", "Rina picks <b>Saturday 14:00</b> at 22:15. Your agent wakes up to a booked visit, the buyer’s budget and the unit she asked about, all in the calendar note.", mis="Offering every free hour. Send <b>only 3 options</b>: too many choices makes buyers postpone the decision.", z=1.14))
# 10 step 8
S.append(step(8, "Automate <span>follow-ups.</span>",
  "Most buyers don’t say no, they just go quiet. This workflow <b>checks in politely</b> until they reply, then stops by itself.",
  ["Start the workflow when a buyer is <b>warm</b> or has gone quiet.",
   "<b>Wait</b> 2 days, then check Twenty: did they reply?",
   "No reply → send a WhatsApp <b>template</b> with something useful (new unit, price update, KPR simulation).",
   "Repeat up to 3 times. Stop at once if they reply or send <b>STOP</b>."],
  WIN_N8N('<div style="display:flex;gap:7px;align-items:center"><div class="node" style="flex:1">' + I["clock"] + 'Wait<small>2 days</small></div><div style="color:var(--ac)">→</div><div class="node" style="flex:1">' + I["chat"] + 'Replied?</div></div>'
          '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px"><div><div class="lbl" style="font-size:11px;margin-bottom:4px">No reply</div><div class="node hi">' + L("whatsapp") + 'Send follow-up<small>max 3 times</small></div></div>'
          '<div><div class="lbl" style="font-size:11px;margin-bottom:4px">Replied / STOP</div><div class="node">' + I["stop"] + 'Stop<small>hand to agent</small></div></div></div>'),
  "Sample follow-up", "“Pak Budi, unit Cluster A yang kemarin ditanyakan ada <b>simulasi KPR mulai Rp9 jt/bulan</b>. Mau saya kirimkan detailnya?”", mis="Sending “Halo, masih minat?” three times. Every follow-up should <b>give something new</b>: a unit, a price or a simulation."))
# 11 step 9
tiles = [("New leads", "126"), ("Avg. reply time", "38 s"), ("Hot buyers", "19"), ("Site visits", "11"), ("Deals closed", "3"), ("Pipeline", "Rp4,4 M")]
tl = "".join(f'<div class="row" style="display:block;margin:0"><small style="margin:0;display:block">{a}</small><b style="font-size:22px">{b}</b></div>' for a, b in tiles)
S.append(step(9, "Build your <span>growth<br>dashboard.</span>",
  "One screen that tells you <b>what is working</b>: how many leads came in, how fast you replied, and how many became visits and deals.",
  ["Make an n8n workflow that runs <b>every morning</b> and pulls this week’s numbers from Twenty.",
   "Send them to Claude (through the MCP connector from Step 2).",
   "Ask: <b>“Build a visual dashboard from this CRM data.”</b> Claude creates it as an interactive page.",
   "Check it weekly: double down on the lead source with the most <b>closed deals</b>, not the most leads."],
  win("Real estate dashboard", L("claude"), f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">{tl}</div><div style="font-size:11.5px;color:var(--dim);margin-top:8px">Example data</div>'),
  "Example", "The dashboard shows Facebook brings the most leads but <b>website leads close 3× more</b>. You move budget to the website and get more deals for the same spend."))
# 12 recap
steps = ["Claude project with your listings", "n8n connected to Claude (MCP)", "Twenty CRM as the buyer list", "Every lead captured, saved once",
         "WhatsApp AI agent, 24/7", "Buyers scored 0–100", "Site visits booked in chat", "Follow-ups until they reply", "Weekly growth dashboard"]
ck = "".join(f'<div class="row" style="padding:11px 14px;margin-bottom:9px;font-size:18px"><b style="color:var(--ac);width:26px">{i+1}</b>{t}<small style="color:var(--ac);font-size:18px">✓</small></div>' for i, t in enumerate(steps))
S.append(frame(f'''<div class="chip">Recap</div><h2>Your real estate<br><span>autopilot checklist.</span></h2>
  <div style="margin-top:26px">{ck}</div>
  <div class="box"><div class="lbl">Where to start</div><p>Don’t build all 9 at once. Start with <b>Steps 3, 4 and 5</b>: CRM, lead capture and the WhatsApp agent. That’s where most deals leak. Save this post for later.</p></div>'''))

CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Claude + n8n Real Estate</title><style>{CSS}</style></head><body>{"".join(S)}</body></html>')
print("ok", len(S))
