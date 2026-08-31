# Chapter 72 comparison follow-up — 31 August 2026

This follows the separately frozen `chapter72_research_checkpoint_20260831.md`.
It records research and source corrections, not acceptance of new theorems.
The inventory still contains **51 administratively active entries** in
14 problem environments. In particular, this is not a claim of 51 untouched,
precisely formulated conjectures in the current literature: P14.7 remains in
the project's verification queue, while P14.8 needs a precise formulation.

## Mathematical progress

1. **Dominated divisorial approximation.** For every semivaluation v of the
   MP ideal spectrum of a connected compact Kähler manifold, rational
   divisorial q with q≤v on every coherent ideal approximate v. This includes
   proper support and infinite ideal values. A global monomial ideal and
   its coherent annihilator give the all-ideal inequality; ordinary density
   alone is not used to assert ordered density. No increasing net is claimed.
   The complete candidate and its finite-energy consequence passed fresh
   independent exact-byte audit.
2. **Full Kähler DXZ–MP comparison.** Combining dominated approximation with
   the independently audited raw-USC theorem identifies the raw transform
   at every semivaluation. Bounded truncations then give an order isomorphism
   of the entire Kähler cones, without finite-energy, rationality, or
   projectivity assumptions. The proof checks finite energy in the actual
   inverse system, decreasing completion, and the finite endpoint at the
   zero valuation. Its separate audit passes conditionally on the two
   topological inputs and the stated existing finite-energy correspondence.
3. **Nef boundary classes.** Conditional on that full Kähler comparison, the
   DXZ space of a nef class α is the intersection of the MP cones for
   α+ε[ω], ε>0, as actual functions. The proof explicitly reconstructs the
   compatible inverse-system components and proves independence of ω and
   the smooth representative. Nef non-big classes are included. This
   deduction has passed independent conditional audit. It does not identify
   the intersection with the fixed-nef-class model completion; only that
   completion's inclusion is proved.
4. **Arbitrary pseudoeffective classes at the function level.** A further
   frozen candidate embeds every pseudoeffective DXZ object into a sufficiently
   large Kähler class without changing its raw function. It identifies the
   global DXZ quasi-psh space with the union of the Kähler MP cones, and
   proves all-point translation, positive scaling, addition, maximum and
   decreasing-infimum formulas. This does not intrinsically characterize
   the image in each non-nef class or define its measure/energy theory.
   Its independent conditional audit has passed for the full displayed
   function-level scope, with all three new comparison inputs kept explicit.

Every new result and its new dependencies still require production Rethlas
review. Independent model audits, exact hashes and TeX builds are not formal
verification, peer review, or evidence of priority. No new mathematical
candidate has been inserted into the live theorem text in this follow-up.

## Exact candidate and audit anchors

All directories below are under `solver_dossiers_20260831/`.

| Packet | Frozen manifest SHA-256 | Independent report |
| --- | --- | --- |
| `p143_dominated_divisorial_research_20260831` | `c2da7ad2ecb958415835af56e906b2e89a76587a365686b7a79c38e67be1b5a7` | `p143_dominated_divisorial_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md`, SHA `6205fdb014e6364aa8d14fa6a3ec6313da9c16b585bccb9617415dd31474b1d2` |
| `p143_kahler_truncation_research_20260831` | `f5e70b72c09601f27d2210391d8f72935bc37564481be9a5818c19f8926c0b8b` | `p143_kahler_truncation_independent_audit_20260831/CONDITIONAL_AUDIT.md`, SHA `3bfe0d21e177b422282a64f6a6252729fe53dbffd6ca5a03d3021f134e687522` |
| `p143_nef_closure_research_20260831` | `8b03ba68f6a8a1e901d19befd9e832088481d371c936b1349603898317a0bb3b` | `p143_nef_closure_independent_audit_20260831/INDEPENDENT_CONDITIONAL_EXACT_BYTE_AUDIT.md`, SHA `c1814f2cf8c60b0f91cd2f5a330fe0f2d48971ba454bc56e14b37a4c1e1106dc` |
| `p14_pseff_all_point_operations_research_20260831` | `f42fd86160b4a719696d7b0acfec25e741cdfa06c3066a807f9d30a078871add` | `p14_pseff_all_point_operations_independent_audit_20260831/CONDITIONAL_AUDIT.md`, SHA `cf52f916ba1b501113454dcfd737d7c1759ed5c1ddff61d47662b5641f829341` |

