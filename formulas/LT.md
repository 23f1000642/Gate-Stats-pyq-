## Inequalities
- **Markov:** $P(X\ge a)\le\frac{EX}a$. **Chebyshev:** $P(|X-\mu|\ge k)\le\frac{\sigma^2}{k^2}$. **Jensen:** convex $g$ gives $Eg(X)\ge g(EX)$.

## Modes of convergence
- a.s. ⇒ in probability ⇒ in distribution. In $L^r$ ⇒ in probability. In distribution to a **constant** ⇒ in probability.
- In probability ⇒ a.s. along a subsequence. In probability does **not** imply moment convergence (mass escaping, e.g. $X_n=n$ w.p. $\frac1{n+1}$).
- **Borel–Cantelli:** $\sum P(A_n)<\infty$ means $P(A_n\text{ i.o.})=0$. For **independent** events, $\sum P(A_n)=\infty$ means $P(\text{i.o.})=1$. So independent $X_n\to0$ a.s. iff $\sum P(|X_n|>\epsilon)<\infty$.
- **Continuous mapping:** $g(X_n)\to g(X)$ for any mode.

## Laws & limits
- **WLLN/SLLN:** $\bar X\to\mu$. A ratio of sums tends to a ratio of moments. $EX^2=\sigma^2+\mu^2$.
- $P(\bar X_n>\mu+\epsilon)\to0$, and $P(\bar X_n>\mu)\to\frac12$.
- **CLT:** $\sqrt n(\bar X-\mu)\to N(0,\sigma^2)$. **Delta:** $\sqrt n(g(\bar X)-g(\mu))\to N(0,g'(\mu)^2\sigma^2)$.
- **Slutsky:** $X_n\to X$ and $Y_n\to c$ give $X_n+Y_n\to X+c$ and $X_nY_n\to cX$.
- $\operatorname{Var}(X^2)=2\sigma^4+4\mu^2\sigma^2$ for normal $X$.
- **Gumbel:** for Exp(1), $X_{(n)}-\ln n\to F(z)=e^{-e^{-z}}$, with median $-\ln\ln2$.
- Cauchy: $\bar X$ is Cauchy for every $n$, so no LLN.
- $\sum\pm2^{-i}$ with fair signs is $U(-1,1)$.
- A pointwise limit of CDFs need not be a CDF (mass escapes).
