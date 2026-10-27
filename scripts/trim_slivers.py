from PIL import Image
import numpy as np, glob
n=0
for f in glob.glob('build/qimg/*.png'):
    im=Image.open(f); a=np.asarray(im.convert('L'))<180; rows=a.any(1); h=len(rows)
    runs=[];y=0
    while y<h:
        v=rows[y]; s=y
        while y<h and rows[y]==v: y+=1
        runs.append((v,s,y))
    top,bot=0,h
    c=[r for r in runs if r[0]]
    if len(c)>1 and c[0][2]-c[0][1]<10 and np.argmax(a[c[0][1]:c[0][2]].any(0))<0.12*a.shape[1]: top=c[1][1]-6
    if len(c)>1 and c[-1][2]-c[-1][1]<10 and np.argmax(a[c[-1][1]:c[-1][2]].any(0))<0.12*a.shape[1]: bot=c[-2][2]+6
    if (top,bot)!=(0,h): im.crop((0,max(0,top),im.width,min(h,bot))).save(f); n+=1; print(f,top,bot,h)
print(n)
