# compositions/captions.html — kinetic VO text: each word appears on its spoken time, the word being spoken is white,
# spoken words settle to pale blue. Chunks of <=5 words (vertical frame), one line, centred at y~1450.
import json, html
P = json.load(open('production/word_times.json'))
chunks = []
for ph in P:
    ws = ph['words']; n = len(ws)
    k = 1 if n <= 5 else (2 if n <= 10 else 3)
    size = -(-n // k)
    for i in range(0, n, size):
        part = ws[i:i + size]
        chunks.append({'words': part, 's': part[0]['t'], 'pe': ph['e']})
for i, c in enumerate(chunks):
    nxt = chunks[i + 1]['s'] if i + 1 < len(chunks) else 94.9
    last = c['words'][-1]['t']
    c['e'] = round(min(nxt - 0.02, max(last + 0.55, c['pe'] + 0.35)), 3)
rows = []
for i, c in enumerate(chunks):
    spans = ' '.join(f'<span class="kw" data-t="{w["t"]}">{html.escape(w["w"])}</span>' for w in c['words'])
    rows.append(f'    <div id="kc-{i:02d}" class="clip kc" data-start="{c["s"] - 0.02:.3f}" data-duration="{c["e"] - c["s"] + 0.02:.3f}"><div class="kc-in">{spans}</div></div>')
out = f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    #root .kc {{ position: absolute; left: 0; top: 1408px; width: 1080px; height: 110px; display: flex; justify-content: center; align-items: center; }}
    #root .kc-in {{ max-width: 900px; text-align: center; white-space: nowrap; font-family: "Poppins", sans-serif; font-weight: 700;
      font-size: 46px; line-height: 1.15; letter-spacing: -0.01em; }}
    #root .kw {{ display: inline-block; margin: 0 0.12em; color: #ffffff; opacity: 0;
      text-shadow: 0 2px 2px rgba(2, 8, 26, 0.55), 0 6px 22px rgba(2, 8, 26, 0.65); }}
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
