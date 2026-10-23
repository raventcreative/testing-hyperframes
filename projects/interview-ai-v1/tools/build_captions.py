# Generates compositions/captions.html from production/vo_alignment.json (phrase-anchored).
# Long phrases are split into chunks of <=6 words, timed proportionally to syllables.
import json, re, html
d = json.load(open('production/vo_alignment.json'))
def syl(w):
    k = re.sub(r"[^a-z]", "", w.lower())
    return max(1, len(re.findall(r"(ai|au|oi|[aiueo])", k)))
chunks = []
for p in d['phrases']:
    words = p['t'].split()
    n = len(words)
    k = 1 if n <= 6 else (2 if n <= 12 else 3)
    size = -(-n // k)
    parts = [words[i:i + size] for i in range(0, n, size)]
    tot = sum(syl(w) for w in words)
    t = p['s']
    for part in parts:
        dur = (p['e'] - p['s']) * sum(syl(w) for w in part) / tot
        chunks.append([round(t, 2), round(t + dur, 2), ' '.join(part)])
        t += dur
# extend each chunk to just before the next (max +0.6 s) so captions do not flicker
for i, c in enumerate(chunks):
    nxt = chunks[i + 1][0] if i + 1 < len(chunks) else 94.9
    c[1] = round(min(nxt - 0.04, c[1] + 0.6), 2)
rows = []
for i, (s, e, t) in enumerate(chunks):
    rows.append(f'    <div id="cap-{i:02d}" class="clip cap" data-start="{s}" data-duration="{round(e - s, 2)}"><span class="cap-in">{html.escape(t)}</span></div>')
out = f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; pointer-events: none; }}
    #root .cap {{ position: absolute; left: 0; width: 1080px; top: 1418px; display: flex; justify-content: center; }}
    #root .cap-in {{ display: inline-block; max-width: 820px; text-align: center; font-family: "Poppins", sans-serif; font-weight: 400;
      font-size: 38px; line-height: 1.3; color: #eaf4ff; padding: 10px 26px 12px; border-radius: 16px;
      background: rgba(6, 13, 34, 0.62); box-shadow: 0 0 0 1px rgba(170, 215, 255, 0.10); }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920" data-layout-allow-caption-zone>
{chr(10).join(rows)}
  </div>
  <script>
    window.__timelines = window.__timelines || {{}};
    const tl = gsap.timeline({{ paused: true }});
    document.querySelectorAll("#root .cap-in").forEach((el) => {{
      const host = el.parentElement;
      const s = parseFloat(host.dataset.start);
      tl.fromTo(el, {{ opacity: 0, filter: "blur(4px)" }}, {{ opacity: 1, filter: "blur(0px)", duration: 0.14, ease: "power2.out" }}, s);
    }});
    window.__timelines["captions"] = tl;
  </script>
</template>
'''
open('compositions/captions.html', 'w').write(out)
print(len(chunks), 'chunks')
for c in chunks: print(c)
