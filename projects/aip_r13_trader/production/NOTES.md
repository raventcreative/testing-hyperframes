# NOTES — R13 · Claude bantu analisa saham: Day Trader Skill (AI PRENEUR · NAVY)

- **Duration** 49.47 s (1484 frames @30) · VO 47.84 s starting at 0.30 s · CTA keyword **SAHAM** · finance disclaimer pill
  "Bukan ajakan beli/jual · edukasi" on screen from frame 0 to the last frame (top-right, logo row, `#disc` in index.html).
- **Kit**: copied from `projects/aip_r9_youtube` (without `out/`, its VO/SFX/bed audio, QA or cover PNG); index built by
  `tools/build_index.py`; new shared scene kit `vendor/r13kit.js` (layer header with icon/number roll + 3 layer segments, the 11 skill chips
  and the 3 shelves CARI / RENCANA / REM, the plan chart shared by t2 → s05, lucide icons, Claude mark, timeline boilerplate with a
  wrapper-based workspace exit). Audio setup as batch 3/4: `<audio id="vo" src="assets/audio/vo.mp3" data-start="0.3">` +
  `<audio id="sfx" src="assets/audio/sfx.wav">` (no music; the lead adds the ducked bed + loudness pass).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3`
  (NO --tags = the client's auto tags: `[playful] [excited]` on every line, + `[sighs]` on line 6, + `[confident]` on the CTA) →
  `assets/audio/vo.mp3`; `tools/el_to_words.py` → `production/vo_words_raw.json`; `tools/timing.py` → `production/timing.json` +
  `vendor/vo_words.js`. Caption merges: "sebelas" → **11**, "sepuluh ribu" → **10.000**. Timing overrides (OVR in timing.py) for four
  words the ElevenLabs alignment placed late ("dan", "target." at the end of line 4, "Machine:", "sepuluh"), checked against the energy
  segments and a faster-whisper small pass. Pronunciation checked with faster-whisper small.
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples), re-cued to this reel.
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_SAHAM_1080x1920.png` (`node thumbnail/render_cover.cjs thumbnail/COVER_SAHAM_1080x1920.png`,
  static server on :8933 at the project root). NAVY: chip "11 SKILL · GRATIS · OPEN SOURCE", "Claude bantu analisa / SAHAM / yang berani
  bilang "jangan dulu"", the disclaimer pill, the three shelves with the 11 chips (time machine + risk lit, REM outlined), mascot + typing robot.
  No ticker, no numbers, no profit claim.

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–4.93 | Mau pakai AI buat trading saham? Pilih yang berani bilang: jangan dulu. | frame 0 = rising candle chart "SAHAM A" (contoh · ilustrasi) over a pulsing green BELI button; more candles climb; a pushy AI bubble "Lagi naik terus, beli sekarang!" + cursor drifting to BELI; on "Pilih" the bubble is struck (red line + X); Claude bubble slides in (typing dots) → "Jangan dulu." + "cek peluang & batas rugi kamu dulu"; BELI greys out and locks, the cursor is pushed back |
| s02 | 4.93–9.77 | Namanya Day Trader Skill: 11 skill Claude gratis, dibagi tiga lapis. | header drops in as the repo (folder, day-trader-skill, github.com/Jakeschincariol, MIT); pack card (Claude disc, "Day Trader Skill", "skill pack buat Claude · open source"); 11 SKILL + GRATIS pills; the 11 chips (real command names) burst into a mixed pile, then three shelves slide in (LAPIS 1 CARI, LAPIS 2 RENCANA, LAPIS 3 REM) and every chip flies to its shelf |
| t1 | 9.77–14.20 | Lapis satu nyari: ribuan grafik, berita, sampai laporan keuangan. | header 01 "Lapis cari"; scanner panel: 14 mini charts, a cyan beam sweeps, counter → "± 5.900 saham AS dipindai", SETUP · A/B/C tags; BERITA card (SAHAM A, 08:04, "pemicu gerak harga"); LAPORAN KUARTAL card (Pendapatan naik, Laba per saham turun, "contoh") |
| t2 | 14.20–17.90 | Lapis dua ngerencanain: titik masuk, stop loss, dan target. | header 02 "Lapis rencana"; plan chart (12 candles into a breakout, contoh): dashed entry line + dot + MASUK 1.000; red zone + STOP LOSS 970; green zone + TARGET 1.030; notes "dipasang sebelum beli" + "rasio risiko : potensi = 1 : 1" — handed over 1:1 to s05 |
| s05 | 17.90–23.20 | Plus Time Machine: 10.000 simulasi sisa sesi bursa, sebelum sepeser pun keluar. | header → history icon "/trader-timemachine"; candles clear, entry dot slides left, zones stretch; 46 simulated paths fan out of the entry, tinted by what they hit first (green target / red stop / cyan neither); counter → "10.000 simulasi"; axis SEKARANG → TUTUP BURSA; "simulasi, bukan prediksi" + "0 order terkirim · modal masih utuh" |
| s06 | 23.20–29.53 | Di contohnya, peluang target duluan sama stop loss duluan beda tipis: nyaris lempar koin. | result card, source "CONTOH DI README · 1 saham AS · 19 Okt 2026 · 10.000 simulasi"; 100-cell waffle fills 29 green / 26 red / 45 grey with rows "Target duluan 29,4%", "Stop loss duluan 25,5%", "Masih terbuka saat tutup 45,1%"; rows 1–2 pulse + "selisihnya cuma 3,9 poin"; a coin flips + "kesimpulan di README-nya: nyaris lempar koin" |
| t3 | 29.53–33.97 | Lapis tiga ngerem: batas rugi dijaga, trade yang lewat batas diblokir. | header 03 "Lapis rem"; limit card "Batas rugi per trade: $50" (contoh config · modal $5.000 · stop $5,86 per lembar); ORDER 1 (8 lembar, $46,88) meter below the limit → PASS stamp; ORDER 2 (30 lembar, $175,80) runs past the limit → BLOCK stamp, shake, dims |
| s08 | 33.97–38.03 | Nggak ada order tanpa persetujuan kamu, dan bawaannya akun latihan. | header → lock "/trader-broker"; order bar "BELI SAHAM A · 8 lembar · contoh" (menunggu) above three locked gates (1 Risk: PASS · 2 Kamu ketik "ya" · 3 Klik Allow once) that unlock one by one → "siap dikirim"; MODE AKUN switch with PAPER · akun latihan selected (LIVE · uang asli dim), `"paper": true · bawaan config` |
| s09 | 38.03–42.13 | Datanya saham Amerika, jadi anggap ini alat belajar, bukan jaminan. | header → alert "Catatan jujur" (EDUKASI); rows: DATA "Bursa Amerika" + Yahoo Finance / Nasdaq Trader / SEC EDGAR; ANGGAP INI "Alat belajar" (latihan dulu di akun paper, pahami alurnya); INGAT "Bukan jaminan" (kata README-nya: kebanyakan orang yang day trading rugi) |
| s10 | 42.13–45.97 | Pasangnya: tempel link GitHub-nya ke Claude, terus tulis install skill. | header → terminal "Cara pasang" (GRATIS); Claude chat card (own generic mock): the repo link drops in (TEMPEL), "install skill" types with a caret, send pulses; chip "di Claude Code bisa juga lewat /plugin"; last 0.42 s: header + chat fold, the link card pops at x 260, y 504 |
| s11 | 45.97–49.47 | Komen SAHAM, aku kirim lewat DM. | from the link card: comment bar, SAHAM typed per letter, heart; DM panel (AI PRENEUR) "Ini link + cara pasangnya. Mulai di akun paper dulu, ya.", paper plane, the link card lands as an attachment, "terkirim"; end logo (corner logo fades at 48.07; disclaimer stays) |

