# SCENE BUILD BRIEF — "4 plugin sebelum vibe coding" · AI PRENEUR reel remake · NAVY

Project root: `projects/plugin4_2026/` · 1080×1920 · 30 fps · 46.1 s · HyperFrames 0.8.186.
VO (client's voice): "Sebelum vibe coding pakai Claude Code, pasang empat plugin ini dulu. Satu, Superpowers. Lebih dari 300 ribu bintang
di GitHub. Claude nggak langsung ngoding. Dia nanya dulu, bikin rencana, tulis tes duluan, baru jalan. Dua, Karpathy Skills. Cuma satu
file CLAUDE.md isinya empat aturan. Mikir dulu, bikin sesimpel mungkin, ubah seperlunya, dan buktikan jalan. Tiga, Caveman. Jawaban
Claude dipadatkan tanpa basa-basi. Di contohnya, 63 token jadi 20. Isinya tetap sama. Empat, plugin Codex, resmi dari OpenAI. Kerjaan
Claude direview sama Codex, jadi bukan Claude yang nilai dirinya sendiri. Mau link dan cara pasangnya? Komen SETUP, aku kirim lewat DM."
A REMAKE of a reference reel (`production/reference_sheet.png`: black/white wireframe isometric boxes, GitHub screenshot cards, an orange
pixel mascot). DO NOT copy it. Our story: **a developer's power-up rig** — the AI PRENEUR robot is the developer at the keyboard, the
host (3D mascot) presents, and a **PLUGIN DOCK** under the logo fills slot by slot with glowing "cartridges" as each plugin is installed.
Each round SHOWS what the plugin changes in Claude Code's behaviour (before → after), in clean premium generic UI. Client rules: premium
motion, a different creative transition every scene, nothing AI-looking, real or open-source assets only, never boring.

## Facts (verified 10 Nov 2026 from the official READMEs — show only these)
- Superpowers = `obra/superpowers` (MIT). We say "lebih dari 300 ribu bintang" → show **"300K+ ★"** (never an exact live count).
  It makes the agent brainstorm/ask first, write a plan, use test-driven development (tests first), then execute.
- Karpathy Skills = `multica-ai/andrej-karpathy-skills`: ONE file `CLAUDE.md` with 4 rules: Think Before Coding, Simplicity First,
  Surgical Changes, Goal-Driven Execution (VO: "Mikir dulu, bikin sesimpel mungkin, ubah seperlunya, buktikan jalan").
- Caveman = `JuliusBrussee/caveman` (Apache-2.0): terse "caveman" answers; README example **63 tokens → 20 tokens**, same fix.
- Codex = `openai/codex-plugin-cc` (Apache-2.0), official from OpenAI: command **`/codex:review`** — Codex reviews Claude's work.
- Repo names may appear as small mono-ish TEXT (Poppins 400) — no GitHub/OpenAI logos (we have none). The Claude mark
  `assets/icons/lobe-claude-color.svg` may be used.

## Host layers (read; do not edit): index.html, compositions/dock.html, robot.html, mascot.html
Paint order: navy background · **scenes (yours)** · **dock** · robot · mascot · white logo (top-left y 262–300) · captions.
- Captions: words on navy chips, white + cyan #01CCF7, centred at **y ≈ 960–1030** (one line).
- Mascot (host) half body bottom-left, head top ≈ y 1150, x 140–650: presents on each plugin name. Robot (developer) bottom-right
  ≈ x 700–960, y 1340–1680: types on a cyan holo keyboard in the hook (0.3–2.0 s), presents each plugin name, "no" on "nggak", thinks on
  "nanya"/"Mikir", scans on "tes"/"63"/"direview", shock on "300" and "20.", looks at the mascot on "bukan".
- **THE DOCK** (`compositions/dock.html`, persistent): 4 slots, slot k (0–3) rect **x 66+240k, y 318, 228×78, radius 22**. Empty =
  dashed navy glass "0k plugin". They pop in on "empat" (2.69 s). Slot k FILLS at **F[k]** (cartridge gradient + icon + name + green ✓):
  F = [5.37, 16.24, 26.05, 35.24] (= name word + 0.6; also `window.DOCK.F`). Cartridge colours: 1 Superpowers cyan #01ccf7→#0a6fd0
  (zap), 2 Karpathy Skills violet #9d8cff→#5a3fe0 (file-text), 3 Caveman amber #ffb35c→#e2712a (shrink), 4 Codex green #3ddc97→#0f9a62
  (scan-eye). The running round's slot wears a glowing ring. CTA: ripple on "SETUP," (43.31).
- → **Your hero zone is y 410–935, x 60–1020** (the dock owns y 300–400). Nothing in y > 945.
- **HAND-OVER CONTRACT (every round)**: on the plugin's NAME word a big plugin CARTRIDGE CARD (same gradient/icon/name as its dock
  slot, + the repo name small, e.g. "obra/superpowers") arrives in the hero zone; then it shrinks and flies into its dock slot so that it
  matches the slot rect exactly at F[k] − 0.02 and you hide it at F[k] (the dock takes over with a flash). Then the round's demo plays.

