# NOTES — R12 · 5 alat gratis di GitHub jadi 5 menu jasa (LIGHT) · `projects/aip_r12_cuanrepo/`

1080×1920 · 30 fps · **47.4667 s** (1424 frames) · VO 46.16 s starting at 0.30 s · HyperFrames 0.8.186. Kit: `aip_r8_web3d` (LIGHT;
`out/` not copied). Not rendered (the lead renders), not committed. Reference: `projects/aip_remake_batch5/refs/ref2.mp4` (59 s).
Serve for the cover: any static server on :8932 whose root contains this folder as `/proj/` (I used the scratch dev dir), or set
`COVER_URL`. CTA keyword **JASA**; DM hand-out: `production/DM_JASA.md`.

## Pipeline (all re-runnable, run from this folder)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3`
   (NO --tags → client's auto tags: `[playful] [excited]` on every line + `[curious]` on the hook question, `[confident]` on the CTA)
   → `assets/audio/vo.mp3` + `vo.json`. Take 3 (46.24 s); takes 1–2 were 48.8 / 49.3 s → lines tightened so the reel stays ≤ 50 s.
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the ElevenLabs character alignment).
   Checked with faster-whisper `small`: every word spoken; the voice-onset snap in timing.py matches the energy envelope (whisper runs
   ~0.2–0.4 s early on several words, the snapped times are the right ones).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (scene cuts, caption chunks, styles; FIXI shows the
   spoken lowercase "jasa," of the CTA as **JASA,**).