Hand-overs: s01/s02/t1/s05/s06/t3/s08/s09 workspaces exit in their last 0.22 s (wrapper drop + fade), so the next scene starts from the
header alone; the header is rebuilt 1:1 at every scene start and rolls to the next item; t2 → s05 hand the whole plan chart over 1:1
(`K.planSetFinal`); s10 → s11 share the link card. Hosts: mascot bottom-left (welcome, question on "saham?", emphasize on "jangan" /
"stop" / "sebelum" / "lempar" / "diblokir." / "bukan", present per layer, compare on "beda", cta on "Komen"), robot bottom-right (head-shake
"no" on "jangan" / "diblokir." / "Nggak" / "bukan", scans the charts / simulations / odds, startled on "stop" / "lempar" / "lewat", types the
"ya" and the install, cheers "11" / "Plus" / "skill." / "Komen").

## Sources (checked 12 Nov 2026)
- github.com/Jakeschincariol/day-trader-skill — README.md (description, "Free, MIT, no signup, no API key", "The eleven" table, install,
  "How to use it" example incl. the Time Machine result 29.4 / 25.5 / 45.1 % and "close to a coin flip", the budget example $5,000 / $50 /
  5.86 / 8 shares / $46.88, "Fine print": not financial advice, most day traders lose money, no trade without your yes, paper first, simulation
  not prediction), LICENSE (MIT © 2026 Jake Schincariol), trader-broker/SKILL.md (three gates: risk PASS, typed yes, Allow once; paper by
  default), trader-timemachine/SKILL.md, trader-risk/SKILL.md (PASS / BLOCK), trader-scanner/SKILL.md (thousands of charts), trader-budget/
  config.example.json (`"paper": true`, budget 5000, max_loss_per_trade_usd 50). Read via raw.githubusercontent.com (github.com HTML and the
  GitHub API are blocked by this session's proxy). Repo name/author also visible in the reference reel. Claim-by-claim table:
  `production/VO_SCRIPT.md`.

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as R9).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors; warnings = "multiple Three.js instances" (robot + mascot bundles, as in the kit),
  SwiftShader ReadPixels notices, contrast notes on hidden text only (the off-screen digits of the header number roll).
- QA_PLACEHOLDER
