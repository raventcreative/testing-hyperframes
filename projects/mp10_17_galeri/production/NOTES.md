# MasterPajak AI · Video 17: Bukti Transfer Nyelip di Galeri

1080×1920 · **34.06 s** (`TM.total` = `data-duration` = 34.06) · HyperFrames 0.8.186 (kit and series ending from Video 14).
Built VO-first (batch 3 workflow). Not rendered and not committed here: the lead renders, mixes the music and commits.

## Concept
A phone gallery is where proof of payment goes to hide.

- **Light 3D studio (problem).** A large tilted phone (sliced 3D body, generic UI) shows a gallery grid. The tiles are our own
  flat illustrations: selfies (two in hijab), food (kopi, mie, sate, es teh), memes with our own captions, sunsets, mountains, a
  cat, a plant and product shots. Hidden among them are three generic "Transfer berhasil" screenshots and three receipt photos.
  - Thumb flicks scroll the grid with a vertical motion blur (an SVG `feGaussianBlur` animated with `attr`), a touch-point trail
    and a small handheld shake.
  - A transfer is found (yellow ring), then slips away on "nyelip".
  - On "selfie" and "foto makanan", those tiles lift off the screen with label chips.
- **Brand (navy).** The photos drop into a generic upload app ("Unggah foto nota · MasterPajak AI", "Simulasi alur"). They are
  sorted into a calm **Album nota** with one row per tanggal, then become rows of a MasterPajak AI **Pembukuan**.
  - One row traces back to its source photo (a "BUKTI ASLI" callout).
  - A lens runs down the date column and finds the 5 Nov transfer that was "kelewat" in the rekap.
