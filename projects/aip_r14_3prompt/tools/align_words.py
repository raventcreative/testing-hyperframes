"""Builds production/vo_words_raw.json (faster-whisper format) from the ElevenLabs character alignment (assets/audio/vo.json,
written by /home/user/testing-hyperframes/tools/el_tts_ts.py). Words = whitespace-split tokens; audio tags ([playful] ...) skipped.
Run: python3 -I tools/align_words.py ."""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
J = json.loads((P / "assets/audio/vo.json").read_text())
A = J["align"]; ch, st, en = A["chars"], A["start"], A["end"]
segs = []
for line in ch.split("\n"):
    pass
pos = 0
for raw_line in ch.split("\n"):
    words = []
    for m in re.finditer(r"\S+", raw_line):
        tok = m.group(0); a = pos + m.start(); b = pos + m.end() - 1
        if re.fullmatch(r"\[[a-z ]+\]", tok): continue
        # time of the token: first voiced char -> last char (punctuation keeps the end of the last letter)
        bb = b
        while bb > a and not ch[bb].isalnum(): bb -= 1
        words.append({"w": tok, "s": round(st[a], 3), "e": round(en[bb], 3), "p": 1.0})
    if words:
        segs.append({"start": words[0]["s"], "end": words[-1]["e"], "text": " ".join(w["w"] for w in words), "words": words})
    pos += len(raw_line) + 1
out = {"language": "id", "duration": J["duration"], "source": "elevenlabs character alignment", "segments": segs}
(P / "production/vo_words_raw.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
n = sum(len(s["words"]) for s in segs)
print("words", n, "segments", len(segs))
for i, w in enumerate(w for s in segs for w in s["words"]): print(i, w["w"], w["s"], w["e"])
