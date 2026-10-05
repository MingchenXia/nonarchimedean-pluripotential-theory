# Tropical matroid Schubert source audit, 5 October 2026

This is a research record outside active TeX. It follows a full reading of
Seungkyu Lee, *Tropical matroid Schubert varieties and the graded Möbius
algebra*, [arXiv:2604.00750v1](https://arxiv.org/abs/2604.00750v1), submitted
1 April 2026 at 11:17:10 UTC. The live submission history still lists only
v1. The 26-page PDF was acquired successfully; its SHA-256 is
`4ea18e2148d3bdc9f268deed9ea66c15aa22e5b5809b2748d88be318f48bff38`.
The author's inspected research page links to this same arXiv entry.

The cohomology calculation is a promising complement to Appendix G's
published cohomologically tropical comparison. Before integration, however,
the paper's general boundary-complex assertion needs clarification. The
explicit rational construction below tests Proposition A.6 with its printed
hypotheses. It is a source-audit candidate with exact supporting computations,
not an independently admitted new theorem or a certified refutation of
Theorems 1.1 and 1.2. The latter use additional matroid structure described
in Proposition 4.8. No mathematical statement from this preprint is added
to the active manuscript in this checkpoint.

## Reading and primary anchors

The extracted text was read in full, lines 1--1489, in successful bounded
ranges 1--220, 221--440, 441--660, 661--880, 881--1100, 1101--1320 and
1321--1489. Nine image sheets were actually viewed, covering 17 physical
pages: 1, 2, 5, 6, 11--21, 24 and 25. The printed numbering agrees with the
physical numbering. This is not a claim that all 26 pages were viewed as
images. Acquisition, metadata, bounded searches, text and viewed-image
digests are recorded in the accompanying manifest.

| Primary anchor | Pages | Scope retained for later integration |
| --- | --- | --- |
| Theorems 1.1 and 1.2 | 2 | Real-coefficient tropical cohomology is claimed to be diagonal, with its total ring the graded Möbius algebra; algebra degree `p` corresponds to cohomological degree `2p` |
| Standing conventions | 4 | Real coefficients throughout; the stated integral extension is not independently imported here; cones are closed and strongly convex |
| Definitions 2.3--2.5 and Remark 2.6 | 5 | Flat-indexed multiplication, augmented Bergman cones, and zero-coordinate treatment of loops |
| Definitions 4.1--4.2 and Lemma 4.4 | 10--11 | The paper's ambient-fan compatibility condition and projected boundary collection |
| Definition 4.5 | 11 | Closure of augmented Bergman support in the coordinate product `(TP^1)^E`, not its canonical fan compactification |
| Lemma 4.7, Proposition 4.8 and Corollary 4.10 | 12--13 | Independent-set/flat labels identify each sedentary stratum with an augmented Bergman fan of a minor |
| Remarks 4.11 and 4.12 | 13 | The implicit maximal flat resolves the empty-negative-boundary case; isomorphic minors on different ground sets remain different strata; minors can have loops |
| Proposition 5.3 and Lemma 5.4 | 15--17 | Rank filtration, stratumwise local Poincaré duality and the signed wedge boundary map |
| Proposition 5.5 and Corollary 5.6 | 17--18 | Flat-rank filtration splits into Koszul complexes and leaves one diagonal class per rank-`p` flat |
| Proposition 6.1 and the proof of Theorem 1.2 | 19--20 | Pullback from this compactification to the canonical compactification and the Möbius subalgebra of the augmented Chow ring |
| Proposition 7.3 and Corollary 7.4 | 20--21 | A generic coordinate translation of the realization is fixed before extended tropicalization over trivially valued `C` |
| Remark 7.5 | 21 | The generally singular algebraic compactification and possibly irregular tropical boundary are outside the earlier smooth comparison's immediate scope |
| Definitions A.3 and A.5; Proposition A.6 | 24--25 | Target general claim that the stated projected collection is a polyhedral complex |

A bounded search for this arXiv identifier, Proposition A.6 and corrections
did not provide an acquired repair. This is not an exhaustive absence claim.
The search also found Kastner--Shaw--Winz, *Tropical compactification via
Ganter's algorithm*, arXiv:2012.12161, and a published article with DOI
`10.1007/s00454-023-00581-2`. Only metadata/search material was inspected for
that work in this checkpoint. Its theorem numbers or hypotheses are not
imported as a repair without reading the controlling primary text.

## What the proposed cohomology comparison actually says

For a rank-`d` matroid `M` on `E`, let `Sigma_M^+` denote its augmented
Bergman fan in `R^E`. Lee defines

\[
 Y_M=\overline{|\Sigma_M^+|}^{\,(\mathbb{TP}^1)^E},\qquad
 \mathbb{TP}^1=\mathbb R\cup\{-\infty,+\infty\}.
\]

The claimed diagonal ring has basis `y_F`, one vector for each flat, and

\[
 y_Fy_G=
 \begin{cases}
  y_{F\vee G},&r(F\vee G)=r(F)+r(G),\\
  0,&\text{otherwise}.
 \end{cases}
\]

With real coefficients, the stated dimension of `H^{p,p}(Y_M)` is the
Whitney number `W_p(M)`, the number of rank-`p` flats. The proof uses
Poincaré duality on the open augmented-matroid strata, not a claim of global
duality for `Y_M`. Its second filtration decomposes into wedge complexes
with vector `-e_J`; those with nonempty `J` are acyclic, while empty `J`
contributes one vector for each flat of the required rank. The ring step
uses an injective pullback to the canonical compactification and identified
external Chow-ring results, including the paper's citations to AP24b and
BHM+22. These dependencies have not been freshly read in full here.

For a complex realization, the algebraic compactification is the closure
of the embedded vector space in `(P^1_C)^E`. Lee fixes a generic coordinate
translation before tropicalizing. Omitting that translation changes the
embedded tropical support and would incorrectly substitute the ordinary
Bergman construction for the augmented one. The resulting comparison is a
graded-ring comparison with singular cohomology. It is not the full
all-closed-strata comparison used in the preceding AAPS section.

If the asserted computation is admitted after the geometry check, the
uniform matroid `U_{3,4}` provides a transparent explanatory consequence:
its flat counts by rank are `(1,4,6,1)`. Thus its proposed degree-two and
degree-four dimensions are different, which excludes global Poincaré
duality. This is only a prospective direct consequence of the named
preprint result, not an independently proved new result or a statement
currently inserted in the book.

## A rational test of the general projected-complex claim

Work in `N=R^4` with coordinates `(x,y,z,w)`. Let `Delta` consist of the
positive orthant and all its coordinate faces. It is a finite rational
simplicial fan. Set

\[
 h_1=x-y+z-w,\qquad h_2=x-y-z+w.
\]

Let `Sigma` be the common refinement of `Delta` and the central hyperplane
fans cut out by `h_1=0` and `h_2=0`. Its support is the positive orthant.
It is a genuine rational fan: on each coordinate face, split by all signs
of the two linear forms and retain all faces. For every `eta` in `Delta`,
these refinement cones contained in `eta` cover `eta`. Consequently

\[
 |\Sigma|_\eta|=|\Sigma|\cap\eta
\]

is exactly Definition A.3's compatibility condition. No balancing,
completeness or simpliciality of `Sigma` is assumed in that printed general
definition; `Delta` is simplicial as required. Every cone is closed and
strongly convex, since it lies in the positive orthant.

Take the two-dimensional ambient face

\[
 \zeta=\operatorname{cone}(e_x,e_y),\qquad
 \pi^\zeta(x,y,z,w)=(z,w).
\]

Two cones of `Sigma` are

\[
 \sigma_{++}=\{x,y,z,w\ge0:\ h_1\ge0,\ h_2\ge0\},
 \qquad
 \sigma_{+-}=\{x,y,z,w\ge0:\ h_1\ge0,\ h_2\le0\}.
\]

Both meet `relint(zeta)`. Witnesses are respectively `(2,1,0,0)` and
`(1,1,0,0)`. The second witness lies on a face of `sigma_{+-}`, which is
allowed: Definition A.5 requires intersection with the relative interior
of `zeta`, not with the relative interior of `sigma`.

Their projected cones are

\[
 C=\pi^\zeta(\sigma_{++})=\{(z,w):z,w\ge0\},\qquad
 D=\pi^\zeta(\sigma_{+-})=\{(z,w):z\ge w\ge0\}.
\]

These identities have direct all-parameter certificates. Write `t=x-y`.
For `sigma_{++}`, the constraints are `t>=|z-w|`; every point in `C` lifts
by `y=1`, `x=1+|z-w|`. For `sigma_{+-}`, the constraints are
`w-z<=t<=z-w`, which imply `z>=w`; conversely every point in `D` lifts
by `x=y=1`. Thus the projection formulas do not rest on sampling or
floating-point computations.

The intersection `C cap D=D` is not a face of `C`. It is a proper
full-dimensional subcone and contains `(2,1)`, an interior point of `C`.
Equivalently, `(2,0)` and `(0,1)` belong to `C` and their sum `(2,1)` belongs
to `D`, while `(0,1)` does not. This violates the defining additive property
of a face of a convex cone. Both `C` and `D` occur in the collection printed
in Definition A.5, so that collection fails the pairwise face-intersection
axiom on this boundary stratum. Identifying repeated presentations, as in
Remark A.7, does not remove a proper distinct subcone.

The support itself is harmless: in this example its closure is the
nonnegative compact orthant with its usual polyhedral structure. The target
is the particular unrefined collection of *all* projected cones, not the
existence of some polyhedral structure on that closure. Proposition A.1's
single-cone closure identity is also consistent with both explicit
projections; this test challenges the additional complex assertion in A.6.

## Exact supporting computation and limits

The standard-library checker
`tools/check_lee_boundary_projection_20261005.py` enumerates 144 coordinate-
face/sign descriptions and deduplicates them to 52 cones, with dimension
counts `(1,10,21,16,4)`. All 1,326 distinct cone pairs have exact supporting-
form certificates for their common face. Sixteen ambient coordinate faces
are checked. Exact Fraction row reduction enumerates the extreme rays of
the two displayed cones and confirms their projected generators:

- `sigma_{++}` gives `(1,0)`, `(0,1)` and the redundant `(1,1)`;
- `sigma_{+-}` gives `(1,0)` and `(1,1)`.

The cone identities also follow from these generators and the algebraic
lift formulas. Twenty-five rational parameter pairs provide an additional
sign/transcription check; the finite grid is not the justification of an
identity over all real parameters. The supporting-form pair checks concern
the original four-dimensional fan; the explicit two-dimensional addition
witness then diagnoses its projected collection.

This candidate uses a general orthant refinement, not an augmented Bergman
fan of a matroid. Proposition 4.8 separately identifies the actual projected
strata in the matroid construction as augmented Bergman fans of minors.
Whether that specific combinatorics supplies all required cross-stratum
face compatibility must be checked directly. A general boundary collection
can instead be further subdivided, but compatibility of such refinements
across strata, their lifted incidence maps and the cochain computation
would require a separate argument. Neither repair is asserted here.

The previously suspected empty-flag case in Lemma 4.7 is not treated as an
additional counterexample: Remark 4.11 explicitly supplies the maximal-flat
convention. Loop coordinates and distinct independent-set labels likewise
follow the paper's explicit conventions. No integral coefficient extension,
priority claim, main-theorem refutation, Monge--Ampère implication or newly
solved open problem follows from this checkpoint.

## Admission and preservation

The repository protocol applies to statements first proved in the book;
an original formal admission requires an independent production audit and
receipt. None is made here. There are zero new independent model calls,
and no historical receipt is extended. The source-audit candidate,
checker and exact result are retained outside active TeX.

All 425 active TeX inputs, existing formal statements and proofs, the
4,259-page book PDF, bibliography, 86-page catalogue source/PDF and all 42
complete problem-status strings are byte-preserved. Previous frozen book
artifacts and manifests are retained; no fresh book build or page review is
claimed for these identical manuscript bytes. The currently open catalogue
editor is not changed or reopened. Normal work-branch publication is
authorized; incoming remote research is inspected before publication.

Next: read the controlling compactification source and check the stronger
boundary conditions, then examine Proposition 4.8's specific cross-stratum
incidence rather than relying on A.6's general assertion. Only integrate
the cohomology material when the relevant geometric scope is settled.
