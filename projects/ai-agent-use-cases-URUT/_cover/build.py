# 64 AI Agent Use Cases: icon-grid cover (1080x1350). Render: node render.js
import base64
from pathlib import Path
D = Path(__file__).parent

def ic(body):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'

P = {
 "video": '<rect x="3" y="8" width="18" height="12" rx="2"/><path d="m3 8 2-4h14l-2 4M8 4l-1.5 4M13 4l-1.5 4M18 4l-1.5 4"/><path d="m10.5 11.5 4 2.5-4 2.5z"/>',
 "ytfind": '<rect x="2.5" y="5" width="13" height="10" rx="2.5"/><path d="m7.5 8 3.5 2-3.5 2z"/><circle cx="17" cy="15.5" r="3.2"/><path d="m19.4 17.9 2.1 2.1"/>',
 "slides": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4M8.5 20h7M6 8h5M6 11h3"/><rect x="13" y="7.5" width="5" height="5" rx=".6"/>',
 "research": '<path d="M4 20V10M8 20V6M12 20v-6"/><circle cx="16.5" cy="11.5" r="3.5"/><path d="m19 14 2.5 2.5"/>',
 "pdf": '<path d="M13 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9z"/><path d="M13 3v6h6"/><path d="M8.5 16v-3h1.2a1 1 0 0 1 0 2H8.5M12.5 13v3h.8a1.5 1.5 0 0 0 0-3zM16.5 13h-1.3v3M15.2 14.5h1"/>',
 "pie": '<path d="M11 3.5a8.5 8.5 0 1 0 8.5 9.5H11z"/><path d="M14 2.5v7.5h7.5A7.5 7.5 0 0 0 14 2.5z"/>',
 "strategy": '<rect x="3" y="3.5" width="18" height="12" rx="1.5"/><path d="M12 15.5V20M8 20h8"/><path d="M6 7l2 2M8 7 6 9"/><circle cx="16" cy="8" r="1.4"/><path d="M8.5 12.5c3 0 4-1 6-3.5"/>',
 "price": '<path d="M20.5 12.5 12 21l-8.5-8.5V4h8.5z"/><circle cx="7.5" cy="8" r="1.2"/><path d="M14.5 11.5c-.5-.8-1.3-1-2-.8-.9.3-1 1.4 0 1.8l1.3.5c1 .4.8 1.6-.2 1.8-.8.2-1.6-.1-2-.8M13 10v-.8M13 15.6v-.8"/>',
 "canvas": '<rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="M3 10h18M9 4v16M15 10v10M9 15h12"/>',
 "puzzle": '<path d="M5 8h3a2 2 0 1 1 4 0h3v3a2 2 0 1 1 0 4v4h-4a2 2 0 1 0-4 0H5v-4a2 2 0 1 0 0-4z"/>',
 "gift": '<rect x="3.5" y="9" width="17" height="11" rx="1"/><path d="M2.5 9h19M12 9v11"/><path d="M12 9C10 5 6.5 5.5 7 7.5S11 9 12 9zM12 9c2-4 5.5-3.5 5-1.5S13 9 12 9z"/>',
 "map": '<path d="m3 6 5.5-2 7 2.5L21 4.5v13.5L15.5 20l-7-2.5L3 19.5z"/><path d="M8.5 4v13.5M15.5 6.5V20"/>',
 "resume": '<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="9" cy="9" r="2.2"/><path d="M5.8 14c.5-1.5 1.7-2.2 3.2-2.2s2.7.7 3.2 2.2M14 8h3.5M14 11h3.5M7 17h10"/>',
 "asset": '<path d="m12 3 8 4v10l-8 4-8-4V7z"/><path d="m4 7 8 4 8-4M12 11v10"/><path d="M14.5 14.5v3M16 14v3M17.5 13.5v3"/>',
 "rivals": '<circle cx="11" cy="11" r="4.5"/><path d="m14.4 14.4 4.6 4.6"/><circle cx="4.5" cy="6" r="1.8"/><circle cx="19.5" cy="6" r="1.8"/><path d="M2 10.5c.4-1.4 1.3-2 2.5-2M22 10.5c-.4-1.4-1.3-2-2.5-2"/>',
 "chief": '<circle cx="12" cy="7" r="3.5"/><path d="M5 21c.6-4.2 3.3-6.5 7-6.5s6.4 2.3 7 6.5"/><path d="m12 14.5-1.2 2.5L12 21l1.2-4z"/>',
 "timeline": '<path d="M2.5 15h19"/><circle cx="6" cy="15" r="1.6"/><circle cx="12" cy="15" r="1.6"/><circle cx="18" cy="15" r="1.6"/><path d="M6 11V6.5M12 11V4.5M18 11V8"/>',
 "calc": '<rect x="5" y="3" width="14" height="18" rx="2"/><rect x="7.5" y="5.5" width="9" height="4" rx=".6"/><path d="M8 13h.01M12 13h.01M16 13h.01M8 16.5h.01M12 16.5h.01M16 16.5h.01" stroke-width="2.4"/>',
 "salary": '<rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M5.5 9v.01M18.5 15v.01" stroke-width="2.4"/>',
 "budget": '<path d="M5 4h10l4 4v12H5z"/><path d="M15 4v4h4"/><path d="M8 17v-3M11 17v-5M14 17v-2"/>',
 "bulb": '<path d="M9 17.5h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1 2V17h5.2v-1.2c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>',
 "receipt": '<path d="M6 3h12v18l-2-1.4-2 1.4-2-1.4-2 1.4-2-1.4L6 21z"/><path d="M9 8h6M9 11.5h6M9 15h3"/>',
 "profile": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="11" r="2"/><path d="M5.5 16c.5-1.6 1.6-2.4 3-2.4s2.5.8 3 2.4M14 10h4.5M14 13.5h3"/>',
 "cal": '<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="M8 14h.01M12 14h.01M16 14h.01M8 17h.01" stroke-width="2.4"/>',
 "dash": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8.5h18M7 16v-3M10.5 16v-5M14 16v-2"/><circle cx="17.5" cy="13.5" r="1.8"/>',
 "doclines": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 11h6M9 14h6M9 17h4"/>',
 "anime": '<circle cx="12" cy="12" r="8.5"/><path d="M5 9.5c2.5.5 5-1 7-4 2 3 4.5 4.5 7 4"/><path d="M9 13.5v1.5M15 13.5v1.5M10.5 17.5c1 .6 2 .6 3 0"/>',
 "avatar": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="10" r="3"/><path d="M6.5 18.5c1-2.5 3-3.6 5.5-3.6s4.5 1.1 5.5 3.6"/>',
 "camera": '<path d="M3 8.5a2 2 0 0 1 2-2h2.5l1.5-2h6l1.5 2H19a2 2 0 0 1 2 2V18a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><circle cx="12" cy="13" r="3.5"/>',
 "sofa": '<path d="M5 11V8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v3"/><path d="M3 12a2 2 0 0 1 4 0v2h10v-2a2 2 0 0 1 4 0v5H3z"/><path d="M5 17v2M19 17v2"/>',
 "gif": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M9.5 10H7.5v4h2v-1.5H8.5M12 10v4M14.5 14v-4h2.5M14.5 12h2"/>',
 "sketch": '<rect x="3" y="4" width="13" height="16" rx="1.5"/><path d="m6 15 3-4 2.5 3 1.5-2"/><path d="m20.5 6.5-7 9-2 .5.5-2 7-9z"/>',
 "book": '<path d="M12 6.5C10 5 7 4.5 3.5 5v13c3.5-.5 6.5 0 8.5 1.5 2-1.5 5-2 8.5-1.5V5C17 4.5 14 5 12 6.5zM12 6.5v13"/>',
 "quote": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/><path d="M11.5 10.5c-.4-.6-1-.8-1.6-.6-.8.2-.8 1.2 0 1.5l1 .4c.8.3.7 1.4-.1 1.5-.6.1-1.2-.1-1.6-.6M10.4 9.4v-.6M10.4 14v-.6M13.5 17h2"/>',
 "funnel": '<path d="M3.5 5h17l-6.5 7.5V19l-4 2v-8.5z"/>',
 "percent": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="m8.5 16.5 7-9"/><circle cx="9" cy="8.5" r="1.4"/><circle cx="15" cy="15.5" r="1.4"/>',
 "sentiment": '<path d="M20.5 11.5a8 8 0 0 1-11.7 7.1L4 20l1.4-4.6a8 8 0 1 1 15.1-3.9z"/><path d="M9 10.5h.01M15 10.5h.01" stroke-width="2.4"/><path d="M9.5 14c1.5 1.2 3.5 1.2 5 0"/>',
 "ad": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m6.5 15 2-6 2 6M7.2 13h2.6M13 9v6h1.5a3 3 0 0 0 0-6z"/>',
 "text": '<path d="M5 6V4.5h14V6M12 4.5v15M9.5 19.5h5"/>',
 "viral": '<rect x="3" y="7" width="12" height="10" rx="2"/><path d="m8 10 3 2-3 2z"/><path d="m16 15 2.5-3.5 2 1.5L22 9M19.5 9H22v2.5"/>',
 "present": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4M8.5 20h7M6.5 13l3-3 2.5 2 5-5"/>',
 "outline": '<path d="M5 5h3M5 10h3M5 15h3M10 5h9M12 10h7M12 15h7M10 20h9"/>',
 "pen": '<path d="M14 3H6v18h12v-6"/><path d="M9 8h5M9 11.5h3"/><path d="m20.5 6-7 7.5-2.5.8.8-2.5 7-7.5z"/>',
 "math": '<path d="M3 13h2.5L8 19l3.5-14H21"/><path d="m14 10 5 5M19 10l-5 5"/>',
 "robot": '<rect x="5" y="8" width="14" height="10" rx="3"/><path d="M12 8V5M12 4.5h.01M9 12.5h.01M15 12.5h.01" stroke-width="2"/><path d="M10 15.5h4M3 12v3M21 12v3"/>',
 "grad": '<path d="M2.5 9 12 4.5 21.5 9 12 13.5z"/><path d="M6.5 11v4.5c1.5 1.5 3.5 2.3 5.5 2.3s4-.8 5.5-2.3V11M21.5 9v5"/>',
 "deck": '<rect x="6" y="3" width="15" height="11" rx="1.5"/><path d="M3 7v12a1.5 1.5 0 0 0 1.5 1.5H18"/><path d="M9.5 7h5M9.5 10h8"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
 "phone": '<rect x="2.5" y="5" width="7" height="14" rx="1.5"/><rect x="14.5" y="5" width="7" height="14" rx="1.5"/><path d="M11 11.5h2M11 13.5h2"/>',
 "chip": '<rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9" y="9" width="6" height="6" rx=".6"/><path d="M9 3v3M12 3v3M15 3v3M9 18v3M12 18v3M15 18v3M3 9h3M3 12h3M3 15h3M18 9h3M18 12h3M18 15h3"/>',
 "color": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3"/><path d="M12 3.5V9M12 15v5.5M3.5 12H9M15 12h5.5M6 6l4 4M14 14l4 4M18 6l-4 4M10 14l-4 4"/>',
 "tower": '<rect x="6" y="2.5" width="12" height="19" rx="1.5"/><circle cx="12" cy="13" r="3"/><path d="M9 6h6M9 8.5h3"/>',
 "camvs": '<rect x="2" y="8" width="8" height="7" rx="1.5"/><circle cx="6" cy="11.5" r="1.8"/><rect x="14" y="8" width="8" height="7" rx="1.5"/><circle cx="18" cy="11.5" r="1.8"/><path d="M11 10.5h2M11 12.5h2"/>',
 "run": '<circle cx="15" cy="4.5" r="1.8"/><path d="m8 21 3-5 3 2v4M9.5 10l3.5-2.5 3 3 3 1M13 7.5 11 13l3 3M6 12l3.5-2"/>',
 "coupon": '<path d="M3 7h18v3.5a1.5 1.5 0 0 0 0 3V17H3v-3.5a1.5 1.5 0 0 0 0-3z"/><path d="m9.5 14.5 5-5"/><circle cx="10" cy="10" r=".9"/><circle cx="14" cy="14" r=".9"/>',
 "trip": '<rect x="4" y="7" width="12" height="13" rx="2"/><path d="M8 7V4.5h4V7M8 20v1.5M12 20v1.5"/><path d="M19.5 9a2.5 2.5 0 0 0-2.5 2.5c0 2 2.5 4.5 2.5 4.5s2.5-2.5 2.5-4.5A2.5 2.5 0 0 0 19.5 9z"/>',
 "code": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8h18M9.5 11.5 7 14l2.5 2.5M14.5 11.5 17 14l-2.5 2.5"/>',
 "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r=".8"/><path d="m12 12 7-7M16.5 4.5 19 5l.5 2.5"/>',
 "deploy": '<path d="M12 15.5c3.5-2 6-6 6.5-11.5-5.5.5-9.5 3-11.5 6.5z"/><path d="m7 10.5-3 1 2.5 2.5M13.5 17l-1 3-2.5-2.5"/><circle cx="14.5" cy="9.5" r="1.4"/><path d="M5.5 18.5c.5-1.5 1.5-2.5 3-2"/>',
 "onboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V2.5h6V4"/><path d="m8.5 10 1.5 1.5 3-3M8.5 15.5l1.5 1.5 3-3M15 10.5h.5M15 16h.5"/>',
}

