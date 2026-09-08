# P14.8 v4 — proof

Fix $d=[\varphi]_{\mathcal I}$ and set

$$
\mathcal F_d:=\{\psi\in\operatorname{PSH}(X,\theta):
  \psi\le0,\ [\psi]_{\mathcal I}=d\}.
$$

This family is nonempty, since $\varphi-\sup_X\varphi\in\mathcal F_d$. It is
directed under finite maxima. The source package identifies the full
multiplier-ideal tower with its divisorial profile using the
discrepancy-dependent approximation, and generic Lelong numbers satisfy

$$
\nu(\max\{\psi_1,\psi_2\},E)=
\min\{\nu(\psi_1,E),\nu(\psi_2,E)\}
$$

for every prime divisor $E$ over $X$, so the maximum of two members has the
same divisorial profile $d$.

Put $U=(\sup_{\psi\in\mathcal F_d}\psi)^*$. By Choquet's lemma, choose a
sequence $\psi_j\in\mathcal F_d$ whose upper envelope is $U$, and replace it
by the increasing sequence $u_j=\max\{\psi_1,\ldots,\psi_j\}$. Thus each
$u_j$ has profile $d$ and $u_j\nearrow U$ almost everywhere.

We spell out the generic-divisor passage. Fix a model on which a prime divisor
$E$ occurs. Choose a very general point of $E$ simultaneously for the countable
family of pullbacks of the $u_j$ and for the pullback of $U$. Their generic
Lelong numbers are then their point Lelong numbers at that point. After adding
a smooth local potential, the pullbacks form an increasing sequence of psh
functions. The increasing-sequence Lelong theorem therefore gives

$$
\nu(U,E)=\lim_{j\to\infty}\nu(u_j,E)=\nu(d,E).
$$

The valuative multiplier-ideal criterion, applied after every positive integer
scaling, now gives $[U]_{\mathcal I}=d$. Hence $U\in\mathcal F_d$, and it is
the largest member of that family. The family depends only on $d$, so
$U=\mathcal R_\theta(d)$ and applying the construction again returns $U$.

Also $\sup_XU=0$: otherwise a sufficiently small positive constant could be
added without changing multiplier ideals, contradicting maximality in
$\mathcal F_d$. If $u$ is any normalized $\mathcal I$-model potential in the
class $d$, its defining competitor family is the same $\mathcal F_d$, and
fixedness gives $u=U$. This proves the first assertion.

For the second assertion, choose a compact generalized Cantor set
$F\subset\mathbf P^1$ with stage lengths $\ell_0=1$ and
$\ell_m=\exp(-4^m)$ for $m\ge1$. Since

$$
2\ell_1<\ell_0,\qquad
\frac{2\ell_{m+1}}{\ell_m}=2\exp(-3\cdot4^m)<1\quad(m\ge1),
$$

two child intervals fit at every stage. Give each stage-$m$ interval mass
$2^{-m}$. The resulting probability measure $\mu$ is nonatomic, and the
classical generalized-Cantor capacity criterion gives that $F$ is polar because

$$
\sum_{m\ge0}2^{-m}\log\frac1{\ell_m}
=\sum_{m\ge1}2^m=+\infty.
$$

Let $G_p$ be the normalized Green potential on $\mathbf P^1$ satisfying

$$
\omega+\operatorname{dd}^cG_p=\delta_p,\qquad \sup_XG_p=0,
$$

and put $G_\mu(z)=\int_XG_p(z)\,d\mu(p)$. It is not identically
$-\infty$: a point outside $F$ has positive chordal distance from $F$, which
gives a finite uniform lower bound for all integrands. Fubini's theorem yields

$$
\omega+\operatorname{dd}^cG_\mu=\mu.
$$

For $0\le s\le1$, let $\varphi_s=sG_\mu$. Then

$$
\omega+\operatorname{dd}^c\varphi_s=(1-s)\omega+s\mu.
$$

On a Riemann surface, the Lelong number of a positive $(1,1)$-current at a
point is its atomic mass. Both $\omega$ and $\mu$ are nonatomic, so all Lelong
numbers of $\varphi_s$ vanish. Since the prime divisors over a smooth curve are
its points, the valuative multiplier-ideal criterion applied to $m\varphi_s$
gives $\mathcal I(m\varphi_s)=\mathcal O_X$ for every $m\ge1$. Hence
$[\varphi_s]_{\mathcal I}=[0]_{\mathcal I}$.

The degree-one nonpluripolar product is local where the potential is locally
bounded and charges no pluripolar set. $G_\mu$ is locally bounded on
$X\setminus F$. Hence

$$
\mathbf1_{X\setminus F}\left\langle
  \omega+\operatorname{dd}^c\varphi_s\right\rangle
=(1-s)\mathbf1_{X\setminus F}\omega.
$$

The nonpluripolar product gives $F$ zero mass, and so does the smooth measure
$\omega$. Therefore

$$
\left\langle\omega+\operatorname{dd}^c\varphi_s\right\rangle=(1-s)\omega,
\qquad
\int_X\left\langle\omega+\operatorname{dd}^c\varphi_s\right\rangle=1-s.
$$

Applying the first assertion to their common class gives

$$
\mathcal R_\omega([\varphi_s]_{\mathcal I})
=\mathcal R_\omega([0]_{\mathcal I})=0.
$$

At $s=1$, the input representative has mass zero while its canonical
normalized $\mathcal I$-model has mass one. This proves the claimed
non-reconstruction.
