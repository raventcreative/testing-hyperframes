# NOTES — R22 · Agent AI di server klien: checklist AMAN (LIGHT) · `projects/aip_r22_amanagent/`

1080×1920 · 30 fps · **46.57 s** (1397 frames) · VO 45.04 s file (speech 0.08–44.80 s in the file) starting at 0.30 s · HyperFrames 0.8.186.
Kit: `aip_r20_freellm` (LIGHT, glances disabled; `out/` not copied; R20's own scenes, vendor kit, DM and cover removed/replaced). Not rendered
(the lead renders), not committed. Reference: `projects/aip_remake_batch6/refs/ref2.mp4` (178 s, Indonesian, another creator). CTA keyword
**AMAN**; DM hand-out: `production/DM_AMAN.md`. Sources + ATM: `production/VO_SCRIPT.md`. `.gitignore` in this folder: `out/`, `.hyperframes/`.

## Pipeline (all re-runnable, run from this folder)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3`
   (NO --tags → client's auto tags: `[playful] [excited]` on every line + `[curious]` on the hook question, `[confident]` on the CTA)
   → `assets/audio/vo.mp3` + `vo.json`. **Take 1, the only take (45.04 s, 707 characters)** — whisper small + medium check in VO_SCRIPT.md.
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the ElevenLabs character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (scene cuts, caption chunks, styles). FIXI shows the
   spoken `"Kemarin … saya?"` with curly quotes, `audit-d` as **auditd**, `aman,` as **AMAN,**.
4. `python3 -I tools/scenes.py .` → `vendor/scenes.js` · `python3 -I tools/build_index.py .` → `index.html` (captions, logo, grid, grain,
   **phase rail**).
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −31.7 LUFS vs VO −17.3 LUFS). No music (lead adds it).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_AMAN_1080x1920.png` (default URL http://127.0.0.1:8952/proj/thumbnail/cover.html:
   any static server on :8952 whose root contains this folder as `/proj/`, or set `COVER_URL`).

## Shared visual system — `vendor/r22kit.js` (window.K) + `vendor/r22icons.js` (lucide-static 0.460, ISC)
The reel's own structure device: a **three-act checklist — SEBELUM · SELAMA · SESUDAH agent kerja** (7 items). From s03 to s10 a **phase rail**
(index.html, y 308–364 under the logo) shows the active act (navy) and fills one green dot per item on its key word (sudo · awal · yolo ·
ask · jamnya · jejaknya · ubah); a finished act turns its number into a check. It leaves at the CTA.
- `K.hd` card header, `.k-cmd` navy command strip (Poppins only), chips/stamps/footnotes, `K.boot(ID)`: seek-safe scale shorthand;
  **every initial state pinned at 0 in a nested timeline P0 that is the first child at 0**; fromTo without immediate render; word lookup
  that throws on a missing word (and on a word outside the scene); typed text with caret; `done()` = end marker + backward-seek patch +
  **`tl.render(0, true, true)`** + registration. index.html (captions, rail, logo, grid, grain) and s11 use the same rule.
- No brand logos anywhere (Hermes Agent, OpenCode, auditd, git, Ubuntu are text only + generic lucide icons). Every command and setting on
  screen is the real one from the official docs; names, files, times and log lines are illustrative and labelled CONTOH where it matters.

## Scenes (global s)
| id | start–end | VO | visual |
|---|---|---|---|
| s01 | 0.00–5.47 | Klien nanya: "Kemarin AI-nya ngapain aja di server saya?" Kamu punya buktinya? | chat card "Klien · toko online" (CONTOH) on screen from frame 0 with typing dots; "Kemarin": the question pops as a big bubble; "Kamu punya": card "Bukti kerja agent" (JAM · AKUN · PERINTAH) slides in EMPTY, "— belum ada catatan sama sekali —"; "buktinya?": stamp KOSONG + shake |
| s02 | 5.47–10.10 | Ini checklist tiga babak: sebelum, selama, dan sesudah agent kerja. | clipboard "CHECKLIST AMAN · Agent di server klien" with three dashed slots; "tiga": pill "3 babak"; each act's column opens on its word with its items + empty checkboxes (Sebelum 4 · Selama 2 · Sesudah 1); end: clipboard drops, the phase rail slides in |
| s03 | 10.10–14.73 | Sebelum: agent dapat akun sendiri, bukan admin, nggak masuk grup sudo. | access badge on a lanyard swings in ("KARTU AKSES · agent · akun biasa · folder: web klien saja"); `$ sudo adduser agent` types; master-key card "admin / root · cuma kamu yang pegang" dims + red chip "bukan buat agent"; card "GRUP SUDO = akses penuh": "kamu (admin) anggota", agent row "ditolak" + shake; badge row "grup sudo" gets ✗; rail dot 1 |
| s04 | 14.73–18.10 | Commit dulu folder webnya ke git, biar ada titik awal. | folder card "/var/www/toko" (contoh files); "Commit": camera flash + snapshot polaroid "Snapshot: sebelum agent · commit tersimpan di git" slides out and is pinned; `$ git add -A && git commit -m "sebelum agent"` types; timeline: flag "titik awal" plants, "agent kerja di sini →"; rail dot 2 |
| s05 | 18.10–22.10 | Di Hermes, set approvals ke manual, jangan pernah nyalain yolo. | selector "HERMES AGENT · ~/.hermes/config.yaml · approvals.mode": smart (bawaan) · manual · off; `$ hermes config set approvals.mode manual` types; knob slides to manual; Hermes' approval prompt (contoh `rm -r gambar/lama`, once/session/always/deny); "jangan … yolo": `--yolo`, `/yolo`, `mode: off` struck through + stamp JANGAN; rail dot 3 |
| s06 | 22.10–26.43 | Di OpenCode, setelan awalnya serba boleh, jadi ubah permission-nya ke ask. | toll-gate card "OPENCODE · opencode.json · permission": lanes bash / edit / webfetch with raised arms + green "allow" + tag "BAWAAN: HAMPIR SEMUA ALLOW"; "ubah … ask": arms drop, pills turn amber "ask"; lane "bash: rm *" closes red "deny" + shake; config types; footnote "taruh di /etc/opencode/opencode.json — milik root, agent nggak bisa ngubah"; rail dot 4 |
| s07 | 26.43–30.90 | Selama: auditd merekam semua perintah akun agent, plus jamnya. | rail → SELAMA; receipt printer "LINUX · SERVER KLIEN · auditd" with blinking REKAM; the receipt "STRUK PERINTAH · akun: agent · contoh" prints line by line (09.12 ls … / 09.13 nano index.html / 09.15 cat .env + amber flag "kok buka .env?" / 09.16 git status); ring on the time column on "jamnya"; rule `-a always,exit -F arch=b64 -S execve -F uid=agent -k agent` types; rail dot 5 |
| s08 | 30.90–34.17 | Log-nya milik root, jadi agent nggak bisa hapus jejaknya. | vault card "LOG AUDIT DI SERVER · /var/log/audit/"; the receipt slides into its tray; chip "pemilik: root"; padlock snaps shut; the agent's eraser flies in and bounces off + ✗; terminal `$ rm /var/log/audit/audit.log` → `rm: cannot remove '/var/log/audit/audit.log': Permission denied`; chip "jejaknya tetap utuh"; rail dot 6 |
| s09 | 34.17–38.73 | Sesudah: git status dan git diff nunjukin file dan baris yang dia ubah. | rail → SESUDAH; card "git status": index.html DIUBAH, backup.sql FILE BARU "nggak kamu minta?"; compare card "git diff index.html": SEBELUM `<h1>Promo Lebaran</h1>` | handle | SESUDAH `<h1>Promo Akhir Tahun</h1>`; rings on "file" and "baris"; `$ git restore index.html  # nggak diminta? balikin` types; rail dot 7, all three acts checked |
| s10 | 38.73–43.07 | Ingat, larangan di prompt itu bukan pagar. Pagarnya harus di sistem. | left card "LARANGAN DI PROMPT · cuma kalimat": sticky note "Jangan hapus database ya." — the agent's red action passes through a dashed "pagar?" outline to the database (✗), stamp BUKAN PAGAR, chip "AI bisa salah paham"; right card "PAGAR DI SISTEM · dicek mesin": planks akun bukan admin / approvals · ask / log milik root rise between posts, the action bounces off a solid wall, database ✓, chip "tertahan sebelum kejadian" |
| s11 | 43.07–46.57 | Komen AMAN, aku kirim lewat DM. | package card "DIKIRIM LEWAT DM · Checklist AMAN · perintah + config siap salin · 7 langkah"; comment types AMAN, heart, send → plane; DM bubble "Checklist AMAN + perintahnya / akun, auditd, git, Hermes, OpenCode", "terkirim"; end: AI PRENEUR logo + glint |

Robot (co-host, right): flies in on "Kamu punya buktinya?" and thinks, nods through the checklist, points at the badge, shakes its head on
"bukan admin", "sudo", "jangan … yolo", "nggak bisa", "bukan pagar"; TYPES on its holo keyboard for commit, the OpenCode config and git status;
scans the receipt and the diff; small shock on "yolo" and "hapus"; cheers on "ask", "jejaknya", "sistem" and the CTA; waves at the end.
Mascot (host, left): an intent on every beat (present / question / explain / emphasize / compare / cta); **glances disabled**
(`const glance = (t) => 0;`). All robot/mascot word lookups were checked against timing.json (none missing).

## QA (real runtime: `npx --yes hyperframes@0.8.186 snapshot` + `validate`)
Sheets (JPG only, PNG dumps deleted) in `/tmp/claude-0/-home-user-testing-hyperframes/a8ae6177-e310-5942-a663-2ca4db15bda7/scratchpad/r22/`:
- **Full pass qa1, 76 frames** (first frame, every scene 4–6×, every cut ±0.03 s, last frame 46.53): labelled sheets `qa1_sheet_a.jpg`
  (0–10.13 s) · `qa1_sheet_b.jpg` (10.6–20.2) · `qa1_sheet_c.jpg` (21.0–29.6) · `qa1_sheet_d.jpg` (30.5–38.7) · `qa1_sheet_e.jpg`
  (38.76–46.53) + the tool's own `qa1/contact-sheet-1…9.jpg`; mascot/robot eyes close-up `qa1_eyes.jpg` (0, 4.5, 10.6, 19.4, 27.8, 33.1,
  41.0, 46.53 s: pupils/irises present everywhere; at 0 s the mascot is in its settle, at 4.5 s it squints on the question — eyes not blank).
