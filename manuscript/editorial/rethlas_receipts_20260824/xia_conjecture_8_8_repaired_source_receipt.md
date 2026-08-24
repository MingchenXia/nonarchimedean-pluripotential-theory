# Xia Conjecture 8.8: repaired-source production receipt

Date: 24 August 2026.

## Exact objects

- Target statement:
  `manuscript/editorial/solver_dossiers_20260824/xia_conjecture_8_8_source_statement.txt`
- Target-statement SHA-256:
  `b8adabf0730c0ffd35204d72f3667263e250488da23c144c9d8ebeece55fe91a`
- Repaired author source:
  `author_source_repairs/Mixed_volumes_of_partial_Okounkov_bodies/main.tex`
- Repaired-source SHA-256:
  `5746eb011417caecfa876c05c6c74fb548e2ae9d086c1441189bbcad02a96594`
- Repaired bibliography SHA-256:
  `e3e48c5c503cd6cdaa7bb2e02bdbc02767031e3084c52eff7415258d9483813e`

The proof object submitted to Rethlas was the complete frozen `main.tex`,
not an excerpt or paraphrase.  This source-level receipt supplements the
controlling repaired-proof receipt; it does not replace its mathematical
audit chain.

## Production result

- Verification service: local production Rethlas
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Run directory:
  `/Users/mingchen/.codex/visualizations/2026/08/20/01a01d3c-132d-7ca3-b98a-59682fe837e7/Rethlas_popovici_local/agents/verification/results/20260824T032252Z_b8adabf0730c`
- Verification status: `final`
- Verdict: `correct`
- Checked proof items: 1
- Failed or blocked items: 0
- Critical errors: 0
- Gaps: 0
- Proof item: `pi_b80d4a29bb37992748e896a6`
- Aggregate context digest:
  `fd4588256a3682f58b525f88ce4289d20806a11590cafe5ef30b2d70483a541a`
- Adaptive-context digest:
  `f93d73c0b08f46c520b1d7cffe8960cd9499e557c825d0b8de11086cffbeb143`
- Item-context digest:
  `fd381891db033df626e1da43e2ba68e75dd58dcbc6cd8e68deab2e6ec5f19263`
- Manifest SHA-256:
  `06dbca8a1c6ced3e990f92eef7106663f5ac520e88315c0cd5fc11670f716e86`
- Aggregate verification SHA-256:
  `ca35755450d84290fb03884cdfad6e50273d14c956cb7f7f8fbc52eeffd42d39`

The service summary was: “Checked all 1 proof items; 0 item(s) failed or
were blocked.”  No repair hint or expanded proof was requested.

## Independent checks and installation

The exact source snapshot also received the hostile audit recorded in
`manuscript/editorial/xia_conjecture_8_8_repaired_source_hostile_audit_20260824.md`,
whose verdict is PASS with no must-fix finding.  After preserving the raw
source and bibliography as hash-named backups, the repaired source was
installed in
`/Users/mingchen/Downloads/Mixed_volumes_of_partial_Okounkov_bodies`.
It was rebuilt there to a 12-page A4 PDF with no unresolved reference,
unresolved citation, LaTeX error, overfull box, or underfull box.

## Exclusion firewall

The source, proof, bibliography changes, and verification chain exclude
Xia's erroneous Deligne-pairing paper arXiv:1710.09731.  No result from that
paper is cited or used, directly or indirectly.
