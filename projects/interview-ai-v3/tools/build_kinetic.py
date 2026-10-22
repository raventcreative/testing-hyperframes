# compositions/captions.html — kinetic VO text: each word appears on its spoken time, the word being spoken is white,
# spoken words settle to pale blue. Chunks of <=5 words (vertical frame), one line, centred at y~1450.
import json, html
P = json.load(open('production/word_times.json'))
chunks = []
MAXC = 20
for ph in P:
    lines = []; cur = []
    for w in ph['words']:
        if cur and len(' '.join(x['w'] for x in cur + [w])) > MAXC:
            lines.append(cur); cur = []
        cur.append(w)
    if cur: lines.append(cur)
    # avoid a lonely last word: pull one word down if the last line has 1 word and the previous has >=3
    if len(lines) >= 2 and len(lines[-1]) == 1 and len(lines[-2]) >= 3:
        lines[-1].insert(0, lines[-2].pop())
    for i in range(0, len(lines), 2):
        grp = lines[i:i + 2]
        chunks.append({'lines': grp, 'words': [w for l in grp for w in l], 's': grp[0][0]['t'], 'pe': ph['e']})
for i, c in enumerate(chunks):
    nxt = chunks[i + 1]['s'] if i + 1 < len(chunks) else 94.9
    last = c['words'][-1]['t']
    c['e'] = round(min(nxt - 0.02, max(last + 0.55, c['pe'] + 0.35)), 3)
rows = []
for i, c in enumerate(chunks):
    ls = ''.join('<div class="kl">' + ' '.join(f'<span class="kw" data-t="{w["t"]}">{html.escape(w["w"])}</span>' for w in l) + '</div>' for l in c['lines'])
    rows.append(f'    <div id="kc-{i:02d}" class="clip kc" data-start="{c["s"] - 0.02:.3f}" data-duration="{c["e"] - c["s"] + 0.02:.3f}"><div class="kc-in">{ls}</div></div>')
out = f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    #root .kc {{ position: absolute; left: 0; top: 1392px; width: 1080px; height: 130px; display: flex; justify-content: center; align-items: flex-start; }}
    #root .kc-in {{ width: 860px; text-align: center; font-family: "Poppins", sans-serif; font-weight: 700;
      font-size: 46px; line-height: 1.2; letter-spacing: -0.01em; }}
    #root .kl {{ display: block; white-space: nowrap; }}
    #root .kw {{ display: inline-block; margin: 0 0.12em; color: #ffffff; opacity: 0;
      text-shadow: 0 2px 3px rgba(2, 8, 26, 0.6), 0 8px 24px rgba(2, 8, 26, 0.7); }}
    #kc-shade {{ position: absolute; left: 0; top: 1330px; width: 1080px; height: 280px;
      background: linear-gradient(180deg, rgba(4, 10, 30, 0) 0%, rgba(4, 10, 30, 0.42) 45%, rgba(4, 10, 30, 0) 100%); }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920" data-layout-allow-caption-zone>
    <div id="kc-shade"></div>
{chr(10).join(rows)}
  </div>
  <script>
    window.__timelines = window.__timelines || {{}};
    const tl = gsap.timeline({{ paused: true }});
    document.querySelectorAll("#root .kc").forEach((chunk) => {{
      const ws = Array.from(chunk.querySelectorAll(".kw"));
      const end = parseFloat(chunk.dataset.start) + parseFloat(chunk.dataset.duration);
      ws.forEach((w, i) => {{
        const t = parseFloat(w.dataset.t);
        const nt = i + 1 < ws.length ? parseFloat(ws[i + 1].dataset.t) : Math.min(end - 0.2, t + 0.45);
        // arrive: blur → sharp, small rise, lands white (the word being spoken)
        tl.fromTo(w, {{ opacity: 0, y: 16, filter: "blur(6px)", color: "#ffffff", scale: 1.08 }},
          {{ opacity: 1, y: 0, filter: "blur(0px)", scale: 1, duration: 0.18, ease: "power3.out" }}, t);
        // once the next word starts, settle to pale blue
        tl.to(w, {{ color: "#8fb3dc", duration: 0.18, ease: "power2.out" }}, Math.max(t + 0.19, nt));
      }});
      tl.to(ws, {{ opacity: 0, filter: "blur(6px)", duration: 0.14, ease: "power2.in" }}, Math.max(0, end - 0.15));
    }});
    window.__timelines["captions"] = tl;
  </script>
</template>
'''
open('compositions/captions.html', 'w').write(out)
print(len(chunks), 'chunks'); [print(f"{c['s']:6.2f}-{c['e']:6.2f}", ' '.join(w['w'] for w in c['words'])) for c in chunks[:12]]
