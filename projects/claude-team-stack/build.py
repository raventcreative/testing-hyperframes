# The Claude Team Stack (AIpreneur light). Tool logos cropped from the reference the user supplied;
# Claude logo: Simple Icons (CC0); department icons: Lucide (ISC). Render: node render.js
import re
from pathlib import Path
D = Path(__file__).parent
def L(n, w=2):
    s = re.sub(r"<!--.*?-->", "", (D / f"assets/icons/{n}.svg").read_text(), flags=re.S)
    return re.sub(r'class="[^"]*"|width="24"|height="24"', "", s).replace('stroke-width="2"', f'stroke-width="{w}"')
CL = re.search(r'd="([^"]+)"', (D / "assets/icons/claude.svg").read_text()).group(1)
CLAUDE = f'<svg viewBox="0 0 24 24"><path fill="#D97757" d="{CL}"/></svg>'
DEPTS = [("Build", "code-xml"), ("Design", "palette"), ("Grow", "trending-up"), ("Make", "clapperboard"), ("Run", "workflow")]
DATA = {
 "Design": ("Design", "& motion.", "Make your screens, motion and visuals look like one brand.", 11, [
  ("taste", "taste-skill", "Style Director", "Gives generic layouts a distinct look before you design."),
  ("figma", "Figma", "Design Hub", "Pulls frames and components straight into your build."),
  ("uiux", "UI UX Pro Max", "Layout Lead", "Fixes spacing, type scale and mobile navigation."),
  ("impeccable", "Impeccable", "Consistency Checker", "Catches off-brand colors, sizes and spacing."),
  ("emil", "emil-design-eng", "Interaction Designer", "Polishes hover states, transitions and loading moments."),
  ("hyperframes", "HyperFrames", "Motion Designer", "Turns HTML scenes into animated explainers."),
  ("remotion", "Remotion", "Video Coder", "Builds data-driven videos from React code."),
  ("higgsfield", "Higgsfield", "B-roll Studio", "Generates cinematic shots for Reels and ads."),
  ("ffmpeg", "FFmpeg", "Edit Engine", "Trims, merges, compresses and converts footage."),
  ("axe", "axe-core", "Accessibility Check", "Flags contrast and screen-reader issues.")]),
 "Grow": ("Research", "& grow.", "Learn what buyers want, then turn it into sales.", 21, [
  ("last30", "last30days", "Trend Radar", "Shows what your market talked about this month."),
  ("perplexity", "Perplexity", "Fact Checker", "Answers market questions with linked sources."),
  ("gemini", "Google Gemini", "Video Analyst", "Breaks down why competitor videos perform."),
  ("firecrawl", "Firecrawl", "Site Reader", "Turns competitor websites into clean text."),
  ("apify", "Apify", "Data Collector", "Pulls listings, prices and reviews at scale."),
  ("chrome", "Claude in Chrome", "Browser Agent", "Clicks through sites and fills forms for you."),
  ("apollo", "Apollo", "Lead Finder", "Finds decision-makers and how to reach them."),
  ("humanizer", "humanizer", "Copy Polisher", "Removes robotic phrasing from AI drafts."),
  ("metricool", "Metricool", "Social Scheduler", "Plans posts and tracks growth per platform."),
  ("windsor", "Windsor.ai", "ROI Tracker", "Merges ad data to show which campaign pays.")]),
 "Make": ("Create", "& produce.", "Turn one brief into a full library of finished content.", 31, [
  ("granola", "Granola", "Brief Catcher", "Turns client calls into decisions and next steps."),
  ("gptimage", "GPT Image", "Concept Artist", "Creates campaign visuals and illustrations."),
  ("nanobanana", "Nano Banana", "Photo Editor", "Edits product photos from plain instructions."),
  ("canva", "Canva", "Template Studio", "Builds reusable branded social templates."),
  ("puppeteer", "Puppeteer", "Graphics Printer", "Renders HTML layouts into feed-ready images."),
  ("elevenlabs", "ElevenLabs", "Voice Studio", "Turns approved scripts into natural voiceovers."),
  ("whisper", "Whisper", "Transcriber", "Turns recordings into subtitles and captions."),
  ("gamma", "Gamma", "Deck Builder", "Turns research into clean presentations."),
  ("python", "Python", "Data Analyst", "Cleans data and makes charts for reports."),
  ("gdrive", "Google Drive", "Asset Library", "Keeps files, brand assets and deliverables tidy.")]),
 "Run": ("Operate", "& automate.", "Hand off the work nobody wants to do by hand.", 41, [
  ("gmail", "Gmail", "Inbox Assistant", "Sorts email, summarizes threads, drafts replies."),
  ("gcal", "Google Calendar", "Scheduler", "Finds free slots and preps meeting details."),
  ("slack", "Slack", "Team Updates", "Summarizes threads into a daily team brief."),
  ("notion", "Notion", "Operations Hub", "Holds SOPs, project plans and meeting notes."),
  ("zapier", "Zapier", "App Connector", "Links your tools and triggers actions automatically."),
  ("n8n", "n8n", "Workflow Builder", "Automates lead capture, CRM updates and follow-ups."),
  ("nodejs", "Node.js", "Script Runner", "Runs approved scripts and small utilities."),
  ("ollama", "Ollama", "Local AI", "Runs open models privately on your own machine."),
  ("findskills", "find-skills", "Skill Finder", "Finds a ready-made skill for the task at hand."),
  ("caveman", "caveman", "Token Saver", "Shortens replies to cut usage costs.")]),
}
for v in DATA.values(): assert len(v[4]) == 10

