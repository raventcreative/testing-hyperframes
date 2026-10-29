/* MasterPajak 2.5D puppet — WebGL2 renderer for the layered PNG rig (vendor/masterpajak-rig.js).
 *
 * Honest scope: this is image-based puppet animation, NOT a 3D rig. The supplied mascot is a single PNG,
 * cut into 4 layers (body, armR, armL, head) by tools/build_rig.py using the original pixels only.
 *  - Body: grid mesh, upper body rotates/breathes about the hips, legs weight 0 (feet stay planted).
 *  - Arms: grid mesh with smooth skin weights from the shoulder seam (weight 0 = glued to the torso)
 *          to the hand, plus a soft mid-arm bend. Mitten arms bend like a plush toy, no visible joint.
 *  - Head: rigid disk; yaw/pitch are a spherical re-projection of the original head pixels in the
 *          fragment shader, so the logo decal foreshortens like a turning sphere without being redrawn.
 *          The silhouette edge is sampled unrotated so the outline never wobbles. Keep |yaw|,|pitch| <= 10°.
 *
 * API:  MPPuppet.create(canvas, { rig, base, height, feet:[x,y] }) -> Promise<puppet>
 *       puppet.render(pose)  (pose fields documented in DEFAULT_POSE)
 * Everything is a pure function of `pose` -> deterministic, seek-safe.
 */
