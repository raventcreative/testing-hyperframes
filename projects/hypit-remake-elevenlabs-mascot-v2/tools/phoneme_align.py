"""Audio-driven character/phoneme-level forced alignment of the final VO.

Model: MMS-300m CTC forced aligner (ONNX, via the `ctc-forced-aligner` package, runs locally on CPU).
Indonesian orthography is close to phonemic, so each aligned character ~ one phoneme.
The alignment text is the *pronunciation actually heard* in the audio (e.g. "Claude" -> "klod",
"HYPIT" -> "haipit"); see PRON below. Discrepancies vs the canonical script are reported.

Output: production/phoneme_timing.json  { phones: [[char, start, end, word_idx], ...], words: [...] }
Run with the venv that has ctc-forced-aligner:  <venv>/bin/python tools/phoneme_align.py <project>
"""
import json, sys
from pathlib import Path
import numpy as np
from ctc_forced_aligner import (AlignmentSingleton, generate_emissions, get_alignments, get_spans, load_audio)

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
wt = json.loads((P / "production/word_timing.json").read_text())
words = wt["words"]

# pronunciation heard in Freddie's ElevenLabs VO (spoken form, lowercase a-z only)
PRON = {
    "hypit": "haipit", "claude": "klod", "ai": "ai", "github": "githab", "b-roll": "birol",
    "footage": "futej", "caption": "kepsyen", "workflow": "werkflo", "framework-nya": "fremwerknya",
    "open": "open", "source": "sors", "brief": "brif", "skill": "skil", "hook": "huk",
    "katanya": "kataannya", "code": "kod", "agent": "ejen", "coding": "koding",  # audio says "perkataannya" (flagged in transcript_review.md)
}

def spoken(w):
    k = "".join(ch for ch in w.lower() if ch.isalpha() or ch == "-").strip("-")
    s = PRON.get(k, k)
    return "".join(ch for ch in s if "a" <= ch <= "z")

tokens_txt = [spoken(w["text"]) for w in words]
model = AlignmentSingleton(model_path=str(Path.home() / ".cache/ctc_forced_aligner/model.onnx"))
audio = load_audio(str(P / "assets/vo_elevenlabs_final.mp3"))
cache = Path.home() / ".cache/ctc_forced_aligner/vo_emissions.npz"
if cache.exists():
    z = np.load(cache); emissions, stride = z["e"], int(z["s"])
else:
    emissions, stride = generate_emissions(model.alignment_model, audio, batch_size=4)
    np.savez(cache, e=emissions, s=stride)

tokens_starred = []
for t in tokens_txt:
    tokens_starred += ["<star>", " ".join(t)]
segments, scores, blank = get_alignments(emissions, tokens_starred, model.alignment_tokenizer)
spans = get_spans(tokens_starred, segments, blank)

phones, out_words = [], []
wi = 0
for i, tok in enumerate(tokens_starred):
    if tok == "<star>":
        continue
    sp = spans[i]
    chars = tok.split(" ")
    lab = [s for s in sp if s.label != blank]  # CTC character peaks (blanks are padding)
    assert len(lab) == len(chars), (tok, len(lab))
    w0 = sp[0].start * stride / 1000          # word span incl. half the surrounding blanks
    w1 = (sp[-1].end + 1) * stride / 1000
    on = [s.start * stride / 1000 for s in lab]
    ws, we = on[0], max(on[-1] + 0.06, min(w1, (lab[-1].end + 1) * stride / 1000 + 0.08))
    for k, ch in enumerate(chars):
        e = on[k + 1] if k + 1 < len(chars) else we
        phones.append([ch, round(on[k], 3), round(e, 3), wi])
    out_words.append({"i": wi, "text": words[wi]["text"], "spoken": tokens_txt[wi],
                      "start": round(ws, 3), "end": round(we, 3),
                      "prev_start": words[wi]["start"], "prev_end": words[wi]["end"]})
    wi += 1

d = [abs(w["start"] - w["prev_start"]) for w in out_words]
res = {"method": "MMS-300m CTC forced alignment (ctc-forced-aligner ONNX), character level on spoken-form text",
       "stride_ms": stride, "audio": "assets/vo_elevenlabs_final.mp3",
       "pronunciation_overrides": PRON, "phones": phones, "words": out_words,
       "word_start_vs_previous_alignment": {"mean_abs_s": round(float(np.mean(d)), 3), "max_abs_s": round(float(np.max(d)), 3)}}
(P / "production/phoneme_timing.json").write_text(json.dumps(res, indent=1))
print(len(phones), "phones,", len(out_words), "words; stride", stride, "ms; word-start diff vs previous:", res["word_start_vs_previous_alignment"])
