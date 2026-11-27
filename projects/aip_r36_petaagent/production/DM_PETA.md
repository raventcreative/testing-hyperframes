# PETA AI AGENT untuk jalanin bisnis — 7 departemen · 30 agent
*(dikirim lewat DM ke yang komen **PETA** · AI PRENEUR)*

Ini peta yang ada di video, versi lengkap. Bukan produk jadi — ini **cetak biru**: daftar agent, satu tugas per agent, dan alur
kerjanya, supaya kamu bisa pasang satu per satu di bisnismu (mulai dari yang paling makan waktu).

## Cara baca peta ini
1. **Input** = alat yang sudah kamu pakai tiap hari: WhatsApp, Instagram, marketplace, Google Sheets, Google Calendar, email.
2. **Claude di tengah** membaca input itu (lewat connector/integrasi yang tersedia, export data, atau kamu tempel manual) dan
   menjalankan agent sesuai alur kerjanya.
3. **7 departemen → 30 agent.** Tiap agent **cuma pegang 1 tugas** dan punya **alur kerja tertulis** (SOP).
4. **Aturan emas:** nggak ada yang dikirim ke pelanggan sebelum **kamu setuju** (agent bikin draf → kamu klik setuju → baru terkirim).
5. **Tiap pagi 1 halaman:** apa yang sudah beres, apa yang nunggu keputusanmu.

---

## 1. PENJUALAN (5 agent)
| # | Agent | Satu tugasnya |
|---|---|---|
| 1 | Pencari Prospek | Cari calon pembeli yang cocok dengan kriteria yang kamu tulis (bidang, lokasi, ukuran). |
| 2 | Penyaring Prospek | Beri skor tiap prospek (cocok / mungkin / lewati) berdasarkan kriteria tertulis. |
| 3 | Penulis Chat Pertama | Tulis draf chat/email pembuka yang personal untuk prospek yang lolos saring. |
| 4 | Pengatur Janji Temu | Tawarkan slot kosong dari Google Calendar dan catat janji yang disepakati. |
| 5 | Pencatat Prospek | Perbarui daftar prospek di Google Sheets (status, tanggal kontak, catatan). |

## 2. CLOSING (4 agent)
| # | Agent | Satu tugasnya |
|---|---|---|
| 6 | Penyusun Penawaran | Susun draf penawaran dari template + kebutuhan yang dicatat saat janji temu. |
| 7 | Penjaga Follow-up | Ingatkan & tulis draf follow-up (mis. H+1, H+3, H+7) sampai ada jawaban ya/tidak. |
| 8 | Penjawab Keberatan | Siapkan draf jawaban untuk keberatan umum (harga, waktu, bandingkan kompetitor). |
| 9 | Pengonfirmasi Order | Setelah deal, rangkum pesanan + syarat dan kirim draf konfirmasi untuk kamu setujui. |

## 3. MARKETING (5 agent)
| # | Agent | Satu tugasnya |
|---|---|---|
| 10 | Perencana Konten | Susun kalender konten mingguan dari tema & produk yang kamu tentukan. |
| 11 | Penulis Konten | Tulis draf caption/naskah sesuai kalender dan gaya bahasa brand-mu. |
| 12 | Pembalas Komentar | Siapkan draf balasan untuk tiap komentar; yang sensitif diteruskan ke kamu. |
| 13 | Pengubah Format | Ubah 1 konten jadi beberapa format (carousel, naskah reels, status WA). |
| 14 | Pembaca Performa | Ringkas angka mingguan (reach, simpan, chat masuk) jadi 3 poin pelajaran. |

## 4. CS / LAYANAN PELANGGAN (4 agent)
| # | Agent | Satu tugasnya |
|---|---|---|
| 15 | Penjawab Chat | Jawab pertanyaan umum dari FAQ tertulis (jam buka, harga, cara pesan). |
| 16 | Penerus Komplain | Kenali komplain, rangkum, dan teruskan ke kamu — tidak menjawab sendiri. |
| 17 | Penjaga Pelanggan | Tandai pelanggan yang mulai menghilang (lama tidak order) + draf sapaan. |
| 18 | Pengumpul Ulasan | Minta ulasan ke pelanggan yang order-nya selesai, catat hasilnya. |

