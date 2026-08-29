# Non-Archimedean Pluripotential Theory

This repository contains the current second draft of the monograph
*Non-Archimedean Pluripotential Theory*.  The author field is intentionally
left blank in this release.

The last clean 24 August 2026 release snapshot passed the final structural
audit and produced a 3,081-page PDF from its exact 101-file production-source
closure.  That snapshot records nine mathematical production Rethlas
gates: eight exact-current integrations in Chapters 18, 23, 49, 55, and 69,
and one exact frozen statement/proof gate for the Chapter 70 generalized-
Lelong separation theorem, followed by an independent hostile audit.  The
latter is not represented as a post-integration byte-identity gate.  The
additional 25--28 August gates and exact-current integrations are recorded
individually in the editorial receipts and provenance ledgers.  A fresh
current-source whole-book rebuild through 25 August passed and produced a
3,123-page PDF; the dated release artifacts below remain the earlier
3,081-page source freeze until the next release cut.  The integrated
29 August source, including the full projective ample-class MP--BJ comparison
and the exact finite-level closed-immersion reduction for P17.1, also passes a
whole-book build and currently produces 3,284 pages.  These
checks do not turn
source imports or book-level derivations into novelty or priority claims, or
close residual questions outside the displayed theorem scopes.

The manuscript has 72 chapters in six parts and 12 reference appendices.  It
develops:

- valued fields, models, Berkovich spaces, skeleta, and semipositive metrics;
- the Chambert--Loir--Ducros calculus, delta-forms, and tropical methods;
- Boucksom--Favre--Jonsson pluripotential and variational theory;
- Boucksom--Jonsson theory over a trivial valuation, including the supplied
  proof of the envelope theorem for unibranch projective varieties;
- complex and compact Kähler non-Archimedean theories, test curves, tropical
  spectra, and transcendental Monge--Ampère theory;
- comparison theorems, filtrations, hybrid degenerations, and carefully
  delimited research extensions and counterexamples.

## Build

From `manuscript/`, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

The build runs BibTeX and MakeIndex through `latexmkrc`.  The generated PDF is
`manuscript/book.pdf`.  The audited release PDF is
`output/pdf/Non-Archimedean_Pluripotential_Theory.pdf`; the corresponding
source archive is in `output/source/`.  Exact hashes and audit evidence are in
`output/BUILD_AND_AUDIT_SUMMARY.md`, `output/PRODUCTION_SOURCE_SHA256SUMS`,
and `output/RELEASE_ARTIFACT_SHA256SUMS`.

## Editorial records

- `BOOK_PLAN.md`: detailed architecture and chapter plan;
- `LITERATURE_MAP.md`: annotated primary-literature map;
- `RESEARCH_QUESTION_LEDGER.md`: solver and hostile-audit record for open
  questions;
- `author_source_repairs/Mixed_volumes_of_partial_Okounkov_bodies/`: repaired
  source files and the repair log for the supplied proof of Conjecture 8.8;
- `manuscript/editorial/`: hypothesis, notation, provenance, status, and
  mathematical-revision ledgers;
- Appendix L: reader-facing provenance and theorem-status ledger.

The supplied source archives remain locally under `source_material/` and are
intentionally excluded from version control.  Results proved only in the
supplied envelope manuscript are identified as such and are not
misrepresented as previously published theorems.

The editorial records also keep the literal research-frontier inventory at 15
open problem environments, all in Chapter 72, split into 54 active atoms with
tier counts `(0,6,14,17,17)`, together with the source-cutoff
dates, and every remaining mathematical boundary visible.  The clean-build
and exact-current Rethlas gates that have passed are recorded separately from
source imports and unresolved packets.

Downloaded reference copies, temporary build trees, TeX intermediate files,
and superseded release PDFs are also intentionally excluded from version
control.
