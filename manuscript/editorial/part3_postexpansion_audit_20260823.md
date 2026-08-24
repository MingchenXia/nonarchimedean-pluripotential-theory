# Part III post-expansion mathematical and source audit (23 August 2026)

## Scope and source firewall

This audit covers Chapters 20--31 after the second-draft expansion.  It is a
mathematical-correctness and provenance audit, not a Rethlas verification of
new mathematics.  Corrections of computations or of the scope of imported
theorems are not promoted as new results.

The author's Deligne-pairing paper arXiv:1710.09731 is excluded completely.
No argument, citation, or traceable dependency in this audit uses it.

Primary comparison sources include Boucksom--Favre--Jonsson's papers on
singular semipositive metrics and non-Archimedean Monge--Ampere equations,
Chambert--Loir's local-height construction, and the exact later sources named
at the point where the manuscript goes beyond the original BFJ signature.

## Corrections already integrated

### Chapter 20: vertical-factor intersection pairing

The former absolute \((n+1)\)-fold pairing on arbitrary closed model forms
did not descend from relative numerical equivalence.  It has been restricted
to the BFJ pairing

\[
 (D\mathbin\cdot\theta_1\cdots\theta_n)
 =\int\varphi_D\,\operatorname{MA}(\theta_1,\ldots,\theta_n),
\]

with an actual vertical divisor in the first slot.  Apparent absolute powers
in the concavity argument and blown-up-plane example are now written as
mixed vertical energy-difference sums.  This is a correction to the scope of
the pairing, not a new result.

### Chapter 20: relative curves and positive representatives

A vertical curve is now characterized as an integral curve mapping to the
closed point of \(\operatorname{Spec}R\); proper horizontal curves are no
longer incorrectly excluded.  The positive-representative proposition now
asserts the cofinal conclusion proved by its argument, rather than ``every
sufficiently high model,'' and its arbitrary-smallness clause is explicitly
restricted to an already semipositive form.  These are scope corrections,
not new results.

### Chapter 21: uniform limits of BFJ psh functions

The stability theorem retains closure of the BFJ psh class under uniform
limits but deletes the false claim that such a limit is automatically
continuous.  Only restrictions to determining dual complexes are continuous
without a separate global continuity hypothesis.  This is a correction, not
a new result.

### Chapter 22: strict semistability and incidence weights

Strict semistability forces the component multiplicities to be one, but in
higher relative dimension it does not force
\(w_{ij}=(E_i\mathbin\cdot E_j\mathbin\cdot\mathcal A^{n-1})\) to be a unit
weight.  The vertex estimate is therefore stated using weighted valence in
general; unit contributions belong to individual nodes of semistable curves.
This is a correction, not a new result.

### Chapter 22: edge length, multiplicity, and slopes

