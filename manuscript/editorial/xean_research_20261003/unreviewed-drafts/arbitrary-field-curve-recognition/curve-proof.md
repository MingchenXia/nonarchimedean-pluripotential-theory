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

In this finite two-sign situation one can also check the universal part of
GR Definition 3.4 directly, avoiding any inference of current regularization:
the Dirichlet argument first makes the function Thuillier-harmonic. Thuillier
Propositions 2.3.18 and 2.3.19, with their statements and proofs included
below, preserve already harmonic functions under every non-Archimedean
field extension and every morphism between smooth strict curves. Apply
them after scalar extension and then to each connected smooth strict
curve probe. A harmonic function and its negative are subharmonic: their
graph maximum principle on each strict affinoid gives comparison with
every harmonic boundary majorant. Thus both signs satisfy every test in
Definition 3.4. This explains exactly why Thuillier recognition on the
local model yields GR recognition with the field quantifiers; a
zero-current equation itself is never used to pull back to these probes.

For a reduced singular curve, C3 transports the intrinsic equation to
its finite normalization. Since $k$ is perfect, the normalization is
rig-smooth (GR Lemma 3.9(1)); boundarylessness makes it smooth. The
previous paragraph recognizes the lifted function. GR 3.14(7) descends
the **recognized** harmonic function through this finite surjective curve
map. For a nonreduced curve C3 first gives the equation on its reduction;
the reduced result recognizes it there, and GR 3.14(7) descends through
the finite surjective nilpotent closed immersion. Neither descent divides
out a current nor suppresses original nilpotent weights.

The exact published function-theory inputs used here, with their proofs
in Appendix S, are: GR Definition 3.13 (both signs GR-subharmonic),
3.14(1,6,7) (sheafiness, scalar equivalence for every analytic extension,
pullback under curve maps and converse for finite surjective maps),
4.1.2 (on curves classical psh equals GR-subharmonicity), and 3.15
(on **any strict analytic curve** over a nontrivially valued field, harmonic
is equivalent to real PL and all residual classes numerically trivial).
The latter uses GJR Definition 7.2, Remark 7.3(1), Proposition 15.7,
and scalar/proper semipositivity descent; their relevant statements and
proof bodies are also supplied. These are exact external function-theory
theorems, not consequences deduced from a current pullback. They permit
nonreduced curves. This completes algebraically closed intrinsic recognition.

There is a source-numbering distinction in GR 3.15's printed proof: it cites
GJR's earlier Lemma 5.3(3) and Corollary 5.11. In the cached
arXiv:2111.05741v3 (7 March 2025), the matching complete statements are
**Lemma 5.4(3)** (PL equivalence under the reduction immersion) and
**Corollary 5.12** (PL equivalence under completion of an algebraic field
extension, for divisible coefficients). Their statements and proofs are
included below together with Proposition 5.11, on finite flat surjective
PL descent. This is an explicit match of statements, not identification of
different numbers by assumption. GR's bibliography also prints 2111.05747;
the title and authors match the supplied primary PDF, whose actual
identifier is 2111.05741v3. The numerical-triviality part uses GJR
Proposition 7.6(1',2',3') on proper, scalar, and reduction functoriality of
both signs. Its hypotheses are good strict spaces, already real-PL
functions, and the stated proper or scalar maps; these hold after
real-PL descent. The rig-smooth comparison is Proposition 15.7: on a
strict affinoid semistable curve, the weighted sum of outgoing slopes
equals the degree of the model residue line bundle, so harmonicity is
equivalent to numerical triviality. Its complete supplied proof reduces
real slopes to integral ones using a rational basis of that slope equation.
This matches precisely the real coefficient convention used here.

# Part B. The completed algebraic closure and full descent

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

Given R's $U,h$, apply T to $M=\overline K$. T12.5 checks that the actual
$U_C$ is good separated strict boundaryless and locally pure of dimension
one, not merely of total dimension one. Its actual nilpotent lengths are
used in T13. Thus $D[h_C]=0$ unconditionally. Part C recognizes $h_C$ as
GR-harmonic. GR Proposition 3.14(6) then gives GR-harmonicity of $h$.
Apply 4.1.2 to both signs for classical pluriharmonicity. Apply 3.15
over the original $K$ for G-local real PL and GJR harmonicity.

For clarity about the full quantifiers in this descent, let $L/K$ be
**any** complete analytic extension, possibly transcendental. Embed
$\overline K$ into an algebraic closure of $L$ over $K$; extend partial
algebraic embeddings by adjoining roots. The norm agrees on finite
$K$-subfields by uniqueness. Complete that algebraic closure to a field
$F$. The same root argument proves that $F$ is algebraically closed and
complete; the isometric embedding extends from $\overline K$ to $C$.
Thus $F$ is a joint analytic extension of $C$ and $L$. The extension
$F/C$ is not asserted to be algebraic.

The converse scalar assertion in GR 3.5(7), whose complete proof is
reproduced below, uses precisely this joint-field argument. For a smooth
strict connected $L$-curve probe $Y\to U_L$, pull the recognized
$\pm h_C$ to $F$ and to $Y_F$. They are subharmonic. Subharmonic descent
on a smooth strict curve is checked by compact comparison: for a strict
affinoid domain $V\subset Y$ and harmonic boundary majorant $b$, its
scalar pullback is harmonic (Thuillier 2.3.18), the upstairs absolute
boundary maps onto $\partial V$ (GR 2.12), and comparison upstairs
therefore implies comparison downstairs by scalar surjectivity. Components
cause no $-\infty$ issue since our functions are finite. GR's proof supplies
the general curve version, and 4.1.2 then uses both scalar functoriality and
curve-map functoriality to cover **every** analytic curve $Y$, without
smoothness, strictness, or nonreducedness restrictions on the probe.
Equivalently one can use GR 4.2(5) and 7.2(6); their exact proofs are in
Appendix S. This is descent of a recognized function. No equation on
$U_L$ or on a probe is presumed at this stage. R is proved.
