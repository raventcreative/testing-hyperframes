# AI PRENEUR · remake batch 8 (R31–R34) — build brief (2026-11-21)

Client request: "terapin juga skill yang kemarin … ingat ya VO-nya jangan bug kayak kemarin".

## Format (new for this batch)
**Voxel 3D world + the client's 3D mascot host + the AIpreneur robot co-host**, upgraded with the skills learned on
2026-11-20. The client is bored of the same panels every reel ("elemennya gitu-gitu aja") → objects live in a 3D voxel
world, not in flat browser-window panels.
- Base kit: WHITE → copy `projects/aip_voxel_uji/` (white voxel, mascot); NAVY → copy `projects/aip_r26_hookmatrix/`
  (navy voxel, mascot, 57.8 s, full pipeline: words.py, vo_data.py, sfx, build, remix). Never copy `out/`.
- Robot co-host: port the AIpreneur robot (GLB + runtime) from `projects/aip_r25_prompt3d/` (navy) or
  `projects/aip_r24_4plugin/` (white) into the voxel kit as a second host layer (robot whole, never cropped, beside the
  mascot; it reacts/points/shows things on its screen). Mascot glances stay disabled.
- Read first, in full: `skills/aipreneur-reels-studio/SKILL.md` + references (brand.md, voxel_reel.md, client_rules.md,
  qa.md, technique_bank.md, mascot_robot_recipes.md), `skills/voxel-reels/SKILL.md`, `projects/aip_remake_batch7/BRIEF.md`
  (rules that still apply).
- **Apply the new skills (techniques only, never their products/briefs):** pick 3–5 per reel and name them in
  `production/VO_SCRIPT.md`:
  - `skills/prompt-motion-techniques` (catalogue; REEL-tagged techniques)
  - `skills/throughline-explainer` — ONE through-line object that transforms scene to scene and ends as the CTA/logo
  - `skills/beat-promo-film` — beat grid, every change on a beat, 3-subframe motion blur on fast moves
  - `skills/product-launch-film` — shared-element transformations (button → object → page), closed-form springs
  - `skills/html-demo` — when a UI must be shown (chat, terminal, app), draw it as a crisp scripted window View(t) on a
    3D screen/billboard in the voxel world, with a scripted cursor — not a static panel
  - `skills/business-explainer-30s` — problem → what → 3 steps → proof → name structure where it fits

