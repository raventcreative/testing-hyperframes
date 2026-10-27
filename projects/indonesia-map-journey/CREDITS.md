# Credits

## Map data

- Relief & bathymetry: AWS Terrain Tiles (Terrarium), s3://elevation-tiles-prod — sources include SRTM (NASA/USGS), GMTED2010 (USGS), ETOPO1 (NOAA), and others listed at https://github.com/tilezen/joerd/blob/master/docs/attribution.md . Hillshade + hypsometric/bathymetric tint computed in tools/bake_tiles.py.
- Satellite close-ups: contains modified Copernicus Sentinel data (2020–2024), Sentinel-2 L2A via AWS Open Data (s3://sentinel-cogs). Cloud-masked (SCL) median mosaics computed in tools/bake_satellite.py; scene list in data/sat.json.
- City / province boundaries: geoBoundaries gbOpen IDN ADM2 & ADM1 (source: BPS – Statistics Indonesia, WFP, OCHA ROAP), CC BY 3.0 IGO. Jakarta = union of the five Kota Administrasi (Kepulauan Seribu not included).
- Natural Earth 10m (country polygons and land borders, populated places, lakes). Public domain. https://www.naturalearthdata.com/ (via github.com/nvkelso/natural-earth-vector)
- Clouds are procedural (seeded noise, tools/make_clouds.py) — decorative, not weather data.
- Destination anchors: Natural Earth populated places (city points). Bali anchor: centroid of the main Bali island polygon (Natural Earth 10m), used as a regional anchor, not a landmark position.
- Lines between destinations show the order of the video, not travel routes.

## Photographs (Wikimedia Commons)

| Destination | Landmark (on-screen label) | File | Author | Licence |
|---|---|---|---|---|
| surabaya | Patung Suro dan Boyo | NOT YET DOWNLOADED | - | - |
| surabaya | Tugu Pahlawan | NOT YET DOWNLOADED | - | - |
| surabaya | Masjid Nasional Al-Akbar | NOT YET DOWNLOADED | - | - |
| jakarta | Monumen Nasional | NOT YET DOWNLOADED | - | - |
| jakarta | Museum Fatahillah, Kota Tua | NOT YET DOWNLOADED | - | - |
| jakarta | Bundaran HI | NOT YET DOWNLOADED | - | - |
| medan | Istana Maimun | NOT YET DOWNLOADED | - | - |
| medan | Masjid Raya Al-Mashun | NOT YET DOWNLOADED | - | - |
| medan | Tjong A Fie Mansion | NOT YET DOWNLOADED | - | - |
| bali | Tanah Lot | NOT YET DOWNLOADED | - | - |
| bali | Pura Ulun Danu Beratan | NOT YET DOWNLOADED | - | - |
| bali | Garuda Wisnu Kencana | NOT YET DOWNLOADED | - | - |
| solo | Keraton Surakarta | NOT YET DOWNLOADED | - | - |
| solo | Pura Mangkunegaran | NOT YET DOWNLOADED | - | - |
| solo | Pasar Gede | NOT YET DOWNLOADED | - | - |
| bandung | Gedung Sate | NOT YET DOWNLOADED | - | - |
| bandung | Gedung Merdeka | NOT YET DOWNLOADED | - | - |
| bandung | Jalan Braga | NOT YET DOWNLOADED | - | - |
| yogyakarta | Tugu Yogyakarta | NOT YET DOWNLOADED | - | - |
| yogyakarta | Taman Sari | NOT YET DOWNLOADED | - | - |
| yogyakarta | Malioboro | NOT YET DOWNLOADED | - | - |
| makassar | Fort Rotterdam | NOT YET DOWNLOADED | - | - |
| makassar | Masjid 99 Kubah | NOT YET DOWNLOADED | - | - |
| makassar | Pantai Losari | NOT YET DOWNLOADED | - | - |

Photos were resized and cropped inside frames; no other changes. CC BY-SA photos remain under their licence.

## Fonts

- Montserrat (SIL Open Font License 1.1), via @fontsource/montserrat 5.3.0.

## Sound

- Bundled HyperFrames SFX (Pixabay Content License): see assets/sfx/CREDITS.md.
- bed_air, swish_*, trace, tick_* were synthesised / derived for this film (tools/make_sound.py).
