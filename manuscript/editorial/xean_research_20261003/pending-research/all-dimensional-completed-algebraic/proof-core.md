# Completed algebraic transport of ordinary zero-Hessian currents in every pure dimension

Unverified research draft, 4 October 2026. This is a partial result for the
original P06.2 recognition problem. An author audit, source extraction, or a
successful compilation is not mathematical verification. No previous theorem,
catalogue assertion, review verdict, or hash is a premise.

## 1. Statements and conventions

Let K be a complete nontrivially valued non-Archimedean field, let M/K be
an algebraic valued extension, and let L be its completion. All finite stages
E below are actual embedded fields K ⊆ E ⊆ M. They are complete with their
prescribed absolute values. Write p_E:X_E→X and q_E:X_L→X_E, and write
π:X_L→X. Scalar extensions use actual completed affinoid algebras.

**Theorem A (exact compact tests).** If X is good, separated, and strict,
then for every pair of nonnegative integers (a,b) and every ordinary CLD
form β∈A_c^{a,b}(X_L), there is one finite E⊆M and α_E∈A_c^{a,b}(X_E)
such that β=q_E^*α_E as smooth sections. Consequently both differentials,
their compositions, and exterior products with pulled-back sections respect
this identity. No dimension, boundarylessness, or positivity is required
for this assertion. It asserts descent of a compact smooth form, not of an
arbitrary analytic function or an arbitrary upstairs space presentation.

**Theorem B (the new gate).** Suppose in addition that X is boundaryless
and pure of analytic dimension n≥1. Retain its possibly singular and
nonreduced analytic structure. Then X_L has these same ambient properties
and is pure of dimension n. For every finite continuous h:X→R,

\[
 d'd''[h]=0\quad\Longleftrightarrow\quad d'd''[h\circ\pi]=0.       \tag{T}
\]

Both equations are tested against **all** compact ordinary smooth
(n−1,n−1) forms and use the canonical CLD calibration for their own
fields. All assertions remain true on every ordinary open subspace.
No separability, tameness, perfectness, unit-separation, Radon-Hessian,
psh, or invariant-form-descent assumption is imposed. Nilpotents and all
actual local fibre lengths are retained.

The theorem does not recognize h as classically pluriharmonic. It does
not prove two-sign regularization, transport along arbitrary curve maps,
or transport through a general transcendental analytic extension. In
particular L/K may fail to be algebraic, but here it is the completion
of the specified algebraic extension. The original P06.2 remains open;
P05.2 is unchanged. The full input is preserved in original-task.json,
original-problem.txt, completion-criteria.txt, and assignment-verbatim.txt.

All opens and supports use the ordinary Hausdorff topology. An affinoid
neighborhood contains an ordinary neighborhood. Its ordinary interior
inside X is denoted int_X(V); this differs from its absolute analytic
interior Int(V). Set D=d'd'' and t_f=−log|f| for an analytic unit. Up to
the fixed current-duality sign, which has no effect on vanishing, the
equation is

\[
 B_h(\alpha):=\int_X h\,(D\alpha)_{\mathrm{Rad},K}=0
 \quad(\alpha\in A_c^{n-1,n-1}(X)).                         \tag{1}
\]

Only smooth differentiated top forms are assigned Radon measures here.
The current D[h] is not assumed to be a measure.

## 2. Exact primary foundations and their applicability

CLD means Chambert-Loir–Ducros, *Formes différentielles réelles et
courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025.
The complete selected primary statements and their printed proof bodies
are embedded below. These are imported analytic foundations, not previous
campaign claims. The algebra, support, collar, and finite-stage arguments
of Sections 3–10 are supplied in this document.

**Affinoid foundations.** CLD 11.1.1–2: affinoid spectra are compact
Hausdorff; affinoid algebras are noetherian with closed ideals; their
analytic spectra surject onto their prime spectra. Completed residue
fields are completions of the fraction fields of the point-kernel
quotients. In particular an element with no analytic zero is an actual
unit, including in a nonreduced affinoid algebra. CLD 11.1.5: a rational
system |f_i|≤r_i|g| with positive real r_i and no common analytic zero
defines an affinoid domain, and every point has such a neighborhood
inside any prescribed ordinary open, with all inequalities strict at the
point. Its algebra is the quotient obtained by adjoining the bounded
ratios f_i/g. CLD 11.1.7–10: good spaces have affinoid neighborhood
bases; opens are domains; domains have the universal analytic
factorization property; scalar affinoids use completed tensors and
scalar projection is surjective. CLD 11.4.4 gives finite algebras their
finite-module affinoid topology. CLD 11.7.7 gives strict affinoid
neighborhoods in good strict spaces over a nontrivially valued field.
Applying this to ordinary opens gives a strict neighborhood inside any
such open. We use these facts on actual algebras, never spectral norms
on a reduction as substitute Banach norms.

**Dimensions and boundaries.** CLD 11.2.2–3: separatedness implies
Hausdorffness; strict affinoid dimension is Krull dimension; complete
scalar extension preserves total analytic dimension; domains preserve
local dimension. For the minimal components V_i of an affinoid V,
dim_y(V)=max_{y∈V_i}dim(V_i). Purity means constant local dimension.
These statements alone do not assert purity after completion. Sections
3 and 9 prove that separate assertion. CLD 11.4.1 gives the relative
interior composition equality when the middle morphism is locally
separated. Berkovich, *Étale cohomology for non-Archimedean analytic
spaces*, Publ. Math. IHES 78 (1993), Proposition 1.5.5(i),(iii),(iv),
gives the ordinary relative interior of a domain and the base-change
inclusion for relative interiors, including complete field extension.
Thus ordinary opens in a boundaryless space and scalar extensions of
a boundaryless space are boundaryless. Equality of arbitrary absolute
interiors under scalar extension is not used.

**Ordinary forms and nullity.** CLD 6.2.1–2 defines ordinary smooth
forms by tropical descriptions on ordinary open neighborhoods and gives
ordinary sheaves closed under wedge, J,d',d''. Proposition 15.1.1(b)
gives descriptions by finitely many analytic units on an ordinary open
cover, in every bidegree. CLD 3.3.3 and Lemma 1.9.4 give ambient
Euclidean coefficient representatives, using the latter only when the
paralinear subset is closed in the ambient open. CLD 3.3.10–12 gives
the exterior calculus and functorial smooth pullback. Proposition 3.4.4
states exactly: for a tropical chart f and coefficient form ω, f^*ω is
zero in the G-form sheaf iff ω restricts to zero on f(V) for every compact
domain V. We use this to identify scalar sections that are equal as
functions and to identify forms in common moment charts. Ordinary forms
are sections of that sheaf with ordinary local descriptions; no descent
of arbitrary invariant forms is imported.

