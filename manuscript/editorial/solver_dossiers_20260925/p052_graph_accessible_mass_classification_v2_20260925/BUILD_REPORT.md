# P05.2 graph classification build report

## Minimal packet

`minimal_compile.tex` builds successfully to a ten-page PDF of 181,268 bytes.
Its TeX and PDF SHA-256 values are
`9ad71a6145cb240b088bd2c1e3ef04c48e17bc544922764c5591587dbc1be0c2`
and
`9f3414793e4608e429062a22ec9d4b784b16f7ad150af4ad0d8c433067a8c413`.

## Full book

The converged full build produces `manuscript/book.pdf` with:

- 4,082 pages;
- 19,432,997 bytes;
- SHA-256
  `dda782a92de87a6c5b66702251e6a00932dc49e06ad501046a51e5f981d0fbdd`.

The final log has no undefined reference or citation, rerun request,
horizontal overfull box, or vertical overfull box.  The 13 inherited Chapter
70 duplicate destinations are unchanged.

## Visual and structural checks

Physical PDF pages 3799--3804 were rendered and inspected.  The transition
from the local rank-one theorem, the full graph-classification statement,
the ambient-norm accessibility proof, the cone-slice obstruction, and the
return to the following affine-space lemma are complete and unclipped.

The source graph contains 407 build-closure files and 11,853 labels, with no
missing input, duplicate label, dangling reference, or structural error.  All
six reference-checker tests pass.  The Chapter 72 inventory remains 42 active
atoms in 12 formal problem environments, with tiers `(0,3,7,15,17)`.
