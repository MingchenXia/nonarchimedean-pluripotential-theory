# Production Rethlas receipt: canonical-collar nonreduced curve addendum

Date: 28 August 2026

Status: **PASS** for the exact materialized statement and proof identified
below.  The packet contains the previously production-verified arbitrary-field
reduced packet as a byte-for-byte prefix, followed by the conditional
nonreduced addendum.  This receipt controls these exact combined bytes; a
future live-book label or status adaptation must receive its own exact
production verification.

## Submitted bytes

- Combined statement:
  `dfdaa04a1cea28df3d689062fb46f513a7f7aea0ce8ac9f2a707f6c56029d6b4`
- Combined proof:
  `f8eb8968f9ae269b621944cde4b114fa5733f1ae4f4b454284a37b70ea545abe`
- Archived request:
  `73d5b83a3ba931eabce31f554cb4574b23df7acb2c15bc9310c85251a3c4d2af`

Extracting `.statement` and `.proof` from the archived request without adding
bytes reproduces the two submitted hashes exactly.  The respective initial
`16165` and `46966` bytes reproduce the production-verified reduced statement
and proof hashes
`c7b249ecc02e5459ca9ddd78f2746aac273ce9088489fd6c12ee16f4715524af`
and
`63affb48756ec64170b2fef92b9fa347b952aab07278901e37e804efcb15bc0d`.

The standalone compile driver, PDF, and final log have SHA-256 hashes
`8933f6851c9e4c83fa42ba62394306a1bf448e659d5d2bcb547e12a29727bdeb`,
`52d53d42a4674d110b63aa3f5f4acf59a0a59c3ccd7dd3fc01cdca9b9bd34556`,
and
`5ac5c235ccb005afe75ee955f1a94e06174afc8e17f2716795a201b1b22c4bcb`,
respectively.

## Verifier identity and verdict

- Service run: `20260828T044008Z_dfdaa04a1cea`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Started at: `2026-08-28T04:40:08.618632+00:00`
- Verification deadline: `2026-08-28T05:35:08.569032+00:00`
- HTTP status: `200`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`

The service log records the model and reasoning configuration in both the
launch command and runtime header.

## Verification records and schema

- Sequential statement records: `24`; every record has status `checked`, an
  empty `critical_errors` array, and an empty `gaps` array.
- Primary-source reference records: `25`; every applicability value is
  `matched` or `matched within the expressly stated continuous-psh scope`,
  with null critical-error and gap fields.
- Failed-check records: `0`.
- The synthesized payload passed the strict output schema with
  `validation.valid = true` and no validation errors, and the final report was
  persisted with verdict `correct`.

Artifact hashes:

- Archived response:
  `83ebf3a291b54f6405c44dac5e8319e65d70dcd79298793c0e46e76ac9dc5f8c`
- Archived safe headers:
  `de1fb9bbb7f3a6bf9c6acdd917072a99dd730c0d7f3ca6c39b7b7947db92b59e`
- Service `verification.json`:
  `959e3ecc05cd0eac81d54ffca09a1e6cb27ba5a8208dfcb6bd64622afe7ba173`
- Service log:
  `b3fb70011cf0de05ff0c78e8df2e6d38624020c7fd36d081ac6ee7127d7d40bf`
- Statement checks:
  `8b0e0af33f42ad41f1418e6c1e8b77c77a11e74f598a38f7382770ed28bbd8b3`
- Reference checks:
  `f38c02da1673b92ef9bdbdcab68eac644344a8e20cf5bbad74b5aafeb6194f7d`
- Failed checks:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Verification-report memory:
  `e0211535156eb2172a7afd1e60964c103402d45bffd36ac64f8a601f7904f6c6`
- Event memory:
  `82241be09295493b69dd7ffff30eba5fcd3dceede33a2b84f143074f759faa37`
- Run metadata:
  `d393d37678e1978eaab4548cbf01895c3f1ba2990277af5eada808833422a70b`

The archived response and service `verification.json` are semantically
identical.  Their key-sorted compact JSON has SHA-256
`16936065c8fff13ceb5fba3073c9bafe68a94862f2e8134fd1aa421f4b06841d`.
The response schema has the three top-level keys `verification_report`,
`verdict`, and `repair_hints`; `verification_report` contains the summary and
empty `critical_errors` and `gaps` arrays.  Consequently any helper display of
`checked_items: 0` would be a summary artifact caused by the absent top-level
`checked_item_ids` field, not an absence of the 24 statement and 25 reference
records persisted by the verifier.

## Mathematical scope confirmed

In addition to the verified canonical-collar reduced prefix, the exact packet
establishes, under the hypotheses printed in the addendum:

- invariance under nilreduction of analytic points, tropical moments,
  ordinary and `G`-form calculus, compact-test topologies, currents,
  positivity, closedness, admissible current products, and the psh sheaves;
- the distinction between
  `delta_X = sum_i m_i delta_i` and
  `iota_* delta_{X_red} = sum_i delta_i`;
- classification of positive closed bidegree-`(0,0)` currents on the possibly
  nonreduced pure curve by the normalized reduced components;
- equivalence of the multiplicity-weighted and unweighted component curvature
  identities, using the strict rigid conductor locus and rigid zero-atom
  lemma; and
- Bedford--Taylor independence for the stated **continuous** psh pairs.

This receipt does not assert the literal discontinuous-psh predicate of CLD
Definition 8.6.2, a trivially valued ground field, a non-good or non-strict
curve, a curve with boundary, a component with non-rig-smooth normalization,
or analytic dimension at least two.  Nilpotents enter through the generic
cycle multiplicities; no nilpotence exponent or transverse vanishing-order
estimate is asserted.
