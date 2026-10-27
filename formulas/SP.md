## Markov chains
- $\pi_n=\pi_0P^n$. Path probability: $P(X_0=i_0,\dots)=\pi_0(i_0)p_{i_0i_1}p_{i_1i_2}\cdots$
- **Bridge:** $P(X_2=j|X_1=i,X_3=k)=\frac{p_{ij}p_{jk}}{(P^2)_{ik}}$.
- **Classification (finite chains):** a closed communicating class is recurrent. A state that leaks out is transient. Absorbing means $p_{ii}=1$.
- **Period** = gcd of return lengths. Any $p_{ii}>0$ makes it aperiodic. Loops of lengths 2 and 3 give period 1.
- **Stationary:** $\pi P=\pi$, $\sum\pi=1$. Unique iff exactly one closed class. A doubly stochastic $P$ has uniform $\pi$.
- **2-state chain** $\begin{pmatrix}1-a&a\\b&1-b\end{pmatrix}$: $\pi=\left(\frac b{a+b},\frac a{a+b}\right)$.
- **First-step analysis:** $h_i=\sum_jp_{ij}h_j$ with boundary values 0 or 1.
- **Periodic chains:** $\lim P^n$ doesn't exist. Use $\lim P^{dn}$ along the period.

## Poisson process
- $N(t)\sim\text{Poi}(\lambda t)$, with independent increments. $\operatorname{Cov}(N(s),N(t))=\lambda\min(s,t)$. For increments, $\operatorname{Cov}=\lambda|I\cap J|$.
- Inter-arrival times are i.i.d. $\text{Exp}(\lambda)$. $S_n\sim\text{Gamma}(n,\lambda)$, with $P(S_n>t)=P(N(t)<n)$.
- Given $N(t)=n$, arrival times are uniform order statistics: $E T_k=\frac{kt}{n+1}$, and $N(s)\mid N(t)=n\sim\text{Bin}(n,\frac st)$.
- **Thinning** with probability $p$ gives independent Poisson($\lambda p$) and Poisson($\lambda(1-p)$) processes.
- $EN(t)^2=\lambda t+\lambda^2t^2$.
- **Races:** $P(\text{A first})=\frac{\lambda_A}{\lambda_A+\lambda_B}$, and memorylessness restarts the race.

## Birth–death & Brownian motion
- Pure birth: $T=\sum\text{Exp}(\lambda_n)$, $ET=\sum\frac1{\lambda_n}$, $\operatorname{Var}T=\sum\frac1{\lambda_n^2}$.
- Forward equation: $p_i'=\lambda_{i-1}p_{i-1}+\mu_{i+1}p_{i+1}-(\lambda_i+\mu_i)p_i$.
- Birth–death stationary: $\pi_{n+1}=\pi_n\frac{\lambda_n}{\mu_{n+1}}$.
- Brownian motion: $W(t)\sim N(0,t)$, $E W(s)W(t)=\min(s,t)$. Split into independent increments. $\operatorname{Var}(W_sW_t)=st+s^2$ for $s<t$. $E[W_t|W_s]=W_s$ and $E[W_t^2|W_s]=W_s^2+(t-s)$.
