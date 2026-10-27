from PIL import Image
import numpy as np, sys
for i in sys.argv[1:]:
    im=Image.open(f'build/qimg/{i}.png'); a=np.asarray(im.convert('L'))<200
    rows=a.any(1); h=len(rows)
    # find last blank run >=6 rows
    r=h-1
    while r>0 and rows[r]: r-=1
    run=0; cut=None
    for y in range(h-1,-1,-1):
        if not rows[y]: run+=1
        else:
            if run>=6 and cut is None and y<h-5: cut=y+3; break
            run=0
    print(i,h,cut); im.crop((0,0,im.width,cut)).save(f'build/qimg/{i}.png')
