# NOTES — R19 · Asisten suara open source di Mac (Atticus) (AI PRENEUR · NAVY)

- **Duration** 44.93 s (1348 frames @30) · VO 43.52 s starting at 0.30 s (spoken 35–45 s ✓) · CTA keyword **ASISTEN** · reference
  `aip_remake_batch5/refs/ref9.mp4` (27 s, English). Tool: **Atticus** — `github.com/SaarthurR/atticus-mac` (MIT, macOS 26+).
- **Kit**: copied from `projects/aip_r15_hermes` (newest NAVY; without `out/`, its VO/QA/cover PNG, scenes). Index built by
  `tools/build_index.py` from `production/timing.json`; shared scene kit `vendor/r19kit.js` (+ `vendor/r19icons.js`, Lucide 1.70 ISC,
  generated from lucide-static): topic header with icon roll + 8 progress segments, voice pill (mic + seekable bars + typed command),
  window-card mock, timeline boilerplate. **Initial states are pinned in a nested timeline that is the first child at 0** (`I()` →
  `P0.set`, in every scene and in the main/caption timeline via `pin()`), and every timeline ends its build with `tl.render(0, true, true)`.
  Scene lengths come from the timing via `K.dur(id)`. Audio as the batch-3/4/5 kits: `<audio id="vo" src="assets/audio/vo.mp3"
  data-start="0.3">` + `<audio id="sfx" src="assets/audio/sfx.wav">` — no music (the lead adds the ducked bed + loudness pass).
