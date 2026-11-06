import numpy as np, sys
from PIL import Image
pos=np.load('tex_pos.npy'); comp=np.load('tex_comp.npy'); cov=comp>=0
def splat(texfile, out, crop=None, scale=900):
    col=np.asarray(Image.open(texfile).convert('RGB'))
    p=pos[cov]; c=col[cov]
    W,H=990,900; img=np.full((H,W,3),235,np.uint8)
    px=((p[:,0]+0.55)*scale).astype(int); py=((0.95-p[:,1])*scale).astype(int); ok=(px>=0)&(px<W)&(py>=0)&(py<H)
    o=np.argsort(p[ok,2]); img[py[ok][o],px[ok][o]]=c[ok][o]
    im=Image.fromarray(img)
    if crop: im=im.crop(crop)
    im.save(out)
if __name__=='__main__': splat(sys.argv[1], sys.argv[2], tuple(map(int,sys.argv[3].split(','))) if len(sys.argv)>3 else None)
