## ANOVA degrees of freedom
| Design | Error d.f. |
|---|---|
| One-way, $k$ groups, $N$ obs | $N-k$; $F\sim F_{k-1,N-k}$ |
| Two-way, no interaction, 1 obs/cell | $(a-1)(b-1)$ |
| Two-way additive, $r$ per cell | $N-a-b+1$ |
| Two-way with interaction, $r$ per cell | $ab(r-1)$, which is 0 when $r=1$ |
- $\frac{SSE}{\sigma^2}\sim\chi^2_{\text{df}}$, which gives CIs for $\sigma^2$.
- **Estimable:** $\mu+\tau_i$ (by $\bar Y_{i\cdot}$) and contrasts $\sum c_i\tau_i$ with $\sum c_i=0$.

## Factorial & Latin squares
- **Confounding in 2 blocks:** the confounded effect $L$ is the one where all treatments in a block share the parity of letters in common with $L$. $(1),ab,ac,bc$ in one block means ABC is confounded.
- Standard Latin squares: order 3 has 1, order 4 has 4, order 5 has 56. Total = standard $\times n!(n-1)!$.
