# Live build report

Build date: 2026-09-20.

Baseline commit and `origin/main` before integration:

```text
fc79f027689993d55c6f088b01981aaa0e521a40
```

## Automated checks

- Mingchen strict TeX audit on `STATEMENT_LIVE.tex` and `PROOF_LIVE.tex`:
  0 errors, 0 warnings.
- Full reference check: 329 files in the build closure, 11,165 labels,
  0 multiply defined labels, 0 dangling references; all per-file structure
  checks clean.
- Final log scan: no undefined references, undefined citations, or multiply
  defined labels.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`, 46 active atomic
  questions, 14 formal problem environments, with tiers T1=0, T2=5, T3=8,
  T4=16, T5=17.
- `git diff --check`: clean.

## Full book build

The project `latexmk` build completed successfully and reported all targets
up to date.

```text
Output: manuscript/book.pdf
Pages: 3291
File size: 17,493,753 bytes
PDF version: 1.5
SHA-256: 483eb880f556181cb9763f5a18b46e4db68893c51446b05cfbb8b8aaf4169db2
```

Existing book-wide underfull and overfull box notices remain in the log.  No
new warning is attached to the v47 statement or proof, and the relevant pages
have no visible overflow or collision.

## Visual inspection

- Physical PDF pp. 757--760, printed pp. 689--692: complete Chapter 15 live
  insertion, including statements, four proofs, and the transition into
  Section 15.15.
- Physical PDF p. 3065, printed p. 2997: Chapter 72 progress summary.

All five pages were rendered at 110 dpi and inspected page by page.  Result:
PASS.  The theorem blocks, displayed formulas, proof endings, hyperlinks, and
paragraph transitions are legible and balanced; no clipping, overlap, orphaned
heading, or bad page break was found.

## Second pass

After the first successful build, the complete live statement and proof were
reread against the source and their internal dependencies.  The source-facing
phrase was tightened from `analytic neighborhood` to `strictly analytic
neighborhood`.  The strict audit, full build, warning scan, reference check,
inventory check, diff check, and page-by-page visual inspection were then
rerun on the revised files.
