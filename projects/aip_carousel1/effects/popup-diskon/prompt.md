Bikin pop-up diskon pembeli pertama yang muncul halus (latar meredup dan blur) di landing page toko bunga. Satu file HTML, pakai HTML + CSS + GSAP 3 (dari cdnjs), font Poppins, semua teks Bahasa Indonesia.

Tampilan halaman (lebar sekitar 930 px, latar putih dengan semburat pink muda):
- Navbar: logo bulat pink dengan ikon bunga + "Bunga Kirana", menu "Buket  Papan-bunga  Kontak", ikon tas belanja.
- Hero kiri: label "FLORIST · DIANTAR HARI INI" (ikon truk), judul "Buket segar," / "sampai hari ini juga." (baris kedua pink tua), paragraf "Pesan sebelum jam 14.00, diantar ke seluruh Kota Malang.", "mulai Rp 175.000", tombol pink "Pesan buket" dan tombol garis "Lihat katalog". Hero kanan: foto buket sudut membulat 28 px (pakai kotak gradien pink sebagai pengganti foto).
- Lapisan gelap di atas halaman: rgba(40,12,24,.46).
- Pop-up (580 x 344 px, putih, sudut 26 px, bayangan besar): kiri strip foto 196 px; kanan: tombol × bulat, "KHUSUS PEMBELI BARU", "Diskon 15%" (besar, pink tua), "untuk pesanan pertamamu", "Tulis nomor WhatsApp-mu, kode diskonnya langsung kami kirim.", kolom input dengan ikon telepon dan placeholder "Nomor WhatsApp", tombol pink "Kirim kode diskon" (ikon kirim), dan link kecil "Nggak dulu, makasih".
- Toast hijau di atas halaman (awalnya tersembunyi): "✓ Kode KIRANA15 sudah dikirim ke WhatsApp-mu".

Animasi (satu timeline GSAP, repeat: -1, total 6 detik, semua otomatis seperti demo):
1. 0,45 dtk: lapisan gelap muncul (0,45 dtk) dan halaman di belakangnya blur 0 → 3 px.
2. 0,6 dtk: pop-up naik 46 px sambil membesar 0,94 → 1 dan muncul (0,6 dtk, power3.out).
3. 1,4–2,2 dtk: nomor "0812 3456 7890" terketik huruf per huruf (placeholder hilang, ada kursor).
4. 2,55 dtk: tombol ditekan (riak + memantul), lalu berubah hijau "✓ Kode terkirim ke WhatsApp".
5. 3,85 dtk: pop-up turun 24 px dan hilang; 4,0 dtk lapisan gelap dan blur hilang. 4,25 dtk toast hijau turun masuk dari atas (back.out), 5,3 dtk hilang.
6. Input dan tombol di-reset saat pop-up sudah tertutup. Detik 6 sama dengan detik 0, jadi loop-nya mulus.
Catatan: di web asli, tampilkan pop-up ini sekali saja per pengunjung (simpan tanda di localStorage) dan biarkan tombol × / "Nggak dulu" menutupnya.
