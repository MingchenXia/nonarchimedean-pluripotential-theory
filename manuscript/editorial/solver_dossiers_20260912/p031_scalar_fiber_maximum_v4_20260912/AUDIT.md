# P03.1 scalar-fiber maximum — audit

Date: 19 September 2026

## Claim boundary

The packet is a topological refinement of the affine ground-field Perron
theorem.  For a continuous closed surjection with compact fibers, it
identifies the downstairs usc regularization with the maximum of the
pulled-back usc regularization on the fiber.  Applied to analytic scalar
projection, this makes the remaining compatibility condition equivalent
to fiberwise constancy.

The type-4 example concerns a bounded binary raw function.  It is not
asserted to be psh, to be a supremum of psh functions, or to arise from the
P03 obstacle family.  No P03 atom is retired and no CLD-v2 or continuity
conclusion is drawn.

## Proof ledger

1. Pulling back a base neighborhood gives the easy inequality at every
   point of the fiber.
2. The pulled-back regularization is usc and attains a maximum on the
   compact fiber.
3. Finitely many strict upper-bound neighborhoods cover that fiber.
   Closedness produces a saturated base neighborhood whose full inverse
   image lies in their union, and surjectivity descends the bound.
4. A continuous surjection is open exactly when the regularization identity
   holds for every bounded binary raw function.  Non-openness supplies the
   indicator of the complement of a non-neighborhood image.
5. Scalar projections are continuous, closed, and surjective; their fibers
   are compact Berkovich spectra.  The general formula therefore applies
   on the whole space and after restriction over an ordinary open set.
6. Poineau--Turchetti's type-4 fiber contains the open-disc witness to
   non-openness.  The binary construction gives a strict raw-data defect at
   a point of that fiber, while the compact-fiber formula identifies the
   downstairs value with the fiber maximum.

## Hostile checks

- The maximum is used only after restricting an usc function to a compact
  topological fiber; no maximum of psh functions is formed.
- The case in which the fiber maximum is `-infinity` is handled by testing
  every real threshold.
- Compactness is supplied independently by the Berkovich spectrum formula;
  it is not inferred from closedness.
- Relative closedness survives restriction over an ordinary open subset.
- The equivalence with openness quantifies over arbitrary bounded binary
  data and is not transferred to the special psh-supremum class.

No model-backed verifier was used for this dossier.
