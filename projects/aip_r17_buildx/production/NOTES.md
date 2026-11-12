# NOTES — R17 · Repo GitHub buat belajar bikin teknologi dari nol: build-your-own-x (AI PRENEUR · NAVY)

- **Duration** 42.00 s (1260 frames @30) · VO 40.40 s starting at 0.30 s · CTA keyword **RAKIT**.
- **Kit**: copied from `projects/aip_r9_youtube` (navy; without `out/`, its VO/SFX/bed audio, QA or cover PNG), with the R13 builders
  (`tools/build_index.py`, `tools/timing.py`, `tools/sfx.py`, CTA scene pattern) adapted; new shared scene kit `vendor/r17kit.js`
  (header with icon roll / title / one-line job / chip / 3 progress segments, lucide icons, Claude mark, timeline boilerplate).
  **Initial states** are pinned in a NESTED timeline that is the FIRST child of every scene timeline at 0 (`K.scene` → `pin`, `I()`),
  the same in `index.html` (captions + logo), and every build ends with `tl.render(0, true, true)`; tween positions are clamped to
  ≥ 0.005 s. Audio setup as batch 3/4/5: `<audio id="vo" src="assets/audio/vo.mp3" data-start="0.3">` + `<audio id="sfx" src="assets/audio/sfx.wav">`
  (no music; the lead adds the ducked bed + loudness pass). `out/` is git-ignored (`.gitignore` in this folder).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3`
  (NO --tags = the client's auto tags: `[playful] [excited]` on every line + `[confident]` on the CTA) → `assets/audio/vo.mp3`;
  `tools/el_to_words.py` → `production/vo_words_raw.json`; `tools/timing.py` → `production/timing.json` + `vendor/vo_words.js`.
  Take 2 is final (take 1's line 7 "kodenya" was heard as "kodonya" by faster-whisper twice → the line was rewritten, see VO_SCRIPT.md).
  Timing overrides (OVR in timing.py) for "Git," / "Docker," (line 3) and "Code:" (line 7): the onset snap had pushed them into the
  next voiced run; values checked against the energy segments + a faster-whisper small pass. No caption merges.
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples), cued to this reel.
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_RAKIT_1080x1920.png` (`node thumbnail/render_cover.cjs thumbnail/COVER_RAKIT_1080x1920.png`,
  static server on :8937 at the project root). NAVY: chip "REPO GITHUB · GRATIS · 360 TUTORIAL", "Bosen bikin to-do app? / RAKIT /
  Git, Docker & database versi kamu sendiri", the four blueprint cards from t1 (Git lit), mascot + typing robot. No star number / rank
  on the cover (those live in the reel with their check date).
