# P03.1 v57 local hostile audit

Date: 2026-09-20

Baseline commit: 09e361124057ceb3d2dfb4ad51fd8fd7b94853ec

## Result under audit

The live insertion proves three strict partial advances for the rational
globalization defect profile
\[
g_v=v-s_{\mathbf Q,X}.
\]

1. For a fixed root point and a positive local rational competitor defect,
   the boundary contacts of all strict rooted superlevel components form a
   decreasing family of nonempty compact sets.  Their intersection is a
   nonempty compact terminal boundary core.
2. The rooted terminal trace is finite and upper semicontinuous.  Its maximum
   is exactly the pointwise positive defect, its maximizer set is exactly the
   terminal core, and it is bounded above by the full boundary trace.
3. Under finite flat pullback, every lift of a terminal boundary point admits
   one central-fiber anchor lying in the same pulled-back compact component at
   every strict level below the rooted defect height.

This does not settle P03.1.  It replaces a level-dependent family of boundary
contacts and finite-fiber anchors by persistent choices, but it does not make
the terminal trace vanish.  The active inventory therefore remains at 46
atomic questions in 14 formal problem environments.

## Dependency and proof audit

- For every strict level, v55 supplies a nonempty boundary contact set.  It is
  compact because it is closed in the compact boundary of the relatively
  compact test domain.
- If the level increases, the rooted superlevel component can only shrink:
  the higher component is a connected subset of the lower superlevel set
  containing the same root.  The boundary contact sets therefore decrease.
- The finite-intersection property for nested nonempty compact sets produces
  the terminal boundary core.  No sequence, metric, or first-countability
  argument is used.
- The positive superlevel sets of the rooted trace are intersections of the
  closed boundary contact sets.  They are closed, so the rooted trace is
  upper semicontinuous.  The same identity identifies the terminal core with
  its maximizer set and gives maximum equal to the rooted defect height.
- Membership in a rooted boundary contact set forces the full boundary trace
  to be at least that level, directly from the neighborhood definition of the
  trace.  Taking the supremum proves the pointwise rooted-to-full trace bound.
- For finite flat pullback, the compact carriers are connected, contain the
  root and terminal point, and decrease with the level.  The v56
  compact-Hausdorff proper-open component lemma makes every component through
  the chosen boundary lift meet the finite central fiber.
- Those lifted components decrease.  Their intersections with the finite
  central fiber are a decreasing family of nonempty subsets of one finite
  set, hence have a common point.  This is only a common anchor in the compact
  pulled-back carrier components; no path lift or common component of the
  open pulled-back superlevel sets is asserted.
- The final wording says that a positive witnessing competitor *admits* a
  common terminal endpoint.  It does not assert uniqueness: the terminal core
  can contain more than one point.  Likewise, the finite-flat conclusion is
  existential and does not claim a unique sheet.

## Skill-hypothesis ledger

- The `boundary-inverse-radius-collapse` research card was inspected.  Its
  holomorphic coordinate map and inverse-branch radius hypotheses have no
  analogue for the Berkovich defect trace used here, so it was treated as a
  non-trigger and no result from that card was imported.
- The `proper-open-chain-component-anchor` research card was inspected.  Its
  original metric-chain proof is unavailable because the ambient spaces are
  not assumed metrizable.  The manuscript instead uses the independent v56
  compact-Hausdorff quasi-component lemma.
- The `mingchen-writing` second pass replaced two potentially unique-sounding
  endpoint claims by exact existential statements and kept the finite-flat
  conclusion at the level of compact pulled-back components.

## Verdict

PASS as a local, source-aware, dependency-closed partial advance.  The exact
statement and proof pass the strict writing audit with zero errors and zero
warnings.  The full build, reference audit, inventory audit, log scan, and
visual inspection pass.  No model-backed verifier was used for this version.
