# SCENE BRIEF — "Panel rekrutmen 7 Claude" · AI PRENEUR remake R1 · NAVY

Project root: `projects/aip_r1_panelcv/` · 1080×1920 · 30 fps · 44.2 s · HyperFrames 0.8.186. Built from the NAVY kit `projects/igagent_2026/`.
VO + facts: `production/VO_SCRIPT.md`. Timing: `production/timing.json` / `vendor/vo_words.js` (VO starts at 0.3 s).

## Layers (index.html, built by `python3 -I tools/build_index.py .`)
navy bg · scenes s01–s08 · **panel** (`compositions/panel.html`, persistent jury rail) · robot · mascot · white logo (fades 42.8 s) · captions.
- Captions: word chips, white + cyan, y ≈ 960–1030. Mascot bottom-left (head ≈ y 1150), robot bottom-right. Hero zone y 290–935.
- `vendor/cvkit.js` (loaded in <head>) = the shared hero objects: `CVK.cv(prefix, id, ver)` (THE CV, base 460×560, v1 / v2 rows),
  `CVK.css(prefix)`, `CVK.JUDGES` (7 reviewers: role · lucide icon · colour), `CVK.NOTES` (one note per reviewer), `CVK.STAMPS`,
  `CVK.SEAT_X(k)` / `CVK.CMP_X(k)`, `CVK.CLAUDE` (lobe Claude mark), `CVK.isvg` (lucide 1.70, ISC).

## The jury rail (panel.html)
7 judge cards 124×156 (Claude mark + persona chip + "#k" + role), seats top y 314, centres x 540 + (k-4)·134, nameplate table
"PANEL REKRUTMEN" y 448–498 in front. Status dot: grey idle · cyan reading · coral flagged · green fixed. Lit = scale 1.08 + colour ring.
- s01: empty dashed seats at frame 0 → cards drop in on "7"; dots cyan on "Tugasnya", coral per stamp on "nolak".
- s02: rail lifts away. s03: back, #1 lit. s04: #2 lit. s05: #3–#7 lit, glass walls between them ("sendiri-sendiri"), glasses on
  "kacamata", #3/#4/#5 pop on their words. s06–s07: COMPACT (scale .55, centres x 540 + (k-4)·76, role → big "#k"), dots turn
  green at the s06 fix times (FIX, shared with s06). s08: leaves at 39.46; returns as the end signature under the logo (y 480–566).

## Scenes
| id | time | beat |
|---|---|---|
| s01 | 0.00–5.73 | HOOK: CV under a spotlight + empty seats → 7 Claude reviewers take their seats → sight-lines → 7 TOLAK stamps → "7× ditolak" |
| s02 | 5.73–11.30 | the CV shrinks into "Riwayat lamaran": 36 tiles sent (counter 0→36) → all flip to rejected → HRD email, "Alasan:" empty → big "?" |
| s03 | 11.30–16.73 | #1 Sistem ATS: keyword panel (Digital Marketing / Meta Ads / Copywriting / Canva), scan line, ✓/✗, match 1/4, barrier before "Meja HRD (manusia)" |
| s04 | 16.73–21.17 | #2 Hiring Manager: pen circles the vague bullet; "Layak dipanggil interview?" selector lands on "Belum dulu" — "hasil kerja tanpa angka" |
| s05 | 21.17–28.00 | 5 copies in 5 locked booths ("Nggak saling nyontek"), lenses in each colour, quote card: #3 "Inisiatif kamu mana?", #4 "CV-ku lebih spesifik dari ini.", #5 "Dampaknya ke bisnis apa?" |
| s06 | 28.00–34.43 | copies merge into one CV; 7 notes fly in as wired tags + "7 catatan"; rewrite line by line (placeholders "angka"), tags turn green, counter → 0, "CV v2" |
| s07 | 34.43–39.80 | certificate "Dijamin diterima kerja" struck "BUKAN" + torn; timeline: Panel 7 Claude (DULUAN, "7 alasan ketemu") → CV v2 → HRD (NANTI, hourglass) |
| s08 | 39.80–44.20 | CTA: WORKFLOW card "Panel 7 Claude" (lock) → comment "CV" → heart → paper plane → DM "Workflow Panel 7 Claude · terkirim ✓" → logo + 7 cards |

## Conventions (same as the kit)
`<template>` + prefixed ids/classes; GSAP timeline with the `_sc` patch, `ft`, `I`, chained `KF(el, init, steps)` (one KF per element
per property set — a second KF/I on the same property re-pins it at 0), `tl.set({}, {}, D - 0.01)`, seek-order patch. Deterministic.
Every scene's frame 0 = the previous scene's end (s01→s02, s03→s04, s04→s05, s05→s06, s06→s07 hand-over), s02→s03 and s07→s08 are
quick push/fade resets. SFX: `python3 -I tools/sfx.py .`. Cover: `thumbnail/cover.html` → `node thumbnail/render_cover.cjs <png>` (server :8821).
