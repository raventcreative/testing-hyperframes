# VO — R11 · Agen ngoding open source dari DeepSeek (DeepSeek Harness) · background NAVY · 45,9 dtk VO (video 47,47 dtk)

Referensi: `aip_remake_batch5/refs/ref1.mp4` + `ref1.txt` (44 dtk, ID, merah/hitam + maskot rambut merah, "lo/gue").
CTA keyword: **NGODING**. Suara: Dakocan (`tools/voice_config.json`), tag otomatis klien (tanpa `--tags`).

## ATM: what we changed

**Amati (referensi)**
- Ide berguna: DeepSeek merilis agen ngoding open source (DeepSeek Harness); kerjanya mirip agen ngoding di terminal (baca file,
  tulis kode, jalanin perintah), semua bagiannya plugin, bisa pakai model DeepSeek atau model lokal (Ollama), satu perintah →
  kebuka di browser, masih developer preview → baca catatan keamanan.
- Mekanisme hook: BERITA + REKOR ("GitHub langsung pecah rekor", angka bintang hari pertama / 2 minggu).
- Struktur beat: berita → angka bintang → nama → mirip Claude Code → plugin (model / tool / tampilan) → model murah / lokal, tanpa
  langganan → satu perintah → developer preview → pertanyaan retoris "sanggup bayar AI?" → CTA "Comment harness" + "follow kita".
- Mekanisme CTA: komen kata kunci → link repo + panduan via DM, lalu ajakan follow.

**Tiru (yang dipertahankan, hanya ide umum)**: "ada agen ngoding open source dari DeepSeek, ini cara kerjanya, biayanya, cara mulai,
dan peringatan preview-nya" + mekanisme komen-kata-kunci → DM.

**Modifikasi (wajib)**
1. **Hook sendiri, sudut lain.** Referensi = berita rekor bintang. Kita = sudut PRAKTISI + BIAYA: "Reel ini aku bikin bareng agen AI
   yang nulis kode. Agen kayak gini biasanya langganan, yang ini open source." (Benar: reel ini memang HTML/GSAP yang ditulis agen
   ngoding — Claude Code + HyperFrames, BUKAN DeepSeek Harness; VO tidak mengklaim reel ini dibuat dengan DeepSeek Harness.)
   Tidak ada angka rekor sama sekali (lihat "Klaim yang dibuang").
2. **Struktur + metafora visual sendiri.** Urutan kita: kode → reel (editor + HP mini) → kartu langganan 12 bulan dengan stempel
   TAGIH → badge OPEN SOURCE → kartu repo (deskripsi resmi "Everything is a Plugin.", bintang terverifikasi, MIT) → metafora
   **RANGKA + OTAK**: papan "rangka agen" berisi bagian-bagian plugin yang ASLI dari docs/architecture.md (alat/tools, riwayat sesi,
   loop agen, tampilan web) mengelilingi soket OTAK yang kosong → demo Web UI dengan tugas lokal → tiga "otak" dicolok bergantian ke
   soket dengan blok BIAYA → terminal + browser setup → kartu status + checklist aman → CTA. Tidak ada layout/warna/maskot/kartu/ikon
   referensi (tidak ada kartu Model/Tool/Tampilan ber-ikon otak/kunci-inggris, tidak ada banner kuning "DEVELOPER PREVIEW", tidak ada
   screenshot GitHub, tidak ada logo DeepSeek/paus). Gaya NAVY AI PRENEUR (panel kaca navy, aksen cyan, Poppins, robot + maskot).
3. **Sudut praktisi Freddie (yang benar saja):** "Reel ini aku bikin bareng agen AI yang nulis kode" — reel AI PRENEUR memang dibuat
   sebagai kode oleh agen AI (HyperFrames). Tidak ada hasil/angka pribadi yang dikarang; tidak diklaim Freddie memakai DeepSeek Harness.
4. **Nilai untuk penonton Indonesia yang tidak ada di referensi:**
   - contoh tugas lokal: "Bikinin katalog toko kue + tombol pesan WA" (UMKM), ditandai CONTOH;
   - **langkah yang dilewati referensi**: pasang Node.js ≥ 24.9 dulu, isi API key di Settings → Models, pilih folder workspace;
   - **biaya dibedah jujur**: harness gratis (MIT), yang bayar "otaknya" — DeepSeek per token (potong saldo), Claude/GPT pakai API key
     provider-nya, model lokal di Ollama tanpa tagihan API tapi butuh laptop kuat;
   - **izin**: agen minta izin sebelum aksi tertentu (ditunjukkan sebagai kartu "Izinkan perintah ini?");
   - **cara aman konkret** dari SAFETY.md (bukan cuma "baca catatan keamanan"): VM/container terpisah, backup dulu, cek tiap perintah
     sebelum diizinkan; ditambah "belum diaudit keamanan" + "risiko sendiri".