**Compact cutoffs.** CLD 15.2.2 makes good Hausdorff spaces locally
holomorphically separated. Corollary 15.2.5 says that, for a compact C
inside an ordinary open U in such a space, a smooth function exists which
is one near C and has compact support contained in U. Section 3 supplies
the finite compact partition and an independent cutoff construction.
The overly broad fixed-index compact-support reading of 15.2.9 is not used.

**Polyhedra and measures.** Ducros, *Espaces de Berkovich, polytopes,
squelettes et théorie des modèles*, Confluentes Math. 4 (2012), 1250007,
Theorem 3.2(1), states: if a compact Γ-strict k-analytic space has
dimension d and f is a finite tuple of analytic units, |f|(X) is a
c-polytope of dimension at most d, with c=(Q,(|k^*|Γ)^Q). We apply this
to strict compact affinoids, Γ={1}; it permits nilpotents and singularities.
No universal dimension equality from CLD 12.2.4 is used. CLD 5.4.4 and
14.1.8 make compact charts pleasant; 14.1.12 gives compatible skeletal
and image cell refinements. CLD 14.2.2 and 14.3.2–5 give positive
constant canonical calibrations on n-cells: the weight is the actual
finite-flat moment degree times a primitive volume vector. CLD
14.5.1–2 sums these weights on image cells. CLD 5.8.1–5 constructs
top-form Radon measures from their skeletal densities, compatibly on
domains; 5.10.1(c),(d) gives the corresponding pleasant-chart integration
formula. Smooth top forms are locally integrable and compact ones finite.
Lower-dimensional image cells have no n-dimensional top measure.
Section 5 derives the variation bound from the positive sheet densities,
rather than from a signed pushforward equality.

**Two different scalar comparisons.** CLD Proposition 14.3.6 states
π_*μ_L=μ for canonical skeletal calibrations under a complete extension.
Proposition 15.3.1 states that a locally integrable top G-form ω satisfies

\[
 \pi_*((\pi^*\omega)_{\mathrm{Rad},L})
                 =\omega_{\mathrm{Rad},K}.                 \tag{2}
\]

The Borel variation measures have the analogous identity. There is no
field-degree factor. CLD Remark 14.4.3 instead states: on the **same
carrier**, an F-analytic space viewed as K-analytic, for finite F/K,
has the same dimension and skeletal subsets, and its calibration is

\[
                      \mu_K=[F:K]\mu_F.                    \tag{3}
\]

We use (3) only after constructing the actual local F-analytic structure
and identifying the forms. Equation (2) is used only on smooth top
forms, followed by a continuous multiplier, not as continuous-current
pullback. Its primary proof uses CLD 13.3.3, the degree-sum formula
for actual Artinian fibre algebras; Section 10 gives that algebra explicitly.

**Currents and Stokes.** CLD 7.3.5 defines [h] for a locally integrable
multiplier, including finite continuous functions. CLD Theorem 15.7.1
gives Hausdorff pure n-dimensional analytic spaces their level-n tropical
structure and analytic boundary; 15.7.2 gives domain compatibility.
Stokes, CLD 5.11.1(a), applies to compact C^1 (n−1,n) forms; J gives
the double-prime version. On our boundaryless spaces both boundary
integrals vanish. Section 5 uses these twice on arbitrary complementary
forms; the symmetry-restricted Green formula is not used.

## 3. Actual finite algebras, geometry, and compact partitions

### 3.1. Finite topology and elementary field facts

A finite-dimensional normed vector space over a complete valued field
has a norm equivalent to the coefficient maximum norm in every basis.
Induct on dimension: the preceding span is complete and closed, so the
last basis vector has positive distance from it. Dividing a vector by
its last coefficient bounds that coefficient by its norm; the triangle
inequality and induction bound the remaining coefficients. The reverse
bound is the triangle inequality. Consequently, for any affinoid Banach
algebra A and finite E/K of degree m, tensoring the bounded coordinate
maps E→K identifies the tensor topology with that of A^m. The latter
is complete. Hence

\[
            A\widehat\otimes_K E=A\otimes_K E               \tag{4}
\]

with its actual finite-module topology, including nilpotents.

A finite field extension is complete for its extending norm; existence
follows by giving the finite algebra its affinoid finite-module topology
and taking a point of its nonempty spectrum. Its kernel is zero. Any two
extending absolute values are equivalent finite-dimensional norms; apply
their comparison constants to powers z^j and take j-th roots to prove
equality. Thus all finite field embeddings here preserve the norm.

The elementary Galois facts needed below can be reconstructed as follows.
A finite separable extension has degree-many embeddings into an
algebraic closure, by successively choosing the distinct roots along a
finite generating tower. K is infinite, since a finite field has no
nontrivial absolute value. For generators a_1,…,a_s choose coefficients
(1,t,…,t^{s−1}) such that their linear combination has distinct values
under all embeddings: each pair forbids the roots of one nonzero
polynomial in t, and finitely many forbidden roots cannot exhaust K.
The combination is primitive by comparing the number of its conjugates
with the degree. In a finite normal separable extension E/K all
embeddings of intermediate fields extend to E by adjoining successive
roots and normality; the image is again E. Thus E^G=K. For H≤G and
F=E^H, choose a K-primitive element b for E. Then E=F[b], and its
H-orbit polynomial has coefficients in F. The F-minimal polynomial
divides this polynomial and has all its |H| distinct roots, so its
degree is |H|. Thus E/F is Galois with group H. Conjugating embeddings
of F conjugates H. A splitting field of a separable primitive polynomial
is the actual finite Galois normal closure used in Section 6.

For a finite Galois E/K, tensoring the finite kernel equations defining
E^G=K with the K-vector space A gives

\[
 (A\otimes_K E)^G=A,\qquad
 N(f):=\prod_{g\in G}gf\in A^\times\quad(f\in(A\otimes E)^\times). \tag{5}
\]

The inverse product descends as well. No averaging in K is used.
The automorphisms are bounded on the finite-module algebra. Its restricted
K-spectrum and E-spectrum agree because all bounded multiplicative
seminorms restrict to the unique norm on E. Their actual rational algebras
and unit germs agree; the action on points satisfies |gf(y)|=|f(g^{-1}y)|.

### 3.2. All minimal components at finite stages

In a strict affinoid domain M(A) in pure n-dimensional X, every minimal
prime P has $\dim(A/P)=n$. Spectral surjectivity supplies a point of kernel P;
it lies on that component alone, and the primary local dimension formula
gives this equality.

