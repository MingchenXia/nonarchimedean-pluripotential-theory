# Verification repair ledger

Date: 20 September 2026

## First submission

The dependency-bundled first submission was rejected with one critical
error and five dependency gaps.  The critical error was mathematical: a
closed point on a smooth curve need not have separable residue field over
an imperfect base.  The response is preserved in
`model_run_full_closure/response.json`.

## Repair

- Replaced the false separability and finite-etale assertion by the finite
  faithfully flat ground-field projection actually needed by the descent.
- Removed the unnecessary exact fibre-slicing dependency: the
  scalar-stability hypothesis directly supplies the zero-current equality
  after completed algebraic closure.
- Replaced book-local Wanner and maximum-principle references by the exact
  published Wanner and Thuillier locators.
- Expanded the continuous-multiplier projection-formula argument and made
  clear that the normalized top form is integrated on the fixed
  `K`-analytic fibre.
- Removed the auxiliary regularity-transfer paragraph from the principal
  proposition so the verified claim is exactly the new descent theorem.

The repaired standalone packet was then accepted with no critical errors
and no gaps.
