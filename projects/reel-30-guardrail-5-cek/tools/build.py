"""Assemble index.html from production/index.src.txt: static SFX <audio> tags timed from production/word_timing.json.
The 3D presenter robot ships separately: python3 -I ../../tools/add_robot3d.py .
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
DUR = {"whoosh": 0.574, "pop": 0.72, "click": 0.366, "ping": 1.32, "sparkle": 1.8}
VOL = {"whoosh": 0.06, "pop": 0.045, "click": 0.08, "ping": 0.045, "sparkle": 0.035}
S = lambda s: ph(s)["start"]

tLima, tCek = S("Ini lima pagar"), S("Cek simulasinya")
tP1, tSkor, tInstr = S("Pagar pertama"), S("Tiap balasan dikasih"), S("skornya nentuin")
tP2, tDraft, tPadahal, tDib = S("Pagar kedua"), S("Draft pertama"), S("padahal aturannya"), S("Dibalikin")
tP3, tRef = S("Pagar ketiga"), S("Refund delapan juta")
tP4, tBud, tSis = S("Pagar keempat"), S("Budget iklan"), S("sistemnya berhenti")
tP5, tData, tHarga = S("Pagar kelima"), S("Data pelanggan"), S("harga ngasal")
tCl1, tCl2, tKunci = S("Lima pagar ini"), S("Cuma bikin"), S("Yang pegang kuncinya")
tCta = S("Mau sistem kayak")

tZ1, tW2, tZ3, tW4, tZ5, tSp1, tSp2, tW7, tZ7 = tCek - 0.85, tP2 - 1.2, tP3 - 0.95, tP4 - 1.2, tP5 - 0.95, tRef + 0.75, tHarga + 0.05, tCl1 - 1.1, tCta - 0.78

# one quiet whoosh per transition / 3D swing / reveal
ev = [("whoosh", t) for t in (tZ1 + 0.1, tW2, tZ3, tSp1, tW4, tZ5 + 0.3, tSp2 + 0.95, tW7, tZ7)]
# hook: the send bar, the hold, the five gates arriving
ev += [("pop", 0.2), ("ping", S("mau kirim refund") + 0.1), ("pop", S("Nggak ada yang ngecek") + 0.1),
       ("click", tLima), ("ping", tLima + 0.15)] + [("pop", tLima + 0.45 + k * 0.17) for k in range(5)] + [("pop", tLima + 1.3)]
# P1 feedback loop
ev += [("pop", tP1 + 0.1), ("pop", tP1 + 0.26), ("pop", tP1 + 0.42), ("pop", tP1 + 0.58), ("ping", tSkor - 0.2), ("sparkle", tSkor + 0.2), ("pop", tInstr + 0.6)]
# P2 corrective action
ev += [("pop", tP2 + 0.05), ("pop", tDraft), ("pop", tPadahal - 0.25), ("click", tPadahal + 0.25), ("whoosh", tDib + 0.3), ("ping", tDib + 0.7), ("pop", tDib + 1.1), ("pop", tDib + 1.3)]
# P3 human in the loop
ev += [("pop", tP3 + 0.05), ("pop", tP3 + 0.3), ("pop", tP3 + 0.9), ("ping", tRef - 0.2), ("pop", tRef + 0.65),
       ("pop", tSp1 + 0.7), ("pop", tSp1 + 0.84), ("ping", tSp1 + 1.0)]
# P4 emergency stop
ev += [("pop", tP4 + 0.1), ("pop", tP4 + 0.4), ("pop", tP4 + 0.6), ("click", tSis - 0.06), ("ping", tSis + 0.15), ("pop", tSis + 0.7)]
# P5 guards
ev += [("pop", tP5 + 0.35), ("pop", tP5 + 0.7), ("pop", tData + 0.1), ("pop", tData + 0.36), ("pop", tHarga + 0.1), ("pop", tHarga + 0.36), ("ping", tHarga + 0.68),
       ("pop", tSp2 + 1.5), ("pop", tSp2 + 1.72)]
# closer + CTA
ev += [("pop", tCl1 - 0.1 + k * 0.1) for k in range(5)]
ev += [("pop", tCl1 + 1.15), ("pop", tCl2 + 0.2), ("sparkle", tKunci), ("ping", tKunci + 0.3),
       ("pop", tCta - 0.1), ("click", wt("Klik link", "link"))]

tags = [f'<audio id="sx{i:02d}" class="clip" src="assets/sfx/{k}.wav" data-start="{t:.2f}" data-duration="{DUR[k]}" data-track-index="{10 + i % 4}" data-volume="{VOL[k]}"></audio>'
        for i, (k, t) in enumerate(sorted(ev, key=lambda e: e[1]))]
(P / "index.html").write_text(src.replace("<!--SFX-->", "\n      ".join(tags)))
print("ok", len(tags), "sfx")
