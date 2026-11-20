#!/usr/bin/env python3
"""AIpreneur closing (CTA) slide for every feed carousel — client rule 2026-11-20.
Usage: python3 closing.py --n 6 --total 6 --out projects/<p>/out/stills/SLIDE_06.png [--mp4 path.mp4]   (copy is fixed — client rule: do NOT translate or reword)
Renders PNG (final state) and optionally a 6 s MP4 (elements rise in, cursor taps Follow -> Mengikuti)."""
import argparse, pathlib, re, subprocess, json
HERE = pathlib.Path(__file__).resolve().parent
BRAND = (HERE / "../../../../brand").resolve()

COPY = {
 "en": dict(h='Your business<br>deserves a<br><u>better agent.</u>', sub="Less manual work. More business growth.",
            pills=["Custom Software", "AI Agents", "Automation"], who="Follow for AI agents and automation",
            follow="Follow", following="Following", cta="Get your custom agentic software. Tap the link in our bio."),
}

def ic(name, size):
    s = (HERE / f"{name}.svg").read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S).strip()
    s = re.sub(r"<svg[^>]*>", lambda m: re.sub(r'\s(width|height|class)="[^"]*"', "", m.group(0)), s, count=1)
    return s.replace("<svg", f'<svg width="{size}" height="{size}"', 1)

