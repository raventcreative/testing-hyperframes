# SCENE BUILD BRIEF — "9 aplikasi berbayar vs kembaran gratisnya di GitHub" (AI PRENEUR reel, remake)

Project root: `projects/repo9_2026/` · 1080x1920 · 30 fps · 56.0667 s · HyperFrames 0.8.186.
Story: 9 paid apps → their free open-source twins on GitHub, one ROUND each (r1–r9), then the CTA "Komen OPEN" (s12).
The client wants top-designer motion, a DIFFERENT creative transition in every round ("jangan boring"), nothing AI-looking, and it must
not look like a copy of the reference reel.

## Read first (fully)
- `compositions/r1.html` = THE ROUND TEMPLATE ("ROUND KIT"): use-case pill, PAID card, FREE repo card (real GitHub data from
  `window.APPS`), chips, feature chips, GRATIS stamp, and the shared EXIT into the tracker. Copy its kit (CSS + markup + builders), rename
  the `r1-` prefix, keep the layout and the exit exactly; replace ONLY its signature transition (the coin flip) with yours.
- `compositions/s01.html`, `s02.html` (hook), `compositions/tracker.html` (host: the 9-tile tracker row at y 300–410 that strikes
  each paid tile and flips it to the free logo on the free name), `vendor/apps.js` (all data: names, logos, repo, stars, licence,
  features, `start`, `dur`, `tFree` = global time the free name is spoken), robot.html / mascot.html (characters).
- Look at them rendered: `npx --yes hyperframes@0.8.186 snapshot . -o <scratch> --at 2.0,4.6,5.6,7.3,8.75,9.4,11.0,11.75 --no-end --describe false --timeout 15000`

## Host layers (never edit index.html, the tracker, the characters, or other agents' files)
Paint order: light background (+ animated grid top-right) · scenes · TRACKER · robot · mascot · dark logo (top-left y 262–283) · captions.
- Tracker row: y 300–410 (tiles x 134 + 92·i, 76 px). In rounds your hero zone is **y 430–935**. s12: the tracker lifts away at its start,
  hero zone **y 290–935**.
- Captions: navy-gradient text centred at **y ≈ 966–1090**. Mascot half body below (head top ≈ 1145, x ≈ 140–650), robot at the right
  (x ≈ 700–960, y ≈ 1340–1680). Keep y > 940 free.

## STYLE LOCK (client rules)
- Background: the host's (light). No opaque full-screen fills (≤ 0.3 s flash allowed in a transition).
- Text: **Poppins 700/400 only**, colour = navy GRADIENT `linear-gradient(172deg, #0a0d2c 8%, #294b77 92%)` (class `-grad` in the kit)
  for headings; solid #0a0d2c / #294b77 small text. Materials exactly as in r1: white cards `linear-gradient(180deg,#ffffff,#f6f8fd)`,
  radius 30–36, soft navy shadows, navy gradient pills for features.
- Semantic colours: PAID = coral `#e5484d` (BERBAYAR tag, strikes); FREE/OPEN SOURCE = GitHub green `#2da44e → #116329` / `#1a7f37`;
  stars gold `#d4a72c`. No neon, no purple voids.
