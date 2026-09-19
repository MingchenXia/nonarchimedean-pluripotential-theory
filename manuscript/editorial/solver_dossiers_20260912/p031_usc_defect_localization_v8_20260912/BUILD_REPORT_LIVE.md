# P03.1 upper-regularization defect localization — build report

Date: 19 September 2026

## Live integration

The source-audited theorem and its completed-algebraic-closure corollary
were integrated in Chapter 15.  Chapter 72 and the atomic inventory were
updated in parallel.  The quarantined corollary depending on the
unintegrated v6 packet was excluded, as was the redundant obstacle-family
restatement.

## Two-pass editorial audit

The first pass checked the primary-source statements, the finite-maximum
net, every live dependency, the closure-pullback argument, labels,
citations, and the mathematical claim boundary.  The automatic second pass
reread the theorem, both proofs, both chapter transitions, and the
inventory entry after visual review.  It confirmed that the live text makes
no smallness or removability claim for the defect support and no claim for
further analytic extensions.

The Mingchen TeX audit reported 0 errors and 1 reviewed warning: the cited
Gubler--Rabinoff entry is the repository-pinned arXiv version.  The pinned
PDF has SHA-256
`83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726`.

## Structural and adversarial checks

- build closure: 317 files;
- labels in the closure: 11,092;
- multiply defined labels: 0;
- dangling references: 0;
- per-file structures: clean;
- open-problem inventory: 46 active atoms in 14 Chapter 72 problem
  environments, with tiers T1=0, T2=5, T3=8, T4=16, T5=17;
- finite-topology checker: 389 topologies, 29,577 value assignments,
  330 open continuous surjections, and 1,948 subset pullbacks;
- `git diff --check`: clean.

## Full-book build

Command:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

The final build succeeded and produced a PDF with 3,275 pages, size
17,426,863 bytes, and PDF version 1.5.  The final log scan found no LaTeX
error, undefined control sequence, undefined citation or reference, rerun
request, fatal error, emergency stop, or overfull vertical box.

- `book.pdf` SHA-256:
  `68a19bec44a59b785a27ed3797463446bb6b0fbfc04ef514aa21679cccdf32e8`;
- `book.log` SHA-256:
  `9e60028d1ce2806d264f1ec1fb39e19f8f3a3ec05f6643430294d526e9e5b9f2`.

The final 150-dpi visual audit covered printed pages 675--677 in Chapter 15
and page 2982 in Chapter 72.  The theorem, corollary, proofs, equations,
transitions, and status text are legible and free of local overflow or
collision.

## Verification boundary

This dossier received primary-source, dependency, finite-topology,
structural, build-log, and visual review.  No model-backed verifier was
used for this theorem.
