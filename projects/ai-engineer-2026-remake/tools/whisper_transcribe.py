"""Local multilingual transcription of the VO (faster-whisper, CPU, int8) for comparison with the script.
Run: <venv>/bin/python -I tools/whisper_transcribe.py <project>   -> production/whisper_transcript.json"""
import json, sys
from pathlib import Path
import subprocess, numpy as np
from faster_whisper import WhisperModel
P = Path(sys.argv[1]).resolve()
m = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else "small", device="cpu", compute_type="int8")
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(P / "assets/audio/voiceover_final.mp3"), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True, check=True).stdout
segs, info = m.transcribe(np.frombuffer(raw, dtype=np.float32), language="id", word_timestamps=True, beam_size=5,
                          initial_prompt="AI agent, AI Engineer, Python, debugging, software engineering, Git, database, backend, machine learning, deep learning, neural network, tensor, PyTorch, LLM, token, embedding, API, RAG, evaluation, production, deploy, training, roadmap.")
words = []
for s in segs:
    for w in s.words:
        words.append({"text": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3), "p": round(w.probability, 3)})
(P / "production/whisper_transcript.json").write_text(json.dumps({"model": "faster-whisper " + (sys.argv[2] if len(sys.argv) > 2 else "small"), "words": words}, indent=1, ensure_ascii=False))
print(" ".join(w["text"] for w in words))
