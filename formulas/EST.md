## Sufficiency & completeness
- **Factorisation:** $f(x|\theta)=g(T(x),\theta)h(x)$.
- **Uniform families:** $U(0,\theta)$: $X_{(n)}$. $U(-\theta,\theta)$: $\max|X_i|$. $U(\theta,\theta+1)$: $(X_{(1)},X_{(n)})$, not complete.
- A full-rank exponential family gives a complete sufficient $T$. **Curved** families such as $N(\theta,\theta^2)$ or $N(\theta,2\theta^2)$ are **not complete**, and unbiased estimators are not unique.
- $N(-\theta,\theta)$ reduces to the one-parameter family in $\sum X^2$.
- A complete sufficient statistic is minimal. A one-to-one function of a complete statistic is complete.
- **Basu:** complete sufficient $\perp$ any ancillary. Location families: differences are ancillary. Scale families: ratios are ancillary.

## Point estimators
- **MLE:** solve $\ell'=0$. If the support depends on $\theta$, the MLE is an order statistic. **Restricted** $\Theta$: clip to the boundary. **Invariance:** $\widehat{g(\theta)}=g(\hat\theta)$.
- $\theta x^{\theta-1}$: $\hat\theta=\frac{-n}{\sum\ln x_i}$. Laplace: the sample median (non-unique for even $n$). Shifted exponential: $X_{(1)}$.
- **Method of moments:** set $\bar X=EX$, or use $EX^2$ when $EX$ doesn't involve $\theta$.
- **Unbiasedness:** $ES^2=\sigma^2$, but $ES<\sigma$. For $U(a,\theta)$: $\frac{n+1}n(X_{(n)}-a)+a$.
- **Lehmann–Scheffé:** an unbiased function of a complete sufficient statistic is the UMVUE. $E[h|T]$ gives the UMVUE.
- **Poisson UMVUEs:** $e^{-\theta}$: $(1-\frac1n)^T$. $P(X\le1)$: $(1-\frac1n)^T+\frac Tn(1-\frac1n)^{T-1}$.
- **CRLB:** $\frac{[g'(\theta)]^2}{nI(\theta)}$. $N(\mu,\sigma^2)$ mean: $\frac{\sigma^2}n$. Gamma scale $\beta$ with shape $\alpha$: $I=\frac\alpha{\beta^2}$.
- **Min-MSE multiple:** $c^*=\frac{(ET)^2}{ET^2}$.
- **Consistency:** bias $\to0$ and variance $\to0$.