5. **CTA + penutup sendiri:** "Komen NGODING, aku kirim lewat DM." — DM berisi link repo + checklist aman (bukan "link repo sama
   panduannya"); TIDAK ada "follow kita untuk update lainnya" dan tidak ada pertanyaan retoris "sanggup bayar AI".
- **Cek kata:** tidak ada lebih dari 3 kata berurutan yang sama dengan naskah referensi (dicek otomatis terhadap `ref1.txt` yang
  sudah dinormalisasi: rangkaian terpanjang = 3 kata, "atau model lokal").

## Fakta yang dicek (sumber resmi, dicek 12 Nov 2026)
| Klaim di VO / layar | Bunyi di sumber | Sumber |
|---|---|---|
| Nama "DeepSeek Harness" (`dsh`), dari DeepSeek, open source | "DeepSeek Harness (`dsh`) is an open-source agent harness developed by DeepSeek AI." | github.com/deepseek-ai/deepseek-harness — README.md |
| "Everything is a Plugin." (kartu repo) | Deskripsi repo: "DeepSeek Harness: Everything is a Plugin."; README: "everything-is-a-plugin architecture … powered by Cordis" | halaman repo (About), README.md |
| Lisensi MIT | LICENSE: "MIT License · Copyright (c) 2026 DeepSeek"; README "## License · MIT" | LICENSE, README.md |
| ★ 279 rb+ bintang (layar, "dicek 12 Nov 2026") | Halaman repo 12 Nov 2026: Stars 279.5k (forks 34.4k) | github.com/deepseek-ai/deepseek-harness |
| Bagian-bagiannya plugin: alat (tools), riwayat sesi, loop agen, tampilan web; otak = model | "Every part of the product is a plugin, including the model adapter, the tool registry, the session log, and the agent loop itself, so each is replaceable from configuration." `dsh-web-app` "adds the browser application" | docs/architecture.md |
| Dia baca file, ubah kode, jalanin perintah, minta izin buat aksi penting | "The agent can read and edit workspace files, run commands, delegate work, and maintain a plan. The Web UI asks before operations that require approval under the active permission policy." | docs/user/guide/index.md |
| DeepSeek: bayar per pemakaian (per token, potong saldo) | Halaman harga resmi: harga per 1 juta token; biaya = jumlah token input + output, dipotong dari saldo (top-up / granted) | api-docs.deepseek.com/quick_start/pricing (dibaca lewat cuplikan pencarian; host tidak bisa dibuka langsung dari sesi ini) |
| Isi API key DeepSeek di Settings → Models | "Open **Settings → Models**, enter a DeepSeek API key, and save it." | docs/user/guide/index.md, providers.md |
| Claude atau GPT pakai API key | "pick a provider dsh ships with — the list shows provider ids such as `anthropic`, `openai`, `moonshotai` for Kimi, or `zai` for GLM — enter its API key, and save" | docs/user/guide/providers.md |
| Model lokal di Ollama (gratis, asal laptop kuat) | Harness: "Custom model API … for a relay, a company gateway, a **self-hosted server** … API protocol: OpenAI Chat Completions …". Ollama: OpenAI-compatible endpoint `http://localhost:11434/v1/`; Ollama open source (MIT). "asal laptopnya kuat" = kehati-hatian umum (model lokal butuh RAM/GPU), bukan klaim angka | providers.md; github.com/ollama/ollama — docs/api/openai-compatibility.mdx, README |
| Pasang Node.js terbaru (layar: Node.js ≥ 24.9) | README: "Install `Node.js`, then run: `npx @deepseek-ai/dsh web`"; package.json + npm `@deepseek-ai/dsh`: `"engines": {"node": ">=24.9.0"}` | README.md, package.json, registry.npmjs.org/@deepseek-ai/dsh |
| Satu perintah, browser kebuka: `npx @deepseek-ai/dsh web` → 127.0.0.1:3080 | "The command starts the Web UI at `http://127.0.0.1:3080` by default and opens it in the default browser for a local launch." | README.md |
| Pilih folder | "Click **Choose workspace**, add the project directory … and select it." | docs/user/guide/index.md |
| Masih developer preview; versi baru bisa bikin setelan lama nggak cocok | "DeepSeek Harness is in _developer preview_ and iterating rapidly. **THERE WILL BE COMPATIBILITY-BREAKING CHANGES.**" | README.md |
| Belum diaudit keamanan; risiko sendiri | "It has not undergone a security audit and must not be treated as secure or production-ready." "Use DeepSeek Harness at your own risk." | SAFETY.md |
| VM terpisah, backup dulu, cek tiap perintah sebelum diizinkan | "Prefer a disposable virtual machine, container, or dedicated environment." "Keep backups of files that the project can access." "Review plugins, configuration, and proposed commands before allowing them to run." | SAFETY.md ("Responsible use") |

**Klaim referensi yang DIBUANG / dikoreksi**
- "74.000 bintang di hari pertama, 200.000 cuma dalam 2 minggu" / "pecah rekor": hanya ada di situs pihak ketiga dan angkanya saling
  bertentangan (13 rb / 30 rb / 74.578 di hari pertama; ±197 rb dalam 8 hari / 206 rb dalam 18 hari) — tidak ada di repo/rilis resmi →
  tidak dipakai. Yang ditampilkan hanya jumlah bintang saat ini di halaman repo resmi (279 rb+, tertulis "dicek 12 Nov 2026").
- Referensi menulis web UI di `127.0.0.1:3000`; README resmi: **`127.0.0.1:3080`** (dipakai yang resmi).
- "nggak perlu langganan bulanan" dibuat lebih jujur: harness-nya gratis, model DeepSeek/Claude/GPT tetap bayar per pemakaian; yang
  tanpa tagihan API hanya model lokal (butuh laptop kuat).
- "Mirip Claude Code" tidak dipakai sebagai klaim; kita tunjukkan langsung apa yang didokumentasikan (baca/ubah file, jalankan
  perintah, minta izin).
- Angka di demo: tidak ada. "toko-kue/", "menu.json", "katalog.html", "npm run dev", "sk-••••" = contoh ilustrasi (jendela diberi label
  CONTOH; kartu langganan diberi label "contoh", tanpa harga).

## Naskah (dikirim ke ElevenLabs persis begini — `production/vo_lines.txt`; tanpa `--tags` = tag otomatis klien)
| # | Tag yang dipakai (auto) | Baris |
|---|---|---|
| 1 | [playful] [excited] | Reel ini aku bikin bareng agen AI yang nulis kode. Agen kayak gini biasanya langganan, yang ini open source. |
| 2 | [playful] [excited] | Kenalin, DeepSeek Harness, lisensi M I T. Harness-nya gratis, otaknya kamu yang pilih.  (caption: **MIT.**) |
| 3 | [playful] [excited] | Suruh bikin katalog toko kue: dia ngebaca file, ngubah kode, ngejalanin perintah, dan minta izin buat aksi penting. |
| 4 | [playful] [excited] | Pilihannya: DeepSeek bayar per pemakaian, Claude atau GPT pakai API key, atau model lokal di Ollama, gratis asal laptopnya kuat. |
| 5 | [playful] [excited] | Cara mulai: pasang Node JS terbaru, jalanin satu perintah, browser kebuka. Isi API key, pilih folder, beres.  (caption: **Node.js**) |
| 6 | [playful] [excited] | Catatannya: masih developer preview, belum diaudit keamanan. Pakai VM terpisah, backup dulu, cek tiap perintah sebelum diizinkan. |
| 7 | [playful] [excited] [confident] | Komen NGODING, aku kirim lewat DM. |

Perintah: `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3` (satu panggilan,
45,92 dtk) → `assets/audio/vo.mp3`. Take pertama (49,4 dtk, versi lebih panjang) dibuang supaya tempo lebih rapat; naskah dipangkas
("Contohnya", "dulu", "sendiri", "tanpa tagihan API" dipindah ke layar). Cek pelafalan dengan faster-whisper small: semua baris terbaca
(whisper menulis "DeepSeek" sebagai "DeepSync" dan "Claude" sebagai "cloud" — ejaan whisper, bukan salah ucap; "M I T" terbaca "MIT").
