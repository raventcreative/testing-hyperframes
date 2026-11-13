# Best AI apps 2027 (AIpreneur navy, 2 slides). App icons cropped from the user's reference; line icons: Lucide (ISC).
import re
from pathlib import Path
D = Path(__file__).parent
def L(n, w=2):
    s = re.sub(r"<!--.*?-->", "", (D / f"assets/icons/{n}.svg").read_text(), flags=re.S)
    return re.sub(r'class="[^"]*"|width="24"|height="24"', "", s).replace('stroke-width="2"', f'stroke-width="{w}"')
def frame(cls, body, swipe=False):
    sw = '<div class="bot">Swipe →</div>' if swipe else ''
    return f'<section class="slide {cls}"><img class="logo" src="assets/logo_white.png" alt="AIpreneur">{body}{sw}</section>'
CAT = [
 ("sparkles", "AI assistants", "Research · plan · write", [("chatgpt","ChatGPT"),("claude","Claude"),("gemini","Gemini"),("perplexity","Perplexity"),("grok","Grok"),("copilot","Copilot")]),
 ("code-xml", "Build & code", "Apps · sites · deploy", [("claudecode","Claude Code"),("cursor","Cursor"),("lovable","Lovable"),("replit","Replit"),("bolt","Bolt.new"),("windsurf","Windsurf")]),
 ("clapperboard", "Video & audio", "Shoot · edit · voice", [("veo","Veo 3"),("flow","Google Flow"),("kling","Kling"),("runway","Runway"),("pika","Pika"),("elevenlabs","ElevenLabs")]),
 ("paintbrush", "Design & visuals", "Ideate · design · edit", [("canva","Canva"),("midjourney","Midjourney"),("higgsfield","Higgsfield"),("figma","Figma"),("firefly","Firefly"),("ideogram","Ideogram")]),
 ("layers", "Productivity", "Notes · tasks · inbox", [("notion","Notion"),("granola","Granola"),("clickup","ClickUp"),("superhuman","Superhuman"),("raycast","Raycast"),("otio","Otio")]),
 ("workflow", "Automation", "Connect · scale", [("n8n","n8n"),("zapier","Zapier"),("make","Make"),("lindy","Lindy AI"),("apify","Apify"),("firebase","Firebase")]),
]
rows = "".join(f'''<div class="cr"><div class="ch"><span class="ci">{L(ic)}</span><div><b>{t}</b><small>{s}</small></div></div>
  <div class="apps">{"".join(f'<div class="ap"><img src="assets/apps/{f}.png" alt=""><span>{n}</span></div>' for f, n in apps)}</div></div>''' for ic, t, s, apps in CAT)
s1 = frame("s1", f'''<div class="label">The creator & marketer toolkit</div>
  <h1>The best AI apps<br><span>for 2027.</span></h1>
  <p class="lede">36 apps, 6 jobs. You don’t need all of them, just one per job.</p>
  <div class="rows">{rows}</div>''', swipe=True)
PB = [
 ("laptop", "Create faster", "Write, design, edit and produce in less time.", "play", "Turn one product photo into a 15-second Reel for your shop.", "Veo 3 + ElevenLabs"),
 ("trending-up", "Be more productive", "Plan, organize and automate the busywork.", "calendar-check", "Run your content calendar and team tasks in one place.", "Notion + Granola"),
 ("sparkles", "Unlock creativity", "Fresh ideas, visuals and brand assets on demand.", "image", "Make a full campaign visual set for a Lebaran promo.", "Midjourney + Canva"),
 ("code-xml", "Build & automate", "Tools, workflows and agents, with little or no code.", "layers", "Auto-reply WhatsApp leads and log them in one sheet.", "n8n + Claude"),
 ("rocket", "Grow your business", "Research, analyze and spot new opportunities.", "target", "Check what competitors sell and price before you launch.", "Perplexity + Gemini"),
]
pb = "".join(f'''<div class="pr"><div class="pl"><span class="pi">{L(i)}</span><b>{t}</b></div>
  <div class="pu"><small>Use it for</small><p>{u}</p></div>
  <div class="pe"><span class="ei">{L(ei)}</span><div><small>Real example</small><p>{e}</p><em>{tools}</em></div></div></div>''' for i, t, u, ei, e, tools in PB)
s2 = frame("s2", f'''<div class="label">A simple playbook</div>
  <h1>How to use these<br><span>apps in 2027.</span></h1>
  <div class="pbs">{pb}</div>
  <div class="tip">{L("lightbulb")}<p><b>Pro tip:</b> combine 2–3 tools from different rows to build one complete content and sales system.</p></div>''')
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Best AI Apps 2027</title><style>{CSS}</style></head><body>{s1}{s2}</body></html>')
print("ok")
