# DM untuk komentar "LLM" — Panduan FreeLLMAPI (Claude Code pakai model gratis)

Halo! Ini yang aku janjiin di reel:

**Repo resmi:** https://github.com/tashfeenahmed/freellmapi (open source, lisensi MIT)
Hati-hati: ada beberapa fork/mirror bernama sama — pakai yang dari **tashfeenahmed**.

## Ingat dulu
- Ini **bukan Claude gratis**. Aplikasinya tetap Claude Code, tapi jawabannya datang dari **model lain** (jatah gratis Google, Groq,
  Mistral, Cerebras, OpenRouter, dll.). Kualitasnya bisa beda dan kadang lebih lemah dari Claude.
- Anthropic **tidak mendukung resmi** pemakaian Claude Code dengan model non-Claude. Ada fitur Claude Code yang bisa saja tidak jalan.
- Jatah gratis tiap penyedia bisa dikurangi, diganti, atau dihapus kapan saja. Jatah harian banyak model reset 00.00 UTC (07.00 WIB).

## 3 langkah
1. **Pasang servernya**
   - Windows / macOS: download app desktop di halaman *Releases* repo, atau
   - Docker: `curl -fsSL https://freellmapi.co/install.sh | bash` (baca dulu isi skripnya sebelum dijalankan).
2. **Isi API key tiap penyedia**
   - Daftar akun di penyedia yang kamu mau (mis. Google AI Studio, Groq, Mistral), buat API key.
   - Buka dashboard `http://localhost:3001` → halaman **Keys** → tempel key-nya → ambil **unified key** kamu.
3. **Satu perintah buat Claude Code**
   - `npx freellmapi setup-claude --url http://localhost:3001 --api-key <unified-key>`
   - (config lama di-backup otomatis; tambah `--dry-run` kalau mau lihat perubahannya dulu)

## Biar aman
- Kode dan prompt kamu **dikirim ke server penyedia**. Baca aturan (Terms of Service) tiap penyedia — ada layanan gratis yang boleh
  memakai data kamu untuk mengembangkan modelnya.
- **Jangan kirim** password, file `.env`, data pelanggan, atau kode rahasia klien. Latihan pakai data contoh.
- Jalankan untuk dirimu sendiri saja — jangan dibuka ke internet atau dibagi ke orang lain.
- Pakai buat **belajar & eksperimen**. Untuk kerjaan klien, pakai API berbayar resmi.

Catatan: FreeLLMAPI juga punya opsi Premium berbayar (update katalog model lebih cepat). Untuk belajar, versi gratisnya sudah bisa dipakai.
Info dicek 12 Nov 2026 dari README resmi — perintah bisa berubah, selalu cek README terbaru.
