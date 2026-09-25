# P03.1 curvewise scalar-defect localization: audit

Status: live-integrated, dependency-closed, independently verified, and
full-book built on 2026-09-25.

## Logical chain

1. The intrinsic curve regularization `p_g` is subharmonic by the verified
   rig-smooth curve Perron lemma.
2. The ambient extended-field regularization `h_g` is subharmonic by the
   live affine ground-field Perron theorem over `K'`.
3. Continuous pullback of usc regularization gives `p_g <= h_g`.
4. The canonical-retraction normal form gives `h_g <= q_g` and
   `q_g = v o r o g`.
5. Off the closure of `{h_g < q_g}`, the last two functions agree locally;
   hence `q_g` is subharmonic there.
6. Any local failure point therefore lies in the closure of the genuine
   scalar-retraction defect, regardless of the separate gap `{p_g < h_g}`.

## Non-claims

- No converse to the witness condition.
- No discreteness, polarity, capacity-zero, or removability assertion for
  the defect locus.
- No normal higher-dimensional counterexample.
- No P03 retirement or active-count change.

## Adversarial verification history

The first exact submission to the local `gpt-6-astra`/`xhigh` verifier was
rejected.  It identified one genuine theorem-application error: the draft
corollary replaced its smooth boundaryless test curve by an affinoid
neighborhood, although a nonempty affinoid curve has nonempty relative
boundary and therefore need not remain smooth in the convention used by the
curve test.  It also requested the transitive statements and proofs behind
the canonical section and compact-fiber maximum formula.

The repair keeps the original test curve, which is separated under the
standing convention of Gubler--Rabinoff, and applies the localization theorem
directly.  The second packet also supplies the requested dependency closure in
`VERIFIER_TRANSITIVE_DEPENDENCIES_STATEMENT.tex` and
`VERIFIER_TRANSITIVE_DEPENDENCIES_PROOF.tex`.  The repaired exact statement
and proof received verdict `correct`, with zero critical errors and zero gaps.
Both the rejected packet and the successful resubmission are retained so that
the repair remains auditable.

## Exact frozen principal files

- `STATEMENT_LIVE.tex`:
  `75db7b80043da2f760290b5b2841fb13a504f5794547e093baf01848ac292f3f`
- `PROOF_LIVE.tex`:
  `76c16fe38955ef598a3977a89c1663e172ed41005232ea7bc7998a5a25f726d3`

The successful verifier request ends with these exact files.  Its archived
response is in `rethlas_run2_gpt6astra_xhigh_20260925/response.json`; the
external verifier result directory was
`results/20260925T145835Z_86b0568fa6d6`.  The rejected first result was
`results/20260925T144631Z_09dfad110430`.

## Final checks

- Focused Mingchen-style audit on the exact statement, proof, transitive
  dependency extracts, and minimal driver: zero errors and zero warnings.
- Citation keys `GR25Classical` and `Poi13Angelic` occur in
  `NonArchimedean.bib`; `Berk12` occurs in `ComplexGeometry.bib`.
- Minimal two-page compile and forced full-book compile: pass.
- Full log scan: no undefined references or citations, multiply defined
  labels, undefined control sequences, or LaTeX errors.
- Physical PDF pages 793--795 and 3773--3774 were inspected page by page;
  the theorem, corollary, proofs, Chapter 15 synthesis, and Chapter 72 status
  paragraph are complete and visually clean.
- `git diff --check`: pass.
