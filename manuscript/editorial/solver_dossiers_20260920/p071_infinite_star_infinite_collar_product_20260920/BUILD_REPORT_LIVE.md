# P07.1 exact infinite-star × infinite-collar product: live build report

Date: 2026-09-20

## Mathematical and editorial checks

- Final typography-corrected dependency-closed verifier result: `correct`,
  with `0` critical errors and `0` gaps.
- Checked item: `pi_7f64cae4c772b9edf730c3eb`.
- Strict exact-current receipt audit: `PASS`; the materialized request agrees
  byte-for-byte with the five statement dependencies, the five proof
  dependencies, and the final principal files.
- Strict Mingchen-writing audit on the final principal statement and proof:
  `0` errors and `0` warnings.
- Principal statement SHA-256:
  `ec4503f598beba8b853e18a50561d476b754f5f0bf615ff221e26e78a36c6576`.
- Principal proof SHA-256:
  `d915ae5a407e65ef82a9eb02d205c0cd3e8871e6ba0c8dfec94b182d2edff49c`.
- The rejected first request and its exact response remain archived.  The
  intervening mathematical pass is also retained because the subsequent
  visual audit changed only two TeX spacing-command backslashes; the final
  corrected bytes were resubmitted and accepted.

## Structural checks

- Open-problem inventory audit:
  `PASS_OPEN_PROBLEM_INVENTORY`; `46` active atoms across `14` Chapter 72
  environments, with tiers `T1=0`, `T2=5`, `T3=8`, `T4=16`, `T5=17`.
- Build-closure reference audit: `379` files, `11420` labels, `0` multiply
  defined labels, `0` dangling references, and all per-file structures clean.
- `git diff --check`: clean.

## Full-book build and visual inspection

- Full `latexmk` PDF build completed successfully; a final check reported all
  targets up to date.
- Output: `book.pdf`, `3379` pages, `17867706` bytes, PDF version `1.5`.
- The build-log block for the new statement and proof contains no overfull
  box warning.
- Rendered and visually inspected PDF page `893` (printed page `825`),
  containing the corrected derivative inequality and the end of the proof.
- Rendered and visually inspected PDF page `3196` (printed page `3128`),
  containing the new Chapter 72 scope and final verification record.
- Both inspected pages have legible mathematics and citations, with no
  literal spacing commands, clipping, overlap, or margin overflow in the new
  material.
