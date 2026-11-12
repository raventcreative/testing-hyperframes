# NOTES — R14 · Claude Code edit reels: 3 prompt aja (LIGHT) · `projects/aip_r14_3prompt/`

1080×1920 · 30 fps · **50.8333 s** (1525 frames) · VO 49.52 s starting at 0.30 s · HyperFrames 0.8.186. Kit: `aip_r8_web3d` (LIGHT;
copied without `out/` and `.hyperframes/`; its scenes, kit JS, audio and production files were not copied). Serve:
`python3 -m http.server 8934 --bind 127.0.0.1` in this folder. Not rendered (the lead renders), not committed.

## Pipeline (all re-runnable)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3`
   (NO --tags = the client's AUTO tags: `[playful] [excited]` on every line + `[curious]` on "Mau teks lengkapnya?" and `[confident]`
   on the CTA) → `assets/audio/vo.mp3` + `assets/audio/vo.json` (line times, tags used, character alignment).
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js`. TFIX (checked against the energy envelope and
   faster-whisper `small`): the alignment squeezes the first word after the audio tags into the tag span ("Prompt" of lines 5/7/9, "Mau")
   and runs "alat." (end of line 3) into the pause. FIX: "YT-DLP" shown as "yt-dlp"; FIXI: the CTA word is spoken lower-case (so the
   voice doesn't spell it) and shown as "PROMPT,".
4. `python3 -I tools/scenes.py .` → `vendor/scenes.js` (`window.TOTAL`, `window.SCN`) · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −31.6 LUFS vs VO −19.1 LUFS). No music (lead adds it).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_PROMPT_1080x1920.png` (server on :8934 at the project root).

## Shared visual system — `vendor/r14kit.js` (window.R14, loaded in <head>)
- `R14.P` = the three prompts (on-screen short form, pre-broken into 5 lines that fit the 860 px well at 28 px; the full DM version is
  `production/TIGA_PROMPT.md`, consistent with the cards).
- `R14.card(p, i)` big copyable PROMPT CARD (940×560 at 70,330: number, "PROMPT n DARI 3", title, "buat Claude Code" chip, the prompt in a
  well, "salin → tempel ke Claude Code", **Salin** button / green **Tersalin**); `R14.cardIn` (dealt from lower right, lines revealed by
  masks), `R14.cardCopy` (cursor click), `R14.cardOut` (folds into `R14.strip`, 940×76 at 70,306, status "dikerjain Claude").
- `R14.scene(ID)` = the timeline boilerplate (scale shorthand patch, `ft`/`I` with every initial state pinned at 0, word lookup,
  seek-order patch, registration). Icons: lucide-static 1.70.0 (ISC) inlined; Claude mark `assets/icons/lobe-claude-color.svg` (MIT).

## Scenes (global s)
| id | start–end | VO | visual |
|---|---|---|---|
| s01 | 0.00–6.33 | Simpan dulu: tiga prompt buat ngedit reels pakai Claude Code. Ini alur yang aku pakai sendiri. | frame 0: title "[3] prompt" + a deck of three prompt cards + bookmark button; "Simpan": bookmark pressed + toast "Disimpan"; "tiga": deck spreads into 1 Siapin alat · 2 Bikin selera · 3 Edit (each with Salin); "ngedit reels"/"Claude Code": header pills; "alur": dotted flow line 1→2→3; "aku pakai sendiri": green stamp "Alur kerjaku" |
| s02 | 6.33–19.00 | Prompt satu: siapin alat … HyperFrames sama Remotion bikin animasi. | PROMPT 1 card (real text) → Salin → Tersalin → strip; work folder hub `studio-reels/` (rekaman · inspirasi · final) + Claude mark; 5 dashed slots + note "Izin dulu"; each tool on its word: node (icon, job, licence tag) + connector + tick: yt-dlp · Whisper · FFmpeg · HyperFrames · Remotion; note "*Lisensi Remotion"; "5 alat siap" |
| s03 | 19.00–30.97 | Prompt dua: bikin selera … jangan upload ulang video orang. | PROMPT 2 card → Salin → strip; 4 generic reel thumbnails + hearts; console `selera.md` (CONTOH) slides up, scan beam, dashed "pattern" frames on the thumbnails; knobs Tempo · Caption · Warna · Pembuka on their words; "Pola tersimpan"; veil + chip "Isinya nggak ditiru"; chip "Jangan re-upload video orang" (ban icon) |
| s04 | 30.97–42.00 | Prompt tiga: edit … caption-nya naikin dikit. | PROMPT 3 card → Salin → strip; transcript rows of `rekaman.mp4` (CONTOH) + 9:16 preview (MENTAH); scissors on the pauses + repeated take, rows collapse, "Jeda & take ulang dibuang", length bars mentah vs hasil; word captions; `selera.md` flies into the preview → styled caption + "3 PROMPT" sticker, EDIT v1; "Kurang pas?": dashed selection + "?"; the transcript turns into a Claude Code chat with a voice bubble; words appear as spoken; "naikin": caption moves up, EDIT v2, "Siap, caption dinaikin." |
| s05 | 42.00–46.17 | Prompt satu dan dua cukup sekali. Video berikutnya, tinggal prompt tiga. | three mini cards; stamps "SEKALI AJA" + ticks on 1 and 2; video-02/03/04.mp4 slide in and fly into card 3 (lifted, glow ring, "tiap video baru") |
| s06 | 46.17–50.83 | Mau teks lengkapnya? Komen PROMPT, aku kirim lewat DM. | the mini cards gather into the pack "3 prompt lengkap" (versi panjang + catatan); "ketik di komentar" + keycaps P R O M P T pressed in sync; pack → paper plane → DM bubble "3 prompt lengkap · terkirim"; end: big dark logo + pill "Komen PROMPT" (corner logo fades at 49.58 s) |

Robot (co-host, right): flies in on "tiga", waves on "prompt", points at the Claude Code pill and at each prompt card, TYPES on the holo
keyboard while the tools install and while the pauses are cut, scans the favourite reels, shakes its head on "bukan isinya"/"jangan
upload", thinks on "Kurang pas?", cheers the v2 caption, claps "sekali", cheers "prompt tiga" + CTA, waves at the end. Mascot (host,
left): intents on every beat (present / explain / point / emphasize / compare on "bukan isinya" / question on "Kurang pas?" and "Mau" / cta),
glances at the robot when it flies in and on "PROMPT".

## Sources (checked 2026-11-12) — details in production/VO_SCRIPT.md
code.claude.com/docs/en/overview · code.claude.com/docs/en/desktop · github.com/remotion-dev/remotion (README + LICENSE.md) ·
github.com/heygen-com/hyperframes · github.com/FFmpeg/FFmpeg · github.com/openai/whisper (+ transcribe.py, tokenizer.py) ·
github.com/yt-dlp/yt-dlp. remotion.dev itself is outside this session's network allowlist (LICENSE.md on GitHub used instead).

## QA (real runtime)
QA_PLACEHOLDER

## Known issues / notes for the lead
KNOWN_PLACEHOLDER
