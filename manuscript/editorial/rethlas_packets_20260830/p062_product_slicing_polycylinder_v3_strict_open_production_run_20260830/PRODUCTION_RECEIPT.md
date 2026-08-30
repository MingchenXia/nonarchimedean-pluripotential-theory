# Production verification receipt

Date: 30 August 2026

## Verdict

The dependency-closed strict-open request returned `verdict: correct`, with
zero critical errors and zero gaps.  The verifier expressly confirmed the
rational-centred trace and descent inputs, the finite-flat trace and
arbitrary-field disc inputs, exact restriction of the zero-Hessian current
to every product fibre, arbitrary-field strict-open annulus affinity, and
joint affinity on strict-open polycylinders.  It also confirmed that the
scope firewall excludes the closed and half-closed endpoint assertions that
had been rejected from v2.

The local production service was configured with `gpt-5.6-sol` and
reasoning effort `xhigh`.  The direct endpoint assigned no run or item
identifier, so the archive hashes below are the controlling receipt.

## Frozen principal bytes

| role | SHA-256 |
|---|---|
| v3 strict-open statement | `985be85d97b583f72be5cee65988df6f31c1edb49a685121b834df179fa87fda` |
| v3 strict-open proof | `42b592bf8ac26ed46c36928e5e90272225ae6883bd2bfe62d3ff2840f01d46e5` |
| independent exact-byte audit | `016e189d71d2d6694650b1e1c2d7b6eb9b0632a61a049ccb8f0bca1feb9a6d3d` |

The verified dependencies have statement/proof SHA-256 pairs
`7510083fecda2d561c4ce2a1b35d08377268ef48adda2b242172428dbd39caec` /
`77a013d4e655d288d8803c9650df5446bed570de2644591edddfc116c323eab2`
and
`67a8d8a21e23cb34cf9b8f6685efbf2c9eaa6ff484b3696cbc1867a8940e095c` /
`479643ee3aa534bbfc98adcf69837356d3cd8eff22d92accd1319aabb049553e`.
After prepending them, the decoded materialized statement and proof have
SHA-256 values
`01f77980b905d53e93d82cf353c2a713be720288f02cd2d0e588b4c03ae26458`
and
`e6cbd94578bf3d56c4d086913bf9e83f1912d49094d6030e13724d9a442160de`.
The v3 principal files are their final exact blocks.

## Production archive

| file | SHA-256 |
|---|---|
| `request.json` | `6261b61bc49669a74a6eee4a2d834c25c8741bef59b084b81eaa684629f2d604` |
| `response.json` | `c8c951075a574c6a3badde2e2a22942718616cd21da0144cb8a983bc3cac822f` |
| `headers.json` | `dcac7f45ad5464d4599d880862ce27c9c98e18cc3f4060bbf250426080c7fb45` |

The HTTP status was 200.  No repair hint, critical error, or unresolved gap
was returned.

## Scope consequence

The exact v3 statement and proof are authorized for live-book integration.
Over every complete non-Archimedean field with nontrivial absolute value,
they prove exact fibre slicing on standard strict-open products, affinity on
a standard strict-open annulus, and the classification
`h = c + sum_j lambda_j log|S_j|` on every standard strict-open
polycylinder.  They make no assertion for a closed or half-closed domain,
for a non-strict endpoint, or for an arbitrary nonproduct analytic germ.
Thus P06.2 is narrowed but remains active, and the active-atom count does not
change.
