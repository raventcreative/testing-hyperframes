# Transcript review — `assets/vo_elevenlabs_final.mp3`

## File check (ffprobe / ffmpeg, measured)
| Item | Result |
|---|---|
| Codec / channels / rate | MP3, mono, 44 100 Hz |
| Duration | 61.074 s (matches handoff 61.07425 s) |
| Decode | full decode with ffmpeg, no errors |
| Loudness | mean −17.8 dB, peak −0.7 dBFS (no clipping measured) |
| Leading silence | ~0.04 s (speech starts at the very start) |
| Last word ends | 60.864 s; file tail silence 0.21 s |
| Last sentence intact | yes — Whisper hears "nanti gue bagiin" fully before the tail silence |
| MD5 | 2628b7be63b8e063a4d0fc4876da7d45 (identical to the ZIP copy) |

The old source voice `voice_source_full.m4a` was NOT copied into the project and is not in the timeline.

## ASR used
- HyperFrames `transcribe` v0.8.186 → whisper.cpp **large-v3**, `--language id` (full file) → `production/transcript_machine.json`.
- Re-checks on cut clips with large-v3 (id, unbiased, no prompt) and large-v3 (en) for the English product name.
- Note: I cannot listen to audio. "Review" here = two independent ASR passes + waveform measurements, not a human ear.

## Verbatim comparison vs `07_VO_ELEVENLABS_READY.txt`
145 canonical words. All sentences, order and wording match, except these items:

| # | Canonical | Machine heard | Re-check | Status |
|---|---|---|---|---|
| 1 | "efek **per katanya**." (2.84–4.07 s) | "efek **perkataannya**." | 2 more passes: still "perkataannya" | **FLAG — Freddie please listen.** Could be Whisper merging into a real word, or the TTS really said "perkataannya". Captions show the script ("per katanya"). |
| 2 | "seperti **Claude** Code" (≈13.05 s) | "seperti **Cloud** Code" | id + en passes: "Cloud Code" | **FLAG — pronunciation.** Very likely ElevenLabs pronouncing "Claude" like "klaud". Wording is the same; caption shows the real product name "Claude Code". If the pronunciation bothers you, re-generate only this phrase. |
| 3 | "panduan **instalnya**?" | 1st pass "pandu? Pertanyaannya," | clip pass: "**panduan installnya**?" | OK — 1st pass misheard; spoken text matches. |
| 4 | "Komen **HYPIT**." | "komen hype it" | clip pass: "komen hype it" | OK — that is how "Hypit" is pronounced (hype-it). |
| 5 | "Framework-nya", "B-roll", "produksinya:" | "Frameworknya", "b-roll", "produksinya," | — | OK — spelling/punctuation only. |

No missing or extra sentences. No source/old narration detected. Nothing materially different → synced build proceeds; items 1–2 are listed in the approval request.

## Pauses (measured, silencedetect −38 dB / 60 ms) used as anchors
viral, 2.43–2.54 · katanya. 4.07–4.30 · Hypit, 5.36–5.56 · stars. 9.02–9.33 · Code, 13.73–13.89 · kode. 16.67–17.06 · produksinya: 20.32–20.65 · footage, 21.25–21.33 · caption, 21.97–22.05 · efek. 23.12–23.42 · skrip, 24.99–25.25 · lagi. 27.75–28.19 · jualan. 29.91–30.29 · dipertahankan, 31.78–31.95 · hook, 32.83–32.92 · presenter, 33.67–33.84 · ganti. 35.85–36.03 · nol. 40.52–40.91 · orang. 42.82–42.95 · musik, 44.00–44.11 · jelas. 46.70–47.06 · mulai, 47.69–48.00 · agent, 49.81–49.90 · brief. 51.66–51.88 · source, 53.62–53.70 · berbayar. 56.48–56.90 · instalnya? 58.54–58.92 · HYPIT. 59.71–60.07

## Word timing method & accuracy (honest)
1. Whisper words mapped by position onto the canonical script (reviewed table in `tools/align_words.py`).
2. Every punctuation pause anchored to the measured silence above (boundary accuracy ≈ ±0.02 s).
3. Words between two anchors: average of Whisper's relative timing and a syllable-proportional estimate, snapped to genuinely quiet frames (< −40 dB) within ±70 ms.
4. Accuracy: words right after a pause (most apex words are) ≈ ±0.03 s; interior words estimated ≈ ±0.1 s. Not hand-verified by ear.

Output: `production/word_timing.json` (words, caption groups, audio facts). Scenes: `production/scenes.json` + `production/storyboard_locked.md`.

## Timeline length
Video 61.100 s = 1833 frames @ 30 fps (covers the full 61.074 s MP3, nothing stretched or re-pitched). Tail after the last word: 0.236 s, plus the CTA visuals settle ~1 s before the end, so the final still is calm. Option for Freddie: add ~0.5 s silent hold at the end if you want a longer final still (the MP3 itself stays untouched).
