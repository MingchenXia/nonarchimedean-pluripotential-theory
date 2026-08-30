# Production verification receipt

Date: 30 August 2026

## Verdict

The dependency-closed source-aware request returned `verdict: correct`,
with zero critical errors and zero gaps.  The verifier checked thirteen
proof-item groups and fourteen external-reference groups.  Its summary
expressly confirms the formal-twistor construction, connectedness,
analytic Picard bridge, admissible blow-up and divisorial metric
calculation, and the global-psh/global-dpsh constancy argument.

The local production service was configured with `gpt-5.6-sol` and
reasoning effort `xhigh`.  The direct endpoint assigned no run or item
identifier, so the archive hashes below are the controlling receipt.

## Frozen principal bytes

| role | SHA-256 |
|---|---|
| statement | `1e9b7c31a70c55f407de07d76c67d6912e61e1673ef81c66c60789afd2202d2f` |
| proof | `78fab726abcdfb3086988150359568ccd8a9b29d63c3a94e0c513f14b9fc148c` |
| independent hostile-audit receipt | `3bfc1f94ce5f5aee981281e6a4f292ccbd30b79b3a6d264319d3271620c9a4c0` |

The decoded request statement has the same SHA-256 as the frozen principal
statement.  After prepending the primary-source locators, source matrix,
hostile-audit obligations, and independent audit receipt, the decoded
materialized proof has SHA-256
`596198e4cabbb256f949ebad7498dee6880353d27b619e4488a999eb93ec37d2`.
The frozen principal proof occurs as its final exact block.

## Production archive

| file | SHA-256 |
|---|---|
| `request.json` | `7916d3750482946cd933591a3f836d6e3b308dcbddb8a24a26c836de41d73e1b` |
| `response.json` | `f5e780184515b39bbb7d4fd099366da98b96a74896fa1d693b43f66cce19d57e` |
| `headers.json` | `29d3ae7255f5ee74b5deca5d6cc3c297ec382d97c8d078731eecc273940c1d45` |

The HTTP status was 200.  The response contains no repair hint, critical
error, or unresolved gap.

## Scope consequence

The exact statement and proof are authorized for live-book integration.
They disprove only the second question in CLD Remark 17.8.10: the extension
of Corollary 17.8.9 from analytifications of projective varieties to proper
strict analytic spaces possessing a formal model with projective special
fibre.  They do not answer the first continuous-psh/global-psh question and
do not assert that the constructed parlinear metric is psh.  P08.2 may be
retired negatively; P08.1 remains active.