First let E/K be finite separable. For the nilradical J of A, J is
nilpotent, and the injection A/J→∏_P Frac(A/P) stays injective under
algebraic tensor over K. Each field tensor with E is a finite product of
fields (factor a separable primitive polynomial). Thus (A/J)⊗E is reduced,
and the nilradical of A⊗E is precisely J⊗E. The finitely many maps of
this reduced algebra into those field factors have prime kernels with
zero intersection. A minimal prime Q contains their product, hence one
kernel, and by minimality equals it. Its contraction is the associated P.
The finite integral injection A/P→(A⊗E)/Q gives equal Krull dimensions.

Here are the elementary integral dimension facts used in that last step.
For a finite integral injection of domains C→D, localization at a prime
of C is a nonzero finite module. Its reduction modulo the maximal ideal
is nonzero by the determinant argument for Nakayama: if generators equal
a maximal-ideal-valued matrix times themselves, det(I−matrix), a unit,
annihilates them. A maximal ideal of the finite quotient lies over the
given prime (a subring over which a field is integral is a field).
Applying lying over after a quotient gives going up. For incomparability,
quotient by the smaller upstairs prime and invert the nonzero elements
of the base domain. The resulting finite integral domain over a field
is a field, since a least-degree monic equation expresses the inverse
of any nonzero element. A nonzero element of the quotient domain cannot
disappear in that localization. Thus strictly nested primes cannot have
the same contraction. Chain contraction and chain lifting prove equal
dimensions. This argument needs no completeness of the fraction fields.

For finite purely inseparable E/K in characteristic p, choose q=p^r
with E^q⊆K. In the actual algebra B=A⊗E every b satisfies b^q∈A.
A→B is an injection, finite and integral. For each prime P of A there
is exactly one prime Q above it: membership b∈Q is equivalent to b^q∈P.
Lying over gives existence. This formula also preserves and reflects
prime inclusions, so minimal primes correspond and dimensions of their
quotients agree by the preceding integral argument. Every component of
B has dimension n, whether or not B is reduced. Combining the two cases
in the embedded mixed tower of Section 6 proves finite-stage purity for
every finite algebraic E/K.

### 3.3. Other ambient properties and compact scalar inverse images

For any complete extension, scalar affinoids are actual completed
tensors. Inverse images of downstairs affinoid neighborhoods contain
inverse images of their ordinary interiors, so goodness is preserved.
Strict presentations base change to strict presentations. Closed diagonal
base change proves separatedness; hence Hausdorffness. Relative-interior
base-change inclusion proves boundarylessness. Ordinary opens retain all
these properties. Finite-stage purity has just been proved; completed-stage
purity is established independently in Section 9.

Scalar projection has compact inverse images. Cover a downstairs compact
C by finitely many ordinary interiors of affinoid neighborhoods V_i.
Its inverse image is closed in the finite union of the compact (V_i)_L,
because the carrier is Hausdorff. This applies also to an infinite
completed extension. No finite-fibre assertion is used for that extension.

We also need a finite full-fibre shrinking argument. Inside an affinoid
neighborhood V_0 of x, if an ordinary open N⊆(V_0)_E contains the
whole fibre, its compact complement has closed image excluding x.
A smaller strict affinoid neighborhood V of x can be chosen in the
complement of that image and in int_X(V_0). Then V_E⊆N.

### 3.4. Valid cutoffs, finite partitions, and continuous approximation

The compact-cutoff input can also be proved directly. Given x∈U ordinary
open, choose an affinoid neighborhood V of x and let
C_0=V\(int_X(V)∩U). It is compact and excludes x. For each y∈C_0 an
analytic function on V separates x,y by its norm. A smooth real function
of its logarithm can be chosen one near the first value and zero near
the second. If either norm is zero, make the composing function constant
on a sufficiently negative half-line and extend by that constant across
the zero locus. This extension is locally constant there and ordinary
smooth; elsewhere the analytic function is locally a unit. A finite
product of these functions is one near x and zero on a relative
neighborhood of C_0. Its zero extension outside V is smooth: on int_X(V)
and outside V this is immediate, and at C_0 relative vanishing gives an
ordinary zero neighborhood. Its support is compact inside U. Finite sums
of squares and smooth composition give the same assertion for compact C⊆U.

For a finite open cover U_i of compact C, choose finitely many such
nonnegative bumps with positive loci covering C, grouped as ψ_i supported
compactly inside U_i. Put s=∑ψ_i, and choose compact χ=1 near C supported
inside {s>0}. The functions θ_i=χψ_i/s on {s>0}, zero elsewhere, are
ordinary smooth with compact support inside U_i and sum one near C.
Zero extension is smooth because each support is a compact closed subset
of its defining open. This construction requires no global paracompactness.
Applying it to small-oscillation neighborhoods of a continuous h gives a
compact ordinary smooth a with |a−h|<ε on any fixed compact C.

## 4. Reconstructed finite-Galois supporting theorem

This section proves the finite-Galois case of (T), independently of the
round-19 conclusion. The stabilizer, Newton, tensor, support, and collar
steps are included because a scalar-test-only finite theorem would not
support the completion argument.

### 4.1. Actual fibres and stabilizers

For x∈X put C=H(x). The actual fibre is M(C⊗_K E). Factoring a
separable primitive polynomial gives a finite product of fields D_y, each
with a single analytic point by finite norm uniqueness. G acts transitively
on those factors: a union of two distinct orbits would give a nontrivial
invariant idempotent, whereas (C⊗E)^G=C by the kernel calculation.
For the actual point stabilizer H, invariant tuples identify D_y^H=C.
The image of the primitive b has |H| distinct conjugates in D_y and
D_y=C[b]. The same orbit-polynomial argument gives [D_y:C]=|H| and
group H. In particular E^H embeds in C. If y is not G-fixed, H is proper.
This uses actual tensor factors, not a covering-space model.

### 4.2. A separable residue constant lifts by quotient-Banach Newton

Suppose a specified finite separable F/K embeds in H(x). Choose a
primitive a with monic minimal polynomial P(T)=∑p_jT^j. In a strict
affinoid neighborhood of x, fractions of the kernel quotient are dense
in H(x). Approximate a by g=f/b, retaining b invertible on a strict
rational neighborhood where |b|≥|k_0| is strictly satisfied at x.
Choose R∈|K^*| with R>max(1,|a|), d∈|K^*| with 0<d<|P'(a)|, and

