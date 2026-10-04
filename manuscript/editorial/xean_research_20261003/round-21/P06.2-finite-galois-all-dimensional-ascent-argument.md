# Finite Galois transport of ordinary zero-Hessian currents

Unverified proof draft, 4 October 2026. Author audit only. The original atom
P06.2 remains open. No catalogue description, earlier proof, receipt, model
verdict, or hash is a mathematical premise of this argument.

## Result and scope

Let K be a complete nontrivially valued non-Archimedean field, let E/K be
any finite Galois extension, and let X be a good, separated, strict,
boundaryless K-analytic space, pure of dimension n >= 1. Retain the actual
analytic structure of X, including its nilpotents. Let h: X -> R be finite
and continuous and let pi: X_E -> X be scalar projection. The assertion
proved below is

\[
 d'd''[h]=0\quad\Longleftrightarrow\quad d'd''[h\circ\pi]=0.       \tag{T}
\]

The tests on each side are **all** ordinary smooth, compactly supported
(n-1,n-1)-forms. The respective canonical CLD calibrations are used. No
ramification, residue-characteristic, perfectness, normality, reducedness,
unit separation, Radon-Hessian, or invariant-form-descent hypothesis is
imposed. All open sets, neighborhoods, and supports below use the ordinary
Hausdorff topology. An affinoid neighborhood contains an ordinary open
neighborhood; this interior is not its absolute analytic interior.

This is a scalar-current transport theorem, not recognition of a general
continuous zero-current function as classically pluriharmonic. It establishes
the requested finite-Galois gate if the proof withstands independent review.
It does not establish two-sign regularization, ascent through the completion
of an infinite algebraic extension, purely inseparable ascent, transcendental
ascent, or full P06.2. None of those consequences is asserted here. The
original task and completion criteria are preserved verbatim in
original-task.json and original-problem.txt, rather than rewritten as a
weaker task.

Write D=d'd'' and t_f=-log|f| for an analytic unit. With a harmless fixed
duality sign suppressed, current vanishing means

\[
 B_h(\alpha):=\int_X h\,(D\alpha)_{\mathrm{Rad},K}=0
 \quad\text{for every }\alpha\in A_c^{n-1,n-1}(X).             \tag{1}
\]

Only differentiated smooth top forms in this proof define Radon measures.
No order-zero assertion is made about the Hessian current of h itself.

## Exact imported analytic foundations

These are foundations imported from primary texts, not conclusions from
earlier campaign manuscripts. The appendix embeds the primary bodies used,
including their complete endings and proofs when the primary text gives
one. The precise restricted uses are recorded here. The new algebraic,
Banach, support, and collar arguments are proved below.

**A. Affinoids and ordinary neighborhoods.** CLD, arXiv:1204.6277v2,
25 July 2025, sections 11.1.1-2, 11.1.5-10 and 11.7.7: affinoid
spectra are compact Hausdorff; an affinoid algebra is noetherian with closed
ideals and has surjective spectrum-to-prime-spectrum map. Its completed
residue field is the completion of the fraction field of the quotient by
the point's kernel. Rational affinoid neighborhoods can be chosen inside
any prescribed ordinary open with every defining inequality strict at the
point. Good strict spaces over a nontrivially valued field have strict
affinoid neighborhood bases. Affinoid domains admit finite rational
coverings (11.1.6). Products of affinoids use completed tensor
products, and scalar projection is surjective. CLD 11.4.4 makes a finite
algebra with its finite-module Banach topology affinoid. Actual quotient
Banach norms, not spectral seminorms on reductions, are used below.

**B. Dimensions and boundaries.** CLD 11.2.2-3: separatedness implies
Hausdorffness; on a strict affinoid analytic dimension is Krull dimension;
analytic domains preserve local dimension; local dimension at a point is
the maximum dimension of the minimal-prime components containing it.
CLD 11.4.1 gives the composition equality for relative interiors when the
middle-to-target morphism is locally separated. In its application below
that morphism is the finite separated map M(F)->M(K).
Berkovich, *Etale cohomology for non-Archimedean analytic spaces*, Publ.
Math. IHES 78 (1993), Proposition 1.5.5(i), (iii), (iv): an analytic domain's
relative interior is its ordinary topological interior; relative interior
is preserved by base change, including complete ground-field extension.
Thus ordinary opens and finite scalar extensions of boundaryless spaces
are boundaryless. We prove componentwise purity separately.

**C. Ordinary forms.** CLD Definition 6.2.1 and 6.2.2 define ordinary
smooth forms by smooth tropical descriptions on ordinary neighborhoods;
these form ordinary sheaves stable under wedge, J, d', d''. CLD Proposition
15.1.1(b) gives descriptions using finitely many analytic units. CLD 3.3.3
permits a coefficient form to be represented by a Euclidean smooth form on
an ambient open; this uses Lemma 1.9.4 only with the paralinéaire subset
closed in that open. CLD 3.3.11-12 gives Leibniz and functorial pullback for
forms. CLD Proposition 3.4.4 says that a coefficient-form pullback is zero
exactly when its restriction to the image of every compact domain is zero.
These inputs identify the ordinary sheaves on a same-carrier restriction
of scalars, without any claim about descent of arbitrary invariant forms.

**D. Compact cutoffs.** CLD 15.2.2 and Corollary 15.2.5: on a good
Hausdorff analytic space, for a compact C inside an ordinary open U there
is an ordinary smooth function equal to one near C with compact support
contained in U. We derive the finite compact partition and continuous
approximation statements below. We do not use the overly broad printed
compact-support assertion of CLD 15.2.9.

