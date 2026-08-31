# Exact source matrix: independent nearby-wall audit

Reviewer: /root/p082_independent_reaudit.
Access and review date: 1 September 2026.

This matrix records sources actually read by the reviewer, not inherited
acceptance. It separates literal source theorems from the candidate's own
local proof. Exact local bytes appear in MANIFEST.json.

## A. BFJ original-field monomial and completed-local interfaces

Boucksom-Favre-Jonsson, Singular semipositive metrics in non-Archimedean
geometry, arXiv:1201.0187v2, 21 January 2014.
Primary version: https://arxiv.org/abs/1201.0187v2 .

- PDF: /private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf
  SHA256 8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270.
- Text: /private/tmp/BFJ_singular_1201.0187_audit_20260831.txt
  SHA256 df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f.

Read Section 1.1 and Definition 1.1, printed p6; Sections 3.1-3.3,
pp12-15; Theorem 3.15 and full proof including Lemma 3.16, pp16-19;
Corollary 3.17, p19. Independently rendered and viewed complete pp14,15,18.

The field hypotheses allow nonalgebraically closed residue field in
characteristic zero and nonreduced SNC multiplicities. The local Cohen,
weighted-series, independent-weight uniqueness, continuity and toric
completion arguments are relevant. The theorem's vertical complexes and
irreducible-intersection convention are NOT silently extended to a mixed
pair or disconnected closed intersection. Normal/Q-factorial output in
Theorem 3.15 is not regular output. Those extra facts are proved by the
specific chart calculation of the candidate. BFJ density and psh theory
are not proof substitutes or current inputs.

## B. GRW comparison and exclusions

Gubler-Rabinoff-Werner, Skeletons and tropicalizations,
arXiv:1404.7044v3, 28 February 2016.
Primary version: https://arxiv.org/abs/1404.7044v3 .

- PDF: /private/tmp/grw1404.7044v3_p213_residual.pdf
  SHA256 f7a909a8508032d8e2e0a0c6f9cd14b06f36cfa465c3e83fa5d40be6033678ad.
- Text: /private/tmp/grw1404.7044v3_p213_residual.txt
  SHA256 851b1820299b758f96db87f37da1ce786b6d169597dc9bebb0f5e3208b1079af.

Read Section 1.1 p1, Definition 3.1 and Section 3.2 pp8-9, the local
skeleton discussion 4.2-4.6 pp12-14 and Proposition 4.10/Corollary 4.11 p14.
Complete printed p8 was independently rendered and viewed.

The standing K is algebraically closed and the charts are strictly
semistable with distinct vertical coordinates. These passages are a
comparison for the face-stratum terminology, not an original-field
arbitrary-multiplicity construction. No claim about primitive affine
lengths, unit conductances or ordinary-sheet decomposition is imported.

## C. Stacks: completion, parameters and connected centers

Current primary HTML, read on the stated date; no local HTML hash asserted.

- https://stacks.math.columbia.edu/tag/0323 :
  Section 10.160, Theorem 10.160.8 and Lemma 10.160.10, including proof.
  Complete regular local rings containing Q have coefficient fields and
  power-series presentations with a chosen regular parameter system.
- https://stacks.math.columbia.edu/tag/00NN :
  Lemmas 10.106.1-3, including proofs, and their Krull-intersection input.
  Associated graded ring, domain, regular sequence and regular quotient.
- https://stacks.math.columbia.edu/tag/0CBN :
  Definition 41.21.1, Lemmas 41.21.2-3 and complete proofs. These verify
  regular closed intersections, component selection and parameter
  independence in a smooth polynomial ambient ring.

These support the local algebra used in Sections 2-3. The actual
multi-coordinate Rees quotient and its nonzerodivisor argument were
checked directly, not merely attributed to a resolution theorem.

## D. Stacks: blowup and flatness interfaces

- https://stacks.math.columbia.edu/tag/01OF :
  Lemmas 31.33.2, .3, .4, .9 and .13 with proofs. Affine Rees charts,
  flat-base-change compatibility, isomorphism off the center,
  integrality and projectivity for finite-type ideals.
- https://stacks.math.columbia.edu/tag/0539 :
  Lemma 15.22.10 and proof. Torsion-free modules over a valuation ring
  are flat.

The candidate uses flat completion base change, not arbitrary base change.
The blowup is vertical because its actual closed center is in the special
fibre. Properness of the original model, not projectivity of X, suffices.

## E. Stacks: smoothness of the residual curve

https://stacks.math.columbia.edu/tag/0B8X :
Lemma 33.25.8, statement and proof read in primary search result.
Regularity and smoothness coincide for a locally algebraic reduced scheme
over a perfect field. This applies because residue characteristic zero
implies k perfect. It does not imply geometric connectedness, and that
stronger property is neither required nor asserted.

The whole curve maps to p by its generic-point image and specialization;
that separate argument was checked in the candidate itself.

## F. Actual topology, not only the tropical image

Chambert-Loir-Ducros, arXiv:1204.6277v2 (25 July 2025), Section 11.1.11,
printed p302; the affine-analytification paragraph was read in:

/private/tmp/CLD25.txt
SHA256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

It describes the topology by coordinate-ring evaluations and the
algebraic support by the seminorm kernel. The note's positive-weight
tail calculation supplies continuity of every such evaluation. Only
this basic topology interface is used; no CLD source representation,
slicing, current extension or rigidity theorem is a dependency.

## G. What was proved locally rather than obtained from a citation

The positive-support integer subtraction terminates; the retained-ray
shears preserve a lattice basis; the normalized vertices converge while
the simplex stays nondegenerate; old positive weights control every
new zero-weight face; the full closed simplex belongs to the chosen
ordinary W; the facet gives a whole proper curve over p; independent
normal weights are dense by the affine-hyperplane/Baire argument.

These are the candidate's explicit geometric arguments independently
checked in the audit. No priority claim is made. No separately authored
capture, outer-collar, finite-projection, wall, or source-representation
packet is a premise.

## H. Visual and preservation record

Fresh rendering used system pdftoppm at 105 dpi, four complete pages:
BFJ14, BFJ15, BFJ18, GRW8. All commands exited zero and emitted no warnings.
The reviewer viewed all four complete images; source headings, formulas,
footnote and page boundaries were legible. PNG hashes are recorded in
CHECKS.json; disposable PNGs are removed after that record. This is
source inspection, not a candidate PDF artifact or a TeX compile.
No PDF source was edited or re-exported.
