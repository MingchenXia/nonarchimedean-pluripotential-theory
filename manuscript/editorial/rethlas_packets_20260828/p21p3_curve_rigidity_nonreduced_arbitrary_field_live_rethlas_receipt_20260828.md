# Production Rethlas receipt: exact live arbitrary-field nonreduced curve theorem

Date: 28 August 2026

Status: **PASS** for the exact live-book statement and proof materialized from
the six files listed below.  The controlling production run is the complete
HTTP-archived closure run `20260828T051601Z_db92555a72e1`.

## Live source bytes

- Bridge statement:
  `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033`
- Bridge proof:
  `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5`
- Reduced statement:
  `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21`
- Reduced proof:
  `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af`
- Nonreduced statement:
  `e7b9889f6c063d9952d61c0472290183aac07b58c8d0569cfebc5e9ea73f1a9c`
- Nonreduced proof:
  `25fe49a46b1c5cd62b0d1a5024095b47cdd49c66f594d1d86eec4f9f270c83ec`
- Materialized statement submitted to the service:
  `db92555a72e145591f922b3ffc623148dcaca7d252ea220d694203b04d164c49`
- Materialized proof submitted to the service:
  `b13829d962614f35af3f3725eb04be1d6f1b6b78490cb13d65e4ed43a05de779`
- Archived closure request:
  `d0cc30cbd8110de827077054d6320900865fff3d06657d9c659e412cadb79f64`

Extracting `.statement` and `.proof` from the archived request without adding
bytes reproduces the two materialized hashes exactly.  Independently joining
the three statement files, and separately the three proof files, with the one
additional newline inserted by the submission helper at each file boundary
reproduces the same submitted bytes.

The six-file compile driver, PDF, and final log have SHA-256 hashes
`c93392ec3e9df492693c475917b759a866562616429e60d2552569fdf720bdb3`,
`3d4752b254684e6767770234d87fa2eb3de0bcee2a1411ae93c50fcf2990a68e`,
and
`7790f772aec5b2fc437855664fe2b37f56d1c4c03c433771e4f835dd064c0ee6`,
respectively.  The standalone build produced 20 pages without an error,
warning, undefined reference or citation, duplicate label, or overfull or
underfull box.

## Verifier identity and verdict

- Controlling service run: `20260828T051601Z_db92555a72e1`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Started at: `2026-08-28T05:16:01.119258+00:00`
- Verification deadline: `2026-08-28T06:11:01.065472+00:00`
- HTTP status: `200`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`

The service log records the exact model and reasoning configuration in both
the launch command and runtime header.

## Verification records and schema

- Sequential statement records: `23`; every record has status `checked`, an
  empty `critical_errors` array, and an empty `gaps` array.
- Primary-source reference records: `25`; every applicability value is
  `matched` or `matched within the expressly stated continuous-psh scope`,
  with null critical-error and gap fields.
- Failed-check records: `0`.
- The synthesized payload passed the strict output schema with
  `validation.valid = true` and no validation errors.  The final report was
  persisted with verdict `correct`.

Artifact hashes for the controlling run:

- Archived response:
  `e2e7d8943b8a4f5bbd677065299bda3ebae0d22be10a71f2962ae38c40830f3f`
- Archived safe headers:
  `0e23adb170ea7848dab43cc432b1f50aa29e8f37e3f9fdac0c06a4a667201299`
- Service `verification.json`:
  `f1e20502448f27381329b2b94612ea901c72cc3771db26c83f715c14c0a8e35a`
- Final service log:
  `69208e44e730089339cd3d1ae45e414c5cb8c6e56b3de4b32af98c258658ab3f`
- Statement checks:
  `ba897956a121706b33f22571d5246bcc847a5a0ad497c2a3605733663564d043`
- Reference checks:
  `230f83afe0c86fd71f4d5fd7c7ffc1ed240b82faad6d1d7dfd5cfaa37d2a0f5c`
- Failed checks:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Verification-report memory:
  `aedaf731dc558ab0265f0fe15f63e9c7c39e091f19a1b3b42e7a302da8d0501b`
- Event memory:
  `4d31c290884da5a99565cc0fdc6420f81d723e192ef33c7a77f70c70df73f6db`
- Run metadata:
  `badb01c5368116abb1f8df77600f595a5c84821c797ebc04966af741923117f9`

The archived response and service `verification.json` are semantically
identical.  Their key-sorted compact JSON has SHA-256
`154ece11a07682a5d9bb3521dd4e6b7f1e9c5de92cdcba72e934dade0e57e1a7`.
The response schema has the three top-level keys `verification_report`,
`verdict`, and `repair_hints`; `verification_report` contains the summary and
empty `critical_errors` and `gaps` arrays.  Thus any helper display of
`checked_items: 0` would be a schema-summary artifact caused by the absent
top-level `checked_item_ids` field, not an absence of the 23 statement and 25
reference records persisted by the verifier.

## Provenance of the closure resubmission

The same materialized statement and proof first received a service-side PASS
in run `20260828T045515Z_db92555a72e1`, with 23 statement records, 25
reference records, no failed checks, no critical errors, and no gaps.  Its
client directory retained only the exact request and did not archive the
response and safe headers.  It is therefore corroborating provenance, not the
controlling production run.  The later `051601` run above resubmitted the same
six source files and is controlling because it closes both the service and
client HTTP evidence.

## Mathematical scope confirmed

The exact live bytes establish:

- the canonical-collar source localization and global-in-`U` exact preimage
  identity, including the common virtual-annulus expansion index and finite
  branch separation;
- the rigid-point zero-atom estimate and classification of positive closed
  bidegree-`(0,0)` CLD currents on connected rig-smooth curves;
- the reduced pure one-dimensional classification by normalized irreducible
  components and the stated continuous-psh Bedford--Taylor independence;
- invariance under nilreduction of analytic points, ordinary and `G`-form
  calculus, compact-test topologies, currents, admissible Borel products,
  positivity, closedness, and psh sheaves;
- the distinction between the multiplicity-weighted integration current on
  the nonreduced curve and the unweighted current of its reduction;
- classification of positive closed currents on the nonreduced curve; and
- equivalence of the multiplicity-weighted and unweighted component curvature
  identities, hence continuous-pair Bedford--Taylor independence for every
  classified positive closed current.

These conclusions are under the exact goodness, separatedness, strictness,
pure-dimensionality, boundarylessness, nontrivial-valuation, and rig-smooth
component-normalization hypotheses printed in the theorem.  This receipt does
not assert the literal discontinuous-psh predicate of CLD Definition 8.6.2, a
trivially valued field, a non-good or non-strict curve, a curve with boundary,
a component with non-rig-smooth normalization, or analytic dimension at least
two.  Nilpotents enter through generic cycle multiplicities; no nilpotence
exponent or transverse vanishing-order estimate is asserted.
