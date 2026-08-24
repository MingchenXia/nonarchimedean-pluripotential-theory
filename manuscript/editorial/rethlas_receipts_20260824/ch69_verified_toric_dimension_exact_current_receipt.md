# Chapter 69 toric numerical dimension: exact-current production receipt

Date: 24 August 2026.

## Exact objects

- Frozen live chapter:
  `manuscript/parts/part6/ch69_verified_extensions.tex`
- Live-chapter bytes and SHA-256:
  37,496 bytes,
  `39e5caa017d1181696a3a3757848980b989809b2b30aac598ebf7a6032f9be14`
- Exact target statement:
  `manuscript/editorial/rethlas_packets_20260824/ch69_verified_toric_dimension_target_statement.txt`
- Target-statement bytes and SHA-256:
  224 bytes,
  `d706dc98ccca14bb0fad879619de60e22f07c34a7333f5bbf54dc1d061df9700`
- Submitted source-aware composite context:
  `manuscript/editorial/rethlas_packets_20260824/ch69_verified_toric_dimension_source_aware_composite_context_20260824.tex`
- Composite-context bytes and SHA-256:
  17,196 bytes,
  `8aefa5096761f66d4b8f7bda26f0f5f037048e9832bdb03de7921e807aa5d618`
- Persistent request object:
  `manuscript/editorial/rethlas_packets_20260824/ch69_verified_toric_dimension_source_aware_request_20260824.json`
- Request bytes and SHA-256:
  18,824 bytes,
  `8a91bc8af4cf854edd9dd9958c8828b1cb16c3dec9166977e29f2c805d2e5379`

All six Chapter 69 extracts compare byte for byte with the frozen live source.
The composite's first component is the receipt-authenticated Chapter 55
Cao-attested proof context, SHA-256
`f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`;
its second component is the exact contiguous Chapter 69 section packet,
SHA-256
`1f3916a0924195133dc40b1c9804a46b3d8fad294303164d5a3cd60401668811`.
Both composite-component comparisons and both decoded-request comparisons
returned zero.

## Production result

- Verification service: local production Rethlas
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Run ID: `20260824T070302Z_d706dc98ccca`
- Proof item: `pi_bbf8518d7f87e9372b79f4ff`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Failed or blocked items: 0
- Critical errors: 0
- Gaps: 0
- Proof digest:
  `8aefa5096761f66d4b8f7bda26f0f5f037048e9832bdb03de7921e807aa5d618`
- Aggregate context digest:
  `86de424eb9db2000fcd9b22d2f3234d76de26ea1fd4d6960a80c08bd3b8adcad`
- Adaptive-context digest:
  `a50385495d943e42185ba965667813d811f89e1332c8c482eeb8ddd9c967d6c8`
- Item-context digest:
  `ae11a60d3cc7f94dca258477f701377832f3d4831dfc4ee3fe6e259313136428`
- Elapsed verifier time: 909.819 seconds
- Billed verifier tokens: 85
- Source raw-response bytes and SHA-256:
  820 bytes,
  `41c775d1fc7e9820f46d25ce2436ecd2180cf33847ac15318596adcdbff086ef`
- Archived response:
  `manuscript/editorial/rethlas_receipts_20260824/ch69_verified_toric_dimension_source_aware_response_20260824.json`
- Archived-response bytes and SHA-256:
  821 bytes,
  `14cbbb12414395c9bda888cf2135f7400e718af1620665a9f9fa8b415d718cda`

The archive contains the complete 820-byte service response in order and
adds one terminal LF.  Its first 820 bytes therefore have the source-response
SHA-256 above.  The service reported one checked proof item and no failed or
blocked item; it requested neither a repair nor an expanded proof.

## Dependency, provenance, and scope boundary

The exact Chapter 69 proof delegates the local character calculation to the
Chapter 55 theorem whose controlling receipt is
`ch55_toric_zero_mass_cao_attested_receipt.md`.  The composite embeds that
receipt-authenticated proof context in full and then gives the exact Chapter
69 setup, target, and adjacent proof.  The target theorem is the final
mathematical proof item.  The valid Cao locator is Proposition 4.4 in the
controlled primary PDF; the earlier model response substituting nonexistent
Proposition 4.3 is diagnostic only.

This is a book synthesis: the verified Chapter 55 character calculation is
combined with the elementary convex tube estimate recorded in Chapter 69.
The receipt makes no claim that this precise theorem is a published result,
and it makes no novelty or priority claim.

The authenticated theorem covers smooth projective toric varieties and
integral or rational big toric classes.  It neither extends the conclusion to
irrational real classes nor identifies a zero-volume Newton body with an
unsupported positive-volume partial-body construction.  It does not use
arXiv:1710.09731, directly or indirectly.