## YOUR SCENES (ideas; make them better; every beat lands on its spoken word — see the timing table)
- **s01 HOOK** (0–3.83) "Sebelum vibe coding pakai Claude Code, pasang empat plugin ini dulu." — frame 0 already striking: a generic
  dark terminal/editor window "Claude Code" (Claude mark + title, a prompt `>` with a blinking caret block) where the robot is about to
  type "bikinin aplikasi…"; a big glowing "▶ VIBE CODING" button; on "Sebelum" the button gets a hard STOP (a red-coral "TAHAN DULU"
  stamp / lock); on "pasang empat plugin" four empty cartridge outlines fly from the terminal up toward the 4 dock slots (the dock pops
  in at 2.69 s) — the hand-over to the dock.
- **r1 Superpowers** (3.83–14.27) — cartridge card + "300K+ ★" counter rolling up on "300 ribu" (per-value tl.set windows), "GitHub" as
  text. Demo: "nggak langsung ngoding" = a "langsung ngoding" path gets blocked/struck; then a 4-node pipeline lights on each word:
  "nanya dulu" (chat bubble "Mau bikin apa?"), "bikin rencana" (plan checklist), "tulis tes duluan" (test file with red ✗ tests),
  "baru jalan" (▶ run → tests turn green ✓).
- **r2 Karpathy Skills** (14.27–24.53) — cartridge card; on "satu file CLAUDE.md" one document "CLAUDE.md" opens; "empat aturan" = 4
  empty rule rows; each rule writes itself on its words with a micro-visual: "Mikir dulu" (thinking dots/brain), "sesimpel mungkin"
  (a bloated code block collapses into 3 clean lines), "ubah seperlunya" (a diff where only 1 line changes, green/red), "buktikan
  jalan" (a test ✓ goal flag).
- **r3 Caveman** (24.53–33.37) — cartridge card; two answer bubbles: a long verbose reply (lots of filler) with a token meter "63
  token"; on "dipadatkan tanpa basa-basi" the filler words get crushed/fly out and the reply compresses to a short terse one; the meter
  counts 63 → 20 (on "63"/"20."); "Isinya tetap sama" = both carry the same "solusi: …" chip with an "=" badge.
- **r4 Codex** (33.37–41.03) — cartridge card + a small "resmi · OpenAI" text pill; `/codex:review` types in the terminal; Claude's code
  panel slides left, a "Codex review" panel slides in with 2–3 review comments landing on lines; on "bukan Claude yang nilai dirinya
  sendiri" a mirror/self-grade badge "Claude ✓ Claude" gets crossed out and replaced by "Reviewer: Codex".
- **s06 CTA** (41.03–46.10) "Mau link dan cara pasangnya? Komen SETUP, aku kirim lewat DM." — a comment row slides up (avatar circle with
  lucide user-round, input field); "SETUP" types itself big in cyan on "SETUP," (per-letter tl.set) while the dock ripples; a heart pops;
  on "kirim … DM." a paper plane carries a "Link + cara pasang" card (listing the 4 plugin names with their colour dots) into a DM card
  ("terkirim ✓"); last ~1 s calm end beat (the corner logo stays; keep the end clean).

## STYLE LOCK
- Text **Poppins 700/400 only**: white `#ffffff`, cool `#e3edfa`, cyan `#01ccf7` / `#6adfff`; navy glass panels `rgba(12,22,64,.82)` with
  `inset 0 0 0 1.5px rgba(255,255,255,.10)` borders, radius 24–34; terminal/editor panels darker `#070b24` with a title row. Code lines
  may be drawn as Poppins 400 text or rounded bars (no other font). Accents: green #2da44e/#3ddc97 (ok/tests pass), coral #e5484d (fail,
  stop; sparingly), the 4 cartridge colours above.
- Icons: `assets/icons/lucide-*.svg` (ISC): zap, file-text, shrink, scan-eye, check, terminal, star, list-checks, flask-conical, play,
  brain, sparkles, code-xml, search-check, git-pull-request, message-circle, send, heart, user-round, shield-check, minimize-2, scissors.
  Inline the SVG path markup (stroke currentColor). More: `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/npm_lucide/package/icons/`.