- **Lead fix applied**: the mascot's "glance at the robot" (`glance` in `compositions/mascot.html`) is disabled
  (`const glance = (t) => 0;`, the old function kept as `glance_unused`) — it rendered blank white-disc eyes in the real render (R13).

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–5.73 | Portofolio kamu isinya to-do app lagi? Coba rakit Git versi kamu sendiri, dari nol. | frame 0 = board "PORTOFOLIO KAMU" with two identical to-do cards (todo-app, todo-app-2) + two dashed empty slots; "to-do app" = card 2 copies itself into slot 3 (todo-app-final) and slot 4 (todo-app-beneran), counter 2 → 4 proyek; "lagi?" = all four pulse + sticker "4× to-do app"; "Coba" = board slides away, KIT RAKIT (model-kit frame) pops with three parts on runners (blob, commit, tree); "Git" = scissors run along the runner, gates snap, frame fades; "versi kamu sendiri" = parts re-order into commit → tree → blob with arrows + hash chips, terminal types "$ mygit commit" → "✓ commit a1f3c9e tersimpan"; "nol." = stamp "BUATAN KAMU · DARI NOL" |
| s02 | 5.73–10.73 | Panduannya gratis di Build Your Own X, repo dengan bintang terbanyak di GitHub saat ini. | header drops in as the repo (folder tile, build-your-own-x, github.com/codecrafters-io, GRATIS chip pulses on "gratis"); README card: README.md, "Build your own <insert-technology-here>" (cyan marker on "Build Your Own X"), our translation of the README line, chips "CC0 · bebas dipakai" + "gratis"; leaderboard "BINTANG GITHUB · REPO TERBANYAK" + "dicek 12 Nov 2026": build-your-own-x 562 rb (#1, trophy, glow) / awesome 536 rb / public-apis 498 rb, bars to scale |
| t1 | 10.73–16.93 | Isinya ratusan tutorial step by step: bikin Git, Docker, database, sampai sistem operasi. | header → "Isinya · 30 kategori · 360 tutorial"; counter card: 360 rolls up, "tutorial · di 30 kategori · dari nol", ticker of real category names; STEP BY STEP nodes 1–5 fill; 2 × 2 white blueprint cards pop on their words: Git (7 tutorial · Python, JS, Ruby, Haskell), Docker (6 · Python, Go, C, Shell), Database (14 · Go, Rust, Python, C …), Sistem Operasi (19 · C, Rust, C++, Assembly) |
| t2 | 16.93–22.07 | To-do app udah pasaran. Git rakitan sendiri? Itu baru bikin CV kamu beda. | header → "Portofolio"; glass panel "CV PELAMAR LAIN" deals six mini CVs, all with the project row "todo-app" (rows light up), pill "6 dari 6 isinya to-do app"; white "CV KAMU" (CONTOH): Kamu · Junior Developer, PROYEK UTAMA mygit (Git rakitan sendiri · Python) + commit → tree → blob + init · add · commit · log, todo-app dimmed as "proyek lama"; pile dims; badge "INI YANG BIKIN BEDA" (no hiring claim) |
| t3 | 22.07–26.87 | Pas interview, kamu bisa jelasin cara kerjanya dari dalam, bukan cuma cara pakainya. | header → "Interview"; white question card "PERTANYAAN INTERVIEW · CONTOH — “Apa yang terjadi di balik git commit?”"; glass cutaway: CARA PAKAI strip ($ git commit -m "fitur baru" types) over a striped lid "di baliknya ?"; "jelasin" = the lid rolls up → CARA KERJA: commit (siapa · kapan · pesan → tree + commit induk) → tree (daftar file + folder → blob tiap file) → blob (isi file-nya) with hash chips; "dari dalam," = scan line + note "nama tiap objek = hash dari isinya · isi berubah, nama ikut berubah"; "bukan cuma cara pakainya." = pills "hafal cara pakai" + "paham cara kerja" (glows), the CARA PAKAI strip blinks |
| s06 | 26.87–32.60 | Tutorialnya bahasa Inggris? Jadiin Claude tutor: minta dia jelasin tiap langkah pakai bahasa Indonesia. | header → "Claude jadi tutor"; white tutorial page (CONTOH) "TUTORIAL · EN · Build your own Git · Bab 3 · Objects" with an English sentence; "Inggris?" = cyan marker + amber "?"; "Jadiin Claude tutor:" = glass Claude panel (Claude mark, "mode tutor", EN → ID chip) + a translate badge at the seam; your message types "Jelasin langkah ini pakai bahasa Indonesia, pelan-pelan. Jangan kasih kode jadi."; typing dots; Claude's answer line by line ("sidik jari" (hash) … "Coba tebak: kenapa itu berguna?") |
| s07 | 32.60–38.43 | Jangan minta kode jadi. Pakai gaya Learning di Claude Code: beberapa baris, kamu yang tulis sendiri. | header → "Gaya Learning · Claude Code · /output-style learning"; request bubble "Kasih kode lengkapnya dong, biar tinggal copy-paste." over a finished code block with SALIN → red X on SALIN, strike, stamp "KODE JADI"; Claude Code terminal (our mock) types "/output-style learning" → "✓ Output style: Learning" on "Code:"; editor objects.py (CONTOH): blob-hash function with "# TODO(human): hitung hash-nya" lit on "beberapa baris," + note "Learn by Doing · tugas kamu: isi TODO(human)"; "kamu yang tulis sendiri." = your line types "return sha1(header + data).hexdigest()" + chip "kamu yang nulis"; last 0.3 s header + workspace leave |
| s08 | 38.43–42.00 | Komen RAKIT, aku kirim lewat DM. | link card "build-your-own-x · link repo + prompt tutor" pops; comment bar, RAKIT typed per letter, heart; DM panel (AI PRENEUR) "Ini link repo + prompt tutor-nya. Rakit pelan-pelan, ya.", paper plane, link card lands as attachment, "terkirim"; end logo (corner logo fades at 40.60) |

Hand-overs: s01 exits in its last 0.22 s (wrapper drop + fade) so s02 starts on an empty hero zone and its header drops in; s02 → s07
keep the same header plate (rebuilt 1:1 at every scene start, its contents roll between items); every workspace exits in its scene's
last 0.22 s; s07 also takes the header out, s08 starts clean. Hosts: mascot bottom-left (welcome, question on "lagi?", pointFwd on
"Coba", emphasize on "nol." / "operasi." / "beda." / "bukan" / "Jangan", present per beat, reveal on "terbanyak", compare on "To-do",
cta on "Komen"); robot bottom-right (thinks at "to-do", shakes its head on "lagi?" / "To-do" / "Jangan", cheers "Git" / "GitHub" /
"rakitan" / "Claude" / "sendiri." / "Komen", scans the stars / tutorials / internals, types the prompt to Claude, the command and the
TODO line).

## Sources (checked 12 Nov 2026) — claim-by-claim table in `production/VO_SCRIPT.md`
- github.com/codecrafters-io/build-your-own-x — repo page (WebFetch): description, **562.0k stars**, 52.6k forks, CC0 badge.
- GitHub search sorted by stars (WebFetch): `stars:>300000` → #1 codecrafters-io/build-your-own-x 562k, #2 sindresorhus/awesome 536k,
  #3 public-apis/public-apis 498k, …; `stars:>540000` → one result (build-your-own-x). → "bintang terbanyak di GitHub saat ini" is
  true today; the reel dates it on screen ("dicek 12 Nov 2026"). Not used as the hook, not "of all time".
- README.md (raw.githubusercontent.com): "compilation of well-written, step-by-step guides for re-creating our favorite technologies
  from scratch", 30 table-of-contents categories, 360 tutorial entries (counted), per-category counts/languages for Git / Docker /
  Database / Operating System, "Origins & License" (CC0; started by Daniel Stefanovic, maintained by CodeCrafters, Inc.).
- git glossary (github.com/git/git `Documentation/glossary-content.adoc`, raw) + local `git cat-file` for the commit / tree / blob model.
- code.claude.com/docs/en/output-styles (WebFetch): built-in **Learning** style, `TODO(human)`, "Learn by Doing", `/output-style <style>`.
- Not reachable from this session (outside the network allowlist): git-scm.com, codecrafters.io, wyag.thb.lt — nothing on screen
  depends on them. GitHub API / github.com via curl are blocked by the proxy (WebFetch + raw files worked).

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as R9/R13).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors; warnings = "multiple Three.js instances" (robot + mascot bundles, as in the kit),
  SwiftShader ReadPixels notices; the contrast notes it raised on small UI text were fixed before the snapshot pass (darker cyan
  #08729a for text on white, darker greys for line numbers / part numbers, navy "?" on amber); re-run after the fix: 0 errors, 17
  contrast notes left, all on secondary text — the deliberately dimmed "CV PELAMAR LAIN" pile (35 % opacity behind "CV KAMU"), and
  the decorative kit part numbers A1–A3, editor line numbers 1–5 and "todo-app · proyek lama" at 4.2–4.4:1 (just under 4.5:1).
- Snapshots (`snapshot . --at … --no-end --timeout 60000 --describe false`): ONE full pass of 66 frames — first frame, every scene's
  beats, both sides of every cut, the end. Contact sheets (JPG only): `production/qa/runtime_full_1.jpg` … `_6.jpg` (whole frames,
  labelled with the time), `production/qa/runtime_hero_1.jpg` … `_9.jpg` (hero zone + captions, larger),
  `production/qa/runtime_mascot_eyes.jpg` (the mascot's eyes in all 66 frames: pupils everywhere, one normal blink, no white discs).
  The PNG dumps were deleted after the sheets were made (disk budget). No fix pass was needed (nothing changed after the pass except
  the cover).
- Layout was iterated before that with a fast DOM-only scene preview (scratch tool) that flags text overflowing its card / the frame /
  the 945 px line; every held frame was clean (only in-motion frames show transitions; the counter rollers' line boxes are clipped on
  purpose).

## Known issues / notes for the lead
- The hosts pop in over the first 0.5–0.75 s (frame 0 shows the PORTOFOLIO board without them) — same kit behaviour as R9/R13.
- Short caption gaps of ≈ 0.1 s at chunk starts (the first word of a chunk rises in), and short "header only" beats at the start of
  t1 / t2 / t3 / s06 / s07 while the header rolls (≈ 0.2–0.4 s) — intentional, same as R13. s02's lower half stays empty until the
  leaderboard arrives on "repo" (≈ 5.9–8.0 s) while the README card carries the beat.
- The star number (562 rb) and the #1 rank are dated on screen ("dicek 12 Nov 2026"); they will drift over time (the gap to #2 is
  ≈ 26 rb today). The cover carries no number and no rank.
- All mock UI is our own and labelled where it carries content: the CV ("CONTOH"), the interview question ("CONTOH"), the tutorial page
  ("CONTOH", generic chapter + sentence, not quoted from a specific tutorial), the Claude chat (generic), the Claude Code terminal
  line "✓ Output style: Learning" (paraphrase, not a screenshot), objects.py ("CONTOH"). Short hashes (a1f3c9e, 7b2e04d, e41c16a) are
  illustrative. The blob-hash code is technically correct for Git's blob ids (SHA-1 of "blob <size>\0" + content).
- Freddie's practitioner angle is NOT used (no evidence he built a project from this repo) — no "aku pakai ini buat…", no personal results.
- `hyperframes snapshot` writes `.hyperframes/` (video state) into the project folder; harmless.