**E. Polyhedrality, calibration, and top measures.** Antoine Ducros,
*Espaces de Berkovich, polytopes, squelettes et théorie des modèles*,
Confluentes Math. 4 (2012), 1250007, Theorem 3.2(1): for a compact,
Gamma-strict k-analytic space of dimension d and finitely many analytic
units, their multiplicative norm image is a c-polytope of dimension **at
most** d, with c=(Q,(|k^*| Gamma)^Q). Taking minus logarithms gives the
finite affine polyhedral description used here. We apply it to strict
affinoids (Gamma={1}); no equality of moment dimension and analytic
dimension is used. The printed universal equality in CLD 12.2.4 is not
imported.

CLD 5.4.4 makes compact moment charts pleasant and identifies their
tropical polyhedron with the top-dimensional part of the image. CLD
14.3.2-5 defines the positive standard canonical calibration. On a
skeletal n-cell C, a torus projection q injective on its moment image gives
the constant calibration d_C times the inverse image of the primitive
volume, where d_C is the actual finite-flat moment degree. CLD 14.5.1-2
pushes these calibrations to the moment image: on an n-cell sigma its
weight is the sum of the positive d_C above sigma times the corresponding
primitive volume vector. CLD 5.8.1-5 associates a Radon measure to every
smooth top form, locally using precisely those calibrations, with absolute
variation equal to the associated Borel measure. CLD 5.10.1(c),(d) gives
the corresponding pushforward and integration formula in a pleasant
chart. Lower-dimensional cells carry no n-dimensional top measure.
All degrees count the actual finite fibre algebras and their Artinian
lengths. We spell out the resulting variation estimate below.

**F. Two different scalar comparisons.** CLD Proposition 14.3.6 and
Proposition 15.3.1: for a complete extension L/K and a locally integrable
(n,n)-form omega,

\[
 \pi_* (\pi^*\omega)_{\mathrm{Rad},L}
       =\omega_{\mathrm{Rad},K}.                             \tag{2}
\]

There is **no [L:K] factor**. CLD Remark 14.4.3: for a finite extension
F/K and an F-analytic space viewed as a K-analytic space on the **same
carrier**, the dimensions and skeletal subsets agree and

\[
 \mu_K=[F:K]\mu_F.                                          \tag{3}
\]

These are different comparisons. Neither imports a pullback of [h] or
D[h]. The finite Artinian-algebra reason for the normalization in (2)
is reconstructed below, in addition to the embedded primary proof.

**G. Stokes.** CLD Theorem 15.7.1 gives a Hausdorff pure n-dimensional
analytic space its tropical structure with its analytic boundary; 15.7.2
makes restrictions to analytic domains compatible. CLD Proposition
5.11.1(a) gives Stokes for compact C1 (n-1,n)-forms. On a boundaryless
space their d' integral is zero, and the J-transformed statement gives
the d'' version. Applying these twice below proves the integration by
parts formula for arbitrary complementary forms. The symmetric-form
restriction in the separately printed Green formula is not used.

The hypotheses just listed allow singularities and nilpotents. Their use
does not replace the measure by a normalized measure on the reduction.

## 1. Actual finite tensors, fibres, and component dimensions

### 1.0. Elementary field facts used in the construction

For completeness, no primitive-element or fixed-field result is hidden
in the induction. A finite separable extension L/K of an infinite field
has [L:K] embeddings into an algebraic closure: along a finite generating
tower, each existing embedding extends in exactly as many ways as the
degree of the next separable minimal polynomial, by choosing its distinct
roots. If a1,...,aq generate L, choose theta=sum_j c_j a_j so all these
embeddings give distinct values of theta. This is possible: each pair of
embeddings forbids a nonzero linear equation on (c_j); putting
(c_j)=(1,t,...,t^{q-1}) makes each forbidden equation a nonzero polynomial
in t, so finitely many forbidden roots cannot exhaust infinite K. The
minimal polynomial of theta has at least [L:K] distinct roots and degree
at most [L:K], hence L=K[theta]. Our K is infinite because a finite field
cannot have a nontrivial absolute value.

For normal separable E/K, every embedding of an intermediate field
extends to an embedding of E by the same successive-root construction;
normality puts the image back in E. Thus all such embeddings extend to
G. A G-fixed element has only one K-conjugate, so is in K: E^G=K.
For a subgroup H, put F=E^H and choose a K-primitive b for E. Then
E=F[b], and the product of T-hb over H has coefficients in F. Every
hb is a distinct root of the F-minimal polynomial of b, whereas that
minimal polynomial divides the product. Its degree is |H|, proving
E/F is Galois with group H. F/K is finite separable as a subextension
of E/K. For any embedding tau:F->E, its extension g in G identifies
the stage E/tau(F) with the conjugate subgroup gHg^{-1}.

### 1.1. Finite-module topology and invariants

For a K-affinoid Banach algebra A and a finite extension E/K of degree m,

\[
 A\widehat\otimes_K E=A\otimes_K E.                          \tag{4}
\]

Here is the topology justification. A fixed basis of a finite-dimensional
normed vector space over a complete valued field identifies its norm with
a norm equivalent to the coefficient maximum norm. Induct on dimension:
the span of all but the last basis vector is complete, hence closed; the
last vector has positive distance from it. Scaling that distance bounds
its coefficient in a vector; the ultrametric inequality and induction
bound the remaining coefficients. The upper bound follows directly from
the triangle inequality. Thus all coordinate maps E->K are bounded.
Tensor them with A. The tensor-norm upper bound in the other direction
identifies the topology on A tensor E with that on the finite direct sum
A^m. This direct sum is complete, proving (4). This proof is for the
actual algebra; no quotient by its nilradical occurs.

