# AI PRENEUR · remake batch 7 (R27–R30) — build brief

Format: the client's **mascot + robot** reels (R-series kit, `/aip-remake`) upgraded with the new recipes. Read first, in full:
- `skills/aip-remake/SKILL.md` + `projects/aip_remake_batch3..6/BRIEF.md` (house style, ATM rules, QA lessons, mascot glance fix)
- `skills/aipreneur-reels-studio/references/brand.md`, `client_rules.md`, `qa.md`, `mascot_robot_recipes.md`, `technique_bank.md`
- `skills/aipreneur-reels-studio/references/prompt_motion_catalogue.md` (skim the REEL-tagged techniques)

## Client rules for THIS batch
- **Do NOT shorten the videos.** Keep each reel about as long as its reference (±10 %): R27 ≈39 s, R28 ≈38 s,
  R29 ≈160 s (the dice video — full length), R30 ≈92 s. Long reels need more beats, not slower ones: keep a change on
  every beat, a new visual device every 4–8 s, no hold > 1 s.
- Mascot (host) + AIpreneur robot (co-host) in every reel, both whole, never cropped, glances disabled.
- Apply 4–6 recipes from `mascot_robot_recipes.md` per reel (different sets per reel): guide object (robot screen /
  mascot hand / cyan dot), robot-screen portal, button → page, accent-dot journey, spinning pain list, process fill,
  chaos → control → clarity → brand arc, camera push 1.0→1.04, small-overshoot springs, beat-locked changes, VO ducking.
  Write the chosen recipes + credits in `production/VO_SCRIPT.md`.
- Brand colours only in UI text (see brand.md). Logos: Simple Icons (CC0) → 3D extruded (SVGLoader + ExtrudeGeometry),
  credits in production/asset_credits.json. No reference likeness, UI or brand.
- NO cut text anywhere (frame edge, texture edge, behind objects, under captions). Audit every second before rendering.

## Order / themes (alternation continues — R26 was NAVY)
| reel | folder | theme | ref | ref length | CTA keyword |
|---|---|---|---|---|---|
| R27 | `aip_r27_simulasipasar` | **WHITE** | ref1 (MiroFish: test a startup idea on AI personas) | 39 s | IDE |
| R28 | `aip_r28_sistembisnis` | **NAVY** | ref2 (Hindi: "don't build companies, build systems") | 38 s | SISTEM |
| R29 | `aip_r29_dadubisnis` | **WHITE** | ref3 (dice odds of entrepreneurship, 2:41) | ≈160 s | DADU |
| R30 | `aip_r30_timmarketingai` | **NAVY** | ref4 (AI marketing team, 0 employees, 3 modules) | 92 s | MARKETING |
Kits: WHITE → copy `projects/aip_r24_4plugin/` (or `aip_r20_freellm/`); NAVY → copy `projects/aip_r25_prompt3d/`
(or `aip_r19_jarvis/`). Never copy `out/`. References + transcripts: `refs/refN.mp4`, `refN.txt`, `refN_sheet.jpg`.

## Per-reel notes (ATM — own hook/order/metaphors; ≤3 consecutive words of the reference)
- **R27**: verify MiroFish on GitHub (name, what it really does, licence, star count today — say "puluhan ribu bintang"
  only if verified, else drop the number); Freddie's angle: test a product/offer idea for an Indonesian audience before
  spending on stock/ads (illustrative example, labelled). No promises. DM: setup guide + Claude Code prompt.
- **R28**: own Indonesian script about the 5 systems (sales, marketing, keuangan, rekrutmen, delivery) + "revenue naik,
  biaya turun" (no numbers unless illustrative); AI angle: which parts AI/automation can run. DM: system map checklist.
- **R29**: verify the maths (1 roll 16,7 %; 10 rolls 1−(5/6)^10 ≈ 83,8 %; 100 rolls ≈ 99,99999 %). Keep ALL the
  reference's ideas (wrong approach too big/small, wrong idea, too many unknowns, market too small, no real problem, few
  tries, pick the dice = idea, pick the tray = market, change the throw before the tray, shiny object syndrome,
  refine product/offer/pricing/distribution) but in our own order and metaphors, Indonesian UMKM examples. Ideal format
  for a 3D dice + tray + mascot/robot world; vary devices every few seconds across 160 s. DM: worksheet "pilih dadu & nampan".
- **R30**: verify every tool named (Claude Code, Higgsfield, ElevenLabs, the analytics tool — read the frames; drop
  what you can't verify); keep the 3 modules (riset & konten → kreatif & distribusi → loop analitik) + "approve before
  posting" + one-page morning brief; "AI memindahkan informasi, kamu pegang brand & budget". No earning promises.
  DM: blueprint.

## Pipeline per reel
1. Script (Indonesian, "kamu"), `production/vo_lines.txt`, VO: `python3 tools/el_tts_ts.py production/vo_lines.txt
   assets/audio/vo.mp3` (auto tags, voice Dakocan, eleven_v4). Credits are fine (≈178k chars left). Whisper small +
   medium listen-check; reword words both mishear (bad: "pembukaan", "penyedia", "calon mitra"; avoid "rahasia").
2. Timing → scenes → `npx --yes hyperframes@0.8.186 check .` (0 errors).
3. QA: snapshot EVERY second, look at every frame (contact sheets), fix, re-check.
4. Render ONE AT A TIME (shared lock): `nohup setsid bash -c "sleep 20; /tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/ml/render_aip.sh $PWD AIP_R<n>_<TOPIC>.mp4" < /dev/null > /dev/null 2>&1 & disown`
   — it waits for the lock and SKIPs under 3000 MB free disk (then tell the coordinator; don't delete other projects' files).
5. Verify the final MP4 (duration, whisper the audio once, 12–20 sampled frames).
6. Cover per `skills/cover-topik/SKILL.md` (minimal, brand theme, mascot + ONE topic logo in 3D above the head;
   value hooks only if the DM delivers exactly that), 1080×1920 + HD. `production/DM_<KEYWORD>.md`, `production/CAPTION.md`
   (complementary angle, CTA, #aipreneur #skoolcommunity #aimarketing).
7. Do NOT git commit/push (the coordinator does). Report: final MP4 path, cover paths, DM/caption paths, recipes used,
   anything you could not verify or do.
