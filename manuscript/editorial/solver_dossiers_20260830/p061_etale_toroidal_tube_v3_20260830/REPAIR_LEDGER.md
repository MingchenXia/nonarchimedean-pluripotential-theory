# Repair ledger: P06.1 v2 to v3

The controlling independent audit is

`../p061_etale_toroidal_tube_v2_independent_audit_20260830/INDEPENDENT_EXACT_BYTE_HOSTILE_AUDIT_20260830.md`,

SHA-256
`d884005655ff604eea9e45d90c243f8751ed8505d92700033d90ac2ef8ae4d10`.
It returned `FAIL-CLOSED`, zero critical errors, one mathematical/proof gap,
zero source-scope gaps, zero byte mismatches, and zero compile failures.

The frozen v2 principal hashes are preserved:

| role | SHA-256 |
|---|---|
| v2 statement | `ad8ecd1a3f1197e9ba2234595f4f43e40099bcd5b04cfe925a53865f452b94bd` |
| v2 proof | `b18a0274e52e6f74ede7ca22e1d9d70ed68bff076f6768e15ff2b972d5c4fb96` |

## The sole mathematical repair

The proposition permits `rank(N)=0`.  V3 now separates this case explicitly:

```text
N=0, rho={0}, S={0}, Z=Spec K,
U_k=M(K), q=0, R_k=K, A=A_n=B, J=0.
```

It follows directly that every coefficient error
`a^circ=a-iota epsilon(a)` is zero in every `A_n`.  Hence the finite
coefficient maximum in the standard-etale lemma is zero for every `n`, and
no maximum over an empty family of monoid generators is formed.  The
positive-rank normalized-semigroup estimate is unchanged.

The source-Zariski corollary now says explicitly that its dense torus orbit
has transverse pointed factor `Spec K` and is handled by this rank-zero
branch.

## Mechanical changes only

Research labels and filenames were advanced from `v2` to `v3`, and metadata
was updated to describe the new release and its audit gate.  All other
statement/proof mathematics, external citations, internal dependencies, and
scope firewalls are retained from v2.  The three quasi-smooth dependency
excerpts remain byte-identical to the already verified ranges.

V3 remains quarantined until a fresh independent exact-byte audit and a
fresh dependency-closed production verification both pass.