(function () {
  const DEG = Math.PI / 180;
  const DEFAULT_POSE = {
    opacity: 1,
    scale: 1,          // about the feet
    x: 0, y: 0,        // canvas px offset of the whole character
    chestRot: 0,       // deg, + = clockwise on screen, about the hips
    chestX: 0, chestY: 0, // source px
    breath: 0,         // -1..1
    headRoll: 0,       // deg, + = clockwise on screen (tilt), about the neck
    headYaw: 0,        // deg, + = face turns to screen-right
    headPitch: 0,      // deg, + = nod down
    headY: 0,          // source px bob
    armR: { up: 0, bend: 0, lift: 0 }, // character's right arm (screen-left). up/bend deg outward(+)
    armL: { up: 0, bend: 0, lift: 0 }, // character's left arm (screen-right)
  };

  // ---------- tiny 2D affine helpers: [a,b,c,d,e,f] => x' = a x + c y + e ; y' = b x + d y + f ----------
  const mul = (m, n) => [
    m[0] * n[0] + m[2] * n[1], m[1] * n[0] + m[3] * n[1],
    m[0] * n[2] + m[2] * n[3], m[1] * n[2] + m[3] * n[3],
    m[0] * n[4] + m[2] * n[5] + m[4], m[1] * n[4] + m[3] * n[5] + m[5],
  ];
  const T = (x, y) => [1, 0, 0, 1, x, y];
  const R = (deg) => { const c = Math.cos(deg * DEG), s = Math.sin(deg * DEG); return [c, s, -s, c, 0, 0]; };
  const S = (sx, sy) => [sx, 0, 0, sy, 0, 0];
  const about = (p, m) => mul(T(p[0], p[1]), mul(m, T(-p[0], -p[1])));
  const ap = (m, x, y) => [m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5]];
  const sstep = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };

  const VS = `#version 300 es
    in vec2 a_pos; in vec2 a_uv; in vec2 a_src;
    uniform vec2 u_res;
    out vec2 v_uv; out vec2 v_src;
    void main(){ v_uv=a_uv; v_src=a_src; gl_Position=vec4(a_pos.x/u_res.x*2.0-1.0, 1.0-a_pos.y/u_res.y*2.0, 0.0, 1.0); }`;
  const FS = `#version 300 es
    precision highp float;
    in vec2 v_uv; in vec2 v_src; uniform sampler2D u_tex; uniform float u_op; out vec4 o;
    void main(){ o = texture(u_tex, v_uv) * u_op; }`;
  // head: spherical re-projection. u_rect = layer rect in source px (x,y,w,h), u_c/u_r = head circle.
  const FS_HEAD = `#version 300 es
    precision highp float;
    in vec2 v_uv; in vec2 v_src;
    uniform sampler2D u_tex; uniform float u_op; uniform vec4 u_rect; uniform vec2 u_c; uniform float u_r;
    uniform mat3 u_inv; out vec4 o;
    vec2 toUV(vec2 s){ return (s - u_rect.xy) / u_rect.zw; }
    void main(){
      vec4 base = texture(u_tex, v_uv);
      vec2 u = (v_src - u_c) / u_r;
      float d = length(u);
      if (d >= 0.999) { o = base * u_op; return; }
      vec3 p = vec3(u, sqrt(max(0.0, 1.0 - d*d)));
      vec3 q = u_inv * p;
      q.z = max(q.z, 0.0);
      vec2 qs = normalize(q).xy;
      float rim = smoothstep(0.90, 0.995, d);
      vec2 s = u_c + mix(qs, u, rim) * u_r;
      vec4 c = texture(u_tex, toUV(s));
      vec3 rgb = c.rgb / max(c.a, 1e-3);
      o = vec4(rgb * base.a, base.a) * u_op;
    }`;

  function compile(gl, vs, fs) {
    const p = gl.createProgram();
    for (const [type, src] of [[gl.VERTEX_SHADER, vs], [gl.FRAGMENT_SHADER, fs]]) {
      const s = gl.createShader(type);
      gl.shaderSource(s, src); gl.compileShader(s);
      if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
      gl.attachShader(p, s);
    }
    gl.linkProgram(p);
    if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
    return p;
  }

  function loadImage(src) {
    return new Promise((res, rej) => { const im = new Image(); im.onload = () => res(im); im.onerror = () => rej(new Error("load " + src)); im.src = src; });
  }

  function grid(rect, cell) {
    const nx = Math.max(1, Math.ceil(rect.w / cell)), ny = Math.max(1, Math.ceil(rect.h / cell));
    const src = [], uv = [], idx = [];
    for (let j = 0; j <= ny; j++) for (let i = 0; i <= nx; i++) {
      const u = i / nx, v = j / ny;
      src.push(rect.x + u * rect.w, rect.y + v * rect.h); uv.push(u, v);
    }
    for (let j = 0; j < ny; j++) for (let i = 0; i < nx; i++) {
      const a = j * (nx + 1) + i, b = a + 1, c = a + nx + 1, d = c + 1;
      idx.push(a, b, c, b, d, c);
    }
    return { src: new Float32Array(src), uv: new Float32Array(uv), idx: new Uint16Array(idx), n: src.length / 2 };
  }

  async function create(canvas, opts) {
    const rig = opts.rig, base = opts.base || "assets/mascot/";
    const gl = canvas.getContext("webgl2", { premultipliedAlpha: true, alpha: true, antialias: true, preserveDrawingBuffer: true });
    if (!gl) throw new Error("webgl2 unavailable");
    const prog = compile(gl, VS, FS), progH = compile(gl, VS, FS_HEAD);
    const names = ["body", "armR", "armL", "head"];
    const imgs = await Promise.all(names.map((n) => loadImage(base + "layer_" + n + ".png")));
    const L = {};
    names.forEach((n, k) => {
      const rect = rig.layers[n];
      const tex = gl.createTexture();
      gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, true);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, imgs[k]);
      gl.generateMipmap(gl.TEXTURE_2D);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      const g = grid(rect, n === "body" ? 12 : n === "head" ? 64 : 7);
      const vao = gl.createVertexArray(); gl.bindVertexArray(vao);
      const pb = gl.createBuffer(), ub = gl.createBuffer(), sb = gl.createBuffer(), ib = gl.createBuffer();
      const p = n === "head" ? progH : prog;
      const bind = (buf, data, name, usage) => {
        gl.bindBuffer(gl.ARRAY_BUFFER, buf); gl.bufferData(gl.ARRAY_BUFFER, data, usage);
        const loc = gl.getAttribLocation(p, name); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
      };
      bind(pb, new Float32Array(g.n * 2), "a_pos", gl.DYNAMIC_DRAW);
      bind(ub, g.uv, "a_uv", gl.STATIC_DRAW);
      if (gl.getAttribLocation(p, "a_src") >= 0) bind(sb, g.src, "a_src", gl.STATIC_DRAW);
      gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ib); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, g.idx, gl.STATIC_DRAW);
      gl.bindVertexArray(null);
      // precomputed skin weights
      const w1 = new Float32Array(g.n), w2 = new Float32Array(g.n), wc = new Float32Array(g.n);
      const arm = rig[n];
      for (let v = 0; v < g.n; v++) {
        const x = g.src[2 * v], y = g.src[2 * v + 1];
        wc[v] = 1 - sstep(rig.waist[0], rig.waist[1], y);
        if (arm && arm.n) {
          const ds = (x - arm.A[0]) * arm.n[0] + (y - arm.A[1]) * arm.n[1];
          const ax = arm.tip[0] - arm.pivot[0], ay = arm.tip[1] - arm.pivot[1], len = Math.hypot(ax, ay);
          const s = ((x - arm.pivot[0]) * ax + (y - arm.pivot[1]) * ay) / len;
          w1[v] = sstep(-6, 120, ds) * sstep(-60, 60, s);
          w2[v] = sstep(len * 0.2, len * 1.0, s) * w1[v];
        }
      }
      L[n] = { rect, tex, vao, pb, g, w1, w2, wc, out: new Float32Array(g.n * 2), prog: p };
    });

    const W = canvas.width, H = canvas.height;
    const k0 = opts.height / (rig.bbox[3] - rig.bbox[1]);
    const feetC = opts.feet;

    function render(pose0) {
      const P = Object.assign({}, DEFAULT_POSE, pose0);
      P.armR = Object.assign({}, DEFAULT_POSE.armR, pose0.armR);
      P.armL = Object.assign({}, DEFAULT_POSE.armL, pose0.armL);
      gl.viewport(0, 0, W, H);
      gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);
      if (P.opacity <= 0.001) return;
      gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
      const k = k0 * P.scale;
      const M = mul(T(feetC[0] + P.x, feetC[1] + P.y), mul(S(k, k), T(-rig.feet[0], -rig.feet[1])));
      const b = P.breath;
      const C = mul(T(P.chestX, P.chestY), about(rig.hip, mul(R(P.chestRot), S(1 + 0.0025 * b, 1 + 0.006 * b))));

      // body: legs fixed, upper body follows C
      {
        const l = L.body, s = l.g.src, o = l.out;
        for (let v = 0; v < l.g.n; v++) {
          const x = s[2 * v], y = s[2 * v + 1], w = l.wc[v];
          const c = ap(C, x, y);
          const q = ap(M, x + (c[0] - x) * w, y + (c[1] - y) * w);
          o[2 * v] = q[0]; o[2 * v + 1] = q[1];
        }
      }
      // arms: shoulder seam glued to the chest; upper rotation about the shoulder, soft bend mid-arm
      for (const n of ["armR", "armL"]) {
        const l = L[n], arm = rig[n], st = P[n], sg = -arm.side;
        const U = about(arm.pivot, R(sg * st.up));
        const el = [arm.pivot[0] + (arm.tip[0] - arm.pivot[0]) * 0.45, arm.pivot[1] + (arm.tip[1] - arm.pivot[1]) * 0.45];
        const UE = mul(U, about(el, R(sg * st.bend)));
        const MC = mul(M, C);
        const s = l.g.src, o = l.out;
        for (let v = 0; v < l.g.n; v++) {
          const x = s[2 * v], y = s[2 * v + 1], a1 = l.w1[v], a2 = l.w2[v];
          const pu = ap(U, x, y), pl = ap(UE, x, y);
          const qx = x * (1 - a1) + pu[0] * (a1 - a2) + pl[0] * a2;
          const qy = y * (1 - a1) + pu[1] * (a1 - a2) + pl[1] * a2 - st.lift * a1;
          const q = ap(MC, qx, qy);
          o[2 * v] = q[0]; o[2 * v + 1] = q[1];
        }
      }
      // head: rigid on the chest, roll about the neck
      const HM = mul(mul(M, C), mul(T(0, P.headY), about(rig.head.neck, R(P.headRoll))));
      {
        const l = L.head, s = l.g.src, o = l.out;
        for (let v = 0; v < l.g.n; v++) { const q = ap(HM, s[2 * v], s[2 * v + 1]); o[2 * v] = q[0]; o[2 * v + 1] = q[1]; }
      }

      for (const n of ["body", "armR", "armL", "head"]) {
        const l = L[n];
        gl.useProgram(l.prog);
        gl.bindVertexArray(l.vao);
        gl.bindBuffer(gl.ARRAY_BUFFER, l.pb); gl.bufferSubData(gl.ARRAY_BUFFER, 0, l.out);
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, l.tex);
        gl.uniform1i(gl.getUniformLocation(l.prog, "u_tex"), 0);
        gl.uniform2f(gl.getUniformLocation(l.prog, "u_res"), W, H);
        gl.uniform1f(gl.getUniformLocation(l.prog, "u_op"), P.opacity);
        if (n === "head") {
          const r = l.rect;
          gl.uniform4f(gl.getUniformLocation(l.prog, "u_rect"), r.x, r.y, r.w, r.h);
          gl.uniform2f(gl.getUniformLocation(l.prog, "u_c"), rig.head.c[0], rig.head.c[1]);
          gl.uniform1f(gl.getUniformLocation(l.prog, "u_r"), rig.head.r);
          // inverse of (pitch * yaw): x right, y down, z toward viewer
          const y = P.headYaw * DEG, p = P.headPitch * DEG;
          const cy = Math.cos(y), sy = Math.sin(y), cp = Math.cos(p), sp = Math.sin(p);
          // forward Ry: x'=x cy + z sy, z'=-x sy + z cy ; Rp: y'=y cp + z sp, z'=-y sp + z cp
          // inverse = Ry^T * Rp^T ; build as column-major mat3
          const RyT = [[cy, 0, -sy], [0, 1, 0], [sy, 0, cy]];   // rows
          const RpT = [[1, 0, 0], [0, cp, -sp], [0, sp, cp]];
          const m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
          for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) for (let q = 0; q < 3; q++) m[i][j] += RyT[i][q] * RpT[q][j];
          gl.uniformMatrix3fv(gl.getUniformLocation(l.prog, "u_inv"), false, [m[0][0], m[1][0], m[2][0], m[0][1], m[1][1], m[2][1], m[0][2], m[1][2], m[2][2]]);
        }
        gl.drawElements(gl.TRIANGLES, l.g.idx.length, gl.UNSIGNED_SHORT, 0);
      }
      gl.bindVertexArray(null);
    }
    return { render, gl, k0, rig };
  }

  window.MPPuppet = { create, DEFAULT_POSE };
})();
