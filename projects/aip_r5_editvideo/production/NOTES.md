# R5 · Edit video pakai Claude, step by step — NOTES (NAVY · 1080×1920 · 30 fps · 55.17 s · HyperFrames 0.8.186)

Folder: `projects/aip_r5_editvideo/` (copied from the NAVY kit `projects/igagent_2026/` without `out/`; the kit's old scenes, reference
files and `.hyperframes` state were moved out). Served for preview: `python3 -m http.server 8825 --bind 127.0.0.1` (project root).
Not rendered, not committed.

## Pipeline
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_take1/vo.mp3 --tags "[playful] [excited]"`
   (saved voice, every line tagged) → `assets/audio/vo.mp3` (53.92 s). Sent text: `production/vo_text_sent.txt`.
2. `python3 -I tools/align_words.py . production/vo_take1/vo.json` → `production/vo_words_raw.json` (ElevenLabs character alignment →
   words; a word ends on its last letter so trailing punctuation does not swallow the pause).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (onset snapping OFF: the alignment is exact).
4. `python3 -I tools/build_index.py .` → `index.html` (captions, logo, the persistent 4-step rail, scene slots with 0.4 s overlap).
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; mean −30.6 dB like the kit).
6. Cover: `node thumbnail/render_cover.cjs <out.png>` (server on :8825) → `thumbnail/COVER_EDITVIDEO_1080x1920.png`.

Shared scene kit: `vendor/r5_kit.js` (loaded in `<head>`): lucide icons, the Claude mark, shared CSS for the generic Claude desktop
window (`R5.win`, x 60–1020 / y 404–932), the folder tree (`R5.tree`), the finished-reel card (`R5.fin`), and the timeline boilerplate
(`R5.scene(id)`: scale patch, `ft`/`I`, word-time lookup, typewriter/counter via per-step `tl.set`, seek-order patch, registration).
Every initial state is pinned on the timeline at 0; no Math.random/Date/rAF/onUpdate/CSS animation; no 3D in scenes.

## Layers
navy bg · scenes (track 2/3/4, each lives 0.4 s past its cut: its OUT plays under the next scene's IN) · robot (bottom-right) · mascot
(bottom-left) · fx: grain + white logo (top-left y 262–283) + **4-step rail** (y 316–376: Setup · Tools · Gaya · Edit; pops in when the
hook's 4 chapter markers land at 4.0–4.27 s, active pill white, done pills cyan check; fades with the logo at 53.77 s) · captions (word
chips, y ≈ 960–1026). Scene hero zone y 400–935.

## Scenes (global s)
| id | start–end | VO | visual |
|---|---|---|---|
| s01 | 0.00–4.50 | Reel ini aku edit bareng Claude. Ini setup-nya, step by step. | title "Edit video / pakai ✳ Claude" + generic editor timeline (Video/Motion/Caption/Audio); "edit" = the playhead cuts a dead bit out; "Claude." = a Claude tag rides the playhead, motion clips/caption chips/waveform fill in; "setup-nya" = 4 chapter markers; "step by step" = they fly up and become the rail |
| st1 | 4.50–13.87 | Satu: download Claude desktop … buka folder itu di Claude. | white "Claude · Desktop app · macOS · Windows" card, cursor clicks Download → 0–100 % → "Terpasang"; file window: new folder, name types "AI Video Editor", opens, 3 slots → raw-footage / referensi / export; folder chip flies into the Claude window's title bar, Claude shows the folder tree |
| st2 | 13.87–27.87 | Dua: pasang empat tool gratis … Claude yang pasang. | 4 card backs dealt 2×2, "GRATIS · OPEN SOURCE" ribbon, cards flip on their names: HyperFrames (motion graphic dari HTML · Apache-2.0, sticker "aku pakai"), FFmpeg (potong & convert video · LGPL/GPL), Whisper (suara jadi caption · MIT), yt-dlp (unduh reel buat dipelajari · Unlicense); cards shrink into the 4 official repo links in a Claude message; Claude answers with 4 green ticks |
| st3 | 27.87–40.40 | Tiga, ini kuncinya … Hasilnya satu style sheet. | key in a glowing disc orbited by the 5 style parts (turns on "kuncinya"); 3 then 5 generic reel tiles fan in, hearts on "suka"; middle reel → 6-frame film strip "via FFmpeg", Claude scan beam; white "Bedah gaya" panel, 5 skeleton rows fill on font/warna/caption/transisi/sound; "style-sheet.md" doc + "SIAP DIPAKAI" stamp |
| st4 | 40.40–50.83 | Empat: masukin raw footage … render jadi video final. | Claude window: raw_footage.mp4 attachment + typed prompt; 6-panel storyboard (Hook · Setup · Tools · Gaya · Edit · CTA) + status chips; "Kurang pas?" dashed selection; "font-nya gedein" typed + sent, caption bars grow (+A); "oke" → Storyboard green; render bar 0–100 %; finished 9:16 reel card + "export/" + "Selesai" |
| s06 | 50.83–55.17 | Mau prompt lengkapnya? Komen EDIT, aku kirim lewat DM. | reel steps aside, 4 prompt cards deal; comment row, "EDIT" types big in cyan, heart; paper plane tows the pack away → "Terkirim lewat DM ✓"; end: centred white logo + the EDIT comment |

Robot/mascot re-choreographed to the new words (`compositions/robot.html`, `compositions/mascot.html`: gesture/intent lists only).

## Sources (checked 12 Nov 2026) — details in VO_SCRIPT.md
claude.com/download · support.claude.com/en/articles/10065433-install-claude-desktop · code.claude.com/docs/en/desktop ·
github.com/heygen-com/hyperframes · github.com/FFmpeg/FFmpeg · github.com/openai/whisper (+ transcribe.py, tokenizer.py) ·
github.com/yt-dlp/yt-dlp. ffmpeg.org itself is outside this session's network allowlist (README on GitHub used instead).

## QA (real runtime)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit-level warnings about #bg/#fx nesting, same as the kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors; WebGL/Three.js perf notices from the hosts; 5 contrast warnings, all sampled on
  elements mid-exit or scrolled/clipped out of view (ribbon flying out, link chip scrolled away, attachment scrolled away, chip mid-fade).
- Snapshots of every scene, beat, cut and transition midpoint: contact sheets in `production/qa/`.

## Known issues / notes
- Mascot + robot pop in during the first 0.5–0.75 s (kit behaviour), so frame 0 shows the title + editor timeline only.
- During s01 "step by step" the 4 chapter markers fly across the title for ~0.4 s (intended motion).
- Scene hand-offs st2→st3 and st3→st4 are 0.3–0.4 s overlaps (outgoing panel fades under the incoming one).
- UI values (2:14, 1080×1920, style-sheet entries, storyboard labels) are interface examples, not claims. Claude itself is never called
  free; "gratis" refers to the 4 open-source tools. Plan requirements of the Claude desktop app are not mentioned.
- The `.hyperframes/` folder was (re)created by the CLI snapshots (gitignored).
