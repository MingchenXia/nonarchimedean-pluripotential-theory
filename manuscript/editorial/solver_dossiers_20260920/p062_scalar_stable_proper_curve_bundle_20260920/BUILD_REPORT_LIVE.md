# P06.2 scalar-stable proper curve-bundle descent: live build report

Date: 2026-09-20

## Mathematical verification

- The repaired standalone statement and proof were submitted to the local
  model-backed verifier with `gpt-6-astra` at `xhigh`.
- Final verdict: `correct`; critical errors: `0`; gaps: `0`.
- Checked item: `pi_3cceee63c457c144abd9869c`.
- Statement SHA-256:
  `cce5a5ff689f110e02564ee155b75027c3eec06d0e484af8e86dba0662fe9564`.
- Proof SHA-256:
  `b371852f0f87b4a1b382d6f67d792d8b34ba5299ee43e40323b01f7df8ede2d5`.
- The rejected precursor and the repair of its false separability claim are
  retained in the dossier.

## Editorial and structural checks

- Strict Mingchen-writing audit on `STATEMENT_LIVE.tex` and `PROOF_LIVE.tex`:
  `0` errors and `0` warnings.
- Open-problem inventory audit:
  `PASS_OPEN_PROBLEM_INVENTORY`; `46` active atoms across `14` Chapter 72
  environments, with tiers `T1=0`, `T2=5`, `T3=8`, `T4=16`, `T5=17`.
- Build-closure reference audit: `375` files, `11389` labels, `0` multiply
  defined labels, `0` dangling references, and all per-file structures clean.
- `git diff --check`: clean.
- Whole-file house-style audits of the very large legacy chapter files still
  report pre-existing book-wide style debt; this report does not relabel that
  baseline debt as introduced by the present packet.

## Full-book build and visual inspection

- Full `latexmk` PDF build completed successfully with no fatal errors.
- Output: `book.pdf`, `3367` pages, `17818838` bytes, PDF version `1.5`.
- The new Chapter 72 overfull box caused by an inline verifier item identifier
  was removed; the exact identifier remains in this dossier and in provenance.
- Rendered and visually inspected PDF page `1317` (printed page `1249`), which
  contains Proposition 18.8.35 and the beginning of its proof.
- Rendered and visually inspected PDF page `3178` (printed page `3110`), which
  contains the Chapter 72 integration, hashes, verifier result, and residual
  scope.
- Both inspected pages have legible mathematics and citations, with no clipping,
  overlap, or margin overflow in the newly added material.
