# Matroid-specific boundary and wedge-complex follow-up, 5 October 2026

This research checkpoint follows the general projected-collection diagnostic.
It finds additional structure in the matroid construction and verifies the
printed wedge calculation on all 92 labelled matroids with at most four
elements, including the empty ground set and 55 matroids with loops. It does
not import the Lee preprint into active TeX, certify its general cohomology
theorems, repair the general Proposition A.6 or retire a problem atom.

The source remains Seungkyu Lee, *Tropical matroid Schubert varieties and the
graded Möbius algebra*, [arXiv:2604.00750v1](https://arxiv.org/abs/2604.00750v1).
The preceding full-reading audit and its 17 actual primary-page views retain
their own recorded scope. This follow-up rereads the boundary formulas and
the signed wedge calculation, rather than claiming a second complete reading.

## Additional controlling source

The published paper of Eur--Huh--Larson, *Stellahedral geometry of matroids*,
Forum of Mathematics, Pi 11 (2023), e24, 48 pages,
[DOI 10.1017/fmp.2023.24](https://doi.org/10.1017/fmp.2023.24), was acquired
from its publisher, HTTP 200 with PDF magic verified. Its SHA-256 is
`ba22e004dda4991c5961276020376ff029da57e213f3dea9c9500223c3d61501`.
The publisher page was acquired separately and supplies the actual PDF link.
The web extraction of that page failed because it exceeded the tool's content
limit; the direct acquisition subsequently succeeded. Neither event is
represented as a negative literature result.

Targeted extracted-text ranges 1--205, 590--725 and 1300--1475 were inspected.
Four actual published pages, physical and printed 11, 12, 23 and 24, were
viewed in two sheets. No full reading of all 48 pages is claimed here.

| Source item | Printed/physical page | Role |
| --- | --- | --- |
| Definitions 3.1--3.2 and Proposition 3.3 | 11 | Compatible pairs and the simplicial stellahedral fan; an empty flat is allowed in its chain |
| Proposition 3.6(b) | 12 | Stellar subdivision of the negative orthant and its faces relates the stellahedral fan to the coordinate product fan |
| Definition 5.10 | 23 | The augmented Bergman fan is the subfan with independent positive labels and proper-flat negative labels |
| Proposition 5.13 and its proof | 24 | A general coordinate translation of a realization tropicalizes to the augmented support; the unshifted realization is not interchangeable with it |
| Lemma 5.14 | 24 | Free-coextension support and the printed flag clause, with the qualification below |

The printed final clause of Lemma 5.14 says that the flag consists of
**nonempty** proper flats of the original matroid. Read literally, this
excludes the empty flat of a loopless matroid, although the displayed building
set includes its union with the new element and Definition 5.10 retains that
flat. The one-element Boolean matroid makes the issue explicit: allowing its
proper flat `emptyset` gives rays `+e_1` and `-e_1`, whereas excluding it
leaves only the nonnegative ray. A generic translate of its full realization
still tropicalizes to the whole real line. Thus the literal nonempty clause
cannot describe this entire augmented support. This is a local source-text
diagnostic, not a refutation of Proposition 5.13 or the general intended
free-coextension identity. No silently corrected quotation of Lemma 5.14 is
imported. The finite checker uses the proper-flat convention of Definitions
3.2/5.10 and Lee Definition 2.5, including the empty flat when it is a flat.

## Why the matroid projections have additional structure

Write `E` for the ground set, `I` for an independent set and `C` for a chain
of proper flats containing `I`. A cone has generators

\[
 \sigma_{I,C}=\operatorname{cone}(e_i:i\in I)
        +\operatorname{cone}(-e_{E\setminus G}:G\in C).
\]

For a boundary stratum labelled by an admissible pair `(J,F)`, projection
deletes coordinates `J` and `E minus F`. Lee Lemma 4.7, with the implicit
maximal flat `E` supplied by Remark 4.11, says that a cone meets that stratum
exactly when `J subset I` and `F` occurs in the chain or equals `E`. Its
nonzero projected generators are

\[
 e_i\quad(i\in I\setminus J),\qquad
 -e_{F\setminus G}\quad(G\in C,\ G\subsetneq F).
\]

They are the augmented generators of `(M restricted to F)/J`. The flat
interval from `cl(J)` to `F`, with coordinates actually deleted, is essential.
Isomorphic minors with different independent labels are not identified.
Loops of a minor retain zero ambient coordinates; dropping their labels
without recording the embedding would lose information.

There is a useful candidate route for the common-face check. Two original
cones meeting this same stratum share all `e_j` for `j in J` and, if `F` is
proper, the ray `-e_(E minus F)`. Their common original face consequently
still meets the stratum, with witness `e_J-e_(E minus F)`. Nonzero positive
rays remain distinct under projection. For the negative rays below `F`,
the label map `G -> G minus J` is injective, since all these flats contain
`J`. This prevents the projected ray identification responsible for the
earlier general diagnostic.

Subject to the named augmented-fan common-face input, these observations
suggest the identity

\[
 \pi_{J,F}(\sigma\cap\tau)
       =\pi_{J,F}(\sigma)\cap\pi_{J,F}(\tau)
\]

for cones meeting a common matroid stratum. This is a research argument,
not an independently admitted general repair. A complete integration audit
must still distinguish raw stratum cones from their compactified closures,
verify the global closed-cell intersections across different sedentarity
labels, and check the identification with the cellular/sheaf calculation.
The finite checks below verify ray labels and minors; they do not compute
the intersections of arbitrary real cones independently of the source fan
theorem, nor do they settle those topological identification steps.

## Exact finite checks

The standard-library checker enumerates every nonempty equicardinal basis
family and tests the basis-exchange axiom. It therefore includes all labelled
matroids on each ground set of size 0, 1, 2, 3 or 4, with counts
`1, 2, 5, 16, 68`. It constructs their flats, independent sets, chains and
compatible cones. It checks generator linear independence over `Q`, each
projected cone collection against the coordinate-labelled minor fan, the
shared boundary witnesses and projection of common ray sets.

The calculation covers 2,111 augmented cones, 1,330 admissible strata and
119,374 pairs of cones meeting a common stratum. The last number counts
**ray-set** checks. It is not a count of independent polyhedral intersection
certificates. All minors, including those with loops and rank zero, retain
their actual coordinates.

For the cochain check, a basis element is labelled by `(I,F,S)`, where
`I union S` is independent, `S subset F minus I`, and
`|S|=r(F)-|I|-p`. Its cohomological degree is `a=r(F)-|I|`.
The two components of the printed differential in Lee Lemma 5.4 are

\[
 (I,F,S)\longmapsto -e_j\wedge e_S
       \text{ in }(I\setminus\{j\},F),\qquad
 (I,G,S)\longmapsto e_{F\setminus G}\wedge e_S
       \text{ in }(I,F)
\]

for deletion of `j in I` and a covering relation of flats `G<F`, respectively.
The sign of the wedge is computed from the fixed total order of the original
coordinates. The checker verifies that the maps stay in the independent
coordinate basis, that `d squared=0` exactly, and that rational elimination
gives the predicted diagonal flat counts. All 258 fixed-`p` complexes pass.
This tests the printed algebraic complex, including its signs; it does not
prove that this complex computes tropical cohomology for every matroid or
establish an integral/torsion assertion.

For `U_(3,4)`, there are 94 augmented cones and 48 admissible strata. The
fixed-`p` chain dimensions, differential ranks and cohomology are:

| `p` | Chain dimensions in degrees 0--3 | Differential ranks | Cohomology in degrees 0--3 |
| --- | --- | --- | --- |
| 0 | 15, 28, 18, 4 | 14, 14, 4 | 1, 0, 0, 0 |
| 1 | 0, 22, 24, 6 | 0, 18, 6 | 0, 4, 0, 0 |
| 2 | 0, 0, 10, 4 | 0, 0, 4 | 0, 0, 6, 0 |
| 3 | 0, 0, 0, 1 | 0, 0, 0 | 0, 0, 0, 1 |

The diagonal dimensions `(1,4,6,1)` agree with the Whitney numbers claimed
by the preprint. They support the prospective example from the earlier audit;
they do not yet justify inserting a general theorem or singular comparison
into the book. The cup-product and external Chow-ring steps remain separate
source checks. These computations give no Monge--Ampère, metric-convergence,
Siu-division or general closure conclusion.

## Preservation and next step

This checkpoint changes only research records and reader-facing progress
links. All 425 active TeX inputs, bibliography, standalone catalogue source
and PDF, 42 complete problem statuses, and the current 4,261-page book PDF
remain byte-identical to the compactification release. That release's build
and ten-page actual review are reused with their existing scope; no fresh
book compilation or page review is claimed for this research-only change.
There is no new independent model receipt. The previous orthant diagnostic
and its more limited target remain unchanged.

Next checks concern global compactified cells and the cup-product pullback
to the canonical augmented-fan compactification. Known imports can use the
ordinary source protocol after their hypotheses and locators are cleared.
Any original general repair remains a candidate under the repository's
verification protocol until an exact independent receipt exists.
