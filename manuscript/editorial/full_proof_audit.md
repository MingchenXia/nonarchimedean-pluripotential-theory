# Full-proof release audit

**Historical snapshot:** 14 August 2026, frozen after the exercise-conversion
pass and before the concurrent proof-expansion agents completed their next
pass.  
**Current static reconciliation:** 22 August 2026, after the second-draft
expansion pass.  
**Scope:** the historical inventory covers the 92 sources included by
`manuscript/book.tex`; the current mechanical scan covers the live numbered
chapters and appendices.  
**Rule:** every theorem, lemma, proposition, and corollary must have a complete
proof. A deep imported result must additionally be visibly marked as imported
and carry a precise primary-source anchor. Exercises are forbidden. Open
`problem` environments in Chapter 71 record research status and are not reader
assignments.

This is a static expansion queue, not a claim that every row is mathematically
false or unsupported. The scanner selected a statement whenever no `proof`
environment occurred between its end and the next theorem-like statement or
section/chapter boundary. Thus a row can represent a genuinely missing proof,
a proof dispersed through later prose, or a correctly sourced import that
still violates the new presentation rule. Line numbers are those of the
frozen snapshot and drifted during the subsequent expansions.

The reproducible scan at this snapshot finds exactly **66** items: 51 in the
six numbered parts and 15 in the appendices. Earlier provisional totals were
taken while proof edits were landing and are superseded by this frozen list.

## Classification

| Code | Required disposition |
|---|---|
| E | Elementary proof can be supplied locally. |
| D | Deep literature theorem: expand the proof to the book's required level and visibly mark every irreducible imported input with an exact primary-source anchor. |
| R | Definition, scope ledger, or status statement: retype it outside a theorem-like environment. |
| B | Likely missing-proof bug: the manuscript presently offers neither a complete local proof nor an adequate imported-theorem presentation. |

“Exact” in the source column means that the adjacent prose gives a theorem,
proposition, corollary, section, or Stacks tag sufficient to locate the input.
It does not mean that omission of a full proof is accepted.

## Inventory

