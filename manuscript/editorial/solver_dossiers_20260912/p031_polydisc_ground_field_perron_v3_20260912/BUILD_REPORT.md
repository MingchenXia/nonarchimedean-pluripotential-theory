# Build report

Date: 19 September 2026

## Live integration

The affine ground-field Perron theorem, its scalar-compatibility upgrade,
the obstacle corollary, and the scalar-projection non-openness proposition
are included in Chapter 15.  The matching claim boundary is recorded in
Chapter 72 and in the atomic inventory.  No P03 atom is retired: the exact
remaining issue is whether upper-semicontinuous regularization commutes
with scalar pullback for the relevant raw supremum.

## House-style audit

The Mingchen-writing TeX audit was run on `STATEMENT.tex` and `PROOF.tex`
against the live non-Archimedean bibliography.  It reported 0 errors and
one reviewed warning: `GR25Classical` is still an arXiv-only entry.  Its
pinned v2 text and all cited locators were checked directly.

The automatic second pass reread the entire statement-to-proof sequence,
the Chapter 15 transitions, and the Chapter 72 status paragraph.  It also
removed duplicated wording in the displayed proof headings.  The
mathematical claims were not enlarged.

## Full-book build

The final command was:

    latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex

It exited successfully and reported all targets up to date.  The final PDF
has:

- 3269 pages;
- 17397803 bytes;
- PDF version 1.5;
- SHA-256
  `f6919a3a87ce803e8e55c4b388e8fd05ddd99fa4e583ee29f28461761f61c2d0`.

The final `book.log` has SHA-256
`a37d386a86dfb69bdab88fcf9b916ead88efebdfcbd3ca1e389c2de53630ac51`.
A targeted scan found no LaTeX error, undefined control sequence,
undefined citation or reference, multiply-defined label, rerun request,
fatal error, emergency stop, or overfull vertical box.

## Structural checks

- `git diff --check`: PASS.
- Reference checker: 311 files and 11076 labels in the build closure;
  0 multiply-defined labels and 0 dangling references; all per-file
  structures clean.
- Chapter 72 atomic inventory: PASS, with 46 active atoms across 14 problem
  environments; tiers T1=0, T2=5, T3=8, T4=16, T5=17.

## Visual review

The integrated Chapter 15 material was inspected on physical PDF pages
734--739 (printed pages 666--671).  The Chapter 72 status paragraph was
inspected on physical PDF pages 3044--3045 (printed pages 2976--2977).
The theorem hierarchy, displays, proof headings, citations, transitions,
and page breaks are legible, with no new clipping or overflow.

## Verification boundary

The source and proof audit is recorded in `SOURCES.md` and `AUDIT.md`.
No model-backed verifier was used for this dossier.
