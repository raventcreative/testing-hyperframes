# AI PRENEUR · remake batch 4 (R6–R9) — build brief

Client/brand: **AI PRENEUR** (Freddie Kashawan's practical-AI education brand; IG AIpreneur Academy). Format 1080×1920, Indonesian.
These are REMAKES of reference reels (`projects/aip_remake_batch4/refs/refN.mp4`, transcripts `refN.txt`): same useful idea, our own
angle, framing, visuals and script — never a copy of the reference's look (their cream/peach palette, pixel crab mascot, layouts) or wording.

## House style — identical to batch 3 (read `projects/aip_remake_batch3/BRIEF.md` in full; everything there applies)
- Reference implementations, newest first (copy the kit of the right colour, then replace the content):
  - **LIGHT** → `projects/aip_r4_remote/` (batch 3, LIGHT) and the original kit `projects/promptbuilder_2026/`.
  - **NAVY** → `projects/aip_r3_desainer/` (batch 3, NAVY) and the original kit `projects/igagent_2026/`.
  These batch-3 folders already have the current audio setup: `<audio id="vo" src="assets/audio/vo.mp3" data-start="0.3">` + an sfx
  `<audio>` inside the composition (the lead adds a ducked music bed and loudness-normalises after rendering — do not add music).
- NAVY = white #ffffff / #e3edfa text + cyan #01CCF7 / #6adfff accents, navy glass panels, white logo. LIGHT = navy-gradient headings
  (#0a0d2c→#294b77), small text #0a0d2c / #294b77 / #5d6f8f, white cards, animated grid, dark logo. Poppins 700/400 only. Robot + mascot
  hosts exactly like the kits. Hero zone y 290–935; nothing in y > 945 except captions / mascot / robot.
- Order continues the alternation (R5 was NAVY): **R6 LIGHT · R7 NAVY · R8 LIGHT · R9 NAVY**.

## Script, VO, QA, house rules
Exactly as batch 3: `production/VO_SCRIPT.md` (header: what changed vs the reference + verified facts with source and date), Indonesian
"aku/kamu", hook in line 1, practical, no overclaims / no invented numbers, 35–55 s, last line **"Komen <KEYWORD>, aku kirim lewat DM."**;
ElevenLabs via `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py <lines.txt> <out.mp3> --tags "[playful] [excited]"`
(every line tagged), `vo_words_raw.json` from the character alignment, kit `tools/timing.py`; SFX via the kit's `tools/sfx.py`.
Verify every concrete fact (tool/repo names, what they do, free vs paid, install steps) against official sources (GitHub README /
official site) with WebSearch/WebFetch; drop or generalise anything you can't verify. QA with the REAL runtime
(`npx --yes hyperframes@0.8.186 snapshot . --at … --no-end --timeout 60000 -o <dir>` + `validate`); pin initial states at 0; wait for
robot/mascot globals; shallow 3D only; no clipped/overflowing text; captions never covered.
House rules: Write/Edit for files (no heredocs with `$$(`), no `rm -rf`, do NOT git commit/push, do NOT run the full render, only
touch your own folder. Deliverables: `index.html` + `compositions/*`, `production/{VO_SCRIPT.md, vo lines, timing.json, NOTES.md}`,
`assets/audio/vo.mp3` + `assets/audio/sfx.wav`, `thumbnail/cover.html` + `thumbnail/COVER_<NAME>_1080x1920.png`.
Final reply: duration, VO script, scene list, sources checked, real-runtime contact sheet path(s), cover path, known issues.

## The four reels
- **R6 · Tes ide bisnis ke 100 "pembeli AI" sebelum keluar modal** (LIGHT · folder `aip_r6_founder` · port 8826 · ref1, 46 s): the
  reference presents "Founder", a pack of free Claude skills that act as a startup team (a "board", a CFO that finds the real margin,
  and a simulated consumer panel of AI buyers with their own income, habits and doubts). Verify the exact name, repo, number of skills
  and what they do. Indonesian angle: test an idea before spending capital — use an Indonesian example business (e.g. jasa cuci mobil
  panggilan / katering harian), clearly labelled "contoh simulasi"; numbers in the demo are illustrative, consistent with each other
  (check the arithmetic), never presented as real results. Keep the honest point from the reference: the panel is simulated → validate
  the winner with real customers next. CTA keyword **FOUNDER**.
- **R7 · 1 skill Claude bikin reels animasi tanpa kredit video AI** (NAVY · `aip_r7_reelskill` · 8827 · ref2, 50 s): Claude writes the
  whole reel as CODE (HTML/GSAP) instead of a video-generation model, so no video credits; any style (cerita anak, animasi, kolam koi,
  film pendek). Freddie really uses **HyperFrames** (`npx hyperframes`, open source by HeyGen — verify name, repo, licence, install) for
  exactly this — this very reel is made that way: say so (practitioner voice, it's true). Do NOT copy the reference's personal stats
  (60 reels / 1 juta views / 11 ribu followers) — no growth numbers at all. CTA keyword **REELS**.
- **R8 · Jualan website 3D, 1 prompt jadi** (LIGHT · `aip_r8_web3d` · 8828 · ref3, 50 s): a library of 3D-website prompts ("Motion
  Sites" in the reference — verify name, that it's paid, what's inside); copy a prompt → paste into Claude (or another AI) → it builds the
  site → swap in the client's images → sell it as a service. Indonesian angle for UMKM/freelancer clients; no fixed earning promise (the
  reference's "$500" → say the price depends on the client/scope, or give a clearly-labelled example range only if you can justify it).
  Since the library is paid, the CTA offers Freddie's free starter prompt pack. CTA keyword **3D**.
- **R9 · YouTube agent: 11 skill Claude buat channel kamu** (NAVY · `aip_r9_youtube` · 8829 · ref4, 48 s): a free pack of Claude skills
  for YouTube — script from proven hook formulas with a hook score, title + thumbnail as one pairing, transcript → timed edit list,
  comment sorting + replies in your voice, weekly plan, and a "virality engine" that finds outlier videos in your niche and names the
  formula. Setup: open Claude Code, paste the GitHub link, type `/ytscript` (verify the exact repo, skill count, command names). Don't
  repeat the reference's clickbait opener ("Claude just killed YouTube"). No YouTube logo art copied — a neutral play-button glyph is fine.
  CTA keyword **YOUTUBE**.