| # | File:line | Environment / label | Source-prose status | Class | Action |
|---:|---|---|---|:---:|---|
| 1 | `part1/ch03_models.tex:292` | theorem `thm:flattening-models` | Exact: Stacks Tags 0815 and 081T; explicitly identified as Raynaud--Gruson flattening | D | Expand the reduction used in the book and mark the flattening theorem as imported. |
| 2 | `part1/ch04_berkovich.tex:205` | theorem `thm:berk-proper-compact` | Exact: Berkovich, Theorem 3.4.8; prose admits that only an outline is given | D | Expand the analytic properness argument and mark the foundational imported step. |
| 3 | `part1/ch05_skeleta.tex:250` | theorem `thm:skeleton-deformation` | Exact literal citation: Berkovich, *Invent. Math.* 137 (1999), Theorem 8.1; not encoded as a bibliography citation | D | Add a primary-source citation and a full proof-level reconstruction. |
| 4 | `part1/ch05_skeleta.tex:309` | theorem `thm:skeleton-subdivision` | Exact: BFJ16 Theorem 3.15; only the toroidal construction is sketched | D | Expand normalized blowup, incidence, Cartier, and resolution steps. |
| 5 | `part1/ch06_metrics.tex:180` | theorem `thm:gm-metric-comparison` | Inadequate: attributes the result to Gubler--Martin but gives no paper key or theorem numbers | D | Insert exact anchors for all three clauses and expand their reductions. |
| 6 | `part1/ch06_metrics.tex:312` | theorem `thm:model-semipositive-closed` | Partial: generic `GM19` citation without theorem number | D | Locate the exact GM statement and expand the divisorial-point closedness proof. |
| 7 | `part1/ch06_metrics.tex:466` | theorem `thm:cl-continuous-extension` | Exact by section: CL06 §§2.3--2.4; only the local-height mechanism is outlined | D | Expand existence, approximation independence, positivity, mass, and weak continuity. |
| 8 | `part2/ch13_forms.tex:55` | proposition `prop:cld-local-normal-form` | Exact: CLD25 Proposition 15.1.1 and Corollary 15.1.2 | D | Expand chart descent and the reduced-space assertion. |
| 9 | `part2/ch13_forms.tex:244` | theorem `thm:cld-analytic-integration` | Exact: CLD25 Propositions 15.3.1--15.3.2 | D | Expand common refinement, projection formula, and scalar extension. |
| 10 | `part2/ch13_forms.tex:258` | theorem `thm:analytic-is-tropical-space` | Exact: CLD25 Theorems 15.6.1 and 15.7.1 | D | Expand interior balancing and analytic-boundary identification. |
| 11 | `part2/ch13_forms.tex:303` | theorem `thm:cld-smooth-partition` | Exact: CLD25 Proposition 15.2.8 and Corollary 15.2.10 | D | Expand separation, approximation, bump, and locally finite gluing. |
| 12 | `part2/ch14_currents.tex:342` | theorem `thm:current-fundamental-cycle` | Exact: CLD25 Proposition 16.6.3 | D | Give the component-removal and generic-multiplicity proof. |
| 13 | `part2/ch14_currents.tex:382` | theorem `thm:cld-fibre-integration` | Exact: CLD25 Theorem 16.5.4 and Corollary 16.5.5 | D | Expand compatible tropicalizations, cellwise Fubini, and degree indices. |
| 14 | `part2/ch14_currents.tex:405` | theorem `thm:cld-fibre-projection` | Exact: CLD25 Theorem 16.5.7 | D | Expand the smooth case and the continuous Bedford--Taylor passage. |
| 15 | `part2/ch14_currents.tex:434` | theorem `thm:cld-positive-support` | Exact: CLD25 Theorem 16.8.5 and Corollary 16.8.6 | D | Expand support positivity and the Gauss-extension reduction. |
| 16 | `part2/ch15_poincare_lelong.tex:44` | theorem `thm:cld-poincare-lelong` | Exact: CLD25 Theorem 16.7.3 and counterexample 16.1.4 | D | Expand the regular meromorphic-function proof; retain the literature-established title. |
| 17 | `part2/ch15_poincare_lelong.tex:250` | theorem `thm:gr-pl-comparison` | Partial: cites GR25Classical/GR25PL but omits Theorem 4.3 and the exact curve-criterion number in the adjacent source prose | D | Add exact anchors and expand both arrows with all base hypotheses. |
| 18 | `part2/ch15_poincare_lelong.tex:264` | proposition, unlabeled | Partial: generic GR25Classical citation; functorial steps are asserted in prose | D | Separate the formal pullback argument from the imported maximum principle and prove both. |
| 19 | `part2/ch15_poincare_lelong.tex:333` | theorem `thm:cld-levine` | Exact: CLD25 Theorem 18.7.5 | D | Expand blowup, Poincaré--Lelong, telescoping, and pushforward. |
| 20 | `part2/ch16_bedford_taylor.tex:323` | theorem `thm:bt-harmonic-compatibility` | Exact: CLD25 Proposition 8.11.1 and Corollary 8.11.2 | D | Expand the calibrated Stokes and face-balancing proof. |
| 21 | `part2/ch16_bedford_taylor.tex:346` | corollary, unlabeled | Exact: CLD25 Corollary 8.11.3 | D | Derive it explicitly from the preceding theorem and source hypotheses. |
| 22 | `part2/ch16_bedford_taylor.tex:398` | theorem `thm:cld-polar-negligibility` | Exact: CLD25 Theorem 16.9.2, Corollaries 16.9.3--16.9.4, Proposition 16.9.1 | D | Expand barrier, CLN, approximation, and monotone-convergence steps. |
| 23 | `part2/ch17_metrized_bundles.tex:103` | theorem `thm:cld-formal-pl-comparison` | Exact: CLD25 §17.5; GM19 Proposition 2.10 and Theorem 1.1 | D | Expand Raynaud/formal gluing and state each algebraization boundary. |
| 24 | `part2/ch17_metrized_bundles.tex:239` | theorem `thm:cld-relative-ma` | Exact by section: CLD25 §18.6 | D | Expand the analytic-fibre and curvature-product comparison. |
| 25 | `part2/ch17_metrized_bundles.tex:284` | theorem `thm:cld-formal-intersection` | Exact: CLD25 Theorem 18.5.5 | D | Expand graded reductions, residual bundles, and defect factors. |
| 26 | `part2/ch17_metrized_bundles.tex:403` | theorem `thm:cld-bochner-martinelli` | Exact by section: CLD25 §18.7 | D | Expand regular-sequence, extension-by-zero, and current identity steps. |
| 27 | `part2/ch18_delta_forms.tex:100` | theorem `thm:delta-preform-algebra` | Broad: GK17 §§1--3 | D | Expand stable intersection, refinement independence, Leibniz, and pullback range. |
| 28 | `part2/ch18_delta_forms.tex:120` | proposition `prop:tropical-delta-pl` | Exact: GK17 Theorem 3.16 and Corollary 3.19 | D | Supply the facewise Hessian/corner-current proof. |
| 29 | `part2/ch18_delta_forms.tex:165` | theorem `thm:gk-poincare-lelong` | Exact: GK17 Theorem 7.2 | D | Expand the delta-form proof; retain the established title. |
| 30 | `part2/ch18_delta_forms.tex:205` | theorem `thm:gk-delta-cl-measure` | Exact: GK17 Theorem 10.5 | D | Expand the Chern delta-form/model-intersection comparison. |
| 31 | `part2/ch18_delta_forms.tex:240` | theorem `thm:gk-tropical-frame-positivity` | Exact: GK19 Theorem 8.4 | D | Expand Hessian versus corner-effectivity equivalence. |
| 32 | `part2/ch18_delta_forms.tex:253` | theorem `thm:gk-formal-positivity-comparison` | Exact: GK19 Theorem 6.10 and Proposition 7.2 | D | Expand model nefness, functorial positivity, and approximation equivalence. |
| 33 | `part2/ch18_delta_forms.tex:314` | theorem `thm:harmonic-balancing` | Exact: GJR26 Theorem 9.7 | D | Expand Stokes, wall cancellation, and the boundary qualification. |
| 34 | `part2/ch18_delta_forms.tex:387` | theorem `thm:gr-pl-curve-test` | Exact: GR25PL Theorems 5.3 and 5.6; GM19 gives context | D | Expand the curve-lifting and residue-nef detection proof. |
| 35 | `part2/ch18_delta_forms.tex:415` | theorem `thm:gr-classical-pl` | Exact: GR25Classical Theorem 4.3; adjacent prose also anchors §1.2 and Wanner 4.7 | D | Expand the curve-test/model-semipositivity equivalence without importing R3-24's extra arrow. |
| 36 | `part2/ch19_cld_examples.tex:95` | theorem `thm:wanner-curve-comparison` | Exact: Wanner Corollaries 4.8, 5.1, 5.4 and GJR26 Theorem 15.11 | D | Expand the comparison and keep the smaller regularization scopes separate. |
| 37 | `part2/ch19_cld_examples.tex:156` | theorem `thm:toric-positivity` | Exact: GK19 Proposition 8.13/Corollary 8.14 and BGJKK25 Theorem 5.3.11 | D | Expand sign conversion, convexity, and formal/continuous boundaries. |
| 38 | `part2/ch19_cld_examples.tex:284` | theorem `thm:abelian-harmonic-tropicalization` | Exact: GJR26 Proposition 16.2 and BGJKK25 Proposition 7.4.5 | D | Expand the rigidified-line-bundle argument and state the good-reduction factor. |
| 39 | `part3/ch23_bfj_envelopes.tex:302` | theorem `thm:bfj-envelope-regularity` | Exact and visibly imported: BFJ16 Theorem 8.3; reduction is dispersed through following subsections | D | Finish the promised reconstruction and place it in a proof environment with the global-generation input marked imported. |
| 40 | `part3/ch23_bfj_envelopes.tex:426` | theorem `thm:ch23-base-ideal-approximation` | Exact and visibly imported: BFJ16 Theorem 8.5; proof mechanism follows in prose | D | Convert the mechanism into a complete proof and isolate the imported multiplier-ideal theorem. |
| 41 | `part3/ch29_continuity.tex:187` | theorem `thm:curves-arbitrary-field-continuity` | Inadequate: only a general Thuillier/slope outline; `GJKM19` is cited for a different higher-dimensional warning | D | Locate exact curve sources for envelope continuity and MA solvability and expand the graph proof. |
| 42 | `part3/ch29_continuity.tex:209` | theorem `thm:gjkm-positive-characteristic-cy` | Exact: GJKM19 Theorems 1.4, 1.5, and 9.3 | D | Expand the test-ideal/variational chain with resolution dependencies visible. |
| 43 | `part3/ch29_continuity.tex:234` | theorem `thm:fgk-mixed-characteristic-cy` | Exact: FGK25 Theorems 7.1 and 8.1 | D | Expand the envelope-continuity and variational reduction, retaining conditional resolution hypotheses. |
| 44 | `part3/ch29_continuity.tex:306` | proposition, unlabeled | No source: this is a three-part comparison/status summary and explicitly distinguishes separate completion theorems | R | Retype as a scope-ledger paragraph or table, with citations for each positive clause. |
| 45 | `part4/ch32_trivial_analytification.tex:187` | theorem `thm:triv-divisorial-density` | Partial and remote: chapter source note cites BJ22 §1, but no exact theorem number is attached here | D | Add the exact density anchor and expand the net approximation, including proper-support limits. |
| 46 | `part4/ch36_envelopes_history.tex:250` | theorem `thm:bj22-nef-envelope` | Partial and remote: source note gives BJ22 §5, without a theorem number | D | Add the exact BJ theorem and expand or explicitly import each multiplier/test-ideal input. |
| 47 | `part4/ch36_envelopes_history.tex:265` | theorem `thm:bj-addendum-all-classes` | Partial and remote: generic BJ22b citation; reduction sketch follows | D | Add the exact addendum theorem and complete the PL-obstacle/decreasing-regularization proof. |
| 48 | `part4/ch37_envelope_statement.tex:56` | theorem `thm:bj-final-envelope` | Provenance only: supplied archive named in the source note; proof is promised across Chapters 38--45 but no proof environment closes this statement | B | Add an explicit proof assembling and citing each later numbered result, or relocate the theorem to the assembly chapter where its proof can close. |
| 49 | `part4/ch42_alterations.tex:53` | theorem `thm:bj-de-jong-input` | Exact: de Jong 1996, Theorem 4.1; properness argument follows | D | Expand the alteration theorem to the exact used case and retain the imported source marker. |
| 50 | `part4/ch49_linear_growth.tex:323` | theorem `thm:bj-toric-psh-convex` | Partial and remote: source note cites BJ22 Appendix B, but no adjacent anchor or proof | D | Add the exact Appendix-B proposition and expand the convex/psh and Legendre bijections. |
| 51 | `part6/ch66_hybrid_spaces.tex:380` | theorem `thm:hybrid-volume-forms` | Partial: cites BJ17Hybrid only for hypotheses, with no theorem number; a cautionary remark follows instead of proof | D | Give the exact hybrid-volume theorem and expand normalization, skeletal support, and residual coefficients. |

