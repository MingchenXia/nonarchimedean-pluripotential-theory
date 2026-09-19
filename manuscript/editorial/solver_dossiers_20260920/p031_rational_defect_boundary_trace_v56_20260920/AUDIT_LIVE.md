# P03.1 v56 local hostile audit

Date: 2026-09-20

Baseline commit: e07f3e2f1bd13bc5a72f6219d760408e935f25e6

## Result under audit

The live insertion proves four strict partial advances for the rational
globalization defect profile
\[
g_v=v-s_{\mathbf Q,X}.
\]

1. On every relatively compact ordinary open domain with nonempty boundary,
   the supremum of the positive defect is exactly the maximum of its positive
   interior upper trace on the actual boundary.
2. The pointwise positive defect is exactly the supremal height of a connected
   superlevel carrier whose closure reaches that boundary.  Taking the
   supremum over local rational competitors gives the complete rational
   globalization defect.
3. Vanishing of the rational defect on an open set is equivalent to zero
   positive boundary trace for every relatively compact local rational
   competitor there.
4. Finite flat pullback preserves the trace at every boundary lift.  Each
   compact truncated carrier pulls back to at most as many connected
   components as there are points in one central fiber, and every component
   is anchored in that fiber.

This does not settle P03.1.  It supplies an exact numerical signature and a
finite-flat branch bound for any surviving obstruction.  The active inventory
therefore remains at 46 atomic questions in 14 formal problem environments.

## Dependency and proof audit

- The boundary maximum identity uses only the v55 coherent-carrier result and
  the existence of a global rational minorant.  The minorant bounds the trace
  on the compact closure; no sequential compactness or first-countability
  assertion is used.
- The trace is defined by an infimum over ordinary neighborhoods.  Its strict
  upper level complements are open, so it is upper semicontinuous on the
  compact boundary and attains its maximum.
- For every interior point and every level below its positive defect, the v55
  carrier reaches the boundary.  Evaluating the neighborhood trace at an
  accumulation point and increasing the level proves the reverse maximum
  inequality.
- The end-height formula does not require the top level itself to reach the
  boundary: all strict lower levels do, and their supremum is the pointwise
  defect.
- The open-set converse first shrinks an arbitrary local competitor to a
  relatively compact domain with nonempty boundary.  The trace formula then
  bounds its value at the chosen point by the global rational envelope.
- For the proper-open component lemma, the inverse image of the compact
  connected carrier is compact Hausdorff.  Components equal
  quasi-components there.  If one component avoided the finite anchor fiber,
  finitely many clopen separators would give a nonempty proper clopen image in
  the connected base.  This avoids all metric, path-lifting, and local
  connectedness assumptions.
- Openness of a finite flat analytic morphism gives both the reverse closure
  inclusion and the neighborhood comparison needed for exact trace pullback.
  Properness makes the pulled-back carrier compact.  Applying the component
  lemma anchors every component and yields the fiber-cardinality bound.

## Skill-hypothesis ledger

- The `proper-open-chain-component-anchor` research card was inspected.  Its
  metric-chain proof is not available for a general nonmetrizable Berkovich
  space, so no chain argument was imported.  The manuscript instead uses the
  compact-Hausdorff quasi-component separation already proved in v54.
- The `boundary-curve-envelope-escape` card was also inspected.  Its complex
  envelope extension, global Stein curve slicing, interpolation, and lifting
  hypotheses are absent here.  It was treated as a non-trigger and no theorem
  from that card was imported.
- The `mingchen-writing` second pass made the possibly disconnected pullback
  trace definition explicit and removed two optional-proof-title spacing
  defects found in the rendered PDF.

## Verdict

PASS as a local, source-aware, dependency-closed partial advance.  The exact
statement and proof pass the strict writing audit with zero errors and zero
warnings.  The full build, reference audit, inventory audit, log scan, and
visual inspection pass.  No model-backed verifier was used for this version.
