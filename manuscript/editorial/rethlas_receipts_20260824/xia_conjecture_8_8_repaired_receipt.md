# Xia Conjecture 8.8: repaired-proof production receipt

Date: 24 August 2026.

## Exact objects

- Target statement:
  `manuscript/editorial/solver_dossiers_20260824/xia_conjecture_8_8_statement.txt`
- Target-statement SHA-256:
  `fe2b418a660abe1fcc3e3736d9f659c7c54deef95f92abdbda4d69a78aea91c6`
- Proof packet:
  `manuscript/editorial/solver_dossiers_20260824/xia_conjecture_8_8_repaired_proof_packet.md`
- Proof-packet SHA-256:
  `9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`
- Author-supplied raw `main.tex` SHA-256:
  `9a039a5070d2f82ae258d56eec22c8cb998c473b4234158ac1ddd5ebbef78298`

The raw source received a separate first-pass receipt, but the repaired proof
packet is the controlling mathematical proof object.  The raw pass is not used
to erase the defects found by the human and hostile audits.

## Production result

- Verification service: local production Rethlas
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Run directory:
  `/Users/mingchen/.codex/visualizations/2026/08/20/01a01d3c-132d-7ca3-b98a-59682fe837e7/Rethlas_popovici_local/agents/verification/results/20260824T023833Z_fe2b418a660a`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Failed or blocked items: 0
- Critical errors: 0
- Gaps: 0
- Proof item: `pi_c41c7ec0b7c9768a64d29183`
- Context digest:
  `591fd089caf2052b07bca6883cbeda2ae95d2f39628992ca821a6df88f72591b`
- Adaptive-context digest:
  `09b6d17818c36712d128b791967f9a91f8c8fa957b958c9eb63dda984b6a5c68`
- Item-context digest:
  `3807c39a768aa53d248267d83e0f172a78282adea955bb48591fe606d17b2be3`

The service summary was: “Checked all 1 proof items; 0 item(s) failed or
were blocked.”  No repair hint or expanded proof was requested.

## Audit chain

The controlling proof was also checked in:

- `manuscript/editorial/xia_conjecture_8_8_source_audit_20260824.md`;
- `manuscript/editorial/xia_conjecture_8_8_repaired_hostile_audit_20260824.md`;
- `manuscript/editorial/xia_conjecture_8_8_import4_audit_20260824.md`.

These audits forced the positive-Cao-volume/model-envelope reduction, the
four-inclusion convex sandwich, the tail/order-closure proof of the pointwise
potential sandwich, the rational residual classes, the degenerate
one-dimensional factor, the multigraded irrelevant-torsion explanation, and
the canonical-section proof of the effective-shift body inclusion.

## Exclusion firewall

The proof and every load-bearing source path exclude Xia's erroneous
Deligne-pairing paper arXiv:1710.09731.  No result from that paper is cited or
used, directly or indirectly, in this verification chain.
