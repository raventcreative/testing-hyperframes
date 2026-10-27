# REVIEW — Indonesia Map Journey (placeholder-photo build)

Status: **structure, camera, map, markers, routes, timing and sound are built and checked. The 24 landmark photos are NOT in the film yet** — the cloud environment's network policy refuses `commons.wikimedia.org` and `upload.wikimedia.org` (proxy `403` on CONNECT; also Flickr, Unsplash, Pexels, Openverse, Wikipedia). Every photo frame currently shows a hatched "FOTO MENUNGGU AKSES WIKIMEDIA" placeholder at the photo's expected orientation. Nothing was substituted.

## Creative calls
- Map rebuilt from Natural Earth 10m (public domain) on a 2D canvas in Web Mercator; one projection function drives land, bathymetry, routes, markers and labels (`index.html`, `tools/build_geo.py`).
- Depth = real Natural Earth bathymetry polygons (200 / 1000 / 3000 m). No invented terrain (no elevation data reachable from this environment).
- Camera = van Wijk–Nuij smooth zoom-pan: the camera climbs higher for long moves (Medan → Bali reaches a Sumatra–Java–Kalimantan altitude) and stays low for Java hops. Deterministic function of time; exact states in `CAMERA.md`.
- Camera is dead still while photos are open, so connectors stay attached; ambient motion = 3.5 % photo push.
- Bali = regional: island polygon highlight + dashed halo; no pin; routes stop at the halo edge; landmark connectors start on the halo, not a point. Visited Bali marker is a hollow ring (cities are solid dots).
- Destination titles auto-placed by the generator in the free space around the marker (collision-checked against cards and connectors).
- Map credit line states that the lines show the order of the video, not travel routes.
- Storylines not built: none — the brief fixed the storyboard.

## Measured (evidence)
- `npx hyperframes check --json`: ok, **0 errors**. Warnings kept: `nested_structure_needs_subcomposition` and `composition_file_too_large` (the brief asks for map + camera + markers in `index.html`); `canvas_content_at_edge` (full-bleed map, intended). `text_below_floor` from placeholders/credits/labels was fixed (labels 28 px, map labels 26 px; credits 13 px marked `data-layout-ignore`). Closing "INDONESIA" now holds > 2 s.
- Marker accuracy: every anchor lies inside an Indonesian land polygon; nearest-coast distance: Surabaya 3.6 km, Makassar 3.3 km, Jakarta 7.9 km, Medan 22.9 km, Yogyakarta 27.5 km, Bandung 63.7 km, Solo 69.5 km, Bali centroid 23.4 km — consistent with real geography.
- Seams (`snapshot --review`, ±0.2 s around each scene boundary): continuous camera, no jumps, no black frames.
- Seek-order determinism: frames at 9 / 30.5 / 45 / 51.5 / 81.9 s snapshotted in forward and reverse order: 30.5 and 81.9 s pixel-identical; others differ only by anti-aliasing (≤ 3/255, max 19/255 on < 1 000 px of a line edge) — visually identical.
- Generator layout check: no card overlaps, no connector crossing a card or title, all cards inside the 80 px safe margin.
- Photo read windows: 9 s blocks ≈ 4.0 s with all three open; 8 s blocks ≈ 3.5 s.

## Not checked / cannot be checked yet
- Real photos: content, crop, landmark visibility, label accuracy (Pasar Gede interior?, Fort Rotterdam building?).
- Sound was measured (cue timing), not heard. No music: none supplied.

## Weakest shots / next changes
- Travel stretches between cities show only coastline + trail (deliberately clean); with real photos the contrast between empty travel and rich holds should feel right — re-check after photos land.
- Natural Earth 10m coastline is slightly faceted at the Bali zoom (span 4.8°). Acceptable; a higher-resolution coastline source is not reachable here.
- Card proportions will change to each real photo's aspect; re-run `node tools/build.mjs` and re-check the collision report.
