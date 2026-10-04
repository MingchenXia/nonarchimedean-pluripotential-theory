# HNF height slices: coherent models and the boundary of IDP

Date: 4 October 2026. This dossier continues the known
[Sylvester local-model application](sylvester_height_slice_models_20261004.md)
and the [compatible dilation route](li_face_compatible_dilation_and_semistable_scope_20261004.md).
It records source-supported combinatorics and explicit toric consequences.
It does not solve one of the book's 42 open atoms or certify a general
Calabi–Yau, global gluing or semistable-reduction theorem.

## Controlling sources and attribution

Liu–Tang–Tao–Zhang, *Two families of Hermite normal form simplices*,
[arXiv:2609.36818v1](https://arxiv.org/abs/2609.36818v1), supplies the
finite IDP criterion (Theorem 1.6, proof on physical pages 17–18),
the constant-coordinate equivalence with coherent unimodular
triangulations (Theorem 1.4, proof on pages 19–27), and the general
finite triangulation/coherence tests (Theorem 6.1 and Proposition 6.2,
pages 30–31). Its Examples 6.4–6.5, pages 31–32, explicitly import
the Firla–Ziegler obstruction. These are the actual statement headings;
several automatic cross-references in the preprint call lemmas,
propositions or examples “Theorem.”

The constant-coordinate result is explicitly presented as an HNF
specialization of the earlier two-parameter theory of Dais–Haus–Henk
(1998), with Sato (2020) as another antecedent. Those earlier primary
texts have not been freshly acquired in this checkpoint. The displayed
preprint proof is checked below, with no novelty reassignment. Its
Ehrhart results and their imported antecedents are outside the proposed
model application, even though the complete extracted text was read.

Firla–Ziegler, *Hilbert Bases, Unimodular Triangulations, and Binary
Covers of Rational Polyhedral Cones*, Discrete Comput. Geom. 21 (1999),
205–216, [DOI:10.1007/PL00009416](https://doi.org/10.1007/PL00009416),
is inspected in the published PDF. Example 10, printed page 213,
physical page 9, is the controlling obstruction. Section 4, printed
page 212, explicitly says its Hilbert-partition existence tests use
the integer programs of Corollary 5 and CPLEX. Their nonexistence
computation is a published import, not a reproduced certificate here.

## General one-row simplex and exact box criterion

Let d,N >= 2 and 0 <= a_i < N for 1 <= i < d. Put

    S_a = conv(0,e_1,...,e_{d-1},(a_1,...,a_{d-1},N)),
    A = sum_i a_i.

The normalized volume in the original Z^d lattice is N. In the
homogenized cone, coordinates with respect to its vertex generators
give the lattice

    Lambda_a = Z^{d+1} + Z (A-1,-a_1,...,-a_{d-1},1)/N.

Write [x]_N for the least residue in {0,...,N-1}. The fundamental
half-open box consists of

    lambda(t) = ([ (A-1)t ]_N,[-a_1 t]_N,...,[-a_{d-1}t]_N,t)/N,
    0 <= t < N.

Its integral degree is

    H(t) = sum_i ceil(a_i t/N) - floor((A-1)t/N).

The degree-one indices J are precisely those t in {1,...,N-1}
with H(t)=1. The lattice points of S_a are its vertices and

    p_t = (ceil(a_1 t/N),...,ceil(a_{d-1}t/N),t),  t in J.

IDP means every lattice point of k S_a is a sum of k lattice points
of S_a, for every integer k >= 1. Theorem 1.6 gives the finite test:
for every t with H(t)>=2, there must be s in J with 1<=s<t and
H(t-s)=H(t)-1. The final box coordinate makes s<t necessary in any
actual decomposition. Coordinatewise residue carry in
lambda(s)+lambda(t-s)-lambda(t) is nonnegative and integral; the
height identity forces all carries to vanish. Induction then gives
an exact sum of H(t) junior box points. Conversely a degree-one
decomposition of a nonvertex box point has a junior first summand;
a vertex summand is impossible since the box coordinates are <1.
Every cone lattice point is a box point plus nonnegative integral
vertex generators, so the test controls all degrees, not only a
finite list of dilations.

The quoted O(dN+N^2) bound counts arithmetic operations, with O(N+d)
stored integers. It is not a bound on bit complexity or printed
decomposition output. Failure supplies a finite box witness.

## What makes the constant-coordinate family stronger

Set m=d-1, choose 1<=q<N, and take a_i=N-q for every i<d.
Let B=N-mq-1. Theorem 1.4 says the following are equivalent:
IDP; a unimodular triangulation; a coherent unimodular triangulation;
and the arithmetic condition that B=0, or B>0 and every ceiling
quotient in the negative continued fraction N/B is congruent to
2 modulo m. For B<0, the box point with final coordinate one is
already a higher-degree obstruction. The dimension-two case m=1
has the usual coherent full lattice triangulation of a polygon.

For B>=0 the relevant lattice is

    Z^{m+2} + Z (B,q,...,q,1)/N.

Projection to first and last numerator coordinates lands in

    K_B = {(s,t) in Z^2 : s = Bt mod N},

whose covolume is N. Lemma 5.1's ceiling Euclidean algorithm gives
successive Hilbert-basis vectors U_i=(R_i,T_i) of its positive cone,
with det(U_i,U_{i+1})=N. Their height-one lifts are

    Z_i = (R_i,rho_i,...,rho_i,T_i)/N,
    rho_i = [q T_i]_N.

The recurrence for R_i and T_i makes the degree-one identities
R_i+m rho_i+T_i=N equivalent to the displayed congruence of the
ceiling quotients (Propositions 5.2–5.3). No coprimality reduction
changes the original lattice when gcd(N,B)>1.

The coherent construction in Lemmas 5.4–5.5 and Proposition 5.6
uses the plane of equal middle coordinates, the face
F=conv(E_1,...,E_m), and its centroid c. The centroid is generally
not a lattice point. The planar lattice configuration A_D is the
actual height-one lattice intersection; it is not blindly replaced
by all of K_B in the enclosing triangle. In the original simplex
coordinates that plane has affine lattice Z^2. Its polygon Q is
triangulated fully and coherently, while the successive triangles
(c,Z_i,Z_{i+1}) form the prescribed chain fan. A small generic
quadratic perturbation of the planar lifting gives compatible
heights. Giving every E_j height one extends those heights to a
single lifting of the entire simplex.

The maximal cells are conv(E_1,...,E_m,Z_i,Z_{i+1}) and the cells
obtained by adjoining all but one E_j to a planar triangle of Q.
The first have normalized volume one by det(U_i,U_{i+1})=N;
the second have volume one in the original affine lattice by the
coordinate differences x_l-x_j. Coverage is checked explicitly:
subtract the minimum of the middle barycentric coordinates and
normalize the remainder into the plane. The single supporting
lifting gives common faces and coherence. Thus coverage and
projectivity are established as well as determinants; mere
additivity of volume would not suffice without compatibility.

Proposition 5.7 expresses the same criterion recursively. With
L=mq+1, reject N<L; accept N>=L when N mod L=0; otherwise test
(N mod L, q mod (N mod L)), allowing q=0 as the terminal true case.
An unchanged positive q at the first reduction leads immediately
to rejection; positive nonterminal q otherwise decreases.
For example S_(5,5,7) has N/B=7/2=[4,2]^- and a coherent
unimodular triangulation. S_(6,6,8) has 8/3=[3,3]^- and fails
IDP: (3,3,3) lies in 2S, whereas the final coordinates of lattice
points in S are {0,1,4,8}, with no two summing to three.

## The published obstruction and the independent finite scope

Example 10 of Firla–Ziegler is

    C = cone(e_1,e_2,e_3,(14,31,34,39)) in R^4.

Its minimal Hilbert basis lies in y_1+y_2+y_3-2y_4=1, but
there is no Hilbert partition: no face-to-face triangulation into
unimodular cones generated by that Hilbert basis. The published
counts are 12 Hilbert-basis elements and 161 candidate unimodular
subcones. The source also states a binary Hilbert cover, which
is a different property and supplies no triangulation.

The HNF identification is the integral lattice isomorphism

    Phi(h,x_1,x_2,x_3) = (h-x_1-x_2+2x_3,x_2,x_1,x_3),
    Phi^{-1}(y) = (y_1+y_2+y_3-2y_4,y_3,y_2,y_4).

It maps the homogenized vertices of
S=conv(0,e_1,e_2,(34,31,39)) onto the displayed cone generators
and takes homogenized degree to the displayed height. Accordingly
S is IDP but has no unimodular triangulation, hence no coherent one.
These are the actual Examples 6.4–6.5 of the September preprint.

The [exact integer calculation](../hnf_firla_ziegler_exact_enumeration_20261004.json)
independently enumerates all 39 box points and decomposes all 38
nonzero ones into junior points. Their indices are
{1,2,5,8,10,11,16,25}. The vertices plus these points give 12
degree-one generators. Exhausting all four-element subsets of
these 12 points with the exact three-by-three determinant gives
161 candidates of volume one. All box-sum identities and the
height of every mapped generator were checked with arbitrary-
precision integers. This clears IDP and the 12/161 counts for this
particular simplex. No compatibility search, integer-program
infeasibility certificate or binary-cover computation was run;
nonexistence of a triangulation remains the precise published import.

## Direct local toric-model consequence

Take the cone sigma over this S in N=Z x Z^3, with generators
(1,0), (1,e_1), (1,e_2), (1,34,31,39), and dual lattice M.
Let h in M be projection to the first coordinate. The affine
normal toric variety

    X_sigma = Spec C[sigma^vee intersect M]

maps to A^1 by tau=chi^h. Its ring is a domain, hence is flat
over C[tau]. Inverting tau inverts enough positive-height
monomials to obtain C[M]; since h is primitive, its generic
fibre is the three-dimensional torus over C(tau), and is smooth.

Every primitive original ray has h-value one. The principal
monomial ideal (chi^h) is the intersection of the four ray-prime
ideals: an integral dual exponent lies in that intersection
exactly when its pairing with every ray is >=1, exactly when
subtracting h still belongs to sigma^vee intersect M. Thus the
central fibre is reduced. The original cone nevertheless has
index 39 and is singular.

A smooth toric subdivision over the same parameter would have
primitive generators forming a lattice basis on each maximal
cone. If its central fibre were also reduced, all its rays would
have h-value one. Intersecting with h=1 would consequently give
an ambient-unimodular triangulation of S, which the published
Example 10 excludes. This obstructs that particular *toric*
smooth reduced model without further base change. It does not
exclude arbitrary nontoric constructions, and it does not
contradict semistable reduction after dilation of the height
slice. Projectivity would additionally require coherence.

More generally, the constant-coordinate family supplies coherent
smooth reduced toric subdivisions exactly under its stated
arithmetic condition. The general IDP test supplies normality of
the degree-one-generated cone semigroup, not that stronger model
conclusion. The Sylvester example and this obstruction therefore
give complementary local tests for the book's subdivision discussion.

## Other source boundaries and next work

The general finite compatibility graph (Theorem 6.1) has one vertex
for each determinant-one (d+1)-subset of the explicit lattice
point configuration. A clique of size N covers by volume and
closedness once pairwise common-face compatibility is known.
Proposition 6.2 adds a common lifting with strict gaps normalized
to one. Both are finite exact procedures, not a structural
classification of all one-row simplices or a polynomial graph
search bound.

Theorem 6.6 gives a checked coherent two-pyramid construction
for a=(2M-1,2c_2,...,2c_{d-1},2M), reduced to
b=(c_2,...,c_{d-1},M). The primitive functional x_1-x_d puts
the two apices at heights +1 and -1 and their integral midpoint
in the common lattice slice. A small multiple of one base lifting,
with both apex heights one, gives both halves coherently. Corollary
6.7 consequently gives coherent unimodular triangulations for
conv(0,e_1,e_2,(N-1,N-2,N)) when N is even; for odd N the
displayed degree-two box point obstructs IDP. No new experiment
on these families was run.

Firla–Ziegler's general toric-resolution sentence on printed page
207 must retain its Hilbert-basis restriction: ordinary toric
resolution can add rays of larger degree. Likewise its normality
wording on printed page 213 is used with the specified degree-one
grading. The saturated ring of an arbitrary cone is already normal;
normality alone cannot force its Hilbert basis into height one.
These scope qualifications do not dispute Example 10. The note
added in proof on page 216 already announces a Hilbert-cover
counterexample, so historical introductory conjecture statements
are not transplanted as current open problems.

The next admission candidate is a short known-source model example
beside the Sylvester construction. Further global compatible
heights, strictification and polarization remain the separate
inputs in the existing trait dossier. The book's 42 statuses are
unchanged; no independent production-model verification is claimed.
