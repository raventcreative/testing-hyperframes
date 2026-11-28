# Client rules & feedback log (why the format is what it is)

- **ATM remake**: amati-tiru-modifikasi, never copy-paste. Own hook/angle/order/metaphors/CTA; ≤3 consecutive words of
  the reference; no reference names/greetings/donation lists; verify facts, drop unverifiable claims (e.g. a creator's
  "27 ads in Meta Ad Library"). No invented results for Freddie.
- **Mascot required**: "tetap ada maskot 3D saya". Flow the client designed: "tunjukin dunia voxel dulu, terus zoom out,
  terus maskot 3D-nya keluar, habis itu dia jelasin".
- **More creative, not boring**: "transisi sama motion jangan itu-itu aja" — vary transitions and motion per beat.
- **Text must never be cut** ("kamu harus teliti"): canvas texture text uses fitFont/safeText (shrinks to fit), frame whole
  objects, no text behind flying objects, labels above the caption band. Audit every second before rendering.
- **Logos**: always sourced from open-source sets on the web (Simple Icons CC0) and built as animated 3D objects.
- **Brand colours only** in UI (no red/yellow); thumbnails minimal with negative space + one topic logo above the mascot.
- **Readable captions**: bold everywhere, boxed, never over the mascot face.
- **VO**: ElevenLabs, voice Dakocan (`plgKUYgnlZ1DCNh54DwJ`), model `eleven_v4`, stability 0.41 / similarity 0.75 /
  style 0, auto tags (`[playful] [excited]` + one context tag). If the user says "gak ada suara VO", verify with whisper
  on the final MP4 and send the extracted audio; usually the in-app preview is muted.
- **Deliverables always**: video + thumbnail (+HD) + DM file + caption. The client asks "mana thumbnail/VO-nya" if missing.
- Google Drive uploads only when asked. Never paste API keys in chat.
- When the client is in a hurry, give honest ETA (render ≈ 23 min per 58 s of 3D) and offer the preview with its known flaws,
  but recommend the final.
- **Real screen recordings** (2026-11-20): if a reel shows a website or social media (IG, TikTok, WhatsApp, web), ask
  Freddie to screen-record his own account/website and use that real footage (phone/browser frame, crop, zoom, cursor
  highlights) instead of mock UI. Tell him exactly what to record (screens, ~10–20 s each, 9:16) at the start of the job.
- **Stored recordings, use automatically** (2026-11-21): `brand/rec/` holds his IG, website and Claude Code recordings (README lists them). If a reel's topic matches, use the recording in that reel and name it in the brief — the client said "pakai aja kalau ada pembahasan yang menyangkut". Missed in batch 8 (R31/R34 fixed after).

## 2D reels — mascot staging + no counter (client, 2026-11-28)
"Pas ngejelasin maskot 3D-nya majuin sampai setengah badan … kalau ngasih contoh maskot 3D-nya hilangin biar video contohnya aja
… foto 02/24 itu hilangin … jangan pakai dunia voxel."
- Explaining beats (hook, why it matters, CTA): the 3D mascot comes forward BIG, half-body (waist-up, cropped by the frame
  bottom), lip-synced, under the spoken headline — animated push-in/rise, never a pop.
- Example / demo beats (cards, UI windows, diagrams): the mascot is fully hidden; the example gets the whole frame.
- No beat counter ("02 / 24" pill) in any reel.
