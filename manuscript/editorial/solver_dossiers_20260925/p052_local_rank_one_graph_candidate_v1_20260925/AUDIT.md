# P05.2 local rank-one graph audit

## Mathematical boundary

The theorem proves real-polyhedral orthogonality when every vertex relation
cone is one-dimensional.  The proof is local at a positive-mass noncontact
vertex: raising the vertex by a sufficiently small amount decreases each
outgoing slope by a controlled quantity, while the unique balancing relation
keeps the local Jensen inequality positive.  Each cutoff contributes an
upward one-variable slope jump.  This argument neither cuts bounded edges nor
uses acyclicity.

At a higher-rank vertex, the earlier extreme-relation construction gives a
local obstruction germ.  The audit does not identify that germ with a global
obstacle on an arbitrary bounded graph.  The converse, literal integral-slope
formulation, and higher-dimensional problem remain open; P05.2 is not
retired.

## Verification boundary

Three dependency-closed gpt-6-astra/xhigh reviews returned `correct`, with
zero critical errors and zero gaps.  The first checked forty internal
deduction steps and the relevant BMPS definitions and propositions.  The
second followed the proof-environment copyedit.  The final request followed
the explicit continuity sentence and is byte-identical to the exact current
principal statement and proof together with their frozen dependencies.  Its
server run is `20260925T191853Z_a6da387d529c`; the request and response
SHA-256 values are
`06c65634e5c5d179591dbe3e25dfc4168f75c536f5f08654ca05dcbf2deb72d7`
and
`4dcf06edf6ab3c98ae6cc1753b6d2cde3b98575603e8d8d3187e170eefec29bd`.

These receipts are model-backed review, not formal verification or peer
review.
