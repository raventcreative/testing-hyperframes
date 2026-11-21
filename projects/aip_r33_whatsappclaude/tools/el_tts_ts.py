"""ElevenLabs TTS with character timestamps (voice + settings from tools/voice_config.json; the API key is injected by the
session's network proxy, never stored here).
Usage: python3 tools/el_tts_ts.py <lines.txt> <out.mp3> [--tags "[playful] [excited]" | --tags auto]
  lines.txt: one VO line per line. Every line gets audio tags in front. Writes out.mp3 and out.json with each line's
  start/end time in seconds (from the character alignment), for re-timing the film to the voice.
  Tags: "auto" (the default, from voice_config.json) = the client's base tags "[playful] [excited]" on every line PLUS one
  context tag picked from the line itself (question -> [curious], pain point -> [sighs], surprise -> [surprised], secret/tip ->
  [whispers], joke -> [laughs], call to action -> [confident]). A line that already starts with its own [tags] keeps them
  (they are added after the base tags). Any other --tags value is used verbatim on every line (old behaviour)."""
import base64, json, re, sys, urllib.request, urllib.error
from pathlib import Path
CFG = json.loads((Path(__file__).parent / "voice_config.json").read_text())
src, out = Path(sys.argv[1]), Path(sys.argv[2])
tags = sys.argv[sys.argv.index("--tags") + 1] if "--tags" in sys.argv else CFG.get("tags", "")
BASE = CFG.get("base_tags", "[playful] [excited]")
AUTO = [   # first match wins; Indonesian + English cues
    ("[confident]", r"\b(komen|coba kalkulator|link di bio|klik|follow|daftar|cek link|ketik)\b"),
    ("[whispers]", r"\b(rahasia|diam-diam|jarang yang tahu|banyak yang nggak tahu|bocoran|psst)\b"),
    ("[laughs]", r"\b(haha|wkwk|lucu|bercanda|ngakak)\b"),
    ("[surprised]", r"\b(ternyata|padahal|wah|loh|lho|kaget|siapa sangka|beneran)\b"),
    ("[sighs]", r"\b(capek|pusing|ribet|bingung|berantakan|numpuk|telat|nyesel|bocor|tipis|ilang|hilang|lupa|kacau)\b"),
    ("[curious]", r"\?\s*$"),
]
def tags_for(line):
    own = re.match(r"^((?:\[[^\]]+\]\s*)+)", line)
    text = line[own.end():] if own else line
    if tags != "auto":
        return (tags + " " if tags else "") + (own.group(1) if own else ""), text
    extra = own.group(1).strip() if own else next((t for t, rx in AUTO if re.search(rx, text.lower())), "")
    return (BASE + (" " + extra if extra else "") + " "), text
raw = [l.strip() for l in src.read_text().splitlines() if l.strip()]
lines, parts, spans, used, pos = [], [], [], [], 0
for l in raw:
    pre, text = tags_for(l)
    seg = pre + text
    a = pos + len(pre)                                   # first spoken character of this line
    spans.append((a, pos + len(seg))); parts.append(seg); used.append(pre.strip()); lines.append(text); pos += len(seg) + 1
text = "\n".join(parts)
body = {"text": text, "model_id": CFG["model_id"], "voice_settings": CFG["voice_settings"]}
req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{CFG['voice_id']}/with-timestamps?output_format={CFG.get('output_format', 'mp3_44100_128')}",
                             data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "xi-api-key": "proxy-injected"}, method="POST")
try:
    with urllib.request.urlopen(req, timeout=300) as r: res = json.loads(r.read())
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode()[:600]); sys.exit(1)
out.write_bytes(base64.b64decode(res["audio_base64"]))
al = res.get("alignment") or res.get("normalized_alignment")
chars, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
full = "".join(chars)
# map our text offsets onto the alignment (the service may echo the text 1:1; fall back to searching each line)
res_lines, cursor = [], 0
for l, (a, b) in zip(lines, spans):
    i = full.find(l[: min(len(l), 24)], cursor)
    if i < 0: i = a if a < len(full) else cursor
    j = min(len(full), i + len(l)) - 1
    while j > i and not chars[j].strip(): j -= 1
    res_lines.append({"text": l, "start": round(st[i], 3), "end": round(en[j], 3)}); cursor = j + 1
for r_, u in zip(res_lines, used): r_["tags"] = u
json.dump({"voice_id": CFG["voice_id"], "tags": tags, "duration": round(en[-1], 3), "lines": res_lines,
           "align": {"chars": full, "start": [round(v, 3) for v in st], "end": [round(v, 3) for v in en]}},
          open(out.with_suffix(".json"), "w"), indent=1, ensure_ascii=False)
print("ok", out, f"{en[-1]:.2f}s", len(res_lines), "lines")
for r_ in res_lines: print(f"  {r_['start']:6.2f}-{r_['end']:6.2f}  {r_['tags']:<34} {r_['text'][:60]}")
