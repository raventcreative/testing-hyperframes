"""PROVISIONAL word timings, estimated from the script — NOT a real alignment.

Only for checking layout while the ElevenLabs key is unavailable. The moment a real
vo.wav exists, run tools/align_whisper.py instead; it overwrites production/word_timing.json
with true times. The phrase TEXTS produced here match what align_whisper produces for the
same script, so every ph("...") anchor in index.src.txt keeps working unchanged.

Run: python3 -I tools/provisional_timing.py <project>
"""
import json, re, sys
from pathlib import Path

P = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
raw = (P / "production/vo_script.txt").read_text().strip().splitlines()

WPS = 3.05          # Indonesian words per second, measured across reels 27-32
GAP_CLAUSE = 0.14   # comma break inside a line
GAP_LINE = 0.30     # between script lines (client rule: <= 0.45 s)

phrases, words, t = [], [], 0.0
for li, line in enumerate(raw):
    line = re.sub(r"\[[a-z ]+\]\s*", "", line).strip()
    if not line:
        continue
    # align_whisper splits on , . ? ! keeping the delimiter on the clause
    parts = [p.strip() for p in re.findall(r"[^,.?!]+[,.?!]?", line) if p.strip()]
    for pi, part in enumerate(parts):
        ws = part.split()
        start = t
        for w in ws:
            d = max(0.12, len(w) / (WPS * 4.6))
            words.append([w, round(t, 3), round(t + d, 3), len(phrases)])
            t += d
        phrases.append({"text": part, "start": round(start, 3), "end": round(t, 3)})
        t += GAP_CLAUSE if pi < len(parts) - 1 else GAP_LINE

out = {"words": words, "phrases": phrases, "_provisional": True}
(P / "production/word_timing.json").write_text(json.dumps(out, indent=1))
js = "// PROVISIONAL (tools/provisional_timing.py) — replaced by align_whisper.py once the VO exists\n"
js += "window.VO_WORDS = " + json.dumps(words) + ";\n"
js += "window.VO_PHR = " + json.dumps(phrases) + ";\n"
(P / "vendor/vo_words.js").write_text(js)
print(f"provisional: {len(phrases)} phrases, {len(words)} words, {t:.2f}s")
