# R39 · "Colibri: model AI raksasa di PC sendiri" — VO script (NAVY, CTA COLIBRI)

Reference: `projects/aip_remake_batch10/refs/ref2.mp4` (61.4 s, EN: "run DeepSeek, GLM, Qwen, Kimi K3 on your own PC … Colibri",
CTA "Comment colibri"). Batch-10 format: the batch-9 2D look (spoken headline + one emphasised word, brand navy plate, html-demo cards)
with the NEW client staging: explaining beats = the 3D mascot comes forward half-body; example/demo beats = mascot fully hidden and
the example gets the whole frame; no beat counter; no voxel world, no robot.
Target 58–66 s → final **65.2 s** (VO 63.40 s, ONE untouched ElevenLabs take, offset 0.3 s, ~1.5 s tail on the CTA).

## Fact check (done BEFORE scripting) — github.com/JustVugg/colibri, README + LICENSE read 2026-11-28 via raw.githubusercontent.com
- Repo exists and does what the reference says: "colibri runs very large open models on the machine you already have … keeps that
  part in RAM and reads the rest, the experts, from the disk … Pure C, one file per model family, no GPU required." Licence
  **Apache-2.0** (LICENSE + README). "colibri is free and open source."
- Mechanism (README "What colibri is" / "How it works"): dense part (attention, shared experts, embeddings) in RAM; routed experts on
  disk, read when the router asks, through a cache that learns which experts your work uses (per-layer LRU + pinned hot set); a GPU,
  when there is one, holds the hottest experts; "Where a weight sits changes how fast the answer comes, not which weights or which
  router decisions produce it"; "colibri gets faster the more you use it".
- RAM figures (README "Which model for my machine", first number = below it the model does not start):
  DeepSeek V4 Flash 16 / 32 GB ✓ · Kimi K3 32 / 64 GB ✓ · Qwen3-Coder-30B-A3B ("Qwen's coding model") 8 / 18 GB ✓ ·
  machine minimum "8 GB of RAM at the very least (16 GB or more is better), 22 GB free on the disk for the smallest model" ✓.
- Platforms: Windows (`START-HERE.bat`), Linux and macOS (`./start-here.sh`) ✓. The setup "looks at your machine: RAM, free disk,
  CPU and GPUs; recommends the model … Enter takes the recommendation … starts colibri and opens the chat in your browser" ✓.
- Trade-off (stated in the reel and the DM): large models stream from the disk ("the disk sets the speed"): DeepSeek V4 Flash
  0.93 tok/s with 32 GB (Ryzen 7 5800X, CPU only), Kimi K3 about 9.4 s per token; downloads 167 GB / 1.56 TB.
- **Dropped / changed from the reference:** "GLM" kept only on screen as the 744B example (GLM-5.2) — not in the VO list; the
  reference's "free repo" kept as "gratis, open source" (true); star count not mentioned (not needed); the reference's "you don't need
  a server anymore" softened to "buat nyobain AI besar, cukup PC sendiri plus SSD yang lega" plus an explicit honest beat ("model besar
  jalannya pelan, dan makan SSD ratusan giga") that the reference skips. "plain C" kept on screen ("mesin C · 1 file per model"),
  not in the VO (whisper could not hear "C" reliably).

## VO lines (`production/vo_lines.txt`, voice Dakocan, eleven_v4, auto tags) — 19 beats
1. Model AI raksasa sekarang bisa jalan di PC kamu sendiri.  *(explain · mascot)*
2. Bahkan ada yang mulai dari RAM delapan giga.  *(demo · RAM card)*
3. Namanya Colibri, gratis, open source, dan mesinnya mungil.  *(demo · repo card)*
4. Kartu grafis? Opsional, nggak wajib.  *(demo · GPU toggle)*
5. Kenapa bisa? Model kayak gini isinya banyak ahli kecil.  *(explain · mascot + expert cubes)*
6. Tiap kata, cuma sedikit ahli yang kerja.  *(demo · model map)*
7. Bagian yang selalu kepakai, disimpan di RAM.  *(demo · model map)*
8. Ahli sisanya nunggu di SSD, dipanggil pas dibutuhkan.  *(demo · model map)*
9. Yang sering dipanggil nempel di RAM atau GPU, makin dipakai makin cepat.  *(demo · model map)*
10. Posisinya cuma ngaruh ke kecepatan, modelnya tetap utuh.  *(explain · mascot)*
11. Contohnya DeepSeek V4 Flash, mulai dari RAM enam belas giga.  *(demo · model shelf)*
12. Model Kimi K3, mulai tiga puluh dua giga.  *(demo · model shelf)*
13. Model coding dari Qwen, cukup delapan giga.  *(demo · model shelf)*
14. Jalan di Windows, Mac, dan Linux.  *(demo · OS tiles)*
15. File Start Here ngecek PC kamu, terus milihin modelnya.  *(demo · file window + terminal)*
16. Habis itu, chat-nya langsung kebuka di browser.  *(demo · URL → browser)*
17. Tapi jujur, model besar jalannya pelan, dan makan SSD ratusan giga.  *(demo · honest numbers card)*
18. Jadi buat nyobain AI besar, cukup PC sendiri plus SSD yang lega.  *(explain · mascot)*
19. Komen COLIBRI, aku kirim link-nya plus tabel model per ukuran RAM lewat DM.  *(CTA · mascot + pill)*

