# Source and dependency ledger

Date: 19 September 2026

## Integrated dependencies

- `eq:p061-orbit-product-chart`: separates the pointed transverse toric
  factor from the orbit torus.
- `prop:p061-v3-etale-toric-product`: manufactures an actual weighted-tube
  product from a separated finite-type ordinary-etale source chart.
- `lem:p061-product-open-tube` and
  `prop:p061-v3-single-shilov-factorization`: shrink inside the function's
  domain and factor it through the retained parameter.
- `lem:p061-product-factor-reduction` and
  `thm:p061-arbitrary-curve-factors-ph-rpl`: identify the quasi-smooth
  reduction of the enlarged final factor and handle the arbitrary curves.
- `prop:ch18-harmonic-functorial`: preserves harmonicity under pullback.
- `cor:p061-zariski-etale-algebraic-split-toric-charts`: supplies scalar
  extension and the ground-field two-sign comparison.
- Gubler--Jell--Rabinoff, `GJR26`, Lemma 5.4(1) and Corollary 5.12:
  pullback stability and completed-algebraic-extension descent for real-PL
  functions.

## Dependency closure

The proof first constructs the transverse toric product upstairs, rather
than assuming a product chart.  Singleton-Shilov factorization removes the
weighted toric factor.  The retained quasi-smooth fixed fibre is grouped
with the final factor; its reduction remains quasi-smooth, so the existing
arbitrary-curve-factor theorem applies.  Completed-algebraic-extension
descent then returns the result to the ground field.

No new external source is invoked, no novelty or priority claim is made,
and no model-backed verifier was used for this dossier.
