# The AI stack for every job (AIpreneur navy remake, 1 slide 1080x1350).
# Logos: Lobe Icons (MIT, colour) + Simple Icons (CC0, brand hex), flat on white app tiles.
from pathlib import Path
D = Path(__file__).parent
ROWS = [
 ("Websites", "lovable", "Lovable", False),
 ("CRM", "twenty", "Twenty CRM", False),
 ("AI video", "kling", "Kling", False),
 ("Strategy", "claude", "Claude Fable 5.2", True),
 ("Slides & sheets", "claude", "Claude Sonnet 5.5", True),
 ("Images", "nanobanana", "Nano Banana", False),
 ("Video editing", "capcut", "CapCut", False),
 ("Coding", "claudecode", "Claude Code", True),
 ("Animations", "claude", "Claude Opus 5.5", True),
 ("Voice to text", "openai", "Whisper", False),
 ("Note taking", "notion", "Notion", False),
 ("Research", "perplexity", "Perplexity", False),
 ("Automation", "n8n", "n8n", False),
 ("Tasks", "todoist", "Todoist", False),
 ("VPS", "hostinger", "Hostinger", False),
 ("Email", "resend", "Resend", False),
 ("Voice", "elevenlabs", "ElevenLabs", False),
 ("AI assistant", "claude", "Claude", True),
]
rows = "".join(f'<div class="r"><span class="k">{k}</span><span class="tile"><img src="assets/logos/{s}.svg" alt=""></span><span class="pill{" cl" if c else ""}">{n}</span></div>' for k, s, n, c in ROWS)
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>AI Stack 2026</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>
  <h1>One AI tool for <span>every job</span></h1>
  <div class="list">{rows}</div>
</section></body></html>''')
print("ok", len(ROWS))
