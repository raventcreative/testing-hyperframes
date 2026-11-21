# AI tools: beginners vs professionals (AIpreneur navy remake, 5 slides 1080x1350, old house style).
# Logos: Simple Icons (CC0) + Lobe Icons (MIT) extruded to 3D (render_logos.js). Icons: Lucide (ISC).
from pathlib import Path
D = Path(__file__).parent
def ic(b): return f'<svg class="ti" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{b}</svg>'
ICON = {
 "code": ic('<path d="m18 16 4-4-4-4"/><path d="m6 8-4 4 4 4"/><path d="m14.5 4-5 16"/>'),
 "clap": ic('<path d="M20.2 6 3 11l-.9-2.4c-.3-1.1.3-2.2 1.3-2.5l13.5-4c1.1-.3 2.2.3 2.5 1.3Z"/><path d="m6.2 5.3 3.1 3.9"/><path d="m12.4 3.4 3.1 4"/><path d="M3 11h18v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>'),
 "cog": ic('<path d="M12 20a8 8 0 1 0 0-16 8 8 0 0 0 0 16Z"/><path d="M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z"/><path d="M12 2v2"/><path d="M12 22v-2"/><path d="m17 20.66-1-1.73"/><path d="M11 10.27 7 3.34"/><path d="m20.66 17-1.73-1"/><path d="m3.34 7 1.73 1"/><path d="M14 12h8"/><path d="M2 12h2"/><path d="m20.66 7-1.73 1"/><path d="m3.34 17 1.73-1"/><path d="m17 3.34-1 1.73"/><path d="m11 13.73-4 6.93"/>'),
 "globe": ic('<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>'),
 "search": ic('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><circle cx="11.5" cy="14.5" r="2.5"/><path d="M13.3 16.3 15 18"/>'),
}
SQ = '<svg class="sq" viewBox="0 0 300 24" preserveAspectRatio="none"><path d="M4 8 C80 4, 200 4, 296 7" /><path d="M90 18 C140 12, 200 13, 236 15"/></svg>'
SLIDES = [
 ("code", "For", "Coding", [("openai", "ChatGPT", "Write, explain & debug code"), ("lovable", "Lovable", "Build an app by chatting")], ("claudecode", "Claude Code", "Writes code, runs tests, opens PRs")),
 ("clap", "Video", "Creation", [("capcut", "CapCut", "Edit, auto captions, templates"), ("hailuo", "Hailuo", "Text or image to AI video")], ("kling", "Kling", "Camera control & motion brush")),
 ("cog", "Task", "Automation", [("zapier", "Zapier", "Connects 9,000+ apps"), ("make", "Make", "Drag-and-drop visual workflows")], ("n8n", "n8n", "Self-hostable, AI agent workflows")),
 ("globe", "Building", "Websites", [("shopify", "Shopify", "A store in hours, no coding"), ("framer", "Framer", "No-code sites, built for designers")], ("replit", "Replit", "Full-stack apps with an AI agent")),
 ("search", "For", "Research", [("googlegemini", "Gemini", "Built into Gmail, Docs & Drive"), ("perplexity", "Perplexity", "Answers with sources")], ("notebooklm", "NotebookLM", "Answers only from your own sources")),
]
def tool(slug, name, why, cls):
    return f'<div class="col {cls}"><div class="bar"><img src="assets/3d/{slug}.png" alt="{name}"></div><div class="nm">{name}</div><div class="why">{why}</div></div>'
S = []
for i, (icon, w1, w2, beg, pro) in enumerate(SLIDES):
    sw = '<div class="swipe">Swipe →</div>' if i == 0 else ''
    S.append(f'''<section class="slide"><div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>
  <div class="hd">{ICON[icon]}<h1>{w1} <span class="hl">{w2}</span></h1><p class="note">Ranked by how easy they are to start with, not how good they are.</p></div>
  <div class="chart">
    <div class="lab lb">Beginners{SQ}</div><div class="lab lp">Professionals{SQ}</div>
    <div class="cols">{"".join(tool(*t, "b") for t in beg)}<div class="gap"></div>{tool(*pro, "p")}</div>
  </div>{sw}</section>''')
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>AI Tools Levels</title><style>{CSS}</style></head><body>{"".join(S)}</body></html>')
print("ok", len(S))
