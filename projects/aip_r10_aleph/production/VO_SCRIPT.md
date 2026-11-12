# VO — Edit video yang sudah ada pakai AI (Runway Aleph) · background TERANG · 34,3 dtk VO (video 35,83 dtk)
Referensi: ref5 (22 dtk) — footage asli seorang pria di taman (atas "AI Video", bawah "Raw"): siang → malam, ganti musim (sakura),
tambah mobil / produk; teks: "teknologi baru ini bikin gampang ganti apa pun di video … malam … ganti musim … berguna buat konten
dan marketing … aku bikin ini pakai Runway Aleph, komen buat link, diskon 50%".

## Yang diubah dari referensi
- Tidak ada footage Freddie, jadi versi ANIMASI: semua demo before/after adalah ilustrasi kita sendiri (HTML/CSS/GSAP: taman,
  jalan ruko, rak dinding) dengan label **ILUSTRASI** di setiap player, dan pembatas geser **VIDEO ASLI | HASIL EDIT AI** (bukan
  layout atas/bawah referensi). Klipnya "hidup" (kamera bergerak pelan, parallax, awan, orang bergoyang/melambai/berjalan).
- 22 dtk → 35,8 dtk: hook → 4 demo (siang→malam, panas→sakura→salju, kerb kosong→mobil, rak polos→produk) → cara kerja 3 langkah
  → kegunaan (konten & marketing, 1 video → banyak versi) → catatan paket berbayar → CTA.
- Klaim diskon/afiliasi referensi ("50% off") dibuang. Ditambah catatan jujur: Aleph 2.0 ada di paket berbayar Runway.
- Prompt di layar sengaja berbahasa Inggris ("Make it night", "Change the season to winter", …) mengikuti pola panduan prompt
  Runway (kata kerja + hasil); dukungan prompt berbahasa Indonesia TIDAK kami klaim.
- "Runway Aleph" hanya ditulis sebagai teks (tanpa logo Runway). Merek "PRODUKMU" di rak = fiktif. Tidak ada angka harga di layar.
- "bagian lainnya dibiarin kayak aslinya" = perilaku yang dideskripsikan Runway sendiri (edit sesuai prompt, sisanya dipertahankan);
  kami tidak menjanjikan hasil sempurna.
- CTA: "Komen AI, aku kirim cara pakainya." (paket DM: langkah + contoh prompt).

## Fakta yang dicek (2026-11-12)
Halaman resmi (runway.com, runwayml.com, help.runwayml.com) DNS-blocked dari sandbox, jadi diverifikasi lewat hasil WebSearch yang
dibatasi ke domain resmi tsb (judul + cuplikan halaman) + listing Runway di Replicate:
- **Aleph = model edit video dari Runway** ("in-context video editing model"): kasih video + kalimat, model membuat edit yang
  diminta dan mempertahankan yang tidak diminta. Bisa untuk footage asli (bukan cuma video AI).
  Sumber: https://runway.com/product/aleph-2 · https://runway.com/product/ai-video-editor (FAQ) · https://replicate.com/runwayml/aleph-2
- **Aleph (2025)**: tambah / hapus / ubah objek, sudut kamera baru, ubah style dan pencahayaan.
  Sumber: https://runway.com/research/introducing-runway-aleph
- **Aleph 2.0 + Edit Studio (21 Mei 2026)**: ganti waktu (time of day) / relight, ganti musim (contoh prompt resmi "Change the season
  to winter"), hapus objek, ganti varian produk, ganti background; edit satu frame lalu dibawa ke seluruh klip.
  Sumber: https://runway.com/news/introducing-aleph-2-and-edit-studio
- **Ketersediaan**: "available now on all paid Runway plans" (desktop web app) → di VO: "ada di paket berbayar Runway".
  Sumber: https://runway.com/news/introducing-aleph-2-and-edit-studio · https://runway.com/pricing
- **Biaya**: pakai kredit, dihitung per detik video (Aleph 2.0: 28 kredit/detik, minimum 56; input 2–30 dtk, 480p–1080p) → di layar
  hanya "Pakai kredit, dihitung per detik video" + "Dicek 12 Nov 2026 · harga & kuota bisa berubah" (tanpa angka).
  Sumber: https://help.runwayml.com/hc/en-us/articles/51683104370451-Creating-with-Edit-Studio
- **Pola prompt**: kata kerja (add, remove, change, replace, re-light) + deskripsi hasil.
  Sumber: https://help.runwayml.com/hc/en-us/articles/52150503729171-Aleph-2-0-Prompting-Guide
- Tambah mobil / taruh produk = kategori "add objects" (Aleph) + use case produk (Aleph 2.0); di reel hanya sebagai ILUSTRASI.

## Naskah (dikirim ke ElevenLabs, voice tersimpan; SETIAP baris diawali tag `[playful] [excited]`)
[playful] [excited] Video yang udah kamu rekam, sekarang bisa kamu ubah cuma pakai satu kalimat.
[playful] [excited] Mau siang jadi malam? Tinggal ketik.
[playful] [excited] Mau ganti musim? Dari musim panas, jadi sakura, atau salju.
[playful] [excited] Pinggir jalan yang kosong, bisa ditambahin mobil.
[playful] [excited] Rak yang polos, bisa diisi produk kamu.
[playful] [excited] Namanya Runway Aleph. Kamu kasih videonya, tulis mau diubah apa, bagian lainnya dibiarin kayak aslinya.
[playful] [excited] Cocok banget buat konten dan marketing: satu video, banyak versi, tanpa syuting ulang.
[playful] [excited] Catatan: fitur ini ada di paket berbayar Runway.
[playful] [excited] Komen AI, aku kirim cara pakainya.

Teks tanpa tag: `production/vo_lines.txt`. Audio: `assets/audio/vo.mp3` (+ `assets/audio/vo.json` = waktu per baris + alignment
karakter). Dibuat dengan `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3
--tags "[playful] [excited]"`. Cek ulang dengan faster-whisper `small`: semua kata terucap ("Runway Aleph" terbaca jelas), tag tidak
ikut terbaca.
