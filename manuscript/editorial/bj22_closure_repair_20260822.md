# BJ22 closure repair audit, 22 August 2026

## Scope and status

This record covers the repair of `thm:bj-basic-closure` in Chapter 34 and the
dependent citations in Chapter 35.  The mathematical package is imported from
the primary sources listed below.  The integration decisions and replacement
of the former topology statement are **Rethlas verification pending**, not
verified: at `2026-08-22T07:46:21Z` the requested production launch with
`gpt-5.6-sol` and reasoning effort `xhigh` was rejected because the configured
Codex account had reached its usage limit (reported reset time: 27 August 2026,
11:30 AM).  No receipt was produced, and this record makes no Rethlas
verification claim.

After the presentation-only reflow of 23 August, the exact current
theorem-and-proof block `ch34_fs_pl_psh.tex:2466--2588` has SHA-256
`38bd7071c4722348dc8a29f7f890714e8e96e466fc09a814a63fbe93a95a5973`.
Its statement digest is
`50173e9c3be0fae0ea71b5ae2ec013fb107ed0dc427a143d37356fc325cafdcd`,
and its proof digest is
`2b115d0cd2abbf2568e158a8df722f8ec595bf50a0105a76aa69179d521d4093`.
The extraction is the exact UTF-8/LF byte stream from the opening
environment through the closing environment inclusive, including the
terminal LF.  This is the block that must be submitted when the gate becomes
available.

## Primary-source audit

- Boucksom--Jonsson, *Global pluripotential theory over a trivially valued
  field* (`BJ22`), Definition 4.1 and Theorem 4.5: definition of
  `PSH(theta)` and decreasing closure when both functions and numerical
  classes vary.
- `BJ22`, Lemma 4.6: the compactness-based diagonal construction.  Its
  directed set controls the outer index, the order of shifted inner
  approximants, and the class error simultaneously.  A bare disjoint union of
  the inner index sets does not establish directedness.
- `BJ22`, Lemma 4.9 and Theorem 4.7: simultaneous same-class approximation,
  finite maxima, sums, addition of constants, strictly positive scalar
  multiplication, pullback with the componentwise `-infinity` alternative,
  and restriction to irreducible components.
- `BJ22`, Corollary 4.17, Theorem 4.22, and Corollaries 4.23 and 4.25:
  finiteness on the linear (hence divisorial) locus, divisorial comparison and
  determination, and convergence of a decreasing psh net from its divisorial
  limit.
- Boucksom--Jonsson, addendum (`BJ22b`): the addendum retains the above psh
  definition and closure package; its corrections concern the envelope
  property and energy of a regularized envelope.

The repaired scalar statement is deliberately restricted to `a>0`.  A zero
coefficient means that a summand is omitted; it is never evaluated as
`0*(-infinity)`.

## Integration and build audit

The closure theorem now has seven numbered clauses: constants; same-class
finite maxima; sums and positive scalars; fixed-class decreasing closure;
varying-class decreasing closure and closedness in the class; pullback and
component restriction; and divisorial finiteness, comparison, and
determination.  Every numbered reference in Chapter 35 was checked against
this list.  The supporting GF sum calculation was also corrected to place
products in `H^0(X,m(L+M))`, and every convexity argument touched in Chapter
35 now handles endpoint coefficients by omission, rather than forming
`0*(-infinity)`.

The former assertion that pointwise convergence on the divisorial locus
coincides unconditionally with pointwise convergence on all of `X^An` was
removed.  The replacement states only Hausdorffness/determination and the
source-backed decreasing-net conclusion of `BJ22`, Corollary 4.25.

A two-chapter `includeonly` build was run on 22 August from
`tmp/pdfs/part4_ch34_ch35_slice.tex`.  It completed successfully with
`latexmk -pdf -interaction=nonstopmode -halt-on-error`; the output is
`build_part4_closure_slice/part4_ch34_ch35_slice.pdf` (123 pages, 923786
bytes, SHA-256
`544e1c3df794b814901b8b157df2153db6f7f2063e8fc480e51307439487ae15`).
Undefined cross-references and destinations in that log are the expected
effect of the two-chapter `includeonly` slice; there was no fatal TeX error.

That build is a historical integration check; later presentation-only
reflows changed the chapter-file hashes without changing the closure theorem
or proof.  The current chapter file digests are
`0d064f10d313e506a048df34c8f007bafe36db3f530df56f63e9c4c45437b0d9`
for Chapter 34 and
`45d39f528be1a0092be409e24f3aec575256ce10d6782dec831ff12e96a34851`
for Chapter 35.  A current full build belongs to the release gate rather
than to this dated source-audit record.
