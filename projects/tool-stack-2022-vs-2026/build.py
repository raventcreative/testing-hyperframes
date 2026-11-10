# Tool stack 2022 vs 2026 (1080x1350). Render: node render.js | Check: node check-safezone.js
import base64
from pathlib import Path
D = Path(__file__).parent

G = [
 ("Create", [("AI images","Midjourney","GPT Image"),("Video generation","Basic AI video demos","Higgsfield"),
   ("Video editing","Premiere Pro","Claude + Remotion"),("Content creation","Canva","Claude + Higgsfield"),
   ("Presentations","PowerPoint","Claude Slides"),("Writing","ChatGPT","Claude Opus 5.5"),
   ("Marketing copy","Jasper","Claude"),("Voice dictation","Manual typing","Wispr Flow"),("Transcription","Otter.ai","Whisper")]),
 ("Research", [("Web research","Google Search","Claude Sonnet 5.5"),("Deep research","Google Search","Perplexity"),
   ("Meeting notes","Fireflies","Granola"),("Second brain","Google Drive","Obsidian")]),
 ("Build", [("Websites","WordPress","Claude Code"),("AI coding","VS Code","Cursor"),
   ("Database","Google Sheets","Supabase"),("Dashboards","Power BI","Claude Dashboards")]),
 ("Run", [("Automations","Zapier","Claude Cowork"),("AI agents","n8n","Grok Bot"),("Project management","Trello","Linear"),
   ("CRM","HubSpot","Twenty CRM"),("Email marketing","Mailchimp","Kit"),("Lead capture","Google Forms","Tally")]),
]
assert sum(len(r) for _, r in G) == 23

def group(name, rows):
    li = "".join(f'<li><small>{c}</small><p><s>{o}</s><i>→</i><b class="g">{n}</b></p></li>' for c, o, n in rows)
    return f'<div class="grp"><h3><span>{name}</span><em>{len(rows)}</em></h3><ul>{li}</ul></div>'

left = group(*G[0]) + group(*G[1])
nc = sum(n.startswith("Claude") for _, r in G for _, _, n in r)
right = group(*G[2]) + group(*G[3]) + f'<div class="stat"><b class="g">{nc}<span>/23</span></b><p>of my new tools run on <strong>Claude</strong>. One assistant, most of the stack.</p></div>'
logo = "data:image/png;base64," + base64.b64encode((D / "assets/logo.png").read_bytes()).decode()
CSS = (D / "style.css").read_text().replace("LOGO", logo)
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Tool Stack 2022 vs 2026</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><div class="logo"></div></div>
  <div class="label">My tool stack · 23 swaps</div>
  <h1><span class="old">2022</span><i>→</i><span class="g">2026.</span></h1>
  <p class="lede">Same jobs. Different tools. Here’s what I actually switched to.</p>
  <div class="cols"><div>{left}</div><div>{right}</div></div>
  <div class="foot"><b class="g">Save this.</b> Swap one tool this week, not all 23.</div>
</section></body></html>''')
print("ok")
