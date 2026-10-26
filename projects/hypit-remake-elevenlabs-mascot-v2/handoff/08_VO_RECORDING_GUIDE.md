# VO ElevenLabs — sumber audio INCLUDED (V3)

## Status audio

Audio ElevenLabs dari Freddie **sudah disalin ke ZIP** sebagai `assets/vo_elevenlabs_final.mp3`. Metadata yang berhasil diperiksa: MP3 mono, sample rate 44.100 Hz, durasi 61.07425 detik. Tidak perlu ekspor atau upload audio lagi. Gunakan file ini sebagai **satu-satunya voice-over** pada proyek final dan lakukan word alignment terhadap isi file sebenarnya di Claude Code.

## Jika Freddie ingin re-record di masa depan (opsional)

1. Salin **hanya isi** `07_VO_ELEVENLABS_READY.txt` ke ElevenLabs. File tersebut naskah final; jangan menambahkan judul, timecode, atau petunjuk panggung ke kotak teks TTS.
2. Pilih suara Bahasa Indonesia laki-laki yang natural, semi-formal, energik tapi tidak seperti iklan hard sell. Pace kira-kira 145–160 kata/menit; berikan jeda singkat setelah hook dan sebelum CTA. Hindari emosi hiperbola, pitch berubah drastis, dan efek suara robotik.
3. Ekspor audio berkualitas tinggi sebagai MP3 atau WAV. Jika ingin mengganti sumber VO yang sudah ada, lakukan secara eksplisit dan perbarui word timing serta storyboard. Jangan menimpa diam-diam versi lama saat proyek sudah dibuat.
4. Dengarkan kembali pengucapan `Hypit` (nama produk), `GitHub`, `Claude Code`, `B-roll`, dan `HYPIT` pada CTA. Jika salah ucap, revisi pronunciation/pengaturan suara dan ekspor ulang sebelum lanjut.
5. Untuk VO yang sudah terlampir, langsung buka Claude Code di folder hasil extract ZIP dan tempel *seluruh* `01_CLAUDE_CODE_EXECUTION_PROMPT.txt`.

## Catatan produksi

- Panjang file media saat diperiksa adalah **61.07425 detik**. Transkrip, pause, detail onset tiap kata dan ending sebenarnya belum di-review manual, sehingga timecode scene masih harus dibuat Claude Code dari file.
- Audio sumber (`assets/voice_source_full.m4a`) disediakan untuk inspeksi sumber saja. **Jangan pernah dimasukkan ke timeline V2.**
- No BGM. Tambahkan SFX lembut hanya jika tidak mengganggu VO.
- File sudah tersedia, jadi Claude Code dapat melakukan alignment dan preview. Jika tidak bisa memproses media, laporkan blocker yang nyata. **Render final tetap menunggu approval Freddie** setelah melihat preview.
