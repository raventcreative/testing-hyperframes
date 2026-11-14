# AI productivity tools (AIpreneur, transparent background). Tool logos cropped from the user's reference; line icons: Lucide (ISC).
import re
from pathlib import Path
D = Path(__file__).parent
def L(n, w=2):
    s = re.sub(r"<!--.*?-->", "", (D / f"assets/icons/{n}.svg").read_text(), flags=re.S)
    return re.sub(r'class="[^"]*"|width="24"|height="24"', "", s).replace('stroke-width="2"', f'stroke-width="{w}"')
C = [
 ("message-circle", "Chatbots", [("chatgpt","ChatGPT"),("claude","Claude"),("gemini","Gemini"),("perplexity","Perplexity"),("deepseek","DeepSeek"),("grok","Grok"),("copilot","Copilot")]),
 ("code-xml", "Coding", [("cursor","Cursor"),("lovable","Lovable"),("replit","Replit"),("bolt","Bolt"),("ghcopilot","GitHub Copilot"),("windsurf","Windsurf"),("qodo","Qodo")]),
 ("image", "Image", [("midjourney","Midjourney"),("firefly","Firefly"),("ideogram","Ideogram"),("flux","FLUX"),("recraft","Recraft"),("leonardo","Leonardo"),("dalle","DALL·E")]),
 ("clapperboard", "Video", [("runway","Runway"),("kling","Kling"),("descript","Descript"),("luma","Luma"),("pika","Pika"),("krea","Krea"),("ltx","LTX Studio")]),
 ("pen-line", "Writing", [("grammarly","Grammarly"),("quillbot","QuillBot"),("jasper","Jasper"),("copyai","Copy.ai"),("writesonic","Writesonic"),("sudowrite","Sudowrite"),("rytr","Rytr")]),
 ("presentation", "Presentations", [("gamma","Gamma"),("beautiful","Beautiful.ai"),("pitch","Pitch"),("plus","Plus AI"),("popai","PopAi"),("presentationsai","Presentations.AI")]),
 ("workflow", "Workflows", [("zapier","Zapier"),("make","Make"),("n8n","n8n"),("monday","monday.com"),("wrike","Wrike"),("integrately","Integrately")]),
 ("users", "Meetings", [("fireflies","Fireflies"),("otter","Otter.ai"),("fathom","Fathom"),("krisp","Krisp"),("fellow","Fellow"),("avoma","Avoma")]),
 ("calendar-clock", "Scheduling", [("motion","Motion"),("reclaim","Reclaim"),("calendly","Calendly"),("clockwise","Clockwise"),("taskade","Taskade"),("trevor","Trevor AI")]),
 ("mail", "Email", [("superhuman","Superhuman"),("shortwave","Shortwave"),("mailmaestro","MailMaestro"),("friday","Friday"),("cliipt","Cliipt")]),
 ("sheet", "Spreadsheets", [("rowsai","Rows AI"),("gigasheet","Gigasheet"),("formulabot","Formula Bot"),("sheetai","SheetAI"),("bricks","Bricks")]),
]
n_tools = sum(len(t) for *_, t in C)
rows = "".join(f'''<div class="r"><div class="c"><span class="ci">{L(ic)}</span><b>{name}</b></div>
 <div class="ts">{"".join(f'<div class="t"><img src="assets/apps/{f}.png" alt=""><span>{n}</span></div>' for f, n in tools)}</div></div>''' for ic, name, tools in C)
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>AI Productivity Tools</title><style>{CSS}</style></head><body>
<section class="slide"><div class="hd"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"><span class="cnt">Save this</span></div>
 <h1>AI productivity <span>tools.</span></h1><p class="sub">{n_tools} picks, sorted by the job you need done.</p>
 <div class="rows">{rows}</div></section></body></html>''')
print("ok", n_tools)
