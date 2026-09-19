# Build and integration report

## Integrated result

The live revision adds:

- protected-collar gluing for rational LFS minorants;
- arbitrarily small relatively compact domains with nonempty boundary in the
  connected nontrivial topological range;
- an exact boundary minimax formula for each positive rational globalization
  gap;
- an exact collar representation of the complete rational globalization
  defect;
- a boundary-absorption characterization of zero rational defect;
- an obstacle-level boundary-saturation criterion that collapses the
  rational, LFS, and PL defect ledger;
- propagation of this collapse through every finite flat tower.

Chapter 15 contains the full statement and proof.  Chapter 72 and the atomic
inventory record both the advance and the remaining normal or geometrically
unibranch higher-dimensional obstruction.

## Verification

- Full `latexmk` build after the automatic second pass: PASS.
- Output: `book.pdf`, 3307 pages, 17,559,939 bytes.
- PDF SHA-256:
  `e6b7e01d65a8c58dc2446663298b6e4000e147aa6791460823666d064592c7c4`.
- Reference closure: 337 files, 11,240 labels, 0 multiply defined labels,
  0 dangling references.
- Log scan: no undefined citation, undefined reference, or multiply defined
  label diagnostic.
- Mingchen strict audit of the live statement and proof: 0 errors,
  0 warnings.
- `git diff --check`: PASS.
- Atomic inventory: PASS, 46 active atomic questions in 14 formal problem
  environments; tiers T1=0, T2=5, T3=8, T4=16, T5=17.

## Automatic second pass

The second pass checked every hypothesis from the collar lower bound through
the tower propagation.  It made the tower corollary self-contained by
restating completeness and nontriviality of the valuation, required
`r >= 1`, quantified the stage index before the lifted point, and made the
boundaryless inheritance explicit in the pointwise collapse corollary.  The
book was rebuilt after these revisions.

## Visual audit

Rendered and inspected page by page after the second pass:

- Chapter 15 physical PDF pages 770--774 (printed pages 702--706);
- Chapter 72 physical PDF pages 3081--3083 (printed pages 3013--3015).

The transition, lemmas, theorem, corollaries, definition, proofs, Chapter 72
summary, and adjoining text are legible.  The nested infimum and supremum
displays, tower display, and six-envelope equalities fit the text area;
cross-references are resolved, and no new clipping, collision, or obscuring
overfull box appears on the affected pages.

## Exact live hashes

- `STATEMENT_LIVE.tex`:
  `fcdd83f0a00689612ac4dca622c58d3dadd84eb8477bab164db57d0aa38dfc64`.
- `PROOF_LIVE.tex`:
  `4de2d4616c38600ec93d48ca589977033e5ad1c1db7431daa09a3d51904454fd`.

No model-backed verifier was invoked for this version.
