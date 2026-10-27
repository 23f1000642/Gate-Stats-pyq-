## Dimensions
- Symmetric $n\times n$: $\frac{n(n+1)}2$. Skew-symmetric: $\frac{n(n-1)}2$. Each independent linear constraint subtracts 1.
- $\dim(U+V)=\dim U+\dim V-\dim(U\cap V)$.
- **Rank–nullity:** rank + nullity $=n$. $\text{rank}(BA)=\text{rank}(A)$ if $B$ is invertible.
- $M^2=0$ means $\text{rank}\le\frac n2$.
- For a square $A$, these are equivalent: invertible, RREF $=I$, 0 not an eigenvalue, $Ax=b$ always solvable, $\det\ne0$.
- Skew-symmetric of **odd** order means $\det=0$.

## Eigenvalues
- $\sum\lambda_i=\text{tr}A$ and $\prod\lambda_i=\det A$. For $2\times2$: $\lambda^2-(\text{tr})\lambda+\det=0$.
- Eigenvalues of $p(A)$, $A^{-1}$, $A^k$, $(A+cI)^{-1}$ are $p(\lambda)$, $\frac1\lambda$, $\lambda^k$, $\frac1{\lambda+c}$.
- $\text{tr}(A^k)=\sum\lambda_i^k$ and $\det p(A)=\prod p(\lambda_i)$.
- **Rank-one update:** $vv^T$ has eigenvalues $\|v\|^2,0,\dots,0$, so $\det(I+vv^T)=1+v^Tv$. Also $\det(aI+bJ)=a^{n-1}(a+nb)$.
- **Equicorrelation** $(1-\rho)I+\rho J$: eigenvalues $1+(n-1)\rho$ (once) and $1-\rho$ ($n-1$ times).
- **Idempotent:** eigenvalues 0 or 1, rank = trace. $I-M$ is idempotent and $(I+cM)^{-1}=I-\frac c{1+c}M$. Centring matrix $I-\frac1nJ$ has rank $n-1$.
- **Cayley–Hamilton ($2\times2$):** $A^2=(\text{tr}A)A-(\det A)I$.
- **Rotations:** eigenvalues $1,e^{\pm i\theta}$. An orthogonal matrix has $|\lambda|=1$.

## Diagonalization & Jordan form
- Diagonalizable iff geometric multiplicity = algebraic multiplicity for every $\lambda$, iff the minimal polynomial has distinct linear factors.
- Distinct eigenvalues means diagonalizable. A nilpotent diagonalizable matrix is $0$.
- Power of $(x-\lambda)$ in the minimal polynomial = size of the largest Jordan block. Number of blocks for $\lambda$ = nullity of $(A-\lambda I)$.
- $A^k=0$ but $A^{k-1}\ne0$ means the largest nilpotent block has size exactly $k$.
- Commutes with every matrix means $A=cI$.
- **Cayley transform:** $B=(I+A)^{-1}(I-A)$ is an involution and maps skew-symmetric to orthogonal.

## Definite matrices & singular values
- **Rayleigh:** $\lambda_{\min}\le\frac{x^TAx}{x^Tx}\le\lambda_{\max}$.
- A PD matrix has a unique PD square root. $A+cI$ is PD for large $c$.
- Singular values $=\sqrt{\text{eig}(A^TA)}$. Rank = number of non-zero singular values. $\text{tr}(A^TA)=\sum s_i^2$. All $s_i=1$ means orthogonal.
- **Orthonormal basis:** $u=\sum\langle u,v_i\rangle v_i$ and $\|u\|^2=\sum\langle u,v_i\rangle^2$.
