# Current-source whole-book build after the P07.1 finite-star theorem — 27 August 2026

This record concerns the current working source after first-stage collapse
was proved for finite ambient-induced real-affine stars, production-verified,
and integrated into Chapter 16.  It supersedes the post-P06.3 build record for
release decisions about this source state while preserving every earlier
record as dated evidence.

- Result: clean, converged whole-book build.
- Commands: `latexmk -gg -pdf book.tex`, followed by `latexmk -pdf book.tex`,
  from `manuscript/`; the repository `latexmkrc` supplies nonstop mode and
  halt-on-error.
- PDF: `manuscript/book.pdf`, 3,187 pages, 15,344,143 bytes.
- PDF SHA-256:
  `1516064109f0c8c8ebc38b9c2e9e7a99ff8749d44881578b65c132a44ba6184d`.
- Log: `manuscript/book.log`.
- Log SHA-256:
  `a80d466b3a330c6dee653ec7134e9728a7f8a11bcd5acf7fb33b5e3d7286330a`.
- Final-log audit: no TeX error, undefined control sequence, fatal or
  emergency stop, undefined reference or citation, multiply defined label,
  duplicate destination, rerun request, BibTeX warning, index warning, or
  overfull box.  There are 991 underfull-box notices from the long tables and
  monograph layout.  The only `Warning:` line is the harmless historical
  class-path mismatch: the requested local file `style/svmono` declares
  itself as `svmono`.
- Bibliography and index: generated and included by the converged build.
- `git diff --check`: passed before this record was written.

## Mathematical integration

Chapter 16 directly inputs the exact production-verified statement and proof
of `thm:ch16-collapse-finite-tropical-curves`.  For a finite union of pairwise
distinct half-open rays in a finite-dimensional real vector space with the
ambient-induced smooth and psh-generator sheaves, the theorem identifies the
first decreasing-limit stage and the full generated psh sheaf with the
branchwise-convex junction-Jensen sheaf.  It gives decreasing smooth psh
approximation on one fixed neighbourhood and chartwise descent under
generator-preserving local identifications.

The exact bytes passed the direct production Rethlas endpoint using
`gpt-5.6-sol` at `xhigh`, with final `correct`, zero critical errors, and zero
gaps.  The endpoint assigned no run or item identifier; the response is
preserved under the local archive label
`20260827T103835Z_c8131b22d800`.  The statement and proof SHA-256 digests are
`c8131b22d8002212e31cd526095317734a2b67be5d47f1387e5ee6bc041af5e3`
and
`921e8b46690e69cbacea66bf86cbcdf628e7dbc95651f526d62cc6d755d7cbcf`.

The integration preserves the exact scope firewall.  It does not identify
the ambient-induced generator sheaf with arbitrary analytic, sedentary, or
nonambient tropical smooth structures and proves nothing for infinite-valence
stars or arbitrary higher-dimensional faces.  Thus P07.1 and P07.2 remain
open in their residual scopes.

## Source closure and structural checks

- Source closure: 119 files.
- Controlling ledger:
  `editorial/current_source_closure_p071_20260827.sha256`.
- Ledger SHA-256:
  `4419d2cfb1f64525f81d1e7a21d734c5ed716099c4a4ed9a78d84f641609e962`.
- Every ledger entry passed `shasum -a 256 -c`.
- The path set contains 114 repository-local TeX/class inputs from the
  converged build together with the two bibliographies, BibTeX style, index
  style, and `latexmkrc`, for 119 inputs in total.
- Relative to the 117-file post-P06.3 closure, the path set adds the exact
  P07.1 statement and proof inputs.
- The literal frontier is 15 formal problem environments in Chapter 72 and
  one in Chapter 71, hence 16 book-wide and 55 active atoms, with tier counts
  7, 14, 17, and 17.
- A live-input label scan found no duplicate label.  No theorem, lemma,
  proposition, corollary, or claim has an optional conventional name.
- No exercise environment or exercise heading occurs.  The author and PDF
  author fields remain empty, and the acknowledgements have no body.

## Visual inspection

The latest PDF was rendered with Poppler and inspected as page images.

- Physical pages 431--432 cleanly render the corrected ambient-slope
  convention and cross example.
- Physical pages 679--680 and 692 cleanly render the hierarchy status and the
  extended-real convex model introduction.
- Physical pages 721--729 contain the exact theorem, full proof, example,
  scope firewall, and neighbouring transitions, without clipping, overlap,
  malformed display, missing glyph, or unreadable line.
- Physical pages 1002--1005 cleanly render the revised limitations table.
- Physical pages 3002--3006 cleanly render the P06/P07 frontier, the exact
  finite-star advance, the surviving residual scope, and the following
  local-to-global problem.
- Physical pages 3161--3163 cleanly render the separate toric and finite-star
  provenance gates and the neighbouring entries.

Headers, footers, page numbers, hyperlinks, margins, and section hierarchy
are consistent on all inspected pages.  This is build and integration
evidence; it makes no novelty or priority claim.
