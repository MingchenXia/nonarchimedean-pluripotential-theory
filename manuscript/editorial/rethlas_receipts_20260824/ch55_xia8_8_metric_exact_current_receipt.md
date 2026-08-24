# Chapter 55 Xia 8.8 metric theorem: exact-current production receipt

Date: 24 August 2026.

## Exact objects

- Frozen live chapter:
  `manuscript/parts/part5/ch55_okounkov_dh.tex`
- Live-chapter bytes and SHA-256:
  64,938 bytes,
  `b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab`
- Shared Chapter 51 source SHA-256:
  `60e1165fad0cf2b05e5bb03602c485a18d49160b40d1fc4c2569e4ca383371dc`
- Exact target statement:
  `manuscript/editorial/rethlas_packets_20260824/ch55_xia8_8_metric_statement_exact.tex`
- Target-statement bytes and SHA-256:
  390 bytes,
  `57635bfa07f426eaa50998ba241506a6237a3127cf5113789f7d0cf43cf90a2c`
- Submitted source-aware proof context:
  `manuscript/editorial/rethlas_packets_20260824/ch55_xia8_8_metric_source_aware_proof_context_20260824.tex`
- Proof-context bytes and SHA-256:
  32,945 bytes,
  `1092b9c37729db232f5b0978a7d267e7666144177c6c79be65f9aea170b8cd1e`
- Persistent request object:
  `manuscript/editorial/rethlas_packets_20260824/ch55_xia8_8_metric_source_aware_request_20260824.json`
- Request bytes and SHA-256:
  36,016 bytes,
  `d70268798320646d4d9bed44508299346f9200109813cbf1d534dbb5d01ca541`

The exact components and their live-source intervals are recorded in
`ch55_xia8_8_exact_block_manifest_20260824.md`.  Every component comparison
returned zero.  Decoding the request fields reproduces the target and proof
files byte for byte.

## Production result

- Verification service: local production Rethlas
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Run ID: `20260824T054849Z_57635bfa07f4`
- Proof item: `pi_01a5edbb4e5e1a3a59ed8d9e`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Failed or blocked items: 0
- Critical errors: 0
- Gaps: 0
- Proof digest:
  `1092b9c37729db232f5b0978a7d267e7666144177c6c79be65f9aea170b8cd1e`
- Aggregate context digest:
  `2bc8afe0f8f9744676b9cbd7548e157501109aed8a1ebb8f77c638b8d8d39cee`
- Adaptive-context digest:
  `d532a9c541fc8baa4db178e13c503f0a50caa4bd3cd73efea0e4397015ef3798`
- Item-context digest:
  `58009e78f42ff330277c3f0670781871226594cb63574895808345eead6ddeb6`
- Source raw-response bytes and SHA-256:
  820 bytes,
  `3110a9b269c01f69a0843478025c56a65ba68f5180fdff1b176c333dd4d209fb`
- Archived response:
  `manuscript/editorial/rethlas_receipts_20260824/ch55_xia8_8_metric_source_aware_response_20260824.json`
- Archived-response bytes and SHA-256:
  821 bytes,
  `f00b56a9f506ddc3311314c780b934e66736eebc44f65cfe85fcfc86318b10ed`

The archive contains the complete 820-byte service response in order and
adds one terminal LF.  Its first 820 bytes therefore have the source-response
SHA-256 above.  The service reported one checked proof item and no failed or
blocked item; it requested neither a repair nor an expanded proof.

## Provenance and scope boundary

The submitted context contains the exact Chapter 51 and Chapter 55 premises,
the complete metric proof chain, and packet-only primary-source attestations.
The controlling XiaBook locators were checked against the persistent PDF;
the earlier wrong-locator response and the later correct verdict on the
wrong-locator snapshot remain diagnostics, not receipts for the live bytes.

This theorem reconstructs a proof supplied in an unpublished author
manuscript.  The receipt verifies the stated proof object; it makes no
publication, novelty, or priority claim.  The older
`xia_conjecture_8_8_repaired_receipt.md` and
`xia_conjecture_8_8_repaired_source_receipt.md` are corroborating proof-object
checks only and do not control this exact-current gate.

The authenticated metric statement assumes a connected smooth projective
complex variety, a big line bundle, positive multiplier-ideal volume in each
factor, and every surjective rank-`n` lexicographic valuation in the family
fixed by the chapter.  It asserts neither a zero-volume extension, a
transcendental-class extension, a singular-variety extension, nor attainment
of the supremum.  It does not use arXiv:1710.09731, directly or indirectly.