### Appendix queue

| # | File:line | Environment / label | Source-prose status | Class | Action |
|---:|---|---|---|:---:|---|
| 52 | `appendices/appD_convexity.tex:319` | theorem `thm:appD-minkowski-polynomial` | Broad: Schneider Chapter 5; only the mixed-cell and Hausdorff-approximation mechanism is stated | D | Expand polytope polynomiality and the approximation proof, importing only the precise mixed-volume input. |
| 53 | `appendices/appD_convexity.tex:340` | theorem `thm:appD-af` | Exact: Schneider Theorem 7.3.1; the degenerate perturbation step alone is given | D | Mark Alexandrov--Fenchel as imported with the exact anchor and prove the extension to degenerate bodies. |
| 54 | `appendices/appD_convexity.tex:395` | theorem `thm:appD-alexandrov-measure` | Section-level: Rockafellar §§23--25; countable additivity, the smooth formula, and weak continuity are only sketched | D | Expand all three assertions and isolate the imported convex-analysis inputs. |
| 55 | `appendices/appD_convexity.tex:567` | theorem `thm:appD-support-current-mixed-volume` | Section-level: Berndtsson §§5--6, 10; equal-body and polarization sketches are given with a sign-convention warning | D | Complete the polarization/sign proof and mark the strong-current construction imported. |
| 56 | `appendices/appF_intersection_bdivisors.tex:399` | theorem `thm:appF-df-nef-intersection` | Broad: generic `DF20`; the approximation/negativity/compactness ingredients are named but not numbered | D | Add exact DF theorem numbers and reconstruct the product and its four continuity/monotonicity properties. |
| 57 | `appendices/appG_tropical_algebra.tex:527` | theorem `thm:appG-analytic-calibration` | Broad: CLD25 §§12--15; no numbered anchor or proof beyond scope cautions | D | Add exact balancing/calibration anchors and expand compatibility with products and projections. |
| 58 | `appendices/appH_complex_reference.tex:152` | theorem `thm:appH-npp-ledger` | Broad: BEGZ10 for deep monotonicity; the other clauses and bimeromorphic invariance lack adjacent exact anchors | D | Split the ledger into sourced inputs and prove the formal clauses; mark the mass theorem imported exactly. |
| 59 | `appendices/appH_complex_reference.tex:187` | proposition `prop:appH-safe-continuity` | Mixed internal/unsourced scope ledger; item 1 points to a later proposition, item 2 invokes an unspecified strong-convergence theorem, and item 3 is a warning | R | Retype as a sourced scope ledger rather than one proposition. |
| 60 | `appendices/appH_complex_reference.tex:266` | proposition `prop:appH-energy-formulas` | Remote broad citations to Darvas/DDNL/Xia; no proof of extension from bounded difference or first variation | D | Add exact primary anchors and expand truncation, cocycle, and first-variation arguments. |
| 61 | `appendices/appH_complex_reference.tex:334` | theorem `thm:appH-comparison` | No adjacent citation or proof; only a mass-domain warning follows | D | Add the precise relative-comparison source and reproduce the truncation/full-mass proof. |
| 62 | `appendices/appH_complex_reference.tex:369` | theorem `thm:appH-p-projection` | No adjacent source; only positive-mass and zero-mass scope prose follows | D | Add the exact model-envelope projection theorem and expand idempotence, mass, and maximality. |
| 63 | `appendices/appH_complex_reference.tex:393` | theorem `thm:appH-i-projection` | No adjacent exact source; only the analytic-singularity log-resolution mechanism is sketched | D | Source and prove each ideal-envelope identity, separating the log-resolution special case. |
| 64 | `appendices/appH_complex_reference.tex:442` | theorem `thm:appH-strong-openness` | No adjacent source at all; three distinct deep assertions are bundled | D | Add exact primary anchors for strong openness, valuative recovery, and ideal/divisorial-data equivalence, and separate their proofs. |
| 65 | `appendices/appH_complex_reference.tex:494` | theorem `thm:appH-weak-geodesic` | No adjacent source; only endpoint caveats follow | D | Add exact finite-energy geodesic sources and expand construction, energy affinity, metric speed, and HCMA. |
| 66 | `appendices/appH_complex_reference.tex:565` | theorem `thm:appH-rwn` | Broad: RWN14 and a chapter cross-reference; exact hypotheses and theorem number are absent | D | State the precise maximal test-curve/ray domain and expand both Legendre inversions and energy compatibility. |

