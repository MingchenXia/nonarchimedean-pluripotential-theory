# P14.8 v3 external-review input audit

## Exact candidate boundary

The review statement is a Markdown rendering of the v2 statement bytes
(`PROPOSED_STATEMENT.tex`, SHA-256
`9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715`).
The review proof is a Markdown rendering of v3: it changes only the Cantor
initial-index block in v2 `PROOF.tex` (SHA-256
`adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9`)
through `V2_TO_V3.patch`. The resulting authoritative TeX proof has SHA-256
`94e6efde9dc8e14bb90ae8b63a3cfa0b0f53b024210e570e29b0b67bd450b47b`.

The Markdown files in this directory are the exact submission inputs:

| Input | SHA-256 |
| --- | --- |
| `VERIFICATION_STATEMENT.md` | `8887cb1fdb9620b0bef7b972321eb4814142d85b118a1c52c0b72b4dcf6cd532` |
| `VERIFICATION_PROOF.md` | `cb5bc46223402afc095f3f0c59fce57399753d6c77aecf0272b25cd7495a1d1b` |

The verification receipt records these values again with the service response.

## Source dependency

The attached dependency is the frozen Chapter 51 source-stage extract
`p148_ch51_dependency_v3.txt`, SHA-256
`c2404ea689ed09cf80fb8059145bc74bab123fd39c7e1d3b70f2f37b4c484fce`.
It supplies the imported $\mathcal I$-envelope/projection, Lelong and strong
openness package, polar-Cantor construction, Green-potential computation,
and nonpluripolar-product facts used by the proof.

The current-source rebase record
`../p148_v3_current_source_rebase_20260908/VALIDATION.md` binds those inputs
to present Chapter 51 spans. In particular, the Cantor/Green span is the
exact v3 repair. This is a provenance packet for external review, not a claim
that any remaining production or integration gate has passed.
