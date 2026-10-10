# Cyclic toric models: primary-source and scope check

Date: 4 October 2026. This continues the related-paper reading after the
BJ22 Siu proof correction. The new Chapter 5 example uses the known
cyclic quotient `1/15(1,2,4,8)` and direct finite lattice calculations.
It does not use an unresolved two-parameter classification proof or
claim a new general result.

## Controlling source for the positive example

Kohei Sato and Yusuke Sato, *Crepant Property of Fujiki-Oka Resolutions
for Gorenstein Abelian Quotient Singularities*,
[arXiv:2004.03522v4](https://arxiv.org/abs/2004.03522v4), revised
10 September 2020, is the controlling version. The author/title/version
are visible on its actual first page. The arXiv abstract page's current
submission history lists versions 1–4, with version 4 last at the time
of the 4 October lookup. This is a bounded version check, not a complete
search for later published results.

Theorem 3.1, physical page 9, concerns the **Fujiki–Oka resolution
procedure** for a cyclic type `1/r(1,a_2,...,a_n)`: it is crepant iff all
coefficients of its remainder polynomial have age one. The complete
displayed proof on physical page 10 was read. Definitions 2.8–2.12
on physical page 6 specify proper fractions, least residues, the
noncommutative word order and the excluded infinity/zero terms.
The Oka-centre and lower-order quotient interpretations on pages 7–8
were checked at their exact source scope. Ashikaga, Fujiki and Oka's
original antecedents have not all been freshly audited.

Example 3.10, physical page 12, gives `1/15(1,2,4,8)` and its eight
remainder terms, all of age one. The published-in-preprint positive case
is the source of the worked example. The book additionally specifies
one actual fan and its rational coherent lifting, so its local-model
calculation is inspectable without treating the general algorithmic
criterion as an oracle.

All nine selected actual pages 1 and 5–12 of version 4 were viewed.
One actual page 11 of version 3 was also viewed. The ten pages are
accounted for in five contact sheets. There is no whole-paper actual
visual claim. Fresh extracted-text coverage for version 4 is lines
1–108, 242–620 and 663–750; version 3 includes lines 653–735. The
first version's standing scope and original sufficient theorem were
read at lines 1–195 and 479–592, without a whole-version review.

## The toric obstruction and accurate locator attribution

Proposition 3.9 in both version 3 and version 4 explicitly excludes
**toric** crepant resolutions when an iterated remainder coefficient
has age at least two. It is not cited here as a nontoric obstruction.
Nor is a failure of an arbitrary resolution procedure equated with the
nonexistence of every possible resolution.

Yusuke Sato's [arXiv:2007.00504v1](https://arxiv.org/abs/2007.00504v1),
*Existence of Crepant Resolutions for Two-Parameter Gorenstein Cyclic
Quotient Singularities*, was cumulatively read in its full 489 extracted
lines and all six actual pages. Its Theorem 3.2 combines citations to
Sato–Sato Theorem 3.1 and Proposition 3.9. Theorem 3.2 is its own
number, not an incorrect locator for a Sato–Sato Theorem 3.2. An initial
commentary conflated these sources; that observation was corrected
before any book or bibliographic edit.

The single-author text drops the word “toric” in its paraphrase of the
negative conclusion. This audit retains the controlling antecedent's
scope. Its repeated-coordinate Lemma 3.4 also requires allowance for
zero coordinates and trivial factors: its own `1/15(1,2,6,6)` example
has `R_2=(1,1,0,0)/2`. The positive and negative tests in that family
do not license rescaling a generator while discarding its normalized
age-one hypothesis. Its coprime continued-fraction Theorem 3.6 imports
earlier classification and does not display an independent proof of
every direction. The unsuccessful earlier current-version metadata
lookup is preserved as a failure, not a latest-version clearance.

## Earlier two-parameter classification: completed reading scope

Dais, Haus and Henk's Results Math. 33 (1998), 208–265, DOI
[10.1007/BF03322085](https://doi.org/10.1007/BF03322085), has separately
checked bibliographic metadata. The controlling proof file actually
acquired here is its [arXiv:math/9803096v1](https://arxiv.org/abs/math/9803096v1)
preprint, not the final journal PDF. The publisher response was HTML;
it supplies no fresh journal-proof clearance.

Theorem 5.13, physical page 26 of the preprint, treats a Gorenstein
cyclic msc-singularity of dimension `r>=4`, order `l>=r`, with at
least `r-2` equal weights. It equates the junior Hilbert-basis condition
with a full crepant torus-equivariant resolution and claims a projective
one exists. Its geometric proof is in Section 6, pages 29–35. Theorem
5.15, pages 27–28, gives a more restrictive arithmetic parametrization;
its proof was read through the end of Section 6 at extracted line 4945.

The cumulative extracted-text scopes are lines 1–220, 352–406,
2203–2690, 2778–3040 and 3093–4945. All seventeen selected actual
pages 3 and 20–35 were viewed. No whole 52-page reading or visual claim
is made; pages 36–44 were freshly read in extracted text only.
The Sebö three-dimensional Hilbert-basis theorem invoked in Proposition
6.7 is a precisely identified import, not a freshly cleared original
proof. The triangulation notation in Proposition 6.7 must be read
within Definition 5.7's junior-simplex scope.

Proposition 6.5's support-function gluing needs a compatibility choice:
when the centroid `c` of the equal-coordinate face is in the planar
configuration, upper concavity requires its assigned height to be at
least the average of the face-vertex heights. The selected proof fixes
the planar lifting and introduces an additional affine support function
without spelling out this height relation. Arbitrary independent choices
are therefore not an independently verified coherence construction.
This records an unclosed proof step in the inspected preprint; it does
not disprove Theorem 5.13. The new cyclic example uses a complete
explicit support-inequality certificate instead of this gluing step.

The September 2026 HNF preprint itself attributes its special-family
geometric equivalence to this earlier classification. Its separate
explicit coordinate/lifting proof was already audited at the preceding
checkpoint. The earlier-proof limitations above do not create a new
novelty claim or retroactively change those dated review scopes.

## Exact calculation and mathematical boundary

The [calculation](research_calculations/fujiki_oka_height_one_20261004.py)
and [finite record](research_calculations/fujiki_oka_height_one_20261004.json)
use rational arithmetic in `Z^4+Z(1,2,4,8)/15`. Four specified global
stars produce 4, 7, 11 and 15 maximal cones. Every final cone has
ordinary absolute determinant `1/15`, hence lattice multiplicity one.
Their volume totals remain 15 at each stage. The record lists every
final cone and the eight exact remainder terms.

An explicit lifting assigns heights 0 to the original rays, 1 to the
first new ray, and `1/8+2^-10`, `1/4+2^-20`, `1/2+2^-30` to the
remaining rays. All 120 support-plane inequalities are checked exactly,
with equality precisely at each cell's four vertices. The resulting
concave lifting is coherent and integral after scaling by `2^30`.
These are finite certificates for this known example, not a general
classification, a proof of an open problem or a production-model receipt.

The height character is primitive; the affine family is flat with generic
three-dimensional torus. All eight ray heights are one. In regular toric
chart coordinates the parameter is `tau=z_1 z_2 z_3 z_4`, so completion
over `C[[tau]]` is a strictly semistable local model at the original
parameter. No compact-family or arbitrary-field gluing statement is
deduced. The previously recorded BJ22 critical Siu input remains explicit
and conditional; it is unrelated to this finite toric calculation.

The accompanying source manifest pins the acquired PDFs, extracted texts,
actual-view records, metadata and exact calculation. Historical receipts,
the 42-atom inventory and protected Appendix M–N sources are preserved.
