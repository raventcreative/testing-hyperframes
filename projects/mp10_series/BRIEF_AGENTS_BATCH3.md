# MasterPajak AI · videos 16–30 — batch 3 brief

Read first: `BRIEF_AGENTS.md` (brand rules, look, shared ending, tech — all still apply) and `BRIEF_AGENTS_BATCH2.md` (real-renderer
lessons — all still apply). Videos 01–15 are finished and approved. Good references: `mp10_14_data` (newest kit, VO + lip-sync already
wired), `mp10_15_tanya`, `mp10_09_tutupbulan` (3D worlds, whip pans), `mp10_05_omzet` (3D objects + camera), `mp10_10_sebelumsesudah`.
Each new video must have its OWN visual idea (format listed below) — same series, not a copy of an earlier video.

## What is new in batch 3: VO FIRST
The earlier videos were built first and re-timed to the voice later. Here the voice comes first and the film is built on it.
1. Copy the kit: `cp -r` the needed parts of `projects/mp10_14_data/` into your folder (index.html, robot_perf.js, vendor/, tools/,
   assets/ fonts + robot, thumbnail/cover.html) — NOT its `out/`, `production/vo/` or `lipsync.js`. Then replace the content.
2. Write the script: `production/vo/lines.txt`, one VO line per line, Indonesian, "kamu", warm and practical, 28–36 s spoken.
   Line 1 = hook. Always end with the series close as two lines: `Jualan jalan terus, pajaknya AI yang urus.` and
   `Coba kalkulator gratis. Link di bio.` No tax rates, deadlines, penalties, guarantees or invented statistics.
3. Voice (ElevenLabs, client's voice, AUTO TAGS — the client's instruction): 
   `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo/lines.txt production/vo/VO_MPxx.mp3`
   (no --tags: the default "auto" puts [playful] [excited] on every line plus one context tag chosen from the line; it prints the
   tags used and writes VO_MPxx.json with per-line start/end + a character alignment for word times). Listen-check with
   faster-whisper (`small`, numpy input) that every word is spoken and no tag is read aloud; re-generate a line set if not.
4. Put the voice on the timeline: `ffmpeg -y -i production/vo/VO_MPxx.mp3 -af "adelay=300|300,aformat=sample_rates=48000:channel_layouts=mono" assets/audio/vo.wav`
   (speech starts at 0.30 s). Every `window.TM` key = a real word time from the JSON alignment + 0.30. `TM.total` = last word end
   + ~1.6 s (end card hold) and `data-duration` equal to it.
5. Lip-sync for the robot: `python3 tools/lipsync.py assets/audio/vo.wav lipsync.js`. SFX: `python3 tools/sfx.py` (after TM is final).
6. Build every scene on those TM keys (captions are not needed — the series has none; on-screen text must follow what is said).
7. QA with the REAL runtime (`npx --yes hyperframes@0.8.186 snapshot . --at … --no-end --timeout 60000 -o <scratch>` for every scene,
   cut and the end card; `validate` with only lipsync-style 404s allowed). Make the cover: `thumbnail/COVER_MPxx_<NAME>.png` from
   `thumbnail/cover.html` (same series cover style as mp10_14_data).
8. Write `production/NOTES.md` (script with tags used, scene list with times, labels used, known issues).

House rules: Write/Edit for files (no heredocs containing `$$(`), no `rm -rf` (delete single files only), do NOT git commit/push, do NOT
run the full render (the lead renders and mixes music), touch only your own folder + your scratch dir
`/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/mp<xx>/`. Disk is limited: QA as small JPG
contact sheets, delete PNG dumps after. Stop any http.server you start (ports below) before you finish.

