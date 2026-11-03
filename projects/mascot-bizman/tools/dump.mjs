// dump POSITION / TEXCOORD_0 / indices of the first primitive to raw float32/uint32 files for analysis
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import fs from 'fs';
const [src, outPrefix] = process.argv.slice(2);
const doc = await new NodeIO().registerExtensions(ALL_EXTENSIONS).read(src);
const p = doc.getRoot().listMeshes()[0].listPrimitives()[0];
fs.writeFileSync(outPrefix + '_pos.f32', Buffer.from(p.getAttribute('POSITION').getArray().buffer));
fs.writeFileSync(outPrefix + '_uv.f32', Buffer.from(p.getAttribute('TEXCOORD_0').getArray().buffer));
fs.writeFileSync(outPrefix + '_idx.u32', Buffer.from(Uint32Array.from(p.getIndices().getArray()).buffer));
const tex = doc.getRoot().listTextures();
for (const t of tex) fs.writeFileSync(outPrefix + '_' + (t.getName() || 'tex').replace(/[^a-z0-9_]/gi, '') + '.webp', Buffer.from(t.getImage()));
console.log('done', p.getAttribute('POSITION').getCount(), tex.map((t) => t.getName()));
