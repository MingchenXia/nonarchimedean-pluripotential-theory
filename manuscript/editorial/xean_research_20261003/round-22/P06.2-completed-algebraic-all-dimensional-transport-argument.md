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

## Embedded primary-source bodies

The following are exact cached primary units, not campaign descriptions. Each selected statement has its full source ending and all of the proof printed for that unit. They import the stated analytic foundations; they do not independently reprove the entire CLD theory or every source-internal reference. Mathematical typography in text extraction can be defective. The restricted, explicit uses in the argument control applicability. In particular, the false universal dimension equality in CLD 12.2.4 and the broad compact-support formulation in 15.2.9 are excluded. Ducros 3.2 supplies the correct upper bound. The source manifest records whole-file origins and hashes; hashes are integrity data only. In the PDF rendering alone, unsupported monospaced norm bars and slanted inequalities are written as ||, <=, and >=, and the ffi ligature is expanded. Invisible OCR control bytes are displayed explicitly. The authoritative Markdown and individual primary text artifacts retain their original bytes.

### primary-01: CLD 1.3.6: J and the differential signs

Cached primary CLD-v2.txt, lines 1212 to 1247. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
Lemme 1.3.6. — On a les relations
(1.3.6.1)                       J d′ = d′′ J et J d′′ = − d′ J.
Par suite, sur AVp,q , on a les relations
(1.3.6.2)                 d′′ = J d′ J−1 = −J−1 d′ J = (−1)p+q J d′ J
et
(1.3.6.3)                d′ = J−1 d′′ J = −J d′′ J−1 = (−1)p+q J d′′ J.
On a aussi
(1.3.6.4)                                d′ d′′ J = J d′ d′′ .
Démonstration. — Par linéarité, il suffit de traiter le cas d’une forme du type ω =
α d′ xI ∧ d′′ xJ , où I et J sont des multi-indices de longueur p et q. D’après la for-
mule (1.3.3.2), on a
                J d′ Jω = J d′ J (α d′ xI ∧ d′′ xJ )
                        = (−1)(p+1)q J d′ (α d′ xJ ∧ d′′ xI )
                                        n
                                       X    ∂α ′
                        = (−1)(p+1)q
                                     J           d xj ∧ d′ xJ ∧ d′′ xI
                                       j=1
                                            ∂x j
                                                       n
                                                       X ∂α
                        = (−1)(p+1)q (−1)(q+2)p                  d′ xI ∧ d′′ xj ∧ d′′ xJ
                                                       j=1
                                                           ∂xj
                                  n
                                  X ∂α
                        = (−1)q               d′ xI ∧ d′′ xi ∧ d′′ xJ
                                  j=1
                                        ∂xj
                        = (−1)p+q d′′ ω,
d’après la formule (1.3.5.2).
  Puisque d′′ ω est de type (p, q + 1), cela démontre l’égalité J d′ J = −J2 d′′ , autrement
dit d′ J = −J d′′ . Les autres relations s’en déduisent, compte tenu du fait que J2 vaut
(−1)p+q sur AVp,q .

                § 1.3. SUPERFORMES DIFFÉRENTIELLES, D’APRÈS A. LAGERBERG                                31
