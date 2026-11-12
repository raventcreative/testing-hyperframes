# NOTES — R11 · Agen ngoding open source dari DeepSeek (DeepSeek Harness) (AI PRENEUR · NAVY)

- **Duration** 47.47 s (1424 frames @30) · VO 45.84 s starting at 0.30 s · CTA keyword **NGODING**.
- **Kit**: copied from `projects/aip_r9_youtube` (newest NAVY; without `out/`, its audio, QA, cover PNG, `.hyperframes/`); index built by
  `tools/build_index.py`; shared scene kit `vendor/r11kit.js` (= R9 kit minus the 11 skill tiles: step header with icon/number roll,
  4 progress segments, lucide icons (ISC, 24 new: plug, cpu, laptop, shield, box, archive, eye, globe, code, …), timeline boilerplate
  incl. the per-letter typer). Audio setup as batch 3/4: `<audio id="vo" src="assets/audio/vo.mp3" data-start="0.3">` +
  `<audio id="sfx" src="assets/audio/sfx.wav">` (no music; the lead adds the ducked bed + loudness pass).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3`
  (NO `--tags` = client's auto tags: `[playful] [excited]` on every line, + `[confident]` on the CTA line) → `assets/audio/vo.mp3`;
  `tools/el_to_words.py` → `production/vo_words_raw.json`; `tools/timing.py` → `production/timing.json` + `vendor/vo_words.js`.
  Caption merges: "M I T." → **MIT.**, "Node JS" → **Node.js**. One word excluded from the onset snap ("kuat.", NOSNAP in timing.py:
  the energy heuristic had moved it onto line 5's onset). Pronunciation checked with faster-whisper small (all lines read).
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples).
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_NGODING_1080x1920.png` (`node thumbnail/render_cover.cjs thumbnail/COVER_NGODING_1080x1920.png`,
  static server on :8931 at the project root). NAVY like the reel: chip "OPEN SOURCE · DARI DEEPSEEK · MIT", "Agen AI buat / NGODING /
  tanpa langganan bulanan", the OTAK socket + three brains (DeepSeek API · Claude · GPT · Model lokal · Ollama), mascot + typing robot.
  No DeepSeek / GitHub logo.

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–7.10 | Reel ini aku bikin bareng agen AI yang nulis kode. Agen kayak gini biasanya langganan, yang ini open source. | code editor "reel-ini.html" + mini 9:16 phone: each code line builds its element in the phone (frame 0 = 2 lines built); "agen AI · nulis kode" chip; play on "kode."; white subscription card "Langganan" with 12 month tiles stamped TAGIH + "bayar tiap bulan" (labelled contoh, no price); X stamp, card tips away; OPEN SOURCE badge group (code tile, "Open source", pills kode terbuka · tanpa langganan) |
| s02 | 7.10–13.00 | Kenalin, DeepSeek Harness, lisensi MIT. Harness-nya gratis, otaknya kamu yang pilih. | badge lifts, step header drops in as the repo (plug tile, DeepSeek Harness, github.com/deepseek-ai/deepseek-harness, MIT); repo card "Everything is a Plugin." (official description) + ★ 279 rb+ bintang + MIT stamp + "dicek 12 Nov 2026"; RANGKA AGEN board: real plugin parts (Alat/tools, Riwayat sesi, Loop agen, Tampilan web) click in around an empty dashed OTAK socket, GRATIS stamp; "pilih" = socket label spins DeepSeek → Claude → GPT → model lokal |
| s03 | 13.00–19.90 | Suruh bikin katalog toko kue: dia ngebaca file, ngubah kode, ngejalanin perintah, dan minta izin buat aksi penting. | header 01 "Cara kerjanya"; Web UI window (our mock, CONTOH, workspace toko-kue/): task types "Bikinin katalog toko kue + tombol pesan WA"; Baca file (menu.json · index.html) ✓, Ubah kode (katalog.html · tombol WA) ✓, Jalanin perintah (npm run dev) → "menunggu izin"; approval card "Izinkan perintah ini?" Tolak / Izinkan, cursor clicks Izinkan on "aksi" → ✓ jalan |
| s04 | 19.90–28.20 | Pilihannya: DeepSeek bayar per pemakaian, Claude atau GPT pakai API key, atau model lokal di Ollama, gratis asal laptopnya kuat. | header 02 "Pilih otaknya"; left OTAK TERPASANG socket + BIAYA block, right 3 options; each lights on its words and its chip plugs into the socket: DeepSeek (per token · potong saldo, usage meter) → Claude / GPT (tagihan provider-nya, key wiggle) → Ollama (tanpa tagihan API, GRATIS stamp, amber RAM / GPU bar = butuh laptop kuat); footer "harness-nya tetap gratis (MIT)" |
| s05 | 28.20–35.57 | Cara mulai: pasang Node.js terbaru, jalanin satu perintah, browser kebuka. Isi API key, pilih folder, beres. | header 03 "Cara mulai"; terminal: requirement chip Node.js ≥ 24.9 ✓ (nodejs.org), `$ npx @deepseek-ai/dsh web` types + SATU PERINTAH flash, "✓ Web UI jalan → http://127.0.0.1:3080"; browser card opens: Settings → Models, DeepSeek API key sk-•••• ✓; Choose workspace toko-kue/ ✓; "siap dipakai" |
| s06 | 35.57–43.67 | Catatannya: masih developer preview, belum diaudit keamanan. Pakai VM terpisah, backup dulu, cek tiap perintah sebelum diizinkan. | header 04 "Cek aman dulu" (PENTING); amber-accent status card "Developer preview" + "versi baru bisa bikin setelan lama nggak cocok" + "sumber: README + SAFETY.md di repo", BELUM DIAUDIT + RISIKO SENDIRI stamps; 3 checks wait dimmed, then light + tick: Pakai VM / container terpisah · Backup dulu · Cek tiap perintah sebelum diizinkan; last 0.45 s → link card |
| s07 | 43.67–47.47 | Komen NGODING, aku kirim lewat DM. | link card "deepseek-harness · link repo + checklist aman"; comment bar, NGODING typed per letter, heart; DM panel (AI PRENEUR) + paper plane, link card lands as attachment, "terkirim"; end logo (corner logo fades at 46.07) |

