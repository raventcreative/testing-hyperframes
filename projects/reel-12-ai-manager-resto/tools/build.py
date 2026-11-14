"""Assemble index.html from production/index.src.txt: static SFX <audio> tags timed from production/word_timing.json.
(3D robot reel: the robot is wired in the source; ship it with tools/add_robot3d.py.)
Run: python3 -I tools/build.py <project>"""
import json, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
src = (P / "production/index.src.txt").read_text()
T = json.loads((P / "production/word_timing.json").read_text())
W, PH = T["words"], T["phrases"]
ph = lambda s: next(p for p in PH if p["text"].startswith(s))
def wt(s, w):
    k = PH.index(ph(s))
    return next((x[1] for x in W if x[3] == k and x[0].lower().startswith(w.lower())), ph(s)["start"])
DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32, "sparkle": 1.2}
VOL = {"whoosh": 0.055, "pop": 0.04, "click": 0.08, "ping": 0.04, "sparkle": 0.035}
S = lambda p: ph(p)["start"]
tCoba, tJad, tSeh, tRev, tJ3, tTapi, tKir, t11, tKirim, tBes, tSem, tCta = (S(x) for x in
    ["Coba lihat", "Agent jadwal", "Seharian", "Agent review", "Jam tiga", "Tapi AI", "langsung dikirim", "Jam sebelas", "kirim satu", "Besok", "semuanya", "Mau sistem"])
tHab = wt("nemu cabai", "hampir")
ev = [("pop", 0.05), ("pop", S("resto lu") - 0.12), ("pop", wt("resto lu", "AI") + 0.08), ("pop", S("Padahal") - 0.08), ("pop", wt("Padahal", "tidur") + 0.12),
      ("whoosh", tCoba - 0.22),
      ("pop", wt("Pertama", "bangunin") + 0.4), ("whoosh", S("Dia baca") - 0.42), ("pop", wt("nemu cabai", "cabai")), ("pop", wt("nemu cabai", "ayam")),
      ("whoosh", tHab + 0.08), ("ping", wt("langsung order", "supplier") - 0.15),
      ("whoosh", tJad - 1.13), ("whoosh", tJad + 0.42), ("pop", wt("Agent jadwal", "reservasi") - 0.15), ("pop", wt("sama cuaca", "cuaca") - 0.25), ("pop", S("Jumat") - 0.2),
      ("pop", S("jadi dia minta") - 0.05), ("ping", wt("jadi dia minta", "lebih") - 0.1),
      ("whoosh", tSeh - 0.55), ("pop", wt("Seharian", "bales") - 0.1), ("pop", wt("Seharian", "bales") + 0.32), ("pop", wt("Seharian", "bales") + 0.74),
      ("whoosh", tRev - 0.42), ("pop", wt("Agent review", "bales") - 0.1), ("pop", wt("Agent review", "bales") + 0.3), ("ping", wt("yang bintang", "dilempar") - 0.25),
      ("whoosh", tJ3 - 0.8), ("pop", S("bikin promo") - 0.2), ("pop", wt("buat Selasa", "Selasa")),
      ("whoosh", tTapi - 0.05), ("pop", wt("jadi ditolak", "ditolak") + 0.04), ("whoosh", S("Diganti") + 0.02),
      ("pop", S("disetujui") + 0.04), ("sparkle", S("disetujui") + 0.1), ("whoosh", tKir + 0.1), ("ping", tKir + 1.2),
      ("whoosh", t11 - 1.16), ("whoosh", wt("agent keuangan", "keuangan") - 0.15), ("pop", wt("agent keuangan", "tutup") - 0.05), ("ping", tKirim - 0.25),
      ("whoosh", tBes - 0.25), ("whoosh", tSem - 0.15), ("whoosh", tCta - 0.55), ("click", wt("Klik link", "link"))]
tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
out = src.replace("<!--SFX-->", "\n      ".join(tags))
(P / "index.html").write_text(out)
print("ok", len(tags), "sfx")