- **Close.** A split screen: the calm gallery phone (personal photos only, "♥ kenangan") next to the pembukuan ("✓ nota
  tercatat"). Then the series end card.

## VO (ElevenLabs, client voice, default AUTO tags, generated once, no failures)
`production/vo/lines.txt` → `VO_MP17.mp3` / `VO_MP17.json` (32.16 s). Per-word times are in `production/vo/words_MP17.json`.
`assets/audio/vo.wav` is the mp3 delayed by 0.30 s (48 kHz mono).

| # | tags used (auto) | line | VO (s) | timeline (s) |
|---|---|---|---|---|
| 1 | [playful] [excited] [curious] | Bukti transfer pembeli nyelip di galeri, di antara selfie sama foto makanan? | 0.08–4.48 | 0.38–4.78 |
| 2 | [playful] [excited] [sighs] | Scroll atas, scroll bawah, nota belanja numpuk bareng meme. | 5.20–9.16 | 5.50–9.46 |
| 3 | [playful] [excited] | Pas mau rekap, ada aja yang kelewat. | 9.43–11.64 | 9.73–11.94 |
| 4 | [playful] [excited] | Mulai sekarang, nota jangan cuma nginep di galeri. | 11.90–14.89 | 12.21–15.19 |
| 5 | [playful] [excited] | Unggah foto notanya lewat aplikasi MasterPajak AI, terus disusun rapi per tanggal. | 14.96–19.94 | 15.26–20.24 |
| 6 | [playful] [excited] | Masuk ke pembukuan yang bisa ditelusuri, jadi gampang dicari lagi. | 20.14–23.77 | 20.44–24.07 |
| 7 | [playful] [excited] | Galeri buat kenangan, nota buat pembukuan. | 23.84–26.57 | 24.14–26.87 |
| 8 | [playful] [excited] | Jualan jalan terus, pajaknya AI yang urus. | 26.64–29.77 | 26.94–30.07 |
| 9 | [playful] [excited] [confident] | Coba kalkulator gratis. Link di bio. | 29.84–32.16 | 30.14–32.46 |

**Listen-check** (faster-whisper `small`, numpy input): every word was transcribed and no tag was read aloud.
- The `[sighs]` tag is performed as an audible sigh just before line 2 (≈4.95–5.4 s on the timeline). This is intended.
- Whisper wrote "nyelip" as "ngelip" (p = 0.78) and "meme" as "mim". These are most likely ASR spellings, but worth one listen.

## TM keys (all from real word times + 0.30)
- `hook` 0.38 · `tf` 0.70 · `nyelip` 1.46 · `selfie` 3.10 · `makan` 3.82
- `scroll` 5.50 · `bawah` 6.673 · `nota` 7.66 · `numpuk` 8.30 · `meme` 9.06
- `rekap` 9.725 · `ada` 10.62 · `lewat` 11.34
- `mulai` 12.205 · `nota2` 13.02 · `jangan` 13.50 · `nginep` 13.98 · `galeri2` 14.42
- `sol` 15.26 · `app` 16.50 · `mpai` 17.10 · `susun` 18.407 · `tgl` 19.42
- `led` 20.442 · `telusur` 21.66 · `cari` 22.46 · `dicari` 23.18
- `kenang` 24.14 · `notab` 25.34
- `end` 26.94 · `cta` 30.14 · `bio` 31.58
- `total` 34.06 (the last word ends at 32.46, followed by a 1.6 s end-card hold)

## Scenes
| # | time (s) | VO | what happens |
|---|---|---|---|
| S1 | 0 – 5.5 | L1 | **Hook (light 3D).** The camera starts close on the tilted gallery phone, mid-flick (motion blur). On "transfer", a transfer screenshot lands under a yellow ring. On "nyelip", three frantic flicks lose it again. On "selfie" and "foto makanan", those tiles lift out with chips. The camera pulls back and the robot hops in at bottom-right. Text: "Bukti transfer" (stabilo) / "nyelip di galeri?". |
| S2 | 5.5 – 9.7 | L2 | "scroll atas" is a long flick up, "scroll bawah" a flick down and settle (blur, touch trail, the robot's head follows). On "nota belanja", three receipt tiles ring yellow. On "numpuk", the robot sighs. On "meme", the meme tiles wobble. Text: "scroll atas, scroll bawah…" / "nota belanja" / "numpuk (stabilo) bareng meme." |
| S3 | 9.7 – 12.2 | L3 | A "REKAP TRANSFER" card (Ilustrasi data) swings in beside the phone. The 3 Nov and 4 Nov rows fill as their tiles ring. The 5 Nov row stays dashed ("Rp ???") and gets a "kelewat" chip and a shake. A "?" pops on the missed transfer tile in the gallery. The robot shrugs. Text: "pas mau rekap," / "ada aja yang kelewat (stabilo)." |
| S4 | 12.2 – 15.3 | L4 | The rekap card leaves and the gallery greys out. The six key photos lift off the screen with yellow rings (overlay rig). The robot shakes its head on "jangan" and points on "nginep". On "di galeri." the photos fly up out of frame. Text: "mulai sekarang," / "nota jangan cuma" / "nginep (stabilo) di galeri." |
| T | 14.78 – 15.34 | | Series band sweep with the "MasterPajak AI" marquee. |
| S5 | 15.26 – 20.44 | L5 | **Brand (navy).** The robot rises half-body bottom-left with the chest hologram (x ≈ 520–940, y ≈ 1550). The upload app phone swings in, the six photos drop from above the frame into its slots (checks, progress bar, "6 foto terunggah"), and "MasterPajak AI" lands on the word. On "terus disusun", the phone steps back-left and the **Album nota** card swings in. The photos sort into three date rows (3/4/5 Nov), and the date pills flash on "per tanggal". Captions: "unggah foto notanya lewat aplikasi" / "MasterPajak AI", then "terus disusun" / "rapi per tanggal." (underline). |
| S6 | 20.44 – 24.14 | L6 | The album recedes and fades. The **Pembukuan** card lifts in and its six rows fill (tanggal · keterangan · nominal · bukti thumbnail). On "ditelusuri", row 3 highlights and its "BUKTI ASLI" callout shows the source screenshot. On "dicari", a lens slides down the date column to row 5, the formerly missed Rp95.000 transfer, which flashes and gets a check. Captions: "masuk ke pembukuan yang" / "bisa ditelusuri." (underline), then "jadi gampang dicari lagi". |
| S7 | 24.14 – 26.94 | L7 | Split screen: the pembukuan steps right and shrinks, and the calm gallery phone (personal photos only) slides in on the left. Badges "♥ kenangan" and "✓ nota tercatat". Captions: "Galeri buat kenangan," / "nota buat pembukuan." (yellow keywords). |
| T | 26.44 – 27.44 | | Series beam flood and iris. |
| S8 | 26.94 – 34.06 | L8–L9 | Series end card: the tagline in two lines, the CTA pill "Coba kalkulator gratis" on `cta`, "Link di bio" on `bio`. The robot waves and points, with the logo hologram on the left. |

**Holograms:**
- The brand hologram is at full alpha from 15.98 to 26.64 s (10.7 s).
- The end-card hologram runs from 27.69 to 34.06 s (6.4 s).
- Both stay inside the safe zone (x 120–960, y ≤ 1600).

## Labels and brand rules
- **"Ilustrasi data"** appears on everything that shows demo amounts:
  - the gallery phone header
  - the rekap card
  - the upload app
  - the album
  - the pembukuan card
- **"Simulasi alur"** appears on every app flow: the upload app, the album and the pembukuan.
- **Amounts are consistent everywhere.** Transfers are Rp185.000 / Rp240.000 / Rp95.000. Receipts are kemasan 120.000, bahan
  baku 350.000 and ongkir 68.000.
- **Dates.** "3–5 Nov" are illustrative transaction dates, not obligation dates.
- **Nothing forbidden.** There are no tax rates, deadlines, penalties or guarantees.
- **Features are named only** as "unggah foto nota lewat aplikasi", "pembukuan yang bisa ditelusuri" and "kalkulator gratis"
  (end card).
- **No logos or brand colours.** There are no app, marketplace, bank or e-wallet names, logos or colours:
  - the transfer screenshots are generic white/navy
  - the camera/gallery UI is generic
  - the tiles are our own illustrations
- **No real people.** There are no photos of real people; selfies are simple flat avatars. The meme captions are our own
  ("KOK UDAH / SENIN?", "GAJIAN / MODE ON", "AKU / TIAP PAGI") on our own cartoon cat, blob and frog.
- **Tagline and CTA** are exact. The spelling "MasterPajak AI" is used throughout.

## Tech notes (real-runtime lessons applied)
- **Overlay rig.** The lifted tiles, the "?" badge and the rekap card live in an **overlay rig** (`#w1b`). It is a camera twin
  plus a phone-transform twin (`#phB`), so it is never depth-sorted against the phone's slices. The tiles hand over from the grid
  (hidden) to their overlay clones at the same pose.
- **Pinned visibility.** In the first real-runtime pass, every key tile was blank from 0 s, because a later `visibility:hidden`
  set leaked backwards. All tile visibility, rotation and scale is now pinned at 0, along with every initial state, through
  `init()` = `gsap.set` + `tl.set(…, 0)`.
- **Opacity.** Only flat elements get fractional opacity. Phone groups only switch 0/1 with `autoAlpha`. The album fades on its
  flat card.
- **Captions above the stage.** Navy captions sit above the 3D stage in DOM order, so a moving card can never cover a spoken
  line. An album exit that covered "bisa ditelusuri." for about 0.4 s was fixed this way.
- **Measured landings.** The upload landing points (`FLAND`) were measured in the browser at each landing time.

## QA done (final build)
- **`hyperframes validate`:** 0 errors. `lipsync.js` exists, so there are no 404s. The contrast warnings are only the meme
  captions (white text with a black outline; the checker ignores the stroke).
- **Real-runtime snapshots** (`npx hyperframes@0.8.186 snapshot`) covered every scene, transition midpoint and caption swap, and
  the end card. Contact sheets are in the scratchpad `mp17/`:
  - `QA_final_A/contact-sheet-1..2.jpg` (0.3–14.95 s)
  - `QA_final_B/contact-sheet-1..2.jpg` (15.15–33.9 s)
  - `QA_final_C/contact-sheet.jpg` (album-exit fix)
  - `QA_final_D/contact-sheet.jpg` (caption-swap midpoints)
- **Text containment:** every visible text run sits inside its nearest block container at 11 held moments (0 hits).
- **Frame-edge sweep** every 0.2 s: the only hits are
  - objects entering or leaving (single frames)
  - the series marquee
  - tiles at the bottom edge in the close hook shot (see below)
- **Audio:** `tools/sfx.py` → `assets/audio/sfx.wav` (34.06 s, synthesised, keyed to TM). `tools/lipsync.py` → `lipsync.js`.

## Known issues / notes for the lead
- **Hook crop.** In the close hook shot (0–4.5 s), the phone runs past the frame bottom, so the bottom tile row is cropped by the
  camera. This is a 3D camera framing under the IG UI zone, not flat text.
- **Callout.** The "BUKTI ASLI" callout covers the nominal column of pembukuan rows 1–2 for about 0.8 s (21.8–22.5 s). It is a
  deliberate popover; it points at row 3.
- **Transitions.** Brief overlaps while objects swap:
  - rekap card exit (12.2–12.7 s)
  - album entry (18.4–18.7 s)
  - upload phone exit (20.4–21.0 s)
  - calm gallery entry (24.1–24.5 s)
- **Cropped text.** These moving objects are cropped by the frame edge for a few frames. As in the approved videos, the text
  never overflows its own box.
- **VO length.** The VO runs to 32.46 s, so the end-card hold is 1.6 s after "Link di bio".
- **File size.** `index.html` is about 87 KB, because the tile illustrations are inline SVG generated in the script.
