"""Assemble index.html from index.src.html: robot presenter rig (CSS/markup/JS setup reused from agent-demo-137)
and static SFX <audio> tags timed from production/word_timing.json.
Run: python3 -I tools/build.py <project>"""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
src = (P / "production/index.src.txt").read_text()
ref = (P.parent / "agent-demo-137/index.html").read_text()
lines = ref.split("\n")
c0 = next(i for i, l in enumerate(lines) if l.strip().startswith("#robot { position: absolute;"))
c1 = next(i for i, l in enumerate(lines) if l.strip().startswith("#logo {"))
css = "\n".join(lines[c0:c1])
h0 = ref.index('<div id="robot">'); h1 = ref.index("</div></div></div></div>", h0) + len("</div></div></div></div>")
html = ref[h0:h1]
j0 = ref.index("        /* robot presenter rig v2"); j1 = ref.index("        // gestures:", j0)
js = ref[j0:j1]

T = json.loads((P / "production/word_timing.json").read_text())
W, PH = T["words"], T["phrases"]
ph = lambda s: next(p for p in PH if p["text"].startswith(s))
def wt(s, w):
    k = PH.index(ph(s))
    return next((x[1] for x in W if x[3] == k and x[0].lower().startswith(w.lower())), ph(s)["start"])
DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32}
VOL = {"whoosh": 0.06, "pop": 0.045, "click": 0.08, "ping": 0.045}
VOL["whoosh"] = 0.05
tSim = ph("Gue tunjukin")["start"]; tCta = ph("Mau sistem")["start"]; tJalan = wt("di bisnis lu", "jalan"); t24 = ph("24 jam")["start"]; tTanpa = ph("tanpa nungguin")["start"]
tZ1 = wt("tanpa nungguin", "lu") - 0.25; tAS = ph("Agent sales")["start"]; tZ2 = tAS - 0.62; tProp = wt("Agent sales", "proposal"); tHW = wt("lengkap sama", "harganya")
tBack = ph("Terus nyari")["start"] - 0.25; tLW = wt("Terus nyari", "leads"); tFu = wt("dan follow", "follow"); tOp = ph("Agent operasional")["start"]; tNul = wt("Agent operasional", "nulis")
tOnb = wt("dan onboarding", "onboarding"); tFin = ph("Agent keuangan")["start"]; tSw = wt("Agent keuangan", "tarik") - 0.35; tCoc = ph("terus cocokin")["start"]
tMk = ph("Agent marketing")["start"]; tPec = wt("Agent marketing", "pecah"); tPlat = ph("ke semua platform")["start"]; tZ3 = ph("Dan semuanya")["start"] - 0.78
tPus = wt("ke satu memori", "memori"); tPel = wt("Dia inget", "pelanggan"); tDeal = wt("tiap deal", "deal"); tObr = wt("tiap deal", "obrolan")
tBuk = ph("Bukan workflow")["start"]; tBuk2 = ph("Bukan juga")["start"]; tSini = ph("Di sini")["start"]; tAg = ph("Mau agency")["start"]
tTools = wt("sistemnya dibangun", "tools"); tGaya = wt("dan gaya", "bahasa")
ev = [("pop", 0.05), ("pop", 0.35), ("pop", wt("Gini jadinya", "divisi") - 0.2), ("ping", tJalan - 0.15), ("pop", t24 - 0.15), ("pop", tTanpa - 0.2), ("pop", wt("tanpa nungguin", "nungguin") - 0.1),
      # one quiet whoosh per transition (zoom-in, zoom-in, 3D split, zoom-out, doors, blocks, iris) + pop-out moves
      ("whoosh", tZ1), ("click", wt("Gue tunjukin", "simulasinya")), ("pop", wt("Ini sistem", "sistem")), ("ping", ph("dipegang")["start"] + 0.05),
      ("click", tZ2 - 0.1), ("whoosh", tZ2), ("whoosh", tProp - 0.35), ("pop", tProp + 0.1), ("ping", tHW + 0.55),
      ("whoosh", tBack), ("pop", tLW - 0.2), ("click", tFu - 0.02), ("pop", tFu + 0.2),
      ("click", tOp - 0.45), ("pop", tNul - 0.25), ("ping", tOnb + 1.1),
      ("click", tFin - 0.42), ("whoosh", tSw), ("pop", tCoc - 0.05), ("ping", tCoc + 1.4),
      ("click", tMk - 0.42), ("pop", tPec + 0.35), ("ping", tPlat + 0.05),
      ("whoosh", tZ3), ("ping", tPus - 0.05), ("pop", tPel - 0.25), ("pop", tDeal - 0.25), ("pop", tObr - 0.45),
      ("whoosh", tBuk - 1.08), ("pop", tBuk - 0.15), ("pop", tBuk2 - 0.15), ("ping", tSini - 0.15),
      ("whoosh", tAg - 1.1), ("pop", wt("Mau agency", "agency") - 0.2), ("pop", wt("Mau agency", "toko") - 0.2), ("pop", wt("atau bisnis", "jasa") - 0.2), ("pop", tTools - 0.25), ("pop", tGaya - 0.15),
      ("whoosh", tCta - 1.08), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
out = src.replace("<!--ROBOT_CSS-->", css.strip()).replace("<!--ROBOT_HTML-->", html).replace("/*ROBOT_SETUP*/", js.strip()).replace("<!--SFX-->", "\n      ".join(tags))
(P / "index.html").write_text(out)
print("ok", len(tags), "sfx")
