# Author report: repaired Chapter 51 comprehensive ledger production packet

Status: `REPAIRED_PACKET_AUTHORED_NOT_INDEPENDENTLY_AUDITED_NOT_SUBMITTED`.

The production target is the exact ordered pair `STATEMENT.tex`,
`PROOF.tex`.  The Statement field is byte-identical to the independently
audited 150-line `LOCAL_CONSTRUCTION_REPLACEMENT.tex`; the Proof field is
byte-identical to the independently audited 420-line
`LEDGER_REPLACEMENT.tex`.  The unusual split is deliberate and is preserved
without extraction, reformatting, or relocation.

The source bundle pins BEGZ arXiv:0812.3674v2, Bedford--Taylor 1982, and DDNL
arXiv:1705.05796 as exact PDF/text pairs and provides two exact routes to the
candidate itself.  The independent hostile audit of v1 proved that every raw
derivative was made by `pdftotext -layout`, although v1 falsely declared plain
`pdftotext` for BEGZ and Bedford--Taylor.  This sibling declares the exact
command for all three PDFs.  Its checker executes that command, reproduces
each raw hash, and proves that the bundled derivative is exactly the raw bytes
followed by one LF after the terminal form-feed.

The second v1 packet defect was a split line-number domain.  This sibling uses
one-based LF-only addressing everywhere: only byte `0x0a` separates lines and
form-feed byte `0x0c` remains within its line.  Each of the thirteen external
ranges has an exact content hash.  Exact anchor hashes additionally bind BEGZ
Definition 1.1 to LF line 211, Bedford--Taylor Theorem 6.9 to LF line 1107,
and DDNL Theorem 1.1 to LF line 81.  The checker and regression suite reject
form-feed-aware line semantics and any runtime/LF line-number split-brain in
route metadata.

Only Proof lines 317--327 import DDNL Theorem 1.1.  The packet explicitly
routes its less-singular orientation and its `p<n` specialization.  Statement
lines 1--150 and Proof lines 51--316 and 328--420 are internally supplied
mathematics that a production verifier must check in full, including both
potential-choice mass inequalities, the common-exhaustion current, local
finiteness, closedness, and modification pullback/pushforward.

No production submission was made.  No final-path smoke was run.  No live
manuscript or inventory file was changed and no git operation was performed.
No runtime stage is bundled or authorized: the known failed-runner blocker is
outside this packet and must be repaired and independently audited in a
separate sibling.  This packet is prepared only for an independent hostile
audit and, if that passes, later attachment to that separately audited
final-path release.

## Authored hash ledger

The read-only packet checker parses every row and checks it against the actual
file bytes.

| file | SHA-256 |
|---|---|
| `PRODUCTION_REQUEST.json` | `110bee13be427c9ec4cb1b6f684514c8aa2432811bb6d44fe3b125185518dd1c` |
| `PROOF.tex` | `187ef5530c9baf375cab4d15108a4447f3ddb3cc4c0b2780a7bf8d7cd2f33d70` |
| `README.md` | `9713fab6e88606a8f44d0e5cf1d64693f17a4dfa577a9cecbc197e37071d267e` |
| `REPAIR_LEDGER.json` | `bd5a6d6f6cde7581b0db693f7fb19248369b50ca043248b3bb4eda9a3fa0f37a` |
| `REQUEST_CONTRACT.md` | `117a1796c124273c066cf0a2f0643b059589c62c195ba3c9871ce842342268fc` |
| `SOURCE_ROUTES.json` | `0e759a8aa997ecd047328e8e43d493b62fec91c7f6566908e3ce0b1c1db75ff4` |
| `STATEMENT.tex` | `9ff17ccf6ecafdaedf746e8472671bbd9436cf5661667e27815e1a1d39698575` |
| `audit/INDEPENDENT_AUDIT.md` | `03dcce4596c3ceb3a8ed25a7ad755cde2c7feea1fa38a30f116bacd4447b54ef` |
| `audit/INDEPENDENT_AUDIT_RESULT.json` | `0e10ec20f585cbcb4158db8415620e75fd8fec0b3d30de1a3cccef67d3be73e6` |
| `audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/SHA256SUMS` | `173fc76c8dbe077eaa61fa60d89c1d586d2405bf01bc238bcf92f5415aff0a19` |
| `check_packet.py` | `3b2a482b70f23c4d85eb3a8b981bf7a07ed7198b8bfdd666b21830f3a59c8706` |
| `source_exact/LEDGER_REPLACEMENT.tex` | `187ef5530c9baf375cab4d15108a4447f3ddb3cc4c0b2780a7bf8d7cd2f33d70` |
| `source_exact/LOCAL_CONSTRUCTION_REPLACEMENT.tex` | `9ff17ccf6ecafdaedf746e8472671bbd9436cf5661667e27815e1a1d39698575` |
| `tests/test_packet.py` | `cdc8fb6c5da9ab235566670a6853b362989c7b4f32aac501427907311d2e3b38` |
