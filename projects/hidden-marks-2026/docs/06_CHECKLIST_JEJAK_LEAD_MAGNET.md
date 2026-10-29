# JEJAK — Checklist Memeriksa Penanda AI di File

**AIpreneur Academy · Free Resource**

Lihat file yang dihasilkan alat AI? Ini cara sederhana memeriksa informasi asalnya tanpa menyimpulkan hal yang tidak terbukti.

## 1. Siapkan file asli

- [ ] Simpan file yang pertama kali diunduh dari tool pembuatnya.
- [ ] Buat salinan untuk eksperimen atau pengeditan.
- [ ] Jangan dulu mengambil screenshot atau konversi format jika ingin memeriksa metadata asli; perubahan format bisa memengaruhi penanda yang dapat ditemukan.
- [ ] Hindari mengunggah file rahasia, pribadi atau milik klien ke situs yang tidak tepercaya.

## 2. Kenali dua jenis jejak

| Jenis | Analogi mudah | Artinya |
| --- | --- | --- |
| **Metadata / C2PA** | Kartu identitas yang ikut bersama file | Informasi yang melekat pada file; pada beberapa file didukung bisa berupa kredensial asal bertanda tangan digital |
| **Watermark dalam konten** | Pola yang menjadi bagian dari gambar, audio atau teks | Sinyal yang tidak otomatis hilang hanya karena metadata file dibuang |

Karakter tak terlihat dalam teks **belum tentu** watermark AI; jangan menganggap setiap karakter Unicode aneh sebagai bukti bahwa sebuah teks dibuat AI.

## 3. Gunakan alat resmi sesuai sumber dan jenis file

### Jika konten berasal dari Claude

- [ ] Buka **Claude Content Checker**: https://claude.com/check-files
- [ ] Pilih file yang **didukung** untuk memeriksa Content Credentials terkait Claude.
- [ ] Pahami: alat pemeriksa file ini **bukan detektor publik untuk seluruh watermark teks Claude**.

### Jika konten berupa gambar/audio OpenAI yang didukung

- [ ] Buka **OpenAI Verify**: https://openai.com/research/verify/
- [ ] Unggah satu gambar atau audio yang didukung; periksa apakah ada sinyal provenance yang dikenali seperti C2PA/SynthID.
- [ ] Pahami: pemeriksaan ini **bukan alat yang bisa membuktikan siapa penulis semua teks**.

## 4. Catat hasilnya secara bertanggung jawab

- [ ] **Terdeteksi**: ada sinyal yang didukung dan dikenali alat. Ini tidak otomatis mengungkap keseluruhan proses edit setelahnya.
- [ ] **Tidak terdeteksi**: alat tidak menemukan sinyal yang didukung. **Bukan bukti** konten dibuat manusia atau tidak pernah dibantu AI.
- [ ] **Tidak didukung / gagal diperiksa**: jenis file, model, atau kondisi file tidak sesuai dengan alat; jangan tarik kesimpulan.

## 5. Kalau ingin membagikan file ke publik/klien

- [ ] Tinjau metadata yang bersifat pribadi atau rahasia secara terpisah dari penanda provenance.
- [ ] Pertahankan informasi asal konten bila relevan, terutama untuk karya, berita, atau materi klien.
- [ ] Jika output dibantu AI, jelaskan kontribusi AI dengan jujur sesuai kebutuhan dan aturan yang berlaku.
- [ ] Jangan menjanjikan “watermark pasti hilang” setelah menghapus metadata. Keduanya bukan hal yang sama.

**Kesimpulan:** Pemeriksaan yang baik mencari bukti asal file dan memahami keterbatasannya. Tidak ditemukannya tanda bukan sertifikat bahwa konten dibuat tanpa AI.

### Sumber resmi

1. Anthropic — How Claude marks AI-generated content: https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
2. Claude Content Checker: https://claude.com/check-files
3. OpenAI — Verify OpenAI-generated content: https://openai.com/research/verify/
4. OpenAI — Provenance signals: https://help.openai.com/en/articles/8912793-provenance-signals-in-openai-generated-content

*Tanggal penyusunan: 29 Oktober 2026. Dukungan model, format dan pemeriksaan dapat berubah; cek kembali dokumentasi resmi saat menggunakan.*