Hand-overs: s01 → s02 rebuilt 1:1 (OPEN SOURCE badge group); s02 → s06 keep the same header plate (contents roll); every workspace
exits in its scene's last ~0.2 s so the next scene starts from the header alone; s06 → s07 share the link card.
Hosts: mascot bottom-left (welcome, explain on "agen", emphasize on "langganan", reveal on "open", present per step, compare on
"Catatannya", cta on "Komen", point on "DM"); robot bottom-right (types the code, shakes its head at "langganan", cheers "open",
thinks on "otaknya"/"izin", types the task / npx / API key, scans files / Ollama / the checklist, shock on "diaudit", cheers the CTA).

## Sources (checked 12 Nov 2026) — claim-by-claim table in `production/VO_SCRIPT.md`
- github.com/deepseek-ai/deepseek-harness — repo page (About "DeepSeek Harness: Everything is a Plugin.", 279.5k stars, MIT), README.md
  (developer preview + compatibility-breaking changes, `npx @deepseek-ai/dsh web`, Web UI at http://127.0.0.1:3080, run from source),
  SAFETY.md (not audited, own risk, VM/container, backups, review commands), LICENSE (MIT, © 2026 DeepSeek), package.json
  (engines node ">=24.9.0"), docs/architecture.md (every part is a plugin: model adapter, tool registry, session log, agent loop; web
  app bundle), docs/user/guide/index.md (Settings → Models, Choose workspace, read/edit files, run commands, asks before approval-gated
  operations), docs/user/guide/providers.md (anthropic / openai / moonshotai / zai providers by API key; Custom model API for
  self-hosted OpenAI-compatible servers).
- registry.npmjs.org/@deepseek-ai/dsh — MIT, engines node >=24.9.0.
- github.com/ollama/ollama — docs/api/openai-compatibility.mdx (OpenAI-compatible endpoint http://localhost:11434/v1/), README.
- api-docs.deepseek.com/quick_start/pricing — per-token billing deducted from the topped-up/granted balance (read via search snippet;
  the host is not reachable from this session — no prices are shown in the reel).
- NOT used: third-party "star record" numbers (74k day one / 200k in two weeks): conflicting, not on official pages.

## DM text for the NGODING keyword (suggestion for the client's DM reply)
Ini link repo DeepSeek Harness: https://github.com/deepseek-ai/deepseek-harness
Cara mulai: pasang Node.js versi 24.9 ke atas → jalankan `npx @deepseek-ai/dsh web` → browser kebuka di http://127.0.0.1:3080 →
Settings → Models (isi API key) → Choose workspace (pilih folder proyek).
Checklist aman (dari SAFETY.md di repo): 1) jalankan di VM / container / komputer terpisah, 2) kasih akses seminimal mungkin,
3) backup file yang bisa diakses agen, 4) jangan taruh password / API key / data penting di situ, 5) cek plugin, setelan dan tiap
perintah sebelum klik izinkan. Ingat: masih developer preview dan belum diaudit keamanan.

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the R9 kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors; warnings = "multiple Three.js instances" (robot + mascot bundles, as in the
  kit), SwiftShader ReadPixels notices, contrast notes on hidden text only (off-screen digits of the header number roll, the step
  numbers hidden under their check badges in s06). The two real low-contrast items it found (white "TAGIH" on coral 2.79:1, cyan "→" on
  white 2.77:1) were fixed (#d63b30 ≈ 4.6:1, #0889b3 ≈ 4.0:1 on large bold text).
- Snapshots (`snapshot . --at … --no-end --timeout 60000`): one full pass of 65 frames — first frame, every scene's beats, both sides of
  every cut, the end — plus one targeted fix pass (4.9, 33.3, 43.3, 43.45, 43.6 s) after the s06 → s07 hand-over fix. Contact sheets:
  `production/qa/runtime_full_1..3.jpg` (full frames), `production/qa/runtime_hero_1..3.jpg` (hero zone + captions, larger),
  `production/qa/runtime_fix_*.jpg`. The PNGs were deleted after the sheets were made (disk budget).
- Every scene script checked for exceptions (a throwing scene stays static in snapshots); every `wt()` word lookup verified against
  timing.json; all 37 caption chunks measured: one line each, x 124–956, y 960–1030 (nothing covers them; hero content ends ≤ 932).
- Initial states pinned at 0 through the kit's `I()` (gsap.set + tl.set at 0); positions clamped ≥ 0.

## Known issues / notes for the lead
- Frame 0 shows the code editor + phone but no hosts yet: the robot flies in over 0.75 s and the mascot pops up over 0.5 s (kit
  behaviour, same as R9). The cover PNG is the intended thumbnail.
- Short header-only beats at the very start of s03–s06 (≈0.1–0.3 s while the header number rolls) — intentional breathing room, as in R9.
- s01 "Reel ini aku bikin bareng agen AI yang nulis kode" is true for AI PRENEUR reels (HTML/GSAP written by an AI coding agent with
  HyperFrames); the reel is NOT made with DeepSeek Harness and the VO does not say so.
- "★ 279 rb+ bintang" is the count on the official repo page on 12 Nov 2026 (279.5k); it can only go up, so "279 rb+" stays true.
- DeepSeek pricing was read from the official pricing page's search snippet (the host api-docs.deepseek.com is not reachable from
  this session); the reel shows no prices, only "bayar per pemakaian / per token, potong saldo".
- The Web UI, terminal and browser cards are our own mocks of the documented flow (labelled CONTOH where they show example data); the
  file names (menu.json, katalog.html), `npm run dev`, "toko-kue/" and the masked key are illustrative.
- `tools/render_chunks.py` (kit helper) now cuts at the s04 and s06 starts; `hyperframes snapshot/validate` wrote `.hyperframes/`
  (video state) into the project folder; harmless.
