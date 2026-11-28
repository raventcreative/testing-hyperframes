# DM · WIFI — RuView: Wi-Fi sensing open source (link + panduan pasang)

Halo! Ini yang kamu minta dari video "Wi-Fi bisa deteksi gerakan" 👇

**Repo:** https://github.com/ruvnet/RuView
- Pembuat: ruvnet · Lisensi: **MIT** (open source) · ±105 ribu bintang GitHub (dicek 28 Nov 2026)
- Status: **beta** — masih aktif dikembangkan, API & firmware bisa berubah.

## Apa ini sebenarnya
Router Wi-Fi memenuhi ruangan dengan gelombang radio. Waktu orang bergerak, bahkan cuma napas, gelombang itu berubah sedikit.
RuView membaca perubahan itu (namanya **CSI — Channel State Information**) dari sensor kecil, lalu model AI menebak:
ada orang atau tidak, ada gerakan, sampai pola napas. **Tanpa kamera.** Menurut README, deteksi bisa tembus tembok
sampai sekitar ±5 m, tergantung kondisi sinyal.

## Yang kamu butuhkan
| Pilihan | Hardware | Hasil |
|---|---|---|
| Coba dulu tanpa alat | Docker di laptop | demo dengan **data simulasi** (bukan sinyal asli) |
| Sensing beneran | **ESP32-S3** (±$9 per board) — README menyarankan 2+ node | kehadiran, gerakan, napas |
| Laptop biasa saja | Wi-Fi bawaan laptop | cuma **deteksi kasar** (RSSI), bukan CSI penuh |
Catatan README: ESP32-C3 dan ESP32 original **tidak didukung**.

## Cara pasang (dari README RuView)
**A. Dibantu Claude Code (plugin bawaan repo)** — di Claude Code ketik:
```
/plugin marketplace add ruvnet/RuView
/plugin install ruview@ruview
/ruview-start
```
`/ruview-start` memandu onboarding (demo Docker / build repo / ESP32 live). Perintah lain: `/ruview-flash` (flash firmware ESP32),
`/ruview-provision` (isi Wi-Fi & IP), `/ruview-app` (jalankan aplikasi sensing), `/ruview-verify` (tes + bukti).

**B. Demo Docker (tanpa hardware, data simulasi)**
```
docker pull ruvnet/wifi-densepose:latest
export RUVIEW_API_TOKEN=$(openssl rand -hex 32)
docker run -p 127.0.0.1:3000:3000 -e RUVIEW_API_TOKEN ruvnet/wifi-densepose:latest
# buka http://localhost:3000
```
**C. ESP32-S3 beneran** — flash firmware + provisioning Wi-Fi, ikuti `firmware/esp32-csi-node/README.md` di repo
(atau `/ruview-flash` + `/ruview-provision` lewat plugin Claude Code).

**Contoh prompt buat Claude Code:**
> Bantu aku pasang RuView dari https://github.com/ruvnet/RuView. Mulai dari demo Docker dulu (data simulasi). Jelaskan tiap
> langkah, jangan jalankan perintah yang menulis/flash ke perangkat sebelum aku setuju.

## Bisa dipakai buat apa (contoh dari README)
- Lampu / AC nyala otomatis saat ada orang di ruangan — lewat integrasi **Home Assistant** (MQTT).
- Tahu ruangan meeting kosong atau terisi, hitung jumlah orang di suatu area.

## Batasannya (jujur)
- **Beta.** Belum alat medis / sistem keamanan bersertifikat.
- Laptop tanpa sensor CSI = cuma deteksi kasar.
- **Pose tubuh tanpa kamera belum akurat** (README: model on-device masih tahap awal).
- Satu ESP32 saja = resolusi ruang terbatas; README menyarankan 2+ node.

## Privasi — wajib
- Pasang **hanya di ruangan milikmu sendiri**.
- **Semua penghuni harus tahu** dan setuju ada sensor gerakan.
- Jangan dipakai untuk memantau orang lain diam-diam.

Selamat coba! Kalau mau belajar bikin sistem AI buat bisnismu, cek link di bio AI PRENEUR.
