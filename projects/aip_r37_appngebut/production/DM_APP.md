# APP NGEBUT TOOLKIT — 24 perbaikan + prompt siap tempel buat Claude

Buat kamu yang bikin aplikasi pakai Claude / Claude Code (vibe coding) dan nggak mau pelanggan kabur karena lemot.
Isinya 24 perbaikan standar yang dipakai developer di mana-mana, masing-masing dengan alasan singkat + prompt siap tempel.

## Cara pakai (baca dulu)
1. **Ukur dulu.** Minta Claude bikin catatan "sebelum": halaman mana yang lambat, request mana yang lama. Tanpa angka sebelum,
   kamu nggak tahu perbaikannya berhasil atau nggak.
2. **Satu perbaikan, satu sesi.** Tempel satu prompt, minta Claude jelasin rencananya dulu, baru ubah kode.
   Tambahkan ke akhir prompt: *"Jelasin dulu rencanamu sebelum ngubah kode, dan jangan ubah perilaku aplikasi."*
3. **Tes lagi setelah tiap perubahan** (fitur masih jalan? lebih cepat?). Kalau nggak ada bedanya, kembalikan.
4. Nggak semua tips cocok buat semua aplikasi. Kalau Claude bilang "aplikasi kamu belum butuh ini", itu jawaban yang bagus.
5. Sebutkan stack-mu di prompt kalau tahu (misal: Next.js + Supabase, Laravel + MySQL, React + Firebase).

---

## A. Yang langsung terasa di layar

**01 · Skeleton loading** — layar nggak pernah kosong; orang lihat "kerangka" halaman sambil data dimuat.
> Tambahkan skeleton loading di halaman-halaman yang mengambil data (daftar, detail, dashboard). Bentuk skeleton harus mirip layout aslinya supaya halaman nggak "loncat" saat data masuk. Jangan pakai spinner di tengah layar kosong.

**02 · Tampilan berubah duluan (optimistic UI)** — tombol suka/simpan/centang langsung berubah; server menyusul di belakang.
> Untuk aksi kecil seperti suka, simpan, centang tugas, dan ubah status, terapkan optimistic update: ubah tampilan langsung, kirim ke server di belakang, dan kembalikan tampilan + tampilkan pesan kalau server gagal.

**03 · Jawaban AI streaming** — jawaban AI muncul kata demi kata, pengguna nggak menatap layar kosong.
> Fitur AI di aplikasiku masih menunggu jawaban selesai baru ditampilkan. Ubah supaya respons di-stream (kata demi kata) dari server ke tampilan, dengan tombol berhenti, dan tetap aman kalau koneksi putus di tengah jalan.

**04 · Virtualisasi daftar panjang** — cuma baris yang kelihatan di layar yang digambar, jadi scroll tetap mulus.
> Ada daftar/tabel yang bisa berisi ribuan baris. Terapkan list virtualization (hanya render baris yang terlihat) memakai library yang cocok dengan stack-ku. Pastikan scroll, pencarian, dan klik baris tetap jalan.

## B. Gambar & file yang dikirim ke browser

**05 · Gambar WebP / AVIF** — ukuran file gambar umumnya lebih kecil dari JPG/PNG dengan kualitas yang mirip.
> Ubah semua gambar di aplikasiku supaya disajikan dalam WebP atau AVIF (dengan fallback untuk browser lama), dengan ukuran yang sesuai tampilan (responsive sizes). Kalau gambar diunggah pengguna, konversi otomatis saat upload.

**06 · Lazy-load gambar di bawah layar** — gambar yang belum kelihatan dimuat belakangan, halaman pertama lebih cepat tampil.
> Terapkan lazy loading untuk gambar dan embed yang berada di bawah layar pertama. Gambar utama di atas (hero/logo) JANGAN di-lazy-load. Kasih ukuran width/height supaya layout nggak loncat.

**07 · Pecah JavaScript per halaman (code splitting)** — yang dimuat cuma kode untuk halaman yang dibuka.
> Analisis ukuran bundle JavaScript aplikasiku, lalu terapkan code splitting per halaman/route dan dynamic import untuk komponen berat (editor, grafik, peta). Tunjukkan ukuran bundle sebelum dan sesudah.

**08 · Script pihak ketiga dimuat setelah halaman siap** — chat widget, analitik, iklan nggak boleh menahan tampilan utama.
> Daftar semua script pihak ketiga di aplikasiku (chat widget, analytics, pixel iklan, dll). Muat semuanya setelah halaman utama siap (defer/async/after load), dan hapus yang sudah tidak dipakai.

**09 · Buang library yang nggak dipakai** — unduhan aplikasi jadi lebih kecil.
> Cari dependency/library di proyekku yang tidak dipakai atau dobel fungsinya, dan yang terlalu besar untuk kebutuhan kecil. Usulkan mana yang bisa dihapus atau diganti yang lebih ringan, lalu hapus setelah aku setuju.

**10 · File lewat CDN** — gambar, CSS, JS dikirim dari server terdekat dengan pengunjung.
> Sajikan file statis (gambar, CSS, JS, font) lewat CDN sesuai hosting-ku. Jelaskan langkah setup-nya dan pastikan cache header file statis sudah benar.

**11 · Kompresi Gzip (atau Brotli)** — kiriman teks (HTML, CSS, JS, JSON) jadi lebih ringan.
> Pastikan server/hosting-ku mengirim respons HTML, CSS, JS, dan JSON dengan kompresi Brotli atau Gzip. Cek apakah sudah aktif, dan aktifkan kalau belum.

