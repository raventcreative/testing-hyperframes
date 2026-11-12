"""Builds production/vo_words_raw.json (faster-whisper format) from the ElevenLabs character alignment
(production/vo_el_alignment.json, written by tools/el_tts_ts.py): words = whitespace-split tokens, audio tags skipped,
one segment per VO line. Exact, no whisper needed.   Run: python3 -I tools/align_words.py ."""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
A = json.loads((P / "production/vo_el_alignment.json").read_text())
ch, st, en = A["align"]["chars"], A["align"]["start"], A["align"]["end"]
segs, cur, i, n = [], [], 0, len(ch)
while i < n:
    if ch[i] == "\n":
        if cur: segs.append(cur); cur = []
        i += 1; continue
    if ch[i].isspace(): i += 1; continue
    j = i
    while j < n and not ch[j].isspace(): j += 1
    tok = ch[i:j]
    if not re.fullmatch(r"\[[^\]]*\]", tok):
        # first / last character that carries real timing
        cur.append({"w": tok, "s": round(st[i], 3), "e": round(en[j - 1], 3), "p": 1.0})
    i = j
if cur: segs.append(cur)
out = {"language": "id", "source": "elevenlabs-alignment", "segments": [
    {"start": s[0]["s"], "end": s[-1]["e"], "text": " ".join(w["w"] for w in s), "words": s} for s in segs]}
(P / "production/vo_words_raw.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
for k, s in enumerate(segs):
    print(k, f"{s[0]['s']:.2f}-{s[-1]['e']:.2f}", " ".join(f"{w['w']}@{w['s']:.2f}" for w in s))
