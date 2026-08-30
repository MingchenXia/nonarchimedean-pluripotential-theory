# Hostile self-audit

## Counterexample checks

1. **Existence of the radius.** The proposition is conditional on a radius
   outside the divisible value group.  This is enough to disprove the
   universal arbitrary-radius claim.  Concretely, for
   `K = Q_l` one may take `R = |l|^{sqrt(2)}`.
2. **Nonemptiness.** The image of the `R`-Gauss point under
   `U -> (U,U^{-1})` lies in `P` and satisfies `TS-1=0`.
3. **No cancellation gap.** The assumption
   `R notin sqrt(|K^times|)` makes the weighted norms of distinct monomials
   pairwise different.  Hence restriction to `K[T]` is literally the
   `R`-Gauss seminorm.
4. **Interior gap.** The proof does not infer interior behaviour after
   scalar extension.  It uses the open-map theorem for the ambient smooth
   coordinate projection to show directly that the whole tube is outside
   the base absolute interior.
5. **Support gap.** The support of the cutoff is contained in
   `|TS-1| <= c`, and `c<1`; it is therefore contained in the boundary
   tube even though the cutoff vanishes on its level-`c` boundary.
6. **Current gap.** On the absolute interior the function is identically
   zero, so its associated Hessian current vanishes there without any
   regularity or pullback assertion.
7. **Failure of the conclusion.** The function is one at the torus Gauss
   point and zero at `(0,0)`.  Since there are no annulus factors, the
   claimed affine form would be constant.

## Scalar-stable repair checks

1. The extension field is assumed complete and contains elements of every
   defining norm, so every factor is strict after base change.
2. The current equation is explicitly assumed on `Int(P_L)`.  It is not
   inferred from the downstairs equation.
3. The strict v4 theorem is used only in its exact stated scope.
4. Descent uses only surjectivity and preservation of coordinate
   seminorms; it does not descend currents.
5. The existence of a strictifying extension is separate from the current
   ascent problem.

## Release status

This is an author-side audit only.  The exact principal statement and proof
remain quarantined pending an independent exact-byte hostile audit and
production Rethlas verification.
