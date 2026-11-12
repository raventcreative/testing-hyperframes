# VO — Tes ide bisnis ke 100 pembeli AI · background TERANG · 48,4 dtk VO (video 49,70 dtk)
Referensi: ref1 (46 dtk) — "Founder", 11 skill Claude gratis: dewan direksi (Hormozi, Thiel, Jobs), CFO yang mencari margin asli, dan
panel konsumen berisi pembeli AI (penghasilan, kebiasaan, keraguan masing-masing). Contohnya mobil cuci/detailing $89: "cuma 3 dari 20
yang beli", CFO bilang angkanya masuk, pembeli bilang "belum". Ditutup "mereka simulasi, tes pemenangnya ke orang beneran", CTA
"comment FOUNDER". Visual referensi: palet krem/oranye, maskot kepiting piksel, orang-orang piksel.

## Yang diubah dari referensi
- Visual sepenuhnya milik kita: sistem LIGHT AI PRENEUR (grid animasi, kartu putih, judul gradasi navy, maskot + robot). Panel = 100
  avatar bulat (20 × 5) yang dipakai ulang di s01/s05/s06/s08/s10 — bukan orang piksel, bukan kepiting, bukan palet krem/oranye.
- Sudut Indonesia: "tes ide sebelum keluar modal". Contoh bisnis lokal: **katering makan siang kantor, Rp25.000/porsi** (bukan van
  detailing $89). Semua angka contoh diberi label **CONTOH / CONTOH SIMULASI** di layar dan konsisten satu sama lain:
  - per porsi: Rp25.000 − bahan Rp11.000 − kemasan Rp2.000 − ongkir kurir Rp3.000 = **sisa Rp9.000** → margin asli 9.000/25.000 = **36 %**
  - biaya tetap Rp3,6 jt/bulan ÷ Rp9.000 = 400 porsi/bulan ÷ 20 hari kerja = **balik modal 20 porsi/hari**
  - panel: **18 dari 100** mau beli; 82 belum = 34 ("bawa bekal dari rumah") + 29 ("warteg lebih murah") + 19 ("takut telat sampai")
  - persona pembeli AI (Rina 27, Dimas 31, Sari 35) fiktif, ditandai "PEMBELI AI" + "CONTOH SIMULASI".
  VO membingkainya sebagai contoh ("Contohnya, …") — tidak ada "aku coba" atau hasil nyata.
- Dewan direksi digambarkan sebagai **kerangka berpikir dari buku** ($100M Offers, Zero to One, biografi Isaacson), bukan orangnya:
  tanpa wajah/foto tokoh; di layar "kerangka dari buku, bukan orangnya" (sesuai fine print README).
- Poin jujur dari referensi dipertahankan dan diperkuat: "panelnya simulasi" + catatan di layar "angka beli = batas atas, bukan
  ramalan" (README: buy rate = upper bound, bukan forecast) → "ide yang menang, tes lagi ke pembeli beneran" (/founder-launch mulai dari
  tes kecil di dunia nyata).
- Tidak ada janji untung, tidak ada angka hasil nyata. Kalimat "Mending dengar ini sekarang, daripada setelah beli peralatan dapur" =
  versi lokal dari "better to hear that before you buy the van" (keranjang peralatan tanpa harga, stempel TAHAN DULU).
- CTA: "Komen FOUNDER, aku kirim lewat DM." (isi DM: link repo + urutan pakainya).

## Fakta yang dicek (2026-11-12) — sumber resmi: README repo
Sumber utama: https://github.com/Jakeschincariol/founder-skill (README dibaca langsung dari
https://raw.githubusercontent.com/Jakeschincariol/founder-skill/main/README.md, 2026-11-12).
- Nama: **Founder** ("The Founder skill"), oleh Jake Schincariol. "Eleven Claude skills that test a business before you launch it.
  Free, MIT, no signup, no API key, nothing to connect." → **11 skill Claude, gratis, lisensi MIT (open source)**.
  (Referensi sempat menulis "10 free skills" di satu frame — README: sebelas.)
