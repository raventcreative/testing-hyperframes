# NOTES — R29 · Bisnis itu lempar dadu (WHITE) · `projects/aip_r29_dadubisnis/`

1080×1920 · 30 fps · **164,40 s** (4932 frames) · VO 162,77 s from 0,30 s · HyperFrames 0.8.186. Kit: `aip_r24_4plugin` (white, mascot
glances disabled) for the hosts + brand assets; three.js r169 from `aip_r26_hookmatrix/vendor/three` (+ RoundedBoxGeometry) for a
NEW 3D dice/tray world written for this reel (`vendor/dice.js`). Reference: batch 7 `refs/ref3.mp4` (161,6 s) — kept full length.
CTA **DADU**; DM `production/DM_DADU.md`; caption `production/CAPTION.md`; script/ATM/facts/recipes `production/VO_SCRIPT.md`.

## Pipeline (re-runnable from this folder)
1. `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3` (auto tags) — take 1
   and take 2 kept in the session scratchpad; final = `python3 -I tools/splice_vo.py take2.mp3 take1.mp3 assets/audio/vo.mp3 7,8,20`.
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (ElevenLabs character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (TOTAL, VO_WORDS/PHONES/ENV/SCENES/CAPS).
   45 scenes = word-index starts (SC_RAW); captions: per scene, break at , . : ? or > 23 chars / 4 words; number words merged
   into figures (16,7% · 83,8% · 100% · 0,02% · 1.000 …), CTA word shown as DADU.
4. `python3 -I tools/build.py .` → `index.html` (from `tools/index.src.html`, inlines `vendor/ui.js`).
5. `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised; ≈ −30 LUFS vs VO ≈ −17 LUFS). Music bed: render script.
6. Cover: `python3 thumbnail/build_cover.py && node thumbnail/render_cover.cjs thumbnail/COVER_R29_DADU_1080x1920.png 1`
   (and `... COVER_R29_DADU_HD_2160x3840.png 2`).
7. Render (shared lock): `render_aip.sh <this dir> AIP_R29_DADU_BISNIS.mp4`; the render started before the VO joins were fixed,
   so the final audio is re-mixed from the picture with `bash tools/remix_audio.sh` (new vo.mp3 + sfx + ducked bed, two-pass
   loudnorm −14 LUFS; same timeline, video stream copied).

## Layers
- `#world` canvas (1080×800 at y 200–1000, transparent, soft fades top/bottom) = `vendor/dice.js`: dice (white/navy/blue/sky
  sets, the no-six die, ? cubes, giant + tiny die), six trays (main felt tray, small, floorless, three colour variants), padlocks,
  magnifier, gem, target flag, growth arrow, dot trails, glow rings, 100 instanced dice. Every throw is closed-form (arc → two
  damped hops, remaining spin decays to the exact face-up quaternion). Camera = shot groups with a 4 % push + 0,55 s eased blend.
  Shots shift the image down (setViewOffset) so the tray sits at y ≈ 610–930 and the cards fit above it.
- `#ui` (GSAP, `vendor/ui.js` inlined): section tab (y 318), problem chip MASALAH n/6 (top right, y 222), cards/stamps per beat,
  wipes (stripes ×6 directions), iris ×2, flood, flip, world blur, captions (per-word white boxes y 1000, key words #294b77 + marker).
- Hosts: `compositions/mascot.html` (left, half body, intent on every beat, glances disabled) and `compositions/robot.html`
  (right; flies in on "satu", types the odds/counters, cheers sixes, shakes its head at misses, scans markets).

## Beats (45) — see `production/timing.json` for exact times
s01 hook throw → 6, stat 16,7 % · s02 ten throws 83,8 % · s03 hundred-dice rain 99,99999 % · s04 question card + world blur ·
s05 paper "di atas kertas" + IYA stamp → spinning pain list → "DUNIA NYATA: BEDA" · s06 the table (dice = ide + cara, trays =
pasar) · s07 giant vs tiny die · s08 kopi susu → ruko 3 lantai crash · s09 grup keluarga tiny die · s10 die unfolds into its net
(no 6) · s11 1.000 throws counter · s12 ? cubes orbit · s13 cubes drop per "baru" + list card · s14 cubes flip into dice ·
s15 five dice 6-6-3-6-6, (1/6)^5 card · s16 tray shrinks · s17 mesin ketik map pin · s18 die bounces out · s19 iris, floor falls ·
s20 survey card · s21 warteg queue app (ilustrasi) · s22 die drops through · s23 three "lives" · s24 modal/waktu/tenaga bars ·
s25 cara A / cara B cards · s26–27 chaos swaps + scatter · s28 padlocks · s29 throw controls + converging arcs · s30 learning
chart drawn by the guide dot · s31 IDE TEPAT ring · s32 tray grows + arrow · s33 miss → idea yanked · s34 SHINY OBJECT SYNDROME
slam + gem · s35–36 route to target, gem pulls the die, progress 62 % → 0 % · s37 flip card "Kebalikannya" · s38 magnifier picks
market then idea · s39 process fill 0/4 → 4/4 · s40 throw lands 6 → dot flood · s41 three AI task cards · s42 "bukan soal
banyak-banyakan lemparan" strike · s43 three rules + final six · s44 worksheet card · s45 comment DADU → DM → logo.

## QA
- Real runtime (`npx hyperframes@0.8.186 snapshot`): full pass every second 0,5 … 163,5 s (164 frames) → sheets `r29/qa1_a … qa1_g.jpg`
  in the session scratchpad; fix pass of 24 frames on every changed beat (+ first frame 0 and last frame 164,35) → `r29/qa2.jpg`.
  PNG dumps deleted. Dev stills (plain page, no hosts) `r29/s1 … s7.jpg`.
- Fixed during QA: hook die entering off-frame; stat card "0,0 %" before the number is spoken (now "?"); the problem chip moved to
  the top right (full-width cards at y 410 covered it); spread trays cut at the edges + unreadable 3D labels (bigger, trays packed);
  giant die cut at the left edge; 3D labels for the four unknowns → HTML list card; the floorless tray never lost its floor
  (`lantai.` matched the earlier "3 lantai." — word lookups now scoped by scene); "?" cubes read upside down during the flip; exits
  that flew dice over the logo/tab → shrink exits; phone card missing `position:absolute`; ctaveil covering the worksheet; k42 text
  overlapping the rules; tank text doubled; flip card faces both visible; static survey/phone cards got per-word motion; dice storm
  kept below the kinetic type; tray shifted lower (shot offset) under the process-fill tank, the rules and the worksheet.
- `check`: lint 0 errors (5 warnings: nested timeline elements like the kits, duplicate-media hint, negative z-index on the marker).
  Browser phase: the first full run reported only "text_occluded" on the problem chip under the full-frame mascot canvas (false
  positive — the chip is visible in every snapshot) → marked `data-layout-allow-occlusion`; contrast 35/35 AA. Later re-runs could
  not finish the browser phase inside the CLI's 120 s deadline while three other renders loaded the CPU (load ≈ 14 on 4 cores).
- Mascot eyes checked in every QA frame (glances disabled): pupils present throughout.

## Known notes
- Captions: the last chunk "aku kirim lewat DM." stays over the end card (house style). Chunks are short (≤ 23 chars) so they
  never reach the mascot's head.
- All business examples, the warteg queue app, "120 ulasan" and the complaint quotes are illustrative (labelled CONTOH /
  ILUSTRASI / CONTOH TUGAS).