## Themes / order (R30 was NAVY → R31 WHITE, alternating)
| reel | folder | theme | ref | ref length | target | CTA keyword |
|---|---|---|---|---|---|---|
| R31 | `aip_r31_volume` | **WHITE** | ref1 (Hormozi: so much volume it's unreasonable to fail) | 52.7 s | 48–58 s | VOLUME |
| R32 | `aip_r32_videoproduk` | **NAVY** | ref2 (AI turns pasted product photos into a promo video with a marketer voice) | 52.1 s | 47–57 s | PROMO |
| R33 | `aip_r33_whatsappclaude` | **WHITE** | ref3 (WhatsApp MCP: connect WhatsApp to Claude, 12 tools) | 100.2 s | 90–110 s | WA |
| R34 | `aip_r34_motionstudio` | **NAVY** | ref4 (free GitHub repos that turn Claude into a motion studio, 4 picks) | 38.4 s | 35–42 s | STUDIO |
**Do not shorten below the target** (client rule from batch 7: keep the reference's length).
References: `projects/aip_remake_batch8/refs/refN.mp4` (gitignored), transcripts `refN.txt`, contact sheets `refN_sheet.jpg`.

## Per-reel notes (ATM — own hook/order/metaphors, ≤3 consecutive words of the reference, Indonesian, "kamu")
- **R31**: framework "dipopulerkan Alex Hormozi" (attribute, no quote marks around a translation). Own examples for
  Indonesian business owners/creators: konten, follow-up/closing, iklan/kreatif, olahraga. Visual metaphor of our own
  (NOT a stick figure throwing balls into a basket — e.g. the mascot firing voxel blocks/arrows at a target island,
  tries vs hits counter, a 30-day grid filling, stairs of days to a goal). AI angle: AI makes the volume cheap
  (batch scripts, variations, drafts) but you still ship. No invented results. DM: 30-day volume tracker + prompt pack
  for producing content volume with AI.
- **R32**: the reference doesn't name its tool and shows a third-party cosmetics brand — never show that brand or any
  real brand packaging. Freddie's angle: "fotoin produk → AI bikin video promo + suara marketer" using a workflow we can
  honestly describe (Claude writes the scenes/script, an AI voice reads it, it renders to video — this is how these reels
  are made; say "contoh alur", no promise of sales). Unbranded illustrative products (bottle/jar/tube, labelled CONTOH).
  Audience: UMKM, online shop, affiliator (keranjang kuning / TikTok Shop / Shopee mention ok, no platform logos unless
  Simple Icons CC0 3D). DM: prompt + checklist foto produk → video promo.
- **R33**: verify on GitHub (lharries/whatsapp-mcp): author, licence, what it does, the exact tool count (12?), setup
  (Go, Python, uv, QR scan, Claude Desktop config, restart), local SQLite storage, the README's prompt-injection warning,
  re-auth after ~20 days. Say only what the README says. Keep the security caveat prominent. Show WhatsApp + Claude logos
  only from Simple Icons (CC0) in 3D. Chat UI must be SIMULASI with invented, neutral names (no real people). DM: setup
  guide step by step + safety checklist.
- **R34**: verify every repo named on GitHub (HyperFrames — star count today, GSAP skills by GreenSock, Blender MCP,
  "Video Shotcraft"); drop or replace any you can't verify with a real, verifiable one. Authentic angle: these reels are
  made with HyperFrames (true). Don't claim "20 repos" unless the DM really lists 20 verified repos — otherwise use the
  real count. DM: the verified repo list with one-line use each.

## VO — HARD RULES (the client explicitly warned: no VO bugs like R30)
1. `python3 tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` (voice Dakocan, eleven_v4, auto tags).
2. **Use the VO as ONE untouched take.** Do not cut, pad, splice or time-stretch it. Timing comes from the alignment;
   scenes follow the voice. If a pause is needed, write it into the script (punctuation / a short line), regenerate.
3. If (and only if) a single line must be replaced, cut ONLY at measured silence (20 ms RMS < −60 dB, search ±0.3 s),
   5–10 ms fades, and re-run the full check below.
4. Listen-check: whisper small + medium; reword words BOTH mishear and regenerate the whole take.
5. Final check on the FINAL MP4: whisper MEDIUM, diff word by word against vo_lines.txt; only spelling/number-format
   differences are allowed. Also check no word onset is chopped (no "odul" for "Modul").
6. Mix: SFX at a fixed lower level, no hard sidechain on SFX (it pumps); music bed ducked under VO; no SFX transient on a
   word onset. Loudness −14 LUFS ±1 (two-pass loudnorm, `projects/aip_r30_timmarketingai/tools/remix_audio.sh` pattern).

## QA + render
- `npx --yes hyperframes@0.8.186 check .` → 0 errors. Snapshot EVERY second, look at every frame (contact sheets),
  zoom small text at 2×. No cut text anywhere (frame edge, texture edge, behind objects, under captions); captions never
  over a face; mascot + robot whole; camera never inside geometry.
- Render ONE AT A TIME (shared lock): `nohup setsid bash -c "sleep 20; /tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/ml/render_aip.sh $PWD AIP_R<n>_<TOPIC>.mp4" < /dev/null > /dev/null 2>&1 & disown`
  — it waits for the lock and SKIPs under 3000 MB free (disk is tight: ~3.5 GB). Don't delete other projects' files;
  after your render, delete your own `out/video.mp4` duplicate only if the remix no longer needs it.
- Cover per `skills/cover-topik/SKILL.md` (minimal, brand theme, mascot + ONE topic logo in 3D above the head — Simple
  Icons CC0; value hooks only if the DM delivers exactly that), 1080×1920 + HD. `production/DM_<KEYWORD>.md`,
  `production/CAPTION.md` (complementary angle, CTA, #aipreneur #skoolcommunity #aimarketing).
- Do NOT git commit/push (the coordinator does). Report: final MP4, covers, DM, caption, skills/techniques used, the VO
  check result (whisper medium diff), loudness, and anything not verified.

## ADDENDUM 2026-11-21 — backgrounds: ONLY the 2 brand plates (client reminder)
"jangan lupa ya background-nya format kita kan 2 aja". The voxel sky must BE the brand plate:
- NAVY reels (R32, R34): `projects/aip_r25_prompt3d/assets/brand/bg_1080x1920.png` (copy into assets/brand/).
- WHITE reels (R31, R33): `brand/bg-light.png` (1080×1350 → cover-fit to 1080×1920, copy into assets/brand/).
How: renderer with alpha (`new WebGLRenderer({alpha:true})`, `setClearColor(0x000000, 0)`, `scene.background = null`,
no sky dome / star sprites / voxel clouds / sky gradients behind the world), and the plate as a full-frame `<img>` (or CSS
background) UNDER the `#vx` canvas. Fog: keep it subtle and tint it to the plate's mid colour (navy ≈ #13284f,
white ≈ #eef3fb) or turn it off so it doesn't paint a non-brand haze. The plate must be clearly visible behind the islands
in every shot — prefer camera angles that show the backdrop (floating islands, not wall-to-wall floor). Floors/islands keep
their brand-tinted colours. Every transition flash stays white (white) / cyan-white (navy).
Then: re-run check + snapshot EVERY second, look at all frames, launch the render with the same command, remix, whisper
-medium diff + loudness, report. Stop any of your own waiting render launchers/waiter loops before changing files.
