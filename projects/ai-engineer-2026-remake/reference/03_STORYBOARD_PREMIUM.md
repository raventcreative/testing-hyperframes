# Storyboard — *Build the Machine* / 15 Scenes

**Durasi sasaran:** ±100–115 dtk setelah VO direkam. Timecode kolom di bawah **perkiraan pacing**, wajib di-re-time ke audio VO aktual di Claude Code. Label `SC` = nomor scene produksi; `ref` = referensi source.

| SC / Estimasi | VO intinya | Objek hero / aksi maskot | Kamera dan transisi unik | Tipografi utama | Sound cue opsional |
| --- | --- | --- | --- | --- | --- |
| `01` `00–05` | “Bikin AI agent doang…” | Close-up core AI metalik tanpa baut fondasi; maskot 3D meraih modul saat struktur miring | Macro 85 mm → **inertia tilt** kecil pada “ambruk”; pecahan alur kabel membentuk garis blueprint | `AI AGENT ≠ AI ENGINEER` (kata penting di kotak navy) | mechanical clack |
| `02` `05–11` | “Sepuluh komponen… urutannya penting” | Blueprint besar 10 slot terangkat dari workbench; maskot memberi gestur “ayo bangun” | Top-down morph ke angle 35°; satu socket kosong jadi fokus pertama | `10 KOMPONEN` | paper slide / servo soft |
| `03` `11–20` | `01 Python` | Tulisan kode sebagai engraved strips; strip mengunci menjadi track mekanik; roda akhirnya mulai berputar | Tracking sepanjang garis code → orbit 18° menuju modul | `01 / PYTHON` dan `fungsi · data · API · debugging` hanya saat diucapkan | precise key taps |
| `04` `20–29` | `02 Software Engineering` | Cabang Git berbentuk rel, tabung database, port API dan slot authentication bekerja secara bertahap; maskot menyambungkan kabel | Lens follows cable melalui satu port (**portal handoff**) → reveal bangunan sistem | `02 / SOFTWARE ENGINEERING` | latch clicks |
| `05` `29–38` | `03 Machine Learning` | Manik data menggelinding ke tray training. Garis prediksi muncul, satu titik anomali ditandai; cek ulang model | Macro scatter 2.5D, axis rotates jadi landasan untuk objek berikutnya | `03 / MACHINE LEARNING` | subtle counting ticks |
| `06` `38–45` | `04 Deep Learning` | Rangkaian neuron berlapis, pulsa blue-light menyalur; glass-node modules masuk satu per satu | Dolly-through jaringan; node terdekat menjadi wipe ke jalur tekstual | `04 / DEEP LEARNING` | muted electronic ping |
| `07` `45–54` | `05 LLM` | Token typeset 3D masuk ke context reel; matrix attention “memilih hubungan” lewat jalur halus | Tight track atas token, pull-back 35° matrix; **no random glowing word cloud** | `05 / LLM` | sliding register ticks |
| `08` `54–61` | `06 AI Application` | Satu konektor API menyambung ke aplikasi UI kecil; structured response keluar dalam bentuk kartu data terstruktur | Kabel output jadi jalur kameranya; focus pull dari port ke app running | `06 / AI APPLICATION` | connector snap |
| `09` `61–72` | `07 RAG` | Lemari arsip terbuka; dokumen dipotong menjadi indeks lembar; satu query menarik 2 potongan yang relevan, model merakit jawaban bersumber | **Hero wow:** kamera masuk ke laci, melewati rak arsip dan keluar sebagai satu result panel | `07 / RAG` | paper, restrained lift |
| `10` `72–82` | `08 AI Agent` | Mini-agent mengunjungi 4 node: pahami → pilih alat → jalankan → cek. Maskot membuka gerbang izin pada tahap “action” | Long take satu loop 270° (simulated via scene camera), melewati roda yang jadi tes bench | `08 / AI AGENT` | step clicks |
| `11` `82–90` | `09 Evaluation` | Unit test rig, kasus hijau dan merah. Maskot mengganti modul rusak lalu mengetes ulang; hasil tampak membaik tanpa angka palsu | Hit cut dari loop ke rotating test gauge; kalibrasi → close on pass | `09 / EVALUATION` | test buzzer low / check |
| `12` `90–99` | `10 Production` | Mesin meluncur masuk shell produksi bertekstur porcelain+navy enamel; security, latency, log, cost gauges aktif | Giant casing mengangkat kamera **crane up** → polished machine ready | `10 / PRODUCTION` | industrial closure |
| `13` `99–106` | “Pilih jalur…” | Workbench bercabang menjadi dua jalur rapi: **build product** dan **deeper models**; maskot menggeser selector lever | Symmetrical dolly-out lalu split-focus 2 jalur; no 3D tunnel berlebihan | `BUILD PRODUCTS` / `DEEPER MODELS` (sesuai VO) | two detent clicks |
| `14` `106–112` | “Mulai proyek kecil…” | Mini proyek tumbuh ke prototipe → working system, semuanya komponen mesin yang sama, bukan aset terbang acak | One continuous camera pull-back menyingkap perubahan progresif | `SATU PROYEK DULU` | step-up mechanical ticks |
| `15` `112–end` | “AI Engineer … benar-benar bekerja. Simpan…” | Semua 10 modul tersusun. Mesin bergerak, maskot mengamati dengan ekspresi bangga alami. AIpreneur upper-left tetap; end hero locked calm | Hero 3/4 view, soft rimlight, camera ease-out lalu **still lockup** no fade | `SISTEM AI YANG BEKERJA` → `SIMPAN ROADMAP INI` | completion seal, then silence |

