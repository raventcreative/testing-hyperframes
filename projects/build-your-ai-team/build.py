# Build Your AI Team (1080x1350, dark). Render: node render.js | Check: node check-safezone.js
from pathlib import Path
D = Path(__file__).parent
LV = [
 (5, "Your 24/7 Team", "Agents that work for you", ["Manus", "Hermes", "Claude Duet", "Muse", "Dots"]),
 (4, "Build", "From prompt to app", ["Cursor", "Claude Code", "Lovable", "Replit"]),
 (3, "Research", "Answers with sources", ["ChatGPT", "Gemini", "Perplexity", "NotebookLM"]),
 (2, "Automate", "Notes, voice and workflows", ["Notion AI", "Granola", "Wispr Flow", "Zapier", "n8n"]),
 (1, "Create", "Images, video and voice", ["Midjourney", "Kling", "Runway", "HeyGen", "ElevenLabs", "Suno"]),
]
assert sum(len(t) for *_, t in LV) == 24
floors = "".join(
    f'<div class="fl{" hi" if n == 5 else ""}" style="--i:{5-n}"><div class="lv"><small>Level {n:02d}</small><b>{name}</b><span>{desc}</span></div>'
    f'<div class="chips">{"".join(f"<i>{t}</i>" for t in tools)}</div></div>' for n, name, desc, tools in LV)
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Build Your AI Team</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo.png" alt="AIpreneur"></div>
  <div class="label">The best AI apps in 2026</div>
  <h1>Build your <span>AI team.</span></h1>
  <p class="lede">24 apps, 5 levels. Start at the bottom, hire up one level at a time.</p>
  <div class="stack">{floors}</div>
  <div class="foot"><span class="up">↑</span>Start here: one tool from Level 01 this week.</div>
</section></body></html>''')
print("ok")
