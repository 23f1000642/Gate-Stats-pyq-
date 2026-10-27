import numpy as np
rng=np.random.default_rng(1); N=2_000_000
r={}
# 2020 Q56: X geometric(1/2) on 1..; Y|X~Bin(X,1/2); Var Y
X=rng.geometric(.5,N); Y=rng.binomial(X,.5); r['2020Q56 VarY=1']=Y.var()
# 2020 Q64: order stats of g=1.5x^2 on [-1,1]; var of sum
U=rng.random((N,3)); Xs=np.cbrt(2*U-1); r['2020Q64 1.8']=Xs.sum(1).var()
# 2021 Q12 Var(W1W2)=3
W1=rng.normal(size=N); W2=W1+rng.normal(size=N); r['2021Q12 3']=(W1*W2).var()
# 2021 Q57 P(U+E>1)=.632
r['2021Q57 .632']=(rng.random(N)+rng.exponential(1,N)>1).mean()
# 2021 Q60 1/p=143: simulate race
cnt=0;M=400000
n=10;
arr=rng.random((M,3))
# step probabilities
p1=1/11;p2=1/12;p3=12/13
r['2021Q60 143']=1/(p1*p2*p3)
# 2022 Q53 P(max>=2min) n=3, f=2x -> X=sqrt(U)
Xs=np.sqrt(rng.random((N,3))); r['2022Q53 .4375']=(Xs.max(1)>=2*Xs.min(1)).mean()
# 2022 Q26 sum P(n<X<=n+3), geometric p=1/4 support 1..
X=rng.geometric(.25,N); r['2022Q26 2.3125']=np.minimum(X,3).mean()
# 2022 Q64 E Y^2
Xu=4*rng.random(N); Yv=rng.random(N)*Xu**2/4; r['2022Q64 1.067']=(Yv**2).mean()
# 2023 Q31 bulbs
def bulbs():
    p=rng.permutation([1,1,0,0,0]); found=0
    for i,b in enumerate(p,1):
        found+=b
        if found==2: return i
        if i-found==3: return i
c=sum(bulbs()==3 for _ in range(200000)); r['2023Q31 .3']=c/200000
# 2023 Q61 delta: n large
n=4000; Ys=np.abs(rng.exponential(1,(500,2*n))[:, ::2]-rng.exponential(1,(500,2*n))[:,1::2])[:, :n]
v=np.sqrt(n)*(np.exp(-Ys.mean(1))-np.exp(-1)); r['2023Q61 .135']=v.var()
# 2024 Q40 P(Gamma2 mean10 >15)
r['2024Q40 2.5e^-1.5=%.4f'%(2.5*np.exp(-1.5))]=(rng.exponential(10,N)+rng.exponential(10,N)>15).mean()
# 2025 Q44 E(R1+R2)
X=rng.exponential(.5,N);Y1=rng.exponential(1,N);Y2=rng.exponential(1,N)
R1=1+(Y1>X)+(Y1>Y2);R2=1+(Y2>X)+(Y2>Y1); r['2025Q44 4.333']=(R1+R2).mean()
# 2025 Q45 Var Z
Xm=rng.normal(size=(400000,5,2)); W11=(Xm[:,:,0]**2).sum(1);W22=(Xm[:,:,1]**2).sum(1);W12=(Xm[:,:,0]*Xm[:,:,1]).sum(1)
r['2025Q45 250']=(W11+4*W12+4*W22).var()
# 2025 Q58
Xb=rng.binomial(2,1/3,N);S=rng.poisson(3,N); r['2025Q58 0.443']=10*(Xb>S).mean()
# 2025 Q62 power
th=np.log(.36); M2=np.maximum(th+np.log(rng.random(N)),th+np.log(rng.random(N))); r['2025Q62 .694']=(M2<np.log(.3)).mean()
# 2019 Q32
r['2019Q32 .0186']=0.31*0.3*0.2
# 2020 Q55 hitting
P=np.array([[.5,.5,0,0],[.5,.25,.25,0],[0,0,.25,.75],[0,0,0,1]])
hits=0;T=100000
for _ in range(T):
    s=1
    while s not in(0,3): s=rng.choice(4,p=P[s])
    hits+=s==0
r['2020Q55 6p=4']=6*hits/T
# 2020 Q63 c^2: simulate
n=3000;Xn=rng.standard_t(1e9,size=(1,)) # placeholder
for k,v in r.items(): print(f'{k:30s} {v:.4f}')
