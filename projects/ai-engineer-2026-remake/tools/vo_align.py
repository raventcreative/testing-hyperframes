"""VO timing master for SIX WORLDS (measured from the audio, never estimated).

1. Script words (the exact spoken script from the brief) -> spoken form (what the ElevenLabs voice says).
2. MMS-300m CTC forced alignment (ctc-forced-aligner, ONNX, local CPU), character level  -> phone onsets.
3. Word start = first phone onset - 20 ms; word end = first 30 ms below -40 dB after the last phone.
4. Caption groups (1-2 lines, phrase-bounded) + keyword highlights.
Outputs: production/word_timing.json, production/phoneme_timing.json, vendor/vo_words.js
         (window.VO_WORDS [text,start,end,keyword,spoken], VO_PHONES, VO_ENV 100 Hz 0..99)
Run: <venv>/bin/python -I tools/vo_align.py <project>
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np
from ctc_forced_aligner import AlignmentSingleton, generate_emissions, get_alignments, get_spans, load_audio

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
AUDIO = P / "assets/audio/voiceover_final.mp3"
SCRIPT = """Bikin AI agent doang, belum bikin lo jadi AI Engineer.
Kalau fondasinya bolong, demo yang keren pun bisa ambruk.
Bayangin lo lagi ngerakit satu mesin AI. Ada sepuluh komponen. Dan urutannya penting.
Pertama, Python. Kuasai fungsi, struktur data, API, dan debugging. Mulai dari program kecil yang benar-benar jalan.
Kedua, software engineering. Pahami Git, database, backend, dan cara aplikasi saling terhubung. Karena AI tetap butuh sistem yang rapi.
Ketiga, machine learning. Pelajari cara data dipakai buat melatih dan menguji model. Termasuk cara mengetahui ketika modelnya salah.
Keempat, deep learning. Kenali neural network, tensor, dan framework seperti PyTorch.
Kelima, LLM. Pahami token, konteks, embedding, dan cara model memproses bahasa.
Keenam, AI application. Hubungkan model lewat API, atur output, lalu jadikan fitur yang benar-benar bisa dipakai.
Ketujuh, RAG. Sebelum menjawab, sistem mencari bagian dokumen yang relevan. Jadi jawaban bisa didukung data yang kita berikan.
Kedelapan, AI agent. Beri sistem alat dan batasan yang jelas. Supaya dia bisa memilih langkah, menjalankan tugas, lalu memeriksa hasilnya.
Kesembilan, evaluation. Tes pakai kasus sulit. Cari bagian yang gagal. Perbaiki. Lalu tes lagi.
Kesepuluh, production. Deploy sistemnya. Pantau biaya, kecepatan, keamanan, dan kestabilannya.
Setelah itu, pilih jalur. Mau membangun produk AI? Atau mendalami modelnya sampai level training?
Gak perlu belajar semuanya sekaligus. Mulai dari satu proyek kecil, lalu naikkan levelnya sedikit demi sedikit.
Karena AI Engineer bukan yang paling banyak coba tools. Tapi yang bisa membangun sistem AI yang benar-benar bekerja.
Simpan roadmap ini. Mulai dari komponen pertama."""

# pronunciation heard in the VO (lowercase a-z), checked against production/whisper_transcript.json
PRON = {
    "ai": "eiai", "agent": "ejen", "engineer": "enjinir", "python": "paiton", "api": "eipiai", "debugging": "dibaging",
    "software": "softwer", "engineering": "enjiniring", "git": "git", "database": "deitabeis", "backend": "bekend",
    "machine": "mesin", "learning": "lerning", "deep": "dip", "neural": "nural", "network": "netwerk",
    "framework": "frermwerk", "pytorch": "paitorc", "llm": "elelem", "embedding": "embeding", "application": "aplikeisyen",
    "output": "autput", "rag": "rag", "evaluation": "ivaluasyen", "production": "prodaksyen", "deploy": "diploi",
    "training": "trening", "tools": "tuls", "roadmap": "roudmep", "sepuluh": "sepuluh", "token": "token",
}
KEYWORDS = {"agent", "Engineer.", "fondasinya", "ambruk.", "mesin", "sepuluh", "Python.", "debugging.", "jalan.",
            "engineering.", "rapi.", "learning.", "salah.", "PyTorch.", "LLM.", "embedding,", "application.", "dipakai.",
            "RAG.", "relevan.", "agent.", "batasan", "memeriksa", "evaluation.", "gagal.", "production.", "keamanan,",
            "jalur.", "produk", "training?", "satu", "kecil,", "bekerja.", "roadmap", "pertama."}

words = SCRIPT.split()
def spoken(w):
    k = re.sub(r"[^a-z0-9\-]", "", w.lower()).strip("-")
    s = PRON.get(k, k)
    return "".join(ch for ch in s if "a" <= ch <= "z")
sp_txt = [spoken(w) for w in words]

model = AlignmentSingleton(model_path=str(Path.home() / ".cache/ctc_forced_aligner/model.onnx"))
cache = Path.home() / ".cache/ctc_forced_aligner/aie_vo_emissions.npz"
if cache.exists():
    z = np.load(cache); emissions, stride = z["e"], int(z["s"])
else:
    emissions, stride = generate_emissions(model.alignment_model, load_audio(str(AUDIO)), batch_size=4)
    np.savez(cache, e=emissions, s=stride)
toks = []
for t in sp_txt:
    toks += ["<star>", " ".join(t)]
segments, scores, blank = get_alignments(emissions, toks, model.alignment_tokenizer)
spans = get_spans(toks, segments, blank)

# energy envelope (100 Hz)
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(AUDIO), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768
hop = 160; n = len(a) // hop
db = 20 * np.log10(np.sqrt(np.mean(a[: n * hop].reshape(n, hop) ** 2, axis=1)) + 1e-6)
DUR = len(a) / 16000

ph_raw, wi = [], 0
for i, tok in enumerate(toks):
    if tok == "<star>":
        continue
    lab = [s for s in spans[i] if s.label != blank]
    chars = tok.split(" ")
    assert len(lab) == len(chars), (tok, len(lab))
    for k, ch in enumerate(chars):
        ph_raw.append([ch, round(lab[k].start * stride / 1000, 3), wi])
    wi += 1

out_words = []
for k, w in enumerate(words):
    my = [x for x in ph_raw if x[2] == k]
    s = max(0.0, my[0][1] - 0.02)
    nxt_first = [x for x in ph_raw if x[2] == k + 1]
    nxt = nxt_first[0][1] - 0.02 if nxt_first else DUR
    e, f = None, int(round((my[-1][1] + 0.04) * 100))
    while f < n - 3 and f / 100 < nxt:
        if db[f] < -40 and db[f + 1] < -40 and db[f + 2] < -40:
            e = f / 100; break
        f += 1
    e = max(e if e is not None else nxt, my[-1][1] + 0.06)
    on_db = float(db[min(n - 1, int(round((my[0][1] + 0.02) * 100)))])
    out_words.append({"i": k, "text": w, "spoken": sp_txt[k], "start": round(s, 3), "end": round(min(e, nxt + 0.02), 3),
                      "onset_db": round(on_db, 1)})

phones = []
for k, w in enumerate(out_words):
    my = [x for x in ph_raw if x[2] == k]
    for j, x in enumerate(my):
        e = my[j + 1][1] if j + 1 < len(my) else w["end"]
        phones.append([x[0], x[1], round(e, 3), k])

# caption groups: break at sentence/phrase punctuation, max 6 words / 34 chars, never a 1-word orphan if avoidable
groups, cur = [], []
def flush():
    if cur:
        groups.append(list(cur)); cur.clear()
for k, w in enumerate(words):
    cur.append(k)
    txt = " ".join(words[i] for i in cur)
    end_phrase = re.search(r"[.,:?!]$", w) is not None
    if end_phrase and (len(cur) >= 2 or re.search(r"[.?!:]$", w)):
        flush()
    elif len(cur) >= 6 or len(txt) >= 34:
        flush()
flush()
# merge 1-word tails into the previous group when it stays short
merged = []
for g in groups:
    if merged and len(g) == 1 and len(merged[-1]) <= 3 and not re.search(r"[.?!]$", words[merged[-1][-1]]):
        merged[-1] += g
    else:
        merged.append(g)
cap = []
for gi, g in enumerate(merged):
    st = round(max(0.0, out_words[g[0]]["start"] - 0.1), 3) if gi else 0.0
    cap.append({"id": f"cg{gi:02d}", "word_idx": g, "text": " ".join(words[i] for i in g),
                "highlight": [i for i in g if words[i] in KEYWORDS], "start": st})
for gi, g in enumerate(cap):
    g["end"] = cap[gi + 1]["start"] if gi + 1 < len(cap) else round(DUR, 3)

res = {"audio": "assets/audio/voiceover_final.mp3", "audio_duration": round(DUR, 3),
       "method": "MMS-300m CTC forced alignment (local) on the spoken form; start = first phone - 20 ms; end = first 30 ms < -40 dB",
       "pronunciation_overrides": PRON, "words": out_words, "caption_groups": cap,
       "speech_onset": out_words[0]["start"], "last_word_end": out_words[-1]["end"]}
(P / "production/word_timing.json").write_text(json.dumps(res, indent=1, ensure_ascii=False))
(P / "production/phoneme_timing.json").write_text(json.dumps({"stride_ms": stride, "phones": phones}, indent=0))
env = np.clip((db + 60) / 60, 0, 1)
vw = [[w["text"], w["start"], w["end"], 1 if w["text"] in KEYWORDS else 0, w["spoken"]] for w in out_words]
(P / "vendor/vo_words.js").write_text(
    "// generated by tools/vo_align.py — VO timing measured from the audio (CTC forced alignment + energy)\n"
    "window.VO_WORDS = " + json.dumps(vw, separators=(",", ":"), ensure_ascii=False) + ";\n"
    "window.VO_PHONES = " + json.dumps(phones, separators=(",", ":")) + ";\n"
    "window.VO_ENV = " + json.dumps([int(round(v * 99)) for v in env], separators=(",", ":")) + "; // 100 Hz, 0..99 = -60..0 dB\n")
# report vs whisper
wh = json.loads((P / "production/whisper_transcript.json").read_text())["words"]
print(f"{len(out_words)} words, {len(phones)} phones, {len(cap)} caption groups, duration {DUR:.3f}s, last word end {out_words[-1]['end']}")
low = [(w['text'], w['start'], w['onset_db']) for w in out_words if w['onset_db'] < -38]
print("onsets below -38 dB:", low)
for w in out_words:
    best = min(wh, key=lambda x: abs(x["start"] - w["start"]))
    if abs(best["start"] - w["start"]) > 0.25:
        print("  vs whisper >0.25s:", w["text"], w["start"], "| whisper nearest:", best["text"], best["start"])
