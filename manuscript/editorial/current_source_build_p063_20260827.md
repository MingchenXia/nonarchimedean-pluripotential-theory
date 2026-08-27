# Current-source whole-book build after P06.3 — 27 August 2026

This record concerns the current working source after ordinary CLD-smooth
monotone regularization on smooth proper curves was production-verified,
integrated into Chapter 19, and removed from the active open-problem
inventory.  It supersedes the post-P09.2 build record for release decisions
about this source state while preserving every earlier record as dated
evidence.

- Result: clean, converged whole-book build.
- Command: `latexmk -pdf book.tex` from `manuscript/`; the repository
  `latexmkrc` supplies nonstop mode and halt-on-error.
- PDF: `manuscript/book.pdf`, 3,181 pages, 15,329,788 bytes.
- PDF SHA-256:
  `c748ff631165674847f2b75916530c65f2b799e94164fe4cfee0a437f1ae3eaa`.
- Log: `manuscript/book.log`.
- Log SHA-256:
  `aac330c5db747f5e80e4780be975722195d38f0ae9885ff98fc3aad7b4e61fde`.
- Final-log audit: no TeX error, undefined control sequence, fatal or
  emergency stop, undefined reference or citation, multiply defined label,
  duplicate destination, rerun request, BibTeX warning, index warning, or
  overfull box.  There are 1,002 underfull-box notices from the long tables
  and monograph layout.  The only `Warning:` line is the harmless historical
  class-path mismatch: the requested local file `style/svmono` declares
  itself as `svmono`.
- Bibliography and index: generated and included by the converged build.
- `git diff --check`: passed before this record was written.

## Mathematical integration

Chapter 19 directly inputs the exact production-verified statement and proof
of `thm:p063-current-psh-ordinary-regularization`.  Over an algebraically
closed complete nontrivially valued field, for a smooth proper algebraic
curve and a continuous function, the theorem identifies current positivity,
Thuillier subharmonicity, and local uniform decreasing approximation by
ordinary CLD-smooth psh functions.  The proof treats all four Berkovich point
types through finite local trees, rational strictification, movement of
residual divisors into fresh directions, ordinary-smooth harmonic germs, and
smooth convex capping.

The exact bytes passed production Rethlas run
`20260827T090645Z_767cbf81c723`, using `gpt-5.6-sol` at `xhigh`, with final
`correct`, zero critical errors, and zero gaps.  The direct endpoint assigned
no item identifier.  Three independent exact-byte mathematical and source
audits passed.  The statement and proof SHA-256 digests are
`767cbf81c723279c1218df4136f8e299465240b325f41f6b0663d001fb5d8a68` and
`d1db3c2db861d920598697fdad5d002a2b1ce947dbdbd95ad9b78b8f9f312bd8`.

The integration preserves two firewalls.  The ordinary CLD-smooth harmonic
counterexample remains valid because it forbids zero-curvature approximants,
whereas the new psh construction carries moving positive curvature.
Moreover, the theorem proves neither arbitrary singular or
`-infinity`-valued curve regularization, higher-dimensional hierarchy
collapse, descent of ordinary-smooth approximants to the standing BFJ base
field, nor a local-to-global BFJ numerical converse.

## Source closure and structural checks

- Source closure: 117 files.
- Controlling ledger:
  `editorial/current_source_closure_p063_20260827.sha256`.
- Ledger SHA-256:
  `9132f4cd13d4ffd28777536c1044511646159e2945090cd5ee7d3bcba06770b9`.
- Every ledger entry passed `shasum -a 256 -c`.
- Comparison with the converged `book.fls` found exactly the same 112
  repository-local TeX/class inputs; the ledger adds the two bibliographies,
  BibTeX style, index style, and `latexmkrc`, for 117 inputs in total.
- Relative to the 111-file post-P09.2 closure, the path set adds four exact
  P21.3 inputs already integrated in the intervening source state and the two
  exact P06.3 inputs.  This explains why the current count is 117 rather than
  113.
- The literal frontier is 15 formal problem environments in Chapter 72 and
  one in Chapter 71, hence 16 book-wide and 55 active atoms, with tier counts
  7, 14, 17, and 17.
- A live-input label scan found no duplicate label.  No theorem, lemma,
  proposition, corollary, or claim has an optional conventional name.
- No exercise environment or exercise heading occurs.  The author and PDF
  author fields remain empty, and the acknowledgements have no body.

## Visual inspection

The latest PDF was rendered with Poppler and inspected as page images.

- PDF pages 948--959 contain the complete statement and proof.  The theorem
  hypotheses, four equivalences/conditions, local-tree construction,
  residual-divisor formulas, convex caps, monotone sequence, and final weak
  closure argument have no clipping, overlap, malformed display, missing
  glyph, or unreadable line.
- PDF page 960 cleanly starts the toric section, so the inserted proof and
  examples terminate without a bad page break.
- PDF page 1000 cleanly renders the revised limitations table: it explicitly
  retains arbitrary singular curve functions and higher dimensions as open.
- PDF pages 2996--2999 cleanly render the P06.3 retirement, the surviving
  P06.1--P06.2 problem, the distinct P07 hierarchy problem, and the following
  transition.

Headers, footers, page numbers, hyperlinks, margins, and section hierarchy
are consistent on all inspected pages.  This is build and integration
evidence; it makes no novelty or priority claim.
