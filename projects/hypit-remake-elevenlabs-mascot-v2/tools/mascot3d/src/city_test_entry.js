import * as THREE from 'three';
import { City } from './city.js';
window.boot = async () => {
  const canvas = document.getElementById('c');
  const r = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
  r.setPixelRatio(1); r.setSize(1080, 1920, false); r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.ACESFilmicToneMapping;
  r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap;
  window.C = await City.create(r, { base: 'assets/3d/', draco: 'vendor/draco/' });
};
window.shot = (t) => { C.render(+t, 0); return document.getElementById('c').toDataURL('image/jpeg', 0.85); };
