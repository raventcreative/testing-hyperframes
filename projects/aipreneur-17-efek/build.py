"""17 efek video AI as 17 animated 1080x1080 slides. Run: python3 build.py"""
import re
import shutil
from pathlib import Path

from fx import EFFECTS

ROOT = Path(__file__).parent

# (name, tagline, dipakai waktu, prompt, problem, fix)
DATA = [
    ("orbit", "Kartu melayang muter ngelilingin kamu.", "Nyebut banyak hal sekaligus: jenis konten, klien, hasil.",
     "Pas aku nyebut [kata], bikin 5 kartu screenshot melayang muter ngelilingin badanku. Orbitnya elips, lebar 128px dan tinggi 46px dari titik tengah dada. Kartu yang lagi di belakang badan lewat di belakang cutout-ku dan ukurannya jadi 0,78. Yang di depan jadi 1,05. Satu putaran 1,3 detik. Kartunya miring ngikutin posisi orbit.",
     "Kartunya nutupin wajah", "turunin tinggi orbit jadi 30px"),
    ("couch wall", "Dinding di belakangmu penuh kartu konten.", "Nunjukin volume kerja atau banyaknya postingan.",
     "Ganti dinding di belakangku jadi grid 4 baris 3 kolom berisi kartu konten, selang-seling antara thumbnail video dan kartu tulisan. Kartunya muncul satu per satu dari tengah, jeda 0,035 detik antar kartu, masing-masing miring acak 3 derajat. Badanku tetap di depan grid. Taruh satu kalimat besar di bawah dada.",
     "Gridnya terlalu ramai", "jadiin 3 baris 2 kolom aja"),
    ("ui world", "Kamu ada di dalam tampilan aplikasi.", "Nunjukin alat yang kamu pakai tanpa harus screen record.",
     "Taruh aku di dalam tampilan aplikasi chat berlatar krem. Di atas kepalaku ada baris 4 thumbnail klip yang jatuh satu per satu dari atas, jeda 0,08 detik. Di bawahnya ada kolom chat berisi instruksiku. Badanku ada di bagian bawah jendela, kayak lagi berdiri di dalam aplikasinya. Tulisan di bawah ganti dari [teks 1] ke [teks 2] di tengah klip.",
     "Jendelanya kekecilan", "besarin jendela sampai memenuhi layar"),
    ("frame break", "Kepala kamu nembus keluar bingkai.", "Kalimat yang isinya nerobos aturan atau keluar dari kebiasaan.",
     "Taruh videoku di dalam bingkai HP di tengah layar, latar belakangnya gelap. Kepala dan tanganku nembus keluar lewat sisi atas bingkai, jadi yang di dalam bingkai cuma dari dada ke bawah. Bagian yang nembus kasih bayangan biar kelihatan keluar beneran. Pas efeknya masuk, badanku naik 40px dalam 0,3 detik.",
     "Potongannya kelihatan garis lurus", "haluskan tepi potongan 2px"),
    ("digital zoom", "Punch-in cepat ke wajah plus satu kata gede.", "Satu kata yang paling pengen kamu tekenin.",
     "Pas aku nyebut [kata kunci], punch-in ke wajahku sampai 1,7 kali dalam 0,1 detik, titik zoom-nya di mata. Pas mentok, kasih getar 3px kiri kanan selama 0,15 detik. Barengan itu munculin kata [kata kunci] gede di bawah wajah, warna aksen, masuk dari skala 1,8 ke 1.",
     "Zoom-nya bikin pusing", "buang getarnya, zoom aja"),
    ("phone mockup", "Layar HP melayang di samping kepala.", "Nunjukin chat, DM, atau notifikasi sebagai bukti.",
     "Munculin layar HP melayang di samping kepalaku, ukuran sepertiga tinggi layar. Isinya percakapan chat: 2 pesan dariku dan 2 balasan. HP-nya masuk dari kanan sambil muter dari 12 derajat ke -8 derajat dalam 0,32 detik, terus naik turun pelan 5px biar kelihatan melayang. Jangan nutupin wajahku.",
     "HP-nya terlalu dekat ke muka", "geser 100px ke kanan"),
    ("checklist", "Kartu daftar yang dicentang satu per satu.", "Nyebut langkah atau syarat yang jumlahnya pasti.",
     "Taruh kartu checklist di atas kepalaku, latar gelap transparan. Isinya 3 langkah: [langkah 1], [langkah 2], [langkah 3]. Centangnya muncul satu per satu tiap 0,2 detik dengan pop kecil. Di pojok kanan atas kartu ada penghitung yang ikut berubah dari &ldquo;0 of 3&rdquo; sampai &ldquo;3 of 3&rdquo;.",
     "Centangnya mendahului ucapan", "pas centangnya ke kata [x], [y], [z]"),
    ("headline wall", "Kertas dan sticky note nempel di dinding.", "Ngomongin opini orang, berita, atau komentar.",
     "Tempel 7 kertas di dinding belakangku, campuran potongan artikel dan sticky note warna aksen. Posisinya acak di kiri, kanan, dan atas kepala, masing-masing miring 3 sampai 7 derajat. Kertasnya muncul satu per satu dari skala 1,4 ke 1, jeda 0,06 detik. Semua kertas ada di belakang badanku.",
     "Kertasnya nempel di badan", "semua kertas di belakang cutout"),
    ("zoom cut", "Zoom nembus satu kata, terus pindah shot.", "Pindah topik atau pindah babak.",
     "Pas pindah dari kalimat ini ke kalimat berikutnya, taruh satu kata gede di tengah layar, terus zoom nembus kata itu sampai 16 kali dalam 0,25 detik. Pas paling mentok kasih kilat putih 0,06 detik, terus potong ke shot berikutnya yang masuk dari skala 1,25 turun ke 1 dalam 0,3 detik.",
     "Transisinya kelamaan", "percepat jadi 0,18 detik"),
    ("chart grow", "Grafik naik kegambar di belakangmu.", "Nyebut pertumbuhan atau perubahan dari waktu ke waktu.",
     "Gambar grafik garis naik di belakangku, 7 titik mingguan dengan label hari di atasnya. Garisnya kegambar dari kiri ke kanan dalam 0,55 detik, warna aksen, tebal 5px, ujungnya bulat. Pas garisnya sampai ujung, munculin titik bulat dan label kecil di sebelahnya. Grafiknya ada di belakang badanku.",
     "Grafiknya ketutup kepala", "naikin grafik 120px"),
    ("pull-back reveal", "Kamera mundur, ternyata kamu di dalam aplikasi.", "Reveal di akhir kalimat, atau buka sesuatu yang belum kelihatan.",
     "Mulai dari close-up wajahku, terus kamera mundur pelan dalam 0,55 detik sampai kelihatan ternyata videoku ada di dalam jendela aplikasi. Di kiri jendela ada panel progres berisi 4 langkah yang udah dicentang dan satu bar 62 persen. Mundurnya dari skala 2,05 ke 1, pakai easing yang pelan di awal dan di akhir.",
     "Mundurnya kecepetan", "pelanin jadi 0,9 detik"),
    ("green screen", "Latar belakangmu diganti tampilan aplikasi.", "Ngomongin alat atau proses, tapi tetap mau wajahmu yang utama.",
     "Hapus latar belakangku, ganti jadi tampilan aplikasi: timer gede di kiri atas, daftar 3 tugas di tengah, satu kalimat di bawahnya. Badanku ditaruh di depan tampilan itu, agak ke bawah biar kepalaku ga nabrak timer. Jangan ubah warna kulit dan bajuku.",
     "Ada garis sisa latar di rambut", "bersihin tepi cutout, buang halo-nya"),
    ("paper cut", "Kamu jadi potongan kertas di kolase.", "Kalimat yang nyinggung sesuatu yang kasar atau jujur.",
     "Bikin aku jadi potongan kertas: kasih pinggiran putih tebal 14px di sekeliling cutout badanku, plus bayangan tipis. Latarnya kertas krem. Tambahin coretan pulpen, satu blok warna aksen di belakang, dan 4 kotak angka gaya surat kaleng di atas, tiap kotak beda warna dan beda huruf. Potongan kertasnya goyang 1 derajat tiap 0,1 detik biar kelihatan stop motion.",
     "Goyangnya bikin mual", "goyangnya tiap 0,2 detik aja"),
    ("doodle boil", "Garis gambar tangan bergetar ngikutin siluetmu.", "Kalimat ringan, bercanda, atau bagian yang santai.",
     "Gambar garis putih tangan di sekeliling siluetku, tebal 7px, dengan lekukan ga rapi kayak gambar tangan. Bikin 3 versi garis yang beda sedikit, terus puter 3 versi itu tiap 0,1 detik biar kelihatan bergetar. Tambahin 2 ikon doodle di kiri atas dan kanan atas yang ikut bergetar. Latar belakangnya gelapin sedikit.",
     "Garisnya terlalu jauh dari badan", "rapetin garisnya ke siluet"),
    ("vertigo", "Latar membesar, badanmu tetap.", "Kalimat yang isinya kaget, ga nyangka, atau tekanan.",
     "Bikin efek dolly zoom: badanku ukurannya tetap, tapi latar belakangnya membesar dari skala 1 ke 1,55 dalam 0,85 detik. Caranya pisahin cutout badanku dari latar, isi bagian latar yang ketutup badan pakai inpaint, baru zoom latarnya doang.",
     "Ada bayangan aneh di sekitar badan", "perlebar area inpaint-nya"),
    ("cover story", "Judul serif gede di belakang kepala.", "Buka video, atau nyebut satu kata yang jadi tema.",
     "Taruh judul serif gede di belakang kepalaku kayak sampul majalah, tulisannya [kata]. Hurufnya masuk dari jarak antar huruf 30px mengecil ke 3px dalam 0,45 detik. Tambahin label kecil di kiri atas dan kanan atas, sama satu kalimat miring di bawah kiri. Judulnya di belakang badanku, jadi kepalaku nutupin sebagian hurufnya.",
     "Judulnya ketutup kepala semua", "naikin judul 60px"),
    ("glass type", "Tulisan kaca 3D di belakang kepala.", "Tutup video, atau nyebut nama produk dan konsep.",
     "Taruh tulisan [kata] gede di belakang kepalaku dengan tampilan kaca: isinya gradasi putih transparan, pinggirannya garis putih tipis, plus bayangan halus. Tulisannya miring 3D, muter pelan dari -24 derajat ke -2 derajat selama efeknya jalan. Tulisannya di belakang badanku.",
     "Tulisannya ga kebaca di latar terang", "tambahin bayangan di belakang huruf"),
]

