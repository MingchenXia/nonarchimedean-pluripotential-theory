# Build report

Date: 19 September 2026

## Live integration

The compact-fiber maximum lemma, the open-map characterization, the scalar
fiber formula, the fiberwise-constancy upgrade, and the type-4 bounded-data
defect are included in Chapter 15.  Chapter 72 and the atomic inventory now
record the resulting exact residual condition.  No P03 atom is retired.

## House-style audit

The Mingchen-writing TeX audit was run on `STATEMENT.tex` and `PROOF.tex`
against the live non-Archimedean bibliography after both editorial passes.
It reported 0 errors and one reviewed warning: `GR25Classical` is still an
arXiv-only entry.  Its pinned v2 text and the cited Section 2.9 statement
were checked directly.

The automatic second pass reread the complete statement-to-proof sequence,
made the type-4 open-disc witness explicit, and rechecked every transition
and displayed formula.  It did not enlarge the mathematical claim.

## Full-book build

The final command was:

    latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex

It exited successfully and reported all targets up to date.  The final PDF
has:

- 3271 pages;
- 17414943 bytes;
- PDF version 1.5;
- SHA-256
  `b6f50cace41735229c3e296047eaf18b8f058eca81667a8ff4eefd00647c3a7e`.

The final `book.log` has SHA-256
`23993ec0c8b104e7377d563c2890635b5bcd0080c77df3566ed3183f8c151ae4`.
A targeted scan found no LaTeX error, undefined control sequence,
undefined citation or reference, multiply-defined label, rerun request,
fatal error, emergency stop, or overfull vertical box.

## Structural checks

- `git diff --check`: PASS.
- Reference checker: 313 files and 11088 labels in the build closure;
  0 multiply-defined labels and 0 dangling references; all per-file
  structures clean.
- Chapter 72 atomic inventory: PASS, with 46 active atoms across 14 problem
  environments; tiers T1=0, T2=5, T3=8, T4=16, T5=17.

## Visual review

The Chapter 15 integration was inspected on physical PDF pages 738--742
(printed pages 670--674).  The Chapter 72 status paragraph was inspected on
physical PDF pages 3046--3047 (printed pages 2978--2979).  The result
hierarchy, displays, proof headings, source locators, transitions, and page
breaks are legible, with no new clipping or overflow.

## Verification boundary

The source and proof audits are recorded in `SOURCES.md` and `AUDIT.md`.
The earlier finite-topology enumeration remains a diagnostic artifact, not
a substitute for the general proof.  No model-backed verifier was used for
this dossier.