The full Kähler auditor authored the dominated-density candidate and
explicitly assumes, rather than self-certifies, that geometric premise.
A different reviewer independently checked dominated density. The nef
auditor likewise explicitly assumes the full Kähler comparison. These
dependencies must remain explicit in any production packet and integration.
The operations auditor also authored the dominated-density premise and
explicitly assumes it; the operations audit does not replace its separate
independent geometric check. Root read all four complete reports and source
ledgers and reran their relevant exact-byte checks. The final Kähler and
operations draft logs each contain one nonblocking underfull bibliography
box; no error, undefined reference/citation, or overfull box remains. No PDF
was produced by any of these checks.

The full Kähler audit supplies the complete sup–mean estimate behind the
zero-valuation slope identity; include that estimate in the eventual
pedagogical proof. The dominated-density audit supplies the precise analytic
principalization locator and the local nonprojective Gauss/Lelong interface
from published DX22 Lemma 3.14. Do not cite the projective-only DXZ
Proposition 3.1 by itself as a full compact-Kähler theorem.

## Source correction actually applied

Only the source/status paragraph concerning P14.7/P14.8, its bibliography,
and the corresponding inventory wording were changed in the live sources.
The patch was first independently checked, then applied identically in the
temporary editing tree and durable local project.

- DXZ's strict-interior filtration levels all have positive mass.
- Their Lemma 4.5 already gives P[u]=P[u]_I; the historical conjecture asks
  for the additional raw equality u=P[u].
- The alleged second zero-mass interior interval was removed.
- P14.8 now records the missing data/class/normalization/equivalence choices
  instead of silently being replaced by a terminal-left-limit statement.
- The 2026 Finski preprint is cited. The editorial source audit identifies
  the maximality conclusion as a deduction from its stated approximation
  theorem, with an explicit resolved-envelope comparison. This is an
  attributed inference, not a claim that Finski states a theorem under the
  DXZ conjecture's name or that his proof has been independently verified.

Controlling source audit:
`p147_source_correction_independent_audit_20260831/SOURCE_CORRECTION_AUDIT.md`,
SHA `afa9420dc2ec5d3b029d5a60a4368093ded498ad0a85e0f43132dbbbd072260e`.
The exact staged text, second source/exposition review, original live
snapshots, before/after identities and standalone draft build are preserved
in `p147_live_source_correction_20260831`; its manifest SHA is
`f3d95e752a4013ea00d657ad799ba6556e772ecfebe87ce692e601c930ad2eea`.
The source-correction build has no warning or box defect and produces no PDF.
All 14 problem environments, 51 active identifiers and existing labels remain.

The original Chapter 72 and inventory bytes bound by earlier audits are
preserved in that source-correction directory. Their hashes remain valid
historical inputs. A later old checker reading the now-edited live path may
report drift; it must be pointed to or compared with the preserved original,
not used as a reason to rewrite a frozen receipt or pretend nothing changed.

## CLD work

The three bounded auxiliary results in the earlier P21.3 note have passed a
separate independent review: the absence of a common dominating Radon measure
for all coefficient measures, the Gauss-fibre obstruction to ordinary étale
sheet counting, and the positive divisor-functional lemma on a proper
regular curve. Their scope does not include full scalar rigidity or general
Bedford–Taylor independence.

Audit: `p213_auxiliary_obstructions_independent_audit_20260831/INDEPENDENT_AUXILIARY_AUDIT.md`,
SHA `8793e00d1c4f5635ab127e4584fac5c9761e6f6aecbe45aa3e5af31fb1aad1a2`.
The next active research step is the actual analytic construction of the
residual-curve functional in a product/good-reduction surface neighborhood.
No solution of the complete higher-dimensional P21.3 problem is claimed.

## Integration and remaining work

After all required gates, put dominated density with the ideal-spectrum
approximation theory, and the full Kähler/nef/function-level comparisons
beside the raw-transform and finite-energy bridge in Chapter 71. Include
the full proofs and their boundary examples, preserve existing equation
labels and `eqref`, and use `cref` for theorem/section references.
During pedagogical assembly use roman differential d and constants i/e;
in particular the nef candidate's smooth-factor display `e^{mh}` should be
typeset as `\mathrm e^{mh}`. This is a recorded notation correction for the
future integrated version, not an alteration of its frozen mathematical bytes.

The general non-nef intrinsic image, P-sensitive positivity/measure/energy
theory, zero-volume constructions, unrestricted CLD regularization and
higher-dimensional P21.3 remain outside these comparison results. No general
envelope theorem over nontrivially valued fields has been obtained here.

No production call or alternative permission workflow was used. The existing
production review gate remains pending. The book PDF has not been rebuilt
by this follow-up; the work consists of source corrections and isolated
candidate proofs/audits. The earlier commits `864bf35` and `2a6ddfe` were
already pushed normally to the existing private repository; the present
follow-up is preserved separately.
