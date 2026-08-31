# Uniform full-fibre extension and a constant-field envelope bridge

Date: 2026-08-31. Authoring agent: `/root/p082_independent_reaudit`.

**RESEARCH CANDIDATE ONLY.** No independent audit, production acceptance,
live integration, inventory closure, or novelty/priority claim. The new
argument remains conditional on the explicitly stated trivial-field EP
input. No old rejected curve theorem is a dependency.

The packet proves two proposed statements in full:

1. Every real-weighted FS potential in `[-M,0]` on a constant polarized
   variety over `k((t))` extends EXACTLY to weighted FS data on
   `X x P1` in the one class `L + C O(1)`, with integer
   `C >= max(1,M)`. Its global bounds are `[-C,1]`, and its normalized
   weights are uniformly in `[-C,1)`. Changing a fixed FS reference adds
   only a fixed oscillation bound to the choice of C.
2. Assuming the trivial-field envelope property on that product in these
   ample classes, the full envelope property follows for the decreasing-FS
   metric class on the fixed ample `L_K`. The target definition is exactly
   Boucksom--Eriksson Definition 7.2, with identically minus infinity
   excluded and metrics expressed as relative potentials.

The mechanism is coefficient integrality at a single generic Gauss point,
strict uniform tail truncation, weighted padding at both base endpoints,
a full-fibre collar with uniform scaling control, and a product-net
argument. It retains all fibre information and is compatible with the
earlier Gauss-trace reconstruction obstruction.

## Files

- `statement.tex`, `proof.tex`: complete candidate principal inputs.
- `SOURCE_LEDGER.md`: exact source versions, locations, scope, dependency
  interfaces and proof-risk checklist.
- `references.bib`: isolated bibliography, with version-specific citations.
- `SHA256SUMS`: principal/support files and exact local primary inputs.

This packet has not been compiled or visually checked as a PDF. It uses
ordinary AMS theorem/proof environments and `cref`/`eqref`; a future
harness must load amsmath, amssymb, amsthm, hyperref and cleveref and define
proposition and theorem environments. No live book macros or bibliography
were edited.

## Coordination and authorization

The parent independently suggested the integral-section/tail observation,
identified the central-fibre padding problem, and supplied the collar and
product-net reductions. The author independently found that negative FS
weights solve the padding problem and independently reached the collar
argument before receiving the parent's matching observation. Source
checks and the written synthesis are not an independent audit of that
shared construction.

The first normal apply_patch creation attempt timed out in automatic
approval review. The single allowed normal retry succeeded. There was no
permission bypass, alternative write mechanism, live mutation or
production call. Earlier blocked unrelated manifests were not retried.

## Deliberately excluded next steps

No theorem for a nonconstant family over `k(t)` or its completion is
included. Such an extension would require a separately audited integral
section-lattice identity and uniformly controlled generation of the
relative section algebra. No arbitrary complete valued-field theorem,
real numerical-class extension, or CLD/BFJ comparison is inferred.
Continuous-obstacle continuity is not used and is not asserted here.
