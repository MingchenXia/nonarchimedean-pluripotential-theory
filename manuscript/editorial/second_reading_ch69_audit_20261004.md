# Chapter 69 renewed second-reading audit

Date: 4 October 2026. Baseline: `66e9f50611b229f9542eb52663193122f591dda7`.

The complete 1,790-line source `parts/part6/ch69_verified_extensions.tex`
was freshly read in seven consecutive ranges. There are no direct inputs.
The source remains byte-identical. This checkpoint closes only Chapter 69
in the ordered whole-book rereading.

## Mathematical and expository review

- The CLD criterion assumes actual smooth pluriharmonic approximants
  converging locally uniformly. Order-zero positivity controls multiplication
  against every compactly supported smooth test form; closedness and
  continuity of differentiation give the result. Equal curvatures alone
  do not construct those approximants. Distributional cell rigidity uses
  all second derivatives and a connected cell interior, not vertex gluing.
- The abstract cross has unit-weight curvatures four at the vertex and
  weighted-product defect two for weights (2,2,1,1). It is an abstract fan
  calculation. A compact harmonic chart cannot have that unbounded image.
  On the proper reducible torus curve, the two Gauss points are distinct:
  U has curvature 4 delta_qh, V has 2 delta_qh + 2 delta_qv, and HT has
  defect 4 delta_qh - 2 delta_qv. Equality arises only after tropical
  pushforward. The proof treats arbitrary refined test charts, partitions
  of unity and the rigid intersection node; it does not assert equality
  of these two curvatures upstairs.
- The smooth four-punctured projective-line candidate does have equal
  upstairs curvature. Its third-unit refinement has primitive rays
  (1,0,1), (-1,0,0), (0,1,-1), (0,-1,0). Closedness forces all four ray
  weights to agree, excluding (2,2,1,1) on this concrete candidate. The
  order-zero vertex term is tested separately. Restriction of a delta-current
  to smooth tests gives the same obstruction. This is neither a classification
  on arbitrary curves nor a solution of the general upstairs-cross problem.
- A fixed SNC dual complex is strongly compact by the sourced equi-Lipschitz
  estimate. Compact-to-Hausdorff comparison makes it weakly closed first,
  then identifies its two topologies. Weak convergence alone therefore
  suffices within that fixed complex. The moving-centre projective-space
  counterexample lies outside any one such complex; no global Radon–Riesz
  implication is restored.
- Trace has an I-class input and a P-class output with I-good representatives.
  The generic-Lelong-zero domain is saturated before quotienting. In the
  split product calculation, transverse strict positivity supplies a common
  mass floor; smooth pullback of multiplier ideals is checked for every real
  coefficient. The result is the I-envelope's P-class, rather than the P-class
  of an arbitrary input. Retraction and class splitting remain hypotheses.
- The toric section-counting proof is on an integral/rational big class.
  Strict multiplier-ideal inequalities are squeezed between shifted convex
  bodies. The inner limit is lattice-normalized volume of K + epsilon Q,
  without an n! factor or literal finite-level equality. Its epsilon exponent
  is n - dim K. The segment example separates numerical dimension from
  vanishing top mass. The separate Chapter 55 fixed-current argument treats
  real classes; no class-varying rational approximation is substituted here.
- The mass-body obstruction works even for arbitrary Lebesgue-measurable
  bodies. The polar Cantor measure is atom free, giving zero Lelong numbers
  and trivial multiplier ideals for all positive coefficients. Its Green
  potential is integrable by Tonelli and has zero non-pluripolar mass, whereas
  the smooth zero potential has mass one. Convexity of the proposed body is
  unnecessary. P-sensitive constructions remain outside this obstruction.
- Complete-intersection slicing tests restrictions of nonnegative ambient
  smooth functions only. Regularized maxima are smooth across the zero set
  by the deletion property. Two integrations by parts have positive sign;
  bounded continuity and Gauss-fibre specialization give the curve formula.
  The regular-sequence and pure-relative-dimension-one hypotheses remain.
  No arbitrary-current pullback, residue-degree atom formula or global
  positivity converse is inferred.
- For real PL functions, CLD-v2 implies classical psh, and classical psh is
  equivalent to model semipositivity in the good strict nontrivially valued
  domain. The reverse CLD-v2 arrow requires the relative interior. The exact
  local Fubini–Study form uses nonnegative coefficients and maxima of unit
  logarithms after inversion. Log-sum-exp is smooth, convex and decreasing
  along its own parameter; summable constant shifts turn locally uniform
  approximants into one decreasing sequence. Separatedness is retained for
  the current implication, with no reverse-current implication. The annulus
  corner shows why these equivalences do not imply CLD smoothness.
- The boundary ledger and dependency diagram preserve every missing arrow.
  The final invariant-toric, difference-invariant Bedford–Taylor and
  modulus-controlled-envelope paragraphs retain their stated source and
  receipt boundaries. Chapter 66's completed review supplies prior hybrid
  context; these summaries do not turn the remaining Chapter 72 atoms into
  solved problems or constitute new verification of frozen proof objects.

