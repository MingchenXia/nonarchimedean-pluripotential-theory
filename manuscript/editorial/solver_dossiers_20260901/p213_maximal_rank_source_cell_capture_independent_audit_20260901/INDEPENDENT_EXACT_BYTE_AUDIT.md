# Independent exact-byte audit: maximal-rank source-cell capture

Date: 1 September 2026. Reviewer: /root/p081_weighted_repair_fresh.
Candidate author: /root/p082_independent_reaudit.

## 1. Verdict and independence

PASS for the full stated geometric capture result. No substantive gap or
required correction was found. The optional normalized-coefficient conclusion
is valid conditional on the explicitly stated source representation R and
the specified common-moment comparison. R is not proved or independently
certified by this audit.

The existence assertion is for smooth proper integral algebraic X over the
original complete DVR in residue characteristic zero. It preserves the
specified rational functions' common algebraic unit-open U. The generic
map may be birational, not an isomorphism outside U. The rank argument
after an adapted model is supplied does not use characteristic zero.
No field extension, current extension or non-isomorphic current pullback
is involved on W.

I read the entire frozen note, source ledger, author validation and manifest,
checked the primary interfaces described below, and re-read the complete
optional common-moment note to verify its conditional role. I did not author
or supply the finite affine-subspace argument. I previously audited related
common-moment and model-adaptation packets; those verdicts are not a
substitute for this new review. I authored the separate nearby-wall
construction, which is NOT a premise of the capture note and is not
self-certified by this audit.

Independent review is not production acceptance, integration authorization
or a P21.3 conclusion. Candidate, predecessor and live bytes are unchanged.

## 2. Exact input identity

Candidate directory:

/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_maximal_rank_source_cell_capture_research_20260901

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| RESEARCH_NOTE.md | 19244 | 4cc25ff627af56aca05c8733e3e5bff65aea21015abe35e49726f9966bb1b384 |
| SOURCE_LEDGER.md | 5606 | cb4df5336a983b058d55b25c1dd4ec68e82d3ef155785e2bb59f3ed8281413b4 |
| VALIDATION.json | 2803 | 37bc6cce6d3ba6a363bcaae72d265a9e0ca6b66a4beeef39c929b93cebfc1a59 |
| MANIFEST.json | 5755 | 52b8f6a75dda7caca6d3449a4e5e969f3abd3f4a6800cb9cf6bc091230713265 |
| SHA256SUMS | 2772 | 3f6f3de6b1dd631260d47c3dcfd28d2fef05f055458fba3e186baf067d15efb8 |

The author confirmed these frozen pins. The independent read-only verifier
matched all four announced hashes, all 13 candidate manifest entries and
14 candidate checksums. It also matched all 12/13 common-moment predecessor
entries/checksums and all 23/24 model-adaptation predecessor entries/checksums.
The five candidate files have no forbidden control bytes; the note has
11 distinct equation tags. INPUT_CHECKS.json records the completed run.

## 3. Rational replacement and actual compact source supports

Section 2 is correct over the stated original field. For an algebraic
analytification, the residue field of the underlying scheme point is
dense in the completed analytic residue field. A strict approximation
to a nonzero analytic value can therefore be represented by a rational
function with denominator nonvanishing at the point. Both the analytic
unit and that representative are defined on an ordinary neighbourhood.
Continuity preserves the strict inequality after shrinking, and the
ultrametric inequality gives exact equality of norms there.

This does not claim equality of the analytic functions or a global
algebraization. A representative is a rational function on the integral
X, and after shrinking its zero/pole support is avoided, so it really
belongs to a common algebraic unit-open locus of the stated kind.
Doing this for a finite tuple gives equality of the entire tropical
maps on the ordinary neighbourhood, not just equality at one point.
Consequently their pullback forms and maximal-variation sets there agree.

The finite compact-support reduction is legitimate. Good separated
algebraic analytifications are locally holomorphically separated, so
CLD Corollary 15.2.5 supplies compact smooth cutoffs inside the chosen
ordinary opens. Taking nonnegative cutoffs whose sum is positive near
the original compact support, followed by the displayed eta/H
normalization, gives a finite partition there. The extra eta has compact
support inside {H>0}, so division and zero extension are smooth. Every
resulting test has actual compact source support inside its own open.
There is no conversion of a formal or G-open cover into an ordinary one.

