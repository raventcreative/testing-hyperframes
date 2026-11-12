# NOTES — R1 · Panel rekrutmen 7 Claude (NAVY) · AI PRENEUR

Duration 44.2 s (1326 frames @30) · VO 42.88 s at +0.3 s · CTA keyword **CV**. Not rendered (the lead renders); not committed.

## Files
- `index.html` (built by `tools/build_index.py`) · `compositions/s01–s08.html` · `compositions/panel.html` (persistent 7-judge rail) ·
  `compositions/robot.html`, `mascot.html` (kit, retargeted gestures) · `vendor/cvkit.js` (shared CV + judges + icons).
- `production/VO_SCRIPT.md` (script, what changed vs ref1, sources) · `production/vo_lines.txt` (text sent to ElevenLabs) ·
  `production/vo_takes/take1.{mp3,json}` · `production/vo_fw_small.json` · `production/vo_words_raw.json` · `production/timing.json` ·
  `production/SCENE_BRIEF.md` (system + scene table).
- `assets/audio/vo.mp3` (−17.7 LUFS) · `assets/audio/sfx.wav` (synth, −27.7 LUFS, peak −7 dB; `tools/sfx.py`).
- `thumbnail/cover.html` → `thumbnail/COVER_PANELCV_1080x1920.png` ("CARI KERJA? COBA INI DULU · 7 Claude NOLAK CV kamu duluan").

## Scenes (global s)
| scene | start–end | words |
|---|---|---|
| s01 hook | 0.00–5.73 | Aku bikin panel rekrutmen isinya 7 Claude. Tugasnya cuma satu: nolak CV kamu. |
| s02 ghosted | 5.73–11.30 | Soalnya, kamu udah ngelamar ke puluhan lowongan, tapi nggak pernah dikasih tahu kenapa ditolak. |
| s03 #1 ATS | 11.30–16.73 | Claude pertama jadi sistem ATS, penyaring otomatis sebelum CV kamu dibaca manusia. |
| s04 #2 HM | 16.73–21.17 | Claude kedua jadi hiring manager. Kamu layak dipanggil interview, atau nggak? |
| s05 #3–#7 | 21.17–28.00 | 5 Claude sisanya baca sendiri-sendiri, pakai kacamata yang beda: calon atasan, sesama pelamar, sampai CEO. |
| s06 rewrite | 28.00–34.43 | Semua alasan nolaknya dikumpulin. Terus dia tulis ulang CV kamu, dengan semua catatan tadi udah dibenerin. |
| s07 jujur | 34.43–39.80 | Ini bukan jaminan diterima, ya. Tapi kamu jadi tahu kenapa ditolak, sebelum HRD yang nolak. |
| s08 CTA | 39.80–44.20 | Mau workflow-nya? Komen CV, aku kirim lewat DM. |

## Sources (checked 12 Nov 2026)
- ATS definition (generic, no statistics): WebSearch summary of Tufts Career Center, The Forage (theforage.com/blog/basics/applicant-tracking-system),
  Jobscan (jobscan.co/blog/what-is-an-applicant-tracking-system). en.wikipedia.org / careers.tufts.edu are not reachable from this sandbox.
- Claude file uploads (PDF/DOCX/TXT…): support.claude.com/en/articles/8241126-uploading-files-to-claude.
- Subagents each run in their own context window: code.claude.com/docs/en/sub-agents.

## QA (real runtime, hyperframes 0.8.186)
- `npx --yes hyperframes@0.8.186 lint .` → 0 errors (2 kit warnings: nested #bg / #fx layers in index.html).
- `npx --yes hyperframes@0.8.186 validate .` → 0 errors, 22 contrast warnings, only for dimmed seats, fading exits and the CV's 16 px
  section labels; Three.js/WebGL driver notices from the robot/mascot runtimes.
- 60 real-runtime snapshots (first frame, every beat, both sides of every cut, end frame) → contact sheets in
  `out/qa_runtime/` (A1, A2, A3, C, B1–B4; full frames in the session scratchpad `r1/final_a`, `r1/final_b`).

## Known issues / notes for the lead
- The CTA promises "workflow-nya" by DM: the actual workflow/prompt (7 reviewer roles + rewrite step) must exist before posting.
- CV copies in s03–s05 and the CV node in s07 are scaled down (objects, not meant to be read); all key text is ≥ 20 px.
- ElevenLabs character alignment for this take drifted late at phrase ends, so word timing comes from faster-whisper small + our
  script text (documented in VO_SCRIPT.md). Captions checked against the waveform.
- s02→s03 and s07→s08 are quick push / fade resets (≈0.1 s of near-empty frame at 39.8 s before the CTA card flips in).
