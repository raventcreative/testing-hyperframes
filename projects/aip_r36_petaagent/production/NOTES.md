# NOTES — R36 · Peta AI agent (AI PRENEUR · WHITE) · `projects/aip_r36_petaagent/`

1080×1920 · 30 fps · **55,5 s** · VO 54,2 s from 0,3 s (one untouched ElevenLabs take, take 2) · HyperFrames 0.8.186 · CTA **PETA**.
Reference `aip_remake_batch9/refs/ref1.mp4` (51,2 s). Format: the 2D "ref2 look" (no voxel world) — spoken headline, one card,
small whole mascot bottom-left, beat counter "NN / 24" bottom-right, particles + grain, pill CTA "Komen PETA".

## Pipeline (re-runnable from this folder)
1. `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` (auto tags; take 1 kept in the
   session scratchpad) → `python3 tools/words.py` (production/words.json) → `python3 tools/vo_check.py assets/audio/vo.mp3 small|medium`.
2. `python3 -I tools/vo_data.py` → `vendor/vo_words.js` (mascot lip sync/acting) + `vendor/words.js` (scene word times).
3. 3D logo sprites: static server on the project root, `PORT=… node tools/logo_sprites.cjs` → `assets/logos3d/*.png`.
4. Scenes = `vendor/r36.js` (pure render(t); beats = word ranges; sound events via ev()). Mascot host = `vendor/r36_host.js`.
5. Dev stills: `node tools/shots.cjs <port> <dir> 1.5,2.5,…`; SFX events: `SFX=production/sfx_events.json node tools/shots.cjs <port> <dir> ""`
   → `python3 -I tools/sfx.py` → `assets/audio/sfx.wav`.
6. `npx --yes hyperframes@0.8.186 check .` → render with the shared-lock script → `bash tools/remix_audio.sh` (two-pass −14 LUFS from the
   untouched VO + SFX + ducked bed; picture stream copied) → `python3 tools/vo_check.py out/AIP_R36_PETA_AI_AGENT.mp4 medium`.
7. Cover: `node thumbnail/render.cjs <port> "host.html?t=1.1" thumbnail/host_full.png 1100 1500` (crop → host_cut.png),
   `node thumbnail/render.cjs <port> "logo3d.html?name=claude" thumbnail/logo3d_claude.png` (crop → _cut), then
   `node thumbnail/cover.cjs thumbnail/COVER_R36_PETA_1080x1920.png 1` and `… _HD_2160x3840.png 2`.

## Beats (24, each starts 0,12 s before its first word)
01 hook map (Claude node, 7 pills, 30 dots) · 02 dots light up, counter 0→30, PETANYA GRATIS stamp · 03 input card, 6 empty slots ·
04 WhatsApp / Instagram / marketplace pop on their words · 05 Google Sheets / Kalender / Email · 06 real claude.ai window (client
recording) → collapses into the map node; tiles fly to a ring, reading lines; tiles absorbed on "semuanya" · 07 7 departments grow, chip
"7 departemen" · 08 Penjualan pill morphs into the department card; search + 3 prospects · 09 first chat typed + appointment booked ·
10 Closing (whip): proposal PDF + TERKIRIM · 11 follow-ups H+1/H+3 → answer · 12 Marketing (flip): post + comments + draft replies ·
13 CS (zoom-through): chats answered, quiet customer flagged · 14 Operasional (whip): order board + team week · 15 Admin & Keuangan
(rise): invoice sent · 16 overdue INV-0109 + drafted reminder · 17 Analis (flip): client brief + SIAP SEBELUM KETEMU · 18 card morphs
back into its pill; map with 30 dots; "Pengingat Bayar" dot grows into a 1-task card · 19 workflow doc, 4 steps typed + ticked ·
20 the reminder hits the approval gate (lock) · 21 "Kamu · persetujuan", cursor clicks Setujui, lock opens, Terkirim · 22 morning
page slides up (skeleton) · 23 BERES / NUNGGU KAMU rows · 24 "Peta AI agent" doc, pill button "Komen PETA" pressed on "peta", DM chip.

## QA
- `check` 0 errors (warnings: nested-structure kit notes, WebGL ReadPixels perf notes, read-time advisories on the fast cards).
- Snapshot every second 0,5…54,5 s (hyperframes snapshot) → sheets `scratchpad/r36/qa1_0..4.jpg`, all 55 frames looked at; fixes:
  hidden-parent visibility bug (all headlines stacked), `.in` class clash (giant reply bubbles), stamps overlapping docs, cursor target
  measured from the DOM, morning page skeleton, rise/drop transitions no longer touch the mascot head, page/doc and workflow/approval
  cross-fades separated, DM chip earlier.
