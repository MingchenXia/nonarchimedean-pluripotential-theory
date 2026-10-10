# Griffiths positivity and pointwise Chern forms: book integration

Date: 7 October 2026. Baseline and explicitly fetched `origin/work`:
`1e9eb6e8830297b7919d2a8813c4cd1da84c0e69`; fetched `origin/main`:
`00957114db21b627e97369563032ceda9cea09c7`.

The integration adds Appendix H.12, a Chapter 17 orientation connection
and Appendix L.70. Du's exact arXiv:2610.05931v1 construction gives a
smooth Griffiths-positive metric on O(1)^{direct sum r} over complex
projective r-space, for every r at least nine, whose top Chern form is
negative on a nonempty open set. The same bundle has top Chern number
one. The book explains the distinction between a metric-dependent
Chern--Weil representative, its class and its integral.

The final v3 book has 4,469 physical pages and 20,753,987 bytes, SHA-256
`4e85d63a295c450b68e42cdb9b6960996764f9e29625da817319eec2a639f4f5`.
All 54 matching selected final pages were freshly read as complete text
and matching images in 27 individually displayed sheets. The review
includes the complete index and bibliography. This checkpoint is an
attributed literature integration and selected final review, not another
complete ordered book reading or a new original theorem.

## Mathematical scope and reading interface

1. Appendix H explicitly distinguishes ordinary smooth possibly signed
   Chern--Weil forms from nonpluripolar products and full local Cegrell
   products. The convention is Omega=i R/(2pi), with squared line-bundle
   norm and c1=-dd^c log h. The local negative quadratic jet carries its
   2pi factor and oriented volume, each factor i dz wedge dbarz being
   twice the real oriented area.
2. The positive-map dictionary uses rank-one tests and spectral
   decomposition. The apolar pairing is bilinear; the Gaussian form
   conjugates determinant because its polynomial coefficients are real,
   without restricting the Gaussian matrix to the Hermitian locus.
3. The nine-by-nine map uses the explicit unitary skew J and the
   Breuer--Hall rank-one projection argument. The block determinant
   identity extends polynomially across singular middle matrices.
   Independent-entry Cayley constants 24 and 8 and exact weighted
   Gaussian moments 24 and 72 give -48 and the coefficient -1536 t^3.
   No simulation determines that sign.
4. Appended scalar diagonal entries preserve the determinant coefficient
   at zero perturbation. A positive trace perturbation makes the map
   strictly positivity improving; polynomial continuity keeps the
   coefficient negative for sufficiently small rank-dependent perturbation.
5. Du Proposition 3.2 supplies global realization. The book explains the
   common vanishing first jets, uniform local negative-Hessian bound,
   H=O(s), partial H=O(sqrt(s)), logarithmic cutoff and O(1/L) cross
   errors. The positive first-derivative quadratic curvature term is
   retained. This is the stated local patching construction, without a
   general convexity assertion for Griffiths-positive metrics.
6. The rank-two and rank-three positive cases retain exact source scopes.
   Rank-three normalization uses positivity-improving exact scaling;
   trace-three sphere averaging, Schur's eigenvalue inequality and F3/3!
   give the stated positive scalar. Higher-rank c3 is treated by
   pointwise principal curvature blocks and tangent-plane restriction.
   Arbitrary holomorphic subbundles with induced metrics need not retain
   Griffiths positivity. Stronger Nakano/dual Nakano Schur positivity
   remains a separately attributed input.
7. Chapter 17 connects this distinction to its first-Chern line-bundle
   products. Its non-Archimedean higher-rank total-space smooth-metric
   obstruction remains unchanged. No higher non-Archimedean Chern
   construction or singular product is introduced.
8. The least negative top-Chern rank remains a source-scoped literature
   direction. Read positive cases and the rank-nine example leave ranks
   four through eight as candidates in that question; this is not an
   exhaustive intervening-literature audit or a new canonical problem atom.

## Exact editions and reused source audit

The [source audit](Du_Griffiths_Chern_source_review_20261007.md) and its
immutable manifest, SHA-256
`ad08ef86a89e04b9bcde6dd4c3d37da787dbafad0ae692e99ba332a7785374b0`,
are reused. They record 68 distinct exact-source/page pairs, all fresh
in that preceding audit, displayed on 35 sheets. Du's fourteen-page v1
and Wan's sixteen-page v2 were read completely. Published Finski
(17 of 41 actual pages), published Caracciolo--Sokal--Sportiello
(7 of 121), Hall v1 (4 of 16) and Idel v1 (10 of 101) are partial
selections. This book integration adds no fresh primary-source reading.

