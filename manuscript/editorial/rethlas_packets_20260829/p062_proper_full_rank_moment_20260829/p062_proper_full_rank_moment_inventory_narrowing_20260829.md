# Staging-only replacement for the P06.2 atomic-inventory entry

The heading ``prob:frontier-pluriharmonic --- 2 atoms`` and all global atom
and tier counts remain unchanged.

Change the inventory date at line 3 from 28 to 29 August 2026.  Keep the
literature cutoff at 24 August 2026 and leave the T2 queue unchanged.

```markdown
**Inventory date:** 29 August 2026
```

## Replacement P06.2 bullet

- **P06.2** `[T2; open after the weakly smooth, real-PL, proper full-rank
  moment-factor, and smooth-proper-curve cases]` Decide whether an arbitrary
  continuous function with zero
  \(\mathrm d'\mathrm d''\)-current is classically pluriharmonic, or
  harmonic whenever the classical notion is available, without assuming a
  proper full-rank moment factorization.

## Scope paragraph to insert after the existing real-PL audit paragraph

The proper full-rank moment-factor case is also verified by
`prop:p062-proper-full-rank-moment`.  It applies only to
\(h=\varphi\circ F\), where \(F=(-\log|f_1|,\ldots,-\log|f_n|)\) is one
pleasant full-rank moment, \(F(X)=F(\Sigma_F^{(n)})\) is a nonempty connected
open subset of \(\mathbf R^n\), \(F\) has compact inverse images of compact
subsets, and the pushed-forward canonical calibration has constant positive
multiplicity.  In this scope, zero current forces \(\varphi\) to be affine.
When \(X\) is boundaryless,
`cor:p062-proper-full-rank-moment-automatic-calibration` makes the constant
calibration automatic and gives the converse.  The exact statement and proof
passed production Rethlas run `20260829T031126Z_75e9cb498ce4`, item
`pi_f96fe9f8904943602779f274`, final `correct`, with zero critical errors and
zero gaps.  No theorem in the packet constructs such an \(F\) for an
arbitrary continuous function, so P06.2 remains one active T2 atom outside
this factorized scope.  No atom count, tier count, or queue position changes.
