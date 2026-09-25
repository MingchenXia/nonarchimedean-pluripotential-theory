# P06.2 scalar regularization two-gate reduction: audit

Status: live-integrated, dependency-closed, independently verified, and
full-book built on 2026-09-25.

## Logical chain

1. Scalar ascent gives zero Hessian current for both signs of `h_L`.
2. The signwise regularization gate puts both signs in the CLD-psh
   hierarchy.
3. `thm:cld-to-classical-psh` makes both signs classically psh, hence `h_L`
   classically pluriharmonic.
4. Gubler--Rabinoff Proposition 7.2(6) descends classical
   pluriharmonicity from `X_L` to `X`.
5. `thm:supplied-p061-singular-pluriharmonic` gives local real-PL
   regularity.
6. In the pure-dimensional case, the original zero-current equation and
   `thm:p01-real-pl-positive-current-candidate` make both signs
   semipositive, hence GJR harmonic.
7. The corollary is the contrapositive at each analytic extension.  At the
   identity extension, scalar ascent cannot fail, so one sign is a
   continuous zero-current function outside the CLD-psh hierarchy.

## Scope firewalls

- No pullback of a continuous current through an arbitrary scalar extension
  is asserted.
- No general implication from positive current to CLD-psh hierarchy
  membership is asserted.
- The GJR conclusion and the identification with a counterexample to the
  converse of `prop:cld-psh-positive-current` are explicitly restricted to
  the pure-dimensional scope of that comparison theorem.
- The result is a reduction of P06.2, not a retirement; the active count
  remains 42 and P06.2 remains T2.

## Independent verification history

The first exact `gpt-6-astra`/`xhigh` submission returned `wrong` with one
gap and no critical error.  It correctly observed that the draft called the
identity-extension sign a counterexample to the converse of
`prop:cld-psh-positive-current` without assuming the pure-dimensional scope
of that proposition.  The statement, proof synthesis, Chapter 72 prose, and
inventory were repaired.

The repaired second exact packet returned `correct`, with zero critical
errors and zero gaps.  The automatic second writing pass then replaced an
ambiguous “in the setting of the proposition” in the corollary by a complete
restatement of the ambient hypotheses.  The final third exact packet,
including that clarification, again returned `correct`, with zero critical
errors and zero gaps.  Its archived response is
`rethlas_run3_gpt6astra_xhigh_20260925/response.json`.

## Sources

- The scalar-descent locator was checked in the archived primary-source PDF
  `Gubler_Rabinoff_2506.13548v2.pdf`: Proposition 7.2(6) states the required
  if-and-only-if under every analytic extension.
- The official arXiv metadata checked on 2026-09-25 still identifies v2 and
  contains no journal reference, so the project-local arXiv record is not a
  stale substitute for a listed publication.
- All other dependencies are live internal theorems, listed in
  `SOURCES_LIVE.md` and materialized for the verifier in the two
  `VERIFIER_DEPENDENCIES_*.tex` files.

## Final checks

- Focused Mingchen-style audit: zero errors.  Its sole warning was the
  arXiv-only status checked above.
- Minimal one-page compile: pass.
- Forced full-book compile: pass, 4,070 pages.
- Full log scan: no undefined references or citations, multiply defined
  labels, undefined control sequences, or LaTeX errors.
- Open-problem inventory checker: pass, 42 active atoms with tier counts
  `(0, 3, 7, 15, 17)`.
- Printed pages 3744--3746 (physical PDF pages 3812--3814) were inspected
  page by page; the statement, corollary, proofs, synthesis, and transition
  are complete and visually clean.
- `git diff --check`: pass.

## Exact principal hashes

- `STATEMENT_LIVE.tex`:
  `fb43941c971e1a103f169c824ada5dc092fcd320cec5963b4a3f4afe787d630e`
- `PROOF_LIVE.tex`:
  `725c3b6ed6dcfa4731151883e3f0007a379572150d78361094476bcb54f0f958`
- final verifier request:
  `a06447f9789d27369e76dd56c80b72d619ae5862caa8b44f86cdc5f676c50324`
- final verifier response:
  `1bd82c12b62b7df14ba0dfcd510e8834267571a0e9af36e3bed41833209b0a17`
