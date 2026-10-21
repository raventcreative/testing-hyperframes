import json, sys, subprocess, glob, os, numpy as np, sherpa_onnx
md, proj, wj, out = sys.argv[1:5]
g=lambda p: glob.glob(os.path.join(md,p))[0]
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=g("*encoder.int8.onnx"), decoder=g("*decoder.int8.onnx"),
      tokens=g("*tokens.txt"), language="id", task="transcribe", num_threads=4, tail_paddings=2000)
pcm = subprocess.run(["ffmpeg","-v","error","-i",os.path.join(proj,"assets/audio/vo_master_39s.wav"),"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True,check=True).stdout
x = np.frombuffer(pcm, dtype=np.float32)
d = json.load(open(wj)); res={}
for s in d["segments"]:
    r=[]
    for p0,p1 in s["pauses"]:
        mid=(p0+p1)/2; st=rec.create_stream(); st.accept_waveform(16000, x[int(s["start"]*16000):int(mid*16000)]); rec.decode_stream(st)
        t=st.result.text.strip(); r.append([p0,p1,t]); print(s["id"], p0, p1, "|", t, flush=True)
    res[s["id"]]=r
json.dump(res, open(out,"w"), ensure_ascii=False, indent=1)
