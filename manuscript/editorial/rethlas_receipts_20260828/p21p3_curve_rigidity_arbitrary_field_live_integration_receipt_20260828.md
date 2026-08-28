# P21.3 arbitrary-field curve classification: live integration receipt

**Date:** 28 August 2026

**Controlling service run:** `20260828T051601Z_db92555a72e1`

**Model:** `gpt-5.6-sol`

**Reasoning effort:** `xhigh`

**HTTP status:** `200`

**Verdict:** `correct`

**Critical errors:** `0`

**Gaps:** `0`

The run above is the controlling exact-live nonreduced gate because both the
service evidence and the complete client HTTP evidence are archived.  The
earlier run `20260828T045515Z_db92555a72e1` passed on the same materialized
statement and proof and persisted 23 statement checks and 25 source checks,
with no failure, critical error, or gap.  Its client directory retained only
the exact request, however, so it is service-only corroboration and does not
control this integration receipt.

## Exact-byte identity

Chapter 16 inputs the following six verified mathematical files directly,
without mathematical-text or label transformation:

| Live file | SHA-256 |
|---|---|
| `editorial/rethlas_packets_20260828/p21p3_curve_rigidity_virtual_annulus_bridge_statement_live_20260828.tex` | `f3202ef13495aad790ee2b1ff057a89b34e76eff15761c33c88e7b809c3e1033` |
| `editorial/rethlas_packets_20260828/p21p3_curve_rigidity_virtual_annulus_bridge_proof_live_20260828.tex` | `ff8225ed6206f97e628504ab5b255c58a1a0de4fda13962e1ab09092fe2be7d5` |
| `editorial/rethlas_packets_20260828/p21p3_curve_rigidity_arbitrary_field_reduced_statement_live_20260828.tex` | `c9f27245f5608b772385167c84bfe9e836fc9f4b164477a578b6c26712e35b21` |
| `editorial/rethlas_packets_20260828/p21p3_curve_rigidity_arbitrary_field_reduced_proof_live_20260828.tex` | `01ab07fdacedfe95e1d764656a071a88395f5d0766115fd0a67164e3162410af` |
| `editorial/rethlas_packets_20260828/p21p3_curve_rigidity_nonreduced_arbitrary_field_statement_live_20260828.tex` | `e7b9889f6c063d9952d61c0472290183aac07b58c8d0569cfebc5e9ea73f1a9c` |
| `editorial/rethlas_packets_20260828/p21p3_curve_rigidity_nonreduced_arbitrary_field_proof_live_20260828.tex` | `25fe49a46b1c5cd62b0d1a5024095b47cdd49c66f594d1d86eec4f9f270c83ec` |

The submission helper joined the three statement files and, separately, the
three proof files with exactly one additional newline at each boundary.  The
materialized statement and proof SHA-256 digests are
`db92555a72e145591f922b3ffc623148dcaca7d252ea220d694203b04d164c49`
and
`b13829d962614f35af3f3725eb04be1d6f1b6b78490cb13d65e4ed43a05de779`.
Extracting `.statement` and `.proof` from the archived request without adding
bytes reproduces these two digests exactly.

The controlling request, response, and safe headers have SHA-256 digests
`d0cc30cbd8110de827077054d6320900865fff3d06657d9c659e412cadb79f64`,
`e2e7d8943b8a4f5bbd677065299bda3ebae0d22be10a71f2962ae38c40830f3f`,
and
`0e23adb170ea7848dab43cc432b1f50aa29e8f37e3f9fdac0c06a4a667201299`.
The service `verification.json` and final service log have SHA-256 digests
`f1e20502448f27381329b2b94612ea901c72cc3771db26c83f715c14c0a8e35a`
and
`69208e44e730089339cd3d1ae45e414c5cb8c6e56b3de4b32af98c258658ab3f`.
The controlling exact-live Rethlas receipt is
`editorial/rethlas_packets_20260828/p21p3_curve_rigidity_nonreduced_arbitrary_field_live_rethlas_receipt_20260828.md`,
SHA-256
`193e4e63a6f6db4c747189ded171334ccc664f7474cd048fe7f123054f6f1cb0`.

The exact-live reduced gate is independently archived as run
`20260828T042906Z_f2a1c1b9f2a3`: 17 statement records, 19 primary-source
records, zero failed checks, zero critical errors, and zero gaps.  The
independent nonreduced combined gate is run
`20260828T044008Z_dfdaa04a1cea`: 24 statement records, 25 source records,
zero failed checks, zero critical errors, and zero gaps.  All controlling
gates used `gpt-5.6-sol` at `xhigh` and returned final `correct`.

