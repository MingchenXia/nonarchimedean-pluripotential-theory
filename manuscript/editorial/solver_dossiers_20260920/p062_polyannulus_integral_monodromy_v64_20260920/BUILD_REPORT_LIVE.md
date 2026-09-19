# P06.2 integral polyannulus monodromy v64: build report

## Integrated result

The Chapter 18 overlap theorem now upgrades the real linear coefficient
monodromy of a locally trivial strict open-polyannulus bundle over a published
curve to a rank-`s` local system of lattices with transition matrices in
`GL_s(Z)`.  The proof adds the one-dimensional analytic-unit lemma and tests
each overlap coefficient on a geometric one-coordinate fibre slice.  The
translation cocycle remains real and zero-current.  No global annular
coordinate, trivial-monodromy, or arbitrary-germ conclusion is asserted.

The corresponding P06.2 descriptions in Chapter 72 and the atomic inventory
were updated.  The active-atom count remains 46.

## Independent model verification

- First frozen run: final `wrong`, zero critical errors, four gaps, all caused
  by omitted book-local dependency statements.  The original request,
  response, and headers are preserved in `VERIFICATION_RUN_20260920/`.
- Repaired frozen run: final `correct`, one proof item checked, zero critical
  errors, zero gaps.  The exact dependency extracts are preserved in
  `VERIFIER_DEPENDENCIES_LIVE.tex`; the request, response, and headers are in
  `VERIFICATION_RUN_REPAIRED_20260920/`.
- Verified proof digest:
  `1ab2003537c0eb427d88b8705672bde5089dd81899c9276a87ce0196a47af8ca`.

## Build and audit

- Forced full build: `latexmk -g -pdf -interaction=nonstopmode
  -halt-on-error book.tex`, passed.
- Automatic second-pass build: `latexmk -pdf -interaction=nonstopmode
  -halt-on-error book.tex`, passed.
- Output: 3333 pages, 17,679,118 bytes.
- Mingchen strict audit, with and without the project bibliography: zero
  errors and zero warnings.
- Reference closure: 355 files, 11,326 labels, zero multiply defined labels,
  zero dangling references.
- Final log scan: no undefined-reference, undefined-citation, or rerun
  warning matched.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`, 46 active atomic
  questions, 14 formal problem environments.
- PDF inspection: physical pages 1289--1293 (complete new statement and
  proofs), 1324 (Chapter 18 synthesis), 3149 (P06.2 detailed status), and
  3177 (Chapter 72 current-results summary).  No clipping, overlap, malformed
  formula, or bad page break was found.

## SHA-256 ledger

| Artifact | SHA-256 |
|---|---|
| `STATEMENT_LIVE.tex` | `12bc0d83c523fa43f2dcb29260db2388b6ef56f29b116dc74811281aadf59862` |
| `PROOF_LIVE.tex` | `1ab2003537c0eb427d88b8705672bde5089dd81899c9276a87ce0196a47af8ca` |
| `AUDIT_LIVE.md` | `85e96098243614a759c2e1a3cb4f9ae87d86c5f4ca0cc0fc977b997c5f73b79b` |
| `SOURCES_LIVE.md` | `798997bcc97ceb05e92a830e776babc7f32ede22ad6d96fa144225f7e7a160ed` |
| `VERIFIER_DEPENDENCIES_LIVE.tex` | `0a97355a1df98125ed429d21b8aa76f29ed4df6f73b0fe8d2ddc6d70743f1990` |
| first request | `eb626fd2e3b7e8341fb19002392edae70451beb07c5e3425ab0e7a6d26650b94` |
| first response | `53ea9aa43e2ce3a491589a73c4d8270f1e7de02022877e6687cb2e39d1bc8d40` |
| first headers | `85f2f240b75ff85662df225324eecef07001d5799115b1cc6ab51c90dffb14c5` |
| repaired request | `9743cce1f78d717a7b70cfacdd9319124cb671fcc5094fbe531b8394ddfe5b09` |
| repaired response | `9d94819e1951108d504ebe8a0e0035bdbfa8b9fe187cb20413b88dcc08584e82` |
| repaired headers | `bd1dafcccabaa9a78b6638659cb91a17b4f3aeb4b4507aa5720d00caa94f9026` |
| `ch18_delta_forms.tex` | `671f76a9cbab97f060efccc2af9d6488cbfe86806131bce0cf8aeb64abcedc20` |
| `ch72_major_open_problems.tex` | `56658503a7931958adbcc15b6536441e6703bb262f253e873de3637e7a1e75c4` |
| atomic inventory | `7d376abbdb4b2a448ea72329b383b6fa0be8cdddb53cc6cf87cc7d31144c5dd4` |
| `book.pdf` | `c93dc026774185b7a1482195f08d6563cecca39ecef4020e0af567de06695f8f` |
| `book.log` | `c94cd872ac1748ebc339edbde33da94dc229f2c65a7a18dced6026a8470d6008` |
