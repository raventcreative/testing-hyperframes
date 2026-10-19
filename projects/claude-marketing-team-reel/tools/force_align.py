"""Forced alignment of the corrected Indonesian script against the real VO using pocketsphinx (PyPI,
bundled en-us acoustic model) + a rule-based Indonesian G2P mapped to CMU phones.
Writes transcript.json: [{text, start, end}] with display spellings (Claude, SKINKU, Higgsfield, ...)."""
import json, re, subprocess, sys, os
from pocketsphinx import Decoder, get_model_path

SRC, OUT, SCRIPT = sys.argv[1], sys.argv[2], sys.argv[3]
LOAN = {"plugin":"P L AH G IH N","claude":"K L AO D","marketing":"M AA R K AH T IH NG","full":"F UH L",
 "skill":"S K IH L","campaign":"K AE M P EY N","live":"L AY V","website":"W EH B S AY T","copy":"K AO P IY",
 "server":"S ER V ER","mcp":"EH M S IY P IY","ai":"EY AY","agent":"EY JH AH N T","higgsfield":"HH IH G Z F IY L D",
 "skinku":"S K IH N K UW","upload":"AH P L OW D","scale":"S K EY L","up":"AH P","link":"L IH NG K",
 "dm":"D IY EH M","meta":"M EH T AH","16":"AH N AA M B AH L AA S","7":"T UW JH UW","nge":"NG AH",
 "nya":"N Y AA","gua":"G UW AA","lu":"L UW","visual":"V IH S UW AA L","visualnya":"V IH S UW AA L N Y AA"}
V = {"a":"AA","i":"IY","u":"UW","e":"AH","o":"AO"}
C = {"b":"B","c":"CH","d":"D","f":"F","g":"G","h":"HH","j":"JH","k":"K","l":"L","m":"M","n":"N","p":"P",
     "q":"K","r":"R","s":"S","t":"T","v":"F","w":"W","x":"K S","y":"Y","z":"Z"}
def g2p(w):
    if w in LOAN: return LOAN[w]
    out=[]; i=0
    while i < len(w):
        two=w[i:i+2]
        if two=="ng": out.append("NG"); i+=2; continue
        if two=="ny": out.append("N Y"); i+=2; continue
        if two=="sy": out.append("SH"); i+=2; continue
        if two=="kh": out.append("HH"); i+=2; continue
        if two=="ai" and (i+2==len(w)): out.append("AY"); i+=2; continue
        if two=="au" and (i+2==len(w)): out.append("AW"); i+=2; continue
        ch=w[i]
        if ch in V: out.append(V[ch])
        elif ch in C: out.append(C[ch])
        i+=1
    return " ".join(out)

disp = open(SCRIPT).read().split()
tokens=[]  # (display_index, token)
for di,w in enumerate(disp):
    clean = re.sub(r"[,.:?!‘’']", "", w)
    for part in clean.split("-"):
        if part: tokens.append((di, part.lower()))
words = sorted(set(t for _,t in tokens))
dpath = os.path.join(os.path.dirname(OUT) or ".", "tools", "id.dict")
with open(dpath,"w") as f:
    for w in words: f.write(f"{w} {g2p(w)}\n")


pcm = subprocess.run(["ffmpeg","-v","error","-i",SRC,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True,check=True).stdout
HMM=os.path.join(get_model_path(),"en-us","en-us")
dec = Decoder(hmm=HMM, dict=dpath, samprate=16000, loglevel="FATAL", beam=1e-60, wbeam=1e-40, pbeam=1e-60)
dec.set_align_text(" ".join(t for _,t in tokens))
dec.start_utt(); dec.process_raw(pcm, full_utt=True); dec.end_utt()
seg=[(re.sub(r"\(\d+\)$","",x.word), x.start_frame/100.0, (x.end_frame+1)/100.0) for x in dec.seg() if x.word not in ("<s>","</s>","<sil>","(NULL)")]
assert [w for w,_,_ in seg]==[t for _,t in tokens]
res=[]
for (di,tok),(w,a,b) in zip(tokens,seg):
    if res and res[-1]["i"]==di: res[-1]["end"]=round(b,3)
    else: res.append({"i":di,"text":disp[di],"start":round(a,3),"end":round(b,3)})
for r in res: r.pop("i")
if res[-1]["text"]=="DM":  # final word the en-us model cannot fit; speech ends at the 69.8s pause
    res[-1]["end"]=69.35; res.append({"text":"kalian.","start":69.35,"end":69.8})
json.dump(res, open(OUT,"w"), ensure_ascii=False, indent=0)
print("aligned", len(res), "words", res[-2:])
