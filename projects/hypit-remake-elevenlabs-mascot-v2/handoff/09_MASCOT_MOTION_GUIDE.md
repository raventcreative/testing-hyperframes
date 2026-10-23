# Maskot AI PRENEUR — gerak dan batas teknik

**Sumber:** `mascot/mascot_three_view_source.png`. Aset original dari Freddie: lembar gambar 3 tampak depan/samping/belakang, 1536×1024, warna latar putih dan label di bagian bawah. Karakter chibi ramah, rambut gelap bervolume, mata cokelat, polo hitam bertuliskan `AI PRENEUR`, celana krem, sepatu putih. Jangan ubah wajah, warna pakaian, bentuk rambut, atau tulisan kaos.

## Ini bukan file model 3D ber-rig

PNG sheet tidak punya mesh, bone, IK, layer lengan terpisah, atau blendshape mulut. Jangan mendeskripsikan gerakan tangan independen/mimik bibir/lipsync penuh seolah bisa langsung dilakukan. Dua opsi:

**Mode A — saat hanya PNG tersedia (WAJIB default):**
- Buat cutout front/side/back dengan mask transparan rapi, **non-destruktif**, tanpa memotong rambut, kaki, sepatu, atau tulisan polo. Hapus label bawah hanya dari cutout, pertahankan sumber asli. Jangan memakai rectangle berlatar putih yang akan menutup background user.
- Tempatkan maskot sebagai satu sprite utuh di stage; animasikan transform parent: translateX/Y, rotationZ kecil ±4°, scale 0.95–1.05, tilt/perspective sangat halus, step/landing via parent; bayangan/contact shadow mengikuti posisi kaki. Boleh *swapping* front ↔ side ↔ back saat transition hard cut hanya jika pose masuk akal.
- Respons aksi non-rig: muncul dari bawah belakang objek, mengangguk sebagai whole-body tilt, memiringkan tubuh saat melihat terminal, langkah menggeser seluruh sprite dan shadow, berganti tampak saat memperlihatkan bagian mesin. Tangan tetap relatif terhadap badan; jangan potong lalu putar lengan secara acak.
- Kehadiran terpilih: s02, s04, s08, s11, s14, s16, s19. Maksimal sekitar 25–40% lebar frame untuk maskot, jangan menutupi hero, bagian kepala, caption, atau komponen penting. Untuk beberapa adegan maskot boleh hanya cameo di pojok depan objek.
- Berikan ritme: aksi relevan dipicu kata bermakna; *idle bouncing* sepanjang video DILARANG. Variasikan shot maskot vs shot tanpa maskot agar punch visual terjaga.

**Mode B — bila kemudian ada GLB/FBX blendshape/rig atau sprite berlayer:**
- Inspeksi asset rig/bone naming/renderer dulu; gunakan skeletal animation sederhana (gesture menunjuk, head turn, small wave, blinking/lipsync hanya jika benar-benar punya kontrol). Pose harus menjaga identitas. Jangan invent rig, bones, mesh, atau aksesori.
- Render 3D/rigged karakter bisa direkomendasikan sebagai peningkatan setelah user memberikan berkas rig. **Jangan menahan Mode A hanya karena Mode B tidak tersedia.**

## Arc karakter

Maskot bukan host yang bicara sepanjang video. Ia pemandu visual yang membantu memahami proses; tidak menyaingi VO.

| Beat | Kemunculan | Aksi yang aman dari PNG | Interaksi/continuity |
|---|---|---|---|
| Intro Hypit | s02 | Peek dari balik mesin stars/reel, whole-body tilt mengikuti bintang | Mendorong tatapan ke input video berikutnya |
| Agent | s04 | Side cutout hadir di pinggir inti agent, sedikit lean saat rail aktif | Tidak menghalangi coding core |
| Editing | s08 | Side sprite menatap timeline, sedikit lean in lalu settle | Tidak menutup caption/track |
| Variasi | s11 | Front sprite berpindah bersama dial saat kartu produk berganti | Beri efek dial, bukan tangan independen |
| Hak aset | s14 | Front sprite menunduk ringan saat vault izin terbuka | Tidak mengklaim aset random sudah legal |
| Brief | s16 | Side sprite muncul di sisi terminal sebagai fasilitator | Command install muncul s15, diverifikasi terpisah |
| CTA | s19 | Front sprite cameo tenang di sisi kanan gelembung `HYPIT` | Last frame diam, tidak lip sync palsu |

## QA karakter

- Siluet, rambut, mata, outfit, label polo konsisten dengan **source**.
- Mask bersih tanpa halo putih, tanpa label `FRONT/SIDE/BACK`.
- Tidak ada morph antar-view aneh, tidak ada tangan/jari yang tiba-tiba muncul.
- Semua animasi seek-safe/deterministik di GSAP; clip sprite dari file lokal.
- Character never obscures the hero, small upper captions, highlight, or mobile safe areas.
- Jika portrait 3-view ini tidak bisa dipisahkan rapi dengan tool yang ada, catat blocker dan gunakan hanya **satu cutout depan** yang diverifikasi, bukan gambar sheet penuh.
