# VO — Claude Code pakai model AI gratis (FreeLLMAPI) · background TERANG · 43,4 dtk VO (video 45,30 dtk)
Referensi: batch 5 · ref10 (28 dtk, reel bahasa Inggris, kreator lain, latar gelap → terang): "You can now run Claude Code for free with
unlimited usage" → "7 billion free AI tokens … renew every month" → token dari ChatGPT, Gemini, Grok, Kimi, Qwen → "It's called FreeLLMAPI"
→ server kecil yang "speaks the same language as Claude's API", Claude Code "thinks it's talking to Claude" tapi permintaan dioper ke
"pool of free models" → "setup takes about two minutes" → CTA komen kata kunci, dikirim ke DM. Visual referensi: logo Claude oranye +
"$100/mo" dicoret "FREE", simbol tak terhingga "UNLIMITED", orbit logo di sekitar logo GitHub, penghitung token raksasa, grid "Models in the
pool", kartu repo GitHub, diagram vertikal 3 kartu (Claude Code → FreeLLMAPI server → Pool of free models), terminal + timer "1:27 setup
time", kartu profil + komentar.

## ATM: what we changed
**Amati** — ide yang berguna: ada proyek open source yang bikin aplikasi Claude Code bisa jalan pakai jatah gratis model dari penyedia
lain. Mekanisme hook: janji besar ("free", "unlimited", "7 billion tokens") + logo produk yang dikenal. Struktur: klaim → angka token →
daftar model → nama alat → cara kerja (server penerjemah → pool model) → "setup 2 menit" → CTA kata kunci ke DM.
**Tiru** — hanya ide + mekanismenya: sebut nama alatnya, jelaskan cara kerjanya (server lokal yang paham format API Claude, lalu oper ke
model gratis), tunjukkan langkah pasang, tutup dengan CTA kata kunci.
**Modifikasi** (wajib):
1. **Hook sendiri, sudut beda** — "Pengen belajar Claude Code, tapi belum sanggup langganan?": sudut pelajar/dev/UMKM Indonesia yang
   belum sanggup bayar langganan — bukan janji "gratis tanpa batas". Kalimat kedua langsung jujur: "Ada jalan tengahnya".
2. **Struktur, urutan, dan metafora visual sendiri** — urutan kita: masalah (paywall + dompet tipis) → jalan tengah (server kecil di
   ujung "jalan tengah") → jalan di laptop & paham format API Claude (gelembung permintaan + amplop ke kotak server) → dioper ke **"Sisa
   jatah gratis"** (metafora kita: cek sisa kuota seperti di HP, bukan grid logo model) → **badan vs otak** (aplikasi = Claude Code, otak =
   model lain, cap "BUKAN CLAUDE") → jatah habis → pindah otomatis → 3 kartu langkah pasang dengan perintah asli → **catatan jujur**
   (kualitas ≠ Claude, limit bisa berubah, reset 07.00 WIB) → **datamu ikut terkirim** (alur file + kartu ToS + kaca pembesar + chip
   merah "jangan kirim") → kartu "Belajar ✓ / Kerjaan klien ✗" → CTA. Semua dalam gaya LIGHT AI PRENEUR (latar putih–biru + grid animasi,
   kartu putih, teks gradasi navy, Poppins), maskot + robot kita. **Tidak ada** logo Claude/Anthropic, logo GitHub, logo penyedia, harga
   "$100/mo", simbol infinity, penghitung token, grid model, diagram 3 kartu vertikal, timer setup, atau kartu profil referensi.
3. **Sudut praktisi yang benar** — reel ini sendiri dikerjakan di Claude Code (pakai model Claude, bukan FreeLLMAPI). Karena itu VO tidak
   mengklaim "aku pakai ini"; yang kita bawa adalah kebiasaan praktisi: cek aturan penyedia, jangan kirim data sensitif, latihan pakai data
   contoh. Tidak ada klaim hasil atau angka pribadi.
4. **Nilai untuk penonton Indonesia** — sudut pelajar/mahasiswa/UMKM yang belum sanggup langganan; jam reset jatah harian dikonversi ke
   **07.00 WIB** (README: reset 00.00 UTC); kejujuran yang dilewati referensi: **ini bukan Claude gratis** (otaknya model lain), Anthropic
   tidak mendukung resmi pemakaian Claude Code dengan model non-Claude, kualitas bisa lebih lemah, jatah bisa dikurangi/dihapus, **kode
   & prompt ikut dikirim ke server penyedia** (contoh: syarat Gemini API untuk pemakaian gratis membolehkan data dipakai buat
   mengembangkan model), jangan kirim `.env`/password/data pelanggan/kode klien, dan **pakai untuk belajar — kerjaan klien pakai API berbayar
   resmi** (sesuai disclaimer README). Langkah yang referensi lewati: daftar & isi API key di tiap penyedia.
5. **CTA dan penutup sendiri** — "Pakai buat belajar dulu, bukan buat kerjaan klien." + "Komen LLM, aku kirim lewat DM." Tanpa "follow".
   Isi DM: `production/DM_LLM.md` (link repo, 3 langkah, catatan aman).
