# P07.1 finite unbranched polyhedral-complex follow-up

Date: 30 August 2026

Status: **isolated research candidate**.  This directory is not a live-book
input.  No production Rethlas call was made for these principal bytes.

## Result proved

The production-verified Stone-parameter times convex-polyhedron theorem
extends, as a local sheaf statement, to a finite face-to-face polyhedral
complex whenever every complete germ, including its generator sheaf, has a
generator-preserving convex development.  The extension gives a decreasing
smooth psh approximation on one fixed chart neighbourhood crossing all
faces at the germ.

The proof is exact chart transport.  It does not glue separately chosen
chamberwise approximants and does not claim one global decreasing sequence
on the whole complex.

## Hostile boundary found

Topological unbranching and cellwise positivity alone are insufficient for
that reduction.  Two perpendicular rays form a face-to-face topological
line, but the ambient affine psh generator `-x-y` unfolds to `-|t|`.  Hence
the ambient cellwise generator germ is not the convex interval generator
germ.  Branches, singular lower links, and nonconvex unions without a
generator-convex chart remain excluded.

## Files

- `statement.tex`: precise theorem and scope firewall;
- `proof.tex`: chart transport, comparison-chart independence, fixed-star
  approximation, and the two-ray obstruction;
- `SOURCE_AND_OBLIGATION_MATRIX.md`: exact dependency/source hashes and
  proof-obligation ledger;
- `EDGE_CASES_AND_OBSTRUCTIONS.md`: zero-dimensional, boundary, unbounded,
  monodromy, nonconvex, and branching analysis;
- `compile.tex`, `compile.pdf`, `compile.log`: minimal build artifacts;
- `SHA256SUMS`: frozen identities.

Any later production submission must materialize the exact D1 dependency
identified in the source matrix and must not enlarge the theorem to
cellwise-positive or globally approximable complexes.
