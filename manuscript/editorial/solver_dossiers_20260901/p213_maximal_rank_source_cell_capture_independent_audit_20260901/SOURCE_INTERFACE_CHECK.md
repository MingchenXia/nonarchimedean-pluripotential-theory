# Independent primary-interface checks

Date: 1 September 2026. No new proof status is inferred from compilation
or from the author's source ledger.

## Direct algebraic sources

- Temkin, arXiv:0912.2570v2,
  https://arxiv.org/pdf/0912.2570v2 . Theorems 1.1.3 and 1.1.6 and their
  surrounding remarks, pp.2-3, were read directly. They require
  noetherian quasi-excellent characteristic-zero schemes. Empty-boundary
  regularization preserves the regular locus; divisorial-boundary
  resolution preserves the ORIGINAL SNC boundary locus and its complement.
  Read also the ordered boundary definition 2.1.1, strict monomial/SNC
  definitions 2.1.9 and Lemma 2.1.10, and complete-transform support
  identities 2.2.6 and Lemma 2.2.9(iv). These support the exact preservation
  of U and the generic horizontal support, not reduced semistability.
  The separate theorem permitting a DVR extension is not used.
- Stacks 0F41, https://stacks.math.columbia.edu/tag/0F41 : Nagata
  compactification for separated finite-type maps to a quasi-compact
  quasi-separated base. Spec(R) qualifies. No projectivity assumption.
- Stacks 0HA6, https://stacks.math.columbia.edu/tag/0HA6 : excellence for
  finite-type schemes over a noetherian complete local ring.
- Stacks 0AG0, https://stacks.math.columbia.edu/tag/0AG0 : regular local
  rings are UFDs. This converts zero local divisor into a genuine unit.
- Stacks 0CBN, https://stacks.math.columbia.edu/tag/0CBN : strict SNC
  parameters and regular intersections of the stated codimension.
- Stacks 0539, https://stacks.math.columbia.edu/tag/0539 : torsion-free
  modules over valuation rings are flat.
- Stacks 00NN, https://stacks.math.columbia.edu/tag/00NN : regular
  associated graded polynomial algebra, domains and parameter quotients.
  Its proof explicitly cites Krull intersection (10.51.4), the exact
  finite-order property used in the note.

All these primary pages/theorem passages were read in this audit. The
remote Temkin PDF text was accessible, but a screenshot request for
printed page 3 failed because the reader did not expose a screenshot-enabled
PDF. No local Temkin copy or hash was created; no visual acceptance is
claimed. This does not affect the readable theorem-text scope check.

## CLD source interfaces

Exact local source:

/private/tmp/CLD25.pdf
SHA-256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.

Text:

/private/tmp/CLD25.txt
SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

Directly checked passages:

- Definition 5.2.1 and Proposition 5.2.5, pp.123-125: fixed ambient
  level n, closed maximal-variation source set, pure n-dimensional PL
  structure and immersion by pieces. Ordinary restrictions keep the
  corresponding open pure-dimensional source set.
- Lemma 12.2.3 and proof, pp.334-335: strict approximation and exact
  norm equality on an ordinary neighbourhood, under the almost-good
  hypothesis. Algebraic analytifications here are good. The author's
  rational rather than analytic representative is supplied by the
  algebraic residue-field completion construction, not by misquoting
  this lemma as a global algebraization theorem.
- Lemma 12.9.2(a),(c), p.358, and Section 12.9.5, p.359: injective
  affine invariance and the analytic skeletal setting. This is equality
  of maximal-variation SOURCE sets. The boundary warning preceding
  the lemma is retained; no unrestricted characteristic-skeleton
  assertion is substituted.
- Corollary 15.2.5 and surrounding scope, pp.423-424: compact ordinary
  cutoffs in a locally holomorphically separated analytic space.
  Good separated algebraic analytifications satisfy this hypothesis.
  The finite partition argument needs no global source algebraization.

The full text excerpts were read. Eight complete source PDF pages
123,124,125,334,335,358,359,424 were rendered and inspected under the
read-only PDF skill. SOURCE_QA.json records a zero exit and no warnings,
and the removal of the owned PNG intermediates. No source PDF was edited.

## Predecessor and authorship boundaries

The common-moment note was read completely and its exact formula R and
normalized determinant comparison checked for the optional application.
Its source representation remains conditional. Its 12-entry manifest
and 13 checksums were independently matched.

The original-field model-adaptation diagnostic is source/history context,
not the black-box proof of the new finite rank exception. Its 23-entry
manifest and 24 checksums were matched. Earlier review involvement in
those packets is disclosed in the main audit.

The reviewer's authored nearby-wall candidate has NO dependency role in
the capture proof. The downstream continuity clarification does not
promote that separate candidate or close the current-propagation problem.