- **VO**: `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt production/vo_el.mp3`
  (NO --tags = client's AUTO tags: `[playful] [excited]` on every line + `[confident]` on the CTA; no other context tag matched), one call,
  43.60 s → `assets/audio/vo.mp3`; `tools/el_to_words.py` → `production/vo_words_raw.json`; `tools/timing.py` → `production/timing.json` +
  `vendor/vo_words.js` (PRON map updated for lip sync: Atticus, WhatsApp, Claude, Mac, …). Listen-check with faster-whisper small (id):
  every line as written (whisper spells Claude "cloud").
- **SFX**: `python3 -I tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic, no samples; key clacks, typing, snaps, flaps,
  stamp, plug seats, switches, packets, CTA; mean −35 dB vs R15 −33 dB).
- **Cover**: `thumbnail/cover.html` → `thumbnail/COVER_ASISTEN_1080x1920.png` (`python3 -m http.server 8939` at the project root, then
  `PORT=8939 node thumbnail/render_cover.cjs thumbnail/COVER_ASISTEN_1080x1920.png`). NAVY: chip "ASISTEN SUARA · OPEN SOURCE · KHUSUS MAC",
  "Suruh Mac kamu / PAKAI SUARA / Atticus · tahan 3 tombol, ngomong", the three glowing keycaps + voice pill “rapikan jendelaku, dong”,
  mascot presenting + robot typing. Key content inside the 4:5 crop (y 285–1635). No third-party logos, no Jarvis imagery.

## Scenes (global s) — hero zone y 290–935, captions y≈960–1030, hosts below
| id | start–end | VO | visual |
|----|-----------|----|--------|
| s01 | 0.00–4.83 | Tahan tiga tombol, ngomong, lepas. Mac kamu yang beresin sisanya. | headline "3 tombol, 1 kalimat." + three white keycaps (control · option · space); "Tahan": keys press down one by one + cyan glow; "ngomong": voice pill, bars, types “rapikan jendelaku, dong” (contoh); "lepas": keys spring back, pill flies off; "Mac kamu": keys/headline lift away, "MAC KAMU" desktop with 4 messy tilted windows; "beresin": they snap into a tidy 2×2 grid; green "beres, tanpa klik" |
| s02 | 4.83–8.50 | Namanya Atticus, asisten suara open source khusus Mac. | topic header builds (Atticus · asisten suara open source · khusus Mac · MIT); white spec card: repo link `github.com/SaarthurR/atticus-mac` + REPO RESMI, rows tick on the words: Asisten suara (tahan Control + Option + Space, lalu ngomong), Open source (lisensi MIT), Khusus Mac (butuh macOS 26 ke atas); footnote "Pakai Windows? Ada versi buatan komunitas · proyek terpisah" |
| s03 | 8.50–12.33 | Bilang: buka WhatsApp, taruh di kiri. Jendelanya langsung pindah. | header → Atur jendela · TANPA AI; voice pill types “buka WhatsApp, taruh di kiri”; MAC KAMU panel with Browser on the right; "WhatsApp": chat-window mock opens mid; "kiri": dashed "← KIRI" target; "pindah": the window slides left; green "buka & geser jendela: tanpa AI" |
| s04 | 12.33–16.60 | Cari file penawaran klien? Dia nyari dari isi filenya, bukan cuma nama. | header → Cari file · ISI FILE; voice pill “cari file penawaran klien”; 4 files with useless names (dokumen (3).pdf, catatan_baru.txt, final_revisi2.docx, untitled.xlsx); "nyari dari isi": a cyan scanner frame walks the list while the ISI FILE pane (CONTOH) shows each file's content with a red x; "filenya": final_revisi2.docx = "Penawaran Harga · CV Contoh Jaya", COCOK; "bukan cuma nama": green "ketemu dari isinya" |
| s05 | 16.60–22.00 | Buka email, bilang: balas, Kamis aku bisa. Drafnya jadi, tapi nggak dikirim sendiri. | header → Baca layar · AMAN; email card (Bu Rina · Katering Sehat, CONTOH) slides in; "bilang": focus corners + scan line + "BACA LAYAR" tag, voice pill types “balas: Kamis aku bisa”; "Drafnya": DRAF BALASAN card (ditulis Atticus) types "Halo Bu Rina, Kamis saya bisa. Mau jam berapa?", buttons Sisipkan / Kirim (locked); "nggak dikirim": Kirim shakes + "tidak dikirim otomatis" |
| s06 | 22.00–25.90 | Pasangnya: tempel link repo ke Claude Code, minta dia yang pasangin. | header → Cara pasang · lewat Claude Code · macOS 26+ · 1 LINK; repo link pill + "Cara resmi di README: curl -fsSL …/atticus-mac/main/install.sh \| bash"; "tempel": "disalin", a copy drops into our own "Claude Code · di Mac kamu" card (text only); "minta dia": "pasangin di Mac aku, ya" types; "pasangin": rail of the installer's real steps lights (cek Mac macOS 26+ · unduh ke ~/.atticus · build Atticus.app · buka setup, izin satu-satu) |
| s07 | 25.90–30.87 | Aplikasinya gratis, otaknya langganan Claude Pro atau Max, atau model lokal. | header → Biayanya · JUJUR; app card "Atticus.app · Rp0 · open source · lisensi MIT" + GRATIS stamp; "otaknya": cable + plug; sockets "Langganan Claude · PRO / MAX" and "Model lokal · OLLAMA / LM STUDIO"; plug seats in Claude (Pro, Max light), then moves to Model lokal; green "tanpa API key" |
| s08 | 30.87–36.43 | Tapi ingat, dia bisa lihat layarmu. Kamu kasih izin mikrofon, aksesibilitas, rekam layar. | header → Izin akses · PENTING (amber); amber "PERHATIAN: dia bisa lihat layarmu" + a screen with two windows and a big eye; amber focus corners + scan line on "lihat layarmu"; "Kamu kasih izin": white card "Izin macOS untuk Atticus · SAAT SETUP": Mikrofon, Pengenalan ucapan, Aksesibilitas, Rekam layar (amber row) switch on with the words; footnote "+ opsional buat agen: Kalender, Otomasi · bisa dicabut kapan saja" |
| s09 | 36.43–41.43 | Suaramu diolah di Mac, tapi permintaan dan tangkapan layar dikirim ke penyedia model. | header → Data kamu · PRIVASI; dashed "MAC KAMU" zone + dim "Penyedia model · mis. Anthropic, kalau pakai Claude" card; mic → bars → "teks" + green "suaramu nggak keluar dari Mac"; packets "Permintaan" and "Tangkapan layar" appear, then fly across the border into the provider card (amber glow + "ikut terkirim"); cyan "model lokal = tetap di Mac"; last 0.3 s workspace + header lift away |
| s10 | 41.43–44.93 | Komen ASISTEN, aku kirim lewat DM. | house CTA: "Atticus · repo resmi · link + cara setting yang aman" card; comment bar, ASISTEN typed per letter + caret, heart; DM panel (AI PRENEUR) "Ini link resmi + cara setting amannya, ya", paper plane, card lands as attachment, "terkirim"; end logo (corner logo fades at 43.53) |

Hosts: mascot bottom-left (welcome, explain/emphasize/present/reveal per beat, question on "Cari", compare on "otaknya" and the s09
"tapi", cta on "Komen", point on "DM."); robot bottom-right (types on the holo keyboard while the keys are held, scans windows/files/
email/screen, types the draft and the install ask, "no" on "nggak", shock on "ingat"/"dikirim", cheers on "beresin"/"filenya"/
"pasangin"/"Komen"). **Mascot glance-at-robot disabled from the start** (`const glance = (t) => 0;`, old word list emptied).

## Sources (checked 12 Nov 2026) — claim-by-claim table in `production/VO_SCRIPT.md`
- github.com/SaarthurR/atticus-mac — cloned (commit 46edb57, 10 Nov 2026, v1.6.0): README (shortcut, instant commands with no AI, file
  search by content, sees your screen, reply drafts "It never sends", AI client = Claude Pro/Max + Claude Code / Devin / Pi / local server,
  "No API key", macOS 26+, quick install one-liner, Nix, setup window asks each permission, on-device speech "audio never leaves your Mac",
  anonymous usage + opt-out, Windows community port), LICENSE (MIT), install.sh (steps), ui/onboarding.html (permission rows + required
  set), ui/settings.html ("Look at my screen: Automatic / Never", "The picture goes with that one ask."), atticus.py (screenshot capture
  handed to the model, deleted after). GitHub page (About text, MIT; 736 stars / 76 forks on 12 Nov — NOT used on screen).
- github.com/FindlayHi/atticus-windows — exists (git ls-remote); linked from the Atticus README as a separate community project.
- code.claude.com/docs/en/overview — Claude Code "reads your codebase, edits files, runs commands" (basis for "minta dia yang pasangin").

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: #bg / #fx nested in index.html, same as the R9/R15 kit).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors, 0 contrast warnings; remaining warnings = "multiple Three.js instances"
  (robot + mascot bundles, as in the kit) + SwiftShader ReadPixels notices.
- Script check (`tools/check_scene.cjs`, preview on :8939, then stopped): s01–s10, robot, mascot, main all register, no exceptions;
  the preview's stamped `data-hf-id` attributes were stripped again afterwards.
- Snapshots (`snapshot . --at … --no-end --timeout 60000`): one full pass of 74 frames — first frame, every scene's beats, both sides of
  every cut, the end — + two targeted fix passes (14 + 3 frames). Contact sheets (JPG): `production/qa/runtime_full_1..4.jpg` (full
  frames), `production/qa/runtime_hero_1..4.jpg` (hero zone + captions, larger), `production/qa/runtime_hosts_1..4.jpg` (mascot + robot,
  eye check), `production/qa/runtime_fix_1.jpg`, `production/qa/runtime_fix_2.jpg` (after the fixes). The full-pass sheets predate the
  fixes listed below. PNG dumps deleted (disk budget).
- Mascot eyes: pupils in every frame of the full pass (closed lids = blinks); glance disabled from the start.
- Fixed during QA: s01 keys and the desktop cross-faded into each other (keys now leave before the desktop appears); s03 "KIRI" label was
  hidden behind the opened window (now "← KIRI" at the left of the target); s04 the scan line through the file names read as
  strike-through (now a cyan scanner frame around the file, fading as the match lands so it never cuts the COCOK badge); s05 the voice
  pill overlapped the rising draft card (pill leaves earlier); s09 packets were small in a sparse zone (bigger packets, wider provider card).
  Early: the voice pill / window cards had no left/top anchor (kit CSS fixed); keycap row re-spaced and lowered.

## Known issues / notes for the lead
- Frame 0 shows the headline + keycaps only: mascot pops up from below over 0.5 s and the robot flies in over 0.75 s (kit behaviour,
  same as R9/R15). The cover is separate.
- Short "header only" beats at the start of each topic (≈0.1–0.3 s while the header rolls and the workspace rises) — intentional, same
  as R9/R15; a caption chunk can show an empty chip for 1–2 frames while its first word rises (house caption behaviour).
- All on-screen examples are illustrative and labelled CONTOH / mocks: "rapikan jendelaku, dong", WhatsApp window, file names, "Penawaran
  Harga · CV Contoh Jaya", Bu Rina's email + the reply. Window cards, the "Claude Code" card and the permission switches are our own
  mocks (permission labels translated from Atticus's setup window). Brand names are text only.
- "minta dia yang pasangin": the README's official install is the one-liner (shown on screen); asking Claude Code to run it works because
  Claude Code runs commands — but it still needs macOS 26+, Xcode command line tools and an AI client; the setup window then asks every
  permission. Worth saying in the DM guide.
- Privacy points for the DM guide (verified, not all in the VO): Settings → "Look at my screen" can be set to Never; anonymous usage
  ping is on by default (random ID, no task text/screen content) and can be turned off in Settings → Account & Access → Count me as a
  user; Safe mode asks before deletes/sends/purchases. Link to send: `github.com/SaarthurR/atticus-mac` (Windows users:
  `github.com/FindlayHi/atticus-windows`, a separate community project).
- "Jarvis" never appears (not on screen, not in the VO, not in captions); folder name `aip_r19_jarvis` is internal only.
- `hyperframes snapshot`/`preview` wrote `.hyperframes/` into the project folder (harmless, as in R15).