For G=Gal(E/K), the action 1 tensor g on (4) is bounded. The linear
equations (g-1)v=0 on E have common kernel K. Tensoring this finite kernel
calculation with a K-vector space is exact; hence

\[
 (A\otimes_K E)^G=A.                                       \tag{5}
\]

No averaging in characteristic p is used. In particular, an invariant
unit, together with its invariant inverse, is a unit of A. For every
unit f of A tensor E,

\[
N(f)=\prod_{g\in G}g f\in A^\times.                         \tag{6}
\]

For clarity, the point action and the translates of unit domains used
later are analytic on the restricted K-carrier: (4) is finite over A,
so foundation A makes it a K-affinoid algebra, and 1 tensor g is a
bounded K-algebra automorphism. Its K-spectrum is the same as its
E-spectrum because every seminorm restricts to the unique valued-field
norm on E. The actual rational algebras and their unit germs agree.
In particular |g f(y)|=|f(g^{-1}y)|. No invariance of a continuous
current or semilinear averaging of forms is used.

### 1.2. Analytic fibres and their decomposition groups

Let x belong to X, put C=H(x), and choose y above it. By (4) the actual
analytic fibre is M(C tensor_K E). A primitive element b for the finite
separable extension E/K identifies this algebra with C[T]/P(T), where
P is separable. Its factorization is a finite product of fields; each
factor is a finite complete valued extension of C and has one analytic
point. The uniqueness of its extending absolute value can be checked
without residue assumptions: two such values are equivalent norms on the
finite C-vector space, so comparison on z^r followed by r-th roots makes
them equal. Existence and completeness follow from the finite affinoid
field construction and the same finite-dimensional norm argument.

The G action is transitive on these factors. Otherwise the sum of the
idempotents of one orbit would be a nontrivial invariant idempotent, in
contradiction with (C tensor E)^G=C. Let H be the actual stabilizer of y
and let D_y be its field factor. Invariant tuples in the transitive
product are equivalent to H-invariant elements of D_y; therefore

\[
 D_y^H=C.                                                   \tag{7}
\]

The map E->D_y is injective. The image of b has |H| distinct H-conjugates,
and D_y=C[b]. The polynomial product over those conjugates has coefficients
in (7); the minimal polynomial of b over C divides it and has every one
of those distinct conjugates as a root. Its degree is consequently exactly
|H|. This proves directly that D_y/C is Galois with group H. In particular
the image of the finite separable field

\[
 F=E^H                                                     \tag{8}
\]

lies in C. If y is not fixed by all of G, H is proper and |H|<|G|.
This is a statement about the actual point and its fibre, not a
topological covering assertion.

### 1.3. Purity, strictness, and ordinary topology

Strict affinoid presentations base change to strict ones. Inverse images
of ordinary affinoid interiors give goodness upstairs; separatedness is
preserved by base change of the closed diagonal, and boundarylessness
follows from foundation B. The same assertions hold for ordinary opens.

We check every minimal component, not just total dimension. In a strict
affinoid neighborhood M(A) of a pure n-dimensional space, each minimal
prime P has dim(A/P)=n: by spectral surjectivity a point of kernel P
exists, belongs to that component alone, and its local dimension is n.
Let J be the nilradical. It is nilpotent. The injection

\[
 A/J\longrightarrow\prod_{P\text{ minimal}}\operatorname{Frac}(A/P)
\]

remains injective on tensoring with E. Each field tensor is reduced by
separability, so (A/J) tensor E is reduced. The nilradical of A tensor E
is exactly J tensor E. The kernels of the finitely many maps of this
reduced tensor algebra to those field factors are primes whose
intersection is zero. A minimal prime Q contains their product and hence
one of them; minimality makes it that kernel. Its contraction is its
associated P. The finite integral injection

\[
 A/P\hookrightarrow (A\otimes_K E)/Q
\]

preserves dimension. For clarity, this last elementary fact follows from
lying over, going up, and incomparability: for a finite integral injection
of domains C0->D0, localizing at p gives a nonzero finite C0_p-module.
If pD0_p=D0_p, the determinant of I minus a p-valued generator matrix
is a unit annihilating it, a contradiction. A maximal ideal over pD0_p
proves lying over. Apply the same argument after quotienting by a prime
to get going up. For incomparability, quotient by the smaller prime and
localize by the nonzero elements of the base domain. The resulting
finite integral domain over a field is a field: a minimum-degree monic
relation for a nonzero element expresses its inverse using its nonzero
constant term. Thus two strictly nested primes cannot have the same
contraction. Chain contraction and chain lifting prove dimension equality.

Every minimal component upstairs therefore has dimension n, and the
local dimension formula proves purity. Reduction was used only in this
dimension calculation, not in any current, unit, or calibration step.

Inverse images of compact sets under pi are compact. Indeed a downstairs
compact set is covered by finitely many ordinary interiors of affinoid
neighborhoods. Its inverse image is closed in the finite union of their
compact scalar extensions. Hausdorffness ensures that the closedness
statements here are ordinary topological statements.

