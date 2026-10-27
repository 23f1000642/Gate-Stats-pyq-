import re, json, subprocess, os
rng={2019:(115,133),2020:(134,159),2021:(160,200),2022:(201,232),2023:(233,265),2024:(266,299),2025:(300,328)}
mine={}
for y in rng:
    for blk in re.split(r'^=== ',open(f'solutions/{y}.txt').read(),flags=re.M)[1:]:
        h,_,b=blk.partition('\n'); q=int(h.split()[1])
        a=re.search(r'^ans: (.*)$',b,re.M).group(1).strip(); t=re.search(r'^type: (.*)$',b,re.M).group(1).strip()
        mine[(y,q)]=(t,a)
out=[]
for y,(a,b) in rng.items():
    txt=subprocess.run(['pdftotext','-f',str(a),'-l',str(b),'-layout',os.environ.get('PYQ_PDF','source/pyq.pdf'),'-'],capture_output=True,text=True).stdout
    lines=txt.split('\n')
    cur=None; key={}
    for ln in lines:
        m=re.match(r'^\s{0,8}\(?(\d{1,2})[.)]\)?\s',ln)
        if m and 1<=int(m.group(1))<=65:
            n=int(m.group(1))
            if cur is None or n>cur and n-cur<=3: cur=n
        k=re.search(r'[Cc]orrect\s+(?:option|answer|options)\s*(?:is|are)?\s*\(?\s*([^)]*)\)?',ln)
        if k and cur and cur not in key: key[cur]=k.group(1).strip()
    for q in range(11,66):
        t,a=mine[(y,q)]
        out.append((y,q,t,a,key.get(q,'?')))
def norm(s): return re.sub(r'[\s,;]','',s.upper())
bad=[]
for y,q,t,a,k in out:
    if t in('MCQ','MSQ'):
        if norm(a)!=norm(k): bad.append((y,q,t,a,k))
    else:
        try:
            nums=[float(x) for x in re.findall(r'-?\d+\.?\d*',k.replace('–','-').replace(' ',''))]
            av=float(a)
            if not nums or not any(abs(av-v)<=0.011*max(1,abs(v)) for v in nums): bad.append((y,q,t,a,k))
        except: bad.append((y,q,t,a,k))
for b in bad: print(b)
print(len(bad))