## Counts and release order

| Class | Count |
|---|---:|
| E | 0 |
| D | 63 |
| R | 2 |
| B | 1 |

The 66 rows above are complete for the frozen scanner signature. The first
expansion pass should handle the `B` row and retype the two `R` rows. The `D`
queue should be processed chapterwise so that a shared deep input is expanded
once and later statements cite the fully proved in-book version.

At this snapshot Chapter 71 has no theorem, lemma, proposition, corollary, or
exercise environment; it has 17 explicitly open `problem` environments. A
fresh global literal scan finds no remaining `exercise` environment.

**23 August editorial note.**  The preceding sentence is retained as part of
the frozen 14 August scan.  The live research-frontier chapter is now Chapter
72 and has 21 `problem` environments.  The book-wide literal count is 22
because the preceding pseudoeffective MP--DXZ chapter contains one separate
projective-rational full-link problem.  The former trace-refinement
environment was removed after the complete source proved the \(P\)-valued
trace theorem, and was replaced by Wu's genuine affine-cone finite-energy
equation problem.  The remaining environments are research-status records, not
exercises; no claim about a Rethlas attempt follows from their addition.

## Post-freeze live reconciliation

After the Chapter 1--23 and Appendix H proof-expansion passes settled, the
same scanner was rerun on the live included tree.  It finds **11** residual
items, all class `D`; the former `B` and `R` items and every elementary item
have been resolved.  This reconciliation does not erase the frozen 66-item
queue above, which remains the requested expansion record.

