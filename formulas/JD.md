## Joint, marginal & conditional
- $f(y|x)=\frac{f(x,y)}{f_X(x)}$. The regression of $Y$ on $X$ is $E(Y|X)$. Recognise kernels: $y^{a-1}e^{-by}$ means Gamma$(a,b)$.
- **Classic pair:** $e^{-y}$ on $0<x<y$ gives $X\sim\text{Exp}(1)$, $Y-X\sim\text{Exp}(1)$, $E(Y|X)=X+1$, $E(X|Y)=\frac Y2$.
- **Tower & total variance:** $EY=E[E(Y|X)]$ and $\operatorname{Var}Y=E\operatorname{Var}(Y|X)+\operatorname{Var}E(Y|X)$.
- $f(x,y)$ factorising **and** a product-shaped support means independence. A triangular support means dependence.

## Multinomial
- Marginals are binomial, and merged cells are binomial.
- $X_j\mid X_i=x\sim\text{Bin}\left(n-x,\frac{p_j}{1-p_i}\right)$ and $\operatorname{Cov}(X_i,X_j)=-np_ip_j$.

## Recognising structure
- $\frac{e^{-2}}{x!(y-x)!}$ means $X\sim\text{Poi}(1)$ plus an independent $\text{Poi}(1)$. Then $Y\sim\text{Poi}(2)$ and $X|Y\sim\text{Bin}(Y,\frac12)$.
- Joint MGF $e^{2s^2+t}$ means $N(0,4)$ and the constant 1. $e^{u^2/2}(1-2v)^{-3}$ means $N(0,1)\perp\chi^2_6$.
- A joint CDF that factorises means independence. Read each marginal off its own variable.
- The density $1+\prod g(x_i)$ with $\int g=0$ is pairwise independent but not mutually.
- Uncorrelated does not imply independent, except under joint normality.
