---
title: Two-sign ordinary smooth psh regularization on actual analytic curves
author: Unverified research draft; author audit only
date: 3 October 2026
geometry: margin=1in
fontsize: 10pt
---

# Statement, conventions, and review boundary

This packet claims Theorem R16 (the new two-sign ordinary-smooth psh
regularization gate on every original pure analytic curve, after one completed
algebraic closure), Bridge H16, and Theorem E16 (ordinary-current ascent under
every complete analytic extension on those curves). The detailed statements
and proofs follow the independently exposed transport and recognition bodies.
The original arbitrary-dimensional P06.2 remains open; P05.2 is not addressed.
The status is partial and candidate=false. No earlier review or production
receipt, no hash, and no predecessor native note grants a theorem here.

All equations use ordinary analytic Chambert--Loir--Ducros forms on ordinary
topological opens. Write D=d'd''. On a pure curve the actual equation is

\[
 D[h](\psi)=\int h(D\psi)_{\mathrm{Rad}}=0
 \quad(\psi\in A_c^{0,0}),
\]

where the smooth top-form measure carries the actual generic Artinian
lengths, including nilpotents. The unknown Hessian itself is not presumed
a Radon measure. Finite, continuous, real-valued functions are used
throughout. Ordinary smoothness means Euclidean smooth coefficients of
analytic-unit tropicalizations, not harmonic tropicalizations. G-local real
PL, weak smoothness and ordinary smoothness are not identified.

The source versions are CLD arXiv:1204.6277v2 (25 July 2025),
GR arXiv:2506.13548v2 (17 September 2025),
GJR arXiv:2111.05741v3 (7 March 2025), Wanner arXiv:1801.04713v3,
Thuillier HAL tel-00010990v1, van der Put AIF 30(4) (1980), and
Berkovich PMIHES 78 (1993). These installed sources and their proof bodies
are reproduced below. Standard affinoid algebra, faithful scalar base change,
semistable curve reduction, the strict Nullstellensatz and curve
Riemann--Roch/Serre duality are stated precisely where applied. Complete
source proof bodies are accessible in this same document; their remaining
standard foundational citations do not become an independent proof of those
foundations. The author audit records this review boundary explicitly.

The supplied assignment, ch72, appM and the two-gate statement specify the
task's scope. They are mathematical data, not theorem grants. The monotone
book packet was read in full, including its residual divisor, fresh-cap and
tail-shift steps. R3--R7 reconstruct those steps for already harmonic
functions, and supply the new ordinary-local singular/nilpotent extension.
They do not invoke the book's whole regularization theorem or its acceptance.
In particular its general decreasing-net approximation and Wanner's reverse
test-class bridge are unnecessary for this zero-current two-sign gate.

The fallible prior transport/recognition bodies T and C are reproduced here
in full for the operations actually used; their source passages have been
rebound by newline-only extraction. T handles finite separable differentiated
approximation, wild averaging, inseparability, mixed stages and completed
finite-stage scalar-test descent. C handles actual component lengths, rigid
punctures, normalization, actual algebraic-model interiors and the one-way
use of Wanner comparison. R and E are the new proofs. Fullbody reuse is
an exposed argument, not reliance on a previously accepted claim.

# Part T. Completed-algebraic transport: statement

**Transport lemma.** For a good separated strict boundaryless pure
$K$-analytic curve $Z$, an algebraic extension $M/K$ with its extending
absolute value, and $L=\widehat M$, the actual scalar projection satisfies
\[
                  D[u]=0\quad\Longleftrightarrow\quad D[u\circ\pi]=0.
\]
It holds on every ordinary open, with the original lengths. A subsidiary
lemma, not requiring dimension one, is that every compact ordinary smooth
scalar test on $Z_L$ is exactly the pullback of a compact smooth scalar
test on $Z_E$ for some finite embedded $K\subseteq E\subseteq M$.
The following T2--T13 prove these assertions. Equation numbers inside T
are local to this proof; the asserted equivalence is equation (1). All source excerpts referenced there are supplied
in Appendix S; the historical misselected Section 15 blocks are excluded.


For a finite Galois stage the approximation assertion proved below is that an
invariant compact ordinary scalar test $\beta$ has downstairs compact smooth
approximants $\alpha_j$ supported in one compact $H$, with all errors supported
in $\pi^{-1}H$, such that
\[
 \big\|(D(\beta-\pi^*\alpha_j))_{\mathrm{Rad}}\big\|_{\mathrm{TV}}\to0.\tag{2}
\]
Set
\[
 B_u(\psi)=\int_Zu(D\psi)_{\mathrm{Rad}}.\tag{3}
\]
Equation (1) denotes the equivalence in the transport lemma, while (2) and
(3) are local equation labels for T. The proof handles finite separable,
finite inseparable, mixed embedded finite stages, then the completion.

## T2. Exact analytic dependencies and source checks

CLD refers to Chambert-Loir--Ducros, *Formes différentielles réelles et
courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025.
GR refers to Gubler--Rabinoff, *Classically psh and pluriharmonic functions
on Berkovich spaces*, arXiv:2506.13548v2, 17 September 2025. Numbering is
that of these cached primary snapshots, whose statements and proof
bodies, not just the former drafts' descriptions, were inspected.

1. **Affinoid foundations.** CLD 11.1.1--2: an affinoid spectrum is
   compact Hausdorff; its algebra is noetherian with closed ideals; the
   map to its prime spectrum is surjective. CLD 11.1.5: every point of
   an affinoid has rational affinoid neighbourhoods inside any prescribed
   ordinary open, with the point satisfying all associated strict
   inequalities. Rational systems have positive real radii and
   denominator/numerators with no common zero (T12 uses this
   stronger neighbourhood clause of 11.1.5). CLD 11.1.7--8: a good space has an affinoid
   neighbourhood basis; ordinary opens are analytic domains; analytic
   sections form a sheaf also for ordinary opens, and
   $\mathcal O(\mathcal M(A))=A$. CLD 11.1.9: affinoid fibre products
   and scalar extensions use completed tensor products, and scalar
   projection is surjective. CLD 11.4.4: a finite algebra with its
   finite-module Banach topology is affinoid. CLD 11.7.7: over a
   nontrivially valued field, every point of a good strict space has a
   strict affinoid neighbourhood. Applying this to ordinary opens
   gives such a neighbourhood inside the open. Particular tensor,
   orbit, compactness, shrinking and unit claims are proved in T3.

2. **Dimension and boundary.** CLD 11.2.2: separated analytic spaces
   are topologically separated. CLD 11.2.3: strict affinoid dimension
   is Krull dimension, dimension is preserved by complete scalar
   extension, and domains preserve local analytic dimension. If the
   minimal-prime components of $\mathcal M(A)$ are $X_i$, then
   $\dim_xX=\sup_{x\in X_i}\dim X_i$. Pure dimension means constant
   local dimension. GR 2.11(5), equivalently (5'), states for a morphism
   $Y\to Z$ and any analytic extension $L/K$ that
   $\partial(Y_L/Z_L)\subseteq\pi^{-1}(\partial(Y/Z))$.
   Hence a boundaryless space remains boundaryless. GR 2.11(3),(4)
   gives boundarylessness for an ordinary open in a boundaryless space:
   its relative interior is its ordinary topological interior and
   interiors compose. T3 proves purity component by component;
   equality of total dimensions alone is not the proof.

3. **Ordinary forms.** CLD Corollary 15.1.2 states that a function is
   smooth near $x$ if it has a representation
   $\varphi(t_{f_1},\ldots,t_{f_m})$ on a neighbourhood of $x$, where
   the $f_i$ are analytic units and $\varphi$ is smooth on a Euclidean
   neighbourhood of the coordinate value. CLD Proposition 15.1.1(b)
   gives ordinary open moment descriptions for forms in every
   bidegree. CLD 6.2.1--2 defines ordinary forms and says they form an
   ordinary sheaf stable under wedge, $J,d',d''$. Moment pullback
   commutes with the exterior calculus (CLD 3.3.12). In a moment a
   logarithm is an affine coordinate, so $Dt_f=0$ as a **form**.
   CLD 3.4.4: for a G-tropical chart $f$ and a coefficient form $a$,
   its pullback is zero in the G-form sheaf exactly when $a$ restricts
   to zero on $f(V)$ for every compact domain $V$. This identifies the
   ordinary form sheaves when the analytic units, domains and moment
   images are the same; it is not descent through scalar projection.

4. **Compact cutoffs only.** CLD 15.2.2: a good topologically
   separated space is locally holomorphically separated. CLD
   Corollary 15.2.5: on a locally holomorphically separated analytic
   space, for any compact $F$ and ordinary open neighbourhood $U$ of
   $F$, there is an ordinary smooth function equal to one near $F$
   with compact support contained in $U$. Its proof uses local
   differential separation (15.2.4) and the smooth bump result 6.2.4.
   T4 constructs the only partition statement needed, for
   compact $F$ and finite covers. The overbroad fixed-index
   countable-at-infinity reading of CLD 15.2.9 is not used.

5. **Canonical top measures.** CLD Theorem 15.7.1: a pure
   $n$-dimensional topologically separated analytic space with its
   canonical calibration and analytic boundary is a tropical space of
   level $n$. CLD 15.7.2: the induced structure on a domain agrees
   with that domain's analytic structure. CLD 5.4.4: every compact
   tropical chart is pleasant, and its tropical polyhedron is the
   top-dimensional part of its compact moment image. CLD
   14.3.2--5, 14.5.1--2: canonical calibrations are standard and
   positive, and on a top moment cell $Q$ the calibration is
   $d_Q\tau_{Q,*}|e_1\wedge\cdots\wedge e_n|$, where $\tau_Q$
   is the affine inverse of an injective torus projection and $d_Q$
   is the sum of the actual finite-flat degrees of the skeletal
   cells above $Q$. Those degrees retain fibre-algebra dimensions,
   including lengths. CLD 5.8.3--5 constructs a top form's measure by
   contraction on its supporting skeleton. CLD Proposition
   5.10.1(c,d): for a pleasant chart $f$ and a Borel $(n,n)$
   coefficient form $a$, the induced measure is locally finite
   exactly when $a$ is locally integrable on the calibrated tropical
   polyhedron, and then
   $f_*((f^*a)_{\mathrm{Rad}})=\langle a,\mu_{\Pi_f}\rangle_{\mathrm{Rad}}$;
   the corresponding integrals agree. In particular a smooth top
   form is finite on a compact moment domain. Lower-dimensional
   cells have no top measure. Compact moment images are finite
   polyhedra by the polyhedrality assertion of CLD Theorem 12.2.4.
   The dimension bound is specifically CLD 12.2.10(1)--(2):
   $\dim_{\mathrm{trop},x}f\le d_K(x)\le\dim_xX$ and, for compact
   $X$, $\dim f_{\mathrm{trop}}(X)=\sup_x\dim_{\mathrm{trop},x}f$.
   Thus compact curve images have dimension at most one. We do not
   use a claim that a moment image always has dimension equal to its
   source; constant moments rule out that reading. CLD 7.3.5 defines integration currents
   for locally integrable multipliers; a continuous finite multiplier
   is locally integrable. T8 proves the carrier total-variation
   estimate needed here, before any possibly cancelling signed
   pushforward.

6. **Scalar projection has no field-degree factor.** CLD
   Proposition 14.3.6: on a level-$n$ analytic space, if $\Sigma$
   has canonical calibration $\mu$ and $\Sigma_L$ its scalar extension
   has canonical calibration $\mu_L$, then $\pi_*\mu_L=\mu$.
   CLD Proposition 15.3.1: for a tropically Borel $(n,n)$ G-form
   $\omega$, $\pi_*\omega_{L,\mathrm{Bor}}=\omega_{\mathrm{Bor}}$;
   for a locally integrable such form,
   \[
              \pi_*\omega_{L,\mathrm{Rad}}
                        =\omega_{\mathrm{Rad}}.          \tag{4}
   \]
   Here is the primary proof mechanism, retaining its lengths.
   On a convenient skeletal cell choose a torus projection injective
   on the cell. Its finite-flat degree downstairs equals the sum of
   its degrees at all upstairs skeletal lifts. This is CLD Lemma
   13.3.3(a): degrees at $y$ equal the sum of degrees over $y$ after
   complete base change and choice of a target lift. The lemma reduces
   to a fibre; a zero-dimensional local fibre algebra is Artinian,
   and its tensor decomposes into its local Artinian factors. The sum
   of their dimensions is the original dimension after scalar
   extension. Positive-dimensional fibres give infinite degrees on
   both sides. Thus the cell volume vectors sum to the downstairs
   vector, proving 14.3.6. Contracting the form and taking Radon
   measures proves 15.3.1. We apply (4) only to smooth top forms,
   then pair with $h$; this never assumes pullback of a continuous
   current.

7. **Same-carrier field restriction has a degree factor.** CLD Remark
   14.4.3: for a finite extension $F/K$, an $F$-analytic space $Z$
   of level $n$, and its restricted $K$ structure $Z_0$, dimensions
   and skeletal subsets agree and
   $\mu_{Z_0}=[F:K]\mu_Z$. The proof uses the finite-flat degree
   $[F:K]$ of the projection of the split torus on this restricted
   carrier. CLD 15.4.1 and Proposition 15.4.3: for a morphism
   $f:Y\to Z$ of level-$n$ spaces finite off a Zariski closed set of
   dimension $<n$, a locally integrable $(p,n)$ G-form $\omega$,
   $p\in\{n-1,n\}$, has locally integrable pullback and
   $f_*((f^*\omega)_{\mathrm{Rad}})=\mathrm{dc}(f)\omega_{\mathrm{Rad}}$.
   Its proof first proves the calibrated volume-vector identity on
   the inverse skeletal set (14.4.2), then contracts and integrates.
   We use only an actual isomorphism on $Z_0$, whose calibrated
   degree is one: both local Artinian rings are identical. Cancelling
   the same-carrier factor $[F:K]$ proves invariance over $F$.

The stated calibration and form statements apply to the actual, potentially singular
and nonreduced structure. They require no normalization and no
quasi-smoothness. No weakly smooth GJR descent, positive-current
recognition, or catalogue theorem is used as an ordinary form theorem.

### T2.1. Direct proofs of the neighbourhood and compact-cutoff facts used here

The finite proof uses the primary foundations above. For the two
topological localization facts decisive at completion, the following
direct constructions supply their proof bodies as well.

On $\mathcal M(A)$ the ordinary topology is initial for all
evaluations $|a|$ (CLD 11.1.1). A prescribed neighbourhood of a point
therefore contains a finite intersection of conditions
$|a_j|>\ell_j>0$ and $|b_k|<u_k$, where thresholds can be chosen
strictly between the point's value and the excluded endpoint.
Missing lower or upper bounds impose no condition. Put
$g=\prod_j a_j$, with $g=1$ when there are no lower bounds. Choose
$C>0$ so that $C^{-1}<\prod_j\ell_j$. The rational conjunction
\[
 |1|\le C|g|,\qquad
 |\prod_{j'\ne j}a_{j'}|\le\ell_j^{-1}|g|\ (\forall j),\qquad
 |b_kg|\le u_k|g|\ (\forall k)                         \tag{R}
\]
has no common zero among its denominator and numerators, because
one numerator is $1$. It is a rational analytic domain by the
universal rational-domain construction of CLD 11.1.5. Its validity
locus lies in the originally prescribed neighbourhood if the
thresholds were chosen inside that neighbourhood's intervals:
its first inequality excludes $g=0$, so division of norms gives
all chosen lower and upper bounds. The original point satisfies
every strict inequality, including the first. Non-strict thresholds
in (R) were chosen inside the original open intervals, so validity
of the weak system suffices for containment. This proves the strong
rational-neighbourhood clause needed in T12 using the initial
topology and the rational-domain construction. Real positive
thresholds suffice even when the value group is discrete.

Here is also a direct compact-cutoff construction in every good
Hausdorff analytic space occurring in the proof. For a point $x$ in
an ordinary open $U$, take an affinoid neighbourhood $V_0$ and
within its ordinary interior a rational neighbourhood $R$ of $x$
contained in $U$, with strict inequalities
$|f_i(x)|<r_i|g(x)|$. Its denominator satisfies $g(x)\ne0$.
Choose $b_i$ with $|f_i(x)|/|g(x)|<b_i<r_i$ and choose
$0<a<|g(x)|$. On the ordinary nonzero locus of $g$ in $V_0$, a
smooth function of $\log|g|$ equals one near $x$ and vanishes
where $|g|\le a$. For each $i$, choose a smooth real function of
$\log|f_i/g|$ that is one when $|f_i/g|\le b_i$ and zero when
$|f_i/g|\ge r_i'$ for some $b_i<r_i'<r_i$. Extend that factor
as the constant one at zeros of $f_i$: near such a zero its ratio
is below $b_i$, so the extension is locally constant and ordinary
smooth. On its nonzero locus the ratio is an analytic unit, giving
the required ordinary moment description. Multiply the factors
with the denominator cutoff. At points where $g=0$, extend by
zero; the denominator cutoff already vanishes on a neighbourhood
of each such point.

The support of this product lies in the compact set in $V_0$
defined by $|g|\ge a$ and $|f_i|\le r_i'|g|$ for all $i$.
That compact set lies in the strict locus of $R$, hence in
$U\cap\operatorname{int}_X(V_0)$. Extend the product by zero
outside $V_0$: every point outside the compact support has a zero
neighbourhood, so the extension is ordinary smooth. It equals one
near $x$. Taking squares gives nonnegative cutoffs. For compact
$F\subset U$, finitely many positive loci of these point cutoffs
cover $F$. Their sum $s$ is positive near $F$. Compose with a
real smooth function that vanishes near zero and equals one on a
neighbourhood of the compact positive set $s(F)$. This gives a
compact cutoff equal to one near $F$ and supported in $U$.
This reconstructs the compact CLD 15.2.5 conclusion in our actual
good Hausdorff scope. T4 then proves its finite-cover
partition specialization. No countable-at-infinity fixed-index
compact-support assertion is used.

In particular all cutoffs are obtained from ordinary analytic-unit
moments, flat constant extensions near analytic zeros and compact
extension by zero. No weakly smooth tropicalization is substituted.


## T3. Finite fields, fibres, analytic structures, and purity

We first treat a finite Galois extension $E/K$, with group $G$ and
$d=[E:K]=|G|$. The elementary finite field facts used below can be
justified as follows. A finite separable extension has as many distinct
embeddings in an algebraic closure as its degree: extend embeddings
successively by the distinct roots of each separable minimal polynomial.
The field $K$ is infinite. For two separable generators $u,v$, all but
finitely many $c\in K$ make the values of $u+cv$ distinct for every
pair of distinct embeddings; if their $v$ values agree their $u$ values
already differ. Its minimal polynomial then has at least as many roots
as the extension degree, so $u+cv$ generates the extension. Induction
gives a primitive element. The splitting field of its separable minimal
polynomial is finite separable. Every embedding of this splitting field
permutes the roots and is onto, so it is Galois and its automorphism
group has its degree as order. Its fixed field is $K$: the embeddings
of any intermediate separable simple field extend successively to the
splitting field, so a fixed element has a minimal polynomial of degree
one. This also provides the normal closure used in T10.

Finite-dimensional norms over a complete non-Archimedean field are
equivalent to the coefficient maximum norm in a fixed basis. Here is a
proof. Induct on dimension. The span of all but the last vector is
complete by induction, hence closed. The last vector has positive
distance from this span, bounding its coefficient in any combination.
The ultrametric inequality and induction then bound all other
coefficients. The reverse bound is the triangle inequality. Consequently
finite-dimensional normed spaces are complete and their coordinate
maps bounded. Existence of an absolute value on a finite field extension
can also be seen by giving the finite algebra its finite-module Banach
topology, using CLD 11.4.4, and taking a point of its nonempty affinoid
spectrum. Its kernel is zero since the algebra is a field. Uniqueness
follows from norm equivalence: compare two extending norms on $z^m$
and take $m$th roots. Hence all finite field automorphisms preserve the
absolute value, and every finite field here is complete.

For a $K$-affinoid algebra $A$, tensor the bounded coordinate maps of
$E$ with $A$. The tensor norm upper bound and these coordinate maps
identify its topology with a finite sum of copies of $A$. Already
complete, this proves
\[
             B=A\widehat\otimes_K E=A\otimes_K E.        \tag{5}
\]
This is the actual algebra, including nilpotents. Taking the kernel of
$E\to\bigoplus_{g\in G}E$, $z\mapsto(gz-z)_g$, and tensoring over
the field gives $B^G=A$. Invariant units descend as units since their
inverses are invariant too. There is no field averaging or division by
$d$. An affinoid element nonzero at every analytic point is a unit:
otherwise a maximal ideal containing it and spectral surjectivity give
a zero.

The fibre over $x$ is
$\mathcal M(\mathcal H(x)\otimes_K E)$. A primitive separable
polynomial factors without repeated factors over $\mathcal H(x)$, so
the tensor is a finite product of fields. Each has one analytic point
by the existence and uniqueness argument above. The $G$ action on
these finitely many points is transitive: two orbits would supply a
nontrivial invariant idempotent, but the invariant algebra is
$\mathcal H(x)$. Stabilizers can be nontrivial; no local covering-space
description is claimed or used.

Inverse images of affinoid ordinary interiors give goodness upstairs.
Strict presentations base change to strict presentations. Base change
of the closed diagonal gives separatedness. Boundarylessness follows
from T2(2). In particular all carriers are Hausdorff. The inverse
image of any compact $F\subset X$ is compact: cover $F$ by finitely
many interiors of affinoid neighbourhoods $V_i$; its inverse image is
closed in the finite union of the compact $V_{i,E}$.

**Full-fibre shrinking.** In a downstairs strict affinoid neighbourhood
$V_0$ of $x$, let $N\subset V_{0,E}$ be a relative ordinary open
containing the whole fibre. The compact complement has closed image
excluding $x$. Choose a smaller strict affinoid neighbourhood $V$ of
$x$ in the complement of that image and inside
$\operatorname{int}_X(V_0)$. Then $V_E\subset N$. Thus finitely many
unit or strict norm conditions holding on the whole fibre persist on
one neighbourhood. This includes conditions on elements of zero
seminorm at $x$ and never replaces $A$ by its reduction.

For completeness, purity is checked at minimal components. In a strict
affinoid $\mathcal M(A)$ in $X$, each minimal-prime component has
dimension one: choose a point with kernel that prime by spectral
surjectivity and apply the local dimension formula. Let $J$ be the
nilradical. It is nilpotent since $A$ is noetherian. The injection
$A/J\hookrightarrow\prod_P\operatorname{Frac}(A/P)$ stays injective
after tensoring with a separable field. Each field tensor is a product
of fields, hence $(A/J)\otimes E$ is reduced and the nilradical of
$B$ is exactly $J\otimes E$. The finitely many kernels of its maps
to those field factors have zero intersection. Their product is zero,
so a minimal prime contains one of these kernels, and by minimality
equals it. Its contraction is the corresponding minimal $P$ of $A$.
The finite integral injection $A/P\hookrightarrow B/Q$ preserves Krull
dimension. One elementary justification is lying over and going up
from the determinant argument for a finite module over a local ring:
$\mathfrak pD_{\mathfrak p}\ne D_{\mathfrak p}$, since otherwise
the determinant of $I-M$, $M$ with entries in $\mathfrak p$, is a
unit annihilating that nonzero module. Choose a maximal ideal above it
and then repeat after quotienting by a chosen prime. For
incomparability quotient by the smaller prime and invert the nonzero
elements of the base domain. The resulting finite integral domain over
a field is a field, since a least-degree monic equation for a nonzero
element expresses its inverse. A strictly larger prime of the same
contraction could not survive, nor could a nonzero element of a domain
vanish under that localization. Going up lifts chains and
incomparability makes contractions strict. The dimensions agree.
Every minimal component upstairs therefore has dimension one, proving
purity. The same proof works for any finite separable stage. Reduction
here is a dimension check only; all measures below use $B$ itself.

Finally consider the same carrier $Z=X_E$ with its restricted
$K$-analytic structure $Z_0$. A finite $E/K$ is $K$-affinoid; an
$E$-affinoid presentation is therefore $K$-affinoid under finite field
restriction. The finite-module topology is unchanged. Rational domains
are defined by the same elements and inequalities and have the same
analytic rings. They give a common local basis and the same unit germs
and compact moment images. The moment nullity criterion of Section
2(3) identifies the ordinary form sheaves, their exterior calculus and
supports. Each $g\in G$ is a bounded $K$-algebra automorphism of (5),
gluing to a $K$-analytic automorphism of $Z_0$. Its isomorphism
pushforward formula, followed by cancellation of the same-carrier
factor $d$, gives for a smooth compact top form $\omega$
\[
             g_*((g^*\omega)_{\mathrm{Rad},E})
                            =\omega_{\mathrm{Rad},E}.    \tag{6}
\]
This is different from (4). Both are valid with actual generic lengths.

## T4. Compact partitions and full-fibre scalar descriptions

Let compact $F$ have an ordinary open cover. At every point of $F$,
apply T2(4)'s bump theorem to the singleton in a chosen cover
member. Squaring the bump makes it nonnegative, still equal to one
near that point and compactly supported there. Select finitely many
whose positive loci cover $F$, and group them by cover index as
$\psi_i$. Then $s=\sum_i\psi_i>0$ near $F$. Take a bump $\chi=1$
near $F$ compactly supported in $\{s>0\}$ and put
\[
                \theta_i=\chi\psi_i/s                  \tag{7}
\]
there, extending by zero. Products, smooth composition, and reciprocal
on $s>0$ are ordinary smooth operations in moment coordinates. The
compact support of $\chi$ lies inside $\{s>0\}$, so extension by
zero is smooth also at its complement. Each support is compact and
contained in its cover member. The sum is one near $F$. This proves
the needed finite compact partition without any noncompact
fixed-cover-index assertion.

Let $\beta$ be an invariant ordinary smooth scalar function near a
whole fibre over $x$. Its fibre has finitely many points. Choose
pairwise disjoint ordinary neighbourhoods $N_i$ of them with local
representations $\beta=\varphi_i(t_{f_{i,1}},\ldots)$, using Corollary
15.1.2. Shrink $N_i$ so the coordinate values are in a relatively
compact Euclidean region on which $\varphi_i$ is smooth. Full-fibre
shrinking gives a strict affinoid $V$ with $V_E\subset\bigcup_iN_i$.
The pieces $C_i=V_E\cap N_i$ are disjoint ordinary opens and closed
in $V_E$. They are compact. Analytic gluing gives idempotents $e_i$
which are one on $C_i$ and zero on the other pieces, and gives a global
unit $\widetilde f_{i,k}$ equal to $f_{i,k}$ on $C_i$ and one elsewhere.
Its inverse glues in the same way. These are elements of the actual
affinoid algebra $B$, not formal topological selectors.

Choose $a\in K^\times$ with $|a|\ne1$. The analytic unit
$s_i=e_i+a(1-e_i)$ has $t_{s_i}=0$ on $C_i$ and
$t_{s_i}=-\log|a|$ elsewhere. Choose a real smooth $q$ equal to one
near zero and zero near $-\log|a|$. Extend $\varphi_i$ by a Euclidean
cutoff equal to one near its compact coordinate image. Thus
\[
 \beta=\sum_i q(t_{s_i})\varphi_i(t_{\widetilde f_{i,1}},\ldots)
                          =\Phi(T)\quad\text{on }V_E,   \tag{8}
\]
for one global unit tuple $T$ and a Euclidean smooth $\Phi$.
All group translates of these units exist on $V_E$; adjoining them
gives one fixed tuple. The real average
$|G|^{-1}\sum_g\Phi(T\circ g)$ equals $\beta$ there. This construction
works for every orbit and stabilizer, including singleton fibres. It
does not assume exact invariant ordinary scalar descent.

## T5. Polarization removes the orbit-correlation difficulty

For a smooth Euclidean function on a neighbourhood of a compact box,
there are real polynomials converging through order two on that box.
Here is a proof of precisely the version used. Extend it by a compact
Euclidean cutoff, convolve with a Gaussian, and differentiate under the
integral. Uniform continuity of the derivatives through order two and
the Gaussian tail give uniform derivative convergence on the box. For
fixed convolution width, the Gaussian and its first two derivatives
are uniform limits of their Taylor polynomials on the compact
difference of the box and the original coefficient support. Integrate
these polynomials to get polynomial approximants through order two,
then choose widths and truncation degrees diagonally.

For $k\ge1$ and real symbols $z_1,\ldots,z_k$, including repeated
symbols, inclusion-exclusion and the multinomial expansion give
\[
 z_1\cdots z_k=\frac1{k!}\sum_{J\subseteq\{1,\ldots,k\}}
            (-1)^{k-|J|}\left(\sum_{j\in J}z_j\right)^k. \tag{9}
\]
Indeed each term missing one symbol cancels, and the only surviving
degree-$k$ term containing every symbol is their product with
coefficient $k!$. For unit logarithms, a sum is the logarithm of the
corresponding product unit. Consequently the real group average of
**every** scalar polynomial in an arbitrary tuple of unit logarithms
is a finite real linear combination of constants and terms
\[
        T_{f,k}=\frac1d\sum_{g\in G}t_{gf}^{k},          \tag{10}
\]
with actual product units $f$. This recovers mixed orbit correlations;
no claim that separate symmetric sums for the original individual
units suffice is used. The number of product units may grow with
polynomial degree. T9 handles this explicitly; no common
neighbourhood for infinitely many product units is assumed.

## T6. Actual root valuations and all coefficient-zero cases

For a unit $f\in B^\times$ set
\[
 P_f(Z)=\prod_{g\in G}(Z-gf)
             =Z^d+\sum_{i=0}^{d-1}c_iZ^i.               \tag{11}
\]
Its coefficients lie in $B^G=A$; $c_0$ is a unit. At an analytic
point $y$, the roots $gf(y)$ are actual nonzero elements of
$\mathcal H(y)$ with multiplicities indexed by **all** group elements.
This includes repeated roots and arbitrary stabilizers. Neither a
separable orbit polynomial nor characteristic-zero coefficients are
required.

We prove the root-valuation rule rather than importing Newton-polygon
recognition. For a polynomial $\prod_{j=1}^d(Z-r_j)$ over any valued
field with nonzero roots, sort $u_j=-\log|r_j|$ in nondecreasing order.
The coefficient of $Z^{d-k}$ is a sum of products of $k$ roots.
Every summand has valuation at least $u_1+\cdots+u_k$, so its
coefficient has valuation at least that number, allowing infinity.
If $u_k<u_{k+1}$, the subset of the $k$ roots of smallest valuation
is unique and its product has strictly greater norm than every other
summand. Ultrametricity makes the coefficient valuation exactly that
sum. Equality also holds at $k=0,d$. These equality points are
precisely the ends of constant-valuation blocks. The convex polygon
joining them lies below all the coefficient points and has its
successive slopes equal to the root valuations in reversed sign when
indexed by coefficient exponent. Thus the lower convex hull of
\[
          (i,v(c_i))\ (0\le i\le d),\qquad v(c_d)=0      \tag{12}
\]
has each segment $i<j$ contributing $j-i$ roots of valuation
$(v(c_i)-v(c_j))/(j-i)$. Repeated roots, ties, and every cancellation
are covered by the strict-gap argument. No division occurs in the
valued field.

Near a fixed downstairs $x$, choose $M$ so all $|t_{gf}|<M$ on its
finite fibre and retain this inequality by full-fibre shrinking. Then
$|t_{c_0}|<dM$. If $c_i(x)=0$ for $0<i<d$, shrink further until
\[
                      |c_i|<\exp(-dM-1).                \tag{13}
\]
Its valuation lies strictly above the chord from $(0,t_{c_0})$ to
$(d,0)$, since that chord's height is at most $dM$. Hence it cannot
belong to the lower hull and may be omitted. If $c_i(x)\ne0$, shrink
to make it a downstairs unit: choose a strict affinoid neighbourhood
inside its nonzero locus, then use the unit criterion of T3.
Keep $c_0,c_d=1$ in all cases. The retained index set
$I\subseteq\{0,\ldots,d\}$ therefore includes both ends. Its other
coefficients are actual units; all omitted coefficients obey (13)
throughout this neighbourhood. Nilpotent coefficients are included in
the zero-seminorm case. No coefficient with value zero is logarithmed,
and small coefficients are not simply assumed harmless.

## T7. A $C^1$ piecewise polynomial and its tangential mollification

For arbitrary real heights $z_i$, $i\in I$, with $z_d=0$, form the
lower hull of the finitely many points $(i,z_i)$. If consecutive
vertices are $i<j$, put $m=j-i$ and $u=(z_i-z_j)/m$. Define
\[
               H_{I,k}(z)=\sum_{\text{hull segments }i<j}
                                 m\,u^k.                \tag{14}
\]
Collinear vertices may be retained or omitted: (14) is unchanged.
There are finitely many possible hull chains. Each is selected by
linear weak inequalities in the heights, so (14) is a polynomial on
each region of a finite polyhedral subdivision of the whole height
space. Equations (11)--(13) prove at **every** point upstairs that
\[
               T_{f,k}=d^{-1}H_{I,k}(t_{c_i}).            \tag{15}
\]

We need more than continuity of this formula. For a general smooth
one-variable $\phi$, the segment term $m\phi((z_i-z_j)/m)$ has gradient
$\phi'(u)(e_i-e_j)$ and Hessian
\[
            \frac{\phi''(u)}m(e_i-e_j)\otimes(e_i-e_j).  \tag{16}
\]
If a vertex is inserted or deleted on a collinear segment, all the
affected $u$ equal one common value. The gradients then telescope:
$\sum\phi'(u)(e_i-e_j)$ is exactly the gradient of the single merged
segment. This remains true if several vertices are collinear.
At a height configuration on a chamber boundary, every limiting hull
chain refines the unique lower hull by such collinear vertices. Values
and gradients therefore agree for every limiting chamber. A finite
piecewise smooth function with these matching values and gradients is
$C^1$: integrate the matching, continuous candidate gradient on short
line segments subdivided by the finitely many chamber faces; segments
contained in faces follow by a small translation and continuity. The
usual differentiability remainder follows from continuity of that
gradient. Thus (14) is $C^1$.

On any compact neighbourhood, slopes $u$ are bounded. Each Hessian
(16) is bounded by $2\sup|\phi''|/m$ in operator norm; there are at
most $d$ segments. For $\phi(u)=u^k$, there is a finite bound for all
chamber Hessians on that neighbourhood. The gradient is locally
Lipschitz by integrating these Hessians along line segments, using its
continuity at faces as above. The weak Hessian is the bounded
piecewise Hessian, with no singular face measure: integrate by parts
on each polyhedral region; the boundary contributions from the
continuous gradient cancel in pairs. Lower-dimensional intersections
give no additional boundary term. This proves all assertions used in
mollification; bounded third or fourth derivatives are unnecessary.

Choose a nonnegative even $C^\infty$ kernel $\rho$ supported in the
unit ball with integral one. Let $H_\varepsilon=H*\rho_\varepsilon$.
The local gradient Lipschitz bound yields uniformly on fixed compacts
$H_\varepsilon\to H$ and $\nabla H_\varepsilon\to\nabla H$; in fact
the errors are $O(\varepsilon^2)$ and $O(\varepsilon)$. The first
bound follows from the first-order remainder and the kernel's zero
first moment. Its Hessian is the convolution of the weak Hessian and
is uniformly bounded on those compacts.

**Tangential second derivative lemma.** Let an open segment $L$ lie in
the relative interior of a face $F$ of the subdivision of $H$, with
tangent vector $v$ in the affine direction of $F$. At every point
$z\in L$,
\[
        \nabla^2H_\varepsilon(z)(v,v)
                  \longrightarrow (H|_L)''(z;v,v).       \tag{17}
\]
To prove this, only chambers incident to $F$ meet a sufficiently small
ball about $z$. Let their polynomial formulas be $Q_a$. Each agrees
with $H$ on a relatively open neighbourhood in $F$, so
$\nabla^2Q_a(z)(v,v)$ is the same tangential derivative of that
restriction. For points $w$ tending to $z$ through any such chamber,
the corresponding tangential Hessian tends to this common value.
Convolving the bounded, piecewise Hessian proves (17). If the line is
mapped to one point in height space, the tangent is zero and the
statement is immediate. This proof deals with segments **entirely
contained in collision walls**; they are not dismissed as measure
zero. A compact moment segment maps affinely to height space and can
be subdivided at finitely many face preimages, so the conclusion holds
almost everywhere on every such segment, including those of deficient
height-map rank.

## T8. Calibrated differentiated approximation of a fixed trace

Fix $f,k$ and one neighbourhood on which (13)--(15) hold. The
functions
\[
                b_\varepsilon=d^{-1}H_\varepsilon(t_{c_i})
                                                               \tag{18}
\]
are ordinary smooth downstairs, using actual unit moments. On a
compact upstairs domain add to one moment tuple the units $gf$, the
pullbacks of all retained coefficients, and any fixed cutoff's units.
Its image is a finite polyhedral set. Refine its one-dimensional cells
by the height-fan preimages and by a common skeletal calibration
subdivision. On each segment, (15) is an identity of functions of
affine coordinates. Its right side restricts to a polynomial on the
segment, whose first and second tangent derivatives are therefore
those of the ordinary upstairs polynomial $T_{f,k}$.

The errors $e_\varepsilon=T_{f,k}-\pi^*b_\varepsilon$ and their first
derivatives converge uniformly tangentially. Their second tangential
derivatives are uniformly bounded and converge almost everywhere on
every segment by (17). No differentiation of (15) as a nonsmooth
ordinary section is performed; the derivatives are compared on actual
moment cell tangents.

Here is why this is a total-variation statement on the actual carrier.
For the enlarged tuple $t_1,\ldots,t_r$ put
$\zeta=\sum_a d't_a\wedge d''t_a$, with the positive top-order
convention. On a segment with tangent $v$, a coefficient matrix
$A=(A_{ab})$ contracts to $\sum A_{ab}v_av_b$ times its positive
calibration; $\zeta$ contracts to $\sum v_a^2$ times the same
calibration. Hence $|A_{ab}|\le M$ gives
\[
       |\eta_{\mathrm{Rad}}|\le rM\zeta_{\mathrm{Rad}},    \tag{19}
\]
by $\big(\sum|v_a|\big)^2\le r\sum v_a^2$. Equivalently use
bounded tangential coefficients in unit tangent frames on the finitely
many segments. The estimate is made on the supporting skeletal cells
before pushforward. T2(5) gives finite total mass of $\zeta$
on the compact domain and a constant finite positive density on each
moment segment. Thus bounded tangential error converging almost
everywhere has carrier total variation tending to zero by bounded
convergence on those finite calibrated segments. Zero-dimensional
faces carry no top measure. Multiplicities and generic lengths multiply
both sides of (19); none is removed or replaced by a point count.

For any **fixed** ordinary smooth cutoff $\lambda$ supported in the
neighbourhood, the product rule for $D(\lambda e_\varepsilon)$ uses
the scalar error, its two first derivatives, and its mixed second
derivative, together with fixed bounded derivatives of $\lambda$.
The preceding convergence and (19) show
\[
       \big\|(D((\lambda\circ\pi)e_\varepsilon))_{
                          \mathrm{Rad},E}\big\|_{\mathrm{TV}}
                                 \longrightarrow0.       \tag{20}
\]
Cover a fixed compact cutoff support by finitely many compact moment
neighbourhoods to use this argument; their enlarged tuples and
calibration refinements are fixed during this limit. Signed fibre
cancellation is not used to infer (20).

For a fixed finite combination of traces (10), T6--T8 apply near
every downstairs point, with finitely many units, omitted coefficients
and strict inequalities at that point. If a fixed downstairs cutoff
$\chi$ has compact support in the original unit domain, cover its
support by finitely many of these local neighbourhood interiors, and
choose an inner compact partition $\theta_a$ by (7). Let
$b_{a,\varepsilon}$ be the local combination of (18). Put
\[
        a_\varepsilon=
              \sum_a\widetilde{\chi\theta_a b_{a,\varepsilon}},     \tag{21}
\]
where tilde means extension by zero. This is ordinary smooth and
supported in $\operatorname{supp}\chi$. A product supported compactly
inside its ordinary open is identically zero on a neighbourhood of
each point outside that open, so this extension is smooth and has no
boundary derivative term. The sum-one identity near
$\operatorname{supp}\chi$ and (20), for this finite fixed cover, prove
\[
 \big\|(D((\chi\circ\pi)T-\pi^*a_\varepsilon))_{
                      \mathrm{Rad},E}\big\|_{\mathrm{TV}}\to0       \tag{22}
\]
for the given invariant scalar polynomial $T$. All supports here lie
in $\pi^{-1}(\operatorname{supp}\chi)$, independently of
$\varepsilon$. There is no assertion of positive-test preservation.

## T9. Every compact ordinary scalar test; the two limits and support

Let invariant $\beta\in A_c^{0,0}(X_E)$ be arbitrary, and set
$F=\pi(\operatorname{supp}\beta)$. It is compact. Cover $F$ by
finitely many ordinary interiors $U_i$ of strict affinoids $V_i$ on
which (8) holds, and choose outer cutoffs $\chi_i$ from (7), compactly
supported in $U_i$, with sum one near $F$. Put
$C=\bigcup_i\operatorname{supp}\chi_i$. It is a fixed compact set
containing $F$.

On $V_{i,E}$ approximate the fixed Euclidean coefficient $\Phi_i$
through order two on a box containing the fixed unit moment image by
polynomials $P_{i,j}$. Choose the box to contain all translated tuple
images as well. Let $T_{i,j}$ be the real group average of
$P_{i,j}(T_i)$. Since $\beta$ is invariant, it is also the average
of $\Phi_i(T_i)$, so $\beta-T_{i,j}$ tends to zero in coefficient
$C^2$ on a **fixed upstairs** moment tuple containing all the
translates. Include fixed moment descriptions of $\chi_i\circ\pi$
on a finite compact cover of its support. The product rule and (19)
give
\[
 \big\|(D((\chi_i\circ\pi)(\beta-T_{i,j})))_{
                     \mathrm{Rad},E}\big\|_{\mathrm{TV}}\to0.       \tag{23}
\]

For each fixed $j$, use (9) to express $T_{i,j}$ as finitely many
traces. Apply (21)--(22) with outer cutoff $\chi_i$ to obtain
$a_{i,j}$ supported in $\operatorname{supp}\chi_i$ and with
\[
 \big\|(D((\chi_i\circ\pi)T_{i,j}-\pi^*a_{i,j}))_{
                     \mathrm{Rad},E}\big\|_{\mathrm{TV}}<1/j       \tag{24}
\]
(or $1/(ij)$ after any fixed finite enumeration). Each fixed-polynomial
local cover, inner partition and moment refinement is chosen **before**
its smoothing limit. It may depend on $j$. Its derivative bounds may
grow with $j$; smoothing is chosen after those bounds. This causes no
problem because (23) is evaluated with the fixed outer cutoffs, before
the inner localization of $T_{i,j}$. The varying inner cutoffs never
multiply the polynomial approximation error in (23), and every
approximate support remains inside the same outer $C$. Neither a
degree-uniform estimate nor an infinite simultaneous unit shrink is
asserted.

Set $\alpha_j=\sum_i a_{i,j}$. Globally
$\beta=\sum_i(\chi_i\circ\pi)\beta$, since the sum is one near
its support and it vanishes off that support. Equations (23)--(24)
and the finite triangle inequality prove (2). The support of every
differentiated error is contained in $\pi^{-1}(C)$, compact by
T3. Thus for **every** continuous finite multiplier $h$,
\[
       B_{h\circ\pi}(\beta-\pi^*\alpha_j)\longrightarrow0,
                                                               \tag{25}
\]
using its boundedness on that compact set. This proves the actual
ordinary scalar test gate for curves, not merely $C^0$ density of
invariant functions.

## T10. Forward Galois ascent and actual normal-closure descent

For a general compact ordinary scalar test $\beta$ upstairs, (6),
ordinary exterior functoriality on the restricted carrier, and
invariance of $h\circ\pi$ show
$B_{h\circ\pi}(g^*\beta)=B_{h\circ\pi}(\beta)$. Its real average
$\beta^{\mathrm{av}}=d^{-1}\sum_g g^*\beta$ has the same pairing.
Its support is in a compact finite group saturation. Real averaging
does not divide by $d$ in $K$, including when $\operatorname{char}K$
divides $d$.

For every downstairs compact test $\alpha$, its pullback is compact.
The scalar projection formula (4), with **no degree factor**, gives
\[
  B_{h\circ\pi}(\pi^*\alpha)
     =\int_{X_E}(h\circ\pi)(\pi^*D\alpha)_{\mathrm{Rad},E}
     =\int_X h(D\alpha)_{\mathrm{Rad},K}=B_h(\alpha).     \tag{26}
\]
Smooth exterior functoriality suffices; no continuous-current pullback
has been presumed. If the downstairs current is zero, approximate
$\beta^{\mathrm{av}}$ by (2). Its approximate pairings vanish by
(26), and (25) proves that its pairing, hence that of every upstairs
test, vanishes. This proves forward ascent for every finite Galois
extension, including wild ones, on all curves in the stated scope.

Conversely, (26) alone proves reverse descent whenever the upstairs
current is zero. This calculation works for every finite separable
extension, without a group, by compactness, purity, and (4). It is an
actual proof of the descent needed below, not a use of an earlier note.

For arbitrary finite separable $E/K$, take the finite Galois normal
closure $N/K$ constructed in T3, with its unique extending
absolute value and completeness. Forward Galois ascent gives zero
current on $X_N$. The space $X_E$ retains every ambient hypothesis
and pure dimension one by T3, and $N/E$ is finite separable.
There is a canonical analytic identification
$(X_E)_N=X_N$: on affinoids it is the associative tensor isomorphism
$(A\otimes_K E)\otimes_E N=A\otimes_K N$ with the equivalent
finite-module topologies. The pullback of $h\circ\pi_E$ is the
original pullback on $X_N$. Apply the just-proved reverse calculation
to $N/E$, testing each compact ordinary function on $X_E$, to obtain
zero current on $X_E$. This proves (1) at every finite separable stage. It is the
finite dependency, before the completed stage in T13. Ordinary opens retain the stated assumptions and the
same argument applies to their scalar inverse images.



## T11. Finite inseparability and arbitrary finite algebraic stages

### T11.1. Frobenius, topology and exact scalar tests

Let $k$ be complete, nontrivially valued, of characteristic $p>0$,
and let $F/k$ be finite purely inseparable. Choose $q=p^e$ with
$F^q\subset k$. T3's bounded-coordinate argument applies to
**every** finite extension, and gives
$A\widehat\otimes_k F=A\otimes_k F$ with its finite-module topology.
Consequently every $u=\sum a_i\otimes\lambda_i$ satisfies
\[
                    u^q=\sum a_i^q\lambda_i^q\in A.       \tag{27}
\]
This is an identity in the actual algebra, including nilpotents.

Scalar projection is surjective by the affine foundation in T2;
T12.1 also gives a direct proof for all fields used here.
If two points of $\mathcal M(A\otimes F)$ project to $x$, (27) forces
their values on every $u$ to equal $|u^q(x)|^{1/q}$. They are the same
seminorm. The projection is thus a continuous bijection from a compact
space to a Hausdorff space, hence a homeomorphism. On a good separated
space these affine homeomorphisms glue on the ordinary interiors of
downstairs affinoid neighbourhoods. No covering-space assertion is used.

For a unit $f\in(A\otimes F)^\times$, (27) gives $f^q=g\in A$.
The function $g$ has no analytic zero downstairs, by surjectivity,
so it is an actual unit by T3's unit criterion. On the upstairs
carrier $t_f=q^{-1}t_g$. Now let
$\beta\in A_c^{0,0}(X_F)$ be arbitrary. Its support has compact
image $C$ under the homeomorphism. For each point of $C$, select an
ordinary local description of $\beta$, then a downstairs affinoid
neighbourhood $V$ whose full inverse image lies in that description
open. The inverse image is $V_F$, so all coordinate units restrict
to elements of its actual affinoid algebra. Taking their $q$th powers
gives an ordinary downstairs scalar description
$\varphi(q^{-1}t_{g_1},\ldots,q^{-1}t_{g_m})$ on
$\operatorname{int}_X V$. Equality of numerical smooth scalar
functions is equality of their ordinary $(0,0)$ sections, as explained
in T12.3. Cover $C$ by finitely many such opens, apply the
compact partition of T4, multiply these local descriptions by
its cutoffs, and extend by zero. This produces
$\alpha\in A_c^{0,0}(X)$ with $\beta=\pi_F^*\alpha$ everywhere.
Compact support inside each open makes the extension ordinary smooth;
no derivative is extended through an exposed boundary.

Goodness, strictness, separatedness and boundarylessness are preserved
as in T3. Purity is also preserved, and here is a proof that
does not assume equality of total dimensions gives local purity.
Given an upstairs point $y$, a downstairs affinoid neighbourhood of
its image has dimension one, and its scalar extension has dimension
one, giving the upper local bound. If local dimension at $y$ were
zero, take this affinoid upstairs and remove all its positive-dimensional
irreducible components, none of which contains $y$. An affinoid
neighbourhood inside the remaining ordinary open has dimension zero
by CLD 11.2.3's component/domain formula. By the homeomorphism choose
a downstairs affinoid neighbourhood whose full inverse image is
inside that open. Its downstairs dimension is one (it is a domain in
the pure curve), and its upstairs total dimension is one by scalar
dimension invariance, a contradiction. Existence of the smaller
downstairs affinoid neighbourhood uses goodness. This argument only
checks dimension; it never reduces the measure.

On these pure curves $D\beta=\pi_F^*D\alpha$, and the smooth
top-measure identity (4) proves
\[
             B_{h\circ\pi_F}(\beta)=B_h(\alpha).         \tag{28}
\]
All supports are compact. The converse is obtained by taking
$\beta=\pi_F^*\alpha$ for an arbitrary compact downstairs scalar
test. Thus finite purely inseparable zero-Hessian ascent and descent
are proved here directly. No earlier inseparable manuscript is a premise.

### T11.2. The finite mixed-field decomposition

Let $E/K$ be any finite algebraic extension. In characteristic zero
every irreducible polynomial has nonzero derivative, and is separable,
so T3--T10 apply. In characteristic $p$, choose finitely many
generators $a_1,\ldots,a_r$ of $E/K$. For each irreducible minimal
polynomial, repeatedly remove common factors $p$ from its exponents
until it has the form
\[
                f_i(Z)=g_i(Z^{p^{e_i}}),\qquad g_i'\ne0.
                                                               \tag{29}
\]
The polynomial $g_i$ is irreducible: a factorization of $g_i$ would
give a factorization of $f_i$ by substitution. Since $g_i$ is
irreducible and its derivative is nonzero of smaller degree,
$\gcd(g_i,g_i')=1$; its roots are distinct. Therefore
$b_i=a_i^{p^{e_i}}$ is separable over $K$. The compositum
$S=K(b_1,\ldots,b_r)\subset E$ is finite separable: adjoining a
root of a separable polynomial remains separable over an intermediate
field because its minimal polynomial divides that polynomial; extending
embeddings successively gives degree-many embeddings of the tower.
An intermediate simple field has degree-many embeddings as well:
each embedding has at most the remaining extension degree lifts, while
the entire tower has its full degree of embeddings. Thus its minimal
polynomial is separable. This proves the field facts used here without
assuming separability of an arbitrary algebraic stage.

With $e=\max e_i$, every $a_i^{p^e}\in S$, and taking $p^e$th powers
in a rational expression in the $a_i$ shows $E^{p^e}\subset S$.
Hence $E/S$ is finite purely inseparable. Both fields are complete
under the prescribed absolute value by the finite norm proof in
T3. This gives the **actual embedded** tower
$K\subset S\subset E$, not an abstract factorization of degrees.

The finite tensor associativity with bounded inverse maps, proved in
T12.1, identifies $(X_S)_E=X_E$ as analytic spaces, with the
actual algebra and not its reduction. $X_S$ has all ambient hypotheses
and pure curve dimension by T3. Finite separable ascent to $S$,
then the proved Frobenius ascent to $E$, proves (1) at every finite
algebraic stage. Reverse descent uses (4) directly. Generic lengths
are those of the actual tensors throughout. No degree factor is
introduced into scalar projection.

## T12. Completion, rational neighbourhoods and every compact scalar test

### T12.1. Fields, completed tensors, surjectivity and compactness

Write $M=\bigcup_E E$, where $E$ ranges over its finite subextensions
of $K$. It is a directed union: a finite list of algebraic elements
generates a finite field, by successive multiplication of finite
degrees. Each $E$ is complete by T3. We never regard $M$ as
a complete analytic field unless it happens already to be complete.
Its completion $L$ is a complete valued field. For a $K$-affinoid
algebra $A$, the image of $A\otimes_K M$ is dense in
$A_L=A\widehat\otimes_K L$. Indeed finite algebraic tensors are
dense by definition of completion; a tensor
$\sum a_j\otimes\lambda_j$ can be approximated by replacing its
finitely many $\lambda_j\in L$ with $m_j\in M$, with tensor error
at most $\max_j\|a_j\||\lambda_j-m_j|$. Approximation statements
refer to the **image**, so no injectivity or isometry of an
uncompleted infinite tensor is presumed.

Here is the associative tensor argument actually required. For finite
$E/K$ with a basis $e_i$, the bounded coordinate maps give
$A_E=A\otimes_K E$ with its finite-module topology. The maps on
algebraic tensors
\[
 (a\otimes e)\otimes\lambda\mapsto a\otimes e\lambda,
 \qquad a\otimes\lambda\mapsto(a\otimes1)\otimes\lambda
                                                               \tag{30}
\]
extend continuously to inverse maps
$(A_E)\widehat\otimes_E L\simeq A\widehat\otimes_K L$.
For the first map, the bounded multiplication map
$(b,\lambda)\mapsto\sum_i a_i\otimes e_i\lambda$, where
$b=\sum_i a_i\otimes e_i$, is bounded in $b$ by the coordinate
estimates and in $\lambda$ by the tensor inequality. It is balanced
over $E$. The reverse map is bounded by the tensor inequality and
the bounded inclusion $A\to A_E$. These maps are inverse on dense
elementary tensors, hence inverse on the completions. The same proof
works when $A$ is affinoid with arbitrary radii, and for two finite
stages. Thus all stage projections and inverse images of rational
domains used below are actual analytic base changes. No associativity
claim for an infinite uncompleted Banach tensor is needed.

For clarity, scalar surjectivity in the present completed-algebraic
scope also has a direct seminorm proof. Given
$x\in\mathcal M(A)$, put $H=\mathcal H(x)$. Embed the algebraic
extension $M$ into an algebraic closure $\overline H$ over $K$.
Such an embedding is obtained by successively adjoining roots, or by
maximizing partial embeddings and adjoining a root of the minimal
polynomial if the domain is not all of $M$. Equip $\overline H$ with
the extending absolute value: the finite extension existence and
uniqueness proof of T3 makes the norms on its finite
$H$-subfields compatible. On every finite $K$-subfield of $M$ this
value is the specified one, again by uniqueness. Completing
$\overline H$ gives a complete field $F$ into which the isometric
embedding $M\to F$ extends to $L\to F$. For **every** tensor
representation with $\lambda_j\in L$, evaluation satisfies
\[
 \left|\sum_j a_j(x)\lambda_j\right|
       \le \max_j\|a_j\||\lambda_j|.
                                                               \tag{31}
\]
Taking the infimum over all representations bounds it by the full
tensor seminorm. It extends to $A_L$ and gives an analytic point
over $x$. This proof handles the separated quotient in the tensor
completion and uses no claimed isometry of $A\otimes M$.
The identical proof over $E$ gives surjectivity $X_L\to X_E$ and
surjectivity on every scalar-extended affinoid domain. On good spaces
these affine facts cover the whole space.

The inverse image of a compact $C\subset X_E$ is compact: finitely
many ordinary interiors of affinoid neighbourhoods cover $C$.
Its inverse image is closed in the finite union of their compact
scalar extensions, since the spaces are Hausdorff. This works for
the infinite completed projection. It does not assert a finite
fibre, a finite Galois cover or any infinite group averaging.

For a nonzero $\lambda\in L$, choose $m\in M$ with
$|m-\lambda|<|\lambda|$. Then $|m|=|\lambda|$. Thus
$|L^\times|=\bigcup_E|E^\times|$. This observation handles any
value-group radius if desired, but the rational argument below
allows **all positive real radii**, so it needs no strictifying
extension and no approximation of a radius.

### T12.2. Exact rational and strict-locus descent

Let $A$ be affinoid over a finite stage $E_0$, set
$B=A\widehat\otimes_{E_0}L$, and let a rational domain of
$\mathcal M(B)$ be defined by
\[
             |f_i|\le r_i|g|\quad(1\le i\le s),
             \qquad r_i>0,                              \tag{32}
\]
where $g,f_1,\ldots,f_s$ have no common analytic zero. Empty
systems can instead be handled by the whole affinoid with the
harmless condition $|1|\le2|1|$. Compactness gives
\[
 \delta=\min_{y\in\mathcal M(B)}
             \max\{|g(y)|,r_1^{-1}|f_1(y)|,\ldots,
                                  r_s^{-1}|f_s(y)|\}>0.
                                                               \tag{33}
\]
Choose simultaneous finite-stage approximants $g',f_i'$ in one
$A_E$ with Banach errors less than
$\delta\min(1,r_1,\ldots,r_s)$. This is possible by T12.1.
Their evaluation errors satisfy
\[
                 |g'-g|<\delta,
                 |f_i'-f_i|<r_i\delta                 \tag{34}
\]
at every point upstairs. Neither vanished nor nilpotent functions
are logarithmed, and none is assumed to have small Banach norm merely
because its spectral norm is zero. They are approximated in the actual
Banach algebra just like the other elements.

Both conjunctions, (32) and the conjunction of its strict versions,
are **unchanged** by (34). To check all boundary cases, first suppose
$|g(y)|\ge\delta$. Then $|g'(y)|=|g(y)|$. For each $i$ with
$|f_i(y)|\ge r_i|g(y)|$, (34) forces $|f_i'(y)|=|f_i(y)|$.
For each $i$ with $|f_i(y)|<r_i|g(y)|$, it instead forces
$|f_i'(y)|<r_i|g'(y)|$. Hence each weak inequality, each equality,
and each strict inequality is preserved at that point. If
$|g(y)|<\delta$, (33) supplies an $i$ with
$r_i^{-1}|f_i(y)|\ge\delta$. Its numerator norm is unchanged,
while $|g'(y)|<\delta$. This inequality remains strictly false,
so both conjunctions remain false. These arguments also cover
$g(y)=0$ and any number of zero numerators.

The weighted maximum for the approximants is everywhere positive
upstairs. Surjectivity to $\mathcal M(A_E)$ then shows the
denominator/numerators have no common zero there. They generate the
unit ideal: otherwise a maximal ideal containing them gives an
analytic common zero. Thus they define a genuine rational analytic
domain $R_E$ by CLD 11.1.5. Its scalar extension has exactly the set
(32). Analytic domain uniqueness, or the universal rational-domain
presentation by adjoining the bounded ratios, identifies it with the
given domain $R_L$ as an analytic domain. The actual rational
localization algebra, with all nilpotents, is retained. The strict
locus $O_E=\{|f_i'|<r_i|g'|\ \forall i\}$ is ordinary open in
the ambient affinoid, lies in its rational domain, and has inverse
image **exactly** the original strict locus $O_L$. No invariance of
absolute analytic interiors or equality of all topological interiors
is asserted.

The stronger rational-neighbourhood statement of CLD 11.1.5 says
that for any $y$ and any prescribed ordinary open in an affinoid,
one can choose (32) with $R_L$ inside that open and $y$ in its
strict locus. Thus the preceding construction supplies finite-stage
ordinary neighbourhoods of each chosen point, without controlling
an entire infinite scalar fibre. Only finitely many such choices
are subsequently needed on a compact support.

### T12.3. Exact finite-stage local descriptions

Let $\beta$ be ordinary smooth on $X_L$ near $y$, and let $x$ be
its image in $X$. Choose a downstairs affinoid neighbourhood $V_0$
and an ordinary open $U_0\subset V_0$ containing $x$. The inverse
image $U_{0,L}$ is open. Intersect it with an ordinary moment
description open of $\beta$; on that intersection write
$\beta=\varphi(t_{f_1},\ldots,t_{f_m})$, with actual analytic
units and a smooth real coefficient defined on an open Euclidean
set containing the coordinate image. This can always be arranged
locally by shrinking the description near $y$.

Inside $V_{0,L}$ select a rational neighbourhood $R_L$ of $y$
contained in this intersection, with $y$ in its strict locus.
T12.2 gives $R_L=(R_{E_0})_L$ for a finite stage $E_0$,
and a descended strict locus. Because $R_L\subset U_{0,L}$,
surjectivity on $R_{E_0}$ gives $R_{E_0}\subset U_{0,E_0}$.
Its strict locus is therefore an ordinary open of the whole
$X_{E_0}$, not just an open of an exposed affinoid boundary.

On the compact rational affinoid $R_L$, put
$\delta_j=\min|f_j|>0$. Apply density in the actual rational
affinoid algebra, now viewed over $E_0$, to select a common finite
$E\supset E_0$ and $u_j\in\mathcal O(R_E)$ with
$\|u_j-f_j\|<\delta_j$ upstairs. Ultrametricity gives
\[
                     |u_j(y')|=|f_j(y')|
                                 \quad(y'\in R_L).     \tag{35}
\]
By surjectivity $u_j$ has no zero on $R_E$, so it is an actual
unit by the unit criterion. Its inverse exists in that affinoid
algebra; no approximation of an inverse or reduction of the algebra
is necessary. Surjectivity also makes the finite-stage moment image
of the $u_j$ equal to the upstairs image of the $f_j$, so the same
Euclidean coefficient $\varphi$ is defined on it.

On the inverse image $O_E$ of the strict locus define the ordinary
smooth function $b_E=\varphi(t_{u_1},\ldots,t_{u_m})$.
Then $q_E^*b_E=\beta$ on $O_L=q_E^{-1}O_E$. This is an exact
scalar-section identity. To justify the section claim precisely,
CLD 3.4.6 embeds the $(0,0)$ G-form sheaf in numerical functions:
on each compact chart the nullity criterion 3.4.1/3.4.4 says that a
zero numerical coefficient is the zero section; compact charts
G-cover the space. Hence equal numerical scalar sections coincide,
and ordinary scalar sections are included in this sheaf. Alternatively,
the combined moment $(f,u)$ has image in the diagonal
$\{t_f=t_u\}$ by (35); the difference of the two scalar
coefficient functions restricts to zero there, and moment nullity
gives the same conclusion. No universal moment-dimension equality
is used. Smooth differentiation consequently commutes with this
**exact identity**, giving $D\beta=q_E^*Db_E$ on that open.

### T12.4. Compact scalar tests and extension by zero

Now let $\beta\in A_c^{0,0}(X_L)$ be arbitrary and put
$F=\operatorname{supp}\beta$. If $F$ is empty, take $\alpha=0$
at any finite stage. Otherwise T12.3 gives a neighbourhood
$O_{i,L}=q_{E_i}^{-1}O_{i,E_i}$ and a descended ordinary function
$b_{i,E_i}$ near each point of $F$. Choose finitely many covering
$F$. Enlarge to a common finite field $E\subset M$ and base change
all these rational domains, strict loci and unit lists to $E$.
Associativity (30) shows
$O_{i,L}=q_E^{-1}O_{i,E}$ and $\beta=q_E^*b_{i,E}$ there.

The compact set $F_E=q_E(F)$ is covered by the finitely many
$O_{i,E}$. Apply T4's explicit compact partition, built
only from CLD 15.2.5, to obtain ordinary smooth $\theta_i$ with
compact support in $O_{i,E}$ and sum one near $F_E$. Put
\[
                \alpha=\sum_i\widetilde{\theta_i b_{i,E}},
                                                               \tag{36}
\]
where tilde means extension by zero to $X_E$. Each product is
ordinary smooth on its open, with support in the compact
$\operatorname{supp}\theta_i\subset O_{i,E}$. Since that compact
set is closed in the Hausdorff $X_E$, every point outside it has
an ordinary zero neighbourhood. Therefore its extension is ordinary
smooth at every exterior point as well. This proves (36) lies in
$A_c^{0,0}(X_E)$, with no boundary derivative term.

On the inverse image of its defining open each summand pulls back
to $(\theta_i\circ q_E)\beta$. Off that open its pullback is
zero, and $\theta_i\circ q_E$ is also zero. Thus, **globally**,
\[
 q_E^*\alpha=(\sum_i\theta_i\circ q_E)\beta=\beta.       \tag{37}
\]
On $F$ the sum is one. Outside $F$ the function $\beta$ is zero,
so the equality also holds there regardless of that sum. No descent
or saturation of the original support is assumed. No agreement of
the separate $b_{i,E}$ on downstairs overlaps needs to be presumed;
the finite sum is itself a smooth section, and (37) proves precisely
its required pullback. Its support is contained in a finite union of
compact cutoff supports. The inverse image of that union is compact
by T12.1. Differentiation commutes with the exact ordinary
smooth identity (37), so every compact upstairs scalar test and its
Hessian are covered. This is stronger than $C^0$ density and does
not use a differentiated approximation topology at completion.

### T12.5. Ambient geometry and local purity after completion

Goodness follows because inverse images of downstairs affinoid
neighbourhoods are affinoid and contain inverse images of their
ordinary interiors. Strict presentations base change to strict
presentations. The diagonal base change preserves separatedness.
Boundarylessness follows from GR 2.11(5'), as stated in T2;
ordinary open restrictions retain it by GR 2.11(3),(4).

We check local purity for $X_L$, rather than just total dimension.
Around the image of $y\in X_L$ take a downstairs strict affinoid
neighbourhood $V_0$ of dimension one. Then $V_{0,L}$ has dimension
one, giving the upper local bound. Suppose local dimension at $y$
were zero. In $V_{0,L}$ discard its finitely many dimension-one
minimal-prime components, none of which contains $y$. In the
remaining ordinary open choose a rational affinoid neighbourhood
$R_L$ of $y$ inside the inverse image of
$\operatorname{int}_X V_0$, with strict inequalities at $y$.
The component/domain dimension formula in CLD 11.2.3 gives
$\dim R_L=0$. T12.2 descends $R_L$ to a nonempty
$R_E$ at a finite field, inside $X_E$. The actual $X_E$ is pure
one-dimensional by T3 and 11. Its domain $R_E$ has dimension
one, including if its chosen real radii make the domain non-strict.
Scalar dimension invariance and analytic domain identification give
$\dim R_L=\dim(R_E)_L=\dim R_E=1$, a contradiction.
Hence every upstairs point has dimension one. This argument keeps
the original strict ambient space and does not infer an endpoint
theorem from a non-strict radial core.

All top measures below are on the **actual** pure curves just proved
to exist. Their multiplicities need not remain numerically unchanged
point by point. They are the finite-flat fibre-algebra dimensions in
the canonical calibration. For reference, the usual generic-length
identity is obtained by tensoring a composition series of a generic
Artinian stalk with the flat upstairs generic stalk: each residue-field
quotient becomes the generic Artinian algebra of the base-changed
reduction. If its length is $\mu$ and the original length is $\ell$,
the length upstairs is $\mu\ell$. This is CLD 13.2.8 with
$\mathcal F=\mathcal O_X$; its proof body is included in Appendix S.
We use the calibration and the Artinian degree-sum proof of (4), not
a replacement by geometric point counts or a supposed constant
extension degree for an infinite extension.

## T13. Completed forward ascent and actual reverse descent

Assume $D[h]=0$ downstairs. Given **any**
$\beta\in A_c^{0,0}(X_L)$, T12.4 supplies finite $E$ and
$\alpha\in A_c^{0,0}(X_E)$ with $\beta=q_E^*\alpha$ exactly.
Put $h_E=h\circ\pi_E$. Finite algebraic ascent, proved in
T3--T11, gives $D[h_E]=0$. T12.5 verifies the pure
curve and ambient hypotheses for both $X_E$ and $X_L$. Smooth
functoriality and the **$L$- and $E$-calibrated** projection formula
(4) yield
\[
 \begin{aligned}
 B_{h\circ\pi}(\beta)
 &=\int_{X_L}(h_E\circ q_E)(q_E^*D\alpha)_{\mathrm{Rad},L}\\
 &=\int_{X_E}h_E(D\alpha)_{\mathrm{Rad},E}
 =0.
 \end{aligned}                                             \tag{38}
\]
The relevant supports lie in the compact inverse image of
$\operatorname{supp}\alpha$; the continuous finite multiplier
is bounded there. The signed-measure pushforward formula is therefore
legitimate. Since $\beta$ was arbitrary, the upstairs zero-current
equation follows. There is no pullback of an arbitrary continuous
current in this proof and no field-degree factor in (38).

Conversely, suppose the upstairs equation holds. For an arbitrary
$\psi\in A_c^{0,0}(X)$ its pullback has compact support by
T12.1. Apply smooth functoriality and (4) directly for $L/K$:
\[
             B_h(\psi)=B_{h\circ\pi}(\pi^*\psi)=0.        \tag{39}
\]
Thus the downstairs equation holds. This reverse calculation is
included for completeness, not counted as new forward progress.
Ordinary-open localization follows from the ambient checks and
the same arguments on that open; no global quasicompactness or
paracompactness is added. This proves (1) with all its stated scope.

# Part C. Algebraically closed recognition, with the actual structures

Here $k$ is complete, algebraically closed, and nontrivially valued.
The transport proof T2 already supplies affinoid foundations, compact ordinary
cutoffs, finite compact partitions, ordinary moment presentations, and canonical
calibrated integration. We need the following additional exact source inputs.

CLD 11.2.5 states that affinoid irreducible components are finite in number,
that an irreducible analytic space is pure, that its proper closed analytic
subsets have smaller dimension, and that components of analytic-domain
intersections retain their dimensions. CLD 11.3.1 supplies finite normalization
of a reduced analytic space, locally the integral closure in its total quotient
ring, and persistence of $S_j$, regularity, and normality on domains.
CLD 11.4.8--9 identifies quasi-smoothness with geometric regularity and, on
good spaces, smoothness with quasi-smoothness plus relative interior.
CLD 11.4.1.3 gives
\[
 \operatorname{Int}(V/Z)\cap f^{-1}\operatorname{Int}(Z)=\operatorname{Int}(V)
\]
when the target is separated. Domain relative interior is ordinary topological
interior; finite maps are boundaryless. CLD 16.6.3 states
$\delta_Z=\delta_{[Z]}$: the integration current is the sum over reduced
irreducible components with their actual generic lengths. Its proof contracts
canonical calibrations, not point-count measures. CLD 15.2.1(b) says the support
of a $(p,q)$ form avoids a closed analytic subspace of dimension less than
$\max(p,q)$. Thus a curve top form vanishes in a neighbourhood of each rigid
point, but a scalar test need not vanish there.

The strict affinoid Nullstellensatz used here is BGR, *Non-Archimedean
Analysis*, 6.1.2/1: over a complete nontrivially valued field, every maximal
ideal of a strict affinoid has residue field finite over the ground field.
A zero-dimensional strict affinoid is consequently a finite-dimensional
Artinian algebra over the field. Indeed its semisimple quotient is a finite
product of these fields, and its nilpotent radical has a finite filtration
with finite-dimensional quotients. Its points are finitely many rigid points,
with their actual residue degrees and lengths. This standard foundation is
stated and cited exactly; no BGR PDF retrieval is claimed.

The calibrated specialization input is CLD 14.7.2 with **target dimension
$d=1$**: a compact pure $r$-dimensional source satisfying $S_1$, a regular
pure one-dimensional target, a morphism pure of relative dimension $r-1$,
a unit moment $b$, and a rigid target point have locally constant calibrated
$(r-1)$-dimensional fibre tropicalization. For target $\mathbb A^1$ and zero,
the top calibrated tropicalization of $(b,f)$ for sufficiently negative
$\log|f|$ is its zero-fibre tropicalization times the standard negative interval.
The theorem permits source boundary. The complete theorem and proof, including
14.7.1's boundary estimate and 14.7.3's finite-flat degree argument, appear
in Appendix S. No unsupported $S_1$ inference in CLD 16.7.5 is used.

## C1. Lifting compact tests through closed immersions

If $i:C\hookrightarrow V$ is a closed embedding of good separated spaces,
every compact ordinary test on $C$ lifts to a compact ordinary test of the
same bidegree on $V$. Locally express the test by unit germs and a smooth
Euclidean superform. The quotient sheaf $i_*\mathcal O_C=\mathcal O_V/\mathcal I$
lifts each germ. Its nonzero value at the point permits an ordinary shrinking
on which the lift is a unit. Shrink also into the coefficient domain and into
the given presentation on $C$. Thus one local ambient form restricts to the
given test everywhere on that intersection, including its zero regions.

Choose finitely many such opens covering the compact support. A compact
ambient cutoff $\chi=1$ near that support can be supported inside their union.
The finite compact partition of T4 on $\operatorname{supp}\chi$ gives
$\theta_i$ supported in the respective opens with sum one nearby. The form
$\widetilde\eta=\chi\sum_i\theta_i\eta_i$, extended by zero, is compact
ordinary smooth. Its restriction is $\eta$: wherever a term contributes it
restricts to $\eta$, and the factors sum to one near its support. Off the
support the restriction is zero. Therefore $i_*$ is injective on currents,
by evaluation on these lifts. This proves injectivity, not pullback of
arbitrary continuous currents.

## C2. Scalar tests at rigid points and removal of rigid punctures

Every ordinary smooth scalar germ at a rigid point $a$ is locally constant,
also over a nonclosed imperfect field. For a unit germ $v$, let $q=|v(a)|>0$
and let $P(T)=T^e+\sum_{j<e}c_jT^j$ be the minimal polynomial of $v(a)$
over the ground field. All conjugate roots have norm $q$, with inseparable
repetitions, by the unique extending valuation proved in T3. Hence
$|c_j|\leq q^{e-j}$ and $|c_0|=q^e$. On the ordinary neighbourhood
$|P(v)|<q^e$, neither $|v|>q$ (dominant leading term) nor $|v|<q$
(dominant constant term) is possible. Thus $|v|=q$ there. Intersect for
the finitely many units of a scalar moment description. All its coordinates
are constant. This proves the assertion for every ordinary scalar section.

On a reduced good separated strict boundaryless pure curve $V$, at any rigid
$a$ there are compact ordinary smooth cutoffs $\chi_m=1$ near $a$ whose
supports shrink to $a$, with
\[
             \int_V D\chi_m=0,
             \|(D\chi_m)_{\mathrm{Rad}}\|_{\mathrm{TV}}\leq M
\]
for one fixed finite $M$. Here is a construction, including its weights.
Choose a reduced strict affinoid neighbourhood $N$ of $a$. In its algebra
choose $f\in\mathfrak m_a$ outside every minimal prime. Such a choice is
possible: no one-dimensional component is contained in the rigid point, and
finite prime avoidance applies. Explicitly, express generators of
$\mathfrak m_a$ and avoid the finitely many proper linear subspaces of their
coefficients over the infinite ground field. A product of nonzero linear
forms cannot vanish everywhere on that coefficient space. Reduced rings
have zero intersection of minimal primes, so this $f$ is a non-zero-divisor.

Its zero locus on $N$ is pure zero-dimensional and consists of finitely many
rigid points. Remove the others and shrink inside $\operatorname{int}_V N$.
At $a$ the map $f$ has relative dimension zero. Zariski upper semicontinuity
(CLD 11.4.5, Ducros's local fibre-dimension theorem) gives an ordinary
neighbourhood on which the relative dimension is zero. Choose a smaller
strict affinoid neighbourhood $N'$ there. Its zero fibre has support exactly
$a$, with some length $\ell>0$. Reduced noetherian rings satisfy $S_1$:
an element outside all minimal primes is regular, and prime avoidance in a
positive-dimensional local ring produces one in its maximal ideal. The
property persists on analytic domains. Thus CLD 14.7.2 applies to $N'$,
with $r=d=1$, target $\mathbb A^1$, and trivial auxiliary moment. Its exact
negative interval has calibration
\[
                      d_0|e_1|,
                  \qquad d_0=\ell[\mathcal H(a):k].
\]
The degree is the full degree, not its separable part: CLD 13.3.7 and
14.4.3 compute zero-dimensional canonical mass from fibre algebra dimension.

Choose a real smooth $\chi$, one for $s\leq-1$, zero for $s\geq0$, valued
in $[0,1]$. On $N'\setminus\{a\}$ set
$\chi_m=\chi(\log|f|+m)$ and extend as one at the zero and zero outside
$N'$. These extensions are ordinary smooth. For any neighbourhood $H$ of
$a$ with closure inside $\operatorname{int}_V N'$, compactness gives
$\min_{N'\setminus H}|f|>0$. For sufficiently large $m$ the support lies
in $H$ and avoids the domain boundary. The same argument for any
neighbourhood proves shrinking support.
On the transition region
$D\chi_m=\chi''(\log|f|+m)d'\log|f|\wedge d''\log|f|$.
Take compact nonnegative smooth $b\geq|\chi''|$ on $\mathbb R$. The
positive form with coefficient $b$ dominates its absolute measure.
Calibrated integration gives total mass $d_0\int b$, independent of $m$,
and $\int D\chi_m=d_0\int\chi''=0$. Stokes on the boundaryless curve
gives the same zero. No measure has been assigned to an unknown Hessian.

Now suppose $g$ is continuous and $D[g]=0$ off a locally finite rigid set.
Localize to one puncture $a$. For a compact scalar test $\psi$, local
constancy just proved implies $\psi-\psi(a)\theta$ has support disjoint
from $a$, where $\theta=1$ near $a$ is a compact smooth cutoff. Thus
$D[g](\psi)=c\psi(a)$ with $c=D[g](\theta)$ as a functional on all
ordinary scalar tests, without presuming order zero. Evaluate on $\chi_m$:
\[
 |c|=\left|\int(g-g(a))D\chi_m\right|
 \leq M\sup_{\operatorname{supp}\chi_m}|g-g(a)|\longrightarrow0.
\]
Continuity and shrinking support prove $c=0$. This removes all punctures
locally. This argument is valid over every complete nontrivially valued field.

## C3. Component weights and normalization transport

On the ordinary interior $O$ of a strict affinoid curve with algebra $A$,
associated-cycle integration gives
$[g]=\sum_i m_i(i_i)_*[g|_{Z_i}]$, where $Z_i$ are reduced components
and $m_i=\operatorname{length}(A_{P_i})>0$ are the original generic lengths.
Distinct components intersect in a finite rigid set. On the ordinary open
where only $Z_i$ remains, $D[g]=0$ implies
$m_i(i_i)_*D[g|_{Z_i}]=0$. C1 and the actual positive $m_i$ imply the
intrinsic reduced-component equation there. C2 removes its rigid intersections,
giving $D[g|_{Z_i}]=0$ on all of $Z_i\cap O$. Multiplicities may be unequal;
they have been separated locally, not divided by a global scalar. Combining
the equations with generic lengths also proves the equation on the reduction.
This works pointwise on ordinary neighbourhoods, so the reduced-curve equation
holds globally without choosing global component labels.

Let $\nu:\widetilde Z\to Z$ be the normalization of a reduced strict curve.
On a reduced affinoid $A$, its finite integral closure $\overline A$ lies in
the total quotient ring. A common regular denominator $q$ for finitely many
module generators gives $q\overline A\subseteq A$ and
$A[q^{-1}]=\overline A[q^{-1}]$. Thus normalization is an actual analytic
isomorphism away from a locally finite rigid set. Its preimage is rigid and
locally finite. Finite maps give good separated strict boundaryless pure
curves here. On the isomorphism open, ordinary forms, $D$, and calibration
transport the equation to $g\circ\nu$. C2 removes the upstairs punctures,
giving $D[g\circ\nu]=0$ throughout. This proves normalization transport
without inverting a finite-current direct image.

## C4. Local algebraic model and Wanner comparison

The exact embedding input is van der Put, *The class group of a one-dimensional
affinoid space*, Ann. Inst. Fourier 30(4) (1980), Theorem 1.1: every
one-dimensional normal connected affinoid over a **complete algebraically
closed** non-Archimedean field is an affinoid subspace of a nonsingular
complete algebraic curve. His affinoids are strict quotients of Tate algebras.
The theorem's proof and field assumption appear in Appendix S. The
Berkovich-domain formulation is explicitly used in Thuillier's proof of
Theorem 2.3.8, printed page 53: a pure rig-smooth strict affinoid, after a
finite separable extension, is an affinoid domain of a smooth proper algebraic
curve. Here the extension is trivial. Affinoid-domain compatibility of rigid
and Berkovich geometry is Berkovich (1993), Section 1.6; the actual algebra
and domain structure are unchanged. No general category equivalence on
nonparacompact spaces is needed.

Every point $z$ of a smooth strict boundaryless analytic curve has a strict
affinoid neighbourhood $Q$. Select its connected component containing $z$.
It is still a neighbourhood and is normal, reduced, pure one-dimensional.
Its algebra is a domain: distinct minimal components of a noetherian normal
ring are disjoint and yield idempotents, and connectedness selects one.
The embedding gives $j:Q\simeq Q'\subseteq C^{\mathrm{an}}$ for a smooth
proper algebraic curve over this same algebraically closed field.
This is a domain embedding, so it does not yet identify an ordinary open.
Because both ambient curves are separated and boundaryless, the boundary
equality above gives
\[
 \operatorname{int}_Z Q=\operatorname{Int}(Q),\qquad
 \operatorname{int}_{C^{\mathrm{an}}}Q'=\operatorname{Int}(Q').
\]
Absolute interior is intrinsic to the analytic space and preserved by $j$.
It therefore identifies actual ordinary neighbourhoods of $z$. This treats
every analytic point, not merely rigid points.

Wanner, arXiv:1801.04713v3, Theorem 4.7 has exactly the following scope:
$C$ is a smooth proper algebraic curve over an algebraically closed complete
nontrivially valued field, $W\subset C^{\mathrm{an}}$ is ordinary open, and
$v:W\to\mathbb R$ is continuous. If $v$ is current-psh in her Definition
3.16, then it is Thuillier-subharmonic. The field and curve assumptions are
in her global conventions; “psh” here is positive CLD Hessian current, not
the classical curve-test class. The statement and its complete proof, and
the definition of its test forms, appear in Appendix S.
Every one of her tests is an ordinary analytic CLD test: its algebraic
moment coordinates are analytic units on that ordinary open, with the
same smooth superform and compact support. Canonical integration of this
form is the CLD calibrated integral. Hence a zero ordinary current gives
her positivity for **both** signs. Only this inclusion of test classes is
used, not a reverse identification of all analytic tests with algebraic
ones. Analytic isomorphisms and domain restriction preserve that integral.

Transport a continuous zero-current function on a smooth curve to the
ordinary algebraic-model open just constructed. Compact tests pull back
and extend by zero in the original open; $D$ and integration are unchanged.
Wanner's theorem applies with all its hypotheses, so both signs are
Thuillier-subharmonic. They are harmonic by the Dirichlet comparison
criterion: on a strict affinoid domain the unique harmonic solution
with the same boundary values dominates the function by subharmonicity;
applying the same comparison to its negative gives equality.
This is GR 3.12, with Thuillier Lemma 2.3.9; its proof body appears below.
GR 3.4.2 identifies finite Thuillier-subharmonicity with GR-subharmonicity
on smooth strict curves, and GR 3.5(1) gives locality. Thus the function
is GR-harmonic on the entire smooth curve.

For the present submission we use only this Thuillier harmonicity,
not a reverse identification of Wanner's and ordinary analytic test classes.
Apply it to the normalization of the reduction obtained in C3. Over the perfect
field k the normalization is rig-smooth, and finite boundaryless composition
makes it smooth on the ordinary open in question (GR Lemma 3.9(1), with its
proof below). This yields exactly R1's harmonic-normalization input, without
taking the predecessor's arbitrary-field recognition conclusion as a premise.
No current is restricted directly to a normalization fibre.

# Part B. The completed algebraic closure

Equip an algebraic closure $\overline K$ with the extending absolute value.
It exists consistently on finite subextensions: existence and uniqueness
are proved in T3, and uniqueness makes restrictions compatible. Let
$C=\widehat{\overline K}$. It is a complete valued field containing $K$
isometrically, so its valuation is nontrivial. It is **algebraically closed**,
not just perfect; the following argument proves this without assuming
spherical completeness or separability.

For a monic polynomial $F\in C[T]$ of degree $d>0$, approximate its
coefficients by coefficients in $\overline K$, obtaining monic $F_m$ with
errors tending to zero arbitrarily fast. All coefficients are bounded,
so every root of every $F_m$ has norm at most one fixed $B\geq1$: if a
root had norm larger than both 1 and all coefficient norms, the leading
term would dominate every other term. Arrange successive coefficient
differences so that
$\max_i|a_{i,m+1}-a_{i,m}|B^{d-1}\leq\epsilon_m^d$, with
$\epsilon_m\downarrow0$. Choose a root $r_1$ of $F_1$ in $\overline K$.
After choosing $r_m$, evaluate $F_{m+1}(r_m)$; its norm is at most
$\epsilon_m^d$. Factoring $F_{m+1}=\prod_{j=1}^d(T-s_j)$ in $\overline K$
shows that some $s_j$ has $|r_m-s_j|\leq\epsilon_m$. Set it to $r_{m+1}$.
Ultrametricity makes this a Cauchy sequence. Its limit $r\in C$ satisfies
$F(r)=0$, by continuity and uniform coefficient convergence on the bounded
ball. This holds for every monic polynomial. Divide by the linear factor
and induct on degree to conclude algebraic closedness. The argument works
also for inseparable polynomials.

Applying T13 with M=the algebraic closure proves the actual zero-current equation on U_C. Part C applies over this algebraically closed C. This establishes the two inputs used in R16, separately.

# New gate: ordinary smooth two-sign regularization

## R0. Exact claim and independence of the gates

**Theorem R16 (completed-algebraic two-sign first-stage regularization).**
Let $K$ be complete and nontrivially valued, and let $X$ be good,
separated, strict, boundaryless and pure of analytic dimension one.
Let $U\subseteq X$ be an arbitrary ordinary open and
$h:U\to\mathbb R$ finite and continuous, with zero **ordinary analytic
CLD** current $D[h]$, where $D=d'd''$ and integration uses the actual
structure of $U$. Put $C=\widehat{\overline K}$, with its extending norm,
and $h_C=h\circ\pi$. For every $x\in U_C$ there is a compact strict
affinoid analytic domain $Y\subset U_C$, containing $x$ in its actual
ordinary interior, and, for each $\sigma\in\{1,-1\}$, functions
$u_n^\sigma\in C(Y)$ such that

\[
 u_{n+1}^\sigma\leq u_n^\sigma\quad\hbox{on }Y,\qquad
 \|u_n^\sigma-\sigma h_C\|_{C(Y)}\longrightarrow0.
\]

Each $u_n^\sigma$ is ordinary CLD-smooth and psh on the **same**
$Y^\circ=\operatorname{int}_{U_C}Y=\operatorname{Int}(Y)$.
The common $Y$ may be chosen inside any prescribed ordinary neighborhood
of $x$ in $U_C$.
Here psh means that its ordinary Hessian current is nonnegative against
every nonnegative compact ordinary scalar test on that interior.
No reduction of the calibration is implicit. In particular, both signs
are locally in the first ordinary-smooth decreasing-limit stage, and
hence in the requested CLD-psh hierarchy. The two sequences may differ.

This is a pure-curve theorem. It does not resolve the original
arbitrary-dimensional P06.2, and does not claim downstairs ordinary-smooth
regularization over every $K$. Approximation is not asserted to be harmonic.
The field $C$ is one field for the entire $U$, not a point-dependent choice.

The proof order matters: T proves completed-algebraic **ordinary-current**
transport by differentiated scalar tests; C recognizes the function on
smooth normalizations over $C$; R1--R7 produce ordinary-smooth psh
approximants with a fixed neighborhood. None of the approximation steps
assumes all-extension ascent. E below obtains that additional consequence
only after the ordinary harmonic-to-current bridge has been proved.

## R1. The precise curve input furnished by C

We only need the following outcome of the proof in Part C. Over an
algebraically closed complete nontrivially valued field $k$, a continuous
finite zero ordinary-current function on a good separated strict
boundaryless pure curve pulls back to a Thuillier harmonic function on
the smooth finite normalization of its reduction. Its reduction is
smooth on one branch outside a locally finite set of rigid points.

These assertions are not being imported from an accepted predecessor.
T2--T13, C1--C4, and the primary proof bodies are reproduced in this
document. In C3, distinct components are separated away from their rigid
intersections before division by their own positive generic lengths;
continuous rigid punctures are removed by C2's bounded-variation cutoffs.
Normalization is an actual analytic isomorphism away from its rigid
conductor set. C4 embeds a connected normal strict affinoid into a smooth
proper algebraic curve over this algebraically closed field and uses its
actual ordinary interior. Wanner Theorem 4.7 is applied there to both
signs. Only inclusion of her algebraic tests into ordinary analytic
tests is used in this direction. No reverse equality of test classes
is claimed. Both signs' Dirichlet comparison gives harmonicity.

For the new construction, it is enough to start with a continuous
function $v$ whose pullback to this normalization is harmonic.
Thus R2--R7 also prove, independently of an original current equation:

**Bridge H16.** On a good separated strict boundaryless pure curve over
an algebraically closed complete nontrivially valued field, every
continuous finite function harmonic on the normalization of its reduction
has the two-sign approximation of R16 and has zero ordinary Hessian
current with its actual generic lengths.

The proof below establishes the last assertion by approximation against
the full ordinary test class; it is not inferred from a recognized
function or from a weakly smooth Hessian.

## R2. Rigid points, including conductor and intersection points

Fix a rigid point $a$ of the actual curve $Z$. Work inside the ordinary
interior of a strict affinoid neighborhood $N$ of $a$.
The finite normalization of $N_{\mathrm{red}}$ is affinoid, and its
finite fibre over $a$ consists of rigid points $a_1,\ldots,a_r$.
They are $k$-rational because $k$ is algebraically closed.
The normalization is rig-smooth over the perfect field $k$, and is
smooth over the boundaryless ordinary open under consideration.

A harmonic germ at a rigid point of a smooth strict curve is constant
on an actual ordinary neighborhood. Here is the neighborhood justification.
The semistable local structure gives a fundamental system of strict
closed disc neighborhoods at such a point (equivalently, at least
strict affinoid neighborhoods with singleton Shilov boundary).
On each sufficiently small such neighborhood the harmonic function is
the graph-harmonic solution with its Shilov boundary values. Thuillier
Lemma 2.3.9 makes the restriction map to that singleton an isomorphism,
so the function is constant. Its ordinary interior contains the rigid
point. Alternatively, the type-(1) part of Thuillier Theorem 2.3.21
identifies the harmonic germ with a finite real sum of unit logarithms.
For a unit $f$, $|f-f(a)|<|f(a)|$ on an actual open neighborhood,
so $|f|=|f(a)|$ there. A finite intersection handles all unit germs.
Both arguments are ordinary-neighborhood statements, not G-cover
constancy. The semistable structure and Lemma 2.3.9 proof bodies appear
in the source appendix; no density assertion supplies this step.

Choose ordinary opens $V_i$ at $a_i$, inside the normalization of $N$,
where $v\circ\nu=v(a)$, and put $V=\bigcup_iV_i$.
The compact complement of $V$ has closed image under the finite map
to $N_{\mathrm{red}}$, and its image excludes $a$. Removing that image
gives an actual ordinary neighborhood $O$ of $a$ with
$\nu^{-1}O\subset V$. Surjectivity implies $v=v(a)$ on $O$.
The reduction immersion is a homeomorphism, so $O$ is also ordinary
open in the actual $N$, with all nilpotents retained.

Goodness, strictness, and nontrivial valuation give an actual strict
affinoid neighborhood $Y\subset O\cap\operatorname{int}_Z N$ of $a$.
The two sequences $u_n^\sigma=\sigma v(a)+4^{-n}$ suffice on this common
$Y$. They are continuous, decreasing, and uniformly convergent.
They are ordinary smooth constants. On $Y^\circ$, Stokes gives zero
Hessian current for a constant, component by component and with every
generic length. In particular they are psh on the actual interior.
This handles every rigid point, not only the singular ones.

## R3. One fixed tree neighborhood at each nonrigid point

At a nonrigid point the locally finite rigid intersection/conductor
set can be excluded on an ordinary open. Its reduction is then one
smooth branch. The nilpotent structure need not be removed from the
chosen neighborhood. Its continuous numerical function $v$ restricts
to a harmonic function on that reduced branch.

We spell out the local finite-tree statement being used. On a smooth
strict boundaryless curve over algebraically closed $k$, inside every
ordinary neighborhood of every point, there is a connected strict
affinoid neighborhood $A$, with the point in $A^\circ$, whose semistable
skeleton is a finite metric tree. A harmonic function on a neighborhood
of $A$ factors as $F\circ\tau$ on a finite semistable refinement, where
$F$ is edgewise affine and the sum of outgoing slopes at every
nonboundary vertex is zero. The same finite tree works for $F$ and $-F$.

Here is a reconstruction from the exact semistable inputs, without
assuming an algebraic open chart covers every analytic germ. First choose
a connected normal strict affinoid neighborhood $Q$ in the smooth branch.
Van der Put Theorem 1.1 and Thuillier Theorem 2.3.8 give an actual
smooth-proper-algebraic-curve domain model and a strictly semistable
formal model of $Q$. All finite separable extensions in these statements
are trivial over $k$. The skeleton is a finite graph embedded in the
curve, with open discs attached to it and open annular tubes on its
edges. This is Thuillier Section 2.2, in particular Theorem 2.2.10,
Corollary 2.2.12, and Propositions 2.2.15--2.2.20. A type-(2) or
type-(3) point can be placed on the skeleton by Lemma 2.2.22(ii);
at type (2) it can be a vertex by (i). Every type-(1) or type-(4)
point off that skeleton has a strict disc neighborhood contained in
an attached disc. The disc description also gives such neighborhoods
directly at type (1) and (4).

At a skeletal point choose a star or segment so short that it has no
circuit and no other old vertex. The entire inverse image under the
retraction has a tree of nonrigid norm points: attached disc trees meet
the central star at only their attachment points. This tree fact on a
disc follows from the nested-disc seminorm description: two norm points
have a unique common containing disc of least radius, and their unique
arc runs up to it and down. Type-(4) points are the ends defined by
nested discs with empty intersection, with the same unique-arc property.
It therefore holds on a star with attached discs, without a residual
genus assumption. At a central type-(2) vertex its tangent directions
are the closed points of its residual curve. Only finitely many are
graph directions. If a prescribed open requires removing further parts
of attached discs, only finitely many directions need truncation:
the compact complement in $Q$ is covered by the open tangent components
and the finitely many complementary graph pieces, and a finite
subcover suffices. Truncate those directions on short collars. Thus
there is an actual ordinary star neighborhood $O$ inside the prescribed
open, whose nonrigid points lie in a tree. The open disc and annular
descriptions are on whole tubes, not just their skeletal arms.

Choose a connected strict affinoid neighborhood inside this $O$ using
the good strict affinoid-neighborhood basis. In the nonreduced situation
choose it in the **actual** space and then reduce it. Its reduction
is a connected smooth strict affinoid $A$ in $O$ and has its own finite
semistable skeleton. That skeleton, embedded in the nonrigid tree of
$O$, cannot contain a circuit, hence is a finite tree. No lifting of
an arbitrary reduced affinoid is assumed. Nilpotent reduction preserves
ordinary topology, and $x\in Y^\circ$ on the actual affinoid $Y$.
In a boundaryless ambient curve, relative interior of a domain is
its topological interior and the composition rule gives
$Y^\circ=\operatorname{Int}(Y)$. The same assertions hold after reduction
(GR Lemma 3.8, or the finite boundary composition rule).

Harmonic functions lie in Thuillier's lisse sheaf: on a strict affinoid
their graph model is the definition of $H(A)$ (2.3.1, 2.3.8--2.3.16).
Proposition 3.2.4 and Lemma 2.2.22 give a finite common refinement
containing all breakpoints. It remains a tree inside $O$. An interior
vertex is of type (2) or (3). Boundary vertices include all of the
Shilov boundary; the boundary set is nonempty for this proper local
affinoid, since the local open star is not an entire proper curve.
For a singleton tree the function is constant and R2's sequences suffice.
Henceforth fix this actual compact $Y$, its reduced tree $\Gamma$,
and the harmonic edgewise affine function $F$ once and for all.

## R4. Rational slopes with positive interior graph mass

We prove the finite-tree approximation used for each sign.
Let $\Gamma$ have at least one edge, and write
$I=V(\Gamma)\setminus\partial\Gamma$. Choose a root
$b\in\partial\Gamma$. Set $\mu(v)=1$ for $v\in I$,
$\mu(b)=-\#I$, and $\mu=0$ at the other boundary vertices.
For an edge directed from a child subtree to the root prescribe
the integer slope $s_e=\sum_{v\text{ in that subtree}}\mu(v)$.
The absence of circuits determines a continuous edgewise affine
$\psi$ with $\psi(b)=0$. At an interior vertex the parent outgoing
slope is $\mu(v)$ plus the sum of its child-subtree slopes; the
child outgoing slopes are their negatives. Therefore
$\Delta\psi(v)=\mu(v)$ at every vertex, including the root by
the zero total sum of $\mu$.

For any $\epsilon>0$ choose $\delta>0$ with
$\delta\|\psi\|_\infty<\epsilon/2$. The graph function
$H=\sigma F+\delta\psi$ has $\Delta H(v)\geq\delta$ on $I$.
Approximate each of its finitely many oriented edge slopes by a rational
number within $\eta$. Integration from the root defines $G$, with
$G(b)=H(b)$. If $L$ is total edge length and $d$ the largest valency,
then

\[
 \|G-H\|_\infty\leq L\eta,\qquad
 |\Delta G(v)-\Delta H(v)|\leq d\eta.
\]

Taking $L\eta<\epsilon/2$ and $d\eta<\delta/2$ proves
$\|G-\sigma F\|_\infty<\epsilon$ and $\Delta G(v)>0$ on $I$.
If $I$ is empty the strict condition is empty; just approximate the
edge slopes. The scalar values of $G$ need not be rational, and edge
lengths need not be rational. Acyclicity is exactly what permits the
independent rational-slope choices to integrate consistently.

## R5. Residual divisors, ordinary unit germs, and fresh collars

Let $z$ be an interior type-(2) vertex of $\Gamma$. Its residual curve
$C_z$ is smooth projective over the infinite algebraically closed
residue field $\widetilde k$. Indeed a monic polynomial over
$\widetilde k$ lifts to an integral monic polynomial over $k$;
its roots in $k$ have norm at most one, and their reductions
give its residual roots. Thus $\widetilde k$ is algebraically
closed, and in particular infinite. The divisor
$B_z=\sum_{e\ni z}d_eG(z)[p_e]$ has rational coefficients and positive
degree $\Delta G(z)$. Choose a finite forbidden set $M_z$ containing all
graph directions and the finitely many directions in which a whole
fresh disc is not available in the fixed $Y$. Such a finite set exists
by the local star description in R3.

For a smooth projective curve of genus $g$ and any positive-degree
rational divisor $B$, choose a denominator-clearing $N$ so large that
$\deg NB\geq2g+1$. The line bundle $L=\mathcal O(NB)$ satisfies
$H^1(L(-p))=0$ for every point $p$: by Serre duality the dual space
is $H^0(\omega\otimes L^{-1}(p))$, whose degree
$2g-1-\deg L$ is negative. The evaluation map $H^0(L)\to L|_p$
is consequently onto. For the finite set $M$, its kernels are proper
linear subspaces of $H^0(L)$. A finite union of such subspaces cannot
cover a vector space over an infinite field: the product of their
nonzero linear equations is a nonzero polynomial, which cannot vanish
at every point by induction on the number of variables. Choose a
section avoiding them. Its effective zero divisor $A$ is disjoint from
$M$ and linearly equivalent to $NB$. Thus
$D_z=B_z-N^{-1}A$ is a rational multiple of a principal divisor.
This proves the residual moving assertion rather than importing the
book packet's lemma. Riemann--Roch/Serre duality and the negative-degree
vanishing used here are standard algebraic foundations, with exactly
the smooth projective curve hypotheses just stated.

We also reconstruct the required principal residual germ. At an interior
type-(2) point of a smooth curve, Thuillier Lemma 2.3.22 identifies the
outgoing-slope map on harmonic germs with
$\ker(\deg:\operatorname{Div}(C_z)_{\mathbb R}\to\mathbb R)$,
with constants as kernel. The image of the subspace generated by
ordinary analytic-unit logarithms is
$\operatorname{Prin}(C_z)\otimes\mathbb R$. Its proof constructs the
graph germs by semistable blowups in the finitely many directions.
For the unit part, a rational residual function can be lifted to a
quotient of analytic germs nonzero at $z$: the residue field of the
analytic local ring is dense in $\mathcal H(z)$ on a good space
(CLD 11.1.10); approximation to error less than one preserves a chosen
norm-one reduction. On shrinking both numerator and denominator
become units. Along a residual direction the local annular expansion
gives the outgoing log-norm slope as the order of the residual
function, with the globally opposite sign if $t=-\log|T|$ is used.
Use the reciprocal for that sign. Outside its finitely many zeros
and poles the slope is zero. This verifies surjectivity of the unit
residual map, not just that its image is contained in the principal
subspace. The full source proof of Lemma 2.3.22 and the annulus unit
expansion of Lemma 2.2.1 are embedded below. Constants may be added
since they are ordinary smooth and harmonic.

We obtain one germ $H_z$, a finite real linear combination of ordinary
unit logarithms plus a constant, with value $G(z)$, the prescribed
graph slopes, slopes $-a_p=-\operatorname{mult}_p(A)/N$ in the fresh
directions, and zero in every other direction. It is ordinary smooth;
$DH_z=0$ as an ordinary form. Stokes on the boundaryless reduced
curve identifies this with zero ordinary Hessian **current**. This
last step uses actual ordinary forms and the canonical positive
calibration (CLD 5.11.1 and 15.7.1), not weak smoothness or an
algebraic-only test class.

Choose one representative of this finite unit tuple on one strict
affinoid neighborhood of $z$. Its logarithms are harmonic and lisse.
A common finite semistable refinement (Thuillier 3.2.4) exhibits each
on a finite graph. Choose a short central star in that refinement.
There are only finitely many extra graph directions. Where the summed
outgoing slope of $H_z$ is zero, the summed function is exactly
constant on the entire short annular tube; in the attached discs
outside this finite graph it is constant by the retraction.
Shrink along the finitely many graph and fresh directions.
Thus, on a single ordinary representative neighborhood, $H_z$ agrees
with $G\circ\tau$ on all original graph collars and all zero-slope
overlaps simultaneously. This is why equality of slopes as germs
does give equality on the **whole** overlaps needed for gluing.
No direction-dependent neighborhoods are intersected infinitely often.

In a fresh open-disc direction use its annular collar coordinate
$t=-\log|T|+c\geq0$, so $H_z=G(z)-a_pt$, $a_p>0$.
Take an even nonnegative smooth function $\rho$ supported in $(-1,1)$
with integral one, and define

\[
 \chi_\eta(r)=\int_{\mathbb R}|r-\eta s|\rho(s)\,ds,
 \qquad m_\eta(s,t)=\frac{s+t+\chi_\eta(s-t)}2.
\]

It is smooth, convex, nondecreasing in each variable, equals
$\max(s,t)$ when $|s-t|\geq\eta$, and lies between that maximum
and that maximum plus $\eta/2$. Indeed convolution smooths the
absolute value, $\chi''_\eta\geq0$, $|\chi'_\eta|\leq1$, Jensen
gives the lower bound, and the triangle inequality gives the upper.
Evenness makes the first moment zero, giving exact equality away
from the transition.

Choose $r_p,\eta_p>0$ with $\eta_p<a_pr_p$, with
$r_p+\eta_p/a_p$ strictly inside the valid short collar, and with
$a_pr_p+\eta_p/2<\epsilon$. On the whole collar replace $H_z$ by

\[
 q_p(t)=m_{\eta_p}\bigl(G(z)-a_pt,G(z)-a_pr_p\bigr).
\]

Near $z$ it equals $H_z$, and for $t>r_p+\eta_p/a_p$ it equals
the constant $G(z)-a_pr_p$. Continue it by that constant throughout
the remaining open-disc component. Its difference from the original
off-graph value $G(z)$ is at most $a_pr_p+\eta_p/2<\epsilon$.
The cap is convex in the ordinary annular unit coordinate, so its
ordinary Hessian form is nonnegative. Green/Stokes against every
nonnegative compact ordinary scalar test proves current psh.
There is no attempt to return to $G(z)$ farther down the disc.
The cap can therefore carry positive curvature without a later
negative-curvature repair. This is also why these approximants are
not harmonic approximants.

## R6. Gluing and error on the fixed affinoid

At an interior type-(3) subdivision point the two affine edge formulas
are $G(z)+\alpha t$ for $t\leq0$ and $G(z)+\beta t$ for $t\geq0$.
The strictly positive outgoing-slope sum says $\beta>\alpha$.
Their maximum is exactly $G$ on that collar. Replace it by
$m_\eta(G(z)+\alpha t,G(z)+\beta t)$, taking
$\eta/(\beta-\alpha)$ smaller than the collar half-length.
It agrees with the old function on open overlaps at both ends,
is ordinary smooth convex, and differs by at most $\eta/2$.

All graph collars around the finitely many vertices can be chosen
disjoint. Fresh directions at distinct vertices are different
components of $Y_{\mathrm{red}}\setminus\Gamma$ and are disjoint.
At every type-(2) vertex all caps equal the one central unit germ
near the vertex. Each cap equals its constant continuation on an
open overlap. On graph arms the central germ equals $G\circ\tau$
on an open overlap. All other local pieces are either affine in an
ordinary annular coordinate or constant. Thus equality on actual
ordinary overlaps glues them into a continuous $g$ on the whole
$Y_{\mathrm{red}}$, ordinary smooth and current-psh on its interior.
Boundary vertices need no smoothing, since that interior excludes
the Shilov boundary. The original boundary values stay continuous:
all replacement graph collars are compactly inside the interior.
No partition of unity is used to glue psh functions. To verify the
global current positivity, partition a compact nonnegative scalar
test using T4's nonnegative ordinary cutoffs subordinate to the
finitely many local descriptions. Only the test is partitioned:
linearity writes $D[g](\psi)$ as the sum of the nonnegative
local pairings $D[g](\theta_i\psi)$.

Use R4 with error $\epsilon/3$, every fresh collar with error
$\epsilon/3$, and every type-(3) replacement with error
$\epsilon/3$. The disjoint supports give

\[
 \|g-G\circ\tau\|_\infty<\epsilon/3,
 \qquad \|g-\sigma v\|_\infty<2\epsilon/3<\epsilon.
\]

There are finitely many modifications for each $\epsilon$; the
fresh directions and collars may vary with $\epsilon$. The fixed
compact domain $Y$ does not vary. If there are no interior vertices,
there are no such replacements and the graph-affine pieces are
already ordinary smooth in the interior. This proves uniform
ordinary-smooth psh approximation for each sign on the common $Y$.

## R7. Actual nilpotents, ordering, and the full test class

The reduction of $Y$ is a smooth connected branch in the nonrigid
case. Let $\ell>0$ be the generic Artinian length of the actual
affinoid algebra along that branch. CLD Proposition 16.6.3 states,
with its supporting proof embedded below,
$\delta_Y=\ell\,i_*\delta_{Y_{\mathrm{red}}}$.
Embedded zero-dimensional pieces contribute no top cycle. The
restriction is valid on every ordinary domain, hence on $Y^\circ$.

An ordinary smooth reduced numerical germ lifts as an ordinary
smooth germ on the actual space. Express it as a smooth coefficient
of finitely many unit logarithms. The quotient of local analytic
rings lifts those unit germs; a lift nonzero at the point is a unit
after an ordinary shrink. Nilpotents have zero seminorm at every
point, so the logarithmic values are identical. Equality of scalar
ordinary sections is equality of their numerical functions by the
ordinary $(0,0)$ moment nullity criterion. Therefore these local
lifts define the same global numerical $g$; there is no line-bundle
or unit-gluing assertion. For any actual nonnegative
$\psi\in A_c^{0,0}(Y^\circ)$, $\psi_0=i^*\psi$ is a nonnegative
compact ordinary smooth reduced test, $i^*D\psi=D\psi_0$, and

\[
 D[g]_Y(\psi)
   =\ell\int_{Y_{\mathrm{red}}^\circ}gD\psi_0\geq0.
\]

This proves positivity against **every actual ordinary scalar test**
using the actual positive generic length. It does not assume an
identification of higher-degree nilpotent form sheaves. At a constant
rigid neighborhood the same calculation is the finite sum over
all reduced components with their possibly unequal positive lengths;
each constant pairing vanishes by Stokes on the component interior.
Consequently reduction has not changed the current being asserted.

Now put $b_n=4^{-n}$. For each sign choose the preceding approximant
$g_n^\sigma$ on the fixed $Y$ with error $<b_n$, and set

\[
 c_n=\sum_{j=n}^\infty(b_j+b_{j+1})=\tfrac53 b_n,
 \qquad u_n^\sigma=g_n^\sigma+c_n.
\]

Since $c_n-c_{n+1}=b_n+b_{n+1}$,
$u_{n+1}^\sigma-u_n^\sigma\leq b_n+b_{n+1}-(b_n+b_{n+1})=0$
pointwise on **all** $Y$, including its boundary. Moreover
$\|u_n^\sigma-\sigma v\|_\infty<(8/3)b_n\to0$.
Constant shifts preserve ordinary smoothness and current psh.
This proves the required ordered sequences without commuting two
local limits or gluing separately chosen positive functions.

For completeness, uniform convergence proves the ordinary bridge:
for every compact ordinary scalar test $\psi$ on $Y^\circ$,

\[
 |D[u_n^\sigma-\sigma v](\psi)|
 \leq\|u_n^\sigma-\sigma v\|_{C(Y)}
          \|(D\psi)_{\mathrm{Rad},Y}\|_{\mathrm{TV}}\longrightarrow0.
\]

The finite variation measure on the right is the actual calibrated
smooth top-form measure. Both $D[v]$ and $D[-v]$ are nonnegative
on all nonnegative ordinary tests. For an arbitrary compact scalar
test take a compact nonnegative smooth cutoff $\theta=1$ near its
support and $M\geq\|\psi\|_\infty$. Both $M\theta+\psi$ and
$M\theta$ are nonnegative compact ordinary tests; their difference
is $\psi$. Linearity makes the pairing of $D[v]$ with each of them
zero, hence with $\psi$ zero. Thus $D[v]=0$ on $Y^\circ$ for the
full ordinary current class. These interiors cover $Z$, proving H16.

By T13, $D[h_C]=0$ with the actual tensor structure; the completed
field is algebraically closed by B's root proof. C1--C4 supply R1's
harmonic normalization over that same $C$. R2--R7 apply to every
point of $U_C$. This proves R16.

# Additional gate: all analytic field-extension current ascent on curves

## E. An ordinary-current consequence of the proved bridge

**Theorem E16.** Under R16's ground-field hypotheses, for every
complete analytic extension $L/K$, possibly transcendental,
$D[h_L]=0$ as an ordinary analytic CLD current on the actual $U_L$.
No ordinary-smooth psh approximants over $L$ itself are claimed.

Here is a proof avoiding a cached weakly smooth/current identification.
Let $F=\widehat{\overline L}$. Extend the $K$-embedding of
$\overline K$ into an algebraic closure of $L$, by adjoining roots
of minimal polynomials. The norm agrees on finite $K$-subextensions
by uniqueness of the extending valuation (T3). Completing extends
it to $C\hookrightarrow F$. B's root proof applies over $L$ as
well, so $F$ is algebraically closed, complete and nontrivially valued.
It is a joint complete field, but $F/C$ need not be algebraic.

Work locally on $U_C$. Its reduced normalization is a finite
surjective map $\nu:N\to U_C$, where $N$ is a smooth strict
boundaryless curve, and $h_C\circ\nu$ is Thuillier harmonic by C.
After base change to $F$, $N_F$ is smooth, strict and locally pure
one-dimensional. Smoothness and relative dimension one follow from
the quasi-smooth Jacobian criterion and absence of boundary under
base change (CLD 11.4.8--9 and GR 2.11(5')); these are standard
analytic foundations with their precise statements in the source
appendix. Finite surjectivity persists. Off the original rigid
conductor/intersection set the reduced normalization was an actual
isomorphism; its scalar pullback is still an isomorphism. The
excluded rigid set base changes to a locally finite set of
$F$-rational rigid points: locally its strict zero-dimensional
algebra is finite over $C$, hence its actual tensor is finite over
$F$, with Artinian lengths retained. The kernel of the reduction
immersion remains nilpotent after this tensor. Thus outside that
set the actual $U_F$ is a nilpotent thickening of the smooth
branch $N_F$, and the topological quotient $N_F\to U_F$ is
finite surjective everywhere. No assertion that arbitrary reduced
base change preserves every embedded structure is needed here.

Thuillier Proposition 2.3.18 preserves the **already harmonic**
function on $N$ under every analytic field extension. Its proof
is Lemma 2.3.5 on semistable graph retractions: the base-change
skeletal map is a surjective G-local isomorphism of weighted
integral polyhedra, and the graph Laplacian is supported on the
boundary before extension exactly when it is so afterwards.
Definitions 2.3.12--2.3.16 give the local sheaf assertion.
These complete proof bodies, including the semistable scalar
structure, are in Appendix S. Therefore $h_F$ is harmonic on
the displayed smooth branches. At the excluded rigid points its
pullback is constant on ordinary neighborhoods of all finitely
many preimages, and finite quotient shrinking as in R2 makes
$h_F$ constant on an actual ordinary neighborhood downstairs.
R3--R7 then apply at every nonrigid point, with the actual
generic lengths, and R2 applies at every rigid point. This proves
$D[h_F]=0$ against all ordinary analytic tests, without assuming
current ascent through $F/C$ or invoking Wanner in reverse.

We check purity also for $U_L$, rather than presuming it from
total dimension. The finite surjective smooth curve cover $N_F$
just described makes $U_F$ locally pure one-dimensional. On
affinoids a finite surjective map is integral, dimensions of its
component images agree by lying over, going up and incomparability;
each minimal target component has a source component over it.
All source components have dimension one. Equivalently, a
zero-dimensional ordinary neighborhood downstairs would have a
nonempty zero-dimensional preimage, impossible in the smooth
pure curve. Nilpotents do not change dimension. Each point of
$U_L$ has an affinoid neighborhood of total dimension at most
one by CLD 11.2.3 and base change from $U$. If a point had
local dimension zero, remove the finitely many one-dimensional
affinoid components and choose a zero-dimensional affinoid
neighborhood there. Its scalar extension to $F$ is nonempty
by scalar surjectivity and has dimension zero by CLD 11.2.3,
contradicting local purity of $U_F$. Hence $U_L$ is pure one.
Goodness, strictness, separatedness and boundarylessness were
already checked under scalar extension in T3/T12.5 using
presentations, diagonal base change and GR 2.11(5'). The same
checks apply to arbitrary complete extensions.

Finally every compact $\psi\in A_c^{0,0}(U_L)$ has compact
pullback to $U_F$: cover its support by finitely many affinoid
ordinary interiors and take the closed inverse image in their
finite union of compact scalar affinoids. Smooth pullback commutes
with $D$, and the canonical measure projection formula
CLD Proposition 15.3.1 gives

\[
 \int_{U_L}h_L(D\psi)_{\mathrm{Rad},L}
 =\int_{U_F}h_F(D\pi_{F/L}^*\psi)_{\mathrm{Rad},F}=0.
\]

The formula is for actual smooth top-form measures on pure curves;
its proof sums finite-flat skeletal degrees, each calculated as
the dimension of its actual Artinian fibre algebra. It has **no**
scalar degree factor, even when $F/L$ is infinite. Its complete
source statement and proof are embedded in Part T's primary
appendix. Pairing with the bounded continuous multiplier on
the compact support proves ordinary-current descent, not a
pullback of an arbitrary continuous current. Since $\psi$ was
arbitrary, E16 follows. This additional all-extension assertion
is downstream of H16 and is logically absent from R16's premises.

# Scope and limitations of the new submission

The new deliverable is R16, together with H16 and E16 as proved
above, not a paper restating recognition or completed-algebraic
transport. Its first-stage sequences are explicit as a construction
on one fixed compact strict affinoid for both signs, smooth/psh
only where promised, on the actual ordinary interior. It includes
singular, nonreduced, imperfect and inseparable ground-field curves.
The catalogue's ordinary-smooth monotone theorem is restricted to
opens of smooth proper algebraic curves over an algebraically
closed field. Here actual local algebraic interiors, finite
normalization, rigid constancy and nilpotent positive generic
lengths extend the two-sign zero-current conclusion to every
original pure analytic curve after $\widehat{\overline K}$.
E16 additionally proves ordinary-current ascent under every
complete analytic extension of such a curve. No identification
of weak smoothness with ordinary smoothness is used.

The original P06.2 includes arbitrary-dimensional nonproduct
analytic germs, so it is **not solved**. P05.2 is not addressed.
No claim is made for regularization of every positive-current
function on arbitrary singular analytic curves, for first-stage
ordinary-smooth approximation over every nonclosed ground field,
or for harmonic ordinary-smooth approximants. The latter can
fail even in the published curve scope; the fresh caps in R5
carry curvature and do not establish that false strengthening.
No arbitrary-radius non-strict product endpoint theorem is
deduced. There is no certification or priority claim; these are
fallible proof drafts, with author audit and reproducible sources.

The programs and evidence are local to this workspace. Rerun
`python3 prepare.py` and `python3 build-and-check.py`. The first
rebuilds this main manuscript from the audited dependency bodies,
this new construction, and newline-bound primary sources. The
second executes bounded diagnostics and two XeLaTeX passes.
`status.json` has exactly the required five keys and records
`status=partial`; the canonical native notes record
`candidate=false`. Compilation and hash checks do not verify
the mathematics. No supervised compute service is exposed in
the installed tools; no resource-heavy computation is needed
or launched. No other model, subagent, network, external message,
installation, credential or older-artifact write is used.

# Appendix S. Exact primary statements and supporting proof bodies

The following quotations are source data, not blanket theorem grants.
Extraction splits only on the newline character, never str.splitlines().
Only PDF page-form-feed markers are removed for display. The main proof uses
the source statements with the exact hypotheses enumerated in T, C, R and E.
Unused source sentences remain source data: the universal moment-dimension
equality in CLD 12.2.4, broad fixed-index noncompact support statement in
15.2.9, and unsupported regular-element-to-S1 inference in 16.7.5 are
not invoked. No closed-curve ambient restriction theorem or Part Q from the
older draft is used in this submission.

## CLD.txt, newline lines 14838–15060

```text

 § 11.1. GÉOMÉTRIE ANALYTIQUE : CONVENTIONS, NOTATIONS,
                       PREMIERS RAPPELS

   On fixe pour toute la suite de l’article un corps ultramétrique complet k ; sa valeur
absolue peut être triviale. On note k ◦ son anneau de valuation. Nous désignerons par ek
                                                         1
le corps gradué résiduel de k (10.8.1). Sa composante k de degré 1 est le corps résiduel
                                                        e
standard de k, c’est-à-dire le corps résiduel de l’anneau local k ◦ .
   Dans ce texte, la notion d’espace k-analytique sera à prendre au sens de Berkovich,
et plus précisément de [9]. Rappelons qu’un polyrayon est une famille (le plus souvent
finie) de nombres réels strictement positifs ; la longueur d’un polyrayon est le cardinal
de son ensemble d’indices. Faisons quelques rappels pour la commodité du lecteur.
11.1.1. — La construction fondamentale sur laquelle repose la géométrie de Berkovich
est la suivante. Soit A un anneau de Banach, c’est-à-dire un anneau A muni d’une norme
sous-multiplicative ∥ · ∥ (on inclut dans la définition le fait que ∥1∥ ⩽ 1, ce qui entraîne
que ∥1∥ = 1 dès que A est non nul) pour laquelle il est complet. À un tel anneau A on
associe son spectre analytique M (A), qui est défini comme l’ensemble des semi-normes
multiplicatives bornées sur A, c’est-à-dire des applications φ : A → R+ vérifiant les
propriétés suivantes :

  – on a φ(0) = 0 et φ(f + g) ⩽ φ(f ) + φ(g) pour tous f, g ∈ A (propriété de semi-
norme) ;
  – on a φ(1) = 1 et φ(f g) = φ(f )φ(g) pour tout f, g ∈ A (multiplicativité) ;
  – il existe un nombre réel c tel que φ(f ) ⩽ c∥f ∥ pour tout f ∈ A (caractère borné de
φ).

Notons qu’on impose que φ(0) = 0 et φ(1) = 1 : si A est nul, M (A) est donc vide.
Cet ensemble M (A) est muni de la topologie la moins fine pour laquelle les applications
φ 7→ φ(f ) sont continues pour tout f ∈ A. L’application φ 7→ (φ(a))a∈A identifie topo-
logiquement M (A) à un fermé de l’espace produit a∈A [0, ∥a∥], si bien que M (A) est
                                                   Q
compact. Si φ appartient à M (A), son noyau est un idéal premier de A, et l’application
298                   CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

φ 7→ ker φ de M (A) vers Spec A est continue. Son image contient tous les idéaux maxi-
maux de A (c’est ce qui est réellement démontré dans la preuve du théorème 1.2.1 de
[8]) ; en particulier M (A) est non vide dès que A est non nul.
   En général, on note typiquement plutôt x que φ un élément de M (A), en y pensant
comme à un point. Soit x ∈ M (A). La semi-norme multiplicative x induit une valeur
absolue sur le corps des fractions de l’anneau intègre A / ker x, corps des fractions dont
le complété est noté H (x). L’application composée A → A / ker x → H (x) sera notée
f 7→ f (x), et la valeur absolue du corps complet H (x) sera notée |·| ; avec ces conventions
on a x(f ) = |f (x)| pour toute f ∈ A et nous utiliserons sauf exception la notation de
droite. Cette construction est fonctorielle : tout morphisme borné A → B d’anneaux de
Banach induit par composition une application continue de M (B) vers M (A).
   La semi-norme spectrale de A est la semi-norme ρ commutant aux puissances définie
par les formules
                     ρ(f ) = sup |f (x)| = lim inf ∥f n ∥1/n = inf ∥f n ∥1/n
                              x∈M (A)            n→∞                n→∞


(voir [8], 1.3, pour les deux dernières égalités). Nous désignerons par A◦ (resp. A◦◦ )
l’ensemble des éléments f de A tels que ρ(f ) ⩽ 1 (resp. ρ(f ) < 1), et par A     e l’anneau
gradué résiduel de A (10.8.1) relativement à ρ. Sa composante A     e1 est l’anneau résiduel
            ◦    ◦◦
standard A /A .
   Supposons maintenant que A est une k-algèbre et que sa norme est une norme de k-
espace vectoriel. Dans ce cas λ 7→ |λ(x)| définit pour tout x ∈ M (A) une valeur absolue
sur k bornée relativement à la valeur absolue structurale de k, ce qui entraîne que
|λ(x)| = |λ| pour tout λ : la semi-norme x induit donc la valeur absolue structurale de k,
et (H (x), |·|) est une extension de (k, ·). Comme la valeur absolue de k est ultramétrique,
celle de H (x) l’est aussi (une valeur absolue |·| étant ultramétrique si et seulement si
|n| ⩽ 1 pour tout n ∈ Z). On a donc dans ce cas |(f + g)(x)| ⩽ max(|f (x)|, |g(x)|) pour
tout f, g dans A, puis ρ(f + g) ⩽ max(ρ(f ), ρ(g)) (comme on le voit en faisant varier x).
11.1.2. — Soit n un entier. Pour tout polyrayon r = (r1 , . . . , rn ), nous désignerons
         −1             −1
      P 1 T1 , . . . ,νrn Tn } la sous-algèbre
par k{r
                                         ν
                                                   de k[[T1 , . . . , Tn ]] formée des séries formelles
                                                  ν1      νn
                                                                                                 P
f =      ν∈N n a ν T    telles que a ν r   = a ν 1 . . . rn converge vers 0 lorsque |ν| =
                                                r                                                  |νj |
tend vers +∞. On la munit de la norme multiplicative ultramétrique définie par ∥f ∥ =
max|aν |rν . Pour abréger les notations, on notera aussi k{r−1 T } cette algèbre. C’est une
algèbre de Banach dont tous les idéaux sont fermés et de type fini.
   Soit maintenant A une k-algèbre de Banach commutative (par convention, dans cet
ouvrage, les normes de k-algèbres seront toujours ultramétriques). On dit que A est une
algèbre k-affinoïde s’il existe un entier n, un polyrayon (r1 , . . . , rn ) et une surjection de
k{r−1 T } vers A telle que la norme de A soit équivalente à la norme quotient correspon-
dante. On dit que A est strictement k-affinoïde si l’on peut de plus prendre rj = 1 pour
tout j. Pour que A soit strictement k-affinoïde, il suffit en fait que l’on puisse prendre
les rj de torsion modulo |k × | ([20] 6.1.5/4).
   Une k-algèbre de Banach A est dite affinoïde s’il existe une extension valuée com-
plète K de k telle que A soit une algèbre K-affinoïde.
   Si A est une k-algèbre affinoïde l’application continue naturelle de M (A) vers Spec A
est surjective ([9], Proposition 2.1.1).
   Soit A une k-algèbre affinoïde et soit ρ sa semi-norme spectrale. L’algèbre A est
noethérienne, et ses idéaux sont fermés. Pour tout f ∈ A on a ρ(f ) = 0 si et seulement
     § 11.1. GÉOMÉTRIE ANALYTIQUE : CONVENTIONS, NOTATIONS, PREMIERS RAPPELS             299

si f est nilpotent. En particulier, ρ est une norme si et seulement si A est réduite et si
c’est le cas, ρ est équivalente à la norme structurale de A.
Exemple 11.1.3. — Soit r = (ri ) un polyrayon de longueur finie. Soit T P        = (Ti ) une
famille d’indéterminées et soit kr la k-algèbre constituée des séries formelles I∈Zn aI T I
à coefficients
           P dans    k, où |aI | · rI tend vers zéro quand |I| tend vers l’infini, munie de
la norme      aI T 7→ max|aI | · rI . La k-algèbre normée kr est une k-algèbre affinoïde :
                  I

elle est en effet isomorphe à k{r−1 T, rS}/(ST − 1). Sa norme est multiplicative ([48],
1.2.1). Supposons de plus que r soit k-libre, c’est-à-dire que les ri soient Q-linéairement
indépendants dans Q ⊗Z (R×           ×
                                + /|k |). Dans ce cas kr est un corps ([48], 1.2.2), et c’est
donc à la fois une extension complète de k et une algèbre k-affinoïde.
Remarque 11.1.4. — Soit A = k{r−1 T } une algèbre k-affinoïde, où r = (ri ) est un
polyrayon de longueur finie. Choisissons un ensemble J d’indices tel que le polyrayon
s := (rj )j∈J soit k-libre et quiQsoit maximal pour cette propriété. Chacun des ri est
alors de torsion modulo |k × | · j∈J riZ , si bien que la ks -algèbre de Banach A⊗
                                                                                 b k ks est
strictement ks -affinoïde.
11.1.5. — Soit A une algèbre k-affinoïde ; posons X = M (A ). Une partie V de X
est appelée un domaine affinoïde de X si le foncteur qui envoie une k-algèbre de Ba-
nach affinoïde B sur l’ensemble des morphismes bornés de A vers B tels que l’image
de M (B) soit contenue dans V est représentable par une algèbre k-affinoïde AV . Si c’est
le cas, M (AV ) ≃ V .
   Un système rationnel d’inéquations sur X est une combinaison booléenne d’inégalités
qui est de la forme
                     |f1 | ⩽ λ1 |g| et |f2 | ⩽ λ2 |g| et . . . et |fn | ⩽ λn |g|
où g et les fi sont des fonctions analytiques sur X sans zéro commun, et où les λi sont
des réels.
  Si β est un système rationnel d’inéquations sur X, on notera β̊ le système défini à partir
de β en remplaçant toutes inégalités larges par les inégalités strictes correspondantes.
  Soit
                    β : |f1 | ⩽ λ1 |g| et |f2 | ⩽ λ2 |g| et . . . et |fn | ⩽ λn |g|
un système rationnel d’inéquations sur X.
  On qualifiera de rationnel le lieu de X défini par un tel système d’inéquations. C’est
un domaine affinoïde de X, avec
                          AV ≃ k{T1 /λ1 , . . . , Tn /λn }/(fi − Ti g)i .
Notons que si g s’annulait en un point de V , il en irait de même de chacune des fi ; en
conséquence, g|V est inversible.
  Tout point de X possède une base de voisinages rationnels, en particulier une base
de voisinages affinoïdes. Plus précisément, pour tout x ∈ X et tout voisinage ouvert U
de x, il existe un système rationnel d’inéquations β dont le lieu de validité est contenu
dans U , et tel que x satisfasse β̊.
11.1.6. — Le théorème de Gerritzen-Grauert affirme que tout domaine affinoïde de X
est réunion finie de domaines rationnels (pour le cas non strict, voir [47], lemme 2.4 ;
pour une preuve directe, voir aussi [128], théorème 3.1). Il en résulte que si x est un
point de X situé sur un domaine affinoïde V de X, le corps résiduel complété H (x) ne
dépend pas du fait que l’on voie x comme appartenant à V = M (AV ) ou à X = M (A).
300                CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

11.1.7. — À partir des espaces affinoïdes, Berkovich définit dans [9] la catégorie des
espaces k-analytiques par un procédé de recollement un peu délicat qu’il serait trop
long de décrire ici en détail ; nous allons tout de même rappeler quelques faits. Suivant
Berkovich, si X est un espace topologique et si (Xi ) est une famille de parties de X,
nous dirons que les Xi constituent
                           S         un G-recouvrement de X si tout point x de X possède
un voisinage de la forme i∈J Xi où J est fini et où x ∈ Xi pour tout i ∈ J. Si l’on
ne s’astreint à recoller que des espaces strictement affinoïdes, on obtient la classe des
espaces strictement k-analytiques.
   Soit X un espace k-analytique. C’est en particulier un espace topologique dont tout
point possède une base de voisinages compacts (mais X n’est pas nécessairement lo-
calement compact puisqu’un espace topologique localement compact est par définition
séparé, et que ce n’est pas forcément le cas de X). L’espace X possède par ailleurs une
classe distinguée de partie compactes, ses domaines affinoïdes (si X = M (A ), les do-
maines affinoïdes de X sont précisément ceux décrits au 11.1.5 ci-dessus). Un domaine
analytique de X est une partie de X qui est G-recouverte par les domaines affinoïdes
qu’elle contient. Tout domaine affinoïde de X est un domaine analytique de X ; plus
généralement, tout compact de X qui est une union finie de domaines analytiques de
X est un domaine analytique. Et tout ouvert de X (et notamment X lui-même) est un
domaine analytique. En particulier, tout point x de X possède un voisinage compact
qui est une réunion finie de domaines affinoïdes contenant x. Les espaces définis dans [8]
sont ceux qui sont qualifiés de bons dans [9], c’est-à-dire ceux dont tout point admet un
voisinage affinoïde (et donc une base de voisinages affinoïdes.) Tout domaine analytique
de X est une partie localement fermée de X : l’intersection d’une famille finie de do-
maines analytiques est un domaine analytique ; la réunion d’une famille localement finie
de domaines analytiques fermés est un domaine analytique.
   Tout domaine analytique V de X hérite d’une structure canonique d’espace analy-
tique, et d’un morphisme V ,→ X dont l’application sous-jacente est l’inclusion. Tout
morphisme f : Y → X se factorisant ensemblistement par V se factorise en fait unique-
ment par la structure analytique de V .
11.1.8. La G-topologie. — Soit X un espace k-analytique. En plus du site topolo-
gique sur X on définit un second site plus fin, noté XG . Ses objets sont les domaines
analytiques de X, ses flèches sont les inclusions, et ses familles couvrantes sont les G-
recouvrements. La topologie de ce site est appelée la G-topologie de X.
  Comme tout ouvert de X est un domaine analytique et comme tout recouvrement
ouvert est un G-recouvrement, on dispose d’un morphisme de site canonique π : XG →
X. L’unité d’adjonction id → π∗ π ∗ est un isomorphisme ([9], p. 26).
  Le site XG est annelé. Nous noterons OX le faisceau structural de XG . Sauf mention du
contraire, lorsque nous parlerons de faisceaux cohérents sur X, il s’agira plus précisément
de OX -module cohérents sur XG . Précisons que le faisceau OX ainsi que sa restriction
au site topologique usuel de X sont cohérents ([49], lemme 0.1 ; pour la correction d’une
petite erreur dans la preuve, signalée par Jérôme Poineau, voir [52], 1.1.1). Si X = M (A)
alors OX (X) = A.
  Tout morphisme f : Y → X entre espaces analytiques est en particulier un morphisme
de sites annelés : si V est un domaine analytique de Y alors f −1 (V ) est un domaine
analytique de X et l’on dispose d’un morphisme f ∗ : OX (V ) → OY (f −1 (V )). Si X est
un espace k-affinoïde M (A) et si Y est un espace affinoïde M (B) sur une extension de
     § 11.1. GÉOMÉTRIE ANALYTIQUE : CONVENTIONS, NOTATIONS, PREMIERS RAPPELS               301

k, l’application f 7→ f ∗ établit une bijection entre l’ensemble des k-morphismes de Y
vers X et l’ensemble des morphismes bornés de k-algèbres de A vers B.
   Si X = M (A) est un espace k-affinoïde et si M est un A-module de type fini, le
faisceau Mf sur XG associé au préfaisceau V 7→ M ⊗A OX (V ) est cohérent. Le foncteur
M 7→ M f établit une équivalence entre la catégorie des A-modules de type fini et celle
des faisceaux cohérents sur X, de quasi-inverse F 7→ F (X) (cf. [9] ; ce résultat est dû
à Kiehl dans le cas strictement affinoïde).
   Lorsque X est bon, le foncteur π∗ induit une équivalence de catégories entre faisceaux
cohérents sur XG et faisceaux cohérents sur X, et qu’un faisceau cohérent F sur XG est
localement libre si et seulement si c’est le cas de π∗ F ([9], 1.3.4 ; notons que la définition
de faisceau cohérent qu’il utilise dans cette proposition est ad hoc, mais qu’elle coïncide
bien en fait avec la notion usuelle au vu de la cohérence des faisceaux structuraux sur
les deux sites annelés en jeu).
11.1.9. Produits fibrés, extension des scalaires. — La catégorie des espaces k-
analytiques admet des produits fibrés. Si A → B et A → C sont deux morphismes
d’algèbres k-affinoïdes, M (B) ×M (A) M (C) = M (B ⊗     b A C).
   Si L est un extension complète de k on dispose d’un foncteur d’extension des scalaires
X 7→ XL de la catégorie des espaces k-analytiques vers celle des espaces L-analytiques.
Si X = M (A) alors XL = M (A⊗       b k L). En général on dispose d’un morphisme naturel
de sites annelés de XL vers X, qui est surjectif (cf. [48], 0.5).
   Supposons X bon, soit y un point de XL et soit x son image sur X. Le morphisme
naturel de Spec OXL ,y vers Spec OX,x est plat à fibres localement d’intersection complète,
et à fibres géométriquement régulières si L est analytiquement séparable sur k ; c’est le
théorème [52], th. 2.6.5. La notion d’extension analytiquement séparable est définie
dans [49] (définition 1.6). Une extension finie de k est analytiquement séparable si et
seulement si elle est séparable ; si r est un polyrayon de longueur finie et k-libre, kr est
une extension analytiquement séparable de k ; si k est parfait, toute extension complète
de k est analytiquement séparable.
   On définit la catégorie des espaces analytiques au-dessus de k comme la catégorie dont
```

## CLD.txt, newline lines 15287–15355

```text
topologie de V induite par la topologie de Zariski de X, et en général strictement plus
fine.
   Si E est une partie de X et si (Xi ) est un G-recouvrement de X par des domaines
analytiques, alors E est un fermé (resp. un ouvert) de Zariski de X si et seulement si
E ∩ Xi est un fermé (resp. un ouvert) de Zariski de Xi pour tout i ([49], Prop. 4.2.1).
306                  CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

   Une immersion fermée (1) est un morphisme d’espaces k-analytiques f : Y → X se
factorisant par un isomorphisme entre Y et un sous-espace analytique fermé de X. Une
immersion fermée préserve les corps résiduels complétés.
   Un morphisme d’espaces k-analytiques f : Y → X est dit séparé si sa diagonale
δ : Y → Y ×X Y est une immersion fermée, et X est dit séparé si le morphisme structural
de X vers M (k) est séparé. La séparation dans ce sens entraîne la séparation topolo-
gique, mais la réciproque est fausse : le recollement de deux copies du disque unité le
long du domaine affinoïde décrit par l’égalité |T | = 1 est topologiquement séparé car le
domaine de recollement est fermé, mais n’est pas séparé.
11.2.3. Dimension. — On dispose d’une théorie de la dimension en géométrie ana-
lytique, due à Berkovich, au sujet de laquelle on pourra consulter le chapitre 2 de [8], la
fin du paragraphe 1.2 de [9] ou encore l’article [48].
   Soit X un espace k-analytique. Sa dimension (k-analytique) est définie comme suit.
Commençons par le cas affinoïde. Écrivons X = M (A) et choisissons une extension
complète L de k telle que AL := A⊗        b k L soit strictement L-affinoïde. La dimension de
Krull de AL ne dépend alors pas de L ([48], 1.5) et est appelée dimension de X. (Si X est
strictement k-affinoïde sa dimension est donc simplement sa dimension de Krull relative
à sa topologie de Zariski.) On a par construction dim Xred = dim X et dim XL = dim X
pour toute extension complète L de k.
   Si Y est un fermé de Zariski de X, le choix d’une structure de sous-espace analytique
fermé sur Y , c’est-à-dire d’un idéal I de A définissant Y , fait de Y un espace affinoïde
(identifié à M (A/I)). Sa dimension ne dépend pas du choix de I, et nous parlerons donc
de la dimension de Y sans spécifier I.
   Soit X1 , . . . , Xn les fermés de Zariski de X correspondant aux idéaux premiers mini-
maux de A. Si V est un domaine affinoïde de X on a alors dim V = supi,V ∩Xi ̸=∅ dim Xi .
En particulier dim V ⩽ dim X = supi dim Xi . Si x est un point de X on définit dimx X
comme le minimum des dim V où V est un domaine affinoïde de X contenant x ; c’est
aussi supi,x∈Xi dim Xi . Il vient dim X = supi dim Xi = supx∈X dimx X.
   Ne supposons plus X affinoïde. Si x est un point de X, on définit la dimension locale
dimx X de X en x comme le minimum des dim V où V parcourt l’ensemble des domaines
affinoïdes de X contenant x, et l’on pose alors dim X = supx∈X dimx X. Cette définition
est compatible avec la précédente lorsque X est affinoïde. Si V est un domaine analytique
de X on a dimx V = dimx X pour tout x ∈ V , si bien que dim V ⩽ dim X. Si d est un
entier on dit que X est purement de dimension d si dimx X = d pour tout x ∈ X. Si
c’est le cas X est ou bien vide, ou bien de dimension d.
   Pour tout point x de X on pose
(11.2.3.1)
                                                   1
      dk (x) = degtr(H      (x)/k̃) = degtr(H        k 1 ) + dimQ Q ⊗Z (|H (x)× |/|k × |) ,
                                                                                         
                         ^                  ^  (x) /e
où la seconde égalité provient de 10.1.9 ; Berkovich le note d(κ(x)/k) ou d(H (x)/k)
L’intérêt majeur de cet invariant est l’égalité dim(X) = supx∈X dk (x) ([9], Lemma 2.5.2).
   Soit Y un fermé de Zariski de X. Munissons-le d’une structure de sous-espace analy-
tique fermé. La dimension de l’espace analytique correspondant ne dépend que de Y , et
(1)
   Dans l’expression « immersion fermée » ou dans l’expression « sous-espace analytique fermé », l’ad-
jectif « fermé » fait implicitement référence à la topologie de Zariski. Ainsi, en général, un domaine
analytique fermé V de X n’est pas un sous-espace analytique fermé de X, et le morphisme canonique
V ,→ X n’est pas une immersion fermée.
                 § 11.2. TOPOLOGIE DE ZARISKI, THÉORIE DE LA DIMENSION                     307

pas de la structure en question (par exemple au vu de l’égalité ci-dessus, ou par réduc-
tion au cas affinoïde via la description des domaines analytiques de Y ). On pourra donc
parler de la dimension de Y sans spécifier la structure dont on le munit.


Remarque 11.2.4. — Insistons sur le fait que la dimension considérée ici est en fait
une dimension relative au corps de base k, même si nous ne rappelons pas cette dépen-
dance. Considérons par exemple l’algèbre de Banach kr associée à un polyrayon k-libre
(r1 , . . . , rn ) (exemple 11.1.3). C’est une extension complète de k. En tant qu’algèbre kr -
affinoïde elle est stricte, et sa dimension de Krull est nulle. Par conséquent la dimension
```

## CLD.txt, newline lines 15567–15604

```text
compact si l’image réciproque de toute partie compacte est compacte. Comme tout point
possède un voisinage compact, cela revient à dire que f est topologiquement propre et
topologiquement séparé.
  Suivant [9] (1.5.3), un morphisme est dit propre s’il est compact et sans bord.
11.4.4. Morphismes finis. — Soit A une algèbre k-affinoïde. Une A-algèbre de Ba-
nach finie est une A-algèbre de Banach B qui est finie comme A-algèbre, et dont la
norme est équivalente à la norme quotient induite par une présentation finie An → B
du A-module B. Dans ce cas la norme de B est en fait équivalente à la norme quotient
associée à n’importe quelle présentation finie du A-module B (c’est une conséquence de
[8], Prop. 2.1.9). Toute A-algèbre de Banach finie est k-affinoïde (combiner [20], Prop.
6.1.3/4 et [8], Cor. 2.1.8). Le foncteur d’oubli de la norme induit une équivalence de
catégories entre A-algèbres de Banach finies et A-algèbres finies(2) ([8], Prop. 2.1.12).
   Soit f : Y → X un morphisme entre espaces k-analytiques. Si X et Y sont affinoïdes,
on dit que f est fini si f ∗ fait de O(Y ) une O(X)-algèbre de Banach finie ; cela revient
à demander que f soit sans bord ([8], Cor. 2.5.13). En général (si l’on ne suppose plus
X et Y affinoïdes) les assertions suivantes sont équivalentes : ([9], Cor. 1.3.7).
  (i) Il existe un G-recouvrement (Xi ) de X par des domaines affinoïdes tels que pour
tout i, l’image réciproque f −1 (Xi ) soit affinoïde et que le morphisme induit de f −1 (Xi )
vers Xi soit fini
  (ii) Pour tout domaine affinoïde V de X l’image réciproque f −1 (V ) est affinoïde et le
morphisme induit de f −1 (V ) vers V est fini.

  Si |k × | ̸= {1} et si A est strictement k-affinoïde, on déduit de [8], Prop. 2.1.1 et [20], Thm. 6.1.3/1
(2)

que toute A-algèbre de Banach qui est finie comme A-algèbre est une A-algèbre de Banach finie. Par
contre si k est trivialement valué et si 0 < r < s < 1, le morphisme continu naturel de k{T /s} vers
k{T /r} est bijectif (sa source et son but s’identifient tous deux à k[[T ]]) mais sa réciproque n’est pas
bornée, si bien que k{T /s} n’est pas une k{T /r}-algèbre de Banach finie).
312                CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

On dit que f est fini si elles sont satisfaites ; cette définition est compatible avec la
précédente si X et Y sont affinoïdes. Un morphisme fini est sans bord.
  La classe des morphismes finis est stable par composition et changement de base
analytique sur k, et la propriété d’être fini est G-locale au but.
  Soit y un point de Y . On dit que f est fini en y s’il existe un voisinage analytique
U de f (y) dans X et un voisinage analytique V de y dans f −1 (U ) tel que f induise un
morphisme fini de V vers U . Si c’est le cas le point y appartient à Int(Y /X), et si de
```

## CLD.txt, newline lines 16122–16143

```text
  Supposons réciproquement que (X, ^   x) soit l’image réciproque d’un ouvert affine de
P ^ 1 e1 . Il résulte de la preuve du lemme 3.5.1 de [52] qu’il existe un entier n, un
 H (x) /k
point y du polydisque unité D de dimension n et un morphisme sans bord de (X, x) vers
(D, y). Lorsque la valeur absolue de k n’est pas triviale, y possède une base de voisinages
strictement affinoïdes dans D, si bien que (X, x) possède un représentant strictement
affinoïde.
11.7.7. — Supposons que la valeur absolue de k n’est pas triviale. On déduit alors
des résultats rappelés au 11.7.6 que (X, x) est strictement k-analytique si et seulement
   ^
si (X, x) est strict, cf. [52, Lemma 3.5.2]. Mentionnons incidemment que si (X, x) est
                         ^
à la fois bon et strict, (X, x) est à la fois affine et strict, donc est l’image réciproque
d’un ouvert affine de P ^ 1 e1 (10.5.5) ; il découle alors de 11.7.6 que le germe (X, x) est
                        H (x) /k
strictement affinoïde. Autrement dit tout point d’un bon espace strictement k-analytique
admet un voisinage strictement affinoïde ce qui, à notre connaissance, ne figurait pas
jusqu’ici explicitement dans la littérature.
   Notons que l’hypothèse que la valeur absolue de k n’est pas triviale est indispensable
à la validité des énoncés ci-dessus. Supposons en effet que |k × | = {1}, et soit X l’ouvert
de A1k défini par les inégalités 0 < |T | < 1 ; il est sans bord, si bien que pour tout x ∈ X
              ^
```

## CLD.txt, newline lines 3750–3920

```text
3.3.8. — Soit ω une G-forme (resp. une forme) de type (p, q) à coefficients dans G
sur X. Si V est un domaine de X, une G-tropicalisation de ω sur V est la donnée d’une
carte G-tropicale (f : V → E, P ) et d’une forme α ∈ GPp,q (P ) telle que ω = f ∗ α.
  On dira que ω est G-tropicale si elle admet une G-tropicalisation sur X.
  Si V est un domaine de X tel que ω possède une G-tropicalisation sur V , nous dirons
aussi que V G-tropicalise ω.
  Soit V un domaine compact de X qui G-tropicalise ω, et soit (f V → E, P, α) une
G-tropicalisation de ω|V . Comme f (V ) est un sous-espace paralinéaire de E, (f : V →
E, f (V ), α|f (V ) ) est encore une G-tropicalisation de ω|V ; une telle G-tropicalisation sera
simplement notée (f : V → E, α) : lorsque V est compact, l’omission du sous-espace
paralinéaire P signifie qu’il est égal à f (V ).

Remarque 3.3.9. — Soit H une classe de coefficients contenant G . Observons que
les G-formes à coefficients dans G s’identifient à des G-formes à coefficients dans H .
   En effet, le G-préfaisceau Gpfp,q sur XG s’identifie à un sous-G-préfaisceau de Hpfp,q , de
sorte que le G-faisceau GXp,qG sur X s’identifie alors à un sous-G-faisceau de HXp,qG
                                                                                       . Ces
identifications sont compatibles avec les constructions faites dans ce paragraphe.

3.3.10. — Le faisceau GXG := GX0,0G est un faisceau en R-algèbres et les faisceaux GXp,qG
sont des GXG -modules. Leur somme directe GX∗,∗G = p,q GXp,qG est un faisceau en algèbres
                                                   L

bigraduées commutatives : si ω est de type (p, q) et ω ′ de type (p′ , q ′ ), alors
                                                    ′     ′
                                ω ′ ∧ ω = (−1)(p+p )(q+q ) ω ∧ ω ′ .
3.3.11. — Le G-préfaisceau Gpf∗,∗ est naturellement muni d’un opérateur J qui s’étend
au faisceau GX∗,∗G . Ce sont des morphismes d’algèbres. On dit qu’une section ω de GXp,qG
est symétrique si p = q et si Jω = ω.
    Soit H une classe de coefficients telles que les dérivées partielles des fonctions de G
existent et appartiennent à H . On dispose alors d’opérateurs différentiels d′ et d′′ de
Gpf∗,∗ dans Hpf∗,∗ ; ils induisent des opérateurs différentiels de GX∗,∗G dans HX∗,∗
                                                                                  G
                                                                                     , caractérisés
par les relations
                               d′ f ∗ α = f ∗ d′ α, d′′ f ∗ α = f ∗ d′′ α,
                                 § 3.4. NULLITÉ DES G-FORMES                             81

pour toute carte G-tropicale (f : U → E, P ) et toute forme α de type (p, q) à coeffi-
cients dans G sur P . Les différentielles vérifient la règle de Leibniz : si ω et ω ′ sont
respectivement de type (p, q) et (p′ , q ′ ), on a
(3.3.11.1)               d′ (ω ∧ ω ′ ) = d′ ω ∧ ω ′ + (−1)p+q ω ∧ d′ ω ′ ,
et de même pour d′′ (ω ∧ ω ′ ).
   Si G ⊂ C 2 , ces opérateurs vérifient d′ d′ = d′′ d′′ = 0.
3.3.12. — Cette construction est fonctorielle. Plus précisément, si f : Y → X est un
morphisme d’espaces G-tropicaux, on dispose de morphismes de faisceaux
                                     f ∗ : GX∗,∗G → f∗ (GY∗,∗
                                                           G
                                                              )
sur XG qui sont des morphismes d’anneaux gradués, commutent aux dérivations d′ et
d′′ (lorsqu’elles existent) et à l’opérateur J.
   Lorsque le contexte rend évident le morphisme f , on se permettra parfois de noter
ω|Y l’image dans GYp,q G
                         (Y ) d’une G-forme ω ∈ GXp,qG .
3.3.13. — Soit (p, q) un couple d’entiers naturels. Soit Σ une partie paralinéaire de X
et soit j l’inclusion de Σ dans X. C’est un morphisme d’espaces G-tropicaux. On dispose
donc d’un morphisme de faisceaux de FXp,qG dans j∗ FΣp,qG . On notera ω 7→ ω|Σ l’image
d’une forme ω et on dira que c’en est la restriction à Σ.
   Concrètement, cette restriction se calcule de la façon suivante.
   Soit V un domaine de X, soit (f : V → E, P ) une carte G-tropicale sur V , et soit
α ∈ FPp,q (P ). Alors Σ ∩ V est une partie paralinéaire de V , l’application f : Σ ∩ V → E
est paralinéaire et son image est contenue dans P , l’image réciproque f ∗ α de α est
une forme de type (p, q) sur l’espace paralinéaire Σ ∩ V . Par définition de l’ensemble
Fpfp,q (V ) comme limite inductive, la forme f ∗ α ne dépend que de la classe de f ∗ α dans
cet ensemble. Cette construction définit un morphisme de préfaisceaux de FX,pf     p,q
                                                                                       dans
j∗ FΣp,q .
   Par passage aux faisceaux associés, on en déduit le morphisme de restriction de FXp,qG
dans j∗ FΣp,qG .
3.3.14. — Soit f : Y → X un morphisme d’espaces G-tropicaux, soit T une partie
paralinéaires de Y et soit Σ une partie paralinéaire de X telle que f (Σ) ⊂ T. Pour toute
forme ω ∈ FXp,qG (X), on a (f ∗ ω)|T = (f |T )∗ (ω|Σ ).
   Nous appliquerons notamment cette remarque lorsque Y est un domaine de X et
T = Σ ∩ Y , ou bien lorsque Y = X et T est une partie polyédrale de Σ.



                          § 3.4. NULLITÉ DES G-FORMES

Proposition 3.4.1. — Soit X un espace G-tropical compact, soit f : X → E une carte
G-tropicale, soit P un sous-ensemble paralinéaire de E contenant f (X) et soit α ∈
GPp,q (P ). Les assertions suivantes sont équivalentes :
   a) La restriction de α au sous-espace paralinéaire f (X) est nulle ;
   b) La section globale f ∗ α de Gpfp,q est nulle.
Démonstration. — L’hypothèse (1) entraîne que l’image de α dans la carte tropicale
(f, f (X)) est nulle, de sorte que (2) vaut. Supposons que (2) est vérifiée et prouvons (1).
82                          CHAPITRE 3. ESPACES G-TROPICAUX

   On peut remplacer P par f (X). Par définition, il existe une carte G-tropicale g : X →
F , une morphisme affine p : F → E tel que p ◦ g = f , et un sous-espace paralinéaire Q
de F contenant g(X) tels que p(Q) ⊂ P et p∗ α = 0 dans GQp,q (Q). On peut aussi
remplacer Q par g(X) ; on a alors p(Q) = P .
   Le morphisme de Q sur P induit par p possède G-localement des sections. D’après
le corollaire 1.8.5, il existe une décomposition cellulaire (Ci ) de P et, pour tout i, une
section de ptrop sur Ci à valeurs dans Q. Puisque p∗ α = 0, on a donc α|Ci = 0 pour
tout i. Par suite, α = 0.

Corollaire 3.4.2. — Soit X un espace G-tropical compact, soit ω ∈ Gpfp,q (X) et soit
(Xi ) un G-recouvrement de X. Supposons que pour tout i, la restriction de ω à Xi soit
nulle ; alors ω = 0.
Démonstration. — Tout G-recouvrement admet un G-recouvrement plus fin formé de
domaines compacts. Comme X est compact, cela permet de supposer que le recouvre-
ment (Xi ) est formé d’un nombre fini de domaines compacts. Par définition du préfais-
ceau Gpfp,q , il existe une carte G-tropicale f : X → E, un sous-espace paralinéaire P de E
contenant f (X), et une forme α ∈ GPp,q (P ) tels que ω = f ∗ α.
   Il résulte que de la proposition 3.4.1 que α|f (Xi ) = 0 pour tout i. Comme f (X) est la
réunion des f (Xi ), la forme α est nulle sur f (X) (lemme 1.9.2). On a donc ω = f ∗ α =
0.

Remarque 3.4.3. — L’hypothèse que X est compact est cruciale pour le corol-
laire 3.4.2.
   Prenons pour espace G-tropical l’ensemble X = R, muni de la topologie discrète, et
pour carte l’application identique f : R → R. Soit α la forme d′ x sur R. Soit g : X → Rn
une carte qui domine la carte f , et soit p : Rn → R une application affine telle que
f = p ◦ g. Alors, p est surjective, donc p∗ α ̸= 0. Cela prouve que la section f ∗ α de Gpf1,0
n’est pas nulle. En revanche, pour tout t ∈ R, le singleton Vt = {t} est un domaine de X
de tropicalisation Pt = {t} et α|Pt = 0, si bien que α|Vt = 0. Comme ces domaines Vt
forment un G-recouvrement de X, cela montre que le préfaisceau Gpf1,0 n’est pas séparé.
Proposition 3.4.4. — Soit X un espace G-tropical, soit f : X → E une carte G-
tropicale, soit P un sous-espace paralinéaire de E contenant f (X) et soit α ∈ FPp,q (P ).
   Les propriétés suivantes sont équivalentes :
   a) Pour tout domaine compact V de X, la restriction de α au polytope f (V ) est nulle ;
   b) Pour tout domaine compact V de X, la restriction de f ∗ α à V est nulle ;
   c) L’image de f ∗ α dans FXp,qG (X) est nulle.
Démonstration. — D’après la proposition 3.4.1, les assertions (1) et (2) sont équiva-
lentes.
   Supposons (1). Comme X admet un G-recouvrement par des domaines compacts,
l’assertion (3) s’en déduit.
   Supposons (3). Il existe donc un G-recouvrement (Xi ) tel que f ∗ α|Xi = 0 en tant que
section du préfaisceau Fpfp,q . Soit V un domaine compact de X. La restriction de f ∗ α
à Xi ∩ V est nulle pour tout i ; comme la famille (Xi ∩ V ) est un G-recouvrement de V ,
le corollaire 3.4.2 entraîne que f ∗ α|V = 0, d’où l’assertion (2). Cela termine la preuve
de la proposition.
                                § 3.4. NULLITÉ DES G-FORMES                                83

Corollaire 3.4.5. — Soit X un espace G-tropical compact, soit f : X → E une carte
G-tropical et soit P le sous-espace paralinéaire f (X). Soit α ∈ GPp,q (P ), et soit ω la
G-forme f ∗ α. Notons K le support de ω dans X et H celui de α dans f (X). On a
H = f (K).

Démonstration. — Soit x un point de X. Soit Q un voisinage de f (x) dans P qui est
                                             −1
un polytope compact. Le domaine W = ftrop       (Q) de X est un voisinage de x et ω|W =
       ∗
(f |W ) (α|Q ).
   Supposons que x appartienne à K. Le compact K rencontre alors l’intérieur de W , ce
qui entraîne que ω|W ̸= 0, et donc que α|Q ̸= 0. Il s’ensuit que H rencontre Q. Comme
Q peut être choisi arbitrairement petit, f (x) appartient à H, d’où l’inclusion f (K) ⊂ H.
   Réciproquement, supposons que f (x) ∈ H. Par définition de H, la restriction à Q de
la forme α est non nulle. D’après la proposition 3.4.4, la restriction de ω à f −1 (Q) est
non nulle. Par conséquent, f −1 (Q) rencontre K, donc Q = f (f −1 (Q)) rencontre f (K).
Comme Q est un voisinage arbitrairement petit de f (x), celui-ci est adhérent à f (K).
Puisque f (K) est compact, f (x) appartient à f (K).

3.4.6. — À toute carte G-tropicale (f : V → E, P ) sur un domaine V de X et à toute
fonction u sur P , associons la fonction u◦f sur V . On définit ainsi un morphisme de pré-
faisceaux de Fpf0,0 vers le G-faisceau des fonctions sur X. Il découle de la proposition 3.4.4
que le morphisme de FX0,0G dans le G-faisceau des fonctions sur X est injectif, morphisme
par lequel nous identifierons systématiquement une (0, 0)-G-forme à une fonction.
   Une section globale du faisceau GX0,0G est une fonction sur X qui est G-localement de la
forme φ(f1 , . . . , fn ) où les fi sont des fonctions paralinéaires sur X, et où φ appartient
à la classe G . De telles fonctions seront appelées G-localement tropicales de classe G .

Définition 3.4.7. — Soit A la classe des fonctions lisses. Les sections de AX0,0
                                                                              G
                                                                                 sont
appelées fonctions G-lisses sur X.

   Les fonctions G-lisses sont donc les fonctions sur X sont G-localement de la forme
φ(f1 , . . . , fn ) où les fi sont des fonctions paralinéaires et où φ est une fonction de
classe C ∞ .
```

## CLD.txt, newline lines 5289–5314

```text

Lemme 4.4.5. — Soit f : Y → X une immersion par morceaux d’espaces paralinéaires
de niveau n. Soit α une forme-volume à coefficients boréliens sur X. On a l’égalité
(f ∗ α)Bor = f ∗ (αBor ) de mesures de Borel régulières positives sur Y . Si α est localement
intégrable, alors f ∗ α est localement intégrable et l’on a l’égalité (f ∗ α)Rad = f ∗ (αRad ) de
mesures de Radon sur Y .

   Comme f est une immersion par morceaux, l’image inverse de la mesure de Borel
régulière αBor par f est définie G-localement (cf. A.3.13) ; de même pour les mesures de
Radon.
Démonstration. — L’espace Y est G-recouvert par des cellules C telles que f induise un
isomorphisme de C sur son image, laquelle possède une immersion paralinéaire dans Rn .
L’assertion découle alors de la construction de ces mesures.

Lemme 4.4.6. — Soit f : Y → X une immersion par morceaux compacte d’espaces
paralinéaires de niveau n. Soit α une forme-volume à coefficients boréliens sur Y . On
a une inégalité (f∗ α)Bor ⩽ f∗ (αBor ) de mesures de Borel régulières positives sur X, qui
est une égalité si f est injective. Si α est localement intégrable, alors f∗ α est localement
intégrable et l’on a l’égalité (f∗ α)Rad = f∗ (αRad ) de mesures de Radon sur X.

Démonstration. — En raisonnant localement, on se ramène au cas où X est paracom-
pact. Soit (C , D) un couple de décompositions cellulaires qui est adapté à f . Après
restriction à toute cellule D de D, les assertions découlent directement des définitions
des mesures et des images directes.
108    CHAPITRE 4. CALIBRAGES ET INTÉGRATION SUR LES ESPACES PARALINÉAIRES

```

## CLD.txt, newline lines 5449–5483

```text
forme ω sont positifs.
   Les (n, n)-formes localement µ-intégrables forment un sous-faisceau en BXG -module
de BX n,n
        G
          , et l’application ω 7→ ⟨ω, µ⟩ est linéaire.
   On dira enfin que le calibrage µ est localement intégrable si toute forme à coefficients
localement bornés est localement µ-intégrable. Sur une cellule, cela revient à dire que
le calibrage est produit d’un calibrage standard par une fonction localement intégrable.
Les calibrages G-localement constants sont localement intégrables.

Exemple 4.5.7. — Lorsque X est un sous-espace affine de dimension n d’un espace
affine V , ω une forme lisse sur X et µ un vecteur-volume sur X, on retrouve la notion
d’intégrale définie dans le paragraphe 1.5.3 à partir des idées de Lagerberg.
   D’une certaine manière, les constructions de ce chapitre visaient simplement à « G-
faisceautiser » cette formule élémentaire de Lagerberg sur un espace affine.

Proposition 4.5.8. — Soit f : Y → X une immersion par morceaux propre d’espaces
paralinéaire de niveau n.
   a) Pour toute (n, n)-forme ω sur X et tout calibrage µ de Y , on a l’égalité f∗ ⟨f ∗ ω, µ⟩ =
⟨ω, f∗ µ⟩ de formes-volume n-dimensionnelles sur X.
   b) Pour toute (n, n)-forme ω sur Y et tout calibrage µ de X, on a l’égalité ⟨f∗ ω, µ⟩ =
f∗ ⟨ω, f ∗ µ⟩ de formes-volume n-dimensionnelles sur X.

Démonstration. — En raisonnant localement, on se ramène au cas où X est paracom-
pact. Il existe alors un couple (C , D) de décompositions cellulaires qui est adapté à f .
                  § 4.6. CALIBRAGES ET INTÉGRALES DES (n − 1, n)-FORMES                  111

Les assertions indiquées se vérifient alors, cellule par cellule, à partir des constructions
des intégrales et de la définition du calibrage f∗ µ (resp. du calibrage f ∗ µ).



     § 4.6. CALIBRAGES ET INTÉGRALES DES (n − 1, n)-FORMES

4.6.1. — Soit G une classe de coefficients. Soit X un espace paralinéaire de niveau n,
```

## CLD.txt, newline lines 6308–6332

```text
Lemme 5.3.4. — Si la forme ω est G-tropicalisée par une carte G-tropicale f de do-
                (n)
maine X, alors Σf supporte fortement ω.

Démonstration. — Le support de ω est contenu dans l’ensemble des points x ∈ X en
                                                                    (n)
lesquels f est de dimension tropicale ⩾ n qui, par définition, est Σf .
                                                                  (n)
  Soit T un sous-espace paralinéaire fermé de X qui contient Σf . Démontrons que ω|T
est le prolongement par zéro de ω|Σ(n) . Soit C une décomposition cellulaire en f -cellules
                                     f
                             (n)
de T qui est compatible à Σf . Il suffit de prouver que pour toute cellule C de C      telle
                        (n)
que C̊ est disjoint de Σf , on a ω|C = 0.
  Par hypothèse, f est de dimension tropicale < n en tout point de C̊, donc il existe une
cellule D, compacte, d’intérieur non vide, de C̊ telle que dim(f (D)) < n. Comme C est
une f -cellule, on dim(f (C)) = dim(f (C̊)) = dim(f (D)). D’après la proposition 3.4.4, on
a donc ω|C = 0.
                          (n)
  Cela démontre que Σf supporte fortement ω.

Proposition 5.3.5. — Soit n un entier et soit X un espace G-tropical vertébré de
niveau n. Soit (p, q) un couple d’entiers naturels tel que max(p, q) = n et soit ω une
G-forme de type (p, q) sur X. Supposons que X est paracompact, ou que le support de ω
```

## CLD.txt, newline lines 6400–6414

```text
                                      f
composition cellulaire finie en f -cellules.
                                                                         (n)
   Lorsque f est une carte agréable, nous noterons Πf l’ensemble f (Σf ) et l’appellerons
le polyèdre tropical de la carte G-tropicale agréable f . Il est purement de dimension n
                                                               (n)
et l’application f induit une immersion par morceaux de Σf sur Πf .
5.4.4. — Si X est compact, toute carte G-tropicale est agréable et l’on a Πf = f (X)(n)
(proposition 5.2.5).
Proposition 5.4.5. — Soit X un espace G-tropical vertébré de niveau n, soit f : X →
E une carte G-tropicale agréable et soit P un sous-espace paralinéaire P de E. Consi-
dérons la carte G-tropicale fP : f −1 (P ) → E sur le domaine f −1 (P ) (considéré comme
130                      CHAPITRE 5. ESPACES G-TROPICAUX CALIBRÉS

espace G-tropical vertébré de niveau n) déduite de f par restriction. La carte fP est
```

## CLD.txt, newline lines 6753–6812

```text
            = ⟨ω|T , µT ⟩                  d’après (3.3.14)
            = ⟨(ω|Σ )|T , (µΣ )|T ⟩        d’après (3.3.14) et la définition d’un calibrage
            = ⟨ω|Σ , µΣ ⟩|T = ω
                              e |Y
parce que l’accouplement entre (n, n)-formes et calibrages est un morphisme de faisceaux
sur le site XG . Le lemme est ainsi démontré.

Proposition 5.8.3. — Il existe un unique morphisme de faisceaux FXn,n            G
                                                                                    → VXnG
sur XG , noté ω 7→ ω e , qui prolonge l’application définie en (5.8.1) lorsque ω possède
un support fort. Ce morphisme est FX0,0G -linéaire. Si ω est une G-forme positive, la
forme-volume ωe est positive. Si ω est à coefficients dans une classe G , il en va de même
de la forme-volume ωe.
Démonstration. — Compte tenu du lemme 5.8.2, la première assertion résulte de ce que
toute forme sur un domaine paracompact possède un support fort, et que tout domaine
est G-recouvert par ses domaines paracompacts. Les autres propriétés découlent alors
de la construction.

5.8.4. — Explicitons cette construction lorsque ω est tropicale. Soit f : X → E une
carte G-tropicale et soit α une (n, n)-forme sur un sous-espace paralinéaire de E conte-
                                         (n)
nant f (X) telle que ω = f ∗ α. Alors, Σf est un support fort de ω (lemme 5.3.4) et on
                                         (n)
a l’égalité de formes-volume sur Σf            :
                                                ∗
(5.8.4.1)                                ω̃ = ⟨ftrop α, µΣ(n) ⟩.
                                                            f

Si, de plus, la carte G-tropicale f est agréable, la proposition 4.5.8 entraîne alors que
(5.8.4.2)                       ftrop,∗ (ω̃) = ⟨α, f∗ µΣ(n) ⟩ = ⟨α, µΠf ⟩.
                                                        f
                                   § 5.9. MESURES DE BORD                                  137

 5.8.5. — Soit ω une forme de type (n, n) sur XG à coefficients tropicalement boréliens.
 Nous venons de lui associer une forme-volume n-dimensionnelle ω̃. Nous noterons alors
 ωBor la mesure de Borel sur X associée à ω̃ par la construction du §5.7.1.
   Nous dirons que ω est localement intégrable si cette mesure est localement finie, et
 que ω est intégrable si cette mesure est finie. Lorsque ω est localement intégrable, nous
 noterons ωRad la mesure de Radon associée à ω̃ ; on a |ωRad | = ωBor . Lorsque ω est une
 G-forme positive, la mesure ωRad est positive.         R           R
   Si f est une fonction borélienne sur X, on notera X f |ω| et X f ω les intégrales de f
Rcontre les mesures ωBor et ωRad lorsqu’elles existent. Cela définit en particulier l’intégrale
  X
    ω pour toute G-forme de type (n, n) à support compact qui est localement intégrable
(par exemple lisse).
   Les G-formes localement intégrables constituent un sous-espace vectoriel de F n,n (XG )
contenant les G-formes lisses. Les G-formes intégrables en sont un sous-espace vectoriel
qui contient les G-formes lisses à support compact.
5.8.6. — Soit u une fonction localement intégrable sur X et soit ω une G-forme lisse
de type (n, n) sur X. Alors, u est localement intégrable par rapport à la mesure ωBor ,
de sorte que uωRad est une mesure de Radon sur X.
   L’application (u, ω) 7→ uωRad est bilinéaire ; elle induit une application linéaire de
Lloc
   1
     (XG ) ⊗ A n,n (XG ) dans l’ensemble des mesures de Radon sur X. Cette application
se factorise par L1loc (XG ) ⊗ A n,n (XG ). On la notera bien sûr α 7→ αRad .
   Cette construction s’étend en des morphismes de G-faisceaux
                  Lloc,X
                    1
                        G
```

## CLD.txt, newline lines 6934–6977

```text

               § 5.10. INTÉGRALES ET TROPICALISATIONS

  Soit X un espace G-tropical calibré de niveau n.
Proposition 5.10.1. — Soit f : X → E une carte G-tropicale agréable, soit Πf le
polyèdre tropical de la carte f et soit µΠf son calibrage.
  Soit p ∈ {n−1, n} et soit α une (p, n)-forme à coefficients boréliens sur un sous-espace
paralinéaire P de E contenant f (X).
  a) Si p = n, on a l’égalité
                                   ftrop,∗ (f ∗ α)Bor ⩾ ⟨α, µΠf ⟩Bor
                             (n)
de mesures de Borel sur Πf .
  b) Si p = n − 1, on a l’inégalité
                                   ftrop,∗ (f ∗ α)Bor ⩾ ⟨α, µΠf ⟩Bor
                             (n)
de mesures de Borel sur Πf .
  c) La mesure (f ∗ α)Bor est localement finie si et seulement si la forme α|Πf est locale-
ment intégrable sur Πf ; dans ce cas, on a l’égalité
                                   ftrop,∗ (f ∗ α)Rad = ⟨α, µΠf ⟩Rad
de mesures de Radon sur Πf .
   d) En particulier, si α est intégrable sur Πf , la forme f ∗ α est intégrable sur X, on a
l’égalité
                                   Z         Z
                                        ∗
(5.10.1.1)                            f α=       ⟨α, µΠf ⟩
                                        X           Πf

lorsque p = n et l’égalité
                                      Z ∂          Z ∂
                                            ∗
(5.10.1.2)                                  f α=         ⟨α, µΠf ⟩
                                        X           Πf

lorsque p = n − 1.
Démonstration. — Posons ω = f ∗ α. D’après la relation (5.8.4.2) lorsque p = n et la
relation (5.9.4.2) lorsque p = n−1, on a l’égalité (ftrop )∗ (ω̃) = ⟨α, µΠf ⟩ de formes-volume
p-dimensionnelles sur Πf . Le lemme 4.4.6 entraîne alors que f∗ (ω̃Bor ) ⩾ ⟨α, µΠf ⟩Bor .
Loreque p = n, on vérifie, en revenant aux définitions et en utilisant la positivité du
140                   CHAPITRE 5. ESPACES G-TROPICAUX CALIBRÉS

calibrage canonique, que l’on a en fait l’égalité, d’où (1). En appliquant le lemme 4.4.6
aux mesures de Radon correspondantes, on en déduit (2), puis (3) par intégration.

5.10.2. — La formule (5.10.1.1) définit explicitement l’intégrale d’une forme tropicale.
```

## CLD.txt, newline lines 7070–7101

```text


      § 6.2. FORMES LISSES SUR UN ESPACE G-TROPICAL AFFINÉ

  Soit G une classe de coefficients.
Définition 6.2.1. — Soit (p, q) un couple d’entiers naturels. Soit ω une G-forme de
type (p, q) à coefficients dans G sur un domaine V de X.
  On dit que ω est tropicale s’il existe une carte tropicale qui G-tropicalise ω.
  On dit que ω est une forme (de type (p, q) à coefficients dans G ) si pour tout point x
de V , il existe un voisinage ouvert U de x dans V sur lequel ω est tropicale.
  Lorsque G est la classe des fonctions lisses, on parle de forme lisse sur l’espace G-
tropical affiné X. Si de plus p = q = 0, on parle de fonction lisse.
6.2.2. — Les formes lisses forment un sous-G-préfaisceau en R-espaces vectoriels
de AXp,q qui est un faisceau pour la topologie usuelle. Ces faisceaux sont stables par les
opérateurs d′ , d′′ , J et par le produit extérieur.
6.2.3. — Un espace G-tropical affiné (X, LX ) est dit affinement séparé si pour tout
couple (x, y) de points de X avec x ̸= y, il existe une fonction affine f sur X telle que
f (x) ̸= f (y). A fortiori, les fonctions lisses sur X séparent les points. On dira alors que
X est différentiellement séparé.
   Si X est affinement (resp. différentiellement) séparé, il en est de même de tout domaine.
   Un espace G-tropical affiné (X, LX ) est dit localement affinement (resp. différentielle-
ment) séparé si chacun de ses points possède un voisinage affinement (resp. différentiel-
lement) séparé.
   Cela entraîne que le faisceau des fonctions lisses sépare localement les points au sens
du §A.2.2.
Corollaire 6.2.4. — Soit (X, LX ) un espace G-tropical affiné qui est localement dif-
férentiellement séparé. Soit K une partie compacte de X et soit U un voisinage ouvert
de K. Il existe une fonction lisse sur X qui vaut 1 au voisinage de K et dont le support
est compact et contenu dans U .
Démonstration. — C’est une conséquence du corollaire A.2.4.

Théorème 6.2.5 (Stone–Weierstraß). — Soit (X, LX ) un espace G-tropical affiné
```

## CLD.txt, newline lines 8130–8168

```text
forme positive est positive.                             R∂
   On définit aussi le courant [ω]∂ par la formule α 7→ X ω∧α défini à l’aide de l’intégrale
de bord des G-formes. Il est d’ordre 0 et de bidimension (n − p − 1, n − q). Lorsque ω
est une forme lisse, on a [ω]∂ = δX ∂
                                      ∧ ω.
   Il découle de la définition de la topologie des espaces de courants que les applications
ω 7→ [ω] et ω 7→ [ω]∂ sont continues.
7.3.5. — Nous allons maintenant généraliser cette construction aux « G-formes » qui
sont combinaisons linéaires de G-formes usuelles à coefficients dans un anneau de fonc-
tions non nécessairement tropicales.
   Soit V un domaine de X et soit U un voisinage ouvert de V dans X dans lequel V
est fermé. Soit u ∈ L1loc (V ), ω ∈ AXp,q
                                       G
                                          (V ) et α ∈ Acn−p,n−q (U ) ; la G-forme ω ∧ α|V est à
support compact
            R     dans V , de sorte que u est intégrable pour la mesure associée. L’appli-
cation α 7→ V u(ω ∧ α)Rad est un courant d’ordre 0 sur U . La section correspondante de
                              § 7.3. COURANTS D’INTÉGRATION                              165

π ∗ Dp,q (V ) ne dépend pas du choix de U . On définit ainsi un morphisme de G-faisceaux
                                L1loc,X ⊗ AXp,q
                                             G
                                                → π ∗ (Dp,q )X .
Par adjonction, on en déduit un morphisme de faisceaux
                            π∗ (L1loc,X ⊗ AXp,q
                                             G
                                                ) → π∗ π ∗ (Dp,q )X .
Comme l’unité id → π∗ π ∗ est un isomorphisme de foncteurs, on en déduit un morphisme
de faisceaux
                               π∗ (L1loc,X ⊗ AXp,q
                                                G
                                                   ) → (Dp,q )X .
   L’image d’une section ω sera notée [ω]. La notation est cohérente avec le cas des G-
formes lisses ; via l’isomorphisme de la proposition 3.4.11, elle est aussi cohérente avec
les cas des G-formes à coefficients tropicalement boréliens localement bornés. Ce courant
est d’ordre 0 et de bidimension (n − p, n − q).
   Par composition avec l’homomorphisme canonique
                               1
                         π∗ (Lloc,X ⊗ AXp,q
```

## CLD.txt, newline lines 16809–16927

```text
Définition 12.2.1. — Soit X un espace k-analytique ; on appelle moment sur X un
morphisme de X vers un tore.

   Soit f : X → T un moment sur un espace k-analytique X. On désignera par ftrop : X →
Ttrop l’application composée X → T → Ttrop . On dira que l’application ftrop est la
tropicalisation de f ; c’est une application continue.

Remarque 12.2.2. — Si f : T → T ′ est un morphisme affine entre tores, la nota-
                                                                  ′
tion ftrop désigne donc aussi bien l’application induite Ttrop → Ttrop que sa composée
        ′     ′
T → T → Ttrop avec l’application de tropicalisation de T . Cette ambiguïté n’aura, en
pratique, guère de conséquences.

Lemme 12.2.3. — Soit X un espace analytique, soit x un point de X et soit V un
domaine analytique de X contenant x. Soit f : V → Gm une fonction analytique in-
versible. On suppose que X est presque bon en x. Il existe alors un voisinage ouvert U
de x et une fonction analytique inversible g sur U telle que |f − g| < |f | sur U ∩ V ; en
particulier, ftrop et gtrop coïncident sur U ∩ V .
                      § 12.2. MOMENTS, TROPICALISATIONS, POLYÈDRES                         335

Démonstration. — Soit U un voisinage ouvert de x dans X et g ∈ OX (U ) tels que
|f (x) − g(x)| < |f (x)| ; il en existe car κ(x) est dense dans H (x) et |f (x)| > 0. L’en-
semble des points de U ∩ V en lesquels |f − g| < |f | est un voisinage de x dans V ; quitte
à restreindre U , on peut supposer que cette inégalité vaut dans U ∩ V tout entier. Quitte
à restreindre encore U , on peut supposer que g est inversible sur U , d’où le lemme.

Théorème 12.2.4. — Soit X un espace k-analytique compact et soit f : X → T un
moment. Le sous-espace compact ftrop (X) est un polyèdre de Ttrop de dimension dim(X).
   L’assertion a été établie par Berkovich dans le cas où X est G-localement algébrisable,
cf. [11], cor. 6.2.2. Pour le cas général, on pourra se reporter à [46], §3.30, ou à [50],
th. 3.2.
Corollaire 12.2.5. — Soit X un espace k-analytique compact et soit V une partie
fermée de X munie d’une structure faiblement analytique de dimension d. Soit f : X → T
un moment. Alors, ftrop (V ) est une partie paralinéaire de dimension ⩽ d de Ttrop .
Démonstration. — On se ramène immédiatement au cas où il existe un morphisme
g : X → Y et un point y ∈ Y tel que V = g −1 (y). Alors, le produit fibré X ×Y H (y)
permet de considérer V comme un espace H (y)-analytique compact, de dimension ⩽ d,
et f |V : V → TH (y) comme un moment sur cet espace. On donc dim(ftrop (V )) ⩽ d.

Corollaire 12.2.6. — Soit X un espace k-analytique compact de dimension n. Soit
f : X → T un moment. Si X est affinoïde, alors ftrop (∂(X)) est une partie paralinéaire
de dimension ⩽ n − 1 de Ttrop ; en genéral, ftrop (∂(X)) est contenu dans une telle partie
paralinéaire.
Démonstration. — Compte tenu de l’exemple 11.10.2 selon lequel ∂(X) est une partie
faiblement analytique de dimension ⩽ dim(X) − 1, cela résulte du corollaire précédent.
Il s’agit en fait du théorème 3.2 de [50], démontré de la même façon, même si la notion
de structure faiblement analytique n’avait pas été dégagée.

12.2.7. — Soit X un espace k-analytique et f : X → T un moment. Soit x ∈ X. On
appellera degré de transcendance résiduel (gradué) de f en x le degré de transcendance
résiduel torique du point f (x) de T . Si χ1 , . . . , χn est une base de X(T ), ce degré est
le degré de transcendance sur ek du sous-corps gradué de H         ^  (x) engendré par e
                                                                                       k et les
χi^◦ f (x). Si T = Gn et f = (f1 , . . . , fn ), c’est donc le degré de transcendance sur e
                     m                                                                    k du
sous-corps gradué de H ^ (x) engendré par e k et les f]
                                                      i (x).
   Le degré de transcendance résiduel de f en x est majoré à la fois par dk (x) et par n.
Il vaut n si et seulement si f (x) ∈ S(T ).
Proposition 12.2.8. — Soit X un espace k-analytique et soit x un point de X. Soit
f = X → T un moment ; posons ξ = ftrop (x). Notons d le degré de transcendance
résiduel de f en x.
   Il existe un voisinage analytique compact U de x dans X tel que pour pour tout voi-
sinage analytique compact V de x contenu dans U , on ait les propriétés suivantes :
   i) Les germes de polyèdres (ftrop (U ), ξ) et (ftrop (V ), ξ) coïncident ;
   ii) La dimension locale dimξ (ftrop (V )) est majorée par d, et a fortiori par dk (x).
336           CHAPITRE 12. PARTIES SQUELETTIQUES D’UN ESPACE ANALYTIQUE

   iii) Si x ̸∈ ∂(X), alors ftrop (V ) est purement de dimension d en ξ. Si, de plus, d = n,
alors ftrop (V ) est un voisinage de ξ dans Ttrop .
   iv) Si dimξ (ftrop (V )) = n, alors f (x) ∈ S(T ) ; inversement, si f (x) ∈ S(T ) et si de
plus x ∈ / ∂(X), alors dimξ (ftrop (V )) = n.
Démonstration. — L’existence d’un voisinage analytique U vérifiant les i), ii) et iii) est
le théorème 3.4 de [50]. Montrons (iv). Si dimξ (ftrop (V )) = n, il résulte de (ii) que n ⩽ d,
donc que d = n et que f (x) ∈ S(T ). Réciproquement, si f (x) ∈ S(T ) alors d = n et si
de plus x ∈
          / ∂X il résulte de (iii) que dimξ (ftrop (V )) = n.

Remarque 12.2.9. — Soit X un espace k-analytique et soit x ∈ X. Soit f : X → Gnm
un moment. Si V est un voisinage analytique compact de x dans X, il résulte de la
proposition ci-dessus que le germe de ftrop (V ) en x ne dépend pas de V . Nous le noterons
ftrop (X, x).
   La preuve du théorème 3.4 de [50] en donne une description en termes de réduction
de Temkin, que nous allons rappeler ici, en supposant que le germe est (X, x) séparé.
   Le théorème 10.5.7 assure (en reprenant le vocabulaire et les notations de 10.5.6)
l’existence d’un sous-foncteur D de Dn{1} tel que pour tout H ∈ D et tout n-uplet
(h1 , . . . , hn ) d’éléments de H, les assertions suivantes soient équivalentes :
   (i) h ∈ D(H) ;
   (ii) il existe H ′ ∈ DH et une valuation w appartenant à (X,   ^   x) à valeurs dans H ′ telle
que w(f]     i (x)) = hi pour tout i.
Comme le groupe des paramètres est ici {1}, le foncteur D est simplement définiQpar
conjonctions et disjonctions d’inégalités de la forme φ ⩽ 1 où φ est un monôme xri i
à exposants rationnels. L’ensemble D(R×      + ) est alors un cône rationnel, et ftrop (X, x) =
                ×
(ftrop (x) · D(R+ ), ftrop (x)) en notation multiplicative.
                                                      ^
  En particulier, si x est intérieur, c’est-à-dire si (X, x) = P       , ce germe de polytope
                                                                 H
                                                                 ^ (x)/e
                                                                       k

ne dépend que de la classe d’isomorphie de l’extension graduée F de e       k dans H^  (x)
engendrée par les f]
                   i (x), munie de cette famille. Dans ce cas, il est équidimensionnel, de
dimension égale au degré de transcendance (gradué) de F sur e    k.
Définition 12.2.10. — Soit X un espace analytique et soit f : X → T un moment.
Soit x un point de X. On appelle dimension tropicale de f en x la borne inférieure de di-
mensions des polyèdres ftrop (V ), où V est un domaine analytique compact qui contient x.
On la note dimtrop,x (f ).
  Soit d le degré de transcendance résiduel de f en x. D’après le théorème 12.2.4 et la
proposition 12.2.8, on a
(12.2.10.1)                 dimtrop,x (f ) ⩽ d ⩽ dk (x) ⩽ dimx (X),
et dimtrop,x (f ) = d si x ∈
                           / ∂X. Si X est compact, il résulte de la définition que
(12.2.10.2)                   dim(ftrop (X)) = sup dimtrop,x (f ).
                                                x∈X

Proposition 12.2.11. — Soit X un espace analytique, soit x un point de X ∂(X).
```

## CLD.txt, newline lines 18040–18119

```text
      § 12.8. POLYÈDRES CARACTÉRISTIQUES ET DIMENSION
                            TROPICALE

12.8.1. — Soit X un espace k-analytique de niveau n, soit m un entier et soit f =
X → Gm   m un moment sur X. On note (f1 , . . . , fm ) les composantes de f . Pour toute
partie I de {1, . . . , m}, on note qI la projection canonique de Gm      I
                                                                   m sur Gm .
  Rappelons (proposition 12.6.8) que le polyèdre caractéristique de f est une partie
paralinéaire de X et que l’application ftrop |Σf est une immersion par morceaux d’espaces
paralinéaires.
  Le but de ce numéro est de relier la dimension tropicale de ftrop aux propriétés de Σf .
Théorème 12.8.2. — Soit x un point de X.
                                                                    (n)
   a) On a dimtrop,x (f ) ⩽ n, avec égalité si et seulement si x ∈ Σf .
   b) Supposons x ∈ Int(X). Les trois assertions suivantes sont équivalentes : (i) x ∈ Σf ;
                                                        (n)
(ii) f est de dimension tropicale n en x ; (iii) x ∈ Σf .
   c) Si X est compact ou plus généralement si l’application ftrop est topologiquement
                                    (n)
propre, on a ftrop (X)(n) = ftrop (Σf ).
Démonstration. — a) Soit d le degré de transcendance résiduel de f en x. On a
dimtrop,x (f ) ⩽ d ⩽ dimx X ((12.2.10.1)). Comme dimx X ⩽ n, il vient dimtrop,x (f ) ⩽
d ⩽ n.
                                                              (n)
   Supposons que dimtrop,x (f ) = n, et montrons que x ∈ Σf . Puisque dimtrop,x (f ) ⩽
d ⩽ n, on a d = n. Il existe donc un sous-ensemble I de cardinal d de {1, . . . , m}
tels que les f] i (x) soient algébriquement indépendants sur k. ll s’ensuit que x ∈ Σf . Il
                                                             e
reste à vérifier que dimx (Σf ) = n. Soit V un voisinage analytique compact arbitraire
de x dans X et démontrons que dim(Σf ∩ V ) = n. Comme dimtrop,x (f ) = n, on a
dim(ftrop (V )) = n. Soit C une cellule compacte de dimension n de ftrop (V ) et soit
             § 12.8. POLYÈDRES CARACTÉRISTIQUES ET DIMENSION TROPICALE                     357

q : Gm        n
      m → Gm un morphisme de tores tel que la restriction de qtrop à ⟨C⟩ soit injective.
                                                                            (n)
Alors, dim(q ◦ f )trop (V ) = n. D’après le lemme 12.2.13, (q ◦ f )trop (V )sq est contenu dans
(q ◦f )(V ), donc dans (q ◦f )(Σf ∩V ). Comme dim(Σf ∩V ) ⩾ n, il vient dim(Σf ∩V ) = n,
ce qu’il fallait démontrer.
                                          (n)
   Inversement, supposons que x ∈ Σf et montrons que dimtrop,x (f ) = n. Soit V un
                                         (n)                                (n)
voisinage compact de x. Alors, V ∩ Σf est un voisinage de x dans Σf , donc contient
une cellule de dimension n puisque dimx Σf = n par hypothèse. Comme la restriction
               (n)
de ftrop à Σf est une immersion par morceaux, cela prouve que dim(ftrop (V )) ⩾ n,
et donc que dim(ftrop (V )) = n puisque dim V ⩽ n. Comme V est arbitraire, il vient
dimtrop,x (f ) = n.
   b) Faisons l’hypothèse que x ∈ Int(X). Supposons x ∈ Σf . Il existe alors un sous-
ensemble I de {1, . . . , m} tels que les f]   i (x) pour i ∈ I soient algébriquement indépen-
dantes sur k ; par conséquent, d ⩾ n, si bien que d = n puisqu’on sait que d ⩽ n. Et
              e
comme x ∈ Int(X), la dimension tropicale de f en x est égale à d (12.2.10.1), et donc
à n.
   Supposons réciproquement que x est de dimension tropicale n en x. Le point x appar-
                  (n)
tient alors à Σf d’après (a).
   L’implication (iii)⇒(i) est évidente.
   c) Supposons ftrop topologiquement propre. En raisonnant G-localement sur Rm on
                                           (n)
voit que ftrop (X), ftrop (Σf ) et ftrop (Σf ) sont des parties paralinéaires fermées de Rm .
                                                                                           (n)
Comme ftrop induit une immersion par morceaux de Σf sur ftrop (Σf ), l’image ftrop (Σf )
est purement de dimension n et est donc contenue dans ftrop (X)(n) .
                                                                         (n)
  Soit maintenant ξ un point de ftrop (X) qui n’appartient pas à ftrop (Σf ). Soit x un
                                                     (n)
point de X tel que ftrop (x) = ξ ; on a donc x ̸∈ Σf . D’après a), ftrop est de dimension
tropicale < n en x. Comme ftrop est topologiquement propre, il existe un voisinage
                             −1
analytique compact V de ftrop   (ξ) et un voisinage paralinéaire U de ξ dans ftrop (X) tels
      −1
que ftrop (U ) ⊂ V et que dim(ftrop (V )) ⩽ n−1. Puisque U ⊂ ftrop (V ), il est de dimension
au plus n − 1 et ξ n’appartient à ftrop (X)(n) .

Corollaire 12.8.3. — Soit X un espace k-analytique de niveau n et soit f : X → T un
                  (n)                                             (n)
moment. Alors Σf coïncide avec le polyèdre de variation maximale Σftrop de l’application
paralinéaire ftrop (définition 5.2.1).
Démonstration. — C’est l’assertion a) du théorème 12.8.2.
```

## CLD.txt, newline lines 19153–19240

```text
Lemme 13.2.8 (Longueur générique et extension des scalaires)
    Soit X un espace k-analytique et soit K une extension complète de k. Soit F un
faisceau cohérent sur X. Soit Z une composante irréductible de X, soit ℓ la longueur
générique de X le long de Z, soit ℓK la longueur générique de FK le long de ZK , et soit
µ la multiplicité générique de Xred,K le long de ZK . On a alors ℓK = µℓ.
                                                   gen     gen
Démonstration. — Choisissons un point y sur ZK         ⊂ XK    dont on note x l’image sur
X ; par construction, x ∈ Z. L’anneau local OXK,G ,y est artinien car y ∈ XK    gen
                                                                                    , et il est
plat sur OXG ,x (13.1.5) ; ce dernier est donc également artinien, ce qui montre que x
appartient à X gen , et donc à Z gen car x ∈ Z.
   Pour alléger les notations posons A = OXG ,x , B = OXK,G ,y et M = FXG ,x . On note m
l’idéal maximal de A et κ = A/m son corps résiduel. Enfin on pose B ′ = B/mB = κ⊗A B.
Remarquons que κ = OXred,G ,x et B ′ = OXred,K,G ,y (proposition 13.1.9 d ) et c)).
   Par définition de ℓ il existe une filtration

                             {0} = M0 ⊂ M1 ⊂ . . . ⊂ Mℓ = M

du A-module M dont les quotients successifs sont A-isomorphes à κ. Comme B est plat
sur A, cette filtration en induit une

                {0} = B ⊗A M0 ⊂ B ⊗A M1 ⊂ . . . ⊂ B ⊗A Mℓ = B ⊗A M

dans la catégorie des B-modules dont les quotients successifs sont tous B-isomorphes à
B ′ . Il vient
                    ℓK = ℓB (B ⊗A M ) = ℓ · ℓB (B ′ ) = ℓ · ℓB ′ (B ′ ) = ℓµ.
378              CHAPITRE 13. COMPLÉMENTS DE GÉOMÉTRIE ANALYTIQUE

§ 13.3. DEGRÉ ET DEGRÉ CALIBRÉ D’UN MORPHISME QUASI-FINI

13.3.1. — Soit f : Y → X un morphisme d’espaces k-analytiques. Soit y ∈ Y . Si
dimy (f −1 (f (y)) > 0, on pose degy (f ) = +∞. Sinon, le point y est isolé dans sa fibre
f −1 (f (y)), l’anneau local de f −1 (f (y)) en y est une H (f (y))-algèbre de dimension finie
et on note degy (f ) sa dimension.
   Lorsque f est fini et plat en y, cet entier degy (f ) coïncide avec l’entier degy (f ) défini
en 11.6.3.
   Nous dirons que degy (f ) est le degré de f en y.
   Soit V un domaine analytique de Y contenant y et soit U un domaine analytique
de X tel que f (V ) ⊂ U ; soit g : V → U le morphisme déduit de f . Pour tout y ∈ V , on
a degy (f ) = degy (g), car pour tout y ∈ V d’image x ∈ X, les anneaux locaux en y de
f −1 (f (y)) et de g −1 (g(y)) coïncident.
   Soit Z un sous-espace analytique fermé de X contenant x et soit g : Y ×X Z → Z le
morphisme déduit de f par changement de base. Comme les espaces H (x)-analytiques
f −1 (x) et g −1 (x) coïncident, on a degy (f ) = degy (g).
13.3.2. — Soit f : Y → X un morphisme d’espaces k-analytiques. Pour tout x ∈ X,
on définit de le degré de f au-dessus de x comme la somme
                                            X
                               degx (f ) =     degy (f ).
                                              y∈f −1 (x)


Il est fini si et seulement si f −1 (x) est compact et de dimension nulle ; alors f −1 (x) est
un espace analytique fini sur H (x), et degx (f ) = dimH (x) (O(f −1 (x))).
   Lorsque f est globalement fini et plat, cet entier degx (f ) coïncide avec l’entier degx (f )
défini en 11.6.1.

Lemme 13.3.3. — Soit f : Y → X un morphisme d’espaces analytiques. Soit K une
extension valuée complète de k ; notons p : XK → X et q : YK → Y les morphismes de
changement de base, et fK : YK → XK le morphisme déduit de f par changement de
base. Soit xK ∈ p−1 (x).
  a) Pour tout y ∈ Y d’image x = f (y) ∈ X, tout point xK ∈ p−1 (x), on a
                                        X
                         degy (f ) =              degz (fK ).
                                           −1
                                        z∈fK  (xK )∩q −1 (y)


  b) Pour tout x ∈ X et tout point xK ∈ p−1 (x), on a degx (f ) = degxK (fK ).

Démonstration. — Tout se passe dans les fibres f −1 (x) et fibre fK−1 (xK ) = f −1 (x) ×
M (H (xK )). Cela permet de supposer que X = M (k) = {x} et XK = M (K) = {xK }.
  Prouvons l’égalité a). Si dimy (Y ) > 0, il en est de même de dimz (YK ) pour tout
antécédent z de y, si bien que les deux membres de l’égalité sont infinis. Supposons
maintenant dimy (Y ). Alors OY,y est une k-algèbre artinienne et OY,y ⊗k K = z OYK ,z ,
                                                                              Q
où z parcourt l’ensemble des antécédents de y dans YK . L’égalité s’ensuit.
  L’égalité b) s’en déduit en sommant sur tous les points de Y .
               § 13.3. DEGRÉ ET DEGRÉ CALIBRÉ D’UN MORPHISME QUASI-FINI                    379

13.3.4. — Soit A un anneau local artinien et soit M un A-module de longueur finie.
Nous noterons δA (M ) le nombre rationnel ℓA (M )/ℓA (A). Indiquons quelques propriétés
élémentaires de cet invariant.
   Si A est réduit, c’est un corps, on a ℓA (A) = 1 et δA (M ) est donc simplement ℓA (M ),
c’est-à-dire la dimension de M comme A-espace vectoriel.
   Supposons M plat sur A, c’est-à-dire libre comme A-module ; soit r son rang. Comme
M ≃ Ar , ℓA (M ) = rℓA (A), si bien que δA (M ) = r.
   Si M = Ared , alors ℓA (M ) = 1 et δA (M ) = 1/ℓA (A).
   Soit B une A-algèbre finie. Soit κ le corps résiduel de A et λ celui de B. Choisis-
```

## CLD.txt, newline lines 18355–18407

```text
Théorème 12.9.11. — Soit X un espace k-analytique de niveau n. Soit L une exten-
sion complète de k et notons p : XL → X la projection canonique. Soit Σ une partie sque-
lettique de X ; notons ΣL la réunion des polyèdres caractéristiques ΣfL , où f : V → T
parcourt l’ensemble des moments définis sur un domaine analytique V de X tels que
Σf ⊂ Σ.
   L’ensemble ΣL est une partie squelettique de XL et le morphisme p induit une immer-
sion par morceaux surjective de ΣL sur Σ qui préserve la dimension locale.
   De plus, pour tout moment f : V → T tel que Σf ⊂ Σ, on a ΣL ×Σ Σf = ΣfL .

Démonstration. — La première assertion est G-locale sur X ; comme elle est vérifiée
pour l’application ΣfL → Σf , il suffit de démontrer la seconde assertion.
   Soit f : V → T un moment défini sur un domaine analytique V de X. Démontrons
l’égalité PL ×P Σf = ΣfL . Cela revient à démontrer que si g : W → T ′ est un moment et
x ∈ Σf ∩Σg , alors les fibres de ΣfL et ΣgL au-dessus de x coïncident. Quitte à remplacer X
par V ∩ W , on suppose que les moments f et g sont définis sur X.
   Soit x ∈ Σf ∩ Σg . Soit C la complétion d’une clôture algébrique de k et soit M une
extension complète composée de L et C. Considérons le diagramme

                                               XM   →
                                                           σ
                                         q′
                                         →    ←      ←
                                                       →
                                                           ←

                                    XL                  XC
                                         ←             ←
                                         p →
                                                   →   q

                                               X
dans lequel σ est la section de Poineau de l’application XM → XC dont l’existence
résulte de ce que C est algébriquement clos. Comme l’extension C/k contient une sous-
extension algébrique dense, on a ΣfC = q −1 (Σf ). Comme C est algébriquement clos, on
a ΣfM = σ(ΣfC ). Enfin, on a ΣfL = q ′ (ΣfM ). Par suite,
                                  ΣfL = q ′ (σ(q −1 (Σf ))),
donc la fibre de ΣfL au-dessus de x est donnée par la formule
                                   ΣfL ,x = q ′ (σ(q −1 (x)))
dans laquelle Σf n’intervient plus ; cette fibre coïncide donc avec la fibre de ΣgL au-dessus
de x. Cela conclut la démonstration du théorème.
  Le cas des polyèdres caractéristiques et la définition de ΣL entraînent de plus la
caractérisation suivante :

Proposition 12.9.12. — Conservons les notations du théorème 12.9.11.
   a) Si l’extension L/k possède une sous-extension algébrique dense, alors ΣL = p−1 (Σ) ;
   b) Si l’extension L/k est universellement multiplicative, ou si le corps le corps k est
algébriquement clos, on a ΣL = σL (Σ).

Démonstration. — Compte tenu de la seconde assertion du théorème, l’assertion a)
découle de la proposition 12.7.2, et l’assertion b) du corollaire 12.7.5.
                  § 12.9. PARTIES SQUELETTIQUES D’UN ESPACE ANALYTIQUE                         363

Lemme 12.9.13. — Soit X un espace k-analytique de niveau n, soit Σ une partie
```

## CLD.txt, newline lines 20320–20360

```text
                           § 14.2. MOMENTS ET DEGRÉS

Lemme 14.2.1. — Soit X un espace analytique de niveau n, soit f : X → Gnm un
moment. Alors, f est quasi-fini et plat en tout point de Σf .
Démonstration. — Soit x ∈ Σf . On a f (x) ∈ S(Gnm ), donc dk (f (x)) = n. D’après
le lemme 11.5.1, le morphisme f est quasi-fini en x. Comme Gnm est réduit, le théo-
rème 10.3.7 de [52] entraîne que f est plat en x.

Proposition 14.2.2. — Soit X un espace analytique de niveau n, soit f : X → T un
moment sur X et soit C une f -cellule commode de dimension n de X. Soit q : T → Gnm
un morphisme de tores tel que qtrop |ftrop (C) est injectif. Alors le morphisme q ◦ f est de
dimension relative nulle en tout point de C et il existe un unique entier d > 0 tel que ce
morphisme soit fini et plat de degré d en tout point de C̊.
Démonstration. — Soit q : T → Gnm un morphisme de tores tel que qtrop soit injectif sur
ftrop (C). La dimension tropicale de q ◦ f est égale à n en tout point de C, donc C ⊂
(q ◦f )−1 (S(Gnm )) d’après la prop. 12.2.8, (iv). D’après le lemme 11.5.1, le morphisme q ◦f
est de dimension relative nulle en tout point de C.
   Comme C̊ ne rencontre pas ∂(X), il résulte du lemme 11.6.5 que le morphisme q ◦f est
fini et plat en tout point de C̊ ; on a noté degx (q ◦ f ) son degré et il s’agit de démontrer
que l’entier degx (q ◦ f ) est indépendant du point x ∈ C̊.
   Soit D la cellule sq(qtrop (ftrop (C))) de Gnm . Si un point x ∈ Int(X) vérifie q ◦ f (x) ∈ D̊,
                                                                                 (n)
alors q◦f est de dimension tropicale n en x, donc f aussi, si bien que x ∈ Σf . Autrement
dit, on a les inclusions
                                                                (n)
                             C̊ ⊂ (q ◦ f )−1 (D̊) ∩ Int(X) ⊂ Σf .
                                                                        (n)
   Soit maintenant x ∈ C̊. Par hypothèse, C̊ est ouvert dans Σf ; il est donc ouvert
dans (q ◦ f )−1 (D̊) ∩ Int(X). Comme q ◦ f est fini et plat en x, il existe un voisinage
ouvert U de x dans Int(X) et un voisinage ouvert V de q ◦ f (x) dans Gnm tels que
q ◦ f induise un morphisme fini et plat de degré degx (q ◦ f ) de U sur V , et tel que
(q ◦ f )−1 (D̊) ∩ U ⊂ C̊. Un point y ∈ C̊ ∩ U est alors le seul antécédent dans U de
q ◦ f (y) par q ◦ f ; on a donc degy (q ◦ f ) = degx (q ◦ f ) pour tout y ∈ C̊ ∩ U . La
fonction x 7→ degx (q ◦ f ) est localement constante sur l’ensemble C̊ ; comme celui-ci est
connexe, elle est constante.
400           CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

Proposition 14.2.3. — Soit X un espace k-analytique paracompact de niveau n et
soit f : X → Gnm un moment. Soit Σ un sous-espace paralinéaire paracompact de Σf .
Il existe une décomposition cellulaire C de Σ en f -cellules telle que pour toute cellule
C ∈ C , l’application x 7→ degx (f ) soit finie et constante sur C̊.
```

## CLD.txt, newline lines 20700–20870

```text
de l’anneau local de (g ′ )−1 (g ′ (y)) en g ′ (y). Considérons X × Gdm comme Gdm,X ; alors
406           CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

g ′ (y) s’identifie au point g|Yx (y) de Gdm,H (x) . De même, la fibre (g ′ )−1 (g ′ (y)) s’identifie à
la fibre (g|Yx )−1 (g|Yx (y)). Il en résulte l’égalité degy (g ′ ) = degy (g|Yx ).
                                   ′                                            ′
     Démontrons enfin que degg (y) (f ′ ) = degx (f ). Par définition, degg (y) (f ′ ) est la dimen-
sion sur f ′ (g ′ (y)) = h(y) de l’anneau local de (f ′ )−1 (h(y)) en g ′ (y). Le morphisme f ′
est déduit de f par changement de base. Ainsi, (f ′ )−1 (h(y)) = f −1 (f (x)) ⊗H (f (x))
H (h(y)). L’anneau local de f −1 (f (x)) en x est une algèbre locale artinienne de di-
mension degx (f ) sur H (x). Son produit tensoriel par H (h(y)) est le produit des an-
neaux locaux de (f ′ )−1 (h(y)) en tous les antécédents de x. Pour conclure la démons-
tration de l’égalité voulue, il suffit de démontrer que le point x n’a qu’un seul an-
técédent dans (f ′ )−1 (h(y)). Cela résulte du fait que H (f (x)) est séparablement clos
dans H (h(y)) : le point h(y) appartient à S(Gnm,H (f (x)) ), le corollaire 12.1.8 s’applique
donc.



                        § 14.3. CALIBRAGES CANONIQUES

  Soit X un espace analytique de niveau n.
Proposition 14.3.1. — Soit f : X → T un moment et soit C une f -cellule de dimen-
                                                                                 ′
sion n. Soit q et q ′ des morphismes de tores de T dans Gnm tels que qtrop et qtrop  soient in-
jectifs sur ftrop (C). Soit σq l’unique section affine de qtrop dont l’image contient ftrop (C) ;
on définit σq′ de façon analogue.
   Soit µ un vecteur-volume sur Rn . Pour presque tout x ∈ C, on a l’égalité
(14.3.1.1)                  degx (q ◦ f )σq,∗ (µ) = degx (q ′ ◦ f )σq′ ,∗ (µ)
de vecteurs volumes sur l’espace affine ⟨ftrop (C)⟩.
Démonstration. — Notons Cf = ftrop (C).
  Supposons d’abord que q ′ soit de la forme φ ◦ q, où φ : Gnm → Gnm est un morphisme
surjectif de tores. D’après la proposition 13.3.10, on a
                  degx (q ′ ◦ f ) = degx (φ ◦ q ◦ f ) = degq◦f (x) (φ) degx (q ◦ f ).
Le morphisme φ est fini et plat et pour tout t ∈ S(Gnm ), on a degt (φ) = deg(φ), en vertu
du corollaire 12.1.7. Par suite, on a degx (q ′ ◦ f ) = deg(φ) degx (q ◦ f ) pour tout x ∈ C.
   Par ailleurs, φtrop est une application affine bijective de Rn dans lui-même et l’on a
σq′ = σq ◦φ−1                                                                    →
                                                                                 −
              trop . La valeur absolue du déterminant de l’application linéaire φ trop est égale
au degré de φ. Par suite, φ−1                                                 −1
                                trop applique le vecteur volume µ sur deg(φ) µ, de sorte que
σq′ ,∗ (µ) = deg(φ)−1 σq,∗ (µ). La relation voulue est donc vérifiée dans ce cas particulier.
                               ′
   Supposons ensuite que qtrop    − qtrop soit constante sur Cf . D’après le théorème 14.2.7,
          x                 x ′
on a deg (q ◦ f ) = deg (q ◦ f ) pour tout x ∈ C ∩ Int(X) ; d’autre part, C ∩ ∂(X)
est localement négligeable. De plus, σq et σq′ diffèrent d’une constante, si bien que
σq,∗ (µ) = σq′ ,∗ (µ). Cela prouve la relation voulue dans ce cas.
   Montrons maintenant comment la conjonction de ces deux cas permet d’obtenir le
cas général. Notons ψ l’unique application linéaire de Rn dans lui-même telle que ψ ◦
          ′
qtrop et qtrop diffèrent d’une translation sur Cf . Compte tenu de la convention faite
au paragraphe 12.1.13, l’espace affine ⟨Cf ⟩ est Q-rationnel, si bien que ψ appartient
                                 § 14.3. CALIBRAGES CANONIQUES                                  407

à GLn (Q). Il existe donc deux morphismes de tores φ et φ′ de Gnm dans lui-même tels
que φ′trop ◦ ψ = φtrop . Ainsi, (φ′ ◦ q ′ ◦ f )trop et (φ ◦ q ◦ f )trop diffèrent d’une constante
                       −1
sur C. Posons V = ftrop   (Cf ) ; c’est un domaine analytique fermé de X qui contient C.
                ′  ′
Sur V , on a (φ ◦ q ◦ f )trop = (φ ◦ q ◦ f )trop .
  D’après le premier cas particulier, on a donc presque partout les relations

                     degx (φ ◦ q ◦ f |V )σφ◦q,∗ (µ) = degx (q ◦ f |V )σq,∗ (µ)

et
                   degx (φ′ ◦ q ′ ◦ f |V )σφ′ ◦q′ ,∗ (µ) = degx (q ′ ◦ f |V )σq′ ,∗ (µ).
D’autre part, il résulte du second cas particulier traité que

                degx (φ ◦ q ◦ f |V )σφ◦q,∗ (µ) = degx (φ′ ◦ q ′ ◦ f |V )σφ′ ◦q′ ,∗ (µ).

Comme V est un domaine de X contenant x, on a les égalités de degrés

             degx (q ◦ f |V ) = degx (q ◦ f ) et         degx (q ′ ◦ f |V ) = degx (q ′ ◦ f )

pour tout x ∈ V . Cela conclut la démonstration de la proposition.

14.3.2. — Soit Σ une partie squelettique de X, paracompacte et contenue dans le
polyèdre caractéristique Σf d’un moment f : V → T défini sur un domaine analytique V
de X. Nous allons définir un calibrage µΣ de Σ.
   Soit C une décomposition cellulaire de Σ en f -cellules commodes (lemme 14.1.5).
Soit C une cellule de dimension n appartenant à C . Soit q : T → Gnm un morphisme de
tores tel que qtrop soit injectif sur ftrop (C). D’après la proposition 14.2.2, le morphisme
q ◦f est fini et plat sur C̊ et son degré x 7→ degx (q ◦f ) prend une valeur finie, strictement
positive et constante dC sur C̊. Notons e = |e1 ∧ · · · ∧ en | le vecteur-volume canonique
de Rn , considéré comme un calibrage constant, et posons µC = dC (q ◦ f )∗trop (e) ; c’est
un calibrage standard de la cellule C. Il ne dépend pas du choix de q d’après la propo-
sition 14.3.1. La famille (µC ) définit un calibrage standard de Σ ; on le note µΣ,f,C .
   Vérifions que ce calibrage est indépendant du choix de (V, f, C ).
   Soit V ′ un domaine analytique de X, soit f ′ : V ′ → T ′ un moment tel que Σ ⊂ Σf ′ et
soit C ′ une décomposition cellulaire de Σ en f ′ -cellules commodes. Posons W = V ∩ V ′
et soit g le moment (f, f ′ ) sur W et considérons une décomposition cellulaire D de Σ en
g-cellules commodes qui est adaptée aux décompositions cellulaires C et C ′ .
   Soit D une cellule de dimension n appartenant à D. Soit q : T → Gnm un morphisme
de tores tel que qtrop est injectif sur ftrop (D). Notons aussi p : T × T ′ → T la première
projection.
   Soit C une cellule de C contenant D. Comme D̊ ne rencontre pas ∂(W ), il est contenu
dans Int(W/V ), si bien que q ◦ f |W est fini et plat de degré dC en tout point de D̊. Il
existe aussi un entier dD > 0 tel que (q ◦ p) ◦ g soit fini et plat de degré dD en tout point
de D̊ (proposition 14.2.2). Comme on a (q ◦ p) ◦ g = q ◦ f |W , on a dC = dD . Par ailleurs,
(q ◦ g)∗trop (e) = (q ◦ f )∗trop (e). Par suite, les triplets (V, f, C ) et (W, g, D) induisent le
même calibrage sur D.
   Cela entraîne que le calibrage µΣ,f,C de Σ déduit de (V, f, C ) coïncide avec celui déduit
de (W, g, D) ; par symétrie, il coïncide avec celui déduit de (V ′ , f ′ , C ′ ). Notons-le µΣ .
408          CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

14.3.3. — Soit Σ′ un sous-espace paralinéaire de Σ. Soit C ′ une décomposition cellu-
laire de Σ en f -cellules commodes qui raffine C ∩ Σ′ . La description de µΣ′ ,f,C ′ entraîne
alors l’égalité µΣ |Σ′ = µΣ′ .
Lemme 14.3.4. — Soit X un espace analytique de niveau n et soit Σ une partie sque-
lettique de X. Il existe un unique calibrage µΣ de Σ vérifiant la propriété suivante : pour
tout domaine analytique V de X, tout moment f sur V et tout sous-espace paralinéaire Σ′
de Σf ∩ Σ qui est paracompact, on a µΣ |Σ′ = µΣ′ . Ce calibrage µΣ est standard.
Démonstration. — Par définition, l’espace squelettique Σ est G-recouvert par des sous-
espaces paralinéaires Σ′ comme dans l’énoncé. Les calibrages formant un G-faisceau, il
existe au plus un tel calibrage. Pour démontrer son existence, il suffit alors de vérifier
la condition de coïncidence. Or, si Σ′ est Σ′′ sont des sous-espaces paralinéaires de Σ
satisfaisant les conditions de l’énoncé, on a µΣ′ |Σ′ ∩Σ′′ = µΣ′ ∩Σ′′ = µΣ′′ |Σ′ ∩Σ′′ d’après le
paragraphe 14.3.3.

Définition 14.3.5. — Soit X un espace analytique de niveau n, topologiquement sé-
paré, et soit Σ une partie squelettique de X. On appelle calibrage canonique de Σ le
calibrage dont le lemme 14.3.4 affirme l’existence et l’unicité.
   Par construction, ce calibrage est standard. Si Σ′ ⊂ Σ, on a µΣ |Σ′ = µΣ′ . Il résulte
aussi des constructions que si Σ est contenu dans un domaine analytique V de X, le
calibrage canonique µΣ de Σ, vu comme partie squelettique de V , coïncide avec son
calibrage canonique comme partie squelettique de X.
   Ce calibrage canonique munit l’espace vertébré associé à l’espace analytique X d’une
structure d’espace G-tropical calibré de niveau n. Nous supposerons toujours implicite-
ment que X est muni de cette structure.
Proposition 14.3.6. — Soit X un espace analytique de niveau n. Soit Σ une partie
squelettique de X, soit µ son calibrage canonique. Soit L une extension complète de k,
soit p : XL → X le morphisme de changement de base, soit ΣL la partie squelettique dé-
duite de Σ par changement de base (théorème 12.9.11) et soit µL son calibrage canonique.
On a p∗ (µL ) = µ.
Démonstration. — Il suffit de traiter le cas où X est (para)compact et où il existe un
moment f : X → T tel que Σ = Σf . Alors, ΣL = ΣfL (théorème 12.9.11). Le morphisme
de changement de base p étant compact, il existe une décomposition cellulaire C de Σ en
f -cellules commodes et une décomposition cellulaire D de ΣL en fL -cellules commodes
telles que le couple (D, C ) soit adapté au morphisme p. Soit C une cellule de dimension n
de C . et soit q : T → Gnm un morphisme de tores tel que qtrop soit injectif sur ftrop (C).
Soit x ∈ C̊ et soit t = q ◦ f (x) ∈ S(Gnm ). Soit tL ∈ (Gnm )L l’unique antécédent de t
dans S(Gnm )L . D’après le lemme 13.3.3, on a
                                             X
                       degx (q ◦ f ) =                 degy (q ◦ fL ).
                                      y∈p−1 (x)∩(q◦fL )−1 (tL )

Les points y qui apparaissent au second membre de cette égalité sont des antécédents
de x dans ΣfL . Inversement, soit y ∈ ΣfL un point tel que p(y) = x ; prouvons que
q ◦ fL (y) = tL . Soit D la cellule de D telle que y ∈ D̊ ; on a p(D) = C, donc (q ◦ fL )trop =
(q ◦ f )trop ◦ p est injectif sur D, si bien que q ◦ fL est de dimension tropicale n en y. Cela
                  § 14.4. CALIBRAGES CANONIQUES ET MORPHISMES FINIS                         409

entraîne que q ◦ fL (y) ∈ S((Gnm )L ) ; comme c’est un antécédent de t, on a q ◦ fL (y) = tL .
On a donc                                    X
                          degx (q ◦ f ) =            degy (q ◦ fL ).
                                            y∈p−1 (x)∩ΣfL

Par conséquent, µC = D p∗ µD , où D parcourt l’ensemble des n-cellules D de D au-
                         P
dessus de C. Ainsi, µΣ = p∗ (µΣL ).




       § 14.4. CALIBRAGES CANONIQUES ET MORPHISMES FINIS

14.4.1. — Soit p : Y → X un morphisme entre espaces k-analytiques de niveau n.
Soit Σ une partie squelettique de X. Supposons que les fibres de p au-dessus de tout
point de Σ sont des ensembles finis.
```

## CLD.txt, newline lines 20924–20976

```text
Remarque 14.4.3. — Soit F une extension finie de k et soit X un espace F -analytique
de niveau n. On peut aussi voir X comme un espace k-analytique de niveau n ; pour
éviter les confusions nous le noterons ici X0 ; on a dim(X0 ) = dim(X).
   Comme l’extension F de k est algébrique, le squelette canonique S(Gnm,F ) est l’image
réciproque de S(Gnm ) par la projection de Gnm,F sur Gnm , et S(Gnm ) est l’image de S(Gnm,F )
([50], (0.15)). On en déduit qu’une partie de X est squelettique si et seulement si elle
l’est en tant que partie de X0 .
   Soit donc Σ une partie squelettique de X ; notons µ son calibrage canonique et µ0 celui
de Σ vu comme partie squelettique de X0 . La projection canonique de Gnm,F sur Gnm est
finie et plate de degré [F : k]. Il découle donc de la définition du calibrage canonique
que µ0 = [F : k]µ.



                § 14.5. CALIBRAGES ET TROPICALISATIONS

Définition 14.5.1. — Soit n un entier, soit X un espace k-analytique de niveau n et
soit f : X → T un moment agréable sur X. On appelle polyèdre tropical du moment f
                    (n)                                                            (n)
le polyèdre ftrop (Σf ) muni du calibrage image directe du calibrage canonique de Σf .
On le note Πf .
  Ce n’est autre que le polyèdre tropical de la carte tropicale agréable ftrop .
  Lorsque X est compact, rappelons (théorème 12.8.2) que l’on a l’égalité de polyèdres
Πf = ftrop (X)(n) .
                                       (n)
  Comme le calibrage canonique de Σf est standard, il en est de même du calibrage
canonique de Πf .
  Comme la formation du calibrage canonique de Σf commute à l’extension des scalaires
(proposition 14.3.6), il en est de même de la formation du calibrage canonique de Πf .
14.5.2. — Voyons maintenant comment décrire explicitement le calibrage de Πf . Soit
                                       (n)
C une décomposition cellulaire de Σf vérifiant les propriétés de la proposition 14.1.12
et soit D = {ftrop (C) ; C ∈ C } la décomposition cellulaire de Πf qui lui correspond.
Soit D une n-cellule appartenant à D et soit q : T → Gnm un morphisme de tores tel que
qtrop |D soit injectif. Soit CD l’ensemble des n-cellules C ∈ C telles que ftrop (C) = D ;
pour C ∈ CD , soit dC l’entier naturel que q ◦ f soit fini et plat de degré dC en tout
                           § 14.5. CALIBRAGES ET TROPICALISATIONS                              411
                                          P
point de C̊ (prop. 14.2.2). Notons dD = C∈CD dC . Notons e = |e1 ∧ · · · ∧ en | le vecteur-
volume canonique de Rn , considéré comme un calibrage constant. Soit σD : Rn → Ttrop
                                                                                        (n)
l’unique section affine de qtrop d’image ⟨D⟩. Par définition du calibrage canonique de Σf
et de l’image directe d’un calibrage, on a µΠf ,D = dD σD,∗ (e).

Proposition 14.5.3. — Soit X un espace k-analytique de dimension n, soit f : X → T
un moment agréable et soit x ∈ Πf . Soit V un voisinage de x dans Πf qui est une n-cellule
ouverte de Ttrop . Soit q : T → Gnm un morphisme de tores tel que qtrop |V est injectif.
Supposons que q ◦ f |ftrop
                       −1
                           (V ) est fini et plat au-dessus de qtrop (x)sq , de degré dx . Notons
        n
σq : R → Ttrop l’unique section affine de qtrop d’image ⟨V ⟩ et notons e = |e1 ∧ · · · ∧ en |
le vecteur-volume canonique de Rn , considéré comme un calibrage constant. Alors, le
```

## CLD.txt, newline lines 21545–21664

```text
Proposition 15.1.1. — Soit X un espace k-analytique topologiquement séparé, consi-
déré comme espace G-tropical affiné.
   a) Soit ω une G-forme de type (p, q) sur X. Il existe un G-recouvrement (Vi ) de X et,
pour tout i, un moment fi : Vi → Ti sur Vi , une forme αi de type (p, q) sur une partie
                                                                 ∗
paralinéaire de Ti,trop contenant fi,trop (Vi ) tels que ω|Vi = fi,trop αi .
   b) Soit ω une forme de type (p, q) sur X. Il existe un recouvrement ouvert (Vi ) de X
et, pour tout i, un moment fi : Vi → Ti sur Vi , une forme αi de type (p, q) sur une partie
                                                                 ∗
paralinéaire de Ti,trop contenant fi,trop (Vi ) tels que ω|Vi = fi,trop αi .
422 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Démonstration. — On ne traite que le cas des G-formes, l’autre est analogue. Par hy-
pothèse, il existe un G-recouvrement (Wi ) de X et, pour tout i, une application parali-
néaire gi sur Wi à valeurs dans un espace affine Rni , une forme βi de type (p, q) sur une
partie paralinéaire de Ei contenant gi (Wi ), tels que ω|Wi = gi∗ βi pour tout i. Par défini-
tion d’une application paralinéaire, il existe pour tout i un G-recouvrement (Vi,j ) de Wi
et, pour tout j, un moment fi,j sur Vi,j , à valeurs dans le tore Gnmi un nombre rationnel
ai,j et un élément ci,j ∈ Rni tels que gi,j = ai,j fi,j,trop + ci,j . Notons pi,j : Rntrop
                                                                                        i
                                                                                           → Rni
l’application affine t 7→ at + ci,j ; on a donc gi,j = pi,j ◦ fi,j,trop , de sorte que
                                               ∗
                                     ω|Vi,j = fi,j,trop (p∗i,j βi ).

L’assertion en résulte.


Corollaire 15.1.2. — Une fonction u sur X est lisse au voisinage d’un point x s’il
existe un voisinage U de x dans X, des fonctions inversibles f1 , . . . , fn sur U et une
fonction φ sur Rn au voisinage de (f1,trop (x), . . . , fn,trop (x)) telle que u = φ ◦ ftrop sur U .

  Dans la suite du texte, nous travaillerons essentiellement avec ce type de cartes (G)-
tropicales.

Proposition 15.1.3. — Soit G une classe de coefficients. Soit X un espace analytique
topologiquement séparé et soit u une fonction numérique sur X.
  a) Pour que u soit G-localement de classe G , il faut et il suffit que u|Xred le soit.
  b) Si X est presque bon, pour que u soit localement de classe G , il faut et il suffit que
u|Xred le soit.

  Une variante de cet énoncé vaut pour les formes et les G-formes.
Démonstration. — Si u est localement (resp. G-localement) de classe G , il en est de
même de sa restriction à Xred . Démontrons la réciproque.
   a) Supposons que u|Xred soit G-localement de classe G . Soit V un domaine affinoïde
de Xred sur lequel il existe un moment f : V → Gnm et une fonction φ de classe G sur Rn
telle que u|V = φ ◦ ftrop . On déduit du théorème de Gerritzen–Grauert (voir par exemple
[128], théorème 3.1) que V est recouvert par une réunion de domaines affinoïdes de la
forme Wred , où W est un domaine affinoïde de X. Sur Wred , chacune des fi se relève
en une fonction gi sur W ; ces fonctions sont inversibles et ont même norme que fi ;
elles définissent un moment g : W → Gnm tel que uW = φ ◦ gtrop . Cela prouve que u est
G-localement de classe G .
   b) Soit x un point de X et soit V un voisinage analytique de x dans Xred sur lequel
il existe un moment f : V → Gnm et une fonction φ de classe G sur Rn telle que u|V =
φ ◦ ftrop . Comme X est presque bon en x, chaque fi (x) ∈ H (x) est approchée par une
fonction gi ∈ OX,x . En particulier fi et gi ont même norme au voisinage de g. Ainsi, les
gi définissent un moment g défini au voisinage de X sur lequel on a u = φ ◦ gtrop ; cela
prouve que u est de classe G au voisinage de x.
                              § 15.2. SÉPARATION HOLOMORPHE                                423

                      § 15.2. SÉPARATION HOLOMORPHE

Proposition 15.2.1. — Soit X un espace k-analytique topologiquement séparé, consi-
déré comme espace G-tropical affiné. Soit ω une G-forme de type (p, q) sur X.
  a) Le support de ω est contenu dans l’ensemble des points x ∈ X tels que dk (x) ⩾
max(p, q).
  b) Soit V un domaine analytique de X et soit Y un fermé de Zariski de V . Si
dim(Y ) < max(p, q), le support de ω ne rencontre pas Y .

Démonstration. — Démontrons l’assertion a). Soit x ∈ X un point tel que dk (x) <
max(p, q). Comme dtrop (x) ⩽ dk (x), on a donc dtrop (x) < max(p, q) ; l’assertion résulte
donc de la proposition 3.3.6.
  L’assertion b) en résulte car tout point y de Y vérifie dk (y) ⩽ dim(Y ).

15.2.2. Séparation holomorphe. — On dira qu’un espace analytique X est holo-
morphiquement séparé si pour tout couple (x, y) de points de X avec x ̸= y il existe une
fonction analytique f sur X telle que |f (x)| =
                                              ̸ |f (y)|. Un tel espace est topologiquement
séparé.
  Si X est un espace holomorphiquement séparé, il en va trivialement de même de tout
domaine analytique de X.
  Tout espace affinoïde est par définition holomorphiquement séparé ; en conséquence,
tout domaine analytique d’un espace affinoïde est holomorphiquement séparé.
  Un espace analytique sera dit localement holomorphiquement séparé s’il est topologi-
quement séparé et si chacun de ses points possède un voisinage analytique holomorphi-
quement séparé.
  Un espace analytique topologiquement séparé qui est bon, ou plus généralement dont
tout point possède un voisinage isomorphe à un domaine analytique d’un espace affi-
noïde, est localement holomorphiquement séparé. C’est en particulier le cas d’un espace
analytique topologiquement séparé sans bord.

Lemme 15.2.3. — Soit X un espace k-analytique holomorphiquement séparé. L’an-
neau des fonctions lisses sur X sépare les points.

Démonstration. — Soit x, y des points distincts de X. Par définition de la séparation
holomorphe, il existe une fonction analytique f sur X telle que |f (x)| =     ̸ |f (y)|.
  Supposons ces deux valeurs non nulles ; soit φ une fonction C ∞ à support compact
sur R valant 0 au voisinage de log|f (x)| et 1 au voisinage de log|f (y)|. La fonction
φ ◦ log|f |, définie sur l’ouvert d’inversibilité de f , est lisse ; prolongeons-la par 0 sur X
tout entier. Comme φ est à support compact, la fonction obtenue est nulle au voisinage
de l’ensemble des zéros de f ; elle est donc lisse et prend des valeurs différentes en x et y.
  Si f (x) = 0, on a alors f (y) ̸= 0 et on raisonne de même à partir d’une fonction φ à
support compact valant 1 au voisinage de log|f (y)|.
  Le cas où f (y) = 0 est analogue par symétrie.

Corollaire 15.2.4. — Soit X un espace k-analytique localement holomorphiquement
séparé. L’espace G-tropical affiné X est localement différentiellement séparé. En parti-
culier, le faisceau des fonctions lisses sur X sépare localement les points.
424 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Corollaire 15.2.5. — Soit X un espace analytique localement holomorphiquement sé-
paré. Soit K une partie compacte de X et soit U un voisinage ouvert de K. Il existe
une fonction lisse sur X qui vaut 1 au voisinage de K et dont le support est compact et
contenu dans U .
Démonstration. — Comme X est localement différentiellement séparé, c’est une consé-
quence du corollaire 6.2.4.

Théorème 15.2.6 (Stone–Weierstraß). — Soit X un espace analytique localement
holomorphiquement séparé et soit U un ouvert de X. Soit f une fonction continue à
valeurs réelles sur X dont le support est compact et contenu dans U . Soit a et b des
```

## CLD.txt, newline lines 21712–21776

```text
coefficients tropicalement boréliens définit une mesure de Borel ωBor sur X, et lorsque
cette G-forme est localement intégrable, une mesure de Radon ωRad .

Proposition 15.3.1. — Soit L une extension complète de k, soit p : XL → X le mor-
phisme de changement de base. Pour toute forme ω de type (n, n) sur XG à coefficients
tropicalement boréliens, on a p∗ (ωL,Bor ) = ωBor . Lorsque ω est localement intégrable, on
a p∗ (ωL,Rad ) = ωRad .

Démonstration. — En revenant aux définitions, on déduit de la compatibilité du cali-
brage canonique à l’extension des scalaires (proposition 14.3.6) l’égalité p∗ ω
                                                                              fL = ωL de
formes-volume n-dimensionnelles. La proposition en résulte.

Proposition 15.3.2. — Soit L une extension complète de k, soit p : XL → X le mor-
phisme de changement de base. Pour toute forme ω de type (n−1, n) sur XG à coefficients
tropicalement boréliens, on a p∗ (ωL,Bor ) = ωBor . Lorsque ω est localement intégrable, on
a p∗ (ωL,Rad ) = ωRad .

Démonstration. — En revenant aux définitions, on déduit de la compatibilité du cali-
brage canonique à l’extension des scalaires (proposition 14.3.6) l’égalité p∗ ω
                                                                              fL = ωL de
formes-volume (n − 1)-dimensionnelles. La proposition en résulte.




               § 15.4. INTÉGRALES ET MORPHISMES FINIS

15.4.1. — Soit n ∈ N et soit X et Y des espaces k-analytiques de niveau n et soit
f : Y → X un morphisme qui est fini au-dessus du complémentaire d’un fermé de Zariski
de X de dimension < n. On a défini au §14.4.1 une fonction x 7→ dcx (f ) de X dans N ;
nous la noterons dcf .
   Soit p ∈ {n − 1, n} et soit ω une G-forme de type (p, n) sur X. Posons η = f ∗ ω.

Lemme 15.4.2. — Soit Σ un partie squelettique de X qui supporte fortement ω ; notons
ω̃ la forme-volume p-dimensionnelle sur Σ déduite de ω et du calibrage canonique de Σ.
   Alors p−1 (Σ) est une partie squelettique de Y qui supporte fortement f ∗ ω ; notons fg
                                                                                         ∗ω

la forme-volume p-dimensionnelle sur p−1 (Σ) déduite de f ∗ ω et du calibrage canonique
de p−1 (Σ). On a l’égalité :
                                          ∗ ω = dc ·ω̃.
                                      f∗ fg       f
426 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Démonstration. — Posons T = f −1 (Σ). Notons µΣ et µT les calibrages canoniques de Σ
et T. On a l’égalité f∗ µT = dcf ·µΣ (proposition 14.4.2). L’assertion découle alors de la
proposition 4.5.8.
  Compte tenu de la définition des mesures de Borel et, éventuellement de Radon,
associées aux formes volumes p-dimensionnelles, on en déduit la proposition suivante.

Proposition 15.4.3. — Supposons que ω soit localement intégrable. Alors, f ∗ ω est
localement intégrable et l’on a l’égalité
                                    f∗ (f ∗ ω)Rad = dcf ·ωRad
de mesures de Radon sur X.

   Remarquons que les supports des mesures ωRad et f∗ (f ∗ ω)Rad évitent tout fermé de Za-
riski d’intérieur vide de X ; en particulier, ils sont contenus dans le domaine de définition
du degré calibré.



§ 15.5. EXISTENCE DE TROPICALISATIONS (PRESQUE) GLOBALES

   La définition d’une forme (resp. d’une G-forme) est locale (resp. G-locale), mais lorsque
```

## CLD.txt, newline lines 22100–22151

```text
§ 15.7. L’ESPACE TROPICAL ASSOCIÉ À UN ESPACE ANALYTIQUE

  Soit X un espace analytique purement de dimension n, topologiquement séparé. On le
considère comme espace G-tropical calibré de niveau n. Il est riche (théorème 12.10.6).

Théorème 15.7.1. — Soit X un espace analytique purement de dimension n, topolo-
giquement séparé. Muni de son bord ∂(X) au sens de la théorie des espaces analytiques,
l’espace G-tropical affiné et calibré de niveau n associé à X est un espace tropical de
niveau n.

Démonstration. — Vérifions les conditions de la définition 6.6.2.
  L’intérieur Int(X) de X est localement holomorphiquement séparé (15.2.2) ; il est donc
localement différentiellement séparé (corollaire 15.2.4). Il est décent (proposition 12.4.7)
car il est sans bord, donc bon, donc presque bon. Il est très riche (théorème 12.11.1) et
harmonieux (théorème 15.6.1).
  Et il résulte du corollaire 12.9.14 que Σ ∩ ∂X est n-négligeable pour toute partie
paralinéaire Σ de X, de même que Σ∩∂(V /X) pour tout domaine V de X car ∂(V /X) ⊂
∂V .
  On munit ainsi tout espace analytique X, topologiquement séparé, et purement de
dimension n, d’une structure d’espace tropical de niveau n.
              § 15.7. L’ESPACE TROPICAL ASSOCIÉ À UN ESPACE ANALYTIQUE              433

15.7.2. — Soit X un espace analytique topologiquement séparé, purement de dimen-
sion n et soit V un domaine de X. Le domaine V est muni de deux façons, a priori
distinctes, d’une structure d’espace tropical de niveau n, soit comme espace analytique,
soit comme domaine de l’espace tropical X. La formule ∂(V ) = (∂(X) ∩ V ) ∪ ∂(V /X)
montre que ces deux structures coïncident.
Remarque 15.7.3. — Soit X un espace analytique de niveau n ; pour que l’on puisse
le munir d’une structure d’espace tropical de niveau n, il faut et il suffit que X soit
purement de dimension n. En effet, dans le cas contraire, il possède un domaine ana-
lytique compact non vide V tel que dim(V ) < n. L’espace X n’est donc pas riche : la
tropicalisation constante de V n’est couverte par aucun squelette de V puisque la seule
partie squelettique de V est vide.
CHAPITRE 16


COURANTS SUR LES ESPACES ANALYTIQUES




   Soit X un espace k-analytique topologiquement séparé et purement de dimension n.
Pour alléger la terminologie, nous dirons plus simplement que X est un n-espace k-
analytique. Nous l’avons muni d’une structure d’espace G-tropical de niveau n, calibré
et affiné, et démontré (théorème 15.7.1) que muni de son bord au sens de la théorie des
espaces k-analytiques, c’est un espace tropical de niveau n.
   Il en résulte des notions de formes et G-formes différentielles de type (p, q) sur X, à
coefficients dans une classe de coefficients, une théorie de l’intégration des (n, n)-formes
et des (n − 1, n)-formes ainsi qu’une théorie de courants.
   Dans ce chapitre, nous explorons plus avant les propriétés spécifiques des courants
sur les espaces analytiques qui semblent difficilement formulables dans le contexte des
espaces tropicaux.
```

## CLD.txt, newline lines 29080–29148

```text
pour tout entier n ⩾ 1, posons Kn = W n Wn−1 ; les ensembles Kn sont compacts.
L’ensemble ouvert Ωn = Vn+1 Vn−2 est un voisinage de Kn ; par construction, Ωn ne
rencontre pas Ωm si |m − n| ⩾ 3. Pour tout x ∈ Kn , il existe un élément Vx de B contenu
dans un des ensembles Ui et contenu dans cet ouvert Ωn et tel que x ∈ V̊x . Comme Kn est
compact, il existe une partie finie Jn de Kn telle que les V̊x , pour x ∈ Jn , recouvrent Kn .
La famille des Vx , pour n ∈ N et x ∈ Jn , convient.




      § A.2. SÉPARATION, DENSITÉ ET PARTITIONS DE L’UNITÉ

A.2.1. — Nous démontrons ici un certain nombre de résultats généraux et relative-
ment standard concernant la séparation, la densité de certains sous-espaces de fonctions
continues et les partitions de l’unité par de telles fonctions.
   Nous considérons un espace topologique localement compact X (en particulier séparé)
et un sous-faisceau A en R-algèbres du faisceau des fonctions continues à valeurs réelles
sur X. On suppose que pour tout ouvert U de X, tout élément f ∈ A (U ) et toute
fonction lisse φ sur R définie au voisinage de f (U ), la fonction φ ◦ f appartient à A (U ).
   Notons que cette hypothèse est vérifiée dans les deux cas suivants :
   – L’espace X est un espace topologique et A est le faisceau des fonctions continues
sur X ;
   – L’espace X est un espace paralinéaire affiné ou un espace analytique, plus généra-
lement un espace G-tropical affiné, et A est le faisceau des fonctions lisses sur X.
   Pour alléger la rédaction, nous appellerons fonctions lisses les sections du faisceau A .
A.2.2. — On dit que A (X) sépare les points si pour tout couple (x, y) de points de X
tels que x ̸= y, il existe une section globale f de AX telle que f (x) ̸= f (y).
   On dit que A sépare localement les points si pour tout point x de X, il existe un
voisinage ouvert U de X tel que A (U ) sépare les points de U .
                   § A.2. SÉPARATION, DENSITÉ ET PARTITIONS DE L’UNITÉ                      565

Lemme A.2.3. — Supposons que A (X) sépare les points. Soit K un sous-ensemble
compact de X et soit x ∈ X K. Il existe une fonction lisse sur X qui vaut 1 au voisinage
de x et nulle au voisinage de K.
Démonstration. — On commence par traiter le cas où K est réduit à un point y. Par
hypothèse, il existe une fonction lisse f sur X telle que f (x) ̸= f (y). On choisit une
fonction lisse u sur R qui est constante égale à 0 au voisinage de f (x) et constante égale
à 1 au voisinage de y ; l’existence de telles fonctions est classique. La fonction u ◦ f sur X
est lisse et convient.
   D’après ce qui précède, pour tout y ∈ K, il existe une fonction lisse fy sur X valant 1
au voisinage de x et nulle dans un voisinage ouvert Vy de    Qy. Soit S une partie finie de K
telle que les Vy , pour y ∈ S, recouvrent K ; la fonction y∈S fy convient.

Corollaire A.2.4. — On suppose que A sépare localement les points. Soit K une
partie compacte de X et soit U un voisinage ouvert de K. Il existe une fonction lisse
sur X qui vaut 1 au voisinage de K et dont le support est compact et contenu dans U .
Démonstration. — On commence par traiter le cas où le compact K est réduit à un
point x. Soit V un voisinage compact de x tel que A (V̊ ) sépare les points de V̊ . L’en-
semble F = V (V̊ ∩U ) est une partie fermée de X contenue dans V . Soit f une fonction
lisse sur V qui vaut 1 au voisinage de x et qui est nulle au voisinage de F . Soit g la
fonction sur X qui coïncide avec f sur V et qui est nulle en dehors de V . Elle est lisse
sur l’intérieur de V , sur l’ouvert X V ainsi que sur un voisinage ouvert de F dans X ;
ces trois ouverts recouvrent X. La fonction g est donc lisse. Son support est contenu
dans U ; comme il est contenu dans V , il est aussi compact.
   Traitons maintenant le cas général. Pour tout x ∈ K, soit fx une fonction lisse sur X
qui vaut 1 au voisinage de x et dont le support est compact et contenu dans U . Quitte à
remplacer fx par son carré, on suppose que cette fonction est positive ou nulle. Comme K
est compact, la somme g d’une sous-famille finie de ces fonctions est strictement positive
en tout point de K. Elle est lisse et son support est compact et contenu dans U . Soit φ
une fonction lisse de R vers [0; 1], nulle en 0 et égale à 1 sur un voisinage de g(K) ; la
fonction f = φ ◦ g convient.

Théorème A.2.5 (Stone–Weierstraß). — On suppose que A sépare localement les
points. Soit U un ouvert de X et soit f une fonction continue à valeurs réelles sur X
dont le support est compact et contenu dans U . Soit a et b des nombres réels tels que
a ⩽ f (x) ⩽ b pour tout x ∈ X.
  Pour tout ε > 0, il existe une fonction lisse g sur X dont le support est compact,
contenu dans U , et telle que a ⩽ g(x) ⩽ b et |f (x) − g(x)| < ε pour tout x ∈ X.
Démonstration. — Soit X ′ le compactifié d’Alexandroff de X ; comme X est localement
```

## GR.txt, newline lines 302–368

```text
2.11. Relative boundary. An important notion in this paper is that of the relative bound-
ary of a morphism ϕ : X → Y of k-analytic spaces. This is a closed subset of X which we
denote by ∂ (X /Y ). We will not give the details of this definition, but let us try to explain
the literature on the subject. In [Ber90, §2.5], Berkovich defines the relative boundary
∂ (X /Y ) for k-affinoid spaces X and Y . Then in [Ber90, §3.1], he generalizes ∂ (X /Y ) for
good k-analytic spaces using that all points of X and Y have k-affinoid neighborhoods.
Berkovich calls ϕ closed if ∂ (X /Y ) = ;. Berkovich defines ∂ (X /Y ) for arbitrary k-analytic
spaces in [Ber93, 1.5.3(ii)], as follows. A morphism ϕ is closed if for every morphism
Y ′ → Y from a good k-analytic space Y ′ , the fiber product X ′ := X ×Y Y ′ is good and the
canonical morphism X ′ → Y ′ is closed in the previous sense. Finally in [Ber93, Defini-
tion 1.5.4], a point x ∈ X is defined to be in Int(X /Y ) if x has an open neighborhood U
such that ϕ induces a closed morphism U → Y in the above sense. We refer to [Tem15,
Definition 4.2.4.1] for a more explicit equivalent definition of ∂ (X /Y ). Note that in this
paper, we will use the notion closed map in the usual topological sense meaning that it
maps closed sets to closed sets. This is different from Berkovich’s terminology.
   The complement Int(X /Y ) := X \ ∂ (X /Y ) is called the relative interior. We will usually
apply this in the case Y = M (k), in which case we call ∂ X := ∂ (X /M (k)) the boundary
of X and Int(X ) := X \ ∂ X the interior. If ∂ X = ;, we say that X boundaryless. A bound-
aryless space is good by definition. Note that Berkovich calls boundaryless k-analytic
spaces closed.
   We list here some properties of the boundary and interior which we will use throughout
the paper:
   (1) A point x ∈ X is contained in Int(X /Y ) if and only if there is an open neighbor-
       hood U of x such that Int(U/Y ) = U: this is part of the above definition.
   (2) If ϕ : X → Y is finite, then Int(X /Y ) = X [Ber93, Example 1.5.3(iii)].
   (3) If X is an analytic domain in Y , then Int(X /Y ) is the topological interior of X in
       Y [Ber93, Proposition 1.5.5(i)].
             ϕ     ψ
   (4) If X → Y → S are morphisms of k-analytic spaces, then

(2.11.1)                   Int(X /Y ) ∩ ϕ −1 Int(Y /S) ⊂ Int(X /S)

        [Ber93, Proposition 1.5.5(ii)], with equality if ψ is locally separated [Tem04,
        Corollary 5.7]. Taking S = M (k), this becomes

(2.11.2)                      Int(X /Y ) ∩ ϕ −1 Int(Y ) ⊂ Int(X ).

   (5) If k′ /k is an analytic extension field, then

                                π−1
                                 k′ /k
                                       Int(X /Y ) ⊂ Int(X k′ /Yk′ )
8                                      W. GUBLER AND J. RABINOFF

         [Ber93, Proposition 1.5.5(iii)]. Taking Y = M (k), this becomes
                                       π−1
                                        k′ /k
                                              Int(X ) ⊂ Int(X k′ ).
For convenience, we restate these properties in terms of the relative boundary:
   (1′ ) A point x ∈ X is contained in ∂ (X /Y ) if and only if ∂ (U/Y ) ̸= ; for every open
         neighborhood U of x.
   (2′ ) If ϕ is finite, then ∂ (X /Y ) = ;.
   (3′ ) If X is an analytic domain in Y , then ∂ (X /Y ) is the topological boundary of X
         in Y .
               ϕ     ψ
     ′
   (4 ) If X → Y → S are morphisms of k-analytic spaces, then
(2.11.3)                        ∂ (X /S) ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ (Y /S)),
         with equality if ψ is locally separated. Taking S = M (k), this becomes
(2.11.4)                             ∂ X ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ Y ).
    (5′ ) If k′ /k is an analytic extension field, then
                                     ∂ (X k′ /Yk′ ) ⊂ π−1
                                                       k′ /k
                                                             ∂ (X /Y ).
         Taking Y = M (k), this becomes
                                           ∂ X k′ ⊂ π−1
                                                     k′ /k
```

## Additional complete body: CLD.txt, newline lines 15061–15081

```text
les objets sout les couples (X, L) où L est une extension complète de k et X un espace L-
analytique. Un mrophisme de (X, L) vers (Y, M ) est un couple formé d’un k-morphisme
de M vers L et d’un morphisme d’espaces L-analytiques de X vers YL .
   Cette catégorie n’admet pas tous les produits fibrés (par exemple M (Cp ) ×M (Qp )
M (Cp ) n’existe pas en tant qu’espace analytique au-dessus de Qp ) mais si Y → X est
un morphisme d’espaces k-analytiques et X ′ → X un morphisme d’espaces analytiques
au-dessus de k alors Y ×k X ′ existe : si L est le corps de définition fourni avec X ′ , le
produit fibté Y ×k X ′ est simplement le produit fibré YL ×XL X ′ , calculé dans la catégorie
des espaces L-analytiques.
11.1.10. — Soit X un espace k-analytique, et soit x ∈ X.
   On note OX,x la fibre en x de la restriction de OX à la catégorie des ouverts de X,
c’est-à-dire la colimite des OX (U ) où U parcourt l’ensemble des voisinages ouverts de
X. C’est un anneau local dont nous noterons κ(x) le corps résiduel.
   Lorsque X est bon, cet anneau est noethérien ([9], th. 2.1.4), hensélien ([9], th. 2.1.5)
et excellent ([49], th. 2.13).
   Au point x est également associé une extension ultramétrique complète H (x) de k,
qu’on appelle le corps résiduel complété de x ; pour tout domaine analytique V de X
302                  CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

contenant x, on dispose d’un morphisme d’évaluation f 7→ f (x) de OX (V ) dans H (x).
Si X = M (A), le corps H (x) et l’application f 7→ f (x) de A vers H (x) coïncident avec
```

## Additional complete body: CLD.txt, newline lines 15356–15361

```text
kr -analytique de M (kr ) est nulle. Par ailleurs on a kr ⊗kb r = (kr )r ≃ kr {T, S}/(ST − 1),
qui est strictement kr -affinoïde de dimension de Krull n. La dimension k-analytique de
M (kr ) est donc égale à n.


11.2.5. Les composantes irréductibles. — Lorsque nous parlerons d’un espace k-
```

## Additional complete body: CLD.txt, newline lines 6978–6985

```text
Prouvons inversement que cette relation dans des cartes tropicales permet de reconstituer
la mesure de Radon associée à une G-forme de type (n, n) et en donne ainsi une définition
tropicale.
   Soit ω une G-forme de type (n, n) sur X ; supposons-la à support compact et à coef-
ficients tropicalement boréliens localement bornés.
   Soit (Vi )i∈I une famille finie de domaines compacts de X tropicalisant ω et dont dont
la réunion
      T       V recouvre le support de ω. Pour toute partie non vide J de I, posons
```

## Additional complete body: CLD.txt, newline lines 20871–20923

```text
  Soit x un point de Σ et soit y ∈ f −1 (x). Comme dk (x) = n, on a dim(f −1 (x)) = 0, de
sorte que f est quasi-finie en y. Par suite, f −1 (x) est un H (x)-espace analytique fini.
On a ainsi défini au §13.3.6 le nombre rationnel dcx (f ).

Proposition 14.4.2. — Soit p : Y → X un morphisme d’espaces k-analytiques de
niveau n. Soit Σ une partie squelettique de X, soit µΣ son calibrage canonique. Soit T la
partie squelettique p−1 (Σ) de Y (proposition 12.9.6) et soit µT son calibrage canonique.
  Supposons que le morphisme pΣ : T → Σ est topologiquement compact.
  a) La restriction de la fonction x 7→ dcx (p) à toute partie paralinéaire paracompacte
de Σ est localement constante en dehors d’une partie paralinéaire n-négligeable.
  b) On a p∗ µT = dc(p)µΣ .

   Sous les hypothèses de b), les fibres de f en tout point de Σ sont finies, de sorte que
la fonction x 7→ dcx (p) sur Σ est définie. De plus, l’assertion a) donne sens au produit
dc(p)µΣ et montre que c’est un calibrage standard de Σ.
Démonstration. — On sait (proposition 12.9.6) que p induit une immersion par mor-
ceaux compacte de T sur Σ. Ainsi, l’image directe p∗ µT est définie, et est un calibrage
standard de Σ.
   L’espace X est G-recouvert par des domaines analytiques compacts V sur lesquels
il existe un moment f tel que Σ ∩ V ⊂ Σf . Puisque la formation des calibrages cano-
niques et des degrés calibrés commute à la restriction à un domaine analytique, on peut
remplacer X par V et Y par p−1 (V ), ce qui nous ramène à prouver la proposition sous
l’hypothèse supplémentaire que X est compact et qu’il existe un moment f : X → Gnm tel
que Σ soit une partie squelettique de Σf . En remplaçant Y par un voisinage analytique
compact de T, on se ramène au cas où Y est compact.
                                                                                    (n)
   Les moments f et f ◦ p sont agréables et l’on a p−1 (Σf ) = Σf ◦p et p−1 (Σf ) =
 (n)                                                                        (n)
Σf ◦p (prop. 12.9.6). Choisissons une décomposition cellulaire C de Σf            en f -cellules
                                                     (n)
commodes, et une décomposition cellulaire D de Σf ◦p en f ◦ p-cellules commodes, telles
                                             (n)     (n)
que le couple (D, C ) soit adapté à pΣ(n) : Σf ◦p → Σf , à Σ et à T.
                                        f
  Soit C une n-cellule de C et soit D1 , . . . , Dr les n-cellules de D dont l’image par p
                                                   (n)        (n)
est égale à C ; l’immersion par morceaux de Σf ◦p vers Σf induit au-dessus de C̊ un
410          CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

revêtement dont les feuillets sont les D̊i . Soit x ∈ C̊ ; pour tout i, on note yi l’unique
antécédent de x sur D̊i , et l’on pose ξ = f (x).
  Par définition d’une cellule commode, le point x appartient à Int(X). De même, chacun
des yi appartient Int(Y ). Le morphisme f ◦ p est fini et plat en chacun des yi , de degré
degyi (f ◦ p). Le morphisme f est fini et plat en x, de degré degx (f ).
  Pour tout i, on a degyi (f ◦ p) = dcyi (f ◦ p), car f ◦ p est fini et plat en yi . Par
multiplicativité des degrés calibrés, on a degyi (f ◦p) = dcyi (p) dcx (f ), donc degyi (f ◦p) =
dcyi (p) degx (f ) puisque f est fini et plat en x. On a donc
                   Xr                 X r
                          yi
                       deg (f ◦ p) =      dcyi (p) · degx (f ) = dcx (p) degx (f ).
                 i=1                 i=1
Compte tenu de la définition des calibrages canoniques, cela entraîne l’égalité voulue.

```

## Additional complete body: Ducros-S1793744212500077.txt, newline lines 2077–2154

```text
Théorème 3.2. Soit X un espace k-analytique compact et Γ-strict de dimension d,
et soit f = (f1 , . . . , fn ) une famille de fonctions analytiques inversibles sur X ;
notons |f | l’application (|f1 |, . . . , |fn |) de X vers (R∗+ )n . Posons c = (Q, (|k ∗ | · Γ)Q ).
1) L’image |f |(X) est un c-polytope de (R∗+ )n , qui est de dimension inférieure ou
   égale à d.
2) L’image |f |(∂X) est contenue dans un c-polytope de (R∗+ )n qui est de dimension
   inférieure ou égale à d − 1 ; lorsque X est aﬃnoı̈de |f |(∂X) est elle-même un c-
   polytope de (R∗+ )n de dimension inférieure ou égale à d − 1.
    Démonstration. La seconde assertion se déduira de la première.
(3.2.1) Preuve de 1) : réduction à une situation algébrique. On peut supposer
que X est aﬃnoı̈de et irréductible, et l’on procède alors par récurrence sur d. Si d = 0
il n’y a rien à démontrer. Supposons que d > 0 et que 1) est vraie en dimension < d.
     Le théorème à établir est purement topologique. On peut donc supposer k parfait
(en étendant les scalaires au complété de la clôture radicelle de k), et X réduit (en
le remplaçant par Xred ). L’espace X est alors génériquement quasi-lisse. Soit Y son
lieu de non-quasi-lissité. C’est un fermé de Zariski de X dont toutes les composantes
irréductibles sont de dimension < d. Par hypothèse de récurrence, |f |(Y ) est un
c-polytope de (R∗+ )n de dimension ⩽ d − 1. Son image réciproque |f |−1 (|f |(Y )) est
un domaine analytique Γ-strict de X contenant Y . Comme Y → X est sans bord, Y
est contenu dans l’intérieur topologique de |f |−1 (|f |(Y )). Ce dernier apparaı̂t ainsi
comme un voisinage de Y dont l’image par |f | est un c-polytope de dimension
⩽ d − 1.
     Soit x ∈ X − Y . Comme X est quasi-lisse en x, le lemme 0.21 assure l’existence
d’un voisinage aﬃnoı̈de V de x dans X, et d’une k-variété aﬃne X de dimension d,
telle que V s’identiﬁe à un domaine aﬃnoı̈de Γ-strict de X an (on peut imposer à X
d’être lisse, mais nous ne nous en servirons pas).
     Par compacité de X, on se ramène ﬁnalement au cas où X lui-même est est un
domaine aﬃnoı̈de Γ-strict de l’analytiﬁcation X an d’une k-variété algébrique X
aﬃne de dimension d.
     Écrivons X ≃ Spec A où A est une k-algèbre de type ﬁni, et soit (a1 , . . . , ar )
un système de générateurs de A. Il existe R ∈ Γ · |k ∗ | tel que X soit contenu
dans le domaine aﬃnoı̈de W de X an déﬁni par les conditions |ai | ⩽ R. En vertu
du théorème de Gerritzen-Grauert (0.20.7), le domaine X est réunion ﬁnie de
domaines Γ-rationnels de W ; il suﬃt dès lors de traiter le cas où X est lui-même
un domaine Γ-rationnel de W .
     Il est alors déﬁni par une conjonction d’inégalités de la forme |gi | ⩽ λi |h| où les λi
appartiennent à Γ et où (g1 , . . . , gr , h) engendre l’idéal des fonctions analytiques
sur W . Cette dernière condition implique que h ne s’annule pas sur X (tout zéro
de h sur X est un zéro commun à h et aux gi ), et l’on peut donc, par compacité,
                                            1250007-40
                            Espaces de Berkovich, polytopes, squelettes et théorie des modèles


rajouter une condition de la forme |h| ⩾ r à la déﬁnition de X, où r est un élément
convenable de (Γ · |k ∗ |)Q . Il est dès lors immédiat que V ne change pas si l’on
perturbe un peu les gi et h ; on peut par conséquent supposer que toutes ces
fonctions appartiennent à A.
    L’anneau des fonctions de la forme a/h , où a ∈ A, et  ⩾ 0, est dense dans
l’anneau des fonctions de X. Cela permet de supposer, quitte à remplacer X
par D(h), à remplacer gi par gi /h et à approcher convenablement chacune des fi ,
que fi ∈ A pour tout i et que h = 1.
(3.2.2) Nature c-polytopale de |f |(X) dans le cas algébrique. Soit (F, |.|) une
extension valuée de k (on ne suppose pas que le groupe ordonné |F ∗ | est de
rang 1). On peut donner un sens naturel à la notation X(F ), coı̈ncidant avec sa
signiﬁcation usuelle lorsque F est un corps ultramétrique complet : c’est le sous-
ensemble de X (F ) formé des points P tels que |gi (P )| ⩽ λi pour tout i.
    Le théorème 1.2 assure l’existence d’un sous-foncteur fermé et déﬁnissable D
de GnΓ·|k∗ | , de dimension majorée par d (les notations et déﬁnitions sont celles de
0.32 et sq.) tel que
                             |f |(X(F )) = D(|F ∗ |) ⊂ |F ∗ |n
pour tout F ∈ Ck,Γ·|k∗ | .
     Si F est une extension ultramétrique complète et algébriquement close de k
munie d’un |k ∗ |-isomorphisme |F ∗ | ≃ R∗+ , tout point P de X(F ) déﬁnit un point x
de l’espace k-aﬃnoı̈de X, et |f |(x) = |f |(P ) ∈ (R∗+ )n .
     Réciproquement si x ∈ X il existe une extension complète et algébriquement
close F de H (x) et un |H (x)∗ |-isomorphisme |F ∗ | ≃ R∗+ , et x est alors induit par
un F -point canonique de X.
     En conséquence, le compact |f |(X) est le sous-ensemble D(R∗+ ) de (R∗+ )n , ce
qui achève de prouver 1).
                                                                                  
(3.2.3) Démonstration de l’assertion 2. Si X s’écrit comme une réunion ﬁnie Xi
où les Xi sont aﬃnoı̈des et Γ-stricts, son bord est contenu dans la réunion des bords
des Xi . On peut donc supposer que X est aﬃnoı̈de, auquel cas le résultat découle
de l’assertion 1) déjà établie et du lemme 3.1.
(3.3) Remarque. Faute d’avoir réussi à exhiber une description suﬃsamment
maniable de ∂X en général, l’auteur ignore s’il peut arriver que |f |(∂X) ne soit
pas un polytope, lorsque X n’est pas aﬃnoı̈de. Il serait évidemment intéressant de
disposer d’un tel exemple — ou, au contraire, d’une preuve que |f |(∂X) est toujours
```

## Application of the underlying Ducros polyhedrality theorem

Ducros Theorem3.2(1) is used only for the compact strict affinoid moment domains in the finite separable curve argument. With Γ={1}, K nontrivially valued, these are compact Γ-strict analytic spaces of dimension1; finite analytic unit tuples have finite polyhedral image of dimension at most1. The proof's preliminary reductions concern only the topological moment image and do not replace the actual algebra in canonical measures. Its model-theoretic Theorem1.2 is explicitly an underlying foundational dependency of the cited polyhedrality theorem, not a new result proved here. The cited primary theorem applies precisely under these hypotheses. No claim of universal moment-image dimension equality is used.

## CLD-curve, newline lines 910--978

```text
qui est croissante et d’image I sur {1, . . . , p} et est croissante sur {p + 1, . . . , n}. Si K
et L sont des parties à n − p éléments de {1, . . . , n}, on a
                                      (
                                        (−1)p(n−p) εI εJ λ ∧ Jλ si K = ∁I et L = ∁J,
           ω ∧ d′ xK ∧ J d′ xL =
                                        0                            sinon.
En outre, φeK = εK d′ x∁K , si bien que
                                (
                                 (−1)p(n−p) λ ∧ Jλ si I = K et J = L,
                bω (eK , eL ) =
                                 0                 sinon.
                                § 1.2. SUPERFORMES POSITIVES                                  25

Enfin,                                                      (
                                                             1 si I = K et J = L,
               qω (eK , eL ) = ⟨d′ xI , eK ⟩⟨d′ xJ , eL ⟩ =
                                                             0 sinon,
d’où la formule annoncée.
   En outre, les formules précédentes entraînent que les signes de ces diverses formes sont
reliées par les équivalences suivantes :
La forme ω est positive au sens de la définition 1.2.3 ;
⇔ L’application bilinéaire (α, β) 7→ ω ∧ α ∧ Jβ est de signe σn−p ;
⇔ L’application bilinéaire bω est de signe σn−p ;
⇔ La forme bilinéaire qω est de signe σn−p (−1)p(n−p) σn = σp .
   Enfin, si f : W → V est une application linéaire, on a qf ∗ ω = qω ◦ (f, f ).
   Nous dirons qu’une (p, p)-forme symétrique est définie positive si la forme bilinéaire
symétrique σp qω est définie positive.
Lemme 1.2.7. — Soit ω ∈ Ap,p (V ) une forme symétrique de type (p, p), soit
(x1 , . . . , xn ) une base de V et soit
                                                X
                               ω = (−1)p(p−1)/2   ωI,J d′ xI ∧ d′′ xJ
                                               I,J

la décomposition de ω dans la base correspondante de Ap,p (V ). Alors, les quatre propriétés
suivantes sont équivalentes :
   a) La forme ω est positive ( resp. définie positive) ;
   b) La matrice symétrique (ωI,J ) (indexée par les parties à p éléments de {1, . . . , n})
est positive ( resp. définie positive) ;
   c) Il existe une base (αI ) de Λp V ∗ et une famille (cI ) de nombres réels positifs ou nuls
( resp. strictement positifs), indexées par les parties à p éléments de {1, . . . , n}, telles
que                                             X
                              ω = (−1)p(p−1)/2     cI αI ∧ J(αI ).
                                                     I

Démonstration. — L’équivalence des assertions (1) et (2) résulte de la discussion qui
précède le lemme et de ce qu’avec les notations introduites, la matrice (ωIJ ) est celle de
la forme bilinéaire (−1)p(p−1)/2 qω dans la base duale de la base (d′ xI )I de Λp V ∗ . Celle des
propriétés (2) et propriétés (3) découle de la diagonalisation des formes quadratiques.

Corollaire 1.2.8. — L’ensemble des formes positives dans Ap,p (V ) est le cône convexe
fermé engendré par les formes du type (−1)p(p−1)/2 α ∧ Jα, où α parcourt l’ensemble des
formes de type (p, 0).
Démonstration. — Le lemme précédent montre que les formes positives sont contenues
dans ce cône. Inversement, si α ∈ Ap,0 (V ) est une forme de type (p, 0) et β est une
(n − p, 0)-forme, la formule
     (−1)p(p−1)/2 α ∧ Jα ∧ (−1)(n−p)(n−p−1)/2 β ∧ Jβ = (−1)n(n−1)/2 (α ∧ β) ∧ J(α ∧ β)
montre que (−1)p(p−1)/2 α ∧ Jα est une forme positive, d’où l’autre inclusion.

Corollaire 1.2.9. — La condition de positivité est auto-duale : une forme α, symé-
trique de type (p, p), est positive si et seulement si α ∧ β est positive pour toute forme
positive β de type (n − p, n − p).
26 CHAPITRE 1. SUPERFORMES SUR UN ESPACE VECTORIEL RÉEL (D’APRÈS LAGERBERG)

Démonstration. — Cela résulte immédiatement du corollaire précédent.

Corollaire 1.2.10. — Les trois notions de positivité coïncident pour les formes de
bidegrés (0, 0), (1, 1), (n − 1, n − 1) et (n, n).
   Elles ne coïncident pas en général, pas plus que leurs analogues en géométrie complexe.
Démonstration. — Le cas des formes de type (0, 0) et (n, n) a déjà été expliqué. Par
```

## CLD-curve, newline lines 6860--7020

```text
sur le site topologique de X. Le lemme est ainsi démontré.


Proposition 5.9.3. — Notons π : XG → X le morphisme canonique de sites. Il existe
un unique morphisme de faisceaux π∗ FXn−1,n
                                          G
                                              → π∗ VXn−1
                                                       G
                                                          sur l’espace topologique X, noté
ω 7→ ω
     e , qui prolonge l’application définie en (5.9.1) lorsque ω possède un support fort.
Ce morphisme est FX0,0 -linéaire.

Démonstration. — Compte tenu du lemme 5.9.2, cela résulte de ce que toute G-forme
sur un ouvert paracompact possède un support fort, et que tout espace G-tropical est
recouvert par ses ouverts paracompacts.

5.9.4. — Explicitons cette construction lorsque ω est tropicale. Soit f : X → E une
carte G-tropicale et soit α une (n − 1, n)-forme sur un sous-espace paralinéaire de E
                                             (n)
contenant f (X) telle que ω = f ∗ α. Alors, Σf est un support fort de ω (lemme 5.3.4)
                                                                             (n)
et on a l’égalité de formes-volume (n − 1)-dimensionnelles sur Σf                  :

(5.9.4.1)                                 ω̃ = ⟨f ∗ α, µΣ(n) ⟩.
                                                            f


Si, de plus, l’application f |Σ(n) est topologiquement propre, la proposition 4.5.8 entraîne
                               f
alors que

(5.9.4.2)                       ftrop,∗ (ω̃) = ⟨α, f∗ µΣ(n) ⟩ = ⟨α, µΠf ⟩.
                                                        f


Rappelons alors (cf. §4.6.13) que la forme-volume (n − 1)-dimensionnelle ⟨α, µΠf ⟩ se
calcule par accouplement avec la discordance du calibrage de Πf .

Proposition 5.9.5 (Compensation des bords). — Soit (Xi )i∈I un G-recouvrement
localement fini de X et soit ω ∈ FXn−1,n
                                     GT
                                         (X) une G-forme de type (n − 1, n) sur X.
Pour toute partie J de I, notons XJ = j∈J Xj et uJ l’immersion de XJ dans X. On a
l’égalité
                                X
                           ω̃ =     (−1)Card(J)−1 (uJ )∗ ω|
                                                         g XJ .
                                      ∅̸=J⊂I


Démonstration. — En raisonnant localement, on suppose que X est paracompact et
donc que ω possède un support fort. La formule découle alors de la proposition 4.6.6.
                         § 5.10. INTÉGRALES ET TROPICALISATIONS                           139

5.9.6. — Soit ω une G-forme de type (n − 1, n) sur X à coefficients tropicalement
boréliens. Nous venons de lui associer une forme-volume (n − 1)-dimensionnelle ω̃. Nous
noterons alors ωBor la mesure de Borel sur X associée par la construction du §5.7.1.
   Lorsque la forme-volume ω̃ est localement intégrable, la mesure ωBor est localement
finie ; on note alors ω|Rad la mesure de Radon associée à ω̃. On a |ωRad | = ωBor .
                                                     R∂         R∂
   Si f est une fonction borélienne sur X, on notera X f |ω| et X f ω les intégrales de f
contreR les mesures ωBor et ωRad lorsqu’elles existent. Cela définit en particulier l’inté-
         ∂
grale X ω pour toute G-forme de type (n − 1, n) à support compact qui est localement
intégrable (par exemple lisse).



               § 5.10. INTÉGRALES ET TROPICALISATIONS

  Soit X un espace G-tropical calibré de niveau n.
Proposition 5.10.1. — Soit f : X → E une carte G-tropicale agréable, soit Πf le
polyèdre tropical de la carte f et soit µΠf son calibrage.
  Soit p ∈ {n−1, n} et soit α une (p, n)-forme à coefficients boréliens sur un sous-espace
paralinéaire P de E contenant f (X).
  a) Si p = n, on a l’égalité
                                   ftrop,∗ (f ∗ α)Bor ⩾ ⟨α, µΠf ⟩Bor
                             (n)
de mesures de Borel sur Πf .
  b) Si p = n − 1, on a l’inégalité
                                   ftrop,∗ (f ∗ α)Bor ⩾ ⟨α, µΠf ⟩Bor
                             (n)
de mesures de Borel sur Πf .
  c) La mesure (f ∗ α)Bor est localement finie si et seulement si la forme α|Πf est locale-
ment intégrable sur Πf ; dans ce cas, on a l’égalité
                                   ftrop,∗ (f ∗ α)Rad = ⟨α, µΠf ⟩Rad
de mesures de Radon sur Πf .
   d) En particulier, si α est intégrable sur Πf , la forme f ∗ α est intégrable sur X, on a
l’égalité
                                   Z         Z
                                        ∗
(5.10.1.1)                            f α=       ⟨α, µΠf ⟩
                                        X           Πf

lorsque p = n et l’égalité
                                      Z ∂          Z ∂
                                            ∗
(5.10.1.2)                                  f α=         ⟨α, µΠf ⟩
                                        X           Πf

lorsque p = n − 1.
Démonstration. — Posons ω = f ∗ α. D’après la relation (5.8.4.2) lorsque p = n et la
relation (5.9.4.2) lorsque p = n−1, on a l’égalité (ftrop )∗ (ω̃) = ⟨α, µΠf ⟩ de formes-volume
p-dimensionnelles sur Πf . Le lemme 4.4.6 entraîne alors que f∗ (ω̃Bor ) ⩾ ⟨α, µΠf ⟩Bor .
Loreque p = n, on vérifie, en revenant aux définitions et en utilisant la positivité du
140                   CHAPITRE 5. ESPACES G-TROPICAUX CALIBRÉS

calibrage canonique, que l’on a en fait l’égalité, d’où (1). En appliquant le lemme 4.4.6
aux mesures de Radon correspondantes, on en déduit (2), puis (3) par intégration.

5.10.2. — La formule (5.10.1.1) définit explicitement l’intégrale d’une forme tropicale.
Prouvons inversement que cette relation dans des cartes tropicales permet de reconstituer
la mesure de Radon associée à une G-forme de type (n, n) et en donne ainsi une définition
tropicale.
   Soit ω une G-forme de type (n, n) sur X ; supposons-la à support compact et à coef-
ficients tropicalement boréliens localement bornés.
   Soit (Vi )i∈I une famille finie de domaines compacts de X tropicalisant ω et dont dont
la réunion
      T       V recouvre le support de ω. Pour toute partie non vide J de I, posons
VJ = j∈J Vj . On a alors
                          Z        Z       X                  Z
                                                    Card(J)−1
                              ω=       ω=       (−1)            ω.
                          X       V       ∅̸=J⊂I              VJ

Pour toute partie non vide J, la forme ω est tropicaleR sur VJ , et VJ est compact, si bien
que toute carte G-tropicale sur VJ . Ainsi, l’intégrale VJ ω peut se calculer à l’aide de la
formule (5.10.1.1).



                 § 5.11. FORMULES DE STOKES ET GREEN

  Soit X un espace G-tropical calibré de niveau n.
Proposition 5.11.1. — a) Soit ω une G-forme à coefficients C 1 et à support com-
pact sur X, de type (n − 1, n). On a la formule de Stokes :
                                   Z         Z ∂
                                        ′
                                       d ω=      ω.
                                      X                X
   b) Soit α et β des G-formes à coefficients C sur X, symétriques, de type (p, p) et (q, q)
                                                   2

respectivement, où p + q = n − 1. Si l’intersection de leurs supports est compact, on a la
formule de Green :
                 Z                               Z ∂
                          ′ ′′     ′ ′′
                    (α ∧ d d β − d d α ∧ β) =        (α ∧ d′′ β − d′′ α ∧ β).
                  X                                    X

Démonstration. — Comme le support de ω est compact, il existe une partie squelettique
fermée Σ de X qui la supporte fortement. La formule de Stokes découle alors de la
formule correspondante en géométrie paralinéaire (proposition 4.6.15), appliquée à Σ(n) ,
à la forme ω|Σ(n) et au calibrage canonique de Σ(n) .
   La formule de Green s’en déduit comme dans le lemme 1.5.10 en appliquant la formule
de Stokes à la forme à support compact ω = α ∧ d′′ β − d′′ α ∧ β. Lorsque α et β sont
toutes deux à support compact, elle découle aussi de la formule de Green en géométrie
paralinéaire, appliqué à une partie polyédrale qui supporte fortement ces deux formes.
CHAPITRE 6

```

## CLD-curve, newline lines 15082--15286

```text
bon en x. Un espace bon est presque bon. Le point x est traditionnellement dit rigide si
H (x) est une extension finie de k (la terminologie provient du fait que ces points sont
ceux considérés par Tate dans sa théorie des espaces analytiques rigides).
   Soit f : Y → X un morphisme entre espaces k-analytiques et soit x ∈ X. La fibre
f (x) possède une structure naturelle d’espace H (x)-analytique, et sera toujours im-
  −1

plicitement considérée comme munie de cette structure. Nous la noterons souvent Yx .
11.1.11. — Berkovich a construit ([9], 2.6) un foncteur d’analytification X 7→ X an
qui va de la catégorie des A-schémas localement de type fini vers celle des bons espaces
k-analytiques. L’espace X an est muni d’un morphisme d’espaces localement annelés
X an → X qui est fidèlement plat ([9], Prop. 2.6.2). L’application π induit une bijection
entre l’ensemble X0an des points rigides de X an et l’ensemble X0 des points fermés
de X , qui préserve les corps résiduels ; on en tire en particulier une bijection entre
{x ∈ X an , H (x) = k et X (k), qui est un homéomorphisme (la source étant munie de
la topologie induite par celle de X an , et le but de la topologie déduite de celle de k). Si
|k × | ̸= {1}, l’ensemble X0an est dense dans X an .
   Si x est un point de X an d’image ξ sur X , le morphisme local OX ,ξ → OX an ,x est
régulier ([49], théorème 3.3).
   Donnons quelques détails sur la construction de X an lorsque X est affine. Écrivons
X = Spec A où A est une k-algèbre de type fini. Topologiquement, X an est l’en-
semble des semi-normes multiplicatives sur A qui induisent la valeur absolue structurale
sur k, muni de la topologie induite par la topologie produit sur RA ; le morphisme de
X an vers X envoie une semi-norme sur son noyau. Fixons un système fini de géné-
rateurs a1 , . . . , am de A, et soit I le noyau de la surjection Ti 7→ ai de k[T1 , . . . , Tm ]
sur A. Pour tout R > 0 le sous-ensemble VR de X an constitué des points x tels que
|ai (x)| ⩽ R pour tout i est un domaine affinoïde de X an , d’algèbre affinoïde associée
k{T1 /R, . . . , Tn /R}/I. L’espace X an est la réunion croissante des VR , qui en constituent
un G-recouvrement.
   On dispose d’un théorème GAGA dans ce contexte : si X est propre et si π désigne
le morphisme structural de X an vers X alors F 7→ π ∗ F établit une équivalence entre
la catégorie des faisceaux cohérents sur X et celle des faisceaux cohérents sur X an , qui
préserve les groupes de cohomologie ([109], annexe A).
   Le foncteur d’analytification commute à la formation des produits fibrés.
   Pour tout espace analytique X et tout entier n, l’application f 7→ (f ∗ T1 , . . . , f ∗ Tn )
met en bijection Hom(X, An,an   k  ) et OX (X)n .

                                                                                        aI T I 7→
                                                                                      P
Exemple 11.1.12. — Soit r = (r1 , . . . , rn ) un polyrayon. L’application
max|aI | · rI de k[T1 , . . . , Tn ] vers R+ est une norme multiplicative prolongeant la valeur
absolue de k. C’est donc un point ηr de An,an     k  , situé au-dessus du point générique de Ank .
Le corps H (ηr ) est le complété de k(T1 , . . . , Tn ) pour la valeur absolue induite par ηr .
  Lorsque r est k-libre le corps H (ηr ) s’identifie au corps k-affinoïde kr décrit en 11.1.3
(ce dernier contient en effet k(T1 , . . . , Tn ) comme sous-corps dense), le singleton {ηr } est
     § 11.1. GÉOMÉTRIE ANALYTIQUE : CONVENTIONS, NOTATIONS, PREMIERS RAPPELS                     303

alors le domaine affinoïde de An,an
                               k    défini par les égalités |Ti | = ri pour tout i, et l’on a
OAk ({ηr }) = kr .
   n,an




Exemple 11.1.13      P (La droite affine). —i Pour tout a ∈ k et tout réel r, notons
ηa,r l’application      ai (T − a) 7→ max|ai |r de k[T ] vers R+ . C’est une semi-norme
multiplicative, et donc un point de Ak1,an ; si r = 0 c’est l’application P 7→ |P (a)| de
noyau (T − a), et ηa,0 est donc le k-point standard d’équation T = a ; si r > 0 alors ηa,r
est une norme, ce qui revient à dire que ηa,r est situé au-dessus du point générique de
A1k . On a ηa,r = ηb,s si et seulement si r = s ⩾ |b − a|. Si |k × | est dense dans R×  + on a
|P (ηa,r )| = supb∈k,|b−a|⩽r |P (b)|.
   On a H (ηa,0 ) = k. Supposons r > 0 et posons τ = (T −  ^ a)(ηa,r ).Il résulte de l’exemple
10.8.4 que τ est transcendant sur e k et que H^
                                              (ηa,r ) = e
                                                        k(τ ).
    Donnons quelques précisions supplémentaires dans deux cas extrêmes. Si r = |λ| avec
                                                                           1
λ ∈ k × alors H (η
                 ^  a,r ) = k(τ /λ). Comme |τ /λ| = 1 on voit que H (ηa,r ) est égal à
                            e e                e                    ^
k 1 (τ /λ),
e       e et est donc une extension rationnelle de degré de transcendance 1 de ek 1 ; de
                                                                 1
                                        / |k × |Q alors H^
même, on a |H (ηa,r )× | = |k × |. Si r ∈                          k 1 et |H (ηa,r )× | = |k × |·rZ .
                                                         (ηa,r ) = e
  Supposons maintenant que k est algébriquement clos (auquel cas |k × | est divisible).
On démontre alors (voir [8], 1.4.4) que tout point de A1,an    k  est de l’un des quatre types
suivants.
   – Les points de type I sont les points rigides, c’est-à-dire ceux pour lesquels H (x) = k,
ou encore les points de la forme ηa,0 pour a ∈ k.
   – Les points de type II sont les points de la forme ηa,r où a ∈ k et où r ∈ |k × |. Si x
                                1
est de type II le corps H ^  (x) est une extension rationnelle de degré de transcendance 1
de ke1 et |H (x)× | = |k × |. En particulier dk (x) = 1.
   – Les points de type III sont les points de la forme ηa,r où a ∈ k et où r ∈         / |k × |. Si
                                     1
x est de type III le corps H   ^  (x) est égale à ek 1 et |H (x)× | = |k × | · rZ . En particulier
dk (x) = 1.
   – Les points de type IV n’existent que si le corps k n’est pas maximalement complet,
c’est-à-dire s’il existe des familles totalement ordonnées de boules fermées de k d’inter-
section vide (c’est par exemple le cas si k = Cp , ou si k est le complété du corps des
séries de Puiseux sur C). Si (B(ai , ri ))i est une telle famille de boules, le point x de type
IV qu’on lui associe est la semi-norme inf i ηai ,ri , qui est en fait une norme. Le point x
est donc situé au-dessus du point générique de A1,an     k . Le corps complet H (x) est une
extension immédiate de k, c’est-à-dire que H (x) = e
                                                  ^         k, ou encore que H (x) a même
groupe des valeurs et même corps résiduel (au sens classique) que k ; et cette extension
est stricte. On a dk (x) = 0.

11.1.14. — Rappelons ([36], chap. 1, §9, no 10, définition 6, p. 69) qu’un espace to-
pologique X est dit paracompact s’il est séparé et si tout recouvrement ouvert possède
un raffinement qui est localement fini. Un espace compact est paracompact. Une partie
fermée d’un espace paracompact est paracompacte.
   Un espace localement compact est dit dénombrable à l’infini s’il est réunion dénom-
brable d’ensembles compacts ; un espace localement compact dénombrable à l’infini est
304                CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

paracompact. Plus généralement, un espace topologique localement compact est pa-
racompact si et seulement si c’est l’espace somme d’une famille d’espaces localement
compacts dénombrables à l’infini (loc. cit., théorème 5, p. 70).
Lemme 11.1.15 (cf. [9], remarque 1.2.4 (iii)). — Un espace analytique possède
une base de voisinages ouverts dénombrables à l’infini (et donc paracompacts).
   Cet énoncé figure dans [8, 2.2.8 et 3.2.1] pour les espaces affinoïdes ; nous détaillons
ci-dessous les arguments de la remarque 1.2.4, (iii), de [9] qui l’en déduit.
Démonstration. — Soit x un point de X. Nous allons montrer que tout voisinage de x
dans X contient un voisinage ouvert de x qui est dénombrable à l’infini. On peut pour
ce faire restreindre X et donc le supposer topologiquement séparé. Le point x possède
alors une base de voisinages compacts dans X qui sont des réunions finies de domaines
affinoïdes contenant x. On peut donc supposer que X est compact et est une union finie
V1 ∪V2 . . .∪Vn de domaines affinoïdes contenant x ; on se donne un voisinage ouvert U de
x dans X et on veut montrer qu’il contient un voisinage ouvert de x qui est dénombrable
à l’infini. Raisonnons par récurrence sur n. Si n = 1 alors X est affinoïde et le résultat
est connu dans ce cas comme on l’a rappelé. Supposons n > 1 et le résultat vrai pour
n − 1. Posons W = V1 ∪ · · · ∪ Vn−1 . Par récurrence, x possède un voisinage ouvert et
dénombrable à l’infini Ω dans W ∩ U , dont l’intersection ω avec Vn est un voisinage
ouvert et dénombrable à l’infini de x dans W ∩ Vn ∩ U . Soit (Ki )i⩾0 une suite de parties
compactes de W ∩ Vn telles que ω = i⩾0 Ki et Ki ⊂ K˚
                                       S
                                                           i+1 pour tout i. Soit i ⩾ 0. Soit
y ∈ Ki ; il existe un voisinage Ωy de y dans Vn tel que Ωy ∩ W ∩ Vn ⊂ K̊i+1 ; par le cas
affinoïde on peut supposer, quitte à le restreindre, que Ωy est un ouvert dénombrable
à l’infini de Vn ∩ U . L’espace Ki étant compact, il est recouvert par un nombre fini de
ces ouverts Ωy de Vn ; leur réunion est un voisinage Ωi de Ki dans Vn ∩ U , ouvert et
dénombrable à l’infini, tel que Ωi ∩ W ∩ Vn ⊂ K̊i+1 . La réunion Ω′ des Ωi est un voisinage
ouvert de x dans Vn ∩ U , ouvert et dénombrable à l’infini, et Ω′ ∩ W ∩ Vn = ω. La réunion
Ω ∪ Ω′ est dénombrable à l’infini et contient x. On peut écrire Ω = Υ ∩ W et Ω′ = Υ′ ∩ Vn
où Υ et Υ′ sont deux ouverts de X contenus dans U . Quitte à remplacer Υ par son
intersection avec le complémentaire dans X du compact Vn ω, on peut supposer que
Υ∩Vn = ω ; et quitte à remplacer Υ′ par son intersection avec le complémentaire dans X
du compact W ω, on peut supposer que Υ′ ∩ W = ω. Mais on a alors Ω ∪ Ω′ = Υ ∪ Υ′ ,
si bien que Ω ∪ Ω′ est un voisinage ouvert de x dans U .




      § 11.2. TOPOLOGIE DE ZARISKI, THÉORIE DE LA DIMENSION

11.2.1. Topologie de Zariski. — Soit X un espace k-analytique. Pour tout faisceau
cohérent d’idéaux I sur X on note V (I ) son lieu des zéros, c’est-à-dire l’ensemble
des point x de X tel que f (x) = 0 pour toute section f de I définie sur un domaine
analytique de X contenant x. Les parties de X de la forme V (I ) sont les fermés d’une
topologie appelée topologie de Zariski de X.
   Supposons que X est affinoïde, et écrivons X = M (A). Se donner un faisceau cohérent
d’idéaux I sur X revient alors à se donner un idéal I de A (on a I = Ie et I = I (X)),
et V (I ) est alors l’image réciproque de V (I) par la surjection continue de M (A) vers
                § 11.2. TOPOLOGIE DE ZARISKI, THÉORIE DE LA DIMENSION               305

Spec A (il est en particulier compact). On dispose donc dans ce cas d’une bijection
croissante entre l’ensemble des fermés de Zariski de M (A) et l’ensemble des fermés de
Zariski de Spec A. En particulier la topologie de X est noethérienne.
  On ne suppose plus X affinoïde. Les fermés de Zariski de X sont fermés dans X (cela se
vérifie G-localement, ce qui perrmet de se ramener au cas affinoïde). Si X est compact,
sa topologie de Zariski est noethérienne (on le déduit du cas affinoïde en écrivant X
comme une union finie de domaines affinoïde).
11.2.2. Sous-espaces analytiques fermés. — Soit X un espace k-analytique et soit
I un faisceau cohérent d’idéaux sur X. Supposons d’abord que X est affinoïde, et
écrivons X = M (A). Posons I = I (X). Le fermé V (I ) coïncide avec l’ensemble des
x dans M (A) tel que f (x) = 0 pour tout x ∈ I, qui est homéomorphe à M (A/I) via
le morphisme induit par la surjection canonique de A vers A/I. Ainsi, V (I ) peut être
muni d’une structure d’espace k-analytique, dépendant du choix de l’idéal I , et d’un
morphisme de V (I ) dans X dont l’application continue sous-jacente est l’inclusion.
   On ne suppose plus X affinoïde. En procédant G-localement à la construction pré-
cédente puis en recollant on obtient une structure d’espace k-analytique au-dessus de
X sur V (I ), l’application continue sous-jacente au morphisme de V (I ) dans X étant
l’inclusion i : V (I ) ,→ X, et i∗ OV (I ) = OX /I .
   Un sous-espace analytique fermé de X est un fermé de Zariski Y de X muni d’une
structure d’espace k-analytique au-dessus de X induite selon le procédé décrit ci-dessus
par un faisceau cohérent d’idéaux I tel que Y = V (I ) ; notons que I se reconstitue
alors à partir de cette structure comme le noyau de OX → i∗ OY , où i : Y → X est le
morphisme structural, qui est topologiquement l’inclusion.
   Tout fermé de Zariski Y possède au moins une structure de sous-espace analytique
fermé : celle donnée par le faisceau

                 J := V 7→ {f ∈ O(V ), f (x) = 0 pour tout ∈ Y ∩ V

qui est bien cohérent ([49], Prop. 4.2.1). C’est la plus petite structure de sous-espace
analytique fermé sur Y , au sens où J est le plus grand faisceau cohérent d’idéaux
sur X définissant le fermé Y ; c’est aussi la seule structure de sous-espace analytique
fermée sur Y dont le faisceau structural n’a pas de sections nilpotentes non nulles ;
on l’appelle la structure réduite sur Y . Si Y = X la structure réduite est associée au
faisceau d’idéaux dont les sections sont les fonctions localement nilpotentes ; le sous-
espace analytique fermé correspondant est noté Xred . Le morphisme Xred ,→ X induit
un homéomorphisme entre Xred et X pour leur topologies usuelles, mais aussi pour leurs
topologies de Zariski.
   Si Y est un sous-espace analytique fermé de X, il résulte du théorème de Gerritzen-
Grauert dans sa version due à Temkin ([128], Th. 3.1) que les domaines analytiques de
Y sont les sous-ensembles de Y qui admettent un G-recouvrement par des parties de la
forme V ∩ Y où V est un domaine affinoïde de X.
   Si V est un domaine analytique de X la topologie de Zariski de V est plus fine que la
topologie de V induite par la topologie de Zariski de X, et en général strictement plus
fine.
   Si E est une partie de X et si (Xi ) est un G-recouvrement de X par des domaines
analytiques, alors E est un fermé (resp. un ouvert) de Zariski de X si et seulement si
```

## CLD-curve, newline lines 15362--15566

```text
                                                                                    k      est
un ensemble infini de points rigides tendant vers l’infini. C’est donc un fermé de Zariski
de A1,an possédant une infinité de composantes connexes.
   On peut néanmoins développer une théorie des composantes irréductibles en géométrie
analytique sur k. Brian Conrad l’a fait dans [43] (dans le cas strictement k-analytique)
en procédant comme en géométrie complexe, c’est-à-dire en construisant d’abord le nor-
malisé X e d’un espace k-analytique, puis en définissant les composantes irréductibles de
X comme les images des composantes connexes de X.        e Dans ce texte, nous nous ap-
puierons sur une approche différente présentée dans [49], que nous allons brièvement
rappeler.
   On y démontre tout d’abord que si X est un espace k-analytique irréductible, il est
purement de dimension d pour un certain entier d, et tout fermé de Zariski strict de
X est alors de dimension
                  S          < d ([49], cor. 4.14) puis que si X s’écrit comme une union
localement finie i Xi de fermés de Zariski irréductibles alors X est égal à l’un des Xi .
   Si X = M (A) est un espace affinoïde, sa topologie de Zariski est noethérienne et il
possède donc un ensemble fini de composantes irréductibles pour cette topologie, que l’on
appelle simplement les composantes irréductibles de X. Ce sont les images réciproques
des composantes irréductibles de Spec A.
   Si X est un espace k-analytique quelconque, on appelle composante irréductible de X
toute partie de X qui est l’adhérence pour la topologie de Zariski de X d’une composante
irréductible d’un domaine affinoïde de X. On démontre ([49], Th. 4.20) que les compo-
santes irréductibles de X constituent un ensemble localement fini de fermés de Zariski
irréductibles de X qui recouvrent X, sont deux à deux non comparables pour l’inclusion
et sont maximaux ; plus précisément, tout fermé irréductible de X est contenu dans une
composante irréductible
                S          de X. Si E est un ensemble de composantes irréductibles de
X, la réunion Z∈E Z est un fermé de Zariski de X dont les éléments de E sont les
composantes irréductibles.
   Si x est un point de X l’entier dimx X est le maximum des dimensions des composantes
irréductibles de X contenant x ([49], Lemme 4.21).
308                 CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

   Soit V un domaine analytique de X. Pour toute composante irréductible Y de X,
l’intersection Y ∩ V est une union (éventuellement vide, éventuellement infinie) de com-
posantes irréductibles de V de même dimension que Y ; pour toute composante irréduc-
tible T de V , l’adhérence de Zariski Z de T dans X est une composante irréductible de
X de dimension dim T , et T est une composante irréductible de Z ∩ V ([49], prop. 4.22).
   Si U est un ouvert de Zariski de X les assertions suivantes sont équivalentes ([49],
Lemme 4.24)
  (i) U est Zariski-dense ;
  (ii) U est dense pour la topologie usuelle de X ;
  (iii) U rencontre toutes les composantes irréductibles de X.
Et si elles sont satisfaites, U ∩ V est dense dans V pour tout domaine analytique V de
X ([52], Cor. 1.5.13).
   Soit L une extension complète de k. Soit (Xi ) la famille des composantes irréductibles
de X. Pour tout i l’image réciproque Xi,L de Xi sur XL a une famille finie (Yij )j de
composantes irréductibles. Chacune des Yij a même dimension que Xi et se surjecte sur
Xi ; de plus (Yij )i,j est la famille des composantes irréductibles de XL ([49], Lemme 4.25
et théorème 7.1.16 (i), (ii) et (iii)).
   Mentionnons qu’on dispose d’un principe GAGA pour les composantes irréductibles :
si X est un schéma localement de type fini sur une algèbre affinoïde A, et si les Xi sont
les composantes irréductibles de X , les Xian sont les composantes irréductibles de X an
([52], Prop. 2.7.16). Si X est irréductible et si Y est un fermé irréductible de X on a
alors

                          dim X an = dim Y an + codim(Y , X )

([52], Lemma 2.7.10 ; la preuve est un peu plus simple lorsque X = Spec A, voir [48],
Prop. 1.11).


Lemme 11.2.6. — Soit X un espace k-analytique et soit x ∈ X. Les assertions sui-
vantes sont équivalentes :
                                    XZar
  (i) l’adhérence de Zariski {x}      est une composante irréductible de X ;
                           XZar
  (ii) la dimension de {x}      est égale à dimx X.
                             XZar
Si elles sont satisfaites, {x}      est l’unique composante irréductible de X contenant x.


Démonstration. — Choisissons une composante irréductible Z de X contenant x et de
                                                 XZar
dimension dimx X. Le fermé de Zariski {x}             est alors contenu dans la composante
irréductible Z, et les assertions (i) et (ii) sont donc toutes deux équivalentes à l’égalité
    XZar
{x}      = Z. Si elles sont satisfaites et si T est une composante irréductible de X
                                                                         XZar
distincte de Z alors T ∩ Z est un fermé de Zariski strict de Z = {x}          , si bien que T
ne peut contenir x.
                                                                             309
 § 11.3. PROPRIÉTÉS LOCALES DES ESPACES ANALYTIQUES ET DES FAISCEAUX COHÉRENTS

  § 11.3. PROPRIÉTÉS LOCALES DES ESPACES ANALYTIQUES ET
                    DES FAISCEAUX COHÉRENTS

11.3.1. — Soit P une des propriétés suivantes des anneaux locaux noethériens : vérifier
la condition Rm , être régulier, être Gorenstein, être intersection complète. Soit Q une
des propriétés suivantes d’un module de type fini sur un anneau local noethérien : être
libre de rang r, vérifier la condition Sn , être de Cohen-Macaulay
   Soit X un espace k-analytique et soit x un point de X. Soit F un faisceau cohérent
sur X. Pour tout bon domaine analytique V de X contenant x, nous noterons FV,x la
fibre en x de F |V vu comme faisceau sur le site topologique de V , c’est-à-dire encore
la colimite des F (U ) où U parcourt l’ensemble des voisinage ouverts de x dans V . S’il
existe un bon domaine analytique V de X contenant x tel que l’anneau local noethérien
OV,x (resp. tel que le OV,x -module de type fini FV,x ) satisfasse P (resp. Q) ceci reste vrai
pour tout bon domaine analytique de X qui contient x (théorème 3.4 de [49]). On dit
alors que X (resp. F ) satisfait la propriété P (resp. Q) en x.
   Le lieu des point en lesquels la propriété X (resp. F ) satisfait P (resp. Q) est un
ouvert de Zariski de X ([49], théorème 4.4).
   On dit que X (resp. F ) satisfait la propriété P (resp. Q) s’il la satisfait en chacun de
ses points. Si U est un domaine analytique de X contenant x alors X (resp. F ) satisfait
P (resp. Q) en x si et seulement si c’est le cas de U (resp. F |U ).
   Mentionnons une entorse à ces principes généraux : si F est libre de rang r en tout
point de X nous ne dirons évidemment pas que F est libre de rang r, mais qu’il est
localement libre de rang r – et d’après un résultat de Berkovich ([9], 1.3.4) déjà rappelé et
discuté en 11.1.8, cela équivaut à dire que F est localement libre en tant que OX -module
sur le site annelé XG .
   Lorsque F = OX nous dirons souvent « X satisfait Q en x » plutôt que « OX satisfait
Q en x ».
   Nous étendrons les conventions ci-dessus à la conjonction de différentes propriétés d’al-
gèbre commutative ; nous parlerons ainsi d’espace réduit (c’est-à-dire satisfaisant (R0 )
et (S1 )) ou normal (c’est-à-dire satisfaisant (R1 ) et (S2 )) en un point x, ou globalement.
Tout espace X possède un normalisé X,    e muni d’un morphisme fini surjectif X    e → X qui
induit une bijection entre π0 (X)
                                e et l’ensemble des composantes irréductibles de X ([49],
Déf. 5.10, Thm. 5.13, Thm. 5.17) ; la normalisation commute à l’analytification ([52],
Lemma 2.7.15).
   Soit L une extension complète de k et soit π le morphisme structural de XL vers X.
Le faisceau cohérent F satisfait Q en x si et seulement si π ∗ F satisfait Q en y ; si si
P est la propriété d’être Gorenstein ou d’intersection complète, X satisfait P en x si et
seulement si XL la satisfait en y ; si P est la propriété d’être régulier ou de vérifier (Rn )
alors X satisfait P en x dès que XL satisfait P en y, et la réciproque est vraie si L est
analytiquement séparable sur k ([52], Prop. 2.6.7), mais elle ne l’est pas en général.
   Si P est la propriété d’être régulier ou de vérifier (Rm ), ou une propriété impliquant
d’une façon ou d’une autre la régularité (comme le fait d’être réduit, ou normal), on
est dès lors conduit à introduire la notion de validité géométrique de P : on dit que X
satisfait la propriété P géométriquement en x si pour toute extension complète L de k
et tout antécédent y de x sur XL , l’espace XL satisfait P en y. Pour que ce soit le cas, il
suffit qu’il existe une extension parfaite L de k et un antécédent y de x sur XL tel que
XL satisfasse P en y ([52], 2.6.9).
310                 CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

   Soit X un schéma localement de type fini sur une algèbre affinoïde A et soit G un
faisceau cohérent sur X . Soit x un point de X an d’image ξ sur X . Le schéma X (resp.
le faisceau G ) satisfait P (resp. Q) en ξ si et seulement si X an (resp. G an ) la satisfait en
x ([52], Lemma 2.4.6). En étendant les scalaires au complété d’une clôture algébrique
de k, on obtient un principe GAGA analogue pour les propriétés géométriques.



                   § 11.4. PROPRIÉTÉS DES MORPHISMES

11.4.1. Bord et intérieur. — Soit f : Y → X un morphisme d’espaces k-analytiques.
On note Int(Y /X) l’intérieur relatif de f et ∂(Y /X) son complémentaire, le bord relatif
de f ([9], Definition 1.5.4). Par construction, Int(Y /X) est un ouvert de Y . Si ∂(Y /X) =
0, nous dirons que f est sans bord (la terminologie de [9] est closed ). Lorsque f est
l’inclusion d’un domaine analytique, Int(Y /X) coïncide avec l’intérieur Y̊ de Y dans X
au sens de la topologie générale et ∂(Y /X) coïncide donc avec le bord topologique de Y
dans X ([9], Prop. 1.5.4).
   Si X est un schéma localement de type fini sur une algèbre affinoïde A, le morphisme
structural de X an vers M (A) est sans bord.
   Si g : Z → Y et f : Y → X sont deux morphismes d’espaces k-analytiques alors ([9],
Prop. 1.5.5)
(11.4.1.1)                  Int(Z/Y ) ∩ g −1 (Y /X) ⊆ Int(Z/X),
et l’on a
(11.4.1.2)                  Int(Z/Y ) ∩ g −1 (Y /X) = Int(Z/X),
si f est localement séparé ([127], Corollary 5.7), ce qui est notamment le cas dès que Y
est séparé.
   Lorsque X = M (k), on note Int(Y ) = Int(Y /k) et ∂(Y ) = ∂(Y /k), qu’on appelle
l’intérieur et le bord de Y respectivement. Nous dirons que Y est sans bord si ∂(Y ) = ∅.
Si Y est sans bord, ou plus généralement si f : Y → X est sans bord et si X est bon,
l’espace Y est bon. Si f : Y → X est un morphisme d’espaces k-analytiques et que X
est séparé, le cas 11.4.1.2 entraîne les égalités
(11.4.1.3)    Int(Y /X) ∩ f −1 (Int(X)) = Int(Y ) et ∂(Y ) = ∂(Y /X) ∪ f −1 (∂(X)).
   Si Y → X est un morphisme d’espaces k-analytiques et si si X ′ est un espace analy-
tique sur une extension complète de k muni d’un k-morphisme vers X, on a l’inclusion
Int(Y /X) ×X X ′ ⊂ Int(Y ×X X ′ /X ′ ) (cela découle de la proposition 3.13 de [8]). La
classes des morphismes sans bord est en particulier stable par changement de base ana-
lytique sur k. Elle est stable par composition d’après 11.4.1.2 et est G-locale au but
([127], Cor. 5.6).

Exemple 11.4.2. — 1) Soit r un nombre réel s > 0. Soit D le domaine affinoïde de
Ak1,an défini par l’inégalité |T | ⩽ r ; c’est le disque fermé de rayon r au sens de Berkovich,
isomorphe à M (k{T /r}). Son bord topologique dans Ak1,an est le singleton {ηr } (défini
à l’exemple 11.1.12). On a donc aussi {ηr } = ∂(D/A1,an       k ) = ∂(D), la seconde égalité
                            1,an
provenant du fait que Ak est sans bord.
                                § 11.4. PROPRIÉTÉS DES MORPHISMES                                      311

   Si E désigne le domaine analytique fermé (mais non compact) de Ak1,an défini par
l’inégalité |T | ⩾ r, le bord topologique de E dans Ak1,an est encore {ηr }, si bien que
{ηr } = ∂(E/A1,ank ) = ∂(E).
   2) Soit X un espace k-analytique, soit f ∈ O(X) et soit W le domaine analytique de X
défini par l’inégalité |f | ⩽ r. La fonction f induit un morphisme de X vers Ak1,an , encore
noté f ; avec cette convention, on a W = f −1 (D). Comme A1,an est sans bord, ∂(W ) =
∂(W/A1,an ). La formule (11.4.1.3) appliquée au diagramme W → D → A1,an , couplée
au fait que ∂(D/A1,an k ) = {ηr }, assure que ∂(W ) = f
                                                          −1
                                                             (ηr ) ∪ (∂(W/D)). Et la même
formule appliquée à W → X → M (k) entraîne que ∂(W ) = ∂(W/X) ∪ (∂(X) ∩ W ).
Cela démontre que ∂(W ) contient (∂(X) ∩ W ) ∪ f −1 (ηr ). Par ailleurs, la propriété pour
un morphisme d’être sans bord étant stable par changement de base, le morphisme
W f −1 (ηr ) → X est sans bord ; autrement dit, ∂(W/X) ⊂ f −1 (ηr ). On en déduit
(11.4.2.1)                        ∂(W ) = (∂(X) ∩ W ) ∪ f −1 (ηr ).
Si W ′ est le domaine analytique de X défini par l’inégalité |f | ⩾ r, on démontre de
même que
(11.4.2.2)                       ∂(W ′ ) = (∂(X) ∩ W ′ ) ∪ f −1 (ηr ).

11.4.3. — Soit f : Y → X un morphisme d’espaces k-analytiques. On dit que f est
compact si l’image réciproque de toute partie compacte est compacte. Comme tout point
possède un voisinage compact, cela revient à dire que f est topologiquement propre et
topologiquement séparé.
  Suivant [9] (1.5.3), un morphisme est dit propre s’il est compact et sans bord.
```

## CLD-curve, newline lines 15605--15677

```text
f en y, ou encore dimension relative de Y sur X en y, et l’on note dimy f , la dimension
de l’espace H (x)-analytique f −1 (x) en y. Nous dirons que f est quasi-fini en y (resp.
que f est quasi-fini) si dimy f = 0 (resp. si f est partout de dimension relative nulle).
   L’application y 7→ dimy f est semi-continue supérieurement pour la topologie de Za-
riski ([48], Théorème 4.9).
   Le morphisme f est fini en un point y de Y si et seulement si f est quasi-fini en y et
y ∈ Int(Y /X) ([9], Cor. 3.1.10).
11.4.6. Morphismes plats. — Soit f : Y → X un morphisme d’espaces k-
analytiques. Soit y un point de Y et soit x son image sur X.
   Supposons tout d’abord que X et Y sont bons. On dit que f est plat en y, ou que
Y est plat sur X en y, si pour tout morphisme X ′ → X dont la source X ′ est un bon
espace analytique sur k, et tout point y ′ de Y ×X X ′ situé au-dessus de y et dont on
note x′ l’image sur X ′ , le OX ′ ,x′ -module OY ×X X ′ ,y′ est plat.
   Ne supposons plus que X et Y sont bons. On dit alors que f est plat en y s’il existe
un bon domaine analytique U de X contenant x et un bon domaine analytique V de
f −1 (U ) contenant y tels que f |V : V → U soit plat en y ; et c’est alors le cas pour tout
tel couple (U, V ) ([52], 4.1.7).
   Soit maintenant U un domaine analytique quelconque (non nécessairement bon) de
X contenant x, et soit V un domaine analytique quelconque de f −1 (U ) contenant y. Il
résulte aussitôt de la définition que f est plat en y si et seulement si f |V : V → U est
plat en y.
   On dit que f est plat s’il est plat en tout point de Y . La platitude est préservée par
composition et changement de base (la définition est conçue pour garantir cette dernière
propriété).
   Le morphisme structural d’un espace k-analytique vers M (k) est plat ([52], Lemma
4.1.13).
   L’ensemble des points de Y en lesquels f est plat est un ouvert de Zariski de Y ([52],
Thm. 10.3.2).
   Soit φ : Y → X un morphisme entre schémas de type fini sur une algèbre affinoïde et
soit y un point de Y an d’image η sur Y . Le morphisme φan est plat en y si et seulement
si φ est plat en η ([52], Lemma 4.2.1 et Prop. 4.2.4).


Remarque 11.4.7. — Supposons que X et Y sont bons. Si f est plat en y, l’anneau
local OY,y est plat sur OX,x . La réciproque est fausse en général, le problème étant que
la platitude de OY,y est plat sur OX,x n’est pas en général préservée par changement
                            § 11.4. PROPRIÉTÉS DES MORPHISMES                              313

de base bon (un contre-exemple dû à Temkin est étudié en détail au paragraphe 4.4 de
[52]).
   La platitude de OY,y sur OX,x entraîne toutefois la platitude de f en y lorsque y est
un point rigide (cf. [52], 4.2.3) ou plus généralement lorsque y appartient à Int(Y /X)
([52], Thm. 8.3.4).

11.4.8. Morphismes quasi-lisses. — Soit f : Y → X un morphisme entre espaces k-
analytiques. On définit comme en géométrie algébrique le OY -module des différentielles
de Kähler relatives ΩY /X ([8], §3.3) ; c’est un faisceau cohérent sur Y . On dispose en
particulier sur tout espace k-analytique X du faisceau cohérent ΩX/k . Si x est un point
de X, la tige ΩX/k ⊗ H (x) est de dimension ⩾ dimx X ([49], Lemma 6.2 (i)) et l’on dit
que X est quasi-lisse en x si cette dimension vaut exactement dimx X. L’espace X est
quasi-lisse en x si et seulement s’il est géométriquement régulier en x ([49], Prop. 6.3) et
si x est un k-point, il suffit pour que ce soit le cas que X soit régulier en x ([49], Lemma
6.2 (iii) ; l’hypothèse que |k × | ̸= {1} figurant dans son énoncé est inutile, et n’est pas
utilisée dans la preuve).
   Cette notion admet une variante relative : dans [52] (déf. 5.2.4) on définit la notion
de morphisme quasi-lisse en un point au moyen d’un critère jacobien (et un morphisme
est dit quasi-lisse s’il l’est en tout point de sa source). On démontre ([52], Thm. 5.3.4)
que f : Y → X est quasi-lisse en y si et seulement si f est plat en y et la fibre f −1 (f (y))
est quasi-lisse en y. Si d est un entier le lieu Ud des points de Y en lesquels f est quasi-
lisse et de dimension relative d est un ouvert de Zariski de Y ([52], Thm. 10.7.2 (2)) et
ΩUd /X est G-localement libre de rang d ([52], Cor. 5.3.2 ; la preuve dans le cas absolu où
X = M (k) est beaucoup plus simple, cf. [49], Prop. 6.6).
   On dit que f est quasi-étale en y s’il est quasi-lisse et quasi-fini en y, et que f est
quasi-étale s’il est quasi-étale en tout point de Y .

Remarque 11.4.9. — Berkovich a introduit au paragraphe 3 de [10] une notion de
morphisme quasi-étale ; même si sa définition diffère en apparence de celle que nous
donnons ici, les deux sont en fait équivalentes ([52], Lemma 5.4.11).
   Berkovich a par ailleurs défini aux paragraphes 3.3 et 3.5 de [9] des notions de mor-
phisme étale et lisse. Si Y et X sont bons, le morphisme f est lisse en y si et seulement
s’il est quasi-lisse et intérieur en y ([52], Cor. 5.4.8). Il est vraisemblable que l’hypothèse
de bonté est nécessaire pour que cette équivalence soit valable ; on peut toutefois s’en
passer en dimension relative nulle : même si l’on ne suppose plus X et Y bons, f est
```

## CLD-curve, newline lines 19240--19275

```text
                        dcx (f ) = δOXG ,x ((OXG ,x )red ) = 1/ℓ(OXG ,x ).
Autrement dit, le degré calibré de f en x est l’inverse de la multiplicité générique de X
le long de l’unique composante irréductible de X qui contient x.
Proposition 13.3.7. — Soit f : Y → X un morphisme fini d’espaces k-analytiques et
soit Z une composante irréductible de X. Soit λ la longueur générique de f∗ OY le long
de Z, et soit µ la multiplicité générique de X le long de Z. Pour tout x ∈ Z gen , on a
dcx (f ) = λ/µ.
  En particulier, si f est l’immersion canonique de Xred dans X, on a dcx (f ) = 1/µ.
Démonstration. — Soit x ∈ Z gen ⊂ X gen et soit y1 , . . . , yr les antécédents de x sur Y .
Soit V un bon domaine analytique de X contenant x ; posons W = f −1 (V ). On a alors
                                  X
                       dcx (f ) =   dcyi (f )
                                        i
                                             1   X
                                   =               ℓOXG ,x (OYG ,yi )
                                     ℓ(OXG ,x ) i
                                     1X
                                   =      ℓOXG ,x (OYG ,yi )
                                     µ i
                                     1         Y
                                   = ℓOXG ,x ( OYG ,yi )
                                     µ          i
                                       λ
                                   =     ,
                                       µ
où la dernière égalité résulte du corollaire 13.1.10 et du fait que f est fini, d’où la
proposition.

Lemme 13.3.8. — Soit f : Y → X un morphisme entre espaces k-analytiques. Soit y
un point de Y et soit x son image sur X. Supposons que x ∈ X gen et que f est quasi-fini
et plat en y. On a alors l’égalité dcy (f ) = degy (f ).
Démonstration. — Pour établir le lemme, on peut remplacer X par n’importe quel do-
maine analytique V de X contenant x et Y par n’importe quel domaine analytique W
de f −1 (V ) contenant y. Cela permet, au vu du corollaire 13.1.8, de supposer que X et
Y ont affinoïdes et que f est fini. Comme f est plat en y, l’anneau local OY,y est un
OX,x -module libre de rang degy (f ). En vertu de la proposition 13.1.9, c), OYG ,y est un
```

## CLD-curve, newline lines 19660--19720

```text
n’est pas diviseur de zéro dans OX (Vi ). Puisque les Vi recouvrent X, il vient a = 0, ce
qui est absurde, son annulateur étant égal à p.
   Si h est un élément régulier de A qui appartient à I, la fonction méromorphe hf
est une section globale de OX (X), donc appartient à A. Par conséquent, f = (hf )/h
appartient à Frac(A).

Corollaire 13.6.6. — Soit X un bon espace k-analytique et soit f une fonction mé-
romorphe sur X. Pour tout x ∈ X il existe un voisinage ouvert U de x, une fonc-
tion g ∈ OX (U ) et une fonction h ∈ SX (U ) telles que f |U = g/h.
13.6.7. — Soit X un espace analytique et soit f ∈ MX (X) une fonction méromorphe
sur X. On dit que f est une fonction méromorphe régulière (cf. [72], 20.1.8) si pour
tout domaine affinoïde V de X, la restriction de f à V est un élément régulier de
l’anneau MX (V ). Alors, f est un élément inversible de l’anneau MX (X). De plus, il
existe un ouvert de Zariski U de X, dont le complémentaire est rare, tel que f définisse
une fonction holomorphe inversible sur U .
   Observons que le faisceau MX× des fonctions méromorphes régulières est le faisceau
en groupes abéliens associé au faisceau des fonctions holomorphes régulières sur X.



 § 13.7. DIVISEUR D’UNE FONCTION MÉROMORPHE RÉGULIÈRE

13.7.1. — Soit X un espace k-analytique. Soit f ∈ SX (X) une fonction analytique
régulière sur X. Le sous-espace analytique fermé de X d’équation f = 0 est purement
de codimension 1, il est vide si et seulement si f est inversible. Notons div(f ) le cycle
sur X associé ; ce cycle est effectif et nul si et seulement si f est inversible.
  Pour tout sous-espace analytique fermé intègre Y de X, notons mY (f ) le coefficient
de Y dans div(f ).
Lemme 13.7.2. — Soit f une fonction analytique régulière sur X. Soit Y un sous-
espace analytique fermé intègre de X. Soit V un bon domaine analytique de X et soit
y ∈ V ∩ Y tel que l’anneau local OV ∩Y,y soit artinien. On a mY (f ) = long(OV,y /(f )).
Démonstration. — Si f (y) ̸= 0, alors Y n’est pas une composante irréductible de {f =
0}. Dans ce cas, mY (f ) = 0 ; de plus, f est inversible dans OV,y donc long(OV,y /(f )) = 0.
                   § 13.8. EXTENSIONS D’ABHYANKAR ET LEUR DÉFAUT                      389

   Supposons maintenant f (y) = 0. Comme {y} est Zariski dense dans Y (voir les com-
mentaires après la définition 13.1.3), on a Y ⊂ {f = 0}. Puisque Y est purement de
codimension 1, c’est une composante irréductible de {f = 0}. Par définition, mY (f ) est
la longueur générique du faisceau cohérent OX /(f ) le long de Y . D’après la proposi-
tion 13.2.4, c’est la longueur de l’anneau OV,y /(f ).

Lemme 13.7.3. — Si f et g sont deux fonctions holomorphes régulières sur X,
alors div(f g) = div(f ) + div(g).
Démonstration. — Soit Y un sous-espace analytique fermé intègre de X, de codimen-
sion 1 ; démontrons que mY (f g) = mY (f ) + my (g). Soit V un domaine affinoïde de X
et soit y ∈ V ∩ Y tel que OV ∩Y,y soit artinien (il en existe). Notons A = OV,y ; la suite
exacte
                         0 → gA /(f g) → A (f g) → A /(g) → 0
peut se récrire
                           0 → A /(f ) → A /f g → A /(g) → 0
puisque g n’est pas diviseur de zéro dans A . on a donc l’égalité long(OV,y /(f g)) =
long(OV,y /(f )) + long(OV,y /(g)), d’où l’assertion d’après le lemme 13.7.2.

Proposition 13.7.4. — a) La formule f 7→ div(f ) définit un morphisme de G-
faisceaux en monoïdes abéliens du G-faisceau des fonctions analytiques régulières sur X
dans le G-faisceau des cycles effectifs sur X.
   b) Ce morphisme de faisceaux se prolonge de manière unique en un morphisme de G-
faisceaux en groupes abéliens du G-faisceau des fonctions méromorphes régulières sur X
dans le G-faisceau des cycles sur X.
Démonstration. — (1) Soit V et W des domaines analytiques de X tels que W ⊂ V .
Pour toute fonction analytique régulière f sur V , f |W est une fonction analytique ré-
```

## CLD-curve, newline lines 21280--21445

```text

                § 14.7. VARIATION DES TROPICALISATIONS

Lemme 14.7.1. — Soit X un espace analytique compact, soit f : X → Y un mor-
phisme d’espaces analytiques, soit g : X → Gnm un moment. Pour tout y ∈ Y , on pose
Xy = f −1 (y). Soit y un point rigide de Y . Il existe un voisinage U de y dans Y et un
polyèdre ∆ ⊂ gtrop (Xy ) de dimension ⩽ dim(Xy ) − 1 tels que gtrop (Xu ) ⊂ gtrop (Xy ) et
gtrop (Xu ∩ ∂(X)) ⊂ ∆ pour tout u ∈ U .
                                               −1
Démonstration. — Le domaine analytique gtrop      (gtrop (Xy )) de X contient le fermé de
Zariski Xy , donc en est un voisinage (lemme 11.4.10). Comme X est compact, il existe
                                           −1
un voisinage U de y tel que f −1 (U ) ⊂ gtrop (gtrop (Xy )). Ainsi, si u ∈ U , gtrop (Xu ) est
contenu dans gtrop (Xy ).
   Le bord ∂(X) de X est contenu dans une réunion finie de compacts qui sont chacun de
la forme φ−1 (ηr ), où φ est un morphisme d’un domaine affinoïde V de X vers A1 et r est
un nombre réel > 0 ([50], lemme 3.1). Soit φ : V → A1 un tel morphisme et soit r > 0.
418          CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

                                            −1
Posons Q = gtrop (Xy ∩ φ−1 (ηr )) et W = gtrop  (Q) ∩ φ−1 (ηr ). L’espace W est un domaine
analytique compact de V ∩ φ−1 (ηr ) et en contient le fermé de Zariski Xy ∩ φ−1 (ηr ). Par
suite, W est un voisinage de Xy ∩ φ−1 (ηr ) dans X ∩ φ−1 (ηr ). Puisque X est compact, et
quitte à diminuer U , on a gtrop (Xu ∩ φ−1 (ηr )) ⊂ Q pour u ∈ U .
  Par ailleurs, démontrons que dim(Q) ⩽ dim(Xy ) − 1. Soit x ∈ Xy ∩ φ−1 (ηr ) ;
on a dk (x) ⩽ dim(Xy ) ; d’autre part, dk (x) = dH (ηr ) (x) + 1 ; par conséquent,
dH (ηr ) (x) ⩽ dim(Xy ) − 1. Ainsi, la dimension H (ηr )-analytique de Xy ∩ φ−1 (ηr )
est majorée par dim(Xy ) − 1 et, a fortiori, dim(Q) ⩽ dim(Xy ) − 1.
  Le lemme en résulte.

Théorème 14.7.2. — Soit d un entier, soit X un espace analytique compact purement
de dimension n qui satisfait à la condition (Sd ), soit Y un espace analytique régulier
purement de dimension d et soit f : X → Y un morphisme purement de dimension
relative n − d ; pour tout t ∈ Y , on pose Xt = f −1 (t).
   Soit g : X → GN   m un moment. Soit y un point rigide de Y et soit P le polyèdre calibré
           (n−d)
gtrop (Xy )      .
   a) Il existe un voisinage ouvert U de y dans Y tel que, pour tout point u ∈ U , le
polyèdre calibré gtrop (Xu )(n−d) soit égal à P .
   b) On suppose de plus que Y = Ad et que y est l’origine. Posons X ′ = f −1 (Gdm ) et
soit h : X ′ → GN        d
                   m × Gm le moment défini par (g, f ) ; c’est un moment agréable. Il existe
un nombre réel r > 0 tel que le polyèdre calibré htrop (X ′ ) ∩ RN × ]−∞, log(r)[d soit égal
au produit des polyèdre calibrés P et de la cellule ]−∞, log(r)[d munie de son calibrage
standard.
   Dans une première version de ce texte, l’énoncé de ce théorème supposait d = 1.
Comme l’a noté A. Mihatsch dans [103], la démonstration s’étend à tout d.
Démonstration. — D’après le lemme 14.7.1, il existe un voisinage ouvert U de y dans Y
et un polyèdre ∆ de dimension ⩽ n − d − 1 tels que gtrop (Xu ) ⊂ gtrop (Xy ) et gtrop (Xu ∩
∂(X)) ⊂ ∆ pour tout u ∈ U . Quitte à le remplacer par la composante connexe de y
dans U , on suppose que U est connexe.
   Choisissons une décomposition cellulaire C de gtrop (Xy ) telle que ∆ soit contenu dans
la réunion des (n − d − 1)-cellules de C .
Lemme 14.7.3. — Soit C une (n−d)-cellule de C . Soit p : GN       m → Gm
                                                                           n−d
                                                                                un morphisme
affine de tores tel que la restriction à C de ptrop soit injective ; soit σC : Rn−d → RN
                                                                             −1
l’unique section affine de p dont l’image contient C. Posons W = gtrop          (C) ; c’est un
domaine de Weierstrass de X, purement de dimension n.
                                                                                     n−d
   a) Il existe un entier naturel δC ̸= 0 tel que le morphisme (p◦g, f )|W : W → Gm      ×Gdm
soit fini et plat de degré δC au-dessus de tout point de sqU (ptrop (C̊)).
   b) Pour tout u ∈ U , on a C ⊂ gtrop (Xu ).
  (Rappelons, voir §12.1.12, que l’ensemble sqU (ptrop (C̊)) est constitué des points de X
de la forme squ (c), pour u ∈ U et c ∈ ptrop (D̊).)
                                                                       n−d
Démonstration. — a) Soit u ∈ U et soit Su le squelette de (Gm              )u , identifié à une
partie de Gn−d
             m    ×  Y . Soit s un  point de  l’image  canonique  sq u trop (C̊)) de ptrop (C̊)
                                                                      (p
dans Su . Prouvons que (p ◦ g, f )|Y est fini et plat au-dessus de s.
  Soit x un point de W tel que (p◦g, f )(x) = s. Le lemme 11.5.1, appliqué au morphisme
de Wu dans Gn−dm,u induit par p◦g, affirme que la dimension de ce morphisme en x est nulle.
                          § 14.7. VARIATION DES TROPICALISATIONS                             419

                                                                      −1
Cela entraîne que dimx (p ◦ g, f ) = 0. Puisque ∂(W ) ⊂ ∂(X) ∪ gtrop     (∂C), on a x ̸∈ ∂(W ).
Puisque fW est propre, le lemme 11.6.6, a), entraîne que f |W est fini au-dessus d’un
voisinage de s.
                                                                            n−d
   Comme dH (t) (s) = n − d, on a dk (s) ⩾ n − d. Les espaces W et Gm           × Y sont tous
                                                             n−d
deux purement de dimension n, l’espace k-analytique Gm × Y est régulier. Comme X
vérifie la propriété (Sd ), le lemme 11.5.8 appliqué au morphisme (p ◦ g, f )|W entraîne que
ce morphisme est plat au-dessus de s.
   Comme U est connexe, l’ensemble sqU (ptrop (C̊)) = {squ (ptrop (C̊))}u∈U est connexe,
d’après 12.1.12. Par suite, le degré de (p ◦ g, f )|W au-dessus de s ne dépend pas du
point s choisi. Notons-le δC .
   Par hypothèse, C ⊂ gtrop (Xy ), donc ptrop (C) ⊂ p ◦ gtrop (Wy ) ; d’après le théo-
                                             (n−d)
rème 12.8.2, on a ptrop (C) ⊂ p ◦ gtrop (Σ(p◦g)y ) donc tout point de sqy (ptrop (C̊)) possède
un antécédent par p ◦ g. Cela entraîne que δC ̸= 0 et termine la démonstration de
l’assertion a).
   b) Soit s un point de sqU (ptrop (C̊)) et soit u son image sur U . Par changement de base,
le morphisme de Wu dans (Gn−d     m )u déduit de p ◦ g est fini et plat de degré δC au-dessus
de s.
   Comme δC ̸= 0, il s’ensuit que ptrop (C̊) ⊂ p ◦ gtrop (Wu ) pour tout u ∈ U . Par densité
de C̊ dans C et compacité de Wu , on a ptrop (C) ⊂ p ◦ gtrop (Wu ) pour tout u ∈ U . Par
définition de W , ceci entraîne que C ⊂ gtrop (Wu ) pour tout u ∈ U .
  Reprenons la démonstration du théorème 14.7.2.
  a) Démontrons d’abord la constance des polyèdres calibrés gtrop (Xu )(n−d) pour u ∈ U .
  Soit u ∈ U .
  D’après le lemme précédent, toute (n − d)-cellule de gtrop (Xy ) est contenue
dans gtrop (Xu ). Par suite, gtrop (Xy )(n−d) ⊂ gtrop (Xu ). Par définition de U , on a
également gtrop (Xu ) ⊂ gtrop (Xy ). Il en résulte que gtrop (X, u)(n−d) = gtrop (Xy )(n−d) .
  De plus, le calibrage canonique de gtrop (Xu ) est adapté à la décomposition cellulaire C ,
car aucune (n − d)-cellule ouverte de C ne rencontre gtrop (Xu ∩ ∂(X)).
  Soit C une (n − d) cellule de C , soit p : GN  m → Gm
                                                         n−d
                                                              un morphisme affine de tores tel
                                                              n−d
que la restriction à C de ptrop soit injective et soit σC : R     → RN l’unique section affine
de p dont l’image contient C. Par définition des calibrages canoniques, le vecteur-volume
µC,u de gtrop (Xu ) sur C est donné par
                               µC,u = δC σC,∗ (|e1 ∧ · · · ∧ en−d |).
Ainsi, le polyèdre calibré gtrop (Xu )(n−d) est égal à gtrop (Xy )(n−d) = P , ainsi qu’il fallait
démontrer.
  b) Nous supposons maintenant que Y = Ad et que y = 0 est l’origine.
  Le morphisme f : X → Y est topologiquement propre, donc le morphisme f |X ′ : X ′ →
Gm est topologiquement propre. Par suite, le moment h′ = (g|X ′ , f |X ′ ) est topologique-
  d

ment propre, et en particulier agréable.
  On choisit un nombre réel r > 0 assez petit tel que l’on puisse prendre U = D(0, r)
dans a).
                                                                               −1
  Posons Γ = ]−∞; log(r)[d et notons XΓ = X ′ ∩ f −1 (D(0, r)) = X ′ ∩ ftrop      (Γ).
                           ′
  Prouvons d’abord que htrop (XΓ ) = P × Γ.
  Soit γ ∈ Γ et soit u ∈ D(0, r) tel que trop(u) = γ. Soit C une cellule de dimension (n−
d) de C . La cellule C × {γ} est contenue dans gtrop (Xu ), d’après a). Par suite, la cellule
420           CHAPITRE 14. CALIBRAGE CANONIQUE D’UN ESPACE ANALYTIQUE

C × Γ est contenue dans h′trop (XΓ ). Comme elle est de dimension n, elle est contenue
dans h′trop (XΓ )(n) . Inversement, la définition de U au début de la démonstration garantit
que pour tout u ∈ D(0, r)∩Gdm , gtrop (Xu′ ) ⊂ gtrop (Xy ). Par suite, h′trop (XΓ ) ⊂ gtrop (Xy )×
Γ. On a donc h′trop (XΓ )(n) ⊂ gtrop (Xy )(n−d) × Γ. On a donc l’égalité voulue.
  Démontrons maintenant l’égalité des calibrages. Soit C une (n−d)-cellule de C . notons
                   d        n
aussi q : GN m ×Gm → Gm le morphisme de tores (p, id). L’application affine τC = (σC , id)
est l’unique section affine de qtrop dont l’image contient C × Γ. Nous allons démontrer
que le calibrage de la cellule C × Γ de h′trop (XΓ )(n) est au produit du calibrage µC de C
dans P par le calibrage standard de Γ.
  Posons XC,Γ = (h′trop )−1 (C × Γ) ; nous allons démontrer que le morphisme q ◦ h′ |XC,Γ
est fini et plat de degré δC au-dessus de tout point de sq(qtrop (C̊ × Γ)).
  Soit c ∈ ptrop (C̊) et γ ∈ Γ Par la construction de la décomposition cellulaire C et le
choix de r, le point sq(c, γ) n’appartient pas à q ◦ h′ (∂(XC,Γ )). D’après le lemme 11.6.6,
c), le morphisme q ◦ h′ |XC,Γ est fini et plat au-dessus de sq(c, γ) ; notons δ son degré.
  On a q ◦ h′ = (p, id) ◦ (g, f )|X ′ = (p ◦ g, f )|X ′ . Par changement de base, le mor-
phisme de XC,Γ,sq(γ) dans Gn−d  m,H (sq(γ)) déduit de p ◦ g est fini et plat de degré δ au-dessus
de sqH sq(γ) (sq(γ)). D’après la première partie de l’énoncé et le choix de r, ce degré est
égal à δC .
  Par conséquent (cf. §14.5.2), le calibrage de la cellule C × Γ est constant, de vecteur-
volume
                              µC×Γ = δC τC,∗ (|e1 ∧ · · · ∧ en−1 ∧ en |).
De plus,
         τC,∗ (|e1 ∧ · · · ∧ en−1 ∧ en )| = σC,∗ (|e1 ∧ · · · ∧ en−d |) · |en−d+1 ∧ · · · ∧ en |,
qui est le produit du vecteur-volume associé à C dans P et du vecteur-volume associé
au calibrage standard de Γ. Ceci achève la démonstration du théorème.

Remarque 14.7.4. — Le théorème 14.7.2 ne peut pas être vrai sans certaines hypo-
thèses sur le morphisme f : X → Y .
   Considérons par exemple le cas où f est la normalisation d’une courbe lisse en dehors
d’un unique point double ordinaire y et g est le moment trivial (N = 0). Dans ce cas,
la tropicalisation de Xy est un point avec multiplicité 2. En revanche, pour tout autre
```

## CLD-curve, newline lines 23340--23453

```text

  Soit X un n-espace k-analytique, considéré comme espace tropical de niveau n.
16.6.1. — Soit Y un sous-espace analytique fermé de X, purement de dimension p. On
le considère comme un espace tropical de niveau p et on note j : Y → X l’immersion
fermée canonique. Le courant j∗ δY sur X est de bidimension (p, p) ; on le note plus
simplement δY .
                                        P
16.6.2. — Soit p un entier et soit z =     z(Y )Y un cycle purement p-dimensionnel
sur X. Soit ω ∈ Ac (X) ; posons
                  p,p

                                    Z      X        Z
                          ⟨δz , ω⟩ = ω =       z(Y ) ω.
                                         z       Y            Y


C’est une somme finie : en effet, comme ω est à support compact et la famille (z(Y )) est
                                      R de Zariski intègres Y de X tels que z(Y ) ̸= 0 et
localement finie, l’ensemble des fermés
ω|Y ̸= 0 est fini. L’application ω 7→ z ω est un courant : si l’on se restreint aux formes
à support dans un domaine analytique compact donné V , il s’agit de la somme finie des
courants z(Y )δY , où Y parcourt l’ensemble fini des fermés de Zariski intègres Y de X
qui rencontrent V et tels que z(Y ) ̸= 0.
   Lorsqu’on se donne un sous-espace analytique fermé de X, purement de dimension p,
on peut considérer d’une part l’intégration sur ce sous-espace et d’autre part l’intégration
sur le cycle associé. La proposition suivante affirme que ces deux opérations coïncident.

Proposition 16.6.3. — Soit Y un sous-espace analytique fermé de X, purement de
dimension p. On a δY = δ[Y ] .

Démonstration. — Notons j l’immersion   R de     Y dans X. Soit ω une (p, p)-forme à support
                                              ∗
compact sur X. On a donc ⟨δY , ω⟩ = Y j ω, ce qui permet de supposer que Y = X.
  Soit (Xi ) la famille des composantes irréductibles de X et, pour tout i, soit mi la
multiplicité de X le long de Xi . Soit X ′ l’ouvert de Zariski de X constitué des points qui
sont situés sur une unique composante irréductible de X ; il contient le support de ω.
Pour tout i, posons Xi′ = X ′ ∩ Xi ; c’est un ouvert de X et l’on a
                             Z            Z              Z
                                                       1
                                     ω=            ω=        ω,
                              Xi,red          ′
                                            Xi,red    mi Xi′
                                                              ′
en vertu de la proposition 15.4.3 appliquée à l’immersion de Xi,red dans Xi′ , dont le degré
calibré est 1/mi (proposition 13.3.7). Alors, on a
              Z      Z        XZ          X Z               X Z
   ⟨δX , ω⟩ =    ω=      ω=          ω=        mi      ω=       mi        ω = ⟨δ[X] , ω⟩,
              X       X′       i   Xi′       i
                                                      ′
                                                     Xi,red       i   Xi,red


comme il fallait démontrer.

                     z(Y )Y , on définit aussi δz∂ =   z(Y )δY∂ . Si Y est un sous-espace
                   P                                 P
16.6.4. — Si z =
analytique fermé de X, on démontre comme pour la proposition 16.6.3 que δY∂ = δ[Y    ∂
                                                                                       ].
460              CHAPITRE 16. COURANTS SUR LES ESPACES ANALYTIQUES

               § 16.7. LA FORMULE DE POINCARÉ–LELONG

16.7.1. — Soit X un n-espace k-analytique sans bord ; on le considère comme un espace
tropical de niveau n.
   Soit f une fonction méromorphe régulière f sur X. Le courant d’intégration δdiv(f ) sur
le cycle div(f ) est un courant symétrique de bidimension (n − 1, n − 1) sur X, donc de
bidegré (1, 1) ; il est d′ -fermé et d′′ -fermé (proposition 7.7.9).
   La formule de Poincaré–Lelong (théorème 16.7.3) va entraîner qu’il est d′ d′′ -exact.
16.7.2. — Soit f une fonction méromorphe régulière sur X. Soit U le sous-espace
de X formé des points au voisinage desquels f est définie et non nulle ; c’est un ouvert
de Zariski de X sur lequel la fonction log |f | est lisse, et il est Zariski dense. Pour tout
point x du fermé complémentaire, on a dk (x) < dim(X). D’après le paragraphe 7.1.12,
le courant [log|f |] sur U se prolonge un unique courant de bidegré (0, 0) sur X que nous
noterons encore [log|f |].
Théorème 16.7.3 (Formule de Poincaré–Lelong). — Soit X un n-espace k-
analytique sans bord et soit f une fonction méromorphe régulière sur X. On a l’égalité
                                   δdiv(f ) = d′ d′′ [log|f |].
   L’exemple 16.1.4 montre que l’hypothèse de régularité sur f est nécessaire, même si
le complémentaire de son lieu d’inversibilité est de dimension < n.
Lemme 16.7.4. — L’égalité ci-dessus est vraie sur l’ouvert d’inversibilité de f .
Démonstration. — On peut supposer f inversible. On a alors div f = 0 et le terme
de gauche de l’égalité est donc nul. On a par ailleurs d′ d′′ x = 0 dans A 1,1 (R) ; il
vient d′ d′′ log|f | = 0.

Lemme 16.7.5. — Il suffit de démontrer le théorème 16.7.3 si l’on suppose de plus que
X satisfait à la propriété (S1 ) et que f est une fonction holomorphe régulière qui définit
un morphisme purement de dimension relative n − 1 de X vers A1 .
Démonstration. — Le théorème est local sur X ; il suffit donc de prouver que tout point x
de X a un voisinage sur lequel cette égalité de courant est vérifiée. On peut ainsi com-
mencer par supposer que f est quotient de deux fonctions holomorphes régulières. Par
additivité des deux termes de l’égalité à établir, on peut donc supposer que f est ho-
lomorphe. Pour alléger les notations, nous noterons encore f le morphisme X → A1
qu’elle induit.
   Si f (x) ̸= 0, il existe un voisinage U de x sur lequel f est inversible, et l’égalité à
établir vaut sur U en vertu du lemme 16.7.4.
   Supposons que f (x) = 0. Comme la fonction f est régulière, le morphisme f qu’elle
induit est de dimension relative n − 1 en x. Par suite, ce morphisme est de dimension ⩽
n − 1 au voisinage de x ([48], th. 4.9). En vertu du Hauptidealsatz (lemme 11.5.2), le
morphisme f est donc purement de dimension relative n − 1 au voisinage de x.
   Démontrons que l’espace X a la propriété (S1 ) en x. Soit V un domaine affinoïde de X
contenant x. Le germe de f |V en x est un élément de l’idéal maximal de OV,x et est un
élément régulier de cet anneau. En conséquence, l’anneau local OV,x a la propriété (S1 ),
si bien que X a la propriété (S1 ) en x. Il existe dès lors un voisinage ouvert U de x
                          § 16.7. LA FORMULE DE POINCARÉ–LELONG                               461

dans X tel que U satisfasse la propriété (S1 ) et tel que f |U soit purement de dimension
relative n − 1.
   Le lemme précédent permet de supposer à partir de maintenant que X a la pro-
priété (S1 ) et que f est une fonction holomorphe régulière induisant un morphisme
purement de dimension relative n − 1 de X dans A1 .
   Les deux courants δdiv f et d′ d′′ [log|f |] sont symétriques ; pour s’assurer de leur égalité,
il suffit de les appliquer à une forme test symétrique.
   Soit donc ω une forme lisse de type (n − 1, n − 1) sur X, symétrique et à support
```

## GR, newline lines 70--138

```text
Jonsson [BJ22] give a far reaching global pluripotential theory on a projective variety
over a trivially valued field. Some parts work for any non-Archimedean field, at least in
residue characteristic zero. These psh functions might be singular, and the definition uses
decreasing limits of semipositive model functions as in Zhang’s approach. Chambert–Loir
and Ducros [CD25] have posted a second version of their work in which they give a new
definition of psh functions which is functorial and is based on a transfinite regularization
process.
   In all of the above approaches, a maximum principle for plurisubharmonic functions
is missing. In this paper, we propose another class of psh functions called classically
plurisubharmonic functions in close analogy to the complex case. The definition is local,
the functions are upper semicontinuous, and we will show that properties (1)–(4) are
satisfied. It will be clear that classically psh functions form a maximal class of reasonable
plurisubharmonic functions that is compatible with Thuillier’s definition for curves. In
particular, the psh functions from the above are classically psh (see 1.2 below).
   To get regularization by smooth psh functions in the sense of Chambert-Loir and Ducros
or to define a Monge–Ampère measure for psh functions, additional hypotheses as in
[CD25] might be needed, but that is not the subject of this paper.

1.1. Subharmonic functions on arbitrary k-analytic curves. In Section 3, we define
subharmonic functions on any k-analytic curve X to be the elements of the following
subsheaf of the sheaf of upper semicontinuous functions on X with range [−∞, ∞).
It is the smallest subsheaf that is functorial with respect to pullback, stable under base
change, and agrees with Thuillier’s subharmonic functions on smooth k-analytic curves.
We will show in Proposition 3.5 that subharmonic functions satisfy the properties (1)–(3)
as in the complex case, and the local maximum principle on the interior Int(X ) = X \ ∂ X .

1.2. Plurisubharmonic functions on k-analytic spaces. We define classically plurisub-
harmonic functions on k-analytic spaces as the elements of the smallest subsheaf of the
sheaf of upper semicontinuous functions with range [−∞, ∞) that is functorial with
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              3

respect to pullback, stable under base change, and agrees with the above defined sheaf
of subharmonic functions on k-analytic curves. In Section 4, we will show that classically
psh functions satisfy properties (1)–(3).
   We use the terminology classically psh to distinguish from the psh functions introduced
by Chambert-Loir and Ducros in [CD25]. Note that psh functions are classically psh.
Indeed, psh functions are upper semi-continuous and the definition is functorial, so we
are reduced to the case of a smooth analytic curve C. We have to see that a psh function
is subharmonic. By base change, we may assume that k is algebraically closed and non-
trivially valued, see Proposition 3.5(7). Since subharmonic functions are stable under
decreasing limits, and the psh functions are defined by a transfinite regularization process
from smooth psh functions, it is enough to show that a smooth psh function on C is
subharmonic. This follows from a result of Wanner [Wan19, Theorem 4.7].
1.3. Plurisubharmonic R-PL functions. For an R-piecewise linear function h: X → R
on a good strictly k-analytic space over a non-trivially valued field k, we have studied the
notion of semipositivity in the paper [GR25]. This notion is a local analytic version of
the global semipositive metrics introduced by Zhang [Zha95] which are induced by nef
models. We show in Theorem 4.3 that an R-PL function h is semipositive if and only if h
is classically psh.
1.4. Connectivity by curves. In Theorem 5.4, we show that two points x, y of a con-
nected k-analytic space X can be connected by analytic curves (assumed to be compact
and defined over a non-Archimedean field extension of k). If ∂ X = ;, then we even show
that x, y can be connected by overconvergent curves, which means roughly speaking that
we can connect them with the interiors of compact curves. We refer to Section 5 for the
precise definitions. The proof of Theorem 5.4 is inspired by Berkovich’s proof [Ber90,
§3.2] showing that a connected k-analytic space is pathwise connected. However, we
have to choose different paths, as the ones in ibid are not analytic curves. This result is
related to [dJ95, Proposition 6.1.1] and [Ber07, Theorem 4.1.1] (see the discussion after
the statement of Theorem 5.4 for more details).
Theorem 1.5 (Local Maximum Principle). Let X be a k-analytic space, and let u be a
classically psh function on X . If u has a local maximum on x ∈ Int(X ), then u is locally
constant at x.
  This will be shown in Theorem 6.1. For the proof, one may assume that ∂ X = ;;
then we reduce the claim to the local maximum principle for k-analytic curves using
connectivity by overconvergent curves.
1.6. Global maximum principle for affinoids. Berkovich has shown [Ber90, Propo-
sition 2.4.4] that a k-affinoid space X = M (A ) has a Shilov boundary, i.e. there is a
smallest subset Γ of X such that
                                 max | f (x)| = max | f (x)|
```

## GR, newline lines 250--405

```text
finite extension of k.
   If ϕ : Y → X is a morphism, then the fiber ϕ −1 (x) over x ∈ X is an H (x)-analytic
space, and the underlying topological space has the induced topology [Ber93, §1.4].

2.8. Fiber products. The category of k-analytic spaces admits fiber products by [Ber93,
§1.4]. For analytic spaces X , Y over a k-analytic space S, we denote the fiber product by
X ×S Y . Given x ∈ X and y ∈ Y over the same point s ∈ S, there always exists z ∈ X ×S Y
mapping to x and to y with respect to the canonical projections [Duc18, 1.2.13]. For
convenience, we repeat the argument. The completed tensor product H (x)⊗         b H (s) H ( y)
contains H (x) ⊗H (s) H ( y) by a result of Gruson [Gru66, §3.2 Théorème 1(4)], so
H (x)⊗b H (s) H ( y) ̸= 0. The Berkovich spectrum of any nonzero Banach ring is nonempty
                                                                 
[Ber90, Theorem 1.2.1], and any z ′ ∈ M H (x)⊗     b H (s) H ( y) induces a point z ∈ X ×S Y
mapping to x and y. Note that H (z) is a simultaneous analytic extension field of H (x)
and of H ( y).
  Since Gruson’s result holds for Banach algebras over a non-Archimedean field, the
same argument shows that for two analytic field extensions of k, there is a joint analytic
extension of both.

2.9. Extension of scalars. Let k′ /k be an an analytic extension field. Then there is a
base extension functor (·)k′ which associates to a k-analytic space X a k′ -analytic space
X k′ , given on a k-affinoid space X = M (A ) by the k′ -affinoid space X k′ = M (A ⊗b k k′ )
[Ber90, §1.4]. We denote by πk′ /k : X k′ → X the structure map, which is closed and
surjective by [GRW17, Lemma 2.19], [Duc24, (3.1.1.2)].

2.10. The Shilov section. For r = (r1 , . . . , rn ) ∈ R>0     n
                                                                   , we consider the k-affinoid do-
main in the closed polydisc M k〈r1 T1 , . . . , rn Tn 〉 given by the equations |T j (x)| = r j ,
                                          −1            −1

j = 1, . . . , n. The corresponding      k-affinoid algebra is denoted by k r ; it consists of the
Laurent series f = λ∈Zn aλ T λ such that aλ r λ → 0 for |λ| → ∞. The k-affinoid al-
                           P

gebra M (k r ) has a unique Shilov        boundary point equal to the weighted Gauss point
η r ∈ M k〈r1−1 T1 , . . . , rn−1 Tn 〉 given by the weighted Gauss norm ∥ ∥ r from 2.3. If
                                                                                       p
r1 , . . . , rn induce linearly independent elements in the Q-vector space R>0 / |k× |, then k r
is a non-Archimedean field; it follows that k r = H (η r ). For every k-affinoid algebra A ,
there is always such an r such that A ⊗        b k r is a strictly k r -affinoid algebra. See [Ber90,
pp. 21–22].
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                 7

   For any k-analytic space X and r ∈ R>0n
                                             , the structure map πkr /k : X kr → X has a canon-
ical section σ : X → X r mapping x ∈ X to the unique Shilov boundary point of the fiber
π−1
  k r /k
         (x) = M (H (x)⊗b k r ) = M (H (x) r ) (which is the weighted Gauss point η r ). We
call σ the Shilov section. The Shilov section is continuous: see [Ber90, Lemma 3.2.2(i)],
[Duc18, 1.2.16].

2.11. Relative boundary. An important notion in this paper is that of the relative bound-
ary of a morphism ϕ : X → Y of k-analytic spaces. This is a closed subset of X which we
denote by ∂ (X /Y ). We will not give the details of this definition, but let us try to explain
the literature on the subject. In [Ber90, §2.5], Berkovich defines the relative boundary
∂ (X /Y ) for k-affinoid spaces X and Y . Then in [Ber90, §3.1], he generalizes ∂ (X /Y ) for
good k-analytic spaces using that all points of X and Y have k-affinoid neighborhoods.
Berkovich calls ϕ closed if ∂ (X /Y ) = ;. Berkovich defines ∂ (X /Y ) for arbitrary k-analytic
spaces in [Ber93, 1.5.3(ii)], as follows. A morphism ϕ is closed if for every morphism
Y ′ → Y from a good k-analytic space Y ′ , the fiber product X ′ := X ×Y Y ′ is good and the
canonical morphism X ′ → Y ′ is closed in the previous sense. Finally in [Ber93, Defini-
tion 1.5.4], a point x ∈ X is defined to be in Int(X /Y ) if x has an open neighborhood U
such that ϕ induces a closed morphism U → Y in the above sense. We refer to [Tem15,
Definition 4.2.4.1] for a more explicit equivalent definition of ∂ (X /Y ). Note that in this
paper, we will use the notion closed map in the usual topological sense meaning that it
maps closed sets to closed sets. This is different from Berkovich’s terminology.
   The complement Int(X /Y ) := X \ ∂ (X /Y ) is called the relative interior. We will usually
apply this in the case Y = M (k), in which case we call ∂ X := ∂ (X /M (k)) the boundary
of X and Int(X ) := X \ ∂ X the interior. If ∂ X = ;, we say that X boundaryless. A bound-
aryless space is good by definition. Note that Berkovich calls boundaryless k-analytic
spaces closed.
   We list here some properties of the boundary and interior which we will use throughout
the paper:
   (1) A point x ∈ X is contained in Int(X /Y ) if and only if there is an open neighbor-
       hood U of x such that Int(U/Y ) = U: this is part of the above definition.
   (2) If ϕ : X → Y is finite, then Int(X /Y ) = X [Ber93, Example 1.5.3(iii)].
   (3) If X is an analytic domain in Y , then Int(X /Y ) is the topological interior of X in
       Y [Ber93, Proposition 1.5.5(i)].
             ϕ     ψ
   (4) If X → Y → S are morphisms of k-analytic spaces, then

(2.11.1)                   Int(X /Y ) ∩ ϕ −1 Int(Y /S) ⊂ Int(X /S)

        [Ber93, Proposition 1.5.5(ii)], with equality if ψ is locally separated [Tem04,
        Corollary 5.7]. Taking S = M (k), this becomes

(2.11.2)                      Int(X /Y ) ∩ ϕ −1 Int(Y ) ⊂ Int(X ).

   (5) If k′ /k is an analytic extension field, then

                                π−1
                                 k′ /k
                                       Int(X /Y ) ⊂ Int(X k′ /Yk′ )
8                                      W. GUBLER AND J. RABINOFF

         [Ber93, Proposition 1.5.5(iii)]. Taking Y = M (k), this becomes
                                       π−1
                                        k′ /k
                                              Int(X ) ⊂ Int(X k′ ).
For convenience, we restate these properties in terms of the relative boundary:
   (1′ ) A point x ∈ X is contained in ∂ (X /Y ) if and only if ∂ (U/Y ) ̸= ; for every open
         neighborhood U of x.
   (2′ ) If ϕ is finite, then ∂ (X /Y ) = ;.
   (3′ ) If X is an analytic domain in Y , then ∂ (X /Y ) is the topological boundary of X
         in Y .
               ϕ     ψ
     ′
   (4 ) If X → Y → S are morphisms of k-analytic spaces, then
(2.11.3)                        ∂ (X /S) ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ (Y /S)),
         with equality if ψ is locally separated. Taking S = M (k), this becomes
(2.11.4)                             ∂ X ⊂ ∂ (X /Y ) ∪ ϕ −1 (∂ Y ).
    (5′ ) If k′ /k is an analytic extension field, then
                                     ∂ (X k′ /Yk′ ) ⊂ π−1
                                                       k′ /k
                                                             ∂ (X /Y ).
         Taking Y = M (k), this becomes
                                           ∂ X k′ ⊂ π−1
                                                     k′ /k
                                                           ∂ X.
We will need the following lemma, which is a consequence of deep results in [CT21] in
general, although it has an elementary proof for good spaces.
Lemma 2.12. If X is a k-analytic space and k′ /k is an analytic field extension, then
                                          πk′ /k (∂ X k′ ) = ∂ X .
Proof. We have πk′ /k (∂ X k′ ) ⊂ ∂ X by 2.11(5′ ). Let x ∈ ∂ X , and let U ⊂ X be a compact
neighborhood of x. We claim that x ∈ ∂ U. If not, then there is an open neighborhood
V of x in U such that ∂ V = ; by 2.11(1′ ). If V ′ ⊂ V is a smaller open neighborhood of
x in X , then ∂ V ′ = ; as well by 2.11(3′ ) and by (2.11.4) as applied to V ′ → V → M (k).
Thus we may assume that V is open in X , which implies by 2.11(1) that x ∈ Int(X ), a
contradiction. Hence x ∈ ∂ U. If x ′ ∈ π−1      k′ /k
                                                      (x), then x ′ ∈ ∂ Uk′ if and only if x ′ ∈ ∂ X k′
for the same reason. We need to show π−1        k′ /k
                                                      (x) ∩ ∂ X k′ ̸= ;, so we may replace X by U to
assume that X is compact. In this case, the closed subset ∂ X k′ is compact; suppose that
it is disjoint from π−1
                      k′ /k
                            (x). Then πk′ /k (∂ X k′ ) is a closed subset of X not containing x, so
there exists an open neighborhood V of x such that Vk′ = π−1            k′ /k
                                                                              (V ) ⊂ Int(X k′ ). This means
that ∂ Vk′ = ; by 2.11(3,4). But x ∈ ∂ V , and boundarylessness can be checked after
extension of scalars by [CT21, Theorem 11.5]. This contradiction proves the claim. □
2.13. A k-analytic space X is called rig-smooth at x ∈ X if it is flat (in the sense of
[Duc18]) and if the sheaf of Kähler differentials ΩX (considered on the G-topology) is
free at x of rank equal to the dimension of X at y. We call X smooth if it is rig-smooth
and boundaryless. We refer to [Duc18, Chapter 5] for a discussion (note that rig-smooth
is called quasi-smooth there) and comparison to other definitions.
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                9

2.14. Models and formal geometry. A quasi-compact admissible formal scheme over
k◦ is a quasi-compact formal scheme X over k◦ with an open covering by affine formal
schemes Spf(A) for k◦ -algebras A which are topologically of finite type and flat over k◦ .
The generic fiber Xη of X is the strictly k-analytic space obtained by gluing the Berkovich
spectra M (A ⊗k◦ k), and the special fiber Xs is the scheme over ek obtained by gluing the
affine schemes Spec(A ⊗k◦ ek).

Definition 2.15. A formal k◦ -model X for a quasi-compact strictly k-analytic space X is a
```

## GR, newline lines 454--1190

```text
smooth strictly analytic curves to arbitrary k-analytic curves.
3.1 (k-Analytic Curves). By a k-analytic curve we mean a separated k-analytic space of
pure dimension 1. We gather the following facts about k-analytic curves:
   (1) A k-analytic curve is good, i.e., every point has an affinoid neighborhood. [Duc24,
        Proposition 3.3.7]
   (2) A k-analytic curve is paracompact. [Duc24, Théorème 4.5.10]
   (3) If X is an affinoid k-analytic curve, then ∂ X coincides with the Shilov boundary
        of X . [Thu05, 2.1.2]
An analytic domain in a k-analytic curve (for example, an open subset) is again a k-
analytic curve.
3.2 (Thuillier’s Harmonic Functions). Thuillier [Thu05, §2.3] defines a sheaf of harmonic
functions on a smooth, strictly k-analytic curve for a non-trivially valued k, roughly as
follows. If X is affinoid, then a continuous function h: X → R is harmonic if, after passing
to a finite, separable field extension, it coincides with the composition of a harmonic
function on a skeleton of X (in the sense of graph theory) with the retraction to the
skeleton. If X is smooth, then a harmonic function on an open subset of X is defined to be
a continuous function whose restriction to every strictly affinoid subdomain is harmonic.
3.3 (Thuillier’s Subharmonic Functions). For a non-trivally valued k, Thuillier [Thu05,
Définition 3.1.5] defines a subharmonic function on a smooth, strictly k-analytic curve X
to be an upper semicontinuous function u: X → R ∪ {−∞} that is not identically −∞
on any connected component of X and that satisfies the following property: for every
strictly k-affinoid domain U ⊂ X and every harmonic function h: U → R, if u ≤ h on ∂ U
then u ≤ h on U.
  Now we extend this definition to the case of non-smooth curves. The idea is that a
function should be subharmonic if it pulls back to a subharmonic function along any
morphism from a smooth curve. However, an inseparable curve over an imperfect field
does not admit any non-constant morphisms from a smooth curve, so one has to allow
an extension of scalars as well. We also consider the constant function −∞ to be sub-
harmonic, following Demailly [Dem85] in the complex case.
Definition 3.4 (Subharmonic functions). Let X be a k-analytic curve and let u: X →
R ∪ {−∞} be an upper semicontinuous function. We say that u is subharmonic provided
that, for every non-trivially valued analytic extension field k′ /k, every smooth, connected,
strictly k′ -analytic curve Y , and every morphism Y → X k′ , the composition
                                        πk′ /k     u
                              Y −→ X k′ −→ X −→ R ∪ {−∞}
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              11

is either subharmonic on Y in the sense of [Thu05, Définition 3.1.5], or is identically −∞.
3.4.1. If X is a smooth, connected, strictly k-analytic curve over a non-trivially valued k,
then an upper semicontinuous function u: X → R ∪ {−∞} is subharmonic in our sense
if and only if it is either subharmonic in Thuillier’s sense or is identically −∞. Indeed, if
u is subharmonic in our sense then one can take k = k′ and Y = X to see that it is either
subharmonic in Thuillier’s sense or is identically −∞. Conversely, if u is identically −∞
then it is clearly subharmonic in our sense, and if u is subharmonic in Thuillier’s sense
then it is subharmonic in our sense by [Thu05, Proposition 3.1.14 and Corollaire 3.4.5].
3.4.2. As a special case of (3.4.1), if X is a smooth, connected, strictly k-analytic curve
over a non-trivially valued k, then a function u: X → R (taking finite values) is subhar-
monic in our sense if and only if it is subharmonic in Thuillier’s sense.
  Here we collect the basic properties of subharmonic functions, which we will prove
over the course of this section.
Proposition 3.5. Let X be a k-analytic curve and let u: X → R ∪ {−∞} be an upper
semicontinuous function.
   (1) (Sheafiness) The subharmonic functions form a sheaf on X .
   (2) (Analytic functions) If f ∈ Γ (X , OX ) then log | f | : X → R ∪ {−∞} is subharmonic.
   (3) (Boundaries) If u is subharmonic on Int(X ), then u is subharmonic on X .
   (4) (Cone Property) If u1 , u2 : X → R ∪ {−∞} are subharmonic and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are subharmonic.
   (5) (Limits) The infimum of a decreasing net of subharmonic functions is subharmonic.
   (6) (Maximum Principle) If u is subharmonic and u attains a local maximum at x ∈
       Int(X ), then u is constant in a neighborhood of x.
   (7) (Extension of scalars) Let k′ /k be an analytic extension field. Then u is subharmonic
       if and only if u ◦ πk′ /k : X k′ → R ∪ {∞} is subharmonic.
   (8) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If u
       is subharmonic then u ◦ f is subharmonic, and the converse holds if f is finite and
       surjective.
   (9) (Finite Values) If u is subharmonic and u(x) = −∞ for a non-rig-point x ∈ X ,
       then u ≡ −∞ on the irreducible component of Int(X ) ∪ {x} containing x.
  Let us make some remarks regarding the content of Proposition 3.5.
3.5.1. If U ⊂ X is an open subset then U is again a k-analytic curve, so it makes sense
to speak of subharmonic functions on U. It is immediate from the definition that a sub-
harmonic function on X restricts to a subharmonic function on U. Hence subharmonic
functions form a presheaf on X . Proposition 3.5(1) asserts that this presheaf is a sheaf.
3.5.2. The maximum principle (Proposition 3.5(6)) is [Thu05, Proposition 3.4.10] in the
smooth, strictly analytic case.
3.5.3. In the situation of Proposition 3.5(7), it is immediate from Definition 3.4 that
u ◦ πk′ /k is subharmonic when u is subharmonic. This is the difficult direction in the
smooth, strictly analytic case: see [Thu05, Corollaire 3.4.5]. This result is hidden in the
12                                 W. GUBLER AND J. RABINOFF

fact that Definition 3.4 essentially recovers Thuillier’s definition of subharmonicity in that
case 3.4.1.
3.5.4. In the situation of Proposition 3.5(8), it is immediate from Definition 3.4 that u◦ f
is subharmonic when u is subharmonic. The remark in 3.5.3 applies to a lesser extent in
this case: see [Thu05, Proposition 3.1.14].
3.5.5. For any x ∈ X , the subset Int(X )∪{x} is open in X . This is obvious if x ∈ Int(X ), and
if x ∈ ∂ X then it follows from the fact that ∂ X is discrete in X . In particular, Int(X ) ∪ {x}
is again a k-analytic curve, so it makes sense to speak of its irreducible components
in Proposition 3.5(9). Irreducible components can only meet at rig-points (their inter-
sections are Zariski-closed), so a non-rig-point x is contained in a unique irreducible
component of Int(X ) ∪ {x}; this is implicit in Proposition 3.5(9).
3.5.6. Proposition 3.5(9) implies that if u is subharmonic and u(x) = −∞ for a non-rig-
point x ∈ X , then u ≡ −∞ in a neighborhood of x.
3.6. In order to extend Thuillier’s results, we will pass from a k-analytic curve to a
smooth, strictly k-analytic curve in four steps:
      (1) Extend scalars to a field as in 2.10 to make the curve strictly analytic.
                                                                                          −∞
      (2) If char(k) = p, then extend scalars to the completion of the perfect closure k p .
      (3) Replace the analytic curve by the underlying reduced curve.
      (4) Pass to the interior of the normalization, which is smooth (see 2.13).
We begin with some lemmas about this process.
                                                                                 −∞
Lemma 3.7. Suppose that char(k) = p > 0. Let k′ be the completion of k p . Then k′ is
perfect, and if X is a k-analytic space then πk′ /k : X k′ → X is a homeomorphism such that
π(∂ X k′ ) = ∂ X .
Proof. We leave it as an exercise for the reader to verify that k′ is perfect. The fact that
πk′ /k is a homeomorphism is [Duc09, Remarque 0.5], and the assertion about boundaries
is Lemma 2.12.                                                                            □
     We make the following observation to mirror Lemma 3.7. Its proof is immediate.
Lemma 3.8. Let X be a strictly k-analytic space and let ι : X red ,→ X be the inclusion of the
underlying reduced space. Then ι is a homeomorphism of underlying topological spaces, and
ι(∂ X red ) = ∂ X .
  We refer the reader to [Ber90, before Proposition 3.1.8] for the construction of the
normalization.
Lemma 3.9. Let X be a reduced, strictly k-analytic curve and let ν: Xe → X be its normal-
ization. Then the following hold:
    (1) Xe is rig-smooth if k is perfect.
    (2) ν is an isomorphism outside of a discrete set of rig-points of X .
                                     ∼
    (3) ν induces a bijection ∂ Xe −→ ∂ X .
    (4) ν is a topological quotient.
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                       13

                                                                             e = ν−1 (U) →
    (5) Let x ∈ X , let U be an open neighborhood of x, and consider the map U
        U. If U is a sufficiently small connected open neighborhood of x, then:
         (a) Ue → U is injective on connected components of U.  e
                                                                 ∼
         (b) Ue → U restricts to an isomorphism U  e \ ν−1 (x) −→ U \ {x}.
         (c) Every connected component of U   e intersects ν−1 (x).
    (6) A function h: X → R is R-PL if and only if h ◦ ν is R-PL.



Proof. The normalization Xe is locally the Berkovich spectrum of a Dedekind domain, so it
is rig-smooth when k is perfect because it is regular; this proves (1). Normalization is an
isomorphism away from codimension 1 as in algebraic geometry, which yields (2). Since
ν is finite, we have ∂ Xe = ν−1 (∂ X ) by the properties (2′ ) and (4′ ) of 2.11, so (3) follows
from (2) because the boundaries do not contain any rig-points. Assertion (4) was noted
in [Duc24, (3.1.3)].
    Now we prove (5). Since normalization is a local construction, we may shrink X to
assume that it is normal away from x. Suppose that ν−1 (x) = {x 1 , . . . , x n }, and choose
disjoint, connected open neighborhoods U1′ , . . . , Un′ of x 1 , . . . , x n , respectively. Let U ′ =
Sn                                                                         ∼
   i=1
       ν(Ui′ ).FSince ν induces an isomorphism Xe \ {x 1 , . . . , x n } −→ X \ {x}, it is clear that
                      n
ν−1 (U ′ ) = i=1 Ui′ . Since ν is a topological quotient, we have that U ′ is open, and ν is
injective on each Ui′ by construction.
    Suppose now that U ⊂ U ′ is a connected open neighborhood of x. By [Ber90, Theorem
3.2.1], U is path-connected. Clearly U satisfies (a) and (b). Let Ui = ν−1 (U) ∩ Ui′ , so that
                      e = ν−1 (U) = n Ui . In order to prove (c), it is enough to show that Ui
                                      F
x i ∈ Ui and U                          i=1
is path-connected. Let y ∈ Ui \ {x i }, and let γ: [0, 1] → U be a path from π( y) to x.
We may assume that γ−1 (x) = {1}, so that γ restricts to a path [0, 1) → U \ {x}. Let
γ
e : [0, 1) → U       e \ ν−1 (x) be the composition of γ|[0,1) with the inverse of the isomorphism
                      ∼
e \ ν−1 (x) −→ U \ {x}. Then γ
U                                        e(0) = y, so the image of γ e is contained in Ui . Extend γ  e
to a function [0, 1] → Ui by setting γ        e(1) = x i . One checks continuity of γ e at 1 using the
fact that an open neighborhood of x is the same as a collection of open neighborhoods
of x 1 , . . . , x n , as in the previous paragraph. This shows that Ui is path-connected.
    In the situation of (6), if h is R-PL then h◦ν is R-PL by [GJR21, Lemma 5.4(1)]. Suppose
then that h ◦ ν is R-PL. Piecewise linearity of h is local on X , and ν is an isomorphism
away from a finite set of (non-normal) rig-points, so it is enough to check that h is R-PL
in a neighborhood of a single rig-point x. Let x ′ ∈ Xe be a preimage ofPx. There is a
                                                                                          n
covering of Xe by strictly affinoid domains on which h ◦ ν has the form i=1 λi log | f i |,
where λi ∈ R and f i ∈ O × . Since x ′ is      Pan rig-point, it is contained in the interior   of one
of these affinoid domains, so h ◦ ν = i=1 λi log | f i | in a neighborhood of x . But if f is
                                                                                          ′

invertible in a neighborhood of a rig-point x ′ , then | f | is constant on a neighborhood of
x ′ (this elementary fact can be seen as a very special case of [Duc12, Theorem 3.4]). It
follows that h◦ν is constant in a neighborhood of x ′ . Suppose that ν−1 (x) = {x 1 , . . . , x n }.
For eachSn i choose an open neighborhood Ui of x i on which h ◦ ν is constant. As above,
U = i=1 ν(Ui ) is an open neighborhood of x, and clearly h is constant, hence R-PL,
on U.                                                                                                 □
14                                  W. GUBLER AND J. RABINOFF

Proof of Proposition 3.5(1). This follows from the corresponding fact for subharmonic
functions on smooth, strictly analytic curves [Thu05, Corollaire 3.1.13], except that one
has to be careful about where a function takes the value −∞. Suppose then that {Ui }
is an open cover of X and that u: X → R ∪ {−∞} is subharmonic on each Ui . Note that
u is upper semicontinuous. Let k′ /k be an analytic extension field with k′ non-trivially
valued, let Y be a smooth, connected, strictly k′ -analytic curve, and let f : Y → X k′ be a
morphism. Assume that u ◦ πk′ /k ◦ f ̸≡ −∞, so we must show that u ◦ πk′ /k ◦ f is sub-
harmonic in Thuillier’s sense. Let Ui′ = π−1 k′ /k
                                                   (Ui ) = (Ui )k′ and let Yi = f −1 (Ui′ ). Since u
is subharmonic on Ui , the composition u ◦ πk′ /k ◦ f |Yi is either subharmonic in Thuillier’s
sense or is identically −∞ on each connected component of Yi .
   Let W1 be the set of all points y ∈ Y that admit a neighborhood on which u ◦ πk′ /k ◦ f
is subharmonic in Thuillier’s sense, and let W2 be the set of all points y ∈ Y that admit a
neighborhood on which u ◦ πk′ /k ◦ f ≡ −∞. Clearly W1 and W2 are open, and they cover
Y since Y is covered by the connected components of the Yi . They are disjoint because if
u ◦ πk′ /k ◦ f is subharmonic in Thuillier’s sense on a connected neighborhood of y ∈ Y ,
then it cannot be identically −∞ on any neighborhood of y [Thu05, Lemme 3.1.9].
Since Y is connected and u ◦ πk′ /k ◦ f ̸≡ −∞, we have Y = W1 . The result now follows
from [Thu05, Corollaire 3.1.13].                                                                  □


Proof of Proposition 3.5(2). Let f be an analytic function on X . The function | f | is con-
tinuous and hence u := log | f | is upper semicontinuous as a continuous function with
values in R ∪ {−∞}. According to our definition of subharmonic functions, we have to
show that after base change of u with respect to an analytic field extension k′ /k with k′
non-trivially valued and then pull-back to a smooth strictly k′ -analytic curve, the resulting
function is subharmonic. This boils down to showing that u is subharmonic in the special
case of a smooth strictly k-analytic curve X . For this, we may assume X connected. If
f = 0, then u is identically −∞ and hence subharmonic in the sense of Definition 3.4. If
f is not identically zero, then the Poincaré–Lelong formula [Thu05, Proposition 3.3.15]
and the characterization in terms of positive currents [Thu05, Proposition 3.4.4] show
that u is subharmonic in the sense of Thuillier.                                            □


  We will use the following lemma in the proofs of Proposition 3.5(3,9). If X is a k-
analytic space and k′ /k is an analytic extension field, then π−1
                                                               k′ /k
                                                                     (x) = M (H (x)⊗
                                                                                   b k k′ )
has a finite Shilov boundary for any Abhyankar point x ∈ X by [Duc24, 3.2.14]; we
denote this boundary by x [k′ ] .

Lemma 3.10. Let X be a k-analytic curve and let k′ /k be an analytic field extension. Then
for all x ∈ ∂ X we have (∂ X k′ ) ∩ π−1
                                     k′ /k
                                           (x) = x [k′ ] .

Proof. Replacing X by an affinoid neighborhood of x, we may assume that X = M (A )
is affinoid. By a result of Ducros [Duc12, Lemme 3.1], there exists a morphism g : X →
B1 (0, s) for some s ∈ R>0 such that x ∈ g −1 (ηs ), where ηs is the maximal point of B1 (0, s).
                CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                                 15

This is discussed in detail in Section 6. Consider the commutative square

                                                          g′
                                                           → B1k′ (0, s)
                                                      ←
                                               X k′




                                                ←




                                                                  ←
                                           πk′ /k                   πk′ /k




                                                                 →
                                               →
                                                          g → B (0, s).
                                                      ←        1
                                                X

Since ∂ B1k′ (0, s) contains (only) its maximal point ηs,k′ , we have (g ′ )−1 (ηs,k′ ) ⊂ ∂ X k′
by (2.11.4) (which is an equality because B1k′ (0, s) is separated). The morphism g is an
Abhyankar presentation of x in the sense of [Duc24, 3.2.12.2], so by Proposition 3.2.13
of ibid, we have x [k′ ] = (g ′ )−1 (ηs,k′ ) ∩ π−1
                                                k′ /k
                                                      (x) ⊂ (∂ X k′ ) ∩ π−1
                                                                         k′ /k
                                                                               (x).
   For the reverse inclusion, let x ∈ (∂ X k′ ) ∩ πk′ /k (x), and suppose that x ′ ∈
                                        ′                   −1
                                                                                         / x [k′ ] . Since
∂ X k′ is the Shilov boundary of X k′ = M (A ⊗         b k k ), by [Ber90, Corollary 2.4.5] there exist
                                                            ′

f ∈ A⊗   b k k and ϵ > 0 such that | f | attains its maximum value at x ′ and such that
              ′

                          
                            y ∈ X k′ | f ( y)| > | f (x ′ )| − ϵ ⊂ X k′ \ x [k′ ] .

In particular, the restriction of f to π−1
                                        k′ /k
                                              (x) does not attain its maximum value on x [k′ ] ,
which cannot happen. Thus x ∈ x [k′ ] , so (∂ X k′ ) ∩ π−1
                                 ′
                                                         k′ /k
                                                               (x) ⊂ x [k′ ] .             □

Proof of Proposition 3.5(3). Suppose that u is subharmonic on Int(X ). Let k′ /k be an
analytic extension field with k′ non-trivially valued, let Y be a smooth, connected, strictly
k′ -analytic curve, and let f : Y → X k′ be a morphism. We must prove that u ◦ πk′ /k ◦
f is subharmonic in Thuillier’s sense or is identically −∞. Since ∂ Y = ;, it follows
from 2.11(4) that f (Y ) ⊂ Int(X k′ ). If πk′ /k ◦ f (Y ) ⊂ Int(X ) then u◦πk′ /k ◦ f is subharmonic
in Thuillier’s sense or is identically −∞ because u is subharmonic on Int(X ). Suppose
then that πk′ /k ◦ f ( y) = x ∈ ∂ X for some y ∈ Y , so that f ( y) ∈ Int(X k′ ) ∩ π−1                 k′ /k
                                                                                                             (x).
    We claim that πk′ /k (x)∩Int(X k′ ) is both open and closed in Int(X k′ ). By [Duc24, Propo-
                         −1

sition 5.3.4], if U is a connected component of π−1               k′ /k
                                                                        (X \ {x}), then the closure of U in
X k′ is contained in πk′ /k (X \ {x}) ∪ x [k′ ] . Let U be the connected component of X k′ \ x [k′ ]
                            −1                                ′

containing U. The above shows that U is closed in U ′ . Since U is open in X (an analytic
space is locally connected [Ber93, Remark 1.2.4(iii)] and hence its connected compo-
nents are open [Sta21, Lemma 04ME]), it is open in U ′ , so U = U ′ since U ′ is connected.
Hence π−1  k′ /k
                 (X \ {x}) is a union of connected components of X k′ \ x [k′ ] , so the same is
true of πk′ /k (x) \ x [k′ ] . Since X k′ \ x [k′ ] is itself a k-analytic space as x [k′ ] is a finite set, its
           −1

connected components are open, so we conclude that π−1                       k′ /k
                                                                                   (x) \ x [k′ ] is open and closed
in X k′ \ x [k′ ] . Since x ∈ ∂ X , we have (πk′ /k (x)) ∩ ∂ X k′ = x [k′ ] by Lemma 3.10, which
                                                         −1

shows Int(X k′ ) ⊂ X k′ \ x [k′ ] and π−1   k′ /k
                                                  (x) \ x [k′ ] = π−1 k′ /k
                                                                            (x) ∩ Int(X k′ ). We conclude that
πk′ /k (x) \ x [k′ ] is both open and closed in Int(X k′ ), as claimed.
  −1

    Since Y is connected, f (Y ) ⊂ Int(X k′ ), and f ( y) ∈ Int(X k′ ) ∩ π−1            k′ /k
                                                                                              (x), we deduce from
the above claim that f (Y ) ⊂ Int(X k′ )∩πk′ /k (x). Hence πk′ /k ◦ f is constant, so u◦πk′ /k ◦ f
                                                      −1

is constant. It follows that u is subharmonic in Thuillier’s sense or is identically −∞. □
16                                        W. GUBLER AND J. RABINOFF

Proof of Proposition 3.5(4,5). These follow quickly from the corresponding facts for sub-
harmonic functions on smooth, strictly analytic curves [Thu05, Proposition 3.1.8].     □

Proof of Proposition 3.5(6). Suppose first that X is strictly k-analytic for k non-trivially
                                                                                −∞
valued. If char(k) = p > 0 then let k′ be the completion of k p ; otherwise let k′ = k.
Let X ′ = X k′ and let π = πk′ /k : X ′ → X , so π is a homeomorphism preserving boundaries
by Lemma 3.7. Let ι : X red    ′
                                  ,→ X ′ be the inclusion of the underlying reduced space and let
ν: Xe ′ → X red′
                  be the normalization. Note that ν and ι are finite, so ∂ Xe ′ = (ι ◦ ν)−1 (∂ X ′ ),
and hence ∂ Xe ′ = (π◦ι ◦ν)−1 (∂ X ). Let Y = Int(Xe ′ ) and let f = ι ◦ν|Y : Y → X ′ . Then Y is
smooth and strictly analytic, so u ◦ π ◦ f is by definition either subharmonic in Thuillier’s
sense or identically −∞ on every connected component of Y .
   Suppose that u attains a local maximum at x ∈ Int(X ). If u(x) = −∞ then u must
be constant in a neighborhood of x by semicontinuity of u. Assume then that u(x) >
−∞. Both π and ι are homeomorphisms, so it suffices to show that u ◦ π ◦ ι : X red                 ′
                                                                                                      →
R ∪ {−∞} is constant in a neighborhood of the unique point x ∈ Int(X red ) mapping to
                                                                                 ′       ′

x. Choose a connected open neighborhood U ⊂ Int(X red                ′
                                                                       ) of x ′ as in Lemma 3.9(5), on
which u ◦ π ◦ ι attains a maximum at x ′ . By Lemma 3.9(3), we have ν−1 (U) ⊂ Y =
Int(Xe ′ ), so u ◦ π ◦ f is again either subharmonic in Thuillier’s sense or identically −∞
on each connected component C of ν−1 (U); since u(x) > −∞ and C ∩ ν−1 (x ′ ) ̸= ;, the
former is true. The function u◦π◦ f attains its maximum on every connected component
of ν−1 (U), so by the maximum principle for subharmonic functions on smooth, strictly
analytic curves [Thu05, Proposition 3.1.11], the function u ◦ π ◦ f is constant on every
connected component of ν−1 (U). It follows that u ◦ π ◦ ι is constant on U.
   Now we reduce to the strictly analytic case handled above. We may assume that X
is affinoid. As explained in 2.10, there is an analytic extension field k′ = k r for some
r ∈ R>0n
             such that X k′ is strictly k′ -analytic. Let σ : X → X k′ be the Shilov section of πk′ /k .
Then x = σ(x) ∈ Int(X k′ ) because π−1
           ′
                                                k′ /k
                                                      (Int(X )) ⊂ Int(X k′ ) by 2.11(5). It is immediate
from the definition that u ◦ πk′ /k is subharmonic, and it attains a local maximum at x ′ ,
so u ◦ πk′ /k is constant in an open neighborhood U ′ of x ′ . Then u is constant on the open
set U = σ−1 (U ′ ).                                                                                   □

Proof of Proposition 3.5(7). It is immediate from the definition that subharmonicity of
u implies subharmonicity of u ◦ πk′ /k . Suppose then that u ◦ πk′ /k is subharmonic. Let
k′′ /k be another analytic extension field with k′′ non-trivially valued, and let f : Y →
X k′′ be a morphism from a smooth, connected, strictly k′′ -analytic curve. Assume that
u ◦ πk′′ /k ◦ f ̸≡ −∞, so we need to show that u ◦ πk′′ /k ◦ f is subharmonic in Thuillier’s
sense. Let K be a non-Archimedean field that is simultaneously an analytic extension of
k′ and k′′ 2.2, and consider the following commutative diagram:

                               ←   fK            πK/k′
                                                 ←
                          YK            → XK          → X k′
                          ←



                                           ←



                                                            ←




(3.10.1)                                     πK/k′′             πk′ /k
                          →



                                          →



                                                            →




                               ←                 ←                ←
                           Y       f
                                       → X k′′         →
                                                  πk′′ /k   X            u → R ∪ {−∞}.
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                 17

Since u ◦ πk′ /k is subharmonic, the composition u ◦ πK/k ◦ f K is, on each connected compo-
nent C of YK , either subharmonic in Thuillier’s sense or identically −∞; since C surjects
onto Y [Duc18, 1.5.6] and u ◦ πk′′ /k ◦ f ̸≡ −∞, the latter does not happen. Replacing
X by Y and k′ /k by K/k′′ , we are reduced to showing that if X is smooth and strictly
k-analytic for k non-trivially valued and u ◦ πk′ /k is subharmonic in Thuillier’s sense, then
so is u.
   We can do this directly using Thuillier’s definition. (The converse is the difficult di-
rection: see [Thu05, Corollaire 3.4.5].) Let U ⊂ X be a strictly k-affinoid domain and
let h: U → R be a harmonic function such that u ≤ h on ∂ U. Then h ◦ πk′ /k : Uk′ =
π−1
  k′ /k
        (U) → R is harmonic by [Thu05, Proposition 2.3.18]. We have πk′ /k (∂ Uk′ ) = ∂ U by
Lemma 2.12, so u ◦ πk′ /k ≤ h ◦ πk′ /k on ∂ Uk′ . Since u ◦ πk′ /k is subharmonic in Thuillier’s
sense, this implies u ◦ πk′ /k ≤ h ◦ πk′ /k on Uk′ , so u ≤ h on U since πk′ /k : Uk′ ↠ U is
surjective. Thus u is subharmonic in Thuillier’s sense, as claimed.                          □

Proof of Proposition 3.5(8). It is immediate that subharmonicity of u implies subharmonic-
ity of u ◦ f . Suppose then that f is finite and surjective and that u ◦ f is subharmonic. Let
k′ /k be an analytic extension field with k′ non-trivially valued and let g : Z → X k′ be a
morphism from a smooth, connected, strictly k′ -analytic curve. Suppose that u◦πk′ /k ◦g ̸≡
−∞, so we need to show that u ◦ πk′ /k ◦ g is subharmonic in Thuillier’s sense. Let
W = Z ×X k′ Yk′ , and consider the following commutative diagram:

                                   ←   g′           πk′ /k
                                                    ←
                          W             → Yk′           → Y
                           ←




                                                             ←
                                            ←




(3.10.2)                f ′′           □       f′                f
                          →



                                            →



                                                             →




                                   ←                ←                ←
                               Z       g→   X k′        →
                                                    πk′ /k   X           u → R ∪ {−∞}.


The composition (u ◦ f ) ◦ πk′ /k ◦ g ′ is subharmonic because it is pulled back from u ◦ f by
an extension of scalars and the morphism g ′ : W → Yk′ . Since f is finite and surjective,
so are f ′ and f ′′ by 2.2, so we may replace X by Z and Y by W to assume X is a smooth,
connected, strictly k-analytic curve for k non-trivially valued and that u ̸≡ −∞. We can
check subharmonicity of u (in Thuillier’s sense) after extending scalars as in the proof of
Proposition 3.5(7), so we may assume in addition that k is perfect.
   Let ι : Yred ,→ Y be the inclusion of the underlying reduced space, and let ν: Ye → Yred be
the normalization. Since k is perfect, the normal curve Ye is rig-smooth, and since Ye → X
is finite and ∂ X = ; (as X is smooth), the curve Ye is smooth as well: see Lemmas 3.8
and 3.9. Both ι and ν are finite and surjective, so f ◦ ι ◦ ν: Ye → X is again finite and
surjective. By Definition 3.4 (with k = k′ ), subharmonicity of u ◦ f means that, on each
connected component C of Ye , the function (u◦ f )◦ι◦ν is either subharmonic in Thuillier’s
sense or is identically −∞. Since C → X is surjective (it is finite, hence it is a closed
map, and it is an open map by [Ber90, Lemma 3.2.4], so its image is all of X since X is
connected), the latter does not happen, so u ◦ f ◦ ι ◦ ν is subharmonic in Thuillier’s sense.
Thus we replace Y by Ye and f by f ◦ ι ◦ ν to assume X and Y are both smooth, and that
u ◦ f is subharmonic in Thuillier’s sense.
18                                W. GUBLER AND J. RABINOFF

   At this point, one proves that u is subharmonic in Thuillier’s sense directly from Thuil-
lier’s definition, as in the proof of Proposition 3.5(7), this time using [Thu05, Proposi-
tion 2.3.19]. The converse is the difficult direction: see [Thu05, Proposition 3.1.14]. □
  We will need the following lemma in the proof of Proposition 3.5(9). (Note that
Lemma 3.11 itself follows from Proposition 3.5(9) as we have seen in 3.5.5.)
Lemma 3.11. Let X be a strictly k-analytic curve over a non-trivially valued field k and let
u: X → R ∪ {−∞} be a subharmonic function. If x ∈ ∂ X and u(x) = −∞, then u ≡ −∞
on a neighborhood of x.
                                                          −∞
Proof. If char(k) = p > 0 let k′ be the completion of k p , and otherwise let k′ = k. Let
X ′ = X k′ and π = πk′ /k : X ′ → X , let ι : X red
                                                ′
                                                     ,→ X ′ be the inclusion of the underlying
reduced space, and let ν: Xe ′ → X red
                                     ′
                                        be the normalization. Then π and ι are homeomor-
phisms preserving boundaries by Lemmas 3.7 and 3.8, and ν is a boundary-preserving
isomorphism in a neighborhood of the unique point x ′ ∈ Xe ′ lying over x by Lemma 3.9.
The composition u ◦ π ◦ ι ◦ ν is subharmonic, so we may replace X by Xe ′ to assume that
X is rig-smooth. After shrinking X , we may assume that X is strictly affinoid. By [Ber90,
Corollary 1.3.6], if K is the completion of an algebraic closure of k then X K → X is an
open map, and by Lemma 2.12 there is a point of ∂ X K lying over x, so we may extend
scalars to assume that k is algebraically closed.
   By the semistable reduction theorem [Thu05, Théorème 2.3.8], there exists a semistable
(formal) model X of X . Let red: X → Xs denote the reduction map, which is anti-
continuous. Let ξ ∈ Xs be any point. As explained in [BPR13, Theorem 4.6] (see also
[BL85, Propositions 2.2 and 2.3]), if ξ is a generic point then red−1 (ξ) is a single type-2
point of X ; if ξ is a smooth closed point then red−1 (ξ) is isomorphic to an open unit ball;
and if ξ is a node then red−1 (ξ) is isomorphic to an open annulus. In particular, if ξ is a
closed point then red−1 (ξ) is connected and open.
   By [CD12, Lemme 6.5.1], the closure of ζ = red(x) is not proper, so ζ is a generic
point of Xs . Let Y ⊂ Xs denote its closure. Then red−1 (Y ) is an open neighborhood of
x in X . Let ξ ∈ Y be a closed point and let U = red−1 (ξ). Then x is a limit point of U:
one can use [BPR13, Lemma 3.2], or one can see this using retraction to the skeleton
S(X) from [Thu05, Théorème 2.2.10]; in this case, x is a vertex of S(X), and either U
deformation retracts onto x if ξ is smooth, or U contains an edge of S(X) adjacent to
x when ξ is a node. It follows that red−1 (Y ) is contained in the union of {x} with all
connected components U of Int(X ) having x as a limit point. We will show that u ≡ −∞
on every such U.
   We adapt the proof of [Thu05, Lemme 3.1.9]. Suppose that u ̸≡ −∞ on some such
U. Then u|U is subharmonic in Thuillier’s sense as U is smooth and connected and u is
subharmonic in our sense. By [Thu05, Lemme 2.3.9], for every N ∈ Z≥0 , there exists a
unique harmonic function hN : X → R such that hN (x) = −N and
                                           u( y) if u( y) > −∞
                                         
                               hN ( y) =
                                           0        otherwise
for every y ∈ ∂ X \ {x}. By construction, we have u − hN ≤ 0 on ∂ X . By [Thu05,
Corollaire 3.1.12], if the function u − hN attains a local maximum at a point y ∈ U, then
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                       19

u − hN takes a constant value C on U. By semicontinuity, we have
                                                             
                   −∞ = u(x) − hN (x) ≥ lim sup u(z) − hN (z) = C,
                                                   z→x
                                                   z∈U

which is a contradiction. Thus u−hN does not attain a local maximum on U. It does attain
a maximum on the closure U, which is compact. We have U ⊂ U ∪ ∂ X and u − hN ≤ 0 on
∂ X , so u−hN ≤ 0 on U. Clearly −hN (x) → ∞ as N → ∞, so by [Thu05, Lemme 2.3.10],
we have −hN → ∞ on U. Since u ≤ hN on U for all N , it follows that u ≡ −∞ on U. □
Proof of Proposition 3.5(9). We replace X by Int(X )∪{x} to assume that ∂ X = ; or ∂ X =
{x}. Replacing X by the irreducible component of X containing x (see 3.5.5), we assume
in addition that X is irreducible. Let k′ = k r /k be an analytic extension field for some
r ∈ R>0 n
           as in 2.10 such that X k′ is strictly k′ -analytic. Note that X k′ is again irreducible:
any irreducible component of X k′ is defined over a finite, separable extension of k inside
k′ [Duc18, 1.5.6], but k is algebraically closed in k′ [Duc24, 3.2.11]. The fiber π−1         k′ /k
                                                                                                    (x)
has a unique Shilov boundary point x ′ = σ(x), so by Lemma 3.10, if ∂ X = {x} then
∂ X k′ = {x ′ }; of course, if ∂ X = ; then ∂ X k′ = ; as well. Replacing X by X k′ and x by
x ′ , we may assume that X is strictly k-analytic and irreducible over a non-trivially valued
field k, and that ∂ X = {x} or ∂ X = ;.
                                                             −∞
    If char(k) = p > 0 let k′ be the completion of k p , and otherwise let k′ = k. Let X ′ =
X k′ and let π = πk′ /k : X ′ → X , let ι : X red
                                              ′
                                                  ,→ X ′ be the inclusion of the underlying reduced
space, and let ν: Xe ′ → X red′
                                 be the normalization. Since π and ν are homeomorphisms,
the space X red is again irreducible, so Xe ′ is connected by [Duc09, Proposition 5.16]. Since
              ′

x is not a rig-point of X , there exists a unique point x ′ ∈ Xe ′ lying over x by Lemmas 3.7,
3.8 and 3.9. We must show that u◦π◦ι ◦ν ≡ −∞ on Xe ′ . Since u◦π◦ι ◦ν is subharmonic
by Proposition 3.5(7,8), we may replace X by Xe ′ to assume that X is rig-smooth and
connected (and still that ∂ X = ; or ∂ X = {x} using the quoted lemmas again).
    If ∂ X = ; then X is smooth and connected, so u is either identically −∞ or it is sub-
harmonic in Thuillier’s sense. The latter case is impossible when u(x) = −∞ by [Thu05,
Proposition 3.4.10].
    Suppose then that X is rig-smooth and connected, and that ∂ X = {x} and u(x) = −∞.
By Lemma 3.11, there is an open neighborhood U of x on which u ≡ −∞. Since X
is connected, every connected component of Int(X ) contains x in its closure. Thus U
intersects every connected component C of Int(X ). This implies that u takes the value
−∞ on a non-rig point of C, so the previous paragraph shows that u ≡ −∞ on C. It
follows that u ≡ −∞ on X .                                                                           □
3.12. Now we turn to harmonic functions. Let X be a smooth, strictly k-analytic curve
with k non-trivially valued and let h: X → R be a function. We claim that h is harmonic
in the sense of (3.2) if and only if h and −h are subharmonic (in our sense or Thuillier’s—
see (3.4.2)). This is implicit in Thuillier’s thesis, but it requires justification. Suppose then
that h: X → R is harmonic. Then ±h are subharmonic by [Thu05, Proposition 2.3.13 and
Corollaire 3.1.12]. Conversely, suppose that ±h are subharmonic. This implies that h is
continuous. Let U ⊂ X be a strictly affinoid domain. By [Thu05, Lemme 2.3.9], there
exists a unique harmonic function h′ : U → R that coincides with h on ∂ U. By definition
20                                 W. GUBLER AND J. RABINOFF

of subharmonicity, we have h ≤ h′ on U. By the same argument as applied to −h, we see
that h = h′ on U, so that h is harmonic on U. As U was arbitrary, h is harmonic.
  By 3.12, the following definition recovers Thuillier’s definition of harmonicity on a
smooth, strictly k-analytic curve, and even on a strictly affinoid rig-smooth curve us-
ing [Thu05, Corollaire 2.3.14].
Definition 3.13 (Harmonic functions). Let X be a k-analytic curve for a possibly trivially
valued non-Archimedean field k. A function h: X → R is harmonic if h and −h are both
subharmonic.
   The advantage of this definition is that the following basic properties of harmonic func-
tions follow immediately from the corresponding properties of subharmonic functions.
Proposition 3.14. Let X be a k-analytic curve and let h: X → R be a continuous function.
     (1) (Sheafiness) The harmonic functions form a sheaf on X .
     (2) If f ∈ Γ (X , OX× ) then log | f | is harmonic.
     (3) The harmonic functions on X form a real vector space.
     (4) (Limits) If h is locally a uniform limit of harmonic functions, then it is harmonic.
     (5) (Maximum Principle) If h is harmonic and h attains a local extremum at x ∈ Int(X ),
         then h is constant in a neighborhood of x.
     (6) (Extension of Scalars) Let k′ /k be an analytic extension field. Then h is harmonic
         if and only if h ◦ πk′ /k : X k′ → R is harmonic.
     (7) (Functoriality) Let Y be a k-analytic curve and let f : Y → X be a morphism. If h is
         harmonic then h ◦ f is harmonic, and the converse holds if f is finite and surjective.
     (8) (Boundaries) If h is harmonic on Int(X ), then it is harmonic on X .
   We will later see in Theorem 7.6 that (4) holds even for pointwise limits. The fol-
lowing proposition asserts that Definition 3.13 is equivalent to the notion of harmonicity
in [GJR21, Definition 7.2]. We assume that k is non-trivially valued as in ibid.
Proposition 3.15. Let X be a strictly k-analytic curve and let h: X → R be a continuous
function. The function h is harmonic if and only if it is R-PL and the line bundle Lh (x) ∈
Pic(red(X , x))R defined in (2.17) is numerically trivial for every point x ∈ X .
Proof. This is [GJR21, Proposition 15.7] in the rig-smooth case; we reduce to this case
                                                                         −∞
in the usual way. If char(k) = p > 0 let k′ be the completion of k p , and otherwise let
k′ = k. Let X ′ = X ⊗b k k′ and let π: X ′ → X be the structure morphism. Let ι : X red
                                                                                      ′
                                                                                        ,→ X ′
be the underlying reduced space and let ν: Xe ′ → X red  ′
                                                            be the normalization, so that Xe ′ is
rig-smooth. Let f : Xe ′ → X denote the composition π ◦ ι ◦ ν.
   Suppose that h is harmonic. Then h ◦ f is harmonic by Proposition 3.14(6,7), so h ◦ f
is R-PL and Lh (x ′ ) is numerically trivial for all x ′ ∈ Xe ′ by the rig-smooth case. Then
h is R-PL by Lemma 3.9(6) and [GJR21, Lemma 5.3(3), Corollary 5.11], and Lh (x) is
numerically trivial for all x ∈ X by [GJR21, Proposition 7.6(1′ , 2′ )]. Conversely, suppose
that h is R-PL and that Lh (x) is numerically trivial for all x ∈ X . The same holds for
h ◦ f by [GJR21, Proposition 7.6(1′ , 2′ )], so h ◦ f is harmonic by the rig-smooth case, and
hence h is harmonic by Proposition 3.14(6,7).                                                  □
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES               21

Remark 3.16. We still assume that X is a strictly k-analytic curve over a non-trivially
valued field k and that h: X → R is continuous. Proposition 3.15 and Proposition 3.14(6)
imply in particular that if h◦πk′ /k is harmonic for some analytic extension field k′ /k, then
h◦πk′′ /k is R-PL for any analytic extension k′′ /k, which is by no means obvious. Likewise,
Proposition 3.14(7) implies that if f : Y → X is finite and surjective and h◦ f is harmonic,
then h is R-PL, and Proposition 3.14(8) implies that if h|Int(X ) is harmonic then h is R-PL.

                     4. CLASSICALLY PLURISUBHARMONIC FUNCTIONS
  In this section we define the notion of a classically plurisubharmonic function. The
definition follows Definition 3.4.
Definition 4.1 (Classically Plurisubharmonic Functions). Let X be a k-analytic space and
let u: X → R ∪ {−∞} be an upper semicontinuous function. We say that u is classically
plurisubharmonic or classically psh provided that, for every analytic extension field k′ /k,
every k′ -analytic curve Y , and every morphism f : Y → X k′ , the function u◦πk′ /k ◦ f : Y →
R ∪ {−∞} is subharmonic on Y in the sense of Definition 3.4.
4.1.1. Any class of psh functions should respect extension of scalars and should be stable
under pullback, so the conditions in Definition 4.1 are necessary. In complex analysis,
this condition (without the extension of scalars) is the definition of plurisubharmonicity,
which is why we call the notion “classically psh”.
4.1.2. If X is a k-analytic curve, then a function u: X → R∪{−∞} is classically psh if and
only if it is subharmonic. Indeed, if u is classically psh then taking k′ = k and Y = X in
Definition 4.1 shows that u is subharmonic, and if u is subharmonic then it is classically
psh by Proposition 3.5(7,8).
4.1.3. In Definition 4.1, one can assume that Y is a connected, smooth, strictly k′ -analytic
curve: this follows from Definition 3.4.
  Classically psh functions satisfy the basic properties of subharmonic functions on curves.
Proposition 4.2. Let X be a k-analytic space.
   (1) (Sheafiness) The classically psh functions form a sheaf on X .
   (2) If f ∈ Γ (X , OX ) then log | f |: X → R ∪ {−∞} is classically psh.
   (3) (Cone Property) If u1 , u2 : X → R∪{−∞} are classically psh and λ1 , λ2 ∈ R≥0 then
       λ1 u1 + λ2 u2 and max{u1 , u2 } are classically psh.
   (4) (Limits) The infimum of a decreasing net of classically psh functions is classically
       psh. For arbitrary pointwise limits, we refer to Theorem 6.5.
   (5) (Extension of Scalars) Let k′ /k be an analytic extension field. A function u: X →
       R ∪ {−∞} is classically psh if and only if u ◦ πk′ /k : X k′ → R ∪ {−∞} is classically
       psh.
   (6) (Functoriality) Let Y be a k-analytic space and let f : Y → X be a morphism. If
       u: X → R ∪ {−∞} is classically psh then u ◦ f is classically psh, and the converse
       holds if f is finite and surjective.
Proof. Properties (1,3,4) follow immediately from Proposition 3.5(1,4,5). For Proposi-
tion 4.2(2), we consider an analytic function f on X . As | f | is continuous, we deduce
22                                  W. GUBLER AND J. RABINOFF

that log | f | is a continuous function with values in R ∪ {−∞} and hence it is upper semi-
continuous. Then Proposition 4.2(2) follows from Proposition 3.5(2).
    To prove Proposition 4.2(5), it is clear from the definitions that if u is classically psh,
then u ◦ πk′ /k is classically psh for every analytic extension field k′ /k. To prove the con-
verse, we assume that k′ /k is an analytic extension field and that u′ := u ◦ πk′ /k is a
classically psh function on X k′ . Since the morphism πk′ /k is closed and surjective 2.9,
it is clear that u is upper semicontinuous. Let k′′ /k be an analytic extension field and
let f : Y → X k′′ be a morphism over k′′ from a k′′ -analytic curve Y . We have to show
that u ◦ πk′′ /k ◦ f is subharmonic. As in the proof of Proposition 3.5(7), we consider
a simultaneous analytic extension field K of k′ and k′′ . It follows from the above that
u ◦ πK/k = u′ ◦ πK/k′ is classically psh and hence u ◦ πK/k ◦ f K is subharmonic. We con-
clude from the commutative diagram (3.10.1) that u ◦ πK/k ◦ f K = u ◦ πk′′ /k ◦ f ◦ πK/k′′ is
subharmonic and hence u ◦ πk′′ /k ◦ f is subharmonic by Proposition 3.5(7).
    Likewise, the proof of Proposition 4.2(6) follows the same lines as the proof of Propo-
sition 3.5(8). Again, it follows from the definitions if u is a classically psh function on X ,
then u ◦ f is a classically psh function on Y . Conversely, we assume that u ◦ f is a clas-
sically psh function for a finite surjective morphism f : Y → X . Since finite morphisms
are proper and hence closed, we deduce from upper semicontinuity of u ◦ f and from
surjectivity of f that u is upper semicontinuous. It remains to show that u ◦ πk′ /k ◦ g is
subharmonic for any analytic extension field k′ /k and any morphism g : Z → X k′ from a
connected k′ -analytic curve Z. Setting W := Z ×X k′ Yk′ , we get a morphism g ′ : W → Yk′
from f by base change with respect to f ′ : Yk′ → X k′ as in (3.10.2). Since u ◦ f is classi-
cally psh, it follows from Proposition 4.2(5) that u ◦ πk′ /k ◦ f ′ = u ◦ f ◦ πk′ /k is classically
psh. The morphism f is finite and surjective, hence the same holds for f ′ . We con-
clude that the base change f ′′ : W → Z of the morphism f ′ is finite and surjective. The
k′ -analytic space W has irreducible components of dimension 1 and maybe isolated irre-
ducible components of dimension 0. Removing the latter, we obtain a k′ -analytic curve
W ′ as an open and closed subset of W . Since Z is a connected k′ -analytic curve and f ′′
is a finite surjective map from W onto Z, we get an induced finite surjective morphism
W ′ → Z. Indeed, as W ′ is also Zariski-closed in W , we deduce from finiteness of f ′′ that
f ′′ (W ′ ) is a Zariski-closed subset in Z of dimension 1 and hence f ′′ (W ′ ) = Z as Z is a
connected k′ -analytic curve. Since the inclusion W ′ → W is obviously finite, the com-
position W ′ → Z is also finite. In the following, we replace W by W ′ , which preserves
the commutativity of the diagram (3.10.2) and has the advantage that W is a k′ -analytic
curve. It follows that u ◦ πk′ /k ◦ f ′ ◦ g ′ = u ◦ πk′ /k ◦ g ◦ f ′′ is subharmonic on W . The
morphism of k′ -analytic curves f ′′ : W → Z is finite and surjective, so we deduce from
Proposition 3.5(8) that u ◦ πk′ /k ◦ g is subharmonic.                                           □

  In the paper [GR25], we have studied semipositive R-PL functions on a good strictly
k-analytic space over a non-trivially valued non-archimedean field k. This turns out to
be the same as an R-PL function that is classically psh, as we now show.

Theorem 4.3. Suppose that the valuation on k is nontrivial. Let X be a good, strictly k-
analytic space and let h: X → R be an R-PL function. Then h is semipositive if and only if h
is classically psh.
              CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES                  23

Proof. For x ∈ X , an R-PL function h: X → R induces a residue line bundle Lh (x) ∈
Pic(red(X , x))R on the reduction red(X , x) of the germ (X , x): see 2.17. Recall from
[GJR21, Definition 7.2] that h is semipositive at x ∈ X if and only if the associated residue
```

## Wanner, newline lines 168--1612

```text
Terminology. In this paper, let K be an algebraically closed field endowed with a com-
plete, non-archimedean, non-trivial absolute value | |. We write val(K × ) := − log |K × |
and R := {x ∈ K | |x| ≤ 1} with maximal ideal m ⊂ R and residue field K   e := R/m. By
suitably normalizing the absolute value | |, we may assume that Z, and so Q, is contained
in val(K × ). A variety over K is an irreducible separated reduced scheme of finite type
over K and a curve is a 1-dimensional variety over K.

Acknowledgements. The author would like to thank Walter Gubler for very carefully
reading drafts of this work and for the helpful discussions. The author is also grateful
to Philipp Jell for providing a simplification of the proof of Proposition 4.4 and further
useful comments. Finally, the author would like to thank the referee for their very precise
report and helpful suggestions.


     2. Preliminaries on Thuillier’s notion of subharmonic functions
   Let X be a smooth algebraic curve over K and X an be its analytification. In this
section, we define subharmonic functions in the sense of Thuillier on X an and give some
properties of these functions. Subharmonic functions are defined with the help of har-
monic functions as in the complex case. We therefore recall the definition of harmonic
functions on strictly affinoid domains from [Thu05, §2.3]. For this definition, one needs
the skeleton S(Y) corresponding to a strictly semistable formal model Y of a strictly
affinoid domain Y , which has the structure of a finite graph.
   Furthermore, we study lisse (subharmonic) functions, which are crucial for the proofs
in Section 4. These functions are Thuillier’s smooth functions, but note that they are
totally different from those smooth functions introduced by Chambert-Loir and Ducros,
which we define in Section 3. Hence, we use the term lisse instead of smooth here.

Definition 2.1. A semistable R-curve is an integral admissible formal R-curve Y whose
special fiber has only ordinary double points as singularities. A semistable R-curve is
called strictly semistable if in addition the irreducible components of the special fiber
are smooth. Let Y be a strictly analytic domain in X an , i.e. a subset that has a locally
finite covering by strictly affinoid domains, then we say that Y is a (strictly) semistable
formal model of Y if Y is a (strictly) semistable proper formal R-curve with generic fiber
Y η isomorphic to Y .

Definition 2.2. Let Y be a strictly semistable proper formal R-curve, then there is a
corresponding closed subset S(Y) of the generic fiber Y η consisting of points of type II
and III (see [Ber90, §1.4.4] for the classification of points) that has the structure of a
finite metric graph and has a canonical retraction map τY : Y η → S(Y) (cf. [Thu05,
Théorème 2.2.10] or [BPR13, Chapter 3 & 5]). We call S(Y) the skeleton of Y and the
canonical metric is called the skeletal metric. Note that the irreducible components of
the special fiber of Y correspond to vertices, which are all of type II, and the points in
the intersection of two irreducible components correspond to the edges joining the two
vertices. For every edge e of S(Y), we have an isometry αe : [a, b] → e for a closed real
interval [a, b]. A piecewise affine function on S(Y) is a continuous function F : S(Y) → R
such that F |e ◦ αe is piecewise affine for every edge e of S(Y). We can define the outgoing
slope of a piecewise affine function F on S(Y) at a point x ∈ S(Y) along a tangent
direction ve at x corresponding to an adjacent edge e as

                         dve F (x) := lim (F |e ◦ αe )′ (α−1
                                                          e (x) + ε).
                                      ε→0
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES                     5


  One obtains a finite measure on X an by
                                     X X
                           ddc F :=       ( dve F (x))δx ,
                                      x∈S(Y)   ve
                                                           P
where e is running over all edges in S(Y) at x. Note that ve dve F (x) = 0 if F is affine in
x, and hence the sum is finite. Let S0 be a finite subset of S(Y). We say that a piecewise
affine function F on S(Y) is harmonic on S(Y)\S0 , and write F ∈ H(S(Y), S0 ), if
ddc F (x) = 0 for all x ∈ S(Y)\S0 .
Definition 2.3.        i) For a strictly semistable proper formal R-curve Y, we define
                              H(Y) := τY∗ (H(S(Y), ∂ Y η )),
        where ∂ Y η is the Berkovich boundary (see [Thu05, §2.1.2]) of the generic fiber
        Yη.
    ii) Let Y be a strictly affinoid domain in X an . Then there exists a strictly semistable
        R-curve Y and an isomorphism ϕ : Y → Y η (see [BL85] and [Thu05, Théorème
        2.3.8]), and we define the harmonic functions on Y as
                                   H(Y ) := ϕ∗ (H(Y)).
       Note that the definition is independent of ϕ and Y [Thu05, Proposition 2.3.3].
Definition 2.4. Let W be an open subset of X an . Then f : W → [−∞, ∞) is called
subharmonic if f is upper semi-continuous, f 6≡ −∞ on every connected component of
W and for every strictly K-affinoid domain Y in W and every harmonic function h on
Y , we have
                             (f |∂Y ≤ h|∂Y ) ⇒ (f |Y ≤ h).
  We recall some important properties of subharmonic functions from [Thu05, §3].
Proposition 2.5. The subharmonic functions form a sheaf on X an .
Proof. See [Thu05, Corollaire 3.1.13].                                                     
                                                                    ′ an
Proposition 2.6. Let X, X ′ be smooth algebraic curves, ϕ : (X ) → X an be a mor-
phism of K-analytic spaces and W be an open subset of X an . If f : W → R is a subhar-
monic function on W , then ϕ∗ f is a subharmonic function on ϕ−1 (W ).
Proof. See [Thu05, Proposition 3.1.14].                                                    
  In the following, we define the class of lisse functions using the characterization in
[Thu05, Proposition 3.2.4]. Note that we can replace compact strictly analytic domains
by strictly affinoid domains looking at the proof of [Thu05, Proposition 3.2.4] and using
[Thu05, Proposition 3.2.2].
Definition 2.7. Let W be an open subset of X an . A function f : W → R is called lisse
if for every strictly affinoid domain Y ⊂ W , there exists a strictly semistable formal
R-curve Y such that Y = Y η and f |Y = F ◦ τY for a piecewise affine function F on S(Y).
Proposition 2.8. Let W be an open subset of X an and f a subharmonic function on
W . For every relatively compact open subset W ′ of W , there is a decreasing net hfj i of
lisse subharmonic functions converging pointwise to f on W ′ .
Proof. See [Thu05, Théorème 3.4.2].                                                        
Definition 2.9. Let W be an open subset of X an and f : W → R be a lisse function on
W , then we denote by ddc f the unique real measure on W that
6                                         V. WANNER


     i) has discrete support contained in the set of type II and III points of X an , and
    ii) coincides with ddc F on Y whenever f = F ◦ τY on a strictly affinoid domain
        Y = Y η in W .
This measure exists and is unique by [Thu05, Théorème 3.2.10].
   With the help of this operator ddc , one can define harmonic functions on open subsets
in the Berkovich topology (see [Thu05, Corollaire 3.2.11]).
Definition 2.10. A function f : W → R on an open subset W of X an is called harmonic
if f is lisse and ddc f = 0. Harmonic functions form a sheaf on X an , which we denote by
HX .
  This measure leads also to a further way to decide whether a lisse function is subhar-
monic or not.
Proposition 2.11. A lisse function f : W → R is subharmonic if and only if ddc f ≥ 0.
Proof. See [Thu05, Proposition 3.4.4].                                                   
Proposition 2.12. Let Y    be a connected strictly affinoid domain in X an and x ∈ Y \∂Y
be a point of type II or III. Then there exists a unique lisse function gxY on X an such
that
      i) gxY is strictly positive on Y \∂Y and equal to zero on ∂Y ∪ X an \Y ;
     ii) ddc gxY is supported on ∂Y ∪ {x} with ddc gxY = −δx in a neighborhood of x;
    iii) for every harmonic function h on Y we have
                                             Z
(2.1)                                 h(x) =    h ddc gxY .
                                             ∂Y
Proof. See [Thu05, Proposition 3.3.7 & Corollaire 3.3.9].                                
Corollary 2.13. Let W be an open subset of X an . A continuous function f : W → R
is subharmonic if and only if for every connected strictly affinoid domain Y ⊂ W and
every point x ∈ Y \∂Y of type II or III, we have
                                   Z
                                        f ddc gxY ≥ 0.
                                      W
Proof. Consider a strictly affinoid domain Y in W and a harmonic function f on Y with
f ≤ h on ∂Y . As explained in [Thu05, Remarque 3.1.10], we may assume f = h on ∂Y ,
and without loss of generality Y is connected. For every x ∈ Y \∂Y of type II or III,
Equation (2.1) implies that
        Z              Z                       Z
                c Y              c Y
           f dd gx =        f dd gx − f (x) =       h ddc gxY − f (x) = h(x) − f (x).
         W               ∂Y                      ∂Y
                  R
Hence, we have W f ddc gxY ≥ 0 for every type II or III point in Y if and only if
h(x) ≥ f (x) for every type II or III point in Y . Since f and h are continuous and the
type II and III points are dense, the last is equivalent to h − f ≥ 0 on Y .          

3. Preliminaries on subharmonic functions in the sense of Chambert-Loir
                               and Ducros
  In this section, let X be an n-dimensional algebraic variety over K. We define psh
functions on open subsets of X an in the sense of Chambert-Loir and Ducros [CD12]. For
the definition of psh functions, we need the sheaf of smooth real-valued differential forms
on Berkovich analytic spaces introduced by them. We follow [Gub16] for the definition of
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES                                  7


these forms Ap,q
             X on the analytification X
                                          an of an algebraic variety X. One can also define

currents which are linear functionals on Ap,q
                                           X,c (W ) for an open subset W of X
                                                                              an satisfying
                                  p,q                                 p,q
a continuity property, where AX,c (W ) denotes the sections of AX (W ) with compact
support. We refer to [CD12, §4.2] or [Gub16, §6] for the precise definition of currents.
Subsequently, we will give a definition of the Monge-Ampère measure corresponding to
locally approximable functions, and give some properties of it. These properties are
needed in Section 4 for the proofs of our main theorems.
   We start with recalling (p, q)-superforms on open subsets of Rr , which were originally
defined by Lagerberg in [Lag12]. This theory of superforms leads to superforms on
polyhedral complexes developed in [CD12]. With the help of the theorem of Bieri-Groves
one can define real-valued differential forms on X an .
Definition 3.1.      i) For an open subset U ⊂ Rr denote by Ap (U ) the space of smooth
real differential forms of degree p. The space of superforms of bidegree (p, q) on U is
defined as
        Ap,q (U ) := Ap (U ) ⊗C ∞ (U ) Aq (U ) = Ap (U ) ⊗R Λq Rr∗ = Λp Rr∗ ⊗R Aq (U ).
  ii) There are differential operators
             d′ : Ap,q (U ) = Ap (U ) ⊗R Λq Rr∗ → Ap+1 (U ) ⊗R Λq Rr∗ = Ap+1,q (U )
             d′′ : Ap,q (U ) = Λp Rr∗ ⊗R Aq (U ) → Λp Rr∗ ⊗R Aq+1 (U ) = Ap,q+1 (U )
that are given by D ⊗ (−1)q id and (−1)p id ⊗D, where D is the usual exterior derivative.
 iii) There is a wedge product
                                             ′   ′             ′       ′
                        ∧ : Ap,q (U ) × Ap ,q (U ) → Ap+p ,q+q (U ),
                                                                   ′
                                   (α ⊗ ψ, β ⊗ ν) 7→ (−1)p q α ∧ β ⊗ ψ ∧ ν,
that is, up to sign, induced by the usual wedge product.
 iv) We have the following canonical involution J : Ap,q (U ) → Aq,p (U ) given by
                       X                                X
                  α=       αIJ d′ xI ∧ d′′ xJ 7→ (−1)pq   αIJ d′ xJ ∧ d′′ xI ,
                           I,J                                 I,J

where d′ x  I ∧ d′′ x   J := (dxi1 ⊗ . . . ⊗ dxip ) ⊗R (dxj1 ⊗ . . . ⊗ dxjq ) for I = {i1 , . . . , ip } and
J = {j1 , . . . , jq }.
  For all p, q the functor U 7→ Ap,q (U ) defines a sheaf on Rr and we have Ap,q = 0 if
max(p, q) > r.
Definition 3.2.          i) A polyhedron in Rr is the intersection of finitely many half-
        spaces Hi := {w ∈ Rr |hui , wi ≤ ci } with ui ∈ Rr∗ and ci ∈ R.
    ii) A polyhedral complex C in Rr is a finite set of polyhedra in Rr satisfying the
        following two properties:
         (a) If τ is a closed face of a polyhedra σ ∈ C , then τ ∈ C .
         (b) If σ, τ ∈ C , then σ ∩ τ is a closed face of both.
Definition 3.3. Let C be a polyhedral complex in Rr .
     i) We say that C is of dimension d if the maximal dimension of its polyhedra is
        d. A polyhedral complex C is called pure dimensional of dimension d if every
        maximal polyhedron in C has dimension d.
    ii) The support |C | of C is the union of all polyhedra in C .
   iii) For σ ∈ C , we denote by relint(σ) the relative interior of σ, by Aσ the affine
        space that is spanned by σ and by Lσ the corresponding linear subspace of Rr .
8                                                    V. WANNER


Definition 3.4. Let C be a polyhedral complex and Ω be an open subset of |C |. Then a
superform α ∈ Ap,q (Ω) of bidegree (p, q) on Ω is given by a superform α′ ∈ Ap,q (V ) where
V is an open subset of Rr with V ∩ |C | = Ω. Two forms α′ ∈ Ap,q (V ) and α′′ ∈ Ap,q (W )
with V ∩ |C | = W ∩ |C | = Ω define the same form in Ap,q (Ω) if we have for each σ ∈ C
               hα′ (x); v1 , . . . , vp , w1 , . . . , wq i = hα′′ (x); v1 , . . . , vp , w1 , . . . , wq i
for all x ∈ σ ∩ Ω, v1 , . . . , vp , w1 , . . . , wq ∈ Lσ . If this is true, we say that the restrictions
α′ |σ and α′′ |σ agree. If α ∈ Ap,q (Ω) is given by α′ ∈ Ap,q (V ), we write
                                                     α′ |Ω = α.
                               ′                                                                              ′
Remark 3.5. Let F : Rr → Rr be an affine map. If C ′ is a polyhedral complex of Rr and
C a polyhedral complex of Rr with F (|C ′ |) ⊂ |C |, then the pullback F ∗ : Ap,q (|C |) →
Ap,q (|C ′ |) is well-defined and compatible with the differential operators d′ and d′′ . In
particular, we have the operators d′ and d′′ on Ap,q (|C |) given by the restriction of the
corresponding operators on Ap,q (Rr ).
Definition 3.6. We set Grm := Spec K[T1±1 , . . . , Tr±1 ]. Recall that its Berkovich ana-
lytification Gr,an
              m    is the set of all multiplicative seminorms on K[T1±1 , . . . , Tr±1 ] extend-
ing the given absolute value | | on K endowed with the coarsest topology such that
Gr,an                                                    ±1       ±1
  m → R; ρ 7→ ρ(f ) is continuous for every f ∈ K[T1 , . . . , Tr ]. We define

                   trop : Gr,an r
                           m → R ; ρ 7→ (− log(ρ(T1 )), . . . , − log(ρ(Tr ))).
Note that trop is a proper map in the sense of topological spaces.
  Let U be an open affine subset of X and let ϕ : U → Grm be a closed embedding, then
we set ϕtrop := trop ◦ϕan and Tropϕ (U ) := ϕtrop (U an ).
Theorem 3.7 (Bieri-Groves). For every open affine subset U of X and every closed
embedding ϕ : U → Grm , the set Tropϕ (U ) is the support of an R-affine polyhedral complex
of pure dimension n = dim(X).
Proof. See [BG84, Theorem A].                                                                                     
                                                                                                                  ′
Definition 3.8. Let U, U ′ be open affine subsets of X and ϕ : U → Grm and ϕ′ : U ′ → Grm
be closed embeddings. We say that ϕ′ refines ϕ if U ′ ⊂ U and there is an affine
homomorphism (i.e. group homomorphism composed with a multiplicative translation)
       ′
ψ : Grm → Grm of multiplicative tori such that ϕ = ψ ◦ ϕ′ . This homomorphism induces
                                      ′
an integral affine map Trop(ψ) : Rr → Rr such that ϕtrop = Trop(ψ) ◦ ϕ′trop .
   We call an open affine subset U of X very affine if O(U ) is generated as a K-algebra by
O(U )× . If U is very affine, then there exists a canonical (up to multiplicative translation)
                                                                                             ′
closed embedding ϕU : U → Grm which refines all other closed embeddings ϕ : U → Grm
(see [Gub16, 4.12]). For the canonical embedding ϕU , we use the notations tropU :=
(ϕU )trop and Trop(U ) := tropU (U an ).
Definition 3.9. Let W be an open subset of X an . A tropical chart (V, ϕU ) of W consists
of the canonical closed embedding ϕU : U → Grm of a very affine open subset U of X
and an open subset V of W that is of the form V = trop−1        U (Ω) for an open subset Ω of
Trop(U ).
   We say that (V ′ , ϕU ′ ) is a tropical subchart of (V, ϕU ) if V ′ ⊂ V and U ′ ⊂ U . In this
situation, ϕU ′ refines ϕU .
Remark 3.10. Theorem 3.7 allows us to consider a superform α ∈ Ap,q  Trop(U ) (tropU (V ))
for a tropical chart (V, ϕU ) of X . Let (V , ϕU ′ ) be another tropical chart of X an ,
                                  an       ′
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES                             9


then (V ∩ V ′ , ϕU ∩U ′ ) is a tropical subchart of both by [Gub16, Proposition 4.16] with
ϕU ∩U ′ = ϕU × ϕU ′ . We get a canonical homomorphism ψU,U ∩U ′ : Gm    r+r ′ → Gr of the
                                                                                  m
underlying tori with
                                     ϕU = ψU,U ∩U ′ ◦ ϕU ∩U ′
                                                                        ′
on U ∩ U ′ and an associated affine map Trop(ψU,U ∩U ′ ) : Rr+r → Rr such that
                                tropU = Trop(ψU,U ∩U ′ ) ◦ tropU ∩U ′
and the tropical variety Trop(U ∩ U ′ ) is mapped onto Trop(U ) (see [Gub16, 5.1]). We
define the restriction of α to tropU ∩U ′ (V ∩ V ′ ) as
                       Trop(ψU,U ∩U ′ )∗ α ∈ Ap,q                             ′
                                              Trop(U ∩U ′ ) (tropU ∩U ′ (V ∩ V ))

and write α|V ∩V ′ .
Definition 3.11. Let X be an algebraic variety over K and W be an open subset of
X an . An element of Ap,q   X (W ) is given by a family (Vi , ϕUi , αi )i∈I such that
                                                                             S
       i) for all i ∈ I the pair (Vi , ϕUi ) is a tropical chart and W = i∈I Vi ;
      ii) for all i ∈ I we have αi ∈ Ap,qTrop(Ui ) (tropUi (Vi ));
     iii) for all i, j ∈ I the restrictions αi |Vi ∩Vj = αj |Vi ∩Vj agree;
   If α′ is another differential form of bidegree (p, q) on W given by a triple (Vj′ , ϕUj′ , α′j )j∈J ,
then we consider α and α′ as the same differential form if and only if
                                         αi |Vi ∩Vj′ = α′j |Vi ∩Vj′
for every i ∈ I and j ∈ J.
   Then W 7→ Ap,q                              an                          p,q
                   X (W ) defines a sheaf on X , which we denote by AX and we write
Ap,q
  X,c (W ) for the sections with compact support in W . If the space of definition is clear,
                                                                                  p,q
we often just use the notations Ap,q and Ap,q c . By Theorem 3.7, we have AX = 0 if
max(p, q) > n = dim(X).
   The differentials d′ and d′′ and the wedge product carry Rover. Moreover, for every
open subset W of X an there is a non-trivial integration map : An,n   c (W ) → R which is
compatible with pullback.
   Note that smooth differential forms of bidegree (0, 0) are well-defined continuous func-
tions.
Definition 3.12. Let W be an open subset of X an . A function f : W → R is called
smooth if f ∈ A0,0 (W ). We use the notations C ∞ (W ) := A0,0 (W ) and Cc∞ (W ) :=
A0,0
 c (W ).

   Next to (0, 0)-forms, we also work a lot with (n, n)-forms. It is important to know the
following fact about these forms.
Proposition 3.13. Let W be an open subset of X an and   R α ∈ A (W
                                                                  n,n
                                                                      R ). Then there
is a unique signed Radon measure µα on W such that W f dµα = W f α for every
f ∈ Cc∞ (W ). If α has compact support on W , so has µα and |µα |(W ) < ∞.
Proof. See [Gub16, Proposition 6.8].                                                                
Definition 3.14. Let U be an open subset of Rr . A superform α ∈ Ap,p(U ) is called
strongly positive if there exist finitely many superforms αj,s of type (0, 1) and non-
negative smooth functions fs on U such that
                          X
                      α=      fs α1,s ∧ J(α1,s ) ∧ . . . ∧ αp,s ∧ J(αp,s ).
                                s
10                                       V. WANNER


   Let C be a polyhedral complex and Ω an open subset of |C |. A superform α ∈ Ap,p (Ω)
is called strongly positive if there is a polyhedral decomposition of C such that the
restriction of α to relint(σ) ∩ Ω is strongly positive for every polyhedron σ ∈ C .
   For an open subset W of X an , a smooth form ω ∈ Ap,p (W ) is called strongly positive if
for every point x in W there is a tropical chart (V, ϕU ) with x ∈ V such that ω = α◦tropU
on V for a strongly positive form α ∈ Ap,p Trop(U ) (tropU (V )).
   Note that for forms of type (0, 0), (1, 1), (n − 1, n − 1) and (n, n) the notion of
strongly positivity defined here coincides with the other positivity notions from [CD12,
§5.1]. Thus, we just say that a smooth form ω in Ap,p (W ) is positive if it is of one of
these types and it is strongly positive.
   A smooth function f is (strongly) positive as a form if and only if f ≥ 0.
Definition 3.15. Let W be an open subset of X an . We call a function f : W → [−∞, ∞]
locally integrable if f is integrable
                             R          withR respect to every measure µα associated to a form
α ∈ An,n
       c  (W  ). We  write     W  f ∧ α := W f dµα .
   Then for every locally integrable (e.g. continuous) function f : W → [−∞, ∞] one can
define a current in the sense of [CD12, §4.2] by
                                                             Z
                        ′ ′′        n−1,n−1
                       d d [f ] : Ac        (W ) → R, α 7→      f ∧ d′ d′′ α.
                                                          W
Definition 3.16. Let W be an open subset of            an
                                                      X . A locally integrable  function
f : W → [−∞, ∞) is called psh if f is upper semi-continuous and d′ d′′ [f ] is a positive
current, i.e. d′ d′′ [f ](ω) ≥ 0 for all positive forms ω ∈ An−1,n−1
                                                             c       (W ).
  Note that we do not require that a psh function has to be continuous, contrary to
[CD12, Définition 5.5.1].
Proposition 3.17. Let W be a paracompact open subset of X an and (Vi )i∈I be an open
covering of W . Then there are smooth non-negative functions (ηj )j∈J with compact
support on W such that
     i) the family
                 P(supp(ηj ))j∈J is locally finite on W ;
    ii) we have j∈J ηj ≡ 1 on W ;
   iii) for every j ∈ J, there is a i(j) ∈ I such that supp(ηj ) ⊂ Vi(j) .
We call (ηj )j∈J a partition of unity subordinated to the open covering (Vi )i∈I .
Proof. See [Gub16, Proposition 5.10].                                                       
Remark 3.18. Note that every open subset W of X an is paracompact if X is a curve
[Ber90, Theorem 4.2.1 & 4.3.2].
Proposition 3.19. The psh functions form a sheaf on X an .
Proof. Let W be an open subset of X an and (Wi )i∈I be an open covering of W . Consider
a function f : W → [−∞, ∞). If f is psh on W , the restrictions f |Wi are clearly psh for
every i ∈ I.
   Assume that f |Wi is psh on Wi for every i ∈ I and show that f is then psh on W .
Consider ω ∈ An,nc (W ) and let V be a paracompact open neighborhood of supp(ω) in
W , which we can find by [CD12, 2.1.5 & Lemme 2.1.6]. Then ω ∈ An,n      c (V ), the family
(Vi := Wi ∩ V )i∈I defines an open covering of V and the restrictions f |Vi are psh for
every i ∈ I. Let (ηj )j∈J be a partition of unity subordinated to the covering (Vi )i∈I (see
Proposition 3.17). Then for every j ∈ J, we have ηj ω ∈ An,nc (Vi(j) ). Since f |Vi(j) is psh,
             R
the integral V f ∧ ηj ω has to be finite for every j ∈ J. Furthermore, we can write
               i(j)
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 11
    P
ω = j∈J ηj ω on V , where this sum has to be finite as ω has compact support on V .
Hence,
                     Z           Z          XZ
                        f ∧ω =      f ∧ω =            f ∧ ηj ω
                           W            V           j∈J   Vi(j)

has to be finite as well, i.e. f is locally integrable.
   Now, consider a positive form ω ∈ An−1,n−1     c     (W ). Again, we work over the paracom-
pact open neighborhood V of supp(ω) in W and consider ω as a form in An−1,n−1         c    (V ).
As above, P we have a partition of unity (ηj )j∈J subordinated to the covering (Vi )i∈I ,
and ω =       j∈J ηj ω, where the sum is finite since ω has compact support. Then
        n−1,n−1
ηj ω ∈ Ac        (Vi(j) ) and ηj ω is a positive form for every j ∈ J. Thus,
                                                 X          X
                 d′ d′′ [f |V ](ω) = d′ d′′ [f ](   ηj ω) =     d′ d′′ [f ](ηj ω) ≥ 0
                                              j             j
by linearity and the fact that f |Vi(j) is psh for every j ∈ J.           Since d′ d′′ [f ](ω) =
d′ d′′ [f |V ](ω), the function f is psh on W .                                                
  Next, we translate a very useful characterization of smooth psh functions from [CD12,
Lemme 5.5.3] to our setting.
Proposition 3.20. Let W be an open subset of X an . A smooth function f : W → R is
psh if and only if for every x ∈ W there is a tropical chart (V, ϕU : U → Grm ) of W with
x ∈ V such that f = ψ ◦ tropU on V for a smooth function ψ : Rr → R whose restriction
ψ|σ to every polyhedron σ in Rr with σ ⊂ tropU (V ) is convex.
Proof. First, assume that f is psh on W , i.e. d′ d′′ [f ] defines a positive current on W .
Since f is smooth, we can find for every x ∈ W a tropical chart (V, ϕU : U → Grm ) in W
with x ∈ V such that f = ψ ◦ tropU on V = trop−1                                      r
                                                  U (Ω) for a smooth function ψ : R → R
and an open subset Ω of Trop(U ). We choose a compact neighborhood B of tropU (x)
in Ω. Then the preimage Y := trop−1    U (B) under the proper map tropU is a compact
analytic domain. The restriction of the current d′ d′′ [f ] to this compact analytic domain
Y is still positive. Applying [CD12, Lemme 5.5.3] to f = ψ ◦ tropU : Y → R, we know
that for every polyhedron ∆ in Rr with ∆ ⊂ B the restriction ψ|∆ is convex. Now,
let Ω′ be an open neighborhood of tropU (x) in B and consider the open neighborhood
V ′ := trop−1     ′             −1                           ′
            U (Ω ) of x in tropU (B). Then the pair (V , ϕU ) is a tropical chart in W
that contains x and f |V ′ = ψ ◦ tropU , where ψ is smooth. Consider a polyhedron σ in
Rr with σ ⊂ Ω′ = tropU (V ′ ). Then σ ⊂ B, and so ψ|σ is convex.
   Next, we assume that there is for every x ∈ W a tropical chart (V, ϕU ) of W with
x ∈ V such that f = ψ ◦ tropU on V for a function ψ satisfying i) and ii). Our goal is to
show that f is psh in a neighborhood of x. As above, we choose a compact neighborhood
B of tropU (x) in tropU (V ) and set Y := trop−1U (B). Since every polyhedron ∆ in R
                                                                                          r

with ∆ ⊂ B is contained in tropU (V ), the restriction ψ|∆ is convex by ii). Again [CD12,
Lemme 5.5.3] tells us that f is psh on the compact analytic domain Y . Choosing (V ′ , ϕU )
as above, we obtain a tropical chart of W with x ∈ V ′ . Due to V ′ ⊂ Y , the function f is
psh on the open neighborhood V ′ of x. Psh functions form a sheaf by Proposition 3.19,
and so the claim follows.                                                                 
Remark 3.21. Let X and X ′ be algebraic varieties over K, ϕ : W ′ → W a morphism
of analytic spaces for open subsets W ⊂ X an and W ′ ⊂ (X ′ )an , and f : W → [−∞, ∞)
a psh function on W . If f is smooth, it follows directly from the definition of smooth
functions by Chambert-Loir and Ducros [CD12, 3.1.3] and [Gub16, Proposition 7.2] that
ϕ∗ f is smooth on ϕ−1 (W ). Furthermore, [Gub16, Proposition 7.2] and Proposition 3.20
12                                              V. WANNER


imply that ϕ∗ f is also psh on ϕ−1 (W ). If f is not smooth, it is not clear whether ϕ∗ f
is psh or not. At the end of this paper, we will answer this question positively for a
continuous psh function f on an open analytic subset of a smooth proper curve.
     We recall the following definitions from [CD12, §5.6].
Definition 3.22. A function f : W → R on an open subset W of X an is called locally
psh-approximable if every point of W has a neighborhood V in W such that f is the
uniform limit of smooth psh functions fi on V . A function f is locally approximable if it
is locally the difference of two locally psh-approximable functions. Furthermore, we say
that f is globally psh-approximable (resp. globally approximable) on W if f is a uniform
limit (resp. the difference of two uniform limits) of smooth psh functions on W .
   Let f : W → R be a locally psh-approximable function, then there exists a unique
positive Radon measure MA(f ) on W such that for every open subset V ⊂ W , g ∈
Cc∞ (V ) and smooth psh functions fi ∈ C ∞ (V ) converging uniformly to f |V , we have
                           Z                    Z
                               g dMA(f ) = lim     g ∧ (d′ d′′ fi )n ,
                               V                    i→∞ V

where n = dim(X) and (d′ d′′ fi )n is defined as the n-th wedge product of d′ d′′ fi . We call
MA(f ) the Monge-Ampère measure of f .
   For a locally approximable function f that is given locally by fV+ − fV− for locally psh-
approximable functions fV+ and fV− on V , we define the Monge-Ampère measure MA(f )
to be the measure obtained by gluing MA(fV+ ) − MA(fV− ). Note that the definition is
independent of the decompositions. For details see [CD12, Corollaire 5.6.5 & 5.6.6] and
[CD12, Définition 5.6.7].
Lemma 3.23. Let X be a curve, W be an open subset of X an and f : W → R.
   i) If f is locally approximable, we have
                                            Z
                               ′ ′′
                              d d [f ](g) =   g dMA(f )
                                                       W
          for every g ∈ Cc∞ (W ).
      ii) If f is locally psh-approximable, then f is in particular psh.
Proof. At first, note that every locally (psh-)approximable function is continuous, and so
locally integrable. We start with assertion i) and assume that f is locally approximable.
We therefore can cover W by open subsets Vi on which f is the difference of uniform
limits
                                              +        −
                                   f = lim fik  − lim fik
                                              k→∞          k→∞
                            +         −
of smooth psh functions fik    and fik   on Vi . Choose a partition of unity (ηj )j∈J subordi-
nated to this covering (Vi )i∈I (see Proposition 3.17). We write for simplicity Vj instead
of Vi(j) andPfjk instead of fi(j)k . Then for every j ∈ J, we have ηj g ∈ Cc∞ (Vj ). Further-
more, g = j∈J ηj g on W . Since g has compact support on W , the sum has to be finite.
Hence,
                        XZ
           ′ ′′
          d d [f ](g) =        f ∧ d′ d′′ (ηj g)
                         j∈J   Vj
                                         Z                               Z                    !
                         X
                                              +                               −
                     =             lim       fjk ∧ d′ d′′ (ηj g) − lim       fjk ∧ d′ d′′ (ηj g) .
                               k→∞ Vj                            k→∞ Vj
                         j∈J
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 13


Using the theorem of Stokes [Gub16, Theorem 5.17] twice, we get
                       Z                         Z
                             ±
                           fjk ∧ d′ d′′ (ηj g) =   ηj g ∧ d′ d′′ fjk
                                                                  ±
                                                                     ,
                                Vj                              Vj

and so we finally obtain
                                                Z                                 Z                       !
                              X
                                                                   +                                 −
           d′ d′′ [f ](g) =             lim         ηj g ∧ d′ d′′ fjk − lim           ηj g ∧ d′ d′′ fjk
                                        k→∞ Vj                             k→∞ Vj
                              j∈J
                                                                                            !
                              X Z                                     Z
                        =                      ηj g dMA(f + ) −            ηj g dMA(f − )
                              j∈J         Vj                          Vj
                              XZ                              Z
                        =                 ηj g dMA(f ) =              g dMA(f ).
                              j∈J    Vj                           W

For assertion ii), we assume that f is locally psh-approximable, i.e. we can cover W
by open subsets (Vi )i∈I such that f is the uniform limit f = limk→∞ fik of smooth
psh functions fik on Vi . As above let (ηj )j∈J be a partition of unity subordinated to
(Vi )i∈I . For every non-negative function g ∈ Cc∞ (W ), the smooth function ηj g is also
non-negative as ηj ≥ 0 and has compact support on Vj . From the calculations above,
we get
                                         X     Z
                        d′ d′′ [f ](g) =   lim   ηj g ∧ d′ d′′ fjk ≥ 0.
                                                       k→∞ Vj
                                                 j∈J

This proves that f is psh on W .                                                                                    
Lemma 3.24. Let X be a curve, f : W → R be a globally psh-approximable function,
i.e. f is the uniform limit of smooth psh functions fi on W , and g ∈ Cc0 (W ), then
                           Z                     Z
                                g dMA(f ) = lim     g ∧ d′ d′′ fi .
                                    W                     i→∞ W

Proof. By [CD12, Proposition 3.3.5], there are smooth functions gk ∈ Cc∞ (W ) converging
uniformly to g. Then
                     Z                        Z
                          g dMA(f ) = lim        gk dMA(f )
                       W                 k→∞ W
                                                  Z
                                      = lim lim       gk ∧ d′ d′′ fi
                                         k→∞ i→∞ W
                                                  Z
                                      = lim lim       gk ∧ d′ d′′ fi
                                         i→∞ k→∞ W
                                              Z
                                      = lim      g ∧ d′ d′′ fi .
                                                        i→∞ W


                                                                           R           ′ ′′
                                                                                                              R
Note that we may change the order of the limits since                          W gk ∧ d d fi converges to         W g∧
d′ d′′ fi uniformly in i ∈ N.                                                                                       

   Model functions and their Monge-Ampère measures play an important role in the
proofs of the main theorems in Section 4. We therefore recall the definition of metrics,
formal metrics and model functions.
14                                      V. WANNER


Definition 3.25. Let X be a proper and normal variety over K and L be a line bundle
on X. A continuous metric k k on Lan associates to every section s ∈ Γ(U, L) on a Zariski
open subset U of X a continuous function ksk : U an → [0, ∞) such that kf · sk = |f | · ksk
holds for every f ∈ OX (U ) and ks(x)k = 0 if and only if s vanishes in x.
   We call a continuous metric k k on Lan smooth (resp. psh) if for every open subset U
of X and every invertible section s of L on U the function − log ksk is smooth (resp. psh)
on U an .
   A continuous metric k k on Lan is psh-approximable if there is a sequence of smooth
psh metrics k kk on Lan such that supx∈X an | log(ksx (x)k/ksx (x)kk )| converges to zero
for any local section sx of L that does not vanish in x. Clearly, this is independent of
the choice of sx .
Definition 3.26. Let X be a proper variety over K and let L be a line bundle on X.
A semistable formal model of (X, L) is a pair (X , L) consisting of a semistable formal
model X of X an and a line bundle L on X such that L |X an ≃ Lan . Note that we always
may assume that X is strictly semistable by the semistable reduction Theorem [BL93,
Ch. 7] since K is algebraically closed.
   Let (X , L) be a semistable formal model of (X, L⊗m ) for m ∈ N>0 . Then one can
define a continuous metric on Lan in the following way: If U is a formal trivialization
of L and s is a section of Lan on U η such that s⊗m corresponds to λ ∈ OX an (U η ) with
respect to this trivialization, then
                                                   1
                             − log ks(x)kL := −       log |λ(x)|
                                                   m
for all x ∈ U η . This definition is independent of all choices and shows immediately that
the defined metric is continuous. Metrics of this form are called Q-formal metrics, and
they are called formal metrics if m = 1.
   Let OX be the trivial line bundle on X. A function f : X an → R of the form f =
− log k1kL for a formal metric k kL associated to a semistable formal model of (X, O X )
is called model function.
   We have the following statements for model functions due to Chambert-Loir and
Ducros and Katz, Rabinoff and Zureick-Brown. The first theorem is a direct consequence
of a result of Chambert-Loir and Ducros in [CD12, §6.3].
Theorem 3.27. Let X be a projective variety over K and f = − log k1kL be a model
function on X an for a semistable formal model (X , L) of (X, O X ).
     i) The function f is locally approximable on X an , and so the Monge-Ampère mea-
        sure MA(f ) exists.
    ii) We have the following identity of measures
                                         X
                                MA(f ) =    degL (Y )δζY ,
                                           Y

       where Y runs over all irreducible components of the special fiber X s and ζY is the
       unique point in X an mapped to the generic point of Y under the reduction map
       (see [Ber90, Proposition 2.4.4]).
Proof. By [CD12, Corollaire 6.3.5], we know that there are line bundles L1 , L2 on X
with formal models L1 , L2 such that OX = L1 ⊗ L−1              −1
                                                 2 , L = L1 ⊗ L2 , the corresponding
metrics k kL1 and k kL2 are psh-approximable and
                         − log k · kL = − log k · kL1 + log k · kL2
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 15


on X an . Let k ki,k be a sequence of smooth psh metrics converging uniformly to k · kLi
on X an . For every point x in X an , let U be an open subset of X with x ∈ U an and s an
invertible section of L1 = L2 on U . Then − log kskLi,k is a smooth psh function on U an
for i = 1, 2 and for every k ∈ N
        − log k1kL = − log kskL1 + log kskL2 = lim − log ksk1,k + lim log ksk2,k .
                                                    k→∞                  k→∞

Hence, the function f = log k1kL is locally approximable.
  The second assertion is shown in [CD12, §6.9].                                                

  The slope formula for line bundles by Katz, Rabinoff, and Zureick-Brown in [KRZB15]
implies directly the following theorem.
Theorem 3.28. Let X be a smooth proper algebraic curve over K and f = − log k1kL
be a model function on X an for a semistable formal model (X , L) of (X, O X ). The
restriction F of f to S(X ) is a piecewise affine function and f = F ◦ τX on X an .
Furthermore, we have
                               MA(f ) = ddc F = ddc f.
Proof. This follows directly from [KRZB15, Theorem 2.6] using Theorem 3.27.                     

        4. Comparison of the two notions of subharmonic functions
  In this section, we consider a smooth proper algebraic curve X over K. We show
that every subharmonic function on X an is psh and that every continuous psh function
on X an is subharmonic. In particular, the notion of subharmonic and the notion of psh
agree for continuous functions.

4.1. Thuillier’s subharmonic functions are also subharmonic in the sense of
Chambert-Loir and Ducros. In this subsection, we show that every subharmonic
function on an open subset of X an is psh. First, we prove that every lisse subharmonic
function is psh and that every subharmonic function is locally integrable. Then we use
these results and the fact that a subharmonic function is the limit of subharmonic lisse
functions from Proposition 2.8 to prove the general claim.
Remark 4.1. Every signed Radon measure µ on an open subset W of X an defines the
following current
                                                 Z
                        [µ] : Cc∞ (W ) → R, g 7→   g dµ
                                                          W
(see [Gub16, Example 6.3]). Consider a smooth function f ∈ C ∞ (W ), then we have seen
in Proposition 3.13 that the smooth form d′ d′′ f corresponds to a signed Radon measure
which we also denote by d′ d′′ f . Using the theorem of Stokes [Gub16, Theorem 5.17], we
get d′ d′′ [f ] = [d′ d′′ f ]. Recall that a function is called psh if and only if this current is
positive.
   Analogously, for every lisse function f : W → R we get a current [ddc f ] for the corre-
sponding measure ddc f from Definition 2.9 which is positive if and only if f is subhar-
monic (cf. Proposition 2.11).
Proposition 4.2. Let W be an open subset of X an and f : W → R a lisse function.
For every type II point x ∈ W , there is an open neighborhood V of x in W on which the
currents d′ d′′ [f ] and [ddc f ] agree.
16                                          V. WANNER


Proof. Consider a point x ∈ W and let Y be a strictly affinoid domain containing x
in its interior. Since f is lisse, there is a strictly semistable formal model Y of Y with
corresponding skeleton S(Y) and f = F ◦ τY on S(Y) for a piecewise affine function F
on S(Y).
   If x ∈
        / S(Y), then f is constant on an open neighborhood V of x, and so
                               d′ d′′ [f ] = [d′ d′′ f ] = [0] = [ddc f ]
on V .
   If x ∈ S(Y), we may assume that x is a vertex in S(Y). Let e1 = [x, y1 ], . . . , er = [x, yr ]
be the edges in S(Y) emanating from x, v1 , . . . , vr the corresponding tangent directions
and λi := dvi F (x). By blowing up Y, we may assume that F |ei is affine, d(x, yi ) ∈ Q and
that we divide the edge ei by an additional vertex yi′ with d(x, yi ) = 2d(x, yi′ ). Denote
this blowing up by Y ′ , and the tangent direction corresponding
                                                              S     to [yi′ , yi ] by vi′ . Define
the piecewise affine functions Fi on the closed subset Γ := i=1,...,r [x, yi ] of S(Y ′ ) by the
following data
            Fi (x) = 0, dvi (Fi )(x) = sgn(λi )δij and dvi′ (Fi )(yi′ ) = −dvi (Fi )(x).

Set fi = Fi ◦τY ′ on Y ′ := τY−1
                               ′ (Γ), which is a strictly affinoid domain in W . By definition,

fi = 0 on ∂Y for every i ∈ {1, . . . , r}. Note that ∂Y ′ = ∂Γ (cf. [JW18, Lemma 5.4]).
              ′

Hence, we can extend fi to X an by setting fi = 0 on X an \Y ′ . Then we have a G-
covering of X an on which fi is piecewise S linear, and      so fi is a model function on X an
[GK14, Proposition 8.11]. Set Γ := i=1,...,r [x, yi ] and V := τY−1
                                      ′                  ′                    ′ ◦
                                                                         ′ ((Γ ) ), which is an

open neighborhood of x in W . By the definition of fi on V , we have on V ⊂ Y
                                     Xr                            r
                                                                   X
(4.1)       f = F ◦ τY = F ◦ τY ′ = (   |λi |Fi ) ◦ τY ′ + F (x) =   |λi | · fi + F (x)
                                          i=1                                   i=1

and
                                            r
                                            X                r
                                                             X
                           c          c
(4.2)                   dd f = dd F =             λi δx =          |λi |(ddc (fi )).
                                            i=1              i=1

Since the functions fi are model functions, we know that they are locally approximable
on V and MA(fi ) = ddc (fi ) by Theorem 3.27 and Theorem 3.28. Let 0 ≤ g ∈ Cc∞ (V ).
Then for every i ∈ {1, . . . , r} we have by Lemma 3.23 and MA(fi ) = ddc (fi ) that
                                  Z               Z
                 ′ ′′
                d d [fi ](g) =       g dMA(fi ) =   g ddc (fi ) = [ddc fi ](g).
                                  V                      V

Linearity and the Equations (4.1) and (4.2) imply consequently d′ d′′ [f ](g) = [ddc f ](g).
                                                                                          
Proposition 4.3. Let W be an open subset of X an and f : W → R be a lisse function.
If f is subharmonic, then f is psh.
Proof. Note that the property to be psh, i.e. d′ d′′ [f ] ≥ 0, is a local property by Proposi-
tion 3.19.
   If x is of type I or IV, the lisse function f is constant on an open neighborhood V of
x in W by the definition of lisse. Hence, d′ d′′ [f ] = [d′ d′′ f ] = 0 on V .
   If x is of type II, we have seen in Proposition 4.2 that there is an open neighborhood
V of x in W such that d′ d′′ [f ] = [ddc f ] on V . Since f is subharmonic, the measure ddc f
on W is non-negative by Proposition 2.11, and so we have d′ d′′ [f ] = [ddc f ] ≥ 0 on V .
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 17


   If x is of type III, we choose a strictly affinoid domain Y that contains x in its interior.
Since f is lisse, there is a strictly semistable model Y of Y with corresponding skeleton
S(Y) and a piecewise affine function F on S(Y) such that f = F ◦ τY on Y .
   If x is not contained in S(Y), then there is as in the first case an open neighborhood
V of x in W on which f is constant, and so d′ d′′ [f ] = [d′ d′′ f ] = 0 on V .
   If x ∈ S(Y), then there is an edge e in S(Y) such that x lies in the interior of e. The
closed annulus A := τY−1 (e) is isomorphic to a closed annulus A′ = trop−1 ([val(b), val(a)])
in G1,an
      m    for some a, b ∈ K × with |a| < |b| and trop := − log |T |. Thus, we can identify
                                                                                        ∼
e with the real interval [val(b), val(a)] via trop ◦Φ for a fixed isomorphism Φ : A −   → A′ .
Since e is isometric to [val(b), val(a)], we can define a function
                     ψ : [val(b), val(a)] → R; z 7→ F ((trop ◦Φ)−1 (z)).
                                                           1,an
Then ψ extends to a piecewise affine function on trop(Gm        ) = R, and its restriction to
the connected components of R\{trop(Φ(x))} is affine with outgoing slopes at trop(Φ(x))
equal to the ones of F at x on e. We have required that f is subharmonic, so the sum of
the outgoing slopes at x is greater than or equal to zero by Proposition 2.11. Hence, ψ is
convex on R, and so we can find smooth convex functions ψi on R converging uniformly
                                                                                        1,an
to ψ. Then ψi ◦ trop are smooth psh functions on trop−1 (val(b), val(a)) ⊂ Gm                by
Proposition 3.20. By Remark 3.21, the pullbacks fi := Φ∗ (ψi ◦ trop) are smooth psh
function on V ′ := τY−1 (e◦ ) converging uniformly to f on V ′ . Note that by [BPR13,
Lemma 2.13 & 3.8], the map trop = − log |T | factors through τA and τA = τY on A.
Hence, the function f is itself psh on V ′ by Lemma 3.23, i.e. d′ d′′ [f ] ≥ 0 on V ′ .       
Proposition 4.4. Let W be an open subset of X an and f : W → [−∞, ∞) be a subhar-
monic function, then f is locally integrable.
                                   R
Proof. We have to show that W f ∧ ω is finite for every ω ∈ Ac1,1 (W ). By [Gub16,
Proposition 5.13], we may assume that the (1, 1)-form ω is of the form ω = trop∗U ωtrop for
a tropical chart (V, ϕU ) of W and a form ωtrop ∈ A1,1c (tropU (V )). The closed embedding
ϕU is given by γ1 , . . . , γr ∈ O(U )× , and we denote by H the set of zeros and poles of
γ1 , . . . , γr on X. We choose a strictly semistable model X of X such that the type I
points of H lie in distinct connected components of X an \S0 (X ) (see [BPR13, Theorem
4.11 & 5.2]), where S0 (X ) denotes the vertices of the skeleton S(X ) corresponding to X .
By [BPR13, Lemma 2.13 & 3.8], we have the following commutative diagram
                                                  tropU
                                             V            // Ω
                                                        ③③==
                                        τX            ③③
                                                   ③③③trop
                                                ③         U

                                        S(X )

where τX : X an → S(X ) is the retraction map corresponding to X and Ω := tropU (V ).
The retraction map τX is defined in such a way (see [BPR13, Lemma 3.4 & Definition
3.7]) that every connected component of X an \S(X ) is retracted to a single point in
S(X ). Due to this fact and the commutativity of the diagram, the form ω = trop∗U ωtrop
is supported on S(X ). Since the restriction of the subharmonic function f to S(X ) is
continuous by [Thu05, Proposition 3.4.6], we get
                              Z           Z
                                  f ∧ω =     (f ◦ τX ) ∧ ω
                                  W                 W
is finite. Hence, f is locally integrable.                                                   
18                                         V. WANNER


Theorem 4.5. Let W be an open subset of X an and f : W → [−∞, ∞) be a subharmonic
function, then f is psh.
Proof. We already know by Proposition 4.4 that f is locally integrable, so it remains
to show that d′ d′′ [f ] is non-negative, which is also a local property by Proposition 3.19.
Since X an is a locally compact Hausdorff space, we can find for every x ∈ W a relatively
compact neighborhood W ′ of x in W . By Proposition 2.8, there is a decreasing net
hfj i of lisse subharmonic functions converging pointwise to f on W ′ . Consider a non-
negative function g ∈ Cc∞ (W ′ ). Then there are smooth forms ω + , ω − ∈ A1,1 (X an ) such
that d′ d′′ g = ω + − ω − and the corresponding signed Radon measures from Proposition
3.13 are non-negative [CD12, Lemme 5.3.3]. By [CD12, Corollaire 3.3.4], we can find a
smooth non-negative function η ∈ Cc∞ (W ′ ) such that η ≡ 1 on supp(g), and hence
                               d′ d′′ g = ηd′ d′′ g = ηω + − ηω −
on W ′ . The smooth (1, 1)-forms ηω ± are contained in Ac1,1 (W ′ ) and the corresponding
RadonRmeasures are still non-negative and have compact support by Proposition 3.13.
Thus, W ′ f ∧ ηω ± is finite (see Proposition 4.4), and we have
                             Z                   Z
                                  f ∧ ηω ± = lim     fj ∧ ηω ±
                               W′                  j   W′
by [BFJ15, Lemma 2.23]. Together, we get
                      Z                  Z             Z
          ′ ′′                    ′ ′′              +
        d d [f ](g) =      f ∧ ηd d g =      f ∧ ηω −      f ∧ ηω −
                        W′                W′            W′
                           Z               Z                   Z
                                       +              −
                    = lim(     fj ∧ ηω −       fj ∧ ηω ) = lim     fj ∧ d′ d′′ g.
                         j   W′                   W′               j   W′
                                     R             ′ ′′
By Proposition 4.3, we know that         W ′ fj ∧ d d g ≥ 0 for every fj in the net, and hence
d′ d′′ [f ](g) ≥ 0.                                                                         

4.2. Continuous subharmonic functions in the sense of Chambert-Loir and
Ducros are subharmonic in the sense of Thuillier. In this subsection, we prove
that every continuous psh function is subharmonic in the sense of Thuillier. The key
tool of the proof is the coincidence of the Monge-Ampère measure and the measure ddc g
for model functions (see Theorem 3.28).
Lemma 4.6. Let W be an open subset of X an and f : W → R be a continuous function.
If f is not subharmonic, then there is a strictly semistable formal model (X , L) of (X, O X )
such that the model function g := − log k1kL satisfies the following properties:
      i) supp(g) is a connected strictly affinoid domain Y ⊂ W ;
     ii) g is strictly positive on Y \∂Y ;
    iii)                                Z
                                               f ddc g < 0.
                                           W
Proof. By Corollary 2.13, thereR is a connected strictly affinoid domain Y and a type II
or III point x in Y \∂Y with W f ddc gxY < 0. Since gxY is lisse, we can find a strictly
semistable formal model Y of Y and a piecewise affine function GYx on the corresponding
skeleton S(Y) such that gxY = GYx ◦τY on Y . Note that S(Y) is a closed connected subset
of X an with the structure of a finite metric graph. By blowing up Y, we may assume
that there is no edge in S(Y) whose endpoints are all contained in the boundary ∂Y . We
will explain in steps, why there is a strictly semistable formal model (X , L) such that
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 19


the corresponding
               R model  function g = − log k1kL on X an satisfies g > 0 on Y \∂Y , g = 0
                     c
elsewhere, and W f dd g < 0.

  0. Step: Strategy of the proof.

   We construct a val(K × )-rational function (see definition below) G on S(Y) with the
required properties
                                                    Z
(4.3)               G|S(Y)\∂Y > 0, G|∂Y = 0 and           f ddc G < 0.
                                                           S(Y)

Then the function g := G ◦ τY is piecewise Q-linear in the sense of [GK15] on Y . Setting
g ≡ 0 on X an \Y , we get a well-defined continuous non-negative function g on X an and
we have a G-covering of X an on which g is piecewise Q-linear. Thus, there is a semistable
                                         1
formal model (X , L) such that g = − m     log k1kL on X an by [GK14, Proposition 8.11&
8.13]. Note that we always may assume X to be strictly semistable by the semistable
reduction Theorem [BL93, Ch. 7] since K is algebraically closed. Then the formal model
(X , L⊗m ) of (X, O X ) gives the claim.
   Before we start with the construction, note that a val(K × )-rational function is a
piecewise affine function on S(Y) (we refine the vertex set such that G is affine on every
edge) such that the following properties are satisfied
   (a) ddc G is only supported on points of type II.
   (b) G has values in val(K × ) at every vertex of S(Y).
   (c) G has rational slopes.


    1. Step: Replace GYx by a piecewise affine function G′ such that (4.3) is still
             satisfied and (a) additionally holds.

   If x is of type II, the support of ddc GYx consists only of type II points. If x is of type III,
we use that the points of type II are dense in X an . Let e = [y1 , y2 ] be the edge of S(Y)
having x in its interior. Let xn be a sequence of type II points in e converging to x with
respect to the skeletal metric. Consider the piecewise affine functions Gn on S(Y) that
are given by the affine function on [y1 , xn ] (resp. on [xn , y2 ]) connecting the points GYx (y1 )
and GYx (xn ) (resp. GYx (xn ) and GYx (y2 )) and Gn ≡ GYx on S(Y)\e. It is easy to see that
the slopes converge to the ones of GYx , i.e. ddc Gn → ddc GYx for n → ∞. Furthermore, f
is continuous, so we can find n Rbig enough such that |f (xn )ddc Gn (xn ) − f (x)ddc GYx (x)|
is so small that we still have S(Y) f ddc Gn < 0 (cf. [Thu05, Proposition 3.3.4]). Set
G′ := Gn for such an n.

    2. Step: Replace G′ by a piecewise affine function G′′ such that (4.3) and (a)
             are still satisfied and (b) additionally holds.
   Due to normalizing the absolute value | |, we assume that Q is contained, and so dense,
in val(K × ). Let z be a vertex of S(Y). If G′ (z) is not in Q and (an )n is a sequence of
rational points converging to G′ (z), then the slopes of the piecewise affine functions G′n
on S(Y) resulting by replacing G′ (z) by an converge to the slopes of G′ . Thus, we can
choose an n ∈ N such that G′′ := G′n still satisfies (4.3) and takes only values in Q at
every vertex of S(Y). We choose these values such that G′′ is still strictly positive on
S(Y)\∂Y .
20                                             V. WANNER

      3. Step: Replace G′′ by a piecewise affine function G such that (4.3), (a) and (b)
               are still satisfied and (c) additionally holds.

    Now, consider an edge e = [y1 , y2 ] of S(Y). Denote by d(y1 , y2 ) the distance between
these two points with respect to the skeletal metric. If d(y1 , y2 ) ∈ Q, we are done. If
not, we can find points y1′ and y2′ of type II in e with distance d(y1′ , y2′ ) ∈ Q arbitrary
close to d(y1 , y2 ). These points are chosen so that we can decompose the edge e into
[y1 , y1′ ] ∪ [y1′ , y2′ ] ∪ [y2′ , y2 ]. Let G be the piecewise affine function on e defined by the
data G ≡ G′′ (y1 ) on [y1 , y1′ ], G ≡ G′′ (y2 ) on [y2′ , y2 ] and G|[y1′ ,y2′ ] is affine (see Figure 1).
Since G(yi′ ) = G′′ (yi ) ∈ Q, the constructed function G on e has rational slopes. Choose
yi′ with d(y1′ , y2′ ) close enough to d(y1 , y2 ) such that (4.3) is still satisfied. Note that this
is possible since f is continuous (cf. [Thu05, Proposition 3.3.4]).
    We do this for all edges except the ones containing the boundary points ∂Y , where
we just move the other vertex. Then the function G on S(Y) has slopes in Q and is
consequently the required function.


                                                    G′′ (y1 )
                                                        |
              G′′ (y1 )
                  |
                                                                                         G′′ (y2 )
                                                                                             |
                          ỹ0                 ỹ1               y1′                y2′
                 •         •                   •       •        •                  •        •
                 y0                                    y1                                   y2
                                  ∈Q                                   ∈Q

                                    ẽ                                   e

                                                FIGURE 1

                                                                                                        
Theorem 4.7. Let W be an open subset of X an and f : W → R be a continuous function.
If f is psh, then f is subharmonic.
Proof. The proof is by contradiction.R We assume that there is a strictly semistable formal
model (X , L) of (X, O X ) such that W f ddc g < 0 for g := − log k1kL as in Lemma 4.6.

     0. Step: Strategy of the proof.

  We know that g = G ◦ τX on X an for the piecewise affine function G = g|S(X ) on
S(X ), the Monge-Ampère measure exists and ddc g = ddc G = MA(g) by Theorem 3.28.
  Assume that we have the following situation: We can write g = g + − g− on an open
subset V of W that contains the connected strictly affinoid domain Y = supp(g) such
that
     (a) g ± is the uniform limit of smooth psh functions gk± on V , i.e. g is globally ap-
         proximable on V ,
     (b) gk := gk+ − gk− ≥ 0 on V , and
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 21


    (c) gk has compact support on V .
Moreover, we want to have a connected open subset V ′ of V with Y ⊂ V ′ , V ′ ⊂ V and
gk ∈ Cc∞ (V ′ ), and a continuous map η on V such that η ≡ 1 on V ′ and η has compact
support in V .
   In this situation, we have ηf ∈ Cc0 (V ), f = ηf on V ′ and by the definition of the
Monge-Ampère measure and Theorem 3.28
                            ddc g = MA(g) = MA(g + ) − MA(g− )
is a measure with finite support contained in Y ⊂ V ′ ⊂ V . Due to our assumption, this
implies
          Z                 Z                 Z                 Z
                                                           +
       0>     f dMA(g) =       ηf dMA(g) =      ηf dMA(g ) −       ηf dMA(g − ).
             W                   V                        V   V
Applying Lemma 3.24 to the right hand side and using gk ∈ Cc (V ′ ), we get
                                                           ∞
                   Z                            Z                           Z
             0>         f dMA(g) = lim              ηf ∧ d′ d′′ gk+ − lim       ηf ∧ d′ d′′ gk−
                    W                   k→∞ V                        k→∞    V
                                                Z
                                                           ′ ′′
                                     = lim          ηf ∧ d d gk
                                        k→∞ V
                                                Z
                                     = lim       f ∧ d′ d′′ gk
                                      k→∞ V ′
                                     = lim d′ d′′ [f |V ′ ](gk ).
                                      k→∞

We know that d′ d′′ [f ] is positive on W , and so it is on V ′ . Thus,
                                        lim d′ d′′ [f |V ′ ](gk ) ≥ 0,
                                       k→∞
and so we have a contradiction. Hence, f has to be subharmonic.
  We explain in several steps how to construct V , V ′ , η and the functions gk+ , gk− such
that one has the described situation.

  1. Step:       Show that the function g is globally approximable on W .
  The curve X is projective, so we may assume X to be projective as well and can
therefore find very ample line bundles L1 , L2 such that L = L1 ⊗ L−1
                                                                   2 . Thus, we can
write
                       g = log k1kL = − log ks1 kL1 + log ks2 kL2
on W for global sections s1 , s2 that coincide on the generic fiber. Since we may work on
every open subset of W containing the compact subset Y by Proposition 3.19, we may
assume that s1 and s2 do not vanish on W . Due to the very ampleness, we can find
closed embeddings ϕi : X → PnRi such that Li ≃ ϕ∗i OPni (1) and si = ϕ∗i xji for i = 1, 2.
                                                            R
Here, let x0 , . . . , xni be the coordinates of PnRi and ji ∈ {0, . . . , ni }. Without loss of
generality, we assume xj1 = xn1 and xj2 = xn2 . These closed embeddings induce closed
embeddings ϕi : X → PnKi into the toric varieties PnKi . Then
  g = − log ks1 kL1 + log ks2 kL2
    = ((ϕan ∗
         1 ) (− log |xn1 | +      max          log |xj |) − (ϕan ∗
                                                              2 ) (− log |xn2 | +      max          log |xj |))
                               j∈{0,...,n1 }                                        j∈{0,...,n2 }

on W . We approximate the functions φi := − log |xni | + maxj∈{0,...,ni } log |xj | for i = 1, 2
                                    ni ,an
by smooth convex functions on {η ∈ PK      | |xni |η 6= 0} as in [CD12, Proposition 6.3.2].
22                                                   V. WANNER


   For every k ∈ N>0 and n ∈ N, there is a smooth, convex function Mn, 1 on Rn+1 that
                                                                       k
is non-decreasing in every variable and has the following properties
       i) max(t0 , . . . , tn ) ≤ Mn, 1 (t0 , . . . , tn ) ≤ max(t0 , . . . , tn ) + k1 ;
                                         k
       ii) If tl + k2 ≤ maxj6=l tj , then Mn, 1 (t0 , . . . , tn ) = Mn−1, 1 (t0 , . . . , tbl , . . . , tn );
                                              k                            k
      iii) For all t ∈ R, we have Mn, 1 (t0 + t, . . . , tn + t) = Mn, 1 (t0 , . . . , tn ) + t.
                                                k                                   k

     Define for k ∈ N>0 and i ∈ {1, 2} the following function
                            φi,k := − log |xni | + Mni , 1 (log |x0 |, . . . , log |xni |)
                                                              k

    ni ,an                            ni ,an
on PK      For every point ζ in {η ∈ PK
           .                                 | |xni |η 6= 0} there is an open neighborhood
of ζ such that φi,k is smooth and psh on this neighborhood. Both are local properties
and si does not vanish on W , so (ϕan ∗
                                   i ) φi,k is a smooth psh function on W (see Remark
3.21) converging uniformly to − log ksi kLi on W . We use in the following the notations
g+ := − log ks1 kL1 and g− := − log ks2 kL2 . Furthermore, we set gk+ := (ϕan  ∗
                                                                            1 ) φ1,k and
gk− := (ϕan ∗
         2 ) φ2,k . Note that we have by construction

                                              g ± ≤ gk± ≤ gk± + 1/k.

     These functions do not necessarily satisfy (b) and (c), so we need to modify gk± .

      2. Step: Construct a suitable V and study the behavior of gk± outside of Y :


   At the end of Step 2, one can find an illustration of the construction in Figure 2. The
boundary of the strictly affinoid domain Y is a finite set of points of type II. By blowing
up our model X , we may assume that the points ∂Y are vertices in S(X ). Note that
we always may assume that an admissible blowing up is strictly semistable again by the
semistable reduction Theorem [BL85, Ch. 7]. Consider a point y ∈ ∂Y . Since y is of type
II, [BPR13, Corollary 4.27 & Theorem 4.11] tells us that there are a strictly semistable
formal model X y of X and a star-shaped open neighborhood Ωy of y in S(X y ) such that
τX−1y (Ωy ) is an open neighborhood of y in W . Here, a star-shaped open neighborhood
Ωy of y in S(X y ) is a simply-connected open neighborhood of y in S(X y ) such that the
intersection of Ωy with any edge e in S(X y ) emanating from y is a half-open interval
Iy,e = [y, xe ) with endpoints y and xe of type II. By blowing up X and modifying Ωy , we
may assume that we can find this star-shaped open neighborhood Ωy in S(X ). We explain
how to do this. The model X has to be blown up such that every vertex of S(X y ) is a
vertex in the new skeleton S(X ). Then we can modify Ωy in the following way. Consider
an edge e of the new skeleton S(X ). Then the interior of e is either contained in an
edge ẽ of S(X y ) or lies in a connected component of X an \S(X y ) isomorphic to an open
ball. In the first case, we shrink Iy,ẽ so that Iy,e is a half-open interval in e. Note that
τX−1 (Iy,e ) = τX−1y (Iy,e ), and so it is still contained in W . In the second case, we just add
a new half-open interval Iy,e to Ωy . Then τX−1 (Iy,e ) ⊂ τX−1y (y) ⊂ W . We do this blowing
ups and modifications for all boundary points. Moreover, we always choose Ωy such that
Ωy ⊂ W . Before we can construct V , we have to blow up X one more time. We find
this admissible formal blowing up X ′ of X such that Y = Y η for a formal open subset Y
of X ′ , which is possible by [BL93, Lemma 4.4]. Then we have Y = τX−1′ (S(X ′ ) ∩ Y ). As
described above, we modify Ωy such that it is a star-shaped open neighborhood of y in
S(X ′ ). Altogether, we have a strictly semistable formal model X ′ of X such that every
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 23


boundary point y of Y has an open neighborhood τX−1′ (Ωy ) in W for an open star-shaped
neighborhood Ωy of y in S(X ′ ) and Y = τX−1′ (S(X ′ ) ∩ Y ).
   For every point z ∈ (S(X ′ ) ∩ Y )\∂Y , we choose some star-shaped open neighborhood
Ωz of z in S(X ′ ) with Ωz ⊂ Y \∂Y . Then τX−1′ (Ωz ) is automatically contained in W due
to Y = τX−1′ (S(X ′ ) ∩ Y ) and Y ⊂ W .
   We have constructed for every point in S(X ′ )∩Y an open neighborhood of it in S(X ′ ),
Ωy for y ∈ ∂Y and Ωz for z ∈    / ∂Y , and so these open subsets clearly cover our compact
subset S(X ′ ) ∩ Y . Thus, there is a finite subset Y0 of S(X ′ ) ∩ Y such that
                                                        [
                             Y = τX−1′ (S(X ′ ) ∩ Y ) ⊂   τX−1′ (Ωz ).
                                                               z∈Y0

By construction, the set of boundary points ∂Y is contained in Y0 . Furthermore, we
choose Y0 minimal, i.e. removing one open subset τX−1′ (Ωz ) from the covering would no
longer cover Y . Set
                                       [
                                 V :=      τX−1′ (Ωz ),
                                                 z∈Y0
then V is an open subset of W containing Y = supp(g).
   Let y be a point in ∂Y , e an edge emanating from y in S(X ′ ) not contained in Y and
Iy,e the corresponding half-open interval in the star-shaped open neighborhood Ωy . Note
that g|e = 0. We may shrink the half-open interval Iy,e in e, and so Ωy and V , such that
        g + = (ϕan ∗
                1 ) (− log |xn1 | +       max          log |xj |) = (ϕan ∗
                                                                      1 ) (− log |xn1 | + log |xl1 |)
                                       j∈{0,...,n1 }

        g − = (ϕan ∗
                2 ) (− log |xn2 | +       max          log |xj | = (ϕan ∗
                                                                     2 ) (− log |xn2 | + log |xl2 |))
                                       j∈{0,...,n2 }

on Iy,e for some li ∈ {0, . . . , ni }. Define the map Ni,max : Iy,e → N as follows
            Ni,max (η) := |{j ∈ {0, . . . , ni }|(ϕan ∗                an ∗
                                                   i ) (log |xj |) = (ϕi ) (log |xli |)}|.

Shrink Iy,e again such that (ϕan   ∗
                                i ) (log |xj |) is affine on Iy,e for every j ∈ {0, . . . , ni }. Con-
sequently, the function Ni,max is constant on Iy,e \{y} as (ϕan       ∗                         an ∗
                                                                  i ) (log |xli |) = max(ϕi ) (log |xj |)
on Iy,e . Hence, we write Ni,max for this constant value.
   Define
                                                       2
          Ωi,k :={η ∈ Iy,e | (ϕan  ∗
                               i ) (log |xj |)(η) +      < (ϕan   ∗
                                                              i ) (log |xli |)(η)
                                                       k
                   if (ϕan  ∗                      an ∗
                        i ) (log |xj |)|Iy,e 6= (ϕi ) (log |xli |)|Iy,e , j ∈ {0, . . . , ni }}

Let N ′ ∈ N such that Ωk := (Ω1,k ∩ Ω2,k )\{y} is a non-empty connected open subset
of Iy,e for every k ≥ N ′ . We have Ωk ⊂ Ωk+1 , and we work in the following with
Ωy,e := ΩN ′ . Then we get for every k ≥ N ′ using properties i)-iii) that
(4.4)    gk+ = (ϕan ∗                            an ∗                       an ∗
                 1 ) (− log |xn1 |) + Mn1 , 1 ((ϕ1 ) (log |x0 |), . . . , (ϕ1 ) (log |xn1 |))
                                                 k

            = (ϕan ∗                                  an ∗                        an ∗
                1 ) (− log |xn1 |) + MN1,max −1, 1 ((ϕ1 ) (log |xl1 |), . . . , (ϕ1 ) (log |xl1 |))
                                                           k

            = (ϕan ∗                   an ∗
                1 ) (− log |xn1 |) + (ϕ1 ) (log |xl1 |) + MN1,max −1, 1 (0, . . . , 0)
                                                                                k
                 +
            = g + MN1,max −1, 1 (0, . . . , 0)
                                   k

on Ωy,e . Set Ck+ := MN1,max −1, 1 (0, . . . , 0) ∈ [0, k1 ]. Analogously,
                                 k

(4.5)                           gk− = g− + MN2,max −1, 1 (0, . . . , 0)
                                                                k
24                                                   V. WANNER


on Ωy,e . Set Ck− := MN2,max −1, 1 (0, . . . , 0) ∈ [0, k1 ]. Due to g = g+ − g − = 0 on Ωy,e , we
                                 k
have
                      gk+ − gk− = MN1,max −1, 1 (0, . . . , 0) − MN2,max −1, 1 (0, . . . , 0)
                                                 k                             k

on Ωy,e .



                                                                                gk+
                                                                                gk−
                                                                                       g+ = g−




            •                      •[
                                   y                                                  xe
                S(X ′ ) ∩ Y                                Ωy,e

     W                                                     Iy,e


                                                      FIGURE 2


 3. Step: Modify the constructed functions gk± on the open subset V ⊂ W
          such that (b) and (c) are satisfied.

   We start with (b). To ensure that the difference gk+ − gk− = (ϕan  ∗         an ∗
                                                                   1 ) φ1,k − (ϕ2 ) φ2,k is
non-negative on V , we work with gk+ := (ϕan ∗       1                   an ∗
                                          1 ) φ1,k + k on V instead of (ϕ1 ) φ1,k , which is
                                                                         +
still a smooth psh function on V converging uniformly to the function g = − log ks1 kL1 ,
and
                       1                               1
          (ϕan ∗
            1 ) φ1,k +   − (ϕan  ∗         an ∗
                              2 ) φ2,k ≥ (ϕ1 ) φ1,k +    − g+ + g − − (ϕan  ∗
                                                                         2 ) φ2,k
                       k                               k
                                             1 1
                                       ≥0+ − =0
                                             k k
on V . Note that we have used g = g + − g− ≥ 0 on V and property i) of Mni ,k .
   Next, we deal with (c), i.e. we modify gk+ and gk− such that gk := gk+ − gk− has compact
support on V . As in Step 2, let y be a boundary point of Y , Ωy a star-shaped open
neighborhood of y and Iy,e = [y, xe ) be a half-open interval of Ωy contained in an edge e
of S(X ′ ) emanating from y and pointing outwards of Y . Recall that we have constructed
in the second step the open subset Ωy,e of Iy,e . Here, we start with the construction
of an affine function on the closed annulus A := τX−1′ ([y, xe ]) whose graph intersects the
graphs of all our functions gk± on Ωy,e for k big enough. The annulus A is isomorphic to
a closed annulus A′ := S(a, b) = trop−1 ([val(b), val(a)]) in G1,an                     ×
                                                                  m for some a, b ∈ K with
                                                 ∼     ′
|a| < |b| and trop := − log |T |. Let Φy,e : A − → A be an isomorphism. For simplicity, we
may assume that val(b) = 0. Then we can identify Iy,e = [y, xe ) with the real half-open
                                                                              ′ ∈Ω
interval [0, val(a)) via tropy,e := − log |T | ◦ Φy,e . Choose points ζy,e , ζy,e  y,e ⊂ e, and
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 25


m ∈ N, c ∈ R such that the function

                              ψy,e : Iy,e → R; ζ 7→ m · tropy,e (ζ) + c

satisfies

            ψy,e (ζy,e ) = ((ϕan ∗                   an ∗                          +
                              1 ) (− log |xn1 |) + (ϕ1 ) (− log |xl1 |))(ζy,e ) = g (ζy,e ),

           ′ ) = g + (ζ ′ ). Recall that N ′ was fixed in Step 2 to define Ω . Since g ±
and ψy,e (ζy,e    N ′ y,e                                                   y,e       k
converges uniformly to g+ = g − on Ωy,e , there is an N ′′ ≥ N ′ such that

                             sup (gk± − g ± ) = sup |gk± − g± | ≤ CN
                                                                   +
                                                                     ′
                            x∈Ωy,e                   x∈Ωy,e

                                        +       ± = C + + 1/N ′ , and hence
for every k ≥ N ′′ . By (4.4), we have gN ′ − g      N′

                               gk± − gN
                                      +      ±
                                        ′ = gk − g
                                                   ±         +
                                                     + g± − gN ′ < 0


on Ωy,e for every k ≥ N ′′ . Thus, for every k ≥ N ′′ there is a point ζk+ in Ωy,e such that
ψy,e (ζk+ ) = gk+ (ζk+ ). Due to g + = g− ≤ gk− ≤ gk+ by (4.5) and construction, there is also
for every k ≥ N ′′ a point ζk− in Ωy,e such that ψy,e (ζk− ) = gk− (ζk− ). Recall that g− = g+
and gk+ and gk− with k ≥ N ′ are affine on Ωy,e .
   We choose ε such that

                           Ωy,e,< := {ζ ∈ Ωy,e | ψy,e (ζ) + 2ε < g+ (ζ)}
                           Ωy,e,> := {ζ ∈ Ωy,e | ψy,e (ζ) > g+ (ζ) + 2ε}

are non-empty open subsets of Ωy,e , and we set Γy,e := Ωy,e \(Ωy,e,< ∪ Ωy,e,> ).
   In the following, we smoothen the piecewise affine functions max(gk± , ψy,e ) in a proper
way. One can construct a smooth symmetric convex 1-Lipschitz continuous function
θε : R → (0, ∞) such that θε (a) = |a| if |a| ≥ ε. We set
                                                    a + b + θε (a − b)
(4.6)                                mε (a, b) :=                      .
                                                            2
  Then the smooth function mε : R2 → R satisfies the following properties:
      i) mε is convex;
     ii) max(a, b) ≤ mε (a, b) ≤ max(a, b) + 2ε ;
    iii) mε (a, b) = max(a, b) whenever |a − b| ≥ ε;
    iv) mε is increasing in every variable.
We define the functions

                                          gek+ := mε (gk+ , ψy,e ),
                                           gek− := mε (gk− , ψy,e )

on Ωy,e . Then e gk+ (resp. gek− ) coincides with gk+ (resp. with gk− ) on Ωy,e,< for every
k ≥ N since g = g− ≤ gk− ≤ gk+ on Iy,e by (4.5) and by construction. The functions
       ′′       +

gk+ converge uniformly to g − = g+ , so we can choose Ny,e ≥ N ′′ such that for all k ≥ Ny,e ,
we have g + + ε ≥ gk+ ≥ gk− on Ωy,e . Then gek+ and gek− coincide with ψy,e on Ωy,e,> for all
                 gk+ − gek− = 0 on Ωy,e,> for every k ≥ Ny,e . We do this for every y ∈ ∂Y
k ≥ Ny,e . Thus, e
and for every edge e in S(X ′ ) emanating from y and pointing outwards of Y .
26                                              V. WANNER


                                                                                 ψy,e




                                                                           +
                                                                          gN  ′

                                                                          gk+
                                                                          gk− g+ = g−
                        g+ + ε
               max(gk± , ψy,e )


                                                     ζy,e
          •                       •[            [     •      ]
                                                      Γy,e
                                  y                                          xe
              S(X ′ ) ∩ Y              Ωy,e,<                    Ωy,e,>
                                                     Ωy,e
      W                                               Iy,e

                                             FIGURE 3
                                                   S
   Recall that we work on the open subset V = z∈Y0 τX−1′ (Ωz ) of W containing Y , where
Ωz is a star-shaped open neighborhood of z in S(X ′ ) and Iz,e = Ωz ∩ e for every edge
e in S(X ′ ) emanating from z. We have ∂Y ⊂ Y0 and the sets Ωy \Y with y ∈ ∂Y are
disjoint of all other star-shaped open neighborhoods Ωz . We write Sy for the set of edges
e in S(X ′ ) emanating from y and pointing outwards of Y . Then for every y ∈ ∂Y and
e ∈ Sy , we have constructed the open subset ΩS     y,e of Iy,e = [y, xe ) ⊂ Ωy .
   Let VY be the connected component of V \( y∈∂Y ;e∈Sy Γy,e ) containing Y and Ve be
the connected component of V \Γy,e containing xe . Note that by the construction of V
all connected components Ve are pairwise disjoint. We can extend gek± to a continuous
function on V by
                                
                                      ±                       −1
                                mε (gk , ψy,e ◦ τX ′ ) on τX ′ (Ωy,e ),
                         gek± := gk±                      on VY ,
                                
                                
                                 ψy,e ◦ τX ′              on Ve .

  Then the functions gek+ − gek− are non-negative and continuous on V with compact
support for every k ≥ maxy,e Ny,e . Recall that by property iv), mε is increasing in every
variable. From now on we only consider k ∈ N with k ≥ maxy∈∂Y,e∈Sy Ny,e .

                                                gk+ (resp. gek− ) converge uniformly to a function
      4. Step: Show that the modified functions e
               e+         −                g − ge− on V .
               g (resp. ge ) such that g = e+


     Define the following functions on V
                                
                                       ±
                                mε (g , ψy,e ◦ τX ′ )       on τX−1′ (Ωy,e ),
                         ge± := g±                           on VY ,
                                
                                
                                  ψy,e ◦ τX ′                on Ve .
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 27


  By construction, these functions are well-defined and continuous. Since g = g + − g−
on V with g = g + − g− = 0 on V \Y , we clearly have g = ge+ − e    g− on V .
                           +         −
  Next, we show that e   gk (resp. gek ) converge uniformly to ge (resp. to ge− ) on V . We
                                                                 +

                                                                                           gk− )
                                                                                gk+ (resp. e
know that gk+ (resp. gk− ) converge uniformly to g + (resp. to g− ) on V , thus e
                           +             −                  ±                      ±
converge uniformly to g (resp. to g ) on VY . Since gek = ψy,e ◦ τX ′ = e        g on Ve , it
                                          −1                        −1
remains to consider the open subset τX ′ (Ωy,e ). For every x ∈ τX ′ (Ωy,e ), we have
 gk± (x) − ge± (x)| = mε (gk± (x), ψy,e (τX ′ (x)) − mε (g± (x), ψy,e (τX ′ (x)))
|e
                       gk± (x) − g ± (x) + θε (gk± (x) − ψy,e (τX ′ (x))) − θε (g± (x) − ψy,e (τX ′ (x)))
                   =
                                                               2
                       gk± (x) − g ± (x)   g± (x) − g ± (x)
                   ≤                     + k
                               2                  2
                   ≤ |gk± (x) − g ± (x)|
where we used that θε is 1-Lipschitz continuous to get the inequality. Due to the uniform
convergence of gk± to g± on V , which contains τX−1′ (Ωy,e ), we get
                               lim      sup            gk± (x) − e
                                                      |e         g ± (x)| = 0.
                              k→∞ x∈τ −1 (Ω
                                       X′     y,e )


  5. Step: Show that the modified functions gek+ and e
                                                     gk− are smooth and psh on V .


  Note that both properties are local. We already know that gk± ∈ C ∞ (VY ), so it
remains to find for every point x in τX−1′ (Ωy,e ) ∪ Ve an open neighborhood Vx in V such
that gek± is smooth and psh on Vx .
  We start with a point x ∈ Ve . Choose an open neighborhood Vx of x in the open
subset Ve ⊂ V , then gek± is given by ψy,e ◦ τX ′ on Vx . For every ζ ∈ Vx ⊂ A, we have
            gek± (ζ) = (ψy,e ◦ τX ′ )(ζ) = (ψy,e ◦ τA )(ζ) = Φ∗y,e (−m · log |T | + c)(ζ)
on Vx . We first show
                   −m · log |T | + c ∈ ker(d′ d′′ : C ∞ (G1,an   1,1 1,an
                                                          m ) → A (Gm )).

Consider the tropical chart (V, ϕU ) = (G1,an                  1,an
                                               m , id) of Gm . Then tropU = log |T |, and
                                                    1,an
so −m · log |T | can be written as the triple (Gm , id, λ), where λ : R → R is the affine
                                                                               1,an
function t 7→ mt + c. Thus, −m · log |T | + c is a smooth function on Gm            (cf. Definition
                                                                                    1,an
3.11). The (1, 1) form d d (−m · log |T | + c) is given by the triple (Gm , id, d′ d′′ λ).
                              ′ ′′

Since λ is affine, the form d′ d′′ λ is zero, and so is d′ d′′ (−m · log |T | + c). Consequently,
−m · log |T | + c ∈ ker(d′ d′′ : C ∞ (G1,an         1,1    1,an
                                         m ) → A (Gm )). This implies that e              gk± |Vx =
Φ∗y,e (−m · log |T | + c) is a smooth psh function on Vx (see Remark 3.21).
   Now, consider x ∈ τX−1′ (Ωy,e ). We have just seen that ψy,e ◦ τX ′ is a smooth psh
function on τX−1′ ((y, xe )). Using Proposition 3.20, there is a chart (Vx , ϕUx ) with x ∈
Vx ⊂ τX−1′ ((y, xe )) such that ψy,e ◦ τX ′ = φ ◦ tropUx on Vx for a smooth function φ on
Rr that is convex restricted to every polyhedron contained in tropUx (Vx ). On the other
hand, we know that the function gk± is smooth and psh on τX−1′ ((y, xe )) as well. Hence,
there is also a chart (Vx′ , ϕUx′ ) with x ∈ Vx′ ⊂ τX−1′ ((y, xe )) such that gk± = φ′ ◦ tropUx′
                                            ′
on Vx′ for a smooth function φ′ on Rr that is convex restricted to every polyhedron
contained in tropUx′ (Vx′ ). Working on the intersection (Vx ∩ Vx′ , ϕUx × ϕUx′ ), which is a
28                                         V. WANNER


subchart of both [Gub16, Proposition 4.16], we get
                           ψy,e ◦ τX ′ = (φ ◦ Trop(π)) ◦ tropUx ∩Ux′
                                  gk± = (φ′ ◦ Trop(π ′ )) ◦ tropUx ∩Ux′
for the corresponding transition functions π, π ′ satisfying ϕUx = π ◦ (ϕUx × ϕUx′ ) and
ϕUx′ = π ′ ◦ (ϕUx × ϕUx′ ). Since Trop(π) and Trop(π ′ ) are integral affine functions on
     ′                                                                                     ′
Rr+r , the composition φ◦Trop(π) (resp. φ′ ◦Trop(π ′ )) is still a smooth function on Rr+r
with a convex restriction to every polyhedron. Thus, mε (φ ◦ Trop(π), φ′ ◦ Trop(π ′ )) is a
                           ′
smooth function on Rr+r , and the properties i) and iv) of mε imply that the restriction
to every polyhedron is convex since the restriction of φ ◦ Trop(π) and φ′ ◦ Trop(π ′ ) are.
We have
          gk± = mε (gk± , ψy,e ◦ τX ′ ) = mε (φ ◦ Trop(π), φ′ ◦ Trop(π ′ )) ◦ tropUx ∩Ux′
          e
on Vx ∩ Vx′ for every x ∈ τX−1′ (Ωy,e ), so gek± is a smooth psh function on τX−1′ (Ωy,e ) by
Proposition 3.20, which proves Step 5.
  Altogether, egk± are smooth psh function on V . We set
                                         gk := gek+ − gek− ,
                                         e
then the functions e
                   gk satisfy by construction all the required properties in Step 0.

     6. Step: Construction of V ′ and η.

   By the construction of V and e  gk , it is no problem to construct the required set V ′ ,
                       ′
i.e. an open subset V of V containing Y such that V ′ ⊂ V and e        gk ∈ Cc∞ (V ′ ). Fur-
thermore, let V ′′ be an open neighborhood of V ′ in V with V ′′ ⊂ V . The topological
space X an is a compact Hausdorff space. Urysohn’s Lemma states the existence of a
continuous function η : X an → [0, 1] with η ≡ 1 on V ′ and η ≡ 0 on X an \V ′′ . Thus, η
has compact support in V , i.e. it is the required function in Step 0.

  Thus, we have constructed everything as it was described in Step 0 proving the theo-
rem.                                                                                
Corollary 4.8. Let f : W → R be a continuous function. Then f is subharmonic if and
only if f is psh.
Proof. Follows directly from Theorem 4.5 and Theorem 4.7.                                   

```

## van-der-Put, newline lines 1--230

```text
A NNALES DE L’ INSTITUT F OURIER




 M ARIUS VAN D ER P UT
 The class group of a one-dimensional affinoid space
 Annales de l’institut Fourier, tome 30, no 4 (1980), p. 155-164
 <http://www.numdam.org/item?id=AIF_1980__30_4_155_0>




    © Annales de l’institut Fourier, 1980, tous droits réservés.
    L’accès aux archives de la revue « Annales de l’institut Fourier »
    (http://annalif.ujf-grenoble.fr/) implique l’accord avec les conditions gé-
    nérales d’utilisation (http://www.numdam.org/conditions). Toute utilisa-
    tion commerciale ou impression systématique est constitutive d’une in-
    fraction pénale. Toute copie ou impression de ce fichier doit conte-
    nir la présente mention de copyright.




                  Article numérisé dans le cadre du programme
                Numérisation de documents anciens mathématiques
                              http://www.numdam.org/
Ann. Inst. Fourier, Grenoble
30, 4 (1980), 155-164.




                THE CLASS GROUP
      OF A ONE-DIMENSIONAL AFFINOID SPACE

                           by Marius van der PUT


                                Introduction.

    The field k is supposed to be complete with respect to a non-
archimedean valuation. Moreover we will assume that k is algebraically
closed. An afflnoid space Y over k is the set of maximal ideals of an
affmoid algebra. The standard affinoid algebra is fc<T^,...,T^>= the
set of all power series SflaT^ • • • T^ converging on the closed polydisk
                          {(^....rJe^alllr.Kl}.

An affinoid algebra is a residue class ring of some fc<Ti,.. .,T^>. An
algebraic variety over k can be studied locally by its analytic structure over
k, that is by means of afflnoid spaces.
    We show that a one-dimensional, normal, connected afflnoid space Y is
an afflnoid subset ofa non-singular, complete curve C over k (Thm 1.1). If
Y has a trivial classgroup then Y is in fact an afflnoid subset of P1
(Thm 2.1). A curve is locally a unique factorization domain (U.F.D.
for short) if and only the curve is a Mumford curve (i.e. can be
parametrized by a Schottky group). In general the class group of Y
can be expressed in terms of the Jacobi-variety of C (prop. 3.1).
    Some examples show the connection between the class group of Y and
the class group of the (stable) reduction of Y. For fc-analytic spaces we refer
to
    [2], [3]. I thank A. Escassut for bringing the problem on unique
factorization on afflnoid spaces to my attention. Related questions are treated
in [1].

                 1. Affinoid subspaces of an algebraic curve.

     A curve C (non-singular and complete) over k has a natural structure as
(rigid) analytic space over k. This structure is given by a collection
156                       MARIUS VAN DER PUT


of subspaces Y of C, called affmoid, and a sheaf 0 = (9^ with
respect to the Grothendieck topology of finite coverings by afflnoids.
For any Y, ^P(Y) is an affinoid algebra (1-dim. and normal) over k
with Sp((P(Y)) = Y. We want to show :

   1.1. — THEOREM. — Every 1-dimensional, normal, connected affinoid space
Y = sp(A) is an affinoid subspace of a non-singular complete curve.

     Proof. — Y is called connected and normal if the algebra A has no
idempotents ^ 0, 1 and A is integrally closed. We use the notations
A° = {/eA| 11/H <!}, A00 = {/eA| ||/||<1} and A = A7A00, where
11/11 = max {\f(y)\ \y e Y} is the spectral norm on Y. The algebra A is of
finite type over k = the residue field of k and the algebraic variety
Yc = Max (A) is called the canonical reduction of Y. There is a natural
surjective map R : Y -> Y^, also called the canonical reduction. A pure
covering of an analytic space X, is an allowed covering ^ = (U^) by
affinoid spaces, such that for every i + j with U, n U, ^ 0, the set
U; n \Jj is the inverse image of a Zariski open set V^ in (U^ under the
map U, -> (U^. The reduction X^ of X with respect to ^ is
obtained by glueing the afflne algebraic varieties (U^ over the open
sets V^.. The result is an algebraic variety over k. If X is separated
then the U^ n Uj are also affinoid, the V^ are afflne and equal to
(U^oU), and X^ is separated. If X is non-singular, 1-dimensional,
connected and if X^ is complete then X is a non-singular complete
curve over k (see [2] ch. IV 2.2).
    Our proof consists of glueing affinoid spaces Y i , . . . , Y , to Y
such that the reduction of X = Y u Y^ u . . . u Y, with respect
to the pure covering {Y,Yi,...,Yj is complete. Then clearly Y is
an affinoid domain of the algebraic curve X. The 1-dimensional
space Yc lies in a complete 1-dimensional Z such that F = Z - Y^
is a finite set of non-singular points. Suppose that we can find for
every p e F an affinoid space Yp with canonical reduction
Rp : Yp -> (Yp)^ <= Z where (Y^ is a neighbourhood of p and
such that
             Y, ^ R;1^ n Y,) ^ R-^Y;), n Y,) c Y.

   Then we can glue Yp to Y. The space X = YU u Yp has reduction Z
which is complete. So the glueing has to be done locally on Y and Y^. The
component C of Z on which p lies can be projected into P^k) such that
         THE CLASS GROUP OF A ONE-DIMENSIONAL AFFINOID SPACE              157


 (the image of) p is still non-singular. A good projection onto P1 maps p
 onto o and o is an unramified point for the projection. Replacing Y and
 Y^ by neighbourhoods of p we may therefore suppose :

                     W) = d)(^) = feEr.Mrr^JAP),
 where

     1) e(t) = (t-a,) . . . (t-a,) with ^, .. .,^ different points of ^ ;they
 are the residues of ^4, . . . , a, e fe°.
     2) P is a monic irreducible polynomial of degree n with coefficients in
 ~k[f}.
    . dP
     ' d~~ ls mvertlble as Cement of H[_t,(e(t))~1,5]/(P).
    4) the point « p » corresponds to t = 0.
 Then ^(Y)° has the form fe°<T,U,S>/(TE(T)U-l,Q) where

              E(T) = ( T - a i ) ; . . (T-a,)   and     Q = P.

Since Q is general with respect to the variable S, we can apply Weierstrass-
division and assume that Q is a monic polynomial of degree n in S with
coefficients in fe°<T,U>/(TE(T)U-l). Suppose that we can find a monic
polynomial Q* of degree n in S and coefficients in fe°<T,V>/(E(T)V-l)
such that
                   fe°<T,U,S>/(TE(T)U-l,Q*) ^ ^(Y)°.

Then Y^ = Sp(fe<T,V,S>/(E(T)V-l,Q*)) has the required properties. So we
have to get rid of the negative powers of T in the coefficients of

                    C^S^^S"-^ ... +^.


    1.2. - LEMMA. - If Q* = S" + a;-^-1 ^ . . . + a? ^5
coefficients in A = fe°<T,U>/(TE(T)U-l) ^ Q* = Q = p, then
   a) Q* i5 irreducible
   b) Q* /ia5 a z^ro in ^(Y)°
   c) fe<T,U,S>/(TE(T)U-l,Q*) ^ (P(Y).

    Proo/ - a) Let Q* be reducible over the quotient field of A.
Since A is normal, Q* is a product of monic polynomials with
coefficients in A. This contradicts the irreducibility of Q* = P.
158                       MARIUS VAN DER PUT


                             f      ^Q*1
   b) First we show that \Q*,——^ generates the unit ideal in A[S]. Let
                          I   rfS J
                                          dQ*
m be a maximal ideal containing Q* and ——. If m n k° ^ 0 then m
                                           dS
induces a maximal ideal of H^t,(te(t))~^][S] = A[S] containing P and
dP
—. This contradicts our assumptions on P. So m corresponds to a
aS
maximal ideal m^, of fe<T,U>/(TE(T)U-l)[S], containing Q* and
dQ*
~dS~'
   If mi nk<T,U>/(TE(T)U-l) + 0 then m^, is the kernel of a
homomorphism in k given by T i—> ^ e k, S i—> ^ 6 k with

                  |?4|^ 1,          P4E(5iO|= 1,     |^1 < 1

                                 / dP\
since Q*^) = 0. Ffom              P.— = ^[^(^(O'^S] it follows that
                                 \ »S/
                                 dO*
                   Z,(S)Q alt +Z,(S)-^=l + S ^S1
                                  "^       i>o

for certain Z^, Z2 e A[S] and ^ 6 A with ||flf|| < 1. The substitution
T i—^ ^ i ; S i—> ^2 makes 0 = 1 + ^ ^Ai)^2» which is impossible. So
                                   i>o
m and m^ correspond to an ideal of L[S] with L the quotient field of A.
                                              dQ*
Since Q* is irreducible, this means that —— = 0. This is obviously in
                                         dS
contradiction with (P,—) = K[^?(0)~1].
                   \ ^S/
      We conclude the existence of Z^, Z^ e A[S] with

                                                   dQ*
                        1 =Z,(S)Q*+Z2(S)——.
                                         aS

    By Newton's method we will show that Q* has a zero in ^(Y)°. Let
T| e ^(Y)° satisfy IIQ^rOII < 1 (e.g. TI is the residue of S mod Q in
                                                dO*
W).         Then       1 - Z,(Ti)Q*(ri) = Z^) -^ (TI)       and  since
                                                 aS
        THE CLASS GROUP OF A ONE-DIMENSIONAL AFFINOID SPACE                    159


                                               dO*
l|Zi(ri)Q*(il)|| < 1   it   follows    that    ——(r|)      is   invertible.   Put
                                               aS
               /d0*   \~1
Th = TI - Q*(^)(-^-(Ti)t . Then ||Q*(Tii)|| < ||Q*(Ti)||2. The usual

procedure and the completeness of (P(Y)0 show the existence of a root of Q*
in (P(Y)°.
    c) The quotient field of A[S]/Q* is contained in that of A[S]/Q,
because of (b). Both fields are extensions of degree n of the quotient field
of A. So they are equal. The rings fe<T,U,S>/(TE(T)U-l,Q*) and ^P(Y)
are both the integral closure of k<T,U>/(TE(T)U-l) in that field. So they
are equal.

  End of the proof of 1.1. — We choose Q* with coefficients in
k°<T,V>/(VE(T)-l) and Q* = P.

   1.3. — COROLLARY. — Let Y be as in (1.1); then Y is affinoid in a curve X
(complete non-singular} such that X — Y^. is a finite set of non-singular points.

                            2. Unique factorization.

    We want to show the following :

   2.1. — THEOREM. — Let Y = Sp A be a 1-dimensional connected affinoid
```

## Berkovich, newline lines 1350--1444

```text
through the strictly affinoid domains in X, are compatible on intersections, and to they
glue together to form a sheaf of rings (9^ on the G-topological space Xo. The locally
G-ringed space (Xo, (P^) satisfies the conditions of Definition 9.3.1/4 from [BGR],
and so we get a rigid ^-analytic space. We remark that the rigid yfe-analytic space cons-
tructed is quasiseparated. (A rigid A-analytic space is called quasiseparated if the inter-
section of two open affinoid domains is a finite union of open affinoid domains.)

       1.6.1. Theorem. —The correspondence X i-> XQ is a fully faithful junctor from the
category of Hausdorff strictly k-analytic spaces to the category of quasiseparated rigid k-andlytic
36
                                    VLADIMIR G. BERKOVICH

spaces. Furthermore, this functor induces an equivalence between, the category of paracompact strictly
k'analytic spaces and the category of quasiseparated rigid k-analytic spaces that have an admissible
affinoid covering of finite type.

      A collection of subsets of a set is said to be of finite type if each subset of the col-
lection meets only a finite number of other subsets of the collection.

      Proof. — Let X be a Hausdorff strictly A-analytic space. First of all we establish
the following fact.

      1.6.2. Lemma. — (i) Any open affinoid domain in the rigid k-analytic space XQ is of the
formVo, where V is a strictly affinoid domain in X.
      (ii) Let {VJ^ be a system of strictly affinoid domains in X. Then { V , o } ^ i is
 an admissible covering of XQ if and only if each point ofX has a neighborhood of the form
 V^ U ... uV^ (i.e., { V J ^ i is a quasinet on X).

       Proof. — (i) An open affinoid domain in XQ is an open immersion of rigid ^-analytic
spaces/: Uo -> XQ, where U is a strictly ^-affinoid space. In particular, for any strictly
affinoid domain V C X , /-^(Vo) is a finite union of affinoid domains in UQ, and
{/"^(Vo)}, where V runs through strictly affinoid domains in X, is an affinoid covering.
It follows that we can find strictly affinoid domains Ui, ..., U^ C U and V\, ..., V C X
such that U = Ui U ... u U^ and f\^ ^ comes from a morphism of strictly affinoid
spaces 9,: U, ->V, that identifies U, with an affinoid domain in V,. Moreover, all 9,
are compatible on intersections. Therefore, we get a morphism of strictly ^-analytic
spaces <p : U -> X. Since 9, as a map of topological spaces, is compact and induces an
injection on the everywhere dense subset Uo C U, it follows that 9 induces a homeo-
morphism of U with its image in X. Finally, 9 identifies U, with a strictly affinoid
domain in V,, and therefore 9 identifies U with a strictly analytic domain in X. It is
clear that this is a strictly affinoid domain.
       (ii) Suppose first that {V, o h e i ls an admissible covering of XQ. This means
that, for any strictly affinoid domain V C X, { V, o n V^ }, ^; is an admissible covering
of Vo. It follows that V is contained in a finite union V^ U .. . U V^, and therefore
each point of X has a neighborhood of the required form. Conversely, assume that
the latter property is true. Then any strictly affinoid domain is contained in a finite
union V^ U . .. u V^, and therefore { V, ^ n VQ }^ j is an admissible covering of Vo. •
       Let 9 : Y -> X be a morphism of strictly A-analytic spaces. First of all we claim
that the induced map 90 : Yg -> XQ is continuous with respect to the G-topologies on XQ
and Yo. Let ^C XQ be an admissible open subset, and let VC Y be a strictly affinoid
domain. By [BGR], 9.1.4/2, and Lemma 1.6.2 (i), the set ^ has an admissible cove-
ring { U ^ p J ^ j , where U^ are strictly affinoid domains in X. By Corollary 1.2.14,
for each i e I one has 9-1(U,) n V = U,gj. V^., where V,, are strictly affinoid domains
in V and J, is finite. We get a covering { V,, o } of the set 9o'lW ^ VQ. To verify that
            fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                             37

the latter set is admissible open in VQ, it suffices to show that for any morphism of
strictly ^-affinoid spaces + : W —Vwith^(Wo) C 9o-l(^) n Vg, the covering { ^ '(V,, o)}
has a finite affinoid covering that refines it. But this follows from the fact that the latter
condition is satisfied by the covering {(9^)0" ^U^o h e r Thus, the set 9o~l(<%^) is admis-
sible open in Yo. In the same way one shows that the preimage of an admissible covering
of an admissible open set is an admissible open covering. Hence the map of G-topological
spaces 90 : Y^ -> X^ is continuous. That 9 induces a morphism of locally G-rmged
spaces easily follows from this.
       Let now/: Y() -> X^ be a morphism between the above rigid ^-analytic spaces.
We have to show that it comes from a unique morphism of strictly ^-analytic spaces
9 : Y -> X. First of all, from Proposition 1.3.2 it follows that it suffices to verify the
required fact only in the case when Y is strictly ^-affinoid. For this we remark that the
system { Uo}, where U runs through strictly affinoid domains in X, is an admissible
covering of X^. Therefore {/"^(Uo)} is an admissible covering of Yg by admissible open
subsets. By [BGR], 9.1.4/2, the latter covering has a finite affinoid covering that refines
it. In this way we get strictly affinoid domains V,, . . . , V ^ C Y and Ui, ..., U^C X
such that YQ = V^o U . . . u V^ (and therefore Y = V^ u . . . u VJ and/(V^) C U,^.
The induced morphisms of strictly affinoid spaces V, -> U, are obviously compatible
on intersections, and therefore we get a morphism of strictly yfe-analytic spaces 9 : Y -> X.
It is easy to see that 90 ==/and that 9 is a unique morphism satisfying this property.
       If X is a paracompact strictly A-analytic space, then it has a strictly A-affinoid
atlas with a locally finite net, and therefore the rigid ^-analytic space X^ has an admis-
sible affinoid covering of finite type. It is also evident that it is quasiseparated. Conversely,
let °K be a quasiseparated rigid ^-analytic space that has an admissible affinoid cove-
^g { ^ } i e i of finite tyP0- First of ^ let ^ = L^o, where the U, are strictly
A-affinoid spaces. Since 3E is quasiseparated, for any pair i,j e I the intersection ^ n %.
is a finite union of open affinoid domains in SK\ Thus, there are strictly special domains
U,, C U, and U^ C U, that correspond to ^ n ^, under the identifications ^ == U, p
and ^. = U, o. Let ^ denote the induced isomorphism U ^ ^ U ^ . It is clear that
v
  ii = U? ^(U, n UJ = U,, n U,^ and ^ == v^ o v,, on U^. n U^. By Proposi-
tion 1.3.3, we can glue all U, along U,, and get a paracompact strictly ^-analytic
space X. It is easy to see that XQ is isomorphic to S\ •
       Let X be a Hausdorff strictly A-analytic space. From Lemma 1.6.2 it follows
that there is an isomorphism of topoi X^ ^ X^. In particular, there is a morphism of
topoi (7^,71;*) : X^ -^X^ such that the functor TC* is fully faithful (and TC, is not).
Furthermore, from Proposition 1.3.6 it follows that if F is an abelian sheaf on X, then
H^X, F) ^> H^Xo, TT* F), q ^ 0, and if X is good and F is a coherent 0^ module, then
H^(X,F)^IP(Xo,Fo), q ^ O , where F o = = ^ F ® ^ ^ ^ o - Finally, there are equi-
```

## Thuillier, newline lines 1740--3225

```text
  2. Supposons maintenant que Z soit une omposante irrédu tible de Ys , de point générique
     ηe = rY (η), η ∈ S0 (Y). Vérions tout d'abord que, si f −1     s
                                                                        (Z) ontient un point fermé
     x de Xs , il ontient toute une omposante irrédu tible de Xs passant par x. Ce i se
     reformule ainsi : étant données une omposante c ∈ π0 (Yη − S0 (Y)) telle que η ∈ ∂c et
     une omposante c′ ∈ π0 (Xη − S0 (X )) telle que f (c′ ) ⊂ c, il existe un point ξ ∈ ∂c′ tel que
     f (ξ) ∈ c ou f (ξ) = η . Si f −1 (c) ne ren ontre pas ∂c′ , nous venons de prouver qu'alors
     f (c′ ) = c ; on en déduit que le fermé f (c′ ) est l'adhéren e de c dans Yη , e qui implique
     que f envoie surje tivement ∂c′ sur ∂c et fournit l'existen e d'un point ξ ∈ ∂c′ tel que
     f (ξ) = η .
         Il ne reste plus, pour établir que f −1
                                              s
                                                 (Z) est un fermé de Xs , qu'à montrer que 'est une
     partie stable par spé ialisation. Soit ξ un point dans S0 (X ) tel que rX (ξ) appartienne à
     f −1
       s
           (Z). Notons que, puisque Z est une partie fermée de Ys , rY−1 (Z) est un ouvert de Yη ;
     rX (f s (Z)) = f −1 (rY−1 (Z)) est alors un voisinage ouvert de ξ dans Xη et ren ontre don
       −1 −1
26



       toutes les omposantes onnexes de Xη − S0 (X ) adhérentes à ξ . Ce i prouve l'in lusion
       {rX (ξ)} ⊂ f −1
                    s
                       (Z).
Troisième étape. Il sut maintenant de dénir le prolongement f de f omme le morphisme de
S -s hémas formels (f s , f ♯ ) : X = (Xs , OX ) → Y = (Ys , OY ), où f s : Xs → Ys est l'appli ation
 ontinue que l'on vient de dé rire entre les espa es topologiques et f ♯ est l'homomorphisme
entre les fais eaux stru turaux ara térisé par la ondition suivante : pour tous ouverts anes
                                                                                               −1
U ⊂ Xs et V ⊂ Ys tels f s (U ) ⊂ V  'est-à-dire tels que f envoie le domaine anoïde rX          (U )
                                 −1         ♯
dans le domaine anoïde rY (V ) , f est l'homomorphisme de
                                                  −1
                                   Γ(U, OX ) = Γ(rX  (U ), OXη )◦
dans
                              Γ(V, OY ) = Γ(rY−1 (V ), OYη )◦
induit par l'homomorphisme d'algèbres stri tement k-anoïdes
                                      −1
                             f ♯ : Γ(rX  (U ), OXη ) → Γ(rY−1 (V ), OYη ).

(ii) Le morphisme f est lo alement de type ni. S'il est quasi-ni, sa bre au-dessus de tout
point fermé de Ys ne ontient au un point générique de Xs , ondition qui s'é rit de manière
équivalente sous la forme
                                    f (S0 (X )) ⊂ S0 (Y).
Ré iproquement, si ette ondition est vériée, le raisonnement onduit lors de la deuxième
étape montre que les bres de f sont dis rètes.                                            2
Domaines analytiques ompa ts.
Proposition 2.1.16.  Soit X une S - ourbe quasi- ompa te dont la bre générique est
irrédu tible.
   (i ) Si Xs est propre, Xη est propre.
   (ii ) Si Xs n'est pas propre  'est-à-dire si l'une au moins de ses omposantes irrédu tibles
est ane , Xη est un espa e stri tement k-anoïde.
Démonstration. Notons tout d'abord que les omposantes irrédu tibles de la ek - ourbe sé-
parée Xs sont des e  k- ourbes algébriques anes ou propres.
   La k◦ -algèbre A = Γ(X , OX ) est topologiquement de présentation nie et le morphisme
stru tural X → S se fa torise par Y = Spf(A) :
                                             X@
                                                  @@ p
                                                    @@
                                                      @@
                                                        
                                                            Y
                                                       ~~
                                                    ~~~
                                               ~ ~
                                             S.
Le morphisme ps : Xs → Ys induit un isomorphisme de haque omposante irrédu tible ane
de Xs sur une omposante irrédu tible ane de Ys et ontra te ha une des omposantes
irrédu tibles propres de Xs sur un point de Ys . La e
                                                    k- ourbe algébrique Xs étant onnexe, Ys
est un ek-s héma ane onnexe et il y a don deux possibilités :
    si Xs est une ourbe propre, Ys est un point, auquel as p est la fa torisation de Stein
     du morphisme propre p ;
                                                                                               27



    si la ourbe Xs n'est pas propre, Ys est une e   k- ourbe algébrique ane.
La on lusion est immédiate dans le premier as : l'espa e stri tement k-analytique Xη est
 ompa t et sans bord (2.1.2), don propre.
   Envisageons maintenant le se ond as. Les morphismes p et pη sont propres, surje tifs et,
leurs fa torisations de Stein étant manifestement triviales, à bres onnexes. Puisque l'espa e
stri tement k-analytique Xη est, par hypothèse, irrédu tible, l'image de pη est un sous-espa e
stri tement k-analytique irrédu tible de Yη , né essairement de dimension 1 vu la surje tivité
de pη . On en déduit que pη est une bije tion, et don un isomorphisme ([3℄, 2.2.7, (iii), omplété
par [4℄, 1.2.1, Remarks, (i)).                                                                 2
Corollaire 2.1.17.  Soit X          une S - ourbe formelle séparée dont la bre générique X
est irrédu tible et soit Y1 , Y2 ⊂ X deux domaines stri tement k-anoïdes ; si Y1 ∪ Y2 6= X ,
Y1 ∪ Y2 est un domaine stri tement k-anoïde.
Démonstration. Le as de deux domaines stri tement k-anoïdes d'interse tion vide est
trivial : Y1 ∪ Y2 = M(AY1 ⊕ AY2 ). Nous pouvons don supposer Y1 ∩ Y2 6= ∅, auquel as Y1 ∪ Y2
est onnexe.
   Il existe un é latement admissible q : Y → X et des ouverts U1 , U2 ⊂ Ys tels que
Yi = Y|Ui η ([25℄, 3). Le morphisme q étant séparé, Y|U1∪U2 est une S - ourbe dont la
bre générique Y1 ∪ Y2 est irrédu tible.
   Si la ek - ourbe U1 ∪ U2 est propre, 'est une partie ouverte et fermée de Ys ; il en est de
même pour Y1 ∪ Y2 ⊂ Xη et don Y1 ∪ Y2 puisque Xη est onnexe. La on lusion dé oule don
de la proposition pré édente.                                                               2
Corollaire 2.1.18.  Soit X une         ourbe stri tement k-analytique irrédu tible ; tout om-
pa t stri t K ⊂ X est l'interse tion d'une famille dé roissante de domaines stri tement k-
anoïdes.
Démonstration. Les domaines stri tement k-anoïdes formant un système fondamental de
voisinages des points de X , tout ompa t K ⊂ X est ontenu dans un domaine stri tement
k-analytique ompa t de X . En vertu du orollaire pré édent, un domaine stri tement k-
analytique ompa t distin t de X est un domaine stri tement k-anoïde ; ainsi, les domaines
stri tement k-anoïdes forment un système fondamental de voisinages des ompa ts stri ts
de X .                                                                                  2
Classi ation des points.
   Soient x un point d'une ourbe stri tement k-analytique X et H(x) son orps résiduel
                                 ] e
 omplété. L'extension résiduelle H(x)/ k est de degré de trans endan e au plus 1, noté s(x),
et le groupe abélien |H(x) |/|k | est de rang au plus 1, noté t(x) ; l'inégalité
                          ×    ×


                                        s(x) + t(x) ≤ 1

est toujours vériée.
   Reprenant la terminologie de [3℄, le point x sera dit
    de type (2) si s(x) = 1,
    de type (3) si t(x) = 1.
                                 ] e
Dans es deux as, l'extension H(x)/     k et le groupe abélien |H(x)× |/|k× | sont de type ni.
   Les points de type (2) ou (3) (resp. de type (2)) sont en ore ara térisés par la propriété
suivante : x ∈ X est de type (2) ou (3) (resp. de type (2)) si et seulement s'il existe un domaine
k-anoïde (resp. un domaine stri tement k-anoïde Y ⊂ X ) tel que Γ(Y ) = {x}.
  Lorsque s(x) = t(x) = 0, le point x est dit
28



      de type (1) lorsque l'extension non ar himédienne H(x)/k se plonge dans la omplétion
       d'une lture algébrique de k :
                                       ca bD
                                       kO D DD
                                              DD
                                                DD
                                        k       / H(x),

   de type (4) sinon.
Parmi les points de type (1) gurent en parti ulier eux tels que l'extension H(x)/k soit
nie ; e sont les points traditionnellement onsidérés en géométrie rigide et ils forment un
sous-ensemble partout dense de X , noté X0 .
    Il est lair qu'un morphisme ni f : Y → X onserve le type des points : tous les points de
la bre f −1 (x) sont du type de x ; il en va de même pour le hangement de base k → k  ca .
Lemme 2.1.19.  Soient x un point d'une                ourbe stri tement k-analytique X et
px : X ⊗ b k H(x) → X la proje tion anonique ; les onditions suivantes sont équivalentes :
(i ) x est de type (1) ;
(ii ) s(y) = 0 pour tout point y ∈ p−1
                                    x (x).
Démonstration. On peut supposer X = A1k .
    Soient x un point dans A1k et x∗ : k[T ] → H(x) l'homomorphisme orrespondant ; le H(x)-
point x de A1H(x) déni par l'homomorphisme
                                H(x)[T ] → H(x),     T 7→ x∗ T
est tel que px (x) = x et on pose
                                     r(x) = sup |T − x|
                                            p−1
                                             x (x)

([3℄, 4.2). Le disque ouvert D(x, r(x)) = {y ∈ A1H(x) ; |T − x|(y) < r(x)} est trivialement
 ontenu dans la bre p−1
                       x (x) et la on lusion dé oule de e que le point x est de type (1) si et
seulement si r(x) = 0 ([3℄, 4.2).                                                           2
Extension des s alaires.
   Soient X une ourbe k-analytique et K/k une extension non ar himédienne ; posons XK =
X⊗ b k K et soit pK : XK → X le morphisme anonique.
   Étant donné un point x ∈ X de type (2) ou (3), onsidérons un domaine k-anoïde Y ⊂ X
tel que Γ(Y ) = {x}. Le bord de Shilov du domaine K -anoïde YK = Y ⊗         b k K de XK est
  ontenu dans la bre de pK (x) d'après [3℄, 2.2.5 et il dénit un sous-ensemble ni iK (x) de
                           −1

p−1
  K (x), formé de points de type (2) ou (3), qui ne dépend lairement pas du hoix de Y .
Dans le as d'un point x de type (2), Ye est une ek - ourbe algébrique (ane) intègre et iK (x)
est l'image ré iproque de l'ensemble des points génériques de la K e - ourbe ane Ye ⊗e Ke par
                                                                                       k
l'appli ation de rédu tion YK → Ye ⊗ek K
                                       e (2.1.1, Rédu tions ).
                            −1
Lemme 2.1.20.  L'ensemble pK (x) − iK (x) est un ouvert de XK .

Démonstration. C'est évident puisque YK − Γ(YK ) est un ouvert de XK en vertu de la
proposition 2.1.12.                                                                         2
Proposition 2.1.21.  Soient X une ourbe stri tement k -analytique et Ω ⊂ X un ou-
vert tel que tous les points de ∂Ω soient de type (2) ou (3) ; étant donnée une extension non
ar himédienne K/k, tous les points de ∂p−1 K (Ω) sont de type (2) ou (3).
                                                                                                           29



Démonstration. D'après le lemme pré édent,
                           [                                [                  
                                 i−1       −1
                                  K (x) = pK (∂Ω) −             p−1
                                                                 K (x) − iK (x)
                          x∈∂Ω                          x∈∂Ω

est un fermé de XK et la on lusion dé oule de e qu'il ontient ∂p−1
                                                                K (Ω).                                     2
Re ouvrements.
   L'espa e topologique sous-ja ent à une ourbe stri tement k-analytique est de dimension
1 : tout re ouvrement ouvert lo alement ni U admet un ranement lo alement ni U ′ tel
que trois ouverts distin ts dans U ′ soient d'interse tion vide ([3℄, 3.2.1). Nous terminons ette
se tion par la des ription d'un système nal de re ouvrements ouverts lo alement nis d'une
 ourbe stri tement k-analytique.
Proposition 2.1.22.  Soit X un espa e k -analytique onnexe et para ompa t de di-
mension 1 et soit U un re ouvrement ouvert lo alement ni de Ω = X − ∂X . Il existe un
re ouvrement ouvert lo alement ni V de Ω ranant U et tel que, posant
                                                 [
                                           S=        ∂V,
                                                     V ∈V

tout point de S soit de type (2) et ontenu dans un unique ouvert V ∈ V .
Démonstration. On peut supposer que les éléments de U sont relativement ompa ts (raf-
ner U si né essaire).
  Un premier ranement de U permet de supposer que les points de ∂U sont de type (2)
pour tout ouvert U ∈ U . Fixons en eet U0 ∈ U ; le fermé
                                                [
                                  F0 = Ω −              U
                                                     U ∈U ; U 6=U0

est ontenu dans U0 et il existe un domaine stri tement k-anoïde Y0 ⊂ U0 tel que
                                              F0 ⊂ Y0 − ∂Y0 .
On obtient un ranement de U en remplaçant U0 par U0′ = Y0 − ∂Y0 . Appliquant le même
raisonnement à ha un des ouverts U1,1 , . . . , U1,n ∈ U ren ontrant U0′  il n'y en a qu'un
nombre ni , on obtient des ouverts U1,1                             1,n tels que ∂U1,i ⊂ I(X) pour tout i et
                                                         ′ , . . . , U′              ′

{U0 , U1,1 , . . . , U1,n } ∪ (U − {U0 , U1,1 , . . . , U1,n } soit un re ouvrement de Ω ranant U ; raison-
   ′   ′              ′

nant par ré urren e transnie, on peut, après ranement, supposer que la frontière de tout
ouvert U ∈ U est un ensemble ni de points de type (2).
   Sous ette hypothèse, la réunion S des ∂U , U ∈ U , est un ensemble lo alement ni de
points de type (2) dans Xη . Quels que soient l'ouvert U ∈ U et la omposante onnexe C de
Ω − S,
                                        C ∩U =C ∩U
puisque ∂U = U − U est ontenu dans S et don C ⊂ U ou C ∩ U = ∅ ; par suite, étant
donnés un point x ∈ S et un ouvert U ∈ U ontenant x, toute omposante onnexe de Ω − S
adhérente à x est ontenue dans U . Soit Ωx la réunion des omposantes onnexes de Ω − S
qui sont adhérentes à x ; 'est un voisinage de x dans Ω qui, d'après e que l'on vient de dire,
est ontenu dans
              tout ouvert U ∈ U qui ontient x.
   La famille Ωx x∈S est un re ouvrement ouvert lo alement ni de Ω qui rane le re ou-
vrement U ; S est la réunion des ∂Ωx , x ∈ S , et un point y de S appartient à l'ouvert Ωx si
et seulement si y = x. Ce re ouvrement satisfait à toutes les onditions de l'énon é.       2
30



                                 2.2. S - ourbes semi-stables
  Le ontenu de ette partie est un as très parti ulier des onstru tions introduites par
Berkovi h dans [5℄.

2.2.1. Courbes S(a)
  Soit a un élément non nul de k◦ et soit A(a) la k◦ -algèbre topologiquement de présentation
nie
                                  k◦ {T0 , T1 }/(T0 T1 − a).
L'épimorphisme anonique k◦ {T0 , T1 } → A(a) induit un isomorphisme α du sous k◦ -module
libre                                                                              
                     X
                                      ν0 ν1    ◦
        M= f=                aν (f )T0 T1 ∈ k {T0 , T1 } ; aν (f ) = 0 si ν0 ν1 6= 0
                      ν=(ν0 ,ν1 )∈N2
de k {T0 , T1 } sur A(a). L'homomorphisme de k-algèbres de Bana h
    ◦

                                   ϕ : k{T0 , T1 } → k{|a|T −1 , T }
déni par ϕ(T0 ) = aT −1 , ϕ(T1 ) = T , réalise un isomorphisme du k-espa e de Bana h M ⊗k◦ k
sur k{|a|T −1 , T } et ϕ ◦ α−1 est un isomorphisme isométrique entre la k-algèbre de Bana h
A(a) ⊗k◦ k, munie de la norme dénie par le k◦ -module A(a), et la k-algèbre de Bana h
k{|a|T −1 , T }, munie de sa norme spe trale. Il dé oule de es observations que :
  (i) la k◦ -algèbre A(a) est plate,                           ◦
  (ii) l'homomorphisme anonique A(a) → A(a) ⊗k◦ k est un isomorphisme,
  (iii) pour tout ρ = (ρ0 , ρ1 ) ∈ R2>0 tel que ρ0 ρ1 = |a|, la (semi-)norme sur M ⊗k◦ k → R≥0
induite par l'appli ation
                                             X
                    k{T0 , T1 } → R≥0 , f =      aν (f )T0ν0 T1ν1 7→ max |aν (f )|ρν
                                                                       ν
                                                 ν
dénit via α une (semi-)norme multipli ative sur A(a) ⊗k◦ k, notée ηρ .
   Soit S(a) le S -s héma formel Spf(A(a)). Sa bre générique est le domaine stri tement k-
anoïde {x ∈ A1k | |a| ≤ |T1 (x)| ≤ 1} de la droite ane sur k tandis que sa bre spé iale est
le tore Gmek si |a| = 1, la somme amalgamée du diagramme

                                            A1e
                                                Ok
                                            0


                                         Spec(e
                                              k) 0       / A1
                                                           e
                                                           k

si |a| < 1.

     Introduisons le polytope entier
                     S(|a|) = {t ∈ R2 | 0 ≤ t0 , 0 ≤ t1 et t0 + t1 = − log |a|},
de groupe stru tural ( f. 1.1.1)
                                                 
                        Λ(S(|a|)) = R ⊕ Zt0 ⊕ Zt1 /Z(log |a| + t0 + t1 ).
     L'appli ation
                       µ : S(a)η → R2 , x 7→ (− log |T0 (x)|, − log |T1 (x)|)
                                                                                                  31



est ontinue et à valeurs dans S(|a|) ⊂ R2 ; elle admet une se tion ontinue
                                  ι : S(|a|) → S(a)η ,     t 7→ ηe−t
réalisant un homéomorphisme de S(|a|) sur un fermé S(S(a)) de S(a)η .           
   Par dénition, le squelette de S(a) est le polytope entier S(a), µ∗ Λ(S(|a|)) . L'appli ation
ι ◦ µ : S(a)η → S(S(a)), notée τ , est une rétra tion de S(a)η sur son squelette.
                                                                                              
   Étant donnée une extension non ar himédienne K de k, S(a)η ⊗     b k K = S(a)×S Spf(K ◦ )
                                                                                                η
et le morphisme anonique p : S(a)η ⊗     b k K → S(a) induit une appli ation de S(S(a) ×S
Spf(K ◦ )) dans S(S(a)) ; 'est un isomorphisme de polytopes entiers s'insérant dans le dia-
gramme ommutatif
                                             τ /
                                   b kK
                             S(a)η ⊗             S(S(a) ×S Spf(K ◦ ))
                                  p                               p
                                                             
                                S(a)η                   / S(S(a)).
                                                 τ
Les squelettes S(S(a) ×S Spf(K ◦ )) et S(S(a)) sont don anoniquement isomorphes ; pour
alléger l'é riture, nous é rirons S(S(a))K en lieu et pla e de S(S(a) ×S Spf(K ◦ )).

   Il est fa ile de donner une ara térisation intrinsèque du squelette de S(a). Commen-
çons par observer que le groupe stru tural de e polyèdre entier s'identie
                                                                        × au sous-groupe de
C (|S(a)η |, R) engendré par R et les fon tions log |f |, f ∈ A(a) ⊗k◦ k : 'est le ontenu du
  0

lemme suivant.
Lemme 2.2.1.  Soit |.|sp la norme spe trale de la k -algèbre de Bana h A(a) ⊗k ◦ k ; le
                    ×
groupe A(a) ⊗k◦ k des inversibles de l'anneau A(a) ⊗k◦ k est onstitué des éléments de la
forme

                                       αT0n0 T1n1 (1 + g),
où α ∈ k× , n0 , n1 ∈ N, g ∈ A(a) ⊗k◦ k et |g|sp < 1.
  En parti ulier : l'image de l'homomorphisme
                                    ×
                          A(a) ⊗k◦ k → C0 (|S(a)η |, R), f 7→ log |f |,
est le sous-groupe abélien engendré par log |k× | et les fon tions log |T0 |, log |T1 |.
Démonstration. Les éléments de   ×
                                    A(a) ⊗k◦ k pouvant s'é rire omme dans l'énon é forment
un sous-groupe I ⊂ A(a) ⊗k◦ k       et il sut don de vérier que tout élément inversible de
A(a) ⊗k◦ k appartient à I .
   Considérons tout d'abord le as parti ulier a = 1. La norme spe trale |.|sp de la k-algèbre de
Bana h k{T −1 , T } étant multipli ative (en vertu de l'irrédu tibilité de Spec(e k[T ]), proposition
2.1.2), un élément inversible f de k{T −1 , T } est de la forme f = αg, ave α ∈ k× tel que
|α| = |f |sp et g ∈ k◦ {T −1 , T }× . La rédu tion de g dans e
                                                             k[T −1 , T ] est inversible, don de la
forme βT n ave β ∈ e  k et n ∈ Z, et g s'é rit par onséquent
                                      g = γT n + h = γT n (1 + h′ ),
où γ ∈ k◦ − k◦◦ , h ∈ k◦◦ {T −1 , T } et h′ = γ −1 T −n h. Comme |h′ |sp = |h|sp < 1, f appartient
à I.
  Le as général se déduit du as a = 1. C'est immédiat si |a| = 1 puisqu'alors A(a) ≃ A(1),
de sorte que l'on peut supposer |a| < 1. Identions A(a) ⊗k◦ k et k{|a|T −1 , T } en posant
32


                                                                   P
T1 = T , T0 = aT −1 et onsidérons un élément inversible f = n∈Z an T n dans k{|a|T −1 , T }.
Quel que soit le nombre réel r ∈ [|a|, 1], l'image de f par l'homomorphisme k{|a|T −1 , T } →
k{rX −1 , r −1 X}, T 7→ X , est inversible ( 'est la restri tion de f au domaine k-anoïde
|T | = r ) et il en est de même après une extension non ar himédienne K/k telle que r ∈
|K × |. Étant donnée l'identi ation K{rX −1 , r −1 X} ≃ K{Y −1 , Y }, la dis ussion pré édente
implique l'existen e d'un unique entier relatif N (r) tel que |aN (r) |r N (r) = maxn (|an |r n ) = |f |r ,
|.|r désignant la norme spe trale sur k{rX −1 , r −1 X}.
    L'appli ation N : [|a|, 1] → Z, r 7→ N (r) est lo alement onstante : soit en eet r0 ∈ [|a|, 1] ;
la suite (|an |r n ) tendant vers 0 lorsque |n| tend vers +∞ pour tout r ∈ [|a|, 1], il existe un
sous-ensemble ni I de Z et un voisinage V de r0 dans [|a|, 1] tels que
                                        max |an |r n = max |an |r n
                                        n∈Z                     n∈I

pour tout r ∈ V     et les inégalités |aN (r0 ) |r N (r0 ) > |an |r n , n ∈ I − {N (r0 )}, sont vériées sur
tout un voisinage de r0 dans V .
  L'appli ation N est don onstante et il existe ainsi un entier relatif N tel que :
                               |an | < |aN |        et     |an ||a|n < |aN ||a|N
pour tout n ∈ Z − {N }. Ces inégalités peuvent s'é rire sous la forme
                                                                 
                      max max(|an a−1                −1
                                      N |), max(|an aN ||a|
                                                           n−N
                                                                ) < 1,
                                 n6=N                    n6=N
                P              −1
                                         
 'est-à-dire      n∈Z−{N } an aN T     < 1, et nous obtenons nalement la formule
                                     n−N
                                               sp
                  X                     X                 
                        n       N                   −1 n−N
               f=   an T = aN T     1+          an aN T      = aN T N (1 + g)
                    n∈Z                             n∈Z−{N }

ave |g|sp < 1. La démonstration est a hevée.                                                             2

Remarque 2.2.2.  Le lemme pré édent n'est bien entendu pas autre hose que l'assertion
 lassique selon laquelle un élément f ∈ k{|a|T −1 , T } est inversible si et seulement si son
polygone de Newton {(x, y) ∈ [0, − log |a|] × R ; y = maxn log |an |e−nx } est un segment ; 'est
d'ailleurs exa tement e que l'on a démontré.

     Passons à la des ription du fermé S(S(a)) de S(a)η .
Définition 2.2.3.  Un espa e k -anoïde X est dit potentiellement isomorphe au disque
unité s'il existe une extension nie séparable k′ de k telle que l'espa e k′ -anoïde X ⊗k k′
soit isomorphe à une somme (né essairement nie) de opies du disque unité Ek′ (0, 1) = {x ∈
A1k′ | |T1 (x)| ≤ 1}.

Remarque 2.2.4.  Un domaine k-anoïde est potentiellement isomorphe au disque unité
si et seulement si ha une de ses omposantes onnexes l'est.

Proposition 2.2.5.  Pour tout a ∈ k
                                                         ◦ − {0}, le fermé S(S(a)) ⊂ S(a)
                                                                               est le om-η
plémentaire de l'ensemble des points de S(a)η ayant un voisinage k-anoïde potentiellement
isomorphe au disque unité.

  Rappelons que, pour tout point x ∈ A1k , il existe une et une seule omposante onnexe Ω
de A1k − {x} dont l'adhéren e dans A1k n'est pas ompa te ; on la qualiera de non bornée.
                                                                                                  33



Lemme 2.2.6.  Un domaine k -anoïde         onnexe V dans A1k est potentiellement isomorphe
au disque unité si et seulement s'il possède un unique point de Shilov ξ et oïn ide ave le
 omplémentaire, dans A1k , de la omposante onnexe non bornée de A1k − {ξ}.
Démonstration. L'image d'un morphisme non onstant ϕ : M(k{T }) → A1k est le disque
{|T1 − f (0)| ≤ |f − f (0)|sup = |f − f (0)|(η)}, f ∈ k{T } étant la série entière ϕ∗ T1 ; 'est le
  omplémentaire dans A1k de la omposante onnexe non bornée de A1k − {ϕ(η)} (η est le point
de Shilov de M(k{T })).
   Un domaine k-anoïde V ⊂ A1k , onnexe et potentiellement isomorphe au disque unité, est
l'image d'un morphisme non onstant ϕ : M(k′ {T }) → A1k , k′ étant une extension séparable
nie de k. Le morphisme ϕ se fa torise par le morphisme anonique q : A1k′ → A1k et, puisque
l'image du morphisme induit de M(k′ {T }) dans A1k′ est le omplémentaire dans A1k′ de la
  omposante non bornée de A1k′ − {ϕ′ (η ′ )}, V est le omplémentaire dans A1k de la omposante
  onnexe non bornée de A1k − {ϕ(η ′ )} (η ′ est le point de Shilov de M(k′ {T })).
   Soient ré iproquement ξ ∈ A1k un point de type (2)  'est-à-dire tel que l'extension de
       ] e
 orps H(x)/  k soit de degré de trans endan e 1  et V le omplémentaire de la omposante
 onnexe non bornée de A1k − {ξ}. Par densité de l'ensemble E des points x ∈ A1k tels que κ(x)
soit une extension séparable nie de k, il existe un point de E appartenant à l'ouvert non vide
V − {ξ} ; soit f ∈ k[T1 ] son polynme minimal unitaire. La fon tion |f | atteint son maximum
sur le ompa t V en un point de la frontière ∂V , don en ξ ; par suite, V est ontenu dans le
domaine stri tement k-anoïde {|f | ≤ |f (ξ)|} et oïn ide en fait ave lui puisque A1k − V est
la omposante onnexe non bornée de A1k −{ξ}. Ce i prouve que V est un domaine stri tement
k-anoïde dont ξ est l'unique point de Shilov. Enn, f étant par hypothèse séparable sur k,
V est isomorphe à une somme de opies du disque unité sur toute extension séparable nie k′
de k dé omposant f et telle que |f (ξ)| ∈ |k′ × |.                                           2
Démonstration de la proposition 2.2.5. Identions S(a)η au domaine stri tement k-
anoïde {|a| ≤ |T1 | ≤ 1} de A1k et introduisons l'ouvert Ω de S(a)η onstitué des points
admettant un voisinage k-anoïde potentiellement isomorphe au disque unité.
Étant donné un tel domaine k-anoïde onnexe V ⊂ S(a)η , les deux omposantes onnexes de
A1k − S(a)η sont ontenues dans l'ouvert onnexe U = A1k − V ; elui- i ontient en parti ulier
0, et don toute l'image de l'appli ation ontinue R≥0 → A1k envoyant le nombre réel positif
r sur la semi-norme
                                           X
                        ηr : k[T ] → R≥0 ,    an T n 7→ max(|an |r n )
                                                              n
                                                n

 ar U est onnexe par ar s et tout hemin ontinue reliant 0 au point à l'inni ontient l'image
de ette appli ation. Puisque l'image de ι : S(|a|) → S(a)η ⊂ A1k est le fermé {ηr ; r ∈ [|a|, 1]},
 ela prouve l'in lusion Ω ⊂ S(a)η − S(S(a)).
   L'in lusion ré iproque S(a)η − S(S(a)) ⊂ Ω        dé oule du fait suivant : pour tout point
t ∈ S(|a|) ⊂ R, τ (t) ∩ S(a)η − S(S(a)) est la réunion d'une famille roissante de
                       −1

domaines
       p k-anoïdes potentiellement        isomorphes au disque unité. Cette
                                                                          p assertion est triviale
si t ∈
     /    |k× | puisque la bre τ −1 (t) est réduite au point ι(t). Si t ∈ |k× |, il existe un point
x ∈ τ −1 (t) tel que l'extension κ(x)/k soit nie et séparable ; notant f le polynome minimal
unitaire de x sur k, l'ouvert τ −1 (t) − {ι(t)} oïn ide ave {|f | < |f (ι(t))|} et est la réunion des
domaines stri tement k-anoïdes potentiellement       p isomorphes au disque unité {|f | ≤ αn },
(αn ) étant une suite stri tement roissante dans |k× | qui onverge vers |f |(ι(t)).                2
34



Remarque 2.2.7.  Soit ξ un point de type (2) dans S(a)η − S(S(a)) ; le omplémentaire
V de la omposante onnexe non bornée de A1k − {ξ} est un domaine k-anoïde potentielle-
ment isomorphe au disque unité, que l'on peut dé rire en termes d'é latements admissibles ;
rappelons qu'il s'agit des é latements, dans la atégorie des S -s hémas formels, des Idéaux
 ohérents et ouverts (voir [10℄, 2).
  On note r l'appli ation de rédu tion S(a)η → S(a)s .
   Si r(ξ) est un point lisse de S(a)s , il existe un é latement admissible q : Y → S(a),
     entré au point r(ξ), tel que la bre spé iale réduite de Y soit la somme amalgamée du
    diagramme
                                        S(a)s
                                                   O
                                       r(ξ)

                                   Spec(κ(r(ξ)))                            / P1
                                                                    ∞          κ(r(ξ))


       et V soit la bre générique du S -s héma formel induit par Y sur l'ouvert Ysréd − S(a)s ≃
       A1κ(r(ξ)) .
      Si r(ξ) est le point singulier de S(a)s , il existe un é latement admissible q1 : Y1 →
       S(a), entré en r(ξ), tel que la bre spé iale réduite de Y1 soit la somme amalgamée du
       diagramme
                                            `
                                         A1e A1e
                                                   k       O    k

                                                       0
                                                       `
                                   Spec(k)                     Spec(k) `           / P1 ,
                                                                                      e
                                                                                      k
                                                                        0     ∞

       et, notant r ′ l'appli ation de rédu tion Y1,η → Y1,s , un é latement admissible q2 : Y2 →
       Y1 , entré en un point fermé de P1e − {0, ∞} ⊂ Y1,s , tel que la bre spé iale réduite de
                                            k
       Y2 soit la somme amalgamée du diagramme

                                        Y1 réd
                                           s   O
                                     r ′ (ξ)

                                  Spec(κ(r ′ (ξ)))                          / P1
                                                                    ∞         κ(r ′ (ξ)) ,

                                                                                   réd − Y réd ≃
       et V soit la bre générique du S -s héma formel induit par Y2 sur l'ouvert Y2,s    1,s
       A1κ(r′ (ξ)) . Le point de Y1,η = S(a)η envoyé par r ′ sur le point générique du diviseur
       ex eptionnel de Y1,s est le point τ (ξ) de S(S(a)).
   Dans les deux as envisagés, les bres spé iales Ys , Y1,s et Y2,s sont réduites si (et seulement
si) |κ(ξ)× | = |k× |. Finalement : étant donné un domaine k-anoïde V de S(a)η potentielle-
ment isomorphe au disque unité, il existe, après un hangement de base S ′ → S , S ′ = Spf(k′ ◦ )
ave k′ /k une extension séparable nie, un é latement admissible q : Y → S(a), entré en
r(ξ), et un ouvert U de Ys tels que
   (i) la bre spé iale Ys soit réduite ;
   (ii) l'adhéren e de U soit une réunion de omposantes irrédu tibles de Ys isomorphes à P1e′ ;
                                                                                                k
   (iii) V ⊗k k′ s'identie à la bre générique du S ′ -s héma formel induit par Y sur U .
                                                                                              35



2.2.2. Le squelette d'une S - ourbe simplement semi-stable : début
   La onstru tion du squelette et de la rétra tion se généralise naturellement aux S - ourbes
formelles admettant lo alement un morphisme étale vers une S - ourbe S(a), a ∈ k◦ − {0}.
Introduisons plus pré isément la dénition habituelle suivante.
Définition 2.2.8.  Une S - ourbe X est dite simplement semi-stable s'il existe un re ou-
vrement par des ouverts U admettant un morphisme étale pU : U → S(a(U )), a(U ) ∈ k◦ −{0}.

Remarque 2.2.9
  1. La bre générique d'une S - ourbe simplement semi-stable X est un espa e stri tement
     k-analytique rig-lisse, 'est-à-dire tel que le G-fais eau ΩXη /k soit un OXη -module lo a-
     lement libre.
  2. L'adverbe simplement vient de e que l'on travaille ave la topologie de Zariski ; on
     pourrait, plus généralement, onsidérer les S - ourbes qui, lo alement pour la topologie
     étale, sont isomorphes à une ourbe S(a), a ∈ k◦ − {0}. Cette restri tion a pour eet de
     garantir la lissité de ha une des omposantes irrédu tibles de Xs . Soient en eet C une
     e
     k- ourbe lo alement algébrique et p : C → S(a)s un morphisme étale ave 0 < |a| < 1.
     Les omposantes irrédu tilbes de C sont lisses : étant donné un point singulier x e de C et
     une omposante irrédu tible Z de C passant par x    e, l'image de Z par p est ontenue dans
     une omposante irrédu tible Y de S(a)s et le hangement de base Y ֒→ S(a)s donne
     lieu à un morphisme étale p|Z : Z → Y ; la lissité de Y implique elle de Z au point x  e.
        Pour e qui suit, la restri tion aux ourbes simplement semi-stables n'est pas indis-
     pensable.
  3. La déformation des singularités quadratiques montre qu'une S - ourbe X est simplement
     semi-stable si et seulement si sa bre générique Xη est lisse et sa bre spé iale Xs est
     une ek- ourbe (lo alement algébrique) dont les seules singularités sont des points doubles
     ordinaires et dont les omposantes irrédu tibles sont lisses.

  Passons maintenant à la onstru tion du squelette d'une S - ourbe simplement semi-stable.
Théorème 2.2.10.  Il existe, pour toute S - ourbe simplement semi-stable X , un unique
 ouple (S(X ), τX ), onstitué d'un polyèdre entier de dimension au plus 1 et d'une appli ation
τX : Xη → S(X ), tel que :
   (i ) l'espa e topologique sous-ja ent à S(X ) soit un fermé de Xη et l'appli ation τX soit une
rétra tion, 'est-à-dire induise l'identité sur S(X ) ;
   (ii ) pour toutouvert U de X , S(X )∩Uη est un domaine polyédral dans S(X ) et l'immersion
 anonique X|U η ֒→ Xη induit un isomorphisme de S(X|U ) sur S(X ) ∩ Uη , ompatible aux
rétra tions ;
   (iii ) quel que soit le morphisme étale p : X → Y entre deux S - ourbes semi-stables, pη
induit une appli ation de S(X ) dans S(Y) qui est un isomorphisme G-lo al de polyèdres entiers
s'insérant dans un diagramme ommutatif :
                                                 τX
                                         Xη           / S(X )

                                        pη                   pη
                                                        
                                         Yη      τY
                                                      / S(Y).



  La démonstration du théorème 2.2.10 s'étend jusqu'à le proposition 2.2.20.
36



  La ara térisation du fermé S(X ) ⊂ Xη reprend la des ription de S(S(a)) ⊂ S(S(a))η
donnée dans la proposition 2.2.5.
Lemme 2.2.11.  Soient X une S - ourbe, p : X → S(a)                un morphisme étale (a ∈
k◦ − {0}) et V ⊂ Xη , Z ⊂ S(a)η des domaines k-anoïdes ;
   si V est potentiellement isomorphe au disque unité, il en est de même pour p(V ) ;
   si p−1 (Z) 6= ∅ et Z est potentiellement isomorphe au disque unité, il en est de même pour
     p−1 (Z).
Démonstration. Soit V ⊂ Xη un domaine k-anoïde potentiellement isomorphe au disque
unité. Chaque omposante onnexe de V est l'image de M(k′ {T }) par un morphisme non
 onstant, k′ étant une extension nie séparable onvenable de k, et p(V ) est don un domaine
k-anoïde potentiellement isomorphe au disque unité (lemme 2.2.6).
   Soit Z ⊂ S(a)η un domaine k-anoïde onnexe et potentiellement isomorphe au disque
unité. Après un hangement de base S ′ → S , ave S ′ = Spf(k′ ◦ ), k′ étant une extension nie
séparable de k, il existe un é latement admissible q : Y → S(a), entré en un point fermé x    e
de S(a)s , et un ouvert U de Ys tels que le ek-s héma Ys soit réduit, l'adhéren e de U soit une
réunion de omposantes irrédu tibles isomorphes à P1e et Z s'identie à la bre générique du
                                                        k
s héma formel induit par Y sur U . Si l'image ré iproque p−1 (Z) est non vide, la bre de ps
au-dessus de xe est non vide et le morphisme induit par p entre les s hémas formels semi-lo aux
Xp−1  e)
   s (x
         et S(a) e est étale et ni. Considérons alors le diagramme artésien
                 x

                                                 q′
                                         Y′            /X

                                        p′                   p
                                                        
                                         Y       q
                                                      / S(a);

le morphisme p′ est étale et il est ni au-dessus de q −1 (e
                                                           x) ; il induit don un revêtement
étale au-dessus du sous-s héma fermé réduit U de Ys . Cha une des omposantes irrédu tibles
de U étant, par hypothèse, isomorphe à P1e , le revêtement p′ −1
                                                              s (U ) → U est isotrivial ; nous
                                           k
pouvons don supposer, quitte à faire un nouveau hangement de base S ′′ → S ′ du même
type que pré édemment, que le revêtement U ′ = p′ −1 (U ) → U est trivial. Le revêtement
p′ : Y|U ′ → YU est alors trivial et, par passage aux bres génériques,    haque omposante
       ′

 onnexe de p (Z) = (Y |U ′ )η est isomorphe à Z . Ce i a hève de prouver que le domaine
              −1          ′

k-anoïde p−1 (Z) est potentiellement isomorphe au disque unité.                            2
Corollaire 2.2.12.  Soient C            une S - ourbe et r l'appli ation de rédu tion Cη → Cs ;
pour tout point fermé lisse x e de Cs , l'ouvert r −1 (e
                                                       x) est le réunion d'une suite roissante de
domaines k-anoïdes potentiellement isomorphes au disque unité.
Démonstration. Quitte à rempla er C par C|U , où U est un voisinage ouvert de xe dans Cs ,
on peut supposer qu'il existe un morphisme étale p : C → S(1). La bre Ω de l'appli ation de
rédu tion S(1)η → S(1)s au-dessus du point p(e      x) étant la réunion d'une suite roissante de
domaines k-anoïdes potentiellement isomorphes au disques unité (voir la démonstration de
la proposition 2.2.5), il en est de même pour r −1 (e  x) = p−1 (Ω) d'après le lemme pré édent. 2

Définition 2.2.13.  Pour toute S - ourbe simplement semi-stable X , S(X ) est le fermé
de Xη dont le omplémentaire est la réunion des domaines k-anoïdes potentiellement iso-
morphes au disque unité et ontenus dans Xη − S0 (X ).
                                                                                            37



Lemme 2.2.14.  Pour tout ouvert U             de X et tout morphisme étale p : U → S(a), a ∈
k − {0},
 ◦

                             S(X ) ∩ Uη = S(X|U ) = p−1 S(S(a)).
Démonstration. Soit V ⊂ Xη − S0 (X ) un domaine k-anoïde onnexe et potentiellement
isomorphe au disque unité ; l'image de V est une partie onstru tible et, l'appli ation de
                                                  (0)
rédu tion étant anti- ontinue, onnexe de Xs − Xs , 'est-à-dire un point fermé. L'égalité
S(X ) ∩ Uη = S(X|U ) en dé oule pour tout ouvert U de X .
  La se onde égalité S(X|U ) = p−1 S(S(a)) est une reformulation du lemme 2.2.11.            2
   Étant donnée une S - ourbe simplement semi-stable X , le lemme 2.2.14 permet de travailler
lo alement sur X pour dénir la stru ture de polyèdre entier sur S(X ) et la rétra tion τX →
S(X ).
Proposition 2.2.15.  Soient X           une S - ourbe onnexe et p : X → S(a) un morphisme
étale.
    Si la ourbe Xs est lisse, elle est irrédu tible et S(X ) = S0 (X ).
    Supposons 0 < |a| < 1 ; si la bre de p au-dessus du point singulier de S(a)s est réduite
     à un point, p induit un homéomorphisme de S(X ) sur S(S(a)).
Démonstration. Les omposantes irrédu tibles d'une ek - ourbe lisse oïn idant ave ses om-
posantes onnexes, Xs est irrédu tible si elle lisse. L'image du morphisme ps : Xs → S(a)s
est ontenue dans l'une des omposantes irrédu tibles de S(a)s , déterminant un point ξ ∈
S0 (S(a)) ⊂ S(S(a)), et p−1 (S(S(a))) = p−1 (ξ) = S0 (X ).
   Passons au se ond point de l'énon é.
   La ourbe Xs étant un e  k-s héma ane ( ar quasi- ompa te et étale sur la e   k - ourbe ane
S(a)s ), la bre générique Xη de X est un espa e (stri tement) k-anoïde ; l'espa e topologique
|Xη | est en parti ulier ompa t et l'appli ation ontinue de |Xη | dans |S(a)η | est don propre.
Il sut alors de vérier que p induit une bije tion de p−1 (S(S(a))) sur S(S(a)) ; e sera
automatiquement un homéomorphisme.
   Il s'agit don de prouver que la bre du morphisme p : Xη → S(a)η est réduite à un point
au-dessus de tout x ∈ S(S(a)) ⊂ S(a)η .
  Observons tout d'abord que la démonstration peut se faire après passage à une quel onque
extension non ar himédienne K de k : dans le diagramme ommutatif
                                                   q′
                                       b kK
                                    Xη ⊗                  / Xη

                                       p                        p
                                                           
                                         b kK
                                   S(a)η ⊗         q
                                                        / S(a)η ,


le morphisme q induit un homéomorphisme de S(S(a))K = S(S(a)⊗      b S Spf(K ◦ )) sur S(S(a))
et le morphisme q est surje tif.
                 ′

   Appliquant ette remarque ave K = H(x)  le omplété du orps résiduel de x  nous
pouvons supposer que le point x est de type (2), de groupe des valeurs |H(x)× | = |k× |.
  Soit b ∈ k◦ tel que |T1 (x)| = |b|. Il existe un é latement admissible Y → S(a) et un ouvert
U de Ys tels que
   le S -s héma formel Y|U soit isomorphe à S(b),
   le point x appartienne au bord de S(S(b)) ⊂ S(S(a)),
38



et il est don nalement susant de vérier que les bres de l'appli ation p : S(X ) → S(S(a))
sont réduites à un point au-dessus du bord S0 (S(a)) de S(S(a)), 'est-à-dire qu'il existe une
unique omposante irrédu tible de Xs au-dessus de ha une des deux omposantes irrédu -
tibles de S(a)s .
   Soit x e l'unique point de Xs au-dessus du point singulier de S(a)s . Il passe exa tement
deux omposantes irrédu tibles de Xs par le point x  e et, le lieu singulier de Xs étant réduit
àxe, toutes les autres omposantes irrédu tibles de Xs doivent être lisses et don dénir des
 omposantes onnexes de Xs . La ourbe Xs étant par hypothèse onnexe, elle possède ainsi
exa tement deux omposantes irrédu tibles, passant par le point singulier x   e et dominant les
deux omposantes irrédu tibles de S(a)s . Les bres de l'appli ation p : S(X ) → S(S(a)) sont
don réduites à un point au-dessus du bord S0 (S(a)) de S(S(a)).                             2
   Soit X une S - ourbe simplement semi-stable et onsidérons un re ouvrement U de Xs par
des ouverts onnexes tel que :
    haque U ∈ U ontienne au plus un point singulier de Xs ,
    si U, V ∈ U sont deux ouverts distin ts, U ∩ V ne ontienne au un point singulier de Xs ,
    il existe, pour tout U ∈ U , un morphisme étale pU : X|U → S(a(U )), a(U ) ∈ k◦ − {0}.
                                      
   Étant donné U ∈ U , S(X ) ∩ X|U η = S(X|U ) = p−1  U,η (S(S(a(U )))) ontient les points de
S0 (X) au-dessus des points génériques de U et pU,η réalise un homéomorphisme de S(X ) ∩
 X|U η sur son image dans S(S(a)), laquelle est une fa e de e polytope entier. Il existe par
                                                                   
suite, pour tout ouvert U ∈ U , une unique appli ation τU : X|U η → S(X|U ) telle que le
diagramme

                                              τU
                                      X|U η         / S(X|U )

                                    pU,η                    pU,η
                                                       
                                   S(a(U ))η   τ
                                                    / S(S(a))



soit ommutatif ; pour tout U ∈ U , la restri tion de τU à S(X|U ) est l'identité. Le re ollement
des es appli ations en une rétra tion τX : Xη → S(X ) est immédiat : si U, V ∈ U sont
deux ouverts
           distin ts, U ∩ V est par hypothèse un ouvert irrédu tible disjoint de Sing(Xs )
et X|U ∩V η est envoyé par ha une des rétra tions τU , τV sur le point de S0 (X ) au-dessus du
point générique de U ∩ V .
  Quels que soient les points distin ts x, y ∈ S(X ), des domaines k-anoïdes onnexes V, W ⊂
Xη tels que Γ(V ) = {x} et Γ(W ) = {y} sont né essairement disjoints. Il sut en eet de le
vérier pour les domaines k-anoïdes V ∩ X|U η et W ∩ X|U η , U par ourant U : leurs images
par pU,η sont des domaines k-anoïdes dans S(a(U ))η satisfaisant à la même ondition et la
 on lusion est alors immédiate.
  L'observation pré édente permet de vérier que l'appli ation τX : Xη → S(X ) que l'on vient
de dénir ne dépend pas du hoix des morphismes étales pU : X|U → S(a(U )) : elle induit
en eet l'identité sur S(X ) et, pour tout x ∈ Xη , le point τX (x) de S(X ) est uniquement
déterminé par la ondition intrinsèque suivante : il existe un domaine k-anoïde onnexe
V ⊂ Xη ontenant x et dont τX (x) est l'unique point de Shilov.
                                                                                                            39



Proposition 2.2.16.  Soient X , Y deux S - ourbes simplement semi-stables et f : X →
Y un S -morphisme étale ; le morphisme fη : Xη → Yη envoie S(X ) dans S(Y) et le diagramme
                                                            τX
                                                    Xη                 / S(X )

                                                fη                               fη
                                                                            
                                                    Yη      τY
                                                                       / S(Y)

est ommutatif.
Démonstration. Traitons tout d'abord le         as où Y = S(a), a ∈ k◦ − {0}. L'in lusion
fη (S(X )) ⊂ S(S(a)) dé oule du lemme 2.2.14. Considérons un re ouvrement U de Xs par
des ouverts onnexes U ontenant au plus un point singulier de Xs , deux ouverts distin ts
dans U ayant de plus une interse tion disjointe de Sing(Xs ) ; reprenant la des ription qui
pré ède la proposition, nous pouvons onstruire à partir des artes étales f|U : X|U → S(a)
une rétra tion τX′ : Xη → S(X ) telle que le diagramme
                                                             ′
                                                            τX
                                            Xη                             / S(X )

                                           fη                                        fη
                                                                                
                                        S(a)η                          / S(S(a))
                                                               τ

soit ommutatif, la rétra tion τX étant, elle, dénie à partir de morphismes étales pU : X|U →
S(a(U )), a(U ) ∈ k◦ − {0} ; la ara térisation intrinsèque de la rétra tion τX donnée pré é-
demment implique l'identité τX = τX′ .
   Le as d'une S - ourbe simplement semi-stable Y quel onque se déduit trivialement du as
parti ulier Y = S(a) : onsidérons en eet un re ouvrement U de Ys par des ouverts onnexes
tel que :
    haque ouvert U ∈ U ontienne au plus un point singulier de Ys ,
    deux ouverts distin ts U, V ∈ U aient une interse tion disjointe de Sing(Ys ),
    il existe pour tout U ∈ U un morphisme étale pU : Y|U → S(a(U )), a(U ) ∈ k◦ − {0}.
                          
   Puisque S(Y) ∩ Y|U η = S(Y|U ) = p−1         U,η (S(S(a(U )))) (lemme 2.2.14) et (pU ◦
                                                                    
f )η (S(X )) ⊂ S(S(a(U ))), fη (S(X )) ∩ Y|U η ⊂ S(Y) ∩ Y|U η pour tout U ∈ U et
don fη (S(X )) ⊂ S(Y).
   Dans le diagramme
                                      fη                                       pU,η
                          X|f −1 (U ) η                  / Y|U
                                                               η
                                                                                              / S(a(U ))η

                            τX                            τY                                           τ
                                                                                                 
                         S(X|f −1 (U ) )                 / S(Y|U )
                                                                                 pU,η S(S(a(U )))
                                                                                          /
                                            fη

les égalités
                                     pU,η ◦ fη ◦ τX = τ ◦ pU,η ◦ fη
et
                                           pU,η ◦ τY = τ ◦ pU,η
sont onnues d'après la première partie de la démonstration ; l'appli ation pU,η étant inje tive,
la ommutativité du diagramme en dé oule. En vertu des identités S(X|f −1 (U ) ) = S(X ) ∩
40


                                    
 X|f −1 (U ) η , S(Y|U ) = S(Y) ∩ Y|U η , U ∈ U , le diagramme

                                                         τX
                                                Xη            / S(X )

                                           fη                        fη
                                                                
                                                Yη       τY
                                                              / S(Y)

est également ommutatif.                                                                                  2

2.2.3. Le squelette d'une S - ourbe simplement semi-stable : n.
   Rappelons que, pour tout S -s héma formel plat et lo alement de présentation nie X , Λk (X )
est le sous-groupe du groupe abélien C0 (|Xη |, R) image de l'homomorphisme anonique
                                        ×
                        Γ(X , OX ) ⊗k◦ k → C0 (|Xη |, R), f 7→ log |f |
et Λ(X ) est le sous-groupe engendré par Λk (X ) et R (2.1.1).
  Soit X une S - ourbe simplement semi-stable ; il reste, pour a hever la démonstration du
théorème 2.2.10, à dénir la stru ture de polyèdre entier sur S(X ) et à vérier sa ompatibilité
aux S -morphismes étales.
  Tout e dont nous avons besoin est ontenu dans la proposition suivante.
Proposition 2.2.17.  Soit U un ouvert         onnexe de Xs ren ontrant Sing(Xs ) en au plus
un point ; pour tout morphisme étale p : X|U → S(a), où
    |a| = 1 si U est lisse,
    0 < |a| < 1 si U ontient un point singulier de Xs ,
l'homomorphisme Λ(p) : Λk (S(a)) → Λk (X|U ) est un isomorphisme.
Démonstration. La proposition 2.2.15, jointe à la ondition sur |a|, implique que pη réalise
un homéomorphisme de S(X|U ) sur S(S(a)), identiant S0 (X ) et S0 (S(a)).
  Les bres spé iales Xs et S(a)s étant réduites, |H(x)|× = |k× | pour tout point
x ∈ S0 (X ) ∪ S0 (S(a)).
     Considérons le diagramme ommmutatif
                                          res        / Hom(S0 (S(a)), log |k × |)
                             Λk (S(a))
                              Λ(p)                                        p∗
                                                                 
                                          res         / Hom(S0 (X ), log |k|× ),
                              Λk (X|U )

dans lequelle la è he p∗ est un isomorphisme. La è he Λk (S(a)) → Hom(S0 (S(a)), log |k|× )
est un isomorphisme en vertu du lemme 2.2.1 ; toutes les è hes de e diagramme sont don
des isomorphismes.                                                                        2

Corollaire 2.2.18.  Pour tous a, b ∈ k
                                                          ◦ tels que 0 < |a|, |b| < 1, les points singuliers

des S -s hémas formels S(a) et S(b) ont des voisinages étales isomorphes si et seulement si
|a| = |b|.

     Considérons un re ouvrement U de Xs par des ouverts onnexes tel que :
      haque U ∈ U ontienne au plus un point singulier de Xs ;
      l'interse tion de deux ouverts distin ts U, V ∈ U soit disjointe de Sing(Xs ).
                                                                                             41



  Pour tous U, V ∈ U distin ts, U ∩ V est un ouvert irrédu tible et lisse de Xs , S(XU ∩V ) est
réduit au point de S0 (X ) au-dessus du point générique de U ∩ V et le morphisme de polytopes
                         (S(X|U ∩V ), Λ(X|U ∩V )) ֒→ (S(X|U ), Λ(X|U ))
induit par l'in usion U ∩ V ⊂ U est une immersion anonique de 0-fa e. La olle tion des
(S(X|U ), Λ(X|U )), U ∈ U , est par onséquent un atlas Z-polyédral sur l'espa e topologique
S(X ) et la proposition 2.2.17 garantit que la stru ture de polyèdre entier sur S(X ) ainsi
obtenue ne dépend pas du hoix du re ouvrement ouvert U .
   Le re ouvrement ouvert U de Xs étant de la forme pré édente, l'espa e topologique S(X|U )
est réduit à un point si l'ouvert U est lisse, homéomorphe au segment [0, 1] si U ontient un
point singulier de Xs ; l'espa e topologique S(X ) est don naturellement homéomorphe au
graphe dual de la ek- ourbe nodale Xs et l'appli ation de rédu tion r : Xη → Xs induit, pour
tout point x ∈ S0 (X ), une bije tion du ne tangent Tx S(X ) à S(X ) en ξ sur l'ensemble des
points singuliers de Xs appartenant à la omposante irrédu tible de Xs de point générique
r(ξ).
  Ce polyèdre entier est muni du poids ( f. 1.2.1) déni par l'appli ation
                                                ∼
                           π0 (S(X ) − S0 (X )) −→ Sing(Xs ) → R>0
qui asso ie à la omposante onnexe de S(X ) − S0 (X ) orrespondant à un point singulier x
                                                                                       e
de Xs le nombre entier stri tement positif [κ(e    e
                                              x) : k].
   Le polyèdre entier pondéré d'espa e topologique sous-ja ent S(X ) que l'on vient de dénir
est appelé le squelette de la S - ourbe simplement semi-stable X ; il sera également noté S(X ).
Remarque 2.2.19

  1. Le polyèdre entier S(X ) est l'égalisateur du diagramme
                          `                          /`
                            (U,V )∈U S(X|U ∩V )      / U ∈U S(X|U )
     dans la atégorie des polyèdres entiers.
  2. Tout re ouvrement de Xs par des ouverts onnexes ontenant ha un au plus un des
     points singuliers de Xs dénit une dé omposition élémentaire du polyèdre S(X ) sur
     laquelle le poids est onstant.
  3. Puisque S(X ) s'identie, en tant que polyèdre, au graphe dual de la e  k- ourbe Xs , l'ap-
     pli ation S(X ) → Xs induite par la rédu tion de Xη sur Xs détermine une bije tion entre
     π0 (S(X )) et π0 (Xs ). On en déduit que l'in lusion S(X ) ⊂ Xη induit une bije tion entre
     π0 (S(X )) et π0 (Xη ).

Proposition 2.2.20.  Soient X , Y deux S - ourbes simplement semi-stables et f : X →
Y un morphisme étale. Le morphisme fη : Xη → Yη induit une appli ation de S(X ) dans
S(Y) qui est un isomorphisme G-lo al de polyèdres entiers.
Démonstration. Il a déjà été établi (propostion 2.2.16) que le morphisme fη envoie le fermé
S(X ) de Xη dans le fermé S(Y) de Yη .
   Le résultat dé oule immédiatement de la proposition 2.2.17 lorsque Y = S(a), a ∈ k◦ −{0} :
 onsidérant un re ouvrement U de X par des ouverts onnexes ontenant au plus un point
singulier de Xs , haque morphisme f|U : X|U → S(a) induit un isomorphisme du polytope
                             
entier S(X|U ) = S(X ) ∩ X|U η sur une fa e du polytope entier S(S(a)).
42



  Le as général s'obtient en re ouvrant Ys par des ouverts onnexes U ontenant au plus
un point singulier de Ys et pour lesquels il existe un morphisme étale pU : Y|U → S(a(U )),
a(U ) ∈ k◦ − {0} induisant un isomorphisme entre les polytopes entiers S(X|U ) et S(S(a(u))).
2
     La démonstration du théorème 2.2.10 est maintenant a hevée.
Proposition 2.2.21.  Soit         X une S - ourbe simplement semi-stable ; quelle que
soit l'extension non ar himédienne K/k, le morphisme anonique d'espa es analytiques
p K : Xη ⊗b k K → Xη envoie S(X ×S Spf(K ◦ )) dans S(X ) et l'appli ation induite est un
isomorphisme G-lo al de polyèdres entiers pondérés.
Démonstration. Les deux assertions de l'énon é sont démontrées si elles le sont pour ha une
des S - ourbes X|U , U par ourant un re ouvrement ouvert de Xs ; nous pouvons don supposer
qu'il existe un morphisme étale q : X → S(a) induisant un isomorphisme du polyèdre entier
S(X ) sur S(S(a)). Considérons le diagramme ommutatif
                                                           pK
                                         b kK
                                      Xη ⊗                        / Xη

                                     qη,K                                    qη
                                                                        
                                          b kK
                                    S(a)η ⊗                     / S(a)η ;
                                                           p′K

il a été noté au début de 2.2.1 que le morphisme p′K induit un isomorphisme du polyèdre entier
S(S(a) ×S Spf(K ◦ )) sur S(S(a)), d'où il dé oule que le morphisme pK dénit une appli ation
de S(X ×S Spf(K ◦ )) dans S(X ) qui est un morphisme de polyèdres entiers s'insérant dans le
diagramme ommutatif
                                                           pK
                                S(X ×S Spf(K ◦ ))                             / S(X )

                                    qη,K                                              qη
                                                                                 
                              S(S(a) ×S Spf(K ◦ )) ′                   / S(S(a)).
                                                           pK

Les è hes p′K et qη sont des isomorphismes et, d'après la proposition 2.2.20, la è he qη,K
est un isomorphisme G-lo al ; le morphisme pK : S(X ×S Spf(K ◦ )) → S(X ) est nalement un
isomorphisme G-lo al de polyèdres entiers.
     Nous é rirons S(X )K en lieu et pla e de S(X ×S Spf(K ◦ )).
  Il reste à vérier la ompatibilité ave les poids. Notons r : Xη → Xs et rK : Xη ⊗ b kK →
                
              ◦            e
 X ×S Spf(K ) s = Xs ⊗ek K les appli ations de rédu tion, qui s'insèrent dans le diagramme
 ommutatif :
                                             r
                                   Xη ⊗                e
                                      b k K K / Xs ⊗ e K
                                                     k
                                      pK                               pK
                                                                        e
                                                                  
                                       Xη              r
                                                                / Xs .

Considérons un point ξ de S0 (X ) et un élément t de Tξ S(X ), e dernier orrespondant à
un point singulier x
                   e de Xs ontenu dans la omposante irrédu tible de point générique r(ξ).
Étant donné un voisinage U de x  e dans X et un morphisme étale p : U → S(a), a ∈ k◦ ,
on peut restreindre U de telle sorte que x
                                         e soit l'unique point de la bre p−1 (p(e
                                                                                 x)) ; elle- i
est alors un κ(p(e      e
                 x)) = k-s héma ni et réduit (p est étale), de rang [κ(e     e
                                                                         x) : k]. La bre de
                                                                                                 43



(p ⊗ 1) : U ⊗S Spf(K ◦ ) → S(a) ⊗S Spf(K ◦ ) au-dessus du point singulier est, de même, un
Ke -s héma ni et réduit ; puisqu'il s'identie à p−1 (p(x)) ⊗e K                     x) : e
                                                                e , il est de rang [κ(e
                                                                        k
                                                                                           k] et don

                                                       X
                                    x) : e
                                 [κ(e    k] =                            e
                                                                  x′ ) : K].
                                                               [κ(e
                                                     e′ ∈p−1
                                                     x       e)
                                                          e (x
                                                         K


Cette dernière identité se réé rit sous la forme
                                          X                   X
                            wξ (t) =                                          wξ ′ (t′ ),
                                       ξ ′ ∈p−1       t′ ∈Tξ′ S(X )K ,t′ →t
                                             K (ξ)



  e qui établit que pK est un isomorphisme de polyèdres entiers pondérés ( f. remarque 1.2.3,
2).                                                                                         2
    La notation iK que nous employons dans le lemme suivant a été dénie en 2.1.3 (Extension
des s alaires ). Rappelons que, pour tout point x de X , s(x) est le degré de trans endan e de
             e
l'extension H(x)/  e
                   k ; x est dit de type (2) si et seulement si s(x) = 1.
Lemme 2.2.22.  Soit X         une S - ourbe simplement semi-stable.
   (i ) Étant donné un sous-ensemble ni Σ ⊂ S(X ), il existe une extension non ar himédienne
K/k et un é latement admissible Y → X ×S Spf(K ◦ ) tels que Y soit une Spf(K ◦ )- ourbe
simplement semi-stable et iK (Σ) ⊂ S0 (Y). L'extension K/k peut être hoisie nie (séparable)
si et seulement si tous les points de Σ sont de type (2).
   (ii ) Étant donné un ensemble ni Σ′ de points de type (2) ou (3) dans Xη , il existe une
extension nie (séparable) k′ /k et un é latement admissible Y ′ → X ×S Spf(k′ ◦ ) tels que Y ′
soit une Spf(k′ ◦ )- ourbe simplement semi-stable et ik′ (Σ′ ) ⊂ S(Y ′ ).
Démonstration. Traitons d'abord le as X = S(a).
(i) On peut supposer que l'ensemble Σ est réduit à un point x.
    Considérons une extension non ar himédienne K/k telle que |H(x′ )× | = |K × |, où x′ est le
point de S(S(a))K orrespondant à x dans l'identi ation anonique S(S(a))K = S(S(a)) ;
  ette extension peut être hoisie si (et seulement si) x est de type (2).
    Fixons b ∈ K × tel que |T0 (x′ )| = |b| ; |a| ≤ |b| ≤ 1 et l'é latement sur S ×S Spf(K ◦ ) de
l'Idéal (T0 , b)  inversible en dehors du point singulier de S(a)s  donne lieu à un morphisme
q : Z → S(a) ×S Spf(K ◦ ) tel que Z soit une Spf(K ◦ )- ourbe simplement semi-stable et
S0 (Z) = S0 (S(a)) ∪ {x′ }.
(ii) On peut de nouveau supposer Σ′ réduit à un point x. Si x ∈ S(S(a)), il n'y a rien
à démontrer ; sinon, le point x′ = τ (x) de S(S(a)) est tel que s(x′ ) = 1 et on vient de
prouver qu'il existe une extension nie k′ /k telle que le point de S(S(a))k′ orrespondant à
x′ dans l'identi ation anonique S(S(a))k′ = S(S(a)) appartienne à S0 (S(a) ×S Spf(k′ ◦ )).
On est ainsi ramené au as d'un point x tel que τ (x) ∈ S0 (S(a)). L'appli ation de rédu tion
S(a)η → S(a)s envoie x sur un point lisse x    e appartenant à la omposante irrédu tible de
point générique r(τ (x)).
   Le omplémentaire E de la omposante onnexe non bornée de S(a)η − {x} ⊂ A1k − {x} est
un disque fermé de point de Shilov x. Soit y un point dans E tel que l'extension κ(y)/k soit
nie, de polynme minimal f normalisé de telle sorte que |f (τ (x))| = 1 ; hoisissons également
b ∈ k× tel que |f (x)| > |b|. L'Idéal I sur S(a) tel que Ixe = f OS(a),xe + bOS(a),xe et I = OS(a)
sur S(a)s − {ex} est admissible et son é latement q : Z → S(a) fournit une S - ourbe Z dont
44



la bre spé iale est la somme amalgamée du diagramme

                                          P1e
                                              Ok
                                          0

                                        Spec(e
                                             k)         e
                                                        x
                                                            / S(a)s ,

qui devient simplement semi-stable après une extension nie k′ /k et telle que S(Z ×S Spf(k′ ◦ )
 ontienne le sous-ensemble ik′ (x).
   Le as d'une ourbe simplement semi-stable quel onque se déduit dire tement de e qui
pré ède. On peut en eet supposer que X est munie d'un morphisme étale p : X → S(a) ar
la question est lo ale sur Xη .
   Étant donnée une extension non-ar himédienne (resp. une extension nie) K/k telle
qu'il existe un é latement admissible q : Z → S(a) ×S Spf(K ◦ ) satisfaisant à la ondition
iK (pη (Σ)) ⊂ S0 (Z) (resp. iK (Σ) ⊂ S(Z)), l'é latement admissible q ′ : Y → X ×S Spf(K ◦ )
déni par le diagramme artésien
                                          q′
                                    Y               / X ×S Spf(K ◦ )

                                                                 p
                                                            
                                    Z              / S(a) ×S Spf(K ◦ )
                                              q

fournit une S - ourbe simplement semi-stable Y telle que iK (Σ) ⊂ S0 (Y) (resp. iK (Σ) ⊂
S(Z ′ )).
  L'extension K/k peut être hoisie nie si tous les points de pη (Σ) sont de type (2), don si
tous les points de Σ sont de type (2).
     Toutes les extensions nies peuvent être hoisies séparables.                             2
   La proposition suivante sera utilisée au hapitre 3 ( f. théorème 3.2.10).
Proposition 2.2.23.  Soit Y un espa e k -anoïde rig-lisse de dimension 1. Toute om-
posante onnexe Ω de Int(Y ) et la réunion d'une suite de domaines k-anoïdes telle que, pour
tout n :
- Vn ⊂ Vn+1 − ∂Vn+1 ;
- la frontière de haque omposante onnexe de Vn+1 − Vn ne ren ontre Vn (resp. Vn+1 ) qu'en
un seul point.
Démonstration. Si l'on dispose d'une telle suite après une extension non ar himédienne
K/k, son image par la proje tion anonique p : Y ⊗ b k K → Y satisfait aux onditions imposées
 ar p(∂(V ⊗ b k K)) = ∂V pour tout domaine k-anoïde V ([3℄, proposition 3.1.3, (iv)). Nous
pouvons don supposer que Y est un domaine sri tement k-anoïde, bre générique d'une
S - ourbe simplement semi-stable Y .
   La omposante onnexe Ω de Y = Yη est l'image ré iproque par l'appli ation de rédu tion
r : Yη → Ys d'un sous-s héma fermé (réduit) Z de Ys , propre sur e   k et onnexe. Les points
de ∂Ω sont en bije tion ave l'ensemble des points génériques des omposantes irrédu tibles
anes de Ys ren ontrant Z .
   L'interse tion Ω ∩ S(Y) est un ouvert de S(Y). Elle est vide si et seulement si Z est un
point fermé lisse de Ys et la on lusion est dans e as immédiate puisque Ω est la réunion
d'une suite roissante de domaines stri tement k-anoïdes ayant un unique point de Shilov
                                                                                                  45



( orollaire 2.2.12). Si Ω ∩ S(Y) est non vide, il dé oule immédiatement de la onstru tion de
S(Y)) que
                                      Ω = τ −1 (Ω ∩ S(Y));
il ne reste alors plus qu'à dénir les domaines k-anoïdes désirés par :
                                          Vn = τ −1 (Sn ),
où (Sn ) est une suite roissante de domaines polyédraux ompa ts de réunion S telle que, pour
tout n, les omposantes onnexes de Sn+1 − Sn soient des polytopes entiers de dimension 1.
2

2.2.4. Polygones de Newton généralisés
   La notion lassique de polygone de Newton d'une série de Laurent à oe ients dans k per-
met l'étude des fon tions holomorphes sur les ouronnes {r ≤ |T1 | ≤ R} ⊂ Gmk , 0 < r < R,
lesquelles sont essentiellement les bres génériques des S - ourbes S(a) ( f. [Man℄, hapter 1,
par exemple). La onstru tion du squelette d'une S - ourbe simplement semi-stable X fournit
le adre d'une généralisation évidente pour les éléments f de Γ(Xη , OXη ), ledit polygone de
Newton n'étant autre que le graphe de la fon tion réelle log |f ||S(X ) .

Proposition 2.2.24.  Soient X une S - ourbe simplement semi-stable, de bre générique
X = Xη , et f une se tion globale de OX , inversible sur un ouvert dense de X .
   (i ) La restri tion F de la fon tion log |f | à S(X ) ⊂ X est ane par mor eaux : F ∈
A0Z (S(X )).
   (ii ) Pour tout point x ∈ S(X ), log |f | ≤ F (x) sur τX−1 (x), ave égalité si et seulement si f
ne s'annule pas sur τX−1 (x) ; ainsi, la fon tion F ◦ τX majore log |f | sur X , et il y a égalité si
et seulement si f ∈ Γ(X, OX )× .
   (iii ) Pour tout x ∈ S(X ) − ∂X , le oe ient de δx dans ddc F est le degré du diviseur
div(f )|τ −1 (x) ; la mesure induite par ddc F sur S(X )−∂X est don positive et F est harmonique
        X
sur S(X ) − ∂X si et seulement si f est inversible sur l'ouvert τ −1 (S(X ) − ∂X) de X .
Démonstration. Observons tout d'abord que la fon tion log |f | prend des valeurs nies sur
S(X ) ⊂ X : en eet, f étant génériquement inversible, elle ne peut s'annuler qu'en des points
x ∈ X tels que |κ(x) : k] < ∞ et la on lusion dé oule de e que l'extension κ(x)/k est
trans endante pour tout point x ∈ S(X ).
   Le support du diviseur de f étant un fermé lo alement ni de X , son image Σ par l'appli-
  ation propre τX est un fermé lo alement ni de S(X ) tel que s(x) = 1 pour tout x ∈ Σ ;
il existe alors, par appli ation du lemme 2.2.22, une extension nie k′ /k et un é latement
admissible q : Y → X ×S Spf(k′ ◦ ) tel que Y soit une Spf(k′ ◦ )- ourbe simplement semi-stable
et q −1 (Σ) ⊂ S0 (Y). Posons S ′ = Spf(k′ ◦ ) ; le morphisme anonique p : Xη ⊗k k′ → Xη induit
un isomorphisme G-lo al entre les poyèdres entiers pondérés S(X ×S S ′ ) et S(X ) (proposition
2.2.21) et
                                       ddc F = p∗ ddc p∗ F
(remarque 1.2.8, 4). Il est don susant de démontrer la proposition pour p∗ f ∈ Γ(X ⊗k
k′ , OX⊗k k′ ), e qui permet de supposer que Σ est ontenu dans S0 (X ) ou, de manière équiva-
lente, que l'image du support de div(f ) par l'appli ation de rédu tion X → Xs est disjointe
du lieu singulier Sing(Xs ) de Xs .
  Soit, pour tout point x e ∈ Sing(Xs ), Uxe un voisinage ouvert onnexe de x      e dans
Xs − r(|div(f )|) tel que U − {e
                               x} soit lisse ; f étant inversible sur ha un des domaines
46



k-anoïdes r −1 (Uxe ), F|S(X )∩r−1 (U ) ∈ Λk (X|U ) d'après le lemme 2.2.22 et le point (i) est
démontré.
   Pour tout x ∈ S(X ), τX−1 (x) est un domaine k-anoïde dont x est l'unique point de Shilov.
La restri tion de f à τX−1 (x) atteint son maximum au point x, d'où l'inégalité log |f | ≤
log |f (x)| = F (x) sur τX−1 (x) ; appliquant le même raisonnement à f −1 , on obtient l'égalité
log |f | = F (x) si f est inversible sur τX−1 (x). Ré iproquement, puisque f ne peut s'annuler
aux points de S(X ), |div(f )| ∩ τX−1 (x) = ∅ si log |f | = F (x) sur τX−1 (x) et fτ −1 (x) est alors
                                                                                     X
inversible ; le point (ii) est démontré.
   Étant donnés un point ξ ∈ S0 (X ) et α ∈ k× tel que |α| = |f (ξ)|, α−1 f est inversible au
voisinage de ξ dans X et don induit une fon tion méromorphe régulière feξ sur la omposante
irrédu tible Z[ξ] de Xs de point générique r(ξ). Elle est indépendante du hoix de α et son
diviseur des ples est lo alisé dans Sing(Xs ) puisque |f | ≤ |α| sur τX (ξ). Quel que soit l'élément
t de Tξ S(X ) orrespondant à un point singulier x    e de Xs ontenu dans Z[ξ],

                                        λξ,t(F ) = −ordxe (feξ )
(lemme 2.2.25 i-dessous) et, vu la dénition du poids dont est muni S(X ) (2.2.3),
                              X  X                           
                 ddc F =                       λξ,t (F )wξ (t) δξ
                                ξ∈S0 (X )        t∈Tξ S(X )
                                  X                X                                
                            =                                          eξ
                                                              (−ordxe (f ))[κ(e    e
                                                                              x) : k] δξ .
                                ξ∈S0 (X )        e∈Xs ∩Z[ξ]
                                                 x


Le oe ient de −δξ dans ddc F est don le degré de la omposante du diviseur de feξ ontenue
dans Sing(Xs ). La ek- ourbe Z[ξ] est propre si et seulement si ξ ∈ S0 (X ) − ∂X ; par suite,
pour tout point ξ ∈ S0 (X ) − ∂X , le oe ient de δξ dans ddc F n'est autre que le degré
de la omposante du diviseur de feξ ontenu dans Xs − Sing(Xs ). C'est également le degré
de la omposante de div(f ) ontenu dans le domaine k-anoïde τX−1 (x). En eet, si Z[ξ]′
est l'ouvert Z[ξ] − (Sing(Xs ) ∩ Z[ξ]) (remarquer que Z[ξ] ren ontre les autres omposantes
irrédu tibles de Xs en des points singuliers de Xs ) et si α ∈ k× est hoisi tel que |α| = |f (ξ)|,
α−1 f appartient à la sous-k◦ -algèbre Γ(Z[ξ]′ , OX ) de Γ(Z[ξ]′ , OX ) ⊗k◦ k (proposition 2.1.1)
et le sous-s héma fermé V (α−1 f ) de X|Z[ξ]′ est l'adhéren e de div(f ) ∩ τX−1 (ξ) dans X ; 'est
don un S -s héma ni et plat, d'où dé oule l'identité
                                              
                        deg div(f ) ∩ τX−1 (ξ) = deg(div(feξ ) ∩ Z[ξ]′ ).
  Cela garantit la positivité de ddc F sur S(X )−∂X et établit l'équivalen e entre l'inversibilité
de f sur τX−1 (S(X ) − ∂X) et l'harmoni ité de F sur S(X ) − ∂X .                               2
Lemme 2.2.25.  Soient X         une S - ourbe simplement semi-stable onnexe dont la bre
spé iale possède un unique point singulier xe, X = Xη sa bre générique et f un élément de
Γ(X, OX )× ; notons F la restri tion à S(X ) ⊂ X de la fon tion log |f |.
   Soient ξ un point dans S0(X ) = ∂S(X ) et Z[ξ] la omposante irrédu tible de Xs orrespon-
dante ; étant donné α ∈ k× tel que |f (ξ)| = |α|, α−1 f est inversible au voisinage de ξ dans X
et induit une fon tion méromorphe régulière feξ sur Z[ξ], indépendante du hoix de α.
     La fon tion F appartient à Λk (X ) et
                                            λξ (F ) = −ordxe(feξ ).
                                                                                               47



Démonstration. Quitte à restreindre U , on peut supposer qu'il existe un morphisme étale
surje tif p : X → S(a), a ∈ k◦ − {0}, induisant un isomorphisme entre S(X ) et S(S(a)) =
Spf(k◦ {T0 , T1 }/(T0 T1 − a)) ; on peut également supposer que p∗ T0 est une équation de Z[ξ]
dans X , auquel as p∗ T1−1 est un paramètre lo al en x       e sur Z[ξ]. L'élément F de Λk (X ) =
log |k× | ⊕ Z log |p∗ T1 | s'é rit
                                    F = log |f |(ξ) + n log |p∗ T1 |
et, si α ∈ k× est hoisi tel que |α| = |f (ξ)|, la se tion α−1 f p∗ T1−n de OX     ×
                                                                                    est de module
 onstant égal à 1 sur X et appartient don à Γ(X , OX ) (proposition 2.1.1). Il en dé oule
                                                               ×
                                                     ×
en parti ulier l'appartenan e de α−1 f à p∗ T1n OZ[ξ]    et don , p∗ T1−1 dénissant un paramètre
lo al en xe sur Z[ξ], l'égalité
                                     λξ (F ) = n = −ordxe(feξ ).
                                                                                                2
2.2.5. Morphismes entre S - ourbes semi-stables.
   Le ouple (S(X ), τX ) asso ié à une S - ourbe simplement semi-stable dépend (en général)
du S -s héma formel X et non pas seulement de l'espa e k-analytique Xη ; la situation est
toutefois assez fa ile à analyser.
Proposition 2.2.26.  Soient X une S - ourbe simplement semi-stable et q : Y → X un
é latement admissible tel que Y soit une S - ourbe simplement semi-stable.
   (i ) L'isomorphisme qη−1 de Xη sur Yη identie S(X ) à un domaine polyédral dans S(Y).
   (ii ) L'appli ation S(q) = τX ◦ qη |S(Y) est une rétra tion de S(Y) sur S(X ) s'insérant dans
le diagramme ommutatif
                                                    τY
                                         Yη               / S(Y)

                                       qη                         S(q)
                                                             
                                        Xη          τX
                                                          / S(X ).

   (iii ) Soit V une omposante onnexe de S(Y) − S(X ) ; son adhéren e V dans S(Y) est un
polyèdre entier ompa t dont la frontière V ∩ S(X ) est réduite à un point.
   (iv ) Quelle que soit la fon tion Φ ∈ A0 (S(X )), S(q)∗ Φ ∈ A0 (S(Y)) et
                                  ddc Φ = S(q)∗ (ddc S(q)∗ Φ).
Démonstration. Les espa es k-analytiques Yη et Xη sont identiés via l'isomorphisme qη .
(i) Le sous-ensemble Σ = S0 (Y) ∩ S(X ) de S(X ) ontient S0 (X ) ( ar qs est dominant) et
est onstitué de points x tels que |κ(x)× | = |k× | ; il existe par onséquent un é latement
admissible p : Z → X tel que Z soit une S - ourbe simplement semi-stable, S(Z) = S(X ) et
S0 (Z) = Σ ; la proposition 2.1.15 implique alors la fa torisation du morphisme q à travers p :
                                                Y@
                                                   @@ q
                                                     @@
                                                u      @@
                                                        @
                                                Z         / X,
                                                      p

u étant un é latement admissible induisant un isomorphisme au-dessus d'un voisinage ouvert
de Sing(Zs )  ar au une omposante irrédu tible de Ys ne ren ontre u−1 (Sing(Zs ))  et
identiant Zs à son transformé stri t dans Ys . Il est maintenant évident que S(X ) = S(Z) est
un domaine polyédral dans S(Y) : ayant hoisi, pour tout point ye ∈ Sing(Ys ), un voisinage
ouvert onnexe Uye tel que Uye −{e
                                y} soit lisse, S(Y) est obtenu en re ollant à S0 (Y) les polytopes
48



entiers S(Y|Uye ), ye ∈ Sing(Ys ), tandis que S(Z) est obtenu en re ollant à S0 (Z) ⊂ S0 (Y) les
polytopes entiers S(Y|Uye ), ye ∈ Sing(Zs ) ⊂ Sing(Ys ).
(ii) Soit Z ′ le s héma formel induit par Z sur l'ouvert Zs′ = Zs − Sing(Zs ) ; 'est une S - ourbe
lisse de squelette S0 (Z) et dont la bre générique ontient S(Y)−S(Z). L'appli ation τX envoie
 ha une des omposantes onnexes de Zη′ ⊂ Xη sur le point de S0 (Z) qu'elle ontient et elle
rétra te le polyèdre S(Y) sur le domaine polyédral S(Z) ; la ommutativité du diagramme
                                                    uη                      pη
                                     Yη                   / Zη                        / Xη

                                   τY                    τZ                                 τX
                                                                                      
                                   S(Y)             uη
                                                         / S(Z)                       S(X )

est évidente.
(iii) Les bres du morphisme u sont onnexes puisqu'il s'agit de l'é latement d'un Idéal (ad-
missible) sur Z inversible en dehors d'un fermé ontenu dans le lieu lisse Z ′ . Soit Z ′′ la réunion
des omposantes onnexes de Zs′ qui ren ontrent Sing(Ys ). Comme on peut le onstater sur la
des ription du domaine polyédral S(Z) ⊂ S(Y) donnée en (i), l'adhéren e de S(Y)−S(Z) dans
S(Y) s'identie anoniquement au squelette de la S - ourbe simplement semi-stable u−1 (Z ′′ ),
dont les omposantes onnexes sont en bije tion ave l'ensemble des points génériques de Zs′′ ;
il en dé oule que haque omposante onnexe de S(Y) − S(Z) est adhérente à un et un seul
point dans S0 (Z ′′ ) ⊂ S0 (Z), qui n'est autre que son image par la rétra tion τX .
(iv) Quels que soient le point x ∈ S(X ) et l'élément t ∈ Tx S(Y), orrespondant à un germe
de omposante onnexe c de S(Y) en x,
                           
                             0         si c est ontenue dans S(Y) − S(X );
                λx,t (Φ) =
                             λx,t (Φ) si c est ontenue dans S(X );

l'égalité
                                     ddc Φ = S(q)∗ (ddc S(q)∗ Φ)
en dé oule immédiatement.                                                                            2
Proposition 2.2.27.  Soient X , Y deux S - ourbes simplement semi-stables et f : Xη →
Yη un morphisme quasi-ni. Il existe une extension nie séparable k′ /k et un é latement
admissible q : X ′ → X ×S S ′ , S ′ = Spf(k′ ◦ ), tels que
  (i ) X ′ soit une S - ourbe simplement semi-stable et le morphisme f ′ = f ⊗ 1 : Xη ⊗k k′ →
Yη ⊗k k′ se prolonge en un Spf(S ′ )-morphisme f ′ : X ′ → Y ′ , où Y ′ = Y ×S Spf(S ′ )
  (ii ) l'appli ation S(f ′ ) = τY ′ ◦ f|S(X ′ ) de S(X ′ ) dans S(Y ′ ) soit un morphisme de polyèdres
entiers,
  (iii ) le diagramme
                                                          ′
                                                         τX
                                            Xη′                     / S(X ′ )

                                            f                               S(f ′ )
                                                                       
                                            Yη′          τY ′
                                                                    / S(Y ′ )

soit ommutatif.
                                                                                                  49



  Dans es onditions :
  (iv ) pour tout point x ∈ S(X ′ ) − ∂Xη′ et toute fon tion Φ ∈ A0 (S(Y ′ )),
                          Z                              Z
                                   c   ′ ∗             ′
                              dd S(f ) Φ = (degx f )            ddc Φ.
                             {x}                                      {f ′ (x)}

Démonstration.
(i) Tous les points du sous-ensemble Σ = f −1 (S0 (Y)) de Xη sont de type (2) ( ar f est quasi-
ni) et, par appli ation du lemme 2.2.22, il existe une extension nie k′ /k et un é latement
admissible q : X ′ → X ×S S ′ , ave S ′ = Spf(k′ ◦ ), tels que X ′ soit une S - ourbe simplement
semi-stable et p−1
                 k ′ (Σ) ⊂ S0 (X ). Sous es onditions, la proposition 2.1.15 montre que le
                                 ′

morphisme f = f ⊗ 1 : Xη = Xη ⊗k k′ → Yη ⊗k k′ se prolonge en un S ′ -morphisme f : X ′ →
              ′            ′

Y ′ = Y ×S S ′ .
  Nous notons dorénavant X , Y , f et f en lieu et pla e de X ′ , Y ′ , f ′ et f ′ respe tivement.
(ii) Considérons deux points x ∈ Sing(Xs ), y ∈ Sing(Ys ) tels que f (x) = y et soient U ⊂ Xs ,
V ⊂ Ys des voisinages ouverts anes onnexes de x, y respe tivement tels que U − {x} et
V − {y} soient lisses. Par onstru tion des polyèdres entiers S(X ) et S(Y),
                                                               
                  S(X ) ∩ X|U η = S(X|U ) et S(Y) ∩ Y|V η = S(Y|V )

sont des polytopes entiers, de groupes stru turaux Λ(X|U ) et Λ(Y|V ) respe tivement. Il nous
faut nous assurer que, pour toute fon tion ϕ ∈ Λ(Y|V ), la fon tion S(f )∗ ϕ sur S(X|U ) appar-
tient à Λ(X|U ) ; e i est ontenu dans la formule
                                        S(f )∗ ϕ = Λ(f )(ϕ),
où Λ(f ) est l'homomorphisme de Λ(Y|V ) dans Λ(X|U ) induit par le morphisme f : X|U → Y|V
(2.1.1). La véri ation en est fa ile :
    il n'y a rien à dire si ϕ est onstante ;
    si la fon tion ϕ appartient au sous-groupe Λk (Y|V ) de Λ(Y|V ), elle est de la forme − log |u|,
                              ×
     u ∈ Γ(Y|V , OY ) ⊗k◦ k , et alors
                                                                  
                          S(f )∗ ϕ = f ∗ τY∗ ϕ |S(X ) = f ∗ log |u| |S(X )
                                    = log |f ∗ u||S(X )
                                    = Λ(f )(ϕ).

(iii) L'appli ation S(f ) : S(X ) → S(Y) étant par dénition la omposée τY ◦ f|S(X ) , le dia-
gramme
                                                 τX
                                         Xη           / S(X )

                                         f                    S(f )
                                                         
                                          Yη     τY
                                                      / S(Y)

est ommutatif si et seulement si l'appli ation τY ◦f est onstante sur les bres de la rétra tion
τX .                                                                                       
    Soit Ω l'ouvert Ys − Sing(Ys ) ; la rétra tion τY étant lo alement onstante sur Y|Ω η et
                                                                                               
     à valeurs dans S0 (Y), τY ◦ f est onstantes sur les bres de τY au-dessus de S Y|f −1 (Ω)
     puisque es dernières sont onnexes.
50



      Soient y un point dans Sing(Ys ) et V un voisinage ane onnexe de y dans Ys tel que
       V − {y} soit lisse. Étant donnée une fon tion ϕ ∈ Λ(Y|V ), la fon tion f ∗ ϕ = Λ(f )(ϕ)
       appartient à Λ(X|f −1 (V ) ) ; elle est don onstante sur les bres de τX . Comme
                                        f ∗ ϕ = (τY ◦ f )∗ ϕ|S(Y)
       et que les éléments de Λ(Y|V ) séparent les points de S(Y|V ), ela établit que l'appli ation
                                                                          
       τY ◦ f est onstante sur les bres de τX au-dessus de S X|f −1 (V ) .
(iv) Traitons tout d'abord le as d'un point x ∈ S(X ) appartenant à S0 (X ).
   Quitte à ee tuer un é latement admissible sur Y , on peut supposer que le point y ap-
partient à S0 (Y). Notons Cx (resp. Cy ) la omposante irrédu tible de Xs (resp. Ys ) de point
générique rX (x) (resp. rY (y)).
   Le morphisme f s : Xs → Ys induit un morphisme quasi-ni et dominant de Cx dans Cy et
l'homomorphisme orrespondant κ(rY (y)) → κ(rX (x)) entre les orps de fon tions oïn ide
ave elui provenant de l'homomorphisme H(y) → H(x), déni par f , via les identi ations
  anoniques
                             ] = κ(rX (x)),
                            H(x)                 ] = κ(rY (y))
                                                H(y)
                                          / ∂Xη est équivalente à la propreté de la e
(proposition 2.1.2, (iii)). L'hypothèse x ∈                                         k- ourbe
algébrique Cx ; il en est alors de même pour la ourbe Cy et le morphisme induit par f s de
Cx dans Cy est ni, de degré
                              ] : H(y)]
                             [H(x) ] = [H(x) : H(y)] = deg f
                                                          x

(l'extension H(x)/H(y) est non ramiée puisque, les S - ourbes X , Y étant simplement semi-
stables, |H(y)× | = |k× | = |H(x)× |).
   Soit p un point singulier de Ys appartenant à Cy ; à p orrespond un sous-polytope entier
P de S(Y) tel que y ∈ ∂P et on note t la fon tion ane positive sur P qui s'annule en x et
engendre le groupe abélien Λ(P )/R. Notons ep′ (f ) l'indi e de ramid ation de f en un point
fermé p′ de Cx .
   Nous avons d'une part
                                          ep′ (f ) = 1
pour tout point fermé ξ ′ ∈ Cx ∩ (Xs − Sing(Xs )) : il passe en eet né essairement deux
 omposantes irrédu tibles distin tes de Xs par tout point de Cx au-dessus d'un point de
Cy ∩ Sing(Ys ).
  D'autre part, la dénition de la stru ture entière sur S(X ) est telle que
                                        λx,p′ (S(f )∗ t) = ep′ (f )
pour tout point p′ ∈ Cx ∩ Sing(Xs ).
  Nous en déduisons :
                Z                              X
                    ddc S(f )∗ t =                           λx,p′ (S(f )∗ t)[κ(p′ ) : e
                                                                                       k]
                    {x}                  p′ ∈Cx ∩Sing(Xs )
                                               X
                                    =                        ep′ (f )[κ(p′ ) : κ(p)][κ(ξ) : e
                                                                                            k]
                                         p′ ∈Cx ∩Sing(Xs )

                                    = (deg (f |Cx ))[κ(p) : e
                                                            k]
                                                Z
                                    = (degx f )      ddc t
                                                      {y}
                                                                                               51



et l'égalité
                            Z                               Z
                                     c      ∗
                                   dd S(f ) Φ = (degx f )                 ddc Φ
                             {x}                                {f (x)}

pour toute fon tion Φ ∈ A0 (S(Y)) s'en déduit immédiatement par linéarité.
```

## Thuillier, newline lines 3226--3765

```text
    Le as général se déduit du pré édent en appliquant la proposition 2.2.21 et le lemme 2.2.22.
2


                                   2.3. Fon tions harmoniques
2.3.1. L'espa e H(X ).
   Étant donnée une S - ourbe X , le bord de l'espa e k-analytique Xη (2.1.2) est le sous-
ensemble ∂Xη de S0 (X ) formé des points au-dessus des points génériques des omposantes
irrédu tibles anes de Xs .
Définition 2.3.1.  Soit X une S - ourbe simplement semi-stable ; le sous-espa e ve toriel

                                           τX∗ H(S(X ), ∂Xη )
de C0 (|Xη |, R) est noté H(X ).

   Nous nous restreindrons, dans e qui suit, à la onsidération de S - ourbes simplement
simplement semi-stables X qui sont quasi- ompa tes ; ette hypothèse équivaut à la ompa ité
de l'espa e topologique |Xη |.
Proposition 2.3.2
  (i ) Lorsque la e
                  k- ourbe Xs est propre, H(X ) est l'espa e des fon tions réelles lo alement
 onstantes sur Xη .
  (ii ) Lorsque ∂Xη ren ontre haque omposante onnexe de |Xη |, l'appli ation de restri tion
                                         H(X ) → Hom(∂Xη , R)
est bije tive.
Démonstration.
(i) Si la e
          k- ourbe Xs est propre, l'ensemble ∂Xη est vide ; l'assertion dé oule don du orollaire
1.2.11.
(ii) Si l'ensemble ∂Xη ren ontre ha une des omposantes onnexes de |Xη |, il ren ontre éga-
lement haque omposante onnexe de S(X ) (remarque 2.2.19,3) et l'assertion dé oule de la
proposition 1.2.15.                                                                           2

    Comme annon é en introdu tion de e hapitre, nous allons établir le résultat suivant.
Proposition 2.3.3.  Soient X , X
                                       ′ deux S - ourbes simplement semi-stables et f : X ′ →
                                                                                             η
Xη un morphisme quasi-ni. L'appli ation R-linéaire f ∗ : C0 (|Xη |, R) → C0 (|Xη′ |, R) envoie le
sous-espa e H(X ) dans le sous-espa e H(X ′ ).
Démonstration. Vu la proposition 2.2.26, le résultat s'obtient en ombinant les trois lemmes
suivants.                                                                                       2
Lemme 2.3.4.  Soient X         une S - ourbe simplement semi-stable et q : Y → X un é late-
ment admissible tel que Y soit une S - ourbe simplement simplement semi-stable ; l'isomor-
                            ∼
phisme qη∗ : C0 (|Xη |, R) −→ C0 (|Yη |, R) identie les sous-espa es H(X ) et H(Y).
52



Démonstration. L'isomorphisme qη identie ∂Yη et ∂Xη .
  D'après la proposition 2.2.26, le polyèdre entier S(X ) s'identie à un domaine polyédral
dans le polyèdre entier S(Y) tel que, posant S(q) = τX ◦ qη |S(Y) , le diagramme
                                                    τY
                                           Yη            / S(Y)

                                       qη                           S(q)
                                                               
                                           Xη       τX
                                                         / S(X )

soit ommutatif, haque omposante onnexe de S(Y) − S(X ) ne ren ontre S(X ) qu'en un
seul point et l'appli ation S(q) soit la rétra tion envoyant ha une de es omposantes sur le
point orrespondant de S(X ).
   Les espa es k-analytiques Yη et Xη sont identiés via l'isomorphisme qη ; on déduit du
diagramme ommutatif pré édent que, pour toute fon tion F sur S(X ), la fon tion f = F ◦τX
sur Xη = Yη se fa torise par τX sous la forme :
                                     f = (F ◦ S(q)) ◦ τY .
L'appli ation linéaire
                              S(q)∗ : A0 (S(X )) → A0 (S(Y))
induisant un isomorphisme de H(S(X ), ∂Xη ) sur H(S(Y), ∂Yη ) (proposition 1.2.20), il en
résulte que l'isomorphisme anonique de C0 (|Xη |, R) sur C0 (|Yη |, R) envoie le sous-espa e
H(X ) dans H(Y) et induit un isomorphisme de l'un sur l'autre.                            2
Lemme 2.3.5.  Soient X         une S - ourbe simplement semi-stable (quasi- ompa te ) et K/k
une extension non-ar himédienne ; une fon tion h ∈ C0 (|Xη |, R) appartient au sous-espa e
H(X ) si et seulement si la fon tion p∗K h appartient au sous-espa e H(X ×S Spf(K ◦ )).
Démonstration. Le morphisme anonique pK : Xη ⊗            b k K → Xη induit un isomorphisme
G-lo al surje tif S(X )K → S(X ) de polyèdres entiers pondérés (proposition 2.2.21) et, les
 omposantes irrédu tibles anes de la K   e - ourbe Xs ⊗e K   e étant les images ré iproques des
                                                           k
                                                             −1
 omposantes irrédu tibles anes de Xs , ∂(Xη ⊗  b k K) = pK (∂Xη )) ∩ S0 (X ×S Spf(K ◦ )). Ce i
implique, pour tout fon tion Φ ∈ A (S(X )), que la fon tion p∗K Φ appartient à A0 (S(X )K ) et
                                     0

que le support de la mesure ddc Φ = (pK )∗ ddc p∗K Φ est ontenu dans ∂Xη si et seulement si
 elui de la mesure ddc p∗K Φ est ontenu dans ∂(Xη ⊗  b k K).                                  2
Lemme 2.3.6.  Soient X , Y deux S - ourbes simplement semi-stables et f : Yη → Xη un
morphisme quasi-ni ; l'homomorphisme f ∗ : C0 (|Yη |, R) → C0 (|Xη |, R) envoie le sous-espa e
H(Y) dans H(X ).
Démonstration. Appliquant la proposition 2.2.27 et les deux lemmes pré édents, on peut
supposer que f induit un morphisme de Y dans X . On a alors un diagramme ommutatif
                                                    τX
                                       Xη                / S(X )

                                       f                            S(f )
                                                           
                                       Yη           τY
                                                         / S(Y),

où S(f ) = τY ◦ f est un morphisme de polyèdres entiers.
  Étant donnée une fon tion H dans H(S(Y), ∂Yη ),
                                  f ∗ (H ◦ τY ) = S(f )∗ H ◦ τX
                                                                                                53



et S(f )∗ H ∈ A0 (S(X )). Il reste à vérier que la fon tion S(f )∗ H est harmonique sur S(X ) −
∂Xη . C'est une onséquen e dire te du point (iv) de la proposition 2.2.27 : f (x) ∈ / ∂Yη pour
tout point x ∈ S(X ) − ∂Xη et
                         Z                              Z
                               ddc S(f )∗ H = (degx f )       ddc H = 0.
                          {x}                             {f (x)}
                                                                                                 2
  Si X est un espa e stri tement k-anoïde et ϕ : X → ˜ Xη est un isomorphisme de X sur la
bre générique d'une S - ourbe simplement semi-stable X , le sous-espa e ve toriel réel ϕ∗ H(X )
de C0 (|X|, R) ne dépend pas du hoix de X et de ϕ ; il est noté H(X).
   De manière générale, étant donnés un espa e k-analytique X et une lture algébrique ka de
k, le groupe de Galois G de la fermeture séparable ksep de k dans ka opère par automorphismes
sur l'espa e c                b kc
             ka -analytique X ⊗  ka . On dispose d'un morphisme G-équivariant anonique
                                          p : X⊗  ca → X
                                               b kk
d'espa es analytiques et l'appli ation ontinue sous-ja ente est un quotient de |X ⊗        ca | par
                                                                                        b kk
l'a tion de G dans la atégorie des espa es topologiques : 'est en eet un quotient dans la
  atégorie des ensembles d'après le orollaire 1.3.6 de [3℄ et l'appli ation ontinue p est ouverte.
Proposition 2.3.7.  Quelles que soient la S - ourbe simplement semi-stable X et l'ex-
tension nie galoisienne k′ /k, l'a tion du groupe G = Gal(k′ /k) sur C0 (|Xη ⊗k k′ |, R) stabilise
le sous-espa e H(Xη ) et l'isomorphisme anonique
                                 C0 (|Xη |, R) → C0 (|Xη ⊗k k′ |, R)G
induit un isomorphisme de H(Xη ) sur H(Xη ⊗k k′ )G .
Démonstration. On peut supposer Xη onnexe.
   Si Xη est propre, H(Xη ) (resp. H(Xη ⊗k k′ )) est l'espa e des fon tions onstantes sur Xη
(resp. lo alement onstantes sur Xη ⊗k k′ ) (proposition 2.3.2, 1) et l'assertion est évidente.
   Si Xη n'est pas propre, alors il en est de même pour haque omposante onnexe de Xη ⊗k k′
et, d'après la proposition 2.3.2,2, les restri tions
                                      H(Xη ) → Hom(∂Xη , R)
et
                                H(Xη ⊗k k′ ) → Hom(∂(Xη ⊗k k′ , R)
sont bije tives. L'assertion résulte ainsi de l'identité ∂Xη = ∂(Xη ⊗k k′ )G .                   2

2.3.2. Le théorème de rédu tion semi-stable.
   C'est i i qu'intervient le théorème de rédu tion semi-stable.
Théorème 2.3.8.  Soit X un espa e stri tement k -anoïde purement de dimension 1
et rig-lisse ; il existe une extension nie séparable k′ de k telle que le domaine k′ -anoïde
X ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable.
Démonstration. Il existe une extension nie séparable k1 de k et une ourbe algébrique C
propre et lisse sur k1 telles que X ⊗k k1 soit isomorphe à un domaine anoïde de C ([31℄,
theorem 1). Appliquant le théorème de rédu tion semi-stable sous la forme rigide-analytique
établie par S. Bos h et W. Lütkebohmert dans [9℄, il existe une extension nie séparable k′
de k1 telle que C ⊗k1 k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe C dont la
bre spé iale est simplement semi-stable ; 'est automatiquement une S - ourbe semi-stable
54



(remarque 2.2.9, 3). En hoisissant onvenablement k′ , on peut en outre supposer que tout
point x du bord de X ⊗k k′ satisfait à la ondition |κ(x)× | = |k′ × |.
    Envisageons X ′ = X ⊗k k′ omme un domaine stri tement k′ -anoïde de Cη et soit q :
C ′ → C un é latement admissible tel que C ′ soit une Spf(k′ ◦ )- ourbe simplement semi-stable,
ave ∂X ′ ⊂ S0 (C ′ ) (lemme 2.2.22). L'image de X ′ par l'appli ation de rédu tion Cη′ → Cs
est un ouvert U et X ′ est isomorphe à la bre générique de la Spf(k′ ◦ )- ourbe simplement
semi-stable X = C|U′ .                                                                       2
  Soient X un espa e stri tement k-anoïde purement de dimension 1 rig-lisse et k′ , k′′ deux
extensions nies galoisiennes de k telles que X ⊗k k′ et X ⊗k k′′ soient isomorphes aux bres
génériques de ourbes stri tement semi-stables ; étant donnée une extension nie galoisienne
K de k oiant k′ et k′′ , la proposition 2.3.7 implique l'identité des espa es H(X ⊗k k′ ) et
                   ′                                          ′′
H(X ⊗k K)Gal(K/k ) (resp. H(X ⊗k k′′ ) et H(X ⊗k K)Gal(K/k ) ), d'où dé oule l'égalité
                               ′                                              ′′
              H(X ⊗k k′ )Gal(k /k) = H(X ⊗k K)Gal(K/k) = H(X ⊗k k′′ )Gal(k /k) .
Le théorème pré édent permet ainsi de dénir, pour tout espa e stri tement k-anoïde X
purement de dimension 1 et rig-lisse, un sous-espa e ve toriel H(X) de C0 (|X|, R) : H(X) =
                ′
H(X ⊗k k′ )Gal(k /k) ⊂ C0 (|X|, R), k′ étant une extension nie galoisienne de k telle que X ⊗k k′
soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable.
   Désignant par C la atégorie dont les objets sont les espa es stri tement k-anoïdes, pure-
ment de dimension 1 et rig-lisses, et les morphismes les immersions anoïdes, il dé oule de la
proposition 2.3.3 que l'on vient ainsi de dénir un fon teur H sur Cop à valeurs dans VectR .
  Nous aurons besoin des deux résultats suivants.
Lemme 2.3.9.  Pour tout espa e stri tement k -anoïde Y rig-lisse et purement de di-
mension 1, l'appli ation de restri tion
                                   C0 (|Y |, R) → Hom(Γ(Y ), R)
induit un isomorphisme du sous-espa e H(Y ) sur Hom(Γ(Y ), R).
Démonstration. Soit k′ une extension galoisienne nie de k telle que l'espa e stri tement
k′ -anoïde Y ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-
                                                                                            ′
stable Y . La proje tion anonique p : Y ⊗k k′ → Y induit une bije tion de Γ(Y ⊗k k′ )Gal(k /k)
sur Γ(Y ) et l'appli ation de restri tion
                                   C0 (|Y |, R) → Hom(Γ(Y ), R)
 oïn ide ave l'appli ation induite par la restri tion
                            C0 (|Y ⊗k k′ |, R) → Hom(Γ(Y ⊗k k′ ), R)
                                                                                           ′
entre les sous-espa es des invariants sous Gal(k′ /k) ; puisque H(Y ) = H(Y ⊗k k′ )Gal(k /k) , la
 on lusion dé oule de la proposition 2.3.2.                                                    2
Lemme 2.3.10.  Soient Y un espa e stri tement k -anoïde onnexe, de dimension 1 et
rig-lisse, et (hn ) une suite roissante de fon tions appartenant à H(Y ). L'alternative suivante
est vraie :
    soit la suite (hn ) onverge, uniformément sur Y , vers une fon tion h ∈ H(Y ),
    soit la suite (hn ) onverge, lo alement uniformément sur Y − Γ(Y ), vers ∞.
Démonstration. Soient k′ une extension nie galoisienne de k telle que Y ′ = Y ⊗k k′ soit
isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement nodale Y′ et p : Y ′ → Y la
proje tion anonique. Si l'assertion est démontrée pour la suite (p∗ hn ) dans H(Y ′ ), elle l'est
                                                                      ′
également pour la suite (hn ) : en eet, puisque H(Y ) = H(Y ′ )Gal(k /k) , il sut de s'assurer
                                                                                               55



que la fon tion limite h ∈ H(Y ′ ) du premier as de l'alternative est invariante sous Gal(k′ /k) ;
utilisant l'isomorphisme Gal(k′ /k)-équivariant de restri tion
                                   H(Y ′ ) → Hom(Γ(Y ′ ), R),
                                                    ′
 ela dé oule de l'identité entre Γ(Y ) et Γ(Y ′ )Gal(k /k) .
   Vu la dénition de l'espa e H(Y ′ ) = H(Y ′ ) (dénition 2.3.1), le résultat pour une suite
 roissante dans H(Y ′ ) s'obtient par appli ation de la proposition 1.2.12.                 2
2.3.3. Le fais eau HX .
  Soit X une ourbe stri tement k-analytique lisse. Le fon teur H : Cop → VectR donne
naturellement naissan e à un préfais eau HX sur le site rigide XR de X (2.1.1) : étant donné
un objet V de XR , les domaines stri tement k-anoïdes de X ontenus dans V forment un
système indu tif ltrant I(V ) (les morphismes sont les in lusions) et l'on pose
                                      HX (V ) = ←
                                                lim
                                                  −I(V ) H.
Remarque 2.3.11
  1. Pour tout domaine stri tement k-anoïde Y dans X , l'homomorphisme anonique
     HX (Y ) → H(Y ) est un isomorphisme.
  2. Le préfais eau HX sur le site XR n'est lairement pas un fais eau. Il sut en eet de
      onsidérer, sur X = P1k = A1k ∪ {∞}, le re ouvrement ni par les domaines stri tement
     k-anoïdes Y1 = {|T1 ≤ r}, Y2 = {r ≤ |T1 | ≤ r −1 } et Y3 = {|T1 | ≥ r −1 }  r étant un
     élément de ]0, 1[∩|k× |  et la fon tion ontinue h sur X telle que
         h|Y1 = 0 ;
         h|Y2 = log |T1 | − log(r) ;
         h|Y3 = −2 log(r).
        Cha une des fon tions h|Yi appartient à H(Yi ), i ∈ {1, 2, 3}, mais la fon tion h n'ap-
     partient ertainement pas à HX (X) : si tel était en eet le as, la restri tion de h au
     domaine stri tement k-anoïde Y = {|T1 | ≤ r −1 } de X devrait appartenir à H(Y ),
     don , en vertu de la proposition 2.3.2, 1, être onstante puisque Γ(Y ) est réduit à un
     point (asso ié à la semi-norme
                                           X
                            k[T1 ] → R≥0 ,    an T1n 7→ max(|an |r −n ).
                                                        n≥0
                                          n≥0
        Nous nous intéresserons au fais eau asso ié à e préfais eau dans le pro hain hapitre
     ( f. 3.2.1).

   Tout ouvert Ω de X admet un re ouvrement lo alement ni par des domaines stri tement
k-anoïdes : 'est don un objet de XR et tout re ouvrement ouvert de Ω est une famille
  ouvrante dans XR . Notant |X| le site asso ié à l'espa e topologique |X|, la remarque pré-
  édente montre que l'on dispose d'un morphisme de sites anonique ι : XR → |X|. À tout
préfais eau (resp. fais eau) F sur XR est don asso ié le préfais eau (resp. fais eau) ι∗ F sur
l'espa e topologique |X|.
Définition 2.3.12.  Étant donnée une ourbe simplement k -analytique lisse X , le pré-
fais eau ι∗ HX sur l'espa e topologique |X| sous-ja ent à X se note HX .
   Le préfais eau Y 7→ C0 (Y, R) sur le site XR étant un fais eau (remarque 2.1.7), HX est
un sous-préfais eau du fais eau CX des germes de fon tions réelles ( ontinues) sur |X|. Les
éléments de HX (X) sont les fon tions (réelles) ontinues sur |X| dont la restri tion à tout
domaine stri tement k-anoïde Y de X appartient au sous-espa e H(Y ) de C0 (|Y |, R).
56



   Soit X une ourbe stri tement k-analytique lisse et désignons momentanément par HX le
fais eau sur |X| asso ié au préfais eau HX ; nous allons maintenant vérier l'identité HX =
HX , établissant ainsi que HX est un fais eau.
Proposition 2.3.13.  Les se tions du fais eau HX satisfont au prin ipe du maximum :
quel que soit l'ouvert Ω de X , une fon tion h ∈ Γ(Ω, HX ) admet un extremum lo al en un
point x de Ω si et seulement si elle est onstante au voisinage de x.
Démonstration. Il existe par hypothèse un voisinage stri tement k-anoïde Y de x tel que
h|Y ∈ H(Y ). Soit k′ une extension nie galoisienne de k telle que Y ⊗k k′ soit isomorphe
à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable Y ; h ⊗ 1 = H ◦ τY ave
H ∈ H(S(Y), Γ(Yη )) et, le morphisme anonique d'espa es analytiques p : Y ⊗k k′ → Y
étant ouvert, il sut de vérier que h ⊗ 1 est lo alement onstante en un point y de p−1 (x).
Si y ∈/ S(Y), h ⊗ 1 est lo alement onstante au voisinage de y ; sinon, H a un extremum
lo al sur S(Y) − Γ(Yη ) en y , don est lo alement onstante en e point en vertu du prin ipe
du maximum sur les polyèdres entiers (proposition 1.2.9) et il en va de même de h ⊗ 1 par
 ontinuité de τY .                                                                        2
   Soit Y un domaine stri tement k-anoïde dans X ; vu la dénition du préfais eau HX , on
dispose d'une appli ation R-linéaire anonique de restri tion H(Y ) → HX (Y − ∂Y ) (induite
par les restri tions H(Y ) → H(Y ′ ), Y ′ par ourant l'ensemble des domaines stri tement k-
anoïdes de Y − ∂Y ) et don d'une appli ation R-linéaire anonique
                           ρ : H(Y ) → Γ(Y − ∂Y, HX ) ∩ C0 (Y, R).
Corollaire 2.3.14.  L'appli ation linéaire        anonique
                           ρ : H(Y ) → Γ(Y − ∂Y, HX ) ∩ C0 (Y, R)
est un isomorphisme.
Démonstration. Considérons le diagramme ommutatif
                                 H(Y )                 / Hom(Γ(Y ), R)

                                  ρ
                                      
                      Γ(Y − ∂Y, HX ) ∩ C0 (Y, R)       / Hom(Γ(Y ), R),

dans lequel les è hes horizontales sont les restri tions ; la proposition pré édente implique
l'inje tivité de l'appli ation de restri tion
                Γ(Y − ∂Y, HX ) ∩ C0 (Y, R) → Hom(∂Y, R) = Hom(Γ(Y ), R)
et don la bije tivité de ρ puisque l'appli ation H(Y ) → Hom(Γ(Y ), R) est un isomorphisme
(proposition 2.3.2).                                                                      2
Corollaire 2.3.15.  Pour toute ourbe stri tement k -analytique lisse X , l'homomor-
phisme anonique de préfais eaux HX → HX est un isomorphisme ; HX est don un fais eau.
Démonstration. Le sous-préfais eau HX du fais eau CX est séparé et l'homomorphisme
 anonique HX → HX est don inje tif. Sa surje tivité équivaut à l'assertion suivante : pour
tout ouvert U de X et tout domaine stri tement k-anoïde Y de U , la restri tion à Y d'une
fon tion h ∈ Γ(U, HX ) appartient au sous-espa e H(Y ) de C0 (|Y |, R) ; 'est une onséquen e
immédiate du orollaire pré édent.                                                         2
Définition 2.3.16.  Le fais eau HX sur une ourbe stri tement k -analytique lisse X est
appelé le fais eau des germes de fon tions harmoniques.
                                                                                                 57



Remarque 2.3.17.  La dénition du fais eau HX rend évidente les assertions suivantes :
   le fais eau HX sur l'espa e topologique |X| est invariant par les automorphismes
    k-analytiques de X ; plus généralement, si X et Y sont deux ourbes stri tement
    k-analytiques lisses et ϕ : X →Y
                                  ˜ est un k-isomorphisme, l'isomorphisme de fais eaux
      ♯
    ϕ : CY →C˜ X induit un isomorphisme de HY sur HX ;
   pour toute extension nie galoisienne k′ de k, l'opération de G = Gal(k′ /k) sur CX⊗k k′
    stabilise la sous-fais eau HX⊗k k′ et l'isomorphisme anonique CX →     G
                                                                       ˜ CX⊗   kk
                                                                                  ′ induit un

    isomorphisme de HX sur HX⊗k k′ .
                                G


  Étant donné un domaine k-anoïde Y d'une ourbe k-analytique lisse X , nous noterons
H(Y ) le sous-espa e ve toriel
                                   Γ(Y − ∂Y, HX ) ∩ C0 (Y, R)
de C0 (|Y |, R) ; vu le orollaire 2.3.14, ette notation oïn ide ave elle introduite pré édem-
ment lorsque Y est stri tement k-anoïde.
   La orrespondan e Y 7→ H(Y ) est un préfais eau sur le G-site XG de X qui prolonge
évidemment le préfais eau sur le site XR déni au début de 2.3.3.
Proposition 2.3.18.  Soient X une ourbe stri tement k -analytique lisse et K une ex-
tension non ar himédienne de k ; notant XK pour X ⊗       b k K et pK le morphisme anonique
XK → X , pK HX ⊂ HX ⊗
              ∗
                          b kK .
Démonstration. C'est une onséquen e immédiate de la dénition du fais eau HX et du
lemme 2.3.5.                                                                                      2
   A hevons e paragraphe par le résultat suivant :
Proposition 2.3.19.  Soient X, Y deux ourbes stri tement k -analytiques lisses et f :
Y → X un morphisme. Pour toute fon tion harmonique h ∈ Γ(X, HX ), la fon tion f ∗ h = h◦f
est harmonique sur Y : f ∗ h ∈ Γ(Y, HY ).
Démonstration. On peut supposer Y onnexe et f quasi-ni. Étant donnés des domaines
stri tement k-anoïdes W ⊂ Y et V ⊂ X tels que f (W ) ⊂ V , h|V ∈ H(V ) et don , par appli-
 ation des propositions 2.3.3 et 2.3.7, (f ∗ h)|W ∈ H(W ). La fon tion f ∗ h est don harmonique
sur Y .                                                                                      2

2.3.4. Le préfais eau log |OX× |.
  Considérant toujours une ourbe stri tement k-analytique lisse X , examinons mainte-
nant les liens entre les fon tions harmoniques sur X et les fon tions de la forme log |f |,
            ×
f ∈ Γ(X, OX   ).
                                                   ×
Proposition 2.3.20.  Pour toute se tion f ∈ Γ(X, OX ), la fon tion log |f | est harmo-
nique sur X .
Démonstration. Il sut de vérier que la restri tion de la fon tion log |f | à tout domaine
stri tement k-anoïde Y ⊂ X appartient au sous-espa e H(Y ) ⊂ C0 (|Y |, R) ; vu le lemme
2.3.5 et le théorème 2.3.8, on peut en outre supposer que Y est la bre générique d'une S -
 ourbe simplement semi-stable, auquel as il ne reste plus qu'à invoquer le point (iii) de la
proposition 2.2.24.                                                                              2
Théorème 2.3.21.  Soit X une ourbe stri tement k -analytique lisse. Le fais eau de R-
                                                                                                 ×
ve toriels engendré par les germes de fon tions log |f |, f étant un germe de se tion de OX        ,
est un sous-fais eau de HX ; le quotient est un fais eau gratte- iel sur |X| et il est nul si l'une
des deux onditions suivantes est vériée :
58



      le orps e
               k est algébrique sur un orps ni ;
      la ourbe X ⊗  ca est lo alement isomorphe à P1 .
                  b kk                               a        k
Démonstration. Soit FX le sous-fais eau de CX asso ié au préfais eau sur |X| faisant orres-
pondre à un ouvert U le sous-espa e ve toriel de C0 (U, R) engendré par les fon tions log |f |,
               ×
f ∈ Γ(U, OX      ) ; 'est un sous-fais eau de HX en vertu de la proposition pré édente. Les germes
de FX et HX oïn ident en tout point x de X de type (1), (3) ou (4) :
     si x est de type (1) ou (4), e point admet un système fondamental de voisinages k-
       anoïdes ayant un unique point de Shilov et les se tions de FX et HX sont don
        onstantes au voisinage de x ;
     si x est de type (3), e point admet un système fondamental de voisinages k-anoïdes
       ayant exa tement deux points de Shilov ; les espa es ve toriels FX,x et HX,x sont alors
       de dimension 2, engendrés par les germes de la fon tion onstante 1 et de la fon tion
       log |f |, f étant une se tion quel onque de OX au voisinage de x telle que |f | ne soit pas
       lo alement onstante en x.
    Soient maintenant x ∈ X un point de type (2), k′ une extension nie galoisienne de k et x′ un
point de X ′ = X⊗k k′ au-dessus de x : l'égalité FX ′ ,x′ = HX ′ ,x′ implique l'égalité FX,x = HX,x .
En eet, si V est un voisinage stri tement k-anoïde de x dans X , V ′ est la omposante
 onnexe de x′ dans V ⊗k k′ , et f ′ ∈ A×                                                        ×
                                                    V ′ , la norme f de f est un élément de AV tel que
                                                                              ′
                      ′
p∗ |f ||V ′ = |f ′ |[k :k] ; si une fon tion h ∈ H(V ) est telle que p∗ h|V ′ soit une ombinaison linéaire
de fon tions log |f |, f ∈ A×                                                                           ×
                                    V ′ , 'est don une ombinaison linéaire de fon tions log |f |, f ∈ AV .
Cette remarque préliminaire permet de supposer que X est isomorphe à la bre générique
d'une S - ourbe simplement semi-stable X et que le point x orrespond à une omposante
irrédu tible propre et géométriquement onnexe Cx de Xs .
Lemme 2.3.22.  Ave les notations en vigueur, l'espa e ve toriel HX,x /FX,x est anoni-
quement isomorphe à l'espa e ve toriel Pic0 (Cx ) ⊗Z R.
Démonstration. Soit V un voisinage stri tement k-anoïde de X . Il existe une extension
galoisienne nie k′ de k et un é latement admissible q : X ′ → X ⊗S Spf(k′ ◦ ) tel que V ⊗k k′
soit isomorphe à la bre générique du s héma formel induit par X ′ sur un ouvert U de Xs′ . La
 omposante irrédu tible Cx de Xs étant supposée géométriquement onnexe, il y a un unique
point x′ ∈ X ⊗k k′ au-dessus de x, orrespondant à la omposante irrédu tible Cx ⊗ek ke′ de
X ⊗S Spf(S ′ ) et, elle- i étant propre et lisse, le morphisme q induit un isomorphisme de la
 omposante irrédu tible de X ′ asso iée à x′ sur Cx ⊗ek ke′ .
                                                               ′
    À toute fon tion h ∈ H(V ) = H(V ⊗k k′ )Gal(k /k) orrespond naturellement un R-diviseur
div(h) sur la ke′ - ourbe Cx ⊗ek ke′ , vue omme omposante irrédu tible de Xs′ : en eet, l'ensemble
Tx′ S(X ′ ) est anoniquement identié à l'ensemble des points singuliers de Xs′ appartenant à
Cx ⊗ek ke′ et, notant x      et le point orrespondant à l'élément t de Tx′ S(X ′ ), on pose :
                                                          X
                                            div(h) =             λx,t (h)[e
                                                                          xt ].
                                              t∈Tx′ S(X ′ )

La ondition d'harmoni ité de h en x′ équivaut à la ondition
                                            deg div(h) = 0.
   Le groupe de Galois Gal(k′ /k) opère naturellement sur la ke′ - ourbe Cx ⊗ek ke′ et son a tion
est transitive sur haque bre du morphisme anonique Cx ⊗ek ke′ → Cx ; puisque h est, par
hypothèse, invariante sous Gal(k′ /k), ela implique que le R-diviseur div(h) sur Cx ⊗ek ke′
des end en un R-diviseur de degré 0 sur sur Cx , en ore noté div(h).
                                                                                                59



  Nous obtenons ainsi une appli ation linéaire div : HX,x → Div(Cx ) ⊗Z R s'insérant dans
une suite
                  0       /R      / HX,x   div   / Div(Cx ) ⊗Z R deg   /R     / 0,

laquelle est exa te. Seule la surje tivité de div sur le sous-espa e des R-diviseurs de degré 0
requiert une démonstration. Soit
                                              X
                                        D=        n(e
                                                    x)[ex]
                                             e∈|D|
                                             x

un R-diviseur de degré 0 sur Cx ; soit I l'Idéal (admissible) dénissant le sous-s héma fermé
réduit Z = |D|∩(Xs −Sing(Xs )) dans Xs et soit q : X ′ → X son é latement. Puisque X est lisse
aux points de Z , X ′ est en ore une S - ourbe simplement semi-stable et on note Y l'ouvert de
X ′ obtenu en retirant, à ha une des omposantes irrédu tibles du diviseur ex eptionnel de X ′ ,
un point fermé disjoint (du transformé stri t) de X . La S - ourbe Y est simplement semi-stable
et Yη est un voisinage de x dans X = Xη . L'ensemble Tx S(Y) s'indentie anoniquement à
une partie nie de l'ensemble des points fermés de Cx et nous avons fait e qu'il fallait pour
que
                                         |D| ⊂ Tx S(Y).
Considérons alors une fon tion ane par mor eaux H sur S(Y) telle que, pour tout polytope
entier P ⊂ S(Y) de dimension un orrespondant à un élément t ∈ Tx S(Y),
- λx,t (H) = 0 si x  / |D|,
                  et ∈
- λx,t (H) = n(e
               xt ) si x
                       et ∈ |D|.
   Une telle fon tion H est harmonique au point x en vertu de la nullité du degré de D ; elle
est don harmonique sur un voisinage de x dans S(Y) et la fon tion h = τY∗ H sur X est par
 onséquent harmonique au voisinage de x dans X . L'identité
                                           div(h) = D
est vériée par onstru tion et nous avons ainsi établi l'exa titude de la suite onsidérée
 i-dessus.
  Soit Pr(Cx ) le groupe des diviseurs prin ipaux sur Cx . On dispose d'une autre suite exa te

                                  /R       / FX,x    div   / Pr(Cx )   / 0,
                           0
                                            ×
 ar, pour tout germe log |f | ∈ FX,x , f ∈ OX,x , le diviseur de la fon tion harmonique N log |f |
s'identie à elui de la fon tion méromorphe induite par f N /α sur Cx , où N est un entier
supérieur à 1 tel que |f (x)|N ∈ |k× | et α est un élément de k tel que |f (x)|N = |α|. Il en
résulte un isomorphisme d'espa es ve toriels réels
                                                 ∼
                                HX,x /FX,x −→ Pic0 (Cx ) ⊗Z R,
 e qui a hève la preuve du lemme.                                                                2
   Terminons la démonstration du théorème. Le fais eau HX /FX est un fais eau gratte- iel
dont le support est un ensemble dis ret de points de type (2) ; sa nullité équivaut à la propriété
suivante : pour tout point x ∈ X ⊗k c ka de type (2), le groupe de Pi ard Pic0 (Cx ) de la e   ka -
                                                                   g , est de torsion. Il y a au
 ourbe irrédu tible, propre et lisse Cx , de orps des fon tions κ(x)
moins deux onditions impliquant ette propriété :
    le orps ek est algébrique sur un orps ni : Pic0 (Cx ) est l'ensemble des e  ka -points d'un
     e
     ka -s héma en groupes de type ni et don est de ardinal ni ;
60



      pour tout point x ∈ X ⊗k k ca de type (2), la eka - ourbe irrédu tible, propre et lisse de
                           g est rationnelle  de manière équivalente, X ⊗
        orps des fon tions κ(x)                                             b kb
                                                                               ka est lo alement
       isomorphe à Pba (si X est irrédu tible et propre, 'est une ourbe de Mumford ).
                     1
                     k
                                                                                              2
                                                                                              61



                              3. Théorie du potentiel



                              3.1. Le problème de Diri hlet
  Dans e qui suit, X est une ourbe stri tement k-analytique lisse.
3.1.1. Propriétés fondamentales des fon tions harmoniques.
  Les se tions du fais eau HX satisfont au prin ipe du maximum.
Proposition 3.1.1.  Étant donné un ouvert Ω de X , une fon tion h ∈ Γ(Ω, HX ) admet
un extremum lo al en un point x de Ω si et seulement si elle est onstante au voisinage de x.
  C'est la onjon tion de la proposition 2.3.13 et du orollaire 2.3.14.
   Le problème de Diri hlet est lo alement résoluble : tout point x ∈ X admet un système
fondamental de voisinages ouverts relativement ompa ts Ω tels que l'appli ation de restri tion
                              C0 (Ω, R) ∩ Γ(Ω, HX ) → C0 (∂Ω, R)
soit un isomorphisme. Il sut en eet de prendre pour Ω l'intérieur d'un voisinage stri tement
k-anoïde Y de x dans X et d'appliquer le lemme 2.3.9.
  Le prin ipe de Harna k est valide
Proposition 3.1.2.  Soient Ω un ouvert onnexe de X et (Ωn ) une suite d'ouverts de
X telle que haque point de Ω admette un voisinage ontenu dans presque tous les Ωn : quelle
que soit la suite roissante de fon tions hn ∈ Γ(Ωn , HX ), l'alternative est la suivante :
   soit (hn ) onverge vers +∞ uniformément sur tout ompa t de Ω,

   soit (hn ) onverge vers une fon tion h ∈ Γ(Ω, HX ), uniformément sur tout ompa t de
     Ω.
Démonstration. Puisque tout point de x admet un système fondamental de voisinages stri -
tement k-anoïdes, il dé oule du lemme 2.3.10 que l'ensemble U (resp. U ′ = Ω−U ) des points
de Ω en lesquels la suite (hn ) est majorée (resp. n'est pas majorée) est une partie ouverte ; de
plus, toujours par appli ation de e lemme, la suite (hn ) onverge
   lo alement uniformément vers ∞ sur U ′ ;
   lo alement uniformément sur U vers une fon tion h  né essairement ontinue  telle que,
     pour tout domaine stri tement k-anoïde Y de Ω, la restri tion de h à Y appartienne à
     H(Y ) ; vu la dénition du fais eau HX (2.3.3), la fon tion h est harmonique sur Ω.
                                                                                               2
   Notons également le résultat de onvergen e suivant :
Proposition 3.1.3.  Soient Ω un ouvert de X et (hn ) une suite de fon tions harmo-
niques sur Ω ; si la suite (hn ) est lo alement bornée, on peut en extraire une sous-suite onver-
geant, lo alement uniformément sur Ω, vers une fon tion harmonique.
Démonstration. Nous démontrerons au orollaire 3.3.7 que toute famille lo alement bornée
de fon tions harmoniques sur Ω est automatiquement équi ontinue en tout point de Ω ; bien
entendu, la proposition ne sera pas utilisée d'i i là. Appliquant le théorème d'As oli, on peut
```

## Thuillier, newline lines 4100--4216

```text
le bord de Shilov Γ(Y ) d'un domaine k-anoïde Y de X est un sous-ensemble ni de I(X) et
toute partie nie S de I(X) est la réunion des bords de Shilov d'un nombre ni de domaines
k-anoïdes.

3.2.1. Les fais eaux A0X et A1X sur XG .
     Dans e qui suit, X désigne une ourbe stri tement k-analytique lisse.
Définition 3.2.1.  Soit Ω ⊂ X un ouvert.
   (i ) Une fon tion réelle ϕ ∈ C (Ω, R) est dite lisse s'il existe un re ouvrement lo alement
                           0

ni V de Ω par des domaines k-anoïdes Y tel que ϕ|Y ∈ H(Y ). L'ensemble des fon tions
lisses sur Ω est un sous-espa e ve toriel de C0 (Ω, R), noté A0 (Ω).
   (ii ) On désigne par A1 (Ω) l'espa e ve toriel des mesures réelles sur Ω dont le support est
un sous-ensemble lo alement ni de I(Ω). Les éléments de A1 (Ω) seront appelés formes lisses
(sur Ω).

  (iii ) Le sous-espa e ve toriel de A0 (Ω) (resp. A1 (Ω)) onstituté des fon tions (resp. me-
sures) dont le support est ompa t se note A0c (Ω) (resp. A1c (Ω)).

   La orrespondan e Ω 7→ A0 (Ω) est un sous-fais eau du fais eau CX
                                                                  0 des germes de fon tions

réelles ontinues sur X .
   La dénition du fais eau A0X s'étend d'elle même au G-site XG de X : il sut, pour tout
objet V de XG , de dénir A0 (V ) omme le sous-espa e ve toriel de C0 (V, R) onstitué des
fon tions ϕ ontinues sur V qui satisfont à la ondition suivante : tout point x ∈ V possède
un voisinage k-anoïde W ⊂ V tel que ϕ|W ∈ H(W ). Désignant par A0X le fais eau ainsi
déni sur XG et notant π : XG → |X| le morphisme de sites anonique, l'identité
                                         A0X = π∗ A0X
est évidente. La proposition suivante l'est tout autant.

Proposition 3.2.2.  L'homomorphisme            anonique de préfais eaux HX → A0X sur le site
XG identie A0X au fais eau asso ié à HX .

Remarque 3.2.3
     1. La proposition pré édente répond à la question soulevée par le point 2 de la remarque
        2.3.11.
                                                                                              69



  2. Pour toute extension nie galoisienne k′ /k, l'homomorphisme anonique
                                                           ′
                                   A0X → (A0 X⊗k k′ )Gal(k /k)
     est un isomorphisme de fais eaux sur XG .

 La proposition suivante n'est guère surprenante, ompte tenu de la onstru tion du fais eau
HX .
Proposition 3.2.4.  Une fon tion réelle ϕ sur un ouvert Ω ⊂ X est lisse si et seulement
s'il existe, pour tout domaine stri tement k-analytique ompa t Y ⊂ Ω, une extension nie
(séparable ) k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-stable Y telles que :
    Yη = Y ⊗k k ′ ;
    la fon tion Φ = (ϕ ⊗ 1)|S(Y) appartienne à l'espa e A0 (S(Y)) ;
    ϕ|Y ⊗k k′ = Φ ◦ τY .
Démonstration. Soit Y ⊂ X un domaine stri tement k-analytique ompa t.
   Étant données une extension nie galoisienne k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-
stable Y de bre générique Y ⊗k k′ , onsidérons une fon tion Φ ∈ A0 (S(Y)) et notons S la
réunion du support de la mesure ddc Φ et du bord de Shilov Γ(Yη ) de Yη . Quelle que soit la
 omposante onnexe c de S(X ) − S , la restri tion de Φ au domaine polyédral c appartient
à l'espa e H(c) et la fon tion Φ|c ◦ τY = (Φ ◦ τY )|τ −1 (c) sur le domaine k-analytique τY−1 (c)
                                                      Y
de Y ⊗k k′ appartient à H(τY−1 (c)) ; en vertu de la proposition pré édente, ela implique
Φ ◦ τY ∈ A0 (Y ⊗k k′ ). La ondition de l'énon é est don susante.
   Considérons ré iproquement une fon tion ϕ ∈ A0 (Y ) et un re ouvrement ni V de Y par
des domaines k-anoïdes V tels que ϕ|V ∈ H(V ) ; par appli ation du point (ii) du lemme
2.2.22, il existe une extension nie (séparable) k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-
stable Y , de bre générique Y ⊗k k′ , dont le squelette S(Y) ontient l'ensemble Γ des points de
Shilov des domaines k′ -anoïdes V ⊗k k′ , V ∈ V . Désignons par Φ la restri tion de ϕ′ = ϕ ⊗ 1
au squelette S(Y) de Y . Les bres de la rétra tion τY sont des domaines k′ -anoïdes dont le
bord de Shilov est réduit à un point ; la fon tion ϕ′ , étant harmonique sur Y ⊗k k′ − Γ, est
par suite onstante haque bre de τY en vertu du prin ipe du maximum et
                                          ϕ′ = Φ ◦ τY .
Vérions enn l'appartenan e de Φ à l'espa e A0 (S(Y)) : quel que soit le polytope entier
P ⊂ S(Y) − Γ dont le bord est formé de points de type (2), W = τY−1 (P ) est un domaine
stri tement k-anoïde dans Y tel que ϕ′|W ∈ H(τY−1 (P )) ( orollaire 2.3.14) ; on a don Φ|P =
(ϕ′|W )|P ∈ H(P ) et la fon tion ontinue Φ est bien ane par mor eaux sur S(Y).              2
   La proposition 3.2.2 peut maintenant être pré isée de manière à donner une nouvelle dé-
nition du fais eau A0X sur le G-site XG de X . Étant donné un domaine k-analytique V ⊂ X ,
 onvenons de désigner par R log |OX (V )× | le sous-espa e ve toriel réel de C0 (V, R) engendré
par les fon tions de la forme log |f |, f ∈ OX (V )× . La orrespondan e
                                       ×
                               R log |OX | : V 7→ R log |OX (V )× |

est un sous-préfais eau de A0X sur XG puisque R log |OX (V )× | ⊂ H(V ) pour tout domaine
k-anoïde V ⊂ X .
                                                                   ×
Proposition 3.2.5.  L'homomorphisme              anonique R log |OX | → A0X identie A0X au
                                        ×
fais eau asso ié au préfais eau R log |OX |.
70



Démonstration. Soit FX le fais eau sur XG asso ié au préfais eau R log |OX× |. Quelle que
                                                                                   ×
soit l'extension galoisienne nie k′ /k, la norme Nk′ /k : (pk′ )∗ (OX ⊗k k′ )× → OX induit un
homomorphisme Nk′ /k : (pk )∗ FX⊗k k → F tel que
                             ′        ′

                                           1
                                   f=              Nk′ /k (f ⊗ 1)
                                        [k′ : k]
pour toute se tion f de F , pk′ désignant la proje tion anonique de X ⊗k k′ sur X . Il sut don
de prouver qu'une se tion ϕ de A0X provient de FX après passage à une extension galoisienne
nie de k.
    Soient Y ⊂ X un domaine k-analytique ompa t et ϕ une fon tion dans A0X (Y ). Il existe par
hypothèse un re ouvrement ni V de Y par des domaines k-anoïdes V tels que ϕ|V ∈ H(V )
et, omme dans la démonstration pré édente, on peut trouver une extension galoisienne nie
k′ /k et une Spf(k′ ◦ )- ourbe simplement semi-stable Y dont la bre générique est un voisinage
de Y ⊗k k′ dans X ⊗k k′ et dont le squelette S(Y) ontient l'ensemble Γ de tous les points de
Shilov des domaines k-anoïdes V ⊗k k′ , V ∈ V .
    Considérons alors une dé omposition élémentaire D de S(Y) telle que Γ ⊂ D[0] (on rappelle
que D[0] est l'ensemble des 0-fa es des polytopes gurant dans D ). Quel que soit le polytope
Q ∈ D , τ −1 (Q) est un domaine k-anoïde et, par onstru tion,
                           ϕ|Q ∈ H(τ −1 (Q)) = R log |OX (τ −1 (Q))|.
                                                                                              2
Remarque 3.2.6.  Cette proposition est à rappro her des onsidérations de 2.3.4.
```

## GJR, newline lines 2415--2618

```text
and functoriality of reduction. The converse holds if x ∈ Int(X ′ /X ) by Theorem 6.15
and Lemma 6.12(1), using functoriality of residues 6.19. Assertion (1′ ) follows because
a proper morphism has no boundary.
                 FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                             47

  To prove (2), let ϕ : PHf(x ′ )/Ke ′ → PHf(x)/Ke be the natural morphism. We have seen in 6.13
that ϕ −1 (red(X , x)) = red(X ′ , x ′ ). The assertions now follow from Lemma 6.12 and
functoriality of residues 6.19. To prove (2′ ), by Corollary 5.9 we may shrink X such that
X is compact with formal model X and such that there is L ∈ M (X)Λ with h = hL . Then
the claim follows from Lemma 6.8(2) and Lemma 7.4.
  The claims (3) and (3′ ) follow from (7.6,1′ ) since X red → X is proper and surjective. 
 The following proposition allows us to pass to Galois extensions when studying har-
monic and semipositive functions.
Proposition 7.7. Suppose that Λ is divisible. Let L/K be a (potentially infinite) normal
extension with automorphism group G := Aut(L/K). Let K ′ be the completion of L and let
X ′ := X ⊗
         b K K ′ , with structure morphism π: X ′ → X . Then h 7→ h ◦ π induces an isomor-
phism from the monoid of semipositive Λ-PL functions on X (resp. the group of Λ-harmonic
functions on X ) to the monoid of G-invariant semipositive Λ-PL functions on X ′ (resp. the
group of G-invariant Λ-harmonic functions on X ′ ).
Proof. This is an immediate consequence of Corollary 5.13 and Proposition 7.6(2′ ).                       
  Our next goal is to approximate locally semipositive metrics by local Fubini–Study
metrics (Proposition 7.10). This will be a crucial ingredient in proving the balancing
condition in Section 9.
  Recall that a line bundle on a scheme Y is called semiample if some positive tensor
power is globally generated. We say that L ∈ Pic(Y )R is ample (resp. semiample) if there
P r ample (resp. semiample) line bundles H1 , . . . , H r and λ1 , . . . , λ r ∈ R≥0 such that L =
are
     λ H ∈ Pic(Y )R . An ample L is semiample and a semiample L is nef.
  j=1 j j

Definition 7.8. Let h: X → R be an R-PL function. We say that h is Fubini–Study at a
point x ∈ X if Lh (x) is semiample. We say that h is locally Fubini–Study or LFS if it is
Fubini–Study at every point of X .
  Clearly if h is Fubini–Study at x then it is semipositive at x.
7.9. It follows from [CD12, Proposition 6.8.2] that h is Fubini–Study at x if and only if
there is an open neighbourhood U of x such that h|U is an R≥0 -linear combination of func-
tions of the form max{− log | f1 |, . . . , − log | f n |} for invertible analytic functions f1 , . . . , f n
on U.
  The following proposition can be seen as a local analogue of the fact that one can
approximate a nef Q-line bundle by ample Q-line bundles on a projective variety.
Proposition 7.10. Let h: X → R be an R-PL function that is semipositive at a point x ∈
Int(X ). Then there exists a strictly analytic neighbourhood U of x and a sequence h1 , h2 , . . .
of R-PL LFS functions on U such that hi → h|U uniformly.
Proof. We may shrink X to assume it is compact. By Corollary 5.9, we may assume that
there exists a formal K ◦ -model X of X and a line bundle L ∈ M (X)R with h = hL , using
the notation of 5.7. Since x is inner, the closure VX,x of redX (x) in Xs is proper (with the
notation of 6.13): see [CD12, Lemma 6.5.1] and [Vil21, Appendix A]. By Chow’s lemma,
48                               W. GUBLER, P. JELL, AND J. RABINOFF

there is a proper birational morphism V → VX,x with V projective over K              e . Let L ′ be an
                                                                                ′
ample line bundle on V . By [CD12, 6.6.5], there is a PL function h on the germ (X , x)
such that (V, L ′ ) is a model of the residue Lh′ (x). Let U be a compact strictly analytic
neighbourhood of x on which h′ is defined. Then there is a formal K ◦ -model U of U and
a line bundle L′ on U with h′ = hL′ . By Lemma 6.14, there is a compact strictly analytic
neighbourhood U ′ of x and a formal K ◦ -model U′ of U ′ such that the closure V ′ := VU′ ,x
of redU′ (x) dominates V . We may assume that U ′ ⊂ U and that this inclusion extends to
a morphism f : U′ → U by using Raynaud’s theorem. Let L ′ |V ′ be the pull-back of L ′ with
respect to V ′ → V . Then L ′ |V ′ and f ∗ (L′ )|V ′ are both models for Lh′ (x). We conclude that
there is a dominating model V ′′ of red(X , x) such that the pull-backs of L ′ |V ′ and f ∗ (L′ )|V ′
to V ′′ agree. Using Lemma 6.14 again and the arguments above, we may assume that
V ′′ = VU′′ ,x for a formal K ◦ -model U′′ of a compact strictly analytic neighbourhood U ′′
of x contained in U ′ such that the inclusion U ′′ ⊂ U ′ extends to a morphism U′′ → U′ .
Moreover, we may assume that U ′′ ⊂ X extends to a morphism U′′ → X. Replacing X by
U′′ and L, L′ by their pull-backs to U′′ , we put ourselves in the following situation:
     (1) The closure V ′ of redX (x) in Xs dominates V .
     (2) There is L ∈ M (X)R and L ∈ Pic(V )R such that h = hL and L|V ′ is the pullback of
         L under V ′ → V , and such that (V, L) is a model of Lh (x).
     (3) There is a line bundle L′ on X and an ample line bundle L ′ on V such that h′ = hL′
         and L′ |V ′ is the pullback of L ′ under V ′ → V .
We recycle notation now and let U := red−1       X
                                                     (V ′ ). By anticontinuity of the reduction map,
the set U is an open neighbourhood of x. For ǫ ∈ Q>0 let Lǫ := L + ǫ L ′ , Lǫ := L + ǫ L′ ,
and hǫ := hLǫ = h + ǫh′ . Then hǫ is an R-PL function on X and Lǫ |V ′ is the pullback of Lǫ
under V ′ → V . Note that hǫ → h uniformly as ǫ → 0. If h is semipositive at x then L is
nef by Lemma 6.11, so Lǫ is ample as a consequence of Kleiman’s theorem, see [Laz04,
Corollary 1.4.10]. It follows that Lǫ |V ′ is semiample. If y ∈ U then redX ( y) ∈ V ′ , so the
closure Y of redX ( y) in Xs is contained in V ′ . Since h = hL and h′ = hL′ on all of X ,
the pair (Y, Lǫ |Y ) is a model of Lhǫ ( y) by the construction in 6.16. Since Lǫ |Y is again
semiample, we see that hǫ is Fubini–Study at y. Thus hǫ is LFS on U.                                 
Remark 7.11. Let X be a proper scheme over K. It is shown in [GM19, Section 5] that
a pointwise limit of semipositive Q-PL metrics is semipositive. We expect the analogous
result to hold in our situation. In particular, we expect the converse of Proposition 7.10
to hold true: namely, if an R-PL function h is a uniform limit of R-PL LFS functions on
a strictly analytic neighbourhood U of an interior point x, then h is semipositive at x.
This would imply that if h and h′ are R-PL functions that are semipositive at x, then so is
max{h, h′ }. Indeed, we can write h = lim hi and h′ = lim h′i for R-PL LFS functions hi , h′i
in a neighbourhood U of x. By 7.9, the functions max{hi , h′i } are R-PL LFS functions on
U, and we have max{h, h′ } = lim max{hi , h′i }.
   Now we relate semipositivity to positive forms and currents. See 2.8 for the definitions
of positivity based on the corresponding notions for Lagerberg forms and Lagerberg cur-
rents introduced in 2.7. The next result serves as a replacement for [CD12, Lemmas 5.2.3
and 5.3.3] where the result is claimed for strongly positive forms; this is not correct, as
explained in [BGJK21a, Example 2.3.6].
                FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                             49

                                                                      p,p
Lemma 7.12. Let X be a Hausdorff analytic space over K and let ω ∈ Asm,c   (X ) be symmetric.
                                         p,p
Then there are positive forms ω1 , ω2 ∈ Asm,c (X ) such that ω = ω1 − ω2 .
Proof. The support of ω is compact and hence has a paracompact open neighbourhood
in X by [CD12, Lemme 2.1.6]. Replacing X by this open neighbourhood, we may as-
sume that X is paracompact. Then we have smooth partitions of unity available [CD12,
Proposition 3.3.6], so we may argue locally. Hence we may assume that there is an open
subset U of X such that the support of ω is contained in U and such that W := U is a
                                                                   n,an               ∗
compact analytic domain in X with a moment map ϕ : W → Gm               and with ω = ϕtrop (α)
                              p,p
for a symmetric form α ∈ A (ϕtrop (W )). It follows from 2.7 that α = α1 − α2 for two
smooth positive forms α1 , α2 on ϕtrop (W ). As usual, the existence of smooth partitions of
unity yield that there is a smooth non-negative function ψ with support in U such that
                                         ∗
ψ ≡ 1 on supp(ω). Setting ωi := ψ · ϕtrop   (αi ) for i = 1, 2, we get the claim.           
7.13 (Continuous Plurisubharmonic Functions). For simplicity, we suppose that X is a
boundaryless6 good separated strictly analytic space to use currents on X as in 2.8. Using
the theory of integration from [CD12, 3.7–3.10], every continuous real function h on X
has an associated current [h] given by
                                                       Z
                               [h]: Asm,c (X ) −→ R ,        ω 7→            h·ω
                                                                         X
where the integral is defined by a limit process using that h is a uniform limit of smooth
functions on a neighbourhood of the support of ω (see [CD12, Corollaire 5.4.7, 5.4.8]).
We say that h is plurisubharmonic (short: psh) if the current d′ d′′ [h] is positive. A parti-
tion of unity argument shows that plurisubharmonicity is a local notion on X (see [CD12,
Lemme 5.5.2]).
   By [CD12, Lemme 5.5.3], a smooth function h is psh if and only if every x ∈ X has a
                                                                                r,an
compact strictly analytic neighbourhood V with a moment map ϕ : V → Gm               such that
h|V = u◦ϕtrop for a continuous function u on ϕtrop (V ) which restricts to a convex function
on each face. This characterization shows that smooth psh functions admit pull-backs
with respect to morphisms.
Theorem 7.14. Let X be a good separated strictly analytic space over K and let h: X → R
be a semipositive R-PL function. Then h restricts to a psh function on X \ ∂ X .
Proof. By restriction to X \ ∂ X , we may assume that X is boundaryless. The claim is local
in X and so we may assume that h is a uniform limit of R-PL LFS functions hi on X by
using Proposition 7.10. It follows from 7.9 and from [CD12, Corollaire 6.3.2] that an
R-PL locally Fubini–Study function is locally a uniform limit of smooth psh functions and
hence hi is psh. For any positive form ω ∈ Asm,c (X ), we deduce from uniform convergence
that                                 Z                  Z
                      〈ω, d′ d′′ [h]〉 =        h · d′ d′′ ω = lim       hi · d′ d′′ ω ≥ 0.
                                                              i
                                           X                        X
  6
    Currents in analysis work well only in the boundaryless case, as otherwise there are disturbing residues
along the boundary. Note that Chambert-Loir and Ducros also omit the boundary in their definition of
currents [CD12, 4.2.2], as their currents act on smooth forms with compact support disjoint from the
boundary.
50                                W. GUBLER, P. JELL, AND J. RABINOFF

We conclude that h is psh.                                                                          
Corollary 7.15. Let h be a harmonic function on a good separated strictly analytic space X
over K. Then the restriction of the current d′ d′′ [h] to X \ ∂ X is zero.
Proof. We may assume that X is boundaryless. It follows from Theorem 7.14 that h and
−h are psh on X . By linearity in the irreducible components and by arguing locally, we
may assume that X is of pure dimension d. Let η ∈ Asm,c             d−1,d−1
                                                                            (X ). Since d′ d′′ [h] is a
symmetric current on X , we have
                           1                                              1
         〈η, d′ d′′ [h]〉 =    〈η, d′ d′′ [h]〉 + (−1)d−1 〈Jη, d′ d′′ [h]〉 = 〈ω, d′ d′′ [h]〉
                           2                                                  2
for the symmetric form ω := η + (−1)d−1 Jη ∈ Asm,c       d−1,d−1
                                                                 (X ). By Lemma 7.12, there are
                             d−1,d−1
positive forms ω1 , ω2 ∈ Asm,c (X ) such that ω = ω1 − ω2 . As h and −h are psh, we get
                 2〈η, d′ d′′ [h]〉 = 〈ω1 , d′ d′′ [h]〉 − 〈ω2 , d′ d′′ [h]〉 = 0 − 0 = 0,
proving the claim.                                                                                  
Remark 7.16. In this section, we have focused on the concept of semipositive and har-
monic functions. In fact, all the results immediately transfer to Λ-PL metrics k k of a
line bundle L over a good strictly analytic space X . Indeed, the choice of a local frame s
gives rise to a Λ-PL function h := − log ksk, to which we can apply the above results. Then
Theorem 7.14 yields that on a good separated strictly analytic space X every semipositive
R-PL metric of L has a positive first Chern current c1 (L, k k) as defined in [CD12, 6.4.1].
The same holds for uniform limits of such metrics on L which includes all the metrics
considered by Zhang [Zha95] over projective varieties.

                  8. PIECEWISE LINEAR AND HARMONIC TROPICALIZATIONS
  In this section, we assume that X is a compact good strictly K-analytic space of pure
dimension d. We will define a piecewise linear tropicalization map to be a tuple h =
(h1 , . . . , hn) of PL functions on X . We will endow h(X ) ⊂ Rn with the structure of a
weighted (Z, Γ )-polytopal complex, which is canonical up to subdivision. The difficult
part is defining weights on h(X ), which we will do G-locally using the results of 4.
Definition 8.1. A piecewise linear (PL) tropicalization is a map
                                    h = (h1 , . . . , hn): X −→ Rn
where h1 , . . . , hn are piecewise linear functions. It is called a harmonic tropicalization if
in addition all the hi are harmonic (which means that all of the hi are Z-harmonic). It is
called a smooth tropicalization map if hi = log | f i | for f i ∈ Γ (X , OX× ).
8.2. Remarks:
                                                                                     n,an
   (1) A smooth tropicalization map has the form ϕtrop for a moment map ϕ : X → Gm        .
       These are the tropicalizations considered in [CD12].
   (2) A smooth tropicalization map is harmonic by Remark 7.3(6).
   (3) A piecewise linear tropicalization is G-locally a smooth tropicalization map.
                  FORMS ON BERKOVICH SPACES BASED ON HARMONIC TROPICALIZATIONS                                  51

    (4) Piecewise linear, harmonic, and smooth tropicalization maps all pull back under
        morphisms of analytic spaces and arbitrary change of base: see Lemma 5.4 and
        Proposition 7.6.
Proposition 8.3. A function h: X → R is piecewise linear if and only if each x ∈ X has a
strictly affinoid neighbourhood U such that h|U = F ◦ h′ for a smooth tropicalization map
h′ : U → Rn and a piecewise (Z, Γ )-linear function F : h′ (U) → R.
Proof. Suppose that h is piecewise linear. Fix x ∈ X . As X is a good analytic                  S      space, we
may assume that it is strictly affinoid. There is a finite G-covering X = i∈I X i by strictly
affinoid domains X i on whichT         h = − log | f i | for an invertible function f i on X i . Shrinking
```

## Thuillier visually checked printed-page transcription

# Thuillier primary-source transcription

Controlling PDF: https://theses.hal.science/tel-00010990v1/document
SHA-256: 9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a.
The root viewed PDF physical pages 67 and 68, printed pages 53 and 54.
The following passages are transcribed from those rendered pages to repair
missing characters in the PDF's text extraction. The surrounding extracted
proof bodies accompany the review separately. These are primary-source
quotations, not newly proved lemmas or grants of assumptions.

## Printed page 53, proof of Theorem 2.3.8, first paragraph

« Il existe une extension finie séparable $k_1$ de $k$ et une courbe
algébrique $C$ propre et lisse sur $k_1$ telles que $X\otimes_k k_1$
soit isomorphe à un domaine affinoïde de $C$ ([31], theorem 1).
Appliquant le théorème de réduction semi-stable sous la forme rigide-analytique
établie par S. Bosch et W. Lütkebohmert dans [9], il existe une extension
finie séparable $k'$ de $k_1$ telle que $C\otimes_{k_1} k'$ soit isomorphe
à la fibre générique d'une $\operatorname{Spf}(k'^\circ)$-courbe
$\mathcal C$ dont la fibre spéciale est simplement semi-stable ; c'est
automatiquement une $S$-courbe semi-stable ».
The final parenthesis and continuation appear on printed page 54.

## Printed page 54, Lemma 2.3.9 and its proof

« Pour tout espace strictement $k$-affinoïde $Y$ rig-lisse et purement de
dimension $1$, l'application de restriction
$C^0(|Y|,\mathbb R)\to\operatorname{Hom}(\Gamma(Y),\mathbb R)$
induit un isomorphisme du sous-espace $H(Y)$ sur
$\operatorname{Hom}(\Gamma(Y),\mathbb R)$.

Démonstration. Soit $k'$ une extension galoisienne finie de $k$ telle que
l'espace strictement $k'$-affinoïde $Y\otimes_k k'$ soit isomorphe à la
fibre générique d'une $\operatorname{Spf}(k'^\circ)$-courbe simplement
semi-stable $\mathcal Y$. La projection canonique
$p:Y\otimes_k k'\to Y$ induit une bijection de
$\Gamma(Y\otimes_k k')^{\operatorname{Gal}(k'/k)}$ sur $\Gamma(Y)$ et
l'application de restriction
$C^0(|Y|,\mathbb R)\to\operatorname{Hom}(\Gamma(Y),\mathbb R)$
coïncide avec l'application induite par la restriction
$C^0(|Y\otimes_k k'|,\mathbb R)\to
\operatorname{Hom}(\Gamma(Y\otimes_k k'),\mathbb R)$
entre les sous-espaces des invariants sous $\operatorname{Gal}(k'/k)$ ;
puisque $H(Y)=H(Y\otimes_k k')^{\operatorname{Gal}(k'/k)}$, la conclusion
découle de la proposition 2.3.2. »

The superscript notation on the boundary is retained as printed; it is
not silently reinterpreted as a pointwise fixed-boundary assertion.

# Appendix P. Examined book regularization packet; not a theorem premise

The new proof uses and reconstructs the finite-tree construction,
not the general positive-current equivalence. Exact packet bodies are exposed
for source-aware comparison. Their historical acceptance is not a premise.


## book-monotone-statement.tex

```latex
% Exact candidate statement for hostile audit and production Rethlas.
% Date: 27 August 2026.
% This packet is isolated from the live book.  It makes no novelty or
% priority claim and must not be promoted before a final correct receipt.

\begin{lemma}
\label{lem:p063-local-tree-affinoid}
Let $K$ be algebraically closed, complete, and nontrivially valued, let
$C$ be a smooth algebraic $K$-curve, let $W\subset C^{\mathrm{an}}$ be
open, and let $x\in W$.  There is a connected strict affinoid domain
$Y\subset W$, with $x\in Y^\circ$, which admits a strictly semistable
skeleton that is a finite metric tree.  Moreover, if $f$ is lisse on a
neighbourhood of $Y$, then, after refining that skeleton and making a
finite metric subdivision, one can write
\[
                         f|_Y=F\circ\tau
\]
for the retraction $\tau:Y\to\Gamma$ onto a finite metric tree $\Gamma$
and a continuous function $F$ that is affine on every edge.  The added
vertices away from the boundary are of type $2$ or type $3$.
\end{lemma}

\begin{lemma}
\label{lem:p063-tree-rational-strictification}
Let $\Gamma$ be a finite metric tree, let $\partial\Gamma$ be a nonempty
set of vertices containing every endpoint designated as boundary, and let
$F:\Gamma\to\mathbf R$ be continuous and affine on every edge.  Suppose
that
\begin{equation}
\label{eq:p063-graph-subharmonicity}
 \Delta_\Gamma F(v):=\sum_{e\ni v}d_eF(v)\geq0
 \qquad
 \bigl(v\in V(\Gamma)\setminus\partial\Gamma\bigr),
\end{equation}
where $d_eF(v)$ denotes the outgoing slope.  For every $\varepsilon>0$
there is a continuous function $G:\Gamma\to\mathbf R$, affine with
rational slope on every edge, such that
\begin{equation}
\label{eq:p063-graph-rational-error}
             \lVert G-F\rVert_{L^\infty(\Gamma)}<\varepsilon
\end{equation}
and
\begin{equation}
\label{eq:p063-graph-strict-mass}
 \Delta_\Gamma G(v)>0
 \qquad
 \bigl(v\in V(\Gamma)\setminus\partial\Gamma\bigr).
\end{equation}
If there are no interior vertices, the last condition is empty.
\end{lemma}

\begin{lemma}
\label{lem:p063-residual-divisor-moving}
Let $C_0$ be a smooth projective connected curve of genus $g$ over an
infinite algebraically closed field $k_0$, let $M\subset C_0$ be finite, and let
$B\in\operatorname{Div}_{\mathbf Q}(C_0)$ have positive degree.  There are
an integer $N>0$ and an effective integral divisor $A$ such that
\begin{equation}
\label{eq:p063-moving-divisor}
          A\sim NB,
          \qquad
          \operatorname{Supp}(A)\cap M=\varnothing.
\end{equation}
Consequently $B-N^{-1}A$ is a rational multiple of a principal divisor.
\end{lemma}

\begin{lemma}
\label{lem:p063-principal-residual-germ}
Let $K$ be as in \cref{lem:p063-local-tree-affinoid}, let $C$ be a smooth
$K$-analytic curve, and let $v\in C$ be an interior point of type $2$.
Let $C_v$ be its residual smooth projective curve.  Choose finitely many
tangent directions $\xi$ at $v$, let $p_\xi\in C_v(\widetilde K)$ be the
corresponding residual points, and let $r_\xi\in\mathbf Q$ satisfy
\begin{equation}
\label{eq:p063-residual-degree-zero}
                         \sum_\xi r_\xi=0.
\end{equation}
Assume that
\[
                         D=\sum_\xi r_\xi[p_\xi]
\]
is a rational multiple of a principal divisor.  For every $c\in\mathbf R$
there is an ordinary Chambert--Loir--Ducros smooth harmonic germ $h$ at
$v$ such that
\begin{equation}
\label{eq:p063-prescribed-residual-slopes}
                    h(v)=c,
                    \qquad
                    d_\xi h(v)=r_\xi
\end{equation}
in the displayed directions and $d_\xi h(v)=0$ in every other tangent
direction.  Here ordinary smoothness means smoothness for analytic moment
maps, not weak smoothness for harmonic tropicalizations.
\end{lemma}

\begin{proposition}
\label{prop:p063-tree-lisse-ordinary-regularization}
Let $K$ be as above, let $C$ be a smooth proper algebraic $K$-curve, and
let $Y\subset C^{\mathrm{an}}$ be a connected strict affinoid domain
admitting a strictly semistable skeleton that is a finite tree.  Let
$f:Y\to\mathbf R$ be lisse and suppose that $f|_{Y^\circ}$ is
Thuillier-subharmonic.  For every $\varepsilon>0$ there is $g\in C(Y)$
such that
\begin{equation}
\label{eq:p063-lisse-uniform-regularization}
             \lVert g-f\rVert_{L^\infty(Y)}<\varepsilon
\end{equation}
and $g|_{Y^\circ}$ is ordinary Chambert--Loir--Ducros smooth and
plurisubharmonic.
\end{proposition}

\begin{theorem}
\label{thm:p063-current-psh-ordinary-regularization}
Let $K$ be an algebraically closed, complete, nontrivially valued
non-Archimedean field, let $C$ be a smooth proper algebraic $K$-curve,
and let $W\subset C^{\mathrm{an}}$ be open.  For a continuous function
$u:W\to\mathbf R$, the following conditions are equivalent.
\begin{enumerate}
\item
\begin{equation}
\label{eq:p063-current-positivity}
                         \mathrm d'\mathrm d''[u]\geq0.
\end{equation}
\item The function $u$ is Thuillier-subharmonic.
\item For every $x\in W$, there are a connected strict affinoid domain
$Y\subset W$, with $x\in Y^\circ$, and functions $u_n\in C(Y)$ such that
$u_n|_{Y^\circ}$ is ordinary Chambert--Loir--Ducros smooth and
plurisubharmonic,
\begin{equation}
\label{eq:p063-monotone-ordinary-approximation}
                         u_{n+1}\leq u_n\quad\text{on }Y,
                         \qquad
                         u_n\longrightarrow u|_Y
\end{equation}
uniformly on $Y$.
\end{enumerate}
Consequently, in this curve scope, current positivity, Thuillier
subharmonicity, and local membership of a continuous function in the first
ordinary Chambert--Loir--Ducros decreasing-limit stage agree.
\end{theorem}

```

## book-monotone-proof.tex

```latex
% Source-aware proof for the exact candidate statement
% p063_curve_cld_monotone_regularization_statement_20260827.tex.
% Date: 27 August 2026.
% This packet is isolated from the live book and has not received a final
% production-Rethlas verdict.

\paragraph{Imported facts and conventions.}
We use Thuillier's potential theory on smooth strictly analytic curves.
In particular, lisse functions factor through finite semistable skeleta by
\cite[Proposition~3.2.4]{Thu05}, lisse subharmonicity is characterized by
the nonnegativity of the graph Laplacian by
\cite[Proposition~3.4.4]{Thu05}, and every subharmonic function is the
pointwise infimum of a decreasing net of lisse subharmonic functions on
each relatively compact open set by \cite[Theorem~3.4.2]{Thu05}.  We use
the local semistable structure and the insertion of finitely many type
$2$ or type $3$ points into a skeleton from
\cite[\S2.2.3 and Lemma~2.2.22(ii)]{Thu05}.

At a type-$2$ point \(v\), define \(\operatorname{div}_v(h)\) to be the
divisor whose coefficient at the residual point \(p_\xi\) is the outgoing
slope \(d_\xi h(v)\).  With this definition the smooth image is the
principal subspace.  If the source uses the globally opposite divisor-sign
convention, both residual maps below are multiplied by \(-1\); the
principal subspace is invariant under this change, and the prescribed
outgoing slopes are unchanged.  The two exact residual-divisor sequences
used below are proved in \cite[Lemma~2.3.22]{Thu05}.  The identification of the
subsheaf generated by local analytic units with the sheaf of ordinary
Chambert--Loir--Ducros smooth harmonic functions is
\cite[Remark~15.10]{GJR26}.  This is the ordinary smooth sheaf, not the
weakly smooth sheaf of harmonic tropicalizations.

\begin{proof}[Proof of \cref{lem:p063-local-tree-affinoid}]
Replace \(C\) first by the smooth projective compactification of the
connected component containing \(x\).  The original analytification is an
open subspace of the compactification, so \(W\) is unchanged for the local
question.  If \(x\) is of type \(2\), \(3\), or \(4\), choose a simple
connected open neighbourhood \(U\subset W\) of \(x\) such that
\[
                         \mathbb H(U):=U\setminus U(K)
\]
is an \(\mathbf R\)-tree.  Such neighbourhoods form a fundamental system by
\cite[Corollary~4.27 and Proposition~5.9]{BPR13Structure}.

Strict affinoid neighbourhoods form a fundamental system on a smooth strict
analytic curve; see the proof of \cite[Corollary~2.1.18]{Thu05}.  Hence
there is a strict affinoid neighbourhood \(A\) of \(x\) with \(A\subset U\).
Let \(Y\) be the connected component of \(A\) containing \(x\).  A strict
affinoid algebra has finitely many connected components, each cut out by an
idempotent.  Thus \(Y\) is a connected strict affinoid domain.  Since
\(x\in A^\circ\) and \(Y\) is open and closed in \(A\), we also have
\(x\in Y^\circ\).

By \cite[Theorem~2.3.8]{Thu05}, after a finite separable extension of \(K\),
the domain \(Y\) admits a strictly semistable formal model.  The extension is
trivial because \(K\) is algebraically closed.  Its skeleton \(\Gamma_0\) is
a finite connected metric graph contained in
\(\mathbb H(Y)\subset\mathbb H(U)\).  An \(\mathbf R\)-tree contains no
embedded circuit, so \(\Gamma_0\) is a finite metric tree.

If \(x\) is of type \(1\), use
\cite[Corollary~4.27(1)]{BPR13Structure} to identify an open neighbourhood
\(U\subset W\) with the standard open unit ball.  In a coordinate \(T\),
choose \(R\in|K^\times|\) with \(|T|_x<R<1\) and put
\[
                         Y=\{|T|\leq R\}.
\]
Then \(Y\) is a connected strict affinoid neighbourhood of \(x\), and its
one-point Gauss skeleton \(\Gamma_0\) is a finite tree.

Let now \(f\) be lisse on a neighbourhood of \(Y\).  By
\cite[Proposition~3.2.4]{Thu05}, after a strictly semistable refinement there
are a retraction \(\tau:Y\to\Gamma\) and a continuous piecewise affine
function \(F\) on \(\Gamma\) such that \(f|_Y=F\circ\tau\).  Take a common
semistable refinement with \(\Gamma_0\) and insert all type-\(2\)
breakpoints; retain every type-\(3\) breakpoint as a metric subdivision
point.  The refined skeleton is still contained in
\(\mathbb H(Y)\subset\mathbb H(U)\); in the type-\(1\) case it lies in the
norm-point tree of the open ball.  Hence it is a finite metric tree.  After
the indicated subdivision, \(F\) is affine on each edge, and every added
interior vertex is of type \(2\) or type \(3\).
\end{proof}

\begin{proof}[Proof of
\cref{lem:p063-tree-rational-strictification}]
If \(\Gamma\) has no edge, take \(G=F\).  Assume henceforth that it has an
edge.  Choose \(b\in\partial\Gamma\), regard \(b\) as the root, and put
\[
                 I=V(\Gamma)\setminus\partial\Gamma.
\]
Define \(\mu:V(\Gamma)\to\mathbf Z\) by
\[
 \mu(v)=
 \begin{cases}
  1,&v\in I,\\
  0,&v\in\partial\Gamma\setminus\{b\},\\
  -\#I,&v=b.
 \end{cases}
\]
Thus \(\sum_v\mu(v)=0\).

For an edge \(e\), let \(\Gamma_e\) be the component of
\(\Gamma\setminus e^\circ\) not containing \(b\), and orient \(e\) from
\(\Gamma_e\) towards \(b\).  Prescribe on \(e\) the slope
\[
                         s_e=\sum_{v\in\Gamma_e}\mu(v)
\]
and normalize the resulting piecewise affine function \(\psi\) by
\(\psi(b)=0\).  The absence of circuits makes these prescriptions
compatible and determines \(\psi\).  If \(v\ne b\), the outgoing slope on
the edge from \(v\) to its parent is
\[
 \mu(v)+\sum_{\substack{e\text{ joining }v\\
                        \text{to a child subtree}}}s_e,
\]
whereas the outgoing slope from \(v\) towards a child subtree is
\(-s_e\).  Therefore
\[
                         \Delta_\Gamma\psi(v)=\mu(v).
\]
The same equality at \(b\) follows from \(\sum_v\mu(v)=0\).  In
particular,
\begin{equation}
\label{eq:p063-unit-interior-laplacian}
                         \Delta_\Gamma\psi(v)=1
                         \qquad(v\in I).
\end{equation}

Choose \(\delta>0\) so small that
\[
                   \delta\lVert\psi\rVert_\infty
                   <\frac{\varepsilon}{2}.
\]
Then \(H=F+\delta\psi\) satisfies
\[
                         \Delta_\Gamma H(v)\geq\delta
                         \qquad(v\in I)
\]
by \eqref{eq:p063-graph-subharmonicity} and
\eqref{eq:p063-unit-interior-laplacian}.  Denote the slope of \(H\) on an
oriented edge \(e\) by \(a_e\), and choose \(q_e\in\mathbf Q\) with
\[
                         |q_e-a_e|<\eta.
\]
There is a unique continuous function \(G\) with \(G(b)=H(b)\) and slope
\(q_e\) on every oriented edge.  If \(d\) is the largest valency of a
vertex and \(L\) is the sum of all edge lengths, then
\[
 |\Delta_\Gamma G(v)-\Delta_\Gamma H(v)|\leq d\eta,
 \qquad
 \lVert G-H\rVert_\infty\leq L\eta.
\]
The second estimate follows by integration along the unique path from
\(b\).  Taking
\[
              d\eta<\frac{\delta}{2},
              \qquad
              L\eta<\frac{\varepsilon}{2}
\]
proves \eqref{eq:p063-graph-rational-error} and
\eqref{eq:p063-graph-strict-mass}.
\end{proof}

\begin{proof}[Proof of \cref{lem:p063-residual-divisor-moving}]
After replacing a denominator-clearing integer by a sufficiently large
multiple, choose \(N\) so that \(NB\) is integral and
\[
                         \deg(NB)\geq2g+1.
\]
Put \(L=\mathcal O_{C_0}(NB)\).  For every \(p\in C_0\), Serre duality
gives
\[
 H^1(C_0,L(-p))
 \simeq
 H^0\bigl(C_0,\omega_{C_0}\otimes L^{-1}(p)\bigr)^\vee.
\]
The line bundle on the right has degree
\[
                   2g-1-\deg L<0,
\]
so \(H^1(C_0,L(-p))=0\).  The exact sequence
\[
 0\longrightarrow L(-p)\longrightarrow L
   \longrightarrow L|_p\longrightarrow0
\]
therefore makes \(H^0(C_0,L)\to L|_p\) surjective.  Its kernel is a
proper linear subspace.

For \(p\in M\), choose a nonzero \(k_0\)-linear functional
\(\lambda_p:H^0(C_0,L)\to k_0\) representing evaluation after a
trivialization of \(L|_p\).  The polynomial
\[
                         \prod_{p\in M}\lambda_p
\]
is nonzero.  A nonzero polynomial on a finite-dimensional vector space
over an infinite field cannot vanish everywhere; this follows by
induction on the dimension from the corresponding assertion in one
variable.  We may choose \(s\in H^0(C_0,L)\) with \(s(p)\ne0\) for every
\(p\in M\).  Its zero divisor \(A=(s)_0\) is effective, is disjoint from
\(M\), and satisfies
\[
                         \mathcal O_{C_0}(A)\simeq L
                         \simeq\mathcal O_{C_0}(NB).
\]
Thus \eqref{eq:p063-moving-divisor} holds.  Moreover,
\[
                         N\left(B-\frac1N A\right)=NB-A
\]
is principal.
\end{proof}

\begin{proof}[Proof of \cref{lem:p063-principal-residual-germ}]
Let \(\mathcal H_v\) be the stalk of Thuillier harmonic germs and let
\(\mathcal F_v\) be the stalk generated over \(\mathbf R\) by germs
\(\log|f|\), with \(f\) an invertible analytic function.  The proof of
\cite[Lemma~2.3.22]{Thu05} gives exact sequences
\begin{align}
 0&\longrightarrow\mathbf R\longrightarrow\mathcal H_v
 \xrightarrow{\operatorname{div}_v}
 \operatorname{Div}(C_v)\otimes_{\mathbf Z}\mathbf R
 \xrightarrow{\deg}\mathbf R\longrightarrow0,
\label{eq:p063-harmonic-residual-exact}\\
 0&\longrightarrow\mathbf R\longrightarrow\mathcal F_v
 \xrightarrow{\operatorname{div}_v}
 \operatorname{Prin}(C_v)\otimes_{\mathbf Z}\mathbf R
 \longrightarrow0.
\label{eq:p063-smooth-residual-exact}
\end{align}
The coefficient at \(p_\xi\) is the outgoing slope \(d_\xi h(v)\).
By \eqref{eq:p063-residual-degree-zero}, the divisor \(D\) lies in the
image of the first residual map.  Its class in
\(\operatorname{Pic}^0(C_v)\otimes_{\mathbf Z}\mathbf R\) vanishes
because it is a rational multiple of a principal divisor.  Comparing
\eqref{eq:p063-harmonic-residual-exact} and
\eqref{eq:p063-smooth-residual-exact} gives a germ in \(\mathcal F_v\)
with residual divisor \(D\); adjusting by a constant gives a germ \(h\)
with \(h(v)=c\).
The construction in the proof of Thuillier's lemma permits a
representative containing short arms in every one of the finitely many
displayed directions.

By \cite[Remark~15.10]{GJR26}, \(\mathcal F\) is exactly the sheaf of
ordinary Chambert--Loir--Ducros smooth harmonic functions on a smooth
boundaryless analytic curve.  Hence \(h\) has all the properties in
\eqref{eq:p063-prescribed-residual-slopes}.
\end{proof}

\begin{proof}[Proof of
\cref{prop:p063-tree-lisse-ordinary-regularization}]
By \cite[Proposition~3.2.4]{Thu05}, after a semistable refinement and a
finite metric subdivision, there are a finite metric tree \(\Gamma\), a
retraction \(\tau:Y\to\Gamma\), and a continuous edgewise affine function
\(F\) such that
\[
                         f=F\circ\tau.
\]
Here no extension of scalars is needed because \(K\) is algebraically
closed.  Include every breakpoint and branch point among the metric
vertices, and let \(\partial\Gamma\) contain the vertices over the Shilov
boundary of \(Y\).  Interior vertices are of type \(2\) or type \(3\).
Subharmonicity and \cite[Proposition~3.4.4]{Thu05} give
\[
                         \Delta_\Gamma F(v)\geq0
                         \qquad
                         \bigl(v\notin\partial\Gamma\bigr).
\]
If \(\Gamma\) has no edge, then \(f\) is constant and there is nothing to
prove.  Otherwise apply
\cref{lem:p063-tree-rational-strictification}, with error
\(\varepsilon/3\), to obtain a rational-slope function \(G\) satisfying
\begin{equation}
\label{eq:p063-tree-graph-error}
 \lVert G\circ\tau-f\rVert_{L^\infty(Y)}
 <\frac{\varepsilon}{3}
\end{equation}
and
\begin{equation}
\label{eq:p063-tree-positive-vertex-mass}
                         \Delta_\Gamma G(v)>0
                         \qquad
                         \bigl(v\notin\partial\Gamma\bigr).
\end{equation}

We first modify \(G\circ\tau\) near each interior type-\(2\) vertex
\(v\).  Choose pairwise disjoint simple star neighbourhoods
\(U_v\Subset Y^\circ\).  Such a neighbourhood contains short arms in all
graph directions, and all but finitely many other tangent directions are
open-disc components contained in \(U_v\).  Let \(E_v\) be the finite set
of exceptional directions.  Enlarge
\[
 M_v=\{p_{v,e}:e\ni v\}\subset C_v(\widetilde K)
\]
by the residual points corresponding to \(E_v\).  This is the finite
forbidden set; in particular it contains every graph direction and every
direction in which a fresh collar is not available.

Define
\[
                         B_v
   =\sum_{e\ni v}d_eG(v)[p_{v,e}]
   \in\operatorname{Div}_{\mathbf Q}(C_v).
\]
By \eqref{eq:p063-tree-positive-vertex-mass},
\[
                         \deg B_v
                         =\Delta_\Gamma G(v)>0.
\]
Apply \cref{lem:p063-residual-divisor-moving} to \(B_v\) and \(M_v\).
There are \(N_v>0\) and an effective divisor
\[
                         A_v=\sum_{p\in S_v}m_{v,p}[p]
\]
such that
\[
 A_v\sim N_vB_v,
 \qquad
 S_v\cap M_v=\varnothing.
\]
Thus
\[
                         D_v
    =B_v-\frac1{N_v}A_v
\]
has degree zero and is a rational multiple of a principal divisor.  By
\cref{lem:p063-principal-residual-germ}, there is an ordinary smooth
harmonic germ \(h_v\), normalized by \(h_v(v)=G(v)\), whose graph slopes
are \(d_eG(v)\), whose slopes in the fresh directions \(p\in S_v\) are
\[
                         -a_{v,p},
             \qquad
                         a_{v,p}=\frac{m_{v,p}}{N_v}>0,
\]
and whose slopes in all remaining directions vanish.

We now choose one representative on one neighbourhood, rather than making
direction-by-direction choices.  Write it as a finite real linear
combination of logarithms of analytic units.  After one common shrink, each
unit has a rational reduction on \(C_v\); the union \(T_v\) of the supports
of their divisors is finite.  On every reduction fibre outside \(T_v\),
the absolute value of every unit is constant.  In a direction belonging to
\(T_v\) but not to the support of \(D_v\), the sum has outgoing slope zero;
after shrinking the finitely many such annular collars, its affine germ is
therefore constant.  This uses the reduction-fibre description of a simple
type-\(2\) neighbourhood in
\cite[\S4.29 and Lemma~5.12(3)]{BPR13Structure}.

Shrink once more along the finitely many graph and fresh directions.  On
this single neighbourhood, \(h_v\) agrees with \(G\circ\tau\)
simultaneously on every graph collar and on every zero-slope overlap: on a
graph collar the two functions have the same value and affine slope, and on
all remaining directions both are constant with value \(G(v)\).  The
avoidance of \(E_v\) ensures that each \(p\in S_v\)
determines an available open-disc component of \(Y\setminus\{v\}\),
disjoint from \(\Gamma\).

We cap the negative slope in each of these fresh directions.  Fix an even
nonnegative function \(\rho\in C^\infty_c((-1,1))\) of integral one and
put
\[
 \chi_\eta(r)=\int_{\mathbf R}|r-\eta s|\rho(s)\,\mathrm ds,
 \qquad
 m_\eta(s,t)=\frac{s+t+\chi_\eta(s-t)}2.
\]
Then \(m_\eta\) is smooth, convex, and nondecreasing in each variable,
\begin{equation}
\label{eq:p063-regularized-max-bounds}
 \max\{s,t\}\leq m_\eta(s,t)
       \leq\max\{s,t\}+\frac{\eta}{2},
\end{equation}
and it equals \(\max\{s,t\}\) if \(|s-t|\geq\eta\).  Indeed, Jensen's
inequality gives \(\chi_\eta(r)\geq|r|\), the triangle inequality gives
\(\chi_\eta(r)\leq|r|+\eta\), evenness gives zero first moment, and hence
\(\chi_\eta(r)=|r|\) for \(|r|\geq\eta\).  Also
\(|\chi_\eta'|\leq1\) and \(\chi_\eta''\geq0\).

Fix \(p\in S_v\).  On a sufficiently short punctured neighbourhood in its
open-disc component, choose an invertible annular coordinate \(T\) and a
constant \(c\) such that
\[
                         t=-\log|T|+c\geq0
\]
is distance from \(v\) on the skeleton.  Shrinking the whole annular tube,
not merely its skeletal arm, we have
\[
                         h_v=G(v)-a_{v,p}t.
\]
Choose \(r_{v,p}>0\) and \(\eta_{v,p}>0\) so that
\[
 \eta_{v,p}<a_{v,p}r_{v,p},
 \qquad
 r_{v,p}+\frac{\eta_{v,p}}{a_{v,p}}
\]
lies inside the arm on which this formula holds, and
\begin{equation}
\label{eq:p063-fresh-collar-error-choice}
 a_{v,p}r_{v,p}+\frac{\eta_{v,p}}2
 <\frac{\varepsilon}{3}.
\end{equation}
On that entire annular tube set
\begin{equation}
\label{eq:p063-fresh-collar-cap}
 q_{v,p}(t)
  =
 m_{\eta_{v,p}}\bigl(
     G(v)-a_{v,p}t,\,
     G(v)-a_{v,p}r_{v,p}
   \bigr).
\end{equation}
It equals \(h_v\) on
\[
               0\leq t<
               r_{v,p}-\frac{\eta_{v,p}}{a_{v,p}}
\]
and equals the constant \(G(v)-a_{v,p}r_{v,p}\) when
\[
               t>
               r_{v,p}+\frac{\eta_{v,p}}{a_{v,p}}.
\]
The same formula therefore assigns values on all residue discs attached to
the skeletal arm.  Extend it by that constant over the rest of the
open-disc component in the direction \(p\).  No return to the old constant
\(G(v)\) is made or needed.  By
\eqref{eq:p063-regularized-max-bounds},
\begin{equation}
\label{eq:p063-fresh-collar-error}
 \left|q_{v,p}-G(v)\right|
 \leq a_{v,p}r_{v,p}+\frac{\eta_{v,p}}2
 <\frac{\varepsilon}{3}.
\end{equation}

The function in \eqref{eq:p063-fresh-collar-cap} is ordinary smooth and
psh.  Indeed, \(t\) differs by a constant from \(-\log|T|\) for an
invertible analytic annular coordinate, and
\eqref{eq:p063-fresh-collar-cap} is a smooth convex function of \(t\) on
the whole annular tube.
Equivalently, it is a smooth convex coordinatewise nondecreasing
regularized maximum of the ordinary smooth harmonic functions \(h_v\)
and \(G(v)-a_{v,p}r_{v,p}\).  Near \(v\) every cap equals \(h_v\), while
at its far end it equals its constant extension on an open overlap.
Since \(S_v\) is finite, the modifications therefore glue around \(v\)
to an ordinary smooth psh function.

It remains to smooth the corners at interior type-\(3\) subdivision
vertices.  A smooth analytic curve has exactly two tangent directions at
such a point.  In an annular coordinate \(t\), with the vertex at \(0\),
write
\[
 G(t)=
 \begin{cases}
  G(v)+\alpha t,&t\leq0,\\
  G(v)+\beta t,&t\geq0.
 \end{cases}
\]
The outgoing-slope sum is \(\beta-\alpha\), so
\eqref{eq:p063-tree-positive-vertex-mass} gives \(\alpha<\beta\), and
\[
 G(t)=\max\{G(v)+\alpha t,G(v)+\beta t\}.
\]
Choose a collar on which the two affine formulas hold and which is disjoint
from every other replacement collar.  On that collar replace this maximum
by
\[
 m_\eta\bigl(G(v)+\alpha t,G(v)+\beta t\bigr).
\]
Choose \(\eta>0\) so small that
\(\eta/(\beta-\alpha)\) lies strictly inside this chosen collar.  The
replacement agrees with \(G\) whenever
\[
                         |t|>\frac{\eta}{\beta-\alpha},
\]
is ordinary smooth and psh, and differs from \(G\) by at most
\(\eta/2\).  Decrease \(\eta\), if necessary, so that also
\(\eta<2\varepsilon/3\).

There are only finitely many interior type-\(2\) and type-\(3\) vertices,
so all graph collars can be chosen pairwise disjoint.  At a type-\(2\)
vertex the central function is \(h_v\); on every graph or zero-slope arm
it equals \(G\circ\tau\) on an open overlap.  Every fresh direction is
off the graph, different fresh directions give disjoint open-disc
components, and the cap equals its constant continuation on an open
overlap.  The type-\(3\) replacement equals \(G\circ\tau\) on open
overlaps at both ends.  Away from these collars,
\(G\circ\tau\) is either affine in an ordinary annular coordinate or
locally constant.  Thus all local functions glue to a continuous
function \(g\) on \(Y\), and \(g|_{Y^\circ}\) is ordinary smooth and psh.
Boundary vertices need no smoothing because smoothness is asserted only
on \(Y^\circ\).

The local replacement supports are disjoint.  By
\eqref{eq:p063-fresh-collar-error} and the type-\(3\) error bound,
\[
                \lVert g-G\circ\tau\rVert_{L^\infty(Y)}
                    <\frac{\varepsilon}{3}.
\]
Together with \eqref{eq:p063-tree-graph-error}, this gives
\[
                         \lVert g-f\rVert_{L^\infty(Y)}
                         <\frac{2\varepsilon}{3}<\varepsilon,
\]
which proves \eqref{eq:p063-lisse-uniform-regularization}.
\end{proof}

\begin{proof}[Proof of
\cref{thm:p063-current-psh-ordinary-regularization}]
The equivalence between
\eqref{eq:p063-current-positivity} and Thuillier subharmonicity for
continuous functions is \cite[Corollary~4.8]{Wanner19}.
We prove that condition \(2\) implies condition \(3\).

Fix \(x\in W\).  By \cref{lem:p063-local-tree-affinoid}, choose a connected
strict affinoid tree domain \(Y\subset W\) with \(x\in Y^\circ\).  Choose
an open set \(\Omega\) with
\[
                         Y\subset\Omega\Subset W.
\]
Thuillier's approximation theorem
\cite[Theorem~3.4.2]{Thu05} gives a decreasing net
\((f_i)_i\) of lisse subharmonic functions on \(\Omega\), converging
pointwise to \(u\).  Its restriction to the compact space \(Y\) converges
uniformly.  Indeed, for \(\delta>0\), the increasing family of open sets
\[
                         U_i=\{y\in Y:f_i(y)-u(y)<\delta\}
\]
covers \(Y\).  A finite subcover and directedness provide one index \(i\)
with \(U_i=Y\).  This is the net form of Dini's argument; it uses the
continuity of \(u\) and of every \(f_i\).

Put \(b_n=4^{-n}\).  Recursively choose an increasing sequence of indices
\(i_n\) such that
\[
                         \lVert f_{i_n}-u\rVert_{L^\infty(Y)}
                         <\frac{b_n}{2}.
\]
At the \(n\)-th step, take a common upper bound of \(i_{n-1}\) and an
index supplied by uniform convergence.  Apply
\cref{prop:p063-tree-lisse-ordinary-regularization} to
\(f_{i_n}|_Y\), with error \(b_n/2\).  We obtain \(g_n\in C(Y)\), ordinary
smooth and psh on \(Y^\circ\), with
\begin{equation}
\label{eq:p063-raw-uniform-error}
                         \lVert g_n-u\rVert_{L^\infty(Y)}<b_n.
\end{equation}

The functions \(g_n\) need not be ordered.  Define
\begin{equation}
\label{eq:p063-tail-shift}
                         c_n
   =\sum_{j=n}^{\infty}(b_j+b_{j+1}),
   \qquad
                         u_n=g_n+c_n.
\end{equation}
Since \(c_n-c_{n+1}=b_n+b_{n+1}\),
\eqref{eq:p063-raw-uniform-error} gives, pointwise on \(Y\),
\[
 \begin{aligned}
 u_{n+1}-u_n
   &=
 g_{n+1}-g_n-(b_n+b_{n+1})\\
   &\leq
 |g_{n+1}-u|+|g_n-u|-(b_n+b_{n+1})
 \leq0.
 \end{aligned}
\]
Thus \(u_{n+1}\leq u_n\).  Moreover,
\[
                         \lVert u_n-u\rVert_\infty
                         \leq b_n+c_n\longrightarrow0.
\]
Adding constants preserves ordinary smoothness and psh.  This proves
\eqref{eq:p063-monotone-ordinary-approximation}.

Finally assume condition \(3\).  On \(Y^\circ\), each
\(\mathrm d'\mathrm d''[u_n]\) is a positive current.  Uniform convergence
gives \([u_n]\to[u]\) as currents: for every compactly supported smooth
test function \(\varphi\), the absolute value of
\[
 \bigl\langle [u_n-u],\mathrm d'\mathrm d''\varphi\bigr\rangle
\]
is at most \(\lVert u_n-u\rVert_\infty\) times the total variation of the
compactly supported smooth signed measure
\(\mathrm d'\mathrm d''\varphi\).  Hence
\[
                    \mathrm d'\mathrm d''[u_n]
                    \longrightarrow
                    \mathrm d'\mathrm d''[u]
\]
weakly.  Positivity is closed under weak convergence, so
\(\mathrm d'\mathrm d''[u]\geq0\) on \(Y^\circ\).  These interiors cover
\(W\), proving condition \(1\).

Condition \(3\) is exactly local membership, for continuous functions, in
the first decreasing-limit stage generated by ordinary smooth psh
functions.  The convergence obtained above is even uniform.
\end{proof}

```

# Bibliography and precisely identified standard foundations


* A. Chambert-Loir and A. Ducros, *Formes différentielles réelles et courants
  sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025.
* W. Gubler and J. Rabinoff, *Classically psh and pluriharmonic functions on
  Berkovich spaces*, arXiv:2506.13548v2, 17 September 2025.
* W. Gubler, P. Jell, J. Rabinoff, *Forms on Berkovich spaces based on harmonic
  tropicalizations*, arXiv:2111.05741v3, 7 March 2025. Sections 7.8--7.15
  were examined; their two local limits are not used as a first-stage sequence.
* V. Wanner, *Comparison of two notions of subharmonicity on non-archimedean
  curves*, arXiv:1801.04713v3; Math. Z. 293 (2019), 443--474.
* M. van der Put, *The class group of a one-dimensional affinoid space*,
  Ann. Inst. Fourier 30(4) (1980), 155--164, Theorem 1.1 and its proof.
* A. Thuillier, thesis, HAL tel-00010990v1, Sections 2.2 and 2.3 and
  Proposition 3.2.4. Theorem 2.3.8's semistable-reduction input is the
  classical smooth proper curve stable-reduction theorem: after a finite
  separable extension a smooth proper curve over a complete nontrivially
  valued field has a strictly semistable formal model; the algebraically
  closed case needs no field extension. Its precise use is given in the
  complete Thuillier proof reproduced here.
* V. Berkovich, *Étale cohomology for non-Archimedean analytic spaces*,
  Publ. Math. IHÉS 78 (1993), Sections 1.5--1.6; the strict affinoid-domain
  comparison is used, not a global nonparacompact category equivalence.
* S. Bosch, U. Güntzer, R. Remmert, *Non-Archimedean Analysis* (1984),
  3.2.4/2 and 6.1.2/1, finite valued-field norms and the strict affinoid
  Nullstellensatz, as stated exactly in T and C. No new BGR retrieval.
* R. Hartshorne, *Algebraic Geometry* (1977), III.7.6 (Serre duality for
  a smooth projective curve) and IV.1.3 (Riemann--Roch). R5 uses only
  H1(L(-p)) dual to H0(omega tensor L inverse(p)), and negative-degree
  line bundles have no nonzero global section. A nonzero section's zero
  divisor is effective and represents L, providing the full moving proof.



# Complete supporting proofs supplied for independent reconstruction

These are mathematical evidence, not grants of assumptions. Each application and dependency must be reconstructed. Prior verdicts and hashes do not replace these proofs.
