# Video 8 · Asisten AI vs Tim Ahli — production notes

Format 1080×1920, 31.7 s (`TM.total` = `data-duration` = 31.7). Title: "MasterPajak AI · Video 8 — Asisten AI vs Tim Ahli".
Tech skeleton unchanged from Video 1 (GSAP `tl` paused in `window.__timelines.main`, `F/show/hide`, backward-seek patch, robot
`onUpdate` line, end marker, `buildReady["layout"]` + `buildReady["robot"]`). No full render done (the lead renders).

## Concept
Two lanes in depth. **Hook (light):** a 3D versus set: "TANYA · AI" panel (navy, asisten AI) and "TANYA · AHLI" panel (yellow,
tim ahli · sesuai layanan) hinged like an open book on a perspective floor grid, a VS medallion floating in front, blurred "?"
bubbles at several depths. The robot host stands at the fork, looks at AI, then at AHLI, then shrugs. **AI lane (navy):** the camera
turns to the AI panel and dives through it; a tilted 3D chat (generic UI, "SIMULASI ALUR" chip) flies in from depth. The robot plays
the asisten AI: question "Angka laba ini dari mana?" → typing → answer "Dari data usahamu bulan ini: Penjualan / Biaya / Laba"
(digit roller + stabilo, "ILUSTRASI DATA"), then the user's own data cards (Catatan jualan, Foto nota, Pencairan) fly out of the
depth of field into the answer's source chips (312 pesanan · 46 nota · 3 pencairan). **AHLI lane:** whip pan right; a tangled case
file ("kasusnya rumit & butuh pertimbangan khusus", robot with X-eyes) flips over in 3D (navy iris) into the expert card
"Tim ahli · Muamalah Pajak · ✓ kasus rumit ✓ pertimbangan khusus · sesuai layanan". **Brand moment:** MasterPajak AI band sweep →
"kamu nggak sendirian." — Asisten AI and Tim ahli Muamalah Pajak (sesuai layanan) as two 3D wings linked to "usahamu", robot rises
with the chest hologram logo (~4.4 s). **End card:** series template (tagline, CTA "Coba kalkulator gratis", "Link di bio", robot
waves/points, logo hologram left, ~7 s).

Wording: the expert team always appears as "tim ahli … Muamalah Pajak … sesuai layanan"; no promise of results. The AI only
explains numbers from the user's data (no advice claims). No rates, deadlines, guarantees, DJP/government marks.

## TM keys ↔ VO lines (VO_SCRIPTS.md §8, planned at ~2.4 words/s)
| key | t (s) | VO |
|---|---|---|
| `q` | 0.3 | Kapan cukup tanya AI... |
| `q2` | 2.0 | kapan perlu tanya ahli? |
| `ai` | 4.4 | Pertanyaan ringan, kayak |
| `ask` | 5.6 | "angka laba ini dari mana?", |
| `ans` | 7.8 | asisten AI bantu jelasin |
| `dat` | 9.5 | dari data usahamu. |
| `ex` | 11.4 | Tapi kalau kasusnya rumit dan butuh pertimbangan khusus, |
| `tim` | 15.0 | ada tim ahli Muamalah Pajak, |
| `sl` | 17.1 | sesuai layanan. |
| `sol` | 18.6 | Jadi kamu nggak sendirian ngurusin pajak usahamu. |
| `end` | 24.0 | Jualan jalan terus, pajaknya AI yang urus. |
| `cta` | 27.5 | Coba kalkulator pajak gratisnya. |
| `bio` | 29.2 | Link di bio. |
| `total` | 31.7 | — |

Re-time: put the real VO word stamps into `window.TM` (keep `key: number` pairs), set `data-duration` = `TM.total`, re-run
`python3 tools/sfx.py`. Everything (scenes, robot, SFX) follows the keys. The gap `sol → end` (5.4 s) holds the brand hologram
≥ 4 s; if the real line 4 is short, keep `end ≥ sol + 5.0`.

## Scenes
| scene | TM span | background | depth / camera |
|---|---|---|---|
| S0 hook — versus set | 0 → ai | paper | panels open in 3D, floor grid, DOF bubbles, camera orbits to AI then AHLI, dive through the AI panel (blur + navy veil) |
| S1 AI lane — chat | ai → ex | navy | chat arrives from depth, data cards in DOF fly into the answer, slow push/orbit |
| S2 AHLI lane — case → expert | ex → sol | paper → navy | whip pan in, floating sheets in DOF, 3D card flip + iris, slow orbit |
| S3 brand — nggak sendirian | sol → end | navy | band sweep in, wings fly in in 3D, links + pulses, sparks at depth, orbit; chest hologram |
| S4 end card | end → total | deep | beam + iris in (series template), slow settle |

Robot (`robot_perf.js`): host at the bottom centre (S0) → glides bottom-left as the assistant (S1) → leaves with the whip (cut) →
bottom-right on the AHLI lane, X-eyes on the tangle, presents the expert card (S2) → ducks under the bands (cut) → half-body
bottom-left, hologram right at (720, 1470, w 420) (S3) → ducks under the beam (cut) → end card as Video 1 (hologram 360, 1500).
CUTS = `ex - 0.01`, `sol - 0.05`, `end - 0.01`. Lip-sync: `lipsync.js` not present yet (loaded with `onerror`, the 404 in the
console is expected until the VO exists).

## Labels / rules check
- "SIMULASI ALUR" on the chat UI; "ILUSTRASI DATA" inside the answer bubble whenever numbers / counts are on screen.
- Hologram on screen: brand ≈ 19.1 → 23.75 s, end ≈ 24.5 → 31.7 s; both inside x 120–960 / y ≤ 1600.
- QA: text-in-box containment check (custom) clean; frame-edge check only hits during the dive (4.2–4.4 s), whip (11.2 s) and
  band sweep (18.2–18.6 s) camera transitions. No other console errors.

## Files
`index.html`, `robot_perf.js`, `tools/sfx.py` → `assets/audio/sfx.wav` (31.7 s, 48 kHz mono), `thumbnail/cover.html` →
`thumbnail/COVER_MP08_ASISTEN_AHLI.png`.

## Not done / open
- No full render (by brief). Timing is planned, not measured against the real VO.
- The robot's arms cannot reach its head, so the "rumit" beat uses X-eyes + head wobble + a raised hand instead of a head scratch.
