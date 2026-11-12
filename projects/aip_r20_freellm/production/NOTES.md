# NOTES — R20 · Claude Code pakai model AI gratis (FreeLLMAPI) (LIGHT) · `projects/aip_r20_freellm/`

1080×1920 · 30 fps · **44.3333 s** (1330 frames) · VO 42.72 s starting at 0.30 s · HyperFrames 0.8.186. Kit: `aip_r12_cuanrepo` (LIGHT,
glances already disabled; `out/` not copied). Not rendered (the lead renders), not committed. Reference: `projects/aip_remake_batch5/refs/ref10.mp4`
(28 s, English). CTA keyword **LLM**; DM hand-out: `production/DM_LLM.md`. Sources + ATM: `production/VO_SCRIPT.md`.
`.gitignore` in this folder: `out/`, `.hyperframes/`.

## Pipeline (all re-runnable, run from this folder)
1. `production/vo_lines.txt` → `python3 /home/user/testing-hyperframes/tools/el_tts_ts.py production/vo_lines.txt assets/audio/vo.mp3`
   (NO --tags → client's auto tags: `[playful] [excited]` on every line + `[curious]` on the hook question, `[confident]` on the CTA)
   → `assets/audio/vo.mp3` + `vo.json`. Take 2 (42.80 s). Take 1 (43.60 s) had "isi API key tiap penyedia" heard as "API Kitia
   penyebiah" by faster-whisper → line 7 became "isi API key dari tiap penyedia". "LLM" is spoken as letters (whisper small + medium).
2. `python3 -I tools/align_words.py .` → `production/vo_words_raw.json` (faster-whisper format, from the ElevenLabs character alignment).
3. `python3 -I tools/timing.py .` → `production/timing.json` + `vendor/vo_words.js` (scene cuts, caption chunks, styles; MERGE shows the
   spoken "Free LLM API," as **FreeLLMAPI,** and keeps "Claude Code" as one caption word; merged words keep the alignment start — the
   energy snap would have moved "Claude Code" 0.33 s late because of the stop consonant between the two words).
4. `python3 -I tools/scenes.py .` → `vendor/scenes.js` · `python3 -I tools/build_index.py .` → `index.html`.
5. `python3 tools/sfx.py .` → `assets/audio/sfx.wav` (synthesised, deterministic; −31.3 LUFS vs VO −18.2 LUFS). No music (lead adds it).
6. Cover: `node thumbnail/render_cover.cjs thumbnail/COVER_LLM_1080x1920.png` (default URL http://127.0.0.1:8940/proj/thumbnail/cover.html:
   any static server on :8940 whose root contains this folder as `/proj/`, or set `COVER_URL`).

## Shared visual system — `vendor/r20kit.js` (window.K) + `vendor/r20icons.js` (lucide-static 0.460, ISC)
Metaphors: the app (Claude Code) is the BODY, the model is the BRAIN; FreeLLMAPI is a small SERVER BOX on your laptop that understands the
Claude API format and passes requests on ("dioper") to whichever provider still has free quota — shown as a "Sisa jatah gratis" panel
(like checking remaining data quota on a phone; bars labelled ILUSTRASI).
- `K.term` (Claude Code window: text label + generic terminal icon, no logo), `K.box` (server box, LEDs, "FreeLLMAPI · localhost:3001"),
  `K.quota` (quota panel: rows with bar, red overlay, idle/serving/empty status pills, blue ring), `K.laptop`, chips/stamps/footnotes.
- `K.boot(ID)`: seek-safe scale shorthand; **every initial state pinned at 0 in a nested timeline P0 that is the first child at 0**;
  fromTo without immediate render; word lookup that throws on a missing word; typed text with caret; `done()` = end marker +
  backward-seek patch + **`tl.render(0, true, true)`** + registration. index.html (captions, logo, grid, grain) and s11 use the same rule.
- No brand logos anywhere (Claude/Anthropic, GitHub, providers are text only). All commands shown are the real README commands.

## Scenes (global s)
| id | start–end | VO | visual |
|---|---|---|---|
| s01 | 0.00–3.47 | Pengen belajar Claude Code, tapi belum sanggup langganan? | Claude Code window on screen from frame 0, a learner's request types itself ("> ajarin aku bikin web portofolio"); "tapi": paywall card drops over it ("BIASANYA · Perlu paket berbayar · paket langganan Claude atau kredit API", lock jiggles); "belum sanggup": "Dompet pelajar" card, bar drains → "tipis"; "langganan?": big navy "?"; hand-over: only the window stays |
| s02 | 3.47–8.60 | Ada jalan tengahnya: FreeLLMAPI, server kecil gratis di GitHub. | window shrinks top-left; dashed "middle road" draws + "Jalan tengah" signpost chip; server box drops onto the road's end (bounce); repo card "OPEN SOURCE · DI GITHUB · FreeLLMAPI · github.com/tashfeenahmed/freellmapi"; LEDs blink + chip "Server kecil · jalan lokal"; chip "Gratis · lisensi MIT"; path underline on "GitHub"; hand-over: only the box stays |
| s03 | 8.60–11.77 | Dia jalan di laptopmu, ngerti format API Claude. | laptop rises, the box settles on its screen, chip "Berjalan di laptopmu"; "Claude Code" pill + request bubble "KIRIM PERMINTAAN · POST /v1/messages"; envelope travels a wire into the box; green badge "ngerti format API Claude"; chip "Juga paham format OpenAI" |
| s04 | 11.77–16.90 | Perintah Claude Code dioper ke jatah gratis model dari Google, Groq, Mistral, dan lainnya. | Claude Code card types "> bikinin halaman login"; box top-right; "perintah" token arcs app → box (LEDs); "Sisa jatah gratis" panel slides up; Google / Groq / Mistral rows get name + bar on their words, "+ penyedia lain · Cerebras, OpenRouter, dll."; token drops into Google → "melayani" + ring |
| s05 | 16.90–20.27 | Jadi aplikasinya Claude Code, tapi otaknya bukan Claude. | BODY: Claude Code window tagged APLIKASI + chip "Aplikasinya: Claude Code"; BRAIN card ("OTAKNYA · MODEL AI · Claude") drops on top, neck wires draw; "bukan": strike + stamp "BUKAN CLAUDE" + shake; value swaps to "Model gratis · dari Google, Groq, Mistral, dll."; footnote "Catatan: Anthropic tidak mendukung resmi Claude Code + model non-Claude" |
| s06 | 20.27–23.00 | Jatah satu habis, otomatis pindah ke yang lain. | chips Claude Code → FreeLLMAPI; quota panel with Google serving; Google bar drains to zero, turns red, "habis" + shake; "Otomatis pindah" pill (spinning icon); ring slides to Groq along a curved arrow → "melayani" + tick; chip "Claude Code tetap jalan, tanpa ganti setting" |
| s07 | 23.00–27.63 | Pasang servernya, isi API key dari tiap penyedia, lalu satu perintah setup. | 3 step cards: 1 "Pasang servernya" (`$ curl -fsSL https://freellmapi.co/install.sh \| bash` types; "butuh Docker · atau pakai app desktop Windows / macOS"); 2 "Isi API key tiap penyedia" (Google / Groq / Mistral key chips ••••, "daftar akun di tiap penyedia → tempel di halaman Keys"); 3 "Satu perintah setup" (`$ npx freellmapi setup-claude` types → chip "Claude Code tersambung"); green ticks |
| s08 | 27.63–32.10 | Jujur ya: kualitasnya beda dari Claude, limit gratisnya juga bisa berubah. | amber chip "CATATAN JUJUR" + "Yang perlu kamu tahu"; card 1 "KUALITAS JAWABAN": tile "Model Claude" ≠ tile "Model gratis · tergantung yang kebagian" (amber ≠ slams), "Hasilnya bisa beda — kadang oke, kadang lebih lemah."; card 2 "LIMIT GRATIS": bar jumps around, chip "Reset 07.00 WIB (00.00 UTC) tiap hari", "Bisa berubah kapan aja — dikurangi, diganti, atau dihapus." |
| s09 | 32.10–37.47 | Kodemu ikut dikirim ke server penyedia, jadi baca aturannya dan jangan kirim data sensitif. | nodes Laptopmu → FreeLLMAPI → Server penyedia, "kode.py" card travels the wire, amber eye on the provider; ToS card "BACA DULU · TERMS OF SERVICE · Aturan tiap penyedia", magnifier sweep, highlighted line "Layanan gratis: data bisa dipakai buat melatih model*" + "*contoh: syarat Gemini API (Google) untuk pemakaian gratis"; "Jangan kirim:" red chips ".env & password", "data pelanggan", "kode rahasia klien" (shake on "sensitif"); green tip "Latihan pakai data contoh" |
| s10 | 37.47–40.57 | Pakai buat belajar dulu, bukan buat kerjaan klien. | card "COCOK BUAT · Belajar" (latihan ngoding, proyek portofolio, coba fitur Claude Code) + stamp COCOK; card "BELUM BUAT · Kerjaan klien" (kode & data klien, butuh hasil stabil, note "pakai API berbayar resmi") + stamp NANTI DULU |
| s11 | 40.57–44.33 | Komen LLM, aku kirim lewat DM. | package card "DIKIRIM LEWAT DM · Panduan FreeLLMAPI · link repo · 3 langkah setup · catatan aman"; comment types LLM, heart, send → plane; DM bubble "Link repo + 3 langkah setup / plus catatan biar kodemu aman", "terkirim"; end: AI PRENEUR logo + glint |

Robot (co-host, right): flies in on "tapi", thinks on "langganan?", cheers the box, TYPES on its holo keyboard when a request is sent or
something is set up (ngerti, Perintah, Pasang, key, satu perintah setup), scans the providers, shakes its head on "bukan Claude", "beda",
"jangan", small shock on "habis" and "berubah", cheers the CTA, waves at the end. Mascot (host, left): an intent on every beat
(present / explain / question on "langganan?" / emphasize / compare / cta); **glances disabled** (`const glance = (t) => 0;`).

## QA
(see below — filled in after the real-runtime pass)
