# Chapter 55 toric zero-mass package: production receipt

Date: 24 August 2026.

## Exact objects

- Live chapter:
  `manuscript/parts/part5/ch55_okounkov_dh.tex`
- Live-chapter bytes and SHA-256:
  64,938 bytes,
  `b2134d6b59f7687f8f5f296023a7d80703122210909032856b965f12f61619ab`
- Exact target statement:
  `manuscript/editorial/rethlas_packets_20260824/ch55_toric_zero_mass_target_statement.txt`
- Target-statement bytes and SHA-256:
  558 bytes,
  `703e3b50120292333f6b00a3e18e887a2a67f2aa7d5dbaf5197c3f4e1a3296aa`
- Exact contiguous setup, statement, proof, and scope packet:
  `manuscript/editorial/rethlas_packets_20260824/ch55_toric_zero_mass_section_packet_exact.tex`
- Section-packet bytes and SHA-256:
  10,352 bytes,
  `e4a77f88ab81bbcf403ef3b740af409e53a5454bed95ecf0321f42fd1a25bb58`
- Submitted Cao-attested proof context:
  `manuscript/editorial/rethlas_packets_20260824/ch55_toric_zero_mass_proof_context_cao_attested_20260824.tex`
- Submitted proof-context bytes and SHA-256:
  11,260 bytes,
  `f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`

The first 10,352 bytes of the submitted proof context are byte-identical to
the contiguous live Chapter 55 section packet.  The remaining packet-only
attestation records the persistent Cao PDF and the verified Proposition 4.4
locator.  All exact extracts still compare byte for byte with the current
live chapter.  The later Schneider locator edits occur before these intervals
and therefore changed the live-chapter digest but none of the submitted
statement or proof bytes.

## Production result

- Verification service: local production Rethlas
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Run ID: `20260824T052605Z_703e3b501202`
- Run directory:
  `/Users/mingchen/.codex/visualizations/2026/08/20/01a01d3c-132d-7ca3-b98a-59682fe837e7/Rethlas_popovici_local/agents/verification/results/20260824T052605Z_703e3b501202`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Failed or blocked items: 0
- Critical errors: 0
- Gaps: 0
- Proof item: `pi_1f43447774c9ced4048c2efa`
- Request SHA-256:
  `a4be04e568428d2de5ce8c657f27bc5a595cb8aa89e8d0c157386c26c9a6e649`
- Proof digest:
  `f978d2ee49a3f90d29f010cdc750fe0c28370f9b4b63a9f96dce5b297423896d`
- Aggregate context digest:
  `a7b2810ae9892efcd25ab816b6ca81b1ef2d260705055da11156f3b430d98535`
- Adaptive-context digest:
  `c16ee814024761038c55fc1416f8804a31290b5fad272704962fc2771a74ea8b`
- Item-context digest:
  `477d75874ccdbdfdda9f02a0617f62e91c4b816a096393c0ce25d50b0c2d01a5`
- Source raw-response bytes and SHA-256:
  820 bytes,
  `2691e5802961cd88ba400f9ba701a670c0e036b1ecb1521b1871c0f3e35b2a66`
- Archived response:
  `manuscript/editorial/rethlas_receipts_20260824/ch55_toric_zero_mass_cao_attested_response.json`
- Archived-response bytes and SHA-256:
  821 bytes,
  `6ae6fdf288771b75f49d2a2745863394faab260fc9057458545627bf9f7984ac`

The archive contains the complete 820-byte service response in order and
adds one terminal LF.  Its first 820 bytes therefore have the source-response
SHA-256 above.

The service summary was: “Checked all 1 proof items; 0 item(s) failed or
were blocked.”  No repair hint or expanded proof was requested.

## Primary-source and diagnostic boundary

The controlling source is
`tmp/pdfs/Cao14_arxiv1210.5692_primary.pdf`, 309,281 bytes, SHA-256
`17717664b0ae2b154e76e2ecb68c9f63f09dc74be6f25bac7f04b7ee0103b0d6`.
Physical page 19 contains Proposition 4.4 and its ordinary-versus-
upper-regularized multiplier-ideal comparison; physical page 17 contains
Lemma 4.3, and the paper has no Proposition 4.3.

The earlier run `20260824T045229Z_703e3b501202` is retained only as a
diagnostic because its sole objection replaced the correct Proposition 4.4
locator by nonexistent Proposition 4.3.  The present source-attested run is
the controlling valid receipt for the exact proof bytes identified above.
No claim beyond the integral/rational toric framework recorded in the packet
is authenticated by this receipt.