\[
 M_0=\max\bigl(\{1\}\cup\{|p_j|R^{j-2}:2\le j\le\deg P\}\bigr).
\]

Choose c∈|K^*| so that s=c/d<min(1,R) and v=M_0c/d^2<1. Approximate
closely enough that |g(x)|<R, |P(g)(x)|<c, |P'(g)(x)|>d, and
|g(x)−a|<s. Retain the strict rational neighborhood
|g|≤R, |P(g)|≤c, |P'(g)|≥d. Its actual quotient Tate algebra has
||g||≤R, ||P(g)||≤c, ||P'(g)^{-1}||≤d^{-1}, by the adjoined quotient
variables. These are Banach bounds imposed by relations, valid with
nilpotents; spectral smallness is not being used.

Binomial expansion, with integer coefficients of norm at most one,
gives for ||z||≤R and ||w||≤min(1,R)

\[
 \|P(z+w)-P(z)-P'(z)w\|\le M_0\|w\|^2,
 \qquad\|P'(z+w)-P'(z)\|\le M_0\|w\|.
\]

Iterate z_{j+1}=z_j−P'(z_j)^{-1}P(z_j), z_0=g. The first increment
has norm ≤s; Neumann inversion retains the derivative inverse bound
because M_0s/d=v<1. The next increment is at most
(M_0/d)||z_{j+1}−z_j||^2≤v||z_{j+1}−z_j||. All z_j have norm ≤R,
so they converge in the actual algebra to z with P(z)=0 and ||z−g||≤s.
Two roots within s of g(x) have difference times P'(g(x))+w, |w|≤M_0s<d,
equal to zero. This nonzero factor proves uniqueness, hence z(x)=a.
The map F=K[T]/P→O(V), T↦z, is injective (a unital map from a field
to a nonzero algebra) and bounded by finite norm equivalence.

This gives an actual F-analytic neighborhood. For the finite F-action
on A=O(V), ||u||_A≤C|u|. The equivalent complete norm
||b||_F=sup_{u∈F^*}||ub||_A/|u| is F-homogeneous and submultiplicative:
||ab||_F≤||a||_F||b||_A≤||a||_F||b||_F. A strict K-Tate presentation
has uniformly bounded monomials also in this equivalent norm and thus
extends to a bounded surjection F{T}→A. The quotient norm is equivalent:
boundedness gives one bound, and uniform lifts through the original K-Tate
presentation give the other. The spectra coincide by finite norm uniqueness,
and actual rational algebras coincide by their universal presentations.
These rational bases identify analytic sheaves on the common ordinary
carrier. Common unit moments and compact-image nullity identify all
ordinary forms, operations, and supports over F and K.

Restrict to an ordinary U around x. It is good, strict, separated and
pure over F: its affinoid algebras and Krull component dimensions are
unchanged. The F-diagonal is the closed equalizer inside the K-fibre
product, so separatedness is retained. Boundarylessness over F follows
from interior composition for U→M(F)→M(K), with finite separated
second map. On this actual same carrier, (3) gives for every compact
complementary test

\[
                         B_{h,K}=[F:K]B_{h,F}.             \tag{6}
\]

The positive real integer is cancellable even if its image in K is zero.

### 4.3. Strong induction off the fixed locus

Induct simultaneously for every field and space on |G|. The identity
case is immediate. Let S be the G-fixed locus in X_E, closed by
Hausdorffness and the finite equalizer description. At y∉S, the proper
stabilizer H gives a specified F=E^H⊆H(x). Section 4.2 lifts it on U;
(6) shows zero F-current there. The actual tensor identities are

\[
 F\otimes_K E\simeq\prod_{\tau:F\hookrightarrow E}E,
 \quad A\otimes_K E\simeq
             \prod_{\tau}A\otimes_{F,\tau}E.                \tag{7}
\]

They follow from the distinct linear factors of a primitive polynomial
and the Chinese remainder theorem, and retain all nilpotents of A.
Finite-module topologies identify their analytic components, which are
open and closed. Each is scalar extension by E/τ(F), a Galois extension
with group conjugate to H, of smaller order. All induction hypotheses
were checked above. Thus the current vanishes near y. Compact partitions
show that it vanishes on every complementary test supported outside S.

### 4.4. Norm units match arbitrary tensor tests on the fixed subspace

Let β be any compact ordinary complementary test. At y∈S∩supp(β),
transitivity makes its entire fibre the singleton {y}. A local description
uses units f_1,…,f_k and a Euclidean smooth superform ω. Intersect the
G-translates of the description/unit open. Full-fibre shrinking produces
a strict affinoid V downstairs with V_E inside it. Include all gf_i in
the orbit moment t. G permutes its coordinates. Let W be the fixed
linear subspace, i its inclusion, and P_0=|G|^{-1}∑_g g the real
averaging projection onto W. At actual fixed points t∈W, and its
averaged orbit coordinates are

\[
       |G|^{-1}\sum_g t_{gf_i}
          =|G|^{-1}t_{N(f_i)}\circ p_E.                     \tag{8}
\]

All norms in (8) are actual downstairs units by (5); division is real.
Shrink V so that both t(V_E) and iP_0t(V_E) lie in the Euclidean coefficient
open. This is possible because both agree at the singleton fibre and
full-fibre shrinking preserves these open conditions. Extend ω globally
by a Euclidean bump unchanged near those compact images. Set
ω_0=P_0^*i^*ω. Then i^*(ω−ω_0)=0 and t^*ω_0=p_E^*α_0 for a
downstairs ordinary complementary form obtained using (8). This matches
on W; it does not descend β or an arbitrary invariant form.

Cover p_E(S∩supp β) by finitely many such ordinary downstairs opens,
and take compact θ_i supported there with sum one near that compact.
Decompose β into β_rem=(1−p_E^*∑θ_i)β and β_i=p_E^*θ_i β.
The remainder is supported outside S. Put β_{0,i}=p_E^*(θ_iα_{0,i}),
γ_i=β_i−β_{0,i}, with all products extended by zero. Their supports
lie in fixed compact inverse images of supp θ_i inside the charts.
Equation (2) gives B_{h_E}(β_{0,i})=B_h(θ_iα_{0,i})=0. Each γ_i
has coefficient restriction zero on W. Coordinates used by θ_i enlarge
this to W times their entire coordinate space. This property persists
under any further moment refinement.

## 5. Tensor collars, actual variation, and continuous multipliers

