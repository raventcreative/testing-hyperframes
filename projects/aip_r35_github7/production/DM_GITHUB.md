# DM · GITHUB — 7 aplikasi AI open-source yang jalan di laptop sendiri

Halo! Ini link yang aku janjiin di reel. Semua repo di bawah aku cek langsung README-nya di GitHub (24 Nov 2026).
Semuanya gratis & open-source — yang perlu kamu siapkan cuma laptop/PC yang cukup kuat (catatan spek di tiap poin).

1. **Jan** — https://github.com/janhq/jan
   Pengganti ChatGPT yang open-source: download model AI (Llama, Gemma, Qwen, dll.), lalu chat langsung di laptop. Bisa sepenuhnya lokal (opsional bisa juga sambung ke model cloud).
   Windows, macOS, Linux · Lisensi Apache-2.0.
   Spek (README): macOS 13.6+ — RAM 8 GB untuk model 3B, 16 GB untuk 7B, 32 GB untuk 13B; Windows 10+ dengan GPU NVIDIA/AMD/Intel Arc.

2. **Upscayl** — https://github.com/upscayl/upscayl
   Perbesar & pertajam foto resolusi kecil pakai AI (cocok buat foto produk). Catatan README: tidak bisa memperbaiki foto yang out-of-focus/blur total.
   Windows 10+, macOS 12+, Linux · Lisensi AGPL-3.0.
   Spek: butuh kartu grafis (GPU) yang mendukung Vulkan — banyak GPU bawaan (iGPU) tidak jalan.

3. **Buzz** — https://github.com/chidiwilliams/buzz
   Transkrip & terjemahkan audio/video secara offline, mesinnya Whisper dari OpenAI. Ekspor ke TXT, SRT, VTT (subtitle).
   Windows, macOS (Apple Silicon), Linux · Lisensi MIT.
   Spek (README): akselerasi opsional lewat GPU NVIDIA (CUDA), Apple Silicon, atau Vulkan (termasuk banyak GPU bawaan).

4. **Ultimate Vocal Remover (UVR)** — https://github.com/Anjok07/ultimatevocalremovergui
   Pisahkan vokal dan musik dari file audio (jadi dua file terpisah). Berguna buat ngolah audio konten.
   Windows 10+, macOS Big Sur+, Linux · Lisensi MIT.
   Spek (README): untuk proses pakai GPU minimal NVIDIA GTX 1060 6 GB, disarankan GPU NVIDIA dengan VRAM 8 GB+.
   Catatan: pakai hanya untuk audio yang kamu punya haknya.

5. **Chatterbox** — https://github.com/resemble-ai/chatterbox
   Model text-to-speech open-source: ketik naskah, keluar suara (voice over).
   Catatan jujur (README): bahasa Indonesia **belum ada** di daftar 23 bahasanya, dan sejak Agustus 2026 proyek ini **retired / tidak di-maintain lagi** (kode tetap tersedia, lisensi MIT). Setiap audio yang dihasilkan diberi watermark tak terdengar (PerTh).
   Instal lewat Python (`pip install chatterbox-tts`); paling nyaman dengan GPU.

6. **Meetily** — https://github.com/Zackriya-Solutions/meetily
   Asisten meeting: rekam, transkrip real-time, lalu ringkasan otomatis — audio & transkripnya tetap di perangkatmu (ringkasan pakai model lokal secara default).
   Windows (x64), macOS (Apple Silicon), Linux · Lisensi MIT. Ada versi PRO berbayar, tapi Community Edition gratis.
   Spek: Windows butuh CPU x64 dengan AVX2; Linux x86_64 (glibc 2.35+).

7. **ComfyUI** — https://github.com/Comfy-Org/ComfyUI
   Bikin gambar, video, audio, sampai 3D pakai AI dengan menyambung blok-blok node. Bisa jalan offline.
   Windows, macOS, Linux (ada Comfy Desktop) · Lisensi GPL-3.0.
   Spek: makin besar modelnya, makin butuh GPU & RAM. README menyebut model besar bisa jalan mulai dari 4 GB VRAM + 8 GB RAM, tapi hasil & kecepatan sangat tergantung GPU-mu.

## Mulai dari mana?
- Mau chat AI tanpa kirim data ke luar → **Jan**.
- Foto produk kecil/burik dari supplier → **Upscayl**.
- Bikin subtitle konten/podcast → **Buzz**.
- Rapat tim tiap minggu → **Meetily**.
- Mau eksplor gambar/video AI lokal → **ComfyUI** (siapkan GPU).

Catatan: cek dulu spek laptop kamu sebelum download model besar, dan selalu download dari link resmi di atas.
