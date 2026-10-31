# QA — assembled preview (out/claude_code_3d_remake_preview_draft.mp4, draft quality)

- ffprobe: H.264 1080x1920, 2217 frames @30 fps, 73.90 s; AAC. VO head -18 dB at 0.5 s, speech -14.8 dB mid, CTA tail -24 dB at 72.5 s, clean silence at 73.6 s (logo hold).
- VO: user's ElevenLabs file once from 0 (no TTS, no speed change). Word timing = local MMS CTC forced alignment (169 words); whisper transcript matches the script.
- Lint: 0 errors (8 warnings: one large captions file + overlapping-tween notices, visually checked).
- Transitions: 17 cuts sampled at -6 / 0 / +6 frames (qa/transitions/grid.jpg). No black gaps, no frozen frames.
  - FIX BEFORE FINAL: S14->S15 playhead matte fills the frame with full cyan for ~0.25 s (too harsh) -> lower to a 35 % cyan wash.
  - Minor: some headings show their empty plate for ~0.1 s before the first word rises.
- Logo: genuine logo_trim.png upper-left all scenes, 14 masked sheens, 3 % pulses at SATU KALIMAT / 06 / ANIMASI, calm hold at the end.
- Mascot: texture-repaired GLB (mascot_jas3_clean.glb), lip sync to VO, faces viewer; 12/18 scenes. Known limits: no finger bones (open-hand pointing), residual cuff/pocket fringe visible only in close-ups.
- S15 before/after uses the real jacket crops (before vs after the texture repair).