| File:line | Environment / label |
|---|---|
| `part4/ch36_envelopes_history.tex:250` | theorem `thm:bj22-nef-envelope` |
| `part4/ch36_envelopes_history.tex:265` | theorem `thm:bj-addendum-all-classes` |
| `part4/ch42_alterations.tex:53` | theorem `thm:bj-de-jong-input` |
| `part4/ch49_linear_growth.tex:323` | theorem `thm:bj-toric-psh-convex` |
| `part6/ch66_hybrid_spaces.tex:380` | theorem `thm:hybrid-volume-forms` |
| `appendices/appD_convexity.tex:319` | theorem `thm:appD-minkowski-polynomial` |
| `appendices/appD_convexity.tex:340` | theorem `thm:appD-af` |
| `appendices/appD_convexity.tex:395` | theorem `thm:appD-alexandrov-measure` |
| `appendices/appD_convexity.tex:567` | theorem `thm:appD-support-current-mixed-volume` |
| `appendices/appF_intersection_bdivisors.tex:399` | theorem `thm:appF-df-nef-intersection` |
| `appendices/appG_tropical_algebra.tex:527` | theorem `thm:appG-analytic-calibration` |

The live reconciliation counted 622 theorem/lemma/proposition/corollary
environments in total.  Its mechanical signature is unchanged: a row is
selected only when no `proof` environment occurs before the next
theorem-like statement or section/chapter boundary.  These 11 deep imported
statements are therefore the remaining expansion queue under the binding
full-proof presentation rule.

