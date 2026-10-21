# F. QA ACCEPTANCE CRITERIA — PRODUCTION FINAL

## Required gates

| QA gate | Acceptance / PASS | Failure / repair required |
|---|---|---|
| Audio order | 11 source clips menciptakan rangkaian kalimat yang coherent dan sesuai maksud user; mapping `production/audio_timeline.json` dipakai | Klip tertukar, kata terpotong, gap buatan, overlap yang mengganggu |
| Transcription | Exact words, nama produk/merek, numerals, hook, CTA diverifikasi dari audio; subtitle sync per frasa/kata | AI menulis copy/CTA/claim yang tidak ada di VO, ASR hallucination |
| Runtime | Canvas native 1080×1920, 9:16, 30fps, final 39.40s (1182 video frames) toleransi codec normal | Landscape/crop, duration mismatch, tail hitam/diam panjang |
| Audio mix | Master WAV hanya sekali, audible until 39.381s, tidak clipping/garbled; other SFX minimal and below VO | WAV + 11 parts dimainkan bersamaan, dua suara dobel, abrupt speaker split, bass masking |
| Brand lock | Logo AI PRENEUR asli utuh, BG mirip image asli, bukan re-created misleading logo | Warped/recolored/deformed logo, huruf rusak, BG berubah jauh tanpa motivasi |
| Hook narrative | Opening mulai cepat dengan frasa yang benar-benar muncul di VO; satu focal object dan teks terbaca | Generic intro/logo sting yang menghabiskan hook, klaim tidak ada di VO |
| Mobile/safe zone | Critical text roughly x90–900 y220–1540 (heuristik saja), 2 lines captions readable, gesture/UI rail aman pada mobile preview | Teks kecil, cut off, overlay bawah kanan, copy over object tanpa contrast |
| 3D/depth QA | Hero shots menunjukkan minimal 3 depth cues: perspective/thickness + coherent occlusion + contact shadow/light or parallax | Rounded flat rectangles & shadow-only disebut "3D", perspective/artifact morphing patah |
| Material/glass QA | Tinted translucent, controlled edge response, soft separation, coherent upper-left key, credible contact/cast shadow; check mid-tween | Opacity-only glass, highlight/shadow contradictory, broken backdrop-filter |
| Motion grammar | For each beat entry / anticipation / main action / apex keyed to VO / settle / hold / handoff, different mechanisms for different meanings | All text rises/fades identically, endless floating, whip transition random |
| Technical seek safety | Arbitrary timeline seeks produce same frame, motion no jumps, shared 30fps clock | Wall-clock/random independent RAF, manual media.play or currentTime, async inconsistent render |
| Core HyperFrames QA | `npx hyperframes lint` completed, `npx hyperframes check --snapshots` completed per installed version, snapshot visual inspection | Lint/check errors ignored, scene offscreen, name/path broken, unreviewed code-only success |
| Preview/render gate | Full assembled preview displayed and official user approval obtained BEFORE final export | Bypass checkpoint, render status claimed without actually rendering |
| Final MP4 | File truly exists, nonzero, metadata verified, visual frame review hook/hero/transition/end, audio stream correct | Empty/broken link, wrong specs/codecs, missing audio or black frames |

## Sampling plan (candidate absolute seconds; adapt to final semantic cuts)

- Opening: `t=0.20, 0.65, 1.40, 2.70`
- Mid-scene and boundary: `t=5.70, 6.08, 8.60, 11.85, 14.70, 16.30, 18.50`
- Semantic interaction: `t=20.10, 22.80, 24.40, 27.80, 29.50, 32.80, 35.60`
- Outro: `t=36.00, 37.10, 38.70, 39.30`

At each perspective/hinge/selection: inspect **motion midpoint** and final hero frame. Mid-tween fail is fail even if first/end stills look okay. If `*.motion.json` supported locally, assert `appearsBy`, `staysInFrame`, `keepsMoving` only with validated schema and selectors.

## Blocking scenario

If no reliable transcript can be produced from the files, output **BLOCKED: TRANSCRIPT NEEDED**, provide what was built independently (media inventory, logo/background lookdev, 39.4s timing manifest), request the original script/transcript. **Do not generate fictional text, subtitles, or assert a fully locked story.**

## Completion report

Claude Code reports: verified Windows output project path, file MP4 path **only after successful render**, exact duration/fps/resolution/audio streams, status lint/check/snapshots/preview/review/approval, narrative text gate status, visual depth self-review, repairs and blockers. Distinguish visual review from automatic CLI pass.
