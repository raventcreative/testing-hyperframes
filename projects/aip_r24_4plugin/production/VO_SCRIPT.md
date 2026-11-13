# VO — R24 · 4 alat biar web dari Claude Code jadi sampai online · background TERANG (LIGHT) · VO 43,4 dtk bicara (video 45,20 dtk)
Referensi: batch 6 · `refs/ref4.mp4` (51 dtk, bahasa Indonesia, kreator lain, latar hitam–merah + maskot chibi berambut merah):
"Claude Code itu jago nulis kode, tapi tanpa empat plugin ini dia kerja sambil merem" → 1 Chrome DevTools MCP ("paling penting",
buatan Google: buka browser, baca error konsol, cek network, ukur performa) → 2 Context7 (dokumentasi library versi terbaru, bukan
dari ingatan lama) → 3 Supabase (nyambung ke database: jalanin SQL, bikin migration, generate types tanpa buka dashboard) → 4 Vercel
("ketik deploy", preview atau production) → "pertanyaannya bukan Claude-nya pinter atau enggak, tapi udah kasih dia mata dan tangan
atau belum?" → CTA "Komen PLUGIN, panduannya kami kirim gratis lewat DM" + kartu follow. Visual referensi: angka besar bergaris "01
DevTools", kartu gelap dengan tab Console/Network/Performance, cincin progres "Claude Code 0/4 aktif" dengan persen, pipeline
build → deploy → live, teks merah "PINTER?", baris MATA / TANGAN, kartu follow.

## ATM: what we changed
**Amati** — ide yang berguna: empat alat (MCP/plugin) yang bikin Claude Code bisa kerja di luar editor: baca dokumentasi terbaru,
pegang database, coba web di browser beneran, dan deploy. Mekanisme hook: "jago, tapi ada kekurangan" (merem). Struktur: listicle 4 alat
dengan urutan "paling penting dulu" → kalimat refleksi (mata & tangan) → CTA kata kunci ke DM.
**Tiru** — hanya ide + mekanisme listicle: empat alat yang sama (nama resminya), tiap alat satu kalimat "apa yang dia bikin bisa",
tutup dengan CTA kata kunci.
**Modifikasi** (wajib):
1. **Hook sendiri, sudut beda** — "Kode dari Claude Code itu baru setengah jalan." Sudutnya PERJALANAN sebuah web usaha dari kode
   sampai online (bukan "Claude buta / merem"). Visual: kartu "PERJALANAN WEB-MU" (Kode → Online) yang terisi cuma sampai tengah + pin
   "Kamu di sini", dan HP yang webnya baru jadi separuh (separuh bawah masih wireframe putus-putus, garis "SETENGAH JADI").
