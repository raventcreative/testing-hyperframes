# Covers (thumbnails) — 1080×1920 + HD 2160×3840 (render with DSF=2)

## Topic cover (navy or white, matching the video's theme) — template `templates/thumbnail/cover_navy_minimal.html`
Client: "kebanyakan elemen, gak ada negative space, gak elegan" → minimal only:
- logo (top centre) · one chip (e.g. `PROMPT GRATIS`, cyan outline on navy) · 2-line headline (line 1 white,
  line 2 cyan gradient on navy / blue gradient on white) · short tagline · the 3D mascot (bottom centre, cut from a
  still: `tools/still.cjs <port> <t> <out> host`) · **ONE topic logo in 3D floating above the mascot's head**
  (`templates/thumbnail/logo3d.html?name=meta|tiktok|instagram|claude…` via `tools/logo3d.cjs`; topic TikTok → TikTok,
  "3 AI" → those three AI logos in a row). Background = the brand plate + one soft cyan glow. Nothing else.
- Free/value hooks are welcome ("orang tertarik sama yang gratis") but the number must be TRUE: the cover promise must
  equal what DM_<KEYWORD>.md delivers (R26: "50 Hook Iklan / Dari 1 Prompt", not "30 prompt").

## Testimonial cover (white) — template `templates/thumbnail/cover_testimoni_white.html`
- Photo: subject sharp, room blurred + lifted to white (high-key), thin navy grid behind the subject only, white
  gradients top/bottom. `scripts/thumb/testi_build_bg.py` (photo + client cut-out as matte) or
  `testi_build_from_screenshot.py` (LaMa removes burned-in captions/watermarks, Real-ESRGAN ×2 ×2, GFPGAN face, u2net matte).
- Text: logo, "TESTIMONI PESERTA", "Kata Mereka Setelah / Belajar AI", name tag lower-left (see brand.md). Name given by
  the client (e.g. "DEBI KURNIAWAN", "Owner 8 Bidang Usaha · Lamongan"); keep it inside 820 px width.

## Face/real-person covers (navy, e.g. "5 Level Adopsi AI", "1 Orang Bisa Mimpin 100 AI Agent?")
Client photo full-bleed, navy gradients top/bottom, grid behind subject, logo + eyebrow + 2-line headline + tagline,
Real-ESRGAN + GFPGAN when the source is small. Use the client's exact headline text when given.