def html(n, total, lang):
    c, B = COPY[lang], BRAND.as_uri()
    dots = "".join(f'<i class="{"on" if k == n else "done" if k < n else ""}"></i>' for k in range(1, total + 1))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Poppins;font-weight:700;src:url({B}/fonts/poppins-latin-700-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:400;src:url({B}/fonts/inter-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--ink:#0a0d2c;--blue:#294b77;--soft:rgba(10,13,44,.74);--line:rgba(41,75,119,.28);--grad:linear-gradient(100deg,#0a0d2c,#294b77)}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:url({B}/feed/bg-white.png) center/cover;font-family:Inter;color:var(--ink)}}
.logo{{position:absolute;left:100px;top:92px;height:34px}}
.count{{position:absolute;right:100px;top:94px;font-size:26px;letter-spacing:.06em;color:var(--soft)}}
.c{{position:absolute;left:100px;right:100px;top:290px}}
h1{{font-family:Poppins;font-weight:700;font-size:80px;line-height:1.12;letter-spacing:-.015em;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;padding-bottom:8px}}
h1 u{{text-decoration:underline;text-decoration-color:#0a0d2c;text-decoration-thickness:7px;text-underline-offset:10px}}
.sub{{font-size:34px;color:var(--soft);margin-top:30px}}
.pills{{display:flex;gap:12px;margin-top:34px}}
.pills span{{font-size:25px;padding:10px 22px;border:2px solid var(--blue);border-radius:40px;opacity:.95}}
.acc{{display:flex;align-items:center;gap:24px;margin-top:48px;padding:28px 32px;background:rgba(255,255,255,.94);border:2px solid var(--line);border-radius:30px;box-shadow:0 14px 40px rgba(41,75,119,.08)}}
.av{{width:96px;height:96px;border-radius:50%;background:var(--grad);display:flex;align-items:center;justify-content:center;flex:none}}
.av img{{width:52px}}
.acc b{{display:block;font-family:Poppins;font-size:33px}}
.acc small{{font-size:23px;color:var(--soft)}}
.fol{{margin-left:auto;position:relative;height:64px;min-width:164px;border-radius:40px;font-family:Poppins;font-weight:700;font-size:28px;display:flex;align-items:center;justify-content:center;gap:8px;padding:0 34px;flex:none}}
.fol.a{{background:var(--grad);color:#fff}}
.fol.b{{position:absolute;right:0;top:0;height:64px;padding:0 22px;font-size:25px;white-space:nowrap;background:#fff;color:var(--ink);border:2px solid var(--line);opacity:0}}
.cta{{display:flex;align-items:center;gap:20px;margin-top:38px;font-size:28px;color:var(--soft)}}
.cta .dn{{width:60px;height:60px;border-radius:50%;background:var(--grad);color:#fff;display:flex;align-items:center;justify-content:center;flex:none}}
.dots{{position:absolute;left:100px;bottom:100px;display:flex;gap:9px;align-items:center}}
.dots i{{width:10px;height:10px;border-radius:5px;background:rgba(41,75,119,.25)}}.dots i.done{{background:var(--blue)}}.dots i.on{{width:38px;background:var(--blue)}}
.cur{{position:absolute;left:0;top:0;filter:drop-shadow(0 3px 6px rgba(0,0,0,.25));opacity:0}}
.cur path{{fill:#0a0d2c;stroke:#fff;stroke-width:1.4}}
</style></head><body><section class="slide" id="s">
<img class="logo" src="{B}/feed/logo-dark.png"><div class="count">{n:02d} / {total:02d}</div>
<div class="c"><h1 class="r">{c["h"]}</h1><p class="sub r">{c["sub"]}</p>
<div class="pills r">{"".join(f"<span>{p}</span>" for p in c["pills"])}</div>
<div class="acc r"><div class="av"><img src="{B}/feed/a-mark-white.png"></div><div><b>@aipreneur.automation</b><small>{c["who"]}</small></div>
<div class="fol a" id="fol">{c["follow"]}<div class="fol b" id="fol2">{ic("check", 26)}{c["following"]}</div></div></div>
<div class="cta r"><span class="dn">{ic("arrow-down", 30)}</span><span>{c["cta"]}</span></div></div>
<div class="dots">{dots}</div><div class="cur" id="cur">{ic("mouse-pointer-2", 46)}</div></section>
<script>
const cl=(x)=>Math.min(1,Math.max(0,x)),ease=x=>{{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}},seg=(t,a,b)=>cl((t-a)/(b-a));
const rs=[...document.querySelectorAll('.r')],fol=document.getElementById('fol'),f2=document.getElementById('fol2'),cur=document.getElementById('cur');
const fb=()=>{{const s=document.getElementById('s').getBoundingClientRect(),b=fol.getBoundingClientRect();return [b.left-s.left+b.width*.55,b.top-s.top+b.height*.6]}};
window.setT=t=>{{rs.forEach((e,i)=>{{const p=ease(seg(t,.1+i*.22,.7+i*.22));e.style.opacity=p;e.style.transform=`translateY(${{(1-p)*26}}px)`}});
 const [x,y]=fb(),m=ease(seg(t,2.2,3.0)),cx=x+(1-m)*180,cy=y+(1-m)*260,clk=3.15;
 cur.style.opacity=seg(t,2.1,2.3)*(1-seg(t,4.4,4.7));const d=Math.abs(t-clk);
 cur.style.transform=`translate(${{cx-8}}px,${{cy-8}}px) scale(${{d<.08?.82+d*2.2:1}})`;cur.style.transformOrigin='8px 8px';
 f2.style.opacity=t>=clk?1:0;fol.style.transform=`scale(${{d<.12?.94+d*.5:1}})`}};
window.final=()=>{{setT(10);document.getElementById('cur').style.opacity=0;f2.style.opacity=0}};
</script></body></html>'''

if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("--n", type=int, required=True); a.add_argument("--total", type=int, required=True)
    a.add_argument("--out", required=True); a.add_argument("--mp4"); a.add_argument("--lang", default="en", choices=["en"])
    o = a.parse_args()
    out = pathlib.Path(o.out).resolve(); out.parent.mkdir(parents=True, exist_ok=True)
    page = out.with_suffix(".closing.html"); page.write_text(html(o.n, o.total, o.lang))
    subprocess.run(["node", str(HERE / "render_closing.cjs"), str(page), str(out), str(pathlib.Path(o.mp4).resolve()) if o.mp4 else ""], check=True)
    page.unlink()