```

### primary-02: CLD 1.9.4: closed-subset extension, whole proof

Cached primary CLD-v2.txt, lines 2410 to 2472. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
Lemme 1.9.4. — Soit V un espace affine de dimension finie, soit P un sous-espace
paralinéaire de V .
  Pour tout ouvert U de V , l’application canonique

                        GVp,q (U )/ (GVp,q (U ) ∩ NPp,q (U )) → GPp,q (U ∩ P )

est injective.
  Si de plus U ∩ P est fermé dans U , cette application est bijective.

Démonstration. — Démontrons que l’application donnée est injective. Soit ω ∈ GVp,q (U )
d’image nulle dans GPp,q (U ∩ P ) et démontrons que ω ∈ NPp,q (U ). Il existe donc une
famille (Ui ) d’ouverts de U telle que (Ui ∩ P ) soit un recouvrement de U ∩ P et telle
que ω|Ui ∈ NPp,q (Ui ) pour tout i. On a alors ω|P ∩Ui = 0 pour tout i, d’où ω|P = 0
(lemme 1.9.2).
   Supposons maintenant que U ∩P est fermé dans U et démontrons que cette application
est surjective. Commençons par observer que GPp,q ∩NPp,q est un AV -module, donc est fin.
Par suite, sa cohomologie est triviale sur tout ouvert, si bien que l’application canonique

                               GVp,q (U ) → (GVp,q /GVp,q ∩ NPp,q )(U )

est surjective pour tout ouvert U de V .
   Soit ω ∈ GPp,q (U ∩P ). Par définition et par ce qui précède, ω est donnée par une famille
(Ui ) d’ouverts de U recouvrant U ∩ P et, pour tout i, un élément ωi de GVp,q (Ui ) sujets
à la condition de compatibilité suivante : pour tout couple (i, j), il existe une famille
                                                                            k − ωj |U k ∈ N
   k                                                                                          p,q   k
(Ui,j )k d’ouverts de Ui ∩ Uj recouvrant Ui ∩ Uj ∩ P telle que ωi |Ui,j               i,j    P (Ui,j )
                                       ; on a ωi |Vi,j − ωj |Vi,j ∈ NPp,q (Vi,j ). Puisque Vi,j est un
                                 S k
pour tout k. Posons Vi,j = k Ui,j
voisinage de Ui ∩ Uj ∩ P dans Ui ∩ Uj , on a donc ωi |Ui ∩Uj − ωj |Ui ∩Uj ∈ NPp,q (Ui ∩ Uj ).
Comme P est fermé dans U , U0 = U P est un ouvert de U ; Adjoignons-le à la
famille (Ui ) et considérons une partition de l’unité (φi ) sur U formée de fonctions lisses
et subordonnée au recouvrement (Ui ) de U ainsi obtenu. Le P            support de φ0 est disjoint
de P , donc φ0 est nulle au voisinage de P . La fonction φ = i̸=0 φi = 1 − φ0 est donc
égale à 1 au voisinage de P . Pour tout i ̸= 0, le support de la section φi ωi est contenu
dans Ui et est contenu dans le support de φi qui est fermé dans U , de sorte qu’il est
lui-même fermé dans U ; notons        (φi ωi )U le prolongement (par zéro) à tout l’espace de
cette section. Posons ω = i̸=0 (φi ωi )U . Pour prouver que ω ′ |P = ω, il suffit de vérifier
                            ′
                                 P

que pour tout i ̸= 0, ω ′ |Ui coïncide avec ωi modulo NPp,q . Fixons un indice i ̸= 0. La
famille (φj |Ui )j est une partition de l’unité sur Ui subordonnée au recouvrement (Ui ∩Uj )j ,
et l’on a
                                   X
                         ω ′ |Ui =   (φj ωj )U |Ui
                                 j̸=0
                                X
                              =  (φj ωj |Ui ∩Uj )Ui
                                 j̸=0
                                X                            X
                              =  (φj (ωj − ωi )|Ui ∩Uj )Ui +   φj ωi |Ui
                                 j̸=0                            j̸=0
                                X
                              =  (φj (ωj − ωi )|Ui ∩Uj )Ui − φ0 ωi + ωi
                                 j̸=0

52 CHAPITRE 1. SUPERFORMES SUR UN ESPACE VECTORIEL RÉEL (D’APRÈS LAGERBERG)

Puisque ωj − ωi ∈ NPp,q (Ui ∩ Uj ), la forme (φj (ωj − ωi ))Ui appartient à NPp,q (Ui ). Comme
φ0 est nulle au voisinage de P , le terme −φ0 ωi appartient à NPp,q (Ui ). Cela prouve que
ω ′ |Ui coïncide avec ωi au voisinage de P modulo NPp,q et conclut la démonstration.
```

### primary-03: CLD 1.9.8-9: differentials and dimension nullity

Cached primary CLD-v2.txt, lines 2494 to 2509. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
1.9.8. — Soit GV et HV des sous-faisceaux en R-vectoriels de FV tels que les dérivées
partielles de toute fonction de GV soient définies et appartiennent à HV . Alors, les
opérateurs d′ et d′′ induisent deux opérateurs différentiels d′ et d′′ de GV∗,∗ vers HV∗,∗ . Si
GV ⊂ CV2 , ces opérateurs vérifient d′ d′ = d′′ d′′ = 0 et d′ d′′ = − d′′ d′ .
   Lorsque GV = HV = AV sont le faisceau des fonctions lisses sur V , les opérateurs d′
