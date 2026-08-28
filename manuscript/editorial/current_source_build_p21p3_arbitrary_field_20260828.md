# Current-source whole-book build after the P21.3 arbitrary-field curve extension — 28 August 2026

This record concerns the current working source after the arbitrary-field
dimension-one current classification and its nonreduced extension were
production-verified and integrated into Chapters 16 and 72 and Appendix L.
It supersedes the 27 August post-P21.3 nonreduced build record for release
decisions about this source state while preserving every earlier record as
dated evidence.

- Result: clean, converged whole-book build.
- Command: convergent `latexmk -pdf book.tex` runs from `manuscript/`; the repository
  `latexmkrc` supplies nonstop mode and halt-on-error.
- PDF: `manuscript/book.pdf`, 3,207 pages, 15,433,695 bytes.
- PDF SHA-256:
  `e2e68023a6b9e7a5e4bd671504d8226f6c1a377c9749bdf0c3745d2932d7c028`.
- Log: `manuscript/book.log`.
- Log SHA-256:
  `d91cbee2b685c928086c8b9f5d9156e4b4f7749eadacc6ff9d94200042a3a983`.
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

Chapter 16 directly inputs the exact production-verified bridge, reduced
statement and proof, and nonreduced statement and proof.  Let \(K\) be any
complete nontrivially valued non-Archimedean field, and let \(X\) be a good,
separated, strict, pure one-dimensional boundaryless \(K\)-analytic space.
The space need not be reduced.  If every irreducible component of
\(X_{\mathrm{red}}\) has rig-smooth normalization, every positive
\(\mathrm d'\)- and \(\mathrm d''\)-closed CLD current of bidegree \((0,0)\)
is a unique locally finite nonnegative combination of the normalized reduced
component currents.  Nilreduction preserves the ordinary and \(G\)-form
calculi, compact-test and weak current topologies, positivity, closedness,
the stated Borel products, and the psh sheaves.  The integration current
retains the generic multiplicities of the fundamental cycle.

For continuous CLD-psh pairs, equality of curvature with respect to the
nonreduced integration current is equivalent to equality after reduction,
and every classified positive closed current has the Bedford--Taylor
independence property.  The proof uses legal analytic-moment localization,
cofinal virtual-annular collars, exact source-ray separation, the common
virtual-annulus expansion index, residual closed points of arbitrary degree,
residual-divisor balancing, and a rigid-point zero-atom estimate.  Smooth
cutoff plateaux are factored through analytic moments and are never treated
as analytic tropical coordinates.

The controlling exact-live nonreduced production run is the complete
HTTP-archived run `20260828T051601Z_db92555a72e1`.  It used
`gpt-5.6-sol` at `xhigh`, returned final `correct`, persisted 23 sequential
statement checks and 25 primary-source checks, and recorded zero failed
checks, zero critical errors, and zero gaps.  The exact-live receipt is
`editorial/rethlas_packets_20260828/p21p3_curve_rigidity_nonreduced_arbitrary_field_live_rethlas_receipt_20260828.md`,
SHA-256
`193e4e63a6f6db4c747189ded171334ccc664f7474cd048fe7f123054f6f1cb0`.
The earlier service-side PASS
`20260828T045515Z_db92555a72e1` used the same materialized bytes but lacks a
client-archived response and safe headers; it is corroborating provenance,
not the controlling run.

The integration preserves the exact scope firewall.  It proves only the
continuous-pair Bedford--Taylor predicate, not the literal possibly
discontinuous predicate of CLD Definition 8.6.2.  It does not treat a
trivially valued field, a non-good or non-strict curve, a curve with boundary,
a component normalization outside the rig-smooth hypothesis, or analytic
dimension at least two.  P21.3 therefore remains one active T2 atom in this
complementary scope.

## Source closure and structural checks

- Source closure: 127 files.
- Controlling ledger:
  `editorial/current_source_closure_p21p3_arbitrary_field_20260828.sha256`.
- Ledger SHA-256:
  `eecc05a93d3cdccf82b6b2411662ac16ce34221f3ced4829613b88119782514b`.
- Every one of the 127 ledger entries passed `shasum -a 256 -c`.
- The production request's statement and proof strings reproduce the six
  mathematical files directly input by Chapter 16, with exactly the
  submission helper's documented separating newlines; `book.fls` records
  all six inputs.
- A live-input scan found 9,913 labels and no duplicate label, and 30,768
  references with no dangling target.  The bibliography audit found 208
  cited keys and no missing key.
- The literal frontier contains 16 formal problem environments and 55 active
  atoms, with tier counts 0/7/14/17/17.
- No exercise environment or exercise heading occurs.  No theorem, lemma,
  proposition, corollary, or claim has an optional conventional name.  The
  author and PDF author fields remain empty, and the acknowledgements have no
  body.

## Visual inspection

The final PDF was rendered with Poppler and inspected as page images.

- Physical pages 737--765 cleanly render the complete Chapter 16
  arbitrary-field curve package: source localization, virtual-annulus
  bridge, examples, reduced classification, nonreduced extension, full
  proofs, and scope firewalls.
- Physical pages 3035--3037 cleanly render the narrowed P21.3 residual
  problem and its neighbouring open-problem transitions.
- Physical pages 3182--3184 cleanly render the corresponding Appendix L
  provenance record and neighbouring entries.

No inspected page has clipping, overlap, malformed display, missing glyph,
or unreadable text.  Headers, footers, page numbers, hyperlinks, margins, and
section hierarchy are consistent.  This is build and integration evidence;
it makes no novelty or priority claim.
