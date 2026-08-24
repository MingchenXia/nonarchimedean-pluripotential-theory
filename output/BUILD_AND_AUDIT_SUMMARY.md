# Non-Archimedean Pluripotential Theory — release and audit summary

Release date: 24 August 2026

## Release artifacts

- PDF: `output/pdf/Non-Archimedean_Pluripotential_Theory.pdf`
- Source archive: `output/source/Non-Archimedean_Pluripotential_Theory_Source_2026-08-24.zip`
- Production-source checksum ledger: `output/PRODUCTION_SOURCE_SHA256SUMS`
- PDF pages: 3,081
- PDF size: 14,845,904 bytes
- PDF SHA-256:
  `666e17884d74a7df85aa85c8c281d7cbc81c8edba3e30b382321f2ae30953eee`
- Production-source ledger: 101 files, SHA-256
  `fa71b10717ff443a5d349f8abb8ee5f78fa097b7d30072c4184e9ac08bc84384`

The author field is intentionally blank in both the title page and the PDF
metadata of this release.

The PDF was built in a fresh empty staging directory from exactly the 101
files in the production-source ledger. A post-build byte comparison showed
that every staged input remained identical to the corresponding canonical
source.

## Scope of the book

The manuscript has six parts, 72 numbered chapters, and 12 appendices. It
develops:

1. valuation, model, Berkovich, metric, and skeletal foundations;
2. the Chambert--Loir--Ducros differential calculus, tropicalization,
   currents, integration, Poincaré--Lelong theory, Bedford--Taylor products,
   delta-forms, and the interfaces with work of Gubler, Künnemann, Rabinoff,
   Jell, and Gubler--Jell--Rabinoff;
3. the nontrivially valued Boucksom--Favre--Jonsson theory, including
   envelopes, Monge--Ampère measures, capacities, energies, variational
   methods, and finite-energy measures;
4. the trivially valued Boucksom--Jonsson theory and a complete modular
   integration of the supplied proof of the envelope property for unibranch
   projective varieties;
5. complex pluripotential prerequisites, rays and test curves, the
   Mesquita--Piccione and MPWN theories, Darvas--Xia trace theory, partial
   Okounkov bodies, and projective and transcendental comparison maps; and
6. the comparison dictionary, hybrid and local valuative theories,
   pseudoeffective MP--DXZ interfaces, verified extensions and
   counterexamples, and a source-scoped research inventory.

## Structural audit

The dependency closure rooted at `manuscript/book.tex` contains 95 canonical
TeX files. Adding the class, bibliography style, index style, two
bibliography databases, and `latexmkrc` gives the 101 production inputs.

- Chapters 1--72 and Appendices A--L are present exactly once and in order.
- Labels: 9,578, all unique.
- Reference occurrences: 30,574, involving 6,470 distinct targets; missing
  targets: 0.
- Equation references: 6,454 uses of `\eqref`; equation/object routing
  errors: 0.
- Raw `\ref`, `\autoref`, and `\pageref`: 0. Object navigation uses
  `\cref` or `\Cref`.
- Citation commands: 3,234; cited-key occurrences: 3,472; distinct cited
  keys: 198.
- Bibliography entries: 499; missing or duplicate keys: 0.
- Formal theorem/lemma/proposition/corollary environments: 1,785.
- Proof environments: 1,821. The structural proof audit found 0 theorem-like
  statements without a proof before the next formal or sectional boundary and
  0 empty proofs. Additional proof environments are second proofs or proofs
  of definition-level and explicitly delimited imported claims.
- Optional parenthetical names on formal statements: 0.
- Examples: 669; every numbered chapter contains at least one.
- Exercise environments, exercise declarations, and exercise headings: 0.
- Open research-problem environments: 22, consisting of one in Chapter 71
  and 21 in Chapter 72. They are research boundaries, not reader exercises.
- The acknowledgements body is empty; the book has no subtitle.
- The excluded erroneous Deligne-pairing paper arXiv:1710.09731 and its title
  occur 0 times in the canonical source and production bibliographies.
- Body typography uses `\rd` for differentials, `\rmi` for the imaginary
  constant, and `\rme` for the exponential constant. The six body instances
  of `\mathrm i` are inseparable-degree subscripts, not the imaginary unit.

## Clean build and rendered-page audit

The clean build used `latexmk` 4.70b with pdfTeX 1.40.22 from TeX Live 2021.
BibTeX and the index were regenerated from an empty staging directory.

The final-log scan found:

- 0 TeX errors or undefined control sequences;
- 0 undefined references or citations;
- 0 multiply defined labels or duplicate PDF destinations;
- 0 overfull horizontal or vertical boxes;
- 0 BibTeX warnings;
- a nonempty bibliography (41,309 bytes) and index (40,964 bytes).

