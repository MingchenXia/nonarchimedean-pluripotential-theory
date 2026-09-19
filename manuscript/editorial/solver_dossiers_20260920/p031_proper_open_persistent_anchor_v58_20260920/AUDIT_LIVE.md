# P03.1 v58 local hostile audit

Date: 2026-09-20

Baseline commit: d29d33bc9d89bcd1c4eb7194bef6522906a0dc58

## Result under audit

The live insertion removes the finite-fiber hypothesis from the topological
anchor mechanism used for the rational globalization defect.

1. If a continuous proper open surjection of locally compact Hausdorff spaces
   is restricted over a nonempty compact connected set, every connected
   component of the inverse image maps onto the whole set.
2. For a decreasing linearly ordered family of such compact connected sets,
   the components through one fixed lifted endpoint are nested and share one
   point in any fixed fiber over their common intersection.
3. Applied to the terminal carriers from v57, every lifted terminal endpoint
   has a single root-fiber anchor valid at every strict defect level, even
   when the fiber is infinite or nondiscrete.

This is a strict partial advance, not a solution of P03.1.  The projection
arising from general scalar extension is not known here to be open, and the
finite-flat trace identity remains a separate analytic input.  The active
inventory therefore remains at 46 atomic questions in 14 formal problem
environments.

## Dependency and proof audit

- Properness makes the inverse image of the compact connected base set
  compact.  Hausdorffness makes it compact Hausdorff and makes images of
  compact subsets closed.
- The restriction of an open map to the inverse image of the base set is open:
  for `U = V ∩ p^{-1}(K)`, its image is `p(V) ∩ K`.
- In a compact Hausdorff space, a component is the intersection of its clopen
  neighborhoods.  If one component missed a fiber, compactness of that fiber
  would reduce the pointwise clopen separations to one clopen neighborhood of
  the component missing the entire fiber.
- The image of this clopen neighborhood would be nonempty, open, and compact,
  hence closed, while missing the chosen base point.  This contradicts
  connectedness of the base set.  Thus every component meets every fiber and
  maps onto the base set.
- The optional numerical component bound uses finiteness only after
  surjectivity: distinct components meet a chosen finite fiber in disjoint
  nonempty subsets.
- For a decreasing family, the component through the fixed endpoint at a
  higher index is a connected subset of the earlier inverse image, so it lies
  in the earlier component.  Intersecting these components with one fixed
  compact fiber gives a decreasing family of nonempty compact sets.
- Any finite subfamily has the member with largest index as its intersection.
  The finite-intersection property in the fixed compact fiber then gives one
  common anchor.  No sequential compactness, metric, local connectedness,
  discrete-fiber, covering-space, or path-lifting argument is used.
- The v57 terminal carriers are compact, connected, nested, and contain both
  the root and the chosen terminal endpoint, so they satisfy the hypotheses
  of the abstract persistent-anchor theorem.

## Skill-hypothesis ledger

- The `proper-open-chain-component-anchor` research card was inspected.  Its
  metric-chain route does not apply because the manuscript assumes neither
  metrizability nor a finite or discrete fiber.  No theorem from that route
  was imported.  The live proof instead uses the compact-Hausdorff
  component--quasi-component separation already established in v56.
- The `mingchen-writing` pass tightened the Chapter 15 summary to repeat the
  full topological hypotheses and kept the analytic finite-flat trace claim
  separate from the purely topological anchor claim.

## Verdict

PASS as a local, source-aware, dependency-closed partial advance.  The exact
statement and proof pass the strict writing audit with zero errors and zero
warnings.  The full build, reference audit, inventory audit, log scan, and
visual inspection are recorded in `BUILD_REPORT_LIVE.md`.  No model-backed
verifier was used for this version.
