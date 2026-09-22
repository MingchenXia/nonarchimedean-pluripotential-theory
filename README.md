# Non-Archimedean Pluripotential Theory

This repository contains the current second draft of the monograph
*Non-Archimedean Pluripotential Theory*.  The author field is intentionally
left blank in this release.

**Current-source status, 22 September 2026:** the author supplied the
missing Chapter 70 `CURVE_PSH.tex`, which is now restored byte for byte.
The complete source check passes (389 TeX files, 11,500 unique labels),
and the full build produces a 3,919-page PDF with no unresolved reference
or citation and no horizontal or vertical layout overflow.
The [display-layout audit](manuscript/editorial/full_book_overflow_audit_20260922.md)
records the final line-break checks and preservation of the research sources.
The [current-pushforward audit](manuscript/editorial/ch14_pushforward_sign_audit_20260922.md)
corrects the involution sign and the use of measure pushforward on a curve skeleton.
The [projection and metric-variation audit](manuscript/editorial/ch17_projection_and_variation_audit_20260922.md)
reconstructs the Chapter 17 proofs with their correct current domains and multiplicities.
The [curve curvature and slope audit](manuscript/editorial/ch19_curvature_slope_audit_20260922.md)
reconstructs the graph calculation, residue-degree weights and descent over the ground field.
The [curve length and norm audit](manuscript/editorial/curve_length_norm_audit_20260922.md)
separates intersection and lattice metrics and corrects the compatible-norm calculation.
The [point-energy audit](manuscript/editorial/ch61_point_energy_audit_20260922.md)
proves the truncation bound and completes the global extrema calculation in the P1 example.
The [variational-limit audit](manuscript/editorial/ch61_variational_limit_audit_20260922.md)
reconstructs bounded-energy compactness and integral convergence, with a curve counterexample to weak-to-strong convergence.
The [font-scope correction](manuscript/editorial/ch18_font_scope_audit_20260922.md)
restores normal body type after two Chapter 18 tables.
Source provenance, exact input checksums and validation limits are in the
[recovery build receipt](manuscript/editorial/source_recovery_build_20260922.md).
Continued mathematical and editorial work is tracked in
[`manuscript/editorial/continuation_20260922.md`](manuscript/editorial/continuation_20260922.md).
The current checked editorial inventory is 46 active atoms in 14 formal
problem environments, with tiers `(0,5,8,16,17)`.

The same continuation adds a worked Chapter 16 example explaining the
convexity-forced affine region and nonseparable mixed terms in the latest
two-star smoothing proposition. Its scoped compilation and visual checks
are recorded separately from the full-book build.
Chapter 60 now also spells out the relative numerical nefness reduction,
with exact source locators, a checked normalization, and a separate
[chapter audit](manuscript/editorial/ch60_relative_nef_audit_20260922.md).
Chapter 46's finite-energy measure construction now uses differences of
positive pairs, with explicit counterexamples to two invalid shortcuts;
see its [pairing audit](manuscript/editorial/ch46_finite_pairing_audit_20260922.md).
The subsequent [support and capacity audit](manuscript/editorial/ch47_49_support_capacity_audit_20260922.md)
corrects the scope of the linear-growth support assertion and adds a
model counterexample to its former capacity argument.

The last clean 24 August 2026 release snapshot passed the final structural
audit and produced a 3,081-page PDF from its exact 101-file production-source
closure.  That snapshot records nine mathematical production Rethlas
gates: eight exact-current integrations in Chapters 18, 23, 49, 55, and 69,
and one exact frozen statement/proof gate for the Chapter 70 generalized-
Lelong separation theorem, followed by an independent hostile audit.  The
latter is not represented as a post-integration byte-identity gate.  The
additional 25--28 August gates and exact-current integrations are recorded
individually in the editorial receipts and provenance ledgers.  A fresh
current-source whole-book rebuild through 25 August passed and produced a
3,123-page PDF; the dated release artifacts below remain the earlier
3,081-page source freeze until the next release cut.  The integrated
29 August source, including the full projective ample-class MP--BJ comparison
and the exact finite-level closed-immersion reduction for P17.1, also passes a
whole-book build and produced 3,284 pages at that stage.  On 30 August the full
Banach-base continuity theorem answering Pille--Schneider Question 4.9 in its
stated scope was integrated as `thm:p171-full-assembly`; its exact live gate,
item `pi_87b42b938a8d830222bed78f`, returned final `correct`, with zero
critical errors and zero gaps.  The resulting clean current-source build had
3,318 pages.  Also on 30 August, the exact P07.1 theorem for the
Chambert--Loir--Ducros star \(X_B\) of CLD Section 6.7.3 passed production
verification for every nonempty branch set \(B\).  It proves equality of the
first-stage, full, and explicit comparison psh sheaves and gives decreasing
smooth psh approximation on one fixed neighbourhood.  Production item
`pi_00f6c73303087d94da9eb724`, using `gpt-5.6-sol` at `xhigh`, returned final
`correct`, zero critical errors, and zero gaps.  This narrows P07.1 to
arbitrary higher-dimensional and other nonambient local models outside the
two exact interval structures and \(X_B\); P07.1 and P07.2 remain active, and
the inventory remains 14 formal problem environments and 53 active atoms,
with tiers `(0,5,14,17,17)`.  After that theorem was integrated, the clean
current-source build produced 3,330 pages.  These checks do not turn
source imports or book-level derivations into novelty or priority claims, or
close residual questions outside the displayed theorem scopes.

The manuscript has 72 chapters in six parts and 12 reference appendices.  It
develops:

