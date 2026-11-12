"""MasterPajak AI series: put the ElevenLabs VO on a finished composition without breaking its design.
For each VO line, the speech starts at the line's planned beat (TM key or seconds); if the previous line is still talking,
that line - and everything after it - moves later (never earlier), so no designed interval ever shrinks between lines.
TM keys tied to a word (anchors) follow that word exactly; other keys are warped linearly between neighbours.
Writes: production/vo/{lines.txt, VO_MPxx.mp3/.json, vo_timed.wav, TM_original.json}, assets/audio/vo.wav, lipsync.js,
and the re-timed window.TM + data-duration in index.html. Then run tools/sfx.py in the project.
Usage: python3 tools/mp_vo.py <video number>"""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "projects"
TAGS = "[playful] [excited]"
GAP = 0.22          # minimum silence between two VO lines
# per video: folder, the planned start of every VO line (TM key or seconds), word anchors (key, line index, phrase)
V = {
 1: ("mp10_01_berita", [0.3, 4.9, "e2", "e3", "e4", "conf", "sol", "help", "end"], []),
 2: ("mp10_02_jejak", ["l1", "l2", "l3", "l4", "l5", "l6", "l7"],
     [("q1", 0, "uangnya lari"), ("fee", 1, "Kepotong"), ("ong", 1, "ongkir"), ("ret", 1, "kadang retur"), ("bank", 2, "Baru nyampe"),
      ("l4b", 3, "jalannya sepanjang"), ("ribu", 3, "gimana yang ribuan"), ("l5b", 4, "jadi pembukuan"), ("l5c", 4, "dari pesanan"),
      ("l6b", 5, "dan mana yang"), ("cta", 6, "Coba kalkulator"), ("bio", 6, "Link di bio")]),
 3: ("mp10_03_nota", ["hook", "brand", "read", "row", "ledger", "end"],
     [("numpuk", 0, "numpuk"), ("lupa", 0, "Difoto doang"), ("up", 1, "foto nota"), ("snap", 1, "diunggah"), ("susun", 2, "terus disusun"),
      ("tgl", 2, "tanggal"), ("kat", 2, "kategori"), ("nom", 2, "nominal"), ("ketik", 3, "Nggak perlu ketik"), ("lap", 4, "siap dipakai"),
      ("cta", 5, "Coba kalkulator"), ("bio", 5, "Link di bio")]),
 4: ("mp10_04_tanda", ["hook", "s1", "s2", "s3", "kal", "sol", "end"], [("h3", 0, "Nomor tiga"), ("s3u", 3, "tapi untungnya")]),
 5: ("mp10_05_omzet", ["hook", "c1", "laba", "seller", "sol", "end"],
     [("ask", 0, "Tapi untungnya"), ("c2", 1, "Kurangi ongkir"), ("c3", 1, "Kurangi iklan"), ("labaW", 2, "beneran laba"),
      ("dec", 3, "padahal keputusan"), ("cta", 5, "Coba kalkulator"), ("bio", 5, "Link di bio")]),
 6: ("mp10_06_rekon", ["hook", "sum", "why", "hunt", "sol", "know", "end"],
     [("ne", 0, "kok beda"), ("add", 1, "dijumlah"), ("tot", 1, "hasilnya nggak sama"), ("dup", 2, "dua kali"), ("miss", 2, "kelewat"),
      ("day", 3, "Bisa seharian"), ("cek", 4, "cocokkan"), ("flag", 4, "tandai baris"), ("cta", 6, "Coba kalkulator"), ("bio", 6, "Link di bio")]),
 7: ("mp10_07_kalkulator", ["hook", "s1", "s2", "s3", "res", "end"],
     [("brand", 0, "Coba kalkulator gratis"), ("kon", 4, "sebelum ngobrol"), ("bio", 5, "Link ada di bio")]),
 8: ("mp10_08_asisten", ["q", "ai", "ex", "sol", "end"],
     [("q2", 0, "kapan perlu"), ("ask", 1, "angka laba"), ("ans", 1, "asisten AI bantu"), ("dat", 1, "dari data"), ("tim", 2, "ada tim ahli"),
      ("sl", 2, "sesuai layanan"), ("cta", 4, "Coba kalkulator"), ("bio", 4, "Link di bio")]),
 9: ("mp10_09_tutupbulan", ["pov", "w1", "nota", "capek", "sol", "end"],
     [("notif", 0, "Notifikasi"), ("w2", 1, "Pencairan"), ("w3", 1, "Mutasi bank"), ("sih", 3, "capek nggak"), ("satu", 4, "catatan jualan"),
      ("tenang", 4, "jadi tutup bulan"), ("cta", 5, "Coba kalkulator"), ("bio", 5, "Link di bio")]),
 10: ("mp10_10_sebelumsesudah", ["l1", "l2", "l3", "l4", "l5"],
     [("rk", 0, "rekap manual"), ("tf", 0, "tiga file"), ("nc", 0, "angka nggak"), ("cj", 1, "catatan jualan"), ("pb", 1, "pembukuan"),
      ("lp", 1, "dan laporan"), ("sa", 1, "dalam satu alur"), ("l3b", 2, "Sesudah"), ("jl", 2, "yang jelas"), ("l4b", 3, "Sesudah"),
      ("ta", 3, "plus tim ahli"), ("cta", 4, "Coba kalkulator"), ("bio", 4, "Link di bio")]),
 11: ("mp10_11_mitos", ["hook", "m1", "m2", "m3", "sol", "end"],
     [("f1", 1, "Faktanya"), ("f2", 2, "Faktanya"), ("f3", 3, "Faktanya"), ("cta", 5, "Coba kalkulator"), ("bio", 5, "Link di bio")]),
 12: ("mp10_12_pisah", ["masuk", "cek", "campur", "pisah", "sol", "end"],
     [("eh", 0, "eh, kepake"), ("cicil", 0, "bayar cicilan"), ("kirim", 0, "kirim ke keluarga"), ("mana", 1, "untungnya ke mana"),
      ("kebaca", 2, "angka usahamu"), ("lane1", 3, "mana pemasukan"), ("lane2", 3, "mana pengeluaran"), ("telusur", 4, "jadi pembukuan"),
      ("cta", 5, "Coba kalkulator"), ("bio", 5, "Link di bio")]),
 13: ("mp10_13_cerita", ["rina", "tipis", "ternyata", "rapi", "sol", "end"],
     [("laris", 0, "Jualannya laris"), ("sal", 1, "saldonya kok"), ("ongkir", 2, "ongkir"), ("kemasan", 2, "kemasan"), ("iklan", 2, "iklan"),
      ("potongan", 2, "potongan platform"), ("pergi", 3, "baru kelihatan"), ("lap", 4, "catatan jualan"), ("baca", 4, "jadi laporan"),
      ("cta", 5, "Coba kalkulator"), ("bio", 5, "Link di bio")]),
 14: ("mp10_14_data", ["hook", "d1", "d2", "d3", "d4", "kum", "end"],
     [("siap", 0, "Siapin empat"), ("d2b", 2, "termasuk ongkir"), ("sol", 5, "MasterPajak AI bantu"), ("est", 5, "terus bantu hitung"),
      ("cta", 6, "Coba kalkulator"), ("bio", 6, "Link di bio")]),
 15: ("mp10_15_tanya", ["hook", "q1", "q2", "q3", "end"],
     [("a1", 1, "Perlu, biar"), ("a2", 2, "Nggak harus"), ("sol", 2, "MasterPajak AI bantu"), ("lap", 2, "jadi laporan"), ("a3", 3, "Ada asisten"),
      ("tim", 3, "dan tim ahli"), ("cta", 4, "Coba kalkulator"), ("bio", 4, "Link di bio")]),
}

