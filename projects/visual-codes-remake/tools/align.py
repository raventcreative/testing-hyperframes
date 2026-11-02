"""VO timing master without network ASR (Hugging Face is blocked here).
The ElevenLabs read pauses at every comma/period, so speech segments (energy > -40 dB, gaps >= 90 ms) map 1:1 to
script phrases (MAP below, checked by ear-free counting: 4 hook segs, 15 x (name, explanation), CTA).
Inside a phrase, word boundaries = syllable-weighted split, each boundary snapped to the lowest-energy 10 ms frame
within +-70 ms. Phones = letters spread evenly over their word (the lip track is gated by the VO energy anyway).
Outputs: production/word_timing.json, vendor/vo_words.js (VO_WORDS, VO_PHONES, VO_ENV, VO_PHR)
Run: python3 -I tools/align.py <project>"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np
P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
AUDIO = P / "assets/audio/vo_tight.wav"
CODES = [("blueprint", "Blueprint,", "bedah sistem kayak gambar teknik."), ("roadmap", "Roadmap,", "urutan belajar dari nol."),
         ("handwritten", "Handwritten,", "catatan tulisan tangan."), ("decision-matrix", "Decision matrix,", "bandingin pilihan sekali lihat."),
         ("flowchart", "Flowchart,", "alur proses step by step."), ("infographic", "Infographic,", "data padat jadi gampang."),
         ("canvas", "Canvas,", "semua poin dalam satu halaman."), ("layers", "Layers,", "bongkar lapis demi lapis."),
         ("cycle", "Cycle,", "proses berulang jadi satu putaran."), ("diagram", "Diagram,", "bagian lengkap sama labelnya."),
         ("sketchnotes", "Sketchnotes,", "doodle yang bikin nempel."), ("iceberg", "Iceberg,", "yang kelihatan versus yang tersembunyi."),
         ("exploded-view", "Exploded view,", "komponen dipisah satu-satu."), ("tree", "Tree,", "dari akar sampai cabang."),
         ("timeline", "Timeline,", "sejarah jadi garis waktu.")]
EXPL_SEGS = {7: [19, 20], 13: [32, 33]}          # code index -> explanation spans two segments
PHR = [("hook", "Lu masih belajar dari teks panjang di ChatGPT?", [0]),
       ("hook", "Pantes nggak nempel. Ketik salah satu dari lima belas kode ini,", [1]),
       ("hook", "materi apa pun", [2]), ("hook", "langsung jadi visual.", [3])]
for i, (k, name, ex) in enumerate(CODES):
    PHR.append(("name", name, [4 + 2 * i if i < 8 else None]))
    PHR.append(("expl", ex, None))
# explicit segment map (index 36 is a breath, skipped)
seg_of = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17],
          [18], [19, 20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32, 33], [34], [35]]
PHR = PHR[:4] + [p for i in range(15) for p in (PHR[4 + 2 * i], PHR[5 + 2 * i])]
PHR = [(k, txt, seg_of[j]) for j, (k, txt, _) in enumerate(PHR)]
PHR += [("cta", "Komen PROMPT,", [37]), ("cta", "gue kirim lima belas full prompt-nya langsung ke DM lu.", [38])]
KEY = {"teks", "panjang", "nempel.", "lima", "belas", "kode", "visual.", "PROMPT,", "DM"} | {c[1].split()[0].strip(",") for c in CODES}
PRON = {"blueprint": "bluprin", "roadmap": "rodmep", "handwritten": "henriten", "decision": "disisyen", "matrix": "metriks",
        "flowchart": "flocart", "infographic": "infografik", "layers": "leyers", "cycle": "saikel", "sketchnotes": "sketnots",
        "iceberg": "aisberg", "exploded": "eksploded", "view": "fiu", "tree": "tri", "timeline": "taimlain", "doodle": "dudel",
        "chatgpt": "cetgipiti", "step": "step", "by": "bai", "full": "ful", "promptnya": "promnya", "prompt": "promt", "dm": "diem", "gue": "gue"}

raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(AUDIO), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.int16).astype(float) / 32768
hop = 160; n = len(a) // hop; DUR = len(a) / 16000
db = 20 * np.log10(np.sqrt(np.mean(a[: n * hop].reshape(n, hop) ** 2, axis=1)) + 1e-6)
sp = db > -40; segs = []; i = 0
while i < n:
    if sp[i]:
        j = i
        while j < n and (sp[j] or any(sp[j:j + 9])): j += 1
        segs.append((i / 100, j / 100)); i = j
    else: i += 1
assert len(segs) == 39, len(segs)

def spoken(w):
    k = re.sub(r"[^a-z0-9]", "", w.lower())
    return "".join(ch for ch in PRON.get(k, k) if "a" <= ch <= "z")
def syl(s):
    return max(1, len(re.findall(r"[aiueo]+", s)))

words, phones, phr_out = [], [], []
for kind, txt, sidx in PHR:
    s0, e0 = segs[sidx[0]][0], segs[sidx[-1]][1]
    ws = txt.split(); sps = [spoken(w) for w in ws]; wt = np.array([syl(s) + 0.35 for s in sps])
    cum = np.concatenate([[0], np.cumsum(wt)]) / wt.sum()
    bounds = [s0 + c * (e0 - s0) for c in cum]
    # multi-segment phrase: put the boundary at the inner gap
    if len(sidx) == 2:
        g = (segs[sidx[0]][1] + segs[sidx[1]][0]) / 2
        k = int(np.argmin([abs(b - g) for b in bounds[1:-1]])) + 1; bounds[k] = g
    for k in range(1, len(bounds) - 1):
        f0, f1 = int((bounds[k] - 0.07) * 100), int((bounds[k] + 0.07) * 100)
        bounds[k] = (f0 + int(np.argmin(db[f0:f1 + 1]))) / 100
    first = len(words)
    for k, w in enumerate(ws):
        st, en = round(bounds[k], 3), round(bounds[k + 1] - 0.01, 3)
        words.append([w, st, en, 1 if w.strip(",.?") in {x.strip(",.?") for x in KEY} or kind == "name" else 0, sps[k]])
        L = len(sps[k]); step = (en - st) / max(1, L)
        for c, ch in enumerate(sps[k]):
            phones.append([ch, round(st + c * step, 3), round(st + (c + 1) * step, 3), len(words) - 1])
    phr_out.append({"kind": kind, "text": txt, "start": round(s0, 3), "end": round(e0, 3), "w0": first, "w1": len(words) - 1})

codes = []
for i, (key, name, ex) in enumerate(CODES):
    nm, ep = phr_out[4 + 2 * i], phr_out[5 + 2 * i]
    codes.append({"i": i + 1, "key": key, "name": nm["start"], "nameEnd": nm["end"], "expl": ep["start"], "explEnd": ep["end"], "text": ex})
info = {"dur": round(DUR, 3), "hook": phr_out[:4], "codes": codes, "cta": phr_out[-2:],
        "words": {w[0] + "@" + str(k): [w[1], w[2]] for k, w in enumerate(words)}}
env = np.clip((db + 60) / 60, 0, 1)
(P / "production/word_timing.json").write_text(json.dumps({"audio": AUDIO.name, "segments": segs, "phrases": phr_out, "codes": codes,
    "words": words, "method": __doc__.strip().splitlines()[0]}, indent=1, ensure_ascii=False))
(P / "vendor/vo_words.js").write_text(
    "// generated by tools/align.py — VO timing measured from assets/audio/vo_tight.wav\n"
    "window.VO_WORDS = " + json.dumps(words, separators=(",", ":"), ensure_ascii=False) + ";\n"
    "window.VO_PHONES = " + json.dumps(phones, separators=(",", ":")) + ";\n"
    "window.VO_ENV = " + json.dumps([int(round(v * 99)) for v in env], separators=(",", ":")) + ";\n"
    "window.VO_PHR = " + json.dumps({"dur": info["dur"], "hook": info["hook"], "codes": codes, "cta": info["cta"]}, separators=(",", ":"), ensure_ascii=False) + ";\n")
print(f"{len(words)} words, {len(phones)} phones, dur {DUR:.3f}")
for p in phr_out: print(f"  {p['kind']:5s} {p['start']:6.2f}-{p['end']:6.2f}  {p['text']}")
