# P06.2 polyannulus slope exact sequence v66: live audit

## Claim boundary

The revision refines the v65 radiance obstruction slope by slope.  A
parallel dual slope occurs in a global continuous zero-current function
exactly when its scalar contraction with the zero-current radiance class
vanishes.  This gives a natural exact sequence and two consequences:
injectivity of the contraction forces descent to the curve, while vanishing
of the full radiance class gives a gauge-dependent direct-sum splitting.

The result retains every v64/v65 geometric hypothesis.  It does not
trivialize the lattice local system, turn zero-current gauges into analytic
units, construct global annular coordinates, or treat a fibration without
the displayed local curve--polyannulus charts.

## Proof ledger

1. Contracting the twisted affine cocycle with a parallel dual section
   gives a scalar Cech one-cocycle.
2. A change of annular coordinates changes this scalar cocycle by the
   coboundary of the contracted translation zero-cochain.
3. Unique local coefficients define the slope map; zero slope is equivalent
   to unique descent from the curve.
4. Every realized slope annihilates the radiance class because its local
   base coefficients provide the required coboundary.
5. Conversely, a vanishing scalar obstruction supplies local base
   coefficients.  Their affine logarithmic formulas glue, and the local
   curve--polyannulus converse makes the glued function zero-current.
6. Exactness gives the injective-obstruction descent criterion.  When the
   full radiance class vanishes, the v65 gauge supplies an explicit linear
   splitting.

## Model-verifier repair

The first frozen submission returned `wrong` with zero critical errors and
two dependency-packaging gaps.  It required the packet itself to state that
the translations in a change of annular coordinates have zero-current
components, and to spell out the zero-current affine gauge and the local
zero-current property of its pairings rather than merely citing the v65
proposition.  The repaired statement now includes both inputs explicitly.
The original request, response, and safe headers remain archived without
alteration in `VERIFICATION_RUN_20260920/`.

The repaired frozen packet returned `correct`, checking one item with zero
critical errors and zero gaps.  During the automatic second prose pass, the
notation `Z(Y)` was replaced at its one pre-definition occurrence by its
full phrase.  This changed only the exposition, but the final bytes are
being resubmitted so the controlling receipt matches the live packet.

The final frozen submission returned `correct`: one proof item checked,
zero critical errors, and zero gaps.  Its item identifier is
`pi_c7e21a8b160c7d9b03b50d58`, and its proof digest is
`8deb5a42fb2210dc3202964d87f7cecbaf57211ccf6746093a5042ff876ebadc`.
The final request, response, and safe headers are archived in
`VERIFICATION_RUN_FINAL_20260920/`; both earlier runs remain preserved in
their own directories.

The page-level second pass then split the opening display to remove a local
overfull box and corrected the phrase `glue to an element of a continuous
zero-current function` to `glue to a continuous zero-current function`.
Neither change alters the mathematical content, but the resulting frozen
bytes were submitted once more.  The controlling polished submission also
returned `correct`: one proof item checked, zero critical errors, and zero
gaps.  Its item identifier is `pi_2956b458517b66c3aab40649`, its statement
digest is
`e8d4ed82a6806be8f5120c563a105b09d5eb37cca8af35b2861593c80fbc3790`,
and its proof digest remains
`8deb5a42fb2210dc3202964d87f7cecbaf57211ccf6746093a5042ff876ebadc`.
The controlling request, response, and safe headers are archived in
`VERIFICATION_RUN_POLISHED_20260920/`.

## Residual boundary

P06.2 remains open for arbitrary analytic germs, nonproduct local domains,
strict-core-only equations, annular fibrations without the stated analytic
product charts, and analytic-coordinate realization of a zero-current
gauge.  The active-atom count is unchanged.