In the segment example, the earlier formula omitted the multiplicity of one
endpoint.  For adjacent components \(F,F'\), with normalized divisorial
parameters \(t_F<t_{F'}\), the correct relation is

\[
 b_Fb_{F'}(F\mathbin\cdot F')=(t_{F'}-t_F)^{-1}.
\]

Accordingly, one first multiplies the nef inequality at \(E_i\) by the
positive number \(b_i\).  The expression

\[
 b_i\sum_{j\ne i}b_j(E_j\mathbin\cdot E_i)(u_j-u_i)
\]

is then the sum of outgoing slopes in the normalized lattice coordinate, and
the reference term is \(b_i d_i\).  The one-node blowup check has exceptional
multiplicity two, strict-transform multiplicities one, intersection number
one, and two edges of length \(1/2\), so both sides equal two.  The final
convexity and boundary inequalities in the displayed semistable example are
unchanged because the original endpoints have multiplicity one and the
inserted exceptional components have reference degree zero by projection.

This is a normalization correction, not a new theorem.

### Chapter 22: the cube of the triangle ideal

The identity

\[
 (xy,yz,zx)^3=((xy)^3,(yz)^3,(zx)^3)
\]

is false: the left side also contains mixed products.  The manuscript now
keeps the full ideal \(\mathfrak a=(xy,yz,zx)^3\).  Its model function is
nevertheless

\[
 \log|\mathfrak a|
 =3\log|(xy,yz,zx)|
 =\max\{3\log|xy|,3\log|yz|,3\log|zx|\},
\]

because a multiplicative non-Archimedean seminorm sends a power of a
finitely generated ideal to the corresponding power of its maximum norm.
Thus all numerical values and gradients in the example remain valid.

This is an algebraic correction, not a new theorem.

### Chapter 30: a fibre of the square map

The earlier measure-theoretic example claimed that the fibre of the
centered monomial point under \(z\mapsto z^2\) contained a second monomial
point obtained by the deck involution.  This is false: the centered Gauss
point is fixed by \(z\mapsto-z\).  The replacement chooses
\(b\in K^\times\) and the two distinct rigid points \(y_+=(z=b)\) and
\(y_-=(z=-b)\), both mapping to \(x=(z=b^2)\).  Thus

\[
 f_*(2\delta_{y_+})=2\delta_x
   =f_*(\delta_{y_+}+\delta_{y_-}).
\]

The revised text explicitly says that this is only a measure-theoretic
example and makes no unsupported assertion that either measure is a
Monge--Ampere measure.  The projection formula itself is unchanged.

This is a correction of an example, not a new theorem.

### Chapter 30: intrinsic vertical divisorial valuations

The birational valuation paragraph had imported the horizontal/trivially
valued dimension count into the vertical discretely valued setting.  If
\(\dim X=n\), a normalized vertical divisorial valuation satisfies

\[
 v_{x_E}(K(X)^\times)=b_E^{-1}\mathbf Z,
 \qquad
 \operatorname{trdeg}_k\widetilde{K(X)}_{x_E}=n,
 \qquad
 v_{x_E}(\varpi)=1.
\]

Thus the residual transcendence degree is \(n\), not \(n-1\), and
\(b_E\) cannot be recovered as \(v_{x_E}(\varpi)^{-1}\).  It is recovered
intrinsically as the finite index of the base value group \(\mathbf Z\) in
the full value group \(b_E^{-1}\mathbf Z\).  The birational invariance
statement remains valid after this correction.

### Chapter 31: direction of the toric measure and logistic substitution

The logistic density is a measure on the real toric skeleton and must be
pushed into the analytification:

\[
 \operatorname{MA}_L(F)=\iota_*(p(1-p)\,\mathrm d u),
\]

not written as the undefined pullback \(\operatorname{trop}^*\) of a
measure.  Since \(p=-F'\), one has
\(\mathrm d p=-F''\,\mathrm d u\), and \(p\) decreases from one to zero.
The mass computation is therefore
\(\int_{\mathbf R}F''\,\mathrm d u=-\int_1^0\mathrm d p=1\).

Both changes are normalization corrections, not new results.

### Chapter 26: nonpluripolar layers and mixed products

The earlier proof incorrectly called \(\{\varphi>-t\}\) open merely from
upper semicontinuity.  Such a strict superlevel set is Borel but need not be
open.  The corrected proof uses the exact bounded maximum principle:

\[
 \varphi^{\langle t\rangle}
 =\max\{\varphi^{\langle s\rangle},-t\},
 \qquad
 \{\varphi^{\langle s\rangle}>-t\}=\{\varphi>-t\},
\]

for \(s\geq t\).  This gives layer consistency directly on the Borel set.
The mixed version is proved by polarizing the bounded maximum principle and
then replacing the truncated entries one at a time.  The former
multilinearity argument also relied on the false openness assertion; it has
been replaced by bounded multilinearity followed by the already proved
monotone continuity of finite-energy mixed products.  Finally, the Radon
property of the increasing limit is now proved by compact approximation from
one sufficiently advanced Radon layer, rather than by an invalid domination
sentence.

These are repairs of the standard BFJ nonpluripolar construction, not new
results.

### Chapter 27: leaving the finite-energy class

An example previously treated
\([E((1-t)\varphi)-E(\varphi)]/t\) as \(+\infty\) when
\(E(\varphi)=-\infty\), asserted without proof that every scaled potential
remained outside \(\mathcal E^1\), and tried to infer divergence of the
integral by reading a one-way tail theorem backwards.  All three steps were
invalid.  The rewritten example states only the correct obstruction: the
endpoint energy is \(-\infty\), so the difference quotient is not defined
under the book's extended-real protocol; scaling can improve a singularity
and must be decided case by case; and the nonpluripolar measure may have
sub-full mass, so no finite-energy derivative formula is available.

This is a correction of an example, not a new theorem.

### Chapter 21: support and residue data

The toroidal example no longer says that every skeleton point has residue
field of positive transcendence degree.  A (K)-rational analytic point has
nonzero schematic support, while a skeleton point is represented by a
valuation of (K(X)) and therefore has zero support.  This separates the
support criterion from residual-transcendence statements.

### Chapters 23--25: convex envelopes, density, and curve capacity

The convex-envelope orthogonality theorem is now stated on a compact convex
body and proved on its interior.  Compactness makes the barycentric minimum
attainable and permits boundary contact points; the former open-domain proof
could have an empty contact set.  A generally nonopen skeletal tube is now
called Borel.  The dense-test lemma allows its strictly positive auxiliary
potential to depend on the model carrying the test function, since pullback
of an ample class to a blowup need only be nef.  Countable polar nullity is
deduced directly from countable subadditivity.

On a curve, arbitrary real breakpoints in the segment-capacity maximizers
are handled by uniform rational model approximation; rational attainment is
claimed only for rational data.  The length-four example is a chain of four
ordinary semistable edges, not a nonexistent regular node of thickness four.
Thuillier's equilibrium potential is corrected to
(g=-(\log r)u).  These changes repair proofs and examples; they introduce
no new theorem.

### Chapter 26: the vertical-factor energy formula

The model energy is no longer written as a difference of two undefined
absolute powers of closed model forms.  Its algebraic formula is

\[
 E_\omega(\varphi)=\frac1{n+1}\sum_{j=0}^n
 (D_\varphi\cdot\omega_\varphi^j\cdot\omega^{n-j}),
\]

and the energy difference uses the corresponding divisor
(D_{\psi-\varphi}).  Every term has the vertical first slot required by
BFJ15 Section 2.7.  Cocycle, variation, reference change, and the dictionary
have been rewritten with this legitimate mixed vertical sum.  This is a
normalization/domain correction, not a new result.

The proof of the difference formula was then tightened once more.  A formal
polynomial shorthand in closed model forms does not by itself remember the
constant part of a model function: the special fibre represents the constant
one while its \(\mathrm d\mathrm d^c\)-class is zero.  The final proof keeps
\(u=\psi-\varphi\) as an actual function, differentiates the finite
model-energy sum along
\(\varphi_t=\varphi+t(\psi-\varphi)\), uses model integration by parts, and
integrates the binomial expansion with
\[
 \binom nk\int_0^1t^k(1-t)^{n-k}\,\mathrm dt=\frac1{n+1}.
\]
It therefore proves the mixed vertical difference formula including
constant potentials, without invoking an undefined absolute power.  This is
a proof repair, not a new result.

### Chapters 28--29: variational domain and the borderline exponent

The Calabi--Yau summary now assumes that the tested potential belongs to the
effective domain of (F_\mu), calls decreasing-net continuity monotone
continuity rather than arbitrary strong-topology continuity, and corrects
the Fenchel rearrangement to

\[
 E_\omega(\varphi)-E_\omega^\vee(\MA_\omega\varphi)
 =\int\varphi\,\MA_\omega(\varphi).
\]

Finite dual energy already forces integrability of every
(\mathcal E^1) potential by applying the bounded-test formula to
truncations.  The warning about vanishing (J\) now distinguishes the
elementary nef-intersection argument from the imported uniqueness theorem.
The exponent-zero example now proves the global inequality
(\mu(E)\leq\operatorname{Cap}_\omega(E)) for every Borel set, rather than
checking only one tail family.  These are corrections and completions of
existing arguments.

### Chapters 30--31: pullback scope, supports, and toric examples

Singular pullback is stated only when the pulled-back generic class remains
ample and the image is not contained in the polar set.  Birational pullback
retains model and continuous projection formulae, but no singular theorem
is asserted in the merely nef-and-big class.  Support containment in the
zero-support locus and supportwise bijectivity are restricted to model
measures; weak limits can acquire additional topological support.  The
standard section metric sign, the non-geometrically-integral base-change
decomposition, and the uniqueness citation in Galois descent were also
corrected.  The surface energy and Gauss comparison now use vertical-factor
mixed sums only.

The toric mixed formula explicitly includes nef line bundles whose sum is
ample, covering the \(\mathcal O(1,0),\mathcal O(0,1)\) example.  A
quadratic Tate canonical weight is never made model by finite subdivision;
its decreasing model approximation is taken along nested dyadic
subdivisions.  General continuous comparison no longer asserts existence of
a delta-form product outside the delta-metric locus.  These are scope and
example corrections, not new results.

A subsequent whole-book terminology scan repaired the Chapter 31 curve row:
Wanner identifies current positivity with Thuillier subharmonicity, not with
the manuscript's approximation-generated CLD hierarchy.  The row now records
the BFJ-to-current-positive implication and makes the reverse passage into
the CLD hierarchy conditional on the separate smooth-regularization
hypotheses.

## Source checks completed

- The exact sequence for the model differential in Chapter 20 matches the
  fixed-model exact sequence and the Kunnemann reduction used in BFJ's
  theorem on closed model forms.  The reconstruction of a numerically
  trivial generic-fibre line bundle is source-aligned: after finite extension
  it is represented by a family over a curve, and a degree-zero divisor on
  that curve supplies the vertical correction through the Chow cap product.
- The finite-energy uniqueness statement in Chapter 29 is exactly the scope
  of BFJ Proposition 8.2: two finite-energy potentials with the same
  Monge--Ampere measure differ by a constant.  The manuscript correctly
  presents this as an imported theorem and does not derive it from the
  strictly ample model equality case alone.
- The capacity definition and its continuity properties in Chapter 25 agree
  with the BFJ construction.  The manuscript deliberately does not claim
  strong subadditivity or analytic capacitability without a separate input.

## Outstanding checks

- Independent high-scrutiny audits of Chapters 20--25 and Chapters 26--31
  have been integrated.
- A 773-page focused build of Chapter 12 followed by Chapters 20--31 succeeds
  with no undefined control sequence, LaTeX error, overfull box, or fatal
  error.  The tropicalization operator has since been moved to the global
  notation file, so focused builds no longer depend on Chapter 12 for that
  macro.
- Full static reference/citation checks, a clean whole-book build, and
  representative visual inspection remain to be run after the simultaneous
  Part II and Part IV audits finish.
- Any genuinely new statement surviving the audit remains quarantined until
  its exact final statement and proof pass the production Rethlas gate.