- **Dibuang:** "for free with unlimited usage", "7 billion free AI tokens … every single month" (README sekarang menyebut ±7,4 miliar token
  per bulan sebagai *kapasitas free tier yang terdaftar*, bukan jaminan — angka ini tidak kita pakai sama sekali), "ChatGPT, Grok, Kimi, Qwen"
  sebagai daftar model (kita sebut penyedia yang memang ada di tabel README: Google, Groq, Mistral, + Cerebras, OpenRouter, dll.), "Claude
  Code thinks it's talking to Claude" (diganti penjelasan jujur badan/otak), "setup takes about two minutes" / timer 1:27 (tidak bisa
  diverifikasi; diganti 3 langkah asli), angka bintang/fork repo (berubah tiap hari; referensi 38,1k — sekarang sudah lain).
- **Aturan 3 kata:** referensinya berbahasa Inggris, naskah kita berbahasa Indonesia; kesamaan hanya nama produk ("Claude Code",
  "FreeLLMAPI") dan "DM" di CTA wajib — tidak ada 3 kata berurutan yang sama.

## Fakta yang dicek (2026-11-12, sumber resmi)
- **Nama & repo (dibaca dari frame referensi: "FreeLLMAPI", kartu repo "freellmapi", perintah `npx freellmapi setup-claude`)** —
  https://github.com/tashfeenahmed/freellmapi (README + LICENSE dibaca langsung dari raw.githubusercontent.com). README: "Aggregate free
  tiers from dozens of providers … behind a single `/v1` API. Keys are stored encrypted. A router picks the best available model for each
  request, falls over to the next provider when one is rate-limited, and tracks per-key usage so you stay under every free-tier cap."
  Fork/mirror bernama sama ada (S40014/…, vi70x4/… "airiOS", Gitee) — yang dirujuk adalah repo asli tashfeenahmed.
- **Lisensi** — LICENSE: **MIT** (Copyright (c) 2026 Tashfeen Ahmed). README: router "stays MIT-licensed and fully free"; ada opsi
  **Premium** berbayar ($19/tahun atau $49 sekali) hanya untuk feed katalog model *live* — versi gratis memakai snapshot bulanan. (Tidak
  disebut di VO; dicatat di DM.)
- **Paket npm** — https://registry.npmjs.org/freellmapi: `freellmapi` 0.8.2 (20 Okt 2026), MIT, "Set up coding agents to use a
  FreeLLMAPI gateway", repo tashfeenahmed/freellmapi (folder `cli`).
- **Cara kerja / format API Claude** — README Features: "`/v1/messages` speaks Anthropic's wire format over the same router, so Claude
  Code and the official Anthropic SDKs run against your free pool." docs/en/api/01-rest-api.md: nama model Claude (opus/sonnet/haiku)
  dipetakan ke model di pool gratis ("routes to auto (the router picks a free model) or a model you pin"); juga OpenAI-compatible
  (`/v1/chat/completions`, dll.) → chip "Juga paham format OpenAI". Port default **3001** (`http://localhost:3001`).
- **Penyedia** — tabel README: Google, Groq, Cerebras, OpenCode Zen, Mistral, OpenRouter, Cloudflare, Cohere, Z.ai (Zhipu), NVIDIA,
  HuggingFace, ModelScope "… and 22 more free providers" + provider custom (Ollama/LM Studio/vLLM). VO menyebut Google, Groq, Mistral;
  layar menambah Cerebras, OpenRouter.
- **Failover** — README "How it works": "on a 429/5xx it cools that key down and retries the next model in your chain".
- **Langkah pasang** — README Quick start: `curl -fsSL https://freellmapi.co/install.sh | bash` ("Docker required"), atau app desktop
  (.exe Windows / .dmg macOS di Releases); buka http://localhost:3001, isi provider keys di halaman **Keys**, ambil unified key;
  `npx freellmapi setup-claude --url http://localhost:3001 --api-key <unified-key>` ("backs up the existing config and merges into it").
  Alternatif manual (docs/en/api/01-rest-api.md): `ANTHROPIC_BASE_URL=http://localhost:3001` + `ANTHROPIC_AUTH_TOKEN=<key>` (bukan
  `ANTHROPIC_API_KEY`).
- **Keterbatasan (jujur)** — README Limitations + docs/en/architecture/00-high-level-index.md: "no SLA", latency bervariasi, "Intelligence
  degrades as the day progresses … reset at UTC midnight" (= 07.00 WIB), "Free tiers can change without notice … tighten, loosen, or
  remove", "Local-first … don't expose it to the internet".
- **Disclaimer & ToS** — README Disclaimer: "for personal experimentation and learning, not production … If you build something real on
  top of FreeLLMAPI, swap in a paid API before you ship. … those terms still apply when the traffic is proxied through this project, and
  you're responsible for complying with them." Review ToS per penyedia di architecture doc (mis. Cohere ❌ untuk pemakaian pribadi, NVIDIA
  "evaluation only", Google ⚠️) → dicatat di DM.
