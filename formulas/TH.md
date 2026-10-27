## Size, power, p-value
- Size $=\sup_{\theta\in H_0}P_\theta(\text{reject})$. Power $=P_{\theta\in H_1}(\text{reject})$. Type I: reject a true $H_0$. Type II: accept a false $H_0$.
- p-value $=P_{H_0}(T\text{ at least as extreme as observed})$. Two-sided z-test: $2(1-\Phi(|z|))$.
- Sample size: $n\ge\left(\frac{(z_\alpha+z_\beta)\sigma}{\mu_1-\mu_0}\right)^2$.
- Power of the two-sided z-test at $\mu$: $P(\bar X>c)+P(\bar X<-c)$ with $\bar X\sim N(\mu,\sigma^2/n)$.

## Neyman–Pearson & UMP
- **MP test** (simple vs simple): reject when $\frac{f_1}{f_0}>k$. For discrete data, rank points by the ratio and randomise at the boundary: $\gamma=\frac{\alpha-\text{used}}{p_0(\text{boundary})}$.
- Power of an MP test is $\ge\alpha$. It is not unique on $\{f_1=kf_0\}$. With disjoint supports, power can reach 1.
- Simple vs simple: LRT = NP test.
- **MLR in $T$** gives a UMP one-sided test. UMP exists for $\theta\le\theta_0$ vs $>$, and for an interval alternative. **No UMP** for $\theta=\theta_0$ vs $\ne$, or for interval null vs outside. The two-sided z-test is UMP **unbiased**.
- Exponential mean: UMP rejects for large $\sum X$, with $\frac{2\sum X}{\lambda_0}\sim\chi^2_{2n}$. Normal variance with known mean: reject for large $\sum X^2$, which is $\chi^2_n$ under $H_0$.
- Normal vs Laplace: the ratio is monotone in $||x|-1|$.
- LRT $\Lambda=1$ when the MLE lies inside $H_0$.
- A Rao–Blackwellised test $E[\phi|T]$ has the **same power function**.

## Chi-square tests
- Goodness of fit: d.f. $=k-1-(\text{number of estimated parameters})$. $r\times c$ independence: $(r-1)(c-1)$.
- $2\times2$ shortcut: $\chi^2=\frac{N(ad-bc)^2}{R_1R_2C_1C_2}$.
