# P14.8 v3 — exact reconstruction dichotomy

Let $X$ be a connected compact Kähler manifold, and let $\theta$ be a smooth
closed real $(1,1)$-form such that $\operatorname{PSH}(X,\theta)\ne\varnothing$.
Write

$$
\mathscr D_{\mathcal I}(X,\theta)
:=\operatorname{PSH}(X,\theta)/{\sim_{\mathcal I}}
$$

for the set of *realizable* $\mathcal I$-data. Thus an element is induced by
an actual $\varphi\in\operatorname{PSH}(X,\theta)$ and is represented by the
tower $(\mathcal I(m\varphi))_{m\ge1}$, equivalently by its divisorial Lelong
profile; it is not an arbitrary formal sequence of ideals. For
$d=[\varphi]_{\mathcal I}$, define

$$
\mathcal R_\theta(d):=P_\theta[\varphi]_{\mathcal I}.
$$

**Theorem (P14.8 v3).**

1. The map $\mathcal R_\theta$ is well defined and returns the unique
   normalized $\mathcal I$-model potential in the class $d$. Hence full
   realizable $\mathcal I$-data reconstructs its canonical normalized
   $\mathcal I$-model representative, with no hypothesis on nonpluripolar
   mass.

2. Raw nonpluripolar mass is not part of $\mathcal I$-data. On
   $X=\mathbf P^1$, equipped with the Fubini--Study form $\omega$ normalized
   by $\int_X\omega=1$, there is one $\mathcal I$-class containing potentials
   $\varphi_s$, $0\le s\le1$, such that

   $$
   [\varphi_s]_{\mathcal I}=[0]_{\mathcal I},\qquad
   \int_X\left\langle\omega+\operatorname{dd}^c\varphi_s\right\rangle=1-s.
   $$

   In particular, the raw zero-mass representative $\varphi_1$ has canonical
   normalized $\mathcal I$-model representative $0$, whose mass is one. So
   neither a raw zero-mass representative nor its mass can be reconstructed
   from its $\mathcal I$-class.

These settle the two defined readings of the former P14.8 wording: complete
realizable $\mathcal I$-data determines the canonical normalized
$\mathcal I$-model representative, while neither a raw representative nor
its raw mass descends to the $\mathcal I$-quotient.

**Scope.** On a smooth projective variety, the separate all-mass order
isomorphism for full realized DXZ--Boucksom--Jonsson objects in a
pseudoeffective real Néron--Severi class remains distinct. The literal
all-semivaluation ideal formula is used only for a $\mathbf Q$-line-bundle
class. This theorem asserts neither a compact-Kähler nor a genuinely
transcendental extension of that result. Realization of arbitrary formal
ideal or valuative data remains P14.1, and the P14.7 terminal-left-limit
corollary is not used here.
