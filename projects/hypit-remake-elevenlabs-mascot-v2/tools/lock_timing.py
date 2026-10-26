#!/usr/bin/env python3
"""Lock word_timing.json (words + caption groups + apex) and scenes.json from
production/_words_tmp.json. Run: python3 -I tools/lock_timing.py <project_dir>"""
import json, sys, subprocess
from pathlib import Path

P = Path(sys.argv[1]).resolve()
words = json.loads((P / "production/_words_tmp.json").read_text())["words"]
FPS = 30
AUDIO_DUR = 61.07425
D = round(-(-AUDIO_DUR * FPS // 1) / FPS, 4)  # ceil to frame: 1833 frames = 61.1 s

# scene: id, first word, last word, hero, apex word indices, mascot
SC = [
    ("s01", 0, 10, "Reel scanner extracting waveform + keyframes", [8], None),
    ("s02", 11, 20, "Hypit engraved chip + physical star vault", [12, 20], "front peek"),
    ("s03", 21, 32, "Reel enters data capsule on agent input portal", [31], None),
    ("s04", 33, 40, "Illuminated mechanical coding-agent core", [40], "side lean"),
    ("s05", 41, 48, "Giant editing deck assembles", [47], None),
    ("s06", 49, 53, "4 inserts hit production rail", [49, 50, 51, 53], None),
    ("s07", 54, 57, "Paper script peels away from film deck", [57], None),
    ("s08", 58, 65, "Timeline trim handle with capsule", [64], "side watches"),
    ("s09", 66, 70, "Generic tactile product stage", [70], None),
    ("s10", 71, 73, "Reusable film-template frame locks in", [73], None),
    ("s11", 74, 81, "4 parameter token swaps", [75, 76, 77, 79], "front reacts"),
    ("s12", 82, 93, "Master spindle fans out variants", [86], None),
    ("s13", 94, 99, "Ownership gate blocks third-party tokens", [95], None),
    ("s14", 100, 108, "3 cleared media objects enter vault", [101, 102, 104, 108], "front nod"),
    ("s15", 109, 116, "Tactile terminal, verified install line", [111], None),
    ("s16", 117, 121, "Input reel + paper brief slots", [121], "side cameo"),
    ("s17", 122, 133, "Open-source latch vs optional services meter", [123, 133], None),
    ("s18", 134, 139, "Folder opens install quickstart booklet", [138], None),
    ("s19", 140, 144, "Comment bubble HYPIT + mascot final still", [141], "front cameo"),
]
# caption groups: (first, last, [highlight spans as (a,b)])
CG = [
    (0, 3, [(3, 3)]), (4, 6, [(6, 6)]), (7, 10, [(8, 8)]),
    (11, 12, [(12, 12)]), (13, 16, [(14, 14)]), (17, 20, [(20, 20)]),
    (21, 25, []), (26, 29, [(28, 29)]), (30, 32, [(31, 32)]),
    (33, 36, []), (37, 40, [(40, 40)]),
    (41, 45, [(42, 42)]), (46, 48, [(47, 47)]),
    (49, 53, [(49, 49), (50, 50), (51, 51), (53, 53)]),
    (54, 57, [(57, 57)]),
    (58, 60, [(59, 59)]), (61, 65, [(64, 64)]),
    (66, 70, [(70, 70)]),
    (71, 73, [(73, 73)]),
    (74, 76, [(75, 75), (76, 76)]), (77, 81, [(77, 77), (79, 79)]),
    (82, 85, []), (86, 88, [(86, 87)]), (89, 93, [(93, 93)]),
    (94, 99, [(95, 95)]),
    (100, 104, []), (105, 108, [(108, 108)]),
    (109, 113, [(111, 112)]), (114, 116, []),
    (117, 121, [(119, 119), (121, 121)]),
    (122, 124, [(123, 124)]), (125, 128, []), (129, 133, [(133, 133)]),
    (134, 139, [(138, 138)]),
    (140, 141, [(141, 141)]), (142, 144, []),
]


def fr(t):
    return round(round(t * FPS) / FPS, 4)


# scene cuts = middle of the pause between phrases, snapped to frame grid
scenes = []
for k, (sid, a, b, hero, apex, masc) in enumerate(SC):
    start = 0.0 if k == 0 else fr((words[SC[k - 1][2]]["end"] + words[a]["start"]) / 2)
    scenes.append({"id": sid, "start": start, "first_word": a, "last_word": b, "hero": hero, "apex_words": apex, "mascot": masc})
for k, s in enumerate(scenes):
    s["end"] = scenes[k + 1]["start"] if k + 1 < len(scenes) else D
    s["duration"] = round(s["end"] - s["start"], 4)
    s["phrase"] = " ".join(w["text"] for w in words[s["first_word"]: s["last_word"] + 1])
    s["apex"] = [{"word": words[i]["text"], "global": words[i]["start"], "local": round(words[i]["start"] - s["start"], 3)} for i in s["apex_words"]]
    s["words_local"] = [{"i": i, "text": words[i]["text"], "start": round(words[i]["start"] - s["start"], 3), "end": round(words[i]["end"] - s["start"], 3)} for i in range(s["first_word"], s["last_word"] + 1)]

# coverage check
covered = [i for s in scenes for i in range(s["first_word"], s["last_word"] + 1)]
assert covered == list(range(len(words))), "scene word coverage broken"
canon = (P / "handoff/07_VO_ELEVENLABS_READY.txt").read_text().split()
assert [w["text"] for w in words] == canon, "words differ from canonical"

# caption groups timing: open slightly before first word, stay until next group opens
groups = []
for gi, (a, b, hl) in enumerate(CG):
    st = max(0.0, words[a]["start"] - 0.12) if gi else 0.0
    groups.append({"word_idx": list(range(a, b + 1)), "start": round(st, 3), "highlight_spans": [list(x) for x in hl],
                   "highlight": [i for x in hl for i in range(x[0], x[1] + 1)], "text": " ".join(words[i]["text"] for i in range(a, b + 1))})
for gi, g in enumerate(groups):
    g["end"] = groups[gi + 1]["start"] if gi + 1 < len(groups) else D
cg_cover = [i for g in groups for i in g["word_idx"]]
assert cg_cover == list(range(len(words))), "caption coverage broken"

wt = {
    "source": "assets/vo_elevenlabs_final.mp3",
    "audio": {"duration": AUDIO_DUR, "codec": "mp3", "channels": 1, "sample_rate": 44100,
              "speech_onset": words[0]["start"], "last_word_end": words[-1]["end"], "file_tail_silence": round(AUDIO_DUR - words[-1]["end"], 3)},
    "video_duration": D, "fps": FPS, "frames": int(round(D * FPS)),
    "method": "Whisper large-v3 (whisper.cpp, language=id) word stamps -> mapped by position onto 07_VO_ELEVENLABS_READY.txt -> "
              "every punctuation pause anchored to measured silences (ffmpeg silencedetect -38dB/60ms) -> interior words = mean of "
              "Whisper-relative and syllable-proportional boundaries, snapped to <-40 dB frames within +-70 ms.",
    "accuracy": "Pause-anchored boundaries ~+-0.02 s. Interior word boundaries estimated, typically +-0.1 s (not hand-verified by ear).",
    "words": words,
    "caption_groups": groups,
}
(P / "production/word_timing.json").write_text(json.dumps(wt, indent=1, ensure_ascii=False))
(P / "production/scenes.json").write_text(json.dumps({"duration": D, "fps": FPS, "scenes": scenes, "sfx": []}, indent=1, ensure_ascii=False))
for s in scenes:
    print(f'{s["id"]} {s["start"]:7.3f}-{s["end"]:7.3f} ({s["duration"]:.3f}s) apex {[(a["word"], a["global"], a["local"]) for a in s["apex"]]}')
print("D", D, "frames", int(round(D * FPS)), "groups", len(groups))
