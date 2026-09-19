# Source and dependency ledger

Date: 19 September 2026

## Integrated dependencies

- `cor:p061-analytic-standard-etale-all-orbits`: supplies the exact
  principal orbit chart, absorption of the split orbit torus into the
  quasi-smooth parameter, and restriction of the standard-etale
  presentation.
- `prop:p061-analytic-standard-etale-toric-product`: manufactures the
  weighted toric product in the strictly analytic standard-etale source.
- `lem:p061-product-open-tube` and
  `prop:p061-v3-single-shilov-factorization`: keep the product inside the
  function domain and factor through the retained parameter.
- `lem:p061-product-factor-reduction` and
  `thm:p061-arbitrary-curve-factors-ph-rpl`: identify the reduction of the
  enlarged final factor and handle all arbitrary curve factors.
- `prop:ch18-harmonic-functorial`: preserves harmonicity under pullback.
- `cor:p061-analytic-standard-etale-algebraic-split-forms`: supplies the
  scalar-extension principle and the ground-field two-sign comparison.
- Gubler--Jell--Rabinoff, `GJR26`, Lemma 5.4(1) and Corollary 5.12:
  pullback stability and completed-algebraic-extension descent for real-PL
  functions.

## Dependency closure

The proof does not assume a product in the analytic standard-etale source.
It first uses the existing coefficient-contraction theorem to manufacture
the weighted toric product.  Singleton-Shilov factorization removes that
factor, leaving the arbitrary curves and an enlarged final factor with
quasi-smooth reduction.  The established arbitrary-curve theorem applies
there, and completed-algebraic-extension descent returns the conclusion to
the ground field.

No new external source is invoked, no novelty or priority claim is made,
and no model-backed verifier was used for this dossier.
