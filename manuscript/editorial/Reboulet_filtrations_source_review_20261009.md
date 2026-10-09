# Filtrations and asymptotic norms: complete 2026 revision audit

Date: 9 October 2026. Controlling primary: Rémi Reboulet,
*Filtrations and asymptotic geometry of non-Archimedean norms on section
rings*, arXiv:2508.16322v2, revision stamped 3 March 2026. The internal
title page says 4 March 2026. The 39-page PDF has SHA256
728d65e1be5e0471016b429bea9010b20267a61ca1b6637a04c0c6edee270c08.
All 39 physical pages were actually read in order using complete selected
text, twenty individually displayed matching images and twenty
chronological notes/receipts. Preparation flags remain frozen false.

This audit isolates useful finite-dimensional constructions from the
additional graded, radial and pluripotential proof interfaces. It does
not establish Main Theorems A–C as recursively complete, declare their
intended corrected formulations false, or supply an independent
hostile-model receipt. The active 4,661-page book, its 425 core TeX
inputs, bibliographies and native open-problem editor are unchanged in
this checkpoint. The canonical 42 active atoms/twelve formal problems
retain their statuses. General BJ22 critical homogeneous Siu/envelope
bridges remain OPEN, LPWZ density UNVERIFIED, and the author's warning
about the proof of BJ22 Theorem 6.21 remains binding.

## Finite norms and the product-gauge construction

The finite construction distinguishes two norm categories on the same
finite-dimensional vector space over a complete non-Archimedean field:
norms homogeneous for its given absolute value and norms homogeneous
for the trivial absolute value. A filtration norm is not an ordinary
norm for the given absolute value. Let eta belong to the first category
and F to the second. Definition 1.20 and Lemma 1.24 define A(F,eta) as
the largest genuine norm dominated by eta(v)F(v), equivalently the
infimum over finite decompositions of the maximum of these product
gauges. The product itself need not be a norm. In finite rank its
positive finite filtration levels provide a lower positive multiple
of eta, making the envelope nonempty and definite.

The envelope is monotone and commutes with positive scalar
multiplication. Consequently product comparisons directly prove
Theorem 1.33's joint infinity contraction: if the two input distances
are C and D, their gauges differ by factors at most exp(C+D), and so
do their envelopes. This direct argument avoids the index and constant
slips in the printed approximation proof. It requires no spherical
completeness or exact simultaneous splitting.

For a split eta, Theorem 1.22 supplies a basis jointly adapted to eta
and F; the action multiplies the diagonal weights. The exact basis
input is attributed to Gérardin 1981 and BE21 Proposition 1.14. For
general norms, density of diagonalizable norms is weaker than exact
splitting and must remain so. Proposition 1.25 records scalar-extension
and restriction comparisons; an inequality, or equality on original
field vectors, is not by itself equality on all extension vectors.
The present checkpoint does not promote an additional scalar-extension
theorem from this interface.

Lemma 1.34's determinant factorization, the maximum-of-norms identity
and signed-volume monotonicity give the finite d1 contraction in
Theorem 1.36 after the probability normalization below is restored.
In a genuine common apartment the coordinatewise construction preserves
all finite-p spectral distances. This is an actual three-norm
common-basis premise, not a statement that every such triple splits.
The word “action” also does not imply an associative multiplication on
filtration norms; Remark 1.21 explicitly warns of nonassociativity.

## Calibrating the literal formulas

Successive minima use lambda=log(eta prime/eta) and the spectral measure
is the probability average over rank n>0. Its signed mean is therefore
the determinant logarithmic ratio divided by n. Theorem 1.15 omits
that division: scaling the second norm by exp(c) gives mean c but
determinant total nc. In Remark 1.13 the joint coordinates
x=-log eta and y=-log eta prime must push forward by x-y, not y-x.
These conventions must be repaired consistently before using volumes.

With vol(F)=vol(F,trivial)=-mean log F, the correct power identity is

    vol(tF,sG)
      = s vol(F,G)+(t-s)vol(F)
      = t vol(F,G)+(t-s)vol(G).

