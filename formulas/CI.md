## Pivots
| Situation | Pivot |
|---|---|
| Normal mean, $\sigma$ known | $\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$; length $\frac{2z\sigma}{\sqrt n}$, so $n\ge\left(\frac{2z\sigma}L\right)^2$ |
| Normal mean, $\sigma$ unknown | $\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1}$ |
| Normal variance | $\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}$ |
| $g(X)\sim\text{Exp}(\text{mean }\theta)$ | $\frac{2\sum g(X_i)}{\theta}\sim\chi^2_{2n}$ (Weibull: $X^2$ or $X^3$) |
| Scale family $X/\theta\sim F_0$ | equal tails: $F_0^{-1}(\frac\alpha2)$, $F_0^{-1}(1-\frac\alpha2)$ |
| Regression slope, $\sigma$ known | $\hat\beta\pm z\frac{\sigma}{\sqrt{S_{xx}}}$ |
- A CI is **not unique**: any split of $\alpha$ between the tails works. The equal split is shortest for symmetric pivots.
- **Notation trap:** check whether $\chi^2_{v,\alpha}$ means the upper-$\alpha$ point or the $\alpha$-quantile.
