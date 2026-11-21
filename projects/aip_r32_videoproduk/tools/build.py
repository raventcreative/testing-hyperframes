"""tools/index.src.html + tools/main_script.js -> index.html (injects the VO word timings from production/words.json)."""
import json
s = open("tools/index.src.html").read().replace("/*MAIN*/", open("tools/main_script.js").read().rstrip("\n"))
w = json.load(open("production/words.json"))
open("index.html", "w").write(s.replace("/*WORDS*/", json.dumps(w, ensure_ascii=False)))
print("index.html", len(w), "words")