def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode: raise SystemExit("FAILED: " + " ".join(map(str, cmd)) + "\n" + r.stdout[-800:] + r.stderr[-800:])
    return r.stdout

def main(n):
    folder, line_keys, anchors = V[n]
    D = P / folder; vo = D / "production" / "vo"; vo.mkdir(parents=True, exist_ok=True)
    # 1 · script lines
    s = (P / "mp10_series" / "VO_SCRIPTS.md").read_text()
    m = re.search(r"^## %d · .*?\n(.*?)(?:\n\n|\Z)" % n, s, re.S | re.M)
    lines = [l for l in m.group(1).splitlines() if l.strip()]
    assert len(lines) == len(line_keys), (n, len(lines), len(line_keys))
    (vo / "lines.txt").write_text("\n".join(lines) + "\n")
    # 2 · TTS with timestamps (once)
    mp3 = vo / ("VO_MP%02d.mp3" % n); js = mp3.with_suffix(".json")
    if not mp3.exists() or "align" not in json.loads(js.read_text() if js.exists() else "{}"):
        print(run(["python3", str(ROOT / "tools" / "el_tts_ts.py"), str(vo / "lines.txt"), str(mp3), "--tags", TAGS]).strip().splitlines()[0])
    J = json.loads(js.read_text()); L = J["lines"]; A = J["align"]
    # 3 · original TM (kept once, so re-runs start from the design, not from a previous re-time)
    html = (D / "index.html").read_text()
    tm_src = re.search(r"window\.TM = (\{[^}]*\})", html).group(1)
    orig = vo / "TM_original.json"
    if not orig.exists(): orig.write_text(json.dumps({k: float(v) for k, v in re.findall(r"(\w+):\s*([\d.]+)", tm_src)}))
    TM = json.loads(orig.read_text())
    K = [TM[k] if isinstance(k, str) else float(k) for k in line_keys]
    # 4 · place each line: speech start T_i >= K_i + delta (delta never shrinks) and >= previous speech end + GAP
    T, delta, prev_end = [], 0.0, -1e9
    for i, l in enumerate(L):
        t = max(K[i] + delta, prev_end + GAP); delta = t - K[i]; T.append(t)
        prev_end = t + (l["end"] - l["start"])
    # 5 · anchors: line starts + word anchors (time of the phrase inside its line, moved with the line)
    pts = [(0.0, 0.0)]
    for i, k in enumerate(line_keys):
        pts.append((K[i], T[i]))
    chars = A["chars"]
    for key, li, phrase in anchors:
        l = L[li]; i0 = chars.find(l["text"][:20]); i0 = i0 if i0 >= 0 else 0
        j = chars.find(phrase, i0)
        if j < 0: print("  ! phrase not found:", key, phrase); continue
        pts.append((TM[key], T[li] + (A["start"][j] - l["start"])))
    pts.sort()
    # keep the warp monotonic (a word anchor may not jump over a later beat)
    mono = [pts[0]]
    for a, b in pts[1:]:
        if a <= mono[-1][0] + 1e-6: continue
        mono.append((a, max(b, mono[-1][1] + 0.05)))
    shift_end = mono[-1][1] - mono[-1][0]
    def warp(t):
        for (a0, b0), (a1, b1) in zip(mono, mono[1:]):
            if a0 <= t <= a1: return b0 + (t - a0) * (b1 - b0) / (a1 - a0)
        return t + shift_end
    newTM = {k: round(warp(v), 3) for k, v in TM.items() if k != "total"}
    speech_end = T[-1] + (L[-1]["end"] - L[-1]["start"])
    newTM["total"] = round(max(warp(TM["total"]), speech_end + 1.2), 2)
    # 6 · write TM + duration
    tm_txt = "{ " + ", ".join(f"{k}: {v}" for k, v in newTM.items()) + " }"
    html = html.replace(tm_src, tm_txt, 1)
    html = re.sub(r'data-duration="[\d.]+"', 'data-duration="%s"' % newTM["total"], html, count=1)
    (D / "index.html").write_text(html)
    # 7 · timed VO track: cut the TTS take at the middle of each pause, drop every line at its new time
    cuts = [0.0] + [(L[i - 1]["end"] + L[i]["start"]) / 2 for i in range(1, len(L))] + [J["duration"] + 0.6]
    fl, ins = [], []
    for i in range(len(L)):
        at = T[i] - (L[i]["start"] - cuts[i])
        fl.append(f"[0:a]atrim=start={cuts[i]:.3f}:end={cuts[i+1]:.3f},asetpts=PTS-STARTPTS,adelay={max(0, at)*1000:.0f}:all=1[a{i}]"); ins.append(f"[a{i}]")
    fl.append("".join(ins) + f"amix=inputs={len(L)}:normalize=0:dropout_transition=0,apad=whole_dur={newTM['total']},atrim=end={newTM['total']}[o]")
    wav = vo / "vo_timed.wav"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(mp3), "-filter_complex", ";".join(fl), "-map", "[o]", "-ac", "1", "-ar", "44100", "-c:a", "pcm_s16le", str(wav)])
    (D / "assets" / "audio").mkdir(parents=True, exist_ok=True)
    run(["cp", str(wav), str(D / "assets" / "audio" / "vo.wav")])
    run(["python3", str(D / "tools" / "lipsync.py"), str(D / "assets" / "audio" / "vo.wav"), str(D / "lipsync.js")])
    # 8 · SFX from the new TM
    try: run(["python3", "tools/sfx.py"], cwd=D)
    except SystemExit: run(["python3", "tools/sfx.py", "."], cwd=D)
    print(f"MP{n:02d} {folder}: VO {J['duration']:.2f}s -> film {TM['total']} -> {newTM['total']} s (end shift +{shift_end:.2f})")
    for i, l in enumerate(L): print(f"   line {i+1}: planned {K[i]:6.2f}  speech {T[i]:6.2f}  ({l['text'][:48]})")

if __name__ == "__main__":
    for a in sys.argv[1:]: main(int(a))
