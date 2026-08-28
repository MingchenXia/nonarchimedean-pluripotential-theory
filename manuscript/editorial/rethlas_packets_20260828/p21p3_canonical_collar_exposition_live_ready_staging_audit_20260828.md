# Canonical-collar live-ready exposition staging audit — 28 August 2026

Status: **STAGING PASS / NONREDUCED EXACT-LIVE GATE OPEN**.

The arbitrary-field nonreduced combined packet has a production PASS, but its
separately materialized exact-live statement/proof bytes have not yet closed
their exact-live verification gate.  None of the prose audited here is a live
book input.  No live, frozen, or older staging file was edited.

## New live-ready prose

The material is split at its actual insertion boundaries:

| insertion role | file | SHA-256 |
|---|---|---|
| before the bridge | `p21p3_canonical_collar_prebridge_transition_live_ready_staging_20260828.tex` | `b4123d598d78338893a0095c7ba416e9e87d6614266533060e33a4795ecf8ec0` |
| first two examples after the bridge proof | `p21p3_canonical_collar_bridge_examples_live_ready_staging_20260828.tex` | `9634c6f281cefd874e5881a03aba490ef1f8e9ed971e1085b71a25ef21cdb9a2` |
| local-to-global transition before the reduced result | `p21p3_canonical_collar_postbridge_transition_live_ready_staging_20260828.tex` | `d075cff2e6d9c69146cbb5a901bee3650c4f6ea69a0832d90c9d8accf47fc8e1` |
| nodal and nonreduced third example after the reduced proof | `p21p3_canonical_collar_reducible_node_example_live_ready_staging_20260828.tex` | `79b11704cc8777bcebdf5c047f231f4b942f2f8f036cce0d84324d36b10f0b88` |

Each file has a non-rendered header carrying only the remaining nonreduced
exact-live gate.  The rendered prose contains no conditional, “subject to
production,” or candidate-status language.

## Reference and mathematical-scope audit

- The reduced consequence uses the exact-live public labels
  `prop:p21p3-curve-rigidity`,
  `itm:p21p3-curve:classification`, and
  `eq:p21p3-curve-classification`.
- The supporting labels that are already public in the exact-live reduced
  files remain
  `prop:p21p3-gfc-smooth-rigidity` and
  `lem:p21p3-gfc-rigid-zero-atom`.
- The nilreduction references use only the intended public label
  `prop:p21p3-curve-rigidity-nonreduced`.
- The transition does not redeclare the verified source-localization
  equations.  It cites
  `eq:p21p3-gf-source-cutoff-factorization`,
  `eq:p21p3-gf-canonical-full-source-collar`, and
  `eq:p21p3-gf-source-separated-ray-preimage`.
- Analytic pullback is written `F^*\beta`; no `F_trop^*` notation and no
  smooth plateau masquerading as an analytic moment occurs.
- The endpoint paragraph uses the exact tropical-dimension-zero vanishing of
  ordinary smooth `(1,1)` test-form germs at type-1 and type-4 points.  It
  reserves the rigid zero-atom lemma for conductor points.
- The ordinary-annulus example explicitly places the collar at an ambient
  type-2 endpoint, so `T(x)` and `f_j(x)` are values of ambient analytic
  germs.  It distinguishes the one-branch calculation from source separation
  in a genuine open star.
- The higher-degree example retains the degree-two closed point of
  `P^1_{F_3}`, the divisor `[p_q]-2[\infty]`, and both calibrated and current
  balancing identities.
- The nodal example cites the public reduced theorem and proves sheetwise
  continuous-psh descent using the rigid zero-atom input.  Its projective
  thickening `Proj K[X,Y,Z]/((XY)^2)` illustrates the future public
  nonreduced proposition: both generic component multiplicities are two,
  while ordinary currents and continuous-pair independence pass through the
  reduction.
- The literal possibly discontinuous scope of CLD Definition 8.6.2 is not
  claimed.
- All prose references use `\cref`/`\Cref`; all equation references use
  `\eqref`; differentials use `\mathrm d`.  There are no optional
  conventional theorem names and no exercises.

## Standalone compile and collision audit

The standalone driver inputs the four already verified exact-live bridge and
reduced files with hashes

```text
f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033
ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5
c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21
01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af
```

It represents the unverified nonreduced public proposition only through the
label-only auxiliary
`p21p3_canonical_collar_nonreduced_public_aux_staging_20260828.tex`, SHA-256
`2543dc83b7301328166a9dc67ce0ee1582bfd0a6c7be24ced68bb29761a37102`.
That auxiliary states no theorem and must be removed when the verified public
nonreduced files are installed.

The compiled source set has 72 label declarations and 72 distinct labels.
Replacing the dummy anchor, for structural testing only, by the presently
materialized nonreduced statement/proof gives 92 declarations and 92 distinct
labels.  This second count is a collision check, not an exact-live verdict.
The new example and equation labels have no occurrence in the current live
`parts`, `appendices`, `frontmatter`, or `book.tex` sources.

`latexmk -gg -pdf -interaction=nonstopmode -halt-on-error` converged to a
19-page preview.  The final log contains no TeX error, undefined reference or
citation, multiply defined label, rerun request, overfull box, or underfull
box.  Pages 1, 8, 9, 17, and 18 were rendered and visually inspected.

| artifact | SHA-256 |
|---|---|
| `p21p3_canonical_collar_exposition_live_ready_staging_compile_20260828.tex` | `1f525fbc0d4955097030460ce8cb78e67d09ef65b5081fc4a22109ed12f53252` |
| `p21p3_canonical_collar_exposition_live_ready_staging_compile_20260828.pdf` | `56eebc4c78b7b02cea1fa753d4a1606a5e79f2265b18a6a000f31b822ef3fdb9` |
| `p21p3_canonical_collar_exposition_live_ready_staging_compile_20260828.log` | `d33a3d0d6224e837eb291942e5e36c221e1df998c8c71bb43c487dae66b62edb` |

The intended rendered order is: pre-bridge transition; exact bridge
statement/proof; first two examples; local-to-global transition; exact
reduced statement/proof; nodal/nonreduced example; exact nonreduced
statement/proof after its exact-live gate closes.
