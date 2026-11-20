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