- No brand logos except the Claude mark, no people photos, nothing AI-generated, no invented numbers presented as facts (UI example
  values are fine).

## Code conventions (deviations break the render)
- `<template>` + `<style>` + ONE root `<div id="root" data-composition-id="ID" data-width="1080" data-height="1920">` + `<script>` IIFE;
  the runtime strips the root id → `document.getElementById` on unique PREFIXED ids (`r2-…`); prefix classes and SVG ids.
- Timeline boilerplate exactly as `compositions/s01.html` of the sister project `../lamarankerja_2026/compositions/s01.html` (`_sc`
  patch, `ft`, `I`, `tl.set({}, {}, D - 0.01)`, seek-order patch, `window.__timelines["ID"] = tl`). D = the scene dur below; timeline
  length ≤ D. Use `wt(word, after)` on `window.VO_WORDS` for beats.
- Deterministic: no Math.random (seeded PRNG), no Date, no CSS animations/transitions, no rAF, **no onUpdate** (per-value tl.set windows
  for counters/typing). Give every fromTo COMPLETE from-values. One attr/clip-path tween per property; no svgOrigin in CSS-transformed SVG.
- Performance: transforms + opacity; no full-screen blur per frame; ≤ ~250 animated elements per scene.

## Checks (mandatory)
1. `node tools/check_scene.cjs <ids>` → `ok <dur>` (shared preview server on :3018 is running).
2. `npx --yes hyperframes@0.8.186 lint .` → 0 errors in your files.
3. Snapshots (`npx --yes hyperframes@0.8.186 snapshot . -o <your scratch dir> --at <≤8 times> --no-end --describe false --timeout 90000`)
   of the first frame, every beat, the dock hand-over (F[k] ± 0.1) and the last frame. LOOK at them: legible on a phone (≥ 20 px), inside
   the hero zone, nothing over the dock/captions/mascot/robot, transitions between scenes seamless (check the frame before and after each cut).
4. Report briefly. Do not commit. Edit only your scene files (+ new assets under `assets/fx/`).

## VERIFIED TIMING (global s)
- **s01** start 0.0 dur 3.8333 (end 3.8333): Sebelum@0.33  vibe@0.72  coding@0.88  pakai@1.08  Claude Code,@1.37  pasang@2.34  empat@2.74  plugin@2.96  ini@3.14  dulu.@3.33
- **r1** start 3.8333 dur 10.4334 (end 14.2667): Satu,@4.17  Superpowers.@4.77  Lebih@5.90  dari@6.45  300@6.71  ribu@7.08  bintang@7.50  di@7.85  GitHub.@7.96  Claude@8.80  nggak@9.13  langsung@9.27  ngoding.@9.51  Dia@10.23  nanya@10.45  dulu,@10.63  bikin@11.19  rencana,@11.49  tulis@12.36  tes@12.74  duluan,@12.89  baru@13.34  jalan.@13.61
- **r2** start 14.2667 dur 10.2666 (end 24.5333): Dua,@14.57  Karpathy@15.18  Skills.@15.64  Cuma@16.59  satu@17.02  file@17.20  CLAUDE.md@17.45  isinya@18.01  empat@18.55  aturan.@19.04  Mikir@19.88  dulu,@20.18  bikin@20.81  sesimpel@21.23  mungkin,@21.49  ubah@22.29  seperlunya,@22.66  dan@23.10  buktikan@23.36  jalan.@23.86
- **r3** start 24.5333 dur 8.8334 (end 33.3667): Tiga,@24.84  Caveman.@25.45  Jawaban@26.32  Claude@26.89  dipadatkan@27.14  tanpa@27.79  basa-basi.@28.27  Di@28.75  contohnya,@29.18  63@30.08  token@30.56  jadi@31.00  20.@31.26  Isinya@32.15  tetap@32.57  sama.@32.91
- **r4** start 33.3667 dur 7.6666 (end 41.0333): Empat,@33.72  plugin@34.33  Codex,@34.64  resmi@35.33  dari@35.78  OpenAI.@35.90  Kerjaan@36.80  Claude@37.40  direview@37.59  sama@38.12  Codex,@38.29  jadi@38.98  bukan@39.29  Claude@39.45  yang@39.79  nilai@39.95  dirinya@40.17  sendiri.@40.46
- **s06** start 41.0333 dur 5.0667 (end 46.1): Mau@41.42  link@41.74  dan@41.95  cara@42.04  pasangnya?@42.19  Komen@43.06  SETUP,@43.31  aku@43.84  kirim@44.03  lewat@44.33  DM.@44.50