et d′′ sont des dérivations au sens des algèbres graduées.
   Les formules du lemme 1.3.6 restent valables dans ce contexte.
Lemme 1.9.9. — Si P est un sous-espace paralinéaire de V tel que dim(P ) <
max(p, q), le G-préfaisceau FPp,q est nul.
Démonstration. — Soit Q un sous-espace paralinéaire de P et soit α un élément
de FPp,q (Q) = FQp,q (Q) ; prouvons que α = 0. Comme on peut raisonner localement
sur Q, on peut supposer que α est donné par une forme ω ∈ FVp,q (W ), où W est un
voisinage ouvert de Q dans V . Pour toute cellule C de V qui est contenue dans Q, one
a dim(C) ⩽ dim(P ) < max(p, q), et donc ω|C = 0. Cela démontre que ω|Q = 0, d’où le
lemme.
```

### primary-04: CLD 3.3.3: ambient coefficient representatives

Cached primary CLD-v2.txt, lines 3696 to 3707. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
3.3.3. — Pour tout domaine V de X et tout couple (p, q) d’entiers naturels, notons
Gpfp,q (V ) la limite inductive des R-espaces vectoriels GPp,q (P ), lorsque (f : V → E, P )
parcourt l’ensemble des cartes G-tropicales sur V .
    Lorsque V parcourt l’ensemble des domaines de X, les espaces vectoriels Gpfp,q (V )
définissent un préfaisceau sur le site XG .
    Soit V un domaine de X et soit (f : V → E, P ) une carte G-tropicale sur V . Toute
forme α appartenant à GPp,q (P ) définit un élément de Gpfp,q (V ) qui est noté f ∗ α.
    Par définition, toute section de Gpfp,q (V ) est de cette forme ; on peut même supposer
que P est ouvert. Plus précisément, soit (f : V → E, P ) une carte G-tropicale sur V ,
soit α ∈ GPp,q (P ) ; il existe un ouvert U de E dont P est une partie fermée ; d’après le
lemme 1.9.4, il existe β ∈ GEp,q (U ) telle que α = β|P ; on a alors f ∗ α = f ∗ β.
```

### primary-05: CLD 3.3.10-12: wedge, Leibniz, pullback

Cached primary CLD-v2.txt, lines 3762 to 3796. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-06: CLD 3.4.4: compact-image nullity, whole proof

Cached primary CLD-v2.txt, lines 3861 to 3877. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-07: CLD 5.4.3-4: compact charts are pleasant

Cached primary CLD-v2.txt, lines 6387 to 6402. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
Définition 5.4.3. — On dit qu’une carte G-tropicale f : X → E est agréable si f (Σf )
est paralinéaire et si l’application paralinéaire f |Σ(n) est propre sur son image.
                                                     f


                                                                         (n)
   C’est en particulier le cas si f |Σ(n) est propre, en particulier si Σf possède une dé-
                                      f
composition cellulaire finie en f -cellules.
                                                                         (n)
   Lorsque f est une carte agréable, nous noterons Πf l’ensemble f (Σf ) et l’appellerons
le polyèdre tropical de la carte G-tropicale agréable f . Il est purement de dimension n
                                                               (n)
et l’application f induit une immersion par morceaux de Σf sur Πf .
5.4.4. — Si X est compact, toute carte G-tropicale est agréable et l’on a Πf = f (X)(n)
(proposition 5.2.5).
```

### primary-08: CLD 5.8.1-5: top forms and actual variation measures

Cached primary CLD-v2.txt, lines 6727 to 6794. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
5.8.1. — Soit ω ∈ FXn,n  G
                           (X), soit Σ une partie squelettique fermée de X qui supporte
fortement ω. Par la construction du §4.5.5, en accouplant la restriction ω|Σ à Σ de la
forme ω et le n-calibrage µΣ de Σ, on obtient une forme-volume n-dimensionnelle ω̃Σ
sur Σ, et donc une forme-volume n-dimensionnelle sur X au sens du §5.6. D’après la
proposition 4.5.8 et la définition d’un support fort, cette forme-volume sur X ne dépend
pas du choix de Σ ; on la note ω   e . Elle est positive si ω est une forme positive, car le
calibrage canonique est positif (lemme 14.3.4).
Lemme 5.8.2. — Soit ω ∈ FXn,n     G
                                    (X). On suppose qu’il existe une partie squelettique
fermée de X qui supporte fortement ω. Pour tout domaine analytique Y de X, il existe
une partie squelettique fermée de Y qui supporte fortement ω|Y et l’on a l’égalité ω|
                                                                                   g Y =
ω̃|Y de formes-volume n-dimensionnelles sur Y .
Démonstration. — Soit Σ une partie squelettique fermée de X qui supporte fortement ω.
Alors, T = Σ ∩ Y est une partie squelettique fermée de Y qui supporte fortement ω|Y .
De plus, on a
      ω|Y = ⟨(ω|Y )|T , µT ⟩      par définition de ω|
      g                                             g Y

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
```

