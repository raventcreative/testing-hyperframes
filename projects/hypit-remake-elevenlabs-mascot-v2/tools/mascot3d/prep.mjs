// Non-destructive: reads the original Tripo GLB, writes an optimized copy for real-time rendering.
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import { weld, simplify, prune, dedup, textureCompress } from '@gltf-transform/functions';
import { MeshoptSimplifier } from 'meshoptimizer';
import draco3d from 'draco3dgltf';
import sharp from 'sharp';
const [src, out, ratio] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({
  'draco3d.decoder': await draco3d.createDecoderModule(), 'draco3d.encoder': await draco3d.createEncoderModule() });
const doc = await io.read(src);
for (const e of doc.getRoot().listExtensionsUsed()) if (e.extensionName === 'KHR_draco_mesh_compression') e.dispose();
await MeshoptSimplifier.ready;
await doc.transform(weld({}), simplify({ simplifier: MeshoptSimplifier, ratio: Number(ratio || 0.07), error: 0.0008, lockBorder: false }), dedup(), prune());
await doc.transform(textureCompress({ encoder: sharp, targetFormat: 'webp', quality: 92, resize: [2048, 2048] }));
for (const m of doc.getRoot().listMeshes()) for (const p of m.listPrimitives()) console.log('tris', p.getIndices().getCount()/3, 'verts', p.getAttribute('POSITION').getCount());
await io.write(out, doc);