- Found in qa1 and fixed: (1) active rail pill showed a blank white number circle (white digit over the light inactive circle) → the inactive
  number + label now fade out while a pill is active; (2) s06 raised barrier arms read as stray stubs → open lanes show no arm, the arm swings in
  on "ask"; (3) s01 exit left the hero empty ~0.25 s before the cut → exit 0.08 s later; (4) s02 clipboard still overlapped the incoming rail →
  exits 0.16 s earlier; (5) s03 command strip showed an empty box before typing → pop + typing synced.
- **Fix pass qa2** (13 frames: 5.2, 5.437, 9.6, 9.85, 10.13, 11.75, 12.2, 23.5, 25.2, 26.1, 29.6, 36.5, 39.3 s): `qa2_sheet.jpg` (+ `zoom_c.jpg`
  rail/arms close-up) — all clean. `validate` then flagged 5 WCAG contrast notes (light grey #9aa7c0 small text in s01) → all small grey text
  in s01–s10 now #5d6f8f; **`validate` again: 0 errors, 0 contrast warnings** (warnings left = kit "multiple instances of Three.js" + software-GL
  "GPU stall due to ReadPixels"). **qa3** (0, 4.66, 25.0, 25.3, 46.53 s, `qa3_sheet.jpg`) confirms the last edits.
