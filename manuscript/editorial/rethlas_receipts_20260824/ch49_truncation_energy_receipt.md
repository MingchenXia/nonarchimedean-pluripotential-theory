# Chapter 49 truncation-energy package: production receipt

Date: 24 August 2026.

## Exact objects

- Live chapter:
  `manuscript/parts/part4/ch49_linear_growth.tex`
- Live-chapter SHA-256:
  `c6755ba48b4c8295b72f6e9e4c22697c9e66acb2621c9304930d601737ec440a`
- Target statement:
  `manuscript/editorial/rethlas_packets_20260824/ch49_truncation_energy_target_statement.txt`
- Target-statement SHA-256:
  `0c95825dbb063f1f257298e2ba12fd03e41645eba09aa320646e18f5b3f378e7`
- Exact statement, proof, and sharpness payload:
  `manuscript/editorial/rethlas_packets_20260824/ch49_truncation_energy_statement_proof_sharpness_exact.tex`
- Proof-payload SHA-256:
  `312ac46575cb6fba6a0858e4eff38ad78cd223a0560ca0faa731e6c5396c99a2`
- Historical pre-submission manifest SHA-256:
  `429a57cfba0a2f41e722cd308df76dba30c8c04dc71af963f8a7826ff9bd5dc3`
- Current manifest:
  `manuscript/editorial/rethlas_packets_20260824/ch49_truncation_energy_manifest_20260824.md`
- Current-manifest SHA-256:
  `a534502ccdfa6dbe80abbf8645c13bdbaf9c5d1d1762b4c19c4b86791705ed8e`

The payload is byte-identical to the contiguous lemma, proof, and adjacent
sharpness computation in the live chapter snapshot recorded above.

The historical pre-submission manifest bytes were not retained and the old
digest is not the digest of the current manifest.  It is recorded only to
interpret the production metadata and must not be presented as a current
file hash.  The exact request object for this run was likewise not retained;
it is not reconstructed after the fact.  The exact target, proof payload,
run identity, response, and verifier digests are retained.

## Production result

- Verification service: local production Rethlas
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Run directory:
  `/Users/mingchen/.codex/visualizations/2026/08/20/01a01d3c-132d-7ca3-b98a-59682fe837e7/Rethlas_popovici_local/agents/verification/results/20260824T041218Z_0c95825dbb06`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Failed or blocked items: 0
- Critical errors: 0
- Gaps: 0
- Proof item: `pi_8189ce12c89257c9acec4eef`
- Aggregate context digest:
  `08089b376c9befa730e43865a762c975eb803788d2372eef7fb1a9af8750d58a`
- Adaptive-context digest:
  `b36ed175f123fe6393f151a398fb7d985b62a396c70a966a70d56f6ee0bde862`
- Item-context digest:
  `31e901c089612559dd6e6d7d7734b0c70430019c20baee55498a237ee5f1aca5`
- Raw-response SHA-256:
  `66fda2c97601fb25e08f805d4569475727e2ab2517067d282a8800d3b2166910`
- Archived raw response:
  `manuscript/editorial/rethlas_receipts_20260824/ch49_truncation_energy_response.json`
- Archived-response bytes and SHA-256:
  820 bytes,
  `66fda2c97601fb25e08f805d4569475727e2ab2517067d282a8800d3b2166910`

The service summary was: “Checked all 1 proof items; 0 item(s) failed or
were blocked.” No repair hint or expanded proof was requested.

## Diagnostic history and scope

An earlier, shorter payload was rejected because it omitted the precise
mixed-energy inputs, probability normalization, and the sharpness
computations.  That failed response remains archived as a diagnostic and is
not a receipt.  The controlling payload above includes the energy telescope,
monotone passage, mixed-measure normalization, trivial central-fibre
calculation, toric simplex computation, and both surface sharpness examples.

The proof route uses the Chapter 46 PL intersection and polarization
identity.  It does not cite or use the excluded Deligne-pairing paper
arXiv:1710.09731.

This is a book-local sharp consequence of the imported Boucksom--Jonsson
normalized energy and mixed Monge--Ampere package, not a verbatim published
theorem.  Its verified scope is an ample positive-volume class, a bounded psh
potential with finite center, and probability-normalized Monge--Ampere
measures.  It makes no zero-volume or unbounded finite-energy assertion.