## Definitive live reconciliation (15 August 2026)

After the chapterwise hostile audits and the appendix proof pass were
integrated, the identical scanner was run once more on every TeX source in
`manuscript/`.  The live tree contains **645** theorem, lemma, proposition,
and corollary environments and **650** proof environments.  The scanner finds
**zero** theorem-like statements without a proof before the next
theorem-like or sectional boundary.  The five additional proofs are second
proofs, definition-level clarifications, or independent proofs of an already
stated result; they are not substitutes for missing statement proofs.

The same live snapshot contains no `exercise` environment, no placeholder
such as `proof omitted`, `left to the reader`, `TODO`, `FIXME`, or `TBD`, and
no empty proof environment.  Deep foundational inputs remain visibly
isolated and precisely sourced inside their proofs; the local deductions from
those inputs are written out in full.  Thus the former 11-row residual queue
is closed.  The 66-row historical inventory above is retained as an audit
trail rather than silently rewritten.

## Post-expansion mechanical reconciliation (22 August 2026)

The 15 August totals are historical, not totals for the expanded source tree.
The reproducible static scan of the live numbered chapters and appendices now
finds **1,770** theorem/lemma/proposition/corollary environments and **1,806**
proof environments. Using the same adjacency signature as above, it finds
**zero** theorem-like statements without a proof before the next theorem-like
or sectional boundary. Literal scans also find **zero** `exercise`
environments and zero occurrences of `proof omitted`, `left to the reader`,
`TODO`, `FIXME`, or `TBD`.

