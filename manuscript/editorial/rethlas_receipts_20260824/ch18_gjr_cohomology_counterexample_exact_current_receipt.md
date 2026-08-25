# Chapter 18 GJR cohomology counterexample: exact-current production receipt

Date: 24 August 2026.

## Exact objects

- Frozen live chapter:
  `manuscript/parts/part2/ch18_delta_forms.tex`
- Live-chapter bytes and SHA-256:
  176,345 bytes,
  `8e1ca749f52d628f8a8681ff7eba03496fdcab75d8371abbb34dc919d20601cf`
- Exact target statement:
  `manuscript/editorial/rethlas_packets_20260824/ch18_gjr_cohomology_counterexample_target_statement_exact.tex`
- Target-statement bytes and SHA-256:
  699 bytes,
  `fcddc3abc33d3d10de1f5e84b14a892e9ac193a48befaaa51a8104c2ac860e58`
- Exact live proof component bytes and SHA-256:
  1,584 bytes,
  `1abff3f61644a469b6567305ecfdcfb61c729232f20f51c75839b190e45f951c`
- Submitted source-aware composite context:
  `manuscript/editorial/rethlas_packets_20260824/ch18_gjr_cohomology_counterexample_source_aware_composite_context_20260824.tex`
- Composite-context bytes and SHA-256:
  3,216 bytes,
  `99d7583f90ebf7dcb56a40dcc04463ffcb0c04ee4c1c711e0acafacdc85dbe2c`
- Persistent request object:
  `manuscript/editorial/rethlas_packets_20260824/ch18_gjr_cohomology_counterexample_source_aware_request_20260824.json`
- Request bytes and SHA-256:
  4,170 bytes,
  `c97e9ad9c973f855bc8ce73b6521a77c0f13be2bf56866aab5cdc2ec68ca35b0`

The target statement and the first 1,584 bytes of the composite context
compare byte for byte with the current live proposition and its adjacent
proof.  The remaining composite component is packet-only primary-source
attestation.  Decoding the persistent request reproduces the exact statement
and composite strings submitted to the service; both comparisons returned
zero.

## Production result

- Verification service: isolated local production Rethlas
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Run ID: `20260824T123617Z_fcddc3abc33d`
- Proof item: `pi_a039b322c111642b44684f4e`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Failed or blocked items: 0
- Critical errors: 0
- Gaps: 0
- Proof digest:
  `99d7583f90ebf7dcb56a40dcc04463ffcb0c04ee4c1c711e0acafacdc85dbe2c`
- Aggregate context digest:
  `d43cb8979d9aa09bd4f4a4a260a08b6cb47cfb921e3cb3795a7bc45ed7e2baa5`
- Adaptive-context digest:
  `c9409200a9edfa317cd89b865c7907f72b58b116c0ce1f903689fe0f6c994a5a`
- Item-context digest:
  `857f6fd983397b7af48943ecef81b41175baf8ff56a18733aa5a35d186672409`
- Elapsed verifier time: 473.530 seconds
- Billed verifier tokens: 59
- Archived response:
  `manuscript/editorial/rethlas_receipts_20260824/ch18_gjr_cohomology_counterexample_source_aware_response_20260824.json`
- Archived-response bytes and SHA-256:
  964 bytes,
  `40e8f945eef559978c05bdbf561d2a1599d0caeaef0f36b0f9791bb9d98d4138`

The archived response is byte-identical to the aggregate service artifact.
The service requested neither a repair nor an expanded proof.

## Primary-source firewall

The controlling source is W. Gubler, P. Jell, and J. Rabinoff, *Forms on
Berkovich spaces based on harmonic tropicalizations*, Bull. Soc. Math.
France **154** (2026), 135--238, doi:10.24033/bsmf.2919.  The official
published PDF was inspected separately.  On printed page 142 (physical PDF
page 10), Theorem 1.14 gives dimension one for the weakly smooth
`H^{p,q}` of a smooth projective curve when `p+q` is 0 or 2.  Across printed
pages 142--143 (physical PDF pages 10--11), Section 1.15 states the canonical
injection from the invariant exterior algebra for every abelian variety and
asks, without a reduction-type restriction, whether it is an isomorphism.
Section 16 supplies the Raynaud-uniformization context; the good-reduction
specialization is also immediate here from the displayed constant abelian
scheme.

The locally archived arXiv v3 PDF agrees in the load-bearing passages.  It
has 1,092,577 bytes and SHA-256
`572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42`.
The paragraph following Theorem 1.14 delegates its proof to a reference
listed as in preparation.  The book therefore imports the published theorem
statement; neither this receipt nor the proposition claims an independent
proof of the curve-cohomology theorem itself.

## Provenance and scope boundary

The result is a direct counterexample assembled from the published GJR
injection, the published curve-cohomology dimension formula, and the standard
good-reduction extreme of Raynaud uniformization.  The book makes no novelty
or priority claim.

The counterexample answers only the literal unrestricted question: a
good-reduction elliptic curve has toric rank zero, hence zero source in
bidegree `(1,1)`, while the target has dimension one.  It does not answer the
separately sharpened question for totally degenerate abelian varieties.
