import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { RectAreaLightUniformsLib } from 'three/addons/lights/RectAreaLightUniformsLib.js';

// Rendering core.
//  - renders the scene into a linear HDR target with transparent background
//  - accumulates N sub-frames across the shutter interval -> true motion blur
//  - supersamples (ssaa x) and box-filters down to output size
//  - final pass: un-premultiply, Khronos PBR Neutral tone mapping (keeps brand
//    colours honest), sRGB encode, straight alpha out -> composited on #00FF00 by ffmpeg
export class Stage {
  constructor({ size = 1080, ssaa = 2, subframes = 8, shutter = 0.5, fps = 60, msaa = 0 } = {}) {
    this.size = size; this.ssaa = ssaa; this.subframes = subframes; this.shutter = shutter; this.fps = fps;
    const canvas = document.createElement('canvas');
    document.body.appendChild(canvas);
    const renderer = new THREE.WebGLRenderer({
      canvas, antialias: false, alpha: true, premultipliedAlpha: false, preserveDrawingBuffer: true,
      powerPreference: 'high-performance',
    });
    renderer.setPixelRatio(1);
    renderer.autoClear = false; // we manage clears: accumulation must not be wiped between passes
    renderer.setSize(size, size, false);
    renderer.toneMapping = THREE.NeutralToneMapping;
    renderer.toneMappingExposure = 1.0;
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    this.renderer = renderer;

    const S = size * ssaa;
    const rtOpts = { type: THREE.HalfFloatType, format: THREE.RGBAFormat, depthBuffer: true, samples: msaa,
      minFilter: THREE.LinearFilter, magFilter: THREE.LinearFilter, colorSpace: THREE.LinearSRGBColorSpace };
    this.rt = new THREE.WebGLRenderTarget(S, S, rtOpts);
    this.acc = new THREE.WebGLRenderTarget(S, S, { ...rtOpts, depthBuffer: false, samples: 0 });

    this.scene = new THREE.Scene();
    this.scene.background = null;
    this.camera = new THREE.PerspectiveCamera(24, 1, 0.05, 60);
    this.camera.position.set(0, 0, 4.2);

    // studio lighting: neutral environment + key / fill / rim (same rig for all 3 films)
    const pmrem = new THREE.PMREMGenerator(renderer);
    this.scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
    this.scene.environmentIntensity = 0.42;

    // key: spot with physical falloff -> soft brightness gradient across the paper
    const key = new THREE.SpotLight('#FFF4E6', 58, 0, 0.62, 0.95, 2);
    key.position.set(-2.0, 2.7, 3.4);
    key.target.position.set(0.1, -0.1, 0);
    key.castShadow = true;
    key.shadow.mapSize.set(2048, 2048);
    key.shadow.camera.near = 1.5; key.shadow.camera.far = 12;
    key.shadow.bias = -0.0003;
    key.shadow.normalBias = 0.004;
    key.shadow.radius = 4;
    this.scene.add(key, key.target);
    this.key = key;

    // softbox: large rect light high camera-left -> gentle specular sheen sweeping over the stock
    RectAreaLightUniformsLib.init();
    const box = new THREE.RectAreaLight('#FFFFFF', 2.6, 2.6, 1.8);
    box.position.set(-1.6, 1.9, 2.6);
    box.lookAt(0, 0, 0);
    this.scene.add(box);

    const fill = new THREE.DirectionalLight('#DCE4FF', 0.38);
    fill.position.set(3.2, 0.0, 2.2);
    this.scene.add(fill);
    const rim = new THREE.DirectionalLight('#FFFFFF', 1.9);
    rim.position.set(2.8, 2.6, -3.0);
    this.scene.add(rim);
    const under = new THREE.DirectionalLight('#EEF1FA', 0.2);
    under.position.set(0, -3, 1.5);
    this.scene.add(under);

    // fullscreen passes
    const quadGeo = new THREE.PlaneGeometry(2, 2);
    this.orthoCam = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
    this.accMat = new THREE.ShaderMaterial({
      uniforms: { tSrc: { value: null }, uW: { value: 1 } },
      vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, 0., 1.); }',
      fragmentShader: 'uniform sampler2D tSrc; uniform float uW; varying vec2 vUv; void main(){ gl_FragColor = texture2D(tSrc, vUv) * uW; }',
      blending: THREE.CustomBlending,
      blendSrc: THREE.OneFactor, blendDst: THREE.OneFactor,
      blendSrcAlpha: THREE.OneFactor, blendDstAlpha: THREE.OneFactor,
      depthTest: false, depthWrite: false, toneMapped: false,
    });
    this.outMat = new THREE.ShaderMaterial({
      uniforms: { tSrc: { value: this.acc.texture }, uTexel: { value: new THREE.Vector2(1 / S, 1 / S) }, uSS: { value: ssaa } },
      vertexShader: 'varying vec2 vUv; void main(){ vUv = uv; gl_Position = vec4(position.xy, 0., 1.); }',
      fragmentShader: `
        uniform sampler2D tSrc; uniform vec2 uTexel; uniform float uSS; varying vec2 vUv;
        void main(){
          // ssaa 2: one bilinear tap at the output pixel centre = exact 2x2 box filter
          vec4 c = texture2D(tSrc, vUv);
          float a = clamp(c.a, 0.0, 1.0);
          vec3 rgb = a > 0.0005 ? c.rgb / max(c.a, 0.0005) : vec3(0.0);
          gl_FragColor = vec4(rgb, a);
          #include <tonemapping_fragment>
          #include <colorspace_fragment>
        }`,
      depthTest: false, depthWrite: false, toneMapped: true, transparent: false, blending: THREE.NoBlending,
    });
    this.accQuad = new THREE.Mesh(quadGeo, this.accMat);
    this.outQuad = new THREE.Mesh(quadGeo, this.outMat);
    this.passScene = new THREE.Scene();
    this.passScene.add(this.accQuad);
    this.outScene = new THREE.Scene();
    this.outScene.add(this.outQuad);
    this.pixels = new Uint8Array(size * size * 4);
  }

  // Screen-space motion estimate (pixels travelled during the shutter) from probe points
  // on every PaperSheet. Drives the number of motion-blur sub-frames: ~1 sub-frame per
  // 1.25 px of travel, so fast moves get smooth, correct blur and holds stay crisp & cheap.
  motionPixels(t, update) {
    const half = (this.shutter / this.fps) / 2;
    const sample = (ts) => {
      update(ts);
      this.scene.updateMatrixWorld(true);
      this.camera.updateMatrixWorld(true);
      const pts = [];
      this.scene.traverse((o) => {
        if (!o.isPaperSheet || !o.visible) return;
        const a = o.gFront.attributes.position.array;
        const n = a.length / 3;
        const step = Math.max(1, Math.floor(n / 24));
        for (let i = 0; i < n; i += step) {
          const v = new THREE.Vector3(a[i * 3], a[i * 3 + 1], a[i * 3 + 2]);
          o.mFront.localToWorld(v);
          v.project(this.camera);
          pts.push(v);
        }
      });
      return pts;
    };
    const A = sample(t - half), B = sample(t + half);
    let m = 0;
    for (let i = 0; i < Math.min(A.length, B.length); i++) {
      const dx = (A[i].x - B[i].x) * this.size / 2, dy = (A[i].y - B[i].y) * this.size / 2;
      m = Math.max(m, Math.hypot(dx, dy));
    }
    return m;
  }

  // update(t) mutates the scene/camera for time t (seconds)
  render(t, update) {
    const r = this.renderer;
    let N = this.subframes;
    if (N > 1) {
      const px = this.motionPixels(t, update);
      N = Math.max(2, Math.min(this.subframes, Math.ceil(px / 1.25)));
    }
    this.lastSubframes = N;
    r.setRenderTarget(this.acc);
    r.setClearColor(0x000000, 0);
    r.clear(true, false, false);
    for (let k = 0; k < N; k++) {
      const ts = N === 1 ? t : t + (((k + 0.5) / N) - 0.5) * (this.shutter / this.fps);
      update(ts);
      r.setRenderTarget(this.rt);
      r.setClearColor(0x000000, 0);
      r.clear(true, true, false);
      r.render(this.scene, this.camera);
      this.accMat.uniforms.tSrc.value = this.rt.texture;
      this.accMat.uniforms.uW.value = 1 / N;
      r.setRenderTarget(this.acc);
      r.render(this.passScene, this.orthoCam);
    }
    r.setRenderTarget(null);
    r.setClearColor(0x000000, 0);
    r.clear(true, true, false);
    r.render(this.outScene, this.orthoCam);
  }

  readBase64() {
    const gl = this.renderer.getContext();
    gl.readPixels(0, 0, this.size, this.size, gl.RGBA, gl.UNSIGNED_BYTE, this.pixels);
    let s = '';
    const chunk = 0x8000;
    for (let i = 0; i < this.pixels.length; i += chunk) {
      s += String.fromCharCode.apply(null, this.pixels.subarray(i, i + chunk));
    }
    return btoa(s);
  }
}
