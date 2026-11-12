# VO — Panel rekrutmen 7 Claude (CV kamu ditolak duluan) · background NAVY · 42,9 dtk VO / 44,2 dtk film
Referensi: `aip_remake_batch3/refs/ref1.mp4` (36 dtk, EN, "I built a hiring panel where seven Claudes try to reject your resume…").
Yang diubah dari referensi:
- Dibingkai untuk pencari kerja Indonesia: "ngelamar ke puluhan lowongan", email penolakan HRD tanpa alasan, "sebelum HRD yang nolak".
- Klaim referensi yang TIDAK dipakai: "unrejectable", "bulletproof resume that gets you hired", "completely free", link pihak ketiga.
  Diganti dengan baris jujur: "Ini bukan jaminan diterima, ya." (visual: sertifikat "Dijamin diterima kerja" dicoret + disobek).
- Visual & karakter sendiri (panel juri 7 kartu Claude di meja "PANEL REKRUTMEN", CV kita, tidak ada claymation / gaya referensi).
- Angka di CV versi baru sengaja jadi placeholder "angka" — Claude tidak mengarang hasil kerja kamu.
- CTA beda: "Komen CV" → kirim workflow-nya lewat DM.

Fakta yang dicek (12 Nov 2026):
- ATS (applicant tracking system) = software rekrutmen yang mengumpulkan, mengurutkan dan menyaring lamaran sebelum dibaca manusia;
  sebagian bisa menyaring/merangking berdasarkan kata kunci lowongan (tidak semua). Sumber: hasil WebSearch "applicant tracking system"
  (Tufts Career Center careers.tufts.edu, The Forage theforage.com/blog/basics/applicant-tracking-system, Jobscan jobscan.co).
  Statistik populer "75% CV ditolak ATS" TIDAK bisa diverifikasi → tidak dipakai. Di reel, ATS hanya diperankan Claude (simulasi).
- Claude bisa membaca file CV yang diunggah (PDF, DOCX, TXT, dll.): support.claude.com/en/articles/8241126-uploading-files-to-claude.
- "Baca sendiri-sendiri": di Claude Code tiap subagent jalan di context window sendiri ("Each subagent runs in its own context window"),
  jadi 5 pembaca tidak saling memengaruhi: code.claude.com/docs/en/sub-agents. Di VO tidak disebut sebagai klaim teknis.
- Tidak ada klaim "dijamin", "pasti diterima", gratis, atau angka hasil.

Produksi: ElevenLabs, voice tersimpan (`/home/user/testing-hyperframes/tools/voice_config.json`, eleven_v4), SATU panggilan via
`tools/el_tts_ts.py production/vo_lines.txt … --tags "[playful] [excited]"` → `production/vo_takes/take1.mp3` (= `assets/audio/vo.mp3`).
Setiap baris diawali tag `[playful] [excited]` (lihat `production/vo_lines.txt`; tag tidak terucap — dicek dengan faster-whisper small).
Timing kata: alignment karakter ElevenLabs take ini molor di ujung frasa (mis. "manager." 18,36–18,80 dtk padahal suara berhenti 18,40),
jadi `production/vo_words_raw.json` dibangun dari faster-whisper small (`production/vo_fw_small.json`) dengan teks naskah kita
(`tools/fw_to_words.py`), lalu `tools/timing.py` (snap ke onset suara) → `production/timing.json`. Alignment EL disimpan di
`production/vo_el_alignment.json` (+ `tools/el_to_words.py`).

## Naskah (persis yang dikirim; setiap baris = [playful] [excited] + teks)
[playful] [excited] Aku bikin panel rekrutmen isinya tujuh Claude. Tugasnya cuma satu: nolak CV kamu.
[playful] [excited] Soalnya, kamu udah ngelamar ke puluhan lowongan, tapi nggak pernah dikasih tahu kenapa ditolak.
[playful] [excited] Claude pertama jadi sistem ATS, penyaring otomatis sebelum CV kamu dibaca manusia.
[playful] [excited] Claude kedua jadi hiring manager. Kamu layak dipanggil interview, atau nggak?
[playful] [excited] Lima Claude sisanya baca sendiri-sendiri, pakai kacamata yang beda: calon atasan, sesama pelamar, sampai CEO.
[playful] [excited] Semua alasan nolaknya dikumpulin. Terus dia tulis ulang CV kamu, dengan semua catatan tadi udah dibenerin.
[playful] [excited] Ini bukan jaminan diterima, ya. Tapi kamu jadi tahu kenapa ditolak, sebelum HRD yang nolak.
[playful] [excited] Mau workflow-nya? Komen CV, aku kirim lewat DM.

Caption menampilkan "7" dan "5" untuk "tujuh"/"lima".
