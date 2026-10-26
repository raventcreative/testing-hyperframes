import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import draco3d from 'draco3dgltf';
import fs from 'fs';
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({
  'draco3d.decoder': await draco3d.createDecoderModule(), 'draco3d.encoder': await draco3d.createEncoderModule() });
const doc = await io.read(process.argv[2]);
const root = doc.getRoot();
for (const m of root.listMeshes()) for (const p of m.listPrimitives()) {
  const pos = p.getAttribute('POSITION'), idx = p.getIndices();
  console.log('verts', pos.getCount(), 'tris', idx ? idx.getCount()/3 : pos.getCount()/3);
}
for (const t of root.listTextures()) { const img=t.getImage(); console.log('tex', t.getName(), t.getMimeType(), t.getSize(), img.byteLength); fs.writeFileSync('work/'+t.getName().replace(/\.(jpg|png)$/,'')+'.webp', img); }
