# Manifest: Chapter 69 toric numerical dimension intake

**Snapshot date:** 2026-08-24 (Asia/Shanghai)  
**Submission status:** exact-current source-aware packet passed production
Rethlas with final verdict `correct`, zero critical errors, and zero gaps;
the delegated Chapter 55 toric proof has its separate valid receipt  
**Live source:** `manuscript/parts/part6/ch69_verified_extensions.tex`  
**Target label:** `thm:verified-toric-dimension`

SHA-256 values identify the exact bytes on disk.  Line numbers are navigation
aids; hashes and byte identity control the snapshot.

| File | Role | Live lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| `manuscript/parts/part6/ch69_verified_extensions.tex` | complete live Chapter 69 source | 1--end | 37496 | `39e5caa017d1181696a3a3757848980b989809b2b30aac598ebf7a6032f9be14` |
| `ch69_verified_toric_dimension_setup_exact.tex` | exact section setup and Cao criterion | 485--536 | 1881 | `244bc7008b1bbf7a817ea7f063810303620de7fe28680eab6fa5d8bbf419f8f7` |
| `ch69_verified_toric_dimension_statement_exact.tex` | exact complete theorem environment | 538--544 | 224 | `d706dc98ccca14bb0fad879619de60e22f07c34a7333f5bbf54dc1d061df9700` |
| `ch69_verified_toric_dimension_proof_exact.tex` | exact adjacent complete proof environment | 546--620 | 3138 | `48d0403d0a78a9758e9cb3031e96b15caa0d1b51397677920294cd8a1333042b` |
| `ch69_verified_toric_dimension_statement_proof_exact.tex` | exact contiguous theorem-plus-proof payload | 538--620 | 3363 | `a26565adb1f61fe7f3cc5c7f046822411a2c1c09ed779622f375c044c6890f7e` |
| `ch69_verified_toric_dimension_section_packet_exact.tex` | exact contiguous setup, criterion, theorem, and proof; second composite component | 485--620 | 5245 | `1f3916a0924195133dc40b1c9804a46b3d8fad294303164d5a3cd60401668811` |
| `ch69_verified_toric_dimension_source_aware_composite_context_20260824.tex` | source-aware proof field: receipt-authenticated Ch55 Cao-attested context followed by complete Ch69 section packet | composite lines 10--264 and 268--403 | 17196 | `8aefa5096761f66d4b8f7bda26f0f5f037048e9832bdb03de7921e807aa5d618` |
| `ch69_verified_toric_dimension_target_statement.txt` | exact Rethlas statement field, byte-identical to the theorem environment | 538--544 | 224 | `d706dc98ccca14bb0fad879619de60e22f07c34a7333f5bbf54dc1d061df9700` |
| `ch69_verified_toric_dimension_source_aware_request_20260824.json` | persistent exact request assembled from the current target and composite; deadline `2026-08-25T05:45:00+00:00` | n/a | 18824 | `8a91bc8af4cf854edd9dd9958c8828b1cb16c3dec9166977e29f2c805d2e5379` |
| `rethlas_packet_ch69_verified_toric_dimension_20260824.md` | verified intake, authenticated dependency, and scope packet | n/a | 8164 | `3e6db1d33ee4d01d9e99055706daa9e460a6df3edb3dafdf54c36566bc5b22dd` |

## Byte-identity checks

All six exact extracts compared byte for byte with their stated contiguous
line slices of the live Chapter 69 source.  Every `cmp` returned exit status
zero.  The target text is an exact duplicate of the complete theorem
environment.  The combined files preserve the one blank line between the
statement and proof, and the section packet is one continuous source
interval rather than a stitched document.  No annotation, line number,
macro expansion, whitespace normalization, or explanatory header occurs in
an exact file.

