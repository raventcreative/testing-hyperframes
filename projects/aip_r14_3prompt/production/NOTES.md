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
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit).
- `npx --yes hyperframes@0.8.186 validate .` → **0 errors**; kit warning "multiple instances of Three.js" (robot + mascot bundles) + WebGL
  ReadPixels perf notes. The 5 WCAG notes of that run were fixed afterwards (transcript timestamps #8a9ab8 → #5d6f8f; the "done" veil
  on mini cards 1–2 lightened .55 → .42).
- Real-runtime snapshots (`snapshot --at … --no-end --timeout 60000`), JPG sheets only, PNG dumps deleted:
  - full pass, 73 frames (every scene several times, every cut ±0.03–0.07 s, first + last frame): `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r14/qa1/contact-sheet-1.jpg` … `-9.jpg`;
  - fix passes after the fixes below: `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r14/qa2/contact-sheet-1.jpg` … `-3.jpg`, `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r14/qa3/contact-sheet-1.jpg`, `-2.jpg`,
    `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r14/qa4/contact-sheet.jpg`.
- Bugs found in the real runtime and fixed: (1) s03 used the id `s03-ok` for its "Pola tersimpan" chip, colliding with the prompt card's
  own `-ok` (Tersalin) → the card showed "Tersalin" before the click and the chip appeared too early → renamed `s03-saved`; (2) s02
  connector lines (round caps, dash offset = length) left dots at the node ends before they were drawn → hidden until drawn, ids
  `s02-cn*` (no clash with the card's text lines `-ln*`); (3) near-empty frames between the prompt scenes → slots now overlap
  (`OVL` s01–s03 0.3 s, s04 0.25 s, in tools/build_index.py + vendor/scenes.js): the outgoing scene fades UNDER the next card, which
  turns opaque in 0.12 s; (4) "5 alat siap" chip collided with the HyperFrames tick → moved onto the hub's bottom edge; (5) the
  selera.md chip crossed the transcript text → it now pops above the preview and drops into it; (6) s05 card-3 pulse fought the OUT
  tween (end scale 1.04 ≠ s06 start) → pulse moved to its number badge; s05 end state = s06 frame 0 (verified at 46.15 / 46.2 s).
- Every initial state is pinned on the timeline at 0 (`I()` in the kit); no Math.random / Date / rAF / CSS animation in scenes; no 3D in
  scenes (robot + mascot are the kit's WebGL hosts).

## Known issues / notes for the lead
- Robot flies in on "tiga" (~1.3 s); frame 0 shows the title "[3] prompt", the card deck, the bookmark button and the mascot.
- Prompt cards are fully readable for ~1.0–1.5 s each before they fold (viewers can pause); the complete prompts are in the DM file
  `production/TIGA_PROMPT.md` (on-screen text = short form of the same prompts, consistent).
- Captions: during the 0.34 s word rise a chunk can show only i-dots / descenders of the next word on a single frame (kit caption system).
- Transitions between prompts are 0.25–0.3 s crossfades: for ~2 frames the new card is still semi-transparent over the old content.
- Values on screen (console "cepat", "besar, di tengah", transcript lines/timestamps, video-0N.mp4, the preview person) are labelled or
  obviously examples (CONTOH tag on the console); no numbers or results are claimed. Claude is never called free; the reel says nothing
  about price — the DM file states that Claude Code needs a paid Claude plan and that Remotion has a company licence above 3 employees.
- `.hyperframes/` was (re)created by the CLI snapshots (gitignored). The VO is 49.5 s (brief: 35–50 s) — at the upper end.
