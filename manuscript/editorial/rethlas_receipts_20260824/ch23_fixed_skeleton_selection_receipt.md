# Chapter 23 fixed-skeleton selection: production receipt

Date: 24 August 2026.

## Exact objects

- Live chapter:
  `manuscript/parts/part3/ch23_bfj_envelopes.tex`
- Production-submission live-chapter bytes and SHA-256:
  165,480 bytes,
  `72da809fadf0685c8e8bb05559e3c0fd7f8eb3d94a75f1ee8607b7289518f123`
- Current live-chapter bytes and SHA-256 after the post-receipt provenance
  and line-breaking edits below the verified interval:
  165,454 bytes,
  `acaf22a242ee48952d8d4339c9ebd7bd6fafdf5ac118dec66aaf1d67eaaa2bfd`
- Target statement:
  `manuscript/editorial/rethlas_packets_20260824/ch23_fixed_skeleton_selection_target_statement.txt`
- Target-statement SHA-256:
  `25024c43d265636b667320ddb4090b3882320790f029bbe8f3103808dd3595e8`
- Exact statement-plus-proof payload:
  `manuscript/editorial/rethlas_packets_20260824/ch23_fixed_skeleton_selection_statement_proof_exact.tex`
- Proof-payload SHA-256:
  `d91003dd920d193192b4dcd8a064ac46d5535cb6befc53bd08670db8451d7786`
- Historical pre-submission manifest SHA-256:
  `20bfb70d349c56d11c6d35df6bf8a8a538858a92a25bb579192a9a7ff25dd555`
- Current manifest:
  `manuscript/editorial/rethlas_packets_20260824/ch23_fixed_skeleton_selection_manifest_20260824.md`
- Current-manifest SHA-256:
  `a9e46cb2d59f9bb7f9fea7737d5c5757ae6d74b66d607d94b53a679e1d6f9dc6`
- Archived exact request:
  `manuscript/editorial/rethlas_packets_20260824/ch23_fixed_skeleton_selection_request_20260824.json`
- Request bytes and SHA-256:
  8,303 bytes,
  `7eac315d533fff804044fd62cdb8dcb0343554262d33ee8dea96d207a2eb431e`

The historical pre-submission manifest bytes were not retained and the old
digest is not the digest of the current manifest.  It is recorded only to
interpret the production metadata and must not be presented as a current
file hash.

The payload was byte-identical to the complete proposition and its adjacent
proof in the production-submission chapter snapshot.  The later edits change
only the provenance paragraph below the verified interval, including the
typographical use of breakable run identifiers.  After those edits,
the exact statement, proof, and combined statement-plus-proof files were all
compared again with the current live slices; every `cmp` returned zero.  The
verified combined proof digest therefore remains
`d91003dd920d193192b4dcd8a064ac46d5535cb6befc53bd08670db8451d7786`.

## Production result

- Verification service: local production Rethlas
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Run directory:
  `/Users/mingchen/.codex/visualizations/2026/08/20/01a01d3c-132d-7ca3-b98a-59682fe837e7/Rethlas_popovici_local/agents/verification/results/20260824T044830Z_25024c43d265`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Failed or blocked items: 0
- Critical errors: 0
- Gaps: 0
- Proof item: `pi_4cc2365c9c77af25df553e8e`
- Aggregate context digest:
  `4cafc54fb63bc0f0de67c8a5d155ae501b3818cc1f4fa35264a7e713f09b7eb4`
- Adaptive-context digest:
  `3a1b6bf7e1ec657e3988a29f64627e51305d1a5b065b8117bc30f77402ae39b4`
- Item-context digest:
  `59d4723062ca341faf825cc994da77fdfb9751ab4a25e66e648e2eacd1a6f33e`
- Raw-response SHA-256:
  `837f2214b0a224f7b28114929855aabd1c5972f8a0c835282c5589de4ad7307c`
- Archived raw response:
  `manuscript/editorial/rethlas_receipts_20260824/ch23_fixed_skeleton_selection_response.json`
- Archived-response bytes and SHA-256:
  820 bytes,
  `837f2214b0a224f7b28114929855aabd1c5972f8a0c835282c5589de4ad7307c`

The service summary was: “Checked all 1 proof items; 0 item(s) failed or
were blocked.” No repair hint or expanded proof was requested.

## Repair and scope

The first exact submission was rejected for missing dependency context, not
for a counterexample.  The controlling proof now states the fixed-skeleton
Lipschitz input, constructs and topologically verifies the compatible path
metric, derives the global modulus, records finiteness on the skeleton, and
proves the sequential compactness argument usually called Dini's theorem.
It also enumerates the double index set itself, so a finite image of selected
functions creates no gap.

This is a book-local selection result on one fixed determining dual complex.
The sequence depends on that skeleton; neither a global sequential
cofinality result nor a sequence working on all skeleta is claimed.  The
proof uses the published BFJ skeletal inputs but is not presented as a
published BFJ theorem.  It does not use arXiv:1710.09731, directly or
indirectly.
