# NOTES — R30 · Tim marketing AI, 3 modul (AI PRENEUR · NAVY) · `projects/aip_r30_timmarketingai/`

- **Duration** 90.47 s (2714 frames @30) · VO 88.04 s from 0.30 s (take 2 + 6 × 0.7 s section breaths) · CTA **MARKETING** · reference
  `aip_remake_batch7/refs/ref4.mp4` (92.35 s) → −2 %.
- **Kit**: copied from `projects/aip_r25_prompt3d` (NAVY) without `out/`, QA, cover, scenes, music bed; mascot glance disabled (kit);
  new shared kit `vendor/r30kit.js` (scene boilerplate from R25 + cam/hud layers, module header with loop mini-map, 3D logo sprites,
  accent dot, flood helpers, org markup), icons `vendor/r30icons.js` (Lucide 1.70.0), logos `vendor/logos.js` (Simple Icons 16.38.0).
- **Final**: `out/AIP_R30_TIM_MARKETING_AI.mp4` (render_aip.sh: render + ducked music bed + −14 LUFS).

## Pipeline (re-runnable)
1. `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` → `production/vo_el_raw.json`
   (copy of the raw json) → `python3 -I tools/vo_pad.py .` → `assets/audio/vo.mp3` + `production/vo_el.json`.
2. `python3 -I tools/el_to_words.py .` → `python3 -I tools/timing.py .` (auto caption chunks ≤3 words, MARKETING marker) →
   `python3 -I tools/build_index.py .` → `python3 -I tools/sfx.py .`.
3. 3D logos: static server at the project root, `PORT=… node tools/logo_sprites.cjs` → `assets/logos3d/*.png` (36-frame turntables).
4. Cover: `PORT=… node thumbnail/render.cjs logo3d.html thumbnail/logo3d_claude.png name=claude 1` (crop → `_cut.png`), then
   `node thumbnail/render.cjs cover.html thumbnail/COVER_MARKETING_1080x1920.png "" 1` and `… _HD_2160x3840.png "" 2`
   (the mascot is the reel's own rig posed at t=46.2 s, re-framed to the centre).

## Scenes
| id | start–end | content |
|----|-----------|---------|
| s01 | 0.00–13.47 | spinning to-do reel (lands per chore, 1..7 dari 7) → "Semua: kamu sendiri?" wobble → chips burst → 3 TIM AI boxes → boss card "Kamu" + lines |
| s02 | 13.47–24.60 | boxes → pills; funnel drawn, dot drops through → "selesai", struck → ring with 3 stations, dot laps, Minggu 1→2; rule #1 gate: post bounces off the lock, "Setujui" pressed, post enters feed; button → cyan flood |
| s03 | 24.60–38.27 | flood → Modul 1 header; radar + 3D Claude logo, trend chips, question bubbles + frequency bars (CONTOH kedai kopi); process fill into "Bank ide"; 3 typed drafts; 7-day calendar fills; dot flood |
| s04 | 38.27–55.10 | Modul 2: draft → Kreatif → Distribusi; Higgsfield tiles resolve; ElevenLabs 3D logo + waveform driven by the real VO envelope; post + Setujui + Disetujui stamp + schedule; copies → 3D Instagram/TikTok/WhatsApp; comment + typed reply ("gaya bahasamu"); sensitive comment → "Inbox kamu"; whip pan out |
| s05 | 55.10–69.23 | whip in; Modul 3 loop with station 3 lit; results table (likes vs chat/booking/jual bars, CONTOH), likes struck, winner; dot rides 3→1; 4-week chart (ILUSTRASI) line drawn by the dot; spreadsheet struck; dive out |
| s06 | 69.23–80.43 | 3D Claude Code logo + title; terminal (CONTOH) ticks modules; 3 connector cards (MCP) lit along cables, mini 3D channel logos; morning page "Ringkasan pagi" with 3 sections; swipe up |
| s07 | 80.43–90.47 | AI card (data moves) vs Kamu card (Brand, Budget, lock); comment bar types MARKETING; DM panel + blueprint file + "terkirim"; dot blooms into the AI PRENEUR end card + "Komen MARKETING" |

## QA
- `npx --yes hyperframes@0.8.186 check .` → 0 errors (warnings: per-word caption read-time notes, kit nesting, contrast false
  positives measured against the mascot canvas, masked reel rows "outside" their viewport).
- Real-runtime snapshots every second 0.5…90.5 s → `production/qa/runtime_full_1..8.jpg` (6×2 sheets); fix pass →
  `production/qa/runtime_fix.jpg`. Fixed: week counter showing the next line, rule chip off-frame, funnel label under the pills,
  dot covering chip/station text, channel logos shown too briefly, sensitive card over the dimmed thread, chart labels cut at the
  left edge after the shift, connector mini-logos over the card label, empty beats (s03 start, s04 start, s06 page gap), caret gap.
- Mascot eyes: pupils in every QA frame (glance disabled). Captions never covered (hero content ≤ y 935).

## v3 — client's own Instagram recording (client rule 2026-11-20: real screen recordings instead of mock UI)
- `assets/rec/ig_freddie.mp4` (client's recording of @aipreneur_academy) → `assets/rec/seq/` (chrome, IG nav and the Messages pill
  cropped out: 1408×812 at x 248, y 128; header still from 3.0 s; scroll 14.6→26.8 s speed-ramped into 37 frames @30 fps).
- s04 changed between 48.1 and 50.7 s only (timeline/VO unchanged): after "setujui" the mock post card, stamp and button give way to a
  window "Instagram · @aipreneur_academy · REKAMAN ASLI" (48.10); "postingan dijadwalkan": push-in 1→2× on the real profile header
  (48.38–48.98) + "terjadwal" in the title bar (48.60); pull back (49.05–49.37), cyan ring on the real "Tim Marketing AI / Kamu Bosnya"
  post (49.32–49.57); real grid scroll, speed-ramped (49.52–50.75); 3D Instagram/TikTok/WhatsApp logos in a column beside the window
  (49.45–49.8), docking above the thread at 50.43; window fades at 50.38. Comment thread restyled like IG dark comments (username +
  text on a dark row); thread/reply/sensitive/"Inbox kamu" moments unchanged in time. Mock "copy" cards and channel labels removed.
- Previous final kept as `out/AIP_R30_v2_mockIG.mp4`.

## 2026-11-20 — status
- Delivered final = mock-IG version (out/AIP_R30_TIM_MARKETING_AI.mp4, fixed VO, -14.7 LUFS).
- The composition now uses the client IG recording (assets/rec/, local only, gitignored). Its re-render was stopped on the client request ("buat simpenan"); render + remix with tools/remix_audio.sh only if asked.
