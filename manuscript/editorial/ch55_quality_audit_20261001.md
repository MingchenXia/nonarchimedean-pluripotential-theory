# Chapter 55 completion audit

Date: 1 October 2026

Base: local Chapter 54 commit `51ee156`.

Scope: `parts/part5/ch55_okounkov_dh.tex`, under the sequential quality
programme. Chapter 56 is next; the whole-book goal continues. Independent
Chapter 72 research remains paused. Existing validated research proofs and
frozen receipts are preserved.

## Mathematical and expository review

The complete source, 23 formal assertions and eight examples were reviewed.
All assertions have proofs or exact imports. All 46 reusable environments
and all seven sections and four subsections have semantic labels; there are
132 labels. Inline math and equation navigation follow the book conventions.

The principal repairs are:

- The algebraic construction is attributed to the published partial-body
  paper; the transcendental construction and general positive-mass DH
  package are attributed to the supplied lecture. The ordinary
  transcendental-body theorem is identified separately. The published
  paper's remark explicitly leaves its transcendental partial construction
  to later work.
- Surjectivity of the valuation fixes the lattice and prevents an omitted
  index factor. Rational frames and one-dimensional leaves are explicit.
  The almost-semigroup construction is given its counting pseudometric,
  positive-volume completion and exact source interface. It is not the cone
  of every finite-degree valuation point. A pole on the projective line
  computes the multiplier ideals, floor/ceiling discrepancy, actual body and
  raw mass, and demonstrates why that naive cone gives the wrong body.
- Transcendental approximation first uses rational analytic Kähler
  currents with a retained positive margin. Independence uses the source's
  scaled cross-comparison, not cofinality of unscaled ideals. Perturbation,
  correction matrices, closure in the valuative description, positive raw
  mass in dS continuity, ideal projection and real homogeneity have their
  exact interfaces. Minkowski inclusion is not deduced from the reverse
  multiplier-ideal inclusion.
- Convex test curves have a finite terminal level, nonempty compact levels
  and proved positive-volume interior continuity. The convex test-function
  duality now has a full proof, including the interior-simplex argument,
  closed endpoint and inverse level formula. Its energy is explicitly
  unnormalized. Tonelli is applied to a nonnegative difference, so infinite
  negative energy does not produce an undefined subtraction.
- The published finite-energy convention is distinguished from the
  lecture's broader curve definition. A finite DH measure with density
  `1/u^2` on the negative half-line computes infinite energy and all signed
  divergent moments. Flag independence follows directly from the intrinsic
  tail law, including a possible terminal atom. Weak continuity states its
  fixed background and decreasing total-mass hypothesis, proves initial
  mass recovery and tightness, and concludes convergence against bounded
  continuous functions.
- The book's metric DH measure is n! times the body-level measure. The
  section-weight formula and comparison with probability measures explicitly
  convert this mass. The product square computes its superlevel areas,
  density, total mass, first and second moments and finite section weights.
- The existing mixed-volume proof retains its projective positive-ideal-
  volume domain and supremum rather than claiming attainment. The leaf
  argument now proves finiteness of the valuation set before filtering it.
  The rational toric proof uses the proved closed-domain Minkowski identity.
  The irrational-segment example states both positive coefficients.
  Historical receipts are identified as certificates for frozen proof
  objects, not a new independent verification of the edited chapter bytes.
  The Chebyshev question uses its published section locator.
- The adjacent Chapter 54 plan item is reconciled with its established
  ideal-class input and P-class trace output on the Lelong-zero domain.

## Direct source interfaces

Six primary PDFs and 81 rendered source pages were directly inspected.