## 5. OPERASIONAL (4 agent)
| # | Agent | Satu tugasnya |
|---|---|---|
| 19 | Pengurus Pesanan | Pindahkan status pesanan (baru → diproses → dikirim) di Sheets & beri tahu tim. |
| 20 | Penyusun Jadwal Tim | Susun draf jadwal/shift mingguan dari ketersediaan tim. |
| 21 | Pengecek Stok | Cek stok/bahan vs pesanan, kasih peringatan sebelum habis. |
| 22 | Penyusun Ringkasan Pagi | Gabungkan laporan semua agent jadi 1 halaman tiap pagi. |

## 6. ADMIN & KEUANGAN (5 agent)
| # | Agent | Satu tugasnya |
|---|---|---|
| 23 | Pembuat Tagihan | Buat draf invoice dari order yang sudah dikonfirmasi. |
| 24 | Pengingat Bayar | Cek tagihan lewat jatuh tempo dan tulis draf pengingat yang sopan. |
| 25 | Pencatat Pengeluaran | Catat nota/struk ke Sheets per kategori. |
| 26 | Pencocok Mutasi | Cocokkan pembayaran masuk dengan invoice, tandai yang belum cocok. |
| 27 | Penyusun Laporan | Rangkum pemasukan, pengeluaran & piutang bulanan untuk kamu cek. |

## 7. ANALIS (3 agent)
| # | Agent | Satu tugasnya |
|---|---|---|
| 28 | Peneliti Klien | Sebelum kamu ketemu calon klien: rangkum info publik (website, ulasan) jadi 1 brief. |
| 29 | Pemantau Pesaing | Catat perubahan harga/promo/konten pesaing tiap minggu. |
| 30 | Peringkas Ulasan | Kelompokkan ulasan & keluhan pelanggan jadi pola yang berulang. |

**Total: 30 agent** (5 + 4 + 5 + 4 + 4 + 5 + 3).

---

## Template alur kerja (tulis 1 per agent)
```
AGENT      : Pengingat Bayar
TUGAS      : (satu kalimat) Ingetin pelanggan yang belum bayar.
INPUT      : Google Sheets "Tagihan" (kolom: no, pelanggan, jatuh tempo, status)
LANGKAH    : 1) Cek tagihan yang lewat jatuh tempo
             2) Tulis pengingat yang sopan (maks 3 kalimat, sebut nomor tagihan)
             3) Kirim DRAF ke pemilik untuk disetujui
             4) Setelah oke: kirim, lalu catat statusnya di Sheets
BATASAN    : Tidak pernah mengirim ke pelanggan tanpa persetujuan. Tidak mengubah nominal.
LAPOR KE   : Ringkasan pagi (bagian "nunggu kamu" kalau ada draf)
```

## Prompt siap tempel (Claude)
> Kamu adalah agent **[NAMA AGENT]** untuk bisnis saya, **[jenis bisnis]**. Tugasmu cuma satu: **[tugas]**.
> Ikuti alur kerja ini persis: [tempel LANGKAH]. Batasan: jangan pernah mengirim apa pun ke pelanggan — selalu buat **draf**
> dan tunggu persetujuan saya. Kalau datanya kurang atau ragu, tanya saya dulu. Format hasil: [tabel / poin / draf pesan].

## Prompt ringkasan pagi
> Dari catatan semua agent kemarin (saya tempel di bawah), buat **1 halaman**: (1) **BERES** — apa yang sudah selesai,
> maksimal 5 poin; (2) **NUNGGU KAMU** — draf/keputusan yang butuh persetujuan saya, urut dari paling penting, masing-masing
> dengan 1 kalimat konteks. Jangan menambah info yang tidak ada di catatan.

## Urutan pasang yang disarankan
1. Ringkasan pagi + Pengingat Bayar (paling cepat terasa).
2. Penjawab Chat (FAQ tertulis dulu) + Penerus Komplain.
3. Penulis Konten + Pembalas Komentar (selalu lewat persetujuan).
4. Sisanya, satu per minggu. Tulis alurnya dulu, baru jalankan.

*Catatan jujur: contoh di video (katering kantor, nama tagihan, nominal) adalah ilustrasi. Kemampuan tiap integrasi
(WhatsApp, Instagram, marketplace) tergantung akses/connector yang tersedia di akunmu — cek dulu sebelum mengandalkan
otomatisasi penuh. Tidak ada janji hasil.*