### primary-09: CLD 5.10.1: integration/pushforward, whole proof

Cached primary CLD-v2.txt, lines 6932 to 6970. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-10: CLD 5.11.1: Stokes and the separate symmetric Green statement

Cached primary CLD-v2.txt, lines 6995 to 7018. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-11: CLD 6.2.1-2: ordinary smooth forms

Cached primary CLD-v2.txt, lines 7069 to 7078. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-12: CLD 7.3.5: continuous/non-tropical multiplier currents, full ending

Cached primary CLD-v2.txt, lines 8130 to 8179. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
                                         G
                                            ) → π∗ (L1loc,X ⊗ AXp,q
                                                                 G
                                                                    ),
on en déduit un homomorphisme
                                     1
                               π∗ (Lloc,X ⊗ AXp,q
                                               G
                                                  ) → (Dp,q )X
qu’on note encore ω 7→ [ω].
  Pour toute forme α de type (n − p, n − q), lisse à support compact, on a
                            Z             Z                   Z
                      −1           −1           −1
   ⟨J[ω], α⟩ = ⟨[ω], J α⟩ =   ω∧J α=           J (Jω ∧ α) =     Jω ∧ α = ⟨[Jω], α⟩.
                               X                  X                      X
Ainsi, J[ω] = [Jω].
  On laisse au lecteur le soin d’écrire la variante de cette construction pour les intégrales
de bord.
```

### primary-13: CLD 11.1.1-2: Banach spectra and affinoid foundations

Cached primary CLD-v2.txt, lines 14848 to 14929. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-14: CLD 11.1.5-10: rational neighborhoods, good spaces, tensors, residue fields

Cached primary CLD-v2.txt, lines 14948 to 15089. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
ceux définis en 11.1.1. Le corps résiduel κ(x) de l’anneau local OX,x se plonge naturelle-
ment dans H (x). On dira que X est presque bon en x si κ(x) est dense dans H (x) et si
le germe (X, x) est séparé, et qu’il est presque bon s’il est presque bon en tout point. Si
X est presque bon en x, tout domaine analytique de X contenant x est encore presque
bon en x. Un espace bon est presque bon. Le point x est traditionnellement dit rigide si
H (x) est une extension finie de k (la terminologie provient du fait que ces points sont
ceux considérés par Tate dans sa théorie des espaces analytiques rigides).
   Soit f : Y → X un morphisme entre espaces k-analytiques et soit x ∈ X. La fibre
f (x) possède une structure naturelle d’espace H (x)-analytique, et sera toujours im-
  −1

plicitement considérée comme munie de cette structure. Nous la noterons souvent Yx .
```

### primary-15: CLD 11.2.2-3: separatedness and all local dimensions

Cached primary CLD-v2.txt, lines 15248 to 15346. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
complète L de k telle que AL := A b       ⊗k L soit strictement L-affinoïde. La dimension de
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
      dk (x) = degtr(H      (x)/k̃) = degtr(H       k 1 ) + dimQ Q ⊗Z (|H (x)× |/|k × |) ,
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
```

### primary-16: CLD 11.4.1: relative-interior composition equality

Cached primary CLD-v2.txt, lines 15506 to 15534. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-17: CLD 11.4.4: actual finite-module Banach algebras

Cached primary CLD-v2.txt, lines 15567 to 15602. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
plus X et Y sont bons OY,y est un OX,x -module de type fini. La finitude en un point est
stable par composition et changement de base analytique sur k.
```

### primary-18: CLD 11.7.7: strict affinoid neighborhood bases

Cached primary CLD-v2.txt, lines 16121 to 16141. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
la réduction (X,  x) est égale à P        , et est en particulier stricte ; mais comme X n’est
                                   H
                                   ^ (x)/e
                                         k
