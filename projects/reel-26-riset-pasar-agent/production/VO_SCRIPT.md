# Reel 26 — 35 agent AI riset pasar (voxel rebuild, navy)

Brand: **AIpreneur Automation** (software-simulation reel, fixed CTA "Klik link di bio").
Format: the voxel 3D world format (`.claude/skills/voxel-reels`) with the Automation presenter robot
(`brand/robot3d`) as host instead of the R-series mascot — client asked for the voxel look but the
Automation robot stays the presenter.

Reference: `ad663f77-How_35_AI_Agents_Run_Your_Market_Research….mp4` (91 s). Beat order kept; the reference's
product names, UI, logos and price/giveaway claims are not used. Numbers are labelled *angka ilustrasi*.

## Why this rebuild
Client: bored of the software-demo look (app window + card stacks, 16 reels in a row) and called the old
hook ("SALAH BACA PASAR" + red MAHAL badge over an empty middle) ugly. The hook now **shows** the pain —
your stall opens, the order board stays 0, the next stall has a queue — instead of stating it.

## Script (VO 66.88 s, composition 68.6 s; ElevenLabs Dakocan, auto tags per line)
| # | line | on screen |
|---|---|---|
| 1 | Lu buka paket baru. Seminggu jalan, yang mesen nol. | your stall, board "0", one passer-by crosses and never stops |
| 2 | Lapak sebelah antrinya panjang. | queue of five builds at the next stall, board "24" |
| 3 | Bedanya satu: dia tau pasarnya, lu nebak. | "?" floats over your stall, wide on both stalls |
| 4 | Cek simulasinya. Tiga puluh lima agent AI yang jalanin riset pasar lu. | portal through the order board → 35 agents light up row by row |
| 5 | Mereka cuma ngejar tiga jawaban: pelanggan mau apa, kompetitor lewatin apa, dan duitnya di mana. | the 35 regroup into three labelled clusters |
| 6 | Pertama, agent kompetitor. Dia baca penawaran, harga, sama review tiga lapak paling rame di kota lu. | island hop → three stalls, each card read in close-up |
| 7 | Keluar dua celah: layanan yang nggak ada yang nawarin, sama keluhan yang nggak ada yang beresin. | two cyan pillars rise with two-line cards |
| 8 | Kedua, agent suara pelanggan. Empat ratus dua belas review dibaca satu-satu. | iris → wall of review tiles lights up, counter to 412 |
| 9 | Yang dibalikin bukan ringkasan, tapi kata-kata persis yang dipakai orang pas mau beli. | four buyer phrases lift out of the wall |
| 10 | Ketiga, radar permintaan lokal. Dia nandain yang lagi naik di area lu. | whip tilt → radar dish, sweep, blips |
| 11 | Facial malam hari naik enam puluh empat persen. Lu bisa buka duluan, bukan dua bulan setelah kompetitor. | three demand rows with their own bars |
| 12 | Semuanya ngumpul ke satu otak riset. | dive into the top signal → brain core, three streams flow in |
| 13 | Tiap Senin lu terima satu halaman: apa yang berubah, apa yang pelanggan tanyain, sama satu penawaran buat minggu ini. | the Monday one-pager prints |
| 14 | Jadi lu gerak karena tau, bukan karena nebak. | wide over the brain island |
| 15 | Mau sistem kayak gini dipasang di bisnis lu? Klik link di bio, ngobrol langsung sama tim AIpreneur Automation. | shockwave ring → CTA card centred, robot whole at the bottom |

## Transitions (one per beat, none repeated)
1. **Portal zoom-through** (H→G) — camera pushes into the order board, white flash, lands among the agents.
2. **Island-hop flight** (G→K) — one absolute camera key, the camera physically crosses to the next island.
3. **Iris** (K→V) — page-layer iris closes and opens.
4. **Whip tilt to the sky** (V→R) — camera rolls and tilts up, blur ramp, lands tilting down onto the radar.
5. **Dive-into-object match cut** (R→B) — the top signal grows into frame, white flash, out of the brain core.
6. **Zoom-out reveal + shockwave ring** (B→CTA).

## Recipes applied (`references/mascot_robot_recipes.md`, credits in technique_bank.md)
- **Hook shows the problem, not a slogan** (arc chaos → control → clarity → brand).
- **Camera never still**: one eased move per scene, each scene starts at the previous end zoom, slow push.
- **Spring motion / nothing appears from nothing**: agents, pillars, cards and rows all grow or rise in.
- **Beat-locked changes**: agents, stall cards, gaps, phrases and rows land on the word that names them.
- **Robot as co-host**: two side rises (`upR` beside gap card 1 on the left half, `upL` beside gap card 2 on
  the right half), bottom-band moves elsewhere, never centred over the element, never zoomed or cropped.

## Client rules checked
- One theme (navy), `#01ccf7` the only accent in UI text; no red/yellow UI.
- No reference product names, logos or UI; no price/income claims; no "comment X" CTA.
- Every in-world text is a canvas texture with auto-shrink (`fitFont`/`safeText`) so nothing can be sliced;
  verified in snapshots that no card, label or row is cut by the frame or hidden behind the tab/chip/captions.
- Captions in the Automation band (1256–1374), above the robot layer.
- No frame where the stage is empty mid-transition (the agent grid, the stalls and the review wall are all
  up before their transition lands).
