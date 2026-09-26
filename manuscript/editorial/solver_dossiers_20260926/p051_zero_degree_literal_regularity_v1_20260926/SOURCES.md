# P05.1 zero-degree literal regularity: sources

## Primary source

Botero--Mazzon--Pille-Schneider, *Monge--Ampère measures on balanced
polyhedral spaces*, arXiv:2603.08664v1.

- Definition 2.28 fixes integral linear parts and rational constants in the
  literal piecewise-affine class.
- Definition 4.5 defines the degree as the total polyhedral Monge--Ampère
  mass.
- Definition 4.15 says that every recession slope is strictly positive for a
  reference positive at infinity.
- Proposition 4.16 keeps the Monge--Ampère mass away from the boundary at
  infinity.
- Definition 6.15 and Proposition 6.17 identify the one-dimensional
  polyhedral Monge--Ampère measure with the weighted graph Laplacian.
- Theorem 6.4 and Definition 6.5 give the regularity criterion used in the
  final step.

## Internal dependencies

- The real scalar extension and literal coefficient convention are fixed in
  `thm:frontier-polyhedral-one-dimensional-real-regularity`.
- The remaining positive-degree obstruction is
  `thm:frontier-polyhedral-strict-vertex-integral-nonregularity`.

## Scope

The theorem is a book-local finite-graph argument.  It closes the
zero-degree branch in dimension one.  It does not decide the positive-degree
higher-rank boundary case or any higher-dimensional case.
