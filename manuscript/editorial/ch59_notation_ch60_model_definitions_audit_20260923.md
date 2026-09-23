# Chapters 59–60: notation, model definitions and relative positivity

Date: 23 September 2026.
Baseline: `05bcaed4e563049cdf3c5b47d7fe9182b80ef636`.
Scope: the remaining Chapter 59 notation and source-version cleanup;
Chapter 60's opening model definitions, explanatory transitions and a
point-blowup example. This is exposition and verification of existing
constructions, not a new research theorem or an atom closure.

## Chapter 59 preservation and source locators

All 101 legacy inline-delimiter pairs now use the house convention.
The names of the two definitions are introduced in their bodies instead
of optional headings. The remaining seven MP24 citation occurrences use
the explicitly checked `MPTropicalV2` entry. Its Sections 1–3, Remark 1.3.3
(p. 9), Lemma 1.4.3 and Proposition 1.4.4 (p. 11), Proposition 2.1.6
(pp. 12–14), Definition 2.3.1 (p. 15) and Definition 2.5.1 (p. 20)
were checked in the exact author version. The old generic source sentence
now names that same version. No new published-version locator is inferred.

The existing published MP24 bibliography entry gains only `LABEL = {MP}`.
The BibTeX toolchain and its printed labels MP25a and MP25b are unchanged;
the field also makes the compound surname explicit to the house audit.
No entry or citation key is deleted or consolidated.

All 17 Chapter 59 proof blocks are identical to the baseline after
normalizing inline delimiters and the checked citation keys. No proof,
normalization, semantic label or equation number is changed in that chapter.

## Chapter 60 mathematical checks

The initial model is explicitly projective **over** X times P1 in the
cofinal smooth snc system, not asserted to be an absolutely projective
manifold. Its compact Kähler total space supplies the ambient positivity
used later. A divisor D = sum d_E E and central multiplicities b_E give
vertex values d_E/b_E. Equation 60.4a now defines the potential on the
entire spectrum by composing the affine function with the model retraction,
including proper-support characters. The Chapter 59 compatibility theorem
justifies invariance under further pullback.

Relative nefness is defined on each reduced fibre. The smooth-representative
definition with an arbitrary small negative Hermitian bound, positivity
on singular spaces in local embeddings, and the finite-union criterion
are stated where first used. Every noncentral fibre carries the original
Kähler class. The finite-union result therefore proves that relative
nefness, and separately relative Kählerness, can be tested on the smooth
central primes. Fibre multiplicities remain in the potential normalization;
they do not multiply these restriction tests.

Rational and real model classes remain distinct. The rational class H(alpha)
requires a relatively Kähler representative on **some** normal dominating
model. The existing snc nef-descent proof is preserved; the arbitrary normal
case remains explicitly imported. The zero-dimensional case is stated:
X and its spectrum are points, the model functions are respectively rational
or real constants, and fibrewise positivity imposes no further restriction.

Example `ex:mp-model-positivity-interval` blows up (p,0) on P1 times P1.
The exceptional E and strict central F have multiplicity one,
E² = F² = -1 and E.F = 1. For beta_c = alpha_model - c[E], the two
degrees are c and 1-c. Thus relative nefness holds exactly on [0,1],
and relative Kählerness on this model exactly on (0,1). These conclusions
use all fibre components, with both boundary values included in the nef test.
The ideal I_p+(t) gives the global formula -c min{v(I_p),1}; the minimum
is evaluated first, so the proper-support value and c=0 cause no undefined
product. Rational c gives rational PL data.

For the horizontal strict transform S of {p} times P1, projection gives
alpha_model.S = 0. The chart x=tu has E=(t=0), S=(u=0), proving E.S=1.
Hence beta_c.S=-c for 0<c<1: relative Kählerness does not imply total-space
nefness. At c=0 the function has a relatively Kähler representative on the
product model, but its pullback has degree zero on E. This verifies the
different quantifiers for the nef condition and H(alpha).

All 19 existing Chapter 60 proof blocks are identical to the baseline except
the precise source key and page locator in the first proof. The entire text
from the Fubini–Study model-category warning onward is byte-identical.
The existing maximum, numerical-criterion and analytic-cycle arguments
retain the boundaries recorded in `ch60_relative_nef_audit_20260922.md`.