## The 15 concepts (fictional sellers/brands only; no marketplace, bank, e-wallet or chat-app logos/names/colours; generic UI;
## every demo number gets "Ilustrasi data", every app flow "Simulasi alur")
- **16 · Dari Chat ke Catatan Rapi** (`mp10_16_chatwa`, 8916): orders arrive as a flood of chat bubbles on a tilted 3D phone ("mau 2 ya
  kak", "jadi transfer ya", "ongkirnya berapa?") — generic chat UI, no app branding. The bubbles peel off the phone and land as rows of
  a tidy order table (tanggal · pesanan · nominal). Brand: the table becomes pembukuan yang bisa ditelusuri.
- **17 · Bukti Transfer Nyelip di Galeri** (`mp10_17_galeri`, 8917): a phone gallery grid (selfies, food, memes as simple illustrated
  tiles) with transfer screenshots and receipt photos hidden among them; frantic scroll. Brand: foto nota diunggah lewat aplikasi →
  sorted into a calm album per tanggal, then into the pembukuan.
- **18 · Stok Itu Uang yang Lagi Diam** (`mp10_18_stok`, 8918): a 3D warehouse shelf; each box flips to show it is money frozen on the
  shelf ("modal nyangkut"). Point: belanja stok is modal, not lost money and not profit — record it so the laporan laba rugi reads right.
- **19 · Jualan di Banyak Tempat, Catatannya Satu** (`mp10_19_multichannel`, 8919): three channels drawn as rivers ("Toko online A",
  "Toko online B", "Media sosial" — generic) that each carry orders, fees and payouts in different shapes, merging into one lake =
  one pembukuan; rekonsiliasi bulanan checks they match.
- **20 · Diskon Gede, Untung Ikut Gede?** (`mp10_20_diskon`, 8920): a quiz-show format (buzzers, A/B answers, studio lights). Question:
  "diskon 30% bikin untung naik?" Reveal with one product: harga, diskon, modal, ongkir → laba per item shrinks (illustrative,
  arithmetic must add up). Brand: laporan laba rugi shows the real effect before you run the promo.
- **21 · Retur Juga Harus Dicatat** (`mp10_21_retur`, 8921): a boomerang / return arrow: a sale is counted, then the parcel comes back
  and the money with it. If the retur isn't recorded, penjualan looks bigger than it is. Brand: rekonsiliasi flags it.
- **22 · Modal Masuk Bukan Penjualan** (`mp10_22_modal`, 8922): a sorting conveyor: incoming money tokens labelled penjualan, pinjaman,
  tambahan modal, uang pribadi get sorted into lanes; a wrong lane inflates omzet (a gauge jumps falsely). Brand: pembukuan that tells
  each kind of money apart.
- **23 · Utang ke Supplier Jangan Cuma di Kepala** (`mp10_23_utang`, 8923): a cartoon head with sticky notes orbiting it ("Supplier
  kain", "Supplier kemasan"…), notes slipping away; a shop counter scene. Brand: the notes land in the pembukuan, nothing forgotten.
- **24 · Laporan Laba Rugi dalam 30 Detik** (`mp10_24_labarugi`, 8924): a recipe-card / cooking format: bahan = penjualan, modal
  barang, biaya (ongkir, iklan, kemasan); langkah = kurangi satu-satu; hasil = laba. Illustrative numbers, arithmetic exact.
- **25 · Kategori Biaya Biar Nggak Campur Aduk** (`mp10_25_kategori`, 8925): a 3D filing cabinet; a pile of mixed receipts sorts into
  drawers (bahan baku, ongkir, iklan, kemasan, operasional) as they're photographed. Brand: unggah foto nota via aplikasi → tanggal,
  kategori, nominal.
- **26 · Reseller & Dropship: Uang Lewat vs Untung** (`mp10_26_dropship`, 8926): a relay race: the customer's payment is the baton;
  most of it is passed on to the supplier, only the margin stays. Omzet vs untung for resellers. Illustrative numbers, exact.
- **27 · Musim Ramai, Catatan Jangan Ikut Kacau** (`mp10_27_musimramai`, 8927): a rush-hour storm of orders (event belanja / musim
  lebaran, no dates), boxes piling up; habit: catat tiap hari sebentar. Brand: pembukuan + asisten AI keep up with the rush.
- **28 · Target Bulan Depan dari Data, Bukan Feeling** (`mp10_28_target`, 8928): archery: a "feeling" arrow misses wildly, a "data"
  arrow (from last month's laporan laba rugi) hits. Point: set targets from what really sold and what it really cost.
- **29 · Hari Pertama Pakai MasterPajak AI** (`mp10_29_haripertama`, 8929): a day timeline (pagi → siang → sore → malam) of a fictional
  seller trying it: unggah foto nota, catatan jualan rapi, sore lihat laporan, malam tanya asisten AI. Everything "Simulasi alur".
- **30 · "Usahamu Untung Berapa?"** (`mp10_30_ditanya`, 8930): an interview scene — a potential partner (calon mitra / pemodal, generic,
  no bank) asks the question; seller A fumbles through scattered notes, seller B shows a clear laporan laba rugi. No promise of
  approval or funding — the point is being able to answer.
