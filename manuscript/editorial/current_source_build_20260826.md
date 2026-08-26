# Current-source whole-book build — 26 August 2026

This record concerns the current working source after the verified Chapter 18
delta-metric correction.  It supersedes the 25 August current-source build
record for this source state, but it does not alter the separately frozen
24 August release snapshot.

- Result: clean, converged whole-book build.
- Command: latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
  from manuscript/.
- PDF: manuscript/book.pdf, 3,143 pages, 15,146,295 bytes.
- PDF SHA-256:
  54c403acc0de3d609072cdf1be909c1d1557562a0cfedd87c1f9e2f2e5fe8e08.
- Log: manuscript/book.log.
- Log SHA-256:
  6f264879ef7f0331dc747213b5d766679c11785438a818229dfac1a1d6ee47bc.
- Final-log audit: no TeX error, undefined control sequence, fatal or
  emergency stop, undefined reference or citation, multiply defined label,
  duplicate destination, rerun request, or overfull box.
- Bibliography and index: generated and included by the converged build.
- git diff --check: passed.

## Mathematical integration

Chapter 18 now inputs the exact production-verified statement and proof that
separate:

1. the global piecewise smooth Chern form;
2. the canonical residual generalized delta-form of codimension one,
   characterized by all algebraic pullbacks;
3. the ambient codimension-zero Hessian lift required for an ordinary
   delta-metric; and
4. the ambient bidegree after intersection with the tropical cycle.

The corrected exact packet passed production Rethlas run
20260826T011701Z_1e7c96932016, item
pi_a860454e8a0004aa4767207c, using gpt-5.6-sol at xhigh, with final
correct, one checked item, zero critical errors, and zero gaps.  The first
rejected attempt and both repaired quantifiers are preserved with the packet.

## Source closure and structural checks

- Source closure: 109 files.
- Controlling ledger:
  editorial/current_source_closure_20260826.sha256.
- Ledger SHA-256:
  8b16b58ceb11ad3049a7bd42879114988e68db0dd466c6d38a06a5b5a5ad2080.
- Every entry in the ledger passed shasum -a 256 -c.
- The two new production dependencies have SHA-256
  1e7c9693201671bfe90d2843f9894fe2927ebe7d932bca0947b2499eb339075e
  and
  08391542696641113553a71e73d047d68d8b494fc5cd306b9ee6de541468e402.
- Static frontier: 17 formal problem environments and 57 active atoms;
  this correctness repair retires no atom.
- No exercise environment or exercise heading occurs.
- No theorem, lemma, proposition, corollary, or claim has an optional
  conventional name.
- The author field remains empty and the acknowledgements have no body.

## Visual inspection

The five PDF pages carrying the revised transition, full four-part lemma,
source boundary, proof, and following warning were rendered at 130 dpi.
PDF pages 862--866, corresponding to printed pages 796--800, have no
clipping, overlap, malformed links, split display, missing glyph, or
unreadable line.  The long universal-pullback clause and the two-line ambient
representative both fit cleanly.

This is build and integration evidence.  It does not enlarge the scope of
the Rethlas receipt and makes no novelty or priority claim.
