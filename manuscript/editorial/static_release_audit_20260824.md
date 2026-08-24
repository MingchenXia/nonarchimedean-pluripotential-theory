# Final static source audit — 24 August 2026

## Scope and current verdict

The audit starts from `manuscript/book.tex`, resolves every uncommented
`\input`, `\include`, and `\draftinclude`, and scans the resulting canonical
dependency closure.  The closure contains 95 TeX files: the driver, notation
file, front matter, 72 numbered chapters, and 12 appendices.  Generated build
trees, temporary slice drivers, and editorial Markdown are excluded.  Citation
keys are checked against both production bibliography databases.

The canonical source is statically clean at this snapshot.  There are no
duplicate labels, missing reference targets, missing citation keys, raw
`\ref`/`\autoref`/`\pageref`, equation references through cleveref, object
references through `\eqref`, formal exercises, optional names on formal
statements, or direct occurrences of the excluded arXiv source.  The three
source defects recorded by the earlier version of this audit were repaired:
the mixed equation/object reference was split, both differential symbols now
use `\rd`, and the final research chapter is named
`ch72_major_open_problems.tex` and included under that name.

This is a static source audit, not by itself a whole-book compile certificate.
The separate release build of the exact 101-file production snapshot has now
succeeded: it produced a 3,081-page PDF, and the final log scan found no
undefined reference or citation, LaTeX error, duplicate destination, or
overfull box.  The source-freeze ledger and artifact digest are recorded in
`output/PRODUCTION_SOURCE_SHA256SUMS` and
`output/BUILD_AND_AUDIT_SUMMARY.md`.

## Checks that passed

- **Labels and references.**  Comment-stripped recursive parsing found 9,578
  label occurrences, all unique.  It found 30,574 referenced-label
  occurrences involving 6,470 distinct
  targets, with no missing target.  There are 0 raw `\ref`, 0 raw
  `\autoref`, and 0 raw `\pageref`.  All 6,454 `\eqref` calls target equations;
  no equation label is passed through `\cref` or `\Cref`, and no object label
  is passed through `\eqref`.

- **Citations.**  The source contains 3,234 citation commands, 3,472 cited-key
  occurrences, and 198 distinct cited keys.  The two bibliography files
  contain 499 entries.  Missing cited keys: 0.  Duplicate bibliography keys:
  0.

- **Excluded Deligne-pairing paper.**  The identifier `1710.09731` occurs 0
  times in the canonical TeX closure and 0 times in the production
  bibliographies; there is no bibliography entry for that paper.  The generic
  Deligne-pairing arguments in Chapters 65--66 point instead to the explicitly
  delimited, unaffected Sections 1--4 of `BHJ19` and cite `BHJ19err`.  A static
  audit cannot prove the absence of every conceptual indirect dependency, but
  no direct or traceable source-level dependency was found.

- **Acknowledgements.**  `frontmatter/acknowledgements.tex` consists of exactly
  the unnumbered chapter heading and its table-of-contents line; it has no body
  text.

- **Exercises.**  There are 0 `exercise` environments, 0 exercise theorem
  declarations, and 0 chapter/section/subsection headings titled “Exercise” or
  “Exercises”.  Nine lexical hits of the English word are descriptive prose or
  source locators, not assignments to the reader.

- **Formal statements and names.**  Across 1,785
  theorem/lemma/proposition/corollary/claim environments, 0 has an optional
  bracketed name.  Named definitions, examples, remarks, and names already
  established in the literature were not treated as violations.

- **Chapter and tag structure.**  The production order contains exactly 72
  main chapters and 12 appendices; the chapter order is unique and complete.
  There are 1,469 explicit `\tag` commands and no duplicate printed tag.  The
  sole tag not carrying a chapter-style number is `\tag{R}` in Chapter 72.  It
  labels the symbolic restriction condition denoted by \(R\), not a manually
  numbered equation, and is an intentional exception that must be preserved.

- **Typography macros.**  The only literal `\mathrm d` in the canonical TeX
  closure is the definition of `\rd` in `style/notations.tex`; book prose and
  formulas use `\rd` (1,427 occurrences).  There is no direct `\mathrm d`,
  `{\rm d}`, or `\textup{d}` bypass in the body.  The source uses `\rmi` 44
  times and `\rme` 348 times.  The six appearances of `\mathrm i` are
  inseparable-degree subscripts, not the imaginary constant.

## Rethlas and provenance boundary

The exact-current production gates for Chapters 23, 49, 55, and 69 are
recorded in `rethlas_verified_results.md` and their receipt directory.  This
static scan does not substitute for those mathematical audits.  Conversely,
the Rethlas verdicts do not certify bibliographic theorem numbers or pages;
the primary-source locator firewall in `rethlas_verification_protocol.md`
applies.  The BJ22 basic-closure integration remains a source-audited import
without an exact-current Rethlas receipt, and the standalone MP reduced
entropy-slope reconstruction remains pending and is not asserted as a theorem.

## Reproducibility summary

The principal literal scans include:

```sh
rg -n --glob '*.tex' '\\begin\{(theorem|lemma|proposition|corollary|claim)\}\s*\[[^]]+\]' manuscript/frontmatter manuscript/parts manuscript/appendices
rg -n -i --glob '*.tex' '\\begin\{exercise\}|\\newtheorem\{exercise\}|\\(chapter|section|subsection)\*?\{[^}]*exercises?' manuscript/frontmatter manuscript/parts manuscript/appendices
rg -n -i '1710\.09731' manuscript/book.tex manuscript/frontmatter manuscript/parts manuscript/appendices manuscript/bibliography
rg -n --pcre2 --glob '*.tex' '(\\mathrm\{d\}|\\mathrm d(?![A-Za-z])|\{\\rm d\}|\\textup\{d\})' manuscript/frontmatter manuscript/parts manuscript/appendices manuscript/style
```

Counts for labels, reference targets, citation keys, chapter order, and tags
were obtained with a comment-stripping recursive parser rooted at `book.tex`;
this is necessary because several production citations and references span
source lines and a line-by-line regular expression undercounts them.
