# Template prompt website 3D — 5 bagian (gratis) · hand-out DM untuk komentar "SITUS"

Ini template kosong yang dibahas di reel: satu prompt untuk landing page dengan objek 3D, dipecah jadi **5 bagian berlabel**.
Isi bagian yang ada di [kurung siku], hapus yang tidak perlu, lalu tempel seluruhnya ke Claude (atau AI lain yang bisa menulis kode).
Hasilnya satu file `index.html`.

## Cara pakai (4 langkah)
1. Copy template di bawah, isi semua [ … ]. Satu kalimat per bagian sudah cukup, yang penting jelas.
2. Tempel ke Claude. Simpan kodenya sebagai `index.html`.
3. Buka lewat server lokal, jangan dobel-klik file-nya (dokumentasi Three.js menyarankan server lokal; wajib kalau pakai file model
   `.glb`). Paling gampang: di folder file itu jalankan `npx serve .` (butuh Node.js) atau `python3 -m http.server`, lalu buka alamat
   yang muncul di browser. Cek juga di HP.
4. Revisi pakai bahasa sehari-hari (contoh di bawah), sampai pas.

---

## TEMPLATE (copy dari sini)

```
Buatkan landing page satu halaman dengan objek 3D untuk [NAMA USAHA], [JENIS USAHA] di [KOTA].
Tujuan halaman: [mis. pengunjung pesan lewat WhatsApp / datang ke toko / daftar].

[1 · OBJEK UTAMA]
Objek 3D yang jadi bintang di tengah layar: [benda apa, bahan, warna, detail penting].
Posisi dan sikapnya: [mis. melayang pelan di tengah, sedikit miring].
(Kalau saya punya file model 3D: muat file [nama-file.glb] pakai GLTFLoader. Kalau tidak: bentuk objeknya dari bentuk sederhana Three.js.)

[2 · SUASANA]
Warna latar: [warna / gradasi]. Cahaya: [hangat/dingin], datang dari [arah, mis. kiri atas].
Bayangan: [lembut di bawah objek / tanpa bayangan]. Kesan keseluruhan: [mis. mewah, segar, ceria].

[3 · GERAKAN]
Saat halaman di-scroll: [mis. objek berputar 360° dan makin dekat ke kamera, lalu mengecil ke pojok].
Saat diam: [mis. objek naik-turun pelan]. Animasi halus, tidak bikin pusing.

[4 · ISI HALAMAN] (urut dari atas ke bawah)
1) Hero: judul besar "[JUDUL]", satu kalimat "[DESKRIPSI]", tombol "[TEKS TOMBOL]".
2) [Produk / layanan]: [jumlah] kartu berisi foto/nama/[harga atau info].
3) Testimoni: [jumlah] kutipan pembeli [isi asli dari klien, jangan dikarang].
4) [Bagian lain: lokasi + jam buka / FAQ / galeri].
5) Tombol "[Pesan via WhatsApp]" ke wa.me/[NOMOR, format 62…], selalu terlihat di HP.

[5 · TEKNIS]
Satu file index.html (CSS dan JavaScript di dalam file).
Three.js dari CDN lewat import map (semua import dari versi dan CDN yang sama). Animasi scroll pakai GSAP + ScrollTrigger dari CDN.
Wajib ringan di HP: pixel ratio maksimal 2, tanpa video besar, gambar dikompres, teks tetap terbaca dan tombol tetap bisa diklik.
Kalau browser tidak mendukung WebGL atau pengguna memilih "kurangi gerakan" (prefers-reduced-motion), tampilkan versi gambar biasa
tanpa animasi 3D.
Pakai gambar placeholder kalau file gambar belum ada. Tulis kodenya lengkap dalam satu blok, lalu jelaskan singkat bagian mana yang
bisa saya ganti (warna, teks, nomor WhatsApp, gambar).
```

---

## Contoh terisi (sama dengan reel · CONTOH, toko parfum lokal fiktif)