L = [("AI video generator","video"),("YouTube influencer finder","ytfind"),("AI slides generator","slides"),("Market research tool","research"),
 ("PDF translator","pdf"),("AI market sizing tool","pie"),("Business strategy deck","strategy"),("Startup idea POC","bulb"),
 ("Business canvas maker","canvas"),("Chrome extension builder","puzzle"),("Incentive tracking","gift"),("Client onboarding generator","onboard"),
 ("AI resume builder","resume"),("AI asset tracking system","asset"),("Competitor analysis tool","rivals"),("Chief of staff","chief"),
 ("AI timeline generator","timeline"),("AI salary calculator","salary"),("AI budget tracker","budget"),("GitHub deployment tool","deploy"),
 ("Reimbursement form maker","receipt"),("AI profile builder","profile"),("AI scheduling assistant","cal"),("Billing dashboard builder","dash"),
 ("AI document summariser","doclines"),("AI anime generator","anime"),("AI avatar generator","avatar"),("PhotoStyle insight scanner","camera"),
 ("AI interior design","sofa"),("Video to GIF converter","gif"),("Sketch-to-photo converter","sketch"),("AI story generator","book"),
 ("AI sales quote generator","quote"),("Sales funnel builder","funnel"),("Commission calculator","percent"),("Reddit sentiment analyzer","sentiment"),
 ("Ad copy generator","ad"),("AI text generator","text"),("YouTube viral analysis","viral"),("Marketing deck maker","present"),
 ("Sales territory mapping","map"),("English → Japanese translator","EN→JP"),("Essay outline generator","outline"),("AI essay writer","pen"),
 ("English → Spanish translator","EN→ES"),("AI math solver","math"),("AI writing assistant","robot"),("English → Latin translator","EN→LA"),
 ("AI homework helper","grad"),("Training deck maker","deck"),("Intro email generator","mail"),("Everything calculator","calc"),
 ("Phone comparison","phone"),("PC parts comparison","chip"),("AI color analysis","color"),("PC builder","tower"),
 ("Camera comparison","camvs"),("AI fitness coach","run"),("Coupon finder","coupon"),("AI trip planner","trip"),
 ("AI text summarizer","doclines"),("AI code generator","code"),("AI PDF summarizer","pdf"),("AI lead management tool","target")]
