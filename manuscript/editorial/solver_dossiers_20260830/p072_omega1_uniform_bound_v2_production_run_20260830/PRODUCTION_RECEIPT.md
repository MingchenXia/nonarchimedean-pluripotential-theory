# Production verification receipt

Date: 30 August 2026

## Verdict

The dependency-closed request returned `verdict: correct`, with zero
critical errors and zero gaps.  The verifier expressly confirmed the
sheaf-theoretic local union at the limit stage, the compact-core finite-rank
argument for each row, the countable supremum and successor step, the
minimality argument, and the continuous-hierarchy identity.

The local production service was configured with `gpt-5.6-sol` and
reasoning effort `xhigh`.  The direct endpoint assigned no run or item
identifier.

## Frozen principal bytes

| role | SHA-256 |
|---|---|
| statement | `37ca59d5bd863e6af4d46ed18d1cf1c4cfcdb45aeeac1f25631fa582750985f8` |
| proof | `9cb9222dbd307d4ff21c0043951a5c0b4a65dec645012fe5e5584b86808a6b5b` |
| independent exact-byte re-audit | `93e04bfd5db84b1649a67b2bc9fb134d33434866de509f7e07cbc2d81483188e` |

The decoded request statement has the same SHA-256 as the principal
statement.  After prepending the v1-to-v2 repair note and independent
re-audit, the decoded materialized proof has SHA-256
`b62d3e957bd9f10fb61ff05fd61b71340109d7c72f033bee64b14aacdd301a30`.
The frozen principal proof is its final exact block.

## Production archive

| file | SHA-256 |
|---|---|
| `request.json` | `befa29ce409a5b20bf3d40acd1adf20c99a599ecab7c3d886b29327676950f11` |
| `response.json` | `d40c473aad890ff6361e637af8219e5f8ed3c09fc6c8beacd77e94e49780fec3` |
| `headers.json` | `226053b84fefdb73d19c1ae547c54425604190f55d4d026f5a9f46ab061d064c` |

The HTTP status was 200.  No repair hint, critical error, or gap was
returned.

## Scope consequence

For every CLD affine `G`-tropical space,
`Psh_{X,omega_1}=Psh_X` and
`CPsh_{X,omega_1}=CPsh_X`.  This supplies one universal ordinal bound and
retires the literal P07.2 atom.  It does not supply a finite or fixed
countable bound and does not prove first-stage collapse; P07.1 remains
active.