The composite has explicit packet-comment boundaries.  Extracting its lines
10--264 gives a byte-identical copy of
`ch55_toric_zero_mass_proof_context_cao_attested_20260824.tex`, and extracting
lines 268--403 gives a byte-identical copy of
`ch69_verified_toric_dimension_section_packet_exact.tex`; both `cmp` checks
returned zero.  The first component's initial 10352-byte prefix is itself
byte-identical to `ch55_toric_zero_mass_section_packet_exact.tex`.  The second
component ends with the adjacent proof of the target theorem, after which
there is only an `END` comment marker, so the Chapter 69 target is the final
mathematical proof item.

Decoding the persistent request with `jq -j` reproduces the target statement
and source-aware composite byte for byte; both `cmp` checks returned zero.
The decoded field hashes are respectively `d706dc98...9700` and
`8aefa509...5d618`, and the request contains no field beyond `statement`,
`proof`, and `verification_deadline_utc`.

## Submitted Rethlas fields

- `statement`: exact bytes of
  `ch69_verified_toric_dimension_target_statement.txt`;
- `proof`: exact bytes of
  `ch69_verified_toric_dimension_source_aware_composite_context_20260824.tex`;
- optional human/context attachment:
  `rethlas_packet_ch69_verified_toric_dimension_20260824.md`.

The persistent request containing exactly those two fields is
`ch69_verified_toric_dimension_source_aware_request_20260824.json`; its
verification deadline is `2026-08-25T05:45:00+00:00`.

The adjacent-proof and theorem-plus-proof extracts are retained for
independent boundary checks.  The controlling Chapter 69 receipt records the
target hash `d706dc...9700`, composite proof hash `8aefa5...5d618`, and frozen
live-chapter hash `39e5ca...be14`.  Run
`20260824T070302Z_d706dc98ccca`, item
`pi_bbf8518d7f87e9372b79f4ff`, returned final verdict `correct`, with zero
critical errors and zero gaps.  Its receipt is
`../rethlas_receipts_20260824/ch69_verified_toric_dimension_exact_current_receipt.md`.
The Chapter 55 receipt digest was frozen in the composite header before
submission; no placeholder remains.

## Delegated Chapter 55 proof object

Chapter 69 explicitly delegates the local character calculation to
`thm:ok-toric-zero-mass`.  The current exact dependency is identified by:

- Chapter 55 live hash
  `b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab`;
- adjacent proof hash
  `69df8ceb670f2f3db57f97fece992373849bff9057b2e04d9c4780a922434b03`;
- full contiguous section-packet hash
  `e4a77f88ab81bbcf403ef3b740af409e53a5454bed95ecf0321f42fd1a25bb58`;
- complete Cao-attested proof-context hash
  `f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`;
- Chapter 55 valid-receipt manifest hash (metadata only)
  `5b15b44725133bd0d113a8dc636e135bba15a1978c384f2980fc8ac9d6ab6d34`.

Both Chapter 55 exact files compare byte for byte with their current live
source slices.  Production run
`20260824T052605Z_703e3b501202` returned `final/correct` with zero
critical errors and zero gaps for the exact Chapter 55 target and submitted
Cao-attested proof context.  The intake and composite record its authenticated
proof digest
`f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`.
The controlling receipt is
`../rethlas_receipts_20260824/ch55_toric_zero_mass_cao_attested_receipt.md`.
The invalid locator diagnostic from the earlier run
`20260824T045229Z_703e3b501202` remains diagnostic-only and is not used.

## Mathematical and scope audit

The exact section packet carries the full integral/rational toric setup and
Cao's Proposition 4.4 criterion.  The delegated calculation supplies the
actual normalized section-count limit
`S_A(epsilon)=vol_n(K+epsilon Q)`, including the strict shifted chart
conditions, gluing, lattice normalization, and absence of an `n!` factor.
The adjacent Chapter 69 proof then establishes the two-sided estimate
`vol_n(K+epsilon Q) asymp epsilon^(n-dim K)` and reads its exponent in Cao's
criterion.  It does not extend to irrational real classes, identify a
zero-volume Newton body with an unsupported positive-volume construction,
or assert a finite-level unshifted lattice-count identity.

No Chapter 69 source was modified during preparation or after verification.
All exact-source and composite-component comparisons passed immediately
before and after the production submission.
