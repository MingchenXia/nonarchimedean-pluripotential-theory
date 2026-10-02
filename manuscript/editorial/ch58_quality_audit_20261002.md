# Chapter 58 completion audit

Date: 2 October 2026

Base: local Chapter 57 commit `6c08bf0`.

Scope: `parts/part5/ch58_tropical_spectra.tex`, under the sequential quality
programme. Chapter 59 is next; the whole-book goal continues. Independent
Chapter 72 research remains paused. Frozen proofs and receipts are preserved.

## Mathematical and expository review

The complete source, fourteen formal assertions and five examples were
reviewed. Every assertion has a proof or exact import. All 27 reusable
environments and eight numbered sections have semantic labels; there are
66 labels. Inline mathematics follows the book convention.

The principal checks and repairs are:

- The target is explicitly the compact positive tropical semiring. Ideal
  characters are nonnegative by the unit-sum identity. No unrestricted
  compactness claim for the source's larger general-semiring target is
  imported. The affine family includes the zero polynomial, the residue
  character at the infinite endpoint and its finite truncation.
- A new reduction proposition proves that nilpotent coherent ideals have
  infinite value. Local nilpotence and a finite compact cover give one
  nilradical exponent. Quotient and inverse-image ideals give inverse
  continuous character maps and a compact-Hausdorff homeomorphism. The
  empty space is included. The dual-number example identifies all three
  ideals and their values; it distinguishes the ideal semiring from its
  character space. This is a direct deduction, not a newly imported theorem.
- PL density now proves closure under sums, positive rational scalars and
  finite maxima using ideal products, powers and common denominators. Every
  rational PL function is a difference of positive generators. The displayed
  difference identity proves lattice closure. Its uniform closure is a real
  vector lattice, so the precise Stone--Weierstrass argument also proves
  density of the rational space. Extended ideal functions remain unchanged.
- Support and center retain the strong Noetherian sheaf input, finite global
  ideal sums and global-prime convention. The nodal example separates global
  primeness from stalk primeness. Point-local reconstruction uses coherent
  truncations, the product sandwich and increasing extended limits, including
  an infinite point-ideal value.
- The bimeromorphic full-support bijection retains its conductor argument,
  finite cancellation, ideal order reflection through normalized blowup,
  weighted relative ample construction and normalization square. The nodal
  normalization example delimits both ideal descent and proper supports.
- Proper algebraic recovery keeps exact proper GAGA, stalk-ideal extension,
  the colon-ideal comparison, all valuation rings in properness, and the finite
  closed affine-center cover for topology. It includes nonprojective proper
  varieties, nonnormality, zero ideals and trivial valuations. The Gauss and
  sine examples explain the nonproper restrictions. The multiplier-ideal
  bridge preserves its divisorial Legendre domain and order of infimum and
  supremum. The separate positivity comparison remains Chapter 71's theorem.

The three dated support, bimeromorphic and recovery audits remain historical
records of their identified bytes, not independent receipts for this revision.

## Direct source interfaces

Two primary PDFs and thirteen rendered source pages were directly inspected.

| Source and version | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Mesquita-Piccione, arXiv 2409.06221 v2, 18 September 2025 | Positive ideal characters, PL functions, global primeness, support, point-local valuations and full-support modifications | 6--14 |
| SGA 1, recomposed and annotated SMF reprint, 2003, arXiv math/0206203 v2 | Expose XII, Proposition 1.3.1 and Theorem 4.4: exact, faithful proper coherent GAGA | 257--258, 265--266 |

PDF SHA-256 values, in that order:

1. `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`
2. `8e64218d356456c534eebf996940f0f957e43b54f1a080241debe12cbaf60d3c`

Three Stacks statements and their proofs were read from fresh HTML retrieved
on 2 October 2026: Tag 00H3 (Lemma 10.38.2, integral equations and Rees
algebras), Tag 01PF (Lemma 28.23.2, extension of finite-type submodules), and
Tag 0BX5 (Lemma 29.43.1, properness and all valuation rings). HTML SHA-256:

1. `eade0411f2cb0cedf1c8bbe0ba935b7b91eb7d59ec13d71b636420fe7b10efa9`
2. `3ff3fdedfdd2b732dd0fa0bc35a28f3852f5f526119c6ac0d423bd90cfdd489e`
3. `1634a6edadbb19f62f10a3878e081d17b6d7c42e5185ce60962f510ecf54788a`

The numbered Mesquita-Piccione locators belong to the identified author
version, separately from the published entry. Other analytic imports retain
their named interfaces and preceding checks; no further fresh-PDF inspection
is claimed. The archived source file is preserved byte for byte.

## Verification and rendered review

The exact integer/rational supplement passes 1,504 checks and separately
enumerates 5,461 candidate characters of truncated polynomial rings. It
checks nilpotent values, polynomial products and sums, the local ideal
sandwich and truncations, PL sum and lattice identities, nodal conductor
cancellation and Gauss ideal coordinates. These calculations do not verify
the analytic or topological imports.

Scoped checks before and after rendering find no unlabelled reusable
objects, proofless assertions, duplicate labels, nesting errors, legacy
inline delimiters, double-dollar displays or TODO/FIXME/TBD markers. The
legacy writing-audit executable is unavailable; its warning counts are not
claimed. References pass for 425 inputs and 12,142 labels. All six checker
regression tests pass. The inventory remains 42 atoms in twelve environments,
tiers (0,3,7,15,17). Post-render scoped and reference checks and
`git diff --check` pass.

The full workspace-local TeX Live 2025 latexmk build succeeds. Final PDF:
4,122 pages, 19,258,283 bytes, SHA-256
`6ad5a532ba0ee01993aacb761e1f8b71b892edd51197bdf7e921d33f47a14b4f`.
Final chapter source SHA-256:
`e6bed6600121e9207dc2bf612f7d89a0e91b94db2d028e1e27c8aa53635ac745`.
There are no unresolved references or citations, missing glyphs, rerun
requests or fatal errors. Chapter 58 has no overfull boxes or LaTeX/package
warnings. Nineteen overfull boxes elsewhere and thirteen duplicate PDF
destinations in Chapter 70 remain recorded.

All eighteen physical chapter pages 3145--3162 (printed 3077--3094) and
both adjoining seams were inspected at detail size after the final grammar
repair. Physical page 3162 is intentionally blank. No reviewed clipping,
overlap, bad glyph, formula overflow or hierarchy defect remains.

This is a direct editorial/source audit, not an independent-agent verifier
verdict. Generated PDFs remain local review artifacts. Frozen releases,
checksum ledgers and research atoms are unchanged. Verified work remains
local pending explicit remote-push approval.