- 11 perintah: /founder-board, /founder-competitors, /founder-consumer, /founder-pricing, /founder-offer, /founder-cfo,
  /founder-marketing, /founder-brand, /founder-ops, /founder-launch, /founder-plan (urutan pakai di README: board → competitors →
  consumer → pricing → offer → cfo → marketing → brand → ops → launch → plan).
- **/founder-board** = dewan direksi: 3 sub-agent, masing-masing satu kerangka (Offers dari *$100M Offers* — Hormozi; Monopoly dari
  *Zero to One* — Thiel; Product dari biografi Steve Jobs karya Isaacson); memberi skor, menyebut apa yang bisa bikin gagal, lalu vote
  fund / fund if / pass. Fine print: "applies published frameworks. It is not those people … not affiliated".
  (Pertanyaan per kursi di layar — "Tawarannya bikin orang susah nolak?", dst. — adalah ringkasan kita, bukan kutipan.)
- **/founder-cfo** = CFO: unit economics, kontribusi per penjualan, **margin keuntungan asli**, break-even per hari, tahun 1, kas yang
  dibutuhkan, payback, what-if.
- **/founder-consumer** = panel konsumen: "a swarm of buyer agents (**100 by default**) … each with its own **income, habits and
  objection**", menghitung siapa beli, siapa tidak, dan kenapa.
- Fine print: "The consumer panel is simulated buyers, not customers … not a forecast … read the buy rate as an **upper bound**, and
  confirm the big calls with real people. /founder-launch starts with exactly that test."
- Pasang: tempel link repo ke Claude + "install skill", atau plugin Claude Code (`/plugin marketplace add Jakeschincariol/founder-skill`),
  atau salin folder ke `~/.claude/skills/`. Tool Python butuh Python 3.8+ (tidak disebut di VO; untuk isi DM).
- Pembanding sekunder (bukan dasar klaim): skills-hub.ai/sources/founder-skill, explainx.ai (ulasan klaim vs README).

## Naskah (dikirim ke ElevenLabs, voice tersimpan; SETIAP baris diawali tag `[playful] [excited]`)
[playful] [excited] Ide bisnis kamu bisa dites ke seratus pembeli AI dulu, sebelum keluar modal sepeser pun.
[playful] [excited] Namanya Founder: sebelas skill Claude, gratis dan open source.
[playful] [excited] Satu jadi dewan direksi, pakai kerangka berpikir Hormozi, Thiel, dan Steve Jobs.
[playful] [excited] Satu lagi jadi CFO, yang ngitung margin asli kamu.
[playful] [excited] Tapi yang paling seru: panel konsumen. Seratus pembeli AI, masing-masing punya penghasilan, kebiasaan, dan keraguan sendiri.
[playful] [excited] Contohnya, ide katering makan siang kantor, dua puluh lima ribu per porsi.
[playful] [excited] CFO-nya bilang: angkanya masuk. Tapi panelnya bilang: belum.
[playful] [excited] Cuma delapan belas dari seratus yang mau beli. Ada yang bawa bekal, ada yang bilang warteg lebih murah.
[playful] [excited] Mending dengar ini sekarang, daripada setelah beli peralatan dapur.
[playful] [excited] Ingat, panelnya simulasi. Jadi ide yang menang, tes lagi ke pembeli beneran.
[playful] [excited] Komen FOUNDER, aku kirim lewat DM.

Teks tanpa tag: `production/vo_lines.txt` (angka ditulis sebagai kata supaya dibaca benar; caption menampilkan angka: 100, 11, Rp25.000,
18). Audio: `assets/audio/vo.mp3` (+ `assets/audio/vo.json` = waktu per baris + alignment karakter). Dibuat dengan
`python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3 --tags "[playful] [excited]"`.
Cek ulang dengan faster-whisper `small`: semua kata terucap, tag tidak ikut terbaca, "Thiel" terucap benar ("Teal").