- `lint`: 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the kit).
- Dev-preview sheets used while building (not the real runtime): `dev_s01.jpg` … `dev_s11.jpg`; text-overflow checker `tools/overflow.cjs`
  (every text element inside its card and inside the hero zone at each scene's fully built moment: clean; the rotated KOSONG stamp was moved
  inside its card); caption-width check `tools/capw.cjs` (all 36 caption chunks ≤ 869 px of the 940 px caption box → one line each).
- Every initial state is pinned at 0 in the nested P0 timeline (scenes, captions, rail); scene words throw if missing; all robot/mascot word
  lookups exist in timing.json.

## Known issues / notes for the lead
- Duration 46.57 s (speech ≈ 44.7 s, within 35–48 s; ~1.4 s end card after "DM."). VO is the only take (no re-take, ≈ 707 ElevenLabs
  characters used).
- Captions: during the 0.34 s word rise a chunk can show part of a word for a frame (kit caption system). The last chunk ("aku kirim lewat
  DM.") stays up over the end card (same as R8/R12/R20).
- "auditd" is spoken "audit-D" (written "audit-d" for the TTS; caption shows auditd). "git diff" is pronounced correctly (checked with English
  whisper); Indonesian whisper spells it "Git Div".
- Facts are from the official docs (13 Nov 2026). hermes-agent.nousresearch.com and opencode.ai are blocked by this sandbox's proxy, so their
  docs were read from the source files in the official GitHub repos (website/docs/… and services/site/src/docs/…), same content.
- OpenCode now has V1 (`opencode-ai` 1.19.5) and V2 (`@opencode/cli` 2.3.0): the screen shows the V1 `permission` keys (still read by V2 per its
  migration guide); the DM gives the optional native V2 `permissions` array too.
- Hermes `approvals.mode: manual` asks only for commands on Hermes' dangerous-pattern list (said on screen: "perintah bahaya: tanya kamu" and in
  the DM), not for every command.
- Illustrative content (client chat, /var/www/toko files, 09.xx log lines, Promo Lebaran diff, backup.sql) is labelled CONTOH / contoh on screen.
- The robot types on its holo keyboard at three beats (commit, OpenCode config, git status) by design. No music (lead adds it).
- `.hyperframes/` in this folder is created by the CLI (lint/validate/snapshot) and is git-ignored.

## Assets
Poppins 400/700 (OFL, `assets/fonts/OFL-Poppins.txt`) · lucide-static 0.460.0 icons (ISC, `assets/icons/LICENSE-lucide.txt`, inlined in
`vendor/r22icons.js`) · AI PRENEUR logo, background, robot and mascot = the client's own kit assets (copied from `aip_r20_freellm`) ·
SFX synthesised by `tools/sfx.py` (no samples) · VO: ElevenLabs, the client's saved voice. No third-party logos or screenshots.
