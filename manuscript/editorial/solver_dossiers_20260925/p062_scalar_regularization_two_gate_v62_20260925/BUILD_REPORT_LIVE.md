# P06.2 v62 live build report

Date: 2026-09-25

## Integration

Chapter 72 now records a two-gate sufficient criterion for P06.2 and its
contrapositive obstruction.  The result separates scalar ascent of the
zero-current equation from regularization of continuous positive-current
functions into the CLD-psh hierarchy.  If both gates hold after one analytic
extension, the function is classically pluriharmonic and locally real PL;
in the pure-dimensional case it is also GJR harmonic.  A counterexample must
therefore fail scalar ascent or exhibit a specific sign outside the CLD-psh
hierarchy.  The atomic inventory records the same reduction without changing
the status or count.

The newly supplied PDF
`global-smooth-psh-counterexample (1).pdf` has SHA-256
`682eec5c367f9cd5d81427173a540b8c87b844ca7803c776344bd21eb117944a`,
identical to
`manuscript/author_sources_20260925/global-smooth-psh-counterexample.pdf`.
That source was already integrated in the P08.1 repair at commit
`ac6e03e2a13fd0533673379bf843d129e6a421d9`; no duplicate import was made.

## Independent verifier

- model: `gpt-6-astra`
- reasoning effort: `xhigh`
- first packet: `wrong`, zero critical errors, one genuine scope gap
- repaired second packet: `correct`, zero critical errors, zero gaps
- final post-copyedit packet: `correct`, zero critical errors, zero gaps

All three exact requests, responses, and HTTP headers are archived in this
dossier.  The final response states that every deduction and dependency
hypothesis passes and that the cited scalar-descent locator matches the
source.

## Mechanical checks

- Focused Mingchen-style audit: zero errors; one reviewed arXiv-status
  warning.
- Minimal compile: pass, one page.
- Forced full-book `latexmk` build: pass.
- Output: 4,070 pages, 19,386,241 bytes, PDF 1.5.
- Final `book.pdf` SHA-256:
  `aa9c78e08019e553a2f61f4a0b9dd63e6881de0239ace6605b4c2b77bd20b9c1`.
- Final log scan: no undefined citation, undefined reference,
  multiply-defined-label, undefined-control-sequence, or LaTeX-error match.
- Inventory checker: 42 active atoms; T1=0, T2=3, T3=7, T4=15, T5=17.
- `git diff --check`: pass.

## Automatic second pass and visual review

The second pass rechecked quantifiers, inheritance of hypotheses, linearity
of the current operator, both uses of pure-dimensionality, the scalar
descent direction, and every non-claim.  It replaced the corollary's shorthand
opening by a complete hypothesis list, preventing accidental inheritance of
the proposition's two sufficient gates.

The final book PDF was inspected on printed pages 3744--3746 (physical pages
3812--3814).  The proposition, corollary, displayed current identities,
proofs, and transition to the dated P06 history are legible and free of
clipping, overlap, or malformed page breaks.
