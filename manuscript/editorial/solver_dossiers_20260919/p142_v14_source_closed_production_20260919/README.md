# P14.2 V14 source-closed production verification

Date: 19 September 2026.

This dossier archives the initial source-closed production review of the V14
packet.  The target files are byte-identical to the V14 preproduction release:

| file | SHA-256 |
| --- | --- |
| `STATEMENT.tex` | `cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2` |
| `PROOF.tex` | `7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac` |
| `EXAMPLE.tex` | `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f` |

`materialize_packet.py` verifies those target hashes and the five full
source-file hashes pinned by V14, then emits the seven cited physical-line
ranges in `SOURCE_EXTRACTS.txt`.  The production request prepends those
extracts to the exact proof.  Its proof-field SHA-256 is
`76e91218db89f4ec02063ebc0521f712bc335a2c0cf5acaf6ee7d92810df13f2`.

The isolated verifier used `gpt-5.6-sol` at `xhigh`.  It returned final
`correct` for item `pi_786d6710873ea471db69e4e0`, with zero critical
errors and zero gaps.  The request, response, and HTTP headers are preserved
under `VERIFICATION_RUN_20260919/`; `RESULT.md` records the exact
attestations and integration boundary.

This receipt establishes only the frozen V14 packet.  A later combined
exact-live audit found that its proof did not display the local
quasi-psh-to-psh bounded-perturbation reduction needed before applying DEL00
subadditivity.  The live proof was repaired, and the exact-current V15 packet
in `../p142_v15_qpsh_repair_production_20260919/` supersedes this receipt as
the retirement gate for P14.2.  This dossier is retained as an immutable
history of the earlier review.
