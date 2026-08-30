# Source and hostile audit

Status: isolated audit of `candidate_statement.tex` and
`candidate_proof.tex`; not a production verification receipt.

## Frozen primary/local inputs

| input | SHA-256 |
|---|---|
| CLD 2025 extracted text | `24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727` |
| existing exact infinite-star statement | `99c1a6a6a712005e73ee3b7cdae297606895b22ce79c80a6411dfd7f4863c963` |
| existing exact infinite-star proof | `ca49ad210cf8e64100cc00c31c16a76f207ecd0d4b37dc365e8e1c61ce903090` |
| fixed-core statement | `b29ccabac98982c239fcedcc34a701c9a9bb98ca95710d6ed7fbaa3f0f96e4d9` |
| fixed-core proof | `7677ba46620cc4cef8a74d502cdf9fde344e045b04bbc66a4274a5c20b1838c2` |

## Source checks

1. CLD Section 6.7.3 says that a centre neighbourhood has only finitely
   many branches which are not full.  The `U_n` in the statement are legal
   standard open neighbourhoods.
2. On a full branch, a CLD-smooth function is constant near minus infinity.
3. Near the centre, only finitely many branches of a smooth function fail to
   be both full and constant, and the finite sum of centre derivatives is
   zero.
4. The exact infinite-star packet, already source-audited and production
   verified, identifies smooth psh positivity with branchwise nonnegative
   second derivative in this model.
5. The new proof uses precisely those four rules and no quotient-topology,
   ambient-star, or unproved analytic-realization substitution.

## Hostile tests

### Could the common neighbourhood be nonstandard?

No escape.  Every open neighbourhood of the centre contains a standard
one.  Restrict all hypothetical representatives to it and use its finite
exceptional set.

### Could equality of germs fail to determine the centre derivative?

No.  Equality of germs gives equality of branch profiles on a collar of the
centre, so their ordinary derivatives at zero agree.

### Could a convex full-branch profile have derivative minus one at zero
while being constant near minus infinity?

No.  Its derivative is zero on the constant collar and nondecreasing on the
finite stratum.  Hence its terminal derivative is nonnegative.

### Is the exceptional profile `-t` convex and legal?

Yes.  Its second derivative is zero.  Its branch is truncated to `(-1,0]`,
so the CLD full-endpoint collar condition does not apply.

### Is the positive branch profile genuinely smooth at minus infinity?

Yes.  The chosen derivative `q` vanishes on `(-infinity,-2]`, so `psi` is
exactly constant there.

### Does adding a constant and scaling preserve psh?

Yes.  Constants have zero Hessian and positive scaling preserves positivity.
The lower bound `f_n >= -2` makes `f_n+3` strictly positive, so multiplication
by the decreasing positive scalars `2^{-k}` is pointwise decreasing.

### Does the no-common-domain argument survive the added constant/scaling?

Yes.  The centre derivative on `b_n` becomes `-2^{-k}`.  Taking `k=1`
already contradicts convexity on any full `b_n`.

### Does the construction prove a rank-two function?

No.  Every row limit is zero, the outer limit is zero, and zero is smooth.
The statement and memo explicitly firewall this point.

### Can the bad germ be the germ of a psh section on the whole star?

No.  The full branch `b_n` would have a negative centre derivative, contrary
to the same convexity and endpoint-trace argument.  This is exactly why the
construction cannot be promoted to a hierarchy counterexample by simply
declaring the `f_n` global.

## Verdict

The candidate is internally consistent and source-legal as a counterexample
to **automatic common representatives for a countable family of smooth psh
germs**.  It is not evidence of a later CLD closure rank.  Production Rethlas
verification remains mandatory before any live theorem/example integration.
