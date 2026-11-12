# SCENE BRIEF — "Tim 3 Claude cari kerja remote" (AI PRENEUR reel remake R4) · LIGHT background

Project root: `projects/aip_r4_remote/` · 1080×1920 · 30 fps · 44.8333 s · HyperFrames 0.8.186. Kit: copied from `promptbuilder_2026`.
VO + facts: `production/VO_SCRIPT.md`. Timing: `production/timing.json` (built by `tools/align_words.py` → `tools/timing.py`).

## Host layers (index.html via tools/build_index.py; robot.html; mascot.html; vendor/rounds.js; vendor/r4kit.js)
Paint order: light background + ANIMATED grid · scenes · robot · mascot · dark logo (top-left y 262–300, leaves at 43.63 s) · captions
(navy gradient, centred y ≈ 966–1030). Hero zone y 290–935, x 60–1020 (x > 340 for y < 305). Nothing in y > 945.
- `vendor/r4kit.js` (loaded in <head>) = the shared visual system: lucide icons (`R4.svg`), the 3 members `R4.M`, the TEAM RAIL
  (`R4.rail(prefix)`: chips at left 141/411/681, top 312, 258×84), the example listings `R4.JOBS`, the job card `R4.job`, the job board
  `R4.board(prefix)` (left 70, top 316, 940×614) and `R4.spinAt(globalTime)` (rail spinner angle, continuous across cuts).
- `vendor/rounds.js` (`window.ROUNDS`) = the three members' beats (s04/s05/s06: tNum = pertama/kedua/ketiga, tName = first c-word).

## Members (semantic colours)
Claude 1 · Pencari (blue #3a6fe0, search) · Claude 2 · Penyaring (violet #7c5cff, funnel) · Claude 3 · Penulis CV (navy #294b77,
file-pen). Green = lolos/done, coral = dibuang/mencurigakan, gold = "Paling cocok".

## Scenes (global s) and hand-overs
| id | start | dur | VO | visual | end state → next |
|---|---|---|---|---|---|
| s01 | 0.000 | 4.867 | Aku bikin tim isi tiga Claude, yang tugasnya nyariin aku kerja remote. | eyebrow + 3 face-down seats → flip into the 3 members, job lines, connectors, "Kerja remote" pill slams | all out |
| s02 | 4.867 | 8.100 | Soalnya … capek banget. Buka puluhan situs loker satu-satu, apply berkali-kali, yang bales dikit banget. | search window + ENERGI battery drains; 8 job-site windows stack (text names); Apply hammered → "Lamaran terkirim" counter; inbox "Belum dibalas", "Balasan: cuma 1" | all out |
| s03 | 12.967 | 4.133 | Sekarang aku cukup ketik satu perintah, dan timnya langsung kerja. | terminal card, `/loker-remote` types (robot types), Enter; 3 sparks land as the TEAM RAIL | rail only, all ready |
| s04 | 17.100 | 4.267 | Claude pertama keliling ke banyak situs loker, ngumpulin lowongan remote yang ada. | chip 1 active; 8 site chips, scanner hops; 6 example listings fly into the tray (CONTOH) | rail (1 active) + tray |
| s05 | 21.367 | 6.933 | Claude kedua nyaring: … skill aku, … dari Indonesia, dan yang mencurigakan dibuang. | chip 2 active; 3 criteria pills; scan sweeps; 3 rejects (CPA / khusus warga AS / bayar biaya daftar) → bin; 3 survivors line up | rail (2 active) + survivors |
| s06 | 28.300 | 5.500 | Yang lolos dilempar ke Claude ketiga. Dia bikinin CV dan cover letter khusus buat tiap lowongan. | survivors tossed into chip 3; tabs per listing; CV + cover letter write (pen bubble); KHUSUS stamp; per-listing swaps | rail all done |
| s07 | 33.800 | 3.700 | Terus semuanya masuk ke satu halaman, kayak papan loker pribadi. | chips dive into the board avatars; board "Papan Loker Remote-ku" (DATA CONTOH), rows + score rings, "Pribadi" | board at rest |
| s08 | 37.500 | 3.400 | Aku tinggal cek, pilih yang paling cocok, terus klik apply. | cursor: CV preview, row 1 "Paling cocok", Apply click → "Buka halaman lamaran aslinya ↗" | board + highlight + toast |
| s09 | 40.900 | 3.933 | Mau cobain? Komen REMOTE, aku kirim lewat DM. | board folds into the "Tim 3 Claude" package; comment REMOTE types; plane; DM "terkirim"; end logo | end card |

## Conventions
Kit conventions apply (template + one root `id="root"`, prefixed ids, `_sc`/`ft`/`I` boilerplate, every initial state pinned at 0 with
`tl.set`, deterministic, no onUpdate, `tl.set({}, {}, D - 0.01)`, seek-order patch). Poppins 700/400 only.
