# Build and integration report

## Integrated result

The live revision adds:

- conservation of the rational globalization defect along every compatible
  chain in a finite flat tower;
- additive LFS and PL gain formulas across the tower;
- telescoping descriptions by branch-gap increase and globalization-defect
  decrease;
- the no-cancellation theorem: composite exactness is equivalent to
  stagewise exactness;
- simultaneous collapse of all local and global rational, LFS, and PL
  envelopes along a tower when the bottom rational defect vanishes.

Chapter 15 contains the full statement and proof. Chapter 72 and the atomic
inventory record the restriction imposed on tower-based scalar-extension
strategies while preserving the unresolved boundary.

## Verification

- Full `latexmk` build: PASS.
- Output: `book.pdf`, 3303 pages, 17,539,561 bytes.
- PDF SHA-256:
  `b3c1e10c17dd1c2ad6d4d6e3f4e9de0f6fbff5c5c84fe8765ff59ea39004a860`.
- Reference closure: 335 files, 11,217 labels, 0 multiply defined labels,
  0 dangling references.
- Log scan: no undefined citation, undefined reference, or multiply defined
  label diagnostic.
- Mingchen strict audit of the live statement and proof: 0 errors,
  0 warnings.
- `git diff --check`: PASS.
- Atomic inventory: PASS, 46 active atomic questions in 14 formal problem
  environments; tiers T1=0, T2=5, T3=8, T4=16, T5=17.

## Automatic second pass

The second pass made the positive tower length explicit, handled the top
index separately in the lifting argument, and inserted the spacing required
between the preceding transition and the theorem statement. The book was
rebuilt after these changes.

## Visual audit

Rendered and inspected page by page after the second pass:

- Chapter 15 physical PDF pages 767--771 (printed pages 699--703);
- Chapter 72 physical PDF pages 3077--3079 (printed pages 3009--3011).

The theorem, corollaries, displays, proofs, Chapter 72 summary, and adjoining
text are legible. The long tower and gain displays fit the text area,
cross-references are resolved, and no new clipping, collision, or obscuring
overfull box appears on the affected pages.

## Exact live hashes

- `STATEMENT_LIVE.tex`:
  `d12d20d2ed5594474e6258782f146a3986efc4ad6fffe9ef94bb8874cd4cb69b`.
- `PROOF_LIVE.tex`:
  `1d4371f80bf5d034c25fcac19f2cdc60b7bbca64aa4825061f1f02e54d2bd944`.

No model-backed verifier was invoked for this version.
