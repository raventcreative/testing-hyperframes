# Transcript review — AI Engineer 2026 (VO: ElevenLabs "Dakocan", supplied by the user)

- Audio: `assets/audio/voiceover_final.mp3` (copied untouched from the upload), duration **113.006 s**. Video = VO + 0.33 s still hold = **113.3333 s**.
- Machine transcript: faster-whisper small (local CPU, language id) -> `production/whisper_transcript.json`. Every phrase matches `reference/02_VOICE_OVER_FINAL.txt`; whisper spellings that differ (`mesin learning`, `Kepet`, `Kenam`, `Kedulapan`, `Diploi`, `Test pake`, `10`) are recognition errors, the written script wins.
- Word timing master: MMS-300m CTC forced alignment (local ONNX) on the spoken form -> `production/word_timing.json` (240 words) + `production/phoneme_timing.json` (1389 phones, used for the mouth). Start = first phone - 20 ms; end = first 30 ms below -40 dB.
- Low-energy onsets flagged by the aligner are plosive starts after pauses (p/t/k: `Pahami`, `Pelajari`, `PyTorch`, `Tes`, `Perbaiki`, `Tapi`...) — expected, not misalignments.
- Disagreements > 0.25 s with whisper: `AI` (52.02 vs 52.30), `agent.` (68.82 vs 68.54), `Deploy` (85.08 vs whisper's merged `Diploi`). CTC is phone-level and kept; these words carry no hard visual apex.

## Recognition watch-list (brief section 5)

| # | script | spoken form | start | end | whisper nearest |
|---|---|---|---|---|---|
| 1 | AI | `eiai` | 0.42 | 0.82 | AI @ 0.38 (p 0.917) |
| 2 | agent | `ejen` | 0.80 | 1.04 | doang, @ 1.00 (p 0.966) |
| 8 | AI | `eiai` | 3.08 | 3.36 | AI @ 2.96 (p 0.292) |
| 9 | Engineer. | `enjinir` | 3.36 | 4.03 | Engineer. @ 3.28 (p 0.1) |
| 25 | AI. | `eiai` | 9.74 | 10.10 | AI. @ 9.62 (p 0.988) |
| 38 | API, | `eipiai` | 17.10 | 17.68 | API, @ 17.08 (p 0.88) |
| 40 | debugging. | `dibaging` | 17.84 | 18.39 | debugging. @ 17.80 (p 0.847) |
| 49 | software | `softwer` | 22.36 | 22.80 | software @ 22.42 (p 0.708) |
| 50 | engineering. | `enjiniring` | 22.80 | 23.39 | engineering. @ 22.68 (p 0.935) |
| 61 | AI | `eiai` | 28.40 | 28.82 | AI @ 28.22 (p 0.961) |
| 68 | machine | `mesin` | 31.60 | 31.98 | mesin @ 31.74 (p 0.532) |
| 69 | learning. | `lerning` | 31.98 | 32.37 | learning. @ 31.96 (p 0.099) |
| 86 | deep | `dip` | 40.12 | 40.38 | deep @ 39.96 (p 0.784) |
| 87 | learning. | `lerning` | 40.38 | 40.77 | learning. @ 40.32 (p 0.981) |
| 95 | PyTorch. | `paitorc` | 44.06 | 44.70 | PyTorch. @ 43.88 (p 0.888) |
| 97 | LLM. | `elelem` | 45.86 | 46.46 | LLM. @ 45.92 (p 0.97) |
| 101 | embedding, | `embeding` | 48.60 | 49.20 | embedding, @ 48.62 (p 0.874) |
| 108 | AI | `eiai` | 52.02 | 52.74 | AI @ 52.30 (p 0.971) |
| 113 | API, | `eipiai` | 54.88 | 55.48 | API, @ 54.80 (p 0.931) |
| 124 | RAG. | `rag` | 60.28 | 60.66 | RAG. @ 60.32 (p 0.767) |
| 142 | AI | `eiai` | 68.32 | 68.82 | AI @ 68.32 (p 0.956) |
| 143 | agent. | `ejen` | 68.82 | 69.12 | agent. @ 68.54 (p 0.418) |
| 162 | evaluation. | `ivaluasyen` | 77.24 | 78.05 | Evaluation. @ 77.28 (p 0.896) |
| 176 | production. | `prodaksyen` | 84.04 | 84.71 | Production. @ 84.10 (p 0.934) |
| 177 | Deploy | `diploi` | 85.08 | 85.56 | sistemnya. @ 85.50 (p 0.966) |
| 192 | AI? | `eiai` | 93.08 | 93.45 | AI? @ 92.94 (p 0.96) |
| 216 | AI | `eiai` | 103.34 | 103.60 | AI @ 103.18 (p 0.984) |
| 217 | Engineer | `enjinir` | 103.60 | 104.16 | engineer @ 103.50 (p 0.302) |
| 223 | tools. | `tuls` | 105.46 | 105.89 | tools. @ 105.38 (p 0.914) |
| 229 | AI | `eiai` | 107.74 | 108.08 | AI @ 107.60 (p 0.987) |
| 234 | roadmap | `roudmep` | 110.42 | 110.76 | roadmap @ 110.36 (p 0.82) |