Twenty-four scoped source records and twenty-one passing elementary
diagnostics retain their existing scope. Finski's technical form-pushforward
proof, Gurvits's original complete scaling proof and the signed-Segre and
lower-degree Schur inputs are not declared fully read or independently
certified. Adjacent formula slips in dependency sources stay distinct
from the unrefuted Du construction. The preceding raw-symbolic diagnostic
failure and exact acquisition-text restoration record remain preserved;
neither is relabeled as a mathematical source error.

Six exact-edition bibliography keys are appended:
`Du26GriffithsTopChernV1`, `Finski22CharacteristicPublished`,
`CaraccioloSokalSportiello13CayleyPublished`, `Hall06PositiveMapsV1`,
`Wan26ThirdChernV2`, `Idel16MatrixScalingV1`. Appendix L records the
published/arXiv edition and actual selected pages separately, including
Hall's later internal typesetting date and distinct journal title.

## Numbering repair and final validation

Partial v1 reading displayed five sheets with ten pages. Sheet five
revealed that nine new automatic equations restarted at H.1 after the
legacy explicit H.24. That partial record is retained with SHA-256
`377a9869a53c1a6ad36531ae2b891e910759a8a37097916f0fa8a75f8cc7ce17`.
The v2 edit supplied explicit H.25--H.33 tags. Its layout gate then
reported 23 duplicate automatic hyperlink-anchor warnings because of
the unstarred equation environments. That failed gate and matching log
are retained. V3 uses explicitly tagged starred equations, matching
legacy practice; all nine destinations are distinct valid AMS anchors.
These are editorial defects and repairs, not mathematical source errors.

Final source gate SHA-256:
`120608bded4b647c823e9ab3c44ca224dd1cf21c55ed8d33839d7be7d7b896bb`.
Final release gate SHA-256:
`58ce704ead47921343ee3fd3c0bd1d099fd69389e17fc13384cee2173e819c42`.
Final actual reading record SHA-256:
`cb2bde400c74ba93f5c4fcd02eddf998da4314ba952b7f38304281c8f1b00a11`.
No successful frozen gate or earlier artifact is overwritten.

The required command
`TEXMFHOME=/workspace/.texlive scripts/validate-manuscript.sh`
completed with exit code zero. It includes repository reference checks,
the canonical inventory check, existing unit tests and the full book
build. Final checks find:

- Zero TeX errors, LaTeX/package warnings, pdfTeX warnings, missing
  characters, overfull boxes, unresolved references/citations or rerun
  requests. The existing 954 underfull boxes remain unchanged.
- 449 used entries among 744 unique bibliography keys; zero BibTeX warnings.
- 794 accepted index entries, zero rejected, 1,065 output lines and zero
  index warnings; 793 numeric page groups resolve to 431 distinct pages.
- 22,281 named destinations, 47,537 valid internal links and 171 URL links;
  zero invalid internal/named destinations. All six parts and all 2,614
  contents entries have valid page ranges.
- Fifteen new labels, nine new formula tags H.25--H.33, with all 24 legacy
  H equation tags and auxiliary numbers preserved, and two new index
  entries. The active closure has 12,997 unique labels and no dangling
  references.

The selected final physical pages are 67, 70, 1121--1123, 4035--4036,
4062--4069, 4224--4229 and 4437--4469. Every one of the 54 pages and
27 matching sheets was freshly read/displayed in v3; no earlier reading
was reused. These include the Chapter 17 connection, Appendix H scope,
entire new explanation and transitions, Appendix L provenance and
transition, and the complete ten-page index and twenty-three-page
bibliography. The intentional blank verso before Appendix M was checked.

## Preservation and publication

All 112 prior formal blocks and 63 prior proof blocks in the three
changed active files retain exact bytes and order. No formal or proof
environment is added. The 425-member active TeX closure has the same
members; 422 other active inputs are byte-identical. All 108 protected
inputs, 99 preceding frozen manifests and 169 exports retain their bytes.
The non-Archimedean bibliography, book entry file, index configuration,
gitignore and native catalogue source/PDF are preserved. The open native
editor is neither changed nor reopened.

All 42 canonical problem atoms and status tiers 0/3/7/15/17 remain
unchanged. No original theorem, independent model call, new production
receipt, Xean run or general BJ22 Theorem 6.21 Siu/envelope-closure repair
is added. Historical verification receipts are not extended.

Save immutable book, selected-review PDF and source ZIP in the existing
research-integration export directory, with a 427-input source closure.
The inherited 758 source-archive members plus six current evidence members
give 764 members, each checked against its repository bytes; no fresh
isolated archive compilation is claimed. The current external artifact
record is excluded from its own source ZIP.

Both main and work are explicitly fetched before publication. Publication
uses a normal work-branch push and an update to the existing draft PR 2,
preserving earlier history. Continue incoming-author progress and related
recent primary-source research after this checkpoint.