**Collar lemma.** Let Q be a fixed linear map with kernel W. Let σ
be a compact n-dimensional affine polytope and ξ a smooth (n−1,n−1)
superform defined near σ and its nearby W comparison points, with i^*ξ=0
on W. Let χ be smooth radial, one near zero and zero outside the unit
ball, and set ξ_δ=χ(Qz/δ)ξ. On the tangent of σ, the coefficient L^1
norm of Dξ_δ is bounded uniformly for small δ; the L^1 norm of ξ_δ
tends to zero. Extra coordinates annihilated by Q are allowed.

**Proof.** Let H be the tangent and r=rank(Q|H). If the affine span
misses W, its Q-image is a closed affine space at positive distance from
zero, so the collar is eventually empty. Otherwise choose w_0 in that
span∩W and write z=w_0+u+v, with u∈H∩W and v in a fixed r-dimensional
complement. The map Q on the complement is injective; |Qz|≤δ bounds
v in an O(δ) box, while compactness bounds u in a fixed box. Fubini
with the fixed Jacobian bounds collar volume by O(δ^r). The comparison
point w_0+u need not be in σ, which handles contact only on a boundary face.
If r=0 the cell either misses the collar or lies in W, on which ξ and
its restricted derivatives vanish. If r≥2, cutoff derivatives through
order two are O(δ^{-2}); bounded derivatives of ξ times O(δ^r) volume
give the asserted bound.

If r=1 use tangent coordinates (u_1,…,u_{n−1},t). The restricted cutoff
depends only on t. In its second-derivative term
χ''(t)d't∧d''t∧ξ, every exterior component with either transverse
generator is killed by repetition. The unique surviving basis component is

\[
 A(u,t)\,d'u_1\wedge\cdots\wedge d'u_{n-1}
              \wedge d''u_1\wedge\cdots\wedge d''u_{n-1}.
\]

Restriction-zero gives A(u,0)=0, so smoothness gives |A(u,t)|≤C|t|
on the fixed compact comparison region. The second-cutoff term is therefore
O(δ^{-1}); first-cutoff terms also are O(δ^{-1}). O(δ) collar volume
gives uniform integrability. This includes n=1. Finally ξ is bounded,
so its undifferentiated L^1 norm tends to zero on positive-rank collars;
rank-zero restrictions vanish. Finite cells and fixed positive weights
preserve both conclusions. This proves the lemma.

The lemma controls the variation of differentiated **smooth** top forms
on actual carriers. On a strict compact affinoid with fixed moment t,
the cited polyhedral and skeletal refinements give finitely many n-sheets
above each image n-cell. Each has constant positive weight, its actual
finite-flat fibre degree times a primitive volume. Thus for any represented
top coefficient form ζ,

\[
 \|(t^*\zeta)_{\mathrm{Rad}}\|_{\mathrm{TV}}
 \le\sum_{\sigma}c_\sigma
        \int_\sigma\|\zeta|_{T\sigma}\|\,d\mathrm{vol}_\sigma,  \tag{9}
\]

with fixed finite constants. Indeed evaluate the scalar density separately
on every sheet, take its absolute value there, and sum the positive
weights. This is the density construction in 5.8.4–5 and 14.3.2;
it cannot be replaced by cancellation in a signed pushforward. All
nilpotent lengths enter the positive weights. Lower-dimensional moment
images give zero top form. Covering a fixed compact support by finitely
many strict compact charts and overcounting their positive variations gives
a valid bound; no partition derivatives are needed for this estimate.

Fix one γ=γ_i from Section 4.4, with Q=1−P_0. Define e_δ=χ(Qt/δ)γ,
extended by zero in its chart. Its support lies in one fixed compact C.
The test (1−χ(Qt/δ))γ is supported outside S: Qt=0 on S and χ is one
near zero. The induction therefore gives the exact identity

\[
                  B_{h_E}(\gamma)=B_{h_E}(e_\delta).        \tag{10}
\]

On a finite strict compact cover of C, add the moment coordinates
describing the fixed θ_i. The coefficient of γ still restricts to zero
on W times the added space. On each chart extend the smooth coefficient
of θ_i to the full ambient Euclidean space by a bump unchanged near its
compact image; multiplying the globally defined ω−ω_0 by this extension
preserves restriction-zero on the whole enlarged W. This ensures that
the off-cell comparison points in the collar proof lie in a valid smooth
coefficient domain. The collar lemma and (9) give

\[
     \sup_{0<\delta<\delta_0}
       \|(De_\delta)_{\mathrm{Rad},E}\|_{\mathrm{TV}}=C_1<\infty. \tag{11}
\]

For any fixed ordinary smooth compact scalar a, two Stokes applications
on the pure boundaryless space give

\[
                   \int a\,De_\delta
                       =\int e_\delta\wedge Da.             \tag{12}
\]

Explicitly, Stokes on a d''e gives ∫aDe=−∫d'a∧d''e. Stokes on
d'a∧e gives ∫d'a∧d''e=−∫Da∧e; e has even total degree, so Da∧e=e∧Da.
No symmetry of the complementary form is required. To estimate the
right side, add **a's moment coordinates** on a finite compact cover.
The enlarged fixed space is W times the entire extra space. Restriction-zero
persists; extend the local scalar coefficients by Euclidean bumps near
each compact joint image as above. The undifferentiated collar lemma on the joint moment gives
L^1 convergence of e_δ, and Da has bounded coefficients on these compact
images. Formula (9) for e_δ∧Da proves ∫a(De_δ)_Rad→0. If the original
moment has dimension <n, De_δ is zero; that observation alone is not
substituted for this joint-moment estimate. The weak estimate may depend
on the fixed a, whereas (11) was established independently of a.

Choose a with |a−h_E|<ε on C using Section 3.4. Equation (11) yields
\[
 \limsup_{\delta\to0}\left|\int h_E(De_\delta)_{\mathrm{Rad}}\right|
                                      \le C_1\varepsilon.
\]
Let ε→0, and use (10).
Thus B_{h_E}(γ)=0. The norm-matched tests, γ_i, and off-S remainder
exhaust the original arbitrary β, proving finite-Galois ascent.
Reverse transport follows at once from (2) applied to Dα for each
downstairs compact α, whose pullback is compact by Section 3.3.
This finishes the reconstructed finite-Galois supporting theorem.

## 6. Actual mixed finite stages and purely inseparable higher forms

### 6.1. Finite separable transport uses an actual normal closure

For finite separable E/K, choose its actual finite Galois normal closure
N/K in an algebraic closure containing E, with the unique extending norm.
Finite purity and all ambient properties hold. Finite-Galois ascent makes
h_N zero-current. For each compact complementary test α_E on X_E,
its compact pullback to X_N has pairing equal to B_{h_E}(α_E) by (2).
Thus h_E has zero current. This is descent through N/E by the canonical
top measure, not a normalization by [N:E] or an abstract degree argument.
The construction of N does not require N⊆M. Reverse finite transport
uses (2) directly.

