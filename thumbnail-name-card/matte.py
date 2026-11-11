# Portrait matte with MODNet (Apache-2.0) -> person cutout PNG at the upscaled photo size.
import onnxruntime as ort, numpy as np, sys
from PIL import Image, ImageFilter
model, src, out = sys.argv[1:4]
im = Image.open(src).convert('RGB'); W, H = im.size
w, h = 576, 1024                                              # multiples of 32, ~512 ref
x = (np.asarray(im.resize((w, h), Image.BILINEAR)).astype(np.float32) / 255 - 0.5) / 0.5
a = ort.InferenceSession(model).run(None, {'input': x.transpose(2, 0, 1)[None]})[0][0, 0]
m = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)
m.save(out.replace('.png', '_matte.png'))
rgba = im.copy(); rgba.putalpha(m); rgba.save(out)
print(W, H, 'mean alpha', round(float(np.asarray(m).mean() / 255), 3))
