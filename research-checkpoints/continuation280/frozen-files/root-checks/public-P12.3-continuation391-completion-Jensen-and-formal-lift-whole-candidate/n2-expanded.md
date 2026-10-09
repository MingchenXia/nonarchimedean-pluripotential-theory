## 4. Complete Jensen theorem on compact Hausdorff spaces

Let $X$ be nonempty compact Hausdorff and $C\subset C(X,\mathbb R)$ a norm-closed convex cone of nonpositive functions, containing every negative constant and stable under finite maxima. Define $p_C(f)=\sup\{h\in C:h\le f\}$ for $f\in C(X,\mathbb R)$. A sufficiently negative constant is a competitor; hence $p_C(f)$ is finite bounded. It is lower semicontinuous. Negative shifting gives $\|p_C(f)-p_C(g)\|_\infty\le\|f-g\|_\infty$. If $D$ consists of actual decreasing $C$-nets, compact directed strict covers show its raw envelope agrees with this one: for $h_i\downarrow h\le f$, some $h_i<f+\varepsilon$ on all of $X$, and $h_i-\varepsilon\in C$ is a minorant. This is valid for nonmetrizable $X$ and arbitrary nets.

Put
\[
 J_x=\{\mu\ge0:\mu(X)\le1,\ h(x)\le\int h\,d\mu\ (h\in C)\}.
\]
Positive functionals and Radon measures are identified by the compact-Hausdorff Riesz theorem. The positive subprobability dual ball is weak-* compact; the inequalities make $J_x$ closed convex, and $\delta_x\in J_x$. The joint graph is closed since every $h$ is continuous. Its ambient product is compact, so this graph gives upper hemicontinuity: a contrary net of measures outside an open neighbourhood of $J_x$ has a converging subnet in that closed complement, contradicting the graph. This does not give lower hemicontinuity.

We prove the exact formula, including its signs:
\[
 p_C(f)(x)=\min_{\mu\in J_x}\int f\,d\mu. \tag{5}
\]
Consider the convex cone $W=\{(g,t):\exists h\in C,\ h\le g,\ t\le h(x)\}$ in $C(X)\times\mathbb R$. If $t>p_C(f)(x)$, the Lipschitz estimate places $(f,t)$ outside the norm closure of $W$. Hahn--Banach separation of a point from a closed convex cone supplies a continuous linear form $L(g,t)=\mu(g)-\alpha t$ nonnegative on $W$ and negative at $(f,t)$. Pairs $(r,-s)$ with $r\ge0,s\ge0$ belong to $W$, so $\mu$ is positive and $\alpha\ge0$. If $\alpha=0$, pairs $(-a,-a)$ force $-a\mu(X)\ge0$; positivity forces $\mu=0$, contradicting strict separation. Thus $\alpha>0$. Divide by $\alpha$. The same negative-constant pairs give $\mu(X)\le1$, and pairs $(h,h(x))$ give all Jensen inequalities. Separation gives $\int f\,d\mu<t$. Conversely each Jensen measure satisfies $h(x)\le\int h\,d\mu\le\int f\,d\mu$ for all competitors. Letting $t\downarrow p_C(f)(x)$ proves (5), with attainment by compactness. The mass bound is at most one, not necessarily one. In the cone of all nonpositive functions the zero measure is allowed and ensures the zero envelope of a positive obstacle; $\delta_x$ gives a negative obstacle at $x$.

There is the exact equivalence
\[
 \text{CE for all continuous signed }f
 \quad\Longleftrightarrow\quad x\mapsto J_x\text{ is weak lower hemicontinuous}. \tag{6}
\]
If lower hemicontinuity holds, a weak neighbourhood of a minimizing measure where $\int f$ is less than $p_C(f)(x)+\varepsilon$ meets every nearby fibre. This proves upper semicontinuity of $p_C(f)$, while its raw supremum already gives lower semicontinuity.

Conversely suppose CE holds and lower hemicontinuity fails at $x$. There is $\mu_0\in J_x$ and a weak neighbourhood $U$ of it missed by fibres along a net $x_i\to x$. Choose finitely many continuous tests $f_1,\ldots,f_s$ and a Euclidean ball of radius $\varepsilon>0$ around $y_0=(\int f_j\,d\mu_0)_j$ whose inverse image is contained in $U$. The compact convex projections $K_i=(\int f_j\,dJ_{x_i})_j$ avoid this ball. A closest point $z_i$ to $y_0$ exists, and the elementary squared-distance derivative at the minimizer gives, for $a_i=(z_i-y_0)/\|z_i-y_0\|$,
\[
 a_i\cdot(y-y_0)\ge\varepsilon\quad(y\in K_i).
\]
Take a subnet with $a_i\to a$ in the finite-dimensional unit sphere. All projected points are uniformly bounded, since the measures have mass at most one. Therefore for $f=\sum a_j f_j$ and all sufficiently late indices, every $\mu\in J_{x_i}$ satisfies $\int f\,d\mu\ge\int f\,d\mu_0+\varepsilon/2$. Formula (5) then contradicts continuity at $x$, since $p_C(f)(x)\le\int f\,d\mu_0$. This uses a subnet, not a sequential compactness assumption on $X$ or on its measure space.

When $p_C(f)$ is continuous it belongs to $C$: local continuous competitors approximating it from below have a finite subcover, and their maximum is a uniform approximant in $C$. It belongs to $D$ iff it is continuous, because $D$ is upper semicontinuous and the raw supremum is lower semicontinuous. A maximal $D$ minorant is greatest by taking maxima with arbitrary minorants; it equals the raw supremum. These equivalences show exactly what (6) still needs to prove for the general geometric cone.

## 5. Normal uniform negativity and what it does not settle

Use precisely G331's normal-domain inequality: for each normalized centred divisorial $\nu$ there is $A_\nu>0$, independent of $g\in C$ and $v\in X$, such that $g(\nu)\ge A_\nu g(v)$. Its source qualifications, nonunit treatment and all-support density are part of the entire grant. If $f\ge0$, zero is a competitor and $p_C(f)=0$. Otherwise $f<0$ on a nonempty open set; divisorial density gives $\nu$ with $f(\nu)<0$. Every competitor satisfies
\[
 g(v)\le g(\nu)/A_\nu\le f(\nu)/A_\nu<0.
\]
Taking the supremum proves $p_C(f)$ is uniformly strictly negative. This does not make it upper semicontinuous and does not prove (6). In particular a mixed-zero nonnormal profile or an increasing energy spike is not a normal continuous-obstacle counterexample. Sections 1--3 transport this exact dichotomy, rather than enlarge it, to excellent normal completions.

Artifacts: P12.3-completion-and-formal-lifting.tex, whole-proof.md, completion-proof.md, independent-review.md, source-application-ledger.md, coverage.md, original-residual.md, scope-and-decision.json, native-notes.json and reports. Rerun from this directory: python retain_and_identify.py; python audit_delivery.py; python finite_checks.py; python assemble_delivery.py; python final_audit.py. No supplied program is executed or imported. Source uncompiled; ROOT retains compiler/acceptance/publication. Execution and hashes do not certify the mathematics.
