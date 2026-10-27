import re, sys, subprocess, json, html
from xml.etree import ElementTree as ET
import os
pdf=os.environ.get('PYQ_PDF','source/pyq.pdf')
years={2019:(3,14),2020:(15,30),2021:(31,46),2022:(47,62),2023:(63,79),2024:(80,98),2025:(99,114)}
os.makedirs('build',exist_ok=True)
out={}
for y,(a,b) in years.items():
    x=subprocess.run(['pdftotext','-bbox','-f',str(a),'-l',str(b),pdf,'-'],capture_output=True,text=True).stdout
    x=re.sub(r'<!DOCTYPE[^>]*>','',x); x=x.replace('&nbsp;',' ')
    x=re.sub(r'xmlns="[^"]*"','',x)
    root=ET.fromstring(x)
    pages=root.findall('.//page')
    found=[]
    for i,pg in enumerate(pages):
        pn=a+i
        for w in pg.findall('word'):
            t=w.text or ''
            xm=float(w.get('xMin'))
            m=re.fullmatch(r'\(?(\d{1,2})\.?\)?\.?',t)
            if m and xm<75 and ('(' in t or ')' in t or t.endswith('.')):
                found.append((pn,int(m.group(1)),round(xm),round(float(w.get('yMin'))),t))
    out[y]=found
    nums=[f[1] for f in found]
    print(y,len(found),nums)
json.dump(out,open('build/qpos.json','w'))