## Scene contract ringkas

**Hero position:** mayoritas elemen di x 100–1000, y 500–1490; tekstur background tetap terlihat. Teks penjelas di y 270–430; logo x ≈ 65, y ≈ 70, ukuran proporsional 160–200 px, jaga jarak dengan UI Instagram.

**Setiap beat wajib punya empat fase:** visible entering frame (0.0), anticipation (0.08–0.30), meaningful action pada kata VO, settle (0.15–0.3) sebelum handoff.

**Material dan lighting:** porcelain white, satin navy enamel, brushed aluminum, charcoal rubber gasket, frosted translucent plates (tidak mengklaim real refraction), key light dari upper-left, real contact shadow dan occlusion, 3 depth planes.

**Path-based transitions, bukan preset:**

- Kode Python **menjadi kabel** yang diikuti kamera sampai port software.
- Grafik ML **menjadi node neural** melalui transformasi vertex-ke-node.
- Token LLM **masuk ke output socket API** sehingga cut AI application punya alasan.
- Kabel API **menjadi pembatas rak arsip** pada RAG.
- Potongan jawaban RAG **masuk ke agent tool tray**, bukan tiba-tiba fade.
- Roda agent **menjadi jarum gauge eval**.
- Hasil test **dimasukkan ke casing** production.
- Selector production **membuka 2 jalur** yang masuk kembali ke lockup final.

**Batasan:** Tidak boleh menaruh semua 10 konsep sekaligus pada satu shot; jangan ganti warna background menjadi gelap penuh; jangan jadikan robot maskot sebagai TTS otomatis; hindari gerak “floating” tanpa sebab. Satu scene harus dapat dipahami dalam screenshot diam.

## Highlight/pacing yang diinginkan

- **Peak 1:** hook 0–3s (kegagalan visual langsung bisa dipahami).
- **Peak 2:** ML–neural–LLM bertransformasi seamless sekitar tengah video.
- **Peak 3:** RAG physical retrieval, wajib shot paling detail dan memuaskan.
- **Peak 4:** agent loop dengan decision gate, menunjukkan agency secara terbatas.
- **Peak 5:** production beauty shot + full recap dan CTA.

**Re-timing rule:** jangan mengejar perkiraan timecode sampai mengubah kecepatan VO. Ukur durasi final, jalankan transkripsi multilingual Indonesia atau forced alignment, anchor tiap scene ke frase, lalu skala beat antarscene dengan kurva waktu lokal. Durasi akhir = akhir VO + ±0.3 detik visual hold, dalam kelipatan frame.
