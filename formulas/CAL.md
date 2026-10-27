## Limits & series
- **Riemann sum:** $\lim\frac1n\sum_{k=1}^{n}f\left(\frac kn\right)=\int_0^1f(x)\,dx$. If the sum runs to $pn$, the upper limit is $p$.
- **Standard limits:** $(1+n)^{1/n}\to1$, $\left(1+\frac an\right)^n\to e^a$, $\frac{u}{\sqrt{u+a^2}-a}\to2a$ as $u\to0$.
- **Second difference:** $\lim_{h\to0}\frac{f(h)+f(-h)-2f(0)}{h^2}=f''(0)$. A Taylor expansion is often faster.
- **Monotone + bounded ⇒ convergent.** For $a_{n+1}=g(a_n)$, the limit solves $L=g(L)$. Show monotonicity by comparing $a_{n+1}-a_n$ with the sign of $g(a)-a$.
- **Radius of convergence:** $\frac1R=\limsup|a_n|^{1/n}$. Use the root test when the coefficients alternate in form.
- **Alternating series:** converges if the terms decrease to 0 (Leibniz). It is conditionally convergent if $\sum|a_n|$ diverges, e.g. $\sim\frac1n$.
- **Partial sums:** if $b_n=\sum_{k\le n}a_k$, then $\sum b_nx^n=\frac{1}{1-x}\sum a_nx^n$.
- **Countability:** finite products, countable unions and finitely supported sequences are countable. $\{0,1\}^{\mathbb N}$, $(0,1)$ and infinite digit choices are uncountable. Disjoint open intervals form a countable family (one rational in each).

## Continuity & differentiability
- **Two-variable continuity at 0:** use polar form $x=r\cos\theta$, $y=r\sin\theta$. If $|f|\le r^k g(\theta)$ with $k>0$, then $f$ is continuous.
- **Differentiable at $p$:** $\frac{f(p+h)-f(p)-\nabla f\cdot h}{\|h\|}\to0$. A function with total "vanishing degree" $>1$ (e.g. $|k|\,|h|^{1/2}$) is differentiable with zero gradient.
- **Partial derivatives exist but $f_x$ is discontinuous:** compare $f_x$ along $y=0$ and along $x=0$.
- **Uniform continuity:** a bounded derivative (Lipschitz) gives UC. Continuous on a compact set gives UC. Continuous with finite limits at $\pm\infty$ gives UC. Not UC: $x^2$, $e^{x^2}$, $x\sin x$, $\sin(x^2)$ and $\frac1x$ near 0.
- **Darboux:** a derivative has the intermediate value property, even if it is discontinuous.
- **Integrating factor:** $f'+af>0$ means $(e^{ax}f)'>0$.
- **Integral equations:** differentiate both sides with the FTC, and get the initial value from $x=0$.

## Maxima & minima
- **Two-variable test** at a critical point: $D=f_{xx}f_{yy}-f_{xy}^2$. $D>0$ with $f_{xx}>0$ is a min, with $f_{xx}<0$ a max. $D<0$ is a saddle. If $f_{xx}=f_{yy}=0$ and $f_{xy}\ne0$, it is a saddle.
- **Constraint substitution:** on $x^2\pm y^2=c$, substitute $y^2$, then **check the domain** (e.g. $|x|\ge2$).
- **AM–GM tricks:** on $ax^2+by^2=1$, $\max xy=\frac1{2\sqrt{ab}}$.
- **Point to disk:** max distance $=R+d$, min distance $=\max(R-d,0)$.
- **Infeasible free optimum ⇒ the optimum lies on the boundary.**

## Integration
- **Area between curves:** $\int(\text{top}-\text{bottom})$. Parabola–chord area $=\frac{|a|(\beta-\alpha)^3}6$.
- **Volume with square cross-sections:** $\int(\text{side})^2dx$.
- **Polar:** $dx\,dy=r\,dr\,d\theta$. Also $\int_0^{\pi/4}\sec\theta\,d\theta=\ln(1+\sqrt2)$.
- **Simplex (Dirichlet):** $\int_{x+y+z\le1}x^ay^bz^c=\frac{a!\,b!\,c!}{(a+b+c+3)!}$. The volume is $\frac16$.
- **Green's theorem:** $\oint P\,dx+Q\,dy=\iint(Q_x-P_y)\,dA$, positive when anticlockwise.
- **Symmetry:** $\int_0^\pi f(\sin x)\cos x\,dx=0$.
