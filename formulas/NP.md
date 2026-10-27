## Rank tests
- **Sign test:** under $H_0$, $S\sim\text{Bin}(n,\frac12)$ (distribution-free). For odd $n$, $P(S\le\frac{n-1}2)=\frac12$.
- **Wilcoxon signed rank:** $2^n$ equally likely subsets. $ET^+=\frac{n(n+1)}4$, $\operatorname{Var}=\frac{n(n+1)(2n+1)}{24}$, symmetric about the mean. Count small-sum subsets by hand.
- **Mann–Whitney:** $U=\#\{x<y\}$ (ties count $\frac12$), $U_1+U_2=n_1n_2$, $U_1=R_1-\frac{n_1(n_1+1)}2$.
- **Median coverage:** $P(Y_1<\text{median}<Y_n)=1-2^{1-n}$.
- **Expected rank** of $Y_1$ among the sample: $1+\sum P(Y_1>\text{other})$.

## Empirical CDF & K–S
- $nF_n(x)\sim\text{Bin}(n,F(x))$ and $\operatorname{Cov}(F_n(x),F_n(y))=\frac1n[F(\min)-F(x)F(y)]$.
- **Glivenko–Cantelli:** $\sup|F_n-F|\to0$ a.s. The K–S statistic is distribution-free for continuous $F$.
- For uniform $F_0$: $D=\max_i\max\left(\frac in-u_{(i)},u_{(i)}-\frac{i-1}n\right)$.

## Rank correlation
- **Spearman:** $\rho_s=1-\frac{6\sum d^2}{n^3-n}$, with $\sum d^2\le\frac{n^3-n}3$.
- **Kendall** for bivariate normal: $\tau=\frac2\pi\sin^{-1}\rho$.
