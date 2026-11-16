"""Word timing: local Whisper (faster-whisper, 'small', Indonesian) word timestamps aligned to the exact script text.
Script tokens are matched to recognised words with difflib; unmatched tokens are interpolated between neighbours.
Output: production/word_timing.json, vendor/vo_words.js (VO_WORDS [word,start,end,phraseIdx], VO_PHR)
Run: python3 tools/align_whisper.py <project>"""
import difflib, json, re, sys, wave
from pathlib import Path
import numpy as np

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
# caption phrases (short on-screen chunks), in spoken order
PHRASES = """Telepon masuk jam sembilan malam,
pas lu udah tutup.
Biasanya, pelanggannya
langsung cari tempat lain.
Sekarang, satu asisten suara AI
yang ngangkat, ngatur jadwal,
dan nyatet datanya.
Cek simulasinya.
Pelanggan bilang, mau booking
potong rambut besok jam empat.
AI langsung nangkep
layanan, hari, dan jamnya.
Terus dia cek kalender.
Jam empat udah penuh,
jadi dia tawarin
jam empat tiga puluh.
Pelanggan setuju,
dan slotnya langsung kebooking.
Di detik yang sama,
nama, nomor WA,
dan layanannya masuk ke
satu baris spreadsheet.
Terakhir, AI-nya konfirmasi
lewat suara:
jadwal Kakak besok
jam empat tiga puluh, ya.
Satu telepon,
tiga sistem nyambung.
Tanpa ada yang
ngetik manual.
Mau sistem kayak gini
dipasang di bisnis lu?
Klik link di bio,
ngobrol langsung sama
tim AIpreneur Automation.""".strip().split("\n")
NUM = {}
ALIAS = {"lo": "lu", "5": "lima", "9": "sembilan", "4": "empat", "3": "tiga", "7": "tujuh", "pake": "pakai", "kaya": "kayak", "telefon": "telepon", "telpon": "telepon", "jatwal": "jadwal", "kaka": "kakak", "pelangganya": "pelanggannya", "keboking": "kebooking", "ke": "ke", "nggak": "gak", "2": "dua", "1": "satu", "cepat": "cepet", "30": "puluh", "ainya": "ainya", "nya": "nya"}
norm = lambda w: ALIAS.get(re.sub(r"[^a-z0-9]", "", w.lower()), re.sub(r"[^a-z0-9]", "", w.lower()))

w = wave.open(str(P / "assets/audio/vo.wav")); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
if sr != 16000:
    idx = np.arange(0, len(x), sr / 16000); x = np.interp(idx, np.arange(len(x)), x).astype(np.float32)
cache = P / "production/whisper_words.json"
if cache.exists():
    raw = json.loads(cache.read_text())
else:
    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = model.transcribe(x, language="id", word_timestamps=True)
    raw = [[wd.word, wd.start, wd.end] for s in segs for wd in s.words]
    cache.write_text(json.dumps(raw, ensure_ascii=False))
rec = [(norm(w0), s0, s1) for w0, s0, s1 in raw if norm(w0)]
# script tokens (numbers expanded so they can match spoken words; each expansion maps back to its token)
toks, sub = [], []
for pi, ph in enumerate(PHRASES):
    for t in ph.split():
        parts = NUM.get(t.strip(",.?:"), t).split() if t.strip(",.?:") in NUM else [t]
        for k, p in enumerate(parts):
            sub.append((len(toks), norm(p)))
        toks.append([t, None, None, pi])
sm = difflib.SequenceMatcher(a=[s[1] for s in sub], b=[r[0] for r in rec], autojunk=False)
for blk in sm.get_matching_blocks():
    for k in range(blk.size):
        ti = sub[blk.a + k][0]; _, s0, s1 = rec[blk.b + k]
        toks[ti][1] = s0 if toks[ti][1] is None else min(toks[ti][1], s0)
        toks[ti][2] = s1 if toks[ti][2] is None else max(toks[ti][2], s1)
# interpolate gaps
known = [i for i, t in enumerate(toks) if t[1] is not None]
for i, t in enumerate(toks):
    if t[1] is not None: continue
    lo = max([k for k in known if k < i], default=None); hi = min([k for k in known if k > i], default=None)
    a0 = toks[lo][2] if lo is not None else 0.0; b0 = toks[hi][1] if hi is not None else len(x) / 16000
    n0 = (lo if lo is not None else -1); n1 = (hi if hi is not None else len(toks))
    f0 = (i - n0) / (n1 - n0); f1 = (i + 1 - n0) / (n1 - n0)
    t[1] = a0 + (b0 - a0) * f0; t[2] = a0 + (b0 - a0) * f1
words = [[t[0], round(t[1], 3), round(t[2], 3), t[3]] for t in toks]
# snap phrase boundaries to the real silences (whisper start/end stamps drift 0.3-0.5 s around long pauses)
hop = 160; n = len(x) // hop
env = np.array([np.abs(x[i * hop:(i + 1) * hop]).mean() for i in range(n)]) * 32768
gaps, g = [], None
for i, v in enumerate(env):
    if v < 120 and g is None: g = i
    if v >= 120 and g is not None:
        if i - g >= 15: gaps.append((g / 100, i / 100))
        g = None
first = {}; last = {}
for wi, wd in enumerate(words):
    first.setdefault(wd[3], wi); last[wd[3]] = wi
for pi in range(1, len(PHRASES)):
    f, l = first[pi], last[pi - 1]
    for g0, g1 in gaps:
        if g0 <= words[f][1] <= g1 + 0.3 or abs(words[f][1] - g1) <= 0.45:
            if words[l][2] <= g1:
                words[f][1] = round(max(g1 - 0.03, words[f][1] if words[f][1] > g1 else 0), 3)
                if words[l][2] > g0 + 0.05 or g0 - words[l][2] < 0.45: words[l][2] = round(max(words[l][1] + 0.05, g0 + 0.03), 3)
                if words[f][2] < words[f][1] + 0.05: words[f][2] = round(words[f][1] + 0.2, 3)
                break
phr = []
for pi, ph in enumerate(PHRASES):
    ws = [wd for wd in words if wd[3] == pi]
    phr.append({"text": ph, "start": ws[0][1], "end": ws[-1][2]})
matched = len(known)
(P / "vendor/vo_words.js").write_text("// generated by tools/align_whisper.py\nwindow.VO_WORDS = " + json.dumps(words, ensure_ascii=False) +
                                      ";\nwindow.VO_PHR = " + json.dumps(phr, ensure_ascii=False) + ";\n")
(P / "production/word_timing.json").write_text(json.dumps({"words": words, "phrases": phr}, ensure_ascii=False, indent=1))
print(f"matched {matched}/{len(toks)} tokens")
for p in phr: print(f"{p['start']:6.2f}-{p['end']:6.2f}  {p['text']}")