- Logos: ONLY from `window.APPS` (paid + free logos, already wired in the kit's `logo()` builder) and `assets/icons/si-*.svg`
  (Simple Icons, CC0: e.g. si-github, si-googlecalendar, si-facebook, si-instagram). UI icons: `assets/icons/lucide-*.svg` (CSS mask).
  Never redraw/recolour a brand logo. Never show people's photos.
- Truth: repo name/path/stars/licence/features come ONLY from `window.APPS` (verified via the GitHub API). Features = what the VO says.
  No invented numbers, screenshots or product UIs (stylised generic illustrations are fine).

## YOUR ROUNDS — signature transitions (one each, make them great)
Each round: question → paid card appears → paid name ("Lupakan X" / "tanpa X" / "ala X" / "kayak X") = strike/shake → SIGNATURE
TRANSITION → free card lands on/after the free name (`tFree`) → stats chips → feature chips on the spoken feature words → GRATIS
stamp → shared EXIT into the tracker tile (last 0.36 s, identical to r1 with `K` = round index).
- r2 ElevenLabs → VoiceStudio: **SOUND-WAVE MORPH** — the paid card collapses into an audio waveform line that ripples across and
  re-forms into the free card. Feature words: "suara" (Kloning suara), "laptop" (100% lokal: a laptop icon chip).
- r3 Semrush → OpenSEO: **MAGNIFIER SCAN** — a big lens sweeps over the paid card; under the lens it already shows the free card, and the
  sweep reveals it fully. Features on "Keyword", "backlink", "audit".
- r4 Notion → AppFlowy: **PAGE PEEL** — the paid card is a page that curls/peels away (fold shadow), revealing the free card beneath.
  Features on "AI-nya" (Ada AI-nya), "punya kamu" (Data milik kamu).
- r5 Wispr Flow → OpenWhispr: **MIC RIPPLE** — a mic pulses, its ripples wash the paid card away and the free card condenses from the
  rings; "offline" = a wifi-off chip.
- r6 Asana → OpenProject: **KANBAN DRAG** — a cursor drags the paid card as a task card into a "GRATIS" column; on drop it turns into
  the free card. Features on "proyek tim", "server sendiri" (server icon).
- r7 Calendly → Cal.diy: **TEAR-OFF CALENDAR** — the paid card is the top sheet of a desk calendar that tears off; the free card is the
  next sheet; then two sync arrows to "Google Calendar" (si-googlecalendar) and "Outlook" (text chip with a lucide calendar icon).
- r8 Intercom → Chatwoot: **CHANNEL FUNNEL** — chat bubbles from many channels (lucide mail / message-circle / globe, si-instagram,
  si-facebook) fly from the edges into ONE inbox; the inbox is the free card. Features on "semua channel", "satu inbox".
- r9 Loom → Cap: **SCREEN-RECORD CUT** — a REC frame (corner brackets + red dot + timer) captures the paid card, a "cut" clapper-style
  wipe swaps it for the free card; "sekali klik" = a link chip that copies (✓ Tersalin) / share.
- s12 CTA (51.1667, 4.9 s): "Kalian mau 9 link-nya? Komen OPEN, aku kirim lewat DM." — the tracker lifts away at s12's start; the nine
  FREE logos rain down into a "9 link repo gratis" list card (numbered, repo paths, link icons); then a comment row where "OPEN" types
  itself big in the navy gradient + heart; paper plane (lucide-send) flies the list into a DM card; last 1.6 s: centred DARK AI PRENEUR
  lockup (`assets/brand/logo_dark_trim.png`, ~420 px) with a glint (the corner logo fades out at 54.467 s).

## Code conventions (as r1 — deviations break the render)
- `<template>` + `<style>` + ONE root `<div data-composition-id="ID" ...>` + `<script>` IIFE. The runtime STRIPS the template root's id →
  look elements up with `document.getElementById` on unique PREFIXED ids (`r2-…`); prefix classes and SVG ids too.
- `gsap.timeline({ paused: true })`, `_sc` patch, `ft`, `I(el, vars)`, `tl.set({}, {}, D - 0.01)`, seek-order patch,
  `window.__timelines["ID"] = tl`. Timeline length must be ≤ DUR (check it).
- Deterministic: no Math.random (seeded PRNG), no Date, no CSS animations/transitions, no rAF, **no onUpdate** (use per-value tl.set
  windows for counters/typing). Pitfalls: one `attr`/`clip-path` tween per property (chains start stale); no `svgOrigin` inside CSS-
  transformed SVG (rotate nested groups); an `attr` tween ignores a different `I()` start.
- Performance: no full-screen blur/turbulence per frame; ≤ ~400 animated elements; transforms + opacity.

## Mandatory checks
1. `node tools/check_scene.cjs <ids…>` → `ok <duration>` (preview server on :3013; if down: `npx --yes hyperframes@0.8.186 preview . --port 3013 --no-open`).
2. `npx --yes hyperframes@0.8.186 lint .` → no errors in your files.
3. Snapshots (4 shared CPUs: ≤ 10 `--at` per run, `--describe false --timeout 15000`, own scratch dir): frame 0, every beat, the transition
   (several frames), the tracker flip moment (tFree−0.1…+0.5), the exit, the last frame. LOOK at them (Read). Legible at phone size
   (≥ 20 px body), inside the hero zone, nothing under captions/mascot/robot, no blank frames, no overlaps.
4. Report briefly: what you built, risks. Do not commit.

## VERIFIED TIMING (local s = global − start; DUR = timeline length)
- **s01** start 0.0 · DUR 3.1 — "9 aplikasi ini kamu bayar tiap bulan." — 9 0.37 · aplikasi 0.74 · ini 1.25 · kamu 1.48 · bayar 1.79 · tiap 2.38 · bulan. 2.53
- **s02** start 3.1 · DUR 2.6333 — "Padahal kembaran gratisnya ada di GitHub." — Padahal 0.22 · kembaran 0.82 · gratisnya 1.11 · ada 1.59 · di 1.90 · GitHub. 2.11
- **r1** start 5.7333 · DUR 6.1667 — "Gambar dan video AI? Lupakan Higgsfield. Open Generative AI punya 600 lebih model." — Gambar 0.32 · dan 0.84 · video 0.91 · AI? 1.10 · Lupakan 1.85 · Higgsfield. 2.28 · Open 3.36 · Generative 3.75 · AI 4.19 · punya 4.40 · 600 4.77 · lebih 5.16 · model. 5.60
- **r2** start 11.9 · DUR 5.1333 — "Kloning suara tanpa ElevenLabs? VoiceStudio. Semuanya jalan di laptop kamu sendiri." — Kloning 0.29 · suara 0.67 · tanpa 0.97 · ElevenLabs? 1.25 · VoiceStudio. 2.22 · Semuanya 3.20 · jalan 3.70 · di 4.12 · laptop 4.22 · kamu 4.39 · sendiri. 4.58
- **r3** start 17.0333 · DUR 5.8334 — "Riset SEO bukan cuma Semrush. OpenSEO. Keyword, backlink, sampai audit website." — Riset 0.33 · SEO 0.70 · bukan 0.90 · cuma 1.31 · Semrush. 1.62 · OpenSEO. 2.53 · Keyword, 3.50 · backlink, 4.06 · sampai 4.55 · audit 4.83 · website. 5.23
- **r4** start 22.8667 · DUR 5.0666 — "Workspace ala Notion? AppFlowy. Ada AI-nya, datanya tetap punya kamu." — Workspace 0.33 · ala 0.78 · Notion? 1.09 · AppFlowy. 1.79 · Ada 2.78 · AI-nya, 3.05 · datanya 3.53 · tetap 4.07 · punya 4.39 · kamu. 4.53
- **r5** start 27.9333 · DUR 4.3 — "Ngetik pakai suara kayak Wispr Flow? OpenWhispr bisa jalan offline." — Ngetik 0.31 · pakai 0.73 · suara 0.83 · kayak 1.25 · Wispr Flow? 1.39 · OpenWhispr 2.42 · bisa 2.88 · jalan 3.33 · offline. 3.77
- **r6** start 32.2333 · DUR 4.3334 — "Kelola proyek tim tanpa Asana. OpenProject pasang di server sendiri." — Kelola 0.32 · proyek 0.72 · tim 1.03 · tanpa 1.17 · Asana. 1.59 · OpenProject 2.32 · pasang 3.17 · di 3.61 · server 3.67 · sendiri. 3.79
- **r7** start 36.5667 · DUR 5.9666 — "Jadwal meeting tanpa Calendly. Cal.diy langsung sinkron ke Google Calendar dan Outlook." — Jadwal 0.31 · meeting 0.76 · tanpa 0.98 · Calendly. 1.36 · Cal.diy 2.20 · langsung 3.65 · sinkron 4.21 · ke 4.57 · Google 4.67 · Calendar 4.81 · dan 5.12 · Outlook. 5.39
- **r8** start 42.5333 · DUR 4.5 — "Live chat pelanggan ala Intercom. Chatwoot, semua channel masuk satu inbox." — Live 0.22 · chat 0.54 · pelanggan 0.69 · ala 1.09 · Intercom. 1.27 · Chatwoot, 2.09 · semua 2.69 · channel 2.96 · masuk 3.31 · satu 3.69 · inbox. 3.93
- **r9** start 47.0333 · DUR 4.1334 — "Rekam layar kayak Loom. Cap, sekali klik langsung bisa dibagikan." — Rekam 0.34 · layar 0.76 · kayak 1.04 · Loom. 1.12 · Cap, 1.83 · sekali 2.24 · klik 2.49 · langsung 2.90 · bisa 3.32 · dibagikan. 3.43
- **s12** start 51.1667 · DUR 4.9 — "Kalian mau 9 link-nya? Komen OPEN, aku kirim lewat DM." — Kalian 0.20 · mau 0.59 · 9 0.73 · link-nya? 1.06 · Komen 1.78 · OPEN, 2.01 · aku 2.54 · kirim 2.77 · lewat 3.08 · DM. 3.24