## Mathematical and source audits

The exact verification chain separately checked legal analytic-moment
localization, cofinal virtual-annular collars, exact source-ray separation,
the common expansion index, arbitrary-degree residual closed points,
residual-divisor balancing, the rigid-point zero-atom estimate, finite
normalization pushforward, and the nilreduction calculus.  It also checked
the fundamental-cycle multiplicities, classification of positive closed
bidegree-\((0,0)\) currents, and the equivalence of multiplicity-weighted and
reduced curvature equalities for continuous psh pairs.

The live integration keeps the six exact mathematical files as separate
direct inputs, in dependency order.  A clean standalone Chapter 16 package
build and the final whole-book build close all local labels, equations,
citations, and transitions.  The open-problem ledger, provenance appendix,
revision ledger, theorem-provenance ledger, and chapter-status ledger all use
the same scope: algebraic closedness and nonreducedness are removed from the
one-dimensional residual list, while the discontinuous, trivially valued,
non-rig-smooth, and higher-dimensional cases remain.

## Exact scope and conclusion

Let \(K\) be any complete nontrivially valued non-Archimedean field.  Let
\(X\) be a good separated strict pure one-dimensional boundaryless
\(K\)-analytic space, not necessarily reduced, and suppose that the
normalization of every irreducible component of \(X_{\mathrm{red}}\) is
rig-smooth.  The integrated results prove:

- the canonical-collar source-localization and exact source-preimage
  identities required for the arbitrary-field flux comparison;
- unique locally finite classification of every positive
  \(\mathrm d'\)- and \(\mathrm d''\)-closed CLD current of bidegree \((0,0)\)
  as a nonnegative combination of normalized reduced-component currents;
- invariance under nilreduction of ordinary and \(G\)-form calculus,
  compact-test and weak current topologies, positivity, closedness, the
  stated products, and psh sheaves;
- the multiplicity-sensitive formula for the nonreduced integration current;
  and
- equivalence of the multiplicity-weighted and reduced curvature identities,
  hence Bedford--Taylor independence for continuous psh pairs and every
  classified positive closed current.

The theorem does not assert the literal discontinuous-psh predicate of CLD
Definition 8.6.2.  It does not treat a trivially valued field, a non-good or
non-strict curve, a curve with boundary, a component normalization outside
the rig-smooth hypothesis, or analytic dimension at least two.  Nilpotents
enter only through generic cycle multiplicities; no transverse
nilpotence-order estimate is asserted.  P21.3 therefore remains one T2
residual atom in precisely this complementary scope.

## Whole-book gate

- Final PDF: 3,207 pages, 15,433,695 bytes, SHA-256
  `e2e68023a6b9e7a5e4bd671504d8226f6c1a377c9749bdf0c3745d2932d7c028`.
- Final log SHA-256:
  `d91cbee2b685c928086c8b9f5d9156e4b4f7749eadacc6ff9d94200042a3a983`.
- No TeX error, undefined control sequence, fatal or emergency stop,
  undefined reference or citation, multiply defined label, duplicate
  destination, rerun request, BibTeX warning, index warning, or overfull box.
  There are 991 underfull-box notices from the monograph layout and long
  tables.  The only `Warning:` line is the harmless historical class-path
  mismatch: the requested local file `style/svmono` declares itself as
  `svmono`.
- Exact source closure: 127 files; manifest SHA-256
  `eecc05a93d3cdccf82b6b2411662ac16ce34221f3ced4829613b88119782514b`;
  every entry verifies.
- Static audit: 9,913 labels and no duplicate; 30,768 references and no
  dangling target; 208 cited keys and no missing key.
- Structural frontier: 16 formal problem environments and 55 active atoms,
  with tier counts 0/7/14/17/17.
- Author blank; acknowledgements empty; no exercises; no optional
  conventional theorem-like names.
- Rendered inspection passed on physical PDF pages 737--765, 3035--3037,
  and 3182--3184.  These pages cover the complete Chapter 16 theorem and
  proofs, examples and scope firewalls, the Chapter 72 residual statement,
  the Appendix L provenance gate, and all neighbouring transitions.

This receipt controls exact-byte integration and scope.  It makes no novelty
or priority claim.
