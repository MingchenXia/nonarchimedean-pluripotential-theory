# Production Rethlas receipt: exact live arbitrary-field reduced curve theorem

Date: 28 August 2026

Status: **PASS** for the exact live-book statement and proof materialized
from the four files listed below.  The bridge is prepended to the reduced
statement and proof by the submission helper, with exactly one separating
newline.

## Live source bytes

- Bridge statement:
  `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033`
- Bridge proof:
  `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5`
- Reduced statement:
  `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21`
- Reduced proof:
  `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`
- Materialized statement submitted to the service:
  `f2a1c1b9f2a3d9f60422fc1697d31c5265704a73f0c27f180adc36e65d5bbda6`
- Materialized proof submitted to the service:
  `745c842490484fdcba1eebe0bee83cf050b3c8050fafdf751a973615414ce4fe`
- Archived request:
  `28c2c69f5adc388a838365726ce83f95f557aea52108d4408914de9659ab41b6`

Extracting `.statement` and `.proof` from the archived request with no
additional bytes reproduces the two materialized hashes exactly.  The bridge
files are byte-for-byte identical to the separately verified canonical-collar
bridge.  Independent comparison with the verified combined candidate found
only removal of conditional/candidate prose, discharge of the two internal
bridge assumptions after the verified bridge was placed immediately before
the consequence, a synchronized public-label remapping, and two
nonmathematical wording changes.  No formula, external hypothesis, proof
step, or conclusion changed.

## Verifier identity and verdict

- Service run: `20260828T042906Z_f2a1c1b9f2a3`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Started at: `2026-08-28T04:29:06.563958+00:00`
- Verification deadline: `2026-08-28T05:24:06.510244+00:00`
- HTTP status: `200`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`

The service log records the exact model and reasoning configuration.  The
strict output schema was validated before the final report was written.

## Verification records

- Sequential statement records: `17`; all passed.
- Primary-source reference records: `19`; all passed.
- Failed-check records: `0`.
- Primary sources checked: arXiv:1204.6277v2, arXiv:2405.10619, and
  arXiv:2111.05741.

Artifact hashes:

- Archived response:
  `1b305d4e21fc1280efe1787468b7c2101a7d0de964ce54d70cad92921df4bd3c`
- Archived safe headers:
  `4cbca05e289105e26cbeaa051ab3f71897381033d013686ad28ec8e2971f8947`
- Service `verification.json`:
  `13503d522e437ff7c9d16634b51cc65c6572937fd68b5abecc336b4a8b18f9f2`
- Service log:
  `1b55a8cf30c5af09eb52404fc1b4dd65ad0cd77ea44425f0d526db543a290e80`
- Statement checks:
  `98d1c845134de0d3fa64f5fd9c29d7f0fbbfaad1c48e7e4da6712a2dfcf58958`
- Reference checks:
  `b00dbba0eb8022dc6986bef0320f4bec33a829b3e2a0f1b6914ed5f44d84f0a5`
- Failed checks:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Verification-report memory:
  `f1b96c1dffa5ba98f80d7696f43a8a90d7dc50ee3fa9e02def815cdc4b5bd44e`
- Event memory:
  `5240a0552e78ee20b3239847da98872e1b182e6222363caba4356b51518f5b35`

The archived response and service report are semantically identical.  Their
canonical key-sorted compact JSON has SHA-256
`864f62167da67e7a378b04e4190e209cf74ed2abd1022991d777e8e1ce624f96`.
The helper's displayed `checked_items: 0` reflects the absence of a top-level
`checked_item_ids` field; the authoritative service memory contains the 17
statement and 19 reference records above.

## Mathematical scope confirmed

The verified live bytes establish the canonical-collar source localization,
the rigid-point zero-atom estimate, classification of positive closed
bidegree-`(0,0)` CLD currents on connected rig-smooth curves, the reduced
pure one-dimensional classification by normalized irreducible components,
and Bedford--Taylor independence for the stated **continuous** psh pairs over
an arbitrary complete nontrivially valued ground field, under the exact
goodness, separatedness, strictness, boundarylessness, and normalization
hypotheses printed in the theorem.

The receipt does not assert the literal discontinuous-psh form of CLD
Definition 8.6.2, a trivially valued ground field, a non-good or non-strict
curve, a space with boundary, a component normalization outside the
rig-smooth hypothesis, or analytic dimension at least two.
