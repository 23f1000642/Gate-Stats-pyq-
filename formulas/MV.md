## Multivariate normal
- $a^TX\sim N(a^T\mu,a^T\Sigma a)$ and $\operatorname{Cov}(a^TX,b^TX)=a^T\Sigma b$. Jointly normal: independent iff covariance is 0.
- **Conditional:** $E(X_1|X_2)=\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2)$ and $\operatorname{Var}=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$.
- **Bivariate:** $E(Y|X)=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\mu_X)$ and $\operatorname{Var}(Y|X)=\sigma_Y^2(1-\rho^2)$.
- Read $\Sigma^{-1}$ from the exponent $-\frac12x^T\Sigma^{-1}x$, then invert.
- **Sheppard:** $P(X>\mu_X,Y>\mu_Y)=\frac14+\frac{\sin^{-1}\rho}{2\pi}$.
- $E\max(X,Y)=\sqrt{\frac{1-\rho}\pi}$ for standard bivariate normal. $E|N(0,\sigma^2)|=\sigma\sqrt{2/\pi}$.
- $P(\text{mean-zero combination}>0)=\frac12$.

## Correlations
- **Partial:** $\rho_{12\cdot3}=\frac{\rho_{12}-\rho_{13}\rho_{23}}{\sqrt{(1-\rho_{13}^2)(1-\rho_{23}^2)}}$. Equicorrelation $\rho$ gives $\frac\rho{1+\rho}$.
- **Multiple:** $R^2_{Y\cdot X}=\frac{\sigma_{YX}^T\Sigma_{XX}^{-1}\sigma_{XY}}{\sigma_{YY}}$.

## Quadratic forms, Wishart, Hotelling
- $X\sim N(0,I)$: $X^TAX\sim\chi^2_r$ iff $A$ is idempotent of rank $r$. Independent iff $AB=0$.
- $(X-\mu)^T\Sigma^{-1}(X-\mu)\sim\chi^2_p$ **only with the true $\Sigma$**.
- $\sum X_iX_i^T\sim W_p(n,\Sigma)$ and $(n-1)S\sim W_p(n-1,\Sigma)$. $BWB^T\sim W_q(n,B\Sigma B^T)$. Wisharts with the same $\Sigma$ add their d.f.
- For $W_p(n,I)$: $\operatorname{Var}W_{ii}=2n$ and $\operatorname{Var}W_{ij}=n$.
- **Hotelling:** $T^2=n(\bar X-\mu)^TS^{-1}(\bar X-\mu)\sim\frac{p(n-1)}{n-p}F_{p,n-p}$.
- MLE: $\hat\mu=\bar x$ and $\hat\Sigma=\frac1n\sum(x_i-\bar x)(x_i-\bar x)^T$ (**divisor $n$**).

## PCA, LDA, clustering
- PCs are eigenvectors of $\Sigma$. Proportion explained $=\frac{\lambda_1+\dots+\lambda_k}{\text{tr}\Sigma}$.
- **LDA** (equal priors and costs): assign to $P_1$ iff $(\mu_1-\mu_2)^T\Sigma^{-1}\left(z-\frac{\mu_1+\mu_2}2\right)\ge0$. With $\Sigma=I$, pick the nearest mean.
- **Single linkage** uses the minimum distance, **complete linkage** the maximum.
