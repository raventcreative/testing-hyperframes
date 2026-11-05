# SCENE BUILD BRIEF — Cloudflare Security Audit Skill reel (AI PRENEUR)

Project root: `projects/cloudflare_audit_2026/` · 1080x1920 · 30 fps · 48.6667 s (1460 frames). The host `index.html` renders the user's navy background, the word-synced top caption (y ≈ 214–340), a vignette+grain layer, the VO and the 3D mascot layer. Each scene is ONE sub-composition `compositions/sNN.html` (currently empty placeholders for s04–s15).

## QUALITY BAR = the approved lookdev
The client approved scenes s01–s03. Read `compositions/s01.html`, `s02.html`, `s03.html` fully before building: same visual language, same craft level, same code conventions (seeded PRNG, `ft()` fromTo helper with immediateRender:false, tl.set at 0, the seek-order safety patch before registration). The rendered lookdev is `out/LOOKDEV_8detik.mp4` (extract frames with ffmpeg to look at it).

## STYLE LOCK (client-chosen — overrides any older house style)
- Background: the client's dark navy gradient is drawn by the host. Scenes have NO full-screen opaque background; keep the navy visible. No ivory/pastel plates, no neon purple, no black voids, no red.
- Typography: Poppins 700 + Poppins 400 ONLY for editorial text (host loads them). White #FFFFFF for main words, cool white #E3EDFA for secondary, cyan #01CCF7 for 1–3 key words. The crisp white rectangle + cyan bold text marker is reserved for apex words (the host caption already uses it). Code / paths / commands from real sources may use "DejaVu Sans Mono" (installed).
- Materials: dark navy glass cards (linear-gradient(165deg, rgba(23,38,78,.97), rgba(10,17,44,.98)) + 1.5px white inset hairline + deep drop shadow), cyan light (#01CCF7 → #6ADFFF) with bloom, small white sparkles. Amber #F2C46D ONLY for 'candidate / needs validation', mint #9FD8C4 ONLY for 'confirmed'. No green ticks unless it is the 'confirmed' lane.
- RECURRING VISUAL THREAD (from the Amazon 'From A to Z' reference: the brand light connects every stage): a cyan light line/edge must carry the eye INTO and OUT OF every scene — e.g. a frame border that draws itself, an underline that extends, a cable, a scan line, a ring that morphs into the next shape. Each scene's exit should hand its shape/motion to the next scene (match cut), see the continuity list.
- Motion: frame 0 already shows a large, legible hero. Vary the camera and the transitions (dolly, whip with motion blur, 180° pivot, rack focus, mask wipe, match cut, snap zoom) — no two consecutive scenes with the same move. 3 depth planes (far blurred text/props, hero, near blurred motes). Apex on the key spoken word ±0.05 s: glint/bracket/flash/scale pulse — tasteful, not a shockwave on every noun. ~0.4 s calm reading holds between big moves.
- Hero zone x 50–1030, y 400–1520 (caption above y≈360). Hero 60–75 % of it, readable at phone size.

## TRUTH RULES (non-negotiable)
- Public source = https://github.com/cloudflare/security-audit-skill (README.md and skills/security-audit/SKILL.md are in `assets/src/` — the ONLY source of product text/labels). The README describes six phases (reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, reporting) and three verdicts `confirmed` / `needs_validation` / `rejected`.
- NEVER invent findings, vulnerabilities, file paths of a scanned target, counts, severities, terminal output, 'scan complete'/'install success' messages, or any Cloudflare endorsement. Agents, maps, lanes, verifier, triage and report visuals are CONCEPTUAL illustrations (abstract bars/dots/nodes) — they must not look like a real audit result. Candidate = amber with a question glyph, never a red bug.
- On-screen editorial text = spoken words of that scene, exact quotes of official README/SKILL.md labels, real command `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit`, or a short source credit like `sumber: github.com/cloudflare/security-audit-skill`.
- Real assets you may use: `assets/src/cloudflare_avatar.png` (genuine Cloudflare logo, 400x400, white bg — show it on a white rounded tile, never recolour), `assets/src/README.md`, `assets/src/SKILL.md` (render exact excerpts), `assets/src/web_page_top.jpg` (real AIpreneur website capture 1200x3600), `assets/brand/logo_trim.png` (genuine AI PRENEUR logo, WHITE on transparent, 1199x119 — s15 lockup only, set width only), `assets/brand/cursor_trim.png` (a cursor). A REAL project file tree you may show (this very project, owned by the creator): `projects/cloudflare_audit_2026/` → assets/ (audio, brand, fonts, mascot3d, src), compositions/ (s01.html … s15.html, mascot.html), production/, tools/ (align.py, build_index.py), vendor/, index.html, hyperframes.json, package.json — and you may quote real lines from those files as 'source code' crops.

## MASCOT (host layer, do NOT add one in scenes)
The 3D mascot is drawn by `compositions/mascot.html` above the scenes in three windows: s01 (bottom-right), **s07** (big, centred: feet below the frame, figure from y≈830 down — keep the centre-bottom free of important hero detail during s07; your hero can sit higher/behind and the mascot 'taps' your pause pane), **s15** (left side, y≈1250–1920, from s15 start +0.05 s to +1.55 s, then it drops out — keep the left-bottom free in that window; the final still logo lockup must be fully visible and calm in the last 0.6 s).

## VERIFIED TIMING (local seconds = global − scene start; DUR in the scene must equal the slot duration)
- **s01** start 0.0 s, DUR 3.7667 s — "Website buatan AI kamu keren. Tapi aman belum?"
  - Website 0.13, buatan 0.58, AI 1.01, kamu 1.34, keren. 1.77, Tapi 2.69, aman 2.84, belum? 3.05
- **s02** start 3.7667 s, DUR 3.3333 s — "Ini ada skill open-source dari Cloudflare yang menarik banget."
  - Ini 0.07, ada 0.45, skill 0.71, open-source 0.97, dari 1.38, Cloudflare 1.81, yang 2.06, menarik 2.30, banget. 2.72
- **s03** start 7.1 s, DUR 2.2333 s — "Namanya Security Audit Skill."
  - Namanya 0.17, Security 0.78, Audit 1.38, Skill. 1.75
- **s04** start 9.3333 s, DUR 3.5 s — "Kamu pasang di coding agent, lalu arahkan ke project milikmu."
  - Kamu 0.15, pasang 0.37, di 0.78, coding 1.02, agent, 1.22, lalu 1.70, arahkan 1.98, ke 2.32, project 2.60, milikmu. 2.85
- **s05** start 12.8333 s, DUR 3.7667 s — "Pertama, dia memetakan kode dan jalur akses aplikasi."
  - Pertama, 0.13, dia 0.69, memetakan 0.92, kode 1.51, dan 1.93, jalur 2.08, akses 2.39, aplikasi. 2.78
- **s06** start 16.6 s, DUR 4.1333 s — "Setelah itu, beberapa agent berburu potensi celah dari sisi berbeda."
  - Setelah 0.19, itu, 0.61, beberapa 0.95, agent 1.59, berburu 1.87, potensi 2.30, celah 2.70, dari 3.00, sisi 3.23, berbeda. 3.50
- **s07** start 20.7333 s, DUR 2.9667 s — "Tapi tunggu, ini bagian yang paling keren."
  - Tapi 0.15, tunggu, 0.53, ini 1.02, bagian 1.43, yang 1.78, paling 2.04, keren. 2.26
- **s08** start 23.7 s, DUR 2.3333 s — "Kalau satu agent merasa menemukan masalah,"
  - Kalau 0.17, satu 0.45, agent 0.76, merasa 0.97, menemukan 1.30, masalah, 1.81
- **s09** start 26.0333 s, DUR 3.4334 s — "agent lain justru ditugaskan untuk membantah temuannya."
  - agent 0.11, lain 0.55, justru 0.75, ditugaskan 1.08, untuk 1.69, membantah 2.07, temuannya. 2.73
- **s10** start 29.4667 s, DUR 1.7666 s — "Bukan asal kasih peringatan."
  - Bukan 0.16, asal 0.47, kasih 0.73, peringatan. 1.01
- **s11** start 31.2333 s, DUR 4.6 s — "Hasilnya dipisah: terkonfirmasi, masih perlu diperiksa, atau ditolak."
  - Hasilnya 0.06, dipisah: 0.64, terkonfirmasi, 1.39, masih 2.02, perlu 2.47, diperiksa, 2.74, atau 3.54, ditolak. 3.83
- **s12** start 35.8333 s, DUR 3.6 s — "Lalu disusun jadi laporan yang bisa kamu cek satu per satu."
  - Lalu 0.14, disusun 0.51, jadi 0.84, laporan 1.26, yang 1.59, bisa 1.77, kamu 2.10, cek 2.34, satu 2.54, per 2.85, satu. 3.12
- **s13** start 39.4333 s, DUR 4.2334 s — "Perlu diingat, ini alat bantu audit, bukan jaminan website aman."
  - Perlu 0.14, diingat, 0.42, ini 1.03, alat 1.35, bantu 1.55, audit, 2.06, bukan 2.42, jaminan 2.69, website 3.30, aman. 3.61
- **s14** start 43.6667 s, DUR 2.8 s — "Mau link resmi, cara pasang, dan contoh prompt-nya?"
  - Mau 0.16, link 0.42, resmi, 0.61, cara 1.06, pasang, 1.32, dan 1.72, contoh 1.93, prompt-nya? 2.22
- **s15** start 46.4667 s, DUR 2.2 s — "Komen AMAN. Aku kirim panduannya."
  - Komen 0.18, AMAN. 0.43, Aku 0.98, kirim 1.22, panduannya. 1.49

## STORYBOARD + CONTINUITY (s01–s03 done)
- **s04** Kamu pasang di coding agent, lalu arahkan ke project milikmu. — continues from s03's install-command box: a navy caret runs along the REAL command (readable, large); on 'coding agent' the command plate docks into a sleek abstract 'agent' glass console (no product UI, no output text); the caret stretches into a curving cyan cable that dives into the REAL project file tree (this project's folders) on 'project'. Exit: the cable splits into route lines.
- **s05** Pertama, dia memetakan kode dan jalur akses aplikasi. — overhead-to-angled camera over a large 2.5D board showing the real file tree / real code crop; a CONCEPTUAL route map draws itself (nodes + paths), 2–3 branches light up; one trace arrives on 'jalur akses'. Optional tiny quote of the README phrase 'map architecture, trust boundaries, input surfaces'. Exit: lines open into four lanes.
- **s06** Setelah itu, beberapa agent berburu potensi celah dari sisi berbeda. — four deep, angled lanes each carrying a different REAL code crop; four small schematic magnifier 'hunters' sweep independently, camera tracks laterally then rises to overhead; amber CANDIDATE glints (question glyph) on 'potensi', never 'confirmed'. Exit: the four lanes converge into one centred amber tile.
- **s07** Tapi tunggu, ini bagian yang paling keren. — FREEZE BEAT: every lane/hunter brakes hard on 'tunggu' (motion stops, a slim glass pause pane slams into place; the host mascot taps it). Then a rack focus to the BACK of the pane. Keep the centre-bottom clear for the mascot. Exit: the pane starts rotating (180°) → s08.
- **s08** Kalau satu agent merasa menemukan masalah, — one amber HYPOTHESIS tile (question glyph, abstract evidence lines, no file/path) floats beside a real code crop; inspector lens #1 lands on it on 'masalah'; the camera begins to orbit. Exit: camera continues around the tile's far edge.
- **s09** agent lain justru ditugaskan untuk membantah temuannya. — SIGNATURE 180° pivot: the camera completes the orbit and reveals a clearly different second inspector (verifier) on the opposite side of the same tile; on 'membantah' it pressure-tests the tile (tile flips/reorients, evidence lines realign, crisp glint). Optional exact README quote 'candidate validation'. Exit: the pressure flips the tile toward a filter slot.
- **s10** Bukan asal kasih peringatan. — fast tactile question-mark STAMP hits the tile on 'Bukan' (no green check); on 'peringatan' the tile drops through a precise paper slit. Short scene (1.77 s) — one strong move.
- **s11** Hasilnya dipisah: terkonfirmasi, masih perlu diperiksa, atau ditolak. — three kinetic intake lanes/chutes; on each spoken category one conceptual tile snaps into its lane: 'terkonfirmasi' → mint lane labelled `confirmed`, 'masih perlu diperiksa' → amber lane `needs_validation`, 'ditolak' → neutral grey lane `rejected` (official README labels, plus the spoken Indonesian word). No counts, no claims a real scan ran. Exit: lanes merge into a report spine.
- **s12** Lalu disusun jadi laporan yang bisa kamu cek satu per satu. — report pages assemble with a stapled mechanical motion; use EXACT README text about the output (e.g. the line about findings.json / report-schema.json, or 'The verdicts are distinct…') or clearly blank conceptual pages; pages flip one by one on 'satu per satu'. Exit: a page corner becomes the shield outline.
- **s13** Perlu diingat, ini alat bantu audit, bukan jaminan website aman. — an elegant semi-transparent blue-white glass shield over the navy; on 'alat bantu audit' it reads solid; on 'bukan jaminan' the camera orbits to reveal a deliberate small open inspection seam (honest: no 100 % safety). Calm, credible, no alarm graphics. Exit: the seam/outline unwinds into a chat bubble.
- **s14** Mau link resmi, cara pasang, dan contoh prompt-nya? — three tangible panels orbit a central comment input with clear negative space, each snapping forward on its spoken word: 'link resmi' → `github.com/cloudflare/security-audit-skill` (with the genuine logo tile), 'cara pasang' → the real install command, 'contoh prompt-nya' → a folded prompt note with ABSTRACT lines only (no invented prompt text). Each readable ≥0.5 s. Exit: a cursor drops into the comment field.
- **s15** Komen AMAN. Aku kirim panduannya. — a giant comment card; the cursor types 'AMAN' (Poppins 700 cyan on a crisp white rectangle) exactly on 'AMAN' (host mascot points from the left until ~1.55 s local); then the card slides down to reveal the genuine AI PRENEUR logo (white, assets/brand/logo_trim.png, width ~620) on a subtle dark-blue glass lockup plate with a thin cyan reflected accent. The last 0.6 s must be COMPLETELY still (no drift, no particles moving over it). No fade to black.

