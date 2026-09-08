# Local preflight — P21.3 toric-boundary subcase

The proof is intentionally based on the full partial compactification rather
than extrapolating the dense-torus proof cell by cell.

1. The exact source gives the continuous invariant descent on `O subset
   N_Sigma`, not merely on the dense stratum.
2. It also gives the explicit basic-neighborhood model at a boundary stratum.
   In that model the dense part is one convex set, so a zero distributional
   Hessian yields one affine function rather than unrelated cellwise pieces.
3. Each normal ray remains in the same basic neighborhood. Finite continuity
   at its compactified endpoint forces the affine slope to vanish in every
   normal direction. This is the missing boundary compatibility step.
4. Zero normal slope gives the source's precise `constant towards the
   boundary` smoothness condition, and Proposition 2.3.4 then supplies the
   analytic CLD-smooth pullback.
5. No claim is made that arbitrary polyhedral face gluings, including the
   cross-fan obstruction recorded in Chapter 16, share this unbranched toric
   boundary mechanism.
