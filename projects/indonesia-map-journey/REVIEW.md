# REVIEW — Indonesia Map Journey, revision 2

Feedback addressed (user, rev 1 draft): map too white/plain → realistic map; add clouds; much more and more realistic sound; highlight each city with its boundary when zooming in.

Status: map, camera, clouds, boundaries, sound and timing are done and checked. **The 24 landmark photos are still placeholders**: the environment's network policy refuses `commons.wikimedia.org` / `upload.wikimedia.org` (proxy 403). Nothing was substituted.

## What changed
- **Relief basemap** from real elevation + bathymetry (AWS Terrain Tiles, Terrarium): hypsometric land tint × hillshade, bathymetric ocean tint × seafloor shade. 1,675 WebP tiles (z4–10) baked only along the camera path (`tools/bake_tiles.py`), drawn as a tile pyramid on the canvas with ancestor fallback; the render waits for exact tiles (`hf-seek` + `waitUntil`).
- **Satellite close-ups**: cloud-free Sentinel-2 L2A mosaics per destination (`tools/bake_satellite.py`): 6 dry-season passes per MGRS tile, SCL cloud mask, per-pixel median, shared acquisition dates across neighbouring tiles, colour matching + 70 px feathered seams, swath-edge holes filled from other passes (`tools/patch_holes.py`). Crossfades in during the last part of each descent. Bali: imagery only for the island (official province mask), so Bali reads as the destination inside the relief view.
- **Official boundaries** (geoBoundaries, BPS/OCHA, CC BY 3.0 IGO): Kota Surabaya, Kota Medan, Kota Surakarta, Kota Bandung, Kota Yogyakarta, Kota Makassar, DKI Jakarta (5 kota, inner lines shown), Provinsi Bali. Drawn on in 1.1 s at landing with a light fill; fades at departure. Markers moved from Natural Earth points to the boundary centroids (shift 0.8–8.2 km; Bandung's old point sat on the boundary edge).
- **Clouds**: 10 seeded volume-lit cumulus sprites, 46 cloud systems with perspective parallax and ground shadows; a fly-through bank over every destination during its descent; none during photo holds; none over markers/labels in the final frame; no drift after 79.8 s (still ending).
- **Sound**: synthesised air bed driven by the camera (≈ −18 dB in travel, ≈ −30 dB at holds, rush pans with the direction of travel, gusts in the cloud layer) + 103 cues: whoosh per travel, click + low thump per landing, pen-trace per boundary draw, tick per connector, paper swish per frame (3 takes rotated), reverse swish per retract, Bandung locator clicks, closing chime + swell.
- White UI on the darker map (routes, labels, titles, light trace, pulses).

## Measured
- `npx hyperframes check --json`: ok, 0 errors. Fixed after it: overlapping audio lanes (bed on its own track, cues packed into non-overlapping lanes), audio slots set to the real file lengths, closing labels now ≥ 2 s, map labels 28 px. Kept: `nested_structure_needs_subcomposition` / `composition_file_too_large` (map + camera live in index.html by brief), `canvas_content_at_edge` (full-bleed map), two `text_below_floor` hits sampled while a frame is still scaling up (labels are 24–28 px at rest).
- Satellite coverage: Surabaya 1.00, Yogyakarta 1.00, Solo 1.00, Makassar 1.00, Bandung 0.998, Medan 0.994, Jakarta 0.991; Bali island fully covered except a ~15 px notch on the north coast (relief shows through).
- Texture-edge audit over all 2,460 camera frames: no frame shows the edge of a satellite texture while it is visible (one Yogyakarta frame at 69.33 s at alpha ≈ 0).
- Draft render `out/draft-rev2.mp4` (local, `--quality draft`): H.264 1920×1080, 30/1 fps, 82.000 s, 2,460 frames; AAC 48 kHz 82.000 s. Mix −16.9 LUFS integrated, −1.2 dBTP, no clipping (after a +4.5 dB master gain; first pass measured −21.4 LUFS). Frames extracted from the MP4 at 12 beats confirm every relief tile and satellite texture loaded in the render.

## Not checked / weakest
- Real photos (blocked). Sound measured, not heard.
- Some ocean areas inside the Jakarta/Medan mosaics still show faint rectangular tone shifts between passes.
- At the very start of each satellite crossfade the relief tile level is z10 (≈150 m/px), slightly soft for ~0.3 s.
