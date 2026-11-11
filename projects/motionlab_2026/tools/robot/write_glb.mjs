// Rebuild the robot GLB from the arm-cut arrays (cut_arms.py): node write_glb.mjs <in_rt.glb> <cut_prefix_dir> <out.glb>
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import fs from 'fs';
const [src, dir, out] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(src);
const rd = (f, T) => { const b = fs.readFileSync(dir + '/' + f); return new T(b.buffer, b.byteOffset, b.byteLength / T.BYTES_PER_ELEMENT).slice(); };
const p = doc.getRoot().listMeshes()[0].listPrimitives()[0];
p.getAttribute('POSITION').setArray(rd('cut_pos.f32', Float32Array));
p.getAttribute('NORMAL').setArray(rd('cut_nrm.f32', Float32Array));
p.getAttribute('TEXCOORD_0').setArray(rd('cut_uv.f32', Float32Array));
p.getIndices().setArray(rd('cut_idx.u32', Uint32Array));
if (fs.existsSync(dir + '/cut_side.f32')) { const side = doc.createAccessor('side').setType('SCALAR').setArray(rd('cut_side.f32', Float32Array)).setBuffer(doc.getRoot().listBuffers()[0]); p.setAttribute('_SIDE', side); }
for (const e of doc.getRoot().listExtensionsUsed()) if (e.extensionName === 'KHR_materials_volume') e.dispose();
await io.write(out, doc);
console.log('wrote', out, p.getAttribute('POSITION').getCount(), p.getIndices().getCount() / 3);
