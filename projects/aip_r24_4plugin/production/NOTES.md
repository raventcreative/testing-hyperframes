# NOTES — R24 · 4 alat biar web dari Claude Code jadi sampai online (LIGHT) · `projects/aip_r24_4plugin/`

1080×1920 · 30 fps · **45.20 s** (1356 frames) · VO 43.68 s file (speech 0.07–43.44 s) starting at 0.30 s · HyperFrames 0.8.186. Kit:
`aip_r20_freellm` (LIGHT, mascot glances already disabled; `out/` not copied). Not rendered (the lead renders), not committed. Reference:
`projects/aip_remake_batch6/refs/ref4.mp4` (51 s, Indonesian). CTA keyword **ALAT**; DM hand-out: `production/DM_ALAT.md`.
Sources + ATM: `production/VO_SCRIPT.md`. `.gitignore` in this folder: `out/`, `.hyperframes/`.

## Pipeline (all re-runnable, run from this folder)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3`
   (NO --tags → client's auto tags: `[playful] [excited]` on every line + `[confident]` on the CTA) → `assets/audio/vo.mp3` + `vo.json`.
   **Take 1 only** (43.68 s, 728 characters). whisper small + medium check in VO_SCRIPT.md (brand names are written phonetically by
   whisper: Cloud Code / SuperBase / Versal / Contact 7 — no Indonesian word misheard by both models → no re-take).
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the ElevenLabs character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js`. TFIX (checked against the energy envelope +
   whisper): "Context Seven dari Upstash" (alignment ~0.2 s late), "production." in line 7 (0.4 s late), and three words the energy snap
   would have pushed onto the next word ("Empat,", "cek,", "oke."). MERGE: "Claude Code" (one caption word), "Context Seven" → **Context7**;
   FIXI: spoken "alat," → caption **ALAT,**.
4. `python3 -I tools/scenes.py .` → `vendor/scenes.js` · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; ≈ −31.8 LUFS vs VO ≈ −18.1 LUFS). No music (lead adds it).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_ALAT_1080x1920.png` (default URL http://127.0.0.1:8954/proj/thumbnail/cover.html:
   any static server on :8954 whose root contains this folder as `/proj/`, or set `COVER_URL`).

## Shared visual system — `vendor/r24kit.js` (window.K) + `vendor/r24icons.js` (lucide-static 0.460.0, ISC)
Metaphors (ours): the code alone is **half the road**; the 4 tools come out of a **toolbox**; Context7 = a **library card** that borrows
the official docs of the exact version in package.json; Supabase MCP = the **key to the data warehouse**; Chrome DevTools MCP = Claude as
the shop's first **test buyer** in a real browser; Vercel = a **launch console** whose PRODUCTION switch sits under a safety cover.
One Indonesian UMKM example runs through the whole reel: the pre-order web of a fictional **"Toko Kue Rumahan"** (labelled CONTOH/ILUSTRASI).
- `K.term` (Claude Code window, text + generic terminal icon), `K.head` (tool title card), `K.orderPhone` / `K.toolbox` (the exact markup
  shared by s01 → s02 → s03 so the hand-overs are pixel-identical), `K.store` / `K.item` / `K.field` / `K.button` (the order page),
  `K.cursor` (pointer + label "Claude · pembeli uji" / "kamu"), chips / stamps / tags.
- `K.boot(ID)`: seek-safe scale shorthand; **every initial state pinned at 0 in a nested timeline P0 that is the first child at 0**;
  fromTo without immediate render; word lookup that THROWS on a missing word; `$()` that throws on a missing OR duplicate id (caught two
  id clashes during the build); typed text with caret; `done()` = end marker + backward-seek patch + **`tl.render(0, true, true)`** +
  registration. index.html (captions, logo, grid, grain) and s08 use the same rule. Robot + mascot word lookups throw too.
- No brand logos anywhere (Claude/Anthropic, Upstash, Supabase, Google/Chrome, Vercel are text only; lucide's "chrome" icon deliberately
  not used). The browser is a generic window. Tool names on screen are the real ones (`resolve-library-id`, `query-docs`, `execute_sql`).

## Scenes (global s)
| id | start–end | VO | visual |
|---|---|---|---|
| s01 | 0.00–3.07 | Kode dari Claude Code itu baru setengah jalan. | frame 0: Claude Code window writing the order form + phone where the web builds itself (top half real, bottom half dashed wireframe); "Claude Code": tag "✓ KODE JADI"; "baru setengah": card "PERJALANAN WEB-MU" Kode → Online fills to the middle, dashed line "SETENGAH JADI" cuts the phone; "jalan.": pin "Kamu di sini" drops; window + card leave, phone stays |
| s02 | 3.07–7.30 | Biar web pesanan toko kue kamu jadi sampai online, pasang empat alat ini. | phone glides left, chip "CONTOH · web pesanan toko kue"; shop header/items pulse; "jadi": the dashed half becomes the real form + "Pesan sekarang"; "online,": dashed target badge (globe) + tag "TUJUAN: ONLINE"; "pasang empat alat ini": toolbox "PASANG DI CLAUDE CODE · 4 alat" with 4 tiles (Kartu perpustakaan · Context7 / Kunci gudang data · Supabase MCP / Pembeli uji coba · Chrome DevTools MCP / Tombol luncur · Vercel) |
| s03 | 7.30–13.90 | Satu, Context7 dari Upstash: sebelum ngoding, Claude ngecek dokumentasi resmi sesuai versi yang kamu pakai. | starts as s02 ends; tile 1 flies into a LIBRARY CARD "KARTU PERPUSTAKAAN · Context7 · dari Upstash · server MCP · ANGGOTA Claude Code" (barcode beep); Claude Code window types "bikin form pesanan kue, pakai Next.js. use context7", tag "CEK DOCS DULU", tool calls `resolve-library-id` / `query-docs`; "DOKUMENTASI RESMI · Next.js" card slides out + green tick on "resmi"; "versi": `package.json → "next": "16.x"` highlighted, dashed link, stamp "VERSI 16.x"; "✓ ngoding pakai docs v16" |
| s04 | 13.90–20.73 | Dua, Supabase MCP: Claude bikin tabel pesanan di database, dan tiap perubahan disimpan sebagai migration. | key card "2 · KUNCI GUDANG DATA · Supabase MCP · resmi dari Supabase" + locked "Database · toko kue"; "MCP:": key flies over, turns, "terkunci" → "terhubung"; table "pesanan" (NAMA · KUE · AMBIL · STATUS, rows Rina/Dewi, ILUSTRASI); "tiap": card "migrations/ · tiap perubahan tercatat · bisa diulang" + `01_buat_tabel_pesanan.sql ✓`; "perubahan": new green column CATATAN; "disimpan sebagai migration": `02_tambah_kolom_catatan.sql` flies from the column into the list ✓ |
| s05 | 20.73–28.37 | Tiga, Chrome DevTools MCP dari Google: Claude buka webnya di Chrome, nyobain pesan kayak pembeli, lalu ngecek console sama network. | head "3 · PEMBELI UJI COBA · Chrome DevTools MCP · dari tim Chrome · Google"; generic browser (tab "Toko Kue Rumahan", URL `localhost:3000/pesan` types, badge "dikendalikan Claude"), page loads on "webnya"; cursor "Claude · pembeli uji" fills NAMA "Rina" / KUE "Bolu pandan" / TANGGAL "Sabtu, 10.00", presses "Pesan sekarang" → toast "Gagal kirim pesanan"; "lalu": DevTools drawer (Console "Failed to load resource: 500", Network "POST /api/pesanan 500", "contoh error"), rings on "console" / "network", chip "dibaca Claude" |
| s06 | 28.37–34.00 | Empat, Vercel: Claude deploy ke link preview buat kamu cek, baru production setelah kamu oke. | head "4 · TOMBOL LUNCUR · Vercel · plugin resmi Vercel · deploy langsung dari Claude Code"; PANEL DEPLOY: cursor "Claude" presses the big DEPLOY button (ripple, rocket dot) → "link preview dulu"; card "LINK PREVIEW · tokokue-k3x9-kamu.vercel.app · belum dilihat pelanggan · CONTOH"; "Kamu cek dulu" card ticks 3 checks; "production": the covered PRODUCTION switch glows amber; "kamu oke": cursor "kamu" presses "Oke, naikkan ke production", cover lifts (lock opens), switch flips green, chip "LIVE · tokokue-kamu.vercel.app" |
| s07 | 34.00–41.70 | Hati-hati, akses database dan deploy itu nyentuh production. Latihan di project tes, dan baca tiap perintah sebelum kamu izinkan. | amber header "HATI-HATI · Akses = tanggung jawab" (shake); cards "Akses database · lewat Supabase MCP" / "Akses deploy · lewat Vercel" wire into "PRODUCTION · web & data asli pelanggan"; "nyentuh production": wires turn red, red ring + shake; "Latihan di project tes": green "PROJECT TES · data contoh · aman buat latihan", wires re-route, production dims + lock; "baca tiap perintah": permission prompt "Izinkan perintah ini?" `DELETE FROM pesanan;` (`execute_sql`), magnifier reads it, red ring + "hapus SEMUA data pesanan!"; "sebelum kamu izinkan": cursor "kamu" skips "Izinkan", presses "Tolak" → "ditolak · data pesanan aman" |
| s08 | 41.70–45.20 | Komen ALAT, aku kirim lewat DM. | house CTA: package card "DIKIRIM LEWAT DM · Panduan 4 alat · cara pasang · contoh prompt · catatan aman"; comment types ALAT, heart, send → plane; DM bubble "4 alat + cara pasangnya / plus catatan biar production aman", "terkirim"; end: AI PRENEUR logo + glint |

Robot (co-host, right): flies in on "baru", thinks on "setengah", TYPES on its holo keyboard when Claude Code is asked to do something
(installing on "pasang", the docs request, the table, the test buyer's form), scans docs / migrations / DevTools, cheers each tool name,
small shock at the failed order and on "Hati-hati", shakes its head on "nyentuh" and on the refused DELETE, cheers the CTA, waves at the
end. Mascot (host, left): an intent on every beat (present / explain / emphasize / point / compare / cta); **glances disabled**
(`const glance = (t) => 0;`).

## QA (real runtime: `npx --yes hyperframes@0.8.186 snapshot` + `validate`)
(filled in below after the passes)
