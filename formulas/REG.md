## Simple linear regression
- $\hat\beta=\frac{S_{xy}}{S_{xx}}$ and $\hat\alpha=\bar y-\hat\beta\bar x$. If $\bar x=0$: $\hat\alpha=\bar y$ and $\hat\beta=\frac{\sum xy}{\sum x^2}$.
- $\operatorname{Var}\hat\beta=\frac{\sigma^2}{S_{xx}}$. $\operatorname{Var}\hat\alpha=\sigma^2\left(\frac1n+\frac{\bar x^2}{S_{xx}}\right)$. $\operatorname{Cov}(\hat\alpha,\hat\beta)=-\frac{\bar x\sigma^2}{S_{xx}}$, which is 0 if $\bar x=0$. $\operatorname{Cov}(\bar y,\hat\beta)=0$.
- **Mean response at $x_0$:** $\sigma^2\left(\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}\right)$.
- **Through the origin:** $\hat\beta=\frac{\sum xy}{\sum x^2}$.
- **Transformed regressor** ($x^2$, $\ln x$): substitute $z$ and use the same formulas.
- Weighted LS / BLUE with $\operatorname{Var}=\sigma_i^2$: weights $\propto\frac1{\sigma_i^2}$.
- **Variance estimates:** the $Y$ values are not needed. Only $x$ and $\sigma^2$.

## Multiple regression & ANOVA
- $\hat\sigma^2=\frac{SSE}{n-p}$, with $p$ = number of mean parameters. $E(SSR)=\sigma^2+\beta_1^2S_{xx}$ (simple).
- $F=\frac{SSR/k}{SSE/(n-k-1)}=\frac{R^2/k}{(1-R^2)/(n-k-1)}$.
- $R^2=\frac{SSR}{SST}$ and $R^2_{adj}=1-(1-R^2)\frac{n-1}{n-k-1}$.
- The joint confidence region for $(\beta_0,\beta_1)$ is an ellipse.
- **Ridge:** biased, normal, $\operatorname{Var}=(X^TX+\lambda I)^{-1}X^TX(X^TX+\lambda I)^{-1}$.
- **Identifiability:** only linear functions of $E(y)$ have unbiased estimators.
- OLS is unique iff $X$ has full column rank. The LAD/MLE under Laplace errors may be non-unique.
