# P03.1 finite-flat local pullback: live audit

## Scope and baseline

- Live integration baseline: `2714bf8ddd787c64e008f21603ce9fd0eca4d4a3`.
- Live files: `STATEMENT_LIVE.tex` and `PROOF_LIVE.tex`.
- Integration sites: Chapter 15, Chapter 72, and the atomic open-problem inventory.
- This packet synthesizes the usable cores of the quarantined v36, v37, and
  v48 dossiers into a standalone proof. It does not import the collar or
  repair formulas from v38, v44, or v49.
- No model-backed verifier was used for this packet.

## Mathematical ledger

1. The characteristic polynomial of multiplication by an analytic unit on a
   finite locally free algebra records the maximum modulus on each analytic
   fiber. The proof treats local Artinian factors explicitly; nilpotents
   change eigenvalue multiplicities but not the set of eigenvalue moduli.
2. The nonzero constant coefficient is a unit. Near a selected base point,
   coefficients vanishing there are strictly dominated by that coefficient.
   A common denominator therefore converts the logarithmic spectral maximum
   into a rational LFS formula.
3. A finite flat fiber is separated into finitely many disjoint branches.
   Properness saturates the branch neighborhood, openness retains every
   branch over a smaller base neighborhood, and local constancy of rank gives
   fixed positive branch degrees.
4. Finite sums and maxima in a rational LFS presentation compress to a single
   finite maximum after taking common denominators. Applying the spectral
   formula branchwise proves closure under fiberwise maximum and exact global
   pullback for the rational LFS envelope.
5. Real nonnegative coefficients in a local LFS presentation are approximated
   by nonnegative rational coefficients. Subtracting a small rational
   value-group constant makes the approximation one-sided. Restriction from
   the compact analytic neighborhood to an ordinary open neighborhood places
   the approximants in the local-envelope competitor family.
6. To descend a competitor defined near one cover point, an assumed LFS
   baseline fills the other points of the complete fiber. Proper shrinking
   captures the entire nearby fiber, and rational fiberwise maximum descends
   the resulting obstacle minorant.
7. On boundaryless spaces, the established local PL--LFS cofinality theorem
   upgrades local LFS pullback to local PL pullback. With a global LFS
   baseline, subtraction from the common local value yields the defect
   balance, contraction, and gain bound with the displayed signs.
8. In the finite-orbit range, substitution of the previously established
   PL--LFS defect split and symmetry identity gives the four-defect balance.
   The envelope chain justifies the simultaneous vanishing conclusion.

## Hostile checks

- No analytic section is used.
- No closure of arbitrary real PL functions under fiberwise maximum is used.
- No globalization or collar-extension theorem is asserted.
- No scalar-extension map is asserted to admit a finite-flat presentation.
- Empty rational competitor families are handled in both directions.
- The second-pass audit added an explicit restriction to the interior of the
  compact analytic neighborhood before using the rational approximants as
  ordinary-open local competitors.

## Verdict

The live packet is internally consistent and suitable for integration as a
strict partial advance on P03.1. It removes the local-section gate for finite
flat covers but does not prove base local-to-global LFS cofinality or produce
the finite-flat scalar-extension presentation needed by the full problem.
Accordingly, no P03 atom is retired.