No new mathematical or layout defect was identified. Source checks preserve
108 labels, 50 formal environments including 17 proofs, all 50 bodies and
their order, and 61 labelled tagged displays. Five protected blocks remain
byte-identical to the pinned historical source. Their SHA-256 values and
lengths are in the manifest. All 596 legacy inline delimiters (298 pairs)
occur inside those protected blocks; none occurs outside. No double-dollar
display, placeholder, unlabelled numbered object or direct input was found.

## Scoped primary evidence and historical provenance

Eight pinned cached PDFs, 58 selected physical pages and all selected text
were freshly read. All nineteen primary contact sheets were actually viewed.
The manifest records complete page lists, hashes and precise import limits.
There was no new acquisition, whole-paper dependency audit or exhaustive
literature search.

| Source | Selected physical pages | Evidence boundary |
| --- | --- | --- |
| CLD, arXiv:1204.6277v2, 25 July 2025 | 1, 139–140, 187, 209, 223, 424, 466–467, 533–537 | Printed calibration/Stokes and regularized-maximum proofs; 18.6.2 Gauss-fibre and 18.7.2/3 printed proofs. 8.7.2 continuation on 210 is unselected. Earlier calibration, integration and continuity facts remain imports. The n-d relative dimension follows 18.7.3's proof, correcting its stated d. |
| GRPL, arXiv:2503.05513v1, 7 March 2025 | 1–3, 16–18 | 1.5 statement and complete printed 5.3/5.4/5.5 proofs. 5.6 continues on unselected 19. Lifting and curve inputs remain imports. |
| GRC, arXiv:2506.13548v2, 17 September 2025 | 1–3, 22–23 | CLD-v2/classical interface and complete printed 4.3 proof; Wanner, GRPL and preceding functoriality remain imports. |
| BJ, published AFST 31 (2022), 647–836 | 1, 157–159, 184–186 | Section formula, 11.12 printed proof and literal 11.16; A.4 printed proof imports BFJ Izumi estimates. Toric probability/raw normalization retained. |
| Cao, arXiv:1210.5692v1, 21 October 2012 | 1, 19–23 | Correct Proposition 4.4 and its complete printed proof, including Lemma 4.5. Earlier approximation and vanishing theorems remain imports. |
| Xia, lecture book updated 18 July 2026 | 1, 216, 254, 274–278, 282–283 | Polar Cantor example; 7.1.2 and 8.1.1/2 printed proofs, trace definitions and birational lemma. Carleson's Cantor construction and prior dS theory remain imports. 8.2.2 begins before selected 282; no full proof claim. |
| BEGZ, arXiv:0812.3674v2, 9 September 2010 | 1, 5–8 | Degree-one formula, printed 1.4 locality/potential-independence and 1.5/1.6 proofs. Multilinearity is left to the reader; 1.8 only begins in this selection. |
| GJR, arXiv:2111.05741v3, 7 March 2025 | 1, 47–50 | Exact 7.9 local form and complete printed 7.10/7.14/7.15 proofs. Earlier formal-model/residue inputs imported; positivity is distinguished from strong positivity. 7.11's expectation is historical. |

The toric exact-current receipt, production lci-slicing receipt, and both
production/live-integration four-punctured receipts were freshly read.
The controlling four-punctured run is `20260825T034743Z_ea6194f07e86`, item
`pi_19c9aad210847a2875a0fe4a`; its negative scope matches the live proposition.
The Part VI post-expansion audit was freshly read with its dated addenda;
its superseded counts are historical snapshots. The five live-block pins
are preservation checks, not new production verdicts. Historical Chapter 69
calculation supplements (11,863 exact and 90 numerical checks in twelve
families) were not rerun. Frozen packets, receipts and historical audits
remain unchanged.

## Build and actual visual review

The unchanged source reuses the successful Chapter 60 fourth-stage full
validation. Current book PDF: 4,236 pages, 19,733,185 bytes; SHA-256
`c06b9b2487f7c2f82a4fc8d19fa02eae760368547d3e23cbdbcf24b3f680bc8d`.
The current log has zero TeX errors, package warnings, overfull boxes,
unresolved references/citations or rerun requests; 953 bookwide underfull
boxes remain. All six checker regressions passed in that full validation.
No redundant build or regression rerun is claimed here.

All 26 chapter physical pages 3547–3572 and seams 3546/3573 were actually
viewed in seven contacts. The preceding seam is an intentional blank;
Chapter 69 itself ends with source notes on 3572. Formulas, tables and the
dependency graph fit. Review export:
`/workspace/book-completion-drafts/second-reading/Ch69_Review_2026-10-04.pdf`.
Fresh post-render checks pass for 425 inputs and 12,569 labels. Inventory
remains 42 active atoms in twelve families, tiers (0,3,7,15,17).

A fresh main fetch found no incoming commits. Publication continues through
normal work-branch pushes and the existing draft PR. Chapter 70's full
2,268-line main source has now been freshly read; its eight direct inputs
and scoped checks continue. Later units are not marked complete. Related
directions and recent-arXiv integration follow the whole-book polishing pass.
