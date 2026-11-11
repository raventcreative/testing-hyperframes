// dump POSITION/NORMAL/UV/INDICES of the first primitive as raw little-endian arrays (for numpy analysis)
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import fs from 'fs';
const [src, outPrefix] = process.argv.slice(2);
const doc = await new NodeIO().registerExtensions(ALL_EXTENSIONS).read(src);
const p = doc.getRoot().listMeshes()[0].listPrimitives()[0];
fs.writeFileSync(outPrefix + '_pos.f32', Buffer.from(p.getAttribute('POSITION').getArray().buffer));
fs.writeFileSync(outPrefix + '_uv.f32', Buffer.from(p.getAttribute('TEXCOORD_0').getArray().buffer));
fs.writeFileSync(outPrefix + '_idx.u32', Buffer.from(Uint32Array.from(p.getIndices().getArray()).buffer));
console.log('ok', p.getAttribute('POSITION').getCount(), p.getIndices().getCount() / 3);
