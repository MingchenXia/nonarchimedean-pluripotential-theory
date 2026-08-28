# Current-source whole-book build after the P00.1 projective MP--BJ comparison — 28 August 2026

This record concerns the current working source after the full projective
ample-class Mesquita--Piccione--Boucksom--Jonsson comparison and its rational
DXZ corollary were production-verified, integrated, and removed from the
active open-problem inventory.  It supersedes the P21.3 arbitrary-field build
record for release decisions about this source state while preserving every
earlier record as dated evidence.

- Result: clean, converged whole-book build.
- Command: convergent `latexmk -pdf book.tex` runs from `manuscript/`; the
  repository `latexmkrc` supplies nonstop mode and halt-on-error.
- PDF: `manuscript/book.pdf`, 3,209 pages, 15,454,115 bytes.
- PDF SHA-256:
  `3a6d9ca097f32fba6c07c20fd7a11f2d2b0eddb91a15f9d14132cd78114509c1`.
- Log: `manuscript/book.log`, 237,506 bytes.
- Log SHA-256:
  `5dd43406cb541e179f3a6369cbb9bccf86db735ab3b40fc03937a581fa0ad645`.
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

For a connected smooth projective complex variety and every ample real
Néron--Severi class, Theorem `thm:pseff-projective-full-mp-bj` proves that the
canonical GAGA homeomorphism identifies the rational PL relative-nef
Mesquita--Piccione and Boucksom--Jonsson model cones and identifies their full
decreasing completions on all semivaluations.  For an ample rational
line-bundle class, composition with Darvas--Xia--Zhang, Theorem 3.14 gives the
full DXZ--MP order isomorphism without a finite-energy hypothesis.

The proof keeps the exact scope firewall: it does not cover nonprojective
compact Kähler manifolds, transcendental classes outside real
Néron--Severi space, non-nef classes, Monge--Ampère or energy compatibility,
or equality of the MP relatively Kähler locus with the BJ
Fubini--Study/dominating locus.  It algebraizes finite flag-ideal
presentations, not arbitrary analytic test configurations.

The frozen candidate statement/proof SHA-256 values are

- `e40829e3586bcabeeb866229dc068c2e518a736fc908dec32f3bf3957c59c9ab`;
- `baad23068e9dcae47619f3e2d81cfd26fa5bd51b1e4c4d4baa1a7c024824e671`.

The production archive `p001_mp_bj_full_cone_run_20260828` returned
`correct`, zero critical errors, and zero gaps.  Its request/response/safe
header SHA-256 values are

- `5247582aa59d492ecc683c2740eac8783528df9dacb0b49aedb710c08dab677a`;
- `b2e490edd946e0c32d2e59ba941d77cc38425956f4cde0ecc82f49adc173917f`;
- `c9dcbbbaae1d0b1064b9e21df6976bee6c7c647306cec57a85e43ea4588b4371`.

The final exact-live statement/proof SHA-256 values are

- `949819c48c8d0e991acbb92ed7c15d504dd691056f06553c58ac1d4ab564d33e`;
- `58c2954ad1e541ab41e0649c4e84e22252299265b422159df41fe5772f2e8064`.

They reproduce exactly Chapter 71, lines 818--864 and 866--1026,
respectively, and exactly reproduce the materialized strings in
`p001_mp_bj_full_cone_live_run2_20260828/request.json`.  The superseding
exact-live response returned `correct`, with empty critical-error and gap
arrays, and explicitly checked the cited numbered primary-source statements.
Its request/response/safe-header SHA-256 values are

- `0117a2a2669e2980b620e9fedc53d9ca6fb59c9b8d312f9fa46935dad82bcea6`;
- `aa83284548a249c6e1538a7d0c352e6181936e4d79455b5a8f980400aec8b960`;
- `1bf4eb42373b4422429660ca6be4c02fd27681fdd3ea3e76a52dd1edbe05c862`.

The integration receipt is
`editorial/rethlas_receipts_20260828/p001_mp_bj_full_cone_live_integration_receipt_20260828.md`,
SHA-256
`84dbd2096962ad8a9865642b65705ea33ef51b1797846f4a8a98334a835cc6c2`.

This result is a book-level, source-explicit synthesis of published MP, BJ,
and DXZ inputs.  It makes no novelty or priority claim.

## Source closure and structural checks

- Source closure: 127 files.
- Controlling ledger:
  `editorial/current_source_closure_p001_20260828.sha256`.
- Ledger SHA-256:
  `88faf5f75884e19295d642d7f66d0aef7b29b9fa50f3f50b2eb7a1fc29a086b5`.
- Every one of the 127 ledger entries passed `shasum -a 256 -c`.
- The path set is unchanged from the 127-file P21.3 arbitrary-field closure.
  Nine live build inputs have new hashes: Appendix L and Chapters 57, 58, 60,
  63, 64, 65, 71, and 72.
- The final log has no duplicate label, undefined reference, or missing
  citation.  The bibliography audit has no missing cited key.
- The literal frontier contains exactly 15 formal problem environments, all
  in Chapter 72, and 54 active atoms, with tier counts `(0,6,14,17,17)`.
- P00.1 and `prob:pseff-projective-rational-full-link` are absent from the
  active frontier.
- No exercise environment or exercise heading occurs.  No theorem, lemma,
  proposition, corollary, or claim has an optional conventional name.
- The author and PDF-author fields remain empty, and the acknowledgements
  have no body.

## Visual inspection

The final PDF was rendered with Poppler at 130 dpi and inspected as page
images.

- Physical pages 2997--3000 cleanly render Theorem 71.7.2, equations
  (71.42)--(71.44), and the complete proof.
- Physical page 3178 cleanly renders the detailed Appendix L provenance and
  the exact-live hashes and archive identifiers.
- Physical page 3181 cleanly renders the Appendix L comparison-ledger entry.

No inspected page has clipping, overlap, malformed display, missing glyph,
margin overflow, or unreadable text.  Headers, footers, page numbers,
hyperlinks, margins, and section hierarchy are consistent.  This is build
and integration evidence; it makes no novelty or priority claim.