| Source and version | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Xia, supplied lecture snapshot dated 18 July 2026, matching the historical pin | Counting completion, algebraic bodies, full transcendental construction and volume package, convex duality and energy, positive-mass DH and monotone limits | 340--342, 349--357, 365--371, 374--384, 451--454 |
| Xia, published Geometry & Topology 29 (2025), 1283--1344 | Lattice normalization, ideal counting, almost semigroups, partial bodies and their scope, volume/order/continuity, Minkowski inclusion, finite-energy curve conventions, DH normalization and conjecture boundaries | 10--11, 14--15, 21--22, 26--34, 41, 45--50, 55--56, 61 |
| Wilms, arXiv 2502.18441 v3, uploaded 26 February 2026 | Theorem 1.1 and its common-flag proof | 1, 6--8 |
| Xia, current author-hosted MVOB PDF, separately from the historical supplied proof | Finite-level upper bound, uniform sandwich, analytic approximation and positive-volume formula | 1--11 |
| Kaveh--Manon, arXiv 1610.00298 v4 | Matrix/scalar initial-ideal comparison, Proposition 8.10 and proof | 39--40 |
| Cao, arXiv 1210.5692 v1, 21 October 2012 | Definitions 2--3 and approximation independence; Proposition 4.4 statement and coefficient argument | 4--6, 19--20 |

PDF SHA-256 values, in that order:

1. `c816eea5f06822021fa8dd75b70f82724ee47e6dcd6830729f5ecc109296b706`
2. `b8568896bbf7cdad2dedfc97a8048d3caa75bc800d67f04bfcbadd3705a2a5f9`
3. `7ba48e15de6953c7a19accf5e72ab17d482ad9370b9c180c2b2b8feefead060c`
4. `96eb629a1f168ec5bd394838a00c924a8f709691b8d8dbf978aa0b26b426ca33`
5. `29336df84b61fe8e514ea6cb709a70e810b2fc4cdf51879237c5e00212c30ec4`
6. `17717664b0ae2b154e76e2ecb68c9f63f09dc74be6f25bac7f04b7ee0103b0d6`

The current author-hosted MVOB PDF is a comparison source, not the frozen
proof object covered by the historical receipts. The Kaveh--Manon and Cao
interfaces were checked in the identified preprints. The attempted fresh
Cao publication download returned HTML; a fresh publication-PDF inspection
is not claimed. Other exact imports retain their stated source boundaries
and existing provenance; their PDFs are not counted as freshly inspected.

## Verification and rendered review

The symbolic/exact-rational supplement passes 93,604 checks for pole
integrability and section counts, the honest ceiling semigroup, square DH
moments and finite-weight convergence bounds, infinite signed moments, box
permanents and lower-dimensional toric tube coefficients. These verify
calculations, not the analytic imports.

Scoped checks before and after rendering find no unlabelled reusable
objects, proofless assertions, duplicate labels, nesting errors, legacy
inline delimiters, double-dollar displays or TODO/FIXME/TBD markers. The
legacy writing-audit executable is unavailable; its warning counts are not
claimed. References pass for 425 inputs and 12,099 labels. All six checker
regression tests pass. The inventory remains 42 atoms in twelve environments,
tiers (0,3,7,15,17). Post-render scoped and reference checks and
`git diff --check` pass.

The full workspace-local TeX Live 2025 latexmk build succeeds. Final PDF:
4,118 pages, 19,234,722 bytes, SHA-256
`523b35438c621d5a999a492543aa1ff7f96d3f67679b04218d7d2e70919076b7`.
Final chapter source SHA-256:
`6ebb7a4f4e81a11d778dadafa41425ee0db1a734ab12c6de18a87ae4c8db69d1`.
There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 55 has no overfull boxes or LaTeX/package
warnings. Nineteen overfull boxes elsewhere and thirteen duplicate PDF
destinations in Chapter 70 remain recorded.

All 32 physical chapter pages 3083--3114 (printed 3015--3046) and both
adjoining seams were inspected at detail size. After the final published-
locator correction, the last three pages were reinspected; the preceding
reviewed layout is unchanged. Physical 3114 is intentionally blank. The
Tonelli display was repaired after the first build. No reviewed clipping,
overlap, bad glyph, formula overflow or hierarchy defect remains.

This is a direct editorial/source audit, not an independent-agent verifier
verdict. Generated PDFs remain local review artifacts. Frozen releases,
checksum ledgers and research atoms are unchanged. Verified work remains
local pending explicit remote-push approval.
