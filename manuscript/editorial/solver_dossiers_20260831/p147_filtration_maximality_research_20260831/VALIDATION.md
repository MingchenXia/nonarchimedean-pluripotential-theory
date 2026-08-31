# Mechanical validation — not mathematical acceptance

All six read-only inputs match their recorded SHA-256 values. No live chapter, source dossier, or inventory was edited.

Three `pdflatex -draftmode` passes and one BibTeX run succeeded in `/private/tmp/p147_filtration_draft_20260831.lVmGlG`. The final log has no undefined references or citations, no overfull/underfull boxes, and no LaTeX warnings. The standalone document has eight draft pages. No PDF exists and no visual QA is claimed.

The new TeX contains 19 unique labels and 12 internal references, with zero duplicates and zero unresolved internal references. A direct monomial enumeration agrees with the blowup dimension formula in all 2436 tested integer cases (`d=1,...,7`, `m=1,...,12`, and every tested vanishing order). These are syntax and arithmetic checks, not a proof of maximality.

`checks.json` contains the exact input rechecks and mechanical results. `MANIFEST.json` freezes all packet files other than itself. The source theorem, conductor argument, endpoint statement, and diagnostics still require fresh independent mathematical review and the unchanged production review gate.

