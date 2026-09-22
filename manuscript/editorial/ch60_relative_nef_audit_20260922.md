# Chapter 60: relative numerical nefness — 22 September 2026

## Scope and sources

This revision fills in the numerical reduction in
`thm:mp-model-closedness`. It does not change that imported theorem, promote
a new research result, or change the active problem inventory.

The published primary source checked was Demailly–Păun, *Annals of
Mathematics* 159 (2004), 1247–1274, DOI
[10.4007/annals.2004.159.1247](https://doi.org/10.4007/annals.2004.159.1247).
The [journal PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf)
provides the following exact dependencies:

- Theorem 4.3(iii), p. 1267: linear intersection tests against every Kähler
  class characterize nefness on a compact Kähler manifold.
- Proposition 3.3(i)–(ii), p. 1262: extension of positivity to an ambient
  neighbourhood and gluing on finite unions of analytic subsets.
- Theorem 0.1, p. 1248: the connected-component characterization of the
  Kähler cone.
- Equation (4.4) and its polynomial-pairing proof, pp. 1267–1268.

Mesquita-Piccione's [arXiv:2409.06221v2, Theorem 4.1.5](https://arxiv.org/html/2409.06221v2)
was checked directly for the divisorial-net statement and its cycle/current
argument. The publisher record confirms *Advances in Mathematics* 481
(2025), 110543, already present in `MP24`. The publisher's full text was
not available during this audit. The revised proof therefore explicitly
identifies arXiv version 2 as the version whose theorem number was checked.
No published locator is asserted on the strength of a preprint alone.

## Mathematical checks

The previous bare reference to a numerical criterion omitted the distinction
between Kähler classes on a central component and on the total space. The
new argument uses only the latter, as the imported theorem does.

For a class Kähler on each reduced fibre, local positive representatives
are patched using weights pulled back from the base. The error terms vanish
on the vertical tangent kernel. Adding a sufficiently large multiple of
the pullback of a base Kähler form then gives total-space positivity, by
compactness of the unit tangent bundle. This argument also covers critical
points of the model morphism.

Starting with `beta + a Omega` positive on every fibre, the proof produces
ambient Kähler test classes `s beta + a Omega + C_a eta`. The base term
restricts to zero on every central cycle. The polynomial identity and
connected-component criterion reduce `a` by a factor `1-delta_0`, uniformly
in all iterations and dimensions `1,...,n`. The constants `C_a` may vary.
Taking `a` to zero proves relative nefness. The zero-dimensional case is
handled separately. This is a reconstruction of the omitted reduction,
not a new regularization theorem.

**Normalization correction.** As printed, the sentence after (4.4') says
`A_p(t,0)=1`; with the displayed (4.4), the correct value is `p`. For
example, in degree 2, an integrand coefficient 1 gives only half of
`y^2-x^2`. The book factors out `d`, uses `B_d(s,0)=1`, and proves the
normalization by polynomial pairing and the fundamental theorem of calculus.
Equivalently, its coefficients are uniquely determined by
`integral_0^1 B_d(s,delta) s^j ds = (1-delta)^(d-1-j)/(j+1)`.
An exact rational-arithmetic check of these moments in dimensions 1–5
confirms the displayed identity and its normalization; the all-dimensional
argument is in the text and does not rely on that finite check.

The final analytic-cycle paragraph stays explicitly imported. It now says
that the exceptional current's **pushforward** is a positive multiple of
the cycle, and that its intersection expression is affine in finitely many
divisorial values: the fixed background class supplies the constant term.
No common model for the entire net is assumed.

## Validation and remaining limits

- Baseline scoped Chapter 60 build: 82 pages, two unresolved occurrences
  of an external Chapter 71 label, and one 4.25891 pt overfull display.
- Second-pass scoped build: 84 pages, the same two external-reference
  occurrences, no unresolved citation, and no overfull box. The old energy
  display was split into two aligned lines without changing its mathematics.
- The revised proof passes the strict writing audit with zero errors and
  zero warnings. The bibliography-aware house audit requests a BibLaTeX
  `label` field for `MP24`; this book uses its existing BibTeX style, which
  already renders the correct compound-name label `MP25`. No unrelated
  bibliography migration was made. Both cited keys resolve.
- Physical pages 58–61 and 66–67 of the final scoped PDF were rendered
  and inspected. The proof, the neighbouring transitions, and the repaired
  energy display have no clipping or overlap.
- Second reading checked the vertical gluing, the positive base correction,
  the uniform shrinking parameter, all cycle dimensions, the zero-dimensional
  exception, and the imported-core boundary.
- The source check still reports the same missing Chapter 70 input and
  thirteen unresolved file/label pairs: 388 available files, 11,428 labels,
  no duplicates or structural defects. No full-book success is claimed.
- The inventory check passes: 46 active atoms, 14 formal problem
  environments, tiers `(0,5,8,16,17)`.

At the end of this numerical-criterion revision, the model-independence
lemma still required a separate descent audit. That follow-up is recorded
next.

## Follow-up: model independence and terminology

The proof of `lem:mp-relative-nef-independent` now supplies the descent
argument on smooth snc models. Given a cycle downstairs, it chooses a
component of its full inverse image that dominates it and then an embedded
resolution. A Kähler form upstairs, raised to the relative dimension,
pushes forward to a strictly positive multiple of the cycle. The projection
formula transfers nonnegativity to every Kähler test class on the smooth
central component. Demailly–Păun Theorem 4.3(iii) and Proposition 3.3(ii)
then give fibrewise nefness. This also covers cycles inside the exceptional
image, for which a strict-transform argument would be invalid.

The proof explicitly separates the general normal-model assertion imported
from `MP24`, Definition 4.1.2 in arXiv version 2, from the direct snc proof.
It does not claim that a smooth positive representative pushes down smoothly,
or that the direct argument establishes a numerical criterion on every
singular compact space. Păun's 1998 paper was located bibliographically but
its full text was not available; no uninspected theorem locator was added.

The second reading checked equality of divisor coefficients on a common
model, existence of a dominating inverse-image component, Kähler embedded
resolution, the current's bidimension, positivity of its scalar coefficient,
the case of equal dimensions, and zero-dimensional fibres. The strict
writing audit passes. The final scoped build remains 84 pages with no
overfull box or unresolved citation and the same two external-reference
occurrences. Physical pages 56–59 were rendered; the changed introduction,
proof, and transitions were inspected without clipping or overlap. The
source check retains exactly the pre-existing Chapter 70 failure.

The introduction now says that a general Kähler class need not be a
line-bundle class, replacing the false assertion that there need be no
line bundle at all. Fixed-background psh sets are called classes rather
than cones. The separate Fubini–Study warning still needs a model-category
and rationality audit; it is not validated by this descent proof.

## Follow-up: Fubini--Study comparisons

The warning `warn:mp-h-not-fs` no longer asserts a blanket strict inclusion
from the absence of a line bundle. For a smooth projective algebraic model,
an ample rational polarization and a rational vertical Cartier divisor
produce an actual line bundle after clearing denominators. Relative Kähler
positivity then gives fibrewise ampleness by Nakai--Moishezon and relative
ampleness by the fibre criterion. This is a statement about the specified
algebraic model, not an algebraization theorem for all analytic models.

The published [Boucksom--Jonsson PDF](https://afst.centre-mersenne.org/item/10.5802/afst.1705.pdf)
was checked at Corollary 2.32 (p. 686), Definition 3.8 and Example 3.9
(p. 694). These identify the algebraic Fubini--Study locus with ample,
integrally closed test configurations, and distinguish its sublocus whose
ample model dominates the trivial model. The warning now records that
distinction and explains why passage to a common resolution cannot be used
to identify the strictly positive loci: it preserves nefness but can lose
ampleness. No equality or strict containment for the unrestricted analytic
Kähler model locus is asserted by this revision.

[Stacks Tag 0D2S](https://stacks.math.columbia.edu/tag/0D2S), checked on
22 September 2026, is the proper-morphism fibre criterion actually used.
Appendix I now records its hypotheses, first use, and algebraic scope.
The definition of `H(alpha)` explicitly permits some normal model; it does
not require positivity to survive every snc refinement.

The full MP--BJ psh comparison is in **Chapter 71**, not Chapter 69; the
earlier audit and continuation note have been corrected. That comparison
uses common-model nefness and decreasing completions. Its frozen text,
including its historical discussion of MP24 Remark 4.1.3, was not changed
or newly certified. The Chapter 71 file's SHA-256 is unchanged:
`05ce1967cb4d083613bcb72dae1c23ebbc60156840f9fa3555caba32d85ad634`.

Validation:

- The second reading checked rational denominators, the line-bundle class,
  properness, the fibrewise criterion, the dominance condition, and the
  distinction between nef and strictly positive representatives.
- The scoped Chapter 60 build is 84 pages with no overfull box or
  unresolved citation. The newly added pointer gives three occurrences
  of the existing external Chapter 71 reference, rather than the baseline
  two. That label exists in the full source graph.
- The Appendix I scoped baseline has 79 pages; the revised scoped build
  has 81 pages. Both have no overfull box, unresolved reference or citation.
  These diagnostic drivers are not complete-book releases.
- The strict writing audit of the new warning and appendix entry has zero
  errors and one reviewed warning: the existing `warn:` label prefix is
  outside the house audit's list. The established label is preserved.
- The new warning, appendix dependency entry and table were rendered and
  inspected (physical pages 58 of the Chapter 60 driver and 61, 67 of the
  appendix driver). The existing compact table's close column spacing is
  a separate layout follow-up.
- The source check retains the one missing Chapter 70 input and thirteen
  unresolved file/label pairs, with 388 available files and 11,428 labels.
  The open-problem inventory and whitespace check pass.


## Appendix I layout follow-up

The compact dependency ledger now uses a text table with explicit column
widths and spacing, rather than a mathematical array. All 21 entries,
their order, wording, and chapter references were compared with the prior
version and preserved. Tags now print as upright text. The table has
repeated headings available if a future revision requires a page break.

The second layout pass keeps all 21 rows on one page at the book's small
text size, with a visible gap between the longest description and its
chapter reference. The final scoped build remains 81 pages with no
unresolved reference, citation, or overfull box. The strict audit has zero
errors or warnings, the whitespace check passes, and physical page 67
was rendered and inspected after the final adjustment. The following
paragraph is also clear of the table. No dependency statement was changed.

## Follow-up: maxima of relatively nef model functions

The maximum assertion in `prop:mp-model-psh-stability` retains the scope
of MP24 Proposition 4.1.4. Its proof now states the ideal and supplies the
approximation argument, rather than only referring to relatively Kähler
approximants.

On a common snc model, clearing denominators and a common integral shift
give effective Cartier divisors `F=m(c X_0-D)` and `G=m(c X_0-E)`.
Principalize `O(-F)+O(-G)=O(-H)` on one fixed higher model. The maximum
is represented by `c Y_0-H/m`. The sign can already be checked for
the constant functions 0 and 1: the ideal is `(t)+O=O`, so the maximum
is represented by the central fibre and equals 1.

For each positive epsilon, a small ambient Kähler perturbation and a
sufficiently large base correction make both shifted divisor classes
positive. Maxima of their logarithmic canonical-section norms have the
singularity type of the sum ideal. On the fixed resolution, the residual
potential is locally bounded because the residual generators have no
common zero. The regularization input is explicitly imported from
[MP24 Proposition 5.0.1, arXiv version 2](https://arxiv.org/html/2409.06221v2),
whose statement and proof were checked. Restriction to central components
kills the base correction before epsilon tends to zero. No uniform bound
on that correction is asserted or needed.

This writes out the canonical-section argument also for reducible and
zero effective Cartier divisors; it does not apply the source's Lemma
5.0.2 beyond its stated irreducible-divisor wording without explanation.
The model, the resolved ideal and the representing divisor stay fixed in
the limit. Equal inputs and the unit-ideal case satisfy the same argument.

The previously written relative Kähler gluing argument has been extracted
as `lem:mp-relative-kahler-extension`, before the stability proposition.
Both the maximum proof and the numerical nefness reduction invoke this
lemma. Its proof uses DP04 Proposition 3.3(i)--(ii), a partition of unity
on the base and compactness of the unit tangent bundle. Thus the maximum
proof no longer requires the later divisorial closedness theorem, and the
closedness theorem does not depend on the maximum argument. This is an
expository reorganization of existing sourced mathematics; no open problem
is promoted or retired.

The automatic second pass checked the signs, denominators, fixed-model
limit, positivity of the common background class, adjustable Hermitian
metrics, the zero-divisor case, and this dependency order. The revised
lemma and proof pass the strict writing audit with zero errors or warnings.
The final scoped Chapter 60 build has 85 pages, no overfull box or unresolved
citation, and the same three occurrences of the external Chapter 71
reference. Physical pages 58--61 were rendered and inspected after the
final edit. Shortening the preceding warning's last sentence also keeps
its closing rule on the page with its text.

The source closure now has 11,429 labels, including the new lemma, with
no duplicate or structural defect. The same single Chapter 70 input and
thirteen file/label pairs remain missing. The exact problem inventory
and whitespace checks pass; the Chapter 71 file hash is unchanged.