The live research-status count is **22** `problem` environments: one in
Chapter 71 and 21 in Chapter 72. They are not proof obligations or reader
exercises. The final-chapters source audit confirms that all 22 retain a
genuinely open residual scope.

This is a mechanical presentation check only. It does **not** certify every
expanded proof mathematically or source-audit every chapter, and it does not
replace the pending whole-book build or Rethlas receipts. In particular, the
22 August repair of `thm:bj-basic-closure` is source-audited but awaits an
exact-current-text Rethlas review; the stale `R3-BFJ-SKEL-01` receipt also
awaits re-audit.

## Final live structural reconciliation (23 August 2026)

After the Part IV--VI proof-depth passes, the same scan was rerun on all 95
sources compiled by `book.tex`.  The live tree contains **1,774** theorem,
lemma, proposition, and corollary environments and **1,810** proof
environments.  It finds **zero** structurally unproved theorem-like
statements, **zero** empty proofs, **zero** optional conventional names on
formal statements, and **zero** exercise environments.  All 72 numbered
chapters contain at least one example.

The larger proof count is legitimate: some results have a second proof, and
some proof environments justify definition-level or imported-boundary
claims.  The scan also finds 38 explicit phrases such as `not proved here` or
`without proof`.  Each occurs at a visibly delimited deep-source firewall
with a precise citation; none substitutes for an empty local deduction.

This remains a structural presentation audit, not a semantic certificate.
In particular, Chapter 35 now records that the strict homogeneous Siu
division is proved internally while the critical endpoint remains an
imported theorem.  The separate attempted repair and counterexample to one
published proof step are quarantined in a Rethlas packet and are not part of
the main text.  The pending exact-current Rethlas receipts listed in
`rethlas_verified_results.md` therefore remained release gates at that
snapshot.

## Exact-current reconciliation (24 August 2026)

The identical live-source scan now finds **1,785** theorem, lemma,
proposition, corollary, or claim environments and **1,821** proof
environments.  It finds zero theorem-like statement without a proof before
the next theorem-like or sectional boundary, zero empty proof environment,
zero optional parenthetical name on a formal statement, and zero exercise
environment.  The excess proof environments are second proofs and proofs of
definition-level or explicitly imported-boundary claims; they are not used to
mask a missing statement proof.

The exact-current production status also changed after the 23 August
snapshot.  The Chapter 23 fixed-skeleton block passed run
`20260824T044830Z_25024c43d265`; the Chapter 49
statement-proof-sharpness package passed run
`20260824T041218Z_0c95825dbb06`; the Chapter 55 toric zero-mass block passed
source-attested run `20260824T052605Z_703e3b501202`; the current Chapter 55
metric theorem and line-bundle specialization passed separate runs
`20260824T054849Z_57635bfa07f4` and
`20260824T061508Z_17bf73c6b37c`; and the current Chapter 69 toric-dimension
block passed run `20260824T070302Z_d706dc98ccca`.  Every one of these six
runs used `gpt-5.6-sol` at `xhigh` and returned final `correct`, zero critical
errors, and zero gaps.

These gates do not convert the BJ22 basic-closure integration into a Rethlas
receipt; that integration remains a precisely delimited source import.  They
also do not promote the pending MP reduced entropy-slope reconstruction.  The
current structural proof scan is complete.  The separate clean whole-book
build of the exact 101-file release snapshot has also passed; its artifact and
log evidence are recorded in `output/BUILD_AND_AUDIT_SUMMARY.md`.
