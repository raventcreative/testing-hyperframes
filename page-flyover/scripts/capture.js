// Capture landing page: clean page (layers hidden) in chunks + each layer alone (transparent, 28px pad)
const { chromium } = require('playwright');
const fs=require('fs'); const OUT=process.argv[2]; fs.mkdirSync(OUT+'/layers',{recursive:true});
const URL='https://marketing.aipreneur.co.id', PAD=28, CH=4096;
(async()=>{
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:2});
 await p.goto(URL,{waitUntil:'networkidle',timeout:90000});
 // swap blocked YouTube embeds for their thumbnails
 await p.evaluate(()=>{for(const f of document.querySelectorAll('iframe[src*="youtube"]')){const id=(f.src.match(/embed\/([^?&/]+)/)||[])[1];const i=document.createElement('img');i.src='https://i.ytimg.com/vi/'+id+'/maxresdefault.jpg';i.className='yt-thumb';i.style.cssText=f.style.cssText+';object-fit:cover;width:100%;height:100%;position:absolute;inset:0;border-radius:inherit';f.replaceWith(i);}});
 let H=await p.evaluate(()=>document.documentElement.scrollHeight);
 for(let y=0;y<H;y+=300){await p.evaluate(y=>window.scrollTo(0,y),y);await p.waitForTimeout(110);}
 await p.waitForTimeout(1500); await p.evaluate(()=>window.scrollTo(0,0)); await p.waitForTimeout(600);
 await p.addStyleTag({content:`#hdr{position:absolute!important;top:0!important}.fab,.mobile-cta,#promoPop,#lb,.promo-overlay{display:none!important}
  *,*::before,*::after{transition:none!important;caret-color:transparent!important}`});
 // finish one-shot animations (reveal/skew-ins), freeze looping ones (marquees)
 await p.evaluate(()=>{for(const a of document.getAnimations()){const it=a.effect&&a.effect.getComputedTiming().iterations; if(it===Infinity){a.pause();} else {try{a.finish();}catch(e){a.pause();}}}});
 await p.waitForTimeout(500);
 H=await p.evaluate(()=>document.documentElement.scrollHeight);
 // mark layers
 const layers=await p.evaluate(()=>{
  const L=[]; const vis=e=>{const r=e.getBoundingClientRect(); let x0=r.left,x1=r.right,y0=r.top,y1=r.bottom;
    for(let a=e.parentElement;a&&a!==document.body;a=a.parentElement){const cs=getComputedStyle(a);if(cs.overflow!=='visible'||cs.overflowX!=='visible'){const q=a.getBoundingClientRect();x0=Math.max(x0,q.left);x1=Math.min(x1,q.right);y0=Math.max(y0,q.top);y1=Math.min(y1,q.bottom);}}
    x0=Math.max(x0,0);x1=Math.min(x1,1440); return (x1-x0)*(y1-y0)>=0.9*r.width*r.height && r.width>8;};
  const add=(e,kind)=>{if(!e||e.dataset.layer||!vis(e))return; const r=e.getBoundingClientRect(); if(L.some(o=>Math.abs(o.x-r.left)<20&&Math.abs(o.y-(r.top+scrollY))<20)){return;} e.dataset.layer=L.length;
    L.push({id:L.length,kind,x:r.left,y:r.top+scrollY,w:r.width,h:r.height,label:(e.innerText||e.alt||'').slice(0,24).replace(/\n/g,' ')});};
  const all=(s,k)=>document.querySelectorAll(s).forEach(e=>add(e,k));
  add(document.querySelector('.hero-cover'),'mock');
  add([...document.querySelectorAll('.hero a.btn')].find(a=>/Masuk Sekarang/.test(a.innerText)),'btn');
  // tools-section floating icon chips
  const ts=document.querySelector('.tools-sec'); if(ts) [...ts.querySelectorAll('*')].filter(e=>{const r=e.getBoundingClientRect();return r.width>=30&&r.width<=110&&Math.abs(r.width-r.height)<12;})
     .filter((e,i,a)=>!a.some(o=>o!==e&&o.contains(e))).forEach(e=>add(e,'toolchip'));
  all('.stat60-row','stat'); all('.show-card','photo'); all('.vcar-card','card'); all('.lfc .yt-thumb, .lfc img','card');
  all('.persona .card','card'); all('.tcard','tcard'); all('.pain-item','chip'); all('.kur-img','card');
  all('.bonus-card','card');
  [...document.querySelectorAll('section')].filter(s=>/Apa Kata Mereka Tentang/.test(s.innerText)).forEach(s=>s.querySelectorAll('img').forEach(e=>add(e,'testi')));
  [...document.querySelectorAll('img')].filter(i=>/^Freddie Kashawan$/.test(i.alt)).forEach(e=>add(e,'card'));
  all('.soc-card','chip'); all('.cred-card','card'); all('.final a.btn, .final .btn','btn');
  return L;});
 // full page, layers hidden
 await p.addStyleTag({content:'[data-layer]{visibility:hidden!important}'});
 const chunks=[]; for(let y=0;y<H;y+=CH){const h=Math.min(CH,H-y); const f=`page_${chunks.length}.png`;
   await p.screenshot({path:OUT+'/'+f,fullPage:true,clip:{x:0,y,width:1440,height:h}}); chunks.push({file:f,y,h});}
 // each layer alone on transparent
 await p.addStyleTag({content:'html,body{background:transparent!important} body *{visibility:hidden!important} .solo, .solo *{visibility:visible!important}'});
 for(const l of layers){
  await p.evaluate(id=>{document.querySelectorAll('.solo').forEach(e=>e.classList.remove('solo'));document.querySelector(`[data-layer="${id}"]`).classList.add('solo');},String(l.id));
  const clip={x:Math.max(0,l.x-PAD),y:Math.max(0,l.y-PAD)}; clip.width=Math.min(1440,l.x+l.w+PAD)-clip.x; clip.height=Math.min(H,l.y+l.h+PAD)-clip.y;
  l.file=`layers/L${l.id}.png`; l.cx=clip.x; l.cy=clip.y; l.cw=clip.width; l.ch=clip.height;
  await p.screenshot({path:OUT+'/'+l.file,fullPage:true,omitBackground:true,clip});
 }
 const sec=await p.evaluate(()=>[...document.querySelectorAll('section,footer')].map(e=>{const r=e.getBoundingClientRect();const h=e.querySelector('h1,h2,h3');const hr=h&&h.getBoundingClientRect();return {y:r.top+scrollY,h:r.height,title:h?h.innerText.slice(0,40).replace(/\n/g,' '):'',ty:hr?hr.top+scrollY+hr.height/2:null};}).filter(s=>s.h>0));
 fs.writeFileSync(OUT+'/page.json',JSON.stringify({width:1440,height:H,dpr:2,pad:PAD,chunks,layers,sections:sec},null,1));
 console.log('H',H,'layers',layers.length); console.log(layers.map(l=>`${l.id} ${l.kind} ${Math.round(l.x)},${Math.round(l.y)} ${Math.round(l.w)}x${Math.round(l.h)} ${l.label}`).join('\n'));
 await b.close();})();