constitué que de points de type 3, il ne possède aucun domaine strictement affinoïde non
vide.
```

### primary-19: CLD 13.3.1-3: degree and Artinian base change, complete lemma proof

Cached primary CLD-v2.txt, lines 19143 to 19191. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-20: CLD 14.1.8: compact pleasant moments

Cached primary CLD-v2.txt, lines 20151 to 20154. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
Proposition 14.1.8. — Si X est un espace k-analytique compact de niveau n, tout
moment sur X est agréable.
Démonstration. — C’est un cas particulier du §5.4.4.
```

### primary-21: CLD 14.1.12: compatible skeletal refinements, complete proof

Cached primary CLD-v2.txt, lines 20242 to 20281. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
Proposition 14.1.12. — Soit X un espace analytique de niveau n et soit f : X → T
                            (n)
un moment agréable. Alors, Σf est paracompact.
                                                    (n)
  Il existe une décomposition cellulaire C de Σf en f -cellules commodes et une décom-
                                       (n)
position cellulaire forte D de ftrop (Σf ) tel que le couple (C , D) soit adapté à l’immersion
par morceaux compacte ftrop |Σ(n) .
                                 f
                                                                             (n)
  Enfin, pour tout couple (C , D) comme ci-dessus, ftrop (∂(X) ∩ Σf ) est une partie
                   (n)
fermée de ftrop (Σf ), contenue dans la réunion des cellules de dimension ⩽ n − 1 de D.
                                                          (n)
  On dira qu’une décomposition cellulaire C de Σf est agréable (relativement à f ) s’il
existe une décomposition cellulaire D (nécessairement unique) telle que le couple (C , D)
vérifie les conclusions de la proposition.
                                      (n)
Démonstration. — L’espace ftrop (Σf ) est réunion d’une famille dénombrable de sous-
                                                                               (n)
espaces compacts, dont l’image réciproque par ftrop est compacte dans Σf , par définition

                                  § 14.2. MOMENTS ET DEGRÉS                                   399

                                        (n)
d’un moment agréable. Par suite, Σf est réunion d’une famille dénombrable de sous-
espaces compacts. Cela entraîne qu’il est paracompact.
                                                                         (n)
  D’après le lemme 14.1.5, il existe une décomposition cellulaire C1 de Σf en f -cellules
                                                                                               (n)
commodes. D’après la proposition 2.3.6, il existe une décomposition cellulaire C de Σf
                                                                                              (n)
qui raffine C1 et une décomposition cellulaire D adaptée à l’inclusion de ftrop (Σf )
dans Ttrop tel que le couple (C , D) soit adapté à l’immersion par morceaux compacte ftrop .
Ses cellules sont des f -cellules commodes car la décomposition cellulaire C raffine C1 .
  La dernière assertion découle de la définition d’une cellule commode.



                           § 14.2. MOMENTS ET DEGRÉS
```

### primary-22: CLD 14.2.2: actual constant finite-flat degrees, complete proof

Cached primary CLD-v2.txt, lines 20288 to 20316. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-23: CLD 14.3.2-6: canonical calibration and scalar projection, complete proof endings

Cached primary CLD-v2.txt, lines 20714 to 20803. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-24: CLD 14.4.3: same-carrier restriction factor, full body

Cached primary CLD-v2.txt, lines 20860 to 20875. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

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
```

### primary-25: CLD 14.5.1-2: positive summed image calibration

Cached primary CLD-v2.txt, lines 20876 to 20903. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-26: CLD 15.1.1: ordinary unit descriptions, complete proof

Cached primary CLD-v2.txt, lines 21482 to 21509. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

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
```

### primary-27: CLD 15.2.2: good Hausdorff implies local holomorphic separation

Cached primary CLD-v2.txt, lines 21556 to 21571. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
15.2.2. Séparation holomorphe. — On dira qu’un espace analytique X est holo-
morphiquement séparé si pour tout couple (x, y) de points de X avec x ̸= y il existe une
fonction analytique f sur X telle que |f (x)| ̸= |f (y)|. Un tel espace est topologiquement
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
```

### primary-28: CLD 15.2.5: compact cutoff, entire stated proof