SHELL = """<!doctype html>
<html lang="id">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1080" />
<title>AIpreneur — %%NAME%%</title>
<script src="vendor/gsap/dist/gsap.min.js"></script>
<link rel="stylesheet" href="assets/shared.css" />
<style>
%%CSS%%
</style>
</head>
<body>
<div id="root" data-composition-id="%%CID%%" data-start="0" data-duration="6" data-width="1080" data-height="1080" data-fps="30">
  <div id="stage" class="clip" data-start="0" data-duration="6" data-track-index="0" data-track-kind="graphics" style="position:absolute;inset:0">
    <div class="bg"></div>
    <div class="logo"></div>
    <div class="eyebrow">17 EFEK VIDEO AI</div>
    <div class="ph" id="ph"><div class="wall"></div><div class="floor"></div><div class="rec"><i></i>DEMO</div>
%%VIS%%
    </div>
    <div class="col">
      <div class="no">EFEK %%NO%% / 17</div>
      <div class="ttl"><span class="hb">%%TITLE%%</span></div>
      <div class="tag w">%%TAG%%</div>
      <div class="use"><div class="lb">DIPAKAI WAKTU</div><div class="tx">%%USE%%</div></div>
      <div class="pr"><div class="lb">PROMPT</div><div class="tx w r">%%PROMPT%%</div></div>
      <div class="fix"><span class="c b">Kalau meleset:</span> %%PROB%%? Bilang<br><span class="hb">&ldquo;%%FIX%%&rdquo;</span></div>
    </div>
    <div class="foot"><div class="who"><div class="av">FK</div><span>Freddie Kashawan</span></div>
      <div class="pg"><span class="c">%%NO%% / 17</span>%%RIGHT%%</div></div>
  </div>
</div>
<script>
(function () {
  const D = 6, TAU = Math.PI * 2;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const smooth = (p) => { p = clamp(p, 0, 1); return p * p * (3 - 2 * p); };
  const env = (t, a, b, f) => { f = f || 0.18; return smooth((t - a) / f) * (1 - smooth((t - b) / f)); };
  const backOut = (p, s) => { p = clamp(p, 0, 1); s = s === undefined ? 1.7 : s; const q = p - 1; return q * q * ((s + 1) * q + s) + 1; };
  const io3 = (p) => { p = clamp(p, 0, 1); return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; };
  const mix = (a, b, k) => a + (b - a) * k;
  const $ = (id) => document.getElementById(id);
  const tl = gsap.timeline({ paused: true });
  const st = { t: 0 };
%%JS%%
  tl.to(st, { t: D, duration: D, ease: "none", onUpdate: () => render(st.t) }, 0);
  render(0);
  window.__timelines = window.__timelines || {};
  window.__timelines["%%CID%%"] = tl;
})();
</script>
</body>
</html>
"""


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


