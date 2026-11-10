---
tags: [aipreneur, reel, remake, hyperframes, elevenlabs, batch, instagram, claude]
date: 2026-11-10
project: projects/igagent_2026
---
# Reel: Claude jadi tim konten Instagram (Instagram Agent Skill) · NAVY

- **Referensi**: "Claude sekarang beneran bisa ngurusin akun Instagram" (kartu UI terang, gauge setengah lingkaran, hub-and-spoke, bar chart, HP "stop scroll", tag Rp0).
- **Versi kita**: 57,8 s, navy, CTA **Komen TIM**. Metafora baru: **Claude merekrut TIM — 13 ID badge berlanyard**, tiap skill = anggota tim (peran + /command), tiap ronde buka "meja kerja" anggotanya.
- **Fakta (README resmi `Jakeschincariol/instagram-agent-skill`, MIT, dicek 10 Nov 2026)**: 13 skill (/ig-viral, /ig-reel, /ig-profile, /ig-plan, /ig-caption, /ig-carousel, /ig-story, /ig-human, /ig-comment, /ig-reply, /ig-dm, /ig-repurpose, /ig-audit); /ig-viral ranking vs median akun; /ig-reel 3 hook dari 26 rumus; /ig-profile skor /100 rubrik 12 bagian, fix-first; /ig-plan seminggu + 10 akun buat interaksi; pasang = tempel URL repo ke Claude; **tidak posting sendiri** (semua draf). Angka di UI (×6,4, skor 64 → 86, view) = contoh.

## Alur
1. s01 — medali Claude di atas kartu profil "Instagram", 6 badge jatuh berlanyard di "tim konten", stempel GRATIS + segel "OPEN SOURCE • MIT".
2. s02 — pita lanyard ketik "Instagram Agent Skill", counter 1 → 13, TEAM WALL 5/4/4, gelombang flip nunjukin peran.
3. r1 /ig-viral — badge 1 ke header, kilat "kaget", 6 tile reel discan x-ray, leaderboard sort, #1 "×6,4 dari median".
4. r2 /ig-reel — tile #1 flip jadi sticky note ide → halaman naskah → slot machine 3 hook (26 rumus) → stempel skor.
5. r3 /ig-profile — kartu profil discan, cincin 12 segmen (bukan gauge setengah), 64/100, bagian lemah (bio) dibenerin duluan → 86.
6. r4 /ig-plan — cincin menggelinding jadi papan 7 hari (topik/format/jam), 10 avatar inisial + benang interaksi.
7. s07 — 9 badge dibagi kayak kartu di tiap katanya, badge Penghalus Tulisan menghapus frasa khas AI.
8. s08 — chat Claude: tempel link repo → "install skill ini" → "13 skill terpasang ✓" masuk folder.
9. s09 — switch auto-posting dikunci, 3 kartu distempel DRAF, tombol Posting cuma ditekan kursor "kamu".
10. s10 — kartu link, komen TIM, hati, pesawat ke DM, logo besar + 13 badge.

## Pelajaran teknis
- **Komponen bersama ditulis DULUAN** (badge di s02, ditandai "copy exactly") → 3 agen paralel konsisten.
- Tween `clip-path: polygon()` di runtime ini cuma tukar nilai awal/akhir (gak interpolasi); `inset()` aman. Polygon → `tl.set` per frame.
- End state scene sebelumnya berubah → scene berikut rusak di cut: tiap perubahan dikabarin ke pemilik scene berikutnya.
Output: `out/IGAGENT_1080x1920.mp4` · cover `thumbnail/COVER_IGAGENT_1080x1920.png`.
