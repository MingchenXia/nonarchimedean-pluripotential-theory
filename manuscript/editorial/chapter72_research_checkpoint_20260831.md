# Chapter 72 research checkpoint — 31 August 2026

This checkpoint records the continuation requested specifically for Chapter 72. It is not a theorem-acceptance record. The active inventory remains **51 atoms**: no candidate below has been retired from it. The independent mathematical audit and the production Rethlas review are distinct requirements; an independent PASS is not a production receipt, formal verification, peer review, or a priority claim.

## Results and present status

| Target | Concrete progress | Current limitation |
| --- | --- | --- |
| P14.2: upper semicontinuity of the raw ideal-valuative DXZ transform | Full-scope proof, dense-parameter formula, and an explicit decreasing sequence of bounded continuous finite-ideal expressions; independent exact-byte mathematical audit PASS. | Production Rethlas review remains pending. The approximants are not asserted to be MP-psh. |
| P14.7: maximality of filtration test curves | Complete candidate proof in the full strict-interior big-line-bundle setting, with a separately stated terminal-left-limit corollary; independent exact-byte mathematical audit PASS. | Production review is pending. A newer preprint already covers the same conclusion as a deduction, so no novelty claim is appropriate. |
| P21.3: higher-dimensional Bedford–Taylor independence | Three precise diagnostics/lemmas recorded, including obstructions to common-measure and ordinary-sheet shortcuts. | No full scalar-rigidity proof and no noncanonical analytic current were obtained. The higher-dimensional target remains open. |
| P14.3: MP positivity / realization | Follow-up investigation of dominated divisorial approximation and the MP divisorial comparison theorem. | Research route only. Ordinary density does not justify a dominated approximation, and no unrestricted MP realization is claimed. |

The other Chapter 72 atoms are unchanged. In particular no general envelope theorem over nontrivially valued fields, general CLD regularization theorem, or general zero-mass reconstruction theorem has been proved in this continuation.

## P14.2: precise mathematical content

Let a family of nonnegative extended-real lower semicontinuous functions \(a_\tau\), indexed by \(\tau<c\) for a finite real \(c\), increase with \(\tau\). On an arbitrary topological space,
\[
F=\sup_{\tau<c}(\tau-a_\tau)
\]
is upper semicontinuous. The proof uses finite left-endpoint meshes and a finite lower truncation, not the generally false assertion that a supremum of upper semicontinuous functions is upper semicontinuous. It treats \(F=-\infty\) and does not evaluate the family at the endpoint.

For decreasing quasi-psh levels on any complex manifold, take
\[
a_\tau(v)=\sup_{m\geq1}m^{-1}v\bigl(\mathcal I(m\Gamma_\tau)\bigr).
\]
Analytic multiplier-ideal subadditivity and the ideal-evaluation topology supply all hypotheses, including infinite ideal values. No projectivity, finite energy, or positive background class is required for this topological assertion. In the DXZ inverse system, the equality of every multiplier ideal under transition makes both the transform and the explicit continuous approximating sequence independent of the chosen perturbation component. Thus the application includes arbitrary real pseudoeffective classes on connected compact Kähler manifolds, including zero-volume classes.

The continuous expressions use negative ideal evaluations, translations, positive rational rescaling, and finite minima/maxima. A finite lower floor removes infinite negative values. Their positivity is not proved and must not be inferred from their continuity or piecewise-linear character. The example on \(\mathbf P^1\) checks the floor in the multiplier ideal and the semivaluation supported at a point without using \(0\cdot\infty\).

Frozen directory: `solver_dossiers_20260831/p142_raw_transform_usc_research_20260831`.

- Statement SHA-256: `488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949`.
- Proof SHA-256: `bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21`.
- Example SHA-256: `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f`.
- Manifest SHA-256: `c677e7a289d9b957d2269cb7b68da4dfcfa89faa4a761a15e8fd8b6dc65e5a87` (20 entries).
- Independent report: `p142_raw_transform_usc_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md`, SHA-256 `29464ed02a022362b2564b2392e8fc457ec9deffe14f6771250ef56792f4f084`.

The author and independent read-only checks agree on all frozen entries, seven historical parent inputs, fourteen internal labels, three imported labels, and four bibliography keys. The successful standalone draft-mode build has no warnings and produces no PDF. This is not a full-book build or visual-review claim.

## P14.7: proof and attribution

The candidate proves the fixed-degree estimate \(P_\theta[u_m]\leq u_W\) whenever \(W_m\) defines a birational map. It resolves the base ideal, identifies the residual obstacle, quantizes smooth approximations to that extended-real obstacle using Berman's big-line-bundle theorem, and returns complete sections to the original graded series using a fixed conductor section. The fixed degree and norm costs are retained until the final limit. No finite generation of the full filtered ring, normality of the projective image, or generic-finiteness substitute for birationality is assumed.

DXZ Lemma 4.5 already supplies the ordinary-envelope / multiplier-ideal-envelope identity. The missing function-level equality is supplied by the candidate estimate and the increasing dyadic-envelope identity. A separate monotonicity argument treats the particular left-limit terminal slice. That terminal assertion is not arbitrary zero-mass recovery.