if __name__ == "__main__":
    for i, ((name, tag, use, prompt, prob, fix), (css, vis, js)) in enumerate(zip(DATA, EFFECTS)):
        no = f"{i + 1:02d}"
        prompt_h = re.sub(r"\[([^\]]+)\]", r'<span class="ph2">[\1]</span>', prompt)
        fix_h = re.sub(r"\[([^\]]+)\]", r"[\1]", fix)
        rep = {"NAME": name, "CID": f"e{no}", "CSS": css, "VIS": vis, "NO": no, "TITLE": name, "TAG": tag, "USE": use,
               "PROMPT": prompt_h, "PROB": prob, "FIX": fix_h, "JS": js, "RIGHT": "GESER &rarr;" if i < 16 else "SAVE &middot; SHARE"}
        html = SHELL
        for k, v in rep.items():
            html = html.replace("%%" + k + "%%", v)
        d = ROOT / "slides" / f"e{no}"
        d.mkdir(parents=True, exist_ok=True)
        for sub in ("assets", "vendor"):
            if (d / sub).exists():
                shutil.rmtree(d / sub)
            shutil.copytree(ROOT / sub, d / sub)
        (d / "index.html").write_text(html)
        (d / "slug.txt").write_text(f"efek-{no}-{slug(name)}")
    print("built", len(DATA))
