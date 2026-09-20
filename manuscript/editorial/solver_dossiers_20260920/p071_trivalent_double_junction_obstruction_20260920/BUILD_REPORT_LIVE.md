# P07.1 trivalent double-junction obstruction: live build report

Date: 2026-09-20

## Mathematical and editorial checks

- The repaired dependency-closed verifier result is `correct`, with `0`
  critical errors and `0` gaps.
- Checked item: `pi_5cdbc27108d6b165871775d9`.
- Strict exact-current receipt audit against the archived verifier source:
  `PASS`.
- The rejected precursor is retained in
  `model_run_dependency_closed/`; it identified the shrinking-neighbourhood
  gap that the radial-propagation argument repairs.
- Strict Mingchen-writing audit on the principal statement and proof: `0`
  errors and `0` warnings.
- Principal statement SHA-256:
  `160f5a469a9a43cc0750932b40ba36108d547791dbd0e1a55eeba3221c7315f0`.
- Principal proof SHA-256:
  `563f8b4992f16d95623684533cf4d126ecc74d9d0acf2a4ec527cb6b87318683`.
- A complete second mathematical reading checked the generator case, the
  radial propagation through decreasing limits and sheafification, both
  one-star--line inequalities, and the three-atom mixed violation.  No
  further revision was required.

## Structural checks

- Open-problem inventory audit:
  `PASS_OPEN_PROBLEM_INVENTORY`; `46` active atoms across `14` Chapter 72
  environments, with tiers `T1=0`, `T2=5`, `T3=8`, `T4=16`, `T5=17`.
- Build-closure reference audit: `383` files, `11,439` labels, `0`
  multiply defined labels, `0` dangling references, and all per-file
  structure checks clean.
- The final build log contains no unresolved-reference or rerun warning.
- No box warning occurs while the new principal statement or proof is read.
- `git diff --check`: clean.

## Full-book build and visual inspection

- Full `latexmk` build: success; all targets are up to date.
- Artifact: `manuscript/book.pdf`, PDF 1.5, letter size, `3,385` pages,
  `17,898,224` bytes.
- The new Chapter 16 statement and proof occupy printed pages `828--831`
  (physical PDF pages `896--899`).
- The Chapter 72 status integration occupies printed pages `3135--3136`
  (physical PDF pages `3203--3204`).
- The Appendix L provenance record appears on printed page `3286`
  (physical PDF page `3354`).
- All seven affected physical pages were rendered from the final full-book
  PDF and inspected at source resolution.  Equations, page breaks,
  headings, cross-references, and margins are clear, with no clipping,
  overlap, or malformed glyphs.

## Scope outcome

- The result proves that coupled double-junction moment inequalities are
  necessary already on the trivalent--trivalent product node and that the
  two separate one-factor junction families are insufficient.
- Sufficiency of the mixed conditions remains open.  P07.1 therefore stays
  active, and the global active-atom count is unchanged.
