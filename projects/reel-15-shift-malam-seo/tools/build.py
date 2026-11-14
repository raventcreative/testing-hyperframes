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
tSim = wt("Coba lihat", "simulasi"); tPes = ph("Pesan ayam")["start"]; tRam = ph("Ramah, cepet")["start"]; tCta = ph("Mau sistem")["start"]
ev = [("pop", 0.05), ("pop", 0.35), ("pop", wt("Admin lu", "telat") + 0.25), ("pop", wt("Admin lu", "telat") + 0.85),
      ("click", wt("orderan kabur", "kabur") - 0.02), ("pop", wt("orderan kabur", "kabur") + 0.28),
      ("whoosh", tSim - 1.15), ("click", tSim), ("whoosh", tSim + 0.28)]
for s0, w0, dt in [("Pelanggan chat", "Halo", -0.15), ("AI admin", "nyapa", -0.05), ("Dia minta", "Dia", 0.05), ("Pesan ayam", "Pesan", -0.05),
                   ("Nambah es teh", "Nambah", -0.05), ("Begitu beres", "Begitu", -0.35), ("pesanan langsung masuk", "pesanan", -0.15)]:
    ev.append(("pop", wt(s0, w0) + dt))
ev += [("whoosh", ph("menu lengkap")["start"] + 0.18), ("ping", wt("langsung dikirim", "dikirim") - 0.1), ("whoosh", tPes - 0.62),
       ("ping", wt("totalnya dihitung", "dihitung") + 0.8), ("whoosh", ph("Pesanan diupdate")["start"] - 0.25), ("ping", wt("totalnya ikut", "totalnya") + 0.8),
       ("whoosh", ph("pesanan langsung masuk")["start"] - 0.2), ("ping", wt("pesanan langsung masuk", "dapur") - 0.2),
       ("pop", wt("dan kecatat", "rekap") - 0.3), ("whoosh", tRam - 0.8), ("pop", tRam - 0.1),
       ("pop", wt("Ramah, cepet", "cepet") - 0.1), ("pop", ph("jalan dua")["start"] - 0.05),
       ("whoosh", tCta - 0.62), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
js = js.replace('ft(rob, { opacity: 0, x: -320 }, { opacity: 1, x: 0, duration: 0.8, ease: "power3.out" }, 0.4);', "st(rob, { opacity: 1 }, 0); // REEL_FX entrance")
out = src.replace("<!--ROBOT_CSS-->", css.strip()).replace("<!--ROBOT_HTML-->", html).replace("/*ROBOT_SETUP*/", js.strip()).replace("<!--SFX-->", "\n      ".join(tags))
(P / "index.html").write_text(out)
print("ok", len(tags), "sfx")
