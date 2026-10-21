"""Transcribe each VO segment (from the master WAV, sample-exact) with sherpa-onnx Whisper.
usage: python asr_segments.py <model_dir> <project_dir> <out_json> [lang]
"""
import json, sys, subprocess, numpy as np, sherpa_onnx, glob, os

model_dir, proj, out = sys.argv[1], sys.argv[2], sys.argv[3]
lang = sys.argv[4] if len(sys.argv) > 4 else "id"
enc = glob.glob(os.path.join(model_dir, "*encoder.int8.onnx"))[0]
dec = glob.glob(os.path.join(model_dir, "*decoder.int8.onnx"))[0]
tok = glob.glob(os.path.join(model_dir, "*tokens.txt"))[0]
rec = sherpa_onnx.OfflineRecognizer.from_whisper(
    encoder=enc, decoder=dec, tokens=tok, language=lang, task="transcribe",
    num_threads=4, tail_paddings=2000)

tl = json.load(open(os.path.join(proj, "production/audio_timeline.json")))
wav = os.path.join(proj, tl["master_audio"])
pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", wav, "-ac", "1", "-ar", "16000",
                      "-f", "f32le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(pcm, dtype=np.float32)

def run(samples):
    s = rec.create_stream(); s.accept_waveform(16000, samples); rec.decode_stream(s)
    r = s.result
    return r.text.strip(), list(getattr(r, "tokens", []) or []), list(getattr(r, "timestamps", []) or [])

res = []
for seg in tl["segments"]:
    a, b = int(seg["start_seconds"] * 16000), int(seg["end_seconds"] * 16000)
    text, toks, ts = run(x[a:b])
    # also transcribe the untouched original part as cross-check
    op = subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(proj, seg["asset"]), "-ac", "1",
                         "-ar", "16000", "-f", "f32le", "-"], capture_output=True, check=True).stdout
    text_o, _, _ = run(np.frombuffer(op, dtype=np.float32))
    res.append(dict(id=seg["id"], start=seg["start_seconds"], end=seg["end_seconds"],
                    text_master=text, text_original_part=text_o, tokens=toks, token_ts=ts))
    print(seg["id"], f'{seg["start_seconds"]:.3f}-{seg["end_seconds"]:.3f}', "|", text, "||", text_o, flush=True)
json.dump(dict(engine="sherpa-onnx whisper large-v3 int8", language=lang, segments=res),
          open(out, "w"), ensure_ascii=False, indent=1)
