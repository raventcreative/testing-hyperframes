/* Shared, tweenable state for the 3D presenter robot (load before the composition script).
   Angles in degrees. aL* / aR* = arm offsets on top of the rest pose (screen-left / screen-right arm).
   happy / x / wide / excited / flat = expression weights (0..1, >0.5 shows it). */
window.R3D = window.R3D || {};
window.R3D.pxPerUnit = 590; // robot size: px per model unit (head top 40 px under the canvas top)
window.R3D.REST = { aLz: 12, aLx: 0, aRz: 0, aRx: 0 };
window.R3D.state = { zoom: 1, zy: 0, yaw: 0, yawT: 0, pitch: 0, lean: 0, bob: 0, sq: 1, aLx: 0, aLy: 0, aLz: 12, aRx: 0, aRy: 0, aRz: 0,
  happy: 0, x: 0, wide: 0, excited: 0, flat: 0, lookX: 0, lookY: 0 };
window.R3D.render = window.R3D.render || function (t) { window.R3D.t0 = t; };
