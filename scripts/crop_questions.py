import json, subprocess, os
from PIL import Image, ImageChops
d=json.load(open('build/qpos.json'))
DPI=160; S=DPI/72
TOP,BOT=74,756
os.makedirs('build/pages',exist_ok=True); os.makedirs('build/qimg',exist_ok=True)
years={2019:(3,14),2020:(15,30),2021:(31,46),2022:(47,62),2023:(63,79),2024:(80,98),2025:(99,114)}
def page(p):
    f=f'build/pages/p{p:03d}.png'
    if not os.path.exists(f):
        subprocess.run(['pdftoppm','-r',str(DPI),'-f',str(p),'-l',str(p),'-png','-singlefile','build/clean.pdf',f[:-4]],check=True)
    im=Image.open(f).convert('RGB')
    import numpy as np
    a=np.asarray(im).copy()
    a=a[:, 66:1258]
    return Image.fromarray(a)
def trim(im):
    bg=Image.new('RGB',im.size,(255,255,255))
    diff=ImageChops.difference(im,bg).convert('L').point(lambda v:255 if v>40 else 0)
    bb=diff.getbbox()
    if not bb: return None
    x0,y0,x1,y1=bb
    return im.crop((max(0,x0-10),max(0,y0-8),min(im.width,x1+10),min(im.height,y1+8)))
import re as _re, subprocess as _sp
from xml.etree import ElementTree as _ET
_words={}
def words(p):
    if p not in _words:
        x=_sp.run(['pdftotext','-bbox','-f',str(p),'-l',str(p),'build/clean.pdf','-'],capture_output=True,text=True).stdout
        x=_re.sub(r'<!DOCTYPE[^>]*>','',x).replace('&nbsp;',' '); x=_re.sub(r'xmlns="[^"]*"','',x)
        r=_ET.fromstring(x); _words[p]=[(float(w.get('xMin')),float(w.get('yMin')),float(w.get('yMax'))) for w in r.iter('word')]
    return _words[p]
import numpy as _np
_pg={}
def pagearr(p):
    if p not in _pg: _pg[p]=_np.asarray(page(p).convert('L'))<170
    return _pg[p]
OVR={(38,104):74,(76,100):74,(37,503):490,(37,537):526,(11,621):613,(37,598):580}
def adj(p,y):
    if (p,round(y)) in OVR: return OVR[(p,round(y))]
    a=pagearr(p); ym=int(y*S); lo=max(int(TOP*S),ym-int(70*S))
    rows=a[lo:ym-2].any(1)
    runs=[]; i=len(rows)-1
    while i>=0:
        if rows[i]:
            e=i
            while i>=0 and rows[i]: i-=1
            runs.append((lo+i+1,lo+e+1))
        else: i-=1
    top=ym-int(3*S)
    for r0,r1 in runs:
        if r1<top-int(14*S): break
        left=_np.argmax(a[r0:r1].any(0))
        if left>(200-33)*S: top=r0-3
        else: break
    return top/S
meta={}
for y,(a,b) in years.items():
    f=[tuple(x) for x in d[str(y)] if x[4]!='0.']
    f.sort(key=lambda t:(t[0],t[3]))
    # choose chain
    best=None
    for si,s in enumerate(f):
        if s[1]!=1: continue
        chain=[s]; pos=si
        for n in range(2,66):
            nxt=[j for j in range(pos+1,len(f)) if f[j][1]==n]
            if not nxt: break
            pos=nxt[0]; chain.append(f[pos])
        if len(chain)==65: best=chain
    assert best, y
    for i,(pg,n,x,yy,t) in enumerate(best):
        end = best[i+1] if i+1<len(best) else (b,99,0,BOT+4,'')
        parts=[]
        p=pg; ystart=adj(pg,yy)
        while True:
            yend = adj(end[0],end[3]) if (p==end[0] and end[1]!=99) else (end[3]-4 if p==end[0] else BOT)
            if yend<=ystart+8: yend=end[3]-4 if p==end[0] else BOT
            t2=None
            if yend>ystart+8:
                pim=page(p); im=pim.crop((0,int(ystart*S),pim.width,int(yend*S)))
                t2=trim(im)
            if t2: parts.append(t2)
            if p>=end[0]: break
            p+=1; ystart=TOP
        W=max(pp.width for pp in parts); H=sum(pp.height for pp in parts)
        out=Image.new('RGB',(W,H),'white'); yo=0
        for pp in parts: out.paste(pp,(0,yo)); yo+=pp.height
        fn=f'build/qimg/{y}_{n:02d}.png'; out.save(fn)
        meta[f'{y}_{n:02d}']={'page':pg,'w':W,'h':H}
    print(y,'ok')
json.dump(meta,open('build/qmeta.json','w'))