```
Buatkan landing page satu halaman dengan objek 3D untuk Parfum Lokal (nama contoh), toko parfum racikan di Bandung.
Tujuan halaman: pengunjung pesan lewat WhatsApp.

[1 · OBJEK UTAMA]
Botol parfum kaca warna amber, tutup hitam, kerah emas tipis, label krem kecil bertuliskan "PARFUM". Melayang pelan di tengah layar.
Bentuk botolnya dari bentuk sederhana Three.js (tidak ada file model).

[2 · SUASANA]
Latar hijau toska gelap bergradasi ke hampir hitam di bawah. Cahaya hangat dari kiri atas, ada pantulan terang di kaca.
Bayangan lembut di bawah botol. Kesan: mewah tapi hangat.

[3 · GERAKAN]
Saat di-scroll, botol berputar 360° dan makin dekat ke kamera. Saat diam, botol naik-turun pelan.

[4 · ISI HALAMAN]
1) Hero: judul "Wangi lokal, nempel seharian.", satu kalimat tentang parfum racikan lokal, tombol "Lihat aroma".
2) Produk: 3 kartu (Senja, Hujan, Kopi), masing-masing nama + ukuran 50 ml + harga [ISI DARI KLIEN].
3) Testimoni: 2 kutipan pembeli [ISI ASLI DARI KLIEN].
4) Lokasi toko + jam buka.
5) Tombol "Pesan via WhatsApp" ke wa.me/62[NOMOR], menempel di bawah layar HP.

[5 · TEKNIS]
(sama seperti template)
```

## Contoh kalimat revisi (bahasa sehari-hari)
- "Judulnya gedein dikit, ya."
- "Botolnya muter lebih pelan, dan jangan terlalu dekat ke kamera."
- "Cahayanya kurang hangat, bikin lebih kuning."
- "Di HP tombol WhatsApp-nya ketutup, naikin sedikit."
- "Di HP saya patah-patah. Kurangi efeknya biar lebih ringan."

## Catatan jujur
- Hasil tiap AI beda-beda, dan biasanya perlu beberapa kali revisi. Prompt ini titik awal, bukan jaminan hasil jadi sekali klik.
- **Maskot / karakter** susah dibuat dari bentuk sederhana. Untuk maskot, siapkan file model 3D (`.glb`/`.gltf`, format yang
  disarankan dokumentasi Three.js) yang memang boleh dipakai (buatan sendiri atau berlisensi jelas).
- Tes di HP kelas menengah/bawah, bukan cuma di laptop. Kalau berat, minta AI mengurangi efek.
- Foto, logo, teks, dan testimoni harus milik klien atau seizin klien. Jangan mengarang testimoni.
- Lisensi: Three.js berlisensi MIT; GSAP (termasuk ScrollTrigger) gratis, juga untuk komersial, dengan lisensi "standard no charge"
  dari GSAP.

## Soal harga (dalam rupiah, tanpa janji)
Tidak ada angka pasti dari kami, dan ini bukan janji penghasilan. Cara menghitungnya:
1. **Jam kerjamu** × tarif per jam yang masuk akal buat kamu (termasuk revisi kecil dan tes di HP).
2. **Jatah revisi**: tulis jelas di penawaran (mis. 2 kali). Revisi di luar itu = biaya tambahan.
3. **Domain + hosting**: biaya berjalan (domain dibayar per tahun). Tulis terpisah, atas nama klien.
4. **Bandingkan** dengan harga jasa website serupa di kotamu (cek 3–5 penyedia), lalu sesuaikan dengan scope dan budget klien.

## Sumber (dicek 13 Nov 2026)
- Three.js — repo resmi github.com/mrdoob/three.js (README "JavaScript 3D library", LICENSE MIT); manual "Installation" (Option 2:
  Import from a CDN, import map; saran pakai server lokal, `npx serve .`) dan "Loading 3D Models" (glTF/.GLB disarankan, GLTFLoader).
- GSAP — repo resmi github.com/greensock/GSAP (README: "GSAP is now 100% FREE … even for commercial use", ScrollTrigger; lisensi
  "Standard 'no charge' license").
- MDN — `prefers-reduced-motion` (mendeteksi pengaturan "kurangi gerakan" di perangkat pengguna).