We will repeatedly use a full-fibre shrinking observation. Inside an
affinoid neighborhood V0 of x, let N be an ordinary open in V0_E containing
the entire fibre over x. The compact complement has a closed image in V0
not containing x. Choose a smaller strict affinoid neighborhood V of x
inside that image's complement and inside the ordinary interior of V0.
Then V_E is contained in N. Its ordinary interior gives the corresponding
ordinary downstairs neighborhood. This retains any finite collection of
unit or strict norm conditions holding on the whole fibre.

## 2. A separable residue constant lifts to an actual neighborhood

**Local lifting lemma.** Suppose F/K is finite separable and a specified
K-embedding F->H(x) is given at a point of a good strict K-space. There
is a strict affinoid neighborhood V of x and a bounded embedding
F->O(V) whose evaluation is the specified embedding. Its restriction to
an ordinary neighborhood U of x makes U an F-analytic space on the same
carrier and with the same actual analytic function sheaf.

**Proof.** Let a be a primitive element of F, P its monic separable
minimal polynomial, and a also its specified image in H(x). Begin in a
strict affinoid neighborhood M(A0). The fraction field of A0/ker(x) is
dense in H(x). Thus choose g=f/b with b(x) nonzero and g(x) arbitrarily
close to a. Retain b invertible on a strict rational neighborhood, by
an inequality |b|>=|k0| strictly satisfied at x, with k0 in K^*. This
turns g into an actual analytic element. The following choices are
made before the final shrink.

Fix R in |K^*| with R>max(1,|a|), and fix d in |K^*| with
0<d<|P'(a)|. Put

\[
 M=\max\bigl(1,\max_{2\leq j\leq\deg P}
                     |p_j|R^{j-2}\bigr),
 \qquad P(T)=\sum_jp_jT^j.                                 \tag{9}
\]

Choose c in |K^*| so small that

\[
 s:=c/d<1,\qquad q:=Mc/d^2<1,\qquad s< R.                   \tag{10}
\]

This is possible by taking powers of a K-element of norm <1. Approximate
a sufficiently closely that |g(x)|<R, |P'(g)(x)|>d,
|P(g)(x)|<c and also |g(x)-a|<s. Preserve these strict inequalities
on the strict rational domain defined by

\[
 |g|\leq R,\quad |P(g)|\leq c,\quad |P'(g)|\geq d.            \tag{11}
\]

Here scalar representatives of R,c,d are chosen in K^*. The rational
algebra is an actual complete quotient of a Tate algebra with variables
g/R, P(g)/c, and d/P'(g). The last relation makes P'(g) invertible
as an actual algebra element. Its quotient Banach norm has

\[
 \|g\|\leq R,\quad\|P(g)\|\leq c,
              \|P'(g)^{-1}\|\leq d^{-1}.                    \tag{12}
\]

These bounds arise from relations in the quotient algebra and remain
valid in the presence of nilpotents. We have not inferred a Banach bound
from the spectral seminorm.

For ||z||<=R and ||v||<=min(1,R), binomial expansion and the
ultrametric inequality give

\[
 \|P(z+v)-P(z)-P'(z)v\|\leq M\|v\|^2,
 \qquad \|P'(z+v)-P'(z)\|\leq M\|v\|.                       \tag{13}
\]

Binomial coefficients have norm at most one; this also covers positive
characteristic. Starting with z0=g, iterate
z_{j+1}=z_j-P'(z_j)^{-1}P(z_j). Let v_j=z_{j+1}-z_j. The first
step has ||v0||<=s. If ||v_j||<=s, (13) and M s/d=q<1 show that
P'(z_{j+1}) is invertible by a Neumann series with inverse norm <=d^-1.
The Newton cancellation and (13) give

\[
 \|v_{j+1}\|\leq (M/d)\|v_j\|^2\leq q\|v_j\|.              \tag{14}
\]

All z_j have norm <=R. Thus the sequence converges in the actual Banach
algebra to z with P(z)=0, ||z-g||<=s, and invertible derivative.

Evaluation is norm-contracting. Both z(x) and a are roots within s of
g(x). For two such roots r,r', the factorization of P(r)-P(r') gives