The log contains one harmless class-identity warning because the local class
is loaded as `style/svmono` while declaring its upstream name `svmono`.
It also reports 951 underfull boxes, chiefly from narrow audit tables,
longtables, and the index; these do not protrude into margins. Twenty-two
rendered pages were inspected at 150 dpi, spanning the title and empty
acknowledgements, Parts I--VI, the CLD chapters, Chapters 23, 49, 55, 69,
70, and 72, and Appendix L. No clipping, overlap, broken glyph, malformed
display, or margin intrusion was found.

## Exact-current Rethlas gates

The following six live statement-and-proof integrations were independently
checked with `gpt-5.6-sol` at `xhigh`. Each result is `final/correct`, with
one checked item, zero critical errors, and zero gaps:

| Book block | Run |
|---|---|
| Chapter 23 fixed-skeleton decreasing selection | `20260824T044830Z_25024c43d265` |
| Chapter 49 truncation-energy estimate and sharpness | `20260824T041218Z_0c95825dbb06` |
| Chapter 55 toric zero-mass block | `20260824T052605Z_703e3b501202` |
| Chapter 55 Xia 8.8 metric theorem | `20260824T054849Z_57635bfa07f4` |
| Chapter 55 Xia 8.8 line-bundle specialization | `20260824T061508Z_17bf73c6b37c` |
| Chapter 69 toric numerical-dimension integration | `20260824T070302Z_d706dc98ccca` |

The packet checksum ledger has 88/88 passing entries and SHA-256
`6f01be8f900831203bc6b0cef6bf16560d26ec195be56f8ec07479b4d77c709a`.
The receipt checksum ledger has 14/14 passing entries and SHA-256
`786f1409a2ccba0a94e5c2dcb36e24d3fa732ffaa4b0c903bc7a70b0f3616515`.
All six archived JSON responses agree with their Markdown receipts and exact
live-source extracts.

## Results proved, confirmed, or refuted in the draft

The classifications below are deliberately narrower than a novelty or
priority claim.

- Xia's Conjecture 8.8 is proved in its positive-ideal-volume projective
  scope: connected smooth projective varieties, big line bundles, and the
  stated singular psh metrics. The metric formula and its line-bundle
  specialization have separate exact-current receipts. Zero volume,
  transcendental classes, singular varieties, and attainment of the
  supremum are not inferred.
- A countable finite-maximum approximation is proved on one fixed determining
  dual complex. It is a book-local consequence of published BFJ skeletal
  inputs; the sequence depends on the skeleton, and no global sequential
  cofinality is claimed.
- The centered BJ truncation-energy estimate is proved with the sharp
  coefficient `n/(n+1)`. Retaining the trivial-valuation `j=0` term and
  centering at the finite supremum corrects the earlier false formulation.
- For invariant currents in integral or rational big toric classes, Cao's
  numerical dimension is identified with the dimension of the Newton body.
  This is a verified synthesis of published Cao, Guenancia, and toric
  character inputs, not a priority claim; irrational real classes remain
  outside the theorem.
- The boundaryless PL psh equivalence in the CLD framework is proved by
  log-sum-exp regularization and a legal decreasing-sequence correction. Its
  stated current-positivity implication remains one-way under the explicit
  separatedness hypotheses.
- The formerly listed analytic-trace refinement is closed by the complete
  supplied Darvas--Xia source: input `I`-classes map to output `P`-classes.
  This is a corrected source import, not a new theorem.
- Two overly broad positive expectations are refuted in the stated scopes:
  an `I`-invariant body cannot universally recover actual non-pluripolar
  mass, and cellwise positive data on a weighted cross-fan need not glue to a
  global positive current. The book also proves the fixed-dual-complex
  Radon--Riesz statement while keeping the global version open.
- Earlier audits corrected the BFJ skeletal slope-intersection exponent, the
  missing factor `n` in the MPWN scalar-curvature normalization, and the
  fixed-dual-complex boundary-continuity formulation. Their receipts and
  exact scope are retained in Appendix L and the editorial ledgers.

## Remaining research boundary

No unverified attempted solution is promoted. In particular:

- the BJ22 basic psh-closure package is a source-audited import but has no
  exact-current Rethlas receipt;
- the standalone reduced MP entropy-slope reconstruction remains pending and
  is not asserted;
- the unrestricted full-cone pseudoeffective MP--DXZ comparison remains open;
  the book proves only the sourced divisorial, ideal-valuative,
  projective-rational, and finite-energy Kähler interfaces;
- Xia's zero-volume, transcendental, singular-variety, and supremum-attainment
  extensions remain open;
- irrational-real toric zero-mass numerical dimension and the arbitrary-germ
  finite-energy local theory remain open; and
- the other major CLD, Gubler--Rabinoff, hybrid, Monge--Ampère, and YTD
  residuals are stated with exact hypotheses and attempted-solution dossiers
  in Chapters 69--72 and `output/open_problem_packets`.

This is therefore the strongest defensible release snapshot of the present
draft, not a claim that every open problem in the field has been solved or
that every source-level import has an independent Rethlas receipt.
