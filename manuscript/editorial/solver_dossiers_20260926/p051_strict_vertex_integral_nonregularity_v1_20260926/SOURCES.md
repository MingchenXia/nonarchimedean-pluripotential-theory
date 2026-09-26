# P05.1 strict-vertex integral-slope nonregularity: sources

## Primary source

Botero--Mazzon--Pille-Schneider, *Monge--Ampère measures on balanced
polyhedral spaces*, arXiv:2603.08664v1.

- Definition 2.28 fixes the literal integral-slope piecewise-affine class.
- Theorem 4.13 and Proposition 4.16 give the positive polyhedral
  Monge--Ampère measure and its total mass `deg(gamma)`.
- Theorem 6.4 and Definition 6.5 characterize and define regularity.
- Definition 6.9 assumes regularity before defining orthogonality.

## Internal dependencies

- `lem:frontier-polyhedral-one-vertex-convexity` is the local
  one-dimensional slope criterion and the vertex-mass formula.
- `thm:frontier-polyhedral-graph-orthogonality-classification` classifies
  real-PA orthogonality by the same local relation cones.
- `thm:frontier-polyhedral-one-vertex-integral-nonregularity` is recovered
  as the special case of a one-vertex fan with positive outgoing slopes.

## Scope

The theorem is a book-local consequence of the literal coefficient
convention and elementary convexity.  It proves nonregularity when the
reference slope vector is strictly positive on every nonzero local
balancing relation.  It covers every positive-degree finite graph whose
local relation cones are one-dimensional.  It does not classify the
zero-degree case or the higher-rank case when the reference slope vector
lies on a proper face of the dual relation cone, and it makes no
higher-dimensional assertion.
