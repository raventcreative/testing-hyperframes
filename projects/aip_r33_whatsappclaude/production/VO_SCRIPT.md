# R33 · WhatsApp disambung ke Claude (WhatsApp MCP) — tema PUTIH · VO 102,8 dtk · video 104,6 dtk · CTA "Komen WA"

Format batch 8: dunia voxel 3D (putih) + maskot 3D host + robot AIpreneur co-host (kanan, utuh). Referensi: `aip_remake_batch8/refs/ref3`
(100,2 dtk) — panjang dipertahankan (target 90–110 dtk).

## Naskah (production/vo_lines.txt — satu take ElevenLabs, Dakocan, eleven_v4, auto tags)
1. Jempol sampai pegel, cuma buat nyari satu pesan di WhatsApp?
2. Sekarang Claude bisa nyariin buat kamu.
3. Proyek open source WhatsApp MCP buatan Luke Harries, lisensi MIT.
4. Dia nyambungin akun WhatsApp pribadimu ke Claude Desktop.
5. Kirain cuma bisa baca chat? Ada dua belas tool, aku bagi jadi empat laci.
6. Laci cari: cari kontak, lihat daftar chat, buka detail chat, dan nemuin chat pribadi sama satu orang.
7. Laci baca: tarik pesan pakai filter, lihat konteks di sekitar pesan, cek interaksi terakhir, dan semua chat tempat orang itu ikut.
8. Laci kirim: pesan ke nomor atau grup, file seperti gambar, video, dokumen, plus pesan suara.
9. Laci unduh: media dari chat disimpan ke komputermu.
10. Bagian paling enak: kamu tinggal nanya pakai bahasa sehari-hari.
11. Misalnya, supplier kemarin kasih harga berapa, ya?
12. Claude milih tool yang cocok, nyari di pesanmu, lalu jawab lengkap dengan konteksnya.
13. Cara pasangnya? Siapin Go, Python, UV, dan Claude Desktop.
14. Unduh repo-nya, jalankan bridge-nya, lalu scan kode QR-nya dari WhatsApp di ponselmu.
15. Tempel konfigurasinya di Claude Desktop, restart, dan WhatsApp muncul sebagai integrasi.
16. Riwayat pesanmu disimpan di database SQLite, di komputermu sendiri.
17. Isinya cuma dikirim ke Claude kalau tool-nya dipakai, dan itu kamu yang kendalikan.
18. Tapi README-nya sendiri kasih peringatan: seperti banyak server MCP, ada risiko prompt injection yang bisa bikin data pribadi bocor.
19. Artinya, pesan dari orang lain bisa nyelipin perintah buat AI-nya. Jadi cek dulu sebelum Claude ngirim apa pun.
20. Satu lagi: kira-kira tiap dua puluh hari, koneksinya mungkin minta scan ulang.
21. Claude bantu nyari, kendali tetap di tangan kamu.
22. Komen WA, aku kirim panduan setup langkah demi langkah plus checklist keamanannya lewat DM.

## ATM — apa yang kami ubah
- **Amati (referensi):** "bayangin WhatsApp disambung ke Claude" → nama proyek + gratis → "cuma baca chat? salah" → 12 tools dibacakan
  berkelompok → tanya-jawab → cara pasang (Go/Python/UV, unduh, scan QR, Claude Desktop, restart) → data lokal → risiko prompt injection →
  login ulang ±20 hari → CTA + follow.
- **Tiru (hanya ide + fakta yang dicek):** proyek, 12 tool, langkah setup, penyimpanan lokal, peringatan, ±20 hari.
- **Modifikasi:** hook sendiri (rasa sakit "jempol pegel" ditunjukkan, bukan ditulis di kartu); urutan sendiri (12 tool dikelompokkan jadi
  **4 laci** CARI · BACA · KIRIM · UNDUH — metafora kami, setiap tool disebut per laci sesuai daftar README); contoh UMKM sendiri (harga
  supplier, SIMULASI, nama karangan); bagian risiko diperjelas (apa itu prompt injection + "cek dulu sebelum Claude ngirim apa pun") dan
  penutup "kendali tetap di tangan kamu"; CTA AIpreneur ("Komen WA … lewat DM"). Tidak ada "gratis" (README tidak bicara harga; yang benar:
  open source, lisensi MIT), tidak ada klaim "server asing" (tidak ada di README), tidak ada follow-CTA referensi. Tidak ada kalimat
  referensi > 3 kata berurutan.

## Fakta — dicek di README + LICENSE github.com/lharries/whatsapp-mcp (diambil 2026-11-21, raw.githubusercontent.com)
- MCP server untuk WhatsApp; nyambung ke **akun WhatsApp pribadi** lewat WhatsApp web multidevice API (library whatsmeow).
- Lisensi **MIT**, "Copyright (c) 2025 Luke Harries".
- **12 tool** persis: search_contacts, list_messages, list_chats, get_chat, get_direct_chat_by_contact, get_contact_chats,
  get_last_interaction, get_message_context, send_message, send_file, send_audio_message, download_media.
