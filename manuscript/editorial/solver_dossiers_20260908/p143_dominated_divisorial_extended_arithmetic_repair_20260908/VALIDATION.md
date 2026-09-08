# Validation record

The repair patch is checked against the exact v1 proof with zero fuzz before
any postimage claim is made.  The resulting disposable postimage is compiled
only in LaTeX draft mode, with bibliography and cross-reference checks, so the
source candidate is not modified and no PDF is produced.

The required postimage checks are:

- both original hunk contexts match exactly;
- the patch changes only `proof.tex`;
- the repaired proof contains the explicit positive-coefficient convention
  and the explicit directed net; and
- the final draft log contains no TeX errors, warnings, unresolved references
  or citations, duplicate labels, or box diagnostics.

These are syntactic and reproducibility checks only.  They do not replace an
independent review of the repaired mathematical proof.

## 8 September execution

The patch applied with `git apply --check` to the frozen v1 proof and then
with zero fuzz to a new disposable copy.  Its repaired `proof.tex` SHA-256 is
`04f10c6dc7ae7f60ac6e71f8834f8712e7761d24d0e6a3614134f101c0b08614`.

The disposable postimage was compiled in draft mode with the usual initial
TeX run, BibTeX run, and two final TeX runs.  The final draft log SHA-256 is
`c5ec7383d06cfa94bac240f6fd6162f49109f18e00dd1be1eb47adcfe138a1b6`.
It has no matching diagnostic in the required error/warning/reference/box
scan, and the output directory contains no PDF.
