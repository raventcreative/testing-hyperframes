# NOTES — R4 · Tim 3 Claude cari kerja remote (LIGHT) · `projects/aip_r4_remote/`

1080×1920 · 30 fps · **44.8333 s** (1345 frames) · VO 43.55 s starting at 0.30 s · HyperFrames 0.8.186. Kit: `promptbuilder_2026` (LIGHT).
Serve: `python3 -m http.server 8824 --bind 127.0.0.1` in this folder. Not rendered (the lead renders), not committed.

## Pipeline (all re-runnable)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3 --tags "[playful] [excited]"`
   (saved voice; every line tagged) → `assets/audio/vo.mp3` + `vo.json` (line times + character alignment).
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (scene cuts, caption chunks, styles).
4. `python3 -I tools/rounds.py .` → `vendor/rounds.js` (the three members' beats) · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −30.7 LUFS vs VO −18.4 LUFS).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_REMOTE_1080x1920.png` (server on :8824).

## Scenes (see production/SCENE_BRIEF.md for the hand-over states)
| id | start–end (s) | VO | visual |
|---|---|---|---|
| s01 | 0.00–4.87 | Aku bikin tim isi tiga Claude, yang tugasnya nyariin aku kerja remote. | 3 face-down seats flip into Claude 1 Pencari / 2 Penyaring / 3 Penulis CV; "Kerja remote" pill |
| s02 | 4.87–12.97 | Soalnya nyari kerja remote itu capek banget. Buka puluhan situs loker satu-satu, apply berkali-kali, yang bales dikit banget. | search window + ENERGI battery drains; 8 job-site windows (text names); Apply hammered; inbox "Belum dibalas" |
| s03 | 12.97–17.10 | Sekarang aku cukup ketik satu perintah, dan timnya langsung kerja. | terminal, `/loker-remote` (robot types), Enter, TEAM RAIL lands |
| s04 | 17.10–21.37 | Claude pertama keliling ke banyak situs loker, ngumpulin lowongan remote yang ada. | scanner hops 8 site chips; 6 example listings into the tray (CONTOH) |
| s05 | 21.37–28.30 | Claude kedua nyaring: mana yang cocok sama skill aku, bisa dikerjain dari Indonesia, dan yang mencurigakan dibuang. | 3 criteria; rejects: CPA-only, US-citizens-only, "bayar biaya daftar dulu" (MENCURIGAKAN) → bin |
| s06 | 28.30–33.80 | Yang lolos dilempar ke Claude ketiga. Dia bikinin CV dan cover letter khusus buat tiap lowongan. | survivors into Claude 3; CV + cover letter write; KHUSUS stamp; per-listing swaps |
| s07 | 33.80–37.50 | Terus semuanya masuk ke satu halaman, kayak papan loker pribadi. | board "Papan Loker Remote-ku" (DATA CONTOH), score rings, "Pribadi" |
| s08 | 37.50–40.90 | Aku tinggal cek, pilih yang paling cocok, terus klik apply. | CV preview, "Paling cocok", Apply → "Buka halaman lamaran aslinya ↗" |
| s09 | 40.90–44.83 | Mau cobain? Komen REMOTE, aku kirim lewat DM. | package "Tim 3 Claude · /loker-remote", REMOTE types, plane, DM "terkirim", end logo |

Robot: flies in on "tiga", waves, shakes head on "capek"/"dikit"/"mencurigakan", TYPES on "ketik satu perintah" and while Claude 3
writes, scans while Claude 1 crawls, presents the board, claps on "apply", cheers the CTA. Mascot: presents each member on its ordinal.

## Sources (checked 2026-11-12)
- Claude Code subagents — https://code.claude.com/docs/en/sub-agents (own system prompt/tools/context; `.claude/agents/`; chaining).
- Custom slash commands / skills — https://code.claude.com/docs/en/slash-commands (`.claude/commands/<name>.md` → `/<name>`).
- Remote job boards shown as plain-text names (Remote OK, We Work Remotely, Remotive, Himalayas, Jobicy, Working Nomads; plus
  LinkedIn, Upwork, Glints in the "capek" scene): web search (dev.to "four remote job boards have free public APIs", aggregator
  listings). Their official sites are DNS-blocked from this sandbox, so the VO names none of them and makes no API claims.

## QA (real runtime: `npx --yes hyperframes@0.8.186 snapshot`)
- Final pass, 55 frames (every scene, each cut ±0.03 s, first + last frame): contact sheets in
  `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r4/qa_final/` (contact-sheet-*.jpg).
- `lint`: 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit). `validate`: 0 errors; kit warning "multiple
  instances of Three.js" (robot + mascot bundles); remaining WCAG notes are measured on transient states (dimmed rows, mid-scale toast).
- Every initial state is pinned at 0 on the timelines; the TEAM RAIL (s03→s07) and the board (s07→s08→s09) hand over at identical
  positions (verified on the ±0.03 s frames); the rail spinner angle is a function of global time.

## Known issues / notes for the lead
- The pain scene (s02) dramatises with illustrative UI numbers ("Lamaran terkirim" counting to 25, "Balasan: cuma 1", battery 12%);
  the tray/board/listings/scores/CV are labelled CONTOH / DATA CONTOH. No number is spoken.
- s04's first ~0.1 s is nearly empty (rail only) while the site chips stagger in; s06 has ~0.3 s with only rail + tabs after the toss.
- `production/SETUP_TIM_3_CLAUDE.md` is the DM hand-out (command + 3 subagent prompts) written to the documented formats; it was not
  run end-to-end against the live job sites (blocked here). Each site's terms of use apply (personal use).
- The HTTP server started for this session stops when the session ends; restart with the command above.
