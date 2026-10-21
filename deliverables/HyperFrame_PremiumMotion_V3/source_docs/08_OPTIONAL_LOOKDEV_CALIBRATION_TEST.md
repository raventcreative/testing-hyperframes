# 08 — OPTIONAL 12-SECOND REF-H CALIBRATION TEST (V3.0)

**Status:** optional smoke test for a fresh Claude Code workspace or a new machine. It checks that the house style (REF-H) is reproduced before spending time on a real Reel. Original fictional text, no real claims, no audio. **Not a deliverable.** Render only if the user deliberately runs the test, and only after the preview gate.

**Pass condition:** the 4 scenes, placed next to `golden_frames/` (e.g. H03, H06, H12, H18), look like the same series: light ice-ivory world, one big detailed lit hero per scene, contact shadows, far blurred discs, a small top caption only, an apex burst on the key word, and a still final lockup.

## READY-TO-PASTE CLAUDE CODE PROMPT
```text
[ROUTE] general-video. Use house_style_kit/starter (copy into a new project projects/refh-calibration/ after `npx hyperframes init refh-calibration --example blank --resolution portrait --non-interactive --skip-transcribe`). Read source_docs/11, 12, 13 and view golden_frames/ before building.

[SPEC] 1080×1920, 30 fps, 12.0 s, no audio (remove the <audio> element). Caption words are timed from the table below (no VO).

[SCENES] (caption text = the exact words; key word in navy)
| s01 | 0–3 s | "Ide bagus" (key: bagus @1.2) | a porcelain lightbulb on a pedestal; the filament draws in and the bulb lights up at 1.2 with a glow + shockwave + sparkles |
| s02 | 3–6 s | "butuh arah" (key: arah @4.4) | a porcelain compass with a navy needle swinging and settling on N at 4.4; tick ring, glass cover with a rim highlight |
| s03 | 6–9 s | "yang jelas" (key: jelas @7.3) | a frosted glass panel with abstract layout blocks going blur→sharp at 7.3 behind a focus ring |
| s04 | 9–12 s | "biar hasilnya premium" (key: premium @10.4) | a faceted gem rising onto a porcelain plate; ray burst at 10.4; still final frame by 11.6 |

[HOUSE STYLE LOCK] paste from doc 02.
[SCENE CONTRACT] paste from doc 02.
[QA] lint 0 errors; snapshot each scene (cut + key word + end) and compare side by side with golden_frames; check 0 errors; determinism 0 px; report honestly whether it matches REF-H and what differs.
```
