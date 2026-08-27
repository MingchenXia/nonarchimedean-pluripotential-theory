# Current-source whole-book build after the P21.3 nonreduced-curve extension — 27 August 2026

This record concerns the current working source after reduction invariance and
the nonreduced dimension-one Bedford--Taylor extension were
production-verified and integrated into Chapters 13, 16, and 72 and Appendix
L.  It supersedes the post-P07.1 build record for release decisions about this
source state while preserving every earlier record as dated evidence.

- Result: clean, converged whole-book build.
- Commands: `latexmk -gg -pdf book.tex`, followed by convergent
  `latexmk -pdf book.tex` runs, from `manuscript/`; the repository
  `latexmkrc` supplies nonstop mode and halt-on-error.
- PDF: `manuscript/book.pdf`, 3,193 pages, 15,368,835 bytes.
- PDF SHA-256:
  `f6ac291a3a3e0ba3455b734e41dfd3693f723d311a90abcd8f9edcd9752bab14`.
- Log: `manuscript/book.log`.
- Log SHA-256:
  `762e6b3c8e09cbc597a25d695e4bacc84ae0db8bff2a81580915dc095419796b`.
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
of `prop:p21p3-curve-rigidity-nonreduced`.  For a good separated strict pure
one-dimensional boundaryless analytic space over an algebraically closed
complete nontrivially valued field, with rig-smooth reduced
irreducible-component normalizations, the result removes the reducedness
assumption.  Ordinary CLD forms and compact-test topology, currents and weak
topology, positivity, closedness, the stated products, psh filtrations, and
G-forms pass unchanged to the reduction.  The integration current instead
records the generic multiplicities.  Positive closed currents of bidegree
`(0,0)` are uniquely locally finite nonnegative sums of reduced-component
integration currents, and the Bedford--Taylor predicate is unchanged by the
nilpotent thickening.

The exact bytes passed the production Rethlas endpoint using `gpt-5.6-sol` at
`xhigh`, with final `correct`, zero critical errors, and zero gaps.  The
endpoint assigned no run, item, or status identifier.  Its response is
preserved under the local archive label
`20260827T133151Z_3ee099341ca1`.  The statement and proof SHA-256 digests are
`3ee099341ca1ba77d806082ca2903320fd9db25c448b48f3dab9c2bb607a777e`
and
`b8aac711aafa611750c56a960177182ff1b7b8f78b489d7b43575d03b28b7f43`.

The integration preserves the exact scope firewall.  It does not relax
algebraic closedness, completeness, nontriviality of the valuation, goodness,
separatedness, strictness, pure dimension one, boundarylessness, or
rig-smoothness of the reduced component normalizations.  It proves nothing
in analytic dimension at least two.  P21.3 therefore remains one active T2
atom outside this class.

## Source closure and structural checks

- Source closure: 121 files.
- Controlling ledger:
  `editorial/current_source_closure_p21p3_nonreduced_20260827.sha256`.
- Ledger SHA-256:
  `6f90d646f518ce1950ab2a4af3c8ed1180dd50bcc51ab7754d53a6655a9ef55d`.
- Every ledger entry passed `shasum -a 256 -c`.
- Relative to the 119-file post-P07.1 closure, the path set adds the exact
  P21.3 nonreduced statement and proof inputs.
- The production request's statement and proof strings compare byte-for-byte
  equal with the two files directly input by Chapter 16; `book.fls` records
  both inputs.
- The literal frontier is 15 formal problem environments in Chapter 72 and
  one in Chapter 71, hence 16 book-wide and 55 active atoms, with tier counts
  0/7/14/17/17.
- A live-input label scan found no duplicate label.  No theorem, lemma,
  proposition, corollary, or claim has an optional conventional name.
- No exercise environment or exercise heading occurs.  The author and PDF
  author fields remain empty, and the acknowledgements have no body.

## Visual inspection

The latest PDF was rendered with Poppler and inspected as page images.

- Physical pages 571--573 cleanly render the corrected ordinary-open
  reduction argument in Chapter 13 and its neighbouring transitions.
- Physical pages 746--754 contain the exact proposition, full proof, double
  line example, scope firewall, and the following Bedford--Taylor material,
  without clipping, overlap, malformed display, missing glyph, or unreadable
  line.
- Physical pages 3019--3022 cleanly render the narrowed P21.3 frontier, the
  retirement of the nilpotent-thickening slice, the remaining problem, and
  the following open-problem summary.
- Physical pages 3168--3171 cleanly render the separate reduced and
  nonreduced provenance gates and neighbouring entries.

Headers, footers, page numbers, hyperlinks, margins, and section hierarchy
are consistent on all inspected pages.  This is build and integration
evidence; it makes no novelty or priority claim.
