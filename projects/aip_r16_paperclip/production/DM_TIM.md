# DM untuk keyword TIM (saran balasan klien — dicek ke README + docs repo Paperclip, 12 Nov 2026)

Ini paketnya 🙌

**1. Repo resmi (open source, MIT, gratis):** https://github.com/paperclipai/paperclip

**2. Cara pasang (di komputer kamu sendiri):**
- Pasang Node.js versi 24.11 ke atas.
- Jalankan: `npx paperclipai onboard --yes`
- Buka dashboard di browser: http://localhost:3100 (database-nya ikut terpasang otomatis, tanpa akun Paperclip).
- Siapkan akun AI untuk agent-nya: login langganan Claude / ChatGPT (Codex) atau API key (mis. Anthropic / OpenAI).

**3. Contoh struktur tim UMKM (contoh: toko keripik online):**
- Tujuan perusahaan: "Tembus 100 pesanan online per minggu."
- CEO (Claude Code): nyusun strategi → kamu setujui dulu.
- Tim Web: bikin / rapikan toko online + tombol pesan.
- Tim Konten: caption & jadwal posting 7 hari.
- Tim Riset: cek harga dan promo pesaing.
- (Nanti, kalau perlu) Agent Desain: CEO yang ngajuin, kamu yang approve.

**4. Biar aman & hemat:**
- Paperclip-nya gratis, tapi tiap agent pakai token dari API / langganan AI kamu → ada biayanya.
- Mulai kecil: 2–3 agent dulu, kasih budget bulanan kecil per agent. Paperclip kasih peringatan di 80% dan otomatis menjeda agent di 100%
  (catatan resmi: pencatatan biaya bisa sedikit terlambat, jadi tetap pantau).
- Agent tidak nyala 24 jam: mereka "bangun" kalau ada tugas, jadwal, atau mention.
- Kamu tetap pengawas: setujui strategi & rekrut, cek hasil kerja, jeda kapan saja.
- Telemetri anonim Paperclip aktif secara default; bisa dimatikan dengan `PAPERCLIP_TELEMETRY_DISABLED=1`.
