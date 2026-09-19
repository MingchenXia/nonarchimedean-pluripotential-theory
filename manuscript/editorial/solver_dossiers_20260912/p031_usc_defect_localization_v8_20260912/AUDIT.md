# P03.1 upper-regularization defect localization — audit

Date: 19 September 2026

## Claim boundary

For a nonempty locally upper-bounded family of classically psh functions,
the regularized supremum is classically psh off the closure of the strict
gap between the raw supremum and its upper-semicontinuous regularization.
No smallness, polarity, capacity-zero, or removability property is claimed
for that closed defect support.

For the affine Perron family, completed algebraic closure preserves the
defect set and its closure exactly.  This does not settle compatibility for
further analytic extensions and retires no P03 atom.

## Proof ledger

1. The complement of the closure of the strict defect is exactly the union
   of all ordinary open equality loci.
2. Finite maxima of competitors are classically psh and form a directed
   net converging pointwise to the raw supremum.
3. On the open equality locus the limit is the upper-semicontinuous
   function $u=s^*$, so Gubler--Rabinoff Theorem 6.5 applies.
4. The completed-algebraic-closure identity pulls back the strict defect
   set exactly.
5. Continuity gives one closure inclusion; openness of scalar projection
   gives the reverse inclusion.

## Exclusions

- No maximizing competitor, countability, or Choquet sequence is assumed.
- The pointwise-limit theorem is not used on the defect support.
- The old quarantined corollary depending on the unintegrated v6 packet is
  excluded from the live theorem.
- The already-usc obstacle special case is recorded only as a consequence,
  not as a new solution of P03.2 or P03.3.

No model-backed verifier was used for this dossier.
