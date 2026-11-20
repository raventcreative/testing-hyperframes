# Instagram growth cheat sheet (AIpreneur navy, 1080x1350). Render: node render.js | Check: node check-safezone.js
from pathlib import Path
D = Path(__file__).parent
steps = ["Research", "Create", "Post", "Measure", "Double down", "Repurpose", "Test"]
sys_html = '<s>›</s>'.join(f'<span><i>{i}</i>{t}</span>' for i, t in enumerate(steps, 1))
ang = [("Educate", "Teach one useful thing"), ("Inspire", "Show what is possible"), ("Relate", "Make them feel seen"),
       ("Prove", "Results and real stories"), ("Entertain", "Make them watch and share")]
ang_html = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in ang)
pyr = ["Follows + DMs", "Profile visits", "Shares", "Saves", "Watch time", "Reach"]
widths = [52, 60, 68, 76, 88, 100]
pyr_html = "".join(f'<div style="width:{w}%">{t}</div>' for t, w in zip(pyr, widths))
wk = [("MON", "Check analytics"), ("TUE", "Research outliers"), ("WED", "Create"), ("THU", "Publish + reply"),
      ("FRI", "Repurpose"), ("SAT", "Review"), ("SUN", "Plan next week")]
wk_html = "".join(f"<div><b>{d}</b>{t}</div>" for d, t in wk)
stop = ["Posting without checking data", "Chasing a new idea daily", "Copying instead of adapting",
        "Hours editing low-value posts", "Changing niche every week", "Testing a format once, then quitting"]
stop_html = "".join(f"<span>{s}</span>" for s in stop)
CSS = (D / "style.css").read_text()
(D / "carousel.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Instagram Growth Cheat Sheet</title><style>{CSS}</style></head><body>
<section class="slide">
  <div class="top"><img class="logo" src="assets/logo_white.png" alt="AIpreneur"></div>
  <div class="hd"><h1>Instagram growth<br><span>cheat sheet.</span></h1><div class="tag">What to do when you want<br>your account to grow.<b>Stop guessing. Use your data.</b></div></div>
  <div class="sys">{sys_html}</div>
  <div class="g">
    <div class="c w"><h3><i>01</i>The content system</h3>
      <p>Your job is <b>not</b> to find new ideas. Pick <b>who you help</b> + <b>what you know</b> (e.g. home bakers + pricing), name <b>one clear problem</b> (“I never know my real profit”), then talk about it 5 ways:</p>
      <div class="ang">{ang_html}</div></div>
    <div class="c"><h3><i>02</i>Find what already works</h3>
      <p>Follow <b>5–10 accounts</b> in your niche → open their best posts → spot the <b>outliers</b> (far above their normal views, saves or shares) → study → adapt.</p>
      <div class="ch"><span class="on">Hook</span><span>Format</span><span>Topic</span><span>Delivery</span><span>Payoff</span><span>CTA</span></div>
      <p>Study the structure. <b>Never copy the script.</b></p></div>
    <div class="c"><h3><i>03</i>4 formats to keep testing</h3>
      <p><b>Reels:</b> new audiences, quick tips, demos.<br><b>Carousels:</b> steps, frameworks, saves.<br><b>Image posts:</b> opinions, quotes, one idea.<br><b>Stories:</b> polls, behind the scenes, trust.</p></div>
    <div class="c"><h3><i>04</i>Hooks that stop the scroll</h3>
      <p><b>Curiosity:</b> “You’re probably pricing this wrong…”<br><b>Contrarian:</b> “Stop posting daily if…”<br><b>Result:</b> “How I got ___ without ___”<br><b>Direct:</b> “If your reach is stuck, read this.”</p>
      <p>Win the first 2 seconds: <b>what they see, read, hear.</b></p></div>
    <div class="c"><h3><i>05</i>What your analytics tell you</h3>
      <div class="pyr">{pyr_html}</div>
      <p style="text-align:center">Don’t just look at views.</p></div>
    <div class="c"><h3><i>06</i>Double down + test</h3>
      <div class="split"><div class="a"><b>70%</b>repeat winning topics, hooks, formats</div><div class="b"><b>30%</b>test new</div></div>
      <p>One post working once is a <b>signal</b>. One idea → reel, carousel, story, checklist. Never start from a blank page.</p></div>
    <div class="c"><h3><i>07</i>The weekly workflow</h3>
      <div class="wk">{wk_html}</div></div>
    <div class="c w"><h3><i>08</i>Stop doing these</h3><div class="stop">{stop_html}</div></div>
  </div>
  <p class="end"><b>You don’t need more ideas.</b> You need a better system for the ideas you already have.</p>
</section></body></html>''')
print("ok")
