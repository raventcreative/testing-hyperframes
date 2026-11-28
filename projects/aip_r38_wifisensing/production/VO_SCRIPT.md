# R38 · "Wi-Fi bisa deteksi gerakan" (RuView) — VO script (WHITE, CTA WIFI)

Reference: `projects/aip_remake_batch10/refs/ref1.mp4` (43.4 s, EN: "we're officially cooked … AI can see you through Wi-Fi …
install it with Claude Code … watch every move from your phone … comment WiFi"). Target 40–48 s → final **47.6 s**
(VO 45.87 s, ONE untouched ElevenLabs take, offset 0.3 s, ~1.4 s tail on the CTA).

## VO lines (`production/vo_lines.txt`, Dakocan, eleven_v4, auto tags) — take 4
1. Sinyal Wi-Fi sekarang bisa mendeteksi gerakan orang, bahkan di balik tembok.
2. Tanpa kamera sama sekali.
3. Namanya RuView. Open source, lisensi MIT, lebih dari seratus ribu bintang di GitHub.
4. Caranya gini.
5. Waktu kamu gerak, bahkan cuma napas, tubuh kamu mengubah sinyal Wi-Fi di ruangan.
6. Sensor kecil sekitar sembilan dolar nangkep perubahan itu.
7. Lalu AI-nya nebak: ada orang atau nggak, lagi gerak, sampai napasnya.
8. Pasangnya bisa dibantu Claude Code, repo-nya udah punya plugin sendiri.
9. Hasilnya bisa nyalain lampu otomatis lewat Home Assistant.
10. Tapi ini masih beta. Laptop tanpa sensor cuma deteksi kasar, dan pose tubuhnya belum akurat.
11. Pakai cuma di ruangan sendiri, dan penghuninya harus tahu.
12. Komen Wi-Fi, aku kirim link GitHub plus panduannya lewat DM.
Takes: 1 "ngubah" misheard by small AND medium → "mengubah"; 2 "ngerasain gerakan" misheard by medium ("ngerasa imgerakan") →
"mendeteksi"; 3 "ESP32" misheard by small AND medium ("ASP32") → the word left the VO ("Sensor kecil"), ESP32-S3 is on screen;
4 = final (only spelling/number differences + the proper names RuView / Claude).

## Fact check (GitHub, 2026-11-28) — what was kept, softened or dropped
| reference claim | README / repo says | in the reel |
|---|---|---|
| "100k stars" | 105,364 stars (GitHub search API, read today) | "lebih dari seratus ribu bintang" + card "105.364 · dibaca 28 Nov 2026" |
| "MIT" | LICENSE = MIT License (c) 2024 rUv | kept |
| "see you through walls, no cameras" | "detect people … through walls, in the dark, with no cameras"; through-wall "up to ~5 m, signal-dependent" | kept, with chip "sampai ± 5 m · tergantung sinyal" |
| (implied: any Wi-Fi) | full sensing needs CSI from an ESP32-S3 (~$9) or research NIC; laptops = RSSI-only coarse presence | "Sensor kecil sekitar sembilan dolar" + limits card "Laptop … deteksi kasar" |
| "AI estimates human movement" | presence, motion, breathing, heart rate; camera-free pose accuracy still limited / first-cut | presence · movement · breathing; "pose tubuhnya belum akurat" |
| "install it using Claude Code" | in-repo Claude Code plugin: `/plugin marketplace add ruvnet/RuView`, `/plugin install ruview@ruview`, `/ruview-start` | kept, commands verbatim from README |
| "watch every move from your phone" | not in README (it has a local dashboard and Home Assistant / Apple Home / Matter integration; live single-ESP32 pose is a first-cut stub) | **dropped**; replaced by the README's smart-home use: lights via Home Assistant |
| "covering your webcam isn't enough" / "we're cooked" | — | **dropped** (fear hook); replaced by the honest "masih beta" beat + privacy/consent line |
Added (README): beta status; Docker demo with simulated data (DM); ESP32-C3 / original ESP32 not supported (DM); privacy note (own
space, everyone inside knows).

## ATM (Amati, Tiru, Modifikasi)
- Indonesian, "kamu", Freddie's practical tone; own hook (no "we're cooked"), own order: what → proof (repo) → how it works →
  hardware → what the AI outputs → how to install → one real use → honest limits → privacy → CTA. No sentence uses >3 consecutive
  words of the reference (different language, own wording).
- Own visuals on the client's white plate (no 3D room / wooden mannequin of the reference): wall diagram with attenuated waves,
  camera-off emblem, GitHub repo card + star counter, floor plan (walk → breathe → rays to the sensor), live CSI graph, generic
  ESP32-S3 board, AI node, room dashboard, the client's real Claude Code input → plugin terminal, floor plan lamp + Home Assistant
  automation card, honest-limits card.

## Staging (batch-10 client rule)
- Explaining beats → mascot FORWARD half-body (waist-up, cropped by the frame bottom), push-in + rise from the bottom-left corner pose
  (closed-form spring), lip-synced, Wi-Fi rings behind it: hook (0–3.4 s), "Caranya gini" (13.2–14.2 s), "Tapi ini masih beta" (+ BETA
  stamp, 33.9–35.3 s), privacy + CTA (39.4 s → end).
- Example beats → mascot fully hidden (it shrinks back to the corner and sinks out; the card lands 0.24 s later, every card leaves
  before the mascot returns). No beat counter. No voxel world, no robot.

## Techniques used (skills)
- **html-demo**: scripted View(t) windows — the Claude Code input with a scripted cursor glide + click and typed example prompt, the
  terminal typing the README commands, the dashboard rows with live bars / breathing wave.
- **product-launch-film**: shared-element transformations (wall diagram → camera-off emblem; repo card → star counter; floor plan
  shrinks into plan + graph, the graph stays under the board; board → AI node → zoom-through into the dashboard; Claude Code input
  grows into the plugin terminal; the floor plan returns for the lamp), closed-form springs everywhere.
- **beat-promo-film**: every change on a VO word; 3-subframe ghosts on the flying signal dots; velocity blur on whips.
- **throughline-explainer**: ONE through-line — the Wi-Fi wave (rings behind the mascot → waves through the wall → waves in the
  floor plan → the CSI line → dots into the sensor → the CTA).
- A different transition every beat: whip-in, stamp + strike, card flip (rotateY), rise, counter roll, push-in, shrink-to-top,
  whip-left, shrink-aside + arrow, zoom-through, slide-up, grow/morph, flip-down (rotateX), drop-in with bounce, pill press.
- SFX: whoosh-in when the mascot comes forward, soft pop when it leaves, whoosh per card, pops/clicks on chips/rows, typing ticks,
  impact on stamps, riser + impact + click on the CTA.