The two occurrences of s-t in Proposition 1.16(6) and its graded
counterpart have the wrong sign. Rank-one F=exp(-3), G=exp(-1),
t=2, s=1 gives actual volume 5; the printed alternatives give -1 and 3.
The degree-normalized metric formula in the introduction and §2.2 also
needs its last power:

    d_p^p = integral |lambda|^p d sigma
          = lim_m (d_{p,m}/m)^p.

For scalar normalized slopes 2 and p=2 the moment is 4, whereas
the unpowered normalized distance is 2. Signed volume, absolute d1
distance and the strong infinity distance remain separate quantities.

Several other displayed slips are recorded in the actual notes:
self-ratios in Lemma 1.27, missing primes in Lemma 1.30 and
Theorem 1.51, and a constant 3d where the displayed powers give 5d in
the proof of Proposition 1.32. They do not replace the direct envelope
comparison or prove that an intended continuity statement is false.
Likewise an empty family of norms has no positive-definite supremum,
so supremum assertions require nonempty families. The finite apartment
distance uses the probability-normalized l_p norm, including n^(-1/p).

## Selected rays and the graded boundedness premise

The geodesics in Definition 1.38 are the specified interpolation
envelopes. Definition 1.45 requires every segment of a ray to be one
of these selected geodesics; an arbitrary d1 metric geodesic is a
different object. Lemma 1.46's displayed positive lower estimate is
false already for eta_t=exp(10+t)|.|: at s=1 it bounds the root limit
exp(1) below by exp(10). The proper speed bound retains the initial
norm, exp(-Ct)eta_0(v)<=eta_t(v)<=exp(Ct)eta_0(v), and its t-th root
has the required finite positive limit. Root-limit preservation of
ultrametric inequalities is then a separate direct step.

The corrected ray-apartment input is Parreau 2000 Proposition 2.18,
not yet primary-read here. The general proof of Theorem 1.51 also
passes to a spherically complete extension. The displayed restriction
identity of Lemma 1.48 does not alone identify the complete extended
root-limit norm with scalar extension of the original direction.
That compatibility needs its own justification before this proof can
be imported. The statement's two identical unprimed directions are
another literal slip: scalar rays of slopes 1 and 2 have radial
distance 1, whereas the printed right side is zero.

In §2.1 a graded norm is called bounded if it has O(m) distance from
some unrestricted graded norm. Choosing itself as the comparison makes
this condition vacuous. On (P1_K,O(1)), let eta be the Gauss graded
norm and set zeta_m=exp(-m^2)eta_m, with degree zero unchanged. The
family is submultiplicative, since (m+n)^2>=m^2+n^2. It satisfies
the literal comparison definition but its strong distance from eta is
infinite and its normalized relative laws are delta_m, escaping to
infinity. The compact spectral theory requires a fixed admissible
degree-one/model reference or an independently specified linearly
bounded class. This example does not challenge that properly bounded
theory. Its proof interfaces still retain their original ample,
projective, integral/valuation and coefficient hypotheses from CM15,
Reb21a and BE21 Theorem 9.5.

The finite-p asymptotic quotient is also weaker than the strong
infinity metric. The genuine bounded monomial norms with weights
(exp(m),1,...,1) on H0(P1,O(m)) have normalized finite-p distance
(m+1)^(-1/p) from the Gauss norm, but strong infinity distance 1.
Finite-rank equivalence constants cannot be reused uniformly as rank
grows with section degree.

## The radial-volume convergence step

Proposition 2.12 constructs the geodesic from a common initial norm
to the maximum of two time-t ray endpoints. At fixed s these chords
increase as t increases. Page 30 invokes Proposition 2.1(4), claiming
that strong graded infinity convergence follows once they are uniformly
bounded. That proposition gives a bounded supremum norm, not uniform
convergence over section degree. Pages 31–32 then use the asserted
strong convergence to conclude that the limit is a geodesic and to
pass signed volume to the limit. They provide no additional uniform
tail estimate at this step.

A direct boundary to the general inference is

    zeta^(k)_m = exp(min(m,k)) eta_m,
    zeta_m     = exp(m) eta_m.

