# COLIBRI — link repo + tabel model per ukuran RAM

Makasih udah komen COLIBRI! Ini link-nya plus tabel buat milih model sesuai RAM PC kamu.
Semua angka di bawah diambil dari README resmi repo-nya (dicek 28 November 2026). Repo ini terus di-update, jadi cek lagi README-nya
sebelum download.

**Repo:** https://github.com/JustVugg/colibri  ·  lisensi **Apache-2.0** (gratis & open source)
Website: https://justvugg.github.io/colibri

## Apa itu Colibri (versi singkat)
- Mesin kecil berbahasa C buat jalanin model AI besar jenis *mixture-of-experts* (MoE) di komputer yang kamu punya.
- Model MoE isinya banyak "ahli" kecil; tiap token cuma sebagian kecil yang kerja. Bagian yang selalu dipakai (inti model) disimpan
  di RAM, ahli-ahli lainnya tetap di SSD dan dibaca saat dibutuhkan. Ahli yang sering dipakai disimpan di cache (RAM, atau GPU kalau
  ada), jadi makin sering dipakai makin cepat.
- Posisi ahli (GPU / RAM / SSD) cuma ngaruh ke kecepatan, bukan ke modelnya: bobot dan keputusan router-nya tetap sama.
- GPU opsional. Semua engine bisa jalan di CPU saja.

## Minimal PC (README)
- RAM **8 GB** paling sedikit (16 GB atau lebih lebih enak)
- Disk kosong **22 GB** untuk model paling kecil
- Internet buat download; kartu grafis opsional
- Windows, macOS, Linux

## Tabel model per ukuran RAM
RAM = dua angka di README: di bawah angka pertama model **nggak mau jalan**; mulai angka kedua jalan seperti yang diukur di README.

**Model kecil (jalan dari RAM)**
| Model | `--model` | Download | RAM (min / nyaman) | Catatan |
|---|---|---|---|---|
| Inkling-2-Mini UD-IQ2_XXS | `inkling2-mini-iq2` | 9 GB | 4 / 12 GB | chat, gambar, tools (versi 2-bit) |
| Inkling-2-Mini UD-Q4_K_XL | `inkling2-mini` | 18 GB | 6 / 21 GB | chat, gambar, tools |
| **Qwen3-Coder-30B-A3B** | `qwen3-coder-30b` | 19 GB | **8** / 18 GB | khusus coding & tool calls |
| Qwen3.6-35B-A3B | `qwen36-35b` | 23 GB | 10 / 20 GB | chat dengan thinking & tools |
| Qwen-Image-2.1 | `qwen-image-2.1` | 33 GB | 12 / 18 GB | teks jadi gambar, **lisensi non-komersial** |

**Model besar (ahli di-stream dari SSD — SSD cepat/NVMe paling membantu)**
| Model | `--model` | Download | RAM (min / nyaman) |
|---|---|---|---|
| DeepSeek V4 Flash REAP 150B | `deepseek-v4-flash-reap` | 85 GB | 16 / 32 GB |
| **DeepSeek V4 Flash** (284B) | `deepseek-v4-flash` | 167 GB | **16** / 32 GB |
| Qwen3.8-Flash-Next UD-IQ2_XS | `qwen38-flash-next-iq2xs` | 80 GB | 16 / 54 GB |
| Qwen3.8-Flash-Next UD-IQ3_XXS | `qwen38-flash-next-iq3` | 88 GB | 16 / 62 GB |
| GLM-5.2 (744B) | `glm-5.2` | 429 GB | 16 / 24 GB |
| GLM-5.3 (744B) | `glm-5.3` | 419 GB | 16 / 24 GB |
| Qwen3.8-Flash-Next (125B + 51B n-gram) | `qwen38-flash-next` | 186 GB | 24 / 32 GB |
| MiMo-V2.6 Flash (309B) | `mimo-v2.6-flash` | 172 GB | 32 / 52 GB |
| **Kimi K3** (2.8T) | `kimi-k3` | 1,56 TB | **32** / 64 GB |
| Kimi K3.1 Pro (2.8T) | `kimi-k3.1-pro` | 1,56 TB | 32 / 64 GB |
| MiMo-V2.6 Pro (1.02T) | `mimo-v2.6-pro` | 564 GB | 54 / 64 GB |

**Contekan cepat**
- RAM 8 GB → Qwen3-Coder-30B (coding) atau Inkling-2-Mini versi 2-bit.
- RAM 16 GB → semua model kecil di atas; model besar seperti DeepSeek V4 Flash *bisa start*, tapi pelan.
- RAM 32 GB → DeepSeek V4 Flash lebih nyaman; Kimi K3 bisa start (butuh SSD 1,56 TB).
- Bingung? Jalankan setup dengan `--list`: dia nunjukin semua model dibanding PC kamu, plus kenapa yang nggak cocok.

## Jujur soal kecepatan & SSD (angka README)
- Model besar itu pelan, kecepatannya ditentukan disk. Contoh: DeepSeek V4 Flash **0,93 token/detik** (Ryzen 7 5800X, RAM 32 GB,
  CPU saja); Kimi K3 sekitar **9,4 detik per token**.
- Ukuran download model besar ratusan GB sampai 1,56 TB. Pastikan SSD-nya lega (pakai `--dir` buat taruh model di disk lain).
- Kalau mau yang lancar buat kerja harian, mulai dari model kecil (misalnya Qwen3-Coder-30B: 8,5–9,6 token/detik di CPU saat semua
  ahlinya muat di RAM, angka README).

## Cara pasang (langkah dari README)
**Windows**
1. Buka halaman repo → **Code** → **Download ZIP** → unzip.
2. Klik dua kali **`START-HERE.bat`**. Kalau Python belum ada, dia nawarin install.

**Linux (Ubuntu/Debian)**
```bash
sudo apt install git python3 build-essential
git clone https://github.com/JustVugg/colibri
cd colibri
./start-here.sh
```

**macOS (pakai Homebrew)**
```bash
xcode-select --install
brew install libomp git python
git clone https://github.com/JustVugg/colibri
cd colibri
./start-here.sh
```

Setup-nya: ngecek PC kamu (RAM, disk kosong, CPU, GPU) → ngerekomendasiin model (tekan Enter buat ambil rekomendasi) → nyiapin
engine → download model (bisa dilanjut kalau putus) → buka chat di browser (`http://127.0.0.1:8000/`).
Opsi berguna: `--list`, `--model ID`, `--yes`, `--dir DIR` (simpan model di disk lain), `--no-gpu`.
Lain kali tinggal jalankan `START-HERE.bat` / `./start-here.sh` lagi.

## Catatan penting
- Tiap model punya lisensi sendiri dari pembuatnya (contoh: Qwen-Image-2.1 cuma untuk non-komersial). Cek sebelum dipakai buat bisnis.
- Download model besar makan kuota dan waktu; pakai koneksi yang stabil.
- Simpan model di SSD internal (di WSL, jangan di `/mnt/c` — README bilang jauh lebih lambat).
