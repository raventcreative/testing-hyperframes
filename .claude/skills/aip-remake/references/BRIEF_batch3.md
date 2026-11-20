# AI PRENEUR · remake batch 3 (5 reels) — build brief

Client/brand: **AI PRENEUR** (Freddie Kashawan's practical-AI education brand; IG AIpreneur Academy). Format 1080×1920, Indonesian.
These are REMAKES of 5 reference reels (in `projects/aip_remake_batch3/refs/refN.mp4`, transcripts `refN.txt`): same useful idea,
our own angle, framing, visuals and script — never a copy of the reference's look, characters or wording.

## Approved house style (use the previous remakes as the reference implementation — copy the kit, then replace the content)
- **NAVY reels** → kit `projects/igagent_2026/` (read `production/SCENE_BRIEF.md`, `tools/*.py`, `compositions/`, `index.html`):
  navy background, text **white #ffffff / cool #e3edfa**, accents **cyan #01CCF7 / #6adfff**; navy glass panels `rgba(12,22,64,.82)` with
  `inset 0 0 0 1.5px rgba(255,255,255,.10)`, radius 24–34; white cards (navy text) for UI; **white** AI PRENEUR logo top-left; captions =
  word chips on navy, white + cyan, centred y≈960–1030.
- **LIGHT reels** → kit `projects/promptbuilder_2026/` (read its `production/SCENE_BRIEF.md`): white → soft-blue background with the
  ANIMATED grid; headings in the navy gradient `linear-gradient(172deg,#0a0d2c 8%,#294b77 92%)` (background-clip text); small text
  #0a0d2c / #294b77 / #5d6f8f; white cards `linear-gradient(180deg,#fff,#f6f8fd)` radius 24–34 with soft navy shadows; **dark** logo
  top-left; captions in the navy gradient.
- Both: **Poppins 700/400 only**; robot (operator) + mascot (host) exactly like the kits; hero zone y 290–935 (x > 340 when y < 305
  because of the logo); nothing in y > 945 except captions/mascot/robot; semantic accent colours only where the kit uses them.
- Order alternates navy / light: R1 NAVY · R2 LIGHT · R3 NAVY · R4 LIGHT · R5 NAVY.

## Script + VO
- Write `production/VO_SCRIPT.md` like `projects/igagent_2026/production/VO_SCRIPT.md`: a header on what changed vs the reference and
  which facts were verified (source + date), then the lines. Indonesian, "aku/kamu", practical, punchy, strong hook in line 1, no
  overclaims (no "dijamin diterima kerja", no "pasti", no fake numbers). 35–60 s. Last line = CTA **"Komen <KEYWORD>, aku kirim lewat DM."**
- VO: ElevenLabs with the saved voice (`tools/voice_config.json`, key injected by the proxy) — **every line starts with the tags
  `[playful] [excited]`** (client's instruction). Use `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py <lines.txt> <out.mp3>
  --tags "[playful] [excited]"`: one call, writes the mp3 + a JSON with line times and a character alignment. Build the kit's
  `production/vo_words_raw.json` (faster-whisper format: `{"segments":[{"start","end","text","words":[{"w","s","e","p"}]}]}`) from
  that character alignment (split on spaces) instead of running whisper — exact and fast. Fallback: the kit's `tools/fw_transcribe.py`
  with model `small`. Then the kit's `tools/timing.py` → `production/timing.json` (+ `vendor/vo_words.js`).
- Verify every concrete fact (tool names, what they do, free/open source, install steps) against official sources (WebSearch /
  WebFetch: GitHub README, official site). If you can't verify a claim, drop it or say it generically. Record sources in VO_SCRIPT.md.

## QA (lessons from the last batches — the real renderer differs from quick snapshots)
- Final check with the REAL runtime: `npx --yes hyperframes@0.8.186 snapshot . --at t1,t2,… --no-end --timeout 60000 -o <dir>` for
  every scene, transition midpoint, first frame and end; `npx --yes hyperframes@0.8.186 validate .` (only lipsync-style 404s allowed).
- Pin every initial state on the timeline at 0 (`tl.set(el, {...}, 0)`) — elements hidden only by inline CSS show up at frame 0 in
  the real runtime. Don't rely on `gsap.set` outside the timeline for states later tweens change. Avoid build-time `tl.seek` leaks.
- If a build step needs globals from another script (robot/mascot runtimes), wait for them (script order differs in the render).
- The real renderer (software compositing) does NOT depth-sort nested 3D layers reliably: keep 3D rigs shallow, cards as flat planes,
  separate 3D contexts for intersecting objects, and never fade (opacity) a 3D group — fade the flat card inside it.
- No text may overflow its box or be cut by the frame on held frames. Captions must never be covered.

## House rules
- Write files with Write/Edit (heredocs with `$$(` get blocked); no `rm -rf` (use new dir names); do NOT git commit/push; do NOT run
  the full render (the lead renders); do not touch other folders.
- Deliverables in your folder: `index.html` + `compositions/*`, `production/{VO_SCRIPT.md, vo text, timing.json, ...}`,
  `assets/audio/vo.mp3` (or .wav) + `assets/audio/sfx.wav` (kit's `tools/sfx.py`), `thumbnail/cover.html` + `thumbnail/COVER_<NAME>.png`,
  `production/NOTES.md` (scenes, timings, sources, known issues).
- Final reply: duration, VO script, scene list, sources checked, real-runtime contact sheet path(s), cover path, known issues.

## The five reels
- **R1 · Panel rekrutmen 7 Claude** (NAVY · folder `aip_r1_panelcv` · port 8821 · ref1, 36 s): a workflow where 7 Claude reviewers try to
  reject your CV — 1 acts as the ATS gatekeeper, 1 as the hiring manager, 5 read it alone as different people (manager, another applicant,
  CEO…) — then it writes an improved CV with every flagged issue fixed. Frame it for Indonesian job seekers. No "bulletproof/pasti dapat
  kerja" claims. CTA keyword **CV**.
- **R2 · 4 open source buat ngatur banyak AI agent** (LIGHT · `aip_r2_orkestrator` · 8822 · ref2, 93 s → make it ≤ 55 s): the reference
  lists OpenHands, Paperclip, Orca, TeamAI as free alternatives to "Hermes Agent". Verify each project (name, repo, what it actually does,
  licence/free); keep only verified facts, replace any that don't check out with a verified open-source multi-agent orchestrator. Do
  not repeat the reference's clickbait claim ("era Hermes sudah selesai"). CTA keyword **AGENT**.
- **R3 · 5 tool gratis bikin Claude jadi desainer** (NAVY · `aip_r3_desainer` · 8823 · ref3, 39 s): Taste, Impeccable, Playwright CLI,
  Awesome Design (DESIGN.md collections), image → interactive 3D (three.js) — verify exact names/repos/what they do. CTA **DESAIN**.
- **R4 · Tim 3 Claude cari kerja remote** (LIGHT · `aip_r4_remote` · 8824 · ref4, 44 s): Claude 1 crawls many job sites and collects
  remote openings, Claude 2 filters what fits your skills and can be done from Indonesia, Claude 3 writes a tailored CV + cover letter per
  opening, then everything lands on one job-board page you can apply from. No job-site logos (text names only). CTA **REMOTE**.
- **R5 · Edit video pakai Claude, step by step** (NAVY · `aip_r5_editvideo` · 8825 · ref5, 81 s → ≤ 60 s): 1 Claude desktop app + a folder
  "AI Video Editor" with raw-footage / reference / export; 2 free tools: HyperFrames (motion graphics), FFmpeg (cuts), Whisper (captions),
  yt-dlp (download references to study); 3 give Claude 3–5 reels you like → it breaks down the style → style sheet; 4 drop raw footage +
  prompt → storyboard first → revisions ("font lebih besar") → final video. Freddie really uses HyperFrames — practitioner voice. CTA **EDIT**.