## Primary sources inspected

- Mesquita-Piccione, [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2),
  dated 18 September 2025, especially Definition 4.1.2 on printed p. 33.
  That page was rendered and inspected; the Chapter 59 locators above were
  checked in the same exact PDF/text. PDF SHA-256:
  `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
  The book does not repeat the source's unrestricted wording about
  reflection of nefness by a holomorphic map; its direct proof uses proper
  surjective modifications of smooth snc models.
- Demailly–Păun, [published Annals PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf),
  Proposition 3.3(ii) and the following paragraph, pp. 1262–1263.
  Both pages were rendered and inspected for the finite-union criterion
  and the singular-space positivity definitions. PDF SHA-256:
  `0fa73d0742f6990e14dd15b6b19dd49b2c3a1b7db69c89785cca98e8edc9c41f`.
  No new claim is attributed to an uninspected published MP theorem.

## Two passes and final validation

The first complete draft passed the full build, reference and inventory
checks, and its changed definition/example pages were rendered and inspected.
The second full statement/proof/source reading rechecked the reduced-fibre
convention, componentwise positivity, rational/real distinction, all endpoint
degrees, global ideal formula and horizontal intersection. It clarified the
relative projectivity hypothesis, supplied the zero-dimensional case and
the transverse chart, repaired the obsolete definition transition, and
shortened the explanation of the H(alpha) quantifier. The final layout
follow-up keeps the model-pair introduction and display together.

- Full `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`:
  PASS, **3,967 pages, 18,876,314 bytes**.
- Reference/input check: 390 TeX inputs, 11,601 unique labels; no missing
  input, duplicate label, dangling reference or per-file structure defect.
- Final log: no undefined reference/citation, multiply defined label,
  rerun request or horizontal/vertical overflow. Existing underfull and
  class warnings remain.
- Inventory check: PASS, 45 active atoms in 14 environments,
  tiers (0,5,8,15,17).
- Changed pages and their boundaries were rendered and visually checked:
  physical 3309–3316 (Chapter 59), 3337–3343 (Chapter 60), and 3964
  (the separate published and author-version bibliography entries).
  This is a scoped page check, not a new all-page visual audit.
- `git diff --check`: PASS.

Final Chapter 59 SHA-256: `e3d78eee4cefe735aec18e28a58f477e084dce5917087c98515289d00e0804eb`.
Final Chapter 60 SHA-256: `5fd7ef3c3c371f3c5c16207ef395c87ba489ec0ad0d906a1b85faf37f4b896da`.
Final bibliography SHA-256: `d53fcee4464bab08425a1384bfbe35d423e3c630ad9341c7a9825c4523c31fda`.
Final live PDF SHA-256: `3417afe1cdac7bdfcd537bc81a3c4bb84635778a7ac05c15d96b2eb2b22ef2c7`.

The strict bibliography-aware Chapter 59 audit reports zero errors and four
warnings; the changed Chapter 60 block reports zero errors and two warnings.
Strict mode exits 1 on those warnings. The reviewed warnings are the existing
chapter-label convention and explicitly versioned author notes/preprints.
The published MP entry is retained separately; the checked author-version
locators intentionally remain version-specific. Xia's notes and MPWN's
preprint status retain the source checks in the preceding unit. No clean
whole-book or whole-Chapter-60 house-style claim is made.

The P12.1 fragment is unchanged, SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied PDF still matches its archived copy byte for byte, SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
Its completed source integration, retirement and supplied-author provenance
remain as recorded in `p121_integration_audit_20260923.md`.
All 45 active atoms, restored CURVE_PSH.tex, author source packets, frozen
statements and proofs, verifier receipts and dated release products are
unchanged. There is no new independent-agent or production-verifier receipt.
The live PDF remains an ignored build product, not a replacement of a dated
release. The overall chapter-by-chapter audit remains ongoing.

Next: inspect Chapter 60's rational ramified-scaling construction and the
domain hypotheses of finite pullback. Retain the already checked maximum
and relative numerical-criterion proofs and the explicitly imported cycle
argument unless a concrete defect is found.
