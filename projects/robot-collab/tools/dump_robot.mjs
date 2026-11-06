import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import fs from 'fs';
const [src, outdir] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(src);
const p = doc.getRoot().listMeshes()[0].listPrimitives()[0];
fs.writeFileSync(outdir + '/pos.f32', Buffer.from(p.getAttribute('POSITION').getArray().buffer));
fs.writeFileSync(outdir + '/nrm.f32', Buffer.from(p.getAttribute('NORMAL').getArray().buffer));
fs.writeFileSync(outdir + '/uv.f32', Buffer.from(p.getAttribute('TEXCOORD_0').getArray().buffer));
fs.writeFileSync(outdir + '/idx.u32', Buffer.from(new Uint32Array(p.getIndices().getArray()).buffer));
const mat = p.getMaterial();
for (const [k, t] of [['base', mat.getBaseColorTexture()], ['normal', mat.getNormalTexture()], ['mr', mat.getMetallicRoughnessTexture()]]) {
  fs.writeFileSync(outdir + '/rt_' + k + '.' + (t.getMimeType().split('/')[1]), t.getImage()); console.log(k, t.getMimeType(), t.getSize());
}
console.log('verts', p.getAttribute('POSITION').getCount(), 'tris', p.getIndices().getCount() / 3);