## 4. Model existence, exact preservation of U and divisor monomials

Section 3 passes, including the nonprojective proper case.

Since K=R[1/pi], X is separated and of finite type over R. Nagata
compactification applies to Spec(R). Taking the reduced closure of the
integral open X gives an integral proper model. Its generic fibre is
exactly X: the given open immersion into a separated generic fibre is
also closed because X is proper over K. Torsion-free over the DVR gives
flatness. Finite type over the complete noetherian base gives excellence.

Residue characteristic zero makes R a Q-algebra. Temkin Theorem 1.1.6
with empty boundary gives a regular model while leaving its original
regular locus, in particular the whole smooth generic fibre, unchanged.
On this regular model each special-fibre component and each closure of
a prime zero/pole divisor is Cartier locally. There are finitely many.
They can be put in any fixed order to make the divisorial boundary
required by Temkin Theorem 1.1.3.

That theorem's centers lie over the ORIGINAL non-SNC locus of the
boundary, not merely in some unspecified birational exceptional locus.
The boundary complement is therefore unchanged. Its generic part
contains U. The output remains regular and its total boundary support
is SNC. No assertion that all intermediate boundaries are SNC is needed;
Temkin explicitly warns otherwise.

The equality of generic horizontal boundary support with the inverse
image of X minus U is also justified. The total transform contains the
inverse image of every initial horizontal zero/pole support. Every
new generic exceptional divisor maps to that support, since the
generic centers lie above the initial bad boundary. The support identity
for complete transforms in Temkin Lemma 2.2.9(iv) prevents the introduction
of an unrelated generic boundary component. The first empty-boundary
regularization introduced only vertical exceptional components. Thus
the identification over U is exact, not merely generically an isomorphism.

On the final regular model, factoriality of each local ring implies
that the rational f_i divided by its indicated parameter monomial is
a LOCAL UNIT: all its height-one orders vanish. This is stronger than
knowing its divisor at a single component. It justifies both (4.2) and
the entire-tube identity (5.2). Extra boundary components with zero
order for some or all f_i cause no error; they remain in the finite
matrix data with zero entries. The vertical multiplicities are retained.

## 5. The finite affine rank argument

Sections 4-5 contain the central new step and pass as written.

At every source point over U, properness gives an actual center y.
Every boundary parameter through y has strictly positive value. These
values are finite: vertical ones are nonzero because pi is nonzero,
and horizontal ones are nonzero because the generic horizontal boundary
is exactly the excluded inverse image of X minus U. A unit of the local
ring and its inverse belong to the valuation ring at that center, so
both have norm at most one and the unit has value zero. Thus

\[
       F(x)=M_I\beta,\qquad N_I\beta=\ell
\]

holds at EVERY indicated source point, including points not yet known
to have generic algebraic support or to be monomial.

There are finitely many boundary index sets I. Their affine image spaces
H_I in (4.3) depend only on the global integer divisor orders and ell,
not on a chosen local unit. Their dimensions are at most |I|-1. Hence,
outside the specified finite union E of spaces of dimension below n,
the realized H_I must have dimension n. Strict SNC and model dimension
give |I|<=n+1, so |I|=n+1 and the center has maximal local dimension.
It is a closed point of the special fibre, and its residue field is
finite over k. The restriction of M_I to ker(N_I) has equal source
and image dimension n and is injective.

An affine injective map from a compact n-cell preserves dimensions of
its PL subsets. Therefore the preimages of these finitely many lower
affine subspaces, together with the cell boundary, form the asserted
closed PL subset Z_C of dimension below n. A finite union of proper
affine subspaces cannot cover an n-dimensional relatively open set.
The complement is dense. This does not discard a full-dimensional
rank-drop cell belonging to a different, enlarged moment; the model
and finite matrices here were built for one fixed rational tuple.

At the resulting maximal stratum p, all n+1 local boundary equations
and the local model units are defined on the entire ordinary p-tube.
The chosen vertical equation has positive N_0. Eliminating its value
gives precisely (5.2), with the displayed rational matrix A_p and
rational ell-translation. The rank is n because this elimination
parametrizes the affine hyperplane N_I.beta=ell whose direction has
already been checked injective under M_I.

