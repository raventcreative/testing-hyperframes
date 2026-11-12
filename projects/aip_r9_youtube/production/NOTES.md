# NOTES — R9 · YouTube agent: 11 skill Claude buat channel kamu (AI PRENEUR · NAVY)

- **Duration** 45.70 s (1371 frames @30) · VO 44.08 s starting at 0.30 s · CTA keyword **YOUTUBE**.
- **Kit**: copied from `projects/aip_r3_desainer` (without `out/`, without its VO/QA/cover PNG); index built by `tools/build_index.py`;
  new shared scene kit `vendor/r9kit.js` (skill header with icon/number roll, 11 skill tiles, lucide icons, Claude mark, timeline
  boilerplate incl. a word-wrapping per-letter typer). Audio setup as batch 3: `<audio id="vo" src="assets/audio/vo.mp3" data-start="0.3">`
  + `<audio id="sfx" src="assets/audio/sfx.wav">` (no music; the lead adds the ducked bed + loudness pass).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3 --tags "[playful] [excited]"`
  (saved voice, every line tagged, one call) → `assets/audio/vo.mp3`; `tools/el_to_words.py` → `production/vo_words_raw.json` (from the
  character alignment); `tools/timing.py` → `production/timing.json` + `vendor/vo_words.js`. Two caption merges: "dua puluh satu" → **21**,
  "slash Y T script." → **/yt-script.** New in timing.py: the first word of every VO line is snapped to the real voice onset (ElevenLabs'
  alignment puts line-first words ~0.1–0.25 s late because of the audio-tag characters). Pronunciation checked with faster-whisper small.
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples).
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_YOUTUBE_1080x1920.png` (`node thumbnail/render_cover.cjs thumbnail/COVER_YOUTUBE_1080x1920.png`,
  static server on :8829 at the project root). Chip "11 SKILL · GRATIS · OPEN SOURCE", "Claude jadi tim / YOUTUBE / dari naskah sampai
  riset video viral", the 11 skill tiles (/yt-script + /yt-viral lit), mascot + typing robot. No platform logo.

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–6.37 | Ngurus channel YouTube sendirian? Sebelas skill Claude gratis ini bantu dari naskah sampai ide viral. | "kamu" avatar + job chips (Naskah, Judul, Thumbnail, Edit video, Balas komentar, Jadwal upload, Riset ide) pile in; shake + "7 kerjaan · 1 orang"; collapse → Claude disc + "11 skill Claude" + GRATIS / open source; 11 skill tiles dealt (3 columns); glow runs /yt-script → /yt-viral |
| s02 | 6.37–11.30 | Namanya YouTube Agent Skill: open source, tanpa daftar, tanpa API key. | title lifts away, header drops in as the repo (folder tile, youtube-agent-skill, github.com/Jakeschincariol, MIT); tiles fly into the folder, "11" badge; proof rows Open source (MIT) / Tanpa daftar akun / Tanpa API key (key struck), green check stamps |
| t1 | 11.30–16.10 | Satu, naskah dari 21 rumus hook, plus skor hook-nya sebelum rekaman. | header 01 /yt-script; HOOK card types the example hook; reel of the 21 real formula names spins → "The Question" (chip on the card); SKOR HOOK panel (Spesifik, Menyapa kamu, Taruhan, Bikin penasaran, Ringkas = example 82/90/70/86/74) + "76 STRONG"; REC → "siap rekam" |
| t2 | 16.10–18.87 | Dua, judul dan thumbnail ditulis sepasang. | header 02 /yt-package; JUDUL card types "Konten Seminggu, Direkam Sehari"; thumbnail "SEKALI REKAM"; link + cyan outline "1 PASANGAN"; lint chips 31 karakter (≤ 60) · teks beda dari judul · 2 kata (≤ 3) |
| t3 | 18.87–22.70 | Tiga, transkrip jadi daftar potongan edit, lengkap dengan timecode. | header 03 /yt-edit; TRANSKRIP card (5 timed lines); REPEAT / DEAD / FILLER struck + tagged; DAFTAR POTONGAN EDIT card with 3 cuts (DEAD trimmed from the middle); timecodes light in sequence |
| t4 | 22.70–26.47 | Empat, komentar dipilah, lalu dibalas pakai gaya bahasa kamu. | header 04 /yt-comment; 6 comments (generic @penonton_01…06) pile → 4 piles Pertanyaan 2 · Koreksi 1 · Pujian 2 · Pancingan 1; bait dimmed "tidak dibalas"; pin on the top question; reply types "Bisa banget, aku sendiri ngerekam pakai HP kok." + "gaya kamu · voice.md" |
| t5 | 26.47–29.50 | Lima, rencana upload seminggu sesuai waktu kamu. | header 05 /yt-plan; Sen–Min board: VIDEO UTAMA (Sel, 4 jam), Shorts (Rab, Jum, Min), VIDEO RINGAN (Sab, 1,5 jam), Sen + Kam "kosong"; hours bar "Waktu kamu: 8 jam · plan butuh ± 7 jam" → "muat" |
| s07 | 29.50–36.43 | Paling seru, mesin viral: … terus nyebut rumus judulnya. | header flame /yt-viral + PALING SERU ribbon + sparkles; engine panel with radar sweep; niche "masak hemat anak kos" types; 4 example results; bars run past each channel's median tick (6,4× / 4,1× / 3,2× / 2,3×), rows re-sort; formula chips The Question / Before and After / The Mistake / The List |
| s08 | 36.43–42.27 | Cara pasang: buka Claude Code, tempel link GitHub-nya, minta install, terus ketik /yt-script. | header "Cara pasang"; Claude Code terminal opens; repo URL pasted (TEMPEL); "Install skill ini, lalu cek /yt-script." types; "menyalin skills/yt-* ke ~/.claude/skills/" + "✓ 11 skill terpasang"; /yt-script with autocomplete → "jalan"; step badges 1–4; last 0.45 s → link card |
| s09 | 42.27–45.70 | Komen YOUTUBE, aku kirim lewat DM. | comment bar, YOUTUBE typed per letter (caret follows), heart; DM panel (AI PRENEUR pill) + paper plane, link card lands as attachment, "terkirim"; end logo (corner logo fades at 44.30) |