## SCENE CONTRACT
- Write ONLY your assigned `compositions/sNN.html`. Structure exactly like s01–s03: `<template>` with scoped `<style>`, `<div id="root" data-composition-id="sNN" data-width="1080" data-height="1920">`, one IIFE script with `gsap.timeline({paused:true})`, the seek-order safety patch, then `window.__timelines['sNN']=tl` LAST.
- Prefix every class/id/SVG id with `sNN-`; query only inside the scene root.
- `tl.set` initial states at 0 first; then `fromTo(..., {immediateRender:false})`; never `gsap.from`; never tween left/top/width/height; no CSS transform + GSAP transform fight on one element. If one property is animated by several tweens, make each tween's FROM equal the previous TO, or use one tween with a custom ease (see s01's peel).
- No Math.random/Date/rAF/timers/repeat:-1/play(); seeded PRNG only. No <video>/<audio> in scenes. Static images allowed.
- Check your work: from the project root `npx --yes hyperframes@0.8.186 snapshot --at <global seconds>` (entry +0.1 s, each apex, exit −0.1 s) and LOOK at the PNGs; iterate at least twice; `npx --yes hyperframes@0.8.186 lint` must show 0 errors (the host's nested_structure warnings are expected).
- Do not edit index.html, other scenes, timing or assets; do not render, commit or push.