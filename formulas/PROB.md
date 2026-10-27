## Core rules
- $A,B$ independent iff $P(A\cap B)=P(A)P(B)$. Then $A$ and $B^c$ are independent too.
- If $A\subset B$ with $0<P(A)$ and $P(B)<1$, they are **never** independent.
- **At least 2 of 3 independent events:** $P(EF)+P(EG)+P(FG)-2P(EFG)$.
- Pairwise independent does not imply mutually independent.
- **Conditioning on an event:** restrict to the event and renormalise. Use symmetry, e.g. $(x,y)\to(7-x,7-y)$ for dice.

## σ-fields
- $X$ is measurable w.r.t. $\mathcal G$ iff it is constant on each atom of $\mathcal G$.
- Probabilities on a generated σ-field are only defined on unions of atoms.
- On a countable $\Omega$, $\sum\alpha_n=1$ gives $\alpha_n\to0$, but not $\sum\sqrt{\alpha_n}<\infty$.
