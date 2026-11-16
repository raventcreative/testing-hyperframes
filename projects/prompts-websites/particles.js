// Static particle art for mockup canvases (deterministic).
(function(){let s=7;const R=()=>(s=(s*16807)%2147483647)/2147483647;
document.querySelectorAll('canvas.pc').forEach(c=>{const W=c.clientWidth*2,H=c.clientHeight*2;c.width=W;c.height=H;const g=c.getContext('2d');
 if(c.dataset.k==='x'){for(let i=0;i<5200;i++){const t=R(),arm=R()<.5?1:-1,sp=(R()-.5)*0.17;const x=W/2+(t-.5)*H*0.95+sp*H,y=H/2+arm*(t-.5)*H*0.95+(R()-.5)*H*0.17;
   const a=.25+R()*.7;g.fillStyle=`rgba(${215+R()*40|0},${190+R()*40|0},255,${a})`;g.beginPath();g.arc(x,y,R()*2.4+.4,0,7);g.fill();}}
 else{for(let i=0;i<6500;i++){const u=R()*Math.PI*2,v=Math.acos(2*R()-1);let x=Math.sin(v)*Math.cos(u),y=Math.cos(v),z=Math.sin(v)*Math.sin(u);
   const sx=W*0.62+x*H*0.26*(1-0.25*y),sy=H*0.44+y*H*0.36;if(y>0.6&&Math.abs(x)>0.5)continue;const m=(x+1)/2;
   g.fillStyle=`rgba(${80+m*170|0},${120-m*60|0},255,${.35+R()*.5})`;g.beginPath();g.arc(sx,sy,R()*2+.5,0,7);g.fill();}
   for(let i=0;i<2600;i++){const sx=W*0.62+(R()-.5)*H*0.5,sy=H*0.8+R()*H*0.2;g.fillStyle=`rgba(90,140,255,${R()*.5})`;g.fillRect(sx,sy,2,2);}}
});})();