The punctured p-tube excludes all horizontal zero loci and is an ordinary
open subset of the preserved unit-open analytification. The exact
identity F=A_p q+b_p holds there, not only on a candidate skeleton.
An injective affine change leaves local tropical dimension unchanged
on every ordinary restriction. CLD Lemma 12.9.2(a) therefore gives
the literal equality of maximal-variation SOURCE sets for F, q and
(F,q) on W intersect D_p. The statement is about maximal variation,
not an unqualified characteristic-skeleton identity on arbitrary
domains with boundary.

For x off Z_C, the trace of this ordinary open on the chosen C is a
relatively open n-dimensional patch. The left inverse of A_p makes
q affine and injective on it. A smaller compact polytope can be chosen
around x in this trace. This is an actual shared source patch. For
coefficient isolation, any additionally chosen coefficient-presentation
boundaries must still be avoided/refined, as Section 5 explicitly says;
the finite rank exception is not advertised as already encoding every
future presentation boundary.

## 6. Independence and the finite monomial characterization

Section 6 passes in its precise claimed form.

Choose n rows of F whose linear parts are independent on the patch.
Their n values have an open image in R^n. The exclusions for rational
dependence together with ell are proper affine hyperplanes: a relation
with all n variable coefficients zero cannot vanish, since ell>0.
Their countable union has dense complement. The matrix with these n
rows of M_I and the row N_I is invertible over Q, so this condition
is exactly Q-independence of the n+1 normal weights beta.

The finite regular-local expansion is enough to characterize such a
point without assuming generic support in advance. A nonzero element
has finite maximal-ideal order by Krull intersection. The regular
associated graded ring provides finitely many unit residue lifts and
an exact degree-M remainder with coefficients in the local ring.
Independence makes the retained values distinct, and
M min(beta)>d max(beta) puts the remainder above the unique least
retained value. The nonnegative values of remainder coefficients
are sufficient, even when some are killed by the semivaluation.
Strict dominance forces a finite value for every nonzero local
element. This proves injectivity/generic support and uniqueness
on the fraction field in the intended direction.

The countable independent subfamily is not confused with the finite
PL exceptional locus. The proof makes no unproved assertion about
all dependent points being ordinary covering sheets.

## 7. Optional R comparison and a downstream interface clarification

The geometric capture does not use R, L, V, O or a nearby-wall theorem.
Section 7's coefficient statement separately assumes R with arbitrary
compact ordinary source multipliers and no residual lower-cell term.
On the ordinary domain in question, the concatenated moment has the
same source set and both projections have rank n. The generic
common-moment argument can therefore be applied after the indicated
presentation refinement. Its determinant factor is the same for the
arbitrary current and the canonical calibration, so their normalized
ratios agree. Source cutoffs are chosen compactly INSIDE W intersect
D_p. This does not apply a whole-tube coefficient to a current defined
only on that smaller open, and does not extend the current by zero.

One clarification should be retained when assembling a later theorem.
This note proves a coordinate-source patch and identifies a dense
independent subfamily by a monomial rule. A later use of a theorem
about an entire continuously embedded MODEL cell should explicitly
state the short continuity bridge, rather than silently identify
different skeleton definitions. On a small compact q-patch, q is an
affine homeomorphism. In residue characteristic zero the local
weighted-series model embedding is continuous. Its inverse-coordinate
map and this source-patch inverse agree on the dense independent
normal values by Section 6. Since the analytic space is Hausdorff,
they agree on that compact patch by continuity. This is a downstream
interface explanation, not a required repair of the capture statement,
and does not independently accept the reviewer's separate nearby-wall
candidate.

No claim of a whole proper inverse target box inside W, a common
constant across all coordinate patches, arbitrary-field/nonalgebraic
capture, or T=c times canonical integration follows from this packet
alone. Those exclusions are genuine, not merely editorial gates.

## 8. Source and preservation conclusion

The exact primary interfaces and visual limitations are recorded in
SOURCE_INTERFACE_CHECK.md and SOURCE_QA.json. The eight relevant CLD
pages were viewed completely; their render exited zero without warnings.
The remote Temkin theorem and definition text was read, but the page-3
web screenshot failed; no Temkin visual verification or local file hash
is claimed. Only exclusively owned source-render PNGs were removed.

No mathematical revision is requested. The exact candidate remains
frozen. This audit supplies a full-scope independent geometric PASS
and a conditional PASS for the optional R consequence, not production
acceptance or a current-rigidity solution.