2. **Struktur, urutan, metafora visual sendiri** — urutan kita mengikuti siklus bikin web: **dokumentasi dulu (Context7) → data
   (Supabase MCP) → dites (Chrome DevTools MCP) → online (Vercel)** (referensi: DevTools → Context7 → Supabase → Vercel, "paling penting"
   dulu). Satu contoh UMKM Indonesia dari awal sampai akhir: **web pesanan "Toko Kue Rumahan"** (pre-order bolu/brownies, ambil di
   rumah; berlabel CONTOH/ILUSTRASI). Metafora per alat (milik kita): **kotak alat** "PASANG DI CLAUDE CODE · 4 alat"; Context7 =
   **kartu perpustakaan** (Anggota: Claude Code, barcode) + kartu "DOKUMENTASI RESMI" yang dicap **"VERSI 16.x"** sesuai package.json;
   Supabase MCP = **kunci gudang data** (kunci terbang ke gudang "Database", gembok terbuka → tabel "pesanan" tersusun → kolom baru
   → file migration masuk folder `migrations/`); Chrome DevTools MCP = **pembeli uji coba** (kursor "Claude · pembeli uji" mengisi form
   pesanan di browser generik, klik "Pesan sekarang", toast gagal, laci DevTools: Console + Network); Vercel = **panel peluncuran**
   (tombol DEPLOY → link preview → kartu "Kamu cek dulu" → saklar PRODUCTION di bawah tutup pengaman yang baru terbuka setelah "kamu
   oke" → LIVE). Semua dalam gaya LIGHT AI PRENEUR (latar putih–biru + grid animasi, kartu putih, teks gradasi navy, Poppins 700/400),
   maskot + robot kita. **Tidak ada**: angka besar bergaris, cincin progres/persen, kartu gelap bertab, pipeline build→deploy→live,
   teks "PINTER?", baris MATA/TANGAN, kartu follow, warna merah–hitam, maskot mereka, logo produk (semua nama alat = teks + ikon lucide).
3. **Sudut praktisi yang benar** — tidak ada klaim "aku pakai ini" atau hasil pribadi (tidak bisa diverifikasi). Yang kita bawa adalah
   kebiasaan praktisi: preview dulu baru production, latihan di project tes, baca tiap perintah sebelum diizinkan.
4. **Nilai untuk penonton Indonesia** — contoh nyata UMKM (toko kue rumahan, web pre-order) yang dipakai dari alat 1 sampai 4; peringatan
   yang dilewati referensi: **akses database & deploy menyentuh production** (web & data asli pelanggan) → latihan di project tes (data
   contoh), dan **baca tiap perintah sebelum diizinkan** (contoh layar: prompt izin `DELETE FROM pesanan;` lewat `execute_sql` → ditolak
   → "data pesanan aman"). Detail langkah aman: Vercel = preview dulu, production setelah kamu cek dan oke.
5. **CTA dan penutup sendiri** — "Komen ALAT, aku kirim lewat DM." (kata kunci kita ALAT; diucapkan "alat" huruf kecil supaya dibaca
   sebagai kata, caption menampilkan **ALAT**). Kartu DM "Panduan 4 alat · cara pasang · contoh prompt · catatan aman"; isi DM:
   `production/DM_ALAT.md`. Tanpa "follow", tanpa "gratis lewat DM", tanpa kartu profil.
- **Dibuang dari referensi:** "kerja sambil merem", "mata dan tangan", "bukan Claude-nya pinter atau enggak", "yang pertama paling
  penting" (peringkat tanpa dasar), "generate types tanpa buka dashboard", "ukur performa" (fitur ada, tapi kita fokus ke alur pembeli:
  console + network), "aplikasi kamu langsung online" (kita tegaskan preview dulu), "panduannya kami kirim gratis".
- **Beda dari `plugin4_2026`** (reel 4 plugin kita sebelumnya: Superpowers, Karpathy Skills, Caveman, Codex; NAVY; dock "cartridge"
  4 slot; hook "Sebelum vibe coding…"; CTA SETUP): alat lain semua, LIGHT, tanpa dock/cartridge, hook "setengah jalan", alur satu web
  UMKM dari kode sampai online, CTA ALAT.
- **Aturan 3 kata:** dicek otomatis (n-gram setelah normalisasi Cloud→Claude, konsol→console): tidak ada 4 kata berurutan yang sama;
  3-gram yang sama hanya nama produk ("Claude Code itu", "Chrome DevTools MCP").

