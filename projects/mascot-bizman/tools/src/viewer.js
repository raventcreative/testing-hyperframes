import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
window.MascotViewer = {
  async render(canvas, url, views, box, unlit) {
    const r = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true });
    r.setSize(canvas.width, canvas.height, false); r.outputColorSpace = THREE.SRGBColorSpace;
    const scene = new THREE.Scene();
    scene.add(new THREE.HemisphereLight(0xffffff, 0x8899bb, 1.6));
    const key = new THREE.DirectionalLight(0xffffff, 1.6); key.position.set(-1, 2, 2); scene.add(key);
    const g = await new GLTFLoader().loadAsync(url);
    if (unlit) g.scene.traverse(o => { if (o.isMesh) o.material = new THREE.MeshBasicMaterial({ map: o.material.map }); });
    scene.add(g.scene);
    const n = views.length, w = canvas.width / n, h = canvas.height;
    const [x0, x1, y0, y1] = box || [-0.36, 0.36, -0.02, 1.0];
    r.setScissorTest(true);
    views.forEach((v, i) => {
      const cam = new THREE.OrthographicCamera(x0, x1, y1, y0, -5, 5);
      const a = v * Math.PI / 180; cam.position.set(Math.sin(a), 0, Math.cos(a)); cam.lookAt(0, 0, 0); cam.updateProjectionMatrix();
      r.setViewport(i * w, 0, w, h); r.setScissor(i * w, 0, w, h); r.render(scene, cam);
    });
  }
};