### 6.2. Finite purely inseparable all-bidegree descent

For finite purely inseparable E/K of exponent q=p^r and actual affinoid
A, (4) and Frobenius give, in B=A⊗E,

\[
       (\sum_j a_j\otimes e_j)^q=\sum_j a_j^q e_j^q\in A.    \tag{13}
\]

If f is a unit, both f^q and (f^{-1})^q lie in A and multiply to one;
so f^q is an actual unit without reducing any algebra. Any two analytic
points above x have on every b the forced value |b^q(x)|^{1/q}. Scalar
surjectivity gives one, hence exactly one. Compact-to-Hausdorff projection
is therefore a homeomorphism on each affinoid; these homeomorphisms glue
on the ordinary affinoid interiors. Purity was proved by prime chains in
Section 3.2, without a reducedness assumption.

Let β be any ordinary (a,b) form near an upstairs point. The homeomorphism
and goodness give a downstairs affinoid neighborhood V whose whole V_E
lies in its ordinary moment-description open. Its units f_j are elements
of O(V)⊗E. Put g_j=f_j^q∈O(V)^*. Then t_f=q^{-1}t_g∘p_E. If ω
is the Euclidean coefficient superform, the downstairs form is
t_g^*(s_q^*ω), where s_q(t)=t/q. Its coefficient domain contains t_g(V)
by scalar surjectivity. Explicitly, a basis term of bidegree (a,b)
is multiplied by q^{-(a+b)}, as well as evaluating its coefficient at
t/q. Thus both prime and double-prime differential factors descend.
Equality as smooth sections follows either from this moment identity
or from compact-image nullity. The equality is on int_X(V) and its
entire inverse image, including any zero region of β.

For a compact β, cover its compact image by finitely many such opens,
take the compact partition of Section 3.4 downstairs, multiply each local
descendant by its cutoff and extend by zero. The result α is compact,
and its pullback is β globally: the cutoff sum is one near supp β and
β is zero elsewhere. No overlap agreement is needed for this finite-sum
construction. For completeness pullback is locally faithful: in any
downstairs unit chart and compact V, surjectivity gives identical compact
moment images for V and V_E, so 3.4.4 says zero pullback implies zero
section on V. Hence local descendants also agree if sheaf gluing is used.
Under the homeomorphism their supports correspond. This proves exact
purely inseparable descent for every bidegree, with compact supports.
Applying (2) to Dα proves the finite purely inseparable current equivalence
against all complementary tests. No curve comparison is involved.

### 6.3. The actual embedded mixed tower

For finite algebraic E/K in characteristic p, choose generators a_i.
Write each irreducible minimal polynomial f_i(T)=g_i(T^{p^{r_i}}),
removing powers of p until g_i'≠0. Substitution proves g_i irreducible;
coprimality with its derivative proves separability. Thus b_i=a_i^{p^{r_i}}
are separable over K. Their compositum S=K(b_i)⊆E is finite separable:
at each adjoining step its minimal polynomial divides a separable
polynomial, and successively extending embeddings gives degree-many
embeddings of the tower. Every intermediate simple field is separable
by comparing its number of embeddings with the tower degree. For
r=max r_i, taking p^r powers of a rational expression gives E^{p^r}⊆S.
Thus the **embedded** tower K⊆S⊆E is separable then purely inseparable.
In characteristic zero the derivative test makes every finite stage
separable. Finite tensor associativity with the bounded basis maps in
(4) identifies the actual spaces (X_S)_E=X_E. Their componentwise
purity was proved in Section 3.2. Applying Sections 6.1 and 6.2 proves
zero-current transport to every finite embedded E⊆M. This uses no
previous inseparable or curve theorem as a premise.

## 7. Completion, exact rational domains, and ordinary presentation opens

### 7.1. Density and finite associativity in the actual Banach algebra

M is the directed union of its finite embedded subextensions. For
A_L=A completed-tensor_K L, the **image** of A⊗M is dense. First
approximate by finitely many algebraic tensors ∑a_j⊗λ_j, λ_j∈L;
then replace each λ_j by m_j∈M. The Banach tensor error is at most
max_j||a_j|| |λ_j−m_j|. This concerns actual Banach norms and images;
no injection of an infinite uncompleted tensor is presumed.

For finite E/K the maps
(a⊗e)⊗λ↦a⊗eλ and a⊗λ↦(a⊗1)⊗λ extend to inverse bounded maps

\[
        (A\widehat\otimes_K E)\widehat\otimes_E L
                          \simeq A\widehat\otimes_K L.      \tag{14}
\]

The first is bounded using the finitely many bounded coordinate maps
of E and the tensor bound; the second is bounded by the inclusion
A→A_E and the tensor bound. They are inverse on dense elementary
tensors, hence inverse on the completions. This applies also to any
actual rational localization affinoid, with arbitrary real radii.
Density supplies approximants, while the next argument, not density
alone, supplies exact domains and presentation opens.

Scalar surjectivity here can also be reconstructed. Given x with H=H(x),
embed the algebraic M into an algebraic closure of H over K, by a maximal
partial embedding and adjoining a root if it is not yet defined on M.
The finite extensions of H have their compatible unique absolute values
by Section 3.1. Complete that algebraic closure to a field F. The
restriction on each finite K-subfield of M is its specified norm, so
the embedding extends isometrically to L→F. Evaluation of any tensor
representation obeys |∑a_j(x)λ_j|≤max_j||a_j|| |λ_j|. Taking the infimum
over representations bounds it by the full tensor seminorm; it extends
to a multiplicative seminorm of A_L over x, including the separated
quotient in its completion. The same proof over E works on every
scalar-extended affinoid domain. This avoids an assumed isometry or
injectivity of A⊗M. Compact inverse images were proved in Section 3.3.

### 7.2. Rational inequalities, equality loci, and strict loci

Let A be affinoid over a finite E_0⊆M, B=A_L, and let R_L⊆M(B)
be the rational domain |f_i|≤r_i|g|, r_i>0, with no common analytic
zero. Put

\[
 \delta=\min_{y\in\mathcal M(B)}
    \max(|g(y)|,r_1^{-1}|f_1(y)|,\ldots,r_s^{-1}|f_s(y)|)>0. \tag{15}
\]

