# P03.1 rational collar minimax and boundary saturation: live audit

Audit date: 2026-09-20.

## Scope and baseline

- Live integration baseline:
  `838c2ad94a4f4239068472758d4c6f798563648d`.
- Live files: `STATEMENT_LIVE.tex` and `PROOF_LIVE.tex`.
- Integration sites: Chapter 15, Chapter 72, and the atomic open-problem
  inventory.
- The packet derives an exact collar formula for the base rational
  globalization defect and a sufficient boundary-saturation criterion for
  its vanishing.
- No model-backed verifier was used for this packet.

## Mathematical ledger

1. A connected separated good analytic space with at least two points has,
   inside every neighborhood of a chosen point, a relatively compact open
   domain with nonempty topological boundary.  This uses only local
   compactness, Hausdorff regularity, and connectedness.
2. The rational LFS class is local and closed under finite maxima.  Hence a
   local rational minorant that lies below a global rational minorant on a
   protected collar can be glued to the latter by a maximum.
3. Nontriviality of the valuation supplies a positive value
   `tau = -log|gamma|`; the subgroup `Q tau` is dense in `R`, and every
   negative shift by a positive element of this subgroup is rational LFS.
4. If a local competitor has pointwise excess `delta > 0` over the global
   rational envelope, a boundary load below `delta` permits such a rational
   downward shift and protected-collar gluing.  The glued global competitor
   would exceed the global envelope at the central point, a contradiction.
5. Conversely, a global rational competitor arbitrarily close to the
   envelope at the central point, continuity, and a sufficiently small
   nonempty-boundary domain give boundary load below `delta + epsilon`.
   The two bounds prove the exact minimax identity.
6. Taking the supremum over all positive-gap local competitors gives the
   exact collar representation of the rational globalization defect.  The
   empty positive-gap family corresponds precisely to zero defect.
7. Zero defect is equivalent to arbitrarily small boundary absorption for
   every local rational competitor.  Approximating the obstacle itself on a
   surrounding boundary is a stronger sufficient condition.
8. Under boundarylessness, the three-level defect ledger turns zero rational
   defect into simultaneous vanishing of the rational, LFS, and PL defects
   and both branch gaps.  The existing finite-flat tower theorem then
   propagates the resulting six-envelope equality through every stage.

## Hostile checks

- A global rational LFS minorant is finite everywhere and lies below the
  obstacle, so the obstacle is real-valued; every envelope value and
  difference in the packet is finite.
- Every boundary used in the minimax is nonempty and compact.  The relevant
  continuous or upper-semicontinuous function therefore attains its maximum.
- The local competitor is defined on a neighborhood of the compact closure
  of the chosen domain, so its boundary values are legitimate.
- In the lower-bound argument, the compact complement of the boundary
  neighborhood lies in the open domain because the boundary neighborhood
  contains the entire topological boundary.
- The rational shift is strictly positive; shifting downward preserves the
  obstacle inequality.
- Connectedness and the at-least-two-points hypothesis are used only to
  guarantee arbitrarily small domains with nonempty boundary.  They are not
  silently dropped in the tower corollary.
- Completeness, nontrivial valuation, and positive tower length are stated
  explicitly in the tower corollary after the automatic second pass.
- Boundarylessness is invoked only when the rational conclusion is upgraded
  to the PL ledger.
- The result does not claim that normal or geometrically unibranch
  higher-dimensional obstacles satisfy boundary saturation, and it does not
  construct a finite-flat presentation of arbitrary scalar extension.

## Verdict

PASS.  The collar minimax formula follows from the live rational LFS calculus
and elementary topology, and the saturation consequences follow from the
already integrated v51--v52 defect ledgers.  The result gives a precise new
characterization and a concrete sufficient vanishing criterion without
retiring a P03 atom.
