// STYLEBOT: the AI PRENEUR robot + a small procedural office set, re-rendered in 10 animation genres
// (lego, glow, comic, chalk, pixel, line, explainer, ps2, flat, cgi) from one pose state, plus the signature
// "re-render scan line" sweep between two styles. Fully deterministic: no clock, no Math.random; seeded hash noise only.
// Bundled to vendor/stylebot3d.js (window.StyleBot) by tools/build_stylebot.sh.
import * as THREE from 'three';
import { loadRobot, applyState } from './sb/robot.js';
import { buildSet, PAL, LAYOUT } from './sb/set.js';
import { makeRT, Pass } from './sb/common.js';
import { createSweep } from './sb/sweep.js';
import createLego from './sb/styles/lego.js';
import createGlow from './sb/styles/glow.js';
import createComic from './sb/styles/comic.js';
import createChalk from './sb/styles/chalk.js';
import createPixel from './sb/styles/pixel.js';
import createLine from './sb/styles/line.js';
import createExplainer from './sb/styles/explainer.js';
import createPs2 from './sb/styles/ps2.js';
import createFlat from './sb/styles/flat.js';
import createCgi from './sb/styles/cgi.js';

const FACTORIES = { lego: createLego, glow: createGlow, comic: createComic, chalk: createChalk, pixel: createPixel, line: createLine,
  explainer: createExplainer, ps2: createPs2, flat: createFlat, cgi: createCgi };
export const STYLE_IDS = ['lego', 'glow', 'comic', 'chalk', 'pixel', 'line', 'explainer', 'ps2', 'flat', 'cgi'];
export const STYLE_NAMES = { lego: 'Lego', glow: 'Glow Sketch', comic: 'Comic', chalk: 'Chalkboard', pixel: 'Pixel Art', line: 'Minimal Line',
  explainer: 'Explainer 3D', ps2: 'PS2 Style', flat: 'Flat Vector', cgi: 'CGI Motion' };

export class StyleBot {
  static async create(canvas, opts = {}) { const b = new StyleBot(); await b.init(canvas, opts); return b; }

  async init(canvas, { url, width = 820, height = 980, logoUrl = 'assets/brand/logo_white_trim.png', styles = STYLE_IDS, warm = true } = {}) {
    this.W = width; this.H = height;
    const r = (this.renderer = new THREE.WebGLRenderer({ canvas, antialias: false, alpha: false, preserveDrawingBuffer: true, powerPreference: 'high-performance' }));
    r.setPixelRatio(1); r.setSize(width, height, false);
    r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.NoToneMapping; r.setClearColor(0x000000, 1);
    r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap; r.shadowMap.autoUpdate = true;
    this.camera = new THREE.PerspectiveCamera(27, width / height, 0.05, 40);
    this.rig = await loadRobot(url, logoUrl);
    this.t = 0;
    const self = this;
    this.ctx = {
      renderer: r, W: width, H: height, camera: this.camera, rig: this.rig, PAL, LAYOUT, makeRT, Pass,
      get t() { return self.t; },
      setGeo: { sharp: buildSet({ round: 0 }) },
      softSet() { return this.setGeo.soft || (this.setGeo.soft = buildSet({ round: 0.03 })); },
      // a robot SkinnedMesh sharing the rig's geometry + skeleton (one per style scene)
      robotMesh(mat, geo) {
        const m = new THREE.SkinnedMesh(geo || self.rig.mesh.geometry, mat);
        m.bind(self.rig.mesh.skeleton, self.rig.mesh.bindMatrix); m.frustumCulled = false; m.userData.isRobot = true;
        return m;
      },
      get robotVisible() { return self.rig.visible !== false; },
      cache: {},
    };
    this.styles = {};
    for (const id of styles) this.styles[id] = FACTORIES[id](this.ctx);
    this.sweep = createSweep(this.ctx);
    this.rtA = makeRT(width, height, { depth: false, type: THREE.UnsignedByteType });
    this.rtB = makeRT(width, height, { depth: false, type: THREE.UnsignedByteType });
    this.style = styles[0];
    this.setCamera({});
    this.setState({});
    if (warm) this.warm();
  }

  // compile shaders + allocate targets for every style once (switching styles per frame is then free of recompiles)
  warm() {
    for (const id of Object.keys(this.styles)) this.styles[id].render(this.rtA);
    this.sweep.render(this.rtA.texture, this.rtB.texture, 0.5, 20, null);
    this.renderer.setRenderTarget(null);
    const gl = this.renderer.getContext(), px = new Uint8Array(4); gl.readPixels(0, 0, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, px);
  }

  setStyle(id) { if (!this.styles[id]) throw new Error('StyleBot: unknown style ' + id); this.style = id; }
  setTime(t) { this.t = t || 0; }
  setState(s) { applyState(this.rig, s || {}); if (s && s.t != null) this.t = s.t; }

  // perspective camera orbiting `target`: yaw/pitch in degrees, dist in world units (robot = 0.9 tall), fov in degrees,
  // roll in degrees, shift [x,y] = lens shift as a fraction of the frame (moves the subject without changing perspective)
  setCamera({ yaw = 15, pitch = 6, dist = 4.5, target = [0.0, 0.8, 0], fov = 27, roll = 0, shift = [0, 0] } = {}) {
    const c = this.camera, a = THREE.MathUtils.degToRad(yaw), p = THREE.MathUtils.degToRad(pitch);
    c.fov = fov; c.aspect = this.W / this.H;
    c.position.set(target[0] + Math.sin(a) * Math.cos(p) * dist, target[1] + Math.sin(p) * dist, target[2] + Math.cos(a) * Math.cos(p) * dist);
    c.up.set(0, 1, 0); c.lookAt(target[0], target[1], target[2]);
    if (roll) c.rotateZ(THREE.MathUtils.degToRad(roll));
    if (shift[0] || shift[1]) c.setViewOffset(this.W, this.H, -shift[0] * this.W, shift[1] * this.H, this.W, this.H); else c.clearViewOffset();
    c.updateProjectionMatrix(); c.updateMatrixWorld(true);
    this.camState = { yaw, pitch, dist, target, fov, roll, shift };
  }

  render() { this.styles[this.style].render(null); }
  renderStyle(id, target = null) { this.styles[id].render(target); }

  // signature transition: same scene in style A and style B, B revealed behind a moving cyan "re-render" scan line.
  // u: 0 -> all A, 1 -> all B. angleDeg: direction the line travels (0 = left->right, 90 = bottom->top).
  renderSweep(idA, idB, u, angleDeg = 18) {
    if (u <= 0) return this.renderStyle(idA);
    if (u >= 1) return this.renderStyle(idB);
    this.styles[idA].render(this.rtA);
    this.styles[idB].render(this.rtB);
    this.sweep.render(this.rtA.texture, this.rtB.texture, u, angleDeg, null);
  }
}
window.StyleBot = StyleBot;
StyleBot.STYLE_IDS = STYLE_IDS; StyleBot.STYLE_NAMES = STYLE_NAMES;
