# Smooth Hessian integral comparison: integration audit

Date: 6 October 2026. Baseline work:
`4574e9be5ee2fa651327023e303c02523478ef23`.
Baseline main: `00957114db21b627e97369563032ceda9cea09c7`.

Appendix H.9 explains the attributed smooth Newton-tensor mechanism
and Dinew's published obstruction to integral comparison for products
of eigenvalue sums. Appendix L.65 binds these statements to exact
editions and the preceding source diagnostics. Chapter 68.9.6 links
the coordinate account to its fully nonlinear analytic discussion.
Four bibliography entries are appended without rewriting old entries.

## Mathematical scope

- The argument of the operator is the real coordinate Hessian or
  complex coordinate Hessian, with ordinary unweighted Lebesgue
  measure. A variable Hermitian background is a separate input.
  The book retains `ddc = i/(2 pi) partial bar-partial` and the
  degree-dependent binomial conversion of coordinate polynomials
  to wedge densities. Adding a constant to the operator preserves
  integral comparison.
- The Newton divergence identity requires the Hessian/Codazzi
  symmetry. It is false for arbitrary symmetric matrix fields.
  The imported smooth real sufficiency proposition retains regular
  boundary, a whole admissible segment and positivity of the full
  linearization. Its boundary flux has the comparison sign. The
  complex counterpart is an attributed Newton/Stokes mechanism.
- Signed combinations of elementary symmetric polynomials retain
  a fixed positive convex branch where applicable. The positive
  critical `sigma_3 - sigma_1` branch in complex dimension four is
  distinguished from disconnected components with opposite sign.
- Plurisubharmonicity on complex p-planes is distinct from Gårding
  m-subharmonicity. The positive-factor branch of the product of
  p-eigenvalue sums is distinguished from the whole product-positive
  set. Dinew's published Theorem 4.1 allows universal comparison
  only at the trace/determinant endpoints with exponent one. Its
  proof outline retains the two separate exponent restrictions.
  A radial-only remark does not restore universal comparison;
  viscosity comparison is a separate question.
- The first-variation adjoint test is a necessary condition for a
  smooth operator. It does not establish the preprint's global C1
  classification. Affine normalization, maximality of a branch,
  eigenvalue regularity and the real quartic-jet calculation retain
  the exact-source review's qualifications.
- A raw fixed quotient and a cross-multiplied polynomial define
  different off-solution operators. Smooth comparison does not
  construct an approximation-independent weak measure or establish
  compact comparison with variable coefficients. Signed coordinate
  polynomial densities are not nonpluripolar products.

The two new formal blocks and their source-input proof outlines
are attributed exposition. This checkpoint adds no original theorem,
classification repair, weak-measure construction, model call or
verification receipt. It supplies no general BJ22 homogeneous Siu
or envelope-division input and changes no canonical problem status.

## Reused exact-source evidence

The preceding [source audit](Hessian_null_lagrangian_source_review_20261006.md)
and immutable manifest are reused: 44 actual physical pages in 22
displayed sheets and twelve elementary diagnostics. These comprise
all twelve pages of Dinew–Myga–Sroka 2610.06313v1, all sixteen
physical pages of Dinew's published 2022 article including its cover,
Guan course-note pages 1–6 and Ball author-scan pages 1–10. The
unread remainder of Ball's paper is not counted as reviewed. The
course-note and published layouts retain distinct locators.

This integration adds zero fresh primary-page audits. The source
diagnostics do not refute the preprint's main classification after
possible correction, and no complete independent repair is certified.
The published product obstruction retains its own complete reading.

## Source preservation and validation

The active closure has 425 TeX inputs. Appendix H, Appendix L and
Chapter 68 change; all 422 other active inputs retain baseline bytes.
All 57 pre-existing formal blocks and 23 proof blocks in the edited
files retain their bytes and order. Sixteen labels, eight equation
tags H.8–H.15, three index entries and four bibliography keys are
added. The fifteen Appendix H equation tags are unique and its old
H.1–H.7 tags are preserved. Both preceding bibliography contents are
byte-preserved; only ComplexGeometry.bib receives appended entries.

All 108 protected inputs, 89 prior frozen manifests and 154 prior
exports retain their bytes. The 42-atom canonical inventory retains
its twelve Chapter 72 environments and tiers `(0,3,7,15,17)`.
The native catalogue source/PDF and open editor remain unchanged.
Historical verification receipts retain their original scope.

Required `scripts/validate-manuscript.sh` completes with exit zero,
including reference checks, inventory checks, six existing checker
unit tests and the full book build. There are 12,946 unique labels,
418 cited entries and 713 bibliography keys. The final build has no
TeX error, package or pdfTeX warning, missing character, overfull box,
unresolved reference/citation or rerun request. Its 954 underfull
boxes equal baseline.

The index accepts 784 entries with zero rejection or warning and
426 resolved numeric destinations. Navigation verifies 22,160 named
destinations, 47,325 internal links, 171 URL links, 2,589 contents
entries and six parts, with no invalid destination or internal link.

## Matching final-page reading and release

The final book has 4,438 pages, 20,622,795 bytes, SHA-256
`4815f4dd2231693f7a91a7c49f6326ce47b50d9df75ccbb1d88b7e11a6fb5f56`.
All 48 selected matching final pages were read as complete extracted
text and actually displayed in 24 separate sheet views. The selection
covers affected contents, the Chapter 68 paragraph, Appendix H
introduction/addition/transitions, Appendix L addition/transitions,
the entire index and bibliography. This is a scoped review, not a
fresh full-book rereading.

Reading the first candidate found a duplicate plural index heading.
It was merged into the existing singular heading, then the required
checks and all 48 final selected pages were completed again. The
superseded candidate's 26 actually-read pages in thirteen sheets
are separately preserved and excluded from final-reading counts.
Complete physical-page text comparison with that candidate finds
only page 4415 changed and 4,437 unchanged page texts; pagination
and contents positions are unchanged. Text comparison is not reading.

The final review PDF SHA-256 is
`e816903d60de3337f022345ac9a9f867898ae2380977d42968b125a559bb8162`.
The final reading record SHA-256 is
`a853137db98d0cf23d6001b5bba4d0ac6fb9a48b17a2c4a3ead4465aecd75f38`.
The release gate SHA-256 is
`5f9f6e1ba88126c74a86d995a31d19113320fc25e79de46caba5e062c4c2c2af`.
The immutable manifest retains source gates, exact review selection,
actually-viewed flags and reused source evidence. The external
artifact record gives the release hashes; the closure ledger has
427 TeX/bibliography records. Every source-archive member is compared
with current source bytes. No fresh isolated archive build is claimed.

Publication uses the standing GitHub authorization and a normal
work-branch push. Fetch both main and work before packaging and
retain incoming author progress. Update the existing draft PR after
the push. Continue with the exact hyper-Kähler group-entropy paper
2610.05173v1 and its relevant dependencies before deciding whether
it adds a useful, accurately scoped connection to Chapter 66.
