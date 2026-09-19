# P03.1 v59 local hostile audit

Date: 2026-09-20

Baseline commit: `cc4a7c4d3040f3be7d2c953a90c9d70ab470b975`

## Result under audit

The live insertion isolates the canonical scalar-extension range of the
persistent terminal-anchor problem.

1. A continuous section makes the projection open at every point of the
   section image and makes usc regularization commute with pullback at those
   points.
2. For every decreasing family of connected base sets, the component through
   a section-selected endpoint contains the section of the whole base set,
   maps onto that set, and contains the explicit common anchor `sigma(x)`.
3. Over an algebraically closed complete non-Archimedean field, Poineau's
   universal-point theorem supplies exactly such a continuous canonical
   section for every analytic scalar extension.
4. The rooted terminal carriers from v57 therefore have a canonical persistent
   root anchor even when scalar projection is not globally open.

This is a strict partial advance, not a solution of P03.1.  It controls the
component through the canonical endpoint lift, not components through every
point of the scalar fiber.  It proves neither fiberwise constancy of the
regularized envelope nor compatibility of the analytic defect with scalar
extension.  The inventory therefore remains at 46 active atomic questions in
14 formal problem environments.

## Proof audit

- If `N` is a neighborhood of `sigma(z)`, continuity makes
  `sigma^{-1}(N)` a neighborhood of `z`, and the section identity places it
  inside `q(N)`.  This is pointwise openness and does not assert that `q(N)`
  is open as a set.
- Continuity of `q` gives the upper regularization inequality by using
  `q^{-1}(U)` for a base neighborhood `U`; pointwise openness gives the
  reverse inequality from every neighborhood `N` upstairs.
- For connected `K`, the set `sigma(K)` is connected, contains the selected
  endpoint, and lies in `q^{-1}(K)`.  Hence it lies in the selected component,
  and the section identity forces that component to map onto all of `K`.
- For a decreasing family, the later component is a connected subset of the
  earlier inverse image through the same endpoint.  Nesting follows from the
  maximality of connected components.
- Since every base set contains `x`, every selected component contains the
  same explicit point `sigma(x)`.  No compactness or finite-intersection
  argument is needed.
- The scalar application uses only the four precisely cited Poineau items;
  the official PDF hash agrees with the earlier quarantined source audit.
- The v57 carrier closures meet all hypotheses.  Their compactness is true
  but deliberately unused in the section argument.

## Firewall audit

- The canonical section is continuous; it is not asserted to be analytic.
- Pointwise openness on the section image is not promoted to global openness.
- The result treats the canonical lift of the terminal endpoint, not an
  arbitrary lift.
- No psh functoriality, Shilov-boundary assertion, or scalar-fiber constancy is
  inferred.
- The finite-flat trace identity from v57 is not generalized.

## Skill scope

- The `proper-open-chain-component-anchor` card was inspected.  Its finite or
  discrete-fiber metric-chain theorem does not trigger here.  The live proof
  is the independent continuous-section argument above.
- The `mingchen-writing` pass keeps the imported source statement separate
  from the elementary topological deductions and states the remaining P03.1
  obstruction at each integration point.

## Verdict

PASS as a source-aware, dependency-closed partial advance, subject to the
full build, reference, inventory, log, and visual checks recorded in
`BUILD_REPORT_LIVE.md`.  No model-backed verifier was used for this version.