## Fakta yang dicek (2026-11-13, sumber resmi)
- **Chrome DevTools MCP** — repo resmi https://github.com/ChromeDevTools/chrome-devtools-mcp (README + LICENSE Apache-2.0 dibaca
  langsung dari raw.githubusercontent.com). README sekarang menamainya "Chrome DevTools for agents (`chrome-devtools-mcp`)": "lets your
  coding agent (such as … Claude …) control and inspect a live Chrome browser"; fitur: "record traces and extract actionable performance
  insights", "Analyze network requests, take screenshots and check browser console messages (with source-mapped stack traces)",
  "Uses puppeteer to automate actions in Chrome". Pembuat: tim Chrome DevTools di **Google** — diumumkan di blog resmi Chrome for
  Developers https://developer.chrome.com/blog/chrome-devtools-mcp (23 Sep 2025, public preview); README: "Google collects usage
  statistics … to improve … Chrome DevTools MCP"; catatan rilis Chrome 149 (developer.chrome.com/blog/new-in-devtools-149, 2 Jun 2026):
  MCP server + CLI "officially stable" (lewat WebSearch). Nama tool di docs/tool-reference.md: `navigate_page`, `click`, `fill`,
  `fill_form`, `list_console_messages`, `list_network_requests`, `get_network_request`, `performance_start_trace`, `take_screenshot`, dll.
  Pasang di Claude Code (docs/client-configurations.md): `claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest`
  atau sebagai plugin `/plugin marketplace add ChromeDevTools/chrome-devtools-mcp` → `/plugin install chrome-devtools-mcp@chrome-devtools-plugins`.
  Disclaimer README: isi browser terbuka untuk klien MCP — jangan buka data sensitif/pribadi saat dipakai (→ DM).
- **Context7** — https://github.com/upstash/context7 (README + LICENSE MIT "Copyright (c) 2021 Upstash, Inc."). README: "Context7 pulls
  up-to-date, version-specific documentation and code examples straight from the source — and gives them to your coding agent";
  "Specify a Version: … just mention the version in your prompt"; contoh prompt diakhiri "use context7"; mode MCP dengan tool
  `resolve-library-id` dan `query-docs` (dipakai di layar s03); server `https://mcp.context7.com/mcp`; setup `npx ctx7 setup` (opsi
  `--claude`), API key gratis "recommended … for higher rate limits". Disclaimer: dokumentasi di Context7 dikontribusi komunitas, tidak
  dijamin 100% akurat (→ DM). Pembuat **Upstash** juga tercantum sebagai author di marketplace plugin resmi Claude Code.
- **Supabase MCP** — https://github.com/supabase-community/supabase-mcp (README "Supabase MCP Server", LICENSE Apache-2.0, terdaftar
  di MCP Registry sebagai `com.supabase/mcp`); plugin resmi https://github.com/supabase-community/supabase-plugin ("Official Supabase
  plugin for Claude Code, Cursor, …": MCP server `https://mcp.supabase.com/mcp` + skill). Daftar tool & keamanan dari sumber docs resmi
  (supabase/supabase `apps/docs/content/guides/ai-tools/mcp.mdx`, dibaca dari GitHub karena supabase.com diblokir DNS di sandbox ini):
  Database `list_tables`, `list_migrations`, **`apply_migration`**, **`execute_sql`**; Development `generate_typescript_types`.
  docs/production.md: `apply_migration` "tracks any schema or data changes as a migration so that it can be replayed on your production
  branch". Keamanan (dipakai di s07): "Protect production data: Connect to a production project only when the task requires production
  evidence. Use project scoping, read-only mode…", "Most MCP clients ask you to accept each tool call before it runs. Keep manual approval
  enabled … and review each tool call before you run it", opsi `read_only=true` dan `project_ref=…`, branching untuk dev.
