# Manifest: Chapter 49 truncation-energy intake

**Snapshot date:** 2026-08-24 (Asia/Shanghai)  
**Submission status:** repaired current payload passed production Rethlas;
see `../rethlas_receipts_20260824/ch49_truncation_energy_receipt.md`  
**Target labels:** `lem:ch49-truncation-energy`,
`rem:ch49-truncation-sharp`

SHA-256 values identify the exact bytes on disk.

| File | Role | Bytes | SHA-256 |
|---|---|---:|---|
| `manuscript/parts/part4/ch49_linear_growth.tex` | live source snapshot | 202422 | `c6755ba48b4c8295b72f6e9e4c22697c9e66acb2621c9304930d601737ec440a` |
| `ch49_truncation_energy_statement_exact.tex` | exact complete lemma environment, live lines 968--992 | 783 | `87943e4ffca417bdd6fde859bc299177a18827a1754ceff8231de8624a3078f2` |
| `ch49_truncation_energy_proof_exact.tex` | exact adjacent complete proof environment, live lines 994--1099 | 4353 | `9c927a7d5c01d0f169825578cb0e9627cedee32c0fca575cd4b357e30086242b` |
| `ch49_truncation_energy_sharpness_exact.tex` | exact adjacent complete sharpness remark, live lines 1101--1219 | 4222 | `5289e0ab7a676d7e09e584d7a4bc5972a8ef9cb36c9a4f59c36da644dd59027b` |
| `ch49_truncation_energy_statement_proof_exact.tex` | exact contiguous lemma-plus-proof payload, live lines 968--1099 | 5137 | `aa9be74a09af5db3b9184f04cf9710c2abc9843867d5df5426310045390add25` |
| `ch49_truncation_energy_statement_proof_sharpness_exact.tex` | exact full payload, live lines 968--1219 | 9360 | `312ac46575cb6fba6a0858e4eff38ad78cd223a0560ca0faa731e6c5396c99a2` |
| `ch49_truncation_energy_target_statement.txt` | plain-English Rethlas target | 1592 | `0c95825dbb063f1f257298e2ba12fd03e41645eba09aa320646e18f5b3f378e7` |
| `rethlas_packet_ch49_truncation_energy_20260824.md` | verified intake/context packet with post-gate status | 8036 | `61ef7c36b33150340714cbd4360442f7d4749c2282fc66d3dc5f7b3398ca7821` |
| `ch49_truncation_energy_failed_gate_20260824.json` | failed predecessor diagnostic, terminal newline normalized | 4189 | `bc33245662ba208df0be731b6abc1c9301d6643f12f4ad090261d4d2ceb567ed` |

## Byte-identity checks

At preparation time, every exact TeX extract compared byte-for-byte equal to
its stated contiguous slice of the live chapter.  The two combined payloads
retain the original blank lines between adjacent environments.  No header,
annotation, macro expansion, or newline normalization was added.

## Intended Rethlas fields

- `statement`: `ch49_truncation_energy_target_statement.txt`
- `proof`: `ch49_truncation_energy_statement_proof_sharpness_exact.tex`
- optional human/context attachment:
  `rethlas_packet_ch49_truncation_energy_20260824.md`

The shorter lemma-plus-proof payload is available if the sharpness remark is
verified in a distinct run, but the requested full gate uses the full payload
with hash `312ac4...6c99a2`.

The production receipt controls this snapshot: it records the target and
full-proof hashes above and the unchanged live-chapter hash.  Run
`20260824T041218Z_0c95825dbb06`, item
`pi_8189ce12c89257c9acec4eef`, returned final verdict `correct`, with zero
critical errors and zero gaps.  The exact request object used by that run was
not retained; the target and proof files, response archive, run identity, and
digests are retained.  No request file is reconstructed after the fact.

## Extraction and mathematical questions

1. **Exact extraction:** none.  The lemma, adjacent proof, and adjacent
   sharpness remark have unambiguous environment boundaries and byte equality
   was confirmed.
2. **Failed predecessor:** the old full payload hash `188ecc...f7b9` was
   rejected only because exact dependencies and computations were not present.
   The production diagnostic is archived as
   `ch49_truncation_energy_failed_gate_20260824.json`.
3. **Mixed-energy repair:** energy monotonicity, translation, fixed-class
   regularization, decreasing-pairing continuity, normalized mixed duality,
   mass one, and the trivial central-fibre computation now occur inside the
   proof; the mixed-energy identity is derived from the PL telescope.
4. **Sharpness repair:** the weight sandwich, toric conjugate
   `f_psi^vee=1+m_1`, normalized simplex integral, point-blowup cubic, and
   conic deformation cubic are all displayed in the adjacent remark.
5. **Normalization risk:** any verifier must keep probability normalization
   and the convention `E_omega(0)=0`; an unnormalized reading changes the
   formula by `V`.
6. **Source firewall:** the permitted mixed-energy route is the Chapter 46 PL
   intersection/polarization identity plus monotone extension.  The excluded
   Deligne-pairing paper arXiv:1710.09731 is neither cited nor permitted.

The production receipt cited above controls the repaired hashes in this
manifest.  Its final verdict is `correct`, with zero critical errors and zero
gaps.

## Manifest-history boundary

The receipt historically recorded pre-submission manifest digest
`429a57cfba0a2f41e722cd308df76dba30c8c04dc71af963f8a7826ff9bd5dc3`.
That exact metadata snapshot was not retained in the repository and is not
the digest of this current manifest.  The current manifest is identified by
the enclosing checksum ledger; the historical digest must not be presented
as a current file hash.