These are submultiplicative because min(m+n,k)<=min(m,k)+min(n,k).
They increase to zeta at each fixed degree and share the genuine
linear bound 0<=min(m,k)<=m. Yet

    d_infinity(zeta^(k),zeta)
      = sup_m (m-min(m,k))/m = 1

for every finite k. This example refutes monotone boundedness as a
general sufficient condition for strong convergence. It is not a
counterexample to the special chord family or the intended
Proposition 2.12. That family needs an additional proof, or a weaker
convergence theorem sufficient for the volume passage.

Theorem 2.10 tests probability laws by continuous stop-loss functions
max(x,c), appropriately avoiding discontinuous tail endpoints. Its
scalar chain on pages 32–33 nevertheless puts exp(tc times degree)F
inside an additional power t. The required identity is

    exp(tc times degree) A(tF,eta)
      = A(t(exp(c times degree)F),eta).

The printed powered direction has t squared c instead. Correcting
that scalar, and supplying the volume-of-maximum asymptotic input,
would give the intended conditional stop-loss route. Neither a scalar
display correction nor the preceding generic diagnostic completes the
radial theorem. Existence of general-p radial limits must also not be
deduced solely from the d1/infinity Busemann inequalities stated earlier.

## Flat function domains and finite-energy completions

Section 2.6 cites RWN25 for convex decreasing functions on S, the
support of sigma(F,trivial), but its norm formula evaluates f at every
normalized finite-degree eigenvalue. Those values need not belong to S.
For the same monomial norm with weights (exp(m),1,...,1), the law is
(delta_-1+m delta_0)/(m+1), tending to delta_0. Thus S={0}, while
the constant monomial still requires f(-1). A function given only on
S does not specify that value. A full interval, global extension or
explicit quotient convention needs to be checked against RWN25.

The displayed formula sends f=0 to the trivial norm, contrary to the
opening sentence saying it sends zero to F. It sends f(lambda)=-lambda
to F and f(lambda)=-t lambda to tF. Item 4's constant function -t+c
gives a scalar multiple of the trivial norm; the shifted F formula
needs -lambda+c. The proof of Theorem 2.13 establishes norm membership
under a bounded-right-derivative premise, whereas its statement ranges
over the whole stated bounded convex function class. A limiting
argument or clarified class is required. A singleton support gives
only a one-dimensional cone, and L1 is not strictly convex, so both
the dimension and the introduction's strict flat terminology need
qualification. Exact common apartments also require split premises;
nonsplit norms cannot acquire an orthogonal basis by definition.

An actual isometry extends to metric completions. In contrast,
d_p<=d_q alone produces a map from the q-completion to the
p-completion, not its injectivity. The stated nested completions
therefore need the further structure that prevents distinct strong
boundary points from merging in the weaker metric. The N1/E1
identification in §2.7 is explicitly envelope-dependent and attributed
to adapting BJ22 Theorem 12.8 with BJ25's synthetic inputs. This
paragraph supplies no proof of the adapted identification and does
not bypass the binding BJ22 Siu warning. Original Thuillier/BFJ field
and characteristic hypotheses must be recovered before importing the
known-envelope cases. The p>1 pluripotential characterization is
explicitly left as a research direction.

## Evidence and next source gates

Twelve elementary diagnostic families preserve the calculations and
their precise scope. An initial JSON serializer omitted handling for
exact rational numbers and failed before writing diagnostics; the
dependent finalizer likewise produced no output. Both helpers and the
failure record remain frozen. Fresh v2 adds rational-string
serialization, repeats the checks and finalizes the twenty actual
notes without changing any source page or reading flags. Failure,
preparation, export and upload provide zero reading credit.

The authored archive preserves notes, receipts, diagnostics, records,
helpers and this audit. The separate cloud archive additionally keeps
the external primary PDF, full text, individual images and metadata.
Remote publication receives its own expected-head and byte-verification
record. Continue with the actual RWN25 construction, Parreau's ray
statement, BE21 Theorem 9.5 and the published comparison editions.
The last complete ordered whole-book pass remains the 4 October pass;
this primary audit does not extend it. Cloud-only work and checks for
incoming author updates continue, with Xean suspended.