Hand-overs: s01 → s02 rebuilt 1:1 (title group + 11 tiles + glows); s02 → s08 keep the same header plate (its contents roll between
items); every workspace exits in its scene's last ~0.2 s, so the next scene starts from the header alone; s08 → s09 share the link card.
Hosts: mascot bottom-left (welcome, question on "sendirian?", present/explain/emphasize per skill, reveal on "Paling", cta on "Komen"),
robot bottom-right (no on "sendirian?", types the hook / cuts / reply / install, scans score / comments / results, shock on "mesin" and
"ngalahin", cheer on "/yt-script" and "Komen").

## Sources (checked 12 Nov 2026)
- github.com/Jakeschincariol/youtube-agent-skill — README (description, "The eleven" table, install, fine print), LICENSE (MIT),
  skills/yt-script/{SKILL.md, hooks.json (21 formulas), hookscore.py (5 properties, verdict, STRONG ≥ 72)}, skills/yt-package/SKILL.md,
  skills/yt-edit/SKILL.md, skills/yt-comment/SKILL.md (4 piles), skills/yt-plan/SKILL.md, skills/yt-viral/SKILL.md.
  Repo URL also confirmed from the reference reel's own screen recording. Claim-by-claim table: `production/VO_SCRIPT.md`.

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors; warnings = "multiple Three.js instances" (robot + mascot bundles, as in the
  kit), SwiftShader ReadPixels notices, contrast notes on hidden text only (off-screen digits of the header number roll, the step numbers
  hidden under their check badges in s08, the deliberately greyed-out "REC" before the score lands).
- Snapshots (`snapshot . --at … --no-end --timeout 60000`): 59 frames — first frame, every scene's beats, both sides of every cut,
  the end. Contact sheets: `production/qa/runtime_full_1.jpg` … (full frames) and `production/qa/runtime_hero_1.jpg` … (hero zone +
  captions, larger). The full-resolution PNGs were deleted after the sheets were made (disk budget).

## Known issues / notes for the lead
- Short "header only" beats while a skill's number is being said (≈0.3–0.6 s at the start of t1–t5, s08) — intentional breathing room,
  same as R3.
- s07: while the four result rows re-sort (≈33.9–34.4 s) two rows cross each other for a few frames — it reads as a shuffle in motion.
- All demo numbers, titles, channels and handles are invented examples (labelled "contoh" where they carry a number); the skill
  names, the 21 formula names, the 4 comment piles, DEAD/FILLER/REPEAT, the week shape (1 anchor, 1 cheap, 3 Shorts) and the install
  text are taken from the repo.
- The terminal in s08 is our own mock of Claude Code (generic dark window); "✓ 11 skill terpasang" paraphrases what the README's copy
  step does, it is not a screenshot of real output.
- `hyperframes snapshot` writes `.hyperframes/` (video state) into the project folder; harmless.
