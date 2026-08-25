# P21 four-punctured smooth-cross obstruction: live integration receipt

Date: 25 August 2026

## Controlling production verification

- Guarded run: `20260825T034743Z_ea6194f07e86`.
- Proof item: `pi_19c9aad210847a2875a0fe4a`.
- Model and scrutiny: `gpt-5.6-sol`, `xhigh`.
- Verdict: final `correct`, zero critical errors, zero gaps.
- Exact frozen statement SHA-256:
  `ea6194f07e869610c427c326311d7a0bea38ca15e8c0050e396d3c9b5b92a596`.
- Exact frozen source-aware proof SHA-256:
  `2426acd5e1662ed5aad826597b389884ef925c42258538c86184ab7dd7817a11`.
- Controlling production-receipt SHA-256:
  `3dc26b87d4fda3787f9f60df654418186a7f5d019f834627a86766e1ea60c4a0`.

The three frozen hashes were recomputed immediately before integration and
matched the controlling receipt.  No frozen packet, response, guard,
verification, manifest, or production receipt was modified.

## Integrated mathematical scope

Chapter 69 now contains one unnamed proposition and its full proof.  On the
four-punctured smooth projective line with punctures in pairwise distinct
residue classes, the natural full-cross real-PL psh potentials have equal
CLD and delta curvature `4 delta_q`.  A third-unit refinement forces the
visible ray weights of a positive closed order-zero CLD current to be all
equal; the same conclusion holds for a positive closed delta-current whose
restriction to smooth test forms has those ray weights.  Thus the proposed
weights `(2,2,1,1)` are impossible on this concrete candidate.

The integration does **not** classify currents on arbitrary connected
analytic curves, prove a global constant-calibration theorem, treat
higher-dimensional or non-PL candidates, or solve `P21.3`.  The Chapter 72
problem environment and atom remain present.  At this integration stage, the
inventory remained exactly 20 formal problems / 61 active atoms.  No novelty
or priority claim is made.  For arbitrary continuous multipliers in the
delta-current branch, Chapter 72 explicitly retains the product-legality
firewall.

## Live files and SHA-256 values

| File | SHA-256 |
|---|---|
| `../../../RESEARCH_QUESTION_LEDGER.md` | `78a14cc2c31a9888fb2c847682d02551d5f2fa21e8a703299fe692d55dee676c` |
| `../../parts/part6/ch69_verified_extensions.tex` | `d0aa7f22017966b4b463cfb427b8122de5b6be49d3e38dc3ce7801cd143e2eec` |
| `../../parts/part6/ch72_major_open_problems.tex` | `e5baef15ffbfea8298e8ab507fe2e330031188cadf956810bf3896759c67c9ac` |
| `../major_open_problem_program.md` | `668b3249371aaed893119d096d41e5ca64e84800044431f1afef2a2f52cc3311` |
| `../open_problem_atomic_inventory_20260824.md` | `29c8e192886a8b0e0163dcf862c254b2111a152ef8f84972357a2206961d4039` |
| `../rethlas_verified_results.md` | `cedc28ebd57864b9ca683621c70b48f76a72e99b394d5a715291e97bc5d47bc4` |
| `../theorem_provenance.md` | `ec38bf164d9179d8096461357e0eb37eb9a908202f173ceabaaa001c7fc5c58d` |
| `../../appendices/appL_provenance.tex` | `a843e900d4e48cfaf3000e6c6c2d18682691095c3f2d6e4538233414ba194a8f` |
| `../solver_dossiers_20260825/p21_upstairs_cross_curve_obstruction_dossier_20260825.md` | `f366a7e4748f2c9a12f939aedff5b8ef3de501199d947d4701a4cc66cca8abac` |

The live theorem is a house-style rendering of the exact frozen packet, not
a claim of post-integration byte identity.  It uses `cref`/`eqref`, the
book's upright differential macros, and no conventional theorem name.

## Static and focused-build checks

- `git diff --check`: passed.
- The proposition label, scope-remark label, and eight new equation labels
  each occur exactly once in the manuscript.
- The Chapter 72 problem and `P21.3` inventory atom remain present.
- At this integration stage, the `20/61` counts remained unchanged.
- Focused `latexmk -pdf -interaction=nonstopmode -halt-on-error` build of
  Chapters 69 and 72 together with Appendix L: exit code `0`, 87 pages.
- Focused PDF SHA-256:
  `e454b413779d00dd90e6f28f19a6cc4d9e39e123fd9f012451c12e323f4b5089`.
- Focused log SHA-256:
  `4660228a78ff741a6260f77a5860c8d651226decb8824a34f54832bafb30b73c`.
- The log contains no TeX error, fatal error, emergency stop, duplicate
  label, duplicate destination, or unresolved reference to a label
  introduced by this integration.  The slice omits most chapters and hence
  reports unrelated unresolved external cross-references.

Nine existing live/editorial files were updated, and this integration
receipt was added.  The mathematical insertion consists of one proposition,
one complete proof, one scope remark, and eight numbered equations; no open
problem or atomic inventory entry was removed.
