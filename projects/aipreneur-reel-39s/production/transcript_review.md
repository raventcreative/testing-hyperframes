# Transcript review — AI PRENEUR Reel 39.40s

**Status:** machine transcript, reviewed by agent. Text is high-confidence (master WAV slice and untouched original part give identical text for all 11 segments). **Awaiting user confirmation of 3 flagged spellings below.**

Engine: Whisper **large-v3** multilingual, `language=id`, local CPU (sherpa-onnx int8; same weights from the official k2-fsa/sherpa-onnx GitHub release). No paid ASR, no HeyGen.

## Cross-check with official `npx hyperframes transcribe` (whisper.cpp, ggml-large-v3, `--language id`)
Run after Hugging Face access was enabled (model fetched with curl into `~/.cache/hyperframes/whisper/models/` because the CLI's Node downloader does not use the HTTPS proxy; sha256 64d182b4…d1e2). Output: `production/transcript_cli_whispercpp_large-v3.json`.
- **Text: 86/86 words identical** to the reviewed transcript. Brand heard as “AI-preneur” (confirms AI PRENEUR), “se-level” = “selevel”.
- **Timing: NOT adopted.** whisper.cpp word starts run a median 0.32 s early; 10 words start before their own clip even begins (inside silence), and 11 of 13 ASR-verified pause anchors are contradicted. The pause-anchored timing in `transcript_machine.json` stays the timing of record.

## Verbatim (reviewed display spelling)

| Cue | Audio (s) | Text |
|---|---|---|
| VO01 | 0.000–3.379 | Banyak orang bilang hasil AI itu masih biasa aja. |
| VO02 | 3.379–6.026 | Padahal masalahnya sering bukan di AI-nya. |
| VO03 | 6.026–8.336 | Masalahnya ada di arahan yang diberikan. |
| VO04 | 8.336–11.935 | AI itu cepat, tapi hasilnya mengikuti seberapa jelas brief-nya. |
| VO05 | 11.935–14.582 | Jadi bukan cuma bilang bikin yang keren, |
| VO06 | 14.582–19.888 | tapi menjelaskan style, ritme, komposisi, transisi, dan hierarki. |
| VO07 | 19.888–24.265 | Karena prompt yang tepat bisa mengubah output secara drastis. |
| VO08 | 24.265–28.073 | Dari teks biasa, menjadi motion yang terlihat mahal. |
| VO09 | 28.073–31.161 | Dan inilah cara AI PRENEUR mengarahkan AI. |
| VO10 | 31.161–35.701 | Lebih cepat, lebih terarah, dan hasilnya jauh lebih premium. |
| VO11 | 35.701–39.381 | AI bisa membuat motion selevel ini, asal prompt-nya tepat. |

## Order integrity
Filename-based order (VO01→VO11) reads as one continuous argument: problem → real cause → what to brief → result → AI PRENEUR method → conclusion. VO05+VO06 are one sentence split across two clips (comma at VO05 end) — kept as ONE visual scene. No cut words: every clip boundary falls in a pause (speech_on/off inside each cue, see transcript_machine.json).

## Flagged for user verification
1. **VO09 “AI PRENEUR”** — ASR wrote “AI perenior”. Audio is the brand name; displayed as the logo spelling **AI PRENEUR**.
2. **VO11 “prompt-nya”** — ASR wrote “prompnya”. Displayed as “prompt-nya” (same spoken word, standard spelling with hyphen).
3. **VO04 “brief-nya”** — ASR wrote “briefnya”. Displayed as “brief-nya”.
Also normalised: “AI-nya” (VO02). No numbers, no platform names, no URLs, no explicit CTA (no “follow/save/link”) were spoken.

## Word timing
Word starts are **estimated** (energy envelope + syllable-proportional distribution) and **anchored at 16 internal pauses whose word position was verified** by transcribing audio from segment start up to each pause (e.g. 13.11s → “Jadi bukan cuma bilang”, 23.06s → “…output secara”, 34.69s → “…jauh lebih”). Expected error ±0.12s off-anchor; anchored boundaries are exact to ~10ms. One gap at 22.66s is inside the word “output” (ignored).

## Derived content
- **Core takeaway:** hasil AI ditentukan oleh arahan / brief / prompt yang jelas — bukan oleh AI-nya.
- **Hook (VO01, 0.11s):** “Banyak orang bilang hasil AI itu masih biasa aja.”
- **Spoken CTA:** none. VO11 is a conclusion (“asal prompt-nya tepat”), not a follow/save CTA → no CTA invented.