Frozen directory: `solver_dossiers_20260831/p147_filtration_maximality_research_20260831`.

- Statement SHA-256: `d6fca037467563e9af28d2ca97917eb1d2f5697c0b36d36f6a6217439bdd444c`.
- Proof SHA-256: `865717efa134e64f113ccf3b57a339b657059bc2b0ee7368ee5b70dd9872a362`.
- Manifest SHA-256: `3ffa1f46f96ce438bf46dd0159cd036f10e79437c1b242a688359b53d652b7fb` (12 entries).

The author reports a clean eight-page standalone draft-mode assembly and 2,436 monomial diagnostic checks; these are assembly/example checks, not a substitute for the independent proof audit. No PDF was generated. The independent reviewer checked the complete proof, all twelve manifest entries, six historical inputs, nineteen labels, twelve references, six bibliography keys, and all 2,436 arithmetic cases. The root reran both independent read-only packet checkers successfully before any later source-only edits.

The independent report is `p147_filtration_maximality_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md`, SHA-256 `85b6399d9f62b44cdcc7f507419b445eb589cf3f0bc5ad532277842910b8f75a`. It explains the ordinary-model closure prerequisite behind DXZ's compressed dyadic argument; the argument does not assume the desired raw maximality. The audit does not independently endorse a priority claim or the separate Finski comparison.

The separate `p147_filtration_maximality_literature_status_20260831/LITERATURE_STATUS_ADDENDUM.md` identifies the relationship with [Finski, arXiv:2603.22194v1, Theorem 4.3](https://arxiv.org/html/2603.22194v1). The source does not literally state a named DXZ-maximality theorem. Its approximation statement, a birational residual-envelope identification, and DXZ Lemma 4.5 yield the same interior conclusion. The appropriate provisional classification is a detailed independent proof of a deduction covered by a newer preprint, not a new solution of an untouched conjecture. This attribution is separate from checking the candidate proof's correctness.

The old 15 August research dossier is retained as history, not an accepted proof. Source corrections concerning ordinary versus multiplier-ideal maximality, the \(1/m\) squared-norm normalization, the actual positive-mass strict interior, and the sign of an exceptional divisor are being independently checked. P14.8 must be formulated separately and must not be retired by silently replacing it with the particular terminal-left-limit assertion.

## P21.3: what was and was not achieved

The frozen `p213_calibrated_chart_rigidity_research_20260831/OBSTRUCTION_NOTE.md` proves three bounded statements:

1. On \((\mathbf A^1\times\mathbf G_m)^{\mathrm{an}}\) over \(\mathbf C((\pi))\), the positive coefficient measures of all compactly supported canonical top forms need not admit one common dominating Radon measure. This holds already for the canonical current and is not a counterexample to scalar rigidity.
2. A finite étale power map can have a single Gauss fibre point of nontrivial residue degree. Finite étale degree cannot be replaced by a count of ordinary-open sheets.
3. A finite-valued positive functional on divisors of a regular proper integral curve, vanishing on principal divisors, is a nonnegative multiple of degree. The proof uses Riemann–Roch for both positive and negative multiples of a degree-zero divisor.

The remaining step is analytic: construct the residual divisor-functional relations with the correct weights on individual source sheets under arbitrary chart refinements, and propagate them through all relevant cells and flags. No such general construction was obtained. No actual noncanonical compatible family was constructed either.

Note SHA-256: `b27c56591db85bfef79e8e34b47637a06bd7df8f9d065b46b5303c64cfd61b86`; manifest SHA-256: `a27d1042cf1426de4c28146994a84dac816fa6ec88992cbfd4bfc9c28cc5ec4b` (15 entries). These research notes have not passed production review and are not promoted as live theorems.

## Integration map after the required gates

- P14.2 belongs immediately after the Chapter 71 raw-transform definition and perturbation-independence proof. Preserve existing equation labels and `eqref`; replace only the now-obsolete USC disclaimers after acceptance. Expand the finite-ideal approximation section with the explicit continuous sequence, retaining the warning about positivity. Then update the Chapter 72 discussion and retire only P14.2.
- P14.7 belongs beside the filtered-series/test-curve construction, with the conductor and norm calculation included in full. Credit DXZ's existing envelope identity and the newer Finski connection explicitly. Change Chapter 72 and the atomic inventory only after proof and literature-status checks are complete and production review has passed.
- P21.3 remains in the active queue. Its diagnostics can guide further research, but no full-current, ordinary-neighborhood, or higher-bidegree conclusion follows.

The production permission/review gate has not been resolved in this continuation. No alternate endpoint, delegated submission, weaker verifier, or reused receipt has been substituted. Work can continue on source checks, independent mathematics, exact-byte preservation, and genuinely separate open questions while that gate remains pending.

## Preservation already completed

The earlier foundational-repair checkpoint was copied byte-for-byte to the durable local project and committed as `864bf35` on the existing private repository. Its 285 explicitly selected paths contain source candidates, audits, retained build evidence, and the preface's verification warning; no mathematical candidate was promoted. The normal, non-force push to `origin/main` completed successfully. The newer Chapter 72 packets described above are separate from that commit and will be preserved in their own checkpoint.
