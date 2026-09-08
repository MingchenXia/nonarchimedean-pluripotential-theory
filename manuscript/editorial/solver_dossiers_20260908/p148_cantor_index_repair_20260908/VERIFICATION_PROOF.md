# P14.8 v3 — proof

Fix $d=[\varphi]_{\mathcal I}$, and set

$$
\mathcal F_d:=\{\psi\in\operatorname{PSH}(X,\theta):
  \psi\le0,\ [\psi]_{\mathcal I}=d\}.
$$

The family is nonempty, since $\varphi-\sup_X\varphi\in\mathcal F_d$. It is
directed under finite maxima: for every prime divisor $E$ over $X$,

$$
\nu(\max\{\psi_1,\psi_2\},E)=
\min\{\nu(\psi_1,E),\nu(\psi_2,E)\},
$$

and the maximum of two members therefore has the same divisorial profile
$d$.

Put $U=(\sup_{\psi\in\mathcal F_d}\psi)^*$. Choquet reduction and the
increasing-supremum formula yield

$$
\nu(U,E)=\inf_{\psi\in\mathcal F_d}\nu(\psi,E)=\nu(d,E)
$$

for each prime divisor $E$ over $X$. Strong openness together with the
valuative characterization of multiplier ideals gives
$[U]_{\mathcal I}=d$. As $U\le0$, this shows $U\in\mathcal F_d$, so it is the
largest element of that family. The family depends only on $d$, hence
$U=\mathcal R_\theta(d)$; repeating the construction with $U$ returns $U$,
and the map is well defined.

Moreover $\sup_XU=0$: otherwise a sufficiently small positive constant could
be added without changing multiplier ideals, contradicting maximality in
$\mathcal F_d$. If $u$ is a normalized $\mathcal I$-model potential in the
class $d$, its defining competitor family is the same $\mathcal F_d$ and
fixedness gives $u=U$. This proves the first assertion.

For the second assertion, take a compact polar generalized Cantor set
$F\subset\mathbf P^1$ carrying a nonatomic probability measure $\mu$. Set
$\ell_0=1$ and $\ell_m=\exp(-4^m)$ for $m\ge1$. Then

$$
2\ell_1<\ell_0,\qquad
\frac{2\ell_{m+1}}{\ell_m}=2\exp(-3\cdot4^m)<1\quad(m\ge1),
$$

so two child intervals fit at every stage. Give each of the $2^m$ stage-$m$
intervals mass $2^{-m}$. The masses of nested intervals tend to zero, so
$\mu$ has no atoms. The generalized-Cantor capacity criterion applies
because

$$
\sum_{m\ge0}2^{-m}\log\frac1{\ell_m}
=\sum_{m\ge1}2^m=+\infty,
$$

and therefore $F$ is polar.

Let $G_p$ be the normalized Green potential satisfying

$$
\omega+\operatorname{dd}^cG_p=\delta_p,\qquad \sup_XG_p=0,
$$

and define $G_\mu(z):=\int_XG_p(z)\,d\mu(p)$. It is not identically
$-\infty$: at a point outside $F$, positive chordal distance from $F$ gives a
finite uniform lower bound for every integrand. Fubini's theorem gives

$$
\omega+\operatorname{dd}^cG_\mu=\mu.
$$

For $0\le s\le1$, set $\varphi_s=sG_\mu$. Then

$$
\omega+\operatorname{dd}^c\varphi_s=(1-s)\omega+s\mu.
$$

On a Riemann surface, the Lelong number of a positive current at a point is
its atomic mass. Both $\omega$ and $\mu$ are nonatomic, so every Lelong
number of every $\varphi_s$ vanishes. The valuative characterization now
gives $[\varphi_s]_{\mathcal I}=[0]_{\mathcal I}$.

In bidegree one, the nonpluripolar product agrees with the curvature measure
where the potential is locally bounded and charges no pluripolar set.
$G_\mu$ is locally bounded on $X\setminus F$, whereas $F$ is polar. Thus

$$
\mathbf1_{X\setminus F}\left\langle\omega+\operatorname{dd}^c\varphi_s\right\rangle
=\mathbf1_{X\setminus F}\bigl((1-s)\omega+s\mu\bigr)
=(1-s)\mathbf1_{X\setminus F}\omega.
$$

The measure on the left gives $F$ mass zero. The smooth measure $\omega$
also gives $F$ mass zero, since polar subsets of a Riemann surface have zero
area. Consequently

$$
\left\langle\omega+\operatorname{dd}^c\varphi_s\right\rangle=(1-s)\omega,
\qquad
\int_X\left\langle\omega+\operatorname{dd}^c\varphi_s\right\rangle=1-s.
$$

This yields the required family. Applying the first assertion to its common
class gives

$$
\mathcal R_\omega([\varphi_s]_{\mathcal I})
=\mathcal R_\omega([0]_{\mathcal I})=0.
$$

At $s=1$, the input representative has mass zero while its canonical
normalized $\mathcal I$-model has mass one. This proves the claimed
non-reconstruction.
