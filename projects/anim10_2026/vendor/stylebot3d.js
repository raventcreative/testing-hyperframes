(()=>{var gc="170";var Xh=0,Cl=1,qh=2;var Yu=1,vc=2,Gn=3,en=0,Vt=1,Lt=2,li=0,Qi=1,is=2,Il=3,Pl=4,Yh=5,Ii=100,$h=101,Zh=102,Kh=103,Jh=104,jh=200,Qh=201,ef=202,tf=203,sa=204,ra=205,nf=206,sf=207,rf=208,of=209,af=210,cf=211,lf=212,uf=213,hf=214,oa=0,aa=1,ca=2,ss=3,la=4,ua=5,ha=6,fa=7,$u=0,ff=1,df=2,Ln=0,pf=1,mf=2,gf=3,vf=4,xf=5,_f=6,yf=7,Ll="attached",Mf="detached",Zu=300,rs=301,os=302,da=303,pa=304,po=306,qn=1e3,En=1001,Ys=1002,yt=1003,xc=1004;var Ji=1005;var wt=1006,Gs=1007;var Pn=1008;var Dt=1009,Ku=1010,Ju=1011,$s=1012,_c=1013,Yn=1014,Tn=1015,$e=1016,yc=1017,Mc=1018,as=1020,ju=35902,Qu=1021,eh=1022,Ht=1023,th=1024,nh=1025,es=1026,cs=1027,bc=1028,Sc=1029,ih=1030,wc=1031;var Ec=1033,Hr=33776,Vr=33777,Gr=33778,Wr=33779,ma=35840,ga=35841,va=35842,xa=35843,_a=36196,ya=37492,Ma=37496,ba=37808,Sa=37809,wa=37810,Ea=37811,Ta=37812,Aa=37813,Ra=37814,Ca=37815,Ia=37816,Pa=37817,La=37818,Da=37819,Ua=37820,Na=37821,Xr=36492,Fa=36494,Oa=36495,sh=36283,Ba=36284,za=36285,ka=36286;var ls=2300,us=2301,To=2302,Dl=2400,Ul=2401,Nl=2402,bf=2500;var rh=0,mo=1,rr=2,Sf=3200,wf=3201;var oh=0,Ef=1,fn="",St="srgb",Wt="srgb-linear",go="linear",lt="srgb";var Fi=7680;var Fl=519,Tf=512,Af=513,Rf=514,ah=515,Cf=516,If=517,Pf=518,Lf=519,Ha=35044;var Ol="300 es",Wn=2e3,qr=2001,ui=class{addEventListener(e,t){this._listeners===void 0&&(this._listeners={});let n=this._listeners;n[e]===void 0&&(n[e]=[]),n[e].indexOf(t)===-1&&n[e].push(t)}hasEventListener(e,t){if(this._listeners===void 0)return!1;let n=this._listeners;return n[e]!==void 0&&n[e].indexOf(t)!==-1}removeEventListener(e,t){if(this._listeners===void 0)return;let i=this._listeners[e];if(i!==void 0){let r=i.indexOf(t);r!==-1&&i.splice(r,1)}}dispatchEvent(e){if(this._listeners===void 0)return;let n=this._listeners[e.type];if(n!==void 0){e.target=this;let i=n.slice(0);for(let r=0,o=i.length;r<o;r++)i[r].call(this,e);e.target=null}}},Bt=["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","40","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"],Bl=1234567,Ws=Math.PI/180,hs=180/Math.PI;function An(){let s=Math.random()*4294967295|0,e=Math.random()*4294967295|0,t=Math.random()*4294967295|0,n=Math.random()*4294967295|0;return(Bt[s&255]+Bt[s>>8&255]+Bt[s>>16&255]+Bt[s>>24&255]+"-"+Bt[e&255]+Bt[e>>8&255]+"-"+Bt[e>>16&15|64]+Bt[e>>24&255]+"-"+Bt[t&63|128]+Bt[t>>8&255]+"-"+Bt[t>>16&255]+Bt[t>>24&255]+Bt[n&255]+Bt[n>>8&255]+Bt[n>>16&255]+Bt[n>>24&255]).toLowerCase()}function kt(s,e,t){return Math.max(e,Math.min(t,s))}function Tc(s,e){return(s%e+e)%e}function Df(s,e,t,n,i){return n+(s-e)*(i-n)/(t-e)}function Uf(s,e,t){return s!==e?(t-s)/(e-s):0}function Xs(s,e,t){return(1-t)*s+t*e}function Nf(s,e,t,n){return Xs(s,e,1-Math.exp(-t*n))}function Ff(s,e=1){return e-Math.abs(Tc(s,e*2)-e)}function Of(s,e,t){return s<=e?0:s>=t?1:(s=(s-e)/(t-e),s*s*(3-2*s))}function Bf(s,e,t){return s<=e?0:s>=t?1:(s=(s-e)/(t-e),s*s*s*(s*(s*6-15)+10))}function zf(s,e){return s+Math.floor(Math.random()*(e-s+1))}function kf(s,e){return s+Math.random()*(e-s)}function Hf(s){return s*(.5-Math.random())}function Vf(s){s!==void 0&&(Bl=s);let e=Bl+=1831565813;return e=Math.imul(e^e>>>15,e|1),e^=e+Math.imul(e^e>>>7,e|61),((e^e>>>14)>>>0)/4294967296}function Gf(s){return s*Ws}function Wf(s){return s*hs}function Xf(s){return(s&s-1)===0&&s!==0}function qf(s){return Math.pow(2,Math.ceil(Math.log(s)/Math.LN2))}function Yf(s){return Math.pow(2,Math.floor(Math.log(s)/Math.LN2))}function $f(s,e,t,n,i){let r=Math.cos,o=Math.sin,a=r(t/2),c=o(t/2),l=r((e+n)/2),u=o((e+n)/2),h=r((e-n)/2),f=o((e-n)/2),p=r((n-e)/2),g=o((n-e)/2);switch(i){case"XYX":s.set(a*u,c*h,c*f,a*l);break;case"YZY":s.set(c*f,a*u,c*h,a*l);break;case"ZXZ":s.set(c*h,c*f,a*u,a*l);break;case"XZX":s.set(a*u,c*g,c*p,a*l);break;case"YXY":s.set(c*p,a*u,c*g,a*l);break;case"ZYZ":s.set(c*g,c*p,a*u,a*l);break;default:console.warn("THREE.MathUtils: .setQuaternionFromProperEuler() encountered an unknown order: "+i)}}function wn(s,e){switch(e.constructor){case Float32Array:return s;case Uint32Array:return s/4294967295;case Uint16Array:return s/65535;case Uint8Array:return s/255;case Int32Array:return Math.max(s/2147483647,-1);case Int16Array:return Math.max(s/32767,-1);case Int8Array:return Math.max(s/127,-1);default:throw new Error("Invalid component type.")}}function ct(s,e){switch(e.constructor){case Float32Array:return s;case Uint32Array:return Math.round(s*4294967295);case Uint16Array:return Math.round(s*65535);case Uint8Array:return Math.round(s*255);case Int32Array:return Math.round(s*2147483647);case Int16Array:return Math.round(s*32767);case Int8Array:return Math.round(s*127);default:throw new Error("Invalid component type.")}}var vi={DEG2RAD:Ws,RAD2DEG:hs,generateUUID:An,clamp:kt,euclideanModulo:Tc,mapLinear:Df,inverseLerp:Uf,lerp:Xs,damp:Nf,pingpong:Ff,smoothstep:Of,smootherstep:Bf,randInt:zf,randFloat:kf,randFloatSpread:Hf,seededRandom:Vf,degToRad:Gf,radToDeg:Wf,isPowerOfTwo:Xf,ceilPowerOfTwo:qf,floorPowerOfTwo:Yf,setQuaternionFromProperEuler:$f,normalize:ct,denormalize:wn},le=class s{constructor(e=0,t=0){s.prototype.isVector2=!0,this.x=e,this.y=t}get width(){return this.x}set width(e){this.x=e}get height(){return this.y}set height(e){this.y=e}set(e,t){return this.x=e,this.y=t,this}setScalar(e){return this.x=e,this.y=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setComponent(e,t){switch(e){case 0:this.x=t;break;case 1:this.y=t;break;default:throw new Error("index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;default:throw new Error("index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y)}copy(e){return this.x=e.x,this.y=e.y,this}add(e){return this.x+=e.x,this.y+=e.y,this}addScalar(e){return this.x+=e,this.y+=e,this}addVectors(e,t){return this.x=e.x+t.x,this.y=e.y+t.y,this}addScaledVector(e,t){return this.x+=e.x*t,this.y+=e.y*t,this}sub(e){return this.x-=e.x,this.y-=e.y,this}subScalar(e){return this.x-=e,this.y-=e,this}subVectors(e,t){return this.x=e.x-t.x,this.y=e.y-t.y,this}multiply(e){return this.x*=e.x,this.y*=e.y,this}multiplyScalar(e){return this.x*=e,this.y*=e,this}divide(e){return this.x/=e.x,this.y/=e.y,this}divideScalar(e){return this.multiplyScalar(1/e)}applyMatrix3(e){let t=this.x,n=this.y,i=e.elements;return this.x=i[0]*t+i[3]*n+i[6],this.y=i[1]*t+i[4]*n+i[7],this}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this}clamp(e,t){return this.x=Math.max(e.x,Math.min(t.x,this.x)),this.y=Math.max(e.y,Math.min(t.y,this.y)),this}clampScalar(e,t){return this.x=Math.max(e,Math.min(t,this.x)),this.y=Math.max(e,Math.min(t,this.y)),this}clampLength(e,t){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(e,Math.min(t,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this}negate(){return this.x=-this.x,this.y=-this.y,this}dot(e){return this.x*e.x+this.y*e.y}cross(e){return this.x*e.y-this.y*e.x}lengthSq(){return this.x*this.x+this.y*this.y}length(){return Math.sqrt(this.x*this.x+this.y*this.y)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)}normalize(){return this.divideScalar(this.length()||1)}angle(){return Math.atan2(-this.y,-this.x)+Math.PI}angleTo(e){let t=Math.sqrt(this.lengthSq()*e.lengthSq());if(t===0)return Math.PI/2;let n=this.dot(e)/t;return Math.acos(kt(n,-1,1))}distanceTo(e){return Math.sqrt(this.distanceToSquared(e))}distanceToSquared(e){let t=this.x-e.x,n=this.y-e.y;return t*t+n*n}manhattanDistanceTo(e){return Math.abs(this.x-e.x)+Math.abs(this.y-e.y)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,t){return this.x+=(e.x-this.x)*t,this.y+=(e.y-this.y)*t,this}lerpVectors(e,t,n){return this.x=e.x+(t.x-e.x)*n,this.y=e.y+(t.y-e.y)*n,this}equals(e){return e.x===this.x&&e.y===this.y}fromArray(e,t=0){return this.x=e[t],this.y=e[t+1],this}toArray(e=[],t=0){return e[t]=this.x,e[t+1]=this.y,e}fromBufferAttribute(e,t){return this.x=e.getX(t),this.y=e.getY(t),this}rotateAround(e,t){let n=Math.cos(t),i=Math.sin(t),r=this.x-e.x,o=this.y-e.y;return this.x=r*n-o*i+e.x,this.y=r*i+o*n+e.y,this}random(){return this.x=Math.random(),this.y=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y}},ke=class s{constructor(e,t,n,i,r,o,a,c,l){s.prototype.isMatrix3=!0,this.elements=[1,0,0,0,1,0,0,0,1],e!==void 0&&this.set(e,t,n,i,r,o,a,c,l)}set(e,t,n,i,r,o,a,c,l){let u=this.elements;return u[0]=e,u[1]=i,u[2]=a,u[3]=t,u[4]=r,u[5]=c,u[6]=n,u[7]=o,u[8]=l,this}identity(){return this.set(1,0,0,0,1,0,0,0,1),this}copy(e){let t=this.elements,n=e.elements;return t[0]=n[0],t[1]=n[1],t[2]=n[2],t[3]=n[3],t[4]=n[4],t[5]=n[5],t[6]=n[6],t[7]=n[7],t[8]=n[8],this}extractBasis(e,t,n){return e.setFromMatrix3Column(this,0),t.setFromMatrix3Column(this,1),n.setFromMatrix3Column(this,2),this}setFromMatrix4(e){let t=e.elements;return this.set(t[0],t[4],t[8],t[1],t[5],t[9],t[2],t[6],t[10]),this}multiply(e){return this.multiplyMatrices(this,e)}premultiply(e){return this.multiplyMatrices(e,this)}multiplyMatrices(e,t){let n=e.elements,i=t.elements,r=this.elements,o=n[0],a=n[3],c=n[6],l=n[1],u=n[4],h=n[7],f=n[2],p=n[5],g=n[8],v=i[0],m=i[3],d=i[6],M=i[1],b=i[4],_=i[7],C=i[2],A=i[5],E=i[8];return r[0]=o*v+a*M+c*C,r[3]=o*m+a*b+c*A,r[6]=o*d+a*_+c*E,r[1]=l*v+u*M+h*C,r[4]=l*m+u*b+h*A,r[7]=l*d+u*_+h*E,r[2]=f*v+p*M+g*C,r[5]=f*m+p*b+g*A,r[8]=f*d+p*_+g*E,this}multiplyScalar(e){let t=this.elements;return t[0]*=e,t[3]*=e,t[6]*=e,t[1]*=e,t[4]*=e,t[7]*=e,t[2]*=e,t[5]*=e,t[8]*=e,this}determinant(){let e=this.elements,t=e[0],n=e[1],i=e[2],r=e[3],o=e[4],a=e[5],c=e[6],l=e[7],u=e[8];return t*o*u-t*a*l-n*r*u+n*a*c+i*r*l-i*o*c}invert(){let e=this.elements,t=e[0],n=e[1],i=e[2],r=e[3],o=e[4],a=e[5],c=e[6],l=e[7],u=e[8],h=u*o-a*l,f=a*c-u*r,p=l*r-o*c,g=t*h+n*f+i*p;if(g===0)return this.set(0,0,0,0,0,0,0,0,0);let v=1/g;return e[0]=h*v,e[1]=(i*l-u*n)*v,e[2]=(a*n-i*o)*v,e[3]=f*v,e[4]=(u*t-i*c)*v,e[5]=(i*r-a*t)*v,e[6]=p*v,e[7]=(n*c-l*t)*v,e[8]=(o*t-n*r)*v,this}transpose(){let e,t=this.elements;return e=t[1],t[1]=t[3],t[3]=e,e=t[2],t[2]=t[6],t[6]=e,e=t[5],t[5]=t[7],t[7]=e,this}getNormalMatrix(e){return this.setFromMatrix4(e).invert().transpose()}transposeIntoArray(e){let t=this.elements;return e[0]=t[0],e[1]=t[3],e[2]=t[6],e[3]=t[1],e[4]=t[4],e[5]=t[7],e[6]=t[2],e[7]=t[5],e[8]=t[8],this}setUvTransform(e,t,n,i,r,o,a){let c=Math.cos(r),l=Math.sin(r);return this.set(n*c,n*l,-n*(c*o+l*a)+o+e,-i*l,i*c,-i*(-l*o+c*a)+a+t,0,0,1),this}scale(e,t){return this.premultiply(Ao.makeScale(e,t)),this}rotate(e){return this.premultiply(Ao.makeRotation(-e)),this}translate(e,t){return this.premultiply(Ao.makeTranslation(e,t)),this}makeTranslation(e,t){return e.isVector2?this.set(1,0,e.x,0,1,e.y,0,0,1):this.set(1,0,e,0,1,t,0,0,1),this}makeRotation(e){let t=Math.cos(e),n=Math.sin(e);return this.set(t,-n,0,n,t,0,0,0,1),this}makeScale(e,t){return this.set(e,0,0,0,t,0,0,0,1),this}equals(e){let t=this.elements,n=e.elements;for(let i=0;i<9;i++)if(t[i]!==n[i])return!1;return!0}fromArray(e,t=0){for(let n=0;n<9;n++)this.elements[n]=e[n+t];return this}toArray(e=[],t=0){let n=this.elements;return e[t]=n[0],e[t+1]=n[1],e[t+2]=n[2],e[t+3]=n[3],e[t+4]=n[4],e[t+5]=n[5],e[t+6]=n[6],e[t+7]=n[7],e[t+8]=n[8],e}clone(){return new this.constructor().fromArray(this.elements)}},Ao=new ke;function ch(s){for(let e=s.length-1;e>=0;--e)if(s[e]>=65535)return!0;return!1}function Zs(s){return document.createElementNS("http://www.w3.org/1999/xhtml",s)}function Zf(){let s=Zs("canvas");return s.style.display="block",s}var zl={};function Hs(s){s in zl||(zl[s]=!0,console.warn(s))}function Kf(s,e,t){return new Promise(function(n,i){function r(){switch(s.clientWaitSync(e,s.SYNC_FLUSH_COMMANDS_BIT,0)){case s.WAIT_FAILED:i();break;case s.TIMEOUT_EXPIRED:setTimeout(r,t);break;default:n()}}setTimeout(r,t)})}function Jf(s){let e=s.elements;e[2]=.5*e[2]+.5*e[3],e[6]=.5*e[6]+.5*e[7],e[10]=.5*e[10]+.5*e[11],e[14]=.5*e[14]+.5*e[15]}function jf(s){let e=s.elements;e[11]===-1?(e[10]=-e[10]-1,e[14]=-e[14]):(e[10]=-e[10],e[14]=-e[14]+1)}var Ye={enabled:!0,workingColorSpace:Wt,spaces:{},convert:function(s,e,t){return this.enabled===!1||e===t||!e||!t||(this.spaces[e].transfer===lt&&(s.r=Xn(s.r),s.g=Xn(s.g),s.b=Xn(s.b)),this.spaces[e].primaries!==this.spaces[t].primaries&&(s.applyMatrix3(this.spaces[e].toXYZ),s.applyMatrix3(this.spaces[t].fromXYZ)),this.spaces[t].transfer===lt&&(s.r=ts(s.r),s.g=ts(s.g),s.b=ts(s.b))),s},fromWorkingColorSpace:function(s,e){return this.convert(s,this.workingColorSpace,e)},toWorkingColorSpace:function(s,e){return this.convert(s,e,this.workingColorSpace)},getPrimaries:function(s){return this.spaces[s].primaries},getTransfer:function(s){return s===fn?go:this.spaces[s].transfer},getLuminanceCoefficients:function(s,e=this.workingColorSpace){return s.fromArray(this.spaces[e].luminanceCoefficients)},define:function(s){Object.assign(this.spaces,s)},_getMatrix:function(s,e,t){return s.copy(this.spaces[e].toXYZ).multiply(this.spaces[t].fromXYZ)},_getDrawingBufferColorSpace:function(s){return this.spaces[s].outputColorSpaceConfig.drawingBufferColorSpace},_getUnpackColorSpace:function(s=this.workingColorSpace){return this.spaces[s].workingColorSpaceConfig.unpackColorSpace}};function Xn(s){return s<.04045?s*.0773993808:Math.pow(s*.9478672986+.0521327014,2.4)}function ts(s){return s<.0031308?s*12.92:1.055*Math.pow(s,.41666)-.055}var kl=[.64,.33,.3,.6,.15,.06],Hl=[.2126,.7152,.0722],Vl=[.3127,.329],Gl=new ke().set(.4123908,.3575843,.1804808,.212639,.7151687,.0721923,.0193308,.1191948,.9505322),Wl=new ke().set(3.2409699,-1.5373832,-.4986108,-.9692436,1.8759675,.0415551,.0556301,-.203977,1.0569715);Ye.define({[Wt]:{primaries:kl,whitePoint:Vl,transfer:go,toXYZ:Gl,fromXYZ:Wl,luminanceCoefficients:Hl,workingColorSpaceConfig:{unpackColorSpace:St},outputColorSpaceConfig:{drawingBufferColorSpace:St}},[St]:{primaries:kl,whitePoint:Vl,transfer:lt,toXYZ:Gl,fromXYZ:Wl,luminanceCoefficients:Hl,outputColorSpaceConfig:{drawingBufferColorSpace:St}}});var Oi,Va=class{static getDataURL(e){if(/^data:/i.test(e.src)||typeof HTMLCanvasElement>"u")return e.src;let t;if(e instanceof HTMLCanvasElement)t=e;else{Oi===void 0&&(Oi=Zs("canvas")),Oi.width=e.width,Oi.height=e.height;let n=Oi.getContext("2d");e instanceof ImageData?n.putImageData(e,0,0):n.drawImage(e,0,0,e.width,e.height),t=Oi}return t.width>2048||t.height>2048?(console.warn("THREE.ImageUtils.getDataURL: Image converted to jpg for performance reasons",e),t.toDataURL("image/jpeg",.6)):t.toDataURL("image/png")}static sRGBToLinear(e){if(typeof HTMLImageElement<"u"&&e instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&e instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&e instanceof ImageBitmap){let t=Zs("canvas");t.width=e.width,t.height=e.height;let n=t.getContext("2d");n.drawImage(e,0,0,e.width,e.height);let i=n.getImageData(0,0,e.width,e.height),r=i.data;for(let o=0;o<r.length;o++)r[o]=Xn(r[o]/255)*255;return n.putImageData(i,0,0),t}else if(e.data){let t=e.data.slice(0);for(let n=0;n<t.length;n++)t instanceof Uint8Array||t instanceof Uint8ClampedArray?t[n]=Math.floor(Xn(t[n]/255)*255):t[n]=Xn(t[n]);return{data:t,width:e.width,height:e.height}}else return console.warn("THREE.ImageUtils.sRGBToLinear(): Unsupported image type. No color space conversion applied."),e}},Qf=0,Yr=class{constructor(e=null){this.isSource=!0,Object.defineProperty(this,"id",{value:Qf++}),this.uuid=An(),this.data=e,this.dataReady=!0,this.version=0}set needsUpdate(e){e===!0&&this.version++}toJSON(e){let t=e===void 0||typeof e=="string";if(!t&&e.images[this.uuid]!==void 0)return e.images[this.uuid];let n={uuid:this.uuid,url:""},i=this.data;if(i!==null){let r;if(Array.isArray(i)){r=[];for(let o=0,a=i.length;o<a;o++)i[o].isDataTexture?r.push(Ro(i[o].image)):r.push(Ro(i[o]))}else r=Ro(i);n.url=r}return t||(e.images[this.uuid]=n),n}};function Ro(s){return typeof HTMLImageElement<"u"&&s instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&s instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&s instanceof ImageBitmap?Va.getDataURL(s):s.data?{data:Array.from(s.data),width:s.width,height:s.height,type:s.data.constructor.name}:(console.warn("THREE.Texture: Unable to serialize Texture."),{})}var ed=0,Pt=class s extends ui{constructor(e=s.DEFAULT_IMAGE,t=s.DEFAULT_MAPPING,n=En,i=En,r=wt,o=Pn,a=Ht,c=Dt,l=s.DEFAULT_ANISOTROPY,u=fn){super(),this.isTexture=!0,Object.defineProperty(this,"id",{value:ed++}),this.uuid=An(),this.name="",this.source=new Yr(e),this.mipmaps=[],this.mapping=t,this.channel=0,this.wrapS=n,this.wrapT=i,this.magFilter=r,this.minFilter=o,this.anisotropy=l,this.format=a,this.internalFormat=null,this.type=c,this.offset=new le(0,0),this.repeat=new le(1,1),this.center=new le(0,0),this.rotation=0,this.matrixAutoUpdate=!0,this.matrix=new ke,this.generateMipmaps=!0,this.premultiplyAlpha=!1,this.flipY=!0,this.unpackAlignment=4,this.colorSpace=u,this.userData={},this.version=0,this.onUpdate=null,this.isRenderTargetTexture=!1,this.pmremVersion=0}get image(){return this.source.data}set image(e=null){this.source.data=e}updateMatrix(){this.matrix.setUvTransform(this.offset.x,this.offset.y,this.repeat.x,this.repeat.y,this.rotation,this.center.x,this.center.y)}clone(){return new this.constructor().copy(this)}copy(e){return this.name=e.name,this.source=e.source,this.mipmaps=e.mipmaps.slice(0),this.mapping=e.mapping,this.channel=e.channel,this.wrapS=e.wrapS,this.wrapT=e.wrapT,this.magFilter=e.magFilter,this.minFilter=e.minFilter,this.anisotropy=e.anisotropy,this.format=e.format,this.internalFormat=e.internalFormat,this.type=e.type,this.offset.copy(e.offset),this.repeat.copy(e.repeat),this.center.copy(e.center),this.rotation=e.rotation,this.matrixAutoUpdate=e.matrixAutoUpdate,this.matrix.copy(e.matrix),this.generateMipmaps=e.generateMipmaps,this.premultiplyAlpha=e.premultiplyAlpha,this.flipY=e.flipY,this.unpackAlignment=e.unpackAlignment,this.colorSpace=e.colorSpace,this.userData=JSON.parse(JSON.stringify(e.userData)),this.needsUpdate=!0,this}toJSON(e){let t=e===void 0||typeof e=="string";if(!t&&e.textures[this.uuid]!==void 0)return e.textures[this.uuid];let n={metadata:{version:4.6,type:"Texture",generator:"Texture.toJSON"},uuid:this.uuid,name:this.name,image:this.source.toJSON(e).uuid,mapping:this.mapping,channel:this.channel,repeat:[this.repeat.x,this.repeat.y],offset:[this.offset.x,this.offset.y],center:[this.center.x,this.center.y],rotation:this.rotation,wrap:[this.wrapS,this.wrapT],format:this.format,internalFormat:this.internalFormat,type:this.type,colorSpace:this.colorSpace,minFilter:this.minFilter,magFilter:this.magFilter,anisotropy:this.anisotropy,flipY:this.flipY,generateMipmaps:this.generateMipmaps,premultiplyAlpha:this.premultiplyAlpha,unpackAlignment:this.unpackAlignment};return Object.keys(this.userData).length>0&&(n.userData=this.userData),t||(e.textures[this.uuid]=n),n}dispose(){this.dispatchEvent({type:"dispose"})}transformUv(e){if(this.mapping!==Zu)return e;if(e.applyMatrix3(this.matrix),e.x<0||e.x>1)switch(this.wrapS){case qn:e.x=e.x-Math.floor(e.x);break;case En:e.x=e.x<0?0:1;break;case Ys:Math.abs(Math.floor(e.x)%2)===1?e.x=Math.ceil(e.x)-e.x:e.x=e.x-Math.floor(e.x);break}if(e.y<0||e.y>1)switch(this.wrapT){case qn:e.y=e.y-Math.floor(e.y);break;case En:e.y=e.y<0?0:1;break;case Ys:Math.abs(Math.floor(e.y)%2)===1?e.y=Math.ceil(e.y)-e.y:e.y=e.y-Math.floor(e.y);break}return this.flipY&&(e.y=1-e.y),e}set needsUpdate(e){e===!0&&(this.version++,this.source.needsUpdate=!0)}set needsPMREMUpdate(e){e===!0&&this.pmremVersion++}};Pt.DEFAULT_IMAGE=null;Pt.DEFAULT_MAPPING=Zu;Pt.DEFAULT_ANISOTROPY=1;var We=class s{constructor(e=0,t=0,n=0,i=1){s.prototype.isVector4=!0,this.x=e,this.y=t,this.z=n,this.w=i}get width(){return this.z}set width(e){this.z=e}get height(){return this.w}set height(e){this.w=e}set(e,t,n,i){return this.x=e,this.y=t,this.z=n,this.w=i,this}setScalar(e){return this.x=e,this.y=e,this.z=e,this.w=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setZ(e){return this.z=e,this}setW(e){return this.w=e,this}setComponent(e,t){switch(e){case 0:this.x=t;break;case 1:this.y=t;break;case 2:this.z=t;break;case 3:this.w=t;break;default:throw new Error("index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;case 2:return this.z;case 3:return this.w;default:throw new Error("index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y,this.z,this.w)}copy(e){return this.x=e.x,this.y=e.y,this.z=e.z,this.w=e.w!==void 0?e.w:1,this}add(e){return this.x+=e.x,this.y+=e.y,this.z+=e.z,this.w+=e.w,this}addScalar(e){return this.x+=e,this.y+=e,this.z+=e,this.w+=e,this}addVectors(e,t){return this.x=e.x+t.x,this.y=e.y+t.y,this.z=e.z+t.z,this.w=e.w+t.w,this}addScaledVector(e,t){return this.x+=e.x*t,this.y+=e.y*t,this.z+=e.z*t,this.w+=e.w*t,this}sub(e){return this.x-=e.x,this.y-=e.y,this.z-=e.z,this.w-=e.w,this}subScalar(e){return this.x-=e,this.y-=e,this.z-=e,this.w-=e,this}subVectors(e,t){return this.x=e.x-t.x,this.y=e.y-t.y,this.z=e.z-t.z,this.w=e.w-t.w,this}multiply(e){return this.x*=e.x,this.y*=e.y,this.z*=e.z,this.w*=e.w,this}multiplyScalar(e){return this.x*=e,this.y*=e,this.z*=e,this.w*=e,this}applyMatrix4(e){let t=this.x,n=this.y,i=this.z,r=this.w,o=e.elements;return this.x=o[0]*t+o[4]*n+o[8]*i+o[12]*r,this.y=o[1]*t+o[5]*n+o[9]*i+o[13]*r,this.z=o[2]*t+o[6]*n+o[10]*i+o[14]*r,this.w=o[3]*t+o[7]*n+o[11]*i+o[15]*r,this}divide(e){return this.x/=e.x,this.y/=e.y,this.z/=e.z,this.w/=e.w,this}divideScalar(e){return this.multiplyScalar(1/e)}setAxisAngleFromQuaternion(e){this.w=2*Math.acos(e.w);let t=Math.sqrt(1-e.w*e.w);return t<1e-4?(this.x=1,this.y=0,this.z=0):(this.x=e.x/t,this.y=e.y/t,this.z=e.z/t),this}setAxisAngleFromRotationMatrix(e){let t,n,i,r,c=e.elements,l=c[0],u=c[4],h=c[8],f=c[1],p=c[5],g=c[9],v=c[2],m=c[6],d=c[10];if(Math.abs(u-f)<.01&&Math.abs(h-v)<.01&&Math.abs(g-m)<.01){if(Math.abs(u+f)<.1&&Math.abs(h+v)<.1&&Math.abs(g+m)<.1&&Math.abs(l+p+d-3)<.1)return this.set(1,0,0,0),this;t=Math.PI;let b=(l+1)/2,_=(p+1)/2,C=(d+1)/2,A=(u+f)/4,E=(h+v)/4,I=(g+m)/4;return b>_&&b>C?b<.01?(n=0,i=.707106781,r=.707106781):(n=Math.sqrt(b),i=A/n,r=E/n):_>C?_<.01?(n=.707106781,i=0,r=.707106781):(i=Math.sqrt(_),n=A/i,r=I/i):C<.01?(n=.707106781,i=.707106781,r=0):(r=Math.sqrt(C),n=E/r,i=I/r),this.set(n,i,r,t),this}let M=Math.sqrt((m-g)*(m-g)+(h-v)*(h-v)+(f-u)*(f-u));return Math.abs(M)<.001&&(M=1),this.x=(m-g)/M,this.y=(h-v)/M,this.z=(f-u)/M,this.w=Math.acos((l+p+d-1)/2),this}setFromMatrixPosition(e){let t=e.elements;return this.x=t[12],this.y=t[13],this.z=t[14],this.w=t[15],this}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this.z=Math.min(this.z,e.z),this.w=Math.min(this.w,e.w),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this.z=Math.max(this.z,e.z),this.w=Math.max(this.w,e.w),this}clamp(e,t){return this.x=Math.max(e.x,Math.min(t.x,this.x)),this.y=Math.max(e.y,Math.min(t.y,this.y)),this.z=Math.max(e.z,Math.min(t.z,this.z)),this.w=Math.max(e.w,Math.min(t.w,this.w)),this}clampScalar(e,t){return this.x=Math.max(e,Math.min(t,this.x)),this.y=Math.max(e,Math.min(t,this.y)),this.z=Math.max(e,Math.min(t,this.z)),this.w=Math.max(e,Math.min(t,this.w)),this}clampLength(e,t){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(e,Math.min(t,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this.w=Math.floor(this.w),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this.w=Math.ceil(this.w),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this.w=Math.round(this.w),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this.w=Math.trunc(this.w),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this.w=-this.w,this}dot(e){return this.x*e.x+this.y*e.y+this.z*e.z+this.w*e.w}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)+Math.abs(this.w)}normalize(){return this.divideScalar(this.length()||1)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,t){return this.x+=(e.x-this.x)*t,this.y+=(e.y-this.y)*t,this.z+=(e.z-this.z)*t,this.w+=(e.w-this.w)*t,this}lerpVectors(e,t,n){return this.x=e.x+(t.x-e.x)*n,this.y=e.y+(t.y-e.y)*n,this.z=e.z+(t.z-e.z)*n,this.w=e.w+(t.w-e.w)*n,this}equals(e){return e.x===this.x&&e.y===this.y&&e.z===this.z&&e.w===this.w}fromArray(e,t=0){return this.x=e[t],this.y=e[t+1],this.z=e[t+2],this.w=e[t+3],this}toArray(e=[],t=0){return e[t]=this.x,e[t+1]=this.y,e[t+2]=this.z,e[t+3]=this.w,e}fromBufferAttribute(e,t){return this.x=e.getX(t),this.y=e.getY(t),this.z=e.getZ(t),this.w=e.getW(t),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this.w=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z,yield this.w}},Ga=class extends ui{constructor(e=1,t=1,n={}){super(),this.isRenderTarget=!0,this.width=e,this.height=t,this.depth=1,this.scissor=new We(0,0,e,t),this.scissorTest=!1,this.viewport=new We(0,0,e,t);let i={width:e,height:t,depth:1};n=Object.assign({generateMipmaps:!1,internalFormat:null,minFilter:wt,depthBuffer:!0,stencilBuffer:!1,resolveDepthBuffer:!0,resolveStencilBuffer:!0,depthTexture:null,samples:0,count:1},n);let r=new Pt(i,n.mapping,n.wrapS,n.wrapT,n.magFilter,n.minFilter,n.format,n.type,n.anisotropy,n.colorSpace);r.flipY=!1,r.generateMipmaps=n.generateMipmaps,r.internalFormat=n.internalFormat,this.textures=[];let o=n.count;for(let a=0;a<o;a++)this.textures[a]=r.clone(),this.textures[a].isRenderTargetTexture=!0;this.depthBuffer=n.depthBuffer,this.stencilBuffer=n.stencilBuffer,this.resolveDepthBuffer=n.resolveDepthBuffer,this.resolveStencilBuffer=n.resolveStencilBuffer,this.depthTexture=n.depthTexture,this.samples=n.samples}get texture(){return this.textures[0]}set texture(e){this.textures[0]=e}setSize(e,t,n=1){if(this.width!==e||this.height!==t||this.depth!==n){this.width=e,this.height=t,this.depth=n;for(let i=0,r=this.textures.length;i<r;i++)this.textures[i].image.width=e,this.textures[i].image.height=t,this.textures[i].image.depth=n;this.dispose()}this.viewport.set(0,0,e,t),this.scissor.set(0,0,e,t)}clone(){return new this.constructor().copy(this)}copy(e){this.width=e.width,this.height=e.height,this.depth=e.depth,this.scissor.copy(e.scissor),this.scissorTest=e.scissorTest,this.viewport.copy(e.viewport),this.textures.length=0;for(let n=0,i=e.textures.length;n<i;n++)this.textures[n]=e.textures[n].clone(),this.textures[n].isRenderTargetTexture=!0;let t=Object.assign({},e.texture.image);return this.texture.source=new Yr(t),this.depthBuffer=e.depthBuffer,this.stencilBuffer=e.stencilBuffer,this.resolveDepthBuffer=e.resolveDepthBuffer,this.resolveStencilBuffer=e.resolveStencilBuffer,e.depthTexture!==null&&(this.depthTexture=e.depthTexture.clone()),this.samples=e.samples,this}dispose(){this.dispatchEvent({type:"dispose"})}},Rn=class extends Ga{constructor(e=1,t=1,n={}){super(e,t,n),this.isWebGLRenderTarget=!0}},$r=class extends Pt{constructor(e=null,t=1,n=1,i=1){super(null),this.isDataArrayTexture=!0,this.image={data:e,width:t,height:n,depth:i},this.magFilter=yt,this.minFilter=yt,this.wrapR=En,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1,this.layerUpdates=new Set}addLayerUpdate(e){this.layerUpdates.add(e)}clearLayerUpdates(){this.layerUpdates.clear()}};var Wa=class extends Pt{constructor(e=null,t=1,n=1,i=1){super(null),this.isData3DTexture=!0,this.image={data:e,width:t,height:n,depth:i},this.magFilter=yt,this.minFilter=yt,this.wrapR=En,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}};var rn=class{constructor(e=0,t=0,n=0,i=1){this.isQuaternion=!0,this._x=e,this._y=t,this._z=n,this._w=i}static slerpFlat(e,t,n,i,r,o,a){let c=n[i+0],l=n[i+1],u=n[i+2],h=n[i+3],f=r[o+0],p=r[o+1],g=r[o+2],v=r[o+3];if(a===0){e[t+0]=c,e[t+1]=l,e[t+2]=u,e[t+3]=h;return}if(a===1){e[t+0]=f,e[t+1]=p,e[t+2]=g,e[t+3]=v;return}if(h!==v||c!==f||l!==p||u!==g){let m=1-a,d=c*f+l*p+u*g+h*v,M=d>=0?1:-1,b=1-d*d;if(b>Number.EPSILON){let C=Math.sqrt(b),A=Math.atan2(C,d*M);m=Math.sin(m*A)/C,a=Math.sin(a*A)/C}let _=a*M;if(c=c*m+f*_,l=l*m+p*_,u=u*m+g*_,h=h*m+v*_,m===1-a){let C=1/Math.sqrt(c*c+l*l+u*u+h*h);c*=C,l*=C,u*=C,h*=C}}e[t]=c,e[t+1]=l,e[t+2]=u,e[t+3]=h}static multiplyQuaternionsFlat(e,t,n,i,r,o){let a=n[i],c=n[i+1],l=n[i+2],u=n[i+3],h=r[o],f=r[o+1],p=r[o+2],g=r[o+3];return e[t]=a*g+u*h+c*p-l*f,e[t+1]=c*g+u*f+l*h-a*p,e[t+2]=l*g+u*p+a*f-c*h,e[t+3]=u*g-a*h-c*f-l*p,e}get x(){return this._x}set x(e){this._x=e,this._onChangeCallback()}get y(){return this._y}set y(e){this._y=e,this._onChangeCallback()}get z(){return this._z}set z(e){this._z=e,this._onChangeCallback()}get w(){return this._w}set w(e){this._w=e,this._onChangeCallback()}set(e,t,n,i){return this._x=e,this._y=t,this._z=n,this._w=i,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._w)}copy(e){return this._x=e.x,this._y=e.y,this._z=e.z,this._w=e.w,this._onChangeCallback(),this}setFromEuler(e,t=!0){let n=e._x,i=e._y,r=e._z,o=e._order,a=Math.cos,c=Math.sin,l=a(n/2),u=a(i/2),h=a(r/2),f=c(n/2),p=c(i/2),g=c(r/2);switch(o){case"XYZ":this._x=f*u*h+l*p*g,this._y=l*p*h-f*u*g,this._z=l*u*g+f*p*h,this._w=l*u*h-f*p*g;break;case"YXZ":this._x=f*u*h+l*p*g,this._y=l*p*h-f*u*g,this._z=l*u*g-f*p*h,this._w=l*u*h+f*p*g;break;case"ZXY":this._x=f*u*h-l*p*g,this._y=l*p*h+f*u*g,this._z=l*u*g+f*p*h,this._w=l*u*h-f*p*g;break;case"ZYX":this._x=f*u*h-l*p*g,this._y=l*p*h+f*u*g,this._z=l*u*g-f*p*h,this._w=l*u*h+f*p*g;break;case"YZX":this._x=f*u*h+l*p*g,this._y=l*p*h+f*u*g,this._z=l*u*g-f*p*h,this._w=l*u*h-f*p*g;break;case"XZY":this._x=f*u*h-l*p*g,this._y=l*p*h-f*u*g,this._z=l*u*g+f*p*h,this._w=l*u*h+f*p*g;break;default:console.warn("THREE.Quaternion: .setFromEuler() encountered an unknown order: "+o)}return t===!0&&this._onChangeCallback(),this}setFromAxisAngle(e,t){let n=t/2,i=Math.sin(n);return this._x=e.x*i,this._y=e.y*i,this._z=e.z*i,this._w=Math.cos(n),this._onChangeCallback(),this}setFromRotationMatrix(e){let t=e.elements,n=t[0],i=t[4],r=t[8],o=t[1],a=t[5],c=t[9],l=t[2],u=t[6],h=t[10],f=n+a+h;if(f>0){let p=.5/Math.sqrt(f+1);this._w=.25/p,this._x=(u-c)*p,this._y=(r-l)*p,this._z=(o-i)*p}else if(n>a&&n>h){let p=2*Math.sqrt(1+n-a-h);this._w=(u-c)/p,this._x=.25*p,this._y=(i+o)/p,this._z=(r+l)/p}else if(a>h){let p=2*Math.sqrt(1+a-n-h);this._w=(r-l)/p,this._x=(i+o)/p,this._y=.25*p,this._z=(c+u)/p}else{let p=2*Math.sqrt(1+h-n-a);this._w=(o-i)/p,this._x=(r+l)/p,this._y=(c+u)/p,this._z=.25*p}return this._onChangeCallback(),this}setFromUnitVectors(e,t){let n=e.dot(t)+1;return n<Number.EPSILON?(n=0,Math.abs(e.x)>Math.abs(e.z)?(this._x=-e.y,this._y=e.x,this._z=0,this._w=n):(this._x=0,this._y=-e.z,this._z=e.y,this._w=n)):(this._x=e.y*t.z-e.z*t.y,this._y=e.z*t.x-e.x*t.z,this._z=e.x*t.y-e.y*t.x,this._w=n),this.normalize()}angleTo(e){return 2*Math.acos(Math.abs(kt(this.dot(e),-1,1)))}rotateTowards(e,t){let n=this.angleTo(e);if(n===0)return this;let i=Math.min(1,t/n);return this.slerp(e,i),this}identity(){return this.set(0,0,0,1)}invert(){return this.conjugate()}conjugate(){return this._x*=-1,this._y*=-1,this._z*=-1,this._onChangeCallback(),this}dot(e){return this._x*e._x+this._y*e._y+this._z*e._z+this._w*e._w}lengthSq(){return this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w}length(){return Math.sqrt(this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w)}normalize(){let e=this.length();return e===0?(this._x=0,this._y=0,this._z=0,this._w=1):(e=1/e,this._x=this._x*e,this._y=this._y*e,this._z=this._z*e,this._w=this._w*e),this._onChangeCallback(),this}multiply(e){return this.multiplyQuaternions(this,e)}premultiply(e){return this.multiplyQuaternions(e,this)}multiplyQuaternions(e,t){let n=e._x,i=e._y,r=e._z,o=e._w,a=t._x,c=t._y,l=t._z,u=t._w;return this._x=n*u+o*a+i*l-r*c,this._y=i*u+o*c+r*a-n*l,this._z=r*u+o*l+n*c-i*a,this._w=o*u-n*a-i*c-r*l,this._onChangeCallback(),this}slerp(e,t){if(t===0)return this;if(t===1)return this.copy(e);let n=this._x,i=this._y,r=this._z,o=this._w,a=o*e._w+n*e._x+i*e._y+r*e._z;if(a<0?(this._w=-e._w,this._x=-e._x,this._y=-e._y,this._z=-e._z,a=-a):this.copy(e),a>=1)return this._w=o,this._x=n,this._y=i,this._z=r,this;let c=1-a*a;if(c<=Number.EPSILON){let p=1-t;return this._w=p*o+t*this._w,this._x=p*n+t*this._x,this._y=p*i+t*this._y,this._z=p*r+t*this._z,this.normalize(),this}let l=Math.sqrt(c),u=Math.atan2(l,a),h=Math.sin((1-t)*u)/l,f=Math.sin(t*u)/l;return this._w=o*h+this._w*f,this._x=n*h+this._x*f,this._y=i*h+this._y*f,this._z=r*h+this._z*f,this._onChangeCallback(),this}slerpQuaternions(e,t,n){return this.copy(e).slerp(t,n)}random(){let e=2*Math.PI*Math.random(),t=2*Math.PI*Math.random(),n=Math.random(),i=Math.sqrt(1-n),r=Math.sqrt(n);return this.set(i*Math.sin(e),i*Math.cos(e),r*Math.sin(t),r*Math.cos(t))}equals(e){return e._x===this._x&&e._y===this._y&&e._z===this._z&&e._w===this._w}fromArray(e,t=0){return this._x=e[t],this._y=e[t+1],this._z=e[t+2],this._w=e[t+3],this._onChangeCallback(),this}toArray(e=[],t=0){return e[t]=this._x,e[t+1]=this._y,e[t+2]=this._z,e[t+3]=this._w,e}fromBufferAttribute(e,t){return this._x=e.getX(t),this._y=e.getY(t),this._z=e.getZ(t),this._w=e.getW(t),this._onChangeCallback(),this}toJSON(){return this.toArray()}_onChange(e){return this._onChangeCallback=e,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._w}},P=class s{constructor(e=0,t=0,n=0){s.prototype.isVector3=!0,this.x=e,this.y=t,this.z=n}set(e,t,n){return n===void 0&&(n=this.z),this.x=e,this.y=t,this.z=n,this}setScalar(e){return this.x=e,this.y=e,this.z=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setZ(e){return this.z=e,this}setComponent(e,t){switch(e){case 0:this.x=t;break;case 1:this.y=t;break;case 2:this.z=t;break;default:throw new Error("index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;case 2:return this.z;default:throw new Error("index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y,this.z)}copy(e){return this.x=e.x,this.y=e.y,this.z=e.z,this}add(e){return this.x+=e.x,this.y+=e.y,this.z+=e.z,this}addScalar(e){return this.x+=e,this.y+=e,this.z+=e,this}addVectors(e,t){return this.x=e.x+t.x,this.y=e.y+t.y,this.z=e.z+t.z,this}addScaledVector(e,t){return this.x+=e.x*t,this.y+=e.y*t,this.z+=e.z*t,this}sub(e){return this.x-=e.x,this.y-=e.y,this.z-=e.z,this}subScalar(e){return this.x-=e,this.y-=e,this.z-=e,this}subVectors(e,t){return this.x=e.x-t.x,this.y=e.y-t.y,this.z=e.z-t.z,this}multiply(e){return this.x*=e.x,this.y*=e.y,this.z*=e.z,this}multiplyScalar(e){return this.x*=e,this.y*=e,this.z*=e,this}multiplyVectors(e,t){return this.x=e.x*t.x,this.y=e.y*t.y,this.z=e.z*t.z,this}applyEuler(e){return this.applyQuaternion(Xl.setFromEuler(e))}applyAxisAngle(e,t){return this.applyQuaternion(Xl.setFromAxisAngle(e,t))}applyMatrix3(e){let t=this.x,n=this.y,i=this.z,r=e.elements;return this.x=r[0]*t+r[3]*n+r[6]*i,this.y=r[1]*t+r[4]*n+r[7]*i,this.z=r[2]*t+r[5]*n+r[8]*i,this}applyNormalMatrix(e){return this.applyMatrix3(e).normalize()}applyMatrix4(e){let t=this.x,n=this.y,i=this.z,r=e.elements,o=1/(r[3]*t+r[7]*n+r[11]*i+r[15]);return this.x=(r[0]*t+r[4]*n+r[8]*i+r[12])*o,this.y=(r[1]*t+r[5]*n+r[9]*i+r[13])*o,this.z=(r[2]*t+r[6]*n+r[10]*i+r[14])*o,this}applyQuaternion(e){let t=this.x,n=this.y,i=this.z,r=e.x,o=e.y,a=e.z,c=e.w,l=2*(o*i-a*n),u=2*(a*t-r*i),h=2*(r*n-o*t);return this.x=t+c*l+o*h-a*u,this.y=n+c*u+a*l-r*h,this.z=i+c*h+r*u-o*l,this}project(e){return this.applyMatrix4(e.matrixWorldInverse).applyMatrix4(e.projectionMatrix)}unproject(e){return this.applyMatrix4(e.projectionMatrixInverse).applyMatrix4(e.matrixWorld)}transformDirection(e){let t=this.x,n=this.y,i=this.z,r=e.elements;return this.x=r[0]*t+r[4]*n+r[8]*i,this.y=r[1]*t+r[5]*n+r[9]*i,this.z=r[2]*t+r[6]*n+r[10]*i,this.normalize()}divide(e){return this.x/=e.x,this.y/=e.y,this.z/=e.z,this}divideScalar(e){return this.multiplyScalar(1/e)}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this.z=Math.min(this.z,e.z),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this.z=Math.max(this.z,e.z),this}clamp(e,t){return this.x=Math.max(e.x,Math.min(t.x,this.x)),this.y=Math.max(e.y,Math.min(t.y,this.y)),this.z=Math.max(e.z,Math.min(t.z,this.z)),this}clampScalar(e,t){return this.x=Math.max(e,Math.min(t,this.x)),this.y=Math.max(e,Math.min(t,this.y)),this.z=Math.max(e,Math.min(t,this.z)),this}clampLength(e,t){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(e,Math.min(t,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this}dot(e){return this.x*e.x+this.y*e.y+this.z*e.z}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)}normalize(){return this.divideScalar(this.length()||1)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,t){return this.x+=(e.x-this.x)*t,this.y+=(e.y-this.y)*t,this.z+=(e.z-this.z)*t,this}lerpVectors(e,t,n){return this.x=e.x+(t.x-e.x)*n,this.y=e.y+(t.y-e.y)*n,this.z=e.z+(t.z-e.z)*n,this}cross(e){return this.crossVectors(this,e)}crossVectors(e,t){let n=e.x,i=e.y,r=e.z,o=t.x,a=t.y,c=t.z;return this.x=i*c-r*a,this.y=r*o-n*c,this.z=n*a-i*o,this}projectOnVector(e){let t=e.lengthSq();if(t===0)return this.set(0,0,0);let n=e.dot(this)/t;return this.copy(e).multiplyScalar(n)}projectOnPlane(e){return Co.copy(this).projectOnVector(e),this.sub(Co)}reflect(e){return this.sub(Co.copy(e).multiplyScalar(2*this.dot(e)))}angleTo(e){let t=Math.sqrt(this.lengthSq()*e.lengthSq());if(t===0)return Math.PI/2;let n=this.dot(e)/t;return Math.acos(kt(n,-1,1))}distanceTo(e){return Math.sqrt(this.distanceToSquared(e))}distanceToSquared(e){let t=this.x-e.x,n=this.y-e.y,i=this.z-e.z;return t*t+n*n+i*i}manhattanDistanceTo(e){return Math.abs(this.x-e.x)+Math.abs(this.y-e.y)+Math.abs(this.z-e.z)}setFromSpherical(e){return this.setFromSphericalCoords(e.radius,e.phi,e.theta)}setFromSphericalCoords(e,t,n){let i=Math.sin(t)*e;return this.x=i*Math.sin(n),this.y=Math.cos(t)*e,this.z=i*Math.cos(n),this}setFromCylindrical(e){return this.setFromCylindricalCoords(e.radius,e.theta,e.y)}setFromCylindricalCoords(e,t,n){return this.x=e*Math.sin(t),this.y=n,this.z=e*Math.cos(t),this}setFromMatrixPosition(e){let t=e.elements;return this.x=t[12],this.y=t[13],this.z=t[14],this}setFromMatrixScale(e){let t=this.setFromMatrixColumn(e,0).length(),n=this.setFromMatrixColumn(e,1).length(),i=this.setFromMatrixColumn(e,2).length();return this.x=t,this.y=n,this.z=i,this}setFromMatrixColumn(e,t){return this.fromArray(e.elements,t*4)}setFromMatrix3Column(e,t){return this.fromArray(e.elements,t*3)}setFromEuler(e){return this.x=e._x,this.y=e._y,this.z=e._z,this}setFromColor(e){return this.x=e.r,this.y=e.g,this.z=e.b,this}equals(e){return e.x===this.x&&e.y===this.y&&e.z===this.z}fromArray(e,t=0){return this.x=e[t],this.y=e[t+1],this.z=e[t+2],this}toArray(e=[],t=0){return e[t]=this.x,e[t+1]=this.y,e[t+2]=this.z,e}fromBufferAttribute(e,t){return this.x=e.getX(t),this.y=e.getY(t),this.z=e.getZ(t),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this}randomDirection(){let e=Math.random()*Math.PI*2,t=Math.random()*2-1,n=Math.sqrt(1-t*t);return this.x=n*Math.cos(e),this.y=t,this.z=n*Math.sin(e),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z}},Co=new P,Xl=new rn,dn=class{constructor(e=new P(1/0,1/0,1/0),t=new P(-1/0,-1/0,-1/0)){this.isBox3=!0,this.min=e,this.max=t}set(e,t){return this.min.copy(e),this.max.copy(t),this}setFromArray(e){this.makeEmpty();for(let t=0,n=e.length;t<n;t+=3)this.expandByPoint(yn.fromArray(e,t));return this}setFromBufferAttribute(e){this.makeEmpty();for(let t=0,n=e.count;t<n;t++)this.expandByPoint(yn.fromBufferAttribute(e,t));return this}setFromPoints(e){this.makeEmpty();for(let t=0,n=e.length;t<n;t++)this.expandByPoint(e[t]);return this}setFromCenterAndSize(e,t){let n=yn.copy(t).multiplyScalar(.5);return this.min.copy(e).sub(n),this.max.copy(e).add(n),this}setFromObject(e,t=!1){return this.makeEmpty(),this.expandByObject(e,t)}clone(){return new this.constructor().copy(this)}copy(e){return this.min.copy(e.min),this.max.copy(e.max),this}makeEmpty(){return this.min.x=this.min.y=this.min.z=1/0,this.max.x=this.max.y=this.max.z=-1/0,this}isEmpty(){return this.max.x<this.min.x||this.max.y<this.min.y||this.max.z<this.min.z}getCenter(e){return this.isEmpty()?e.set(0,0,0):e.addVectors(this.min,this.max).multiplyScalar(.5)}getSize(e){return this.isEmpty()?e.set(0,0,0):e.subVectors(this.max,this.min)}expandByPoint(e){return this.min.min(e),this.max.max(e),this}expandByVector(e){return this.min.sub(e),this.max.add(e),this}expandByScalar(e){return this.min.addScalar(-e),this.max.addScalar(e),this}expandByObject(e,t=!1){e.updateWorldMatrix(!1,!1);let n=e.geometry;if(n!==void 0){let r=n.getAttribute("position");if(t===!0&&r!==void 0&&e.isInstancedMesh!==!0)for(let o=0,a=r.count;o<a;o++)e.isMesh===!0?e.getVertexPosition(o,yn):yn.fromBufferAttribute(r,o),yn.applyMatrix4(e.matrixWorld),this.expandByPoint(yn);else e.boundingBox!==void 0?(e.boundingBox===null&&e.computeBoundingBox(),pr.copy(e.boundingBox)):(n.boundingBox===null&&n.computeBoundingBox(),pr.copy(n.boundingBox)),pr.applyMatrix4(e.matrixWorld),this.union(pr)}let i=e.children;for(let r=0,o=i.length;r<o;r++)this.expandByObject(i[r],t);return this}containsPoint(e){return e.x>=this.min.x&&e.x<=this.max.x&&e.y>=this.min.y&&e.y<=this.max.y&&e.z>=this.min.z&&e.z<=this.max.z}containsBox(e){return this.min.x<=e.min.x&&e.max.x<=this.max.x&&this.min.y<=e.min.y&&e.max.y<=this.max.y&&this.min.z<=e.min.z&&e.max.z<=this.max.z}getParameter(e,t){return t.set((e.x-this.min.x)/(this.max.x-this.min.x),(e.y-this.min.y)/(this.max.y-this.min.y),(e.z-this.min.z)/(this.max.z-this.min.z))}intersectsBox(e){return e.max.x>=this.min.x&&e.min.x<=this.max.x&&e.max.y>=this.min.y&&e.min.y<=this.max.y&&e.max.z>=this.min.z&&e.min.z<=this.max.z}intersectsSphere(e){return this.clampPoint(e.center,yn),yn.distanceToSquared(e.center)<=e.radius*e.radius}intersectsPlane(e){let t,n;return e.normal.x>0?(t=e.normal.x*this.min.x,n=e.normal.x*this.max.x):(t=e.normal.x*this.max.x,n=e.normal.x*this.min.x),e.normal.y>0?(t+=e.normal.y*this.min.y,n+=e.normal.y*this.max.y):(t+=e.normal.y*this.max.y,n+=e.normal.y*this.min.y),e.normal.z>0?(t+=e.normal.z*this.min.z,n+=e.normal.z*this.max.z):(t+=e.normal.z*this.max.z,n+=e.normal.z*this.min.z),t<=-e.constant&&n>=-e.constant}intersectsTriangle(e){if(this.isEmpty())return!1;this.getCenter(Ds),mr.subVectors(this.max,Ds),Bi.subVectors(e.a,Ds),zi.subVectors(e.b,Ds),ki.subVectors(e.c,Ds),ni.subVectors(zi,Bi),ii.subVectors(ki,zi),Si.subVectors(Bi,ki);let t=[0,-ni.z,ni.y,0,-ii.z,ii.y,0,-Si.z,Si.y,ni.z,0,-ni.x,ii.z,0,-ii.x,Si.z,0,-Si.x,-ni.y,ni.x,0,-ii.y,ii.x,0,-Si.y,Si.x,0];return!Io(t,Bi,zi,ki,mr)||(t=[1,0,0,0,1,0,0,0,1],!Io(t,Bi,zi,ki,mr))?!1:(gr.crossVectors(ni,ii),t=[gr.x,gr.y,gr.z],Io(t,Bi,zi,ki,mr))}clampPoint(e,t){return t.copy(e).clamp(this.min,this.max)}distanceToPoint(e){return this.clampPoint(e,yn).distanceTo(e)}getBoundingSphere(e){return this.isEmpty()?e.makeEmpty():(this.getCenter(e.center),e.radius=this.getSize(yn).length()*.5),e}intersect(e){return this.min.max(e.min),this.max.min(e.max),this.isEmpty()&&this.makeEmpty(),this}union(e){return this.min.min(e.min),this.max.max(e.max),this}applyMatrix4(e){return this.isEmpty()?this:(On[0].set(this.min.x,this.min.y,this.min.z).applyMatrix4(e),On[1].set(this.min.x,this.min.y,this.max.z).applyMatrix4(e),On[2].set(this.min.x,this.max.y,this.min.z).applyMatrix4(e),On[3].set(this.min.x,this.max.y,this.max.z).applyMatrix4(e),On[4].set(this.max.x,this.min.y,this.min.z).applyMatrix4(e),On[5].set(this.max.x,this.min.y,this.max.z).applyMatrix4(e),On[6].set(this.max.x,this.max.y,this.min.z).applyMatrix4(e),On[7].set(this.max.x,this.max.y,this.max.z).applyMatrix4(e),this.setFromPoints(On),this)}translate(e){return this.min.add(e),this.max.add(e),this}equals(e){return e.min.equals(this.min)&&e.max.equals(this.max)}},On=[new P,new P,new P,new P,new P,new P,new P,new P],yn=new P,pr=new dn,Bi=new P,zi=new P,ki=new P,ni=new P,ii=new P,Si=new P,Ds=new P,mr=new P,gr=new P,wi=new P;function Io(s,e,t,n,i){for(let r=0,o=s.length-3;r<=o;r+=3){wi.fromArray(s,r);let a=i.x*Math.abs(wi.x)+i.y*Math.abs(wi.y)+i.z*Math.abs(wi.z),c=e.dot(wi),l=t.dot(wi),u=n.dot(wi);if(Math.max(-Math.max(c,l,u),Math.min(c,l,u))>a)return!1}return!0}var td=new dn,Us=new P,Po=new P,on=class{constructor(e=new P,t=-1){this.isSphere=!0,this.center=e,this.radius=t}set(e,t){return this.center.copy(e),this.radius=t,this}setFromPoints(e,t){let n=this.center;t!==void 0?n.copy(t):td.setFromPoints(e).getCenter(n);let i=0;for(let r=0,o=e.length;r<o;r++)i=Math.max(i,n.distanceToSquared(e[r]));return this.radius=Math.sqrt(i),this}copy(e){return this.center.copy(e.center),this.radius=e.radius,this}isEmpty(){return this.radius<0}makeEmpty(){return this.center.set(0,0,0),this.radius=-1,this}containsPoint(e){return e.distanceToSquared(this.center)<=this.radius*this.radius}distanceToPoint(e){return e.distanceTo(this.center)-this.radius}intersectsSphere(e){let t=this.radius+e.radius;return e.center.distanceToSquared(this.center)<=t*t}intersectsBox(e){return e.intersectsSphere(this)}intersectsPlane(e){return Math.abs(e.distanceToPoint(this.center))<=this.radius}clampPoint(e,t){let n=this.center.distanceToSquared(e);return t.copy(e),n>this.radius*this.radius&&(t.sub(this.center).normalize(),t.multiplyScalar(this.radius).add(this.center)),t}getBoundingBox(e){return this.isEmpty()?(e.makeEmpty(),e):(e.set(this.center,this.center),e.expandByScalar(this.radius),e)}applyMatrix4(e){return this.center.applyMatrix4(e),this.radius=this.radius*e.getMaxScaleOnAxis(),this}translate(e){return this.center.add(e),this}expandByPoint(e){if(this.isEmpty())return this.center.copy(e),this.radius=0,this;Us.subVectors(e,this.center);let t=Us.lengthSq();if(t>this.radius*this.radius){let n=Math.sqrt(t),i=(n-this.radius)*.5;this.center.addScaledVector(Us,i/n),this.radius+=i}return this}union(e){return e.isEmpty()?this:this.isEmpty()?(this.copy(e),this):(this.center.equals(e.center)===!0?this.radius=Math.max(this.radius,e.radius):(Po.subVectors(e.center,this.center).setLength(e.radius),this.expandByPoint(Us.copy(e.center).add(Po)),this.expandByPoint(Us.copy(e.center).sub(Po))),this)}equals(e){return e.center.equals(this.center)&&e.radius===this.radius}clone(){return new this.constructor().copy(this)}},Bn=new P,Lo=new P,vr=new P,si=new P,Do=new P,xr=new P,Uo=new P,fs=class{constructor(e=new P,t=new P(0,0,-1)){this.origin=e,this.direction=t}set(e,t){return this.origin.copy(e),this.direction.copy(t),this}copy(e){return this.origin.copy(e.origin),this.direction.copy(e.direction),this}at(e,t){return t.copy(this.origin).addScaledVector(this.direction,e)}lookAt(e){return this.direction.copy(e).sub(this.origin).normalize(),this}recast(e){return this.origin.copy(this.at(e,Bn)),this}closestPointToPoint(e,t){t.subVectors(e,this.origin);let n=t.dot(this.direction);return n<0?t.copy(this.origin):t.copy(this.origin).addScaledVector(this.direction,n)}distanceToPoint(e){return Math.sqrt(this.distanceSqToPoint(e))}distanceSqToPoint(e){let t=Bn.subVectors(e,this.origin).dot(this.direction);return t<0?this.origin.distanceToSquared(e):(Bn.copy(this.origin).addScaledVector(this.direction,t),Bn.distanceToSquared(e))}distanceSqToSegment(e,t,n,i){Lo.copy(e).add(t).multiplyScalar(.5),vr.copy(t).sub(e).normalize(),si.copy(this.origin).sub(Lo);let r=e.distanceTo(t)*.5,o=-this.direction.dot(vr),a=si.dot(this.direction),c=-si.dot(vr),l=si.lengthSq(),u=Math.abs(1-o*o),h,f,p,g;if(u>0)if(h=o*c-a,f=o*a-c,g=r*u,h>=0)if(f>=-g)if(f<=g){let v=1/u;h*=v,f*=v,p=h*(h+o*f+2*a)+f*(o*h+f+2*c)+l}else f=r,h=Math.max(0,-(o*f+a)),p=-h*h+f*(f+2*c)+l;else f=-r,h=Math.max(0,-(o*f+a)),p=-h*h+f*(f+2*c)+l;else f<=-g?(h=Math.max(0,-(-o*r+a)),f=h>0?-r:Math.min(Math.max(-r,-c),r),p=-h*h+f*(f+2*c)+l):f<=g?(h=0,f=Math.min(Math.max(-r,-c),r),p=f*(f+2*c)+l):(h=Math.max(0,-(o*r+a)),f=h>0?r:Math.min(Math.max(-r,-c),r),p=-h*h+f*(f+2*c)+l);else f=o>0?-r:r,h=Math.max(0,-(o*f+a)),p=-h*h+f*(f+2*c)+l;return n&&n.copy(this.origin).addScaledVector(this.direction,h),i&&i.copy(Lo).addScaledVector(vr,f),p}intersectSphere(e,t){Bn.subVectors(e.center,this.origin);let n=Bn.dot(this.direction),i=Bn.dot(Bn)-n*n,r=e.radius*e.radius;if(i>r)return null;let o=Math.sqrt(r-i),a=n-o,c=n+o;return c<0?null:a<0?this.at(c,t):this.at(a,t)}intersectsSphere(e){return this.distanceSqToPoint(e.center)<=e.radius*e.radius}distanceToPlane(e){let t=e.normal.dot(this.direction);if(t===0)return e.distanceToPoint(this.origin)===0?0:null;let n=-(this.origin.dot(e.normal)+e.constant)/t;return n>=0?n:null}intersectPlane(e,t){let n=this.distanceToPlane(e);return n===null?null:this.at(n,t)}intersectsPlane(e){let t=e.distanceToPoint(this.origin);return t===0||e.normal.dot(this.direction)*t<0}intersectBox(e,t){let n,i,r,o,a,c,l=1/this.direction.x,u=1/this.direction.y,h=1/this.direction.z,f=this.origin;return l>=0?(n=(e.min.x-f.x)*l,i=(e.max.x-f.x)*l):(n=(e.max.x-f.x)*l,i=(e.min.x-f.x)*l),u>=0?(r=(e.min.y-f.y)*u,o=(e.max.y-f.y)*u):(r=(e.max.y-f.y)*u,o=(e.min.y-f.y)*u),n>o||r>i||((r>n||isNaN(n))&&(n=r),(o<i||isNaN(i))&&(i=o),h>=0?(a=(e.min.z-f.z)*h,c=(e.max.z-f.z)*h):(a=(e.max.z-f.z)*h,c=(e.min.z-f.z)*h),n>c||a>i)||((a>n||n!==n)&&(n=a),(c<i||i!==i)&&(i=c),i<0)?null:this.at(n>=0?n:i,t)}intersectsBox(e){return this.intersectBox(e,Bn)!==null}intersectTriangle(e,t,n,i,r){Do.subVectors(t,e),xr.subVectors(n,e),Uo.crossVectors(Do,xr);let o=this.direction.dot(Uo),a;if(o>0){if(i)return null;a=1}else if(o<0)a=-1,o=-o;else return null;si.subVectors(this.origin,e);let c=a*this.direction.dot(xr.crossVectors(si,xr));if(c<0)return null;let l=a*this.direction.dot(Do.cross(si));if(l<0||c+l>o)return null;let u=-a*si.dot(Uo);return u<0?null:this.at(u/o,r)}applyMatrix4(e){return this.origin.applyMatrix4(e),this.direction.transformDirection(e),this}equals(e){return e.origin.equals(this.origin)&&e.direction.equals(this.direction)}clone(){return new this.constructor().copy(this)}},Le=class s{constructor(e,t,n,i,r,o,a,c,l,u,h,f,p,g,v,m){s.prototype.isMatrix4=!0,this.elements=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],e!==void 0&&this.set(e,t,n,i,r,o,a,c,l,u,h,f,p,g,v,m)}set(e,t,n,i,r,o,a,c,l,u,h,f,p,g,v,m){let d=this.elements;return d[0]=e,d[4]=t,d[8]=n,d[12]=i,d[1]=r,d[5]=o,d[9]=a,d[13]=c,d[2]=l,d[6]=u,d[10]=h,d[14]=f,d[3]=p,d[7]=g,d[11]=v,d[15]=m,this}identity(){return this.set(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),this}clone(){return new s().fromArray(this.elements)}copy(e){let t=this.elements,n=e.elements;return t[0]=n[0],t[1]=n[1],t[2]=n[2],t[3]=n[3],t[4]=n[4],t[5]=n[5],t[6]=n[6],t[7]=n[7],t[8]=n[8],t[9]=n[9],t[10]=n[10],t[11]=n[11],t[12]=n[12],t[13]=n[13],t[14]=n[14],t[15]=n[15],this}copyPosition(e){let t=this.elements,n=e.elements;return t[12]=n[12],t[13]=n[13],t[14]=n[14],this}setFromMatrix3(e){let t=e.elements;return this.set(t[0],t[3],t[6],0,t[1],t[4],t[7],0,t[2],t[5],t[8],0,0,0,0,1),this}extractBasis(e,t,n){return e.setFromMatrixColumn(this,0),t.setFromMatrixColumn(this,1),n.setFromMatrixColumn(this,2),this}makeBasis(e,t,n){return this.set(e.x,t.x,n.x,0,e.y,t.y,n.y,0,e.z,t.z,n.z,0,0,0,0,1),this}extractRotation(e){let t=this.elements,n=e.elements,i=1/Hi.setFromMatrixColumn(e,0).length(),r=1/Hi.setFromMatrixColumn(e,1).length(),o=1/Hi.setFromMatrixColumn(e,2).length();return t[0]=n[0]*i,t[1]=n[1]*i,t[2]=n[2]*i,t[3]=0,t[4]=n[4]*r,t[5]=n[5]*r,t[6]=n[6]*r,t[7]=0,t[8]=n[8]*o,t[9]=n[9]*o,t[10]=n[10]*o,t[11]=0,t[12]=0,t[13]=0,t[14]=0,t[15]=1,this}makeRotationFromEuler(e){let t=this.elements,n=e.x,i=e.y,r=e.z,o=Math.cos(n),a=Math.sin(n),c=Math.cos(i),l=Math.sin(i),u=Math.cos(r),h=Math.sin(r);if(e.order==="XYZ"){let f=o*u,p=o*h,g=a*u,v=a*h;t[0]=c*u,t[4]=-c*h,t[8]=l,t[1]=p+g*l,t[5]=f-v*l,t[9]=-a*c,t[2]=v-f*l,t[6]=g+p*l,t[10]=o*c}else if(e.order==="YXZ"){let f=c*u,p=c*h,g=l*u,v=l*h;t[0]=f+v*a,t[4]=g*a-p,t[8]=o*l,t[1]=o*h,t[5]=o*u,t[9]=-a,t[2]=p*a-g,t[6]=v+f*a,t[10]=o*c}else if(e.order==="ZXY"){let f=c*u,p=c*h,g=l*u,v=l*h;t[0]=f-v*a,t[4]=-o*h,t[8]=g+p*a,t[1]=p+g*a,t[5]=o*u,t[9]=v-f*a,t[2]=-o*l,t[6]=a,t[10]=o*c}else if(e.order==="ZYX"){let f=o*u,p=o*h,g=a*u,v=a*h;t[0]=c*u,t[4]=g*l-p,t[8]=f*l+v,t[1]=c*h,t[5]=v*l+f,t[9]=p*l-g,t[2]=-l,t[6]=a*c,t[10]=o*c}else if(e.order==="YZX"){let f=o*c,p=o*l,g=a*c,v=a*l;t[0]=c*u,t[4]=v-f*h,t[8]=g*h+p,t[1]=h,t[5]=o*u,t[9]=-a*u,t[2]=-l*u,t[6]=p*h+g,t[10]=f-v*h}else if(e.order==="XZY"){let f=o*c,p=o*l,g=a*c,v=a*l;t[0]=c*u,t[4]=-h,t[8]=l*u,t[1]=f*h+v,t[5]=o*u,t[9]=p*h-g,t[2]=g*h-p,t[6]=a*u,t[10]=v*h+f}return t[3]=0,t[7]=0,t[11]=0,t[12]=0,t[13]=0,t[14]=0,t[15]=1,this}makeRotationFromQuaternion(e){return this.compose(nd,e,id)}lookAt(e,t,n){let i=this.elements;return nn.subVectors(e,t),nn.lengthSq()===0&&(nn.z=1),nn.normalize(),ri.crossVectors(n,nn),ri.lengthSq()===0&&(Math.abs(n.z)===1?nn.x+=1e-4:nn.z+=1e-4,nn.normalize(),ri.crossVectors(n,nn)),ri.normalize(),_r.crossVectors(nn,ri),i[0]=ri.x,i[4]=_r.x,i[8]=nn.x,i[1]=ri.y,i[5]=_r.y,i[9]=nn.y,i[2]=ri.z,i[6]=_r.z,i[10]=nn.z,this}multiply(e){return this.multiplyMatrices(this,e)}premultiply(e){return this.multiplyMatrices(e,this)}multiplyMatrices(e,t){let n=e.elements,i=t.elements,r=this.elements,o=n[0],a=n[4],c=n[8],l=n[12],u=n[1],h=n[5],f=n[9],p=n[13],g=n[2],v=n[6],m=n[10],d=n[14],M=n[3],b=n[7],_=n[11],C=n[15],A=i[0],E=i[4],I=i[8],x=i[12],y=i[1],T=i[5],L=i[9],D=i[13],F=i[2],X=i[6],z=i[10],K=i[14],H=i[3],k=i[7],$=i[11],ie=i[15];return r[0]=o*A+a*y+c*F+l*H,r[4]=o*E+a*T+c*X+l*k,r[8]=o*I+a*L+c*z+l*$,r[12]=o*x+a*D+c*K+l*ie,r[1]=u*A+h*y+f*F+p*H,r[5]=u*E+h*T+f*X+p*k,r[9]=u*I+h*L+f*z+p*$,r[13]=u*x+h*D+f*K+p*ie,r[2]=g*A+v*y+m*F+d*H,r[6]=g*E+v*T+m*X+d*k,r[10]=g*I+v*L+m*z+d*$,r[14]=g*x+v*D+m*K+d*ie,r[3]=M*A+b*y+_*F+C*H,r[7]=M*E+b*T+_*X+C*k,r[11]=M*I+b*L+_*z+C*$,r[15]=M*x+b*D+_*K+C*ie,this}multiplyScalar(e){let t=this.elements;return t[0]*=e,t[4]*=e,t[8]*=e,t[12]*=e,t[1]*=e,t[5]*=e,t[9]*=e,t[13]*=e,t[2]*=e,t[6]*=e,t[10]*=e,t[14]*=e,t[3]*=e,t[7]*=e,t[11]*=e,t[15]*=e,this}determinant(){let e=this.elements,t=e[0],n=e[4],i=e[8],r=e[12],o=e[1],a=e[5],c=e[9],l=e[13],u=e[2],h=e[6],f=e[10],p=e[14],g=e[3],v=e[7],m=e[11],d=e[15];return g*(+r*c*h-i*l*h-r*a*f+n*l*f+i*a*p-n*c*p)+v*(+t*c*p-t*l*f+r*o*f-i*o*p+i*l*u-r*c*u)+m*(+t*l*h-t*a*p-r*o*h+n*o*p+r*a*u-n*l*u)+d*(-i*a*u-t*c*h+t*a*f+i*o*h-n*o*f+n*c*u)}transpose(){let e=this.elements,t;return t=e[1],e[1]=e[4],e[4]=t,t=e[2],e[2]=e[8],e[8]=t,t=e[6],e[6]=e[9],e[9]=t,t=e[3],e[3]=e[12],e[12]=t,t=e[7],e[7]=e[13],e[13]=t,t=e[11],e[11]=e[14],e[14]=t,this}setPosition(e,t,n){let i=this.elements;return e.isVector3?(i[12]=e.x,i[13]=e.y,i[14]=e.z):(i[12]=e,i[13]=t,i[14]=n),this}invert(){let e=this.elements,t=e[0],n=e[1],i=e[2],r=e[3],o=e[4],a=e[5],c=e[6],l=e[7],u=e[8],h=e[9],f=e[10],p=e[11],g=e[12],v=e[13],m=e[14],d=e[15],M=h*m*l-v*f*l+v*c*p-a*m*p-h*c*d+a*f*d,b=g*f*l-u*m*l-g*c*p+o*m*p+u*c*d-o*f*d,_=u*v*l-g*h*l+g*a*p-o*v*p-u*a*d+o*h*d,C=g*h*c-u*v*c-g*a*f+o*v*f+u*a*m-o*h*m,A=t*M+n*b+i*_+r*C;if(A===0)return this.set(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);let E=1/A;return e[0]=M*E,e[1]=(v*f*r-h*m*r-v*i*p+n*m*p+h*i*d-n*f*d)*E,e[2]=(a*m*r-v*c*r+v*i*l-n*m*l-a*i*d+n*c*d)*E,e[3]=(h*c*r-a*f*r-h*i*l+n*f*l+a*i*p-n*c*p)*E,e[4]=b*E,e[5]=(u*m*r-g*f*r+g*i*p-t*m*p-u*i*d+t*f*d)*E,e[6]=(g*c*r-o*m*r-g*i*l+t*m*l+o*i*d-t*c*d)*E,e[7]=(o*f*r-u*c*r+u*i*l-t*f*l-o*i*p+t*c*p)*E,e[8]=_*E,e[9]=(g*h*r-u*v*r-g*n*p+t*v*p+u*n*d-t*h*d)*E,e[10]=(o*v*r-g*a*r+g*n*l-t*v*l-o*n*d+t*a*d)*E,e[11]=(u*a*r-o*h*r-u*n*l+t*h*l+o*n*p-t*a*p)*E,e[12]=C*E,e[13]=(u*v*i-g*h*i+g*n*f-t*v*f-u*n*m+t*h*m)*E,e[14]=(g*a*i-o*v*i-g*n*c+t*v*c+o*n*m-t*a*m)*E,e[15]=(o*h*i-u*a*i+u*n*c-t*h*c-o*n*f+t*a*f)*E,this}scale(e){let t=this.elements,n=e.x,i=e.y,r=e.z;return t[0]*=n,t[4]*=i,t[8]*=r,t[1]*=n,t[5]*=i,t[9]*=r,t[2]*=n,t[6]*=i,t[10]*=r,t[3]*=n,t[7]*=i,t[11]*=r,this}getMaxScaleOnAxis(){let e=this.elements,t=e[0]*e[0]+e[1]*e[1]+e[2]*e[2],n=e[4]*e[4]+e[5]*e[5]+e[6]*e[6],i=e[8]*e[8]+e[9]*e[9]+e[10]*e[10];return Math.sqrt(Math.max(t,n,i))}makeTranslation(e,t,n){return e.isVector3?this.set(1,0,0,e.x,0,1,0,e.y,0,0,1,e.z,0,0,0,1):this.set(1,0,0,e,0,1,0,t,0,0,1,n,0,0,0,1),this}makeRotationX(e){let t=Math.cos(e),n=Math.sin(e);return this.set(1,0,0,0,0,t,-n,0,0,n,t,0,0,0,0,1),this}makeRotationY(e){let t=Math.cos(e),n=Math.sin(e);return this.set(t,0,n,0,0,1,0,0,-n,0,t,0,0,0,0,1),this}makeRotationZ(e){let t=Math.cos(e),n=Math.sin(e);return this.set(t,-n,0,0,n,t,0,0,0,0,1,0,0,0,0,1),this}makeRotationAxis(e,t){let n=Math.cos(t),i=Math.sin(t),r=1-n,o=e.x,a=e.y,c=e.z,l=r*o,u=r*a;return this.set(l*o+n,l*a-i*c,l*c+i*a,0,l*a+i*c,u*a+n,u*c-i*o,0,l*c-i*a,u*c+i*o,r*c*c+n,0,0,0,0,1),this}makeScale(e,t,n){return this.set(e,0,0,0,0,t,0,0,0,0,n,0,0,0,0,1),this}makeShear(e,t,n,i,r,o){return this.set(1,n,r,0,e,1,o,0,t,i,1,0,0,0,0,1),this}compose(e,t,n){let i=this.elements,r=t._x,o=t._y,a=t._z,c=t._w,l=r+r,u=o+o,h=a+a,f=r*l,p=r*u,g=r*h,v=o*u,m=o*h,d=a*h,M=c*l,b=c*u,_=c*h,C=n.x,A=n.y,E=n.z;return i[0]=(1-(v+d))*C,i[1]=(p+_)*C,i[2]=(g-b)*C,i[3]=0,i[4]=(p-_)*A,i[5]=(1-(f+d))*A,i[6]=(m+M)*A,i[7]=0,i[8]=(g+b)*E,i[9]=(m-M)*E,i[10]=(1-(f+v))*E,i[11]=0,i[12]=e.x,i[13]=e.y,i[14]=e.z,i[15]=1,this}decompose(e,t,n){let i=this.elements,r=Hi.set(i[0],i[1],i[2]).length(),o=Hi.set(i[4],i[5],i[6]).length(),a=Hi.set(i[8],i[9],i[10]).length();this.determinant()<0&&(r=-r),e.x=i[12],e.y=i[13],e.z=i[14],Mn.copy(this);let l=1/r,u=1/o,h=1/a;return Mn.elements[0]*=l,Mn.elements[1]*=l,Mn.elements[2]*=l,Mn.elements[4]*=u,Mn.elements[5]*=u,Mn.elements[6]*=u,Mn.elements[8]*=h,Mn.elements[9]*=h,Mn.elements[10]*=h,t.setFromRotationMatrix(Mn),n.x=r,n.y=o,n.z=a,this}makePerspective(e,t,n,i,r,o,a=Wn){let c=this.elements,l=2*r/(t-e),u=2*r/(n-i),h=(t+e)/(t-e),f=(n+i)/(n-i),p,g;if(a===Wn)p=-(o+r)/(o-r),g=-2*o*r/(o-r);else if(a===qr)p=-o/(o-r),g=-o*r/(o-r);else throw new Error("THREE.Matrix4.makePerspective(): Invalid coordinate system: "+a);return c[0]=l,c[4]=0,c[8]=h,c[12]=0,c[1]=0,c[5]=u,c[9]=f,c[13]=0,c[2]=0,c[6]=0,c[10]=p,c[14]=g,c[3]=0,c[7]=0,c[11]=-1,c[15]=0,this}makeOrthographic(e,t,n,i,r,o,a=Wn){let c=this.elements,l=1/(t-e),u=1/(n-i),h=1/(o-r),f=(t+e)*l,p=(n+i)*u,g,v;if(a===Wn)g=(o+r)*h,v=-2*h;else if(a===qr)g=r*h,v=-1*h;else throw new Error("THREE.Matrix4.makeOrthographic(): Invalid coordinate system: "+a);return c[0]=2*l,c[4]=0,c[8]=0,c[12]=-f,c[1]=0,c[5]=2*u,c[9]=0,c[13]=-p,c[2]=0,c[6]=0,c[10]=v,c[14]=-g,c[3]=0,c[7]=0,c[11]=0,c[15]=1,this}equals(e){let t=this.elements,n=e.elements;for(let i=0;i<16;i++)if(t[i]!==n[i])return!1;return!0}fromArray(e,t=0){for(let n=0;n<16;n++)this.elements[n]=e[n+t];return this}toArray(e=[],t=0){let n=this.elements;return e[t]=n[0],e[t+1]=n[1],e[t+2]=n[2],e[t+3]=n[3],e[t+4]=n[4],e[t+5]=n[5],e[t+6]=n[6],e[t+7]=n[7],e[t+8]=n[8],e[t+9]=n[9],e[t+10]=n[10],e[t+11]=n[11],e[t+12]=n[12],e[t+13]=n[13],e[t+14]=n[14],e[t+15]=n[15],e}},Hi=new P,Mn=new Le,nd=new P(0,0,0),id=new P(1,1,1),ri=new P,_r=new P,nn=new P,ql=new Le,Yl=new rn,pn=class s{constructor(e=0,t=0,n=0,i=s.DEFAULT_ORDER){this.isEuler=!0,this._x=e,this._y=t,this._z=n,this._order=i}get x(){return this._x}set x(e){this._x=e,this._onChangeCallback()}get y(){return this._y}set y(e){this._y=e,this._onChangeCallback()}get z(){return this._z}set z(e){this._z=e,this._onChangeCallback()}get order(){return this._order}set order(e){this._order=e,this._onChangeCallback()}set(e,t,n,i=this._order){return this._x=e,this._y=t,this._z=n,this._order=i,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._order)}copy(e){return this._x=e._x,this._y=e._y,this._z=e._z,this._order=e._order,this._onChangeCallback(),this}setFromRotationMatrix(e,t=this._order,n=!0){let i=e.elements,r=i[0],o=i[4],a=i[8],c=i[1],l=i[5],u=i[9],h=i[2],f=i[6],p=i[10];switch(t){case"XYZ":this._y=Math.asin(kt(a,-1,1)),Math.abs(a)<.9999999?(this._x=Math.atan2(-u,p),this._z=Math.atan2(-o,r)):(this._x=Math.atan2(f,l),this._z=0);break;case"YXZ":this._x=Math.asin(-kt(u,-1,1)),Math.abs(u)<.9999999?(this._y=Math.atan2(a,p),this._z=Math.atan2(c,l)):(this._y=Math.atan2(-h,r),this._z=0);break;case"ZXY":this._x=Math.asin(kt(f,-1,1)),Math.abs(f)<.9999999?(this._y=Math.atan2(-h,p),this._z=Math.atan2(-o,l)):(this._y=0,this._z=Math.atan2(c,r));break;case"ZYX":this._y=Math.asin(-kt(h,-1,1)),Math.abs(h)<.9999999?(this._x=Math.atan2(f,p),this._z=Math.atan2(c,r)):(this._x=0,this._z=Math.atan2(-o,l));break;case"YZX":this._z=Math.asin(kt(c,-1,1)),Math.abs(c)<.9999999?(this._x=Math.atan2(-u,l),this._y=Math.atan2(-h,r)):(this._x=0,this._y=Math.atan2(a,p));break;case"XZY":this._z=Math.asin(-kt(o,-1,1)),Math.abs(o)<.9999999?(this._x=Math.atan2(f,l),this._y=Math.atan2(a,r)):(this._x=Math.atan2(-u,p),this._y=0);break;default:console.warn("THREE.Euler: .setFromRotationMatrix() encountered an unknown order: "+t)}return this._order=t,n===!0&&this._onChangeCallback(),this}setFromQuaternion(e,t,n){return ql.makeRotationFromQuaternion(e),this.setFromRotationMatrix(ql,t,n)}setFromVector3(e,t=this._order){return this.set(e.x,e.y,e.z,t)}reorder(e){return Yl.setFromEuler(this),this.setFromQuaternion(Yl,e)}equals(e){return e._x===this._x&&e._y===this._y&&e._z===this._z&&e._order===this._order}fromArray(e){return this._x=e[0],this._y=e[1],this._z=e[2],e[3]!==void 0&&(this._order=e[3]),this._onChangeCallback(),this}toArray(e=[],t=0){return e[t]=this._x,e[t+1]=this._y,e[t+2]=this._z,e[t+3]=this._order,e}_onChange(e){return this._onChangeCallback=e,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._order}};pn.DEFAULT_ORDER="XYZ";var Zr=class{constructor(){this.mask=1}set(e){this.mask=(1<<e|0)>>>0}enable(e){this.mask|=1<<e|0}enableAll(){this.mask=-1}toggle(e){this.mask^=1<<e|0}disable(e){this.mask&=~(1<<e|0)}disableAll(){this.mask=0}test(e){return(this.mask&e.mask)!==0}isEnabled(e){return(this.mask&(1<<e|0))!==0}},sd=0,$l=new P,Vi=new rn,zn=new Le,yr=new P,Ns=new P,rd=new P,od=new rn,Zl=new P(1,0,0),Kl=new P(0,1,0),Jl=new P(0,0,1),jl={type:"added"},ad={type:"removed"},Gi={type:"childadded",child:null},No={type:"childremoved",child:null},gt=class s extends ui{constructor(){super(),this.isObject3D=!0,Object.defineProperty(this,"id",{value:sd++}),this.uuid=An(),this.name="",this.type="Object3D",this.parent=null,this.children=[],this.up=s.DEFAULT_UP.clone();let e=new P,t=new pn,n=new rn,i=new P(1,1,1);function r(){n.setFromEuler(t,!1)}function o(){t.setFromQuaternion(n,void 0,!1)}t._onChange(r),n._onChange(o),Object.defineProperties(this,{position:{configurable:!0,enumerable:!0,value:e},rotation:{configurable:!0,enumerable:!0,value:t},quaternion:{configurable:!0,enumerable:!0,value:n},scale:{configurable:!0,enumerable:!0,value:i},modelViewMatrix:{value:new Le},normalMatrix:{value:new ke}}),this.matrix=new Le,this.matrixWorld=new Le,this.matrixAutoUpdate=s.DEFAULT_MATRIX_AUTO_UPDATE,this.matrixWorldAutoUpdate=s.DEFAULT_MATRIX_WORLD_AUTO_UPDATE,this.matrixWorldNeedsUpdate=!1,this.layers=new Zr,this.visible=!0,this.castShadow=!1,this.receiveShadow=!1,this.frustumCulled=!0,this.renderOrder=0,this.animations=[],this.userData={}}onBeforeShadow(){}onAfterShadow(){}onBeforeRender(){}onAfterRender(){}applyMatrix4(e){this.matrixAutoUpdate&&this.updateMatrix(),this.matrix.premultiply(e),this.matrix.decompose(this.position,this.quaternion,this.scale)}applyQuaternion(e){return this.quaternion.premultiply(e),this}setRotationFromAxisAngle(e,t){this.quaternion.setFromAxisAngle(e,t)}setRotationFromEuler(e){this.quaternion.setFromEuler(e,!0)}setRotationFromMatrix(e){this.quaternion.setFromRotationMatrix(e)}setRotationFromQuaternion(e){this.quaternion.copy(e)}rotateOnAxis(e,t){return Vi.setFromAxisAngle(e,t),this.quaternion.multiply(Vi),this}rotateOnWorldAxis(e,t){return Vi.setFromAxisAngle(e,t),this.quaternion.premultiply(Vi),this}rotateX(e){return this.rotateOnAxis(Zl,e)}rotateY(e){return this.rotateOnAxis(Kl,e)}rotateZ(e){return this.rotateOnAxis(Jl,e)}translateOnAxis(e,t){return $l.copy(e).applyQuaternion(this.quaternion),this.position.add($l.multiplyScalar(t)),this}translateX(e){return this.translateOnAxis(Zl,e)}translateY(e){return this.translateOnAxis(Kl,e)}translateZ(e){return this.translateOnAxis(Jl,e)}localToWorld(e){return this.updateWorldMatrix(!0,!1),e.applyMatrix4(this.matrixWorld)}worldToLocal(e){return this.updateWorldMatrix(!0,!1),e.applyMatrix4(zn.copy(this.matrixWorld).invert())}lookAt(e,t,n){e.isVector3?yr.copy(e):yr.set(e,t,n);let i=this.parent;this.updateWorldMatrix(!0,!1),Ns.setFromMatrixPosition(this.matrixWorld),this.isCamera||this.isLight?zn.lookAt(Ns,yr,this.up):zn.lookAt(yr,Ns,this.up),this.quaternion.setFromRotationMatrix(zn),i&&(zn.extractRotation(i.matrixWorld),Vi.setFromRotationMatrix(zn),this.quaternion.premultiply(Vi.invert()))}add(e){if(arguments.length>1){for(let t=0;t<arguments.length;t++)this.add(arguments[t]);return this}return e===this?(console.error("THREE.Object3D.add: object can't be added as a child of itself.",e),this):(e&&e.isObject3D?(e.removeFromParent(),e.parent=this,this.children.push(e),e.dispatchEvent(jl),Gi.child=e,this.dispatchEvent(Gi),Gi.child=null):console.error("THREE.Object3D.add: object not an instance of THREE.Object3D.",e),this)}remove(e){if(arguments.length>1){for(let n=0;n<arguments.length;n++)this.remove(arguments[n]);return this}let t=this.children.indexOf(e);return t!==-1&&(e.parent=null,this.children.splice(t,1),e.dispatchEvent(ad),No.child=e,this.dispatchEvent(No),No.child=null),this}removeFromParent(){let e=this.parent;return e!==null&&e.remove(this),this}clear(){return this.remove(...this.children)}attach(e){return this.updateWorldMatrix(!0,!1),zn.copy(this.matrixWorld).invert(),e.parent!==null&&(e.parent.updateWorldMatrix(!0,!1),zn.multiply(e.parent.matrixWorld)),e.applyMatrix4(zn),e.removeFromParent(),e.parent=this,this.children.push(e),e.updateWorldMatrix(!1,!0),e.dispatchEvent(jl),Gi.child=e,this.dispatchEvent(Gi),Gi.child=null,this}getObjectById(e){return this.getObjectByProperty("id",e)}getObjectByName(e){return this.getObjectByProperty("name",e)}getObjectByProperty(e,t){if(this[e]===t)return this;for(let n=0,i=this.children.length;n<i;n++){let o=this.children[n].getObjectByProperty(e,t);if(o!==void 0)return o}}getObjectsByProperty(e,t,n=[]){this[e]===t&&n.push(this);let i=this.children;for(let r=0,o=i.length;r<o;r++)i[r].getObjectsByProperty(e,t,n);return n}getWorldPosition(e){return this.updateWorldMatrix(!0,!1),e.setFromMatrixPosition(this.matrixWorld)}getWorldQuaternion(e){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(Ns,e,rd),e}getWorldScale(e){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(Ns,od,e),e}getWorldDirection(e){this.updateWorldMatrix(!0,!1);let t=this.matrixWorld.elements;return e.set(t[8],t[9],t[10]).normalize()}raycast(){}traverse(e){e(this);let t=this.children;for(let n=0,i=t.length;n<i;n++)t[n].traverse(e)}traverseVisible(e){if(this.visible===!1)return;e(this);let t=this.children;for(let n=0,i=t.length;n<i;n++)t[n].traverseVisible(e)}traverseAncestors(e){let t=this.parent;t!==null&&(e(t),t.traverseAncestors(e))}updateMatrix(){this.matrix.compose(this.position,this.quaternion,this.scale),this.matrixWorldNeedsUpdate=!0}updateMatrixWorld(e){this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||e)&&(this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),this.matrixWorldNeedsUpdate=!1,e=!0);let t=this.children;for(let n=0,i=t.length;n<i;n++)t[n].updateMatrixWorld(e)}updateWorldMatrix(e,t){let n=this.parent;if(e===!0&&n!==null&&n.updateWorldMatrix(!0,!1),this.matrixAutoUpdate&&this.updateMatrix(),this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),t===!0){let i=this.children;for(let r=0,o=i.length;r<o;r++)i[r].updateWorldMatrix(!1,!0)}}toJSON(e){let t=e===void 0||typeof e=="string",n={};t&&(e={geometries:{},materials:{},textures:{},images:{},shapes:{},skeletons:{},animations:{},nodes:{}},n.metadata={version:4.6,type:"Object",generator:"Object3D.toJSON"});let i={};i.uuid=this.uuid,i.type=this.type,this.name!==""&&(i.name=this.name),this.castShadow===!0&&(i.castShadow=!0),this.receiveShadow===!0&&(i.receiveShadow=!0),this.visible===!1&&(i.visible=!1),this.frustumCulled===!1&&(i.frustumCulled=!1),this.renderOrder!==0&&(i.renderOrder=this.renderOrder),Object.keys(this.userData).length>0&&(i.userData=this.userData),i.layers=this.layers.mask,i.matrix=this.matrix.toArray(),i.up=this.up.toArray(),this.matrixAutoUpdate===!1&&(i.matrixAutoUpdate=!1),this.isInstancedMesh&&(i.type="InstancedMesh",i.count=this.count,i.instanceMatrix=this.instanceMatrix.toJSON(),this.instanceColor!==null&&(i.instanceColor=this.instanceColor.toJSON())),this.isBatchedMesh&&(i.type="BatchedMesh",i.perObjectFrustumCulled=this.perObjectFrustumCulled,i.sortObjects=this.sortObjects,i.drawRanges=this._drawRanges,i.reservedRanges=this._reservedRanges,i.visibility=this._visibility,i.active=this._active,i.bounds=this._bounds.map(a=>({boxInitialized:a.boxInitialized,boxMin:a.box.min.toArray(),boxMax:a.box.max.toArray(),sphereInitialized:a.sphereInitialized,sphereRadius:a.sphere.radius,sphereCenter:a.sphere.center.toArray()})),i.maxInstanceCount=this._maxInstanceCount,i.maxVertexCount=this._maxVertexCount,i.maxIndexCount=this._maxIndexCount,i.geometryInitialized=this._geometryInitialized,i.geometryCount=this._geometryCount,i.matricesTexture=this._matricesTexture.toJSON(e),this._colorsTexture!==null&&(i.colorsTexture=this._colorsTexture.toJSON(e)),this.boundingSphere!==null&&(i.boundingSphere={center:i.boundingSphere.center.toArray(),radius:i.boundingSphere.radius}),this.boundingBox!==null&&(i.boundingBox={min:i.boundingBox.min.toArray(),max:i.boundingBox.max.toArray()}));function r(a,c){return a[c.uuid]===void 0&&(a[c.uuid]=c.toJSON(e)),c.uuid}if(this.isScene)this.background&&(this.background.isColor?i.background=this.background.toJSON():this.background.isTexture&&(i.background=this.background.toJSON(e).uuid)),this.environment&&this.environment.isTexture&&this.environment.isRenderTargetTexture!==!0&&(i.environment=this.environment.toJSON(e).uuid);else if(this.isMesh||this.isLine||this.isPoints){i.geometry=r(e.geometries,this.geometry);let a=this.geometry.parameters;if(a!==void 0&&a.shapes!==void 0){let c=a.shapes;if(Array.isArray(c))for(let l=0,u=c.length;l<u;l++){let h=c[l];r(e.shapes,h)}else r(e.shapes,c)}}if(this.isSkinnedMesh&&(i.bindMode=this.bindMode,i.bindMatrix=this.bindMatrix.toArray(),this.skeleton!==void 0&&(r(e.skeletons,this.skeleton),i.skeleton=this.skeleton.uuid)),this.material!==void 0)if(Array.isArray(this.material)){let a=[];for(let c=0,l=this.material.length;c<l;c++)a.push(r(e.materials,this.material[c]));i.material=a}else i.material=r(e.materials,this.material);if(this.children.length>0){i.children=[];for(let a=0;a<this.children.length;a++)i.children.push(this.children[a].toJSON(e).object)}if(this.animations.length>0){i.animations=[];for(let a=0;a<this.animations.length;a++){let c=this.animations[a];i.animations.push(r(e.animations,c))}}if(t){let a=o(e.geometries),c=o(e.materials),l=o(e.textures),u=o(e.images),h=o(e.shapes),f=o(e.skeletons),p=o(e.animations),g=o(e.nodes);a.length>0&&(n.geometries=a),c.length>0&&(n.materials=c),l.length>0&&(n.textures=l),u.length>0&&(n.images=u),h.length>0&&(n.shapes=h),f.length>0&&(n.skeletons=f),p.length>0&&(n.animations=p),g.length>0&&(n.nodes=g)}return n.object=i,n;function o(a){let c=[];for(let l in a){let u=a[l];delete u.metadata,c.push(u)}return c}}clone(e){return new this.constructor().copy(this,e)}copy(e,t=!0){if(this.name=e.name,this.up.copy(e.up),this.position.copy(e.position),this.rotation.order=e.rotation.order,this.quaternion.copy(e.quaternion),this.scale.copy(e.scale),this.matrix.copy(e.matrix),this.matrixWorld.copy(e.matrixWorld),this.matrixAutoUpdate=e.matrixAutoUpdate,this.matrixWorldAutoUpdate=e.matrixWorldAutoUpdate,this.matrixWorldNeedsUpdate=e.matrixWorldNeedsUpdate,this.layers.mask=e.layers.mask,this.visible=e.visible,this.castShadow=e.castShadow,this.receiveShadow=e.receiveShadow,this.frustumCulled=e.frustumCulled,this.renderOrder=e.renderOrder,this.animations=e.animations.slice(),this.userData=JSON.parse(JSON.stringify(e.userData)),t===!0)for(let n=0;n<e.children.length;n++){let i=e.children[n];this.add(i.clone())}return this}};gt.DEFAULT_UP=new P(0,1,0);gt.DEFAULT_MATRIX_AUTO_UPDATE=!0;gt.DEFAULT_MATRIX_WORLD_AUTO_UPDATE=!0;var bn=new P,kn=new P,Fo=new P,Hn=new P,Wi=new P,Xi=new P,Ql=new P,Oo=new P,Bo=new P,zo=new P,ko=new We,Ho=new We,Vo=new We,Pi=class s{constructor(e=new P,t=new P,n=new P){this.a=e,this.b=t,this.c=n}static getNormal(e,t,n,i){i.subVectors(n,t),bn.subVectors(e,t),i.cross(bn);let r=i.lengthSq();return r>0?i.multiplyScalar(1/Math.sqrt(r)):i.set(0,0,0)}static getBarycoord(e,t,n,i,r){bn.subVectors(i,t),kn.subVectors(n,t),Fo.subVectors(e,t);let o=bn.dot(bn),a=bn.dot(kn),c=bn.dot(Fo),l=kn.dot(kn),u=kn.dot(Fo),h=o*l-a*a;if(h===0)return r.set(0,0,0),null;let f=1/h,p=(l*c-a*u)*f,g=(o*u-a*c)*f;return r.set(1-p-g,g,p)}static containsPoint(e,t,n,i){return this.getBarycoord(e,t,n,i,Hn)===null?!1:Hn.x>=0&&Hn.y>=0&&Hn.x+Hn.y<=1}static getInterpolation(e,t,n,i,r,o,a,c){return this.getBarycoord(e,t,n,i,Hn)===null?(c.x=0,c.y=0,"z"in c&&(c.z=0),"w"in c&&(c.w=0),null):(c.setScalar(0),c.addScaledVector(r,Hn.x),c.addScaledVector(o,Hn.y),c.addScaledVector(a,Hn.z),c)}static getInterpolatedAttribute(e,t,n,i,r,o){return ko.setScalar(0),Ho.setScalar(0),Vo.setScalar(0),ko.fromBufferAttribute(e,t),Ho.fromBufferAttribute(e,n),Vo.fromBufferAttribute(e,i),o.setScalar(0),o.addScaledVector(ko,r.x),o.addScaledVector(Ho,r.y),o.addScaledVector(Vo,r.z),o}static isFrontFacing(e,t,n,i){return bn.subVectors(n,t),kn.subVectors(e,t),bn.cross(kn).dot(i)<0}set(e,t,n){return this.a.copy(e),this.b.copy(t),this.c.copy(n),this}setFromPointsAndIndices(e,t,n,i){return this.a.copy(e[t]),this.b.copy(e[n]),this.c.copy(e[i]),this}setFromAttributeAndIndices(e,t,n,i){return this.a.fromBufferAttribute(e,t),this.b.fromBufferAttribute(e,n),this.c.fromBufferAttribute(e,i),this}clone(){return new this.constructor().copy(this)}copy(e){return this.a.copy(e.a),this.b.copy(e.b),this.c.copy(e.c),this}getArea(){return bn.subVectors(this.c,this.b),kn.subVectors(this.a,this.b),bn.cross(kn).length()*.5}getMidpoint(e){return e.addVectors(this.a,this.b).add(this.c).multiplyScalar(1/3)}getNormal(e){return s.getNormal(this.a,this.b,this.c,e)}getPlane(e){return e.setFromCoplanarPoints(this.a,this.b,this.c)}getBarycoord(e,t){return s.getBarycoord(e,this.a,this.b,this.c,t)}getInterpolation(e,t,n,i,r){return s.getInterpolation(e,this.a,this.b,this.c,t,n,i,r)}containsPoint(e){return s.containsPoint(e,this.a,this.b,this.c)}isFrontFacing(e){return s.isFrontFacing(this.a,this.b,this.c,e)}intersectsBox(e){return e.intersectsTriangle(this)}closestPointToPoint(e,t){let n=this.a,i=this.b,r=this.c,o,a;Wi.subVectors(i,n),Xi.subVectors(r,n),Oo.subVectors(e,n);let c=Wi.dot(Oo),l=Xi.dot(Oo);if(c<=0&&l<=0)return t.copy(n);Bo.subVectors(e,i);let u=Wi.dot(Bo),h=Xi.dot(Bo);if(u>=0&&h<=u)return t.copy(i);let f=c*h-u*l;if(f<=0&&c>=0&&u<=0)return o=c/(c-u),t.copy(n).addScaledVector(Wi,o);zo.subVectors(e,r);let p=Wi.dot(zo),g=Xi.dot(zo);if(g>=0&&p<=g)return t.copy(r);let v=p*l-c*g;if(v<=0&&l>=0&&g<=0)return a=l/(l-g),t.copy(n).addScaledVector(Xi,a);let m=u*g-p*h;if(m<=0&&h-u>=0&&p-g>=0)return Ql.subVectors(r,i),a=(h-u)/(h-u+(p-g)),t.copy(i).addScaledVector(Ql,a);let d=1/(m+v+f);return o=v*d,a=f*d,t.copy(n).addScaledVector(Wi,o).addScaledVector(Xi,a)}equals(e){return e.a.equals(this.a)&&e.b.equals(this.b)&&e.c.equals(this.c)}},lh={aliceblue:15792383,antiquewhite:16444375,aqua:65535,aquamarine:8388564,azure:15794175,beige:16119260,bisque:16770244,black:0,blanchedalmond:16772045,blue:255,blueviolet:9055202,brown:10824234,burlywood:14596231,cadetblue:6266528,chartreuse:8388352,chocolate:13789470,coral:16744272,cornflowerblue:6591981,cornsilk:16775388,crimson:14423100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:12092939,darkgray:11119017,darkgreen:25600,darkgrey:11119017,darkkhaki:12433259,darkmagenta:9109643,darkolivegreen:5597999,darkorange:16747520,darkorchid:10040012,darkred:9109504,darksalmon:15308410,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:11674146,floralwhite:16775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14474460,ghostwhite:16316671,gold:16766720,goldenrod:14329120,gray:8421504,green:32768,greenyellow:11403055,grey:8421504,honeydew:15794160,hotpink:16738740,indianred:13458524,indigo:4915330,ivory:16777200,khaki:15787660,lavender:15132410,lavenderblush:16773365,lawngreen:8190976,lemonchiffon:16775885,lightblue:11393254,lightcoral:15761536,lightcyan:14745599,lightgoldenrodyellow:16448210,lightgray:13882323,lightgreen:9498256,lightgrey:13882323,lightpink:16758465,lightsalmon:16752762,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:11584734,lightyellow:16777184,lime:65280,limegreen:3329330,linen:16445670,magenta:16711935,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:12211667,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:13047173,midnightblue:1644912,mintcream:16121850,mistyrose:16770273,moccasin:16770229,navajowhite:16768685,navy:128,oldlace:16643558,olive:8421376,olivedrab:7048739,orange:16753920,orangered:16729344,orchid:14315734,palegoldenrod:15657130,palegreen:10025880,paleturquoise:11529966,palevioletred:14381203,papayawhip:16773077,peachpuff:16767673,peru:13468991,pink:16761035,plum:14524637,powderblue:11591910,purple:8388736,rebeccapurple:6697881,red:16711680,rosybrown:12357519,royalblue:4286945,saddlebrown:9127187,salmon:16416882,sandybrown:16032864,seagreen:3050327,seashell:16774638,sienna:10506797,silver:12632256,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:16775930,springgreen:65407,steelblue:4620980,tan:13808780,teal:32896,thistle:14204888,tomato:16737095,turquoise:4251856,violet:15631086,wheat:16113331,white:16777215,whitesmoke:16119285,yellow:16776960,yellowgreen:10145074},oi={h:0,s:0,l:0},Mr={h:0,s:0,l:0};function Go(s,e,t){return t<0&&(t+=1),t>1&&(t-=1),t<1/6?s+(e-s)*6*t:t<1/2?e:t<2/3?s+(e-s)*6*(2/3-t):s}var ve=class{constructor(e,t,n){return this.isColor=!0,this.r=1,this.g=1,this.b=1,this.set(e,t,n)}set(e,t,n){if(t===void 0&&n===void 0){let i=e;i&&i.isColor?this.copy(i):typeof i=="number"?this.setHex(i):typeof i=="string"&&this.setStyle(i)}else this.setRGB(e,t,n);return this}setScalar(e){return this.r=e,this.g=e,this.b=e,this}setHex(e,t=St){return e=Math.floor(e),this.r=(e>>16&255)/255,this.g=(e>>8&255)/255,this.b=(e&255)/255,Ye.toWorkingColorSpace(this,t),this}setRGB(e,t,n,i=Ye.workingColorSpace){return this.r=e,this.g=t,this.b=n,Ye.toWorkingColorSpace(this,i),this}setHSL(e,t,n,i=Ye.workingColorSpace){if(e=Tc(e,1),t=kt(t,0,1),n=kt(n,0,1),t===0)this.r=this.g=this.b=n;else{let r=n<=.5?n*(1+t):n+t-n*t,o=2*n-r;this.r=Go(o,r,e+1/3),this.g=Go(o,r,e),this.b=Go(o,r,e-1/3)}return Ye.toWorkingColorSpace(this,i),this}setStyle(e,t=St){function n(r){r!==void 0&&parseFloat(r)<1&&console.warn("THREE.Color: Alpha component of "+e+" will be ignored.")}let i;if(i=/^(\w+)\(([^\)]*)\)/.exec(e)){let r,o=i[1],a=i[2];switch(o){case"rgb":case"rgba":if(r=/^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(a))return n(r[4]),this.setRGB(Math.min(255,parseInt(r[1],10))/255,Math.min(255,parseInt(r[2],10))/255,Math.min(255,parseInt(r[3],10))/255,t);if(r=/^\s*(\d+)\%\s*,\s*(\d+)\%\s*,\s*(\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(a))return n(r[4]),this.setRGB(Math.min(100,parseInt(r[1],10))/100,Math.min(100,parseInt(r[2],10))/100,Math.min(100,parseInt(r[3],10))/100,t);break;case"hsl":case"hsla":if(r=/^\s*(\d*\.?\d+)\s*,\s*(\d*\.?\d+)\%\s*,\s*(\d*\.?\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(a))return n(r[4]),this.setHSL(parseFloat(r[1])/360,parseFloat(r[2])/100,parseFloat(r[3])/100,t);break;default:console.warn("THREE.Color: Unknown color model "+e)}}else if(i=/^\#([A-Fa-f\d]+)$/.exec(e)){let r=i[1],o=r.length;if(o===3)return this.setRGB(parseInt(r.charAt(0),16)/15,parseInt(r.charAt(1),16)/15,parseInt(r.charAt(2),16)/15,t);if(o===6)return this.setHex(parseInt(r,16),t);console.warn("THREE.Color: Invalid hex color "+e)}else if(e&&e.length>0)return this.setColorName(e,t);return this}setColorName(e,t=St){let n=lh[e.toLowerCase()];return n!==void 0?this.setHex(n,t):console.warn("THREE.Color: Unknown color "+e),this}clone(){return new this.constructor(this.r,this.g,this.b)}copy(e){return this.r=e.r,this.g=e.g,this.b=e.b,this}copySRGBToLinear(e){return this.r=Xn(e.r),this.g=Xn(e.g),this.b=Xn(e.b),this}copyLinearToSRGB(e){return this.r=ts(e.r),this.g=ts(e.g),this.b=ts(e.b),this}convertSRGBToLinear(){return this.copySRGBToLinear(this),this}convertLinearToSRGB(){return this.copyLinearToSRGB(this),this}getHex(e=St){return Ye.fromWorkingColorSpace(zt.copy(this),e),Math.round(kt(zt.r*255,0,255))*65536+Math.round(kt(zt.g*255,0,255))*256+Math.round(kt(zt.b*255,0,255))}getHexString(e=St){return("000000"+this.getHex(e).toString(16)).slice(-6)}getHSL(e,t=Ye.workingColorSpace){Ye.fromWorkingColorSpace(zt.copy(this),t);let n=zt.r,i=zt.g,r=zt.b,o=Math.max(n,i,r),a=Math.min(n,i,r),c,l,u=(a+o)/2;if(a===o)c=0,l=0;else{let h=o-a;switch(l=u<=.5?h/(o+a):h/(2-o-a),o){case n:c=(i-r)/h+(i<r?6:0);break;case i:c=(r-n)/h+2;break;case r:c=(n-i)/h+4;break}c/=6}return e.h=c,e.s=l,e.l=u,e}getRGB(e,t=Ye.workingColorSpace){return Ye.fromWorkingColorSpace(zt.copy(this),t),e.r=zt.r,e.g=zt.g,e.b=zt.b,e}getStyle(e=St){Ye.fromWorkingColorSpace(zt.copy(this),e);let t=zt.r,n=zt.g,i=zt.b;return e!==St?`color(${e} ${t.toFixed(3)} ${n.toFixed(3)} ${i.toFixed(3)})`:`rgb(${Math.round(t*255)},${Math.round(n*255)},${Math.round(i*255)})`}offsetHSL(e,t,n){return this.getHSL(oi),this.setHSL(oi.h+e,oi.s+t,oi.l+n)}add(e){return this.r+=e.r,this.g+=e.g,this.b+=e.b,this}addColors(e,t){return this.r=e.r+t.r,this.g=e.g+t.g,this.b=e.b+t.b,this}addScalar(e){return this.r+=e,this.g+=e,this.b+=e,this}sub(e){return this.r=Math.max(0,this.r-e.r),this.g=Math.max(0,this.g-e.g),this.b=Math.max(0,this.b-e.b),this}multiply(e){return this.r*=e.r,this.g*=e.g,this.b*=e.b,this}multiplyScalar(e){return this.r*=e,this.g*=e,this.b*=e,this}lerp(e,t){return this.r+=(e.r-this.r)*t,this.g+=(e.g-this.g)*t,this.b+=(e.b-this.b)*t,this}lerpColors(e,t,n){return this.r=e.r+(t.r-e.r)*n,this.g=e.g+(t.g-e.g)*n,this.b=e.b+(t.b-e.b)*n,this}lerpHSL(e,t){this.getHSL(oi),e.getHSL(Mr);let n=Xs(oi.h,Mr.h,t),i=Xs(oi.s,Mr.s,t),r=Xs(oi.l,Mr.l,t);return this.setHSL(n,i,r),this}setFromVector3(e){return this.r=e.x,this.g=e.y,this.b=e.z,this}applyMatrix3(e){let t=this.r,n=this.g,i=this.b,r=e.elements;return this.r=r[0]*t+r[3]*n+r[6]*i,this.g=r[1]*t+r[4]*n+r[7]*i,this.b=r[2]*t+r[5]*n+r[8]*i,this}equals(e){return e.r===this.r&&e.g===this.g&&e.b===this.b}fromArray(e,t=0){return this.r=e[t],this.g=e[t+1],this.b=e[t+2],this}toArray(e=[],t=0){return e[t]=this.r,e[t+1]=this.g,e[t+2]=this.b,e}fromBufferAttribute(e,t){return this.r=e.getX(t),this.g=e.getY(t),this.b=e.getZ(t),this}toJSON(){return this.getHex()}*[Symbol.iterator](){yield this.r,yield this.g,yield this.b}},zt=new ve;ve.NAMES=lh;var cd=0,an=class extends ui{static get type(){return"Material"}get type(){return this.constructor.type}set type(e){}constructor(){super(),this.isMaterial=!0,Object.defineProperty(this,"id",{value:cd++}),this.uuid=An(),this.name="",this.blending=Qi,this.side=en,this.vertexColors=!1,this.opacity=1,this.transparent=!1,this.alphaHash=!1,this.blendSrc=sa,this.blendDst=ra,this.blendEquation=Ii,this.blendSrcAlpha=null,this.blendDstAlpha=null,this.blendEquationAlpha=null,this.blendColor=new ve(0,0,0),this.blendAlpha=0,this.depthFunc=ss,this.depthTest=!0,this.depthWrite=!0,this.stencilWriteMask=255,this.stencilFunc=Fl,this.stencilRef=0,this.stencilFuncMask=255,this.stencilFail=Fi,this.stencilZFail=Fi,this.stencilZPass=Fi,this.stencilWrite=!1,this.clippingPlanes=null,this.clipIntersection=!1,this.clipShadows=!1,this.shadowSide=null,this.colorWrite=!0,this.precision=null,this.polygonOffset=!1,this.polygonOffsetFactor=0,this.polygonOffsetUnits=0,this.dithering=!1,this.alphaToCoverage=!1,this.premultipliedAlpha=!1,this.forceSinglePass=!1,this.visible=!0,this.toneMapped=!0,this.userData={},this.version=0,this._alphaTest=0}get alphaTest(){return this._alphaTest}set alphaTest(e){this._alphaTest>0!=e>0&&this.version++,this._alphaTest=e}onBeforeRender(){}onBeforeCompile(){}customProgramCacheKey(){return this.onBeforeCompile.toString()}setValues(e){if(e!==void 0)for(let t in e){let n=e[t];if(n===void 0){console.warn(`THREE.Material: parameter '${t}' has value of undefined.`);continue}let i=this[t];if(i===void 0){console.warn(`THREE.Material: '${t}' is not a property of THREE.${this.type}.`);continue}i&&i.isColor?i.set(n):i&&i.isVector3&&n&&n.isVector3?i.copy(n):this[t]=n}}toJSON(e){let t=e===void 0||typeof e=="string";t&&(e={textures:{},images:{}});let n={metadata:{version:4.6,type:"Material",generator:"Material.toJSON"}};n.uuid=this.uuid,n.type=this.type,this.name!==""&&(n.name=this.name),this.color&&this.color.isColor&&(n.color=this.color.getHex()),this.roughness!==void 0&&(n.roughness=this.roughness),this.metalness!==void 0&&(n.metalness=this.metalness),this.sheen!==void 0&&(n.sheen=this.sheen),this.sheenColor&&this.sheenColor.isColor&&(n.sheenColor=this.sheenColor.getHex()),this.sheenRoughness!==void 0&&(n.sheenRoughness=this.sheenRoughness),this.emissive&&this.emissive.isColor&&(n.emissive=this.emissive.getHex()),this.emissiveIntensity!==void 0&&this.emissiveIntensity!==1&&(n.emissiveIntensity=this.emissiveIntensity),this.specular&&this.specular.isColor&&(n.specular=this.specular.getHex()),this.specularIntensity!==void 0&&(n.specularIntensity=this.specularIntensity),this.specularColor&&this.specularColor.isColor&&(n.specularColor=this.specularColor.getHex()),this.shininess!==void 0&&(n.shininess=this.shininess),this.clearcoat!==void 0&&(n.clearcoat=this.clearcoat),this.clearcoatRoughness!==void 0&&(n.clearcoatRoughness=this.clearcoatRoughness),this.clearcoatMap&&this.clearcoatMap.isTexture&&(n.clearcoatMap=this.clearcoatMap.toJSON(e).uuid),this.clearcoatRoughnessMap&&this.clearcoatRoughnessMap.isTexture&&(n.clearcoatRoughnessMap=this.clearcoatRoughnessMap.toJSON(e).uuid),this.clearcoatNormalMap&&this.clearcoatNormalMap.isTexture&&(n.clearcoatNormalMap=this.clearcoatNormalMap.toJSON(e).uuid,n.clearcoatNormalScale=this.clearcoatNormalScale.toArray()),this.dispersion!==void 0&&(n.dispersion=this.dispersion),this.iridescence!==void 0&&(n.iridescence=this.iridescence),this.iridescenceIOR!==void 0&&(n.iridescenceIOR=this.iridescenceIOR),this.iridescenceThicknessRange!==void 0&&(n.iridescenceThicknessRange=this.iridescenceThicknessRange),this.iridescenceMap&&this.iridescenceMap.isTexture&&(n.iridescenceMap=this.iridescenceMap.toJSON(e).uuid),this.iridescenceThicknessMap&&this.iridescenceThicknessMap.isTexture&&(n.iridescenceThicknessMap=this.iridescenceThicknessMap.toJSON(e).uuid),this.anisotropy!==void 0&&(n.anisotropy=this.anisotropy),this.anisotropyRotation!==void 0&&(n.anisotropyRotation=this.anisotropyRotation),this.anisotropyMap&&this.anisotropyMap.isTexture&&(n.anisotropyMap=this.anisotropyMap.toJSON(e).uuid),this.map&&this.map.isTexture&&(n.map=this.map.toJSON(e).uuid),this.matcap&&this.matcap.isTexture&&(n.matcap=this.matcap.toJSON(e).uuid),this.alphaMap&&this.alphaMap.isTexture&&(n.alphaMap=this.alphaMap.toJSON(e).uuid),this.lightMap&&this.lightMap.isTexture&&(n.lightMap=this.lightMap.toJSON(e).uuid,n.lightMapIntensity=this.lightMapIntensity),this.aoMap&&this.aoMap.isTexture&&(n.aoMap=this.aoMap.toJSON(e).uuid,n.aoMapIntensity=this.aoMapIntensity),this.bumpMap&&this.bumpMap.isTexture&&(n.bumpMap=this.bumpMap.toJSON(e).uuid,n.bumpScale=this.bumpScale),this.normalMap&&this.normalMap.isTexture&&(n.normalMap=this.normalMap.toJSON(e).uuid,n.normalMapType=this.normalMapType,n.normalScale=this.normalScale.toArray()),this.displacementMap&&this.displacementMap.isTexture&&(n.displacementMap=this.displacementMap.toJSON(e).uuid,n.displacementScale=this.displacementScale,n.displacementBias=this.displacementBias),this.roughnessMap&&this.roughnessMap.isTexture&&(n.roughnessMap=this.roughnessMap.toJSON(e).uuid),this.metalnessMap&&this.metalnessMap.isTexture&&(n.metalnessMap=this.metalnessMap.toJSON(e).uuid),this.emissiveMap&&this.emissiveMap.isTexture&&(n.emissiveMap=this.emissiveMap.toJSON(e).uuid),this.specularMap&&this.specularMap.isTexture&&(n.specularMap=this.specularMap.toJSON(e).uuid),this.specularIntensityMap&&this.specularIntensityMap.isTexture&&(n.specularIntensityMap=this.specularIntensityMap.toJSON(e).uuid),this.specularColorMap&&this.specularColorMap.isTexture&&(n.specularColorMap=this.specularColorMap.toJSON(e).uuid),this.envMap&&this.envMap.isTexture&&(n.envMap=this.envMap.toJSON(e).uuid,this.combine!==void 0&&(n.combine=this.combine)),this.envMapRotation!==void 0&&(n.envMapRotation=this.envMapRotation.toArray()),this.envMapIntensity!==void 0&&(n.envMapIntensity=this.envMapIntensity),this.reflectivity!==void 0&&(n.reflectivity=this.reflectivity),this.refractionRatio!==void 0&&(n.refractionRatio=this.refractionRatio),this.gradientMap&&this.gradientMap.isTexture&&(n.gradientMap=this.gradientMap.toJSON(e).uuid),this.transmission!==void 0&&(n.transmission=this.transmission),this.transmissionMap&&this.transmissionMap.isTexture&&(n.transmissionMap=this.transmissionMap.toJSON(e).uuid),this.thickness!==void 0&&(n.thickness=this.thickness),this.thicknessMap&&this.thicknessMap.isTexture&&(n.thicknessMap=this.thicknessMap.toJSON(e).uuid),this.attenuationDistance!==void 0&&this.attenuationDistance!==1/0&&(n.attenuationDistance=this.attenuationDistance),this.attenuationColor!==void 0&&(n.attenuationColor=this.attenuationColor.getHex()),this.size!==void 0&&(n.size=this.size),this.shadowSide!==null&&(n.shadowSide=this.shadowSide),this.sizeAttenuation!==void 0&&(n.sizeAttenuation=this.sizeAttenuation),this.blending!==Qi&&(n.blending=this.blending),this.side!==en&&(n.side=this.side),this.vertexColors===!0&&(n.vertexColors=!0),this.opacity<1&&(n.opacity=this.opacity),this.transparent===!0&&(n.transparent=!0),this.blendSrc!==sa&&(n.blendSrc=this.blendSrc),this.blendDst!==ra&&(n.blendDst=this.blendDst),this.blendEquation!==Ii&&(n.blendEquation=this.blendEquation),this.blendSrcAlpha!==null&&(n.blendSrcAlpha=this.blendSrcAlpha),this.blendDstAlpha!==null&&(n.blendDstAlpha=this.blendDstAlpha),this.blendEquationAlpha!==null&&(n.blendEquationAlpha=this.blendEquationAlpha),this.blendColor&&this.blendColor.isColor&&(n.blendColor=this.blendColor.getHex()),this.blendAlpha!==0&&(n.blendAlpha=this.blendAlpha),this.depthFunc!==ss&&(n.depthFunc=this.depthFunc),this.depthTest===!1&&(n.depthTest=this.depthTest),this.depthWrite===!1&&(n.depthWrite=this.depthWrite),this.colorWrite===!1&&(n.colorWrite=this.colorWrite),this.stencilWriteMask!==255&&(n.stencilWriteMask=this.stencilWriteMask),this.stencilFunc!==Fl&&(n.stencilFunc=this.stencilFunc),this.stencilRef!==0&&(n.stencilRef=this.stencilRef),this.stencilFuncMask!==255&&(n.stencilFuncMask=this.stencilFuncMask),this.stencilFail!==Fi&&(n.stencilFail=this.stencilFail),this.stencilZFail!==Fi&&(n.stencilZFail=this.stencilZFail),this.stencilZPass!==Fi&&(n.stencilZPass=this.stencilZPass),this.stencilWrite===!0&&(n.stencilWrite=this.stencilWrite),this.rotation!==void 0&&this.rotation!==0&&(n.rotation=this.rotation),this.polygonOffset===!0&&(n.polygonOffset=!0),this.polygonOffsetFactor!==0&&(n.polygonOffsetFactor=this.polygonOffsetFactor),this.polygonOffsetUnits!==0&&(n.polygonOffsetUnits=this.polygonOffsetUnits),this.linewidth!==void 0&&this.linewidth!==1&&(n.linewidth=this.linewidth),this.dashSize!==void 0&&(n.dashSize=this.dashSize),this.gapSize!==void 0&&(n.gapSize=this.gapSize),this.scale!==void 0&&(n.scale=this.scale),this.dithering===!0&&(n.dithering=!0),this.alphaTest>0&&(n.alphaTest=this.alphaTest),this.alphaHash===!0&&(n.alphaHash=!0),this.alphaToCoverage===!0&&(n.alphaToCoverage=!0),this.premultipliedAlpha===!0&&(n.premultipliedAlpha=!0),this.forceSinglePass===!0&&(n.forceSinglePass=!0),this.wireframe===!0&&(n.wireframe=!0),this.wireframeLinewidth>1&&(n.wireframeLinewidth=this.wireframeLinewidth),this.wireframeLinecap!=="round"&&(n.wireframeLinecap=this.wireframeLinecap),this.wireframeLinejoin!=="round"&&(n.wireframeLinejoin=this.wireframeLinejoin),this.flatShading===!0&&(n.flatShading=!0),this.visible===!1&&(n.visible=!1),this.toneMapped===!1&&(n.toneMapped=!1),this.fog===!1&&(n.fog=!1),Object.keys(this.userData).length>0&&(n.userData=this.userData);function i(r){let o=[];for(let a in r){let c=r[a];delete c.metadata,o.push(c)}return o}if(t){let r=i(e.textures),o=i(e.images);r.length>0&&(n.textures=r),o.length>0&&(n.images=o)}return n}clone(){return new this.constructor().copy(this)}copy(e){this.name=e.name,this.blending=e.blending,this.side=e.side,this.vertexColors=e.vertexColors,this.opacity=e.opacity,this.transparent=e.transparent,this.blendSrc=e.blendSrc,this.blendDst=e.blendDst,this.blendEquation=e.blendEquation,this.blendSrcAlpha=e.blendSrcAlpha,this.blendDstAlpha=e.blendDstAlpha,this.blendEquationAlpha=e.blendEquationAlpha,this.blendColor.copy(e.blendColor),this.blendAlpha=e.blendAlpha,this.depthFunc=e.depthFunc,this.depthTest=e.depthTest,this.depthWrite=e.depthWrite,this.stencilWriteMask=e.stencilWriteMask,this.stencilFunc=e.stencilFunc,this.stencilRef=e.stencilRef,this.stencilFuncMask=e.stencilFuncMask,this.stencilFail=e.stencilFail,this.stencilZFail=e.stencilZFail,this.stencilZPass=e.stencilZPass,this.stencilWrite=e.stencilWrite;let t=e.clippingPlanes,n=null;if(t!==null){let i=t.length;n=new Array(i);for(let r=0;r!==i;++r)n[r]=t[r].clone()}return this.clippingPlanes=n,this.clipIntersection=e.clipIntersection,this.clipShadows=e.clipShadows,this.shadowSide=e.shadowSide,this.colorWrite=e.colorWrite,this.precision=e.precision,this.polygonOffset=e.polygonOffset,this.polygonOffsetFactor=e.polygonOffsetFactor,this.polygonOffsetUnits=e.polygonOffsetUnits,this.dithering=e.dithering,this.alphaTest=e.alphaTest,this.alphaHash=e.alphaHash,this.alphaToCoverage=e.alphaToCoverage,this.premultipliedAlpha=e.premultipliedAlpha,this.forceSinglePass=e.forceSinglePass,this.visible=e.visible,this.toneMapped=e.toneMapped,this.userData=JSON.parse(JSON.stringify(e.userData)),this}dispose(){this.dispatchEvent({type:"dispose"})}set needsUpdate(e){e===!0&&this.version++}onBuild(){console.warn("Material: onBuild() has been removed.")}},Yt=class extends an{static get type(){return"MeshBasicMaterial"}constructor(e){super(),this.isMeshBasicMaterial=!0,this.color=new ve(16777215),this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new pn,this.combine=$u,this.reflectivity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.color.copy(e.color),this.map=e.map,this.lightMap=e.lightMap,this.lightMapIntensity=e.lightMapIntensity,this.aoMap=e.aoMap,this.aoMapIntensity=e.aoMapIntensity,this.specularMap=e.specularMap,this.alphaMap=e.alphaMap,this.envMap=e.envMap,this.envMapRotation.copy(e.envMapRotation),this.combine=e.combine,this.reflectivity=e.reflectivity,this.refractionRatio=e.refractionRatio,this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this.wireframeLinecap=e.wireframeLinecap,this.wireframeLinejoin=e.wireframeLinejoin,this.fog=e.fog,this}};var bt=new P,br=new le,it=class{constructor(e,t,n=!1){if(Array.isArray(e))throw new TypeError("THREE.BufferAttribute: array should be a Typed Array.");this.isBufferAttribute=!0,this.name="",this.array=e,this.itemSize=t,this.count=e!==void 0?e.length/t:0,this.normalized=n,this.usage=Ha,this.updateRanges=[],this.gpuType=Tn,this.version=0}onUploadCallback(){}set needsUpdate(e){e===!0&&this.version++}setUsage(e){return this.usage=e,this}addUpdateRange(e,t){this.updateRanges.push({start:e,count:t})}clearUpdateRanges(){this.updateRanges.length=0}copy(e){return this.name=e.name,this.array=new e.array.constructor(e.array),this.itemSize=e.itemSize,this.count=e.count,this.normalized=e.normalized,this.usage=e.usage,this.gpuType=e.gpuType,this}copyAt(e,t,n){e*=this.itemSize,n*=t.itemSize;for(let i=0,r=this.itemSize;i<r;i++)this.array[e+i]=t.array[n+i];return this}copyArray(e){return this.array.set(e),this}applyMatrix3(e){if(this.itemSize===2)for(let t=0,n=this.count;t<n;t++)br.fromBufferAttribute(this,t),br.applyMatrix3(e),this.setXY(t,br.x,br.y);else if(this.itemSize===3)for(let t=0,n=this.count;t<n;t++)bt.fromBufferAttribute(this,t),bt.applyMatrix3(e),this.setXYZ(t,bt.x,bt.y,bt.z);return this}applyMatrix4(e){for(let t=0,n=this.count;t<n;t++)bt.fromBufferAttribute(this,t),bt.applyMatrix4(e),this.setXYZ(t,bt.x,bt.y,bt.z);return this}applyNormalMatrix(e){for(let t=0,n=this.count;t<n;t++)bt.fromBufferAttribute(this,t),bt.applyNormalMatrix(e),this.setXYZ(t,bt.x,bt.y,bt.z);return this}transformDirection(e){for(let t=0,n=this.count;t<n;t++)bt.fromBufferAttribute(this,t),bt.transformDirection(e),this.setXYZ(t,bt.x,bt.y,bt.z);return this}set(e,t=0){return this.array.set(e,t),this}getComponent(e,t){let n=this.array[e*this.itemSize+t];return this.normalized&&(n=wn(n,this.array)),n}setComponent(e,t,n){return this.normalized&&(n=ct(n,this.array)),this.array[e*this.itemSize+t]=n,this}getX(e){let t=this.array[e*this.itemSize];return this.normalized&&(t=wn(t,this.array)),t}setX(e,t){return this.normalized&&(t=ct(t,this.array)),this.array[e*this.itemSize]=t,this}getY(e){let t=this.array[e*this.itemSize+1];return this.normalized&&(t=wn(t,this.array)),t}setY(e,t){return this.normalized&&(t=ct(t,this.array)),this.array[e*this.itemSize+1]=t,this}getZ(e){let t=this.array[e*this.itemSize+2];return this.normalized&&(t=wn(t,this.array)),t}setZ(e,t){return this.normalized&&(t=ct(t,this.array)),this.array[e*this.itemSize+2]=t,this}getW(e){let t=this.array[e*this.itemSize+3];return this.normalized&&(t=wn(t,this.array)),t}setW(e,t){return this.normalized&&(t=ct(t,this.array)),this.array[e*this.itemSize+3]=t,this}setXY(e,t,n){return e*=this.itemSize,this.normalized&&(t=ct(t,this.array),n=ct(n,this.array)),this.array[e+0]=t,this.array[e+1]=n,this}setXYZ(e,t,n,i){return e*=this.itemSize,this.normalized&&(t=ct(t,this.array),n=ct(n,this.array),i=ct(i,this.array)),this.array[e+0]=t,this.array[e+1]=n,this.array[e+2]=i,this}setXYZW(e,t,n,i,r){return e*=this.itemSize,this.normalized&&(t=ct(t,this.array),n=ct(n,this.array),i=ct(i,this.array),r=ct(r,this.array)),this.array[e+0]=t,this.array[e+1]=n,this.array[e+2]=i,this.array[e+3]=r,this}onUpload(e){return this.onUploadCallback=e,this}clone(){return new this.constructor(this.array,this.itemSize).copy(this)}toJSON(){let e={itemSize:this.itemSize,type:this.array.constructor.name,array:Array.from(this.array),normalized:this.normalized};return this.name!==""&&(e.name=this.name),this.usage!==Ha&&(e.usage=this.usage),e}};var Kr=class extends it{constructor(e,t,n){super(new Uint16Array(e),t,n)}};var Jr=class extends it{constructor(e,t,n){super(new Uint32Array(e),t,n)}};var nt=class extends it{constructor(e,t,n){super(new Float32Array(e),t,n)}},ld=0,hn=new Le,Wo=new gt,qi=new P,sn=new dn,Fs=new dn,It=new P,Mt=class s extends ui{constructor(){super(),this.isBufferGeometry=!0,Object.defineProperty(this,"id",{value:ld++}),this.uuid=An(),this.name="",this.type="BufferGeometry",this.index=null,this.indirect=null,this.attributes={},this.morphAttributes={},this.morphTargetsRelative=!1,this.groups=[],this.boundingBox=null,this.boundingSphere=null,this.drawRange={start:0,count:1/0},this.userData={}}getIndex(){return this.index}setIndex(e){return Array.isArray(e)?this.index=new(ch(e)?Jr:Kr)(e,1):this.index=e,this}setIndirect(e){return this.indirect=e,this}getIndirect(){return this.indirect}getAttribute(e){return this.attributes[e]}setAttribute(e,t){return this.attributes[e]=t,this}deleteAttribute(e){return delete this.attributes[e],this}hasAttribute(e){return this.attributes[e]!==void 0}addGroup(e,t,n=0){this.groups.push({start:e,count:t,materialIndex:n})}clearGroups(){this.groups=[]}setDrawRange(e,t){this.drawRange.start=e,this.drawRange.count=t}applyMatrix4(e){let t=this.attributes.position;t!==void 0&&(t.applyMatrix4(e),t.needsUpdate=!0);let n=this.attributes.normal;if(n!==void 0){let r=new ke().getNormalMatrix(e);n.applyNormalMatrix(r),n.needsUpdate=!0}let i=this.attributes.tangent;return i!==void 0&&(i.transformDirection(e),i.needsUpdate=!0),this.boundingBox!==null&&this.computeBoundingBox(),this.boundingSphere!==null&&this.computeBoundingSphere(),this}applyQuaternion(e){return hn.makeRotationFromQuaternion(e),this.applyMatrix4(hn),this}rotateX(e){return hn.makeRotationX(e),this.applyMatrix4(hn),this}rotateY(e){return hn.makeRotationY(e),this.applyMatrix4(hn),this}rotateZ(e){return hn.makeRotationZ(e),this.applyMatrix4(hn),this}translate(e,t,n){return hn.makeTranslation(e,t,n),this.applyMatrix4(hn),this}scale(e,t,n){return hn.makeScale(e,t,n),this.applyMatrix4(hn),this}lookAt(e){return Wo.lookAt(e),Wo.updateMatrix(),this.applyMatrix4(Wo.matrix),this}center(){return this.computeBoundingBox(),this.boundingBox.getCenter(qi).negate(),this.translate(qi.x,qi.y,qi.z),this}setFromPoints(e){let t=this.getAttribute("position");if(t===void 0){let n=[];for(let i=0,r=e.length;i<r;i++){let o=e[i];n.push(o.x,o.y,o.z||0)}this.setAttribute("position",new nt(n,3))}else{for(let n=0,i=t.count;n<i;n++){let r=e[n];t.setXYZ(n,r.x,r.y,r.z||0)}e.length>t.count&&console.warn("THREE.BufferGeometry: Buffer size too small for points data. Use .dispose() and create a new geometry."),t.needsUpdate=!0}return this}computeBoundingBox(){this.boundingBox===null&&(this.boundingBox=new dn);let e=this.attributes.position,t=this.morphAttributes.position;if(e&&e.isGLBufferAttribute){console.error("THREE.BufferGeometry.computeBoundingBox(): GLBufferAttribute requires a manual bounding box.",this),this.boundingBox.set(new P(-1/0,-1/0,-1/0),new P(1/0,1/0,1/0));return}if(e!==void 0){if(this.boundingBox.setFromBufferAttribute(e),t)for(let n=0,i=t.length;n<i;n++){let r=t[n];sn.setFromBufferAttribute(r),this.morphTargetsRelative?(It.addVectors(this.boundingBox.min,sn.min),this.boundingBox.expandByPoint(It),It.addVectors(this.boundingBox.max,sn.max),this.boundingBox.expandByPoint(It)):(this.boundingBox.expandByPoint(sn.min),this.boundingBox.expandByPoint(sn.max))}}else this.boundingBox.makeEmpty();(isNaN(this.boundingBox.min.x)||isNaN(this.boundingBox.min.y)||isNaN(this.boundingBox.min.z))&&console.error('THREE.BufferGeometry.computeBoundingBox(): Computed min/max have NaN values. The "position" attribute is likely to have NaN values.',this)}computeBoundingSphere(){this.boundingSphere===null&&(this.boundingSphere=new on);let e=this.attributes.position,t=this.morphAttributes.position;if(e&&e.isGLBufferAttribute){console.error("THREE.BufferGeometry.computeBoundingSphere(): GLBufferAttribute requires a manual bounding sphere.",this),this.boundingSphere.set(new P,1/0);return}if(e){let n=this.boundingSphere.center;if(sn.setFromBufferAttribute(e),t)for(let r=0,o=t.length;r<o;r++){let a=t[r];Fs.setFromBufferAttribute(a),this.morphTargetsRelative?(It.addVectors(sn.min,Fs.min),sn.expandByPoint(It),It.addVectors(sn.max,Fs.max),sn.expandByPoint(It)):(sn.expandByPoint(Fs.min),sn.expandByPoint(Fs.max))}sn.getCenter(n);let i=0;for(let r=0,o=e.count;r<o;r++)It.fromBufferAttribute(e,r),i=Math.max(i,n.distanceToSquared(It));if(t)for(let r=0,o=t.length;r<o;r++){let a=t[r],c=this.morphTargetsRelative;for(let l=0,u=a.count;l<u;l++)It.fromBufferAttribute(a,l),c&&(qi.fromBufferAttribute(e,l),It.add(qi)),i=Math.max(i,n.distanceToSquared(It))}this.boundingSphere.radius=Math.sqrt(i),isNaN(this.boundingSphere.radius)&&console.error('THREE.BufferGeometry.computeBoundingSphere(): Computed radius is NaN. The "position" attribute is likely to have NaN values.',this)}}computeTangents(){let e=this.index,t=this.attributes;if(e===null||t.position===void 0||t.normal===void 0||t.uv===void 0){console.error("THREE.BufferGeometry: .computeTangents() failed. Missing required attributes (index, position, normal or uv)");return}let n=t.position,i=t.normal,r=t.uv;this.hasAttribute("tangent")===!1&&this.setAttribute("tangent",new it(new Float32Array(4*n.count),4));let o=this.getAttribute("tangent"),a=[],c=[];for(let I=0;I<n.count;I++)a[I]=new P,c[I]=new P;let l=new P,u=new P,h=new P,f=new le,p=new le,g=new le,v=new P,m=new P;function d(I,x,y){l.fromBufferAttribute(n,I),u.fromBufferAttribute(n,x),h.fromBufferAttribute(n,y),f.fromBufferAttribute(r,I),p.fromBufferAttribute(r,x),g.fromBufferAttribute(r,y),u.sub(l),h.sub(l),p.sub(f),g.sub(f);let T=1/(p.x*g.y-g.x*p.y);isFinite(T)&&(v.copy(u).multiplyScalar(g.y).addScaledVector(h,-p.y).multiplyScalar(T),m.copy(h).multiplyScalar(p.x).addScaledVector(u,-g.x).multiplyScalar(T),a[I].add(v),a[x].add(v),a[y].add(v),c[I].add(m),c[x].add(m),c[y].add(m))}let M=this.groups;M.length===0&&(M=[{start:0,count:e.count}]);for(let I=0,x=M.length;I<x;++I){let y=M[I],T=y.start,L=y.count;for(let D=T,F=T+L;D<F;D+=3)d(e.getX(D+0),e.getX(D+1),e.getX(D+2))}let b=new P,_=new P,C=new P,A=new P;function E(I){C.fromBufferAttribute(i,I),A.copy(C);let x=a[I];b.copy(x),b.sub(C.multiplyScalar(C.dot(x))).normalize(),_.crossVectors(A,x);let T=_.dot(c[I])<0?-1:1;o.setXYZW(I,b.x,b.y,b.z,T)}for(let I=0,x=M.length;I<x;++I){let y=M[I],T=y.start,L=y.count;for(let D=T,F=T+L;D<F;D+=3)E(e.getX(D+0)),E(e.getX(D+1)),E(e.getX(D+2))}}computeVertexNormals(){let e=this.index,t=this.getAttribute("position");if(t!==void 0){let n=this.getAttribute("normal");if(n===void 0)n=new it(new Float32Array(t.count*3),3),this.setAttribute("normal",n);else for(let f=0,p=n.count;f<p;f++)n.setXYZ(f,0,0,0);let i=new P,r=new P,o=new P,a=new P,c=new P,l=new P,u=new P,h=new P;if(e)for(let f=0,p=e.count;f<p;f+=3){let g=e.getX(f+0),v=e.getX(f+1),m=e.getX(f+2);i.fromBufferAttribute(t,g),r.fromBufferAttribute(t,v),o.fromBufferAttribute(t,m),u.subVectors(o,r),h.subVectors(i,r),u.cross(h),a.fromBufferAttribute(n,g),c.fromBufferAttribute(n,v),l.fromBufferAttribute(n,m),a.add(u),c.add(u),l.add(u),n.setXYZ(g,a.x,a.y,a.z),n.setXYZ(v,c.x,c.y,c.z),n.setXYZ(m,l.x,l.y,l.z)}else for(let f=0,p=t.count;f<p;f+=3)i.fromBufferAttribute(t,f+0),r.fromBufferAttribute(t,f+1),o.fromBufferAttribute(t,f+2),u.subVectors(o,r),h.subVectors(i,r),u.cross(h),n.setXYZ(f+0,u.x,u.y,u.z),n.setXYZ(f+1,u.x,u.y,u.z),n.setXYZ(f+2,u.x,u.y,u.z);this.normalizeNormals(),n.needsUpdate=!0}}normalizeNormals(){let e=this.attributes.normal;for(let t=0,n=e.count;t<n;t++)It.fromBufferAttribute(e,t),It.normalize(),e.setXYZ(t,It.x,It.y,It.z)}toNonIndexed(){function e(a,c){let l=a.array,u=a.itemSize,h=a.normalized,f=new l.constructor(c.length*u),p=0,g=0;for(let v=0,m=c.length;v<m;v++){a.isInterleavedBufferAttribute?p=c[v]*a.data.stride+a.offset:p=c[v]*u;for(let d=0;d<u;d++)f[g++]=l[p++]}return new it(f,u,h)}if(this.index===null)return console.warn("THREE.BufferGeometry.toNonIndexed(): BufferGeometry is already non-indexed."),this;let t=new s,n=this.index.array,i=this.attributes;for(let a in i){let c=i[a],l=e(c,n);t.setAttribute(a,l)}let r=this.morphAttributes;for(let a in r){let c=[],l=r[a];for(let u=0,h=l.length;u<h;u++){let f=l[u],p=e(f,n);c.push(p)}t.morphAttributes[a]=c}t.morphTargetsRelative=this.morphTargetsRelative;let o=this.groups;for(let a=0,c=o.length;a<c;a++){let l=o[a];t.addGroup(l.start,l.count,l.materialIndex)}return t}toJSON(){let e={metadata:{version:4.6,type:"BufferGeometry",generator:"BufferGeometry.toJSON"}};if(e.uuid=this.uuid,e.type=this.type,this.name!==""&&(e.name=this.name),Object.keys(this.userData).length>0&&(e.userData=this.userData),this.parameters!==void 0){let c=this.parameters;for(let l in c)c[l]!==void 0&&(e[l]=c[l]);return e}e.data={attributes:{}};let t=this.index;t!==null&&(e.data.index={type:t.array.constructor.name,array:Array.prototype.slice.call(t.array)});let n=this.attributes;for(let c in n){let l=n[c];e.data.attributes[c]=l.toJSON(e.data)}let i={},r=!1;for(let c in this.morphAttributes){let l=this.morphAttributes[c],u=[];for(let h=0,f=l.length;h<f;h++){let p=l[h];u.push(p.toJSON(e.data))}u.length>0&&(i[c]=u,r=!0)}r&&(e.data.morphAttributes=i,e.data.morphTargetsRelative=this.morphTargetsRelative);let o=this.groups;o.length>0&&(e.data.groups=JSON.parse(JSON.stringify(o)));let a=this.boundingSphere;return a!==null&&(e.data.boundingSphere={center:a.center.toArray(),radius:a.radius}),e}clone(){return new this.constructor().copy(this)}copy(e){this.index=null,this.attributes={},this.morphAttributes={},this.groups=[],this.boundingBox=null,this.boundingSphere=null;let t={};this.name=e.name;let n=e.index;n!==null&&this.setIndex(n.clone(t));let i=e.attributes;for(let l in i){let u=i[l];this.setAttribute(l,u.clone(t))}let r=e.morphAttributes;for(let l in r){let u=[],h=r[l];for(let f=0,p=h.length;f<p;f++)u.push(h[f].clone(t));this.morphAttributes[l]=u}this.morphTargetsRelative=e.morphTargetsRelative;let o=e.groups;for(let l=0,u=o.length;l<u;l++){let h=o[l];this.addGroup(h.start,h.count,h.materialIndex)}let a=e.boundingBox;a!==null&&(this.boundingBox=a.clone());let c=e.boundingSphere;return c!==null&&(this.boundingSphere=c.clone()),this.drawRange.start=e.drawRange.start,this.drawRange.count=e.drawRange.count,this.userData=e.userData,this}dispose(){this.dispatchEvent({type:"dispose"})}},eu=new Le,Ei=new fs,Sr=new on,tu=new P,wr=new P,Er=new P,Tr=new P,Xo=new P,Ar=new P,nu=new P,Rr=new P,Fe=class extends gt{constructor(e=new Mt,t=new Yt){super(),this.isMesh=!0,this.type="Mesh",this.geometry=e,this.material=t,this.updateMorphTargets()}copy(e,t){return super.copy(e,t),e.morphTargetInfluences!==void 0&&(this.morphTargetInfluences=e.morphTargetInfluences.slice()),e.morphTargetDictionary!==void 0&&(this.morphTargetDictionary=Object.assign({},e.morphTargetDictionary)),this.material=Array.isArray(e.material)?e.material.slice():e.material,this.geometry=e.geometry,this}updateMorphTargets(){let t=this.geometry.morphAttributes,n=Object.keys(t);if(n.length>0){let i=t[n[0]];if(i!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,o=i.length;r<o;r++){let a=i[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[a]=r}}}}getVertexPosition(e,t){let n=this.geometry,i=n.attributes.position,r=n.morphAttributes.position,o=n.morphTargetsRelative;t.fromBufferAttribute(i,e);let a=this.morphTargetInfluences;if(r&&a){Ar.set(0,0,0);for(let c=0,l=r.length;c<l;c++){let u=a[c],h=r[c];u!==0&&(Xo.fromBufferAttribute(h,e),o?Ar.addScaledVector(Xo,u):Ar.addScaledVector(Xo.sub(t),u))}t.add(Ar)}return t}raycast(e,t){let n=this.geometry,i=this.material,r=this.matrixWorld;i!==void 0&&(n.boundingSphere===null&&n.computeBoundingSphere(),Sr.copy(n.boundingSphere),Sr.applyMatrix4(r),Ei.copy(e.ray).recast(e.near),!(Sr.containsPoint(Ei.origin)===!1&&(Ei.intersectSphere(Sr,tu)===null||Ei.origin.distanceToSquared(tu)>(e.far-e.near)**2))&&(eu.copy(r).invert(),Ei.copy(e.ray).applyMatrix4(eu),!(n.boundingBox!==null&&Ei.intersectsBox(n.boundingBox)===!1)&&this._computeIntersections(e,t,Ei)))}_computeIntersections(e,t,n){let i,r=this.geometry,o=this.material,a=r.index,c=r.attributes.position,l=r.attributes.uv,u=r.attributes.uv1,h=r.attributes.normal,f=r.groups,p=r.drawRange;if(a!==null)if(Array.isArray(o))for(let g=0,v=f.length;g<v;g++){let m=f[g],d=o[m.materialIndex],M=Math.max(m.start,p.start),b=Math.min(a.count,Math.min(m.start+m.count,p.start+p.count));for(let _=M,C=b;_<C;_+=3){let A=a.getX(_),E=a.getX(_+1),I=a.getX(_+2);i=Cr(this,d,e,n,l,u,h,A,E,I),i&&(i.faceIndex=Math.floor(_/3),i.face.materialIndex=m.materialIndex,t.push(i))}}else{let g=Math.max(0,p.start),v=Math.min(a.count,p.start+p.count);for(let m=g,d=v;m<d;m+=3){let M=a.getX(m),b=a.getX(m+1),_=a.getX(m+2);i=Cr(this,o,e,n,l,u,h,M,b,_),i&&(i.faceIndex=Math.floor(m/3),t.push(i))}}else if(c!==void 0)if(Array.isArray(o))for(let g=0,v=f.length;g<v;g++){let m=f[g],d=o[m.materialIndex],M=Math.max(m.start,p.start),b=Math.min(c.count,Math.min(m.start+m.count,p.start+p.count));for(let _=M,C=b;_<C;_+=3){let A=_,E=_+1,I=_+2;i=Cr(this,d,e,n,l,u,h,A,E,I),i&&(i.faceIndex=Math.floor(_/3),i.face.materialIndex=m.materialIndex,t.push(i))}}else{let g=Math.max(0,p.start),v=Math.min(c.count,p.start+p.count);for(let m=g,d=v;m<d;m+=3){let M=m,b=m+1,_=m+2;i=Cr(this,o,e,n,l,u,h,M,b,_),i&&(i.faceIndex=Math.floor(m/3),t.push(i))}}}};function ud(s,e,t,n,i,r,o,a){let c;if(e.side===Vt?c=n.intersectTriangle(o,r,i,!0,a):c=n.intersectTriangle(i,r,o,e.side===en,a),c===null)return null;Rr.copy(a),Rr.applyMatrix4(s.matrixWorld);let l=t.ray.origin.distanceTo(Rr);return l<t.near||l>t.far?null:{distance:l,point:Rr.clone(),object:s}}function Cr(s,e,t,n,i,r,o,a,c,l){s.getVertexPosition(a,wr),s.getVertexPosition(c,Er),s.getVertexPosition(l,Tr);let u=ud(s,e,t,n,wr,Er,Tr,nu);if(u){let h=new P;Pi.getBarycoord(nu,wr,Er,Tr,h),i&&(u.uv=Pi.getInterpolatedAttribute(i,a,c,l,h,new le)),r&&(u.uv1=Pi.getInterpolatedAttribute(r,a,c,l,h,new le)),o&&(u.normal=Pi.getInterpolatedAttribute(o,a,c,l,h,new P),u.normal.dot(n.direction)>0&&u.normal.multiplyScalar(-1));let f={a,b:c,c:l,normal:new P,materialIndex:0};Pi.getNormal(wr,Er,Tr,f.normal),u.face=f,u.barycoord=h}return u}var cn=class s extends Mt{constructor(e=1,t=1,n=1,i=1,r=1,o=1){super(),this.type="BoxGeometry",this.parameters={width:e,height:t,depth:n,widthSegments:i,heightSegments:r,depthSegments:o};let a=this;i=Math.floor(i),r=Math.floor(r),o=Math.floor(o);let c=[],l=[],u=[],h=[],f=0,p=0;g("z","y","x",-1,-1,n,t,e,o,r,0),g("z","y","x",1,-1,n,t,-e,o,r,1),g("x","z","y",1,1,e,n,t,i,o,2),g("x","z","y",1,-1,e,n,-t,i,o,3),g("x","y","z",1,-1,e,t,n,i,r,4),g("x","y","z",-1,-1,e,t,-n,i,r,5),this.setIndex(c),this.setAttribute("position",new nt(l,3)),this.setAttribute("normal",new nt(u,3)),this.setAttribute("uv",new nt(h,2));function g(v,m,d,M,b,_,C,A,E,I,x){let y=_/E,T=C/I,L=_/2,D=C/2,F=A/2,X=E+1,z=I+1,K=0,H=0,k=new P;for(let $=0;$<z;$++){let ie=$*T-D;for(let j=0;j<X;j++){let ue=j*y-L;k[v]=ue*M,k[m]=ie*b,k[d]=F,l.push(k.x,k.y,k.z),k[v]=0,k[m]=0,k[d]=A>0?1:-1,u.push(k.x,k.y,k.z),h.push(j/E),h.push(1-$/I),K+=1}}for(let $=0;$<I;$++)for(let ie=0;ie<E;ie++){let j=f+ie+X*$,ue=f+ie+X*($+1),G=f+(ie+1)+X*($+1),J=f+(ie+1)+X*$;c.push(j,ue,J),c.push(ue,G,J),H+=6}a.addGroup(p,H,x),p+=H,f+=K}}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new s(e.width,e.height,e.depth,e.widthSegments,e.heightSegments,e.depthSegments)}};function ds(s){let e={};for(let t in s){e[t]={};for(let n in s[t]){let i=s[t][n];i&&(i.isColor||i.isMatrix3||i.isMatrix4||i.isVector2||i.isVector3||i.isVector4||i.isTexture||i.isQuaternion)?i.isRenderTargetTexture?(console.warn("UniformsUtils: Textures of render targets cannot be cloned via cloneUniforms() or mergeUniforms()."),e[t][n]=null):e[t][n]=i.clone():Array.isArray(i)?e[t][n]=i.slice():e[t][n]=i}}return e}function qt(s){let e={};for(let t=0;t<s.length;t++){let n=ds(s[t]);for(let i in n)e[i]=n[i]}return e}function hd(s){let e=[];for(let t=0;t<s.length;t++)e.push(s[t].clone());return e}function uh(s){let e=s.getRenderTarget();return e===null?s.outputColorSpace:e.isXRRenderTarget===!0?e.texture.colorSpace:Ye.workingColorSpace}var fd={clone:ds,merge:qt},dd=`void main() {
	gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}`,pd=`void main() {
	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}`,Gt=class extends an{static get type(){return"ShaderMaterial"}constructor(e){super(),this.isShaderMaterial=!0,this.defines={},this.uniforms={},this.uniformsGroups=[],this.vertexShader=dd,this.fragmentShader=pd,this.linewidth=1,this.wireframe=!1,this.wireframeLinewidth=1,this.fog=!1,this.lights=!1,this.clipping=!1,this.forceSinglePass=!0,this.extensions={clipCullDistance:!1,multiDraw:!1},this.defaultAttributeValues={color:[1,1,1],uv:[0,0],uv1:[0,0]},this.index0AttributeName=void 0,this.uniformsNeedUpdate=!1,this.glslVersion=null,e!==void 0&&this.setValues(e)}copy(e){return super.copy(e),this.fragmentShader=e.fragmentShader,this.vertexShader=e.vertexShader,this.uniforms=ds(e.uniforms),this.uniformsGroups=hd(e.uniformsGroups),this.defines=Object.assign({},e.defines),this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this.fog=e.fog,this.lights=e.lights,this.clipping=e.clipping,this.extensions=Object.assign({},e.extensions),this.glslVersion=e.glslVersion,this}toJSON(e){let t=super.toJSON(e);t.glslVersion=this.glslVersion,t.uniforms={};for(let i in this.uniforms){let o=this.uniforms[i].value;o&&o.isTexture?t.uniforms[i]={type:"t",value:o.toJSON(e).uuid}:o&&o.isColor?t.uniforms[i]={type:"c",value:o.getHex()}:o&&o.isVector2?t.uniforms[i]={type:"v2",value:o.toArray()}:o&&o.isVector3?t.uniforms[i]={type:"v3",value:o.toArray()}:o&&o.isVector4?t.uniforms[i]={type:"v4",value:o.toArray()}:o&&o.isMatrix3?t.uniforms[i]={type:"m3",value:o.toArray()}:o&&o.isMatrix4?t.uniforms[i]={type:"m4",value:o.toArray()}:t.uniforms[i]={value:o}}Object.keys(this.defines).length>0&&(t.defines=this.defines),t.vertexShader=this.vertexShader,t.fragmentShader=this.fragmentShader,t.lights=this.lights,t.clipping=this.clipping;let n={};for(let i in this.extensions)this.extensions[i]===!0&&(n[i]=!0);return Object.keys(n).length>0&&(t.extensions=n),t}},jr=class extends gt{constructor(){super(),this.isCamera=!0,this.type="Camera",this.matrixWorldInverse=new Le,this.projectionMatrix=new Le,this.projectionMatrixInverse=new Le,this.coordinateSystem=Wn}copy(e,t){return super.copy(e,t),this.matrixWorldInverse.copy(e.matrixWorldInverse),this.projectionMatrix.copy(e.projectionMatrix),this.projectionMatrixInverse.copy(e.projectionMatrixInverse),this.coordinateSystem=e.coordinateSystem,this}getWorldDirection(e){return super.getWorldDirection(e).negate()}updateMatrixWorld(e){super.updateMatrixWorld(e),this.matrixWorldInverse.copy(this.matrixWorld).invert()}updateWorldMatrix(e,t){super.updateWorldMatrix(e,t),this.matrixWorldInverse.copy(this.matrixWorld).invert()}clone(){return new this.constructor().copy(this)}},ai=new P,iu=new le,su=new le,_t=class extends jr{constructor(e=50,t=1,n=.1,i=2e3){super(),this.isPerspectiveCamera=!0,this.type="PerspectiveCamera",this.fov=e,this.zoom=1,this.near=n,this.far=i,this.focus=10,this.aspect=t,this.view=null,this.filmGauge=35,this.filmOffset=0,this.updateProjectionMatrix()}copy(e,t){return super.copy(e,t),this.fov=e.fov,this.zoom=e.zoom,this.near=e.near,this.far=e.far,this.focus=e.focus,this.aspect=e.aspect,this.view=e.view===null?null:Object.assign({},e.view),this.filmGauge=e.filmGauge,this.filmOffset=e.filmOffset,this}setFocalLength(e){let t=.5*this.getFilmHeight()/e;this.fov=hs*2*Math.atan(t),this.updateProjectionMatrix()}getFocalLength(){let e=Math.tan(Ws*.5*this.fov);return .5*this.getFilmHeight()/e}getEffectiveFOV(){return hs*2*Math.atan(Math.tan(Ws*.5*this.fov)/this.zoom)}getFilmWidth(){return this.filmGauge*Math.min(this.aspect,1)}getFilmHeight(){return this.filmGauge/Math.max(this.aspect,1)}getViewBounds(e,t,n){ai.set(-1,-1,.5).applyMatrix4(this.projectionMatrixInverse),t.set(ai.x,ai.y).multiplyScalar(-e/ai.z),ai.set(1,1,.5).applyMatrix4(this.projectionMatrixInverse),n.set(ai.x,ai.y).multiplyScalar(-e/ai.z)}getViewSize(e,t){return this.getViewBounds(e,iu,su),t.subVectors(su,iu)}setViewOffset(e,t,n,i,r,o){this.aspect=e/t,this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=e,this.view.fullHeight=t,this.view.offsetX=n,this.view.offsetY=i,this.view.width=r,this.view.height=o,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let e=this.near,t=e*Math.tan(Ws*.5*this.fov)/this.zoom,n=2*t,i=this.aspect*n,r=-.5*i,o=this.view;if(this.view!==null&&this.view.enabled){let c=o.fullWidth,l=o.fullHeight;r+=o.offsetX*i/c,t-=o.offsetY*n/l,i*=o.width/c,n*=o.height/l}let a=this.filmOffset;a!==0&&(r+=e*a/this.getFilmWidth()),this.projectionMatrix.makePerspective(r,r+i,t,t-n,e,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(e){let t=super.toJSON(e);return t.object.fov=this.fov,t.object.zoom=this.zoom,t.object.near=this.near,t.object.far=this.far,t.object.focus=this.focus,t.object.aspect=this.aspect,this.view!==null&&(t.object.view=Object.assign({},this.view)),t.object.filmGauge=this.filmGauge,t.object.filmOffset=this.filmOffset,t}},Yi=-90,$i=1,Xa=class extends gt{constructor(e,t,n){super(),this.type="CubeCamera",this.renderTarget=n,this.coordinateSystem=null,this.activeMipmapLevel=0;let i=new _t(Yi,$i,e,t);i.layers=this.layers,this.add(i);let r=new _t(Yi,$i,e,t);r.layers=this.layers,this.add(r);let o=new _t(Yi,$i,e,t);o.layers=this.layers,this.add(o);let a=new _t(Yi,$i,e,t);a.layers=this.layers,this.add(a);let c=new _t(Yi,$i,e,t);c.layers=this.layers,this.add(c);let l=new _t(Yi,$i,e,t);l.layers=this.layers,this.add(l)}updateCoordinateSystem(){let e=this.coordinateSystem,t=this.children.concat(),[n,i,r,o,a,c]=t;for(let l of t)this.remove(l);if(e===Wn)n.up.set(0,1,0),n.lookAt(1,0,0),i.up.set(0,1,0),i.lookAt(-1,0,0),r.up.set(0,0,-1),r.lookAt(0,1,0),o.up.set(0,0,1),o.lookAt(0,-1,0),a.up.set(0,1,0),a.lookAt(0,0,1),c.up.set(0,1,0),c.lookAt(0,0,-1);else if(e===qr)n.up.set(0,-1,0),n.lookAt(-1,0,0),i.up.set(0,-1,0),i.lookAt(1,0,0),r.up.set(0,0,1),r.lookAt(0,1,0),o.up.set(0,0,-1),o.lookAt(0,-1,0),a.up.set(0,-1,0),a.lookAt(0,0,1),c.up.set(0,-1,0),c.lookAt(0,0,-1);else throw new Error("THREE.CubeCamera.updateCoordinateSystem(): Invalid coordinate system: "+e);for(let l of t)this.add(l),l.updateMatrixWorld()}update(e,t){this.parent===null&&this.updateMatrixWorld();let{renderTarget:n,activeMipmapLevel:i}=this;this.coordinateSystem!==e.coordinateSystem&&(this.coordinateSystem=e.coordinateSystem,this.updateCoordinateSystem());let[r,o,a,c,l,u]=this.children,h=e.getRenderTarget(),f=e.getActiveCubeFace(),p=e.getActiveMipmapLevel(),g=e.xr.enabled;e.xr.enabled=!1;let v=n.texture.generateMipmaps;n.texture.generateMipmaps=!1,e.setRenderTarget(n,0,i),e.render(t,r),e.setRenderTarget(n,1,i),e.render(t,o),e.setRenderTarget(n,2,i),e.render(t,a),e.setRenderTarget(n,3,i),e.render(t,c),e.setRenderTarget(n,4,i),e.render(t,l),n.texture.generateMipmaps=v,e.setRenderTarget(n,5,i),e.render(t,u),e.setRenderTarget(h,f,p),e.xr.enabled=g,n.texture.needsPMREMUpdate=!0}},Qr=class extends Pt{constructor(e,t,n,i,r,o,a,c,l,u){e=e!==void 0?e:[],t=t!==void 0?t:rs,super(e,t,n,i,r,o,a,c,l,u),this.isCubeTexture=!0,this.flipY=!1}get images(){return this.image}set images(e){this.image=e}},qa=class extends Rn{constructor(e=1,t={}){super(e,e,t),this.isWebGLCubeRenderTarget=!0;let n={width:e,height:e,depth:1},i=[n,n,n,n,n,n];this.texture=new Qr(i,t.mapping,t.wrapS,t.wrapT,t.magFilter,t.minFilter,t.format,t.type,t.anisotropy,t.colorSpace),this.texture.isRenderTargetTexture=!0,this.texture.generateMipmaps=t.generateMipmaps!==void 0?t.generateMipmaps:!1,this.texture.minFilter=t.minFilter!==void 0?t.minFilter:wt}fromEquirectangularTexture(e,t){this.texture.type=t.type,this.texture.colorSpace=t.colorSpace,this.texture.generateMipmaps=t.generateMipmaps,this.texture.minFilter=t.minFilter,this.texture.magFilter=t.magFilter;let n={uniforms:{tEquirect:{value:null}},vertexShader:`

				varying vec3 vWorldDirection;

				vec3 transformDirection( in vec3 dir, in mat4 matrix ) {

					return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );

				}

				void main() {

					vWorldDirection = transformDirection( position, modelMatrix );

					#include <begin_vertex>
					#include <project_vertex>

				}
			`,fragmentShader:`

				uniform sampler2D tEquirect;

				varying vec3 vWorldDirection;

				#include <common>

				void main() {

					vec3 direction = normalize( vWorldDirection );

					vec2 sampleUV = equirectUv( direction );

					gl_FragColor = texture2D( tEquirect, sampleUV );

				}
			`},i=new cn(5,5,5),r=new Gt({name:"CubemapFromEquirect",uniforms:ds(n.uniforms),vertexShader:n.vertexShader,fragmentShader:n.fragmentShader,side:Vt,blending:li});r.uniforms.tEquirect.value=t;let o=new Fe(i,r),a=t.minFilter;return t.minFilter===Pn&&(t.minFilter=wt),new Xa(1,10,this).update(e,o),t.minFilter=a,o.geometry.dispose(),o.material.dispose(),this}clear(e,t,n,i){let r=e.getRenderTarget();for(let o=0;o<6;o++)e.setRenderTarget(this,o),e.clear(t,n,i);e.setRenderTarget(r)}},qo=new P,md=new P,gd=new ke,Sn=class{constructor(e=new P(1,0,0),t=0){this.isPlane=!0,this.normal=e,this.constant=t}set(e,t){return this.normal.copy(e),this.constant=t,this}setComponents(e,t,n,i){return this.normal.set(e,t,n),this.constant=i,this}setFromNormalAndCoplanarPoint(e,t){return this.normal.copy(e),this.constant=-t.dot(this.normal),this}setFromCoplanarPoints(e,t,n){let i=qo.subVectors(n,t).cross(md.subVectors(e,t)).normalize();return this.setFromNormalAndCoplanarPoint(i,e),this}copy(e){return this.normal.copy(e.normal),this.constant=e.constant,this}normalize(){let e=1/this.normal.length();return this.normal.multiplyScalar(e),this.constant*=e,this}negate(){return this.constant*=-1,this.normal.negate(),this}distanceToPoint(e){return this.normal.dot(e)+this.constant}distanceToSphere(e){return this.distanceToPoint(e.center)-e.radius}projectPoint(e,t){return t.copy(e).addScaledVector(this.normal,-this.distanceToPoint(e))}intersectLine(e,t){let n=e.delta(qo),i=this.normal.dot(n);if(i===0)return this.distanceToPoint(e.start)===0?t.copy(e.start):null;let r=-(e.start.dot(this.normal)+this.constant)/i;return r<0||r>1?null:t.copy(e.start).addScaledVector(n,r)}intersectsLine(e){let t=this.distanceToPoint(e.start),n=this.distanceToPoint(e.end);return t<0&&n>0||n<0&&t>0}intersectsBox(e){return e.intersectsPlane(this)}intersectsSphere(e){return e.intersectsPlane(this)}coplanarPoint(e){return e.copy(this.normal).multiplyScalar(-this.constant)}applyMatrix4(e,t){let n=t||gd.getNormalMatrix(e),i=this.coplanarPoint(qo).applyMatrix4(e),r=this.normal.applyMatrix3(n).normalize();return this.constant=-i.dot(r),this}translate(e){return this.constant-=e.dot(this.normal),this}equals(e){return e.normal.equals(this.normal)&&e.constant===this.constant}clone(){return new this.constructor().copy(this)}},Ti=new on,Ir=new P,Ks=class{constructor(e=new Sn,t=new Sn,n=new Sn,i=new Sn,r=new Sn,o=new Sn){this.planes=[e,t,n,i,r,o]}set(e,t,n,i,r,o){let a=this.planes;return a[0].copy(e),a[1].copy(t),a[2].copy(n),a[3].copy(i),a[4].copy(r),a[5].copy(o),this}copy(e){let t=this.planes;for(let n=0;n<6;n++)t[n].copy(e.planes[n]);return this}setFromProjectionMatrix(e,t=Wn){let n=this.planes,i=e.elements,r=i[0],o=i[1],a=i[2],c=i[3],l=i[4],u=i[5],h=i[6],f=i[7],p=i[8],g=i[9],v=i[10],m=i[11],d=i[12],M=i[13],b=i[14],_=i[15];if(n[0].setComponents(c-r,f-l,m-p,_-d).normalize(),n[1].setComponents(c+r,f+l,m+p,_+d).normalize(),n[2].setComponents(c+o,f+u,m+g,_+M).normalize(),n[3].setComponents(c-o,f-u,m-g,_-M).normalize(),n[4].setComponents(c-a,f-h,m-v,_-b).normalize(),t===Wn)n[5].setComponents(c+a,f+h,m+v,_+b).normalize();else if(t===qr)n[5].setComponents(a,h,v,b).normalize();else throw new Error("THREE.Frustum.setFromProjectionMatrix(): Invalid coordinate system: "+t);return this}intersectsObject(e){if(e.boundingSphere!==void 0)e.boundingSphere===null&&e.computeBoundingSphere(),Ti.copy(e.boundingSphere).applyMatrix4(e.matrixWorld);else{let t=e.geometry;t.boundingSphere===null&&t.computeBoundingSphere(),Ti.copy(t.boundingSphere).applyMatrix4(e.matrixWorld)}return this.intersectsSphere(Ti)}intersectsSprite(e){return Ti.center.set(0,0,0),Ti.radius=.7071067811865476,Ti.applyMatrix4(e.matrixWorld),this.intersectsSphere(Ti)}intersectsSphere(e){let t=this.planes,n=e.center,i=-e.radius;for(let r=0;r<6;r++)if(t[r].distanceToPoint(n)<i)return!1;return!0}intersectsBox(e){let t=this.planes;for(let n=0;n<6;n++){let i=t[n];if(Ir.x=i.normal.x>0?e.max.x:e.min.x,Ir.y=i.normal.y>0?e.max.y:e.min.y,Ir.z=i.normal.z>0?e.max.z:e.min.z,i.distanceToPoint(Ir)<0)return!1}return!0}containsPoint(e){let t=this.planes;for(let n=0;n<6;n++)if(t[n].distanceToPoint(e)<0)return!1;return!0}clone(){return new this.constructor().copy(this)}};function hh(){let s=null,e=!1,t=null,n=null;function i(r,o){t(r,o),n=s.requestAnimationFrame(i)}return{start:function(){e!==!0&&t!==null&&(n=s.requestAnimationFrame(i),e=!0)},stop:function(){s.cancelAnimationFrame(n),e=!1},setAnimationLoop:function(r){t=r},setContext:function(r){s=r}}}function vd(s){let e=new WeakMap;function t(a,c){let l=a.array,u=a.usage,h=l.byteLength,f=s.createBuffer();s.bindBuffer(c,f),s.bufferData(c,l,u),a.onUploadCallback();let p;if(l instanceof Float32Array)p=s.FLOAT;else if(l instanceof Uint16Array)a.isFloat16BufferAttribute?p=s.HALF_FLOAT:p=s.UNSIGNED_SHORT;else if(l instanceof Int16Array)p=s.SHORT;else if(l instanceof Uint32Array)p=s.UNSIGNED_INT;else if(l instanceof Int32Array)p=s.INT;else if(l instanceof Int8Array)p=s.BYTE;else if(l instanceof Uint8Array)p=s.UNSIGNED_BYTE;else if(l instanceof Uint8ClampedArray)p=s.UNSIGNED_BYTE;else throw new Error("THREE.WebGLAttributes: Unsupported buffer data format: "+l);return{buffer:f,type:p,bytesPerElement:l.BYTES_PER_ELEMENT,version:a.version,size:h}}function n(a,c,l){let u=c.array,h=c.updateRanges;if(s.bindBuffer(l,a),h.length===0)s.bufferSubData(l,0,u);else{h.sort((p,g)=>p.start-g.start);let f=0;for(let p=1;p<h.length;p++){let g=h[f],v=h[p];v.start<=g.start+g.count+1?g.count=Math.max(g.count,v.start+v.count-g.start):(++f,h[f]=v)}h.length=f+1;for(let p=0,g=h.length;p<g;p++){let v=h[p];s.bufferSubData(l,v.start*u.BYTES_PER_ELEMENT,u,v.start,v.count)}c.clearUpdateRanges()}c.onUploadCallback()}function i(a){return a.isInterleavedBufferAttribute&&(a=a.data),e.get(a)}function r(a){a.isInterleavedBufferAttribute&&(a=a.data);let c=e.get(a);c&&(s.deleteBuffer(c.buffer),e.delete(a))}function o(a,c){if(a.isInterleavedBufferAttribute&&(a=a.data),a.isGLBufferAttribute){let u=e.get(a);(!u||u.version<a.version)&&e.set(a,{buffer:a.buffer,type:a.type,bytesPerElement:a.elementSize,version:a.version});return}let l=e.get(a);if(l===void 0)e.set(a,t(a,c));else if(l.version<a.version){if(l.size!==a.array.byteLength)throw new Error("THREE.WebGLAttributes: The size of the buffer attribute's array buffer does not match the original size. Resizing buffer attributes is not supported.");n(l.buffer,a,c),l.version=a.version}}return{get:i,remove:r,update:o}}var $t=class s extends Mt{constructor(e=1,t=1,n=1,i=1){super(),this.type="PlaneGeometry",this.parameters={width:e,height:t,widthSegments:n,heightSegments:i};let r=e/2,o=t/2,a=Math.floor(n),c=Math.floor(i),l=a+1,u=c+1,h=e/a,f=t/c,p=[],g=[],v=[],m=[];for(let d=0;d<u;d++){let M=d*f-o;for(let b=0;b<l;b++){let _=b*h-r;g.push(_,-M,0),v.push(0,0,1),m.push(b/a),m.push(1-d/c)}}for(let d=0;d<c;d++)for(let M=0;M<a;M++){let b=M+l*d,_=M+l*(d+1),C=M+1+l*(d+1),A=M+1+l*d;p.push(b,_,A),p.push(_,C,A)}this.setIndex(p),this.setAttribute("position",new nt(g,3)),this.setAttribute("normal",new nt(v,3)),this.setAttribute("uv",new nt(m,2))}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new s(e.width,e.height,e.widthSegments,e.heightSegments)}},xd=`#ifdef USE_ALPHAHASH
	if ( diffuseColor.a < getAlphaHashThreshold( vPosition ) ) discard;
#endif`,_d=`#ifdef USE_ALPHAHASH
	const float ALPHA_HASH_SCALE = 0.05;
	float hash2D( vec2 value ) {
		return fract( 1.0e4 * sin( 17.0 * value.x + 0.1 * value.y ) * ( 0.1 + abs( sin( 13.0 * value.y + value.x ) ) ) );
	}
	float hash3D( vec3 value ) {
		return hash2D( vec2( hash2D( value.xy ), value.z ) );
	}
	float getAlphaHashThreshold( vec3 position ) {
		float maxDeriv = max(
			length( dFdx( position.xyz ) ),
			length( dFdy( position.xyz ) )
		);
		float pixScale = 1.0 / ( ALPHA_HASH_SCALE * maxDeriv );
		vec2 pixScales = vec2(
			exp2( floor( log2( pixScale ) ) ),
			exp2( ceil( log2( pixScale ) ) )
		);
		vec2 alpha = vec2(
			hash3D( floor( pixScales.x * position.xyz ) ),
			hash3D( floor( pixScales.y * position.xyz ) )
		);
		float lerpFactor = fract( log2( pixScale ) );
		float x = ( 1.0 - lerpFactor ) * alpha.x + lerpFactor * alpha.y;
		float a = min( lerpFactor, 1.0 - lerpFactor );
		vec3 cases = vec3(
			x * x / ( 2.0 * a * ( 1.0 - a ) ),
			( x - 0.5 * a ) / ( 1.0 - a ),
			1.0 - ( ( 1.0 - x ) * ( 1.0 - x ) / ( 2.0 * a * ( 1.0 - a ) ) )
		);
		float threshold = ( x < ( 1.0 - a ) )
			? ( ( x < a ) ? cases.x : cases.y )
			: cases.z;
		return clamp( threshold , 1.0e-6, 1.0 );
	}
#endif`,yd=`#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, vAlphaMapUv ).g;
#endif`,Md=`#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,bd=`#ifdef USE_ALPHATEST
	#ifdef ALPHA_TO_COVERAGE
	diffuseColor.a = smoothstep( alphaTest, alphaTest + fwidth( diffuseColor.a ), diffuseColor.a );
	if ( diffuseColor.a == 0.0 ) discard;
	#else
	if ( diffuseColor.a < alphaTest ) discard;
	#endif
#endif`,Sd=`#ifdef USE_ALPHATEST
	uniform float alphaTest;
#endif`,wd=`#ifdef USE_AOMAP
	float ambientOcclusion = ( texture2D( aoMap, vAoMapUv ).r - 1.0 ) * aoMapIntensity + 1.0;
	reflectedLight.indirectDiffuse *= ambientOcclusion;
	#if defined( USE_CLEARCOAT ) 
		clearcoatSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_SHEEN ) 
		sheenSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD )
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		reflectedLight.indirectSpecular *= computeSpecularOcclusion( dotNV, ambientOcclusion, material.roughness );
	#endif
#endif`,Ed=`#ifdef USE_AOMAP
	uniform sampler2D aoMap;
	uniform float aoMapIntensity;
#endif`,Td=`#ifdef USE_BATCHING
	#if ! defined( GL_ANGLE_multi_draw )
	#define gl_DrawID _gl_DrawID
	uniform int _gl_DrawID;
	#endif
	uniform highp sampler2D batchingTexture;
	uniform highp usampler2D batchingIdTexture;
	mat4 getBatchingMatrix( const in float i ) {
		int size = textureSize( batchingTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( batchingTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( batchingTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( batchingTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( batchingTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
	float getIndirectIndex( const in int i ) {
		int size = textureSize( batchingIdTexture, 0 ).x;
		int x = i % size;
		int y = i / size;
		return float( texelFetch( batchingIdTexture, ivec2( x, y ), 0 ).r );
	}
#endif
#ifdef USE_BATCHING_COLOR
	uniform sampler2D batchingColorTexture;
	vec3 getBatchingColor( const in float i ) {
		int size = textureSize( batchingColorTexture, 0 ).x;
		int j = int( i );
		int x = j % size;
		int y = j / size;
		return texelFetch( batchingColorTexture, ivec2( x, y ), 0 ).rgb;
	}
#endif`,Ad=`#ifdef USE_BATCHING
	mat4 batchingMatrix = getBatchingMatrix( getIndirectIndex( gl_DrawID ) );
#endif`,Rd=`vec3 transformed = vec3( position );
#ifdef USE_ALPHAHASH
	vPosition = vec3( position );
#endif`,Cd=`vec3 objectNormal = vec3( normal );
#ifdef USE_TANGENT
	vec3 objectTangent = vec3( tangent.xyz );
#endif`,Id=`float G_BlinnPhong_Implicit( ) {
	return 0.25;
}
float D_BlinnPhong( const in float shininess, const in float dotNH ) {
	return RECIPROCAL_PI * ( shininess * 0.5 + 1.0 ) * pow( dotNH, shininess );
}
vec3 BRDF_BlinnPhong( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 specularColor, const in float shininess ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( specularColor, 1.0, dotVH );
	float G = G_BlinnPhong_Implicit( );
	float D = D_BlinnPhong( shininess, dotNH );
	return F * ( G * D );
} // validated`,Pd=`#ifdef USE_IRIDESCENCE
	const mat3 XYZ_TO_REC709 = mat3(
		 3.2404542, -0.9692660,  0.0556434,
		-1.5371385,  1.8760108, -0.2040259,
		-0.4985314,  0.0415560,  1.0572252
	);
	vec3 Fresnel0ToIor( vec3 fresnel0 ) {
		vec3 sqrtF0 = sqrt( fresnel0 );
		return ( vec3( 1.0 ) + sqrtF0 ) / ( vec3( 1.0 ) - sqrtF0 );
	}
	vec3 IorToFresnel0( vec3 transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - vec3( incidentIor ) ) / ( transmittedIor + vec3( incidentIor ) ) );
	}
	float IorToFresnel0( float transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - incidentIor ) / ( transmittedIor + incidentIor ));
	}
	vec3 evalSensitivity( float OPD, vec3 shift ) {
		float phase = 2.0 * PI * OPD * 1.0e-9;
		vec3 val = vec3( 5.4856e-13, 4.4201e-13, 5.2481e-13 );
		vec3 pos = vec3( 1.6810e+06, 1.7953e+06, 2.2084e+06 );
		vec3 var = vec3( 4.3278e+09, 9.3046e+09, 6.6121e+09 );
		vec3 xyz = val * sqrt( 2.0 * PI * var ) * cos( pos * phase + shift ) * exp( - pow2( phase ) * var );
		xyz.x += 9.7470e-14 * sqrt( 2.0 * PI * 4.5282e+09 ) * cos( 2.2399e+06 * phase + shift[ 0 ] ) * exp( - 4.5282e+09 * pow2( phase ) );
		xyz /= 1.0685e-7;
		vec3 rgb = XYZ_TO_REC709 * xyz;
		return rgb;
	}
	vec3 evalIridescence( float outsideIOR, float eta2, float cosTheta1, float thinFilmThickness, vec3 baseF0 ) {
		vec3 I;
		float iridescenceIOR = mix( outsideIOR, eta2, smoothstep( 0.0, 0.03, thinFilmThickness ) );
		float sinTheta2Sq = pow2( outsideIOR / iridescenceIOR ) * ( 1.0 - pow2( cosTheta1 ) );
		float cosTheta2Sq = 1.0 - sinTheta2Sq;
		if ( cosTheta2Sq < 0.0 ) {
			return vec3( 1.0 );
		}
		float cosTheta2 = sqrt( cosTheta2Sq );
		float R0 = IorToFresnel0( iridescenceIOR, outsideIOR );
		float R12 = F_Schlick( R0, 1.0, cosTheta1 );
		float T121 = 1.0 - R12;
		float phi12 = 0.0;
		if ( iridescenceIOR < outsideIOR ) phi12 = PI;
		float phi21 = PI - phi12;
		vec3 baseIOR = Fresnel0ToIor( clamp( baseF0, 0.0, 0.9999 ) );		vec3 R1 = IorToFresnel0( baseIOR, iridescenceIOR );
		vec3 R23 = F_Schlick( R1, 1.0, cosTheta2 );
		vec3 phi23 = vec3( 0.0 );
		if ( baseIOR[ 0 ] < iridescenceIOR ) phi23[ 0 ] = PI;
		if ( baseIOR[ 1 ] < iridescenceIOR ) phi23[ 1 ] = PI;
		if ( baseIOR[ 2 ] < iridescenceIOR ) phi23[ 2 ] = PI;
		float OPD = 2.0 * iridescenceIOR * thinFilmThickness * cosTheta2;
		vec3 phi = vec3( phi21 ) + phi23;
		vec3 R123 = clamp( R12 * R23, 1e-5, 0.9999 );
		vec3 r123 = sqrt( R123 );
		vec3 Rs = pow2( T121 ) * R23 / ( vec3( 1.0 ) - R123 );
		vec3 C0 = R12 + Rs;
		I = C0;
		vec3 Cm = Rs - T121;
		for ( int m = 1; m <= 2; ++ m ) {
			Cm *= r123;
			vec3 Sm = 2.0 * evalSensitivity( float( m ) * OPD, float( m ) * phi );
			I += Cm * Sm;
		}
		return max( I, vec3( 0.0 ) );
	}
#endif`,Ld=`#ifdef USE_BUMPMAP
	uniform sampler2D bumpMap;
	uniform float bumpScale;
	vec2 dHdxy_fwd() {
		vec2 dSTdx = dFdx( vBumpMapUv );
		vec2 dSTdy = dFdy( vBumpMapUv );
		float Hll = bumpScale * texture2D( bumpMap, vBumpMapUv ).x;
		float dBx = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdx ).x - Hll;
		float dBy = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdy ).x - Hll;
		return vec2( dBx, dBy );
	}
	vec3 perturbNormalArb( vec3 surf_pos, vec3 surf_norm, vec2 dHdxy, float faceDirection ) {
		vec3 vSigmaX = normalize( dFdx( surf_pos.xyz ) );
		vec3 vSigmaY = normalize( dFdy( surf_pos.xyz ) );
		vec3 vN = surf_norm;
		vec3 R1 = cross( vSigmaY, vN );
		vec3 R2 = cross( vN, vSigmaX );
		float fDet = dot( vSigmaX, R1 ) * faceDirection;
		vec3 vGrad = sign( fDet ) * ( dHdxy.x * R1 + dHdxy.y * R2 );
		return normalize( abs( fDet ) * surf_norm - vGrad );
	}
#endif`,Dd=`#if NUM_CLIPPING_PLANES > 0
	vec4 plane;
	#ifdef ALPHA_TO_COVERAGE
		float distanceToPlane, distanceGradient;
		float clipOpacity = 1.0;
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
			distanceGradient = fwidth( distanceToPlane ) / 2.0;
			clipOpacity *= smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			if ( clipOpacity == 0.0 ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			float unionClipOpacity = 1.0;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
				distanceGradient = fwidth( distanceToPlane ) / 2.0;
				unionClipOpacity *= 1.0 - smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			}
			#pragma unroll_loop_end
			clipOpacity *= 1.0 - unionClipOpacity;
		#endif
		diffuseColor.a *= clipOpacity;
		if ( diffuseColor.a == 0.0 ) discard;
	#else
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			if ( dot( vClipPosition, plane.xyz ) > plane.w ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			bool clipped = true;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				clipped = ( dot( vClipPosition, plane.xyz ) > plane.w ) && clipped;
			}
			#pragma unroll_loop_end
			if ( clipped ) discard;
		#endif
	#endif
#endif`,Ud=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
	uniform vec4 clippingPlanes[ NUM_CLIPPING_PLANES ];
#endif`,Nd=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
#endif`,Fd=`#if NUM_CLIPPING_PLANES > 0
	vClipPosition = - mvPosition.xyz;
#endif`,Od=`#if defined( USE_COLOR_ALPHA )
	diffuseColor *= vColor;
#elif defined( USE_COLOR )
	diffuseColor.rgb *= vColor;
#endif`,Bd=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR )
	varying vec3 vColor;
#endif`,zd=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	varying vec3 vColor;
#endif`,kd=`#if defined( USE_COLOR_ALPHA )
	vColor = vec4( 1.0 );
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	vColor = vec3( 1.0 );
#endif
#ifdef USE_COLOR
	vColor *= color;
#endif
#ifdef USE_INSTANCING_COLOR
	vColor.xyz *= instanceColor.xyz;
#endif
#ifdef USE_BATCHING_COLOR
	vec3 batchingColor = getBatchingColor( getIndirectIndex( gl_DrawID ) );
	vColor.xyz *= batchingColor.xyz;
#endif`,Hd=`#define PI 3.141592653589793
#define PI2 6.283185307179586
#define PI_HALF 1.5707963267948966
#define RECIPROCAL_PI 0.3183098861837907
#define RECIPROCAL_PI2 0.15915494309189535
#define EPSILON 1e-6
#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
#define whiteComplement( a ) ( 1.0 - saturate( a ) )
float pow2( const in float x ) { return x*x; }
vec3 pow2( const in vec3 x ) { return x*x; }
float pow3( const in float x ) { return x*x*x; }
float pow4( const in float x ) { float x2 = x*x; return x2*x2; }
float max3( const in vec3 v ) { return max( max( v.x, v.y ), v.z ); }
float average( const in vec3 v ) { return dot( v, vec3( 0.3333333 ) ); }
highp float rand( const in vec2 uv ) {
	const highp float a = 12.9898, b = 78.233, c = 43758.5453;
	highp float dt = dot( uv.xy, vec2( a,b ) ), sn = mod( dt, PI );
	return fract( sin( sn ) * c );
}
#ifdef HIGH_PRECISION
	float precisionSafeLength( vec3 v ) { return length( v ); }
#else
	float precisionSafeLength( vec3 v ) {
		float maxComponent = max3( abs( v ) );
		return length( v / maxComponent ) * maxComponent;
	}
#endif
struct IncidentLight {
	vec3 color;
	vec3 direction;
	bool visible;
};
struct ReflectedLight {
	vec3 directDiffuse;
	vec3 directSpecular;
	vec3 indirectDiffuse;
	vec3 indirectSpecular;
};
#ifdef USE_ALPHAHASH
	varying vec3 vPosition;
#endif
vec3 transformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );
}
vec3 inverseTransformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( vec4( dir, 0.0 ) * matrix ).xyz );
}
mat3 transposeMat3( const in mat3 m ) {
	mat3 tmp;
	tmp[ 0 ] = vec3( m[ 0 ].x, m[ 1 ].x, m[ 2 ].x );
	tmp[ 1 ] = vec3( m[ 0 ].y, m[ 1 ].y, m[ 2 ].y );
	tmp[ 2 ] = vec3( m[ 0 ].z, m[ 1 ].z, m[ 2 ].z );
	return tmp;
}
bool isPerspectiveMatrix( mat4 m ) {
	return m[ 2 ][ 3 ] == - 1.0;
}
vec2 equirectUv( in vec3 dir ) {
	float u = atan( dir.z, dir.x ) * RECIPROCAL_PI2 + 0.5;
	float v = asin( clamp( dir.y, - 1.0, 1.0 ) ) * RECIPROCAL_PI + 0.5;
	return vec2( u, v );
}
vec3 BRDF_Lambert( const in vec3 diffuseColor ) {
	return RECIPROCAL_PI * diffuseColor;
}
vec3 F_Schlick( const in vec3 f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
}
float F_Schlick( const in float f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
} // validated`,Vd=`#ifdef ENVMAP_TYPE_CUBE_UV
	#define cubeUV_minMipLevel 4.0
	#define cubeUV_minTileSize 16.0
	float getFace( vec3 direction ) {
		vec3 absDirection = abs( direction );
		float face = - 1.0;
		if ( absDirection.x > absDirection.z ) {
			if ( absDirection.x > absDirection.y )
				face = direction.x > 0.0 ? 0.0 : 3.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		} else {
			if ( absDirection.z > absDirection.y )
				face = direction.z > 0.0 ? 2.0 : 5.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		}
		return face;
	}
	vec2 getUV( vec3 direction, float face ) {
		vec2 uv;
		if ( face == 0.0 ) {
			uv = vec2( direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 1.0 ) {
			uv = vec2( - direction.x, - direction.z ) / abs( direction.y );
		} else if ( face == 2.0 ) {
			uv = vec2( - direction.x, direction.y ) / abs( direction.z );
		} else if ( face == 3.0 ) {
			uv = vec2( - direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 4.0 ) {
			uv = vec2( - direction.x, direction.z ) / abs( direction.y );
		} else {
			uv = vec2( direction.x, direction.y ) / abs( direction.z );
		}
		return 0.5 * ( uv + 1.0 );
	}
	vec3 bilinearCubeUV( sampler2D envMap, vec3 direction, float mipInt ) {
		float face = getFace( direction );
		float filterInt = max( cubeUV_minMipLevel - mipInt, 0.0 );
		mipInt = max( mipInt, cubeUV_minMipLevel );
		float faceSize = exp2( mipInt );
		highp vec2 uv = getUV( direction, face ) * ( faceSize - 2.0 ) + 1.0;
		if ( face > 2.0 ) {
			uv.y += faceSize;
			face -= 3.0;
		}
		uv.x += face * faceSize;
		uv.x += filterInt * 3.0 * cubeUV_minTileSize;
		uv.y += 4.0 * ( exp2( CUBEUV_MAX_MIP ) - faceSize );
		uv.x *= CUBEUV_TEXEL_WIDTH;
		uv.y *= CUBEUV_TEXEL_HEIGHT;
		#ifdef texture2DGradEXT
			return texture2DGradEXT( envMap, uv, vec2( 0.0 ), vec2( 0.0 ) ).rgb;
		#else
			return texture2D( envMap, uv ).rgb;
		#endif
	}
	#define cubeUV_r0 1.0
	#define cubeUV_m0 - 2.0
	#define cubeUV_r1 0.8
	#define cubeUV_m1 - 1.0
	#define cubeUV_r4 0.4
	#define cubeUV_m4 2.0
	#define cubeUV_r5 0.305
	#define cubeUV_m5 3.0
	#define cubeUV_r6 0.21
	#define cubeUV_m6 4.0
	float roughnessToMip( float roughness ) {
		float mip = 0.0;
		if ( roughness >= cubeUV_r1 ) {
			mip = ( cubeUV_r0 - roughness ) * ( cubeUV_m1 - cubeUV_m0 ) / ( cubeUV_r0 - cubeUV_r1 ) + cubeUV_m0;
		} else if ( roughness >= cubeUV_r4 ) {
			mip = ( cubeUV_r1 - roughness ) * ( cubeUV_m4 - cubeUV_m1 ) / ( cubeUV_r1 - cubeUV_r4 ) + cubeUV_m1;
		} else if ( roughness >= cubeUV_r5 ) {
			mip = ( cubeUV_r4 - roughness ) * ( cubeUV_m5 - cubeUV_m4 ) / ( cubeUV_r4 - cubeUV_r5 ) + cubeUV_m4;
		} else if ( roughness >= cubeUV_r6 ) {
			mip = ( cubeUV_r5 - roughness ) * ( cubeUV_m6 - cubeUV_m5 ) / ( cubeUV_r5 - cubeUV_r6 ) + cubeUV_m5;
		} else {
			mip = - 2.0 * log2( 1.16 * roughness );		}
		return mip;
	}
	vec4 textureCubeUV( sampler2D envMap, vec3 sampleDir, float roughness ) {
		float mip = clamp( roughnessToMip( roughness ), cubeUV_m0, CUBEUV_MAX_MIP );
		float mipF = fract( mip );
		float mipInt = floor( mip );
		vec3 color0 = bilinearCubeUV( envMap, sampleDir, mipInt );
		if ( mipF == 0.0 ) {
			return vec4( color0, 1.0 );
		} else {
			vec3 color1 = bilinearCubeUV( envMap, sampleDir, mipInt + 1.0 );
			return vec4( mix( color0, color1, mipF ), 1.0 );
		}
	}
#endif`,Gd=`vec3 transformedNormal = objectNormal;
#ifdef USE_TANGENT
	vec3 transformedTangent = objectTangent;
#endif
#ifdef USE_BATCHING
	mat3 bm = mat3( batchingMatrix );
	transformedNormal /= vec3( dot( bm[ 0 ], bm[ 0 ] ), dot( bm[ 1 ], bm[ 1 ] ), dot( bm[ 2 ], bm[ 2 ] ) );
	transformedNormal = bm * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = bm * transformedTangent;
	#endif
#endif
#ifdef USE_INSTANCING
	mat3 im = mat3( instanceMatrix );
	transformedNormal /= vec3( dot( im[ 0 ], im[ 0 ] ), dot( im[ 1 ], im[ 1 ] ), dot( im[ 2 ], im[ 2 ] ) );
	transformedNormal = im * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = im * transformedTangent;
	#endif
#endif
transformedNormal = normalMatrix * transformedNormal;
#ifdef FLIP_SIDED
	transformedNormal = - transformedNormal;
#endif
#ifdef USE_TANGENT
	transformedTangent = ( modelViewMatrix * vec4( transformedTangent, 0.0 ) ).xyz;
	#ifdef FLIP_SIDED
		transformedTangent = - transformedTangent;
	#endif
#endif`,Wd=`#ifdef USE_DISPLACEMENTMAP
	uniform sampler2D displacementMap;
	uniform float displacementScale;
	uniform float displacementBias;
#endif`,Xd=`#ifdef USE_DISPLACEMENTMAP
	transformed += normalize( objectNormal ) * ( texture2D( displacementMap, vDisplacementMapUv ).x * displacementScale + displacementBias );
#endif`,qd=`#ifdef USE_EMISSIVEMAP
	vec4 emissiveColor = texture2D( emissiveMap, vEmissiveMapUv );
	#ifdef DECODE_VIDEO_TEXTURE_EMISSIVE
		emissiveColor = sRGBTransferEOTF( emissiveColor );
	#endif
	totalEmissiveRadiance *= emissiveColor.rgb;
#endif`,Yd=`#ifdef USE_EMISSIVEMAP
	uniform sampler2D emissiveMap;
#endif`,$d="gl_FragColor = linearToOutputTexel( gl_FragColor );",Zd=`vec4 LinearTransferOETF( in vec4 value ) {
	return value;
}
vec4 sRGBTransferEOTF( in vec4 value ) {
	return vec4( mix( pow( value.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), value.rgb * 0.0773993808, vec3( lessThanEqual( value.rgb, vec3( 0.04045 ) ) ) ), value.a );
}
vec4 sRGBTransferOETF( in vec4 value ) {
	return vec4( mix( pow( value.rgb, vec3( 0.41666 ) ) * 1.055 - vec3( 0.055 ), value.rgb * 12.92, vec3( lessThanEqual( value.rgb, vec3( 0.0031308 ) ) ) ), value.a );
}`,Kd=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vec3 cameraToFrag;
		if ( isOrthographic ) {
			cameraToFrag = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToFrag = normalize( vWorldPosition - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vec3 reflectVec = reflect( cameraToFrag, worldNormal );
		#else
			vec3 reflectVec = refract( cameraToFrag, worldNormal, refractionRatio );
		#endif
	#else
		vec3 reflectVec = vReflect;
	#endif
	#ifdef ENVMAP_TYPE_CUBE
		vec4 envColor = textureCube( envMap, envMapRotation * vec3( flipEnvMap * reflectVec.x, reflectVec.yz ) );
	#else
		vec4 envColor = vec4( 0.0 );
	#endif
	#ifdef ENVMAP_BLENDING_MULTIPLY
		outgoingLight = mix( outgoingLight, outgoingLight * envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_MIX )
		outgoingLight = mix( outgoingLight, envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_ADD )
		outgoingLight += envColor.xyz * specularStrength * reflectivity;
	#endif
#endif`,Jd=`#ifdef USE_ENVMAP
	uniform float envMapIntensity;
	uniform float flipEnvMap;
	uniform mat3 envMapRotation;
	#ifdef ENVMAP_TYPE_CUBE
		uniform samplerCube envMap;
	#else
		uniform sampler2D envMap;
	#endif
	
#endif`,jd=`#ifdef USE_ENVMAP
	uniform float reflectivity;
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		varying vec3 vWorldPosition;
		uniform float refractionRatio;
	#else
		varying vec3 vReflect;
	#endif
#endif`,Qd=`#ifdef USE_ENVMAP
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		
		varying vec3 vWorldPosition;
	#else
		varying vec3 vReflect;
		uniform float refractionRatio;
	#endif
#endif`,ep=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vWorldPosition = worldPosition.xyz;
	#else
		vec3 cameraToVertex;
		if ( isOrthographic ) {
			cameraToVertex = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToVertex = normalize( worldPosition.xyz - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vReflect = reflect( cameraToVertex, worldNormal );
		#else
			vReflect = refract( cameraToVertex, worldNormal, refractionRatio );
		#endif
	#endif
#endif`,tp=`#ifdef USE_FOG
	vFogDepth = - mvPosition.z;
#endif`,np=`#ifdef USE_FOG
	varying float vFogDepth;
#endif`,ip=`#ifdef USE_FOG
	#ifdef FOG_EXP2
		float fogFactor = 1.0 - exp( - fogDensity * fogDensity * vFogDepth * vFogDepth );
	#else
		float fogFactor = smoothstep( fogNear, fogFar, vFogDepth );
	#endif
	gl_FragColor.rgb = mix( gl_FragColor.rgb, fogColor, fogFactor );
#endif`,sp=`#ifdef USE_FOG
	uniform vec3 fogColor;
	varying float vFogDepth;
	#ifdef FOG_EXP2
		uniform float fogDensity;
	#else
		uniform float fogNear;
		uniform float fogFar;
	#endif
#endif`,rp=`#ifdef USE_GRADIENTMAP
	uniform sampler2D gradientMap;
#endif
vec3 getGradientIrradiance( vec3 normal, vec3 lightDirection ) {
	float dotNL = dot( normal, lightDirection );
	vec2 coord = vec2( dotNL * 0.5 + 0.5, 0.0 );
	#ifdef USE_GRADIENTMAP
		return vec3( texture2D( gradientMap, coord ).r );
	#else
		vec2 fw = fwidth( coord ) * 0.5;
		return mix( vec3( 0.7 ), vec3( 1.0 ), smoothstep( 0.7 - fw.x, 0.7 + fw.x, coord.x ) );
	#endif
}`,op=`#ifdef USE_LIGHTMAP
	uniform sampler2D lightMap;
	uniform float lightMapIntensity;
#endif`,ap=`LambertMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularStrength = specularStrength;`,cp=`varying vec3 vViewPosition;
struct LambertMaterial {
	vec3 diffuseColor;
	float specularStrength;
};
void RE_Direct_Lambert( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Lambert( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Lambert
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Lambert`,lp=`uniform bool receiveShadow;
uniform vec3 ambientLightColor;
#if defined( USE_LIGHT_PROBES )
	uniform vec3 lightProbe[ 9 ];
#endif
vec3 shGetIrradianceAt( in vec3 normal, in vec3 shCoefficients[ 9 ] ) {
	float x = normal.x, y = normal.y, z = normal.z;
	vec3 result = shCoefficients[ 0 ] * 0.886227;
	result += shCoefficients[ 1 ] * 2.0 * 0.511664 * y;
	result += shCoefficients[ 2 ] * 2.0 * 0.511664 * z;
	result += shCoefficients[ 3 ] * 2.0 * 0.511664 * x;
	result += shCoefficients[ 4 ] * 2.0 * 0.429043 * x * y;
	result += shCoefficients[ 5 ] * 2.0 * 0.429043 * y * z;
	result += shCoefficients[ 6 ] * ( 0.743125 * z * z - 0.247708 );
	result += shCoefficients[ 7 ] * 2.0 * 0.429043 * x * z;
	result += shCoefficients[ 8 ] * 0.429043 * ( x * x - y * y );
	return result;
}
vec3 getLightProbeIrradiance( const in vec3 lightProbe[ 9 ], const in vec3 normal ) {
	vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
	vec3 irradiance = shGetIrradianceAt( worldNormal, lightProbe );
	return irradiance;
}
vec3 getAmbientLightIrradiance( const in vec3 ambientLightColor ) {
	vec3 irradiance = ambientLightColor;
	return irradiance;
}
float getDistanceAttenuation( const in float lightDistance, const in float cutoffDistance, const in float decayExponent ) {
	float distanceFalloff = 1.0 / max( pow( lightDistance, decayExponent ), 0.01 );
	if ( cutoffDistance > 0.0 ) {
		distanceFalloff *= pow2( saturate( 1.0 - pow4( lightDistance / cutoffDistance ) ) );
	}
	return distanceFalloff;
}
float getSpotAttenuation( const in float coneCosine, const in float penumbraCosine, const in float angleCosine ) {
	return smoothstep( coneCosine, penumbraCosine, angleCosine );
}
#if NUM_DIR_LIGHTS > 0
	struct DirectionalLight {
		vec3 direction;
		vec3 color;
	};
	uniform DirectionalLight directionalLights[ NUM_DIR_LIGHTS ];
	void getDirectionalLightInfo( const in DirectionalLight directionalLight, out IncidentLight light ) {
		light.color = directionalLight.color;
		light.direction = directionalLight.direction;
		light.visible = true;
	}
#endif
#if NUM_POINT_LIGHTS > 0
	struct PointLight {
		vec3 position;
		vec3 color;
		float distance;
		float decay;
	};
	uniform PointLight pointLights[ NUM_POINT_LIGHTS ];
	void getPointLightInfo( const in PointLight pointLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = pointLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float lightDistance = length( lVector );
		light.color = pointLight.color;
		light.color *= getDistanceAttenuation( lightDistance, pointLight.distance, pointLight.decay );
		light.visible = ( light.color != vec3( 0.0 ) );
	}
#endif
#if NUM_SPOT_LIGHTS > 0
	struct SpotLight {
		vec3 position;
		vec3 direction;
		vec3 color;
		float distance;
		float decay;
		float coneCos;
		float penumbraCos;
	};
	uniform SpotLight spotLights[ NUM_SPOT_LIGHTS ];
	void getSpotLightInfo( const in SpotLight spotLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = spotLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float angleCos = dot( light.direction, spotLight.direction );
		float spotAttenuation = getSpotAttenuation( spotLight.coneCos, spotLight.penumbraCos, angleCos );
		if ( spotAttenuation > 0.0 ) {
			float lightDistance = length( lVector );
			light.color = spotLight.color * spotAttenuation;
			light.color *= getDistanceAttenuation( lightDistance, spotLight.distance, spotLight.decay );
			light.visible = ( light.color != vec3( 0.0 ) );
		} else {
			light.color = vec3( 0.0 );
			light.visible = false;
		}
	}
#endif
#if NUM_RECT_AREA_LIGHTS > 0
	struct RectAreaLight {
		vec3 color;
		vec3 position;
		vec3 halfWidth;
		vec3 halfHeight;
	};
	uniform sampler2D ltc_1;	uniform sampler2D ltc_2;
	uniform RectAreaLight rectAreaLights[ NUM_RECT_AREA_LIGHTS ];
#endif
#if NUM_HEMI_LIGHTS > 0
	struct HemisphereLight {
		vec3 direction;
		vec3 skyColor;
		vec3 groundColor;
	};
	uniform HemisphereLight hemisphereLights[ NUM_HEMI_LIGHTS ];
	vec3 getHemisphereLightIrradiance( const in HemisphereLight hemiLight, const in vec3 normal ) {
		float dotNL = dot( normal, hemiLight.direction );
		float hemiDiffuseWeight = 0.5 * dotNL + 0.5;
		vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight );
		return irradiance;
	}
#endif`,up=`#ifdef USE_ENVMAP
	vec3 getIBLIrradiance( const in vec3 normal ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, envMapRotation * worldNormal, 1.0 );
			return PI * envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	vec3 getIBLRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 reflectVec = reflect( - viewDir, normal );
			reflectVec = normalize( mix( reflectVec, normal, roughness * roughness) );
			reflectVec = inverseTransformDirection( reflectVec, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, envMapRotation * reflectVec, roughness );
			return envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	#ifdef USE_ANISOTROPY
		vec3 getIBLAnisotropyRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
			#ifdef ENVMAP_TYPE_CUBE_UV
				vec3 bentNormal = cross( bitangent, viewDir );
				bentNormal = normalize( cross( bentNormal, bitangent ) );
				bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
				return getIBLRadiance( viewDir, bentNormal, roughness );
			#else
				return vec3( 0.0 );
			#endif
		}
	#endif
#endif`,hp=`ToonMaterial material;
material.diffuseColor = diffuseColor.rgb;`,fp=`varying vec3 vViewPosition;
struct ToonMaterial {
	vec3 diffuseColor;
};
void RE_Direct_Toon( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 irradiance = getGradientIrradiance( geometryNormal, directLight.direction ) * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Toon( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Toon
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Toon`,dp=`BlinnPhongMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularColor = specular;
material.specularShininess = shininess;
material.specularStrength = specularStrength;`,pp=`varying vec3 vViewPosition;
struct BlinnPhongMaterial {
	vec3 diffuseColor;
	vec3 specularColor;
	float specularShininess;
	float specularStrength;
};
void RE_Direct_BlinnPhong( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
	reflectedLight.directSpecular += irradiance * BRDF_BlinnPhong( directLight.direction, geometryViewDir, geometryNormal, material.specularColor, material.specularShininess ) * material.specularStrength;
}
void RE_IndirectDiffuse_BlinnPhong( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_BlinnPhong
#define RE_IndirectDiffuse		RE_IndirectDiffuse_BlinnPhong`,mp=`PhysicalMaterial material;
material.diffuseColor = diffuseColor.rgb * ( 1.0 - metalnessFactor );
vec3 dxy = max( abs( dFdx( nonPerturbedNormal ) ), abs( dFdy( nonPerturbedNormal ) ) );
float geometryRoughness = max( max( dxy.x, dxy.y ), dxy.z );
material.roughness = max( roughnessFactor, 0.0525 );material.roughness += geometryRoughness;
material.roughness = min( material.roughness, 1.0 );
#ifdef IOR
	material.ior = ior;
	#ifdef USE_SPECULAR
		float specularIntensityFactor = specularIntensity;
		vec3 specularColorFactor = specularColor;
		#ifdef USE_SPECULAR_COLORMAP
			specularColorFactor *= texture2D( specularColorMap, vSpecularColorMapUv ).rgb;
		#endif
		#ifdef USE_SPECULAR_INTENSITYMAP
			specularIntensityFactor *= texture2D( specularIntensityMap, vSpecularIntensityMapUv ).a;
		#endif
		material.specularF90 = mix( specularIntensityFactor, 1.0, metalnessFactor );
	#else
		float specularIntensityFactor = 1.0;
		vec3 specularColorFactor = vec3( 1.0 );
		material.specularF90 = 1.0;
	#endif
	material.specularColor = mix( min( pow2( ( material.ior - 1.0 ) / ( material.ior + 1.0 ) ) * specularColorFactor, vec3( 1.0 ) ) * specularIntensityFactor, diffuseColor.rgb, metalnessFactor );
#else
	material.specularColor = mix( vec3( 0.04 ), diffuseColor.rgb, metalnessFactor );
	material.specularF90 = 1.0;
#endif
#ifdef USE_CLEARCOAT
	material.clearcoat = clearcoat;
	material.clearcoatRoughness = clearcoatRoughness;
	material.clearcoatF0 = vec3( 0.04 );
	material.clearcoatF90 = 1.0;
	#ifdef USE_CLEARCOATMAP
		material.clearcoat *= texture2D( clearcoatMap, vClearcoatMapUv ).x;
	#endif
	#ifdef USE_CLEARCOAT_ROUGHNESSMAP
		material.clearcoatRoughness *= texture2D( clearcoatRoughnessMap, vClearcoatRoughnessMapUv ).y;
	#endif
	material.clearcoat = saturate( material.clearcoat );	material.clearcoatRoughness = max( material.clearcoatRoughness, 0.0525 );
	material.clearcoatRoughness += geometryRoughness;
	material.clearcoatRoughness = min( material.clearcoatRoughness, 1.0 );
#endif
#ifdef USE_DISPERSION
	material.dispersion = dispersion;
#endif
#ifdef USE_IRIDESCENCE
	material.iridescence = iridescence;
	material.iridescenceIOR = iridescenceIOR;
	#ifdef USE_IRIDESCENCEMAP
		material.iridescence *= texture2D( iridescenceMap, vIridescenceMapUv ).r;
	#endif
	#ifdef USE_IRIDESCENCE_THICKNESSMAP
		material.iridescenceThickness = (iridescenceThicknessMaximum - iridescenceThicknessMinimum) * texture2D( iridescenceThicknessMap, vIridescenceThicknessMapUv ).g + iridescenceThicknessMinimum;
	#else
		material.iridescenceThickness = iridescenceThicknessMaximum;
	#endif
#endif
#ifdef USE_SHEEN
	material.sheenColor = sheenColor;
	#ifdef USE_SHEEN_COLORMAP
		material.sheenColor *= texture2D( sheenColorMap, vSheenColorMapUv ).rgb;
	#endif
	material.sheenRoughness = clamp( sheenRoughness, 0.07, 1.0 );
	#ifdef USE_SHEEN_ROUGHNESSMAP
		material.sheenRoughness *= texture2D( sheenRoughnessMap, vSheenRoughnessMapUv ).a;
	#endif
#endif
#ifdef USE_ANISOTROPY
	#ifdef USE_ANISOTROPYMAP
		mat2 anisotropyMat = mat2( anisotropyVector.x, anisotropyVector.y, - anisotropyVector.y, anisotropyVector.x );
		vec3 anisotropyPolar = texture2D( anisotropyMap, vAnisotropyMapUv ).rgb;
		vec2 anisotropyV = anisotropyMat * normalize( 2.0 * anisotropyPolar.rg - vec2( 1.0 ) ) * anisotropyPolar.b;
	#else
		vec2 anisotropyV = anisotropyVector;
	#endif
	material.anisotropy = length( anisotropyV );
	if( material.anisotropy == 0.0 ) {
		anisotropyV = vec2( 1.0, 0.0 );
	} else {
		anisotropyV /= material.anisotropy;
		material.anisotropy = saturate( material.anisotropy );
	}
	material.alphaT = mix( pow2( material.roughness ), 1.0, pow2( material.anisotropy ) );
	material.anisotropyT = tbn[ 0 ] * anisotropyV.x + tbn[ 1 ] * anisotropyV.y;
	material.anisotropyB = tbn[ 1 ] * anisotropyV.x - tbn[ 0 ] * anisotropyV.y;
#endif`,gp=`struct PhysicalMaterial {
	vec3 diffuseColor;
	float roughness;
	vec3 specularColor;
	float specularF90;
	float dispersion;
	#ifdef USE_CLEARCOAT
		float clearcoat;
		float clearcoatRoughness;
		vec3 clearcoatF0;
		float clearcoatF90;
	#endif
	#ifdef USE_IRIDESCENCE
		float iridescence;
		float iridescenceIOR;
		float iridescenceThickness;
		vec3 iridescenceFresnel;
		vec3 iridescenceF0;
	#endif
	#ifdef USE_SHEEN
		vec3 sheenColor;
		float sheenRoughness;
	#endif
	#ifdef IOR
		float ior;
	#endif
	#ifdef USE_TRANSMISSION
		float transmission;
		float transmissionAlpha;
		float thickness;
		float attenuationDistance;
		vec3 attenuationColor;
	#endif
	#ifdef USE_ANISOTROPY
		float anisotropy;
		float alphaT;
		vec3 anisotropyT;
		vec3 anisotropyB;
	#endif
};
vec3 clearcoatSpecularDirect = vec3( 0.0 );
vec3 clearcoatSpecularIndirect = vec3( 0.0 );
vec3 sheenSpecularDirect = vec3( 0.0 );
vec3 sheenSpecularIndirect = vec3(0.0 );
vec3 Schlick_to_F0( const in vec3 f, const in float f90, const in float dotVH ) {
    float x = clamp( 1.0 - dotVH, 0.0, 1.0 );
    float x2 = x * x;
    float x5 = clamp( x * x2 * x2, 0.0, 0.9999 );
    return ( f - vec3( f90 ) * x5 ) / ( 1.0 - x5 );
}
float V_GGX_SmithCorrelated( const in float alpha, const in float dotNL, const in float dotNV ) {
	float a2 = pow2( alpha );
	float gv = dotNL * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNV ) );
	float gl = dotNV * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNL ) );
	return 0.5 / max( gv + gl, EPSILON );
}
float D_GGX( const in float alpha, const in float dotNH ) {
	float a2 = pow2( alpha );
	float denom = pow2( dotNH ) * ( a2 - 1.0 ) + 1.0;
	return RECIPROCAL_PI * a2 / pow2( denom );
}
#ifdef USE_ANISOTROPY
	float V_GGX_SmithCorrelated_Anisotropic( const in float alphaT, const in float alphaB, const in float dotTV, const in float dotBV, const in float dotTL, const in float dotBL, const in float dotNV, const in float dotNL ) {
		float gv = dotNL * length( vec3( alphaT * dotTV, alphaB * dotBV, dotNV ) );
		float gl = dotNV * length( vec3( alphaT * dotTL, alphaB * dotBL, dotNL ) );
		float v = 0.5 / ( gv + gl );
		return saturate(v);
	}
	float D_GGX_Anisotropic( const in float alphaT, const in float alphaB, const in float dotNH, const in float dotTH, const in float dotBH ) {
		float a2 = alphaT * alphaB;
		highp vec3 v = vec3( alphaB * dotTH, alphaT * dotBH, a2 * dotNH );
		highp float v2 = dot( v, v );
		float w2 = a2 / v2;
		return RECIPROCAL_PI * a2 * pow2 ( w2 );
	}
#endif
#ifdef USE_CLEARCOAT
	vec3 BRDF_GGX_Clearcoat( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material) {
		vec3 f0 = material.clearcoatF0;
		float f90 = material.clearcoatF90;
		float roughness = material.clearcoatRoughness;
		float alpha = pow2( roughness );
		vec3 halfDir = normalize( lightDir + viewDir );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float dotNH = saturate( dot( normal, halfDir ) );
		float dotVH = saturate( dot( viewDir, halfDir ) );
		vec3 F = F_Schlick( f0, f90, dotVH );
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
		return F * ( V * D );
	}
#endif
vec3 BRDF_GGX( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material ) {
	vec3 f0 = material.specularColor;
	float f90 = material.specularF90;
	float roughness = material.roughness;
	float alpha = pow2( roughness );
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( f0, f90, dotVH );
	#ifdef USE_IRIDESCENCE
		F = mix( F, material.iridescenceFresnel, material.iridescence );
	#endif
	#ifdef USE_ANISOTROPY
		float dotTL = dot( material.anisotropyT, lightDir );
		float dotTV = dot( material.anisotropyT, viewDir );
		float dotTH = dot( material.anisotropyT, halfDir );
		float dotBL = dot( material.anisotropyB, lightDir );
		float dotBV = dot( material.anisotropyB, viewDir );
		float dotBH = dot( material.anisotropyB, halfDir );
		float V = V_GGX_SmithCorrelated_Anisotropic( material.alphaT, alpha, dotTV, dotBV, dotTL, dotBL, dotNV, dotNL );
		float D = D_GGX_Anisotropic( material.alphaT, alpha, dotNH, dotTH, dotBH );
	#else
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
	#endif
	return F * ( V * D );
}
vec2 LTC_Uv( const in vec3 N, const in vec3 V, const in float roughness ) {
	const float LUT_SIZE = 64.0;
	const float LUT_SCALE = ( LUT_SIZE - 1.0 ) / LUT_SIZE;
	const float LUT_BIAS = 0.5 / LUT_SIZE;
	float dotNV = saturate( dot( N, V ) );
	vec2 uv = vec2( roughness, sqrt( 1.0 - dotNV ) );
	uv = uv * LUT_SCALE + LUT_BIAS;
	return uv;
}
float LTC_ClippedSphereFormFactor( const in vec3 f ) {
	float l = length( f );
	return max( ( l * l + f.z ) / ( l + 1.0 ), 0.0 );
}
vec3 LTC_EdgeVectorFormFactor( const in vec3 v1, const in vec3 v2 ) {
	float x = dot( v1, v2 );
	float y = abs( x );
	float a = 0.8543985 + ( 0.4965155 + 0.0145206 * y ) * y;
	float b = 3.4175940 + ( 4.1616724 + y ) * y;
	float v = a / b;
	float theta_sintheta = ( x > 0.0 ) ? v : 0.5 * inversesqrt( max( 1.0 - x * x, 1e-7 ) ) - v;
	return cross( v1, v2 ) * theta_sintheta;
}
vec3 LTC_Evaluate( const in vec3 N, const in vec3 V, const in vec3 P, const in mat3 mInv, const in vec3 rectCoords[ 4 ] ) {
	vec3 v1 = rectCoords[ 1 ] - rectCoords[ 0 ];
	vec3 v2 = rectCoords[ 3 ] - rectCoords[ 0 ];
	vec3 lightNormal = cross( v1, v2 );
	if( dot( lightNormal, P - rectCoords[ 0 ] ) < 0.0 ) return vec3( 0.0 );
	vec3 T1, T2;
	T1 = normalize( V - N * dot( V, N ) );
	T2 = - cross( N, T1 );
	mat3 mat = mInv * transposeMat3( mat3( T1, T2, N ) );
	vec3 coords[ 4 ];
	coords[ 0 ] = mat * ( rectCoords[ 0 ] - P );
	coords[ 1 ] = mat * ( rectCoords[ 1 ] - P );
	coords[ 2 ] = mat * ( rectCoords[ 2 ] - P );
	coords[ 3 ] = mat * ( rectCoords[ 3 ] - P );
	coords[ 0 ] = normalize( coords[ 0 ] );
	coords[ 1 ] = normalize( coords[ 1 ] );
	coords[ 2 ] = normalize( coords[ 2 ] );
	coords[ 3 ] = normalize( coords[ 3 ] );
	vec3 vectorFormFactor = vec3( 0.0 );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 0 ], coords[ 1 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 1 ], coords[ 2 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 2 ], coords[ 3 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 3 ], coords[ 0 ] );
	float result = LTC_ClippedSphereFormFactor( vectorFormFactor );
	return vec3( result );
}
#if defined( USE_SHEEN )
float D_Charlie( float roughness, float dotNH ) {
	float alpha = pow2( roughness );
	float invAlpha = 1.0 / alpha;
	float cos2h = dotNH * dotNH;
	float sin2h = max( 1.0 - cos2h, 0.0078125 );
	return ( 2.0 + invAlpha ) * pow( sin2h, invAlpha * 0.5 ) / ( 2.0 * PI );
}
float V_Neubelt( float dotNV, float dotNL ) {
	return saturate( 1.0 / ( 4.0 * ( dotNL + dotNV - dotNL * dotNV ) ) );
}
vec3 BRDF_Sheen( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, vec3 sheenColor, const in float sheenRoughness ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float D = D_Charlie( sheenRoughness, dotNH );
	float V = V_Neubelt( dotNV, dotNL );
	return sheenColor * ( D * V );
}
#endif
float IBLSheenBRDF( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	float r2 = roughness * roughness;
	float a = roughness < 0.25 ? -339.2 * r2 + 161.4 * roughness - 25.9 : -8.48 * r2 + 14.3 * roughness - 9.95;
	float b = roughness < 0.25 ? 44.0 * r2 - 23.7 * roughness + 3.26 : 1.97 * r2 - 3.27 * roughness + 0.72;
	float DG = exp( a * dotNV + b ) + ( roughness < 0.25 ? 0.0 : 0.1 * ( roughness - 0.25 ) );
	return saturate( DG * RECIPROCAL_PI );
}
vec2 DFGApprox( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	const vec4 c0 = vec4( - 1, - 0.0275, - 0.572, 0.022 );
	const vec4 c1 = vec4( 1, 0.0425, 1.04, - 0.04 );
	vec4 r = roughness * c0 + c1;
	float a004 = min( r.x * r.x, exp2( - 9.28 * dotNV ) ) * r.x + r.y;
	vec2 fab = vec2( - 1.04, 1.04 ) * a004 + r.zw;
	return fab;
}
vec3 EnvironmentBRDF( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness ) {
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	return specularColor * fab.x + specularF90 * fab.y;
}
#ifdef USE_IRIDESCENCE
void computeMultiscatteringIridescence( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float iridescence, const in vec3 iridescenceF0, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#else
void computeMultiscattering( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#endif
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	#ifdef USE_IRIDESCENCE
		vec3 Fr = mix( specularColor, iridescenceF0, iridescence );
	#else
		vec3 Fr = specularColor;
	#endif
	vec3 FssEss = Fr * fab.x + specularF90 * fab.y;
	float Ess = fab.x + fab.y;
	float Ems = 1.0 - Ess;
	vec3 Favg = Fr + ( 1.0 - Fr ) * 0.047619;	vec3 Fms = FssEss * Favg / ( 1.0 - Ems * Favg );
	singleScatter += FssEss;
	multiScatter += Fms * Ems;
}
#if NUM_RECT_AREA_LIGHTS > 0
	void RE_Direct_RectArea_Physical( const in RectAreaLight rectAreaLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
		vec3 normal = geometryNormal;
		vec3 viewDir = geometryViewDir;
		vec3 position = geometryPosition;
		vec3 lightPos = rectAreaLight.position;
		vec3 halfWidth = rectAreaLight.halfWidth;
		vec3 halfHeight = rectAreaLight.halfHeight;
		vec3 lightColor = rectAreaLight.color;
		float roughness = material.roughness;
		vec3 rectCoords[ 4 ];
		rectCoords[ 0 ] = lightPos + halfWidth - halfHeight;		rectCoords[ 1 ] = lightPos - halfWidth - halfHeight;
		rectCoords[ 2 ] = lightPos - halfWidth + halfHeight;
		rectCoords[ 3 ] = lightPos + halfWidth + halfHeight;
		vec2 uv = LTC_Uv( normal, viewDir, roughness );
		vec4 t1 = texture2D( ltc_1, uv );
		vec4 t2 = texture2D( ltc_2, uv );
		mat3 mInv = mat3(
			vec3( t1.x, 0, t1.y ),
			vec3(    0, 1,    0 ),
			vec3( t1.z, 0, t1.w )
		);
		vec3 fresnel = ( material.specularColor * t2.x + ( vec3( 1.0 ) - material.specularColor ) * t2.y );
		reflectedLight.directSpecular += lightColor * fresnel * LTC_Evaluate( normal, viewDir, position, mInv, rectCoords );
		reflectedLight.directDiffuse += lightColor * material.diffuseColor * LTC_Evaluate( normal, viewDir, position, mat3( 1.0 ), rectCoords );
	}
#endif
void RE_Direct_Physical( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	#ifdef USE_CLEARCOAT
		float dotNLcc = saturate( dot( geometryClearcoatNormal, directLight.direction ) );
		vec3 ccIrradiance = dotNLcc * directLight.color;
		clearcoatSpecularDirect += ccIrradiance * BRDF_GGX_Clearcoat( directLight.direction, geometryViewDir, geometryClearcoatNormal, material );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularDirect += irradiance * BRDF_Sheen( directLight.direction, geometryViewDir, geometryNormal, material.sheenColor, material.sheenRoughness );
	#endif
	reflectedLight.directSpecular += irradiance * BRDF_GGX( directLight.direction, geometryViewDir, geometryNormal, material );
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Physical( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectSpecular_Physical( const in vec3 radiance, const in vec3 irradiance, const in vec3 clearcoatRadiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight) {
	#ifdef USE_CLEARCOAT
		clearcoatSpecularIndirect += clearcoatRadiance * EnvironmentBRDF( geometryClearcoatNormal, geometryViewDir, material.clearcoatF0, material.clearcoatF90, material.clearcoatRoughness );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularIndirect += irradiance * material.sheenColor * IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
	#endif
	vec3 singleScattering = vec3( 0.0 );
	vec3 multiScattering = vec3( 0.0 );
	vec3 cosineWeightedIrradiance = irradiance * RECIPROCAL_PI;
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.iridescence, material.iridescenceFresnel, material.roughness, singleScattering, multiScattering );
	#else
		computeMultiscattering( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.roughness, singleScattering, multiScattering );
	#endif
	vec3 totalScattering = singleScattering + multiScattering;
	vec3 diffuse = material.diffuseColor * ( 1.0 - max( max( totalScattering.r, totalScattering.g ), totalScattering.b ) );
	reflectedLight.indirectSpecular += radiance * singleScattering;
	reflectedLight.indirectSpecular += multiScattering * cosineWeightedIrradiance;
	reflectedLight.indirectDiffuse += diffuse * cosineWeightedIrradiance;
}
#define RE_Direct				RE_Direct_Physical
#define RE_Direct_RectArea		RE_Direct_RectArea_Physical
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Physical
#define RE_IndirectSpecular		RE_IndirectSpecular_Physical
float computeSpecularOcclusion( const in float dotNV, const in float ambientOcclusion, const in float roughness ) {
	return saturate( pow( dotNV + ambientOcclusion, exp2( - 16.0 * roughness - 1.0 ) ) - 1.0 + ambientOcclusion );
}`,vp=`
vec3 geometryPosition = - vViewPosition;
vec3 geometryNormal = normal;
vec3 geometryViewDir = ( isOrthographic ) ? vec3( 0, 0, 1 ) : normalize( vViewPosition );
vec3 geometryClearcoatNormal = vec3( 0.0 );
#ifdef USE_CLEARCOAT
	geometryClearcoatNormal = clearcoatNormal;
#endif
#ifdef USE_IRIDESCENCE
	float dotNVi = saturate( dot( normal, geometryViewDir ) );
	if ( material.iridescenceThickness == 0.0 ) {
		material.iridescence = 0.0;
	} else {
		material.iridescence = saturate( material.iridescence );
	}
	if ( material.iridescence > 0.0 ) {
		material.iridescenceFresnel = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.specularColor );
		material.iridescenceF0 = Schlick_to_F0( material.iridescenceFresnel, 1.0, dotNVi );
	}
#endif
IncidentLight directLight;
#if ( NUM_POINT_LIGHTS > 0 ) && defined( RE_Direct )
	PointLight pointLight;
	#if defined( USE_SHADOWMAP ) && NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHTS; i ++ ) {
		pointLight = pointLights[ i ];
		getPointLightInfo( pointLight, geometryPosition, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_POINT_LIGHT_SHADOWS )
		pointLightShadow = pointLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getPointShadow( pointShadowMap[ i ], pointLightShadow.shadowMapSize, pointLightShadow.shadowIntensity, pointLightShadow.shadowBias, pointLightShadow.shadowRadius, vPointShadowCoord[ i ], pointLightShadow.shadowCameraNear, pointLightShadow.shadowCameraFar ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SPOT_LIGHTS > 0 ) && defined( RE_Direct )
	SpotLight spotLight;
	vec4 spotColor;
	vec3 spotLightCoord;
	bool inSpotLightMap;
	#if defined( USE_SHADOWMAP ) && NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHTS; i ++ ) {
		spotLight = spotLights[ i ];
		getSpotLightInfo( spotLight, geometryPosition, directLight );
		#if ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#define SPOT_LIGHT_MAP_INDEX UNROLLED_LOOP_INDEX
		#elif ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		#define SPOT_LIGHT_MAP_INDEX NUM_SPOT_LIGHT_MAPS
		#else
		#define SPOT_LIGHT_MAP_INDEX ( UNROLLED_LOOP_INDEX - NUM_SPOT_LIGHT_SHADOWS + NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#endif
		#if ( SPOT_LIGHT_MAP_INDEX < NUM_SPOT_LIGHT_MAPS )
			spotLightCoord = vSpotLightCoord[ i ].xyz / vSpotLightCoord[ i ].w;
			inSpotLightMap = all( lessThan( abs( spotLightCoord * 2. - 1. ), vec3( 1.0 ) ) );
			spotColor = texture2D( spotLightMap[ SPOT_LIGHT_MAP_INDEX ], spotLightCoord.xy );
			directLight.color = inSpotLightMap ? directLight.color * spotColor.rgb : directLight.color;
		#endif
		#undef SPOT_LIGHT_MAP_INDEX
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		spotLightShadow = spotLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( spotShadowMap[ i ], spotLightShadow.shadowMapSize, spotLightShadow.shadowIntensity, spotLightShadow.shadowBias, spotLightShadow.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_DIR_LIGHTS > 0 ) && defined( RE_Direct )
	DirectionalLight directionalLight;
	#if defined( USE_SHADOWMAP ) && NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHTS; i ++ ) {
		directionalLight = directionalLights[ i ];
		getDirectionalLightInfo( directionalLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_DIR_LIGHT_SHADOWS )
		directionalLightShadow = directionalLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( directionalShadowMap[ i ], directionalLightShadow.shadowMapSize, directionalLightShadow.shadowIntensity, directionalLightShadow.shadowBias, directionalLightShadow.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_RECT_AREA_LIGHTS > 0 ) && defined( RE_Direct_RectArea )
	RectAreaLight rectAreaLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_RECT_AREA_LIGHTS; i ++ ) {
		rectAreaLight = rectAreaLights[ i ];
		RE_Direct_RectArea( rectAreaLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if defined( RE_IndirectDiffuse )
	vec3 iblIrradiance = vec3( 0.0 );
	vec3 irradiance = getAmbientLightIrradiance( ambientLightColor );
	#if defined( USE_LIGHT_PROBES )
		irradiance += getLightProbeIrradiance( lightProbe, geometryNormal );
	#endif
	#if ( NUM_HEMI_LIGHTS > 0 )
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_HEMI_LIGHTS; i ++ ) {
			irradiance += getHemisphereLightIrradiance( hemisphereLights[ i ], geometryNormal );
		}
		#pragma unroll_loop_end
	#endif
#endif
#if defined( RE_IndirectSpecular )
	vec3 radiance = vec3( 0.0 );
	vec3 clearcoatRadiance = vec3( 0.0 );
#endif`,xp=`#if defined( RE_IndirectDiffuse )
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
		irradiance += lightMapIrradiance;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD ) && defined( ENVMAP_TYPE_CUBE_UV )
		iblIrradiance += getIBLIrradiance( geometryNormal );
	#endif
#endif
#if defined( USE_ENVMAP ) && defined( RE_IndirectSpecular )
	#ifdef USE_ANISOTROPY
		radiance += getIBLAnisotropyRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
	#else
		radiance += getIBLRadiance( geometryViewDir, geometryNormal, material.roughness );
	#endif
	#ifdef USE_CLEARCOAT
		clearcoatRadiance += getIBLRadiance( geometryViewDir, geometryClearcoatNormal, material.clearcoatRoughness );
	#endif
#endif`,_p=`#if defined( RE_IndirectDiffuse )
	RE_IndirectDiffuse( irradiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif
#if defined( RE_IndirectSpecular )
	RE_IndirectSpecular( radiance, iblIrradiance, clearcoatRadiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif`,yp=`#if defined( USE_LOGDEPTHBUF )
	gl_FragDepth = vIsPerspective == 0.0 ? gl_FragCoord.z : log2( vFragDepth ) * logDepthBufFC * 0.5;
#endif`,Mp=`#if defined( USE_LOGDEPTHBUF )
	uniform float logDepthBufFC;
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,bp=`#ifdef USE_LOGDEPTHBUF
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,Sp=`#ifdef USE_LOGDEPTHBUF
	vFragDepth = 1.0 + gl_Position.w;
	vIsPerspective = float( isPerspectiveMatrix( projectionMatrix ) );
#endif`,wp=`#ifdef USE_MAP
	vec4 sampledDiffuseColor = texture2D( map, vMapUv );
	#ifdef DECODE_VIDEO_TEXTURE
		sampledDiffuseColor = sRGBTransferEOTF( sampledDiffuseColor );
	#endif
	diffuseColor *= sampledDiffuseColor;
#endif`,Ep=`#ifdef USE_MAP
	uniform sampler2D map;
#endif`,Tp=`#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
	#if defined( USE_POINTS_UV )
		vec2 uv = vUv;
	#else
		vec2 uv = ( uvTransform * vec3( gl_PointCoord.x, 1.0 - gl_PointCoord.y, 1 ) ).xy;
	#endif
#endif
#ifdef USE_MAP
	diffuseColor *= texture2D( map, uv );
#endif
#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, uv ).g;
#endif`,Ap=`#if defined( USE_POINTS_UV )
	varying vec2 vUv;
#else
	#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
		uniform mat3 uvTransform;
	#endif
#endif
#ifdef USE_MAP
	uniform sampler2D map;
#endif
#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,Rp=`float metalnessFactor = metalness;
#ifdef USE_METALNESSMAP
	vec4 texelMetalness = texture2D( metalnessMap, vMetalnessMapUv );
	metalnessFactor *= texelMetalness.b;
#endif`,Cp=`#ifdef USE_METALNESSMAP
	uniform sampler2D metalnessMap;
#endif`,Ip=`#ifdef USE_INSTANCING_MORPH
	float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	float morphTargetBaseInfluence = texelFetch( morphTexture, ivec2( 0, gl_InstanceID ), 0 ).r;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		morphTargetInfluences[i] =  texelFetch( morphTexture, ivec2( i + 1, gl_InstanceID ), 0 ).r;
	}
#endif`,Pp=`#if defined( USE_MORPHCOLORS )
	vColor *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		#if defined( USE_COLOR_ALPHA )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ) * morphTargetInfluences[ i ];
		#elif defined( USE_COLOR )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ).rgb * morphTargetInfluences[ i ];
		#endif
	}
#endif`,Lp=`#ifdef USE_MORPHNORMALS
	objectNormal *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) objectNormal += getMorph( gl_VertexID, i, 1 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,Dp=`#ifdef USE_MORPHTARGETS
	#ifndef USE_INSTANCING_MORPH
		uniform float morphTargetBaseInfluence;
		uniform float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	#endif
	uniform sampler2DArray morphTargetsTexture;
	uniform ivec2 morphTargetsTextureSize;
	vec4 getMorph( const in int vertexIndex, const in int morphTargetIndex, const in int offset ) {
		int texelIndex = vertexIndex * MORPHTARGETS_TEXTURE_STRIDE + offset;
		int y = texelIndex / morphTargetsTextureSize.x;
		int x = texelIndex - y * morphTargetsTextureSize.x;
		ivec3 morphUV = ivec3( x, y, morphTargetIndex );
		return texelFetch( morphTargetsTexture, morphUV, 0 );
	}
#endif`,Up=`#ifdef USE_MORPHTARGETS
	transformed *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) transformed += getMorph( gl_VertexID, i, 0 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,Np=`float faceDirection = gl_FrontFacing ? 1.0 : - 1.0;
#ifdef FLAT_SHADED
	vec3 fdx = dFdx( vViewPosition );
	vec3 fdy = dFdy( vViewPosition );
	vec3 normal = normalize( cross( fdx, fdy ) );
#else
	vec3 normal = normalize( vNormal );
	#ifdef DOUBLE_SIDED
		normal *= faceDirection;
	#endif
#endif
#if defined( USE_NORMALMAP_TANGENTSPACE ) || defined( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY )
	#ifdef USE_TANGENT
		mat3 tbn = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn = getTangentFrame( - vViewPosition, normal,
		#if defined( USE_NORMALMAP )
			vNormalMapUv
		#elif defined( USE_CLEARCOAT_NORMALMAP )
			vClearcoatNormalMapUv
		#else
			vUv
		#endif
		);
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn[0] *= faceDirection;
		tbn[1] *= faceDirection;
	#endif
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	#ifdef USE_TANGENT
		mat3 tbn2 = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn2 = getTangentFrame( - vViewPosition, normal, vClearcoatNormalMapUv );
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn2[0] *= faceDirection;
		tbn2[1] *= faceDirection;
	#endif
#endif
vec3 nonPerturbedNormal = normal;`,Fp=`#ifdef USE_NORMALMAP_OBJECTSPACE
	normal = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#ifdef FLIP_SIDED
		normal = - normal;
	#endif
	#ifdef DOUBLE_SIDED
		normal = normal * faceDirection;
	#endif
	normal = normalize( normalMatrix * normal );
#elif defined( USE_NORMALMAP_TANGENTSPACE )
	vec3 mapN = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	mapN.xy *= normalScale;
	normal = normalize( tbn * mapN );
#elif defined( USE_BUMPMAP )
	normal = perturbNormalArb( - vViewPosition, normal, dHdxy_fwd(), faceDirection );
#endif`,Op=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,Bp=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,zp=`#ifndef FLAT_SHADED
	vNormal = normalize( transformedNormal );
	#ifdef USE_TANGENT
		vTangent = normalize( transformedTangent );
		vBitangent = normalize( cross( vNormal, vTangent ) * tangent.w );
	#endif
#endif`,kp=`#ifdef USE_NORMALMAP
	uniform sampler2D normalMap;
	uniform vec2 normalScale;
#endif
#ifdef USE_NORMALMAP_OBJECTSPACE
	uniform mat3 normalMatrix;
#endif
#if ! defined ( USE_TANGENT ) && ( defined ( USE_NORMALMAP_TANGENTSPACE ) || defined ( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY ) )
	mat3 getTangentFrame( vec3 eye_pos, vec3 surf_norm, vec2 uv ) {
		vec3 q0 = dFdx( eye_pos.xyz );
		vec3 q1 = dFdy( eye_pos.xyz );
		vec2 st0 = dFdx( uv.st );
		vec2 st1 = dFdy( uv.st );
		vec3 N = surf_norm;
		vec3 q1perp = cross( q1, N );
		vec3 q0perp = cross( N, q0 );
		vec3 T = q1perp * st0.x + q0perp * st1.x;
		vec3 B = q1perp * st0.y + q0perp * st1.y;
		float det = max( dot( T, T ), dot( B, B ) );
		float scale = ( det == 0.0 ) ? 0.0 : inversesqrt( det );
		return mat3( T * scale, B * scale, N );
	}
#endif`,Hp=`#ifdef USE_CLEARCOAT
	vec3 clearcoatNormal = nonPerturbedNormal;
#endif`,Vp=`#ifdef USE_CLEARCOAT_NORMALMAP
	vec3 clearcoatMapN = texture2D( clearcoatNormalMap, vClearcoatNormalMapUv ).xyz * 2.0 - 1.0;
	clearcoatMapN.xy *= clearcoatNormalScale;
	clearcoatNormal = normalize( tbn2 * clearcoatMapN );
#endif`,Gp=`#ifdef USE_CLEARCOATMAP
	uniform sampler2D clearcoatMap;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform sampler2D clearcoatNormalMap;
	uniform vec2 clearcoatNormalScale;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform sampler2D clearcoatRoughnessMap;
#endif`,Wp=`#ifdef USE_IRIDESCENCEMAP
	uniform sampler2D iridescenceMap;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform sampler2D iridescenceThicknessMap;
#endif`,Xp=`#ifdef OPAQUE
diffuseColor.a = 1.0;
#endif
#ifdef USE_TRANSMISSION
diffuseColor.a *= material.transmissionAlpha;
#endif
gl_FragColor = vec4( outgoingLight, diffuseColor.a );`,qp=`vec3 packNormalToRGB( const in vec3 normal ) {
	return normalize( normal ) * 0.5 + 0.5;
}
vec3 unpackRGBToNormal( const in vec3 rgb ) {
	return 2.0 * rgb.xyz - 1.0;
}
const float PackUpscale = 256. / 255.;const float UnpackDownscale = 255. / 256.;const float ShiftRight8 = 1. / 256.;
const float Inv255 = 1. / 255.;
const vec4 PackFactors = vec4( 1.0, 256.0, 256.0 * 256.0, 256.0 * 256.0 * 256.0 );
const vec2 UnpackFactors2 = vec2( UnpackDownscale, 1.0 / PackFactors.g );
const vec3 UnpackFactors3 = vec3( UnpackDownscale / PackFactors.rg, 1.0 / PackFactors.b );
const vec4 UnpackFactors4 = vec4( UnpackDownscale / PackFactors.rgb, 1.0 / PackFactors.a );
vec4 packDepthToRGBA( const in float v ) {
	if( v <= 0.0 )
		return vec4( 0., 0., 0., 0. );
	if( v >= 1.0 )
		return vec4( 1., 1., 1., 1. );
	float vuf;
	float af = modf( v * PackFactors.a, vuf );
	float bf = modf( vuf * ShiftRight8, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec4( vuf * Inv255, gf * PackUpscale, bf * PackUpscale, af );
}
vec3 packDepthToRGB( const in float v ) {
	if( v <= 0.0 )
		return vec3( 0., 0., 0. );
	if( v >= 1.0 )
		return vec3( 1., 1., 1. );
	float vuf;
	float bf = modf( v * PackFactors.b, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec3( vuf * Inv255, gf * PackUpscale, bf );
}
vec2 packDepthToRG( const in float v ) {
	if( v <= 0.0 )
		return vec2( 0., 0. );
	if( v >= 1.0 )
		return vec2( 1., 1. );
	float vuf;
	float gf = modf( v * 256., vuf );
	return vec2( vuf * Inv255, gf );
}
float unpackRGBAToDepth( const in vec4 v ) {
	return dot( v, UnpackFactors4 );
}
float unpackRGBToDepth( const in vec3 v ) {
	return dot( v, UnpackFactors3 );
}
float unpackRGToDepth( const in vec2 v ) {
	return v.r * UnpackFactors2.r + v.g * UnpackFactors2.g;
}
vec4 pack2HalfToRGBA( const in vec2 v ) {
	vec4 r = vec4( v.x, fract( v.x * 255.0 ), v.y, fract( v.y * 255.0 ) );
	return vec4( r.x - r.y / 255.0, r.y, r.z - r.w / 255.0, r.w );
}
vec2 unpackRGBATo2Half( const in vec4 v ) {
	return vec2( v.x + ( v.y / 255.0 ), v.z + ( v.w / 255.0 ) );
}
float viewZToOrthographicDepth( const in float viewZ, const in float near, const in float far ) {
	return ( viewZ + near ) / ( near - far );
}
float orthographicDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return depth * ( near - far ) - near;
}
float viewZToPerspectiveDepth( const in float viewZ, const in float near, const in float far ) {
	return ( ( near + viewZ ) * far ) / ( ( far - near ) * viewZ );
}
float perspectiveDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return ( near * far ) / ( ( far - near ) * depth - far );
}`,Yp=`#ifdef PREMULTIPLIED_ALPHA
	gl_FragColor.rgb *= gl_FragColor.a;
#endif`,$p=`vec4 mvPosition = vec4( transformed, 1.0 );
#ifdef USE_BATCHING
	mvPosition = batchingMatrix * mvPosition;
#endif
#ifdef USE_INSTANCING
	mvPosition = instanceMatrix * mvPosition;
#endif
mvPosition = modelViewMatrix * mvPosition;
gl_Position = projectionMatrix * mvPosition;`,Zp=`#ifdef DITHERING
	gl_FragColor.rgb = dithering( gl_FragColor.rgb );
#endif`,Kp=`#ifdef DITHERING
	vec3 dithering( vec3 color ) {
		float grid_position = rand( gl_FragCoord.xy );
		vec3 dither_shift_RGB = vec3( 0.25 / 255.0, -0.25 / 255.0, 0.25 / 255.0 );
		dither_shift_RGB = mix( 2.0 * dither_shift_RGB, -2.0 * dither_shift_RGB, grid_position );
		return color + dither_shift_RGB;
	}
#endif`,Jp=`float roughnessFactor = roughness;
#ifdef USE_ROUGHNESSMAP
	vec4 texelRoughness = texture2D( roughnessMap, vRoughnessMapUv );
	roughnessFactor *= texelRoughness.g;
#endif`,jp=`#ifdef USE_ROUGHNESSMAP
	uniform sampler2D roughnessMap;
#endif`,Qp=`#if NUM_SPOT_LIGHT_COORDS > 0
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#if NUM_SPOT_LIGHT_MAPS > 0
	uniform sampler2D spotLightMap[ NUM_SPOT_LIGHT_MAPS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform sampler2D directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		uniform sampler2D spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform sampler2D pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
	float texture2DCompare( sampler2D depths, vec2 uv, float compare ) {
		return step( compare, unpackRGBAToDepth( texture2D( depths, uv ) ) );
	}
	vec2 texture2DDistribution( sampler2D shadow, vec2 uv ) {
		return unpackRGBATo2Half( texture2D( shadow, uv ) );
	}
	float VSMShadow (sampler2D shadow, vec2 uv, float compare ){
		float occlusion = 1.0;
		vec2 distribution = texture2DDistribution( shadow, uv );
		float hard_shadow = step( compare , distribution.x );
		if (hard_shadow != 1.0 ) {
			float distance = compare - distribution.x ;
			float variance = max( 0.00000, distribution.y * distribution.y );
			float softness_probability = variance / (variance + distance * distance );			softness_probability = clamp( ( softness_probability - 0.3 ) / ( 0.95 - 0.3 ), 0.0, 1.0 );			occlusion = clamp( max( hard_shadow, softness_probability ), 0.0, 1.0 );
		}
		return occlusion;
	}
	float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
		float shadow = 1.0;
		shadowCoord.xyz /= shadowCoord.w;
		shadowCoord.z += shadowBias;
		bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
		bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
		if ( frustumTest ) {
		#if defined( SHADOWMAP_TYPE_PCF )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx0 = - texelSize.x * shadowRadius;
			float dy0 = - texelSize.y * shadowRadius;
			float dx1 = + texelSize.x * shadowRadius;
			float dy1 = + texelSize.y * shadowRadius;
			float dx2 = dx0 / 2.0;
			float dy2 = dy0 / 2.0;
			float dx3 = dx1 / 2.0;
			float dy3 = dy1 / 2.0;
			shadow = (
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy1 ), shadowCoord.z )
			) * ( 1.0 / 17.0 );
		#elif defined( SHADOWMAP_TYPE_PCF_SOFT )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx = texelSize.x;
			float dy = texelSize.y;
			vec2 uv = shadowCoord.xy;
			vec2 f = fract( uv * shadowMapSize + 0.5 );
			uv -= f * texelSize;
			shadow = (
				texture2DCompare( shadowMap, uv, shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( dx, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( 0.0, dy ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + texelSize, shadowCoord.z ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, 0.0 ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 0.0 ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, dy ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( 0.0, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 0.0, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( texture2DCompare( shadowMap, uv + vec2( dx, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( dx, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( mix( texture2DCompare( shadowMap, uv + vec2( -dx, -dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, -dy ), shadowCoord.z ),
						  f.x ),
					 mix( texture2DCompare( shadowMap, uv + vec2( -dx, 2.0 * dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 2.0 * dy ), shadowCoord.z ),
						  f.x ),
					 f.y )
			) * ( 1.0 / 9.0 );
		#elif defined( SHADOWMAP_TYPE_VSM )
			shadow = VSMShadow( shadowMap, shadowCoord.xy, shadowCoord.z );
		#else
			shadow = texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z );
		#endif
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
	vec2 cubeToUV( vec3 v, float texelSizeY ) {
		vec3 absV = abs( v );
		float scaleToCube = 1.0 / max( absV.x, max( absV.y, absV.z ) );
		absV *= scaleToCube;
		v *= scaleToCube * ( 1.0 - 2.0 * texelSizeY );
		vec2 planar = v.xy;
		float almostATexel = 1.5 * texelSizeY;
		float almostOne = 1.0 - almostATexel;
		if ( absV.z >= almostOne ) {
			if ( v.z > 0.0 )
				planar.x = 4.0 - v.x;
		} else if ( absV.x >= almostOne ) {
			float signX = sign( v.x );
			planar.x = v.z * signX + 2.0 * signX;
		} else if ( absV.y >= almostOne ) {
			float signY = sign( v.y );
			planar.x = v.x + 2.0 * signY + 2.0;
			planar.y = v.z * signY - 2.0;
		}
		return vec2( 0.125, 0.25 ) * planar + vec2( 0.375, 0.75 );
	}
	float getPointShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		float shadow = 1.0;
		vec3 lightToPosition = shadowCoord.xyz;
		
		float lightToPositionLength = length( lightToPosition );
		if ( lightToPositionLength - shadowCameraFar <= 0.0 && lightToPositionLength - shadowCameraNear >= 0.0 ) {
			float dp = ( lightToPositionLength - shadowCameraNear ) / ( shadowCameraFar - shadowCameraNear );			dp += shadowBias;
			vec3 bd3D = normalize( lightToPosition );
			vec2 texelSize = vec2( 1.0 ) / ( shadowMapSize * vec2( 4.0, 2.0 ) );
			#if defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_PCF_SOFT ) || defined( SHADOWMAP_TYPE_VSM )
				vec2 offset = vec2( - 1, 1 ) * shadowRadius * texelSize.y;
				shadow = (
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxy, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxx, texelSize.y ), dp ) +
					texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxx, texelSize.y ), dp )
				) * ( 1.0 / 9.0 );
			#else
				shadow = texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp );
			#endif
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
#endif`,em=`#if NUM_SPOT_LIGHT_COORDS > 0
	uniform mat4 spotLightMatrix[ NUM_SPOT_LIGHT_COORDS ];
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform mat4 directionalShadowMatrix[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform mat4 pointShadowMatrix[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
#endif`,tm=`#if ( defined( USE_SHADOWMAP ) && ( NUM_DIR_LIGHT_SHADOWS > 0 || NUM_POINT_LIGHT_SHADOWS > 0 ) ) || ( NUM_SPOT_LIGHT_COORDS > 0 )
	vec3 shadowWorldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
	vec4 shadowWorldPosition;
#endif
#if defined( USE_SHADOWMAP )
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * directionalLightShadows[ i ].shadowNormalBias, 0 );
			vDirectionalShadowCoord[ i ] = directionalShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * pointLightShadows[ i ].shadowNormalBias, 0 );
			vPointShadowCoord[ i ] = pointShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
#endif
#if NUM_SPOT_LIGHT_COORDS > 0
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_COORDS; i ++ ) {
		shadowWorldPosition = worldPosition;
		#if ( defined( USE_SHADOWMAP ) && UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
			shadowWorldPosition.xyz += shadowWorldNormal * spotLightShadows[ i ].shadowNormalBias;
		#endif
		vSpotLightCoord[ i ] = spotLightMatrix[ i ] * shadowWorldPosition;
	}
	#pragma unroll_loop_end
#endif`,nm=`float getShadowMask() {
	float shadow = 1.0;
	#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
		directionalLight = directionalLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( directionalShadowMap[ i ], directionalLight.shadowMapSize, directionalLight.shadowIntensity, directionalLight.shadowBias, directionalLight.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_SHADOWS; i ++ ) {
		spotLight = spotLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( spotShadowMap[ i ], spotLight.shadowMapSize, spotLight.shadowIntensity, spotLight.shadowBias, spotLight.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
		pointLight = pointLightShadows[ i ];
		shadow *= receiveShadow ? getPointShadow( pointShadowMap[ i ], pointLight.shadowMapSize, pointLight.shadowIntensity, pointLight.shadowBias, pointLight.shadowRadius, vPointShadowCoord[ i ], pointLight.shadowCameraNear, pointLight.shadowCameraFar ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#endif
	return shadow;
}`,im=`#ifdef USE_SKINNING
	mat4 boneMatX = getBoneMatrix( skinIndex.x );
	mat4 boneMatY = getBoneMatrix( skinIndex.y );
	mat4 boneMatZ = getBoneMatrix( skinIndex.z );
	mat4 boneMatW = getBoneMatrix( skinIndex.w );
#endif`,sm=`#ifdef USE_SKINNING
	uniform mat4 bindMatrix;
	uniform mat4 bindMatrixInverse;
	uniform highp sampler2D boneTexture;
	mat4 getBoneMatrix( const in float i ) {
		int size = textureSize( boneTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( boneTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( boneTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( boneTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( boneTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
#endif`,rm=`#ifdef USE_SKINNING
	vec4 skinVertex = bindMatrix * vec4( transformed, 1.0 );
	vec4 skinned = vec4( 0.0 );
	skinned += boneMatX * skinVertex * skinWeight.x;
	skinned += boneMatY * skinVertex * skinWeight.y;
	skinned += boneMatZ * skinVertex * skinWeight.z;
	skinned += boneMatW * skinVertex * skinWeight.w;
	transformed = ( bindMatrixInverse * skinned ).xyz;
#endif`,om=`#ifdef USE_SKINNING
	mat4 skinMatrix = mat4( 0.0 );
	skinMatrix += skinWeight.x * boneMatX;
	skinMatrix += skinWeight.y * boneMatY;
	skinMatrix += skinWeight.z * boneMatZ;
	skinMatrix += skinWeight.w * boneMatW;
	skinMatrix = bindMatrixInverse * skinMatrix * bindMatrix;
	objectNormal = vec4( skinMatrix * vec4( objectNormal, 0.0 ) ).xyz;
	#ifdef USE_TANGENT
		objectTangent = vec4( skinMatrix * vec4( objectTangent, 0.0 ) ).xyz;
	#endif
#endif`,am=`float specularStrength;
#ifdef USE_SPECULARMAP
	vec4 texelSpecular = texture2D( specularMap, vSpecularMapUv );
	specularStrength = texelSpecular.r;
#else
	specularStrength = 1.0;
#endif`,cm=`#ifdef USE_SPECULARMAP
	uniform sampler2D specularMap;
#endif`,lm=`#if defined( TONE_MAPPING )
	gl_FragColor.rgb = toneMapping( gl_FragColor.rgb );
#endif`,um=`#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
uniform float toneMappingExposure;
vec3 LinearToneMapping( vec3 color ) {
	return saturate( toneMappingExposure * color );
}
vec3 ReinhardToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	return saturate( color / ( vec3( 1.0 ) + color ) );
}
vec3 CineonToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	color = max( vec3( 0.0 ), color - 0.004 );
	return pow( ( color * ( 6.2 * color + 0.5 ) ) / ( color * ( 6.2 * color + 1.7 ) + 0.06 ), vec3( 2.2 ) );
}
vec3 RRTAndODTFit( vec3 v ) {
	vec3 a = v * ( v + 0.0245786 ) - 0.000090537;
	vec3 b = v * ( 0.983729 * v + 0.4329510 ) + 0.238081;
	return a / b;
}
vec3 ACESFilmicToneMapping( vec3 color ) {
	const mat3 ACESInputMat = mat3(
		vec3( 0.59719, 0.07600, 0.02840 ),		vec3( 0.35458, 0.90834, 0.13383 ),
		vec3( 0.04823, 0.01566, 0.83777 )
	);
	const mat3 ACESOutputMat = mat3(
		vec3(  1.60475, -0.10208, -0.00327 ),		vec3( -0.53108,  1.10813, -0.07276 ),
		vec3( -0.07367, -0.00605,  1.07602 )
	);
	color *= toneMappingExposure / 0.6;
	color = ACESInputMat * color;
	color = RRTAndODTFit( color );
	color = ACESOutputMat * color;
	return saturate( color );
}
const mat3 LINEAR_REC2020_TO_LINEAR_SRGB = mat3(
	vec3( 1.6605, - 0.1246, - 0.0182 ),
	vec3( - 0.5876, 1.1329, - 0.1006 ),
	vec3( - 0.0728, - 0.0083, 1.1187 )
);
const mat3 LINEAR_SRGB_TO_LINEAR_REC2020 = mat3(
	vec3( 0.6274, 0.0691, 0.0164 ),
	vec3( 0.3293, 0.9195, 0.0880 ),
	vec3( 0.0433, 0.0113, 0.8956 )
);
vec3 agxDefaultContrastApprox( vec3 x ) {
	vec3 x2 = x * x;
	vec3 x4 = x2 * x2;
	return + 15.5 * x4 * x2
		- 40.14 * x4 * x
		+ 31.96 * x4
		- 6.868 * x2 * x
		+ 0.4298 * x2
		+ 0.1191 * x
		- 0.00232;
}
vec3 AgXToneMapping( vec3 color ) {
	const mat3 AgXInsetMatrix = mat3(
		vec3( 0.856627153315983, 0.137318972929847, 0.11189821299995 ),
		vec3( 0.0951212405381588, 0.761241990602591, 0.0767994186031903 ),
		vec3( 0.0482516061458583, 0.101439036467562, 0.811302368396859 )
	);
	const mat3 AgXOutsetMatrix = mat3(
		vec3( 1.1271005818144368, - 0.1413297634984383, - 0.14132976349843826 ),
		vec3( - 0.11060664309660323, 1.157823702216272, - 0.11060664309660294 ),
		vec3( - 0.016493938717834573, - 0.016493938717834257, 1.2519364065950405 )
	);
	const float AgxMinEv = - 12.47393;	const float AgxMaxEv = 4.026069;
	color *= toneMappingExposure;
	color = LINEAR_SRGB_TO_LINEAR_REC2020 * color;
	color = AgXInsetMatrix * color;
	color = max( color, 1e-10 );	color = log2( color );
	color = ( color - AgxMinEv ) / ( AgxMaxEv - AgxMinEv );
	color = clamp( color, 0.0, 1.0 );
	color = agxDefaultContrastApprox( color );
	color = AgXOutsetMatrix * color;
	color = pow( max( vec3( 0.0 ), color ), vec3( 2.2 ) );
	color = LINEAR_REC2020_TO_LINEAR_SRGB * color;
	color = clamp( color, 0.0, 1.0 );
	return color;
}
vec3 NeutralToneMapping( vec3 color ) {
	const float StartCompression = 0.8 - 0.04;
	const float Desaturation = 0.15;
	color *= toneMappingExposure;
	float x = min( color.r, min( color.g, color.b ) );
	float offset = x < 0.08 ? x - 6.25 * x * x : 0.04;
	color -= offset;
	float peak = max( color.r, max( color.g, color.b ) );
	if ( peak < StartCompression ) return color;
	float d = 1. - StartCompression;
	float newPeak = 1. - d * d / ( peak + d - StartCompression );
	color *= newPeak / peak;
	float g = 1. - 1. / ( Desaturation * ( peak - newPeak ) + 1. );
	return mix( color, vec3( newPeak ), g );
}
vec3 CustomToneMapping( vec3 color ) { return color; }`,hm=`#ifdef USE_TRANSMISSION
	material.transmission = transmission;
	material.transmissionAlpha = 1.0;
	material.thickness = thickness;
	material.attenuationDistance = attenuationDistance;
	material.attenuationColor = attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		material.transmission *= texture2D( transmissionMap, vTransmissionMapUv ).r;
	#endif
	#ifdef USE_THICKNESSMAP
		material.thickness *= texture2D( thicknessMap, vThicknessMapUv ).g;
	#endif
	vec3 pos = vWorldPosition;
	vec3 v = normalize( cameraPosition - pos );
	vec3 n = inverseTransformDirection( normal, viewMatrix );
	vec4 transmitted = getIBLVolumeRefraction(
		n, v, material.roughness, material.diffuseColor, material.specularColor, material.specularF90,
		pos, modelMatrix, viewMatrix, projectionMatrix, material.dispersion, material.ior, material.thickness,
		material.attenuationColor, material.attenuationDistance );
	material.transmissionAlpha = mix( material.transmissionAlpha, transmitted.a, material.transmission );
	totalDiffuse = mix( totalDiffuse, transmitted.rgb, material.transmission );
#endif`,fm=`#ifdef USE_TRANSMISSION
	uniform float transmission;
	uniform float thickness;
	uniform float attenuationDistance;
	uniform vec3 attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		uniform sampler2D transmissionMap;
	#endif
	#ifdef USE_THICKNESSMAP
		uniform sampler2D thicknessMap;
	#endif
	uniform vec2 transmissionSamplerSize;
	uniform sampler2D transmissionSamplerMap;
	uniform mat4 modelMatrix;
	uniform mat4 projectionMatrix;
	varying vec3 vWorldPosition;
	float w0( float a ) {
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - a + 3.0 ) - 3.0 ) + 1.0 );
	}
	float w1( float a ) {
		return ( 1.0 / 6.0 ) * ( a *  a * ( 3.0 * a - 6.0 ) + 4.0 );
	}
	float w2( float a ){
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - 3.0 * a + 3.0 ) + 3.0 ) + 1.0 );
	}
	float w3( float a ) {
		return ( 1.0 / 6.0 ) * ( a * a * a );
	}
	float g0( float a ) {
		return w0( a ) + w1( a );
	}
	float g1( float a ) {
		return w2( a ) + w3( a );
	}
	float h0( float a ) {
		return - 1.0 + w1( a ) / ( w0( a ) + w1( a ) );
	}
	float h1( float a ) {
		return 1.0 + w3( a ) / ( w2( a ) + w3( a ) );
	}
	vec4 bicubic( sampler2D tex, vec2 uv, vec4 texelSize, float lod ) {
		uv = uv * texelSize.zw + 0.5;
		vec2 iuv = floor( uv );
		vec2 fuv = fract( uv );
		float g0x = g0( fuv.x );
		float g1x = g1( fuv.x );
		float h0x = h0( fuv.x );
		float h1x = h1( fuv.x );
		float h0y = h0( fuv.y );
		float h1y = h1( fuv.y );
		vec2 p0 = ( vec2( iuv.x + h0x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p1 = ( vec2( iuv.x + h1x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p2 = ( vec2( iuv.x + h0x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		vec2 p3 = ( vec2( iuv.x + h1x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		return g0( fuv.y ) * ( g0x * textureLod( tex, p0, lod ) + g1x * textureLod( tex, p1, lod ) ) +
			g1( fuv.y ) * ( g0x * textureLod( tex, p2, lod ) + g1x * textureLod( tex, p3, lod ) );
	}
	vec4 textureBicubic( sampler2D sampler, vec2 uv, float lod ) {
		vec2 fLodSize = vec2( textureSize( sampler, int( lod ) ) );
		vec2 cLodSize = vec2( textureSize( sampler, int( lod + 1.0 ) ) );
		vec2 fLodSizeInv = 1.0 / fLodSize;
		vec2 cLodSizeInv = 1.0 / cLodSize;
		vec4 fSample = bicubic( sampler, uv, vec4( fLodSizeInv, fLodSize ), floor( lod ) );
		vec4 cSample = bicubic( sampler, uv, vec4( cLodSizeInv, cLodSize ), ceil( lod ) );
		return mix( fSample, cSample, fract( lod ) );
	}
	vec3 getVolumeTransmissionRay( const in vec3 n, const in vec3 v, const in float thickness, const in float ior, const in mat4 modelMatrix ) {
		vec3 refractionVector = refract( - v, normalize( n ), 1.0 / ior );
		vec3 modelScale;
		modelScale.x = length( vec3( modelMatrix[ 0 ].xyz ) );
		modelScale.y = length( vec3( modelMatrix[ 1 ].xyz ) );
		modelScale.z = length( vec3( modelMatrix[ 2 ].xyz ) );
		return normalize( refractionVector ) * thickness * modelScale;
	}
	float applyIorToRoughness( const in float roughness, const in float ior ) {
		return roughness * clamp( ior * 2.0 - 2.0, 0.0, 1.0 );
	}
	vec4 getTransmissionSample( const in vec2 fragCoord, const in float roughness, const in float ior ) {
		float lod = log2( transmissionSamplerSize.x ) * applyIorToRoughness( roughness, ior );
		return textureBicubic( transmissionSamplerMap, fragCoord.xy, lod );
	}
	vec3 volumeAttenuation( const in float transmissionDistance, const in vec3 attenuationColor, const in float attenuationDistance ) {
		if ( isinf( attenuationDistance ) ) {
			return vec3( 1.0 );
		} else {
			vec3 attenuationCoefficient = -log( attenuationColor ) / attenuationDistance;
			vec3 transmittance = exp( - attenuationCoefficient * transmissionDistance );			return transmittance;
		}
	}
	vec4 getIBLVolumeRefraction( const in vec3 n, const in vec3 v, const in float roughness, const in vec3 diffuseColor,
		const in vec3 specularColor, const in float specularF90, const in vec3 position, const in mat4 modelMatrix,
		const in mat4 viewMatrix, const in mat4 projMatrix, const in float dispersion, const in float ior, const in float thickness,
		const in vec3 attenuationColor, const in float attenuationDistance ) {
		vec4 transmittedLight;
		vec3 transmittance;
		#ifdef USE_DISPERSION
			float halfSpread = ( ior - 1.0 ) * 0.025 * dispersion;
			vec3 iors = vec3( ior - halfSpread, ior, ior + halfSpread );
			for ( int i = 0; i < 3; i ++ ) {
				vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, iors[ i ], modelMatrix );
				vec3 refractedRayExit = position + transmissionRay;
		
				vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
				vec2 refractionCoords = ndcPos.xy / ndcPos.w;
				refractionCoords += 1.0;
				refractionCoords /= 2.0;
		
				vec4 transmissionSample = getTransmissionSample( refractionCoords, roughness, iors[ i ] );
				transmittedLight[ i ] = transmissionSample[ i ];
				transmittedLight.a += transmissionSample.a;
				transmittance[ i ] = diffuseColor[ i ] * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance )[ i ];
			}
			transmittedLight.a /= 3.0;
		
		#else
		
			vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, ior, modelMatrix );
			vec3 refractedRayExit = position + transmissionRay;
			vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
			vec2 refractionCoords = ndcPos.xy / ndcPos.w;
			refractionCoords += 1.0;
			refractionCoords /= 2.0;
			transmittedLight = getTransmissionSample( refractionCoords, roughness, ior );
			transmittance = diffuseColor * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance );
		
		#endif
		vec3 attenuatedColor = transmittance * transmittedLight.rgb;
		vec3 F = EnvironmentBRDF( n, v, specularColor, specularF90, roughness );
		float transmittanceFactor = ( transmittance.r + transmittance.g + transmittance.b ) / 3.0;
		return vec4( ( 1.0 - F ) * attenuatedColor, 1.0 - ( 1.0 - transmittedLight.a ) * transmittanceFactor );
	}
#endif`,dm=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_SPECULARMAP
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,pm=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	uniform mat3 mapTransform;
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	uniform mat3 alphaMapTransform;
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	uniform mat3 lightMapTransform;
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	uniform mat3 aoMapTransform;
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	uniform mat3 bumpMapTransform;
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	uniform mat3 normalMapTransform;
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_DISPLACEMENTMAP
	uniform mat3 displacementMapTransform;
	varying vec2 vDisplacementMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	uniform mat3 emissiveMapTransform;
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	uniform mat3 metalnessMapTransform;
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	uniform mat3 roughnessMapTransform;
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	uniform mat3 anisotropyMapTransform;
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	uniform mat3 clearcoatMapTransform;
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform mat3 clearcoatNormalMapTransform;
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform mat3 clearcoatRoughnessMapTransform;
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	uniform mat3 sheenColorMapTransform;
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	uniform mat3 sheenRoughnessMapTransform;
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	uniform mat3 iridescenceMapTransform;
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform mat3 iridescenceThicknessMapTransform;
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SPECULARMAP
	uniform mat3 specularMapTransform;
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	uniform mat3 specularColorMapTransform;
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	uniform mat3 specularIntensityMapTransform;
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,mm=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	vUv = vec3( uv, 1 ).xy;
#endif
#ifdef USE_MAP
	vMapUv = ( mapTransform * vec3( MAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ALPHAMAP
	vAlphaMapUv = ( alphaMapTransform * vec3( ALPHAMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_LIGHTMAP
	vLightMapUv = ( lightMapTransform * vec3( LIGHTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_AOMAP
	vAoMapUv = ( aoMapTransform * vec3( AOMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_BUMPMAP
	vBumpMapUv = ( bumpMapTransform * vec3( BUMPMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_NORMALMAP
	vNormalMapUv = ( normalMapTransform * vec3( NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DISPLACEMENTMAP
	vDisplacementMapUv = ( displacementMapTransform * vec3( DISPLACEMENTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_EMISSIVEMAP
	vEmissiveMapUv = ( emissiveMapTransform * vec3( EMISSIVEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_METALNESSMAP
	vMetalnessMapUv = ( metalnessMapTransform * vec3( METALNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ROUGHNESSMAP
	vRoughnessMapUv = ( roughnessMapTransform * vec3( ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ANISOTROPYMAP
	vAnisotropyMapUv = ( anisotropyMapTransform * vec3( ANISOTROPYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOATMAP
	vClearcoatMapUv = ( clearcoatMapTransform * vec3( CLEARCOATMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	vClearcoatNormalMapUv = ( clearcoatNormalMapTransform * vec3( CLEARCOAT_NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	vClearcoatRoughnessMapUv = ( clearcoatRoughnessMapTransform * vec3( CLEARCOAT_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCEMAP
	vIridescenceMapUv = ( iridescenceMapTransform * vec3( IRIDESCENCEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	vIridescenceThicknessMapUv = ( iridescenceThicknessMapTransform * vec3( IRIDESCENCE_THICKNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_COLORMAP
	vSheenColorMapUv = ( sheenColorMapTransform * vec3( SHEEN_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	vSheenRoughnessMapUv = ( sheenRoughnessMapTransform * vec3( SHEEN_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULARMAP
	vSpecularMapUv = ( specularMapTransform * vec3( SPECULARMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_COLORMAP
	vSpecularColorMapUv = ( specularColorMapTransform * vec3( SPECULAR_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	vSpecularIntensityMapUv = ( specularIntensityMapTransform * vec3( SPECULAR_INTENSITYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_TRANSMISSIONMAP
	vTransmissionMapUv = ( transmissionMapTransform * vec3( TRANSMISSIONMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_THICKNESSMAP
	vThicknessMapUv = ( thicknessMapTransform * vec3( THICKNESSMAP_UV, 1 ) ).xy;
#endif`,gm=`#if defined( USE_ENVMAP ) || defined( DISTANCE ) || defined ( USE_SHADOWMAP ) || defined ( USE_TRANSMISSION ) || NUM_SPOT_LIGHT_COORDS > 0
	vec4 worldPosition = vec4( transformed, 1.0 );
	#ifdef USE_BATCHING
		worldPosition = batchingMatrix * worldPosition;
	#endif
	#ifdef USE_INSTANCING
		worldPosition = instanceMatrix * worldPosition;
	#endif
	worldPosition = modelMatrix * worldPosition;
#endif`,vm=`varying vec2 vUv;
uniform mat3 uvTransform;
void main() {
	vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	gl_Position = vec4( position.xy, 1.0, 1.0 );
}`,xm=`uniform sampler2D t2D;
uniform float backgroundIntensity;
varying vec2 vUv;
void main() {
	vec4 texColor = texture2D( t2D, vUv );
	#ifdef DECODE_VIDEO_TEXTURE
		texColor = vec4( mix( pow( texColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), texColor.rgb * 0.0773993808, vec3( lessThanEqual( texColor.rgb, vec3( 0.04045 ) ) ) ), texColor.w );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,_m=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,ym=`#ifdef ENVMAP_TYPE_CUBE
	uniform samplerCube envMap;
#elif defined( ENVMAP_TYPE_CUBE_UV )
	uniform sampler2D envMap;
#endif
uniform float flipEnvMap;
uniform float backgroundBlurriness;
uniform float backgroundIntensity;
uniform mat3 backgroundRotation;
varying vec3 vWorldDirection;
#include <cube_uv_reflection_fragment>
void main() {
	#ifdef ENVMAP_TYPE_CUBE
		vec4 texColor = textureCube( envMap, backgroundRotation * vec3( flipEnvMap * vWorldDirection.x, vWorldDirection.yz ) );
	#elif defined( ENVMAP_TYPE_CUBE_UV )
		vec4 texColor = textureCubeUV( envMap, backgroundRotation * vWorldDirection, backgroundBlurriness );
	#else
		vec4 texColor = vec4( 0.0, 0.0, 0.0, 1.0 );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Mm=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,bm=`uniform samplerCube tCube;
uniform float tFlip;
uniform float opacity;
varying vec3 vWorldDirection;
void main() {
	vec4 texColor = textureCube( tCube, vec3( tFlip * vWorldDirection.x, vWorldDirection.yz ) );
	gl_FragColor = texColor;
	gl_FragColor.a *= opacity;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Sm=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
varying vec2 vHighPrecisionZW;
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vHighPrecisionZW = gl_Position.zw;
}`,wm=`#if DEPTH_PACKING == 3200
	uniform float opacity;
#endif
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
varying vec2 vHighPrecisionZW;
void main() {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#if DEPTH_PACKING == 3200
		diffuseColor.a = opacity;
	#endif
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <logdepthbuf_fragment>
	float fragCoordZ = 0.5 * vHighPrecisionZW[0] / vHighPrecisionZW[1] + 0.5;
	#if DEPTH_PACKING == 3200
		gl_FragColor = vec4( vec3( 1.0 - fragCoordZ ), opacity );
	#elif DEPTH_PACKING == 3201
		gl_FragColor = packDepthToRGBA( fragCoordZ );
	#elif DEPTH_PACKING == 3202
		gl_FragColor = vec4( packDepthToRGB( fragCoordZ ), 1.0 );
	#elif DEPTH_PACKING == 3203
		gl_FragColor = vec4( packDepthToRG( fragCoordZ ), 0.0, 1.0 );
	#endif
}`,Em=`#define DISTANCE
varying vec3 vWorldPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <worldpos_vertex>
	#include <clipping_planes_vertex>
	vWorldPosition = worldPosition.xyz;
}`,Tm=`#define DISTANCE
uniform vec3 referencePosition;
uniform float nearDistance;
uniform float farDistance;
varying vec3 vWorldPosition;
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <clipping_planes_pars_fragment>
void main () {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	float dist = length( vWorldPosition - referencePosition );
	dist = ( dist - nearDistance ) / ( farDistance - nearDistance );
	dist = saturate( dist );
	gl_FragColor = packDepthToRGBA( dist );
}`,Am=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
}`,Rm=`uniform sampler2D tEquirect;
varying vec3 vWorldDirection;
#include <common>
void main() {
	vec3 direction = normalize( vWorldDirection );
	vec2 sampleUV = equirectUv( direction );
	gl_FragColor = texture2D( tEquirect, sampleUV );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Cm=`uniform float scale;
attribute float lineDistance;
varying float vLineDistance;
#include <common>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	vLineDistance = scale * lineDistance;
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,Im=`uniform vec3 diffuse;
uniform float opacity;
uniform float dashSize;
uniform float totalSize;
varying float vLineDistance;
#include <common>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	if ( mod( vLineDistance, totalSize ) > dashSize ) {
		discard;
	}
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,Pm=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#if defined ( USE_ENVMAP ) || defined ( USE_SKINNING )
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinbase_vertex>
		#include <skinnormal_vertex>
		#include <defaultnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <fog_vertex>
}`,Lm=`uniform vec3 diffuse;
uniform float opacity;
#ifndef FLAT_SHADED
	varying vec3 vNormal;
#endif
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		reflectedLight.indirectDiffuse += lightMapTexel.rgb * lightMapIntensity * RECIPROCAL_PI;
	#else
		reflectedLight.indirectDiffuse += vec3( 1.0 );
	#endif
	#include <aomap_fragment>
	reflectedLight.indirectDiffuse *= diffuseColor.rgb;
	vec3 outgoingLight = reflectedLight.indirectDiffuse;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Dm=`#define LAMBERT
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,Um=`#define LAMBERT
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_lambert_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_lambert_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Nm=`#define MATCAP
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <displacementmap_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
	vViewPosition = - mvPosition.xyz;
}`,Fm=`#define MATCAP
uniform vec3 diffuse;
uniform float opacity;
uniform sampler2D matcap;
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	vec3 viewDir = normalize( vViewPosition );
	vec3 x = normalize( vec3( viewDir.z, 0.0, - viewDir.x ) );
	vec3 y = cross( viewDir, x );
	vec2 uv = vec2( dot( x, normal ), dot( y, normal ) ) * 0.495 + 0.5;
	#ifdef USE_MATCAP
		vec4 matcapColor = texture2D( matcap, uv );
	#else
		vec4 matcapColor = vec4( vec3( mix( 0.2, 0.8, uv.y ) ), 1.0 );
	#endif
	vec3 outgoingLight = diffuseColor.rgb * matcapColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Om=`#define NORMAL
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	vViewPosition = - mvPosition.xyz;
#endif
}`,Bm=`#define NORMAL
uniform float opacity;
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <packing>
#include <uv_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( 0.0, 0.0, 0.0, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	gl_FragColor = vec4( packNormalToRGB( normal ), diffuseColor.a );
	#ifdef OPAQUE
		gl_FragColor.a = 1.0;
	#endif
}`,zm=`#define PHONG
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,km=`#define PHONG
uniform vec3 diffuse;
uniform vec3 emissive;
uniform vec3 specular;
uniform float shininess;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_phong_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_phong_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + reflectedLight.directSpecular + reflectedLight.indirectSpecular + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Hm=`#define STANDARD
varying vec3 vViewPosition;
#ifdef USE_TRANSMISSION
	varying vec3 vWorldPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
#ifdef USE_TRANSMISSION
	vWorldPosition = worldPosition.xyz;
#endif
}`,Vm=`#define STANDARD
#ifdef PHYSICAL
	#define IOR
	#define USE_SPECULAR
#endif
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float roughness;
uniform float metalness;
uniform float opacity;
#ifdef IOR
	uniform float ior;
#endif
#ifdef USE_SPECULAR
	uniform float specularIntensity;
	uniform vec3 specularColor;
	#ifdef USE_SPECULAR_COLORMAP
		uniform sampler2D specularColorMap;
	#endif
	#ifdef USE_SPECULAR_INTENSITYMAP
		uniform sampler2D specularIntensityMap;
	#endif
#endif
#ifdef USE_CLEARCOAT
	uniform float clearcoat;
	uniform float clearcoatRoughness;
#endif
#ifdef USE_DISPERSION
	uniform float dispersion;
#endif
#ifdef USE_IRIDESCENCE
	uniform float iridescence;
	uniform float iridescenceIOR;
	uniform float iridescenceThicknessMinimum;
	uniform float iridescenceThicknessMaximum;
#endif
#ifdef USE_SHEEN
	uniform vec3 sheenColor;
	uniform float sheenRoughness;
	#ifdef USE_SHEEN_COLORMAP
		uniform sampler2D sheenColorMap;
	#endif
	#ifdef USE_SHEEN_ROUGHNESSMAP
		uniform sampler2D sheenRoughnessMap;
	#endif
#endif
#ifdef USE_ANISOTROPY
	uniform vec2 anisotropyVector;
	#ifdef USE_ANISOTROPYMAP
		uniform sampler2D anisotropyMap;
	#endif
#endif
varying vec3 vViewPosition;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <iridescence_fragment>
#include <cube_uv_reflection_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_physical_pars_fragment>
#include <transmission_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <clearcoat_pars_fragment>
#include <iridescence_pars_fragment>
#include <roughnessmap_pars_fragment>
#include <metalnessmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <roughnessmap_fragment>
	#include <metalnessmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <clearcoat_normal_fragment_begin>
	#include <clearcoat_normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_physical_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 totalDiffuse = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse;
	vec3 totalSpecular = reflectedLight.directSpecular + reflectedLight.indirectSpecular;
	#include <transmission_fragment>
	vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;
	#ifdef USE_SHEEN
		float sheenEnergyComp = 1.0 - 0.157 * max3( material.sheenColor );
		outgoingLight = outgoingLight * sheenEnergyComp + sheenSpecularDirect + sheenSpecularIndirect;
	#endif
	#ifdef USE_CLEARCOAT
		float dotNVcc = saturate( dot( geometryClearcoatNormal, geometryViewDir ) );
		vec3 Fcc = F_Schlick( material.clearcoatF0, material.clearcoatF90, dotNVcc );
		outgoingLight = outgoingLight * ( 1.0 - material.clearcoat * Fcc ) + ( clearcoatSpecularDirect + clearcoatSpecularIndirect ) * material.clearcoat;
	#endif
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Gm=`#define TOON
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,Wm=`#define TOON
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <gradientmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_toon_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_toon_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Xm=`uniform float size;
uniform float scale;
#include <common>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
#ifdef USE_POINTS_UV
	varying vec2 vUv;
	uniform mat3 uvTransform;
#endif
void main() {
	#ifdef USE_POINTS_UV
		vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	#endif
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	gl_PointSize = size;
	#ifdef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) gl_PointSize *= ( scale / - mvPosition.z );
	#endif
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <fog_vertex>
}`,qm=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <color_pars_fragment>
#include <map_particle_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_particle_fragment>
	#include <color_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,Ym=`#include <common>
#include <batching_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <shadowmap_pars_vertex>
void main() {
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,$m=`uniform vec3 color;
uniform float opacity;
#include <common>
#include <packing>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <logdepthbuf_pars_fragment>
#include <shadowmap_pars_fragment>
#include <shadowmask_pars_fragment>
void main() {
	#include <logdepthbuf_fragment>
	gl_FragColor = vec4( color, opacity * ( 1.0 - getShadowMask() ) );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,Zm=`uniform float rotation;
uniform vec2 center;
#include <common>
#include <uv_pars_vertex>
#include <fog_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	vec4 mvPosition = modelViewMatrix[ 3 ];
	vec2 scale = vec2( length( modelMatrix[ 0 ].xyz ), length( modelMatrix[ 1 ].xyz ) );
	#ifndef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) scale *= - mvPosition.z;
	#endif
	vec2 alignedPosition = ( position.xy - ( center - vec2( 0.5 ) ) ) * scale;
	vec2 rotatedPosition;
	rotatedPosition.x = cos( rotation ) * alignedPosition.x - sin( rotation ) * alignedPosition.y;
	rotatedPosition.y = sin( rotation ) * alignedPosition.x + cos( rotation ) * alignedPosition.y;
	mvPosition.xy += rotatedPosition;
	gl_Position = projectionMatrix * mvPosition;
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,Km=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,Ve={alphahash_fragment:xd,alphahash_pars_fragment:_d,alphamap_fragment:yd,alphamap_pars_fragment:Md,alphatest_fragment:bd,alphatest_pars_fragment:Sd,aomap_fragment:wd,aomap_pars_fragment:Ed,batching_pars_vertex:Td,batching_vertex:Ad,begin_vertex:Rd,beginnormal_vertex:Cd,bsdfs:Id,iridescence_fragment:Pd,bumpmap_pars_fragment:Ld,clipping_planes_fragment:Dd,clipping_planes_pars_fragment:Ud,clipping_planes_pars_vertex:Nd,clipping_planes_vertex:Fd,color_fragment:Od,color_pars_fragment:Bd,color_pars_vertex:zd,color_vertex:kd,common:Hd,cube_uv_reflection_fragment:Vd,defaultnormal_vertex:Gd,displacementmap_pars_vertex:Wd,displacementmap_vertex:Xd,emissivemap_fragment:qd,emissivemap_pars_fragment:Yd,colorspace_fragment:$d,colorspace_pars_fragment:Zd,envmap_fragment:Kd,envmap_common_pars_fragment:Jd,envmap_pars_fragment:jd,envmap_pars_vertex:Qd,envmap_physical_pars_fragment:up,envmap_vertex:ep,fog_vertex:tp,fog_pars_vertex:np,fog_fragment:ip,fog_pars_fragment:sp,gradientmap_pars_fragment:rp,lightmap_pars_fragment:op,lights_lambert_fragment:ap,lights_lambert_pars_fragment:cp,lights_pars_begin:lp,lights_toon_fragment:hp,lights_toon_pars_fragment:fp,lights_phong_fragment:dp,lights_phong_pars_fragment:pp,lights_physical_fragment:mp,lights_physical_pars_fragment:gp,lights_fragment_begin:vp,lights_fragment_maps:xp,lights_fragment_end:_p,logdepthbuf_fragment:yp,logdepthbuf_pars_fragment:Mp,logdepthbuf_pars_vertex:bp,logdepthbuf_vertex:Sp,map_fragment:wp,map_pars_fragment:Ep,map_particle_fragment:Tp,map_particle_pars_fragment:Ap,metalnessmap_fragment:Rp,metalnessmap_pars_fragment:Cp,morphinstance_vertex:Ip,morphcolor_vertex:Pp,morphnormal_vertex:Lp,morphtarget_pars_vertex:Dp,morphtarget_vertex:Up,normal_fragment_begin:Np,normal_fragment_maps:Fp,normal_pars_fragment:Op,normal_pars_vertex:Bp,normal_vertex:zp,normalmap_pars_fragment:kp,clearcoat_normal_fragment_begin:Hp,clearcoat_normal_fragment_maps:Vp,clearcoat_pars_fragment:Gp,iridescence_pars_fragment:Wp,opaque_fragment:Xp,packing:qp,premultiplied_alpha_fragment:Yp,project_vertex:$p,dithering_fragment:Zp,dithering_pars_fragment:Kp,roughnessmap_fragment:Jp,roughnessmap_pars_fragment:jp,shadowmap_pars_fragment:Qp,shadowmap_pars_vertex:em,shadowmap_vertex:tm,shadowmask_pars_fragment:nm,skinbase_vertex:im,skinning_pars_vertex:sm,skinning_vertex:rm,skinnormal_vertex:om,specularmap_fragment:am,specularmap_pars_fragment:cm,tonemapping_fragment:lm,tonemapping_pars_fragment:um,transmission_fragment:hm,transmission_pars_fragment:fm,uv_pars_fragment:dm,uv_pars_vertex:pm,uv_vertex:mm,worldpos_vertex:gm,background_vert:vm,background_frag:xm,backgroundCube_vert:_m,backgroundCube_frag:ym,cube_vert:Mm,cube_frag:bm,depth_vert:Sm,depth_frag:wm,distanceRGBA_vert:Em,distanceRGBA_frag:Tm,equirect_vert:Am,equirect_frag:Rm,linedashed_vert:Cm,linedashed_frag:Im,meshbasic_vert:Pm,meshbasic_frag:Lm,meshlambert_vert:Dm,meshlambert_frag:Um,meshmatcap_vert:Nm,meshmatcap_frag:Fm,meshnormal_vert:Om,meshnormal_frag:Bm,meshphong_vert:zm,meshphong_frag:km,meshphysical_vert:Hm,meshphysical_frag:Vm,meshtoon_vert:Gm,meshtoon_frag:Wm,points_vert:Xm,points_frag:qm,shadow_vert:Ym,shadow_frag:$m,sprite_vert:Zm,sprite_frag:Km},he={common:{diffuse:{value:new ve(16777215)},opacity:{value:1},map:{value:null},mapTransform:{value:new ke},alphaMap:{value:null},alphaMapTransform:{value:new ke},alphaTest:{value:0}},specularmap:{specularMap:{value:null},specularMapTransform:{value:new ke}},envmap:{envMap:{value:null},envMapRotation:{value:new ke},flipEnvMap:{value:-1},reflectivity:{value:1},ior:{value:1.5},refractionRatio:{value:.98}},aomap:{aoMap:{value:null},aoMapIntensity:{value:1},aoMapTransform:{value:new ke}},lightmap:{lightMap:{value:null},lightMapIntensity:{value:1},lightMapTransform:{value:new ke}},bumpmap:{bumpMap:{value:null},bumpMapTransform:{value:new ke},bumpScale:{value:1}},normalmap:{normalMap:{value:null},normalMapTransform:{value:new ke},normalScale:{value:new le(1,1)}},displacementmap:{displacementMap:{value:null},displacementMapTransform:{value:new ke},displacementScale:{value:1},displacementBias:{value:0}},emissivemap:{emissiveMap:{value:null},emissiveMapTransform:{value:new ke}},metalnessmap:{metalnessMap:{value:null},metalnessMapTransform:{value:new ke}},roughnessmap:{roughnessMap:{value:null},roughnessMapTransform:{value:new ke}},gradientmap:{gradientMap:{value:null}},fog:{fogDensity:{value:25e-5},fogNear:{value:1},fogFar:{value:2e3},fogColor:{value:new ve(16777215)}},lights:{ambientLightColor:{value:[]},lightProbe:{value:[]},directionalLights:{value:[],properties:{direction:{},color:{}}},directionalLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},directionalShadowMap:{value:[]},directionalShadowMatrix:{value:[]},spotLights:{value:[],properties:{color:{},position:{},direction:{},distance:{},coneCos:{},penumbraCos:{},decay:{}}},spotLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},spotLightMap:{value:[]},spotShadowMap:{value:[]},spotLightMatrix:{value:[]},pointLights:{value:[],properties:{color:{},position:{},decay:{},distance:{}}},pointLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{},shadowCameraNear:{},shadowCameraFar:{}}},pointShadowMap:{value:[]},pointShadowMatrix:{value:[]},hemisphereLights:{value:[],properties:{direction:{},skyColor:{},groundColor:{}}},rectAreaLights:{value:[],properties:{color:{},position:{},width:{},height:{}}},ltc_1:{value:null},ltc_2:{value:null}},points:{diffuse:{value:new ve(16777215)},opacity:{value:1},size:{value:1},scale:{value:1},map:{value:null},alphaMap:{value:null},alphaMapTransform:{value:new ke},alphaTest:{value:0},uvTransform:{value:new ke}},sprite:{diffuse:{value:new ve(16777215)},opacity:{value:1},center:{value:new le(.5,.5)},rotation:{value:0},map:{value:null},mapTransform:{value:new ke},alphaMap:{value:null},alphaMapTransform:{value:new ke},alphaTest:{value:0}}},In={basic:{uniforms:qt([he.common,he.specularmap,he.envmap,he.aomap,he.lightmap,he.fog]),vertexShader:Ve.meshbasic_vert,fragmentShader:Ve.meshbasic_frag},lambert:{uniforms:qt([he.common,he.specularmap,he.envmap,he.aomap,he.lightmap,he.emissivemap,he.bumpmap,he.normalmap,he.displacementmap,he.fog,he.lights,{emissive:{value:new ve(0)}}]),vertexShader:Ve.meshlambert_vert,fragmentShader:Ve.meshlambert_frag},phong:{uniforms:qt([he.common,he.specularmap,he.envmap,he.aomap,he.lightmap,he.emissivemap,he.bumpmap,he.normalmap,he.displacementmap,he.fog,he.lights,{emissive:{value:new ve(0)},specular:{value:new ve(1118481)},shininess:{value:30}}]),vertexShader:Ve.meshphong_vert,fragmentShader:Ve.meshphong_frag},standard:{uniforms:qt([he.common,he.envmap,he.aomap,he.lightmap,he.emissivemap,he.bumpmap,he.normalmap,he.displacementmap,he.roughnessmap,he.metalnessmap,he.fog,he.lights,{emissive:{value:new ve(0)},roughness:{value:1},metalness:{value:0},envMapIntensity:{value:1}}]),vertexShader:Ve.meshphysical_vert,fragmentShader:Ve.meshphysical_frag},toon:{uniforms:qt([he.common,he.aomap,he.lightmap,he.emissivemap,he.bumpmap,he.normalmap,he.displacementmap,he.gradientmap,he.fog,he.lights,{emissive:{value:new ve(0)}}]),vertexShader:Ve.meshtoon_vert,fragmentShader:Ve.meshtoon_frag},matcap:{uniforms:qt([he.common,he.bumpmap,he.normalmap,he.displacementmap,he.fog,{matcap:{value:null}}]),vertexShader:Ve.meshmatcap_vert,fragmentShader:Ve.meshmatcap_frag},points:{uniforms:qt([he.points,he.fog]),vertexShader:Ve.points_vert,fragmentShader:Ve.points_frag},dashed:{uniforms:qt([he.common,he.fog,{scale:{value:1},dashSize:{value:1},totalSize:{value:2}}]),vertexShader:Ve.linedashed_vert,fragmentShader:Ve.linedashed_frag},depth:{uniforms:qt([he.common,he.displacementmap]),vertexShader:Ve.depth_vert,fragmentShader:Ve.depth_frag},normal:{uniforms:qt([he.common,he.bumpmap,he.normalmap,he.displacementmap,{opacity:{value:1}}]),vertexShader:Ve.meshnormal_vert,fragmentShader:Ve.meshnormal_frag},sprite:{uniforms:qt([he.sprite,he.fog]),vertexShader:Ve.sprite_vert,fragmentShader:Ve.sprite_frag},background:{uniforms:{uvTransform:{value:new ke},t2D:{value:null},backgroundIntensity:{value:1}},vertexShader:Ve.background_vert,fragmentShader:Ve.background_frag},backgroundCube:{uniforms:{envMap:{value:null},flipEnvMap:{value:-1},backgroundBlurriness:{value:0},backgroundIntensity:{value:1},backgroundRotation:{value:new ke}},vertexShader:Ve.backgroundCube_vert,fragmentShader:Ve.backgroundCube_frag},cube:{uniforms:{tCube:{value:null},tFlip:{value:-1},opacity:{value:1}},vertexShader:Ve.cube_vert,fragmentShader:Ve.cube_frag},equirect:{uniforms:{tEquirect:{value:null}},vertexShader:Ve.equirect_vert,fragmentShader:Ve.equirect_frag},distanceRGBA:{uniforms:qt([he.common,he.displacementmap,{referencePosition:{value:new P},nearDistance:{value:1},farDistance:{value:1e3}}]),vertexShader:Ve.distanceRGBA_vert,fragmentShader:Ve.distanceRGBA_frag},shadow:{uniforms:qt([he.lights,he.fog,{color:{value:new ve(0)},opacity:{value:1}}]),vertexShader:Ve.shadow_vert,fragmentShader:Ve.shadow_frag}};In.physical={uniforms:qt([In.standard.uniforms,{clearcoat:{value:0},clearcoatMap:{value:null},clearcoatMapTransform:{value:new ke},clearcoatNormalMap:{value:null},clearcoatNormalMapTransform:{value:new ke},clearcoatNormalScale:{value:new le(1,1)},clearcoatRoughness:{value:0},clearcoatRoughnessMap:{value:null},clearcoatRoughnessMapTransform:{value:new ke},dispersion:{value:0},iridescence:{value:0},iridescenceMap:{value:null},iridescenceMapTransform:{value:new ke},iridescenceIOR:{value:1.3},iridescenceThicknessMinimum:{value:100},iridescenceThicknessMaximum:{value:400},iridescenceThicknessMap:{value:null},iridescenceThicknessMapTransform:{value:new ke},sheen:{value:0},sheenColor:{value:new ve(0)},sheenColorMap:{value:null},sheenColorMapTransform:{value:new ke},sheenRoughness:{value:1},sheenRoughnessMap:{value:null},sheenRoughnessMapTransform:{value:new ke},transmission:{value:0},transmissionMap:{value:null},transmissionMapTransform:{value:new ke},transmissionSamplerSize:{value:new le},transmissionSamplerMap:{value:null},thickness:{value:0},thicknessMap:{value:null},thicknessMapTransform:{value:new ke},attenuationDistance:{value:0},attenuationColor:{value:new ve(0)},specularColor:{value:new ve(1,1,1)},specularColorMap:{value:null},specularColorMapTransform:{value:new ke},specularIntensity:{value:1},specularIntensityMap:{value:null},specularIntensityMapTransform:{value:new ke},anisotropyVector:{value:new le},anisotropyMap:{value:null},anisotropyMapTransform:{value:new ke}}]),vertexShader:Ve.meshphysical_vert,fragmentShader:Ve.meshphysical_frag};var Pr={r:0,b:0,g:0},Ai=new pn,Jm=new Le;function jm(s,e,t,n,i,r,o){let a=new ve(0),c=r===!0?0:1,l,u,h=null,f=0,p=null;function g(M){let b=M.isScene===!0?M.background:null;return b&&b.isTexture&&(b=(M.backgroundBlurriness>0?t:e).get(b)),b}function v(M){let b=!1,_=g(M);_===null?d(a,c):_&&_.isColor&&(d(_,1),b=!0);let C=s.xr.getEnvironmentBlendMode();C==="additive"?n.buffers.color.setClear(0,0,0,1,o):C==="alpha-blend"&&n.buffers.color.setClear(0,0,0,0,o),(s.autoClear||b)&&(n.buffers.depth.setTest(!0),n.buffers.depth.setMask(!0),n.buffers.color.setMask(!0),s.clear(s.autoClearColor,s.autoClearDepth,s.autoClearStencil))}function m(M,b){let _=g(b);_&&(_.isCubeTexture||_.mapping===po)?(u===void 0&&(u=new Fe(new cn(1,1,1),new Gt({name:"BackgroundCubeMaterial",uniforms:ds(In.backgroundCube.uniforms),vertexShader:In.backgroundCube.vertexShader,fragmentShader:In.backgroundCube.fragmentShader,side:Vt,depthTest:!1,depthWrite:!1,fog:!1})),u.geometry.deleteAttribute("normal"),u.geometry.deleteAttribute("uv"),u.onBeforeRender=function(C,A,E){this.matrixWorld.copyPosition(E.matrixWorld)},Object.defineProperty(u.material,"envMap",{get:function(){return this.uniforms.envMap.value}}),i.update(u)),Ai.copy(b.backgroundRotation),Ai.x*=-1,Ai.y*=-1,Ai.z*=-1,_.isCubeTexture&&_.isRenderTargetTexture===!1&&(Ai.y*=-1,Ai.z*=-1),u.material.uniforms.envMap.value=_,u.material.uniforms.flipEnvMap.value=_.isCubeTexture&&_.isRenderTargetTexture===!1?-1:1,u.material.uniforms.backgroundBlurriness.value=b.backgroundBlurriness,u.material.uniforms.backgroundIntensity.value=b.backgroundIntensity,u.material.uniforms.backgroundRotation.value.setFromMatrix4(Jm.makeRotationFromEuler(Ai)),u.material.toneMapped=Ye.getTransfer(_.colorSpace)!==lt,(h!==_||f!==_.version||p!==s.toneMapping)&&(u.material.needsUpdate=!0,h=_,f=_.version,p=s.toneMapping),u.layers.enableAll(),M.unshift(u,u.geometry,u.material,0,0,null)):_&&_.isTexture&&(l===void 0&&(l=new Fe(new $t(2,2),new Gt({name:"BackgroundMaterial",uniforms:ds(In.background.uniforms),vertexShader:In.background.vertexShader,fragmentShader:In.background.fragmentShader,side:en,depthTest:!1,depthWrite:!1,fog:!1})),l.geometry.deleteAttribute("normal"),Object.defineProperty(l.material,"map",{get:function(){return this.uniforms.t2D.value}}),i.update(l)),l.material.uniforms.t2D.value=_,l.material.uniforms.backgroundIntensity.value=b.backgroundIntensity,l.material.toneMapped=Ye.getTransfer(_.colorSpace)!==lt,_.matrixAutoUpdate===!0&&_.updateMatrix(),l.material.uniforms.uvTransform.value.copy(_.matrix),(h!==_||f!==_.version||p!==s.toneMapping)&&(l.material.needsUpdate=!0,h=_,f=_.version,p=s.toneMapping),l.layers.enableAll(),M.unshift(l,l.geometry,l.material,0,0,null))}function d(M,b){M.getRGB(Pr,uh(s)),n.buffers.color.setClear(Pr.r,Pr.g,Pr.b,b,o)}return{getClearColor:function(){return a},setClearColor:function(M,b=1){a.set(M),c=b,d(a,c)},getClearAlpha:function(){return c},setClearAlpha:function(M){c=M,d(a,c)},render:v,addToRenderList:m}}function Qm(s,e){let t=s.getParameter(s.MAX_VERTEX_ATTRIBS),n={},i=f(null),r=i,o=!1;function a(y,T,L,D,F){let X=!1,z=h(D,L,T);r!==z&&(r=z,l(r.object)),X=p(y,D,L,F),X&&g(y,D,L,F),F!==null&&e.update(F,s.ELEMENT_ARRAY_BUFFER),(X||o)&&(o=!1,_(y,T,L,D),F!==null&&s.bindBuffer(s.ELEMENT_ARRAY_BUFFER,e.get(F).buffer))}function c(){return s.createVertexArray()}function l(y){return s.bindVertexArray(y)}function u(y){return s.deleteVertexArray(y)}function h(y,T,L){let D=L.wireframe===!0,F=n[y.id];F===void 0&&(F={},n[y.id]=F);let X=F[T.id];X===void 0&&(X={},F[T.id]=X);let z=X[D];return z===void 0&&(z=f(c()),X[D]=z),z}function f(y){let T=[],L=[],D=[];for(let F=0;F<t;F++)T[F]=0,L[F]=0,D[F]=0;return{geometry:null,program:null,wireframe:!1,newAttributes:T,enabledAttributes:L,attributeDivisors:D,object:y,attributes:{},index:null}}function p(y,T,L,D){let F=r.attributes,X=T.attributes,z=0,K=L.getAttributes();for(let H in K)if(K[H].location>=0){let $=F[H],ie=X[H];if(ie===void 0&&(H==="instanceMatrix"&&y.instanceMatrix&&(ie=y.instanceMatrix),H==="instanceColor"&&y.instanceColor&&(ie=y.instanceColor)),$===void 0||$.attribute!==ie||ie&&$.data!==ie.data)return!0;z++}return r.attributesNum!==z||r.index!==D}function g(y,T,L,D){let F={},X=T.attributes,z=0,K=L.getAttributes();for(let H in K)if(K[H].location>=0){let $=X[H];$===void 0&&(H==="instanceMatrix"&&y.instanceMatrix&&($=y.instanceMatrix),H==="instanceColor"&&y.instanceColor&&($=y.instanceColor));let ie={};ie.attribute=$,$&&$.data&&(ie.data=$.data),F[H]=ie,z++}r.attributes=F,r.attributesNum=z,r.index=D}function v(){let y=r.newAttributes;for(let T=0,L=y.length;T<L;T++)y[T]=0}function m(y){d(y,0)}function d(y,T){let L=r.newAttributes,D=r.enabledAttributes,F=r.attributeDivisors;L[y]=1,D[y]===0&&(s.enableVertexAttribArray(y),D[y]=1),F[y]!==T&&(s.vertexAttribDivisor(y,T),F[y]=T)}function M(){let y=r.newAttributes,T=r.enabledAttributes;for(let L=0,D=T.length;L<D;L++)T[L]!==y[L]&&(s.disableVertexAttribArray(L),T[L]=0)}function b(y,T,L,D,F,X,z){z===!0?s.vertexAttribIPointer(y,T,L,F,X):s.vertexAttribPointer(y,T,L,D,F,X)}function _(y,T,L,D){v();let F=D.attributes,X=L.getAttributes(),z=T.defaultAttributeValues;for(let K in X){let H=X[K];if(H.location>=0){let k=F[K];if(k===void 0&&(K==="instanceMatrix"&&y.instanceMatrix&&(k=y.instanceMatrix),K==="instanceColor"&&y.instanceColor&&(k=y.instanceColor)),k!==void 0){let $=k.normalized,ie=k.itemSize,j=e.get(k);if(j===void 0)continue;let ue=j.buffer,G=j.type,J=j.bytesPerElement,re=G===s.INT||G===s.UNSIGNED_INT||k.gpuType===_c;if(k.isInterleavedBufferAttribute){let ee=k.data,oe=ee.stride,ye=k.offset;if(ee.isInstancedInterleavedBuffer){for(let De=0;De<H.locationSize;De++)d(H.location+De,ee.meshPerAttribute);y.isInstancedMesh!==!0&&D._maxInstanceCount===void 0&&(D._maxInstanceCount=ee.meshPerAttribute*ee.count)}else for(let De=0;De<H.locationSize;De++)m(H.location+De);s.bindBuffer(s.ARRAY_BUFFER,ue);for(let De=0;De<H.locationSize;De++)b(H.location+De,ie/H.locationSize,G,$,oe*J,(ye+ie/H.locationSize*De)*J,re)}else{if(k.isInstancedBufferAttribute){for(let ee=0;ee<H.locationSize;ee++)d(H.location+ee,k.meshPerAttribute);y.isInstancedMesh!==!0&&D._maxInstanceCount===void 0&&(D._maxInstanceCount=k.meshPerAttribute*k.count)}else for(let ee=0;ee<H.locationSize;ee++)m(H.location+ee);s.bindBuffer(s.ARRAY_BUFFER,ue);for(let ee=0;ee<H.locationSize;ee++)b(H.location+ee,ie/H.locationSize,G,$,ie*J,ie/H.locationSize*ee*J,re)}}else if(z!==void 0){let $=z[K];if($!==void 0)switch($.length){case 2:s.vertexAttrib2fv(H.location,$);break;case 3:s.vertexAttrib3fv(H.location,$);break;case 4:s.vertexAttrib4fv(H.location,$);break;default:s.vertexAttrib1fv(H.location,$)}}}}M()}function C(){I();for(let y in n){let T=n[y];for(let L in T){let D=T[L];for(let F in D)u(D[F].object),delete D[F];delete T[L]}delete n[y]}}function A(y){if(n[y.id]===void 0)return;let T=n[y.id];for(let L in T){let D=T[L];for(let F in D)u(D[F].object),delete D[F];delete T[L]}delete n[y.id]}function E(y){for(let T in n){let L=n[T];if(L[y.id]===void 0)continue;let D=L[y.id];for(let F in D)u(D[F].object),delete D[F];delete L[y.id]}}function I(){x(),o=!0,r!==i&&(r=i,l(r.object))}function x(){i.geometry=null,i.program=null,i.wireframe=!1}return{setup:a,reset:I,resetDefaultState:x,dispose:C,releaseStatesOfGeometry:A,releaseStatesOfProgram:E,initAttributes:v,enableAttribute:m,disableUnusedAttributes:M}}function e0(s,e,t){let n;function i(l){n=l}function r(l,u){s.drawArrays(n,l,u),t.update(u,n,1)}function o(l,u,h){h!==0&&(s.drawArraysInstanced(n,l,u,h),t.update(u,n,h))}function a(l,u,h){if(h===0)return;e.get("WEBGL_multi_draw").multiDrawArraysWEBGL(n,l,0,u,0,h);let p=0;for(let g=0;g<h;g++)p+=u[g];t.update(p,n,1)}function c(l,u,h,f){if(h===0)return;let p=e.get("WEBGL_multi_draw");if(p===null)for(let g=0;g<l.length;g++)o(l[g],u[g],f[g]);else{p.multiDrawArraysInstancedWEBGL(n,l,0,u,0,f,0,h);let g=0;for(let v=0;v<h;v++)g+=u[v]*f[v];t.update(g,n,1)}}this.setMode=i,this.render=r,this.renderInstances=o,this.renderMultiDraw=a,this.renderMultiDrawInstances=c}function t0(s,e,t,n){let i;function r(){if(i!==void 0)return i;if(e.has("EXT_texture_filter_anisotropic")===!0){let E=e.get("EXT_texture_filter_anisotropic");i=s.getParameter(E.MAX_TEXTURE_MAX_ANISOTROPY_EXT)}else i=0;return i}function o(E){return!(E!==Ht&&n.convert(E)!==s.getParameter(s.IMPLEMENTATION_COLOR_READ_FORMAT))}function a(E){let I=E===$e&&(e.has("EXT_color_buffer_half_float")||e.has("EXT_color_buffer_float"));return!(E!==Dt&&n.convert(E)!==s.getParameter(s.IMPLEMENTATION_COLOR_READ_TYPE)&&E!==Tn&&!I)}function c(E){if(E==="highp"){if(s.getShaderPrecisionFormat(s.VERTEX_SHADER,s.HIGH_FLOAT).precision>0&&s.getShaderPrecisionFormat(s.FRAGMENT_SHADER,s.HIGH_FLOAT).precision>0)return"highp";E="mediump"}return E==="mediump"&&s.getShaderPrecisionFormat(s.VERTEX_SHADER,s.MEDIUM_FLOAT).precision>0&&s.getShaderPrecisionFormat(s.FRAGMENT_SHADER,s.MEDIUM_FLOAT).precision>0?"mediump":"lowp"}let l=t.precision!==void 0?t.precision:"highp",u=c(l);u!==l&&(console.warn("THREE.WebGLRenderer:",l,"not supported, using",u,"instead."),l=u);let h=t.logarithmicDepthBuffer===!0,f=t.reverseDepthBuffer===!0&&e.has("EXT_clip_control"),p=s.getParameter(s.MAX_TEXTURE_IMAGE_UNITS),g=s.getParameter(s.MAX_VERTEX_TEXTURE_IMAGE_UNITS),v=s.getParameter(s.MAX_TEXTURE_SIZE),m=s.getParameter(s.MAX_CUBE_MAP_TEXTURE_SIZE),d=s.getParameter(s.MAX_VERTEX_ATTRIBS),M=s.getParameter(s.MAX_VERTEX_UNIFORM_VECTORS),b=s.getParameter(s.MAX_VARYING_VECTORS),_=s.getParameter(s.MAX_FRAGMENT_UNIFORM_VECTORS),C=g>0,A=s.getParameter(s.MAX_SAMPLES);return{isWebGL2:!0,getMaxAnisotropy:r,getMaxPrecision:c,textureFormatReadable:o,textureTypeReadable:a,precision:l,logarithmicDepthBuffer:h,reverseDepthBuffer:f,maxTextures:p,maxVertexTextures:g,maxTextureSize:v,maxCubemapSize:m,maxAttributes:d,maxVertexUniforms:M,maxVaryings:b,maxFragmentUniforms:_,vertexTextures:C,maxSamples:A}}function n0(s){let e=this,t=null,n=0,i=!1,r=!1,o=new Sn,a=new ke,c={value:null,needsUpdate:!1};this.uniform=c,this.numPlanes=0,this.numIntersection=0,this.init=function(h,f){let p=h.length!==0||f||n!==0||i;return i=f,n=h.length,p},this.beginShadows=function(){r=!0,u(null)},this.endShadows=function(){r=!1},this.setGlobalState=function(h,f){t=u(h,f,0)},this.setState=function(h,f,p){let g=h.clippingPlanes,v=h.clipIntersection,m=h.clipShadows,d=s.get(h);if(!i||g===null||g.length===0||r&&!m)r?u(null):l();else{let M=r?0:n,b=M*4,_=d.clippingState||null;c.value=_,_=u(g,f,b,p);for(let C=0;C!==b;++C)_[C]=t[C];d.clippingState=_,this.numIntersection=v?this.numPlanes:0,this.numPlanes+=M}};function l(){c.value!==t&&(c.value=t,c.needsUpdate=n>0),e.numPlanes=n,e.numIntersection=0}function u(h,f,p,g){let v=h!==null?h.length:0,m=null;if(v!==0){if(m=c.value,g!==!0||m===null){let d=p+v*4,M=f.matrixWorldInverse;a.getNormalMatrix(M),(m===null||m.length<d)&&(m=new Float32Array(d));for(let b=0,_=p;b!==v;++b,_+=4)o.copy(h[b]).applyMatrix4(M,a),o.normal.toArray(m,_),m[_+3]=o.constant}c.value=m,c.needsUpdate=!0}return e.numPlanes=v,e.numIntersection=0,m}}function i0(s){let e=new WeakMap;function t(o,a){return a===da?o.mapping=rs:a===pa&&(o.mapping=os),o}function n(o){if(o&&o.isTexture){let a=o.mapping;if(a===da||a===pa)if(e.has(o)){let c=e.get(o).texture;return t(c,o.mapping)}else{let c=o.image;if(c&&c.height>0){let l=new qa(c.height);return l.fromEquirectangularTexture(s,o),e.set(o,l),o.addEventListener("dispose",i),t(l.texture,o.mapping)}else return null}}return o}function i(o){let a=o.target;a.removeEventListener("dispose",i);let c=e.get(a);c!==void 0&&(e.delete(a),c.dispose())}function r(){e=new WeakMap}return{get:n,dispose:r}}var hi=class extends jr{constructor(e=-1,t=1,n=1,i=-1,r=.1,o=2e3){super(),this.isOrthographicCamera=!0,this.type="OrthographicCamera",this.zoom=1,this.view=null,this.left=e,this.right=t,this.top=n,this.bottom=i,this.near=r,this.far=o,this.updateProjectionMatrix()}copy(e,t){return super.copy(e,t),this.left=e.left,this.right=e.right,this.top=e.top,this.bottom=e.bottom,this.near=e.near,this.far=e.far,this.zoom=e.zoom,this.view=e.view===null?null:Object.assign({},e.view),this}setViewOffset(e,t,n,i,r,o){this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=e,this.view.fullHeight=t,this.view.offsetX=n,this.view.offsetY=i,this.view.width=r,this.view.height=o,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let e=(this.right-this.left)/(2*this.zoom),t=(this.top-this.bottom)/(2*this.zoom),n=(this.right+this.left)/2,i=(this.top+this.bottom)/2,r=n-e,o=n+e,a=i+t,c=i-t;if(this.view!==null&&this.view.enabled){let l=(this.right-this.left)/this.view.fullWidth/this.zoom,u=(this.top-this.bottom)/this.view.fullHeight/this.zoom;r+=l*this.view.offsetX,o=r+l*this.view.width,a-=u*this.view.offsetY,c=a-u*this.view.height}this.projectionMatrix.makeOrthographic(r,o,a,c,this.near,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(e){let t=super.toJSON(e);return t.object.zoom=this.zoom,t.object.left=this.left,t.object.right=this.right,t.object.top=this.top,t.object.bottom=this.bottom,t.object.near=this.near,t.object.far=this.far,this.view!==null&&(t.object.view=Object.assign({},this.view)),t}},ji=4,ru=[.125,.215,.35,.446,.526,.582],Li=20,Yo=new hi,ou=new ve,$o=null,Zo=0,Ko=0,Jo=!1,Ci=(1+Math.sqrt(5))/2,Zi=1/Ci,au=[new P(-Ci,Zi,0),new P(Ci,Zi,0),new P(-Zi,0,Ci),new P(Zi,0,Ci),new P(0,Ci,-Zi),new P(0,Ci,Zi),new P(-1,1,-1),new P(1,1,-1),new P(-1,1,1),new P(1,1,1)],ps=class{constructor(e){this._renderer=e,this._pingPongRenderTarget=null,this._lodMax=0,this._cubeSize=0,this._lodPlanes=[],this._sizeLods=[],this._sigmas=[],this._blurMaterial=null,this._cubemapMaterial=null,this._equirectMaterial=null,this._compileMaterial(this._blurMaterial)}fromScene(e,t=0,n=.1,i=100){$o=this._renderer.getRenderTarget(),Zo=this._renderer.getActiveCubeFace(),Ko=this._renderer.getActiveMipmapLevel(),Jo=this._renderer.xr.enabled,this._renderer.xr.enabled=!1,this._setSize(256);let r=this._allocateTargets();return r.depthBuffer=!0,this._sceneToCubeUV(e,n,i,r),t>0&&this._blur(r,0,0,t),this._applyPMREM(r),this._cleanup(r),r}fromEquirectangular(e,t=null){return this._fromTexture(e,t)}fromCubemap(e,t=null){return this._fromTexture(e,t)}compileCubemapShader(){this._cubemapMaterial===null&&(this._cubemapMaterial=uu(),this._compileMaterial(this._cubemapMaterial))}compileEquirectangularShader(){this._equirectMaterial===null&&(this._equirectMaterial=lu(),this._compileMaterial(this._equirectMaterial))}dispose(){this._dispose(),this._cubemapMaterial!==null&&this._cubemapMaterial.dispose(),this._equirectMaterial!==null&&this._equirectMaterial.dispose()}_setSize(e){this._lodMax=Math.floor(Math.log2(e)),this._cubeSize=Math.pow(2,this._lodMax)}_dispose(){this._blurMaterial!==null&&this._blurMaterial.dispose(),this._pingPongRenderTarget!==null&&this._pingPongRenderTarget.dispose();for(let e=0;e<this._lodPlanes.length;e++)this._lodPlanes[e].dispose()}_cleanup(e){this._renderer.setRenderTarget($o,Zo,Ko),this._renderer.xr.enabled=Jo,e.scissorTest=!1,Lr(e,0,0,e.width,e.height)}_fromTexture(e,t){e.mapping===rs||e.mapping===os?this._setSize(e.image.length===0?16:e.image[0].width||e.image[0].image.width):this._setSize(e.image.width/4),$o=this._renderer.getRenderTarget(),Zo=this._renderer.getActiveCubeFace(),Ko=this._renderer.getActiveMipmapLevel(),Jo=this._renderer.xr.enabled,this._renderer.xr.enabled=!1;let n=t||this._allocateTargets();return this._textureToCubeUV(e,n),this._applyPMREM(n),this._cleanup(n),n}_allocateTargets(){let e=3*Math.max(this._cubeSize,112),t=4*this._cubeSize,n={magFilter:wt,minFilter:wt,generateMipmaps:!1,type:$e,format:Ht,colorSpace:Wt,depthBuffer:!1},i=cu(e,t,n);if(this._pingPongRenderTarget===null||this._pingPongRenderTarget.width!==e||this._pingPongRenderTarget.height!==t){this._pingPongRenderTarget!==null&&this._dispose(),this._pingPongRenderTarget=cu(e,t,n);let{_lodMax:r}=this;({sizeLods:this._sizeLods,lodPlanes:this._lodPlanes,sigmas:this._sigmas}=s0(r)),this._blurMaterial=r0(r,e,t)}return i}_compileMaterial(e){let t=new Fe(this._lodPlanes[0],e);this._renderer.compile(t,Yo)}_sceneToCubeUV(e,t,n,i){let a=new _t(90,1,t,n),c=[1,-1,1,1,1,1],l=[1,1,1,-1,-1,-1],u=this._renderer,h=u.autoClear,f=u.toneMapping;u.getClearColor(ou),u.toneMapping=Ln,u.autoClear=!1;let p=new Yt({name:"PMREM.Background",side:Vt,depthWrite:!1,depthTest:!1}),g=new Fe(new cn,p),v=!1,m=e.background;m?m.isColor&&(p.color.copy(m),e.background=null,v=!0):(p.color.copy(ou),v=!0);for(let d=0;d<6;d++){let M=d%3;M===0?(a.up.set(0,c[d],0),a.lookAt(l[d],0,0)):M===1?(a.up.set(0,0,c[d]),a.lookAt(0,l[d],0)):(a.up.set(0,c[d],0),a.lookAt(0,0,l[d]));let b=this._cubeSize;Lr(i,M*b,d>2?b:0,b,b),u.setRenderTarget(i),v&&u.render(g,a),u.render(e,a)}g.geometry.dispose(),g.material.dispose(),u.toneMapping=f,u.autoClear=h,e.background=m}_textureToCubeUV(e,t){let n=this._renderer,i=e.mapping===rs||e.mapping===os;i?(this._cubemapMaterial===null&&(this._cubemapMaterial=uu()),this._cubemapMaterial.uniforms.flipEnvMap.value=e.isRenderTargetTexture===!1?-1:1):this._equirectMaterial===null&&(this._equirectMaterial=lu());let r=i?this._cubemapMaterial:this._equirectMaterial,o=new Fe(this._lodPlanes[0],r),a=r.uniforms;a.envMap.value=e;let c=this._cubeSize;Lr(t,0,0,3*c,2*c),n.setRenderTarget(t),n.render(o,Yo)}_applyPMREM(e){let t=this._renderer,n=t.autoClear;t.autoClear=!1;let i=this._lodPlanes.length;for(let r=1;r<i;r++){let o=Math.sqrt(this._sigmas[r]*this._sigmas[r]-this._sigmas[r-1]*this._sigmas[r-1]),a=au[(i-r-1)%au.length];this._blur(e,r-1,r,o,a)}t.autoClear=n}_blur(e,t,n,i,r){let o=this._pingPongRenderTarget;this._halfBlur(e,o,t,n,i,"latitudinal",r),this._halfBlur(o,e,n,n,i,"longitudinal",r)}_halfBlur(e,t,n,i,r,o,a){let c=this._renderer,l=this._blurMaterial;o!=="latitudinal"&&o!=="longitudinal"&&console.error("blur direction must be either latitudinal or longitudinal!");let u=3,h=new Fe(this._lodPlanes[i],l),f=l.uniforms,p=this._sizeLods[n]-1,g=isFinite(r)?Math.PI/(2*p):2*Math.PI/(2*Li-1),v=r/g,m=isFinite(r)?1+Math.floor(u*v):Li;m>Li&&console.warn(`sigmaRadians, ${r}, is too large and will clip, as it requested ${m} samples when the maximum is set to ${Li}`);let d=[],M=0;for(let E=0;E<Li;++E){let I=E/v,x=Math.exp(-I*I/2);d.push(x),E===0?M+=x:E<m&&(M+=2*x)}for(let E=0;E<d.length;E++)d[E]=d[E]/M;f.envMap.value=e.texture,f.samples.value=m,f.weights.value=d,f.latitudinal.value=o==="latitudinal",a&&(f.poleAxis.value=a);let{_lodMax:b}=this;f.dTheta.value=g,f.mipInt.value=b-n;let _=this._sizeLods[i],C=3*_*(i>b-ji?i-b+ji:0),A=4*(this._cubeSize-_);Lr(t,C,A,3*_,2*_),c.setRenderTarget(t),c.render(h,Yo)}};function s0(s){let e=[],t=[],n=[],i=s,r=s-ji+1+ru.length;for(let o=0;o<r;o++){let a=Math.pow(2,i);t.push(a);let c=1/a;o>s-ji?c=ru[o-s+ji-1]:o===0&&(c=0),n.push(c);let l=1/(a-2),u=-l,h=1+l,f=[u,u,h,u,h,h,u,u,h,h,u,h],p=6,g=6,v=3,m=2,d=1,M=new Float32Array(v*g*p),b=new Float32Array(m*g*p),_=new Float32Array(d*g*p);for(let A=0;A<p;A++){let E=A%3*2/3-1,I=A>2?0:-1,x=[E,I,0,E+2/3,I,0,E+2/3,I+1,0,E,I,0,E+2/3,I+1,0,E,I+1,0];M.set(x,v*g*A),b.set(f,m*g*A);let y=[A,A,A,A,A,A];_.set(y,d*g*A)}let C=new Mt;C.setAttribute("position",new it(M,v)),C.setAttribute("uv",new it(b,m)),C.setAttribute("faceIndex",new it(_,d)),e.push(C),i>ji&&i--}return{lodPlanes:e,sizeLods:t,sigmas:n}}function cu(s,e,t){let n=new Rn(s,e,t);return n.texture.mapping=po,n.texture.name="PMREM.cubeUv",n.scissorTest=!0,n}function Lr(s,e,t,n,i){s.viewport.set(e,t,n,i),s.scissor.set(e,t,n,i)}function r0(s,e,t){let n=new Float32Array(Li),i=new P(0,1,0);return new Gt({name:"SphericalGaussianBlur",defines:{n:Li,CUBEUV_TEXEL_WIDTH:1/e,CUBEUV_TEXEL_HEIGHT:1/t,CUBEUV_MAX_MIP:`${s}.0`},uniforms:{envMap:{value:null},samples:{value:1},weights:{value:n},latitudinal:{value:!1},dTheta:{value:0},mipInt:{value:0},poleAxis:{value:i}},vertexShader:Ac(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;
			uniform int samples;
			uniform float weights[ n ];
			uniform bool latitudinal;
			uniform float dTheta;
			uniform float mipInt;
			uniform vec3 poleAxis;

			#define ENVMAP_TYPE_CUBE_UV
			#include <cube_uv_reflection_fragment>

			vec3 getSample( float theta, vec3 axis ) {

				float cosTheta = cos( theta );
				// Rodrigues' axis-angle rotation
				vec3 sampleDirection = vOutputDirection * cosTheta
					+ cross( axis, vOutputDirection ) * sin( theta )
					+ axis * dot( axis, vOutputDirection ) * ( 1.0 - cosTheta );

				return bilinearCubeUV( envMap, sampleDirection, mipInt );

			}

			void main() {

				vec3 axis = latitudinal ? poleAxis : cross( poleAxis, vOutputDirection );

				if ( all( equal( axis, vec3( 0.0 ) ) ) ) {

					axis = vec3( vOutputDirection.z, 0.0, - vOutputDirection.x );

				}

				axis = normalize( axis );

				gl_FragColor = vec4( 0.0, 0.0, 0.0, 1.0 );
				gl_FragColor.rgb += weights[ 0 ] * getSample( 0.0, axis );

				for ( int i = 1; i < n; i++ ) {

					if ( i >= samples ) {

						break;

					}

					float theta = dTheta * float( i );
					gl_FragColor.rgb += weights[ i ] * getSample( -1.0 * theta, axis );
					gl_FragColor.rgb += weights[ i ] * getSample( theta, axis );

				}

			}
		`,blending:li,depthTest:!1,depthWrite:!1})}function lu(){return new Gt({name:"EquirectangularToCubeUV",uniforms:{envMap:{value:null}},vertexShader:Ac(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;

			#include <common>

			void main() {

				vec3 outputDirection = normalize( vOutputDirection );
				vec2 uv = equirectUv( outputDirection );

				gl_FragColor = vec4( texture2D ( envMap, uv ).rgb, 1.0 );

			}
		`,blending:li,depthTest:!1,depthWrite:!1})}function uu(){return new Gt({name:"CubemapToCubeUV",uniforms:{envMap:{value:null},flipEnvMap:{value:-1}},vertexShader:Ac(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			uniform float flipEnvMap;

			varying vec3 vOutputDirection;

			uniform samplerCube envMap;

			void main() {

				gl_FragColor = textureCube( envMap, vec3( flipEnvMap * vOutputDirection.x, vOutputDirection.yz ) );

			}
		`,blending:li,depthTest:!1,depthWrite:!1})}function Ac(){return`

		precision mediump float;
		precision mediump int;

		attribute float faceIndex;

		varying vec3 vOutputDirection;

		// RH coordinate system; PMREM face-indexing convention
		vec3 getDirection( vec2 uv, float face ) {

			uv = 2.0 * uv - 1.0;

			vec3 direction = vec3( uv, 1.0 );

			if ( face == 0.0 ) {

				direction = direction.zyx; // ( 1, v, u ) pos x

			} else if ( face == 1.0 ) {

				direction = direction.xzy;
				direction.xz *= -1.0; // ( -u, 1, -v ) pos y

			} else if ( face == 2.0 ) {

				direction.x *= -1.0; // ( -u, v, 1 ) pos z

			} else if ( face == 3.0 ) {

				direction = direction.zyx;
				direction.xz *= -1.0; // ( -1, v, -u ) neg x

			} else if ( face == 4.0 ) {

				direction = direction.xzy;
				direction.xy *= -1.0; // ( -u, -1, v ) neg y

			} else if ( face == 5.0 ) {

				direction.z *= -1.0; // ( u, v, -1 ) neg z

			}

			return direction;

		}

		void main() {

			vOutputDirection = getDirection( uv, faceIndex );
			gl_Position = vec4( position, 1.0 );

		}
	`}function o0(s){let e=new WeakMap,t=null;function n(a){if(a&&a.isTexture){let c=a.mapping,l=c===da||c===pa,u=c===rs||c===os;if(l||u){let h=e.get(a),f=h!==void 0?h.texture.pmremVersion:0;if(a.isRenderTargetTexture&&a.pmremVersion!==f)return t===null&&(t=new ps(s)),h=l?t.fromEquirectangular(a,h):t.fromCubemap(a,h),h.texture.pmremVersion=a.pmremVersion,e.set(a,h),h.texture;if(h!==void 0)return h.texture;{let p=a.image;return l&&p&&p.height>0||u&&p&&i(p)?(t===null&&(t=new ps(s)),h=l?t.fromEquirectangular(a):t.fromCubemap(a),h.texture.pmremVersion=a.pmremVersion,e.set(a,h),a.addEventListener("dispose",r),h.texture):null}}}return a}function i(a){let c=0,l=6;for(let u=0;u<l;u++)a[u]!==void 0&&c++;return c===l}function r(a){let c=a.target;c.removeEventListener("dispose",r);let l=e.get(c);l!==void 0&&(e.delete(c),l.dispose())}function o(){e=new WeakMap,t!==null&&(t.dispose(),t=null)}return{get:n,dispose:o}}function a0(s){let e={};function t(n){if(e[n]!==void 0)return e[n];let i;switch(n){case"WEBGL_depth_texture":i=s.getExtension("WEBGL_depth_texture")||s.getExtension("MOZ_WEBGL_depth_texture")||s.getExtension("WEBKIT_WEBGL_depth_texture");break;case"EXT_texture_filter_anisotropic":i=s.getExtension("EXT_texture_filter_anisotropic")||s.getExtension("MOZ_EXT_texture_filter_anisotropic")||s.getExtension("WEBKIT_EXT_texture_filter_anisotropic");break;case"WEBGL_compressed_texture_s3tc":i=s.getExtension("WEBGL_compressed_texture_s3tc")||s.getExtension("MOZ_WEBGL_compressed_texture_s3tc")||s.getExtension("WEBKIT_WEBGL_compressed_texture_s3tc");break;case"WEBGL_compressed_texture_pvrtc":i=s.getExtension("WEBGL_compressed_texture_pvrtc")||s.getExtension("WEBKIT_WEBGL_compressed_texture_pvrtc");break;default:i=s.getExtension(n)}return e[n]=i,i}return{has:function(n){return t(n)!==null},init:function(){t("EXT_color_buffer_float"),t("WEBGL_clip_cull_distance"),t("OES_texture_float_linear"),t("EXT_color_buffer_half_float"),t("WEBGL_multisampled_render_to_texture"),t("WEBGL_render_shared_exponent")},get:function(n){let i=t(n);return i===null&&Hs("THREE.WebGLRenderer: "+n+" extension not supported."),i}}}function c0(s,e,t,n){let i={},r=new WeakMap;function o(h){let f=h.target;f.index!==null&&e.remove(f.index);for(let g in f.attributes)e.remove(f.attributes[g]);for(let g in f.morphAttributes){let v=f.morphAttributes[g];for(let m=0,d=v.length;m<d;m++)e.remove(v[m])}f.removeEventListener("dispose",o),delete i[f.id];let p=r.get(f);p&&(e.remove(p),r.delete(f)),n.releaseStatesOfGeometry(f),f.isInstancedBufferGeometry===!0&&delete f._maxInstanceCount,t.memory.geometries--}function a(h,f){return i[f.id]===!0||(f.addEventListener("dispose",o),i[f.id]=!0,t.memory.geometries++),f}function c(h){let f=h.attributes;for(let g in f)e.update(f[g],s.ARRAY_BUFFER);let p=h.morphAttributes;for(let g in p){let v=p[g];for(let m=0,d=v.length;m<d;m++)e.update(v[m],s.ARRAY_BUFFER)}}function l(h){let f=[],p=h.index,g=h.attributes.position,v=0;if(p!==null){let M=p.array;v=p.version;for(let b=0,_=M.length;b<_;b+=3){let C=M[b+0],A=M[b+1],E=M[b+2];f.push(C,A,A,E,E,C)}}else if(g!==void 0){let M=g.array;v=g.version;for(let b=0,_=M.length/3-1;b<_;b+=3){let C=b+0,A=b+1,E=b+2;f.push(C,A,A,E,E,C)}}else return;let m=new(ch(f)?Jr:Kr)(f,1);m.version=v;let d=r.get(h);d&&e.remove(d),r.set(h,m)}function u(h){let f=r.get(h);if(f){let p=h.index;p!==null&&f.version<p.version&&l(h)}else l(h);return r.get(h)}return{get:a,update:c,getWireframeAttribute:u}}function l0(s,e,t){let n;function i(f){n=f}let r,o;function a(f){r=f.type,o=f.bytesPerElement}function c(f,p){s.drawElements(n,p,r,f*o),t.update(p,n,1)}function l(f,p,g){g!==0&&(s.drawElementsInstanced(n,p,r,f*o,g),t.update(p,n,g))}function u(f,p,g){if(g===0)return;e.get("WEBGL_multi_draw").multiDrawElementsWEBGL(n,p,0,r,f,0,g);let m=0;for(let d=0;d<g;d++)m+=p[d];t.update(m,n,1)}function h(f,p,g,v){if(g===0)return;let m=e.get("WEBGL_multi_draw");if(m===null)for(let d=0;d<f.length;d++)l(f[d]/o,p[d],v[d]);else{m.multiDrawElementsInstancedWEBGL(n,p,0,r,f,0,v,0,g);let d=0;for(let M=0;M<g;M++)d+=p[M]*v[M];t.update(d,n,1)}}this.setMode=i,this.setIndex=a,this.render=c,this.renderInstances=l,this.renderMultiDraw=u,this.renderMultiDrawInstances=h}function u0(s){let e={geometries:0,textures:0},t={frame:0,calls:0,triangles:0,points:0,lines:0};function n(r,o,a){switch(t.calls++,o){case s.TRIANGLES:t.triangles+=a*(r/3);break;case s.LINES:t.lines+=a*(r/2);break;case s.LINE_STRIP:t.lines+=a*(r-1);break;case s.LINE_LOOP:t.lines+=a*r;break;case s.POINTS:t.points+=a*r;break;default:console.error("THREE.WebGLInfo: Unknown draw mode:",o);break}}function i(){t.calls=0,t.triangles=0,t.points=0,t.lines=0}return{memory:e,render:t,programs:null,autoReset:!0,reset:i,update:n}}function h0(s,e,t){let n=new WeakMap,i=new We;function r(o,a,c){let l=o.morphTargetInfluences,u=a.morphAttributes.position||a.morphAttributes.normal||a.morphAttributes.color,h=u!==void 0?u.length:0,f=n.get(a);if(f===void 0||f.count!==h){let x=function(){E.dispose(),n.delete(a),a.removeEventListener("dispose",x)};f!==void 0&&f.texture.dispose();let p=a.morphAttributes.position!==void 0,g=a.morphAttributes.normal!==void 0,v=a.morphAttributes.color!==void 0,m=a.morphAttributes.position||[],d=a.morphAttributes.normal||[],M=a.morphAttributes.color||[],b=0;p===!0&&(b=1),g===!0&&(b=2),v===!0&&(b=3);let _=a.attributes.position.count*b,C=1;_>e.maxTextureSize&&(C=Math.ceil(_/e.maxTextureSize),_=e.maxTextureSize);let A=new Float32Array(_*C*4*h),E=new $r(A,_,C,h);E.type=Tn,E.needsUpdate=!0;let I=b*4;for(let y=0;y<h;y++){let T=m[y],L=d[y],D=M[y],F=_*C*4*y;for(let X=0;X<T.count;X++){let z=X*I;p===!0&&(i.fromBufferAttribute(T,X),A[F+z+0]=i.x,A[F+z+1]=i.y,A[F+z+2]=i.z,A[F+z+3]=0),g===!0&&(i.fromBufferAttribute(L,X),A[F+z+4]=i.x,A[F+z+5]=i.y,A[F+z+6]=i.z,A[F+z+7]=0),v===!0&&(i.fromBufferAttribute(D,X),A[F+z+8]=i.x,A[F+z+9]=i.y,A[F+z+10]=i.z,A[F+z+11]=D.itemSize===4?i.w:1)}}f={count:h,texture:E,size:new le(_,C)},n.set(a,f),a.addEventListener("dispose",x)}if(o.isInstancedMesh===!0&&o.morphTexture!==null)c.getUniforms().setValue(s,"morphTexture",o.morphTexture,t);else{let p=0;for(let v=0;v<l.length;v++)p+=l[v];let g=a.morphTargetsRelative?1:1-p;c.getUniforms().setValue(s,"morphTargetBaseInfluence",g),c.getUniforms().setValue(s,"morphTargetInfluences",l)}c.getUniforms().setValue(s,"morphTargetsTexture",f.texture,t),c.getUniforms().setValue(s,"morphTargetsTextureSize",f.size)}return{update:r}}function f0(s,e,t,n){let i=new WeakMap;function r(c){let l=n.render.frame,u=c.geometry,h=e.get(c,u);if(i.get(h)!==l&&(e.update(h),i.set(h,l)),c.isInstancedMesh&&(c.hasEventListener("dispose",a)===!1&&c.addEventListener("dispose",a),i.get(c)!==l&&(t.update(c.instanceMatrix,s.ARRAY_BUFFER),c.instanceColor!==null&&t.update(c.instanceColor,s.ARRAY_BUFFER),i.set(c,l))),c.isSkinnedMesh){let f=c.skeleton;i.get(f)!==l&&(f.update(),i.set(f,l))}return h}function o(){i=new WeakMap}function a(c){let l=c.target;l.removeEventListener("dispose",a),t.remove(l.instanceMatrix),l.instanceColor!==null&&t.remove(l.instanceColor)}return{update:r,dispose:o}}var ms=class extends Pt{constructor(e,t,n,i,r,o,a,c,l,u=es){if(u!==es&&u!==cs)throw new Error("DepthTexture format must be either THREE.DepthFormat or THREE.DepthStencilFormat");n===void 0&&u===es&&(n=Yn),n===void 0&&u===cs&&(n=as),super(null,i,r,o,a,c,u,n,l),this.isDepthTexture=!0,this.image={width:e,height:t},this.magFilter=a!==void 0?a:yt,this.minFilter=c!==void 0?c:yt,this.flipY=!1,this.generateMipmaps=!1,this.compareFunction=null}copy(e){return super.copy(e),this.compareFunction=e.compareFunction,this}toJSON(e){let t=super.toJSON(e);return this.compareFunction!==null&&(t.compareFunction=this.compareFunction),t}},fh=new Pt,hu=new ms(1,1),dh=new $r,ph=new Wa,mh=new Qr,fu=[],du=[],pu=new Float32Array(16),mu=new Float32Array(9),gu=new Float32Array(4);function bs(s,e,t){let n=s[0];if(n<=0||n>0)return s;let i=e*t,r=fu[i];if(r===void 0&&(r=new Float32Array(i),fu[i]=r),e!==0){n.toArray(r,0);for(let o=1,a=0;o!==e;++o)a+=t,s[o].toArray(r,a)}return r}function At(s,e){if(s.length!==e.length)return!1;for(let t=0,n=s.length;t<n;t++)if(s[t]!==e[t])return!1;return!0}function Rt(s,e){for(let t=0,n=e.length;t<n;t++)s[t]=e[t]}function vo(s,e){let t=du[e];t===void 0&&(t=new Int32Array(e),du[e]=t);for(let n=0;n!==e;++n)t[n]=s.allocateTextureUnit();return t}function d0(s,e){let t=this.cache;t[0]!==e&&(s.uniform1f(this.addr,e),t[0]=e)}function p0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y)&&(s.uniform2f(this.addr,e.x,e.y),t[0]=e.x,t[1]=e.y);else{if(At(t,e))return;s.uniform2fv(this.addr,e),Rt(t,e)}}function m0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z)&&(s.uniform3f(this.addr,e.x,e.y,e.z),t[0]=e.x,t[1]=e.y,t[2]=e.z);else if(e.r!==void 0)(t[0]!==e.r||t[1]!==e.g||t[2]!==e.b)&&(s.uniform3f(this.addr,e.r,e.g,e.b),t[0]=e.r,t[1]=e.g,t[2]=e.b);else{if(At(t,e))return;s.uniform3fv(this.addr,e),Rt(t,e)}}function g0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z||t[3]!==e.w)&&(s.uniform4f(this.addr,e.x,e.y,e.z,e.w),t[0]=e.x,t[1]=e.y,t[2]=e.z,t[3]=e.w);else{if(At(t,e))return;s.uniform4fv(this.addr,e),Rt(t,e)}}function v0(s,e){let t=this.cache,n=e.elements;if(n===void 0){if(At(t,e))return;s.uniformMatrix2fv(this.addr,!1,e),Rt(t,e)}else{if(At(t,n))return;gu.set(n),s.uniformMatrix2fv(this.addr,!1,gu),Rt(t,n)}}function x0(s,e){let t=this.cache,n=e.elements;if(n===void 0){if(At(t,e))return;s.uniformMatrix3fv(this.addr,!1,e),Rt(t,e)}else{if(At(t,n))return;mu.set(n),s.uniformMatrix3fv(this.addr,!1,mu),Rt(t,n)}}function _0(s,e){let t=this.cache,n=e.elements;if(n===void 0){if(At(t,e))return;s.uniformMatrix4fv(this.addr,!1,e),Rt(t,e)}else{if(At(t,n))return;pu.set(n),s.uniformMatrix4fv(this.addr,!1,pu),Rt(t,n)}}function y0(s,e){let t=this.cache;t[0]!==e&&(s.uniform1i(this.addr,e),t[0]=e)}function M0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y)&&(s.uniform2i(this.addr,e.x,e.y),t[0]=e.x,t[1]=e.y);else{if(At(t,e))return;s.uniform2iv(this.addr,e),Rt(t,e)}}function b0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z)&&(s.uniform3i(this.addr,e.x,e.y,e.z),t[0]=e.x,t[1]=e.y,t[2]=e.z);else{if(At(t,e))return;s.uniform3iv(this.addr,e),Rt(t,e)}}function S0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z||t[3]!==e.w)&&(s.uniform4i(this.addr,e.x,e.y,e.z,e.w),t[0]=e.x,t[1]=e.y,t[2]=e.z,t[3]=e.w);else{if(At(t,e))return;s.uniform4iv(this.addr,e),Rt(t,e)}}function w0(s,e){let t=this.cache;t[0]!==e&&(s.uniform1ui(this.addr,e),t[0]=e)}function E0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y)&&(s.uniform2ui(this.addr,e.x,e.y),t[0]=e.x,t[1]=e.y);else{if(At(t,e))return;s.uniform2uiv(this.addr,e),Rt(t,e)}}function T0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z)&&(s.uniform3ui(this.addr,e.x,e.y,e.z),t[0]=e.x,t[1]=e.y,t[2]=e.z);else{if(At(t,e))return;s.uniform3uiv(this.addr,e),Rt(t,e)}}function A0(s,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z||t[3]!==e.w)&&(s.uniform4ui(this.addr,e.x,e.y,e.z,e.w),t[0]=e.x,t[1]=e.y,t[2]=e.z,t[3]=e.w);else{if(At(t,e))return;s.uniform4uiv(this.addr,e),Rt(t,e)}}function R0(s,e,t){let n=this.cache,i=t.allocateTextureUnit();n[0]!==i&&(s.uniform1i(this.addr,i),n[0]=i);let r;this.type===s.SAMPLER_2D_SHADOW?(hu.compareFunction=ah,r=hu):r=fh,t.setTexture2D(e||r,i)}function C0(s,e,t){let n=this.cache,i=t.allocateTextureUnit();n[0]!==i&&(s.uniform1i(this.addr,i),n[0]=i),t.setTexture3D(e||ph,i)}function I0(s,e,t){let n=this.cache,i=t.allocateTextureUnit();n[0]!==i&&(s.uniform1i(this.addr,i),n[0]=i),t.setTextureCube(e||mh,i)}function P0(s,e,t){let n=this.cache,i=t.allocateTextureUnit();n[0]!==i&&(s.uniform1i(this.addr,i),n[0]=i),t.setTexture2DArray(e||dh,i)}function L0(s){switch(s){case 5126:return d0;case 35664:return p0;case 35665:return m0;case 35666:return g0;case 35674:return v0;case 35675:return x0;case 35676:return _0;case 5124:case 35670:return y0;case 35667:case 35671:return M0;case 35668:case 35672:return b0;case 35669:case 35673:return S0;case 5125:return w0;case 36294:return E0;case 36295:return T0;case 36296:return A0;case 35678:case 36198:case 36298:case 36306:case 35682:return R0;case 35679:case 36299:case 36307:return C0;case 35680:case 36300:case 36308:case 36293:return I0;case 36289:case 36303:case 36311:case 36292:return P0}}function D0(s,e){s.uniform1fv(this.addr,e)}function U0(s,e){let t=bs(e,this.size,2);s.uniform2fv(this.addr,t)}function N0(s,e){let t=bs(e,this.size,3);s.uniform3fv(this.addr,t)}function F0(s,e){let t=bs(e,this.size,4);s.uniform4fv(this.addr,t)}function O0(s,e){let t=bs(e,this.size,4);s.uniformMatrix2fv(this.addr,!1,t)}function B0(s,e){let t=bs(e,this.size,9);s.uniformMatrix3fv(this.addr,!1,t)}function z0(s,e){let t=bs(e,this.size,16);s.uniformMatrix4fv(this.addr,!1,t)}function k0(s,e){s.uniform1iv(this.addr,e)}function H0(s,e){s.uniform2iv(this.addr,e)}function V0(s,e){s.uniform3iv(this.addr,e)}function G0(s,e){s.uniform4iv(this.addr,e)}function W0(s,e){s.uniform1uiv(this.addr,e)}function X0(s,e){s.uniform2uiv(this.addr,e)}function q0(s,e){s.uniform3uiv(this.addr,e)}function Y0(s,e){s.uniform4uiv(this.addr,e)}function $0(s,e,t){let n=this.cache,i=e.length,r=vo(t,i);At(n,r)||(s.uniform1iv(this.addr,r),Rt(n,r));for(let o=0;o!==i;++o)t.setTexture2D(e[o]||fh,r[o])}function Z0(s,e,t){let n=this.cache,i=e.length,r=vo(t,i);At(n,r)||(s.uniform1iv(this.addr,r),Rt(n,r));for(let o=0;o!==i;++o)t.setTexture3D(e[o]||ph,r[o])}function K0(s,e,t){let n=this.cache,i=e.length,r=vo(t,i);At(n,r)||(s.uniform1iv(this.addr,r),Rt(n,r));for(let o=0;o!==i;++o)t.setTextureCube(e[o]||mh,r[o])}function J0(s,e,t){let n=this.cache,i=e.length,r=vo(t,i);At(n,r)||(s.uniform1iv(this.addr,r),Rt(n,r));for(let o=0;o!==i;++o)t.setTexture2DArray(e[o]||dh,r[o])}function j0(s){switch(s){case 5126:return D0;case 35664:return U0;case 35665:return N0;case 35666:return F0;case 35674:return O0;case 35675:return B0;case 35676:return z0;case 5124:case 35670:return k0;case 35667:case 35671:return H0;case 35668:case 35672:return V0;case 35669:case 35673:return G0;case 5125:return W0;case 36294:return X0;case 36295:return q0;case 36296:return Y0;case 35678:case 36198:case 36298:case 36306:case 35682:return $0;case 35679:case 36299:case 36307:return Z0;case 35680:case 36300:case 36308:case 36293:return K0;case 36289:case 36303:case 36311:case 36292:return J0}}var Ya=class{constructor(e,t,n){this.id=e,this.addr=n,this.cache=[],this.type=t.type,this.setValue=L0(t.type)}},$a=class{constructor(e,t,n){this.id=e,this.addr=n,this.cache=[],this.type=t.type,this.size=t.size,this.setValue=j0(t.type)}},Za=class{constructor(e){this.id=e,this.seq=[],this.map={}}setValue(e,t,n){let i=this.seq;for(let r=0,o=i.length;r!==o;++r){let a=i[r];a.setValue(e,t[a.id],n)}}},jo=/(\w+)(\])?(\[|\.)?/g;function vu(s,e){s.seq.push(e),s.map[e.id]=e}function Q0(s,e,t){let n=s.name,i=n.length;for(jo.lastIndex=0;;){let r=jo.exec(n),o=jo.lastIndex,a=r[1],c=r[2]==="]",l=r[3];if(c&&(a=a|0),l===void 0||l==="["&&o+2===i){vu(t,l===void 0?new Ya(a,s,e):new $a(a,s,e));break}else{let h=t.map[a];h===void 0&&(h=new Za(a),vu(t,h)),t=h}}}var ns=class{constructor(e,t){this.seq=[],this.map={};let n=e.getProgramParameter(t,e.ACTIVE_UNIFORMS);for(let i=0;i<n;++i){let r=e.getActiveUniform(t,i),o=e.getUniformLocation(t,r.name);Q0(r,o,this)}}setValue(e,t,n,i){let r=this.map[t];r!==void 0&&r.setValue(e,n,i)}setOptional(e,t,n){let i=t[n];i!==void 0&&this.setValue(e,n,i)}static upload(e,t,n,i){for(let r=0,o=t.length;r!==o;++r){let a=t[r],c=n[a.id];c.needsUpdate!==!1&&a.setValue(e,c.value,i)}}static seqWithValue(e,t){let n=[];for(let i=0,r=e.length;i!==r;++i){let o=e[i];o.id in t&&n.push(o)}return n}};function xu(s,e,t){let n=s.createShader(e);return s.shaderSource(n,t),s.compileShader(n),n}var eg=37297,tg=0;function ng(s,e){let t=s.split(`
`),n=[],i=Math.max(e-6,0),r=Math.min(e+6,t.length);for(let o=i;o<r;o++){let a=o+1;n.push(`${a===e?">":" "} ${a}: ${t[o]}`)}return n.join(`
`)}var _u=new ke;function ig(s){Ye._getMatrix(_u,Ye.workingColorSpace,s);let e=`mat3( ${_u.elements.map(t=>t.toFixed(4))} )`;switch(Ye.getTransfer(s)){case go:return[e,"LinearTransferOETF"];case lt:return[e,"sRGBTransferOETF"];default:return console.warn("THREE.WebGLProgram: Unsupported color space: ",s),[e,"LinearTransferOETF"]}}function yu(s,e,t){let n=s.getShaderParameter(e,s.COMPILE_STATUS),i=s.getShaderInfoLog(e).trim();if(n&&i==="")return"";let r=/ERROR: 0:(\d+)/.exec(i);if(r){let o=parseInt(r[1]);return t.toUpperCase()+`

`+i+`

`+ng(s.getShaderSource(e),o)}else return i}function sg(s,e){let t=ig(e);return[`vec4 ${s}( vec4 value ) {`,`	return ${t[1]}( vec4( value.rgb * ${t[0]}, value.a ) );`,"}"].join(`
`)}function rg(s,e){let t;switch(e){case pf:t="Linear";break;case mf:t="Reinhard";break;case gf:t="Cineon";break;case vf:t="ACESFilmic";break;case _f:t="AgX";break;case yf:t="Neutral";break;case xf:t="Custom";break;default:console.warn("THREE.WebGLProgram: Unsupported toneMapping:",e),t="Linear"}return"vec3 "+s+"( vec3 color ) { return "+t+"ToneMapping( color ); }"}var Dr=new P;function og(){Ye.getLuminanceCoefficients(Dr);let s=Dr.x.toFixed(4),e=Dr.y.toFixed(4),t=Dr.z.toFixed(4);return["float luminance( const in vec3 rgb ) {",`	const vec3 weights = vec3( ${s}, ${e}, ${t} );`,"	return dot( weights, rgb );","}"].join(`
`)}function ag(s){return[s.extensionClipCullDistance?"#extension GL_ANGLE_clip_cull_distance : require":"",s.extensionMultiDraw?"#extension GL_ANGLE_multi_draw : require":""].filter(Vs).join(`
`)}function cg(s){let e=[];for(let t in s){let n=s[t];n!==!1&&e.push("#define "+t+" "+n)}return e.join(`
`)}function lg(s,e){let t={},n=s.getProgramParameter(e,s.ACTIVE_ATTRIBUTES);for(let i=0;i<n;i++){let r=s.getActiveAttrib(e,i),o=r.name,a=1;r.type===s.FLOAT_MAT2&&(a=2),r.type===s.FLOAT_MAT3&&(a=3),r.type===s.FLOAT_MAT4&&(a=4),t[o]={type:r.type,location:s.getAttribLocation(e,o),locationSize:a}}return t}function Vs(s){return s!==""}function Mu(s,e){let t=e.numSpotLightShadows+e.numSpotLightMaps-e.numSpotLightShadowsWithMaps;return s.replace(/NUM_DIR_LIGHTS/g,e.numDirLights).replace(/NUM_SPOT_LIGHTS/g,e.numSpotLights).replace(/NUM_SPOT_LIGHT_MAPS/g,e.numSpotLightMaps).replace(/NUM_SPOT_LIGHT_COORDS/g,t).replace(/NUM_RECT_AREA_LIGHTS/g,e.numRectAreaLights).replace(/NUM_POINT_LIGHTS/g,e.numPointLights).replace(/NUM_HEMI_LIGHTS/g,e.numHemiLights).replace(/NUM_DIR_LIGHT_SHADOWS/g,e.numDirLightShadows).replace(/NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS/g,e.numSpotLightShadowsWithMaps).replace(/NUM_SPOT_LIGHT_SHADOWS/g,e.numSpotLightShadows).replace(/NUM_POINT_LIGHT_SHADOWS/g,e.numPointLightShadows)}function bu(s,e){return s.replace(/NUM_CLIPPING_PLANES/g,e.numClippingPlanes).replace(/UNION_CLIPPING_PLANES/g,e.numClippingPlanes-e.numClipIntersection)}var ug=/^[ \t]*#include +<([\w\d./]+)>/gm;function Ka(s){return s.replace(ug,fg)}var hg=new Map;function fg(s,e){let t=Ve[e];if(t===void 0){let n=hg.get(e);if(n!==void 0)t=Ve[n],console.warn('THREE.WebGLRenderer: Shader chunk "%s" has been deprecated. Use "%s" instead.',e,n);else throw new Error("Can not resolve #include <"+e+">")}return Ka(t)}var dg=/#pragma unroll_loop_start\s+for\s*\(\s*int\s+i\s*=\s*(\d+)\s*;\s*i\s*<\s*(\d+)\s*;\s*i\s*\+\+\s*\)\s*{([\s\S]+?)}\s+#pragma unroll_loop_end/g;function Su(s){return s.replace(dg,pg)}function pg(s,e,t,n){let i="";for(let r=parseInt(e);r<parseInt(t);r++)i+=n.replace(/\[\s*i\s*\]/g,"[ "+r+" ]").replace(/UNROLLED_LOOP_INDEX/g,r);return i}function wu(s){let e=`precision ${s.precision} float;
	precision ${s.precision} int;
	precision ${s.precision} sampler2D;
	precision ${s.precision} samplerCube;
	precision ${s.precision} sampler3D;
	precision ${s.precision} sampler2DArray;
	precision ${s.precision} sampler2DShadow;
	precision ${s.precision} samplerCubeShadow;
	precision ${s.precision} sampler2DArrayShadow;
	precision ${s.precision} isampler2D;
	precision ${s.precision} isampler3D;
	precision ${s.precision} isamplerCube;
	precision ${s.precision} isampler2DArray;
	precision ${s.precision} usampler2D;
	precision ${s.precision} usampler3D;
	precision ${s.precision} usamplerCube;
	precision ${s.precision} usampler2DArray;
	`;return s.precision==="highp"?e+=`
#define HIGH_PRECISION`:s.precision==="mediump"?e+=`
#define MEDIUM_PRECISION`:s.precision==="lowp"&&(e+=`
#define LOW_PRECISION`),e}function mg(s){let e="SHADOWMAP_TYPE_BASIC";return s.shadowMapType===Yu?e="SHADOWMAP_TYPE_PCF":s.shadowMapType===vc?e="SHADOWMAP_TYPE_PCF_SOFT":s.shadowMapType===Gn&&(e="SHADOWMAP_TYPE_VSM"),e}function gg(s){let e="ENVMAP_TYPE_CUBE";if(s.envMap)switch(s.envMapMode){case rs:case os:e="ENVMAP_TYPE_CUBE";break;case po:e="ENVMAP_TYPE_CUBE_UV";break}return e}function vg(s){let e="ENVMAP_MODE_REFLECTION";if(s.envMap)switch(s.envMapMode){case os:e="ENVMAP_MODE_REFRACTION";break}return e}function xg(s){let e="ENVMAP_BLENDING_NONE";if(s.envMap)switch(s.combine){case $u:e="ENVMAP_BLENDING_MULTIPLY";break;case ff:e="ENVMAP_BLENDING_MIX";break;case df:e="ENVMAP_BLENDING_ADD";break}return e}function _g(s){let e=s.envMapCubeUVHeight;if(e===null)return null;let t=Math.log2(e)-2,n=1/e;return{texelWidth:1/(3*Math.max(Math.pow(2,t),7*16)),texelHeight:n,maxMip:t}}function yg(s,e,t,n){let i=s.getContext(),r=t.defines,o=t.vertexShader,a=t.fragmentShader,c=mg(t),l=gg(t),u=vg(t),h=xg(t),f=_g(t),p=ag(t),g=cg(r),v=i.createProgram(),m,d,M=t.glslVersion?"#version "+t.glslVersion+`
`:"";t.isRawShaderMaterial?(m=["#define SHADER_TYPE "+t.shaderType,"#define SHADER_NAME "+t.shaderName,g].filter(Vs).join(`
`),m.length>0&&(m+=`
`),d=["#define SHADER_TYPE "+t.shaderType,"#define SHADER_NAME "+t.shaderName,g].filter(Vs).join(`
`),d.length>0&&(d+=`
`)):(m=[wu(t),"#define SHADER_TYPE "+t.shaderType,"#define SHADER_NAME "+t.shaderName,g,t.extensionClipCullDistance?"#define USE_CLIP_DISTANCE":"",t.batching?"#define USE_BATCHING":"",t.batchingColor?"#define USE_BATCHING_COLOR":"",t.instancing?"#define USE_INSTANCING":"",t.instancingColor?"#define USE_INSTANCING_COLOR":"",t.instancingMorph?"#define USE_INSTANCING_MORPH":"",t.useFog&&t.fog?"#define USE_FOG":"",t.useFog&&t.fogExp2?"#define FOG_EXP2":"",t.map?"#define USE_MAP":"",t.envMap?"#define USE_ENVMAP":"",t.envMap?"#define "+u:"",t.lightMap?"#define USE_LIGHTMAP":"",t.aoMap?"#define USE_AOMAP":"",t.bumpMap?"#define USE_BUMPMAP":"",t.normalMap?"#define USE_NORMALMAP":"",t.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",t.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",t.displacementMap?"#define USE_DISPLACEMENTMAP":"",t.emissiveMap?"#define USE_EMISSIVEMAP":"",t.anisotropy?"#define USE_ANISOTROPY":"",t.anisotropyMap?"#define USE_ANISOTROPYMAP":"",t.clearcoatMap?"#define USE_CLEARCOATMAP":"",t.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",t.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",t.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",t.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",t.specularMap?"#define USE_SPECULARMAP":"",t.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",t.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",t.roughnessMap?"#define USE_ROUGHNESSMAP":"",t.metalnessMap?"#define USE_METALNESSMAP":"",t.alphaMap?"#define USE_ALPHAMAP":"",t.alphaHash?"#define USE_ALPHAHASH":"",t.transmission?"#define USE_TRANSMISSION":"",t.transmissionMap?"#define USE_TRANSMISSIONMAP":"",t.thicknessMap?"#define USE_THICKNESSMAP":"",t.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",t.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",t.mapUv?"#define MAP_UV "+t.mapUv:"",t.alphaMapUv?"#define ALPHAMAP_UV "+t.alphaMapUv:"",t.lightMapUv?"#define LIGHTMAP_UV "+t.lightMapUv:"",t.aoMapUv?"#define AOMAP_UV "+t.aoMapUv:"",t.emissiveMapUv?"#define EMISSIVEMAP_UV "+t.emissiveMapUv:"",t.bumpMapUv?"#define BUMPMAP_UV "+t.bumpMapUv:"",t.normalMapUv?"#define NORMALMAP_UV "+t.normalMapUv:"",t.displacementMapUv?"#define DISPLACEMENTMAP_UV "+t.displacementMapUv:"",t.metalnessMapUv?"#define METALNESSMAP_UV "+t.metalnessMapUv:"",t.roughnessMapUv?"#define ROUGHNESSMAP_UV "+t.roughnessMapUv:"",t.anisotropyMapUv?"#define ANISOTROPYMAP_UV "+t.anisotropyMapUv:"",t.clearcoatMapUv?"#define CLEARCOATMAP_UV "+t.clearcoatMapUv:"",t.clearcoatNormalMapUv?"#define CLEARCOAT_NORMALMAP_UV "+t.clearcoatNormalMapUv:"",t.clearcoatRoughnessMapUv?"#define CLEARCOAT_ROUGHNESSMAP_UV "+t.clearcoatRoughnessMapUv:"",t.iridescenceMapUv?"#define IRIDESCENCEMAP_UV "+t.iridescenceMapUv:"",t.iridescenceThicknessMapUv?"#define IRIDESCENCE_THICKNESSMAP_UV "+t.iridescenceThicknessMapUv:"",t.sheenColorMapUv?"#define SHEEN_COLORMAP_UV "+t.sheenColorMapUv:"",t.sheenRoughnessMapUv?"#define SHEEN_ROUGHNESSMAP_UV "+t.sheenRoughnessMapUv:"",t.specularMapUv?"#define SPECULARMAP_UV "+t.specularMapUv:"",t.specularColorMapUv?"#define SPECULAR_COLORMAP_UV "+t.specularColorMapUv:"",t.specularIntensityMapUv?"#define SPECULAR_INTENSITYMAP_UV "+t.specularIntensityMapUv:"",t.transmissionMapUv?"#define TRANSMISSIONMAP_UV "+t.transmissionMapUv:"",t.thicknessMapUv?"#define THICKNESSMAP_UV "+t.thicknessMapUv:"",t.vertexTangents&&t.flatShading===!1?"#define USE_TANGENT":"",t.vertexColors?"#define USE_COLOR":"",t.vertexAlphas?"#define USE_COLOR_ALPHA":"",t.vertexUv1s?"#define USE_UV1":"",t.vertexUv2s?"#define USE_UV2":"",t.vertexUv3s?"#define USE_UV3":"",t.pointsUvs?"#define USE_POINTS_UV":"",t.flatShading?"#define FLAT_SHADED":"",t.skinning?"#define USE_SKINNING":"",t.morphTargets?"#define USE_MORPHTARGETS":"",t.morphNormals&&t.flatShading===!1?"#define USE_MORPHNORMALS":"",t.morphColors?"#define USE_MORPHCOLORS":"",t.morphTargetsCount>0?"#define MORPHTARGETS_TEXTURE_STRIDE "+t.morphTextureStride:"",t.morphTargetsCount>0?"#define MORPHTARGETS_COUNT "+t.morphTargetsCount:"",t.doubleSided?"#define DOUBLE_SIDED":"",t.flipSided?"#define FLIP_SIDED":"",t.shadowMapEnabled?"#define USE_SHADOWMAP":"",t.shadowMapEnabled?"#define "+c:"",t.sizeAttenuation?"#define USE_SIZEATTENUATION":"",t.numLightProbes>0?"#define USE_LIGHT_PROBES":"",t.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",t.reverseDepthBuffer?"#define USE_REVERSEDEPTHBUF":"","uniform mat4 modelMatrix;","uniform mat4 modelViewMatrix;","uniform mat4 projectionMatrix;","uniform mat4 viewMatrix;","uniform mat3 normalMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;","#ifdef USE_INSTANCING","	attribute mat4 instanceMatrix;","#endif","#ifdef USE_INSTANCING_COLOR","	attribute vec3 instanceColor;","#endif","#ifdef USE_INSTANCING_MORPH","	uniform sampler2D morphTexture;","#endif","attribute vec3 position;","attribute vec3 normal;","attribute vec2 uv;","#ifdef USE_UV1","	attribute vec2 uv1;","#endif","#ifdef USE_UV2","	attribute vec2 uv2;","#endif","#ifdef USE_UV3","	attribute vec2 uv3;","#endif","#ifdef USE_TANGENT","	attribute vec4 tangent;","#endif","#if defined( USE_COLOR_ALPHA )","	attribute vec4 color;","#elif defined( USE_COLOR )","	attribute vec3 color;","#endif","#ifdef USE_SKINNING","	attribute vec4 skinIndex;","	attribute vec4 skinWeight;","#endif",`
`].filter(Vs).join(`
`),d=[wu(t),"#define SHADER_TYPE "+t.shaderType,"#define SHADER_NAME "+t.shaderName,g,t.useFog&&t.fog?"#define USE_FOG":"",t.useFog&&t.fogExp2?"#define FOG_EXP2":"",t.alphaToCoverage?"#define ALPHA_TO_COVERAGE":"",t.map?"#define USE_MAP":"",t.matcap?"#define USE_MATCAP":"",t.envMap?"#define USE_ENVMAP":"",t.envMap?"#define "+l:"",t.envMap?"#define "+u:"",t.envMap?"#define "+h:"",f?"#define CUBEUV_TEXEL_WIDTH "+f.texelWidth:"",f?"#define CUBEUV_TEXEL_HEIGHT "+f.texelHeight:"",f?"#define CUBEUV_MAX_MIP "+f.maxMip+".0":"",t.lightMap?"#define USE_LIGHTMAP":"",t.aoMap?"#define USE_AOMAP":"",t.bumpMap?"#define USE_BUMPMAP":"",t.normalMap?"#define USE_NORMALMAP":"",t.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",t.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",t.emissiveMap?"#define USE_EMISSIVEMAP":"",t.anisotropy?"#define USE_ANISOTROPY":"",t.anisotropyMap?"#define USE_ANISOTROPYMAP":"",t.clearcoat?"#define USE_CLEARCOAT":"",t.clearcoatMap?"#define USE_CLEARCOATMAP":"",t.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",t.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",t.dispersion?"#define USE_DISPERSION":"",t.iridescence?"#define USE_IRIDESCENCE":"",t.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",t.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",t.specularMap?"#define USE_SPECULARMAP":"",t.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",t.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",t.roughnessMap?"#define USE_ROUGHNESSMAP":"",t.metalnessMap?"#define USE_METALNESSMAP":"",t.alphaMap?"#define USE_ALPHAMAP":"",t.alphaTest?"#define USE_ALPHATEST":"",t.alphaHash?"#define USE_ALPHAHASH":"",t.sheen?"#define USE_SHEEN":"",t.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",t.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",t.transmission?"#define USE_TRANSMISSION":"",t.transmissionMap?"#define USE_TRANSMISSIONMAP":"",t.thicknessMap?"#define USE_THICKNESSMAP":"",t.vertexTangents&&t.flatShading===!1?"#define USE_TANGENT":"",t.vertexColors||t.instancingColor||t.batchingColor?"#define USE_COLOR":"",t.vertexAlphas?"#define USE_COLOR_ALPHA":"",t.vertexUv1s?"#define USE_UV1":"",t.vertexUv2s?"#define USE_UV2":"",t.vertexUv3s?"#define USE_UV3":"",t.pointsUvs?"#define USE_POINTS_UV":"",t.gradientMap?"#define USE_GRADIENTMAP":"",t.flatShading?"#define FLAT_SHADED":"",t.doubleSided?"#define DOUBLE_SIDED":"",t.flipSided?"#define FLIP_SIDED":"",t.shadowMapEnabled?"#define USE_SHADOWMAP":"",t.shadowMapEnabled?"#define "+c:"",t.premultipliedAlpha?"#define PREMULTIPLIED_ALPHA":"",t.numLightProbes>0?"#define USE_LIGHT_PROBES":"",t.decodeVideoTexture?"#define DECODE_VIDEO_TEXTURE":"",t.decodeVideoTextureEmissive?"#define DECODE_VIDEO_TEXTURE_EMISSIVE":"",t.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",t.reverseDepthBuffer?"#define USE_REVERSEDEPTHBUF":"","uniform mat4 viewMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;",t.toneMapping!==Ln?"#define TONE_MAPPING":"",t.toneMapping!==Ln?Ve.tonemapping_pars_fragment:"",t.toneMapping!==Ln?rg("toneMapping",t.toneMapping):"",t.dithering?"#define DITHERING":"",t.opaque?"#define OPAQUE":"",Ve.colorspace_pars_fragment,sg("linearToOutputTexel",t.outputColorSpace),og(),t.useDepthPacking?"#define DEPTH_PACKING "+t.depthPacking:"",`
`].filter(Vs).join(`
`)),o=Ka(o),o=Mu(o,t),o=bu(o,t),a=Ka(a),a=Mu(a,t),a=bu(a,t),o=Su(o),a=Su(a),t.isRawShaderMaterial!==!0&&(M=`#version 300 es
`,m=[p,"#define attribute in","#define varying out","#define texture2D texture"].join(`
`)+`
`+m,d=["#define varying in",t.glslVersion===Ol?"":"layout(location = 0) out highp vec4 pc_fragColor;",t.glslVersion===Ol?"":"#define gl_FragColor pc_fragColor","#define gl_FragDepthEXT gl_FragDepth","#define texture2D texture","#define textureCube texture","#define texture2DProj textureProj","#define texture2DLodEXT textureLod","#define texture2DProjLodEXT textureProjLod","#define textureCubeLodEXT textureLod","#define texture2DGradEXT textureGrad","#define texture2DProjGradEXT textureProjGrad","#define textureCubeGradEXT textureGrad"].join(`
`)+`
`+d);let b=M+m+o,_=M+d+a,C=xu(i,i.VERTEX_SHADER,b),A=xu(i,i.FRAGMENT_SHADER,_);i.attachShader(v,C),i.attachShader(v,A),t.index0AttributeName!==void 0?i.bindAttribLocation(v,0,t.index0AttributeName):t.morphTargets===!0&&i.bindAttribLocation(v,0,"position"),i.linkProgram(v);function E(T){if(s.debug.checkShaderErrors){let L=i.getProgramInfoLog(v).trim(),D=i.getShaderInfoLog(C).trim(),F=i.getShaderInfoLog(A).trim(),X=!0,z=!0;if(i.getProgramParameter(v,i.LINK_STATUS)===!1)if(X=!1,typeof s.debug.onShaderError=="function")s.debug.onShaderError(i,v,C,A);else{let K=yu(i,C,"vertex"),H=yu(i,A,"fragment");console.error("THREE.WebGLProgram: Shader Error "+i.getError()+" - VALIDATE_STATUS "+i.getProgramParameter(v,i.VALIDATE_STATUS)+`

Material Name: `+T.name+`
Material Type: `+T.type+`

Program Info Log: `+L+`
`+K+`
`+H)}else L!==""?console.warn("THREE.WebGLProgram: Program Info Log:",L):(D===""||F==="")&&(z=!1);z&&(T.diagnostics={runnable:X,programLog:L,vertexShader:{log:D,prefix:m},fragmentShader:{log:F,prefix:d}})}i.deleteShader(C),i.deleteShader(A),I=new ns(i,v),x=lg(i,v)}let I;this.getUniforms=function(){return I===void 0&&E(this),I};let x;this.getAttributes=function(){return x===void 0&&E(this),x};let y=t.rendererExtensionParallelShaderCompile===!1;return this.isReady=function(){return y===!1&&(y=i.getProgramParameter(v,eg)),y},this.destroy=function(){n.releaseStatesOfProgram(this),i.deleteProgram(v),this.program=void 0},this.type=t.shaderType,this.name=t.shaderName,this.id=tg++,this.cacheKey=e,this.usedTimes=1,this.program=v,this.vertexShader=C,this.fragmentShader=A,this}var Mg=0,Ja=class{constructor(){this.shaderCache=new Map,this.materialCache=new Map}update(e){let t=e.vertexShader,n=e.fragmentShader,i=this._getShaderStage(t),r=this._getShaderStage(n),o=this._getShaderCacheForMaterial(e);return o.has(i)===!1&&(o.add(i),i.usedTimes++),o.has(r)===!1&&(o.add(r),r.usedTimes++),this}remove(e){let t=this.materialCache.get(e);for(let n of t)n.usedTimes--,n.usedTimes===0&&this.shaderCache.delete(n.code);return this.materialCache.delete(e),this}getVertexShaderID(e){return this._getShaderStage(e.vertexShader).id}getFragmentShaderID(e){return this._getShaderStage(e.fragmentShader).id}dispose(){this.shaderCache.clear(),this.materialCache.clear()}_getShaderCacheForMaterial(e){let t=this.materialCache,n=t.get(e);return n===void 0&&(n=new Set,t.set(e,n)),n}_getShaderStage(e){let t=this.shaderCache,n=t.get(e);return n===void 0&&(n=new ja(e),t.set(e,n)),n}},ja=class{constructor(e){this.id=Mg++,this.code=e,this.usedTimes=0}};function bg(s,e,t,n,i,r,o){let a=new Zr,c=new Ja,l=new Set,u=[],h=i.logarithmicDepthBuffer,f=i.vertexTextures,p=i.precision,g={MeshDepthMaterial:"depth",MeshDistanceMaterial:"distanceRGBA",MeshNormalMaterial:"normal",MeshBasicMaterial:"basic",MeshLambertMaterial:"lambert",MeshPhongMaterial:"phong",MeshToonMaterial:"toon",MeshStandardMaterial:"physical",MeshPhysicalMaterial:"physical",MeshMatcapMaterial:"matcap",LineBasicMaterial:"basic",LineDashedMaterial:"dashed",PointsMaterial:"points",ShadowMaterial:"shadow",SpriteMaterial:"sprite"};function v(x){return l.add(x),x===0?"uv":`uv${x}`}function m(x,y,T,L,D){let F=L.fog,X=D.geometry,z=x.isMeshStandardMaterial?L.environment:null,K=(x.isMeshStandardMaterial?t:e).get(x.envMap||z),H=K&&K.mapping===po?K.image.height:null,k=g[x.type];x.precision!==null&&(p=i.getMaxPrecision(x.precision),p!==x.precision&&console.warn("THREE.WebGLProgram.getParameters:",x.precision,"not supported, using",p,"instead."));let $=X.morphAttributes.position||X.morphAttributes.normal||X.morphAttributes.color,ie=$!==void 0?$.length:0,j=0;X.morphAttributes.position!==void 0&&(j=1),X.morphAttributes.normal!==void 0&&(j=2),X.morphAttributes.color!==void 0&&(j=3);let ue,G,J,re;if(k){let at=In[k];ue=at.vertexShader,G=at.fragmentShader}else ue=x.vertexShader,G=x.fragmentShader,c.update(x),J=c.getVertexShaderID(x),re=c.getFragmentShaderID(x);let ee=s.getRenderTarget(),oe=s.state.buffers.depth.getReversed(),ye=D.isInstancedMesh===!0,De=D.isBatchedMesh===!0,Qe=!!x.map,Ce=!!x.matcap,qe=!!K,N=!!x.aoMap,Ft=!!x.lightMap,Ge=!!x.bumpMap,Oe=!!x.normalMap,Re=!!x.displacementMap,ut=!!x.emissiveMap,Ie=!!x.metalnessMap,R=!!x.roughnessMap,S=x.anisotropy>0,W=x.clearcoat>0,te=x.dispersion>0,se=x.iridescence>0,Q=x.sheen>0,Te=x.transmission>0,de=S&&!!x.anisotropyMap,_e=W&&!!x.clearcoatMap,et=W&&!!x.clearcoatNormalMap,ae=W&&!!x.clearcoatRoughnessMap,Me=se&&!!x.iridescenceMap,Pe=se&&!!x.iridescenceThicknessMap,Ue=Q&&!!x.sheenColorMap,be=Q&&!!x.sheenRoughnessMap,Ke=!!x.specularMap,He=!!x.specularColorMap,ht=!!x.specularIntensityMap,U=Te&&!!x.transmissionMap,fe=Te&&!!x.thicknessMap,Z=!!x.gradientMap,ne=!!x.alphaMap,ge=x.alphaTest>0,pe=!!x.alphaHash,Be=!!x.extensions,vt=Ln;x.toneMapped&&(ee===null||ee.isXRRenderTarget===!0)&&(vt=s.toneMapping);let Ot={shaderID:k,shaderType:x.type,shaderName:x.name,vertexShader:ue,fragmentShader:G,defines:x.defines,customVertexShaderID:J,customFragmentShaderID:re,isRawShaderMaterial:x.isRawShaderMaterial===!0,glslVersion:x.glslVersion,precision:p,batching:De,batchingColor:De&&D._colorsTexture!==null,instancing:ye,instancingColor:ye&&D.instanceColor!==null,instancingMorph:ye&&D.morphTexture!==null,supportsVertexTextures:f,outputColorSpace:ee===null?s.outputColorSpace:ee.isXRRenderTarget===!0?ee.texture.colorSpace:Wt,alphaToCoverage:!!x.alphaToCoverage,map:Qe,matcap:Ce,envMap:qe,envMapMode:qe&&K.mapping,envMapCubeUVHeight:H,aoMap:N,lightMap:Ft,bumpMap:Ge,normalMap:Oe,displacementMap:f&&Re,emissiveMap:ut,normalMapObjectSpace:Oe&&x.normalMapType===Ef,normalMapTangentSpace:Oe&&x.normalMapType===oh,metalnessMap:Ie,roughnessMap:R,anisotropy:S,anisotropyMap:de,clearcoat:W,clearcoatMap:_e,clearcoatNormalMap:et,clearcoatRoughnessMap:ae,dispersion:te,iridescence:se,iridescenceMap:Me,iridescenceThicknessMap:Pe,sheen:Q,sheenColorMap:Ue,sheenRoughnessMap:be,specularMap:Ke,specularColorMap:He,specularIntensityMap:ht,transmission:Te,transmissionMap:U,thicknessMap:fe,gradientMap:Z,opaque:x.transparent===!1&&x.blending===Qi&&x.alphaToCoverage===!1,alphaMap:ne,alphaTest:ge,alphaHash:pe,combine:x.combine,mapUv:Qe&&v(x.map.channel),aoMapUv:N&&v(x.aoMap.channel),lightMapUv:Ft&&v(x.lightMap.channel),bumpMapUv:Ge&&v(x.bumpMap.channel),normalMapUv:Oe&&v(x.normalMap.channel),displacementMapUv:Re&&v(x.displacementMap.channel),emissiveMapUv:ut&&v(x.emissiveMap.channel),metalnessMapUv:Ie&&v(x.metalnessMap.channel),roughnessMapUv:R&&v(x.roughnessMap.channel),anisotropyMapUv:de&&v(x.anisotropyMap.channel),clearcoatMapUv:_e&&v(x.clearcoatMap.channel),clearcoatNormalMapUv:et&&v(x.clearcoatNormalMap.channel),clearcoatRoughnessMapUv:ae&&v(x.clearcoatRoughnessMap.channel),iridescenceMapUv:Me&&v(x.iridescenceMap.channel),iridescenceThicknessMapUv:Pe&&v(x.iridescenceThicknessMap.channel),sheenColorMapUv:Ue&&v(x.sheenColorMap.channel),sheenRoughnessMapUv:be&&v(x.sheenRoughnessMap.channel),specularMapUv:Ke&&v(x.specularMap.channel),specularColorMapUv:He&&v(x.specularColorMap.channel),specularIntensityMapUv:ht&&v(x.specularIntensityMap.channel),transmissionMapUv:U&&v(x.transmissionMap.channel),thicknessMapUv:fe&&v(x.thicknessMap.channel),alphaMapUv:ne&&v(x.alphaMap.channel),vertexTangents:!!X.attributes.tangent&&(Oe||S),vertexColors:x.vertexColors,vertexAlphas:x.vertexColors===!0&&!!X.attributes.color&&X.attributes.color.itemSize===4,pointsUvs:D.isPoints===!0&&!!X.attributes.uv&&(Qe||ne),fog:!!F,useFog:x.fog===!0,fogExp2:!!F&&F.isFogExp2,flatShading:x.flatShading===!0,sizeAttenuation:x.sizeAttenuation===!0,logarithmicDepthBuffer:h,reverseDepthBuffer:oe,skinning:D.isSkinnedMesh===!0,morphTargets:X.morphAttributes.position!==void 0,morphNormals:X.morphAttributes.normal!==void 0,morphColors:X.morphAttributes.color!==void 0,morphTargetsCount:ie,morphTextureStride:j,numDirLights:y.directional.length,numPointLights:y.point.length,numSpotLights:y.spot.length,numSpotLightMaps:y.spotLightMap.length,numRectAreaLights:y.rectArea.length,numHemiLights:y.hemi.length,numDirLightShadows:y.directionalShadowMap.length,numPointLightShadows:y.pointShadowMap.length,numSpotLightShadows:y.spotShadowMap.length,numSpotLightShadowsWithMaps:y.numSpotLightShadowsWithMaps,numLightProbes:y.numLightProbes,numClippingPlanes:o.numPlanes,numClipIntersection:o.numIntersection,dithering:x.dithering,shadowMapEnabled:s.shadowMap.enabled&&T.length>0,shadowMapType:s.shadowMap.type,toneMapping:vt,decodeVideoTexture:Qe&&x.map.isVideoTexture===!0&&Ye.getTransfer(x.map.colorSpace)===lt,decodeVideoTextureEmissive:ut&&x.emissiveMap.isVideoTexture===!0&&Ye.getTransfer(x.emissiveMap.colorSpace)===lt,premultipliedAlpha:x.premultipliedAlpha,doubleSided:x.side===Lt,flipSided:x.side===Vt,useDepthPacking:x.depthPacking>=0,depthPacking:x.depthPacking||0,index0AttributeName:x.index0AttributeName,extensionClipCullDistance:Be&&x.extensions.clipCullDistance===!0&&n.has("WEBGL_clip_cull_distance"),extensionMultiDraw:(Be&&x.extensions.multiDraw===!0||De)&&n.has("WEBGL_multi_draw"),rendererExtensionParallelShaderCompile:n.has("KHR_parallel_shader_compile"),customProgramCacheKey:x.customProgramCacheKey()};return Ot.vertexUv1s=l.has(1),Ot.vertexUv2s=l.has(2),Ot.vertexUv3s=l.has(3),l.clear(),Ot}function d(x){let y=[];if(x.shaderID?y.push(x.shaderID):(y.push(x.customVertexShaderID),y.push(x.customFragmentShaderID)),x.defines!==void 0)for(let T in x.defines)y.push(T),y.push(x.defines[T]);return x.isRawShaderMaterial===!1&&(M(y,x),b(y,x),y.push(s.outputColorSpace)),y.push(x.customProgramCacheKey),y.join()}function M(x,y){x.push(y.precision),x.push(y.outputColorSpace),x.push(y.envMapMode),x.push(y.envMapCubeUVHeight),x.push(y.mapUv),x.push(y.alphaMapUv),x.push(y.lightMapUv),x.push(y.aoMapUv),x.push(y.bumpMapUv),x.push(y.normalMapUv),x.push(y.displacementMapUv),x.push(y.emissiveMapUv),x.push(y.metalnessMapUv),x.push(y.roughnessMapUv),x.push(y.anisotropyMapUv),x.push(y.clearcoatMapUv),x.push(y.clearcoatNormalMapUv),x.push(y.clearcoatRoughnessMapUv),x.push(y.iridescenceMapUv),x.push(y.iridescenceThicknessMapUv),x.push(y.sheenColorMapUv),x.push(y.sheenRoughnessMapUv),x.push(y.specularMapUv),x.push(y.specularColorMapUv),x.push(y.specularIntensityMapUv),x.push(y.transmissionMapUv),x.push(y.thicknessMapUv),x.push(y.combine),x.push(y.fogExp2),x.push(y.sizeAttenuation),x.push(y.morphTargetsCount),x.push(y.morphAttributeCount),x.push(y.numDirLights),x.push(y.numPointLights),x.push(y.numSpotLights),x.push(y.numSpotLightMaps),x.push(y.numHemiLights),x.push(y.numRectAreaLights),x.push(y.numDirLightShadows),x.push(y.numPointLightShadows),x.push(y.numSpotLightShadows),x.push(y.numSpotLightShadowsWithMaps),x.push(y.numLightProbes),x.push(y.shadowMapType),x.push(y.toneMapping),x.push(y.numClippingPlanes),x.push(y.numClipIntersection),x.push(y.depthPacking)}function b(x,y){a.disableAll(),y.supportsVertexTextures&&a.enable(0),y.instancing&&a.enable(1),y.instancingColor&&a.enable(2),y.instancingMorph&&a.enable(3),y.matcap&&a.enable(4),y.envMap&&a.enable(5),y.normalMapObjectSpace&&a.enable(6),y.normalMapTangentSpace&&a.enable(7),y.clearcoat&&a.enable(8),y.iridescence&&a.enable(9),y.alphaTest&&a.enable(10),y.vertexColors&&a.enable(11),y.vertexAlphas&&a.enable(12),y.vertexUv1s&&a.enable(13),y.vertexUv2s&&a.enable(14),y.vertexUv3s&&a.enable(15),y.vertexTangents&&a.enable(16),y.anisotropy&&a.enable(17),y.alphaHash&&a.enable(18),y.batching&&a.enable(19),y.dispersion&&a.enable(20),y.batchingColor&&a.enable(21),x.push(a.mask),a.disableAll(),y.fog&&a.enable(0),y.useFog&&a.enable(1),y.flatShading&&a.enable(2),y.logarithmicDepthBuffer&&a.enable(3),y.reverseDepthBuffer&&a.enable(4),y.skinning&&a.enable(5),y.morphTargets&&a.enable(6),y.morphNormals&&a.enable(7),y.morphColors&&a.enable(8),y.premultipliedAlpha&&a.enable(9),y.shadowMapEnabled&&a.enable(10),y.doubleSided&&a.enable(11),y.flipSided&&a.enable(12),y.useDepthPacking&&a.enable(13),y.dithering&&a.enable(14),y.transmission&&a.enable(15),y.sheen&&a.enable(16),y.opaque&&a.enable(17),y.pointsUvs&&a.enable(18),y.decodeVideoTexture&&a.enable(19),y.decodeVideoTextureEmissive&&a.enable(20),y.alphaToCoverage&&a.enable(21),x.push(a.mask)}function _(x){let y=g[x.type],T;if(y){let L=In[y];T=fd.clone(L.uniforms)}else T=x.uniforms;return T}function C(x,y){let T;for(let L=0,D=u.length;L<D;L++){let F=u[L];if(F.cacheKey===y){T=F,++T.usedTimes;break}}return T===void 0&&(T=new yg(s,y,x,r),u.push(T)),T}function A(x){if(--x.usedTimes===0){let y=u.indexOf(x);u[y]=u[u.length-1],u.pop(),x.destroy()}}function E(x){c.remove(x)}function I(){c.dispose()}return{getParameters:m,getProgramCacheKey:d,getUniforms:_,acquireProgram:C,releaseProgram:A,releaseShaderCache:E,programs:u,dispose:I}}function Sg(){let s=new WeakMap;function e(o){return s.has(o)}function t(o){let a=s.get(o);return a===void 0&&(a={},s.set(o,a)),a}function n(o){s.delete(o)}function i(o,a,c){s.get(o)[a]=c}function r(){s=new WeakMap}return{has:e,get:t,remove:n,update:i,dispose:r}}function wg(s,e){return s.groupOrder!==e.groupOrder?s.groupOrder-e.groupOrder:s.renderOrder!==e.renderOrder?s.renderOrder-e.renderOrder:s.material.id!==e.material.id?s.material.id-e.material.id:s.z!==e.z?s.z-e.z:s.id-e.id}function Eu(s,e){return s.groupOrder!==e.groupOrder?s.groupOrder-e.groupOrder:s.renderOrder!==e.renderOrder?s.renderOrder-e.renderOrder:s.z!==e.z?e.z-s.z:s.id-e.id}function Tu(){let s=[],e=0,t=[],n=[],i=[];function r(){e=0,t.length=0,n.length=0,i.length=0}function o(h,f,p,g,v,m){let d=s[e];return d===void 0?(d={id:h.id,object:h,geometry:f,material:p,groupOrder:g,renderOrder:h.renderOrder,z:v,group:m},s[e]=d):(d.id=h.id,d.object=h,d.geometry=f,d.material=p,d.groupOrder=g,d.renderOrder=h.renderOrder,d.z=v,d.group=m),e++,d}function a(h,f,p,g,v,m){let d=o(h,f,p,g,v,m);p.transmission>0?n.push(d):p.transparent===!0?i.push(d):t.push(d)}function c(h,f,p,g,v,m){let d=o(h,f,p,g,v,m);p.transmission>0?n.unshift(d):p.transparent===!0?i.unshift(d):t.unshift(d)}function l(h,f){t.length>1&&t.sort(h||wg),n.length>1&&n.sort(f||Eu),i.length>1&&i.sort(f||Eu)}function u(){for(let h=e,f=s.length;h<f;h++){let p=s[h];if(p.id===null)break;p.id=null,p.object=null,p.geometry=null,p.material=null,p.group=null}}return{opaque:t,transmissive:n,transparent:i,init:r,push:a,unshift:c,finish:u,sort:l}}function Eg(){let s=new WeakMap;function e(n,i){let r=s.get(n),o;return r===void 0?(o=new Tu,s.set(n,[o])):i>=r.length?(o=new Tu,r.push(o)):o=r[i],o}function t(){s=new WeakMap}return{get:e,dispose:t}}function Tg(){let s={};return{get:function(e){if(s[e.id]!==void 0)return s[e.id];let t;switch(e.type){case"DirectionalLight":t={direction:new P,color:new ve};break;case"SpotLight":t={position:new P,direction:new P,color:new ve,distance:0,coneCos:0,penumbraCos:0,decay:0};break;case"PointLight":t={position:new P,color:new ve,distance:0,decay:0};break;case"HemisphereLight":t={direction:new P,skyColor:new ve,groundColor:new ve};break;case"RectAreaLight":t={color:new ve,position:new P,halfWidth:new P,halfHeight:new P};break}return s[e.id]=t,t}}}function Ag(){let s={};return{get:function(e){if(s[e.id]!==void 0)return s[e.id];let t;switch(e.type){case"DirectionalLight":t={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new le};break;case"SpotLight":t={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new le};break;case"PointLight":t={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new le,shadowCameraNear:1,shadowCameraFar:1e3};break}return s[e.id]=t,t}}}var Rg=0;function Cg(s,e){return(e.castShadow?2:0)-(s.castShadow?2:0)+(e.map?1:0)-(s.map?1:0)}function Ig(s){let e=new Tg,t=Ag(),n={version:0,hash:{directionalLength:-1,pointLength:-1,spotLength:-1,rectAreaLength:-1,hemiLength:-1,numDirectionalShadows:-1,numPointShadows:-1,numSpotShadows:-1,numSpotMaps:-1,numLightProbes:-1},ambient:[0,0,0],probe:[],directional:[],directionalShadow:[],directionalShadowMap:[],directionalShadowMatrix:[],spot:[],spotLightMap:[],spotShadow:[],spotShadowMap:[],spotLightMatrix:[],rectArea:[],rectAreaLTC1:null,rectAreaLTC2:null,point:[],pointShadow:[],pointShadowMap:[],pointShadowMatrix:[],hemi:[],numSpotLightShadowsWithMaps:0,numLightProbes:0};for(let l=0;l<9;l++)n.probe.push(new P);let i=new P,r=new Le,o=new Le;function a(l){let u=0,h=0,f=0;for(let x=0;x<9;x++)n.probe[x].set(0,0,0);let p=0,g=0,v=0,m=0,d=0,M=0,b=0,_=0,C=0,A=0,E=0;l.sort(Cg);for(let x=0,y=l.length;x<y;x++){let T=l[x],L=T.color,D=T.intensity,F=T.distance,X=T.shadow&&T.shadow.map?T.shadow.map.texture:null;if(T.isAmbientLight)u+=L.r*D,h+=L.g*D,f+=L.b*D;else if(T.isLightProbe){for(let z=0;z<9;z++)n.probe[z].addScaledVector(T.sh.coefficients[z],D);E++}else if(T.isDirectionalLight){let z=e.get(T);if(z.color.copy(T.color).multiplyScalar(T.intensity),T.castShadow){let K=T.shadow,H=t.get(T);H.shadowIntensity=K.intensity,H.shadowBias=K.bias,H.shadowNormalBias=K.normalBias,H.shadowRadius=K.radius,H.shadowMapSize=K.mapSize,n.directionalShadow[p]=H,n.directionalShadowMap[p]=X,n.directionalShadowMatrix[p]=T.shadow.matrix,M++}n.directional[p]=z,p++}else if(T.isSpotLight){let z=e.get(T);z.position.setFromMatrixPosition(T.matrixWorld),z.color.copy(L).multiplyScalar(D),z.distance=F,z.coneCos=Math.cos(T.angle),z.penumbraCos=Math.cos(T.angle*(1-T.penumbra)),z.decay=T.decay,n.spot[v]=z;let K=T.shadow;if(T.map&&(n.spotLightMap[C]=T.map,C++,K.updateMatrices(T),T.castShadow&&A++),n.spotLightMatrix[v]=K.matrix,T.castShadow){let H=t.get(T);H.shadowIntensity=K.intensity,H.shadowBias=K.bias,H.shadowNormalBias=K.normalBias,H.shadowRadius=K.radius,H.shadowMapSize=K.mapSize,n.spotShadow[v]=H,n.spotShadowMap[v]=X,_++}v++}else if(T.isRectAreaLight){let z=e.get(T);z.color.copy(L).multiplyScalar(D),z.halfWidth.set(T.width*.5,0,0),z.halfHeight.set(0,T.height*.5,0),n.rectArea[m]=z,m++}else if(T.isPointLight){let z=e.get(T);if(z.color.copy(T.color).multiplyScalar(T.intensity),z.distance=T.distance,z.decay=T.decay,T.castShadow){let K=T.shadow,H=t.get(T);H.shadowIntensity=K.intensity,H.shadowBias=K.bias,H.shadowNormalBias=K.normalBias,H.shadowRadius=K.radius,H.shadowMapSize=K.mapSize,H.shadowCameraNear=K.camera.near,H.shadowCameraFar=K.camera.far,n.pointShadow[g]=H,n.pointShadowMap[g]=X,n.pointShadowMatrix[g]=T.shadow.matrix,b++}n.point[g]=z,g++}else if(T.isHemisphereLight){let z=e.get(T);z.skyColor.copy(T.color).multiplyScalar(D),z.groundColor.copy(T.groundColor).multiplyScalar(D),n.hemi[d]=z,d++}}m>0&&(s.has("OES_texture_float_linear")===!0?(n.rectAreaLTC1=he.LTC_FLOAT_1,n.rectAreaLTC2=he.LTC_FLOAT_2):(n.rectAreaLTC1=he.LTC_HALF_1,n.rectAreaLTC2=he.LTC_HALF_2)),n.ambient[0]=u,n.ambient[1]=h,n.ambient[2]=f;let I=n.hash;(I.directionalLength!==p||I.pointLength!==g||I.spotLength!==v||I.rectAreaLength!==m||I.hemiLength!==d||I.numDirectionalShadows!==M||I.numPointShadows!==b||I.numSpotShadows!==_||I.numSpotMaps!==C||I.numLightProbes!==E)&&(n.directional.length=p,n.spot.length=v,n.rectArea.length=m,n.point.length=g,n.hemi.length=d,n.directionalShadow.length=M,n.directionalShadowMap.length=M,n.pointShadow.length=b,n.pointShadowMap.length=b,n.spotShadow.length=_,n.spotShadowMap.length=_,n.directionalShadowMatrix.length=M,n.pointShadowMatrix.length=b,n.spotLightMatrix.length=_+C-A,n.spotLightMap.length=C,n.numSpotLightShadowsWithMaps=A,n.numLightProbes=E,I.directionalLength=p,I.pointLength=g,I.spotLength=v,I.rectAreaLength=m,I.hemiLength=d,I.numDirectionalShadows=M,I.numPointShadows=b,I.numSpotShadows=_,I.numSpotMaps=C,I.numLightProbes=E,n.version=Rg++)}function c(l,u){let h=0,f=0,p=0,g=0,v=0,m=u.matrixWorldInverse;for(let d=0,M=l.length;d<M;d++){let b=l[d];if(b.isDirectionalLight){let _=n.directional[h];_.direction.setFromMatrixPosition(b.matrixWorld),i.setFromMatrixPosition(b.target.matrixWorld),_.direction.sub(i),_.direction.transformDirection(m),h++}else if(b.isSpotLight){let _=n.spot[p];_.position.setFromMatrixPosition(b.matrixWorld),_.position.applyMatrix4(m),_.direction.setFromMatrixPosition(b.matrixWorld),i.setFromMatrixPosition(b.target.matrixWorld),_.direction.sub(i),_.direction.transformDirection(m),p++}else if(b.isRectAreaLight){let _=n.rectArea[g];_.position.setFromMatrixPosition(b.matrixWorld),_.position.applyMatrix4(m),o.identity(),r.copy(b.matrixWorld),r.premultiply(m),o.extractRotation(r),_.halfWidth.set(b.width*.5,0,0),_.halfHeight.set(0,b.height*.5,0),_.halfWidth.applyMatrix4(o),_.halfHeight.applyMatrix4(o),g++}else if(b.isPointLight){let _=n.point[f];_.position.setFromMatrixPosition(b.matrixWorld),_.position.applyMatrix4(m),f++}else if(b.isHemisphereLight){let _=n.hemi[v];_.direction.setFromMatrixPosition(b.matrixWorld),_.direction.transformDirection(m),v++}}}return{setup:a,setupView:c,state:n}}function Au(s){let e=new Ig(s),t=[],n=[];function i(u){l.camera=u,t.length=0,n.length=0}function r(u){t.push(u)}function o(u){n.push(u)}function a(){e.setup(t)}function c(u){e.setupView(t,u)}let l={lightsArray:t,shadowsArray:n,camera:null,lights:e,transmissionRenderTarget:{}};return{init:i,state:l,setupLights:a,setupLightsView:c,pushLight:r,pushShadow:o}}function Pg(s){let e=new WeakMap;function t(i,r=0){let o=e.get(i),a;return o===void 0?(a=new Au(s),e.set(i,[a])):r>=o.length?(a=new Au(s),o.push(a)):a=o[r],a}function n(){e=new WeakMap}return{get:t,dispose:n}}var Qa=class extends an{static get type(){return"MeshDepthMaterial"}constructor(e){super(),this.isMeshDepthMaterial=!0,this.depthPacking=Sf,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.wireframe=!1,this.wireframeLinewidth=1,this.setValues(e)}copy(e){return super.copy(e),this.depthPacking=e.depthPacking,this.map=e.map,this.alphaMap=e.alphaMap,this.displacementMap=e.displacementMap,this.displacementScale=e.displacementScale,this.displacementBias=e.displacementBias,this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this}},ec=class extends an{static get type(){return"MeshDistanceMaterial"}constructor(e){super(),this.isMeshDistanceMaterial=!0,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.setValues(e)}copy(e){return super.copy(e),this.map=e.map,this.alphaMap=e.alphaMap,this.displacementMap=e.displacementMap,this.displacementScale=e.displacementScale,this.displacementBias=e.displacementBias,this}},Lg=`void main() {
	gl_Position = vec4( position, 1.0 );
}`,Dg=`uniform sampler2D shadow_pass;
uniform vec2 resolution;
uniform float radius;
#include <packing>
void main() {
	const float samples = float( VSM_SAMPLES );
	float mean = 0.0;
	float squared_mean = 0.0;
	float uvStride = samples <= 1.0 ? 0.0 : 2.0 / ( samples - 1.0 );
	float uvStart = samples <= 1.0 ? 0.0 : - 1.0;
	for ( float i = 0.0; i < samples; i ++ ) {
		float uvOffset = uvStart + i * uvStride;
		#ifdef HORIZONTAL_PASS
			vec2 distribution = unpackRGBATo2Half( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( uvOffset, 0.0 ) * radius ) / resolution ) );
			mean += distribution.x;
			squared_mean += distribution.y * distribution.y + distribution.x * distribution.x;
		#else
			float depth = unpackRGBAToDepth( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( 0.0, uvOffset ) * radius ) / resolution ) );
			mean += depth;
			squared_mean += depth * depth;
		#endif
	}
	mean = mean / samples;
	squared_mean = squared_mean / samples;
	float std_dev = sqrt( squared_mean - mean * mean );
	gl_FragColor = pack2HalfToRGBA( vec2( mean, std_dev ) );
}`;function Ug(s,e,t){let n=new Ks,i=new le,r=new le,o=new We,a=new Qa({depthPacking:wf}),c=new ec,l={},u=t.maxTextureSize,h={[en]:Vt,[Vt]:en,[Lt]:Lt},f=new Gt({defines:{VSM_SAMPLES:8},uniforms:{shadow_pass:{value:null},resolution:{value:new le},radius:{value:4}},vertexShader:Lg,fragmentShader:Dg}),p=f.clone();p.defines.HORIZONTAL_PASS=1;let g=new Mt;g.setAttribute("position",new it(new Float32Array([-1,-1,.5,3,-1,.5,-1,3,.5]),3));let v=new Fe(g,f),m=this;this.enabled=!1,this.autoUpdate=!0,this.needsUpdate=!1,this.type=Yu;let d=this.type;this.render=function(A,E,I){if(m.enabled===!1||m.autoUpdate===!1&&m.needsUpdate===!1||A.length===0)return;let x=s.getRenderTarget(),y=s.getActiveCubeFace(),T=s.getActiveMipmapLevel(),L=s.state;L.setBlending(li),L.buffers.color.setClear(1,1,1,1),L.buffers.depth.setTest(!0),L.setScissorTest(!1);let D=d!==Gn&&this.type===Gn,F=d===Gn&&this.type!==Gn;for(let X=0,z=A.length;X<z;X++){let K=A[X],H=K.shadow;if(H===void 0){console.warn("THREE.WebGLShadowMap:",K,"has no shadow.");continue}if(H.autoUpdate===!1&&H.needsUpdate===!1)continue;i.copy(H.mapSize);let k=H.getFrameExtents();if(i.multiply(k),r.copy(H.mapSize),(i.x>u||i.y>u)&&(i.x>u&&(r.x=Math.floor(u/k.x),i.x=r.x*k.x,H.mapSize.x=r.x),i.y>u&&(r.y=Math.floor(u/k.y),i.y=r.y*k.y,H.mapSize.y=r.y)),H.map===null||D===!0||F===!0){let ie=this.type!==Gn?{minFilter:yt,magFilter:yt}:{};H.map!==null&&H.map.dispose(),H.map=new Rn(i.x,i.y,ie),H.map.texture.name=K.name+".shadowMap",H.camera.updateProjectionMatrix()}s.setRenderTarget(H.map),s.clear();let $=H.getViewportCount();for(let ie=0;ie<$;ie++){let j=H.getViewport(ie);o.set(r.x*j.x,r.y*j.y,r.x*j.z,r.y*j.w),L.viewport(o),H.updateMatrices(K,ie),n=H.getFrustum(),_(E,I,H.camera,K,this.type)}H.isPointLightShadow!==!0&&this.type===Gn&&M(H,I),H.needsUpdate=!1}d=this.type,m.needsUpdate=!1,s.setRenderTarget(x,y,T)};function M(A,E){let I=e.update(v);f.defines.VSM_SAMPLES!==A.blurSamples&&(f.defines.VSM_SAMPLES=A.blurSamples,p.defines.VSM_SAMPLES=A.blurSamples,f.needsUpdate=!0,p.needsUpdate=!0),A.mapPass===null&&(A.mapPass=new Rn(i.x,i.y)),f.uniforms.shadow_pass.value=A.map.texture,f.uniforms.resolution.value=A.mapSize,f.uniforms.radius.value=A.radius,s.setRenderTarget(A.mapPass),s.clear(),s.renderBufferDirect(E,null,I,f,v,null),p.uniforms.shadow_pass.value=A.mapPass.texture,p.uniforms.resolution.value=A.mapSize,p.uniforms.radius.value=A.radius,s.setRenderTarget(A.map),s.clear(),s.renderBufferDirect(E,null,I,p,v,null)}function b(A,E,I,x){let y=null,T=I.isPointLight===!0?A.customDistanceMaterial:A.customDepthMaterial;if(T!==void 0)y=T;else if(y=I.isPointLight===!0?c:a,s.localClippingEnabled&&E.clipShadows===!0&&Array.isArray(E.clippingPlanes)&&E.clippingPlanes.length!==0||E.displacementMap&&E.displacementScale!==0||E.alphaMap&&E.alphaTest>0||E.map&&E.alphaTest>0){let L=y.uuid,D=E.uuid,F=l[L];F===void 0&&(F={},l[L]=F);let X=F[D];X===void 0&&(X=y.clone(),F[D]=X,E.addEventListener("dispose",C)),y=X}if(y.visible=E.visible,y.wireframe=E.wireframe,x===Gn?y.side=E.shadowSide!==null?E.shadowSide:E.side:y.side=E.shadowSide!==null?E.shadowSide:h[E.side],y.alphaMap=E.alphaMap,y.alphaTest=E.alphaTest,y.map=E.map,y.clipShadows=E.clipShadows,y.clippingPlanes=E.clippingPlanes,y.clipIntersection=E.clipIntersection,y.displacementMap=E.displacementMap,y.displacementScale=E.displacementScale,y.displacementBias=E.displacementBias,y.wireframeLinewidth=E.wireframeLinewidth,y.linewidth=E.linewidth,I.isPointLight===!0&&y.isMeshDistanceMaterial===!0){let L=s.properties.get(y);L.light=I}return y}function _(A,E,I,x,y){if(A.visible===!1)return;if(A.layers.test(E.layers)&&(A.isMesh||A.isLine||A.isPoints)&&(A.castShadow||A.receiveShadow&&y===Gn)&&(!A.frustumCulled||n.intersectsObject(A))){A.modelViewMatrix.multiplyMatrices(I.matrixWorldInverse,A.matrixWorld);let D=e.update(A),F=A.material;if(Array.isArray(F)){let X=D.groups;for(let z=0,K=X.length;z<K;z++){let H=X[z],k=F[H.materialIndex];if(k&&k.visible){let $=b(A,k,x,y);A.onBeforeShadow(s,A,E,I,D,$,H),s.renderBufferDirect(I,null,D,$,A,H),A.onAfterShadow(s,A,E,I,D,$,H)}}}else if(F.visible){let X=b(A,F,x,y);A.onBeforeShadow(s,A,E,I,D,X,null),s.renderBufferDirect(I,null,D,X,A,null),A.onAfterShadow(s,A,E,I,D,X,null)}}let L=A.children;for(let D=0,F=L.length;D<F;D++)_(L[D],E,I,x,y)}function C(A){A.target.removeEventListener("dispose",C);for(let I in l){let x=l[I],y=A.target.uuid;y in x&&(x[y].dispose(),delete x[y])}}}var Ng={[oa]:aa,[ca]:ha,[la]:fa,[ss]:ua,[aa]:oa,[ha]:ca,[fa]:la,[ua]:ss};function Fg(s,e){function t(){let U=!1,fe=new We,Z=null,ne=new We(0,0,0,0);return{setMask:function(ge){Z!==ge&&!U&&(s.colorMask(ge,ge,ge,ge),Z=ge)},setLocked:function(ge){U=ge},setClear:function(ge,pe,Be,vt,Ot){Ot===!0&&(ge*=vt,pe*=vt,Be*=vt),fe.set(ge,pe,Be,vt),ne.equals(fe)===!1&&(s.clearColor(ge,pe,Be,vt),ne.copy(fe))},reset:function(){U=!1,Z=null,ne.set(-1,0,0,0)}}}function n(){let U=!1,fe=!1,Z=null,ne=null,ge=null;return{setReversed:function(pe){if(fe!==pe){let Be=e.get("EXT_clip_control");fe?Be.clipControlEXT(Be.LOWER_LEFT_EXT,Be.ZERO_TO_ONE_EXT):Be.clipControlEXT(Be.LOWER_LEFT_EXT,Be.NEGATIVE_ONE_TO_ONE_EXT);let vt=ge;ge=null,this.setClear(vt)}fe=pe},getReversed:function(){return fe},setTest:function(pe){pe?ee(s.DEPTH_TEST):oe(s.DEPTH_TEST)},setMask:function(pe){Z!==pe&&!U&&(s.depthMask(pe),Z=pe)},setFunc:function(pe){if(fe&&(pe=Ng[pe]),ne!==pe){switch(pe){case oa:s.depthFunc(s.NEVER);break;case aa:s.depthFunc(s.ALWAYS);break;case ca:s.depthFunc(s.LESS);break;case ss:s.depthFunc(s.LEQUAL);break;case la:s.depthFunc(s.EQUAL);break;case ua:s.depthFunc(s.GEQUAL);break;case ha:s.depthFunc(s.GREATER);break;case fa:s.depthFunc(s.NOTEQUAL);break;default:s.depthFunc(s.LEQUAL)}ne=pe}},setLocked:function(pe){U=pe},setClear:function(pe){ge!==pe&&(fe&&(pe=1-pe),s.clearDepth(pe),ge=pe)},reset:function(){U=!1,Z=null,ne=null,ge=null,fe=!1}}}function i(){let U=!1,fe=null,Z=null,ne=null,ge=null,pe=null,Be=null,vt=null,Ot=null;return{setTest:function(at){U||(at?ee(s.STENCIL_TEST):oe(s.STENCIL_TEST))},setMask:function(at){fe!==at&&!U&&(s.stencilMask(at),fe=at)},setFunc:function(at,xn,Nn){(Z!==at||ne!==xn||ge!==Nn)&&(s.stencilFunc(at,xn,Nn),Z=at,ne=xn,ge=Nn)},setOp:function(at,xn,Nn){(pe!==at||Be!==xn||vt!==Nn)&&(s.stencilOp(at,xn,Nn),pe=at,Be=xn,vt=Nn)},setLocked:function(at){U=at},setClear:function(at){Ot!==at&&(s.clearStencil(at),Ot=at)},reset:function(){U=!1,fe=null,Z=null,ne=null,ge=null,pe=null,Be=null,vt=null,Ot=null}}}let r=new t,o=new n,a=new i,c=new WeakMap,l=new WeakMap,u={},h={},f=new WeakMap,p=[],g=null,v=!1,m=null,d=null,M=null,b=null,_=null,C=null,A=null,E=new ve(0,0,0),I=0,x=!1,y=null,T=null,L=null,D=null,F=null,X=s.getParameter(s.MAX_COMBINED_TEXTURE_IMAGE_UNITS),z=!1,K=0,H=s.getParameter(s.VERSION);H.indexOf("WebGL")!==-1?(K=parseFloat(/^WebGL (\d)/.exec(H)[1]),z=K>=1):H.indexOf("OpenGL ES")!==-1&&(K=parseFloat(/^OpenGL ES (\d)/.exec(H)[1]),z=K>=2);let k=null,$={},ie=s.getParameter(s.SCISSOR_BOX),j=s.getParameter(s.VIEWPORT),ue=new We().fromArray(ie),G=new We().fromArray(j);function J(U,fe,Z,ne){let ge=new Uint8Array(4),pe=s.createTexture();s.bindTexture(U,pe),s.texParameteri(U,s.TEXTURE_MIN_FILTER,s.NEAREST),s.texParameteri(U,s.TEXTURE_MAG_FILTER,s.NEAREST);for(let Be=0;Be<Z;Be++)U===s.TEXTURE_3D||U===s.TEXTURE_2D_ARRAY?s.texImage3D(fe,0,s.RGBA,1,1,ne,0,s.RGBA,s.UNSIGNED_BYTE,ge):s.texImage2D(fe+Be,0,s.RGBA,1,1,0,s.RGBA,s.UNSIGNED_BYTE,ge);return pe}let re={};re[s.TEXTURE_2D]=J(s.TEXTURE_2D,s.TEXTURE_2D,1),re[s.TEXTURE_CUBE_MAP]=J(s.TEXTURE_CUBE_MAP,s.TEXTURE_CUBE_MAP_POSITIVE_X,6),re[s.TEXTURE_2D_ARRAY]=J(s.TEXTURE_2D_ARRAY,s.TEXTURE_2D_ARRAY,1,1),re[s.TEXTURE_3D]=J(s.TEXTURE_3D,s.TEXTURE_3D,1,1),r.setClear(0,0,0,1),o.setClear(1),a.setClear(0),ee(s.DEPTH_TEST),o.setFunc(ss),Ge(!1),Oe(Cl),ee(s.CULL_FACE),N(li);function ee(U){u[U]!==!0&&(s.enable(U),u[U]=!0)}function oe(U){u[U]!==!1&&(s.disable(U),u[U]=!1)}function ye(U,fe){return h[U]!==fe?(s.bindFramebuffer(U,fe),h[U]=fe,U===s.DRAW_FRAMEBUFFER&&(h[s.FRAMEBUFFER]=fe),U===s.FRAMEBUFFER&&(h[s.DRAW_FRAMEBUFFER]=fe),!0):!1}function De(U,fe){let Z=p,ne=!1;if(U){Z=f.get(fe),Z===void 0&&(Z=[],f.set(fe,Z));let ge=U.textures;if(Z.length!==ge.length||Z[0]!==s.COLOR_ATTACHMENT0){for(let pe=0,Be=ge.length;pe<Be;pe++)Z[pe]=s.COLOR_ATTACHMENT0+pe;Z.length=ge.length,ne=!0}}else Z[0]!==s.BACK&&(Z[0]=s.BACK,ne=!0);ne&&s.drawBuffers(Z)}function Qe(U){return g!==U?(s.useProgram(U),g=U,!0):!1}let Ce={[Ii]:s.FUNC_ADD,[$h]:s.FUNC_SUBTRACT,[Zh]:s.FUNC_REVERSE_SUBTRACT};Ce[Kh]=s.MIN,Ce[Jh]=s.MAX;let qe={[jh]:s.ZERO,[Qh]:s.ONE,[ef]:s.SRC_COLOR,[sa]:s.SRC_ALPHA,[af]:s.SRC_ALPHA_SATURATE,[rf]:s.DST_COLOR,[nf]:s.DST_ALPHA,[tf]:s.ONE_MINUS_SRC_COLOR,[ra]:s.ONE_MINUS_SRC_ALPHA,[of]:s.ONE_MINUS_DST_COLOR,[sf]:s.ONE_MINUS_DST_ALPHA,[cf]:s.CONSTANT_COLOR,[lf]:s.ONE_MINUS_CONSTANT_COLOR,[uf]:s.CONSTANT_ALPHA,[hf]:s.ONE_MINUS_CONSTANT_ALPHA};function N(U,fe,Z,ne,ge,pe,Be,vt,Ot,at){if(U===li){v===!0&&(oe(s.BLEND),v=!1);return}if(v===!1&&(ee(s.BLEND),v=!0),U!==Yh){if(U!==m||at!==x){if((d!==Ii||_!==Ii)&&(s.blendEquation(s.FUNC_ADD),d=Ii,_=Ii),at)switch(U){case Qi:s.blendFuncSeparate(s.ONE,s.ONE_MINUS_SRC_ALPHA,s.ONE,s.ONE_MINUS_SRC_ALPHA);break;case is:s.blendFunc(s.ONE,s.ONE);break;case Il:s.blendFuncSeparate(s.ZERO,s.ONE_MINUS_SRC_COLOR,s.ZERO,s.ONE);break;case Pl:s.blendFuncSeparate(s.ZERO,s.SRC_COLOR,s.ZERO,s.SRC_ALPHA);break;default:console.error("THREE.WebGLState: Invalid blending: ",U);break}else switch(U){case Qi:s.blendFuncSeparate(s.SRC_ALPHA,s.ONE_MINUS_SRC_ALPHA,s.ONE,s.ONE_MINUS_SRC_ALPHA);break;case is:s.blendFunc(s.SRC_ALPHA,s.ONE);break;case Il:s.blendFuncSeparate(s.ZERO,s.ONE_MINUS_SRC_COLOR,s.ZERO,s.ONE);break;case Pl:s.blendFunc(s.ZERO,s.SRC_COLOR);break;default:console.error("THREE.WebGLState: Invalid blending: ",U);break}M=null,b=null,C=null,A=null,E.set(0,0,0),I=0,m=U,x=at}return}ge=ge||fe,pe=pe||Z,Be=Be||ne,(fe!==d||ge!==_)&&(s.blendEquationSeparate(Ce[fe],Ce[ge]),d=fe,_=ge),(Z!==M||ne!==b||pe!==C||Be!==A)&&(s.blendFuncSeparate(qe[Z],qe[ne],qe[pe],qe[Be]),M=Z,b=ne,C=pe,A=Be),(vt.equals(E)===!1||Ot!==I)&&(s.blendColor(vt.r,vt.g,vt.b,Ot),E.copy(vt),I=Ot),m=U,x=!1}function Ft(U,fe){U.side===Lt?oe(s.CULL_FACE):ee(s.CULL_FACE);let Z=U.side===Vt;fe&&(Z=!Z),Ge(Z),U.blending===Qi&&U.transparent===!1?N(li):N(U.blending,U.blendEquation,U.blendSrc,U.blendDst,U.blendEquationAlpha,U.blendSrcAlpha,U.blendDstAlpha,U.blendColor,U.blendAlpha,U.premultipliedAlpha),o.setFunc(U.depthFunc),o.setTest(U.depthTest),o.setMask(U.depthWrite),r.setMask(U.colorWrite);let ne=U.stencilWrite;a.setTest(ne),ne&&(a.setMask(U.stencilWriteMask),a.setFunc(U.stencilFunc,U.stencilRef,U.stencilFuncMask),a.setOp(U.stencilFail,U.stencilZFail,U.stencilZPass)),ut(U.polygonOffset,U.polygonOffsetFactor,U.polygonOffsetUnits),U.alphaToCoverage===!0?ee(s.SAMPLE_ALPHA_TO_COVERAGE):oe(s.SAMPLE_ALPHA_TO_COVERAGE)}function Ge(U){y!==U&&(U?s.frontFace(s.CW):s.frontFace(s.CCW),y=U)}function Oe(U){U!==Xh?(ee(s.CULL_FACE),U!==T&&(U===Cl?s.cullFace(s.BACK):U===qh?s.cullFace(s.FRONT):s.cullFace(s.FRONT_AND_BACK))):oe(s.CULL_FACE),T=U}function Re(U){U!==L&&(z&&s.lineWidth(U),L=U)}function ut(U,fe,Z){U?(ee(s.POLYGON_OFFSET_FILL),(D!==fe||F!==Z)&&(s.polygonOffset(fe,Z),D=fe,F=Z)):oe(s.POLYGON_OFFSET_FILL)}function Ie(U){U?ee(s.SCISSOR_TEST):oe(s.SCISSOR_TEST)}function R(U){U===void 0&&(U=s.TEXTURE0+X-1),k!==U&&(s.activeTexture(U),k=U)}function S(U,fe,Z){Z===void 0&&(k===null?Z=s.TEXTURE0+X-1:Z=k);let ne=$[Z];ne===void 0&&(ne={type:void 0,texture:void 0},$[Z]=ne),(ne.type!==U||ne.texture!==fe)&&(k!==Z&&(s.activeTexture(Z),k=Z),s.bindTexture(U,fe||re[U]),ne.type=U,ne.texture=fe)}function W(){let U=$[k];U!==void 0&&U.type!==void 0&&(s.bindTexture(U.type,null),U.type=void 0,U.texture=void 0)}function te(){try{s.compressedTexImage2D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function se(){try{s.compressedTexImage3D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function Q(){try{s.texSubImage2D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function Te(){try{s.texSubImage3D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function de(){try{s.compressedTexSubImage2D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function _e(){try{s.compressedTexSubImage3D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function et(){try{s.texStorage2D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function ae(){try{s.texStorage3D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function Me(){try{s.texImage2D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function Pe(){try{s.texImage3D.apply(s,arguments)}catch(U){console.error("THREE.WebGLState:",U)}}function Ue(U){ue.equals(U)===!1&&(s.scissor(U.x,U.y,U.z,U.w),ue.copy(U))}function be(U){G.equals(U)===!1&&(s.viewport(U.x,U.y,U.z,U.w),G.copy(U))}function Ke(U,fe){let Z=l.get(fe);Z===void 0&&(Z=new WeakMap,l.set(fe,Z));let ne=Z.get(U);ne===void 0&&(ne=s.getUniformBlockIndex(fe,U.name),Z.set(U,ne))}function He(U,fe){let ne=l.get(fe).get(U);c.get(fe)!==ne&&(s.uniformBlockBinding(fe,ne,U.__bindingPointIndex),c.set(fe,ne))}function ht(){s.disable(s.BLEND),s.disable(s.CULL_FACE),s.disable(s.DEPTH_TEST),s.disable(s.POLYGON_OFFSET_FILL),s.disable(s.SCISSOR_TEST),s.disable(s.STENCIL_TEST),s.disable(s.SAMPLE_ALPHA_TO_COVERAGE),s.blendEquation(s.FUNC_ADD),s.blendFunc(s.ONE,s.ZERO),s.blendFuncSeparate(s.ONE,s.ZERO,s.ONE,s.ZERO),s.blendColor(0,0,0,0),s.colorMask(!0,!0,!0,!0),s.clearColor(0,0,0,0),s.depthMask(!0),s.depthFunc(s.LESS),o.setReversed(!1),s.clearDepth(1),s.stencilMask(4294967295),s.stencilFunc(s.ALWAYS,0,4294967295),s.stencilOp(s.KEEP,s.KEEP,s.KEEP),s.clearStencil(0),s.cullFace(s.BACK),s.frontFace(s.CCW),s.polygonOffset(0,0),s.activeTexture(s.TEXTURE0),s.bindFramebuffer(s.FRAMEBUFFER,null),s.bindFramebuffer(s.DRAW_FRAMEBUFFER,null),s.bindFramebuffer(s.READ_FRAMEBUFFER,null),s.useProgram(null),s.lineWidth(1),s.scissor(0,0,s.canvas.width,s.canvas.height),s.viewport(0,0,s.canvas.width,s.canvas.height),u={},k=null,$={},h={},f=new WeakMap,p=[],g=null,v=!1,m=null,d=null,M=null,b=null,_=null,C=null,A=null,E=new ve(0,0,0),I=0,x=!1,y=null,T=null,L=null,D=null,F=null,ue.set(0,0,s.canvas.width,s.canvas.height),G.set(0,0,s.canvas.width,s.canvas.height),r.reset(),o.reset(),a.reset()}return{buffers:{color:r,depth:o,stencil:a},enable:ee,disable:oe,bindFramebuffer:ye,drawBuffers:De,useProgram:Qe,setBlending:N,setMaterial:Ft,setFlipSided:Ge,setCullFace:Oe,setLineWidth:Re,setPolygonOffset:ut,setScissorTest:Ie,activeTexture:R,bindTexture:S,unbindTexture:W,compressedTexImage2D:te,compressedTexImage3D:se,texImage2D:Me,texImage3D:Pe,updateUBOMapping:Ke,uniformBlockBinding:He,texStorage2D:et,texStorage3D:ae,texSubImage2D:Q,texSubImage3D:Te,compressedTexSubImage2D:de,compressedTexSubImage3D:_e,scissor:Ue,viewport:be,reset:ht}}function Ru(s,e,t,n){let i=Og(n);switch(t){case Qu:return s*e;case th:return s*e;case nh:return s*e*2;case bc:return s*e/i.components*i.byteLength;case Sc:return s*e/i.components*i.byteLength;case ih:return s*e*2/i.components*i.byteLength;case wc:return s*e*2/i.components*i.byteLength;case eh:return s*e*3/i.components*i.byteLength;case Ht:return s*e*4/i.components*i.byteLength;case Ec:return s*e*4/i.components*i.byteLength;case Hr:case Vr:return Math.floor((s+3)/4)*Math.floor((e+3)/4)*8;case Gr:case Wr:return Math.floor((s+3)/4)*Math.floor((e+3)/4)*16;case ga:case xa:return Math.max(s,16)*Math.max(e,8)/4;case ma:case va:return Math.max(s,8)*Math.max(e,8)/2;case _a:case ya:return Math.floor((s+3)/4)*Math.floor((e+3)/4)*8;case Ma:return Math.floor((s+3)/4)*Math.floor((e+3)/4)*16;case ba:return Math.floor((s+3)/4)*Math.floor((e+3)/4)*16;case Sa:return Math.floor((s+4)/5)*Math.floor((e+3)/4)*16;case wa:return Math.floor((s+4)/5)*Math.floor((e+4)/5)*16;case Ea:return Math.floor((s+5)/6)*Math.floor((e+4)/5)*16;case Ta:return Math.floor((s+5)/6)*Math.floor((e+5)/6)*16;case Aa:return Math.floor((s+7)/8)*Math.floor((e+4)/5)*16;case Ra:return Math.floor((s+7)/8)*Math.floor((e+5)/6)*16;case Ca:return Math.floor((s+7)/8)*Math.floor((e+7)/8)*16;case Ia:return Math.floor((s+9)/10)*Math.floor((e+4)/5)*16;case Pa:return Math.floor((s+9)/10)*Math.floor((e+5)/6)*16;case La:return Math.floor((s+9)/10)*Math.floor((e+7)/8)*16;case Da:return Math.floor((s+9)/10)*Math.floor((e+9)/10)*16;case Ua:return Math.floor((s+11)/12)*Math.floor((e+9)/10)*16;case Na:return Math.floor((s+11)/12)*Math.floor((e+11)/12)*16;case Xr:case Fa:case Oa:return Math.ceil(s/4)*Math.ceil(e/4)*16;case sh:case Ba:return Math.ceil(s/4)*Math.ceil(e/4)*8;case za:case ka:return Math.ceil(s/4)*Math.ceil(e/4)*16}throw new Error(`Unable to determine texture byte length for ${t} format.`)}function Og(s){switch(s){case Dt:case Ku:return{byteLength:1,components:1};case $s:case Ju:case $e:return{byteLength:2,components:1};case yc:case Mc:return{byteLength:2,components:4};case Yn:case _c:case Tn:return{byteLength:4,components:1};case ju:return{byteLength:4,components:3}}throw new Error(`Unknown texture type ${s}.`)}function Bg(s,e,t,n,i,r,o){let a=e.has("WEBGL_multisampled_render_to_texture")?e.get("WEBGL_multisampled_render_to_texture"):null,c=typeof navigator>"u"?!1:/OculusBrowser/g.test(navigator.userAgent),l=new le,u=new WeakMap,h,f=new WeakMap,p=!1;try{p=typeof OffscreenCanvas<"u"&&new OffscreenCanvas(1,1).getContext("2d")!==null}catch{}function g(R,S){return p?new OffscreenCanvas(R,S):Zs("canvas")}function v(R,S,W){let te=1,se=Ie(R);if((se.width>W||se.height>W)&&(te=W/Math.max(se.width,se.height)),te<1)if(typeof HTMLImageElement<"u"&&R instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&R instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&R instanceof ImageBitmap||typeof VideoFrame<"u"&&R instanceof VideoFrame){let Q=Math.floor(te*se.width),Te=Math.floor(te*se.height);h===void 0&&(h=g(Q,Te));let de=S?g(Q,Te):h;return de.width=Q,de.height=Te,de.getContext("2d").drawImage(R,0,0,Q,Te),console.warn("THREE.WebGLRenderer: Texture has been resized from ("+se.width+"x"+se.height+") to ("+Q+"x"+Te+")."),de}else return"data"in R&&console.warn("THREE.WebGLRenderer: Image in DataTexture is too big ("+se.width+"x"+se.height+")."),R;return R}function m(R){return R.generateMipmaps}function d(R){s.generateMipmap(R)}function M(R){return R.isWebGLCubeRenderTarget?s.TEXTURE_CUBE_MAP:R.isWebGL3DRenderTarget?s.TEXTURE_3D:R.isWebGLArrayRenderTarget||R.isCompressedArrayTexture?s.TEXTURE_2D_ARRAY:s.TEXTURE_2D}function b(R,S,W,te,se=!1){if(R!==null){if(s[R]!==void 0)return s[R];console.warn("THREE.WebGLRenderer: Attempt to use non-existing WebGL internal format '"+R+"'")}let Q=S;if(S===s.RED&&(W===s.FLOAT&&(Q=s.R32F),W===s.HALF_FLOAT&&(Q=s.R16F),W===s.UNSIGNED_BYTE&&(Q=s.R8)),S===s.RED_INTEGER&&(W===s.UNSIGNED_BYTE&&(Q=s.R8UI),W===s.UNSIGNED_SHORT&&(Q=s.R16UI),W===s.UNSIGNED_INT&&(Q=s.R32UI),W===s.BYTE&&(Q=s.R8I),W===s.SHORT&&(Q=s.R16I),W===s.INT&&(Q=s.R32I)),S===s.RG&&(W===s.FLOAT&&(Q=s.RG32F),W===s.HALF_FLOAT&&(Q=s.RG16F),W===s.UNSIGNED_BYTE&&(Q=s.RG8)),S===s.RG_INTEGER&&(W===s.UNSIGNED_BYTE&&(Q=s.RG8UI),W===s.UNSIGNED_SHORT&&(Q=s.RG16UI),W===s.UNSIGNED_INT&&(Q=s.RG32UI),W===s.BYTE&&(Q=s.RG8I),W===s.SHORT&&(Q=s.RG16I),W===s.INT&&(Q=s.RG32I)),S===s.RGB_INTEGER&&(W===s.UNSIGNED_BYTE&&(Q=s.RGB8UI),W===s.UNSIGNED_SHORT&&(Q=s.RGB16UI),W===s.UNSIGNED_INT&&(Q=s.RGB32UI),W===s.BYTE&&(Q=s.RGB8I),W===s.SHORT&&(Q=s.RGB16I),W===s.INT&&(Q=s.RGB32I)),S===s.RGBA_INTEGER&&(W===s.UNSIGNED_BYTE&&(Q=s.RGBA8UI),W===s.UNSIGNED_SHORT&&(Q=s.RGBA16UI),W===s.UNSIGNED_INT&&(Q=s.RGBA32UI),W===s.BYTE&&(Q=s.RGBA8I),W===s.SHORT&&(Q=s.RGBA16I),W===s.INT&&(Q=s.RGBA32I)),S===s.RGB&&W===s.UNSIGNED_INT_5_9_9_9_REV&&(Q=s.RGB9_E5),S===s.RGBA){let Te=se?go:Ye.getTransfer(te);W===s.FLOAT&&(Q=s.RGBA32F),W===s.HALF_FLOAT&&(Q=s.RGBA16F),W===s.UNSIGNED_BYTE&&(Q=Te===lt?s.SRGB8_ALPHA8:s.RGBA8),W===s.UNSIGNED_SHORT_4_4_4_4&&(Q=s.RGBA4),W===s.UNSIGNED_SHORT_5_5_5_1&&(Q=s.RGB5_A1)}return(Q===s.R16F||Q===s.R32F||Q===s.RG16F||Q===s.RG32F||Q===s.RGBA16F||Q===s.RGBA32F)&&e.get("EXT_color_buffer_float"),Q}function _(R,S){let W;return R?S===null||S===Yn||S===as?W=s.DEPTH24_STENCIL8:S===Tn?W=s.DEPTH32F_STENCIL8:S===$s&&(W=s.DEPTH24_STENCIL8,console.warn("DepthTexture: 16 bit depth attachment is not supported with stencil. Using 24-bit attachment.")):S===null||S===Yn||S===as?W=s.DEPTH_COMPONENT24:S===Tn?W=s.DEPTH_COMPONENT32F:S===$s&&(W=s.DEPTH_COMPONENT16),W}function C(R,S){return m(R)===!0||R.isFramebufferTexture&&R.minFilter!==yt&&R.minFilter!==wt?Math.log2(Math.max(S.width,S.height))+1:R.mipmaps!==void 0&&R.mipmaps.length>0?R.mipmaps.length:R.isCompressedTexture&&Array.isArray(R.image)?S.mipmaps.length:1}function A(R){let S=R.target;S.removeEventListener("dispose",A),I(S),S.isVideoTexture&&u.delete(S)}function E(R){let S=R.target;S.removeEventListener("dispose",E),y(S)}function I(R){let S=n.get(R);if(S.__webglInit===void 0)return;let W=R.source,te=f.get(W);if(te){let se=te[S.__cacheKey];se.usedTimes--,se.usedTimes===0&&x(R),Object.keys(te).length===0&&f.delete(W)}n.remove(R)}function x(R){let S=n.get(R);s.deleteTexture(S.__webglTexture);let W=R.source,te=f.get(W);delete te[S.__cacheKey],o.memory.textures--}function y(R){let S=n.get(R);if(R.depthTexture&&(R.depthTexture.dispose(),n.remove(R.depthTexture)),R.isWebGLCubeRenderTarget)for(let te=0;te<6;te++){if(Array.isArray(S.__webglFramebuffer[te]))for(let se=0;se<S.__webglFramebuffer[te].length;se++)s.deleteFramebuffer(S.__webglFramebuffer[te][se]);else s.deleteFramebuffer(S.__webglFramebuffer[te]);S.__webglDepthbuffer&&s.deleteRenderbuffer(S.__webglDepthbuffer[te])}else{if(Array.isArray(S.__webglFramebuffer))for(let te=0;te<S.__webglFramebuffer.length;te++)s.deleteFramebuffer(S.__webglFramebuffer[te]);else s.deleteFramebuffer(S.__webglFramebuffer);if(S.__webglDepthbuffer&&s.deleteRenderbuffer(S.__webglDepthbuffer),S.__webglMultisampledFramebuffer&&s.deleteFramebuffer(S.__webglMultisampledFramebuffer),S.__webglColorRenderbuffer)for(let te=0;te<S.__webglColorRenderbuffer.length;te++)S.__webglColorRenderbuffer[te]&&s.deleteRenderbuffer(S.__webglColorRenderbuffer[te]);S.__webglDepthRenderbuffer&&s.deleteRenderbuffer(S.__webglDepthRenderbuffer)}let W=R.textures;for(let te=0,se=W.length;te<se;te++){let Q=n.get(W[te]);Q.__webglTexture&&(s.deleteTexture(Q.__webglTexture),o.memory.textures--),n.remove(W[te])}n.remove(R)}let T=0;function L(){T=0}function D(){let R=T;return R>=i.maxTextures&&console.warn("THREE.WebGLTextures: Trying to use "+R+" texture units while this GPU supports only "+i.maxTextures),T+=1,R}function F(R){let S=[];return S.push(R.wrapS),S.push(R.wrapT),S.push(R.wrapR||0),S.push(R.magFilter),S.push(R.minFilter),S.push(R.anisotropy),S.push(R.internalFormat),S.push(R.format),S.push(R.type),S.push(R.generateMipmaps),S.push(R.premultiplyAlpha),S.push(R.flipY),S.push(R.unpackAlignment),S.push(R.colorSpace),S.join()}function X(R,S){let W=n.get(R);if(R.isVideoTexture&&Re(R),R.isRenderTargetTexture===!1&&R.version>0&&W.__version!==R.version){let te=R.image;if(te===null)console.warn("THREE.WebGLRenderer: Texture marked for update but no image data found.");else if(te.complete===!1)console.warn("THREE.WebGLRenderer: Texture marked for update but image is incomplete");else{G(W,R,S);return}}t.bindTexture(s.TEXTURE_2D,W.__webglTexture,s.TEXTURE0+S)}function z(R,S){let W=n.get(R);if(R.version>0&&W.__version!==R.version){G(W,R,S);return}t.bindTexture(s.TEXTURE_2D_ARRAY,W.__webglTexture,s.TEXTURE0+S)}function K(R,S){let W=n.get(R);if(R.version>0&&W.__version!==R.version){G(W,R,S);return}t.bindTexture(s.TEXTURE_3D,W.__webglTexture,s.TEXTURE0+S)}function H(R,S){let W=n.get(R);if(R.version>0&&W.__version!==R.version){J(W,R,S);return}t.bindTexture(s.TEXTURE_CUBE_MAP,W.__webglTexture,s.TEXTURE0+S)}let k={[qn]:s.REPEAT,[En]:s.CLAMP_TO_EDGE,[Ys]:s.MIRRORED_REPEAT},$={[yt]:s.NEAREST,[xc]:s.NEAREST_MIPMAP_NEAREST,[Ji]:s.NEAREST_MIPMAP_LINEAR,[wt]:s.LINEAR,[Gs]:s.LINEAR_MIPMAP_NEAREST,[Pn]:s.LINEAR_MIPMAP_LINEAR},ie={[Tf]:s.NEVER,[Lf]:s.ALWAYS,[Af]:s.LESS,[ah]:s.LEQUAL,[Rf]:s.EQUAL,[Pf]:s.GEQUAL,[Cf]:s.GREATER,[If]:s.NOTEQUAL};function j(R,S){if(S.type===Tn&&e.has("OES_texture_float_linear")===!1&&(S.magFilter===wt||S.magFilter===Gs||S.magFilter===Ji||S.magFilter===Pn||S.minFilter===wt||S.minFilter===Gs||S.minFilter===Ji||S.minFilter===Pn)&&console.warn("THREE.WebGLRenderer: Unable to use linear filtering with floating point textures. OES_texture_float_linear not supported on this device."),s.texParameteri(R,s.TEXTURE_WRAP_S,k[S.wrapS]),s.texParameteri(R,s.TEXTURE_WRAP_T,k[S.wrapT]),(R===s.TEXTURE_3D||R===s.TEXTURE_2D_ARRAY)&&s.texParameteri(R,s.TEXTURE_WRAP_R,k[S.wrapR]),s.texParameteri(R,s.TEXTURE_MAG_FILTER,$[S.magFilter]),s.texParameteri(R,s.TEXTURE_MIN_FILTER,$[S.minFilter]),S.compareFunction&&(s.texParameteri(R,s.TEXTURE_COMPARE_MODE,s.COMPARE_REF_TO_TEXTURE),s.texParameteri(R,s.TEXTURE_COMPARE_FUNC,ie[S.compareFunction])),e.has("EXT_texture_filter_anisotropic")===!0){if(S.magFilter===yt||S.minFilter!==Ji&&S.minFilter!==Pn||S.type===Tn&&e.has("OES_texture_float_linear")===!1)return;if(S.anisotropy>1||n.get(S).__currentAnisotropy){let W=e.get("EXT_texture_filter_anisotropic");s.texParameterf(R,W.TEXTURE_MAX_ANISOTROPY_EXT,Math.min(S.anisotropy,i.getMaxAnisotropy())),n.get(S).__currentAnisotropy=S.anisotropy}}}function ue(R,S){let W=!1;R.__webglInit===void 0&&(R.__webglInit=!0,S.addEventListener("dispose",A));let te=S.source,se=f.get(te);se===void 0&&(se={},f.set(te,se));let Q=F(S);if(Q!==R.__cacheKey){se[Q]===void 0&&(se[Q]={texture:s.createTexture(),usedTimes:0},o.memory.textures++,W=!0),se[Q].usedTimes++;let Te=se[R.__cacheKey];Te!==void 0&&(se[R.__cacheKey].usedTimes--,Te.usedTimes===0&&x(S)),R.__cacheKey=Q,R.__webglTexture=se[Q].texture}return W}function G(R,S,W){let te=s.TEXTURE_2D;(S.isDataArrayTexture||S.isCompressedArrayTexture)&&(te=s.TEXTURE_2D_ARRAY),S.isData3DTexture&&(te=s.TEXTURE_3D);let se=ue(R,S),Q=S.source;t.bindTexture(te,R.__webglTexture,s.TEXTURE0+W);let Te=n.get(Q);if(Q.version!==Te.__version||se===!0){t.activeTexture(s.TEXTURE0+W);let de=Ye.getPrimaries(Ye.workingColorSpace),_e=S.colorSpace===fn?null:Ye.getPrimaries(S.colorSpace),et=S.colorSpace===fn||de===_e?s.NONE:s.BROWSER_DEFAULT_WEBGL;s.pixelStorei(s.UNPACK_FLIP_Y_WEBGL,S.flipY),s.pixelStorei(s.UNPACK_PREMULTIPLY_ALPHA_WEBGL,S.premultiplyAlpha),s.pixelStorei(s.UNPACK_ALIGNMENT,S.unpackAlignment),s.pixelStorei(s.UNPACK_COLORSPACE_CONVERSION_WEBGL,et);let ae=v(S.image,!1,i.maxTextureSize);ae=ut(S,ae);let Me=r.convert(S.format,S.colorSpace),Pe=r.convert(S.type),Ue=b(S.internalFormat,Me,Pe,S.colorSpace,S.isVideoTexture);j(te,S);let be,Ke=S.mipmaps,He=S.isVideoTexture!==!0,ht=Te.__version===void 0||se===!0,U=Q.dataReady,fe=C(S,ae);if(S.isDepthTexture)Ue=_(S.format===cs,S.type),ht&&(He?t.texStorage2D(s.TEXTURE_2D,1,Ue,ae.width,ae.height):t.texImage2D(s.TEXTURE_2D,0,Ue,ae.width,ae.height,0,Me,Pe,null));else if(S.isDataTexture)if(Ke.length>0){He&&ht&&t.texStorage2D(s.TEXTURE_2D,fe,Ue,Ke[0].width,Ke[0].height);for(let Z=0,ne=Ke.length;Z<ne;Z++)be=Ke[Z],He?U&&t.texSubImage2D(s.TEXTURE_2D,Z,0,0,be.width,be.height,Me,Pe,be.data):t.texImage2D(s.TEXTURE_2D,Z,Ue,be.width,be.height,0,Me,Pe,be.data);S.generateMipmaps=!1}else He?(ht&&t.texStorage2D(s.TEXTURE_2D,fe,Ue,ae.width,ae.height),U&&t.texSubImage2D(s.TEXTURE_2D,0,0,0,ae.width,ae.height,Me,Pe,ae.data)):t.texImage2D(s.TEXTURE_2D,0,Ue,ae.width,ae.height,0,Me,Pe,ae.data);else if(S.isCompressedTexture)if(S.isCompressedArrayTexture){He&&ht&&t.texStorage3D(s.TEXTURE_2D_ARRAY,fe,Ue,Ke[0].width,Ke[0].height,ae.depth);for(let Z=0,ne=Ke.length;Z<ne;Z++)if(be=Ke[Z],S.format!==Ht)if(Me!==null)if(He){if(U)if(S.layerUpdates.size>0){let ge=Ru(be.width,be.height,S.format,S.type);for(let pe of S.layerUpdates){let Be=be.data.subarray(pe*ge/be.data.BYTES_PER_ELEMENT,(pe+1)*ge/be.data.BYTES_PER_ELEMENT);t.compressedTexSubImage3D(s.TEXTURE_2D_ARRAY,Z,0,0,pe,be.width,be.height,1,Me,Be)}S.clearLayerUpdates()}else t.compressedTexSubImage3D(s.TEXTURE_2D_ARRAY,Z,0,0,0,be.width,be.height,ae.depth,Me,be.data)}else t.compressedTexImage3D(s.TEXTURE_2D_ARRAY,Z,Ue,be.width,be.height,ae.depth,0,be.data,0,0);else console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()");else He?U&&t.texSubImage3D(s.TEXTURE_2D_ARRAY,Z,0,0,0,be.width,be.height,ae.depth,Me,Pe,be.data):t.texImage3D(s.TEXTURE_2D_ARRAY,Z,Ue,be.width,be.height,ae.depth,0,Me,Pe,be.data)}else{He&&ht&&t.texStorage2D(s.TEXTURE_2D,fe,Ue,Ke[0].width,Ke[0].height);for(let Z=0,ne=Ke.length;Z<ne;Z++)be=Ke[Z],S.format!==Ht?Me!==null?He?U&&t.compressedTexSubImage2D(s.TEXTURE_2D,Z,0,0,be.width,be.height,Me,be.data):t.compressedTexImage2D(s.TEXTURE_2D,Z,Ue,be.width,be.height,0,be.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):He?U&&t.texSubImage2D(s.TEXTURE_2D,Z,0,0,be.width,be.height,Me,Pe,be.data):t.texImage2D(s.TEXTURE_2D,Z,Ue,be.width,be.height,0,Me,Pe,be.data)}else if(S.isDataArrayTexture)if(He){if(ht&&t.texStorage3D(s.TEXTURE_2D_ARRAY,fe,Ue,ae.width,ae.height,ae.depth),U)if(S.layerUpdates.size>0){let Z=Ru(ae.width,ae.height,S.format,S.type);for(let ne of S.layerUpdates){let ge=ae.data.subarray(ne*Z/ae.data.BYTES_PER_ELEMENT,(ne+1)*Z/ae.data.BYTES_PER_ELEMENT);t.texSubImage3D(s.TEXTURE_2D_ARRAY,0,0,0,ne,ae.width,ae.height,1,Me,Pe,ge)}S.clearLayerUpdates()}else t.texSubImage3D(s.TEXTURE_2D_ARRAY,0,0,0,0,ae.width,ae.height,ae.depth,Me,Pe,ae.data)}else t.texImage3D(s.TEXTURE_2D_ARRAY,0,Ue,ae.width,ae.height,ae.depth,0,Me,Pe,ae.data);else if(S.isData3DTexture)He?(ht&&t.texStorage3D(s.TEXTURE_3D,fe,Ue,ae.width,ae.height,ae.depth),U&&t.texSubImage3D(s.TEXTURE_3D,0,0,0,0,ae.width,ae.height,ae.depth,Me,Pe,ae.data)):t.texImage3D(s.TEXTURE_3D,0,Ue,ae.width,ae.height,ae.depth,0,Me,Pe,ae.data);else if(S.isFramebufferTexture){if(ht)if(He)t.texStorage2D(s.TEXTURE_2D,fe,Ue,ae.width,ae.height);else{let Z=ae.width,ne=ae.height;for(let ge=0;ge<fe;ge++)t.texImage2D(s.TEXTURE_2D,ge,Ue,Z,ne,0,Me,Pe,null),Z>>=1,ne>>=1}}else if(Ke.length>0){if(He&&ht){let Z=Ie(Ke[0]);t.texStorage2D(s.TEXTURE_2D,fe,Ue,Z.width,Z.height)}for(let Z=0,ne=Ke.length;Z<ne;Z++)be=Ke[Z],He?U&&t.texSubImage2D(s.TEXTURE_2D,Z,0,0,Me,Pe,be):t.texImage2D(s.TEXTURE_2D,Z,Ue,Me,Pe,be);S.generateMipmaps=!1}else if(He){if(ht){let Z=Ie(ae);t.texStorage2D(s.TEXTURE_2D,fe,Ue,Z.width,Z.height)}U&&t.texSubImage2D(s.TEXTURE_2D,0,0,0,Me,Pe,ae)}else t.texImage2D(s.TEXTURE_2D,0,Ue,Me,Pe,ae);m(S)&&d(te),Te.__version=Q.version,S.onUpdate&&S.onUpdate(S)}R.__version=S.version}function J(R,S,W){if(S.image.length!==6)return;let te=ue(R,S),se=S.source;t.bindTexture(s.TEXTURE_CUBE_MAP,R.__webglTexture,s.TEXTURE0+W);let Q=n.get(se);if(se.version!==Q.__version||te===!0){t.activeTexture(s.TEXTURE0+W);let Te=Ye.getPrimaries(Ye.workingColorSpace),de=S.colorSpace===fn?null:Ye.getPrimaries(S.colorSpace),_e=S.colorSpace===fn||Te===de?s.NONE:s.BROWSER_DEFAULT_WEBGL;s.pixelStorei(s.UNPACK_FLIP_Y_WEBGL,S.flipY),s.pixelStorei(s.UNPACK_PREMULTIPLY_ALPHA_WEBGL,S.premultiplyAlpha),s.pixelStorei(s.UNPACK_ALIGNMENT,S.unpackAlignment),s.pixelStorei(s.UNPACK_COLORSPACE_CONVERSION_WEBGL,_e);let et=S.isCompressedTexture||S.image[0].isCompressedTexture,ae=S.image[0]&&S.image[0].isDataTexture,Me=[];for(let ne=0;ne<6;ne++)!et&&!ae?Me[ne]=v(S.image[ne],!0,i.maxCubemapSize):Me[ne]=ae?S.image[ne].image:S.image[ne],Me[ne]=ut(S,Me[ne]);let Pe=Me[0],Ue=r.convert(S.format,S.colorSpace),be=r.convert(S.type),Ke=b(S.internalFormat,Ue,be,S.colorSpace),He=S.isVideoTexture!==!0,ht=Q.__version===void 0||te===!0,U=se.dataReady,fe=C(S,Pe);j(s.TEXTURE_CUBE_MAP,S);let Z;if(et){He&&ht&&t.texStorage2D(s.TEXTURE_CUBE_MAP,fe,Ke,Pe.width,Pe.height);for(let ne=0;ne<6;ne++){Z=Me[ne].mipmaps;for(let ge=0;ge<Z.length;ge++){let pe=Z[ge];S.format!==Ht?Ue!==null?He?U&&t.compressedTexSubImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,ge,0,0,pe.width,pe.height,Ue,pe.data):t.compressedTexImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,ge,Ke,pe.width,pe.height,0,pe.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .setTextureCube()"):He?U&&t.texSubImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,ge,0,0,pe.width,pe.height,Ue,be,pe.data):t.texImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,ge,Ke,pe.width,pe.height,0,Ue,be,pe.data)}}}else{if(Z=S.mipmaps,He&&ht){Z.length>0&&fe++;let ne=Ie(Me[0]);t.texStorage2D(s.TEXTURE_CUBE_MAP,fe,Ke,ne.width,ne.height)}for(let ne=0;ne<6;ne++)if(ae){He?U&&t.texSubImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,0,0,0,Me[ne].width,Me[ne].height,Ue,be,Me[ne].data):t.texImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,0,Ke,Me[ne].width,Me[ne].height,0,Ue,be,Me[ne].data);for(let ge=0;ge<Z.length;ge++){let Be=Z[ge].image[ne].image;He?U&&t.texSubImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,ge+1,0,0,Be.width,Be.height,Ue,be,Be.data):t.texImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,ge+1,Ke,Be.width,Be.height,0,Ue,be,Be.data)}}else{He?U&&t.texSubImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,0,0,0,Ue,be,Me[ne]):t.texImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,0,Ke,Ue,be,Me[ne]);for(let ge=0;ge<Z.length;ge++){let pe=Z[ge];He?U&&t.texSubImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,ge+1,0,0,Ue,be,pe.image[ne]):t.texImage2D(s.TEXTURE_CUBE_MAP_POSITIVE_X+ne,ge+1,Ke,Ue,be,pe.image[ne])}}}m(S)&&d(s.TEXTURE_CUBE_MAP),Q.__version=se.version,S.onUpdate&&S.onUpdate(S)}R.__version=S.version}function re(R,S,W,te,se,Q){let Te=r.convert(W.format,W.colorSpace),de=r.convert(W.type),_e=b(W.internalFormat,Te,de,W.colorSpace),et=n.get(S),ae=n.get(W);if(ae.__renderTarget=S,!et.__hasExternalTextures){let Me=Math.max(1,S.width>>Q),Pe=Math.max(1,S.height>>Q);se===s.TEXTURE_3D||se===s.TEXTURE_2D_ARRAY?t.texImage3D(se,Q,_e,Me,Pe,S.depth,0,Te,de,null):t.texImage2D(se,Q,_e,Me,Pe,0,Te,de,null)}t.bindFramebuffer(s.FRAMEBUFFER,R),Oe(S)?a.framebufferTexture2DMultisampleEXT(s.FRAMEBUFFER,te,se,ae.__webglTexture,0,Ge(S)):(se===s.TEXTURE_2D||se>=s.TEXTURE_CUBE_MAP_POSITIVE_X&&se<=s.TEXTURE_CUBE_MAP_NEGATIVE_Z)&&s.framebufferTexture2D(s.FRAMEBUFFER,te,se,ae.__webglTexture,Q),t.bindFramebuffer(s.FRAMEBUFFER,null)}function ee(R,S,W){if(s.bindRenderbuffer(s.RENDERBUFFER,R),S.depthBuffer){let te=S.depthTexture,se=te&&te.isDepthTexture?te.type:null,Q=_(S.stencilBuffer,se),Te=S.stencilBuffer?s.DEPTH_STENCIL_ATTACHMENT:s.DEPTH_ATTACHMENT,de=Ge(S);Oe(S)?a.renderbufferStorageMultisampleEXT(s.RENDERBUFFER,de,Q,S.width,S.height):W?s.renderbufferStorageMultisample(s.RENDERBUFFER,de,Q,S.width,S.height):s.renderbufferStorage(s.RENDERBUFFER,Q,S.width,S.height),s.framebufferRenderbuffer(s.FRAMEBUFFER,Te,s.RENDERBUFFER,R)}else{let te=S.textures;for(let se=0;se<te.length;se++){let Q=te[se],Te=r.convert(Q.format,Q.colorSpace),de=r.convert(Q.type),_e=b(Q.internalFormat,Te,de,Q.colorSpace),et=Ge(S);W&&Oe(S)===!1?s.renderbufferStorageMultisample(s.RENDERBUFFER,et,_e,S.width,S.height):Oe(S)?a.renderbufferStorageMultisampleEXT(s.RENDERBUFFER,et,_e,S.width,S.height):s.renderbufferStorage(s.RENDERBUFFER,_e,S.width,S.height)}}s.bindRenderbuffer(s.RENDERBUFFER,null)}function oe(R,S){if(S&&S.isWebGLCubeRenderTarget)throw new Error("Depth Texture with cube render targets is not supported");if(t.bindFramebuffer(s.FRAMEBUFFER,R),!(S.depthTexture&&S.depthTexture.isDepthTexture))throw new Error("renderTarget.depthTexture must be an instance of THREE.DepthTexture");let te=n.get(S.depthTexture);te.__renderTarget=S,(!te.__webglTexture||S.depthTexture.image.width!==S.width||S.depthTexture.image.height!==S.height)&&(S.depthTexture.image.width=S.width,S.depthTexture.image.height=S.height,S.depthTexture.needsUpdate=!0),X(S.depthTexture,0);let se=te.__webglTexture,Q=Ge(S);if(S.depthTexture.format===es)Oe(S)?a.framebufferTexture2DMultisampleEXT(s.FRAMEBUFFER,s.DEPTH_ATTACHMENT,s.TEXTURE_2D,se,0,Q):s.framebufferTexture2D(s.FRAMEBUFFER,s.DEPTH_ATTACHMENT,s.TEXTURE_2D,se,0);else if(S.depthTexture.format===cs)Oe(S)?a.framebufferTexture2DMultisampleEXT(s.FRAMEBUFFER,s.DEPTH_STENCIL_ATTACHMENT,s.TEXTURE_2D,se,0,Q):s.framebufferTexture2D(s.FRAMEBUFFER,s.DEPTH_STENCIL_ATTACHMENT,s.TEXTURE_2D,se,0);else throw new Error("Unknown depthTexture format")}function ye(R){let S=n.get(R),W=R.isWebGLCubeRenderTarget===!0;if(S.__boundDepthTexture!==R.depthTexture){let te=R.depthTexture;if(S.__depthDisposeCallback&&S.__depthDisposeCallback(),te){let se=()=>{delete S.__boundDepthTexture,delete S.__depthDisposeCallback,te.removeEventListener("dispose",se)};te.addEventListener("dispose",se),S.__depthDisposeCallback=se}S.__boundDepthTexture=te}if(R.depthTexture&&!S.__autoAllocateDepthBuffer){if(W)throw new Error("target.depthTexture not supported in Cube render targets");oe(S.__webglFramebuffer,R)}else if(W){S.__webglDepthbuffer=[];for(let te=0;te<6;te++)if(t.bindFramebuffer(s.FRAMEBUFFER,S.__webglFramebuffer[te]),S.__webglDepthbuffer[te]===void 0)S.__webglDepthbuffer[te]=s.createRenderbuffer(),ee(S.__webglDepthbuffer[te],R,!1);else{let se=R.stencilBuffer?s.DEPTH_STENCIL_ATTACHMENT:s.DEPTH_ATTACHMENT,Q=S.__webglDepthbuffer[te];s.bindRenderbuffer(s.RENDERBUFFER,Q),s.framebufferRenderbuffer(s.FRAMEBUFFER,se,s.RENDERBUFFER,Q)}}else if(t.bindFramebuffer(s.FRAMEBUFFER,S.__webglFramebuffer),S.__webglDepthbuffer===void 0)S.__webglDepthbuffer=s.createRenderbuffer(),ee(S.__webglDepthbuffer,R,!1);else{let te=R.stencilBuffer?s.DEPTH_STENCIL_ATTACHMENT:s.DEPTH_ATTACHMENT,se=S.__webglDepthbuffer;s.bindRenderbuffer(s.RENDERBUFFER,se),s.framebufferRenderbuffer(s.FRAMEBUFFER,te,s.RENDERBUFFER,se)}t.bindFramebuffer(s.FRAMEBUFFER,null)}function De(R,S,W){let te=n.get(R);S!==void 0&&re(te.__webglFramebuffer,R,R.texture,s.COLOR_ATTACHMENT0,s.TEXTURE_2D,0),W!==void 0&&ye(R)}function Qe(R){let S=R.texture,W=n.get(R),te=n.get(S);R.addEventListener("dispose",E);let se=R.textures,Q=R.isWebGLCubeRenderTarget===!0,Te=se.length>1;if(Te||(te.__webglTexture===void 0&&(te.__webglTexture=s.createTexture()),te.__version=S.version,o.memory.textures++),Q){W.__webglFramebuffer=[];for(let de=0;de<6;de++)if(S.mipmaps&&S.mipmaps.length>0){W.__webglFramebuffer[de]=[];for(let _e=0;_e<S.mipmaps.length;_e++)W.__webglFramebuffer[de][_e]=s.createFramebuffer()}else W.__webglFramebuffer[de]=s.createFramebuffer()}else{if(S.mipmaps&&S.mipmaps.length>0){W.__webglFramebuffer=[];for(let de=0;de<S.mipmaps.length;de++)W.__webglFramebuffer[de]=s.createFramebuffer()}else W.__webglFramebuffer=s.createFramebuffer();if(Te)for(let de=0,_e=se.length;de<_e;de++){let et=n.get(se[de]);et.__webglTexture===void 0&&(et.__webglTexture=s.createTexture(),o.memory.textures++)}if(R.samples>0&&Oe(R)===!1){W.__webglMultisampledFramebuffer=s.createFramebuffer(),W.__webglColorRenderbuffer=[],t.bindFramebuffer(s.FRAMEBUFFER,W.__webglMultisampledFramebuffer);for(let de=0;de<se.length;de++){let _e=se[de];W.__webglColorRenderbuffer[de]=s.createRenderbuffer(),s.bindRenderbuffer(s.RENDERBUFFER,W.__webglColorRenderbuffer[de]);let et=r.convert(_e.format,_e.colorSpace),ae=r.convert(_e.type),Me=b(_e.internalFormat,et,ae,_e.colorSpace,R.isXRRenderTarget===!0),Pe=Ge(R);s.renderbufferStorageMultisample(s.RENDERBUFFER,Pe,Me,R.width,R.height),s.framebufferRenderbuffer(s.FRAMEBUFFER,s.COLOR_ATTACHMENT0+de,s.RENDERBUFFER,W.__webglColorRenderbuffer[de])}s.bindRenderbuffer(s.RENDERBUFFER,null),R.depthBuffer&&(W.__webglDepthRenderbuffer=s.createRenderbuffer(),ee(W.__webglDepthRenderbuffer,R,!0)),t.bindFramebuffer(s.FRAMEBUFFER,null)}}if(Q){t.bindTexture(s.TEXTURE_CUBE_MAP,te.__webglTexture),j(s.TEXTURE_CUBE_MAP,S);for(let de=0;de<6;de++)if(S.mipmaps&&S.mipmaps.length>0)for(let _e=0;_e<S.mipmaps.length;_e++)re(W.__webglFramebuffer[de][_e],R,S,s.COLOR_ATTACHMENT0,s.TEXTURE_CUBE_MAP_POSITIVE_X+de,_e);else re(W.__webglFramebuffer[de],R,S,s.COLOR_ATTACHMENT0,s.TEXTURE_CUBE_MAP_POSITIVE_X+de,0);m(S)&&d(s.TEXTURE_CUBE_MAP),t.unbindTexture()}else if(Te){for(let de=0,_e=se.length;de<_e;de++){let et=se[de],ae=n.get(et);t.bindTexture(s.TEXTURE_2D,ae.__webglTexture),j(s.TEXTURE_2D,et),re(W.__webglFramebuffer,R,et,s.COLOR_ATTACHMENT0+de,s.TEXTURE_2D,0),m(et)&&d(s.TEXTURE_2D)}t.unbindTexture()}else{let de=s.TEXTURE_2D;if((R.isWebGL3DRenderTarget||R.isWebGLArrayRenderTarget)&&(de=R.isWebGL3DRenderTarget?s.TEXTURE_3D:s.TEXTURE_2D_ARRAY),t.bindTexture(de,te.__webglTexture),j(de,S),S.mipmaps&&S.mipmaps.length>0)for(let _e=0;_e<S.mipmaps.length;_e++)re(W.__webglFramebuffer[_e],R,S,s.COLOR_ATTACHMENT0,de,_e);else re(W.__webglFramebuffer,R,S,s.COLOR_ATTACHMENT0,de,0);m(S)&&d(de),t.unbindTexture()}R.depthBuffer&&ye(R)}function Ce(R){let S=R.textures;for(let W=0,te=S.length;W<te;W++){let se=S[W];if(m(se)){let Q=M(R),Te=n.get(se).__webglTexture;t.bindTexture(Q,Te),d(Q),t.unbindTexture()}}}let qe=[],N=[];function Ft(R){if(R.samples>0){if(Oe(R)===!1){let S=R.textures,W=R.width,te=R.height,se=s.COLOR_BUFFER_BIT,Q=R.stencilBuffer?s.DEPTH_STENCIL_ATTACHMENT:s.DEPTH_ATTACHMENT,Te=n.get(R),de=S.length>1;if(de)for(let _e=0;_e<S.length;_e++)t.bindFramebuffer(s.FRAMEBUFFER,Te.__webglMultisampledFramebuffer),s.framebufferRenderbuffer(s.FRAMEBUFFER,s.COLOR_ATTACHMENT0+_e,s.RENDERBUFFER,null),t.bindFramebuffer(s.FRAMEBUFFER,Te.__webglFramebuffer),s.framebufferTexture2D(s.DRAW_FRAMEBUFFER,s.COLOR_ATTACHMENT0+_e,s.TEXTURE_2D,null,0);t.bindFramebuffer(s.READ_FRAMEBUFFER,Te.__webglMultisampledFramebuffer),t.bindFramebuffer(s.DRAW_FRAMEBUFFER,Te.__webglFramebuffer);for(let _e=0;_e<S.length;_e++){if(R.resolveDepthBuffer&&(R.depthBuffer&&(se|=s.DEPTH_BUFFER_BIT),R.stencilBuffer&&R.resolveStencilBuffer&&(se|=s.STENCIL_BUFFER_BIT)),de){s.framebufferRenderbuffer(s.READ_FRAMEBUFFER,s.COLOR_ATTACHMENT0,s.RENDERBUFFER,Te.__webglColorRenderbuffer[_e]);let et=n.get(S[_e]).__webglTexture;s.framebufferTexture2D(s.DRAW_FRAMEBUFFER,s.COLOR_ATTACHMENT0,s.TEXTURE_2D,et,0)}s.blitFramebuffer(0,0,W,te,0,0,W,te,se,s.NEAREST),c===!0&&(qe.length=0,N.length=0,qe.push(s.COLOR_ATTACHMENT0+_e),R.depthBuffer&&R.resolveDepthBuffer===!1&&(qe.push(Q),N.push(Q),s.invalidateFramebuffer(s.DRAW_FRAMEBUFFER,N)),s.invalidateFramebuffer(s.READ_FRAMEBUFFER,qe))}if(t.bindFramebuffer(s.READ_FRAMEBUFFER,null),t.bindFramebuffer(s.DRAW_FRAMEBUFFER,null),de)for(let _e=0;_e<S.length;_e++){t.bindFramebuffer(s.FRAMEBUFFER,Te.__webglMultisampledFramebuffer),s.framebufferRenderbuffer(s.FRAMEBUFFER,s.COLOR_ATTACHMENT0+_e,s.RENDERBUFFER,Te.__webglColorRenderbuffer[_e]);let et=n.get(S[_e]).__webglTexture;t.bindFramebuffer(s.FRAMEBUFFER,Te.__webglFramebuffer),s.framebufferTexture2D(s.DRAW_FRAMEBUFFER,s.COLOR_ATTACHMENT0+_e,s.TEXTURE_2D,et,0)}t.bindFramebuffer(s.DRAW_FRAMEBUFFER,Te.__webglMultisampledFramebuffer)}else if(R.depthBuffer&&R.resolveDepthBuffer===!1&&c){let S=R.stencilBuffer?s.DEPTH_STENCIL_ATTACHMENT:s.DEPTH_ATTACHMENT;s.invalidateFramebuffer(s.DRAW_FRAMEBUFFER,[S])}}}function Ge(R){return Math.min(i.maxSamples,R.samples)}function Oe(R){let S=n.get(R);return R.samples>0&&e.has("WEBGL_multisampled_render_to_texture")===!0&&S.__useRenderToTexture!==!1}function Re(R){let S=o.render.frame;u.get(R)!==S&&(u.set(R,S),R.update())}function ut(R,S){let W=R.colorSpace,te=R.format,se=R.type;return R.isCompressedTexture===!0||R.isVideoTexture===!0||W!==Wt&&W!==fn&&(Ye.getTransfer(W)===lt?(te!==Ht||se!==Dt)&&console.warn("THREE.WebGLTextures: sRGB encoded textures have to use RGBAFormat and UnsignedByteType."):console.error("THREE.WebGLTextures: Unsupported texture color space:",W)),S}function Ie(R){return typeof HTMLImageElement<"u"&&R instanceof HTMLImageElement?(l.width=R.naturalWidth||R.width,l.height=R.naturalHeight||R.height):typeof VideoFrame<"u"&&R instanceof VideoFrame?(l.width=R.displayWidth,l.height=R.displayHeight):(l.width=R.width,l.height=R.height),l}this.allocateTextureUnit=D,this.resetTextureUnits=L,this.setTexture2D=X,this.setTexture2DArray=z,this.setTexture3D=K,this.setTextureCube=H,this.rebindTextures=De,this.setupRenderTarget=Qe,this.updateRenderTargetMipmap=Ce,this.updateMultisampleRenderTarget=Ft,this.setupDepthRenderbuffer=ye,this.setupFrameBufferTexture=re,this.useMultisampledRTT=Oe}function zg(s,e){function t(n,i=fn){let r,o=Ye.getTransfer(i);if(n===Dt)return s.UNSIGNED_BYTE;if(n===yc)return s.UNSIGNED_SHORT_4_4_4_4;if(n===Mc)return s.UNSIGNED_SHORT_5_5_5_1;if(n===ju)return s.UNSIGNED_INT_5_9_9_9_REV;if(n===Ku)return s.BYTE;if(n===Ju)return s.SHORT;if(n===$s)return s.UNSIGNED_SHORT;if(n===_c)return s.INT;if(n===Yn)return s.UNSIGNED_INT;if(n===Tn)return s.FLOAT;if(n===$e)return s.HALF_FLOAT;if(n===Qu)return s.ALPHA;if(n===eh)return s.RGB;if(n===Ht)return s.RGBA;if(n===th)return s.LUMINANCE;if(n===nh)return s.LUMINANCE_ALPHA;if(n===es)return s.DEPTH_COMPONENT;if(n===cs)return s.DEPTH_STENCIL;if(n===bc)return s.RED;if(n===Sc)return s.RED_INTEGER;if(n===ih)return s.RG;if(n===wc)return s.RG_INTEGER;if(n===Ec)return s.RGBA_INTEGER;if(n===Hr||n===Vr||n===Gr||n===Wr)if(o===lt)if(r=e.get("WEBGL_compressed_texture_s3tc_srgb"),r!==null){if(n===Hr)return r.COMPRESSED_SRGB_S3TC_DXT1_EXT;if(n===Vr)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT;if(n===Gr)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT;if(n===Wr)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT}else return null;else if(r=e.get("WEBGL_compressed_texture_s3tc"),r!==null){if(n===Hr)return r.COMPRESSED_RGB_S3TC_DXT1_EXT;if(n===Vr)return r.COMPRESSED_RGBA_S3TC_DXT1_EXT;if(n===Gr)return r.COMPRESSED_RGBA_S3TC_DXT3_EXT;if(n===Wr)return r.COMPRESSED_RGBA_S3TC_DXT5_EXT}else return null;if(n===ma||n===ga||n===va||n===xa)if(r=e.get("WEBGL_compressed_texture_pvrtc"),r!==null){if(n===ma)return r.COMPRESSED_RGB_PVRTC_4BPPV1_IMG;if(n===ga)return r.COMPRESSED_RGB_PVRTC_2BPPV1_IMG;if(n===va)return r.COMPRESSED_RGBA_PVRTC_4BPPV1_IMG;if(n===xa)return r.COMPRESSED_RGBA_PVRTC_2BPPV1_IMG}else return null;if(n===_a||n===ya||n===Ma)if(r=e.get("WEBGL_compressed_texture_etc"),r!==null){if(n===_a||n===ya)return o===lt?r.COMPRESSED_SRGB8_ETC2:r.COMPRESSED_RGB8_ETC2;if(n===Ma)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ETC2_EAC:r.COMPRESSED_RGBA8_ETC2_EAC}else return null;if(n===ba||n===Sa||n===wa||n===Ea||n===Ta||n===Aa||n===Ra||n===Ca||n===Ia||n===Pa||n===La||n===Da||n===Ua||n===Na)if(r=e.get("WEBGL_compressed_texture_astc"),r!==null){if(n===ba)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR:r.COMPRESSED_RGBA_ASTC_4x4_KHR;if(n===Sa)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR:r.COMPRESSED_RGBA_ASTC_5x4_KHR;if(n===wa)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR:r.COMPRESSED_RGBA_ASTC_5x5_KHR;if(n===Ea)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR:r.COMPRESSED_RGBA_ASTC_6x5_KHR;if(n===Ta)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR:r.COMPRESSED_RGBA_ASTC_6x6_KHR;if(n===Aa)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR:r.COMPRESSED_RGBA_ASTC_8x5_KHR;if(n===Ra)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR:r.COMPRESSED_RGBA_ASTC_8x6_KHR;if(n===Ca)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR:r.COMPRESSED_RGBA_ASTC_8x8_KHR;if(n===Ia)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR:r.COMPRESSED_RGBA_ASTC_10x5_KHR;if(n===Pa)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR:r.COMPRESSED_RGBA_ASTC_10x6_KHR;if(n===La)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR:r.COMPRESSED_RGBA_ASTC_10x8_KHR;if(n===Da)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR:r.COMPRESSED_RGBA_ASTC_10x10_KHR;if(n===Ua)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR:r.COMPRESSED_RGBA_ASTC_12x10_KHR;if(n===Na)return o===lt?r.COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR:r.COMPRESSED_RGBA_ASTC_12x12_KHR}else return null;if(n===Xr||n===Fa||n===Oa)if(r=e.get("EXT_texture_compression_bptc"),r!==null){if(n===Xr)return o===lt?r.COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT:r.COMPRESSED_RGBA_BPTC_UNORM_EXT;if(n===Fa)return r.COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT;if(n===Oa)return r.COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT}else return null;if(n===sh||n===Ba||n===za||n===ka)if(r=e.get("EXT_texture_compression_rgtc"),r!==null){if(n===Xr)return r.COMPRESSED_RED_RGTC1_EXT;if(n===Ba)return r.COMPRESSED_SIGNED_RED_RGTC1_EXT;if(n===za)return r.COMPRESSED_RED_GREEN_RGTC2_EXT;if(n===ka)return r.COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT}else return null;return n===as?s.UNSIGNED_INT_24_8:s[n]!==void 0?s[n]:null}return{convert:t}}var tc=class extends _t{constructor(e=[]){super(),this.isArrayCamera=!0,this.cameras=e}},Qt=class extends gt{constructor(){super(),this.isGroup=!0,this.type="Group"}},kg={type:"move"},qs=class{constructor(){this._targetRay=null,this._grip=null,this._hand=null}getHandSpace(){return this._hand===null&&(this._hand=new Qt,this._hand.matrixAutoUpdate=!1,this._hand.visible=!1,this._hand.joints={},this._hand.inputState={pinching:!1}),this._hand}getTargetRaySpace(){return this._targetRay===null&&(this._targetRay=new Qt,this._targetRay.matrixAutoUpdate=!1,this._targetRay.visible=!1,this._targetRay.hasLinearVelocity=!1,this._targetRay.linearVelocity=new P,this._targetRay.hasAngularVelocity=!1,this._targetRay.angularVelocity=new P),this._targetRay}getGripSpace(){return this._grip===null&&(this._grip=new Qt,this._grip.matrixAutoUpdate=!1,this._grip.visible=!1,this._grip.hasLinearVelocity=!1,this._grip.linearVelocity=new P,this._grip.hasAngularVelocity=!1,this._grip.angularVelocity=new P),this._grip}dispatchEvent(e){return this._targetRay!==null&&this._targetRay.dispatchEvent(e),this._grip!==null&&this._grip.dispatchEvent(e),this._hand!==null&&this._hand.dispatchEvent(e),this}connect(e){if(e&&e.hand){let t=this._hand;if(t)for(let n of e.hand.values())this._getHandJoint(t,n)}return this.dispatchEvent({type:"connected",data:e}),this}disconnect(e){return this.dispatchEvent({type:"disconnected",data:e}),this._targetRay!==null&&(this._targetRay.visible=!1),this._grip!==null&&(this._grip.visible=!1),this._hand!==null&&(this._hand.visible=!1),this}update(e,t,n){let i=null,r=null,o=null,a=this._targetRay,c=this._grip,l=this._hand;if(e&&t.session.visibilityState!=="visible-blurred"){if(l&&e.hand){o=!0;for(let v of e.hand.values()){let m=t.getJointPose(v,n),d=this._getHandJoint(l,v);m!==null&&(d.matrix.fromArray(m.transform.matrix),d.matrix.decompose(d.position,d.rotation,d.scale),d.matrixWorldNeedsUpdate=!0,d.jointRadius=m.radius),d.visible=m!==null}let u=l.joints["index-finger-tip"],h=l.joints["thumb-tip"],f=u.position.distanceTo(h.position),p=.02,g=.005;l.inputState.pinching&&f>p+g?(l.inputState.pinching=!1,this.dispatchEvent({type:"pinchend",handedness:e.handedness,target:this})):!l.inputState.pinching&&f<=p-g&&(l.inputState.pinching=!0,this.dispatchEvent({type:"pinchstart",handedness:e.handedness,target:this}))}else c!==null&&e.gripSpace&&(r=t.getPose(e.gripSpace,n),r!==null&&(c.matrix.fromArray(r.transform.matrix),c.matrix.decompose(c.position,c.rotation,c.scale),c.matrixWorldNeedsUpdate=!0,r.linearVelocity?(c.hasLinearVelocity=!0,c.linearVelocity.copy(r.linearVelocity)):c.hasLinearVelocity=!1,r.angularVelocity?(c.hasAngularVelocity=!0,c.angularVelocity.copy(r.angularVelocity)):c.hasAngularVelocity=!1));a!==null&&(i=t.getPose(e.targetRaySpace,n),i===null&&r!==null&&(i=r),i!==null&&(a.matrix.fromArray(i.transform.matrix),a.matrix.decompose(a.position,a.rotation,a.scale),a.matrixWorldNeedsUpdate=!0,i.linearVelocity?(a.hasLinearVelocity=!0,a.linearVelocity.copy(i.linearVelocity)):a.hasLinearVelocity=!1,i.angularVelocity?(a.hasAngularVelocity=!0,a.angularVelocity.copy(i.angularVelocity)):a.hasAngularVelocity=!1,this.dispatchEvent(kg)))}return a!==null&&(a.visible=i!==null),c!==null&&(c.visible=r!==null),l!==null&&(l.visible=o!==null),this}_getHandJoint(e,t){if(e.joints[t.jointName]===void 0){let n=new Qt;n.matrixAutoUpdate=!1,n.visible=!1,e.joints[t.jointName]=n,e.add(n)}return e.joints[t.jointName]}},Hg=`
void main() {

	gl_Position = vec4( position, 1.0 );

}`,Vg=`
uniform sampler2DArray depthColor;
uniform float depthWidth;
uniform float depthHeight;

void main() {

	vec2 coord = vec2( gl_FragCoord.x / depthWidth, gl_FragCoord.y / depthHeight );

	if ( coord.x >= 1.0 ) {

		gl_FragDepth = texture( depthColor, vec3( coord.x - 1.0, coord.y, 1 ) ).r;

	} else {

		gl_FragDepth = texture( depthColor, vec3( coord.x, coord.y, 0 ) ).r;

	}

}`,nc=class{constructor(){this.texture=null,this.mesh=null,this.depthNear=0,this.depthFar=0}init(e,t,n){if(this.texture===null){let i=new Pt,r=e.properties.get(i);r.__webglTexture=t.texture,(t.depthNear!=n.depthNear||t.depthFar!=n.depthFar)&&(this.depthNear=t.depthNear,this.depthFar=t.depthFar),this.texture=i}}getMesh(e){if(this.texture!==null&&this.mesh===null){let t=e.cameras[0].viewport,n=new Gt({vertexShader:Hg,fragmentShader:Vg,uniforms:{depthColor:{value:this.texture},depthWidth:{value:t.z},depthHeight:{value:t.w}}});this.mesh=new Fe(new $t(20,20),n)}return this.mesh}reset(){this.texture=null,this.mesh=null}getDepthTexture(){return this.texture}},ic=class extends ui{constructor(e,t){super();let n=this,i=null,r=1,o=null,a="local-floor",c=1,l=null,u=null,h=null,f=null,p=null,g=null,v=new nc,m=t.getContextAttributes(),d=null,M=null,b=[],_=[],C=new le,A=null,E=new _t;E.viewport=new We;let I=new _t;I.viewport=new We;let x=[E,I],y=new tc,T=null,L=null;this.cameraAutoUpdate=!0,this.enabled=!1,this.isPresenting=!1,this.getController=function(G){let J=b[G];return J===void 0&&(J=new qs,b[G]=J),J.getTargetRaySpace()},this.getControllerGrip=function(G){let J=b[G];return J===void 0&&(J=new qs,b[G]=J),J.getGripSpace()},this.getHand=function(G){let J=b[G];return J===void 0&&(J=new qs,b[G]=J),J.getHandSpace()};function D(G){let J=_.indexOf(G.inputSource);if(J===-1)return;let re=b[J];re!==void 0&&(re.update(G.inputSource,G.frame,l||o),re.dispatchEvent({type:G.type,data:G.inputSource}))}function F(){i.removeEventListener("select",D),i.removeEventListener("selectstart",D),i.removeEventListener("selectend",D),i.removeEventListener("squeeze",D),i.removeEventListener("squeezestart",D),i.removeEventListener("squeezeend",D),i.removeEventListener("end",F),i.removeEventListener("inputsourceschange",X);for(let G=0;G<b.length;G++){let J=_[G];J!==null&&(_[G]=null,b[G].disconnect(J))}T=null,L=null,v.reset(),e.setRenderTarget(d),p=null,f=null,h=null,i=null,M=null,ue.stop(),n.isPresenting=!1,e.setPixelRatio(A),e.setSize(C.width,C.height,!1),n.dispatchEvent({type:"sessionend"})}this.setFramebufferScaleFactor=function(G){r=G,n.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change framebuffer scale while presenting.")},this.setReferenceSpaceType=function(G){a=G,n.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change reference space type while presenting.")},this.getReferenceSpace=function(){return l||o},this.setReferenceSpace=function(G){l=G},this.getBaseLayer=function(){return f!==null?f:p},this.getBinding=function(){return h},this.getFrame=function(){return g},this.getSession=function(){return i},this.setSession=async function(G){if(i=G,i!==null){if(d=e.getRenderTarget(),i.addEventListener("select",D),i.addEventListener("selectstart",D),i.addEventListener("selectend",D),i.addEventListener("squeeze",D),i.addEventListener("squeezestart",D),i.addEventListener("squeezeend",D),i.addEventListener("end",F),i.addEventListener("inputsourceschange",X),m.xrCompatible!==!0&&await t.makeXRCompatible(),A=e.getPixelRatio(),e.getSize(C),i.renderState.layers===void 0){let J={antialias:m.antialias,alpha:!0,depth:m.depth,stencil:m.stencil,framebufferScaleFactor:r};p=new XRWebGLLayer(i,t,J),i.updateRenderState({baseLayer:p}),e.setPixelRatio(1),e.setSize(p.framebufferWidth,p.framebufferHeight,!1),M=new Rn(p.framebufferWidth,p.framebufferHeight,{format:Ht,type:Dt,colorSpace:e.outputColorSpace,stencilBuffer:m.stencil})}else{let J=null,re=null,ee=null;m.depth&&(ee=m.stencil?t.DEPTH24_STENCIL8:t.DEPTH_COMPONENT24,J=m.stencil?cs:es,re=m.stencil?as:Yn);let oe={colorFormat:t.RGBA8,depthFormat:ee,scaleFactor:r};h=new XRWebGLBinding(i,t),f=h.createProjectionLayer(oe),i.updateRenderState({layers:[f]}),e.setPixelRatio(1),e.setSize(f.textureWidth,f.textureHeight,!1),M=new Rn(f.textureWidth,f.textureHeight,{format:Ht,type:Dt,depthTexture:new ms(f.textureWidth,f.textureHeight,re,void 0,void 0,void 0,void 0,void 0,void 0,J),stencilBuffer:m.stencil,colorSpace:e.outputColorSpace,samples:m.antialias?4:0,resolveDepthBuffer:f.ignoreDepthValues===!1})}M.isXRRenderTarget=!0,this.setFoveation(c),l=null,o=await i.requestReferenceSpace(a),ue.setContext(i),ue.start(),n.isPresenting=!0,n.dispatchEvent({type:"sessionstart"})}},this.getEnvironmentBlendMode=function(){if(i!==null)return i.environmentBlendMode},this.getDepthTexture=function(){return v.getDepthTexture()};function X(G){for(let J=0;J<G.removed.length;J++){let re=G.removed[J],ee=_.indexOf(re);ee>=0&&(_[ee]=null,b[ee].disconnect(re))}for(let J=0;J<G.added.length;J++){let re=G.added[J],ee=_.indexOf(re);if(ee===-1){for(let ye=0;ye<b.length;ye++)if(ye>=_.length){_.push(re),ee=ye;break}else if(_[ye]===null){_[ye]=re,ee=ye;break}if(ee===-1)break}let oe=b[ee];oe&&oe.connect(re)}}let z=new P,K=new P;function H(G,J,re){z.setFromMatrixPosition(J.matrixWorld),K.setFromMatrixPosition(re.matrixWorld);let ee=z.distanceTo(K),oe=J.projectionMatrix.elements,ye=re.projectionMatrix.elements,De=oe[14]/(oe[10]-1),Qe=oe[14]/(oe[10]+1),Ce=(oe[9]+1)/oe[5],qe=(oe[9]-1)/oe[5],N=(oe[8]-1)/oe[0],Ft=(ye[8]+1)/ye[0],Ge=De*N,Oe=De*Ft,Re=ee/(-N+Ft),ut=Re*-N;if(J.matrixWorld.decompose(G.position,G.quaternion,G.scale),G.translateX(ut),G.translateZ(Re),G.matrixWorld.compose(G.position,G.quaternion,G.scale),G.matrixWorldInverse.copy(G.matrixWorld).invert(),oe[10]===-1)G.projectionMatrix.copy(J.projectionMatrix),G.projectionMatrixInverse.copy(J.projectionMatrixInverse);else{let Ie=De+Re,R=Qe+Re,S=Ge-ut,W=Oe+(ee-ut),te=Ce*Qe/R*Ie,se=qe*Qe/R*Ie;G.projectionMatrix.makePerspective(S,W,te,se,Ie,R),G.projectionMatrixInverse.copy(G.projectionMatrix).invert()}}function k(G,J){J===null?G.matrixWorld.copy(G.matrix):G.matrixWorld.multiplyMatrices(J.matrixWorld,G.matrix),G.matrixWorldInverse.copy(G.matrixWorld).invert()}this.updateCamera=function(G){if(i===null)return;let J=G.near,re=G.far;v.texture!==null&&(v.depthNear>0&&(J=v.depthNear),v.depthFar>0&&(re=v.depthFar)),y.near=I.near=E.near=J,y.far=I.far=E.far=re,(T!==y.near||L!==y.far)&&(i.updateRenderState({depthNear:y.near,depthFar:y.far}),T=y.near,L=y.far),E.layers.mask=G.layers.mask|2,I.layers.mask=G.layers.mask|4,y.layers.mask=E.layers.mask|I.layers.mask;let ee=G.parent,oe=y.cameras;k(y,ee);for(let ye=0;ye<oe.length;ye++)k(oe[ye],ee);oe.length===2?H(y,E,I):y.projectionMatrix.copy(E.projectionMatrix),$(G,y,ee)};function $(G,J,re){re===null?G.matrix.copy(J.matrixWorld):(G.matrix.copy(re.matrixWorld),G.matrix.invert(),G.matrix.multiply(J.matrixWorld)),G.matrix.decompose(G.position,G.quaternion,G.scale),G.updateMatrixWorld(!0),G.projectionMatrix.copy(J.projectionMatrix),G.projectionMatrixInverse.copy(J.projectionMatrixInverse),G.isPerspectiveCamera&&(G.fov=hs*2*Math.atan(1/G.projectionMatrix.elements[5]),G.zoom=1)}this.getCamera=function(){return y},this.getFoveation=function(){if(!(f===null&&p===null))return c},this.setFoveation=function(G){c=G,f!==null&&(f.fixedFoveation=G),p!==null&&p.fixedFoveation!==void 0&&(p.fixedFoveation=G)},this.hasDepthSensing=function(){return v.texture!==null},this.getDepthSensingMesh=function(){return v.getMesh(y)};let ie=null;function j(G,J){if(u=J.getViewerPose(l||o),g=J,u!==null){let re=u.views;p!==null&&(e.setRenderTargetFramebuffer(M,p.framebuffer),e.setRenderTarget(M));let ee=!1;re.length!==y.cameras.length&&(y.cameras.length=0,ee=!0);for(let ye=0;ye<re.length;ye++){let De=re[ye],Qe=null;if(p!==null)Qe=p.getViewport(De);else{let qe=h.getViewSubImage(f,De);Qe=qe.viewport,ye===0&&(e.setRenderTargetTextures(M,qe.colorTexture,f.ignoreDepthValues?void 0:qe.depthStencilTexture),e.setRenderTarget(M))}let Ce=x[ye];Ce===void 0&&(Ce=new _t,Ce.layers.enable(ye),Ce.viewport=new We,x[ye]=Ce),Ce.matrix.fromArray(De.transform.matrix),Ce.matrix.decompose(Ce.position,Ce.quaternion,Ce.scale),Ce.projectionMatrix.fromArray(De.projectionMatrix),Ce.projectionMatrixInverse.copy(Ce.projectionMatrix).invert(),Ce.viewport.set(Qe.x,Qe.y,Qe.width,Qe.height),ye===0&&(y.matrix.copy(Ce.matrix),y.matrix.decompose(y.position,y.quaternion,y.scale)),ee===!0&&y.cameras.push(Ce)}let oe=i.enabledFeatures;if(oe&&oe.includes("depth-sensing")){let ye=h.getDepthInformation(re[0]);ye&&ye.isValid&&ye.texture&&v.init(e,ye,i.renderState)}}for(let re=0;re<b.length;re++){let ee=_[re],oe=b[re];ee!==null&&oe!==void 0&&oe.update(ee,J,l||o)}ie&&ie(G,J),J.detectedPlanes&&n.dispatchEvent({type:"planesdetected",data:J}),g=null}let ue=new hh;ue.setAnimationLoop(j),this.setAnimationLoop=function(G){ie=G},this.dispose=function(){}}},Ri=new pn,Gg=new Le;function Wg(s,e){function t(m,d){m.matrixAutoUpdate===!0&&m.updateMatrix(),d.value.copy(m.matrix)}function n(m,d){d.color.getRGB(m.fogColor.value,uh(s)),d.isFog?(m.fogNear.value=d.near,m.fogFar.value=d.far):d.isFogExp2&&(m.fogDensity.value=d.density)}function i(m,d,M,b,_){d.isMeshBasicMaterial||d.isMeshLambertMaterial?r(m,d):d.isMeshToonMaterial?(r(m,d),h(m,d)):d.isMeshPhongMaterial?(r(m,d),u(m,d)):d.isMeshStandardMaterial?(r(m,d),f(m,d),d.isMeshPhysicalMaterial&&p(m,d,_)):d.isMeshMatcapMaterial?(r(m,d),g(m,d)):d.isMeshDepthMaterial?r(m,d):d.isMeshDistanceMaterial?(r(m,d),v(m,d)):d.isMeshNormalMaterial?r(m,d):d.isLineBasicMaterial?(o(m,d),d.isLineDashedMaterial&&a(m,d)):d.isPointsMaterial?c(m,d,M,b):d.isSpriteMaterial?l(m,d):d.isShadowMaterial?(m.color.value.copy(d.color),m.opacity.value=d.opacity):d.isShaderMaterial&&(d.uniformsNeedUpdate=!1)}function r(m,d){m.opacity.value=d.opacity,d.color&&m.diffuse.value.copy(d.color),d.emissive&&m.emissive.value.copy(d.emissive).multiplyScalar(d.emissiveIntensity),d.map&&(m.map.value=d.map,t(d.map,m.mapTransform)),d.alphaMap&&(m.alphaMap.value=d.alphaMap,t(d.alphaMap,m.alphaMapTransform)),d.bumpMap&&(m.bumpMap.value=d.bumpMap,t(d.bumpMap,m.bumpMapTransform),m.bumpScale.value=d.bumpScale,d.side===Vt&&(m.bumpScale.value*=-1)),d.normalMap&&(m.normalMap.value=d.normalMap,t(d.normalMap,m.normalMapTransform),m.normalScale.value.copy(d.normalScale),d.side===Vt&&m.normalScale.value.negate()),d.displacementMap&&(m.displacementMap.value=d.displacementMap,t(d.displacementMap,m.displacementMapTransform),m.displacementScale.value=d.displacementScale,m.displacementBias.value=d.displacementBias),d.emissiveMap&&(m.emissiveMap.value=d.emissiveMap,t(d.emissiveMap,m.emissiveMapTransform)),d.specularMap&&(m.specularMap.value=d.specularMap,t(d.specularMap,m.specularMapTransform)),d.alphaTest>0&&(m.alphaTest.value=d.alphaTest);let M=e.get(d),b=M.envMap,_=M.envMapRotation;b&&(m.envMap.value=b,Ri.copy(_),Ri.x*=-1,Ri.y*=-1,Ri.z*=-1,b.isCubeTexture&&b.isRenderTargetTexture===!1&&(Ri.y*=-1,Ri.z*=-1),m.envMapRotation.value.setFromMatrix4(Gg.makeRotationFromEuler(Ri)),m.flipEnvMap.value=b.isCubeTexture&&b.isRenderTargetTexture===!1?-1:1,m.reflectivity.value=d.reflectivity,m.ior.value=d.ior,m.refractionRatio.value=d.refractionRatio),d.lightMap&&(m.lightMap.value=d.lightMap,m.lightMapIntensity.value=d.lightMapIntensity,t(d.lightMap,m.lightMapTransform)),d.aoMap&&(m.aoMap.value=d.aoMap,m.aoMapIntensity.value=d.aoMapIntensity,t(d.aoMap,m.aoMapTransform))}function o(m,d){m.diffuse.value.copy(d.color),m.opacity.value=d.opacity,d.map&&(m.map.value=d.map,t(d.map,m.mapTransform))}function a(m,d){m.dashSize.value=d.dashSize,m.totalSize.value=d.dashSize+d.gapSize,m.scale.value=d.scale}function c(m,d,M,b){m.diffuse.value.copy(d.color),m.opacity.value=d.opacity,m.size.value=d.size*M,m.scale.value=b*.5,d.map&&(m.map.value=d.map,t(d.map,m.uvTransform)),d.alphaMap&&(m.alphaMap.value=d.alphaMap,t(d.alphaMap,m.alphaMapTransform)),d.alphaTest>0&&(m.alphaTest.value=d.alphaTest)}function l(m,d){m.diffuse.value.copy(d.color),m.opacity.value=d.opacity,m.rotation.value=d.rotation,d.map&&(m.map.value=d.map,t(d.map,m.mapTransform)),d.alphaMap&&(m.alphaMap.value=d.alphaMap,t(d.alphaMap,m.alphaMapTransform)),d.alphaTest>0&&(m.alphaTest.value=d.alphaTest)}function u(m,d){m.specular.value.copy(d.specular),m.shininess.value=Math.max(d.shininess,1e-4)}function h(m,d){d.gradientMap&&(m.gradientMap.value=d.gradientMap)}function f(m,d){m.metalness.value=d.metalness,d.metalnessMap&&(m.metalnessMap.value=d.metalnessMap,t(d.metalnessMap,m.metalnessMapTransform)),m.roughness.value=d.roughness,d.roughnessMap&&(m.roughnessMap.value=d.roughnessMap,t(d.roughnessMap,m.roughnessMapTransform)),d.envMap&&(m.envMapIntensity.value=d.envMapIntensity)}function p(m,d,M){m.ior.value=d.ior,d.sheen>0&&(m.sheenColor.value.copy(d.sheenColor).multiplyScalar(d.sheen),m.sheenRoughness.value=d.sheenRoughness,d.sheenColorMap&&(m.sheenColorMap.value=d.sheenColorMap,t(d.sheenColorMap,m.sheenColorMapTransform)),d.sheenRoughnessMap&&(m.sheenRoughnessMap.value=d.sheenRoughnessMap,t(d.sheenRoughnessMap,m.sheenRoughnessMapTransform))),d.clearcoat>0&&(m.clearcoat.value=d.clearcoat,m.clearcoatRoughness.value=d.clearcoatRoughness,d.clearcoatMap&&(m.clearcoatMap.value=d.clearcoatMap,t(d.clearcoatMap,m.clearcoatMapTransform)),d.clearcoatRoughnessMap&&(m.clearcoatRoughnessMap.value=d.clearcoatRoughnessMap,t(d.clearcoatRoughnessMap,m.clearcoatRoughnessMapTransform)),d.clearcoatNormalMap&&(m.clearcoatNormalMap.value=d.clearcoatNormalMap,t(d.clearcoatNormalMap,m.clearcoatNormalMapTransform),m.clearcoatNormalScale.value.copy(d.clearcoatNormalScale),d.side===Vt&&m.clearcoatNormalScale.value.negate())),d.dispersion>0&&(m.dispersion.value=d.dispersion),d.iridescence>0&&(m.iridescence.value=d.iridescence,m.iridescenceIOR.value=d.iridescenceIOR,m.iridescenceThicknessMinimum.value=d.iridescenceThicknessRange[0],m.iridescenceThicknessMaximum.value=d.iridescenceThicknessRange[1],d.iridescenceMap&&(m.iridescenceMap.value=d.iridescenceMap,t(d.iridescenceMap,m.iridescenceMapTransform)),d.iridescenceThicknessMap&&(m.iridescenceThicknessMap.value=d.iridescenceThicknessMap,t(d.iridescenceThicknessMap,m.iridescenceThicknessMapTransform))),d.transmission>0&&(m.transmission.value=d.transmission,m.transmissionSamplerMap.value=M.texture,m.transmissionSamplerSize.value.set(M.width,M.height),d.transmissionMap&&(m.transmissionMap.value=d.transmissionMap,t(d.transmissionMap,m.transmissionMapTransform)),m.thickness.value=d.thickness,d.thicknessMap&&(m.thicknessMap.value=d.thicknessMap,t(d.thicknessMap,m.thicknessMapTransform)),m.attenuationDistance.value=d.attenuationDistance,m.attenuationColor.value.copy(d.attenuationColor)),d.anisotropy>0&&(m.anisotropyVector.value.set(d.anisotropy*Math.cos(d.anisotropyRotation),d.anisotropy*Math.sin(d.anisotropyRotation)),d.anisotropyMap&&(m.anisotropyMap.value=d.anisotropyMap,t(d.anisotropyMap,m.anisotropyMapTransform))),m.specularIntensity.value=d.specularIntensity,m.specularColor.value.copy(d.specularColor),d.specularColorMap&&(m.specularColorMap.value=d.specularColorMap,t(d.specularColorMap,m.specularColorMapTransform)),d.specularIntensityMap&&(m.specularIntensityMap.value=d.specularIntensityMap,t(d.specularIntensityMap,m.specularIntensityMapTransform))}function g(m,d){d.matcap&&(m.matcap.value=d.matcap)}function v(m,d){let M=e.get(d).light;m.referencePosition.value.setFromMatrixPosition(M.matrixWorld),m.nearDistance.value=M.shadow.camera.near,m.farDistance.value=M.shadow.camera.far}return{refreshFogUniforms:n,refreshMaterialUniforms:i}}function Xg(s,e,t,n){let i={},r={},o=[],a=s.getParameter(s.MAX_UNIFORM_BUFFER_BINDINGS);function c(M,b){let _=b.program;n.uniformBlockBinding(M,_)}function l(M,b){let _=i[M.id];_===void 0&&(g(M),_=u(M),i[M.id]=_,M.addEventListener("dispose",m));let C=b.program;n.updateUBOMapping(M,C);let A=e.render.frame;r[M.id]!==A&&(f(M),r[M.id]=A)}function u(M){let b=h();M.__bindingPointIndex=b;let _=s.createBuffer(),C=M.__size,A=M.usage;return s.bindBuffer(s.UNIFORM_BUFFER,_),s.bufferData(s.UNIFORM_BUFFER,C,A),s.bindBuffer(s.UNIFORM_BUFFER,null),s.bindBufferBase(s.UNIFORM_BUFFER,b,_),_}function h(){for(let M=0;M<a;M++)if(o.indexOf(M)===-1)return o.push(M),M;return console.error("THREE.WebGLRenderer: Maximum number of simultaneously usable uniforms groups reached."),0}function f(M){let b=i[M.id],_=M.uniforms,C=M.__cache;s.bindBuffer(s.UNIFORM_BUFFER,b);for(let A=0,E=_.length;A<E;A++){let I=Array.isArray(_[A])?_[A]:[_[A]];for(let x=0,y=I.length;x<y;x++){let T=I[x];if(p(T,A,x,C)===!0){let L=T.__offset,D=Array.isArray(T.value)?T.value:[T.value],F=0;for(let X=0;X<D.length;X++){let z=D[X],K=v(z);typeof z=="number"||typeof z=="boolean"?(T.__data[0]=z,s.bufferSubData(s.UNIFORM_BUFFER,L+F,T.__data)):z.isMatrix3?(T.__data[0]=z.elements[0],T.__data[1]=z.elements[1],T.__data[2]=z.elements[2],T.__data[3]=0,T.__data[4]=z.elements[3],T.__data[5]=z.elements[4],T.__data[6]=z.elements[5],T.__data[7]=0,T.__data[8]=z.elements[6],T.__data[9]=z.elements[7],T.__data[10]=z.elements[8],T.__data[11]=0):(z.toArray(T.__data,F),F+=K.storage/Float32Array.BYTES_PER_ELEMENT)}s.bufferSubData(s.UNIFORM_BUFFER,L,T.__data)}}}s.bindBuffer(s.UNIFORM_BUFFER,null)}function p(M,b,_,C){let A=M.value,E=b+"_"+_;if(C[E]===void 0)return typeof A=="number"||typeof A=="boolean"?C[E]=A:C[E]=A.clone(),!0;{let I=C[E];if(typeof A=="number"||typeof A=="boolean"){if(I!==A)return C[E]=A,!0}else if(I.equals(A)===!1)return I.copy(A),!0}return!1}function g(M){let b=M.uniforms,_=0,C=16;for(let E=0,I=b.length;E<I;E++){let x=Array.isArray(b[E])?b[E]:[b[E]];for(let y=0,T=x.length;y<T;y++){let L=x[y],D=Array.isArray(L.value)?L.value:[L.value];for(let F=0,X=D.length;F<X;F++){let z=D[F],K=v(z),H=_%C,k=H%K.boundary,$=H+k;_+=k,$!==0&&C-$<K.storage&&(_+=C-$),L.__data=new Float32Array(K.storage/Float32Array.BYTES_PER_ELEMENT),L.__offset=_,_+=K.storage}}}let A=_%C;return A>0&&(_+=C-A),M.__size=_,M.__cache={},this}function v(M){let b={boundary:0,storage:0};return typeof M=="number"||typeof M=="boolean"?(b.boundary=4,b.storage=4):M.isVector2?(b.boundary=8,b.storage=8):M.isVector3||M.isColor?(b.boundary=16,b.storage=12):M.isVector4?(b.boundary=16,b.storage=16):M.isMatrix3?(b.boundary=48,b.storage=48):M.isMatrix4?(b.boundary=64,b.storage=64):M.isTexture?console.warn("THREE.WebGLRenderer: Texture samplers can not be part of an uniforms group."):console.warn("THREE.WebGLRenderer: Unsupported uniform value type.",M),b}function m(M){let b=M.target;b.removeEventListener("dispose",m);let _=o.indexOf(b.__bindingPointIndex);o.splice(_,1),s.deleteBuffer(i[b.id]),delete i[b.id],delete r[b.id]}function d(){for(let M in i)s.deleteBuffer(i[M]);o=[],i={},r={}}return{bind:c,update:l,dispose:d}}var eo=class{constructor(e={}){let{canvas:t=Zf(),context:n=null,depth:i=!0,stencil:r=!1,alpha:o=!1,antialias:a=!1,premultipliedAlpha:c=!0,preserveDrawingBuffer:l=!1,powerPreference:u="default",failIfMajorPerformanceCaveat:h=!1,reverseDepthBuffer:f=!1}=e;this.isWebGLRenderer=!0;let p;if(n!==null){if(typeof WebGLRenderingContext<"u"&&n instanceof WebGLRenderingContext)throw new Error("THREE.WebGLRenderer: WebGL 1 is not supported since r163.");p=n.getContextAttributes().alpha}else p=o;let g=new Uint32Array(4),v=new Int32Array(4),m=null,d=null,M=[],b=[];this.domElement=t,this.debug={checkShaderErrors:!0,onShaderError:null},this.autoClear=!0,this.autoClearColor=!0,this.autoClearDepth=!0,this.autoClearStencil=!0,this.sortObjects=!0,this.clippingPlanes=[],this.localClippingEnabled=!1,this._outputColorSpace=St,this.toneMapping=Ln,this.toneMappingExposure=1;let _=this,C=!1,A=0,E=0,I=null,x=-1,y=null,T=new We,L=new We,D=null,F=new ve(0),X=0,z=t.width,K=t.height,H=1,k=null,$=null,ie=new We(0,0,z,K),j=new We(0,0,z,K),ue=!1,G=new Ks,J=!1,re=!1,ee=new Le,oe=new Le,ye=new P,De=new We,Qe={background:null,fog:null,environment:null,overrideMaterial:null,isScene:!0},Ce=!1;function qe(){return I===null?H:1}let N=n;function Ft(w,O){return t.getContext(w,O)}try{let w={alpha:!0,depth:i,stencil:r,antialias:a,premultipliedAlpha:c,preserveDrawingBuffer:l,powerPreference:u,failIfMajorPerformanceCaveat:h};if("setAttribute"in t&&t.setAttribute("data-engine",`three.js r${gc}`),t.addEventListener("webglcontextlost",ne,!1),t.addEventListener("webglcontextrestored",ge,!1),t.addEventListener("webglcontextcreationerror",pe,!1),N===null){let O="webgl2";if(N=Ft(O,w),N===null)throw Ft(O)?new Error("Error creating WebGL context with your selected attributes."):new Error("Error creating WebGL context.")}}catch(w){throw console.error("THREE.WebGLRenderer: "+w.message),w}let Ge,Oe,Re,ut,Ie,R,S,W,te,se,Q,Te,de,_e,et,ae,Me,Pe,Ue,be,Ke,He,ht,U;function fe(){Ge=new a0(N),Ge.init(),He=new zg(N,Ge),Oe=new t0(N,Ge,e,He),Re=new Fg(N,Ge),Oe.reverseDepthBuffer&&f&&Re.buffers.depth.setReversed(!0),ut=new u0(N),Ie=new Sg,R=new Bg(N,Ge,Re,Ie,Oe,He,ut),S=new i0(_),W=new o0(_),te=new vd(N),ht=new Qm(N,te),se=new c0(N,te,ut,ht),Q=new f0(N,se,te,ut),Ue=new h0(N,Oe,R),ae=new n0(Ie),Te=new bg(_,S,W,Ge,Oe,ht,ae),de=new Wg(_,Ie),_e=new Eg,et=new Pg(Ge),Pe=new jm(_,S,W,Re,Q,p,c),Me=new Ug(_,Q,Oe),U=new Xg(N,ut,Oe,Re),be=new e0(N,Ge,ut),Ke=new l0(N,Ge,ut),ut.programs=Te.programs,_.capabilities=Oe,_.extensions=Ge,_.properties=Ie,_.renderLists=_e,_.shadowMap=Me,_.state=Re,_.info=ut}fe();let Z=new ic(_,N);this.xr=Z,this.getContext=function(){return N},this.getContextAttributes=function(){return N.getContextAttributes()},this.forceContextLoss=function(){let w=Ge.get("WEBGL_lose_context");w&&w.loseContext()},this.forceContextRestore=function(){let w=Ge.get("WEBGL_lose_context");w&&w.restoreContext()},this.getPixelRatio=function(){return H},this.setPixelRatio=function(w){w!==void 0&&(H=w,this.setSize(z,K,!1))},this.getSize=function(w){return w.set(z,K)},this.setSize=function(w,O,q=!0){if(Z.isPresenting){console.warn("THREE.WebGLRenderer: Can't change size while VR device is presenting.");return}z=w,K=O,t.width=Math.floor(w*H),t.height=Math.floor(O*H),q===!0&&(t.style.width=w+"px",t.style.height=O+"px"),this.setViewport(0,0,w,O)},this.getDrawingBufferSize=function(w){return w.set(z*H,K*H).floor()},this.setDrawingBufferSize=function(w,O,q){z=w,K=O,H=q,t.width=Math.floor(w*q),t.height=Math.floor(O*q),this.setViewport(0,0,w,O)},this.getCurrentViewport=function(w){return w.copy(T)},this.getViewport=function(w){return w.copy(ie)},this.setViewport=function(w,O,q,Y){w.isVector4?ie.set(w.x,w.y,w.z,w.w):ie.set(w,O,q,Y),Re.viewport(T.copy(ie).multiplyScalar(H).round())},this.getScissor=function(w){return w.copy(j)},this.setScissor=function(w,O,q,Y){w.isVector4?j.set(w.x,w.y,w.z,w.w):j.set(w,O,q,Y),Re.scissor(L.copy(j).multiplyScalar(H).round())},this.getScissorTest=function(){return ue},this.setScissorTest=function(w){Re.setScissorTest(ue=w)},this.setOpaqueSort=function(w){k=w},this.setTransparentSort=function(w){$=w},this.getClearColor=function(w){return w.copy(Pe.getClearColor())},this.setClearColor=function(){Pe.setClearColor.apply(Pe,arguments)},this.getClearAlpha=function(){return Pe.getClearAlpha()},this.setClearAlpha=function(){Pe.setClearAlpha.apply(Pe,arguments)},this.clear=function(w=!0,O=!0,q=!0){let Y=0;if(w){let B=!1;if(I!==null){let ce=I.texture.format;B=ce===Ec||ce===wc||ce===Sc}if(B){let ce=I.texture.type,me=ce===Dt||ce===Yn||ce===$s||ce===as||ce===yc||ce===Mc,Se=Pe.getClearColor(),we=Pe.getClearAlpha(),Ne=Se.r,ze=Se.g,Ee=Se.b;me?(g[0]=Ne,g[1]=ze,g[2]=Ee,g[3]=we,N.clearBufferuiv(N.COLOR,0,g)):(v[0]=Ne,v[1]=ze,v[2]=Ee,v[3]=we,N.clearBufferiv(N.COLOR,0,v))}else Y|=N.COLOR_BUFFER_BIT}O&&(Y|=N.DEPTH_BUFFER_BIT),q&&(Y|=N.STENCIL_BUFFER_BIT,this.state.buffers.stencil.setMask(4294967295)),N.clear(Y)},this.clearColor=function(){this.clear(!0,!1,!1)},this.clearDepth=function(){this.clear(!1,!0,!1)},this.clearStencil=function(){this.clear(!1,!1,!0)},this.dispose=function(){t.removeEventListener("webglcontextlost",ne,!1),t.removeEventListener("webglcontextrestored",ge,!1),t.removeEventListener("webglcontextcreationerror",pe,!1),_e.dispose(),et.dispose(),Ie.dispose(),S.dispose(),W.dispose(),Q.dispose(),ht.dispose(),U.dispose(),Te.dispose(),Z.dispose(),Z.removeEventListener("sessionstart",Ml),Z.removeEventListener("sessionend",bl),bi.stop()};function ne(w){w.preventDefault(),console.log("THREE.WebGLRenderer: Context Lost."),C=!0}function ge(){console.log("THREE.WebGLRenderer: Context Restored."),C=!1;let w=ut.autoReset,O=Me.enabled,q=Me.autoUpdate,Y=Me.needsUpdate,B=Me.type;fe(),ut.autoReset=w,Me.enabled=O,Me.autoUpdate=q,Me.needsUpdate=Y,Me.type=B}function pe(w){console.error("THREE.WebGLRenderer: A WebGL context could not be created. Reason: ",w.statusMessage)}function Be(w){let O=w.target;O.removeEventListener("dispose",Be),vt(O)}function vt(w){Ot(w),Ie.remove(w)}function Ot(w){let O=Ie.get(w).programs;O!==void 0&&(O.forEach(function(q){Te.releaseProgram(q)}),w.isShaderMaterial&&Te.releaseShaderCache(w))}this.renderBufferDirect=function(w,O,q,Y,B,ce){O===null&&(O=Qe);let me=B.isMesh&&B.matrixWorld.determinant()<0,Se=Vh(w,O,q,Y,B);Re.setMaterial(Y,me);let we=q.index,Ne=1;if(Y.wireframe===!0){if(we=se.getWireframeAttribute(q),we===void 0)return;Ne=2}let ze=q.drawRange,Ee=q.attributes.position,tt=ze.start*Ne,ft=(ze.start+ze.count)*Ne;ce!==null&&(tt=Math.max(tt,ce.start*Ne),ft=Math.min(ft,(ce.start+ce.count)*Ne)),we!==null?(tt=Math.max(tt,0),ft=Math.min(ft,we.count)):Ee!=null&&(tt=Math.max(tt,0),ft=Math.min(ft,Ee.count));let pt=ft-tt;if(pt<0||pt===1/0)return;ht.setup(B,Y,Se,q,we);let jt,rt=be;if(we!==null&&(jt=te.get(we),rt=Ke,rt.setIndex(jt)),B.isMesh)Y.wireframe===!0?(Re.setLineWidth(Y.wireframeLinewidth*qe()),rt.setMode(N.LINES)):rt.setMode(N.TRIANGLES);else if(B.isLine){let Ae=Y.linewidth;Ae===void 0&&(Ae=1),Re.setLineWidth(Ae*qe()),B.isLineSegments?rt.setMode(N.LINES):B.isLineLoop?rt.setMode(N.LINE_LOOP):rt.setMode(N.LINE_STRIP)}else B.isPoints?rt.setMode(N.POINTS):B.isSprite&&rt.setMode(N.TRIANGLES);if(B.isBatchedMesh)if(B._multiDrawInstances!==null)rt.renderMultiDrawInstances(B._multiDrawStarts,B._multiDrawCounts,B._multiDrawCount,B._multiDrawInstances);else if(Ge.get("WEBGL_multi_draw"))rt.renderMultiDraw(B._multiDrawStarts,B._multiDrawCounts,B._multiDrawCount);else{let Ae=B._multiDrawStarts,Fn=B._multiDrawCounts,ot=B._multiDrawCount,_n=we?te.get(we).bytesPerElement:1,Ni=Ie.get(Y).currentProgram.getUniforms();for(let tn=0;tn<ot;tn++)Ni.setValue(N,"_gl_DrawID",tn),rt.render(Ae[tn]/_n,Fn[tn])}else if(B.isInstancedMesh)rt.renderInstances(tt,pt,B.count);else if(q.isInstancedBufferGeometry){let Ae=q._maxInstanceCount!==void 0?q._maxInstanceCount:1/0,Fn=Math.min(q.instanceCount,Ae);rt.renderInstances(tt,pt,Fn)}else rt.render(tt,pt)};function at(w,O,q){w.transparent===!0&&w.side===Lt&&w.forceSinglePass===!1?(w.side=Vt,w.needsUpdate=!0,dr(w,O,q),w.side=en,w.needsUpdate=!0,dr(w,O,q),w.side=Lt):dr(w,O,q)}this.compile=function(w,O,q=null){q===null&&(q=w),d=et.get(q),d.init(O),b.push(d),q.traverseVisible(function(B){B.isLight&&B.layers.test(O.layers)&&(d.pushLight(B),B.castShadow&&d.pushShadow(B))}),w!==q&&w.traverseVisible(function(B){B.isLight&&B.layers.test(O.layers)&&(d.pushLight(B),B.castShadow&&d.pushShadow(B))}),d.setupLights();let Y=new Set;return w.traverse(function(B){if(!(B.isMesh||B.isPoints||B.isLine||B.isSprite))return;let ce=B.material;if(ce)if(Array.isArray(ce))for(let me=0;me<ce.length;me++){let Se=ce[me];at(Se,q,B),Y.add(Se)}else at(ce,q,B),Y.add(ce)}),b.pop(),d=null,Y},this.compileAsync=function(w,O,q=null){let Y=this.compile(w,O,q);return new Promise(B=>{function ce(){if(Y.forEach(function(me){Ie.get(me).currentProgram.isReady()&&Y.delete(me)}),Y.size===0){B(w);return}setTimeout(ce,10)}Ge.get("KHR_parallel_shader_compile")!==null?ce():setTimeout(ce,10)})};let xn=null;function Nn(w){xn&&xn(w)}function Ml(){bi.stop()}function bl(){bi.start()}let bi=new hh;bi.setAnimationLoop(Nn),typeof self<"u"&&bi.setContext(self),this.setAnimationLoop=function(w){xn=w,Z.setAnimationLoop(w),w===null?bi.stop():bi.start()},Z.addEventListener("sessionstart",Ml),Z.addEventListener("sessionend",bl),this.render=function(w,O){if(O!==void 0&&O.isCamera!==!0){console.error("THREE.WebGLRenderer.render: camera is not an instance of THREE.Camera.");return}if(C===!0)return;if(w.matrixWorldAutoUpdate===!0&&w.updateMatrixWorld(),O.parent===null&&O.matrixWorldAutoUpdate===!0&&O.updateMatrixWorld(),Z.enabled===!0&&Z.isPresenting===!0&&(Z.cameraAutoUpdate===!0&&Z.updateCamera(O),O=Z.getCamera()),w.isScene===!0&&w.onBeforeRender(_,w,O,I),d=et.get(w,b.length),d.init(O),b.push(d),oe.multiplyMatrices(O.projectionMatrix,O.matrixWorldInverse),G.setFromProjectionMatrix(oe),re=this.localClippingEnabled,J=ae.init(this.clippingPlanes,re),m=_e.get(w,M.length),m.init(),M.push(m),Z.enabled===!0&&Z.isPresenting===!0){let ce=_.xr.getDepthSensingMesh();ce!==null&&Eo(ce,O,-1/0,_.sortObjects)}Eo(w,O,0,_.sortObjects),m.finish(),_.sortObjects===!0&&m.sort(k,$),Ce=Z.enabled===!1||Z.isPresenting===!1||Z.hasDepthSensing()===!1,Ce&&Pe.addToRenderList(m,w),this.info.render.frame++,J===!0&&ae.beginShadows();let q=d.state.shadowsArray;Me.render(q,w,O),J===!0&&ae.endShadows(),this.info.autoReset===!0&&this.info.reset();let Y=m.opaque,B=m.transmissive;if(d.setupLights(),O.isArrayCamera){let ce=O.cameras;if(B.length>0)for(let me=0,Se=ce.length;me<Se;me++){let we=ce[me];wl(Y,B,w,we)}Ce&&Pe.render(w);for(let me=0,Se=ce.length;me<Se;me++){let we=ce[me];Sl(m,w,we,we.viewport)}}else B.length>0&&wl(Y,B,w,O),Ce&&Pe.render(w),Sl(m,w,O);I!==null&&(R.updateMultisampleRenderTarget(I),R.updateRenderTargetMipmap(I)),w.isScene===!0&&w.onAfterRender(_,w,O),ht.resetDefaultState(),x=-1,y=null,b.pop(),b.length>0?(d=b[b.length-1],J===!0&&ae.setGlobalState(_.clippingPlanes,d.state.camera)):d=null,M.pop(),M.length>0?m=M[M.length-1]:m=null};function Eo(w,O,q,Y){if(w.visible===!1)return;if(w.layers.test(O.layers)){if(w.isGroup)q=w.renderOrder;else if(w.isLOD)w.autoUpdate===!0&&w.update(O);else if(w.isLight)d.pushLight(w),w.castShadow&&d.pushShadow(w);else if(w.isSprite){if(!w.frustumCulled||G.intersectsSprite(w)){Y&&De.setFromMatrixPosition(w.matrixWorld).applyMatrix4(oe);let me=Q.update(w),Se=w.material;Se.visible&&m.push(w,me,Se,q,De.z,null)}}else if((w.isMesh||w.isLine||w.isPoints)&&(!w.frustumCulled||G.intersectsObject(w))){let me=Q.update(w),Se=w.material;if(Y&&(w.boundingSphere!==void 0?(w.boundingSphere===null&&w.computeBoundingSphere(),De.copy(w.boundingSphere.center)):(me.boundingSphere===null&&me.computeBoundingSphere(),De.copy(me.boundingSphere.center)),De.applyMatrix4(w.matrixWorld).applyMatrix4(oe)),Array.isArray(Se)){let we=me.groups;for(let Ne=0,ze=we.length;Ne<ze;Ne++){let Ee=we[Ne],tt=Se[Ee.materialIndex];tt&&tt.visible&&m.push(w,me,tt,q,De.z,Ee)}}else Se.visible&&m.push(w,me,Se,q,De.z,null)}}let ce=w.children;for(let me=0,Se=ce.length;me<Se;me++)Eo(ce[me],O,q,Y)}function Sl(w,O,q,Y){let B=w.opaque,ce=w.transmissive,me=w.transparent;d.setupLightsView(q),J===!0&&ae.setGlobalState(_.clippingPlanes,q),Y&&Re.viewport(T.copy(Y)),B.length>0&&fr(B,O,q),ce.length>0&&fr(ce,O,q),me.length>0&&fr(me,O,q),Re.buffers.depth.setTest(!0),Re.buffers.depth.setMask(!0),Re.buffers.color.setMask(!0),Re.setPolygonOffset(!1)}function wl(w,O,q,Y){if((q.isScene===!0?q.overrideMaterial:null)!==null)return;d.state.transmissionRenderTarget[Y.id]===void 0&&(d.state.transmissionRenderTarget[Y.id]=new Rn(1,1,{generateMipmaps:!0,type:Ge.has("EXT_color_buffer_half_float")||Ge.has("EXT_color_buffer_float")?$e:Dt,minFilter:Pn,samples:4,stencilBuffer:r,resolveDepthBuffer:!1,resolveStencilBuffer:!1,colorSpace:Ye.workingColorSpace}));let ce=d.state.transmissionRenderTarget[Y.id],me=Y.viewport||T;ce.setSize(me.z,me.w);let Se=_.getRenderTarget();_.setRenderTarget(ce),_.getClearColor(F),X=_.getClearAlpha(),X<1&&_.setClearColor(16777215,.5),_.clear(),Ce&&Pe.render(q);let we=_.toneMapping;_.toneMapping=Ln;let Ne=Y.viewport;if(Y.viewport!==void 0&&(Y.viewport=void 0),d.setupLightsView(Y),J===!0&&ae.setGlobalState(_.clippingPlanes,Y),fr(w,q,Y),R.updateMultisampleRenderTarget(ce),R.updateRenderTargetMipmap(ce),Ge.has("WEBGL_multisampled_render_to_texture")===!1){let ze=!1;for(let Ee=0,tt=O.length;Ee<tt;Ee++){let ft=O[Ee],pt=ft.object,jt=ft.geometry,rt=ft.material,Ae=ft.group;if(rt.side===Lt&&pt.layers.test(Y.layers)){let Fn=rt.side;rt.side=Vt,rt.needsUpdate=!0,El(pt,q,Y,jt,rt,Ae),rt.side=Fn,rt.needsUpdate=!0,ze=!0}}ze===!0&&(R.updateMultisampleRenderTarget(ce),R.updateRenderTargetMipmap(ce))}_.setRenderTarget(Se),_.setClearColor(F,X),Ne!==void 0&&(Y.viewport=Ne),_.toneMapping=we}function fr(w,O,q){let Y=O.isScene===!0?O.overrideMaterial:null;for(let B=0,ce=w.length;B<ce;B++){let me=w[B],Se=me.object,we=me.geometry,Ne=Y===null?me.material:Y,ze=me.group;Se.layers.test(q.layers)&&El(Se,O,q,we,Ne,ze)}}function El(w,O,q,Y,B,ce){w.onBeforeRender(_,O,q,Y,B,ce),w.modelViewMatrix.multiplyMatrices(q.matrixWorldInverse,w.matrixWorld),w.normalMatrix.getNormalMatrix(w.modelViewMatrix),B.onBeforeRender(_,O,q,Y,w,ce),B.transparent===!0&&B.side===Lt&&B.forceSinglePass===!1?(B.side=Vt,B.needsUpdate=!0,_.renderBufferDirect(q,O,Y,B,w,ce),B.side=en,B.needsUpdate=!0,_.renderBufferDirect(q,O,Y,B,w,ce),B.side=Lt):_.renderBufferDirect(q,O,Y,B,w,ce),w.onAfterRender(_,O,q,Y,B,ce)}function dr(w,O,q){O.isScene!==!0&&(O=Qe);let Y=Ie.get(w),B=d.state.lights,ce=d.state.shadowsArray,me=B.state.version,Se=Te.getParameters(w,B.state,ce,O,q),we=Te.getProgramCacheKey(Se),Ne=Y.programs;Y.environment=w.isMeshStandardMaterial?O.environment:null,Y.fog=O.fog,Y.envMap=(w.isMeshStandardMaterial?W:S).get(w.envMap||Y.environment),Y.envMapRotation=Y.environment!==null&&w.envMap===null?O.environmentRotation:w.envMapRotation,Ne===void 0&&(w.addEventListener("dispose",Be),Ne=new Map,Y.programs=Ne);let ze=Ne.get(we);if(ze!==void 0){if(Y.currentProgram===ze&&Y.lightsStateVersion===me)return Al(w,Se),ze}else Se.uniforms=Te.getUniforms(w),w.onBeforeCompile(Se,_),ze=Te.acquireProgram(Se,we),Ne.set(we,ze),Y.uniforms=Se.uniforms;let Ee=Y.uniforms;return(!w.isShaderMaterial&&!w.isRawShaderMaterial||w.clipping===!0)&&(Ee.clippingPlanes=ae.uniform),Al(w,Se),Y.needsLights=Wh(w),Y.lightsStateVersion=me,Y.needsLights&&(Ee.ambientLightColor.value=B.state.ambient,Ee.lightProbe.value=B.state.probe,Ee.directionalLights.value=B.state.directional,Ee.directionalLightShadows.value=B.state.directionalShadow,Ee.spotLights.value=B.state.spot,Ee.spotLightShadows.value=B.state.spotShadow,Ee.rectAreaLights.value=B.state.rectArea,Ee.ltc_1.value=B.state.rectAreaLTC1,Ee.ltc_2.value=B.state.rectAreaLTC2,Ee.pointLights.value=B.state.point,Ee.pointLightShadows.value=B.state.pointShadow,Ee.hemisphereLights.value=B.state.hemi,Ee.directionalShadowMap.value=B.state.directionalShadowMap,Ee.directionalShadowMatrix.value=B.state.directionalShadowMatrix,Ee.spotShadowMap.value=B.state.spotShadowMap,Ee.spotLightMatrix.value=B.state.spotLightMatrix,Ee.spotLightMap.value=B.state.spotLightMap,Ee.pointShadowMap.value=B.state.pointShadowMap,Ee.pointShadowMatrix.value=B.state.pointShadowMatrix),Y.currentProgram=ze,Y.uniformsList=null,ze}function Tl(w){if(w.uniformsList===null){let O=w.currentProgram.getUniforms();w.uniformsList=ns.seqWithValue(O.seq,w.uniforms)}return w.uniformsList}function Al(w,O){let q=Ie.get(w);q.outputColorSpace=O.outputColorSpace,q.batching=O.batching,q.batchingColor=O.batchingColor,q.instancing=O.instancing,q.instancingColor=O.instancingColor,q.instancingMorph=O.instancingMorph,q.skinning=O.skinning,q.morphTargets=O.morphTargets,q.morphNormals=O.morphNormals,q.morphColors=O.morphColors,q.morphTargetsCount=O.morphTargetsCount,q.numClippingPlanes=O.numClippingPlanes,q.numIntersection=O.numClipIntersection,q.vertexAlphas=O.vertexAlphas,q.vertexTangents=O.vertexTangents,q.toneMapping=O.toneMapping}function Vh(w,O,q,Y,B){O.isScene!==!0&&(O=Qe),R.resetTextureUnits();let ce=O.fog,me=Y.isMeshStandardMaterial?O.environment:null,Se=I===null?_.outputColorSpace:I.isXRRenderTarget===!0?I.texture.colorSpace:Wt,we=(Y.isMeshStandardMaterial?W:S).get(Y.envMap||me),Ne=Y.vertexColors===!0&&!!q.attributes.color&&q.attributes.color.itemSize===4,ze=!!q.attributes.tangent&&(!!Y.normalMap||Y.anisotropy>0),Ee=!!q.morphAttributes.position,tt=!!q.morphAttributes.normal,ft=!!q.morphAttributes.color,pt=Ln;Y.toneMapped&&(I===null||I.isXRRenderTarget===!0)&&(pt=_.toneMapping);let jt=q.morphAttributes.position||q.morphAttributes.normal||q.morphAttributes.color,rt=jt!==void 0?jt.length:0,Ae=Ie.get(Y),Fn=d.state.lights;if(J===!0&&(re===!0||w!==y)){let un=w===y&&Y.id===x;ae.setState(Y,w,un)}let ot=!1;Y.version===Ae.__version?(Ae.needsLights&&Ae.lightsStateVersion!==Fn.state.version||Ae.outputColorSpace!==Se||B.isBatchedMesh&&Ae.batching===!1||!B.isBatchedMesh&&Ae.batching===!0||B.isBatchedMesh&&Ae.batchingColor===!0&&B.colorTexture===null||B.isBatchedMesh&&Ae.batchingColor===!1&&B.colorTexture!==null||B.isInstancedMesh&&Ae.instancing===!1||!B.isInstancedMesh&&Ae.instancing===!0||B.isSkinnedMesh&&Ae.skinning===!1||!B.isSkinnedMesh&&Ae.skinning===!0||B.isInstancedMesh&&Ae.instancingColor===!0&&B.instanceColor===null||B.isInstancedMesh&&Ae.instancingColor===!1&&B.instanceColor!==null||B.isInstancedMesh&&Ae.instancingMorph===!0&&B.morphTexture===null||B.isInstancedMesh&&Ae.instancingMorph===!1&&B.morphTexture!==null||Ae.envMap!==we||Y.fog===!0&&Ae.fog!==ce||Ae.numClippingPlanes!==void 0&&(Ae.numClippingPlanes!==ae.numPlanes||Ae.numIntersection!==ae.numIntersection)||Ae.vertexAlphas!==Ne||Ae.vertexTangents!==ze||Ae.morphTargets!==Ee||Ae.morphNormals!==tt||Ae.morphColors!==ft||Ae.toneMapping!==pt||Ae.morphTargetsCount!==rt)&&(ot=!0):(ot=!0,Ae.__version=Y.version);let _n=Ae.currentProgram;ot===!0&&(_n=dr(Y,O,B));let Ni=!1,tn=!1,Ps=!1,mt=_n.getUniforms(),Cn=Ae.uniforms;if(Re.useProgram(_n.program)&&(Ni=!0,tn=!0,Ps=!0),Y.id!==x&&(x=Y.id,tn=!0),Ni||y!==w){Re.buffers.depth.getReversed()?(ee.copy(w.projectionMatrix),Jf(ee),jf(ee),mt.setValue(N,"projectionMatrix",ee)):mt.setValue(N,"projectionMatrix",w.projectionMatrix),mt.setValue(N,"viewMatrix",w.matrixWorldInverse);let ei=mt.map.cameraPosition;ei!==void 0&&ei.setValue(N,ye.setFromMatrixPosition(w.matrixWorld)),Oe.logarithmicDepthBuffer&&mt.setValue(N,"logDepthBufFC",2/(Math.log(w.far+1)/Math.LN2)),(Y.isMeshPhongMaterial||Y.isMeshToonMaterial||Y.isMeshLambertMaterial||Y.isMeshBasicMaterial||Y.isMeshStandardMaterial||Y.isShaderMaterial)&&mt.setValue(N,"isOrthographic",w.isOrthographicCamera===!0),y!==w&&(y=w,tn=!0,Ps=!0)}if(B.isSkinnedMesh){mt.setOptional(N,B,"bindMatrix"),mt.setOptional(N,B,"bindMatrixInverse");let un=B.skeleton;un&&(un.boneTexture===null&&un.computeBoneTexture(),mt.setValue(N,"boneTexture",un.boneTexture,R))}B.isBatchedMesh&&(mt.setOptional(N,B,"batchingTexture"),mt.setValue(N,"batchingTexture",B._matricesTexture,R),mt.setOptional(N,B,"batchingIdTexture"),mt.setValue(N,"batchingIdTexture",B._indirectTexture,R),mt.setOptional(N,B,"batchingColorTexture"),B._colorsTexture!==null&&mt.setValue(N,"batchingColorTexture",B._colorsTexture,R));let Ls=q.morphAttributes;if((Ls.position!==void 0||Ls.normal!==void 0||Ls.color!==void 0)&&Ue.update(B,q,_n),(tn||Ae.receiveShadow!==B.receiveShadow)&&(Ae.receiveShadow=B.receiveShadow,mt.setValue(N,"receiveShadow",B.receiveShadow)),Y.isMeshGouraudMaterial&&Y.envMap!==null&&(Cn.envMap.value=we,Cn.flipEnvMap.value=we.isCubeTexture&&we.isRenderTargetTexture===!1?-1:1),Y.isMeshStandardMaterial&&Y.envMap===null&&O.environment!==null&&(Cn.envMapIntensity.value=O.environmentIntensity),tn&&(mt.setValue(N,"toneMappingExposure",_.toneMappingExposure),Ae.needsLights&&Gh(Cn,Ps),ce&&Y.fog===!0&&de.refreshFogUniforms(Cn,ce),de.refreshMaterialUniforms(Cn,Y,H,K,d.state.transmissionRenderTarget[w.id]),ns.upload(N,Tl(Ae),Cn,R)),Y.isShaderMaterial&&Y.uniformsNeedUpdate===!0&&(ns.upload(N,Tl(Ae),Cn,R),Y.uniformsNeedUpdate=!1),Y.isSpriteMaterial&&mt.setValue(N,"center",B.center),mt.setValue(N,"modelViewMatrix",B.modelViewMatrix),mt.setValue(N,"normalMatrix",B.normalMatrix),mt.setValue(N,"modelMatrix",B.matrixWorld),Y.isShaderMaterial||Y.isRawShaderMaterial){let un=Y.uniformsGroups;for(let ei=0,ti=un.length;ei<ti;ei++){let Rl=un[ei];U.update(Rl,_n),U.bind(Rl,_n)}}return _n}function Gh(w,O){w.ambientLightColor.needsUpdate=O,w.lightProbe.needsUpdate=O,w.directionalLights.needsUpdate=O,w.directionalLightShadows.needsUpdate=O,w.pointLights.needsUpdate=O,w.pointLightShadows.needsUpdate=O,w.spotLights.needsUpdate=O,w.spotLightShadows.needsUpdate=O,w.rectAreaLights.needsUpdate=O,w.hemisphereLights.needsUpdate=O}function Wh(w){return w.isMeshLambertMaterial||w.isMeshToonMaterial||w.isMeshPhongMaterial||w.isMeshStandardMaterial||w.isShadowMaterial||w.isShaderMaterial&&w.lights===!0}this.getActiveCubeFace=function(){return A},this.getActiveMipmapLevel=function(){return E},this.getRenderTarget=function(){return I},this.setRenderTargetTextures=function(w,O,q){Ie.get(w.texture).__webglTexture=O,Ie.get(w.depthTexture).__webglTexture=q;let Y=Ie.get(w);Y.__hasExternalTextures=!0,Y.__autoAllocateDepthBuffer=q===void 0,Y.__autoAllocateDepthBuffer||Ge.has("WEBGL_multisampled_render_to_texture")===!0&&(console.warn("THREE.WebGLRenderer: Render-to-texture extension was disabled because an external texture was provided"),Y.__useRenderToTexture=!1)},this.setRenderTargetFramebuffer=function(w,O){let q=Ie.get(w);q.__webglFramebuffer=O,q.__useDefaultFramebuffer=O===void 0},this.setRenderTarget=function(w,O=0,q=0){I=w,A=O,E=q;let Y=!0,B=null,ce=!1,me=!1;if(w){let we=Ie.get(w);if(we.__useDefaultFramebuffer!==void 0)Re.bindFramebuffer(N.FRAMEBUFFER,null),Y=!1;else if(we.__webglFramebuffer===void 0)R.setupRenderTarget(w);else if(we.__hasExternalTextures)R.rebindTextures(w,Ie.get(w.texture).__webglTexture,Ie.get(w.depthTexture).__webglTexture);else if(w.depthBuffer){let Ee=w.depthTexture;if(we.__boundDepthTexture!==Ee){if(Ee!==null&&Ie.has(Ee)&&(w.width!==Ee.image.width||w.height!==Ee.image.height))throw new Error("WebGLRenderTarget: Attached DepthTexture is initialized to the incorrect size.");R.setupDepthRenderbuffer(w)}}let Ne=w.texture;(Ne.isData3DTexture||Ne.isDataArrayTexture||Ne.isCompressedArrayTexture)&&(me=!0);let ze=Ie.get(w).__webglFramebuffer;w.isWebGLCubeRenderTarget?(Array.isArray(ze[O])?B=ze[O][q]:B=ze[O],ce=!0):w.samples>0&&R.useMultisampledRTT(w)===!1?B=Ie.get(w).__webglMultisampledFramebuffer:Array.isArray(ze)?B=ze[q]:B=ze,T.copy(w.viewport),L.copy(w.scissor),D=w.scissorTest}else T.copy(ie).multiplyScalar(H).floor(),L.copy(j).multiplyScalar(H).floor(),D=ue;if(Re.bindFramebuffer(N.FRAMEBUFFER,B)&&Y&&Re.drawBuffers(w,B),Re.viewport(T),Re.scissor(L),Re.setScissorTest(D),ce){let we=Ie.get(w.texture);N.framebufferTexture2D(N.FRAMEBUFFER,N.COLOR_ATTACHMENT0,N.TEXTURE_CUBE_MAP_POSITIVE_X+O,we.__webglTexture,q)}else if(me){let we=Ie.get(w.texture),Ne=O||0;N.framebufferTextureLayer(N.FRAMEBUFFER,N.COLOR_ATTACHMENT0,we.__webglTexture,q||0,Ne)}x=-1},this.readRenderTargetPixels=function(w,O,q,Y,B,ce,me){if(!(w&&w.isWebGLRenderTarget)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");return}let Se=Ie.get(w).__webglFramebuffer;if(w.isWebGLCubeRenderTarget&&me!==void 0&&(Se=Se[me]),Se){Re.bindFramebuffer(N.FRAMEBUFFER,Se);try{let we=w.texture,Ne=we.format,ze=we.type;if(!Oe.textureFormatReadable(Ne)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in RGBA or implementation defined format.");return}if(!Oe.textureTypeReadable(ze)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in UnsignedByteType or implementation defined type.");return}O>=0&&O<=w.width-Y&&q>=0&&q<=w.height-B&&N.readPixels(O,q,Y,B,He.convert(Ne),He.convert(ze),ce)}finally{let we=I!==null?Ie.get(I).__webglFramebuffer:null;Re.bindFramebuffer(N.FRAMEBUFFER,we)}}},this.readRenderTargetPixelsAsync=async function(w,O,q,Y,B,ce,me){if(!(w&&w.isWebGLRenderTarget))throw new Error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");let Se=Ie.get(w).__webglFramebuffer;if(w.isWebGLCubeRenderTarget&&me!==void 0&&(Se=Se[me]),Se){let we=w.texture,Ne=we.format,ze=we.type;if(!Oe.textureFormatReadable(Ne))throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in RGBA or implementation defined format.");if(!Oe.textureTypeReadable(ze))throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in UnsignedByteType or implementation defined type.");if(O>=0&&O<=w.width-Y&&q>=0&&q<=w.height-B){Re.bindFramebuffer(N.FRAMEBUFFER,Se);let Ee=N.createBuffer();N.bindBuffer(N.PIXEL_PACK_BUFFER,Ee),N.bufferData(N.PIXEL_PACK_BUFFER,ce.byteLength,N.STREAM_READ),N.readPixels(O,q,Y,B,He.convert(Ne),He.convert(ze),0);let tt=I!==null?Ie.get(I).__webglFramebuffer:null;Re.bindFramebuffer(N.FRAMEBUFFER,tt);let ft=N.fenceSync(N.SYNC_GPU_COMMANDS_COMPLETE,0);return N.flush(),await Kf(N,ft,4),N.bindBuffer(N.PIXEL_PACK_BUFFER,Ee),N.getBufferSubData(N.PIXEL_PACK_BUFFER,0,ce),N.deleteBuffer(Ee),N.deleteSync(ft),ce}else throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: requested read bounds are out of range.")}},this.copyFramebufferToTexture=function(w,O=null,q=0){w.isTexture!==!0&&(Hs("WebGLRenderer: copyFramebufferToTexture function signature has changed."),O=arguments[0]||null,w=arguments[1]);let Y=Math.pow(2,-q),B=Math.floor(w.image.width*Y),ce=Math.floor(w.image.height*Y),me=O!==null?O.x:0,Se=O!==null?O.y:0;R.setTexture2D(w,0),N.copyTexSubImage2D(N.TEXTURE_2D,q,0,0,me,Se,B,ce),Re.unbindTexture()},this.copyTextureToTexture=function(w,O,q=null,Y=null,B=0){w.isTexture!==!0&&(Hs("WebGLRenderer: copyTextureToTexture function signature has changed."),Y=arguments[0]||null,w=arguments[1],O=arguments[2],B=arguments[3]||0,q=null);let ce,me,Se,we,Ne,ze,Ee,tt,ft,pt=w.isCompressedTexture?w.mipmaps[B]:w.image;q!==null?(ce=q.max.x-q.min.x,me=q.max.y-q.min.y,Se=q.isBox3?q.max.z-q.min.z:1,we=q.min.x,Ne=q.min.y,ze=q.isBox3?q.min.z:0):(ce=pt.width,me=pt.height,Se=pt.depth||1,we=0,Ne=0,ze=0),Y!==null?(Ee=Y.x,tt=Y.y,ft=Y.z):(Ee=0,tt=0,ft=0);let jt=He.convert(O.format),rt=He.convert(O.type),Ae;O.isData3DTexture?(R.setTexture3D(O,0),Ae=N.TEXTURE_3D):O.isDataArrayTexture||O.isCompressedArrayTexture?(R.setTexture2DArray(O,0),Ae=N.TEXTURE_2D_ARRAY):(R.setTexture2D(O,0),Ae=N.TEXTURE_2D),N.pixelStorei(N.UNPACK_FLIP_Y_WEBGL,O.flipY),N.pixelStorei(N.UNPACK_PREMULTIPLY_ALPHA_WEBGL,O.premultiplyAlpha),N.pixelStorei(N.UNPACK_ALIGNMENT,O.unpackAlignment);let Fn=N.getParameter(N.UNPACK_ROW_LENGTH),ot=N.getParameter(N.UNPACK_IMAGE_HEIGHT),_n=N.getParameter(N.UNPACK_SKIP_PIXELS),Ni=N.getParameter(N.UNPACK_SKIP_ROWS),tn=N.getParameter(N.UNPACK_SKIP_IMAGES);N.pixelStorei(N.UNPACK_ROW_LENGTH,pt.width),N.pixelStorei(N.UNPACK_IMAGE_HEIGHT,pt.height),N.pixelStorei(N.UNPACK_SKIP_PIXELS,we),N.pixelStorei(N.UNPACK_SKIP_ROWS,Ne),N.pixelStorei(N.UNPACK_SKIP_IMAGES,ze);let Ps=w.isDataArrayTexture||w.isData3DTexture,mt=O.isDataArrayTexture||O.isData3DTexture;if(w.isRenderTargetTexture||w.isDepthTexture){let Cn=Ie.get(w),Ls=Ie.get(O),un=Ie.get(Cn.__renderTarget),ei=Ie.get(Ls.__renderTarget);Re.bindFramebuffer(N.READ_FRAMEBUFFER,un.__webglFramebuffer),Re.bindFramebuffer(N.DRAW_FRAMEBUFFER,ei.__webglFramebuffer);for(let ti=0;ti<Se;ti++)Ps&&N.framebufferTextureLayer(N.READ_FRAMEBUFFER,N.COLOR_ATTACHMENT0,Ie.get(w).__webglTexture,B,ze+ti),w.isDepthTexture?(mt&&N.framebufferTextureLayer(N.DRAW_FRAMEBUFFER,N.COLOR_ATTACHMENT0,Ie.get(O).__webglTexture,B,ft+ti),N.blitFramebuffer(we,Ne,ce,me,Ee,tt,ce,me,N.DEPTH_BUFFER_BIT,N.NEAREST)):mt?N.copyTexSubImage3D(Ae,B,Ee,tt,ft+ti,we,Ne,ce,me):N.copyTexSubImage2D(Ae,B,Ee,tt,ft+ti,we,Ne,ce,me);Re.bindFramebuffer(N.READ_FRAMEBUFFER,null),Re.bindFramebuffer(N.DRAW_FRAMEBUFFER,null)}else mt?w.isDataTexture||w.isData3DTexture?N.texSubImage3D(Ae,B,Ee,tt,ft,ce,me,Se,jt,rt,pt.data):O.isCompressedArrayTexture?N.compressedTexSubImage3D(Ae,B,Ee,tt,ft,ce,me,Se,jt,pt.data):N.texSubImage3D(Ae,B,Ee,tt,ft,ce,me,Se,jt,rt,pt):w.isDataTexture?N.texSubImage2D(N.TEXTURE_2D,B,Ee,tt,ce,me,jt,rt,pt.data):w.isCompressedTexture?N.compressedTexSubImage2D(N.TEXTURE_2D,B,Ee,tt,pt.width,pt.height,jt,pt.data):N.texSubImage2D(N.TEXTURE_2D,B,Ee,tt,ce,me,jt,rt,pt);N.pixelStorei(N.UNPACK_ROW_LENGTH,Fn),N.pixelStorei(N.UNPACK_IMAGE_HEIGHT,ot),N.pixelStorei(N.UNPACK_SKIP_PIXELS,_n),N.pixelStorei(N.UNPACK_SKIP_ROWS,Ni),N.pixelStorei(N.UNPACK_SKIP_IMAGES,tn),B===0&&O.generateMipmaps&&N.generateMipmap(Ae),Re.unbindTexture()},this.copyTextureToTexture3D=function(w,O,q=null,Y=null,B=0){return w.isTexture!==!0&&(Hs("WebGLRenderer: copyTextureToTexture3D function signature has changed."),q=arguments[0]||null,Y=arguments[1]||null,w=arguments[2],O=arguments[3],B=arguments[4]||0),Hs('WebGLRenderer: copyTextureToTexture3D function has been deprecated. Use "copyTextureToTexture" instead.'),this.copyTextureToTexture(w,O,q,Y,B)},this.initRenderTarget=function(w){Ie.get(w).__webglFramebuffer===void 0&&R.setupRenderTarget(w)},this.initTexture=function(w){w.isCubeTexture?R.setTextureCube(w,0):w.isData3DTexture?R.setTexture3D(w,0):w.isDataArrayTexture||w.isCompressedArrayTexture?R.setTexture2DArray(w,0):R.setTexture2D(w,0),Re.unbindTexture()},this.resetState=function(){A=0,E=0,I=null,Re.reset(),ht.reset()},typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}get coordinateSystem(){return Wn}get outputColorSpace(){return this._outputColorSpace}set outputColorSpace(e){this._outputColorSpace=e;let t=this.getContext();t.drawingBufferColorspace=Ye._getDrawingBufferColorSpace(e),t.unpackColorSpace=Ye._getUnpackColorSpace()}};var Et=class extends gt{constructor(){super(),this.isScene=!0,this.type="Scene",this.background=null,this.environment=null,this.fog=null,this.backgroundBlurriness=0,this.backgroundIntensity=1,this.backgroundRotation=new pn,this.environmentIntensity=1,this.environmentRotation=new pn,this.overrideMaterial=null,typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}copy(e,t){return super.copy(e,t),e.background!==null&&(this.background=e.background.clone()),e.environment!==null&&(this.environment=e.environment.clone()),e.fog!==null&&(this.fog=e.fog.clone()),this.backgroundBlurriness=e.backgroundBlurriness,this.backgroundIntensity=e.backgroundIntensity,this.backgroundRotation.copy(e.backgroundRotation),this.environmentIntensity=e.environmentIntensity,this.environmentRotation.copy(e.environmentRotation),e.overrideMaterial!==null&&(this.overrideMaterial=e.overrideMaterial.clone()),this.matrixAutoUpdate=e.matrixAutoUpdate,this}toJSON(e){let t=super.toJSON(e);return this.fog!==null&&(t.object.fog=this.fog.toJSON()),this.backgroundBlurriness>0&&(t.object.backgroundBlurriness=this.backgroundBlurriness),this.backgroundIntensity!==1&&(t.object.backgroundIntensity=this.backgroundIntensity),t.object.backgroundRotation=this.backgroundRotation.toArray(),this.environmentIntensity!==1&&(t.object.environmentIntensity=this.environmentIntensity),t.object.environmentRotation=this.environmentRotation.toArray(),t}},Js=class{constructor(e,t){this.isInterleavedBuffer=!0,this.array=e,this.stride=t,this.count=e!==void 0?e.length/t:0,this.usage=Ha,this.updateRanges=[],this.version=0,this.uuid=An()}onUploadCallback(){}set needsUpdate(e){e===!0&&this.version++}setUsage(e){return this.usage=e,this}addUpdateRange(e,t){this.updateRanges.push({start:e,count:t})}clearUpdateRanges(){this.updateRanges.length=0}copy(e){return this.array=new e.array.constructor(e.array),this.count=e.count,this.stride=e.stride,this.usage=e.usage,this}copyAt(e,t,n){e*=this.stride,n*=t.stride;for(let i=0,r=this.stride;i<r;i++)this.array[e+i]=t.array[n+i];return this}set(e,t=0){return this.array.set(e,t),this}clone(e){e.arrayBuffers===void 0&&(e.arrayBuffers={}),this.array.buffer._uuid===void 0&&(this.array.buffer._uuid=An()),e.arrayBuffers[this.array.buffer._uuid]===void 0&&(e.arrayBuffers[this.array.buffer._uuid]=this.array.slice(0).buffer);let t=new this.array.constructor(e.arrayBuffers[this.array.buffer._uuid]),n=new this.constructor(t,this.stride);return n.setUsage(this.usage),n}onUpload(e){return this.onUploadCallback=e,this}toJSON(e){return e.arrayBuffers===void 0&&(e.arrayBuffers={}),this.array.buffer._uuid===void 0&&(this.array.buffer._uuid=An()),e.arrayBuffers[this.array.buffer._uuid]===void 0&&(e.arrayBuffers[this.array.buffer._uuid]=Array.from(new Uint32Array(this.array.buffer))),{uuid:this.uuid,buffer:this.array.buffer._uuid,type:this.array.constructor.name,stride:this.stride}}},Xt=new P,js=class s{constructor(e,t,n,i=!1){this.isInterleavedBufferAttribute=!0,this.name="",this.data=e,this.itemSize=t,this.offset=n,this.normalized=i}get count(){return this.data.count}get array(){return this.data.array}set needsUpdate(e){this.data.needsUpdate=e}applyMatrix4(e){for(let t=0,n=this.data.count;t<n;t++)Xt.fromBufferAttribute(this,t),Xt.applyMatrix4(e),this.setXYZ(t,Xt.x,Xt.y,Xt.z);return this}applyNormalMatrix(e){for(let t=0,n=this.count;t<n;t++)Xt.fromBufferAttribute(this,t),Xt.applyNormalMatrix(e),this.setXYZ(t,Xt.x,Xt.y,Xt.z);return this}transformDirection(e){for(let t=0,n=this.count;t<n;t++)Xt.fromBufferAttribute(this,t),Xt.transformDirection(e),this.setXYZ(t,Xt.x,Xt.y,Xt.z);return this}getComponent(e,t){let n=this.array[e*this.data.stride+this.offset+t];return this.normalized&&(n=wn(n,this.array)),n}setComponent(e,t,n){return this.normalized&&(n=ct(n,this.array)),this.data.array[e*this.data.stride+this.offset+t]=n,this}setX(e,t){return this.normalized&&(t=ct(t,this.array)),this.data.array[e*this.data.stride+this.offset]=t,this}setY(e,t){return this.normalized&&(t=ct(t,this.array)),this.data.array[e*this.data.stride+this.offset+1]=t,this}setZ(e,t){return this.normalized&&(t=ct(t,this.array)),this.data.array[e*this.data.stride+this.offset+2]=t,this}setW(e,t){return this.normalized&&(t=ct(t,this.array)),this.data.array[e*this.data.stride+this.offset+3]=t,this}getX(e){let t=this.data.array[e*this.data.stride+this.offset];return this.normalized&&(t=wn(t,this.array)),t}getY(e){let t=this.data.array[e*this.data.stride+this.offset+1];return this.normalized&&(t=wn(t,this.array)),t}getZ(e){let t=this.data.array[e*this.data.stride+this.offset+2];return this.normalized&&(t=wn(t,this.array)),t}getW(e){let t=this.data.array[e*this.data.stride+this.offset+3];return this.normalized&&(t=wn(t,this.array)),t}setXY(e,t,n){return e=e*this.data.stride+this.offset,this.normalized&&(t=ct(t,this.array),n=ct(n,this.array)),this.data.array[e+0]=t,this.data.array[e+1]=n,this}setXYZ(e,t,n,i){return e=e*this.data.stride+this.offset,this.normalized&&(t=ct(t,this.array),n=ct(n,this.array),i=ct(i,this.array)),this.data.array[e+0]=t,this.data.array[e+1]=n,this.data.array[e+2]=i,this}setXYZW(e,t,n,i,r){return e=e*this.data.stride+this.offset,this.normalized&&(t=ct(t,this.array),n=ct(n,this.array),i=ct(i,this.array),r=ct(r,this.array)),this.data.array[e+0]=t,this.data.array[e+1]=n,this.data.array[e+2]=i,this.data.array[e+3]=r,this}clone(e){if(e===void 0){console.log("THREE.InterleavedBufferAttribute.clone(): Cloning an interleaved buffer attribute will de-interleave buffer data.");let t=[];for(let n=0;n<this.count;n++){let i=n*this.data.stride+this.offset;for(let r=0;r<this.itemSize;r++)t.push(this.data.array[i+r])}return new it(new this.array.constructor(t),this.itemSize,this.normalized)}else return e.interleavedBuffers===void 0&&(e.interleavedBuffers={}),e.interleavedBuffers[this.data.uuid]===void 0&&(e.interleavedBuffers[this.data.uuid]=this.data.clone(e)),new s(e.interleavedBuffers[this.data.uuid],this.itemSize,this.offset,this.normalized)}toJSON(e){if(e===void 0){console.log("THREE.InterleavedBufferAttribute.toJSON(): Serializing an interleaved buffer attribute will de-interleave buffer data.");let t=[];for(let n=0;n<this.count;n++){let i=n*this.data.stride+this.offset;for(let r=0;r<this.itemSize;r++)t.push(this.data.array[i+r])}return{itemSize:this.itemSize,type:this.array.constructor.name,array:t,normalized:this.normalized}}else return e.interleavedBuffers===void 0&&(e.interleavedBuffers={}),e.interleavedBuffers[this.data.uuid]===void 0&&(e.interleavedBuffers[this.data.uuid]=this.data.toJSON(e)),{isInterleavedBufferAttribute:!0,itemSize:this.itemSize,data:this.data.uuid,offset:this.offset,normalized:this.normalized}}};var Cu=new P,Iu=new We,Pu=new We,qg=new P,Lu=new Le,Ur=new P,Qo=new on,Du=new Le,ea=new fs,gs=class extends Fe{constructor(e,t){super(e,t),this.isSkinnedMesh=!0,this.type="SkinnedMesh",this.bindMode=Ll,this.bindMatrix=new Le,this.bindMatrixInverse=new Le,this.boundingBox=null,this.boundingSphere=null}computeBoundingBox(){let e=this.geometry;this.boundingBox===null&&(this.boundingBox=new dn),this.boundingBox.makeEmpty();let t=e.getAttribute("position");for(let n=0;n<t.count;n++)this.getVertexPosition(n,Ur),this.boundingBox.expandByPoint(Ur)}computeBoundingSphere(){let e=this.geometry;this.boundingSphere===null&&(this.boundingSphere=new on),this.boundingSphere.makeEmpty();let t=e.getAttribute("position");for(let n=0;n<t.count;n++)this.getVertexPosition(n,Ur),this.boundingSphere.expandByPoint(Ur)}copy(e,t){return super.copy(e,t),this.bindMode=e.bindMode,this.bindMatrix.copy(e.bindMatrix),this.bindMatrixInverse.copy(e.bindMatrixInverse),this.skeleton=e.skeleton,e.boundingBox!==null&&(this.boundingBox=e.boundingBox.clone()),e.boundingSphere!==null&&(this.boundingSphere=e.boundingSphere.clone()),this}raycast(e,t){let n=this.material,i=this.matrixWorld;n!==void 0&&(this.boundingSphere===null&&this.computeBoundingSphere(),Qo.copy(this.boundingSphere),Qo.applyMatrix4(i),e.ray.intersectsSphere(Qo)!==!1&&(Du.copy(i).invert(),ea.copy(e.ray).applyMatrix4(Du),!(this.boundingBox!==null&&ea.intersectsBox(this.boundingBox)===!1)&&this._computeIntersections(e,t,ea)))}getVertexPosition(e,t){return super.getVertexPosition(e,t),this.applyBoneTransform(e,t),t}bind(e,t){this.skeleton=e,t===void 0&&(this.updateMatrixWorld(!0),this.skeleton.calculateInverses(),t=this.matrixWorld),this.bindMatrix.copy(t),this.bindMatrixInverse.copy(t).invert()}pose(){this.skeleton.pose()}normalizeSkinWeights(){let e=new We,t=this.geometry.attributes.skinWeight;for(let n=0,i=t.count;n<i;n++){e.fromBufferAttribute(t,n);let r=1/e.manhattanLength();r!==1/0?e.multiplyScalar(r):e.set(1,0,0,0),t.setXYZW(n,e.x,e.y,e.z,e.w)}}updateMatrixWorld(e){super.updateMatrixWorld(e),this.bindMode===Ll?this.bindMatrixInverse.copy(this.matrixWorld).invert():this.bindMode===Mf?this.bindMatrixInverse.copy(this.bindMatrix).invert():console.warn("THREE.SkinnedMesh: Unrecognized bindMode: "+this.bindMode)}applyBoneTransform(e,t){let n=this.skeleton,i=this.geometry;Iu.fromBufferAttribute(i.attributes.skinIndex,e),Pu.fromBufferAttribute(i.attributes.skinWeight,e),Cu.copy(t).applyMatrix4(this.bindMatrix),t.set(0,0,0);for(let r=0;r<4;r++){let o=Pu.getComponent(r);if(o!==0){let a=Iu.getComponent(r);Lu.multiplyMatrices(n.bones[a].matrixWorld,n.boneInverses[a]),t.addScaledVector(qg.copy(Cu).applyMatrix4(Lu),o)}}return t.applyMatrix4(this.bindMatrixInverse)}},Qs=class extends gt{constructor(){super(),this.isBone=!0,this.type="Bone"}},vs=class extends Pt{constructor(e=null,t=1,n=1,i,r,o,a,c,l=yt,u=yt,h,f){super(null,o,a,c,l,u,i,r,h,f),this.isDataTexture=!0,this.image={data:e,width:t,height:n},this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}},Uu=new Le,Yg=new Le,to=class s{constructor(e=[],t=[]){this.uuid=An(),this.bones=e.slice(0),this.boneInverses=t,this.boneMatrices=null,this.boneTexture=null,this.init()}init(){let e=this.bones,t=this.boneInverses;if(this.boneMatrices=new Float32Array(e.length*16),t.length===0)this.calculateInverses();else if(e.length!==t.length){console.warn("THREE.Skeleton: Number of inverse bone matrices does not match amount of bones."),this.boneInverses=[];for(let n=0,i=this.bones.length;n<i;n++)this.boneInverses.push(new Le)}}calculateInverses(){this.boneInverses.length=0;for(let e=0,t=this.bones.length;e<t;e++){let n=new Le;this.bones[e]&&n.copy(this.bones[e].matrixWorld).invert(),this.boneInverses.push(n)}}pose(){for(let e=0,t=this.bones.length;e<t;e++){let n=this.bones[e];n&&n.matrixWorld.copy(this.boneInverses[e]).invert()}for(let e=0,t=this.bones.length;e<t;e++){let n=this.bones[e];n&&(n.parent&&n.parent.isBone?(n.matrix.copy(n.parent.matrixWorld).invert(),n.matrix.multiply(n.matrixWorld)):n.matrix.copy(n.matrixWorld),n.matrix.decompose(n.position,n.quaternion,n.scale))}}update(){let e=this.bones,t=this.boneInverses,n=this.boneMatrices,i=this.boneTexture;for(let r=0,o=e.length;r<o;r++){let a=e[r]?e[r].matrixWorld:Yg;Uu.multiplyMatrices(a,t[r]),Uu.toArray(n,r*16)}i!==null&&(i.needsUpdate=!0)}clone(){return new s(this.bones,this.boneInverses)}computeBoneTexture(){let e=Math.sqrt(this.bones.length*4);e=Math.ceil(e/4)*4,e=Math.max(e,4);let t=new Float32Array(e*e*4);t.set(this.boneMatrices);let n=new vs(t,e,e,Ht,Tn);return n.needsUpdate=!0,this.boneMatrices=t,this.boneTexture=n,this}getBoneByName(e){for(let t=0,n=this.bones.length;t<n;t++){let i=this.bones[t];if(i.name===e)return i}}dispose(){this.boneTexture!==null&&(this.boneTexture.dispose(),this.boneTexture=null)}fromJSON(e,t){this.uuid=e.uuid;for(let n=0,i=e.bones.length;n<i;n++){let r=e.bones[n],o=t[r];o===void 0&&(console.warn("THREE.Skeleton: No bone found with UUID:",r),o=new Qs),this.bones.push(o),this.boneInverses.push(new Le().fromArray(e.boneInverses[n]))}return this.init(),this}toJSON(){let e={metadata:{version:4.6,type:"Skeleton",generator:"Skeleton.toJSON"},bones:[],boneInverses:[]};e.uuid=this.uuid;let t=this.bones,n=this.boneInverses;for(let i=0,r=t.length;i<r;i++){let o=t[i];e.bones.push(o.uuid);let a=n[i];e.boneInverses.push(a.toArray())}return e}},Di=class extends it{constructor(e,t,n,i=1){super(e,t,n),this.isInstancedBufferAttribute=!0,this.meshPerAttribute=i}copy(e){return super.copy(e),this.meshPerAttribute=e.meshPerAttribute,this}toJSON(){let e=super.toJSON();return e.meshPerAttribute=this.meshPerAttribute,e.isInstancedBufferAttribute=!0,e}},Ki=new Le,Nu=new Le,Nr=[],Fu=new dn,$g=new Le,Os=new Fe,Bs=new on,xs=class extends Fe{constructor(e,t,n){super(e,t),this.isInstancedMesh=!0,this.instanceMatrix=new Di(new Float32Array(n*16),16),this.instanceColor=null,this.morphTexture=null,this.count=n,this.boundingBox=null,this.boundingSphere=null;for(let i=0;i<n;i++)this.setMatrixAt(i,$g)}computeBoundingBox(){let e=this.geometry,t=this.count;this.boundingBox===null&&(this.boundingBox=new dn),e.boundingBox===null&&e.computeBoundingBox(),this.boundingBox.makeEmpty();for(let n=0;n<t;n++)this.getMatrixAt(n,Ki),Fu.copy(e.boundingBox).applyMatrix4(Ki),this.boundingBox.union(Fu)}computeBoundingSphere(){let e=this.geometry,t=this.count;this.boundingSphere===null&&(this.boundingSphere=new on),e.boundingSphere===null&&e.computeBoundingSphere(),this.boundingSphere.makeEmpty();for(let n=0;n<t;n++)this.getMatrixAt(n,Ki),Bs.copy(e.boundingSphere).applyMatrix4(Ki),this.boundingSphere.union(Bs)}copy(e,t){return super.copy(e,t),this.instanceMatrix.copy(e.instanceMatrix),e.morphTexture!==null&&(this.morphTexture=e.morphTexture.clone()),e.instanceColor!==null&&(this.instanceColor=e.instanceColor.clone()),this.count=e.count,e.boundingBox!==null&&(this.boundingBox=e.boundingBox.clone()),e.boundingSphere!==null&&(this.boundingSphere=e.boundingSphere.clone()),this}getColorAt(e,t){t.fromArray(this.instanceColor.array,e*3)}getMatrixAt(e,t){t.fromArray(this.instanceMatrix.array,e*16)}getMorphAt(e,t){let n=t.morphTargetInfluences,i=this.morphTexture.source.data.data,r=n.length+1,o=e*r+1;for(let a=0;a<n.length;a++)n[a]=i[o+a]}raycast(e,t){let n=this.matrixWorld,i=this.count;if(Os.geometry=this.geometry,Os.material=this.material,Os.material!==void 0&&(this.boundingSphere===null&&this.computeBoundingSphere(),Bs.copy(this.boundingSphere),Bs.applyMatrix4(n),e.ray.intersectsSphere(Bs)!==!1))for(let r=0;r<i;r++){this.getMatrixAt(r,Ki),Nu.multiplyMatrices(n,Ki),Os.matrixWorld=Nu,Os.raycast(e,Nr);for(let o=0,a=Nr.length;o<a;o++){let c=Nr[o];c.instanceId=r,c.object=this,t.push(c)}Nr.length=0}}setColorAt(e,t){this.instanceColor===null&&(this.instanceColor=new Di(new Float32Array(this.instanceMatrix.count*3).fill(1),3)),t.toArray(this.instanceColor.array,e*3)}setMatrixAt(e,t){t.toArray(this.instanceMatrix.array,e*16)}setMorphAt(e,t){let n=t.morphTargetInfluences,i=n.length+1;this.morphTexture===null&&(this.morphTexture=new vs(new Float32Array(i*this.count),i,this.count,bc,Tn));let r=this.morphTexture.source.data.data,o=0;for(let l=0;l<n.length;l++)o+=n[l];let a=this.geometry.morphTargetsRelative?1:1-o,c=i*e;r[c]=a,r.set(n,c+1)}updateMorphTargets(){}dispose(){return this.dispatchEvent({type:"dispose"}),this.morphTexture!==null&&(this.morphTexture.dispose(),this.morphTexture=null),this}};var er=class extends an{static get type(){return"LineBasicMaterial"}constructor(e){super(),this.isLineBasicMaterial=!0,this.color=new ve(16777215),this.map=null,this.linewidth=1,this.linecap="round",this.linejoin="round",this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.color.copy(e.color),this.map=e.map,this.linewidth=e.linewidth,this.linecap=e.linecap,this.linejoin=e.linejoin,this.fog=e.fog,this}},no=new P,io=new P,Ou=new Le,zs=new fs,Fr=new on,ta=new P,Bu=new P,_s=class extends gt{constructor(e=new Mt,t=new er){super(),this.isLine=!0,this.type="Line",this.geometry=e,this.material=t,this.updateMorphTargets()}copy(e,t){return super.copy(e,t),this.material=Array.isArray(e.material)?e.material.slice():e.material,this.geometry=e.geometry,this}computeLineDistances(){let e=this.geometry;if(e.index===null){let t=e.attributes.position,n=[0];for(let i=1,r=t.count;i<r;i++)no.fromBufferAttribute(t,i-1),io.fromBufferAttribute(t,i),n[i]=n[i-1],n[i]+=no.distanceTo(io);e.setAttribute("lineDistance",new nt(n,1))}else console.warn("THREE.Line.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}raycast(e,t){let n=this.geometry,i=this.matrixWorld,r=e.params.Line.threshold,o=n.drawRange;if(n.boundingSphere===null&&n.computeBoundingSphere(),Fr.copy(n.boundingSphere),Fr.applyMatrix4(i),Fr.radius+=r,e.ray.intersectsSphere(Fr)===!1)return;Ou.copy(i).invert(),zs.copy(e.ray).applyMatrix4(Ou);let a=r/((this.scale.x+this.scale.y+this.scale.z)/3),c=a*a,l=this.isLineSegments?2:1,u=n.index,f=n.attributes.position;if(u!==null){let p=Math.max(0,o.start),g=Math.min(u.count,o.start+o.count);for(let v=p,m=g-1;v<m;v+=l){let d=u.getX(v),M=u.getX(v+1),b=Or(this,e,zs,c,d,M);b&&t.push(b)}if(this.isLineLoop){let v=u.getX(g-1),m=u.getX(p),d=Or(this,e,zs,c,v,m);d&&t.push(d)}}else{let p=Math.max(0,o.start),g=Math.min(f.count,o.start+o.count);for(let v=p,m=g-1;v<m;v+=l){let d=Or(this,e,zs,c,v,v+1);d&&t.push(d)}if(this.isLineLoop){let v=Or(this,e,zs,c,g-1,p);v&&t.push(v)}}}updateMorphTargets(){let t=this.geometry.morphAttributes,n=Object.keys(t);if(n.length>0){let i=t[n[0]];if(i!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,o=i.length;r<o;r++){let a=i[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[a]=r}}}}};function Or(s,e,t,n,i,r){let o=s.geometry.attributes.position;if(no.fromBufferAttribute(o,i),io.fromBufferAttribute(o,r),t.distanceSqToSegment(no,io,ta,Bu)>n)return;ta.applyMatrix4(s.matrixWorld);let c=e.ray.origin.distanceTo(ta);if(!(c<e.near||c>e.far))return{distance:c,point:Bu.clone().applyMatrix4(s.matrixWorld),index:i,face:null,faceIndex:null,barycoord:null,object:s}}var zu=new P,ku=new P,so=class extends _s{constructor(e,t){super(e,t),this.isLineSegments=!0,this.type="LineSegments"}computeLineDistances(){let e=this.geometry;if(e.index===null){let t=e.attributes.position,n=[];for(let i=0,r=t.count;i<r;i+=2)zu.fromBufferAttribute(t,i),ku.fromBufferAttribute(t,i+1),n[i]=i===0?0:n[i-1],n[i+1]=n[i]+zu.distanceTo(ku);e.setAttribute("lineDistance",new nt(n,1))}else console.warn("THREE.LineSegments.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}},ro=class extends _s{constructor(e,t){super(e,t),this.isLineLoop=!0,this.type="LineLoop"}},tr=class extends an{static get type(){return"PointsMaterial"}constructor(e){super(),this.isPointsMaterial=!0,this.color=new ve(16777215),this.map=null,this.alphaMap=null,this.size=1,this.sizeAttenuation=!0,this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.color.copy(e.color),this.map=e.map,this.alphaMap=e.alphaMap,this.size=e.size,this.sizeAttenuation=e.sizeAttenuation,this.fog=e.fog,this}},Hu=new Le,sc=new fs,Br=new on,zr=new P,oo=class extends gt{constructor(e=new Mt,t=new tr){super(),this.isPoints=!0,this.type="Points",this.geometry=e,this.material=t,this.updateMorphTargets()}copy(e,t){return super.copy(e,t),this.material=Array.isArray(e.material)?e.material.slice():e.material,this.geometry=e.geometry,this}raycast(e,t){let n=this.geometry,i=this.matrixWorld,r=e.params.Points.threshold,o=n.drawRange;if(n.boundingSphere===null&&n.computeBoundingSphere(),Br.copy(n.boundingSphere),Br.applyMatrix4(i),Br.radius+=r,e.ray.intersectsSphere(Br)===!1)return;Hu.copy(i).invert(),sc.copy(e.ray).applyMatrix4(Hu);let a=r/((this.scale.x+this.scale.y+this.scale.z)/3),c=a*a,l=n.index,h=n.attributes.position;if(l!==null){let f=Math.max(0,o.start),p=Math.min(l.count,o.start+o.count);for(let g=f,v=p;g<v;g++){let m=l.getX(g);zr.fromBufferAttribute(h,m),Vu(zr,m,c,i,e,t,this)}}else{let f=Math.max(0,o.start),p=Math.min(h.count,o.start+o.count);for(let g=f,v=p;g<v;g++)zr.fromBufferAttribute(h,g),Vu(zr,g,c,i,e,t,this)}}updateMorphTargets(){let t=this.geometry.morphAttributes,n=Object.keys(t);if(n.length>0){let i=t[n[0]];if(i!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,o=i.length;r<o;r++){let a=i[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[a]=r}}}}};function Vu(s,e,t,n,i,r,o){let a=sc.distanceSqToPoint(s);if(a<t){let c=new P;sc.closestPointToPoint(s,c),c.applyMatrix4(n);let l=i.ray.origin.distanceTo(c);if(l<i.near||l>i.far)return;r.push({distance:l,distanceToRay:Math.sqrt(a),point:c,index:e,face:null,faceIndex:null,barycoord:null,object:o})}}var ao=class extends Pt{constructor(e,t,n,i,r,o,a,c,l){super(e,t,n,i,r,o,a,c,l),this.isCanvasTexture=!0,this.needsUpdate=!0}};var Zt=class s extends Mt{constructor(e=1,t=1,n=1,i=32,r=1,o=!1,a=0,c=Math.PI*2){super(),this.type="CylinderGeometry",this.parameters={radiusTop:e,radiusBottom:t,height:n,radialSegments:i,heightSegments:r,openEnded:o,thetaStart:a,thetaLength:c};let l=this;i=Math.floor(i),r=Math.floor(r);let u=[],h=[],f=[],p=[],g=0,v=[],m=n/2,d=0;M(),o===!1&&(e>0&&b(!0),t>0&&b(!1)),this.setIndex(u),this.setAttribute("position",new nt(h,3)),this.setAttribute("normal",new nt(f,3)),this.setAttribute("uv",new nt(p,2));function M(){let _=new P,C=new P,A=0,E=(t-e)/n;for(let I=0;I<=r;I++){let x=[],y=I/r,T=y*(t-e)+e;for(let L=0;L<=i;L++){let D=L/i,F=D*c+a,X=Math.sin(F),z=Math.cos(F);C.x=T*X,C.y=-y*n+m,C.z=T*z,h.push(C.x,C.y,C.z),_.set(X,E,z).normalize(),f.push(_.x,_.y,_.z),p.push(D,1-y),x.push(g++)}v.push(x)}for(let I=0;I<i;I++)for(let x=0;x<r;x++){let y=v[x][I],T=v[x+1][I],L=v[x+1][I+1],D=v[x][I+1];(e>0||x!==0)&&(u.push(y,T,D),A+=3),(t>0||x!==r-1)&&(u.push(T,L,D),A+=3)}l.addGroup(d,A,0),d+=A}function b(_){let C=g,A=new le,E=new P,I=0,x=_===!0?e:t,y=_===!0?1:-1;for(let L=1;L<=i;L++)h.push(0,m*y,0),f.push(0,y,0),p.push(.5,.5),g++;let T=g;for(let L=0;L<=i;L++){let F=L/i*c+a,X=Math.cos(F),z=Math.sin(F);E.x=x*z,E.y=m*y,E.z=x*X,h.push(E.x,E.y,E.z),f.push(0,y,0),A.x=X*.5+.5,A.y=z*.5*y+.5,p.push(A.x,A.y),g++}for(let L=0;L<i;L++){let D=C+L,F=T+L;_===!0?u.push(F,F+1,D):u.push(F+1,F,D),I+=3}l.addGroup(d,I,_===!0?1:2),d+=I}}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new s(e.radiusTop,e.radiusBottom,e.height,e.radialSegments,e.heightSegments,e.openEnded,e.thetaStart,e.thetaLength)}},co=class s extends Zt{constructor(e=1,t=1,n=32,i=1,r=!1,o=0,a=Math.PI*2){super(0,e,t,n,i,r,o,a),this.type="ConeGeometry",this.parameters={radius:e,height:t,radialSegments:n,heightSegments:i,openEnded:r,thetaStart:o,thetaLength:a}}static fromJSON(e){return new s(e.radius,e.height,e.radialSegments,e.heightSegments,e.openEnded,e.thetaStart,e.thetaLength)}};var nr=class s extends Mt{constructor(e=.5,t=1,n=32,i=1,r=0,o=Math.PI*2){super(),this.type="RingGeometry",this.parameters={innerRadius:e,outerRadius:t,thetaSegments:n,phiSegments:i,thetaStart:r,thetaLength:o},n=Math.max(3,n),i=Math.max(1,i);let a=[],c=[],l=[],u=[],h=e,f=(t-e)/i,p=new P,g=new le;for(let v=0;v<=i;v++){for(let m=0;m<=n;m++){let d=r+m/n*o;p.x=h*Math.cos(d),p.y=h*Math.sin(d),c.push(p.x,p.y,p.z),l.push(0,0,1),g.x=(p.x/t+1)/2,g.y=(p.y/t+1)/2,u.push(g.x,g.y)}h+=f}for(let v=0;v<i;v++){let m=v*(n+1);for(let d=0;d<n;d++){let M=d+m,b=M,_=M+n+1,C=M+n+2,A=M+1;a.push(b,_,A),a.push(_,C,A)}}this.setIndex(a),this.setAttribute("position",new nt(c,3)),this.setAttribute("normal",new nt(l,3)),this.setAttribute("uv",new nt(u,2))}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new s(e.innerRadius,e.outerRadius,e.thetaSegments,e.phiSegments,e.thetaStart,e.thetaLength)}};var Dn=class extends an{static get type(){return"MeshStandardMaterial"}constructor(e){super(),this.isMeshStandardMaterial=!0,this.defines={STANDARD:""},this.color=new ve(16777215),this.roughness=1,this.metalness=0,this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.emissive=new ve(0),this.emissiveIntensity=1,this.emissiveMap=null,this.bumpMap=null,this.bumpScale=1,this.normalMap=null,this.normalMapType=oh,this.normalScale=new le(1,1),this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.roughnessMap=null,this.metalnessMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new pn,this.envMapIntensity=1,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.flatShading=!1,this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.defines={STANDARD:""},this.color.copy(e.color),this.roughness=e.roughness,this.metalness=e.metalness,this.map=e.map,this.lightMap=e.lightMap,this.lightMapIntensity=e.lightMapIntensity,this.aoMap=e.aoMap,this.aoMapIntensity=e.aoMapIntensity,this.emissive.copy(e.emissive),this.emissiveMap=e.emissiveMap,this.emissiveIntensity=e.emissiveIntensity,this.bumpMap=e.bumpMap,this.bumpScale=e.bumpScale,this.normalMap=e.normalMap,this.normalMapType=e.normalMapType,this.normalScale.copy(e.normalScale),this.displacementMap=e.displacementMap,this.displacementScale=e.displacementScale,this.displacementBias=e.displacementBias,this.roughnessMap=e.roughnessMap,this.metalnessMap=e.metalnessMap,this.alphaMap=e.alphaMap,this.envMap=e.envMap,this.envMapRotation.copy(e.envMapRotation),this.envMapIntensity=e.envMapIntensity,this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this.wireframeLinecap=e.wireframeLinecap,this.wireframeLinejoin=e.wireframeLinejoin,this.flatShading=e.flatShading,this.fog=e.fog,this}},xt=class extends Dn{static get type(){return"MeshPhysicalMaterial"}constructor(e){super(),this.isMeshPhysicalMaterial=!0,this.defines={STANDARD:"",PHYSICAL:""},this.anisotropyRotation=0,this.anisotropyMap=null,this.clearcoatMap=null,this.clearcoatRoughness=0,this.clearcoatRoughnessMap=null,this.clearcoatNormalScale=new le(1,1),this.clearcoatNormalMap=null,this.ior=1.5,Object.defineProperty(this,"reflectivity",{get:function(){return kt(2.5*(this.ior-1)/(this.ior+1),0,1)},set:function(t){this.ior=(1+.4*t)/(1-.4*t)}}),this.iridescenceMap=null,this.iridescenceIOR=1.3,this.iridescenceThicknessRange=[100,400],this.iridescenceThicknessMap=null,this.sheenColor=new ve(0),this.sheenColorMap=null,this.sheenRoughness=1,this.sheenRoughnessMap=null,this.transmissionMap=null,this.thickness=0,this.thicknessMap=null,this.attenuationDistance=1/0,this.attenuationColor=new ve(1,1,1),this.specularIntensity=1,this.specularIntensityMap=null,this.specularColor=new ve(1,1,1),this.specularColorMap=null,this._anisotropy=0,this._clearcoat=0,this._dispersion=0,this._iridescence=0,this._sheen=0,this._transmission=0,this.setValues(e)}get anisotropy(){return this._anisotropy}set anisotropy(e){this._anisotropy>0!=e>0&&this.version++,this._anisotropy=e}get clearcoat(){return this._clearcoat}set clearcoat(e){this._clearcoat>0!=e>0&&this.version++,this._clearcoat=e}get iridescence(){return this._iridescence}set iridescence(e){this._iridescence>0!=e>0&&this.version++,this._iridescence=e}get dispersion(){return this._dispersion}set dispersion(e){this._dispersion>0!=e>0&&this.version++,this._dispersion=e}get sheen(){return this._sheen}set sheen(e){this._sheen>0!=e>0&&this.version++,this._sheen=e}get transmission(){return this._transmission}set transmission(e){this._transmission>0!=e>0&&this.version++,this._transmission=e}copy(e){return super.copy(e),this.defines={STANDARD:"",PHYSICAL:""},this.anisotropy=e.anisotropy,this.anisotropyRotation=e.anisotropyRotation,this.anisotropyMap=e.anisotropyMap,this.clearcoat=e.clearcoat,this.clearcoatMap=e.clearcoatMap,this.clearcoatRoughness=e.clearcoatRoughness,this.clearcoatRoughnessMap=e.clearcoatRoughnessMap,this.clearcoatNormalMap=e.clearcoatNormalMap,this.clearcoatNormalScale.copy(e.clearcoatNormalScale),this.dispersion=e.dispersion,this.ior=e.ior,this.iridescence=e.iridescence,this.iridescenceMap=e.iridescenceMap,this.iridescenceIOR=e.iridescenceIOR,this.iridescenceThicknessRange=[...e.iridescenceThicknessRange],this.iridescenceThicknessMap=e.iridescenceThicknessMap,this.sheen=e.sheen,this.sheenColor.copy(e.sheenColor),this.sheenColorMap=e.sheenColorMap,this.sheenRoughness=e.sheenRoughness,this.sheenRoughnessMap=e.sheenRoughnessMap,this.transmission=e.transmission,this.transmissionMap=e.transmissionMap,this.thickness=e.thickness,this.thicknessMap=e.thicknessMap,this.attenuationDistance=e.attenuationDistance,this.attenuationColor.copy(e.attenuationColor),this.specularIntensity=e.specularIntensity,this.specularIntensityMap=e.specularIntensityMap,this.specularColor.copy(e.specularColor),this.specularColorMap=e.specularColorMap,this}};function kr(s,e,t){return!s||!t&&s.constructor===e?s:typeof e.BYTES_PER_ELEMENT=="number"?new e(s):Array.prototype.slice.call(s)}function Zg(s){return ArrayBuffer.isView(s)&&!(s instanceof DataView)}function Kg(s){function e(i,r){return s[i]-s[r]}let t=s.length,n=new Array(t);for(let i=0;i!==t;++i)n[i]=i;return n.sort(e),n}function Gu(s,e,t){let n=s.length,i=new s.constructor(n);for(let r=0,o=0;o!==n;++r){let a=t[r]*e;for(let c=0;c!==e;++c)i[o++]=s[a+c]}return i}function gh(s,e,t,n){let i=1,r=s[0];for(;r!==void 0&&r[n]===void 0;)r=s[i++];if(r===void 0)return;let o=r[n];if(o!==void 0)if(Array.isArray(o))do o=r[n],o!==void 0&&(e.push(r.time),t.push.apply(t,o)),r=s[i++];while(r!==void 0);else if(o.toArray!==void 0)do o=r[n],o!==void 0&&(e.push(r.time),o.toArray(t,t.length)),r=s[i++];while(r!==void 0);else do o=r[n],o!==void 0&&(e.push(r.time),t.push(o)),r=s[i++];while(r!==void 0)}var fi=class{constructor(e,t,n,i){this.parameterPositions=e,this._cachedIndex=0,this.resultBuffer=i!==void 0?i:new t.constructor(n),this.sampleValues=t,this.valueSize=n,this.settings=null,this.DefaultSettings_={}}evaluate(e){let t=this.parameterPositions,n=this._cachedIndex,i=t[n],r=t[n-1];n:{e:{let o;t:{i:if(!(e<i)){for(let a=n+2;;){if(i===void 0){if(e<r)break i;return n=t.length,this._cachedIndex=n,this.copySampleValue_(n-1)}if(n===a)break;if(r=i,i=t[++n],e<i)break e}o=t.length;break t}if(!(e>=r)){let a=t[1];e<a&&(n=2,r=a);for(let c=n-2;;){if(r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(n===c)break;if(i=r,r=t[--n-1],e>=r)break e}o=n,n=0;break t}break n}for(;n<o;){let a=n+o>>>1;e<t[a]?o=a:n=a+1}if(i=t[n],r=t[n-1],r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(i===void 0)return n=t.length,this._cachedIndex=n,this.copySampleValue_(n-1)}this._cachedIndex=n,this.intervalChanged_(n,r,i)}return this.interpolate_(n,r,e,i)}getSettings_(){return this.settings||this.DefaultSettings_}copySampleValue_(e){let t=this.resultBuffer,n=this.sampleValues,i=this.valueSize,r=e*i;for(let o=0;o!==i;++o)t[o]=n[r+o];return t}interpolate_(){throw new Error("call to abstract method")}intervalChanged_(){}},rc=class extends fi{constructor(e,t,n,i){super(e,t,n,i),this._weightPrev=-0,this._offsetPrev=-0,this._weightNext=-0,this._offsetNext=-0,this.DefaultSettings_={endingStart:Dl,endingEnd:Dl}}intervalChanged_(e,t,n){let i=this.parameterPositions,r=e-2,o=e+1,a=i[r],c=i[o];if(a===void 0)switch(this.getSettings_().endingStart){case Ul:r=e,a=2*t-n;break;case Nl:r=i.length-2,a=t+i[r]-i[r+1];break;default:r=e,a=n}if(c===void 0)switch(this.getSettings_().endingEnd){case Ul:o=e,c=2*n-t;break;case Nl:o=1,c=n+i[1]-i[0];break;default:o=e-1,c=t}let l=(n-t)*.5,u=this.valueSize;this._weightPrev=l/(t-a),this._weightNext=l/(c-n),this._offsetPrev=r*u,this._offsetNext=o*u}interpolate_(e,t,n,i){let r=this.resultBuffer,o=this.sampleValues,a=this.valueSize,c=e*a,l=c-a,u=this._offsetPrev,h=this._offsetNext,f=this._weightPrev,p=this._weightNext,g=(n-t)/(i-t),v=g*g,m=v*g,d=-f*m+2*f*v-f*g,M=(1+f)*m+(-1.5-2*f)*v+(-.5+f)*g+1,b=(-1-p)*m+(1.5+p)*v+.5*g,_=p*m-p*v;for(let C=0;C!==a;++C)r[C]=d*o[u+C]+M*o[l+C]+b*o[c+C]+_*o[h+C];return r}},oc=class extends fi{constructor(e,t,n,i){super(e,t,n,i)}interpolate_(e,t,n,i){let r=this.resultBuffer,o=this.sampleValues,a=this.valueSize,c=e*a,l=c-a,u=(n-t)/(i-t),h=1-u;for(let f=0;f!==a;++f)r[f]=o[l+f]*h+o[c+f]*u;return r}},ac=class extends fi{constructor(e,t,n,i){super(e,t,n,i)}interpolate_(e){return this.copySampleValue_(e-1)}},mn=class{constructor(e,t,n,i){if(e===void 0)throw new Error("THREE.KeyframeTrack: track name is undefined");if(t===void 0||t.length===0)throw new Error("THREE.KeyframeTrack: no keyframes in track named "+e);this.name=e,this.times=kr(t,this.TimeBufferType),this.values=kr(n,this.ValueBufferType),this.setInterpolation(i||this.DefaultInterpolation)}static toJSON(e){let t=e.constructor,n;if(t.toJSON!==this.toJSON)n=t.toJSON(e);else{n={name:e.name,times:kr(e.times,Array),values:kr(e.values,Array)};let i=e.getInterpolation();i!==e.DefaultInterpolation&&(n.interpolation=i)}return n.type=e.ValueTypeName,n}InterpolantFactoryMethodDiscrete(e){return new ac(this.times,this.values,this.getValueSize(),e)}InterpolantFactoryMethodLinear(e){return new oc(this.times,this.values,this.getValueSize(),e)}InterpolantFactoryMethodSmooth(e){return new rc(this.times,this.values,this.getValueSize(),e)}setInterpolation(e){let t;switch(e){case ls:t=this.InterpolantFactoryMethodDiscrete;break;case us:t=this.InterpolantFactoryMethodLinear;break;case To:t=this.InterpolantFactoryMethodSmooth;break}if(t===void 0){let n="unsupported interpolation for "+this.ValueTypeName+" keyframe track named "+this.name;if(this.createInterpolant===void 0)if(e!==this.DefaultInterpolation)this.setInterpolation(this.DefaultInterpolation);else throw new Error(n);return console.warn("THREE.KeyframeTrack:",n),this}return this.createInterpolant=t,this}getInterpolation(){switch(this.createInterpolant){case this.InterpolantFactoryMethodDiscrete:return ls;case this.InterpolantFactoryMethodLinear:return us;case this.InterpolantFactoryMethodSmooth:return To}}getValueSize(){return this.values.length/this.times.length}shift(e){if(e!==0){let t=this.times;for(let n=0,i=t.length;n!==i;++n)t[n]+=e}return this}scale(e){if(e!==1){let t=this.times;for(let n=0,i=t.length;n!==i;++n)t[n]*=e}return this}trim(e,t){let n=this.times,i=n.length,r=0,o=i-1;for(;r!==i&&n[r]<e;)++r;for(;o!==-1&&n[o]>t;)--o;if(++o,r!==0||o!==i){r>=o&&(o=Math.max(o,1),r=o-1);let a=this.getValueSize();this.times=n.slice(r,o),this.values=this.values.slice(r*a,o*a)}return this}validate(){let e=!0,t=this.getValueSize();t-Math.floor(t)!==0&&(console.error("THREE.KeyframeTrack: Invalid value size in track.",this),e=!1);let n=this.times,i=this.values,r=n.length;r===0&&(console.error("THREE.KeyframeTrack: Track is empty.",this),e=!1);let o=null;for(let a=0;a!==r;a++){let c=n[a];if(typeof c=="number"&&isNaN(c)){console.error("THREE.KeyframeTrack: Time is not a valid number.",this,a,c),e=!1;break}if(o!==null&&o>c){console.error("THREE.KeyframeTrack: Out of order keys.",this,a,c,o),e=!1;break}o=c}if(i!==void 0&&Zg(i))for(let a=0,c=i.length;a!==c;++a){let l=i[a];if(isNaN(l)){console.error("THREE.KeyframeTrack: Value is not a valid number.",this,a,l),e=!1;break}}return e}optimize(){let e=this.times.slice(),t=this.values.slice(),n=this.getValueSize(),i=this.getInterpolation()===To,r=e.length-1,o=1;for(let a=1;a<r;++a){let c=!1,l=e[a],u=e[a+1];if(l!==u&&(a!==1||l!==e[0]))if(i)c=!0;else{let h=a*n,f=h-n,p=h+n;for(let g=0;g!==n;++g){let v=t[h+g];if(v!==t[f+g]||v!==t[p+g]){c=!0;break}}}if(c){if(a!==o){e[o]=e[a];let h=a*n,f=o*n;for(let p=0;p!==n;++p)t[f+p]=t[h+p]}++o}}if(r>0){e[o]=e[r];for(let a=r*n,c=o*n,l=0;l!==n;++l)t[c+l]=t[a+l];++o}return o!==e.length?(this.times=e.slice(0,o),this.values=t.slice(0,o*n)):(this.times=e,this.values=t),this}clone(){let e=this.times.slice(),t=this.values.slice(),n=this.constructor,i=new n(this.name,e,t);return i.createInterpolant=this.createInterpolant,i}};mn.prototype.TimeBufferType=Float32Array;mn.prototype.ValueBufferType=Float32Array;mn.prototype.DefaultInterpolation=us;var di=class extends mn{constructor(e,t,n){super(e,t,n)}};di.prototype.ValueTypeName="bool";di.prototype.ValueBufferType=Array;di.prototype.DefaultInterpolation=ls;di.prototype.InterpolantFactoryMethodLinear=void 0;di.prototype.InterpolantFactoryMethodSmooth=void 0;var lo=class extends mn{};lo.prototype.ValueTypeName="color";var $n=class extends mn{};$n.prototype.ValueTypeName="number";var cc=class extends fi{constructor(e,t,n,i){super(e,t,n,i)}interpolate_(e,t,n,i){let r=this.resultBuffer,o=this.sampleValues,a=this.valueSize,c=(n-t)/(i-t),l=e*a;for(let u=l+a;l!==u;l+=4)rn.slerpFlat(r,0,o,l-a,o,l,c);return r}},Zn=class extends mn{InterpolantFactoryMethodLinear(e){return new cc(this.times,this.values,this.getValueSize(),e)}};Zn.prototype.ValueTypeName="quaternion";Zn.prototype.InterpolantFactoryMethodSmooth=void 0;var pi=class extends mn{constructor(e,t,n){super(e,t,n)}};pi.prototype.ValueTypeName="string";pi.prototype.ValueBufferType=Array;pi.prototype.DefaultInterpolation=ls;pi.prototype.InterpolantFactoryMethodLinear=void 0;pi.prototype.InterpolantFactoryMethodSmooth=void 0;var Kn=class extends mn{};Kn.prototype.ValueTypeName="vector";var uo=class{constructor(e="",t=-1,n=[],i=bf){this.name=e,this.tracks=n,this.duration=t,this.blendMode=i,this.uuid=An(),this.duration<0&&this.resetDuration()}static parse(e){let t=[],n=e.tracks,i=1/(e.fps||1);for(let o=0,a=n.length;o!==a;++o)t.push(jg(n[o]).scale(i));let r=new this(e.name,e.duration,t,e.blendMode);return r.uuid=e.uuid,r}static toJSON(e){let t=[],n=e.tracks,i={name:e.name,duration:e.duration,tracks:t,uuid:e.uuid,blendMode:e.blendMode};for(let r=0,o=n.length;r!==o;++r)t.push(mn.toJSON(n[r]));return i}static CreateFromMorphTargetSequence(e,t,n,i){let r=t.length,o=[];for(let a=0;a<r;a++){let c=[],l=[];c.push((a+r-1)%r,a,(a+1)%r),l.push(0,1,0);let u=Kg(c);c=Gu(c,1,u),l=Gu(l,1,u),!i&&c[0]===0&&(c.push(r),l.push(l[0])),o.push(new $n(".morphTargetInfluences["+t[a].name+"]",c,l).scale(1/n))}return new this(e,-1,o)}static findByName(e,t){let n=e;if(!Array.isArray(e)){let i=e;n=i.geometry&&i.geometry.animations||i.animations}for(let i=0;i<n.length;i++)if(n[i].name===t)return n[i];return null}static CreateClipsFromMorphTargetSequences(e,t,n){let i={},r=/^([\w-]*?)([\d]+)$/;for(let a=0,c=e.length;a<c;a++){let l=e[a],u=l.name.match(r);if(u&&u.length>1){let h=u[1],f=i[h];f||(i[h]=f=[]),f.push(l)}}let o=[];for(let a in i)o.push(this.CreateFromMorphTargetSequence(a,i[a],t,n));return o}static parseAnimation(e,t){if(!e)return console.error("THREE.AnimationClip: No animation in JSONLoader data."),null;let n=function(h,f,p,g,v){if(p.length!==0){let m=[],d=[];gh(p,m,d,g),m.length!==0&&v.push(new h(f,m,d))}},i=[],r=e.name||"default",o=e.fps||30,a=e.blendMode,c=e.length||-1,l=e.hierarchy||[];for(let h=0;h<l.length;h++){let f=l[h].keys;if(!(!f||f.length===0))if(f[0].morphTargets){let p={},g;for(g=0;g<f.length;g++)if(f[g].morphTargets)for(let v=0;v<f[g].morphTargets.length;v++)p[f[g].morphTargets[v]]=-1;for(let v in p){let m=[],d=[];for(let M=0;M!==f[g].morphTargets.length;++M){let b=f[g];m.push(b.time),d.push(b.morphTarget===v?1:0)}i.push(new $n(".morphTargetInfluence["+v+"]",m,d))}c=p.length*o}else{let p=".bones["+t[h].name+"]";n(Kn,p+".position",f,"pos",i),n(Zn,p+".quaternion",f,"rot",i),n(Kn,p+".scale",f,"scl",i)}}return i.length===0?null:new this(r,c,i,a)}resetDuration(){let e=this.tracks,t=0;for(let n=0,i=e.length;n!==i;++n){let r=this.tracks[n];t=Math.max(t,r.times[r.times.length-1])}return this.duration=t,this}trim(){for(let e=0;e<this.tracks.length;e++)this.tracks[e].trim(0,this.duration);return this}validate(){let e=!0;for(let t=0;t<this.tracks.length;t++)e=e&&this.tracks[t].validate();return e}optimize(){for(let e=0;e<this.tracks.length;e++)this.tracks[e].optimize();return this}clone(){let e=[];for(let t=0;t<this.tracks.length;t++)e.push(this.tracks[t].clone());return new this.constructor(this.name,this.duration,e,this.blendMode)}toJSON(){return this.constructor.toJSON(this)}};function Jg(s){switch(s.toLowerCase()){case"scalar":case"double":case"float":case"number":case"integer":return $n;case"vector":case"vector2":case"vector3":case"vector4":return Kn;case"color":return lo;case"quaternion":return Zn;case"bool":case"boolean":return di;case"string":return pi}throw new Error("THREE.KeyframeTrack: Unsupported typeName: "+s)}function jg(s){if(s.type===void 0)throw new Error("THREE.KeyframeTrack: track type undefined, can not parse");let e=Jg(s.type);if(s.times===void 0){let t=[],n=[];gh(s.keys,t,n,"value"),s.times=t,s.values=n}return e.parse!==void 0?e.parse(s):new e(s.name,s.times,s.values,s.interpolation)}var ci={enabled:!1,files:{},add:function(s,e){this.enabled!==!1&&(this.files[s]=e)},get:function(s){if(this.enabled!==!1)return this.files[s]},remove:function(s){delete this.files[s]},clear:function(){this.files={}}},lc=class{constructor(e,t,n){let i=this,r=!1,o=0,a=0,c,l=[];this.onStart=void 0,this.onLoad=e,this.onProgress=t,this.onError=n,this.itemStart=function(u){a++,r===!1&&i.onStart!==void 0&&i.onStart(u,o,a),r=!0},this.itemEnd=function(u){o++,i.onProgress!==void 0&&i.onProgress(u,o,a),o===a&&(r=!1,i.onLoad!==void 0&&i.onLoad())},this.itemError=function(u){i.onError!==void 0&&i.onError(u)},this.resolveURL=function(u){return c?c(u):u},this.setURLModifier=function(u){return c=u,this},this.addHandler=function(u,h){return l.push(u,h),this},this.removeHandler=function(u){let h=l.indexOf(u);return h!==-1&&l.splice(h,2),this},this.getHandler=function(u){for(let h=0,f=l.length;h<f;h+=2){let p=l[h],g=l[h+1];if(p.global&&(p.lastIndex=0),p.test(u))return g}return null}}},Qg=new lc,Jn=class{constructor(e){this.manager=e!==void 0?e:Qg,this.crossOrigin="anonymous",this.withCredentials=!1,this.path="",this.resourcePath="",this.requestHeader={}}load(){}loadAsync(e,t){let n=this;return new Promise(function(i,r){n.load(e,i,t,r)})}parse(){}setCrossOrigin(e){return this.crossOrigin=e,this}setWithCredentials(e){return this.withCredentials=e,this}setPath(e){return this.path=e,this}setResourcePath(e){return this.resourcePath=e,this}setRequestHeader(e){return this.requestHeader=e,this}};Jn.DEFAULT_MATERIAL_NAME="__DEFAULT";var Vn={},uc=class extends Error{constructor(e,t){super(e),this.response=t}},ir=class extends Jn{constructor(e){super(e)}load(e,t,n,i){e===void 0&&(e=""),this.path!==void 0&&(e=this.path+e),e=this.manager.resolveURL(e);let r=ci.get(e);if(r!==void 0)return this.manager.itemStart(e),setTimeout(()=>{t&&t(r),this.manager.itemEnd(e)},0),r;if(Vn[e]!==void 0){Vn[e].push({onLoad:t,onProgress:n,onError:i});return}Vn[e]=[],Vn[e].push({onLoad:t,onProgress:n,onError:i});let o=new Request(e,{headers:new Headers(this.requestHeader),credentials:this.withCredentials?"include":"same-origin"}),a=this.mimeType,c=this.responseType;fetch(o).then(l=>{if(l.status===200||l.status===0){if(l.status===0&&console.warn("THREE.FileLoader: HTTP Status 0 received."),typeof ReadableStream>"u"||l.body===void 0||l.body.getReader===void 0)return l;let u=Vn[e],h=l.body.getReader(),f=l.headers.get("X-File-Size")||l.headers.get("Content-Length"),p=f?parseInt(f):0,g=p!==0,v=0,m=new ReadableStream({start(d){M();function M(){h.read().then(({done:b,value:_})=>{if(b)d.close();else{v+=_.byteLength;let C=new ProgressEvent("progress",{lengthComputable:g,loaded:v,total:p});for(let A=0,E=u.length;A<E;A++){let I=u[A];I.onProgress&&I.onProgress(C)}d.enqueue(_),M()}},b=>{d.error(b)})}}});return new Response(m)}else throw new uc(`fetch for "${l.url}" responded with ${l.status}: ${l.statusText}`,l)}).then(l=>{switch(c){case"arraybuffer":return l.arrayBuffer();case"blob":return l.blob();case"document":return l.text().then(u=>new DOMParser().parseFromString(u,a));case"json":return l.json();default:if(a===void 0)return l.text();{let h=/charset="?([^;"\s]*)"?/i.exec(a),f=h&&h[1]?h[1].toLowerCase():void 0,p=new TextDecoder(f);return l.arrayBuffer().then(g=>p.decode(g))}}}).then(l=>{ci.add(e,l);let u=Vn[e];delete Vn[e];for(let h=0,f=u.length;h<f;h++){let p=u[h];p.onLoad&&p.onLoad(l)}}).catch(l=>{let u=Vn[e];if(u===void 0)throw this.manager.itemError(e),l;delete Vn[e];for(let h=0,f=u.length;h<f;h++){let p=u[h];p.onError&&p.onError(l)}this.manager.itemError(e)}).finally(()=>{this.manager.itemEnd(e)}),this.manager.itemStart(e)}setResponseType(e){return this.responseType=e,this}setMimeType(e){return this.mimeType=e,this}};var hc=class extends Jn{constructor(e){super(e)}load(e,t,n,i){this.path!==void 0&&(e=this.path+e),e=this.manager.resolveURL(e);let r=this,o=ci.get(e);if(o!==void 0)return r.manager.itemStart(e),setTimeout(function(){t&&t(o),r.manager.itemEnd(e)},0),o;let a=Zs("img");function c(){u(),ci.add(e,this),t&&t(this),r.manager.itemEnd(e)}function l(h){u(),i&&i(h),r.manager.itemError(e),r.manager.itemEnd(e)}function u(){a.removeEventListener("load",c,!1),a.removeEventListener("error",l,!1)}return a.addEventListener("load",c,!1),a.addEventListener("error",l,!1),e.slice(0,5)!=="data:"&&this.crossOrigin!==void 0&&(a.crossOrigin=this.crossOrigin),r.manager.itemStart(e),a.src=e,a}};var ys=class extends Jn{constructor(e){super(e)}load(e,t,n,i){let r=new Pt,o=new hc(this.manager);return o.setCrossOrigin(this.crossOrigin),o.setPath(this.path),o.load(e,function(a){r.image=a,r.needsUpdate=!0,t!==void 0&&t(r)},n,i),r}},Ms=class extends gt{constructor(e,t=1){super(),this.isLight=!0,this.type="Light",this.color=new ve(e),this.intensity=t}dispose(){}copy(e,t){return super.copy(e,t),this.color.copy(e.color),this.intensity=e.intensity,this}toJSON(e){let t=super.toJSON(e);return t.object.color=this.color.getHex(),t.object.intensity=this.intensity,this.groundColor!==void 0&&(t.object.groundColor=this.groundColor.getHex()),this.distance!==void 0&&(t.object.distance=this.distance),this.angle!==void 0&&(t.object.angle=this.angle),this.decay!==void 0&&(t.object.decay=this.decay),this.penumbra!==void 0&&(t.object.penumbra=this.penumbra),this.shadow!==void 0&&(t.object.shadow=this.shadow.toJSON()),this.target!==void 0&&(t.object.target=this.target.uuid),t}},mi=class extends Ms{constructor(e,t,n){super(e,n),this.isHemisphereLight=!0,this.type="HemisphereLight",this.position.copy(gt.DEFAULT_UP),this.updateMatrix(),this.groundColor=new ve(t)}copy(e,t){return super.copy(e,t),this.groundColor.copy(e.groundColor),this}},na=new Le,Wu=new P,Xu=new P,sr=class{constructor(e){this.camera=e,this.intensity=1,this.bias=0,this.normalBias=0,this.radius=1,this.blurSamples=8,this.mapSize=new le(512,512),this.map=null,this.mapPass=null,this.matrix=new Le,this.autoUpdate=!0,this.needsUpdate=!1,this._frustum=new Ks,this._frameExtents=new le(1,1),this._viewportCount=1,this._viewports=[new We(0,0,1,1)]}getViewportCount(){return this._viewportCount}getFrustum(){return this._frustum}updateMatrices(e){let t=this.camera,n=this.matrix;Wu.setFromMatrixPosition(e.matrixWorld),t.position.copy(Wu),Xu.setFromMatrixPosition(e.target.matrixWorld),t.lookAt(Xu),t.updateMatrixWorld(),na.multiplyMatrices(t.projectionMatrix,t.matrixWorldInverse),this._frustum.setFromProjectionMatrix(na),n.set(.5,0,0,.5,0,.5,0,.5,0,0,.5,.5,0,0,0,1),n.multiply(na)}getViewport(e){return this._viewports[e]}getFrameExtents(){return this._frameExtents}dispose(){this.map&&this.map.dispose(),this.mapPass&&this.mapPass.dispose()}copy(e){return this.camera=e.camera.clone(),this.intensity=e.intensity,this.bias=e.bias,this.radius=e.radius,this.mapSize.copy(e.mapSize),this}clone(){return new this.constructor().copy(this)}toJSON(){let e={};return this.intensity!==1&&(e.intensity=this.intensity),this.bias!==0&&(e.bias=this.bias),this.normalBias!==0&&(e.normalBias=this.normalBias),this.radius!==1&&(e.radius=this.radius),(this.mapSize.x!==512||this.mapSize.y!==512)&&(e.mapSize=this.mapSize.toArray()),e.camera=this.camera.toJSON(!1).object,delete e.camera.matrix,e}},fc=class extends sr{constructor(){super(new _t(50,1,.5,500)),this.isSpotLightShadow=!0,this.focus=1}updateMatrices(e){let t=this.camera,n=hs*2*e.angle*this.focus,i=this.mapSize.width/this.mapSize.height,r=e.distance||t.far;(n!==t.fov||i!==t.aspect||r!==t.far)&&(t.fov=n,t.aspect=i,t.far=r,t.updateProjectionMatrix()),super.updateMatrices(e)}copy(e){return super.copy(e),this.focus=e.focus,this}},jn=class extends Ms{constructor(e,t,n=0,i=Math.PI/3,r=0,o=2){super(e,t),this.isSpotLight=!0,this.type="SpotLight",this.position.copy(gt.DEFAULT_UP),this.updateMatrix(),this.target=new gt,this.distance=n,this.angle=i,this.penumbra=r,this.decay=o,this.map=null,this.shadow=new fc}get power(){return this.intensity*Math.PI}set power(e){this.intensity=e/Math.PI}dispose(){this.shadow.dispose()}copy(e,t){return super.copy(e,t),this.distance=e.distance,this.angle=e.angle,this.penumbra=e.penumbra,this.decay=e.decay,this.target=e.target.clone(),this.shadow=e.shadow.clone(),this}},qu=new Le,ks=new P,ia=new P,dc=class extends sr{constructor(){super(new _t(90,1,.5,500)),this.isPointLightShadow=!0,this._frameExtents=new le(4,2),this._viewportCount=6,this._viewports=[new We(2,1,1,1),new We(0,1,1,1),new We(3,1,1,1),new We(1,1,1,1),new We(3,0,1,1),new We(1,0,1,1)],this._cubeDirections=[new P(1,0,0),new P(-1,0,0),new P(0,0,1),new P(0,0,-1),new P(0,1,0),new P(0,-1,0)],this._cubeUps=[new P(0,1,0),new P(0,1,0),new P(0,1,0),new P(0,1,0),new P(0,0,1),new P(0,0,-1)]}updateMatrices(e,t=0){let n=this.camera,i=this.matrix,r=e.distance||n.far;r!==n.far&&(n.far=r,n.updateProjectionMatrix()),ks.setFromMatrixPosition(e.matrixWorld),n.position.copy(ks),ia.copy(n.position),ia.add(this._cubeDirections[t]),n.up.copy(this._cubeUps[t]),n.lookAt(ia),n.updateMatrixWorld(),i.makeTranslation(-ks.x,-ks.y,-ks.z),qu.multiplyMatrices(n.projectionMatrix,n.matrixWorldInverse),this._frustum.setFromProjectionMatrix(qu)}},ho=class extends Ms{constructor(e,t,n=0,i=2){super(e,t),this.isPointLight=!0,this.type="PointLight",this.distance=n,this.decay=i,this.shadow=new dc}get power(){return this.intensity*4*Math.PI}set power(e){this.intensity=e/(4*Math.PI)}dispose(){this.shadow.dispose()}copy(e,t){return super.copy(e,t),this.distance=e.distance,this.decay=e.decay,this.shadow=e.shadow.clone(),this}},pc=class extends sr{constructor(){super(new hi(-5,5,5,-5,.5,500)),this.isDirectionalLightShadow=!0}},Un=class extends Ms{constructor(e,t){super(e,t),this.isDirectionalLight=!0,this.type="DirectionalLight",this.position.copy(gt.DEFAULT_UP),this.updateMatrix(),this.target=new gt,this.shadow=new pc}dispose(){this.shadow.dispose()}copy(e){return super.copy(e),this.target=e.target.clone(),this.shadow=e.shadow.clone(),this}};var gi=class{static decodeText(e){if(console.warn("THREE.LoaderUtils: decodeText() has been deprecated with r165 and will be removed with r175. Use TextDecoder instead."),typeof TextDecoder<"u")return new TextDecoder().decode(e);let t="";for(let n=0,i=e.length;n<i;n++)t+=String.fromCharCode(e[n]);try{return decodeURIComponent(escape(t))}catch{return t}}static extractUrlBase(e){let t=e.lastIndexOf("/");return t===-1?"./":e.slice(0,t+1)}static resolveURL(e,t){return typeof e!="string"||e===""?"":(/^https?:\/\//i.test(t)&&/^\//.test(e)&&(t=t.replace(/(^https?:\/\/[^\/]+).*/i,"$1")),/^(https?:)?\/\//i.test(e)||/^data:.*,.*$/i.test(e)||/^blob:.*$/i.test(e)?e:t+e)}};var fo=class extends Jn{constructor(e){super(e),this.isImageBitmapLoader=!0,typeof createImageBitmap>"u"&&console.warn("THREE.ImageBitmapLoader: createImageBitmap() not supported."),typeof fetch>"u"&&console.warn("THREE.ImageBitmapLoader: fetch() not supported."),this.options={premultiplyAlpha:"none"}}setOptions(e){return this.options=e,this}load(e,t,n,i){e===void 0&&(e=""),this.path!==void 0&&(e=this.path+e),e=this.manager.resolveURL(e);let r=this,o=ci.get(e);if(o!==void 0){if(r.manager.itemStart(e),o.then){o.then(l=>{t&&t(l),r.manager.itemEnd(e)}).catch(l=>{i&&i(l)});return}return setTimeout(function(){t&&t(o),r.manager.itemEnd(e)},0),o}let a={};a.credentials=this.crossOrigin==="anonymous"?"same-origin":"include",a.headers=this.requestHeader;let c=fetch(e,a).then(function(l){return l.blob()}).then(function(l){return createImageBitmap(l,Object.assign(r.options,{colorSpaceConversion:"none"}))}).then(function(l){return ci.add(e,l),t&&t(l),r.manager.itemEnd(e),l}).catch(function(l){i&&i(l),ci.remove(e),r.manager.itemError(e),r.manager.itemEnd(e)});ci.add(e,c),r.manager.itemStart(e)}};var Rc="\\[\\]\\.:\\/",ev=new RegExp("["+Rc+"]","g"),Cc="[^"+Rc+"]",tv="[^"+Rc.replace("\\.","")+"]",nv=/((?:WC+[\/:])*)/.source.replace("WC",Cc),iv=/(WCOD+)?/.source.replace("WCOD",tv),sv=/(?:\.(WC+)(?:\[(.+)\])?)?/.source.replace("WC",Cc),rv=/\.(WC+)(?:\[(.+)\])?/.source.replace("WC",Cc),ov=new RegExp("^"+nv+iv+sv+rv+"$"),av=["material","materials","bones","map"],mc=class{constructor(e,t,n){let i=n||dt.parseTrackName(t);this._targetGroup=e,this._bindings=e.subscribe_(t,i)}getValue(e,t){this.bind();let n=this._targetGroup.nCachedObjects_,i=this._bindings[n];i!==void 0&&i.getValue(e,t)}setValue(e,t){let n=this._bindings;for(let i=this._targetGroup.nCachedObjects_,r=n.length;i!==r;++i)n[i].setValue(e,t)}bind(){let e=this._bindings;for(let t=this._targetGroup.nCachedObjects_,n=e.length;t!==n;++t)e[t].bind()}unbind(){let e=this._bindings;for(let t=this._targetGroup.nCachedObjects_,n=e.length;t!==n;++t)e[t].unbind()}},dt=class s{constructor(e,t,n){this.path=t,this.parsedPath=n||s.parseTrackName(t),this.node=s.findNode(e,this.parsedPath.nodeName),this.rootNode=e,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}static create(e,t,n){return e&&e.isAnimationObjectGroup?new s.Composite(e,t,n):new s(e,t,n)}static sanitizeNodeName(e){return e.replace(/\s/g,"_").replace(ev,"")}static parseTrackName(e){let t=ov.exec(e);if(t===null)throw new Error("PropertyBinding: Cannot parse trackName: "+e);let n={nodeName:t[2],objectName:t[3],objectIndex:t[4],propertyName:t[5],propertyIndex:t[6]},i=n.nodeName&&n.nodeName.lastIndexOf(".");if(i!==void 0&&i!==-1){let r=n.nodeName.substring(i+1);av.indexOf(r)!==-1&&(n.nodeName=n.nodeName.substring(0,i),n.objectName=r)}if(n.propertyName===null||n.propertyName.length===0)throw new Error("PropertyBinding: can not parse propertyName from trackName: "+e);return n}static findNode(e,t){if(t===void 0||t===""||t==="."||t===-1||t===e.name||t===e.uuid)return e;if(e.skeleton){let n=e.skeleton.getBoneByName(t);if(n!==void 0)return n}if(e.children){let n=function(r){for(let o=0;o<r.length;o++){let a=r[o];if(a.name===t||a.uuid===t)return a;let c=n(a.children);if(c)return c}return null},i=n(e.children);if(i)return i}return null}_getValue_unavailable(){}_setValue_unavailable(){}_getValue_direct(e,t){e[t]=this.targetObject[this.propertyName]}_getValue_array(e,t){let n=this.resolvedProperty;for(let i=0,r=n.length;i!==r;++i)e[t++]=n[i]}_getValue_arrayElement(e,t){e[t]=this.resolvedProperty[this.propertyIndex]}_getValue_toArray(e,t){this.resolvedProperty.toArray(e,t)}_setValue_direct(e,t){this.targetObject[this.propertyName]=e[t]}_setValue_direct_setNeedsUpdate(e,t){this.targetObject[this.propertyName]=e[t],this.targetObject.needsUpdate=!0}_setValue_direct_setMatrixWorldNeedsUpdate(e,t){this.targetObject[this.propertyName]=e[t],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_array(e,t){let n=this.resolvedProperty;for(let i=0,r=n.length;i!==r;++i)n[i]=e[t++]}_setValue_array_setNeedsUpdate(e,t){let n=this.resolvedProperty;for(let i=0,r=n.length;i!==r;++i)n[i]=e[t++];this.targetObject.needsUpdate=!0}_setValue_array_setMatrixWorldNeedsUpdate(e,t){let n=this.resolvedProperty;for(let i=0,r=n.length;i!==r;++i)n[i]=e[t++];this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_arrayElement(e,t){this.resolvedProperty[this.propertyIndex]=e[t]}_setValue_arrayElement_setNeedsUpdate(e,t){this.resolvedProperty[this.propertyIndex]=e[t],this.targetObject.needsUpdate=!0}_setValue_arrayElement_setMatrixWorldNeedsUpdate(e,t){this.resolvedProperty[this.propertyIndex]=e[t],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_fromArray(e,t){this.resolvedProperty.fromArray(e,t)}_setValue_fromArray_setNeedsUpdate(e,t){this.resolvedProperty.fromArray(e,t),this.targetObject.needsUpdate=!0}_setValue_fromArray_setMatrixWorldNeedsUpdate(e,t){this.resolvedProperty.fromArray(e,t),this.targetObject.matrixWorldNeedsUpdate=!0}_getValue_unbound(e,t){this.bind(),this.getValue(e,t)}_setValue_unbound(e,t){this.bind(),this.setValue(e,t)}bind(){let e=this.node,t=this.parsedPath,n=t.objectName,i=t.propertyName,r=t.propertyIndex;if(e||(e=s.findNode(this.rootNode,t.nodeName),this.node=e),this.getValue=this._getValue_unavailable,this.setValue=this._setValue_unavailable,!e){console.warn("THREE.PropertyBinding: No target node found for track: "+this.path+".");return}if(n){let l=t.objectIndex;switch(n){case"materials":if(!e.material){console.error("THREE.PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!e.material.materials){console.error("THREE.PropertyBinding: Can not bind to material.materials as node.material does not have a materials array.",this);return}e=e.material.materials;break;case"bones":if(!e.skeleton){console.error("THREE.PropertyBinding: Can not bind to bones as node does not have a skeleton.",this);return}e=e.skeleton.bones;for(let u=0;u<e.length;u++)if(e[u].name===l){l=u;break}break;case"map":if("map"in e){e=e.map;break}if(!e.material){console.error("THREE.PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!e.material.map){console.error("THREE.PropertyBinding: Can not bind to material.map as node.material does not have a map.",this);return}e=e.material.map;break;default:if(e[n]===void 0){console.error("THREE.PropertyBinding: Can not bind to objectName of node undefined.",this);return}e=e[n]}if(l!==void 0){if(e[l]===void 0){console.error("THREE.PropertyBinding: Trying to bind to objectIndex of objectName, but is undefined.",this,e);return}e=e[l]}}let o=e[i];if(o===void 0){let l=t.nodeName;console.error("THREE.PropertyBinding: Trying to update property for track: "+l+"."+i+" but it wasn't found.",e);return}let a=this.Versioning.None;this.targetObject=e,e.needsUpdate!==void 0?a=this.Versioning.NeedsUpdate:e.matrixWorldNeedsUpdate!==void 0&&(a=this.Versioning.MatrixWorldNeedsUpdate);let c=this.BindingType.Direct;if(r!==void 0){if(i==="morphTargetInfluences"){if(!e.geometry){console.error("THREE.PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.",this);return}if(!e.geometry.morphAttributes){console.error("THREE.PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.morphAttributes.",this);return}e.morphTargetDictionary[r]!==void 0&&(r=e.morphTargetDictionary[r])}c=this.BindingType.ArrayElement,this.resolvedProperty=o,this.propertyIndex=r}else o.fromArray!==void 0&&o.toArray!==void 0?(c=this.BindingType.HasFromToArray,this.resolvedProperty=o):Array.isArray(o)?(c=this.BindingType.EntireArray,this.resolvedProperty=o):this.propertyName=i;this.getValue=this.GetterByBindingType[c],this.setValue=this.SetterByBindingTypeAndVersioning[c][a]}unbind(){this.node=null,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}};dt.Composite=mc;dt.prototype.BindingType={Direct:0,EntireArray:1,ArrayElement:2,HasFromToArray:3};dt.prototype.Versioning={None:0,NeedsUpdate:1,MatrixWorldNeedsUpdate:2};dt.prototype.GetterByBindingType=[dt.prototype._getValue_direct,dt.prototype._getValue_array,dt.prototype._getValue_arrayElement,dt.prototype._getValue_toArray];dt.prototype.SetterByBindingTypeAndVersioning=[[dt.prototype._setValue_direct,dt.prototype._setValue_direct_setNeedsUpdate,dt.prototype._setValue_direct_setMatrixWorldNeedsUpdate],[dt.prototype._setValue_array,dt.prototype._setValue_array_setNeedsUpdate,dt.prototype._setValue_array_setMatrixWorldNeedsUpdate],[dt.prototype._setValue_arrayElement,dt.prototype._setValue_arrayElement_setNeedsUpdate,dt.prototype._setValue_arrayElement_setMatrixWorldNeedsUpdate],[dt.prototype._setValue_fromArray,dt.prototype._setValue_fromArray_setNeedsUpdate,dt.prototype._setValue_fromArray_setMatrixWorldNeedsUpdate]];var tx=new Float32Array(1);typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("register",{detail:{revision:gc}}));typeof window<"u"&&(window.__THREE__?console.warn("WARNING: Multiple instances of Three.js being imported."):window.__THREE__=gc);function xh(s,e=!1){let t=s[0].index!==null,n=new Set(Object.keys(s[0].attributes)),i=new Set(Object.keys(s[0].morphAttributes)),r={},o={},a=s[0].morphTargetsRelative,c=new Mt,l=0;for(let u=0;u<s.length;++u){let h=s[u],f=0;if(t!==(h.index!==null))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+u+". All geometries must have compatible attributes; make sure index attribute exists among all geometries, or in none of them."),null;for(let p in h.attributes){if(!n.has(p))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+u+'. All geometries must have compatible attributes; make sure "'+p+'" attribute exists among all geometries, or in none of them.'),null;r[p]===void 0&&(r[p]=[]),r[p].push(h.attributes[p]),f++}if(f!==n.size)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+u+". Make sure all geometries have the same number of attributes."),null;if(a!==h.morphTargetsRelative)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+u+". .morphTargetsRelative must be consistent throughout all geometries."),null;for(let p in h.morphAttributes){if(!i.has(p))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+u+".  .morphAttributes must be consistent throughout all geometries."),null;o[p]===void 0&&(o[p]=[]),o[p].push(h.morphAttributes[p])}if(e){let p;if(t)p=h.index.count;else if(h.attributes.position!==void 0)p=h.attributes.position.count;else return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+u+". The geometry must have either an index or a position attribute"),null;c.addGroup(l,p,u),l+=p}}if(t){let u=0,h=[];for(let f=0;f<s.length;++f){let p=s[f].index;for(let g=0;g<p.count;++g)h.push(p.getX(g)+u);u+=s[f].attributes.position.count}c.setIndex(h)}for(let u in r){let h=vh(r[u]);if(!h)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed while trying to merge the "+u+" attribute."),null;c.setAttribute(u,h)}for(let u in o){let h=o[u][0].length;if(h===0)break;c.morphAttributes=c.morphAttributes||{},c.morphAttributes[u]=[];for(let f=0;f<h;++f){let p=[];for(let v=0;v<o[u].length;++v)p.push(o[u][v][f]);let g=vh(p);if(!g)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed while trying to merge the "+u+" morphAttribute."),null;c.morphAttributes[u].push(g)}}return c}function vh(s){let e,t,n,i=-1,r=0;for(let l=0;l<s.length;++l){let u=s[l];if(e===void 0&&(e=u.array.constructor),e!==u.array.constructor)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.array must be of consistent array types across matching attributes."),null;if(t===void 0&&(t=u.itemSize),t!==u.itemSize)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.itemSize must be consistent across matching attributes."),null;if(n===void 0&&(n=u.normalized),n!==u.normalized)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.normalized must be consistent across matching attributes."),null;if(i===-1&&(i=u.gpuType),i!==u.gpuType)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.gpuType must be consistent across matching attributes."),null;r+=u.count*t}let o=new e(r),a=new it(o,t,n),c=0;for(let l=0;l<s.length;++l){let u=s[l];if(u.isInterleavedBufferAttribute){let h=c/t;for(let f=0,p=u.count;f<p;f++)for(let g=0;g<t;g++){let v=u.getComponent(f,g);a.setComponent(f+h,g,v)}}else o.set(u.array,c);c+=u.count*t}return i!==void 0&&(a.gpuType=i),a}function Ic(s,e){if(e===rh)return console.warn("THREE.BufferGeometryUtils.toTrianglesDrawMode(): Geometry already defined as triangles."),s;if(e===rr||e===mo){let t=s.getIndex();if(t===null){let o=[],a=s.getAttribute("position");if(a!==void 0){for(let c=0;c<a.count;c++)o.push(c);s.setIndex(o),t=s.getIndex()}else return console.error("THREE.BufferGeometryUtils.toTrianglesDrawMode(): Undefined position attribute. Processing not possible."),s}let n=t.count-2,i=[];if(e===rr)for(let o=1;o<=n;o++)i.push(t.getX(0)),i.push(t.getX(o)),i.push(t.getX(o+1));else for(let o=0;o<n;o++)o%2===0?(i.push(t.getX(o)),i.push(t.getX(o+1)),i.push(t.getX(o+2))):(i.push(t.getX(o+2)),i.push(t.getX(o+1)),i.push(t.getX(o)));i.length/3!==n&&console.error("THREE.BufferGeometryUtils.toTrianglesDrawMode(): Unable to generate correct amount of triangles.");let r=s.clone();return r.setIndex(i),r.clearGroups(),r}else return console.error("THREE.BufferGeometryUtils.toTrianglesDrawMode(): Unknown draw mode:",e),s}var xo=class extends Jn{constructor(e){super(e),this.dracoLoader=null,this.ktx2Loader=null,this.meshoptDecoder=null,this.pluginCallbacks=[],this.register(function(t){return new Oc(t)}),this.register(function(t){return new Bc(t)}),this.register(function(t){return new Yc(t)}),this.register(function(t){return new $c(t)}),this.register(function(t){return new Zc(t)}),this.register(function(t){return new kc(t)}),this.register(function(t){return new Hc(t)}),this.register(function(t){return new Vc(t)}),this.register(function(t){return new Gc(t)}),this.register(function(t){return new Fc(t)}),this.register(function(t){return new Wc(t)}),this.register(function(t){return new zc(t)}),this.register(function(t){return new qc(t)}),this.register(function(t){return new Xc(t)}),this.register(function(t){return new Uc(t)}),this.register(function(t){return new Kc(t)}),this.register(function(t){return new Jc(t)})}load(e,t,n,i){let r=this,o;if(this.resourcePath!=="")o=this.resourcePath;else if(this.path!==""){let l=gi.extractUrlBase(e);o=gi.resolveURL(l,this.path)}else o=gi.extractUrlBase(e);this.manager.itemStart(e);let a=function(l){i?i(l):console.error(l),r.manager.itemError(e),r.manager.itemEnd(e)},c=new ir(this.manager);c.setPath(this.path),c.setResponseType("arraybuffer"),c.setRequestHeader(this.requestHeader),c.setWithCredentials(this.withCredentials),c.load(e,function(l){try{r.parse(l,o,function(u){t(u),r.manager.itemEnd(e)},a)}catch(u){a(u)}},n,a)}setDRACOLoader(e){return this.dracoLoader=e,this}setKTX2Loader(e){return this.ktx2Loader=e,this}setMeshoptDecoder(e){return this.meshoptDecoder=e,this}register(e){return this.pluginCallbacks.indexOf(e)===-1&&this.pluginCallbacks.push(e),this}unregister(e){return this.pluginCallbacks.indexOf(e)!==-1&&this.pluginCallbacks.splice(this.pluginCallbacks.indexOf(e),1),this}parse(e,t,n,i){let r,o={},a={},c=new TextDecoder;if(typeof e=="string")r=JSON.parse(e);else if(e instanceof ArrayBuffer)if(c.decode(new Uint8Array(e,0,4))===Sh){try{o[Xe.KHR_BINARY_GLTF]=new jc(e)}catch(h){i&&i(h);return}r=JSON.parse(o[Xe.KHR_BINARY_GLTF].content)}else r=JSON.parse(c.decode(e));else r=e;if(r.asset===void 0||r.asset.version[0]<2){i&&i(new Error("THREE.GLTFLoader: Unsupported asset. glTF versions >=2.0 are supported."));return}let l=new rl(r,{path:t||this.resourcePath||"",crossOrigin:this.crossOrigin,requestHeader:this.requestHeader,manager:this.manager,ktx2Loader:this.ktx2Loader,meshoptDecoder:this.meshoptDecoder});l.fileLoader.setRequestHeader(this.requestHeader);for(let u=0;u<this.pluginCallbacks.length;u++){let h=this.pluginCallbacks[u](l);h.name||console.error("THREE.GLTFLoader: Invalid plugin found: missing name"),a[h.name]=h,o[h.name]=!0}if(r.extensionsUsed)for(let u=0;u<r.extensionsUsed.length;++u){let h=r.extensionsUsed[u],f=r.extensionsRequired||[];switch(h){case Xe.KHR_MATERIALS_UNLIT:o[h]=new Nc;break;case Xe.KHR_DRACO_MESH_COMPRESSION:o[h]=new Qc(r,this.dracoLoader);break;case Xe.KHR_TEXTURE_TRANSFORM:o[h]=new el;break;case Xe.KHR_MESH_QUANTIZATION:o[h]=new tl;break;default:f.indexOf(h)>=0&&a[h]===void 0&&console.warn('THREE.GLTFLoader: Unknown extension "'+h+'".')}}l.setExtensions(o),l.setPlugins(a),l.parse(n,i)}parseAsync(e,t){let n=this;return new Promise(function(i,r){n.parse(e,t,i,r)})}};function cv(){let s={};return{get:function(e){return s[e]},add:function(e,t){s[e]=t},remove:function(e){delete s[e]},removeAll:function(){s={}}}}var Xe={KHR_BINARY_GLTF:"KHR_binary_glTF",KHR_DRACO_MESH_COMPRESSION:"KHR_draco_mesh_compression",KHR_LIGHTS_PUNCTUAL:"KHR_lights_punctual",KHR_MATERIALS_CLEARCOAT:"KHR_materials_clearcoat",KHR_MATERIALS_DISPERSION:"KHR_materials_dispersion",KHR_MATERIALS_IOR:"KHR_materials_ior",KHR_MATERIALS_SHEEN:"KHR_materials_sheen",KHR_MATERIALS_SPECULAR:"KHR_materials_specular",KHR_MATERIALS_TRANSMISSION:"KHR_materials_transmission",KHR_MATERIALS_IRIDESCENCE:"KHR_materials_iridescence",KHR_MATERIALS_ANISOTROPY:"KHR_materials_anisotropy",KHR_MATERIALS_UNLIT:"KHR_materials_unlit",KHR_MATERIALS_VOLUME:"KHR_materials_volume",KHR_TEXTURE_BASISU:"KHR_texture_basisu",KHR_TEXTURE_TRANSFORM:"KHR_texture_transform",KHR_MESH_QUANTIZATION:"KHR_mesh_quantization",KHR_MATERIALS_EMISSIVE_STRENGTH:"KHR_materials_emissive_strength",EXT_MATERIALS_BUMP:"EXT_materials_bump",EXT_TEXTURE_WEBP:"EXT_texture_webp",EXT_TEXTURE_AVIF:"EXT_texture_avif",EXT_MESHOPT_COMPRESSION:"EXT_meshopt_compression",EXT_MESH_GPU_INSTANCING:"EXT_mesh_gpu_instancing"},Uc=class{constructor(e){this.parser=e,this.name=Xe.KHR_LIGHTS_PUNCTUAL,this.cache={refs:{},uses:{}}}_markDefs(){let e=this.parser,t=this.parser.json.nodes||[];for(let n=0,i=t.length;n<i;n++){let r=t[n];r.extensions&&r.extensions[this.name]&&r.extensions[this.name].light!==void 0&&e._addNodeRef(this.cache,r.extensions[this.name].light)}}_loadLight(e){let t=this.parser,n="light:"+e,i=t.cache.get(n);if(i)return i;let r=t.json,c=((r.extensions&&r.extensions[this.name]||{}).lights||[])[e],l,u=new ve(16777215);c.color!==void 0&&u.setRGB(c.color[0],c.color[1],c.color[2],Wt);let h=c.range!==void 0?c.range:0;switch(c.type){case"directional":l=new Un(u),l.target.position.set(0,0,-1),l.add(l.target);break;case"point":l=new ho(u),l.distance=h;break;case"spot":l=new jn(u),l.distance=h,c.spot=c.spot||{},c.spot.innerConeAngle=c.spot.innerConeAngle!==void 0?c.spot.innerConeAngle:0,c.spot.outerConeAngle=c.spot.outerConeAngle!==void 0?c.spot.outerConeAngle:Math.PI/4,l.angle=c.spot.outerConeAngle,l.penumbra=1-c.spot.innerConeAngle/c.spot.outerConeAngle,l.target.position.set(0,0,-1),l.add(l.target);break;default:throw new Error("THREE.GLTFLoader: Unexpected light type: "+c.type)}return l.position.set(0,0,0),l.decay=2,Qn(l,c),c.intensity!==void 0&&(l.intensity=c.intensity),l.name=t.createUniqueName(c.name||"light_"+e),i=Promise.resolve(l),t.cache.add(n,i),i}getDependency(e,t){if(e==="light")return this._loadLight(t)}createNodeAttachment(e){let t=this,n=this.parser,r=n.json.nodes[e],a=(r.extensions&&r.extensions[this.name]||{}).light;return a===void 0?null:this._loadLight(a).then(function(c){return n._getNodeRef(t.cache,a,c)})}},Nc=class{constructor(){this.name=Xe.KHR_MATERIALS_UNLIT}getMaterialType(){return Yt}extendParams(e,t,n){let i=[];e.color=new ve(1,1,1),e.opacity=1;let r=t.pbrMetallicRoughness;if(r){if(Array.isArray(r.baseColorFactor)){let o=r.baseColorFactor;e.color.setRGB(o[0],o[1],o[2],Wt),e.opacity=o[3]}r.baseColorTexture!==void 0&&i.push(n.assignTexture(e,"map",r.baseColorTexture,St))}return Promise.all(i)}},Fc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_EMISSIVE_STRENGTH}extendMaterialParams(e,t){let i=this.parser.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=i.extensions[this.name].emissiveStrength;return r!==void 0&&(t.emissiveIntensity=r),Promise.resolve()}},Oc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_CLEARCOAT}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let n=this.parser,i=n.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=[],o=i.extensions[this.name];if(o.clearcoatFactor!==void 0&&(t.clearcoat=o.clearcoatFactor),o.clearcoatTexture!==void 0&&r.push(n.assignTexture(t,"clearcoatMap",o.clearcoatTexture)),o.clearcoatRoughnessFactor!==void 0&&(t.clearcoatRoughness=o.clearcoatRoughnessFactor),o.clearcoatRoughnessTexture!==void 0&&r.push(n.assignTexture(t,"clearcoatRoughnessMap",o.clearcoatRoughnessTexture)),o.clearcoatNormalTexture!==void 0&&(r.push(n.assignTexture(t,"clearcoatNormalMap",o.clearcoatNormalTexture)),o.clearcoatNormalTexture.scale!==void 0)){let a=o.clearcoatNormalTexture.scale;t.clearcoatNormalScale=new le(a,a)}return Promise.all(r)}},Bc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_DISPERSION}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let i=this.parser.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=i.extensions[this.name];return t.dispersion=r.dispersion!==void 0?r.dispersion:0,Promise.resolve()}},zc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_IRIDESCENCE}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let n=this.parser,i=n.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=[],o=i.extensions[this.name];return o.iridescenceFactor!==void 0&&(t.iridescence=o.iridescenceFactor),o.iridescenceTexture!==void 0&&r.push(n.assignTexture(t,"iridescenceMap",o.iridescenceTexture)),o.iridescenceIor!==void 0&&(t.iridescenceIOR=o.iridescenceIor),t.iridescenceThicknessRange===void 0&&(t.iridescenceThicknessRange=[100,400]),o.iridescenceThicknessMinimum!==void 0&&(t.iridescenceThicknessRange[0]=o.iridescenceThicknessMinimum),o.iridescenceThicknessMaximum!==void 0&&(t.iridescenceThicknessRange[1]=o.iridescenceThicknessMaximum),o.iridescenceThicknessTexture!==void 0&&r.push(n.assignTexture(t,"iridescenceThicknessMap",o.iridescenceThicknessTexture)),Promise.all(r)}},kc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_SHEEN}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let n=this.parser,i=n.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=[];t.sheenColor=new ve(0,0,0),t.sheenRoughness=0,t.sheen=1;let o=i.extensions[this.name];if(o.sheenColorFactor!==void 0){let a=o.sheenColorFactor;t.sheenColor.setRGB(a[0],a[1],a[2],Wt)}return o.sheenRoughnessFactor!==void 0&&(t.sheenRoughness=o.sheenRoughnessFactor),o.sheenColorTexture!==void 0&&r.push(n.assignTexture(t,"sheenColorMap",o.sheenColorTexture,St)),o.sheenRoughnessTexture!==void 0&&r.push(n.assignTexture(t,"sheenRoughnessMap",o.sheenRoughnessTexture)),Promise.all(r)}},Hc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_TRANSMISSION}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let n=this.parser,i=n.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=[],o=i.extensions[this.name];return o.transmissionFactor!==void 0&&(t.transmission=o.transmissionFactor),o.transmissionTexture!==void 0&&r.push(n.assignTexture(t,"transmissionMap",o.transmissionTexture)),Promise.all(r)}},Vc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_VOLUME}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let n=this.parser,i=n.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=[],o=i.extensions[this.name];t.thickness=o.thicknessFactor!==void 0?o.thicknessFactor:0,o.thicknessTexture!==void 0&&r.push(n.assignTexture(t,"thicknessMap",o.thicknessTexture)),t.attenuationDistance=o.attenuationDistance||1/0;let a=o.attenuationColor||[1,1,1];return t.attenuationColor=new ve().setRGB(a[0],a[1],a[2],Wt),Promise.all(r)}},Gc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_IOR}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let i=this.parser.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=i.extensions[this.name];return t.ior=r.ior!==void 0?r.ior:1.5,Promise.resolve()}},Wc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_SPECULAR}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let n=this.parser,i=n.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=[],o=i.extensions[this.name];t.specularIntensity=o.specularFactor!==void 0?o.specularFactor:1,o.specularTexture!==void 0&&r.push(n.assignTexture(t,"specularIntensityMap",o.specularTexture));let a=o.specularColorFactor||[1,1,1];return t.specularColor=new ve().setRGB(a[0],a[1],a[2],Wt),o.specularColorTexture!==void 0&&r.push(n.assignTexture(t,"specularColorMap",o.specularColorTexture,St)),Promise.all(r)}},Xc=class{constructor(e){this.parser=e,this.name=Xe.EXT_MATERIALS_BUMP}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let n=this.parser,i=n.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=[],o=i.extensions[this.name];return t.bumpScale=o.bumpFactor!==void 0?o.bumpFactor:1,o.bumpTexture!==void 0&&r.push(n.assignTexture(t,"bumpMap",o.bumpTexture)),Promise.all(r)}},qc=class{constructor(e){this.parser=e,this.name=Xe.KHR_MATERIALS_ANISOTROPY}getMaterialType(e){let n=this.parser.json.materials[e];return!n.extensions||!n.extensions[this.name]?null:xt}extendMaterialParams(e,t){let n=this.parser,i=n.json.materials[e];if(!i.extensions||!i.extensions[this.name])return Promise.resolve();let r=[],o=i.extensions[this.name];return o.anisotropyStrength!==void 0&&(t.anisotropy=o.anisotropyStrength),o.anisotropyRotation!==void 0&&(t.anisotropyRotation=o.anisotropyRotation),o.anisotropyTexture!==void 0&&r.push(n.assignTexture(t,"anisotropyMap",o.anisotropyTexture)),Promise.all(r)}},Yc=class{constructor(e){this.parser=e,this.name=Xe.KHR_TEXTURE_BASISU}loadTexture(e){let t=this.parser,n=t.json,i=n.textures[e];if(!i.extensions||!i.extensions[this.name])return null;let r=i.extensions[this.name],o=t.options.ktx2Loader;if(!o){if(n.extensionsRequired&&n.extensionsRequired.indexOf(this.name)>=0)throw new Error("THREE.GLTFLoader: setKTX2Loader must be called before loading KTX2 textures");return null}return t.loadTextureImage(e,r.source,o)}},$c=class{constructor(e){this.parser=e,this.name=Xe.EXT_TEXTURE_WEBP,this.isSupported=null}loadTexture(e){let t=this.name,n=this.parser,i=n.json,r=i.textures[e];if(!r.extensions||!r.extensions[t])return null;let o=r.extensions[t],a=i.images[o.source],c=n.textureLoader;if(a.uri){let l=n.options.manager.getHandler(a.uri);l!==null&&(c=l)}return this.detectSupport().then(function(l){if(l)return n.loadTextureImage(e,o.source,c);if(i.extensionsRequired&&i.extensionsRequired.indexOf(t)>=0)throw new Error("THREE.GLTFLoader: WebP required by asset but unsupported.");return n.loadTexture(e)})}detectSupport(){return this.isSupported||(this.isSupported=new Promise(function(e){let t=new Image;t.src="data:image/webp;base64,UklGRiIAAABXRUJQVlA4IBYAAAAwAQCdASoBAAEADsD+JaQAA3AAAAAA",t.onload=t.onerror=function(){e(t.height===1)}})),this.isSupported}},Zc=class{constructor(e){this.parser=e,this.name=Xe.EXT_TEXTURE_AVIF,this.isSupported=null}loadTexture(e){let t=this.name,n=this.parser,i=n.json,r=i.textures[e];if(!r.extensions||!r.extensions[t])return null;let o=r.extensions[t],a=i.images[o.source],c=n.textureLoader;if(a.uri){let l=n.options.manager.getHandler(a.uri);l!==null&&(c=l)}return this.detectSupport().then(function(l){if(l)return n.loadTextureImage(e,o.source,c);if(i.extensionsRequired&&i.extensionsRequired.indexOf(t)>=0)throw new Error("THREE.GLTFLoader: AVIF required by asset but unsupported.");return n.loadTexture(e)})}detectSupport(){return this.isSupported||(this.isSupported=new Promise(function(e){let t=new Image;t.src="data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUIAAADybWV0YQAAAAAAAAAoaGRscgAAAAAAAAAAcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAAAAADnBpdG0AAAAAAAEAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAAABcAAAAoaWluZgAAAAAAAQAAABppbmZlAgAAAAABAABhdjAxQ29sb3IAAAAAamlwcnAAAABLaXBjbwAAABRpc3BlAAAAAAAAAAEAAAABAAAAEHBpeGkAAAAAAwgICAAAAAxhdjFDgQAMAAAAABNjb2xybmNseAACAAIABoAAAAAXaXBtYQAAAAAAAAABAAEEAQKDBAAAAB9tZGF0EgAKCBgABogQEDQgMgkQAAAAB8dSLfI=",t.onload=t.onerror=function(){e(t.height===1)}})),this.isSupported}},Kc=class{constructor(e){this.name=Xe.EXT_MESHOPT_COMPRESSION,this.parser=e}loadBufferView(e){let t=this.parser.json,n=t.bufferViews[e];if(n.extensions&&n.extensions[this.name]){let i=n.extensions[this.name],r=this.parser.getDependency("buffer",i.buffer),o=this.parser.options.meshoptDecoder;if(!o||!o.supported){if(t.extensionsRequired&&t.extensionsRequired.indexOf(this.name)>=0)throw new Error("THREE.GLTFLoader: setMeshoptDecoder must be called before loading compressed files");return null}return r.then(function(a){let c=i.byteOffset||0,l=i.byteLength||0,u=i.count,h=i.byteStride,f=new Uint8Array(a,c,l);return o.decodeGltfBufferAsync?o.decodeGltfBufferAsync(u,h,f,i.mode,i.filter).then(function(p){return p.buffer}):o.ready.then(function(){let p=new ArrayBuffer(u*h);return o.decodeGltfBuffer(new Uint8Array(p),u,h,f,i.mode,i.filter),p})})}else return null}},Jc=class{constructor(e){this.name=Xe.EXT_MESH_GPU_INSTANCING,this.parser=e}createNodeMesh(e){let t=this.parser.json,n=t.nodes[e];if(!n.extensions||!n.extensions[this.name]||n.mesh===void 0)return null;let i=t.meshes[n.mesh];for(let l of i.primitives)if(l.mode!==gn.TRIANGLES&&l.mode!==gn.TRIANGLE_STRIP&&l.mode!==gn.TRIANGLE_FAN&&l.mode!==void 0)return null;let o=n.extensions[this.name].attributes,a=[],c={};for(let l in o)a.push(this.parser.getDependency("accessor",o[l]).then(u=>(c[l]=u,c[l])));return a.length<1?null:(a.push(this.parser.createNodeMesh(e)),Promise.all(a).then(l=>{let u=l.pop(),h=u.isGroup?u.children:[u],f=l[0].count,p=[];for(let g of h){let v=new Le,m=new P,d=new rn,M=new P(1,1,1),b=new xs(g.geometry,g.material,f);for(let _=0;_<f;_++)c.TRANSLATION&&m.fromBufferAttribute(c.TRANSLATION,_),c.ROTATION&&d.fromBufferAttribute(c.ROTATION,_),c.SCALE&&M.fromBufferAttribute(c.SCALE,_),b.setMatrixAt(_,v.compose(m,d,M));for(let _ in c)if(_==="_COLOR_0"){let C=c[_];b.instanceColor=new Di(C.array,C.itemSize,C.normalized)}else _!=="TRANSLATION"&&_!=="ROTATION"&&_!=="SCALE"&&g.geometry.setAttribute(_,c[_]);gt.prototype.copy.call(b,g),this.parser.assignFinalMaterial(b),p.push(b)}return u.isGroup?(u.clear(),u.add(...p),u):p[0]}))}},Sh="glTF",or=12,_h={JSON:1313821514,BIN:5130562},jc=class{constructor(e){this.name=Xe.KHR_BINARY_GLTF,this.content=null,this.body=null;let t=new DataView(e,0,or),n=new TextDecoder;if(this.header={magic:n.decode(new Uint8Array(e.slice(0,4))),version:t.getUint32(4,!0),length:t.getUint32(8,!0)},this.header.magic!==Sh)throw new Error("THREE.GLTFLoader: Unsupported glTF-Binary header.");if(this.header.version<2)throw new Error("THREE.GLTFLoader: Legacy binary file detected.");let i=this.header.length-or,r=new DataView(e,or),o=0;for(;o<i;){let a=r.getUint32(o,!0);o+=4;let c=r.getUint32(o,!0);if(o+=4,c===_h.JSON){let l=new Uint8Array(e,or+o,a);this.content=n.decode(l)}else if(c===_h.BIN){let l=or+o;this.body=e.slice(l,l+a)}o+=a}if(this.content===null)throw new Error("THREE.GLTFLoader: JSON content not found.")}},Qc=class{constructor(e,t){if(!t)throw new Error("THREE.GLTFLoader: No DRACOLoader instance provided.");this.name=Xe.KHR_DRACO_MESH_COMPRESSION,this.json=e,this.dracoLoader=t,this.dracoLoader.preload()}decodePrimitive(e,t){let n=this.json,i=this.dracoLoader,r=e.extensions[this.name].bufferView,o=e.extensions[this.name].attributes,a={},c={},l={};for(let u in o){let h=il[u]||u.toLowerCase();a[h]=o[u]}for(let u in e.attributes){let h=il[u]||u.toLowerCase();if(o[u]!==void 0){let f=n.accessors[e.attributes[u]],p=Ss[f.componentType];l[h]=p.name,c[h]=f.normalized===!0}}return t.getDependency("bufferView",r).then(function(u){return new Promise(function(h,f){i.decodeDracoFile(u,function(p){for(let g in p.attributes){let v=p.attributes[g],m=c[g];m!==void 0&&(v.normalized=m)}h(p)},a,l,Wt,f)})})}},el=class{constructor(){this.name=Xe.KHR_TEXTURE_TRANSFORM}extendTexture(e,t){return(t.texCoord===void 0||t.texCoord===e.channel)&&t.offset===void 0&&t.rotation===void 0&&t.scale===void 0||(e=e.clone(),t.texCoord!==void 0&&(e.channel=t.texCoord),t.offset!==void 0&&e.offset.fromArray(t.offset),t.rotation!==void 0&&(e.rotation=t.rotation),t.scale!==void 0&&e.repeat.fromArray(t.scale),e.needsUpdate=!0),e}},tl=class{constructor(){this.name=Xe.KHR_MESH_QUANTIZATION}},_o=class extends fi{constructor(e,t,n,i){super(e,t,n,i)}copySampleValue_(e){let t=this.resultBuffer,n=this.sampleValues,i=this.valueSize,r=e*i*3+i;for(let o=0;o!==i;o++)t[o]=n[r+o];return t}interpolate_(e,t,n,i){let r=this.resultBuffer,o=this.sampleValues,a=this.valueSize,c=a*2,l=a*3,u=i-t,h=(n-t)/u,f=h*h,p=f*h,g=e*l,v=g-l,m=-2*p+3*f,d=p-f,M=1-m,b=d-f+h;for(let _=0;_!==a;_++){let C=o[v+_+a],A=o[v+_+c]*u,E=o[g+_+a],I=o[g+_]*u;r[_]=M*C+b*A+m*E+d*I}return r}},lv=new rn,nl=class extends _o{interpolate_(e,t,n,i){let r=super.interpolate_(e,t,n,i);return lv.fromArray(r).normalize().toArray(r),r}},gn={FLOAT:5126,FLOAT_MAT3:35675,FLOAT_MAT4:35676,FLOAT_VEC2:35664,FLOAT_VEC3:35665,FLOAT_VEC4:35666,LINEAR:9729,REPEAT:10497,SAMPLER_2D:35678,POINTS:0,LINES:1,LINE_LOOP:2,LINE_STRIP:3,TRIANGLES:4,TRIANGLE_STRIP:5,TRIANGLE_FAN:6,UNSIGNED_BYTE:5121,UNSIGNED_SHORT:5123},Ss={5120:Int8Array,5121:Uint8Array,5122:Int16Array,5123:Uint16Array,5125:Uint32Array,5126:Float32Array},yh={9728:yt,9729:wt,9984:xc,9985:Gs,9986:Ji,9987:Pn},Mh={33071:En,33648:Ys,10497:qn},Pc={SCALAR:1,VEC2:2,VEC3:3,VEC4:4,MAT2:4,MAT3:9,MAT4:16},il={POSITION:"position",NORMAL:"normal",TANGENT:"tangent",TEXCOORD_0:"uv",TEXCOORD_1:"uv1",TEXCOORD_2:"uv2",TEXCOORD_3:"uv3",COLOR_0:"color",WEIGHTS_0:"skinWeight",JOINTS_0:"skinIndex"},xi={scale:"scale",translation:"position",rotation:"quaternion",weights:"morphTargetInfluences"},uv={CUBICSPLINE:void 0,LINEAR:us,STEP:ls},Lc={OPAQUE:"OPAQUE",MASK:"MASK",BLEND:"BLEND"};function hv(s){return s.DefaultMaterial===void 0&&(s.DefaultMaterial=new Dn({color:16777215,emissive:0,metalness:1,roughness:1,transparent:!1,depthTest:!0,side:en})),s.DefaultMaterial}function Ui(s,e,t){for(let n in t.extensions)s[n]===void 0&&(e.userData.gltfExtensions=e.userData.gltfExtensions||{},e.userData.gltfExtensions[n]=t.extensions[n])}function Qn(s,e){e.extras!==void 0&&(typeof e.extras=="object"?Object.assign(s.userData,e.extras):console.warn("THREE.GLTFLoader: Ignoring primitive type .extras, "+e.extras))}function fv(s,e,t){let n=!1,i=!1,r=!1;for(let l=0,u=e.length;l<u;l++){let h=e[l];if(h.POSITION!==void 0&&(n=!0),h.NORMAL!==void 0&&(i=!0),h.COLOR_0!==void 0&&(r=!0),n&&i&&r)break}if(!n&&!i&&!r)return Promise.resolve(s);let o=[],a=[],c=[];for(let l=0,u=e.length;l<u;l++){let h=e[l];if(n){let f=h.POSITION!==void 0?t.getDependency("accessor",h.POSITION):s.attributes.position;o.push(f)}if(i){let f=h.NORMAL!==void 0?t.getDependency("accessor",h.NORMAL):s.attributes.normal;a.push(f)}if(r){let f=h.COLOR_0!==void 0?t.getDependency("accessor",h.COLOR_0):s.attributes.color;c.push(f)}}return Promise.all([Promise.all(o),Promise.all(a),Promise.all(c)]).then(function(l){let u=l[0],h=l[1],f=l[2];return n&&(s.morphAttributes.position=u),i&&(s.morphAttributes.normal=h),r&&(s.morphAttributes.color=f),s.morphTargetsRelative=!0,s})}function dv(s,e){if(s.updateMorphTargets(),e.weights!==void 0)for(let t=0,n=e.weights.length;t<n;t++)s.morphTargetInfluences[t]=e.weights[t];if(e.extras&&Array.isArray(e.extras.targetNames)){let t=e.extras.targetNames;if(s.morphTargetInfluences.length===t.length){s.morphTargetDictionary={};for(let n=0,i=t.length;n<i;n++)s.morphTargetDictionary[t[n]]=n}else console.warn("THREE.GLTFLoader: Invalid extras.targetNames length. Ignoring names.")}}function pv(s){let e,t=s.extensions&&s.extensions[Xe.KHR_DRACO_MESH_COMPRESSION];if(t?e="draco:"+t.bufferView+":"+t.indices+":"+Dc(t.attributes):e=s.indices+":"+Dc(s.attributes)+":"+s.mode,s.targets!==void 0)for(let n=0,i=s.targets.length;n<i;n++)e+=":"+Dc(s.targets[n]);return e}function Dc(s){let e="",t=Object.keys(s).sort();for(let n=0,i=t.length;n<i;n++)e+=t[n]+":"+s[t[n]]+";";return e}function sl(s){switch(s){case Int8Array:return 1/127;case Uint8Array:return 1/255;case Int16Array:return 1/32767;case Uint16Array:return 1/65535;default:throw new Error("THREE.GLTFLoader: Unsupported normalized accessor component type.")}}function mv(s){return s.search(/\.jpe?g($|\?)/i)>0||s.search(/^data\:image\/jpeg/)===0?"image/jpeg":s.search(/\.webp($|\?)/i)>0||s.search(/^data\:image\/webp/)===0?"image/webp":s.search(/\.ktx2($|\?)/i)>0||s.search(/^data\:image\/ktx2/)===0?"image/ktx2":"image/png"}var gv=new Le,rl=class{constructor(e={},t={}){this.json=e,this.extensions={},this.plugins={},this.options=t,this.cache=new cv,this.associations=new Map,this.primitiveCache={},this.nodeCache={},this.meshCache={refs:{},uses:{}},this.cameraCache={refs:{},uses:{}},this.lightCache={refs:{},uses:{}},this.sourceCache={},this.textureCache={},this.nodeNamesUsed={};let n=!1,i=-1,r=!1,o=-1;if(typeof navigator<"u"){let a=navigator.userAgent;n=/^((?!chrome|android).)*safari/i.test(a)===!0;let c=a.match(/Version\/(\d+)/);i=n&&c?parseInt(c[1],10):-1,r=a.indexOf("Firefox")>-1,o=r?a.match(/Firefox\/([0-9]+)\./)[1]:-1}typeof createImageBitmap>"u"||n&&i<17||r&&o<98?this.textureLoader=new ys(this.options.manager):this.textureLoader=new fo(this.options.manager),this.textureLoader.setCrossOrigin(this.options.crossOrigin),this.textureLoader.setRequestHeader(this.options.requestHeader),this.fileLoader=new ir(this.options.manager),this.fileLoader.setResponseType("arraybuffer"),this.options.crossOrigin==="use-credentials"&&this.fileLoader.setWithCredentials(!0)}setExtensions(e){this.extensions=e}setPlugins(e){this.plugins=e}parse(e,t){let n=this,i=this.json,r=this.extensions;this.cache.removeAll(),this.nodeCache={},this._invokeAll(function(o){return o._markDefs&&o._markDefs()}),Promise.all(this._invokeAll(function(o){return o.beforeRoot&&o.beforeRoot()})).then(function(){return Promise.all([n.getDependencies("scene"),n.getDependencies("animation"),n.getDependencies("camera")])}).then(function(o){let a={scene:o[0][i.scene||0],scenes:o[0],animations:o[1],cameras:o[2],asset:i.asset,parser:n,userData:{}};return Ui(r,a,i),Qn(a,i),Promise.all(n._invokeAll(function(c){return c.afterRoot&&c.afterRoot(a)})).then(function(){for(let c of a.scenes)c.updateMatrixWorld();e(a)})}).catch(t)}_markDefs(){let e=this.json.nodes||[],t=this.json.skins||[],n=this.json.meshes||[];for(let i=0,r=t.length;i<r;i++){let o=t[i].joints;for(let a=0,c=o.length;a<c;a++)e[o[a]].isBone=!0}for(let i=0,r=e.length;i<r;i++){let o=e[i];o.mesh!==void 0&&(this._addNodeRef(this.meshCache,o.mesh),o.skin!==void 0&&(n[o.mesh].isSkinnedMesh=!0)),o.camera!==void 0&&this._addNodeRef(this.cameraCache,o.camera)}}_addNodeRef(e,t){t!==void 0&&(e.refs[t]===void 0&&(e.refs[t]=e.uses[t]=0),e.refs[t]++)}_getNodeRef(e,t,n){if(e.refs[t]<=1)return n;let i=n.clone(),r=(o,a)=>{let c=this.associations.get(o);c!=null&&this.associations.set(a,c);for(let[l,u]of o.children.entries())r(u,a.children[l])};return r(n,i),i.name+="_instance_"+e.uses[t]++,i}_invokeOne(e){let t=Object.values(this.plugins);t.push(this);for(let n=0;n<t.length;n++){let i=e(t[n]);if(i)return i}return null}_invokeAll(e){let t=Object.values(this.plugins);t.unshift(this);let n=[];for(let i=0;i<t.length;i++){let r=e(t[i]);r&&n.push(r)}return n}getDependency(e,t){let n=e+":"+t,i=this.cache.get(n);if(!i){switch(e){case"scene":i=this.loadScene(t);break;case"node":i=this._invokeOne(function(r){return r.loadNode&&r.loadNode(t)});break;case"mesh":i=this._invokeOne(function(r){return r.loadMesh&&r.loadMesh(t)});break;case"accessor":i=this.loadAccessor(t);break;case"bufferView":i=this._invokeOne(function(r){return r.loadBufferView&&r.loadBufferView(t)});break;case"buffer":i=this.loadBuffer(t);break;case"material":i=this._invokeOne(function(r){return r.loadMaterial&&r.loadMaterial(t)});break;case"texture":i=this._invokeOne(function(r){return r.loadTexture&&r.loadTexture(t)});break;case"skin":i=this.loadSkin(t);break;case"animation":i=this._invokeOne(function(r){return r.loadAnimation&&r.loadAnimation(t)});break;case"camera":i=this.loadCamera(t);break;default:if(i=this._invokeOne(function(r){return r!=this&&r.getDependency&&r.getDependency(e,t)}),!i)throw new Error("Unknown type: "+e);break}this.cache.add(n,i)}return i}getDependencies(e){let t=this.cache.get(e);if(!t){let n=this,i=this.json[e+(e==="mesh"?"es":"s")]||[];t=Promise.all(i.map(function(r,o){return n.getDependency(e,o)})),this.cache.add(e,t)}return t}loadBuffer(e){let t=this.json.buffers[e],n=this.fileLoader;if(t.type&&t.type!=="arraybuffer")throw new Error("THREE.GLTFLoader: "+t.type+" buffer type is not supported.");if(t.uri===void 0&&e===0)return Promise.resolve(this.extensions[Xe.KHR_BINARY_GLTF].body);let i=this.options;return new Promise(function(r,o){n.load(gi.resolveURL(t.uri,i.path),r,void 0,function(){o(new Error('THREE.GLTFLoader: Failed to load buffer "'+t.uri+'".'))})})}loadBufferView(e){let t=this.json.bufferViews[e];return this.getDependency("buffer",t.buffer).then(function(n){let i=t.byteLength||0,r=t.byteOffset||0;return n.slice(r,r+i)})}loadAccessor(e){let t=this,n=this.json,i=this.json.accessors[e];if(i.bufferView===void 0&&i.sparse===void 0){let o=Pc[i.type],a=Ss[i.componentType],c=i.normalized===!0,l=new a(i.count*o);return Promise.resolve(new it(l,o,c))}let r=[];return i.bufferView!==void 0?r.push(this.getDependency("bufferView",i.bufferView)):r.push(null),i.sparse!==void 0&&(r.push(this.getDependency("bufferView",i.sparse.indices.bufferView)),r.push(this.getDependency("bufferView",i.sparse.values.bufferView))),Promise.all(r).then(function(o){let a=o[0],c=Pc[i.type],l=Ss[i.componentType],u=l.BYTES_PER_ELEMENT,h=u*c,f=i.byteOffset||0,p=i.bufferView!==void 0?n.bufferViews[i.bufferView].byteStride:void 0,g=i.normalized===!0,v,m;if(p&&p!==h){let d=Math.floor(f/p),M="InterleavedBuffer:"+i.bufferView+":"+i.componentType+":"+d+":"+i.count,b=t.cache.get(M);b||(v=new l(a,d*p,i.count*p/u),b=new Js(v,p/u),t.cache.add(M,b)),m=new js(b,c,f%p/u,g)}else a===null?v=new l(i.count*c):v=new l(a,f,i.count*c),m=new it(v,c,g);if(i.sparse!==void 0){let d=Pc.SCALAR,M=Ss[i.sparse.indices.componentType],b=i.sparse.indices.byteOffset||0,_=i.sparse.values.byteOffset||0,C=new M(o[1],b,i.sparse.count*d),A=new l(o[2],_,i.sparse.count*c);a!==null&&(m=new it(m.array.slice(),m.itemSize,m.normalized)),m.normalized=!1;for(let E=0,I=C.length;E<I;E++){let x=C[E];if(m.setX(x,A[E*c]),c>=2&&m.setY(x,A[E*c+1]),c>=3&&m.setZ(x,A[E*c+2]),c>=4&&m.setW(x,A[E*c+3]),c>=5)throw new Error("THREE.GLTFLoader: Unsupported itemSize in sparse BufferAttribute.")}m.normalized=g}return m})}loadTexture(e){let t=this.json,n=this.options,r=t.textures[e].source,o=t.images[r],a=this.textureLoader;if(o.uri){let c=n.manager.getHandler(o.uri);c!==null&&(a=c)}return this.loadTextureImage(e,r,a)}loadTextureImage(e,t,n){let i=this,r=this.json,o=r.textures[e],a=r.images[t],c=(a.uri||a.bufferView)+":"+o.sampler;if(this.textureCache[c])return this.textureCache[c];let l=this.loadImageSource(t,n).then(function(u){u.flipY=!1,u.name=o.name||a.name||"",u.name===""&&typeof a.uri=="string"&&a.uri.startsWith("data:image/")===!1&&(u.name=a.uri);let f=(r.samplers||{})[o.sampler]||{};return u.magFilter=yh[f.magFilter]||wt,u.minFilter=yh[f.minFilter]||Pn,u.wrapS=Mh[f.wrapS]||qn,u.wrapT=Mh[f.wrapT]||qn,u.generateMipmaps=!u.isCompressedTexture&&u.minFilter!==yt&&u.minFilter!==wt,i.associations.set(u,{textures:e}),u}).catch(function(){return null});return this.textureCache[c]=l,l}loadImageSource(e,t){let n=this,i=this.json,r=this.options;if(this.sourceCache[e]!==void 0)return this.sourceCache[e].then(h=>h.clone());let o=i.images[e],a=self.URL||self.webkitURL,c=o.uri||"",l=!1;if(o.bufferView!==void 0)c=n.getDependency("bufferView",o.bufferView).then(function(h){l=!0;let f=new Blob([h],{type:o.mimeType});return c=a.createObjectURL(f),c});else if(o.uri===void 0)throw new Error("THREE.GLTFLoader: Image "+e+" is missing URI and bufferView");let u=Promise.resolve(c).then(function(h){return new Promise(function(f,p){let g=f;t.isImageBitmapLoader===!0&&(g=function(v){let m=new Pt(v);m.needsUpdate=!0,f(m)}),t.load(gi.resolveURL(h,r.path),g,void 0,p)})}).then(function(h){return l===!0&&a.revokeObjectURL(c),Qn(h,o),h.userData.mimeType=o.mimeType||mv(o.uri),h}).catch(function(h){throw console.error("THREE.GLTFLoader: Couldn't load texture",c),h});return this.sourceCache[e]=u,u}assignTexture(e,t,n,i){let r=this;return this.getDependency("texture",n.index).then(function(o){if(!o)return null;if(n.texCoord!==void 0&&n.texCoord>0&&(o=o.clone(),o.channel=n.texCoord),r.extensions[Xe.KHR_TEXTURE_TRANSFORM]){let a=n.extensions!==void 0?n.extensions[Xe.KHR_TEXTURE_TRANSFORM]:void 0;if(a){let c=r.associations.get(o);o=r.extensions[Xe.KHR_TEXTURE_TRANSFORM].extendTexture(o,a),r.associations.set(o,c)}}return i!==void 0&&(o.colorSpace=i),e[t]=o,o})}assignFinalMaterial(e){let t=e.geometry,n=e.material,i=t.attributes.tangent===void 0,r=t.attributes.color!==void 0,o=t.attributes.normal===void 0;if(e.isPoints){let a="PointsMaterial:"+n.uuid,c=this.cache.get(a);c||(c=new tr,an.prototype.copy.call(c,n),c.color.copy(n.color),c.map=n.map,c.sizeAttenuation=!1,this.cache.add(a,c)),n=c}else if(e.isLine){let a="LineBasicMaterial:"+n.uuid,c=this.cache.get(a);c||(c=new er,an.prototype.copy.call(c,n),c.color.copy(n.color),c.map=n.map,this.cache.add(a,c)),n=c}if(i||r||o){let a="ClonedMaterial:"+n.uuid+":";i&&(a+="derivative-tangents:"),r&&(a+="vertex-colors:"),o&&(a+="flat-shading:");let c=this.cache.get(a);c||(c=n.clone(),r&&(c.vertexColors=!0),o&&(c.flatShading=!0),i&&(c.normalScale&&(c.normalScale.y*=-1),c.clearcoatNormalScale&&(c.clearcoatNormalScale.y*=-1)),this.cache.add(a,c),this.associations.set(c,this.associations.get(n))),n=c}e.material=n}getMaterialType(){return Dn}loadMaterial(e){let t=this,n=this.json,i=this.extensions,r=n.materials[e],o,a={},c=r.extensions||{},l=[];if(c[Xe.KHR_MATERIALS_UNLIT]){let h=i[Xe.KHR_MATERIALS_UNLIT];o=h.getMaterialType(),l.push(h.extendParams(a,r,t))}else{let h=r.pbrMetallicRoughness||{};if(a.color=new ve(1,1,1),a.opacity=1,Array.isArray(h.baseColorFactor)){let f=h.baseColorFactor;a.color.setRGB(f[0],f[1],f[2],Wt),a.opacity=f[3]}h.baseColorTexture!==void 0&&l.push(t.assignTexture(a,"map",h.baseColorTexture,St)),a.metalness=h.metallicFactor!==void 0?h.metallicFactor:1,a.roughness=h.roughnessFactor!==void 0?h.roughnessFactor:1,h.metallicRoughnessTexture!==void 0&&(l.push(t.assignTexture(a,"metalnessMap",h.metallicRoughnessTexture)),l.push(t.assignTexture(a,"roughnessMap",h.metallicRoughnessTexture))),o=this._invokeOne(function(f){return f.getMaterialType&&f.getMaterialType(e)}),l.push(Promise.all(this._invokeAll(function(f){return f.extendMaterialParams&&f.extendMaterialParams(e,a)})))}r.doubleSided===!0&&(a.side=Lt);let u=r.alphaMode||Lc.OPAQUE;if(u===Lc.BLEND?(a.transparent=!0,a.depthWrite=!1):(a.transparent=!1,u===Lc.MASK&&(a.alphaTest=r.alphaCutoff!==void 0?r.alphaCutoff:.5)),r.normalTexture!==void 0&&o!==Yt&&(l.push(t.assignTexture(a,"normalMap",r.normalTexture)),a.normalScale=new le(1,1),r.normalTexture.scale!==void 0)){let h=r.normalTexture.scale;a.normalScale.set(h,h)}if(r.occlusionTexture!==void 0&&o!==Yt&&(l.push(t.assignTexture(a,"aoMap",r.occlusionTexture)),r.occlusionTexture.strength!==void 0&&(a.aoMapIntensity=r.occlusionTexture.strength)),r.emissiveFactor!==void 0&&o!==Yt){let h=r.emissiveFactor;a.emissive=new ve().setRGB(h[0],h[1],h[2],Wt)}return r.emissiveTexture!==void 0&&o!==Yt&&l.push(t.assignTexture(a,"emissiveMap",r.emissiveTexture,St)),Promise.all(l).then(function(){let h=new o(a);return r.name&&(h.name=r.name),Qn(h,r),t.associations.set(h,{materials:e}),r.extensions&&Ui(i,h,r),h})}createUniqueName(e){let t=dt.sanitizeNodeName(e||"");return t in this.nodeNamesUsed?t+"_"+ ++this.nodeNamesUsed[t]:(this.nodeNamesUsed[t]=0,t)}loadGeometries(e){let t=this,n=this.extensions,i=this.primitiveCache;function r(a){return n[Xe.KHR_DRACO_MESH_COMPRESSION].decodePrimitive(a,t).then(function(c){return bh(c,a,t)})}let o=[];for(let a=0,c=e.length;a<c;a++){let l=e[a],u=pv(l),h=i[u];if(h)o.push(h.promise);else{let f;l.extensions&&l.extensions[Xe.KHR_DRACO_MESH_COMPRESSION]?f=r(l):f=bh(new Mt,l,t),i[u]={primitive:l,promise:f},o.push(f)}}return Promise.all(o)}loadMesh(e){let t=this,n=this.json,i=this.extensions,r=n.meshes[e],o=r.primitives,a=[];for(let c=0,l=o.length;c<l;c++){let u=o[c].material===void 0?hv(this.cache):this.getDependency("material",o[c].material);a.push(u)}return a.push(t.loadGeometries(o)),Promise.all(a).then(function(c){let l=c.slice(0,c.length-1),u=c[c.length-1],h=[];for(let p=0,g=u.length;p<g;p++){let v=u[p],m=o[p],d,M=l[p];if(m.mode===gn.TRIANGLES||m.mode===gn.TRIANGLE_STRIP||m.mode===gn.TRIANGLE_FAN||m.mode===void 0)d=r.isSkinnedMesh===!0?new gs(v,M):new Fe(v,M),d.isSkinnedMesh===!0&&d.normalizeSkinWeights(),m.mode===gn.TRIANGLE_STRIP?d.geometry=Ic(d.geometry,mo):m.mode===gn.TRIANGLE_FAN&&(d.geometry=Ic(d.geometry,rr));else if(m.mode===gn.LINES)d=new so(v,M);else if(m.mode===gn.LINE_STRIP)d=new _s(v,M);else if(m.mode===gn.LINE_LOOP)d=new ro(v,M);else if(m.mode===gn.POINTS)d=new oo(v,M);else throw new Error("THREE.GLTFLoader: Primitive mode unsupported: "+m.mode);Object.keys(d.geometry.morphAttributes).length>0&&dv(d,r),d.name=t.createUniqueName(r.name||"mesh_"+e),Qn(d,r),m.extensions&&Ui(i,d,m),t.assignFinalMaterial(d),h.push(d)}for(let p=0,g=h.length;p<g;p++)t.associations.set(h[p],{meshes:e,primitives:p});if(h.length===1)return r.extensions&&Ui(i,h[0],r),h[0];let f=new Qt;r.extensions&&Ui(i,f,r),t.associations.set(f,{meshes:e});for(let p=0,g=h.length;p<g;p++)f.add(h[p]);return f})}loadCamera(e){let t,n=this.json.cameras[e],i=n[n.type];if(!i){console.warn("THREE.GLTFLoader: Missing camera parameters.");return}return n.type==="perspective"?t=new _t(vi.radToDeg(i.yfov),i.aspectRatio||1,i.znear||1,i.zfar||2e6):n.type==="orthographic"&&(t=new hi(-i.xmag,i.xmag,i.ymag,-i.ymag,i.znear,i.zfar)),n.name&&(t.name=this.createUniqueName(n.name)),Qn(t,n),Promise.resolve(t)}loadSkin(e){let t=this.json.skins[e],n=[];for(let i=0,r=t.joints.length;i<r;i++)n.push(this._loadNodeShallow(t.joints[i]));return t.inverseBindMatrices!==void 0?n.push(this.getDependency("accessor",t.inverseBindMatrices)):n.push(null),Promise.all(n).then(function(i){let r=i.pop(),o=i,a=[],c=[];for(let l=0,u=o.length;l<u;l++){let h=o[l];if(h){a.push(h);let f=new Le;r!==null&&f.fromArray(r.array,l*16),c.push(f)}else console.warn('THREE.GLTFLoader: Joint "%s" could not be found.',t.joints[l])}return new to(a,c)})}loadAnimation(e){let t=this.json,n=this,i=t.animations[e],r=i.name?i.name:"animation_"+e,o=[],a=[],c=[],l=[],u=[];for(let h=0,f=i.channels.length;h<f;h++){let p=i.channels[h],g=i.samplers[p.sampler],v=p.target,m=v.node,d=i.parameters!==void 0?i.parameters[g.input]:g.input,M=i.parameters!==void 0?i.parameters[g.output]:g.output;v.node!==void 0&&(o.push(this.getDependency("node",m)),a.push(this.getDependency("accessor",d)),c.push(this.getDependency("accessor",M)),l.push(g),u.push(v))}return Promise.all([Promise.all(o),Promise.all(a),Promise.all(c),Promise.all(l),Promise.all(u)]).then(function(h){let f=h[0],p=h[1],g=h[2],v=h[3],m=h[4],d=[];for(let M=0,b=f.length;M<b;M++){let _=f[M],C=p[M],A=g[M],E=v[M],I=m[M];if(_===void 0)continue;_.updateMatrix&&_.updateMatrix();let x=n._createAnimationTracks(_,C,A,E,I);if(x)for(let y=0;y<x.length;y++)d.push(x[y])}return new uo(r,void 0,d)})}createNodeMesh(e){let t=this.json,n=this,i=t.nodes[e];return i.mesh===void 0?null:n.getDependency("mesh",i.mesh).then(function(r){let o=n._getNodeRef(n.meshCache,i.mesh,r);return i.weights!==void 0&&o.traverse(function(a){if(a.isMesh)for(let c=0,l=i.weights.length;c<l;c++)a.morphTargetInfluences[c]=i.weights[c]}),o})}loadNode(e){let t=this.json,n=this,i=t.nodes[e],r=n._loadNodeShallow(e),o=[],a=i.children||[];for(let l=0,u=a.length;l<u;l++)o.push(n.getDependency("node",a[l]));let c=i.skin===void 0?Promise.resolve(null):n.getDependency("skin",i.skin);return Promise.all([r,Promise.all(o),c]).then(function(l){let u=l[0],h=l[1],f=l[2];f!==null&&u.traverse(function(p){p.isSkinnedMesh&&p.bind(f,gv)});for(let p=0,g=h.length;p<g;p++)u.add(h[p]);return u})}_loadNodeShallow(e){let t=this.json,n=this.extensions,i=this;if(this.nodeCache[e]!==void 0)return this.nodeCache[e];let r=t.nodes[e],o=r.name?i.createUniqueName(r.name):"",a=[],c=i._invokeOne(function(l){return l.createNodeMesh&&l.createNodeMesh(e)});return c&&a.push(c),r.camera!==void 0&&a.push(i.getDependency("camera",r.camera).then(function(l){return i._getNodeRef(i.cameraCache,r.camera,l)})),i._invokeAll(function(l){return l.createNodeAttachment&&l.createNodeAttachment(e)}).forEach(function(l){a.push(l)}),this.nodeCache[e]=Promise.all(a).then(function(l){let u;if(r.isBone===!0?u=new Qs:l.length>1?u=new Qt:l.length===1?u=l[0]:u=new gt,u!==l[0])for(let h=0,f=l.length;h<f;h++)u.add(l[h]);if(r.name&&(u.userData.name=r.name,u.name=o),Qn(u,r),r.extensions&&Ui(n,u,r),r.matrix!==void 0){let h=new Le;h.fromArray(r.matrix),u.applyMatrix4(h)}else r.translation!==void 0&&u.position.fromArray(r.translation),r.rotation!==void 0&&u.quaternion.fromArray(r.rotation),r.scale!==void 0&&u.scale.fromArray(r.scale);return i.associations.has(u)||i.associations.set(u,{}),i.associations.get(u).nodes=e,u}),this.nodeCache[e]}loadScene(e){let t=this.extensions,n=this.json.scenes[e],i=this,r=new Qt;n.name&&(r.name=i.createUniqueName(n.name)),Qn(r,n),n.extensions&&Ui(t,r,n);let o=n.nodes||[],a=[];for(let c=0,l=o.length;c<l;c++)a.push(i.getDependency("node",o[c]));return Promise.all(a).then(function(c){for(let u=0,h=c.length;u<h;u++)r.add(c[u]);let l=u=>{let h=new Map;for(let[f,p]of i.associations)(f instanceof an||f instanceof Pt)&&h.set(f,p);return u.traverse(f=>{let p=i.associations.get(f);p!=null&&h.set(f,p)}),h};return i.associations=l(r),r})}_createAnimationTracks(e,t,n,i,r){let o=[],a=e.name?e.name:e.uuid,c=[];xi[r.path]===xi.weights?e.traverse(function(f){f.morphTargetInfluences&&c.push(f.name?f.name:f.uuid)}):c.push(a);let l;switch(xi[r.path]){case xi.weights:l=$n;break;case xi.rotation:l=Zn;break;case xi.position:case xi.scale:l=Kn;break;default:switch(n.itemSize){case 1:l=$n;break;case 2:case 3:default:l=Kn;break}break}let u=i.interpolation!==void 0?uv[i.interpolation]:us,h=this._getArrayFromAccessor(n);for(let f=0,p=c.length;f<p;f++){let g=new l(c[f]+"."+xi[r.path],t.array,h,u);i.interpolation==="CUBICSPLINE"&&this._createCubicSplineTrackInterpolant(g),o.push(g)}return o}_getArrayFromAccessor(e){let t=e.array;if(e.normalized){let n=sl(t.constructor),i=new Float32Array(t.length);for(let r=0,o=t.length;r<o;r++)i[r]=t[r]*n;t=i}return t}_createCubicSplineTrackInterpolant(e){e.createInterpolant=function(n){let i=this instanceof Zn?nl:_o;return new i(this.times,this.values,this.getValueSize()/3,n)},e.createInterpolant.isInterpolantFactoryMethodGLTFCubicSpline=!0}};function vv(s,e,t){let n=e.attributes,i=new dn;if(n.POSITION!==void 0){let a=t.json.accessors[n.POSITION],c=a.min,l=a.max;if(c!==void 0&&l!==void 0){if(i.set(new P(c[0],c[1],c[2]),new P(l[0],l[1],l[2])),a.normalized){let u=sl(Ss[a.componentType]);i.min.multiplyScalar(u),i.max.multiplyScalar(u)}}else{console.warn("THREE.GLTFLoader: Missing min/max properties for accessor POSITION.");return}}else return;let r=e.targets;if(r!==void 0){let a=new P,c=new P;for(let l=0,u=r.length;l<u;l++){let h=r[l];if(h.POSITION!==void 0){let f=t.json.accessors[h.POSITION],p=f.min,g=f.max;if(p!==void 0&&g!==void 0){if(c.setX(Math.max(Math.abs(p[0]),Math.abs(g[0]))),c.setY(Math.max(Math.abs(p[1]),Math.abs(g[1]))),c.setZ(Math.max(Math.abs(p[2]),Math.abs(g[2]))),f.normalized){let v=sl(Ss[f.componentType]);c.multiplyScalar(v)}a.max(c)}else console.warn("THREE.GLTFLoader: Missing min/max properties for accessor POSITION.")}}i.expandByVector(a)}s.boundingBox=i;let o=new on;i.getCenter(o.center),o.radius=i.min.distanceTo(i.max)/2,s.boundingSphere=o}function bh(s,e,t){let n=e.attributes,i=[];function r(o,a){return t.getDependency("accessor",o).then(function(c){s.setAttribute(a,c)})}for(let o in n){let a=il[o]||o.toLowerCase();a in s.attributes||i.push(r(n[o],a))}if(e.indices!==void 0&&!s.index){let o=t.getDependency("accessor",e.indices).then(function(a){s.setIndex(a)});i.push(o)}return Ye.workingColorSpace!==Wt&&"COLOR_0"in n&&console.warn(`THREE.GLTFLoader: Converting vertex colors from "srgb-linear" to "${Ye.workingColorSpace}" not supported.`),Qn(s,e),vv(s,e,t),Promise.all(i).then(function(){return e.targets!==void 0?fv(s,e.targets,t):s})}var xv=s=>{let e=Math.sin(s*127.1+311.7)*43758.5453;return e-Math.floor(e)},Kt=(s,e)=>xv(s*157.31+e*113.97+.5);var ol=s=>s<=.04045?s/12.92:Math.pow((s+.055)/1.055,2.4),_i=s=>{let e=new ve;return e.r=(s>>16&255)/255,e.g=(s>>8&255)/255,e.b=(s&255)/255,e},Tt=s=>{let e=_i(s);return e.r=ol(e.r),e.g=ol(e.g),e.b=ol(e.b),e};var yo=`
float h12(vec2 p) { vec3 p3 = fract(vec3(p.xyx) * 0.1031); p3 += dot(p3, p3.yzx + 33.33); return fract((p3.x + p3.y) * p3.z); }
vec2 h22(vec2 p) { vec3 p3 = fract(vec3(p.xyx) * vec3(0.1031, 0.1030, 0.0973)); p3 += dot(p3, p3.yzx + 33.33); return fract((p3.xx + p3.yz) * p3.zy); }
float h13(vec3 p3) { p3 = fract(p3 * 0.1031); p3 += dot(p3, p3.zyx + 31.32); return fract((p3.x + p3.y) * p3.z); }
float vnoise(vec2 p) { vec2 i = floor(p), f = fract(p); vec2 u = f * f * (3.0 - 2.0 * f);
  return mix(mix(h12(i), h12(i + vec2(1, 0)), u.x), mix(h12(i + vec2(0, 1)), h12(i + vec2(1, 1)), u.x), u.y); }
float fbm(vec2 p) { float a = 0.0, w = 0.5; for (int i = 0; i < 4; i++) { a += w * vnoise(p); p = p * 2.03 + vec2(17.1, 9.2); w *= 0.5; } return a; }
vec3 toSRGB(vec3 c) { c = max(c, 0.0); return mix(c * 12.92, 1.055 * pow(c, vec3(1.0 / 2.4)) - 0.055, step(0.0031308, c)); }
vec3 toLin(vec3 c) { return mix(c / 12.92, pow((c + 0.055) / 1.055, vec3(2.4)), step(0.04045, c)); }
float luma(vec3 c) { return dot(c, vec3(0.2126, 0.7152, 0.0722)); }
`,ar=`
uniform float uBlink; uniform vec2 uGaze; uniform float uHappy; uniform float uTalk; uniform vec4 uBars; uniform float uBar5;
uniform float uEyeGlow; uniform float uSquint; uniform float uRing;
float sdEll(vec2 p, vec2 r) { float k0 = length(p / r); float k1 = length(p / (r * r)); return k0 * (k0 - 1.0) / max(k1, 1e-5); }
float sdRound(vec2 p, vec2 b, float rr) { vec2 q = abs(p) - b + rr; return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - rr; }
// signed distance to the face shapes (negative inside), in visor units
float faceSD(vec2 p) {
  float dm = 1e5;
  for (int i = 0; i < 2; i++) {
    float sx = i == 0 ? -1.0 : 1.0;
    vec2 c = vec2(sx, 0.02) + uGaze;
    float open = max(0.07, 1.0 - uBlink);
    vec2 r = vec2(0.39 * (1.0 + 0.08 * uBlink), 0.58 * open * (1.0 - 0.25 * uSquint));
    float d = sdEll(p - c, r);
    float dh = max(d, -sdEll(p - c - vec2(0.0, -0.34), vec2(0.46, 0.62)));
    d = mix(d, dh, uHappy);
    dm = min(dm, d);
  }
  float bars[5]; bars[0] = uBars.x; bars[1] = uBars.y; bars[2] = uBars.z; bars[3] = uBars.w; bars[4] = uBar5;
  if (uTalk > 0.01) for (int k = 0; k < 5; k++) {
    float h = 0.035 + 0.20 * bars[k];
    float d = sdRound(p - vec2(-0.36 + 0.18 * float(k), -1.0), vec2(0.045, h), 0.045);
    dm = min(dm, d + (1.0 - uTalk) * 0.3);
  }
  return dm;
}
float screenFace(vec2 p) { return 1.0 - smoothstep(-0.03, 0.03, faceSD(p)); }
`,al=`
uniform sampler2D uLogo;
float logoMask(vec3 rp, vec3 rn) {
  const float AX = 0.023, AZ = 0.005, RREF = 0.215, W = 0.27, YC = 0.385, H = 0.0241;
  float th = atan(rp.x - AX, rp.z - AZ);
  float lu = (th * RREF + W * 0.5) / W, lv = (YC + H * 0.5 - rp.y) / H;
  vec2 rd = normalize(vec2(rp.x - AX, rp.z - AZ));
  float facing = dot(normalize(rn.xz), rd);
  if (lu < 0.0 || lu > 1.0 || lv < 0.0 || lv > 1.0 || rp.z < 0.0 || facing < 0.35) return 0.0;
  return texture2D(uLogo, vec2(lu, lv)).a;
}
`,_v=`
#include <common>
#include <skinning_pars_vertex>
#ifdef ROBOT
attribute vec3 _face;
attribute vec3 aSmoothN;
attribute vec3 aBlobN;
attribute vec3 aCls;
varying vec3 vFace;
varying vec3 vCls;
#else
attribute float aPal;
flat varying int vPal;
#endif
#ifdef SNAP
uniform vec2 uSnap;
#endif
#ifdef AFFINE
varying vec3 vAff;
#endif
varying vec3 vN; varying vec3 vNV; varying vec3 vW; varying vec3 vRest; varying vec3 vRestN; varying vec2 vUv; varying float vDepth;
#ifdef VLIGHT
uniform vec3 uKeyDir; uniform vec3 uKeyCol; uniform vec3 uAmbUp; uniform vec3 uAmbDn;
varying vec3 vGouraud;
#endif
void main() {
  vUv = uv;
  #include <beginnormal_vertex>
  #if defined(ROBOT) && defined(BLOBN)
  objectNormal = aBlobN;
  #elif defined(ROBOT) && defined(SMOOTHN)
  objectNormal = aSmoothN;
  #endif
  #include <skinbase_vertex>
  #include <skinnormal_vertex>
  #include <defaultnormal_vertex>
  #include <begin_vertex>
  #include <skinning_vertex>
  #include <project_vertex>
  vNV = normalize(transformedNormal);
  vN = normalize((vec4(transformedNormal, 0.0) * viewMatrix).xyz);
  vW = (modelMatrix * vec4(transformed, 1.0)).xyz;
  vRest = position; vRestN = normal;
  #if defined(ROBOT) && defined(SMOOTHN)
  vRestN = aSmoothN;
  #endif
  vDepth = -mvPosition.z;
  #ifdef ROBOT
  vFace = _face; vCls = aCls;
  #else
  vPal = int(aPal + 0.5);
  #endif
  #ifdef SNAP
  vec4 cp = gl_Position; cp.xy = floor(cp.xy / cp.w * uSnap + 0.5) / uSnap * cp.w; gl_Position = cp;
  #endif
  #ifdef AFFINE
  vec3 an = abs(vN); vec2 puv = an.y > 0.5 ? vW.xz : (an.z > 0.5 ? vW.xy : vW.zy);
  vAff = vec3(puv * gl_Position.w, gl_Position.w);
  #endif
  #ifdef VLIGHT
  float nl = max(dot(vN, normalize(uKeyDir)), 0.0);
  vGouraud = uKeyCol * nl + mix(uAmbDn, uAmbUp, vN.y * 0.5 + 0.5);
  #endif
}
`,yv=`
#ifdef ROBOT
varying vec3 vFace; varying vec3 vCls;
uniform sampler2D uMap; uniform sampler2D uEmi;
#else
flat varying int vPal;
#endif
varying vec3 vN; varying vec3 vNV; varying vec3 vW; varying vec3 vRest; varying vec3 vRestN; varying vec2 vUv; varying float vDepth;
#ifdef MRT
layout(location = 1) out highp vec4 gOut1;
// G-buffer: view normal xy, inverse view depth (planes are linear in screen space -> clean Laplacian edges), surface id
void writeG(float id) { vec3 n = normalize(vNV); n = gl_FrontFacing ? n : -n; gOut1 = vec4(n.xy * 0.5 + 0.5, 1.0 / max(vDepth, 1e-3), id); }
#endif
`,Mv=`
struct RobotSurf { float white; float dark; float grey; float blue; float visor; float rim; float eye; float eyeSD; float logo; vec3 alb; };
RobotSurf robotSurf() {
  RobotSurf s;
  s.alb = texture2D(uMap, vUv).rgb;
  float fw = max(fwidth(vCls.x), 1e-3) * 0.8;
  float wv = smoothstep(0.5 - fw, 0.5 + fw, vCls.x);
  float fb = max(fwidth(vCls.y), 1e-3) * 0.8;
  s.blue = smoothstep(0.42 - fb, 0.42 + fb, vCls.y) * (1.0 - smoothstep(0.3, 0.8, vFace.z));
  // visor = geometric ellipse in rest space (front of the helmet) -> one clean visor outline in every style
  float ell = pow((vRest.x - 0.078) / 0.27, 2.0) + pow((vRest.y - 0.647) / 0.18, 2.0);
  float front = step(0.1, vRest.z) * step(0.0, vRestN.z);
  float fe = fwidth(ell) + 1e-4;
  s.visor = max(smoothstep(0.08, 0.3, vFace.z), (1.0 - smoothstep(1.2 - fe, 1.2 + fe, ell)) * front);
  s.eyeSD = vFace.z > 0.01 ? faceSD(vFace.xy) : 1e3;
  s.eye = vFace.z > 0.01 ? screenFace(vFace.xy) * smoothstep(0.2, 0.6, vFace.z) : 0.0;
  // the dark bezel just outside the glass reads as white shell (the scan texture is ragged there)
  float bez = (1.0 - smoothstep(1.55, 1.65, ell)) * front * (1.0 - s.visor);
  wv = max(wv, bez * (1.0 - s.blue));
  s.white = wv * (1.0 - s.blue) * (1.0 - s.visor);
  s.rim = 0.0;
  s.dark = (1.0 - s.white) * (1.0 - s.blue);
  s.grey = smoothstep(0.45, 0.55, vCls.z) * s.dark * (1.0 - s.visor);
  s.logo = logoMask(vRest, vRestN) * s.white;
  return s;
}
`,ws=`
float robotId(RobotSurf s) {
  if (s.eye > 0.5) return 34.0;
  if (s.visor > 0.5) return 33.0;
  if (s.blue > 0.5) return 32.0;
  if (s.white > 0.5) return 30.0;
  return 31.0;
}
`,yi=`
uniform sampler2D tG; uniform vec2 uTexel;
vec3 decN(vec2 e) { vec2 f = e * 2.0 - 1.0; return vec3(f, sqrt(max(0.0, 1.0 - dot(f, f)))); }
float edgeTerm(vec4 c, vec3 n, vec4 a, vec4 b, vec3 k, inout float ie) {
  float lap = (2.0 * c.z - a.z - b.z) / max(c.z, 1e-4);
  float de = smoothstep(k.x, k.x * 2.5, lap);
  float ne = 0.0;
  if (a.w > 0.5) ne = max(ne, 1.0 - dot(n, decN(a.xy)));
  if (b.w > 0.5) ne = max(ne, 1.0 - dot(n, decN(b.xy)));
  ne = smoothstep(k.y, k.y * 1.7, ne) * step(abs(a.z - b.z) / max(c.z, 1e-4), 0.25);
  ie = max(ie, max(step(0.5, c.w - a.w) * step(0.5, a.w), step(0.5, c.w - b.w) * step(0.5, b.w)) * step(c.w, 33.5));
  return max(de, ne);
}
float edgeG(vec2 uv, float r, vec3 k) {
  vec4 c = texture2D(tG, uv);
  if (c.w < 0.5) return 0.0;
  vec3 n = decN(c.xy);
  vec2 o = uTexel * r;
  float ie = 0.0, e = 0.0;
  e = max(e, edgeTerm(c, n, texture2D(tG, uv + vec2(o.x, 0.0)), texture2D(tG, uv - vec2(o.x, 0.0)), k, ie));
  e = max(e, edgeTerm(c, n, texture2D(tG, uv + vec2(0.0, o.y)), texture2D(tG, uv - vec2(0.0, o.y)), k, ie));
  e = max(e, 0.85 * edgeTerm(c, n, texture2D(tG, uv + o), texture2D(tG, uv - o), k, ie));
  e = max(e, 0.85 * edgeTerm(c, n, texture2D(tG, uv + vec2(o.x, -o.y)), texture2D(tG, uv + vec2(-o.x, o.y)), k, ie));
  return max(e, ie * k.z);
}
// background silhouette: background pixel next to geometry (for outer outlines that grow outward)
float silOut(vec2 uv, float r) {
  vec4 c = texture2D(tG, uv); if (c.w > 0.5) return 0.0;
  vec2 o = uTexel * r; float m = 0.0;
  m = max(m, texture2D(tG, uv + vec2(o.x, 0.0)).w); m = max(m, texture2D(tG, uv - vec2(o.x, 0.0)).w);
  m = max(m, texture2D(tG, uv + vec2(0.0, o.y)).w); m = max(m, texture2D(tG, uv - vec2(0.0, o.y)).w);
  return step(0.5, m);
}
`,bv=`
uniform sampler2D tSrc; uniform vec2 uDir; varying vec2 vUv;
void main() {
  vec4 s = texture2D(tSrc, vUv) * 0.2270270270;
  s += (texture2D(tSrc, vUv + uDir * 1.3846153846) + texture2D(tSrc, vUv - uDir * 1.3846153846)) * 0.3162162162;
  s += (texture2D(tSrc, vUv + uDir * 3.2307692308) + texture2D(tSrc, vUv - uDir * 3.2307692308)) * 0.0702702703;
  gl_FragColor = s;
}`,ln=class{constructor(e,t,n){this.a=st(e,t,{depth:!1,type:n}),this.b=st(e,t,{depth:!1,type:n}),this.p=new Je(bv,{tSrc:{value:null},uDir:{value:new le}}),this.w=e,this.h=t,this.out=this.b}run(e,t,n=1,i=1){let r=t;for(let o=0;o<i;o++)this.p.u.tSrc.value=r,this.p.u.uDir.value.set(n/this.w,0),this.p.render(e,this.a),this.p.u.tSrc.value=this.a.texture,this.p.u.uDir.value.set(0,n/this.h),this.p.render(e,this.b),r=this.b.texture;return this.b.texture}},cl=new Mt;cl.setAttribute("position",new nt([-1,3,0,-1,-1,0,3,-1,0],3));cl.setAttribute("uv",new nt([0,2,0,0,2,0],2));var Sv=new hi(-1,1,1,-1,0,1),wv="varying vec2 vUv; void main() { vUv = uv; gl_Position = vec4(position.xy, 0.0, 1.0); }",Je=class{constructor(e,t={},n={}){this.material=new Gt({vertexShader:wv,fragmentShader:yo+e,uniforms:t,depthTest:!1,depthWrite:!1,...n}),this.mesh=new Fe(cl,this.material),this.mesh.frustumCulled=!1,this.u=this.material.uniforms}render(e,t){e.setRenderTarget(t||null),e.render(this.mesh,Sv)}};function st(s,e,t={}){let n=new Rn(s,e,{type:t.type??$e,format:Ht,depthBuffer:t.depth!==!1,samples:t.samples||0,count:t.count||1,minFilter:t.nearest?yt:wt,magFilter:t.nearest?yt:wt,generateMipmaps:!1});t.depthTexture&&(n.depthTexture=new ms(s,e),n.depthTexture.type=Yn);for(let i of n.textures)i.minFilter=n.texture.minFilter,i.magFilter=n.texture.magFilter,i.generateMipmaps=!1;return n}function Jt({robot:s,frag:e,uniforms:t={},defines:n={},shared:i,side:r=en,extra:o="",rawNormals:a=!1,blob:c=!1}){let l={...n};s&&(l.ROBOT="",a||(l.SMOOTHN=""),c&&(l.BLOBN=""));let u={...t};s&&i&&Object.assign(u,i.faceU,{uMap:i.map,uEmi:i.emi,uLogo:i.logo});let h=yo+(s?ar+al:"")+yv+(s?Mv:"")+o+e;return new Gt({vertexShader:_v,fragmentShader:h,uniforms:u,defines:l,side:r})}async function Th(s,e){let n=(await new xo().loadAsync(s)).scene,i={root:n,rigRoot:n.getObjectByName("rig_root"),bones:{},mesh:null};n.traverse(c=>{c.isBone&&(i.bones[c.name]=c),c.isSkinnedMesh&&(i.mesh=c)}),i.rest={};for(let[c,l]of Object.entries(i.bones))i.rest[c]=l.position.clone();let r=i.mesh;r.frustumCulled=!1,i.orig=r.material;let o={uBlink:{value:0},uGaze:{value:new le},uHappy:{value:0},uTalk:{value:0},uBars:{value:new We},uBar5:{value:0},uEyeGlow:{value:1},uSquint:{value:0},uRing:{value:1}},a=await new ys().loadAsync(e);return a.flipY=!1,a.colorSpace=fn,a.anisotropy=4,a.needsUpdate=!0,i.shared={faceU:o,map:{value:i.orig.map},emi:{value:i.orig.emissiveMap},logo:{value:a}},i.logoTex=a,Tv(r.geometry,.035,2),i.texPix={base:wh(i.orig.map.image,1024),emi:wh(i.orig.emissiveMap.image,1024)},Ev(r.geometry,i.texPix),i}function wh(s,e){let t=document.createElement("canvas");t.width=t.height=e;let n=t.getContext("2d",{willReadFrequently:!0});return n.drawImage(s,0,0,e,e),{size:e,data:n.getImageData(0,0,e,e).data}}function Eh(s,e,t){let n=Math.min(s.size-1,Math.max(0,Math.floor(e*s.size))),r=4*(Math.min(s.size-1,Math.max(0,Math.floor(t*s.size)))*s.size+n);return[s.data[r]/255,s.data[r+1]/255,s.data[r+2]/255]}function Ev(s,e){let t=s.attributes.position,n=s.attributes.uv,i=t.count,r=new Float32Array(i*3);for(let g=0;g<i;g++)r[3*g]=t.getX(g),r[3*g+1]=t.getY(g),r[3*g+2]=t.getZ(g);let o=new Float32Array(i*3);for(let g=0;g<i;g++){let v=n.getX(g),m=n.getY(g),d=Eh(e.base,v,m),M=Eh(e.emi,v,m),b=.2126*d[0]+.7152*d[1]+.0722*d[2];o[3*g]=b>.5?1:0,o[3*g+1]=M[2]>.45?1:0,o[3*g+2]=b>.22&&b<=.5?1:0}let a=.02,c=new Map,l=(g,v,m)=>(g+512)*1048576+(v+512)*1024+(m+512);for(let g=0;g<i;g++){let v=l(Math.floor(r[3*g]/a),Math.floor(r[3*g+1]/a),Math.floor(r[3*g+2]/a)),m=c.get(v);m||c.set(v,m=[]),m.push(g)}let u=new Float32Array(i*3),h=[.02,.009,.016];for(let g=0;g<i;g++){let v=r[3*g],m=r[3*g+1],d=r[3*g+2],M=Math.floor(v/a),b=Math.floor(m/a),_=Math.floor(d/a),C=[0,0,0],A=[0,0,0];for(let E=-1;E<=1;E++)for(let I=-1;I<=1;I++)for(let x=-1;x<=1;x++){let y=c.get(l(M+E,b+I,_+x));if(y)for(let T of y){let L=r[3*T]-v,D=r[3*T+1]-m,F=r[3*T+2]-d,X=L*L+D*D+F*F;for(let z=0;z<3;z++){let K=h[z]*h[z];if(X<K){let H=1-X/K;C[z]+=o[3*T+z]*H,A[z]+=H}}}}for(let E=0;E<3;E++)u[3*g+E]=A[E]>0?C[E]/A[E]:o[3*g+E]}let f=s.attributes.skinIndex,p=s.attributes.skinWeight;for(let g of[2,3]){let v=[];for(let E=0;E<i;E++)f.getX(E)===g&&p.getX(E)>.5&&v.push(E);if(v.length<50)continue;let m=[0,0,0],d=0;for(let E of v){for(let I=0;I<3;I++)m[I]+=r[3*E+I];d+=u[3*E]}m=m.map(E=>E/v.length),d/=v.length;let M=[0,0,0];for(let E of v)for(let I=0;I<3;I++)M[I]+=(r[3*E+I]-m[I])*(u[3*E]-d);let b=Math.hypot(...M)||1;for(let E=0;E<3;E++)M[E]/=b;let _=v.map(E=>(r[3*E]-m[0])*M[0]+(r[3*E+1]-m[1])*M[1]+(r[3*E+2]-m[2])*M[2]),C=[..._].sort((E,I)=>E-I),A=C[Math.min(C.length-1,Math.floor((1-d)*C.length))];v.forEach((E,I)=>{let x=(_[I]-A)/.006;u[3*E]=Math.max(0,Math.min(1,.5+.5*x))})}s.setAttribute("aCls",new it(u,3))}function Tv(s,e,t=1){let n=s.attributes.position,i=s.attributes.normal,r=n.count,o=new Float32Array(r*3),a=new Float32Array(r*3);for(let d=0;d<r;d++)o[3*d]=n.getX(d),o[3*d+1]=n.getY(d),o[3*d+2]=n.getZ(d),a[3*d]=i.getX(d),a[3*d+1]=i.getY(d),a[3*d+2]=i.getZ(d);let c=e,l=new Map,u=(d,M,b)=>(d+512)*1048576+(M+512)*1024+(b+512);for(let d=0;d<r;d++){let M=u(Math.floor(o[3*d]/c),Math.floor(o[3*d+1]/c),Math.floor(o[3*d+2]/c)),b=l.get(M);b||l.set(M,b=[]),b.push(d)}let h=new Float32Array(r*3),f=e*e;for(let d=0;d<t;d++){if(d>0){let M=h;h=new Float32Array(r*3);for(let b=0;b<3*r;b++)a[b]=M[b]}for(let M=0;M<r;M++){let b=o[3*M],_=o[3*M+1],C=o[3*M+2],A=a[3*M],E=a[3*M+1],I=a[3*M+2],x=Math.floor(b/c),y=Math.floor(_/c),T=Math.floor(C/c),L=0,D=0,F=0;for(let z=-1;z<=1;z++)for(let K=-1;K<=1;K++)for(let H=-1;H<=1;H++){let k=l.get(u(x+z,y+K,T+H));if(k)for(let $ of k){let ie=o[3*$]-b,j=o[3*$+1]-_,ue=o[3*$+2]-C,G=ie*ie+j*j+ue*ue;if(G>f)continue;let J=A*a[3*$]+E*a[3*$+1]+I*a[3*$+2];if(J<=.2)continue;let re=(1-G/f)*J;L+=a[3*$]*re,D+=a[3*$+1]*re,F+=a[3*$+2]*re}}let X=Math.hypot(L,D,F)||1;h[3*M]=L/X,h[3*M+1]=D/X,h[3*M+2]=F/X}}s.setAttribute("aSmoothN",new it(h,3));let p=[[.02,.33,0],[.03,.63,.03],[.386,.224,.02],[-.38,.282,.142]],g=s.attributes.skinIndex,v=s.attributes.skinWeight,m=new Float32Array(r*3);for(let d=0;d<r;d++){let M=g.getX(d),b=v.getX(d);v.getY(d)>b&&(M=g.getY(d),b=v.getY(d));let _=p[M]||p[0],C=o[3*d]-_[0],A=(o[3*d+1]-_[1])*(M===0?.6:1),E=o[3*d+2]-_[2],I=Math.hypot(C,A,E)||1;C/=I,A/=I,E/=I;let x=h[3*d]*.45+C*.55,y=h[3*d+1]*.45+A*.55,T=h[3*d+2]*.45+E*.55,L=Math.hypot(x,y,T)||1;m[3*d]=x/L,m[3*d+1]=y/L,m[3*d+2]=T/L}s.setAttribute("aBlobN",new it(m,3))}function Ah(s,e){let t=e.root||{},n=s.rigRoot;n.position.set(t.x||0,t.y||0,t.z||0),n.rotation.set(t.rx||0,t.ry||0,t.rz||0,"YXZ");let i=t.s==null?1:t.s;n.scale.set(i,i,i);for(let[c,l]of Object.entries(s.bones)){let u=e.bones&&e.bones[c]||[0,0,0];l.rotation.set(u[0],u[1],u[2],"XYZ");let h=e.offs&&e.offs[c]||[0,0,0];l.position.set(s.rest[c].x+h[0],s.rest[c].y+h[1],s.rest[c].z+h[2])}let r=e.face||{},o=s.shared.faceU;o.uBlink.value=r.blink||0,o.uGaze.value.set(...r.gaze||[0,0]),o.uHappy.value=r.happy||0,o.uSquint.value=r.squint||0,o.uTalk.value=r.talk||0;let a=r.bars||[0,0,0,0,0];o.uBars.value.set(a[0],a[1],a[2],a[3]),o.uBar5.value=a[4]||0,o.uEyeGlow.value=r.glow==null?1:r.glow,o.uRing.value=e.ring==null?1:e.ring,s.visible=e.visible!==!1,s.root.updateMatrixWorld(!0)}function Mo(s,e={}){let t=s.orig,n=new(e.physical?xt:Dn)({map:t.map,normalMap:e.noNormal?null:t.normalMap,roughnessMap:t.roughnessMap,metalnessMap:t.metalnessMap,emissiveMap:t.emissiveMap,emissive:new ve(1,1,1),emissiveIntensity:1,metalness:t.metalness,roughness:t.roughness});e.physical&&(n.clearcoat=e.clearcoat??.6,n.clearcoatRoughness=e.clearcoatRoughness??.12),t.normalScale&&n.normalMap&&n.normalScale.copy(t.normalScale);let i=s.shared.faceU,r={uTint:{value:new P(...e.tintWhite||[1,1,1])},uDarkTint:{value:new P(...e.tintDark||[1,1,1])},uEmiCol:{value:new P(...e.emi||[1,1,1])},uEyeCol:{value:new P(...e.eye||[.82,.92,1])},uEyeAlb:{value:new P(...e.eyeAlb||[.93,.97,1])},uRough:{value:new le(...e.rough||[0,1])},uEyeK:{value:e.eyeK??.95},uEmiK:{value:e.emiK??1},uVisorRough:{value:e.visorRough??-1}};n.userData.u=r;let o=e.classes;return o&&Object.assign(r,{uCW:{value:new P(...o.white)},uCD:{value:new P(...o.dark)},uCB:{value:new P(...o.blue)},uCV:{value:new P(...o.visor)},uCL:{value:new P(...o.logo||[.05,.05,.08])},uLogo:s.shared.logo}),n.onBeforeCompile=a=>{Object.assign(a.uniforms,i,r),a.vertexShader=a.vertexShader.replace("#include <beginnormal_vertex>",e.smoothN?`vec3 objectNormal = aSmoothN;
#ifdef USE_TANGENT
vec3 objectTangent = vec3( tangent.xyz );
#endif`:"#include <beginnormal_vertex>").replace("#include <common>",`#include <common>
attribute vec3 aSmoothN;
attribute vec3 _face;
attribute vec3 aCls;
varying vec3 vFace;
varying vec3 vCls;
varying vec3 vRestP;
varying vec3 vRestN;`).replace("#include <begin_vertex>",`#include <begin_vertex>
vFace = _face; vCls = aCls; vRestP = position; vRestN = normal;`),a.fragmentShader=a.fragmentShader.replace("#include <common>",`#include <common>
varying vec3 vFace; varying vec3 vCls; varying vec3 vRestP; varying vec3 vRestN;
uniform vec3 uTint; uniform vec3 uDarkTint; uniform vec3 uEmiCol; uniform vec3 uEyeCol; uniform vec3 uEyeAlb; uniform vec2 uRough; uniform float uEyeK; uniform float uEmiK; uniform float uVisorRough;
`+ar+(o?`uniform vec3 uCW; uniform vec3 uCD; uniform vec3 uCB; uniform vec3 uCV; uniform vec3 uCL;
`+al:"")).replace("#include <map_fragment>",`#include <map_fragment>
        float faceA = vFace.z > 0.01 ? screenFace(vFace.xy) * vFace.z : 0.0;
        float lumA = dot(diffuseColor.rgb, vec3(0.2126, 0.7152, 0.0722));
        float wht = smoothstep(0.10, 0.45, lumA);
        diffuseColor.rgb *= mix(uDarkTint, uTint, wht);
        float ellV = pow((vRestP.x - 0.078) / 0.27, 2.0) + pow((vRestP.y - 0.647) / 0.18, 2.0);
        float frV = step(0.1, vRestP.z) * step(0.0, vRestN.z);
        float visM = max(smoothstep(0.08, 0.3, vFace.z), (1.0 - smoothstep(1.17, 1.23, ellV)) * frV);
        ${o?`
        float cw = smoothstep(0.45, 0.55, vCls.x), cb = smoothstep(0.37, 0.47, vCls.y) * (1.0 - visM);
        cw = max(cw, (1.0 - smoothstep(1.55, 1.65, ellV)) * frV);
        vec3 cc = mix(uCD, uCW, cw); cc = mix(cc, uCB, cb); cc = mix(cc, uCV, visM);
        cc = mix(cc, uCL, smoothstep(0.35, 0.6, logoMask(vRestP, vRestN)) * cw * (1.0 - visM));
        diffuseColor.rgb = cc;`:""}
        diffuseColor.rgb = mix(diffuseColor.rgb, uEyeAlb, faceA);`).replace("#include <roughnessmap_fragment>",`#include <roughnessmap_fragment>
        roughnessFactor = clamp(roughnessFactor * uRough.y + uRough.x, 0.02, 1.0);
        if (uVisorRough >= 0.0) roughnessFactor = mix(roughnessFactor, uVisorRough, visM);
        roughnessFactor = mix(roughnessFactor, 0.35, faceA);`).replace("#include <emissivemap_fragment>",`#include <emissivemap_fragment>
        totalEmissiveRadiance *= uEmiCol * uEmiK * uRing;
        totalEmissiveRadiance += uEyeCol * faceA * uEyeK * uEyeGlow;`)},n.customProgramCacheKey=()=>"sb-litrobot-"+(e.key||"x")+(e.physical?"p":"s")+(e.smoothN?"n":""),n}var cr=new P;function vn(s,e,t,n,i,r){let o=2*Math.PI*i/4,a=Math.max(r-2*i,0),c=Math.PI/4;cr.copy(e),cr[n]=0,cr.normalize();let l=.5*o/(o+a),u=1-cr.angleTo(s)/c;return Math.sign(cr[t])===1?u*l:a/(o+a)+l+l*(1-u)}var bo=class extends cn{constructor(e=1,t=1,n=1,i=2,r=.1){if(i=i*2+1,r=Math.min(e/2,t/2,n/2,r),super(1,1,1,i,i,i),i===1)return;let o=this.toNonIndexed();this.index=null,this.attributes.position=o.attributes.position,this.attributes.normal=o.attributes.normal,this.attributes.uv=o.attributes.uv;let a=new P,c=new P,l=new P(e,t,n).divideScalar(2).subScalar(r),u=this.attributes.position.array,h=this.attributes.normal.array,f=this.attributes.uv.array,p=u.length/6,g=new P,v=.5/i;for(let m=0,d=0;m<u.length;m+=3,d+=2)switch(a.fromArray(u,m),c.copy(a),c.x-=Math.sign(c.x)*v,c.y-=Math.sign(c.y)*v,c.z-=Math.sign(c.z)*v,c.normalize(),u[m+0]=l.x*Math.sign(a.x)+c.x*r,u[m+1]=l.y*Math.sign(a.y)+c.y*r,u[m+2]=l.z*Math.sign(a.z)+c.z*r,h[m+0]=c.x,h[m+1]=c.y,h[m+2]=c.z,Math.floor(m/p)){case 0:g.set(1,0,0),f[d+0]=vn(g,c,"z","y",r,n),f[d+1]=1-vn(g,c,"y","z",r,t);break;case 1:g.set(-1,0,0),f[d+0]=1-vn(g,c,"z","y",r,n),f[d+1]=1-vn(g,c,"y","z",r,t);break;case 2:g.set(0,1,0),f[d+0]=1-vn(g,c,"x","z",r,e),f[d+1]=vn(g,c,"z","x",r,n);break;case 3:g.set(0,-1,0),f[d+0]=1-vn(g,c,"x","z",r,e),f[d+1]=1-vn(g,c,"z","x",r,n);break;case 4:g.set(0,0,1),f[d+0]=1-vn(g,c,"x","y",r,e),f[d+1]=1-vn(g,c,"y","x",r,t);break;case 5:g.set(0,0,-1),f[d+0]=vn(g,c,"x","y",r,e),f[d+1]=1-vn(g,c,"y","x",r,t);break}}};var V={floor:0,wall:1,trim:2,deskTop:3,deskBody:4,monitor:5,screen:6,bar1:7,bar2:8,bar3:9,bar4:10,board:11,boardFrame:12,leaf:13,pot:14,winFrame:15,sky:16,city:17,clock:18,clockHand:19,keyboard:20,mug:21,axis:22,soil:23},Nt=24,Ct={wallZ:-1.3,win:{x0:-1.25,x1:-.35,y0:1,y1:1.72},desk:{x:-.98,z:-.8,w:1.05,d:.5,h:.6},board:{x:.52,z:-1,w:.6,h:.47,y0:.9},plant:{x:.86,z:.36},clock:{x:.25,y:1.8}};function So({round:s=0,seg:e=1}={}){let t=[],n=(k,$,ie,j=s)=>j>0?new bo(k,$,ie,3,Math.min(j,k/2.01,$/2.01,ie/2.01)):new cn(k,$,ie),i=(k,$,ie=[0,0,0],j=[0,0,0],ue)=>{let G=k.index?k.toNonIndexed():k;G.attributes.uv||G.setAttribute("uv",new nt(new Float32Array(G.attributes.position.count*2),2));let J=new Le().compose(new P(...ie),new rn().setFromEuler(new pn(...j)),new P(...ue||[1,1,1]));G.applyMatrix4(J),G.setAttribute("aPal",new nt(new Float32Array(G.attributes.position.count).fill($),1));for(let re of Object.keys(G.attributes))["position","normal","uv","aPal"].includes(re)||G.deleteAttribute(re);t.push(G)},r=Ct,o=r.wallZ,a=r.win;i(new $t(9,7,9*e,7*e),V.floor,[0,0,.6],[-Math.PI/2,0,0]);let c=(k,$,ie,j)=>i(new $t($-k,j-ie,Math.max(1,Math.round(($-k)*e)),Math.max(1,Math.round((j-ie)*e))),V.wall,[(k+$)/2,(ie+j)/2,o]);c(-4.5,a.x0,0,3.4),c(a.x1,4.5,0,3.4),c(a.x0,a.x1,0,a.y0),c(a.x0,a.x1,a.y1,3.4),i(n(9,.07,.025,0),V.trim,[0,.035,o+.012]);let l=.05,u=.07,h=(a.x0+a.x1)/2,f=(a.y0+a.y1)/2,p=a.x1-a.x0,g=a.y1-a.y0;i(n(p+2*l,l,u),V.winFrame,[h,a.y1+l/2,o]),i(n(p+2*l,l,u),V.winFrame,[h,a.y0-l/2,o]),i(n(l,g,u),V.winFrame,[a.x0-l/2,f,o]),i(n(l,g,u),V.winFrame,[a.x1+l/2,f,o]),i(n(.025,g,.04),V.winFrame,[h,f,o]),i(n(p,.025,.04),V.winFrame,[h,f,o]),i(n(p+.2,.03,.13),V.winFrame,[h,a.y0-l-.012,o+.05]),i(new $t(6,3.2),V.sky,[h,1.4,o-1.6]);let v=[[-.42,.34,.16],[-.25,.52,.12],[-.1,.28,.14],[.06,.62,.15],[.22,.4,.13],[.36,.5,.12],[-.55,.45,.13],[.5,.3,.15]];for(let[k,$,ie]of v)i(n(ie,$,.1,0),V.city,[h+k*1.6,a.y0-.12+$/2,o-1.1]);let m=r.desk,d=m.h;i(n(m.w,.045,m.d),V.deskTop,[m.x,d-.022,m.z]),i(n(.04,d-.045,m.d-.04),V.deskBody,[m.x-m.w/2+.05,(d-.045)/2,m.z]),i(n(.3,d-.045,m.d-.04),V.deskBody,[m.x+m.w/2-.18,(d-.045)/2,m.z]);for(let k=0;k<3;k++)i(n(.24,.008,.01,0),V.trim,[m.x+m.w/2-.18,.12+k*.17,m.z+m.d/2-.015]);let M=m.x+.02,b=m.z-.06,_=.52,C=.32,A=d+.07+C/2;i(n(.18,.015,.11),V.monitor,[M,d+.008,b]),i(n(.04,.09,.025),V.monitor,[M,d+.05,b-.01]),i(n(_,C,.028),V.monitor,[M,A,b]),i(new $t(_-.04,C-.04),V.screen,[M,A,b+.0145]);let E=[.3,.52,.42,.8],I=[V.bar1,V.bar2,V.bar3,V.bar4];for(let k=0;k<4;k++){let $=E[k]*(C-.1);i(n(.06,$,.004,0),I[k],[M-.15+k*.1,A-(C-.1)/2+$/2-.01,b+.017])}i(n(.4,.004,.004,0),V.axis,[M,A-(C-.1)/2-.012,b+.017]),i(n(.36,.018,.12),V.keyboard,[M+.02,d+.01,m.z+.13]),i(new Zt(.035,.032,.09,16),V.mug,[m.x+m.w/2-.12,d+.045,m.z+.08]);let x=r.board,y=x.y0+x.h/2;i(n(x.w,x.h,.025),V.board,[x.x,y,x.z]),i(n(x.w+.05,.03,.04),V.boardFrame,[x.x,x.y0+x.h+.012,x.z]),i(n(x.w+.05,.03,.04),V.boardFrame,[x.x,x.y0-.012,x.z]),i(n(.03,x.h+.05,.04),V.boardFrame,[x.x-x.w/2-.012,y,x.z]),i(n(.03,x.h+.05,.04),V.boardFrame,[x.x+x.w/2+.012,y,x.z]);for(let k of[-1,1])i(n(.03,x.y0,.03),V.boardFrame,[x.x+k*(x.w/2-.06),x.y0/2,x.z-.02]),i(n(.05,.02,.3),V.boardFrame,[x.x+k*(x.w/2-.06),.01,x.z-.02]);i(n(.02,x.y0*.9,.02),V.boardFrame,[x.x,x.y0*.55,x.z-.2],[-.35,0,0]);let T=[.13,.2,.27,.36],L=x.x-x.w/2+.14,D=x.y0+.06;for(let k=0;k<4;k++)i(n(.075,T[k],.012,0),I[k],[L+k*.12,D+T[k]/2,x.z+.018]);i(n(x.w-.12,.008,.01,0),V.axis,[x.x+.02,D-.004,x.z+.016]),i(n(.008,x.h-.1,.01,0),V.axis,[x.x-x.w/2+.07,x.y0+x.h/2,x.z+.016]);let F=[[L-.03,D+.16],[L+.12,D+.22],[L+.24,D+.26],[L+.38,D+.39]];for(let k=0;k<3;k++){let[$,ie]=F[k],[j,ue]=F[k+1],G=Math.hypot(j-$,ue-ie);i(n(G+.01,.012,.008,0),V.axis,[($+j)/2,(ie+ue)/2,x.z+.03],[0,0,Math.atan2(ue-ie,j-$)])}i(new co(.025,.05,3),V.axis,[F[3][0]+.01,F[3][1]+.012,x.z+.03],[0,0,-.72]);let X=r.plant;i(new Zt(.12,.09,.24,24),V.pot,[X.x,.12,X.z]),i(new Zt(.128,.128,.035,24),V.pot,[X.x,.24,X.z]),i(new Zt(.11,.11,.01,24),V.soil,[X.x,.252,X.z]);let z=[[0,.62,0,.05],[1.1,.5,.22,.045],[2.3,.56,.18,.05],[3.4,.44,.28,.042],[4.5,.52,.2,.048],[5.5,.4,.3,.04],[.55,.36,.34,.038]];for(let[k,$,ie,j]of z){let ue=new Zt(0,j,$,6,4);ue.scale(1,1,.28),ue.translate(0,$/2,0),i(ue,V.leaf,[X.x+Math.cos(k)*.03,.25,X.z+Math.sin(k)*.03],[Math.sin(k)*ie,-k,Math.cos(k)*ie])}let K=r.clock;i(new Zt(.13,.13,.035,32),V.clock,[K.x,K.y,o+.02],[Math.PI/2,0,0]),i(new Zt(.112,.112,.01,32),V.board,[K.x,K.y,o+.04],[Math.PI/2,0,0]),i(n(.012,.085,.006,0),V.clockHand,[K.x,K.y+.035,o+.048]),i(n(.06,.012,.006,0),V.clockHand,[K.x+.026,K.y,o+.048]);let H=xh(t,!1);return H.computeBoundingSphere(),H}var Av=`
uniform sampler2D tA; uniform sampler2D tB; uniform vec2 uRes; uniform float uU; uniform vec2 uDir;
varying vec2 vUv;
vec3 sampleB(vec2 uv) { return texture2D(tB, uv).rgb; }
void main() {
  vec2 px = vUv * uRes; vec2 c = uRes * 0.5;
  float smax = 0.5 * (abs(uRes.x * uDir.x) + abs(uRes.y * uDir.y));
  float margin = 90.0;
  float pos = mix(-smax - margin, smax + margin, uU);
  float s = dot(px - c, uDir);
  float d = s - pos;                                   // < 0: already passed (style B)
  vec2 tng = vec2(-uDir.y, uDir.x);
  float along = dot(px - c, tng);
  // render-bucket fringe just ahead of the line
  float tile = 14.0;
  vec2 tid = floor(px / tile); vec2 tf = fract(px / tile);
  float th = h12(tid + 7.0);
  vec2 tc = (tid + 0.5) * tile; float tdist = dot(tc - c, uDir) - pos;
  float fringe = 64.0;
  float tileOn = step(tdist, fringe * th * th) * step(0.0, tdist) * step(0.35, h12(tid * 1.7 + 3.0));
  float isB = max(step(d, 0.0), tileOn);
  // subtle heat shimmer along the line
  float sh = exp(-abs(d) / 26.0);
  vec2 off = uDir / uRes * (sin(along * 0.09 + uU * 31.0) * 2.5 * sh);
  vec3 a = texture2D(tA, vUv + off * 0.6).rgb;
  vec3 b;
  float trail = exp(max(d, -400.0) / 46.0) * step(d, 0.0);             // 1 at the line, fading into B
  vec2 ca = uDir / uRes * 3.0 * trail;
  b = vec3(texture2D(tB, vUv - ca + off).r, texture2D(tB, vUv + off).g, texture2D(tB, vUv + ca + off).b);
  // scan rasters behind the line (lines parallel to the boundary)
  float ras = 0.5 + 0.5 * cos(6.2831853 * d / 4.0);
  b *= 1.0 - 0.16 * trail * ras;
  b += vec3(0.004, 0.8, 0.97) * 0.10 * trail;
  vec3 col = mix(a, b, isB);
  // bucket outlines + tint in the fringe
  float edge = 1.0 - smoothstep(0.0, 0.09, min(min(tf.x, tf.y), min(1.0 - tf.x, 1.0 - tf.y)));
  float inFr = step(0.0, tdist) * step(tdist, fringe);
  col += vec3(0.004, 0.8, 0.97) * (edge * 0.55 * tileOn + 0.10 * tileOn) * (1.0 - tdist / fringe);
  // ahead of the line: faint cyan pre-scan haze on A
  col += vec3(0.004, 0.8, 0.97) * 0.07 * exp(-max(d, 0.0) / 70.0) * step(0.0, d);
  // the line: white-hot core + cyan glow (#01CCF7) + wide haze
  float ad = abs(d);
  float core = exp(-ad / 1.1);
  float glow = exp(-ad / 9.0);
  float haze = exp(-ad / 60.0);
  float flick = 0.85 + 0.15 * vnoise(vec2(along * 0.035, uU * 12.0));
  vec3 cy = vec3(0.004, 0.80, 0.969);
  col = col * (1.0 - 0.35 * glow) + cy * (glow * 0.95 + haze * 0.22) * flick + vec3(0.85, 1.0, 1.0) * core * 1.1;
  // sparks riding the line
  float cell = 34.0; float k = floor(along / cell); float hk = h12(vec2(k, 3.1));
  float sa = (k + 0.5 + (hk - 0.5) * 0.6) * cell; float sd = (h12(vec2(k, 9.7)) - 0.5) * 18.0 - 4.0;
  float spark = exp(-length(vec2(along - sa, d - sd)) / 1.6) * step(0.72, hk);
  col += vec3(0.7, 1.0, 1.0) * spark * 1.4;
  gl_FragColor = vec4(min(col, vec3(1.0)), 1.0);
}`;function Rh(s){let e=new Je(Av,{tA:{value:null},tB:{value:null},uRes:{value:new le(s.W,s.H)},uU:{value:0},uDir:{value:new le(1,0)}});return{render(t,n,i,r,o){let a=vi.degToRad(r);e.u.tA.value=t,e.u.tB.value=n,e.u.uU.value=i,e.u.uDir.value.set(Math.cos(a),Math.sin(a)),e.render(s.renderer,o)}}}function Es({cols:s,rm:e,em:t,physical:n=!1,hooks:i={},uniforms:r={},key:o="x",side:a=en,phys:c={}}){let l=new(n?xt:Dn)({color:16777215,roughness:1,metalness:0,side:a,...c}),u={uCol:{value:s},uRM:{value:e.map(h=>new le(h[0],h[1]))},uEm:{value:t||s.map(()=>new ve(0,0,0))},...r};return l.userData.u=u,l.onBeforeCompile=h=>{Object.assign(h.uniforms,u),h.vertexShader=h.vertexShader.replace("#include <common>",`#include <common>
attribute float aPal;
flat varying int vPal;
varying vec3 vWPos;
`+(i.vpars||"")).replace("#include <begin_vertex>",`#include <begin_vertex>
vPal = int(aPal + 0.5);
vWPos = (modelMatrix * vec4(transformed, 1.0)).xyz;
`+(i.vertex||"")),h.fragmentShader=h.fragmentShader.replace("#include <common>",`#include <common>
flat varying int vPal;
varying vec3 vWPos;
uniform vec3 uCol[${Nt}]; uniform vec2 uRM[${Nt}]; uniform vec3 uEm[${Nt}];
`+yo+(i.pars||"")).replace("#include <map_fragment>",`#include <map_fragment>
diffuseColor.rgb = uCol[vPal];
`+(i.albedo||"")).replace("#include <roughnessmap_fragment>",`#include <roughnessmap_fragment>
roughnessFactor = uRM[vPal].x;
`+(i.rough||"")).replace("#include <metalnessmap_fragment>",`#include <metalnessmap_fragment>
metalnessFactor = uRM[vPal].y;
`).replace("#include <normal_fragment_maps>",`#include <normal_fragment_maps>
`+(i.normal||"")).replace("#include <emissivemap_fragment>",`#include <emissivemap_fragment>
totalEmissiveRadiance = uEm[vPal];
`+(i.emissive||"")).replace("#include <opaque_fragment>",(i.final||"")+`
#include <opaque_fragment>`)},l.customProgramCacheKey=()=>"sb-litset-"+o,l}function Ts(s,{bg:e=0,bgK:t=1,panels:n=[]}={}){let i=new Et,r=new Fe(new cn(14,8,14),new Yt({color:new ve(e).multiplyScalar(t),side:Vt}));r.position.y=3,i.add(r);for(let c of n){let l=new Fe(new $t(c.size[0],c.size[1]),new Yt({color:new ve(c.color).multiplyScalar(c.intensity),side:Lt}));l.position.set(...c.pos),l.lookAt(...c.look||[0,1,0]),i.add(l)}let o=new ps(s),a=o.fromScene(i,0,.1,30).texture;return o.dispose(),a}var wo=class{constructor(){this.cam=new _t,this.texMat=new Le}update(e){let t=new P(0,1,0),n=new P(0,0,0),i=new P().setFromMatrixPosition(e.matrixWorld),r=new Le().extractRotation(e.matrixWorld),o=n.clone().sub(i).reflect(t).negate().add(n),a=new P(0,0,-1).applyMatrix4(r).add(i),c=n.clone().sub(a).reflect(t).negate().add(n),l=this.cam;l.position.copy(o),l.up.set(0,1,0).applyMatrix4(r).reflect(t),l.lookAt(c),l.far=e.far,l.updateMatrixWorld(),l.projectionMatrix.copy(e.projectionMatrix),l.projectionMatrixInverse.copy(e.projectionMatrixInverse),this.texMat.set(.5,0,0,.5,0,.5,0,.5,0,0,.5,.5,0,0,0,1).multiply(l.projectionMatrix).multiply(l.matrixWorldInverse);let u=new Sn().setFromNormalAndCoplanarPoint(t,n).applyMatrix4(l.matrixWorldInverse),h=new We(u.normal.x,u.normal.y,u.normal.z,u.constant),f=l.projectionMatrix,p=new We;return p.x=(Math.sign(h.x)+f.elements[8])/f.elements[0],p.y=(Math.sign(h.y)+f.elements[9])/f.elements[5],p.z=-1,p.w=(1+f.elements[10])/f.elements[14],h.multiplyScalar(2/h.dot(p)),f.elements[2]=h.x,f.elements[6]=h.y,f.elements[10]=h.z+1-.003,f.elements[14]=h.w,l}};var Ze=.036,Mi=Ze*1.2,Ch=Ze*.3,ll=Ze*.2,Lh=[15922162,1780276,7106152,7328767];function Rv(s){let e=s.attributes,t=s.index.array,n=e.position.count,i=new Float32Array(n*3),r=new Float32Array(n*3),o=new Float32Array(n*3),a=new Uint8Array(n);for(let M=0;M<n;M++)i[3*M]=e.position.getX(M),i[3*M+1]=e.position.getY(M),i[3*M+2]=e.position.getZ(M),r[3*M]=e.normal.getX(M),r[3*M+1]=e.normal.getY(M),r[3*M+2]=e.normal.getZ(M),o[3*M]=e.aCls.getX(M),o[3*M+1]=e.aCls.getY(M),o[3*M+2]=e.aCls.getZ(M),a[M]=e.skinWeight.getY(M)>e.skinWeight.getX(M)?e.skinIndex.getY(M):e.skinIndex.getX(M);let c=Math.floor(-.56/Ze),l=Math.floor(-.34/Ze),u=Math.ceil(.56/Ze)-c+1,h=Math.ceil(.96/Mi)+1,f=Math.ceil(.34/Ze)-l+1,p=u*h*f,g=4,v=new Uint16Array(g*p*4),m=(M,b,_)=>(b*f+_)*u+M;for(let M=0;M<t.length;M+=3){let b=t[M],_=t[M+1],C=t[M+2],A=a[b],E=i[3*b],I=i[3*b+1],x=i[3*b+2],y=i[3*_]-E,T=i[3*_+1]-I,L=i[3*_+2]-x,D=i[3*C]-E,F=i[3*C+1]-I,X=i[3*C+2]-x,z=.5*Math.hypot(T*X-L*F,L*D-y*X,y*F-T*D),K=Math.max(1,Math.min(48,Math.ceil(z/(Ze*Ze*.06))));for(let H=0;H<K;H++){let k=(H*.6180339+.13)%1,$=(H*.7548777+.37)%1;k+$>1&&(k=1-k,$=1-$);let ie=1-k-$,j=E+y*k+D*$,ue=I+T*k+F*$,G=x+L*k+X*$,J=r[3*b+2]*ie+r[3*_+2]*k+r[3*C+2]*$,re=o[3*b]*ie+o[3*_]*k+o[3*C]*$,ee=o[3*b+1]*ie+o[3*_+1]*k+o[3*C+1]*$,oe=((j-.078)/.27)**2+((ue-.647)/.18)**2,ye=G>.1&&J>0,De=re>.5||ye&&oe<1.6?0:1;ee>.42&&(De=2),ye&&oe<1.2&&A===1&&(De=3);let Qe=Math.floor(j/Ze)-c,Ce=Math.floor(ue/Mi),qe=Math.floor(G/Ze)-l;if(Qe<0||Ce<0||qe<0||Qe>=u||Ce>=h||qe>=f)continue;let N=(A*p+m(Qe,Ce,qe))*4+De;v[N]<65e3&&v[N]++}}let d=[];for(let M=0;M<g;M++){let b=new Uint8Array(p),_=new Int8Array(p).fill(-1);for(let x=0;x<p;x++){let y=(M*p+x)*4,T=v[y],L=v[y+1],D=v[y+2],F=v[y+3];T+L+D+F<2||F>(T+L+D)*.7||(b[x]=1,_[x]=D>(T+L)*.35?3:T>=L*(M>=2?.55:1)?0:1)}let C=new Uint8Array(p),A=[];for(let x=0;x<h;x++)for(let y=0;y<f;y++)for(let T=0;T<u;T++)(T===0||x===0||y===0||T===u-1||x===h-1||y===f-1)&&!b[m(T,x,y)]&&(C[m(T,x,y)]=1,A.push(T,x,y));for(let x=0;x<A.length;x+=3){let y=A[x],T=A[x+1],L=A[x+2];for(let[D,F,X]of[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]){let z=y+D,K=T+F,H=L+X;if(z<0||K<0||H<0||z>=u||K>=h||H>=f)continue;let k=m(z,K,H);C[k]||b[k]||(C[k]=1,A.push(z,K,H))}}for(let x=0;x<p;x++)!b[x]&&!C[x]&&(b[x]=1,_[x]=1);let E=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],I=(x,y,T,L)=>{let D=0;for(let[F,X,z]of E){let K=x+F,H=y+X,k=T+z;K<0||H<0||k<0||K>=u||H>=h||k>=f||L(m(K,H,k))&&D++}return D};for(let x=0;x<2;x++){let y=[],T=[];for(let L=0;L<h;L++)for(let D=0;D<f;D++)for(let F=0;F<u;F++){let X=m(F,L,D);if(b[X]&&I(F,L,D,z=>C[z])>0&&I(F,L,D,z=>b[z])<=1)y.push(X);else if(C[X]&&I(F,L,D,z=>b[z])>=4){let z=[0,0,0,0];for(let[K,H,k]of E){let $=F+K,ie=L+H,j=D+k;if($<0||ie<0||j<0||$>=u||ie>=h||j>=f)continue;let ue=m($,ie,j);b[ue]&&_[ue]>=0&&z[_[ue]]++}T.push([X,z.indexOf(Math.max(...z))])}}for(let L of y)b[L]=0,C[L]=1,_[L]=-1;for(let[L,D]of T)b[L]=1,C[L]=0,_[L]=D}d.push({occ:b,col:_,ext:C})}return{groups:d,NX:u,NY:h,NZ:f,X0:c,Z0:l,cid:m}}function Cv(s,e){let{NX:t,NY:n,NZ:i,X0:r,Z0:o,cid:a}=s,{occ:c,col:l}=s.groups[e],u=new Int32Array(t*n*i).fill(-1),h=0;for(let T=0;T<n;T++){let L=T%2===0,D=L?i:t,F=L?t:i;for(let X=0;X<D;X++){let z=[],K=()=>{let k=0,$=(T>>1)%2===1&&z.length>2?2:0;for(;k<z.length;){let ie=$||Math.min(4,z.length-k);$=0,z.length-k-ie===1&&ie>2&&(ie-=1);for(let j=0;j<ie;j++)u[z[k+j]]=h;h++,k+=ie}z=[]},H=-2;for(let k=0;k<F;k++){let $=L?k:X,ie=L?X:k,j=a($,T,ie);c[j]&&l[j]===H?z.push(j):(K(),c[j]&&z.push(j)),H=c[j]?l[j]:-2}K()}}let f=[],p=[],g=[],v=[],m=[],d=[],M=[],b=[],_=s.groups[e].ext,C=(T,L,D)=>T<0||L<0||D<0||T>=t||L>=n||D>=i?!0:!!_[a(T,L,D)],A=(T,L,D,F)=>L<0||D<0||F<0||L>=t||D>=n||F>=i?!1:u[a(L,D,F)]===u[T],E=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],I=T=>T[1]!==0?[[1,0,0],[0,0,1]]:T[0]!==0?[[0,0,1],[0,1,0]]:[[1,0,0],[0,1,0]],x=Lh.map(T=>Tt(T));for(let T=0;T<n;T++)for(let L=0;L<i;L++)for(let D=0;D<t;D++){let F=a(D,T,L);if(!c[F])continue;let X=x[l[F]],z=(D+r+.5)*Ze,K=(T+.5)*Mi,H=(L+o+.5)*Ze;for(let k of E){if(!C(D+k[0],T+k[1],L+k[2]))continue;let[$,ie]=I(k),j=[Ze/2,Mi/2,Ze/2],ue=[z+k[0]*j[0],K+k[1]*j[1],H+k[2]*j[2]],G=$.map((Ce,qe)=>Ce*j[qe]),J=ie.map((Ce,qe)=>Ce*j[qe]),re=[!A(F,D-$[0],T-$[1],L-$[2]),!A(F,D+$[0],T+$[1],L+$[2]),!A(F,D-ie[0],T-ie[1],L-ie[2]),!A(F,D+ie[0],T+ie[1],L+ie[2])].map(Number),ee=[[-1,-1],[1,-1],[1,1],[-1,1]],oe=ee.map(([Ce,qe])=>[ue[0]+G[0]*Ce+J[0]*qe,ue[1]+G[1]*Ce+J[1]*qe,ue[2]+G[2]*Ce+J[2]*qe]),ye=[(oe[1][1]-oe[0][1])*(oe[2][2]-oe[0][2])-(oe[1][2]-oe[0][2])*(oe[2][1]-oe[0][1]),(oe[1][2]-oe[0][2])*(oe[2][0]-oe[0][0])-(oe[1][0]-oe[0][0])*(oe[2][2]-oe[0][2]),(oe[1][0]-oe[0][0])*(oe[2][1]-oe[0][1])-(oe[1][1]-oe[0][1])*(oe[2][0]-oe[0][0])],Qe=ye[0]*k[0]+ye[1]*k[1]+ye[2]*k[2]<0?[0,2,1,0,3,2]:[0,1,2,0,2,3];for(let Ce of Qe)f.push(...oe[Ce]),p.push(...k),g.push(X.r,X.g,X.b),v.push((ee[Ce][0]+1)/2,(ee[Ce][1]+1)/2),m.push(...re),d.push(...$),M.push(...ie);k[1]===1&&b.push([z,(T+1)*Mi,H,l[F]])}}let y=new Mt;return y.setAttribute("position",new nt(f,3)),y.setAttribute("normal",new nt(p,3)),y.setAttribute("color",new nt(g,3)),y.setAttribute("aLuv",new nt(v,2)),y.setAttribute("aSeam",new nt(m,4)),y.setAttribute("aT1",new nt(d,3)),y.setAttribute("aT2",new nt(M,3)),{geo:y,studs:b}}function Iv(){let s=new xt({vertexColors:!0,roughness:.3,metalness:0,clearcoat:.35,clearcoatRoughness:.18});return s.onBeforeCompile=e=>{e.vertexShader=e.vertexShader.replace("#include <common>",`#include <common>
attribute vec2 aLuv; attribute vec4 aSeam; attribute vec3 aT1; attribute vec3 aT2;
varying vec2 vLuv; varying vec4 vSeam; varying vec3 vT1; varying vec3 vT2;`).replace("#include <begin_vertex>",`#include <begin_vertex>
vLuv = aLuv; vSeam = aSeam; vT1 = normalize(mat3(modelViewMatrix) * aT1); vT2 = normalize(mat3(modelViewMatrix) * aT2);`),e.fragmentShader=e.fragmentShader.replace("#include <common>",`#include <common>
varying vec2 vLuv; varying vec4 vSeam; varying vec3 vT1; varying vec3 vT2;`).replace("#include <normal_fragment_maps>",`#include <normal_fragment_maps>
        float bw = 0.09;
        float e0 = vSeam.x * (1.0 - smoothstep(0.0, bw, vLuv.x)), e1 = vSeam.y * (1.0 - smoothstep(0.0, bw, 1.0 - vLuv.x));
        float e2 = vSeam.z * (1.0 - smoothstep(0.0, bw * 0.8, vLuv.y)), e3 = vSeam.w * (1.0 - smoothstep(0.0, bw * 0.8, 1.0 - vLuv.y));
        normal = normalize(normal + (vT1 * (e1 - e0) + vT2 * (e3 - e2)) * 1.1);
        float groove = max(max(vSeam.x * (1.0 - smoothstep(0.0, 0.022, vLuv.x)), vSeam.y * (1.0 - smoothstep(0.0, 0.022, 1.0 - vLuv.x))),
                           max(vSeam.z * (1.0 - smoothstep(0.0, 0.02, vLuv.y)), vSeam.w * (1.0 - smoothstep(0.0, 0.02, 1.0 - vLuv.y))));`).replace("#include <emissivemap_fragment>",`#include <emissivemap_fragment>
        diffuseColor.rgb *= 1.0 - 0.75 * groove;
        float isBlue = step(0.8, vColor.b) * step(vColor.r, 0.4);
        totalEmissiveRadiance += vColor.rgb * isBlue * 0.9;`)},s.customProgramCacheKey=()=>"sb-lego-brick",s}function Pv(){let s=new xt({roughness:.3,metalness:0,clearcoat:.35,clearcoatRoughness:.18});return s.onBeforeCompile=e=>{e.fragmentShader=e.fragmentShader.replace("#include <emissivemap_fragment>",`#include <emissivemap_fragment>
      #ifdef USE_INSTANCING_COLOR
      float isBlue = step(0.8, vColor.b) * step(vColor.r, 0.4); totalEmissiveRadiance += vColor.rgb * isBlue * 0.9;
      #endif`)},s.customProgramCacheKey=()=>"sb-lego-stud",s}function Ih(s){let e=new Zt(Ch,Ch,ll,s,1,!1);e.translate(0,ll/2,0);let t=e.attributes.position;for(let n=0;n<t.count;n++)t.getY(n)>ll*.99&&(t.setX(n,t.getX(n)*.93),t.setZ(n,t.getZ(n)*.93));return e.computeVertexNormals(),e}function Ph(s,e,t,n){let i=new xs(e,t,Math.max(1,s.length)),r=new Le,o=new ve;return s.forEach((a,c)=>{r.makeTranslation(a[0],a[1],a[2]),i.setMatrixAt(c,r),o.copy(typeof a[3]=="number"?n[a[3]]:a[3]),i.setColorAt(c,o)}),i.count=s.length,i.castShadow=!0,i.receiveShadow=!0,i.frustumCulled=!1,i.instanceMatrix.needsUpdate=!0,i.instanceColor&&(i.instanceColor.needsUpdate=!0),i}var As={floor:10528169,wall:14994846,trim:9800307,deskTop:5777938,deskBody:10528169,monitor:1780276,screen:879019,bar1:4955978,bar2:15912247,bar3:13179401,bar4:21951,board:16053488,boardFrame:668771,leaf:4955978,pot:10506797,winFrame:16053488,sky:10475253,city:10475253,clock:16053488,clockHand:1780276,keyboard:7106152,mug:13179401,axis:1780276,soil:3481856},Lv=`
uniform sampler2D tC; uniform sampler2D tD; uniform sampler2D tDof; uniform vec2 uNF; uniform float uFocus; uniform vec2 uRes;
varying vec2 vUv;
float viewZ(float d) { return uNF.x * uNF.y / ((uNF.y - uNF.x) * d - uNF.y); }
vec3 filmic(vec3 x) { return clamp((x * (2.51 * x + 0.03)) / (x * (2.43 * x + 0.59) + 0.14), 0.0, 1.0); }
void main() {
  vec3 c = texture2D(tC, vUv).rgb;
  float z = -viewZ(texture2D(tD, vUv).r);
  float coc = 0.85 * smoothstep(0.1, 0.8, clamp(abs(1.0 / uFocus - 1.0 / z) * uFocus * 1.5, 0.0, 1.0));
  c = mix(c, texture2D(tDof, vUv).rgb, coc);
  c = filmic(c * 1.05);
  c = pow(c, vec3(1.0 / 2.2));
  vec2 v = vUv - 0.5; c *= 1.0 - 0.35 * dot(v, v);
  c += (h12(vUv * uRes) - 0.5) * 0.01;
  gl_FragColor = vec4(c, 1.0);
}`;function ul(s){let{W:e,H:t,renderer:n,rig:i}=s,r=new Et;r.background=Tt(14994846),r.environment=Ts(n,{bg:10133672,bgK:.5,panels:[{pos:[-2,3.8,2.6],size:[3,2.2],look:[0,.5,0],color:16774892,intensity:3.2},{pos:[2.8,2.2,2.2],size:[1.6,2.4],look:[0,.5,0],color:15397631,intensity:1.6},{pos:[.5,3,-2.5],size:[3,1],look:[0,.5,0],color:16777215,intensity:1.2}]}),r.environmentIntensity=.75;let o=Rv(i.mesh.geometry),a=i.mesh.skeleton.bones,c=i.mesh.skeleton.boneInverses,l=Iv(),u=Pv(),h=Ih(12),f=Ih(8),p=Lh.map(j=>Tt(j)),g=[];for(let j=0;j<4;j++){let{geo:ue,studs:G}=Cv(o,j),J=new Qt;J.matrixAutoUpdate=!1;let re=new Fe(ue,l);re.castShadow=!0,re.receiveShadow=!0,J.add(re),J.add(Ph(G,h,u,p)),r.add(J),g.push(J)}{let j=8*Ze,ue=Ze*.95,G=i.logoTex,J=new xt({color:Tt(15922162),roughness:.22,clearcoat:.5,clearcoatRoughness:.1}),re=J.clone();re.map=G,re.onBeforeCompile=Oe=>{Oe.fragmentShader=Oe.fragmentShader.replace("#include <map_fragment>",`
          vec2 lu = (vMapUv - vec2(0.06, 0.2)) / vec2(0.88, 0.6);
          float a = (lu.x > 0.0 && lu.x < 1.0 && lu.y > 0.0 && lu.y < 1.0) ? texture2D(map, vec2(lu.x, 1.0 - lu.y)).a : 0.0;
          diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.012, 0.014, 0.03), a);`)},re.customProgramCacheKey=()=>"sb-lego-tile";let ee=new Fe(new cn(j,ue,Ze*.3),J),oe=new Fe(new $t(j*.985,ue*.97),re);oe.position.z=Ze*.151,ee.add(oe);let{NX:ye,NZ:De,X0:Qe,Z0:Ce,cid:qe,groups:N}=o,Ft=Math.floor(.385/Mi),Ge=0;for(let Oe=0;Oe<De;Oe++)for(let Re=0;Re<ye;Re++){let ut=(Re+Qe+.5)*Ze;Math.abs(ut-.02)<.12&&N[0].occ[qe(Re,Ft,Oe)]&&!N[0].ext[qe(Re,Ft,Oe)]&&(Ge=Math.max(Ge,(Oe+Ce+1)*Ze))}ee.position.set(.02,(Ft+.5)*Mi,Ge+Ze*.15),ee.castShadow=!0,g[0].add(ee)}let v=new xt({color:Tt(1053468),roughness:.06,metalness:0,clearcoat:1,clearcoatRoughness:.04,emissive:16777215,emissiveIntensity:1});v.onBeforeCompile=j=>{Object.assign(j.uniforms,i.shared.faceU),j.vertexShader=j.vertexShader.replace("#include <common>",`#include <common>
attribute vec3 _face;
varying vec3 vFace;
varying vec3 vRP;`).replace("#include <begin_vertex>",`#include <begin_vertex>
vFace = _face; vRP = position;`),j.fragmentShader=j.fragmentShader.replace("#include <common>",`#include <common>
varying vec3 vFace;
varying vec3 vRP;
`+ar).replace("#include <clipping_planes_fragment>",`#include <clipping_planes_fragment>
        float ellV = pow((vRP.x - 0.078) / 0.27, 2.0) + pow((vRP.y - 0.647) / 0.18, 2.0);
        if (ellV > 1.32 || vRP.z < 0.08) discard;`).replace("#include <emissivemap_fragment>",`#include <emissivemap_fragment>
        float fa = vFace.z > 0.01 ? screenFace(vFace.xy) * smoothstep(0.2, 0.6, vFace.z) : 0.0;
        diffuseColor.rgb = mix(diffuseColor.rgb, vec3(0.9, 0.97, 1.0), fa);
        totalEmissiveRadiance = vec3(0.55, 0.85, 1.0) * fa * 1.6 * uEyeGlow;`)},v.customProgramCacheKey=()=>"sb-lego-visor";let m=s.robotMesh(v);m.castShadow=!1,r.add(m);let d=[],M=[];for(let j=0;j<Nt;j++){let ue=Object.keys(V).find(G=>V[G]===j);d.push(Tt(As[ue]??10528169)),M.push([ue==="sky"?1:.3,0])}let b=d.map(()=>new ve(0,0,0));b[V.sky]=Tt(10475253).multiplyScalar(.9),b[V.city]=b[V.sky].clone(),b[V.screen]=Tt(879019).multiplyScalar(.5);let _=Es({cols:d,rm:M,em:b,physical:!0,key:"lego",phys:{clearcoat:.3,clearcoatRoughness:.2},hooks:{pars:`const float BS = ${Ze.toFixed(4)}, BH = ${Mi.toFixed(4)};
float gSeam = 0.0;
`,normal:`
      {
        vec3 wn = normalize((vec4(normal, 0.0) * viewMatrix).xyz);
        bool side = abs(wn.y) < 0.5 && vPal != ${V.sky} && vPal != ${V.city} && vPal != ${V.leaf} && vPal != ${V.screen};
        if (side) {
          float u = abs(wn.z) > 0.5 ? vWPos.x : vWPos.z;
          float row = floor(vWPos.y / BH);
          float fy = fract(vWPos.y / BH);
          float fx = fract((u + mod(row, 2.0) * 2.0 * BS) / (4.0 * BS));
          float ey = min(fy, 1.0 - fy) * BH, ex = min(fx, 1.0 - fx) * 4.0 * BS;
          gSeam = 1.0 - smoothstep(0.0, 0.0011, min(ey, ex));
          vec3 tU = abs(wn.z) > 0.5 ? vec3(1.0, 0.0, 0.0) : vec3(0.0, 0.0, 1.0);
          float by = (1.0 - smoothstep(0.0, 0.0035, ey)) * (fy < 0.5 ? -1.0 : 1.0);
          float bx = (1.0 - smoothstep(0.0, 0.0035, ex)) * (fx < 0.5 ? -1.0 : 1.0);
          normal = normalize(normal + (mat3(viewMatrix) * (vec3(0.0, 1.0, 0.0) * by + tU * bx)) * 0.8);
        }
      }`,albedo:`
      if (vPal == ${V.wall}) { float row = floor(vWPos.y / BH); float bi = floor((vWPos.x + mod(row, 2.0) * 2.0 * BS) / (4.0 * BS));
        float hb = h12(vec2(bi, row)); diffuseColor.rgb *= 0.97 + 0.05 * hb; if (hb > 0.9 && vWPos.y > 0.1) diffuseColor.rgb = vec3(0.29, 0.24, 0.16); }`,emissive:"diffuseColor.rgb *= 1.0 - 0.7 * gSeam; totalEmissiveRadiance *= 1.0 - 0.6 * gSeam;"}}),C=new Fe(s.setGeo.sharp,_);C.receiveShadow=!0,C.castShadow=!0,r.add(C);let A=[],E=Tt(As.floor);for(let j=-1.7;j<=1.7;j+=Ze)for(let ue=-1.25;ue<=1.1;ue+=Ze){let G=Math.round(j/Ze)*Ze+Ze/2,J=Math.round(ue/Ze)*Ze+Ze/2,re=Ct.desk,ee=Ct.plant,oe=Ct.board;Math.abs(G-re.x)<re.w/2&&Math.abs(J-re.z)<re.d/2||Math.hypot(G-ee.x,J-ee.z)<.13||A.push([G,0,J,E])}let I=(j,ue,G,J,re,ee)=>{for(let oe=j+Ze/2;oe<ue;oe+=Ze)for(let ye=G+Ze/2;ye<J;ye+=Ze)A.push([oe,re,ye,Tt(ee)])},x=Ct.desk;I(x.x-x.w/2+.02,x.x+x.w/2-.02,x.z-x.d/2+.02,x.z-.1,x.h,As.deskTop),I(x.x+.25,x.x+x.w/2-.02,x.z-.1,x.z+x.d/2-.02,x.h,As.deskTop);let y=Ct.win;I(y.x0-.08,y.x1+.08,Ct.wallZ+0,Ct.wallZ+.1,y.y0-.05+.003,As.winFrame);let T=Ct.board;I(T.x-T.w/2-.02,T.x+T.w/2+.02,T.z-.018,T.z+.018,T.y0+T.h+.027,As.boardFrame);{let j=Ph(A,f,u,null);j.castShadow=!1,r.add(j)}r.add(new mi(16777215,12104360,1.1));let L=new Un(16774376,2.6);L.position.set(-2,3.6,2.8),L.target.position.set(0,.4,-.3),L.castShadow=!0,L.shadow.mapSize.set(1024,1024),L.shadow.bias=-4e-4,L.shadow.normalBias=.012,Object.assign(L.shadow.camera,{left:-2,right:2,top:2.2,bottom:-1.2,near:.5,far:9}),L.shadow.camera.updateProjectionMatrix(),r.add(L,L.target);let D=new Un(15266047,.8);D.position.set(2.4,1.6,2.2),r.add(D);let F=st(e,t,{type:$e,samples:4,depthTexture:!0}),X=Math.ceil(e/2),z=Math.ceil(t/2),K=st(X,z,{depth:!1,type:$e}),H=new Je("uniform sampler2D tSrc; uniform vec2 uTexel; varying vec2 vUv; void main() { gl_FragColor = (texture2D(tSrc, vUv + uTexel * vec2(-1.0)) + texture2D(tSrc, vUv + uTexel) + texture2D(tSrc, vUv + uTexel * vec2(1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(-1.0, 1.0))) * 0.25; }",{tSrc:{value:F.texture},uTexel:{value:new le(.5/e,.5/t)}}),k=new ln(X,z,$e),$=new Je(Lv,{tC:{value:F.texture},tD:{value:F.depthTexture},tDof:{value:null},uNF:{value:new le},uFocus:{value:4.5},uRes:{value:new le(e,t)}}),ie=new P;return{render(j){let ue=s.renderer,G=i.rigRoot,J=s.robotVisible;for(let re=0;re<4;re++)g[re].matrix.multiplyMatrices(a[re].matrixWorld,c[re]),g[re].matrixWorldNeedsUpdate=!0,g[re].visible=J;m.visible=J,ue.shadowMap.needsUpdate=!0,ue.setRenderTarget(F),ue.clear(),ue.render(r,s.camera),H.render(ue,K),$.u.tDof.value=k.run(ue,K.texture,1.5,2),$.u.uNF.value.set(s.camera.near,s.camera.far),$.u.uFocus.value=s.camera.position.distanceTo(ie.set(G.position.x,.5+G.position.y,G.position.z)),$.render(ue,j)}}}function Rs(s,{keyDir:e=[-.6,.7,.45],smooth:t=!0,poolR:n=.75,hideCity:i=!1,simpleIds:r=!1}={}){let o={value:new P(...e).normalize()},a={value:new P(0,0,n)},c=Jt({robot:!0,rawNormals:!t,shared:s.rig.shared,defines:{MRT:""},uniforms:{uKey:o},extra:ws+`uniform vec3 uKey;
`,frag:`
    void main() {
      RobotSurf s = robotSurf();
      float ndl = clamp(dot(normalize(vN), uKey) * 0.5 + 0.5, 0.0, 1.0);
      gl_FragColor = vec4(ndl, s.eye, s.blue * uRing, s.logo);
      ${r?`
      // minimal ids: shell / visor (geometric ellipse -> one clean visor contour) / eyes
      float ell = pow((vRest.x - 0.078) / 0.27, 2.0) + pow((vRest.y - 0.647) / 0.18, 2.0);
      float fr = step(0.1, vRest.z) * step(0.0, vRestN.z);
      float vis = step(ell, 1.18) * fr, bez = step(ell, 1.6) * fr;
      float helmet = step(0.5, vRest.y) * step(abs(vRest.x - 0.03), 0.36);    // helmet: one shell (no side-panel specks)
      writeG(s.eye > 0.5 ? 34.0 : (vis > 0.5 ? 33.0 : (s.white > 0.5 || bez > 0.5 || helmet > 0.5 ? 30.0 : 31.0)));`:"writeG(robotId(s));"}
    }`}),l=Jt({robot:!1,defines:{MRT:""},uniforms:{uKey:o,uPool:a},extra:`uniform vec3 uKey; uniform vec3 uPool;
`,frag:`
    void main() {
      float ndl = clamp(dot(normalize(vN), uKey) * 0.5 + 0.5, 0.0, 1.0);
      float pool = vPal == ${V.floor} ? 1.0 - smoothstep(0.0, uPool.z, length(vW.xz - uPool.xy)) : 0.0;
      float glow = vPal == ${V.screen} ? 1.0 : 0.0;
      // floor dot grid (world space, anti-aliased): used by the minimal-line style
      float dots = 0.0;
      if (vPal == ${V.floor}) { vec2 gp = vW.xz / 0.22; vec2 f = fract(gp) - 0.5; float d = length(f) * 0.22; float w = fwidth(d) + 1e-4;
        dots = 1.0 - smoothstep(0.006 - w, 0.006 + w, d); }
      gl_FragColor = vec4(ndl, glow, dots, pool);
      writeG(float(vPal) + 1.0);
      ${i?`if (vPal == ${V.sky} || vPal == ${V.city}) { gl_FragColor = vec4(0.0); gOut1 = vec4(0.5, 0.5, 0.0, 0.0); }`:""}
    }`}),u=new Et,h=s.robotMesh(c);return u.add(h),u.add(new Fe(s.setGeo.sharp,l)),{scene:u,robot:h,uKey:o,uPool:a,render(f){let p=s.renderer;h.visible=s.robotVisible;let g=s.rig.rigRoot;a.value.x=g.position.x,a.value.y=g.position.z,p.setRenderTarget(f),p.setClearColor(new ve(.5,.5,0),0),p.clear(),p.render(u,s.camera),p.setClearColor(0,1)}}}function Cs(s,e,t=0){return st(s,e,{count:2,type:$e,samples:t})}var Dv=`
uniform sampler2D tI; uniform float uT; varying vec2 vUv;
vec2 wob(vec2 uv, float seed, float amp) {
  float b = floor(uT * 8.0) * 1.37 + seed;
  return (vec2(vnoise(uv * vec2(7.0, 9.0) + b), vnoise(uv * vec2(9.0, 6.5) + b + 17.3)) - 0.5) * amp * uTexel;
}
void main() {
  vec2 w1 = wob(vUv, 0.0, 3.2), w2 = wob(vUv, 41.0, 5.0);
  vec3 K = vec3(0.012, 0.28, 1.0);
  float e1 = edgeG(vUv + w1, 1.2, K);
  float e2 = edgeG(vUv + w2 + vec2(0.7, -0.5) * uTexel, 1.0, K);
  vec4 g = texture2D(tG, vUv + w1); vec4 inf = texture2D(tI, vUv + w1);
  float robot = step(29.5, g.w);
  // pressure: strokes fade in and out along their length
  float pr = 0.55 + 0.45 * smoothstep(0.25, 0.7, vnoise(vUv * vec2(55.0, 61.0) + floor(uT * 8.0)));
  float e = max(e1 * pr, e2 * 0.5 * (1.0 - pr * 0.5));
  vec3 gold = vec3(1.0, 0.72, 0.34), cy = vec3(0.30, 0.86, 1.0);
  vec3 lc = mix(gold * 0.55, gold * 1.05, robot);
  lc = mix(lc, cy * 1.1, smoothstep(0.3, 0.7, inf.b) * robot);
  vec3 col = lc * e;
  // eyes + lights: filled glow; wordmark in thin gold
  col += cy * smoothstep(0.3, 0.7, inf.g) * robot * 1.25;
  col += cy * 0.35 * smoothstep(0.3, 0.7, inf.b) * robot;
  col += gold * 0.9 * smoothstep(0.35, 0.7, inf.a) * robot;
  // monitor screen faint glow
  col += vec3(0.35, 0.6, 0.9) * 0.10 * inf.g * (1.0 - robot);
  // hatch strokes on the floor around the light pool (shadow side)
  float floorM = step(0.5, g.w) * step(g.w, 1.5);
  vec2 hp = gl_FragCoord.xy + w1 / uTexel;
  float hatch = 1.0 - smoothstep(0.0, 0.22, abs(fract((hp.x * 0.55 - hp.y) / 8.0) - 0.5) * 2.0);
  float hz = smoothstep(0.02, 0.2, inf.a) * (1.0 - smoothstep(0.35, 0.6, inf.a)) * floorM;
  float brk = step(0.35, vnoise(vec2((hp.x * 0.55 - hp.y) / 8.0, hp.x * 0.04)));
  col += gold * 0.2 * hatch * hz * brk;
  gl_FragColor = vec4(col, 1.0);
}`,Uv=`uniform sampler2D tSrc; uniform vec2 uTexel; varying vec2 vUv;
void main() { vec4 s = texture2D(tSrc, vUv + uTexel * vec2(-1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(-1.0, 1.0)) + texture2D(tSrc, vUv + uTexel * vec2(1.0, 1.0)); gl_FragColor = s * 0.25; }`,Nv=`
uniform sampler2D tL; uniform sampler2D tB1; uniform sampler2D tB2; uniform vec2 uRes; uniform float uT;
uniform vec2 uLamp; uniform vec2 uPoolC; uniform vec2 uPoolR; uniform float uLampW;
varying vec2 vUv;
void main() {
  vec2 p = vUv * uRes;
  vec3 lines = texture2D(tL, vUv).rgb;
  vec3 b1 = texture2D(tB1, vUv).rgb, b2 = texture2D(tB2, vUv).rgb;
  vec3 gold = vec3(1.0, 0.70, 0.33);
  // room: near black, warm
  vec3 col = vec3(0.026, 0.020, 0.016);
  // spotlight cone: from the lamp (above the frame) to the pool ellipse
  float t = (p.y - uLamp.y) / (uPoolC.y - uLamp.y);
  float hw = mix(uLampW, uPoolR.x * 0.98, clamp(t, 0.0, 1.0));
  float cx = mix(uLamp.x, uPoolC.x, t);
  float inC = (1.0 - smoothstep(hw * 0.78, hw, abs(p.x - cx))) * step(0.0, t) * (1.0 - smoothstep(0.92, 1.02, t));
  float coreC = 1.0 - smoothstep(0.0, hw * 0.75, abs(p.x - cx));
  col += gold * inC * (0.07 + 0.07 * coreC) * (0.55 + 0.45 * t);
  // cone edge strokes (sketched)
  float edgeL = exp(-abs(abs(p.x - cx) - hw) / 1.1) * step(0.0, t) * step(t, 0.97);
  col += gold * edgeL * 0.35 * (0.6 + 0.4 * vnoise(vec2(p.y * 0.05, 3.0)));
  // dust motes in the beam
  vec2 g = floor(p / 23.0); vec2 f = fract(p / 23.0) - 0.5 - (h22(g) - 0.5) * 0.7;
  col += gold * 0.5 * step(0.86, h12(g + 3.0)) * exp(-dot(f, f) * 900.0) * inC;
  // light pool on the floor
  vec2 q = (p - uPoolC) / uPoolR; float pool = 1.0 - smoothstep(0.55, 1.0, length(q));
  col += gold * pool * 0.10;
  col += lines + b1 * 0.85 + b2 * 0.45;
  // vignette + film-like grain (deterministic per frame)
  vec2 v = vUv - 0.5; col *= 1.0 - 0.55 * dot(v, v) * 2.0;
  col += (h12(p + floor(uT * 24.0) * 13.7) - 0.5) * 0.012;
  col = col / (1.0 + max(col - 0.85, 0.0));
  gl_FragColor = vec4(col, 1.0);
}`;function hl(s){let{W:e,H:t}=s,n=Rs(s,{keyDir:[0,1,.2],smooth:!1,poolR:.95,hideCity:!0}),i=Cs(e,t),r=new le(1/e,1/t),o=new Je(yi+Dv,{tG:{value:i.textures[1]},tI:{value:i.textures[0]},uTexel:{value:r},uT:{value:0}}),a=st(e,t,{depth:!1,type:$e}),c=Math.ceil(e/4),l=Math.ceil(t/4),u=st(c,l,{depth:!1,type:$e}),h=new Je(Uv,{tSrc:{value:a.texture},uTexel:{value:r}}),f=new ln(c,l,$e),p=new ln(Math.ceil(c/2),Math.ceil(l/2),$e),g=new Je(Nv,{tL:{value:a.texture},tB1:{value:null},tB2:{value:null},uRes:{value:new le(e,t)},uT:{value:0},uLamp:{value:new le},uPoolC:{value:new le},uPoolR:{value:new le},uLampW:{value:30}}),v=new P,m=(d,M,b)=>(v.set(d,M,b).project(s.camera),new le((v.x*.5+.5)*e,(v.y*.5+.5)*t));return{render(d){let M=s.renderer,b=s.rig.rigRoot;n.render(i),o.u.uT.value=s.t,o.render(M,a),h.render(M,u),g.u.tB1.value=f.run(M,u.texture,1,2),g.u.tB2.value=p.run(M,f.out.texture,2,2);let _=b.position.x,C=b.position.z,A=m(_,0,C),E=m(_-.62,0,C),I=m(_+.62,0,C),x=m(_,0,C+.62),y=m(_,0,C-.62);g.u.uPoolC.value.copy(A),g.u.uPoolR.value.set(Math.abs(I.x-E.x)/2,Math.abs(y.y-x.y)/2),g.u.uLamp.value.copy(m(_,2.4,C)),g.u.uLampW.value=26,g.u.uT.value=s.t,g.render(M,d)}}}var Fv=s=>{let e=new Array(Nt).fill(8947848);for(let[t,n]of Object.entries(s))e[V[t]]=n;return e.map(_i)},Ov=Fv({floor:16765503,wall:9426677,trim:16777215,deskTop:15221562,deskBody:16052712,monitor:2829114,screen:2067414,bar1:3064446,bar2:16765503,bar3:15221562,bar4:2784737,board:16777215,boardFrame:3826377,leaf:3650378,pot:15221562,winFrame:16777215,sky:12577535,city:7124448,clock:16777215,clockHand:1118481,keyboard:16052712,mug:16777215,axis:1118481,soil:5913378}),Dh=`
uniform vec3 uL; uniform float uDot;
// halftone: rotated dot grid in screen space, dot radius grows with darkness k (0..1)
float halftone(float k, float ang, float cell) {
  vec2 p = gl_FragCoord.xy; float c = cos(ang), s = sin(ang);
  vec2 q = mat2(c, -s, s, c) * p / cell; vec2 f = fract(q) - 0.5;
  float r = sqrt(clamp(k, 0.0, 1.0)) * 0.62;
  float d = length(f); float w = 0.7 / cell;
  return 1.0 - smoothstep(r - w, r + w, d);
}
// 3 tones: 1 = light, 0.5 = mid, 0 = shadow
float tone3(vec3 n) { float d = dot(normalize(n), uL); float w = fwidth(d) + 1e-4; return 0.5 * smoothstep(-0.12 - w, -0.12 + w, d) + 0.5 * smoothstep(0.45 - w, 0.45 + w, d); }
`;function fl(s){let{W:e,H:t}=s,n={value:new P(-.55,.7,.48).normalize()},i=Jt({robot:!0,blob:!0,shared:s.rig.shared,defines:{MRT:""},uniforms:{uL:n},extra:Dh+ws,frag:`
    void main() {
      RobotSurf s = robotSurf();
      float t = tone3(vN);
      vec3 V = normalize(cameraPosition - vW);
      float spec = pow(max(dot(reflect(-uL, normalize(vN)), V), 0.0), 24.0);
      // white shell: paper white / light blue-grey dots / blue-grey shadow
      vec3 wL = vec3(1.0, 0.99, 0.95), wM = vec3(0.70, 0.80, 0.93), wS = vec3(0.50, 0.60, 0.80);
      vec3 white = t > 0.75 ? wL : (t > 0.25 ? mix(wL, wM, halftone(0.55, 0.785, 6.0)) : mix(wM, wS, halftone(0.5, 0.785, 6.0)));
      // dark parts: ink black with a blue rim highlight
      vec3 dark = t > 0.75 ? vec3(0.17, 0.19, 0.28) : vec3(0.07, 0.07, 0.10);
      vec3 blue = vec3(0.15, 0.80, 1.0);
      vec3 c = white * s.white + dark * s.dark + blue * s.blue;
      // visor: ink black with a crisp white gloss streak
      float gx = vFace.x * 0.42 + vFace.y * 0.9;
      float gl = smoothstep(1.02, 1.06, gx) * (1.0 - smoothstep(1.32, 1.36, gx)) * step(-0.2, vFace.x * -1.0 + 0.4);
      vec3 vis = mix(vec3(0.06, 0.06, 0.09), vec3(0.95), gl * s.visor * smoothstep(0.5, 0.9, vFace.z));
      c = mix(c, vis, s.visor);
      float ew = fwidth(s.eyeSD) + 1e-4;
      float eye = (1.0 - smoothstep(-ew, ew, s.eyeSD)) * smoothstep(0.2, 0.6, vFace.z);
      c = mix(c, vec3(0.80, 0.97, 1.0), eye);
      c = mix(c, vec3(0.08, 0.08, 0.12), smoothstep(0.35, 0.6, s.logo));
      // glossy highlight shapes on the white shell (cut hard, comic style)
      c = mix(c, vec3(1.0), step(0.55, spec) * s.white);
      gl_FragColor = vec4(c, 1.0);
      writeG(robotId(s));
    }`}),r=Jt({robot:!1,defines:{MRT:""},uniforms:{uL:n,uPal:{value:Ov}},extra:Dh+`uniform vec3 uPal[${Nt}];
`,frag:`
    void main() {
      int p = vPal; vec3 b = uPal[p];
      float t = tone3(vN);
      vec3 shd = b * vec3(0.62, 0.66, 0.85);
      vec3 c = t > 0.75 ? b : (t > 0.25 ? mix(b, shd, halftone(0.45, 0.785, 6.0)) : shd);
      if (p == ${V.wall}) {
        // Ben-Day dots on the wall, denser towards the top
        float k = 0.25 + 0.25 * smoothstep(0.6, 2.4, vW.y);
        c = mix(c, vec3(0.38, 0.69, 0.92), halftone(k, 0.26, 9.0));
      } else if (p == ${V.floor}) {
        // floor planks: ink lines across, dots in the back
        float pl = abs(fract(vW.x / 0.32) - 0.5);
        c = mix(c, vec3(0.80, 0.55, 0.12), smoothstep(0.47, 0.49, pl));
        c = mix(c, vec3(0.92, 0.62, 0.15), halftone(0.18, 0.785, 7.0) * smoothstep(-0.2, -1.2, vW.z));
      } else if (p == ${V.sky}) {
        c = mix(vec3(0.75, 0.92, 1.0), vec3(0.55, 0.82, 0.98), halftone(0.35, 0.3, 7.0));
      } else if (p == ${V.screen}) {
        c = mix(vec3(0.14, 0.55, 0.85), vec3(0.08, 0.4, 0.7), halftone(0.4, 0.785, 5.0));
      }
      gl_FragColor = vec4(c, 1.0);
      writeG(float(p) + 1.0);
    }`}),o=new Et,a=s.robotMesh(i);o.add(a),o.add(new Fe(s.setGeo.sharp,r));let c=st(e,t,{count:2,type:$e}),l=new Je(yi+`
    uniform sampler2D tC; uniform vec2 uRes; varying vec2 vUv;
    void main() {
      vec3 K = vec3(0.025, 0.38, 1.0);
      float e = 0.0;
      e = max(e, edgeG(vUv, 1.6, K));
      e = max(e, edgeG(vUv + vec2(0.8, 0.8) * uTexel, 1.6, K));
      e = max(e, edgeG(vUv - vec2(0.8, 0.8) * uTexel, 1.6, K));
      // thick outer silhouettes: depth-only edges, wider radius
      vec3 KS = vec3(0.06, 9.0, 0.0);
      float es = max(edgeG(vUv, 3.2, KS), edgeG(vUv + vec2(1.5, -1.0) * uTexel, 3.2, KS));
      e = max(e, es);
      vec3 col = texture2D(tC, vUv).rgb;
      col = mix(col, vec3(0.05, 0.05, 0.07), clamp(e, 0.0, 1.0));
      // panel: white page gutter + thick ink border (slightly rough, like a brush-inked frame)
      vec2 p = vUv * uRes;
      float gut = 16.0, bw = 7.0;
      vec2 dd = min(p, uRes - p);
      float m = min(dd.x, dd.y) + (vnoise(p * 0.08) - 0.5) * 0.9;
      vec3 paper = vec3(0.985, 0.975, 0.95);
      col = m < gut ? paper : (m < gut + bw ? vec3(0.05, 0.05, 0.07) : col);
      // paper tooth
      col *= 0.985 + 0.03 * h12(floor(p * 0.5));
      gl_FragColor = vec4(col, 1.0);
    }`,{tG:{value:c.textures[1]},tC:{value:c.textures[0]},uTexel:{value:new le(1/e,1/t)},uRes:{value:new le(e,t)}});return{render(u){let h=s.renderer;a.visible=s.robotVisible,h.setRenderTarget(c),h.setClearColor(new ve(.5,.5,0),0),h.clear(),h.render(o,s.camera),h.setClearColor(0,1),l.render(h,u)}}}var Bv=`
uniform sampler2D tI; uniform vec2 uRes; uniform float uT; varying vec2 vUv;
vec2 wob(vec2 uv, float seed, float amp) {
  float b = floor(uT * 6.0) * 2.1 + seed;
  return (vec2(vnoise(uv * vec2(6.0, 8.0) + b), vnoise(uv * vec2(8.0, 5.0) + b + 9.7)) - 0.5) * amp * uTexel;
}
// chalk grain: fine tooth + streaks along a direction
float grain(vec2 p, float dens) {
  float n = vnoise(p * 0.9) * 0.55 + vnoise(p * 2.3 + 7.0) * 0.3 + h12(floor(p)) * 0.35;
  return smoothstep(1.0 - dens - 0.18, 1.0 - dens + 0.18, n);
}
vec3 pastel(float id) {
  if (abs(id - ${V.bar1+1}.0) < 0.5) return vec3(0.62, 0.90, 0.72);
  if (abs(id - ${V.bar2+1}.0) < 0.5) return vec3(1.0, 0.90, 0.55);
  if (abs(id - ${V.bar3+1}.0) < 0.5) return vec3(1.0, 0.68, 0.70);
  if (abs(id - ${V.bar4+1}.0) < 0.5) return vec3(0.62, 0.84, 1.0);
  if (abs(id - ${V.leaf+1}.0) < 0.5) return vec3(0.60, 0.88, 0.58);
  if (abs(id - ${V.pot+1}.0) < 0.5) return vec3(1.0, 0.72, 0.55);
  if (abs(id - ${V.deskTop+1}.0) < 0.5) return vec3(0.95, 0.80, 0.60);
  return vec3(0.0);
}
void main() {
  vec2 px = vUv * uRes;
  // ---- board
  vec3 board = vec3(0.19, 0.33, 0.26);
  float sm = fbm(px * 0.004 + 3.0);
  board += vec3(0.05, 0.07, 0.06) * smoothstep(0.35, 0.85, sm);                      // erased-chalk haze
  float sw = abs(sin(length(px - vec2(uRes.x * 0.78, uRes.y * 0.82)) * 0.045 + fbm(px * 0.01) * 3.0));
  board += vec3(0.025, 0.035, 0.03) * smoothstep(0.85, 1.0, sw) * smoothstep(0.4, 0.7, fbm(px * 0.006 + 11.0));   // eraser swirls
  board *= 0.96 + 0.06 * vnoise(px * 0.35);
  // ---- chalk drawing
  vec2 w1 = wob(vUv, 0.0, 4.0), w2 = wob(vUv, 23.0, 6.0);
  vec3 K = vec3(0.016, 0.32, 1.0);
  float e1 = max(max(edgeG(vUv + w1, 1.8, K), edgeG(vUv + w1 + vec2(1.1, 0.7) * uTexel, 1.8, K)), edgeG(vUv + w1 - vec2(0.6, 1.0) * uTexel, 1.8, K));
  float e2 = edgeG(vUv + w2 + vec2(-1.0, 1.2) * uTexel, 1.2, K);
  vec4 g = texture2D(tG, vUv + w1); vec4 inf = texture2D(tI, vUv + w1);
  float robot = step(29.5, g.w), has = step(0.5, g.w);
  float pr = 0.6 + 0.4 * vnoise(px * vec2(0.03, 0.035) + 5.0);
  float line = max(e1 * pr, e2 * 0.45) * grain(px, 0.78);
  vec3 chalkW = vec3(0.93, 0.95, 0.92);
  vec3 col = board;
  // rubbed pastel fills
  vec3 pc = pastel(g.w);
  // side-of-the-chalk rub: streaky (stretched noise along the stroke direction), never fully opaque
  vec2 rp = mat2(0.8, -0.6, 0.6, 0.8) * px;
  float rub = 0.45 + 0.35 * vnoise(rp * vec2(0.05, 0.9)) + 0.2 * vnoise(px * 0.6);
  float fillA = (pc.r + pc.g + pc.b > 0.1 ? 0.62 : 0.0) * smoothstep(0.3, 0.75, rub);
  col = mix(col, pc, fillA);
  // robot: faint white rub on the shell, pastel-blue lights, solid chalk eyes, chalk lettering
  float shell = robot * step(g.w, 30.5);
  col = mix(col, chalkW, 0.3 * shell * smoothstep(0.35, 0.8, rub));
  col = mix(col, vec3(0.55, 0.85, 1.0), smoothstep(0.3, 0.7, inf.b) * robot * grain(px + 9.0, 0.85));
  col = mix(col, vec3(0.88, 0.97, 1.0), smoothstep(0.3, 0.7, inf.g) * robot * grain(px + 1.0, 0.92));
  col = mix(col, chalkW, smoothstep(0.3, 0.75, inf.a) * robot * grain(px * 1.4 + 4.0, 0.62) * 0.95);
  // hatching in shadow (diagonal strokes, broken)
  float shade = (1.0 - inf.r) * has;
  vec2 hp = px + w1 / uTexel;
  float hl = abs(fract((hp.x + hp.y) / 7.0) - 0.5) * 2.0;
  float hatch = (1.0 - smoothstep(0.18, 0.42, hl)) * step(0.52, shade) * step(0.4, vnoise(hp * vec2(0.08, 0.02)));
  float hatch2 = (1.0 - smoothstep(0.18, 0.42, abs(fract((hp.x - hp.y) / 7.0) - 0.5) * 2.0)) * step(0.7, shade);
  col = mix(col, chalkW, max(hatch, hatch2) * 0.38 * grain(px * 1.3, 0.7) * (1.0 - step(32.5, g.w)));
  col = mix(col, chalkW, clamp(line, 0.0, 1.0) * 0.95);
  // dust halo around strokes
  col += vec3(0.03) * smoothstep(0.0, 1.0, max(e1, e2)) * (1.0 - grain(px, 0.78));
  // ---- wooden frame + chalk tray
  float fw = 22.0;
  vec2 dd = min(px, uRes - px); float m = min(dd.x, dd.y);
  float tray = step(px.y, 46.0);
  if (m < fw || tray > 0.5) {
    float along = (dd.x < dd.y) ? px.y : px.x;
    float across = min(dd.x, dd.y);
    vec3 wood = vec3(0.52, 0.32, 0.17);
    float gr = vnoise(vec2(along * 0.02, across * 0.6)) * 0.6 + vnoise(vec2(along * 0.08, across * 1.7)) * 0.4;
    wood *= 0.8 + 0.35 * gr;
    float bev = tray > 0.5 ? smoothstep(46.0, 30.0, px.y) * 0.25 + 0.0 : (across / fw);
    wood *= 0.75 + 0.35 * bev;
    if (tray > 0.5) {
      wood *= 0.85 + 0.2 * smoothstep(20.0, 40.0, px.y);
      // chalk sticks + eraser in the tray
      float y = px.y - 30.0;
      float stick1 = step(abs(y), 4.5) * step(abs(px.x - uRes.x * 0.62), 26.0);
      float stick2 = step(abs(y - 0.5), 4.0) * step(abs(px.x - uRes.x * 0.71), 15.0);
      float stick3 = step(abs(y), 4.0) * step(abs(px.x - uRes.x * 0.29), 19.0);
      float er = step(abs(y - 4.0), 10.0) * step(abs(px.x - uRes.x * 0.42), 46.0);
      wood = mix(wood, vec3(0.92, 0.91, 0.86) * (0.9 + 0.1 * vnoise(px)), stick1);
      wood = mix(wood, vec3(1.0, 0.86, 0.55), stick2);
      wood = mix(wood, vec3(0.98, 0.72, 0.76), stick3);
      wood = mix(wood, mix(vec3(0.28, 0.24, 0.2), vec3(0.85, 0.83, 0.78), step(y, 0.0)) * (0.9 + 0.1 * vnoise(px * 0.5)), er);
    }
    col = wood;
  }
  // inner shadow of the frame on the board
  col *= 1.0 - 0.35 * (1.0 - smoothstep(fw, fw + 14.0, m)) * step(fw, m) * (1.0 - tray);
  gl_FragColor = vec4(col, 1.0);
}`;function dl(s){let{W:e,H:t}=s,n=Rs(s,{keyDir:[-.55,.65,.5],smooth:!0,hideCity:!0}),i=Cs(e,t),r=new Je(yi+Bv,{tG:{value:i.textures[1]},tI:{value:i.textures[0]},uTexel:{value:new le(1/e,1/t)},uRes:{value:new le(e,t)},uT:{value:0}});return{render(o){n.render(i),r.u.uT.value=s.t,r.render(s.renderer,o)}}}var lr=8,xe={ink:789016,d1:1382187,d2:2501189,d3:3883108,w1:8753336,w2:12831720,w3:16119807,b1:1731484,b2:2279408,b3:9435391,o1:7028004,o2:10181939,o3:13075530,p1:2760532,p2:3812464,p3:5193364,g1:1924142,g2:3051326,g3:5952090,r1:10824234,r2:15221562,y2:16765503,y3:16773544,sky:1907261},je=s=>{let e=_i(s);return`vec3(${e.r.toFixed(4)}, ${e.g.toFixed(4)}, ${e.b.toFixed(4)})`},Is=(s,e,t)=>`ramp3(t, ${je(xe[s])}, ${je(xe[e])}, ${je(xe[t])})`,Uh=`
uniform vec3 uL;
float bayer4(vec2 p) { ivec2 i = ivec2(mod(p, 4.0)); int k = i.x + i.y * 4;
  float m[16] = float[16](0.0, 8.0, 2.0, 10.0, 12.0, 4.0, 14.0, 6.0, 3.0, 11.0, 1.0, 9.0, 15.0, 7.0, 13.0, 5.0); return (m[k] + 0.5) / 16.0; }
// light level -> ramp position 0..2 with ordered dither near the steps
float rampT(vec3 n, float bias, float dith) {
  float d = dot(normalize(n), uL) * 0.5 + 0.5 + bias;
  float t = clamp(d * 3.0 - 0.6, 0.0, 2.0);
  return floor(t + (bayer4(gl_FragCoord.xy) - 0.5) * dith + 0.5);
}
vec3 ramp3(float t, vec3 a, vec3 b, vec3 c) { return t < 0.5 ? a : (t < 1.5 ? b : c); }
`,Nh={A:[2,5,7,5,5],I:[7,2,2,2,7],P:[6,5,6,4,4],R:[6,5,6,5,5],E:[7,4,6,4,7],N:[5,7,7,7,5],U:[5,5,5,5,7],L:[4,4,4,4,7],V:[5,5,5,5,2],X:[5,5,2,5,5],0:[7,5,5,5,7],1:[2,6,2,2,7],2:[6,1,2,4,7],3:[6,1,2,1,6],4:[5,5,7,1,1],5:[7,4,6,1,6],6:[3,4,7,5,7],7:[7,1,2,2,2],8:[7,5,7,5,7],9:[7,5,7,1,6]," ":[0,0,0,0,0],":":[0,2,0,2,0]};function zv(s,e){let t=new Uint8Array(s*e*4),n=(h,f,p,g=255)=>{if(h<0||f<0||h>=s||f>=e)return;let v=4*((e-1-f)*s+h);t[v]=p>>16&255,t[v+1]=p>>8&255,t[v+2]=p&255,t[v+3]=g},i=(h,f,p,g,v)=>{for(let m=0;m<g;m++)for(let d=0;d<p;d++)n(h+d,f+m,v)},r=(h,f,p,g)=>{for(let v of h)(Nh[v]||Nh[" "]).forEach((d,M)=>{for(let b=0;b<3;b++)d&4>>b&&n(f+b,p+M,g)}),f+=4};i(0,0,s,9,xe.ink),i(0,9,s,1,xe.d2);let o=[[0,1,1,0,1,1,0],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[0,1,1,1,1,1,0],[0,0,1,1,1,0,0],[0,0,0,1,0,0,0]];for(let h=0;h<3;h++)o.forEach((f,p)=>f.forEach((g,v)=>{g&&n(2+h*8+v,2+p,h<2?p===1&&v===1?xe.y3:xe.r2:xe.d3)}));r("AI PRENEUR",Math.floor(s/2)-19,2,xe.w3),i(s-26,2,24,5,xe.d2),i(s-25,3,16,3,xe.g3),i(s-25,3,16,1,11071648);let a=e-12,c=Math.floor(s/2)-27;for(let h=0;h<5;h++){let f=c+h*11;i(f,a,10,10,xe.ink),i(f+1,a+1,8,8,h===2?xe.d3:xe.d2),h===2&&(i(f,a,10,1,xe.y2),i(f,a+9,10,1,xe.y2),i(f,a,1,10,xe.y2),i(f+9,a,1,10,xe.y2))}let l=(h,f)=>f(c+h*11+2,a+2);l(0,(h,f)=>{i(h+1,f,4,6,xe.y2),i(h,f+1,6,4,xe.y2),i(h+2,f+1,1,4,xe.y3)}),l(1,(h,f)=>{i(h,f+4,1,2,xe.g3),i(h+2,f+2,1,4,xe.y2),i(h+4,f,1,6,xe.r2)}),l(2,(h,f)=>{i(h+1,f,4,4,xe.y3),i(h+2,f+4,2,2,xe.w1),i(h+2,f+1,1,1,xe.w3)}),l(3,(h,f)=>{i(h,f+1,6,4,xe.w3),i(h+1,f+2,1,1,xe.d3),i(h+4,f+2,1,1,xe.d3),i(h+2,f+3,2,1,xe.d3)}),l(4,(h,f)=>{i(h+2,f,2,6,xe.b3),i(h,f+2,6,2,xe.b3),i(h+2,f+2,2,2,xe.w3)});let u=new vs(t,s,e,Ht);return u.magFilter=u.minFilter=yt,u.needsUpdate=!0,u}function pl(s){let{W:e,H:t}=s,n=Math.ceil(e/lr),i=Math.ceil(t/lr),r={value:new P(-.6,.7,.45).normalize()},o=Jt({robot:!0,blob:!0,shared:s.rig.shared,defines:{MRT:""},uniforms:{uL:r},extra:Uh+ws,frag:`
    void main() {
      RobotSurf s = robotSurf();
      float t = rampT(vN, 0.05, 0.4);
      vec3 c = ${Is("w1","w2","w3")};
      if (s.white < 0.5) c = ${Is("d1","d2","d3")};
      if (vCls.y > 0.22 && s.visor < 0.5 && s.white < 0.5) c = t > 1.5 ? ${je(xe.b3)} : ${je(xe.b2)};
      if (s.visor > 0.5) {
        c = ${je(xe.d1)};
        float gx = vFace.x * 0.42 + vFace.y * 0.9;
        if (gx > 1.0 && gx < 1.3 && vFace.x < 0.6) c = ${je(xe.d3)};
      }
      // pixel eyes: the face shapes dilated so they survive at sprite resolution
      if (vFace.z > 0.3 && s.eyeSD < 0.16) c = ${je(xe.b3)};
      if (vFace.z > 0.3 && s.eyeSD < 0.02) c = ${je(xe.w3)};
      gl_FragColor = vec4(c, 1.0);
      writeG(robotId(s));
    }`}),a=Jt({robot:!1,defines:{MRT:""},uniforms:{uL:r},extra:Uh,frag:`
    void main() {
      int p = vPal; float t = rampT(vN, 0.0, 0.0);
      vec3 c = ${Is("d1","d2","d3")};
      if (p == ${V.floor}) {
        c = ${je(xe.o2)};
        float pl = fract(vW.x / 0.22 + floor(vW.z / 0.6) * 0.5);
        if (pl < 0.12) c = ${je(xe.o1)};
        if (fract(vW.z / 0.6) < 0.05) c = ${je(xe.o1)};
        if (pl > 0.5 && pl < 0.6 && fract(vW.z / 0.6) > 0.5) c = ${je(xe.o3)};
        if (length((vW.xz - vec2(0.0, 0.05)) / vec2(0.36, 0.2)) < 1.0) c = ${je(xe.o1)};
      }
      else if (p == ${V.wall}) { float st = fract(vW.x / 0.18); c = st < 0.5 ? ${je(xe.p2)} : ${je(xe.p3)}; if (st > 0.92) c = ${je(xe.p1)}; if (vW.y < 0.12) c = ${je(xe.p1)}; }
      else if (p == ${V.trim}) c = ${je(xe.p1)};
      else if (p == ${V.deskTop} || p == ${V.deskBody}) c = ${Is("o1","o2","o3")};
      else if (p == ${V.screen}) { c = ${je(xe.b1)}; }
      else if (p == ${V.bar1} || p == ${V.leaf}) c = t > 0.5 ? ${je(xe.g3)} : ${je(xe.g2)};
      else if (p == ${V.bar2} || p == ${V.mug}) c = ${je(xe.y2)};
      else if (p == ${V.bar3} || p == ${V.pot}) c = t > 0.5 ? ${je(xe.r2)} : ${je(xe.r1)};
      else if (p == ${V.bar4}) c = ${je(xe.b2)};
      else if (p == ${V.board} || p == ${V.clock} || p == ${V.keyboard}) c = ${Is("w1","w2","w3")};
      else if (p == ${V.winFrame}) c = ${Is("w1","w2","w3")};
      else if (p == ${V.sky}) { c = ${je(xe.sky)}; if (h12(floor(gl_FragCoord.xy)) > 0.97) c = ${je(xe.w2)}; if (length(vW.xy - vec2(-0.62, 1.55)) < 0.075) c = ${je(xe.y3)}; }
      else if (p == ${V.city}) { c = ${je(xe.p1)}; vec2 f = floor(gl_FragCoord.xy); if (mod(f.x, 2.0) < 1.0 && mod(f.y, 3.0) < 1.0 && h12(floor(f / vec2(2.0, 3.0))) > 0.45) c = ${je(xe.y2)}; }
      else if (p == ${V.axis} || p == ${V.clockHand}) c = ${je(xe.ink)};
      else if (p == ${V.soil}) c = ${je(xe.o1)};
      gl_FragColor = vec4(c, 1.0);
      writeG(float(p) + 1.0);
    }`}),c=new Et,l=s.robotMesh(o);c.add(l),c.add(new Fe(s.setGeo.sharp,a));let u=st(n,i,{count:2,type:$e,nearest:!0}),h=zv(n,i),f=new le(Math.floor((n*lr-e)/2),Math.floor((i*lr-t)/2)),p=new Je(`
    uniform sampler2D tC; uniform sampler2D tG; uniform sampler2D tH; uniform vec2 uOff; uniform vec2 uLow;
    varying vec2 vUv;
    vec4 G(ivec2 p) { return texelFetch(tG, clamp(p, ivec2(0), ivec2(uLow) - 1), 0); }
    void main() {
      ivec2 p = ivec2(floor((gl_FragCoord.xy + uOff) / ${lr}.0));
      vec3 c = texelFetch(tC, p, 0).rgb;
      vec4 g = G(p);
      // 1-px outline: this pixel is nearer than a neighbour by a clear margin, or borders the empty background
      float o = 0.0, sel = 0.0;
      ivec2 nb[4] = ivec2[4](ivec2(1, 0), ivec2(-1, 0), ivec2(0, 1), ivec2(0, -1));
      for (int k = 0; k < 4; k++) {
        vec4 q = G(p + nb[k]);
        if (g.w > 0.5 && (q.w < 0.5 || g.z > q.z * 1.12)) o = 1.0;
        else if (g.w > 29.5 && q.w > 0.5 && q.w < 29.5) o = 1.0;
        else if (g.w > 0.5 && abs(g.w - q.w) > 0.5 && g.w > q.w && g.w < 33.5 && q.w > 0.5) sel = 1.0;
      }
      if (sel > 0.5 && g.w > 1.5) c *= 0.62;
      if (o > 0.5) c = ${je(xe.ink)};
      vec4 h = texelFetch(tH, p, 0);
      c = mix(c, h.rgb, h.a);
      gl_FragColor = vec4(c, 1.0);
    }`,{tC:{value:u.textures[0]},tG:{value:u.textures[1]},tH:{value:h},uOff:{value:f},uLow:{value:new le(n,i)}});return{render(g){let v=s.renderer;l.visible=s.robotVisible,v.setRenderTarget(u),v.setClearColor(new ve(.5,.5,0),0),v.clear(),v.render(c,s.camera),v.setClearColor(0,1),p.render(v,g)}}}var kv=`
uniform sampler2D tI; uniform vec2 uRes; varying vec2 vUv;
void main() {
  vec3 K = vec3(0.02, 0.3, 1.0);
  float e = 0.0;
  e += edgeG(vUv + vec2(-0.45, -0.45) * uTexel, 1.0, K);
  e += edgeG(vUv + vec2(0.45, -0.45) * uTexel, 1.0, K);
  e += edgeG(vUv + vec2(-0.45, 0.45) * uTexel, 1.0, K);
  e += edgeG(vUv + vec2(0.45, 0.45) * uTexel, 1.0, K);
  e = min(1.0, e * 0.4);
  vec4 g = texture2D(tG, vUv); vec4 inf = texture2D(tI, vUv);
  float robot = step(29.5, g.w);
  float setDim = 0.42 - 0.18 * smoothstep(0.18, 0.12, g.z);   // far set lines fade a little
  vec3 lc = mix(vec3(setDim), vec3(0.97), robot);
  float bl = smoothstep(0.2, 0.8, texture2D(tI, vUv + vec2(0.0, 1.5) * uTexel).b) * robot;
  lc = mix(lc, vec3(0.4, 0.86, 1.0), bl);
  vec3 col = lc * e;
  col += vec3(0.25, 0.75, 1.0) * 0.42 * smoothstep(0.35, 0.9, inf.b) * robot;      // the light strip: a thin cyan glow
  col += vec3(0.97) * smoothstep(0.35, 0.75, inf.g) * robot;
  col += vec3(0.9) * smoothstep(0.4, 0.75, inf.a) * robot * 0.85;
  float floorM = step(0.5, g.w) * step(g.w, 1.5);
  col += vec3(0.5) * inf.b * floorM * smoothstep(0.08, 0.2, g.z);
  gl_FragColor = vec4(col, 1.0);
}`;function ml(s){let{W:e,H:t}=s,n=Rs(s,{smooth:!0,hideCity:!0,simpleIds:!0}),i=Cs(e,t),r=new Je(yi+kv,{tG:{value:i.textures[1]},tI:{value:i.textures[0]},uTexel:{value:new le(1/e,1/t)},uRes:{value:new le(e,t)}});return{render(o){n.render(i),r.render(s.renderer,o)}}}function Hv(s){let e=[],t=[],n=[];for(let i=0;i<Nt;i++){let r=Object.keys(V).find(a=>V[a]===i),o={c:14208964,r:.85,m:0,e:0,k:0,...s[r]||{}};e.push(Tt(o.c)),t.push([o.r,o.m]),n.push(Tt(o.e).multiplyScalar(o.k))}return{cols:e,rm:t,em:n}}var Vv=Hv({floor:{c:15126452,r:.9},wall:{c:16050135,r:.95},trim:{c:15390399},deskTop:{c:16166546,r:.7},deskBody:{c:16373955,r:.8},monitor:{c:9411768,r:.55},screen:{c:14085119,r:.4,e:14085119,k:.35},bar1:{c:9428153,r:.6},bar2:{c:16767098,r:.6},bar3:{c:16751242,r:.6},bar4:{c:8831999,r:.6},board:{c:16775922,r:.8},boardFrame:{c:11846630,r:.6},leaf:{c:8833429,r:.75},pot:{c:15045743,r:.8},soil:{c:9069904},winFrame:{c:16777215,r:.6},sky:{c:0,e:12575487,k:1.25},city:{c:14281722,r:.9,e:14281722,k:.55},clock:{c:16775406,r:.6},clockHand:{c:7041925},keyboard:{c:16184561,r:.6},mug:{c:16762034,r:.5},axis:{c:8095910,r:.7}}),Gv=`
uniform sampler2D tC; uniform vec2 uRes; varying vec2 vUv;
vec3 filmic(vec3 x) { x *= 0.92; return clamp((x * (2.2 * x + 0.04)) / (x * (2.05 * x + 0.62) + 0.16), 0.0, 1.0); }
void main() {
  vec3 c = texture2D(tC, vUv).rgb;
  c = filmic(c);
  c = pow(c, vec3(1.0 / 2.2));
  c = mix(c, c * vec3(1.03, 1.0, 0.96), 0.6);
  vec2 v = vUv - 0.5; c *= 1.0 - 0.28 * dot(v, v);
  gl_FragColor = vec4(c, 1.0);
}`;function gl(s){let{W:e,H:t,renderer:n}=s,i=new Et;i.background=Tt(16050135),i.environment=Ts(n,{bg:13483176,bgK:.6,panels:[{pos:[-2.2,3.6,2.8],size:[3.5,2.5],look:[0,.6,0],color:16774374,intensity:2.2},{pos:[3,1.8,2],size:[2,2],look:[0,.6,0],color:15134719,intensity:1}]}),i.environmentIntensity=.45;let r=Mo(s.rig,{key:"explainer",noNormal:!0,smoothN:!0,rough:[.5,0],visorRough:.18,emiK:.9,eyeK:1.4,emi:[.5,.8,1],eye:[.85,.95,1],eyeAlb:[.95,.98,1],classes:{white:[.86,.82,.77],dark:[.055,.066,.13],blue:[.22,.58,1],visor:[.02,.025,.06],logo:[.06,.07,.15]}}),o=s.robotMesh(r);o.castShadow=!0,o.receiveShadow=!0,i.add(o);let a=Es({...Vv,key:"explainer",hooks:{albedo:`
      if (vPal == ${V.floor}) { float t = abs(fract(vWPos.x / 0.5) - 0.5); diffuseColor.rgb *= 1.0 - 0.06 * smoothstep(0.47, 0.49, t); }
      if (vPal == ${V.sky}) { float cl = smoothstep(0.55, 0.8, fbm(vWPos.xy * vec2(2.2, 4.0) + 3.0)); diffuseColor.rgb = vec3(0.0); }`,emissive:`
      if (vPal == ${V.sky}) { float cl = smoothstep(0.55, 0.75, fbm(vWPos.xy * vec2(2.0, 4.2) + 3.0)); totalEmissiveRadiance = mix(totalEmissiveRadiance, vec3(1.25), cl * 0.8); }`}}),c=new Fe(s.softSet(),a);c.receiveShadow=!0,c.castShadow=!0,i.add(c),i.add(new mi(16774118,14205868,1.35));let l=new Un(16773600,2.4);l.position.set(-2.2,3.4,2.6),l.target.position.set(0,.4,-.3),l.castShadow=!0,l.shadow.mapSize.set(1024,1024),l.shadow.bias=-5e-4,l.shadow.normalBias=.02,Object.assign(l.shadow.camera,{left:-2.2,right:2.2,top:2.4,bottom:-1.2,near:.5,far:9}),l.shadow.camera.updateProjectionMatrix(),i.add(l,l.target);let u=new Un(14674431,.7);u.position.set(2.5,1.5,2),i.add(u);let h=st(e,t,{type:$e,samples:4}),f=new Je(Gv,{tC:{value:h.texture},uRes:{value:new le(e,t)}});return{render(p){let g=s.renderer;o.visible=s.robotVisible,g.shadowMap.needsUpdate=!0,g.setRenderTarget(h),g.clear(),g.render(i,s.camera),f.render(g,p)}}}var Fh=2.75;function Wv(s,e){let t=s.attributes,n=t.position.count,i=t.skinIndex,r=t.skinWeight,o=new Int32Array(n),a=new Map,c=[],l=[];for(let _=0;_<n;_++){let C=i.getX(_);r.getY(_)>r.getX(_)&&(C=i.getY(_));let A=t.position.getX(_),E=t.position.getY(_),I=t.position.getZ(_),x=C+"|"+Math.floor(A/e)+"|"+Math.floor(E/e)+"|"+Math.floor(I/e),y=a.get(x);y===void 0&&(y=c.length,a.set(x,y),c.push(_),l.push({p:[0,0,0],f:[0,0,0],c:[0,0,0],k:0})),o[_]=y;let T=l[y];T.k++,T.p[0]+=A,T.p[1]+=E,T.p[2]+=I,T.f[0]+=t._face.getX(_),T.f[1]+=t._face.getY(_),T.f[2]+=t._face.getZ(_),T.c[0]+=t.aCls.getX(_),T.c[1]+=t.aCls.getY(_),T.c[2]+=t.aCls.getZ(_)}let u=c.length,h=new Float32Array(u*3),f=new Float32Array(u*3),p=new Float32Array(u*3),g=new Float32Array(u*2),v=new Uint16Array(u*4),m=new Float32Array(u*4);for(let _=0;_<u;_++){let C=l[_],A=c[_];for(let E=0;E<3;E++)h[3*_+E]=C.p[E]/C.k,f[3*_+E]=C.f[E]/C.k,p[3*_+E]=C.c[E]/C.k;g[2*_]=t.uv.getX(A),g[2*_+1]=t.uv.getY(A),v[4*_]=i.getX(A),v[4*_+1]=i.getY(A),v[4*_+2]=i.getZ(A),v[4*_+3]=i.getW(A),m[4*_]=r.getX(A),m[4*_+1]=r.getY(A),m[4*_+2]=r.getZ(A),m[4*_+3]=r.getW(A)}let d=s.index.array,M=[];for(let _=0;_<d.length;_+=3){let C=o[d[_]],A=o[d[_+1]],E=o[d[_+2]];C!==A&&A!==E&&C!==E&&M.push(C,A,E)}let b=new Mt;return b.setAttribute("position",new it(h,3)),b.setAttribute("uv",new it(g,2)),b.setAttribute("_face",new it(f,3)),b.setAttribute("aCls",new it(p,3)),b.setAttribute("skinIndex",new it(v,4)),b.setAttribute("skinWeight",new it(m,4)),b.setIndex(M),b.computeVertexNormals(),b.setAttribute("aSmoothN",b.attributes.normal.clone()),b.setAttribute("aBlobN",b.attributes.normal.clone()),b}function ur(s,e,t){let n=document.createElement("canvas");n.width=s,n.height=e;let i=n.getContext("2d");t(i,s,e);let r=new ao(n);return r.wrapS=r.wrapT=qn,r.generateMipmaps=!1,r.minFilter=wt,r.magFilter=wt,r.colorSpace=fn,r}var vl=(s,e,t,n,i,r,o=1)=>{for(let a=0;a<t;a+=o)for(let c=0;c<e;c+=o){let l=(Kt(c+r,a*1.3+r)-.5)*i;s.fillStyle=`rgb(${Math.round(n[0]+l)},${Math.round(n[1]+l)},${Math.round(n[2]+l*.9)})`,s.fillRect(c,a,o,o)}};function Xv(){let s=ur(64,256,(r,o,a)=>{vl(r,o,a,[178,162,130],12,1);for(let l=0;l<o;l+=16)r.fillStyle="rgba(120,96,70,0.32)",r.fillRect(l,0,3,a),r.fillStyle="rgba(255,240,210,0.16)",r.fillRect(l+8,0,2,a);let c=Math.round(a*(1-.9/3.4));for(let l=c;l<a;l++)for(let u=0;u<o;u++){let h=(Kt(u*.2,l*3.1)-.5)*26;r.fillStyle=`rgb(${110+h},${72+h*.7},${44+h*.5})`,r.fillRect(u,l,1,1)}r.fillStyle="rgb(70,44,26)",r.fillRect(0,c-3,o,4);for(let l=0;l<o;l+=32)r.fillRect(l,c,2,a-c);r.fillStyle="rgb(150,110,70)",r.fillRect(0,c-5,o,2)});s.wrapT=En;let e=ur(64,64,(r,o,a)=>{vl(r,o,a,[78,86,108],16,7),r.fillStyle="rgba(40,46,66,0.5)",r.fillRect(0,0,o,1),r.fillRect(0,0,1,a);for(let c=0;c<40;c++)r.fillStyle="rgba(30,34,50,0.35)",r.fillRect(Math.floor(Kt(c,3)*o),Math.floor(Kt(c,9)*a),2,1)}),t=ur(64,64,(r,o,a)=>{for(let c=0;c<a;c++)for(let l=0;l<o;l++){let u=Math.sin(l*.45+Math.sin(c*.15)*2.5+Kt(l,c)*.8)*18+(Kt(l*3,c)-.5)*12;r.fillStyle=`rgb(${132+u},${84+u*.7},${52+u*.45})`,r.fillRect(l,c,1,1)}}),n=ur(64,64,(r,o,a)=>{vl(r,o,a,[226,228,224],8,11);for(let c=0;c<6;c++)r.fillStyle="rgba(150,170,200,0.12)",r.fillRect(Kt(c,5)*o,Kt(c,6)*a,14,5)}),i=ur(128,64,(r,o,a)=>{let c=r.createLinearGradient(0,0,0,a);c.addColorStop(0,"#0b1230"),c.addColorStop(1,"#3a2d48"),r.fillStyle=c,r.fillRect(0,0,o,a);let l=0,u=0;for(;l<o;){let h=8+Math.floor(Kt(u,1)*14),f=14+Math.floor(Kt(u,2)*36);r.fillStyle=`rgb(${18+u%3*6},${20+u%2*6},34)`,r.fillRect(l,a-f,h,f);for(let p=a-f+3;p<a-2;p+=4)for(let g=l+2;g<l+h-2;g+=3)Kt(g*1.7,p*2.3)>.55&&(r.fillStyle=Kt(g,p)>.3?"#ffd27a":"#9fd0ff",r.fillRect(g,p,1,2));l+=h+1,u++}for(let h=0;h<30;h++)r.fillStyle="#ffffff",r.fillRect(Math.floor(Kt(h,8)*o),Math.floor(Kt(h,9)*a*.4),1,1)});return{wall:s,carpet:e,wood:t,board:n,city:i}}var Oh=`
uniform vec3 uFogCol; uniform vec2 uFog;
float fogK() { return smoothstep(uFog.x, uFog.y, vDepth); }
`;function xl(s){let{W:e,H:t}=s,n=Math.round(e/Fh),i=Math.round(t/Fh),r=Wv(s.rig.mesh.geometry,.048),o=Xv(),a={uKeyDir:{value:new P(-.5,.8,.62).normalize()},uKeyCol:{value:new P(1.12,1,.85)},uAmbUp:{value:new P(.36,.36,.44)},uAmbDn:{value:new P(.16,.13,.12)},uSnap:{value:new le(n/2,i/2)},uFogCol:{value:new P(.12,.1,.14)},uFog:{value:new le(4.4,11)}},c=Jt({robot:!0,rawNormals:!0,shared:s.rig.shared,defines:{VLIGHT:"",SNAP:""},uniforms:{...a},side:Lt,extra:`varying vec3 vGouraud;
uniform vec3 uKeyDir;
`+Oh,frag:`
    void main() {
      RobotSurf s = robotSurf();
      vec3 white = vec3(0.8, 0.81, 0.84), dark = vec3(0.09, 0.095, 0.115), blue = vec3(0.25, 0.65, 1.0);
      vec3 base = white * s.white + dark * s.dark;
      vec3 c = base * vGouraud;
      // per-vertex-ish specular (shiny console plastic)
      vec3 V = normalize(cameraPosition - vW); vec3 Hh = normalize(normalize(uKeyDir) + V);
      c += vec3(0.32) * pow(max(dot(normalize(vN), Hh), 0.0), 16.0) * s.white;
      // chrome sphere-map visor (fake reflection from the view normal)
      vec3 n = normalize(vNV);
      float band = smoothstep(0.25, 0.5, n.y) * (1.0 - smoothstep(0.55, 0.85, n.y)) + 0.35 * smoothstep(0.6, 0.95, -n.x);
      vec3 vis = vec3(0.03, 0.035, 0.06) + vec3(0.35, 0.42, 0.55) * band;
      c = mix(c, vis, s.visor);
      c += blue * s.blue * 1.1;
      c = mix(c, vec3(0.75, 0.95, 1.0), s.eye);
      c = mix(c, vec3(0.08, 0.08, 0.1), smoothstep(0.35, 0.6, s.logo));
      c = mix(c, uFogCol, fogK());
      gl_FragColor = vec4(c, 1.0);
    }`}),l=Jt({robot:!1,defines:{VLIGHT:"",SNAP:"",AFFINE:""},uniforms:{...a,tWall:{value:o.wall},tCarpet:{value:o.carpet},tWood:{value:o.wood},tBoard:{value:o.board},tCity:{value:o.city}},extra:`varying vec3 vGouraud;
varying vec3 vAff;
uniform sampler2D tWall; uniform sampler2D tCarpet; uniform sampler2D tWood; uniform sampler2D tBoard; uniform sampler2D tCity;
`+Oh,frag:`
    // affine-ish texture coords (screen-linear interpolation, mixed 50% with perspective-correct)
    vec2 planar() { vec3 a = abs(vN); vec2 pc = a.y > 0.5 ? vW.xz : (a.z > 0.5 ? vW.xy : vW.zy); return mix(pc, vAff.xy / vAff.z, 0.5); }
    void main() {
      int p = vPal; vec2 uv = planar();
      vec3 c = vec3(0.4);
      if (p == ${V.wall}) c = texture2D(tWall, vec2(uv.x / 0.9, clamp(uv.y / 3.4, 0.002, 0.998))).rgb;
      else if (p == ${V.floor}) c = texture2D(tCarpet, uv / 0.7).rgb;
      else if (p == ${V.deskTop} || p == ${V.deskBody} || p == ${V.boardFrame} || p == ${V.winFrame}) c = texture2D(tWood, uv / 0.5).rgb * (p == ${V.deskBody} ? 0.8 : 1.0);
      else if (p == ${V.board}) c = texture2D(tBoard, uv / 0.6).rgb;
      else if (p == ${V.sky}) c = texture2D(tCity, vec2((uv.x + 1.6) / 1.4, (uv.y - 0.85) / 1.0)).rgb * 1.2;
      else if (p == ${V.city}) c = vec3(0.05, 0.05, 0.08);
      else if (p == ${V.monitor} || p == ${V.keyboard}) c = vec3(0.16, 0.16, 0.18);
      else if (p == ${V.screen}) c = vec3(0.1, 0.22, 0.42);
      else if (p == ${V.bar1} || p == ${V.leaf}) c = vec3(0.25, 0.62, 0.3);
      else if (p == ${V.bar2} || p == ${V.mug}) c = vec3(0.92, 0.72, 0.2);
      else if (p == ${V.bar3} || p == ${V.pot}) c = vec3(0.75, 0.25, 0.2);
      else if (p == ${V.bar4}) c = vec3(0.25, 0.5, 0.9);
      else if (p == ${V.clock}) c = vec3(0.85, 0.85, 0.8);
      else if (p == ${V.axis} || p == ${V.clockHand}) c = vec3(0.1);
      else if (p == ${V.trim}) c = vec3(0.3, 0.2, 0.12);
      else if (p == ${V.soil}) c = vec3(0.2, 0.13, 0.08);
      vec3 lit = (p == ${V.sky} || p == ${V.screen}) ? c : c * vGouraud * 1.1;
      lit = mix(lit, uFogCol, fogK());
      gl_FragColor = vec4(lit, 1.0);
    }`}),u=new Et;u.background=new ve(.12,.1,.14);let h=s.robotMesh(c,r);u.add(h),u.add(new Fe(s.tessSet(),l));let f=st(n,i,{type:Dt}),p=st(n,i,{type:Dt,depth:!1}),g=new Je(`uniform sampler2D tSrc; varying vec2 vUv;
    float bayer4(vec2 p) { ivec2 i = ivec2(mod(p, 4.0)); int k = i.x + i.y * 4;
      float m[16] = float[16](0.0, 8.0, 2.0, 10.0, 12.0, 4.0, 14.0, 6.0, 3.0, 11.0, 1.0, 9.0, 15.0, 7.0, 13.0, 5.0); return (m[k] + 0.5) / 16.0 - 0.5; }
    void main() {
      vec3 c = texture2D(tSrc, vUv).rgb;
      c = pow(c, vec3(1.0 / 2.2));
      c = mix(vec3(luma(c)), c, 1.12) * 1.04;                       // slightly punchy console colour
      c = floor(c * 31.0 + 0.5 + bayer4(gl_FragCoord.xy) * 1.0) / 31.0;  // 15-bit (5:5:5) with ordered dither
      gl_FragColor = vec4(clamp(c, 0.0, 1.0), 1.0);
    }`,{tSrc:{value:f.texture}}),v=new Je(`uniform sampler2D tSrc; uniform vec2 uRes; varying vec2 vUv;
    void main() {
      vec3 c = texture2D(tSrc, vUv).rgb;
      float line = mod(floor(gl_FragCoord.y), 3.0) < 1.0 ? 0.94 : 1.0;   // faint interlace / TV lines
      c *= line;
      vec2 v = vUv - 0.5; c *= 1.0 - 0.25 * dot(v, v);
      gl_FragColor = vec4(c, 1.0);
    }`,{tSrc:{value:p.texture},uRes:{value:new le(e,t)}});return{render(m){let d=s.renderer;h.visible=s.robotVisible,d.setRenderTarget(f),d.clear(),d.render(u,s.camera),g.render(d,p),v.render(d,m)}}}var zh=s=>{let e=new Array(Nt).fill(8947848);for(let[t,n]of Object.entries(s))e[V[t]]=n;return e.map(_i)},qv=zh({floor:2766182,wall:3425146,trim:2766182,deskTop:15764061,deskBody:13658442,monitor:1843520,screen:2899578,bar1:5231045,bar2:16762967,bar3:15887725,bar4:8381439,board:15986662,boardFrame:5991075,leaf:4177802,pot:15909198,winFrame:15328498,sky:1712976,city:1054266,clock:15764061,clockHand:1843520,keyboard:14672880,mug:16762967,axis:2830154,soil:3811882}),Yv=zh({floor:2239576,wall:2832491,trim:2239576,deskTop:13199946,deskBody:11030589,monitor:1316913,screen:2241127,bar1:3516575,bar2:14262846,bar3:12996696,bar4:6273500,board:13223382,boardFrame:4543114,leaf:2856048,pot:13212213,winFrame:12170193,sky:1712976,city:1054266,clock:13199946,clockHand:1316913,keyboard:11449292,mug:14262846,axis:2830154,soil:2760222}),Bh=`
uniform vec3 uL;
float toon(vec3 n, float th) { float d = dot(normalize(n), uL); float w = fwidth(d) * 1.2 + 1e-4; return smoothstep(th - w, th + w, d); }
`;function _l(s){let{W:e,H:t}=s,n={value:new P(-.75,.55,.42).normalize()},i={value:new We(0,0,.35,.18)},r=Jt({robot:!0,blob:!0,shared:s.rig.shared,uniforms:{uL:n},extra:Bh,frag:`
    void main() {
      RobotSurf s = robotSurf();
      float lit = toon(vN, 0.05);
      vec3 white = mix(vec3(0.70, 0.74, 0.88), vec3(0.97, 0.96, 0.94), lit);
      vec3 dark = mix(vec3(0.075, 0.08, 0.16), vec3(0.16, 0.18, 0.31), lit);
      vec3 blue = vec3(0.30, 0.78, 1.0);
      vec3 c = white * s.white + dark * s.dark + blue * s.blue;
      // visor: deep navy with one flat highlight band (classic vector gloss)
      vec3 vis = vec3(0.075, 0.08, 0.16);
      float gl = smoothstep(0.35, 0.37, vFace.y * 0.55 + vFace.x * -0.25) * (1.0 - smoothstep(0.62, 0.64, vFace.y * 0.55 + vFace.x * -0.25));
      vis = mix(vis, vec3(0.15, 0.17, 0.30), gl * 0.8);
      c = mix(c, vis, s.visor);
      float ew = fwidth(s.eyeSD) * 1.0 + 1e-4;
      float eye = (1.0 - smoothstep(-ew, ew, s.eyeSD)) * smoothstep(0.2, 0.6, vFace.z);
      c = mix(c, vec3(0.86, 0.97, 1.0), eye);
      float lw = 0.5;
      c = mix(c, vec3(0.11, 0.12, 0.24), smoothstep(0.35, 0.6, s.logo));
      gl_FragColor = vec4(c, 1.0);
    }`}),o=Jt({robot:!1,uniforms:{uL:n,uPal:{value:qv},uShd:{value:Yv},uShadow:i},extra:Bh+`
    uniform vec3 uPal[${Nt}]; uniform vec3 uShd[${Nt}]; uniform vec4 uShadow;`,frag:`
    float aaStep(float e, float x) { float w = fwidth(x) + 1e-5; return smoothstep(e - w, e + w, x); }
    void main() {
      int p = vPal;
      float lit = toon(vN, 0.12);
      vec3 c = mix(uShd[p], uPal[p], lit);
      if (p == ${V.floor}) {
        // round rug under the robot + window light patch + flat ellipse shadow
        vec2 q = (vW.xz - vec2(0.0, 0.08)) / vec2(0.78, 0.5);
        float rug = 1.0 - aaStep(1.0, length(q));
        float rug2 = 1.0 - aaStep(0.78, length(q));
        c = mix(c, vec3(0.86, 0.42, 0.40), rug); c = mix(c, vec3(0.93, 0.52, 0.47), rug2);
        // light through the window: trace back to the wall plane along the light direction
        vec3 ld = normalize(vec3(-0.5, 0.62, -0.6));
        float tt = (${Ct.wallZ.toFixed(3)} - vW.z) / ld.z; vec3 hp = vW + ld * tt;
        float inW = aaStep(${Ct.win.x0.toFixed(3)}, hp.x) * (1.0 - aaStep(${Ct.win.x1.toFixed(3)}, hp.x)) * aaStep(${Ct.win.y0.toFixed(3)}, hp.y) * (1.0 - aaStep(${Ct.win.y1.toFixed(3)}, hp.y));
        c = mix(c, c + vec3(0.035, 0.035, 0.05), inW);
        vec2 sq = (vW.xz - uShadow.xy) / vec2(uShadow.z, uShadow.w);
        c = mix(c, c * vec3(0.62, 0.62, 0.78), 1.0 - aaStep(1.0, length(sq)));
      } else if (p == ${V.sky}) {
        // flat night sky: two bands, a moon and a few stars
        float b = aaStep(1.18, vW.y); c = mix(vec3(0.20, 0.24, 0.50), vec3(0.14, 0.17, 0.40), b);
        vec2 mp = vW.xy - vec2(${(Ct.win.x0+.33).toFixed(3)} - 0.15, 1.58);
        c = mix(c, vec3(1.0, 0.93, 0.74), 1.0 - aaStep(0.09, length(mp)));
        c = mix(c, vec3(0.14, 0.17, 0.40), (1.0 - aaStep(0.085, length(mp - vec2(0.045, 0.03)))) * (1.0 - aaStep(0.09, length(mp))) * 0.0);
        vec2 g = floor(vW.xy * 9.0); float st = step(0.93, h12(g));
        vec2 f = fract(vW.xy * 9.0) - 0.5 - (h22(g) - 0.5) * 0.6;
        c = mix(c, vec3(0.95, 0.95, 1.0), st * (1.0 - aaStep(0.06, length(f))) * b);
      } else if (p == ${V.city}) {
        // lit windows on the skyline
        vec2 g = floor(vec2(vW.x * 40.0, vW.y * 30.0)); vec2 f = fract(vec2(vW.x * 40.0, vW.y * 30.0));
        float win = step(0.55, h12(g)) * step(0.3, f.x) * step(f.x, 0.7) * step(0.3, f.y) * step(f.y, 0.75);
        c = mix(c, vec3(1.0, 0.82, 0.45), win * 0.85);
      } else if (p == ${V.screen}) {
        c = vec3(0.16, 0.22, 0.45);
      }
      gl_FragColor = vec4(c, 1.0);
    }`}),a=new Et;a.background=_i(3425146);let c=s.robotMesh(r);a.add(c),a.add(new Fe(s.setGeo.sharp,o));let l=st(e,t,{samples:4,type:Dt}),u=new Je("uniform sampler2D tSrc; varying vec2 vUv; void main() { gl_FragColor = vec4(texture2D(tSrc, vUv).rgb, 1.0); }",{tSrc:{value:l.texture}});return{render(h){let f=s.renderer;c.visible=s.robotVisible;let p=s.rig.rigRoot;i.value.set(p.position.x,p.position.z+.02,.34*p.scale.x,.17*p.scale.x),f.setRenderTarget(l),f.clear(),f.render(a,s.camera),u.render(f,h)}}}var $v={c:3159100,r:.6,m:0,e:0,k:0};function Zv(s){let e=[],t=[],n=[];for(let i=0;i<Nt;i++){let r=Object.keys(V).find(a=>V[a]===i),o={...$v,...s[r]||{}};e.push(Tt(o.c)),t.push([o.r,o.m]),n.push(Tt(o.e).multiplyScalar(o.k))}return{cols:e,rm:t,em:n}}var Kv=Zv({floor:{c:461068,r:.22},wall:{c:1778480,r:.85},trim:{c:658448,e:3135231,k:.55},deskTop:{c:3810840,r:.32},deskBody:{c:1053206,r:.45},monitor:{c:723983,r:.25,m:.3},screen:{c:132106,r:.2,e:732250,k:1.4},bar1:{c:132106,e:2351301,k:3.2},bar2:{c:132106,e:16757820,k:3},bar3:{c:132106,e:16732026,k:3},bar4:{c:132106,e:3983615,k:3.6},board:{c:725272,r:.12,m:.2,e:464938,k:.6},boardFrame:{c:10134445,r:.32,m:1},leaf:{c:1919532,r:.55},pot:{c:2303532,r:.4},soil:{c:1182728,r:1},winFrame:{c:1382171,r:.4,m:.6},sky:{c:0,e:727603,k:1},city:{c:329483,r:.9,e:16760944,k:0},clock:{c:12107976,r:.25,m:1},clockHand:{c:16777215,e:16777215,k:.4},keyboard:{c:1711136,r:.5},mug:{c:15263976,r:.3},axis:{c:132106,e:12578815,k:1.6}}),Jv=`
uniform sampler2D tC; uniform sampler2D tD; uniform sampler2D tB1; uniform sampler2D tB2; uniform sampler2D tB3; uniform sampler2D tDof;
uniform vec2 uRes; uniform float uT; uniform vec2 uNF; uniform float uFocus; uniform float uExp;
varying vec2 vUv;
float viewZ(float d) { return uNF.x * uNF.y / ((uNF.y - uNF.x) * d - uNF.y); }
vec3 aces(vec3 x) { const float a = 2.51, b = 0.03, c = 2.43, d = 0.59, e = 0.14; return clamp((x * (a * x + b)) / (x * (c * x + d) + e), 0.0, 1.0); }
void main() {
  vec2 uv = vUv;
  // chromatic fringe towards the corners
  vec2 cc = uv - 0.5; float r2 = dot(cc, cc);
  vec3 sharp = vec3(texture2D(tC, uv - cc * r2 * 0.006).r, texture2D(tC, uv).g, texture2D(tC, uv + cc * r2 * 0.006).b);
  float z = -viewZ(texture2D(tD, uv).r);
  float coc = clamp(abs(1.0 / uFocus - 1.0 / z) * uFocus * 2.0, 0.0, 1.0);
  coc = smoothstep(0.08, 0.6, coc);
  vec3 blurred = texture2D(tDof, uv).rgb;
  vec3 col = mix(sharp, blurred, coc);
  col += texture2D(tB1, uv).rgb * 0.55 + texture2D(tB2, uv).rgb * 0.45 + texture2D(tB3, uv).rgb * 0.35;
  col *= uExp;
  col = aces(col);
  // grade: teal shadows, warm highlights
  float l = luma(col);
  col = mix(col * vec3(0.92, 1.02, 1.06), col * vec3(1.05, 1.0, 0.94), smoothstep(0.25, 0.8, l));
  col = pow(col, vec3(1.0 / 2.2));
  col *= 1.0 - 0.9 * r2;
  col += (h12(uv * uRes + floor(uT * 24.0) * 17.31) - 0.5) * 0.028;
  gl_FragColor = vec4(col, 1.0);
}`,jv=`uniform sampler2D tSrc; uniform vec2 uTexel; uniform float uTh; varying vec2 vUv;
void main() { vec3 s = (texture2D(tSrc, vUv + uTexel * vec2(-0.5)) + texture2D(tSrc, vUv + uTexel * vec2(0.5)) + texture2D(tSrc, vUv + uTexel * vec2(0.5, -0.5)) + texture2D(tSrc, vUv + uTexel * vec2(-0.5, 0.5))).rgb * 0.25;
  float l = luma(s); gl_FragColor = vec4(s * smoothstep(uTh, uTh * 2.2, l), 1.0); }`,kh=`uniform sampler2D tSrc; uniform vec2 uTexel; varying vec2 vUv;
void main() { gl_FragColor = (texture2D(tSrc, vUv + uTexel * vec2(-1.0)) + texture2D(tSrc, vUv + uTexel * vec2(1.0)) + texture2D(tSrc, vUv + uTexel * vec2(1.0, -1.0)) + texture2D(tSrc, vUv + uTexel * vec2(-1.0, 1.0))) * 0.25; }`;function yl(s){let{W:e,H:t,renderer:n}=s,i=new Et;i.background=Tt(329482),i.environment=Ts(n,{bg:131846,panels:[{pos:[-1.5,4.2,2],size:[3.2,1.6],look:[0,.6,0],color:16773602,intensity:7},{pos:[.4,1.2,4.2],size:[3,1.6],look:[0,.6,0],color:15922943,intensity:2.2},{pos:[-3.4,1.4,-1.2],size:[.6,3],look:[0,1,0],color:3462911,intensity:7},{pos:[3.2,1.6,-1.8],size:[.8,3],look:[0,1,0],color:13163775,intensity:5},{pos:[2.6,1.2,3],size:[2,1.4],look:[0,1,0],color:16765608,intensity:1}]}),i.environmentIntensity=.9;let r=Mo(s.rig,{physical:!0,key:"cgi",clearcoat:.8,clearcoatRoughness:.08,emiK:3.6,eyeK:2.4,emi:[.25,.65,1],eye:[.75,.92,1],visorRough:.06}),o=s.robotMesh(r);o.castShadow=!0,i.add(o);let a=new wo,c=st(Math.ceil(e/2),Math.ceil(t/2),{type:$e}),l=new ln(Math.ceil(e/2),Math.ceil(t/2),$e),u={tRefl:{value:null},uTexMat:{value:a.texMat},uReflK:{value:1}},h=Es({...Kv,physical:!1,key:"cgi",uniforms:u,hooks:{pars:`uniform sampler2D tRefl; uniform mat4 uTexMat; uniform float uReflK;
`,albedo:`
      if (vPal == ${V.wall}) { float pn = abs(fract(vWPos.x / 0.62) - 0.5); diffuseColor.rgb *= 1.0 - 0.35 * smoothstep(0.485, 0.495, pn); }
      if (vPal == ${V.floor}) { float t = abs(fract(vWPos.x / 0.9) - 0.5); diffuseColor.rgb *= 1.0 - 0.5 * smoothstep(0.494, 0.498, t); }`,emissive:`
      if (vPal == ${V.city}) { vec2 q = vec2(vWPos.x * 13.0, vWPos.y * 10.0); vec2 g = floor(q); vec2 f = fract(q) - 0.5;
        float lw = 1.0 - smoothstep(0.18, 0.3, max(abs(f.x), abs(f.y) * 0.8));
        totalEmissiveRadiance += vec3(1.0, 0.72, 0.42) * 1.6 * step(0.6, h12(g)) * lw; }
      if (vPal == ${V.sky}) totalEmissiveRadiance *= 0.6 + 0.8 * smoothstep(0.9, 1.8, vWPos.y);
      if (vPal == ${V.floor}) {
        vec4 rp = uTexMat * vec4(vWPos, 1.0);
        vec3 refl = texture2DProj(tRefl, rp).rgb;
        vec3 V = normalize(cameraPosition - vWPos);
        float fr = 0.06 + 0.94 * pow(1.0 - max(V.y, 0.0), 5.0);
        totalEmissiveRadiance += refl * mix(0.3, 0.85, fr) * uReflK;
      }`}}),f=new Fe(s.setGeo.sharp,h);f.receiveShadow=!0,i.add(f);let p=new Qt;i.add(p);let g=(re,ee)=>new Yt({color:Tt(ee).multiplyScalar(re),transparent:!0,blending:is,depthWrite:!1,toneMapped:!1}),v=new Fe(new nr(.43,.452,96),g(3,3135231));v.rotation.x=-Math.PI/2,v.position.y=.004,p.add(v);let m=new Fe(new nr(.5,.507,96),g(1.2,3135231));m.rotation.x=-Math.PI/2,m.position.y=.004,p.add(m);let d=new Gt({transparent:!0,depthWrite:!1,blending:is,uniforms:{},vertexShader:"varying vec2 vU; void main(){ vU = uv * 2.0 - 1.0; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }",fragmentShader:"varying vec2 vU; void main(){ float r = length(vU); float g = exp(-pow((r - 0.73) / 0.08, 2.0)) * 0.6 + (1.0 - smoothstep(0.0, 0.75, r)) * 0.18; gl_FragColor = vec4(vec3(0.05, 0.45, 0.8) * g, 1.0); }"}),M=new Fe(new $t(1.25,1.25),d);M.rotation.x=-Math.PI/2,M.position.y=.003,p.add(M);let b=new Gt({transparent:!0,depthWrite:!1,blending:is,side:Lt,vertexShader:"varying vec3 vN; varying vec3 vV; varying float vY; void main(){ vec4 w = modelMatrix * vec4(position,1.0); vY = position.y; vN = normalize(mat3(modelMatrix) * normal); vV = normalize(cameraPosition - w.xyz); gl_Position = projectionMatrix * viewMatrix * w; }",fragmentShader:"varying vec3 vN; varying vec3 vV; varying float vY; void main(){ float f = pow(abs(dot(normalize(vN), normalize(vV))), 2.5); float h = smoothstep(-1.3, 0.6, vY) * (1.0 - smoothstep(0.9, 1.3, vY)); gl_FragColor = vec4(vec3(0.9, 0.85, 0.75) * f * h * 0.05, 1.0); }"}),_=new Fe(new Zt(.12,.75,2.6,48,1,!0),b);_.position.set(-.05,1.3,.05),i.add(_);let C=new jn(16773342,48,0,.55,.65,2);C.position.set(-1.6,3,2.4),C.target.position.set(0,.45,0),C.castShadow=!0,C.shadow.mapSize.set(1024,1024),C.shadow.bias=-4e-4,C.shadow.normalBias=.01,C.shadow.radius=6,C.shadow.camera.near=1,C.shadow.camera.far=8,i.add(C,C.target);let A=new jn(3659007,55,0,.6,.6,2);A.position.set(-1.7,2.2,-1.9),A.target.position.set(0,.55,0),i.add(A,A.target);let E=new jn(13820671,40,0,.6,.6,2);E.position.set(1.9,1.8,-1.6),E.target.position.set(0,.5,0),i.add(E,E.target);let I=new mi(9417944,658448,.12);i.add(I);let x=new jn(7314390,14,0,.9,.9,2);x.position.set(.3,2.9,-.4),x.target.position.set(.1,.9,-1.3),i.add(x,x.target);let y=st(e,t,{type:$e,samples:4,depthTexture:!0}),T=Math.ceil(e/2),L=Math.ceil(t/2),D=Math.ceil(e/4),F=Math.ceil(t/4),X=st(T,L,{depth:!1,type:$e}),z=st(D,F,{depth:!1,type:$e}),K=new Je(jv,{tSrc:{value:y.texture},uTexel:{value:new le(1/e,1/t)},uTh:{value:1.3}}),H=new Je(kh,{tSrc:{value:null},uTexel:{value:new le(1/T,1/L)}}),k=new ln(T,L,$e),$=new ln(D,F,$e),ie=new ln(Math.ceil(D/2),Math.ceil(F/2),$e),j=new Je(kh,{tSrc:{value:y.texture},uTexel:{value:new le(1/e,1/t)}}),ue=st(T,L,{depth:!1,type:$e}),G=new ln(D,F,$e),J=new Je(Jv,{tC:{value:y.texture},tD:{value:y.depthTexture},tB1:{value:null},tB2:{value:null},tB3:{value:null},tDof:{value:null},uRes:{value:new le(e,t)},uT:{value:0},uNF:{value:new le},uFocus:{value:4.5},uExp:{value:1}});return{render(re){let ee=s.renderer,oe=s.camera,ye=s.rig.rigRoot;o.visible=s.robotVisible,p.position.set(ye.position.x,0,ye.position.z),_.position.x=ye.position.x-.05,_.position.z=ye.position.z+.05,ee.shadowMap.enabled=!0,ee.shadowMap.needsUpdate=!0;let De=a.update(oe);h.userData.u.uReflK.value=0,p.visible=!0,ee.setRenderTarget(c),ee.clear(),ee.render(i,De),h.userData.u.uReflK.value=1,h.userData.u.tRefl.value=l.run(ee,c.texture,1,1),ee.setRenderTarget(y),ee.clear(),ee.render(i,oe),K.render(ee,X),J.u.tB1.value=k.run(ee,X.texture,1,1),H.u.tSrc.value=k.out.texture,H.u.uTexel.value.set(1/T,1/L),H.render(ee,z),J.u.tB2.value=$.run(ee,z.texture,1.5,1),J.u.tB3.value=ie.run(ee,$.out.texture,2,2),j.render(ee,ue),J.u.tDof.value=G.run(ee,ue.texture,1.6,2);let Qe=oe.position.distanceTo(new P(ye.position.x,.5+ye.position.y,ye.position.z));J.u.uFocus.value=Qe,J.u.uNF.value.set(oe.near,oe.far),J.u.uT.value=s.t,J.render(ee,re)}}}var Qv={lego:ul,glow:hl,comic:fl,chalk:dl,pixel:pl,line:ml,explainer:gl,ps2:xl,flat:_l,cgi:yl},Hh=["lego","glow","comic","chalk","pixel","line","explainer","ps2","flat","cgi"],ex={lego:"Lego",glow:"Glow Sketch",comic:"Comic",chalk:"Chalkboard",pixel:"Pixel Art",line:"Minimal Line",explainer:"Explainer 3D",ps2:"PS2 Style",flat:"Flat Vector",cgi:"CGI Motion"},hr=class s{static async create(e,t={}){let n=new s;return await n.init(e,t),n}async init(e,{url:t,width:n=820,height:i=980,logoUrl:r="assets/brand/logo_white_trim.png",styles:o=Hh,warm:a=!0}={}){this.W=n,this.H=i;let c=this.renderer=new eo({canvas:e,antialias:!1,alpha:!1,preserveDrawingBuffer:!0,powerPreference:"high-performance"});c.setPixelRatio(1),c.setSize(n,i,!1),c.outputColorSpace=St,c.toneMapping=Ln,c.setClearColor(0,1),c.shadowMap.enabled=!0,c.shadowMap.type=vc,c.shadowMap.autoUpdate=!1,this.camera=new _t(27,n/i,.05,40),this.rig=await Th(t,r),this.t=0;let l=this;this.ctx={renderer:c,W:n,H:i,camera:this.camera,rig:this.rig,PAL:V,LAYOUT:Ct,makeRT:st,Pass:Je,get t(){return l.t},setGeo:{sharp:So({round:0})},softSet(){return this.setGeo.soft||(this.setGeo.soft=So({round:.03}))},tessSet(){return this.setGeo.tess||(this.setGeo.tess=So({round:0,seg:3}))},robotMesh(u,h){let f=new gs(h||l.rig.mesh.geometry,u);return f.bind(l.rig.mesh.skeleton,l.rig.mesh.bindMatrix),f.frustumCulled=!1,f.userData.isRobot=!0,f},get robotVisible(){return l.rig.visible!==!1}},this.styles={};for(let u of o)this.styles[u]=Qv[u](this.ctx);this.sweep=Rh(this.ctx),this.rtA=st(n,i,{depth:!1,type:Dt}),this.rtB=st(n,i,{depth:!1,type:Dt}),this.style=o[0],this.setCamera({}),this.setState({}),a&&this.warm()}warm(){for(let n of Object.keys(this.styles))this.styles[n].render(this.rtA);this.sweep.render(this.rtA.texture,this.rtB.texture,.5,20,null),this.renderer.setRenderTarget(null);let e=this.renderer.getContext(),t=new Uint8Array(4);e.readPixels(0,0,1,1,e.RGBA,e.UNSIGNED_BYTE,t)}setStyle(e){if(!this.styles[e])throw new Error("StyleBot: unknown style "+e);this.style=e}setTime(e){this.t=e||0}setState(e){Ah(this.rig,e||{}),e&&e.t!=null&&(this.t=e.t)}setCamera({yaw:e=15,pitch:t=6,dist:n=4.5,target:i=[0,.8,0],fov:r=27,roll:o=0,shift:a=[0,0]}={}){let c=this.camera,l=vi.degToRad(e),u=vi.degToRad(t);c.fov=r,c.aspect=this.W/this.H,c.position.set(i[0]+Math.sin(l)*Math.cos(u)*n,i[1]+Math.sin(u)*n,i[2]+Math.cos(l)*Math.cos(u)*n),c.up.set(0,1,0),c.lookAt(i[0],i[1],i[2]),o&&c.rotateZ(vi.degToRad(o)),a[0]||a[1]?c.setViewOffset(this.W,this.H,-a[0]*this.W,a[1]*this.H,this.W,this.H):c.clearViewOffset(),c.updateProjectionMatrix(),c.updateMatrixWorld(!0),this.camState={yaw:e,pitch:t,dist:n,target:i,fov:r,roll:o,shift:a}}render(){this.styles[this.style].render(null)}renderStyle(e,t=null){this.styles[e].render(t)}renderSweep(e,t,n,i=18){if(n<=0)return this.renderStyle(e);if(n>=1)return this.renderStyle(t);this.styles[e].render(this.rtA),this.styles[t].render(this.rtB),this.sweep.render(this.rtA.texture,this.rtB.texture,n,i,null)}};window.StyleBot=hr;hr.STYLE_IDS=Hh;hr.STYLE_NAMES=ex;})();