- valued fields, models, Berkovich spaces, skeleta, and semipositive metrics;
- the Chambert--Loir--Ducros calculus, delta-forms, and tropical methods;
- Boucksom--Favre--Jonsson pluripotential and variational theory;
- Boucksom--Jonsson theory over a trivial valuation, including the supplied
  proof of the envelope theorem for unibranch projective varieties;
- complex and compact Kähler non-Archimedean theories, test curves, tropical
  spectra, and transcendental Monge--Ampère theory;
- comparison theorems, filtrations, hybrid degenerations, and carefully
  delimited research extensions and counterexamples.

## Build

From `manuscript/`, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

The build runs BibTeX and MakeIndex through `latexmkrc`.  The generated PDF is
`manuscript/book.pdf`.  The audited release PDF is
`output/pdf/Non-Archimedean_Pluripotential_Theory.pdf`; the corresponding
source archive is in `output/source/`.  Exact hashes and audit evidence are in
`output/BUILD_AND_AUDIT_SUMMARY.md`, `output/PRODUCTION_SOURCE_SHA256SUMS`,
and `output/RELEASE_ARTIFACT_SHA256SUMS`.

## Editorial records

- `BOOK_PLAN.md`: detailed architecture and chapter plan;
- `LITERATURE_MAP.md`: annotated primary-literature map;
- `RESEARCH_QUESTION_LEDGER.md`: solver and hostile-audit record for open
  questions;
- `author_source_repairs/Mixed_volumes_of_partial_Okounkov_bodies/`: repaired
  source files and the repair log for the supplied proof of Conjecture 8.8;
- `manuscript/editorial/`: hypothesis, notation, provenance, status, and
  mathematical-revision ledgers;
- Appendix L: reader-facing provenance and theorem-status ledger.

The supplied source archives remain locally under `source_material/` and are
intentionally excluded from version control.  Results proved only in the
supplied envelope manuscript are identified as such and are not
misrepresented as previously published theorems.

As recorded on 1 September 2026, the current research-frontier inventory is 14
open problem environments, all in Chapter 72, split into 51 active editorial
research atoms with tier counts `(0,5,12,17,17)`. These are not 51 independent
untouched literature conjectures. The editorial records retain the source-cutoff
dates and make every remaining mathematical boundary explicit. The clean-build
and exact-current Rethlas gates that have passed are recorded separately from
source imports and unresolved packets.

The 1 September local-comparison and source-cell-access research is preserved
with its exact independent reviews in
`manuscript/editorial/chapter72_local_access_checkpoint_20260901.md`.
These conditional research results have not passed the production Rethlas
gate and are not promoted to live-book theorems. P21.3 remains open. Historical
verification hashes for the Bedford--Taylor subsection have been moved, without
changing its mathematical statements, to
`manuscript/editorial/chapter72_bedford_taylor_verification_archive_20260901.md`.

The subsequent 1 September rank-drop diagnostic and independently reviewed
conditional four-family coefficient transport are preserved in
`manuscript/editorial/solver_dossiers_20260901/chapter72_propagation_preservation_20260901/CHECKPOINT.md`.
The original proof and its correction history are retained. This does not
establish arbitrary-source propagation or satisfy the production gate.

The subsequent component-curvature and full-CPsh weighted/polar packets have
independent mathematical reviews and actual Rethlas reports returning
`correct`. Detailed execution review, however, found an approval-gate bypass
inside both verifier runs; these reports are not treated as a clean
production gate or as permission to promote new theorems. The exact evidence,
remaining review and integration status are recorded in
`manuscript/editorial/chapter72_curvature_verification_checkpoint_20260901.md`.

The latest 1 September whole-book build has 3,478 pages. It incorporates
Chapter 14 corrections distinguishing skeleton measures from integration
currents, retaining nonreduced multiplicities, and explaining the thickening
counterexample to the unrestricted fibre formula. It also retains the
corrections to the CLD multiplier and harmonic-chart hypotheses in Chapter 16
and a complete replacement of the affected canonical-metric positivity step
in Chapter 19 using residual line bundles and convex tangent-plane approximation.
These are corrections and exposition of existing results, not new research
theorem promotions. Its local output is
`output/pdf/Non-Archimedean_Pluripotential_Theory_current.pdf`; the older release
PDF and the preceding current PDF are preserved. Source hashes, build checks
and the scoped visual review are in
`manuscript/editorial/solver_dossiers_20260901/cld_cycle_current_repair_build_20260901/BUILD_REPORT.md`.
The preceding Chapter 16/19 correction build is documented in
`manuscript/editorial/solver_dossiers_20260901/cld_hypothesis_repair_build_20260901/BUILD_REPORT.md`.
The earlier presentation-only build remains documented separately in
`manuscript/editorial/solver_dossiers_20260901/chapter72_presentation_build_20260901/BUILD_REPORT.md`.

The 3,478-page PDF is still a research draft, not a completed mathematical
audit of the book. The five identified Chapter 16 barrier, weight and
polar-limit proof repairs are no longer outstanding: they entered the live
manuscript in commit `10ccff9` on 8 September 2026 and were independently
re-derived line by line on 14 September 2026. The closed record, including
the re-derivation of the compact-sublevel barrier, the real-parameter weight
forms with their corrected derivative factors, the constant `C(k,a)`, and the
fixed-measure polar limit, is
`manuscript/editorial/chapter16_weighted_polar_rewrite_status_20260901.md`.
That re-derivation certifies internal consistency only; it is not a
production Rethlas gate and authorizes no theorem promotion.

Downloaded reference copies, temporary build trees, TeX intermediate files,
and superseded release PDFs are also intentionally excluded from version
control.