- **Data ke server penyedia** — README: "requests go from your machine to the upstream providers you enabled". Contoh syarat: Gemini API
  Additional Terms (versi arsip 2025, mis. ai.google.dev/gemini-api/terms-archive/terms_11_20_25, terbaca lewat WebSearch; ai.google.dev
  diblokir DNS di sandbox ini): untuk layanan tanpa bayar, Google memakai konten yang dikirim & respons untuk mengembangkan produk dan
  teknologi machine learning, bisa dibaca reviewer manusia, dan meminta jangan mengirim info sensitif/rahasia/pribadi → baris layar
  "Layanan gratis: data bisa dipakai buat melatih model*" + "*contoh: syarat Gemini API (Google) untuk pemakaian gratis".
- **Posisi Anthropic** — https://code.claude.com/docs/en/llm-gateway: "Anthropic doesn't endorse, maintain, or audit third-party gateway
  products, and doesn't support routing Claude Code to non-Claude models through any gateway." → catatan kecil di s05.
- **Claude Code biasanya berbayar** — https://support.claude.com/en/articles/11145838 (Claude Code dengan paket Pro, Max, atau Ultra;
  alternatif: akun Console + kredit API) → kartu paywall s01 "paket langganan Claude atau kredit API" (tanpa harga).
- Tidak ada angka token, harga, jumlah bintang, atau "unlimited" di VO maupun layar. Bar "Sisa jatah gratis" berlabel ILUSTRASI.

## Naskah (dikirim ke ElevenLabs, voice tersimpan, **tanpa --tags** → auto tag klien)
Tag yang benar-benar dipakai (dari `assets/audio/vo.json`):
[playful] [excited] [curious] Pengen belajar Claude Code, tapi belum sanggup langganan?
[playful] [excited] Ada jalan tengahnya: Free LLM API, server kecil gratis di GitHub.
[playful] [excited] Dia jalan di laptopmu, ngerti format API Claude.
[playful] [excited] Perintah Claude Code dioper ke jatah gratis model dari Google, Groq, Mistral, dan lainnya.
[playful] [excited] Jadi aplikasinya Claude Code, tapi otaknya bukan Claude.
[playful] [excited] Jatah satu habis, otomatis pindah ke yang lain.
[playful] [excited] Pasang servernya, isi API key gratis dari tiap layanan, lalu satu perintah setup.
[playful] [excited] Jujur ya: kualitasnya beda dari Claude, limit gratisnya juga bisa berubah.
[playful] [excited] Kodemu ikut dikirim ke server penyedia, jadi baca aturannya dan jangan kirim data sensitif.
[playful] [excited] Pakai buat belajar dulu, bukan buat kerjaan klien.
[playful] [excited] [confident] Komen LLM, aku kirim lewat DM.

Teks tanpa tag: `production/vo_lines.txt` (109 kata). "FreeLLMAPI" ditulis "Free LLM API" supaya dieja jelas; caption menampilkan
**FreeLLMAPI** (MERGE di `tools/timing.py`). Kata "rahasia" sengaja tidak dipakai di VO (auto tag klien akan memberi [whispers]) →
"data sensitif". Dibuat dengan `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3`
→ **take 3, 43,68 dtk, 11 baris**. Riwayat baris 7: take 1 "isi API key tiap penyedia" (whisper small: "API Kitia penyebiah"),
take 2 "isi API key dari tiap penyedia" (small + medium: "penyebiah/penyebiyah") → atas permintaan lead, take 3 memakai **"isi API key
gratis dari tiap layanan"** (kata "penyedia" dihindari di baris ini; baris 9 "server penyedia" terdengar bersih dan tetap).
Cek dengar ulang take 3 dengan faster-whisper `small` (bahasa id) di seluruh take + `small` dan `medium` di potongan baris 7: baris 7
terdengar persis **"Pasang servernya, isi API key gratis dari tiap layanan, lalu satu perintah setup."** di kedua model; semua baris lain
lengkap; **"LLM" diucapkan per huruf (el-el-em)** — whisper menulis "Free LLM API" dan "Komen LLM"; whisper menulis "Cloud Code" untuk
"Claude Code" dan "Grog" untuk "Groq" (pengucapan bahasa Inggris yang benar). Tag tidak ikut terbaca.
Pengen belajar Claude Code, tapi belum sanggup langganan?
Ada jalan tengahnya: Free LLM API, server kecil gratis di GitHub.
Dia jalan di laptopmu, ngerti format API Claude.
Perintah Claude Code dioper ke jatah gratis model dari Google, Groq, Mistral, dan lainnya.
Jadi aplikasinya Claude Code, tapi otaknya bukan Claude.
Jatah satu habis, otomatis pindah ke yang lain.
Pasang servernya, isi API key gratis dari tiap layanan, lalu satu perintah setup.
Jujur ya: kualitasnya beda dari Claude, limit gratisnya juga bisa berubah.
Kodemu ikut dikirim ke server penyedia, jadi baca aturannya dan jangan kirim data sensitif.
Pakai buat belajar dulu, bukan buat kerjaan klien.
Komen LLM, aku kirim lewat DM.