**12 · Cache browser** — kunjungan berikutnya nggak unduh ulang file yang sama.
> Atur cache header untuk file statis: file dengan nama ber-hash di-cache lama (immutable), HTML jangan di-cache lama. Pastikan setelah deploy pengunjung tetap dapat versi terbaru.

## C. Request ke server

**13 · Debounce pencarian** — cari setelah orang berhenti ngetik, bukan tiap huruf.
> Kolom pencarian/autocomplete di aplikasiku mengirim request di setiap ketikan. Tambahkan debounce (sekitar 300 ms) dan batalkan request lama kalau ada ketikan baru, supaya hasil yang tampil selalu untuk teks terakhir.

**14 · Cegah request dobel** — tombol yang diklik dua kali nggak bikin pesanan/pembayaran dobel.
> Cegah request ganda saat tombol diklik berkali-kali (bayar, kirim formulir, simpan): nonaktifkan tombol selama proses, dan di server pakai idempotency key atau pengecekan supaya aksi yang sama tidak diproses dua kali.

**15 · Request paralel** — request yang nggak saling tunggu dijalankan bareng.
> Cari tempat di kodeku yang mengambil beberapa data berurutan padahal tidak saling bergantung, lalu jalankan bersamaan (misalnya Promise.all) dengan penanganan error per request.

**16 · Batas waktu untuk layanan luar (timeout)** — kalau layanan luar lambat, aplikasimu nggak ikut macet.
> Semua panggilan ke API/layanan luar (pembayaran, ongkir, AI, email) harus punya timeout, retry terbatas untuk error sementara, dan pesan yang jelas ke pengguna kalau gagal. Tunjukkan di mana saja kamu menambahkannya.

**17 · Antrean di belakang layar (background job)** — tugas berat (ekspor PDF, kirim email massal, proses video) nggak bikin pengguna menunggu.
> Pindahkan tugas berat seperti ekspor laporan, kirim email, dan proses file ke background job queue yang cocok dengan stack-ku. Pengguna langsung dapat konfirmasi "sedang diproses" dan notifikasi saat selesai.

## D. Database

**18 · Cache data yang sering dibuka (misalnya Redis)** — data yang sama nggak diambil ulang dari database tiap kali.
> Identifikasi data yang sering dibaca tapi jarang berubah (katalog, pengaturan, ringkasan dashboard). Tambahkan cache (misalnya Redis atau cache bawaan hosting-ku) dengan waktu kedaluwarsa dan cara menghapus cache saat datanya berubah.

**19 · Index database** — pencarian nggak perlu memeriksa semua baris.
> Lihat query yang paling sering dijalankan dan yang lambat. Usulkan index database untuk kolom yang dipakai di WHERE, JOIN, dan ORDER BY, jelaskan alasannya, lalu buat migrasinya.

**20 · Benahi query N+1** — ambil data sekaligus, bukan satu-satu per item.
> Cari pola N+1 query di kodeku (mengambil daftar, lalu query lagi untuk setiap item). Ganti dengan eager loading / join / satu query dengan IN, dan tunjukkan jumlah query sebelum dan sesudah.

**21 · Ambil kolom yang perlu saja** — jangan `SELECT *` kalau yang dipakai cuma nama dan email.
> Periksa query yang mengambil semua kolom padahal hanya beberapa yang dipakai (terutama kolom besar seperti teks panjang atau JSON). Ubah supaya hanya mengambil kolom yang dibutuhkan halaman tersebut.

**22 · Pagination** — hasil yang banyak dibagi per halaman, bukan dikirim sekaligus.
> Endpoint/daftar di aplikasiku mengirim semua data sekaligus. Terapkan pagination (atau infinite scroll dengan cursor) di server dan tampilan, dengan batas jumlah per halaman.

**23 · Connection pooling** — koneksi database dipakai ulang, nggak dibuka-tutup setiap request.
> Pastikan aplikasiku memakai connection pooling ke database (termasuk kalau jalan di serverless). Jelaskan setting yang dipakai dan cek tidak ada kebocoran koneksi.

## E. Tes

**24 · Tes di HP murah & sinyal lemah** — pelangganmu belum tentu pakai HP mahal dan Wi-Fi kencang.
> Buatkan aku checklist tes performa: cara mensimulasikan HP lambat dan jaringan lambat (CPU & network throttling di Chrome DevTools), cara menjalankan Lighthouse, dan halaman mana yang wajib dites sebelum rilis. Lalu jalankan dan rangkum hasilnya.

---

### Bonus (dari daftar umum, tidak dibahas di video)
- **Cegah render ulang yang nggak perlu** — *"Cari komponen yang render ulang tanpa perlu (React DevTools Profiler) dan perbaiki dengan memo/useMemo/useCallback hanya di tempat yang terbukti berat."*
- **Font self-host & batasi ketebalan** — *"Host font sendiri, pakai format woff2, hanya ketebalan yang dipakai, dan font-display: swap."*
- **Pantau kecepatan pengguna asli** — *"Pasang pengukuran Core Web Vitals dari pengguna asli (RUM) di aplikasiku dan buat ringkasan mingguannya."*

Catatan jujur: ini praktik standar performa web. Seberapa besar efeknya tergantung aplikasi kamu — makanya selalu ukur sebelum & sesudah.

— AI PRENEUR