def frame(cls, body, swipe=False):
    sw = '<div class="bot">Swipe →</div>' if swipe else ''
    return f'<section class="slide {cls}"><img class="logo" src="assets/logo_navy.png" alt="AIpreneur">{body}{sw}</section>'

# COVER
DESC = ["Sites, apps and code", "Visuals and motion", "Research and leads", "Content and media", "Ops and automation"]
cards = "".join(f'<div class="dp"><span class="di">{L(ic)}</span><small>{i+1:02d} · 10 add-ons</small><b>{n}</b><span>{DESC[i]}</span></div>' for i, (n, ic) in enumerate(DEPTS))
wires = '<svg class="wires" viewBox="0 0 860 90" preserveAspectRatio="none"><path d="M430 0V30M86 90V46q0-16 16-16h656q16 0 16 16v44M258 30v60M430 30v60M602 30v60"/></svg>'
cover = frame("cover", f'''<div class="label">The Claude team stack</div>
  <h1>50 add-ons that turn<br><span>Claude into a team.</span></h1>
  <p class="tag">One AI lead. Five departments. Fifty specialist tools.</p>
  <p class="sub">Build sites, design products, research markets, create content and run operations, all from one assistant.</p>
  <div class="org"><div class="lead"><small>Team lead</small><div class="lc">{CLAUDE}<b>Claude Code</b></div></div>{wires}<div class="dps">{cards}</div></div>''', swipe=True)

def nav(active):
    items = f'<span class="nv cl">{CLAUDE}Lead</span>' + "".join(f'<span class="nv{" on" if n == active else ""}">{n}</span>' for n, _ in DEPTS)
    return f'<div class="nav">{items}</div>'

def dept(key):
    a, b, sub, start, rows = DATA[key]
    idx = [n for n, _ in DEPTS].index(key)
    ic = dict(DEPTS)[key]
    li = "".join(f'<div class="rw"><img src="assets/ref/{f}.png" alt=""><div class="tx"><p><b>{n}</b><em>{r}</em></p><span>{d}</span></div><i>{start+k}</i></div>' for k, (f, n, r, d) in enumerate(rows))
    return frame("dept", f'''<div class="hd"><div><div class="label"><b class="num">{idx+1}</b>Department {idx+1} of 5 · {key} · 10 add-ons</div>
    <h1>{a} <span>{b}</span></h1><p class="sub">{sub}</p></div>
    <div class="dico">{L(ic, 1.8)}</div></div>
    {nav(key)}<div class="rows">{li}</div>''')

slides = [cover] + [dept(k) for k in ["Design", "Grow", "Make", "Run"]]
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Claude Team Stack</title><style>{CSS}</style></head><body>{"".join(slides)}</body></html>')
print("ok")
