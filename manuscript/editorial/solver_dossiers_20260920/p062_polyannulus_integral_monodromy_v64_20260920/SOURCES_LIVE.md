# P06.2 integral polyannulus monodromy v64: source ledger

- `prop:ch08-annulus-skeleton`: Laurent--Gauss maximum inequality and
  concave piecewise-affine radial valuation with integral slopes on a strict
  closed annulus.
- `lem:ch15-log-smooth`: the logarithmic absolute value of an analytic unit
  has zero mixed current.
- `thm:p062-open-polyannulus-products-over-curves`: unique real base and
  slope coefficients for continuous zero-current functions in a standard
  strict polyannulus product chart.
- `thm:wanner-curve-comparison`: the precise algebraically closed,
  complete, nontrivially valued curve setting imported by the product
  theorem.

The dependency statements sent with the repaired model-verifier packet are
preserved verbatim in `VERIFIER_DEPENDENCIES_LIVE.tex`.  The principal
proposition now states the locally trivial bundle geometry in full instead
of importing it through
`cor:p062-open-polyannulus-bundles-over-curves`.

No new external theorem is used.  The unit lemma is proved from the book's
Laurent--Gauss proposition by applying it to both a unit and its inverse.
The integer matrix entries are then obtained by one-coordinate fibre slices;
unimodularity, the cocycle laws, atlas independence, and dual slope gluing
follow from the existing uniqueness theorem.