Compactness and no common zero give positivity. Choose approximants
g_0,f_{i,0} from one finite A_E whose errors in B satisfy
||g_0−g||<δ and ||f_{i,0}−f_i||<r_iδ. Density and (14) give this
simultaneously. If |g(y)|≥δ, its norm is unchanged. A numerator at or
above r_i|g(y)| also has unchanged norm; a numerator below that threshold
remains strictly below, by ultrametricity. Thus every weak, equal, and
strict comparison is preserved at all points where |g|≥δ. If |g|<δ,
some numerator has weighted norm at least δ. Its norm is unchanged,
while |g_0|<δ, so that inequality remains strictly false. In particular
both the entire weak system and the entire strict system are preserved
on all M(B). **Every equality locus inside the validity domain** is
preserved; no claim is made about irrelevant individual comparisons at
points where the whole system is false. Zeros and nilpotent elements
cause no exception, since approximation used the actual Banach norm.

The approximant weighted maximum is positive upstairs. Scalar surjectivity
implies no common analytic zero downstairs at E; spectral surjectivity
then implies they generate the unit ideal. They define a genuine rational
domain R_E. Its base change has precisely the subset R_L. The universal
analytic-domain property identifies their analytic structures, because
each domain inclusion factors uniquely through the other. Thus
R_L=(R_E)_L as actual affinoid domains, including nilpotents. The same
argument gives exact inverse image equality for the strict loci

\[
 O_E=\{|f_{i,0}|<r_i|g_0|\ \forall i\},\qquad O_L=q_E^{-1}O_E. \tag{16}
\]

O_E is an ordinary open in the ambient affinoid and lies inside R_E.
It is an ordinary interior presentation neighborhood. We do not assert
equality of all ordinary interiors or all absolute analytic interiors
under base change. Only these exact saturated strict loci are needed.
A vacuous system is handled by the harmless strict comparison |1|<2|1|.

For each y and each prescribed ordinary description open upstairs, the
primary rational-neighborhood statement supplies an R_L inside it with
y in its strict locus. Equations (15)–(16) produce a finite-stage
saturated presentation neighborhood of y. This establishes the needed
topological refinement directly; no inverse-limit theorem is imported.

## 8. Exact descent and compact gluing of all higher-form tests

Let β be an ordinary (a,b) form near y∈X_L, and x its image in X.
Choose a downstairs strict affinoid neighborhood V_0 and an ordinary
U_0⊆int_X(V_0) containing x. Intersect its upstairs inverse image with
a moment-description open for β. Shrink so that on this intersection

\[
 \beta=\sum_{|I|=a,|J|=b}
       \omega_{IJ}(t_f)\,d't_{f,I}\wedge d''t_{f,J},          \tag{17}
\]

where all f_j are actual analytic units and all coefficients are smooth
on a Euclidean open containing the moment image of the retained compact
neighborhood. Ambient coefficients exist by the stated closed-subset
extension theorem. Select a rational R_L of y contained in this open
with y in its strict locus. Section 7 gives R_L=(R_{E_0})_L and its
descended strict locus. Since R_L⊆U_{0,L}, scalar surjectivity on the
domain implies R_{E_0}⊆U_{0,E_0}. Its strict locus is therefore an
ordinary open of the **whole** X_{E_0}, inside its affinoid interior,
rather than only a relatively open subset at an exposed boundary.

On R_L put δ_j=min|f_j|>0. In its actual affinoid Banach algebra,
approximate all f_j by u_j from one finite R_E, E⊇E_0, with
||u_j−f_j||<δ_j. Equations (14) and density apply to this rational
localization, not just to the original A. Ultrametricity gives exactly

\[
                      |u_j|=|f_j|\quad\text{on }R_L.        \tag{18}
\]

Scalar surjectivity implies no zero of u_j on R_E, so u_j is an actual
unit by the prime-spectrum criterion. This proof ensures its actual
inverse, without requiring spectral smallness of nilpotents. Surjectivity
also gives equality of compact moment images t_u(R_E)=t_f(R_L), so the
same coefficient open and ω_{IJ} are valid at the finite stage.

Equation (18) is sufficient for higher forms for a precise reason.
On the upstairs ordinary presentation open, the unit f_j/u_j has
logarithmic scalar section identically zero. A numerical-zero smooth
scalar section is zero in the smooth sheaf: in each compact moment
description its coefficient vanishes on the moment image, and 3.4.4
gives nullity, followed by ordinary local sheaf gluing. Therefore
t_{f_j}=q_E^*t_{u_j} **as smooth sections**, and applying each derivation
gives d't_{f_j}=q_E^*d't_{u_j} and d''t_{f_j}=q_E^*d''t_{u_j}.
This also follows in the joint (f,u) moment whose image lies on the
diagonal. Substitution in (17), including every exterior factor, proves
exact equality β=q_E^*b_E on O_L=q_E^{-1}O_E, with b_E the ordinary
(a,b) stage form obtained by replacing every f_j by u_j. This is not
C^0 convergence of differentiated forms. The equality holds on the
entire saturated open, including the regions where β is zero.

Now take arbitrary compact β on X_L and F=supp β. If F is empty take
zero at K. Otherwise finitely many opens of this kind cover F. Enlarge
their finite fields to one E⊆M, and use (14) to base change all domains,
strict loci, and local forms. Thus O_{i,L}=q_E^{-1}O_{i,E} and
β=q_E^*b_{i,E} on each entire such open. The compact F_E=q_E(F)
is covered by O_{i,E}. Choose finite compact θ_i supported in O_{i,E}
with sum one near F_E by Section 3.4. Define

\[
             \alpha_E=\sum_i\widetilde{\theta_i b_{i,E}},    \tag{19}
\]

where tilde is extension by zero. Each product has support contained in
the compact closed set supp θ_i⊆O_{i,E}. At every exterior point it
has an ordinary zero neighborhood, so this is a smooth compact form,
with no boundary derivative. Pullback of its summand is q_E^*θ_i β
on O_{i,L}; off that open both sides are zero. Consequently, globally,

\[
           q_E^*\alpha_E=(\sum_i q_E^*\theta_i)\beta=\beta.  \tag{20}
\]

The sum is one near F and β is zero outside F. The support of α_E
is contained in a finite union of compact cutoff supports; their full
scalar inverse image is compact by Section 3.3. We have neither assumed
the original support saturated nor silently glued higher forms from a
scalar lemma. Local descriptions agree with β on their full preimage
opens, and (19) is one concrete smooth global form. Agreement of b_i
on stage overlaps is unnecessary for this construction. Differentiation
of the exact section identity (20) proves Theorem A in every bidegree.

