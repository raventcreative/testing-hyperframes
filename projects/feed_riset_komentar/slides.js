// Riset audiens dari kolom komentar (AIpreneur navy feed carousel). Slide 9 = closing.py (client rule).
window.BRAND='../../brand';
window.TOTAL=9;
const ph=(f,pos='center')=>`<div class="ph"><img src="assets/photos/${f}.jpg" style="object-position:${pos}"></div>`;
const cm=(u,t,meta,st='',hl=false)=>`<div class="cm${hl?' hl':''}" style="${st}"><div class="av"></div><div><small>${u}</small><span>${t}</span><em>${meta}</em></div></div>`;
const lg=(f,st)=>`<img class="lg" src="assets/3d/${f}.png" style="${st}">`;
window.SLIDES=[
 {title:'Riset audiens paling<br>jujur ada di <span class="acc">kolom<br>komentar.</span>',h:66,
  body:'5 langkah narik ratusan komentar, lalu ubah jadi ide konten pakai <span class="acc">Apify + Claude.</span>',
  media: ph('7c64fb38','center 40%')
   + cm('rina.jualan','Kak, ini bisa buat jualan skincare gak?','2 hari · 248 suka','left:28px;top:34px')
   + cm('budi_umkm','Aku masih bingung mulai AI dari mana…','1 hari · 131 suka','left:120px;top:190px',true)
   + cm('dewi.creator','Prompt-nya dong kak 😭','5 jam · 96 suka','left:40px;top:346px')
   + lg('instagram','right:34px;top:26px;width:120px;transform:rotate(8deg)')
   + lg('tiktok','right:150px;bottom:30px;width:100px;transform:rotate(-8deg)')},
 {title:'Banyak tim ngerasa<br><span class="acc">udah riset.</span>',
  body:'Padahal cuma screenshot komentar satu-satu sampai capek. Tenaga habis buat <span class="acc">ngumpulin</span>, bukan buat mikir.',
  media: ph('77477944','center 55%')
   + `<div class="gc" style="right:26px;top:26px;width:300px"><h4>Folder “Riset”</h4><p>IMG_2201.png<br>IMG_2202.png<br>IMG_2203.png<br>… 187 screenshot lagi</p></div>`},
 {title:'Audiens udah nulis isi<br>kepalanya. <span class="acc">Gratis.</span>',
  body:'Pertanyaan, keluhan, sampai kata-kata yang mereka pakai, semua ada di komentar. Masalahnya cuma satu: <span class="acc">kebanyakan buat dibaca manual.</span>',
  media: ph('80e46647','center 30%')
   + cm('andi.coffee','Kalau tim cuma 2 orang, AI-nya kepake gak?','67 suka','right:26px;top:30px')
   + cm('sari.olshop','Capek bales chat satu-satu tiap malam','212 suka','right:60px;top:170px',true)},
 {title:'<span class="acc">01</span> Tarik ratusan<br>komentar pakai Apify.',
  body:'Di Apify Store pilih comment scraper, tempel link post kamu dan kompetitor, klik Start. <span class="acc">Beberapa menit, ratusan komentar.</span>',
  media: ph('9d224b3d','center 60%')
   + `<div class="gc" style="left:26px;top:26px;width:560px"><h4>Instagram Comments Scraper</h4><div class="mono">apify/instagram-comment-scraper</div><span class="btn">Start</span></div>`
   + `<div class="gc" style="left:120px;top:206px;width:560px"><h4>TikTok Comments Scraper</h4><div class="mono">clockworks/tiktok-comments-scraper</div><span class="btn">Start</span></div>`
   + lg('instagram','right:40px;top:30px;width:110px;transform:rotate(8deg)') + lg('tiktok','right:52px;top:200px;width:92px;transform:rotate(-6deg)')},
 {title:'<span class="acc">02</span> Export, lalu<br>bersihin datanya.',
  body:'Download hasilnya jadi CSV. Buang spam, komentar emoji doang, dan yang dobel. Sisain: <span class="acc">teks, jumlah suka, tanggal.</span>',
  media: ph('473a399a','center 45%')
   + `<div class="gc" style="left:26px;right:26px;top:26px"><table><tr><th>komentar</th><th>suka</th><th>tanggal</th></tr>
      <tr><td>capek bales chat satu-satu</td><td>212</td><td>18/11</td></tr>
      <tr><td><s>🔥🔥🔥</s></td><td><s>3</s></td><td><s>18/11</s></td></tr>
      <tr><td>prompt-nya dong kak</td><td>96</td><td>19/11</td></tr>
      <tr><td><s>cek bio aku ya kak!!</s></td><td><s>0</s></td><td><s>19/11</s></td></tr></table></div>`},
 {title:'<span class="acc">03</span> Kasih ke Claude,<br>minta dikelompokkan.',
  body:'Upload CSV-nya, lalu minta Claude bagi jadi 4 kelompok: <span class="acc">pertanyaan, keluhan, keinginan, kalimat yang sering diulang.</span>',
  media: ph('6bfe4660','center 50%')
   + `<div class="gc" style="left:26px;top:26px;width:640px"><h4>Prompt</h4><p>“Ini 300 komentar dari audiens saya. Kelompokkan jadi pertanyaan, keluhan, keinginan, dan kalimat yang sering diulang. Urutkan dari yang paling banyak disukai. Kutip kalimat aslinya.”</p></div>`
   + lg('claude','right:36px;bottom:36px;width:150px;transform:rotate(-8deg)')},
 {title:'<span class="acc">04</span> Bikin kamus<br>bahasa audiens.',
  body:'Catat kata-kata asli mereka. Bukan “optimasi workflow”, tapi <span class="acc">“capek bales chat satu-satu”.</span> Itu bahan hook paling kuat.',
  media: ph('6b5966d5','center 50%')
   + `<div class="gc" style="left:26px;right:26px;bottom:26px"><span class="chip on">capek bales chat</span><span class="chip">bingung mulai dari mana</span><span class="chip">tim cuma 2 orang</span><span class="chip">takut mahal</span><span class="chip">prompt-nya dong</span></div>`},
 {title:'<span class="acc">05</span> Ubah jadi hook<br>dan ide konten.',
  body:'Satu keluhan = satu konten. Mulai dari komentar yang <span class="acc">paling banyak disukai dan dibalas.</span>',
  media: ph('54c7d04d','center 35%')
   + cm('sari.olshop','Capek bales chat satu-satu tiap malam','212 suka','left:26px;top:28px',true)
   + `<div class="arr" style="left:60px;top:150px">↓</div>`
   + `<div class="gc" style="left:26px;right:26px;top:212px"><h4>Hook</h4><p style="font-size:24px;color:#fff">“Masih bales chat pelanggan satu-satu jam 11 malam? Ini cara gue serahin ke AI.”</p></div>`},
];