\[
 P(r)-P(r')=(r-r')\bigl(P'(g(x))+w\bigr),\quad |w|\leq Ms<d.
\]

The factor in parentheses is nonzero; hence r=r'. Consequently z(x)=a.
The homomorphism K[T]/P->O(V) sending T to z is unital and injective,
because its source is a field and its target is nonzero (it has x).
It is bounded: finite-dimensional norm equivalence bounds the coefficient
maps in the basis 1,a,...,a^{deg P-1}, and their images are bounded
elements of O(V). This proves the desired lift.

We verify the F-analytic interpretation rather than treating it as a
change of notation. Let A=O(V). A bounded embedding of the finite valued
field F gives ||u||_A<=C|u| for u in F. The equivalent complete norm

\[
 \|b\|_F:=\sup_{u\in F^*}\|ub\|_A/|u|
\]

is F-homogeneous and submultiplicative: the original norm is bounded above
by this norm, and ||ab||_F<=||a||_F ||b||_A<=||a||_F||b||_F.
Choose a strict K-Tate presentation of A. Its finitely many generators
are power-bounded in the original quotient norm and hence in the
equivalent F-norm. They define a bounded surjection F{T1,...,Tq}->A.
The quotient norm is equivalent to the F-norm: boundedness gives one
inequality; lifting through the original K-Tate presentation gives the
other, since K{T} is a subalgebra of F{T}. Thus A is strictly F-affinoid.

Every bounded K-multiplicative seminorm on A restricts to the unique
extending absolute value on F, so the K- and F-affinoid spectra coincide
with their topology. Rational domains use the same elements of A and
the same inequalities; their actual quotient algebras are the same with
the induced bounded F-action. These common rational bases identify the
analytic sheaves on ordinary opens. Restrict to an ordinary neighborhood
U of x inside V to obtain the assertion. Nilpotent elements have been
retained throughout. **End of proof.**

The same argument identifies ordinary form sheaves on U over K and F.
Their unit germs, compact moment images, and ordinary descriptions are
identical. Foundation C's compact-image nullity criterion identifies
their relations. Supports, wedge products, d' and d'' therefore agree.
Equation (3) and the definitions of top measures give, on this same
carrier and for every complementary test alpha,

\[
 \int_U h\,(D\alpha)_{\mathrm{Rad},K}
 =[F:K]\int_U h\,(D\alpha)_{\mathrm{Rad},F}.                 \tag{15}
\]

The factor is a positive real integer, even in wild characteristic, and
can be cancelled for vanishing.

If U was chosen ordinary open in X, it is boundaryless over K. The
composition equality for U->M(F)->M(K), whose second map is finite
separated, makes U boundaryless over F as well. The same affinoid
algebras and minimal primes prove purity over F. Goodness and strictness
were checked above. Separatedness is retained: the F-fibre product is
the closed equalizer, inside the K-fibre product, of the two F-actions,
and the K-diagonal already is a closed immersion. Thus U is an admissible
input to the induction over F.

## 3. The off-fixed-point induction

We prove the forward assertion of (T) by strong induction on |G|,
simultaneously for every field and every space in its stated scope.
The trivial group is the identity assertion. Suppose smaller groups
have been treated. Let

\[
 S=\{y\in X_E:g y=y\text{ for all }g\in G\}.
\]

It is closed, as a finite intersection of equalizers of continuous maps
on a Hausdorff space. Let y not belong to S and put x=pi(y). Its group H
is proper. The specified F=E^H embedding in H(x) from section 1.2 lifts
on U by section 2. By (15), the restriction of h has zero F-Hessian
current on U.

For its actual F-algebra A, separability and normality give

\[
 F\otimes_K E\simeq\prod_{\tau:F\hookrightarrow E}E,
 \qquad
 A\otimes_K E\simeq\prod_{\tau}A\otimes_{F,\tau}E.           \tag{16}
\]

To see the first identity directly, a primitive polynomial for F/K splits
in E into its distinct linear factors; use the Chinese remainder theorem.
The second follows by tensoring over F. These are identities of the
actual algebras, not their reductions. Their finite-module topologies
agree by section 1.1, and their idempotents give open-and-closed analytic
components. The component selected by y is the one for the specified
embedding. On each component, regard U as a tau(F)-space via tau.
E/tau(F) is Galois with a group conjugate to H, of order |H|<|G|.
All the hypotheses of the induction have been checked in sections 1-2.
It proves zero current on that component, in particular near y.

Consequently B_{h_E} vanishes on every complementary test supported in
X_E minus S. For a compact such support, finitely many ordinary
neighborhoods of the kind just constructed suffice; compact smooth
partitions (proved next) split the test among them. There is no current
pullback in this step.

## 4. Compact partitions and continuous scalar approximation

One can reconstruct the compact-cutoff input directly here, avoiding
any overbroad partition statement. Given a point x inside an ordinary
open U, take an affinoid neighborhood V of x and put
F=V minus (its ordinary interior intersect U). This is compact and
does not contain x. Analytic functions on V separate x from every
point q in F by their norms. For such a function f, compose log|f|
on its nonzero locus with a real smooth function that takes the desired
distinct constant values near |f(x)| and |f(q)|. If either norm is
zero, choose the composing function constant on a sufficiently negative
logarithmic half-line; extension by that constant across the zero locus
is ordinary smooth. Thus there is an ordinary smooth function on V
equal to one near x and zero near q. A finite subcover of F and the
product of these functions gives b on V, one near x and zero on a
relative neighborhood of F. Extend it by zero outside V. It is smooth
on the ordinary interior of V and outside V; at each point of F, a
global ordinary neighborhood meets V only where b is zero, so it is
smooth there too. The support is a closed subset of compact V contained
in its interior intersect U. For a compact C in U, finitely many such
bumps and a smooth real composition of their sum of squares give a
compact smooth cutoff equal to one near C. This proves exactly the
compact cutoff used below. The embedded primary statement 15.2.5 is
consistent with this proof; the printed sign typo in the one-point
construction of A.2.3 is not an additional premise.

For a compact C and a finite ordinary open cover U1,...,Uk of C, use
foundation D point by point to obtain smooth compact bumps equal to one
near their centers and supported in the appropriate Ui. Compose each
with a nonnegative smooth real function equal to zero near zero and one
near one. Finitely many bumps cover C. Group them by index into psi_i
and set s=sum psi_i. It is positive near C. A second compact bump chi
supported in {s>0}, equal to one near C, gives

\[
 \theta_i=\chi\psi_i/s\quad\text{on }\{s>0\},
 \qquad \theta_i=0\quad\text{elsewhere}.                    \tag{17}
\]

These are ordinary smooth, compactly supported inside Ui and sum to
one near C. Extension by zero is smooth because the support lies compactly
inside the defining ordinary open. The same observation applies to every
test extension by zero below. No global paracompactness is required.

Given any continuous h on a fixed compact C and epsilon>0, take a finite
ordinary neighborhood cover on which the oscillation of h is <epsilon.
Apply (17), choose a value c_i of h on each member meeting C, and put
a=sum c_i theta_i. Then a is an ordinary smooth compact scalar function
and |a-h|<epsilon on C. Thus the exact scalar approximation needed below
follows from compact cutoffs; it is not a tropical factorization of h.

## 5. Norm forms match every test on the fixed moment subspace

Let beta be an arbitrary compact complementary ordinary test on X_E.
For y in S intersect supp(beta), the whole fibre over x=pi(y) is the
singleton {y}: transitivity in section 1.2 proves this. An ordinary
description of beta near y uses actual units f1,...,fk and an ambient
smooth superform. Intersect its finitely many G-translates so every
g f_i is an actual unit there. Full-fibre shrinking gives a strict
affinoid neighborhood V of x whose whole scalar extension is inside
that ordinary unit domain.

On V_E take the orbit moment

\[
 t=(t_{g f_i})_{i,g}: V_E\longrightarrow\mathbb R^{k|G|}.
\]

Repeated units may be retained as separate coordinates. G permutes
these coordinates. Let W be its fixed vector subspace, let i:W->R^{k|G|}
be inclusion, and let P0=|G|^-1 sum_g g be the real linear averaging
projection. At every actual G-fixed analytic point t belongs to W.
The coordinate corresponding to each orbit in P0 t is

\[
 |G|^{-1}\sum_g t_{g f_i}=|G|^{-1}t_{N(f_i)}\circ\pi.       \tag{18}
\]

By (6) these norms are actual downstairs units on V. The denominator in
(18) is a real denominator in a superform, not division in K.

Let omega be the ambient coefficient superform describing beta in this
orbit moment (pull back its original coefficient form under coordinate
projection). At t(y) the point is fixed. Shrink V again so that both
t(V_E) and iP0t(V_E) lie in the ambient coefficient domain. By a Euclidean
compact bump, extend omega to a global smooth ambient form, unchanged on
a neighborhood of both compact sets. This elementary extension uses a
compact subset of an open Euclidean set and introduces no singularities.
The form

\[
 \omega_0=P_0^*i^*\omega
\]

has i^*(omega-omega0)=0. Equation (18) makes t^*omega0 exactly the
pullback of a downstairs ordinary smooth form alpha0. This is matching
on W only; it does not say beta, or even an invariant beta, descends.

The compact set T=pi(S intersect supp(beta)) is covered by finitely many
ordinary downstairs neighborhoods Vi of this kind. Choose compact
downstairs theta_i by (17) with sum theta_i=1 near T. Then

\[
 \beta=\beta_{\rm rem}+\sum_i\beta_i,
 \quad \beta_i=\pi^*\theta_i\,\beta,
 \quad \beta_{\rm rem}=(1-\pi^*\sum_i\theta_i)\beta.          \tag{19}
\]

The remainder has compact support disjoint from S, so section 3 kills
its pairing. For each i define

\[
 \beta_{0,i}=\pi^*(\theta_i\alpha_{0,i}),
 \qquad \gamma_i=\beta_i-\beta_{0,i}.                        \tag{20}
\]

All these forms are extended by zero from their ordinary chart. They
have compact support contained in one fixed compact pi^-1(supp theta_i)
inside that chart. Foundation F, applied to the differentiated downstairs
test theta_i alpha0_i, gives

\[
 B_{h_E}(\beta_{0,i})=B_h(\theta_i\alpha_{0,i})=0.            \tag{21}
\]

No degree factor and no unexplained continuous-current pullback occurs.
It remains to kill gamma_i. Its coefficient-form restriction to W is zero;
if theta_i needs extra local moment coordinates, use W times the entire
space of those extra coordinates. Multiplication by theta_i preserves
this restriction-zero assertion.

## 6. The full tensor collar estimate, including boundary-face contact

Here is the elementary estimate needed for (20).

**Collar lemma.** Let Q be a fixed linear map on a Euclidean space V
with kernel W; an orthogonal projection may be used. Let sigma be a
compact n-dimensional affine polytope. Let xi be a smooth (n-1,n-1)
superform on a neighborhood of sigma and of the nearby W points, with
i^*xi=0 on W. Take a fixed smooth radial function chi on Q(V), equal
to one near zero and supported in the unit ball, and define

\[
 \xi_\delta(z)=\chi(Qz/\delta)\xi(z),\quad 0<\delta\leq1.
\]

On sigma, the coefficient L1 norms of D xi_delta are uniformly bounded
as delta tends to zero. The coefficient L1 norm of xi_delta tends to zero.
These conclusions still hold with arbitrary fixed constant cell volume
and with additional Euclidean coordinates on which Q is zero. Only the
restriction of the superforms to the affine tangent of sigma is measured.

**Proof.** Let L be the n-dimensional tangent plane of sigma and put
r=rank(Q|L). If its affine span misses W, the affine image Q(span sigma)
is a closed affine subspace not containing zero, at positive distance
from it. For sufficiently small delta the collar is empty. Otherwise
choose w0 in that affine span intersect W and write z=w0+u+v, with
u in L intersect W and v in a fixed complement L1 of dimension r.
Q|L1 is an isomorphism to its image. Compactness bounds u in one fixed
box, and |Qz|<=delta bounds v in a box of side O(delta). Fubini and the
fixed determinant give collar volume O(delta^r). This argument does not
require w0+u to belong to sigma: it works for a cell meeting W only at a
boundary face, or with zero-dimensional intersection. If a compact cell
itself misses W, its distance is positive and the same conclusion follows.

For r=0 a cell intersecting W lies in W. Its xi restriction is identically
zero, so the restriction of D xi_delta is also identically zero. For
r>=2, cutoff derivatives of orders j=0,1,2 are O(delta^-j) on the fixed
cell, and xi and its first two coefficient derivatives are bounded.
The Leibniz expansion therefore bounds D xi_delta by O(delta^-2).
Multiplying by O(delta^r) gives a uniform integral bound.

For r=1 write the affine tangent coordinates as (u1,...,u_{n-1},t),
with z=w0+u+t v and v fixed, Qv nonzero. The cutoff restricted to this
plane depends only on t and has derivatives O(delta^-1) and
O(delta^-2). Expand the restricted xi in the exterior basis using
d'u_j,d't and d''u_j,d''t. There is exactly one possible basis monomial
of bidegree (n-1,n-1) containing neither d't nor d''t:

\[
 A(u,t)\,d'u_1\wedge\cdots\wedge d'u_{n-1}
          \wedge d''u_1\wedge\cdots\wedge d''u_{n-1}.         \tag{22}
\]

Its coefficient A(u,0) is zero, because the u-plane at t=0 is tangent
to W and i^*xi=0 there. Smoothness on a fixed compact neighborhood gives
|A(u,t)|<=C|t|. The comparison point w0+u can lie outside the cell;
it is still on W and within O(delta) of its compact collar. This is
exactly why restriction-zero is needed on the ambient W, not just at
points of sigma intersect W.

The second-cutoff term is chi''(t) d't wedge d''t wedge xi. Every
monomial of xi containing at least one transverse generator is annihilated
by a repeated exterior generator. Only (22) remains, bounded by
O(delta^-2) O(delta)=O(delta^-1) on the collar. All first-cutoff terms
are O(delta^-1), since their other coefficients and derivatives are
bounded. The term chi D xi is bounded. The collar volume is O(delta),
so all differentiated terms have bounded coefficient L1 norm. This
includes n=1: then (22) is just the scalar coefficient, vanishing on W.

For the undifferentiated form, coefficients are bounded and every
positive-rank collar has volume tending to zero; rank-zero cells either
miss the collar or give the zero restriction. A finite number of cells,
fixed coordinate Jacobians, and fixed positive calibration constants do
not change either conclusion. **End of proof.**

This lemma is not a claim that a small collar gives small differentiated
variation; the latter is only bounded and need not tend to zero. Rank one
uses both exterior-tensor cancellation and the first-order vanishing in
(22). No balanced-fan recognition theorem or curve probe is involved.

### 6.1. From coefficient bounds to actual top-measure variation

On a compact affinoid moment chart of dimension n, foundation E gives a
finite polyhedral image and a finite skeletal n-cell refinement. Above
each image cell sigma, the finitely many skeletal cells map by affine
isomorphisms and have positive constant calibration d_C times a primitive
volume. For an ambient top form zeta, its density on each such sheet is
the same affine-tangent scalar density, multiplied by that positive
constant. Thus taking absolute values before summing gives

\[
 \|(t^*\zeta)_{\mathrm{Rad}}\|_{\mathrm{TV}}
 \leq\sum_{\sigma} c_\sigma
        \int_\sigma\|\zeta|_{T\sigma}\|\,d\operatorname{vol}_\sigma,
                                                                  \tag{23}
\]

for fixed finite c_sigma. In an oriented tangent basis the scalar-density
version is an equality; the norm inequality allows arbitrary bases.
There is no signed cancellation hidden in this bound. It is the local
construction in CLD 5.8.4-5 plus 14.3.2 and 14.5.2, not an inference
from signed pushforward equality alone. The constants include all actual
finite-flat fibre dimensions, and therefore all nilpotent lengths.
Cells below dimension n contribute zero. If the whole moment image has
dimension <n, every represented top form is zero. We never replace that
case by an assumed universal dimension equality.

Finitely many such compact charts covering a fixed ordinary compact
support suffice. Top measures restrict compatibly to domains; overcounting
their positive variations in an overlapping cover yields an upper bound.
No derivative of a partition is needed to obtain (23).

## 7. Weak convergence on the full continuous multiplier

Fix a gamma=gamma_i from (20), its orbit moment t, and put Q=1-P0.
Choose the radial chi of section 6 and define, in its chart and extended
by zero,

\[
 e_\delta=\chi(Qt/\delta)\gamma.                            \tag{24}
\]

These are ordinary smooth complementary tests with supports in the
same compact C. The compact test (1-chi(Qt/delta)) gamma has support
disjoint from S: on S, Qt=0 and the multiplier equals zero on an ordinary
neighborhood. Section 3 therefore gives the **exact** identity

\[
 B_{h_E}(\gamma)=B_{h_E}(e_\delta)\quad(\delta>0).             \tag{25}
\]

Cover C by finitely many strict affinoid neighborhoods contained in the
chart, and add moment coordinates for local descriptions of the fixed
downstairs cutoff theta_i. On each enlarged ambient space, gamma is a
smooth coefficient form whose restriction to W times the extra space
vanishes. The collar lemma, (23), and the finite cover give

\[
 \sup_{0<\delta\leq\delta_0}
       \|(D e_\delta)_{\mathrm{Rad},E}\|_{\mathrm{TV}}<\infty. \tag{26}
\]

The constant may depend on this test and this compact carrier. It is
independent of delta. This is a statement about smooth differentiated
forms, not a Radon regularity hypothesis on D[h_E].

Let a be any fixed ordinary smooth compact scalar multiplier. Stokes
twice, on the boundaryless pure space X_E, gives

\[
 \int_{X_E}a\,D e_\delta=\int_{X_E}e_\delta\wedge D a.        \tag{27}
\]

For explicit signs, 0=integral d'(a d''e) says integral aDe=
-integral d'a wedge d''e. Next 0=integral d''(d'a wedge e) says
integral d'a wedge d''e=integral d''d'a wedge e=-integral Da wedge e.
The total degree of e is even, so Da wedge e=e wedge Da. These
calculations require no symmetry of e and thus treat every ordinary
complementary test.

