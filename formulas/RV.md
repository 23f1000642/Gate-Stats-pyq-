## Reading distributions
- **Jumps:** $P(X=a)=F(a)-F(a^-)$, $P(X<a)=F(a^-)$. In limits, check which endpoints the shrinking intervals keep.
- **MGF:** the coefficient of $e^{kt}$ is $P(X=k)$. A product of MGFs means a sum of independent variables. $(\tfrac34e^{2t}+\tfrac14)$ means an independent $\{0,2\}$-valued piece.
- **Common c.f.s:** $U(-a,a)$: $\frac{\sin at}{at}$. Cauchy: $e^{-|t|}$. Laplace: $\frac1{1+t^2}$. $N$: $e^{i\mu t-\sigma^2t^2/2}$.
- $\phi(t_0)=1$ for $t_0\ne0$ means $X$ lies on the lattice $\frac{2\pi}{t_0}\mathbb Z$, and $\phi$ has period $t_0$.
- A difference of i.i.d. variables has c.f. $|\phi|^2\ge0$, so $U(-a,a)$ is **not** such a difference.

## Transformations
- **Monotone:** $f_Y=f_X\left|\frac{dx}{dy}\right|$. Always check that the result integrates to 1.
- $F(X)\sim U(0,1)$, $-\ln U\sim\text{Exp}(1)$, $-2\ln U\sim\chi^2_2$, $E[(-\ln U)^k]=k!$.
- $X\sim U(-\frac\pi2,\frac\pi2)$: $\tan X$ and $\cot X$ are standard Cauchy.
- Laplace $\to|X-\mu|\sim$ Exp. Pareto $\to\ln X\sim$ Exp. $\theta x^{\theta-1}\to-\ln X\sim\text{Exp}(\theta)$.
- $\text{Exp}(\text{mean }\beta)$: $\frac{2Y}\beta\sim\chi^2_2$.

## Order statistics
- $f_{(k)}(x)=\frac{n!}{(k-1)!(n-k)!}F^{k-1}(1-F)^{n-k}f$. For $U(0,\theta)$, $EX_{(k)}=\frac{k\theta}{n+1}$.
- **Joint density:** $n!\prod f(x_i)$ on $x_1<\dots<x_n$. Symmetric functions are the same as for the unordered sample.
- $P(\min\ge c)=(1-F(c))^n$ and $P(\max\le c)=F(c)^n$.

## Moment facts
| Distribution | Mean | Variance | Extra |
|---|---|---|---|
| Bin$(n,p)$ | $np$ | $np(1-p)$ | $EX^2=np(1-p)+n^2p^2$ |
| Poisson$(\lambda)$ | $\lambda$ | $\lambda$ | $E\frac1{X+1}=\frac{1-e^{-\lambda}}\lambda$, $P(\text{even})=\frac{1+e^{-2\lambda}}2$, mode $\lfloor\lambda\rfloor$ |
| Geometric on $\{1,2,..\}$ | $\frac1p$ | $\frac{1-p}{p^2}$ | $E\min(X,k)=\sum_{j\le k}P(X\ge j)$ |
| Gamma(shape $a$, rate $\lambda$) | $\frac a\lambda$ | $\frac a{\lambda^2}$ | $E\frac1X=\frac{\lambda}{a-1}$, exists iff $a>1$ |
| Beta$(a,b)$ | $\frac a{a+b}$ | $\frac{ab}{(a+b)^2(a+b+1)}$ | $EX^2=\frac{a(a+1)}{(a+b)(a+b+1)}$ |
| $\chi^2_k$ | $k$ | $2k$ | $EV^r=2^r\frac{\Gamma(k/2+r)}{\Gamma(k/2)}$, $E\frac1V=\frac1{k-2}$ |
| Lognormal | $e^{\mu+\sigma^2/2}$ | | $\frac{EX^2}{(EX)^2}=e^{\sigma^2}$ |
| Weibull | | | $F=1-e^{-\lambda x^\alpha}$ |
- **Exponential races:** $P(X<Y)=\frac{\lambda_X}{\lambda_X+\lambda_Y}$ and $P(X>cY)=\frac{\lambda_Y}{\lambda_Y+c\lambda_X}$.
- $\frac{\chi^2_a}{\chi^2_a+\chi^2_b}\sim\text{Beta}(\frac a2,\frac b2)$, independent of the sum. For i.i.d. positive variables, $E\frac{Y_1}{\sum Y_i}=\frac1n$.
- **Random count:** $P(\max_{i\le N}X_i\le c)=G_N(F(c))$, where $G_N$ is the PGF.
