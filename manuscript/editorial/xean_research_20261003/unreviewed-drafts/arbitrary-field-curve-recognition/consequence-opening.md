# Part Q. Closed-curve restriction and ground-field probes

The statements and arguments in this part are over an arbitrary complete
nontrivially valued field. They do not use perfection. In addition to the
foundations in T and C, we use these exact CLD calculus inputs, with complete
primary bodies in Appendix S. CLD 7.2.8--12 gives coefficient Radon measures
and locally bounded Borel multiplication for positive currents. CLD
7.2.7 and 7.3.1--3 gives positivity of integration and preservation of
positivity when wedging a strongly positive smooth form. CLD 7.7.1--8
gives weak continuity of differentiation, smooth Leibniz, ordinary-open
restriction, and compact direct-image compatibility. Canonical integration
on a boundaryless pure space is doubly closed. CLD 5.11.1 is Green's
formula on compact calibrated domains, and 5.9.5 gives finite-domain
inclusion-exclusion for boundary integration. CLD 13.7.1--2 gives purity
and the associated effective divisor cycle for the zero space of a regular
analytic function. They are used on reduced $S_1$ component sources only.

Smooth uniform approximation of a continuous function on a **fixed compact**
set, needed in the positive-limit lemma below, follows directly from T4.
Cover the compact by finitely many ordinary opens on which its oscillation
is less than $\epsilon$, select representative values, and multiply them
by a nonnegative compact subordinate partition of sum one near that compact.
Their sum is ordinary smooth and differs by at most $\epsilon$ there.
Thus no noncompact fixed-index compact-support partition theorem is used.

For Poincare--Lelong here we supply a proof with $S_1$ already imposed;
we do not import the reduction in CLD 16.7.5 claiming that one regular
element forces an arbitrary local ring to be $S_1$. The only local
dimension inference used from that discussion is valid: near a zero of
a regular function on a pure $r$-space, the fibre dimension is $r-1$;
upper semicontinuity (Ducros, *Variation de la dimension relative*,
Theorem 4.9, stated in CLD 11.4.5) and the lower bound CLD 11.5.2 imply
pure relative dimension $r-1$ after an ordinary shrinking. Every compact
domain in that neighbourhood retains this relative dimension and $S_1$.
The exact d=1 calibrated theorem stated in C then applies. Generic
lengths are constant on analytic-domain restrictions (CLD 13.2.6).

The arguments below reconstruct the positive cycle cuts and their local
weights. C1 already proves closed-embedding test lifting, and C2 already
proves rigid puncture removal. Numbered lemmas and equations within Q
are local to that part.

**Closed-curve restriction lemma.** Let $X$ be good, separated, strict,
boundaryless, pure of dimension $n\geq1$, let $\Omega$ be ordinary open,
and let $h$ be continuous finite on $\Omega$ with $D(h\delta_\Omega)=0$.
For every closed analytic subspace $C\hookrightarrow X$ pure of dimension
one, $D(h|_{C\cap\Omega}\delta_{C\cap\Omega})=0$ intrinsically. Both
structures may be nonreduced. The same assertion holds for a curve closed
in an ordinary open of $X$. The proof follows, keeping the component
lengths at every stage.