## ATM — what we changed (Amati, Tiru, Modifikasi)
- Indonesian, "kamu", own hook ("Model AI raksasa sekarang bisa jalan di PC kamu sendiri" — the size first, names later), own order
  (RAM floor → what it is → GPU optional → why it works → numbers → setup → honest trade-off → CTA), own metaphors ("ahli kecil",
  "nunggu di SSD, dipanggil pas dibutuhkan", "nempel di RAM"). Different language, no sentence copies >3 consecutive reference words.
- Added what the reference leaves out: GPU optional, 22 GB disk for the smallest model, the measured slowness and the download sizes.
- DM = repo link + the README's model table grouped by RAM + install steps + honest notes (`production/DM_COLIBRI.md`), exactly what
  the CTA promises ("link-nya plus tabel model per ukuran RAM").

## Staging (client rules 2026-11-28)
- Explaining beats 1, 5, 10, 18–19: mascot rises small in the bottom-left corner, then a spring push-in (log-space size) to the
  half-body pose (waist-up, cropped by the frame bottom on purpose), lip-synced, under the headline; whoosh-in SFX. It shrinks back to
  the corner and drops out (pop-out SFX) before the next example card lands (`window.STAGE` in vendor/r39.js → vendor/mascot_host.js).
- Demo beats: mascot fully hidden (canvas opacity 0, not rendered); cards are 900–960 px wide.
- No beat counter. No voxel world, no robot. Brand navy plate only, white text, accent #01ccf7.

## Techniques used (technique bank — techniques only)
- **html-demo**: scripted windows drawn from t — the file window with a person-like cursor double-clicking `START-HERE.bat`, a
  terminal whose checks print in order, an Enter key press, then a browser with a typed chat (labelled "ilustrasi" / "contoh chat").
  Real labels from the README: `START-HERE.bat`, `start-here.sh`, "Starting colibri", `http://127.0.0.1:8000/`.
- **product-launch-film / shared elements**: the expert cubes that pop around the mascot fly into the model-map grid; the grid cells
  morph into the SSD; the core bar becomes the RAM content; hot experts fly from the SSD into RAM/GPU slots; the terminal's URL line
  flies into the browser's address bar, which then opens (button → page). Closed-form springs everywhere.
- **throughline-explainer**: ONE model-map card carries four VO lines (word → few experts → RAM → SSD → cache/GPU) instead of four
  separate cards.
- **beat-promo-film**: every change lands on a VO word (word timings from the ElevenLabs alignment); velocity-proportional motion blur
  on card moves and on the mascot push-in/exit.
- Real 3D logos (Simple Icons → SVGLoader + ExtrudeGeometry, pre-rendered 24-angle sprite strips, spin-in from edge-on).

## Pronunciation / listen-check notes
- 4 takes. Take 1–2: "DeepSeek", "Kimi K3", "C murni / bahasa C" misheard by both models → reworded ("Contohnya DeepSeek …",
  "Model Kimi K3, …", dropped "C" from the VO). Take 3: "Letaknya" heard "Retaknya" by both → "Posisinya". Take 4 accepted.
- "DeepSeek" is transcribed DeepSync/DeepSig/Deepseq by whisper in every wording tested (3 variants) — a brand-name spelling issue of
  the Indonesian whisper model, same class as the accepted Claude→Cloud since R11.
