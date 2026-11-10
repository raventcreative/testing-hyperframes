---
tags: [aipreneur, reel, remake, hyperframes, elevenlabs, batch, claude-code]
date: 2026-11-10
project: projects/plugin4_2026
---
# Reel: 4 plugin sebelum vibe coding pakai Claude Code · NAVY

- **Referensi**: "Jangan mulai vibe coding pakai Claude Code sebelum pasang 4 plugin ini" (wireframe hitam-putih, kotak isometrik, maskot pixel oranye).
- **Versi kita**: 46,1 s, navy, CTA **Komen SETUP**. Urutan diacak: Superpowers → Karpathy Skills → Caveman → Codex.
- **Fakta (README resmi, dicek 10 Nov 2026)**: obra/superpowers (MIT, ±315 rb ★ → tampil "300K+"), multica-ai/andrej-karpathy-skills (1 file CLAUDE.md, 4 aturan), JuliusBrussee/caveman (Apache-2.0, contoh README 63 → 20 token, teks contoh dipakai persis), openai/codex-plugin-cc (Apache-2.0, `/codex:review`). Nama repo = teks, tanpa logo GitHub/OpenAI.
- **Sistem visual**: **PLUGIN DOCK** persisten (`compositions/dock.html`) — 4 slot cartridge di bawah logo, tiap ronde kartu cartridge besar terbang masuk slotnya tepat di F = kata nama + 0,6 s.

## Alur
1. s01 — terminal "Claude Code" ngetik "bikinin aplikasi kasir…", tombol "▶ VIBE CODING" distempel "TAHAN DULU", 4 outline plugin terbang ke dock.
2. r1 Superpowers — slot kosong jadi cartridge → dock; counter ★ 0 → 300K+; jalan pintas "langsung ngoding" diblok; pipeline Tanya → Rencana → Tes (merah) → Jalan (hijau).
3. r2 Karpathy — 15 file → tinggal 1 CLAUDE.md → editor 4 aturan (judul asli) + visual mini tiap aturan → mati ala TV.
4. r3 Caveman — jawaban panjang 63 token dijepit, kata kunci terbang ke jawaban caveman 20 token, "=" badge "isinya tetap sama".
5. r4 Codex — "=" jadi mata Codex, cartridge hijau, segel "resmi · OpenAI", `/codex:review`, 3 komentar review, badge "Claude ✓ Claude" dicoret → "Reviewer: Codex".
6. s06 — badge jadi kolom komen, kartu "Link + cara pasang" (4 plugin), SETUP diketik, pesawat ke DM.

## Pelajaran teknis
- Layer persisten yang dicat DI ATAS scene (dock) bisa nutupin elemen scene yang mendarat → slot kosong harus fade 0,17 s sebelum kartu masuk.
- Kontrak serah-terima pakai angka pasti (F[k], rect slot) + "spec card" di komentar r1 → agen r2–r4 nyalin 1:1.
Output: `out/PLUGIN4_1080x1920.mp4` · cover `thumbnail/COVER_PLUGIN4_1080x1920.png`.