To show the right side tends to zero, add **the moment coordinates
describing a** on a finite compact chart cover of C. This additional
refinement is essential: L1 information on a smaller moment need not
by itself control a wedge with Da. The enlarged fixed subspace is
W times all the added coordinates, and the coefficient restriction of
gamma still vanishes there. The undifferentiated conclusion of the
collar lemma gives L1 convergence to zero on every calibrated n-cell of
this enlarged moment; Da has bounded coefficients on the fixed compact
images. Formula (23) applied to e_delta wedge Da proves

\[
 \int a\,(D e_\delta)_{\mathrm{Rad},E}\longrightarrow0.       \tag{28}
\]

The refinement and constants for (28) may depend on a. They do not need
to be uniform in a. Uniformity in delta for (26), already obtained
without a, is what the continuous passage uses.

Approximate h_E on C within epsilon by an ordinary smooth compact a
using section 4. If M is the bound in (26), then

\[
 \limsup_{\delta\to0}
 \left|\int h_E\,(D e_\delta)_{\mathrm{Rad},E}\right|
 \leq M\varepsilon.                                       \tag{29}
\]

Let epsilon tend to zero. Equations (25) and (29) imply B_{h_E}(gamma)=0.
By (19)-(21), B_{h_E}(beta)=0 for the original arbitrary compact test.
This completes the induction and the forward implication of (T).

