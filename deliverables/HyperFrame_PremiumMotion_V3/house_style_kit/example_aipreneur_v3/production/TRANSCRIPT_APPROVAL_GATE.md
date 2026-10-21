# TRANSCRIPT / SUBTITLE LOCK BEFORE FINAL BUILD

This project does NOT contain a verified transcript. Voice-over is the user's exact editorial authority.

1. Transcribe `assets/audio/vo_master_39s.wav` locally using an Indonesian-compatible MULTILINGUAL ASR engine. The official CLI documents `npx hyperframes transcribe`; on the installed version first run `npx hyperframes transcribe --help`, inspect supported languages/models. `small.en`/`medium.en` are ENGLISH-ONLY; avoid these for Indonesian. `large-v3` may be supported but downloading large models needs user approval if resources/cost/connection are material.
2. Save machine transcript and word timings into new production files, e.g. `production/transcript_machine.json` and `production/transcript_review.md`. Clearly label `machine` until confirmed; don't silently mark machine output verified.
3. Verify proper nouns, named platforms, numbers, negation words, dates, and CTA against master audio or each original segment. A model-generated guess is not proof.
4. Confirm 11 sections flow together naturally. If they're misordered, stop and obtain ordering rather than silently guessing.
5. Derive exactly quoted copy for each beat from the verified words; do not show subtitles or graphics with unsupported claims.
6. If unable to verify, stop at content gate and ask for user's transcription (not new script rewriting).
