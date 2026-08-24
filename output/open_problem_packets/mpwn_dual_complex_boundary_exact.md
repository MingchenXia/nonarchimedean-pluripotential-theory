# Exact verification packet: boundary continuity on a fixed dual complex

## Statement to verify

Let $X$ be a compact Kähler manifold, let $\alpha$ be a Kähler class, and
let $\Delta_{\mathcal X}$ be the finite dual complex of an snc analytic
model. Assume the following established inputs.

1. Every $\alpha$-psh function $\phi$, normalized by $\sup\phi=0$, satisfies
   $\phi\leq0$, and its restriction to each face of
   $\Delta_{\mathcal X}$ is an extended-real convex function.
2. Each rational point of a face is a divisorial valuation.
3. At each fixed divisorial valuation $v$, normalized $\alpha$-psh
   functions have a uniform lower bound $\phi(v)\geq-C_v$.
4. The restriction of every $\alpha$-psh function to a
   $d_\infty$-bounded subset is continuous, where
   $d_\infty(v,w)=\sup_{\phi\in\mathrm{PSH}(\alpha)}
   |\phi(v)-\phi(w)|$.

Then $\Delta_{\mathcal X}$ is $d_\infty$-bounded. Consequently every
$\alpha$-psh function is finite and continuous on all of
$\Delta_{\mathcal X}$, including the boundaries of its faces.

## Derivation to verify

Fix a maximal face $\sigma$ and a rational point $w_0$ in its relative
interior. By (2)--(3), there is $C_\sigma$ such that for every normalized
$\phi$,

\[
-C_\sigma\leq\phi(w_0)\leq0.
\]

For every $w\in\sigma$, other than the zero-dimensional trivial case,
extend the chord from $w$ through $w_0$ to the opposite boundary point
$y\in\sigma$, and write

\[
w_0=\lambda w+(1-\lambda)y.
\]

Since $w_0$ is a fixed relative-interior point of the compact simplex,
elementary compact geometry gives $\lambda\geq\lambda_0>0$, uniformly in
$w$. Convexity, interpreted in the extended-real sense, gives

\[
-C_\sigma\leq\phi(w_0)
\leq\lambda\phi(w)+(1-\lambda)\phi(y)
\leq\lambda\phi(w),
\]

because $\phi(y)\leq0$. The finite left side also rules out
$\phi(w)=-\infty$ or $\phi(y)=-\infty$. Therefore

\[
\phi(w)\geq-C_\sigma/\lambda_0
\quad\text{for all }w\in\sigma
\]

uniformly over all normalized psh $\phi$. Since the dual complex has
finitely many maximal faces, it is $d_\infty$-bounded. Input (4) now gives
continuity on the entire dual complex.

## Why verification is requested

MPWN25 v1, Theorem 7.1.2, PDF pp. 26--27, proves convexity and interior
continuity, then says it is enough to prove continuity at every vertex and
applies Proposition 7.1.4 only to the finite vertex set. Continuity on a
finite vertex set does not imply boundary continuity. The argument above is
a proposed repair using the same Proposition 7.1.4 on the whole dual
complex after proving the missing $d_\infty$-boundedness.

## Verification status

This is an exact verification input, not a receipt. The manuscript marker is
`% RETHLAS-NEW: mpwn-dual-complex-boundary-repair`.
