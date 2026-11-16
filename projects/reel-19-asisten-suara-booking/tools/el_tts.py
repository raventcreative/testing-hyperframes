"""ElevenLabs TTS for the AI PRENEUR reels (the client's own cloned voice). The API key is injected by the session's network proxy
(header xi-api-key) — never stored here. Usage: python3 tools/el_tts.py "<text with optional [playful]/[excited] tags>" out.mp3
Voice defaults = the client's ElevenLabs settings (tools/voice_config.json)."""
import json, sys, urllib.request, urllib.error
from pathlib import Path
CFG = json.loads((Path(__file__).parent / "voice_config.json").read_text())
text, out = sys.argv[1], sys.argv[2]
body = {"text": text, "model_id": CFG["model_id"], "voice_settings": CFG["voice_settings"]}
if CFG.get("language_code"): body["language_code"] = CFG["language_code"]
req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{CFG['voice_id']}?output_format={CFG.get('output_format', 'mp3_44100_128')}",
                             data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "Accept": "audio/mpeg", "xi-api-key": "proxy-injected"}, method="POST")
try:
    with urllib.request.urlopen(req, timeout=180) as r: Path(out).write_bytes(r.read())
    print("ok", out, Path(out).stat().st_size, "bytes")
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode()[:600]); sys.exit(1)
