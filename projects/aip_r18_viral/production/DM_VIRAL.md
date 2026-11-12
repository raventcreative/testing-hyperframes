# DM untuk yang komen VIRAL — cara pasang Virality Predictor + checklist hook 15 detik pertama
(dicek 12 Nov 2026 di repo GitHub resmi Higgsfield; cara pasang dan biaya bisa berubah, cek lagi halaman resminya sebelum dipakai)

Halo! Ini yang aku janjiin. Anggap ini gladi resik: kamu tes dulu reels-nya, baru posting.

## 1. Pasang di Claude Code (sekali saja)
1. Buka Claude Code, ketik:
   `/plugin marketplace add higgsfield-ai/skills`
   `/plugin install higgsfield@higgsfield`
   (plugin resmi dari Higgsfield AI, gratis, lisensi MIT: https://github.com/higgsfield-ai/skills)
2. Plugin ini memakai Higgsfield CLI (dipasang otomatis kalau belum ada) dan butuh **akun Higgsfield**. Kalau diminta login, jalankan
   `higgsfield auth login` di terminal.
3. Biaya: plugin-nya gratis; analisisnya jalan di server Higgsfield pakai akunmu. Waktu rilis, Higgsfield bilang fitur ini masih preview
   eksperimental dan tidak memotong kredit — cek lagi di akunmu sebelum dipakai rutin.

## 2. Tes reels kamu
- Simpan **15 detik pertama** reels-mu (batas klipnya maksimal 15 detik — dan memang di situ hook-nya).
- Di Claude Code tulis misalnya: "Analisa video ini pakai Virality Predictor: ./reels-sambal-15dtk.mp4"
  (atau di terminal: `higgsfield generate create brain_activity --video ./reels-sambal-15dtk.mp4 --wait`).
- Hasilnya: skor keseluruhan, **detik puncak hook**, skor bertahan (hold/sustain), wilayah respons terkuat/terlemah, plus link laporan visual.

## 3. Checklist baca hasil + perbaiki
- [ ] Puncak hook di detik 1–2? Kalau baru di detik 4–5, intro-mu kelamaan.
- [ ] Pindahkan kalimat/visual terkuat ke detik pertama (hasil, harga, sebelum–sesudah, pertanyaan yang bikin penasaran).
- [ ] Buang basa-basi: "halo semuanya, jadi gini…", intro logo, jeda kosong.
- [ ] Teks di layar terbaca di 1 detik? Suara langsung masuk, bukan musik kosong?
- [ ] Hold rate rendah atau "pikiran melayang" tinggi? Potong bagian yang bertele-tele, lalu **tes ulang**.
- [ ] Buat UMKM: bikin 2 versi pembuka (A/B), tes dua-duanya, baru versi yang lebih kuat yang kamu boost pakai iklan.

## 4. Yang perlu diingat
- Ini **prediksi** dari model AI, bukan jaminan viral dan bukan scan otak penontonmu. Penentunya tetap penonton asli: setelah posting,
  bandingkan dengan Insight (berapa yang nonton sampai habis, disimpan, dibagikan).
- Videomu diunggah ke server Higgsfield. Jangan unggah video klien/produk yang belum boleh dipublikasikan tanpa izin.
- Kadang hook yang "aneh" justru jalan di audiensmu — pakai skor sebagai bahan diskusi, bukan hakim.