- Prasyarat: Go, Python 3.6+, Claude Desktop (atau Cursor), UV; FFmpeg opsional (pesan suara .ogg Opus).
- Langkah: clone repo → `cd whatsapp-bridge && go run main.go` → scan QR pakai WhatsApp di HP → "After approximately 20 days, you
  will might need to re-authenticate" → salin JSON ke `claude_desktop_config.json` → restart Claude Desktop → WhatsApp muncul sebagai integrasi.
- Data: "All your messages are stored locally in a SQLite database and only sent to an LLM (such as Claude) when the agent accesses
  them through tools (which you control)."
- Peringatan README: "as with many MCP servers, the WhatsApp MCP is subject to the lethal trifecta … project [prompt] injection could lead
  to private data exfiltration." (VO baris 18). Baris 19 = penjelasan konsep + saran praktis (bukan klaim README).
- Tidak diverifikasi / tidak dipakai: jumlah bintang GitHub (API tidak bisa diakses dari sesi ini) — tidak disebut di video.

## Teknik (skill baru, teknik saja)
1. **throughline-explainer — satu objek benang merah:** gelembung chat putih (pesan yang hilang) ditemukan di hook, menyeberang jembatan
   ke Claude, disortir ke laci, keluar dari jawaban, disimpan di SQLite, di-X-ray di checkpoint, dan berakhir di atas CTA (kotak komentar).
2. **html-demo — UI digambar sebagai View(t) di layar 3D:** jendela chat Claude (kursor datang, klik, ketik, tombol Kirim, status kerja
   dengan chip tool, jawaban streaming, tahan ≥ 0,8 dtk), jendela baca laci 2 (4 tool berganti di satu jendela), terminal (clone → go run
   → QR → tersambung) dan editor config → restart → toggle integrasi. Semua SIMULASI, nama & angka contoh.
3. **product-launch-film — shared element / match cut:** gelembung masuk ke monitor Claude Desktop → kamera menyelam ke layar (flash) →
   keluar di dunia lemari; tombol/laci mengeluarkan kartu tool; jawaban "mengeluarkan" gelembung hasil.
4. **business-explainer-30s — struktur masalah → apa → langkah → bukti → nama:** hook rasa sakit → apa itu WhatsApp MCP → 12 tool →
   contoh tanya-jawab → cara pasang 4 langkah → data & risiko → CTA.
5. **prompt-motion-techniques — "spinning pain list" + process fill:** daftar chat digulir terlalu cepat untuk dibaca (blur kecepatan) lalu
   melambat dan berhenti di satu pesan; 12 tool "mengisi" lemari (counter 12/12), 4 peti (Go/Python/UV/Claude Desktop) mengisi mesin.
- Transisi (semua beda): zoom-out reveal + island hop, dive ke monitor + flash, whip tilt vertikal (laci 1→2), turntable spin-blur (2→3),
  elevator turun (3→4), iris, whip ke langit (A→S), dolly zoom (S→L), orbit 180° (L→X), shutter (X→C), spin (C→F), shockwave ring (CTA).
- Mascot + robot (mascot_robot_recipes): maskot host (rise di 5,6 dtk, lip sync, point/explain sesuai kata), robot co-host terbang masuk di
  "WhatsApp MCP", mengetik di keyboard hologram saat Claude bekerja, kaget di "injection", menggeleng di "bocor", mengangguk di "cek dulu".

## VO — cek (aturan batch 8)
- Satu take utuh, tidak dipotong/di-pad/di-stretch; scene mengikuti alignment (VO offset +0,3 dtk).
- Listen-check whisper small + medium (bahasa id): medium hanya beda ejaan/angka (dua belas→12, empat→4, dua puluh→20, sehari-hari→
  sehari hari, repo-nya→repo nya…) + "Claude"→"cloud" (nama Inggris, dibaca benar; sama seperti R20) + "Harries"→"Harris". Small salah
  dengar beberapa kata (ritminya, rewaian, nyalimpin, hirain, met) yang didengar benar oleh medium → tidak ada kata yang salah di KEDUA model.
- Cek akhir pada MP4 final: lihat bagian "Final check" di bawah.

## Revisi 2026-11-21 (addendum batch 8 + permintaan SFX)
- Background = HANYA plate putih brand (`brand/bg-light.png` cover-fit → `assets/brand/bg_light_1080x1920.png`, `<img>` di bawah kanvas
  WebGL transparan). Tidak ada langit gradien / awan voxel; fog diwarnai #eef3fb. Wipe shutter + iris pakai putih/biru-muda brand.
- SFX lebih kaya (tools/sfx.py, 333 event): whoosh di setiap transisi, riser + impact lembut di reveal besar, pop/klik UI (judul, chip,
  kartu tool, laci), tik halus saat caption muncul, blip kirim/terima pesan (chat, jawaban Claude, DM), tik ketik (pertanyaan, terminal,
  config, "WA"). Level tetap ≈ −8…−10 dB di bawah puncak VO untuk hit/whoosh (lebih pelan untuk tik), tanpa kompresor; tiap transient
  digeser ±150 ms agar ≥ 70 ms dari onset kata (0 event dekat onset).
