# Indonesia Map Journey — 82 s, 1920 × 1080, 30 fps

Map film: Indonesia → Surabaya → Jakarta → Medan → Bali → Solo → overview (5) → Bandung → Yogyakarta → Makassar → final (8).

## Files
- `data/plan.json` — single source of truth: coordinates, block timing, camera spans, marker screen positions, photo slots.
- `data/photos.json` — 24-photo manifest (file, size, author, licence, source, on-screen label, focus point).
- `tools/build.mjs` — generates `compositions/<city>.html`, `data/plan.js`, `index.html`, `data/sfx.json`, `CAMERA.md`; prints a layout collision report.
- `tools/index.template.html` — root composition source (map canvas, camera, routes, markers). Edit this, not `index.html`.
- `tools/build_geo.py` — Natural Earth 10m → `assets/maps/geo.js`.
- `tools/commons_photos.py` — Wikimedia Commons search / pick / credits.
- `SPEC.md`, `STORYBOARD.md`, `CAMERA.md`, `REVIEW.md`, `CREDITS.md`.

## Finish the photos (needs network access to Wikimedia)
Allow `commons.wikimedia.org` and `upload.wikimedia.org` in the cloud environment (Network access → Allowed domains), then:

```bash
python3 -I tools/commons_photos.py fetch             # candidates + contact sheets in assets/photos/_candidates/<id>/
# inspect each sheet.jpg, then per landmark:
python3 -I tools/commons_photos.py pick sby-tugu 02 --focus 0.5,0.35
python3 -I tools/commons_photos.py credits
node tools/build.mjs                                  # frames adapt to the real aspect ratios
npx hyperframes check --json && npx hyperframes snapshot --review
npx hyperframes render --quality draft -o out/draft.mp4   # review; final render only after approval
```