## 8. Reverse transport and the normalization with actual lengths

For alpha in A_c^{n-1,n-1}(X), pi^*alpha is an ordinary smooth
complementary test with compact support, since pi has compact inverse
images. It is an allowed test upstairs, not a restriction of the upstairs
test class to pullbacks. Apply (2) to omega=Dalpha and use the continuous
multiplier h and the defining pushforward of a signed Radon measure:

\[
 \begin{split}
 B_{h_E}(\pi^*\alpha)
 &=\int_{X_E}(h\circ\pi)\,(\pi^*D\alpha)_{\mathrm{Rad},E}\\
 &=\int_X h\,(D\alpha)_{\mathrm{Rad},K}=B_h(\alpha).
 \end{split}                                               \tag{30}
\]

This proves the reverse implication with no [E:K] factor.

Here is the finite-length algebra in the imported scalar calibration
proof. If R is a finite Artinian C-algebra of dimension d and C' is a
complete extension, then R tensor_C C' is still d-dimensional as a
C'-vector space. Its decomposition into local Artinian factors R_j has

\[
 d=\sum_j\dim_{C'}R_j
   =\sum_j\operatorname{length}_{R_j}(R_j)
                         [\kappa_j:C'].                    \tag{31}
\]

To verify the second equality, take a composition series of each local
factor; every simple quotient is its residue field. Tensoring a C-basis
proves the first dimension statement, without any reducedness or
separability assumption on R. A finite-flat moment fibre is exactly such
an actual algebra. Above the corresponding standard torus Gauss point,
scalar extension chooses its canonical Gauss lift and partitions those
fibre factors; (31) says their degrees sum to the original degree.
On every skeletal n-cell this is precisely the primary proof of CLD
14.3.6, using CLD 13.3.3, and gives (2). The source appendix includes
those complete proofs. In contrast, restricting an F-moment to K
composes its finite-flat torus projection with G_m,F^n->G_m,K^n,
whose actual fibre rank is [F:K]; this gives (3), not (2).

At no point did we replace a local Artinian algebra by its residue field
or a singular component by a component of maximal total dimension.
Equations (4), (5), (6), (11)-(16), (23), and (31) all preserve the
actual structures required in the assignment.

## Audit boundaries and comparison with the catalogue

The new scope is every finite Galois scalar extension on every pure
n-dimensional space in the original strict, good, separated,
boundaryless setting, for finite continuous multipliers. It includes
non-quasi-smooth germs in all positive dimensions and actual nilpotent
thickenings. Unlike the catalogue's scalar-stable special cases, its
upstairs current equation is a conclusion rather than a hypothesis.
It is also stronger than a curve-only scalar-test result: the proof
starts with an arbitrary compact (n-1,n-1) form, uses full tensor
coefficients, and treats every local n-cell and lower-dimensional
moment image.

The conclusion is still just a missing gate. The original recognition
target also requires a bridge from continuous current positivity of the
two signs to the classical curve-test notion (or another recognition
argument). No such bridge is proved. No completed-algebraic ascent is
claimed: finite-stage descent and gluing of arbitrary complementary
ordinary forms would have to be established separately. No mixed-finite
or transcendental ascent is claimed. The unrestricted non-strict
arbitrary-radius statement from the catalogue is untouched.

The self-audit, source-integrity checks, finite diagnostics, and two
document compilations are evidence about the draft and its artifacts;
they are not formal verification or priority certification. The original
atom has status partial and candidate=false. The source appendix below
is part of this authoritative argument; it is not replaced by references
to earlier campaign arguments or review receipts.

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
