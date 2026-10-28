#!/usr/bin/env bash
# Assemble MASTERPAJAK_AI_PREMIUM_3D_MOTION_PACKAGE(.zip) from the final renders.
set -euo pipefail
cd "$(dirname "$0")/.."
FINAL=out/final
NAME=MASTERPAJAK_AI_PREMIUM_3D_MOTION_PACKAGE
PKG=out/package/$NAME
rm -rf out/package && mkdir -p "$PKG"/{01_FINAL_VIDEOS/BONUS_TRANSPARENT_ALPHA_WEBM,02_PREVIEW/contact_sheets,03_SOURCE_PROJECT,04_ASSETS/{fonts,brand,textures},05_DOCUMENTATION}
V1=01_STEP_1_RESI_FLOATING_3D
V2=02_STEP_1_REKENING_KORAN_FLOATING_3D
V3=03_STEP_2_DOKUMEN_MENJADI_LAPORAN_KEUANGAN

# 01 final videos (exactly three MP4s) + optional alpha masters
for v in $V1 $V2 $V3; do
  cp "$FINAL/$v.mp4" "$PKG/01_FINAL_VIDEOS/"
  cp "$FINAL/${v}_ALPHA.webm" "$PKG/01_FINAL_VIDEOS/BONUS_TRANSPARENT_ALPHA_WEBM/"
done

# 02 previews: hero frames (last frame), contact sheets from the ACTUAL renders, combined silent preview
P=$PKG/02_PREVIEW
ffmpeg -v error -y -sseof -0.05 -i "$FINAL/$V1.mp4" -frames:v 1 -update 1 "$P/PREVIEW_RESI.png"
ffmpeg -v error -y -sseof -0.05 -i "$FINAL/$V2.mp4" -frames:v 1 -update 1 "$P/PREVIEW_REKENING_KORAN.png"
ffmpeg -v error -y -sseof -0.05 -i "$FINAL/$V3.mp4" -frames:v 1 -update 1 "$P/PREVIEW_LAPORAN_KEUANGAN.png"
python3 render/contact_sheet.py "$P/contact_sheets/CONTACT_01_RESI.jpg" --video "$FINAL/$V1.mp4" --times 0,0.3,0.6,0.9,1.2,1.6,2.2,3.1,3.4,4.5,5.6,6.98 --title "01 RESI — frames from the final render"
python3 render/contact_sheet.py "$P/contact_sheets/CONTACT_02_REKENING_KORAN.jpg" --video "$FINAL/$V2.mp4" --times 0,0.35,0.7,1.0,1.2,1.45,1.9,2.4,3.0,3.8,5.2,6.98 --title "02 REKENING KORAN — frames from the final render"
python3 render/contact_sheet.py "$P/contact_sheets/CONTACT_03_LAPORAN_KEUANGAN.jpg" --video "$FINAL/$V3.mp4" --times 0,0.6,1.3,2.2,2.9,3.6,4.3,5.0,5.9,6.4,6.95,7.3,7.65,7.9,8.15,8.45,8.8,9.3,9.8,10.98 --title "03 DOKUMEN -> LAPORAN KEUANGAN — frames from the final render"
printf "file '%s'\n" "$PWD/$FINAL/$V1.mp4" "$PWD/$FINAL/$V2.mp4" "$PWD/$FINAL/$V3.mp4" > out/package/concat.txt
ffmpeg -v error -y -f concat -safe 0 -i out/package/concat.txt -an -c copy "$P/COMBINED_PREVIEW_ALL_3_SILENT.mp4"
rm out/package/concat.txt

# 03 source project (no node_modules / caches / renders)
cp -r src render package.json package-lock.json .gitignore "$PKG/03_SOURCE_PROJECT/"
cp -r assets "$PKG/03_SOURCE_PROJECT/assets"

# 04 assets
cp assets/fonts/* "$PKG/04_ASSETS/fonts/"
cp assets/brand/* "$PKG/04_ASSETS/brand/"
cp out/export/textures/* "$PKG/04_ASSETS/textures/"

# 05 documentation (+ live verification report)
cp docs/*.md "$PKG/05_DOCUMENTATION/"
python3 render/verify.py "$PKG"/01_FINAL_VIDEOS/*.mp4 > "$PKG/05_DOCUMENTATION/VERIFICATION_REPORT.md"
cp out/qc/motion_all.png "$PKG/05_DOCUMENTATION/QC_MOTION_VELOCITY_PLOTS.png" 2>/dev/null || true

(cd out/package && zip -qr -X "$NAME.zip" "$NAME")
ls -la out/package
cat "$PKG/05_DOCUMENTATION/VERIFICATION_REPORT.md"