Cached primary CLD-v2.txt, lines 21591 to 21597. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
Corollaire 15.2.5. — Soit X un espace analytique localement holomorphiquement sé-
paré. Soit K une partie compacte de X et soit U un voisinage ouvert de K. Il existe
une fonction lisse sur X qui vaut 1 au voisinage de K et dont le support est compact et
contenu dans U .
Démonstration. — Comme X est localement différentiellement séparé, c’est une consé-
quence du corollaire 6.2.4.
```

### primary-29: CLD 15.3.1: canonical scalar top-measure projection, full proof

Cached primary CLD-v2.txt, lines 21651 to 21660. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
Proposition 15.3.1. — Soit L une extension complète de k, soit p : XL → X le mor-
phisme de changement de base. Pour toute forme ω de type (n, n) sur XG à coefficients
tropicalement boréliens, on a p∗ (ωL,Bor ) = ωBor . Lorsque ω est localement intégrable, on
a p∗ (ωL,Rad ) = ωRad .

Démonstration. — En revenant aux définitions, on déduit de la compatibilité du cali-
brage canonique à l’extension des scalaires (proposition 14.3.6) l’égalité p∗ ω
                                                                              fL = ωL de
formes-volume n-dimensionnelles. La proposition en résulte.
```

### primary-30: CLD 15.7.1-2: pure analytic tropical structure and domain compatibility

Cached primary CLD-v2.txt, lines 22041 to 22062. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-31: CLD A.2.3-4: supporting compact-cutoff argument, full proofs

Cached primary CLD-v2.txt, lines 29020 to 29050. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text
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
```

### primary-32: Ducros Theorem 3.2: correct upper bound and full primary proof

Cached primary Ducros-2012.txt, lines 2077 to 2150. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

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
```

### primary-33: Berkovich 1.5.3-5: boundaryless finite maps and base-change interiors

Cached primary Berkovich-1993.txt, lines 1288 to 1323. The next primary heading is the extraction boundary; no output-budget truncation was used. Source typography and OCR artifacts are retained.

```text

      1.5.3. Examples. — (i) If P is the class of all morphisms of good analytic spaces,
then the morphisms from P are said to be good. For example, finite morphisms and
locally closed immersions are good morphisms.
       (ii) If P is the class of closed morphisms of good analytic spaces ([Ber], p. 49),
then the morphisms from P are said to be closed. For example, finite morphisms and
locally closed immersions are closed morphisms.
       (iii) I f P is the class of proper morphisms of good analytic spaces ([Ber], p. 50),
then the morphisms from P are said to be proper. It follows from the definitions that a
morphism is proper if and only if it is compact and closed. For example, finite morphisms
are closed. Conversely, if a proper morphism has discrete fibres, then it is finite
([Ber], 3.3.8).

      1.5.4. Definition. — The relative interior of a morphism 9 : Y -> X is the set Int(Y/X)
of all points y e Y for which there exists an open neighborhood i^ofjy such that the
induced morphism i^ -> X is closed. The complement of Int(Y/X) is called the relative
boundary of 9 and is denoted by ^(Y/X). IfX ==^(^), these sets are denoted by Int(Y)
and (?(Y) and are called the interior and the boundary of Y, respectively.
      It follows from the definition that ^(Y/X) = 0 if and only if the morphism y is
closed. The following properties of the relative interior are easily deduced from the
definition and [Ber], 3.1.3.

      1.5.5. Proposition. — (i) If Y is an analytic domain in X, then Int(Y/X) coincides
with the topological interior ofY in X.
                                          u/   <p
      (ii) For a sequence of morphisms Z -> Y -> X, one has

                 Int(Z/Y) n ^(In^Y/X)) C Int(Z/X).

             fiTALE COHOMOLOGY FOR NON-ARCHIMEDEAN ANALYTIC SPACES                               35

If 9 is locally separated (resp. and good) then
                   Int(Z/X) C Int(Y/X) (resp. Int(Z/X) = Int(Z/Y) n ^(In^Y/X));.
      (iii) For a morphism f: X' -^X, (w? A^/'-'(In^Y/X)) C Int(YyX'), o^?/' ^
Y ' ^ Y x^X'-^Y.
      (iv) For fl non-Archimedean field K ozw ^, ow? has Tc-^In^Y/X)) C Int(Y §» K/X ® K),
wfer^ TT ^ Y ® K -> Y. •
```

**End of embedded primary bodies and authoritative argument.**



# Complete supporting proofs supplied for independent reconstruction

These are mathematical evidence, not grants of assumptions. Each application and dependency must be reconstructed. Prior verdicts and hashes do not replace these proofs.