assert len(L) == 64 and all(k in P or "→" in k for _, k in L)

def cell(i, name, k):
    art = f'<span class="tr">{k}</span>' if "→" in k else ic(P[k])
    return f'<div class="c"><div class="h"><em>{i:02d}</em><div class="i">{art}</div></div><span class="nm">{name}</span></div>'

grid = "".join(cell(i + 1, n, k) for i, (n, k) in enumerate(L))
logo = "data:image/png;base64," + base64.b64encode((D / "assets/logo.png").read_bytes()).decode()
CSS = f'''@font-face{{font-family:Poppins;font-weight:400;src:url(assets/fonts/Poppins-Regular.ttf)}}
@font-face{{font-family:Poppins;font-weight:600;src:url(assets/fonts/Poppins-SemiBold.ttf)}}
@font-face{{font-family:Poppins;font-weight:700;src:url(assets/fonts/Poppins-Bold.ttf)}}
:root{{--a:#0a0d2c;--b:#294b77;--grad:linear-gradient(100deg,#0a0d2c,#294b77);--rule:rgba(10,13,44,.11);--dim:#56648a}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Poppins,sans-serif}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:url(assets/bg.png) center/cover;padding:110px}}
.g{{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}}
.logo{{width:300px;height:27px;background:var(--grad);-webkit-mask:url({logo}) left center/contain no-repeat;mask:url({logo}) left center/contain no-repeat}}
.hd{{display:flex;align-items:flex-end;gap:26px;margin-top:26px}}
.n64{{font-size:200px;font-weight:700;line-height:.8;letter-spacing:-12px;padding-right:12px}}
.tt{{padding-bottom:6px}}
.tt b{{display:block;font-size:66px;line-height:.98;letter-spacing:-2.5px;padding-bottom:2px}}
.tt span{{display:block;margin-top:10px;font-size:21px;color:var(--dim)}}
.grid{{margin-top:30px;display:grid;grid-template-columns:repeat(8,minmax(0,1fr));border-radius:18px;overflow:hidden;background:rgba(255,255,255,.82);
  box-shadow:0 0 0 1.5px var(--rule),0 24px 50px -34px rgba(10,13,44,.55)}}
.c{{height:92px;padding:8px 8px 7px;display:flex;flex-direction:column;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule)}}
.c:nth-child(8n){{border-right:0}}.c:nth-last-child(-n+8){{border-bottom:0}}
.h{{display:flex;justify-content:space-between;align-items:flex-start}}
.h em{{flex:none;font-style:normal;font-size:10.5px;font-weight:700;color:#fff;background:var(--grad);border-radius:5px;padding:1px 4px;height:16px;line-height:14px}}
.nm{{margin-top:auto;font-size:11.5px;font-weight:600;line-height:1.16;color:var(--a);letter-spacing:-.1px}}
.i{{display:flex;color:var(--b)}}
.i svg{{width:28px;height:28px}}
.tr{{font-size:11px;font-weight:700;color:var(--b);border:1.5px solid var(--b);border-radius:6px;padding:2px 6px}}
.cta{{position:absolute;left:110px;right:110px;bottom:110px;display:flex;align-items:center;justify-content:center;gap:18px;padding:20px 24px;border-radius:20px;background:var(--grad);color:#fff}}
.cta span{{font-size:28px;font-weight:600}}
.cta b{{font-size:36px;background:#fff;color:var(--a);border-radius:12px;padding:2px 16px}}'''
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>64 AI Agent Use Cases</title><style>{CSS}</style></head><body>
<section class="slide"><div class="logo"></div>
<div class="hd"><div class="n64 g">64</div><div class="tt"><b class="g">AI Agent<br>Use Cases.</b><span>Save this. Pick the ones your business needs.</span></div></div>
<div class="grid">{grid}</div>
<div class="cta"><span>Comment</span><b>“LINK”</b><span>to get the full list</span></div>
</section></body></html>''')
print("ok")
