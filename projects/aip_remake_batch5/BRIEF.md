# AI PRENEUR · remake batch 5 (R11–R15) — build brief

Same house style, pipeline, QA lessons and house rules as batch 3 and 4 — read `projects/aip_remake_batch3/BRIEF.md` and
`projects/aip_remake_batch4/BRIEF.md` in full first. References: `projects/aip_remake_batch5/refs/refN.mp4` + `refN.txt`
(Indonesian reels by another creator, red/black brand with a red-haired mascot).

## ATM — Amati, Tiru, Modifikasi (the client insists: a real remake, never a copy-paste)
- **Amati**: watch the reference, list its useful idea, its hook mechanism, its beat structure and its CTA mechanism.
- **Tiru**: keep ONLY the useful idea and the general mechanism (e.g. "listicle of N things", "split old vs new").
- **Modifikasi** (mandatory, write it down in `production/VO_SCRIPT.md` under "ATM: what we changed"):
  1. our OWN hook line (different words AND a different angle from theirs),
  2. our OWN structure/order and our own visual metaphor per beat (never their layouts, colours, mascot, cards or icons),
  3. Freddie's practitioner angle where true ("aku pakai ini buat…") — never invented personal results or numbers,
  4. Indonesian-audience value the reference lacks (a concrete local use case, a caution, a step they skipped),
  5. our own CTA keyword (listed below) and our own closing line — no "follow kita untuk update" copy.
  Never reuse more than 3 consecutive words of their script. Verify every fact on official sources; drop what you can't verify
  (the references contain transcription-garbled names and unverified numbers — check them, don't repeat them).

## Order / colours (alternation continues — R10 was LIGHT)
**R11 NAVY · R12 LIGHT · R13 NAVY · R14 LIGHT · R15 NAVY.** Kits: LIGHT → `projects/aip_r8_web3d/` (newest) or `aip_r4_remote/`;
NAVY → `projects/aip_r9_youtube/` (newest) or `aip_r3_desainer/`. The cover follows the reel's colour (navy reel → navy cover).
VO: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py <lines.txt> <out.mp3>` with NO --tags (default = client's AUTO tags:
[playful] [excited] + one context tag per line). Spoken length 35–50 s (voice ≈ 2.5 words/s). Last line "Komen <KEYWORD>, aku kirim
lewat DM." CPU and disk are shared by many builders: snapshot only what you need (one full real-runtime pass + fix passes), JPG
contact sheets only, delete PNG dumps.

## The five reels
- **R11 · Agen ngoding gratis dari DeepSeek** (NAVY · `aip_r11_harness` · port 8931 · ref1, 44 s): the reference says DeepSeek
  released a free, open-source coding agent ("DeepSeek Harness"?) that broke GitHub star records, works like Claude Code (reads files,
  writes code, runs it), fully pluggable (model, tools, UI), can use cheap DeepSeek models or local models via Ollama, one terminal
  command opens it in the browser, developer preview → read the security notes. VERIFY the real name, repo, licence, star counts and
  install command on GitHub; if star numbers can't be verified, don't show numbers. Angle for Indonesian builders/UMKM devs: what it
  costs vs a monthly subscription, and the honest caveat (preview, run it safely). CTA **NGODING**.
- **R12 · 5 repo GitHub gratis jadi jasa cuan** (LIGHT · `aip_r12_cuanrepo` · 8932 · ref2, 59 s → ≤ 50 s): the code is free, you sell
  the SERVICE. Reference picks: an auto-clipper (long video → short clips + subtitles), Remotion (videos from code), OpenHands (AI
  programmer → UMKM websites), Postiz (schedule posts to many accounts → social media admin service), an AI novel-writing tool. Verify
  each repo (name, what it does, licence — e.g. Remotion's company licence rule) and swap any that don't check out for a verified one.
  Indonesian service ideas with no earning promises. Keep the licence caution. CTA **JASA**.
- **R13 · Claude bantu analisa saham (Trader skill)** (NAVY · `aip_r13_trader` · 8933 · ref3, 73 s → ≤ 50 s): a free Claude skill pack
  that works like a trading team (scanner, news, entry timing, stop loss/target, position sizing, risk blocker, broker order, alerts,
  financial-report summary, … and a "time machine" that simulates the rest of the day thousands of times). Verify the repo, the skill
  list and the paper-trading default + approval step. THIS IS FINANCE: no profit claims, no "pasti cuan", no ticker as a tip; the
  reference's own test shows ~coin-flip odds — keep that honesty; on screen "Bukan ajakan beli/jual · edukasi" and stress practice
  account first, every order needs your approval, it's a tool not a guarantee. Use generic example tickers ("SAHAM A"). CTA **SAHAM**.
- **R14 · Claude Code edit Reels: 3 prompt aja** (LIGHT · `aip_r14_3prompt` · 8934 · ref4, 50 s): one folder + five tools (Remotion,
  HyperFrames, FFmpeg, Whisper, yt-dlp), Claude installs them for you; then give 3–5 favourite reels → it writes a style/brand sheet
  ("terinspirasi, bukan nyontek"); then raw footage + one prompt → silence cut, captions, revisions ("hook-nya gedein"). IMPORTANT: our
  R5 (`projects/aip_r5_editvideo/`, "Edit video pakai Claude, 4 langkah") already covered a similar flow — read its VO_SCRIPT.md and make
  R14 clearly DIFFERENT: frame it as "3 prompt" (prompt 1 siapin alat, prompt 2 bikin selera, prompt 3 edit) and SHOW the three actual
  prompts as copyable cards; different visuals from R5 (no repeat of R5's 4-step tracker/storyboard). Freddie really works this way. CTA **PROMPT**.
- **R15 · Duo agent AI gratis: rumah + mesin (Hermes)** (NAVY · `aip_r15_hermes` · 8935 · ref5, 61 s → ≤ 50 s): the reference pairs an
  open-source agent "home" app (garbled in the transcript — "MausBot"/"Woodbot"? identify it from the video frames and verify) with
  Hermes Agent (Nous Research) as the engine: a team of agents that get better at repeated tasks, login with an existing ChatGPT plan
  instead of an API key or use a cheap DeepSeek model, skills and data stay on your computer, every command asks permission; minus: the
  computer must stay on and security is your responsibility. Verify every claim (names, login method, pricing comparisons — drop the
  "10× cheaper"/benchmark claims unless verified). Angle: data ownership + honest trade-offs. CTA **AGENT**.
