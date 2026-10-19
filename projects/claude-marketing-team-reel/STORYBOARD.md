---
format: 1080x1920
fps: 30
duration: 70.034
music: none
vo: assets/vo.mp3 (Testing Hyperframe(1).MP3)
---

# STORYBOARD — 1 Plugin = 1 Tim Marketing?

Locked storyboard = user brief Section C. Scene order, display copy, layouts and motion follow it exactly.
**Only change: beat boundaries retimed to the real VO** (brief rule: audio is the master timing source).

| Beat | Role | Start | End | Brief window | Transition in | Character |
|---|---|---:|---:|---|---|---|
| S01 | Hook | 0.000 | 4.550 | 0.000–5.700 | — | seated 1.png |
| S02 | 16 skills | 4.550 | 7.550 | 5.700–9.100 | push | seated-head (1.png) |
| S03 | Scope | 7.550 | 15.500 | 9.100–14.400 | push | TALK → SMILE |
| S04 | 7 agents | 15.500 | 21.500 | 14.400–21.960 | diagonal paper wipe | SMILE → CONFIDENT |
| S05 | Install | 21.500 | 27.380 | 21.960–27.640 | card-stack cover | seated-head (1.png) |
| S06 | First command | 27.380 | 35.240 | 27.640–35.240 | push | TALK2 → TALK |
| S07 | Live Meta data | 35.240 | 39.850 | 35.240–40.880 | push | CONFIDENT |
| S08 | Escalation (navy) | 39.850 | 46.450 | 40.880–45.050 | vertical push | CONFIDENT → YAPPING |
| S09 | Second command (navy) | 46.450 | 54.900 | 45.050–53.760 | diagonal paper wipe | TALK2 |
| S10 | Execution pipeline | 54.900 | 63.000 | 53.760–61.330 | card-stack cover | SMILE → CONFIDENT |
| S11 | Payoff | 63.000 | 66.950 | 61.330–66.630 | push | seated 1.png |
| S12 | CTA | 66.950 | 70.034 | 66.630–70.034 | vertical push + 0.45s off-white fade | YAPPING (pointing) |

## Why the retime

Word timestamps come from forced alignment of the corrected script against the real MP3
(`tools/force_align.py`, pocketsphinx). Whisper could not be used: the model hosts (huggingface.co,
openaipublic.azureedge.net) are blocked by this session's network policy.
Cross-checked against independent acoustic evidence — /s/ fricative bursts (4–8 kHz) land on the
predicted words: skill 6.37→6.40, riset→9.06, sampai 10.12→10.20, SKINKU 31.27→31.33, siap 65.60→65.65,
scale 65.86→65.92, sistem 66.60→66.65. The brief's beat starts were off by up to ~1.75s
(e.g. "Kalau lu mau berhenti" is spoken at 63.08s, brief had 61.33s).

## Captions

35 groups, 3–5 words, one visible at a time, hard-killed by their clip window.
Hidden on purpose where the same words are already hero copy on screen: S06 prompt type-on (29.40–35.24),
S09 prompt type-on (49.00–54.90), S12 CTA (66.90–end). Highlighted: 16, 7, Claude, MCP, Meta, SKINKU, Higgsfield, META.

## QA items

- Last word `kalian` (69.35–69.80) could not be fitted by the en-us acoustic model; timing is placed in the remaining speech before the final pause.
- `pembuat` in "AI pembuat visual" (txt said `membuat`) chosen from context; not shown as hero copy.
- No logos, dashboards, URLs, sales numbers or ROAS shown. Tiles, charts and cards are abstract placeholders.
- SFX omitted (no verified licensed local source). No BGM.

## Character (v3)

The character is now the HeyGen talking video supplied by the user (`assets/source/Testing_Karakter_1.mp4`,
720x1280, 25 fps, 70.0s, rendered by HeyGen from 1.png + the same VO; audio cross-correlation with the VO:
0.968, offset 0.02s). Its pure-black background is keyed locally (`tools/key_black.py`, border-connected
flood-fill on r+g+b <= 6 with a 2px soft edge) into `assets/heygen/char-alpha.webm` (VP9 + alpha).
Each scene mounts it as a sub-composition (`compositions/char-sXX.html`, muted, `data-media-start` = scene
start) so mouth/head motion stays in sync with the master VO. The VO stays the only audio source.
