# AI PRENEUR · remake batch 9 (R36–R37) — build brief (2026-11-27)

Client: "remake lagi plus thumbnail … format background-nya jangan lupa … ini gak usah pakai dunia voxel 3D, kayaknya bagus
yang model kayak video ke-2". → **NO voxel world.** Format = the **ref2 look** (technique only, never its brand/mascot):
a clean 2D motion-graphic reel on the brand plate, one idea per beat, a big spoken headline at the top with ONE emphasised word
(italic + accent colour), ONE crisp illustrative UI card / diagram in the middle that animates (html-demo technique: scripted
View(t) windows, cursor, chips, charts, flows, glassy cards with soft shadows), a small host in the bottom-left corner that
reacts every beat (use the client's 3D chibi MASCOT here — whole, never cropped — in place of the reference's pixel creature),
a beat counter bottom-right ("07 / 25"), subtle particles/grain, and a pill CTA button at the end. Every beat changes on a
word of the VO; motion = closed-form springs, short shared-element moves between cards (product-launch-film technique),
3-subframe motion blur on fast moves. Per-word captions are not needed when the headline IS the spoken line — the headline
must match the VO word-for-word in Indonesian.

## Base kits (2D, HTML/GSAP, mascot host) — copy, never copy out/
- WHITE → `projects/aip_r29_dadubisnis/`   - NAVY → `projects/aip_r30_timmarketingai/` (do NOT use its vo_pad.py; no padding)
Background = ONLY the brand plates: NAVY `projects/aip_r25_prompt3d/assets/brand/bg_1080x1920.png`; WHITE `brand/bg-light.png`
cover-fit (a 1080×1920 copy exists at `projects/aip_r31_volume/assets/brand/bg_light_1080x1920.png`). Brand colours only
(navy: white text, accent #01ccf7, white logo; white: text #0a0d2c→#294b77, accent #294b77, dark logo).
Read first: CLAUDE.md, `skills/aipreneur-reels-studio/SKILL.md` + references (brand, client_rules, qa, technique_bank),
`skills/aip-remake/SKILL.md`, `skills/html-demo/SKILL.md`, `skills/product-launch-film/SKILL.md`, and
`projects/aip_remake_batch8/BRIEF.md` (VO hard rules, QA, render command, SFX levels — all still apply).

## Reels
| reel | folder | theme | ref | ref length | target | CTA keyword |
|---|---|---|---|---|---|---|
| R36 | `aip_r36_petaagent` | **WHITE** | ref1 (map of every AI agent it takes to run a company) | 51.2 s | 48–56 s | PETA |
| R37 | `aip_r37_appngebut` | **NAVY** | ref2 (app-performance tips for vibe-coded apps) | 86.0 s | 80–88 s | APP |
References: `projects/aip_remake_batch9/refs/refN.mp4` (gitignored), transcripts `refN.txt`, contact sheets `refN_sheet.jpg`.

### R36 — "peta AI agent untuk jalanin bisnis"
ATM, Indonesian, "kamu". Our own map for an Indonesian business owner: inputs he already uses (WhatsApp, Instagram,
marketplace, Google Sheets/Calendar, email) → Claude in the middle reads them → departments (penjualan, closing, marketing,
CS, operasional, admin & keuangan, riset) → each agent has ONE job + a written workflow → nothing goes to a customer before
the owner approves → one summary page every morning. **Do not claim "137"**: build the actual map in `production/DM_PETA.md`
(departments → named agents → one-line job each) and say the real count in the VO. No invented results. Brand logos only from
Simple Icons (CC0), rendered per the CLAUDE.md logo rule (3D extrude → can be pre-rendered to PNG sprites); record in
asset_credits.json. Cover: white theme, mascot + ONE 3D topic logo above the head (Claude from Simple Icons).

### R37 — "app hasil vibe coding biar ngebut"
For business owners/creators who build apps with Claude/AI: a fast list of real, standard performance fixes (images in
WebP/AVIF, skeleton loading, debounce, pagination, CDN, background jobs, N+1 queries, compression, caching, indexes,
streaming AI responses, lazy-load, parallel requests, code splitting, virtualised lists, connection pooling, etc.). Own order,
own hook ("Claude, bikin app-ku …" framing is fine — ≤3 consecutive words of the reference), ~22–28 tips to fill 80–88 s,
each tip phrased so a non-programmer understands why it matters (one short clause). Technically correct only — no invented
numbers. DM_APP.md = the toolkit: every tip + a ready-to-paste prompt for Claude/Claude Code. Cover: navy, mascot + ONE 3D
topic logo (Claude, Simple Icons).

## VO / QA / render / deliver — exactly as batch 8
ElevenLabs `tools/el_tts_ts.py` (Dakocan, eleven_v4), ONE untouched take (reword + regenerate the whole take when whisper
small AND medium mishear), whisper-medium word diff on the FINAL mp4, −14 LUFS two-pass, rich audible SFX (whoosh per beat,
pops/ticks on cards and counter, riser + impact on the CTA; ≈8–10 dB under VO peaks, none on word onsets, no sidechain on SFX).
`npx --yes hyperframes@0.8.186 check .` 0 errors; snapshot every second and look at every frame (no cut text, mascot whole,
headline never overlapping the card). Render with the shared-lock script exactly as batch-8 shows (one render at a time; it
skips under 2200 MB free — disk is ~2.9 GB; keep your footprint small, hard-link big assets, delete your own out/video.mp4
after the final remix). Deliver: final MP4 `out/AIP_R3x_<TOPIC>.mp4`, covers 1080×1920 + HD, DM, CAPTION.md (complementary
angle, CTA, #aipreneur #skoolcommunity #aimarketing), VO_SCRIPT.md (techniques used), asset_credits.json. Do NOT commit/push.
