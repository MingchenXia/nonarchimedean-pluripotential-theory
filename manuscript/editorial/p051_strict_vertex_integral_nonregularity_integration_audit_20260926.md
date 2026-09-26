# P05.1 strict-vertex integral nonregularity: integration audit — 26 September 2026

## Supplied source and integration decision

The author-supplied PDF is byte-identical to the withdrawn positive draft
already recorded in the repository: 252,482 bytes, SHA-256
`0ad51074108eb2202d4b624637c035610d275c67fd8456dab59282d543d5f5fb`.
Its retained positive theorem is not cited or restored.  The relevant datum
is the coefficient conflict in its withdrawal notice: literal
piecewise-affine functions have integral slopes, whereas the natural
envelopes can have fractional slopes.

Chapter 72 now develops that conflict beyond the one-vertex setting.  At a
vertex `v`, let `K_v` be the cone of nonnegative balancing relations.  If the
reference slope vector is strictly positive on every nonzero element of
`K_v`, a compact normalized-cone argument permits a common decrement `1/N`
of all outgoing slopes.  A bounded integral-slope star obstacle then has the
exact fractional-slope envelope

```text
gamma(x_e(t)) + (R-t)/N   for 0 <= t <= R,
gamma                     off the closed star.
```

The left derivative of any literal approximant is integral.  Evaluating at
`t=R/N` yields the quantitative separation
`(N-1)R/(2N^2)`.  Hence every strict reference vertex obstructs literal
regularity.

If every local relation cone is one-dimensional and the reference has
positive degree, a positive-mass vertex is automatically strict.  Therefore
every such pair fails literal regularity.  This complements, without
contradicting, the real-piecewise-affine classification: the graph class on
which real-PA orthogonality holds is negative for literal regularity whenever
the literal degree is positive.

## Scope boundary

P05.1 remains open.  The theorem does not address the zero-degree graph
case.  For positive-degree references, any remaining literal graph case must
have a higher-rank local relation cone and place the reference slope vector
on a proper face of the dual cone at every positive-mass vertex.  Arbitrary
nonseparable product obstacles, higher-dimensional balanced spaces, and the
source coefficient-convention repair also remain open.  P05.2 likewise
remains active.

No model-verifier result is claimed for the new theorem.  Earlier archived
receipts concern different frozen packets and do not certify this
integration.

## Release gates

- Scoped Mingchen-writing audit: zero errors and zero warnings.
- Minimal packet: 3 pages, 139,291 bytes, SHA-256
  `3a14f5d9a4db2d3d44842d69a1751512876fe5b0f893cdbc74a7d956a44c01e6`;
  the final log is clean and all three pages were visually inspected.
- Reference graph: 417 build-closure files and 11,870 unique labels; zero
  missing inputs, multiply defined labels, dangling references, or structural
  errors.  All six checker tests pass.
- Inventory: 42 active atoms in 12 formal problem environments, tiers
  `(0,3,7,15,17)`.
- Full book: 4,094 pages, 19,477,911 bytes, SHA-256
  `2a444ce73c727fa400277c0cad69c27d8f7dfab5b5ea7d24db83518daa20f60e`.
- Full-book log: no unresolved reference or citation, rerun request, missing
  input, horizontal or vertical overflow, or fatal error.  The 13 inherited
  Chapter 70 duplicate destinations are unchanged.
- Visual audit: physical pages 3809--3813, corresponding to printed pages
  3741--3745, were rendered after the final build and inspected.  The theorem,
  both proofs, and the corrected positive-degree/zero-degree boundary have no
  clipping, collision, or malformed display.

Exact packet-level evidence is preserved in
`solver_dossiers_20260926/p051_strict_vertex_integral_nonregularity_v1_20260926`.
