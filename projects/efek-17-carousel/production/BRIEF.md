# AIpreneur — 17 efek video AI (carousel) · brief untuk tiap efek

Tujuan: 17 video demo pendek, satu per efek, untuk carousel Instagram AIpreneur (Freddie Kashawan).
Tiap video menunjukkan SATU efek dengan jelas dan cantik, tanpa orang asli — pakai presenter ilustrasi bersama.

## Spec (sama untuk semua)
- 1080x1350 (4:5), 30 fps, 4.0 s per efek, tanpa audio.
- Root `index.html` menaruh efek N di slot detik (N-1)*4 .. N*4. File efek: `compositions/eNN.html`, composition id `eNN`.
- Kit wajib: `assets/presenter.js` (window.HFP) + `assets/kit.css`. Baca header presenter.js untuk geometri.
  - `HFP.backdropHTML(P)` latar ruangan navy · `HFP.mount(host,P)` presenter · `HFP.animate(R,t)` napas/kedip/ngomong
  - `HFP.chromeHTML(P, n, "Nama Efek")` logo AI PRENEUR kiri atas + chip "NN/17 · NAMA" kanan atas — WAJIB tampil sepanjang video, paling depan.
  - `HFP.SIL` = path siluet badan (viewBox figur 640x1000, figur di left 220 top 380) untuk outline/cutout.
  - `.k-cap` = caption bawah (y≈1196), kata kunci pakai `<span class="hl">`. `.k-card` kartu kertas, `.k-dark` panel gelap.
- Contoh acuan kualitas & pola kode: `compositions/e01.html` (orbit). Tiru polanya: proxy tween 0→4 s, `render(t)` murni fungsi waktu.
- Brand: Poppins 400/700 saja, warna aksen #00c9ff (cyan), gradasi headline #00c9ff→#294b77, navy. Teks on-screen Bahasa Indonesia, gaya Freddie: pendek, tajam.

## Aturan
- Deterministik: tidak ada Math.random/Date.now; "acak" = angka tetap yang kamu tulis.
- Lapisan: belakang badan = elemen di layer sebelum `figwrap`; depan badan = setelahnya. Wajah (x 400–680, y 450–740) tidak boleh tertutup kecuali efeknya memang zoom/transisi singkat.
- Loop-friendly: detik 0 dan detik 4 hampir sama (efek masuk ~0.3–0.6 s, tahan, kembali ke keadaan awal di ~3.4–3.9 s), karena carousel memutar ulang.
- Safe area teks: x 60–1020, di bawah chip (y>130) dan di atas y 1300.
- Jangan ubah `assets/presenter.js`, `assets/kit.css`, `index.html`, atau file efek lain. Kalau butuh varian (misal presenter tanpa latar), bangun di file efekmu sendiri (boleh panggil `HFP.figureSVG(P)` sendiri).
- Tidak ada CSS transform di elemen yang dianimasikan GSAP; tidak ada filter/opacity di container preserve-3d.
- Hindari CSS blur besar di elemen besar (render lambat); blur kecil ok.

## QA per efek (wajib sebelum selesai)
- `npx hyperframes lint` 0 error.
- `npx hyperframes snapshot --at <4–5 titik di slotmu>` lalu LIHAT gambarnya; perbaiki sampai rapi dan efeknya terbaca jelas.
