# Proposed live integration map

Date: 29 August 2026

No live file was edited.  Apply this map only after the exact packet receives
an independent PASS and a production Rethlas `correct` verdict with zero
critical errors and zero gaps.

## 1. Main theorem and proof

Target: `manuscript/parts/part2/ch14_currents.tex`.

- Replace the present block beginning at the theorem labelled
  `thm:cld-positive-support` (currently around lines 2888--2936) with a
  live adaptation of
  `ch14_cld_support_correction_statement_20260829.tex` and
  `ch14_cld_support_correction_proof_20260829.tex`.
- Preserve the existing live label `thm:cld-positive-support` for the
  nontrivially valued assertion.
- In the trivially valued clause, either use the packet's `q`-factor form
  verbatim or reindex it as `q=n-p`; do not reuse one letter for both the
  number of curvature factors and the bidimension.
- Preserve every displayed `\eqref`; rename only labels that collide with
  existing live labels.

This replacement removes the unsupported Berkovich ball-growth paragraph
and installs the proper-tropical-pushforward plus Lagerberg proof.

## 2. Existing route remark

Target: the remark labelled `rem:ch14-support-route`, currently immediately
after the theorem.

- The packet proof already contains this route in full.  Delete the
  duplicated remark, or shorten it to a one-paragraph comparison that points
  to the proof.
- Do not retain language suggesting that the source proves a local estimate
  `mu(B(a,r)) <= C r^p` on the Berkovich space.

## 3. Counterexample and printed-index warning

Target: immediately after the corrected theorem.

- Insert a compact live adaptation of
  `prop:ch14-cld-support-printed-exponent-counterexample`.
- The chapter already proves the tropical identity
  `d'd'' max(0,t)=delta_0` in
  `ex:ch14-convex-corner-restated`; the live adaptation should cite that
  example rather than repeat both integrations by parts.
- State explicitly that the corrected `H^0` hypothesis is not satisfied by
  a singleton.  This prevents later uses of the corrected theorem as a
  point-zero-atom theorem on curves.

## 4. Source notes

Target: the final source-ledger paragraph around lines 3497--3512.

- Attribute the nontrivially valued assertion to CLD Theorem 16.8.5.
- Attribute the trivial scalar-extension mechanism separately to CLD
  Proposition 16.8.2, Proposition 8.7.5, Lemma 16.8.7, and the proof of
  Corollary 16.8.6.
- Record that `H^p` in the printed corollary must be read as `H^(n-p)` when
  `p` counts curvature factors.
- Replace the present unkeyed prose reference to Lagerberg with
  `\cite[Corollary~4.1]{Lag12Super}`; optionally add that it is Corollary 3.5
  in arXiv:1008.2856v1.

## 5. Bibliography

Target: `manuscript/bibliography/NonArchimedean.bib`.

- Add the exact entry from
  `ch14_cld_support_correction_bibliography_addition_20260829.bib` unless an
  equivalent key has been added in the meantime.

## 6. Provenance

Target: `manuscript/appendices/appL_provenance.tex`.

- Add a provenance row recording the source correction, the exact hostile
  audit digest, and the production Rethlas receipt.
- Classify the theorem itself as sourced, the exponent correction as a
  source erratum diagnosed internally from CLD Theorem 16.8.5, and the
  explicit trivially valued kink as a diagnostic example.

## 7. Validation after integration

- Search all live files for `16.8.6` and inspect every occurrence for the
  same index collision.
- Run the full book build twice.
- Require no undefined references or citations and visually inspect the
  theorem, its two cases, and the counterexample pages.
- Stage only the intended files; do not use a blanket add command because
  unrelated quarantine artifacts coexist in the repository.
