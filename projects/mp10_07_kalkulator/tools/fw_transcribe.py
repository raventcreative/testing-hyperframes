"""Word-level transcription with faster-whisper (CPU int8). Usage: python3 fw_transcribe.py <audio> <out.json> [model] [lang]"""
import json, sys, time
from faster_whisper import WhisperModel
import subprocess, numpy as np

audio, out = sys.argv[1], sys.argv[2]
model_name = sys.argv[3] if len(sys.argv) > 3 else "large-v3"
lang = sys.argv[4] if len(sys.argv) > 4 else "id"
t0 = time.time()
model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=4)
pcm = subprocess.run(['ffmpeg','-v','error','-i',audio,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True,check=True).stdout
samples = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
segs, info = model.transcribe(samples, language=lang, word_timestamps=True, vad_filter=False, beam_size=5,
                              condition_on_previous_text=False)
res = {"language": info.language, "duration": info.duration, "segments": []}
for s in segs:
    res["segments"].append({"start": s.start, "end": s.end, "text": s.text.strip(),
                            "words": [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 3)} for w in (s.words or [])]})
    print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text.strip()}", flush=True)
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
print("done in", round(time.time() - t0, 1), "s")