- **Vercel** — plugin resmi https://github.com/vercel/vercel-plugin (`.claude-plugin/plugin.json`: name "vercel", author Vercel, license
  Apache-2.0) membawa MCP resmi `https://mcp.vercel.com` (catatan di `.mcp.json`: "Official Vercel MCP server … Supports reads and writes,
  including … deployments") + perintah deploy. `commands/deploy.md`: "Default is preview deployment" (`vercel` → "a preview deployment
  on a unique URL"), production (`vercel --prod`) hanya kalau diminta dan "**Ask the user for explicit confirmation before proceeding**";
  catatan: "If the project has no deployments yet, this deployment goes to production" (→ DM). Perintah MCP manual (WebSearch, beberapa
  sumber; vercel.com diblokir DNS di sandbox ini): `claude mcp add --transport http vercel https://mcp.vercel.com`.
- **Pasang di Claude Code** — keempatnya terdaftar di marketplace resmi Anthropic `claude-plugins-official`
  (https://github.com/anthropics/claude-plugins-official, `.claude-plugin/marketplace.json`: `chrome-devtools-mcp`, `context7`
  (author Upstash), `supabase`, `vercel`); README: "`/plugin install {plugin-name}@claude-plugins-official` or browse … `/plugin >
  Discover`" (+ peringatan: pastikan kamu percaya plugin sebelum memasang). Tidak disebut di VO; ada di DM.
- **Izin perintah di Claude Code** — https://code.claude.com/docs/en/permissions: Claude Code meminta persetujuan sebelum menjalankan
  perintah Bash, mengubah file, dan tool MCP ("Bash, PowerShell, file, and MCP tool prompts", opsi Yes/No) → layar s07 "Izinkan perintah
  ini? · Izinkan / Tolak" (desain generik kita, bukan tangkapan layar).
- Semua data/link/versi di layar adalah contoh: "Toko Kue Rumahan", harga, nama pembeli, `tokokue-k3x9-kamu.vercel.app`,
  `tokokue-kamu.vercel.app`, `"next": "16.x"`, error 500 — berlabel CONTOH/ILUSTRASI. Tidak ada angka bintang, harga paket, atau klaim
  "gratis".

## Naskah (dikirim ke ElevenLabs, voice tersimpan, **tanpa --tags** → auto tag klien)
Tag yang benar-benar dipakai (dari `assets/audio/vo.json`):
[playful] [excited] Kode dari Claude Code itu baru setengah jalan.
[playful] [excited] Biar web pesanan toko kue kamu jadi sampai online, pasang empat alat ini.
[playful] [excited] Satu, Context Seven dari Upstash: sebelum ngoding, Claude ngecek dokumentasi resmi sesuai versi yang kamu pakai.
[playful] [excited] Dua, Supabase MCP: Claude bikin tabel pesanan di database, dan tiap perubahan disimpan sebagai migration.
[playful] [excited] Tiga, Chrome DevTools MCP dari Google: Claude buka webnya di Chrome, nyobain pesan kayak pembeli, lalu ngecek console sama network.
[playful] [excited] Empat, Vercel: Claude deploy ke link preview buat kamu cek, baru production setelah kamu oke.
[playful] [excited] Hati-hati, akses database dan deploy itu nyentuh production. Latihan di project tes, dan baca tiap perintah sebelum kamu izinkan.
[playful] [excited] [confident] Komen alat, aku kirim lewat DM.

Teks tanpa tag: `production/vo_lines.txt` (112 kata, 728 karakter). "Context7" ditulis "Context Seven" supaya diucapkan seperti nama
resminya; caption menampilkan **Context7** (MERGE di `tools/timing.py`). Kata kunci CTA dikirim huruf kecil ("alat") supaya tidak dieja;
caption **ALAT**. Dibuat dengan `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3`
→ **take 1 (satu-satunya), 43,68 dtk file, 8 baris**.
Cek dengar ulang dengan faster-whisper `small` dan `medium` (bahasa id, seluruh take): semua baris lengkap dan berurutan. Medium: semua
kata Indonesia benar ("toko kue kamu", "ngoding", "migration", "konsol sama network", "project test", "Komen alat aku kirim lewat DM").
Small saja: "Toko Kuek kamu", "noding" (medium benar → tidak perlu take ulang). Nama produk ditulis whisper secara fonetik di kedua model:
"Cloud Code" (= Claude Code, sesuai catatan lead), "SuperBase/Super Base" (= Supabase), "Versal" (= Vercel, diucapkan benar "ver-sel"),
"Contact 7" (= Context7). Untuk Context7: potongan 6,9–9,4 dtk diuji lagi — whisper small bahasa id menulis **"kontek 7"** (huruf -s
melebur ke "Seven", ucapan wajar), medium "kontak 7"; ini nama merek yang tidak dikenal model, bukan salah ucap → take tidak diulang
(kredit terbatas; mengganti kata tidak mungkin karena ini nama resmi). Tag tidak ikut terbaca.