4. `python3 -I tools/scenes.py .` → `vendor/scenes.js` · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −31.8 LUFS vs VO −17.3 LUFS). No music (lead adds it).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_JASA_1080x1920.png` (default URL http://127.0.0.1:8932/proj/thumbnail/cover.html).

## Shared visual system — `vendor/r12kit.js` (window.K, loaded in <head>)
Metaphor: open-source code = a free RECIPE; what clients pay for = the dish = the SERVICE ("menu jasa").
- `K.recipe(p)` (recipe card "Nasi Goreng", back face = "5 resep gratis · di GitHub" list) and `K.warung(p)` (striped navy awning, own SVG
  plate of nasi goreng, "Tetap dibeli"; second state = MENU JASA board) — handed over s01 → s02 at identical positions.
- `K.head(p, i)`: per-tool "recipe" header (RESEP #n · GRATIS DI GITHUB, name, github.com/owner/repo, licence chip, n/5);
  `K.ticket(p, i)`: "MENU #n" ticket (service + who it's for); `K.headIn / ticketIn / out` (shared in/out motion); `K.boot(ID)` (scene
  boilerplate: seek-safe scale shorthand, fromTo without immediate render, initial states pinned at 0, render patch).
- `K.R`: the five verified repos (order: Postiz → AutoClip → Chatwoot → OpenHands → Remotion). Icons: lucide 0.460 (ISC). No brand logos:
  platforms are text + generic icons. All shops, chats, clients and products on screen are fictional and labelled CONTOH where relevant.

## Scenes (global s)
| id | start–end | VO | visual |
|---|---|---|---|
| s01 | 0.00–3.97 | Resep nasi goreng gratis, tapi kamu tetap beli di warung, kan? | recipe card big + centred from frame 0, ingredients tick; GRATIS stamp slams; recipe slides left, WARUNG card (awning, steaming plate) slides in; "Tetap dibeli"; awning bounce; gold "?" |
| s02 | 3.97–8.17 | Lima alat GitHub ini juga gratis, tapi klien bayar yang ngerjain. | recipe flips (flat scaleX) to "5 resep gratis" (Postiz, AutoClip, Chatwoot, OpenHands, Remotion) + green "gratis" ticks; warung clears into the MENU JASA board (5 empty lines) + "Klien bayar jasanya"; "Kamu yang ngerjain" pill + arrows recipe → kamu → menu |
| s03 | 8.17–13.30 | Satu, Postiz: jadwalin postingan banyak akun sekaligus, buat jasa kelola sosmed. | header RESEP #1 (AGPL-3.0); post card + "Senin · 09.00"; six account chips fan out with connectors; copies fly out at once, green ticks; MENU #1 "Jasa kelola sosmed" |
| s04 | 13.30–18.73 | Dua, AutoClip: video panjang jadi klip bersubtitle, buat podcaster atau seller live. | header RESEP #2 (MIT); film strip (LIVE · 01:58:42, waveform) unrolls (clip-path), playhead; 3 highlights + scissors; 3 vertical clips grow out, subtitles pop, "Podcast" ×2 + "Live jualan" badges; MENU #2 |
| s05 | 18.73–23.97 | Tiga, Chatwoot: chat WhatsApp sampai Instagram masuk satu inbox, buat jasa admin chat. | header RESEP #3 (MIT* + footnote "folder enterprise lisensinya terpisah"); WhatsApp / Instagram / Website chips; customer bubbles fly into one Inbox → rows; "3 baru"; composer types "Siap kak, masih ada!" as "Admin: kamu", tick; MENU #3 |
| s06 | 23.97–29.50 | Empat, OpenHands: agen AI yang ngoding sesuai perintahmu, buat jasa website UMKM. | header RESEP #4 (MIT); "Perintah kamu" card (CONTOH: Klinik Gigi Senyum, 3 items); agent node + connectors; code streams into index.html; checklist ticks; landing page slides over the editor; "DICEK KAMU" stamp; MENU #4 |
| s07 | 29.50–35.27 | Lima, Remotion: video dari kode, kayak reel ini. Satu template, banyak video produk. | header RESEP #5 (amber "Lisensi khusus"); code card with {nama} {foto} {warna}; pill "Reel ini juga dari kode · HyperFrames"; 9:16 template; six product videos fly into a grid; licence chip pulses; MENU #5 |
| s08 | 35.27–40.47 | Tapi gratis belum tentu bebas: Remotion wajib lisensi kalau karyawanmu lebih dari tiga. | heading word by word + "Baca label lisensinya, kayak baca label makanan."; five licence labels, magnifier sweep; Remotion label lifts (amber ring); panel "Remotion: kapan wajib lisensi?": 3 green people + GRATIS (perorangan & usaha ≤ 3 karyawan), amber 4, 5, + and WAJIB LISENSI stamp; footnote on client collaborations |
| s09 | 40.47–44.07 | Cek lisensinya, pilih satu jasa, latihan di usaha teman. | MENU JASA board returns filled (service · tool · licence chip), ticks; others dim, amber ring + cursor on #1; 3-step path: Latihan di usaha teman → Jadi contoh hasil → Baru tawarin ke klien |
| s10 | 44.07–47.47 | Komen JASA, aku kirim lewat DM. | card "5 alat gratis · link GitHub + catatan lisensinya"; comment types JASA, heart, send → plane; DM bubble "Daftar 5 alat + link GitHub / plus catatan lisensi tiap alat", "terkirim"; end: AI PRENEUR logo + glint |

Robot (co-host, right): flies in on the GRATIS stamp, points at the warung, thinks on "kan?", scans the five tools, TYPES on its holo
keyboard whenever the work is done (ngerjain, jadwalin, potong klip, admin chat, ngoding, kode), cheers results, shakes its head on
"Tapi gratis belum tentu bebas", small shock on "lebih", cheers the CTA, waves at the end. Mascot (host, left): an intent on every beat
(present / reveal / point / question on "kan?" / emphasize / cta); no glances (see QA).

## Sources (checked 2026-11-12) — details + URLs in production/VO_SCRIPT.md
github.com/gitroomhq/postiz-app (AGPL-3.0) · github.com/zhouxiaoka/autoclip + README-EN.md (MIT) · github.com/chatwoot/chatwoot + LICENSE
(MIT except enterprise/) + chatwoot.com WhatsApp setup guides · github.com/OpenHands/OpenHands (MIT) · github.com/remotion-dev/remotion +
LICENSE.md (free: individuals, for-profit ≤ 3 employees, non-profits, evaluation; else Company License) + remotion.dev license FAQ via
WebSearch (combined headcount for collaborations; remotion.dev itself is DNS-blocked here) · github.com/xiamuceer-j/MuMuAINovel (checked,
swapped out: GPL-3.0, Chinese-only README/UI). GitHub API is not enabled for this session → pages read with WebFetch.

## QA (real runtime: `npx --yes hyperframes@0.8.186 snapshot`)
Sheets (JPG only, PNG dumps deleted) in `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r12/`:
- Full pass, 78 frames (first frame, every scene 6–9×, every cut ±0.03 s, last frame 47.43): `qa1/contact-sheet-1…9.jpg` (tool sheets)
  + labelled sheets `qa1_sheet_a.jpg` (0–8.2 s) · `qa1_sheet_b.jpg` (8.7–18.7) · `qa1_sheet_c.jpg` (18.76–25.8) · `qa1_sheet_d.jpg`
  (26.6–37) · `qa1_sheet_e.jpg` (37.7–47.43).
- Fix passes: `qa2_sheet.jpg` (s02 pill, s08 stamp timing, CTA) + zoom crops `zoom1.jpg` … `zoom4.jpg` (mascot eyes, s08 panel).
- Dev-preview sheets used while building (not the real runtime): `dev_s01.jpg` … `dev_s10.jpg`; text-overflow checker
  `tools/overflow.cjs` (every text element inside its card and inside the hero zone at each scene's fully-built moment: all clean).
- `lint`: 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit). `validate` (final state): 0 errors; kit warning
  "multiple instances of Three.js"; 6 contrast notes that are intentional (dashed {foto}/{nama} placeholders before they turn blue at
  33.4 s; the dimmed, not-chosen menu rows 2–5 in s09).
- Found in the real runtime and fixed: (1) the mascot's "glance at the robot" (kit behaviour) made the eyes read blank (big white disc)
  at 1.6–2.9 s, 3.4–4.4 s and on the CTA — reducing the turn did not help, glances are now disabled (`glance = () => 0`); worth checking
  R8, whose QA sheet shows the same look at ~12.3 s · (2) the s08 "WAJIB LISENSI" stamp only held ~0.2 s before the cut → GRATIS now
  lands on "karyawanmu", the amber people + stamp on "lebih", stamp readable ~0.6 s; SFX re-synced · (3) s02 "Kamu yang ngerjain" pill
  crowded the card bottoms → moved 12 px down, arrows visible.
- Found in dev and fixed before the pass: s08 heading invisible (background-clip text on a parent of transformed spans → gradient moved
  to each word); s04 strip unroll squished its label (scaleX → clip-path); s07 tokens clipped by the code card (flight → pulses);
  contrast of the n/5 counter, footnote and chat avatars.
- Every initial state is pinned at 0 (`K.boot` → `I()`); the only hand-over is s01 → s02 (recipe + warung at identical positions,
  steam dash offset from global time) — seamless at 3.93 / 3.99.

## Known issues / notes for the lead
- Duration 47.47 s (≤ 50 s). VO is take 3; takes 1–2 were too long.
- Captions: during the 0.34 s word rise a chunk can show only i-dots / descenders for a frame (same caption system as the kit). The last
  caption chunk ("aku kirim lewat DM.") stays up to the end card (same as R8).
- MuMuAINovel (reference pick #5) was swapped for Chatwoot — reasons in VO_SCRIPT.md ("ATM: what we changed").
- Licence facts are from GitHub (12 Nov 2026). The Remotion "combined headcount for collaborations" point comes from its official
  license FAQ as surfaced by WebSearch (remotion.dev is DNS-blocked in this sandbox); it is only a small on-screen footnote + DM note.
- The DM hand-out `production/DM_JASA.md` (5 links + licence notes + start steps) is written by us; no earnings promises.
- The robot types on its holo keyboard at several beats (by design: "kamu yang ngerjain"). No music (lead adds it).
- `.hyperframes/` in this folder was created by the CLI (lint/validate/snapshot), like in the kit.