One can separately check local faithfulness if desired. In a downstairs
unit chart and compact affinoid V, scalar surjectivity gives identical
moment images for V and V_L. Applying compact-image nullity upstairs
and downstairs shows that zero pullback implies zero section on V.
Ordinary neighborhoods then give faithfulness on all ordinary opens.
This is a proved consequence of compact-image equality, not blanket
invariant-form descent, and is not needed for the finite-sum gluing.

## 9. Independent componentwise purity at completion

We do not use simultaneous Noether normalization, flat completed
tensoring of an injection, or a claim inferred from total dimension alone.
Instead, exact rational-domain descent makes the following contradiction
available in every dimension.

Fix y∈X_L and a strict affinoid neighborhood V_0 of its downstairs
image x, with y∈(int_X(V_0))_L. Its scalar extension has total dimension
n by the primary dimension theorem, so dim_y(X_L)≤n. Suppose its local
dimension is m<n. In (V_0)_L, remove the finitely many minimal components
of dimension greater than m. None contains y by the primary local
dimension formula. The remaining ordinary open contains y. Choose a
rational neighborhood R_L of y inside it and inside
(int_X(V_0))_L, with strict inequalities at y. Every local dimension
of this domain is at most m, again by the component/domain formula;
hence dim(R_L)≤m.

Section 7 descends R_L exactly to a nonempty R_E in (V_0)_E at one
finite E⊆M. Scalar surjectivity on R_E places it in
(int_X(V_0))_E, hence in the actual X_E. That space is pure n by
Sections 3 and 6, so the domain formula gives dim(R_E)=n, even if
the auxiliary rational radii make this domain non-strict. Complete
scalar dimension invariance now gives

\[
                    \dim R_L=\dim(R_E)_L=\dim R_E=n,
\]

contradicting dim R_L≤m<n. Therefore dim_y(X_L)=n at every point.
This argument controls local dimensions, not just the total dimension.
For every minimal prime Q of any strict upstairs affinoid domain,
spectral surjectivity gives a point with kernel Q on that component
alone. The local component formula then yields dim(A_L/Q)=n.
Thus **every** actual upstairs minimal component has dimension n.

Nilpotents were never removed from the rational algebras or their
completed tensors. The only reductions earlier were finite separable
prime calculations for dimension. The completed-stage purity proof
does not assert completed scalar extension preserves arbitrary module
injections. Goodness, strictness, separatedness, boundarylessness, and
compact scalar inverse images were checked in Section 3.3 using their
actual presentations and primary boundary theorem. We may therefore
use the canonical level-n tropical structure on all finite and completed
stages, and its domain/top-measure compatibility.

## 10. Pairing, lengths, and conclusion of the gate

Assume B_h=0. Sections 4–6 prove B_{h_E}=0 on every finite embedded
E⊆M, against all ordinary complementary forms. Given **any** compact
ordinary complementary β on X_L, Theorem A supplies β=q_E^*α_E at
one such E. Its derivative is q_E^*Dα_E, a smooth top form. Both
fields' actual spaces are pure n, and all supports are compact. Applying
(2), then the integration formula for signed Radon pushforward, gives

\[
 \begin{aligned}
 B_{h_L}(\beta)
 &=\int_{X_L}(h_E\circ q_E)(q_E^*D\alpha_E)_{\mathrm{Rad},L}\\
 &=\int_{X_E}h_E(D\alpha_E)_{\mathrm{Rad},E}
 =B_{h_E}(\alpha_E)=0.
 \end{aligned}                                             \tag{21}
\]

The continuous multiplier is bounded on the common compact. No
continuous-current pullback has been defined. This proves ascent.
For the converse, pull back any compact downstairs complementary α;
its support remains compact, and (2) gives B_{h_L}(π^*α)=B_h(α).
Vanishing upstairs implies vanishing downstairs, proving (T).

The canonical measure formula preserves all actual Artinian lengths.
If R is any finite Artinian C-algebra of vector-space dimension d and
C'/C any complete extension, its algebraic tensor is finite-dimensional,
already complete, of C'-dimension d. Decomposing it into local factors
R_j and taking a composition series in each gives

\[
 d=\sum_j\dim_{C'}R_j
   =\sum_j\operatorname{length}_{R_j}(R_j)[\kappa_j:C'].      \tag{22}
\]

There is no separability or reducedness assumption. A finite-flat
moment fibre is this actual algebra. CLD 13.3.3 and the full primary
14.3.6 proof choose the canonical lift of the target torus Gauss point
and sum precisely these local degrees on the skeletal n-cells. Equation
(22) preserves that sum; the positive calibrations then give (2).
Pointwise generic multiplicities may change, and are not divided out.
In contrast same-carrier field restriction composes the moment with a
finite-flat torus projection of rank [F:K], giving (3), used only in (6).
These two comparisons remain different in wild and inseparable cases.

The complete claim proved in this draft is the new completed-algebraic
**current transport gate**, with exact higher-test descent and independent
purity. The finite-Galois theorem is supporting mathematics, not reported
as a new theorem by repetition. Relative to the supplied catalogue, the
gate applies to every actual pure singular strict germ, without its
coordinate-product, invariant, real-PL, factorization, or imposed
upstairs-current hypotheses. Nevertheless it gives no recognition or
two-sign approximation in these germs. Catalogue descriptions are not
being used to infer those conclusions. Arbitrary transcendental-extension
transport, arbitrary analytic curve pullback, and ordinary two-sign
regularization remain separate unproved obligations. The original
non-strict arbitrary-radius negative example is not altered and is not
an original-scope counterexample. The status for original P06.2 is
partial, and candidate=false.

## 11. Audit and reproduction boundaries

The primary appendix is part of this authoritative argument and is
generated from the cached primary texts, including every selected
printed proof ending. Source-internal references remain references;
this document imports the stated analytic foundations, not every theorem
of the underlying texts. Obvious extraction defects, such as the
missing zero-dimensional condition in one line of the extracted CLD
13.3.3 proof, do not substitute for (22). The complete body is preserved.
No output truncation marker is used as a proof ending.

The full input and all program, command, source, audit, and build evidence
are retained in this fresh workspace. Run `bash reproduce.sh` to re-extract
the primary units, run finite diagnostics, compile the standalone TeX twice,
and check artifact integrity. These checks establish source identity,
finite toy calculations, and build observations, not the correctness of
the infinite-dimensional analytic theorem or any priority claim.
No additional model, subagent, network, installation, external message,
old-artifact write, database change, credential change, or heavy computation
is used. No supervised heavy-compute service was supplied or needed.

<!-- PRIMARY_APPENDIX_INSERTION_POINT -->
