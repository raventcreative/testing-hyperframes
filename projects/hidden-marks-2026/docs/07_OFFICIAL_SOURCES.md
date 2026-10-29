# Sumber fakta / koreksi editorial

## 1. Anthropic — Claude marking

https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content

- Watermark teks pada output **model-model Claude yang didukung** ditanam pada tingkat model, tidak boleh disederhanakan sebagai karakter Unicode yang bisa dikenali/dihapus universal.
- Content Credentials berstandar **C2PA** terkait **file yang didukung** seperti PNG/JPEG pada permukaan/platform yang mendukung pembuatan file.
- Pendeteksian watermark teks untuk publik masih terbatas/private preview. Tidak semua model lawas atau semua jenis file memiliki penanda yang sama.
- Ketiadaan penanda terdeteksi **tidak membuktikan** konten berasal dari manusia.

## 2. Claude Content Checker

https://claude.com/check-files

- Alat resmi untuk memeriksa file yang didukung terhadap sinyal provenance/content credentials Claude.
- **Bukan** pemeriksa universal watermark teks. Jangan membuat mockup hasil scan yang menyamar sebagai alat resmi.

## 3. OpenAI — Verify OpenAI-generated content

https://openai.com/research/verify/

- Alat memeriksa sinyal provenance OpenAI yang didukung, seperti **C2PA** dan **SynthID**, pada **gambar dan audio**. Tidak menyediakan pemeriksaan teks publik universal pada antarmuka tersebut.
- Sinyal yang terdeteksi memberi konteks asal konten; tidak selalu membuktikan seluruh riwayat pengeditan. Tidak ada sinyal ditemukan ≠ bukan AI.

## 4. OpenAI — Provenance signals

https://help.openai.com/en/articles/8912793-provenance-signals-in-openai-generated-content

- Metadata dan watermark embedded berbeda dan bisa memiliki ketahanan berbeda terhadap modifikasi. Penghapusan metadata bukan jaminan menghilangkan embedded marks.

## Yang sengaja tidak diklaim dalam remake

1. “Semua file Claude/ChatGPT pasti memiliki watermark.”
2. “Watermark AI selalu berupa Unicode tersembunyi.”
3. “Satu tool bisa menghapus 100% fingerprint AI.”
4. “Jika scanner kosong, file pasti 100% manusia.”
5. “Tool GitHub watermark remover pasti aman/efektif.”

Informasi ini untuk literasi provenance digital dan kontrol metadata pribadi, **bukan panduan menyembunyikan asal konten untuk menyesatkan audiens/klien**.
