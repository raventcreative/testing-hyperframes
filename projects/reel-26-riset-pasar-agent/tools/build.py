"""tools/index.src.html -> index.html (injects the VO word timings from production/words.json)."""
import json
s = open("tools/index.src.html").read()
w = json.load(open("production/words.json"))
open("index.html", "w").write(s.replace("/*WORDS*/", json.dumps(w, ensure_ascii=False)))
print("index.html", len(w), "words")
