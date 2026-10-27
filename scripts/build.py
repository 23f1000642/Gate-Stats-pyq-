import re, json, os, io, base64, glob, collections, sys
sys.path.insert(0,'scripts')
from families import family, FAM
from PIL import Image
TOPICS=[('CAL','Calculus'),('LA','Linear Algebra'),('PROB','Probability & Events'),('RV','Random Variables & Distributions'),
('JD','Joint Distributions & Conditioning'),('LT','Limit Theorems & Convergence'),('SP','Markov Chains & Poisson Process'),
('EST','Point Estimation'),('CI','Interval Estimation'),('TH','Testing of Hypotheses'),('NP','Nonparametric Inference'),
('REG','Regression & Linear Models'),('MV','Multivariate Analysis'),('DOE','Design of Experiments & ANOVA'),('GA','General Aptitude')]
TN=dict(TOPICS)
KEYS=['topic','pattern','type','ans','marks','concept','solution','shortcut','trap']
def parse(path):
    txt=open(path).read()
    out=[]
    for blk in re.split(r'^=== ',txt,flags=re.M)[1:]:
        head,_,body=blk.partition('\n')
        y,q=head.split()
        d={'y':int(y),'q':int(q)}
        cur=None
        for line in body.split('\n'):
            m=re.match(r'^('+'|'.join(KEYS)+r'):\s?(.*)$',line)
            if m: cur=m.group(1); d[cur]=m.group(2); continue
            if cur: d[cur]+='\n'+line
        for k in list(d):
            if isinstance(d[k],str): d[k]=d[k].strip()
        assert d.get('topic') in TN, (y,q,d.get('topic'))
        for k in ['pattern','type','ans','concept','solution']: assert d.get(k),(y,q,k)
        out.append(d)
    return out
def marks(y,q): return 1 if q<=35 else 2
allq=[]
for f in sorted(glob.glob('solutions/*.txt')): allq+=parse(f)
allq.sort(key=lambda d:(d['y'],d['q']))
seen=set()
for d in allq:
    k=(d['y'],d['q']); assert k not in seen,k; seen.add(k)
    d['id']=f"{d['y']}_{d['q']:02d}"; d['m']=int(d.get('marks') or marks(d['y'],d['q']))
# pattern groups
pg=collections.defaultdict(list)
for d in allq: pg[d['pattern'].lower()].append(d['id'])
# images
def webp(id):
    if not os.path.exists(f'build/qimg/{id}.png'): return ''
    import numpy as np
    im=Image.open(f'build/qimg/{id}.png').convert('RGB')
    arr=np.asarray(im).astype(int)
    if ((arr.max(2)-arr.min(2))>60).sum()<150: im=im.convert('L')
    if im.width>1000:
        im=im.resize((1000,round(im.height*1000/im.width)),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'WEBP',quality=72,method=6); return base64.b64encode(b.getvalue()).decode()
idx={'topics':[],'q':[]}
fsheet={}
for fp in glob.glob('formulas/*.md'):
    fsheet[os.path.splitext(os.path.basename(fp))[0]]=open(fp).read().strip()
for code,name in TOPICS:
    qs=[d for d in allq if d['topic']==code]
    idx['topics'].append({'id':code,'name':name,'n':len(qs),'marks':sum(d['m'] for d in qs),'f':fsheet.get(code,'')})
    payload={}
    for d in qs:
        payload[d['id']]={'img':webp(d['id']),**{k:d.get(k,'') for k in ['concept','solution','shortcut','trap']}}
    json.dump(payload,open(f'site/data/{code}.json','w'),separators=(',',':'))
for d in allq: d['fam']=family(d['topic'],d['pattern']); assert d['fam'],d['id']
fg=collections.defaultdict(list)
for d in allq: fg[(d['topic'],d['fam'])].append(d['id'])
for d in allq:
    sim=[x for x in pg[d['pattern'].lower()] if x!=d['id']]
    fam=[x for x in fg[(d['topic'],d['fam'])] if x!=d['id'] and x not in sim]
    idx['q'].append({'id':d['id'],'y':d['y'],'q':d['q'],'t':d['topic'],'p':d['pattern'],'f':d['fam'],'ty':d['type'],'a':d['ans'],'m':d['m'],'sim':sim,'fam':fam})
for t in idx['topics']: t['fams']=[n for n,_ in FAM[t['id']]]
json.dump(idx,open('site/data/index.json','w'),separators=(',',':'))
print(len(allq),'questions;', collections.Counter(d['topic'] for d in allq))
print('sizes', sum(os.path.getsize(f) for f in glob.glob('site/data/*.json'))//1024,'KB')
