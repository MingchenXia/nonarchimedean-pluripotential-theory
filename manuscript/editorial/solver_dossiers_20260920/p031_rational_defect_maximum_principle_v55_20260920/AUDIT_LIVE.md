# P03.1 v55 local hostile audit

Date: 2026-09-20

Baseline commit: 9f0c9ac3b6f268257ebbede0ec26562532ea105b

## Result under audit

The live insertion proves three statements for the rational globalization
defect profile
\[
g_v=v-s_{\mathbf Q,X}.
\]

1. The positive part satisfies the exact boundary maximum principle on every
   relatively compact ordinary open test domain with nonempty boundary.
2. Every truncated component supplied by the preceding escape theorem lies
   in one intrinsic connected superlevel component. That component crosses
   every smaller test boundary, is not relatively compact in its local
   domain, and accumulates on the boundary when the ambient closure is
   compact.
3. Positivity of the complete rational globalization defect is equivalent
   to the existence of such a non-relatively-compact connected
   positive-defect carrier.

This is a strict partial advance. It does not settle P03.1 and does not
change the open-problem count.

## Dependency and proof audit

- The preceding rational-defect escape theorem is the sole new mathematical
  input. The v55 statements do not feed back into that theorem, so there is
  no circularity.
- The family of global rational minorants is nonempty in the inherited
  setting. Its pointwise supremum is lower semicontinuous; hence \(g_v\) and
  \((g_v)_+\) are upper semicontinuous and attain maxima on the compact sets
  used in the proof.
- If the positive maximum is zero, the boundary equality is immediate. If a
  positive maximum is attained on the boundary, the reverse inequality is
  immediate. If it is attained in the interior, applying the escape theorem
  at every level below the maximum and letting the level increase proves the
  boundary equality.
- The intrinsic carrier contains every truncated component through the base
  point, so each smaller boundary crossing occurs inside that single carrier.
  No path-connectedness assertion is used.
- A connected component of a closed superlevel set is closed. If the
  intrinsic carrier were relatively compact, it would be compact.
- The exceptional possibility that the carrier equals its whole local domain
  is excluded: a compact open local domain is closed in the Hausdorff space
  \(X\), hence equals connected \(X\); then the local competitor is global,
  contradicting positive defect.
- Otherwise, local compactness and regularity give an ordinary open
  neighborhood of the compact carrier with compact closure inside the local
  domain while excluding one exterior point. Its boundary is nonempty by
  connectedness, contradicting the boundary-crossing property.
- When the local domain has compact closure, failure to meet its boundary
  would make the carrier relatively compact, giving the final accumulation
  statement.
- The converse in the end-carrier characterization uses only the definition
  of the local rational envelope. The boundaryless consequence uses the
  already proved nonnegative three-level defect ledger.

## Scope boundary

The remaining issue is not an isolated or scale-dependent positive defect.
It is the possible existence of a coherent connected positive-defect carrier
that reaches every surrounding collar. The manuscript proves no theorem
excluding all such carriers on normal or geometrically unibranch
higher-dimensional analytic spaces.

## Verdict

PASS as a local, source-independent, dependency-closed partial advance.
The exact live statement and proof pass the strict writing audit with zero
errors and zero warnings. The full build, cross-reference audit, inventory
audit, log scan, and visual inspection all pass. No model-backed verifier
was used for this version.
