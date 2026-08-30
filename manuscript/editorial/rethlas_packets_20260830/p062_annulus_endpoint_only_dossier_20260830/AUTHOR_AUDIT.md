# Author audit of the endpoint-only dossier

## One-dimensional argument

1. **Interior corrected.**  The dossier never identifies the absolute
   interior with the strict radial core.  It explicitly includes every
   endpoint virtual-disc branch and omits only the Gauss point of each
   non-strict endpoint.
2. **Field scope separated.**  Baker--Payne--Rabinoff Lemma 2.12 is used only
   in its algebraically closed scope.  Ducros 3.6.35.5--3.6.35.10 supplies
   arbitrary-field virtual-disc branches and scalar-extension compatibility.
3. **No current pullback.**  The proof does not infer a CLD current equation
   after extension to an algebraic closure.
4. **Tube lies in the equation locus.**  For an endpoint rigid point `y`,
   coefficient dominance gives `X_y={|P|<s^d} subset {|T|=s}`; the endpoint
   Gauss point has `|P|=s^d`, so `X_y` lies in the absolute interior.
5. **Disc theorem applied in its exact scope.**  The finite-flat trace is a
   continuous zero-Hessian function on a standard strict open disc.  No disc
   theorem on a nontrivial virtual disc is assumed.
6. **Individual value recovered.**  The zero fibre is the single rigid point
   `y` with degree `d`; the boundary Gauss fibre is the single `eta_s` with
   degree `d`.  Hence constancy of the trace compares `h(y)` with `h(eta_s)`,
   rather than merely comparing an average over several branches.
7. **Inseparability retained.**  The graded rational-function degree is `d`
   including the inseparable degree; no splitting into geometric roots is
   used.
8. **Nonrigid points included.**  Local rigid density in the strict analytic
   endpoint branches and continuity extend the equality beyond rigid points.
9. **Both endpoints handled independently.**  The same argument applies at
   `r` and `R`, and hence covers both half-closed annuli and the fully closed
   annulus.

## Product extension

The product route is intentionally not certified.  The dossier identifies
two remaining audit obligations: generalized slicing over virtual-disc base
neighbourhoods, and multi-endpoint limiting on Berkovich fibre products.
Consequently no product theorem is frozen, and no change to the live book is
authorized from this dossier.

## Repository isolation

- No Rethlas call was made.
- No live-manuscript file was changed.
- The v3 statement remains SHA-256
  `985be85d97b583f72be5cee65988df6f31c1edb49a685121b834df179fa87fda`.
- The v3 proof remains SHA-256
  `42b592bf8ac26ed46c36928e5e90272225ae6883bd2bfe62d3ff2840f01d46e5`.
