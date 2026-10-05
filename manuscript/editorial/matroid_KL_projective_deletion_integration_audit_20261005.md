# Projective-deletion local-polynomial integration — 5 October 2026

The addition to Appendix G9.6 explains why the known uniform toric
real-rootedness statements in G9.5 concern different polynomials from
matroid Kazhdan–Lusztig polynomials. The explicit Cheng–Liu examples
produce nonreal roots and nonunimodality for the local polynomial P while
preserving a symmetric unimodal Gaussian rank polynomial Z. Appendix
L27 states the source version and finite verification limits.

This checkpoint follows work-branch commit
`399dc97cb274cdec4681f2cf8bb6c779e641d054`. It is an ordinary source-checked
import of existing results and examples, within the user's ongoing
related-literature integration request. It admits no original general
result or fresh independent production-model receipt.

## Frozen primary source and actual reading

- Ronnie Cheng and Shurui Liu, *Kazhdan–Lusztig polynomials of matroids
  need not be unimodal*, arXiv:2607.24186v2, revised 28 July 2026.
- PDF: `https://arxiv.org/pdf/2607.24186v2`, acquired 5 October 2026 at
  11:57:34.129533 UTC, HTTP 200, 443,132 bytes, 17 pages.
- SHA-256: `196203af23dd190cc8383cda7d1cca9bc5c0ff8b2046518969d028b47890770f`.
- The entire extracted text, including the geometric alternative,
  historical AI appendix and references, was read in bounded ranges.
  Actual primary pages 1–7 and 11–13 were viewed in five two-page sheets.
  Full text reading is distinguished from those ten actual page views.
- Primary arXiv metadata checks the authors and version history.
  A final journal edition or exact publisher-file identity is not claimed.
- The ranked-flat palindromic characterization in BHM
  arXiv:2010.06088v5 §1.1 was selectively reread, lines 109–158. Its full
  120-page reading belongs to the earlier singular-Hodge checkpoint; it
  is not counted again as a new full reading or new primary-page view.

Ignored local acquisition evidence is under
`source_material/matroid_KL_followup_20261005/`. Primary page evidence is
under `/tmp/matroid_KL_projective_deletion_primary_20261005/manifest.json`.
The integration manifest retains acquisition, reading and view metadata.

## Known inputs and proof review

The active text identifies Cheng–Liu Theorem 1.1, Lemmas 2.1 and 2.3,
Proposition 2.2, Proposition 2.6, Corollaries 1.2–1.3 and Appendix
Theorem A.4. It retains every controlling hypothesis:

1. The ground points are surviving points of a finite projective geometry
   over a finite field, and they span the ambient space V.
2. A flat span U is defined by the surviving points spanning U; this is
   distinct from an arbitrary subspace of V.
3. C_U counts extensions A containing U with every projective point
   outside U deleted. The zero quotient extension is included.
4. Every proper flat span satisfies the strict half-rank degree bound.
   The condition at U=0 is included. Rank-zero contractions normalize to 1.

The combinatorial proof was checked as follows. The surviving-span map
groups every subspace A into exactly one flat span U. Its fibre consists
of the extensions counted by C_U, yielding the Gaussian rank identity.
Contraction deletes a quotient direction exactly when its entire original
projective fibre is deleted. Successive quotients commute with this
description, the surviving points still span each quotient, and the degree
conditions are inherited. Ranked-flat palindromic uniqueness then proves
the stated contraction polynomials by induction. Spanning is essential
for the ranks and the reciprocal exponent; it has not been dropped.

For Proposition 2.6, line separation confines every entirely deleted
subspace of dimension at least two to W. At a nonzero flat span U, two
independent deleted quotient directions would give two complements, one
shifted by a vector in U outside W, violating line separation. Thus the
quotient degree is at most one. Small quotient dimensions are excluded by
the deleted-point bound. The affine-chart choice of S establishes line
separation and gives the announced rank-seventeen example.

The paper's geometric small-map alternative was read but supplies no new
geometric or sheaf comparison in active TeX. Neither the general singular
Hodge theorem nor a tropical Schubert compactification is newly identified
with any cohomology ring here.

## Exact named-example checks

The accompanying standard-library checker uses exact integers, bit-mask
binary vectors and unique reduced-row-echelon subspace enumeration.
No floating-point root test is used.

**Rank seven.** All 29,212 subspaces of F_2^7 were enumerated, with rank
counts `(1,127,2667,11811,11811,2667,127,1)`. The 13 deleted points are
the seven nonzero points of W and the six specified affine points S.
Seven surviving vectors have rank seven, and the surviving ground set
has 114 points. Direct deleted-subspace counts give `(1,13,7,1)`.

Every one of the 29,131 flat spans was recognized by the rank of its
surviving vectors. For each one, all subspace extensions B with
`B \ U` deleted were enumerated, and every proper-flat degree bound was
checked. This counts 29,212 eligible flat/extension pairs in total.
Their dimension-weighted sum recovers the Gaussian Z-polynomial.
The source's cardinality lower bounds `(15,14,28,24,48,32,64)` are all
greater than 13. The cubic discriminant is exactly -268, proving one
real root and two nonreal conjugate roots. The cubic's positive
coefficient sequence is unimodal, so it is not the nonunimodality example.

**Rank seventeen.** A concrete affine set is
`S={64+(j<<7):0<=j<589}`; W consists of binary vectors 1 through 63.
All 212,226 pairs of the 652 deleted points were checked: each complete
binary projective line lies in W. Exactly 651 such lines occur. Seventeen
specified surviving vectors span the ambient space. The three sufficient
conditions `6<17/2`, `652<2^15` and `589<=2^10` hold. The ground set has
130,419 points. The identified known line-separated criterion gives
`P=1+652t+651t^2+1395t^3+651t^4+63t^5+t^6`.
The valley `652>651<1395` and log-concavity failure
`651^2<652*1395` are checked exactly. The full rank-seventeen subspace and
flat lattices are not enumerated. This distinction is explicit in the
checker output and Appendix L.

The global Z-polynomial in both cases is the Gaussian rank polynomial.
Its adjacent coefficient ratio `(2^(r-j)-1)/(2^(j+1)-1)` gives symmetry
and unimodality. This is a direct formula consequence for these source
examples and does not assert real-rootedness of Z for arbitrary matroids.

## Scope and preservation

The source's known counterexamples concern local P. The global Z and
ordinary, augmented and modified toric cohomology polynomials are kept
distinct. These examples add no solution to an active problem atom.
All 42 complete status rows, the 108 protected Appendix M–N inputs and
the standalone catalogue source/PDF retain their prior bytes. Existing
formal statements and proofs in Appendices G and L are preserved.

The historical external Rethlas experiment is part of the primary source,
not a new local instruction, model call or book verifier receipt. No
current gpt-6.1-sol run is claimed. Cloud-only work continues, Xean remains
suspended, and Siu division and non-nef closure retain their conditions.

Build, source-closure, reference, index, navigation, actual book-page review
and artifact evidence are retained in the companion integration manifest
and artifact record. Frozen prior exports are preserved; an isolated
fresh compilation from the new source archive is not claimed.
