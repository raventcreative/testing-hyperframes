# SCENE BUILD BRIEF — "Lamaran jalan pas kamu tidur" (InstaJob) · AI PRENEUR reel remake · NAVY

Project root: `projects/lamarankerja_2026/` · 1080×1920 · 30 fps · 32.9333 s · HyperFrames 0.8.186.
VO (client's voice): "Kamu lagi tidur, tapi CV-mu lagi keliling ke banyak kantor. Namanya InstaJob. AI ini nyariin lowongan yang pas,
terus ngirim lamaranmu otomatis. Bisa lewat email, sampai ke LinkedIn, Glints, Jobstreet, dan Indeed. Kamu cukup atur sekali. Posisi,
lokasi, mode kerja, sampai batas lamaran per hari. Mau berhenti? Tinggal matiin kapan aja. Tapi ingat, wawancaranya tetap kamu yang
jalanin. Jadi rapiin dulu CV-mu. Mau tutorial lengkapnya? Komen KERJA, aku kirim lewat DM."
A REMAKE of a reference reel (do not copy it): our story is a NIGHT SHIFT — the host (3D mascot) sleeps, the AI PRENEUR robot works,
and the morning comes in s06. Client rules: premium motion, a different creative transition every scene, nothing AI-looking, real or
open-source assets only, never boring.

## Host layers (read; do not edit): index.html, compositions/sky.html, robot.html, mascot.html, s01.html
Paint order: navy background · **sky** (stars + crescent moon, night until s06, then dawn: moon sinks, warm glow, sun rises) ·
**scenes s01–s07 (yours)** · robot · mascot · white logo (top-left y 262–300) · captions.
- Captions: words on navy chips, white + cyan #01CCF7, centred at **y ≈ 960–1030** (one line).
- Mascot (host) half body bottom-left, head top ≈ y 1150, x 140–650 — ASLEEP (eyes shut, head drooping) until "Namanya" (4.5 s),
  then awake. Robot (worker) bottom-right ≈ x 700–960, y 1340–1680: types on a cyan holo keyboard during the hook and during "atur …
  hari.", presents "InstaJob.", scans on "nyariin", points up on "ngirim"/"LinkedIn"/"matiin", looks at the mascot on "wawancaranya".
- → **Your hero zone is y 290–935, x 60–1020** (keep x > 340 for y < 305 because of the logo). Nothing in y > 945.
- `s01` ends with: flip clock "02:01" dimmed (opacity .45, x 130–580, y 330–470, "DINI HARI" under it), a white CV card at x 400–680,
  y 360–730 (avatar, "CV" tag, lines, chips Desain/Konten/Excel), and an office skyline at y 690–930 (7 navy buildings, windows lit
  yellow). **s02 starts by rebuilding that end state exactly (copy the markup/CSS from s01) and transforming it** — a seamless hand-over.

## YOUR SCENES (ideas; make them better; every beat lands on its spoken word — see the timing table)
- **s02** "Namanya InstaJob. AI ini nyariin lowongan yang pas, terus ngirim lamaranmu otomatis." — the skyline + CV fold into a clean
  app window "InstaJob" (name as TEXT in a pill with a lucide briefcase icon — we have no rights to their logo, never draw one); a list
  of generic job cards (role, city/remote, a match % chip) scrolls; a scan beam (synced to the robot's scan) ticks the matching ones on
  "pas"; on "ngirim … otomatis." the matched cards whoosh off as sent (paper plane trails, "Terkirim ✓" toasts). No claims of volume.
- **s03** "Bisa lewat email, sampai ke LinkedIn, Glints, Jobstreet, dan Indeed." — a routing hub: the CV at the centre, an email
  envelope (lucide mail) lights on "email", then four channel pills (plain TEXT wordmarks in neutral white pills — no brand logos) light
  up one by one on their names, each with a flowing dashed line from the CV.
- **s04** "Kamu cukup atur sekali. Posisi, lokasi, mode kerja, sampai batas lamaran per hari." — a "Preferensi" panel: Posisi types
  "Social Media Specialist", Lokasi "Jakarta", Mode kerja segmented control → "Remote", Batas lamaran per hari slider → 30 (each on its
  word; per-letter tl.set typing; the robot types on its keyboard meanwhile). "sekali" = a single "Simpan ✓".
- **s05** "Mau berhenti? Tinggal matiin kapan aja." — a big "Auto apply" switch ON (cyan) → OFF on "matiin" (the robot points), the
  whole flow pauses (dims, a "Dijeda" chip, a pause icon).
- **s06** "Tapi ingat, wawancaranya tetap kamu yang jalanin. Jadi rapiin dulu CV-mu." — dawn (sky.html warms up from 22.7 s): a
  calendar invite card "Wawancara · Kamis, 10.00" slides in on "wawancaranya" (a generic event card, no company names); on "kamu yang
  jalanin" a small "kamu" tag points down toward the (now awake) host; on "rapiin dulu CV-mu" the CV card comes back and gets a quick
  polish checklist (Foto rapi ✓, Pengalaman jelas ✓, Skill relevan ✓) with a sparkle.
- **s07 CTA** "Mau tutorial lengkapnya? Komen KERJA, aku kirim lewat DM." — a comment row slides up (avatar circle with lucide user,
  input field), "KERJA" types itself big in cyan (per-letter tl.set) on "KERJA,", a heart pops; on "kirim" a paper plane carries a
  "Tutorial lengkap" card into a DM card ("Tutorial InstaJob — terkirim ✓", lucide message-circle / check) on "DM."; last ~1 s: calm end
  beat with the white logo `assets/brand/logo_white_trim.png` (the corner logo stays; keep the end card clean).

## STYLE LOCK
- Text **Poppins 700/400 only**: white `#ffffff`, cool `#e3edfa`, cyan `#01ccf7` / `#6adfff`; navy glass panels `rgba(12,22,64,.82)` with
  `inset 0 0 0 1.5px rgba(255,255,255,.10)` borders, radius 24–34, or white cards (`linear-gradient(180deg,#fff,#eef3fb)`) with navy text.
  Accents: green #2da44e (sent/ok), coral #e5484d (sparingly), warm #ffd66b (lit windows / dawn).
- Icons: `assets/icons/lucide-*.svg` (ISC): user-round, building-2, send, briefcase, mail, moon, star, check, settings-2, map-pin,
  calendar-check, file-user, power, sparkles, search, heart, message-circle. More: copy from
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/npm_lucide/package/icons/`.
- No brand logos (InstaJob/LinkedIn/Glints/Jobstreet/Indeed as TEXT only), no people photos, nothing AI-generated, no invented numbers
  presented as InstaJob's results (UI example values like a match % or a slider value are fine).

## Code conventions (deviations break the render)
- `<template>` + `<style>` + ONE root `<div id="root" data-composition-id="ID" data-width="1080" data-height="1920">` + `<script>` IIFE;
  the runtime strips the root id → `document.getElementById` on unique PREFIXED ids (`s03-…`); prefix classes and SVG ids.
- Timeline boilerplate exactly as `compositions/s01.html` (`_sc` patch, `ft`, `I`, `tl.set({}, {}, D - 0.01)`, seek-order patch,
  `window.__timelines["ID"] = tl`). D = the scene dur below; timeline length ≤ D. Use `wt(word, after)` on `window.VO_WORDS` for beats.
- Deterministic: no Math.random (seeded PRNG), no Date, no CSS animations/transitions, no rAF, **no onUpdate** (per-value tl.set windows
  for counters/typing). Give every fromTo COMPLETE from-values. One attr/clip-path tween per property; no svgOrigin in CSS-transformed SVG.
- Performance: transforms + opacity; no full-screen blur per frame; ≤ ~250 animated elements per scene.

## Checks (mandatory)
1. `node tools/check_scene.cjs <ids>` → `ok <dur>` (shared preview server on :3016 is running).
2. `npx --yes hyperframes@0.8.186 lint .` → 0 errors in your files.
3. Snapshots (`npx --yes hyperframes@0.8.186 snapshot . -o <your scratch dir> --at <≤8 times> --no-end --describe false --timeout 90000`)
   of the first frame, every beat and the last frame. LOOK at them: legible on a phone (≥ 20 px), inside the hero zone, nothing over
   captions/mascot/robot, transitions between scenes seamless (check the frame before and after each cut).
4. Report briefly. Do not commit. Edit only your scene files (+ new assets under `assets/fx/`).

## VERIFIED TIMING (global s)
- **s01** start 0.0 dur 4.4667 (end 4.4667): Kamu@0.32  lagi@0.58  tidur,@0.70  tapi@1.59  CV-mu@2.17  lagi@2.84  keliling@3.00  ke@3.55  banyak@3.67  kantor.@3.84
- **s02** start 4.4667 dur 5.9333 (end 10.4): Namanya@4.59  InstaJob.@5.40  AI@6.25  ini@6.66  nyariin@6.98  lowongan@7.45  yang@7.79  pas,@7.90  terus@8.54  ngirim@8.86  lamaranmu@9.27  otomatis.@9.69
- **s03** start 10.4 dur 4.2 (end 14.6): Bisa@10.53  lewat@10.91  email,@11.20  sampai@11.64  ke@11.96  LinkedIn,@12.10  Glints,@12.76  Jobstreet,@13.30  dan@13.88  Indeed.@14.08
- **s04** start 14.6 dur 5.7 (end 20.3): Kamu@14.85  cukup@15.30  atur@15.48  sekali,@15.67  posisi,@16.50  lokasi,@17.23  mode@17.95  kerja,@18.19  sampai@18.66  batas@19.05  lamaran@19.47  per@19.73  hari.@19.84
- **s05** start 20.3 dur 2.5 (end 22.8): Mau@20.59  berhenti?@20.81  Tinggal@21.52  matiin@21.89  kapan@22.07  aja.@22.31
- **s06** start 22.8 dur 5.2 (end 28.0): Tapi@23.13  ingat,@23.40  wawancaranya@23.93  tetap@24.62  kamu@25.13  yang@25.38  jalanin.@25.55  Jadi@26.36  rapiin@26.78  dulu@27.21  CV-mu.@27.36
- **s07** start 28.0 dur 4.9333 (end 32.9333): Mau@28.29  tutorial@28.67  lengkapnya?@28.86  Komen@29.68  KERJA,@30.12  aku@30.58  kirim@30.87  lewat@31.17  DM.@31.34
